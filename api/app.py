from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv


llama2 = Ollama(model="llama2")
codellama = Ollama(model="codellama")

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

add_routes(
    app,
    llama2,
    path="/chatbot"   
)

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an Code about {topic}")

add_routes(
    app,
    prompt1|llama2,
    path="/chat"
)

add_routes(
    app,
    prompt2|codellama,
    path="/code"
)

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)
    