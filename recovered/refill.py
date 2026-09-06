import math, statistics as st
import numpy as np
import ground as G
L="spdfg"
print("  THE FILLING TEST AGAINST THE OBSERVED SEQUENCE\n")
print("      previous tests compared against the MADELUNG order, which the")
print("      configurations show is wrong at two of nineteen openings.\n")
# the observed opening order, with the Z at which each opens
prev=None; OPEN=[]
for Z in range(1,109):
    cur={(n,l):o for n,l,o in G.expand(Z)}
    if prev is not None:
        for k in cur:
            if k not in prev and k not in [x[0] for x in OPEN]: OPEN.append((k,Z))
    else:
        for k in cur: OPEN.append((k,Z))
    prev=cur
print(f"      {'subshell':>9}{'opens at Z':>12}{'element':>9}")
for (n,l),Z in OPEN: print(f"      {f'{n}{L[l]}':>9}{Z:>12}{G.GROUND[Z][0]:>9}")
print()
print("  NOW: WHICH SUBSHELL RECEIVES THE ELECTRON AT EACH Z, OBSERVED\n")
a,b0,b1,b2=0.0,-2.2402,1.3250,-0.1602
def am(ne):
    if ne<2: return 0.0
    u=math.log(ne); return math.exp(b0+b1*u+b2*u*u)
ok=bad=0; BAD=[]
for Z in range(3,109):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: continue        # rearrangements, not simple additions
    got=got[0]
    # candidates: any (n,l) that could take an electron
    cand=[]
    for l in range(5):
        p=sum(1 for (n,ll) in pr if ll==l and pr[(n,ll)]>0)
        n0=p+l+1
        if n0>8: continue
        cap=2*(2*l+1)
        if pr.get((n0,l),0)>=cap: continue
        d=am(Z-1)*math.sqrt(p) if p>0 else 0.0
        cand.append((n0,l,n0-d))
    if len(cand)<2: continue
    pick=min(cand,key=lambda x:x[2])
    if (pick[0],pick[1])==got: ok+=1
    else: bad+=1; BAD.append((Z,got,(pick[0],pick[1])))
print(f"      elements with a single clean addition : {ok+bad}")
print(f"      equation picks correctly              : {ok}  ({100*ok/max(ok+bad,1):.1f}%)")
print(f"      picks another                         : {bad}\n")
from collections import Counter
c=Counter(f"{g[0]}{L[g[1]]}→{p[0]}{L[p[1]]}" for _,g,p in BAD)
print("      failures by pair:")
for k,v in c.most_common(8): print(f"          {k:<12}{v:>4}")
print()
print("  AND HOW MANY OF THOSE ARE THE KNOWN AUFBAU EXCEPTIONS\n")
EXC={24,29,41,42,44,45,46,47,57,58,64,78,79,89,90,91,92,93,96,103}
inexc=sum(1 for Z,_,_ in BAD if Z in EXC)
print(f"      failures at a known exception : {inexc} of {len(BAD)}")
print(f"      failures elsewhere            : {len(BAD)-inexc}")
print(f"      Z of failures elsewhere : "
      f"{sorted(Z for Z,_,_ in BAD if Z not in EXC)[:20]}")