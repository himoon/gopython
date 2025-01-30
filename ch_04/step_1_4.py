from pathlib import Path

import qrcode

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

img_hello = qrcode.make("헬로, QR 코드!")
img_hello.save(OUT_DIR / f"{Path(__file__).stem}_hello.png")

img_youtube = qrcode.make("https://www.youtube.com/")
img_youtube.save(OUT_DIR / f"{Path(__file__).stem}_youtube.png")
