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

        # 💡 st.dataframe() 함수의 기본 설정이 변경되어 책과 같이 천 단위 구분 기호가 자동으로 적용되지 않습니다.
        # 숫자 데이터에 천 단위 구분 기호나 소수점 형식을 적용하고 싶다면 아래 주석을 참고하세요.
        # pandas DataFrame 스타일링을 사용하여 데이터 표시 형식을 개선할 수 있습니다.
        #
        # 🔧 적용 방법: 아래 주석 처리된 코드의 주석을 해제하고 위의 st.dataframe() 라인을 주석 처리하면 됩니다.
        #
        # styler = df_result.style.format(  # 데이터프레임 스타일링
        #     {
        #         "검색수M": "{:,}",  # 천 단위 구분 기호를 사용, 소수점 없이 정수로 표시
        #         "클릭수M": "{:,.1f}",  # 소수점 첫째 자리까지 표시
        #         "클릭률M": "{:,.2f}%",  # 소수점 둘째 자리까지 표시, '%' 기호 추가
        #         "상품수": "{:,.0f}",  # 천 단위 구분 기호를 사용, 소수점 없이 정수로 표시
        #         "경쟁강도": "{:,.4f}",  # 소수점 넷째 자리까지 표시
        #     },
        # )
        # st.dataframe(styler, use_container_width=True)  # 스타일링된 데이터프레임 출력


if __name__ == "__main__":
    init_page()  # 웹 앱 기본 설정 및 텍스트 입력 위젯 출력
    keywords = st.session_state["keywords"]  # 연관 키워드 텍스트 입력 위젯 데이터
    print_dataframe(keywords=keywords)  # 데이터프레임 출력
