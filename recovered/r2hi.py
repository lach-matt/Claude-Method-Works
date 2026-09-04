import math, statistics as st
import numpy as np
from collections import Counter
from scipy import stats as SS
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=g["ROWS"]; L="spdfg"
EL={11:"Na",12:"Mg",13:"Al",14:"Si",15:"P",16:"S",17:"Cl",18:"Ar",19:"K",20:"Ca",
    30:"Zn",31:"Ga",32:"Ge",37:"Rb",38:"Sr",39:"Y",48:"Cd",49:"In",55:"Cs",
    56:"Ba",80:"Hg",81:"Tl",83:"Bi",26:"Fe",21:"Sc",22:"Ti",5:"B",6:"C",4:"Be"}
RO={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",9:"IX",11:"XI",15:"XV",16:"XVI"}
r2=[r for r in ROWS if r["reg"]==2]
print(f"  REGIME 2 — {len(r2)} channels, by electron count\n")
print(f"      {'Nₑ':>4}{'species':>10}{'ℓ':>3}{'p':>3}{'δ':>9}{'δ/√p':>9}")
for r in sorted(r2,key=lambda x:x["ne"]):
    print(f"      {r['ne']:>4}{EL.get(r['Z'],r['Z'])+' '+RO.get(r['c'],str(r['c'])):>10}"
          f"{L[r['l']]:>3}{r['p']:>3}{r['d']:>9.4f}{r['d']/math.sqrt(r['p']):>9.4f}")
print()
print("  IS √p RIGHT IN REGIME 2, AND HOW FAR DOES Nₑ REACH?\n")
ne=[r["ne"] for r in r2]
print(f"      Nₑ range {min(ne)} – {max(ne)}   ·   La needs Nₑ = 57")
print(f"      p values present: " + "  ".join(f"{k}:{v}" for k,v in
      sorted(Counter(r['p'] for r in r2).items())))
print()
y=np.array([r["d"] for r in r2]); P=np.array([r["p"] for r in r2],float)
NE=np.array([r["ne"] for r in r2],float); C=np.array([r["c"] for r in r2],float)
T=np.log(C+1)/C
print(f"      {'form':<28}{'rms':>9}{'R²':>9}{'δ(6p) at La':>14}")
def tryit(nm,f,p0):
    from scipy.optimize import curve_fit
    try:
        pr,_=curve_fit(f,np.arange(len(y)),y,p0=p0,maxfev=800000)
    except Exception:
        print(f"      {nm:<28}   failed"); return
    r=y-f(None,*pr); s=float(np.sqrt(np.mean(r**2)))
    # predict 6p at La: Ne=57, p=4, c=1
    globals()["_P"]=np.array([4.0]); globals()["_NE"]=np.array([57.0])
    globals()["_T"]=np.array([math.log(2)])
    pred=f.__wrapped__(pr) if hasattr(f,"__wrapped__") else None
    print(f"      {nm:<28}{s:>9.4f}{1-np.var(r)/np.var(y):>9.4f}", end="")
    return pr
from scipy.optimize import curve_fit
def fit(nm, model, la, p0):
    best=None
    for q0 in p0:
        try:
            pr,_=curve_fit(model,np.arange(len(y)),y,p0=q0,maxfev=800000)
            r=y-model(None,*pr); s=float(np.sqrt(np.mean(r**2)))
            if best is None or s<best[1]: best=(pr,s)
        except Exception: pass
    if best is None: print(f"      {nm:<28}   failed"); return
    pr,s=best; r=y-model(None,*pr)
    print(f"      {nm:<28}{s:>9.4f}{1-np.var(r)/np.var(y):>9.4f}{la(pr):>14.3f}")
fit("a₂·√p·Nₑ^k·t",
    lambda _,a2,k: a2*np.sqrt(P)*NE**k*T,
    lambda pr: pr[0]*2*57**pr[1]*math.log(2), [[0.5,0.45]])
fit("a₂·p^e·Nₑ^k·t  (e free)",
    lambda _,a2,e,k: a2*P**e*NE**k*T,
    lambda pr: pr[0]*4**pr[1]*57**pr[2]*math.log(2), [[0.5,0.5,0.45]])
fit("a₂·√p·Nₑ^k·t  (k free, e=½)",
    lambda _,a2,k: a2*np.sqrt(P)*NE**k*T,
    lambda pr: pr[0]*2*57**pr[1]*math.log(2), [[0.5,0.40],[0.6,0.35]])
fit("a₂·√(p·Nₑ)·t  (both ½)",
    lambda _,a2: a2*np.sqrt(P*NE)*T,
    lambda pr: pr[0]*2*math.sqrt(57)*math.log(2), [[0.5]])
print()
print("      the measured np defects of heavy elements run 3.5–3.7;")
print("      any form giving δ(6p) above ~4.0 at La will lose 4f.")