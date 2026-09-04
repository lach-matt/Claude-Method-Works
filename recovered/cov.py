import re, math
from collections import defaultdict
src=open('/mnt/user-data/uploads/The_Method_1_2-3.md').read().split('\n')[7336:7656]
R=109737.31568; LMAP={'s':0,'p':1,'d':2,'f':3,'g':4,'h':5,'i':6,'k':7}
rows=[]
for line in src:
    m=re.search(r'(\d+)[–-](\d+)\s+(\d+)\s+(\d+)\s+(\d+)/(\d+)\s+(\d+\.\d+)[–-](\d+\.\d+)\s+([+-]\d+\.\d{4})\s+(\d+\.\d+)\s+(\d+)\s+([\d,]+\.\d+)\s*$',line)
    if not m: continue
    nlo,nhi,mem,cells,bk,bt,nulo,nuhi,dbar,spread,zeff,lim=m.groups()
    head=line[:m.start()].strip()
    sm=re.match(r'([A-Z][a-z]?\s+[IVX]+)\s+(.*)$',head)
    if not sm: continue
    om=re.search(r'n([spdfghik])',sm.group(2))
    if not om: continue
    rows.append(dict(sp=re.sub(r'\s+',' ',sm.group(1)),l=LMAP[om.group(1)],
        nlo=int(nlo),nhi=int(nhi),cells=int(cells),d=float(dbar),
        numax=float(nuhi),zeff=int(zeff)))
tot_cells=sum(r['cells'] for r in rows)
print(f"channels {len(rows)}, interior cells {tot_cells}")
bysp=defaultdict(lambda: defaultdict(list))
for r in rows: bysp[r['sp']][r['l']].append(r)
sig=0.01; gained=0; blocked_mono=0; blocked_adm=0; nopartner=0
detail=defaultdict(int)
for sp,byl in bysp.items():
    for l,chs in byl.items():
        for ch in chs:
            partners=byl.get(l+1,[])+byl.get(l-1,[])
            if not partners: nopartner+=ch['cells']; continue
            best=None
            for p in partners:
                lo,hi=max(ch['nlo'],p['nlo']),min(ch['nhi'],p['nhi'])
                if hi<lo: continue
                hi_l,lo_l=(ch,p) if ch['l']<p['l'] else (p,ch)
                dd=hi_l['d']-lo_l['d']
                if dd<=0: continue
                nu_exit=(2*R*dd/(5*sig))**(1/3)
                ov=min(hi,int(min(nu_exit+ max(ch['d'],0),ch['nhi'])))-lo+1
                if ov>0 and (best is None or ov>best): best=ov
            if best is None:
                ok_mono=any((p['d']-ch['d'] if p['l']<ch['l'] else ch['d']-p['d'])>0 for p in partners)
                if ok_mono: blocked_adm+=ch['cells']
                else: blocked_mono+=ch['cells']
            else:
                g=min(best,ch['cells']); gained+=g; detail[l]+=g
print(f"\ncells with an admissible l-neighbour: {gained} / {tot_cells} = {100*gained/tot_cells:.1f}%")
print(f"  blocked by non-monotone delta : {blocked_mono}")
print(f"  blocked by r_l exit           : {blocked_adm}")
print(f"  no l-partner channel at all   : {nopartner}")
print("\ngained cells by l:")
for l in sorted(detail): print(f"   l={l}: {detail[l]}")
print("\ncells per l (all channels):")
c=defaultdict(int)
for r in rows: c[r['l']]+=r['cells']
for l in sorted(c): print(f"   l={l}: {c[l]}")