import argparse
import os
import re


def extract_and_create_files(markdown_file):
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
    parser = argparse.ArgumentParser(description="Process a markdown file.")
    parser.add_argument("markdown_file", type=str, help="Path to the markdown file")
    args = parser.parse_args()

    extract_and_create_files(args.markdown_file)


if __name__ == "__main__":
    main()
