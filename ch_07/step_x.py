from pathlib import Path

import pandas as pd
from playwright.sync_api import Page
from tqdm import tqdm  # tqdm을 사용하여 진행 상황 표시

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_2 import run_playwright
from step_1_4 import clean_white_space  # 공백 문자 정제 함수


def goto_market_etf(page: Page):
    page.goto("https://finance.naver.com")
    page.get_by_role("link", name="국내증시").click()
    page.get_by_role("link", name="ETF").click()


def parse_table_etf(page: Page) -> tuple[list, list]:
    tag_table = page.locator("table", has_text="ETF 주요시세정보")  # ETF 표
    tag_thead = tag_table.locator("tbody > tr > th")  # 헤더 열
    header = tag_thead.all_inner_texts()  # 헤더 텍스트를 리스트로 가져옴
    tag_tbody = tag_table.locator("tbody > tr")  # 보디 행

    body = []  # 추출한 데이터 저장용 리스트
    count = tag_tbody.count()  # 행의 개수
    with tqdm(total=count) as pbar:  # tqdm을 사용하여 진행 상황 표시(책 343 페이지)
        for i in range(count):  # 각 행을 순회
            tag_tr = tag_tbody.nth(i)  # i번째 행 선택
            texts: list = tag_tr.locator("td").all_inner_texts()  # 각 열의 텍스트를 리스트로 가져옴
            if not texts:  # <th> 태그의 경우 건너뜀
                continue

            # <img> 태그의 'alt' 속성에 '전일비' 열의 방향('상승', '하락')이 저장
            tag_img = tag_tr.locator("td > img")  # <td> 태그 하위의 <img> 태그
            if tag_img.count() > 0:  # <img> 태그 발견 시 다음 코드 블록 실행
                alt_text = tag_img.get_attribute("alt")  # <img> 태그의 'alt' 속성값 추출
                texts[2] = f"{alt_text} {texts[2]}"  # 'alt' 속성값을 '전일비' 열에 반영
            body.append(texts)  # body에 texts 추가

            pbar.update()  # 처리 횟수 업데이트(+1)
            pbar.set_description(f"ETF 데이터 수집: {i + 1}/{count}개 행 처리됨")  # 진행 상황 업데이트
    return header, body


def etf_table_to_dataframe(header: list, body: list) -> pd.DataFrame:
    df_raw = pd.DataFrame(body, columns=header)  # DataFrame 객체 생성
    df_raw = df_raw.dropna(how="any")  # 하나의 열이라도 데이터가 없으면 행 삭제
    for col in df_raw.columns:
        df_raw[col] = df_raw[col].apply(clean_white_space)  # 열별로 공백 문자 정제
    return df_raw


if __name__ == "__main__":
    play, browser, page = run_playwright(slow_mo=1000)
    goto_market_etf(page)  # ETF 페이지로 이동
    header, body = parse_table_etf(page)  # ETF 데이터 수집
    df_raw = etf_table_to_dataframe(header, body)  # 데이터 정제 및 DataFrame 객체 생성
    df_raw.to_csv(OUT_DIR / f"{Path(__file__).stem}.csv", index=False)  # CSV로 저장

    browser.close()
    play.stop()
