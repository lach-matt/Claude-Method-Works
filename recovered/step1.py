import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("/tmp/cross.py",encoding="utf-8").read()
src=src[:src.index('print("  PLUGGING δ INTO')]
g={}; exec(src,g)
H=g["H"]; cfg=g["cfg"]; cp_=g["cp_"]; par=g["par"]; L="spdfg"
EL={1:"H",2:"He",3:"Li",4:"Be",5:"B",6:"C",7:"N",8:"O",9:"F",10:"Ne",11:"Na",
12:"Mg",13:"Al",14:"Si",15:"P",16:"S",17:"Cl",18:"Ar",19:"K",20:"Ca",21:"Sc",
22:"Ti",26:"Fe",29:"Cu",30:"Zn",31:"Ga",32:"Ge",37:"Rb",38:"Sr",39:"Y",47:"Ag",
48:"Cd",49:"In",55:"Cs",56:"Ba",79:"Au",80:"Hg",81:"Tl",83:"Bi",50:"Sn",54:"Xe"}
RO={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",11:"XI",
15:"XV",16:"XVI"}
sp=defaultdict(list)
for (Z,c,l,S),d in H.items():
    ne=Z-c+1
    if Z>92 or c>10 or l>5: continue
    if par(cfg(ne-1,c))>1: continue
    p=cp_(ne-1,l,c)
    sp[(Z,c)].append(dict(l=l,S=S,d=d,p=p,ne=ne))
print("  STEP 1 · ONE EQUATION PER SPECIES    δ = a·√p\n")
print("      a is the only free number. p = the core's orbital count at that ℓ,")
print("      fixed by the ground configuration. Nothing else varies inside a species.\n")
print(f"      {'species':<10}{'Nₑ':>5}{'chg':>4}{'n':>3}{'a':>9}{'rms':>8}{'R²':>8}{'  ℓ present'}")
OUT=[]
for k,v in sorted(sp.items(), key=lambda z:(z[0][1],z[0][0])):
    pen=[x for x in v if x["p"]>0 and x["d"]>0.02]
    if len(pen)<2: continue
    S_=np.array([math.sqrt(x["p"]) for x in pen]); D=np.array([x["d"] for x in pen])
    a=float(np.sum(S_*D)/np.sum(S_**2))
    r=D-a*S_; rms=float(np.sqrt(np.mean(r**2)))
    R2=1-np.var(r)/np.var(D) if np.var(D)>1e-12 else float("nan")
    nm=f"{EL.get(k[0],k[0])} {RO.get(k[1],k[1])}"
    ls="".join(sorted({L[x['l']] for x in pen}))
    print(f"      {nm:<10}{pen[0]['ne']:>5}{k[1]:>4}{len(pen):>3}{a:>9.4f}"
          f"{rms:>8.4f}{R2:>8.3f}   {ls}")
    OUT.append((k[0],k[1],pen[0]["ne"],a,rms,R2,len(pen)))
print(f"\n      {len(OUT)} species fitted\n")
aa=[o[3] for o in OUT]
print(f"      a ranges {min(aa):.3f} – {max(aa):.3f}   median {st.median(aa):.4f}")
good=[o for o in OUT if o[5]==o[5] and o[5]>0.8]
print(f"      {len(good)} with R² > 0.8")
import json
json.dump([list(o) for o in OUT],open("/tmp/step1.json","w"))