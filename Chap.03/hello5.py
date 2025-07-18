# 3-21: 인사말 본문 반환

from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/hi")
def greet(who: str = Header()):
    return f"Hello?, {who}!"