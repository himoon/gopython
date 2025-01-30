from pathlib import Path

import streamlit as st
from PIL import ImageFile

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_2 import upload_image
from step_1_3 import clear_session, init_session
from step_2_2 import synth_speech
from step_3_1 import generate_quiz


def init_page():
    st.set_page_config(layout="wide")
    st.title("🔊 만들면서 배우는 영어 받아쓰기 웹 앱")
    init_session(dict(quiz=[], answ=[], audio=[], voice="en-US-Journey-F"))


def set_quiz(img: ImageFile.ImageFile):  # 퀴즈 출제 위젯
    if img and not st.session_state["quiz"]:  # 'quiz' 세션값이 없으면 퀴즈 출제
        with st.spinner("문제를 출제중입니다...🤯"):
            quiz, answ = generate_quiz(img)  # 퀴즈 생성

            audio = []
            for idx, sent in enumerate(answ):  # 문장별로 음성 파일 생성
                wav_file = synth_speech(sent, st.session_state["voice"], "wav")
                path = OUT_DIR / f"{Path(__file__).stem}_{idx}.wav"
                with open(path, "wb") as fp:
                    fp.write(wav_file)  # 음성 파일 저장
                    audio.append(path.as_posix())  # 파일 경로를 문자열로 저장

            st.session_state["quiz"] = quiz  # 퀴즈 저장
            st.session_state["answ"] = answ  # 정답 저장
            st.session_state["audio"] = audio  # 음성 저장


def reset_quiz():  # 퀴즈 재출제 위젯
    if st.session_state["quiz"]:  # 'quiz' 세션값이 있으면 퀴즈 재출제 위젯 출력
        with st.form("form_reset", border=False):
            if st.form_submit_button(label="새로운 문제 풀어보기", use_container_width=True, type="primary"):
                clear_session()  # 세션 삭제
                st.rerun()  # 앱 재실행


if __name__ == "__main__":
    init_page()  # 페이지 초기화
    if img := upload_image(on_change=clear_session):  # 이미지 등록
        set_quiz(img)  # 퀴즈 출제
        st.write(st.session_state["quiz"])  # 'quiz' 세션값 출력
        reset_quiz()  # 퀴즈 재출제
