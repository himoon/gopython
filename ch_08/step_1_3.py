import json
from pathlib import Path

from datakart import NaverAd

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.


def query_keywords_tool(keywords: str, event: int = None) -> list:
    AD_KEY = "엑세스라이선스"  # 검색광고 API '엑세스라이선스' 입력
    AD_SEC = "비밀키"  # 검색광고 API '비밀키' 입력
    AD_CUST_ID = "CUSTOMER_ID"  # 검색광고 API 'CUSTOMER_ID' 입력
    naver_ad = NaverAd(AD_KEY, AD_SEC, AD_CUST_ID)  # NaverAd 객체 생성
    resp = naver_ad.keywords_tool(keywords=keywords, event=event, show_detail=True)
    return resp.get("keywordList", [])


if __name__ == "__main__":
    keywords = "원피스"  # 검색 키워드
    resp = query_keywords_tool(keywords)  # 연관 키워드 검색
    with open(OUT_DIR / f"{Path(__file__).stem}.json", "w", encoding="utf-8") as fp:
        json.dump(resp, fp, ensure_ascii=False, indent=2)  # JSON으로 저장
