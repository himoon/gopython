import ollama
import streamlit as st

from step_2_1 import chat_message_user, init_session_state


def chat_message_llm_stream(role: str, model: str, messages: list) -> dict:
    with st.chat_message(role):  # LLM 메시지 출력
        with st.spinner("대화를 생성하는 중입니다..."):
            # ollama.chat() 함수의 stream 매개변수에 True를 전달
            stream = ollama.chat(model=model, messages=messages, stream=True)

            # 스트림 형식의 반환값에서 메시지 콘텐츠를 추출하는 함수(제네레이터)
            def stream_parser(stream):
                for chunk in stream:
                    yield chunk["message"]["content"]

            # st.write_stream() 함수를 사용하여 스트림 형식의 메시지 콘텐츠를 출력
            content = st.write_stream(stream_parser(stream))
            return dict(role="assistant", content=content)


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    st.title("🤖 만들면서 배우는 챗봇")

    init_session_state(dict(msgs=[], running=False))  # 세션 저장소 초기화
    msgs: list = st.session_state["msgs"]
    running: bool = st.session_state["running"]

    # 사용자가 대화를 입력하면 'running' 세션값을 True로 지정
    if "prompt" in st.session_state and st.session_state["prompt"] is not None:
        running = True
    else:
        running = False

    for row in msgs:  # msgs에 저장된 메시지를 하나씩 반복 처리
        with st.chat_message(row["role"]):
            st.markdown(row["content"])

    # st.chat_input() 함수 호출 시,
    #   1. disabled 매개변수에 'running' 세션값을 전달하여 위젯 활성화 여부를 결정
    #   2. key 매개변수에 'prompt'를 전달하여 사용자의 대화 입력 여부를 체크하는 데 활용
    if prompt := st.chat_input("대화를 입력하세요!", disabled=running, key="prompt"):
        msg_user = chat_message_user(prompt)
        msgs.append(msg_user)  # 사용자 메시지 추가

        msg_llm = chat_message_llm_stream("assistant", "gemma2:9b", msgs)
        msgs.append(msg_llm)  # LLM 메시지 추가

        st.rerun()  # 앱을 재실행하여 'running' 세션값을 재설정
