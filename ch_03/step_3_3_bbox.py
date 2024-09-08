from PIL import ImageFont

from step_1_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.

text = "Hello, World!"
font = ImageFont.truetype(IN_DIR / "Pretendard-Bold.ttf", size=100)
bbox = font.getbbox(text)  # 바운딩 박스 생성
print(f"{bbox=}")  # bbox=(0, 25, 598, 117)
