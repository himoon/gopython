import pandas as pd

from step_3_2 import OUT_3_2  # 이전에 작성한 모듈을 불러옵니다.

N = 4
df_raw = pd.read_excel(OUT_3_2)
df_head, df_tail = df_raw.iloc[:N], df_raw.iloc[N:]
df_tail

df_sum = df_tail.drop(columns=["분류"]).sum().to_frame().transpose()
df_sum["분류"] = "기타"
df_sum

df_final = pd.concat([df_head, df_sum], ignore_index=True)
df_final

from pathlib import Path

import matplotlib.pyplot as plt

from step_1 import OUT_DIR

values = df_final["누적금액"]

fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.pie(
    values,
    textprops=dict(color="black", size=20),  # 폰트 설정
    startangle=90,  # 차트 각도 설정
    autopct="%.1f%%",  # 비율 출력 형식 지정
)
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png", bbox_inches="tight")
