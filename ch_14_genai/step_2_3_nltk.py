import nltk

sent = "정글 숲을 지나서 가자. 엉금엉금 기어서 가자."  # 분석할 텍스트
nltk.download(["punkt", "punkt_tab"], quiet=True)  # punkt 분석기 다운로드
print(nltk.tokenize.sent_tokenize(sent))  # 문장 단위로 분리
