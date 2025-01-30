from qrcode.constants import ERROR_CORRECT_H
from qrcode.image.styledpil import StyledPilImage
from qrcode.main import QRCode

from step_1_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import OUT_2_2_VCF

with open(OUT_2_2_VCF, encoding="utf-8") as fp:
    vcf = fp.read()

qr = QRCode(error_correction=ERROR_CORRECT_H)
qr.add_data(vcf)
img = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path=IN_DIR / "phone.png",
)
img
