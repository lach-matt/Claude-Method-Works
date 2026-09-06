print("="*88)
print("  AND NOW THE DECISION, ON THE CORRECT TREE")
print("="*88)
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
def nostrict(sp): return not any(a<c and d<b for (a,b) in sp for (c,d) in sp)
def decide(S):
    A=alpha(S); sup=sup_of(S)
    root=build(set(A[1]),list(sup.values()))
    if root is None: return False
    for f in valid_frontiers(root,S):
        ic={c:i for i,c in enumerate(f)}
        sp=[]
        for r in A[0]:
            t=sorted(ic[c] for c in sup[r]); sp.append((t[0],t[-1]))
        if nostrict(sp): return True
    return False
def gen_nested(nc):
    rows=[]
    for _ in range(random.randint(3,6)):
        a=random.randint(0,nc-1); b=random.randint(a,nc-1); rows.append(set(range(a,b+1)))
    return {(i,c) for i,rw in enumerate(rows) for c in rw}
print("\n  %12s%9s%9s%12s%12s"%("source","n","agree","false pos","false neg"))
print("  "+"-"*54)
TF=0
for lab in ("random","nested"):
    n=ag=fp=fn=0
    for _ in range(1200):
        if lab=="random":
            A=[list(range(random.randint(2,4))),list(range(random.randint(2,5)))]
            cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        else:
            S=gen_nested(random.randint(3,5))
        Aa=alpha(S)
        if len(Aa[0])<2 or len(Aa[1])<2: continue
        n+=1
        a=reorderable(S); b=decide(S)
        ag+=(a==b)
        if b and not a: fp+=1
        if a and not b: fn+=1
    TF+=fp+fn
    print("  %12s%9d%9d%12d%12d"%(lab,n,ag,fp,fn))
print()
print("  **%s**"%("EXACT" if TF==0 else "%d errors"%TF))