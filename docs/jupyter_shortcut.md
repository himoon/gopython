# VS Code 대화형 창(Interactive Window) 설정 안내

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/cover_1st.png" width="150" alt="혼자 만들면서 공부하는 파이썬 표지">

이 문서는 VS Code에서 파이썬 코드를 **대화형 창(Interactive Window)** 으로 실행하기 위한 설정 방법을 설명합니다. 대화형 창을 사용하면 파이썬 파일의 코드를 선택해 `Shift + Enter` 한 번으로 오른쪽 화면에서 바로 실행하고, 그 결과를 즉시 확인할 수 있습니다.

## 📋 목차
1. [사전 준비](#1-사전-준비)
2. [`jupyter exec` 설정하기](#2-jupyter-exec-설정하기)
3. [`jupyter mode` 설정하기](#3-jupyter-mode-설정하기)
4. [대화형 창으로 코드 실행하기](#4-대화형-창으로-코드-실행하기)
5. [추가 도움이 필요하다면](#5-추가-도움이-필요하다면)

## 1. 사전 준비
- VS Code를 실행합니다.
- 아직 파이썬 관련 확장 프로그램(`Python`, `Jupyter`)이 설치되어 있지 않다면 먼저 설치해 주세요.
- 키보드 `Ctrl + ,`(macOS는 `Cmd + ,`)를 눌러 **설정(Settings)** 화면을 엽니다.

> 💡 설정 화면은 상단 메뉴에서 `File(파일)` → `Preferences(기본 설정)` → `Settings(설정)` 순서로도 열 수 있습니다.

## 2. `jupyter exec` 설정하기
먼저 코드를 선택한 상태에서 `Shift + Enter`로 실행하는 기능을 켭니다.

1. 설정 화면의 검색창에 `jupyter exec`를 입력합니다.
2. 아래 그림처럼 **Jupyter › Interactive Window › Text Editor: Execute Selection** 항목을 찾습니다.
3. 해당 항목의 체크박스를 **켜(체크)** 줍니다. 이 옵션은 `Shift + Enter`를 눌렀을 때 선택한 코드를 대화형 창으로 보내 실행합니다.

	<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/jupyter-01-exec.png" alt="jupyter exec 설정 - Execute Selection 체크" width="700"/>

## 3. `jupyter mode` 설정하기
다음으로 대화형 창이 파일마다 하나씩 열리도록 설정합니다.

1. 설정 화면의 검색창에 `jupyter mode`를 입력합니다.
2. 아래 그림처럼 **Jupyter › Interactive Window: Creation Mode** 항목을 찾습니다.
3. 드롭다운 값을 **`perFile`** 로 선택합니다. 이렇게 하면 파이썬 파일마다 별도의 대화형 창이 생성되어 코드가 섞이지 않고 깔끔하게 관리됩니다.

	<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/jupyter-02-mode.png" alt="jupyter mode 설정 - Creation Mode를 perFile로 변경" width="700"/>

## 4. 대화형 창으로 코드 실행하기
이제 설정이 끝났으니 실제로 코드를 실행해 봅시다.

1. 실행할 파이썬 코드 파일(`.py`)을 엽니다.
2. 키보드 `Ctrl + A`(macOS는 `Cmd + A`)를 눌러 코드를 **전체 선택**합니다.
3. `Shift + Enter`를 누릅니다.
4. 아래 그림처럼 오른쪽 화면에 **대화형 창**이 새로 생성되고, 선택한 코드가 실행되어 결과가 표시되면 설정이 정상적으로 완료된 것입니다.

	<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/jupyter-03-done.png" alt="대화형 창에서 코드 실행 완료" width="700"/>

> 💡 코드의 일부만 선택한 뒤 `Shift + Enter`를 누르면 선택한 부분만 대화형 창에서 실행할 수 있습니다. 원하는 부분만 골라 실행하며 결과를 확인해 보세요.

## 5. 추가 도움이 필요하다면

위 방법으로도 대화형 창이 열리지 않거나 설정에 어려움이 있는 경우, 오픈 채팅으로 문의해 주세요.

- https://open.kakao.com/o/g5rNEh7d

	<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/open_chat.jpg" width="150" alt="혼자 만들면서 공부하는 파이썬 오픈 채팅">
