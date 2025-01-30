import ollama

msgs = [{"role": "user", "content": "내 이름은 파이썬이야!"}]
resp1 = ollama.chat(model="gemma2:9b", messages=msgs)
msgs.append(resp1["message"])

msgs.append({"role": "user", "content": "내 이름이 뭐라고 했지?"})
resp2 = ollama.chat(model="gemma2:9b", messages=msgs)
msgs.append(resp2["message"])

msgs
