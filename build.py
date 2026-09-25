from pathlib import Path
import re, urllib.request, html, shutil
from PIL import Image

root = Path(__file__).parent
out = root / 'dist'

css = (root / 'fonts-download.css').read_text(encoding='utf-8')
for i, url in enumerate(re.findall(r'url\((https[^)]+)\)', css)):
    name = f'thai-{i}.ttf'
    font_file = out / 'assets' / name
    if not font_file.exists():
        urllib.request.urlretrieve(url, font_file)
    css = css.replace(url, 'assets/' + name)
(out / 'fonts.css').write_text(css, encoding='utf-8')

D = [
    dict(
        id='thawiwat',
        number=2,
        mock=False,
        degree='ผศ.ดร.',
        name='ทวีวัฒน์ ทัศนวัฒน์',
        role='อดีตคณบดี คณะสัตวแพทยศาสตร์',
        role2='รองประธานกรรมการ สอ.มก.',
        lead='ประสบการณ์บริหารมหาวิทยาลัย\nและงานสหกรณ์',
        intro='จากงานบริหารคณะสัตวแพทยศาสตร์ สู่การทำงานในคณะกรรมการ สอ.มก. หลายด้าน ทั้งการบริหาร การเงิน เงินกู้ และการบริหารความเสี่ยง',
        edu=[
            ('2510', 'ม.ศ. 5 โรงเรียนขอนแก่นวิทยายน'),
            ('2516', 'สพ.บ. มหาวิทยาลัยเกษตรศาสตร์'),
            ('2533', 'Dr. Agr. Sci. · Nagoya University, Japan'),
        ],
        jobs=[
            ('2538–2546', 'คณบดี คณะสัตวแพทยศาสตร์', 'มหาวิทยาลัยเกษตรศาสตร์'),
            ('2547–2569', 'กรรมการ สอ.มก. หลายวาระ', 'ดำรงตำแหน่งในช่วง 2547–2550, 2552–2555, 2558–2561, 2563–2566 และ 2568–2569'),
        ],
        experience=[
            'ประธานกรรมการบริหาร',
            'ประธานกรรมการการศึกษาและประชาสัมพันธ์',
            'กรรมการบริหารการเงิน',
            'กรรมการเงินกู้',
            'กรรมการบริหารความเสี่ยง',
            'กรรมการธรรมาภิบาล',
            'กรรมการพัฒนาเทคโนโลยี',
        ],
        policies_original=[
            ('สมาชิกมีส่วนร่วม', 'ผลักดันการมีส่วนร่วมของสมาชิกในการบริหาร สอ.มก.'),
            ('ส่งเสริมการออมหุ้น', 'ขับเคลื่อนการออมหุ้นตามศักยภาพของสมาชิก'),
            ('สวัสดิการที่ดีขึ้น', 'ปรับปรุงระบบสวัสดิการ บนหลักการช่วยเหลือตนเองและช่วยเหลือซึ่งกันและกัน'),
            ('เติบโตอย่างมั่นคง', 'ขับเคลื่อน สอ.มก. ให้เติบโตอย่างมั่นคง ด้วยความซื่อสัตย์สุจริต'),
        ],
        policies_v1_new=[
            ('สมาชิกมีส่วนร่วม', 'ผลักดัน “การมีส่วนร่วม” ของสมาชิกในการบริหาร สอ.มก.'),
            ('ส่งเสริมการออมหุ้น', 'ขับเคลื่อน “การออมหุ้น” ตามศักยภาพของสมาชิก'),
            ('สวัสดิการที่ดีขึ้น', 'ปรับปรุงระบบสวัสดิการเพื่อให้สมาชิกได้รับสวัสดิการที่ดีขึ้น บนหลักการ “การช่วยเหลือตนเอง และ การช่วยเหลือซึ่งกันและกัน” ซึ่งเป็นหลักการสำคัญของสหกรณ์'),
            ('เติบโตอย่างมั่นคง', '“ขับเคลื่อน” สอ.มก.ให้เติบโตอย่างมั่นคง ด้วยความซื่อสัตย์สุจริต'),
        ],
        policies=[
            ('สมาชิกมีส่วนร่วม', 'ผลักดันการมีส่วนร่วมของสมาชิกในการบริหาร สอ.มก.'),
            ('ส่งเสริมการออมหุ้น', 'ขับเคลื่อนการออมหุ้นตามศักยภาพของสมาชิก'),
            ('สวัสดิการที่ดีขึ้น', 'ปรับปรุงระบบสวัสดิการ บนหลักการช่วยเหลือตนเองและช่วยเหลือซึ่งกันและกัน'),
            ('เติบโตอย่างมั่นคง', 'ขับเคลื่อน สอ.มก. ให้เติบโตอย่างมั่นคง ด้วยความซื่อสัตย์สุจริต'),
        ],
        bio='เกิดและจบการศึกษาระดับมัธยมปลายที่จังหวัดขอนแก่น หลังสำเร็จการศึกษาคณะสัตวแพทยศาสตร์ มหาวิทยาลัยเกษตรศาสตร์ บรรจุเป็นอาจารย์โท สังกัดภาควิชาศัลยศาสตร์ในปี 2516 และย้ายไปปฏิบัติงานที่วิทยาเขตกำแพงแสนในปี 2522 จนเกษียณอายุราชการ.',
    ),
    dict(
        id='thawatchai',
        number=3,
        mock=False,
        degree='ผศ.น.สพ.ดร.',
        name='ธวัชชัย ศักดิ์ภู่อร่าม',
        role='อดีตคณบดี คณะสัตวแพทยศาสตร์',
        role2='รองประธานกรรมการ สอ.มก.',
        lead='ประสบการณ์บริหารมหาวิทยาลัย\nและงานสหกรณ์',
        intro='จากบทบาทคณบดีคณะสัตวแพทยศาสตร์ และนายกสัตวแพทยสภา สู่การทำงานในคณะกรรมการ สอ.มก. ด้านการบริหารความเสี่ยงและการเงิน เพื่อความมั่นคงยั่งยืนของสมาชิก',
        edu=[
            ('2518', 'วิทยาศาสตรบัณฑิต (วท.บ.) · มหาวิทยาลัยเกษตรศาสตร์'),
            ('2519', 'สัตวแพทยศาสตรบัณฑิต (สพ.บ.) · มหาวิทยาลัยเกษตรศาสตร์'),
            ('2526', 'สาธารณสุขศาสตรมหาบัณฑิต (สม.) · มหาวิทยาลัยมหิดล'),
            ('2533', 'Ph.D.(Veterinary Science),Japan'),
        ],
        jobs=[
            ('2550–2554', 'คณบดี คณะสัตวแพทยศาสตร์', 'มหาวิทยาลัยเกษตรศาสตร์ (รองคณบดี พ.ศ. 2539–2541)'),
            ('2551–2553', 'กรรมการสภามหาวิทยาลัยเกษตรศาสตร์', 'มหาวิทยาลัยเกษตรศาสตร์'),
            ('2561–2563', 'นายกสัตวแพทยสภาแห่งประเทศไทย', 'สัตวแพทยสภาแห่งประเทศไทย'),
            ('สหกรณ์', 'รองประธานกรรมการ และกรรมการดำเนินการ สอ.มก.', 'สหกรณ์ออมทรัพย์มหาวิทยาลัยเกษตรศาสตร์ จำกัด'),
        ],
        experience=[
            'รองประธานกรรมการ สอ.มก.',
            'ประธานบริหารความเสี่ยง สอ.มก.',
            'กรรมการบริหาร สอ.มก.',
            'กรรมการเงินกู้ สอ.มก.',
            'กรรมการศึกษาและประชาสัมพันธ์ สอ.มก.',
            'กรรมการสภามหาวิทยาลัยเกษตรศาสตร์ (พ.ศ. 2551–2553)',
            'นายกสัตวแพทยสภาแห่งประเทศไทย (พ.ศ. 2561–2563)',
        ],
        policies_original=[
            ('บริหารความเสี่ยงทั่วทั้งองค์กร', 'ใช้ระบบบริหารความเสี่ยงทั่วทั้งองค์กร เพื่อความมั่นคงยั่งยืนของ สอ.มก. และสมาชิก'),
            ('พัฒนาระบบ IT และบริการสินเชื่อ', 'พัฒนาระบบ IT เพื่อการติดต่อสื่อสารกับสมาชิก โดยเฉพาะช่องทางบริการสินเชื่อ ให้สะดวก รวดเร็ว'),
            ('ป้องกันภัยไซเบอร์', 'เพิ่มการป้องกันภัยโจมตีทางไซเบอร์ และการแฮกข้อมูลของ สอ.มก. และของสมาชิก'),
            ('เงินทุนสำรองมั่นคง', 'เงินทุนสำรองไม่ต่ำกว่าเกณฑ์มาตรฐานตามกฎหมาย'),
            ('ธรรมาภิบาลและจรรยาบรรณ', 'นำระบบธรรมาภิบาล และการมีจรรยาบรรณทุกภาคส่วน เพื่อการบริหาร สอ.มก.'),
            ('ส่งเสริมความรู้สมาชิก', 'ส่งเสริมการสัมมนา และการให้ความรู้ด้านเศรษฐกิจ สังคม สาธารณสุขแก่สมาชิกอย่างต่อเนื่อง'),
        ],
        policies_v1_new=[
            ('บริหารความเสี่ยงทั่วทั้งองค์กร', 'ใช้ระบบบริหารความเสี่ยงทั่วทั้งองค์กร เพื่อความมั่นคงยั่งยืนของ สอ.มก. และสมาชิก'),
            ('พัฒนาระบบ IT และบริการสินเชื่อ', 'พัฒนาระบบ IT เพื่อการติดต่อสื่อสารกับสมาชิก โดยเฉพาะช่องทางบริการสินเชื่อ ให้สะดวก รวดเร็ว'),
            ('ป้องกันภัยไซเบอร์', 'เพิ่มการป้องกันภัยโจมตีทางไซเบอร์ และการแฮกข้อมูลของ สอ.มก. และของสมาชิก'),
            ('เงินทุนสำรองมั่นคง', 'เงินทุนสำรองไม่ต่ำกว่าเกณฑ์มาตรฐานตามกฎหมาย'),
            ('ธรรมาภิบาลและจรรยาบรรณ', 'นำระบบธรรมาภิบาล และการมีจรรยาบรรณทุกภาคส่วน เพื่อการบริหาร สอ.มก.'),
            ('ส่งเสริมความรู้สมาชิก', 'ส่งเสริมการสัมมนา และการให้ความรู้ด้านเศรษฐกิจ สังคม สาธารณสุขแก่สมาชิกอย่างต่อเนื่อง'),
        ],
        policies=[
            ('บริหารความเสี่ยงทั่วทั้งองค์กร', 'ใช้ระบบบริหารความเสี่ยงทั่วทั้งองค์กร เพื่อความมั่นคงยั่งยืนของ สอ.มก. และสมาชิก'),
            ('พัฒนาระบบ IT และบริการสินเชื่อ', 'พัฒนาระบบ IT เพื่อการติดต่อสื่อสารกับสมาชิก โดยเฉพาะช่องทางบริการสินเชื่อ ให้สะดวก รวดเร็ว'),
            ('ป้องกันภัยไซเบอร์', 'เพิ่มการป้องกันภัยโจมตีทางไซเบอร์ และการแฮกข้อมูลของ สอ.มก. และของสมาชิก'),
            ('เงินทุนสำรองมั่นคง', 'เงินทุนสำรองไม่ต่ำกว่าเกณฑ์มาตรฐานตามกฎหมาย'),
            ('ธรรมาภิบาลและจรรยาบรรณ', 'นำระบบธรรมาภิบาล และการมีจรรยาบรรณทุกภาคส่วน เพื่อการบริหาร สอ.มก.'),
            ('ส่งเสริมความรู้สมาชิก', 'ส่งเสริมการสัมมนา และการให้ความรู้ด้านเศรษฐกิจ สังคม สาธารณสุขแก่สมาชิกอย่างต่อเนื่อง'),
        ],
        bio='เกิดที่จังหวัดนครสวรรค์ รับราชการที่คณะสัตวแพทยศาสตร์ มหาวิทยาลัยเกษตรศาสตร์ ตั้งแต่ปี พ.ศ. 2520 จนเกษียณอายุราชการในตำแหน่งคณบดีคณะสัตวแพทยศาสตร์.',
    ),
    dict(
        id='rangsarn',
        number=4,
        mock=False,
        degree='ผศ.ดร.',
        name='รังสรรค์ ปีติปัญญา',
        role='อดีตรองอธิการบดี มก.',
        role2='อดีตรองประธานกรรมการ สอ.มก.',
        lead='ทำงานด้านสหกรณ์\nมากกว่า 40 ปี',
        intro='ประสบการณ์ด้านเศรษฐศาสตร์สหกรณ์ งานบริหารมหาวิทยาลัย และการทำงานกับองค์กรสหกรณ์มาอย่างยาวนาน',
        edu=[
            ('ปริญญาตรี', 'เศรษฐศาสตร์สหกรณ์ · มหาวิทยาลัยเกษตรศาสตร์'),
            ('ปริญญาโท', 'เศรษฐศาสตร์เกษตร · มหาวิทยาลัยเกษตรศาสตร์'),
            ('ปริญญาเอก', 'เศรษฐศาสตร์เกษตร · Tokyo University of Agriculture, Japan'),
        ],
        jobs=[
            ('มหาวิทยาลัย', 'งานบริหารมหาวิทยาลัยเกษตรศาสตร์', 'หัวหน้าภาควิชาสหกรณ์ · ผู้อำนวยการสำนักหอสมุด · กรรมการสภา มก. · รองอธิการบดีฝ่ายการเงินและทรัพย์สิน'),
            ('สหกรณ์', 'งานบริหารและพัฒนาสหกรณ์', 'รองประธาน สอ.มก. · รองประธานชุมนุมสหกรณ์ออมทรัพย์แห่งประเทศไทย · กรรมการกองทุนพัฒนาสหกรณ์'),
        ],
        experience=[
            'ทำงานด้านสหกรณ์มากกว่า 40 ปี',
            'เขียนหนังสือและบทความด้านสหกรณ์จำนวนมาก',
        ],
        policies_original=[
            ('ปันผลและเฉลี่ยคืน', 'มุ่งรักษาระดับอัตราเงินปันผลและเฉลี่ยคืนในระดับสูงอย่างต่อเนื่อง'),
            ('บริการและสวัสดิการ', 'พัฒนาบริการและสวัสดิการที่สอดรับกับความต้องการของสมาชิกและสังคมสูงวัย'),
            ('แก้ปัญหาหนี้สิน', 'รวมและลดหนี้ ปรับระยะเวลาและวิธีชำระหนี้ พร้อมโครงการช่วยเหลือสมาชิกที่มีปัญหาหนี้สินรุนแรงและผู้ค้ำอย่างเป็นรูปธรรม'),
            ('ลงทุนอย่างรอบคอบ', 'บริหารเงินและลงทุนด้วยความระมัดระวัง เพื่อสร้างผลตอบแทนที่ดีและมั่นคง'),
        ],
        policies_v1_new=[
            ('ปันผลและเฉลี่ยคืน', 'รักษาระดับอัตราเงินปันผลและเฉลี่ยคืนในระดับสูงอย่างต่อเนื่อง'),
            ('บริการและสวัสดิการ', 'พัฒนาบริการและสวัสดิการที่สอดรับกับความต้องการของสมาชิกและสังคมสูงวัย'),
            ('แก้ปัญหาหนี้สิน', 'แก้ปัญหาหนี้สินโดยการรวม ลด และ ปรับระยะเวลาและวิธีการชำระหนี้ รวมถึงทำโครงการช่วยเหลือสมาชิกที่มีปัญหาหนี้สินรุนแรง และช่วยเหลือผู้ค้ำอย่างเป็นรูปธรรม'),
            ('บริหารเงินและลงทุน', 'บริหารเงินและลงทุนด้วยความระมัดระวังเพื่อสร้างผลตอบแทนที่ดีและมั่นคง'),
        ],
        policies=[
            ('ปันผลและเฉลี่ยคืน', 'มุ่งรักษาระดับอัตราเงินปันผลและเฉลี่ยคืนในระดับสูงอย่างต่อเนื่อง'),
            ('บริการและสวัสดิการ', 'พัฒนาบริการและสวัสดิการที่สอดรับกับความต้องการของสมาชิกและสังคมสูงวัย'),
            ('แก้ปัญหาหนี้สิน', 'รวมและลดหนี้ ปรับระยะเวลาและวิธีชำระหนี้ พร้อมโครงการช่วยเหลือสมาชิกที่มีปัญหาหนี้สินรุนแรงและผู้ค้ำอย่างเป็นรูปธรรม'),
            ('ลงทุนอย่างรอบคอบ', 'บริหารเงินและลงทุนด้วยความระมัดระวัง เพื่อสร้างผลตอบแทนที่ดีและมั่นคง'),
        ],
        bio='ข้าราชการเกษียณ ภาควิชาสหกรณ์ คณะเศรษฐศาสตร์ มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตบางเขน ทำงานด้านสหกรณ์มามากกว่า 40 ปี.',
    ),
]

# Approved campaign artwork.  Keep the filenames stable so the published
# gallery can be refreshed simply by replacing the source files in /final.
MEDIA = [
    ('020304-หน้าตรง-กากบาทแดง-qr-final.png', 'โปสเตอร์ผู้สมัครทั้ง 3 ท่าน'),
    ('poster-กอดอก-พร้อม-QR-20260923-v4.png', 'โปสเตอร์ผู้สมัครทั้ง 3 ท่าน แบบกอดอก'),
    ('thawiwat-infographic-v5.png', 'อินโฟกราฟิก หมายเลข 2 · ทวีวัฒน์ ทัศนวัฒน์'),
    ('thawatchai-infographic-v6.png', 'อินโฟกราฟิก หมายเลข 3 · ธวัชชัย ศักดิ์ภู่อร่าม'),
    ('rangsarn-infographic-v10-reference-layout-20260924.png', 'อินโฟกราฟิก หมายเลข 4 · รังสรรค์ ปีติปัญญา'),
    ('ปกหลัง-ดีไซน์ใหม่-2026-09-21.png', 'โปสเตอร์นโยบาย ดีไซน์ใหม่'),
]

final_artwork = root.parent / 'exports2026-09-25' / 'final'
media_dir = out / 'assets' / 'media'
media_dir.mkdir(parents=True, exist_ok=True)
for filename, _ in MEDIA:
    source = final_artwork / filename
    if not source.is_file():
        raise FileNotFoundError(f'Missing approved artwork: {source}')
    shutil.copy2(source, media_dir / filename)

# Ensure WebP assets exist
for d in D:
    jpg_file = out / 'assets' / f"{d['id']}.jpg"
    webp_file = out / 'assets' / f"{d['id']}.webp"
    if jpg_file.exists() and not webp_file.exists():
        with Image.open(jpg_file) as im:
            im.save(webp_file, 'WEBP', quality=85, method=6)

def head(title, desc, prefix='', is_new_v1=False):
    css_file = f"{prefix}style-v1.css?v=3" if is_new_v1 else f"{prefix}style.css?v=9"
    version_badge = '<span class="version-badge" title="เวอร์ชันปรับปรุงเลย์เอาต์ใหม่">v1 (ใหม่)</span>' if is_new_v1 else ''
    return f'''<!doctype html><html lang="th"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{desc}"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23123f35'/%3E%3Cpath d='M8 23V10h4v13m4 0V6h4v17m4 0V13h3v10' stroke='%23d9be7c' stroke-width='2'/%3E%3C/svg%3E"><link rel="stylesheet" href="{prefix}fonts.css"><link rel="stylesheet" href="{css_file}"></head><body><a class="skip" href="#main">ข้ามไปเนื้อหา</a><header><a class="brand" href="index.html"><span class="brandmark">สอ.มก.</span><span>สมาชิกก้าวหน้า<small>สอ.มก.มั่นคง {version_badge}</small></span></a></header>'''

def get_footer(is_new_v1=False):
    if is_new_v1:
        footer_text = 'ผู้สมัครกรรมการ สายวิชาการ · ประจำปี 2570'
    else:
        footer_text = 'ผู้สมัครกรรมการ สายวิชาการ · ประจำปี 2570 · เปรียบเทียบ: <a href="v1/index.html" style="text-decoration:underline;">v1 (ตราเขียวทอง) ↗</a> | <a href="v2/index.html" style="text-decoration:underline;">v2 (ChatGPT) ↗</a>'
    return f'<footer><span>{footer_text}</span><span>ข้อมูลเรียบเรียงจากประวัติและแนวคิดที่ผู้สมัครส่งมา</span></footer></body></html>'

def generate_site(target_dir: Path, asset_prefix: str = '', is_new_v1: bool = False):
    target_dir.mkdir(parents=True, exist_ok=True)
    cards = ''
    for i, d in enumerate(D):
        mock_badge = '<span class="mock-badge">ข้อมูลตัวอย่าง</span>' if d['mock'] else ''
        if is_new_v1:
            img_loading = 'loading="eager" fetchpriority="high" decoding="async"' if i == 0 else 'loading="lazy" decoding="async"'
            cards += f'''<a class="candidate" href="{d['id']}.html"><div class="portrait"><picture><source srcset="{asset_prefix}assets/{d['id']}.webp" type="image/webp"><img src="{asset_prefix}assets/{d['id']}.jpg" alt="{d['degree']}{d['name']}" width="550" height="740" {img_loading}></picture></div><div class="cardbody">{mock_badge}<div class="cardhead"><div class="cardtitles"><p class="degree">{d['degree']}</p><h2>{d['name']}</h2></div><div class="official-seal card-seal" aria-label="หมายเลขผู้สมัคร {d['number']}"><span class="seal-label">หมายเลข</span><strong class="seal-num">{d['number']}</strong></div></div><p>{d['role']}<br>{d['role2']}</p><span class="read">ดูประวัติและแนวคิด <span aria-hidden="true">↗</span></span></div></a>'''
        else:
            cards += f'''<a class="candidate" href="{d['id']}.html"><div class="portrait"><img src="{asset_prefix}assets/{d['id']}.jpg" alt="{d['degree']}{d['name']}" width="550" height="740"></div><div class="cardbody">{mock_badge}<div class="cardhead"><div class="cardtitles"><p class="degree">{d['degree']}</p><h2>{d['name']}</h2></div><span class="ballot" aria-label="หมายเลขผู้สมัคร {d['number']}"><span>หมายเลข</span><strong>{d['number']}</strong></span></div><p>{d['role']}<br>{d['role2']}</p><span class="read">ดูประวัติและแนวคิด <span aria-hidden="true">↗</span></span></div></a>'''

    (target_dir / 'index.html').write_text(
        head('รู้จักผู้สมัครกรรมการ สอ.มก. 2570', 'ประวัติ ประสบการณ์ และแนวคิดในการทำงานของผู้สมัครกรรมการ สอ.มก. ประจำปี 2570', asset_prefix, is_new_v1=is_new_v1) +
        f'''<main id="main"><section class="intro"><p class="eyebrow">การสรรหากรรมการดำเนินการ · 2570</p><h1>รู้จักผู้สมัคร<br><span>ผ่านประสบการณ์และแนวคิด</span></h1><p class="intro-text">สหกรณ์ออมทรัพย์มหาวิทยาลัยเกษตรศาสตร์ จำกัด</p></section><section class="candidate-directory" id="candidates" aria-labelledby="candidate-group-title"><div class="candidate-group-title"><p class="eyebrow">ผู้สมัครกรรมการ</p><h2 id="candidate-group-title">สายวิชาการ</h2></div><div class="candidates">{cards}</div></section><div class="closing"><span>สมาชิกก้าวหน้า</span><strong>สอ.มก.มั่นคง</strong></div></main>''' +
        get_footer(is_new_v1=is_new_v1),
        encoding='utf-8'
    )

    gallery_items = ''.join(
        f'''<button class="media-card" type="button" data-src="{asset_prefix}assets/media/{filename}" data-label="{label}" aria-label="เปิด {label}"><img src="{asset_prefix}assets/media/{filename}" alt=""{' fetchpriority="high"' if i == 0 else ' loading="lazy"'} decoding="async"><span>{label}</span></button>'''
        for i, (filename, label) in enumerate(MEDIA)
    )
    modal_script = '''<script>(() => { const cards = [...document.querySelectorAll('.media-card')]; const dialog = document.querySelector('.media-modal'); if (!cards.length || !dialog) return; const image = dialog.querySelector('.modal-image'), download = dialog.querySelector('.modal-download'), fullscreen = dialog.querySelector('.modal-fullscreen'); let current = 0, startX = 0; const show = index => { current = (index + cards.length) % cards.length; const card = cards[current]; image.src = card.dataset.src; image.alt = card.dataset.label; download.href = card.dataset.src; download.setAttribute('download', card.dataset.label); }; const open = index => { show(index); dialog.showModal(); }; const updateFullscreenLabel = () => fullscreen.setAttribute('aria-label', document.fullscreenElement ? 'ออกจากโหมดเต็มจอ' : 'ดูเต็มจอ'); cards.forEach((card, index) => card.addEventListener('click', () => open(index))); dialog.querySelector('[data-direction="previous"]').addEventListener('click', () => show(current - 1)); dialog.querySelector('[data-direction="next"]').addEventListener('click', () => show(current + 1)); dialog.querySelector('.modal-close').addEventListener('click', () => dialog.close()); fullscreen.addEventListener('click', async () => { if (!document.fullscreenElement) await dialog.requestFullscreen?.(); else await document.exitFullscreen?.(); }); document.addEventListener('fullscreenchange', updateFullscreenLabel); dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); }); dialog.addEventListener('keydown', event => { if (event.key === 'ArrowLeft') { event.preventDefault(); show(current - 1); } if (event.key === 'ArrowRight') { event.preventDefault(); show(current + 1); } }); dialog.addEventListener('touchstart', event => startX = event.changedTouches[0].screenX, { passive: true }); dialog.addEventListener('touchend', event => { const distance = event.changedTouches[0].screenX - startX; if (Math.abs(distance) > 40) show(current + (distance < 0 ? 1 : -1)); }, { passive: true }); })();</script>'''
    (target_dir / 'media.html').write_text(
        head('สื่อประชาสัมพันธ์ทั้งหมด | ผู้สมัครกรรมการ สอ.มก. 2570', 'รวมโปสเตอร์และอินโฟกราฟิกผู้สมัครกรรมการ สอ.มก. ประจำปี 2570', asset_prefix, is_new_v1=is_new_v1) +
        f'''<main id="main"><section class="media-intro"><p class="eyebrow">สื่อประชาสัมพันธ์ · 2570</p><h1>โปสเตอร์และ<br><span>อินโฟกราฟิกทั้งหมด</span></h1><p>คลิกภาพเพื่อเปิดดูแบบสไลด์และดาวน์โหลดไฟล์</p></section><section class="media-grid" aria-label="โปสเตอร์และอินโฟกราฟิก">{gallery_items}</section></main><dialog class="media-modal" aria-label="แสดงภาพสื่อประชาสัมพันธ์"><button class="modal-close" type="button" aria-label="ปิด">×</button><button class="modal-fullscreen" type="button" aria-label="ดูเต็มจอ"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 14H5v5h5v-2H7v-3m0-4h3V7H5v5h2v-2m10 7h-3v2h5v-5h-2v3m0-10V5h-5v2h3v3h2z"/></svg></button><a class="modal-download" href="#" download aria-label="ดาวน์โหลดภาพ"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 9h-4V3H9v6H5l7 7 7-7M5 20v-2h14v2H5z"/></svg></a><div class="modal-view"><button type="button" data-direction="previous" aria-label="ภาพก่อนหน้า">‹</button><img class="modal-image" src="" alt=""><button type="button" data-direction="next" aria-label="ภาพถัดไป">›</button></div></dialog>{modal_script}''' +
        get_footer(is_new_v1=is_new_v1),
        encoding='utf-8'
    )

    for d in D:
        policy_list = d.get('policies_v1_new', d['policies']) if is_new_v1 else d.get('policies_original', d['policies'])
        policies = ''.join(f'<article class="policy"><span class="number">0{i+1}</span><div><h3>{h}</h3><p>{p}</p></div></article>' for i, (h, p) in enumerate(policy_list))
        jobs = ''.join(f'<div class="timeline-row"><span>{y}</span><div><h3>{h}</h3><p>{p}</p></div></div>' for y, h, p in d['jobs'])
        edu = ''.join(f'<li><span>{y}</span><strong>{p}</strong></li>' for y, p in d['edu'])
        exp = ''.join(f'<li>{x}</li>' for x in d['experience'])
        others = [x for x in D if x != d]
        if is_new_v1:
            other_links = ''.join(f'<a href="{o["id"]}.html"><span class="next-badge">หมายเลข {o["number"]}</span> <span class="next-name">{o["degree"]}{o["name"]}</span> <span class="next-arrow" aria-hidden="true">↗</span></a>' for o in others)
        else:
            other_links = ''.join(f'<a href="{o["id"]}.html"><span class="next-badge">หมายเลข {o["number"]}</span> {o["degree"]}{o["name"]} <span aria-hidden="true">↗</span></a>' for o in others)
        mock_notice = '<div class="mock-notice"><strong>ข้อมูลตัวอย่าง</strong><span>ประวัติ การศึกษา และแนวคิด ใช้ข้อมูลของ อ.ทวีวัฒน์ ทัศนวัฒน์ ชั่วคราว ระหว่างรอข้อมูลจริงของ อ.ธวัชชัย</span></div>' if d['mock'] else ''
        infographic_file = {
            'thawiwat': 'media/thawiwat-infographic-v5.png',
            'thawatchai': 'media/thawatchai-infographic-v6.png',
            'rangsarn': 'media/rangsarn-infographic-v10-reference-layout-20260924.png',
        }.get(d['id'], f"{d['id']}-infographic-v4.png")
        infographic_label = 'ดาวน์โหลดอินโฟกราฟิกตัวอย่าง' if d['mock'] else 'ดาวน์โหลดอินโฟกราฟิก'
        download = f'<div class="download"><a class="button" href="{asset_prefix}assets/{infographic_file}" download>{infographic_label} <span aria-hidden="true">↓</span></a></div>'
        
        if is_new_v1:
            hero_html = f'''<div class="identity-lockup"><div class="official-seal profile-seal" aria-label="หมายเลขผู้สมัคร {d['number']}"><span class="seal-label">หมายเลข</span><strong class="seal-num">{d['number']}</strong><span class="seal-track">สายวิชาการ</span></div><div class="identity-info"><p class="eyebrow">ผู้สมัครกรรมการ สายวิชาการ · 2570</p><h1 class="candidate-fullname"><span class="degree-prefix">{d['degree']}</span>{d['name']}</h1><p class="candidate-roles">{d['role']}<br>{d['role2']}</p></div></div><div class="hero-line"></div><h2>{d['lead'].replace(chr(10), '<br>')}</h2><p class="profile-intro">{d['intro']}</p><a class="button" href="#ideas">แนวคิดในการทำงาน <span aria-hidden="true">↓</span></a></div><div class="profile-photo"><picture><source srcset="{asset_prefix}assets/{d['id']}.webp" type="image/webp"><img src="{asset_prefix}assets/{d['id']}.jpg" alt="{d['degree']}{d['name']}" width="550" height="790" fetchpriority="high" decoding="async"></picture></div>'''
        else:
            hero_html = f'''<div class="profile-hero-top"><div class="profile-titles"><p class="eyebrow">ผู้สมัครกรรมการ สายวิชาการ · 2570</p><p class="degree">{d['degree']}</p><h1>{d['name'].replace(' ', '<br>')}</h1></div><span class="ballot" aria-label="หมายเลขผู้สมัคร {d['number']}"><span>หมายเลข</span><strong>{d['number']}</strong></span></div><p class="role">{d['role']}<br>{d['role2']}</p><div class="hero-line"></div><h2>{d['lead'].replace(chr(10), '<br>')}</h2><p>{d['intro']}</p><a class="button" href="#ideas">แนวคิดในการทำงาน <span aria-hidden="true">↓</span></a></div><div class="profile-photo"><img src="{asset_prefix}assets/{d['id']}.jpg" alt="{d['degree']}{d['name']}" width="550" height="790"></div>'''

        page = f'''<main id="main"><a class="back" href="index.html#candidates">← ผู้สมัครทั้งหมด</a>{mock_notice}<section class="profile-hero"><div class="profile-copy">{hero_html}</section><nav class="section-nav" aria-label="หัวข้อประวัติ"><a href="#ideas">แนวคิด</a><a href="#experience">ประสบการณ์</a><a href="#education">การศึกษา</a></nav><section class="section" id="ideas"><div class="section-heading"><span class="eyebrow">แนวคิดในการทำงาน</span><h2>{len(policy_list)} แนวทางเพื่อสมาชิก</h2></div><div class="policy-grid">{policies}</div></section><section class="section experience" id="experience"><div class="section-heading"><span class="eyebrow">ประสบการณ์</span><h2>งานที่ผ่านมา</h2></div><div>{jobs}<details><summary>อ่านประสบการณ์เพิ่มเติม</summary><ul class="experience-list">{exp}</ul><p>{d['bio']}</p></details></div></section><section class="section education" id="education"><div class="section-heading"><span class="eyebrow">ประวัติการศึกษา</span><h2>พื้นฐานความรู้</h2></div><ul class="education-list">{edu}</ul></section>{download}<aside class="next"><span>รู้จักผู้สมัครท่านอื่น</span><div class="next-links">{other_links}</div></aside></main>'''
        
        html_content = head(f"หมายเลข {d['number']} · {d['degree']}{d['name']} | ผู้สมัครกรรมการ สอ.มก. 2570", d['lead'].replace('\n', ' '), asset_prefix, is_new_v1=is_new_v1) + page + get_footer(is_new_v1=is_new_v1)
        (target_dir / f"{d['id']}.html").write_text(html_content, encoding='utf-8')
        
        # If rangsarn, also create rangsan.html alias
        if d['id'] == 'rangsarn':
            (target_dir / 'rangsan.html').write_text(html_content, encoding='utf-8')

# 1. Generate root site (ของเดิม)
generate_site(out, asset_prefix='', is_new_v1=False)

# 2. Generate /v1/ site (ของใหม่)
generate_site(out / 'v1', asset_prefix='../', is_new_v1=True)

# Make v1 the public entry point while retaining the other versions at their
# existing URLs for comparison and backwards compatibility.
(out / 'index.html').write_text('''<!doctype html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="0; url=v1/index.html">
  <link rel="canonical" href="https://sertjerm.github.io/committee-poster/v1/">
  <title>รู้จักผู้สมัครกรรมการ สอ.มก. 2570</title>
</head>
<body>
  <p>กำลังเปิดหน้าเว็บไซต์หลัก… <a href="v1/index.html">ไปยังเว็บไซต์</a></p>
  <script>location.replace('v1/index.html');</script>
</body>
</html>
''', encoding='utf-8')

print('Build completed successfully.')
