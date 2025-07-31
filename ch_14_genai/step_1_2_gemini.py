from google import genai

GEMINI_KEY = "API_KEY"  # Gemini API 키 입력
GEMINI_MODEL = "gemini-2.5-flash"  # Gemini 모델 입력
client = genai.Client(api_key=GEMINI_KEY)  # 클라이언트 객체 생성
chat = client.chats.create(model=GEMINI_MODEL)  # 챗 객체 생성
resp = chat.send_message("Hello, Gemini!")  # 사용자 메시지 전달
print(resp.text)  # Hello! What can I do for you today?

resp = chat.send_message("내 이름은 파이썬이야!")
print(resp.text)  # 안녕하세요, 파이썬! 만나서 반가워요! 무엇을 도와드릴까요?
resp = chat.send_message("내 이름을 기억하고 있어?")
print(resp.text)  # 네, 파이썬! 당신의 이름을 기억하고 있어요. 무엇을 도와드릴까요?

print(chat.get_history())  # 대화 목록

print(list(client.models.list()))  # 전체 Gemini 모델 목록