#!/usr/bin/env python3
"""xray_cells.py — does Lambda_xray's cell membership predict MEASURED behaviour?

CORRECTION TO MY FIRST FRAMING. Lambda_xray is 33 dipole-allowed inner-shell
lines through the N shell collapsing to 9 cells on (Delta-n, Delta-l,
jtype_hole), E = 0, and the artefact states it was BUILT WITH NO NEW DATA —
from Lambda's own alphabet, EM.map's dipole rule and T.a12's j triangle. So the
five L-shell captures were ALREADY inside the 33. They do not open cells.

What they do is supply MEASUREMENT to a structure that was predicted. That makes
the real test sharper than the one I first wrote:

    DOES CELL MEMBERSHIP PREDICT HOW A LINE BEHAVES?

Two of the captured pairs share a cell and one pair does not:

    L3M4, L3M5   share (1, -1, +)    hole 2p3/2, electron 3d
    L1N2, L1N3   share (2, -1,  0)   hole 2s,    electron 4p
    L3M4, L2M4   DIFFER in jtype only: (1,-1,+) against (1,-1,-)
    L3M1, L3M4   DIFFER in Delta-l only: (1,+1,+) against (1,-1,+)

THE TEST. Fit Moseley's law E = A(Z - s)^2 to each line separately and compare
the exponent and the screening. If the cell is doing work, SAME-CELL lines
should agree more closely than DIFFERENT-CELL lines.

DECLARED BEFORE THE RUN. The null is that all seven lines behave alike because
they are all inner-shell transitions in the same atom — in which case same-cell
and different-cell pairs agree equally well and the cell predicts nothing. That
null is live and I do not know the answer.
"""
import math, itertools
from collections import defaultdict

CELL = {"L3M1": (1, +1, +1), "L3M4": (1, -1, +1), "L3M5": (1, -1, +1),
        "L2M1": (1, +1, -1), "L2M4": (1, -1, -1),
        "L1N2": (2, -1, 0), "L1N3": (2, -1, 0)}
SYM = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn "
       "Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce "
       "Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn "
       "Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm").split()
Z = {s: i + 1 for i, s in enumerate(SYM)}
BLEND = set("Rb Sr Y Zr Nb Mo Ru Rh Pd In Sn Sb Te I Xe Ba".split())


def load(n):
    d = {}
    for l in open(f"/home/claude/work/captures/XRAY-{n}.tsv"):
        if l.startswith("#") or not l.strip():
            continue
        f = l.rstrip("\n").split("\t")
        # theory is field 2 for the five L-shell files, field 2 for L1N*
        try:
            v = float(f[2])
        except ValueError:
            continue
        d[f[0]] = v
    return d


D = {n: load(n) for n in CELL}


def fit(d, lo=30, hi=92):
    """E = A (Z - s)^p ; fit log E against log(Z - s) over a grid of s."""
    best = None
    for s10 in range(0, 300):
        s = s10 / 10
        xs, ys = [], []
        for e, v in d.items():
            z = Z.get(e)
            if z is None or not (lo <= z <= hi) or z - s <= 1 or e in BLEND:
                continue
            xs.append(math.log(z - s)); ys.append(math.log(v))
        if len(xs) < 8:
            continue
        n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
        sxx = sum((x - mx) ** 2 for x in xs)
        p = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
        a = my - p * mx
        ss = sum((y - (a + p * x)) ** 2 for x, y in zip(xs, ys))
        tot = sum((y - my) ** 2 for y in ys)
        r2 = 1 - ss / tot
        if best is None or r2 > best[0]:
            best = (r2, p, s, n)
    return best


print("  MOSELEY FIT PER LINE — exponent p and screening s, Z = 30–92, unblended\n")
print(f"    {'line':<7}{'cell':<14}{'p':>8}{'s':>8}{'R^2':>10}{'n':>5}")
F = {}
for nm in ("L3M1", "L3M4", "L3M5", "L2M1", "L2M4", "L1N2", "L1N3"):
    r2, p, s, n = fit(D[nm])
    F[nm] = (p, s, r2)
    print(f"    {nm:<7}{str(CELL[nm]):<14}{p:>8.4f}{s:>8.2f}{r2:>10.6f}{n:>5}")

print("\n  SAME-CELL AGAINST DIFFERENT-CELL — the declared test\n")
pairs = list(itertools.combinations(CELL, 2))
same = [(a, b) for a, b in pairs if CELL[a] == CELL[b]]
diff = [(a, b) for a, b in pairs if CELL[a] != CELL[b]]


def gap(a, b):
    return abs(F[a][0] - F[b][0]), abs(F[a][1] - F[b][1])


print(f"    {'pair':<16}{'same cell':<12}{'|dp|':>10}{'|ds|':>10}")
for a, b in same:
    dp, ds = gap(a, b)
    print(f"    {a}/{b:<9}{'YES':<12}{dp:>10.4f}{ds:>10.2f}")
for a, b in sorted(diff, key=lambda x: gap(*x)[0])[:6]:
    dp, ds = gap(a, b)
    print(f"    {a}/{b:<9}{'no':<12}{dp:>10.4f}{ds:>10.2f}")

sp = [gap(a, b)[0] for a, b in same]
dpv = [gap(a, b)[0] for a, b in diff]
ss = [gap(a, b)[1] for a, b in same]
dsv = [gap(a, b)[1] for a, b in diff]
print(f"\n    mean |delta p|   same-cell {sum(sp)/len(sp):.4f}   "
      f"different-cell {sum(dpv)/len(dpv):.4f}")
print(f"    mean |delta s|   same-cell {sum(ss)/len(ss):.3f}   "
      f"different-cell {sum(dsv)/len(dsv):.3f}")
better = sum(1 for d in dpv if d > max(sp))
print(f"\n    different-cell pairs whose exponent gap EXCEEDS every same-cell gap: "
      f"{better} of {len(dpv)}")
