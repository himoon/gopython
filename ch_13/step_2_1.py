import ollama
import streamlit as st


def init_session_state(keys: dict):
    for key, value in keys.items():
        if key not in st.session_state:  # key가 세션 저장소에 없는 경우,
            st.session_state[key] = value  # 새로운 세션 생성


def chat_message_user(prompt: str) -> dict:
    with st.chat_message("user"):  # 사용자 메시지 출력
        st.markdown(prompt)
        return dict(role="user", content=prompt)


def chat_message_llm(role: str, model: str, messages: list) -> dict:
    with st.chat_message(role):  # LLM 메시지 출력
        with st.spinner("대화를 생성하는 중입니다..."):
            resp = ollama.chat(model=model, messages=messages)
            msg_llm = resp.get("message", {})
            st.markdown(msg_llm["content"])
            return msg_llm


if __name__ == "__main__":
    st.set_page_config(layout="wide")  # 화면을 넓게 사용
    st.title("🤖 만들면서 배우는 챗봇")

    init_session_state(dict(msgs=[]))  # 세션 저장소 초기화
    msgs: list = st.session_state["msgs"]  # 'msgs' 세션을 msgs 변수로 접근

    for row in msgs:  # msgs에 저장된 모든 메시지 기록을 하나씩 반복 출력
        with st.chat_message(row["role"]):
            st.markdown(row["content"])

    if prompt := st.chat_input("여기에 대화를 입력하세요!"):
        msg_user = chat_message_user(prompt)
        msgs.append(msg_user)  # 사용자 메시지 추가

        msg_llm = chat_message_llm("assistant", "gemma2:9b", msgs)
        msgs.append(msg_llm)  # LLM 메시지 추가
