# ผู้สมัครกรรมการ สอ.มก. 2570

Static, mobile-friendly candidate profiles for ทวีวัฒน์ ทัศนวัฒน์, ธวัชชัย ศักดิ์ภู่อร่าม, and รังสรรค์ ปิติปัญญา.

## Preview

Run `python3 -m http.server 8765 --directory dist` from this directory.

## Content

- `dist/index.html`: canonical redirect to v1, the public primary version
- `dist/v1/media.html`: gallery of all approved posters and infographics; tap an image to open it full size (tap again to toggle actual size, × or backdrop to close), download icon saves the file
- `dist/thawiwat.html`: Thawiwat profile (Number 2)
- `dist/thawatchai.html`: Thawatchai profile (Number 3, real data applied from `ธวัชชัยQR-data.pdf`)
- `dist/rangsarn.html` & `dist/rangsan.html`: Rangsarn profile (Number 4)
- `dist/v1/`: primary full official PDF policies version (`v1/index.html`, `v1/thawiwat.html`, `v1/thawatchai.html`, `v1/rangsarn.html`, `v1/rangsan.html`)
- `dist/style.css`: shared responsive layout
- `dist/assets/`: original candidate photos resized for web, self-hosted fonts, infographic downloads
- `dist/assets/media/`: versioned artwork copied from `../20290930-production/` (five updated images) and `../exports2026-09-25/final/` (policy poster) during each build
- `prompts/`: dedicated directory for candidate-specific infographic prompts and master approved texts

The supplied QR-data PDFs are content sources. Names/titles follow `prompts/ข้อความอินโฟกราฟิก-รายผู้สมัคร.txt`, which confirms the Rangsarn surname as ปิติปัญญา. Private addresses, contact details, dates of birth and application form fields are excluded. Each candidate has an independent URL suitable for a later QR destination. Confirmed ballot numbers: Thawiwat 2; Thawatchai 3; Rangsarn 4. Prominent number badges appear on index and individual profiles. All candidates now use verified, official QR data.

`build.py` holds the content generator (Python 3+); edit it and rebuild so changes remain reproducible. `check.py` checks local asset and page references. Noto Sans Thai is self-hosted under the SIL Open Font License included in assets.

## Draft 4 — 23 September 2026

Preserves the original green-and-white design. Ballot numbers 2, 3, and 4 sit in the text area, outside the portrait. Narrow-screen cards stack the complete portrait above the candidate information; names use the same font size for all candidates. Real data for Thawatchai (Ph.D. Azabu University, former Dean, former Veterinary Council President, 6 policies) fully applied; mock notices removed. Candidate prompts organized cleanly in `minisite-v1/prompts/`.

Validation: local references checked; desktop and narrow mobile layouts reviewed; no horizontal overflow and ballot badges outside portraits confirmed; concept anchor navigation verified; all HTML checks passed.

## Portrait update — 30 September 2026

All candidate cards and profile pages, including legacy URLs, now use versioned logo-free portraits. Approved PNG sources live in `portrait-sources/`; `build.py` creates JPEG and WebP assets from them. Original assets remain available.

## Front poster correction — 1 October 2026

The media gallery now uses `poster-front-20261001.png`, copied unchanged from the corrected `../20290930-production/หน้าตรง.png`. The previous artwork remains available for existing links.
