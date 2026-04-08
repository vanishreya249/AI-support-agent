def query_model(prompt):
    text = prompt.lower().strip()

    # More accurate matching (VERY IMPORTANT)
    if " artificial intelligence " in f" {text} " or text.startswith("ai"):
        return "Artificial Intelligence is the ability of machines to think and learn like humans."

    elif "machine learning" in text:
        return "Machine Learning is a subset of AI that allows systems to learn from data."

    elif "blockchain" in text:
        return "Blockchain is a decentralized system that stores data securely across multiple computers."

    elif "python" in text:
        return "Python is a programming language widely used in AI, web development, and data science."

    elif "cricket" in text:
        return "Cricket is a sport played between two teams where players score runs."
    
    elif "hello" in text:
        return "Hello! How can I assist you today?"

    return f"I understand your question: '{prompt}'. This system responds intelligently to user queries."