# 3-11: 인사말 경로 변경

from fastapi import FastAPI

app = FastAPI()

@app.get("/hi/{who}")
def greet(who):
    return f"Hello?, {who}!"