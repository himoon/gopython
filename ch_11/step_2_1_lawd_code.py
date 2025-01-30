from datakart import Datagokr

DATAGO_KEY = "공공데이터포털 API 키"  # 공공데이터포털 API 키 입력
datago = Datagokr(DATAGO_KEY)  # Datagokr 객체 생성
resp = datago.lawd_code("서울특별시")  # 법정동 데이터 조회
print(resp)
