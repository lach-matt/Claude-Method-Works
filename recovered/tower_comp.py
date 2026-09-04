#!/usr/bin/env python3
"""tower_comp.py -- does composability reach 100% up the tower?

Register 623: Lambda-8 is 50.3% composable and Lambda-9 is 70.7%. Register 313
says Lambda-8 cannot iterate because its target carries three coordinates
against a source's four, and Lambda-9 composes because 2S' balances them.

PREDICTION under test (Matthew's): the fraction reaches 100% by Lambda-13.

Composable = the cell's target signature is some cell's source signature. The
signature grows with the tower: at each stage the new axis joins whichever end
it describes.
"""
import itertools
from zeno import State, step
from method_tower import base, max2J

def run():
    L8 = [tuple(c) for c in base((3,3,1,3,1))]
    # 0 n  1 l  2 k  3 q  4 e  5 f  6 g  7 2S
    L9  = [c + (s,) for c in L8 for s in range(0, c[6] + 1)]          # 2S' <= g
    L10 = [c + (v,) for c in L9 for v in range(c[8], c[6] + 1)]        # 2S' <= v <= g
    ph = {}; run_ = 0
    for k in range(0, 4):
        m = max((max2J(l, kk) for l in range(0, 2) for kk in range(1, min(4*l+2, k)+1)), default=0)
        run_ = max(run_, m); ph[k] = run_
    L11 = [c + (j,) for c in L10 for j in range(0, ph[c[2]] + 1)]      # 2J_c <= phi(k)
    L12 = [c + (K,) for c in L11 for K in range(abs(c[10] - 2*c[5]), c[10] + 2*c[5] + 1, 2)]
    L13 = [c + (J,) for c in L12 for J in range(max(0, c[11]-1), c[11] + 2)]
    # source and target signatures at each stage
    STAGES = [
        ("Λ₈",  L8,  (0,1,2,7), (4,5,6)),                 # 4 vs 3 — cannot balance
        ("Λ₉",  L9,  (0,1,2,7), (4,5,6,8)),               # 4 vs 4
        ("Λ₁₀", L10, (0,1,2,7), (4,5,6,8)),               # v is a target property
        ("Λ₁₁", L11, (0,1,2,7,10), (4,5,6,8,10)),         # 2J_c on the core
        ("Λ₁₂", L12, (0,1,2,7,10), (4,5,6,8,11)),
        ("Λ₁₃", L13, (0,1,2,7,10), (4,5,6,8,12)),
    ]
    out = []
    for lbl, X, si, ti in STAGES:
        if len(X) > 400000: X = X[:400000]
        S = {tuple(c[i] for i in si) for c in X}
        comp = sum(1 for c in X if tuple(c[i] for i in ti) in S)
        out.append((lbl, len(X), len(si), len(ti), comp, comp/len(X)))
    return out

with State("tower_comp") as st:
    rows = step(st, "composable fraction up the tower", run, budget=1500)

print(f"  {'stage':<7}{'cells':>10}{'src':>5}{'tgt':>5}{'composable':>12}{'fraction':>11}")
for lbl, n, s, t, c, f in rows:
    tag = "  ← 100%" if f == 1.0 else ""
    print(f"  {lbl:<7}{n:>10,}{s:>5}{t:>5}{c:>12,}{f:>11.4f}{tag}")
print(f"\n  prediction: reaches 100% by Λ₁₃")
print(f"  result:     {'CONFIRMED' if rows[-1][5] == 1.0 else 'REFUTED — highest is %.4f' % max(r[5] for r in rows)}")