from pathlib import Path

import pandas as pd
from folium import Icon, Map, Marker
from folium.plugins import MarkerCluster

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_1 import get_all_coords, get_map, load_data


def add_marker_cluster(df_raw: pd.DataFrame) -> Map:
    map = get_map()  # 지도 생성
    map.fit_bounds(get_all_coords(df_raw))  # 한눈에 모든 마커가 보이도록 설정
    cluster = MarkerCluster().add_to(map)  # 마커 클러스터 생성 및 지도에 추가
    for idx, sr in df_raw.iterrows():  # 행별로 반복 처리
        name, category, addr = sr["name"], sr["category"], sr["addr"]
        marker = Marker(  # 마커 생성
            location=[sr["laty"], sr["lonx"]],  # 위도 및 경도 좌표 설정
            tooltip=f"<b>{name}</b><br>{category}<br>{addr}",  # 툴팁 설정
            icon=Icon(icon="cutlery", prefix="fa", color="red"),  # 아이콘 설정
        )
        marker.add_to(cluster)  # 마커를 마커 클러스터에 추가
    return map


if __name__ == "__main__":
    df_raw = load_data()  # 데이터 로딩 및 데이터프레임 생성
    map = add_marker_cluster(df_raw)  # 지도 생성 및 마커 클러스터 추가
    map.save(OUT_DIR / f"{Path(__file__).stem}.html")  # HTML 파일로 저장
