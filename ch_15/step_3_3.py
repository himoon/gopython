import pygame

from step_1_2 import init_board  # 이전에 작성한 모듈을 불러옵니다.
from step_2_1 import move_zero_to
from step_2_2 import is_board_solved, shuffle_board
from step_3_2 import draw_board_gui, get_screen_size, init_pygame


def manage_events(board: list[list[int]]) -> bool:
    key_map = {pygame.K_UP: "down", pygame.K_DOWN: "up", pygame.K_LEFT: "right", pygame.K_RIGHT: "left"}
    for event in pygame.event.get():  # 이벤트 목록
        if event.type == pygame.QUIT:  # 창 닫기 이벤트
            return False
        elif event.type == pygame.KEYDOWN:  # 키보드 입력 이벤트
            if event.key in key_map:  # 키보드 입력값이 키 맵에 있는 경우
                move_zero_to(board, key_map[event.key])  # 매핑된 방향으로 0을 이동
                if is_board_solved(board):  # 퍼즐 완성 여부 확인
                    return False
    return True


if __name__ == "__main__":
    n_rows, n_cols = 4, 8  # 4행 8열 보드
    board = init_board(n_rows, n_cols)  # 보드 초기화
    shuffle_board(board, seed=1)  # 보드 섞기
    scr_size = get_screen_size(n_rows, n_cols)  # 화면 크기
    screen, font, clock = init_pygame(scr_size)  # GUI 초기화
    running = True  # 이벤트 루프 관리 변수

    while running:
        running = manage_events(board)  # 이벤트 관리
        screen.fill((0, 0, 0))  # 검정색으로 배경 채우기
        draw_board_gui(board, screen, font)  # 보드 출력
        pygame.display.flip()  # 화면 업데이트
        clock.tick(60)  # 초당 60 프레임으로 화면 업데이트 주기 설정

    pygame.quit()  # pygame 종료
