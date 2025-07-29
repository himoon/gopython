# Chapter 05 이미지 속 텍스트 번역하기

## 🚨 중요한 변경 사항
**EasyOCR 패키지 실습 시 일부 CPU에서 오류 메시지 없이 프로그램이 종료되는 현상이 발생**할 수 있습니다. 이와 관련하여 GitHub 이슈가 등록되어 있으나, 아직 해결되지 않았습니다.
따라서, EasyOCR 패키지로 실습이 어려운 경우 **PaddleOCR**를 사용하여 실습을 진행해 주세요.

  * `step_2_1.py`, `step_2_2.py` - EasyOCR 대신 PaddleOCR로 변경
  * `step_2_4.py`, `step_3_4.py` - 임시 파일의 확장자 '.tmp'를 '.tmp.png'로 변경

## ⚙️ 패키지 설치
실습을 진행하기 위해 비주얼 스튜디오 코드 터미널에 아래 명령어를 입력하여 파이썬 패키지를 설치하세요.

```shell
pip install -U paddlepaddle paddleocr deepl streamlit ipywidgets setuptools
```

> 나머지 내용은 EasyOCR 패키지와 동일합니다. 따라서, EasyOCR 패키지의 설치 방법과 사용법을 참고하세요.