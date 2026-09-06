import numpy as np, random
from itertools import product, permutations
from math import factorial
random.seed(107)
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def Rsize(T):
    A=[sorted({t[i] for t in T}) for i in range(2)]
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in T if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N={};run=-1
    for w in A[1]:
        c=[x for (x,y) in T if y<=w]; run=max(run,max(c) if c else -1); N[w]=run
    return sum(1 for r in A[0] for c in A[1] if c<=M[r] and r<=N[c])
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def E(S,o):
    T=relabel(S,o); return Rsize(T)-len(T)
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if E(S,[list(p0),list(p1)])==0: return True
    return False
def lin_ext(elems,lt,cap=400):
    """linear extensions of a STRICT partial order; ties are free"""
    out=[]
    def rec(rem,acc):
        if len(out)>=cap: return
        if not rem: out.append(list(acc)); return
        for e in sorted(rem):
            if not any(lt(f,e) for f in rem if f!=e):
                rec(rem-{e},acc+[e])
    rec(set(elems),[])
    return out
def derive(S,cap=400):
    A=alpha(S)
    sup={r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
    col={c:frozenset(a for (a,b) in S if b==c) for c in A[1]}
    R=lin_ext(A[0],lambda p,q: sup[p]<sup[q],cap)          # strict
    C=lin_ext(A[1],lambda p,q: col[q]<col[p],cap)
    return R,C
print("="*88)
print("  WITH TIES HANDLED, THE ENUMERATION IS NON-EMPTY")
print("="*88)
inst=[]
while len(inst)<400:
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if reorderable(S): inst.append(S)
sz=[]; ok=0; miss=[]
for S in inst:
    R,C=derive(S); sz.append(len(R)*len(C))
    got=any(E(S,[r,c])==0 for r in R for c in C)
    ok+=got
    if not got and len(miss)<3: miss.append(S)
print("\n     reorderable instances                 : %d"%len(inst))
print("     linear-extension pairs, median / max  : %d / %d"%(int(np.median(sz)),max(sz)))
print("     a pair achieving E = 0 exists         : %d  (%.1f%%)"%(ok,100*ok/len(inst)))
full=[factorial(len(alpha(S)[0]))*factorial(len(alpha(S)[1])) for S in inst]
print("     full search space, median             : %d"%int(np.median(full)))
print("     reduction factor, median              : %.1fx"%np.median([f/max(e,1) for f,e in zip(full,sz)]))
if miss:
    print("\n     instances the extension space MISSES:")
    for S in miss: print("       ",sorted(S))
print("="*88)
print("  AND ON THE INSTANCES DESCENT CANNOT SOLVE")
print("="*88)
def descend1(S,maxit=200):
    A=alpha(S); o=[list(A[0]),list(A[1])]; e=E(S,o); it=0
    while e>0 and it<maxit:
        best=None
        for ax in (0,1):
            for i in range(len(o[ax])-1):
                p=[list(x) for x in o]; p[ax][i],p[ax][i+1]=p[ax][i+1],p[ax][i]
                v=E(S,p)
                if best is None or v<best[0]: best=(v,p)
        if best[0]>=e: break
        e,o=best; it+=1
    return e
stuck=[S for S in inst if descend1(S)>0]
solved=0
for S in stuck:
    R,C=derive(S)
    solved+=any(E(S,[r,c])==0 for r in R for c in C)
print("\n     descent-1 stalls on            : %d"%len(stuck))
print("     linear extensions solve them   : %d  (%.0f%%)"%(solved,100*solved/max(len(stuck),1)))
print("="*88)
print("  LARGER INSTANCES")
print("="*88)
big=[]
while len(big)<150:
    A=[list(range(random.randint(4,6))),list(range(random.randint(4,6)))]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(1,len(cells))))
    if reorderable(S): big.append(S)
ok2=0; sz2=[]; f2=[]
for S in big:
    R,C=derive(S,cap=600); sz2.append(len(R)*len(C))
    f2.append(factorial(len(alpha(S)[0]))*factorial(len(alpha(S)[1])))
    ok2+=any(E(S,[r,c])==0 for r in R for c in C)
print("\n     %d reorderable, alphabets 4-6"%len(big))
print("     solved by linear extensions : %d  (%.1f%%)"%(ok2,100*ok2/len(big)))
print("     search size, median         : %d  vs full %d   (%.0fx smaller)"
      %(int(np.median(sz2)),int(np.median(f2)),np.median([a/max(b,1) for a,b in zip(f2,sz2)])))
print("""
{0}
  VERDICT
{0}
""".format("="*88))
if ok==len(inst) and ok2==len(big):
    print("""  **THE LINEAR-EXTENSION SPACE CONTAINS EVERY SOLUTION, AT BOTH SIZES.**

  It is not a landscape and has no traps: it is an ENUMERATION of the
  orders the structure itself admits, derived from the inclusion order and
  nothing else. **The transposition search had traps because it moved
  through orders the structure does not admit.**

  **And it is the object §7.9 already names** — Birkhoff's linear
  extensions — used there to count maximal chains and never used as a
  search space.""")
else:
    print("""  **NOT COMPLETE: %d of %d small, %d of %d large.** The inclusion order
  is the right KIND of object and not yet the right relation."""%(ok,len(inst),ok2,len(big)))