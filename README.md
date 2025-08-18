# 혼자 만들면서 공부하는 파이썬

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/cover_1st.png" width="150" alt="혼자 만들면서 공부하는 파이썬 표지">

## 📢 공지사항

- [**온라인 소스 코드 - 필요한 코드를 쉽게 복사해서 실습하세요!**](https://github.com/himoon/gopython)

- [**유튜브 채널 - 동영상 강의를 통해 더 깊이 있는 학습을 해보세요!**](https://www.youtube.com/@moon-hyunil)

## 🚀 판매처

- [yes24](https://www.yes24.com/Product/Goods/142258696)
- [교보문고](https://product.kyobobook.co.kr/detail/S000215710144)
- [알라딘](http://aladin.kr/p/lzsPq)
- [한빛미디어](https://www.hanbit.co.kr/store/books/look.php?p_code=B5580711889)

## ⚠️ 중요한 코드 업데이트 안내

일부 챕터의 코드가 외부 환경 변화로 인해 업데이트되었습니다. 원활한 실습을 위해 반드시 확인해 주세요!

### Chapter 1: 폴더 크기 측정 프로그램
- **성능 최적화 필수**: `step_2_3.py` 실행 시 홈 디렉토리의 모든 폴더를 추출하므로 사전 작업이 필요합니다
- **권장 실습 순서**: 
  1. `step_2_3.py` 실행 → `step_2_3.json` 파일 생성
  2. JSON 파일을 열어 불필요한 폴더 목록 삭제 (⭐ 필수)
  3. `step_2_4.py` 실행하여 폴더 크기 측정
- **⚠️ 반드시 삭제해야 할 폴더**: OneDrive, Google Drive, iCloud Drive 등 클라우드 폴더
  > 클라우드 폴더는 수천 개의 하위 폴더를 포함하여 실습 시간이 매우 길어집니다

### Chapter 5: 이미지 속 텍스트 번역하기
- **환경 문제**: EasyOCR 패키지가 일부 CPU에서 오류 없이 종료되는 현상 발생
- **해결책**: PaddleOCR을 사용한 대체 코드 제공 (`ch_05_paddleocr/` 폴더)
- **패키지 설치**: `pip install -U paddlepaddle paddleocr pillow deepl streamlit ipywidgets setuptools`
- **주요 변경사항**:
  - EasyOCR → PaddleOCR로 변경
  - 임시 파일 확장자 `.tmp` → `.tmp.png`로 변경

### Chapter 6: 쇼핑 트렌드 분석  
- **사이트 접근 문제**: 네이버플러스 스토어 직접 접근 시 오류 발생
- **해결책**: 네이버 메인 페이지 → 네이버플러스 스토어 버튼 클릭 방식으로 변경
- **⚠️ 변경된 파일**: `step_1_2.py`, `step_1_3.py`

### Chapter 13: 생성형 AI 기사 번역 앱
- **모델 업데이트**: Gemma3 최신 버전 출시 (기존 Gemma2에서 업그레이드)
- **권장 사용법**: 
  - **최신 권장**: `ollama run gemma3:4b` (빠른 속도, 적은 메모리)
  - **고성능 옵션**: `ollama run gemma3:12b` (높은 품질, 더 많은 메모리)
- **코드 수정**: `'gemma2:9b'` → `'gemma3:4b'` 또는 `'gemma3:12b'`로 변경

### Chapter 14: 영어 받아쓰기 앱
- **API 변경**: Google에서 Gemini API 패키지명 변경
- **최신 버전**: `ch_14_genai/` 폴더 사용 권장
- **패키지 설치**: `pip install -U google-cloud-texttospeech google-genai ipywidgets nltk streamlit`
- **⚠️ 주요 변경사항**:
  - 패키지명: `google-generativeai` → `google-genai`
  - API 사용법 전면 변경 (자세한 내용은 `ch_14_genai/README.md` 참고)

## 💡 실습 가이드

### 🔧 개발 환경 설정
1. **Python 버전 권장사항**:
   - **기본**: Python 3.12.x 또는 3.13.x 버전
   - **Chapter 5 (EasyOCR)**: Python 3.12.x 필수
   - **Chapter 5 (PaddleOCR)**: Python 3.12.x 또는 3.13.x 모두 지원
2. **패키지 설치**: 각 챕터의 `README.md` 파일에서 설치 명령어 확인
3. **업데이트된 코드**: 변경사항이 있는 챕터는 새로운 폴더의 코드 사용 필수

### 📂 폴더 구조 가이드

| 챕터 | 원본 폴더 | 업데이트 폴더 | 권장 사용 |
|------|-----------|---------------|-----------|
| **Chapter 5** | `ch_05/` (EasyOCR) | `ch_05_paddleocr/` (PaddleOCR) | 상황에 따라 선택 |
| **Chapter 14** | `ch_14/` (구버전) | `ch_14_genai/` (최신버전) | `ch_14_genai/` ⭐ |

> ⭐ 표시된 옵션을 우선적으로 사용하시기 바랍니다.
