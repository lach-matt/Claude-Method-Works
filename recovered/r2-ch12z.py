# r2-ch12z.py — Phase R2, main §12.11.3 "The dichotomy" (L3394–3408), chat 78.
# Measured: the dichotomy's two halves — every counting coordinate's realised values fill its bound interval at every
# parent value of Λ₈ (close exactly), while the first coupling constraint 2S ≤ k admits more than the physics realises
# (closes as an envelope; the spin set of ℓᵏ by microstate enumeration) — L3395–3396 and the §7.1 origins-table claim
# (L3398–3399); E(Λ₈) = E(Λ₉) = 0 by the ambient-box sweep (the closure sense of "exact", the 12e-05 disposition's
# first pillar; the bound sense is r2-ch12y's axis-9 gap 16 admitted / 9 realised); the §7.1 table's row and origin
# counts against L3398's "four rows"; the Spectra Compendium Part II channel table counted from its own rows against
# the printed 596 / 477 / 119 / 28 / 70 / 3,342 / 2,269 / 1,577 of 1,738 on 392 / 78 no-triple / 126 untested —
# the current record behind L3406's record-carried "153 channels" (registers 630–631; B.2's disclosed drift).
# tower-2.py by path via r2lib. Deterministic (no wall-clock).
import importlib.util, os, itertools, re
from collections import Counter
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py')); r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib); T = r2lib.load_tower()

# lifted verbatim from r2-ch12q.py (chat 76) — LS terms of ℓ^k by microstate enumeration (L3059–3063)
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

# lifted verbatim from r2-ch12r.py (chat 76) — |ℛ(X)| by sweeping every cell of the ambient box
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

L8, L9 = T.L8(), T.L9()

# ---- L3395 "Counting coordinates close exactly": each counting bound's interval is filled at every parent value of Λ8
print('== L3395 counting coordinates — realised values against the bound interval, over every parent value of Λ8:')
def fills(pairs, lab):
    ok = all(sorted(v) == list(range(min(v), max(v) + 1)) and (min(v), max(v)) == b for v, b in pairs)
    print(f'   {lab}: full interval at every parent value {ok}')
by = lambda key, val: [(sorted({val(c) for c in L8 if key(c) == kv}), kv) for kv in sorted({key(c) for c in L8})]
NMAX, EMAX, LMAX, KMAX, FMAX = 3, 3, 1, 3, 1
fills([(v, (0, min(LMAX, kv - 1))) for v, kv in by(lambda c: c[0], lambda c: c[1])], 'ℓ ≤ n−1        (per n)')
fills([(v, (1, min(KMAX, 4 * kv + 2))) for v, kv in by(lambda c: c[1], lambda c: c[2])], 'k ≤ 2(2ℓ+1)    (per ℓ)')
fills([(v, (0, kv)) for v, kv in by(lambda c: c[2], lambda c: c[3])], 'q ≤ k          (per k)')
fills([(v, (0, min(FMAX, kv - 1))) for v, kv in by(lambda c: c[4], lambda c: c[5])], 'f ≤ e−1        (per e)')
fills([(v, (0, min(4 * kv[0] + 2, kv[1]))) for v, kv in by(lambda c: (c[5], c[3]), lambda c: c[6])], 'g ≤ 2(2f+1), g ≤ q (per (f,q))')

# ---- L3395–3396 "Coupling coordinates close as envelopes. ... the first coupling constraint was already in §7.1":
# 2S ≤ k admits, the spin set of ℓᵏ realises
print('== L3395–3396 the first coupling constraint 2S ≤ k (§7.1 row 7) — admitted vs the spin set of ℓᵏ:')
adm = rea = 0
for (l, k) in sorted({(c[1], c[2]) for c in L8}):
    sp = sorted({s2 for (s2, _) in terms(l, k)})
    adm += k + 1; rea += len(sp)
    print(f'   (ℓ,k)=({l},{k}): admitted [0..{k}] ({k+1}), physics realises {sp} ({len(sp)})')
print(f'   TOTAL admitted {adm}, realised {rea} — an envelope with gap {adm - rea}: the coupling half of the dichotomy, measured')

# ---- 12e-05 disposition, closure sense: E = 0 by the ambient-box sweep at Λ8 and Λ9
for X, lab, exp in [(L8, 'Λ8', 976), (L9, 'Λ9', 1654)]:
    box, r, eq = Rbox(X)
    print(f'== E({lab}) by the box sweep: ambient {box:,} | |ℛ| {r:,} | ℛ(X) = X {eq} | E = {r - len(X)}   (|{lab}| {len(X):,}, expected {exp:,})')

# ---- L3398 "The origins table of Chapter 7 has four rows" — the printed table counted
M = r2lib.read_member('The_Method_1_6-2.md').split('\n')
rows = [M[i] for i in range(1753, 1760)]
origins = []
for r in rows:
    o = r.split(None, 1)[1] if '≤' in r.split()[0] else re.split(r'\s{2,}', r.strip(), 1)[1]
    origins.append(o.strip())
canon = sorted({('hydrogenic' if 'hydrogenic' in o else 'Pauli' if 'Pauli' in o else 'counting' if 'counting' in o else 'vector coupling') for o in origins})
print(f'== L3398 §7.1 table (L1754–1760): constraint rows {len(rows)} | distinct origins {len(canon)} {canon} | L1762 states "Seven constraints, four origins"')

# ---- L3406 "all 153 channels" — record-carried (registers 630–631); the current record counted from the SC's own table
S = r2lib.read_member('The_Method_1_6___Spectra_Compendium-2.md').split('\n')
stop = next(i for i, l in enumerate(S) if '596 channel rows across' in l)
crows = []
for l in S[:stop]:
    if l.startswith('|'):
        f = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(f) == 11 and f[0] not in ('species',) and not set(f[0]) <= {'-', ' '}: crows.append(f)
lv = [int(r[3]) for r in crows]; ic = [int(r[4]) for r in crows]
br = [r[5] for r in crows]
bt = [tuple(int(x.replace(',', '')) for x in b.split('/')) for b in br if '/' in b]
nt = sum(1 for b in br if 'no-triple' in b); ut = sum(1 for b in br if 'untested' in b)
species = sorted({r[0] for r in crows}); elements = sorted({r[0].split()[0] for r in crows})
print(f'== L3406/L10169/SC L994 — SC Part II channel table, counted from its own rows:')
print(f'   rows {len(crows)} (printed 596) | series ≥ 3 members {sum(1 for x in lv if x >= 3)} (477) | two-member {sum(1 for x in lv if x == 2)} (119)')
print(f'   elements {len(elements)} (28) | species {len(species)} (70) | levels {sum(lv):,} (3,342) | interior cells {sum(ic):,} (2,269)')
print(f'   bracket rows {len(bt)} (392): {sum(a for a, b in bt):,} of {sum(b for a, b in bt):,} (1,577 of 1,738) | no-triple {nt} (78) | untested {ut} (126)')
print(f'   L3406\'s "all 153 channels" has no current table: the first collection\'s count, record-carried per B.2\'s disclosure (main L10203–10208; registers 630–631, 1578, 1699–1700)')
