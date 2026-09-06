#!/usr/bin/env python3
"""ladder_index.py -- Lambda_ladder, the index of the ladders themselves.

A ladder is a walk holding something fixed and varying the rest. Every result in
the Loewdin work came from one, and until register 1356 they were never indexed
as objects in their own right.

SUPERSEDES the version that carried `state` -- complete/partial/none -- on an
axis. That is the observer on an object axis, the fault that killed `standing` in
Lambda_const, `origin` in Lambda_var and `kind` in Lambda_phys. Register 1356
withdrew it; the code kept printing it, and E = 0 with it, until register 1384.
It also ABSORBS ladder_index2.py, now deleted: two scripts for one index is the
same class of hazard as a generated artefact with a hand-edited region (R 1373).

THE TWO RELATIONS

    Z = Ne + c - 1      the electronic relation, on Lambda
    A = Z + N           the nuclear relation, on the nuclide chart

Each is ONE linear relation on three named quantities, so fixing each in turn
gives three ladders -- six in all (R 1374). The nuclear three are not a single
"isotopic" direction; that undercount is what 1356 carried.

THE SECOND FAMILY

A SPECIES ladder varies which atom or ion. A STATE ladder fixes the species
entirely and varies which level of it. The work propagates along two of these
already -- the Rydberg series in n, and P.lcollapse in l, whose step ratio A.S
measures at 1.416 over 62 pairs -- without ever indexing them as ladders.

WHY THE OLD ANSWER WAS EMPTY

At four ladders `fixes` is injective by construction: a ladder IS named by what
it holds fixed. One cell per row, and the ordering that monotonises it always
exists, so E = 0 was FORCED -- 2% of admissible arrangements could refuse. At six,
ionisation and isotopic BOTH fix Z, `fixes` stops individuating, and the zero
becomes earnable. R 1374, 1375; see contingency.py.
"""
from itertools import product, permutations

FAMILY = ["species", "state"]
SEAT   = ["nucleus", "core", "subvalence", "valence"]
KIND   = ["counting", "coupling"]                     # T.dich, a proved dichotomy
ZCROSS = ["within one element", "across elements"]    # K.zcross

#  name                    family seat kind zcross   what it fixes / status
LAD = [
 ("isoelectronic",            0, 3, 0, 1, "fixes Ne          · 11 of 11"),
 ("the walk",                 0, 3, 0, 1, "fixes c           · 106 of 106"),
 ("ionisation",               0, 2, 0, 0, "fixes Z           · 15 of 108 (+H,He,Li)"),
 ("isotopic",                 0, 0, 0, 0, "fixes Z,Ne,c      · 1 rung traced, R 1381"),
 ("isotonic",                 0, 0, 0, 1, "fixes N           · NEW R 1374, untraced"),
 ("isobaric",                 0, 0, 0, 1, "fixes A           · NEW R 1374, untraced"),
 ("the Rydberg series",       1, 3, 0, 0, "fixes species     · every delta held"),
 ("the l-ladder",             1, 3, 0, 0, "fixes species,n   · P.lcollapse, 62 pairs"),
 ("the term ladder",          1, 3, 1, 0, "fixes species,cfg · Q.exch, 66 pairs"),
 ("the outer-j ladder",       1, 3, 1, 0, "fixes species,cfg · P.jsplit, 227x"),
 ("the parent-term ladder",   1, 1, 1, 0, "fixes species     · P.termsplit, 12/15"),
 ("the isomeric",             1, 0, 0, 0, "fixes Z,N,e-      · NEW, untraced"),
]

def opR(X, d):
    X = set(X); vals = [sorted({x[i] for x in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for x in X: m[x[j]] = max(m.get(x[j], -10**9), x[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i, j): env(i, j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i != j)}

def minE(cells, axes, want_defects=False):
    best, arg = None, None
    for p in product(*[permutations(range(a)) for a in axes]):
        cs = {tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E = len(opR(cs, len(axes))) - len(cs)
        if best is None or E < best: best, arg = E, p
    if not want_defects: return best
    inv = [{arg[i].index(v): v for v in range(axes[i])} for i in range(len(axes))]
    cs = {tuple(arg[i].index(x[i]) for i in range(len(axes))) for x in cells}
    return best, [tuple(inv[i][x[i]] for i in range(len(axes)))
                  for x in sorted(opR(cs, len(axes)) - cs)]

if __name__ == "__main__":
    print("  Λ_ladder — THE LADDERS AS OBJECTS   (R 1356, 1374, 1375, 1384)\n")
    print("      Z = Nₑ + c − 1  and  A = Z + N — two relations, three ladders each.")
    print("      No ladder varies Z alone: forbidden by arithmetic, not by data.\n")
    print(f"      {'ladder':<24}{'family':<9}{'seat':<12}{'kind':<10}{'crosses Z':<20}status")
    for nm, f, s, k, z, note in LAD:
        print(f"      {nm:<24}{FAMILY[f]:<9}{SEAT[s]:<12}{KIND[k]:<10}{ZCROSS[z]:<20}{note}")

    cells = {(s, k, z) for _, _, s, k, z, _ in LAD}
    axes = [len(SEAT), len(KIND), len(ZCROSS)]
    E, defects = minE(cells, axes, want_defects=True)
    print(f"\n  CLOSURE on seat × kind × Zcross")
    print(f"      {len(LAD)} ladders occupy {len(cells)} cells in a box of "
          f"{axes[0]*axes[1]*axes[2]} · min E = {E}")
    coll = {}
    for nm, _, s, k, z, _ in LAD: coll.setdefault((s,k,z), []).append(nm)
    for key, v in coll.items():
        if len(v) > 1: print(f"      SHARED CELL: {' and '.join(v)}")
    for d in defects:
        print(f"      DEFECT: ({SEAT[d[0]]}, {KIND[d[1]]}, {ZCROSS[d[2]]})")
    print("      the defect sits at the SUBVALENCE seat — the two directions")
    print("      ionisation does not go. That is what demanded Λ_xray (R 1378).")

    print("\n  CONTINGENCY (R 1383) — every E is reported with its rate.")
    print("      4 ladders, `fixes` injective : E = 0 FORCED, 2% could refuse")
    print("      run contingency.py to label the figure above")

    print("\n  WHAT EACH LADDER MEASURES THAT NO OTHER CAN\n")
    for a, b in [("isoelectronic","the crossing charge — a_cross is fixed by the pair"),
                 ("the walk","the corridor sequence and the eighteen resets"),
                 ("ionisation","t above c = 1, and Λ_t's empty cells"),
                 ("isotopic","the field shift — traced at the K shell, R 1381"),
                 ("isotonic","whether the electronic laws move with N at fixed Z−N"),
                 ("isobaric","the proton/neutron trade at fixed nucleon count"),
                 ("the Rydberg series","delta itself — every value in COORDINATES.tsv"),
                 ("the l-ladder","the l-collapse, and the step ratio 1.416"),
                 ("the term ladder","the exchange splitting, where Q.exch failed"),
                 ("the outer-j ladder","fine structure at the valence shell"),
                 ("the parent-term ladder","the core's angular structure"),
                 ("the isomeric","nuclear excitation — the state analogue, untraced")]:
        print(f"      {a:<24}{b}")