from __future__ import annotations

import py_compile
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def chapter_python_files(chapter: str) -> list[Path]:
    chapter_path = REPO_ROOT / chapter
    if not chapter_path.is_dir():
        raise FileNotFoundError(f"Unknown chapter directory: {chapter}")
    return sorted(chapter_path.glob("step*.py"))


def compile_python_file(path: Path) -> None:
    py_compile.compile(str(path), doraise=True)


def run_python_file(path: Path, timeout: int = 20) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def relative_to_repo(path: Path) -> str:
    if path.is_absolute():
        return str(path.relative_to(REPO_ROOT))
    return path.as_posix()