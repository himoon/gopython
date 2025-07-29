from pathlib import Path

from PIL import Image, ImageDraw

from step_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import read_text

OUT_2_3 = OUT_DIR / f"{Path(__file__).stem}.jpg"
PROB = 0.75  # 인식률 기준값


def read_text_and_draw_line(path: Path):
    parsed = read_text(path)  # 문자 인식 결과 저장
    img = Image.open(path)  # 이미지 객체 생성
    draw = ImageDraw.Draw(img, "RGB")  # 이미지드로 객체 생성
    for row in parsed:
        bbox, text, prob = row  # 문자 인식 결과를 좌표, 문자, 인식률로 각각 분리
        box = [(x, y) for x, y in bbox]  # 리스트를 튜플로 변환
        draw.polygon(
            box,
            outline=(255, 0, 0) if prob >= PROB else (0, 255, 0),
            width=10,
        )
    img.save(OUT_2_3)


if __name__ == "__main__":
    path = IN_DIR / "ocr.jpg"
    read_text_and_draw_line(path)
