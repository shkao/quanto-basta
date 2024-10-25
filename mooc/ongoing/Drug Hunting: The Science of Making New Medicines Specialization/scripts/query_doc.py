import os
import asyncio
import argparse
from langchain_community.document_loaders import (
    PyPDFLoader,
    WebBaseLoader,
    UnstructuredMarkdownLoader,
)
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate


async def load_document(source):
    if not source:
        raise ValueError("No source provided.")

    loader = None
    if os.path.isfile(source):
        if source.endswith(".pdf"):
            loader = PyPDFLoader(source)
        elif source.endswith(".md"):
            loader = UnstructuredMarkdownLoader(source)
    elif source.startswith("http"):
        loader = WebBaseLoader(source)

    if loader is None:
        raise ValueError("Invalid or unsupported source.")

    docs = await loader.aload() if not source.startswith("http") else loader.load()
    return docs


async def process_question(question, source=None):
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
    docs = await create_vector_store(pages, args.question)
    response = await get_llm_response(docs, args.question)
    print(response.content)


if __name__ == "__main__":
    asyncio.run(main())
