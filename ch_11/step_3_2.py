from pathlib import Path

from datakart import Sgis

from step_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

OUT_3_2 = OUT_DIR / f"{Path(__file__).stem}.geojson"


def adm_cd_to_geojson(adm_cd: str = None, low_search: str = "1") -> None:
    SGIS_KEY, SGIS_SECRET = "서비스 ID", "보안 Key"  # 통계지리정보서비스 API 서비스 ID, 보안 Key 입력
    sgis = Sgis(SGIS_KEY, SGIS_SECRET)  # Sgis 객체 생성
    resp: str = sgis.hadm_area(adm_cd=adm_cd, low_search=low_search)  # GeoJSON 형식의 문자열 반환
    OUT_3_2.write_text(resp, encoding="utf-8")  # GeoJSON 형식의 텍스트 파일로 저장


if __name__ == "__main__":
    adm_cd, low_search = "11", "1"  # 서울특별시, 시군구 단위
    adm_cd_to_geojson(adm_cd, low_search)  # 행정구역 경계 데이터를 저장
