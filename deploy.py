from fastapi import FastAPI
from pydantic import BaseModel
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ensure environment variables are loaded correctly
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Initialize FastAPI app
mb_app = FastAPI(title="Langchain Server", version="1.0", description="Sample API Server")

# Initialize Ollama model
llm = Ollama(model="llama2")

# Define prompts
prompt1 = ChatPromptTemplate.from_template("Give me information about {topic} in 200 words")
prompt2 = ChatPromptTemplate.from_template("Give me a song about {topic} in 50 words")

# Define request model
class TopicRequest(BaseModel):
    topic: str

# Define routes
@mb_app.post("/information")
async def information(request: TopicRequest):
    chain = LLMChain(prompt=prompt1, llm=llm)
    response = chain.run({"topic": request.topic})
    return {"response": response}

@mb_app.post("/song")
async def song(request: TopicRequest):
    chain1 = LLMChain(prompt=prompt2, llm=llm)
    response = chain1.run({"topic": request.topic})
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(mb_app, host="localhost", port=8000)
