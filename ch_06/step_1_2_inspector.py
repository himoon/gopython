from playwright.sync_api import sync_playwright  # sync_playwright 클래스 불러오기

with sync_playwright() as play:  # Playwright 객체 생성
    browser = play.chromium.launch(headless=False)  # Browser 객체 생성

    # ⚠️ 코드 업데이트 안내 (2025.08.18)
    # 네이버플러스 스토어 사이트에 직접 접근 시 오류가 발생하므로 코드를 변경해야 합니다.
    # 기존 방법:
    # page = browser.new_page()  # Page 객체 생성
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
    page.pause()  # 인스펙터 실행
