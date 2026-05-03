## ch_14_genai 테스트 안내

이 폴더의 테스트는 출판된 소스 코드를 수정하지 않고, `ch_14_genai` 안의 각 `step_*.py` 파일을 파일 단위로 점검하기 위한 스모크 테스트입니다.

핵심 테스트 파일은 [test_infra.py](test_infra.py) 입니다.

### 실행 명령

기본 실행:

```bash
uv run --group dev pytest tests/ch_14_genai/test_infra.py -q
```

실제 API 호출까지 포함한 실행:

```bash
uv run --group dev pytest tests/ch_14_genai/test_infra.py -q --run-live-api
```

### 기본 실행에서 하는 일

기본 명령은 아래 3가지를 기준으로 동작합니다.

1. `ch_14_genai` 폴더 안의 모든 `step*.py` 파일을 컴파일 검사합니다.
2. 로컬에서 바로 끝나는 일부 파일은 실제로 subprocess로 실행합니다.
3. 외부 API나 네트워크가 필요한 파일은 기본 실행에서 건너뜁니다.

### 1. 전체 컴파일 검사

`test_all_step_files_compile`는 `ch_14_genai` 안의 모든 `step*.py` 파일에 대해 `py_compile` 기반 컴파일 검사를 수행합니다.

이 단계는 다음을 확인합니다.

- 문법 오류가 없는지
- 파서 수준 오류가 없는지
- 파일이 최소한 파이썬 코드로 정상 해석되는지

이 단계는 코드를 실행하지 않고, 컴파일만 합니다.

### 2. 기본 실행에서 실제로 실행하는 파일

`test_local_step_scripts_run`는 현재 아래 파일만 실제로 실행합니다.

- `ch_14_genai/step_1_1.py`
- `ch_14_genai/step_3_1_format.py`

이 파일들은 다음 조건을 만족하므로 기본 테스트에 포함했습니다.

- API 키가 필요 없음
- 사용자 입력이 필요 없음
- 실행하면 바로 종료됨

실행 방식은 내부적으로 아래와 같습니다.

```python
subprocess.run(
    [sys.executable, str(path)],
    cwd=REPO_ROOT,
    capture_output=True,
    text=True,
    timeout=20,
)
```

즉, 개념적으로는 아래와 비슷합니다.

```bash
python ch_14_genai/step_1_1.py
python ch_14_genai/step_3_1_format.py
```

### 3. 기본 실행에서 건너뛰는 파일

`@pytest.mark.live_api`가 붙은 `test_live_api_step_scripts_run`는 기본 실행에서는 skip 됩니다.

현재 live API 대상은 아래 파일들입니다.

- `ch_14_genai/step_1_2_gemini.py`
- `ch_14_genai/step_2_1.py`
- `ch_14_genai/step_2_1_tts.py`
- `ch_14_genai/step_2_2.py`
- `ch_14_genai/step_2_3.py`
- `ch_14_genai/step_2_3_nltk.py`
- `ch_14_genai/step_3_1.py`
- `ch_14_genai/step_3_1_prompt.py`

이 파일들은 다음 이유로 기본 테스트에서 제외됩니다.

- 실제 API 키 또는 인증 파일 필요
- 네트워크 호출 발생 가능
- 실행 환경에 따라 결과가 달라질 수 있음

`tests/conftest.py`가 `--run-live-api` 옵션이 없을 때 이 테스트들을 자동으로 skip 처리합니다.

### 기본 실행에서 컴파일만 하는 파일

아래 파일들은 현재 기본 테스트에서 컴파일만 하고, 실제 실행은 하지 않습니다.

- `ch_14_genai/step_1_2.py`
- `ch_14_genai/step_1_3.py`
- `ch_14_genai/step_3_2.py`
- `ch_14_genai/step_3_3.py`
- `ch_14_genai/step_x.py`

이 파일들은 주로 Streamlit 앱이라서, 일반 `python file.py` 실행과 잘 맞지 않습니다. 앱 실행 자체가 실패라는 뜻은 아니고, 종료형 스크립트 테스트에 적합하지 않다는 의미입니다.

### 결과 해석

기본 명령:

```bash
uv run --group dev pytest tests/ch_14_genai/test_infra.py -q
```

이 실행은 보통 아래 의미를 가집니다.

- 전체 `step*.py` 컴파일 검사
- `step_1_1.py`, `step_3_1_format.py` 실제 실행
- live API 테스트는 skip

예를 들어 `17 passed, 8 skipped`라면 보통 다음 뜻입니다.

- 컴파일 검사 15개 통과
- 로컬 실행 검사 2개 통과
- live API 검사 8개 skip

### live API 실행이 실패할 때

아래 명령은 실제 API 파일도 subprocess로 실행합니다.

```bash
uv run --group dev pytest tests/ch_14_genai/test_infra.py -q --run-live-api
```

이 명령이 실패하면 보통 아래 중 하나입니다.

- Gemini API 키 문제
- Google Cloud TTS 인증 파일 문제
- 입력 파일 누락
- 네트워크 문제
- 실행 환경 차이

즉, 기본 테스트 실패와 달리, live API 실패는 코드 문법 문제가 아니라 환경 문제일 가능성도 큽니다.