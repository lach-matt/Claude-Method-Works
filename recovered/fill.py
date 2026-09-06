import math
import numpy as np
src=open("equation.py",encoding="utf-8").read()
src=src[:src.index("# ------------------------------------------------------------ ladder 1")]
g={}; exec(src,g)
config,core_p,thresh,n0,ORDER=g["config"],g["core_p"],g["thresh"],g["n0"],g["ORDER"]
a,h,w=np.load("/tmp/eq3.npy")
L="spdfg"
def delta(Z,c,l):
    ne=Z-c+1; p=core_p(ne-1,l); t=math.log(c+1)/c
    if p>=1: return a*math.sqrt(p*ne)*t
    D=Z-thresh(ne-1,l)
    x=max(-60.0,min(60.0,D/w))
    return h*0.5*(1+math.tanh(0.5*x))*((ne-1)/ne)*math.sqrt(ne)*t
def cap(l): return 2*(2*l+1)
def occ(cfg,n,l):
    for A,B,O in cfg:
        if A==n and B==l: return O
    return 0
print("  DOES THE THREE-PARAMETER EQUATION PRODUCE THE FILLING ORDER?\n")
print("      a = %.4f   h = %.4f   w = %.4f   both exponents ½ exactly\n"%(a,h,w))
ok=bad=0; BAD=[]
for Z in range(3,104):
    ne=Z; cfg=config(ne-1); full=config(ne)
    cand=[]
    for n,l in ORDER:
        if l>4 or n>8: continue
        if occ(cfg,n,l)>=cap(l): continue
        if n!=core_p(ne-1,l)+l+1 and occ(cfg,n,l)==0: continue
        d=delta(Z,1,l); cand.append((n,l,d,n-d))
    if len(cand)<2: continue
    got=None
    for n,l in ORDER:
        if occ(full,n,l)>occ(cfg,n,l): got=(n,l); break
    if got is None: continue
    pick=min(cand,key=lambda x:x[3])
    if (pick[0],pick[1])==got: ok+=1
    else: bad+=1; BAD.append((Z,got,pick,cand))
print(f"      elements                    : {ok+bad}")
print(f"      picks the aufbau subshell   : {ok}  ({100*ok/(ok+bad):.1f}%)")
print(f"      picks another               : {bad}")
print()
if BAD:
    print(f"      {'Z':>4}{'aufbau':>9}{'equation':>10}{'n* aufbau':>11}{'n* eq':>9}")
    for Z,gt,pk,cand in BAD:
        na=[c for c in cand if (c[0],c[1])==gt]
        print(f"      {Z:>4}{f'{gt[0]}{L[gt[1]]}':>9}{f'{pk[0]}{L[pk[1]]}':>10}"
              f"{(na[0][3] if na else float('nan')):>11.3f}{pk[3]:>9.3f}")
print()
print("  AND THE PAIRWISE MADELUNG TEST ON n* = n − δ\n")
ag=dis=0
for Z in range(3,104):
    ne=Z; cfg=config(ne-1)
    cand=[]
    for l in range(5):
        n=core_p(ne-1,l)+l+1
        if n>8: continue
        cand.append((n,l,n-delta(Z,1,l)))
    for i in range(len(cand)):
        for j in range(i+1,len(cand)):
            A,B=cand[i],cand[j]
            ka,kb=(A[0]+A[1],A[0]),(B[0]+B[1],B[0])
            if ka==kb: continue
            lo,hi=(A,B) if ka<kb else (B,A)
            if lo[2]<hi[2]: ag+=1
            else: dis+=1
print(f"      pairs {ag+dis} · Madelung order holds {ag} ({100*ag/(ag+dis):.1f}%)")