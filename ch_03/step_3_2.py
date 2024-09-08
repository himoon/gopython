from pathlib import Path

from PIL import Image, ImageOps

from step_1_1 import IMG_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

OUT_3_2 = OUT_DIR / f"{Path(__file__).stem}.jpg"

if __name__ == "__main__":
    ROWS, COLS = 5, 8  # 5행 8열
    W_IMG, H_IMG = 500, 500  # 개별 이미지 크기
    W_BG, H_BG = COLS * W_IMG, ROWS * H_IMG  # 배경 이미지 크기
    start_x, start_y = 0, 0  # 개별 이미지 시작점 좌표

    img_bg = Image.new(mode="RGB", size=(W_BG, H_BG))
    path_sorted = sorted(Path(IMG_DIR).glob("*.jpg"))
    for path in path_sorted:
        img = Image.open(path)
        img_fit = ImageOps.fit(img, (W_IMG, H_IMG))
        img_bg.paste(img_fit, box=(start_x, start_y))

        start_x += W_IMG
        if start_x >= W_BG:
            start_x = 0
            start_y += H_IMG

    img_bg.save(OUT_3_2)
