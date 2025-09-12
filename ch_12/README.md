# Chapter 12 미쉐린 가이드 지도

## 📋 실습 개요
이번 장에서는 **웹 스크래핑과 지도 시각화**를 통해 미쉐린 가이드 맛집 정보를 인터랙티브한 지도로 표현하는 프로젝트를 진행합니다.
- **Playwright**를 활용한 네이버 지도 웹 스크래핑
- **네이버 지역 API**를 사용한 정확한 위치정보 수집
- **Folium**을 통한 인터랙티브 웹 지도 생성
- **Streamlit**으로 카테고리별 필터링 기능을 갖춘 웹 애플리케이션 구현

## ⚙️ 패키지 설치
실습을 원활하게 진행하기 위해 비주얼 스튜디오 코드 터미널에서 아래 명령어를 실행하여 필요한 파이썬 패키지들을 설치해주세요.

```shell
pip install -U playwright datakart folium pandas streamlit streamlit-folium tqdm
```

Playwright 크로미움 브라우저를 설치하세요.

```shell
playwright install
```

## 🔑 API 키 준비하기
정확한 맛집 위치정보 수집을 위해서는 **네이버 지역 API 키**가 필요합니다. 다음 단계를 따라 준비해주세요:

**네이버 개발자 센터 API 키**
1. [네이버 개발자 센터](https://developers.naver.com/apps/) 접속
2. 회원가입 후 로그인
3. '애플리케이션 등록' - '지역 서비스' API 사용 설정
4. 발급받은 Client ID와 Client Secret을 해당 실습 파일의 `NAVER_KEY`, `NAVER_SEC` 변수에 입력하세요
   - [step_2_1.py](step_2_1.py), [step_2_2.py](step_2_2.py)

## ⚠️ 중요 설정 사항 - Playwright Inspector
Playwright Inspector 사용 시 다음 설정을 확인하세요:

- **문제**: Inspector 실행 시 locator 음영처리가 안 되거나, 코드가 JavaScript로 생성되는 문제
- **해결**: Inspector 창 우측 상단의 **'Target' 메뉴**에서 Python > **'Pytest'** 또는 **'Library'** 선택

> 📋 **자세한 설정 방법은 [INSPECTOR_TARGET.md](../INSPECTOR_TARGET.md) 파일을 참고하세요!**

## 🚀 실습 단계별 가이드
*   **[step_1_1.py](step_1_1.py)**: 실습에 필요한 `input`, `output` 폴더를 생성하여 기본 작업 환경을 구성합니다.

*   **[step_1_2.py](step_1_2.py)**: `Playwright`를 실행하여 네이버 지도 웹사이트로 이동한 후, 사용자가 직접 웹페이지를 탐색할 수 있도록 `pause()`로 실행을 멈추어 수동 탐색 방법을 익힙니다.

*   **[step_1_3.py](step_1_3.py)**: 네이버 지도에서 특정 키워드(예: "미쉐린 서울")를 입력하고 검색하는 자동화 함수를 작성합니다.

*   **[step_1_4.py](step_1_4.py)**: 네이버 지도 검색 결과 페이지(iframe 내부)를 끝까지 스크롤하여, 목록에 있는 모든 장소의 이름과 카테고리를 체계적으로 추출합니다.

*   **[step_1_5.py](step_1_5.py)**: 검색 결과의 여러 페이지를 자동으로 넘겨가며, 모든 페이지에 있는 장소 이름과 카테고리를 수집하여 CSV 파일로 저장하는 종합 함수를 작성합니다.

*   **[step_2_1.py](step_2_1.py)**: `datakart`를 사용하여 네이버 지역 API에 업체명과 카테고리로 장소를 검색하고, 주소와 좌표(위도, 경도) 정보를 반환하는 함수를 작성합니다. (API 키 필요)

*   **[step_2_2_iterrows.py](step_2_2_iterrows.py)**: `pandas` DataFrame의 `iterrows()`를 사용하여 각 행의 인덱스와 데이터를 반복적으로 처리하는 방법을 학습하는 기본 예제입니다.

*   **[step_2_2.py](step_2_2.py)**: `step_1_5.py`에서 수집한 업체 목록 CSV 파일을 읽어, 각 업체별로 네이버 지역 API를 호출하여 주소와 좌표를 가져온 후, 그 결과를 새로운 CSV 파일로 저장합니다. `tqdm`으로 진행 상황을 시각적으로 표시합니다.

*   **[step_3_1_folium.py](step_3_1_folium.py)**: `folium`을 사용하여 특정 좌표에 마커가 있는 기본 지도를 생성하는 방법을 익히는 예제입니다.

*   **[step_3_1.py](step_3_1.py)**: `step_2_2.py`에서 저장한 맛집 데이터를 `folium`을 사용하여 지도에 마커로 표시합니다. 각 마커에 마우스를 올리면 업체명, 카테고리, 주소가 툴팁으로 나타나며, 최종 지도를 HTML 파일로 저장합니다.

*   **[step_3_2_cluster.py](step_3_2_cluster.py)**: `folium`의 `MarkerCluster`를 사용하여 여러 개의 마커를 하나의 클러스터에 추가하는 방법을 학습하는 기본 예제입니다.

*   **[step_3_2.py](step_3_2.py)**: `step_3_1.py`의 기능을 개선하여, `folium`의 `MarkerCluster` 플러그인을 사용해 지도의 줌 레벨에 따라 여러 마커를 자동으로 그룹화하여 보여주는 클러스터링 지도를 생성하고 HTML 파일로 저장합니다.

*   **[step_x_in.py](step_x_in.py)**: `in` 연산자와 `pandas`의 `str.contains`를 사용하여 문자열 포함 여부를 확인하고, 이를 통해 데이터를 필터링하는 방법을 학습하는 예제입니다.

*   **[step_x.py](step_x.py)**: `streamlit`을 사용하여 맛집 지도 웹 애플리케이션을 만듭니다. 사용자가 드롭다운 메뉴에서 카테고리(전체, 한식, 일식, 중식, 기타)를 선택하면, 해당 카테고리의 맛집만 필터링하여 클러스터링된 지도에 인터랙티브하게 보여줍니다.

모든 준비가 완료되었다면 미쉐린 가이드 지도 실습을 시작해보세요! 🚀