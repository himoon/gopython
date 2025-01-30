import os
import random

from readchar import key, readkey  # 키보드 입력 처리

from step_1_2 import draw_board, init_board  # 이전에 작성한 모듈을 불러옵니다.
from step_2_1 import move_zero_to


def is_board_solved(board: list[list[int]]) -> bool:
    n_rows = len(board)  # 행 개수
    n_cols = len(board[0])  # 열 개수
    return board == init_board(n_rows, n_cols)


def clear_terminal_then_draw_board(board: list[list[int]]):
    os.system("cls" if os.name == "nt" else "clear")  # 터미널 화면 지우기
    draw_board(board)  # 보드 출력


def shuffle_board(board: list[list[int]], seed: int = None):
    random.seed(seed)  # 난수 초기화
    for _ in range(10_000):
        direction = random.choice(["up", "down", "right", "left"])
        move_zero_to(board, direction)  # 무작위로 10,000회 이동


if __name__ == "__main__":
    n_rows = n_cols = 3  # 3행 3열 보드
    board = init_board(n_rows, n_cols)  # 보드 초기화
    shuffle_board(board, seed=1)  # 보드 섞기
    clear_terminal_then_draw_board(board)  # 터미널 화면 지우고, 보드 출력

    key_map = {key.UP: "down", key.DOWN: "up", key.LEFT: "right", key.RIGHT: "left"}
    while True:
        key_in = readkey()  # 키보드 입력 대기
        if key_in in key_map:  # 키보드 입력값이 키 맵에 있는 경우
            move_zero_to(board, key_map[key_in])  # 매핑된 방향으로 0을 이동
        clear_terminal_then_draw_board(board)

        if is_board_solved(board):  # 퍼즐 완성 여부 확인
            print(f"🎉 슬라이딩 퍼즐 완성! 축하합니다! 🎉")
            break
