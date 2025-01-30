from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import OUT_2_2

df_raw = pd.read_excel(OUT_2_2, sheet_name="코스피지수", dtype="string")
df_raw["TIME"] = pd.to_datetime(df_raw["TIME"], format="%Y%m%d")  # 날짜 타입으로 변환
df_raw["DATA_VALUE"] = df_raw["DATA_VALUE"].astype(float)  # 부동소수점수 타입으로 변환

# 시각화 스타일 지정(맥OS 환경에서는 매개변수 font에 "Apple SD Gothic Neo"를 입력)
sns.set_theme(context="poster", style="whitegrid", font="Malgun Gothic")
sns.set_style({"grid.linestyle": ":", "grid.color": "#CCCCCC"})

fig, ax = plt.subplots(figsize=(16, 9), dpi=100)  # 이미지 크기 및 해상도 지정
sns.lineplot(data=df_raw, x="TIME", y="DATA_VALUE", ax=ax)  # 선 그래프
sns.despine(top=True, right=True)  # 축 제거 여부 설정

ax.set_title("코스피지수")  # 그래프 제목
ax.set_xlabel("날짜")  # 가로축 제목
ax.set_ylabel("지수")  # 세로축 제목
fig.set_layout_engine("tight")  # 이미지 여백 제거
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png")  # PNG 파일로 저장
