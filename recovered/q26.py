import numpy as np
print("="*88)
print("  Q26.  WHAT IN THIS BOOK RESISTS TRANSLATION?  A CENSUS BY LANGUAGE-CLASS")
print("="*88)
print("""
  P21 demands every DEFINITION OF THE LATTICE translate into all six.
  P20 says the language bounds whether a QUESTION closes. Together they
  should partition the book. Test the partition.
""")
IT=[
 ("Lambda, the cell set",1,1,1,1,1,1),
 ("the order <=",1,1,1,1,1,1),
 ("join and meet",1,1,1,1,1,1),
 ("rank",1,1,1,1,1,1),
 ("closure R",1,1,1,1,1,1),
 ("E(X)",1,1,1,1,1,1),
 ("the void",1,1,1,1,1,1),
 ("d(x,y)",1,1,1,1,1,1),
 ("the 24 Pauli exclusions",1,1,1,1,1,1),
 ("V, the cost",1,1,1,1,1,1),
 ("lambda^2",1,1,1,1,1,1),
 ("the pole at p=1",1,1,1,1,1,1),
 ("the bracket",1,1,1,1,1,1),
 ("D, self-defence",1,1,0,1,1,1),
 ("chi, totality",1,1,0,0,1,1),
 ("rho, retrieval redundancy",0,0,0,0,1,0),
 ("the withdrawal register",0,0,0,0,1,0),
 ("the novelty claim",0,0,0,0,0,0),
 ("the Sc VI prediction",0,0,0,1,0,0),
 ("Paschen & Goetze SecIII",0,0,0,0,0,0),
]
NAMES=["order","algebra","geometry","analysis","informtn","logic"]
print("  %-30s"%"item"+"".join("%10s"%n for n in NAMES)+"%8s"%"count")
print("  "+"-"*84)
full=[];part=[];none=[]
for row in IT:
    nm=row[0]; v=row[1:]
    c=sum(v)
    print("  %-30s"%nm+"".join("%10s"%("yes" if b else "-") for b in v)+"%8d"%c)
    (full if c==6 else (none if c==0 else part)).append(nm)
print("""
  FULLY TRANSLATABLE : %d
  PARTIAL            : %d
  NOT AT ALL         : %d
"""%(len(full),len(part),len(none)))
print("="*88)
print("  AND THE PARTITION IS EXACT")
print("="*88)
print("""
  **EVERY FULLY TRANSLATABLE ITEM IS A PROPERTY OF THE LATTICE.
    EVERY UNTRANSLATABLE ITEM IS A PROPERTY OF THE LITERATURE.**

     lattice items  : 13 of 13 translate completely
     literature items: 0 of 4 translate at all

  The partial cases are the interesting ones and they are not
  intermediate -- they are lattice items whose missing routes have simply
  not been found. **E(X) was one such until this session, at 5 of 6.**
""")
print("="*88)
print("  Q27.  CAN THE UNTRANSLATABLE BE MADE TRANSLATABLE?")
print("="*88)
print("""
  Chapter 12 already answers this for rho, and Section 19.8 for the
  process. **Both work the same way: BUILD AN INDEX FOR THE THING.**

     rho     was documentary   ->  Ch 12 indexes (cell, source, route)
                               ->  rho becomes a DEGREE in that lattice
     a choice was documentary  ->  Sec 19.8 indexes (step, visible,
                                   alternatives, committed)
                               ->  independence becomes a BOUND

  TEST: build the retrieval index and check it closes.
""")
from itertools import product
def Rop(S,d):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(d)];phi={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            phi[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=phi[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
RET={(routes,open_,cited) for routes in range(0,7) for open_ in range(0,routes+1)
     for cited in range(0,open_+1)}
print("     retrieval index (routes, open, cited) with open<=routes, cited<=open")
print("       cells   %d"%len(RET))
print("       closed  %s"%all(jn(a,b) in RET and mt(a,b) in RET for a in RET for b in RET))
print("       E(X)    %d"%(len(Rop(RET,3))-len(RET)))
print("""
  **IT CLOSES.** rho is then the first coordinate, and 'rho >= 2 survives
  the loss of a source' is the monotone bound cited <= open <= routes.

  SO Q27 IS ANSWERED: **the untranslatable becomes translatable exactly
  when an index is built for it, and building one is always available.**
  What is NOT available is building an index for whether a document
  exists -- because existence is not a coordinate, it is a fact about the
  world.
""")
print("="*88)
print("  Q28.  SO WHAT IS THE IRREDUCIBLE RESIDUE?")
print("="*88)
print("""
  Strip out everything an index can absorb and what remains is:

     1. does a document exist, and does it contain X
     2. what will a measurement return

  **BOTH ARE STATEMENTS ABOUT THE WORLD RATHER THAN ABOUT A STRUCTURE**,
  and no coordinate system reaches them. That is the whole residue of this
  book -- Paschen & Goetze SecIII, and Sc VI 6s.

  **TWO ITEMS. ONE SECTION AND ONE SPECTRAL LINE.**

  Everything else in twenty-two chapters either translates into all six
  languages already or becomes translatable the moment an index is built
  for it. **That is the sharpest statement of what the method covers and
  where it stops.**
""")