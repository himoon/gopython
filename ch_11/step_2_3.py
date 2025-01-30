from pathlib import Path

import pandas as pd
from datakart import Datagokr
from tqdm import tqdm

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_1 import OUT_2_1

OUT_2_3 = OUT_DIR / f"{Path(__file__).stem}.csv"


def apt_trade_to_csv():
    df_addr = pd.read_csv(OUT_2_1, dtype="string")  # 주소 데이터
    addr_list = df_addr.values.tolist()  # 데이터프레임을 리스트로 변환

    DATAGO_KEY = "공공데이터포털 API 키"  # 공공데이터포털 API 키 입력
    datagokr = Datagokr(DATAGO_KEY)  # Datagokr 객체 생성
    yyyymm_range = [f"2023{m:02}" for m in range(1, 13)]  # 계약년월 생성
    result = []
    with tqdm(total=len(addr_list)) as pbar:  # 진행 표시줄 생성
        for code, addr in addr_list:  # 주소코드와 주소이름
            for yyyymm in yyyymm_range:  # 계약년월 반복 처리
                pbar.set_description(f"[{addr:20}][{code}][{yyyymm}]")
                resp = datagokr.apt_trade(code, yyyymm)  # 아파트 매매 실거래가 조회
                result += resp  # 실거래가 조회 결괏값을 임시 변수에 저장
            pbar.update()  # 진행 표시줄 횟수 업데이트

    df_raw = pd.DataFrame(result)  # 아파트 매매 실거래가를 데이터프레임으로 생성
    df_filter = df_raw.filter(["sggCd", "dealYear", "dealMonth", "dealingGbn", "umdNm", "aptNm", "excluUseAr", "dealAmount", "cdealDay"])
    df_filter.columns = ["지역코드", "계약년도", "계약월", "거래유형", "법정동", "단지명", "전용면적", "거래금액", "해제사유발생일"]

    f_is_real_deal = df_filter["해제사유발생일"].isna()  # 데이터가 있는지 여부 판단
    df_real = df_filter.loc[f_is_real_deal]  # 취소되지 않은 데이터 추출
    df_real = df_real.drop(columns=["해제사유발생일"])  # '해제사유발생일' 열 제거
    df_real.to_csv(OUT_2_3, index=False)  # CSV로 저장


if __name__ == "__main__":
    apt_trade_to_csv()  # 아파트 매매 실거래가를 CSV로 저장
