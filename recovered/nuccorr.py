import math
from fractions import Fraction as F
LN="s p d f g h i k"
# the observed nuclear filling order to the 126 closure (standard)
ORDER=[(1,0,F(1,2)),(1,1,F(3,2)),(1,1,F(1,2)),(1,2,F(5,2)),(2,0,F(1,2)),
       (1,2,F(3,2)),(1,3,F(7,2)),(2,1,F(3,2)),(1,3,F(5,2)),(2,1,F(1,2)),
       (1,4,F(9,2)),(2,2,F(5,2)),(3,0,F(1,2)),(2,2,F(3,2)),(1,4,F(7,2)),
       (1,5,F(11,2)),(2,3,F(7,2)),(3,1,F(3,2)),(1,5,F(9,2)),(3,1,F(1,2)),
       (2,3,F(5,2)),(1,6,F(13,2))]
def Nosc(nr,l): return 2*(nr-1)+l          # nr is the radial index, 1-based
def cands():
    C={}
    C["s·ℓ  (Laubscher, Mayer)"]  = lambda n,l,j: (l if j>l else -l)
    C["exact ⟨L·S⟩"]              = lambda n,l,j: (F(l,2) if j>l else -F(l+1,2))
    C["s·√p, p = nr−1"]           = lambda n,l,j: (math.sqrt(n-1) if j>l else -math.sqrt(n-1))
    C["s·ℓ(ℓ+1)"]                 = lambda n,l,j: (l*(l+1) if j>l else -l*(l+1))
    C["s·(2j+1)"]                 = lambda n,l,j: (int(2*j+1) if j>l else -int(2*j+1))
    C["s·ℓ·(2j+1)/(2ℓ+1)"]        = lambda n,l,j: (F(l*int(2*j+1),2*l+1) if j>l
                                                   else -F(l*int(2*j+1),2*l+1))
    return C
print("  THE CORRIDOR TEST ON NUCLEAR CORRECTION FORMS\n")
print("      E(nr,ℓ,j) = (N + 3/2) − s·f(nr,ℓ,j),  N = 2(nr−1) + ℓ")
print("      the observed order must be the order of increasing E.")
print("      each consecutive pair gives one inequality in s; the corridor is")
print("      their intersection. an EMPTY corridor eliminates the form.\n")
print(f"      {'form':<26}{'s >':>10}{'s <':>10}{'  verdict'}")
for nm,f in cands().items():
    lo,hi=-1e9,1e9; bad=False
    for i in range(len(ORDER)-1):
        n1,l1,j1=ORDER[i]; n2,l2,j2=ORDER[i+1]
        N1=Nosc(n1,l1); N2=Nosc(n2,l2)
        # E1 < E2 :  N1 - s f1  <  N2 - s f2   →  s(f2 - f1) < N2 - N1
        d=float(f(n2,l2,j2))-float(f(n1,l1,j1)); r=N2-N1
        if abs(d)<1e-12:
            if r<0: bad=True; break
            continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    ok = (not bad) and lo<hi
    print(f"      {nm:<26}{(lo if lo>-1e8 else float('-inf')):>10.4f}"
          f"{(hi if hi<1e8 else float('inf')):>10.4f}"
          f"   {'FEASIBLE' if ok else 'EMPTY — eliminated'}")
print()
print("  AND WHERE 1/12 SITS IN EACH SURVIVING CORRIDOR\n")
for nm,f in cands().items():
    lo,hi=-1e9,1e9; bad=False
    for i in range(len(ORDER)-1):
        n1,l1,j1=ORDER[i]; n2,l2,j2=ORDER[i+1]
        d=float(f(n2,l2,j2))-float(f(n1,l1,j1)); r=Nosc(n2,l2)-Nosc(n1,l1)
        if abs(d)<1e-12:
            if r<0: bad=True; break
            continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    if bad or lo>=hi: continue
    t=(1/12-lo)/(hi-lo) if hi<1e8 and lo>-1e8 else float('nan')
    print(f"      {nm:<26}corridor ({lo if lo>-1e8 else float('-inf'):.4f},"
          f" {hi if hi<1e8 else float('inf'):.4f})   1/12 inside: "
          f"{'YES' if lo<1/12<hi else 'no'}")