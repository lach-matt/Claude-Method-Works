# l-ch2.py — Phase R2 chapter-2 instrument (chat 69). Measures on the rebuilt Λ₉ (tower-2.py, unchanged) the
# properties main §2.16.2 L769–772 prints for the target-spin extension, over ALL pairs rather than the printed 200,000.
import importlib.util
spec=importlib.util.spec_from_file_location('tower','tower-2.py'); tw=importlib.util.module_from_spec(spec); spec.loader.exec_module(tw)
L9=tw.L9(); S9=set(L9); L8=set(tw.L8())
print('|Λ9|',len(L9),'(printed 1,654)')
print('projects exactly onto Λ8:',set(c[:8] for c in L9)==L8)
print('F(-1) =',sum((-1)**sum(c) for c in L9),'(printed 2; rank = Σxᵢ per Ch. 9 L1947)')
bad=0; n=len(L9)
for i in range(n):
    a=L9[i]
    for b in L9[i+1:]:
        if tuple(map(max,a,b)) not in S9 or tuple(map(min,a,b)) not in S9: bad+=1
print('join/meet failures over all',n*(n-1)//2,'pairs:',bad,'→ sublattice and E = 0 iff 0')
print('rank-modularity rank(x∨y)+rank(x∧y)=rank(x)+rank(y): identically true for coordinatewise max/min with rank = Σxᵢ')
print('pendant factor / tree: L9 adds 2S′ with 0 ≤ 2S′ ≤ g only (tower-2.py L9), one new edge g–2S′ on the constraint graph')