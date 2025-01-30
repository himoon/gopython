from pathlib import Path

import pandas as pd
from datakart import Ecos

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

ECOS_KEY = "API_KEY"  # ECOS API 인증키 입력
ecos = Ecos(ECOS_KEY)  # Ecos 객체 생성
resp = ecos.stat_search(  # 통계 조회 API 호출
    stat_code="722Y001",  # 통계표코드
    freq="M",  # 주기
    item_code1="0101000",  # 통계항목코드1
    start="202301",  # 검색시작일자
    end="202412",  # 검색종료일자
)
df_raw = pd.DataFrame(resp)  # 데이터프레임 생성
df_raw.to_csv(OUT_DIR / f"{Path(__file__).stem}.csv", index=False)  # CSV로 저장
