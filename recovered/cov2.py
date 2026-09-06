import re, math
from collections import defaultdict
src=open('/mnt/user-data/uploads/The_Method_1_2-3.md').read().split('\n')[7336:7656]
R=109737.31568; LMAP={'s':0,'p':1,'d':2,'f':3,'g':4,'h':5,'i':6}; SIG=0.01
rows=[]
for line in src:
    m=re.search(r'(\d+)[–-](\d+)\s+(\d+)\s+(\d+)\s+(\d+)/(\d+)\s+(\d+\.\d+)[–-](\d+\.\d+)\s+([+-]\d+\.\d{4})\s+(\d+\.\d+)\s+(\d+)\s+([\d,]+\.\d+)\s*$',line)
    if not m: continue
    nlo,nhi,mem,cells,bk,bt,nulo,nuhi,dbar,spread,zeff,lim=m.groups()
    head=line[:m.start()].strip()
    sm=re.match(r'([A-Z][a-z]?\s+[IVX]+)\s+(.*)$',head)
    if not sm: continue
    ch=re.sub(r'\s+',' ',sm.group(2)); om=re.search(r'n([spdfghi])',ch)
    if not om: continue
    term=ch[om.end():].strip(); mu=re.match(r'([¹²³⁴⁵⁶⁷]|\d)',term)
    rows.append(dict(sp=re.sub(r'\s+',' ',sm.group(1)),l=LMAP[om.group(1)],d=float(dbar),
        cells=int(cells),nlo=int(nlo),nhi=int(nhi),numax=float(nuhi),zeff=int(zeff),
        core=ch[:om.start()].strip(),mult=mu.group(1) if mu else '?',ch=ch))
TOT=sum(r['cells'] for r in rows)
print(f"channels {len(rows)}  interior cells {TOT}")
g=defaultdict(lambda: defaultdict(list))
for r in rows: g[(r['sp'],r['core'],r['mult'])][r['l']].append(r)

buckets=defaultdict(int); detail=defaultdict(int)
for k,byl in g.items():
    for l,chs in byl.items():
        for ch in chs:
            best=0; why='no l-partner in the collection'
            for dl in (-1,1):
                for p in byl.get(l+dl,[]):
                    hi_l,lo_l=(ch,p) if ch['l']<p['l'] else (p,ch)
                    # test 1: sign
                    if hi_l['d']*lo_l['d']<0:
                        why='test 1 - delta changes sign'; continue
                    dd=hi_l['d']-lo_l['d']
                    # test 2: strictly decreasing
                    if abs(dd)<1e-9: why='degenerate - hydrogenic, zero-width bracket'; continue
                    if dd<0: why='test 2 - delta rises with l'; continue
                    # n overlap
                    lo,hi=max(ch['nlo'],p['nlo']),min(ch['nhi'],p['nhi'])
                    if hi<lo: why='n ranges do not overlap'; continue
                    # test 3: r_l >= 5 within the overlap
                    nu_exit=(2*R*dd/(5*SIG))**(1/3)
                    hi=min(hi,int(nu_exit+max(ch['d'],0)))
                    if hi<lo: why='test 3 - r_l exits below the overlap'; continue
                    best=max(best,hi-lo+1)
            gained=min(best,ch['cells'])
            buckets['GAIN']+=gained
            if gained<ch['cells']:
                buckets[why if best==0 else 'outside the n-overlap']+=ch['cells']-gained
            if gained: detail[l]+=gained
print(f"\nCELL-LEVEL COVERAGE, three admissibility tests applied")
print(f"  {'cells with an admissible l-neighbour':52s} {buckets['GAIN']:5d}   {100*buckets['GAIN']/TOT:.1f}%")
for k in sorted(buckets):
    if k!='GAIN': print(f"  {k:52s} {buckets[k]:5d}   {100*buckets[k]/TOT:.1f}%")
print(f"  {'TOTAL':52s} {sum(buckets.values()):5d}")
print(f"\n  by l:  "+"  ".join(f"l={l}:{detail[l]}" for l in sorted(detail)))
print(f"\n  previous figure (defective scan, no tests): 685 / 1000 = 68.5%")
print(f"  corrected figure                          : {buckets['GAIN']} / {TOT} = {100*buckets['GAIN']/TOT:.1f}%")