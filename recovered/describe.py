import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(503)
print("="*88)
print("  DESCRIBING THE COMPONENT DECOMPOSITION, MANY WAYS")
print("="*88)
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
def valid(S,d,cap=200000):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    return [tuple(ps) for ps in product(*[list(permutations(a)) for a in A])
            if lat(relab(S,[list(p) for p in ps],d),d)]
def nbrs(o):
    out=[]
    for i in range(len(o)):
        p=list(o[i])
        for t in range(len(p)-1):
            q=list(p); q[t],q[t+1]=q[t+1],q[t]
            oo=list(o); oo[i]=tuple(q); out.append(tuple(oo))
    return out
def components(V):
    VS=set(V); seen=set(); comps=[]
    for v in V:
        if v in seen: continue
        st=[v]; seen.add(v); c=[]
        while st:
            u=st.pop(); c.append(u)
            for w in nbrs(u):
                if w in VS and w not in seen: seen.add(w); st.append(w)
        comps.append(c)
    return comps
print("="*88)
print("  DESCRIPTION 1 — components vs the DUAL involution")
print("="*88)
print("""
  Reversing EVERY axis maps a sublattice to a sublattice (the dual rule,
  measured 100%). **So the dual is a bijection of the valid set.** Does it
  map each component to a different one?
""")
def dual(o): return tuple(tuple(reversed(p)) for p in o)
n=fix=swap=0
for _ in range(400):
    d=random.choice([2,3]); a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(2,len(cl))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    V=valid(S,d)
    if not V or len(V)<2: continue
    C=components(V); idx={}
    for i,c in enumerate(C):
        for o in c: idx[o]=i
    n+=1
    same=sum(1 for o in V if dual(o) in idx and idx[dual(o)]==idx[o])
    if same==len(V): fix+=1
    elif same==0: swap+=1
print("     instances : %d      dual fixes every component : %d      swaps all : %d"%(n,fix,swap))
print("="*88)
print("  DESCRIPTION 2 — components vs PQ-tree Q-NODES  (d = 2)")
print("="*88)
print("""
  **Each Q-node has exactly two orientations.** If the components are indexed
  by the Q-node orientations, then #components = 2^(#Q-nodes) — a computable
  prediction.
""")
def overlap(p,q): return bool(p&q) and not(p<=q) and not(q<=p)
def n_qnodes(S):
    A=alph(S,2)
    rows=list({frozenset(c for (r,c) in S if r==rr) for rr in A[0]})
    par=list(range(len(rows)))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for i in range(len(rows)):
        for j in range(i+1,len(rows)):
            if overlap(rows[i],rows[j]):
                u,v=f(i),f(j)
                if u!=v: par[u]=v
    g={}
    for i in range(len(rows)): g.setdefault(f(i),[]).append(i)
    return sum(1 for v in g.values() if len(v)>1)
print("\n  %10s%12s%16s%16s%12s"%("instances","mean comps","mean Q-nodes","2^Q predicted","match"))
print("  "+"-"*68)
n=0; cm=[]; qm=[]; hit=0
for _ in range(500):
    a=random.choice([3,4])
    cl=list(product(range(a),range(a)))
    S=set(random.sample(cl,random.randint(2,len(cl))))
    A=alph(S,2)
    if any(len(x)<2 for x in A): continue
    V=valid(S,2)
    if not V or len(V)<2: continue
    C=components(V); q=n_qnodes(S)
    n+=1; cm.append(len(C)); qm.append(q)
    hit+= (len(C)==2**q)
print("  %10d%12.2f%16.2f%16.2f%11d%%"%(n,np.mean(cm),np.mean(qm),np.mean([2**x for x in qm]),int(100*hit/max(n,1))))
print("="*88)
print("  DESCRIPTION 3 — is each component a COSET?")
print("="*88)
print("""
  If each component is a coset of a subgroup of ∏S_{|A_i|}, then it is
  closed under a group action — **and the group is the object.** Test whether
  component sizes divide the total, and whether they are all equal.
""")
n=eq=div=0
for _ in range(400):
    d=random.choice([2,3]); a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(2,len(cl))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    V=valid(S,d)
    if not V or len(V)<2: continue
    C=components(V); szs=[len(c) for c in C]
    tot=int(np.prod([math.factorial(len(x)) for x in A]))
    n+=1
    eq+= (len(set(szs))==1)
    div+= all(tot%s==0 for s in szs)
print("     instances %d    all components EQUAL size : %d  (%.0f%%)    sizes divide the total : %d  (%.0f%%)"
      %(n,eq,100*eq/max(n,1),div,100*div/max(n,1)))
print("="*88)
print("  DESCRIPTION 4 — what invariant is CONSTANT on a component?")
print("="*88)
print("""
  A component is a class. **Find a function of the order that is constant
  within a component and differs between them** — that function is the
  component label, and labels are what a decomposition needs.
""")
def label_candidates(S,d,o):
    T=relab(S,o,d)
    A=[sorted({t[i] for t in T}) for i in range(d)]
    return dict(
      rank_of_top=sum(max(t[i] for t in T) for i in range(d)),
      n_minimal=sum(1 for x in T if not any(all(y[i]<=x[i] for i in range(d)) and y!=x for y in T)),
      n_joinirr=sum(1 for x in T if sum(1 for y in T if all(y[i]<=x[i] for i in range(d)) and y!=x
                                        and not any(all(y[i]<=z[i] for i in range(d)) and z!=y and z!=x
                                                    and all(z[i]<=x[i] for i in range(d)) for z in T))<=1),
      height=max(sum(t) for t in T)-min(sum(t) for t in T),
    )
KEYS=['rank_of_top','n_minimal','n_joinirr','height']
stat={k:[0,0] for k in KEYS}
for _ in range(250):
    d=random.choice([2,3]); a=random.choice([2,3])
    Ax=[list(range(a)) for _ in range(d)]
    cl=list(product(*Ax))
    S=set(random.sample(cl,random.randint(2,len(cl))))
    A=alph(S,d)
    if any(len(x)<2 for x in A): continue
    V=valid(S,d)
    if not V or len(V)<2: continue
    C=components(V)
    if len(C)<2: continue
    for k in KEYS:
        within=all(len({label_candidates(S,d,o)[k] for o in c})==1 for c in C)
        between=len({label_candidates(S,d,c[0])[k] for c in C})==len(C)
        stat[k][0]+= within; stat[k][1]+= (within and between)
print("\n  %-16s%18s%20s"%("candidate label","constant within","and separates"))
print("  "+"-"*56)
for k in KEYS: print("  %-16s%18d%20d"%(k,stat[k][0],stat[k][1]))