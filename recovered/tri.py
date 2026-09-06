import numpy as np, random
from itertools import product, permutations, combinations
random.seed(151)
print("="*88)
print("  THREE TWO-VALUED CONSTRAINTS, USED TOGETHER")
print("="*88)
print("""
     1. C1P            — each row's columns consecutive       (yes / no)
     2. two-sided      — c ≤ M*(r) AND r ≤ N*(c)              (both / not)
     3. end assignment — each contained row at LEFT or RIGHT  (L / R)

  **The third is a boolean per (contained row, container) pair, and the
  constraints between them are pairwise.** Build the 2-SAT instance.
""")
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S):
    return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Rclosed(S):
    A=alpha(S)
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in S if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N={};run=-1
    for w in A[1]:
        c=[x for (x,y) in S if y<=w]; run=max(run,max(c) if c else -1); N[w]=run
    return {(r,c) for r in A[0] for c in A[1] if c<=M[r] and r<=N[c]}==S
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Rclosed(relabel(S,[list(p0),list(p1)])): return True
    return False
def c1p_spans(S,pc):
    ic={v:i for i,v in enumerate(pc)}
    sp={}
    for r in alpha(S)[0]:
        s=sorted(ic[c] for (a,c) in S if a==r)
        if not s or s!=list(range(s[0],s[0]+len(s))): return None
        sp[r]=(s[0],s[-1])
    return sp
def anyc1p(S):
    return any(c1p_spans(S,pc) is not None for pc in permutations(alpha(S)[1]))
def twosat(clauses,varset):
    """standard implication-graph 2-SAT"""
    V=sorted(varset); idx={v:i for i,v in enumerate(V)}; n=len(V)
    g=[[] for _ in range(2*n)]; gr=[[] for _ in range(2*n)]
    lit=lambda v,s: 2*idx[v]+(0 if s else 1)
    neg=lambda l: l^1
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
                st.append((u,i+1))
                w=g[u][i]
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
def endsat(S):
    """2-SAT over 'B sits at the LEFT end of A' for each strict containment"""
    A=alpha(S); sup=sup_of(S)
    pairs=[(b,a) for a in A[0] for b in A[0] if b!=a and sup[b]<sup[a]]
    if not pairs: return True
    varset={p for p in pairs}
    cl=[]
    for a in A[0]:
        ins=[b for b in A[0] if b!=a and sup[b]<sup[a]]
        for b,c in combinations(ins,2):
            inc = not (sup[b]<=sup[c] or sup[c]<=sup[b])
            if inc:
                # incomparable rows inside a cannot share an end
                cl.append((((b,a),True),((c,a),True)))     # not both LEFT
                cl.append((((b,a),False),((c,a),False)))   # not both RIGHT
    return twosat(cl,varset)
def criterion(S):
    return anyc1p(S) and endsat(S)
print("  %10s%10s%12s%12s%12s"%("alphabets","C1P n","agree","false pos","false neg"))
print("  "+"-"*58)
for lo,hi in [(2,4),(2,5),(3,5)]:
    n=ag=fp=fn=0; ex=[]
    for _ in range(2500):
        A=[list(range(random.randint(lo,hi))),list(range(random.randint(lo,hi)))]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(1,len(cells))))
        if not anyc1p(S): continue
        n+=1
        a=reorderable(S); b=criterion(S)
        ag+=(a==b)
        if b and not a: fp+=1; ex.append(('FP',sorted(S)))
        if a and not b: fn+=1; ex.append(('FN',sorted(S)))
    print("  %10s%10d%12d%12d%12d"%("%d-%d"%(lo,hi),n,ag,fp,fn))
    for k,s in ex[:2]: print("        %s %s"%(k,str(s)[:66]))
print("="*88)
print("  AND ON THE DELIBERATELY NESTED INSTANCES")
print("="*88)
def build_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
n=ag=fp=fn=0; ex=[]
for _ in range(2000):
    S=build_nested(random.randint(3,5))
    A=alpha(S)
    if len(A[0])<2 or len(A[1])<2 or not anyc1p(S): continue
    n+=1
    a=reorderable(S); b=criterion(S)
    ag+=(a==b)
    if b and not a: fp+=1; ex.append(('FP',sorted(S)))
    if a and not b: fn+=1; ex.append(('FN',sorted(S)))
print("\n     nested-by-construction : %d   agree %d   FP %d   FN %d"%(n,ag,fp,fn))
for k,s in ex[:3]: print("       %s %s"%(k,str(s)[:66]))