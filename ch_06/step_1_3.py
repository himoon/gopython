from playwright.sync_api import Page

from step_1_2 import run_playwright  # 이전에 작성한 모듈을 불러옵니다.


def goto_best_goods(page: Page):
    page.goto("https://shopping.naver.com/ns/home")  # 페이지 이동

    # 인스펙터 창에서 복사한 코드 붙여넣기
    page.get_by_role("link", name="베스트 NONE").click()
    page.get_by_role("link", name="베스트상품").click()


if __name__ == "__main__":
    play, browser, page = run_playwright(slow_mo=1000)
    goto_best_goods(page)  # 베스트상품 페이지로 이동
    page.pause()  # 인스펙터 실행

    browser.close()
    play.stop()
