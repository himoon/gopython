import pandas as pd
import streamlit as st

from step_2_1 import rel_kwd_to_csv  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import data_cleaning
from step_2_3 import shop_cnt_to_csv
from step_2_4 import OUT_2_4, comp_lev_to_csv


def init_page():
    st.set_page_config(layout="wide")  # 웹 페이지 레이아웃을 넓게 설정
    st.header("🧐 만들면서 배우는 연관키워드 경쟁강도 분석")  # 웹 앱 제목 설정
    if "keywords" not in st.session_state:
        st.session_state["keywords"] = ""  # 'keywords' 세션값 초기화

    with st.form(key="my_form", border=False):  # 폼 위젯 생성
        col_1, col_2 = st.columns([3, 1])  # 3:1 비율로 두 개의 열 위젯 생성
        with col_1:  # 첫 번째 열
            st.text_input("키워드", key="keywords", label_visibility="collapsed")
        with col_2:  # 두 번째 열
            st.form_submit_button(label="분석하기", use_container_width=True)


def analyze_keywords(keywords: str = None, event: int = None):
    rel_kwd_to_csv(keywords=keywords, event=event)  # 연관 키워드 수집
    data_cleaning()  # 데이터 정제
    shop_cnt_to_csv()  # 키워드별 상품 개수 수집
    comp_lev_to_csv()  # 키워드별 경쟁강도 분석


def print_dataframe(keywords: str = None):
    if keywords:
        with st.spinner("잠시만 기다려주세요..."):  # 스피너 위젯 생성
            analyze_keywords(st.session_state["keywords"])  # 연관 키워드 분석
        df_result = pd.read_csv(OUT_2_4)  # 분석 결과를 데이터프레임으로 변환
        st.dataframe(df_result, use_container_width=True)  # 데이터프레임 출력


if __name__ == "__main__":
    init_page()  # 웹 앱 기본 설정 및 텍스트 입력 위젯 출력
    keywords = st.session_state["keywords"]  # 연관 키워드 텍스트 입력 위젯 데이터
    print_dataframe(keywords=keywords)  # 데이터프레임 출력
