from pathlib import Path

WORK_DIR = Path(__file__).parent
IMG_DIR, OUT_DIR = WORK_DIR / "img", WORK_DIR / "output"

if __name__ == "__main__":
    IMG_DIR.mkdir(exist_ok=True)
    OUT_DIR.mkdir(exist_ok=True)
