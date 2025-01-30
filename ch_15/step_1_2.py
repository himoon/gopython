def init_board(n_rows: int, n_cols: int) -> list[list[int]]:
    nums = list(range(1, n_rows * n_cols)) + [0]  # [1, 2, ..., n_rows*n_cols-1, 0]
    return [nums[idx : idx + n_cols] for idx in range(0, n_rows * n_cols, n_cols)]


def draw_board(board: list[list[int]]):
    for row in board:
        print(" ".join("  " if num == 0 else f"{num:>2}" for num in row))
    print()  # 빈 줄 출력


if __name__ == "__main__":
    n_rows = n_cols = 3  # 3행 3열 보드
    board = init_board(n_rows, n_cols)  # 보드 초기화
    draw_board(board)  # 보드 출력
