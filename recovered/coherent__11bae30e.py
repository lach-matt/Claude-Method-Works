import numpy as np
from itertools import product
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=list(product(*AX)); LAM={z for z in BOX if all(z[v]<=ub(z) for v,p,ub in CONS)}
d=8
def C(S):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
y=(1,0,1,0,1,0,0,2)
FAKE=C(LAM|{y})
print("="*84)
print("  TWO INDICES.  ONE IS TRUE, ONE IS NOT.")
print("="*84)
print("""
  Λ      976 cells, the real electron configurations
  FAKE  %d cells, built by inserting ONE impossible configuration
        (one electron with spin multiplicity 2) and letting the closure
        supply everything that follows
"""%len(FAKE))
print("  %-34s%14s%14s"%("test","Λ","FAKE"))
print("  "+"-"*62)
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
def row(nm,f):
    print("  %-34s%14s%14s"%(nm,f(LAM),f(FAKE)))
row("cells",lambda S:len(S))
row("closed under join and meet",lambda S:all(jn(a,b) in S and mt(a,b) in S for a in S for b in S))
row("E(X)",lambda S:len(C(S))-len(S))
row("fixed point of R",lambda S:C(S)==S)
print("""
  **THE REMOVABILITY TEST HAS NOTHING TO WORK ON.** It asks whether the
  GAPS vanish under re-coordinatisation. **Neither index has any gaps.**
  E = 0 for both, in every coordinate system, because both are complete.
""")
print("="*84)
print("  RE-COORDINATISE BOTH AND SEE")
print("="*84)
def perm(S,p): return {tuple(z[i] for i in p) for z in S}
import random; random.seed(5)
print("\n  %-24s%12s%12s"%("coordinate order","E(Λ)","E(FAKE)"))
print("  "+"-"*50)
for t in range(5):
    p=list(range(8)); random.shuffle(p)
    a=len(C(perm(LAM,p)))-len(LAM); b=len(C(perm(FAKE,p)))-len(FAKE)
    print("  %-24s%12d%12d"%(str(p),a,b))
print("""
  **IDENTICAL IN EVERY ONE.** The test that separated the periodic table
  from the asteroid belt cannot separate these, and it never could:

     that test finds MISSING CELLS and asks whether the gap is real
     **a coherent fabrication has no missing cells. It is full.**
""")
print("="*84)
print("  SO WHAT IS THE DIFFERENCE BETWEEN THEM?")
print("="*84)
sat=lambda x: all(x[v]<=ub(x) for v,p,ub in CONS)
bad=[z for z in FAKE if not sat(z)]
print("\n     cells in FAKE that no atom can have : %d"%len(bad))
print("     first three:")
for z in sorted(bad)[:3]:
    print("        (n=%d ℓ=%d k=%d q=%d e=%d f=%d g=%d 2S=%d)  — %d electrons, spin %d"
          %(z+(z[2],z[7])))
print("""
  **THE DIFFERENCE IS NOT IN THE STRUCTURE. IT IS IN WHETHER THE CELLS
  DESCRIBE ANYTHING.** And no property of the structure records that.

  **THE PLAIN VERSION:**

     a DEFECTIVE index is a map with a street missing. You can catch it
     by redrawing the map — the street reappears in another projection.
     That is the Janet test.

     a COHERENT FABRICATION is a complete, consistent map of a city that
     does not exist. Every street connects. Every distance adds up.
     **Redrawing it changes nothing, because nothing is missing.**

  **The only thing that distinguishes a map of a real city from a perfect
  map of an imaginary one is going there.** In this book, going there means
  measuring a level — and that is all D_phys has ever been.
""")
print("="*84)
print("  AND THE BOOK'S FIVE RECORDED FAILURES ARE ALL OF THIS KIND")
print("="*84)
print("""
     a wrong nuclear charge      every derived value shifts together;
                                 the index stays consistent
     a wrong ionisation limit    every term value shifts together
     a mislabelled parent        the whole channel moves as one

  **None is a missing cell. Each is a complete index of something that
  is not there**, and each was caught by a measured number the index could
  not supply: a quantum defect of 4.9, a negative term value.
""")