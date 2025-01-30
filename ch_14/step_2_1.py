from google.cloud import texttospeech  # 구글 클라우드 TTS API
from google.oauth2 import service_account  # 구글 클라우드 계정 인증

from step_1_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.


def tts_client() -> texttospeech.TextToSpeechClient:
    path = IN_DIR / "API_KEY.json"  # 서비스 계정 키 파일 경로 입력
    cred = service_account.Credentials.from_service_account_file(path)  # 자격 증명 객체
    return texttospeech.TextToSpeechClient(credentials=cred)  # 클라이언트 객체 반환
