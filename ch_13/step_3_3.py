import ollama
import streamlit as st

from step_1_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_1 import extract_text_img

SYSTEM_PROMPT = (IN_DIR / "system.txt").read_text(encoding="utf-8")  # 시스템 프롬프트

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    st.title("📰 만들면서 배우는 기사 번역 웹 앱")

    with st.form("form", border=False):
        col_url, col_submit = st.columns([9, 1])  # 9:1 비율로 두 개의 열 생성
        with col_url:  # URL 입력 위젯
            url = st.text_input(
                "text_input",  # 위젯 이름
                placeholder="URL을 입력하세요!",
                label_visibility="collapsed",  # 위젯 이름 출력 방지
            )
        with col_submit:  # '번역하기' 버튼 위젯
            submitted = st.form_submit_button("번역하기", use_container_width=True)

    if submitted:
        st.write(f"(Source) {url}")  # 기사 원문 출처 표시
        text, img_url = extract_text_img(url)  # 기사 원문 및 이미지 URL 추출

        col_input, col_output = st.columns(2)
        with col_input:
            st.image(img_url, use_container_width=True)  # 기사 이미지 출력
            st.markdown(text)  # 기사 원문 출력
        with col_output:
            with st.spinner("번역하는 중입니다..."):
                msgs = [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": text},
                ]
                resp = ollama.chat(
                    model="gemma2:9b",
                    messages=msgs,
                    options=dict(temperature=0.2),  # 온도 옵션 설정
                )
                msg_llm = resp.get("message", {})
                st.markdown(msg_llm["content"])  # 번역 결과 출력
