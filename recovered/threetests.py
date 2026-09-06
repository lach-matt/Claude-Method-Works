import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(509)
print("="*88)
print("  THREE INDEPENDENT TESTS OF THE COSET READING")
print("="*88)
print("""
  **TEST A (the direct one).** Compute H = {g : g∘o is valid for every valid
  o}. Check it is a subgroup, and whether it is computable from X without
  first finding a valid order.

  **TEST B (independence).** For each valid order o, let H_o = {g : g∘o is
  valid}. **If the valid set is a union of cosets of one subgroup, H_o is the
  same set for every o.** If H_o varies, the equal sizes have another cause.

  **TEST C (automorphism).** X may have symmetries — permutations of values
  that map X to itself. Those map valid orders to valid orders. **If
  Aut(X) accounts for the components, the equal sizes are an ORBIT effect,
  not a coset effect** — a different object with the same signature.

  **Run B and C first: they can refute the coset reading without A.**
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
def valid(S,d,cap=60000):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    return [tuple(ps) for ps in product(*[list(permutations(a)) for a in A])
            if lat(relab(S,[list(p) for p in ps],d),d)]
def compose(g,o):
    """apply g (a tuple of permutations of positions) after o"""
    return tuple(tuple(p[i] for i in gg) for gg,p in zip(g,o))
def group_elems(A):
    return [tuple(ps) for ps in product(*[list(permutations(range(len(a)))) for a in A])]
def nbrs(o):
    out=[]
    for i in range(len(o)):
        p=list(o[i])
        for t in range(len(p)-1):
            q=list(p); q[t],q[t+1]=q[t+1],q[t]
            oo=list(o); oo[i]=tuple(q); out.append(tuple(oo))
    return out
def comps(V):
    VS=set(V); seen=set(); C=[]
    for v in V:
        if v in seen: continue
        st=[v]; seen.add(v); c=[]
        while st:
            u=st.pop(); c.append(u)
            for w in nbrs(u):
                if w in VS and w not in seen: seen.add(w); st.append(w)
        C.append(c)
    return C
print("="*88)
print("  TEST B — IS H_o INDEPENDENT OF o?")
print("="*88)
n=same=0; ex=[]
for _ in range(600):
    d=random.choice([2,3]); a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(2,len(cl))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    V=valid(S,d)
    if not V or len(V)<2: continue
    VS=set(V); G=group_elems(A)
    Hs=[]
    for o in V[:6]:
        Hs.append(frozenset(g for g in G if compose(g,o) in VS))
    n+=1
    if len(set(Hs))==1: same+=1
    elif len(ex)<2: ex.append((sorted(S),[len(h) for h in Hs]))
print("\n     instances : %d      H_o identical for every o : %d  (%.0f%%)"%(n,same,100*same/max(n,1)))
for S,hs in ex: print("        varies: sizes %s   X=%s"%(hs,str(S)[:40]))
print("="*88)
print("  TEST C — DOES Aut(X) EXPLAIN THE COMPONENTS?")
print("="*88)
def aut(S,d,A):
    G=group_elems(A); out=[]
    for g in G:
        T={tuple(g[k].index(x[k]) if False else g[k][x[k]] for k in range(d)) for x in S}
        if T==set(S): out.append(g)
    return out
n=hit=0; rows=[]
for _ in range(500):
    d=random.choice([2,3]); a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(2,len(cl))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    V=valid(S,d)
    if not V or len(V)<2: continue
    C=comps(V); Au=aut(S,d,A)
    n+=1; rows.append((len(C),len(Au),len(V)))
    hit+= (len(C)==len(Au))
print("\n     instances : %d      #components == |Aut(X)| : %d  (%.0f%%)"%(n,hit,100*hit/max(n,1)))
if rows:
    cc=[r[0] for r in rows]; aa=[r[1] for r in rows]; vv=[r[2] for r in rows]
    print("     mean components %.2f    mean |Aut(X)| %.2f    mean |valid| %.2f"%(np.mean(cc),np.mean(aa),np.mean(vv)))
    print("     corr(components, |Aut|) : %+.3f"%np.corrcoef(cc,aa)[0,1])
    print("     |valid| = components × comp-size, so comp-size mean %.2f"%np.mean([v/c for c,_,v in rows]))
print("="*88)
print("  WHAT B AND C SAY BEFORE A IS RUN")
print("="*88)
print("""
  **If B says H_o varies, the valid set is not a union of cosets of ONE
  subgroup** — and the equal component sizes need the orbit explanation
  instead.

  **If C says #components = |Aut(X)|, the components are Aut-orbits** — the
  symmetry of X itself, which is computable from X directly and needs no
  valid order. **That would be the object, and it would be better than a
  coset: Aut(X) is computable from X alone.**
""")