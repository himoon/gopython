# Chapter 04 QR 코드로 연락처 공유

## 📋 실습 개요
이번 장에서는 Python을 사용하여 vCard 연락처 정보가 담긴 QR 코드를 생성하는 방법을 배웁니다. `qrcode`와 `Pillow` 패키지를 활용하여 이미지가 포함된 QR 코드를 만드는 과정을 실습합니다.

## ⚙️ 패키지 설치
실습에 필요한 패키지를 비주얼 스튜디오 코드 터미널에 아래 명령어를 입력하여 설치하세요.

> ⚠️ **중요**: `qrcode` 패키지 버전 호환성 문제를 확인하세요!

### 📖 책 내용 그대로 실습하는 경우 (권장)
책과 동일한 환경으로 실습하려면 `qrcode` 버전을 `7.4.2`로 지정해야 합니다.
```bash
pip install "pillow==10.4.0" "qrcode==7.4.2" vobject
```

### 🆕 최신 버전의 qrcode 사용하는 경우
최신 버전의 `qrcode`로 실습하려면 아래 `중요: qrcode 패키지 버전 안내` 섹션을 참고하여 `step_3_1_new.py` 코드를 사용하세요.

## 🔥 중요: qrcode 패키지 버전 안내
`qrcode` 패키지 최신 버전(8.0 이상)에서는 이미지가 포함된 QR 코드를 생성할 때 `error_correction` 레벨을 `ERROR_CORRECT_Q` 또는 `ERROR_CORRECT_H`와 같이 [높은 수준으로 설정해야 하므로](https://pypi.org/project/qrcode/), 다음과 같은 `ValueError`가 발생할 수 있습니다:

```
ValueError: Error correction level must be ERROR_CORRECT_H if an embedded image is provided
```

이 문제를 해결하기 위한 두 가지 방법이 있습니다.

1.  **버전 고정 (책과 동일한 환경)**: 위의 `패키지 설치` 섹션에 안내된 대로 `qrcode==7.4.2` 버전을 설치합니다.
2.  **최신 버전에 맞는 코드 사용**: 최신 `qrcode` 버전을 사용하고 싶다면, 아래의 수정된 코드 파일과 동영상 강의를 참고하세요.

| 📋 구분 | 📝 설명 | 🔗 링크 |
|:---:|:---|:---:|
| **코드 파일** | 최신 버전에 맞게 수정된 실습 코드 | [step_3_1_new.py](step_3_1_new.py) |
| **동영상 강의** | 최신 버전 `qrcode` 실습 가이드 | [강의 보러가기](https://www.youtube.com/watch?v=IpgPhZh4kXE&list=PLID7cC3lN2TF4D1uUL3gYoK6VE7WlorbQ&index=31&t=376s) |

> 💡 **vobject 패키지**는 '좀 더 알아보기' 코너에서 VCF 파일을 편리하게 만드는 용도로 사용합니다. 자세한 내용은 책을 참고하세요.

## ✨ 결과물 예시
실습을 완료하면 다음과 같이 그림이 포함된 연락처 QR 코드를 만들 수 있습니다.

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/ch_04/output/step_x.png" width="300">


## 🚀 실습 순서
1.  [step_1_1.py](step_1_1.py): `qrcode` 패키지를 사용하여 가장 기본적인 QR 코드를 생성합니다.
2.  [step_1_2.py](step_1_2.py): QR 코드의 채우기 색과 배경색을 변경하는 방법을 실습합니다.
3.  [step_1_3.py](step_1_3.py): QR 코드 모듈의 모양을 기본 사각형에서 다른 스타일로 변경합니다.
4.  [step_1_4.py](step_1_4.py): QR 코드의 테두리(border) 두께를 조절합니다.
5.  [step_2_1.py](step_2_1.py): `vobject` 패키지로 vCard(가상 연락처)를 만들기 시작합니다.
6.  [step_2_2.py](step_2_2.py): 생성한 vCard에 이름, 전화번호, 이메일 등 상세 정보를 추가합니다.
7.  [step_2_3.py](step_2_3.py): 완성된 vCard 정보를 `.vcf` 파일 형식으로 저장하는 방법을 알아봅니다.
8.  [step_3_1.py](step_3_1.py): vCard 정보를 담은 QR 코드를 생성합니다. (책 기준 `qrcode==7.4.2` 버전용)
9.  [step_3_2.py](step_3_2.py): 생성된 QR 코드의 중앙에 로고 등 원하는 이미지를 삽입합니다.
10. [step_x.py](step_x.py): 배운 내용을 종합하여 나만의 커스텀 명함 QR 코드를 만드는 미니 프로젝트를 진행합니다.

> 💡 **참고**: 최신 `qrcode` 패키지를 사용한다면 8번 과정에서 `step_3_1.py` 대신 [step_3_1_new.py](step_3_1_new.py) 파일을 참고하세요.