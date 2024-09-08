from pathlib import Path

import pandas as pd

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import OUT_2_2

OUT_3_2 = OUT_DIR / f"{Path(__file__).stem}.xlsx"

if __name__ == "__main__":
    df_raw = pd.read_excel(OUT_2_2)
    df_raw["거래연월"] = df_raw["거래일시"].str.slice(0, 7)

    df_pivot = pd.pivot_table(df_raw, index="분류", columns="거래연월", values="사용금액", aggfunc="sum")
    df_pivot["누적금액"] = df_pivot.sum(axis=1)

    df_sort = df_pivot.sort_values("누적금액", ascending=False)
    df_reindex = df_sort.reset_index()
    df_reindex.to_excel(OUT_3_2, index=False, sheet_name="분류별누적금액")
