import streamlit as st

from step_1_2 import upload_image
from step_1_3 import clear_session, init_session
from step_3_1 import generate_feedback
from step_3_2 import init_page, reset_quiz, set_quiz


def show_quiz():  # 퀴즈 출력 위젯
    zipped = zip(  # 퀴즈 순서, 퀴즈, 정답, 음성 파일 경로를 하나의 세트로 관리
        range(len(st.session_state["quiz"])),  # 퀴즈 순서
        st.session_state["quiz"],  # 퀴즈
        st.session_state["answ"],  # 정답
        st.session_state["audio"],  # 음성 파일 경로
    )
    for idx, quiz, answ, audio in zipped:
        key_input, key_feedback = f"input_{idx}", f"feedback_{idx}"
        init_session({key_input: "", key_feedback: ""})  # 세션 초기화

        with st.form(f"form_question_{idx}", border=True):
            st.success(f"### {quiz}")  # 퀴즈 출력
            st.audio(audio)  # 음성 출력

            col_user_input, col_submit = st.columns([8, 2])
            with col_user_input:  # 사용자 입력 위젯
                user_input = st.text_input(
                    key_input,  # 위젯 이름
                    value=st.session_state[key_input],  # 위젯 값
                    key=key_input,  # 위젯 세션 키
                    label_visibility="collapsed",
                )
            with col_submit:  # 정답 제출 위젯
                submitted = st.form_submit_button("정답 제출", use_container_width=True)
            if user_input and submitted:
                with st.spinner():
                    feedback = generate_feedback(user_input, answ)  # 피드백 생성
                    st.session_state[key_feedback] = feedback  # 세션에 피드백 저장

            if st.session_state[key_feedback]:  # 피드백 세션값이 있는 경우, 피드백 출력
                with st.expander("해설 보기", expanded=True):
                    st.markdown(st.session_state[key_feedback])


if __name__ == "__main__":
    init_page()  # 페이지 초기화
    if img := upload_image(on_change=clear_session):  # 이미지 등록
        set_quiz(img)  # 퀴즈 출제
        show_quiz()  # 퀴즈 출력
        reset_quiz()  # 퀴즈 재출제
