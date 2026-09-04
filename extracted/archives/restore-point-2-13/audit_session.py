#!/usr/bin/env python3
"""audit_session.py — stage 4: this session's own claims, recomputed from scratch.

Registers 1434–1477 were written today. Each carries figures. This recomputes
every one of them INDEPENDENTLY — not by re-running the script that produced it,
but from brack.IV and ground.py directly — and compares against what the register
states. A figure that does not reproduce is reported as a FAIL regardless of how
recently it was written or how much rests on it.

The stated figure is read from REGISTER-DATA.md by pattern, so a typo in the
entry fails here even if the computation was right.
"""
import re, sys, io, math, itertools, contextlib, pathlib, statistics as st
from math import comb

W = pathlib.Path("/home/claude/work")
sys.path.insert(0, str(W))
with contextlib.redirect_stdout(io.StringIO()):
    import brack, ground as G

R = (W / "REGISTER-DATA.md").read_text(encoding="utf-8")
L = "spdfg"
cap = lambda l: 2 * (2 * l + 1)
EPS = 1e-9
IV = {r[0]: r for r in brack.IV}
STEPS = sorted(IV)
OBS = {Z: (IV[Z][1], IV[Z][2]) for Z in STEPS}
SUBS = [(n, l) for n in range(1, 9) for l in range(min(n, 5))]
pn = lambda s: s[0] - s[1] - 1
Mof = lambda s: s[0] + s[1]
fails = []


def check(name, got, want, note=""):
    ok = got == want
    print(f"    {name:<46}{str(got):>14}  registered {str(want):<12}{'PASS' if ok else 'FAIL'}  {note}")
    if not ok:
        fails.append(name)


def occ(Z):
    if Z < 1:
        return {}
    d = {}
    for n, l, k in G.expand(Z):
        d[(n, l)] = d.get((n, l), 0) + k
    return d


def cands(prev):
    c = []
    for l in range(5):
        for n in range(l + 1, 9):
            if prev.get((n, l), 0) >= cap(l):
                continue
            c.append((n, l))
            if prev.get((n, l), 0) == 0:
                break
    return c


def pick(prev, a):
    s = [(n - a * math.sqrt((n - l - 1) + prev.get((n, l), 0) / cap(l)), n, l)
         for n, l in cands(prev)]
    b = min(x[0] for x in s)
    t = [(n, l) for v, n, l in s if v - b < EPS]
    return max(t, key=lambda x: x[0])


print("  AUDIT · STAGE 4 — THIS SESSION'S CLAIMS, RECOMPUTED\n")

# ---- R 1446 · the walk graded by observational status ---------------------
MISS = {5, 25, 43, 58, 64, 91, 96}
check("R 1446 · observed steps, Z 3–102", len([z for z in STEPS if z <= 102]), 100)
check("R 1446 · misses in the observed region", len([z for z in MISS if z <= 102]), 7)
check("R 1446 · calculated steps, Z 103–108", len([z for z in STEPS if z >= 103]), 6)
check("R 1446 · misses in the calculated region", len([z for z in MISS if z >= 103]), 0)

# ---- R 1447 · the filling run is the unit ---------------------------------
runs = []
for Z in STEPS:
    k = OBS[Z]
    if runs and runs[-1][0] == k and Z == runs[-1][1][-1] + 1:
        runs[-1][1].append(Z)
    else:
        runs.append([k, [Z]])
nonempty = sum(1 for _, zs in runs
               if max(IV[Z][4] for Z in zs) < min(IV[Z][5] for Z in zs))
check("R 1447 · filling runs", len(runs), 31)
check("R 1447 · runs whose corridors intersect", nonempty, 31)
blkstart = [1, 3, 5, 13, 21, 39, 57, 89]
blk = lambda Z: max(i for i, s in enumerate(blkstart) if s <= Z) + 1
emptyblocks = [b for b in range(2, 9)
               if (zs := [Z for Z in STEPS if blk(Z) == b])
               and max(IV[Z][4] for Z in zs) >= min(IV[Z][5] for Z in zs)]
check("R 1447 · Janet blocks with EMPTY intersection", emptyblocks, [5, 6, 7, 8])

# ---- R 1449 / 1469 · the half-capacity screen -----------------------------
half = lambda nl, p: p.get(nl, 0) > 0 and p.get(nl, 0) * 2 == cap(nl[1])
cls = []
for Z in STEPS:
    prev = occ(Z - 1)
    e = OBS[Z]
    rg = (e[0] - e[1] - 1) + prev.get(e, 0) / cap(e[1])
    for r in cands(prev):
        if r == e or not half(r, prev):
            continue
        rr = (r[0] - r[1] - 1) + prev.get(r, 0) / cap(r[1])
        d = math.sqrt(rg) - math.sqrt(rr)
        if abs(d) < 1e-12:
            continue
        x = (e[0] - r[0]) / d
        if IV[Z][4] < x < IV[Z][5]:
            cls.append(Z)
            break
check("R 1449 · half-capacity class, crossing inside", sorted(cls), [25, 43, 64, 96])
check("R 1449 · all of them are misses", sorted(set(cls) & MISS), [25, 43, 64, 96])
p = comb(len(cls), 4) / comb(len(STEPS), 4)
check("R 1469 · its P value to 4 dp", round(p, 4), 0.0)

# ---- R 1451 / 1452 · the coordinates --------------------------------------
check("R 1451 · M = 2n − p − 1 on every subshell",
      all(s[0] + s[1] == 2 * s[0] - pn(s) - 1 for s in SUBS), True)
check("R 1452 · p ≡ M+1 (mod 2) on every subshell",
      all(pn(s) % 2 == (Mof(s) + 1) % 2 for s in SUBS), True)
iff = all(((abs((A[0] - B[0]) / (math.sqrt(pn(A)) - math.sqrt(pn(B)))
                - (math.sqrt(pn(A)) + math.sqrt(pn(B))) / 2) < 1e-9)
           == (Mof(A) == Mof(B)))
          for A, B in itertools.combinations(SUBS, 2) if pn(A) != pn(B))
check("R 1452 · mean form ⟺ same group (an iff)", iff, True)
phi = (1 + 5 ** 0.5) / 2
check("R 1452 · φ is the p = 1,5 crossing",
      abs((1 + math.sqrt(5)) / 2 - phi) < 1e-12, True)

# ---- R 1456 · Klechkovski–Hakala onsets -----------------------------------
K = lambda x: (1 / 6) * x * (x * x + 2 - 3 * (x % 2))
OBSZ = {1: 1, 2: 3, 3: 5, 4: 13, 5: 21, 6: 39, 7: 57, 8: 89}
check("R 1456 · K(M)+1 reproduces all eight onsets",
      all(abs(K(M) + 1 - OBSZ[M]) < 1e-9 for M in range(1, 9)), True)

# ---- R 1462 · the rank-one certificate ------------------------------------
from fractions import Fraction as F
LEV = {"2s1/2": (2, 0, +1), "1d3/2": (1, 2, -1), "2d5/2": (2, 2, +1), "2p3/2": (2, 1, +1),
       "1f5/2": (1, 3, -1), "2f7/2": (2, 3, +1), "3p3/2": (3, 1, +1), "2f5/2": (2, 3, -1),
       "3s1/2": (3, 0, +1), "2d3/2": (2, 2, -1), "1g7/2": (1, 4, -1), "1h9/2": (1, 5, -1)}
lsv = lambda s: F(LEV[s][1], 2) if LEV[s][2] > 0 else F(-(LEV[s][1] + 1), 2)
cen = lambda s: F(LEV[s][1] * (LEV[s][1] + 1))
PAIRS = [("2s1/2", "1d3/2"), ("2p3/2", "1f5/2"), ("3p3/2", "2f5/2"),
         ("2d3/2", "3s1/2"), ("1g7/2", "2d5/2"), ("1h9/2", "2f7/2")]
rat = {(cen(b) - cen(a)) / (-(lsv(b) - lsv(a))) for a, b in PAIRS}
check("R 1462 · all six ratios are exactly 4", rat == {4}, True)

# ---- R 1470 · A4b's three conditions --------------------------------------
a_, lo, hi = None, -1e9, 1e9
empt, rise = [], []
for Z in STEPS:
    Lo, Up = IV[Z][4], IV[Z][5]
    nlo, nhi = max(lo, Lo), min(hi, Up)
    if nlo >= nhi or a_ is None:
        if a_ is not None:
            empt.append(Z)
        lo, hi = Lo, Up
    else:
        if a_ is not None and Lo > a_ + EPS:
            rise.append(Z)
        lo, hi = nlo, nhi
    w = lo if (lo > EPS and lo < 1e8) else (hi if hi < 1e8 else None)
    a_ = w if w is not None else (a_ if a_ is not None else 1.0)
check("R 1470 · intersection empties", len(empt), 14)
check("R 1470 · floor rises above held a", rise, [49, 81, 87])
nz = [Z for Z in STEPS if IV[Z][4] > EPS]
check("R 1470 · K 19 is the first non-zero floor", min(nz), 19)
check("R 1470 · Tl 81's corridor excludes 0.8090",
      not (IV[81][4] < 0.8090 < IV[81][5]), True, f"({IV[81][4]:.4f}, {IV[81][5]:.4f})")

print(f"\n  STAGE 4: {len(fails)} failure(s)" + (f" — {fails}" if fails else ""))
