# Chapter 04 QR 코드로 연락처 공유

## 📋 실습 개요
이번 장에서는 **QR 코드 생성과 이미지 처리**를 통해 연락처 정보를 손쉽게 공유할 수 있는 시스템을 구현합니다.
- **qrcode**를 활용한 다양한 형태의 QR 코드 생성
- **vCard 형식**을 통한 표준 연락처 정보 구조화
- **Pillow(PIL)**를 사용한 이미지 합성 및 처리
- **vobject**로 복잡한 연락처 데이터 생성 및 관리

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
| **동영상 강의** | 최신 버전 `qrcode` 실습 가이드 | [강의 보러가기](https://www.youtube.com/watch?v=IpgPhZh4kXE&list=PLID7cC3lN2TF4D1uUL3gYoK6VEWlorbQ&index=31&t=376s) |

> 💡 **vobject 패키지**는 '좀 더 알아보기' 코너에서 VCF 파일을 편리하게 만드는 용도로 사용합니다. 자세한 내용은 책을 참고하세요.

## ✨ 결과물 예시
실습을 완료하면 다음과 같이 그림이 포함된 연락처 QR 코드를 만들 수 있습니다.

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/ch_04/output/step_x.png" width="300">


## 🚀 실습 단계별 가이드

*   **[step_1_1.py](step_1_1.py)**: 실습에 필요한 `input`, `output` 폴더를 생성하여 기본 작업 환경을 구성합니다.

*   **[step_1_2.py](step_1_2.py)**: `qrcode` 라이브러리를 사용하여 "헬로, QR 코드!"라는 텍스트가 포함된 간단한 QR 코드를 생성하고 표시하는 기본 예제입니다.

*   **[step_1_3.py](step_1_3.py)**: 유튜브 URL 주소를 담은 QR 코드를 생성하고 표시하여 웹 링크를 QR 코드로 변환하는 방법을 학습합니다.

*   **[step_1_4.py](step_1_4.py)**: 텍스트와 URL로 각각 QR 코드를 생성한 후, `output` 폴더에 별도의 PNG 이미지 파일로 체계적으로 저장합니다.

*   **[step_2_1.py](step_2_1.py)**: vCard(연락처) 형식의 문자열을 직접 구성하여 `.vcf` 파일로 저장하고, 동일한 문자열로 연락처 정보가 담긴 QR 코드를 생성합니다.

*   **[step_2_2.py](step_2_2.py)**: vCard 연락처 정보를 `.vcf` 파일과 QR 코드 `.png` 파일로 각각 `output` 폴더에 저장하는 완전한 스크립트를 작성합니다.

*   **[step_2_3.py](step_2_3.py)**: `vobject` 라이브러리를 사용하여 이름, 여러 개의 전화번호, 이메일 등 복잡한 정보를 포함한 vCard 객체를 생성하고, 이를 `.vcf` 파일과 QR 코드 이미지로 저장합니다.

*   **[step_3_1.py](step_3_1.py)**: `qrcode` 라이브러리의 `StyledPilImage` 기능을 사용하여 QR 코드 중앙에 이미지를 삽입하는 방법을 구현합니다. (구버전 `qrcode` 용)

*   **[step_3_1_new.py](step_3_1_new.py)**: 최신 `qrcode` 라이브러리(8.0 이상)에서 중앙에 이미지를 삽입하기 위해, 높은 오류 복원 수준(`ERROR_CORRECT_H`)을 명시적으로 설정하는 방법을 학습합니다.

*   **[step_3_2.py](step_3_2.py)**: `Pillow` 라이브러리를 사용하여, 이미 생성된 QR 코드 이미지의 우측 하단에 아이콘 이미지를 직접 붙여넣는 방식으로 이미지를 합성합니다.

*   **[step_x.py](step_x.py)**: `Pillow`을 이용해 QR 코드와 고양이 이미지를 새로운 흰색 배경 위에 좌우로 나란히 배치하여, 하나의 합성된 이미지로 만들고 파일로 저장하는 최종 프로젝트입니다.

모든 준비가 완료되었다면 QR 코드 연락처 공유 실습을 시작해보세요! 🚀
