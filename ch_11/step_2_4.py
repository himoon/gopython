from pathlib import Path

import pandas as pd

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_1 import OUT_2_1
from step_2_3 import OUT_2_3

OUT_2_4 = OUT_DIR / f"{Path(__file__).stem}.csv"


def avg_price_to_csv():
    df_apt = pd.read_csv(OUT_2_3, dtype="string")  # 아파트 매매 실거래가 데이터
    df_apt["거래금액"] = df_apt["거래금액"].str.replace(",", "")  # 콤마 제거
    df_apt = df_apt.astype({"전용면적": float, "거래금액": int})  # 숫자로 변환
    df_apt["면적당금액"] = df_apt["거래금액"] / df_apt["전용면적"]  # 면적당 거래금액
    df_pivot = df_apt.pivot_table(index="지역코드", values=["전용면적", "면적당금액"], aggfunc="mean")
    df_reindex = df_pivot.reset_index(drop=False)  # 데이터프레임의 인덱스 재생성

    df_sido_sgg = pd.read_csv(OUT_2_1, dtype="string")  # 주소 데이터
    df_merge = pd.merge(df_reindex, df_sido_sgg, left_on="지역코드", right_on="sido_sgg", how="inner")
    df_filter = df_merge.filter(["sido_sgg", "locatadd_nm", "전용면적", "면적당금액"])
    df_filter.columns = ["sido_sgg", "locatadd_nm", "avg_area", "avg_price"]
    df_sort = df_filter.sort_values("locatadd_nm")  # 주소이름 기준으로 오름차순 정렬
    df_sort.to_csv(OUT_2_4, index=False)  # CSV로 저장


if __name__ == "__main__":
    avg_price_to_csv()  # 단위 면적당 평균 실거래가를 계산하고 CSV로 저장
