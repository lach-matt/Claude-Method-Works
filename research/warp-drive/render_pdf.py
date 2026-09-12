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
def inline(t):
    t = html.escape(t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
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
            hdr=[c.strip() for c in L.strip().strip('|').split('|')]
            i+=2; rows=[]
            while i<len(lines) and re.match(r'^\|.*\|\s*$', lines[i]):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i+=1
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
