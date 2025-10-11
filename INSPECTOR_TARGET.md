# Playwright Inspector Target 설정 가이드

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/cover_1st.png" width="150" alt="혼자 만들면서 공부하는 파이썬 표지">

Playwright Inspector를 파이썬 환경에서 사용할 때 발생하는 Target 설정 문제와 해결방법을 설명합니다.

## 문제 상황

### 1. Locator 음영처리 문제
- Inspector 창 하단의 `Locator 탭`에서 `locator("table", has_text="코스피")` 등의 올바른 명령어를 입력해도 웹 브라우저에서 실시간 음영처리가 되지 않는 문제

### 2. 녹화 코드 언어 문제
- Record 버튼으로 사용자 액션을 녹화할 때 파이썬 코드 대신 JavaScript 등 다른 언어의 코드가 생성되는 문제

## 원인 분석
이전 버전에서는 파이썬 환경에서 Playwright를 실행하면 Inspector가 자동으로 파이썬 관련 모드(`Pytest`, `Library` 등)를 선택했지만, **현재는 Node.js 환경이 기본값으로 설정되는 버그**가 있습니다. 이는 파이썬 환경에서 Playwright를 실행함에도 불구하고 발생하는 문제입니다.

## 해결 방법

### Target 설정 변경
1. Playwright Inspector 창이 실행되면 **우측 상단의 'Target' 메뉴**를 클릭합니다
   
   <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/inspector_target.png" alt="Target 메뉴 선택" width="700"/>

2. `Python` 섹션에서 다음 중 하나를 선택합니다:
   - **Pytest**: pytest 기반 테스트 코드 생성
   - **Library**: 일반 Playwright 파이썬 라이브러리 코드 생성

### 추가 도움이 필요하다면
문제가 지속될 경우 저자의 오픈 채팅에 문의해 주세요!