from PIL import Image

from step_1_1 import IMG_DIR  # 이전에 작성한 모듈을 불러옵니다.

SIZE = (500, 500)
img = Image.open(IMG_DIR / "img_001.jpg")
img_resize = img.resize(SIZE)
img_black = Image.new(mode="RGBA", size=SIZE, color=(0, 0, 0, 153))

img_comp = Image.alpha_composite(img_resize.convert("RGBA"), img_black)
img_comp
