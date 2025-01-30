from pathlib import Path

import nltk

from step_1_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import synth_speech


def tokenize_sent(text: str) -> list[str]:
    nltk.download(["punkt", "punkt_tab"], quiet=True)  # punkt 분석기 다운로드
    return nltk.tokenize.sent_tokenize(text)  # 텍스트를 문장별로 분리하여 반환


if __name__ == "__main__":
    text_path = IN_DIR / "billboard.txt"  # 'img/billboard.jpg'를 묘사한 텍스트 파일 경로
    text = text_path.read_text(encoding="utf-8")  # 텍스트 파일에서 텍스트 불러오기
    sents = tokenize_sent(text)  # 텍스트를 문장별로 분리
    for idx, sent in enumerate(sents):
        audio = synth_speech(sent, "en-AU-Neural2-B", "mp3")  # 텍스트를 음성으로 변환
        with open(OUT_DIR / f"{Path(__file__).stem}_{idx}.mp3", "wb") as fp:
            fp.write(audio)  # 음성 파일로 저장
