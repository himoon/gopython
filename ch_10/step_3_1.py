from pathlib import Path

from docx import Document
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.shared import Mm, Pt, RGBColor
from docx.styles.style import ParagraphStyle
from docx.text.run import Run

from step_1_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.

OUT_3_1 = OUT_DIR / f"{Path(__file__).stem}.docx"


def apply_font(arg: Run | ParagraphStyle, face: str = "Malgun Gothic", size_pt: int = None, is_bold: bool = None, rgb: str = None):
    if face is not None:
        arg.font.name = face  # 폰트 설정
        for prop in ["asciiTheme", "cstheme", "eastAsia", "eastAsiaTheme", "hAnsiTheme"]:
            arg.element.rPr.rFonts.set(qn(f"w:{prop}"), face)  # 한글 폰트 설정
    if size_pt is not None:
        arg.font.size = Pt(size_pt)  # 폰트 크기 설정
    if is_bold is not None:
        arg.font.bold = is_bold  # 폰트 굵기 설정
    if rgb is not None:
        arg.font.color.rgb = RGBColor.from_string(rgb)  # 폰트 색상 설정("FFFFFF" 형식)


def init_docx():
    doc = Document()  # Document 객체 생성
    section = doc.sections[0]  # 첫 번째 섹션(구역) 반환
    section.page_width, section.page_height = Mm(210), Mm(297)  # A4 페이지 크기 설정
    section.top_margin = section.bottom_margin = Mm(20)  # 위, 아래 여백 설정
    section.left_margin = section.right_margin = Mm(12.7)  # 왼쪽, 오른쪽 여백 설정

    style = doc.styles["Normal"]  # 표준("Normal") 단락 서식 설정
    p_format = style.paragraph_format  # 단락 서식 객체 반환
    p_format.space_before = p_format.space_after = 0  # 단락 앞, 단락 뒤 간격 설정
    p_format.line_spacing_rule = WD_LINE_SPACING.SINGLE  # 줄 간격을 1줄로 설정
    apply_font(style, size_pt=10)  # 폰트 설정
    doc.save(OUT_3_1)  # 워드 파일로 저장


if __name__ == "__main__":
    init_docx()
