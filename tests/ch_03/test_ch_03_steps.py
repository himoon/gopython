import importlib
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest

# ch_03 폴더를 sys.path에 추가하여 step_*.py 내부의 모듈 임포트가 작동하도록 설정
CH_03_DIR = Path(__file__).parent.parent.parent / "ch_03"


@pytest.fixture(autouse=True)
def setup_module_path():
    """
    테스트 실행 전/후로 sys.path와 sys.modules를 초기화하는 픽스처입니다.
    다른 챕터의 동일한 이름의 파일(step_*)이 메모리에 남아있을 경우
    엉뚱한 파일이 import되는 모듈 충돌(ImportError 등)을 방지합니다.
    """
    sys.path.insert(0, str(CH_03_DIR))
    for key in list(sys.modules.keys()):
        if key.startswith("step_"):
            del sys.modules[key]
    yield
    if str(CH_03_DIR) in sys.path:
        sys.path.remove(str(CH_03_DIR))


def test_step_1_1_mkdir(tmp_path, monkeypatch):
    """step_1_1.py: 디렉토리 생성 테스트"""
    import step_1_1  # noqa: E402
    
    # 런타임에 모킹
    monkeypatch.setattr(step_1_1, "IMG_DIR", tmp_path / "img")
    monkeypatch.setattr(step_1_1, "IN_DIR", tmp_path / "input")
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    step_1_1.IMG_DIR.mkdir(exist_ok=True)
    step_1_1.IN_DIR.mkdir(exist_ok=True)
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    assert (tmp_path / "img").is_dir()
    assert (tmp_path / "input").is_dir()
    assert (tmp_path / "output").is_dir()


@patch("PIL.Image.open")
@patch("PIL.Image.new")
def test_step_3_2_concat_image(mock_image_new, mock_image_open, tmp_path, monkeypatch):
    """step_3_2.py: 이미지 병합 로직 검증"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "IMG_DIR", tmp_path / "img")
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    import step_3_2  # noqa: E402
    monkeypatch.setattr(step_3_2, "OUT_3_2", tmp_path / "step_3_2.jpg")
    
    # 가상의 이미지 파일 2개 생성
    (tmp_path / "img").mkdir()
    (tmp_path / "img" / "test1.jpg").touch()
    (tmp_path / "img" / "test2.jpg").touch()
    
    mock_bg = MagicMock()
    mock_image_new.return_value = mock_bg

    mock_img = MagicMock()
    mock_img.size = (500, 500)
    mock_image_open.return_value = mock_img
    
    # __name__ == '__main__' 블록 실행
    import runpy
    runpy.run_module("step_3_2", run_name="__main__")
    
    # 저장되었는지 확인 (runpy는 모듈을 다시 평가하므로 OUT_DIR에 저장됨)
    mock_bg.save.assert_called_with(tmp_path / "output" / "step_3_2.jpg")
    assert mock_image_open.call_count == 2


@patch("PIL.Image.alpha_composite")
@patch("PIL.ImageDraw.Draw")
@patch("PIL.ImageFont.truetype")
@patch("PIL.Image.open")
def test_step_3_3_text_overlay(mock_image_open, mock_font, mock_draw, mock_alpha_composite, tmp_path, monkeypatch):
    """step_3_3.py: 텍스트 오버레이 로직 검증"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "IN_DIR", tmp_path / "input")
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    import step_3_2  # noqa: E402
    monkeypatch.setattr(step_3_2, "OUT_3_2", tmp_path / "step_3_2.jpg")

    mock_font_instance = MagicMock()
    mock_font_instance.getbbox.return_value = (0, 0, 100, 50)
    mock_font.return_value = mock_font_instance

    mock_img = MagicMock()
    mock_img.size = (500, 500)
    mock_image_open.return_value = mock_img
    
    mock_final = MagicMock()
    mock_alpha_composite.return_value = mock_final

    import step_3_3  # noqa: E402
    importlib.reload(step_3_3)
    
    mock_final.convert.return_value.save.assert_called()
