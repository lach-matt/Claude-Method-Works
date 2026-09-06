import numpy as np, random, math
from itertools import product, permutations, combinations
random.seed(431)
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
    if int(np.prod([math.factorial(len(a)) for a in A]))>10**6: return None
    for ps in product(*[list(permutations(a)) for a in A]):
        if lat(relab(S,[list(p) for p in ps],d),d): return True
    return False
def corner_sig(S,d):
    Ss=set(S); out=[]
    for x,y in combinations(sorted(S),2):
        I=tuple(i for i in range(d) if x[i]!=y[i])
        if not I: continue
        pat=[]
        for bits in product([0,1],repeat=len(I)):
            c=list(x)
            for t,i in enumerate(I): c[i]= y[i] if bits[t] else x[i]
            pat.append(1 if tuple(c) in Ss else 0)
        out.append((len(I),tuple(sorted(pat))))
    return tuple(sorted(out))
print("="*86)
print("  ISOLATING THE MIXED CLASS")
print("="*86)
from collections import defaultdict
cls=defaultdict(list)
for _ in range(2500):
    d=3; a=random.choice([2,3])
    A=[list(range(a)) for _ in range(d)]
    cells=list(product(*A))
    S=set(random.sample(cells,random.randint(2,len(cells))))
    Aa=alph(S,d)
    if any(len(x)<2 for x in Aa): continue
    rr=reord(S,d)
    if rr is None: continue
    cls[corner_sig(S,d)].append((frozenset(S),rr))
mixed=[v for v in cls.values() if len({r for _,r in v})>1]
print("\n     mixed classes found : %d"%len(mixed))
for grp in mixed[:2]:
    yes=[s for s,r in grp if r]; no=[s for s,r in grp if not r]
    print("\n  " + "-"*70)
    print("     REORDERABLE  :",sorted(yes[0]))
    print("     NOT          :",sorted(no[0]))
    A1=alph(yes[0],3); A2=alph(no[0],3)
    print("\n     alphabets    : %s   vs   %s"%([len(a) for a in A1],[len(a) for a in A2]))
    print("     cells        : %d   vs   %d"%(len(yes[0]),len(no[0])))
    for lab,S in [("YES",yes[0]),("NO",no[0])]:
        A=alph(S,3)
        fs=[]
        for i in range(3):
            fs.append(sorted(sum(1 for x in S if x[i]==u) for u in A[i]))
        print("     %-4s fibre sizes : %s"%(lab,fs))
    for lab,S in [("YES",yes[0]),("NO",no[0])]:
        A=alph(S,3); ch=[]
        for i in range(3):
            F={u:{tuple(x[k] for k in range(3) if k!=i) for x in S if x[i]==u} for u in A[i]}
            ch.append(all(F[u]<=F[v] or F[v]<=F[u] for u in A[i] for v in A[i]))
        print("     %-4s fibre chains: %s"%(lab,ch))
    for lab,S in [("YES",yes[0]),("NO",no[0])]:
        Ss=set(S)
        tri=0
        for x,y,z in combinations(sorted(S),3):
            j=tuple(max(x[i],y[i],z[i]) for i in range(3))
            m=tuple(min(x[i],y[i],z[i]) for i in range(3))
            if j not in Ss: tri+=1
            if m not in Ss: tri+=1
        print("     %-4s TRIPLE join/meet failures : %d"%(lab,tri))
print("="*86)
print("  DOES A TRIPLE INVARIANT SEPARATE THEM?")
print("="*86)
print("""
  The corner pattern is PAIRWISE. **If the mixed classes differ on a TRIPLE
  statistic, the missing invariant is one arity up** — which is §13.4
  appearing at the level of patterns rather than projections.
""")
def triple_sig(S,d):
    Ss=set(S); out=[]
    for t in combinations(sorted(S),3):
        I=tuple(i for i in range(d) if len({x[i] for x in t})>1)
        if not I: continue
        j=tuple(max(x[i] for x in t) for i in range(d))
        m=tuple(min(x[i] for x in t) for i in range(d))
        out.append((len(I), 1 if j in Ss else 0, 1 if m in Ss else 0))
    return tuple(sorted(out))
sep=0; tot=0
for grp in mixed:
    yes=[s for s,r in grp if r]; no=[s for s,r in grp if not r]
    for a in yes:
        for b in no:
            tot+=1
            if triple_sig(a,3)!=triple_sig(b,3): sep+=1
print("\n     mixed pairs : %d      separated by the TRIPLE signature : %d"%(tot,sep))
print("     **the triple invariant %s**"%("SEPARATES them" if sep==tot and tot>0 else "does not separate them"))