#!/usr/bin/env python3
# fkscale.py (s39, item 1) — F^k FEASIBILITY INTERVAL. No SCF. Arithmetic on the banked s38 table only.
# gap(lam) = gapHF + lam*(gapTERM - gapHF).  A row is CORRECT when sign(gap) matches the record subshell.
# Record column RECALLED-NOT-ENTERED, comparison only.  NO lam IS ADOPTED.
import sys

# Z, el, class, gapHF, gapTERM, record ('d' -> gap must be > 0 ; 's' -> gap must be < 0)
ROWS = [
    (21, "Sc", "A", -0.0637, -0.0689, "s"),
    (39, "Y",  "A", -0.0029, -0.0105, "s"),
    (57, "La", "A", -0.0335, -0.0404, "s"),
    (58, "Ce", "C", -0.0308, -0.0497, "s"),
    (64, "Gd", "C", -0.0002, -0.0344, "s"),
    (71, "Lu", "A",  0.0516,  0.0418, "d"),
    (72, "Hf", "B",  0.0279, -0.0168, "d"),
    (89, "Ac", "A",  0.0240,  0.0149, "d"),
    (90, "Th", "B",  0.0083, -0.0304, "s"),
    (91, "Pa", "C",  0.0241, -0.0198, "d"),
    (92, "U",  "C",  0.0267, -0.0237, "d"),
    (96, "Cm", "C",  0.0463, -0.0009, "d"),
    (104,"Rf", "B",  0.0914,  0.0433, "d"),
]

def gap(r, lam):
    _, _, _, g0, g1, _ = r
    return g0 + lam * (g1 - g0)

def ok(r, lam):
    return (gap(r, lam) > 0) if r[5] == "d" else (gap(r, lam) < 0)

def crossing(r):
    """lam* where gap changes sign, or None if no crossing in [0,1]."""
    _, _, _, g0, g1, _ = r
    D = g1 - g0
    if D == 0:
        return None
    lam = -g0 / D
    return lam if 0.0 <= lam <= 1.0 else None

print("PER-ROW CROSSINGS (lam* = -gapHF / (gapTERM - gapHF))")
print("   Z el  cl   gapHF  gapTERM       D   rec  lam*      role")
cross = []
for r in ROWS:
    Z, el, cl, g0, g1, rec = r
    D = g1 - g0
    lam = crossing(r)
    if lam is None:
        role = "no crossing"
        ls = "   -  "
    else:
        role = "WRONG->RIGHT" if (not ok(r, 0.0)) else "RIGHT->WRONG"
        ls = "%.4f" % lam
        cross.append((lam, el, role))
    print(" %3d %-3s %s  %7.4f %8.4f %8.4f    %s  %s  %s" % (Z, el, cl, g0, g1, D, rec, ls, role))

lo = [c for c in cross if c[2] == "WRONG->RIGHT"]
hi = [c for c in cross if c[2] == "RIGHT->WRONG"]
print()
print("gains (wrong->right):", ", ".join("%s %.4f" % (e, l) for l, e, _ in sorted(lo)))
print("losses (right->wrong):", ", ".join("%s %.4f" % (e, l) for l, e, _ in sorted(hi)))

L = max([l for l, _, _ in lo]) if lo else 0.0
U = min([l for l, _, _ in hi]) if hi else 1.0
print()
print("lower bound (last gain)  L = %.4f  set by %s" % (L, [e for l, e, _ in lo if l == L][0] if lo else "-"))
print("upper bound (first loss) U = %.4f  set by %s" % (U, [e for l, e, _ in hi if l == U][0] if hi else "-"))
print("FEASIBLE" if L < U else "INFEASIBLE", "  interval = (%.4f, %.4f)" % (L, U) if L < U else "  empty")

# score curve, scanned on a grid only to EXHIBIT the shape (no value adopted)
print()
print("score(lam):")
prev = None
for i in range(0, 101):
    lam = i / 100.0
    s = sum(1 for r in ROWS if ok(r, lam))
    if s != prev:
        print("   lam >= %.2f  ->  %d/13" % (lam, s))
        prev = s

# 13/13 window verified by direct evaluation, independent of the crossing algebra
w = [i / 1000.0 for i in range(1001) if sum(1 for r in ROWS if ok(r, i / 1000.0)) == 13]
print()
if w:
    print("direct check: 13/13 on lam in [%.3f, %.3f]  (%d grid points)" % (min(w), max(w), len(w)))
else:
    print("direct check: 13/13 attained at NO lam in [0,1]")
