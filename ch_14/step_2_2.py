from pathlib import Path

from google.cloud import texttospeech

from step_1_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_1 import tts_client


def synth_speech(text: str, voice: str, audio_encoding: str | None = None) -> bytes:
    lang_code = "-".join(voice.split("-")[:2])  # 언어 코드(예: 'en-US', 'ko-KO')
    MP3, WAV = texttospeech.AudioEncoding.MP3, texttospeech.AudioEncoding.LINEAR16
    audio_type = MP3 if audio_encoding == "mp3" else WAV  # MP3 또는 WAV

    client = tts_client()  # TextToSpeechClient 객체 생성
    resp = client.synthesize_speech(  # 텍스트를 음성으로 변환
        input=texttospeech.SynthesisInput(text=text),
        voice=texttospeech.VoiceSelectionParams(language_code=lang_code, name=voice),
        audio_config=texttospeech.AudioConfig(audio_encoding=audio_type),
    )
    return resp.audio_content  # 음성을 바이트(bytes) 형식으로 반환


if __name__ == "__main__":
    text_path = IN_DIR / "billboard.txt"  # 'img/billboard.jpg'를 묘사한 텍스트 파일 경로
    text = text_path.read_text(encoding="utf-8")  # 텍스트 파일에서 텍스트 불러오기
    audio = synth_speech(text, "en-GB-Studio-C", "mp3")  # 텍스트를 음성으로 변환
    with open(OUT_DIR / f"{Path(__file__).stem}.mp3", "wb") as fp:
        fp.write(audio)  # 음성 파일로 저장
