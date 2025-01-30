from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_3 import OUT_3_3

OUT_3_4 = OUT_DIR / f"{Path(__file__).stem}.png"


def geojson_to_img():
    # 시각화 스타일 지정(맥OS 환경에서는 매개변수 font에 "Apple SD Gothic Neo"를 입력)
    sns.set_theme(context="poster", font="Malgun Gothic")
    fig, ax = plt.subplots(figsize=(16, 9), dpi=100)  # 이미지 크기 및 해상도 지정

    gdf_raw: gpd.GeoDataFrame = gpd.read_file(OUT_3_3, encoding="utf-8")
    gdf_raw.plot(  # 행정구역 경계 데이터 시각화
        column="avg_price",  # 단계구분도 기준 열 설정
        cmap="OrRd",  # 단계구분도 색상 설정
        edgecolor="k",  # 경계선 색상 설정
        legend=True,  # 범례 표시 여부
        legend_kwds={"label": "(단위: 만원)", "orientation": "vertical"},  # 범례 설정
        ax=ax,  # 12행에서 생성한 Axes 객체에 시각화 결과물 저장
    )
    ax.set_axis_off()  # 축 제거
    ax.set_title("단위 면적당 평균 아파트 매매 실거래가")  # 제목 설정
    fig.set_layout_engine("tight")  # 여백 제거
    fig.savefig(OUT_3_4)  # PNG 파일로 저장


if __name__ == "__main__":
    geojson_to_img()  # GeoJSON 데이터를 이미지 파일로 시각화
