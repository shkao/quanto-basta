import os
import re
import argparse
import pymupdf4llm
from openai import OpenAI
from docling.document_converter import DocumentConverter


def extract_pdf_text(pdf_file):
    try:
        pdf_text = pymupdf4llm.to_markdown(pdf_file)
    except Exception:
        converter = DocumentConverter()
        result = converter.convert(pdf_file)
        pdf_text = result.document.export_to_markdown()

    pdf_text = re.sub(r"\[\d+(?:,\s*\d+)*(?:–\d+)?\]", "", pdf_text)
    return pdf_text


def generate_paper_deepdive(pdf_text, model=None):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    model = model or os.getenv("OPENAI_FT_MODEL") or "gpt-4o-mini"

    completion = client.chat.completions.create(
        messages=[
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
        ],
        model=model,
    )
    return completion.choices[0].message.content


def main():
    parser = argparse.ArgumentParser(
        description="Process a PDF file to generate a deep dive blog post."
    )
    parser.add_argument(
        "pdf_file", type=str, help="Path to the academic paper PDF file"
    )
    args = parser.parse_args()

    try:
        pdf_text = extract_pdf_text(args.pdf_file)
        deepdive_content = generate_paper_deepdive(pdf_text)
        print(deepdive_content)
    except IndexError as e:
        print(f"An error occurred while processing the PDF: {e}")
        return


if __name__ == "__main__":
    main()
