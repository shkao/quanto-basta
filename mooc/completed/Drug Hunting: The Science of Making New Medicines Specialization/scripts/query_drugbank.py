"""Drug Information Extraction and Processing Module.

This module provides functionality to extract drug names from text queries,
retrieve DrugBank IDs, and fetch detailed drug information from DrugBank's website.
"""

import argparse
import json
import ollama
import os
import pandas as pd
from scrapegraphai.graphs import SmartScraperGraph


def extract_drug_name(question):
    """Extract a drug name from a given text question.

    Uses the Ollama LLM to identify and extract drug names from natural language
    questions.

    Args:
        question (str): The input text containing a drug name.

    Returns:
        str: The extracted drug name.
    """
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": (
                    f"Extract the drug name in this sentence, return only drug name: "
                    f"{question}"
                ),
            }
        ],
    )
    return response["message"]["content"]


def get_drugbank_id(drug_common_name):
    """Retrieve the DrugBank ID for a given drug name.

    Looks up the DrugBank ID in a local vocabulary CSV file using the common name
    of the drug.

    Args:
        drug_common_name (str): The common name of the drug to look up.

    Returns:
        str: The DrugBank ID if found, None otherwise.
    """
    base_dir = os.path.dirname(__file__)
    vocabulary_df = pd.read_csv(os.path.join(base_dir, "drugbank_vocabulary.csv"))
    drug_common_name = drug_common_name.lower()
    result = vocabulary_df[vocabulary_df["Common name"].str.lower() == drug_common_name]
    return result["DrugBank ID"].iloc[0] if not result.empty else None


def main():
    """Process drug-related queries and retrieve information from DrugBank.

    Command-line interface for processing drug-related questions and retrieving
    information from DrugBank's website. Extracts drug names, looks up their
    DrugBank IDs, and uses a smart scraper to fetch relevant information.

    Command-line Arguments:
        question: The question containing the drug name.
        fragment: Optional fragment identifier for the DrugBank URL.
    """
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
