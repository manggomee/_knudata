from fastapi import FastAPI, Response
import plotly.express as px

app = FastAPI()

@app.get("/test")
def test():
    df = px.data.iris()  # Iris 데이터셋 로드
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")  # 산점도 그래프 생성
    fig_bytes = fig.to_image(format="png")  # 그래프를 PNG 이미지로 변환
    return Response(content=fig_bytes, media_type="image/png")  # 이미지 응답 반환
