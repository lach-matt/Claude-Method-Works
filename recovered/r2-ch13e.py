#!/usr/bin/env python3
# r2-ch13e.py — Phase R2, chat 80, segment 1: main §12.11.8 (L3543-3625), the electromagnetic index.
# Re-measures on the rebuilt tower:
#   (1) the image table of Λ₉ under (multipole, ΔS), both signed and absolute readings; 576 E1 with ΔS≠0.
#   (2) the spin rule σ⁻¹({0}) — cell count and E = |R(X)| − |X|; and why E = 0 is structural.
#   (3) the parity rule δ⁻¹({−1,+1}) — cell count and E.
#   (4) the adjunction of electromagnetic coordinates to Λ₉ — E under every candidate reading.
#   (5) the transit condition 2S′ ≤ g, and the shared bits between the electromagnetic and
#       composability predicates against the printed 0.0004 of a possible 0.633.
#   (6) the four cap settings 1,654 / 2,664 / 44,153 / 60,164 and the image rectangle at (5,5,3,10,3).
#   (7) the four coupling schemes: the 2.17 spread of the printed counts, and the J multiset
#       identity across the jK, LS, LK and jj chains on every two-electron configuration to f.
# No wall-clock output.
import importlib.util, os, itertools, math
from collections import Counter, defaultdict
import numpy as np

H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()

n_, l_, k_, q_, e_, f_, g_, S_, Sp_ = range(9)
L9 = T.L9()

# ---- generalises r2-ch13c.py's R(X) (chat 79) from a two-coordinate index to any width; owed to r2lib ----
def Rn(X, cap=400000):
    """Join-and-meet closure to a fixed point on tuples of any width. E(X) = |Rn(X)| − |X|."""
    A = np.unique(np.array(sorted(X), dtype=np.int64), axis=0)
    rad = A.max(axis=0) + 1; w = np.cumprod(np.concatenate(([1], rad[:-1]))).astype(np.int64)
    keys = np.sort(A @ w)
    while True:
        new = []
        CH = max(1, 2_000_000 // max(1, len(A)))
        for i in range(0, len(A), CH):
            B = A[i:i + CH]
            for Z in (np.maximum(B[:, None, :], A[None, :, :]).reshape(-1, A.shape[1]),
                      np.minimum(B[:, None, :], A[None, :, :]).reshape(-1, A.shape[1])):
                zk = Z @ w
                m = ~np.isin(zk, keys)
                if m.any(): new.append(np.unique(Z[m], axis=0))
        if not new: return A
        A = np.unique(np.concatenate([A] + new), axis=0)
        assert len(A) <= cap, 'closure exceeded cap'
        keys = np.sort(A @ w)

def E(X):
    return len(Rn(X)) - len(set(map(tuple, X)))

def dl(c): return c[f_] - c[l_]
def ds(c): return c[Sp_] - c[S_]

def multipole(c):
    """L3557: Δℓ = 0 → M1, 1 → E1, 2 → E2, 3 → E3, the lowest whose parity matches."""
    return {0: 'M1', 1: 'E1', 2: 'E2', 3: 'E3'}[abs(dl(c))]

print('=== (1) L3561-3565: the image of Λ₉ under (multipole, ΔS) ===')
print('|Λ₉| =', len(L9))
for tag, key in (('|Δℓ| and |ΔS| (absolute)', lambda c: (multipole(c), abs(ds(c)))),
                 ('|Δℓ| and signed ΔS', lambda c: (multipole(c), ds(c)))):
    img = Counter(key(c) for c in L9)
    cols = sorted({v for _, v in img}); rows = sorted({m for m, _ in img})
    print('  reading:', tag, '— image cells', len(img), '(%d × %d)' % (len(rows), len(cols)))
    print('    multipole | ' + ' | '.join('ΔS=%s' % c for c in cols))
    for m in rows:
        print('    %-9s | ' % m + ' | '.join('%6d' % img.get((m, c), 0) for c in cols))
print('  printed E1 row 264 342 180 54 ; M1 row 262 337 171 44 ; sum 1,654')
print('  L3572 "576 of its Λ₉ cells are E1 with ΔS ≠ 0" measured:',
      sum(1 for c in L9 if multipole(c) == 'E1' and ds(c) != 0),
      '(signed) /', sum(1 for c in L9 if multipole(c) == 'E1' and abs(ds(c)) != 0), '(absolute)')
print('  Δℓ support', sorted({dl(c) for c in L9}), ' ΔS support', sorted({ds(c) for c in L9}))
print('  E of the image (a full box closes for free):', E([(0 if multipole(c) == 'M1' else 1, abs(ds(c))) for c in L9]))

print()
print('=== (2) L3578: the spin rule ΔS = 0, σ⁻¹({0}) imposed on Λ₉ ===')
S0 = [c for c in L9 if ds(c) == 0]
print('cells', len(S0), ' E =', E(S0), '  (printed 526 cells, E = 0)')
print('structural: 2S′ = 2S is preserved by coordinatewise max and min, and E(Λ₉) = 0,')
print('so the spin set closes at any cap where Λ₉ does — the four-cap claim needs no new sweep.')

print()
print('=== (3) L3579: the parity rule |Δℓ| = 1, δ⁻¹({−1,+1}) imposed on Λ₉ ===')
P = [c for c in L9 if abs(dl(c)) == 1]
RP = Rn(P)
print('cells', len(P), ' |R(X)| =', len(RP), ' E =', len(RP) - len(P), '  (printed 840 cells, E = 750)')
print('the hole is filled straight back in — Δℓ values in R(X):',
      sorted(Counter(int(r[f_]) - int(r[l_]) for r in RP).items()))

print()
print('=== (4) L3586-3587: adjoining the electromagnetic coordinates to Λ₉ ===')
MP = {'M1': 0, 'E1': 1, 'E2': 2, 'E3': 3}
CAND = {
    'Δℓ, ΔS (signed)':        lambda c: (dl(c), ds(c)),
    '|Δℓ|, |ΔS|':             lambda c: (abs(dl(c)), abs(ds(c))),
    'multipole, |ΔS|':        lambda c: (MP[multipole(c)], abs(ds(c))),
    'multipole, ΔS (signed)': lambda c: (MP[multipole(c)], ds(c)),
    'Δℓ, ΔS, multipole':      lambda c: (dl(c), ds(c), MP[multipole(c)]),
    '|Δℓ|, |ΔS|, multipole':  lambda c: (abs(dl(c)), abs(ds(c)), MP[multipole(c)]),
}
print('E(Λ₉) =', E(L9), ' (printed 0)')
for tag, fn in CAND.items():
    X = [tuple(c) + tuple(v - min(0, min(fn(d)[i] for d in L9)) if False else v for i, v in enumerate(fn(c))) for c in L9]
    # shift each adjoined coordinate to a non-negative range without changing the order
    cols = list(zip(*[fn(c) for c in L9])); off = [min(col) for col in cols]
    X = [tuple(c) + tuple(v - off[i] for i, v in enumerate(fn(c))) for c in L9]
    print('  %-24s E = %6d' % (tag, E(X)), ' (printed 3,900)')

print()
print('=== (5) L3591-3592: the transit condition, and the shared bits ===')
tr = [1 if c[Sp_] <= c[g_] else 0 for c in L9]
print('2S′ ≤ g admits', sum(tr), 'cells  (printed 1,169)')
def Hb(xs):
    cnt = Counter(xs); N = len(xs)
    return -sum(v / N * math.log2(v / N) for v in cnt.values())
PRED = {
    'E1 (|Δℓ| = 1)':            [1 if abs(dl(c)) == 1 else 0 for c in L9],
    'spin rule (ΔS = 0)':       [1 if ds(c) == 0 else 0 for c in L9],
    'E1 and ΔS = 0':            [1 if abs(dl(c)) == 1 and ds(c) == 0 else 0 for c in L9],
    'image (multipole, |ΔS|)':  [(multipole(c), abs(ds(c))) for c in L9],
}
print('  transit predicate entropy %.4f bits' % Hb(tr))
for tag, p in PRED.items():
    print('  %-24s H = %.4f  MI with transit = %.4f  min(H) = %.4f  (printed 0.0004 of 0.633)'
          % (tag, Hb(p), r2lib.mi(p, tr), min(Hb(p), Hb(tr))))

print()
print('=== (6) L3568, L3581: the caps ===')
CAPSETS = [(3, 3, 1, 3, 1), (5, 5, 3, 10, 3), (4, 4, 2, 6, 2), (3, 3, 2, 3, 2), (4, 3, 1, 3, 1)]
for caps in CAPSETS:
    X = r2lib.build9(caps)
    img = Counter((multipole(c), abs(ds(c))) for c in X)
    rows = {m for m, _ in img}; cols = {v for _, v in img}
    print('  caps %-16s |Λ₉| = %7d   image %d × %d = %d cells' %
          (str(caps), len(X), len(rows), len(cols), len(img)))
print('  printed cap sizes for the spin rule: 1,654 / 2,664 / 44,153 / 60,164 (MC L1376: from the record)')

print()
print('=== (7) L3597-3617: four schemes, one object ===')
CNT = {'jK': 199130, 'LK': 341150, 'LS': 431050, 'jj': 206520}
print('printed Λ₁₃ counts', CNT, ' |Λ₁₃| built =', len(T.L13()))
print('spread max/min = %d / %d = %.4f  (printed "a factor of 2.17")' %
      (max(CNT.values()), min(CNT.values()), max(CNT.values()) / min(CNT.values())))
print('brackets: LS [383,065, 597,325] ∋ 431,050 =', 383065 <= 431050 <= 597325,
      '; jj [160,380, 244,060] ∋ 206,520 =', 160380 <= 206520 <= 244060)

def tri(a, b):
    """Multiset of 2X from coupling two angular momenta given as doubled values."""
    return list(range(abs(a - b), a + b + 1, 2))

def multiset(l1, l2, scheme):
    """J multiset (doubled) for the two-electron configuration ℓ₁ℓ₂, all four standard chains."""
    L1, L2, S1 = 2 * l1, 2 * l2, 1
    out = Counter()
    if scheme == 'LS':
        for L in tri(L1, L2):
            for S in tri(1, 1):
                for J in tri(L, S): out[J] += 1
    elif scheme == 'LK':
        for L in tri(L1, L2):
            for K in tri(L, 1):
                for J in tri(K, 1): out[J] += 1
    elif scheme == 'jK':
        for j1 in tri(L1, 1):
            for K in tri(j1, L2):
                for J in tri(K, 1): out[J] += 1
    elif scheme == 'jj':
        for j1 in tri(L1, 1):
            for j2 in tri(L2, 1):
                for J in tri(j1, j2): out[J] += 1
    return out

print('J multisets across the four chains, every two-electron configuration ℓ₁ℓ₂ to f:')
bad = 0; conf = 0
for l1 in range(4):
    for l2 in range(4):
        ms = {sch: multiset(l1, l2, sch) for sch in ('jK', 'LS', 'LK', 'jj')}
        conf += 1
        same = len({tuple(sorted(m.items())) for m in ms.values()}) == 1
        if not same: bad += 1
        print('  %s%s  states %3d  identical across jK, LS, LK, jj: %s   J multiset (2J) %s'
              % ('spdf'[l1], 'spdf'[l2], sum(ms['LS'].values()), same, dict(sorted(ms['LS'].items()))))
print('configurations tested', conf, ' disagreeing', bad,
      ' (printed: "identical in all four schemes", verified at L3612 through three chains — jK, LS, jj)')
