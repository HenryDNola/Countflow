# Put a Webstudio export into this repo, safely.
#
#     python publish-export.py "C:\Users\Hi Def\Downloads\CountFlow (8).zip"
#
# Webstudio's export contains ONLY index.html, the page folders and assets/.
# Everything else in this repo has to survive a publish, or things break
# quietly:
#
#   CNAME              countflow.dev stops pointing at the site without it
#   manifest.json      the installable app: name, colours, which icons
#   icon-192.png       the home-screen / Play Store icon
#   icon-512.png       the large icon
#   apple-touch-icon   the iPhone home-screen icon
#   README.md          this note's neighbours
#
# So this script ADDS and REPLACES what the export contains, and never deletes
# anything the export doesn't mention. It also points the pages' icon links at
# the local files instead of Webstudio's own servers, so the favicon and the
# Apple icon keep working even if that project moves or is deleted.
import pathlib
import re
import shutil
import sys
import tempfile
import zipfile

KEEP = ['CNAME', 'manifest.json', 'icon-192.png', 'icon-512.png',
        'apple-touch-icon.png', 'README.md', 'publish-export.py']

LOCAL_ICONS = [
    (re.compile(r'href="https://p-[^"]*icon-192[^"]*"'), 'href="/icon-192.png"'),
    (re.compile(r'href="https://p-[^"]*icon-512[^"]*"'), 'href="/icon-512.png"'),
    (re.compile(r'href="https://p-[^"]*apple-touch-icon[^"]*"'), 'href="/apple-touch-icon.png"'),
]

root = pathlib.Path(__file__).resolve().parent
zip_path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '')
if not zip_path.is_file():
    raise SystemExit('Give me the exported zip: python publish-export.py <path to CountFlow.zip>')

with tempfile.TemporaryDirectory() as tmp:
    out = pathlib.Path(tmp)
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(out)
    # Some exports wrap everything in one folder; step into it if so.
    kids = [p for p in out.iterdir() if not p.name.startswith('__')]
    if len(kids) == 1 and kids[0].is_dir():
        out = kids[0]

    if not (out / 'index.html').exists():
        raise SystemExit('That zip has no index.html at the top — is it a Webstudio export?')

    added = replaced = 0
    for src in sorted(out.rglob('*')):
        if src.is_dir():
            continue
        rel = src.relative_to(out)
        if rel.as_posix() in KEEP:
            print('  kept ours   :', rel.as_posix())
            continue
        dst = root / rel
        existed = dst.exists()
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        replaced += existed
        added += not existed

print(f'{added} new file(s), {replaced} replaced. Nothing else was touched.')

fixed = 0
for page in sorted(root.glob('**/*.html')):
    if '.git' in page.parts:
        continue
    html = page.read_text(encoding='utf-8')
    before = html
    for pattern, local in LOCAL_ICONS:
        html = pattern.sub(local, html)
    if html != before:
        page.write_text(html, encoding='utf-8')
        fixed += 1
if fixed:
    print(f'{fixed} page(s): icon links now point at this site\'s own icon files.')

missing = [k for k in KEEP if not (root / k).exists()]
print('KEEP list:', 'all present' if not missing else 'MISSING → ' + ', '.join(missing))
print('\nNow: git add -A && git commit && git push')
