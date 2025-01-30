import pandas as pd

num = list(range(1, 6))  # 1부터 5까지 정수
df = pd.DataFrame(num, columns=["num"])  # 데이터프레임 생성
df["cumsum"] = df["num"].cumsum()  # 'num' 열의 누적합 계산
print(df)
