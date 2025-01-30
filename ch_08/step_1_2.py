import json
from pathlib import Path

from datakart import Naver

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.


def query_naver_shop(query: str, display: int = 1) -> dict:
    NAVER_KEY = "Client ID"  # 네이버 서비스 API 'Client ID' 입력
    NAVER_SEC = "Client Secret"  # 네이버 서비스 API 'Client Secret' 입력
    naver = Naver(NAVER_KEY, NAVER_SEC)  # Naver 객체 생성
    return naver.shop(query=query, display=display)


if __name__ == "__main__":
    query = "원피스"  # 검색 키워드
    resp = query_naver_shop(query)  # 네이버 쇼핑 상품 검색
    with open(OUT_DIR / f"{Path(__file__).stem}.json", "w", encoding="utf-8") as fp:
        json.dump(resp, fp, ensure_ascii=False, indent=2)  # JSON으로 저장
