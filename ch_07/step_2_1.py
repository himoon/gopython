from playwright.sync_api import Page

from step_1_2 import run_playwright  # 이전에 작성한 모듈을 불러옵니다.
from step_1_3 import goto_market_cap


def fetch_total_page(page: Page) -> int:
    table = page.locator("table", has_text="페이지 네비게이션")  # <table> 태그 추출
    td = table.locator("tbody > tr > td").last  # 마지막 <td> 태그 추출
    href = td.locator("a").get_attribute("href")  # <a> 태그의 href 속성값 추출
    return int(href.split("=")[-1])  # URL에서 페이지 추출


if __name__ == "__main__":
    play, browser, page = run_playwright(slow_mo=1000)
    goto_market_cap(page)  # 시가총액 페이지로 이동
    total_page = fetch_total_page(page)  # 총 페이지 개수 추출
    print(f"{total_page=}")

    browser.close()
    play.stop()
