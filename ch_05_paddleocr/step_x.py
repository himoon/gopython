from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from step_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import read_text

OUT_X = OUT_DIR / f"{Path(__file__).stem}.jpg"
PROB = 0.75  # 인식률 기준값


def read_text_and_draw_line(path: Path):
    parsed = read_text(path)  # 문자 인식 결과 저장
    img = Image.open(path)  # 이미지 객체 생성
    draw = ImageDraw.Draw(img, "RGBA")  # 이미지드로 객체 생성
    font = ImageFont.truetype(IN_DIR / "Pretendard-Bold.ttf", size=50)
    for row in parsed:
        bbox, text, prob = row  # 문자 인식 결과를 좌표, 문자, 인식률로 각각 분리
        box = [(x, y) for x, y in bbox]  # 리스트를 튜플로 변환
        draw.polygon(
            box,
            outline=(255, 0, 0) if prob >= PROB else (0, 255, 0),
            width=10,
        )

        start_x, start_y = box[0]  # 문자열을 그릴 시작점
        left, top, right, bottom = font.getbbox(text)  # text 문자열의 바운딩 박스
        text_width = right  # 문자열 너비
        text_height = bottom  # 문자열 높이

        pad = 10  # 여백
        bg_width = pad + text_width + pad  # 배경 너비
        bg_height = pad + text_height + pad  # 배경 높이

        draw.rectangle(  # 배경 이미지 그리기
            xy=(
                start_x,
                start_y,
                start_x + bg_width,  # 시작점부터 배경 너비만큼
                start_y + bg_height,  # 시작점부터 배경 높이만큼
            ),
            fill=(0, 0, 0, 200),  # 검정색 (0, 0, 0)에 불투명도 적용
        )

        draw.text(  # 문자열 그리기
            xy=(
                start_x + pad,  # 시작점에서 여백만큼 떨어져서
                start_y + pad,
            ),
            text=text,
            fill=(255, 255, 255),
            font=font,
        )
    img.save(OUT_X)


if __name__ == "__main__":
    path = IN_DIR / "ocr.jpg"
    read_text_and_draw_line(path)
