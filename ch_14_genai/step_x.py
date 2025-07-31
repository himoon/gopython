import streamlit as st

from step_1_2 import upload_image  # 이전에 작성한 모듈을 불러옵니다.
from step_1_3 import clear_session
from step_2_1 import list_voices
from step_3_2 import init_page, set_quiz
from step_3_3 import show_quiz


def show_voice_selector():  # 보이스 선택 위젯
    with st.sidebar:
        with st.form("form_voice", border=True):
            voices_en = list_voices("en")  # 영어 보이스 목록
            names = [vo["name"] for vo in voices_en]  # 보이스 이름
            genders = [vo["gender"] for vo in voices_en]  # 보이스 성별
            voice = st.selectbox(
                "보이스 목록",
                index=names.index(st.session_state["voice"]),  # 현재 선택한 보이스
                options=names,  # 보이스 목록
                format_func=lambda vo: f"{vo}({genders[names.index(vo)]})",  # 출력 양식
                label_visibility="collapsed",
            )
            if st.form_submit_button(label="보이스 변경하기", use_container_width=True, type="primary"):
                st.session_state["voice"] = voice  # 'voice' 세션값 지정
                clear_session("voice")  # 'voice' 세션을 제외한 세션 삭제
                st.rerun()  # 앱 재실행


def reset_quiz():  # 퀴즈 재출제 위젯
    if st.session_state["quiz"]:  # 'quiz' 세션값이 있으면 퀴즈 재출제 위젯 출력
        with st.form("form_reset", border=False):
            if st.form_submit_button(label="새로운 문제 풀어보기", use_container_width=True, type="primary"):
                clear_session("voice")  # 'voice' 세션을 제외한 세션 삭제
                st.rerun()  # 앱 재실행


if __name__ == "__main__":
    init_page()  # 페이지 초기화
    if img := upload_image(on_change=clear_session, args=("voice",)):  # 이미지 등록
        show_voice_selector()  # 보이스 선택 위젯
        set_quiz(img)  # 퀴즈 출제
        show_quiz()  # 퀴즈 출력
        reset_quiz()  # 퀴즈 재출제
