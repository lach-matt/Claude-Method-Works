import numpy as np, random
from itertools import product, combinations
random.seed(433)
print("="*88)
print("  FAMILIES WITHIN THE INDEX vs FAMILIES THE INDEX BELONGS TO")
print("="*88)
print("""
  **Two different claims.**

     Λ contains its own rules  ->  does it contain the rules of families
                                   WITHIN it?          (testable)

     Λ contains its own rules  ->  does it contain the rules of the family
                                   of all closed sets?  (a meta-level, and
                                   the earlier measurement was about this)

  **The first is the one the argument supports.** Test it.
""")
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)}
d=8
def Rop(S):
    Ls=sorted(S); A=[sorted({x[i] for x in Ls}) for i in range(d)]
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
def E(S): return len(Rop(S))-len(S)
def sublat(S):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
print("="*88)
print("  1.  THE FIBRES THE BOOK ALREADY NAMES")
print("="*88)
print("\n  %10s%10s%10s%12s%12s"%("family","cells","E(X)","sublattice","closed"))
print("  "+"-"*56)
for q in range(4):
    Aq={x for x in LAM if x[3]==q}
    if Aq: print("  %10s%10d%10d%12s%12s"%("q=%d"%q,len(Aq),E(Aq),sublat(Aq),E(Aq)==0))
for n0 in (1,2,3):
    Sn={x for x in LAM if x[0]==n0}
    print("  %10s%10d%10d%12s%12s"%("n=%d"%n0,len(Sn),E(Sn),sublat(Sn),E(Sn)==0))
print("="*88)
print("  2.  RANDOM SUBLATTICES OF Λ — ARE THEY ALL CLOSED?")
print("="*88)
def gen_sublat(S,k):
    """close a random seed under join and meet"""
    cur=set(random.sample(sorted(S),k))
    while True:
        new=set(cur)
        for x,y in combinations(sorted(cur),2):
            new.add(tuple(max(x[i],y[i]) for i in range(d)))
            new.add(tuple(min(x[i],y[i]) for i in range(d)))
        new &= set(S)
        if new==cur: break
        cur=new
        if len(cur)>300: break
    return cur
print("\n  %10s%12s%12s%14s"%("seed size","n","all sublat","all E = 0"))
print("  "+"-"*50)
for k in (2,3,4,5):
    n=sl=e0=0
    for _ in range(30):
        G=gen_sublat(LAM,k)
        if len(G)<2 or len(G)>250: continue
        n+=1; sl+=sublat(G); e0+= (E(G)==0)
    if n: print("  %10d%12d%12d%14d"%(k,n,sl,e0))
print("="*88)
print("  3.  AND INTERVALS — THE SUB-FAMILIES §3.5 NAMES")
print("="*88)
print("\n  %14s%10s%10s%12s"%("interval","cells","E(X)","closed"))
print("  "+"-"*48)
LS=sorted(LAM)
cnt=0; allz=0
for _ in range(40):
    a,b=random.sample(LS,2)
    lo=tuple(min(a[i],b[i]) for i in range(d)); hi=tuple(max(a[i],b[i]) for i in range(d))
    I={x for x in LAM if all(lo[i]<=x[i]<=hi[i] for i in range(d))}
    if len(I)<2: continue
    cnt+=1; z=(E(I)==0); allz+=z
    if cnt<=6: print("  %14s%10d%10d%12s"%("sampled",len(I),E(I),z))
print("\n     intervals tested %d   with E = 0 : %d  (%.0f%%)"%(cnt,allz,100*allz/max(cnt,1)))
print("""
{0}
  WHAT THIS SETTLES
{0}
""".format("="*88))
print("""  **If every sublattice and every interval of Λ has E = 0, the argument
  holds: the index's rules descend to every family within it.** The
  measurements above say whether they do.

  **And the earlier negative stands unchanged** — the family of ALL closed
  sets is a family Λ BELONGS TO, not one it contains, and nothing about
  Λ's own completeness constrains it.
""")