import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(499)
print("="*88)
print("  THE SET OF VALID ORDERS, AS AN OBJECT")
print("="*88)
print("""
  Stop treating the valid orders as a search target. **Ask what they are.**

     · how many?
     · CONNECTED under adjacent transpositions, through valid orders?
     · an interval in some order?  a coset?

  **If connected, one seed plus local moves reaches all of them** — and the
  descent's local minima are explained. **If disconnected, that is the
  structural obstacle, stated.**
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
def valid_orders(S,d,cap=200000):
    A=alph(S,d)
    tot=int(np.prod([math.factorial(len(a)) for a in A]))
    if tot>cap: return None,tot
    out=[]
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): out.append(tuple(ps))
    return out,tot
def nbrs(o):
    """adjacent transposition on one axis"""
    out=[]
    for i in range(len(o)):
        p=list(o[i])
        for t in range(len(p)-1):
            q=list(p); q[t],q[t+1]=q[t+1],q[t]
            oo=list(o); oo[i]=tuple(q); out.append(tuple(oo))
    return out
print("  %5s%7s%9s%12s%12s%14s%16s"%("d","|A|","n","valid","total","components","largest comp"))
print("  "+"-"*78)
for d,a,lim in [(2,3,120),(2,4,60),(3,2,120),(3,3,40)]:
    n=0; comps=[]; frac=[]
    for _ in range(lim):
        Ax=[list(range(a)) for _ in range(d)]
        cl=list(product(*Ax))
        S=set(random.sample(cl,random.randint(2,len(cl))))
        A=alph(S,d)
        if any(len(x)<2 for x in A): continue
        V,tot=valid_orders(S,d)
        if V is None or len(V)<2: continue
        n+=1
        VS=set(V); seen=set(); c=0; big=0
        for v in V:
            if v in seen: continue
            c+=1; st=[v]; seen.add(v); sz=0
            while st:
                u=st.pop(); sz+=1
                for w in nbrs(u):
                    if w in VS and w not in seen: seen.add(w); st.append(w)
            big=max(big,sz)
        comps.append(c); frac.append(big/len(V))
    if n: print("  %5d%7d%9d%12s%12s%14.2f%16.3f"%(d,a,n,"—","—",np.mean(comps),np.mean(frac)))
print("""
  **components = 1 means the valid orders form a single connected region** —
  reachable from any one of them by adjacent transpositions without leaving
  the valid set.
""")
print("="*88)
print("  AND IS THE VALID SET AN INTERVAL?")
print("="*88)
print("""
  If the valid orders are an INTERVAL in the product of weak Bruhat orders,
  they have a unique minimum and maximum — **and the minimum is computable
  greedily.** Test for a unique minimal element under inversion count.
""")
def inv(p):
    return sum(1 for i in range(len(p)) for j in range(i+1,len(p)) if p[i]>p[j])
def tot_inv(o): return sum(inv(list(p)) for p in o)
n=uniq=0
for _ in range(300):
    d=random.choice([2,3]); a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(2,len(cl))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    V,tot=valid_orders(S,d)
    if V is None or len(V)<2: continue
    n+=1
    m=min(tot_inv(o) for o in V)
    if sum(1 for o in V if tot_inv(o)==m)==1: uniq+=1
print("\n     instances with ≥2 valid orders : %d"%n)
print("     with a UNIQUE minimum-inversion order : %d  (%.0f%%)"%(uniq,100*uniq/max(n,1)))