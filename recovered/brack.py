import sys, math; sys.path.insert(0,"/home/claude/work")
import numpy as np, statistics as st
from fractions import Fraction
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
IV=[]
for Z in range(3,109):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: continue
    gn,gl=got[0]; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: continue
    gp=gn-gl-1; lo,hi=-1e9,1e9; blo=bhi=None
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        rp=n-l-1; d=math.sqrt(rp)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0:
            if r/d<hi: hi,bhi=r/d,(n,l,rp,r)
        else:
            if r/d>lo: lo,blo=r/d,(n,l,rp,r)
    IV.append((Z,gn,gl,gp,lo,hi,blo,bhi))
print("  THE BRACKETS, EXACT — (Δn)/(√p_r − √p_g)\n")
print(f"      {'Z':>4}{'el':>4}{'fills':>7}{'p_g':>5}{'lower bound':>26}{'upper bound':>26}")
def show(b,gp):
    if b is None: return "—"
    n,l,rp,r = b
    return f"{r}/(√{rp}−√{gp}) = {r/(math.sqrt(rp)-math.sqrt(gp)):+.4f}"
for Z,gn,gl,gp,lo,hi,blo,bhi in IV:
    if Z not in (19,20,21,24,29,37,38,39,46,55,56,57,58,64,71,79,87,88,89,91,103): continue
    print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{f'{gn}{L[gl]}':>7}{gp:>5}"
          f"{show(blo,gp):>26}{show(bhi,gp):>26}")
print()
print("  THE BOUNDS ARE A SMALL SET OF SURDS\n")
vals=set()
for Z,gn,gl,gp,lo,hi,blo,bhi in IV:
    if lo>-1e8: vals.add(round(lo,6))
    if hi<1e8:  vals.add(round(hi,6))
V=sorted(vals)
print(f"      {len(V)} distinct bound values across {len(IV)} atoms\n")
NAMES={0.7071068:"1/√2",1.0:"1",1.3660254:"1/(√3−√1)·? = 1/(√3−1)",
       1.7071068:"1+1/√2",1.9841:"?",0.5773503:"1/√3",2.2247449:"?",
       4.2360680:"2+√5?",4.6862915:"?",5.0954452:"?",1.2168502:"?",
       1.3938468:"?",1.9841:"?"}
for v in V[:20]:
    exact=""
    for nm,x in (("1/√2",1/math.sqrt(2)),("1",1.0),("1/(√3−1)",1/(math.sqrt(3)-1)),
                 ("1+1/√2",1+1/math.sqrt(2)),("1/√3",1/math.sqrt(3)),
                 ("2/(√3−1)",2/(math.sqrt(3)-1)),("√2",math.sqrt(2)),
                 ("2/(√5−√2)",2/(math.sqrt(5)-math.sqrt(2))),
                 ("1/(√2−1)",1/(math.sqrt(2)-1))):
        if abs(v-x)<1e-4: exact=nm; break
    print(f"      {v:>12.6f}   {exact}")
print()
print("  AND THE TIGHTEST BRACKETS\n")
w=sorted(((hi-lo,Z,lo,hi) for Z,gn,gl,gp,lo,hi,blo,bhi in IV if lo>-1e8 and hi<1e8))
print(f"      {'Z':>4}{'el':>4}{'width':>9}{'a ∈':>22}")
for wd,Z,lo,hi in w[:10]:
    print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{wd:>9.4f}{f'({lo:.3f}, {hi:.3f})':>22}")