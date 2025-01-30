import json

import trafilatura

url = "https://www.koreaherald.com/view.php?ud=20240725050618"
html: str = trafilatura.fetch_url(url)  # HTML 수집
extracted: str = trafilatura.extract(  # 텍스트 추출
    html,
    output_format="json",  # "csv", "html", "json", "markdown", "txt", "xml" 등 가능
    with_metadata=True,  # 제목, 작성자 등 메타 데이터 포함
)
parsed = json.loads(extracted)  # JSON 형식의 텍스트 문자열 불러오기
print(parsed)
