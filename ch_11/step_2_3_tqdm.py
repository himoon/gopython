from tqdm import tqdm

data = list(range(1000, 0, -1))  # 1000부터 1까지 정수
with tqdm(total=len(data)) as pbar:  # 진행 표시줄 생성
    for num in data:
        pbar.set_description(f"숫자 카운트 {num}")  # 진행 표시줄 메시지
        pbar.update()  # 진행 표시줄 처리 횟수 업데이트
