# VS Code 파이썬 가상환경 설정 

이 문서는 VS Code에서 파이썬 가상환경을 설정하는 방법을 설명합니다. 가상환경은 프로젝트마다 독립적인 파이썬 환경을 제공하여, 패키지 충돌을 방지하고 의존성 관리를 쉽게 합니다.


## 1. 실행 중인 터미널 창 및 대화형 창 종료
현재 실행 중인 터미널 창이나 대화형 창을 모두 종료합니다.

- 아래 그림과 같이 여러 개의 터미널 창이 열려 있는 경우, 마우스를 오른쪽 터미널 목록에 가져가면 나타나는 휴지통 아이콘을 클릭하여 모두 종료하세요.

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/venv-01.png" alt="실행 중인 터미널 종료" width="700"/>


## 2. 터미널 기본 프로필 변경 (윈도우 사용자)
윈도우 환경인 경우 키보드 `F1` 키를 눌러 명령 팔레트를 열고, 아래 그림과 같이 터미널 기본 프로필을 명령 프롬프트(`Command Prompt`)로 변경하세요. 그래야 가상환경 설정 시 `(.venv)` 접두사가 제대로 표시됩니다.

- 명령 팔레트에서 `default profile` 입력 후 `터미널: 기본 프로필 선택` 클릭

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/venv-02.png" alt="터미널 기본 프로필 선택" width="700"/>

- `Command Prompt` 클릭

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/venv-03.png" alt="Command Prompt 클릭" width="700"/>

> ⚠️ macOS 환경에서는 이 단계를 건너뛰어도 됩니다. macOS는 기본적으로 `zsh` 또는 `bash`를 사용하는데, 별다른 설정이 없어도 `(.venv)` 접두사가 잘 표시됩니다.


## 3. 파이썬 가상환경 설치
이제 파이썬 가상환경을 설치할 준비가 되었습니다. 키보드 `F1` 키를 눌러 명령 팔레트를 열고, 아래 그림과 같이 파이썬 가상환경을 설치합니다.

- 명령 팔레트에서 `env` 입력 후 `Python: 환경 만들기` 클릭

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/venv-04.png" alt="파이썬 환경 만들기 클릭" width="700"/>

- `Venv` 클릭

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/venv-05-1.png" alt="Venv 클릭" width="700"/>

- `삭제 및 다시 생성` 클릭(만약 이 옵션이 보이지 않는다면, 다음 단계로 넘어가세요)

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/venv-05-2.png" alt="삭제 및 다시 생성 클릭" width="700"/>

- 설치할 파이썬 버전 클릭

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/venv-06.png" alt="설치할 파이썬 버전 클릭" width="700"/>

> ⚠️ `requirements.txt` 파일에서 패키지를 설치하라는 메시지가 나타나면, 무시하고 다음 단계를 진행하세요.


## 4. VS Code 새로고침
키보드 `F1` 키를 눌러 명령 팔레트를 열고, 아래 그림과 같이 VS Code를 새로고침합니다.

- 명령 팔레트에서 `reload` 입력 후 `Python: 캐시 지우기 및 창 다시 로드` 또는 `개발자: 창 다시 로드` 클릭

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/venv-07.png" alt="캐시 지우기 및 창 다시 로드 클릭" width="700"/>


## 5. 파이썬 가상환경 활성화 확인
새로 설치한 파이썬 가상환경이 잘 활성화되었는지 확인해야 합니다.

- VS Code 상단 메뉴에서 `터미널` 클릭 후 `새 터미널`을 선택하면, 아래 그림과 같이 `터미널 창`에 `(.venv)` 접두사가 표시됩니다.

- 파이썬 소스 코드를 열고, `대화형 창`에서 실행하면 아래 그림과 같이 우측 상단에 `.venv` 접두사가 표시되고, VS Code 하단 상태 표시줄에서도 `(.venv)` 접두사가 표시됩니다.

  <img src="https://raw.githubusercontent.com/himoon/gopython/refs/heads/main/images/venv-10.png" alt="대화형 창에서 가상환경 활성화 확인" width="700"/>

> ⚠️ **가상환경이 활성화되지 않은 경우**
> 1. VS Code를 완전히 종료한 후 다시 시작해 보세요.
> 2. 그래도 활성화되지 않는다면, 터미널에서 직접 활성화 명령어를 입력할 수 있습니다.
>    - **Windows (Command Prompt):** `\.venv\Scripts\activate`
>    - **macOS/Linux (zsh/bash):** `source .venv/bin/activate`
> 3. 윈도우 사용자는 터미널 기본 프로필이 `Command Prompt`로 올바르게 설정되었는지 다시 한번 확인해 보세요.
