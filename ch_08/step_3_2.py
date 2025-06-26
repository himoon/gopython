import pandas as pd
import streamlit as st
from streamlit.column_config import NumberColumn, ProgressColumn  # 열 스타일 지정

from step_2_4 import OUT_2_4  # 이전에 작성한 모듈을 불러옵니다.
from step_3_1 import analyze_keywords, init_page


def print_dataframe_with_style(keywords: str = None, event: int = None):
    if keywords or event is not None:
        with st.spinner("잠시만 기다려주세요..."):  # 스피너 위젯 생성
            analyze_keywords(keywords=keywords, event=event)  # 연관 키워드 분석
        df_result = pd.read_csv(OUT_2_4)  # 분석 결과를 데이터프레임으로 변환
        max_values = df_result.max().to_dict()  # 열별 최댓값을 딕셔너리로 변환
        st.dataframe(  # 데이터프레임 출력
            df_result,
            use_container_width=True,  # 너비 최대화
            hide_index=True,  # 데이터프레임 인덱스 숨김
            column_config={  # 열별 스타일 설정
                "검색수M": ProgressColumn(width="small", max_value=max_values.get("검색수M", 1), format="localized"),  # format 매개변수에 "localized" 전달하여 천 단위 구분 기호 적용
                "클릭수M": ProgressColumn(width="small", max_value=max_values.get("클릭수M", 1), format="localized"),
                "클릭률M": ProgressColumn(width="small", max_value=max_values.get("클릭률M", 1), format="localized"),
                "상품수": ProgressColumn(width="small", max_value=max_values.get("상품수", 1), format="localized"),
                "경쟁강도": NumberColumn(format="%.2f"),
            },
        )


if __name__ == "__main__":
    init_page()  # 웹 앱 기본 설정 및 텍스트 입력 위젯 출력
    keywords = st.session_state["keywords"]  # 연관 키워드 텍스트 입력 위젯 데이터
    print_dataframe_with_style(keywords=keywords)  # 스타일이 반영된 데이터프레임 출력
