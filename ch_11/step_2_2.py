import pandas as pd
from datakart import Datagokr

DATAGO_KEY = "공공데이터포털 API 키"  # 공공데이터포털 API 키 입력
datagokr = Datagokr(DATAGO_KEY)  # Datagokr 객체 생성
resp = datagokr.apt_trade("11680", "202312")  # 아파트 매매 실거래가 조회
df_raw = pd.DataFrame(resp)  # 아파트 매매 실거래가를 데이터프레임으로 생성
df_filter = df_raw.filter(["sggCd", "dealYear", "dealMonth", "dealingGbn", "umdNm", "aptNm", "excluUseAr", "dealAmount", "cdealDay"])
df_filter.columns = ["지역코드", "계약년도", "계약월", "거래유형", "법정동", "단지명", "전용면적", "거래금액", "해제사유발생일"]
df_filter.head(3)  # 첫 3개 행 데이터 출력
