from pathlib import Path

import easyocr

from step_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.


def read_text(path: Path) -> list:
    reader = easyocr.Reader(["ko", "en"], verbose=False)
    return reader.readtext(path.read_bytes())


if __name__ == "__main__":
    path = IN_DIR / "ocr.jpg"
    print(read_text(path))
