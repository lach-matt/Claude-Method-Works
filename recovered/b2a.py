import sys, random; sys.path.insert(0,"/tmp")
import li
from itertools import product, permutations
SEAT,KIND,ZC,FAM=li.SEAT,li.KIND,li.ZCROSS,li.FAMILY
# the TOWER STAGE each ladder's rung variable belongs to — down and inward.
# Λ8 (n,ℓ,k,q,e,f,g,2S) · Λ9 seniority · Λ10 v · Λ11 2J_c · Λ12 2K · Λ13 2J
STAGE={"isoelectronic":8,"the walk":8,"ionisation":8,"isotopic":0,"isotonic":0,
       "isobaric":0,"the Rydberg series":8,"the l-ladder":8,"the term ladder":8,
       "the outer-j ladder":13,"the parent-term ladder":11,"the isomeric":0}
print("  B2a — THE TOWER STAGE AS THE FOURTH AXIS\n")
print(f"  {'ladder':<24}{'moves':<10}{'stage'}")
for nm,f,s,k,z,note in li.LAD:
    mv={"isoelectronic":"cfg","the walk":"cfg","ionisation":"cfg",
        "isotopic":"N","isotonic":"Z","isobaric":"Z,N","the Rydberg series":"n",
        "the l-ladder":"ℓ","the term ladder":"2S","the outer-j ladder":"2J",
        "the parent-term ladder":"2J_c","the isomeric":"nuclear"}[nm]
    st=STAGE[nm]
    print(f"  {nm:<24}{mv:<10}{'Λ'+str(st) if st else 'outside Λ'}")
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
def minE(cells,ax,cap=20000):
    b=None;k=0
    for p in product(*[permutations(range(a)) for a in ax]):
        m={tuple(p[i].index(x[i]) for i in range(len(ax))) for x in cells}
        E=len(opR(m,len(ax)))-len(m)
        b=E if b is None else min(b,E)
        if b==0: return 0
        k+=1
        if k>cap: break
    return b
L=[(s,k,z,STAGE[nm]) for nm,f,s,k,z,note in li.LAD]
L+= [(2,0,1,8),(2,1,0,13)]     # the two X-ray ladders, at subvalence
print("\n  does the stage axis SEPARATE the pairs and keep closure?\n")
for lab,cells in (("(seat, kind, Zcross)          ", {(a,b,c) for a,b,c,d in L}),
                  ("(seat, kind, Zcross, STAGE)   ", set(L)),
                  ("(seat, kind, STAGE)           ", {(a,b,d) for a,b,c,d in L}),
                  ("(kind, Zcross, STAGE)         ", {(b,c,d) for a,b,c,d in L})):
    rel=[{v:i for i,v in enumerate(sorted({c[k] for c in cells}))} for k in range(len(next(iter(cells))))]
    cs={tuple(rel[i][c[i]] for i in range(len(c))) for c in cells}
    ax=[len({c[i] for c in cs}) for i in range(len(next(iter(cs))))]
    print(f"  {lab} cells {len(cs):>2}  box {eval('*'.join(map(str,ax))):>3}  E = {minE(cs,ax)}")
print("\n  the five shared cells, under the stage axis:")
from collections import defaultdict
occ=defaultdict(list)
for nm,f,s,k,z,note in li.LAD: occ[(s,k,z,STAGE[nm])].append(nm)
for key,v in sorted(occ.items()):
    if len(v)>1:
        print(f"      STILL SHARED: {' and '.join(v)}")