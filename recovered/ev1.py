import numpy as np, eldata as ed, itertools, random
from itertools import combinations
from collections import Counter
from scipy import stats
CAP=lambda l: 2*(2*l+1)
L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,CAP(l)+1)]
occ=set(ed.E.values()); zs=sorted(ed.E)
def leq(a,b): return all(x<=y for x,y in zip(a,b))
def V(claim,got,exp,tol=None):
    ok=(abs(got-exp)<=tol) if tol is not None else (got==exp)
    g=f"{got:.4f}" if isinstance(got,float) else str(got)
    print(f"  {claim:<56}{g:>13}  exp {str(exp):>10}  {'OK' if ok else '*** FAIL ***'}")

print("="*84); print("EVIDENCE AUDIT A — CLAIMS IN PART I"); print("="*84)
# |DeltaQ| takes two values
def dq(z):
    n,l,k=ed.E[z]; Q0=np.array([n,l,k],float); Q1=np.array([n+1,l,k],float)
    Q2=np.array([n,l+1,k],float) if l+1<=n-1 else (np.array([n,l-1,k],float) if l>0 else np.array([n+1,l,k],float))
    return np.linalg.norm(Q0-0.5*(Q1+Q2))
vals=sorted(set(round(dq(z),6) for z in zs))
V("distinct |ΔQ| values across 118 elements",len(vals),2)
print(f"      the two values: {vals}   (1 and 1/√2 = {1/np.sqrt(2):.6f})")
# sigma^2_max for H/He
def s2max(z):
    n,l,k=ed.E[z]
    d1=np.array([1,0,0],float)
    d2=(np.array([0,1,0],float) if l+1<=n-1 else (np.array([0,-1,0],float) if l>0 else np.array([1,0,0],float)))
    return (d1@d1+d2@d2)/4 - (d1@d2)/2
V("σ²_max for hydrogen",s2max(1),0.0,1e-9)
V("σ²_max for helium",s2max(2),0.0,1e-9)
V("σ²_max for palladium",s2max(46),0.5,1e-9)
# class membership
def dcls(z):
    n,l,k=ed.E[z]
    return 'B' if l+1<=n-1 else ('C' if l>0 else 'A')
c=Counter(dcls(z) for z in zs)
V("Class A membership",c['A'],2)
print(f"      Class B {c['B']}, Class C {c['C']}, total {sum(c.values())}")
# reserved cell distribution
res=[cc for cc in L if cc not in occ]
byn=Counter(cc[0] for cc in res)
V("reserved cells at n=7",byn[7],42)
V("reserved cells at n=6",byn[6],32)
V("reserved cells at n=5",byn[5],18)
V("reserved total",len(res),92)

print()
print("="*84); print("EVIDENCE AUDIT B — DISTRIBUTIVITY AND JOIN-IRREDUCIBLES"); print("="*84)
S=set(L)
jn=lambda a,b: tuple(max(x,y) for x,y in zip(a,b))
mt=lambda a,b: tuple(min(x,y) for x,y in zip(a,b))
random.seed(11); samp=random.sample(L,45)
bad=sum(1 for a in samp for b in samp for cc in samp if mt(a,jn(b,cc))!=jn(mt(a,b),mt(a,cc)))
V("distributive-law violations (45³ sample)",bad,0)
# join-irreducible = covers exactly one element
def covers(x):
    out=[]
    for d in range(3):
        y=list(x); y[d]-=1; y=tuple(y)
        if y in S: out.append(y)
    return out
ji=[x for x in L if len(covers(x))==1]
V("join-irreducible cells",len(ji),27)
print(f"      examples: {sorted(ji)[:6]}")

print()
print("="*84); print("EVIDENCE AUDIT C — CLAIMS IN PART II"); print("="*84)
# sublattice chain 630 -> 450 -> 210
box=[(n,l,k) for n in range(1,8) for l in range(0,5) for k in range(1,19)]
c1=[cc for cc in box if cc[1]<=cc[0]-1]
c2=[cc for cc in c1 if cc[2]<=CAP(cc[1])]
V("box cells",len(box),630); V("after ℓ ≤ n−1",len(c1),450); V("after k ≤ cap",len(c2),210)
for nm,X in [('box',box),('ℓ-constrained',c1),('Λ',c2)]:
    SS=set(X); b=sum(1 for a,b_ in combinations(X,2) if jn(a,b_) not in SS or mt(a,b_) not in SS)
    print(f"      {nm:<16} closure failures: {b}")
# Madelung tau on raw functional
mad=[ed.E[z][0]+ed.E[z][1] for z in zs]
tau,_=stats.kendalltau(zs,mad)
V("Kendall τ(Z, n+ℓ) raw",tau,0.9013,0.002)
# incomparable pairs
tot=len(zs)*(len(zs)-1)//2
comp=sum(1 for a,b in combinations(zs,2) if leq(ed.E[a],ed.E[b]) or leq(ed.E[b],ed.E[a]))
V("comparable element pairs",comp,3742)
V("incomparable element pairs",tot-comp,3161)
print(f"      incomparable fraction {100*(tot-comp)/tot:.1f}%  (paper says 46%)")
# range of cells below occupied cells
below=[sum(1 for y in L if leq(y,x)) for x in occ]
V("min cells below an occupied cell",min(below),1)
V("max cells below an occupied cell",max(below),92)