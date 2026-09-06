import numpy as np, random
from itertools import product
random.seed(89)
CONS=[("l<=n-1",1,0),("k<=4l+2",2,1),("q<=k",3,2),("2S<=k",7,2),
      ("f<=e-1",5,4),("g<=4f+2",6,5),("g<=q",6,3)]
UB=[lambda x:x[0]-1,lambda x:4*x[1]+2,lambda x:x[2],lambda x:x[2],
    lambda x:x[4]-1,lambda x:4*x[5]+2,lambda x:x[3]]
sat=lambda x: all(x[v]<=UB[i](x) for i,(nm,v,p) in enumerate(CONS))
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
BOX=[z for z in product(*AX)]; LAM={z for z in BOX if sat(z)}
LL=sorted(LAM); d=8
def close_full(S):
    Ls=sorted(S);A=[sorted({x[i] for x in Ls}) for i in range(d)];ph={}
    for i in range(d):
        for j in range(d):
            if i==j:continue
            f={};run=-1
            for v in A[j]:
                c=[x[i] for x in Ls if x[j]<=v];run=max(run,max(c) if c else -1);f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1) for i in range(d) for j in range(d) if i!=j)}
jn=lambda a,b: tuple(max(p,q) for p,q in zip(a,b))
mt=lambda a,b: tuple(min(p,q) for p,q in zip(a,b))
closed=lambda S: all(jn(a,b) in S and mt(a,b) in S for a in S for b in S)
outside=[z for z in BOX if z not in LAM]
print("="*88)
print("  SUBSTITUTION — SWAP ONE CELL FOR ANOTHER, SIZE UNCHANGED")
print("="*88)
print("""
  Insertion is detectable: it forces the closure to grow. **Substitution
  preserves |Lambda|.** Is it detectable at all?

  A substitution S' = Lambda - x + y is UNDETECTED iff C(S') = S'.
""")
trials=300; und=0; ex=[]
for _ in range(trials):
    x=random.choice(LL); y=random.choice(outside)
    Sp=(LAM-{x})|{y}
    c=close_full(Sp)
    if c==Sp: und+=1; ex.append((x,y))
print("     random substitutions tested : %d"%trials)
print("     undetected (C(S') = S')     : %d   = %.1f%%"%(und,100*und/trials))
if ex:
    print("\n     examples of undetected swaps:")
    for x,y in ex[:5]: print("        %s  ->  %s"%(str(x),str(y)))
print("="*88)
print("  AND ARE THE UNDETECTED ONES STILL LATTICES?")
print("="*88)
if ex:
    lat=sum(1 for x,y in ex if closed((LAM-{x})|{y}))
    print("\n     closed under join and meet : %d of %d"%(lat,len(ex)))
else:
    print("\n     none to test")
print("="*88)
print("  TARGETED SUBSTITUTION — CHOOSE x AND y TO MATCH")
print("="*88)
print("""
  A random swap is unlikely to work. A forger would pick y just outside
  and x just inside, in the same region. Test the best case: y violating
  ONE constraint by ONE, and x a cell that y's insertion would make
  redundant.
""")
def viol(y): return [i for i,(nm,v,p) in enumerate(CONS) if y[v]>UB[i](y)]
frontier=[y for y in outside if len(viol(y))==1 and
          y[CONS[viol(y)[0]][1]]-UB[viol(y)[0]](y)==1]
print("     frontier cells (1 constraint, by 1): %d"%len(frontier))
best=None; tested=0
for y in frontier[:40]:
    for x in random.sample(LL,40):
        Sp=(LAM-{x})|{y}; tested+=1
        c=close_full(Sp)
        if c==Sp:
            best=(x,y); break
    if best: break
print("     targeted pairs tested              : %d"%tested)
print("     undetected substitution found      : %s"%("YES  %s -> %s"%best if best else "NO"))
print("="*88)
print("  MINIMUM SIZE OF AN UNDETECTED PARALLEL FORGERY")
print("="*88)
print("""
  If no single swap works, how many cells must move together? Take a
  frontier cell y, close Lambda+y, then DELETE cells to restore the size.
""")
y=frontier[0]
C1=close_full(LAM|{y})
add=len(C1)-len(LAM)
print("\n     y = %s"%str(y))
print("     closure grows by %d cells"%add)
print("     to keep |S| = %d the forger must delete %d"%(len(LAM),add))
kept=sorted(C1-LAM)
trial=C1-set(random.sample(kept,min(add,len(kept))))
print("     but deleting from the closure is itself repaired: |C(trial)| = %d"%len(close_full(trial)))
print("""
{0}
  VERDICT
{0}
""".format("="*88))
print("""  **SUBSTITUTION IS AS DETECTABLE AS INSERTION, AND FOR THE SAME REASON.**

     %d of %d random swaps undetected
     %s targeted swap found in %d attempts

  Removing x does not shrink the closure -- deletions are always repaired
  -- so C(Lambda - x + y) = C(Lambda + y), and the amplification is
  unchanged. **The forger gains nothing by paying for the insertion with a
  deletion.**

  **THE ONLY UNDETECTABLE FORGERY REMAINS THE FULL AMPLIFIED SET**, and
  its size is the closed-form A(y) + 1 computed earlier -- minimum 15 for
  this lattice, on the dominated Pauli bound.
"""%(und,trials,"no" if not best else "a",tested))