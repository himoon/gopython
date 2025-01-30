from pathlib import Path

import pandas as pd

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import OUT_2_2
from step_2_3 import OUT_2_3

OUT_2_4 = OUT_DIR / f"{Path(__file__).stem}.csv"


def comp_lev_to_csv():
    df_kwd = pd.read_csv(OUT_2_2)  # 정제 처리된 연관 키워드
    df_shop = pd.read_csv(OUT_2_3)  # 키워드별 상품 개수
    df_merged = pd.merge(df_kwd, df_shop, left_on="키워드", right_on="키워드")
    df_merged["경쟁강도"] = (df_merged["상품수"] / df_merged["검색수M"]).round(6)

    df_filtered = df_merged.filter(["키워드", "검색수M", "클릭수M", "클릭률M", "상품수", "경쟁강도"])
    df_sorted = df_filtered.sort_values("경쟁강도", ascending=False)  # 내림차순 정렬
    df_sorted.to_csv(OUT_2_4, index=False)  # CSV 파일로 저장


if __name__ == "__main__":
    comp_lev_to_csv()  # 키워드별 경쟁강도 분석
