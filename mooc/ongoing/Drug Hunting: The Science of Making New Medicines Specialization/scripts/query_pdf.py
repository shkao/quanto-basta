import ollama
import asyncio
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# URLs for drug labels
DRUG_URLS = {
    "atorvastatin": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2009/020702s056lbl.pdf",
    "adalimumab": "https://www.accessdata.fda.gov/drugsatfda_docs/label/2008/125057s0110lbl.pdf",
}


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
    return response["message"]["content"].lower()


async def load_pdf(url):
    if not url:
        raise ValueError("No URL found for the specified drug.")
    loader = PyPDFLoader(url)
    return await loader.aload()


async def process_question(question):
    drug_name = extract_drug_name(question)
    drug_url = DRUG_URLS.get(drug_name)
    return await load_pdf(drug_url)


async def create_vector_store(pages, question):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(pages)
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
    question = "What side effects may occur with adalimumab at a frequency of >10%?"
    pages = await process_question(question)
    docs = await create_vector_store(pages, question)
    response = await get_llm_response(docs, question)
    print(response.content)


if __name__ == "__main__":
    asyncio.run(main())
