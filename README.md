# ผู้สมัครกรรมการ สอ.มก. 2570

Static, mobile-friendly candidate profiles for ทวีวัฒน์ ทัศนวัฒน์ and รังสรรค์ ปีติปัญญา.

## Preview

Run `python3 -m http.server 8765 --directory dist` from this directory.

## Content

- `dist/index.html`: candidate index
- `dist/thawiwat.html`: Thawiwat profile
- `dist/rangsarn.html`: Rangsarn profile
- `dist/style.css`: shared responsive layout
- `dist/assets/`: original candidate photos resized for web, self-hosted fonts, infographic downloads

The supplied QR-data PDFs are content sources. Names/titles follow `../prompts/ข้อความที่ถูกต้อง.txt`, which corrects the Rangsarn surname to ปีติปัญญา. Private addresses, contact details, dates of birth and application form fields are excluded. Each candidate has an independent URL suitable for a later QR destination. No candidate ballot numbers were supplied, so none are shown.

`build.py` holds the initial content generator (Python 3.11+); output HTML can also be edited directly. `check.py` checks local asset and page references. Noto Sans Thai is self-hosted under the SIL Open Font License included in assets.
