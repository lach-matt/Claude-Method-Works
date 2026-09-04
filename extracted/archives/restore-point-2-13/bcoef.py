import math, statistics as st
import numpy as np
from collections import defaultdict
from scipy import stats as SS
src=open("channels_principle.py",encoding="utf-8").read()
src=src[:src.index('print("  THE PRINCIPAL STRUCTURE')]
g={}; exec(src,g)
CH=g["CH"]; config=g["config"]; L="spdfghi"
def core_p(ne,l): return sum(1 for n,ll,o in config(ne) if ll==l and o>0)
def outer(ne):
    cfg=config(ne); return cfg[-1] if cfg else (0,0,0)
# fit B per (Ne, l) with A = 0
seq=defaultdict(dict)
for x in CH: seq[(x["ne"],x["l"])][x["c"]]=x["d"]
B={}
for k,d in seq.items():
    if len(d)<3: continue
    xs=np.array([math.log(c+1)/c for c in sorted(d)])
    ys=np.array([d[c] for c in sorted(d)])
    b=float(np.sum(xs*ys)/np.sum(xs*xs))           # A = 0 forced
    r=1-np.sum((ys-b*xs)**2)/max(np.sum((ys-ys.mean())**2),1e-12)
    B[k]=(b,r,len(d))
print(f"  B FITTED PER (Nₑ, ℓ) WITH A ≡ 0 — {len(B)} sequences\n")
print(f"      {'Nₑ':>4}{'ℓ':>3}{'n':>4}{'B':>9}{'r²':>8}{'p':>4}{'core outer':>12}{'ℓ−ℓ_core':>10}")
rows=[]
for (ne,l),(b,r,n) in sorted(B.items()):
    on,ol,oo=outer(ne-1); p=core_p(ne-1,l)
    print(f"      {ne:>4}{L[l]:>3}{n:>4}{b:>9.4f}{r:>8.4f}{p:>4}{f'{on}{L[ol]}':>12}{l-ol:>10}")
    rows.append(dict(ne=ne,l=l,B=b,r2=r,n=n,p=p,on=on,ol=ol,dl=l-ol))
print()
print("  WHAT PREDICTS B?\n")
good=[x for x in rows if x["r2"]>0.9 and x["B"]>0.02]
print(f"      {len(good)} sequences with r² > 0.9 and B > 0.02\n")
print(f"      {'model':<40}{'r²':>8}{'rms':>9}")
y=np.array([x["B"] for x in good])
def fit(name,X):
    X=np.column_stack(X+[np.ones(len(good))])
    b,*_=np.linalg.lstsq(X,y,rcond=None)
    r=y-X@b; s=float(np.sqrt(np.mean(r**2)))
    print(f"      {name:<40}{1-np.var(r)/np.var(y):>8.4f}{s:>9.4f}")
    return b
P=np.array([x["p"] for x in good],float)
NE=np.array([x["ne"] for x in good],float)
LL=np.array([x["l"] for x in good],float)
DL=np.array([x["dl"] for x in good],float)
fit("p alone",[P])
fit("Nₑ^(1/3) alone",[NE**(1/3)])
fit("ℓ alone",[LL])
fit("p + ℓ",[P,LL])
fit("p + Nₑ^(1/3)",[P,NE**(1/3)])
fit("p + ℓ + Nₑ^(1/3)",[P,LL,NE**(1/3)])
fit("p·Nₑ^(1/3) + ℓ",[P*NE**(1/3),LL])
fit("p + ℓ + ln Nₑ",[P,LL,np.log(NE)])
fit("ℓ − ℓ_core",[DL])
fit("p + (ℓ − ℓ_core)",[P,DL])
print()
print("  AND THE SIMPLEST FORM THAT WORKS\n")
b=fit("B = α·p + β·ℓ + γ",[P,LL])
print(f"\n      B ≈ {b[0]:+.4f}·p {b[1]:+.4f}·ℓ {b[2]:+.4f}")
print(f"      compare: floor(δ) = p − min(p, max(2−ℓ,0)) — the same two coordinates")
