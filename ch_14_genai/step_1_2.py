from pathlib import Path

import google.generativeai as genai
import streamlit as st
from PIL import Image, ImageFile

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.


def get_model(sys_prompt: str = None) -> genai.GenerativeModel:
    GEMINI_KEY = "AIzaSyB9dCdlt1AG3la0W_pyCwyyq9RppKqv6nE"  # Gemini API 키 입력
    GEMINI_MODEL = "gemini-1.5-flash"  # Gemini 모델 입력
    genai.configure(api_key=GEMINI_KEY, transport="rest")  # API 키 설정
    return genai.GenerativeModel(GEMINI_MODEL, system_instruction=sys_prompt)


def upload_image(on_change=None, args=None) -> ImageFile.ImageFile | None:
    with st.sidebar:  # 화면 왼쪽에 사이드바 생성
        uploaded = st.file_uploader(  # 파일 업로드 위젯
            "uploader",
            label_visibility="collapsed",
            on_change=on_change,  # 파일 등록 또는 삭제 시 호출될 함수
            args=args,  # on_change 매개변수에 등록된 함수 호출 시 전달할 입력값
        )
        if uploaded is not None:
            with st.container(border=True):  # 이미지를 담을 박스 생성
                tmp_path = OUT_DIR / f"{Path(__file__).stem}.tmp"  # 임시 파일 경로
                tmp_path.write_bytes(uploaded.getvalue())  # 업로드한 이미지 저장
                img = Image.open(tmp_path)  # Image 객체 생성
                st.image(img, use_container_width=True)  # 이미지 출력
                return img


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    st.title("✨ 만들면서 배우는 멀티모달 AI")
    if img := upload_image():  # 이미지 등록
        prompt = "공연은 어디에서 몇 시에 시작해? 한글로 대답해 줘"  # 이미지에 대한 질문
        with st.chat_message("user"):  # 사용자 메시지 출력
            st.markdown(prompt)
        with st.chat_message("✨"):  # LLM 매시지 출력
            with st.spinner("대화를 생성하는 중입니다..."):
                model = get_model()  # 생성형 모델 객체 생성
                chat = model.start_chat()  # 챗 객체 생성
                resp = chat.send_message([img, prompt])  # 이미지 및 텍스트 전송
                st.markdown(resp.text)
