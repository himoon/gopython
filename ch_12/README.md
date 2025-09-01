# Chapter 12 미쉐린 가이드 지도

실습을 진행하기 위해 비주얼 스튜디오 코드 터미널에 아래 명령어를 입력하여 파이썬 패키지를 설치하세요.

```shell
pip install -U playwright datakart folium pandas streamlit streamlit-folium tqdm
```

또한 아래 명령어를 입력하여 최신 크로미움 브라우저를 설치하세요.

```shell
playwright install
```

## ⚠️ 중요 변화 사항 - Playwright Inspector Target 설정

Playwright Inspector를 사용할 때 **중요한 설정 변경이 필요**합니다:

- **문제**: Inspector 실행 시 locator 음영처리가 안 되거나, 녹화된 코드가 JavaScript로 생성되는 문제
- **원인**: 현재 버전에서는 Python 환경임에도 Node.js가 기본값으로 설정되는 버그
- **해결법**: Inspector 창 우측 상단의 **'Target' 메뉴**를 클릭하여 Python > **'Pytest'** 또는 **'Library'** 선택

> 📋 **자세한 설정 방법은 [INSPECTOR_TARGET.md](../INSPECTOR_TARGET.md) 파일을 참고하세요!**

## 🚀 실습 순서
*   **[step_1_1.py](step_1_1.py)**: 실습에 필요한 `input`, `output` 폴더를 생성하여 기본 작업 환경을 설정합니다.
*   **[step_1_2.py](step_1_2.py)**: `Playwright`를 실행하여 네이버 지도 웹사이트로 이동한 후, 사용자가 직접 웹페이지를 탐색할 수 있도록 `pause()`로 실행을 멈춥니다.
*   **[step_1_3.py](step_1_3.py)**: 네이버 지도에서 특정 키워드(예: "미쉐린 서울")를 입력하고 검색하는 자동화 함수를 작성합니다.
*   **[step_1_4.py](step_1_4.py)**: 네이버 지도 검색 결과 페이지(iframe 내부)를 끝까지 스크롤하여, 목록에 있는 모든 장소의 이름과 카테고리를 추출합니다.
*   **[step_1_5.py](step_1_5.py)**: 검색 결과의 여러 페이지를 자동으로 넘겨가며, 모든 페이지에 있는 장소 이름과 카테고리를 수집하여 CSV 파일로 저장하는 종합 함수를 작성합니다.
*   **[step_2_1.py](step_2_1.py)**: `datakart`를 사용하여 네이버 지역 API에 업체명과 카테고리로 장소를 검색하고, 주소와 좌표(위도, 경도) 정보를 반환하는 함수를 작성합니다. (API 키 필요)
*   **[step_2_2_iterrows.py](step_2_2_iterrows.py)**: `pandas` DataFrame의 `iterrows()`를 사용하여 각 행의 인덱스와 데이터를 반복적으로 처리하는 방법을 보여주는 기본 예제입니다.
*   **[step_2_2.py](step_2_2.py)**: `step_1_5.py`에서 수집한 업체 목록 CSV 파일을 읽어, 각 업체별로 네이버 지역 API를 호출하여 주소와 좌표를 가져온 후, 그 결과를 새로운 CSV 파일로 저장합니다. `tqdm`으로 진행 상황을 표시합니다.
*   **[step_3_1_folium.py](step_3_1_folium.py)**: `folium`을 사용하여 특정 좌표에 마커가 있는 기본 지도를 생성하는 방법을 보여주는 예제입니다.
*   **[step_3_1.py](step_3_1.py)**: `step_2_2.py`에서 저장한 맛집 데이터를 `folium`을 사용하여 지도에 마커로 표시합니다. 각 마커에 마우스를 올리면 업체명, 카테고리, 주소가 툴팁으로 나타나며, 최종 지도를 HTML 파일로 저장합니다.
*   **[step_3_2_cluster.py](step_3_2_cluster.py)**: `folium`의 `MarkerCluster`를 사용하여 여러 개의 마커를 하나의 클러스터에 추가하는 방법을 보여주는 기본 예제입니다.
*   **[step_3_2.py](step_3_2.py)**: `step_3_1.py`의 기능을 개선하여, `folium`의 `MarkerCluster` 플러그인을 사용해 지도의 줌 레벨에 따라 여러 마커를 자동으로 그룹화하여 보여주는 클러스터링 지도를 생성하고 HTML 파일로 저장합니다.
*   **[step_x_in.py](step_x_in.py)**: `in` 연산자와 `pandas`의 `str.contains`를 사용하여 문자열 포함 여부를 확인하고, 이를 통해 데이터를 필터링하는 방법을 보여주는 예제입니다.
*   **[step_x.py](step_x.py)**: `streamlit`을 사용하여 맛집 지도 웹 앱을 만듭니다. 사용자가 드롭다운 메뉴에서 카테고리(전체, 한식, 일식, 중식, 기타)를 선택하면, 해당 카테고리의 맛집만 필터링하여 클러스터링된 지도에 보여줍니다.