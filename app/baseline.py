import requests

BASE_URL = "http://127.0.0.1:8000"

def run_baseline():
    results = {}

    # 🟢 EASY TASK
    requests.post(f"{BASE_URL}/reset")
    output_easy = "complaint refund"
    score_easy = requests.post(
        f"{BASE_URL}/grader",
        params={"task_id": "easy", "output": output_easy}
    ).json()["score"]

    results["easy"] = score_easy

    # 🟡 MEDIUM TASK
    requests.post(f"{BASE_URL}/reset")
    output_medium = "Order 1234 refund requested"
    score_medium = requests.post(
        f"{BASE_URL}/grader",
        params={"task_id": "medium", "output": output_medium}
    ).json()["score"]

    results["medium"] = score_medium

    # 🔴 HARD TASK
    requests.post(f"{BASE_URL}/reset")
    output_hard = "complaint order 1234 refund sorry"
    score_hard = requests.post(
        f"{BASE_URL}/grader",
        params={"task_id": "hard", "output": output_hard}
    ).json()["score"]

    results["hard"] = score_hard

    return results


if __name__ == "__main__":
    print(run_baseline())