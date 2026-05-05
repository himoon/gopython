import importlib
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest

# ch_04 폴더를 sys.path에 추가하여 step_*.py 내부의 모듈 임포트가 작동하도록 설정
CH_04_DIR = Path(__file__).parent.parent.parent / "ch_04"


@pytest.fixture(autouse=True)
def setup_module_path():
    """
    테스트 실행 전/후로 sys.path와 sys.modules를 초기화하는 픽스처입니다.
    다른 챕터의 동일한 이름의 파일(step_*)이 메모리에 남아있을 경우
    엉뚱한 파일이 import되는 모듈 충돌(ImportError 등)을 방지합니다.
    """
    sys.path.insert(0, str(CH_04_DIR))
    for key in list(sys.modules.keys()):
        if key.startswith("step_"):
            del sys.modules[key]
    yield
    if str(CH_04_DIR) in sys.path:
        sys.path.remove(str(CH_04_DIR))


def test_step_1_1_mkdir(tmp_path, monkeypatch):
    """step_1_1.py: 디렉토리 생성 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "IN_DIR", tmp_path / "input")
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    step_1_1.IN_DIR.mkdir(exist_ok=True)
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    assert (tmp_path / "input").is_dir()
    assert (tmp_path / "output").is_dir()


@patch("qrcode.make")
def test_step_1_4_save_qrcode(mock_qr_make, tmp_path, monkeypatch):
    """step_1_4.py: QR코드 생성 및 저장 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    mock_img = MagicMock()
    mock_qr_make.return_value = mock_img
    
    import runpy
    runpy.run_module("step_1_4", run_name="__main__")
    
    assert mock_qr_make.call_count == 2
    assert mock_img.save.call_count == 2


@patch("qrcode.make")
def test_step_2_2_vcard(mock_qr_make, tmp_path, monkeypatch):
    """step_2_2.py: vCard 생성 및 QR코드 변환 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path)
    
    import step_2_2  # noqa: E402
    monkeypatch.setattr(step_2_2, "OUT_2_2_VCF", tmp_path / "step_2_2.vcf")
    monkeypatch.setattr(step_2_2, "OUT_2_2_PNG", tmp_path / "step_2_2.png")
    
    mock_img = MagicMock()
    mock_qr_make.return_value = mock_img
    
    # __name__ == '__main__' 블록 실행
    import runpy
    runpy.run_module("step_2_2", run_name="__main__")
    
    assert (tmp_path / "step_2_2.vcf").exists()
    mock_qr_make.assert_called_once()
    mock_img.save.assert_called_once_with(tmp_path / "step_2_2.png")


@patch("PIL.Image.open")
def test_step_3_2_qr_with_icon(mock_image_open, tmp_path, monkeypatch):
    """step_3_2.py: QR코드 가운데 아이콘 삽입 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "IN_DIR", tmp_path / "input")
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    import step_2_2  # noqa: E402
    monkeypatch.setattr(step_2_2, "OUT_2_2_PNG", tmp_path / "step_2_2.png")
    
    import step_3_2  # noqa: E402
    monkeypatch.setattr(step_3_2, "OUT_3_2", tmp_path / "output" / "step_3_2.png")
    
    mock_qr = MagicMock()
    mock_qr.size = (200, 200)
    mock_qr.convert.return_value = mock_qr
    
    mock_icon = MagicMock()
    
    # Image.open은 QR 코드 한번, 아이콘 한번, 총 두 번 호출됨
    mock_image_open.side_effect = [mock_qr, mock_icon]
    
    # __name__ == '__main__' 블록 실행
    import runpy
    runpy.run_module("step_3_2", run_name="__main__")
    
    mock_qr.paste.assert_called_once()
    mock_qr.save.assert_called_once_with(tmp_path / "output" / "step_3_2.png")
