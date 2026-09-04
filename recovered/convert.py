import re,sys,collections
src=open(sys.argv[1],encoding='utf-8').read()
L=src.split('\n')
def find(prefix,start=0):
    for i in range(start,len(L)):
        if L[i].startswith(prefix): return i
    raise SystemExit('not found: '+prefix)
# reader-compendium FILE blocks, located by content
blocks={}
for name in ['Mathematical_Compendium','Spectra_Compendium','The_Index_of_Indices','The_Physics_Compendium']:
    a=find(f'<<<FILE: The_Method_1_6___{name}-2.md>>>'); b=find(f'<<<END FILE: The_Method_1_6___{name}-2.md>>>',a); blocks[name]=(a,b)
ma,mb=blocks['Mathematical_Compendium']
secV=find('# V · THE CHAINS',ma); secVI=find('# VI · WHAT IS UNFINISHED',secV); secVII=find('# VII · THE BIBLIOGRAPHY',secVI)
HEAD=re.compile(r'^(#{2,3}) `([A-Za-z0-9]+\.[A-Za-z0-9_]+)` — (.+?)\s*$')
META=re.compile(r'^grade \*\*([A-Z][A-Z ]*)\*\*· source \*(.*?)\*(?:· depends on (.*?))?(?:· \d+ objects? depends? on it)?(?:· depth \d+)?\s*$')
TOK=re.compile(r'`([A-Z][A-Za-z0-9]*\.[A-Za-z0-9_]+)`')
# pass 1: table handle -> (title, pointer) over the whole Math block (entries live in IV and VI)
table={}; heads=[]
for i in range(ma,mb):
    m=HEAD.match(L[i])
    if m:
        h,title=m.group(2),m.group(3)
        # source for the pointer: the first metadata line before the next header
        src_=None
        for j in range(i+1,min(i+40,mb)):
            if HEAD.match(L[j]) or L[j].startswith('# '): break
            mm=META.match(L[j])
            if mm: src_=mm.group(2); break
        ptr=None
        if src_:
            s=re.search(r'§([0-9A-Z]+(?:\.[0-9]+)*)',src_); r=re.search(r'\bR (\d{3,4})',src_)
            ptr=f'§{s.group(1)}' if s else (f'register {r.group(1)}' if r else None)
        table[h]=(title,ptr); heads.append(i)
coll=collections.Counter(t for t,_ in table.values()); collisions={t:n for t,n in coll.items() if n>1}
# pass 2: rewrite
out=L[:]; stats=collections.Counter(); unknown=collections.Counter()
def in_reader(i):
    for a,b in blocks.values():
        if a<i<b: return True
    return False
def skip(i): return (secV<=i<secVI) or (secVII<=i<mb)   # chains (pending ruling) and bibliography (task 3)
entry_start=None; seen=set()
for i in range(len(L)):
    if not in_reader(i) or skip(i): continue
    l=L[i]
    if l.startswith('#'):
        entry_start=i; seen=set()
        m=HEAD.match(l)
        if m:
            title=m.group(3); out[i]=f"{m.group(1)} {title[0].upper()+title[1:]}"; stats['headers']+=1; self_h=m.group(2); seen={self_h}
        continue
    mm=META.match(l)
    if mm:
        g=mm.group(1).capitalize(); s=mm.group(2).strip()
        out[i]=f"{g} — {s}" + ('' if s.endswith('.') else '.'); stats['metadata lines']+=1; continue
    def rep(m):
        h=m.group(1)
        if h not in table: unknown[h]+=1; return m.group(0)
        title,ptr=table[h]; stats['body tokens']+=1
        first = h not in seen; seen.add(h)
        return title + (f' ({ptr})' if (first and ptr) else '')
    nl=TOK.sub(rep,l)
    nl=nl.replace('> **PRIOR ART:','> **Prior art:'); 
    if nl!=l: stats['lines changed']+=1
    out[i]=nl
open(sys.argv[2],'w',encoding='utf-8',newline='').write('\n'.join(out))
print('table size',len(table),'| title collisions',collisions)
print('stats',dict(stats)); print('unknown handles',dict(unknown))
# residual handle tokens per block after conversion
for name,(a,b) in blocks.items():
    res=sum(len(TOK.findall(out[i])) for i in range(a,b) if not skip(i)); print(f'residual tokens {name}: {res}')
print('section V tokens (untouched):',sum(len(TOK.findall(out[i])) for i in range(secV,secVI)),'| bibliography tokens (untouched):',sum(len(TOK.findall(out[i])) for i in range(secVII,mb)))