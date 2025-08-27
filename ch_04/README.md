# Chapter 04 QR 코드로 연락처 공유

## 📦 패키지 설치 및 버전 호환성

> ⚠️ **중요**: qrcode 패키지가 업데이트되어 최신 버전에서는 다음과 같은 에러가 발생할 수 있습니다:

```
ValueError: Error correction level must be ERROR_CORRECT_H if an embedded image is provided
```

### 📖 책 내용 그대로 실습하는 경우

책에 있는 내용을 그대로 실습하려면 비주얼 스튜디오 코드 터미널에 아래 명령어를 입력하여 qrcode 버전을 `7.4.2`로 고정해주세요.

```bash
pip install "pillow==10.4.0" "qrcode==7.4.2" vobject
```

> 💡 **vobject 패키지**는 '좀 더 알아보기' 코너에서 VCF 파일을 편리하게 만드는 용도로 사용합니다. 자세한 내용은 책을 참고하세요.

### 🆕 최신 버전의 qrcode 사용하는 경우

최신 버전의 qrcode로 실습하고 싶다면 아래 리소스를 활용하세요:

| 📋 구분 | 📝 설명 | 🔗 링크 |
|:---:|:---|:---:|
| **코드 파일** | 최신 버전에 맞는 실습 코드 | [step_3_1_new.py](step_3_1_new.py) |
| **동영상 강의** | 최신 버전 qrcode 실습 가이드 | [강의 보러가기](https://www.youtube.com/watch?v=IpgPhZh4kXE&list=PLID7cC3lN2TF4D1uUL3gYoK6VE7WlorbQ&index=31&t=376s) |
