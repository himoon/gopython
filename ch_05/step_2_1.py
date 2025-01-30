import easyocr

from step_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.

path = IN_DIR / "ocr.jpg"
reader = easyocr.Reader(["ko", "en"], verbose=False)
parsed = reader.readtext(path.read_bytes())
parsed
