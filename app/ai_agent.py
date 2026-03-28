import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"

headers = {
    "Authorization": "Bearer ########"
}


def query_model(prompt):
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    result = response.json()

    if isinstance(result, list):
        return result[0]["generated_text"]
    return str(result)


def generate_agent_output(email):
    prompt = f"""
You are an AI support agent.

Analyze the email and do:
- Identify intent (complaint)
- Extract order ID
- Decide action (refund)
- Respond politely

Email:
{email}
"""
    return query_model(prompt)