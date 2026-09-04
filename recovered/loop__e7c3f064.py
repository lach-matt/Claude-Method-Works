import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(409)
print("="*86)
print("  THE COUPLING: FORCING ON AXIS i NEEDS THE ORDERS OF THE OTHERS")
print("="*86)
print("""
  F(u) ∨ F(v) takes componentwise max **on the other axes**, so the max
  depends on THEIR orders. **The forcing relation is not order-free.**

  > **It is a self-feeding loop**: orders fixed so far determine forcing on
  > the rest, which determines more orders.

  Implement it as a fixed-point iteration over partial orders.
""")
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def lat(S,d):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
def reord(S,d):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>2*10**6: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def forces_given(S,d,i,u,v,rank):
    """can u precede v on axis i, GIVEN ranks on the other axes?"""
    others=[k for k in range(d) if k!=i]
    Fu=[x for x in S if x[i]==u]; Fv=[x for x in S if x[i]==v]
    Ss=set(S)
    for x in Fu:
        for y in Fv:
            j=list(x); m=list(x)
            j[i]=v; m[i]=u
            for k in others:
                a,b=x[k],y[k]
                if rank[k][a]<=rank[k][b]: j[k]=b; m[k]=a
                else: j[k]=a; m[k]=b
            if tuple(j) not in Ss or tuple(m) not in Ss: return False
    return True
def loop(S,d,rounds=8):
    """fixed-point: recompute the forcing relation with current ranks, resort, repeat"""
    A=alph(S,d)
    rank=[{v:i for i,v in enumerate(a)} for a in A]
    hist=[]
    for it in range(rounds):
        newrank=[]
        stable=True
        for i in range(d):
            vals=A[i]
            allowed={(u,v) for u,v in permutations(vals,2) if forces_given(S,d,i,u,v,rank)}
            # find a total order consistent with 'allowed'
            got=None
            for p in permutations(vals):
                if all((p[a],p[b]) in allowed for a in range(len(p)) for b in range(a+1,len(p))):
                    got=p; break
            if got is None: return None,it
            nr={v:k for k,v in enumerate(got)}
            if nr!=rank[i]: stable=False
            newrank.append(nr)
        rank=newrank
        hist.append(stable)
        if stable: break
    order=[sorted(A[i],key=lambda v:rank[i][v]) for i in range(d)]
    return order,it
print("  %5s%7s%9s%14s%16s%14s%12s"%("d","|A|","n","reorderable","loop finds one","loop says no","exact"))
print("  "+"-"*80)
for d,a,lim in [(2,3,200),(2,4,100),(3,2,200),(3,3,70)]:
    n=r=found=no=ex=0
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        rr=reord(S,d)
        if rr is None: continue
        n+=1; r+=rr
        o,it=loop(S,d)
        if o is None: no+=1; ok=(rr==False)
        else:
            good=lat(relab(S,o,d),d)
            found+=good
            ok=(good==rr) if good else None
            if not good: ok=(rr==False)
        ex+= bool(ok)
    print("  %5d%7d%9d%14d%16d%14d%12d"%(d,a,n,r,found,no,ex))
print("""
  **'exact' counts instances where the loop's verdict matched brute force.**
  If the loop converges to a valid order whenever one exists, the d ≥ 3
  question has a procedure — the loop is polynomial per round.
""")