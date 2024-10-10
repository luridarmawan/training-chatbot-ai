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

persist_directory = "D:\\course\\chatbot\\02\\vector"

# Inisialisasi LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", max_retries=2)

# load DB
print("[green]Load DB[/]")
vectorstore = Chroma(persist_directory=persist_directory, embedding_function=OpenAIEmbeddings())
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

