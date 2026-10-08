"""Validate the publication catalog and the built site's local links.
Usage: python scripts/check_site.py --public /path/to/hugo/output
Uses only the Python standard library. No network access or source mutation.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import argparse, json, hashlib, re, sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--public', type=Path, required=True)
args = parser.parse_args()
public = args.public.resolve()
errors, papers, dois, hashes = [], [], {}, {}
for path in sorted((root / 'content/publication').glob('*/index.md')):
    text = path.read_text(encoding='utf-8')
    p, _ = json.JSONDecoder().raw_decode(text)
    papers.append(p)
    translation = path.with_name('index.zh.md')
    if not translation.exists():
        errors.append(f'{path.parent.name}: Chinese translation missing')
    else:
        zh, _ = json.JSONDecoder().raw_decode(translation.read_text(encoding='utf-8'))
        # Translation must not change the identity or publication status of a work.
        for field in ['title', 'authors', 'date', 'date_precision', 'publication', 'publication_kind',
                      'doi', 'slug', 'status', 'url_pdf', 'source_url', 'topic', 'featured']:
            if p.get(field) != zh.get(field):
                errors.append(f'{path.parent.name}: translated {field} differs from source')
        if not re.search(r'[\u4e00-\u9fff]', zh.get('summary', '')):
            errors.append(f'{path.parent.name}: Chinese summary missing')
    for field in ['title', 'authors', 'date', 'publication', 'publication_kind', 'summary', 'doi', 'source_url']:
        if not p.get(field): errors.append(f'{path.parent.name}: missing {field}')
    if not {'Lu Wang', '王璐'}.intersection(p['authors']): errors.append(f'{path.parent.name}: Lu Wang absent')
    doi = p['doi'].lower()
    if doi in dois: errors.append(f'Duplicate DOI: {doi}')
    dois[doi] = p['slug']
    bib = path.with_name('cite.bib')
    if not bib.exists() or p['doi'] not in bib.read_text(encoding='utf-8').replace('\\_', '_'):
        errors.append(f'{path.parent.name}: citation missing or DOI mismatch')
    if p.get('url_pdf'):
        pdf = root / 'static' / p['url_pdf'].lstrip('/')
        if not pdf.exists() or not pdf.read_bytes().startswith(b'%PDF'):
            errors.append(f'{p["slug"]}: invalid PDF')
        else:
            digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
            if digest in hashes: errors.append(f'Duplicate PDF: {p["slug"]} and {hashes[digest]}')
            hashes[digest] = p['slug']

paper_titles = {p['slug']: p['title'] for p in papers}
for path in (root / 'content/post').glob('*/index*.md'):
    text = path.read_text(encoding='utf-8')
    news, end = json.JSONDecoder().raw_decode(text)
    match = re.search(r'/publication/([^/]+)/', text[end:])
    if not match or news['title'] != paper_titles.get(match[1]):
        errors.append(f'{path}: news title must match the full publication title')

class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.ids = set(); self.h1 = 0; self.canonical = ''
        self.lang = ''; self.language_switch = ''; self.citation = {}
        self.in_nav = False; self.nav_links = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == 'nav' and d.get('id') == 'site-nav': self.in_nav = True
        if tag == 'a' and self.in_nav: self.nav_links.append(d.get('href', ''))
        if tag == 'html': self.lang = d.get('lang', '')
        if 'language-switch' in d.get('class', '').split(): self.language_switch = d.get('href', '')
        if tag == 'meta' and d.get('name', '').startswith('citation_'):
            self.citation.setdefault(d['name'], []).append(d.get('content', ''))
        if tag == 'link' and d.get('rel') == 'canonical': self.canonical = d.get('href', '')
        if 'id' in d: self.ids.add(d['id'])
        if tag == 'h1': self.h1 += 1
        for key in ('href', 'src'):
            if key in d: self.links.append(d[key])
    def handle_endtag(self, tag):
        if tag == 'nav': self.in_nav = False

pages = {}
for path in public.rglob('*.html'):
    page = Page(); page.feed(path.read_text(encoding='utf-8')); pages[path] = page
base_path = urlsplit(pages[public / 'index.html'].canonical).path.rstrip('/')
for path, page in pages.items():
    source = path.read_text(encoding='utf-8')
    if any(s in source for s in ['example.com', 'test@example.org', 'GeorgeCushen', 'Lorem ipsum', 'Nelson Bighetti']):
        errors.append(f'{path.relative_to(public)}: starter placeholder remains')
    # Hugo alias pages are redirects with no main content.
    if '<main' in source and page.h1 != 1: errors.append(f'{path.relative_to(public)}: expected one H1')
    if '<main' in source:
        relative = path.relative_to(public)
        chinese = relative.parts[0] == 'zh'
        expected_language = 'zh-CN' if chinese else 'en-US'
        if page.lang != expected_language:
            errors.append(f'{relative}: incorrect HTML language {page.lang}')
        for link in page.nav_links:
            expected_prefix = base_path + ('/zh/' if chinese else '/')
            if not link.startswith(expected_prefix) or (not chinese and link.startswith(base_path + '/zh/')):
                errors.append(f'{relative}: navigation changes language: {link}')
        if path.name != '404.html':
            counterpart = public.joinpath(*relative.parts[1:]) if chinese else public / 'zh' / relative
            expected_switch = base_path + '/' + counterpart.relative_to(public).parent.as_posix().strip('.')
            expected_switch = expected_switch.rstrip('/') + '/'
            if page.language_switch != expected_switch:
                errors.append(f'{relative}: language switch does not preserve the current page')
            if counterpart not in pages:
                errors.append(f'{relative}: translated page missing')
            elif page.citation != pages[counterpart].citation:
                errors.append(f'{relative}: citation metadata differs between languages')
    for link in page.links:
        u = urlsplit(link)
        if u.scheme or u.netloc or link.startswith(('data:', 'mailto:')): continue
        local_path = unquote(u.path)
        if base_path and (local_path == base_path or local_path.startswith(base_path + '/')):
            local_path = local_path[len(base_path):] or '/'
        target = (public / local_path.lstrip('/')) if local_path.startswith('/') else (path.parent / local_path)
        if not u.path: target = path
        if target.is_dir(): target /= 'index.html'
        target = target.resolve()
        if not target.is_file(): errors.append(f'{path.relative_to(public)}: missing {link}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{path.relative_to(public)}: missing anchor {link}')

report = {'publications': len(papers), 'pdfs': len(hashes), 'html_pages': len(pages), 'errors': errors}
print(json.dumps(report, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
