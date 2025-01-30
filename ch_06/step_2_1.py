from playwright.sync_api import Page

from step_1_2 import run_playwright  # 이전에 작성한 모듈을 불러옵니다.
from step_1_3 import goto_best_goods


def select_category(page: Page, category: str = None):
    selector = "li[class*='imageCategoryResponsive_list'] > button"
    page.locator(selector, has_text=category).click()  # 카테고리 버튼 클릭


def select_options(page: Page, option: str = None):
    page.get_by_role("button", name="모두가 좋아하는 레이어 열기").click()
    page.get_by_text(option).click()  # 세부 옵션 버튼 클릭


if __name__ == "__main__":
    play, browser, page = run_playwright(slow_mo=1000)
    goto_best_goods(page)  # 베스트상품 페이지로 이동
    select_category(page, "패션의류")  # 카테고리 클릭
    select_options(page, "10대 여성")  # 세부 옵션 클릭
    page.pause()

    browser.close()
    play.stop()
