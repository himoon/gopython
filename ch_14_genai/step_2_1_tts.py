from google.cloud import texttospeech
from google.oauth2 import service_account

from step_1_1 import IN_DIR, OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

path = IN_DIR / "API_KEY.json"  # 서비스 계정 키 파일 경로 입력
cred = service_account.Credentials.from_service_account_file(path)  # 키 불러오기
client = texttospeech.TextToSpeechClient(credentials=cred)  # 클라이언트 객체 생성
client.list_voices()  # TTS 지원 언어 목록


from pathlib import Path

text = IN_DIR / "billboard.txt"  # 텍스트 파일 경로
lang_code = "en-GB"  # 언어 코드
voice = "en-GB-Studio-C"  # 보이스
encoding = texttospeech.AudioEncoding.MP3  # 오디오 인코딩
resp = client.synthesize_speech(  # 음성 생성
    input=texttospeech.SynthesisInput(text=text.read_text(encoding="utf-8")),  # 텍스트 입력
    voice=texttospeech.VoiceSelectionParams(language_code=lang_code, name=voice),  # 언어와 보이스 선택
    audio_config=texttospeech.AudioConfig(audio_encoding=encoding),  # 오디오 인코딩 설정
)
with open(OUT_DIR / f"{Path(__file__).stem}.mp3", "wb") as fp:
    fp.write(resp.audio_content)
