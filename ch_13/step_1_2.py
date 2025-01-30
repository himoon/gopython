import ollama

resp1 = ollama.chat(
    model="gemma2:9b",
    messages=[{"role": "user", "content": "내 이름은 파이썬이야!"}],
)
resp1["message"]

resp2 = ollama.chat(
    model="gemma2:9b",
    messages=[{"role": "user", "content": "내 이름이 뭐라고 했지?"}],
)
resp2["message"]
