from paddleocr import PaddleOCR  # PaddleOCR 패키지를 불러옵니다.

from step_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.

path = IN_DIR / "ocr.jpg"

ocr = PaddleOCR(
    text_detection_model_name="PP-OCRv5_mobile_det",  # 텍스트 감지 모델을 설정합니다.
    text_recognition_model_name="PP-OCRv5_mobile_rec",  # 텍스트 인식 모델을 설정합니다.
    device="cpu",  # CPU를 사용합니다.
    use_doc_unwarping=False,  # 문서 왜곡 보정을 사용하지 않습니다.
)

result: list[dict] = ocr.predict(str(path))  # 이미지에서 텍스트를 추출합니다.
parsed = result[0]  # 첫 번째 결과를 가져옵니다.
print(parsed["rec_texts"])  # ['Being', 'vegetarian', 'a', 'is a big', 'missed', 'steak']
