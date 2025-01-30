from PIL import Image, ImageOps

from step_1_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

SIZE = (500, 500)
img = Image.open(IN_DIR / "breaking.jpg")
img.resize(SIZE).save(OUT_DIR / "1_resize.jpg")
ImageOps.contain(img, SIZE).save(OUT_DIR / "2_contain.jpg")
ImageOps.cover(img, SIZE).save(OUT_DIR / "3_cover.jpg")
ImageOps.fit(img, SIZE).save(OUT_DIR / "4_fit.jpg")
ImageOps.pad(img, SIZE, color=(0, 0, 0)).save(OUT_DIR / "5_pad.jpg")
