import pandas as pd

from step_2_2 import OUT_2_2  # 이전에 작성한 모듈을 불러옵니다.

df_raw = pd.read_excel(OUT_2_2)
df_pivot_1 = pd.pivot_table(df_raw, index="분류", values="사용금액", aggfunc="sum")
df_pivot_1

df_raw["거래연월"] = df_raw["거래일시"].str.slice(0, 7)
df_raw

df_pivot_2 = pd.pivot_table(df_raw, index="분류", columns="거래연월", values="사용금액", aggfunc="sum")
df_pivot_2["누적금액"] = df_pivot_2.sum(axis=1)
df_pivot_2

df_sort = df_pivot_2.sort_values("누적금액", ascending=False)
df_sort

df_reindex = df_sort.reset_index()
df_reindex

from pathlib import Path

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

df_reindex.to_excel(OUT_DIR / f"{Path(__file__).stem}.xlsx", index=False, sheet_name="분류별누적금액")
