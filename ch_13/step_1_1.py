from pathlib import Path

WORK_DIR = Path(__file__).parent
IN_DIR = WORK_DIR / "input"

if __name__ == "__main__":
    IN_DIR.mkdir(exist_ok=True)
