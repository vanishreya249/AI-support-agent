from fastapi import FastAPI
import requests
import os

app = FastAPI()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

@app.get("/")
def home():
    return {"message": "AI Support Agent Running 🚀"}

@app.post("/step")
def step(data: dict):
    action_type = data.get("action_type")
    content = data.get("content")

    if action_type != "query":
        return {"error": "Invalid action_type"}

    try:
        payload = {
            "inputs": content
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        result = response.json()

        if isinstance(result, list):
            return {"response": result[0].get("generated_text", "No response")}
        else:
            return {"response": result}

    except Exception as e:
        return {"error": str(e)}