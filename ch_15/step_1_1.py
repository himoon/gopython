from pathlib import Path

WORK_DIR = Path(__file__).parent
IMG_DIR, IN_DIR = WORK_DIR / "img", WORK_DIR / "input"

if __name__ == "__main__":
    IMG_DIR.mkdir(exist_ok=True)
    IN_DIR.mkdir(exist_ok=True)
