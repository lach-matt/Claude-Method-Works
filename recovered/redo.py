import re, math
from collections import defaultdict
src=open('/mnt/user-data/uploads/The_Method_1_2-3.md').read().split('\n')[7336:7656]
R=109737.31568; LMAP={'s':0,'p':1,'d':2,'f':3,'g':4,'h':5,'i':6}
rows=[]
for line in src:
    m=re.search(r'(\d+)[–-](\d+)\s+(\d+)\s+(\d+)\s+(\d+)/(\d+)\s+(\d+\.\d+)[–-](\d+\.\d+)\s+([+-]\d+\.\d{4})\s+(\d+\.\d+)\s+(\d+)\s+([\d,]+\.\d+)\s*$',line)
    if not m: continue
    nlo,nhi,mem,cells,bk,bt,nulo,nuhi,dbar,spread,zeff,lim=m.groups()
    head=line[:m.start()].strip()
    sm=re.match(r'([A-Z][a-z]?\s+[IVX]+)\s+(.*)$',head)
    if not sm: continue
    sp=re.sub(r'\s+',' ',sm.group(1)); ch=re.sub(r'\s+',' ',sm.group(2))
    om=re.search(r'n([spdfghi])',ch)
    if not om: continue
    l=LMAP[om.group(1)]
    core=ch[:om.start()].strip()          # parent / core configuration
    term=ch[om.end():].strip()            # term symbol + J
    mult=re.match(r'([¹²³⁴⁵⁶⁷]|\d)',term)
    mult=mult.group(1) if mult else '?'
    J=re.search(r'J=(\S+)',term); J=J.group(1) if J else ''
    rows.append(dict(sp=sp,ch=ch,l=l,d=float(dbar),cells=int(cells),
                     core=core,mult=mult,J=J,numax=float(nuhi),zeff=int(zeff)))
print(f"parsed {len(rows)} channels, {sum(r['cells'] for r in rows)} interior cells")

def scan(keyfn,label):
    g=defaultdict(dict)
    for r in rows:
        k=keyfn(r)
        if r['l'] not in g[k] or abs(r['d'])<abs(g[k][r['l']]['d']): g[k][r['l']]=r
    pairs=[];viol=[];sign=[]
    for k,byl in g.items():
        ls=sorted(byl)
        for i in range(len(ls)-1):
            if ls[i+1]!=ls[i]+1: continue          # only ADJACENT l
            a,b=byl[ls[i]],byl[ls[i+1]]
            pairs.append((k,ls[i],ls[i+1]))
            if a['d']*b['d']<0: sign.append((k,ls[i],ls[i+1],a['d'],b['d']))
            elif b['d']>=a['d']: viol.append((k,ls[i],ls[i+1],a['d'],b['d']))
    print(f"\n{label}")
    print(f"  groups {len(g)}   adjacent-l pairs {len(pairs)}")
    print(f"  SIGN-CHANGE (test 1 fails, excluded before bracketing): {len(sign)}")
    print(f"  NON-MONOTONE with same sign (test 2 fails): {len(viol)}")
    ok=len(pairs)-len(sign)-len(viol)
    print(f"  pass tests 1+2: {ok}  ({100*ok/len(pairs):.1f}%)")
    for s in sign[:8]: print(f"     sign: {s[0]} l{s[1]}->{s[2]}  {s[3]:+.4f} -> {s[4]:+.4f}")
    for s in viol[:8]: print(f"     rise: {s[0]} l{s[1]}->{s[2]}  {s[3]:+.4f} -> {s[4]:+.4f}")
    return pairs,sign,viol

scan(lambda r:r['sp'], "A) OLD GROUPING - species only (this is what produced 11.2%)")
scan(lambda r:(r['sp'],r['core'],r['mult']), "B) NEW GROUPING - species + parent core + multiplicity (B.2.1)")