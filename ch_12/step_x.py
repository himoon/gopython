import pandas as pd
import streamlit as st
from streamlit_folium import st_folium  # Streamlit 환경에서 Folium 지도 출력

from step_3_1 import load_data  # 이전에 작성한 모듈을 불러옵니다.
from step_3_2 import add_marker_cluster


@st.cache_data  # 데이터 캐싱을 통해 동일한 입력값에 대해 함수 재실행 방지
def load_data_by_category(category: str) -> pd.DataFrame:
    df_raw = load_data()  # 데이터 로딩 및 데이터프레임 생성
    if category in ["한식", "일식", "중식"]:
        df_raw = df_raw.loc[df_raw["category"].str.contains(category)]
    elif category == "기타":
        # 'category' 열에 한식, 일식, 중식을 포함하지 않는 행만 슬라이싱
        df_raw = df_raw.loc[~df_raw["category"].str.contains("한식|일식|중식")]
    return df_raw


if __name__ == "__main__":
    st.set_page_config(layout="wide")  # 페이지 레이아웃을 넓게 설정
    st.header("🍴만들면서 배우는 맛집 지도 그리기")  # 웹 앱 제목 설정
    category = st.selectbox(  # 카테고리 선택을 위한 드롭다운 메뉴 출력
        "카테고리",  # 드롭다운 메뉴 제목
        options=["전체", "한식", "일식", "중식", "기타"],  # 드롭다운 옵션 목록
        index=None,  # 기본 선택값을 지정하지 않음
        placeholder="카테고리를 선택하세요.",  # 옵션 선택 전 표시될 안내 문구
        label_visibility="collapsed",  # 드롭다운 메뉴 제목을 표시하지 않음
    )
    if category:  # 사용자가 드롭다운 옵션을 선택한 경우
        with st.container():  # 컨테이너 위젯 생성(지도의 가로, 세로 길이 제한 목적)
            df_raw = load_data_by_category(category)  # 맛집 데이터 불러오기
            map = add_marker_cluster(df_raw)  # 지도 생성 및 마커 클러스터 추가
            st_folium(  # Folium 지도를 Streamlit 환경의 웹 앱에 출력
                map,  # Folium 지도
                use_container_width=True,  # 가로 길이를 최대로 설정
                height=400,  # 세로 길이 설정
                returned_objects=[],  # 사용자 입력을 무시(웹 앱 재실행 방지 목적)
            )
