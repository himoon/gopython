# Chapter 14 영어 받아쓰기 앱

## 📋 실습 개요
이번 장에서는 **Google Gemini AI와 음성 합성 기술**을 결합하여 이미지 기반 영어 받아쓰기 애플리케이션을 구현합니다.
- **Google Gemini Vision**을 활용한 이미지 분석 및 설명 생성  
- **Google Cloud Text-to-Speech**를 통한 고품질 음성 합성
- **NLTK**를 이용한 자연어 처리 및 문장 분할
- **Streamlit**으로 사용자 친화적인 학습 인터페이스 구현

## ⚠️ 중요한 변화: 새로운 패키지로 업그레이드!
최근 Google에서 Gemini API 패키지명을 변경했습니다:
- **구버전**: `google-generativeai` 
- **최신버전**: `google-genai` 

이 폴더(`ch_14_genai`)의 코드들은 모두 **최신 패키지**를 사용합니다. 구버전과의 차이점을 학습하려면 [ch_14](../ch_14/) 폴더의 코드와 비교해보세요.

## ⚙️ 패키지 설치
실습을 원활하게 진행하기 위해 비주얼 스튜디오 코드 터미널에서 아래 명령어를 실행하여 필요한 파이썬 패키지들을 설치해주세요.

```shell
pip install -U google-cloud-texttospeech google-genai ipywidgets nltk streamlit
```

## 🔑 API 키 준비하기
이 실습에서는 **두 가지 Google API 키**가 필요합니다. 다음 단계를 따라 준비해주세요:

**1️⃣ Google Gemini API 키**
1. [Google AI Studio](https://aistudio.google.com/) 접속
2. 회원가입 후 로그인
3. 'Get API Key' 메뉴에서 API 키 발급
4. 발급받은 API 키를 해당 실습 파일의 `API_KEY` 변수에 입력하세요

**2️⃣ Google Cloud Text-to-Speech API 키**
1. [Google Cloud Console](https://console.cloud.google.com/) 접속
2. 프로젝트 생성 및 Text-to-Speech API 활성화
3. 서비스 계정 생성 후 JSON 키 파일 다운로드
4. 다운로드한 JSON 파일을 `API_KEY.json`으로 이름 변경 후 `input` 폴더에 저장

## 🚀 실습 단계별 가이드
*   **[step_1_1.py](step_1_1.py)**: 실습에 필요한 `img`, `input`, `output` 폴더를 생성하여 기본 작업 환경을 구성합니다.

*   **[step_1_2_gemini.py](step_1_2_gemini.py)**: 새로운 `google-genai` 패키지를 사용하여 Gemini 모델과 대화하고, `client.chats.create()`를 통해 생성된 챗 객체로 대화 기록을 관리하는 기본 예제입니다.

*   **[step_1_2.py](step_1_2.py)**: `streamlit`을 사용하여 이미지를 업로드하고, 새로운 Gemini 클라이언트를 통해 이미지에 대한 질문을 하는 간단한 웹 애플리케이션을 만듭니다.

*   **[step_1_3.py](step_1_3.py)**: `st.session_state`와 새로운 `google-genai` API를 활용하여 업로드된 이미지에 대한 대화 기록을 유지하는 챗봇 앱을 구현합니다. `chat.get_history()`로 대화 기록을 확인할 수 있습니다.

*   **[step_2_1_tts.py](step_2_1_tts.py)**: Google Cloud Text-to-Speech(TTS) API를 사용하여 텍스트 파일의 내용을 고품질 음성(MP3)으로 변환하는 기본 예제입니다.

*   **[step_2_1.py](step_2_1.py)**: Google Cloud TTS API 사용에 필요한 인증된 클라이언트 객체를 생성하는 함수를 정의하여 음성 합성 환경을 구성합니다.

*   **[step_2_2.py](step_2_2.py)**: 텍스트와 음성 종류를 입력받아 합성된 음성 데이터를 바이트(bytes) 형태로 반환하는 `synth_speech` 함수를 정의하고, 이를 사용해 텍스트 파일을 MP3로 변환합니다.

*   **[step_2_3_nltk.py](step_2_3_nltk.py)**: `NLTK` 라이브러리의 `sent_tokenize`를 사용하여 텍스트를 문장 단위로 정확하게 분리하는 방법을 학습하는 기본 예제입니다.

*   **[step_2_3.py](step_2_3.py)**: `NLTK`로 텍스트를 문장별로 나눈 뒤, 각 문장을 개별 음성 파일(MP3)로 변환하여 체계적으로 저장합니다.

*   **[step_3_1_format.py](step_3_1_format.py)**: 파이썬의 f-string과 `.format()` 메서드를 사용하여 문자열 서식을 지정하는 방법을 학습하는 기본 예제입니다.

*   **[step_3_1_prompt.py](step_3_1_prompt.py)**: 일회성 요청에 사용하는 `client.models.generate_content` 메서드에 시스템 프롬프트를 제공하여 이미지 분석 응답을 정확하게 유도하는 방법을 학습합니다.

*   **[step_3_1.py](step_3_1.py)**: `google-genai`의 대화형 방식을 사용하여, 각기 다른 시스템 프롬프트를 가진 별도의 챗 세션을 생성함으로써 이미지 묘사, 퀴즈 출제, 피드백 생성 기능을 체계적으로 구현합니다.

*   **[step_3_2.py](step_3_2.py)**: `streamlit` 애플리케이션으로, 이미지를 업로드하면 `step_3_1.py`의 함수를 호출하여 퀴즈, 정답, 음성 파일 경로를 생성하고 세션 상태에 저장하며, 새 문제로 다시 시작하는 기능을 포함합니다.

*   **[step_3_3.py](step_3_3.py)**: 새로운 `google-genai` 패키지를 사용하여 만든, 이미지 기반의 영어 받아쓰기 웹 앱의 완성된 형태입니다. 생성된 퀴즈와 음성 플레이어를 보여주고, 사용자의 답을 받아 즉시 피드백을 제공합니다.

*   **[step_x.py](step_x.py)**: 최종 앱에 사이드바를 추가하여 사용자가 TTS 음성을 직접 선택할 수 있도록 기능을 개선한, `google-genai` 패키지 기반 최종 버전입니다. 음성을 변경하면 퀴즈가 자동으로 초기화됩니다.

## 📚 새로운 패키지의 주요 변화점

### 기본적인 사용법 비교
새로운 패키지에서는 AI와 대화하는 방식이 더 간단하고 명확해졌습니다:

| 단계 | 구버전 (`google-generativeai`) | 최신버전 (`google-genai`) |
|---|---|---|
| **패키지 가져오기** | `import google.generativeai as genai` | `from google import genai` |
| **AI 준비하기** | `genai.configure(api_key="키")`<br>`model = genai.GenerativeModel("모델명")` | `client = genai.Client(api_key="키")` |
| **대화 시작하기** | `chat = model.start_chat()` | `chat = client.chats.create(model="모델명")` |
| **대화 기록 보기** | `print(chat.history)` | `print(chat.get_history())` |

### 개선된 특징들
- **더 간단한 구조**: `Client` 객체 하나로 모든 기능 관리
- **명확한 API**: 각 기능의 역할이 더 분명하게 구분
- **일관된 인터페이스**: 함수 호출 방식이 더 체계적으로 변경

### AI 사용 방식의 두 가지 패턴
**🔄 대화형 방식**: 여러 번 주고받으며 연속 대화 (대부분의 실습 파일)
**⚡ 일회성 방식**: 한 번만 질문하고 답변받기 ([step_3_1_prompt.py](step_3_1_prompt.py))

모든 준비가 완료되었다면 영어 받아쓰기 앱 실습을 시작해보세요! 🚀
