from pathlib import Path

import streamlit as st

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_3 import OUT_3_3, read_text_and_fill_area

st.title("✌ 만들면서 배우는 문자 인식 웹 앱")  # 웹 앱 제목

uploaded = st.file_uploader("인식할 이미지를 선택하세요.")  # 파일 업로더 위젯
if uploaded is not None:  # 파일이 업로드 되면,
    
    # PaddleOCR 패키지는 'jpg, png, jpeg, bmp, pdf' 확장자를 갖는 파일만 인식하므로, 
    # 임시 파일의 확장자 '.tmp'를 '.tmp.png'로 변경합니다.
    tmp_path = OUT_DIR / f"{Path(__file__).stem}.tmp.png"  # 임시 파일 경로
    tmp_path.write_bytes(uploaded.getvalue())  # 업로드한 이미지 저장

    col_left, col_right = st.columns(2)  # 두 개의 열 생성
    with col_left:  # 첫 번째 열
        st.subheader("원본 이미지")  # 부제목
        st.image(tmp_path.as_posix())  # 원본 이미지 출력
    with col_right:  # 두 번째 열
        st.subheader("문자 인식 결과")  # 부제목
        with st.spinner(text="문자를 인식하는 중입니다..."):  # 진행 상황 표시
            read_text_and_fill_area(tmp_path)  # 문자 인식 및 바운딩 박스 채우기
        st.image(OUT_3_3.as_posix())  # 결과 이미지 출력
