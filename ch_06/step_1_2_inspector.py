from playwright.sync_api import sync_playwright  # sync_playwright 클래스 불러오기

with sync_playwright() as play:  # Playwright 객체 생성
    browser = play.chromium.launch(headless=False)  # Browser 객체 생성
    page = browser.new_page()  # Page 객체 생성
    page.goto("https://shopping.naver.com/ns/home")  # 페이지 이동
    page.pause()  # 인스펙터 실행
