import os
import json
import ollama
import pandas as pd
import argparse
from scrapegraphai.graphs import SmartScraperGraph


def extract_drug_name(question):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": f"Extract the drug name in this sentence, return only drug name: {question}",
            }
        ],
    )
    return response["message"]["content"]


def get_drugbank_id(drug_common_name):
    base_dir = os.path.dirname(__file__)
    vocabulary_df = pd.read_csv(os.path.join(base_dir, "drugbank_vocabulary.csv"))
    drug_common_name = drug_common_name.lower()
    result = vocabulary_df[vocabulary_df["Common name"].str.lower() == drug_common_name]
    return result["DrugBank ID"].iloc[0] if not result.empty else None


def main():
    parser = argparse.ArgumentParser(
        description="Process a drug-related question and fragment identifier."
    )
    parser.add_argument(
        "question", type=str, help="The question containing the drug name."
    )
    parser.add_argument(
        "fragment",
        type=str,
        nargs="?",
        default="",
        help="The fragment identifier for the DrugBank URL.",
    )
    args = parser.parse_args()

    drug_name = extract_drug_name(args.question)
    drugbank_id = get_drugbank_id(drug_name)

    if not drugbank_id:
        print(f"No DrugBank ID found for drug: {drug_name}")
        return

    graph_config = {
        "llm": {
            "api_key": os.getenv("OPENAI_API_KEY"),
            "model": "openai/gpt-4o",
        },
        "verbose": True,
        "headless": True,
    }
    smart_scraper_graph = SmartScraperGraph(
        prompt=args.question,
        source=f"https://go.drugbank.com/drugs/{drugbank_id}#{args.fragment}",
        config=graph_config,
    )
    result = smart_scraper_graph.run()
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
