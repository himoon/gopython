import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest

CH_06_DIR = Path(__file__).parent.parent.parent / "ch_06"

@pytest.fixture(autouse=True)
def setup_module_path():
    """
    테스트 실행 전/후로 sys.path와 sys.modules를 초기화하는 픽스처입니다.
    다른 챕터의 동일한 이름의 파일(step_*)이 메모리에 남아있을 경우
    엉뚱한 파일이 import되는 모듈 충돌(ImportError 등)을 방지합니다.
    """
    sys.path.insert(0, str(CH_06_DIR))
    for key in list(sys.modules.keys()):
        if key.startswith("step_"):
            del sys.modules[key]
    yield
    if str(CH_06_DIR) in sys.path:
        sys.path.remove(str(CH_06_DIR))


def test_step_1_1_mkdir(tmp_path, monkeypatch):
    """step_1_1.py: 디렉토리 생성 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    assert (tmp_path / "output").is_dir()


@patch("playwright.sync_api.sync_playwright")
def test_step_1_2_run_playwright(mock_sync_playwright):
    """step_1_2.py: Playwright 초기화 및 브라우저 시작 테스트"""
    import step_1_2  # noqa: E402
    
    mock_playwright = MagicMock()
    mock_browser = MagicMock()
    mock_context = MagicMock()
    mock_page = MagicMock()
    
    mock_sync_playwright.return_value.start.return_value = mock_playwright
    mock_playwright.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    
    # expect_page 컨텍스트 관리자 모킹
    mock_expect_page = MagicMock()
    mock_expect_page.__enter__.return_value.value = mock_page
    mock_context.expect_page.return_value = mock_expect_page

    play, browser, page = step_1_2.run_playwright()
    
    assert play == mock_playwright
    assert browser == mock_browser
    assert page == mock_page
    mock_playwright.chromium.launch.assert_called()


def test_step_1_3_goto_best_goods():
    """step_1_3.py: 베스트상품 페이지 이동 로직 검증"""
    import step_1_3  # noqa: E402
    
    mock_page = MagicMock()
    step_1_3.goto_best_goods(mock_page)
    
    # get_by_role가 올바르게 호출되었는지 확인
    assert mock_page.get_by_role.call_count >= 2


def test_step_2_1_select_category_and_options():
    """step_2_1.py: 카테고리 및 세부 옵션 선택 로직 검증"""
    import step_2_1  # noqa: E402
    
    mock_page = MagicMock()
    step_2_1.select_category(mock_page, "패션의류")
    mock_page.locator.assert_called()
    
    step_2_1.select_options(mock_page, "10대 여성")
    mock_page.get_by_role.assert_called()
    mock_page.get_by_text.assert_called()


def test_step_3_1_init_docx():
    """step_3_1.py: 워드 문서 생성 및 스타일 설정 테스트"""
    import step_3_1  # noqa: E402
    
    doc = step_3_1.init_docx()
    assert doc is not None
    # 단락이 정상적으로 생성되었는지 확인
    assert len(doc.paragraphs) > 0


@patch("docx.text.run.Run.add_picture")
@patch("step_2_3.fetch_trends_by_filter")
@patch("pathlib.Path.read_text")
def test_step_3_2_add_table(mock_read_text, mock_fetch_trends, mock_add_picture, monkeypatch, tmp_path):
    """step_3_2.py: 워드 문서 표 추가 및 이미지 삽입 테스트"""
    import json
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    import step_3_1  # noqa: E402
    doc = step_3_1.init_docx()
    
    import step_3_2  # noqa: E402
    import step_2_2  # noqa: E402
    monkeypatch.setattr(step_2_2, "OUT_2_2", tmp_path / "step_2_2.json")
    
    # 빈 이미지 리스트 반환 모킹
    mock_read_text.return_value = json.dumps(["img1.jpg", "img2.jpg"])
    
    step_3_2.add_table(doc, "패션의류", "10대 여성")
    
    mock_fetch_trends.assert_called_with("패션의류", "10대 여성")
    # 테이블이 추가되었는지 확인
    assert len(doc.tables) > 0
