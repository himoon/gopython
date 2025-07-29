from pathlib import Path

import deepl

from step_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import read_text


def read_text_translated(path: Path) -> list:
    text_list = read_text(path)  # 5-2절의 문자 인식 함수

    DEEPL_KEY = "API_KEY"  # DEEPL API KEY
    DEEPL_KEY = "dddd7d6f-f59b-46e5-beaa-32964f606f6b:fx"  # 복사한 API 키를 붙여 넣으세요.
    tran = deepl.Translator(DEEPL_KEY)
    result = []
    for coords, text, prob in text_list:
        resp = tran.translate_text(text, target_lang="KO")
        result.append((coords, resp.text, prob))
    return result


if __name__ == "__main__":
    path = IN_DIR / "ocr.jpg"
    print(read_text_translated(path))
