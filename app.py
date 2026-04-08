from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StepInput(BaseModel):
    email: str

@app.get("/")
def home():
    return {"message": "AI Support Agent Running 🚀"}

@app.post("/reset")
def reset():
    return {
        "email": "My order is delayed. Can you help me?"
    }

@app.post("/step")
def step(input: StepInput):
    return {
        "response": "We are sorry for the delay. Your order will arrive soon."
    }