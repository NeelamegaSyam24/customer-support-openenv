import gradio as gr
from fastapi import FastAPI
from env.environment import CustomerSupportEnv
from env.models import Action
import uvicorn
from threading import Thread

env = CustomerSupportEnv()

# ================= FASTAPI =================
api = FastAPI()


@api.post("/reset")
def reset():
    return env.reset()


@api.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)

    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }


@api.get("/state")
def state():
    return env.state()


# ================= GRADIO =================

def reset_env():
    state = env.reset()

    chat = [
        {
            "role": "user",
            "content": state["customer_message"]
        }
    ]

    info = f"""
🔹 Task ID: {state['task_id']}  
🔹 Issue Type: {state['issue_type']}  
🔹 Order Status: {state['order_status']}
"""

    return chat, info, "0.0"


def step_env(user_input, chat_history):
    if chat_history is None:
        chat_history = []

    action = Action(
        response=user_input,
        action_type="reply"
    )

    obs, reward, done, _ = env.step(action)

    chat_history.append({
        "role": "assistant",
        "content": user_input
    })

    chat_history.append({
        "role": "user",
        "content": obs["customer_message"]
    })

    return chat_history, f"{reward.score:.2f}"


with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Customer Support AI Environment")

    with gr.Row():
        chatbot = gr.Chatbot()
        user_input = gr.Textbox()
        send_btn = gr.Button("Send")

    task_info = gr.Markdown()
    reward_box = gr.Textbox(label="Reward Score")

    reset_btn = gr.Button("Reset")

    reset_btn.click(reset_env, outputs=[chatbot, task_info, reward_box])
    send_btn.click(step_env, inputs=[user_input, chatbot], outputs=[chatbot, reward_box])


# ================= RUN BOTH =================

def run_fastapi():
    uvicorn.run(api, host="0.0.0.0", port=8000)


# Run FastAPI in background
Thread(target=run_fastapi).start()

# Run Gradio
demo.launch(server_name="0.0.0.0", server_port=7860)
