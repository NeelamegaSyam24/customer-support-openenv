import gradio as gr
import requests

import os

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")

state_data = None


def reset_env():
    global state_data

    response = requests.get(f"{BASE_URL}/reset")
    state_data = response.json()

    chat = []
    chat.append(("Customer", state_data["customer_message"]))

    info = f"""
    🔹 Task ID: {state_data['task_id']}
    🔹 Issue Type: {state_data['issue_type']}
    🔹 Order Status: {state_data['order_status']}
    """

    return chat, info, "0.0"


def step_env(user_input, chat_history):
    global state_data

    payload = {
        "response": user_input,
        "action_type": "reply"
    }

    response = requests.post(f"{BASE_URL}/step", json=payload)
    data = response.json()

    state_data = data["observation"]
    reward = data["reward"]["score"]

    # Update chat
    chat_history.append(("Agent", user_input))
    chat_history.append(("Customer", state_data["customer_message"]))

    return chat_history, f"{reward:.2f}"


with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Customer Support AI Environment")

    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot()
            user_input = gr.Textbox(placeholder="Type your response as the agent...")
            send_btn = gr.Button("Send")

        with gr.Column(scale=1):
            task_info = gr.Markdown("Task info will appear here")
            reward_box = gr.Textbox(label="Reward Score", value="0.0")

    reset_btn = gr.Button("🔄 Reset Environment")

    # Actions
    reset_btn.click(reset_env, outputs=[chatbot, task_info, reward_box])
    send_btn.click(step_env, inputs=[user_input, chatbot], outputs=[chatbot, reward_box])

demo.launch()