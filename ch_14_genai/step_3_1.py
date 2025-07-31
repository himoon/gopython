from google.genai import types
from PIL import Image, ImageFile

from step_1_1 import IMG_DIR, IN_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_2 import get_client
from step_2_3 import tokenize_sent


def generate_quiz(img: ImageFile.ImageFile) -> tuple[list, list]:
    client = get_client()  # 클라이언트 객체 생성

    prompt_desc = IN_DIR / "p1_desc.txt"  # 이미지 묘사 시스템 프롬프트
    resp_desc = client.models.generate_content(
        model="gemini-2.5-flash",  # Gemini 모델 입력
        config=types.GenerateContentConfig(system_instruction=prompt_desc.read_text(encoding="utf-8")),
        contents=[img, "Describe this image"],
    )  # 이미지 묘사 문장 생성

    prompt_quiz = IN_DIR / "p2_quiz.txt"  # 퀴즈 생성 시스템 프롬프트
    resp_quiz = client.models.generate_content(
        model="gemini-2.5-flash",  # Gemini 모델 입력
        config=types.GenerateContentConfig(system_instruction=prompt_quiz.read_text(encoding="utf-8")),
        contents=[resp_desc.text],
    )  # 퀴즈 생성
    return tokenize_sent(resp_quiz.text), tokenize_sent(resp_desc.text)


def generate_feedback(user_input: str, answ: str) -> str:
    client = get_client()  # 클라이언트 객체 생성

    prompt_feedback = IN_DIR / "p3_feedback.txt"  # 피드백 생성 프롬프트 템플릿
    text = prompt_feedback.read_text(encoding="utf-8")  # 템플릿 불러오기
    prompt = text.format(user_input, answ)  # 중괄호 {}를 사용자 입력과 정답으로 대체
    resp_feedback = client.models.generate_content(
        model="gemini-2.5-flash",  # Gemini 모델 입력
        contents=[prompt],
    )  # 피드백 생성
    return resp_feedback.text


if __name__ == "__main__":
    img = Image.open(IMG_DIR / "billboard.jpg")
    quiz, answ = generate_quiz(img)
    print(f"quiz: {quiz[0]}")  # quiz: This _____ advertises...
    print(f"answ: {answ[0]}")  # answ: This billboard advertises...
    resp = generate_feedback(
        "this image showcase a bilboard advertise",  # 사용자 입력 예시
        "This image showcases a billboard advertising",  # 올바른 정답 예시
    )
    print(resp)
