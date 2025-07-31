num_int, num_float = 12_345, 0.12345
print(f"{num_int:,}")  # 12,345
print(f"{num_float:.4f}")  # 0.1235

text = "퀴즈: {}, 정답: {}"  # 서식을 적용할 문자열 템플릿
print(text)  # 퀴즈: {}, 정답: {}

quiz, answ = "바나나가 웃으면?", "바나나킥"
print(text.format(quiz, answ))  # 퀴즈: 바나나가 웃으면?, 정답: 바나나킥
