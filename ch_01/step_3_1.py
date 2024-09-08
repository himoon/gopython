import json
from pathlib import Path

import step_1  # 이전에 작성한 모듈을 불러옵니다.
import step_2_3

OUT_3_1 = step_1.OUT_DIR / f"{Path(__file__).stem}.json"


def dump_plot_data():
    size_per_path = step_2_3.load_filesize_per_dir()
    size_per_stem = {Path(path).stem: size for path, size in size_per_path.items() if size > 0}
    plot_data = dict(
        stem=list(size_per_stem.keys()),
        size=list(size_per_stem.values()),
    )

    with open(OUT_3_1, "w") as fp:
        json.dump(plot_data, fp, ensure_ascii=False, indent=2)


def load_plot_data() -> dict:
    if OUT_3_1.is_file():
        with open(OUT_3_1) as fp:
            return json.load(fp)
    return {}


if __name__ == "__main__":
    dump_plot_data()