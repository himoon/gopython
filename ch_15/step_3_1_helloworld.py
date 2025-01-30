import pygame

pygame.init()  # pygame 패키지 초기화
width, height = 800, 100  # 화면의 가로, 세로 크기(픽셀 단위)
screen = pygame.display.set_mode((width, height))  # 화면 크기 설정
clock = pygame.time.Clock()  # 화면 업데이트 주기를 관리하는 Clock 객체 생성
font = pygame.font.Font(None, size=30)  # 폰트 설정(기본 폰트 사용)
running = True  # 이벤트 루프 관리 변수

while running:  # 이벤트 루프
    for event in pygame.event.get():  # 이벤트 목록
        if event.type == pygame.QUIT:  # 창 닫기 이벤트
            running = False
    screen.fill((255, 255, 255))  # 화면을 흰색으로 채우기
    text = font.render("Hello, World!", True, (0, 0, 0))  # 텍스트 생성
    screen.blit(text, (0, 0))  # (0, 0) 좌표에 텍스트 그리기
    pygame.display.flip()  # 화면 업데이트
    clock.tick(60)  # 초당 60 프레임으로 화면 업데이트 주기 설정

pygame.quit()  # pygame 종료
