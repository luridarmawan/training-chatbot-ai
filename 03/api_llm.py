import os
import sys
import datetime
import platform
from rich import print

from langchain_google_genai import ChatGoogleGenerativeAI

import requests
import uvicorn
from typing import Optional
from fastapi import FastAPI, HTTPException, Depends, Request, status, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

class QuestionPayloadModel(BaseModel):
    question: str

model="gemini-1.5-flash"
llm = ChatGoogleGenerativeAI( model=model)

app = FastAPI()

@app.get('/')
async def root():
    return {"code": 0}

# http://localhost:5000/question
@app.post("/question")
def Question(payload:QuestionPayloadModel):
    print(payload)

    #TODO: tanya ke LLM

    answer = "ini jawaban"
    return {"code":0, "answer": answer, "request": payload, "response": { "answer": answer}}

if __name__ == "__main__":
    PORT = os.getenv("API_PORT", 8088)
    print(f"[green]Starting server at port {PORT}[/green]")
    uvicorn.run('api_llm:app', reload=True, host="0.0.0.0", port=int(PORT))
    