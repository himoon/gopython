from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_1 import init_docx
from step_3_2 import add_table


def make_report(category: str, option: str):
    doc = init_docx()
    add_table(doc, category, option)  # 표 추가
    doc.save(OUT_DIR / f"{category.replace('/','')}_{option}.docx")


if __name__ == "__main__":
    make_report("패션의류", "20대 여성")
    make_report("패션잡화", "30대 남성")
    make_report("화장품/미용", "40대 여성")
    make_report("디지털/가전", "50대 이상 남성")
