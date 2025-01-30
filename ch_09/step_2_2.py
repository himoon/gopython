from pathlib import Path

import pandas as pd
from datakart import Ecos

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

OUT_2_2 = OUT_DIR / f"{Path(__file__).stem}.xlsx"


def ecos_to_xlsx():
    ECOS_KEY = "API_KEY"  # ECOS API 인증키 입력
    CODE_LIST = [  # [지표명, 통계표코드, 주기, 통계항목코드, 요청건수]
        ["기준금리", "722Y001", "D", "0101000", 1000],
        ["국고채", "817Y002", "D", "010200000", 1000],
        ["회사채", "817Y002", "D", "010300000", 1000],
        ["코스피지수", "802Y001", "D", "0001000", 1000],
        ["원달러환율", "731Y001", "D", "0000001", 1000],
    ]

    with pd.ExcelWriter(OUT_2_2) as writer:  # ExcelWriter 객체 생성
        ecos = Ecos(ECOS_KEY)  # Ecos 객체 생성
        for name, stat_code, freq, item_code1, limit in CODE_LIST:
            resp = ecos.stat_search(  # 통계 조회 API 호출
                stat_code=stat_code,  # 통계표코드
                freq=freq,  # 주기
                item_code1=item_code1,  # 통계항목코드1
                limit=limit,  # 요청건수
            )
            df_raw = pd.DataFrame(resp)  # 데이터프레임 생성
            df_raw.to_excel(writer, sheet_name=name, index=False)  # 엑셀로 저장


if __name__ == "__main__":
    ecos_to_xlsx()
