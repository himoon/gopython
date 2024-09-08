from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_2 import OUT_3_2


def load_data(n: int = 4) -> pd.DataFrame:
    df_raw = pd.read_excel(OUT_3_2)
    df_head, df_tail = df_raw.iloc[:n], df_raw.iloc[n:]
    df_sum = df_tail.drop(columns=["분류"]).sum().to_frame().transpose()
    df_sum["분류"] = "기타"
    return pd.concat([df_head, df_sum], ignore_index=True)


if __name__ == "__main__":
    df_raw = load_data()
    values = df_raw["누적금액"]

    fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
    ax.pie(
        values,
        textprops=dict(color="black", size=20),
        startangle=90,
        autopct="%.1f%%",
    )
    fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png", bbox_inches="tight")
