from datakart import Fss

FSS_KEY = "금융감독원 API 인증키"  # 정기예금 API 인증키 입력
fss = Fss(FSS_KEY)  # Fss 객체 생성
resp = fss.deposit_search()  # 정기예금 API 조회
item = resp.pop(0)  # 첫 번째 데이터 추출
print(f"{item['fin_prdt_nm']}, {item['intr_rate']}")  # 상품명, 금리
