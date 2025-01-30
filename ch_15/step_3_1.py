import pygame

from step_1_1 import IN_DIR  # 이전에 작성한 모듈을 불러옵니다.


def init_pygame(scr_size: tuple[int, int], font_size: int = 30):
    pygame.init()  # pygame 패키지 초기화
    pygame.display.set_caption(f"슬라이딩 퍼즐")  # 게임 제목
    screen = pygame.display.set_mode(scr_size)  # 화면 크기
    font = pygame.font.Font(IN_DIR / "Pretendard-Bold.ttf", size=font_size)
    clock = pygame.time.Clock()  # 화면 업데이트 주기를 관리하는 Clock 객체 생성
    return screen, font, clock


if __name__ == "__main__":
    width, height = 800, 100  # 화면 크기
    screen, font, clock = init_pygame((width, height), 15)  # GUI 초기화
    running = True  # 이벤트 루프 관리 변수

    while running:  # 이벤트 루프
        for event in pygame.event.get():  # 이벤트 목록
            if event.type == pygame.QUIT:  # 창 닫기 이벤트
                running = False
            screen.fill((255, 255, 255))  # 화면을 흰색으로 채우기
            center = width / 2, height / 2  # 화면 중앙 위치
            text_img = font.render(f"{event=}", True, (0, 0, 0))  # 텍스트 생성
            text_bbox = text_img.get_rect(center=center)  # 위치 지정
            screen.blit(text_img, text_bbox)  # 화면에 텍스트 그리기
        pygame.display.flip()  # 화면 업데이트
        clock.tick(60)  # 초당 60 프레임으로 화면 업데이트 주기 설정

    pygame.quit()  # pygame 종료
