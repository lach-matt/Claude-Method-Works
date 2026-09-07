#!/usr/bin/env python3
"""bundling.py — §14.3's bundling claim, and the evidence it cites. Phase 1, item E-033.

WHAT §14.3 SAYS, in one paragraph:

  "What fails is bundling. R reconstructs coordinate by coordinate, so folding two chains into one
   non-chain coordinate hides structure from it. In tests, the same sets presented bundled and
   presented decomposed both gave 80/80 AGREEMENT — the theorem survives, but only when the
   presentation respects it."

THE TENSION IS IN THE PARAGRAPH, not in any data. The claim is that presentation matters; the
evidence offered is a test in which it did NOT matter -- 80 out of 80 both ways is a report that
bundling changed nothing. A reader asked to believe that bundling breaks something is shown a test
where bundling broke nothing.

WHAT THIS INSTRUMENT SETTLES. The claim is TRUE and demonstrable, and the demonstration is small
enough to print. There is a three-cell set on the 2x2x2 box whose decomposed presentation has
E = 1 and whose bundled presentation has E = 0: folding two coordinates into one makes R blind to a
defect it otherwise finds. So the chapter is right about the mechanism and cites the wrong
experiment for it.

AND THE REASON IS GENERAL, which is why no search was needed to be sure one existed: with TWO
coordinates R(X) = X for every X, because the only pairwise projection is the set itself. Bundling
any presentation down to two coordinates therefore always reports closure. Verified here on three
thousand random sets and provable in one line.

stdlib only.  --selftest asserts the counterexample and the general fact.
"""
import argparse, itertools, random, sys

PRINTED = "80/80 agreement, bundled and decomposed"
MINIMAL = [(0, 0, 0), (0, 1, 1), (1, 0, 1)]


def R2(X, dims):
    """the closure the book calls R: every tuple whose every 2-D projection lies in X's."""
    A = [sorted({x[i] for x in X}) for i in range(dims)]
    proj = {(i, j): {(x[i], x[j]) for x in X}
            for i in range(dims) for j in range(dims) if i < j}
    return {t for t in itertools.product(*A) if all((t[i], t[j]) in proj[(i, j)] for i, j in proj)}


def bundle(X):
    """fold coordinates 1 and 2 into one non-chain coordinate, as §14.3 describes."""
    return {(x[0], (x[1], x[2])) for x in X}


def E(X, dims):
    return len(R2(X, dims)) - len(X)


def report():
    X = set(MINIMAL)
    dec, bun = E(X, 3), E(bundle(X), 2)
    print("§14.3's bundling claim, and the experiment it cites\n")
    print(f"  the paragraph's evidence: \"{PRINTED}\" — a test in which bundling changed NOTHING")
    print("  the paragraph's conclusion: \"the theorem survives, but only when the presentation")
    print("  respects it\" — which requires a case in which bundling changes SOMETHING.\n")
    print(f"  A three-cell counterexample on the 2×2×2 box: {sorted(X)}")
    print(f"    presented decomposed, three chain coordinates:  E = {dec}")
    print(f"    presented bundled, coordinates 1 and 2 folded:  E = {bun}")
    added = sorted(R2(X, 3) - X)
    print(f"    the cell the decomposed closure adds and the bundled one cannot see: {added}")
    print("\n  So the claim is TRUE and the cited experiment does not show it.")
    print("\n  The reason is general, and it is one line: with two coordinates the only pairwise")
    print("  projection is the set itself, so R(X) = X for EVERY X. Any presentation bundled down")
    print("  to two coordinates reports closure whatever it contains. Bundling does not hide a")
    print("  defect by accident; at two coordinates it cannot do anything else.")
    print("\n  RECORDED, NOT REPAIRED. The chapter is right about the mechanism; the sentence that")
    print("  supports it needs an experiment that exhibits it, and one is printed above.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    X = set(MINIMAL)
    eq("the counterexample has three cells", len(X), 3)
    eq("decomposed, E = 1", E(X, 3), 1)
    eq("bundled, E = 0", E(bundle(X), 2), 0)
    eq("so bundling hides exactly one cell", E(X, 3) - E(bundle(X), 2), 1)
    random.seed(1); every = True
    for _ in range(3000):
        Y = {t for t in itertools.product(range(4), range(4)) if random.random() < 0.5}
        if Y and R2(Y, 2) != Y: every = False; break
    eq("with two coordinates R(X) = X, on 3,000 random sets", every, True)
    eq("and so bundling to two coordinates always reports E = 0",
       all(E(bundle(set(random.sample(list(itertools.product(range(3), range(3), range(3))), 8))), 2) == 0
           for _ in range(200)), True)
    eq("a set that is already closed stays closed decomposed", E(set(itertools.product(range(2), repeat=3)), 3), 0)
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
