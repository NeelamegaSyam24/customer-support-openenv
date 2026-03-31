from fastapi import FastAPI
from env.environment import CustomerSupportEnv
from env.models import Action

app = FastAPI()
env = CustomerSupportEnv()


@app.get("/")
def home():
    return {"message": "Customer Support OpenEnv Running"}


@app.get("/reset")
def reset():
    return env.reset()


@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }


@app.get("/state")
def state():
    return env.state()