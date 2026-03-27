tasks = [
    {
        "id": "easy",
        "description": "Classify customer intent and urgency level",
        "expected_actions": ["classify"]
    },
    {
        "id": "medium",
        "description": "Extract order ID and issue type",
        "expected_actions": ["extract"]
    },
    {
        "id": "hard",
        "description": "Complete full resolution: classify, extract, decide, and respond",
        "expected_actions": ["classify", "extract", "decide", "respond"]
    }
]