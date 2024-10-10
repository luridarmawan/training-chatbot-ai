import os
import random
import time
from rich import print
from langchain import hub
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
)
from langchain.prompts import PromptTemplate
from langchain.tools import tool
from langchain_core.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

# Baca template prompt dari file
# prompt = hub.pull("hwchase17/react")
with open("agent_prompt.txt", "r") as prompt_file:
    prompt_template = prompt_file.read()

prompt = PromptTemplate.from_template( prompt_template)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, )


# fungsi tool sederhana yang memberikan nilai jam saat ini
def get_current_time(*args, **kwargs):
    """Returns the current time in H:MM AM/PM format."""
    import datetime  # Import datetime module to get current time

    now = datetime.datetime.now()  # Get current time
    return now.strftime("%I:%M %p")  # Format time in H:MM AM/PM format

# tool untuk mendapatkan informasi kurs
@tool
def get_exchange_rate(query: str) -> str:
    """Returns the exchange rate."""
    rateFrom, rateTo = query.split(",")
    current_rate = random.randint(100, 5000)
    # current_rate = 15213 # dummy value
    text = f"Rate from {rateFrom} to {rateTo} is {current_rate}"
    return text

def tool_search_pasal_only(string):
    text = "Lengkapi dengan jelas dengan undang-undang/peraturannya."
    return text

def tool_parsing_document(string):
    docType, tahun, nomor, pasal = string.split(",")
    docType = docType.upper()

    # TODO: Search to database
    text = f"{docType} nomor {nomor} tahun {tahun} pasal {pasal} ini tentang kondisi dan situasi yang tak terduga."

    return text


# Daftar tools yang disediakan untuk Agen
tools = [
    Tool(
        name="Time",
        func=get_current_time,  # fungsi yang akan dijalankan
        description="Useful for when you need to know the current time",
    ),
    Tool(
        name="Kurs",
        func=get_exchange_rate,  # fungsi yang akan dijalankan
        description="Use this tool to get the current exchange rate between currencies. The user might ask for something like 'What is the USD to EUR rate?' Input tools ini harus berupa daftar mata uang yang dicari. misal: USD,IDR",
    ),
    Tool(
        name = "PasalOnly",
        func=tool_search_pasal_only,
        description="berguna jika pencarian hanya memiliki informasi pasal saja, tanpa menyebut undang-undang atau peraturan tertentu."
    ),
    Tool(
        name = "Document-Parser",
        func=tool_parsing_document,
        description="berguna untuk mencari suatu pasal dalam dokumen undang-undang. Input untuk tools ini harus berupa daftar yang dipisahkan dalam tanda koma sebanyak 4 item, yang mewakili 4 informasi yang akan dicari. Misalnya, `permen,2023,11,1` akan menjadi input jika anda ingin mencari dokumen permen (peraturan menteri) tahun 2023 nomor 11 pasal1. Gunakan tools `PasalOnly` jika input kurang dari 4 item. Observasi hanya dalam bahasa indonesia."
    ),
]

# Buat agen ReAct 
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
    stop_sequence=True,
    # stop_sequence=None,
)

# Buat agent executor dari agen dan tools
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=3,
    max_execution_time=10,
    handle_parsing_errors=True  # Menangani error parsing
)




while True:
    user_input = input("Pertanyaan: ")
    if user_input.lower() in ("", "exit", "q", "x"):
        break
    else:
        response = agent_executor.invoke({"input": user_input})
        print(f"[yellow]{response['output']}[/]")
        # print(f"[yellow]{response}[/]")


