from datakart import Naver


def fetch_naver_local(name: str, category: str) -> dict:
    NAVER_KEY = "Client ID"  # 네이버 서비스 API 'Client ID' 입력
    NAVER_SEC = "Client Secret"  # 네이버 서비스 API 'Client Secret' 입력
    naver = Naver(NAVER_KEY, NAVER_SEC)  # Naver 객체 생성
    kwd = f'"{name}" {category.split(",")[-1]}'  # 상세검색 키워드('"업체명" 카테고리')
    resp = naver.local(kwd)  # 네이버 지역 서비스 검색
    for item in resp.get("items", []):  # 업체 목록 추출
        title = item.get("title", "")  # "<b>업체명</b>" 형식의 업체명
        if title == f"<b>{name}</b>":  # 업체명이 "<b>업체명</b>"과 정확히 같으면 반환
            return dict(
                name=name,  # 업체명
                kwd=kwd,  # 검색 키워드
                title=title,  # "<b>업체명</b>" 형식의 업체명
                category=item.get("category", ""),  # 카테고리
                addr=item.get("roadAddress", ""),  # 도로명 주소
                lonx=item.get("lonx", 0.0),  # 경도(longitude)
                laty=item.get("laty", 0.0),  # 위도(latitude)
            )
    return dict(name=name, kwd=kwd)  # 검색 결과가 없는 경우 업체명과 검색 키워드만 반환


if __name__ == "__main__":
    name, category = "마포양지설렁탕", "곰탕,설렁탕"  # 업체명, 카테고리
    print(fetch_naver_local(name, category))  # 네이버 지역 서비스 검색 결과
