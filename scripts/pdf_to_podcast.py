import argparse
import asyncio
from loguru import logger
from litellm import completion, completion_cost
from langchain_community.document_loaders import PyPDFLoader

CONVERSION_RATE_USD_TO_TWD = 31.0
total_cost_usd = 0.0


def get_chat_completion(prompt, model="gpt-4o-mini"):
    global total_cost_usd
    messages = [{"content": prompt, "role": "user"}]
    try:
        response = completion(model=model, messages=messages)
        cost_usd = completion_cost(completion_response=response)
        total_cost_usd += float(cost_usd)
    except Exception as e:
        logger.error(f"Error generating summary: {e}")
        raise

    return response["choices"][0]["message"]["content"]


def sanitize_text(text):
    prompt = (
        f"Clean up this messy PDF text: fix formatting, remove extra spaces, and "
        f"ensure it reads smoothly. Do not change any wording or content. Return "
        f"only the cleaned text in a simple format. Here is the text to clean:\n\n"
        f"{text}"
    )
    return get_chat_completion(prompt)


async def load_pages(loader):
    all_text = []
    async for page in loader.alazy_load():
        sanitized_content = sanitize_text(page.page_content)
        all_text.append(sanitized_content)
    return "\n".join(all_text)


def main():
    global total_cost_usd
    parser = argparse.ArgumentParser(description="Load PDF file")
    parser.add_argument("file_path", type=str, help="Path to the PDF file")
    args = parser.parse_args()

    loader = PyPDFLoader(args.file_path)
    all_text = asyncio.run(load_pages(loader))

    print(all_text if all_text else "No text loaded.")
    print(
        f"Total cost: ${total_cost_usd:.2f} USD "
        f"({total_cost_usd * CONVERSION_RATE_USD_TO_TWD:.2f} TWD)"
    )


if __name__ == "__main__":
    main()
