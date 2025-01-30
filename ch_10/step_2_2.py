import matplotlib.pyplot as plt
import pandas as pd

from step_1_1 import IMG_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_1 import OUT_2_1


def indicators_to_png():
    with pd.ExcelFile(OUT_2_1) as xlsx:  # ExcelFile 객체 생성
        for sheet_name in xlsx.sheet_names:
            df_raw = pd.read_excel(xlsx, sheet_name=sheet_name)  # 데이터프레임 생성
            df_raw = df_raw.tail(24)  # 마지막 24개월 데이터 추출

            x_value = df_raw.index  # 가로축 데이터
            y_value = df_raw["DATA_VALUE"]  # 세로축 데이터
            y_min = y_value.min()  # 세로축 데이터 최솟값
            change = y_value.iloc[-1] - y_value.iloc[0]  # 세로축 데이터 변화량
            color = "red" if change > 0 else "blue" if change < 0 else "black"

            fig, ax = plt.subplots(figsize=(9, 3), dpi=100)  # 이미지 크기 및 해상도 지정
            ax.plot(x_value, y_value, color=color, linewidth=3)  # 선 그래프
            ax.fill_between(x_value, y_value, y_min, color=color, alpha=0.10)  # 채우기
            ax.set_axis_off()  # 축 제거
            fig.set_layout_engine("tight")  # 이미지 여백 제거
            fig.savefig(IMG_DIR / f"{sheet_name}.png")  # PNG 파일로 저장


if __name__ == "__main__":
    indicators_to_png()  # 주요 금리지표 데이터 시각화
