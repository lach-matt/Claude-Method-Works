#!/usr/bin/env python3
"""fill_outside.py — the fill-limit from OUTSIDE: the next rung the physics supplies, computed.

Companion to fill_limit.py (which proved the bracket unimprovable from inside).  Outside means a
law independent of the index (M ch. 18, the envelope clause).  Prior art names the rung after 2J:
the hyperfine coupling F = J ⊗ I (Condon & Shortley 1935; Casimir 1936), then the projection M_F.
In the tower's own one-parent envelope style (§12.11.1: f_max, not the cell's f; §12.11.5: every
coupling axis hangs off one side of the tree), the rung is

  axis 14   2F      max(0, 2J − 2I_max) ≤ 2F ≤ 2J + 2I_max        (window on the single parent 2J)
  axis 15   m_F     0 ≤ m_F ≤ 2F,  m_F = F + M_F                    (cap by the single parent 2F)

with 2I_max a declared cap — a declaration about the world, as Z = 120 is (DIGEST).  The exact
triangle |2J − 2I| ≤ 2F ≤ 2J + 2I is a SUM bound and does not close (E3: sums fail); it is measured
here as the density column of §12.11.1 measures it, against the envelope, with 2I adjoined free.

Segments: [1] tower + 2J distribution  [2] envelope fills for every cap  [3] density  [4] closure tests.
"""
import sys, math, importlib.util, time
from collections import Counter
import numpy as np

HERE = __import__('os').path.dirname(__import__('os').path.abspath(__file__))
def load(name, fn):
    s = importlib.util.spec_from_file_location(name, HERE + '/' + fn); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
tower = load('tower_1', 'tower-1.py')

OUT = open(HERE + '/FILL-OUTSIDE-RESULTS.txt', 'w')
def emit(*a):
    s = ' '.join(str(x) for x in a); print(s); OUT.write(s + '\n'); OUT.flush()

def box_of(X): return [sorted(set(c[i] for c in X)) for i in range(len(X[0]))]
def E_of(X, max_box=6_000_000):
    A = box_of(X); d = len(A); boxsize = math.prod(len(a) for a in A)
    if boxsize > max_box: return None, boxsize
    idx = [{v: k for k, v in enumerate(a)} for a in A]
    Xi = np.array([[idx[i][c[i]] for i in range(d)] for c in X], dtype=np.int16)
    grids = np.indices([len(a) for a in A]).reshape(d, -1).astype(np.int16)
    mask = np.ones(boxsize, dtype=bool)
    for i in range(d):
        for j in range(i + 1, d):
            T = np.zeros((len(A[i]), len(A[j])), dtype=bool); T[Xi[:, i], Xi[:, j]] = True
            mask &= T[grids[i], grids[j]]
    return int(mask.sum()) - len(X), boxsize

# ---------------------------------------------------------------- SEGMENT 1
t0 = time.time()
emit('SEGMENT 1 — Λ13 and its 2J distribution (coordinate 12)')
L13 = tower.L13(); box13 = math.prod(len(a) for a in box_of(L13)); fill13 = len(L13) / box13
J = Counter(c[12] for c in L13); Jmax = max(J)
emit(f'  |Λ13| = {len(L13):,}  box13 = {box13:,}  fill13 = {100*fill13:.6f}%  2J ∈ 0..{Jmax}')
emit('  cells by 2J:', [J[j] for j in range(Jmax + 1)])
emit(f'segment 1 closed ({time.time()-t0:.1f}s)')

# ---------------------------------------------------------------- SEGMENT 2
t0 = time.time()
emit('\nSEGMENT 2 — the hyperfine rung, envelope form, for every cap 2I_max = i (I = i/2)')
def cF(j, i):   # multiplicity of 2F on a cell with 2J = j, cap i
    lo = max(0, j - i); hi = j + i; return hi - lo + 1
def stage14(i): return sum(J[j] * cF(j, i) for j in J)
def stage15(i): return sum(J[j] * sum(F + 1 for F in range(max(0, j - i), j + i + 1)) for j in J)
emit('   i   I     vc14   cells14      fill14%   ratio14      cells15       fill15%   ratio15   fill15/fill13')
for i in range(0, 15):
    vc = Jmax + 1 + i                       # realised values of 2F, and of m_F
    c14, c15 = stage14(i), stage15(i)
    f14 = c14 / (box13 * vc); f15 = c15 / (box13 * vc * vc)
    emit(f'  {i:2d}  {i/2:4.1f}   {vc:3d}  {c14:10,d}  {100*f14:10.6f}  {f14/fill13:.4f}  {c15:12,d}  {100*f15:11.7f}  {f15/f14:.4f}  {f15/fill13:.5f}'
         + ('   (I = 0: 2F = 2J, a RELABEL — not an axis by Thm 11.1)' if i == 0 else ''))
emit(f'segment 2 closed ({time.time()-t0:.1f}s)')

# ---------------------------------------------------------------- SEGMENT 3
t0 = time.time()
emit('\nSEGMENT 3 — density of the exact triangle against the envelope (§12.11.1 style), 2I adjoined free')
emit('   i   exact fibre Σ   envelope Σ   density%')
for i in range(1, 15):
    exact = sum(J[j] * sum(min(j, I2) + 1 for I2 in range(0, i + 1)) for j in J)       # parity-respecting
    envel = sum(J[j] * (i + 1) * cF(j, i) for j in J)
    emit(f'  {i:2d}   {exact:14,d}   {envel:12,d}   {100*exact/envel:7.2f}')
emit(f'segment 3 closed ({time.time()-t0:.1f}s)')

# ---------------------------------------------------------------- SEGMENT 4
t0 = time.time()
emit('\nSEGMENT 4 — closure: envelope rung must close (one-parent bounds), exact triangle must not (sum bound)')
def rung_env(X, anchor, i):
    Y = [c + (F,) for c in X for F in range(max(0, c[anchor] - i), c[anchor] + i + 1)]
    return [c + (m,) for c in Y for m in range(0, c[-1] + 1)]
def rung_exact(X, anchor, i):
    Y = [c + (I2,) for c in X for I2 in range(0, i + 1)]
    return [c + (F,) for c in Y for F in range(abs(c[anchor] - c[-1]), c[anchor] + c[-1] + 1, 2)]
stages = {8: tower.L8(), 9: tower.L9(), 10: tower.L10()}
for base, anchor in ((8, 7), (9, 8), (10, 9)):      # anchor = the stage's top coordinate, standing in for 2J
    for i in (1, 3):
        for name, fn in (('envelope F+m', rung_env), ('exact triangle', rung_exact)):
            X = fn(stages[base], anchor, i); E, b = E_of(X)
            emit(f'  Λ{base} + {name:15s} cap i={i}: cells {len(X):,} box {b:,}  E = {E if E is not None else "refused (box above bound)"}')
X = rung_env(L13, 12, 1); b = math.prod(len(a) for a in box_of(X))
emit(f'  Λ13 + envelope F+m cap i=1: cells {len(X):,} box {b:,} — exhaustive test refused at this box; closure by the one-parent argument')
emit(f'segment 4 closed ({time.time()-t0:.1f}s)')
OUT.close()
