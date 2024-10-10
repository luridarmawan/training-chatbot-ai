from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

customer_message="""
Permisi Mas. Saya ingin menyampaikan keluhan tentang makanan yang sudah saya pesan.
Saya tadi memesan nasi goreng, namun tidak diberikan telur mata sapi seperti rincian pesanan saya.
Saya juga memesan minuman namum belum datang.
"""

template = """
Dibawah ini adalah keluhan dari pelanggan restoran:

{content}

Berdasarkan kalimat ini, apa sentimen yang disampaikan? Apakah positif, netral, atau negatif?
"""

prompt = PromptTemplate.from_template( template)
prompt_message = prompt.format(content=customer_message)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
messages = [
    ( "human", prompt_message)
]
ai_msg = llm.invoke(messages)
print( ai_msg.content)
