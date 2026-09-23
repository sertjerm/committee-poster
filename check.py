from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
root=Path(__file__).parent/'dist'
class Check(HTMLParser):
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  for k in ['src','href']:
   v=a.get(k,'').split('#')[0]
   if v and not v.startswith(('data:','http:','https:')):
    assert (root/unquote(v)).is_file(),v
for p in root.glob('*.html'):
 s=p.read_text(); Check().feed(s)
 assert 'ปิติปัญญา' not in s,p
 assert 'สอ.มท.' not in s,p
 assert '<html lang="th">' in s
 print(p.name,'OK')
