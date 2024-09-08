import pandas as pd

from step_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.

df_raw = pd.read_excel(IN_DIR / "2024년1월.xlsx", sheet_name="Sheet1", usecols="B:E", skiprows=2)
df_raw
