import numpy as np, random
from itertools import product, permutations, combinations
random.seed(367)
print("="*86)
print("  IS 𝓡-CLOSURE THE SAME AS JOIN/MEET CLOSURE?")
print("="*86)
print("""
  The book asserts both of Λ: closed under join and meet, and E(Λ) = 0.
  **It never asks whether they are the same condition.** If they are, then
  reorderability = 'some ordering makes X a sublattice', which is a cleaner
  object with its own literature.
""")
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def Rclosed(S,d):
    A=alph(S,d); ph={}
    for i in range(d):
        for j in range(d):
            if i==j: continue
            f={}; run=-1
            for v in A[j]:
                c=[x[i] for x in S if x[j]<=v]; run=max(run,max(c) if c else -1); f[v]=run
            ph[(i,j)]=f
    return {x for x in product(*A) if all(x[i]<=ph[(i,j)].get(x[j],-1)
            for i in range(d) for j in range(d) if i!=j)}==S
def lat(S,d):
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in S: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in S: return False
    return True
print("  %5s%7s%9s%14s%14s%12s%12s"%("d","|A|","n","𝓡-closed","join/meet","both","disagree"))
print("  "+"-"*72)
DIS=[]
for d,a,lim in [(2,2,400),(2,3,400),(2,4,300),(3,2,400),(3,3,200)]:
    n=r=l=b=0
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        n+=1
        rr=Rclosed(S,d); ll=lat(S,d)
        r+=rr; l+=ll; b+= (rr and ll)
        if rr!=ll and len(DIS)<4: DIS.append((d,sorted(S),rr,ll))
    print("  %5d%7d%9d%14d%14d%12d%12d"%(d,a,n,r,l,b,r+l-2*b))
if DIS:
    print("\n  DISAGREEMENTS:")
    for d,S,rr,ll in DIS:
        print("     d=%d 𝓡=%s lat=%s  %s"%(d,rr,ll,str(S)[:56]))
else:
    print("\n  **NO DISAGREEMENTS — the two conditions coincide.**")
print("="*86)
print("  AND THE REORDERABLE VERSIONS")
print("="*86)
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def reord_R(S,d):
    A=alph(S,d)
    for ps in product(*[list(permutations(x)) for x in A]):
        if Rclosed(relab(S,[list(p) for p in ps],d),d): return True
    return False
def reord_lat(S,d):
    A=alph(S,d)
    for ps in product(*[list(permutations(x)) for x in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
print("\n  %5s%7s%9s%16s%16s%12s"%("d","|A|","n","𝓡-reorderable","lat-reorderable","disagree"))
print("  "+"-"*68)
D2=[]
for d,a,lim in [(2,2,300),(2,3,250),(2,4,120),(3,2,250),(3,3,60)]:
    n=r=l=dd=0
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        n+=1
        rr=reord_R(S,d); ll=reord_lat(S,d)
        r+=rr; l+=ll
        if rr!=ll:
            dd+=1
            if len(D2)<3: D2.append((d,sorted(S),rr,ll))
    print("  %5d%7d%9d%16d%16d%12d"%(d,a,n,r,l,dd))
if D2:
    print("\n  DISAGREEMENTS:")
    for d,S,rr,ll in D2: print("     d=%d 𝓡=%s lat=%s  %s"%(d,rr,ll,str(S)[:52]))
else:
    print("""
  **THE TWO REORDERABILITY QUESTIONS ARE THE SAME QUESTION.**

  > **X is 𝓡-reorderable ⟺ some ordering of the axes makes X a
  > SUBLATTICE of the product of chains.**

  That is a statement in lattice theory, not in interval-matrix theory, and
  it is where the problem has been all along.
""")