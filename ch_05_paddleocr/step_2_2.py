from pathlib import Path

from paddleocr import PaddleOCR

from step_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.


def read_text(path: Path) -> list:
    ocr = PaddleOCR(
        text_detection_model_name="PP-OCRv5_mobile_det",  # 텍스트 감지 모델을 설정합니다.
        text_recognition_model_name="PP-OCRv5_mobile_rec",  # 텍스트 인식 모델을 설정합니다.
        device="cpu",  # CPU를 사용합니다.
        use_doc_unwarping=False,  # 문서 왜곡 보정을 사용하지 않습니다.
    )

    result: list[dict] = ocr.predict(str(path))  # 이미지에서 텍스트를 추출합니다.
    parsed = result[0]  # 첫 번째 결과를 가져옵니다.

    # 💡 easyocr 패키지와 같은 형식의 결괏값을 얻기 위해 (인식된 문자의 좌표, 인식된 문자, 인식률)을 묶어서 반환합니다.
    return list(
        zip(
            [arr.tolist() for arr in parsed["rec_polys"]],  # 인식된 문자의 좌표
            parsed["rec_texts"],  # 인식된 문자
            parsed["rec_scores"],  # 인식률
        )
    )


if __name__ == "__main__":
    path = IN_DIR / "ocr.jpg"
    print(read_text(path))
