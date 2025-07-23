from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig

app = FastAPI()

model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
config = GenerationConfig(max_new_tokens=200)

@app.get("/qna")
def prompt(question: str) -> str:
    tokens = tokenizer(question, return_tensors="pt")  # 질문을 토크나이징
    outputs = model.generate(**tokens, max_new_tokens=100)  # 모델로 텍스트 생성
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)  # 결과 디코딩
    return result
