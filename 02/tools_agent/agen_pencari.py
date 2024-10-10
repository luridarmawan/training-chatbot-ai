from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import (
    AgentExecutor, AgentType, initialize_agent
)
from dotenv import load_dotenv
load_dotenv()

model="gemini-1.5-flash"
llm = ChatGoogleGenerativeAI( model=model, max_retries=2,)

def load_agent() -> AgentExecutor:
    llm = ChatGoogleGenerativeAI( model="gemini-1.5-flash", max_retries=2,)
    tools = load_tools(
        tool_names=["wikipedia"],
        llm=llm
    )
    return initialize_agent(
        tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

agent = load_agent()

query = "buat biografi singkat tentang soekarno, presiden indonesia pertama. cantumkan link wikipedia referensi aslinya."
response = agent({"input": query})
print(response["output"])
