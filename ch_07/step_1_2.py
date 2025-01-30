from playwright.sync_api import Browser, Page, Playwright, sync_playwright


def run_playwright(slow_mo: float = None) -> tuple[Playwright, Browser, Page]:
    play: Playwright = sync_playwright().start()  # Playwright 객체 생성
    browser: Browser = play.chromium.launch(  # Browser 객체 생성
        args=["--start-maximized"],  # 웹 브라우저 최대화
        headless=False,  # 헤드리스 모드 사용 여부
        slow_mo=slow_mo,  # 자동화 처리 지연 시간
    )
    page: Page = browser.new_page(no_viewport=True)  # Page 객체 생성
    return play, browser, page


if __name__ == "__main__":
    play, browser, page = run_playwright()
    page.goto("https://finance.naver.com")  # 네이버페이 증권 웹 사이트로 이동
    page.pause()  # 인스펙터 실행

    browser.close()  # Browser 객체 삭제
    play.stop()  # Playwright 객체 삭제
