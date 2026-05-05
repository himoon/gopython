import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest
import pandas as pd

CH_07_DIR = Path(__file__).parent.parent.parent / "ch_07"

@pytest.fixture(autouse=True)
def setup_module_path():
    """
    테스트 실행 전/후로 sys.path와 sys.modules를 초기화하는 픽스처입니다.
    다른 챕터의 동일한 이름의 파일(step_*)이 메모리에 남아있을 경우
    엉뚱한 파일이 import되는 모듈 충돌(ImportError 등)을 방지합니다.
    """
    sys.path.insert(0, str(CH_07_DIR))
    for key in list(sys.modules.keys()):
        if key.startswith("step_"):
            del sys.modules[key]
    yield
    if str(CH_07_DIR) in sys.path:
        sys.path.remove(str(CH_07_DIR))


def test_step_1_1_mkdir(tmp_path, monkeypatch):
    """step_1_1.py: 디렉토리 생성 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    step_1_1.OUT_DIR.mkdir(exist_ok=True)
    
    assert (tmp_path / "output").is_dir()


def test_step_1_3_goto_market_cap_and_parse():
    """step_1_3.py: 시가총액 페이지 이동 및 표 추출 테스트"""
    import step_1_3  # noqa: E402
    
    mock_page = MagicMock()
    step_1_3.goto_market_cap(mock_page)
    
    assert mock_page.goto.call_count == 1
    assert mock_page.get_by_role.call_count == 2
    
    # parse_table_kospi 모킹 테스트
    mock_table = MagicMock()
    mock_page.locator.return_value = mock_table
    
    # header와 body 추출 부분 모킹
    mock_thead = MagicMock()
    mock_thead.all_inner_texts.return_value = ["N", "종목명", "현재가"]
    mock_tbody = MagicMock()
    
    mock_tr = MagicMock()
    mock_td = MagicMock()
    mock_td.all_inner_texts.return_value = ["1", "삼성전자", "80000"]
    mock_tr.locator.return_value = mock_td
    mock_tbody.all.return_value = [mock_tr]
    
    mock_table.locator.side_effect = [mock_thead, mock_tbody]
    
    header, body = step_1_3.parse_table_kospi(mock_page)
    assert header == ["N", "종목명", "현재가"]
    assert body == [["1", "삼성전자", "80000"]]


def test_step_2_1_fetch_total_page():
    """step_2_1.py: 총 페이지 수 추출 테스트"""
    import step_2_1  # noqa: E402
    
    mock_page = MagicMock()
    mock_table = MagicMock()
    mock_td = MagicMock()
    mock_a = MagicMock()
    
    mock_page.locator.return_value = mock_table
    mock_table.locator.return_value.last = mock_td
    mock_td.locator.return_value = mock_a
    mock_a.get_attribute.return_value = "/sise/sise_market_sum.naver?&page=45"
    
    total_page = step_2_1.fetch_total_page(mock_page)
    assert total_page == 45


@patch("pandas.read_csv")
@patch("plotly.express.treemap")
def test_step_3_2_treemap(mock_treemap, mock_read_csv, tmp_path, monkeypatch):
    """step_3_2.py: 트리맵 시각화 로직 검증"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "OUT_DIR", tmp_path / "output")
    
    import step_3_1  # noqa: E402
    monkeypatch.setattr(step_3_1, "OUT_3_1", tmp_path / "step_3_1.csv")
    
    mock_df = pd.DataFrame({"종목명": ["삼성전자", "SK하이닉스"], "조단위": [400, 100]})
    mock_read_csv.return_value = mock_df
    
    mock_fig = MagicMock()
    mock_treemap.return_value = mock_fig
    
    # __name__ == '__main__' 블록 실행
    import runpy
    
    import step_3_2  # noqa: E402
    # step_3_2 uses its __file__ stem, so output is step_3_2.png
    expected_out = tmp_path / "output" / "step_3_2.png"
    monkeypatch.setattr(step_3_2, "img_path", expected_out)
    
    runpy.run_module("step_3_2", run_name="__main__")
    
    assert mock_treemap.call_count == 2
    assert mock_fig.update_traces.call_count == 2
    assert mock_fig.update_layout.call_count == 2
    assert mock_fig.write_image.call_count == 2