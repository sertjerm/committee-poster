# ผู้สมัครกรรมการ สอ.มก. 2570

Static, mobile-friendly candidate profiles for ทวีวัฒน์ ทัศนวัฒน์, ธวัชชัย ศักดิ์ภู่อร่าม, and รังสรรค์ ปีติปัญญา.

## Preview

Run `python3 -m http.server 8765 --directory dist` from this directory.

## Content

- `dist/index.html`: candidate index (original summary version)
- `dist/thawiwat.html`: Thawiwat profile
- `dist/thawatchai.html`: Thawatchai profile (temporary mock content copied from Thawiwat and clearly labelled)
- `dist/rangsarn.html` & `dist/rangsan.html`: Rangsarn profile
- `dist/v1/`: Full official PDF policies version (`v1/index.html`, `v1/thawiwat.html`, `v1/thawatchai.html`, `v1/rangsarn.html`, `v1/rangsan.html`)
- `dist/style.css`: shared responsive layout
- `dist/assets/`: original candidate photos resized for web, self-hosted fonts, infographic downloads

The supplied QR-data PDFs are content sources. Names/titles follow `../prompts/ข้อความที่ถูกต้อง.txt`, which corrects the Rangsarn surname to ปีติปัญญา. Private addresses, contact details, dates of birth and application form fields are excluded. Each candidate has an independent URL suitable for a later QR destination. Confirmed ballot numbers: Thawiwat 2; Thawatchai 3; Rangsarn 4. Source: ../prompts/design-title-airy-20260921-v6.txt. Prominent number badges appear on index and individual profiles. Thawatchai's biography, education, timeline, and four concepts are temporary mock data copied from Thawiwat until the candidate's real information is supplied.

`build.py` holds the content generator (Python 3.11+); edit it and rebuild so changes remain reproducible. `check.py` checks local asset and page references. Noto Sans Thai is self-hosted under the SIL Open Font License included in assets.

## Draft 3 — 23 September 2026

Preserves the original green-and-white design. Ballot numbers 2, 3, and 4 sit in the text area, outside the portrait. Narrow-screen cards stack the complete portrait above the candidate information; names use the same font size for all candidates. Profiles link to freshly generated v3 infographics, with previous assets retained. Thawatchai’s temporary education, biography and concepts are explicitly labelled as sample content from Thawiwat.

Validation: local references checked; desktop and narrow mobile layouts reviewed; no horizontal overflow and ballot badges outside portraits confirmed; concept anchor navigation verified.
