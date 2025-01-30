import pandas as pd

english = ["apple", "orange", "lemon"]
korean = ["사과", "오렌지", "레몬"]
df_raw = pd.DataFrame(dict(korean=korean), index=english)  # 데이터프레임 생성
for idx, sr in df_raw.iterrows():  # 행별로 반복 처리
    value = sr["korean"]  # 시리즈에서 "korean" 열 추출
    print(f"{idx=}, {value=}")
