# Chapter 12 미쉐린 가이드 지도

실습을 진행하기 위해 비주얼 스튜디오 코드 터미널에 아래 명령어를 입력하여 파이썬 패키지를 설치하세요.

```shell
pip install -U playwright datakart folium pandas streamlit streamlit-folium tqdm
```

또한 아래 명령어를 입력하여 최신 크로미움 브라우저를 설치하세요.

```shell
playwright install
```

## ⚠️ 중요 변화 사항 - Playwright Inspector Target 설정

Playwright Inspector를 사용할 때 **중요한 설정 변경이 필요**합니다:

- **문제**: Inspector 실행 시 locator 음영처리가 안 되거나, 녹화된 코드가 JavaScript로 생성되는 문제
- **원인**: 현재 버전에서는 Python 환경임에도 Node.js가 기본값으로 설정되는 버그
- **해결법**: Inspector 창 우측 상단의 **'Target' 메뉴**를 클릭하여 Python > **'Pytest'** 또는 **'Library'** 선택

> 📋 **자세한 설정 방법은 [INSPECTOR_TARGET.md](../INSPECTOR_TARGET.md) 파일을 참고하세요!**