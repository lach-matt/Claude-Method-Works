import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(541)
def alph(S,d): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o,d):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def lat(S,d):
    Ss=set(S)
    for x,y in combinations(sorted(S),2):
        if tuple(max(x[i],y[i]) for i in range(d)) not in Ss: return False
        if tuple(min(x[i],y[i]) for i in range(d)) not in Ss: return False
    return True
def reord(S,d,cap=50000):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
print("="*82)
print("  DISTANCE TO REORDERABILITY — HOW MANY CELLS MUST GO?")
print("="*82)
print("\n  %5s%6s%8s%9s%9s%9s%10s"%("d","|A|","n","dist 1","dist 2","dist 3+","median"))
print("  "+"-"*60)
for d,a,lim in [(2,3,90),(3,2,90),(2,4,40)]:
    n=0; dist=[]
    for _ in range(lim):
        Ax=[list(range(a)) for _ in range(d)]
        cl=list(product(*Ax))
        S=set(random.sample(cl,random.randint(3,min(len(cl),7))))
        A=alph(S,d)
        if any(len(x)<2 for x in A): continue
        if reord(S,d) is not False: continue
        found=None
        for k in (1,2,3):
            for T in combinations(sorted(S),k):
                U=S-set(T); AU=alph(U,d)
                if any(len(x)<2 for x in AU): continue
                if reord(U,d) is True: found=k; break
            if found: break
        if found is None: found=4
        n+=1; dist.append(found)
    if n:
        print("  %5d%6d%8d%9d%9d%9d%10.1f"%(d,a,n,
            sum(1 for x in dist if x==1),sum(1 for x in dist if x==2),
            sum(1 for x in dist if x>=3),np.median(dist)))