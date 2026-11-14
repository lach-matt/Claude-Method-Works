#!/usr/bin/env python3
"""build_html.py SOURCE.md OUT.html

Markdown -> print-ready HTML for the reader's edition (PAPER.md), with the stylesheet of
research/warp-drive/render_pdf.py (the pipeline of the earlier render), but
parsed by pandoc's CommonMark/GFM reader, so that the indented display-equation
blocks, ordered-list numbering and code spans across a line break are kept.
(render_pdf.py's own parser printed the display equations as run-in paragraphs
with their alignment collapsed, restarted numbered lists at 1, and italicised a
whole paragraph of section 8 from a stray `*`.)

The source is only read.  A temporary copy is escaped first, because the paper
writes mathematics in plain Unicode and four Markdown constructs misfire on it:
  * `_`  is always a subscript here, never emphasis       -> `\\_`
  * `[`  is notation (`θ[S](g_λ)`), never a link          -> `\\[`
  * `*`  between two letters/digits (`σ*g`) or after a
         subscript (`t_*`) is a star, not emphasis          -> `\\*`
  * a line starting `+ ` is a wrapped sum, not a bullet   -> `\\+ `
Code spans and indented code blocks are left untouched.  The source holds no
backslash, so every backslash the escape adds is unambiguous.
"""
import html, re, subprocess, sys, unicodedata

SRC, OUT = sys.argv[1], sys.argv[2]
md = open(SRC, encoding='utf-8').read()
assert '\\' not in md, 'source has backslashes; escaping would be ambiguous'
lines = md.split('\n')

# ---- 1. which lines are indented code blocks (the display equations) --------
def ind(s): return len(s) - len(s.lstrip(' '))
code = [False] * len(lines)
for i, l in enumerate(lines):
    if not l.strip() or ind(l) < 4:
        continue
    j = i - 1
    if j < 0 or not lines[j].strip() or code[j]:
        code[i] = True          # after a blank line, or continuing a block
for i, l in enumerate(lines):   # blank lines inside one block belong to it
    if not l.strip():
        a = i - 1
        while a >= 0 and not lines[a].strip(): a -= 1
        b = i + 1
        while b < len(lines) and not lines[b].strip(): b += 1
        if a >= 0 and b < len(lines) and code[a] and code[b]:
            code[i] = True

# ---- 2. escape outside code ---------------------------------------------------
out, in_span = [], 0
stats = {'_': 0, '[': 0, '*': 0, '+': 0}
for i, l in enumerate(lines):
    if code[i]:
        out.append(l); continue
    if not l.strip():
        assert in_span == 0, 'code span open across a blank line at %d' % (i + 1)
    res, k = [], 0
    if not in_span and re.match(r'^\s*\+ ', l):
        p = l.index('+'); res.append(l[:p] + '\\+'); k = p + 1; stats['+'] += 1
    while k < len(l):
        c = l[k]
        if c == '`':
            run = len(re.match(r'`+', l[k:]).group(0))
            if in_span == 0: in_span = run
            elif in_span == run: in_span = 0
            res.append('`' * run); k += run; continue
        if not in_span:
            if c in '_[':
                res.append('\\' + c); stats[c] += 1; k += 1; continue
            if c == '*' and 0 < k and (l[k-1] == '_' or (
                    k < len(l) - 1 and l[k-1].isalnum() and l[k+1].isalnum())):
                res.append('\\*'); stats['*'] += 1; k += 1; continue
        res.append(c); k += 1
    out.append(''.join(res))
assert in_span == 0
esc = '\n'.join(out)

# ---- 3. pandoc ----------------------------------------------------------------
body = subprocess.run(
    ['pandoc', '-f', 'gfm-raw_html-emoji-autolink_bare_uris', '-t', 'html5',
     '--wrap=none'],
    input=esc, capture_output=True, text=True, check=True).stdout

# ---- 4. fit each display block to the measure ---------------------------------
# DejaVu Sans Mono advances 1233/2048 em.  Measure: A4 210 mm - 2 x 16 mm =
# 504.57 pt, less the pre's 2 x 7 pt padding and 2.5 px (1.875 pt) rule; a list
# item takes another 18 pt.  3 % is kept in hand for glyphs drawn from fallback
# fonts (l-script, script P and N are not in DejaVu Sans Mono).  A block keeps
# 8.8 pt when it fits and is never set below FLOOR; past that it wraps.
ADV, MEASURE, BASE, FLOOR = 1233 / 2048, 504.57 - 14 - 1.875, 8.8, 6.4
def cols(text):
    return max((sum(1 for ch in ln if not unicodedata.combining(ch))
                for ln in html.unescape(text).split('\n')), default=0)
shrunk = []
def fit(m):
    inner = m.group(1)
    before = body[:m.start()]
    in_list = before.count('<li') > before.count('</li>')
    width = MEASURE - (18 if in_list else 0)
    n = cols(re.sub(r'<[^>]+>', '', inner))
    size = min(BASE, width * 0.97 / (n * ADV)) if n else BASE
    size = max(FLOOR, int(size * 10) / 10)
    if size < BASE: shrunk.append((n, size))
    # a block longer than ~30 lines may break across pages (else a whole page
    # is left blank before it)
    cls = 'eq long' if inner.count('\n') > 30 else 'eq'
    return '<pre class="%s" style="font-size:%.1fpt">%s</pre>' % (cls, size, inner)
body = re.sub(r'<pre>(.*?)</pre>', fit, body, flags=re.S)
# the same for the two long tables (Appendix C's source map, Appendix D's md5s)
body = re.sub(r'<table>(.*?)</table>',
              lambda m: ('<table class="long">' if m.group(1).count('<tr') > 25 else '<table>')
              + m.group(1) + '</table>', body, flags=re.S)

# ---- 5. break opportunities in inline paths ----------------------------------
# A path such as `docket68/n1star/checks/support8b.py` has no break opportunity,
# so a justified line before it was stretched to wide gaps.  A <wbr> after each
# `/` lets it break there; it adds no character to the text.
def wbr(m):
    return m.group(1) + re.sub(r'/(?=[^/<])', '/<wbr>', m.group(2)) + '</code>'
parts = re.split(r'(<pre\b.*?</pre>)', body, flags=re.S)
body = ''.join(p if p.startswith('<pre') else
               re.sub(r'(<code>)(.*?)</code>', wbr, p, flags=re.S) for p in parts)

# ---- 6. letters carrying a combining accent ---------------------------------------
# Liberation Serif (what 'Times New Roman' resolves to here) and DejaVu Sans Mono
# do not attach a combining accent to a Greek letter or a symbol: the tilde of
# psi-tilde, the dot of mu-dot and the tilde of box-tilde print beside the base,
# and the arrow of c-vec does not print at all.  FreeSerif (a Times face) and
# Liberation Mono (0.6 em, as the mono measure assumes) attach all of them, so
# each such cluster is set in those.
MARK = re.compile(r'[^\s<>&;][̀-ͯ⃐-⃿]+')
ncm = [0, 0]
def marks(chunk, mono):
    def sub(m):
        ncm[mono] += 1
        return '<span class="%s">%s</span>' % ('cmm' if mono else 'cm', m.group(0))
    return MARK.sub(sub, chunk)
toks = re.split(r'(<[^>]+>)', body); depth = 0; outb = []
for t in toks:
    if t.startswith('<'):
        if re.match(r'<pre\b', t): depth += 1
        elif t.startswith('</pre'): depth -= 1
        outb.append(t)
    else:
        outb.append(marks(t, 1 if depth else 0))
body = ''.join(outb)
print('accented clusters set in FreeSerif: %d, in Liberation Mono: %d' % tuple(ncm), file=sys.stderr)

CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
body { font: 10.5pt/1.55 Georgia,'Times New Roman',FreeSerif,serif; color:#111; margin:0; }
h1 { font-size:20pt; margin:0 0 2pt; letter-spacing:-.3pt; }
h2 { font-size:13pt; margin:20pt 0 6pt; padding-bottom:3pt;
     border-bottom:1.5px solid #111; page-break-after:avoid; }
h3 { font-size:11pt; margin:14pt 0 4pt; page-break-after:avoid; }
p { margin:0 0 7pt; text-align:justify; hyphens:auto; }
code { font:9.2pt/1.4 'DejaVu Sans Mono',FreeMono,Menlo,monospace; background:#f2f2ef;
       padding:.5pt 2.5pt; border-radius:2px; overflow-wrap:anywhere;
       word-break:break-word; }
p, li, td, th, blockquote { overflow-wrap:anywhere; }
pre { white-space:pre-wrap; word-break:break-word; font:8.8pt/1.4 'DejaVu Sans Mono',FreeMono,Menlo,monospace; background:#f7f7f4;
      border-left:2.5px solid #999; padding:7pt 7pt; overflow-x:auto;
      page-break-inside:avoid; margin:8pt 0; }
pre code { font:inherit; background:none; padding:0; border-radius:0;
           overflow-wrap:normal; word-break:normal; }
blockquote { margin:8pt 0; padding:6pt 11pt; background:#f7f7f4;
             border-left:2.5px solid #444; page-break-inside:avoid; }
blockquote p:last-child { margin-bottom:0; }
table { border-collapse:collapse; width:100%; margin:8pt 0; font-size:9.2pt;
        page-break-inside:avoid; }
th { text-align:left; border-bottom:1.2px solid #111; padding:3.5pt 6pt;
     background:#f2f2ef; font-family:Helvetica,Arial,sans-serif; font-size:8.6pt;
     text-transform:uppercase; letter-spacing:.4pt; }
td { border-bottom:.5px solid #ddd; padding:3.5pt 6pt; vertical-align:top; }
td code { font-size:8.4pt; }
thead { display:table-header-group; }
tr { page-break-inside:avoid; }
hr { border:0; border-top:.5px solid #ccc; margin:14pt 0; }
ul,ol { margin:0 0 7pt; padding-left:18pt; } li { margin-bottom:2.5pt; }
li > p { margin-bottom:2.5pt; }
del { color:#888; }
a { color:#111; }
table.long, pre.long { page-break-inside:auto; }
.cm { font-family:FreeSerif,serif; }
.cmm { font-family:'Liberation Mono',FreeMono,monospace; }
"""
TITLE = next((x[2:].strip() for x in lines if x.startswith('# ')), 'PAPER')
doc = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>%s</title>'
       '<style>%s</style></head><body>%s</body></html>\n') % (html.escape(TITLE), CSS, body)
open(OUT, 'w', encoding='utf-8').write(doc)
print('escaped %s; display blocks %d, shrunk to fit (cols, pt): %s' % (
    stats, body.count('<pre class="eq'), sorted(shrunk, reverse=True)), file=sys.stderr)
