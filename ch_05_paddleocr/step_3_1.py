import deepl

DEEPL_KEY = "API_KEY"  # 복사한 API 키를 붙여 넣으세요.
DEEPL_KEY = "dddd7d6f-f59b-46e5-beaa-32964f606f6b:fx"  # 복사한 API 키를 붙여 넣으세요.
tran = deepl.Translator(DEEPL_KEY)
resp = tran.translate_text("Hello, World!", source_lang="EN", target_lang="KO")
resp.text
