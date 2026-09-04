import math, statistics as st
from collections import defaultdict, Counter
src=open("madelung2.py",encoding="utf-8").read()
src=src[:src.index('print("  DOES THE EQUATION')]
g={}; exec(src,g)
config=g["config"]; core_p=g["core_p"]; ORDER=g["ORDER"]
L="spdfg"
FRAC={0:0.415,1:0.526,2:0.415,3:0.40,4:0.40}
def nstar(ne,l):
    p=core_p(ne,l)
    return l+1+min(p,max(2-l,0))-FRAC.get(l,0.42)
def cap(l): return 2*(2*l+1)
def occ(cfg,n,l):
    for a,b,o in cfg:
        if a==n and b==l: return o
    return 0
def n0(ne,l): return core_p(ne,l)+l+1
print("  THE RULE, WITH NO FITTED PARAMETER AT ALL\n")
print("      n* = ℓ + 1 + min(p, max(2−ℓ,0)) − frac(δ)")
print("      frac(δ) taken as its measured median per ℓ, one number each.\n")
print("      Does it pick the subshell aufbau fills, at every element?\n")
ok=bad=0; BAD=[]
for Z in range(3,104):
    ne=Z; cfg=config(ne-1); full=config(ne)
    cand=[]
    for n,l in ORDER:
        if l>4 or n>8: continue
        if occ(cfg,n,l)>=cap(l): continue
        if n!=n0(ne-1,l) and occ(cfg,n,l)==0: continue
        cand.append((n,l,nstar(ne-1,l)))
    if len(cand)<2: continue
    got=None
    for n,l in ORDER:
        if occ(full,n,l)>occ(cfg,n,l): got=(n,l); break
    if got is None: continue
    pick=min(cand,key=lambda x:x[2])
    if (pick[0],pick[1])==got: ok+=1
    else: bad+=1; BAD.append((Z,got,pick,cand))
print(f"      elements                : {ok+bad}")
print(f"      picks the aufbau subshell: {ok}  ({100*ok/(ok+bad):.1f}%)")
print(f"      picks another            : {bad}")
print()
if BAD:
    print(f"      {'Z':>4}{'aufbau':>9}{'rule':>8}{'n* aufbau':>11}{'n* rule':>10}")
    for Z,gt,pk,cand in BAD[:20]:
        na=[c for c in cand if (c[0],c[1])==gt]
        print(f"      {Z:>4}{f'{gt[0]}{L[gt[1]]}':>9}{f'{pk[0]}{L[pk[1]]}':>8}"
              f"{(na[0][2] if na else float('nan')):>11.3f}{pk[2]:>10.3f}")
print()
print("  AND WITHOUT frac(δ) AT ALL — pure integers\n")
def nstar0(ne,l): return l+1+min(core_p(ne,l),max(2-l,0))
ok2=bad2=0; tie=0
for Z in range(3,104):
    ne=Z; cfg=config(ne-1); full=config(ne)
    cand=[]
    for n,l in ORDER:
        if l>4 or n>8: continue
        if occ(cfg,n,l)>=cap(l): continue
        if n!=n0(ne-1,l) and occ(cfg,n,l)==0: continue
        cand.append((n,l,nstar0(ne-1,l),n+l,n))
    if len(cand)<2: continue
    got=None
    for n,l in ORDER:
        if occ(full,n,l)>occ(cfg,n,l): got=(n,l); break
    if got is None: continue
    m=min(c[2] for c in cand)
    best=[c for c in cand if c[2]==m]
    if len(best)>1:
        tie+=1
        best=sorted(best,key=lambda c:(c[3],c[4]))   # Madelung tiebreak
    if (best[0][0],best[0][1])==got: ok2+=1
    else: bad2+=1
print(f"      picks the aufbau subshell: {ok2} of {ok2+bad2} ({100*ok2/(ok2+bad2):.1f}%)")
print(f"      ties broken by (n+ℓ, n)  : {tie}")