import json
from pathlib import Path

import pandas as pd

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_3 import OUT_1_3


def clean_white_space(text: str) -> str:
    return " ".join(text.split())  # 공백 문자 정제


def table_to_dataframe(header: list, body: list) -> pd.DataFrame:
    df_raw = pd.DataFrame(body, columns=header)  # DataFrame 객체 생성
    df_raw = df_raw.dropna(how="any")  # 하나의 열이라도 데이터가 없으면 행 삭제
    df_raw = df_raw.iloc[:, :-1]  # 마지막 열 삭제
    for col in df_raw.columns:
        df_raw[col] = df_raw[col].apply(clean_white_space)  # 열별로 공백 문자 정제
    return df_raw


if __name__ == "__main__":
    parsed = json.loads(OUT_1_3.read_text(encoding="utf8"))  # JSON 파일 불러오기
    header, body = parsed["header"], parsed["body"]
    df_raw = table_to_dataframe(header, body)
    df_raw.to_csv(OUT_DIR / f"{Path(__file__).stem}.csv", index=False)  # CSV로 저장
