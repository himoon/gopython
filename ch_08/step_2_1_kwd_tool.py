from datakart import NaverAd

AD_KEY = "엑세스라이선스"  # 검색광고 API '엑세스라이선스' 입력
AD_SEC = "비밀키"  # 검색광고 API '비밀키' 입력
AD_CUST_ID = "CUSTOMER_ID"  # 검색광고 API 'CUSTOMER_ID' 입력
naver_ad = NaverAd(AD_KEY, AD_SEC, AD_CUST_ID)  # NaverAd 객체 생성
resp = naver_ad.keywords_tool(keywords="화장품")  # 연관 키워드 검색
print([row["relKeyword"] for row in resp["keywordList"]])  # ['화장품', '한방화장품', ...]

resp = naver_ad.keywords_tool(event=86)  # '반려동물' 시즌 테마 연관 키워드 검색
print([row["relKeyword"] for row in resp["keywordList"]])  # ['동물병원', '애견미용', ...]
