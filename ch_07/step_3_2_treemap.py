import pandas as pd
import plotly.express as px

df = pd.DataFrame(range(1, 6), columns=["num"])  # 데이터프레임 생성
fig = px.treemap(df, path=["num"], values="num")  # 트리맵 생성
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))  # 이미지 여백 제거
fig.write_image("path_to_img.png", scale=2)  # 파일로 저장
