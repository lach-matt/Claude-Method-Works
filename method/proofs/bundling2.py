#!/usr/bin/env python3
"""bundling2.py — bundling.py's successor, on the operator the book actually defines. Phase 1, item E-033.

WHY A SUCCESSOR. `bundling.py` implemented ℛ as "every tuple whose every 2-D projection lies in X's".
**That operator is not in this book.** §6.1 defines

    Âᵢ(X) = { xᵢ : x ∈ X }        φ̂ᵢⱼ(v) = max{ xᵢ : x ∈ X, xⱼ ≤ v }
    ℛ(X)  = { x ∈ ∏ Âᵢ(X) : xᵢ ≤ φ̂ᵢⱼ(xⱼ) for all i ≠ j }

Theorem 14.1 names the same thing — "ℛ reconstructs value sets and pairwise monotone bounds from X's
own extension" — and the Mathematical Compendium's glossary calls it "closure at the (≤,≤) corner of
Deville's staircase class", beside **ℛ₄, "closure over all four orientations"**, with **E − E₄ the
orientation cost**. The raw projection has no monotone envelope in it and is neither of those two.
The predecessor is left in place, superseded, because it is what produced register 1848.

WHAT CHANGES, AND WHAT DOES NOT. §14.3's claim survives: bundling still hides a defect, under both
operators. What the predecessor got wrong is the number and the reason.

    the three cells {(0,0,0), (0,1,1), (1,0,1)} on the 2×2×2 box
                                    ℛ                          ℛ₄
      decomposed              E  = 2, adding (0,0,1)     E₄ = 1, adding (0,0,1)
                                     and (1,1,1)               (orientation cost 1)
      fold coordinates 1 & 2  E  = 0                     E₄ = 0
      fold coordinates 1 & 3  E  = 2                     E₄ = 1
      fold coordinates 2 & 3  E  = 2                     E₄ = 1

So **E = 1 with the single cell (0,0,1) is ℛ₄'s figure**, and register 1848 prints it under the
symbol E. That is the confusion §14.5.3 names in its own title — "Two pairwise operators, and this
book has used one name for both" — and §14.5.3 is a heading with nothing under it.

AND THE GENERAL REASON THE PREDECESSOR OFFERED IS FALSE. "With two coordinates ℛ(X) = X for every X"
holds for the raw projection and for neither book operator: {(0,1), (1,0)} on the 2×2 box closes
under ℛ to all four cells, and over 3,000 random two-coordinate sets ℛ(X) ≠ X in 1,847 and
ℛ₄(X) ≠ X in 1,120. Only ONE of the three folds closes, which is why no reason of that shape exists.
§14.3's own qualifier is the operative condition and this measurement corroborates it: it says
folding into one **non-chain** coordinate, not folding to two coordinates as such.

THE IMPLEMENTATION IS VALIDATED AGAINST THE BOOK'S OWN NUMBER, not against itself: §6.1 prints
E = 36 for the periodic table, and --selftest asserts that this ℛ returns 36 on the seated periodic
index imported from tools/cypher.py. An operator that could not reproduce 36 would not be ℛ.

stdlib only, except that --selftest imports cypher.py for the periodic index (a seated instrument,
imported by path and never copied).
"""
import argparse, itertools, os, random, sys

MINIMAL = [(0, 0, 0), (0, 1, 1), (1, 0, 1)]
CORNERS = (("le", "le"), ("le", "ge"), ("ge", "le"), ("ge", "ge"))


def _corner(X, d, si, sj):
    """Closure at one orientation. (le, le) is §6.1's ℛ."""
    X = [tuple(x) for x in X]
    A = [sorted({x[i] for x in X}) for i in range(d)]
    def bound(i, j, v):
        sel = [x for x in X if (x[j] <= v if sj == "le" else x[j] >= v)]
        if not sel:
            return None
        return max(x[i] for x in sel) if si == "le" else min(x[i] for x in sel)
    out = set()
    for t in itertools.product(*A):
        ok = True
        for i in range(d):
            for j in range(d):
                if i == j:
                    continue
                b = bound(i, j, t[j])
                if b is None or (t[i] > b if si == "le" else t[i] < b):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.add(t)
    return out


def R(X, d):
    """§6.1 / Theorem 14.1 / the glossary's (≤,≤) corner."""
    return _corner(X, d, "le", "le")


def R4(X, d):
    """§14.5.5's closure over all four orientations."""
    s = None
    for si, sj in CORNERS:
        c = _corner(X, d, si, sj)
        s = c if s is None else (s & c)
    return s


def E(X, d):   return len(R(X, d)) - len(set(map(tuple, X)))
def E4(X, d):  return len(R4(X, d)) - len(set(map(tuple, X)))


def fold(X, i, j):
    """Bundle coordinates i and j into one, keeping the remaining coordinate."""
    rest = [k for k in range(len(X[0])) if k not in (i, j)]
    span = max(x[j] for x in X) + 1
    return [tuple([x[i] * span + x[j]] + [x[k] for k in rest]) for x in X]


def _periodic():
    """The seated periodic index, imported from tools/cypher.py — never reimplemented."""
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(here, "..", "..", "tools"))
    import cypher
    return [tuple(c) for c in cypher._periodic().cells]


def report():
    n = len(set(MINIMAL))
    print("§14.3's bundling claim, on the operator §6.1 defines\n")
    print("  ℛ  = closure at the (≤,≤) corner: xᵢ ≤ φ̂ᵢⱼ(xⱼ), φ̂ᵢⱼ(v) = max{xᵢ : xⱼ ≤ v}")
    print("  ℛ₄ = the same over all four orientations;  E − E₄ is the orientation cost\n")
    print("  validation, against the book's own printed number:")
    p = _periodic()
    print("    periodic table, 90 cells on 2 coordinates -> E = %d   (§6.1 prints 36)\n" % E(p, 2))
    print("  the three cells {(0,0,0), (0,1,1), (1,0,1)} on the 2×2×2 box\n")
    print("    %-24s %-30s %s" % ("", "ℛ", "ℛ₄"))
    print("    %-24s E  = %d, adding %-16s E₄ = %d, adding %s"
          % ("decomposed", E(MINIMAL, 3), str(sorted(set(R(MINIMAL, 3)) - set(MINIMAL))),
             E4(MINIMAL, 3), sorted(set(R4(MINIMAL, 3)) - set(MINIMAL))))
    for i, j in ((0, 1), (0, 2), (1, 2)):
        B = fold(MINIMAL, i, j)
        print("    %-24s E  = %-25d E₄ = %d"
              % ("fold coordinates %d & %d" % (i + 1, j + 1), E(B, 2), E4(B, 2)))
    print("\n  So bundling DOES hide a defect and §14.3's claim stands — 2 → 0 under ℛ and 1 → 0")
    print("  under ℛ₄ — while E = 1 with the single cell (0,0,1) is ℛ₄'S figure, which register")
    print("  1848 printed under the symbol E. §14.5.3 names that confusion in its own title and")
    print("  is a heading with nothing under it.\n")
    S = [(0, 1), (1, 0)]
    print("  and the general reason 1848 offered is false under both operators:")
    print("    {(0,1),(1,0)} on the 2×2 box:  ℛ -> %s ;  ℛ₄ -> %s"
          % (sorted(R(S, 2)), sorted(R4(S, 2))))
    random.seed(11)
    a = b = 0
    for _ in range(3000):
        k, m = random.randint(2, 5), random.randint(2, 5)
        X = sorted({(random.randrange(k), random.randrange(m)) for _ in range(random.randint(2, 8))})
        if R(X, 2) != set(X):  a += 1
        if R4(X, 2) != set(X): b += 1
    print("    of 3,000 random two-coordinate sets: ℛ(X) ≠ X in %d, ℛ₄(X) ≠ X in %d" % (a, b))
    print("    only ONE of the three folds closes, so no reason of that shape exists.")
    print("    §14.3's own qualifier — into one NON-CHAIN coordinate — is the operative condition.")
    print("\n  RECORDED, NOT REPAIRED.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print("  OK   %s: %s" % (name, got))
        else: fail += 1; print("  FAIL %s: got %s, want %s" % (name, got, want))
    eq("ℛ reproduces §6.1's printed E for the periodic table", E(_periodic(), 2), 36)
    eq("the three cells, decomposed, under ℛ", E(MINIMAL, 3), 2)
    eq("and the cells ℛ adds", sorted(set(R(MINIMAL, 3)) - set(MINIMAL)), [(0, 0, 1), (1, 1, 1)])
    eq("the three cells, decomposed, under ℛ₄", E4(MINIMAL, 3), 1)
    eq("and the cell ℛ₄ adds — this is register 1848's figure",
       sorted(set(R4(MINIMAL, 3)) - set(MINIMAL)), [(0, 0, 1)])
    eq("the orientation cost E − E₄", E(MINIMAL, 3) - E4(MINIMAL, 3), 1)
    eq("folding coordinates 1 and 2 closes under ℛ", E(fold(MINIMAL, 0, 1), 2), 0)
    eq("and under ℛ₄", E4(fold(MINIMAL, 0, 1), 2), 0)
    eq("so §14.3's claim stands: a defect is hidden by the fold",
       E(MINIMAL, 3) > 0 and E(fold(MINIMAL, 0, 1), 2) == 0, True)
    eq("the OTHER two folds do not close under ℛ",
       [E(fold(MINIMAL, i, j), 2) for i, j in ((0, 2), (1, 2))], [2, 2])
    eq("nor under ℛ₄", [E4(fold(MINIMAL, i, j), 2) for i, j in ((0, 2), (1, 2))], [1, 1])
    eq("at two coordinates ℛ is NOT the identity — {(0,1),(1,0)} closes to the box",
       sorted(R([(0, 1), (1, 0)], 2)), [(0, 0), (0, 1), (1, 0), (1, 1)])
    random.seed(11)
    a = b = 0
    for _ in range(3000):
        k, m = random.randint(2, 5), random.randint(2, 5)
        X = sorted({(random.randrange(k), random.randrange(m)) for _ in range(random.randint(2, 8))})
        if R(X, 2) != set(X):  a += 1
        if R4(X, 2) != set(X): b += 1
    eq("of 3,000 random two-coordinate sets, ℛ(X) ≠ X in", a, 1847)
    eq("and ℛ₄(X) ≠ X in", b, 1120)
    print("\nOK: %d  FAIL: %d" % (ok, fail))
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
