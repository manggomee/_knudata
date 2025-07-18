# 3-1: hello.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
def greet():
    return "Hello, World!"