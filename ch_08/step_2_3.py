import time
from pathlib import Path

import pandas as pd
from tqdm import tqdm  # 진행 표시줄 관리를 위한 tqdm 클래스

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_2 import query_naver_shop
from step_2_2 import OUT_2_2

OUT_2_3 = OUT_DIR / f"{Path(__file__).stem}.csv"


def shop_cnt_to_csv():
    df_raw = pd.read_csv(OUT_2_2)  # CSV 파일에서 데이터프레임 생성
    kwd_list = df_raw["키워드"].to_list()  # '키워드' 열을 리스트 타입으로 변환
    item_cnt = []  # 키워드별 네이버 쇼핑 상품 개수
    with tqdm(total=len(kwd_list)) as pbar:  # tqdm 객체 생성
        for kwd in kwd_list:
            resp = query_naver_shop(query=kwd)  # 네이버 쇼핑 상품 검색
            total = resp.get("total", 0)  # 전체 등록 상품 개수
            item_cnt.append({"키워드": kwd, "상품수": total})
            time.sleep(0.5)  # 0.5초간 일시 정지
            pbar.set_description(kwd)  # 진행 표시줄 메시지 수정
            pbar.update()  # 진행 표시줄 업데이트

    df_raw = pd.DataFrame(item_cnt)  # 데이터프레임 생성
    df_raw.to_csv(OUT_2_3, index=False)  # CSV 파일로 저장


if __name__ == "__main__":
    shop_cnt_to_csv()  # 키워드별 상품 개수 수집
