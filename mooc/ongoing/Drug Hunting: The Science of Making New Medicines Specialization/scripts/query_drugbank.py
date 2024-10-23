import os
import json
import ollama
import pandas as pd
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
    vocabulary_df = pd.read_csv("drugbank_vocabulary.csv")
    drug_common_name = drug_common_name.lower()
    result = vocabulary_df[vocabulary_df["Common name"].str.lower() == drug_common_name]
    return result["DrugBank ID"].iloc[0] if not result.empty else None


def main():
    question = "What is the fu of ibuprofen (acidic)?"
    drug_name = extract_drug_name(question)
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
        prompt=(
            f"{question}\n\n"
            "PPB values are listed as a single value (e.g., 25%), a range (e.g., 20-40%), or a\n"
            "minimum or maximum value (e.g., <25%). Single PPB values can be directly converted to\n"
            "an fu value. For a PPB range, use the average of the range to determine fu. Round\n"
            "the fu to 2 decimal places if necessary. If PPB is reported as a 'less than' (<)\n"
            "or 'greater than' (>) value, use the provided PPB value to calculate fu."
        ),
        source=f"https://go.drugbank.com/drugs/{drugbank_id}",
        config=graph_config,
    )
    result = smart_scraper_graph.run()
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
