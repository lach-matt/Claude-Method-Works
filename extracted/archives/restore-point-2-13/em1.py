#!/usr/bin/env python3
"""em1.py -- validate the multipole map BEFORE using it.

The map has been wrong twice. §4.6: a check must be shown capable of returning a
failure before its passing is evidence. So the map is tested against transitions
whose classification is textbook, INCLUDING cases it must refuse.

THE RULES, one-electron jump, stated as they are in Condon–Shortley and Cowan:
  Eγ  requires parity change (−1)^γ   and  |Δℓ| ≤ γ,  |ΔJ| ≤ γ,  γ ≥ 1
  Mγ  requires parity change (−1)^(γ+1) and same angular bounds
  for a single active electron the parity change IS (−1)^{Δℓ}
  so  E-type: Δℓ ≡ γ (mod 2)   ·   M-type: Δℓ ≡ γ+1 (mod 2)
  and J = 0 → J = 0 is forbidden at every multipole
"""
import sys
from zeno import State, step

GMAX = 5
def multipole(dl, dJ2=None):
    """the lowest multipole carrying a jump of |Δℓ| = dl.
    dJ2 is |ΔJ| in units of 2J, or None when J is not available."""
    lo = max(dl, 1)
    if dJ2 is not None:
        lo = max(lo, (dJ2 + 1) // 2)
    for g in range(lo, GMAX + 1):
        for t in (0, 1):                       # 0 electric, 1 magnetic
            if (dl % 2) == ((g + t) % 2):
                if dJ2 is not None and dJ2 > 2 * g: continue
                return g, t
    return None

NAME = lambda g, t: f"{'M' if t else 'E'}{g}"

CASES = [
 # (description, |Δℓ|, |ΔJ| in 2J units, expected)
 ("1s → 2p           s→p, parity changes",        1, 2, "E1"),
 ("2p → 3d           p→d, parity changes",        1, 2, "E1"),
 ("2s → 3s           s→s, parity unchanged",      0, 0, "M1"),
 ("2p → 3p           p→p, parity unchanged",      0, 2, "M1"),
 ("3d → 4s           d→s, parity unchanged",      2, 4, "E2"),
 ("2s → 3d           s→d, parity unchanged",      2, 4, "E2"),
 ("2p → 4f           p→f, parity changes",        3, 6, "E3"),
 ("s → p with ΔJ = 2 (in J units)",               1, 4, "E3"),
 ("p → d demanding ΔJ = 3 (in J units)",          1, 6, "E3"),
]
REFUSALS = [
 ("|Δℓ| = 6 beyond the truncation", 6, 12),
]

def run():
    ok = bad = 0; rows = []
    for desc, dl, dj, exp in CASES:
        r = multipole(dl, dj)
        got = NAME(*r) if r else "none"
        good = got == exp
        ok += good; bad += not good
        rows.append((desc, dl, dj, exp, got, good))
    ref = []
    for desc, dl, dj in REFUSALS:
        r = multipole(dl, dj)
        ref.append((desc, r is None))
    return rows, ref, ok, bad

with State("em1") as st:
    rows, ref, ok, bad = step(st, "validate the multipole map", run, budget=60)

print(f"  {'case':<44}{'|Δℓ|':>5}{'|ΔJ|₂':>7}{'expect':>8}{'got':>7}")
for desc, dl, dj, exp, got, good in rows:
    print(f"  {desc:<44}{dl:>5}{dj:>7}{exp:>8}{got:>7}   {'.' if good else 'FAIL'}")
print(f"\n  {ok} of {len(rows)} classify correctly, {bad} wrong")
print(f"\n  AND THE MAP MUST BE ABLE TO REFUSE:")
for desc, refused in ref:
    print(f"    {desc:<44}{'refused' if refused else 'ACCEPTED — the map cannot fail'}")
sys.exit(bad)
