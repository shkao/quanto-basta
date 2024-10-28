"""Script to extract headers from markdown files and create transcript files.

This script processes a markdown file, extracts level 2 headers (## Header), and creates
individual transcript files for each header, excluding welcome/farewell headers.
"""

import argparse
import os
import re


def extract_and_create_files(markdown_file):
    """Extract headers from markdown file and create individual transcript files.

    Processes a markdown file to find all level 2 headers (starting with ##) and creates
    separate text files for each header in a 'transcripts' directory. Headers containing
    'welcome' or 'farewell' (case-insensitive) are skipped.

    Args:
        markdown_file (str): Path to the input markdown file to process.

    Raises:
        ValueError: If the input file doesn't have a .md extension.

    Example:
        >>> extract_and_create_files("lecture.md")
        Found 5 headers in the markdown file.
        Directory 'transcripts' created or already exists.
        Created file: transcripts/01_Introduction.txt with header: Introduction
        ...
    """
    if not markdown_file.endswith(".md"):
        raise ValueError(
            "The input file must be a markdown file with a '.md' extension."
        )

    with open(markdown_file, "r") as file:
        content = file.read()

    headers = re.findall(r"^## (.+)$", content, re.MULTILINE)
    print(f"Found {len(headers)} headers in the markdown file.")
    os.makedirs("transcripts", exist_ok=True)
    print(f"Directory 'transcripts' created or already exists.")

    for index, header in enumerate(headers, start=1):
        if re.search(r"\b(welcome|farewell)\b", header, re.IGNORECASE):
            continue
        sanitized_header = re.sub(r"[\/,]", "", header)
        filename = f"{index:02d}_{sanitized_header}.txt"
        filepath = os.path.join("transcripts", filename)
        with open(filepath, "w") as f:
            f.write(header)
        print(f"Created file: {filepath} with header: {header}")


def main():
    """Parse command line arguments and execute the main script functionality."""
    parser = argparse.ArgumentParser(description="Process a markdown file.")
    parser.add_argument("markdown_file", type=str, help="Path to the markdown file")
    args = parser.parse_args()

    extract_and_create_files(args.markdown_file)


if __name__ == "__main__":
    main()
