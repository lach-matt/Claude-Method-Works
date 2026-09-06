import numpy as np, random
from itertools import product, permutations, combinations
random.seed(239)
print("="*88)
print("  THE STRUCTURAL SOLUTION — NO TREE")
print("="*88)
print("""
  A path in the PQ-tree from A down to B **is** a containment chain
  A ⊃ … ⊃ B in the row poset, and containment is order-independent. **So
  build the 2-SAT on the poset directly.**

  Variable  side(A,B) for each strict containment B ⊂ A
            TRUE = B sits at A's LEFT end, FALSE = at its RIGHT end

  Clauses
     B, C ⊂ A and NOT nested  ->  they cannot share an end
                                  (side(A,B) ∨ side(A,C)) ∧ (¬ ∨ ¬)
     C ⊂ B ⊂ A                ->  side(A,C) → side(A,B), side(A,C) → side(B,C)
                                  and the same for the negations

  **All two-literal. And the second family is what the node tests were
  missing** — it is the chain, which no projection sees.
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def twosat(cl,nv):
    g=[[] for _ in range(2*nv)]; gr=[[] for _ in range(2*nv)]
    lit=lambda v,s: 2*v+(0 if s else 1); neg=lambda l: l^1
    for (a,sa),(b,sb) in cl:
        la,lb=lit(a,sa),lit(b,sb)
        g[neg(la)].append(lb); g[neg(lb)].append(la)
        gr[lb].append(neg(la)); gr[la].append(neg(lb))
    vis=[False]*(2*nv); order=[]
    for s in range(2*nv):
        if vis[s]: continue
        st=[(s,0)]; vis[s]=True
        while st:
            u,i=st.pop()
            if i<len(g[u]):
                st.append((u,i+1)); w=g[u][i]
                if not vis[w]: vis[w]=True; st.append((w,0))
            else: order.append(u)
    comp=[-1]*(2*nv); c=0
    for u in reversed(order):
        if comp[u]!=-1: continue
        st=[u]; comp[u]=c
        while st:
            x=st.pop()
            for w in gr[x]:
                if comp[w]==-1: comp[w]=c; st.append(w)
        c+=1
    return all(comp[2*i]!=comp[2*i+1] for i in range(nv))
def poset_2sat(S):
    rows=sorted(set(sup_of(S).values()),key=lambda s:(-len(s),sorted(s)))
    var={}; nv=0
    def V(k):
        nonlocal nv
        if k not in var: var[k]=nv; nv+=1
        return var[k]
    cl=[]
    cont=[(A,B) for A in rows for B in rows if B<A]
    for A,B in cont: V((A,B))
    for A in rows:
        ins=[B for B in rows if B<A]
        for B,C in combinations(ins,2):
            if not (B<C or C<B):
                a=V((A,B)); b=V((A,C))
                cl.append(((a,True),(b,True)))
                cl.append(((a,False),(b,False)))
        for B in ins:
            for C in ins:
                if C<B:
                    ac=V((A,C)); ab=V((A,B)); bc=V((B,C))
                    cl.append(((ac,False),(ab,True)))
                    cl.append(((ac,False),(bc,True)))
                    cl.append(((ac,True),(ab,False)))
                    cl.append(((ac,True),(bc,False)))
    if nv==0: return True
    return twosat(cl,nv)
def c1p(S):
    A=alpha(S); sup=sup_of(S)
    for p in permutations(A[1]):
        ic={v:i for i,v in enumerate(p)}
        ok=True
        for r in A[0]:
            s=sorted(ic[c] for c in sup[r])
            if s!=list(range(s[0],s[0]+len(s))): ok=False; break
        if ok: return True
    return False
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Rclosed(S):
    A=alpha(S)
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in S if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    NN={};run=-1
    for w in A[1]:
        c=[x for (x,y) in S if y<=w]; run=max(run,max(c) if c else -1); NN[w]=run
    return {(r,c) for r in A[0] for c in A[1] if c<=M[r] and r<=NN[c]}==S
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Rclosed(relabel(S,[list(p0),list(p1)])): return True
    return False
def gen_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
print("  %12s%9s%9s%12s%12s"%("source","n","agree","false pos","false neg"))
print("  "+"-"*54)
TFP=TFN=0
for lab in ("random","nested"):
    n=ag=fp=fn=0; ex=[]
    for _ in range(2000):
        if lab=="random":
            A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        else:
            S=gen_nested(random.randint(3,5))
        Aa=alpha(S)
        if len(Aa[0])<2 or len(Aa[1])<2: continue
        n+=1
        a=reorderable(S); b=c1p(S) and poset_2sat(S)
        ag+=(a==b)
        if b and not a: fp+=1; ex.append(('FP',sorted(S)))
        if a and not b: fn+=1; ex.append(('FN',sorted(S)))
    TFP+=fp; TFN+=fn
    print("  %12s%9d%9d%12d%12d"%(lab,n,ag,fp,fn))
    for k,s in ex[:2]: print("        %s %s"%(k,str(s)[:56]))
print("="*88)
if TFP==0 and TFN==0:
    print("""  **EXACT.**

     X is 𝓡-reorderable  ⟺  X is C1P, and the containment 2-SAT is
     satisfiable.

     C1P            linear     (Booth & Lueker 1976)
     containments   O(r² c)
     2-SAT          linear in the clauses, O(r³)
     **TOTAL        O(r³ + rc)  — POLYNOMIAL**

  **No tree, no traversal, no search.** The chain clauses are what every
  node-local test omitted, and §13.4 says why: a chain is not a projection.
""")
else:
    print("  **NOT EXACT — %d FP, %d FN.**"%(TFP,TFN))