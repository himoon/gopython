# Chapter 13 생성형 AI 기사 번역 앱

실습을 진행하기 위해 비주얼 스튜디오 코드 터미널에 아래 명령어를 입력하여 파이썬 패키지를 설치하세요.

```shell
pip install -U ollama streamlit trafilatura
```

*   **[step_1_1.py](step_1_1.py)**: 실습에 필요한 `input` 폴더를 생성하여 기본 작업 환경을 설정합니다.
*   **[step_1_2.py](step_1_2.py)**: `ollama` 라이브러리를 사용하여 대화형 AI 모델과 상호작용하지만, 이전 대화 내용을 기억하지 못하는 한계를 보여줍니다.
*   **[step_1_3.py](step_1_3.py)**: 대화 기록을 리스트에 저장하고 매번 요청 시 함께 전송하여, 모델이 이전 대화 내용을 기억하고 연속적인 대화를 할 수 있도록 구현합니다.
*   **[step_2_1.py](step_2_1.py)**: `streamlit`과 `st.session_state`를 사용하여 대화 기록을 저장하고 보여주는 기본적인 챗봇 웹 앱을 만듭니다.
*   **[step_2_2_zip.py](step_2_2_zip.py)**: 파이썬 내장 함수 `zip`을 사용하여 여러 개의 리스트를 병렬로 묶어 처리하는 방법을 보여주는 기본 예제입니다.
*   **[step_2_2.py](step_2_2.py)**: `streamlit`의 열(column) 기능을 활용하여 두 개의 다른 언어 모델(Gemma, Llama)의 답변을 나란히 비교하며 보여주는 챗봇 앱을 구현합니다.
*   **[step_3_1_trafilatura.py](step_3_1_trafilatura.py)**: `trafilatura` 라이브러리를 사용하여 웹 페이지(URL)에서 제목, 작성자 등 메타데이터를 포함한 구조화된 데이터(JSON)를 추출하는 방법을 보여줍니다.
*   **[step_3_1.py](step_3_1.py)**: `trafilatura`를 사용하여 지정된 URL의 뉴스 기사에서 본문 텍스트(마크다운 형식)와 대표 이미지 URL을 추출합니다.
*   **[step_3_2_sys_prompt.py](step_3_2_sys_prompt.py)**: `ollama.chat` 함수에 시스템 프롬프트(system prompt)를 전달하여 AI 모델의 역할이나 답변 스타일을 지정하는 방법을 보여주는 기본 예제입니다.
*   **[step_3_2.py](step_3_2.py)**: `trafilatura`로 추출한 기사 본문을 `ollama` 모델에 시스템 프롬프트와 함께 전달하여, 번역과 같은 특정 작업을 수행하도록 요청합니다.
*   **[step_3_3.py](step_3_3.py)**: 사용자가 URL을 입력하면 기사 원문과 이미지를 보여주고, 번역된 결과를 나란히 표시하는 완성된 형태의 `streamlit` 기사 번역 웹 앱을 만듭니다.
*   **[step_x.py](step_x.py)**: `streamlit`의 `st.write_stream`을 사용하여 모델의 답변을 실시간 스트리밍 형태로 표시하고, 답변 생성 중에는 입력창을 비활성화하여 사용자 경험을 개선한 챗봇 앱을 구현합니다.
