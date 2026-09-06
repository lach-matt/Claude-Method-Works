#!/usr/bin/env python3
"""PDF text extractor with full CTM tracking.

This producer (Google Docs export) puts the page's vertical layout in q/cm/Q
graphics transforms, not in the text matrix, and encodes glyphs as 2-byte hex
codes resolved through /ToUnicode.  Spaces are explicit glyphs, so none is ever
inserted heuristically.
"""
import re, sys, zlib

def mul(m1, m2):
    a1,b1,c1,d1,e1,f1 = m1; a2,b2,c2,d2,e2,f2 = m2
    return (a1*a2+b1*c2, a1*b2+b1*d2, c1*a2+d1*c2,
            c1*b2+d1*d2, e1*a2+f1*c2+e2, e1*b2+f1*d2+f2)

def apply(m, x, y):
    a,b,c,d,e,f = m
    return (a*x + c*y + e, b*x + d*y + f)

data = open(sys.argv[1], 'rb').read()
objs = {int(m.group(1)): m.group(2)
        for m in re.finditer(rb'(\d+)\s+\d+\s+obj(.*?)endobj', data, re.S)}

def inflate(body):
    m = re.search(rb'stream\r?\n', body)
    if not m: return None
    end = body.find(b'endstream', m.end())
    try: return zlib.decompress(body[m.end():end].rstrip(b'\r\n'))
    except Exception: return None

cmaps = {}
for num, body in objs.items():
    if not re.search(rb'/Type\s*/Font', body): continue
    r = re.search(rb'/ToUnicode\s+(\d+)\s+\d+\s+R', body)
    if not r: continue
    cs = inflate(objs.get(int(r.group(1)), b''))
    if not cs: continue
    mp = {}
    for blk in re.finditer(rb'beginbfchar(.*?)endbfchar', cs, re.S):
        for a, b in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', blk.group(1)):
            mp[int(a,16)] = bytes.fromhex(b.decode()).decode('utf-16-be','replace')
    for blk in re.finditer(rb'beginbfrange(.*?)endbfrange', cs, re.S):
        for lo,hi,dst in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>',
                                    blk.group(1)):
            lo,hi,d0 = int(lo,16), int(hi,16), int(dst,16)
            for k in range(lo, min(hi, lo+4096)+1): mp[k] = chr(d0+(k-lo))
    cmaps[num] = mp

NUM = rb'-?[\d.]+'
TOK = re.compile(
    rb'\b(q)\b|\b(Q)\b'
    rb'|(%s)\s+(%s)\s+(%s)\s+(%s)\s+(%s)\s+(%s)\s+cm' % ((NUM,)*6) +
    rb'|/(\w+)\s+(%s)\s+Tf' % NUM +
    rb'|(%s)\s+(%s)\s+(%s)\s+(%s)\s+(%s)\s+(%s)\s+Tm' % ((NUM,)*6) +
    rb'|(%s)\s+(%s)\s+(?:Td|TD)' % (NUM, NUM) +
    rb'|<([0-9A-Fa-f]+)>\s*Tj'
    rb'|\((.*?)(?<!\\)\)\s*Tj'
    rb'|\b(BT)\b', re.S)

def font_table(page_body):
    res = re.search(rb'/Font\s*<<(.*?)>>', page_body, re.S)
    src = res.group(1) if res else page_body
    return {n.decode(): int(r) for n, r in re.findall(rb'/(\w+)\s+(\d+)\s+\d+\s+R', src)}

def extract(content, ftab):
    ident = (1.0,0.0,0.0,1.0,0.0,0.0)
    ctm, stack = ident, []
    tm = ident; tx = ty = 0.0; font = None
    glyphs = []
    def dec(hx):
        cm = cmaps.get(ftab.get(font, -1), {})
        raw = bytes.fromhex(hx.decode())
        return ''.join(cm.get(int.from_bytes(raw[i:i+2],'big'), '')
                       for i in range(0, len(raw)-1, 2))
    def place(s):
        if not s: return
        ex, ey = apply(tm, tx, ty)
        dx, dy = apply(ctm, ex, ey)
        glyphs.append((round(dy, 1), dx, s))
    for m in TOK.finditer(content):
        g = m.groups()
        if g[0]: stack.append(ctm)
        elif g[1]:
            if stack: ctm = stack.pop()
        elif g[2] is not None:
            ctm = mul(tuple(float(v) for v in g[2:8]), ctm)
        elif g[8]: font = g[8].decode()
        elif g[10] is not None:
            tm = tuple(float(v) for v in g[10:16]); tx = ty = 0.0
        elif g[16] is not None:
            tx += float(g[16]); ty += float(g[17])
        elif g[18] is not None: place(dec(g[18]))
        elif g[19] is not None: place(g[19].decode('latin-1'))
        elif g[20]:
            tm = ident; tx = ty = 0.0
    return glyphs

def lay_out(glyphs, tol=1.2):
    if not glyphs: return []
    rows, cur, last = [], [], None
    for y, x, s in sorted(glyphs, key=lambda t: (-t[0], t[1])):
        if last is None or abs(y - last) <= tol: cur.append((x, s))
        else: rows.append(cur); cur = [(x, s)]
        last = y if last is None else last if abs(y-last) <= tol else y
    rows.append(cur)
    return [''.join(s for _, s in sorted(r, key=lambda t: t[0])).rstrip() for r in rows]

pages = next(b for b in objs.values() if re.search(rb'/Type\s*/Pages', b))
kids = [int(k) for k in re.findall(rb'(\d+)\s+\d+\s+R',
        re.search(rb'/Kids\s*\[(.*?)\]', pages, re.S).group(1))]

for i, pn in enumerate(kids, 1):
    body = objs.get(pn, b'')
    cref = re.search(rb'/Contents\s+(\d+)\s+\d+\s+R', body)
    if not cref: continue
    cs = inflate(objs.get(int(cref.group(1)), b''))
    if not cs: continue
    print('\n' + '='*74 + '\nPAGE %d\n' % i + '='*74)
    for ln in lay_out(extract(cs, font_table(body))):
        if ln.strip(): print(ln)
