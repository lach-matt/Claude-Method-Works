import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(479)
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
def reord(S,d,cap=200000):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>cap: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def minimal(S,d):
    if reord(S,d) is not False: return False
    for z in sorted(S):
        T=S-{z}; A=alph(T,d)
        if any(len(x)<2 for x in A): continue
        if reord(T,d) is False: return False
    return True
print("="*80)
print("  |A_i| <= |X| ALWAYS — so the census is parameterised by CELLS")
print("="*80)
bad=0
for _ in range(300):
    a=random.randint(2,5)
    cl=list(product(*[list(range(a)) for _ in range(3)]))
    S=set(random.sample(cl,random.randint(3,7)))
    if max(len(x) for x in alph(S,3))>len(S): bad+=1
print("\n     violations : %d   **bound holds : %s**"%(bad,bad==0))
print("="*80)
print("  IS MINIMAL OBSTRUCTION SIZE BOUNDED?")
print("="*80)
print("\n  %8s%10s%12s%12s%16s"%("box","found","min","MAX","sizes"))
print("  "+"-"*60)
for a,kmax,tries in [(3,6,1500),(4,7,1200),(5,7,900)]:
    cl=list(product(*[list(range(a)) for _ in range(3)]))
    sizes={}; cnt=0
    for _ in range(tries):
        k=random.randint(3,kmax)
        S=set(random.sample(cl,k))
        Aa=alph(S,3)
        if any(len(x)<2 for x in Aa): continue
        r=reord(S,3)
        if r is not False: continue
        if not minimal(S,3): continue
        sizes[len(S)]=sizes.get(len(S),0)+1; cnt+=1
    if sizes:
        print("  %8s%10d%12d%12d%16s"%("%d³"%a,cnt,min(sizes),max(sizes),dict(sorted(sizes.items()))))