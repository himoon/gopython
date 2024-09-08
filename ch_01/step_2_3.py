import json
from pathlib import Path

import step_1  # 이전에 작성한 모듈을 불러옵니다.
import step_2_1
import step_2_2

OUT_2_3 = step_1.OUT_DIR / f"{Path(__file__).stem}.json"


def dump_filesize_from_dirnames():
    dirs = step_2_2.load_dirnames()
    result = {}
    for path_str in dirs:
        path = Path(path_str)
        filesize = step_2_1.get_total_filesize(path, pattern="**/*")
        result[path.as_posix()] = filesize

    with open(OUT_2_3, "w") as fp:
        json.dump(result, fp, ensure_ascii=False, indent=2)


def load_filesize_per_dir() -> dict[str, int]:
    if OUT_2_3.is_file():
        with open(OUT_2_3) as fp:
            return json.load(fp)
    return {}


if __name__ == "__main__":
    dump_filesize_from_dirnames()
