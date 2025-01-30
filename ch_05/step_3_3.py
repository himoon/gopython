from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from step_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_2 import read_text_translated

OUT_3_3 = OUT_DIR / f"{Path(__file__).stem}.jpg"
PROB = 0.75


def read_text_and_fill_area(path: Path):
    parsed = read_text_translated(path)  # 문자 인식 및 번역 결과 저장
    img = Image.open(path)
    draw = ImageDraw.Draw(img, "RGBA")  # 알파 채널 사용 가능
    font = ImageFont.truetype(IN_DIR / "Pretendard-Bold.ttf", size=60)
    for row in parsed:
        bbox, text, prob = row
        box = [(x, y) for x, y in bbox]
        draw.polygon(
            box,
            fill=(255, 0, 0, 100) if prob >= PROB else (0, 255, 0, 100),
        )
        draw.text(xy=box[0], text=text, fill=(255, 255, 255), font=font)
    img.save(OUT_3_3)


if __name__ == "__main__":
    path = IN_DIR / "ocr.jpg"
    read_text_and_fill_area(path)
