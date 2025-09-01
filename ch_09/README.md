# Chapter 09 주요 경제지표 그래프

실습을 진행하기 위해 비주얼 스튜디오 코드 터미널에 아래 명령어를 입력하여 파이썬 패키지를 설치하세요.

```shell
pip install -U datakart matplotlib openpyxl pandas requests seaborn
```

## 🚀 실습 순서
*   **[step_1_1.py](step_1_1.py)**: 실습 결과물을 저장할 `output` 폴더를 생성하여 기본 작업 환경을 설정합니다.
*   **[step_1_2.py](step_1_2.py)**: `requests`를 사용하여 한국은행 경제통계시스템(ECOS)의 샘플 API를 호출하고, 그 결과를 JSON 형식으로 확인합니다.
*   **[step_2_1.py](step_2_1.py)**: `datakart` 패키지를 사용하여 ECOS API에서 특정 통계(기준금리) 데이터를 조회하고, `pandas` DataFrame으로 변환한 후 CSV 파일로 저장합니다. (API 키 필요)
*   **[step_2_2.py](step_2_2.py)**: 여러 개의 주요 경제 지표(기준금리, 국고채, 코스피 등)를 ECOS API로 한 번에 조회하여, 각각의 결과를 별도의 시트로 구성된 하나의 엑셀(.xlsx) 파일에 저장합니다.
*   **[step_3_1_datetime.py](step_3_1_datetime.py)**: `datetime` 모듈과 `pandas`의 `to_datetime` 함수를 사용하여 문자열을 날짜/시간 객체로 변환하고, 형식을 지정하는 방법을 보여주는 기본 예제입니다.
*   **[step_3_1.py](step_3_1.py)**: `step_2_2.py`에서 저장한 엑셀 파일 중 '코스피지수' 시트를 읽어, `seaborn`과 `matplotlib`을 사용하여 시계열 선 그래프를 그리고 이미지 파일(.png)로 저장합니다.
*   **[step_3_2_subplots.py](step_3_2_subplots.py)**: `matplotlib`의 `subplots` 기능을 사용하여 하나의 이미지 안에 바, 산점도, 선 그래프 등 여러 종류의 그래프를 함께 그리는 방법을 보여주는 기본 예제입니다.
*   **[step_3_2.py](step_3_2.py)**: 엑셀 파일에 저장된 4개의 경제 지표(국고채, 회사채, 코스피, 원달러환율)를 각각 읽어, `matplotlib`의 `subplots`를 이용해 2x2 격자로 배열된 여러 개의 미니 선 그래프를 하나의 이미지로 생성하고 저장합니다.
*   **[step_x.py](step_x.py)**: ECOS API에서 국고채와 회사채 금리 데이터를 조회하여 하나의 DataFrame으로 합친 후, `seaborn`의 `hue` 옵션을 사용하여 두 데이터를 구별되는 색상으로 표현한 선 그래프를 그리고 이미지 파일로 저장하는 종합 실습입니다.