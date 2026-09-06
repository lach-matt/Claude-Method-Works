import math, itertools
from scipy.special import spherical_jn
from scipy.optimize import brentq

R=109737.31568   # cm^-1

print("="*64); print("ROW 1 — the l-axis admissibility bound"); print("="*64)
d={0:1.35,1:0.85,2:0.015,3:0.001}   # illustrative Na, NOT provenanced
def T(n,l): return R/(n-d[l])**2

# D2/D3: exact vs approximate l-neighbour separation
print("\n D2 check: exact dT vs 2R*Ddelta/nu^3")
for n in [5,10,20,30,50,80]:
    ex = T(n,2)-T(n,3)
    ap = 2*R*(d[2]-d[3])/ (n-d[2])**3
    print(f"  n={n:3d}  exact={ex:10.5f}  approx={ap:10.5f}  ratio={ex/ap:.4f}")

print("\n D3: where each axis exits, sigma = 0.01 cm^-1, Na (Z=1)")
sig=0.01
def r_n(n,l,Z=1): return 2*Z**2*R/((n-d[l])**3*sig)
def r_l(n,l,Z=1): return 2*R*(d[l]-d[l+1])/((n-d[l])**3*sig)
print("   n     r_n(n-axis)     r_l(d-f)   n-axis ok   l-axis ok")
for n in [10,20,30,35,39,40,50,80,150,200]:
    a,b=r_n(n,2),r_l(n,2)
    print(f"  {n:4d}   {a:12.1f}  {b:11.2f}     {str(a>=5):5s}      {str(b>=5):5s}")

# exact exit points
def exit_nu(num):   # solve 2*num*R/(nu^3 sig) = 5
    return (2*num*R/(5*sig))**(1/3)
nu_n=exit_nu(1.0); nu_l=exit_nu(d[2]-d[3])
print(f"\n  n-axis exits at nu = {nu_n:.1f}")
print(f"  l-axis (d-f) exits at nu = {nu_l:.1f}")
print(f"  ratio = {nu_n/nu_l:.3f}   predicted (Z^2/Ddelta)^(1/3) = {(1.0/(d[2]-d[3]))**(1/3):.3f}")
for (la,lb) in [(0,1),(1,2),(2,3)]:
    dd=d[la]-d[lb]
    print(f"  l-axis ({la}-{lb}) Ddelta={dd:.3f}  exits at nu = {exit_nu(dd):.1f}")

# D4: does the tightening concentrate where Ddelta is smallest?
print("\n D4: width ratio vs Ddelta")
rows={}
for n in range(3,10):
    for l in range(0,min(4,n)): rows[(n,l)]=T(n,l)
for (n,l),t in sorted(rows.items()):
    up=[rows[c] for c in [(n+1,l),(n,l+1)] if c in rows]
    dn=[rows[c] for c in [(n-1,l),(n,l-1)] if c in rows]
    if len(up)<2 or len(dn)<2: continue
    wl=min(dn)-max(up); wc=rows[(n-1,l)]-rows[(n+1,l)]
    print(f"  n={n} l={l}  Ddelta(l,l+1)={d[l]-d[l+1]:.3f}  ratio={wl/wc:.4f}")

print("\n"+"="*64); print("ROW 2 — the spherical cavity lattice"); print("="*64)
LMAX, NMAX = 5, 4      # l' = 0..LMAX  (l = 1..LMAX+1), n' = 0..NMAX
cells=[(t,lp,mp,np_) for t in (0,1) for lp in range(LMAX+1)
       for mp in range(2*lp+3) for np_ in range(NMAX+1)]
S=set(cells)
pred=2*(NMAX+1)*sum(2*lp+3 for lp in range(LMAX+1))
print(f"\n S1 |Lambda_sph| = {len(S)}   formula = {pred}   match: {len(S)==pred}")

jf=mf=0
cl=list(S)
for i in range(len(cl)):
    for j in range(i+1,len(cl)):
        x,y=cl[i],cl[j]
        if tuple(max(a,b) for a,b in zip(x,y)) not in S: jf+=1
        if tuple(min(a,b) for a,b in zip(x,y)) not in S: mf+=1
print(f" S1 pairs={len(cl)*(len(cl)-1)//2}  join failures={jf}  meet failures={mf}")

def rk(x): return sum(x)
modv=dv=0
for x in cl:
    for y in cl:
        jn=tuple(max(a,b) for a,b in zip(x,y)); mt=tuple(min(a,b) for a,b in zip(x,y))
        if rk(jn)+rk(mt)!=rk(x)+rk(y): modv+=1
import random
random.seed(0)
samp=random.sample(cl,min(60,len(cl)))
for x in samp:
    for y in samp:
        for z in samp:
            a=tuple(max(p,min(q,r)) for p,q,r in zip(x,y,z))
            b=tuple(min(max(p,q),max(p,r)) for p,q,r in zip(x,y,z))
            if a!=b: dv+=1
print(f" S2 rank-modularity violations={modv}   distributivity violations={dv} over {len(samp)**3} triples")

from collections import Counter
lev=Counter(rk(x) for x in cl)
print(f" S2 height={max(lev)}  Sperner width={max(lev.values())}")

F1=len(S); Fm1=sum((-1)**sum(c) for c in cl)
print(f" S3 F(1)={F1}   F(-1)={Fm1}")
for LM in range(2,8):
    cc=[(t,lp,mp,np_) for t in (0,1) for lp in range(LM+1)
        for mp in range(2*lp+3) for np_ in range(NMAX+1)]
    print(f"    LMAX={LM}: F(1)={len(cc)}  F(-1)={sum((-1)**sum(c) for c in cc)}")
# with the type axis removed
cc=[(lp,mp,np_) for lp in range(LMAX+1) for mp in range(2*lp+3) for np_ in range(NMAX+1)]
print(f"    type axis removed: F(1)={len(cc)}  F(-1)={sum((-1)**sum(c) for c in cc)}")

# ---- physics: TE = zeros of j_l ; TM = zeros of d/dx[x j_l(x)] ----
def jz(l,k):
    xs=[];x=max(l,1)*1.0+0.1
    while len(xs)<k:
        a,b=x,x+0.05
        while spherical_jn(l,a)*spherical_jn(l,b)>0: a,b=b,b+0.05
        xs.append(brentq(lambda t: spherical_jn(l,t),a,b)); x=b+0.05
    return xs[k-1]
def dpsi(l,x): return spherical_jn(l,x)+x*spherical_jn(l,x,derivative=True)
def tmz(l,k):
    xs=[];x=max(l,1)*1.0+0.1
    while len(xs)<k:
        a,b=x,x+0.05
        while dpsi(l,a)*dpsi(l,b)>0: a,b=b,b+0.05
        xs.append(brentq(lambda t: dpsi(l,t),a,b)); x=b+0.05
    return xs[k-1]

print("\n S4 monotonicity of x_{l,n} in l and n (TE and TM), l=1..6, n=1..5")
for tag,fn in (("TE",jz),("TM",tmz)):
    X={(l,n):fn(l,n) for l in range(1,7) for n in range(1,6)}
    ml=all(X[(l,n)]<X[(l+1,n)] for l in range(1,6) for n in range(1,6))
    mn=all(X[(l,n)]<X[(l,n+1)] for l in range(1,7) for n in range(1,5))
    print(f"  {tag}: increasing in l: {ml}   increasing in n: {mn}")
    tight=tot=0; rr=[]
    for l in range(2,6):
        for n in range(2,5):
            lo_c,hi_c=X[(l,n-1)],X[(l,n+1)]
            lo=max(X[(l,n-1)],X[(l-1,n)]); hi=min(X[(l,n+1)],X[(l+1,n)])
            assert lo<=X[(l,n)]<=hi
            wc,wl=hi_c-lo_c,hi-lo; tot+=1; rr.append(wl/wc)
            if wl<wc-1e-12: tight+=1
    print(f"      lattice bracket narrower on {tight}/{tot}, mean ratio {sum(rr)/len(rr):.4f}")
