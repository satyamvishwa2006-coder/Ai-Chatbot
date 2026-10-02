from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import json
import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load intents
with open("intents.json", "r") as json_data:
    intents = json.load(json_data)


# Load trained model
FILE = "data.pth"
data = torch.load(FILE, weights_only=False)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]

all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]


# Create model
model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()


bot_name = "MyChatbot"


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "MyChatbot API is running!"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    sentence = request.message

    sentence_tokens = tokenize(sentence)

    X = bag_of_words(sentence_tokens, all_words)
    X = torch.from_numpy(X)

    output = model(X)

    _, predicted = torch.max(output, dim=0)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=0)

    probability = probs[predicted.item()]


    if probability.item() > 0.75:

        for intent in intents["intents"]:

            if tag == intent["tag"]:

                response = random.choice(
                    intent["responses"]
                )

                return {
                    "response": response
                }


    return {
        "response": "I don't understand. Can you please rephrase?"
    }