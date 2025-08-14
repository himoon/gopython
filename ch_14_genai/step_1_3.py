import streamlit as st
from google.genai.chats import Chat
from PIL import ImageFile

from step_1_2 import get_chat, upload_image  # 이전에 작성한 모듈을 불러옵니다.


def init_session(keys: dict):  # 세션 초기화
    for key, value in keys.items():
        if key not in st.session_state:
            st.session_state[key] = value


def clear_session(*exclude):  # 세션 삭제
    for key in st.session_state.keys():
        if exclude is None or key not in exclude:
            del st.session_state[key]


def init_page():
    st.set_page_config(layout="wide")  # 페이지 레이아웃 설정
    st.title("✨ 만들면서 배우는 멀티모달 AI")
    chat = get_chat()  # 챗 객체 생성
    init_session(dict(chat=chat, msgs=[]))  # 세션 초기화


def show_messages():  # 메시지 기록 출력
    for row in st.session_state["msgs"]:
        with st.chat_message(row["role"]):
            st.markdown(row["content"])


def send_image(img: ImageFile):  # 이미지 전송
    chat: Chat = st.session_state["chat"]  # 챗 객체 가져오기
    if not chat.get_history():  # 대화 기록이 없으면 첫 번째 메시지 전송
        with st.spinner("이미지를 분석하는 중입니다..."):
            chat.send_message([img, "이미지를 분석하고, 내 질문에 대답해줘."])


def send_user_input():  # 사용자 메시지 전송
    if prompt := st.chat_input("여기에 대화를 입력하세요!"):
        msgs: list = st.session_state["msgs"]
        with st.chat_message("user"):  # 사용자 메시지 출력
            st.markdown(prompt)
            msgs.append(dict(role="user", content=prompt))
        with st.chat_message("✨"):  # LLM 메시지 출력
            with st.spinner("대화를 생성하는 중입니다..."):
                chat: Chat = st.session_state["chat"]  # 챗 객체 가져오기
                resp = chat.send_message(prompt)
                st.markdown(resp.text)
                msgs.append(dict(role="✨", content=resp.text))


if __name__ == "__main__":
    init_page()  # 페이지 초기화
    if img := upload_image(on_change=clear_session):  # 이미지 등록
        show_messages()  # 메시지 기록 출력
        send_image(img)  # 이미지 전송
        send_user_input()  # 사용자 메시지 전송
