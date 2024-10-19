import torch
from fastapi import FastAPI
from pydantic import BaseModel
from happytransformer import HappyTextToText, TTSettings

app = FastAPI()

# Load pre-trained BART model and tokenizer from Hugging Face
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
tt_settings = TTSettings(num_beams=5, min_length=1)


class SentenceRequest(BaseModel):
    sentence: str


@app.post("/refine")
async def refine_sentence(request: SentenceRequest):
    # Prepare the input sentence
    # Currently, this model can only handle simple grammar correction
    input_sentence = "grammar: " + request.sentence

    # Generate the refined output from the model
    with torch.no_grad():
        result = happy_tt.generate_text(input_sentence, args=tt_settings)

    # Decode the model's output back to text
    refined_sentence = result.text

    return {
        "refined_sentence": refined_sentence
    }
