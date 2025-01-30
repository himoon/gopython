from pathlib import Path

import pandas as pd
from folium import Icon, Map, Marker

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import OUT_2_2


def load_data() -> pd.DataFrame:
    df_raw = pd.read_csv(OUT_2_2, encoding="utf-8")  # CSV 파일 불러오기
    return df_raw.dropna()  # 좌표가 없는 데이터를 제외한 데이터프레임 반환


def get_map() -> Map:
    return Map(tiles="CartoDB Voyager", font_size="2rem")  # Map 객체 생성


def get_all_coords(df_raw: pd.DataFrame) -> list[tuple[float, float]]:
    # [(위도1, 경도1), (위도2, 경도2), ...] 형식으로 모든 좌표를 반환
    return [(sr["laty"], sr["lonx"]) for _, sr in df_raw.iterrows()]


def add_marker(df_raw: pd.DataFrame) -> Map:
    map = get_map()  # 지도 생성
    map.fit_bounds(get_all_coords(df_raw))  # 한눈에 모든 마커가 보이도록 설정
    for _, sr in df_raw.iterrows():  # 행별로 반복 처리
        name, category, addr = sr["name"], sr["category"], sr["addr"]
        marker = Marker(  # 마커 생성
            location=[sr["laty"], sr["lonx"]],  # [위도, 경도] 좌표 설정
            tooltip=f"<b>{name}</b><br>{category}<br>{addr}",  # 툴팁 텍스트 설정
            icon=Icon(icon="cutlery", prefix="fa", color="red"),  # 아이콘 설정
        )
        marker.add_to(map)  # 마커를 지도에 추가
    return map


if __name__ == "__main__":
    df_raw = load_data()  # 데이터 로딩 및 데이터프레임 생성
    map = add_marker(df_raw)  # 지도 생성 및 마커 추가
    map.save(OUT_DIR / f"{Path(__file__).stem}.html")  # HTML 파일로 저장
