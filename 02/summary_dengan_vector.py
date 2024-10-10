# from langchain.chains.question_answering import load_qa_with_sources_chain
from langchain.chains import create_retrieval_chain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.chains.summarize import load_summarize_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

from rich import print
from dotenv import load_dotenv
load_dotenv()

# Load and split the PDF file
print("[yellow]Loading PDF File[/]")
pdf_file_path = "D:\\course\\chatbot\\data\\pemilu 2024.pdf"
pdf_loader = PyPDFLoader(pdf_file_path)
docs = pdf_loader.load_and_split()

# Initialize the LLM (Language Model)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", max_retries=2)

print("[red]Splitting...[/]")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

print("[green]Store to DB[/]")
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

# buat question-answering chain
system_prompt = (
    "Kamu adalah asisten yang menjawab setiap pertanyaan. "
    "Gunakan kalimat berikut sebagai bahan untuk menjawab pertanyaan."
    "Jawab maksimal 3 kalimat, dan pastikan jawaban tetap singkat"
    "Jika tidak tahu jawabannya, jawab tidak tahu dan jangan cari dari luar dokumen."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

result = rag_chain.invoke({"input": "kapan pemilu dilaksankan"})
print(result["answer"])

