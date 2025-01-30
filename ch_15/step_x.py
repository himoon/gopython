import pygame
from PIL import Image, ImageOps

from step_1_1 import IMG_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_1_2 import init_board
from step_2_2 import shuffle_board
from step_3_2 import get_screen_size, init_pygame
from step_3_3 import manage_events


def draw_board_img(board: list[list[int]], screen: pygame.surface.Surface, font: pygame.font.Font, box_size: int = 100):
    for row in range(len(board)):
        for col in range(len(board[row])):
            number = board[row][col]
            if number != 0:
                bbox = pygame.Rect(col * box_size, row * box_size, box_size, box_size)
                pygame.draw.rect(screen, (200, 200, 200), bbox, 1)  # 외곽선 그리기
                text_img = font.render(f"{number}", True, (255, 255, 255))  # 텍스트 생성
                text_bbox = text_img.get_rect(center=bbox.center)  # 위치 지정
                screen.blit(text_img, text_bbox)  # 화면에 텍스트 그리기


if __name__ == "__main__":
    n_rows, n_cols = 4, 8  # 4행 8열 보드
    board = init_board(n_rows, n_cols)  # 보드 초기화
    shuffle_board(board, seed=1)  # 보드 섞기
    scr_size = get_screen_size(n_rows, n_cols)  # 화면 크기
    screen, font, clock = init_pygame(scr_size)  # GUI 초기화
    running = True  # 이벤트 루프 관리 변수

    img_raw = Image.open(IMG_DIR / "bg.jpg")  # 배경 이미지 불러오기
    img_fit = ImageOps.fit(img_raw, scr_size)  # 이미지 크기 변경
    img_bg = pygame.image.frombuffer(img_fit.tobytes(), scr_size, "RGB")

    while running:
        running = manage_events(board)  # 이벤트 관리
        screen.blit(img_bg, dest=(0, 0))  # 배경 이미지 그리기
        black = pygame.Surface(scr_size, pygame.SRCALPHA)  # Surface 객체 생성
        black.fill((0, 0, 0, 128))  # 불투명도 적용한 검정색으로 채우기
        screen.blit(black, dest=(0, 0))  #  검정색으로 배경 채우기
        draw_board_img(board, screen, font)  # 보드 출력
        pygame.display.flip()  # 화면 업데이트
        clock.tick(60)  # 초당 60 프레임으로 화면 업데이트 주기 설정

    pygame.quit()  # pygame 종료
