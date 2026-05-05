import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest

CH_09_DIR = Path(__file__).parent.parent.parent / "ch_09"

@pytest.fixture(autouse=True)
def setup_module_path():
    """
    테스트 실행 전/후로 sys.path와 sys.modules를 초기화하는 픽스처입니다.
    다른 챕터의 동일한 이름의 파일(step_*)이 메모리에 남아있을 경우
    엉뚱한 파일이 import되는 모듈 충돌(ImportError 등)을 방지합니다.
    """
    sys.path.insert(0, str(CH_09_DIR))
    for key in list(sys.modules.keys()):
        if key.startswith("step_"):
            del sys.modules[key]
    yield
    if str(CH_09_DIR) in sys.path:
        sys.path.remove(str(CH_09_DIR))


def test_step_1_1_mkdir(tmp_path, monkeypatch):
    """step_1_1.py: 디렉토리 생성 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    assert (tmp_path / "output").is_dir()


@patch("datakart.Ecos")
def test_step_2_1_ecos(mock_ecos, tmp_path, monkeypatch):
    """step_2_1.py: ECOS API 호출 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    mock_instance = MagicMock()
    mock_instance.stat_search.return_value = [{"A": 1}]
    mock_ecos.return_value = mock_instance
    
    import runpy
    runpy.run_module("step_2_1", run_name="__main__")
    
    mock_ecos.assert_called_once()
    mock_instance.stat_search.assert_called_once()
    assert (tmp_path / "output" / "step_2_1.csv").exists()


@patch("matplotlib.pyplot.subplots")
@patch("pandas.read_excel")
@patch("seaborn.lineplot")
@patch("seaborn.despine")
def test_step_3_2_subplots(mock_despine, mock_lineplot, mock_read_excel, mock_subplots, tmp_path, monkeypatch):
    """step_3_2.py: 서브플롯 시각화 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    import step_2_2  # noqa: E402
    monkeypatch.setattr(step_2_2, "OUT_2_2", tmp_path / "step_2_2.xlsx")
    
    import pandas as pd
    mock_df = pd.DataFrame({"TIME": ["20230101"], "DATA_VALUE": ["10"]})
    mock_read_excel.return_value = mock_df
    
    mock_fig = MagicMock()
    mock_axes = [[MagicMock(), MagicMock()], [MagicMock(), MagicMock()]]
    mock_subplots.return_value = (mock_fig, mock_axes)
    
    import runpy
    runpy.run_module("step_3_2", run_name="__main__")
    
    mock_fig.savefig.assert_called_once_with(tmp_path / "output" / "step_3_2.png")
