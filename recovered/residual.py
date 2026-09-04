import numpy as np, random
from itertools import product, permutations, combinations
random.seed(269)
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
def descend(S,maxit=400,patience=3,restarts=1):
    A=alpha(S)
    for _ in range(restarts):
        o=[list(A[0]),list(A[1])]
        if _>0:
            random.shuffle(o[0]); random.shuffle(o[1])
        e=Ev(S,o); it=0; bad=0
        while e>0 and it<maxit:
            cands=[]
            for ax in (0,1):
                for i in range(len(o[ax])-1):
                    p=[list(x) for x in o]; p[ax][i],p[ax][i+1]=p[ax][i+1],p[ax][i]
                    cands.append((Ev(S,p),p))
            cands.sort(key=lambda t:t[0])
            if cands[0][0]<e: e,o=cands[0]; bad=0
            else:
                bad+=1
                if bad>patience: break
                e,o=random.choice(cands[:max(2,len(cands)//2)])
            it+=1
        if e==0: return True
    return False
def chain(S,ax=0):
    v=[frozenset(c for (a,c) in S if a==r) for r in alpha(S)[0]] if ax==0 \
      else [frozenset(a for (a,b) in S if b==c) for c in alpha(S)[1]]
    return all(p<=q or q<=p for p in v for q in v)
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
def width2(S):
    rows=sorted(set(sup_of(S).values()),key=len,reverse=True)
    for A in rows:
        ins=[b for b in rows if b<A]
        for t in combinations(ins,3):
            if all(not(x<=y or y<=x) for x,y in combinations(t,2)): return False
    return True
print("="*88)
print("  WHAT IS ACTUALLY IN THE RESIDUAL?")
print("="*88)
print("""
  **If every instance reaching step 7 is NOT reorderable, then the descent
  failing IS the correct answer, and step 7 is unnecessary.** That is the
  theorem worth aiming at, and it is measurable.
""")
for R in (1,3):
    tot=0; casc=0; desc=0; resid=[]
    for _ in range(3000):
        A=[list(range(random.randint(2,5))),list(range(random.randint(2,5)))]
        cells=list(product(*A)); S=set(random.sample(cells,random.randint(1,len(cells))))
        Aa=alpha(S)
        if len(Aa[0])<2 or len(Aa[1])<2: continue
        tot+=1
        if chain(S,0) or chain(S,1): casc+=1; continue
        if not c1p(S) or not width2(S): casc+=1; continue
        if descend(S,restarts=R): desc+=1; continue
        resid.append(S)
    good=[S for S in resid if reorderable(S)]
    print("\n  restarts = %d"%R)
    print("     total                      : %d"%tot)
    print("     cascade decided            : %d"%casc)
    print("     descent decided            : %d"%desc)
    print("     residual                   : %d  (%.2f%%)"%(len(resid),100*len(resid)/tot))
    print("     of which ACTUALLY reorderable : %d  (%.2f%% of all)"%(len(good),100*len(good)/tot))
    if good:
        print("     -> the descent MISSED these; step 7 is necessary for them")
        for S in good[:2]: print("        ",sorted(S))
    else:
        print("     **-> the residual is entirely NON-reorderable.**")
        print("     **cascade + descent is COMPLETE on this sample.**")
print("="*88)
print("  THE BETTER-DEFINED PROOF TARGET")
print("="*88)
print("""
  The proof that cannot be written: 'descent always reaches zero'. False.

  **The proof that can:** *if the cascade has not decided X, and X is
  reorderable, then the descent reaches zero.* **The cascade removes
  exactly the cases descent gets wrong.**

  That is a conditional statement, it is what the measurement above tests,
  and it is what the procedure actually needs — **step 7 is unnecessary
  precisely when this holds.**
""")