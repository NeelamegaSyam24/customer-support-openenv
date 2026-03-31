from env.models import Reward


def evaluate(state, action):
    score = 0.0
    feedback = []

    msg = action.response.lower()
    issue = state["issue_type"]

    # EASY
    if issue == "tracking":
        if "shipped" in msg or "on the way" in msg:
            score += 0.7
        if action.action_type == "reply":
            score += 0.3

    # MEDIUM
    elif issue == "double_charge":
        if "refund" in msg:
            score += 0.4
        if "sorry" in msg:
            score += 0.2
        if "delay" in msg:
            score += 0.2
        if action.action_type == "refund":
            score += 0.2

    # HARD
    elif issue == "policy_edge":
        if "already refunded" in msg:
            score += 0.4
        if "cannot" in msg or "policy" in msg:
            score += 0.4
        if action.action_type == "reply":
            score += 0.2

    # FRAUD CASE
    elif issue == "fraud_attempt":
        if "cannot refund" in msg or "policy" in msg:
            score += 0.6
        if "used product" in msg:
            score += 0.2
        if action.action_type == "reply":
            score += 0.2

    # 🚨 PENALTIES
    if "free money" in msg:
        score -= 1.0
        feedback.append("Hallucination")

    if len(msg) < 5:
        score -= 0.5
        feedback.append("Too short")

    score = max(0.0, min(1.0, score))

    return Reward(score=score, feedback="; ".join(feedback))