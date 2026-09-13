#!/usr/bin/env python3
"""
render_pdf.py -- markdown to print-ready HTML, for the PDF of THE-HIERARCHY-LAW.

stdlib only.  The PDF in paper/pdf/ is GENERATED; regenerate it, never hand-edit:

    python3 render_pdf.py paper/THE-HIERARCHY-LAW.md > /tmp/law.html
    /opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless --disable-gpu \
        --no-sandbox --no-pdf-header-footer \
        --print-to-pdf=paper/pdf/THE-HIERARCHY-LAW.pdf file:///tmp/law.html

No pandoc or LaTeX exists in this environment; Chromium is the only renderer
available, which is why the pipeline goes through HTML.
"""
import html, re, sys
def split_row(L):
    """Split a table row on UNESCAPED pipes only -- `\\|` is a literal pipe in a
    cell and must not create a column."""
    out=[]; cur=''; k=0; body=L.strip()
    if body.startswith('|'): body=body[1:]
    if body.endswith('|'): body=body[:-1]
    while k < len(body):
        if body[k]=='\\' and k+1 < len(body) and body[k+1]=='|':
            cur+='|'; k+=2; continue
        if body[k]=='|':
            out.append(cur); cur=''; k+=1; continue
        cur+=body[k]; k+=1
    out.append(cur)
    return out


def inline(t):
    t = html.escape(t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    # An opening delimiter must not be a BACKSLASH-ESCAPED asterisk.  `Lemma
    # N1\*` appears throughout the paper, and without the `\\` in these
    # lookbehinds its `*` opened an emphasis span that ran to the next real
    # `*` -- swallowing a sentence and leaving the true closer as a stray
    # asterisk in the PDF.
    # Bold may CONTAIN italic.  `[^*]` alone cannot express that: on
    # `**N4 -- it is the *number of factors* that Lemma 7 needs**` the content
    # class rejected the nested `*` and the whole bold failed, leaking literal
    # `**` into the PDF.  A single `*` not followed by another is allowed
    # through here and picked up by the emphasis pass below.
    t = re.sub(r'(?<!\\)\*\*((?:\\\*|\*(?!\*)|[^*])+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![*\\])\*((?:\\\*|[^*])+?)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'~~([^~]+)~~', r'<del>\1</del>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', t)
    t = t.replace('\\*','*').replace('\\|','|')
    return t
def conv(md):
    out=[]; lines=md.split('\n'); i=0
    while i < len(lines):
        L=lines[i]
        if L.startswith('```'):
            i+=1; buf=[]
            while i<len(lines) and not lines[i].startswith('```'):
                buf.append(html.escape(lines[i])); i+=1
            i+=1; out.append('<pre>'+'\n'.join(buf)+'</pre>'); continue
        if re.match(r'^\|.*\|\s*$', L) and i+1<len(lines) and re.match(r'^\|[\s:|-]+\|\s*$', lines[i+1]):
            hdr=[c.strip() for c in split_row(L)]
            i+=2; rows=[]
            while i<len(lines) and re.match(r'^\|.*\|\s*$', lines[i]):
                rows.append([c.strip() for c in split_row(lines[i])]); i+=1
            t='<table><thead><tr>'+''.join('<th>%s</th>'%inline(c) for c in hdr)+'</tr></thead><tbody>'
            for r in rows:
                t+='<tr>'+''.join('<td>%s</td>'%inline(c) for c in r)+'</tr>'
            out.append(t+'</tbody></table>'); continue
        if L.startswith('>'):
            buf=[]
            while i<len(lines) and lines[i].startswith('>'):
                buf.append(lines[i][1:].lstrip()); i+=1
            out.append('<blockquote>'+conv('\n'.join(buf))+'</blockquote>'); continue
        m=re.match(r'^(#{1,6})\s+(.*)$', L)
        if m:
            n=len(m.group(1)); out.append('<h%d>%s</h%d>'%(n,inline(m.group(2)),n)); i+=1; continue
        if re.match(r'^---+\s*$', L): out.append('<hr>'); i+=1; continue
        if re.match(r'^\s*[-*]\s+', L) or re.match(r'^\s*\d+\.\s+', L):
            ordered = bool(re.match(r'^\s*\d+\.\s+', L)); items=[]
            while i<len(lines) and (re.match(r'^\s*[-*]\s+', lines[i]) or re.match(r'^\s*\d+\.\s+', lines[i]) or (items and lines[i].startswith('   ') and lines[i].strip())):
                if re.match(r'^\s*[-*]\s+', lines[i]) or re.match(r'^\s*\d+\.\s+', lines[i]):
                    items.append(re.sub(r'^\s*(?:[-*]|\d+\.)\s+','',lines[i]))
                else: items[-1]+=' '+lines[i].strip()
                i+=1
            tag='ol' if ordered else 'ul'
            out.append('<%s>'%tag+''.join('<li>%s</li>'%inline(x) for x in items)+'</%s>'%tag); continue
        if not L.strip(): i+=1; continue
        buf=[]
        while i<len(lines) and lines[i].strip() and not re.match(r'^(#{1,6}\s|>|\||```|---+\s*$|\s*[-*]\s|\s*\d+\.\s)', lines[i]):
            buf.append(lines[i]); i+=1
        if buf: out.append('<p>%s</p>'%inline(' '.join(buf)))
    return '\n'.join(out)

def selftest():
    """Fixtures are the FOUR real corruptions this renderer shipped, each of
    which reached a committed PDF and was caught only by reading the output.
    A renderer that silently mangles the deliverable is the last place to have
    no guard, so every bug found becomes a case here."""
    ok = True

    def eq(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %s" % ("ok" if good else "XX", name))
        if not good:
            print("        got  %r\n        want %r" % (got, want))

    # 1. A backslash-escaped pipe is a literal, not a column break.
    eq("escaped pipe stays in its cell",
       split_row(r"| a \| b | c |"), [" a | b ", " c "])
    eq("plain row still splits", split_row("| a | b |"), [" a ", " b "])

    # 2. Bold whose content contains an escaped asterisk.
    eq("bold over an escaped asterisk",
       inline(r"**Lemma N1\* holds**"), "<strong>Lemma N1* holds</strong>")

    # 3. An escaped asterisk must NOT open an emphasis span.  This one ran from
    #    `N1\*` to the next real `*`, swallowing a sentence and leaving a stray.
    eq("escaped asterisk is not a delimiter",
       inline(r"Lemma N1\* and then *real italic* here"),
       "Lemma N1* and then <em>real italic</em> here")

    # 4. Bold may CONTAIN italic; the old content class rejected the nested
    #    `*` and leaked literal `**` into the PDF.
    eq("italic nested inside bold",
       inline("**N4 is the *number of factors* needed**"),
       "<strong>N4 is the <em>number of factors</em> needed</strong>")

    # Regressions on the ordinary cases, so a fix cannot trade one for another.
    eq("plain bold", inline("**a**"), "<strong>a</strong>")
    eq("plain italic", inline("*a*"), "<em>a</em>")
    eq("bold then italic", inline("**a** *b*"),
       "<strong>a</strong> <em>b</em>")
    eq("code is escaped", inline("`x<y`"), "<code>x&lt;y</code>")
    eq("strikethrough", inline("~~a~~"), "<del>a</del>")
    eq("link", inline("[t](u)"), '<a href="u">t</a>')
    eq("no emphasis without a pair", inline("2 * 3 = 6"), "2 * 3 = 6")

    print("render_pdf selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
    sys.exit(selftest())

md=open(sys.argv[1]).read()
CSS = """
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
body { font: 10.5pt/1.55 Georgia,'Times New Roman',serif; color:#111; margin:0; }
h1 { font-size:20pt; margin:0 0 2pt; letter-spacing:-.3pt; }
h2 { font-size:13pt; margin:20pt 0 6pt; padding-bottom:3pt;
     border-bottom:1.5px solid #111; page-break-after:avoid; }
h3 { font-size:11pt; margin:14pt 0 4pt; page-break-after:avoid; }
p { margin:0 0 7pt; text-align:justify; hyphens:auto; }
code { font:9.2pt/1.4 'DejaVu Sans Mono',Menlo,monospace; background:#f2f2ef;
       padding:.5pt 2.5pt; border-radius:2px; overflow-wrap:anywhere;
       word-break:break-word; }
p, li, td, th, blockquote { overflow-wrap:anywhere; }
pre { white-space:pre-wrap; word-break:break-word; font:8.8pt/1.4 'DejaVu Sans Mono',Menlo,monospace; background:#f7f7f4;
      border-left:2.5px solid #999; padding:7pt 9pt; overflow-x:auto;
      page-break-inside:avoid; margin:8pt 0; }
blockquote { margin:8pt 0; padding:6pt 11pt; background:#f7f7f4;
             border-left:2.5px solid #444; page-break-inside:avoid; }
blockquote p:last-child { margin-bottom:0; }
table { border-collapse:collapse; width:100%; margin:8pt 0; font-size:9.2pt;
        page-break-inside:avoid; }
th { text-align:left; border-bottom:1.2px solid #111; padding:3.5pt 6pt;
     background:#f2f2ef; font-family:Helvetica,Arial,sans-serif; font-size:8.6pt;
     text-transform:uppercase; letter-spacing:.4pt; }
td { border-bottom:.5px solid #ddd; padding:3.5pt 6pt; vertical-align:top; }
hr { border:0; border-top:.5px solid #ccc; margin:14pt 0; }
ul,ol { margin:0 0 7pt; padding-left:18pt; } li { margin-bottom:2.5pt; }
del { color:#888; }
a { color:#111; }
"""
print('<!doctype html><html><head><meta charset="utf-8"><title>The Hierarchy Law</title>'
      '<style>%s</style></head><body>%s</body></html>' % (CSS, conv(md)))
