import pickle, time
from itertools import product, permutations, combinations
DIMS=(2,3,3); d=3
cells=list(product(*[range(x) for x in DIMS])); n=len(cells)
def alph(S): return [sorted({x[i] for x in S}) for i in range(d)]
def relab(S,o):
    ix=[{v:i for i,v in enumerate(p)} for p in o]
    return {tuple(ix[k][x[k]] for k in range(d)) for x in S}
def canon(T):
    A=alph(T); best=None
    for ps in product(*[list(permutations(a)) for a in A]):
        c=tuple(sorted(relab(T,[list(p) for p in ps])))
        if best is None or c<best: best=c
    return best
t0=time.time()
tab={}
for T in combinations(range(n),3):
    S={cells[i] for i in T}
    tab[T]=canon(S)
print("="*80)
print("  STAGE 1 — CANONICAL FORMS OF EVERY 3-SUBSET")
print("="*80)
print("\n     box                 : %s   (%d cells)"%("×".join(map(str,DIMS)),n))
print("     3-subsets            : %d"%len(tab))
print("     distinct canon forms : %d"%len(set(tab.values())))
print("     time                 : %.2fs"%(time.time()-t0))
ids={c:i for i,c in enumerate(sorted(set(tab.values())))}
tab2={T:ids[c] for T,c in tab.items()}
pickle.dump({'dims':DIMS,'cells':cells,'tab':tab2,'nforms':len(ids)},open('/home/claude/stage/s1.pkl','wb'))
print("\n     saved  /home/claude/stage/s1.pkl")
print("     **every later stage is a table lookup**")