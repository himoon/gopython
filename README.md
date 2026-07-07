# <혼자 만들면서 공부하는 파이썬> 책의 깃허브 자료실

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/cover_1st.png" width="150" alt="혼자 만들면서 공부하는 파이썬 표지">

## 📢 공지사항

- [**유튜브 채널 - 동영상 강의를 통해 더 깊이 있는 학습을 해보세요!**](https://www.youtube.com/@moon-hyunil)

## 🚀 판매처

- [yes24](https://www.yes24.com/Product/Goods/142258696)
- [교보문고](https://product.kyobobook.co.kr/detail/S000215710144)
- [알라딘](http://aladin.kr/p/lzsPq)
- [한빛미디어](https://www.hanbit.co.kr/store/books/look.php?p_code=B5580711889)

## 🚨 실습 중 자주 발생하는 문제 해결 안내

### 갑자기 안 보이던 오류/경고가 쏟아지는 경우
- **문제**: 예제 코드는 정상 실행되는데도 편집기에서 빨간 밑줄이나 경고 메시지가 표시되는 문제
- **원인**: 파이썬 관련 확장 프로그램의 Type Checking Mode가 `basic` 또는 `strict`로 설정되어 코드 타입을 더 엄격하게 점검함
- **해결법**: VS Code 설정에서 `Python › Analysis: Type Checking Mode`를 `off`로 변경
- **📋 자세한 설정 방법**: [docs/type-checking-mode.md](docs/type-checking-mode.md) 파일 참고

### VS Code 파이썬 가상환경 재설정 안내
- **문제**: 가상환경 생성 실패, 패키지 설치 오류, 인터프리터 인식 불가, `(.venv)` 표시 누락 등의 문제
- **원인**: 기존 가상환경 꼬임, 터미널 프로필 설정 문제, 캐시 반영 지연 등으로 VS Code가 가상환경을 정상 인식하지 못함
- **해결법**: 실행 중인 터미널을 종료한 뒤 `Python: 환경 만들기`로 `.venv`를 다시 생성하고, VS Code를 새로고침하거나 다시 실행
- **📋 자세한 재설정 방법**: [docs/venv-setup.md](docs/venv-setup.md) 파일 참고

### VS Code 대화형 창 커널 연결 문제 안내
- **문제**: 대화형 창에서 `.venv` 커널이 표시되어도 Python 커널에 연결되지 않는 문제
- **원인**: 관리자 권한으로 설치된 Python이 시스템 디렉토리에 있어, 일반 권한으로 실행되는 VS Code가 해당 경로에 정상 접근하지 못함
- **해결법**: 기존 Python을 삭제한 뒤 일반 사용자 계정용으로 다시 설치하고, VS Code 재실행 후 가상환경을 다시 설정
- **📋 자세한 해결 방법**: [docs/python-install.md](docs/python-install.md) 파일 참고

### 최신 pandas, streamlit 등 패키지 설치 오류 안내
- **문제**: pandas, streamlit 등 최신 패키지 설치 중 빌드 오류가 발생하는 문제
- **원인**: 윈도우 환경에서 일부 패키지 설치 시 Microsoft C++ 빌드 도구가 필요하거나, Python 버전 호환성 문제로 설치가 실패할 수 있음
- **해결법**: 먼저 `pip`, `setuptools`, `wheel`을 업데이트하고, 필요 시 Microsoft C++ 빌드 도구를 설치하거나 PyPI에서 미리 빌드된 `.whl` 파일을 사용
- **📋 자세한 해결 방법**: [docs/ms-build-tools.md](docs/ms-build-tools.md) 파일 참고

## ⚠️ 중요한 코드 업데이트 안내

일부 챕터의 코드가 외부 환경 변화로 인해 업데이트되었습니다. 원활한 실습을 위해 반드시 확인해 주세요!

### Playwright Inspector Target 설정 (Chapter 6, 7, 12)
- **문제**: Inspector 실행 시 locator 음영처리가 안 되거나, 녹화된 코드가 JavaScript로 생성되는 문제
- **원인**: 현재 버전에서는 Python 환경임에도 Node.js가 기본값으로 설정되는 버그
- **해결법**: Inspector 창 우측 상단의 **'Target' 메뉴** 클릭 → Python > **'Pytest'** 또는 **'Library'** 선택
- **📋 자세한 설정 방법**: [docs/inspector-target.md](docs/inspector-target.md) 파일 참고

### Chapter 1: 폴더 크기 측정 프로그램
- **성능 최적화 필수**: [step_2_3.py](ch_01/step_2_3.py) 실행 시 홈 디렉토리의 모든 폴더를 추출하므로 사전 작업이 필요합니다
- **권장 실습 순서**: 
  1. [step_2_3.py](ch_01/step_2_3.py) 실행 → `step_2_3.json` 파일 생성
  2. JSON 파일을 열어 불필요한 폴더 목록 삭제 (⭐ 필수)
  3. [step_2_4.py](ch_01/step_2_4.py) 실행하여 폴더 크기 측정
- **⚠️ 반드시 삭제해야 할 폴더**: OneDrive, Google Drive, iCloud Drive 등 클라우드 폴더
  > 클라우드 폴더는 수천 개의 하위 폴더를 포함하여 실습 시간이 매우 길어집니다

### Chapter 4: QR 코드로 연락처 공유
- **패키지 업데이트**: qrcode 패키지 최신 버전에서 에러 발생
- **에러 내용**: `ValueError: Error correction level must be ERROR_CORRECT_H if an embedded image is provided`
- **해결책**: 
  - **책 내용 그대로**: `pip install "pillow==10.4.0" "qrcode==7.4.2" vobject` (버전 고정)
  - **최신 버전 사용**: [step_3_1_new.py](ch_04/step_3_1_new.py) 파일 참고 또는 [유튜브 강의](https://www.youtube.com/watch?v=IpgPhZh4kXE&list=PLID7cC3lN2TF4D1uUL3gYoK6VE7WlorbQ&index=31&t=376s) 참고

### Chapter 5: 이미지 속 텍스트 번역하기
- **환경 문제**: EasyOCR 패키지가 일부 CPU에서 오류 없이 종료되는 현상 발생
- **해결책**: PaddleOCR을 사용한 대체 코드 제공 ([ch_05_paddleocr](ch_05_paddleocr/) 폴더)
- **패키지 설치**: `pip install -U paddlepaddle paddleocr pillow deepl streamlit ipywidgets setuptools`
- **주요 변경사항**:
  - EasyOCR → PaddleOCR로 변경
  - 임시 파일 확장자 `.tmp` → `.tmp.png`로 변경

### Chapter 6: 쇼핑 트렌드 분석
네이버 웹사이트 UI가 여러 차례 변경되어, 아래 순서대로 코드가 업데이트되었습니다.

- **① 네이버플러스 스토어 직접 접근 오류** (2025.08.18)
  - **문제**: 네이버플러스 스토어 사이트에 직접 접근하면 오류가 발생함
  - **해결책**: 네이버 메인 페이지를 경유하여 스토어 사이트에 접근하도록 변경
  - **⚠️ 변경된 파일**: [step_1_2.py](ch_06/step_1_2.py)
- **② 스토어 이동 버튼 이름 변경** (2026.07.07)
  - **문제**: 네이버 메인 페이지에서 스토어로 이동하는 버튼 이름이 `스토어` → `쇼핑`으로 변경됨
  - **해결책**: `get_by_role("link", name="쇼핑", exact=True)`로 '쇼핑' 버튼을 클릭하도록 변경
  - **⚠️ 변경된 파일**: [step_1_2.py](ch_06/step_1_2.py)
- **③ 베스트 상품 버튼 변경** (2026.07.07)
  - **문제**: '베스트' 관련 버튼이 여러 개 추가되어, 기존 `name="베스트 NONE"` 방식으로는 원하는 메뉴를 특정하지 못함
  - **해결책**: `exact=True`를 사용해 이름이 정확히 `베스트`인 링크만 선택하도록 변경
  - **⚠️ 변경된 파일**: [step_1_3.py](ch_06/step_1_3.py)

### Chapter 7: 시가총액 분석
- **패키지 버전 관리**: 원활한 실습을 위해 특정 버전 사용 필수
- **Plotly 버전**: 5.24.1 버전 권장 (`"plotly<6"` 설치)
- **Kaleido 버전**: 0.2.1 버전 권장 (`"kaleido<1"` 설치)
- **설치 명령어**: `pip install -U playwright "kaleido<1" nbformat pandas "plotly<6" tqdm`

### Chapter 8: 연관 키워드 경쟁 강도 분석
- **Streamlit 업데이트**: 숫자 천 단위 구분 기호 표시 방식 변경
- **해결책**: 데이터프레임 표시 시 명시적으로 포맷 지정 필요
- **주요 변경사항**:
  - **`step_3_1.py`**: `st.dataframe()` → `st.dataframe(df.style.format())`로 변경
  - **`step_3_2.py`**: `column_config` 매개변수의 `format` 옵션에 `"localized"` 추가

### Chapter 12: 미쉐린 가이드 지도
- **네이버 지도 UI 변경**: 웹사이트 UI 업데이트로 인한 요소 선택자(locator) 변경
- **수정된 파일**: [ch_12/step_1_3.py](ch_12/step_1_3.py)
- **주요 변경사항**:
  - `slow_mo=1000` → `slow_mo=2000`: 브라우저 동작 속도 조절로 안정성 향상
  - 검색창 클릭: `get_by_label()` → `get_by_role("button", name="검색")`
  - 키워드 입력: `get_by_label()` → `get_by_role("combobox", name="장소, 버스, 지하철, 주소 검색")`

### Chapter 13: 생성형 AI 기사 번역 앱
- **모델 업데이트**: Gemma3 최신 버전 출시 (기존 Gemma2에서 업그레이드)
- **권장 사용법**: 
  - **최신 권장**: `ollama run gemma3:4b` (빠른 속도, 적은 메모리)
  - **고성능 옵션**: `ollama run gemma3:12b` (높은 품질, 더 많은 메모리)
- **코드 수정**: `'gemma2:9b'` → `'gemma3:4b'` 또는 `'gemma3:12b'`로 변경

### Chapter 14: 영어 받아쓰기 앱
- **API 변경**: Google에서 Gemini API 패키지명 변경
- **최신 버전**: [ch_14_genai](ch_14_genai/) 폴더 사용 권장
- **패키지 설치**: `pip install -U google-cloud-texttospeech google-genai ipywidgets nltk streamlit`
- **⚠️ 주요 변경사항**:
  - 패키지명: `google-generativeai` → `google-genai`
  - API 사용법 전면 변경 (자세한 내용은 [ch_14_genai/README.md](ch_14_genai/README.md) 참고)
  - 시스템 프롬프트 일부 변경 (각 문장별 개행문자 추가) (자세한 내용은 [ch_14_genai/README.md](ch_14_genai/README.md) 참고)

## 💡 실습 가이드

### 🔧 개발 환경 설정
1. **Python 버전 권장사항**:
   - **기본**: Python 3.12.x 또는 3.13.x 버전
   - **Chapter 5 (EasyOCR)**: Python 3.12.x 필수
   - **Chapter 5 (PaddleOCR)**: Python 3.12.x 또는 3.13.x 모두 지원
   - **Python 3.12.x 설치 방법**: [ch_05/README.md](ch_05/README.md) 파일의 "🔽 파이썬 3.12.x 설치 가이드" 섹션 참고
2. **패키지 설치**: 각 챕터의 `README.md` 파일에서 설치 명령어 확인
3. **업데이트된 코드**: 변경사항이 있는 챕터는 새로운 폴더의 코드 사용 필수

### 📂 폴더 구조 가이드

| 챕터 | 원본 폴더 | 업데이트 폴더 | 권장 사용 |
|------|-----------|---------------|-----------|
| **Chapter 5** | [ch_05](ch_05/) (EasyOCR) | [ch_05_paddleocr](ch_05_paddleocr/) (PaddleOCR) | 상황에 따라 선택 |
| **Chapter 14** | [ch_14](ch_14/) (구버전) | [ch_14_genai](ch_14_genai/) (최신버전) | [ch_14_genai](ch_14_genai/) ⭐ |

> ⭐ 표시된 옵션을 우선적으로 사용하시기 바랍니다.

## 😊 추가 도움이 필요하다면

기타 문의 사항이 있으실 경우 저자의 오픈 채팅에 문의해 주세요~!

- https://open.kakao.com/o/g5rNEh7d

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/open_chat.jpg" width="150" alt="혼자 만들면서 공부하는 파이썬 오픈 채팅">
