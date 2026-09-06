import math, statistics as st
import numpy as np
from collections import defaultdict, Counter
from scipy import stats as SS
src=open("regimes.py",encoding="utf-8").read()
src=src[:src.index("from collections import Counter")]
g={}; exec(src,g)
ROWS=g["ROWS"]; L="spdfg"
# add today's captures
ROWS=list(ROWS)+[dict(Z=81,c=2,l=1,d=3.7167,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
                 dict(Z=82,c=3,l=1,d=3.5402,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0),
                 dict(Z=83,c=4,l=1,d=3.3684,ne=80,p=4,n0=6,non=6,T=9999,reg=2,b24=0.0)]
print("  TEST 1 · HOLD p FIXED, VARY Nₑ.  What exponent does δ show?\n")
print("      Thomas–Fermi predicts ⅓. Our global fit gives 0.44–0.53.")
print("      With p fixed, √p is constant and cannot absorb anything.\n")
print(f"      {'ℓ':>3}{'p':>3}{'chg':>5}{'n':>4}{'Nₑ range':>12}{'exponent':>10}{'r²':>8}")
res=[]
grp=defaultdict(list)
for r in ROWS:
    if r["d"]<0.05: continue
    grp[(r["l"],r["p"],r["c"])].append(r)
for k,v in sorted(grp.items()):
    ne=[x["ne"] for x in v]
    if len(v)<4 or max(ne)/max(min(ne),1)<1.8: continue
    x=np.log(np.array(ne,float)); y=np.log(np.array([q["d"] for q in v]))
    rr=SS.linregress(x,y)
    if rr.rvalue**2<0.5: continue
    print(f"      {L[k[0]]:>3}{k[1]:>3}{k[2]:>5}{len(v):>4}"
          f"{f'{min(ne)}–{max(ne)}':>12}{rr.slope:>10.3f}{rr.rvalue**2:>8.3f}")
    res.append(rr.slope)
if res:
    print(f"\n      {len(res)} groups · median exponent {st.median(res):.3f}"
          f"   sd {st.pstdev(res):.3f}")
    print(f"      within ±0.08 of ⅓ : {sum(1 for z in res if abs(z-1/3)<0.08)}/{len(res)}")
    print(f"      within ±0.08 of ½ : {sum(1 for z in res if abs(z-0.5)<0.08)}/{len(res)}")
print()
print("  TEST 2 · DOES √p·Nₑ^k COLLAPSE TO Nₑ^(1/3) OVERALL?\n")
print("      If TF is right and √p carries the rest, then δ/(c-term) should be")
print("      proportional to Nₑ^(1/3) with NO p factor at all.\n")
D=np.array([r["d"] for r in ROWS]); P=np.array([r["p"] for r in ROWS],float)
NE=np.array([r["ne"] for r in ROWS],float); C=np.array([r["c"] for r in ROWS],float)
keep=(D>0.05)&(P>0)
D,P,NE,C=D[keep],P[keep],NE[keep],C[keep]
xc=0.86-0.18*np.log(NE); T=C**(-np.maximum(xc,0.02))
Y=np.log(D/T)
print(f"      {'model':<34}{'r²':>9}{'rms in ln δ':>14}")
for nm,X in (("Nₑ^(1/3) alone", np.column_stack([np.log(NE)])),
             ("Nₑ^k alone (k free)", np.column_stack([np.log(NE)])),
             ("√p · Nₑ^(1/3)", np.column_stack([0.5*np.log(P), np.log(NE)])),
             ("p^e · Nₑ^k (both free)", np.column_stack([np.log(P), np.log(NE)]))):
    Xm=np.column_stack([X, np.ones(len(Y))])
    b,*_=np.linalg.lstsq(Xm,Y,rcond=None); r=Y-Xm@b
    ex=" ".join(f"{z:+.3f}" for z in b[:-1])
    print(f"      {nm:<34}{1-np.var(r)/np.var(Y):>9.4f}{float(np.sqrt(np.mean(r**2))):>14.4f}   [{ex}]")
print()
print("  TEST 3 · THE TF PREDICTION HAS ℓ ENTERING AS (ℓ+½)²·Nₑ^(−2/3)\n")
print("      so δ should depend on ℓ only through that combination.\n")
LL=np.array([r["l"] for r in ROWS],float)[keep]
u=(LL+0.5)**2/NE**(2/3)
for nm,X in (("ln p, ln Nₑ", np.column_stack([np.log(P),np.log(NE)])),
             ("ln p, ln Nₑ, ℓ", np.column_stack([np.log(P),np.log(NE),LL])),
             ("ln p, ln Nₑ, (ℓ+½)²Nₑ^-2/3", np.column_stack([np.log(P),np.log(NE),u]))):
    Xm=np.column_stack([X,np.ones(len(Y))])
    b,*_=np.linalg.lstsq(Xm,Y,rcond=None); r=Y-Xm@b
    print(f"      {nm:<34}{1-np.var(r)/np.var(Y):>9.4f}{float(np.sqrt(np.mean(r**2))):>14.4f}")