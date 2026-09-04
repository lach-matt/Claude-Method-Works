# r2-ch12r.py — Phase R2, main §12.11.1 second segment (L3092–3135), chat 76.
# (1) L3093 the ninth axis's exact set {g mod 2, g mod 2 + 2, …, min(g, 4f+2−g)} against microstate enumeration for every
#     shell s…f and every occupancy; L3094–3095 p², p³. (2) L3096–3100 Λ₉′: containment min(g, 4f+2−g) ≤ 2f+1, closure by the
#     box sweep and by pairwise joins/meets, the 93 cut cells, the first cycle f–g–2S′. (3) L3102–3119 (Register 249) the
#     closure table: |ℛ(Λ)| against every cell of each stage's ambient box ∏ Âᵢ(Λ), Λ₈ … Λ₁₃ (the 2J coordinate of Λ₁₃'s box
#     is swept as 9 slices over the 5,308,416-cell 12-coordinate grid, so every one of the 47,775,744 cells is decided);
#     the pair counts 2.5 / 19.8 billion. (4) L3121–3124 the four-cap sweep: φ̂ (raw and envelope), fibre non-emptiness (exact
#     projection), |Λ₁₃| by fibre sums and Σ_q |A(q)|·|B(q)|, with explicit enumeration at the first two caps as the control.
# (5) L3126–3134 the density table at four caps by multiplicity weighting (12q-01's parity condition at axis 10).
# terms / new_terms / jc_values lifted verbatim from r2-ch12q.py (chat 76) — owed to r2lib. tower-2.py by path via r2lib. Deterministic.
import importlib.util, os, itertools, math
from collections import Counter, defaultdict
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()

# lifted verbatim from r2-ch12q.py (chat 76)
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
# lifted verbatim from r2-ch12q.py (chat 76)
def new_terms(l, v): return terms(l, v) - terms(l, v - 2) if v >= 2 else terms(l, v)   # multiset difference (L3081)
# lifted verbatim from r2-ch12q.py (chat 76)
def jc_values(l, k, S2): return sorted({j for (s2, L2), _ in terms(l, k).items() if s2 == S2 for j in range(abs(L2 - s2), L2 + s2 + 1, 2)})
_T = {}
def TERMS(l, k):
    if (l, k) not in _T: _T[(l, k)] = terms(l, k)
    return _T[(l, k)]
def spinset(l, g): return sorted({s2 for (s2, _) in TERMS(l, g)})
def formula(l, g): return list(range(g % 2, min(g, 4 * l + 2 - g) + 1, 2))
SYM = {0: 'S', 2: 'P', 4: 'D', 6: 'F'}

# ---- (1) L3093–3095
bad = [(l, g) for l in range(4) for g in range(0, 4 * l + 3) if spinset(l, g) != formula(l, g)]
print(f'== L3093 exact set of the ninth axis = {{g mod 2, …, min(g, 4f+2−g)}}: equals the spin set of f^g by microstate enumeration for every shell s, p, d, f and every occupancy 0 … 4f+2 ({sum(4*l+3 for l in range(4))} cases): {not bad}' + (f' — exceptions {bad}' if bad else ''))
print(f'   L3094–3095 p²: {{{", ".join(f"{t[0]+1}{SYM[t[1]]}" for t in sorted(TERMS(1,2)))}}}, 2S′ ∈ {spinset(1,2)} | p³: {{{", ".join(f"{t[0]+1}{SYM[t[1]]}" for t in sorted(TERMS(1,3)))}}}, 2S′ ∈ {spinset(1,3)}')
print(f'   the seniority ladder at the caps: v ∈ {{g mod 2, …, g}} equals the spin ladder iff g ≤ 2f+1 — at (f, g) with g > 2f+1 (s² only here) the spin ladder stops at 4f+2−g: {[(l, g) for l in (0, 1) for g in range(4) if g <= 4*l+2 and g > 2*l+1]}')

# ---- (2) L3096–3100 Λ₉′
L8, L9 = T.L8(), T.L9(); L9p = [c for c in L9 if c[8] <= 2 * c[5] + 1]
print(f'== L3096 containment min(g, 4f+2−g) ≤ 2f+1 for every (f, g), f ≤ 3, g ≤ 4f+2: {all(min(g, 4*l+2-g) <= 2*l+1 for l in range(4) for g in range(4*l+3))} (min ≤ mean) | Λ9′ {len(L9p):,} cells; cut {len(L9)-len(L9p)}, all (f, g, 2S′) = (0, 2, 2): {all((c[5],c[6],c[8])==(0,2,2) for c in L9 if c[8] > 2*c[5]+1)}')
nn, jl, ml = r2lib.closure(L9p)
print(f'   Λ9′ closure by pairwise joins/meets on all {nn:,} ordered pairs: join failures {jl}, meet failures {ml} → E = {jl+ml}')
def Rbox(X, extra_slices=None):
    """|ℛ(X)| by sweeping every cell of the ambient box ∏ Âᵢ(X): x ∈ ℛ(X) iff xᵢ ≤ φ̂ᵢⱼ(xⱼ) for all i ≠ j (§6.1 L1540)."""
    A = np.array(X, dtype=np.int64); d = A.shape[1]; vals = [np.unique(A[:, i]) for i in range(d)]
    phi = {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            m = np.full(int(A[:, j].max()) + 1, -1, dtype=np.int64)
            for v in vals[j]: m[v] = A[A[:, j] <= v, i].max()
            phi[(i, j)] = m
    box = int(np.prod([len(v) for v in vals]))
    if extra_slices is None:
        G = np.array(np.meshgrid(*vals, indexing='ij')).reshape(d, -1).T
        ok = np.ones(len(G), dtype=bool)
        for (i, j), m in phi.items(): ok &= G[:, i] <= m[G[:, j]]
        return box, int(ok.sum()), set(map(tuple, G[ok])) == set(map(tuple, A))
    # sweep the last coordinate as slices over the grid of the first d−1 (decides every cell of the box)
    G = np.array(np.meshgrid(*vals[:-1], indexing='ij')).reshape(d - 1, -1).T
    ok0 = np.ones(len(G), dtype=bool)
    for (i, j), m in phi.items():
        if i < d - 1 and j < d - 1: ok0 &= G[:, i] <= m[G[:, j]]
    total = 0; inX = 0; Xs = set(map(tuple, A))
    for v in vals[-1]:
        ok = ok0.copy()
        for i in range(d - 1): ok &= (v <= phi[(d - 1, i)][G[:, i]]) & (G[:, i] <= phi[(i, d - 1)][v])
        total += int(ok.sum()); inX += sum(1 for row in G[ok] if tuple(row) + (int(v),) in Xs)
    return box, total, inX == total == len(Xs)
box, r, same = Rbox(L9p); print(f'   Λ9′ by the box sweep: ambient box {box:,} cells, |ℛ(Λ9′)| = {r:,}, ℛ(Λ9′) = Λ9′ {same}, E = {r-len(L9p)}')
E9p = [(0, 1), (1, 2), (2, 3), (2, 7), (4, 5), (5, 6), (3, 6), (6, 8), (5, 8)]     # Λ₈'s seven + g–2S′ + f–2S′
tri = [t for t in itertools.combinations(range(9), 3) if all(tuple(sorted(e)) in {tuple(sorted(x)) for x in E9p} for e in itertools.combinations(t, 2))]
NM = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S', '2S′']
print(f'   L3098 Λ9′\'s constraint graph: 9 nodes {len(E9p)} edges, tree {r2lib.is_tree(9, E9p)}, cycle rank {len(E9p)-9+1}, triangle(s) {["–".join(NM[i] for i in t) for t in tri]}')

# ---- (3) L3102–3119 the closure table, every stage against every cell of its ambient box
rows = []
for d, X in [(8, L8), (9, L9), (10, T.L10()), (11, T.L11()), (12, T.L12())]:
    box, r, same = Rbox(X); rows.append((d, len(X), r, box, same))
L13 = T.L13(); box, r, same = Rbox(L13, extra_slices=True); rows.append((13, len(L13), r, box, same))
print('== L3108–3114 stage |Λ| |ℛ(Λ)| E ambient-box-swept ℛ(Λ)=Λ:')
for d, n, r, box, same in rows: print(f'   Λ{d:<3} {n:>8,} {r:>8,} {r-n:>3} {box:>12,}  {same}')
print(f'   L3103 pairs: Λ12 C(70,905, 2) = {math.comb(70905, 2):,} ({math.comb(70905,2)/1e9:.1f} billion) | Λ13 C(199,130, 2) = {math.comb(199130, 2):,} ({math.comb(199130,2)/1e9:.1f} billion) | ambient box = product of the value-set sizes: ' + ' · '.join(str(len(np.unique(np.array(L13)[:, i]))) for i in range(13)) + f' = {int(np.prod([len(np.unique(np.array(L13)[:, i])) for i in range(13)])):,}')

# ---- (4) L3121–3124 the four-cap sweep — the tower at caps (n_max, e_max, ℓ_max, k_max, f_max) (L1800's order)
def L8_at(caps):
    n_max, e_max, l_max, k_max, f_max = caps
    return [(n, l, k, q, e, f, g, S2) for n in range(1, n_max + 1) for l in range(0, min(l_max, n - 1) + 1) for k in range(1, min(k_max, 4 * l + 2) + 1)
            for q in range(0, k + 1) for e in range(1, e_max + 1) for f in range(0, min(f_max, e - 1) + 1) for g in range(0, min(4 * f + 2, q) + 1) for S2 in range(0, k + 1)]
def phi_at(caps):
    n_max, e_max, l_max, k_max, f_max = caps
    raw = {k: max(L2 + s2 for l in range(l_max + 1) if k <= 4 * l + 2 for (s2, L2) in TERMS(l, k)) for k in range(1, k_max + 1)}
    env = {}; run = 0
    for k in range(1, k_max + 1): run = max(run, raw[k]); env[k] = run
    return raw, env
def fibres(caps, env):
    f_max = caps[4]
    B10 = lambda g: sum(g - s + 1 for s in range(g + 1))                                  # |{(2S′, v)}| over a Λ₈ cell
    A13 = lambda k: sum(3 if K2 >= 1 else 2 for jc in range(env[k] + 1) for K2 in range(jc + 2 * f_max + 1))   # |{(2J_c, 2K, 2J)}|
    return B10, A13
def tower_counts(caps):
    raw, env = phi_at(caps); B10, A13 = fibres(caps, env); L8c = L8_at(caps)
    direct = sum(B10(c[6]) * A13(c[2]) for c in L8c)
    Aq = defaultdict(set); Bq = defaultdict(set)
    for c in L8c: Aq[c[3]].add((c[0], c[1], c[2], c[7])); Bq[c[3]].add((c[4], c[5], c[6]))
    prod = sum(sum(A13(a[2]) for a in Aq[q]) * sum(B10(b[2]) for b in Bq[q]) for q in Aq)
    return raw, env, len(L8c), direct, prod
def L13_explicit(caps):
    raw, env = phi_at(caps); f_max = caps[4]
    return sum(1 for c in L8_at(caps) for s2p in range(0, c[6] + 1) for v in range(s2p, c[6] + 1) for jc in range(0, env[c[2]] + 1) for K2 in range(0, jc + 2 * f_max + 1) for J2 in range(max(0, K2 - 1), K2 + 2))
print('== L3121–3124 the four-cap sweep (n_max, e_max, ℓ_max, k_max, f_max):')
for caps, printed in [((3, 3, 1, 3, 1), 199130), ((4, 4, 2, 4, 1), 4731790), ((4, 4, 2, 6, 2), 40310170), ((5, 5, 2, 6, 2), 77083771)]:
    raw, env, n8, direct, prod = tower_counts(caps)
    ctrl = f', explicit enumeration {L13_explicit(caps):,}' if caps[3] <= 4 else ''
    print(f'   {caps}: Λ8 {n8:,} | φ̂ raw {list(raw.values())} monotone {list(raw.values()) == sorted(raw.values())}, envelope {list(env.values())} monotone True | every fibre non-empty (2S′: g+1 ≥ 1; v: g−2S′+1 ≥ 1; 2J_c: φ̂+1; 2K: 2J_c+2f_max+1; 2J: ≥ 2) so every stage projects exactly | Λ13 by fibre sums {direct:,}{ctrl} | Σ_q |A(q)|·|B(q)| {prod:,} | defect {prod-direct} | printed {printed:,} {"OK" if direct == printed else "MISMATCH"}')

# ---- (5) L3126–3134 the density table by multiplicity weighting
def densities(caps):
    raw, env = phi_at(caps); f_max = caps[4]; L8c = L8_at(caps)
    def v_real(f, g, s2p): return [v for v in range(s2p, g + 1) if (g - v) % 2 == 0 and any(s2 == s2p for (s2, _) in new_terms(f, v))]
    num10 = {}; B10 = {}; A11 = {}; num12 = {}; den12 = {}; num13 = {}; den13 = {}
    for g in range(0, 4 * f_max + 3): B10[g] = sum(g - s + 1 for s in range(g + 1))
    for f in range(f_max + 1):
        for g in range(0, min(4 * f + 2, caps[3]) + 1): num10[(f, g)] = sum(len(v_real(f, g, s)) for s in range(g + 1))
    for k in range(1, caps[3] + 1):
        A11[k] = env[k] + 1
        den13[k] = sum(3 if K2 >= 1 else 2 for jc in range(env[k] + 1) for K2 in range(jc + 2 * f_max + 1)); num13[k] = sum(2 if K2 >= 1 else 1 for jc in range(env[k] + 1) for K2 in range(jc + 2 * f_max + 1))
        for f in range(f_max + 1): den12[(k, f)] = sum(jc + 2 * f_max + 1 for jc in range(env[k] + 1)); num12[(k, f)] = sum(min(jc, 2 * f) + 1 for jc in range(env[k] + 1))
    n = [0.0] * 6; dn = [0.0] * 6
    for c in L8c:
        l, k, f, g, S2 = c[1], c[2], c[5], c[6], c[7]; w = B10[g]
        n[0] += len(spinset(f, g)); dn[0] += g + 1
        n[1] += len(spinset(f, g)); dn[1] += min(g, 2 * f + 1) + 1
        n[2] += num10[(f, g)]; dn[2] += B10[g]
        n[3] += w * len(jc_values(l, k, S2)); dn[3] += w * A11[k]
        n[4] += w * num12[(k, f)]; dn[4] += w * den12[(k, f)]
        n[5] += w * num13[k]; dn[5] += w * den13[k]
    return [100 * a / b for a, b in zip(n, dn)], int(dn[1]), int(dn[5])
print('== L3130–3134 densities by multiplicity weighting (axis 10 with 12q-01\'s parity condition):')
for caps, printed in [((3, 3, 1, 3, 1), (63.7, 67.5, 44.7, 17.0, 31.4, 64.4)), ((4, 4, 1, 6, 1), (54.2, 60.3, 33.2, 7.0, 36.7, 64.5)), ((5, 5, 2, 10, 2), (49.4, 55.6, 28.4, 4.9, 28.2, 65.7)), ((5, 5, 3, 14, 3), (46.6, 53.0, 25.9, 4.2, 22.4, 66.1))]:
    dens, n9p, n13 = densities(caps); r1 = tuple(round(x, 1) for x in dens)
    print(f'   {caps}: {" ".join(f"{x:5.1f}" for x in dens)} | printed {" ".join(f"{x:5.1f}" for x in printed)} | {"all six reproduce" if r1 == printed else "differs at axes " + str([9, "9′", 10, 11, 12, 13][i] for i in range(6) if r1[i] != printed[i]) if False else ("all six reproduce" if r1 == printed else "differs at " + ", ".join(str(["9", "9′", "10", "11", "12", "13"][i]) for i in range(6) if r1[i] != printed[i]))} | Λ9′ {n9p:,} · Λ13 {n13:,} cells')
