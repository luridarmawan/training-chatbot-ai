import os
import time
# from transformers import pipeline
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

system_prompt = """
Kamu adalah customer service asistant yang menghadapi keluhan permasalahan pelanggan.
"""
customer_email = """
Permisi Mas. Saya ingin menyampaikan keluhan tentang makanan yang sudah saya pesan.
Saya tadi memesan nasi goreng, namun tidak diberikan telur mata sapi seperti rincian pesanan saya.
Saya juga memesan minuman namum belum datang.
"""
prompt = """
Berdasarkan kalimat ini, apa sentimen yang disampaikan? Apakah positif, netral, atau negatif?
Berikan rekomendasi jawaban yang diberikan.
"""

message = prompt + customer_email

start_time = time.time()

model="gemini-1.5-flash"
llm = ChatGoogleGenerativeAI(
    model=model,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

messages = [
    ( "system", system_prompt),
    ( "human", message)
]
ai_msg = llm.invoke(messages)
end_time = time.time()
execution_time = end_time - start_time

print( ai_msg.content)
print(f"Waktu eksekusi: {execution_time} detik")
