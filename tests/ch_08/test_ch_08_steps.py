import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest
import pandas as pd

CH_08_DIR = Path(__file__).parent.parent.parent / "ch_08"

@pytest.fixture(autouse=True)
def setup_module_path():
    """
    테스트 실행 전/후로 sys.path와 sys.modules를 초기화하는 픽스처입니다.
    다른 챕터의 동일한 이름의 파일(step_*)이 메모리에 남아있을 경우
    엉뚱한 파일이 import되는 모듈 충돌(ImportError 등)을 방지합니다.
    """
    sys.path.insert(0, str(CH_08_DIR))
    for key in list(sys.modules.keys()):
        if key.startswith("step_"):
            del sys.modules[key]
    yield
    if str(CH_08_DIR) in sys.path:
        sys.path.remove(str(CH_08_DIR))


def test_step_1_1_mkdir(tmp_path, monkeypatch):
    """step_1_1.py: 디렉토리 생성 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    assert (tmp_path / "output").is_dir()


@patch("datakart.Naver")
def test_step_1_2_query_naver_shop(mock_naver, tmp_path, monkeypatch):
    """step_1_2.py: 네이버 쇼핑 검색 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    import step_1_2  # noqa: E402
    
    mock_instance = MagicMock()
    mock_instance.shop.return_value = {"items": []}
    mock_naver.return_value = mock_instance
    
    import runpy
    runpy.run_module("step_1_2", run_name="__main__")
    
    mock_naver.assert_called_once()
    mock_instance.shop.assert_called_once()
    assert (tmp_path / "output" / "step_1_2.json").exists()


@patch("pandas.read_csv")
def test_step_2_2_data_cleaning(mock_read_csv, tmp_path, monkeypatch):
    """step_2_2.py: 데이터 정제 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    import step_2_1  # noqa: E402
    monkeypatch.setattr(step_2_1, "OUT_2_1", tmp_path / "input.csv")
    
    import step_2_2  # noqa: E402
    expected_out = tmp_path / "output" / "step_2_2.csv"
    monkeypatch.setattr(step_2_2, "OUT_2_2", expected_out)
    
    mock_df = pd.DataFrame({
        "검색수PC": ["10", "< 10"],
        "검색수M": ["20000", "5000"],
        "클릭률M": ["2.0", "0.5"]
    })
    mock_read_csv.return_value = mock_df
    
    import runpy
    runpy.run_module("step_2_2", run_name="__main__")
    
    assert expected_out.exists()
