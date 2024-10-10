import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model="gemini-1.5-flash"
llm = ChatGoogleGenerativeAI(
    model=model,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

demografi_file = open("data/demografi-jakarta.txt", "r")
demografi_prompt = demografi_file.readlines()

messages = [
    ( "system", demografi_prompt),
    ( "human", "halo")
]

while True:
    user_input = input("Pertanyaan: ")
    if user_input.lower() in ("", "exit", "q", "x"):
        break
    else:
        messages.append(("human", user_input))
        result = llm.invoke(messages)
        messages.append(("ai", result.content))
        print(result.content)
