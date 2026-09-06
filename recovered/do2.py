import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
from scipy.optimize import curve_fit
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=g["ROWS"]; L="spdfg"
for r in ROWS:
    r["nl"]=r["n0"]+r["l"]; r["nstar"]=r["n0"]-r["d"]
print("  IS THE SLOPE ONE HALF?   n* = a + s·(n+ℓ)\n")
NL=np.array([r["nl"] for r in ROWS],float)
NS=np.array([r["nstar"] for r in ROWS])
NE=np.array([r["ne"] for r in ROWS],float)
C=np.array([r["c"] for r in ROWS],float)
r=SS.linregress(NL,NS)
print(f"      all {len(ROWS)} channels : a = {r.intercept:+.4f}  s = {r.slope:.4f}"
      f"   r² {r.rvalue**2:.4f}")
print()
print("      but a and s must depend on the SPECIES — the DO potential has a")
print("      coupling w and a scale R, and those are what the core supplies.\n")
bysp=defaultdict(list)
for x in ROWS: bysp[(x["Z"],x["c"])].append(x)
EL={3:"Li",11:"Na",12:"Mg",13:"Al",19:"K",20:"Ca",37:"Rb",38:"Sr",39:"Y",
    55:"Cs",56:"Ba",30:"Zn",48:"Cd",80:"Hg",83:"Bi",14:"Si",15:"P",16:"S",
    18:"Ar",26:"Fe",22:"Ti",21:"Sc",31:"Ga",32:"Ge",4:"Be",5:"B",6:"C"}
RO={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",9:"IX",11:"XI",15:"XV",16:"XVI"}
print(f"      {'species':<10}{'Nₑ':>5}{'n':>4}{'a':>9}{'s':>8}{'r²':>8}")
SL=[]
for k,v in sorted(bysp.items(),key=lambda z:-len(z[1]))[:16]:
    if len(v)<4: continue
    x=np.array([z["nl"] for z in v],float); y=np.array([z["nstar"] for z in v])
    if len(set(x))<3: continue
    rr=SS.linregress(x,y)
    print(f"      {EL.get(k[0],k[0])+' '+RO.get(k[1],str(k[1])):<10}"
          f"{v[0]['ne']:>5}{len(v):>4}{rr.intercept:>9.3f}{rr.slope:>8.4f}{rr.rvalue**2:>8.4f}")
    SL.append((v[0]["ne"],k[1],rr.intercept,rr.slope,rr.rvalue**2))
print()
if len(SL)>=6:
    ss=[z[3] for z in SL if z[4]>0.7]
    print(f"      {len(ss)} species with r² > 0.7 : median slope {st.median(ss):.4f}"
          f"   sd {st.pstdev(ss):.4f}")
    print(f"      how many within ±0.1 of ½ : {sum(1 for z in ss if abs(z-0.5)<0.1)}/{len(ss)}")
    print()
    aa=[z[2] for z in SL if z[4]>0.7]
    ne=[z[0] for z in SL if z[4]>0.7]; cc=[z[1] for z in SL if z[4]>0.7]
    r1=SS.linregress(np.log(ne),aa)
    print(f"      intercept a against ln Nₑ : slope {r1.slope:+.4f}  r² {r1.rvalue**2:.3f}")
    r2=SS.linregress(cc,aa)
    print(f"      intercept a against charge: slope {r2.slope:+.4f}  r² {r2.rvalue**2:.3f}")
print()
print("  THE DO FORM WITH s FIXED AT ½\n")
print("      n* = a(species) + (n+ℓ)/2      →      E = −c²R/[a + (n+ℓ)/2]²\n")
res=[]
for k,v in bysp.items():
    if len(v)<3: continue
    x=np.array([z["nl"] for z in v],float); y=np.array([z["nstar"] for z in v])
    a=float(np.mean(y-0.5*x))
    res += list(y-(a+0.5*x))
res=np.array(res)
print(f"      {len(res)} channels · rms of n* {float(np.sqrt(np.mean(res**2))):.4f}")
print(f"      against the spread of n* itself: {float(np.std(NS)):.4f}")
print(f"      → the fixed-½ form explains "
      f"{100*(1-np.var(res)/np.var(NS)):.1f}% of n*'s variance")