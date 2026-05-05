import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest

CH_10_DIR = Path(__file__).parent.parent.parent / "ch_10"

@pytest.fixture(autouse=True)
def setup_module_path():
    """
    테스트 실행 전/후로 sys.path와 sys.modules를 초기화하는 픽스처입니다.
    다른 챕터의 동일한 이름의 파일(step_*)이 메모리에 남아있을 경우
    엉뚱한 파일이 import되는 모듈 충돌(ImportError 등)을 방지합니다.
    """
    sys.path.insert(0, str(CH_10_DIR))
    for key in list(sys.modules.keys()):
        if key.startswith("step_"):
            del sys.modules[key]
    yield
    if str(CH_10_DIR) in sys.path:
        sys.path.remove(str(CH_10_DIR))


def test_step_1_1_mkdir(tmp_path, monkeypatch):
    """step_1_1.py: 디렉토리 생성 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "IMG_DIR", tmp_path / "img")
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    step_1_1.IMG_DIR.mkdir(exist_ok=True)
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    assert (tmp_path / "img").is_dir()
    assert (tmp_path / "output").is_dir()


@patch("datakart.Fss")
def test_step_1_2_fss(mock_fss, tmp_path, monkeypatch):
    """step_1_2.py: 금융감독원 API 호출 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    import step_1_2  # noqa: E402
    monkeypatch.setattr(step_1_2, "OUT_1_2", tmp_path / "output" / "step_1_2.xlsx")
    
    mock_instance = MagicMock()
    mock_instance.deposit_search.return_value = [{"A": 1}]
    mock_fss.return_value = mock_instance
    
    import runpy
    with patch("pandas.DataFrame.to_excel") as mock_to_excel:
        runpy.run_module("step_1_2", run_name="__main__")
        mock_to_excel.assert_called_once()
        mock_fss.assert_called_once()


@patch("datakart.Ecos")
def test_step_2_1_ecos(mock_ecos, tmp_path, monkeypatch):
    """step_2_1.py: 한국은행 ECOS API 다중 호출 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    import step_2_1  # noqa: E402
    monkeypatch.setattr(step_2_1, "OUT_2_1", tmp_path / "output" / "step_2_1.xlsx")
    
    mock_instance = MagicMock()
    mock_instance.stat_search.return_value = [{"A": 1}]
    mock_ecos.return_value = mock_instance
    
    import runpy
    runpy.run_module("step_2_1", run_name="__main__")
    
    mock_ecos.assert_called_once()
    assert mock_instance.stat_search.call_count == 5
    assert (tmp_path / "output" / "step_2_1.xlsx").exists()


@patch("docx.Document")
def test_step_3_2_docx(mock_document, tmp_path, monkeypatch):
    """step_3_2.py: 워드 문서 제목 추가 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    import step_3_1  # noqa: E402
    monkeypatch.setattr(step_3_1, "OUT_3_1", tmp_path / "step_3_1.docx")
    
    import step_3_2  # noqa: E402
    monkeypatch.setattr(step_3_2, "OUT_3_2", tmp_path / "output" / "step_3_2.docx")
    
    mock_doc = MagicMock()
    mock_document.return_value = mock_doc
    
    import runpy
    runpy.run_module("step_3_2", run_name="__main__")
    
    mock_document.assert_called_once()
    mock_doc.save.assert_called_once()
