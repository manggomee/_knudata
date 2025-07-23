from datasets import load_dataset
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
import torch

# 데이터셋 로드 및 샘플 선택
imdb = load_dataset("imdb")
samples = imdb["train"].shuffle(seed=42).select(range(8))

# 토크나이저 & 모델 로드
model_name = "distilbert-base-uncased"
tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)
model = DistilBertForSequenceClassification.from_pretrained(model_name)

# 전처리
def preprocess(batch):
    return tokenizer(batch["text"],
                     truncation=True,
                     padding="max_length",
                     max_length=128)

tokens = samples.map(preprocess, batched=True)
# .set_format으로 텐서 포맷 지정
tokens.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])

# 예: 앞에서 8개만 추출
input_ids = tokens[:8]["input_ids"]
attention_mask = tokens[:8]["attention_mask"]
labels = tokens[:8]["label"]

# 모델 추론
model.eval()
with torch.no_grad():
    outputs = model(input_ids=input_ids, attention_mask=attention_mask)

logits = outputs.logits
preds = torch.argmax(logits, dim=-1)

# 결과 출력
print("예측:", preds.tolist())
print("정답:", labels.tolist())

print("-" * 50)
