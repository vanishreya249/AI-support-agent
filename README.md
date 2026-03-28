# 🤖 AI Support Agent (OpenEnv Hackathon)

## 💡 Overview

This project implements an **AI-powered autonomous customer support agent** that processes user emails using multi-step reasoning.

The agent performs:

* Intent classification
* Order information extraction
* Decision making (refund/replace)
* Response generation

It is built as an **interactive environment with evaluation scoring**, making it suitable for testing intelligent agents.

---

## 🧠 Problem

Automating customer support is challenging because it requires:

* Understanding user intent
* Extracting structured data from text
* Making correct decisions
* Generating human-like responses

---

## ✅ Solution

This project provides a **structured AI agent pipeline** powered by **Hugging Face models**, where:

* AI analyzes customer emails
* Performs multi-step reasoning
* Generates appropriate responses
* Is evaluated using a reward-based scoring system

---

## ⚙️ Features

* 🤖 AI-powered reasoning using Hugging Face (FLAN-T5)
* 🟢 Simulated email environment
* 🟡 Step-by-step agent workflow
* 🔴 Automated grading system
* 🚀 FastAPI backend
* 📊 Baseline evaluation with scoring

---

## 🧱 Architecture

User Input → FastAPI → AI Agent → Environment → Grader → Score

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run server

```bash
python -m uvicorn app.main:app --reload
```

### 3. Run AI agent

```bash
python -m app.baseline
```

---

## 📌 API Endpoints

* `/reset` → Start new email scenario
* `/step` → Perform agent action
* `/state` → Get current state
* `/grader` → Evaluate output
* `/baseline` → Run AI agent

---

## 🎯 Tasks

* Easy → Intent classification
* Medium → Information extraction
* Hard → Full support resolution

---

## 🧪 Example

**Input Email:**

> "Hi, my order #1234 hasn't arrived. I want a refund."

**AI Agent Output:**

* Intent → Complaint
* Order ID → 1234
* Decision → Refund
* Response → Apology

---

## 📊 Evaluation

The system evaluates performance based on:

* Intent detection
* Order ID extraction
* Correct decision
* Response quality

---

## 📈 Sample Output

```python
{'easy': 1.0, 'medium': 1.0, 'hard': 1.0}
```

---

## 🔮 Future Improvements

* Advanced LLM integration
* Frontend UI
* Real-time chatbot
* Multi-language support

---

## 🏁 Conclusion

This project demonstrates how **AI agents can perform structured reasoning and be evaluated in a controlled environment**, making it a strong foundation for real-world customer support automation systems.
