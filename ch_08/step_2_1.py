from pathlib import Path

import pandas as pd

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_3 import query_keywords_tool

OUT_2_1 = OUT_DIR / f"{Path(__file__).stem}.csv"


def rel_kwd_to_csv(keywords: str = None, event: int = None):
    resp = query_keywords_tool(keywords=keywords, event=event)  # 연관 키워드 검색
    df_raw = pd.DataFrame(resp)  # 데이터프레임 생성
    df_raw.columns = ["키워드", "검색수PC", "검색수M", "클릭수PC", "클릭수M", "클릭률PC", "클릭률M", "광고수", "경쟁정도"]
    df_raw.to_csv(OUT_2_1, index=False)  # CSV로 저장


if __name__ == "__main__":
    rel_kwd_to_csv("나이키")  # 연관 키워드 수집
