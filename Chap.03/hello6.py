# 3-26: User-Agent 헤더를 반환

from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/hi")
def greet(who: str = Header()):
    return f"Hello?, {who}!"