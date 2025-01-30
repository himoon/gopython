import trafilatura


def extract_text_img(url: str) -> tuple[str, str]:
    html = trafilatura.fetch_url(url)
    text = trafilatura.extract(  # 텍스트 추출
        html,
        output_format="markdown",  # 마크다운 형식
        include_comments=False,  # 댓글 제외
    )
    img_url = trafilatura.extract_metadata(html).image
    return text, img_url  # (텍스트, 이미지 URL) 형식으로 반환


if __name__ == "__main__":
    url = "https://www.koreaherald.com/view.php?ud=20240725050618"
    text, img_url = extract_text_img(url)
    print(f"{text=}")
    print(f"{img_url=}")
