from playwright.sync_api import Page

from step_1_3 import search_map  # 이전에 작성한 모듈을 불러옵니다.


def parse_names(page: Page) -> list[tuple[str, str]]:
    iframe = page.locator('iframe[title="Naver Place Search"]').content_frame  # 검색 결과 창
    # iframe = page.frame_locator('iframe[title="Naver Place Search"]') # 위와 동일한 코드
    while iframe.locator("ul > div").count() > 0:  # ul 바로 하위의 div가 발견되면,
        iframe.locator("ul > div").last.scroll_into_view_if_needed()  # div로 이동
        page.wait_for_timeout(500)  # 0.5초간 일시정지

    names = []  # 이 변수에 검색 결과를 저장
    for tag_li in iframe.locator("ul > li").all():  # ul 바로 하위의 모든 li 추출
        tag_a = tag_li.locator("a").first  # li 하위의 a 태그 중 첫 번째
        tag_span = tag_a.locator("span")  # a 태그 하위의 span 태그
        name = tag_span.first.inner_text()  # 첫 번째 span의 텍스트는 업체명
        category = tag_span.last.inner_text()  # 마지막 span의 텍스트는 카테고리
        names.append((name, category))  # (업체명, 카테고리) 형식으로 결과를 저장
    return names


if __name__ == "__main__":
    play, browser, page = search_map("미쉐린 서울")  # 네이버 지도에서 키워드 검색
    names = parse_names(page)  # 업체명과 카테고리 추출
    print(names)

    browser.close()  # Browser 객체 삭제
    play.stop()  # Playwright 객체 삭제
