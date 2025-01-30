import geopandas as gpd
from datakart import Sgis

SGIS_KEY, SGIS_SECRET = "서비스 ID", "보안 Key"  # 통계지리정보서비스 API 서비스 ID, 보안 Key 입력
sgis = Sgis(SGIS_KEY, SGIS_SECRET)  # Sgis 객체 생성
resp: str = sgis.hadm_area(adm_cd="11", low_search="1")  # 행정구역 경계 데이터 조회
gdf_resp: gpd.GeoDataFrame = gpd.read_file(resp)  # 지오데이터프레임으로 변환
gdf_resp.head(3)  # 첫 3개 행 출력

gdf_resp.plot()  # 행정구역 경계 데이터 시각화
