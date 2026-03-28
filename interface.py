from fastapi import FastAPI
from app.env import reset, step, state
from app.models import Action

app = FastAPI()

@app.post("/reset")
def reset_env():
    return reset()

@app.post("/step")
def step_env(action: Action):
    return step(action)

@app.get("/state")
def get_state():
    return state()