import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(401)
print("="*86)
print("  A FORCING RELATION ON EACH AXIS")
print("="*86)
print("""
  Fix axis i. For value u let F(u) = the cells with x_i = u, projected onto
  the other axes. If X is a sublattice and u < v then for x ∈ F(v), y ∈ F(u):

     join(x,y) has axis-i value v  ->  **F(u) ∨ F(v) ⊆ F(v)**
     meet(x,y) has axis-i value u  ->  **F(u) ∧ F(v) ⊆ F(u)**

  **That is asymmetric in u and v, so it FORCES an orientation** — and it is
  computable from X alone, with no reference to any order.
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
def fib(S,d,i,u):
    return {tuple(x[k] for k in range(d) if k!=i) for x in S if x[i]==u}
def forces(S,d,i,u,v):
    """can u precede v?  (F(u)∨F(v) ⊆ F(v) and F(u)∧F(v) ⊆ F(u))"""
    Fu=fib(S,d,i,u); Fv=fib(S,d,i,v)
    m=d-1
    for x in Fu:
        for y in Fv:
            if tuple(max(x[t],y[t]) for t in range(m)) not in Fv: return False
            if tuple(min(x[t],y[t]) for t in range(m)) not in Fu: return False
    return True
def build_order(S,d):
    """for each axis, the forcing relation; then test if it admits a total order"""
    A=alph(S,d); out=[]
    for i in range(d):
        vals=A[i]; ok=[]
        for u,v in permutations(vals,2):
            if forces(S,d,i,u,v): ok.append((u,v))
        allowed=set(ok)
        # find total orders consistent with the allowed relation
        good=[]
        for p in permutations(vals):
            if all((p[a],p[b]) in allowed for a in range(len(p)) for b in range(a+1,len(p))):
                good.append(p)
        out.append(good)
    return out
print("  %5s%7s%9s%14s%18s%14s"%("d","|A|","n","reorderable","forcing admits","exact"))
print("  "+"-"*70)
for d,a,lim in [(2,3,200),(2,4,100),(3,2,200),(3,3,70)]:
    n=r=adm=ex=0
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        rr=reord(S,d)
        if rr is None: continue
        n+=1; r+=rr
        cand=build_order(S,d)
        has=all(len(c)>0 for c in cand)
        adm+=has
        ex+= (has==rr)
    print("  %5d%7d%9d%14d%18d%14d"%(d,a,n,r,adm,ex))
print("="*86)
print("  AND IS THE FORCED ORDER THE RIGHT ONE?")
print("="*86)
tot=0; works=0; sizes=[]
for _ in range(400):
    d=3; a=random.choice([2,3])
    A=[list(range(a)) for _ in range(d)]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(2,len(cells))))
    Aa=alph(S,d)
    if any(len(x)<2 for x in Aa): continue
    rr=reord(S,d)
    if rr is not True: continue
    cand=build_order(S,d)
    if any(len(c)==0 for c in cand): continue
    tot+=1; sizes.append(int(np.prod([len(c) for c in cand])))
    hit=False
    for ps in product(*cand):
        if lat(relab(S,[list(p) for p in ps],d),d): hit=True; break
    works+=hit
print("\n     reorderable instances with a non-empty forcing set : %d"%tot)
print("     a forced candidate actually works                  : %d  (%.0f%%)"%(works,100*works/max(tot,1)))
if sizes: print("     candidates left, median %d  max %d   (full space would be %d)"%(int(np.median(sizes)),max(sizes),6**3))