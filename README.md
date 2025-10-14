# <혼자 만들면서 공부하는 파이썬> 책의 깃허브 자료실

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/cover_1st.png" width="150" alt="혼자 만들면서 공부하는 파이썬 표지">

## 📢 공지사항

- [**유튜브 채널 - 동영상 강의를 통해 더 깊이 있는 학습을 해보세요!**](https://www.youtube.com/@moon-hyunil)

## 🚀 판매처

- [yes24](https://www.yes24.com/Product/Goods/142258696)
- [교보문고](https://product.kyobobook.co.kr/detail/S000215710144)
- [알라딘](http://aladin.kr/p/lzsPq)
- [한빛미디어](https://www.hanbit.co.kr/store/books/look.php?p_code=B5580711889)

## 🚨 (긴급) 대화형 창 커널 연결 문제 해결

- [VS Code 업데이트로 인한 대화형 창 커널 연결 문제 해결 가이드](PYTHON_INSTALL.md)

## 🔧 Venv 파이썬 가상환경 설정 오류 발생 시 재설정 방법 안내

- **문제 상황**: 가상환경 생성 실패, 패키지 설치 오류, 인터프리터 인식 불가 등
- **해결 방법**: 기존 가상환경 완전 삭제 후 재설정
- **📋 자세한 재설정 방법**: [VENV_SETUP.md](VENV_SETUP.md) 파일 참고

## ⚠️ 중요한 코드 업데이트 안내

일부 챕터의 코드가 외부 환경 변화로 인해 업데이트되었습니다. 원활한 실습을 위해 반드시 확인해 주세요!

### Playwright Inspector Target 설정 (Chapter 6, 7, 12)
- **문제**: Inspector 실행 시 locator 음영처리가 안 되거나, 녹화된 코드가 JavaScript로 생성되는 문제
- **원인**: 현재 버전에서는 Python 환경임에도 Node.js가 기본값으로 설정되는 버그
- **해결법**: Inspector 창 우측 상단의 **'Target' 메뉴** 클릭 → Python > **'Pytest'** 또는 **'Library'** 선택
- **📋 자세한 설정 방법**: [INSPECTOR_TARGET.md](INSPECTOR_TARGET.md) 파일 참고

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
- **사이트 접근 문제**: 네이버플러스 스토어 직접 접근 시 오류 발생
- **해결책**: 네이버 메인 페이지 → 네이버플러스 스토어 버튼 클릭 방식으로 변경
- **⚠️ 변경된 파일**: [step_1_2.py](ch_06/step_1_2.py), [step_1_3.py](ch_06/step_1_3.py)

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

## 😊 기타 문의 사항

기타 문의 사항이 있으실 경우 저자의 오픈 채팅에 문의해 주세요.
- https://open.kakao.com/o/g5rNEh7d

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/open_chat.jpg" width="150" alt="혼자 만들면서 공부하는 파이썬 오픈 채팅">
