import pygame

from step_1_2 import init_board  # 이전에 작성한 모듈을 불러옵니다.
from step_3_1 import init_pygame


def get_screen_size(n_rows: int, n_cols: int, box_size: int = 100) -> tuple[int, int]:
    return n_cols * box_size, n_rows * box_size  # 너비(열) * 높이(행)


def draw_board_gui(board: list[list[int]], screen: pygame.surface.Surface, font: pygame.font.Font, box_size: int = 100):
    for row in range(len(board)):
        for col in range(len(board[row])):
            number = board[row][col]
            if number != 0:
                bbox = pygame.Rect(col * box_size, row * box_size, box_size, box_size)
                pygame.draw.rect(screen, (255, 255, 255), bbox)  # 흰색으로 배경 채우기
                pygame.draw.rect(screen, (200, 200, 200), bbox, 1)  # 외곽선 그리기
                text_img = font.render(f"{number}", True, (0, 0, 0))  # 텍스트 생성
                text_bbox = text_img.get_rect(center=bbox.center)  # 위치 지정
                screen.blit(text_img, text_bbox)  # 화면에 텍스트 그리기


if __name__ == "__main__":
    n_rows, n_cols = 4, 8  # 4행 8열 보드
    board = init_board(n_rows, n_cols)  # 보드 초기화
    scr_size = get_screen_size(n_rows, n_cols)  # 화면 크기
    screen, font, clock = init_pygame(scr_size)  # GUI 초기화
    running = True  # 이벤트 루프 관리 변수

    while running:
        for event in pygame.event.get():  # 이벤트 목록
            if event.type == pygame.QUIT:  # 창 닫기 이벤트
                running = False
        screen.fill((0, 0, 0))  # 검정색으로 배경 채우기
        draw_board_gui(board, screen, font)  # 보드 출력
        pygame.display.flip()  # 화면 업데이트
        clock.tick(60)  # 초당 60 프레임으로 화면 업데이트 주기 설정

    pygame.quit()  # pygame 종료
