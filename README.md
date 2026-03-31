# 🤖 Customer Support OpenEnv Environment

## 🚀 Overview

This project implements a **real-world OpenEnv environment** that simulates customer support workflows.
AI agents interact with customers, resolve issues, and receive **reward-based feedback** across multi-step conversations.

The system is designed to train and evaluate AI agents in realistic scenarios, bridging the gap between simulation and real-world deployment.

---

## 🎯 Problem Statement

Customer support requires:

* Context understanding
* Multi-step reasoning
* Policy-based decision making

Traditional AI benchmarks are static and do not capture these dynamics.

---

## 🧠 Solution

We built a **multi-turn OpenEnv environment** where:

* Agents interpret customer queries
* Generate responses
* Handle complex real-world scenarios
* Receive continuous reward signals (0.0 → 1.0)

---

## 🔥 Key Features

* ✅ Multi-step interaction environment
* ✅ Realistic customer simulation
* ✅ Reward-based evaluation
* ✅ Easy → Medium → Hard tasks
* ✅ Deterministic grading system
* ✅ Interactive UI dashboard (Gradio)
* ✅ Dockerized deployment
* ✅ Hugging Face live demo

---

## 🧪 Tasks

### 🟢 Easy

* Order tracking queries

### 🟡 Medium

* Double charge + delayed delivery

### 🔴 Hard

* Policy edge cases
* Fraud attempt scenarios

---

## ⚙️ OpenEnv API

| Method         | Description                       |
| -------------- | --------------------------------- |
| `reset()`      | Initializes a new task            |
| `step(action)` | Executes agent action             |
| `state()`      | Returns current environment state |

---

## 🏆 Reward System

The reward function evaluates:

* ✔ Correctness
* ✔ Completeness
* ✔ Policy adherence

| Behavior                 | Score            |
| ------------------------ | ---------------- |
| Correct response         | High (0.8 – 1.0) |
| Partial response         | Medium           |
| Incorrect / hallucinated | Low / penalized  |

---

## 🖥️ Demo

👉 **Live Demo (Hugging Face):**
https://huggingface.co/spaces/NeelamegaSyam/customer-support-openenv

---

## 🤖 Inference Script

Run the baseline agent:

```bash
python inference.py
```

---

## 🐳 Docker Setup

```bash
docker build -t openenv .
docker run -p 7860:7860 openenv
```

---

## ⚙️ Installation (Local Setup)

```bash
git clone https://github.com/NeelamegaSyam24/customer-support-openenv.git
cd customer-support-openenv

pip install -r requirements.txt
python main.py
```

---

## 🔑 Environment Variables

Set the following:

* `API_BASE_URL`
* `MODEL_NAME`
* `OPENAI_API_KEY`
* `HF_TOKEN`

---

## 📁 Project Structure

```
openenv_customer_support/
│
├── env/
│   ├── models.py
│   ├── environment.py
│   ├── tasks.py
│   ├── graders.py
│
├── main.py
├── app.py
├── inference.py
├── openenv.yaml
├── Dockerfile
├── requirements.txt
├── README.md
```

---

## 🏁 Conclusion

This project demonstrates how AI agents can be trained using **realistic, multi-step environments with reward-based feedback**, making it highly relevant for production-level AI systems.

---

## 👨‍💻 Author

Developed by **NMS**

---

## ⭐ Acknowledgment

Built as part of the **Scaler OpenEnv Hackathon**
