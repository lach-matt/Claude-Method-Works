exec(open('/tmp/pq6.py').read().split('print("="*88)')[0])
import numpy as np, random, itertools
from itertools import product, permutations, combinations
random.seed(283)
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Ev(S,o):
    T=relabel(S,o); A=[sorted({t[i] for t in T}) for i in range(2)]
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in T if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    Nn={};run=-1
    for w in A[1]:
        c=[x for (x,y) in T if y<=w]; run=max(run,max(c) if c else -1); Nn[w]=run
    return sum(1 for r in A[0] for c in A[1] if c<=M[r] and r<=Nn[c])-len(T)
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Ev(S,[list(p0),list(p1)])==0: return True
    return False
print("="*88)
print("  THE BOTTOM-UP TRAVERSAL")
print("="*88)
print("""
  **STATE.** solve(v) returns the achievable pairs (Lset, Rset) — the rows
  in v's subtree that touch v's left and right ends. **Both are chains**, so
  the state is bounded by the depth, not by the frontier count.

  **P-node**: choose leftmost i and rightmost j. Rows strictly inside
  ROW(v) must all lie in child i or child j (and reach the right end of
  it); a middle child holding one is an immediate reject.

  **Q-node**: forward or reversed — i and j are forced.
""")
def traverse(S):
    A=alpha(S); sup=sup_of(S)
    ROWS=set(sup.values())
    root=build(set(A[1]),list(sup.values()))
    if root is None: return False
    memo={}
    def rowof(v): return v.leaves if v.leaves in ROWS else None
    def inside(v):
        rv=rowof(v)
        if rv is None: return frozenset()
        return frozenset(r for r in ROWS if r<rv)
    def solve(v):
        key=id(v)
        if key in memo: return memo[key]
        if v.t=='L' or not v.kids:
            res=frozenset({(frozenset(),frozenset())})
            memo[key]=res; return res
        ks=v.kids; k=len(ks)
        ins=inside(v)
        opts=set()
        if v.t=='Q': arr=[list(range(k)),list(range(k))[::-1]]
        else:
            arr=[]
            if k==1: arr=[[0]]
            else:
                for i in range(k):
                    for j in range(k):
                        if i==j: continue
                        arr.append([i]+[t for t in range(k) if t!=i and t!=j]+[j])
        for seq in arr:
            subs=[solve(ks[t]) for t in seq]
            if any(len(s)==0 for s in subs): continue
            mid_ok=True
            for pos,t in enumerate(seq):
                if pos in (0,len(seq)-1): continue
                if any(r<=ks[t].leaves for r in ins): mid_ok=False; break
            if not mid_ok: continue
            for sl in subs[0]:
                for sr in subs[-1]:
                    Lr=rowof(ks[seq[0]]); Rr=rowof(ks[seq[-1]])
                    Lset=set(sl[0]) | ({Lr} if Lr else set())
                    Rset=set(sr[1]) | ({Rr} if Rr else set())
                    if all(r in Lset or r in Rset for r in ins):
                        myL=set(Lset); myR=set(Rset)
                        rv=rowof(v)
                        if rv: myL.add(rv); myR.add(rv)
                        opts.add((frozenset(myL),frozenset(myR)))
            if len(opts)>200: break
        memo[key]=frozenset(opts)
        return memo[key]
    return len(solve(root))>0
def gen_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
print("  %12s%9s%9s%12s%12s"%("source","n","agree","false pos","false neg"))
print("  "+"-"*54)
TF=0; EX=[]
for lab in ("random","nested"):
    n=ag=fp=fn=0
    for _ in range(1500):
        if lab=="random":
            A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        else:
            S=gen_nested(random.randint(3,5))
        Aa=alpha(S)
        if len(Aa[0])<2 or len(Aa[1])<2: continue
        n+=1
        a=reorderable(S)
        try: b=traverse(S)
        except Exception: continue
        ag+=(a==b)
        if b and not a: fp+=1; EX.append(('FP',sorted(S)))
        if a and not b: fn+=1; EX.append(('FN',sorted(S)))
    TF+=fp+fn
    print("  %12s%9d%9d%12d%12d"%(lab,n,ag,fp,fn))
for k,s in EX[:3]: print("        %s %s"%(k,str(s)[:58]))
print("\n  **%s**"%("EXACT" if TF==0 else "%d errors"%TF))