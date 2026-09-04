import sys, math; sys.path.insert(0,"/home/claude/work")
import numpy as np
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
print("  THE IDENTITY — each atom's own interval in a\n")
print("      for atom Z, a must satisfy  n*(got) < n*(rival)  for every rival.")
print("      n* = n − a√(n−ℓ−1), so each rival gives a linear inequality in a.\n")
IV=[]
for Z in range(3,109):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: continue
    gn,gl=got[0]
    cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: continue
    gp=math.sqrt(gn-gl-1)
    lo,hi=-1e9,1e9
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        rp=math.sqrt(n-l-1)
        # gn - a*gp < n - a*rp   →  a*(rp-gp) < n-gn
        d=rp-gp; r=n-gn
        if abs(d)<1e-12:
            if r<=0: lo,hi=1e9,-1e9   # impossible
            continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    IV.append((Z,gn,gl,lo,hi))
print(f"      {'Z':>4}{'el':>4}{'fills':>7}{'a >':>9}{'a <':>9}{'  feasible'}")
for Z,gn,gl,lo,hi in IV:
    if Z%7 and Z not in (19,20,21,37,38,39,55,56,57,87,88,89): continue
    f="yes" if lo<hi else "NO"
    print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{f'{gn}{L[gl]}':>7}"
          f"{(lo if lo>-1e8 else float('-inf')):>9.3f}"
          f"{(hi if hi<1e8 else float('inf')):>9.3f}   {f}")
print()
good=[x for x in IV if x[3]<x[4]]
bad=[x for x in IV if x[3]>=x[4]]
print(f"      {len(IV)} elements · feasible {len(good)} · infeasible {len(bad)}")
if bad: print(f"      infeasible at Z = {[x[0] for x in bad]}")
print()
LO=max(x[3] for x in good); HI=min(x[4] for x in good)
print(f"  THE INTERSECTION OVER ALL FEASIBLE ATOMS\n")
print(f"      a > {LO:.4f}  (binding: Z = "
      f"{[x[0] for x in good if abs(x[3]-LO)<1e-9]})")
print(f"      a < {HI:.4f}  (binding: Z = "
      f"{[x[0] for x in good if abs(x[4]-HI)<1e-9]})")
print(f"      → {'NON-EMPTY: a ∈ (%.4f, %.4f)'%(LO,HI) if LO<HI else 'EMPTY — no single a serves every atom'}\n")
print("  HOW MANY ATOMS CAN ONE a SERVE?\n")
best=None
for av in np.arange(0.0,2.001,0.005):
    n=sum(1 for Z,gn,gl,lo,hi in good if lo<av<hi)
    if best is None or n>best[0]: best=(n,float(av))
n,av=best
print(f"      maximum {n} of {len(good)} at a = {av:.3f}")
rng=[x for x in np.arange(0,2.001,0.005) if sum(1 for Z,g1,g2,lo,hi in good if lo<x<hi)==n]
print(f"      achieved for a from {min(rng):.3f} to {max(rng):.3f}")
