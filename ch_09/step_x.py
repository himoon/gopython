from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from datakart import Ecos

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

ECOS_KEY = "9NPPLWUVZGMSFQP0CL23"  # ECOS API 인증키 입력
CODE_LIST = [  # [지표명, 통계표코드, 주기, 통계항목코드, 검색시작일자, 검색종료일자]
    ["국고채", "721Y001", "M", "5020000", "202101", "202412"],
    ["회사채", "721Y001", "M", "7020000", "202101", "202412"],
]
ecos = Ecos(ECOS_KEY)  # Ecos 객체 생성
data = []
for name, stat_code, freq, item_code1, start, end in CODE_LIST:
    resp = ecos.stat_search(  # 통계 조회 API 호출
        stat_code=stat_code,  # 통계표코드
        freq=freq,  # 주기
        item_code1=item_code1,  # 통계항목코드1
        start=start,  # 검색시작일자
        end=end,  # 검색종료일자
    )
    data += resp
df_raw = pd.DataFrame(data)  # 데이터프레임 생성
df_raw["TIME"] = pd.to_datetime(df_raw["TIME"], format="%Y%m")  # 날짜 타입으로 변환
df_raw["DATA_VALUE"] = df_raw["DATA_VALUE"].astype(float)  # 부동소수점수 타입으로 변환

# 시각화 스타일 지정(맥OS 환경에서는 매개변수 font에 "Apple SD Gothic Neo"를 입력)
sns.set_theme(context="poster", style="whitegrid", font="Malgun Gothic")
sns.set_style({"grid.linestyle": ":", "grid.color": "#CCCCCC"})

fig, ax = plt.subplots(figsize=(16, 9), dpi=100)  # 이미지 크기 및 해상도 지정
sns.lineplot(data=df_raw, x="TIME", y="DATA_VALUE", hue="ITEM_NAME1")  # 선 그래프
sns.despine(top=True, right=True)  # 축 제거 여부 설정

ax.set_xlabel(None)  # 가로축 제목 제거
ax.set_ylabel("시장금리")  # 세로축 제목
ax.get_legend().set_title(None)  # 범례 제목 제거
fig.set_layout_engine("tight")  # 이미지 여백 제거
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png")  # PNG 파일로 저장
