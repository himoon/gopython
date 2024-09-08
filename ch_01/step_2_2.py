import json
from pathlib import Path

import step_1  # 이전에 작성한 모듈을 불러옵니다.

OUT_2_2 = step_1.OUT_DIR / f"{Path(__file__).stem}.json"


def dump_dirnames(base_dir: Path) -> None:
    dirs = []
    for path in base_dir.iterdir():
        if path.is_dir() and (not path.is_symlink()):
            dirs.append(path.as_posix())
    dirs_sorted = sorted(dirs)

    with open(OUT_2_2, "w") as fp:
        json.dump(dirs_sorted, fp, ensure_ascii=False, indent=2)


def load_dirnames() -> list[str]:
    if OUT_2_2.is_file():
        with open(OUT_2_2) as fp:
            return json.load(fp)
    return []


if __name__ == "__main__":
    dump_dirnames(Path.home())
