# 파이썬 새 버전 출시 직후 패키지 설치 오류 해결 (윈도우 환경)

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/cover_1st.png" width="150" alt="혼자 만들면서 공부하는 파이썬 표지">

이 문서는 윈도우 환경에서 최신 pandas, streamlit 등 패키지를 설치할 때 C++ 빌드 도구가 필요하여 발생하는 설치 오류의 해결 방법을 설명합니다.

> 💡 **먼저 알아두세요.** 이 오류는 항상 발생하는 것이 아니라, 파이썬 메이저 버전이 새로 출시된 직후에 종종 나타나는 현상입니다. 시간이 지나면 각 패키지가 새 버전에 맞춘 배포판을 제공하면서 자연스럽게 해결되는 경향이 있습니다. 따라서 파이썬 메이저 버전업 초기에는 곧바로 새 버전을 설치하기보다, **출시 후 6개월 이상 기다렸다가 설치하는 것을 권장합니다.** 학습 단계에서는 안정적으로 검증된 이전 버전(예: 최신 버전 바로 아래의 버전)을 사용하는 것이 편리합니다.

> 🚨 이 문서는 윈도우 환경만 해당됩니다. macOS, 리눅스 환경에서는 적용되지 않습니다.

## 📋 목차
1. [문제 상황](#1-문제-상황)
2. [(방법 1) pip 등 패키지 설치 관련 업데이트](#2-방법-1-pip-등-패키지-설치-관련-업데이트)
3. [(방법 2) Microsoft C++ 빌드 도구 설치](#3-방법-2-microsoft-c-빌드-도구-설치)
4. [(방법 3) pypi 웹 사이트에서 빌드된 배포판 설치](#4-방법-3-pypi-웹-사이트에서-빌드된-배포판-설치)
5. [추가 도움이 필요하다면](#5-추가-도움이-필요하다면)

## 1. 문제 상황
윈도우 환경에서 최신 pandas, streamlit 등 패키지 설치 시 C++ 빌드 도구가 필요하여 아래 그림과 같은 설치 오류가 발생할 수 있습니다. 이 경우, 다음 방법에 따라 문제를 해결할 수 있습니다.

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/build_tools_00.png" alt="패키지 빌드 에러" width="600"/>

> ⚠️ 현재 시점(2025.10.15) 기준, 10월 7일에 발표된 파이썬 3.14 버전에서는 streamlit 패키지 설치에 오류가 발생할 수 있습니다. 이런 경우에는 파이썬 3.13.x 버전을 사용하시기 바랍니다.

## 2. (방법 1) pip 등 패키지 설치 관련 업데이트

pip, setuptools, wheel 패키지를 최신 버전으로 업데이트하고 다시 시도해보세요. VS Code 터미널에서 아래 명령어를 입력하여 실행합니다. 만약 계속 설치 오류가 발생하면 (방법 2)를 시도하세요.

```shell
python -m pip install --upgrade pip setuptools wheel
```

## 3. (방법 2) Microsoft C++ 빌드 도구 설치

1. [Microsoft C++ 빌드 도구](https://visualstudio.microsoft.com/ko/visual-cpp-build-tools/) 페이지로 이동하여 `Build Tools 다운로드` 메뉴를 클릭하여 설치 파일을 다운로드합니다.

    <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/build_tools_01.png" alt="C++ 빌드 도구 다운로드" width="600"/>

2. 다운로드한 설치 파일을 실행하여 Visual Studio 설치 관리자를 엽니다. 설치 시 오른쪽 상단의 `MSBuild 도구`가 선택된 것을 확인한 후 `설치` 버튼을 클릭하여 설치하세요.

    <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/build_tools_02.png" alt="C++ 빌드 도구 설치" width="600"/>

3. 이어서 컴퓨터를 재부팅한 후 다시 패키지 설치를 시도해보세요.

> ⚠️ 설치 후에는 반드시 컴퓨터를 재부팅해야 빌드 도구가 정상적으로 적용됩니다.

## 4. (방법 3) pypi 웹 사이트에서 빌드된 배포판 설치

만약 (방법 1), (방법 2)로도 해결되지 않는다면, [pypi.org](https://pypi.org/) 웹 사이트에서 미리 빌드된 배포판을 다운로드하여 설치할 수 있습니다. 예를 들어, pandas 패키지의 경우 다음 단계를 따르세요.

1. [pypi.org - pandas](https://pypi.org/project/pandas/#files) 페이지로 이동합니다.

2. 자신의 파이썬 버전과 운영체제에 맞는 `.whl` 파일을 다운로드합니다. 예를 들어, Python 3.14, Windows 64비트 환경에서는 `pandas-2.x.x-cp314-cp314-win_amd64.whl` 파일을 선택합니다.

    <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/build_tools_03.png" alt="pandas whl 파일 다운로드" width="600"/>

3. 다운로드한 `.whl` 파일을 작업 폴더에 복사한 후, VS Code 터미널에서 아래 명령어를 입력하여 설치합니다.

```shell
pip install pandas-2.x.x-cp314-cp314-win_amd64.whl
```

> ⚠️ 주의: 위 명령어에서 `pandas-2.x.x-cp314-cp314-win_amd64.whl` 부분은 다운로드한 파일의 실제 이름으로 변경해야 합니다. `pip install pandas` 까지만 입력한 후 `Tab` 키를 눌러 자동 완성 기능을 활용하면 편리합니다.

## 5. 추가 도움이 필요하다면

위 방법으로도 해결되지 않거나 도움이 필요하신 경우, 오픈 채팅으로 문의해 주세요.

- https://open.kakao.com/o/g5rNEh7d

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/open_chat.jpg" width="150" alt="혼자 만들면서 공부하는 파이썬 오픈 채팅">
