gemma = [
    {"role": "user", "content": "네 이름이 뭐야?"},
    {"role": "assistant", "content": "저는 Gemma입니다."},
]
llama = [
    {"role": "user", "content": "네 이름이 뭐야?"},
    {"role": "assistant", "content": "미안하지만, 내 이름은 없어요."},
]
zipped = zip(gemma, llama)
list(zipped)  # zip 객체를 리스트로 변환하기 위해 list() 함수를 사용
