import gradio as gr
import numpy as np

def recerte_audio(audio):
    sr, data = audio                         # 오디오: (샘플레이트, numpy 배열)
    reversed_audio = (sr, np.flipud(data))   # 수직으로 반전된 오디오 생성
    return reversed_audio                     # 오디오 출력용 튜플 반환

mic = gr.Audio(sources="microphone", type="numpy", label="음성 입력")  # 마이크 입력

demo = gr.Interface(fn=recerte_audio, inputs=mic, outputs="audio")    # 오디오 반환 설정

demo.launch()  # Gradio 앱 실행
