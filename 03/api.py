import os
import sys
import datetime
import platform
from rich import print

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

app = FastAPI()

@app.get('/')
async def root():
    return {"code": 222}


if __name__ == "__main__":
    PORT = os.getenv("API_PORT", 8088)
    print(f"[green]Starting server at port {PORT}[/green]")
    uvicorn.run('api:app', reload=True, host="0.0.0.0", port=int(PORT))

