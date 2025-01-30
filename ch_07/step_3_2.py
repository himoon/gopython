from pathlib import Path

import pandas as pd
import plotly.express as px

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_1 import OUT_3_1

df_raw = pd.read_csv(OUT_3_1)
fig = px.treemap(
    df_raw,  # 기준 데이터
    path=["종목명"],  # '종목명' 기준으로 데이터 분류
    values="조단위",  # '조단위' 기준으로 종목별 면전 계산
)
fig.update_traces(
    marker=dict(
        cornerradius=5,  # 모서리 둥글게
        colorscale="Plasma",  # 색상
        pad=dict(t=10, r=10, b=10, l=10),  # 트리맵 여백 지정
    ),
    texttemplate="<b>%{label}</b><br>%{value:,.0f}조원",  # 종목명, 시가총액 표시
    textfont_size=30,  # 폰트 크기
)
fig.update_layout(margin=dict(t=0, r=0, b=0, l=0))  # 이미지 여백 지정
img_path = OUT_DIR / f"{Path(__file__).stem}.png"  # 이미지 경로
fig.write_image(img_path, width=1600, height=900, scale=2)  # 이미지 파일로 저장
