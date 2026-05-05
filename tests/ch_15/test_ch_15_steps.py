import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest

CH_15_DIR = Path(__file__).parent.parent.parent / "ch_15"

@pytest.fixture(autouse=True)
def setup_module_path():
    """
    테스트 실행 전/후로 sys.path와 sys.modules를 초기화하는 픽스처입니다.
    다른 챕터의 동일한 이름의 파일(step_*)이 메모리에 남아있을 경우
    엉뚱한 파일이 import되는 모듈 충돌(ImportError 등)을 방지합니다.
    """
    sys.path.insert(0, str(CH_15_DIR))
    for key in list(sys.modules.keys()):
        if key.startswith("step_"):
            del sys.modules[key]
    yield
    if str(CH_15_DIR) in sys.path:
        sys.path.remove(str(CH_15_DIR))


def test_step_1_2_init_board():
    """step_1_2.py: 보드 초기화 로직 테스트"""
    import step_1_2  # noqa: E402
    
    board = step_1_2.init_board(3, 3)
    assert len(board) == 3
    assert len(board[0]) == 3
    assert board == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]


def test_step_2_1_move_zero():
    """step_2_1.py: 숫자 0(빈칸) 이동 로직 테스트"""
    import step_1_2  # noqa: E402
    import step_2_1  # noqa: E402
    
    board = step_1_2.init_board(3, 3)
    
    # 초기에 0은 (2, 2) 위치에 있음
    assert step_2_1.find_zero(board) == (2, 2)
    
    # 0을 아래나 오른쪽으로 이동할 수 없음 (보드 밖)
    assert not step_2_1.move_zero_to(board, "down")
    assert not step_2_1.move_zero_to(board, "right")
    
    # 0을 위로 이동 (2, 2 -> 1, 2)
    assert step_2_1.move_zero_to(board, "up")
    assert board[1][2] == 0
    assert board[2][2] == 6


@patch("pygame.draw.rect")
def test_step_3_2_draw_board_gui(mock_draw_rect):
    """step_3_2.py: Pygame GUI 보드 그리기 테스트"""
    import pygame
    import step_1_2  # noqa: E402
    import step_3_2  # noqa: E402
    
    board = step_1_2.init_board(2, 2)  # 작은 보드
    
    mock_screen = MagicMock()
    mock_font = MagicMock()
    mock_text_img = MagicMock()
    mock_font.render.return_value = mock_text_img
    
    # 모킹된 객체로 그리기 로직 호출
    step_3_2.draw_board_gui(board, mock_screen, mock_font, box_size=100)
    
    # 1, 2, 3 세 개의 숫자(0 제외)에 대해 텍스트가 렌더링되어야 함
    assert mock_font.render.call_count == 3
    assert mock_screen.blit.call_count == 3


@patch("pygame.event.get")
def test_step_3_3_manage_events(mock_event_get):
    """step_3_3.py: 키보드 이벤트 처리 테스트"""
    import pygame
    import step_1_2  # noqa: E402
    import step_3_3  # noqa: E402
    
    board = step_1_2.init_board(3, 3)
    
    # QUIT 이벤트 생성
    quit_event = MagicMock()
    quit_event.type = pygame.QUIT
    
    # KEYDOWN (UP 화살표) 이벤트 생성
    keydown_up_event = MagicMock()
    keydown_up_event.type = pygame.KEYDOWN
    keydown_up_event.key = pygame.K_UP
    
    # 1. UP 방향키 입력 시 (실제로는 보드 상의 0을 down으로 이동하게 매핑됨)
    mock_event_get.return_value = [keydown_up_event]
    
    # 아직 풀리지 않았으므로 True 반환해야 함
    # 다만 0은 맨 아래(2,2)에 있어서 down으로 못 가므로 보드 상태 변화는 없음
    with patch("step_3_3.is_board_solved", return_value=False):
        assert step_3_3.manage_events(board) is True
    
    # 2. QUIT 이벤트 처리
    mock_event_get.return_value = [quit_event]
    assert step_3_3.manage_events(board) is False
