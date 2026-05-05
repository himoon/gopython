import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest
import pandas as pd

CH_11_DIR = Path(__file__).parent.parent.parent / "ch_11"

@pytest.fixture(autouse=True)
def setup_module_path():
    """
    테스트 실행 전/후로 sys.path와 sys.modules를 초기화하는 픽스처입니다.
    다른 챕터의 동일한 이름의 파일(step_*)이 메모리에 남아있을 경우
    엉뚱한 파일이 import되는 모듈 충돌(ImportError 등)을 방지합니다.
    """
    sys.path.insert(0, str(CH_11_DIR))
    for key in list(sys.modules.keys()):
        if key.startswith("step_"):
            del sys.modules[key]
    yield
    if str(CH_11_DIR) in sys.path:
        sys.path.remove(str(CH_11_DIR))


def test_step_1_mkdir(tmp_path, monkeypatch):
    """step_1.py: 디렉토리 생성 테스트"""
    import step_1  # noqa: E402
    monkeypatch.setattr(step_1, "IN_DIR", tmp_path / "input")
    monkeypatch.setattr(step_1, "OUT_DIR", tmp_path / "output")
    
    step_1.IN_DIR.mkdir(exist_ok=True)
    step_1.OUT_DIR.mkdir(exist_ok=True)
    
    assert (tmp_path / "input").is_dir()
    assert (tmp_path / "output").is_dir()


@patch("datakart.Datagokr")
@patch("pandas.DataFrame.to_csv")
def test_step_2_1_sido_sgg(mock_to_csv, mock_datagokr, tmp_path, monkeypatch):
    """step_2_1.py: 공공데이터포털 법정동 코드 API 테스트"""
    import step_1  # noqa: E402
    monkeypatch.setattr(step_1, "OUT_DIR", tmp_path / "output")
    step_1.OUT_DIR.mkdir(exist_ok=True)
    
    import step_2_1  # noqa: E402
    monkeypatch.setattr(step_2_1, "OUT_2_1", tmp_path / "output" / "step_2_1.csv")
    
    mock_instance = MagicMock()
    mock_instance.lawd_code.return_value = [
        {"sido_cd": "11", "sgg_cd": "110", "umd_cd": "000", "ri_cd": "00", "locatadd_nm": "서울특별시 종로구"}
    ]
    mock_datagokr.return_value = mock_instance
    
    import runpy
    runpy.run_module("step_2_1", run_name="__main__")
    
    mock_datagokr.assert_called_once()
    mock_instance.lawd_code.assert_called_once_with("서울특별시")
    mock_to_csv.assert_called_once()


@patch("datakart.Sgis")
@patch("pathlib.Path.write_text")
def test_step_3_2_sgis(mock_write_text, mock_sgis, tmp_path, monkeypatch):
    """step_3_2.py: 통계지리정보서비스 행정구역 경계 데이터 API 테스트"""
    import step_1  # noqa: E402
    monkeypatch.setattr(step_1, "OUT_DIR", tmp_path / "output")
    step_1.OUT_DIR.mkdir(exist_ok=True)
    
    import step_3_2  # noqa: E402
    expected_out = tmp_path / "output" / "step_3_2.geojson"
    monkeypatch.setattr(step_3_2, "OUT_3_2", expected_out)
    
    mock_instance = MagicMock()
    mock_instance.hadm_area.return_value = '{"type": "FeatureCollection"}'
    mock_sgis.return_value = mock_instance
    
    import runpy
    # write_text 모킹 대신 실제 쓰기를 해도 무방하지만, mock_write_text로 우회
    # 단, Path.write_text를 모킹했으므로 assert_called_once_with로 확인
    runpy.run_module("step_3_2", run_name="__main__")
    
    mock_sgis.assert_called_once()
    mock_instance.hadm_area.assert_called_once_with(adm_cd="11", low_search="1")
    mock_write_text.assert_called_once()
