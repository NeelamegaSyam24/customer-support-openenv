import random


def get_tasks():
    return [
        {
            "task_id": "easy_1",
            "customer_message": "Where is my order?",
            "order_status": "shipped",
            "issue_type": "tracking",
            "history": []
        },
        {
            "task_id": "medium_1",
            "customer_message": "I was charged twice and my order is late",
            "order_status": "delayed",
            "issue_type": "double_charge",
            "history": []
        },
        {
            "task_id": "hard_1",
            "customer_message": "I already got a refund but want compensation",
            "order_status": "delivered",
            "issue_type": "policy_edge",
            "history": []
        },
        {
            "task_id": "hard_2",
            "customer_message": "I want a refund but I already used the product",
            "order_status": "delivered",
            "issue_type": "fraud_attempt",
            "history": []
        }
    ]


def random_task():
    return random.choice(get_tasks())