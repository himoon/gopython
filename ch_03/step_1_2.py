from PIL import Image

from step_1_1 import IMG_DIR  # 이전에 작성한 모듈을 불러옵니다.

img = Image.open(IMG_DIR / "img_001.jpg")
img

from PIL import ImageDraw

draw = ImageDraw.Draw(img)
draw.text(
    xy=(10, 100),
    text="Hello World!",
    fill=(255, 255, 255),
    font_size=100,
)
img
