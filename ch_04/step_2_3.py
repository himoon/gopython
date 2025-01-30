import vobject

vcard = vobject.vCard()
fn = vcard.add("FN")  # 전체 이름
fn.value = "혼자 만들면서 배우는 파이썬"
name = vcard.add("N")  # 이름
name.value = vobject.vcard.Name(family="혼자 만들면서 배우는", given="파이썬")

tel_cell = vcard.add("TEL")  # 전화번호
tel_cell.value = "+82(10)1234-5678"
tel_cell.type_param = "CELL"  # 휴대용
tel_work = vcard.add("TEL")
tel_work.value = "+82(2)1234-5678"
tel_work.type_param = "WORK"  # 업무용
print(vcard.serialize())

email = vcard.add("EMAIL")  # 이메일
email.value = "email@example.com"
email.type_param = "WORK"

title = vcard.add("TITLE")  # 직책
title.value = "(직책)편집자"

org = vcard.add("ORG")  # 소속
org.value = ["(직장)한빛미디어", "(부서)IT1팀"]

url = vcard.add("URL")  # 홈페이지
url.value = "https://www.hanbit.co.kr/"
print(vcard.serialize())

from pathlib import Path

from step_1_1 import OUT_DIR

with open(OUT_DIR / f"{Path(__file__).stem}.vcf", "w", encoding="utf-8") as fp:
    fp.write(vcard.serialize())

import qrcode

qr = qrcode.make(vcard.serialize())
qr.save(OUT_DIR / f"{Path(__file__).stem}.png")
