import json
from pathlib import Path

from step_2_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_2_2 import get_total_filesize
from step_2_3 import load_dirnames

OUT_2_4 = OUT_DIR / f"{Path(__file__).stem}.json"


def dump_filesize_from_dirnames():
    dirs = load_dirnames()
    result = {}
    for path_str in dirs:
        path = Path(path_str)
        filesize = get_total_filesize(path, pattern="**/*")
        result[path.as_posix()] = filesize

    with open(OUT_2_4, "w", encoding="utf-8") as fp:
        json.dump(result, fp, ensure_ascii=False, indent=2)


def load_filesize_per_dir() -> dict[str, int]:
    if OUT_2_4.is_file():
        with open(OUT_2_4, encoding="utf-8") as fp:
            return json.load(fp)
    return {}


if __name__ == "__main__":
    dump_filesize_from_dirnames()
