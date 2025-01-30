import pandas as pd
from datakart import Sgis

df_hadm_codes = pd.DataFrame(Sgis.hadm_codes())  # 통계지리정보서비스(SGIS) 행정구역코드
df_sido = df_hadm_codes.filter(["시도코드", "시도명칭"]).drop_duplicates()  # 중복 제거
df_reindex = df_sido.set_index("시도명칭")  # "시도명칭" 열을 인덱스로 설정
for region in ["서울특별시", "인천광역시", "경기도"]:
    adm_cd = df_reindex.loc[region, "시도코드"]
    print(f"{region=}, {adm_cd=}")
