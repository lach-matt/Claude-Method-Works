import numpy as np, random, itertools
from itertools import product, permutations
from math import factorial
random.seed(197)
print("="*88)
print("  THE PATH THE BOUND IDENTIFIES")
print("="*88)
print("""
  **No backtrack-free method can succeed.** So the path goes through
  backtracking, and the only question left is whether its DEPTH grows
  polynomially with the instance.

     depth bounded by a polynomial  ->  the decision is in P
     depth growing faster           ->  it is not, by this route

  §23.2 measured depths 0, 2, 2, 7, 3 at d = 3…7 for the axis heuristic.
  **Measure it for the tree traversal.**
""")
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
def c1p_orders(cols,rows,cap=3000):
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
def frontiers(node,cap=400000):
    if node.t=='L': return [tuple(node.leaves)]
    if node.t=='Q': return [tuple(o) for o in (node.orders or [])][:cap]
    kid=[frontiers(k,cap) for k in node.kids]
    out=[]
    for perm in permutations(range(len(kid))):
        for combo in product(*[kid[i] for i in perm]):
            out.append(tuple(itertools.chain(*combo)))
            if len(out)>=cap: return out
    return out
def nostrict(sp): return not any(a<c and d<b for (a,b) in sp for (c,d) in sp)
def decide_with_depth(S):
    """exact search over frontiers; returns (answer, frontiers tried)"""
    A=alpha(S); sup={r:frozenset(c for (a,c) in S if a==r) for r in A[0]}
    root=build(set(A[1]),list(sup.values()))
    tried=0
    for f in frontiers(root):
        tried+=1
        ic={v:i for i,v in enumerate(f)}
        sp=[]; ok=True
        for r in A[0]:
            s=sorted(ic[c] for c in sup[r])
            if s!=list(range(s[0],s[0]+len(s))): ok=False; break
            sp.append((s[0],s[-1]))
        if ok and nostrict(sp): return True,tried
    return False,tried
def soln_count(S):
    A=alpha(S); c=0
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Rclosed(relabel(S,[list(p0),list(p1)])): c+=1
    return c
print("="*88)
print("  HOW MANY FRONTIERS MUST BE TRIED BEFORE ONE SUCCEEDS?")
print("="*88)
buck={(0.0,0.05):[],(0.05,0.2):[],(0.2,0.5):[],(0.5,1.01):[]}
for _ in range(1800):
    A=[list(range(random.randint(2,4))),list(range(random.randint(2,4)))]
    cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
    Aa=alpha(S)
    if len(Aa[0])<2 or len(Aa[1])<2: continue
    sc=soln_count(S)
    if sc==0: continue
    d=sc/(factorial(len(Aa[0]))*factorial(len(Aa[1])))
    ok,t=decide_with_depth(S)
    if not ok: continue
    for k in buck:
        if k[0]<=d<k[1]: buck[k].append(t); break
print("\n  %14s%10s%14s%12s"%("density","n","median tries","max"))
print("  "+"-"*52)
for k in sorted(buck):
    v=buck[k]
    if v: print("  %14s%10d%14d%12d"%("%.2f-%.2f"%k,len(v),int(np.median(v)),max(v)))
print("="*88)
print("  AND DOES IT GROW WITH INSTANCE SIZE?")
print("="*88)
print("\n  %10s%10s%16s%12s%14s"%("alphabet","n","median tries","max","|frontiers|"))
print("  "+"-"*62)
for sz in (3,4,5,6):
    tr=[]; fr=[]
    for _ in range(300):
        A=[list(range(sz)),list(range(sz))]
        cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        Aa=alpha(S)
        if len(Aa[0])<2 or len(Aa[1])<2: continue
        ok,t=decide_with_depth(S)
        if ok:
            tr.append(t)
            fr.append(len(frontiers(build(set(Aa[1]),[frozenset(c for (a,c) in S if a==r) for r in Aa[0]]))))
    if tr: print("  %10d%10d%16d%12d%14d"%(sz,len(tr),int(np.median(tr)),max(tr),int(np.median(fr))))
print("""
{0}
  WHAT THIS SAYS
{0}
""".format("="*88))
print("""  **The number of frontiers tried before success is the backtracking
  depth, measured on the tree.** If it stays small while the frontier count
  explodes, the search is guided rather than exhaustive — and a polynomial
  bound is plausible. If it tracks the frontier count, it is not.
""")