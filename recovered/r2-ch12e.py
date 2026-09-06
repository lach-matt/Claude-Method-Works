# r2-ch12e.py — Phase R2 instrument for main §12.11 and §12.11.0 (chat 72). Requires tower-2.py beside it.
# Composition on Λ9 measured on ALL ordered pairs and ALL composable triples (the print: 41,682 pairs, 8,434 sampled triples).
import importlib.util, collections, itertools
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
L8=tw.L8(); L9=tw.L9(); S9=set(L9)
src=lambda c:(c[0],c[1],c[2],c[7]); tgt=lambda c:(c[4],c[5],c[6],c[8])
sources=set(map(src,L9)); targets=set(map(tgt,L9))
print('|Λ9| =',len(L9),'| distinct sources (n,ℓ,k,2S):',len(sources),'| distinct targets (e,f,g,2S′):',len(targets))
legal=[c for c in L9 if tgt(c) in sources]; print('§12.11.0 "all 1,654 targets of Λ9 are legal sources": cells whose target is a source of some cell: %d of %d | targets ∉ sources: %d, all with g = 0: %s (k ≥ 1 in every source; §10.2)'%(len(legal),len(L9),len(L9)-len(legal),all(c[6]==0 for c in L9 if tgt(c) not in sources)))
print('  Λ8 (n,ℓ,k,2S) against (e,f,g): shapes 4 against 3 — no composition defined; source set of Λ8 %d = its A-set'%len({src(c) for c in L8}))
# composition b∘a when tgt(a) == src(b): composite = (src(a), q = min(q_a,q_b), tgt(b))
bysrc=collections.defaultdict(list)
for b in L9: bysrc[src(b)].append(b)
def comp(a,b): return (a[0],a[1],a[2],min(a[3],b[3]),b[4],b[5],b[6],a[7],b[8])
pairs=0; fail=0; qle=0
for a in L9:
    for b in bysrc.get(tgt(a),()):
        pairs+=1; c=comp(a,b)
        if c not in S9: fail+=1
        if b[3]<=a[3]: qle+=1
print('  composable ordered pairs (a,b), target(a) = source(b): %d | composite ∈ Λ9: failures %d | q_b ≤ q_a in every pair (so min(q_a,q_b) = q_b): %s'%(pairs,fail,qle==pairs))
trip=0; afail=0
for a in L9:
    for b in bysrc.get(tgt(a),()):
        for c in bysrc.get(tgt(b),()):
            trip+=1
            if comp(comp(a,b),c)!=comp(a,comp(b,c)): afail+=1
print('  composable triples (a,b,c): %d | (c∘b)∘a ≠ c∘(b∘a): %d (print: 8,434 sampled, none)'%(trip,afail))
# predecessors and successors: cells with at least one predecessor / successor / both (Register 621–623: composable 1,169 of 1,654 = 70.7 %)
has_succ={c for c in L9 if tgt(c) in sources}; bytgt=collections.defaultdict(int)
for a in L9: bytgt[tgt(a)]+=1
has_pred={c for c in L9 if src(c) in targets}
print('  cells with a successor: %d | with a predecessor: %d | with both: %d | with either: %d (of 1,654; Register 621: composable 1,169 = 70.7 %%)'%(len(has_succ),len(has_pred),len(has_succ&has_pred),len(has_succ|has_pred)))
print('  composable cells with g = q (Register 621 "conservative share 739 of 1,169"): %d of %d'%(sum(1 for c in has_succ if c[6]==c[3]),len(has_succ)))
# the table L2556–2562: which end each tower axis attaches to, read from tower-2.py's bounds
print('  tower axes (tower-2.py): 2S′ ∈ [0,g] → target end; v ∈ [2S′,g] → target end; 2Jc ∈ [0,φ̂(k)] → source end; 2K ∈ [0, 2Jc+2·FMAX] → joint (Jc is source, the cap stands for f); 2J ∈ [2K−1, 2K+1] → joint')
for d in (10,11):
    L=tw.STAGES[d](); ends=len({(c[4],c[5],c[6],c[8],c[9]) for c in L}); print('  Λ%d: target set (e,f,g,2S′,v) has %d members, source set %s %d members — no target is a source (shapes differ): composition undefined'%(d,ends,'(n,ℓ,k,2S)' if d==10 else '(n,ℓ,k,2S,2Jc)',len({src(c) for c in L}) if d==10 else len({(c[0],c[1],c[2],c[7],c[10]) for c in L})))
# Figure 12.4 caption: "the forbidden f···K bridge … priced at 3.5%" — §12.11.1 L3067: 2K ≤ 2Jc + 2f (the cell's f) instead of 2Jc + 2·FMAX
L11=tw.L11(); L12=tw.L12()
L12f=[c+(K2,) for c in L11 for K2 in range(0, c[10]+2*c[5]+1)]
A12=lambda c:(c[0],c[1],c[2],c[7],c[10],c[11]); B12=lambda c:(c[4],c[5],c[6],c[8],c[9])
def sep(L):
    tot=0
    for qq in range(4):
        C=[c for c in L if c[3]==qq]; tot+=len({A12(c) for c in C})*len({B12(c) for c in C})
    return tot
print('  Λ12 with the cap (2K ≤ 2Jc + 2): %d cells, Σ_q|A(q)||B(q)| = %d (exact: %s) | with the cell\'s f (2K ≤ 2Jc + 2f): %d cells, Σ_q|A(q)||B(q)| = %d, over-count %.2f %% (L3067 "breaks the factorisation by 3.5%%")'%(len(L12),sep(L12),sep(L12)==len(L12),len(L12f),sep(L12f),100*(sep(L12f)-len(L12f))/len(L12f)))
# the tower's constraint graph: 13 nodes; edges from every two-coordinate bound (tower-2.py), with and without Λ9's 2S′ ≤ g once Λ10's 2S′ ≤ v ≤ g is present
E8={(0,1),(1,2),(2,3),(2,7),(3,6),(4,5),(5,6)}; E13=E8|{(6,8),(8,9),(6,9),(2,10),(10,11),(11,12)}
def cyc(nv,E):
    adj=collections.defaultdict(set)
    for a,b in E: adj[a].add(b); adj[b].add(a)
    seen={0}; st=[0]
    while st:
        u=st.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); st.append(w)
    return len(E)-nv+1 if len(seen)==nv else None
print('  Λ13 constraint graph with every bound drawn: 13 nodes, %d edges, cycle rank %s (the triangle 2S′–g–v; Register 1790) | with 2S′ ≤ g omitted as implied by 2S′ ≤ v ≤ g: %d edges, cycle rank %s — a tree (Figure 12.4 caption, the L2406–2408 amendment)'%(len(E13),cyc(13,E13),len(E13)-1,cyc(13,E13-{(6,8)})))
