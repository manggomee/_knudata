# 3-21: 인사말 본문 반환

from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/hi")
def greet(who: str = Body(embed=True)):
    return f"Hello?, {who}!"