import ollama

msgs = [
    {"role": "system", "content": "입력된 텍스트를 한국어로 번역해줘."},  # 시스템 프롬프트
    {"role": "user", "content": "Hello, World!"},  # 사용자 메시지
]
resp = ollama.chat(model="gemma2:9b", messages=msgs)
print(resp["message"]["content"])  # 안녕 세상! 👋
