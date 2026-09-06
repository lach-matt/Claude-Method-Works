import numpy as np, random, itertools
from itertools import product, permutations
random.seed(191)
print("="*88)
print("  WHAT THE THREE ERRORS TRIANGULATE")
print("="*88)
print("""
  **False negatives** — the traversal rejects arrangements that exist. Its
  row-touching test is too strict: a row may span a PREFIX of children, not
  just the first one.

  **False positives** — it accepts rows as 'touching an end' without
  checking that the child can actually expose them there. The test is not
  recursive.

  **Both errors in both attempts ⟹ the state is wrong, not the code.**
  A boolean 'can offer an end' is insufficient. **The state must be WHICH
  ROWS can touch each end**, and those form chains.

     solve(v)  ->  set of achievable pairs (L, R)
                   L = rows touching v's left end, R = its right end
""")
def overlap(a,b): return bool(a&b) and not (a<=b) and not (b<=a)
def components(sets):
    n=len(sets); par=list(range(n))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    for i in range(n):
        for j in range(i+1,n):
            if overlap(sets[i],sets[j]):
                a,b=f(i),f(j)
                if a!=b: par[a]=b
    g={}
    for i in range(n): g.setdefault(f(i),[]).append(i)
    return list(g.values())
def c1p_orders(cols,rows,cap=2000):
    out=[]
    for p in permutations(sorted(cols)):
        ic={v:i for i,v in enumerate(p)}
        ok=True
        for rw in rows:
            s=sorted(ic[c] for c in rw)
            if s!=list(range(s[0],s[0]+len(s))): ok=False; break
        if ok:
            out.append(p)
            if len(out)>=cap: break
    return out
class Nd:
    __slots__=('t','leaves','kids','orders')
    def __init__(s,t,leaves,kids=None,orders=None):
        s.t=t; s.leaves=frozenset(leaves); s.kids=kids or []; s.orders=orders
def build(cols,rows):
    rows=[r for r in rows if r and r!=frozenset(cols)]
    if not rows: return Nd('P',cols,[Nd('L',{c}) for c in sorted(cols)])
    kids=[]; covered=set()
    for cs in components(rows):
        sub=[rows[i] for i in cs]
        u=frozenset().union(*sub); covered|=set(u)
        if len(sub)==1: kids.append(build(set(u),[r for r in rows if r<u]))
        else: kids.append(Nd('Q',u,orders=c1p_orders(set(u),sub)))
    for c in sorted(set(cols)-covered): kids.append(Nd('L',{c}))
    return Nd('P',cols,kids)
def decide(S,capstates=400):
    A=[sorted({x[i] for x in S}) for i in range(2)]
    sup={r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
    ROWS=sorted(set(sup.values()),key=lambda s:(-len(s),sorted(s)))
    root=build(set(A[1]),list(sup.values()))
    memo={}
    def solve(v):
        """set of achievable (Lrows, Rrows) with no strict nesting inside v"""
        if id(v) in memo: return memo[id(v)]
        ins=[r for r in ROWS if r < v.leaves]
        if v.t=='L':
            memo[id(v)]=frozenset({(frozenset(),frozenset())}); return memo[id(v)]
        cand=[]
        if v.t=='Q':
            for o in (v.orders or []): cand.append([Nd('L',{c}) for c in o])
        else:
            k=len(v.kids)
            if k==1: cand.append(list(v.kids))
            else:
                for i in range(k):
                    for j in range(k):
                        if i==j: continue
                        mid=[v.kids[t] for t in range(k) if t!=i and t!=j]
                        cand.append([v.kids[i]]+mid+[v.kids[j]])
        out=set()
        for seq in cand:
            subs=[solve(k) for k in seq]
            if any(len(s)==0 for s in subs): continue
            # prefix / suffix unions
            pre=[]; acc=frozenset()
            for k in seq: acc|=k.leaves; pre.append(acc)
            suf=[]; acc=frozenset()
            for k in reversed(seq): acc|=k.leaves; suf.append(acc)
            suf=suf[::-1]
            for choice in itertools.islice(itertools.product(*subs),capstates):
                L=set(); R=set(); ok=True
                for r in ins:
                    hitL = any(r==pre[i] for i in range(len(seq))) or (r<=seq[0].leaves and r in choice[0][0]) or r==seq[0].leaves
                    hitR = any(r==suf[i] for i in range(len(seq))) or (r<=seq[-1].leaves and r in choice[-1][1]) or r==seq[-1].leaves
                    if hitL: L.add(r)
                    elif hitR: R.add(r)
                    else: ok=False; break
                if not ok: continue
                Lall=frozenset(L|{v.leaves} if False else L)
                out.add((frozenset(L),frozenset(R)))
                if len(out)>capstates: break
            if len(out)>capstates: break
        memo[id(v)]=frozenset(out)
        return memo[id(v)]
    return len(solve(root))>0
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
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
def build_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
print("  %12s%10s%10s%12s%12s"%("source","n","agree","false pos","false neg"))
print("  "+"-"*56)
for lab in ("random","nested"):
    n=ag=fp=fn=0; ex=[]
    for _ in range(700):
        if lab=="random":
            A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        else:
            S=build_nested(random.randint(3,5))
        A=alpha(S)
        if len(A[0])<2 or len(A[1])<2: continue
        n+=1
        a=reorderable(S)
        try: b=decide(S)
        except Exception: continue
        ag+=(a==b)
        if b and not a: fp+=1; ex.append(('FP',sorted(S)))
        if a and not b: fn+=1; ex.append(('FN',sorted(S)))
    print("  %12s%10d%10d%12d%12d"%(lab,n,ag,fp,fn))
    for k,s in ex[:2]: print("        %s %s"%(k,str(s)[:58]))