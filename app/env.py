import random
from models import Observation

EMAILS = [
    "Hi, my order #1234 hasn't arrived. I want a refund.",
    "I received a damaged product (Order #5678). Please replace it.",
    "Where is my order #9999? It’s been delayed.",
    "I was charged twice for order #2222. Need refund.",
]

current_state = {}


def reset():
    global current_state

    email = random.choice(EMAILS)

    current_state = {
        "email": email,
        "history": [],
        "step": 0
    }

    return Observation(
        email_text=email,
        history=[],
        step_count=0
    )


def step(action):
    global current_state

    reward = 0
    breakdown = {}

    current_state["step"] += 1
    email = current_state["email"].lower()

    if action.action_type == "classify":
        if "refund" in email:
            reward += 0.2
            breakdown["classification"] = 0.2

    elif action.action_type == "extract":
        if any(num in action.content for num in ["1234", "5678", "9999", "2222"]):
            reward += 0.2
            breakdown["extraction"] = 0.2

    elif action.action_type == "decide":
        if "refund" in action.content.lower() or "replace" in action.content.lower():
            reward += 0.3
            breakdown["decision"] = 0.3

    elif action.action_type == "respond":
        content = action.content.lower()
        if "sorry" in content or "apologize" in content:
            reward += 0.3
            breakdown["response"] = 0.3

    done = current_state["step"] >= 4

    return (
        Observation(
            email_text=current_state["email"],
            history=current_state["history"],
            step_count=current_state["step"]
        ),
        reward,
        done,
        {"breakdown": breakdown}
    )


def state():
    return current_state