import gradio as gr
from env.environment import CustomerSupportEnv
from env.models import Action

env = CustomerSupportEnv()


def reset_env():
    state = env.reset()

    chat = []
    chat.append(("Customer", state["customer_message"]))

    info = f"""
    🔹 Task ID: {state['task_id']}
    🔹 Issue Type: {state['issue_type']}
    🔹 Order Status: {state['order_status']}
    """

    return chat, info, "0.0"


def step_env(user_input, chat_history):
    action = Action(
        response=user_input,
        action_type="reply"
    )

    obs, reward, done, _ = env.step(action)

    chat_history.append(("Agent", user_input))
    chat_history.append(("Customer", obs["customer_message"]))

    return chat_history, f"{reward.score:.2f}"


with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Customer Support AI Environment")

    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot()
            user_input = gr.Textbox(placeholder="Type your response...")
            send_btn = gr.Button("Send")

        with gr.Column(scale=1):
            task_info = gr.Markdown()
            reward_box = gr.Textbox(label="Reward", value="0.0")

    reset_btn = gr.Button("🔄 Reset")

    reset_btn.click(reset_env, outputs=[chatbot, task_info, reward_box])
    send_btn.click(step_env, inputs=[user_input, chatbot], outputs=[chatbot, reward_box])

demo.launch(server_name="0.0.0.0", server_port=7860)