from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
load_dotenv()

# pip install pypdf

pdf_file_path = "D:\\course\\chatbot\\data\\pemilu 2024.pdf"
pdf_loader = PyPDFLoader(pdf_file_path)
docs = pdf_loader.load_and_split()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
chain = load_summarize_chain(llm, chain_type="map_reduce")
summary = chain.invoke({"input_documents": docs})
print(summary['output_text'])


terjemahan = llm.invoke("terjemahkan ke dalamm bahasa indonesia:\n" + summary["output_text"])
print(terjemahan.content)
