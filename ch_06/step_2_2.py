import json
from pathlib import Path

from playwright.sync_api import Page

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_2 import run_playwright
from step_1_3 import goto_best_goods

OUT_2_2 = OUT_DIR / f"{Path(__file__).stem}.json"


def take_screenshots(page: Page, count: int = 15):
    locs = page.locator("li[class*='productCardResponsive_product_card']").all()
    imgs_path = []  # 이 변수에 검색 결과를 저장
    for idx, loc in enumerate(locs[:count]):  # 상위 count개 li 태그만 추출
        path = OUT_DIR / f"{Path(__file__).stem}_{idx+1:03}.png"  # 캡처 이미지 경로
        loc.screenshot(path=path)  # 화면 캡처
        imgs_path.append(path.as_posix())  # 이미지 경로를 문자열로 변환하여 저장

    with open(OUT_2_2, "w", encoding="utf-8") as fp:  # 이미지 경로를 JSON으로 저장
        json.dump(imgs_path, fp, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    play, browser, page = run_playwright(slow_mo=1000)
    goto_best_goods(page)  # 베스트상품 페이지로 이동
    page.pause()  # 인스펙터 실행

    take_screenshots(page)  # 화면 캡처
    browser.close()
    play.stop()
