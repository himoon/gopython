from pathlib import Path

from playwright.sync_api import Page

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_2 import run_playwright
from step_1_4 import table_to_dataframe


def goto_market_etf(page: Page):
    page.goto("https://finance.naver.com")
    page.get_by_role("link", name="국내증시").click()
    page.get_by_role("link", name="ETF").click()


def parse_table_etf(page: Page) -> tuple[list, list]:
    tag_table = page.locator("table", has_text="ETF 주요시세정보")  # ETF 표
    tag_thead = tag_table.locator("tbody > tr > th")  # 헤더 열
    header = tag_thead.all_inner_texts()
    tag_tbody = tag_table.locator("tbody > tr")  # 보디 행
    body = []
    for tag_tr in tag_tbody.all():
        texts: list = tag_tr.locator("td").all_inner_texts()
        if not texts:  # <th> 태그의 경우 건너뜀
            continue

        # <img> 태그의 'alt' 속성에 '전일비' 열의 방향('상승', '하락')이 저장
        tag_img = tag_tr.locator("td > img")
        if tag_img.count() > 0:  # <img> 태그 발견 시 다음 코드 실행
            alt_text = tag_img.get_attribute("alt")  # <img> 태그의 'alt' 속성값 추출
            texts[2] = f"{alt_text} {texts[2]}"  # 'alt' 속성값을 '전일비' 열에 반영
        body.append(texts)  # body에 texts 추가
    return header, body


if __name__ == "__main__":
    play, browser, page = run_playwright(slow_mo=1000)
    goto_market_etf(page)  # ETF 페이지로 이동
    header, body = parse_table_etf(page)  # ETF 데이터 수집
    df_raw = table_to_dataframe(header, body)  # 데이터 정제 및 DataFrame 객체 생성
    df_raw.to_csv(OUT_DIR / f"{Path(__file__).stem}.csv", index=False)  # CSV로 저장

    browser.close()
    play.stop()
