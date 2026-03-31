from env.tasks import random_task
from env.graders import evaluate


class CustomerSupportEnv:

    def __init__(self):
        self.current_state = None
        self.steps = 0

    def reset(self):
        self.current_state = random_task()
        self.steps = 0
        return self.current_state

    def simulate_customer(self):
        issue = self.current_state["issue_type"]

        if issue == "tracking":
            return "Thanks, when will it arrive?"

        elif issue == "double_charge":
            return "I still see two charges in my bank."

        elif issue == "policy_edge":
            return "That’s not fair, I want compensation!"

        elif issue == "fraud_attempt":
            return "But others got refunds even after using it!"

        return "Okay"

    def step(self, action):
        self.steps += 1

        if "history" not in self.current_state:
            self.current_state["history"] = []

        # Save agent response
        self.current_state["history"].append({
            "agent": action.response
        })

        reward = evaluate(self.current_state, action)

        # Simulate customer reply
        customer_reply = self.simulate_customer()

        self.current_state["history"].append({
            "customer": customer_reply
        })

        self.current_state["customer_message"] = customer_reply

        # Done conditions
        done = False
        if reward.score > 0.85:
            done = True
        if self.steps >= 5:
            done = True

        return self.current_state, reward, done, {}

    def state(self):
        return self.current_state