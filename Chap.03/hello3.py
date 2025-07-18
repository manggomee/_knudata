# 3-15: 인사말 쿼리 매개변수 반환

from fastapi import FastAPI

app = FastAPI()

@app.get("/hi/")
def greet(who):
    return f"Hello?, {who}!"