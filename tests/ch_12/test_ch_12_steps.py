import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest
import pandas as pd

CH_12_DIR = Path(__file__).parent.parent.parent / "ch_12"

@pytest.fixture(autouse=True)
def setup_module_path():
    """
    테스트 실행 전/후로 sys.path와 sys.modules를 초기화하는 픽스처입니다.
    다른 챕터의 동일한 이름의 파일(step_*)이 메모리에 남아있을 경우
    엉뚱한 파일이 import되는 모듈 충돌(ImportError 등)을 방지합니다.
    """
    sys.path.insert(0, str(CH_12_DIR))
    for key in list(sys.modules.keys()):
        if key.startswith("step_"):
            del sys.modules[key]
    yield
    if str(CH_12_DIR) in sys.path:
        sys.path.remove(str(CH_12_DIR))


def test_step_1_1_mkdir(tmp_path, monkeypatch):
    """step_1_1.py: 디렉토리 생성 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "IN_DIR", tmp_path / "input")
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    step_1_1.IN_DIR.mkdir(exist_ok=True)
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    assert (tmp_path / "input").is_dir()
    assert (tmp_path / "output").is_dir()


@patch("playwright.sync_api.sync_playwright")
def test_step_1_2_playwright(mock_sync_playwright):
    """step_1_2.py: Playwright 구동 테스트"""
    import step_1_2  # noqa: E402
    
    mock_playwright = MagicMock()
    mock_browser = MagicMock()
    mock_page = MagicMock()
    
    mock_sync_playwright.return_value.start.return_value = mock_playwright
    mock_playwright.chromium.launch.return_value = mock_browser
    mock_browser.new_page.return_value = mock_page
    
    import runpy
    runpy.run_module("step_1_2", run_name="__main__")
    
    mock_playwright.chromium.launch.assert_called_once()
    mock_browser.new_page.assert_called_once()
    mock_page.goto.assert_called_once_with("https://map.naver.com")


@patch("step_3_1.get_map")
@patch("folium.Marker")
@patch("folium.plugins.MarkerCluster")
@patch("pandas.read_csv")
@patch("step_3_1.get_all_coords")
def test_step_3_2_folium(mock_coords, mock_read_csv, mock_cluster, mock_marker, mock_get_map, tmp_path, monkeypatch):
    """step_3_2.py: folium 클러스터 지도 생성 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    import step_2_2  # noqa: E402
    import step_3_2  # noqa: E402
    monkeypatch.setattr(step_2_2, "OUT_2_2", tmp_path / "output" / "test.csv")
    
    mock_df = pd.DataFrame({"name": ["가게1"], "category": ["한식"], "addr": ["서울"], "laty": [37.5], "lonx": [127.0]})
    mock_read_csv.return_value = mock_df
    mock_coords.return_value = [[37.5, 127.0], [37.5, 127.0]]
    
    mock_map_instance = MagicMock()
    mock_get_map.return_value = mock_map_instance
    
    import runpy
    runpy.run_module("step_3_2", run_name="__main__")
    
    mock_cluster.assert_called_once()
    mock_marker.assert_called_once()
    mock_map_instance.save.assert_called_once()
