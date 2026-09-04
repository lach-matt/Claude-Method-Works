#!/usr/bin/env python3
# r2-ch16o.py -- chat 122, computable batch for main L9030-L9156
# (32.2 Self-reference, 32.3 Self-defence, 32.4 The recursion, 32.4.1 logic without negation,
#  32.4.2 which figures survive their inputs moving).
#
# Every figure is measured on the rebuilt lattice.  Conventions are NAMED before any figure is
# scored (chats 118-121).  Rounding is Decimal.quantize, never round().
# r2-ch16o2.py — R3 (chat 153-R) — SUCCESSOR to r2-ch16o.py, re-anchored by tools/reanchor.py: every main-volume line the
# predecessor pinned as a literal is resolved by the text of the line it pointed at in the bundle its golden was
# banked against (4 anchors); nothing else changes. r2-ch16o.py is seated and never edited in place (chat 68).
# PROVED by tools/proveanchor.py when the line below says so; until then this file is a draft.
# PROVEANCHOR: 90+184 — reproduces r2-ch16o.out byte-exact on those bundles (G0c)

# --- re-anchoring helper (tools/reanchor.py): a main-volume line found by its own text, never by a number ---
def _L(t, d=0):
    import os as _o
    global _LM
    try: _LM
    except NameError: _LM = open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')
    h = [i for i, l in enumerate(_LM, 1) if l == t]
    assert len(h) == 1, ('re-anchor: line text is not unique or is absent', t[:60], h)
    return h[0] + d
import importlib.util, os, random, sys
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN
import numpy as np

H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(spec); spec.loader.exec_module(r2lib)
L8_at, Rset, factor_q, closure = r2lib.L8_at, r2lib.Rset, r2lib.factor_q, r2lib.closure

MAIN = open(os.path.join(H, 'The_Method_1_6-2.md'), encoding='utf-8').read().split('\n')

def q2(x, places, mode=ROUND_HALF_UP):
    return Decimal(str(x)).quantize(Decimal('1.' + '0' * places), rounding=mode)

def hr(t): print('\n' + '=' * 96 + '\n' + t + '\n' + '=' * 96)

# caps are (n_max, e_max, l_max, k_max, f_max) -- the order L8_at takes and the order 7.4 prints
SETTINGS = [(3, 3, 1, 3, 1), (4, 4, 1, 6, 1), (4, 4, 2, 6, 2), (5, 5, 2, 6, 2)]
PRINTED = {                                   # L9126-L9133, as printed
    'cells':      [976, 8853, 19109, 35789],
    'generators': [17, 31, 33, 35],
    'fill':       ['14.12%', '6.72%', '6.45%', '7.73%'],
    'ranklev':    [18, 32, 34, 36],
    'widest':     [122, 704, 1497, 2742],
    'surplus':    ['7.07', '17.89', '18.78', '19.87'],
    'reflect':    [8, 16, 17, 68],
}

hr('0.  CONVENTIONS, fixed before any figure is scored')
print("""  cells        len(L8_at(caps)) -- the tower member at those caps
  alphabet A_i unique realised values of coordinate i over the cells
  ambient box  prod |A_i| over the 8 coordinates (11.1.1 / 12.11's 'ambient box')
  fill         cells / ambient box, percent, quantize 2dp HALF_UP
  generators   |J(L)|, the join-irreducibles: cells with exactly one lower cover in L
  surplus      |J| - log2(cells)   [DERIVED from L2149: 976 of 131,072 = 2^17 seventeen-bit
               words gives 17 - log2(976) = 7.069 -> 7.07, the figure 11.1.1 states]
  rank         sum of the 8 coordinates            [tested against 'eighteen antichains, the
  rank levels  number of distinct rank values       largest 122 at rank 11' (L2474) before use]
  widest level max cells sharing one rank value
  reflection   x -> (max_i - x_i) coordinate-wise, max_i over the cells (L1887, L10154)
  E(X)         |Rset(X)| - |X|, Rset = r2lib's 6.1 reconstruction
  factorises   factor_q(X) == 0, i.e. sum_q |src fibre|*|tgt fibre| == |X|""")

hr('1.  32.4.2 L9126-L9133 -- the cap-variation table, seven rows x four settings')
MEAS = {k: [] for k in PRINTED}
LAT = {}
for caps in SETTINGS:
    X = L8_at(caps); LAT[caps] = X
    A = np.array(sorted(set(X)), dtype=np.int64)
    alpha = [np.unique(A[:, i]) for i in range(A.shape[1])]
    box = 1
    for a in alpha: box *= len(a)
    fill = 100.0 * len(A) / box
    rank = A.sum(axis=1)
    lev, cnt = np.unique(rank, return_counts=True)
    # join-irreducibles.  L is closed under componentwise meet, so for each coordinate i and each
    # realised value v the set {y in L : y_i >= v} has a minimum m(i,v) (its own meet).  Every x
    # satisfies x = join_i m(i, x_i), hence J(L) is contained in {m(i,v) : v > min A_i}; a candidate
    # is join-irreducible iff the join of everything strictly below it is not itself.  Exact, and
    # O(sum|A_i| . n) instead of O(n^3).
    keys = set(map(tuple, A.tolist()))
    cand = set()
    for i in range(A.shape[1]):
        for v in alpha[i][1:]:
            sub = A[A[:, i] >= v]
            cand.add(tuple(int(t) for t in sub.min(axis=0)))
    ji = 0
    for c in sorted(cand):
        below = A[(A <= np.array(c)).all(axis=1)]
        below = below[~(below == np.array(c)).all(axis=1)]
        if len(below) == 0 or tuple(int(t) for t in below.max(axis=0)) != c:
            ji += 1
    mx = A.max(axis=0)
    refl = sum(1 for c in A.tolist() if tuple(m - v for m, v in zip(mx, c)) in keys)
    import math
    surplus = ji - math.log2(len(A))
    MEAS['cells'].append(len(A)); MEAS['generators'].append(ji)
    MEAS['fill'].append(f'{q2(fill,2)}%'); MEAS['ranklev'].append(len(lev))
    MEAS['widest'].append(int(cnt.max())); MEAS['surplus'].append(str(q2(surplus, 2)))
    MEAS['reflect'].append(refl)
    print(f'  caps {caps}: cells {len(A):,}  box {box:,}  ranks {lev.min()}..{lev.max()}  '
          f'widest at rank {int(lev[cnt.argmax()])}')

print()
for k in ['cells', 'generators', 'fill', 'ranklev', 'widest', 'surplus', 'reflect']:
    ok = all(str(a) == str(b) for a, b in zip(PRINTED[k], MEAS[k]))
    print(f'  {k:<11} printed {str(PRINTED[k]):<44} measured {str(MEAS[k]):<44} '
          f'{"EXACT" if ok else "DEVIATION"}')

hr('2.  32.4.2 count words against their own tables')
def table_rows(a, b):
    """data rows of a space-aligned table: lines between a and b that are not blank and not the
    header line."""
    out = []
    for ln in range(a, b + 1):
        s = MAIN[ln - 1]
        if s.strip():
            out.append((ln, s.strip()))
    return out
vals = table_rows(_L('  cells                             976         8,853        19,109        35,789'), _L('  reflection survivors                8            16            17            68'))
ids = table_rows(_L('  E(Λ) = 0                                        at every setting'), _L('  the cylinder factorises over the transfer       at every setting'))
print(f'  values table L9127-L9133: {len(vals)} data rows ->', [v[1].split()[0] for v in vals])
print(f'  identity table L9141-L9145: {len(ids)} data rows')
for ln, s in ids: print(f'      L{ln}  {s[:70]}')
print(f'\n  L9135 prints "Nine of nine move."          rows measured = {len(vals)}  '
      f'{"EXACT" if len(vals)==9 else "DEVIATION -- the table names " + str(len(vals))}')
print(f'  L9147 prints "Six of six identities hold" rows measured = {len(ids)}  '
      f'{"EXACT" if len(ids)==6 else "DEVIATION -- the table names " + str(len(ids))}')
print('  second reading, "closed under join and meet" counted as two identities: '
      f'{len(ids)+1} -- {"reaches six" if len(ids)+1==6 else "does not reach six"}')
print('  second reading for the values, every distinct figure in the table body counted '
      f'(7 rows x 4 settings = {len(vals)*4}); no reading of the table reaches nine.')

hr('3.  32.4.2 L9141-L9145 -- the five printed identities, tested at all four settings')
for caps in SETTINGS:
    X = LAT[caps]; n = len(X)
    R = Rset(X); E = len(R) - len(set(X))
    A = np.array(sorted(set(X)), dtype=np.int64)
    sig = sum(len(np.unique(A[:, i])) - 1 for i in range(A.shape[1]))
    ji = MEAS['generators'][SETTINGS.index(caps)]
    # FAULT 1, self-caught: r2lib.factor_q is a LAMBDA-9 function -- its tgt() reads tuple index 8,
    # which an 8-tuple does not have.  Rewritten here for L8's halves: source (n, l, k, 2S) =
    # indices 0,1,2,7; transfer q = index 3; target (e, f, g) = indices 4,5,6.  Provenance: the
    # shape of r2lib.factor_q (chat 74, r2-ch12i), the indices re-measured from r2lib.NAMES.
    from collections import defaultdict as _dd
    SRC8, TGT8, Q8 = (0, 1, 2, 7), (4, 5, 6), 3
    _a, _b = _dd(set), _dd(set)
    for c in X:
        _a[c[Q8]].add(tuple(c[i] for i in SRC8)); _b[c[Q8]].add(tuple(c[i] for i in TGT8))
    fq = sum(len(_a[v]) * len(_b[v]) for v in _a) - len(set(X))
    if n <= 1200:                                    # exhaustive pairs, C(n,2)
        tot, jl, ml = closure(list(set(map(tuple, A.tolist()))))
        pairs = f'exhaustive {n*(n-1)//2:,} pairs'
        leaks = jl + ml
        mod = 0                                       # rank is additive: max+min = a+b per coord
        rk = A.sum(axis=1)
        keys = {tuple(c): int(r) for c, r in zip(A.tolist(), rk.tolist())}
        cl = list(keys)
        for i in range(len(cl)):
            for j in range(i + 1, len(cl)):
                a, b = cl[i], cl[j]
                jn = tuple(map(max, a, b)); mt = tuple(map(min, a, b))
                if jn in keys and mt in keys and keys[jn] + keys[mt] != keys[a] + keys[b]:
                    mod += 1
    else:                                             # BUDGET: 200,000 random pairs, seed 122
        rng = random.Random(122); keys = set(map(tuple, A.tolist()))
        rk = {c: sum(c) for c in keys}
        cl = list(keys); leaks = 0; mod = 0; B = 200000
        for _ in range(B):
            a = rng.choice(cl); b = rng.choice(cl)
            jn = tuple(map(max, a, b)); mt = tuple(map(min, a, b))
            if jn not in keys or mt not in keys:
                leaks += 1
            elif rk[jn] + rk[mt] != rk[a] + rk[b]:
                mod += 1
        pairs = f'BUDGET {B:,} random pairs (seed 122) of {n*(n-1)//2:,}'
    print(f'  caps {caps}  n={n:,}')
    print(f'      E(L) = {E}                       {"HOLDS" if E==0 else "FAILS"}')
    print(f'      |J| = {ji}   sum(|A_i|-1) = {sig}   {"HOLDS" if ji==sig else "FAILS"}')
    print(f'      join/meet closed: {leaks} leaks, {pairs}  {"HOLDS" if leaks==0 else "FAILS"}')
    print(f'      rank(a v b)+rank(a ^ b)=rank(a)+rank(b): {mod} failures  '
          f'{"HOLDS" if mod==0 else "FAILS"}')
    print(f'      cylinder factorises over the transfer: factor_q = {fq}  '
          f'{"HOLDS" if fq==0 else "FAILS"}')

print('\n  NOTE on the fourth identity: rank is the coordinate sum (fixed in section 0 and confirmed')
print('  against L2474 by 18 levels with 122 widest at rank 11).  Componentwise max + min = a + b')
print('  in every coordinate, so rank(a v b) + rank(a ^ b) = rank(a) + rank(b) is ENTAILED by the')
print('  third identity: wherever join and meet stay inside the lattice the fourth cannot fail.')
print('  It is an exact identity, not an independent test, and the table prints the two in the')
print('  same voice and with the same "tested by pairs" qualifier.')

hr('4.  32.4 L9069-L9077 -- the recursion table, occupancy against cells and alphabets')
REC = [('0 - the index', 10, '0.625', [4, 4]), ('1 - claims about it', 10, '0.143', [10, 7]),
       ('2 - claims about those', 10, '0.100', [10, 10]), ('3', 10, '0.100', [10, 10])]
for lab, cells, occ, alpha in REC:
    box = alpha[0] * alpha[1]
    m = q2(cells / box, 3)
    print(f'  {lab:<24} cells {cells}  alphabets {alpha}  box {box}  printed {occ}  '
          f'measured {m}  {"EXACT" if str(m)==occ else "DEVIATION"}')
print('\n  L9079 prints "Closure, dimension and E are invariant from level 1."')
print('  measured from the table itself: closed = yes and E = 0 at levels 0,1,2,3; the number of')
print('  alphabets (the dimension) is 2 at levels 0,1,2,3.  All three are invariant from level 0,')
print('  not from level 1 -- the sentence understates its own table.  What changes at level 1 is')
print('  occupancy (0.625 -> 0.143) and the alphabets ([4,4] -> [10,7]), which are exactly the two')
print('  the same paragraph says stabilise "by level 2, not level 1".  CONSISTENT but understated.')

hr('5.  32.4.1 L9100-L9108 -- the closure-operator proof, corroborated as the book corroborates it')
print('  CONVENTION: ambient box = the 8 coordinate value sets of L8_at((3,3,1,3,1)); a random')
print('  subset is 3..40 cells drawn uniformly without replacement; 3,000 draws, seed 122;')
print('  extensive/monotone/idempotent tested per draw exactly as the proof states them.')
rng = random.Random(122)
base = sorted(set(map(tuple, L8_at((3, 3, 1, 3, 1)))))
ext = mono = idem = 0
for _ in range(3000):
    k = rng.randint(3, 40)
    Xs = rng.sample(base, k); RX = Rset(Xs)
    if not set(Xs) <= RX: ext += 1
    if RX != Rset(sorted(RX)): idem += 1
    Ys = Xs + rng.sample(base, rng.randint(1, 10))
    if not (RX <= Rset(sorted(set(Ys)))): mono += 1
print(f'  extensive  failures {ext} / 3,000        {"ZERO" if ext==0 else "DEVIATION"}')
print(f'  monotone   failures {mono} / 3,000        {"ZERO" if mono==0 else "DEVIATION"}')
print(f'  idempotent failures {idem} / 3,000        {"ZERO" if idem==0 else "DEVIATION"}')

print('\n  fixed points closed under intersection: 3,000 random pairs of fixed points, seed 122.')
fps = []
rng2 = random.Random(122)
while len(fps) < 400:
    k = rng2.randint(3, 40)
    F = Rset(rng2.sample(base, k))
    if Rset(sorted(F)) == F: fps.append(frozenset(F))
inter_nonempty = 0; fails = 0
for _ in range(3000):
    a = rng2.choice(fps); b = rng2.choice(fps)
    m = a & b
    if m: inter_nonempty += 1
    if m and Rset(sorted(m)) != set(m): fails += 1
pct = q2(100.0 * inter_nonempty / 3000, 1)
print(f'  non-empty meets {inter_nonempty:,} / 3,000 ({pct}%)   book prints 2,873 / 3,000 (95.8%)')
print(f'  closure failures on the meets: {fails}   {"ZERO, as printed" if fails==0 else "DEVIATION"}')
print('  NOTE the 2,873 is a draw-dependent count, not an invariant: it is reproducible only with')
print('  the original seed and sampler.  Recorded as corroborated in kind, not matched exactly.')

hr('6.  32.4.1 L9093-L9098 -- chi is a product of seven Heaviside steps, and has no negation')
# FAULT 2, self-caught: the first form of this section counted BINDING phi-hat pairs (16) and
# scored the book's "seven factors" against them.  That is the wrong measurement -- phi-hat pairs
# are the reconstruction operator's bounds, not chi's factors.  chi's factors are the
# inter-coordinate bounds of the construction itself, read off L8() (tower-2.py L9-L17).
FACTORS = [('l <= n - 1', lambda c: c[1] <= c[0] - 1),
           ('k <= 4l + 2', lambda c: c[2] <= 4 * c[1] + 2),
           ('q <= k', lambda c: c[3] <= c[2]),
           ('f <= e - 1', lambda c: c[5] <= c[4] - 1),
           ('g <= 4f + 2', lambda c: c[6] <= 4 * c[5] + 2),
           ('g <= q', lambda c: c[6] <= c[3]),
           ('2S <= k', lambda c: c[7] <= c[2])]
CAPS = [('n <= 3', lambda c: c[0] <= 3), ('l <= 1', lambda c: c[1] <= 1),
        ('k <= 3', lambda c: c[2] <= 3), ('e <= 3', lambda c: c[4] <= 3),
        ('f <= 1', lambda c: c[5] <= 1)]
X = LAT[(3, 3, 1, 3, 1)]
A = np.array(sorted(set(X)), dtype=np.int64)
box_cells = [tuple(int(v) for v in c) for c in
             np.array(np.meshgrid(*[np.unique(A[:, i]) for i in range(8)],
                                  indexing='ij')).reshape(8, -1).T]
print(f'  ambient box {len(box_cells):,} cells; L8_at((3,3,1,3,1)) has {len(A):,}')
keep = [c for c in box_cells if all(f(c) for _, f in FACTORS) and all(f(c) for _, f in CAPS)]
print(f'  the seven inter-coordinate factors + the five caps cut the box to {len(keep):,}  '
      f'{"EXACT against the lattice" if len(keep)==len(A) else "DEVIATION"}')
print(f'  factors printed: seven.  Factors measured in the construction: {len(FACTORS)}  '
      f'{"EXACT" if len(FACTORS)==7 else "DEVIATION"}')
for name, f in FACTORS:
    relaxed = [c for c in box_cells if all(g(c) for nm, g in FACTORS if nm != name)
               and all(g(c) for _, g in CAPS)]
    print(f'      {name:<14} binding: relaxing it admits {len(relaxed)-len(keep):>5} further cells'
          f'   {"BINDING" if len(relaxed)>len(keep) else "NOT BINDING"}')
print('  every factor is an upper bound of one coordinate by a monotone function of another:')
print('    available max, min, <=  -- no factor uses complement, negation or implication.  The')
print('    sentence at L9093-L9098 is EXACT on the construction as tower-2.py builds it.')

hr('7.  32.3 L9045-L9047 and L9055 -- the audit figures, sited across the volume')
import re
def sites(pat):
    return [i + 1 for i in range(len(MAIN)) if re.search(pat, MAIN[i])]
for lab, pat in [('102 (digit-bounded)', r'(?<![\d.,])102(?!\d)(?!,\d)(?!\.\d)'),
                 ('"102 quantitative"', r'102 quantitative'),
                 ('thirty (word)', r'(?<![A-Za-z])[Tt]hirty(?![A-Za-z-])'),
                 ('one thousand six hundred and thirty-five',
                  r'one thousand six hundred and thirty-five'),
                 ('1,635 / 1635 digits', r'(?<![\d.,])1,?635(?!\d)')]:
    s = sites(pat)
    print(f'  {lab:<42} {len(s):>3} sites  {s[:18]}')
print('\n  Chapter 28 own statement of the failing-level count (lines matching "failed" in 28):')
c28 = r2lib.section_span(MAIN, '28')
print(f'  chapter 28 span (body): {c28}')
if c28:
    for ln in range(c28[0], c28[1]):
        if re.search(r'fail(ed|ing)', MAIN[ln - 1], re.I) and re.search(r'\d', MAIN[ln - 1]):
            print(f'      L{ln}  {MAIN[ln-1].strip()[:118]}')
