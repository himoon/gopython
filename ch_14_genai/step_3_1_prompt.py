from google import genai
from PIL import Image

from step_1_1 import IMG_DIR, IN_DIR  # 이전에 작성한 모듈을 불러옵니다.

GEMINI_KEY = "API_KEY"  # Gemini API 키 입력
img = Image.open(IMG_DIR / "seminyak.jpg")  # Image 객체 생성
prompt = IN_DIR / "p1_desc.txt"  # 이미지 묘사에 대한 시스템 프롬프트
client = genai.Client(api_key=GEMINI_KEY)  # 클라이언트 객체 생성
resp = client.models.generate_content(
    model="gemini-2.5-flash",  # Gemini 모델 입력
    config=genai.types.GenerateContentConfig(system_instruction=prompt.read_text(encoding="utf-8")),
    contents=[img, "Describe this image"],
)  # 이미지 및 프롬프트 전송
print(resp.text)  # This image captures a warm and inviting atmosphere, ...
