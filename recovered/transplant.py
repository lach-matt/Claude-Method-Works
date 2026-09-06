#!/usr/bin/env python3
# Transplant native markup (italics, bold, pipe tables) from the-lach-cylinder.md
# into BOOK-restored.md, only where stripped content matches exactly.
import re, collections

nat=open('native.md',encoding='utf-8').read()
res=open('BOOK-restored.md',encoding='utf-8').read()

def strip_md(t):
    t=t.replace('**','').replace('*','').replace('`','')
    t=t.replace('\\|','|').replace('|',' ')
    t=re.sub(r'\\([^\s\\]{0,16}?)\\', r'\1', t)
    t=t.replace('\\','')
    t=re.sub(r'[\s—–\-·]+',' ',t)
    return t.strip()

def norm(t): return strip_md(t).lower()

# ---------- native blocks ----------
nlines=nat.split('\n')
nblocks=[]; buf=[]
for ln in nlines:
    if not ln.strip():
        if buf: nblocks.append(buf); buf=[]
    else: buf.append(ln)
if buf: nblocks.append(buf)

para_map={}
table_list=[]
for bl in nblocks:
    if bl[0].lstrip().startswith('|'):
        cells=[]
        for l in bl:
            if re.match(r'^\s*\|[\s\-:|]+\|\s*$',l): continue
            cells+= [norm(c) for c in l.strip().strip('|').split('|')]
        toks=tuple(sorted(t for c in cells for t in c.split() if t))
        table_list.append((toks,bl))
    elif bl[0].startswith('#') or bl[0].startswith('---'):
        continue
    else:
        text=' '.join(bl)
        para_map.setdefault(norm(text), text)

# ---------- walk restored blocks ----------
rlines=res.split('\n')
out=[]; buf=[]
stats=collections.Counter()
TBL=re.compile(r'\S {3,}\S')

def flush(buf):
    if not buf: out.extend(buf) or None
    if not buf: return
    first=buf[0]
    joined=' '.join(l.strip() for l in buf)
    heading=first.startswith('#')
    figcap=first.strip().startswith('Figure ')
    tabley=sum(1 for l in buf if TBL.search(l.strip()))>=2 and len(buf)>=2
    if heading or figcap:
        out.extend(buf); stats['kept_other']+=1; return
    if tabley:
        toks=tuple(sorted(t for l in buf for t in norm(l).split() if t))
        best=None
        for ntoks,nbl in table_list:
            if ntoks==toks: best=nbl; break
        if best:
            out.extend(best); stats['tables_swapped']+=1
        else:
            out.extend(buf); stats['tables_kept']+=1
        return
    key=norm(joined)
    if key and key in para_map and strip_md(para_map[key])==strip_md(joined):
        native_text=para_map[key]
        wrapped=[' '+native_text[i:i+100] for i in range(0,0)]  # keep single line
        out.append(' '+native_text)
        stats['paras_swapped']+=1
    else:
        out.extend(buf); stats['paras_kept']+=1

for ln in rlines:
    if not ln.strip():
        flush(buf); buf=[]; out.append(ln)
    else:
        buf.append(ln)
flush(buf)

merged='\n'.join(out)

# ---------- content invariance over the whole file ----------
def flat(t):
    return re.sub(r'\s+',' ',strip_md(re.sub(r'^\s*\|[\s\-:|]+\|\s*$','',t,flags=re.M))).strip().lower()
a=flat(res); b=flat(merged)
same = a==b
print("stats:",dict(stats))
print("content invariant:", same)
if not same:
    # locate first divergence for the report
    import difflib
    i=next((i for i,(x,y) in enumerate(zip(a,b)) if x!=y), min(len(a),len(b)))
    print("first divergence @",i,":", repr(a[i-60:i+60]),"VS",repr(b[i-60:i+60]))
open('BOOK-restored.md','w',encoding='utf-8').write(merged)
print("written")
