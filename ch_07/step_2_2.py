from pathlib import Path

import pandas as pd
from playwright.sync_api import Page

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_2 import run_playwright
from step_1_3 import goto_market_cap, parse_table_kospi
from step_1_4 import table_to_dataframe
from step_2_1 import fetch_total_page

OUT_2_2 = OUT_DIR / f"{Path(__file__).stem}.csv"


def goto_page(page: Page, to: int):
    page.goto(f"https://finance.naver.com/sise/sise_market_sum.naver?&page={to}")


def fetch_market_cap(page: Page) -> pd.DataFrame:
    total_page = fetch_total_page(page)  # 총 페이지 개수 추출
    result = []
    for to in range(1, total_page + 1):  # 1부터 total_page까지 반복
        goto_page(page, to)  # 페이지 이동
        header, body = parse_table_kospi(page)  # 코스피 시가총액 표 추출
        df_raw = table_to_dataframe(header, body)  # 데이터 정제 및 DataFrame 객체 생성
        result.append(df_raw)  # DataFrame 객체를 리스트에 임시 저장
    return pd.concat(result)  # DataFrame 객체 결합


if __name__ == "__main__":
    play, browser, page = run_playwright(slow_mo=1000)
    goto_market_cap(page)  # 시가총액 페이지로 이동
    df_result = fetch_market_cap(page)  # 코스피 시가총액 표 추출
    df_result.to_csv(OUT_2_2, index=False)  # CSV 파일로 저장

    browser.close()
    play.stop()
