import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI()
result = llm.invoke("siapa presiden indonesia tahun 2026")
print(result.content)
