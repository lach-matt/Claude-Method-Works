import numpy as np, eldata as ed
from collections import Counter
from itertools import combinations

L=[(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)]
occ=set(ed.E[z] for z in ed.E)
zs=sorted(ed.E)

print("="*78)
print("SHEAR FAMILY:  f(n,ℓ,k) = a·n + b·ℓ + c·k   — which slicings are meaningful?")
print("="*78)
print("""  §11 showed that a=1,b=1,c=0 (the Madelung functional) slices Λ into
  levels whose volumes pair to give the period lengths. Test the whole
  small-integer family and ask which produce (i) level volumes matching a
  known chemical sequence, or (ii) levels that respect the occupied set.""")

def levels(a,b,c, cells):
    return Counter(a*n+b*l+c*k for (n,l,k) in cells)

# reference sequences
PERIODS=[2,2,8,8,18,18,32,32]
def seq_of(a,b,c):
    Lbig=[(n,l,k) for n in range(1,40) for l in range(0,n) for k in range(1,2*(2*l+1)+1)]
    cnt=levels(a,b,c,Lbig)
    ks=sorted(cnt)
    return [cnt[k] for k in ks[:10]]

print(f"\n  {'(a,b,c)':<12}{'first level volumes':<44}{'note'}")
print("  "+"-"*76)
best=[]
for a in range(0,3):
    for b in range(0,3):
        for c in range(0,3):
            if a==b==c==0: continue
            s=seq_of(a,b,c)
            note=''
            if s[:8]==PERIODS: note='← PERIOD LENGTHS'
            elif len(set(s[:6]))==1: note='uniform'
            elif all(s[i]<=s[i+1] for i in range(5)): note='monotone'
            if note: best.append(((a,b,c),s,note))
            print(f"  {str((a,b,c)):<12}{str(s):<44}{note}")

print()
print("="*78)
print("AXIS PERMUTATIONS: does relabelling ℓ or k reveal anything?")
print("="*78)
# permute l-values and see whether the occupied set stays a down-set
import itertools
def is_downset(cells_occ, cells_all):
    S=set(cells_occ)
    def leq(x,y): return all(p<=q for p,q in zip(x,y))
    return not any(leq(y,x) and y not in S for x in S for y in cells_all)

print("  permuting the ℓ labels (s,p,d,f,g order) and re-testing down-set:")
base=list(range(5))
hits=0; tested=0
for perm in itertools.permutations(base):
    if perm==tuple(base): tag=' (identity)'
    else: tag=''
    m={old:new for old,new in zip(base,perm)}
    # remap, keeping capacity tied to the ORIGINAL l (capacity is physical)
    Lp=[(n,m[l],k) for (n,l,k) in L]
    Op=[(n,m[l],k) for (n,l,k) in occ]
    tested+=1
    if is_downset(Op,Lp):
        hits+=1
        if tag or hits<=4: print(f"    {perm}{tag}: still a down-set")
print(f"  {hits}/{tested} permutations preserve the down-set property")