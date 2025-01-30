from datetime import datetime

dt = datetime.strptime("20250103", "%Y%m%d")  # 문자열을 datetime 객체로 변환
print(dt.strftime("%Y.%m.%d"))  # datetime 객체를 문자열로 변환 -> "2025.01.03"

import pandas as pd

dt = [f"202501{day:02}" for day in range(1, 3)]  # ['20250101', '20250102']
df_date = pd.DataFrame(dt, columns=["date_string"])  # 데이터프레임 생성
df_date["date"] = pd.to_datetime(df_date["date_string"], format="%Y%m%d")  # 열의 형식 변환
df_date.info()  # 데이터프레임 정보 출력
