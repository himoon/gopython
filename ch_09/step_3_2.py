from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import OUT_2_2

# 시각화 스타일 지정(맥OS 환경에서는 매개변수 font에 "Apple SD Gothic Neo"를 입력)
sns.set_theme(context="poster", style="whitegrid", font="Malgun Gothic")
sns.set_style({"grid.linestyle": ":", "grid.color": "#CCCCCC"})

fig, axes = plt.subplots(figsize=(16, 9), dpi=100, nrows=2, ncols=2)
sheet_names = [["국고채", "회사채"], ["코스피지수", "원달러환율"]]
for idx_row, row in enumerate(sheet_names):
    for idx_col, name in enumerate(row):
        df_raw = pd.read_excel(OUT_2_2, sheet_name=name, dtype="string")
        df_raw["TIME"] = pd.to_datetime(df_raw["TIME"], format="%Y%m%d")
        df_raw["DATA_VALUE"] = df_raw["DATA_VALUE"].astype(float)
        df_tail = df_raw.tail(100)  # 마지막 100개의 데이터만 사용

        ax: Axes = axes[idx_row][idx_col]  # 시각화에 사용할 Axes 객체 지정
        sns.lineplot(data=df_tail, x="TIME", y="DATA_VALUE", ax=ax)
        sns.despine(top=True, right=True, bottom=True, left=True)

        ax.set_title(name)  # 그래프 제목
        ax.xaxis.set_visible(False)  # 가로축 전체 숨김
        ax.set_ylabel(None)  # 세로축 제목 제거
        ax.set_facecolor("#EEEEEE")  # 배경색 지정

fig.set_layout_engine("tight")  # 이미지 여백 제거
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png")  # PNG 파일로 저장
