from pathlib import Path

import pandas as pd
from playwright.sync_api import Page

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_3 import search_map
from step_1_4 import parse_names

OUT_1_5 = OUT_DIR / f"{Path(__file__).stem}.csv"


def rotate_pages(page: Page) -> list[str]:
    iframe = page.locator('iframe[title="Naver Place Search"]').content_frame  # 검색 결과 창
    # iframe = page.frame_locator('iframe[title="Naver Place Search"]') # 위와 동일한 코드
    prev_tag = iframe.get_by_role("button", name="이전페이지")  # "이전페이지" 태그
    navi_tag = prev_tag.locator("..")  # "이전페이지" 태그 상위의 <div> 태그
    navi_text = navi_tag.inner_text()  # 페이지 이동 문자열 추출
    digits = [digit for digit in navi_text if digit.isdigit()]  # 페이지 번호 추출

    names = []  # 이 변수에 검색 결과를 저장
    for digit in digits:  # 페이지 번호 목록(예: ["1", "2", "3"])
        navi_tag.get_by_role("button", name=digit).click()  # 페이지 번호 클릭
        page.wait_for_timeout(500)  # 0.5초간 일시정지
        names += parse_names(page)  # 업체명과 카테고리를 추출한 후, 그 결과를 저장
    return names


def fetch_names(kwd: str) -> list[tuple[str, str]]:
    play, browser, page = search_map(kwd)  # 네이버 지도에서 키워드 검색
    names = rotate_pages(page)  # 페이지를 이동하면서 키워드 검색 결과 추출
    browser.close()  # Browser 객체 삭제
    play.stop()  # Playwright 객체 삭제
    return names


if __name__ == "__main__":
    names = fetch_names("미쉐린 서울")  # 네이버 지도에서 키워드 검색 결과 추출
    df_raw = pd.DataFrame(names, columns=["name", "category"])  # 데이터프레임 생성
    df_raw.to_csv(OUT_1_5, index=False, encoding="utf-8")  # CSV로 저장
