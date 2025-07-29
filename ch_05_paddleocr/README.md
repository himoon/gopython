# Chapter 05 이미지 속 텍스트 번역하기

## 🚨 중요한 변경 사항
**EasyOCR 패키지 실습 시 일부 CPU에서 오류 메시지 없이 프로그램이 종료되는 현상이 발생**할 수 있습니다. 이와 관련하여 [GitHub 이슈](https://github.com/JaidedAI/EasyOCR/issues/704)가 등록되어 있으나, 아직 해결되지 않았습니다.
따라서, EasyOCR 패키지로 실습이 어려운 경우 **PaddleOCR**를 사용하여 실습을 진행해 주세요. 

  * `step_2_1.py`, `step_2_2.py` - EasyOCR 대신 PaddleOCR로 변경
  * `step_2_4.py`, `step_3_4.py` - 임시 파일의 확장자 '.tmp'를 '.tmp.png'로 변경

> [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)은 중국의 Baidu에서 개발한 OCR 패키지로, EasyOCR과 유사한 기능을 제공합니다. 또한, 다양한 언어를 지원하며, 설치가 간편합니다.

## ⚙️ PaddleOCR 관련 패키지 설치
실습을 진행하기 위해 비주얼 스튜디오 코드 터미널에 아래 명령어를 입력하여 파이썬 패키지를 설치하세요.

```shell
pip install -U paddlepaddle paddleocr deepl streamlit ipywidgets setuptools
```