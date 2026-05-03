from __future__ import annotations

from pathlib import Path

import pytest
from support import (
    chapter_python_files,
    compile_python_file,
    relative_to_repo,
    run_python_file,
)

CHAPTER = "ch_14_genai"
ALL_STEP_FILES = chapter_python_files(CHAPTER)
LOCAL_RUN_FILES = [
    Path(CHAPTER) / "step_1_1.py",
    Path(CHAPTER) / "step_3_1_format.py",
]
LIVE_API_FILES = [
    Path(CHAPTER) / "step_1_2_gemini.py",
    Path(CHAPTER) / "step_2_1.py",
    Path(CHAPTER) / "step_2_1_tts.py",
    Path(CHAPTER) / "step_2_2.py",
    Path(CHAPTER) / "step_2_3.py",
    Path(CHAPTER) / "step_2_3_nltk.py",
    Path(CHAPTER) / "step_3_1.py",
    Path(CHAPTER) / "step_3_1_prompt.py",
]


@pytest.mark.parametrize("script_path", ALL_STEP_FILES, ids=relative_to_repo)
def test_all_step_files_compile(script_path):
    compile_python_file(script_path)


@pytest.mark.parametrize("script_path", LOCAL_RUN_FILES, ids=relative_to_repo)
def test_local_step_scripts_run(script_path, repo_root):
    result = run_python_file(repo_root / script_path)

    assert result.returncode == 0, result.stderr or result.stdout


@pytest.mark.live_api
@pytest.mark.parametrize("script_path", LIVE_API_FILES, ids=relative_to_repo)
def test_live_api_step_scripts_run(script_path, repo_root):
    result = run_python_file(repo_root / script_path, timeout=60)

    assert result.returncode == 0, result.stderr or result.stdout