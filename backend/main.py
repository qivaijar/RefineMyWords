import torch
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables from .env
load_dotenv()

# Define FastAPI app
app = FastAPI()

# Create a ChatOpenAI model, automatically detects OPENAI_API_KEY under the hood.
model = ChatOpenAI(model="gpt-3.5-turbo")


# Data class for the input
class SentenceRequest(BaseModel):
    sentence: str


@app.post("/refine")
async def refine_sentence(request: SentenceRequest):
    # Prepare the input sentence messages
    messages = [
        SystemMessage(content="Take the following text and enhance it to improve clarity, \grammar, and conciseness.\
             Make it sound natural and professional, while preserving the original meaning."),
        HumanMessage(content=request.sentence)
    ]

    result = model.invoke(messages)

    refined_text = result.content
    print(refined_text)

    return {
        "refined_sentence": refined_text
    }
