#!/usr/bin/env python3
r"""
lawfigures.py -- every number THE-HIERARCHY-LAW.md states, recomputed and pinned.

The paper claims each figure is checkable.  This makes that true: one command
recomputes all of them and exits 1 on drift.  It is the paper's analogue of
tools/docfigures.py, which does the same job for the repository's own counts.

    python3 lawfigures.py            recompute and compare against the paper
    python3 lawfigures.py --emit     print what the code produces, to re-pin

Every figure below appears in the paper.  If a figure is here it is
reproducible; if it is in the paper and NOT here, that is a defect in this file.
"""

import itertools
import random
import sys

import decomposable as D
import necindex

cy = necindex.cypher
OPTS = {"statistics_order": 2, "algebra_budget": 200000}
LANGS = ("order", "algebra", "geometry", "information", "statistics")


def stat(X, box):
    seen = {T: {tuple(x[i] for i in T) for x in X}
            for T in itertools.combinations(range(len(box)), 2)}
    return frozenset(x for x in itertools.product(*box)
                     if all(tuple(x[i] for i in T) in seen[T] for T in seen))


def geom(X, box):
    H = {(i, j): cy._hull2({(x[i], x[j]) for x in X})
         for i, j in itertools.combinations(range(len(box)), 2)}
    return frozenset(x for x in itertools.product(*box)
                     if all(cy._in_hull2((x[i], x[j]), h) for (i, j), h in H.items()))


OPS = {"order": lambda X, b: D.stair(X, b), "algebra": lambda X, b: D.gen(X),
       "information": lambda X, b: D.joinclose(X), "geometry": geom,
       "statistics": stat}


# --------------------------------------------------- §8 N1: the sharp lemma
def n1_sharp():
    """Lemma N1*: R_B(X) cap Box(X) == <X>, over declared boxes.  (cases, fails)."""
    bad = tot = 0
    for d in (2, 3):
        for vals in (3, 4):
            B = [list(range(vals))] * d
            allc = list(itertools.product(*B))
            for k in (2, 3, 4):
                for X in itertools.combinations(allc, k):
                    X = set(X)
                    obs = [sorted({x[i] for x in X}) for i in range(d)]
                    RB = D.stair(X, B)
                    inbox = {x for x in RB if all(x[i] in obs[i] for i in range(d))}
                    tot += 1
                    bad += inbox != D.gen(X)
    return tot, bad


# ------------------------------------------- §8d: information fails every k
def info_k_construction(dmax=8):
    """The X_d construction.  Returns [(d, |J|, e_d in J, ks that pass)]."""
    out = []
    for d in range(3, dmax + 1):
        X = frozenset([tuple([0] * d)] +
                      [tuple(1 if t == i or t == d - 1 else 0 for t in range(d))
                       for i in range(d - 1)])
        J = D.joinclose(X)
        box = D.box_of(X, d)
        tgt = tuple(1 if t == d - 1 else 0 for t in range(d))
        ks = []
        for k in range(2, d):
            pr = {T: {tuple(x[i] for i in T) for x in J}
                  for T in itertools.combinations(range(d), k)}
            if all(tuple(tgt[i] for i in T) in pr[T] for T in pr):
                ks.append(k)
        out.append((d, len(J), tgt in J, ks))
    return out


# ------------------------------------------------- §6b F: order-dependence
def f_witnesses():
    """{op: (|L(X)|, |sigma^-1 L(sigma X)|)} for the paper's stated witnesses."""
    res = {}
    for L, X, sig in (
            ("order", [(0, 0), (1, 1)], [{0: 0, 1: 1}, {0: 1, 1: 0}]),
            ("algebra", [(0, 0), (1, 1)], [{0: 0, 1: 1}, {0: 1, 1: 0}]),
            ("information", [(0, 0), (1, 1)], [{0: 0, 1: 1}, {0: 1, 1: 0}]),
            ("geometry", [(0, 0), (0, 1), (1, 2)],
             [{0: 0, 1: 1}, {0: 0, 1: 2, 2: 1}])):
        X = frozenset(X); d = 2
        b = D.box_of(X, d)
        Xp = frozenset(tuple(sig[i][x[i]] for i in range(d)) for x in X)
        bp = D.box_of(Xp, d)
        inv = [{v: k for k, v in sig[i].items()} for i in range(d)]
        back = frozenset(tuple(inv[i][y[i]] for i in range(d))
                         for y in OPS[L](sorted(Xp), bp))
        res[L] = (len(OPS[L](sorted(X), b)), len(back))
    return res


# ------------------------------------------------ §6d H: the incomparabilities
H_WITNESSES = [
    ("geometry", "order", [(0, 0), (0, 1), (1, 2), (2, 2)]),
    ("order", "geometry", [(0, 1), (1, 0)]),
    ("information", "statistics", [(0, 1), (1, 0)]),
    ("statistics", "information", [(0, 0, 0), (0, 1, 1), (1, 0, 1)]),
    ("information", "geometry", [(0, 1), (1, 0)]),
    ("geometry", "information", [(0, 0), (0, 2), (1, 1)]),
]


def h_witnesses():
    """Each stated witness really shows the stated non-containment."""
    out = []
    for a, b, X in H_WITNESSES:
        X = frozenset(X); d = len(next(iter(X)))
        box = D.box_of(X, d)
        A, B = OPS[a](sorted(X), box), OPS[b](sorted(X), box)
        out.append((a, b, not (A <= B), sorted(A - B)))
    return out


# ------------------------------- §8b/§8c: the residual and the interpreter
def residual_and_logic():
    """(positions, close_at_zero, unanimous, existential, gap, ties)."""
    rnd = random.Random(53)
    pos = zero = una = exi = gap = ties = 0
    for _ in range(300):
        d = rnd.randint(2, 4)
        alpha = [rnd.randint(2, 4) for _ in range(d)]
        allc = list(itertools.product(*[range(a) for a in alpha]))
        X = frozenset(rnd.sample(allc, rnd.randint(2, min(len(allc), 7))))
        box = D.box_of(X, d)
        S = stat(X, box); G = geom(X, box)
        for x in sorted(S - X):
            Y = frozenset(X) | {x}; by = D.box_of(Y, d); pos += 1
            Cs = {L: frozenset(OPS[L](sorted(Y), by)) for L in LANGS}
            E = {L: len(Cs[L]) - len(Y) for L in LANGS}
            m = min(E.values())
            win = [L for L in LANGS if E[L] == m]
            if len(win) > 1:
                ties += 1
            if m == 0:
                zero += 1
            vs = [Cs[L] <= G for L in win]
            if all(vs):
                una += 1
            if any(vs):
                exi += 1
            if any(vs) != all(vs):
                gap += 1
    return pos, zero, una, exi, gap, ties


PINS = {
    "n1_cases": 702628, "n1_fails": 0,
    "info_k": [(3, 4), (4, 8), (5, 16), (6, 32), (7, 64), (8, 128)],
    "f": {"order": (2, 4), "algebra": (2, 4), "information": (2, 3),
          "geometry": (3, 4)},
    "positions": 155, "zero": 45, "unanimous": 147, "existential": 155,
    "gap": 8, "ties": 35,
}


def run(emit=False):
    fails = []

    def chk(label, got, want):
        if emit:
            print("  EMIT %-52s %r" % (label, got)); return
        ok = got == want
        print("  [%s] %-52s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("lawfigures.py" + (" --emit" if emit else "") + "\n")

    print(" §8 N1 -- Lemma N1*")
    t, b = n1_sharp()
    chk("cases", t, PINS["n1_cases"])
    chk("failures -- must be 0", b, PINS["n1_fails"])

    print("\n §8d -- information is k-determined for no non-vacuous k")
    ik = info_k_construction()
    chk("dimensions checked", [r[0] for r in ik], [3, 4, 5, 6, 7, 8])
    chk("(d, |J(X_d)|)", [(r[0], r[1]) for r in ik], PINS["info_k"])
    chk("e_d in J(X_d) -- must be False everywhere",
        sorted({r[2] for r in ik}), [False])
    chk("passes every k from 2 to d-1",
        all(r[3] == list(range(2, r[0])) for r in ik), True)

    print("\n §6b F -- order-dependence witnesses")
    fw = f_witnesses()
    chk("(|L(X)|, |sigma^-1 L(sigma X)|)", fw, PINS["f"])
    chk("every one differs", all(a != b for a, b in fw.values()), True)

    print("\n §6d H -- incomparability witnesses")
    hw = h_witnesses()
    for a, b, holds, ex in hw:
        chk("%s NOT subset of %s" % (a, b), holds, True)
    chk("witnesses that are non-empty", all(len(e) > 0 for _, _, _, e in hw), True)

    print("\n §8b / §8c -- the residual and the interpreter")
    pos, zero, una, exi, gap, ties = residual_and_logic()
    chk("statistical positions", pos, PINS["positions"])
    chk("close at E = 0", zero, PINS["zero"])
    chk("logic: unanimous", una, PINS["unanimous"])
    chk("logic: existential", exi, PINS["existential"])
    chk("logic: the tie-break gap", gap, PINS["gap"])
    chk("positions with tied languages", ties, PINS["ties"])
    chk("cannot close at E = 0", pos - zero, 110)
    chk("logic never refutes outright", exi == pos, True)

    if emit:
        return 0
    print()
    if fails:
        for lab, g, w in fails:
            print("  DRIFT %s: got %r want %r" % (lab, g, w))
        print("\n%d FIGURE(S) HAVE DRIFTED FROM THE PAPER" % len(fails))
        return 1
    print("every pinned figure in THE-HIERARCHY-LAW.md still holds")
    return 0


if __name__ == "__main__":
    sys.exit(run(emit="--emit" in sys.argv))
