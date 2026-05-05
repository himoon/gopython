# ch_02 테스트 계획 (Test Plan)

`ch_02` 폴더의 `step*.py` 파일들을 테스트하기 위한 전략과 파일별 상세 계획입니다.
이 챕터는 `pandas`를 이용한 엑셀 파일 입출력 및 데이터 가공(Pivot 등)과 `matplotlib`, `seaborn`을 이용한 시각화 로직을 포함합니다. 파일 입출력 속도 저하와 실제 파일 생성을 막기 위해 **Mocking**을 적극 활용합니다.

## 🧪 테스트 전략 (Testing Strategy)

1. **의존성 분리 및 부작용(Side Effects) 통제**
   - 엑셀 파일 입출력(`pd.read_excel`, `pd.DataFrame.to_excel`)을 `unittest.mock.patch`를 이용해 모킹합니다. 실제 디스크에 엑셀 파일을 쓰고 읽지 않도록 하여 테스트를 빠르고 격리된 상태로 유지합니다.
   - 모킹된 `read_excel`이 테스트용 더미 DataFrame을 반환하도록 설정하여, 이후의 데이터 병합(`concat`) 및 집계(`pivot_table`) 로직이 정상 동작하는지 검증합니다.

2. **Matplotlib & Seaborn 제어**
   - `ch_01`과 마찬가지로 `pyplot.subplots`, `Figure.savefig`를 모킹하여 이미지 렌더링 및 저장을 방지합니다.

3. **모듈 레벨 스크립트 실행 제어**
   - `ch_02`의 많은 스크립트가 임포트 시점에 전역에서 코드를 실행합니다. `importlib.reload`를 사용하여 격리된 상태에서 모듈을 재실행하며 테스트합니다.

---

## 📝 파일별 상세 테스트 계획

### 1. `step_1.py` (디렉토리 생성)
- **테스트:** `WORK_DIR`을 `tmp_path`로 모킹한 후 모듈을 임포트/리로드합니다.
- **검증:** `input`, `output` 폴더가 정상적으로 생성되었는지 확인합니다.

### 2. `step_2_1.py`, `step_2_2.py` (데이터 로드 및 병합)
- **테스트:** 
  - `pd.read_excel`을 모킹하여 더미 데이터를 반환하도록 합니다.
  - `step_2_2.py`에서는 `Path.glob`을 모킹하여 여러 개의 가짜 엑셀 파일 경로를 반환하도록 합니다.
  - `pd.DataFrame.to_excel`을 모킹합니다.
- **검증:** 
  - `read_excel`이 올바른 인자(`usecols`, `skiprows`)로 호출되었는지 검증합니다.
  - `to_excel`이 병합된 DataFrame과 함께 호출되었는지 검증합니다.

### 3. `step_3_1.py`, `step_3_2.py` (데이터 집계 - Pivot)
- **테스트:** `pd.read_excel`이 병합된 형태의 더미 데이터를 반환하도록 모킹하고, `to_excel`을 모킹합니다.
- **검증:** 피벗 테이블과 누적 금액이 계산되어 `to_excel`에 전달되는 데이터(DataFrame) 구조를 검사합니다.

### 4. `step_4_1.py`, `step_4_2.py`, `step_4_3.py`, `step_x.py` (시각화)
- **테스트:** 
  - `pd.read_excel` (또는 `load_data` 함수 내부 동작)이 집계된 더미 데이터를 반환하도록 모킹합니다.
  - `matplotlib.pyplot.subplots`와 `Figure.savefig`를 모킹합니다.
- **검증:** 
  - 코드 실행 중 에러가 발생하지 않는지, 그리고 `savefig`가 올바른 파일 경로로 호출되는지 검증합니다.
