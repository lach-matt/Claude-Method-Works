import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(421)
print("="*86)
print("  HOW MANY SEED-INDEPENDENT BREAKS ARE THERE?")
print("="*86)
print("""
  A break is a quantity computable from X that is INVARIANT under
  relabelling of the axes. Candidates:

     1. |F(u)|                fibre cardinality        — total preorder
     2. F(u) ⊆ F(v)           fibre containment        — partial order
     3. |F(u) ∩ F(v)|         fibre overlap            — a symmetric weight
     4. the (d−1)-problem     recursive comparison     — needs recursion
""")
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)}
NM=['n','l','k','q','e','f','g','2S']
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def fib(S,d,i,u): return {tuple(x[k] for k in range(d) if k!=i) for x in S if x[i]==u}
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def lat(S,d):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
print("="*86)
print("  BREAK 2 — FIBRE CONTAINMENT, ON Λ")
print("="*86)
print("\n  %6s%10s%40s"%("axis","values","containment relation among fibres"))
print("  "+"-"*66)
d=8; A=alph(LAM,d)
allchain=True
for i in range(d):
    F={u:fib(LAM,d,i,u) for u in A[i]}
    rel=[]
    for u,v in permutations(A[i],2):
        if F[u]<F[v]: rel.append("%s<%s"%(u,v))
    ch=all(F[u]<=F[v] or F[v]<=F[u] for u in A[i] for v in A[i])
    allchain &= ch
    print("  %6s%10s   chain=%-6s %s"%(NM[i],A[i],ch,", ".join(rel[:6])))
print("\n     **every axis's fibres form a chain : %s**"%allchain)
if allchain:
    o=[]
    for i in range(d):
        F={u:fib(LAM,d,i,u) for u in A[i]}
        o.append(sorted(A[i],key=lambda u:len(F[u])))
    print("     order by fibre containment  = %s"%[list(x) for x in o][:4],"...")
    print("     equals the given order      : %s"%all(list(o[i])==sorted(A[i]) for i in range(d)))
    print("     still a sublattice          : %s"%lat(relab(LAM,o,d),d))
print("="*86)
print("  AND HOW OFTEN DOES CONTAINMENT DECIDE, IN GENERAL?")
print("="*86)
def reord(S,dd):
    Aa=alph(S,dd)
    if int(np.prod([math.factorial(len(a)) for a in Aa]))>2*10**6: return None
    for ps in product(*[list(permutations(a)) for a in Aa]):
        if lat(relab(S,[list(p) for p in ps],dd),dd): return True
    return False
def contain_order(S,dd):
    Aa=alph(S,dd); out=[]
    for i in range(dd):
        F={u:fib(S,dd,i,u) for u in Aa[i]}
        if not all(F[u]<=F[v] or F[v]<=F[u] for u in Aa[i] for v in Aa[i]): return None
        out.append(sorted(Aa[i],key=lambda u:len(F[u])))
    return out
print("\n  %5s%7s%9s%14s%16s%14s%12s"%("d","|A|","n","reorderable","chain on all axes","order works","exact"))
print("  "+"-"*80)
for dd,a,lim in [(2,3,200),(2,4,100),(3,2,200),(3,3,70)]:
    n=r=ch=wk=ex=0
    for _ in range(lim):
        Ax=[list(range(a)) for _ in range(dd)]
        cells=list(product(*Ax))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,dd)
        if any(len(x)<2 for x in Aa): continue
        rr=reord(S,dd)
        if rr is None: continue
        n+=1; r+=rr
        o=contain_order(S,dd)
        if o is None: ex+= (rr==False); continue
        ch+=1
        w=lat(relab(S,o,dd),dd); wk+=w
        ex+= (w==rr) if w else (rr==False)
    print("  %5d%7d%9d%14d%16d%14d%12d"%(dd,a,n,r,ch,wk,ex))