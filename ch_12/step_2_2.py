from pathlib import Path

import pandas as pd
from tqdm import tqdm

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_5 import OUT_1_5
from step_2_1 import fetch_naver_local

OUT_2_2 = OUT_DIR / f"{Path(__file__).stem}.csv"


def naver_local_to_csv():
    df_raw = pd.read_csv(OUT_1_5, encoding="utf-8")  # CSV 파일 불러오기
    addr_list = []  # 이 변수에 검색 결과를 저장
    nrows, _ = df_raw.shape  # 데이터프레임의 행 개수
    with tqdm(total=nrows) as pbar:  # 진행 표시줄 생성
        for idx, sr in df_raw.iterrows():  # 행별로 반복 처리
            name, category = sr["name"], sr["category"]  # 업체명, 카테고리 추출
            resp = fetch_naver_local(name, category)  # 네이버 지역 서비스 검색
            addr_list.append(resp)  # 검색 결과 저장

            msg = f"[{idx+1:5}][{name:10}]"  # 진행 표시줄 메시지
            pbar.set_description(msg)  # 진행 표시줄 메시지 업데이트
            pbar.update()  # 진행 표시줄 처리 횟수 업데이트

    df_addr = pd.DataFrame(addr_list)  # 데이터프레임 생성
    df_addr.to_csv(OUT_2_2, index=False, encoding="utf-8")  # CSV로 저장


if __name__ == "__main__":
    naver_local_to_csv()  # 네이버 지역 서비스 검색 결과를 CSV로 저장
