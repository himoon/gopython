import streamlit as st

from step_2_1 import (  # 이전에 작성한 모듈을 불러옵니다.
    chat_message_llm,
    chat_message_user,
    init_session_state,
)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    st.title("🤖 만들면서 배우는 챗봇")

    init_session_state(dict(gemma=[], llama=[]))  # 세션 저장소 초기화
    gemma: list = st.session_state["gemma"]
    llama: list = st.session_state["llama"]

    for msg_gemma, msg_llama in zip(gemma, llama):  # gemma와 llama 메세지를 결합
        if msg_gemma["role"] == "user":  # 사용자 메시지는 1회만 출력
            with st.chat_message("user"):
                st.markdown(msg_gemma["content"])
        else:  # LLM 메시지는 두 개의 열로 나누어 각각 출력
            col_gemma, col_llama = st.columns(2)
            with col_gemma:  # 젬마 LLM 메시지 출력
                with st.chat_message("Gemma"):
                    st.markdown(msg_gemma["content"])
            with col_llama:  # 라마 LLM 메시지 출력
                with st.chat_message("Llama"):
                    st.markdown(msg_llama["content"])

    if prompt := st.chat_input("여기에 대화를 입력하세요!"):
        msg_user = chat_message_user(prompt)
        gemma.append(msg_user)  # 'gemma' 세션에 사용자 메시지 추가
        llama.append(msg_user)  # 'llama' 세션에 사용자 메시지 추가

        col_gemma, col_llama = st.columns(2)
        with col_gemma:
            msg_gemma = chat_message_llm("Gemma", "gemma2:9b", gemma)
            gemma.append(msg_gemma)  # 'gemma' 세션에 LLM 메시지 추가

        with col_llama:
            msg_llama = chat_message_llm("Llama", "llama3.1:8b", llama)
            llama.append(msg_llama)  # 'llama' 세션에 LLM 메시지 추가
