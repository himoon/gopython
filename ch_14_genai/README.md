# 14장: Gemini AI로 영어 받아쓰기 앱 만들기 🚀

안녕하세요! 이번 장에서는 Google의 최신 AI 모델인 **Gemini**를 사용해서 재미있는 영어 받아쓰기 앱을 만들어 보겠습니다. 

사용자가 이미지를 업로드하면, AI가 이미지를 분석하고 영어로 설명한 다음, 그것을 바탕으로 퀴즈를 내주는 똑똑한 앱이에요! 

## ⚠️ 중요한 변화: 새로운 패키지로 업그레이드!

최근 Google에서 Gemini API 패키지 이름을 바꿨어요:
- **예전 이름**: `google-generativeai` 
- **새로운 이름**: `google-genai` 

이 폴더(`ch_14_genai`)에 있는 코드들은 모두 **새로운 패키지**를 사용해서 작성되었습니다. 혹시 `ch_14` 폴더의 예전 코드와 비교하면서 공부하고 싶다면, 이 문서를 참고해 주세요!

## 1단계: 필요한 도구들 설치하기 🛠️

먼저 우리 프로젝트에 필요한 파이썬 라이브러리들을 설치해야 해요. 터미널을 열고 아래 명령어를 입력해 주세요:

```bash
pip install -U google-cloud-texttospeech google-genai ipywidgets nltk streamlit
```

## 2단계: Gemini AI와 대화하는 방법 익히기 💬

### 기본적인 사용법 비교

새로운 패키지에서는 AI와 대화하는 방식이 조금 달라졌어요. 아래 표를 보면서 차이점을 이해해 보세요:

| 단계 | 예전 방식 (`google-generativeai`) | 새로운 방식 (`google-genai`) |
|------|-----------------------------------|------------------------------|
| **1. 패키지 가져오기** | `import google.generativeai as genai` | `from google import genai` |
| **2. AI 준비하기** | `genai.configure(api_key="키")`<br>`model = genai.GenerativeModel("모델명")` | `client = genai.Client(api_key="키")` |
| **3. 대화 시작하기** | `chat = model.start_chat()` | `chat = client.chats.create(model="모델명")` |
| **4. 대화 기록 보기** | `print(chat.history)` | `print(chat.get_history())` |

### 무엇이 좋아졌나요?
- **더 간단해졌어요**: `Client` 객체 하나로 모든 걸 관리해요
- **더 명확해졌어요**: 각 기능의 역할이 더 분명해졌어요
- **더 체계적이에요**: 코드 구조가 깔끔해졌어요

## 3단계: 웹 애플리케이션 만들기 🌐

이제 Streamlit을 사용해서 사용자가 직접 사용할 수 있는 웹 화면을 만들어 보겠습니다.

### `step_1_2.py` - AI 챗봇 기능 만들기

**예전 방식**에서는 이렇게 했어요:
```python
# 1단계: 모델 객체를 만들고
model = get_model()
# 2단계: 대화를 시작했어요
chat = model.start_chat()
```

**새로운 방식**에서는 한 번에 해결돼요:
```python
# 한 번에 대화 준비 완료!
chat = get_chat()
```

이제 `get_model` 함수가 `get_chat` 함수로 바뀌었어요. 더 직관적이죠?

### `step_1_3.py` - 대화 기록 관리하기

**대화 기록을 확인할 때:**
- **예전**: `chat.history` (속성으로 바로 접근)
- **새로움**: `chat.get_history()` (함수를 호출해서 가져오기)

**왜 바뀌었나요?** 함수로 바뀌면서 더 안전하고 일관된 방식으로 데이터를 가져올 수 있게 되었어요!

## 4단계: AI 사용 방식의 두 가지 패턴 🎯

Gemini AI를 사용하는 방법에는 크게 두 가지가 있어요:

### 🔄 대화형 방식 (`step_3_1.py`)
**언제 사용하나요?** 여러 번 주고받으며 대화해야 할 때
- 퀴즈를 내고 답변을 받고
- 피드백을 주고받고
- 연속된 질문을 할 때

**어떻게 작동하나요?**
```python
# 각각의 목적에 맞는 대화방을 만들어요
quiz_chat = get_chat(sys_prompt="퀴즈를 내는 AI")
feedback_chat = get_chat(sys_prompt="피드백을 주는 AI")

# 계속 대화할 수 있어요
quiz_response = quiz_chat.send_message("퀴즈 내주세요")
feedback_response = feedback_chat.send_message("이 답변 어때요?")
```

### ⚡ 일회성 방식 (`step_3_1_prompt.py`)
**언제 사용하나요?** 한 번만 질문하고 답변받으면 끝날 때
- 이미지 설명하기
- 번역하기
- 간단한 질문 답변

**어떻게 작동하나요?**
```python
# 클라이언트를 만들고
client = genai.Client(api_key="키")
# 바로 질문해요
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[이미지, "이 이미지를 설명해주세요"]
)
```

## 📚 학습 팁

1. **차근차근 따라해 보세요**: 각 파일을 하나씩 실행하면서 어떻게 작동하는지 확인해 보세요
2. **예전 코드와 비교해 보세요**: `ch_14` 폴더의 코드와 비교하면서 무엇이 달라졌는지 찾아보세요
3. **API 키를 꼭 설정하세요**: `"API_KEY"` 부분을 본인의 실제 Gemini API 키로 바꿔주세요
4. **에러가 나면 당황하지 마세요**: 패키지 이름이나 함수 이름을 다시 한번 확인해 보세요

---

이제 새로운 `google-genai` 패키지로 더 쉽고 강력한 AI 앱을 만들 수 있게 되었어요! 

궁금한 점이 있다면 각 파일의 코드를 직접 실행해 보면서 어떻게 작동하는지 확인해 보세요. 실습이 최고의 학습 방법이에요! 💪