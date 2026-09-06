import re, math
from collections import defaultdict

src=open('/mnt/user-data/uploads/The_Method_1_2-3.md').read().split('\n')[7336:7656]
R=109737.31568

LMAP={'s':0,'p':1,'d':2,'f':3,'g':4,'h':5,'i':6,'k':7}
rows=[]
for line in src:
    # channel rows have a numeric limit with a comma and a signed delta-bar
    m=re.search(r'([+-]\d+\.\d{4})\s+(\d+\.\d+)\s+(\d+)\s+([\d,]+\.\d+)\s*$', line)
    if not m: continue
    dbar=float(m.group(1)); spread=float(m.group(2)); zeff=int(m.group(3))
    limit=float(m.group(4).replace(',',''))
    head=line[:m.start()].strip()
    # nu range like 4.0-55.0 just before
    nm=re.search(r'(\d+\.\d+)[–-](\d+\.\d+)\s*$', head)
    numin,numax=(float(nm.group(1)),float(nm.group(2))) if nm else (None,None)
    if nm: head=head[:nm.start()].strip()
    # species = first token(s) up to the channel designation
    sm=re.match(r'([A-Z][a-z]?\s+[IVX]+)\s+(.*)$', head)
    if not sm: continue
    sp=re.sub(r'\s+',' ',sm.group(1)); rest=sm.group(2)
    # orbital letter: the n<letter> pattern
    om=re.search(r'\bn([spdfghik])\b', rest)
    if not om: om=re.search(r'n([spdfghik])', rest)
    if not om: continue
    l=LMAP[om.group(1)]
    # parent/term signature = everything except the n<letter> token
    core=rest[:om.start()].strip()
    term=rest[om.end():].strip()
    rows.append(dict(sp=sp,ch=re.sub(r'\s+',' ',rest),l=l,d=dbar,spread=spread,
                     zeff=zeff,limit=limit,numin=numin,numax=numax,core=core,term=term))

print(f"parsed {len(rows)} channel rows")
bysp=defaultdict(list)
for r in rows: bysp[r['sp']].append(r)
print(f"species: {len(bysp)}")

print("\n"+"="*74)
print("TEST D1 — is delta-bar monotone decreasing in l, within a species?")
print("="*74)
pairs=[]
for sp,rs in sorted(bysp.items()):
    byl=defaultdict(list)
    for r in rs: byl[r['l']].append(r)
    ls=sorted(byl)
    if len(ls)<2: continue
    # use the MINIMUM |delta| per l as the channel-representative (least perturbed)
    rep={l:min(byl[l],key=lambda r:abs(r['d'])) for l in ls}
    seq=[(l,rep[l]['d']) for l in ls]
    viol=[(ls[i],ls[i+1]) for i in range(len(ls)-1) if rep[ls[i+1]]['d']>rep[ls[i]]['d']]
    flag="OK " if not viol else "VIOL"
    print(f" {flag} {sp:8s} " + "  ".join(f"l={l}:{d:+.4f}" for l,d in seq)
          + ("" if not viol else f"   <- rises at {viol}"))
    for i in range(len(ls)-1):
        la,lb=ls[i],ls[i+1]
        pairs.append(dict(sp=sp,la=la,lb=lb,dd=rep[la]['d']-rep[lb]['d'],
                          zeff=rep[la]['zeff'],
                          numax=max(x for x in (rep[la]['numax'],rep[lb]['numax']) if x)))

nviol=sum(1 for p in pairs if p['dd']<=0)
print(f"\n adjacent-l pairs: {len(pairs)}   monotone-decreasing: {len(pairs)-nviol}"
      f"   VIOLATIONS: {nviol}  ({100*nviol/len(pairs):.1f}%)")

print("\n by l-pair:")
agg=defaultdict(lambda:[0,0])
for p in pairs:
    k=(p['la'],p['lb']); agg[k][0]+=1
    if p['dd']<=0: agg[k][1]+=1
for k in sorted(agg):
    n,v=agg[k]; print(f"   l={k[0]}->{k[1]}:  {n:3d} pairs, {v:3d} violations ({100*v/n:.0f}%)")

print("\n"+"="*74)
print("TEST D2/D3 — admissibility r_l = 2*R*Ddelta/(nu^3 sigma) >= 5, sigma=0.01 cm^-1")
print("="*74)
sig=0.01
adm=0; tot=0
print(f" {'species':9s} {'pair':7s} {'Ddelta':>9s} {'nu_max obs':>10s} {'nu_exit':>9s}  verdict")
for p in sorted(pairs,key=lambda x:-abs(x['dd'])):
    if p['dd']<=0: continue
    tot+=1
    nu_exit=(2*R*p['dd']/(5*sig))**(1/3)
    ok = nu_exit >= p['numax']
    if ok: adm+=1
    if tot<=12 or not ok:
        print(f" {p['sp']:9s} l={p['la']}->{p['lb']}  {p['dd']:9.4f} {p['numax']:10.1f} {nu_exit:9.1f}  "
              + ("admissible over full range" if ok else "EXITS INSIDE the measured range"))
print(f"\n monotone pairs: {tot}   admissible over their full measured nu range: {adm}"
      f"   exit inside range: {tot-adm}")
