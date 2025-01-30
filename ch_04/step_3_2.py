from pathlib import Path

from PIL import Image

from step_1_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import OUT_2_2_PNG

OUT_3_2 = OUT_DIR / f"{Path(__file__).stem}.png"

if __name__ == "__main__":
    qr = Image.open(OUT_2_2_PNG).convert("RGBA")  # QR 코드
    width_qr, height_qr = qr.size  # QR 코드의 (가로, 세로) 크기

    icon = Image.open(IN_DIR / "phone.png")  # 전화 아이콘
    width_icon = int(width_qr * 0.2)  # 아이콘 가로 크기
    height_icon = int(height_qr * 0.2)  # 아이콘 세로 크기
    icon_resized = icon.resize((width_icon, height_icon))  # 아이콘 크기 조정

    pad = 50  # 여백
    icon_x = width_qr - width_icon - pad  # 아이콘 x 좌표
    icon_y = height_qr - height_icon - pad  # 아이콘 y 좌표

    qr.paste(icon_resized, box=(icon_x, icon_y), mask=icon_resized)  # 아이콘 삽입
    qr.save(OUT_3_2)  # 파일로 저장
