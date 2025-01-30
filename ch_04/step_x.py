from pathlib import Path

from PIL import Image

from step_1_1 import IN_DIR, OUT_DIR
from step_3_2 import OUT_3_2

# RATIO, OFFSET_X, OFFSET_Y 값을 변경하여 어떤 결과가 나오는지 확인해 보세요.
RATIO = 0.2  # 고양이 이미지 크기의 축소 비율
OFFSET_X, OFFSET_Y = 25, 48  # 이미지 합성 시 고양이 위치 변경을 위한 변수

# QR 코드 이미지
qr = Image.open(OUT_3_2).convert("RGBA")
width_qr, height_qr = qr.size

# QR 코드에 삽입할 고양이 이미지
icon = Image.open(IN_DIR / "cat.png")  # 고양이 아이콘
width_icon = int(icon.size[0] * RATIO)  # 고양이 가로 크기
height_icon = int(icon.size[1] * RATIO)  # 고양이 세로 크기
icon_resized = icon.resize((width_icon, height_icon))  # 고양이 크기 조정

# 배경 이미지
width_bg = width_qr + width_icon - OFFSET_X
height_bg = max(height_qr, height_icon)
img_bg = Image.new("RGBA", size=(width_bg, height_bg), color="#FFFFFF")

# 이미지 합성
icon_x = width_bg - width_icon - OFFSET_X  # 아이콘 x 좌표
icon_y = height_bg - height_icon - OFFSET_Y  # 아이콘 y 좌표
img_bg.paste(qr, box=(0, 0))
img_bg.paste(icon_resized, box=(icon_x, icon_y), mask=icon_resized)
img_bg.save(OUT_DIR / f"{Path(__file__).stem}.png")
