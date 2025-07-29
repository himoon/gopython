import streamlit as st

button = st.button("눌러보세요 👉")  # 버튼 위젯
print(f"{button=}")  # button=True 또는 False

text = st.text_input("텍스트를 입력하세요 ✍️")  # 텍스트 입력 위젯
print(f"{text=}")  # text='Hello, World!'

uploaded = st.file_uploader("파일을 선택하세요 📦")  # 파일 업로더 위젯
if uploaded is not None:  # 파일이 업로드되면, 다음 코드를 실행
    print(f"{uploaded}")  # UploadedFile(name='billboard.jpg', ...)
    print(f"{uploaded.getvalue()[:10]}")  # b'\xff\xd8\xff\xe0\x00\x10JFIF'
