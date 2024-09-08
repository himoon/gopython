from pathlib import Path

import pandas as pd

from step_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

OUT_2_2 = OUT_DIR / f"{Path(__file__).stem}.xlsx"

if __name__ == "__main__":
    result = []
    for xlsx_path in Path(IN_DIR).glob("2024년*월.xlsx"):
        df_raw = pd.read_excel(xlsx_path, sheet_name="Sheet1", skiprows=2, usecols="B:E")
        result.append(df_raw)

    df_concat = pd.concat(result)
    df_concat.to_excel(OUT_2_2, index=False)
