# r2-ch12s.py — Phase R2, main §12.11.1 third segment (L3136–3176), chat 76.
# (1) L3137–3140 "every density except the thirteenth falls" tested on the referee table's 24 entries (record-carried from
#     r2-ch12r, where all 24 reproduce) and on 12r-01's corrected axis-10 column. (2) L3140–3143 the thirteenth's rise and the
#     ⅔ limit: density₁₃ = (2N − N₀)/(3N − N₀) with N₀ the K = 0 cells of Λ₁₂, the K = 0 share by multiplicity weighting at the
#     four caps. (3) L3152–3154 / §12.11.4: the J-set of every (2J_c, f) channel through K and direct; the J-fibre density
#     through K (axis 13) and direct (J taken after axis 11); the 25 points. (4) L3158–3159 every f = 0 channel's K-set is the
#     singleton {2J_c}; L3167–3168 the J doublet except at K = 0. (5) L3148–3150 the exact ninth and tenth objects (realised
#     spins only; realised seniorities only, with v ≡ g mod 2 and v ≤ 4f+2−g) — closure by pairwise joins/meets and by ℛ's box
#     sweep: is the obstruction outside the language. (6) L3152–3156 the J_c–J pair under the table's bounds (no direct edge;
#     the would-be admissible bound 2J_c ≤ 2J + 2f_max + 1 counted against every cell of Λ₁₃).
# terms/new_terms lifted verbatim from r2-ch12q.py; L8_at/phi_at/TERMS lifted verbatim from r2-ch12r.py (chat 76) — owed to r2lib. Deterministic.
import importlib.util, os, itertools
from collections import Counter, defaultdict
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()
PHI, FMAX = T.PHI, T.FMAX

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
# lifted verbatim from r2-ch12r.py (chat 76)
_T = {}
def TERMS(l, k):
    if (l, k) not in _T: _T[(l, k)] = terms(l, k)
    return _T[(l, k)]
# lifted verbatim from r2-ch12r.py (chat 76)
def L8_at(caps):
    n_max, e_max, l_max, k_max, f_max = caps
    return [(n, l, k, q, e, f, g, S2) for n in range(1, n_max + 1) for l in range(0, min(l_max, n - 1) + 1) for k in range(1, min(k_max, 4 * l + 2) + 1)
            for q in range(0, k + 1) for e in range(1, e_max + 1) for f in range(0, min(f_max, e - 1) + 1) for g in range(0, min(4 * f + 2, q) + 1) for S2 in range(0, k + 1)]
# lifted verbatim from r2-ch12r.py (chat 76)
def phi_at(caps):
    n_max, e_max, l_max, k_max, f_max = caps
    raw = {k: max(L2 + s2 for l in range(l_max + 1) if k <= 4 * l + 2 for (s2, L2) in TERMS(l, k)) for k in range(1, k_max + 1)}
    env = {}; run = 0
    for k in range(1, k_max + 1): run = max(run, raw[k]); env[k] = run
    return raw, env

# ---- (1) monotonicity over the referee table (L3130–3134; every entry reproduced by r2-ch12r)
CAPS = [(3, 3, 1, 3, 1), (4, 4, 1, 6, 1), (5, 5, 2, 10, 2), (5, 5, 3, 14, 3)]
TAB = {'9': [63.7, 54.2, 49.4, 46.6], '9′': [67.5, 60.3, 55.6, 53.0], '10': [44.7, 33.2, 28.4, 25.9], '11': [17.0, 7.0, 4.9, 4.2], '12': [31.4, 36.7, 28.2, 22.4], '13': [64.4, 64.5, 65.7, 66.1]}
TAB10c = [44.7, 31.9, 26.0, 22.9]   # 12r-01's corrected axis-10 column
fall = {a: all(x > y for x, y in zip(v, v[1:])) for a, v in TAB.items()}; rise = {a: all(x < y for x, y in zip(v, v[1:])) for a, v in TAB.items()}
print(f'== L3137–3140 over the four caps: strictly falling {[a for a in TAB if fall[a]]}, strictly rising {[a for a in TAB if rise[a]]}, neither {[a for a in TAB if not fall[a] and not rise[a]]} — axis 12 goes {TAB["12"]} (up {TAB["12"][1]-TAB["12"][0]:+.1f} at the first enlargement, then down); axis 10 corrected (12r-01) {TAB10c} falling {all(x > y for x, y in zip(TAB10c, TAB10c[1:]))}')

# ---- (2) the thirteenth's rise and the ⅔ limit via the K = 0 share
print('== L3140–3143 density₁₃ = (2N − N₀)/(3N − N₀), N₀ = the K = 0 cells of Λ₁₂:')
for caps, printed in zip(CAPS, TAB['13']):
    raw, env = phi_at(caps); f_max = caps[4]; B10 = lambda g: (g + 1) * (g + 2) // 2
    N = N0 = 0
    for c in L8_at(caps):
        w = B10(c[6]); k = c[2]; N0 += w * (env[k] + 1); N += w * sum(jc + 2 * f_max + 1 for jc in range(env[k] + 1))
    print(f'   {caps}: Λ12 {N:,}, K = 0 cells {N0:,} = {100*N0/N:.1f}% → density₁₃ {100*(2*N-N0)/(3*N-N0):.1f}% (printed {printed}); with no K = 0 cell the value would be {100*2/3:.1f}%')
print('   the nominal ⅔ and its attribution to the K = 0 singlet have no site in §12.11.1 (L3032–3176) or elsewhere in the main member except L3141–3142 itself (grep ⅔, "K = 0 singlet"): record-carried from the read')

# ---- (3) §12.11.4 through L3152–3154: the J-set of a channel through K and direct
L11, L12, L13 = T.L11(), T.L12(), T.L13()
def Jset_viaK(jc2, f2): return sorted({j for K2 in range(abs(jc2 - f2), jc2 + f2 + 1, 2) for j in (K2 - 1, K2 + 1) if j >= 0})
def Jset_direct(jc2, f2): return list(range(abs(jc2 - f2 - 1), jc2 + f2 + 2, 2))
pairs = [(jc2, f) for jc2 in range(0, 6) for f in (0, 1)]
same = sum(1 for jc2, f in pairs if Jset_viaK(jc2, 2 * f) == Jset_direct(jc2, 2 * f))
print(f'== §12.11.4 (L3458–3460) recoupling: the J-set through K equals the direct J-set in {same} of {len(pairs)} (2J_c, f) pairs')
num_d = sum(len(Jset_direct(c[10], 2 * c[5])) for c in L11); den_d = sum(c[10] + 2 * FMAX + 2 for c in L11)
num_K = sum(2 if c[11] >= 1 else 1 for c in L12); den_K = len(L13)
print(f'   J-fibre density through K (axis 13 over Λ12): {num_K:,}/{den_K:,} = {100*num_K/den_K:.1f}% | direct (J after axis 11, bound 2J ≤ 2J_c + 2f_max + 1 over Λ11): {num_d:,}/{den_d:,} = {100*num_d/den_d:.1f}% | L3153 "25 points": {100*num_K/den_K - 100*num_d/den_d:.1f} (printed 64.4 / 39.4)')

# ---- (4) L3158–3159 and L3167–3168
f0 = [c for c in L11 if c[5] == 0]
print(f'== L3158 f = 0 channels of Λ11: {len(f0):,} cells; realised K-set = {{2J_c}} (one value) in all: {all(list(range(abs(c[10]), c[10]+1, 2)) == [c[10]] for c in f0)} | L3167 J-fibre a doublet at K > 0 ({sum(1 for c in L12 if c[11] >= 1):,} cells), a singleton at K = 0 ({sum(1 for c in L12 if c[11] == 0):,})')

# ---- (5) the exact ninth and tenth objects (realised values only) — closure
L8, L9, L10 = T.L8(), T.L9(), T.L10()
spin = {(l, g): sorted({s2 for (s2, _) in TERMS(l, g)}) for l in (0, 1) for g in range(4)}
X9 = [c + (s2,) for c in L8 for s2 in spin[(c[5], c[6])]]
def v_real(f, g, s2p): return [v for v in range(s2p, g + 1) if (g - v) % 2 == 0 and v <= 4 * f + 2 - g and any(x == s2p for (x, _) in new_terms(f, v))]
X10 = [c + (v,) for c in X9 for v in v_real(c[5], c[6], c[8])]
def Rbox(X):
    A = np.array(X, dtype=np.int64); d = A.shape[1]; vals = [np.unique(A[:, i]) for i in range(d)]; phi = {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            m = np.full(int(A[:, j].max()) + 1, -1, dtype=np.int64)
            for v in vals[j]: m[v] = A[A[:, j] <= v, i].max()
            phi[(i, j)] = m
    G = np.array(np.meshgrid(*vals, indexing='ij')).reshape(d, -1).T; ok = np.ones(len(G), dtype=bool)
    for (i, j), m in phi.items(): ok &= G[:, i] <= m[G[:, j]]
    return int(ok.sum())
for name, X, note in [('Λ9-exact (realised spins only)', X9, 'the parity g mod 2 and the ceiling min(g, 4f+2−g)'), ('Λ10-exact (realised seniorities only)', X10, 'v ≡ g mod 2 and v ≤ 4f+2−g')]:
    nn, jl, ml = r2lib.closure(X); r = Rbox(X)
    print(f'== L3148–3150 {name}: {len(X):,} cells | pairwise closure on {nn:,} ordered pairs: join failures {jl:,}, meet failures {ml:,} | |ℛ(X)| = {r:,} (E = {r-len(X):,}): the exact set is {"" if r == len(X) else "not "}expressible by pairwise bounds — the obstruction is {note}')

# ---- (6) L3152–3156 the J_c–J pair under the table's bounds
viol = sum(1 for c in L13 if c[10] > c[12] + 2 * FMAX + 1); hold = all(c[12] <= c[10] + 2 * FMAX + 1 for c in L13)
print(f'== L3152–3156 the table\'s bounds give K the parent J_c only (L3038, L3066) and J the parent K only (L3039): no J_c–J edge, the 11–12–13 path is not a cycle (READ-ch12q B: 13 edges, one triangle 2S′–g–v) | on every cell of Λ13 the implied 2J ≤ 2J_c + 2f_max + 1 holds: {hold}; the would-be admissible converse 2J_c ≤ 2J + 2f_max + 1 fails on {viol:,} of {len(L13):,} cells — "all admissible bounds" (L3154) names an object smaller than Λ13')
