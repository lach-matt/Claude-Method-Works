import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(419)
print("="*86)
print("  THE SEED-INDEPENDENT QUANTITY: FIBRE CARDINALITY")
print("="*86)
print("""
  |F(u)| — the number of cells with axis-i value u — **requires no order to
  compute.** At d = 2 the proved construction sorts rows by support size,
  which is exactly this. **Test it as the loop's seed at every d.**
""")
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
def reord(S,d):
    A=alph(S,d)
    if int(np.prod([math.factorial(len(a)) for a in A]))>2*10**6: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def fibre_order(S,d,desc=False):
    A=alph(S,d); out=[]
    for i in range(d):
        cnt={u:sum(1 for x in S if x[i]==u) for u in A[i]}
        out.append(sorted(A[i],key=lambda u:(-cnt[u] if desc else cnt[u],u)))
    return out
print("="*86)
print("  1.  DOES IT RECOVER Λ's OWN ORDER?")
print("="*86)
CONS=[(1,0,lambda x:x[0]-1),(2,1,lambda x:4*x[1]+2),(3,2,lambda x:x[2]),(7,2,lambda x:x[2]),
      (5,4,lambda x:x[4]-1),(6,5,lambda x:4*x[5]+2),(6,3,lambda x:x[3])]
AX=[list(range(1,4)),list(range(0,2)),list(range(1,4)),list(range(0,4)),
    list(range(1,4)),list(range(0,2)),list(range(0,4)),list(range(0,4))]
LAM={z for z in product(*AX) if all(z[v]<=ub(z) for v,p,ub in CONS)}
NM=['n','l','k','q','e','f','g','2S']
for lab,desc in [("ascending",False),("descending",True)]:
    o=fibre_order(LAM,8,desc)
    ok=lat(relab(LAM,o,8),8)
    same=all(list(o[i])==sorted(o[i]) for i in range(8))
    print("\n     fibre order %s : still a sublattice = %s   equals the given order = %s"%(lab,ok,same))
    if not same:
        for i in range(8):
            if list(o[i])!=sorted(o[i]): print("        axis %-3s given %s   fibre %s"%(NM[i],sorted(o[i]),list(o[i])))
print("="*86)
print("  2.  AS A SEED, HOW OFTEN DOES IT WORK DIRECTLY?")
print("="*86)
print("\n  %5s%7s%9s%14s%14s%14s%12s"%("d","|A|","n","reorderable","fibre asc","fibre desc","either"))
print("  "+"-"*78)
for d,a,lim in [(2,3,220),(2,4,110),(3,2,220),(3,3,80),(4,2,90)]:
    n=r=fa=fd=ei=0
    for _ in range(lim):
        A=[list(range(a)) for _ in range(d)]
        cells=list(product(*A))
        S=set(random.sample(cells,random.randint(2,len(cells))))
        Aa=alph(S,d)
        if any(len(x)<2 for x in Aa): continue
        rr=reord(S,d)
        if rr is None: continue
        n+=1; r+=rr
        a1=lat(relab(S,fibre_order(S,d,False),d),d)
        a2=lat(relab(S,fibre_order(S,d,True),d),d)
        fa+=a1; fd+=a2; ei+= (a1 or a2)
    print("  %5d%7d%9d%14d%14d%14d%12d"%(d,a,n,r,fa,fd,ei))
print("""
  **'either' against 'reorderable' is the score.** If they match, sorting by
  fibre cardinality DECIDES — one pass, no seed, no iteration.
""")