from fastapi import FastAPI
from app.baseline import run_baseline
from app.env import reset, step, state
from app.models import Action
from app.tasks import tasks
from app.grader import grade

app = FastAPI()


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/reset")
def reset_env():
    return reset()


@app.post("/step")
def step_env(action: Action):
    return step(action)


@app.get("/state")
def get_state():
    return state()


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/grader")
def run_grader(task_id: str, output: str):
    return {"score": grade(task_id, output)}


@app.get("/baseline")
def baseline():
    return run_baseline()