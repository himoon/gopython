from pathlib import Path

import streamlit as st
from google import genai
from google.genai import types
from google.genai.chats import Chat
from PIL import Image, ImageFile

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.


def get_client() -> genai.client.Client:
    GEMINI_KEY = "API_KEY"  # Gemini API 키 입력
    return genai.Client(api_key=GEMINI_KEY)  # 클라이언트 객체 생성


def get_chat(sys_prompt: str | None = None) -> Chat:
    client = get_client()
    return client.chats.create(
        model="gemini-2.5-flash",  # Gemini 모델 입력
        config=types.GenerateContentConfig(system_instruction=sys_prompt),
    )  # 챗 객체 생성


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
    st.title("✨ 혼자 만들면서 공부하는 멀티모달 AI 챗봇")
    if img := upload_image():  # 이미지 등록
        prompt = "공연은 어디에서 몇 시에 시작해? 한글로 대답해 줘"  # 이미지에 대한 질문
        with st.chat_message("user"):  # 사용자 메시지 출력
            st.markdown(prompt)
        with st.chat_message("✨"):  # LLM 매시지 출력
            with st.spinner("대화를 생성하는 중입니다..."):
                chat = get_chat()  # 챗 객체 생성
                resp = chat.send_message([img, prompt])  # 이미지 및 텍스트 전송
                st.markdown(resp.text)
