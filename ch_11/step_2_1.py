from pathlib import Path

import pandas as pd
from datakart import Datagokr

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

OUT_2_1 = OUT_DIR / f"{Path(__file__).stem}.csv"


def sido_sgg_to_csv(region: str = None):
    DATAGO_KEY = "공공데이터포털 API 키"  # 공공데이터포털 API 키 입력
    datago = Datagokr(DATAGO_KEY)  # Datagokr 객체 생성
    resp = datago.lawd_code(region)  # 법정동 데이터 수집
    df_raw = pd.DataFrame(resp)  # 데이터프레임 생성
    df_raw["sido_sgg"] = df_raw["sido_cd"] + df_raw["sgg_cd"]  # '시도_시군구' 열 생성

    f_no_sgg = df_raw["sgg_cd"] == "000"  # 시군구 코드값이 '000'인 경우
    f_no_umd = df_raw["umd_cd"] == "000"  # 읍면동 코드값이 '000'인 경우
    f_no_ri = df_raw["ri_cd"] == "00"  # 리 코드값이 '00'인 경우
    f_only_sgg = (~f_no_sgg) & (f_no_umd) & (f_no_ri)  # 시군구 코드값만 있는 경우
    df_sliced = df_raw.loc[f_only_sgg]  # 데이터프레임에서 시군구 코드값 추출

    df_filter = df_sliced.filter(["sido_sgg", "locatadd_nm"])  # 사용할 열 필터링
    df_sort = df_filter.sort_values("locatadd_nm")  # 지역주소명으로 오름차순 정렬
    df_result = df_sort.reset_index(drop=True)  # 데이터프레임 인덱스 재생성
    df_result.to_csv(OUT_2_1, index=False)  # CSV로 저장


if __name__ == "__main__":
    region = "서울특별시"
    sido_sgg_to_csv(region)  # '시도_시군구' 단위 지역주소명을 CSV로 저장
