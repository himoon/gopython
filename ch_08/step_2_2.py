from pathlib import Path

import pandas as pd

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_1 import OUT_2_1

OUT_2_2 = OUT_DIR / f"{Path(__file__).stem}.csv"


def data_cleaning():
    df_raw = pd.read_csv(OUT_2_1, dtype="string")  # CSV 파일에서 DataFrame 객체 생성
    f_pc_cnt = df_raw["검색수PC"].str.contains("<")  # "<" 문자열 포함 여부
    f_mo_cnt = df_raw["검색수M"].str.contains("<")
    df_sliced = df_raw.loc[(~f_pc_cnt) & (~f_mo_cnt)]  # NOT(~)과 AND(&) 조건

    df_sliced = df_sliced.astype({"검색수M": int, "클릭률M": float})  # 데이터 타입 변환
    f_mo_cnt_cond = df_sliced["검색수M"] >= 10_000  # 검색수 조건
    f_mo_rate_cond = df_sliced["클릭률M"] >= 1.0  # 클릭률 조건
    df_cond = df_sliced.loc[(f_mo_cnt_cond) & (f_mo_rate_cond)]  # AND(&) 조건
    df_sorted = df_cond.sort_values(["검색수M"], ascending=[False])  # 정렬
    df_sorted.to_csv(OUT_2_2, index=False)  # CSV로 저장


if __name__ == "__main__":
    data_cleaning()  # 데이터 정제
