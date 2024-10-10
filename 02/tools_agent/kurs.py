from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import RequestsWrapper
from langchain_community.tools import RequestsGetTool, RequestsPostTool
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


requests_wrapper = RequestsWrapper()
kurs_tool = RequestsGetTool(requests_wrapper=requests_wrapper, allow_dangerous_requests=True)

# Contoh penggunaan untuk mendapatkan data dari API
kurs = kurs_tool.run("https://api.exchangerate-api.com/v4/latest/USD")
print(kurs)

prompt = PromptTemplate.from_template(
"""
Respons dari API Kurs: {content}

{text}

Final Answer: {response}
"""
)

text="berapa kurs SGD?"

message = prompt.format(content=kurs, text=text)
model="gemini-1.5-flash"
llm = ChatGoogleGenerativeAI( model=model, max_retries=2,)

result = llm.invoke(message)
print(result.content)
