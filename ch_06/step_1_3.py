from playwright.sync_api import Page

from step_1_2 import run_playwright  # 이전에 작성한 모듈을 불러옵니다.


def goto_best_goods(page: Page):
    # 인스펙터 창에서 복사한 코드 붙여넣기
    # ⚠️ 코드 업데이트 안내 (2026.07.07)
    # 기존 방법:
    # page.get_by_role("link", name="베스트 NONE").click()

    # 💡 해결책: exact=True를 사용해 이름이 정확히 '베스트'인 링크를 클릭
    # (참고) 여러 개의 '베스트' 관련 버튼이 추가되면서 정확히 원하는 메뉴를 특정하지 못하는 문제가 있었기 때문에,
    # 이름이 정확히 '베스트'인 버튼만 선택하도록 방식을 변경했습니다.
    page.get_by_role("link", name="베스트", exact=True).click()
    page.get_by_role("link", name="베스트상품").click()


if __name__ == "__main__":
    play, browser, page = run_playwright(slow_mo=1000)
    goto_best_goods(page)  # 베스트상품 페이지로 이동
    page.pause()  # 인스펙터 실행

    browser.close()
    play.stop()
