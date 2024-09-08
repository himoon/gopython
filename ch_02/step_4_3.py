from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_4_2 import load_data


def custom_autopct(pct, total):
    real_val = int(pct / 100 * total)
    return f"{real_val:,}원\n({pct:.1f}%)"


df_raw = load_data()
labels, values = df_raw["분류"], df_raw["누적금액"]

sns.set_theme(context="poster", font="Apple SD Gothic Neo")
fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.pie(
    values,
    textprops=dict(color="white", size=20),
    startangle=90,
    autopct=lambda pct: custom_autopct(pct, sum(values)),
)
ax.legend(labels, bbox_to_anchor=(1, 0.5), loc="center left")
ax.set_title(f"1분기에는 {labels[0]}에 {values[0]:,}원을 사용했습니다.")

fig.suptitle("1분기 카드 사용 내역")
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png", bbox_inches="tight")
