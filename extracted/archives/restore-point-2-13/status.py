#!/usr/bin/env python3
"""status.py -- what exists, what might, what cannot, and what certainly cannot.

Register 1178. The survey admits 101,328 cells and only 1,755 are extractable as a
separable Rydberg series. Every accuracy figure today has been quoted against a
denominator that mixes cells nobody will ever measure with cells that are measured.

Before any further fitting, the index is partitioned by EXISTENCE STATUS, because a
model fitted across regions of different status is fitted across different objects.

    VERIFIED        a measurement is in hand or published
    POSSIBLE        the ion exists, the series is separable, nobody has done it
    IMPROBABLE      the ion exists and the series is not separable, or the element
                    is too short-lived to hold a spectrum — theoretically reachable
                    and practically not
    IMPOSSIBLE      forbidden by the index's own constraints, with certainty

The last is the only one that is a mathematical statement. The other three are
statements about the world and they are graded, not proved.

WHAT MAKES A CELL IMPOSSIBLE
    charge > Z                  more charges than protons
    Ne < 1                      no electron to excite
    2S+1 not in mults(Ne)       Hund on the core forbids it — register 1139
    l >= n0                     no orbital of that l is available

WHAT MAKES A CELL IMPROBABLE RATHER THAN POSSIBLE
    Z > 103                     no measurable spectrum has ever been taken
    charge > 10                 essentially no analysed Rydberg data exists
    l > 4                       series are not resolved above g in practice
    an open-shell core          many parent terms, no separable series (R 1177)
"""
import json, math, re
from collections import Counter, defaultdict
from zeno import State, step

def setup():
    ns = {}
    exec(open("aufbau.py", encoding="utf-8").read().split("with State(")[0]
         .replace("from zeno import State, step", ""), ns)
    return ns["config"], ns["mults"], ns["measured"]()

def parents(cfg):
    """how many LS parent terms the core's outermost open subshell carries"""
    if not cfg: return 1
    n, l, occ = cfg[-1]
    cap = 2*(2*l+1)
    if occ in (0, cap, 1, cap-1): return 1          # closed, or one electron/hole
    return {0: 1, 1: 3, 2: 16, 3: 119}.get(l, 8)

def classify(Z, c, l, S, config, mults, measured, extra):
    ne = Z - c + 1
    # --- impossible, with certainty
    if c > Z:            return "impossible", "charge exceeds Z"
    if ne < 1:           return "impossible", "no electron"
    if S and S not in mults(ne): return "impossible", "Hund forbids the multiplicity"
    cfg = config(ne-1)
    v = [n for n, ll, occ in cfg if ll == l and occ > 0]
    n0 = (max(v)+1) if v else l+1
    if l >= n0:          return "impossible", "no orbital of that ℓ"
    # --- verified
    if (Z, c, l, S) in measured or (Z, c, l) in extra:
        return "verified", "measured"
    if ne == 1:          return "verified", "hydrogenic, δ = 0 exactly"
    # --- improbable
    if Z > 103:          return "improbable", "element too short-lived"
    if c > 10:           return "improbable", "no analysed Rydberg data at this charge"
    if l > 4:            return "improbable", "series unresolved above ng"
    if parents(cfg) > 1: return "improbable", f"open-shell core, {parents(cfg)} parents"
    if Z > 92:           return "improbable", "not naturally occurring"
    return "possible", "separable series, not yet measured"

def run():
    config, mults, H = setup()
    extra = {(38,2,0),(38,2,1),(38,2,2),(38,2,3),(38,2,4),
             (22,4,0),(22,4,1),(22,4,2),(22,4,3),
             (7,4,0),(7,4,1),(7,4,2),(20,4,0),(20,4,1),(20,4,2),(19,3,0),(19,3,1)}
    cells = []
    for Z in range(1, 119):
        for c in range(1, Z+1):
            ne = Z-c+1
            for S in mults(ne):
                for l in range(8):
                    st, why = classify(Z, c, l, S, config, mults, H, extra)
                    cells.append((Z, c, l, S, st, why))
    return cells

with State("status") as s:
    CELLS = step(s, "classify every cell by existence status", run, budget=900)

n = len(CELLS)
cnt = Counter(x[4] for x in CELLS)
print("  THE INDEX BY EXISTENCE STATUS\n")
print(f"  {'status':<14}{'cells':>10}{'%':>8}   what it means")
MEAN = {"verified":   "measured, or exact by symmetry",
        "possible":   "the ion exists and the series separates — a capture would get it",
        "improbable": "reachable in principle, not in practice",
        "impossible": "forbidden by the index's own constraints"}
for k in ("verified", "possible", "improbable", "impossible"):
    print(f"  {k:<14}{cnt[k]:>10,}{100*cnt[k]/n:>7.1f}%   {MEAN[k]}")
print(f"  {'':<14}{'-'*10}")
print(f"  {'total':<14}{n:>10,}\n")

print("  WHY, IN DETAIL\n")
by = defaultdict(Counter)
for Z, c, l, S, st, why in CELLS: by[st][why] += 1
for k in ("verified", "possible", "improbable", "impossible"):
    print(f"      {k.upper()}")
    for why, v in by[k].most_common():
        print(f"          {why:<44}{v:>9,}")
    print()

print("  THE REGION TO BUILD THE MATH IN\n")
V = cnt["verified"]; P = cnt["possible"]
print(f"      verified + possible = {V+P:,} cells  ({100*(V+P)/n:.1f}% of the index)")
print(f"      of which {V:,} are in hand and {P:,} are one capture each")
print(f"\n      every accuracy figure should be quoted against {V+P:,}, not {n:,}.")
print(f"      the {cnt['improbable']:,} improbable cells are what the equation EXTRAPOLATES to,")
print(f"      and no measurement will ever check it there.")
