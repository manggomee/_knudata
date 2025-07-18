# 3-33: 모델 변형: model/tag.py
from datetime import datetime
from pydantic import BaseModel

class TagIn(BaseModel):
    tag: str

class Tag(BaseModel):
    tag: str
    created: datetime
    secret: str

class TagOut(BaseModel):
    tag: str
    created: datetime