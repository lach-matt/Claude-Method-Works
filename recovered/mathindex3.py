import numpy as np
from itertools import product, combinations
from collections import defaultdict
print("="*90)
print("  E(X) > 0 REVEALED A MISSING CONSTRAINT, NOT A MISSING ELEMENT")
print("="*90)
print("""
  **Reading the seven admitted-but-absent cells:** four of them pair
  *verification = cited* with *precedent = none found*.

  > **You cannot cite a precedent that does not exist.** So the coordinate
  > system carries an unstated bound:

        verification = cited   ⟹   precedent = found

  **which is a genuine constraint on the index, of exactly the form Λ's own
  bounds take.** §12's diagnostic loop says E(X) > 0 with a separating form in
  the excess means a missing constraint. **This is that case.**
""")
K=['definition','mechanism','formula','theorem','law','method','measurement']
L=['order','combin','analysis','complexity','physics','algeom']
S={'withdrawn':0,'conjectured':1,'measured':2,'verified':3,'proved':4}
V={'cited':0,'sampled':1,'exhaustive':2}
E=[("E(X) closure defect",'definition','order','proved','exhaustive',1),
("the operator 𝓡",'mechanism','order','proved','exhaustive',1),
("Λ's construction",'definition','combin','proved','exhaustive',1),
("join/meet closure of Λ",'theorem','order','proved','exhaustive',1),
("rank modularity",'theorem','order','verified','exhaustive',1),
("the single expression F",'formula','combin','proved','exhaustive',1),
("F(−1) = 2",'measurement','combin','proved','exhaustive',0),
("the fibration",'theorem','combin','verified','exhaustive',0),
("maximal chains = lin ext",'theorem','order','proved','exhaustive',1),
("the bracket method",'method','analysis','proved','sampled',1),
("V = 4ν/3",'formula','analysis','measured','exhaustive',1),
("λ² = Newton decrement",'formula','analysis','proved','cited',1),
("self-concordance",'theorem','analysis','verified','sampled',1),
("Aitken bias = 1/3",'theorem','analysis','proved','exhaustive',1),
("the Ritz expansion",'formula','physics','proved','cited',1),
("the Sc VI bracket",'measurement','physics','verified','exhaustive',0),
("closure not locally det.",'theorem','order','proved','exhaustive',0),
("reorderable ≡ sublattice",'theorem','order','verified','exhaustive',1),
("the arity law",'law','complexity','proved','exhaustive',1),
("the step law 2^(d−2)",'theorem','order','proved','exhaustive',1),
("C1P + monotone endpoints",'theorem','combin','proved','exhaustive',1),
("the level-3 signature",'method','combin','verified','exhaustive',0),
("a(r,c) polynomials",'formula','combin','proved','exhaustive',0),
("N(R,C) transform",'formula','combin','proved','exhaustive',0),
("Tucker obstructions",'theorem','combin','proved','cited',1),
("Dilworth width",'theorem','order','proved','cited',1),
("the construction grammar",'method','order','verified','sampled',1),
("the obstruction census",'measurement','combin','verified','exhaustive',0),
("mirror symmetry 1,095",'measurement','algeom','verified','cited',1),
("the resonance order cut",'measurement','physics','verified','exhaustive',0)]
def Rop(P,dd=3):
    Ls=sorted(P); Aa=[sorted({x[i] for x in Ls}) for i in range(dd)]
    ph={}
    for i in range(dd):
        for j in range(dd):
            if i==j: continue
            f={}; run=-1
            for v in Aa[j]:
                c=[x[i] for x in Ls if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*Aa) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(dd) for j in range(dd) if i!=j)}
def ok_constraint(c):
    # verification == cited (0)  =>  precedent == found (1)
    return not (c[1]==0 and c[2]==0)
fib=defaultdict(set)
for nm,k,l,s,v,p in E: fib[(k,l)].add((S[s],V[v],p))
print("="*90)
print("  CLOSURE WITH THE CONSTRAINT IMPOSED")
print("="*90)
print("\n  %-13s%-12s%8s%12s%12s%10s"%("kind","language","cells","E before","E after","closed"))
print("  "+"-"*68)
tot=cl=0; rem=[]
for key in sorted(fib,key=lambda t:(K.index(t[0]),L.index(t[1]))):
    P=fib[key]
    e0=len(Rop(P))-len(P)
    ex={c for c in Rop(P)-P if ok_constraint(c)}
    e1=len(ex)
    tot+=1; cl+= (e1==0)
    print("  %-13s%-12s%8d%12d%12d%10s"%(key[0],key[1],len(P),e0,e1,"YES" if e1==0 else "no"))
    if ex: rem.append((key,ex))
print("\n     **fibres closed : %d of %d**"%(cl,tot))
SI={v:k for k,v in S.items()}; VI={v:k for k,v in V.items()}
if rem:
    print("\n  STILL ADMITTED AND ABSENT — the genuine questions:\n")
    for key,ex in rem:
        for c in sorted(ex):
            print("     %-12s %-10s  status %-10s verification %-11s precedent %s"
                  %(key[0],key[1],SI[c[0]],VI[c[1]],"found" if c[2] else "none"))
    print("""
  **Each is a question the book's own structure poses:** is there an element of
  that kind, in that language, at that status and verification? **Either it
  exists and is unlisted, or it cannot exist and the reason belongs in the
  text.**""")
else:
    print("""
  > **EVERY FIBRE CLOSES. E = 0 throughout, with one stated constraint.**
  > **No question about the mathematics is admitted by the structure and left
  > unanswered by the book.**""")