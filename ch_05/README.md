# Chapter 05 이미지 속 텍스트 번역하기

## 📋 실습 개요
이번 장에서는 **OCR(Optical Character Recognition)** 기술을 활용하여 이미지 속 텍스트를 인식하고 번역하는 프로젝트를 진행합니다. 
- **EasyOCR**로 이미지에서 한국어/영어 텍스트 추출
- **DeepL API**를 이용한 자동 번역
- **PIL**로 인식된 텍스트 위치 시각화
- **Streamlit**으로 웹 애플리케이션 제작

## 📁 실습 파일 구조
```
ch_05/
├── step_1.py           # 기본 디렉토리 설정
├── step_2_1.py         # EasyOCR 기본 사용법
├── step_2_2.py         # 문자 인식 함수 작성
├── step_2_3.py         # 인식 결과 바운딩 박스 그리기
├── step_2_3_poly.py    # 다각형 바운딩 박스
├── step_2_4.py         # 인식률에 따른 색상 구분
├── step_2_4_widgets.py # Streamlit 위젯 활용
├── step_3_1.py         # DeepL API 기본 사용법
├── step_3_2.py         # OCR + 번역 조합
├── step_3_3.py         # 번역 결과를 이미지에 표시
├── step_3_4.py         # Streamlit 웹앱 완성
├── step_x.py           # 추가 실습 (배경이 있는 텍스트)
├── input/              # 실습용 이미지 파일들
│   ├── ocr.jpg         # 메인 실습 이미지
│   ├── handwriting.jpg # 손글씨 이미지
│   ├── poster.jpg      # 포스터 이미지
│   ├── Pretendard-Bold.ttf # 한글 폰트
│   └── ...             # 추가 이미지 파일들
└── output/             # 결과 이미지 저장 폴더
```

## ⚙️ 패키지 설치
실습을 진행하기 위해 비주얼 스튜디오 코드 터미널에 아래 명령어를 입력하여 파이썬 패키지를 설치하세요.

```shell
pip install -U "numpy<=1.26.4" "torch<=2.5.1" "torchvision<=0.20.1" "easyocr<=1.7.2" "pillow<=10.4.0" deepl streamlit
```

## 🚨 중요한 사전 준비사항

### 💡 OCR 실습 개요
이번 실습은 문자 인식을 위해 최신 딥러닝 모델을 실제로 다운로드하여 실습해볼 수 있는 프로젝트입니다:
- **딥러닝 모델 체험**: 실제 AI 모델 파일을 다운로드하여 사용합니다
- **최신 기술 활용**: PyTorch, EasyOCR 등 최신 AI 라이브러리를 체험합니다
- **정확한 환경 설정**: 원활한 실습을 위해 파이썬과 패키지 버전을 맞춰 진행합니다

### 🐍 파이썬 3.12.x 버전 필수!
딥러닝 모델이 정상적으로 작동하려면 **반드시 파이썬 3.12.x 버전**을 사용해야 합니다.

#### 🔽 파이썬 3.12.x 다운로드 방법

**Windows 사용자**
1. [Python 공식 웹사이트](https://www.python.org/downloads/release/python-3127/)에 접속
2. 페이지 하단의 `Windows installer (64-bit)` 클릭하여 다운로드
3. 다운로드된 파일을 실행하여 설치

**macOS 사용자**
1. [Python 공식 웹사이트](https://www.python.org/downloads/release/python-3127/)에 접속
2. 페이지 하단의 `macOS 64-bit universal2 installer` 클릭하여 다운로드
3. 다운로드된 .pkg 파일을 실행하여 설치

### 🔑 DeepL API 키 준비
3단계 번역 실습을 위해서는 **DeepL API 키**가 필요합니다:
1. [DeepL API 웹사이트](https://www.deepl.com/pro-api)에서 무료 계정 생성
2. API 키를 복사하여 `step_3_1.py`와 `step_3_2.py`의 `DEEPL_KEY` 변수에 입력
3. 무료 계정은 월 50만 문자까지 번역 가능 (웹 사이트 참고)

### 🆘 도움이 필요한 경우
- 파이썬 3.12.x 버전 설치가 어려운 경우
- 가상환경 설정이 복잡한 경우
- 패키지 설치 중 오류가 발생하는 경우
- DeepL API 키 설정이 어려운 경우

**👉 저자의 오픈 채팅에 문의해 주세요!**

---

## 🎯 실습 시작 전 체크리스트
- [ ] 파이썬 3.12.x 버전 설치 완료
- [ ] 가상환경 설정 완료 (명령 팔레트 활용)
  - `F1` 또는 `Ctrl/Cmd+Shift+P` → `env` 입력 → `Python: 환경 만들기` 선택 
  - `Venv` 선택 → `Python 3.12.x` 선택
  - ⚠️ **기존 가상환경이 있는 경우**: `삭제 및 다시 생성` 메뉴가 나타나면 클릭하여 새로 생성
- [ ] 필수 패키지 설치 완료 (터미널 활용)
- [ ] DeepL API 키 준비 완료 (3단계 실습용)
- [ ] 인터넷 연결 확인 (모델 다운로드용)

## 🚀 실습 순서
1. **step_1.py**: 기본 환경 설정 및 폴더 생성
2. **step_2_1.py**: EasyOCR로 첫 문자 인식 체험
3. **step_2_2.py**: 재사용 가능한 문자 인식 함수 작성
4. **step_2_3.py**: 인식된 텍스트 위치를 이미지에 표시
5. **step_3_1.py**: DeepL API로 번역 기능 테스트
6. **step_3_2.py**: OCR과 번역 기능 결합
7. **step_3_3.py**: 번역된 텍스트를 이미지에 오버레이
8. **step_3_4.py**: Streamlit으로 웹 애플리케이션 완성

모든 준비가 완료되었다면 OCR 실습을 시작해보세요! 🚀