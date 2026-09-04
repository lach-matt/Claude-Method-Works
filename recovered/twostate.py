import numpy as np, random
from itertools import product, permutations, combinations
random.seed(359)
print("="*86)
print("  THE TWO-STATE DECOMPOSITION")
print("="*86)
print("""
  A constraint graph with cycles = **a spanning tree + the extra edges**.
  Cyclomatic number k = |E| − |V| + 1.

     Λ's DEFINING system  : 7 bounds, 8 variables  ->  k = 0, a TREE
     Λ's RECOVERED system : 16 bounds, 8 variables ->  k = 9

  **So the recovered system is cyclic and recovery works anyway** — because
  its extra bounds are the transitive closure, implied by the tree. **The
  coupling is trivial there. Where it is not implied, it is real.**

  Test: recover on the spanning tree, then CHECK the extra edges.
""")
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def phis(S,d,A):
    ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in S if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return ph
def closed(S,A):
    d=len(A); ph=phis(S,d,A)
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}==S
def binding(S,d,A):
    ph=phis(S,d,A)
    return {(i,j) for i in range(d) for j in range(d) if i!=j
            and any(ph[(i,j)][v]<max(A[i]) for v in A[j])}
def cyclomatic(E,d):
    par=list(range(d))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    tree=[]; extra=[]
    for (i,j) in sorted(E):
        a,b=f(i),f(j)
        if a!=b: par[a]=b; tree.append((i,j))
        else: extra.append((i,j))
    return tree,extra
print("="*86)
print("  MEASURE k ON REAL INDICES")
print("="*86)
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)}
A8=alph(LAM,8); B=binding(LAM,8,A8)
t,e=cyclomatic(B,8)
print("\n     Λ : |binding| = %d   spanning tree = %d edges   extra = %d   **k = %d**"
      %(len(B),len(t),len(e),len(e)))
print("     defining system : 7 bounds, 8 vars -> k = 0")
print("""
  **Λ's recovered graph has k = %d and its defining graph has k = 0.** The
  nine extra edges are implied; that is why Chapter 10's tree recovery
  works on an object whose recovered graph is dense.
"""%len(e))
print("="*86)
print("  NOW BUILD INDICES WHOSE EXTRA EDGES ARE *NOT* IMPLIED")
print("="*86)
print("""
  Generate random cell sets at d = 3, compute k of the binding graph, and
  test whether **tree recovery + extra-edge check** decides reorderability.
""")
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def reord(S,d):
    A=alph(S,d)
    for ps in product(*[list(permutations(a)) for a in A]):
        T=relab(S,[list(p) for p in ps],d)
        if closed(T,[sorted({t[i] for t in T}) for i in range(d)]): return True
    return False
def tree_then_extra(S,d):
    """order the axes using only the SPANNING TREE bounds, then verify the extras"""
    A=alph(S,d); B=binding(S,d,A)
    tr,ex=cyclomatic(B,d)
    # try orderings that satisfy the tree constraints pairwise, then check all
    for ps in product(*[list(permutations(a)) for a in A]):
        T=relab(S,[list(p) for p in ps],d)
        AT=[sorted({t[i] for t in T}) for i in range(d)]
        ph=phis(T,d,AT)
        okt=all(all(x[i]<=ph[(i,j)].get(x[j],-1) for x in T) for (i,j) in tr)
        if not okt: continue
        # tree-only closure
        cand={x for x in product(*AT) if all(x[i]<=ph[(i,j)].get(x[j],-1) for (i,j) in tr)}
        if cand==T: return True,len(ex),True
        # now the extras
        cand2={x for x in cand if all(x[i]<=ph[(i,j)].get(x[j],-1) for (i,j) in ex)}
        if cand2==T: return True,len(ex),False
    return False,len(ex),None
buck={}
for _ in range(700):
    d=3
    A=[list(range(random.randint(2,3))) for _ in range(d)]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(2,len(cells))))
    Aa=alph(S,d)
    if any(len(a)<2 for a in Aa): continue
    a=reord(S,d); b,k,treeonly=tree_then_extra(S,d)
    buck.setdefault(k,[0,0,0,0])
    buck[k][0]+=1; buck[k][1]+=a; buck[k][2]+=b
    if a==b: buck[k][3]+=1
print("\n  %6s%10s%14s%16s%14s"%("k","n","reorderable","two-state says","agree"))
print("  "+"-"*62)
for k in sorted(buck):
    t2=buck[k]
    print("  %6d%10d%14d%16d%14d"%(k,t2[0],t2[1],t2[2],t2[3]))
tot=sum(v[0] for v in buck.values()); ag=sum(v[3] for v in buck.values())
print("\n     total %d   agree %d  (%.1f%%)"%(tot,ag,100*ag/max(tot,1)))
print("""
  **k is the coupling number.** If the two-state test agrees at k = 0 and
  degrades as k rises, then the tree is decidable and the coupling is
  exactly what is not — which is the decomposition asked for.
""")