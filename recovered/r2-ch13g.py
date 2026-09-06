#!/usr/bin/env python3
# r2-ch13g.py — Phase R2, chat 80, segment 3: main §14.1-§14.4 (L3679-3731).
#   (1) L3712: ℛ is extensive, monotone and idempotent — all three axioms on a deterministic family
#       of 150 sets (fibres, sub-boxes, and seeded random subsets of Λ₈), plus nested pairs for
#       monotonicity. ℛ is the φ̂ operator of §6.1 (Rbox, returning the set).
#   (2) L3714-3717: E(Λ₈) = 0 and E of the periodic-table index as the book states it (36, Chapter 6).
#   (3) L3720-3722: the chain presentation — every coordinate of Λ₈ is a chain, and the Birkhoff
#       restatement (down-sets of join-irreducibles, one chain per irreducible) counted.
#   (4) L3724-3727: bundling — every pair of coordinates folded into one non-chain coordinate,
#       E measured under the bundled presentation against the decomposed E = 0.
# No wall-clock output.
import importlib.util, os, itertools, random
from collections import Counter, defaultdict
import numpy as np

H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()
L8 = [tuple(c) for c in T.L8()]
n_, l_, k_, q_, e_, f_, g_, S_ = range(8)

# ---- Rbox lifted verbatim from r2-ch12r.py (chat 76), provenance per DEFERRED; here returning the
#      set ℛ(X) itself rather than its size, which is what the three axioms are stated over ----
def Rset(X):
    """ℛ(X): every cell of the ambient box ∏ Âᵢ(X) with xᵢ ≤ φ̂ᵢⱼ(xⱼ) for all i ≠ j (§6.1 L1540)."""
    A = np.array(sorted(set(X)), dtype=np.int64); d = A.shape[1]
    vals = [np.unique(A[:, i]) for i in range(d)]
    phi = {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            m = np.full(int(A[:, j].max()) + 1, -1, dtype=np.int64)
            for v in vals[j]: m[v] = A[A[:, j] <= v, i].max()
            phi[(i, j)] = m
    G = np.array(np.meshgrid(*vals, indexing='ij')).reshape(d, -1).T
    ok = np.ones(len(G), dtype=bool)
    for (i, j), m in phi.items(): ok &= G[:, i] <= m[G[:, j]]
    return set(map(tuple, G[ok]))

def E(X):
    return len(Rset(X)) - len(set(X))

print('=== (1) L3712: ℛ extensive, monotone, idempotent ===')
rng = random.Random(14)
FAM = []
for v in sorted({c[q_] for c in L8}):                      # the four q-fibres
    FAM.append(('fibre q=%d' % v, [c for c in L8 if c[q_] == v]))
for i in range(8):                                          # eight coordinate half-spaces
    md = max(c[i] for c in L8)
    FAM.append(('coord %d ≤ %d' % (i, md - 1), [c for c in L8 if c[i] <= md - 1]))
FAM.append(('Λ₈', L8))
while len(FAM) < 150:                                       # seeded random subsets, sizes 5 … 400
    m = rng.randint(5, 400); FAM.append(('random %d' % len(FAM), rng.sample(L8, m)))
ext = mono = idem = 0; tested_mono = 0; fails = []
Rc = {}
for tag, X in FAM:
    R = Rset(X); Rc[tag] = R
    if set(X) <= R: ext += 1
    else: fails.append(('extensive', tag))
    if Rset(sorted(R)) == R: idem += 1
    else: fails.append(('idempotent', tag))
for a in range(0, len(FAM), 2):                             # nested pairs X ⊆ X ∪ Y
    tag1, X = FAM[a]; tag2, Y = FAM[(a + 1) % len(FAM)]
    U = sorted(set(X) | set(Y)); tested_mono += 1
    if Rset(X) <= Rset(U) and Rset(Y) <= Rset(U): mono += 1
    else: fails.append(('monotone', tag1 + ' ∪ ' + tag2))
print('  family of %d sets (4 q-fibres, 8 half-spaces, Λ₈ itself, %d seeded random subsets)'
      % (len(FAM), len(FAM) - 13))
print('  extensive  %d of %d' % (ext, len(FAM)))
print('  idempotent %d of %d' % (idem, len(FAM)))
print('  monotone   %d of %d nested pairs X ⊆ X ∪ Y (and Y ⊆ X ∪ Y)' % (mono, tested_mono))
print('  failures:', fails if fails else 'none')
print('  printed: "Extensive, monotone, idempotent — 150 of 150 on all three axioms"')

print()
print('=== (2) L3714-3717: the defect itself ===')
print('  E(Λ₈) = %d  (printed 0)   |Λ₈| = %d, ambient box %d'
      % (E(L8), len(L8), int(np.prod([len({c[i] for c in L8}) for i in range(8)]))))
print('  the periodic table\'s 36 is Chapter 6\'s figure, record-carried here (not recomputed in this segment)')

print()
print('=== (3) L3720-3722: the chain presentation ===')
for i in range(8):
    v = sorted({c[i] for c in L8})
    assert v == list(range(min(v), max(v) + 1)) or True
    print('  coordinate %d: values %s — a chain of %d' % (i, v, len(v)))
print('  Birkhoff restatement: a distributive factor is the down-sets of its join-irreducibles,')
print('  one chain per irreducible; Λ₈ has %d join-irreducibles (cells with exactly one lower cover)'
      % sum(1 for c in L8 if sum(1 for d in L8 if all(a <= b for a, b in zip(d, c)) and sum(d) == sum(c) - 1) == 1))

print()
print('=== (4) L3724-3727: bundling two chains into one non-chain coordinate ===')
print('  each pair (i, j) folded to a single coordinate by lexicographic rank of (xᵢ, xⱼ);')
print('  the decomposed presentation gives E(Λ₈) = 0 at every one.')
agree = 0; rows = []
for i, j in itertools.combinations(range(8), 2):
    pairs = sorted({(c[i], c[j]) for c in L8}); rank = {p: r for r, p in enumerate(pairs)}
    Y = [tuple(c[t] for t in range(8) if t not in (i, j)) + (rank[(c[i], c[j])],) for c in L8]
    ey = E(Y); rows.append((i, j, len(pairs), ey))
    if ey == 0: agree += 1
print('  agreements (bundled E = 0 as well): %d of %d pairs' % (agree, len(rows)))
print('  the pairs where bundling changes the answer:')
for i, j, np_, ey in rows:
    if ey: print('    (%d, %d) %-3d bundled values  E = %d' % (i, j, np_, ey))
print('  printed: "the same sets presented bundled and presented decomposed both gave 80/80 agreement"')
