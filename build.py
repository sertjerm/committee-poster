from pathlib import Path
import re, urllib.request, html

root = Path(__file__).parent
out = root / 'dist'

css = (root / 'fonts-download.css').read_text()
for i, url in enumerate(re.findall(r'url\((https[^)]+)\)', css)):
    name = f'thai-{i}.ttf'
    font_file = out / 'assets' / name
    if not font_file.exists():
        urllib.request.urlretrieve(url, font_file)
    css = css.replace(url, 'assets/' + name)
(out / 'fonts.css').write_text(css)

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
        mock=True,
        degree='ผศ.น.สพ.ดร.',
        name='ธวัชชัย ศักดิ์ภู่อร่าม',
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
            'ประธานบริหารความเสี่ยง',
            'กรรมการบริหาร',
            'กรรมการเงินกู้',
            'กรรมการศึกษาและประชาสัมพันธ์',
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
        id='rangsarn',
        number=4,
        mock=False,
        degree='ผศ.ดร.',
        name='รังสรรค์ ปีติปัญญา',
        role='อดีตรองอธิการบดี มก.',
        role2='อดีตรองประธานกรรมการ สอ.มก.',
        lead='ศึกษาและทำงานด้านสหกรณ์\nมากกว่า 40 ปี',
        intro='ประสบการณ์ด้านเศรษฐศาสตร์สหกรณ์ งานบริหารมหาวิทยาลัย และการทำงานกับองค์กรสหกรณ์ พร้อมแนวคิดพัฒนาบริการและสวัสดิการให้สอดรับกับสมาชิก',
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
            'ศึกษาและทำงานด้านสหกรณ์มากกว่า 40 ปี',
            'เขียนหนังสือและบทความด้านสหกรณ์จำนวนมาก',
        ],
        policies=[
            ('ปันผลและเฉลี่ยคืน', 'มุ่งรักษาระดับอัตราเงินปันผลและเฉลี่ยคืนในระดับสูงอย่างต่อเนื่อง'),
            ('บริการและสวัสดิการ', 'พัฒนาบริการและสวัสดิการที่สอดรับกับความต้องการของสมาชิกและสังคมสูงวัย'),
            ('แก้ปัญหาหนี้สิน', 'รวมและลดหนี้ ปรับระยะเวลาและวิธีชำระหนี้ พร้อมโครงการช่วยเหลือสมาชิกที่มีปัญหาหนี้สินรุนแรงและผู้ค้ำอย่างเป็นรูปธรรม'),
            ('ลงทุนอย่างรอบคอบ', 'บริหารเงินและลงทุนด้วยความระมัดระวัง เพื่อสร้างผลตอบแทนที่ดีและมั่นคง'),
        ],
        bio='ข้าราชการเกษียณ ภาควิชาสหกรณ์ คณะเศรษฐศาสตร์ มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตบางเขน ศึกษาและทำงานด้านสหกรณ์มามากกว่า 40 ปี.',
    ),
]

def head(title, desc):
    return f'''<!doctype html><html lang="th"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{desc}"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23123f35'/%3E%3Cpath d='M8 23V10h4v13m4 0V6h4v17m4 0V13h3v10' stroke='%23d9be7c' stroke-width='2'/%3E%3C/svg%3E"><link rel="stylesheet" href="fonts.css"><link rel="stylesheet" href="style.css"></head><body><a class="skip" href="#main">ข้ามไปเนื้อหา</a><header><a class="brand" href="index.html"><span class="brandmark">สอ.มก.</span><span>สมาชิกก้าวหน้า<small>สอ.มก.มั่นคง</small></span></a><a class="all-link" href="index.html#candidates">รู้จักผู้สมัคร <span aria-hidden="true">↗</span></a></header>'''

footer = '<footer><span>ผู้สมัครกรรมการ สายวิชาการ · ประจำปี 2570</span><span>ข้อมูลเรียบเรียงจากประวัติและแนวคิดที่ผู้สมัครส่งมา</span></footer></body></html>'

cards = ''
for d in D:
    mock_badge = '<span class="mock-badge">ข้อมูลตัวอย่าง</span>' if d['mock'] else ''
    cards += f'''<a class="candidate" href="{d['id']}.html"><div class="portrait"><img src="assets/{d['id']}.jpg" alt="{d['degree']}{d['name']}" width="550" height="740"><span class="portrait-label">สายวิชาการ</span></div><div class="cardbody">{mock_badge}<div class="cardhead"><div class="cardtitles"><p class="degree">{d['degree']}</p><h2>{d['name']}</h2></div><span class="ballot" aria-label="หมายเลขผู้สมัคร {d['number']}"><span>หมายเลข</span><strong>{d['number']}</strong></span></div><p>{d['role']}<br>{d['role2']}</p><span class="read">ดูประวัติและแนวคิด <span aria-hidden="true">↗</span></span></div></a>'''

(out / 'index.html').write_text(
    head('รู้จักผู้สมัครกรรมการ สอ.มก. 2570', 'ประวัติ ประสบการณ์ และแนวคิดในการทำงานของผู้สมัครกรรมการ สอ.มก. ประจำปี 2570') +
    f'''<main id="main"><section class="intro"><p class="eyebrow">การสรรหากรรมการดำเนินการ · 2570</p><h1>รู้จักผู้สมัคร<br><span>ผ่านประสบการณ์และแนวคิด</span></h1><p class="intro-text">สหกรณ์ออมทรัพย์มหาวิทยาลัยเกษตรศาสตร์ จำกัด</p></section><section class="candidates" id="candidates" aria-label="ผู้สมัคร">{cards}</section><div class="closing"><span>สมาชิกก้าวหน้า</span><strong>สอ.มก.มั่นคง</strong></div></main>''' +
    footer
)

for d in D:
    policies = ''.join(f'<article class="policy"><span class="number">0{i+1}</span><div><h3>{h}</h3><p>{p}</p></div></article>' for i, (h, p) in enumerate(d['policies']))
    jobs = ''.join(f'<div class="timeline-row"><span>{y}</span><div><h3>{h}</h3><p>{p}</p></div></div>' for y, h, p in d['jobs'])
    edu = ''.join(f'<li><span>{y}</span><strong>{p}</strong></li>' for y, p in d['edu'])
    exp = ''.join(f'<li>{x}</li>' for x in d['experience'])
    others = [x for x in D if x != d]
    other_links = ''.join(f'<a href="{o["id"]}.html"><span class="next-badge">หมายเลข {o["number"]}</span> {o["degree"]}{o["name"]} <span aria-hidden="true">↗</span></a>' for o in others)
    mock_notice = '<div class="mock-notice"><strong>ข้อมูลตัวอย่าง</strong><span>ประวัติ การศึกษา และแนวคิด ใช้ข้อมูลของ อ.ทวีวัฒน์ ทัศนวัฒน์ ชั่วคราว ระหว่างรอข้อมูลจริงของ อ.ธวัชชัย</span></div>' if d['mock'] else ''
    infographic_file = f"{d['id']}-infographic-v2.png" if d['mock'] else f"{d['id']}-infographic-v1.png"
    infographic_label = 'ดาวน์โหลดอินโฟกราฟิกตัวอย่าง' if d['mock'] else 'ดาวน์โหลดอินโฟกราฟิก'
    
    page = f'''<main id="main"><a class="back" href="index.html#candidates">← ผู้สมัครทั้งหมด</a>{mock_notice}<section class="profile-hero"><div class="profile-copy"><div class="profile-hero-top"><div class="profile-titles"><p class="eyebrow">ผู้สมัครกรรมการ สายวิชาการ · 2570</p><p class="degree">{d['degree']}</p><h1>{d['name'].replace(' ', '<br>')}</h1></div><span class="ballot" aria-label="หมายเลขผู้สมัคร {d['number']}"><span>หมายเลข</span><strong>{d['number']}</strong></span></div><p class="role">{d['role']}<br>{d['role2']}</p><div class="hero-line"></div><h2>{d['lead'].replace(chr(10), '<br>')}</h2><p>{d['intro']}</p><a class="button" href="#ideas">แนวคิดในการทำงาน <span aria-hidden="true">↓</span></a></div><div class="profile-photo"><img src="assets/{d['id']}.jpg" alt="{d['degree']}{d['name']}" width="550" height="790"></div></section><nav class="section-nav" aria-label="หัวข้อประวัติ"><a href="#ideas">แนวคิด</a><a href="#experience">ประสบการณ์</a><a href="#education">การศึกษา</a></nav><section class="section" id="ideas"><div class="section-heading"><span class="eyebrow">แนวคิดในการทำงาน</span><h2>4 แนวทางเพื่อสมาชิก</h2></div><div class="policy-grid">{policies}</div></section><section class="section experience" id="experience"><div class="section-heading"><span class="eyebrow">ประสบการณ์</span><h2>งานที่ผ่านมา</h2></div><div>{jobs}<details><summary>อ่านประสบการณ์เพิ่มเติม</summary><ul class="experience-list">{exp}</ul><p>{d['bio']}</p></details></div></section><section class="section education" id="education"><div class="section-heading"><span class="eyebrow">ประวัติการศึกษา</span><h2>พื้นฐานความรู้</h2></div><ul class="education-list">{edu}</ul></section><div class="download"><a class="button" href="assets/{infographic_file}" download>{infographic_label} <span aria-hidden="true">↓</span></a></div><aside class="next"><span>รู้จักผู้สมัครท่านอื่น</span><div class="next-links">{other_links}</div></aside></main>'''
    (out / f"{d['id']}.html").write_text(head(f"หมายเลข {d['number']} · {d['degree']}{d['name']} | ผู้สมัครกรรมการ สอ.มก. 2570", d['lead'].replace('\n', ' ')) + page + footer)

print('Build completed successfully.')
