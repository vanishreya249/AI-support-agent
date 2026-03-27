def grade(task_id, output):
    output = output.lower()

    if task_id == "easy":
        # Check classification intent
        if "complaint" in output or "refund" in output:
            return 1.0
        return 0.0

    elif task_id == "medium":
        score = 0.0

        if "1234" in output:
            score += 0.5
        if "refund" in output or "not arrived" in output:
            score += 0.5

        return score

    elif task_id == "hard":
        score = 0.0

        # Intent
        if "complaint" in output:
            score += 0.25

        # Extraction
        if "1234" in output:
            score += 0.25

        # Decision
        if "refund" in output:
            score += 0.25

        # Response quality
        if "sorry" in output or "apologize" in output:
            score += 0.25

        return score

    return 0.0