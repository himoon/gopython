from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_2 import OUT_3_2

df_raw = pd.read_excel(OUT_3_2)

sns.set_theme(context="poster", style="whitegrid", font="Apple SD Gothic Neo")
sns.set_style({"grid.linestyle": "--", "grid.color": "#EEEEEE"})  # 그리드 설정

fig, ax = plt.subplots(figsize=(20, 10), dpi=100)
sns.barplot(data=df_raw, x="분류", y="누적금액", hue="분류", ax=ax)  # 바 차트 생성
sns.despine(top=True, right=True, bottom=True, left=True)  # 축 경계선 설정

ticks = ax.get_yticks()  # y축 눈금
ticks_label = [f"{int(tick):,}" for tick in ticks]  # 눈금 형식 변경
ax.set_yticks(ticks[:-1], ticks_label[:-1])  # y축 눈금 설정
ax.set_title("분류별 누적 사용금액")


fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png", bbox_inches="tight")
