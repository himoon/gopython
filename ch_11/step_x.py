import geopandas as gpd
import pandas as pd
from datakart import Sgis

from step_2_1 import OUT_2_1, sido_sgg_to_csv  # 이전에 작성한 모듈을 불러옵니다.
from step_2_3 import apt_trade_to_csv
from step_2_4 import avg_price_to_csv
from step_3_2 import OUT_3_2, adm_cd_to_geojson
from step_3_3 import merge_dataframe
from step_3_4 import geojson_to_img

# 서울특별시, 인천광역시, 경기도 지역주소명 수집
lawd_codes = []
for region in ["서울특별시", "인천광역시", "경기도"]:
    sido_sgg_to_csv(region)  # '시도_시군구' 단위 지역주소명을 CSV로 저장
    lawd_codes.append(pd.read_csv(OUT_2_1, dtype="string"))
df_lawd_codes = pd.concat(lawd_codes)  # 지역주소명 결합
df_lawd_codes.to_csv(OUT_2_1, index=False)  # OUT_2_1 경로에 결과 저장

apt_trade_to_csv()  # 아파트 매매 실거래가 수집
avg_price_to_csv()  # 단위 면적당 평균 실거래가 계산

# 서울특별시, 인천광역시, 경기도 행정구역 경계 데이터 수집
df_hadm_codes = pd.DataFrame(Sgis.hadm_codes())  # SGIS 행정구역코드
df_sido = df_hadm_codes.filter(["시도코드", "시도명칭"]).drop_duplicates()  # 중복 제거
df_reindex = df_sido.set_index("시도명칭")  # "시도명칭" 열을 인덱스로 설정

hadm_area = []
for region in ["서울특별시", "인천광역시", "경기도"]:
    adm_cd = df_reindex.loc[region, "시도코드"]
    adm_cd_to_geojson(adm_cd, "1")  # 행정구역 경계 데이터를 GeoJSON으로 저장
    hadm_area.append(gpd.read_file(OUT_3_2, encoding="utf-8"))
gdf_hadm_area: gpd.GeoDataFrame = pd.concat(hadm_area)  # 지역주소명 결합
json_string: str = gdf_hadm_area.to_json(drop_id=True, ensure_ascii=False, indent=2)
OUT_3_2.write_text(json_string, encoding="utf-8")  # OUT_3_2 경로에 결과 저장

merge_dataframe()  # 아파트 매매 실거래가 데이터와 행정구역 경계 데이터 결합
geojson_to_img()  # GeoJSON 파일을 이미지 파일로 시각화
