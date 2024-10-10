from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
load_dotenv()

pdf_file_path = "D:\\course\\chatbot\\data\\pemilu 2024.pdf"
pdf_loader = PyPDFLoader(pdf_file_path)
docs = pdf_loader.load_and_split()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

qa_chain = load_qa_with_sources_chain(llm)

while True:
    user_input = input("Pertanyaan: ")
    if user_input.lower() in ("", "exit", "q", "x"):
        break
    else:
        qa_result = qa_chain.invoke({"input_documents": docs, "question": user_input})
        print(qa_result['output_text'])
    
