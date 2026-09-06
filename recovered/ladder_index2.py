"""
Lambda_ladder, rebuilt.

Register 1356 held four ladders on two axes and E = 0 was an artefact of one
cell per row. Three things change here:

  1. THE SPECIES FAMILY IS SIX, NOT FOUR. Z = Ne + c - 1 gives three
     (isoelectronic, the walk, ionisation). The nuclide chart carries the exact
     parallel relation A = Z + N, which gives three more the same way
     (isotopic, isotonic, isobaric). Arithmetic, no collection.

  2. THERE IS A SECOND FAMILY. A species ladder varies WHICH atom; a state
     ladder fixes the species and varies which level of it. The work already
     propagates along two of these (P.lcollapse in l, the Rydberg series in n)
     and measures a step ratio for l at s of 1.416 over 62 pairs, without ever
     indexing them as ladders.

  3. THREE AXES, NEVER TWO. K.three: an index needs three coordinates before
     its languages can disagree, so a 2-axis E carries no information.

The axes, and they are DECISIONS, flagged as such:
    family  species | state
    seat    which Lambda_chem seat the ladder reaches
    moves   which Lambda coordinate the rung variable moves; `none` where the
            ladder moves nothing Lambda carries, `tower` where it moves an
            axis only the tower has.
"""
from itertools import product, permutations

FAMILY = ["species", "state"]
SEAT   = ["nucleus", "core", "subvalence", "valence"]
MOVES  = ["none", "configuration", "n", "l", "2S", "tower"]

#  name                family seat moves   fixes / status
LAD = [
 ("isoelectronic",       0, 3, 1, "fixes Ne      · 11 of 11"),
 ("the walk",            0, 3, 1, "fixes c       · 106 of 106"),
 ("ionisation",          0, 2, 1, "fixes Z       · 15 of 108, +H,He,Li today"),
 ("isotopic",            0, 0, 0, "fixes Z,Ne,c  · mass-shift rung computed"),
 ("isotonic",            0, 0, 1, "fixes N       · NEW, untraced"),
 ("isobaric",            0, 0, 1, "fixes A       · NEW, untraced"),
 ("the Rydberg series",  1, 3, 2, "fixes species · every delta in COORDINATES"),
 ("the l-ladder",        1, 3, 3, "fixes species,n · P.lcollapse, 62 pairs"),
 ("the term ladder",     1, 3, 4, "fixes species,cfg · Q.exch, 66 pairs"),
 ("the outer-j ladder",  1, 3, 5, "fixes species,cfg · P.jsplit, 227x"),
 ("the parent-term",     1, 1, 5, "fixes species · P.termsplit, 12 of 15"),
 ("the isomeric",        1, 0, 0, "fixes Z,N,electrons · NEW, untraced"),
]

def opR(X, d):
    X = set(X); vals = [sorted({x[i] for x in X}) for i in range(d)]
    def env(i, j):
        m = {}
        for x in X: m[x[j]] = max(m.get(x[j], -10**9), x[i])
        b, o = -10**9, {}
        for t in sorted(m): b = max(b, m[t]); o[t] = b
        return o
    phi = {(i,j): env(i,j) for i in range(d) for j in range(d) if i != j}
    return {x for x in product(*vals)
            if all(x[i] <= phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i != j)}

def minE(cells, axes):
    best, arg = None, None
    for p in product(*[permutations(range(a)) for a in axes]):
        cs = {tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E = len(opR(cs, len(axes))) - len(cs)
        if best is None or E < best: best, arg = E, p
    return best, arg

if __name__ == "__main__":
    print("  Λ_ladder — REBUILT OVER BOTH FAMILIES\n")
    print(f"      {'ladder':<22}{'family':<10}{'seat':<13}{'moves':<15}status")
    for nm, f, s, m, note in LAD:
        print(f"      {nm:<22}{FAMILY[f]:<10}{SEAT[s]:<13}{MOVES[m]:<15}{note}")

    cells = {(f, s, m) for _, f, s, m, _ in LAD}
    print(f"\n  {len(LAD)} ladders occupy {len(cells)} distinct cells.")
    coll = {}
    for nm, f, s, m, _ in LAD: coll.setdefault((f,s,m), []).append(nm)
    for k, v in coll.items():
        if len(v) > 1:
            print(f"      COLLISION: {' and '.join(v)} share ({FAMILY[k[0]]}, "
                  f"{SEAT[k[1]]}, {MOVES[k[2]]})")

    axes = [len(FAMILY), len(SEAT), len(MOVES)]
    E, p = minE(cells, axes)
    print(f"\n  CLOSURE : {len(cells)} cells · box {axes[0]*axes[1]*axes[2]} · min E = {E}")
    print(f"      family order : {' < '.join(FAMILY[i] for i in p[0])}")
    print(f"      seat order   : {' < '.join(SEAT[i]   for i in p[1])}")
    print(f"      moves order  : {' < '.join(MOVES[i]  for i in p[2])}")
