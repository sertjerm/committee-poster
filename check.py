from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

root = Path(__file__).parent / 'dist'

class Check(HTMLParser):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for k in ['src', 'href']:
            raw = a.get(k, '')
            if raw.startswith(('data:', 'http:', 'https:')):
                continue
            v = urlsplit(raw).path
            if v:
                target = (self.file_path.parent / unquote(v)).resolve()
                assert target.is_file(), f"Missing file: {v} referenced in {self.file_path}"

for p in sorted(root.glob('**/*.html')):
    s = p.read_text(encoding='utf-8')
    Check(p).feed(s)
    assert 'ปิติปัญญา' not in s, f"Found typo ปิติปัญญา in {p}"
    assert 'สอ.มท.' not in s, f"Found typo สอ.มท. in {p}"
    assert '<html lang="th">' in s, f"Missing lang in {p}"
    print(p.relative_to(root), 'OK')

print('All HTML checks passed!')
