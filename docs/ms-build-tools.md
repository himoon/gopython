# 최신 pandas, streamlit 등 최신 패키지 설치 오류 해결 방법(윈도우 환경)

윈도우 환경에서 최신 pandas, streamlit 등 패키지 설치 시 C++ 빌드 도구가 필요하여 설치 오류가 발생할 수 있습니다. 이 경우, 아래 방법에 따라 문제를 해결할 수 있습니다. 

추가로 현재 시점(2025.10.15)에 10.7일에 발표된 파이썬 3.14 버전에서는 streamlit 패키지 설치에 오류가 발생할 수 있습니다. 이런 경우에는 파이썬 3.13.x 버전을 사용하시기 바랍니다.

> 🚨 이 문서는 윈도우 환경만 해당됩니다. macOS, 리눅스 환경에서는 적용되지 않습니다.

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/build_tools_00.png" alt="패키지 빌드 에러" width="600"/>

## (방법 1) pip 등 패키지 설치 관련 업데이트

pip, setuptools, wheel 패키지를 최신 버전으로 업데이트하고 다시 시도해보세요. VS Code 터미널에서 아래 명령어를 입력하여 실행합니다. 만약 계속 설치 오류가 발생하면 (방법 2)를 시도하세요.

```shell
python -m pip install --upgrade pip setuptools wheel
```

## (방법 2) Microsoft C++ 빌드 도구 설치

1. [Microsoft C++ 빌드 도구](https://visualstudio.microsoft.com/ko/visual-cpp-build-tools/) 페이지로 이동하여 `Build Tools 다운로드` 메뉴를 클릭하여 설치 파일을 다운로드합니다.

    <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/build_tools_01.png" alt="C++ 빌드 도구 다운로드" width="600"/>

2. 다운로드한 설치 파일을 실행하여 Visual Studio 설치 관리자를 엽니다. 설치 시 오른쪽 상단의 `MSBuild 도구`가 선택된 것을 확인한 후 `설치` 버튼을 클릭하여 설치하세요.

    <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/build_tools_02.png" alt="C++ 빌드 도구 설치" width="600"/>

3. ⚠️ 이어서 컴퓨터를 재부팅한 후 다시 패키지 설치를 시도해보세요.

## (방법 3) pypi 웹 사이트에서 빌드된 배포판 설치

만약 (방법 1), (방법 2)로도 해결되지 않는다면, [pypi.org](https://pypi.org/) 웹 사이트에서 미리 빌드된 배포판을 다운로드하여 설치할 수 있습니다. 예를 들어, pandas 패키지의 경우 다음 단계를 따르세요.

1. [pypi.org - pandas](https://pypi.org/project/pandas/#files) 페이지로 이동합니다.

2. 자신의 파이썬 버전과 운영체제에 맞는 `.whl` 파일을 다운로드합니다. 예를 들어, Python 3.14, Windows 64비트 환경에서는 `pandas-2.x.x-cp314-cp314-win_amd64.whl` 파일을 선택합니다.

    <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/build_tools_03.png" alt="pandas whl 파일 다운로드" width="600"/>

3. 다운로드한 `.whl` 파일을 작업 폴더에 복사한 후, VS Code 터미널에서 아래 명령어를 입력하여 설치합니다.

```shell
pip install pandas-2.x.x-cp314-cp314-win_amd64.whl
```

> ⚠️ 주의: 위 명령어에서 `pandas-2.x.x-cp314-cp314-win_amd64.whl` 부분은 다운로드한 파일의 실제 이름으로 변경해야 합니다. `pip install pandas` 까지만 입력한 후 `Tab` 키를 눌러 자동 완성 기능을 활용하면 편리합니다.

## 😊 추가 도움이 필요하다면

만약 위 방법으로도 해결되지 않는다면, 저자의 오픈 채팅에 문의해 주세요~!

- https://open.kakao.com/o/g5rNEh7d

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/open_chat.jpg" width="150" alt="혼자 만들면서 공부하는 파이썬 오픈 채팅">
