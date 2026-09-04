import math
import numpy as np
src=open("/tmp/final2.py",encoding="utf-8").read()
src=src[:src.index('print("  THE EQUATION WITH THE MEASURED SWITCH')]
g={}; exec(src,g)
cfg_c,cp,out_,n0_,thr_,ORDER=g["cfg_c"],g["cp"],g["out_"],g["n0_"],g["thr_"],g["ORDER"]
a,q,k=0.4751,-0.0403,0.4666
L="spdfg"
SW={(3,2):(0.37,-1.5,0.40)}          # measured at the 3d threshold
DEF=(0.37,-1.5,0.40)
def delta(Z,c,l,sw=None):
    ne=Z-c+1; p=cp(ne-1,l,c); t=math.log(c+1)/c
    n_,l_,o_=out_(ne-1,c); n0=n0_(ne-1,l,c)
    if p>=1: return (a+q*(n0-n_))*math.sqrt(p)*ne**k*t
    T=thr_(ne-1,l,c)
    h,m,w=(sw or SW).get((n0,l),DEF)
    x=max(-60.,min(60.,(Z-T-m)/w))
    return h*0.5*(1+math.tanh(0.5*x))*((ne-1)/ne)*ne**k*t
print("  ONE SWITCH, FOUR KEYS\n")
print("      S(Z; n, ℓ) = h(n,ℓ)·σ( (Z − T(n,ℓ) − m(n,ℓ)) / w(n,ℓ) )\n")
print(f"      {'key':>8}{'orbital':>10}{'T':>6}{'status':>28}")
for (n,l),T in ((( 3,2),21),((4,2),39),((4,3),57),((5,3),89)):
    st="MEASURED — K I, Ca I, Sc III, Ti IV" if (n,l)==(3,2) else "no channel within a proton"
    print(f"      {f'({n},{l})':>8}{f'{n}{L[l]}':>10}{T:>6}{st:>28}")
print()
print("  WHAT h MUST BE AT EACH THRESHOLD TO FIX ITS ELEMENT\n")
print("      solve for the smallest h that makes the collapsing orbital win\n")
def cap(l): return 2*(2*l+1)
def occ(cfg,n,l):
    for X,Yl,O in cfg:
        if X==n and Yl==l: return O
    return 0
print(f"      {'Z':>4}{'orbital':>9}{'rival':>8}{'h needed':>11}{'h at 3d':>10}{'ratio':>8}")
NEED={}
for Z,key in ((39,(4,2)),(57,(4,3)),(89,(5,3))):
    ne=Z; c1=cfg_c(ne-1,1); full=cfg_c(ne,1)
    got=None
    for n,l in ORDER:
        if occ(full,n,l)>occ(c1,n,l): got=(n,l); break
    lo=None
    for hh in np.arange(0.30,4.01,0.005):
        sw=dict(SW); sw[key]=(float(hh),-1.5,0.40)
        cand=[]
        for n,l in ORDER:
            if l>4 or n>8: continue
            if occ(c1,n,l)>=cap(l): continue
            if n!=cp(ne-1,l,1)+l+1 and occ(c1,n,l)==0: continue
            cand.append((n,l,n-delta(Z,1,l,sw)))
        pick=min(cand,key=lambda x:x[2])
        if (pick[0],pick[1])==got: lo=float(hh); break
    rival=None
    sw=dict(SW); sw[key]=(0.37,-1.5,0.40)
    cand=[]
    for n,l in ORDER:
        if l>4 or n>8: continue
        if occ(c1,n,l)>=cap(l): continue
        if n!=cp(ne-1,l,1)+l+1 and occ(c1,n,l)==0: continue
        cand.append((n,l,n-delta(Z,1,l,sw)))
    rival=min(cand,key=lambda x:x[2])
    if lo:
        NEED[key]=lo
        print(f"      {Z:>4}{f'{got[0]}{L[got[1]]}':>9}"
              f"{f'{rival[0]}{L[rival[1]]}':>8}{lo:>11.3f}{0.37:>10.2f}{lo/0.37:>8.2f}")
    else:
        print(f"      {Z:>4}{f'{got[0]}{L[got[1]]}':>9}{f'{rival[0]}{L[rival[1]]}':>8}"
              f"{'>4.0':>11}{0.37:>10.2f}{'—':>8}")
print()
print("  AND WHAT SCALES WITH WHAT\n")
print(f"      {'key':>8}{'ℓ(ℓ+1)':>9}{'n':>4}{'T':>6}{'h needed':>11}{'h/ℓ(ℓ+1)':>11}{'h·n/T':>9}")
TT={(3,2):21,(4,2):39,(4,3):57,(5,3):89}
for key in sorted(NEED)+[(3,2)]:
    if key==(3,2): hh=0.37
    else: hh=NEED[key]
    n,l=key; bb=l*(l+1)
    print(f"      {f'({n},{l})':>8}{bb:>9}{n:>4}{TT[key]:>6}{hh:>11.3f}"
          f"{hh/bb:>11.4f}{hh*n/TT[key]:>9.4f}")