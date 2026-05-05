# ch_01 테스트 계획 (Test Plan)

`ch_01` 폴더의 `step*.py` 파일들을 테스트하기 위한 전략과 파일별 상세 계획입니다.
파일 입출력(JSON)과 그래프(Matplotlib) 생성 로직이 포함되어 있어, 부작용(Side Effects)을 통제하는 것이 핵심입니다.

## 🧪 테스트 전략 (Testing Strategy)

1. **테스트 프레임워크 및 환경**
   - 레포지토리에 설정된 `pytest` 프레임워크를 사용합니다.
   - 테스트 코드는 `tests/ch_01/test_steps.py` 파일 하나에 모아서 작성합니다.

2. **의존성 분리 및 부작용(Side Effects) 통제**
   - 실제 디렉토리를 오염시키지 않기 위해 `pytest`의 `tmp_path` 픽스처를 사용하여 임시 디렉토리를 생성합니다.
   - `monkeypatch`를 이용하여 각 모듈이 참조하는 입출력 파일 경로(예: `OUT_2_3`, `OUT_3_1` 등)를 `tmp_path` 아래의 경로로 덮어씁니다.

3. **Matplotlib(그래프) 테스트 제어**
   - `step_3_2.py`와 `step_3_3.py`는 모듈이 임포트될 때 그래프를 렌더링하고 파일을 즉시 저장하는 구조입니다.
   - 실제 이미지 렌더링을 방지하기 위해 `unittest.mock.patch`를 사용해 `matplotlib.pyplot.subplots` 및 `Figure.savefig`를 모킹(Mocking)하여 메서드 호출 여부만 검증합니다.

---

## 📝 파일별 상세 테스트 계획

### 1. `step_2_2.py` (`get_total_filesize`)
- **테스트:** `tmp_path` 픽스처를 이용해 임의의 더미 파일(크기가 지정된 텍스트 파일 등)을 여러 개 생성합니다.
- **검증:** `get_total_filesize` 함수가 해당 임시 경로를 순회하며 파일들의 크기 총합을 올바르게 계산하는지 확인합니다. 와일드카드 패턴(`*`, `**/*`)이 의도대로 동작하는지도 검증합니다.

### 2. `step_2_3.py` (`dump_dirnames`, `load_dirnames`)
- **테스트:** `OUT_2_3` 경로를 `tmp_path` 내 임시 파일로 모킹합니다. `tmp_path` 내에 여러 개의 하위 디렉토리를 생성합니다.
- **검증:** `dump_dirnames()`를 실행했을 때 디렉토리 목록이 오름차순 정렬되어 JSON 포맷으로 정확히 쓰이는지 검증합니다. 이후 `load_dirnames()`를 호출해 해당 리스트를 정상적으로 읽어오는지 확인합니다.

### 3. `step_2_4.py` (`dump_filesize_from_dirnames`, `load_filesize_per_dir`)
- **테스트:** `step_2_3`의 `load_dirnames` 함수를 모킹하여 임의의 디렉토리 목록을 반환하게 설정합니다. `OUT_2_4` 경로 역시 `tmp_path`로 덮어씁니다.
- **검증:** `dump_filesize_from_dirnames()` 실행 시 각 디렉토리별 크기(dictionary 형태)가 계산되어 JSON 파일에 제대로 저장되는지 확인하고, `load_filesize_per_dir()`를 통해 딕셔너리 구조가 복원되는지 검사합니다.

### 4. `step_3_1.py` (`dump_plot_data`, `load_plot_data`)
- **테스트:** `step_2_4`의 `load_filesize_per_dir`를 모킹하여 더미 크기 데이터 딕셔너리를 반환하게 합니다. `OUT_3_1` 경로를 덮어씁니다.
- **검증:** 반환된 데이터 중 크기가 0보다 큰 데이터만 필터링되어 `{stem: [...], size: [...]}`의 형태로 변환 및 JSON 저장되는지 검증합니다.

### 5. `step_3_2.py` & `step_3_3.py` (그래프 생성 스크립트)
- **테스트:** 해당 모듈들은 전역 레벨에서 바로 실행되므로, 스크립트 임포트 **전에** `step_3_1.load_plot_data`가 미리 정의된 더미 데이터를 반환하도록 모킹해 두어야 합니다. 또한 `matplotlib.figure.Figure.savefig`를 모킹합니다.
- **검증:** 테스트 함수 내에서 `importlib.import_module` (또는 직접 import)를 수행하여 런타임 에러 없이 실행이 종료되는지, 그리고 `savefig`가 예상되는 파일명(`step_3_2.png`, `step_3_3.png` 등)을 가지고 정상 호출되었는지 확인합니다.
