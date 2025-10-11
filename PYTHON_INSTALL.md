# VS Code 업데이트로 인한 대화형 창 커널 연결 문제 해결

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/cover_1st.png" width="150" alt="혼자 만들면서 공부하는 파이썬 표지">

최근 VS Code 업데이트로 인해 대화형 창이 Python 커널에 연결되지 않는 문제가 발생할 수 있습니다. 이는 주로 **VS Code가 관리자 권한으로 설치된 Python 경로에 접근하지 못해서** 발생하는 권한 문제입니다.

> ⚠️ **적용 대상**: 이 문서는 윈도우 환경에서만 해당됩니다. macOS나 리눅스 환경에서는 이 단계를 건너뛰어도 됩니다.

## 📋 목차
1. [문제 상황](#1-문제-상황)
2. [설치된 파이썬 삭제](#2-설치된-파이썬-설치파일-삭제)
3. [파이썬 재설치](#3-파이썬-최신-버전-다운로드-및-설치)
4. [설치 옵션 선택](#4-설치-옵션-선택)
5. [고급 옵션 선택](#5-고급-옵션-선택)
6. [VS Code 재설정](#6-vs-code-재실행-및-파이썬-가상환경-재설정)
7. [문제 해결이 안 되는 경우](#7-문제-해결이-안-되는-경우)

## 1. 문제 상황
- 최근 VS Code 업데이트로 인해 윈도우 환경에서 아래 그림과 같이 "커널에 연결:.venv (3.x.x)"이라는 팝업 메시지가 표시된 후 대화형 창이 Python 커널에 연결되지 않는 문제가 발생할 수 있습니다.
- 이는 **VS Code가 관리자 권한으로 설치된 Python의 경로에 접근하지 못해서** 발생합니다.
    
  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/win_install_0.png" alt="커널 연결 문제 발생" width="600"/>

### 🚨 핵심 원인
- **관리자 권한으로 설치된 Python**: 시스템 디렉토리(`C:\Program Files\Python3x\`)에 설치되어 VS Code가 접근 권한 문제로 인해 정상적으로 사용할 수 없음
- **VS Code의 접근 제한**: 일반 사용자 권한으로 실행되는 VS Code는 관리자 권한이 필요한 시스템 디렉토리의 Python에 접근할 수 없음
- **해결 방법**: Python을 **일반 사용자 계정용으로 재설치**하여 VS Code가 정상적으로 접근할 수 있도록 해야 함

## 2. 설치된 파이썬 설치파일 삭제
**관리자 권한으로 설치된 Python을 삭제**하고, 일반 사용자 계정용으로 재설치해야 합니다.
- **설정** → **앱** → **설치된 앱**으로 이동
- "Python" 검색 후 모든 Python 관련 항목 삭제
- **특히 관리자 권한으로 설치된 Python을 완전히 제거**
    
  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/win_install_1.png" alt="설치된 파이썬 삭제" width="600"/>

## 3. 파이썬 최신 버전 다운로드 및 설치
[파이썬 공식 웹사이트](https://www.python.org/)에서 파이썬 설치파일을 다운로드하고 설치합니다.
- **"Add python.exe to PATH"** 옵션을 반드시 체크
- **"Customize installation"** 클릭

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/win_install_2.png" alt="파이썬 설치 1단계" width="600"/>

## 4. 설치 옵션 선택
"Optional Features" 화면에서 기본 옵션을 그대로 두고 "Next"를 클릭합니다.
- 🚨 **"for all users" 옵션을 반드시 체크 해제**해야 합니다.

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/win_install_3.png" alt="파이썬 설치 2단계" width="600"/>

> 💡 이 옵션이 체크되어 있으면 다시 관리자 권한으로 설치되어 같은 문제가 재발합니다.

## 5. 고급 옵션 선택
"Advanced Options" 화면에서 올바른 설치 경로를 설정합니다.
- 🚨 **"Install Python 3.x for all users"** 옵션을 반드시 체크 해제 (가장 중요!)
- 나머지 옵션은 기본값으로 유지하고, **"Install"** 클릭하여 설치 진행  

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/win_install_4.png" alt="파이썬 설치 3단계" width="600"/>

> 💡 "for all users" 옵션이 체크되면 Python이 `C:\Program Files\`에 설치되어 VS Code가 접근할 수 없습니다. 체크 해제하면 `C:\Users\사용자명\AppData\Local\Programs\Python\`에 설치되어 VS Code가 정상적으로 접근할 수 있습니다.

## 6. VS Code 재실행 및 파이썬 가상환경 재설정
- **VS Code를 완전히 종료**한 후 다시 시작
- [VS Code 파이썬 가상환경 설정](VENV_SETUP.md) 문서에 따라 파이썬 가상환경을 다시 설정
- 실행할 코드를 선택한 후 `Shift + Enter` 키를 눌러 대화형 창에서 실행
- 아래와 같이 ipykernel 패키지가 필요하다는 메시지가 나타나면 **"설치"** 버튼을 클릭하여 설치를 진행합니다.

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/win_install_5.png" alt="ipykernel 패키지 설치 안내" width="600"/>

> 💡 ipykernel은 Jupyter 노트북과 VS Code 대화형 창을 연결하는 데 필요한 핵심 패키지입니다.

## 7. 문제 해결이 안 되는 경우

위 단계를 모두 수행했음에도 불구하고 문제가 계속 발생하는 경우:
- 저자의 이메일로 문의
- 오픈 채팅에 문의
- 문제 상황의 스크린샷과 함께 구체적인 오류 메시지를 포함해 주세요

