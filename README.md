---
title: Customer Support OpenEnv
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# 🤖 Customer Support OpenEnv

## 🚀 Description
This project is a multi-turn AI training environment simulating real-world customer support interactions using OpenEnv.

Agents interact with customers, resolve issues, and receive reward-based feedback.

---

## 🧠 Features
- Multi-step conversation environment
- Realistic customer simulation
- Reward-based evaluation (0.0 → 1.0)
- Easy → Medium → Hard tasks
- Interactive UI dashboard (Gradio)

---

## 🎯 Tasks

### 🟢 Easy
- Order tracking queries

### 🟡 Medium
- Double charge + delayed order

### 🔴 Hard
- Policy edge cases
- Fraud attempts

---

## ⚙️ API Endpoints

- `/reset` → Start new task  
- `/step` → Take action  
- `/state` → Get current state  

---

## 🐳 Run with Docker

```bash
docker build -t openenv .
docker run -p 7860:7860 openenv