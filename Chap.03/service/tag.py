# 3-34: 웹 모듈에 무언가를 제공하는 모듈: service/tag.py
from datetime import datetime
from model.tag import Tag

def create(tag: Tag) -> Tag:
    """태그를 생성한다."""
    return tag

def get(tag_str: str) -> Tag:
    """태그를 반환한다."""
    return Tag(tag=tag_str, created=datetime.utcnow(), secret="")
