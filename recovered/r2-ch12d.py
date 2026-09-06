# r2-ch12d.py — Phase R2 instrument for main §12.10–§12.10.2 (chat 72). Requires tower-2.py beside it.
# The §12.10.1 table's Λ9 column, every row measured on ALL 1,654 cells and ALL C(1654,2) pairs (the print sampled 200,000).
import importlib.util, collections, math
import numpy as np
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
L8=tw.L8(); L9=tw.L9(); X8=np.array(L8,dtype=np.int16); X9=np.array(L9,dtype=np.int16)
print('|Λ8| =',len(L8),'| |Λ9| =',len(L9),'(2S′ ∈ [0, g] adjoined to every cell)')
for name,X in (('Λ8',X8),('Λ9',X9)):
    n=len(X); lo=X.min(axis=0); hi=X.max(axis=0); box=int(np.prod(hi-lo+1))
    # closure defect E = |ℛ(X)| − |X| under coordinatewise join and meet, all n² ordered pairs
    S=set(map(tuple,X.tolist())); J=np.maximum(X[:,None,:],X[None,:,:]).reshape(-1,X.shape[1]); M=np.minimum(X[:,None,:],X[None,:,:]).reshape(-1,X.shape[1])
    E=len(set(map(tuple,J.tolist()))|set(map(tuple,M.tolist()))|S)-n
    rank=X.sum(axis=1).astype(np.int64); levels=collections.Counter(rank.tolist()); lv=sorted(levels); seq=[levels[r] for r in lv]
    iu,ju=np.triu_indices(n,1)
    rj=np.maximum(X[iu],X[ju]).sum(axis=1).astype(np.int64); rm=np.minimum(X[iu],X[ju]).sum(axis=1).astype(np.int64)
    viol=int((rank[iu]+rank[ju]!=rj+rm).sum())
    Fm1=int(((-1)**rank).sum()); mx=max(seq); pk=[r for r in lv if levels[r]==mx]
    logc=all(seq[i]**2>=seq[i-1]*seq[i+1] for i in range(1,len(seq)-1)); p=seq.index(mx)
    unim=all(seq[i]<=seq[i+1] for i in range(p)) and all(seq[i]>=seq[i+1] for i in range(p,len(seq)-1))
    print('%s: cells %d | box ∏(hi−lo+1) = %d | E(X) = %d (sublattice of the box: %s) | rank-modular r(x)+r(y) = r(x∨y)+r(x∧y) on %d unordered pairs: violations %d | F(1) = %d | F(−1) = Σ(−1)^rank = %d | rank levels %d (ranks %d..%d), widest %d at rank %s | log-concave %s | unimodal %s'%(name,n,box,E,E==0,len(iu),viol,n,Fm1,len(lv),lv[0],lv[-1],mx,pk,logc,unim))
    print('   level sizes:',seq)
# constraint graph of Λ9: the seven edges of Λ8 plus g–2S′
edges8={(1,0),(2,1),(3,2),(7,2),(6,3),(5,4),(6,5)}; edges9=edges8|{(8,6)}
def is_tree(nv,edges):
    adj=collections.defaultdict(set)
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    seen={0}; st=[0]
    while st:
        u=st.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); st.append(w)
    return len(seen)==nv and len(edges)==nv-1
deg9=collections.Counter([a for a,b in edges9]+[b for a,b in edges9])
print('constraint graph Λ9: 9 vertices, %d edges, tree %s | 2S′ (index 8) degree %d (a leaf, attached at g): %s'%(len(edges9),is_tree(9,edges9),deg9[8],deg9[8]==1 and (8,6) in edges9))
# projection Λ9 → Λ8 (drop 2S′): exact; fibre sizes
proj=collections.Counter(tuple(c[:8]) for c in L9); S8=set(L8)
print('projection of Λ9 onto the first eight coordinates: %d cells, equal to Λ8: %s | fibre sizes (preimages per Λ8 cell): min %d, max %d, distribution %s | mean = %d/%d = %.4f'%(len(proj),set(proj)==S8,min(proj.values()),max(proj.values()),dict(sorted(collections.Counter(proj.values()).items())),len(L9),len(L8),len(L9)/len(L8)))
print('   fibre size = g+1 for every cell:',all(proj[c]==c[6]+1 for c in L8))
