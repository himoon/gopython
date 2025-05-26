import ollama

resp1 = ollama.chat(
    model="gemma2:9b",
    messages=[{"role": "user", "content": "내 이름은 파이썬이야!"}],
)
dict(resp1["message"])  # dict() 함수를 사용하여 ChatResponse 객체를 딕셔너리로 변환

resp2 = ollama.chat(
    model="gemma2:9b",
    messages=[{"role": "user", "content": "내 이름이 뭐라고 했지?"}],
)
dict(resp2["message"])
