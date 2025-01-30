import streamlit as st
from datakart import NaverAd

from step_3_2 import print_dataframe_with_style  # 이전에 작성한 모듈을 불러옵니다.


def init_page_with_dropdown():
    st.set_page_config(layout="wide")  # 웹 페이지 레이아웃을 넓게 설정
    st.header("🧐 만들면서 배우는 연관키워드 경쟁강도 분석")  # 웹 앱 제목 설정
    if "keywords" not in st.session_state:
        st.session_state["keywords"] = ""  # 'keywords' 세션값 초기화
    if "menu_idx" not in st.session_state:
        st.session_state["menu_idx"] = None  # 'menu_idx' 세션값 초기화

    with st.form(key="my_form", border=False):  # 폼 위젯 생성
        col_1, col_2, col_3 = st.columns([2, 2, 1])  # 2:2:1 비율로 열 위젯 생성
        with col_1:  # 첫 번째 열
            st.text_input("키워드", key="keywords", label_visibility="collapsed")
        with col_2:  # 두 번째 열
            st.selectbox(  # 드롭다운 메뉴 출력
                "시즌 테마",  # 드롭다운 메뉴 제목
                key="menu_idx",  # 드롭다운 메뉴 인덱스 값을 저장하기 위한 세션 키
                options=range(len(get_event_codes())),  # 드롭다운 메뉴 추가
                format_func=get_event_name,  # 드롭다운 메뉴에 표시할 텍스트 반환 함수
                index=None,  # 드롭다운 메뉴 기본 인덱스 값
                placeholder="시즌 테마를 선택하세요",  # 드롭다운 메뉴 안내 메시지
                label_visibility="collapsed",  # 드롭다운 메뉴 제목 숨기기
            )
        with col_3:  # 세 번째 열
            st.form_submit_button(label="분석하기", use_container_width=True)


def get_event_codes() -> list[tuple[int, str]]:
    return [(item["id"], item["name_kr"]) for item in NaverAd.get_event_codes()]


def get_event_name(menu_idx: int) -> str:
    event, event_name = get_event_codes()[menu_idx]  # 시즌 테마 추출
    return f"[{event}] {event_name}"


if __name__ == "__main__":
    init_page_with_dropdown()  # 드롭다운 메뉴 추가
    keywords = st.session_state["keywords"]  # 연관 키워드 텍스트 입력 위젯 데이터
    menu_idx = st.session_state["menu_idx"]  # 드롭다운 메뉴의 인덱스 데이터
    if menu_idx is not None:  # 드롭다운 메뉴가 선택되면,
        event, event_name = get_event_codes()[menu_idx]  # 시즌 테마 코드값 저장
        print_dataframe_with_style(keywords=keywords, event=event)
    else:
        print_dataframe_with_style(keywords=keywords)
