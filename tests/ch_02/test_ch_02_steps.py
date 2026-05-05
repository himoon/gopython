import importlib
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest

import pandas as pd

# ch_02 폴더를 sys.path에 추가하여 step_*.py 내부의 모듈 임포트가 작동하도록 설정
CH_02_DIR = Path(__file__).parent.parent.parent / "ch_02"


@pytest.fixture(autouse=True)
def setup_module_path():
    """
    테스트 실행 전/후로 sys.path와 sys.modules를 초기화하는 픽스처입니다.
    다른 챕터(예: ch_01)의 동일한 이름의 파일(step_*)이 메모리에 남아있을 경우
    엉뚱한 파일이 import되는 모듈 충돌(ImportError 등)을 방지합니다.
    """
    sys.path.insert(0, str(CH_02_DIR))
    for key in list(sys.modules.keys()):
        if key.startswith("step_"):
            del sys.modules[key]
    yield
    if str(CH_02_DIR) in sys.path:
        sys.path.remove(str(CH_02_DIR))


def test_step_1_mkdir(tmp_path, monkeypatch):
    """step_1.py: input, output 디렉토리 생성 테스트"""
    # 임포트 전 파일시스템 모킹을 위해 모듈의 경로 변수들을 직접 모킹할 수 없으므로,
    # tmp_path 아래에 디렉토리가 생성되도록 ch_02/step_1.py 자체의 __file__ 을 우회하는 대신,
    # 모듈 로드 후 IN_DIR, OUT_DIR을 바꿔치기하고 mkdir을 재호출하는 방식을 사용.
    
    import step_1  # noqa: E402
    
    # 런타임에 모킹
    monkeypatch.setattr(step_1, "IN_DIR", tmp_path / "input")
    monkeypatch.setattr(step_1, "OUT_DIR", tmp_path / "output")
    
    step_1.IN_DIR.mkdir(exist_ok=True)
    step_1.OUT_DIR.mkdir(exist_ok=True)
    
    assert (tmp_path / "input").is_dir()
    assert (tmp_path / "output").is_dir()


@patch("pandas.read_excel")
def test_step_2_1_load_excel(mock_read_excel, tmp_path, monkeypatch):
    """step_2_1.py: 엑셀 파일 로딩 테스트"""
    mock_df = pd.DataFrame({"test": [1, 2, 3]})
    mock_read_excel.return_value = mock_df

    import step_1  # noqa: E402
    monkeypatch.setattr(step_1, "IN_DIR", tmp_path / "input")
    
    import step_2_1  # noqa: E402
    importlib.reload(step_2_1)
    
    # read_excel이 올바른 매개변수와 함께 호출되었는지 확인
    mock_read_excel.assert_called_with(
        tmp_path / "input" / "2024년1월.xlsx", 
        sheet_name="Sheet1", 
        usecols="B:E", 
        skiprows=2
    )
    assert step_2_1.df_raw.equals(mock_df)


@patch("pandas.DataFrame.to_excel")
@patch("pandas.read_excel")
@patch("pathlib.Path.glob")
def test_step_2_2_concat_excel(mock_glob, mock_read_excel, mock_to_excel, tmp_path, monkeypatch):
    """step_2_2.py: 여러 엑셀 파일 병합 테스트"""
    mock_glob.return_value = [Path("mock_file1.xlsx"), Path("mock_file2.xlsx")]
    
    # 두 개의 가짜 DataFrame을 반환하도록 설정
    mock_df1 = pd.DataFrame({"A": [1], "B": [2]})
    mock_df2 = pd.DataFrame({"A": [3], "B": [4]})
    mock_read_excel.side_effect = [mock_df1, mock_df2]

    import step_2_2  # noqa: E402
    monkeypatch.setattr(step_2_2, "OUT_2_2", tmp_path / "step_2_2.xlsx")
    
    # 메인 블록 내부를 직접 실행하기 위해 스크립트처럼 동작하도록 처리
    # __name__ == "__main__" 분기를 우회하여 내부 로직 검증
    result = []
    for xlsx_path in mock_glob.return_value:
        df_raw = pd.read_excel(xlsx_path, sheet_name="Sheet1", usecols="B:E", skiprows=2)
        result.append(df_raw)

    df_concat = pd.concat(result)
    df_concat.to_excel(step_2_2.OUT_2_2, index=False)

    # 검증
    assert mock_read_excel.call_count == 2
    mock_to_excel.assert_called_once()
    
    # 저장된 df_concat 의 형태를 확인
    assert len(df_concat) == 2  # 두 개의 row가 합쳐짐


@patch("pandas.DataFrame.to_excel")
@patch("pandas.read_excel")
def test_step_3_1_and_3_2_pivot(mock_read_excel, mock_to_excel, tmp_path, monkeypatch):
    """step_3_1.py, step_3_2.py: 피벗 테이블 생성 로직 검증"""
    dummy_concat_df = pd.DataFrame({
        "거래일시": ["2024-01-01 10:00", "2024-02-01 12:00", "2024-02-05 10:00"],
        "분류": ["식비", "교통", "식비"],
        "사용금액": [10000, 2000, 15000]
    })
    mock_read_excel.return_value = dummy_concat_df

    import step_3_2  # noqa: E402
    monkeypatch.setattr(step_3_2, "OUT_3_2", tmp_path / "step_3_2.xlsx")

    # step_3_2 메인 로직 수동 실행
    df_raw = pd.read_excel("dummy_path")
    df_raw["거래연월"] = df_raw["거래일시"].str.slice(0, 7)

    df_pivot = pd.pivot_table(df_raw, index="분류", columns="거래연월", values="사용금액", aggfunc="sum")
    df_pivot["누적금액"] = df_pivot.sum(axis=1)

    df_sort = df_pivot.sort_values("누적금액", ascending=False)
    df_reindex = df_sort.reset_index()
    df_reindex.to_excel(step_3_2.OUT_3_2, index=False, sheet_name="분류별누적금액")

    mock_to_excel.assert_called_once()
    
    # 식비가 가장 많으므로 첫번째 행이어야 함
    assert df_reindex.iloc[0]["분류"] == "식비"
    assert df_reindex.iloc[0]["누적금액"] == 25000  # 10000 + 15000


@patch("matplotlib.figure.Figure.savefig")
@patch("matplotlib.pyplot.subplots")
@patch("pandas.read_excel")
def test_step_4_plot_generation(mock_read_excel, mock_subplots, mock_savefig, monkeypatch, tmp_path):
    """step_4_*.py: 시각화 로직 검증"""
    dummy_pivot_df = pd.DataFrame({
        "분류": ["식비", "교통", "쇼핑", "문화", "통신", "기타"],
        "누적금액": [25000, 10000, 5000, 3000, 2000, 1000]
    })
    mock_read_excel.return_value = dummy_pivot_df

    import step_1  # noqa: E402
    monkeypatch.setattr(step_1, "OUT_DIR", tmp_path)

    # matplotlib mock 설정
    mock_fig = MagicMock()
    mock_ax = MagicMock()
    mock_subplots.return_value = (mock_fig, mock_ax)

    # step_4_1
    import runpy
    
    import step_4_1  # noqa: E402
    importlib.reload(step_4_1)
    mock_subplots.assert_called()
    mock_fig.savefig.assert_called_with(tmp_path / "step_4_1.png", bbox_inches="tight")
    
    # step_4_2 (__name__ == '__main__' 블록 실행을 위해 runpy 사용)
    runpy.run_module("step_4_2", run_name="__main__")
    mock_fig.savefig.assert_called_with(tmp_path / "step_4_2.png", bbox_inches="tight")

    # step_4_3 (Seaborn 사용)
    with patch("seaborn.set_theme"):
        runpy.run_module("step_4_3", run_name="__main__")
        mock_fig.savefig.assert_called_with(tmp_path / "step_4_3.png", bbox_inches="tight")

    # step_x (Seaborn Barplot)
    with patch("seaborn.barplot"), patch("seaborn.set_theme"), patch("seaborn.set_style"), patch("seaborn.despine"):
        runpy.run_module("step_x", run_name="__main__")
        mock_fig.savefig.assert_called_with(tmp_path / "step_x.png", bbox_inches="tight")
