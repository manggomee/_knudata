from transformers import AutoTokenizer

# BERT와 GPT-2 토크나이저 불러오기
bert_tokenizer = AutoTokenizer.from_pretrained("klue/bert-base")
gpt_tokenizer = AutoTokenizer.from_pretrained("skt/kogpt2-base-v2")

# 입력 문장
text = "아버지가방에들어가신다."

# 각 토크나이저로 토큰화
bert_tokens = bert_tokenizer.tokenize(text)
gpt_tokens = gpt_tokenizer.tokenize(text)

# 결과 출력
print("BERT tokens:", bert_tokens)
print("GPT-2 tokens:", gpt_tokens)
