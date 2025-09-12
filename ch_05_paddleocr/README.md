# Chapter 05 이미지 속 텍스트 번역하기 (PaddleOCR 버전)

## 🚨 중요한 변경 사항
**EasyOCR 패키지 사용 시 주의사항:** 일부 CPU 환경에서 오류 메시지 없이 프로그램이 갑자기 종료되는 현상이 발생할 수 있습니다. 이는 [GitHub 이슈](https://github.com/JaidedAI/EasyOCR/issues/704)로 등록되어 있으나 아직 완전히 해결되지 않은 상태입니다.

이러한 문제를 해결하기 위해 이 폴더에서는 **PaddleOCR**을 사용하여 동일한 실습을 진행할 수 있도록 준비했습니다.

**주요 변경 파일:**
  * [step_2_1.py](./step_2_1.py), [step_2_2.py](./step_2_2.py) - EasyOCR을 PaddleOCR로 교체
  * [step_2_4.py](./step_2_4.py), [step_3_4.py](./step_3_4.py) - 임시 파일 확장자를 '.tmp'에서 '.tmp.png'로 변경

> 💡 **PaddleOCR 소개:** 중국의 Baidu에서 개발한 OCR 패키지로, EasyOCR과 유사한 성능을 제공하면서도 다양한 언어를 지원하고 설치가 간편합니다.

## 📋 실습 개요
이번 장에서는 **OCR(Optical Character Recognition)** 기술을 활용하여 이미지 속 텍스트를 인식하고 번역하는 흥미로운 프로젝트를 진행합니다. 
- **PaddleOCR**을 사용하여 이미지에서 한국어/영어 텍스트를 정확하게 추출
- **DeepL API**를 활용한 고품질 자동 번역
- **PIL**을 통해 인식된 텍스트 위치를 직관적으로 시각화
- **Streamlit**으로 사용자 친화적인 웹 애플리케이션 구축

## ⚙️ PaddleOCR 관련 패키지 설치
실습을 원활하게 진행하기 위해 비주얼 스튜디오 코드 터미널에서 아래 명령어를 실행하여 필요한 파이썬 패키지들을 설치해주세요.

```shell
pip install -U paddlepaddle paddleocr pillow deepl streamlit ipywidgets setuptools
```

## 🔑 DeepL API 키 준비하기
세 번째 단계인 번역 실습을 위해서는 **DeepL API 키**가 필요합니다. 다음 단계를 따라 준비해주세요:
1. [DeepL API 웹사이트](https://www.deepl.com/pro-api)에서 무료 계정을 생성하세요
2. 발급받은 API 키를 복사하여 [step_3_1.py](./step_3_1.py)와 [step_3_2.py](./step_3_2.py) 파일의 `DEEPL_KEY` 변수에 입력하세요
3. 무료 계정은 월 50만 문자까지 번역이 가능합니다 (자세한 내용은 공식 웹사이트를 참고하세요)

## 🚀 실습 단계별 가이드

*   **[step_1.py](step_1.py)**: 실습에 필요한 `input`, `output` 폴더를 생성하여 기본 작업 환경을 구성합니다.

*   **[step_2_1.py](step_2_1.py)**: `paddleocr` 라이브러리를 사용하여 이미지(`ocr.jpg`)에서 텍스트를 인식하고, 인식된 텍스트 결과를 출력하는 기본 예제입니다.

*   **[step_2_2.py](step_2_2.py)**: PaddleOCR 로직을 재사용 가능한 `read_text` 함수로 구조화합니다. 특히 `easyocr`과 동일한 형식의 결과(좌표, 텍스트, 신뢰도)를 반환하도록 설계하여 호환성을 확보합니다.

*   **[step_2_3_poly.py](step_2_3_poly.py)**: `Pillow`의 `draw.polygon` 함수를 활용하여 두꺼운 외곽선을 가진 사각형을 그리는 방법을 학습하는 간단한 예제입니다.

*   **[step_2_3.py](step_2_3.py)**: OCR로 텍스트를 인식한 후, 원본 이미지 위에 인식된 텍스트 영역을 사각형(bounding box)으로 표시합니다. 신뢰도에 따라 사각형의 색상을 다르게 적용하여 직관적으로 시각화합니다.

*   **[step_2_4_widgets.py](step_2_4_widgets.py)**: `streamlit`의 핵심 위젯들인 버튼(`st.button`), 텍스트 입력창(`st.text_input`), 파일 업로더(`st.file_uploader`)의 사용법을 익히는 예제입니다.

*   **[step_2_4.py](step_2_4.py)**: `streamlit`을 사용하여 사용자가 이미지를 업로드하면 OCR을 수행하고, 원본 이미지와 텍스트 영역이 표시된 결과 이미지를 나란히 보여주는 간편한 웹 앱을 제작합니다.

*   **[step_3_1.py](step_3_1.py)**: `deepl` 라이브러리를 활용하여 "Hello, World!" 문장을 한국어로 번역하는 기본적인 API 사용법을 학습합니다.

*   **[step_3_2.py](step_3_2.py)**: OCR 기능과 번역 기능을 통합합니다. 이미지에서 `read_text`로 텍스트를 인식한 후, `deepl` API를 호출하여 각 텍스트 조각을 한국어로 번역하는 과정을 구현합니다.

*   **[step_3_3.py](step_3_3.py)**: 번역된 텍스트를 이미지 위에 시각화합니다. OCR로 인식된 영역을 반투명한 배경으로 채우고, 그 위에 번역된 텍스트를 덮어써서 자연스럽게 표시합니다.

*   **[step_3_4.py](step_3_4.py)**: 이미지 업로드, OCR, 번역, 결과 시각화 기능을 모두 결합한 완성도 높은 `streamlit` 웹 애플리케이션을 완성합니다.

*   **[step_x.py](step_x.py)**: 텍스트 시각화 방법을 한층 개선한 고급 예제입니다. 인식된 텍스트의 크기를 정확히 계산하여 텍스트 바로 뒤에만 반투명 배경을 추가하고 테두리를 그려, 원본 이미지의 가시성을 유지하면서도 텍스트 가독성을 극대화합니다.
