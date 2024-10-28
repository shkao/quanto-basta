import os
import asyncio
import argparse
import base64
from openai import OpenAI
from langchain_community.document_loaders import (
    PyPDFLoader,
    WebBaseLoader,
    UnstructuredMarkdownLoader,
    TextLoader,
)
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from rich.console import Console
from rich.markdown import Markdown


def get_loader(file_extension):
    loaders = {
        ".pdf": PyPDFLoader,
        ".md": UnstructuredMarkdownLoader,
        ".txt": TextLoader,
    }
    return loaders.get(file_extension)


async def load_document(source):
    if not source:
        raise ValueError("No source provided.")

    if os.path.isfile(source):
        loader = get_loader(os.path.splitext(source)[1])
        if loader is None:
            raise ValueError("Invalid or unsupported file type.")
        return await loader(source).aload()

    if source.startswith("http"):
        return WebBaseLoader(source).load()

    raise ValueError("Invalid or unsupported source.")


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


async def process_image(image_path, question):
    client = OpenAI()
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
    )
    return response.choices[0].message.content


async def process_question(question, source=None):
    if source and os.path.isfile(source):
        if os.path.splitext(source)[1] in [".jpg", ".jpeg", ".png"]:
            return await process_image(source, question)
    return await load_document(source)


async def create_vector_store(pages, question):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(pages)
    vector_store = FAISS.from_documents(chunks, OpenAIEmbeddings())
    return vector_store.similarity_search(question, k=5)


async def get_llm_response(docs, question):
    template = """Answer the question based on the following context:

Context: {context}
Question: {question}

Answer:"""
    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model_name="gpt-4o")
    chain = prompt | llm
    return chain.invoke({"context": docs, "question": question})


async def main():
    parser = argparse.ArgumentParser(description="Process a document and question.")
    parser.add_argument("--source", type=str, help="URL or path of the document")
    parser.add_argument("--question", type=str, required=True, help="Question to ask")
    args = parser.parse_args()

    pages = await process_question(args.question, args.source)
    if isinstance(pages, str):  # If the result is a final answer from process_image
        response = pages
    else:
        docs = await create_vector_store(pages, args.question)
        response = await get_llm_response(docs, args.question)

    console = Console()
    console.print(Markdown(getattr(response, "content", response)))


if __name__ == "__main__":
    asyncio.run(main())
