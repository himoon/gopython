from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from step_1_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_2 import OUT_3_2

img_raw = Image.open(OUT_3_2)

text = "발리, 인도네시아"  # 이미지에 추가할 메시지
font = ImageFont.truetype(IN_DIR / "Pretendard-Bold.ttf", size=100)
left, top, right, bottom = font.getbbox(text)

pad = 20  # 여백
bg_width = pad + right + pad  # 메시지 너비에 여백 추가
bg_height = pad + bottom + pad  # 메시지 높이에 여백 추가

WIDTH, HEIGHT = img_raw.size  # 전체 이미지 사이즈
start_x = WIDTH - bg_width  # 전체 너비에서 메시지 너비 차감
start_y = HEIGHT - bg_height  # 전체 높이에서 메시지 높이 차감

img_bg = Image.new("RGBA", size=img_raw.size)  # 배경 이미지 생성
draw_bg = ImageDraw.Draw(img_bg)  # 배경 이미지를 위한 이미지드로 객체 생성
draw_bg.rectangle(xy=(start_x, start_y, WIDTH, HEIGHT), fill=(0, 0, 0, 200))

img_final = Image.alpha_composite(img_raw.convert("RGBA"), img_bg)  # 이미지 합성
draw_final = ImageDraw.Draw(img_final)  # 최종 이미지를 위한 이미지드로 객체 생성
draw_final.text(
    xy=(start_x + pad, start_y + pad),
    text=text,
    fill=(255, 255, 255),
    font=font,
)

img_final.convert("RGB").save(OUT_DIR / f"{Path(__file__).stem}.jpg")
