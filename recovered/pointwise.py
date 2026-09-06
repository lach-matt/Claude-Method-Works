import numpy as np, random
from itertools import product, permutations, combinations
random.seed(251)
print("="*88)
print("  THE POINTWISE CONSTRUCTION")
print("="*88)
print("""
  Each containment B ⊂ A forces a PRECEDENCE PATTERN on columns:

     s(A,B) = LEFT   ->  every b ∈ B precedes every a ∈ A\\B
     s(A,B) = RIGHT  ->  every a ∈ A\\B precedes every b ∈ B

  **Two containments conflict if their choices force x<y and y<x on the
  same pair of columns.** That is a 2-clause, and it is derived from EVERY
  pair of containments — not container by container.

  **Plus the chain clauses, and the sibling clauses.** All of them, at
  every point, intersected.
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def twosat(cl,nv):
    if nv==0: return True
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
def pointwise(S):
    rows=sorted(set(sup_of(S).values()),key=lambda s:(-len(s),sorted(s)))
    CT=[(A,B) for A in rows for B in rows if B<A]
    if not CT: return True
    idx={p:i for i,p in enumerate(CT)}; nv=len(CT)
    def prec(A,B,left):
        """set of ordered column pairs (x,y) meaning x precedes y"""
        out=B; rest=A-B
        return {(b,a) for b in out for a in rest} if left else {(a,b) for b in out for a in rest}
    P={}
    for (A,B) in CT:
        P[(A,B,True)]=prec(A,B,True); P[(A,B,False)]=prec(A,B,False)
    cl=[]
    # 1. every pair of containment choices that conflict pointwise
    for i,(A,B) in enumerate(CT):
        for j,(A2,B2) in enumerate(CT):
            if j<=i: continue
            for s1 in (True,False):
                for s2 in (True,False):
                    p1=P[(A,B,s1)]; p2=P[(A2,B2,s2)]
                    if any((y,x) in p2 for (x,y) in p1):
                        cl.append(((idx[(A,B)],not s1),(idx[(A2,B2)],not s2)))
    # 2. self-consistency: a single choice must not contradict itself
    for (A,B) in CT:
        for s in (True,False):
            p=P[(A,B,s)]
            if any((y,x) in p for (x,y) in p):
                cl.append(((idx[(A,B)],not s),(idx[(A,B)],not s)))
    # 3. chain clauses  C ⊂ B ⊂ A
    for A in rows:
        ins=[X for X in rows if X<A]
        for B in ins:
            for C in ins:
                if C<B:
                    ac=idx[(A,C)]; ab=idx[(A,B)]; bc=idx[(B,C)]
                    cl.append(((ac,False),(ab,True)));  cl.append(((ac,False),(bc,True)))
                    cl.append(((ac,True),(ab,False)));  cl.append(((ac,True),(bc,False)))
    # 4. siblings inside a common container cannot share an end
    for A in rows:
        ins=[X for X in rows if X<A]
        for B,C in combinations(ins,2):
            if not (B<C or C<B):
                cl.append(((idx[(A,B)],True),(idx[(A,C)],True)))
                cl.append(((idx[(A,B)],False),(idx[(A,C)],False)))
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
        a=reorderable(S); b=c1p(S) and pointwise(S)
        ag+=(a==b)
        if b and not a: fp+=1; ex.append(('FP',sorted(S)))
        if a and not b: fn+=1; ex.append(('FN',sorted(S)))
    TFP+=fp; TFN+=fn
    print("  %12s%9d%9d%12d%12d"%(lab,n,ag,fp,fn))
    for k,s in ex[:2]: print("        %s %s"%(k,str(s)[:56]))
print("="*88)
if TFP==0 and TFN==0:
    print("""  **EXACT — %d instances, zero errors either way.**

     X is 𝓡-reorderable  ⟺  X is C1P and the pointwise containment 2-SAT
                             is satisfiable

     C1P        linear    (Booth & Lueker 1976)
     clauses    O(r⁴ c²)  every pair of containments, every column pair
     2-SAT      linear in the clauses
     **TOTAL    POLYNOMIAL**
"""%(2000))
else:
    print("  **NOT EXACT — %d FP, %d FN.**"%(TFP,TFN))