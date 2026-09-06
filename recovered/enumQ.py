import numpy as np
from itertools import product, combinations
from collections import defaultdict
print("="*92)
print("  ENUMERATING Q — the open questions as an index, and closing it")
print("="*92)
print("""
  **P7 says all questions must close. §25.2 asserts |Q| = 7.** An assertion is
  not an enumeration. **So index the seven, close the index, and read E(Q).**

  Coordinates, all ordered:

     BLOCKS   0 nothing · 1 a novelty assessment · 2 one stated claim
              · 3 a result the book relies on
     OBSTACLE 0 retrievable · 1 buildable · 2 requires an object that does
              not exist
     COST     0 hours · 1 days · 2 unbounded
     DEPENDS  0 the book does not depend on it · 1 partly · 2 yes

  Fibred by DOMAIN, which is categorical.
""")
B={'nothing':0,'novelty':1,'one claim':2,'a result':3}
O={'retrievable':0,'buildable':1,'new object':2}
C={'hours':0,'days':1,'unbounded':2}
D={'no':0,'partly':1,'yes':2}
Q=[
 ("A  Sc VI 6s level",            'physical',      'one claim','retrievable','unbounded','no'),
 ("B  Paschen & Götze · Runge",   'bibliographic', 'novelty',  'retrievable','days','no'),
 ("C  nine unentered literatures",'bibliographic', 'novelty',  'retrievable','days','no'),
 ("D  E(X) of Kreuzer–Skarke",    'computational', 'nothing',  'retrievable','hours','no'),
 ("E  target-spin selection rule",'physical',      'one claim','buildable',  'days','no'),
 ("F  reorderability at d ≥ 3",   'mathematical',  'nothing',  'new object', 'unbounded','no'),
 ("G  sublattice complexity lit.",'bibliographic', 'novelty',  'retrievable','hours','no'),
]
print("  %-30s%-16s%-11s%-13s%-11s%s"%("item","domain","blocks","obstacle","cost","depends"))
print("  "+"-"*98)
for nm,dom,bl,ob,co,de in Q:
    print("  %-30s%-16s%-11s%-13s%-11s%s"%(nm,dom,bl,ob,co,de))
print("\n     **|Q| = %d**"%len(Q))
d=4
def Rop(P):
    Ls=sorted(P); A=[sorted({x[i] for x in Ls}) for i in range(d)]
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}
print("="*92)
print("  CLOSING Q, FIBRED BY DOMAIN")
print("="*92)
fib=defaultdict(set); nm_of=defaultdict(list)
for nm,dom,bl,ob,co,de in Q:
    fib[dom].add((B[bl],O[ob],C[co],D[de])); nm_of[dom].append(nm)
BI={v:k for k,v in B.items()}; OI={v:k for k,v in O.items()}
CI={v:k for k,v in C.items()}; DI={v:k for k,v in D.items()}
print("\n  %-16s%8s%10s%8s"%("domain","cells","E(fibre)","closed"))
print("  "+"-"*44)
tot=cl=0; gaps=[]
for dom in sorted(fib):
    P=fib[dom]; ex=Rop(P)-P
    tot+=1; cl+= (len(ex)==0)
    print("  %-16s%8d%10d%8s"%(dom,len(P),len(ex),"YES" if not ex else "no"))
    if ex: gaps.append((dom,ex))
print("\n     **fibres closed : %d of %d**"%(cl,tot))
if gaps:
    print("\n  ADMITTED AND ABSENT — questions the structure poses:\n")
    for dom,ex in gaps:
        for c in sorted(ex):
            print("     %-15s blocks %-10s obstacle %-12s cost %-10s depends %s"
                  %(dom,BI[c[0]],OI[c[1]],CI[c[2]],DI[c[3]]))
print("="*92)
print("  THE ONE COLUMN THAT MATTERS")
print("="*92)
dep=[de for *_,de in Q]
print("""
     **Every one of the seven has DEPENDS = no.**

  > **Not one open question blocks a result this book relies on.** Q is a list
  > of things that would ADD, not things whose absence subtracts.

     retrievable : %d of 7        requires a new object : %d of 7
     unbounded cost : %d          blocks a stated claim : %d
"""%(sum(1 for *_,o,c,x in Q if o=='retrievable'),
     sum(1 for *_,o,c,x in Q if o=='new object'),
     sum(1 for *_,o,c,x in Q if c=='unbounded'),
     sum(1 for _,_,b,*_ in Q if b=='one claim')))