import importlib
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

# ch_01 폴더를 sys.path에 추가하여 step_*.py 내부의 모듈 임포트가 작동하도록 설정
CH_01_DIR = Path(__file__).parent.parent.parent / "ch_01"
sys.path.insert(0, str(CH_01_DIR))

import step_2_1  # noqa: E402
import step_2_3  # noqa: E402
import step_2_4  # noqa: E402
import step_3_1  # noqa: E402
from step_2_2 import get_total_filesize  # noqa: E402


def test_step_2_2_get_total_filesize(tmp_path):
    """step_2_2.py: get_total_filesize 테스트"""
    # 임의의 크기를 가지는 더미 파일 생성
    file1 = tmp_path / "test1.txt"
    file1.write_text("a" * 10)  # 10 bytes
    
    file2 = tmp_path / "test2.log"
    file2.write_text("b" * 20)  # 20 bytes
    
    subdir = tmp_path / "sub"
    subdir.mkdir()
    file3 = subdir / "test3.txt"
    file3.write_text("c" * 30)  # 30 bytes

    # 기본 패턴 (*) - 현재 디렉토리 파일만 계산 (file1, file2)
    total_star = get_total_filesize(tmp_path, "*")
    assert total_star == 30
    
    # 모든 하위 디렉토리 패턴 (**/*) - 모든 파일 계산
    total_glob = get_total_filesize(tmp_path, "**/*")
    assert total_glob == 60


def test_step_2_3_dump_and_load_dirnames(monkeypatch, tmp_path):
    """step_2_3.py: dump_dirnames, load_dirnames 테스트"""
    out_file = tmp_path / "step_2_3.json"
    monkeypatch.setattr(step_2_3, "OUT_2_3", out_file)
    
    # 테스트용 디렉토리 생성
    dir1 = tmp_path / "b_dir"
    dir1.mkdir()
    dir2 = tmp_path / "a_dir"
    dir2.mkdir()
    
    # 일반 파일 생성 (디렉토리만 필터링되는지 확인)
    (tmp_path / "file.txt").touch()

    # JSON 저장 실행
    step_2_3.dump_dirnames(tmp_path)
    
    assert out_file.is_file(), "JSON 파일이 생성되어야 합니다."
    
    # JSON 로드 실행 및 정렬 검증
    loaded_dirs = step_2_3.load_dirnames()
    assert loaded_dirs == [dir2.as_posix(), dir1.as_posix()]


def test_step_2_4_dump_and_load_filesize(monkeypatch, tmp_path):
    """step_2_4.py: dump_filesize_from_dirnames, load_filesize_per_dir 테스트"""
    out_file = tmp_path / "step_2_4.json"
    monkeypatch.setattr(step_2_4, "OUT_2_4", out_file)
    
    mock_dirs = [
        (tmp_path / "dir1").as_posix(),
        (tmp_path / "dir2").as_posix(),
    ]
    
    # 디렉토리와 파일 생성
    for d in mock_dirs:
        Path(d).mkdir()
    (Path(mock_dirs[0]) / "file1.txt").write_text("abc")  # 3 bytes
    (Path(mock_dirs[1]) / "file2.txt").write_text("defg") # 4 bytes

    # load_dirnames 모킹 (step_2_3의 결과를 대체)
    monkeypatch.setattr(step_2_4, "load_dirnames", lambda: mock_dirs)

    # 실행
    step_2_4.dump_filesize_from_dirnames()
    
    assert out_file.is_file(), "JSON 파일이 생성되어야 합니다."
    
    # 로드 및 검증
    loaded_sizes = step_2_4.load_filesize_per_dir()
    assert loaded_sizes == {
        mock_dirs[0]: 3,
        mock_dirs[1]: 4,
    }


def test_step_3_1_dump_and_load_plot_data(monkeypatch, tmp_path):
    """step_3_1.py: dump_plot_data, load_plot_data 테스트"""
    out_file = tmp_path / "step_3_1.json"
    monkeypatch.setattr(step_3_1, "OUT_3_1", out_file)
    
    mock_size_data = {
        "/path/to/dirA": 100,
        "/path/to/dirB": 0,    # 0인 항목은 필터링되어야 함
        "/path/to/dirC": 200,
    }
    
    # load_filesize_per_dir 모킹
    monkeypatch.setattr(step_3_1, "load_filesize_per_dir", lambda: mock_size_data)
    
    # 실행
    step_3_1.dump_plot_data()
    
    assert out_file.is_file(), "JSON 파일이 생성되어야 합니다."
    
    # 로드 및 검증
    loaded_data = step_3_1.load_plot_data()
    assert loaded_data == {
        "stem": ["dirA", "dirC"],
        "size": [100, 200]
    }


@patch("matplotlib.figure.Figure.savefig")
@patch("matplotlib.pyplot.subplots")
def test_step_3_2_and_3_3_plot_generation(mock_subplots, mock_savefig, monkeypatch, tmp_path):
    """step_3_2.py, step_3_3.py: 모듈 임포트 시 그래프 생성 로직 검증"""
    
    # load_plot_data 모킹 (step_3_2, step_3_3 모듈이 실행될 때 사용할 더미 데이터 반환)
    mock_plot_data = {
        "stem": ["dir1", "dir2"],
        "size": [10, 20]
    }
    monkeypatch.setattr(step_3_1, "load_plot_data", lambda: mock_plot_data)
    
    # 출력 디렉토리(OUT_DIR) 모킹
    monkeypatch.setattr(step_2_1, "OUT_DIR", tmp_path)

    # matplotlib mock 설정
    mock_fig = MagicMock()
    mock_ax = MagicMock()
    mock_subplots.return_value = (mock_fig, mock_ax)

    # --- step_3_2 검증 ---
    # 모듈 임포트를 통한 코드 실행 유도 (이미 임포트되었을 수 있으므로 reload 사용)
    import step_3_2
    importlib.reload(step_3_2)
    
    mock_subplots.assert_called()
    mock_fig.savefig.assert_called_with(tmp_path / "step_3_2.png")
    
    # --- step_3_3 검증 ---
    # step_3_3도 동일한 방식으로 검증
    import step_3_3
    importlib.reload(step_3_3)
    
    mock_subplots.assert_called()
    mock_fig.savefig.assert_called_with(tmp_path / "step_3_3.png")
