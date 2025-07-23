from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/hi")
def greet2(who: str = Header()):
    return {"message": f"안녕?, {who}!"}

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.get("/bye")
def bye():
    return {"message": "잘 가요!"}

@app.get("/thanks")
def thanks():
    return {"message": "고마워요!"}

@app.get("/add")
def add(a: int, b:int):
    return a+b

@app.get("/user-agent")
def get_user_agent(user_agent: str = Header()):
    if "Edg" in user_agent:
        print('Edge')
        return 'Edge 브라우저를 사용하고 있군요!'
    elif "Chrome" in user_agent:
        print('Chrome')
        return 'Chrome 브라우저를 사용하고 있군요!'
    else:
        print('None')
        return '알 수없는 브라우저를 사용하고 있군요!'