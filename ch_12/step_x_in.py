print("한식" in "음식점>한식")  # True

import pandas as pd

df = pd.DataFrame(["음식점>한식", "음식점>일식", "음식점>양식"], columns=["category"])
print(df["category"].str.contains("한식|일식").tolist())  # [True, True, False]
