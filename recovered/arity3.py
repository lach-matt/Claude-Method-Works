import random
from itertools import product, permutations, combinations
random.seed(661)
print("="*88)
print("  ARITY 3 REDUCES TO 2-SAT ON XOR VARIABLES")
print("="*88)
print("""
  A constraint on {a,b,c} invariant under (a,b,c) -> (¬a,¬b,¬c) depends only
  on (a⊕b, b⊕c). **So an arity-3 complement-closed constraint is a BINARY
  constraint on two XOR variables** — and with t_ij = s_i ⊕ s_j the triangle
  relations are automatic.

     |A| = 2  ->  both XORs determined  ->  two equalities
     |A| = 4  ->  one relation between them
     |A| = 6  ->  one forbidden pair    ->  a 2-CLAUSE

  **Binary constraints on booleans are 2-SAT — linear time.** So if d = 3 has
  no arity ≥ 4, the whole system is 2-SAT.
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
def constraints(S,d):
    A=alph(S,d); Ss=set(S); out=[]
    for x,y in combinations(sorted(S),2):
        I=[i for i in range(d) if x[i]!=y[i]]
        if not I: continue
        V=[(i,tuple(sorted((x[i],y[i])))) for i in I]
        ok=set()
        for bits in product([0,1],repeat=len(I)):
            j=list(x); m=list(x)
            for t,i in enumerate(I):
                u,v=sorted((x[i],y[i]))
                j[i]= v if bits[t]==0 else u
                m[i]= u if bits[t]==0 else v
            if tuple(j) in Ss and tuple(m) in Ss: ok.add(bits)
        if len(ok)<2**len(I): out.append((tuple(V),ok))
    return out
def twosat(clauses,var):
    V=sorted(var); ix={v:i for i,v in enumerate(V)}; n=len(V)
    if n==0: return True
    g=[[] for _ in range(2*n)]; gr=[[] for _ in range(2*n)]
    lit=lambda v,s: 2*ix[v]+(0 if s else 1); neg=lambda l: l^1
    for (a,sa),(b,sb) in clauses:
        la,lb=lit(a,sa),lit(b,sb)
        g[neg(la)].append(lb); g[neg(lb)].append(la)
        gr[lb].append(neg(la)); gr[la].append(neg(lb))
    vis=[False]*(2*n); order=[]
    for s in range(2*n):
        if vis[s]: continue
        st=[(s,0)]; vis[s]=True
        while st:
            u,i=st.pop()
            if i<len(g[u]):
                st.append((u,i+1)); w=g[u][i]
                if not vis[w]: vis[w]=True; st.append((w,0))
            else: order.append(u)
    comp=[-1]*(2*n); c=0
    for u in reversed(order):
        if comp[u]!=-1: continue
        st=[u]; comp[u]=c
        while st:
            x=st.pop()
            for w in gr[x]:
                if comp[w]==-1: comp[w]=c; st.append(w)
        c+=1
    return all(comp[2*i]!=comp[2*i+1] for i in range(n))
def decide(S,d):
    """variables = orientations; encode arity-2 and arity-3 as 2-SAT clauses"""
    cons=constraints(S,d)
    var=set(); cl=[]
    for V,A2 in cons:
        for v in V: var.add(v)
        if not A2: return False
        k=len(V)
        if k>3: return None
        # forbid every assignment NOT in A2 ; each forbidden assignment on k
        # variables is a k-clause.  k<=2 gives 2-clauses directly.
        # for k=3, complement-closure means forbidden assignments come in
        # antipodal pairs, and the pair is expressible as a 2-clause on XORs
        if k==1:
            b=list(A2)[0][0]; cl.append(((V[0],b==1),(V[0],b==1)))
        elif k==2:
            for bits in product([0,1],repeat=2):
                if bits not in A2:
                    cl.append(((V[0],bits[0]==0),(V[1],bits[1]==0)))
        else:
            # k=3 : express via XOR pairs.  t1 = v0⊕v1, t2 = v1⊕v2
            # A2 is complement-closed so it is a set of (t1,t2) values
            T=set()
            for bits in A2: T.add((bits[0]^bits[1], bits[1]^bits[2]))
            for t in product([0,1],repeat=2):
                if t not in T:
                    # forbid t1=t[0] and t2=t[1] -> a 2-clause on XOR vars
                    cl.append((('X',V[0],V[1],t[0]==0),('X',V[1],V[2],t[1]==0)))
                    var.add(('X',V[0],V[1])); var.add(('X',V[1],V[2]))
    # rebuild variable list: raw orientations and XOR aliases
    vv=set()
    for (a,sa),(b,sb) in cl:
        vv.add(a if not (isinstance(a,tuple) and a and a[0]=='X') else a[:3])
        vv.add(b if not (isinstance(b,tuple) and b and b[0]=='X') else b[:3])
    cl2=[]
    for (a,sa),(b,sb) in cl:
        A_=a[:3] if (isinstance(a,tuple) and a and a[0]=='X') else a
        B_=b[:3] if (isinstance(b,tuple) and b and b[0]=='X') else b
        cl2.append(((A_,sa),(B_,sb)))
    return twosat(cl2,vv)
print("="*88)
print("  TEST — DOES 2-SAT DECIDE d = 3?")
print("="*88)
print("\n  %6s%6s%12s%14s%12s%12s"%("d","|A|","instances","2SAT==brute","false pos","false neg"))
print("  "+"-"*64)
for d,a in [(3,2),(3,3),(2,4),(4,2)]:
    n=ag=fp=fn=0
    for _ in range(400):
        cells=list(product(*[range(a)]*d))
        S=set(random.sample(cells,random.randint(4,min(len(cells),10))))
        if any(len({x[k] for x in S})<2 for k in range(d)): continue
        b=reord(S,d); c=decide(S,d)
        if c is None: continue
        n+=1; ag+= (b==c)
        if c and not b: fp+=1
        if b and not c: fn+=1
    if n: print("  %6d%6d%12d%14d%12d%12d"%(d,a,n,ag,fp,fn))