# VS Code 화면에 갑자기 오류/경고가 쏟아지는 경우

<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/cover_1st.png" width="150" alt="혼자 만들면서 공부하는 파이썬 표지">

최근 VS Code나 Python 관련 확장 프로그램 이후, 책의 예제 코드는 정상적으로 실행되는데도 편집기에서 갑자기 오류처럼 보이는 빨간 밑줄이나 경고 메시지가 표시될 수 있습니다. 이 문서를 통해 이러한 현상이 왜 생기는지, 해결책은 무엇인지 확인해 봅시다.

## 📋 목차
1. [현황](#1-현황)
2. [원인](#2-원인)
3. [해결책](#3-해결책)
4. [추가 도움이 필요하다면](#4-추가-도움이-필요하다면)

## 1. 현황
- 예제 코드를 실행하면 정상적으로 동작하는데, VS Code 편집기에서는 갑자기 오류가 생긴 것처럼 표시될 수 있습니다.
- 특히 최근 VS Code 업데이트 이후 아래와 같이 타입 관련 오류 메시지가 더 자주 보이는 경우가 있습니다.
- 이는 실제 실행 오류가 아니라, VS Code가 코드의 타입을 미리 점검하는 기능이 코드를 더 엄격하게 해석하면서 발생하는 경우가 많습니다.

	<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/type-mode-01.png" alt="type checking mode로 인한 오류 표시" width="700"/>

> 💡 즉, 코드 자체가 잘못되었다기보다는 VS Code가 "타입을 명확히 알 수 없다"고 판단해 경고를 보여주는 상황일 수 있습니다.

## 2. 원인
VS Code에서 파이썬 관련 확장 프로그램은 코드 실행과 별개로 **코드의 타입을 미리 점검하는 기능(Type Checking)**을 수행할 수 있습니다.

- 이 기능이 `basic` 또는 `strict`로 설정되어 있으면 변수 타입, 함수 인자, 반환값 등을 더 엄격하게 검사합니다.
- 따라서 코드는 정상 실행되더라도, VS Code가 코드를 미리 점검하는 단계에서 타입을 정확히 추론하지 못하면 편집기에서 경고가 표시될 수 있습니다.
- 특히 책의 예제 코드는 학습 목적상 간결하게 작성되어 있어 모든 코드에 타입 힌트가 붙어 있지 않으며, pandas, streamlit, 크롤링/자동화 관련 라이브러리처럼 동적으로 동작하는 도구도 이 기능에서는 오류처럼 보일 수 있습니다.
- 또한 업데이트나 설정 변경에 따라 Type Checking Mode가 `basic` 또는 `strict`로 활성화되면서, 이전에는 보이지 않던 경고가 갑자기 표시될 수도 있습니다.

## 3. 해결책
가장 간단한 방법은 VS Code에서 `Python Type Checking Mode` 설정을 `off`로 변경하는 것입니다.

### 설정 변경 방법
1. VS Code에서 `Ctrl + ,`를 눌러 설정 화면을 엽니다.
2. 검색창에 `type checking mode`를 입력합니다.
3. `Python › Analysis: Type Checking Mode` 항목을 찾습니다.
4. 아래 그림처럼 값을 `off`로 변경합니다.

	<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/type-mode-02.png" alt="type checking mode를 off로 변경" width="700"/>

### 설정 후 확인
- 열려 있는 Python 파일을 다시 확인해 보세요.
- 대부분의 타입 관련 경고가 사라집니다.
- 그래도 화면이 그대로라면 VS Code를 완전히 종료한 뒤 다시 실행해 보세요.

> ⚠️ `basic` 또는 `strict` 모드는 실무에서 타입 안정성을 높이는 데 도움이 될 수 있지만, 책의 예제를 따라 학습하는 단계에서는 불필요한 혼란을 줄 수 있습니다. 학습 중에는 `off`로 두고 진행하는 것을 권장합니다.

## 4. 추가 도움이 필요하다면

위 방법으로도 문제가 해결되지 않거나, 실제 실행 오류인지 편집기 경고인지 구분이 어려운 경우에는 오픈 채팅으로 문의해 주세요.

- https://open.kakao.com/o/g5rNEh7d

	<img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/open_chat.jpg" width="150" alt="혼자 만들면서 공부하는 파이썬 오픈 채팅">
