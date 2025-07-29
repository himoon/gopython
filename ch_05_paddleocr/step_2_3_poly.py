from PIL import Image, ImageDraw

img = Image.new("RGB", size=(100, 100), color=(238, 238, 238))  # Image 객체 생성
draw = ImageDraw.Draw(img, "RGB")  # ImageDraw 객체 생성
draw.polygon(
    xy=[(10, 10), (90, 10), (90, 90), (10, 90)],  # 좌표
    outline=(0, 0, 0),  # 외곽선 색
    width=10,  # 외곽선 두께
)
img
