import ollama

from step_1_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_1 import extract_text_img

# 시스템 프롬프트를 불러옵니다.
SYSTEM_PROMPT = (IN_DIR / "system.txt").read_text(encoding="utf-8")

url = "https://www.koreaherald.com/view.php?ud=20240725050618"
text, img_url = extract_text_img(url)  # 기사 원문 및 이미지 URL 추출
msgs = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": text},
]
resp = ollama.chat(
    model="gemma2:9b",
    messages=msgs,
    options=dict(temperature=0.2),  # 온도 옵션 설정
)
msg_llm = dict(resp.get("message", {}))
msg_llm
