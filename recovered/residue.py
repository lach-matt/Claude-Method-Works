import numpy as np, random
from itertools import product, permutations, combinations
random.seed(271)
def alpha(S): return [sorted({x[i] for x in S}) for i in range(2)]
def sup_of(S): return {r:frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]}
def relabel(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {(ix[0][x],ix[1][y]) for (x,y) in S}
def Ev(S,o):
    T=relabel(S,o); A=[sorted({t[i] for t in T}) for i in range(2)]
    M={};run=-1
    for v in A[0]:
        c=[y for (x,y) in T if x<=v]; run=max(run,max(c) if c else -1); M[v]=run
    N={};run=-1
    for w in A[1]:
        c=[x for (x,y) in T if y<=w]; run=max(run,max(c) if c else -1); N[w]=run
    return sum(1 for r in A[0] for c in A[1] if c<=M[r] and r<=N[c])-len(T)
def reorderable(S):
    A=alpha(S)
    for p0 in permutations(A[0]):
        for p1 in permutations(A[1]):
            if Ev(S,[list(p0),list(p1)])==0: return True
    return False
def descend(S,moves,maxit=300,patience=3,restarts=3):
    A=alpha(S)
    for t in range(restarts):
        o=[list(A[0]),list(A[1])]
        if t: random.shuffle(o[0]); random.shuffle(o[1])
        e=Ev(S,o); it=0; bad=0
        while e>0 and it<maxit:
            cands=[(Ev(S,p),p) for p in moves(S,o)]
            if not cands: break
            cands.sort(key=lambda x:x[0])
            if cands[0][0]<e: e,o=cands[0]; bad=0
            else:
                bad+=1
                if bad>patience: break
                e,o=random.choice(cands[:max(2,len(cands)//2)])
            it+=1
        if e==0: return True
    return False
def moves_swap(S,o):
    out=[]
    for ax in (0,1):
        for i in range(len(o[ax])-1):
            p=[list(x) for x in o]; p[ax][i],p[ax][i+1]=p[ax][i+1],p[ax][i]; out.append(p)
    return out
def overlap(a,b): return bool(a&b) and not(a<=b) and not(b<=a)
def comps(sets):
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
def moves_struct(S,o):
    """adjacent swaps PLUS block reversals of overlap components"""
    out=moves_swap(S,o)
    rows=list(set(sup_of(S).values()))
    for cs in comps(rows):
        u=frozenset().union(*[rows[i] for i in cs])
        pos=sorted(o[1].index(c) for c in u if c in o[1])
        if len(pos)>1 and pos==list(range(pos[0],pos[0]+len(pos))):
            p=[list(x) for x in o]
            seg=p[1][pos[0]:pos[-1]+1]; p[1][pos[0]:pos[-1]+1]=seg[::-1]; out.append(p)
    # and whole-block moves: shift a component to either end
    for cs in comps(rows):
        u=sorted(frozenset().union(*[rows[i] for i in cs]))
        rest=[c for c in o[1] if c not in u]
        out.append([list(o[0]),u+rest]); out.append([list(o[0]),rest+u])
    for r in rows:
        u=sorted(r); rest=[c for c in o[1] if c not in u]
        out.append([list(o[0]),u+rest]); out.append([list(o[0]),rest+u])
    return out
print("="*88)
print("  WHAT THE RESIDUE SHARES")
print("="*88)
res=[]; other=[]
n=0
while n<2200:
    A=[list(range(random.randint(3,5))),list(range(random.randint(3,5)))]
    cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
    Aa=alpha(S)
    if len(Aa[0])<2 or len(Aa[1])<2: continue
    n+=1
    if not reorderable(S): continue
    if descend(S,moves_swap): other.append(S)
    else: res.append(S)
def feats(S):
    rows=list(set(sup_of(S).values())); A=alpha(S)
    ov=sum(1 for a,b in combinations(rows,2) if overlap(a,b))
    ne=sum(1 for a in rows for b in rows if b<a)
    return dict(dens=len(S)/(len(A[0])*len(A[1])), rows=len(rows),
                overlap_pairs=ov, nest_pairs=ne,
                comps=len(comps(rows)),
                full_union=sum(1 for a in rows for b in rows for c in rows
                               if a!=b and (b|c)==a and overlap(b,c)))
print("\n  %-18s%14s%14s"%("feature","descent OK","descent MISSES"))
print("  "+"-"*48)
if res and other:
    for k in ('dens','rows','overlap_pairs','nest_pairs','comps','full_union'):
        print("  %-18s%14.3f%14.3f"%(k,np.mean([feats(S)[k] for S in other]),
                                       np.mean([feats(S)[k] for S in res])))
print("\n     descent misses : %d of %d reorderable"%(len(res),len(res)+len(other)))
print("="*88)
print("  SO GIVE THE DESCENT THE STRUCTURE'S OWN MOVES")
print("="*88)
print("""
  Adjacent transposition is a move on RAW COLUMNS. **The structure's moves
  are: reverse an overlap component, and shift a component or a row to
  either end.** Add them.
""")
a=b=0
for S in res+other:
    a+= descend(S,moves_swap)
    b+= descend(S,moves_struct)
print("\n     reorderable instances        : %d"%(len(res)+len(other)))
print("     adjacent swaps only          : %d  (%.1f%%)"%(a,100*a/max(len(res)+len(other),1)))
print("     **with structural moves**    : %d  (%.1f%%)"%(b,100*b/max(len(res)+len(other),1)))