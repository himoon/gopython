from step_1_1 import IMG_DIR, IN_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_2 import get_model

prompt = IN_DIR / "p1_desc.txt"  # 이미지 묘사에 대한 시스템 프롬프트
model = get_model(sys_prompt=prompt.read_text(encoding="utf8"))  # 모델 객체 생성

from PIL import Image

img = Image.open(IMG_DIR / "seminyak.jpg")  # Image 객체 생성
resp = model.generate_content([img, "Describe this image"])  # 이미지 및 프롬프트 전송
print(resp.text)  # This image depicts a sophisticated business meeting setting, ...
