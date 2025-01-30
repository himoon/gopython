from pathlib import Path

import pandas as pd
from datakart import Fss

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

OUT_1_2 = OUT_DIR / f"{Path(__file__).stem}.xlsx"


def deposit_info_to_xlsx():
    FSS_KEY = "금융감독원 API 인증키"  # 금융감독원 정기예금 API 인증키 입력
    fss = Fss(FSS_KEY)  # Fss 객체 생성
    resp = fss.deposit_search(fin_grp="은행", intr_rate_type="단리", save_trm="12", join_member="제한없음")  # API 호출
    df_raw = pd.DataFrame(resp)  # 데이터프레임 생성
    df_raw.to_excel(OUT_1_2, index=False)  # 엑셀 파일로 저장


if __name__ == "__main__":
    deposit_info_to_xlsx()  # 정기예금 금리 데이터 수집
