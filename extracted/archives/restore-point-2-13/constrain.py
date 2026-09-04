#!/usr/bin/env python3
"""constrain.py -- what constraint is Lambda_spectra missing?

Register 1177. The index is not under-coordinatised: every available fifth coordinate is
DERIVED, and adding one multiplies the corners by between 70% and 652% because a derived
coordinate enlarges the ambient product without constraining it (register 1122).

It is under-CONSTRAINED. 2,202 cells are admitted by the four-way envelope alone — no
three-axis slice admits them, geometry admits 28%, statistics admits ONE. A constraint
that ruled them out would close the index without adding an axis.

So the question is what constraint. Lambda has eight coordinates and E = 0, and its
constraints are stated: l < n, k <= 4l+2, e <= k, and so on. Lambda_spectra has four
coordinates and ONE stated constraint, charge <= Z. That asymmetry is the whole finding.

METHOD. Take the 2,202 corners and ask what is TRUE of every held cell and FALSE of
them. A predicate that separates the two sets perfectly is the missing constraint. A
predicate that separates them partly is a constraint with exceptions, which is worth
knowing about too.

WHAT WOULD CONFIRM. A predicate, statable in the coordinates, true on all 391 held cells
and false on a large fraction of the corners. WHAT WOULD REFUTE. No predicate does
better than the cell counts alone would predict, which would say the corners are not
separable and the looseness is irreducible at four coordinates.
"""
import itertools, math, re
from itertools import product
from collections import defaultdict
from zeno import State, step

exec(open("slices.py", encoding="utf-8").read().split("with State(")[0]
     .replace("from zeno import State, step", ""))

def corners_and_faces():
    H, INV = load()
    o4 = op_order(H, 4)
    seen = set()
    for axis, keep in ((0,(1,2,3)), (1,(0,2,3)), (2,(0,1,3)), (3,(0,1,2))):
        for v in sorted({c[axis] for c in H}):
            S = {tuple(c[i] for i in keep) for c in H if c[axis] == v}
            if len(S) < 4: continue
            amb = 1
            for i in range(3): amb *= len({c[i] for c in S})
            if amb > 60000: continue
            for x in op_order(S, 3):
                full = [0,0,0,0]; full[axis] = v
                for k, i in enumerate(keep): full[i] = x[k]
                seen.add(tuple(full))
    return H, INV, (o4-H)-seen, (o4-H)&seen

def predicates():
    """every constraint statable in (Z, charge, l, multiplicity), plus the ones Lambda
    states about its own coordinates, translated where they translate."""
    ns = {}
    exec(open("aufbau.py", encoding="utf-8").read().split("with State(")[0]
         .replace("from zeno import State, step", ""), ns)
    config, mults = ns["config"], ns["mults"]
    NOBLE = [0,2,10,18,36,54,86,118]
    def n0(ne, l):
        v = [n for n, ll, occ in config(ne) if ll == l and occ > 0]
        return (max(v)+1) if v else l+1
    return [
      ("charge ≤ Z                      the index's only stated constraint",
       lambda Z,c,l,S: c <= Z),
      ("Nₑ ≥ 1                          at least one electron",
       lambda Z,c,l,S: Z-c+1 >= 1),
      ("the multiplicity is ALLOWED     Hund on the core, register 1139",
       lambda Z,c,l,S: S == 0 or S in mults(Z-c+1)),
      ("ℓ < n₀                          the Rydberg orbital exists",
       lambda Z,c,l,S: l < n0(Z-c, l)),
      ("ℓ ≤ Nₑ + 2                      the orbital is reachable from the core",
       lambda Z,c,l,S: l <= (Z-c) + 2),
      ("2S+1 ≤ Nₑ + 1                   the multiplicity fits the electrons",
       lambda Z,c,l,S: S == 0 or S <= (Z-c+1) + 1),
      ("charge ≤ Nₑ + ℓ                 the charge is bounded by what surrounds it",
       lambda Z,c,l,S: c <= (Z-c) + l + 1),
      ("ℓ ≤ 2·(the core's outer n)      the orbital is bounded by the core's extent",
       lambda Z,c,l,S: l <= 2*(config(Z-c)[-1][0] if config(Z-c) else 1)),
      ("Z ≥ c + ℓ − 3                   a joint bound on all three",
       lambda Z,c,l,S: Z >= c + l - 3),
      ("Nₑ ≥ ℓ − 2                      enough electrons for that orbital",
       lambda Z,c,l,S: (Z-c+1) >= l - 2),
    ]

def run():
    H, INV, corners, faces = corners_and_faces()
    P = predicates()
    rows = []
    for name, f in P:
        held = sum(1 for x in H if f(*x))
        cut  = sum(1 for x in corners if not f(*x))
        cutf = sum(1 for x in faces if not f(*x))
        rows.append((name, held, len(H), cut, len(corners), cutf, len(faces)))
    return H, corners, faces, rows

with State("constrain") as s:
    H, CORN, FACE, ROWS = step(s, "test every statable constraint", run, budget=900)

print("  WHAT CONSTRAINT IS Λ_spectra MISSING?\n")
print(f"      {len(H)} cells held · {len(CORN):,} corners · {len(FACE):,} faces\n")
print("  A constraint must be TRUE on every held cell. Its value is how many")
print("  corners it then rules out.\n")
print(f"  {'constraint':<58}{'holds':>9}{'corners cut':>13}{'faces cut':>11}")
for name, held, nH, cut, nC, cutf, nF in sorted(ROWS, key=lambda r: -r[3]):
    ok = "ALL" if held == nH else f"{held}/{nH}"
    print(f"  {name:<58}{ok:>9}{f'{cut}/{nC}':>13}{f'{cutf}/{nF}':>11}")
print()
valid = [r for r in ROWS if r[1] == r[2] and r[3] > 0]
print(f"  {len(valid)} constraints hold on every held cell AND cut corners:\n")
for name, held, nH, cut, nC, cutf, nF in sorted(valid, key=lambda r: -r[3]):
    print(f"      {name.split('  ')[0]:<34}cuts {100*cut/nC:>3.0f}% of corners,"
          f" {100*cutf/nF:>3.0f}% of faces")
