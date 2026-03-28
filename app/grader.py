def grade(task_id, output):
    output = output.lower()

    if task_id == "easy":
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

        if "complaint" in output:
            score += 0.25
        if "1234" in output:
            score += 0.25
        if "refund" in output:
            score += 0.25
        if "sorry" in output or "apologize" in output:
            score += 0.25

        return score

    return 0.0