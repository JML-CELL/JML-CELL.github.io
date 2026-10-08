"""Regenerate individual and combined citations from publication front matter."""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
entries = []
def escape(value):
    return str(value).replace('&', r'\&').replace('%', r'\%').replace('_', r'\_').replace('#', r'\#')

for path in (root / 'content/publication').glob('*/index.md'):
    p, _ = json.JSONDecoder().raw_decode(path.read_text(encoding='utf-8'))
    kind = {'Journal': 'article', 'Book chapter': 'incollection', 'Book': 'book'}.get(p['publication_kind'], 'inproceedings')
    fields = {'title': '{' + p['title'] + '}', 'author': ' and '.join(p['authors']), 'year': p['date'][:4]}
    if kind == 'book':
        fields.update(publisher=p.get('publisher', 'Springer'), series='SpringerBriefs in Computer Science')
    else:
        fields['journal' if kind == 'article' else 'booktitle'] = p['publication']
    for source, target in [('volume', 'volume'), ('issue', 'number'), ('pages', 'pages'), ('doi', 'doi'), ('article_number', 'articleno')]:
        if p.get(source):
            fields[target] = str(p[source]).replace('-', '--') if source == 'pages' else p[source]
    fields['url'] = p['source_url']
    key = p['slug'].replace('-', '') + p['date'][:4]
    bib = '@' + kind + '{' + key + ',\n' + ',\n'.join('  ' + k + ' = {' + escape(v) + '}' for k, v in fields.items()) + '\n}\n'
    path.with_name('cite.bib').write_text(bib, encoding='utf-8')
    entries.append((p['date'], p['title'], bib))
(root / 'static/publications.bib').write_text('\n'.join(e[2] for e in sorted(entries, reverse=True)), encoding='utf-8')
print(f'Exported {len(entries)} citations.')
