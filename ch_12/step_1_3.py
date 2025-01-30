from playwright.sync_api import Browser, Page, Playwright

from step_1_2 import run_playwright  # 이전에 작성한 모듈을 불러옵니다.


def search_map(kwd: str) -> tuple[Playwright, Browser, Page]:
    play, browser, page = run_playwright(slow_mo=1000)  # 웹 브라우저 실행
    page.goto("https://map.naver.com")  # 페이지 이동
    page.get_by_label("장소, 버스, 지하철, 도로 검색").click()  # 검색창 클릭
    page.get_by_label("장소, 버스, 지하철, 도로 검색").fill(kwd)  # 키워드 입력
    page.keyboard.press("Enter")  # [Enter] 키 입력
    return play, browser, page


if __name__ == "__main__":
    play, browser, page = search_map("미쉐린 서울")  # 네이버 지도에서 키워드 검색
    page.pause()  # 인스펙터 실행

    browser.close()  # Browser 객체 삭제
    play.stop()  # Playwright 객체 삭제
