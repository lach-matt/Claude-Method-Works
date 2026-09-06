import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(397)
print("="*86)
print("  WHY BOTH REDUCTIONS OVER-CONSTRAINED")
print("="*86)
print("""
  In this problem **every pair of cells contributes a constraint**, and the
  constraints are derived from a lattice structure. So an encoder cannot
  isolate one clause from another: removing a corner to forbid one
  orientation also removes a join some other pair needs.

  > **The constraint system is closed under implication. Arbitrary 3-SAT is
  > not.** So SAT does not embed — and that is evidence the problem is
  > EASIER than NP-hard, not harder.

  **Test the consequence.** If the constraints are implication-closed, then
  propagating them to a fixed point should DECIDE, with no search.
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
def propagate(S,d):
    """
    Order variables: for axis i and values u<v, rel[i][(u,v)] ∈ {'<','>',None}.
    Constraint from a pair x,y and an ABSENT corner c: at least one axis must
    orient against c.  Propagate unit implications to a fixed point.
    """
    A=alph(S,d); Ss=set(S)
    rel={}
    for i in range(d):
        for u,v in combinations(A[i],2): rel[(i,u,v)]=None
    def orient(i,a,b):
        """is a<b currently forced?  returns True/False/None"""
        if a==b: return None
        u,v=min(a,b),max(a,b); r=rel[(i,u,v)]
        if r is None: return None
        lt = (r=='<')
        return lt if (a,b)==(u,v) else (not lt)
    clauses=[]
    for x,y in combinations(sorted(S),2):
        I=[i for i in range(d) if x[i]!=y[i]]
        if not I: continue
        for bits in product([0,1],repeat=len(I)):
            c=list(x); o=list(x)
            for t,i in enumerate(I):
                if bits[t]: c[i]=y[i]; o[i]=x[i]
                else: c[i]=x[i]; o[i]=y[i]
            if tuple(c) not in Ss:
                # forbid: NOT(for all t: c is the max on axis I[t])
                lits=[]
                for t,i in enumerate(I):
                    hi = y[i] if bits[t] else x[i]
                    lo = x[i] if bits[t] else y[i]
                    lits.append((i,hi,lo))   # to satisfy: hi < lo on axis i
                clauses.append(lits)
    changed=True; it=0
    while changed and it<400:
        changed=False; it+=1
        for lits in clauses:
            und=[]; sat=False
            for (i,hi,lo) in lits:
                v=orient(i,hi,lo)
                if v is True: sat=True; break
                if v is None: und.append((i,hi,lo))
            if sat: continue
            if not und: return False,it
            if len(und)==1:
                i,hi,lo=und[0]
                u,v2=min(hi,lo),max(hi,lo)
                rel[(i,u,v2)] = '<' if (hi,lo)==(u,v2) else '>'
                changed=True
    return None,it
print("  %5s%7s%9s%14s%14s%14s%12s"%("d","|A|","n","reorderable","prop says NO","prop unsure","wrong NO"))
print("  "+"-"*76)
for d,a,lim in [(2,3,220),(2,4,110),(3,2,220),(3,3,70)]:
    n=r=no=un=bad=0
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        rr=reord(S,d)
        if rr is None: continue
        n+=1; r+=rr
        v,it=propagate(S,d)
        if v is False:
            no+=1
            if rr: bad+=1
        else: un+=1
    print("  %5d%7d%9d%14d%14d%14d%12d"%(d,a,n,r,no,un,bad))
print("""
  **'wrong NO' must be zero** — propagation may only reject when no order
  exists. **The 'unsure' column is what search still has to resolve.**
""")
print("="*86)
print("  AND HOW OFTEN DOES PROPAGATION DECIDE COMPLETELY?")
print("="*86)
for d,a,lim in [(3,2,300),(3,3,90)]:
    n=dec=0
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        rr=reord(S,d)
        if rr is None: continue
        n+=1
        v,it=propagate(S,d)
        if (v is False and not rr): dec+=1
    print("\n     d=%d |A|=%d : propagation correctly rejected %d of %d"%(d,a,dec,n))