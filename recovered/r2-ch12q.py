# r2-ch12q.py — Phase R2, main §12.11.1 "The axes, and what each one sees", first segment (L3032–3090), chat 76.
# The axis table's cells and density column re-measured under the printed definition (L3077–3086: for each axis, over
# every cell of the stage below, count the values of the new coordinate that exact vector coupling realises, divided by
# the values the bound allows — sum over sum), with the loose readings the text rejects printed alongside; the axis-12
# populations Λ₈ / Λ₉ / Λ₁₀ (L3045–3048) and the J_c-realised filter (L3050–3053; Register 434); φ̂(k) as the monotone
# envelope of max 2J (L3070–3071); the 213 φ̂ sites (L3074); the three independence examples (L3087–3089) and the same
# test at every axis; projection exactness (L3086); the constraint graph by stage against Register 1790 and the Figure
# 12.4 caption (DEFERRED); the tight-K factorisation against §12.11.5's 15,150 / 45,450 and L3067's "3.5 %" (DEFERRED).
# LS terms by microstate enumeration (L3059–3063). tower-2.py by path via r2lib. Deterministic (no wall-clock).
import importlib.util, os, re, itertools
from collections import Counter, defaultdict
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()
PHI, FMAX = T.PHI, T.FMAX
N = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S', '2S′', 'v', '2Jc', '2K', '2J']

# ---- LS terms of ℓ^k by microstate enumeration (L3059–3063): accumulate (2M_L, 2M_S), strip (2S, 2L) blocks from the top
def terms(l, k):
    if k == 0: return Counter({(0, 0): 1})
    orbs = [(ml, ms) for ml in range(-l, l + 1) for ms in (-1, 1)]
    ms_count = Counter((2 * sum(o[0] for o in c), sum(o[1] for o in c)) for c in itertools.combinations(orbs, k))
    out = Counter()
    while ms_count:
        ML2 = max(m for m, _ in ms_count); MS2 = max(sv for m, sv in ms_count if m == ML2)
        out[(MS2, ML2)] += 1
        for ml2 in range(-ML2, ML2 + 1, 2):
            for ms2 in range(-MS2, MS2 + 1, 2):
                ms_count[(ml2, ms2)] -= 1
                if ms_count[(ml2, ms2)] == 0: del ms_count[(ml2, ms2)]
                assert ms_count.get((ml2, ms2), 0) >= 0
    return out
def new_terms(l, v): return terms(l, v) - terms(l, v - 2) if v >= 2 else terms(l, v)   # multiset difference (L3081)
def jc_values(l, k, S2): return sorted({j for (s2, L2), _ in terms(l, k).items() if s2 == S2 for j in range(abs(L2 - s2), L2 + s2 + 1, 2)})
SYM = {0: 'S', 2: 'P', 4: 'D', 6: 'F'}
def name(t): return f'{t[0]+1}{SYM[t[1]]}'
print('== L3059–3063 terms(ℓᵏ) by microstate enumeration:')
for l, k in [(0, 1), (0, 2), (1, 1), (1, 2), (1, 3)]:
    tt = terms(l, k); print(f'   {"sp"[l]}^{k}: {" ".join(name(t) + ("×" + str(m) if m > 1 else "") for t, m in sorted(tt.items(), reverse=True))}  (microstates {sum((2*t[0]//2+1)*(t[1]+1) for t in tt.elements())})')
print(f'   p^2 new at 2: {[name(t) for t in new_terms(1, 2)]} | p^3 new at 3: {[name(t) for t in new_terms(1, 3)]} | s^2 new at 2: {[name(t) for t in new_terms(0, 2)]} (seniority 0)')
print(f'   2S ≤ k at every term of s^1..p^3 (Chapter 7\'s origin): {all(t[0] <= k for l, k in [(0,1),(0,2),(1,1),(1,2),(1,3)] for t in terms(l, k))}')

# ---- φ̂(k) (L3070–3071): monotone envelope of k ↦ max 2J over the parent shells the caps admit (ℓ ≤ 1, k ≤ 4ℓ+2)
mx = {k: max(L2 + s2 for l in (0, 1) if k <= 4 * l + 2 for (s2, L2) in terms(l, k)) for k in (1, 2, 3)}
env = {}; run = 0
for k in (1, 2, 3): run = max(run, mx[k]); env[k] = run
print(f'== L3070–3071 φ̂(k): max 2J over admitted parent shells {mx} → monotone envelope {env} | tower-2.py PHI {PHI} | equal {env == PHI} | already monotone {mx == env}')

# ---- stages
L8, L9, L10, L11, L12, L13 = T.L8(), T.L9(), T.L10(), T.L11(), T.L12(), T.L13()
L9p = [c for c in L9 if c[8] <= 2 * c[5] + 1]
print(f'== L3033–3039 cells: Λ9 {len(L9):,} | Λ9′ {len(L9p):,} (2S′ ≤ 2f+1 cuts {len(L9)-len(L9p)}, all at f = 0, g = 2, 2S′ = 2: {all((c[5],c[6],c[8])==(0,2,2) for c in L9 if c[8] > 2*c[5]+1)}) | Λ10 {len(L10):,} | Λ11 {len(L11):,} | Λ12 {len(L12):,} | Λ13 {len(L13):,}')

# ---- densities, sum over sum (L3077–3086)
spin = {(l, g): sorted({s2 for (s2, _) in terms(l, g)}) for l in (0, 1) for g in range(0, 4)}
num9 = sum(len(spin[(c[5], c[6])]) for c in L8)
assert all(s2 <= c[6] and s2 <= 2 * c[5] + 1 for c in L8 for s2 in spin[(c[5], c[6])])
print(f'== axis 9: realised 2S′ = spin set of f^g by microstate enumeration, summed over all {len(L8)} cells of Λ8 = {num9}; over Λ9\'s {len(L9):,} values → {100*num9/len(L9):.1f}% (printed 63.7) | every realised spin obeys 2S′ ≤ g and 2S′ ≤ 2f+1: True')
print(f'== axis 9′: same numerator {num9} over Λ9′\'s {len(L9p):,} → {100*num9/len(L9p):.1f}% (printed 67.5)')
def v_real(c, mode):
    f, g, s2p = c[5], c[6], c[8]; out = []
    for v in range(s2p, g + 1):
        if mode == 'parity' and (g - v) % 2: continue
        pool = new_terms(f, v) if mode in ('new', 'parity') else terms(f, v)
        if any(s2 == s2p for (s2, _) in pool): out.append(v)
    return out
for mode, lab in [('new', 'terms new at v (multiset difference, L3081)'), ('parity', 'new at v AND v ≡ g mod 2'), ('exists', 'a term of spin 2S′ merely existing at v (the loose reading)')]:
    n10 = sum(len(v_real(c, mode)) for c in L9)
    print(f'== axis 10 [{lab}]: Σ over all {len(L9):,} Λ9 cells = {n10:,} / Λ10 {len(L10):,} → {100*n10/len(L10):.1f}%' + (' (printed 44.7)' if mode == 'new' else ''))
jc_all = {(l, k): sorted({j for (s2, L2) in terms(l, k) for j in range(abs(L2 - s2), L2 + s2 + 1, 2)}) for l in (0, 1) for k in (1, 2, 3) if k <= 4 * l + 2}
n11 = sum(len(jc_values(c[1], c[2], c[7])) for c in L10); n11_loose = sum(len(jc_all[(c[1], c[2])]) for c in L10)
assert all(j <= PHI[c[2]] for c in L10 for j in jc_values(c[1], c[2], c[7]))
print(f'== axis 11 [terms carrying the cell\'s own 2S, L3082]: Σ over all {len(L10):,} Λ10 cells = {n11:,} / Λ11 {len(L11):,} → {100*n11/len(L11):.1f}% (printed 17.0) | every realised 2J_c ≤ φ̂(k): True')
print(f'   [all terms of ℓᵏ, the loose reading]: {n11_loose:,} / {len(L11):,} → {100*n11_loose/len(L11):.1f}%')
def k_num(jc2, f2): return min(jc2, f2) + 1            # 2K from |2J_c − 2f| to 2J_c + 2f in steps of 2
def k_den(jc2): return jc2 + 2 * FMAX + 1
realised11 = {(l, k, S2): set(jc_values(l, k, S2)) for l in (0, 1) for k in (1, 2, 3) if k <= 4 * l + 2 for S2 in range(0, k + 1)}
def axis12(pop, filt=False, fcell=True):
    num = den = 0
    for c in pop:
        for jc2 in range(0, PHI[c[2]] + 1):
            den += k_den(jc2)
            if filt and jc2 not in realised11[(c[1], c[2], c[7])]: continue
            num += k_num(jc2, 2 * c[5] if fcell else 2 * FMAX)
    return num, den
for pop, lab in [(L8, 'Λ8'), (L9, 'Λ9'), (L10, 'Λ10 (= every cell of Λ11, the stage below)')]:
    n, d = axis12(pop); nf, df = axis12(pop, filt=True); nm, dm = axis12(pop, fcell=False)
    print(f'== axis 12 over {lab}: cells × J_c fibre = {d:,} | exact coupling of J_c with the cell\'s f: {n:,} → {100*n/d:.1f}% | filtered on J_c realised: {nf:,} → {100*nf/df:.1f}% | coupling with f_max instead of the cell\'s f: {nm:,} → {100*nm/dm:.1f}%')
n12, d12 = axis12(L10); assert d12 == len(L12)
n13 = sum(2 if c[11] >= 1 else 1 for c in L12)
print(f'== axis 13: realised 2J ∈ {{2K−1, 2K+1}} (one value at 2K = 0): Σ over all {len(L12):,} Λ12 cells = {n13:,} / Λ13 {len(L13):,} → {100*n13/len(L13):.1f}% (printed 64.4) | Λ12 cells with 2K = 0: {sum(1 for c in L12 if c[11]==0):,}')
print(f'== L3084–3085 the six, under the definition: {100*num9/len(L9):.1f}, {100*num9/len(L9p):.1f}, {100*sum(len(v_real(c,"new")) for c in L9)/len(L10):.1f}, {100*n11/len(L11):.1f}, {100*n12/len(L12):.1f}, {100*n13/len(L13):.1f}  (printed 63.7, 67.5, 44.7, 17.0, 31.4, 64.4)')

# ---- independence (L3087–3090): at each axis, stage-below cells whose realised set has ≥ 2 values; the three printed examples
p2 = [c for c in L9 if c[5] == 1 and c[6] == 2 and c[8] == 0]
print(f'== L3087 p²\'s ¹S and ¹D share a Λ9 cell (f = 1, g = 2, 2S′ = 0; {len(p2)} such cells) and split at v: realised v {v_real(p2[0], "new")} (¹S new at 0, ¹D new at 2) | seniority of p² terms: ' + ', '.join(f'{name(t)} v={v}' for v in (0, 2) for t in new_terms(1, v) if t in terms(1, 2)))
p1 = [c for c in L10 if c[1] == 1 and c[2] == 1 and c[7] == 1]
print(f'== L3088 p¹\'s ²P shares a Λ10 cell ({len(p1)} cells with ℓ = 1, k = 1, 2S = 1) and splits at J_c: realised 2J_c {jc_values(1, 1, 1)} | every K > 0 cell of Λ12 splits at J (2 values): {sum(1 for c in L12 if c[11] >= 1):,} cells, {sum(1 for c in L12 if c[11] == 0):,} at K = 0 with one value')
ind = {9: sum(1 for c in L8 if len(spin[(c[5], c[6])]) >= 2), 10: sum(1 for c in L9 if len(v_real(c, 'new')) >= 2), 11: sum(1 for c in L10 if len(jc_values(c[1], c[2], c[7])) >= 2),
       12: sum(1 for c in L11 if k_num(c[10], 2 * c[5]) >= 2), 13: sum(1 for c in L12 if c[11] >= 1)}
print(f'== independence at every axis (stage-below cells whose realised set has ≥ 2 values, i.e. the new coordinate is no function of those below): {ind} of {len(L8)}/{len(L9):,}/{len(L10):,}/{len(L11):,}/{len(L12):,}')

# ---- projection exactness (L3086): every stage projects exactly onto the one below
print(f'== L3086 projections: Λ9→Λ8 {set(c[:8] for c in L9) == set(L8)} | Λ9′→Λ8 {set(c[:8] for c in L9p) == set(L8)} | Λ10→Λ9 {set(c[:9] for c in L10) == set(L9)} | Λ11→Λ10 {set(c[:10] for c in L11) == set(L10)} | Λ12→Λ11 {set(c[:11] for c in L12) == set(L11)} | Λ13→Λ12 {set(c[:12] for c in L13) == set(L12)} (closure E = 0 at all seven stages: r2-ch12n, banked)')

# ---- L3074 "a symbol used 213 times": φ̂ sites
main = r2lib.read_member('The_Method_1_6-2.md')
cnt = {k: r2lib.read_member(v).count('φ̂') for k, v in [('main', 'The_Method_1_6-2.md'), ('reg', 'The_Method_1_6___The_Register-2.md'), ('mc', 'The_Method_1_6___Mathematical_Compendium-2.md'), ('pc', 'The_Method_1_6___The_Physics_Compendium-2.md'), ('ioi', 'The_Method_1_6___The_Index_of_Indices-2.md'), ('sc', 'The_Method_1_6___Spectra_Compendium-2.md')]}
print(f'== L3074 φ̂ occurrences: main {cnt["main"]} (printed 213; lines carrying it {sum(1 for l in main.split(chr(10)) if "φ̂" in l)}); by volume {cnt}; the occupancy sense φ̂(k) {main.count("φ̂(k)")}, the pairwise sense φ̂ᵢⱼ {main.count("φ̂ᵢⱼ")}')

# ---- constraint graph by stage (DEFERRED: L2406–2408, Figure 12.4 caption, Register 1790's 13 nodes / 14 edges)
E8 = [(0, 1), (1, 2), (2, 3), (2, 7), (4, 5), (5, 6), (3, 6)]                       # ℓ ≤ n−1, k ≤ 4ℓ+2, q ≤ k, 2S ≤ k, f ≤ e−1, g ≤ 4f+2, g ≤ q
ADD = {9: [(6, 8)], 10: [(8, 9), (6, 9)], 11: [(2, 10)], 12: [(10, 11)], 13: [(11, 12)]}  # 2S′ ≤ g; 2S′ ≤ v ≤ g; 2J_c ≤ φ̂(k); 2K ≤ 2J_c + 2f_max (f_max the cap, one parent); |2J − 2K| ≤ 1
def graph_stats(nv, edges):
    tri = sum(1 for a, b, c in itertools.combinations(range(nv), 3) if {(a, b), (b, c), (a, c)} <= {tuple(sorted(e)) for e in edges})
    return len(edges), len(edges) - nv + 1, tri, r2lib.is_tree(nv, edges)
for label, bridge in [('as the table\'s bounds define it (f_max a constant)', []), ('with the f–K bridge added (K read with two parents)', [(5, 11)])]:
    rows = []; E = list(E8)
    for d in range(8, 14):
        E = E + ADD.get(d, []) + (bridge if d == 12 else [])
        ne, rank, tri, tree = graph_stats(d, E); rows.append(f'Λ{d}: {d} nodes {ne} edges rank {rank} triangles {tri} tree {tree}')
    print(f'== constraint graph {label}: ' + ' | '.join(rows))
print('   Register 1790 (measured there): 13 nodes, 14 edges, cycle rank 0, 0, 1, 1, 2, 2, one triangle 2S′–g–v from Λ10, second cycle 2Jc–2K–f–g–q–k at Λ12; L3066: the f_max bound "has one parent and preserves the tree"; Figure 12.4 caption: "constraint tree … the forbidden f···K bridge dashed"; L2407: "B runs e–f–g–v–2S′" (no g–2S′ edge named).')

# ---- factorisation over the transfer (§12.11.5 L3463–3477; L3067 "3.5 %"; Figure 12.4 caption "priced at 3.5 %")
A_IDX, B_IDX = (0, 1, 2, 7, 10, 11, 12), (4, 5, 6, 8, 9)
def factor(cells, d):
    a = tuple(i for i in A_IDX if i < d); b = tuple(i for i in B_IDX if i < d)
    byq = defaultdict(list)
    for c in cells: byq[c[3]].append(c)
    sec = [len(byq[q]) for q in range(4)]; prod = [len({tuple(c[i] for i in a) for c in byq[q]}) * len({tuple(c[i] for i in b) for c in byq[q]}) for q in range(4)]
    return sec, prod, sum(prod) - sum(sec)
for d, cells in [(11, L11), (12, L12), (13, L13)]:
    sec, prod, dft = factor(cells, d); print(f'== §12.11.5 factorisation at Λ{d} (loose K): sections {sec} sum {sum(sec):,} | Σ_q |A(q)|·|B(q)| {sum(prod):,} | defect {dft}')
tight12 = [c for c in L12 if c[11] <= c[10] + 2 * c[5]]; tight13 = [c for c in L13 if c[11] <= c[10] + 2 * c[5]]
for d, cells in [(12, tight12), (13, tight13)]:
    sec, prod, dft = factor(cells, d); print(f'== tight two-parent K (2K ≤ 2J_c + 2f, the cell\'s f) at Λ{d}: cells {sum(sec):,} (loose {len(L12) if d == 12 else len(L13):,}; removed {(len(L12) if d == 12 else len(L13)) - sum(sec):,}) | product {sum(prod):,} | defect {dft:,} = {100*dft/sum(prod):.1f}% of the product (§12.11.5 prints {"15,150 / 21.4 %" if d == 12 else "45,450 / 22.8 %"})')
print(f'   the withdrawn 2,475 as a share: of Λ12 {100*2475/len(L12):.2f}% | of the tight-K product at Λ12 {100*2475/sum(factor(tight12, 12)[1]):.2f}% — L3067 and the Figure 12.4 caption print "3.5 %"; §12.11.5 prints 21.4 % / 22.8 %')
