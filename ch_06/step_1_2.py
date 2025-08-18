from playwright.sync_api import Browser, Page, Playwright, sync_playwright


def run_playwright(slow_mo: float = None) -> tuple[Playwright, Browser, Page]:
    play: Playwright = sync_playwright().start()  # Playwright 객체 생성
    browser: Browser = play.chromium.launch(  # Browser 객체 생성
        args=["--start-maximized"],  # 웹 브라우저 최대화
        headless=False,  # 헤드리스 모드 사용 여부
        slow_mo=slow_mo,  # 자동화 처리 지연 시간
    )

    # ⚠️ 코드 업데이트 안내 (2025.08.18)
    # 네이버플러스 스토어 사이트에 직접 접근 시 오류가 발생하므로 코드를 변경해야 합니다.
    # 기존 방법:
    # page: Page = browser.new_page(no_viewport=True)  # Page 객체 생성
    # page.goto("https://shopping.naver.com/ns/home")  # 페이지 이동

    # 💡 해결책: 네이버 메인 페이지를 경유하여 네이버플러스 스토어 사이트에 접근
    context = browser.new_context(no_viewport=True)  # 컨텍스트 객체 생성
    main_page = context.new_page()  # Page 객체 생성
    main_page.goto("https://www.naver.com")  # 1. 네이버 메인 페이지 이동

    # 새 페이지(탭)가 열리기를 기다리는 컨텍스트 블록 시작
    with context.expect_page() as new_page_info:
        main_page.get_by_role("link", name="스토어", exact=True).click(delay=1000)  # 2. 스토어 버튼 클릭

    page = new_page_info.value  # with 블록이 끝나면 page 변수에 새 탭(네이버플러스 스토어)의 Page 객체가 저장됩니다.
    page.wait_for_load_state()  # 페이지 로딩이 완료될 때까지 기다립니다.
    page.add_locator_handler(  # 로케이터 핸들러 등록
        page.get_by_role("button", name="하루 동안 보지 않기"),  # 이 버튼을 찾으면,
        handler=lambda loc: loc.click(),  # 해당 요소를 클릭
        times=1,  # 총 한 번만 실행
    )
    return play, browser, page


if __name__ == "__main__":
    play, browser, page = run_playwright()
    page.pause()  # 인스펙터 실행

    browser.close()  # Browser 객체 삭제
    play.stop()  # Playwright 객체 삭제
