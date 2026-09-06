import re, os
exec(open('/home/claude/book/engine.py').read())

# --- override the figure handler for the book's named files -------------
def figure(path, cap):
    p = "/home/claude/book/" + path
    iw, ih = PIL.open(p).size
    w = 163*mm; h = w*ih/iw
    if h > 112*mm: h = 112*mm; w = h*iw/ih
    return KeepTogether([Image(p, width=w, height=h),
                         Paragraph(esc(cap), S['cap'])])

def render_book(md):
    out=[]; lines=md.split('\n'); i=0; buf=[]
    def flush(style='body'):
        nonlocal buf
        if buf:
            txt=' '.join(x.strip() for x in buf if x.strip())
            if txt: out.append(Paragraph(esc(txt), S[style]))
            buf=[]
    while i < len(lines):
        L = lines[i]
        m = re.match(r'^!\[Figure[^\]]*\]\(([^)]+)\)\s*$', L)
        if m:
            flush(); path=m.group(1); j=i+1
            while j < len(lines) and not lines[j].strip(): j+=1
            cap=''
            while j < len(lines) and lines[j].strip() and not lines[j].startswith(('#','|','>','!')):
                cap += (' ' if cap else '') + lines[j].strip(); j+=1
            out.append(figure(path, cap)); i=j; continue
        if L.startswith('|') and i+1 < len(lines) and set(lines[i+1].replace('|','').strip()) <= set('-: '):
            flush(); rows=[]; j=i
            while j < len(lines) and lines[j].startswith('|'):
                if not set(lines[j].replace('|','').strip()) <= set('-: '):
                    rows.append([c.strip() for c in lines[j].strip().strip('|').split('|')])
                j+=1
            out.append(Spacer(1,3)); out.append(mktable(rows)); out.append(Spacer(1,7))
            i=j; continue
        if L.startswith('> '):
            flush(); q=[]
            while i < len(lines) and lines[i].startswith('>'):
                q.append(lines[i].lstrip('>').strip()); i+=1
            out.append(Paragraph(esc(' '.join(x for x in q if x)), S['quote'])); continue
        m = re.match(r'^(#{1,3}) (.+)$', L)
        if m:
            flush(); lvl=len(m.group(1)); txt=m.group(2).strip()
            if lvl == 1:
                brk = bool(re.match(r'^(PART|\d+\.|Appendix|Index|On the word|Nothing is)', txt))
                if brk: out.append(PageBreak())
                out.append(Paragraph(esc(txt), S['part']))
            elif lvl == 2: out.append(Paragraph(esc(txt), S['h1']))
            else: out.append(Paragraph(esc(txt), S['h2']))
            i+=1; continue
        m = re.match(r'^(\s*)([-*]|\d+\.)\s+(.+)$', L)
        if m:
            flush(); body=m.group(3); j=i+1
            while j < len(lines) and lines[j].startswith('   ') and lines[j].strip():
                body += ' ' + lines[j].strip(); j+=1
            bt = "\u2022" if m.group(2) in '-*' else m.group(2)
            out.append(Paragraph(esc(body), S['bul'], bulletText=bt)); i=j; continue
        if L.strip() == '---':
            flush(); out.append(Spacer(1,4)); i+=1; continue
        if not L.strip(): flush(); i+=1; continue
        buf.append(L); i+=1
    flush()
    return out

md = open('/home/claude/book/BOOK.md').read()
# strip the markdown title block; typeset it properly
i = md.index('## Contents')
body = md[i:]

st = []
A = st.append
A(Spacer(1, 46*mm))
A(Paragraph("The Lach Index Lattice", S['tt']))
A(Paragraph("Closure, self-reference, and what an index cannot do", S['ts']))
A(Spacer(1, 8*mm))
A(Paragraph("Matthew Lach", S['auth']))
A(Spacer(1, 26*mm))
A(Paragraph("1,442 verified cells across 35 atomic systems &#183; "
            "\u2113 = 0\u20136 &#183; Z = 1\u201383 &#183; "
            "a forty-eight item withdrawal register &#183; "
            "three falsification tests, run", S['affil']))
A(PageBreak())
st.extend(render_book(body))

doc = Doc("/mnt/user-data/outputs/the-lach-index-lattice.pdf", pagesize=A4,
          leftMargin=19*mm, rightMargin=19*mm, topMargin=19*mm, bottomMargin=17*mm,
          title="The Lach Index Lattice: Closure, self-reference, and what an index cannot do",
          author="Matthew Lach",
          subject="Order theory; atomic spectroscopy; index structure",
          creator="draft one")
doc.build(st)
print("built")