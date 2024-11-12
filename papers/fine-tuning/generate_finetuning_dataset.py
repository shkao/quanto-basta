import glob
import re
import json
import pymupdf4llm
from openai import OpenAI

client = OpenAI()


def extract_pdf_text(pdf_file):
    pdf_text = pymupdf4llm.to_markdown(pdf_file)
    pdf_text = re.sub(r"\[\d+(?:,\s*\d+)*(?:–\d+)?\]", "", pdf_text)
    pdf_text = re.split(r"## References", pdf_text)[0]
    return pdf_text


def read_deepdive_text(pdf_file):
    with open(pdf_file.replace(".pdf", "_deepdive.md"), "r", encoding="utf-8") as file:
        return file.read()


def create_data_entry(pdf_text, deepdive_text):
    return {
        "messages": [
            {
                "role": "system",
                "content": "You are an expert assistant specializing in generating insightful and "
                "comprehensive blog posts. Your task is to create engaging and informative "
                "content based on the provided academic paper, ensuring clarity and depth "
                "for the readers.",
            },
            {
                "role": "user",
                "content": (
                    f"Generate a comprehensive and engaging deep dive blog post summarizing the "
                    f"key insights and findings from the following academic paper:\n\n{pdf_text}"
                ),
            },
            {
                "role": "assistant",
                "content": deepdive_text,
            },
        ]
    }


def prepare_training_dataset(input_dir="data", output_filename="deepdive.jsonl"):
    pdf_files = glob.glob(f"{input_dir}/*.pdf")
    dataset = []

    for pdf_file in pdf_files:
        pdf_text = extract_pdf_text(pdf_file)
        deepdive_text = read_deepdive_text(pdf_file)
        data = create_data_entry(pdf_text, deepdive_text)
        dataset.append(data)

    with open(output_filename, "w", encoding="utf-8") as outfile:
        for entry in dataset:
            json.dump(entry, outfile)
            outfile.write("\n")


def upload_and_train_model(output_filename):
    with open(output_filename, "rb") as file:
        uploaded_file = client.files.create(file=file, purpose="fine-tune")
    client.fine_tuning.jobs.create(
        training_file=uploaded_file.id, model="gpt-4o-mini-2024-07-18"
    )


def main():
    prepare_training_dataset()
    upload_and_train_model("deepdive.jsonl")


if __name__ == "__main__":
    main()
