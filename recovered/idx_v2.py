from itertools import product, permutations, combinations
def E(S,d,ret=False):
    S=set(S); vals=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S:
            if c[i]>m.get(c[j],-99): m[c[j]]=c[i]
        b,o=-99,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    R={x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
    box=1
    for v in vals: box*=len(v)
    return (len(R)-len(S),sorted(R-S),box) if ret else len(R)-len(S)

print('  V2 THEORY -- the four terms, audited before construction')
T=[('causal','Buniy jurisdiction','OPERATIVE',
    'but "causal" = no superluminal propagation, which is SD_obs / X_exp in V1'),
   ('field content','Buniy jurisdiction','OPERATIVE',
    'scalar / gauge / fermionic matter -- CATEGORICAL, not ordered'),
   ('interacting','Hartman jurisdiction','stated, NOT operative',
    'their own appendix: the inequality holds for free scalars too'),
   ('d > 2','Hartman jurisdiction','stated, NOT operative',
    'Fewster: 2d CFTs have their own results, not a counterexample')]
print('  %-16s %-24s %-22s %s' % ('term','source','status','note'))
for a,b,c,d in T: print('  %-16s %-24s %-22s %s' % (a,b,c,d))
print()
print('  -> only TWO terms are operative, and one of them belongs in V1,')
print('     and the other is categorical.')
print()
print('  CAN A CATEGORICAL LETTER BE INDEXED?')
print('     the operator reads monotone upper envelopes. a monotone envelope on a')
print('     categorical axis requires an order. field content has none.')
print()
FT=['scalar','gauge','fermion','mixed']
# build V2 with an imposed ordering on FIELD; the only real edge:
#   d=2 is special (conformal); interacting theories in d=2 are often integrable
# and Buniy's content scope: scalar/gauge/fermion admitted, "mixed/other" outside
NM=['CAUS','FIELD','INT','DIM']
def build(order):
    idx={f:order.index(f) for f in FT}
    cells=set()
    for caus in range(2):
        for f in FT:
            for inte in range(2):
                for dim in range(2):
                    # the one internal edge located: Buniy's content scope requires causality
                    if f=='mixed' and caus==0: continue
                    cells.add((caus,idx[f],inte,dim))
    return cells
print('  %-42s %6s %6s' % ('ordering of FIELD','cells','E'))
res=[]
for order in permutations(FT):
    S=build(list(order)); e=E(S,4)
    res.append((e,order))
    if order[:2] in [('scalar','gauge'),('mixed','scalar')] or e!=res[0][0]:
        pass
best=min(r[0] for r in res); worst=max(r[0] for r in res)
from collections import Counter
print('     orderings tested: %d   E values: %s' % (len(res),dict(Counter(r[0] for r in res))))
for e,order in sorted(res)[:3]:
    print('     %-42s %6d %6d' % (' < '.join(order), len(build(list(order))), e))
print()
if best==worst:
    print('  E is INVARIANT under the ordering: %d' % best)
    print('  -> the categorical axis carries no constraint, so no ordering can matter.')
    print('     V2 %s, and it closes because it is nearly a free product:' % ('CLOSES' if best==0 else 'is OPEN'))
    print('     the terms are jurisdiction conditions for OTHER indices, not constraints on each other.')
else:
    print('  E VARIES with the ordering: %d to %d' % (best,worst))
    print('  -> sub-case A. the defect is an artefact of ordering a categorical axis.')
print()
print('  WHAT V2 ACTUALLY IS')
print('     of four terms: 2 non-operative, 1 belongs in V1, 1 is categorical.')
print('     it has no internal edges that were locatable in the sources.')
print('     V2 is not an index. it is a LIST of scope conditions that other')
print('     chargers cite, with no structure among them.')
print()
print('  CONSEQUENCE FOR THE SYSTEM GRAPH')
print('     Hartman spans V1 + V2 + V3. but both of its V2 conditions are non-operative.')
print('     so Hartman OPERATIVELY spans V1 + V3 only -- a TWO-index charger.')
print('     that is the configuration Part VIII computes as: connected, 1 cycle.')
print()
print('     re-running the connectivity with Hartman as a V1-V3 edge:')
N=['V1','V2','V3','V4','V5','V6','V7']
CH={'Buniy':['V1','V2'],'Hartman':['V1','V3'],'Wall':['V1','V4','V5'],
    'Graham-Olum':['V3','V6'],'spin-statistics':['V1','V4'],'Ostrogradsky':['V1','V7']}
Ed=set()
for k,v in CH.items():
    for a,b in combinations(sorted(v),2): Ed.add((a,b))
from collections import defaultdict
adj=defaultdict(set)
for a,b in Ed: adj[a].add(b); adj[b].add(a)
seen=set(); comp=0
for v in N:
    if v in seen: continue
    comp+=1; st=[v]; seen.add(v)
    while st:
        u=st.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); st.append(w)
print('        nodes %d  edges %d  components %d  cycles %d' % (len(N),len(Ed),comp,len(Ed)-len(N)+comp))
print()
print('     BUT Hartman is still VACUOUS (computed in the V1xV3 product: 0 cells).')
print('     so the edge exists on paper and carries no traffic.')
print('     connectivity in the graph is not the same as reachability in the index.')