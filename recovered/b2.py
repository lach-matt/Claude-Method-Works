import sys, random; sys.path.insert(0,"/tmp")
import li
from itertools import product, permutations
SEAT,KIND,ZC = li.SEAT, li.KIND, li.ZCROSS
base=[(nm,f,s,k,z) for nm,f,s,k,z,_ in li.LAD]
# the two X-ray ladders. Moseley: species, counting, across. doublet: state,
# coupling, within. seat is THE question.
def build(seat):
    L=[(s,k,z) for _,_,s,k,z in base]
    L += [(seat,0,1), (seat,1,0)]
    return set(L)
print("  B2 — Λ_ladder WITH THE X-RAY LADDERS. the seat is the question.\n")
print(f"  {'seat for the X-ray pair':<26}{'cells':>6}{'E':>4}   defects")
best={}
for seat,nm in ((0,"the nucleus"),(1,"the core"),(2,"subvalence"),(3,"the valence shell")):
    cells=build(seat)
    axes=[len(SEAT),len(KIND),len(ZC)]
    E,defects=li.minE(cells,axes,want_defects=True)
    best[nm]=(len(cells),E)
    d=", ".join(f"({SEAT[a]},{KIND[b]},{ZC[c]})" for a,b,c in defects) or "none"
    print(f"  {nm:<26}{len(cells):>6}{E:>4}   {d}")
print("\n  CONTINGENCY — could a 9-cell set on this grid have refused?")
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
def anyzero(cells,ax,cap=3000):
    k=0
    for p in product(*[permutations(range(a)) for a in ax]):
        m={tuple(p[i].index(x[i]) for i in range(3)) for x in cells}
        if len(opR(m,3))-len(m)==0: return True
        k+=1
        if k>cap: break
    return False
ax=[4,2,2]; pool=[c for c in product(*[range(a) for a in ax])]
for n in (7,9):
    pos=tot=0
    for s in range(150):
        c=set(random.Random(s).sample(pool,n)); tot+=1
        if not anyzero(c,ax): pos+=1
    print(f"      {n} cells on {ax}: {100*pos/tot:.0f}% refuse")