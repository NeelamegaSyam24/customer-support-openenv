import os
from openai import OpenAI
from env.environment import CustomerSupportEnv
from env.models import Action

client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

env = CustomerSupportEnv()


def run():
    total_score = 0
    tasks = 3

    for _ in range(tasks):
        state = env.reset()

        messages = [
            {"role": "system", "content": "You are a professional customer support agent. Be polite, accurate, and helpful."}
        ]

        for step in range(5):
            messages.append({"role": "user", "content": str(state)})

            response = client.chat.completions.create(
                model=os.getenv("MODEL_NAME"),
                messages=messages
            )

            text = response.choices[0].message.content

            action = Action(
                response=text,
                action_type="reply"
            )

            obs, reward, done, _ = env.step(action)

            print(f"Step {step+1} Score:", reward.score)

            if done:
                total_score += reward.score
                break

            state = obs

    print("Average Score:", total_score / tasks)


if __name__ == "__main__":
    run()