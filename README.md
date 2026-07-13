# <혼자 만들면서 공부하는 파이썬> 책의 깃허브 자료실

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/cover_1st.png" width="150" alt="혼자 만들면서 공부하는 파이썬 표지">

## 📑 목차

- [공지사항](#-공지사항)
- [판매처](#-판매처)
- [실습 중 자주 발생하는 문제 해결 안내](#-실습-중-자주-발생하는-문제-해결-안내)
- [중요한 코드 업데이트 안내](#-중요한-코드-업데이트-안내)
  - [Playwright Inspector Target 설정 (Chapter 6, 7, 12)](#playwright-inspector-target-설정-chapter-6-7-12)
  - [Chapter 1: 폴더 크기 측정 프로그램](#chapter-1-폴더-크기-측정-프로그램)
  - [Chapter 4: QR 코드로 연락처 공유](#chapter-4-qr-코드로-연락처-공유)
  - [Chapter 5: 이미지 속 텍스트 번역하기](#chapter-5-이미지-속-텍스트-번역하기)
  - [Chapter 6: 쇼핑 트렌드 분석](#chapter-6-쇼핑-트렌드-분석)
  - [Chapter 7: 시가총액 분석](#chapter-7-시가총액-분석)
  - [Chapter 8: 연관 키워드 경쟁 강도 분석](#chapter-8-연관-키워드-경쟁-강도-분석)
  - [Chapter 12: 미쉐린 가이드 지도](#chapter-12-미쉐린-가이드-지도)
  - [Chapter 13: 생성형 AI 기사 번역 앱](#chapter-13-생성형-ai-기사-번역-앱)
  - [Chapter 14: 영어 받아쓰기 앱](#chapter-14-영어-받아쓰기-앱)
- [실습 가이드](#-실습-가이드)
- [추가 도움이 필요하다면](#-추가-도움이-필요하다면)

## 📢 공지사항

- [**유튜브 채널 - 동영상 강의를 통해 더 깊이 있는 학습을 해보세요!**](https://www.youtube.com/@moon-hyunil)

## 🚀 판매처

- [yes24](https://www.yes24.com/Product/Goods/142258696)
- [교보문고](https://product.kyobobook.co.kr/detail/S000215710144)
- [알라딘](http://aladin.kr/p/lzsPq)
- [한빛미디어](https://www.hanbit.co.kr/store/books/look.php?p_code=B5580711889)

## 🚨 실습 중 자주 발생하는 문제 해결 안내

### VS Code 파이썬 가상환경 설정
- **증상**: 가상환경 생성 실패, 패키지 설치 오류, 인터프리터 인식 불가, `(.venv)` 표시 누락 등
- **해결**: 실행 중인 터미널을 종료한 뒤 `Python: 환경 만들기`로 `.venv`를 다시 생성하고, VS Code를 새로고침하거나 다시 실행
- **참고 문서**: [docs/venv-setup.md](docs/venv-setup.md)

### VS Code 터미널로 파이썬 패키지 설치하기
- **증상**: 챕터 실습에 필요한 pandas, streamlit 등 외부 패키지를 설치하는 방법을 모르거나, 실행 시 `ModuleNotFoundError`가 발생함
- **해결**: 가상환경을 먼저 설정한 뒤, VS Code 터미널에서 `pip install 패키지명` 명령으로 설치
- **참고 문서**: [docs/pip_install.md](docs/pip_install.md)

### VS Code 대화형 창(Interactive Window) 설정 안내
- **증상**: `Shift + Enter`로 코드를 실행해도 대화형 창이 열리지 않거나, 파일마다 창이 따로 생성되지 않음
- **해결**: VS Code 설정에서 `Execute Selection`을 켜고, `Creation Mode`를 `perFile`로 변경
- **참고 문서**: [docs/jupyter_shortcut.md](docs/jupyter_shortcut.md)

### VS Code 화면에 갑자기 오류/경고가 쏟아지는 경우
- **증상**: 예제 코드는 정상 실행되는데도 편집기에서 빨간 밑줄이나 경고 메시지가 표시됨
- **해결**: VS Code 설정에서 `Python › Analysis: Type Checking Mode`를 `off`로 변경
- **참고 문서**: [docs/type-checking-mode.md](docs/type-checking-mode.md)

### VS Code 업데이트에 따른 대화형 창 커널 연결 문제 해결
- **증상**: 대화형 창에서 `.venv` 커널이 표시되어도 Python 커널에 연결되지 않음
- **해결**: 기존 Python을 삭제한 뒤 일반 사용자 계정용으로 다시 설치하고, VS Code 재실행 후 가상환경을 다시 설정
- **참고 문서**: [docs/python-install.md](docs/python-install.md)

### 파이썬 새 버전 출시 직후 패키지 설치 오류 해결 (윈도우 환경)
- **증상**: pandas, streamlit 등 최신 패키지 설치 중 빌드 오류가 발생
- **해결**: 먼저 `pip`, `setuptools`, `wheel`을 업데이트하고, 필요 시 Microsoft C++ 빌드 도구를 설치하거나 PyPI에서 미리 빌드된 `.whl` 파일을 사용
- **참고 문서**: [docs/ms-build-tools.md](docs/ms-build-tools.md)

## ⚠️ 중요한 코드 업데이트 안내

일부 챕터의 코드가 외부 환경 변화로 인해 업데이트되었습니다. 원활한 실습을 위해 반드시 확인해 주세요!

### Playwright Inspector Target 설정 (Chapter 6, 7, 12)
- **증상**: Inspector 실행 시 locator 음영처리가 안 되거나, 녹화된 코드가 JavaScript로 생성됨
- **원인**: 현재 버전에서는 Python 환경임에도 Node.js가 기본값으로 설정되는 버그
- **해결**: Inspector 창 우측 상단의 **'Target' 메뉴** 클릭 → Python > **'Pytest'** 또는 **'Library'** 선택
- **참고 문서**: [docs/inspector-target.md](docs/inspector-target.md)

### Chapter 1: 폴더 크기 측정 프로그램
- **증상**: [step_2_3.py](ch_01/step_2_3.py) 실행 시 홈 디렉토리의 모든 폴더를 추출하므로 실습 시간이 매우 길어짐
- **해결**: 아래 순서로 실습 (사전 작업 필수)
  1. [step_2_3.py](ch_01/step_2_3.py) 실행 → `step_2_3.json` 파일 생성
  2. JSON 파일을 열어 불필요한 폴더 목록 삭제 (⭐ **필수**)
  3. [step_2_4.py](ch_01/step_2_4.py) 실행하여 폴더 크기 측정
- **⚠️ 삭제 필수 폴더**: OneDrive, Google Drive, iCloud Drive 등 클라우드 폴더
  > 클라우드 폴더는 수천 개의 하위 폴더를 포함하여 실습 시간이 매우 길어집니다

### Chapter 4: QR 코드로 연락처 공유
- **증상**: qrcode 패키지 최신 버전에서 에러 발생 — `ValueError: Error correction level must be ERROR_CORRECT_H if an embedded image is provided`
- **해결**:
  - **책 내용 그대로**: `pip install "pillow==10.4.0" "qrcode==7.4.2" vobject` (버전 고정)
  - **최신 버전 사용**: [step_3_1_new.py](ch_04/step_3_1_new.py) 파일 참고 또는 [유튜브 강의](https://www.youtube.com/watch?v=IpgPhZh4kXE&list=PLID7cC3lN2TF4D1uUL3gYoK6VE7WlorbQ&index=31&t=376s) 참고

### Chapter 5: 이미지 속 텍스트 번역하기
- **증상**: EasyOCR 패키지가 일부 CPU에서 오류 없이 종료되는 현상 발생
- **해결**: PaddleOCR을 사용한 대체 코드 제공 ([ch_05_paddleocr](ch_05_paddleocr/) 폴더)
- **설치**: `pip install -U paddlepaddle paddleocr pillow deepl streamlit ipywidgets setuptools`
- **변경 내용**:
  - EasyOCR → PaddleOCR로 변경
  - 임시 파일 확장자 `.tmp` → `.tmp.png`로 변경

### Chapter 6: 쇼핑 트렌드 분석
네이버 웹사이트 UI가 여러 차례 변경되어, 아래 순서대로 코드가 업데이트되었습니다.

- **① 네이버플러스 스토어 직접 접근 오류** (2025.08.18)
  - **증상**: 네이버플러스 스토어 사이트에 직접 접근하면 오류가 발생
  - **해결**: 네이버 메인 페이지를 경유하여 스토어 사이트에 접근하도록 변경
  - **변경 파일**: [step_1_2.py](ch_06/step_1_2.py)
- **② 스토어 이동 버튼 이름 변경** (2026.07.07)
  - **증상**: 네이버 메인 페이지에서 스토어로 이동하는 버튼 이름이 `스토어` → `쇼핑`으로 변경됨
  - **해결**: `get_by_role("link", name="쇼핑", exact=True)`로 '쇼핑' 버튼을 클릭하도록 변경
  - **변경 파일**: [step_1_2.py](ch_06/step_1_2.py)
- **③ 베스트 상품 버튼 변경** (2026.07.07)
  - **증상**: '베스트' 관련 버튼이 여러 개 추가되어, 기존 `name="베스트 NONE"` 방식으로는 원하는 메뉴를 특정하지 못함
  - **해결**: `exact=True`를 사용해 이름이 정확히 `베스트`인 링크만 선택하도록 변경
  - **변경 파일**: [step_1_3.py](ch_06/step_1_3.py)

### Chapter 7: 시가총액 분석
- **원인**: Plotly, Kaleido 최신 버전에서 호환성 문제가 발생할 수 있음
- **해결**: 권장 버전으로 고정 설치
  - **Plotly**: 5.24.1 버전 권장 (`"plotly<6"` 설치)
  - **Kaleido**: 0.2.1 버전 권장 (`"kaleido<1"` 설치)
- **설치**: `pip install -U playwright "kaleido<1" nbformat pandas "plotly<6" tqdm`

### Chapter 8: 연관 키워드 경쟁 강도 분석
- **증상**: Streamlit 업데이트로 숫자 천 단위 구분 기호 표시 방식이 변경됨
- **해결**: 데이터프레임 표시 시 명시적으로 포맷 지정
- **변경 내용**:
  - `step_3_1.py`: `st.dataframe()` → `st.dataframe(df.style.format())`로 변경
  - `step_3_2.py`: `column_config` 매개변수의 `format` 옵션에 `"localized"` 추가

### Chapter 12: 미쉐린 가이드 지도
- **증상**: 네이버 지도 웹사이트 UI 업데이트로 요소 선택자(locator) 변경 필요
- **변경 파일**: [ch_12/step_1_3.py](ch_12/step_1_3.py)
- **변경 내용**:
  - `slow_mo=1000` → `slow_mo=2000`: 브라우저 동작 속도 조절로 안정성 향상
  - 검색창 클릭: `get_by_label()` → `get_by_role("button", name="검색")`
  - 키워드 입력: `get_by_label()` → `get_by_role("combobox", name="장소, 버스, 지하철, 주소 검색")`

### Chapter 13: 생성형 AI 기사 번역 앱
- **증상**: Gemma3 최신 버전 출시 (기존 Gemma2에서 업그레이드)
- **해결**: 코드에서 `'gemma2:9b'` → `'gemma3:4b'` 또는 `'gemma3:12b'`로 변경
  - **최신 권장**: `ollama run gemma3:4b` (빠른 속도, 적은 메모리)
  - **고성능 옵션**: `ollama run gemma3:12b` (높은 품질, 더 많은 메모리)

### Chapter 14: 영어 받아쓰기 앱
- **증상**: Google에서 Gemini API 패키지명 변경
- **해결**: 최신 버전 코드 사용 권장 ([ch_14_genai](ch_14_genai/) 폴더)
- **설치**: `pip install -U google-cloud-texttospeech google-genai ipywidgets nltk streamlit`
- **변경 내용**:
  - 패키지명: `google-generativeai` → `google-genai`
  - API 사용법 전면 변경 (자세한 내용은 [ch_14_genai/README.md](ch_14_genai/README.md) 참고)
  - 시스템 프롬프트 일부 변경 (각 문장별 개행문자 추가) (자세한 내용은 [ch_14_genai/README.md](ch_14_genai/README.md) 참고)

## 💡 실습 가이드

### 개발 환경 설정
1. **Python 버전 권장사항**:
   - **기본**: Python 3.12.x 또는 3.13.x 버전
   - **Chapter 5 (EasyOCR)**: Python 3.12.x 필수
   - **Chapter 5 (PaddleOCR)**: Python 3.12.x 또는 3.13.x 모두 지원
   - **Python 3.12.x 설치 방법**: [ch_05/README.md](ch_05/README.md) 파일의 "🔽 파이썬 3.12.x 설치 가이드" 섹션 참고
2. **패키지 설치**: 각 챕터의 `README.md` 파일에서 설치 명령어 확인
3. **업데이트된 코드**: 변경사항이 있는 챕터는 새로운 폴더의 코드 사용 필수

### 폴더 구조 가이드

| 챕터 | 원본 폴더 | 업데이트 폴더 | 권장 사용 |
|------|-----------|---------------|-----------|
| **Chapter 5** | [ch_05](ch_05/) (EasyOCR) | [ch_05_paddleocr](ch_05_paddleocr/) (PaddleOCR) | 상황에 따라 선택 |
| **Chapter 14** | [ch_14](ch_14/) (구버전) | [ch_14_genai](ch_14_genai/) (최신버전) | [ch_14_genai](ch_14_genai/) ⭐ |

> ⭐ 표시된 옵션을 우선적으로 사용하시기 바랍니다.

## 😊 추가 도움이 필요하다면

기타 문의 사항이 있으실 경우 저자의 오픈 채팅에 문의해 주세요~!

- https://open.kakao.com/o/g5rNEh7d

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/open_chat.jpg" width="150" alt="혼자 만들면서 공부하는 파이썬 오픈 채팅">
