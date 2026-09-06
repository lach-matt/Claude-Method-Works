import random, math
from itertools import product, permutations, combinations
random.seed(659)
print("="*88)
print("  ITEM TWO — GENERAL ALPHABETS")
print("="*88)
print("""
  At |A_i| = k a relabelling is a permutation, not a flip. **But the join at
  axis i between two cells with values u,v depends only on WHICH of u,v comes
  first.** So the decision variables are

     o(i,{u,v}) ∈ {0,1}   for each axis i and unordered pair of values

  **Σ C(|A_i|,2) booleans** — 29 for Λ — plus TRANSITIVITY per axis, which the
  binary case does not need.

  **And reversing every orientation in a constraint swaps join and meet**, so
  the constraints are still complement-closed. Verify both.
""")
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def sublat(S,d):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
def reord(S,d):
    A=alph(S,d)
    for ps in product(*[list(permutations(a)) for a in A]):
        if sublat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def cons_general(S,d):
    """constraints on orientation variables o(i,{u,v})"""
    A=alph(S,d); Ss=set(S); out=[]
    for x,y in combinations(sorted(S),2):
        I=[i for i in range(d) if x[i]!=y[i]]
        if not I: continue
        vars_=[(i,tuple(sorted((x[i],y[i])))) for i in I]
        ok=set()
        for bits in product([0,1],repeat=len(I)):
            j=list(x); m=list(x)
            for t,i in enumerate(I):
                u,v=sorted((x[i],y[i]))
                hi = v if bits[t]==0 else u      # bits=0 -> u<v so max is v
                lo = u if bits[t]==0 else v
                j[i]=hi; m[i]=lo
            if tuple(j) in Ss and tuple(m) in Ss: ok.add(bits)
        if len(ok)<2**len(I): out.append((tuple(vars_),ok))
    return out
print("="*88)
print("  TEST 1 — COMPLEMENT-CLOSURE AT GENERAL ALPHABETS")
print("="*88)
n=cc=0
for _ in range(400):
    d=random.choice([2,3]); a=random.choice([3,4])
    cells=list(product(*[range(a)]*d))
    S=set(random.sample(cells,random.randint(3,min(len(cells),9))))
    for V,A2 in cons_general(S,d):
        if not A2: continue
        n+=1
        comp={tuple(1-b for b in bits) for bits in A2}
        cc+= (comp==A2)
print("\n     constraints : %d      complement-closed : %d  (%.1f%%)"%(n,cc,100*cc/max(n,1)))
print("="*88)
print("  TEST 2 — VARIABLE COUNT, AND ARITY")
print("="*88)
from collections import Counter
print("\n  %6s%6s%12s%14s%12s%12s"%("d","|A|","variables","constraints","arity 2","arity ≥3"))
print("  "+"-"*64)
for d,a in [(2,3),(2,4),(3,3),(3,2),(2,5)]:
    nv=d*math.comb(a,2); ar=Counter(); tot=0
    for _ in range(120):
        cells=list(product(*[range(a)]*d))
        S=set(random.sample(cells,random.randint(4,min(len(cells),10))))
        for V,A2 in cons_general(S,d):
            ar[min(len(V),3)]+=1; tot+=1
    if tot: print("  %6d%6d%12d%14d%12.3f%12.3f"%(d,a,nv,tot,ar[2]/tot,ar[3]/tot))
print("="*88)
print("  TEST 3 — DOES 2-COLOURING PLUS TRANSITIVITY DECIDE?")
print("="*88)
def decide(S,d):
    """arity-2 constraints as a signed graph on orientation variables,
       plus transitivity within each axis"""
    A=alph(S,d); cons=cons_general(S,d)
    edges=[]; forced={}
    for V,A2 in cons:
        if len(V)!=2: continue
        if not A2: return False
        if A2=={(0,0),(1,1)}: edges.append((V[0],V[1],0))
        elif A2=={(0,1),(1,0)}: edges.append((V[0],V[1],1))
        else: return None
    import collections
    adj=collections.defaultdict(list)
    for u,v,p in edges: adj[u].append((v,p)); adj[v].append((u,p))
    col={}
    for st in list(adj):
        if st in col: continue
        col[st]=0; stack=[st]
        while stack:
            u=stack.pop()
            for v,p in adj[u]:
                w=col[u]^p
                if v in col:
                    if col[v]!=w: return False
                else: col[v]=w; stack.append(v)
    # transitivity per axis: the coloured orientations must extend to a total order
    for i in range(d):
        vals=A[i]
        rel={}
        for (ax,pr),cv in col.items():
            if ax!=i: continue
            u,v=pr
            rel[(u,v)] = (u,v) if cv==0 else (v,u)
        # check acyclicity of the forced relation
        import collections as C2
        g=C2.defaultdict(list)
        for a2,b2 in rel.values(): g[a2].append(b2)
        WH={}
        def cyc(u):
            WH[u]=1
            for w in g[u]:
                if WH.get(w)==1: return True
                if WH.get(w) is None and cyc(w): return True
            WH[u]=2; return False
        for u in list(g):
            if WH.get(u) is None and cyc(u): return False
    return True
print("\n  %6s%6s%12s%14s%12s%12s"%("d","|A|","instances","2col==brute","false pos","false neg"))
print("  "+"-"*64)
for d,a in [(2,3),(2,4),(3,2),(3,3)]:
    n=ag=fp=fn=0
    for _ in range(300):
        cells=list(product(*[range(a)]*d))
        S=set(random.sample(cells,random.randint(4,min(len(cells),10))))
        if any(len({x[k] for x in S})<2 for k in range(d)): continue
        b=reord(S,d); c=decide(S,d)
        if c is None: continue
        n+=1; ag+= (b==c)
        if c and not b: fp+=1
        if b and not c: fn+=1
    if n: print("  %6d%6d%12d%14d%12d%12d"%(d,a,n,ag,fp,fn))