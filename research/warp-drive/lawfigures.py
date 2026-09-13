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
def residual_and_logic(seed=53):
    """(positions, close_at_zero, unanimous, existential, gap, ties).

    Seeded, because the paper's §8c reports one seed's numbers AND the
    counterexample that withdraws their universal reading: seed 53 gives
    155/155 existential (no outright refusal), seed 77 gives 21 refusals in
    177.  Both are pinned -- a withdrawal has to be reproducible too."""
    rnd = random.Random(seed)
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



# ------------------------------------------- §6b F: the relabelling sweep
def f_sweep(n=400, seed=7):
    """Clause F. Generator: d in 2..3, alphabets 3..4, |X| in 3..8, seed 7.
    Returns {op: invariant_count} and the order/algebra agreement count."""
    rnd = random.Random(seed)
    inv = {L: 0 for L in LANGS}
    tot = 0
    agree = 0
    for _ in range(n):
        d = rnd.randint(2, 3)
        alpha = [rnd.randint(3, 4) for _ in range(d)]
        allc = list(itertools.product(*[range(a) for a in alpha]))
        X = frozenset(rnd.sample(allc, rnd.randint(3, min(len(allc), 8))))
        box = D.box_of(X, d)
        perms = []
        for i in range(d):
            v = box[i]; sh = v[:]; rnd.shuffle(sh); perms.append(dict(zip(v, sh)))
        ip = [{v: k for k, v in p.items()} for p in perms]
        Xp = frozenset(tuple(perms[i][x[i]] for i in range(d)) for x in X)
        bp = D.box_of(Xp, d)
        tot += 1
        res = {}
        for L in LANGS:
            back = frozenset(tuple(ip[i][y[i]] for i in range(d))
                             for y in OPS[L](sorted(Xp), bp))
            res[L] = back == OPS[L](sorted(X), box)
            inv[L] += res[L]
        agree += res["order"] == res["algebra"]
    return inv, agree, tot


# ------------------------------------- §6c G: the hypothetical-language sweep
def g_sweep(n=500, seed=11):
    """Clause G. Generator: d 2..4, alphabets 2..4, |X| 2..10, seed 11."""
    rnd = random.Random(seed)
    r = {"st_in_geom": 0, "geom_preserved": 0, "st_union": 0, "alg_union": 0, "n": 0}
    for _ in range(n):
        d = rnd.randint(2, 4)
        alpha = [rnd.randint(2, 4) for _ in range(d)]
        allc = list(itertools.product(*[range(a) for a in alpha]))
        X = frozenset(rnd.sample(allc, rnd.randint(2, min(len(allc), 10))))
        box = D.box_of(X, d)
        S = stat(X, box); G = geom(X, box)
        r["n"] += 1
        r["st_in_geom"] += S <= G
        r["geom_preserved"] += geom(S, D.box_of(S, d)) == G
        seen = {T: set() for T in itertools.combinations(range(d), 2)}
        for y in X:
            for T in seen:
                seen[T].add(tuple(y[i] for i in T))
        S2 = frozenset(x for x in itertools.product(*box)
                       if all(tuple(x[i] for i in T) in seen[T] for T in seen))
        r["st_union"] += S2 == S
        A = D.gen(X)
        r["alg_union"] += frozenset().union(*[D.gen({y}) for y in X]) == A
    return r


def g5_registers(n=500, seed=3):
    """G.5. N1 is membership-register (invariant), N2 is order-register."""
    rnd = random.Random(seed)
    n1 = n2 = tot = 0
    for _ in range(n):
        d = rnd.randint(2, 3)
        alpha = [rnd.randint(2, 4) for _ in range(d)]
        allc = list(itertools.product(*[range(a) for a in alpha]))
        X = frozenset(rnd.sample(allc, rnd.randint(2, min(len(allc), 8))))
        box = D.box_of(X, d)
        perms = []
        for i in range(d):
            v = box[i]; sh = v[:]; rnd.shuffle(sh); perms.append(dict(zip(v, sh)))
        Xp = frozenset(tuple(perms[i][x[i]] for i in range(d)) for x in X)
        bp = D.box_of(Xp, d)
        holds = lambda Y, b: all(set(b[i]) == {y[i] for y in Y} for i in range(d))
        tot += 1
        n1 += holds(X, box) == holds(Xp, bp)
        ok = True
        for x, y in itertools.combinations(sorted(X), 2):
            if all(x[i] <= y[i] for i in range(d)) != \
               all(perms[i][x[i]] <= perms[i][y[i]] for i in range(d)):
                ok = False; break
        n2 += ok
    return n1, n2, tot


# ------------------------------------------- §6d H: the containment census
def h_sweep(n=600, seed=19):
    """Clause H. Generator: d 2..4, alphabets 2..4, |X| 2..10, seed 19."""
    rnd = random.Random(seed)
    cnt = {(a, b): [0, 0] for a in LANGS for b in LANGS if a != b}
    for _ in range(n):
        d = rnd.randint(2, 4)
        alpha = [rnd.randint(2, 4) for _ in range(d)]
        allc = list(itertools.product(*[range(a) for a in alpha]))
        X = frozenset(rnd.sample(allc, rnd.randint(2, min(len(allc), 10))))
        box = D.box_of(X, d)
        v = {L: OPS[L](sorted(X), box) for L in LANGS}
        for a in LANGS:
            for b in LANGS:
                if a == b:
                    continue
                cnt[(a, b)][1] += 1
                cnt[(a, b)][0] += v[a] <= v[b]
    always = sorted(k for k, (o, t) in cnt.items() if o == t)
    return always, cnt


PINS = {
    "n1_cases": 702628, "n1_fails": 0,
    "info_k": [(3, 4), (4, 8), (5, 16), (6, 32), (7, 64), (8, 128)],
    "f": {"order": (2, 4), "algebra": (2, 4), "information": (2, 3),
          "geometry": (3, 4)},
    "positions": 155, "zero": 45, "unanimous": 147, "existential": 155,
    "gap": 8, "ties": 35, "seed77": (177, 21),
    "f_inv": {"order": 58, "algebra": 58, "geometry": 102, "information": 59,
              "statistics": 400},
    "f_agree": 400,
    "g": {"st_in_geom": 500, "geom_preserved": 500, "st_union": 500,
          "alg_union": 98, "n": 500},
    "g5": (500, 84, 500),
    "h_always": [("algebra", "order"), ("information", "algebra"),
                 ("information", "order"), ("order", "algebra"),
                 ("statistics", "algebra"), ("statistics", "geometry"),
                 ("statistics", "order")],
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

    print("\n §6b F -- the relabelling sweep (seed 7, d 2-3, alphabets 3-4)")
    inv, agree, ftot = f_sweep()
    chk("invariant counts of %d" % ftot, inv, PINS["f_inv"])
    chk("statistics is ORDER-FREE", inv["statistics"] == ftot, True)
    chk("order and algebra agree on which instances break", agree, PINS["f_agree"])

    print("\n §6c G -- the hypothetical language (seed 11) and the registers (seed 3)")
    g = g_sweep()
    chk("statistics subset geometry, always", (g["st_in_geom"], g["n"]), (500, 500))
    chk("geometry(statistics(X)) == geometry(X)", (g["geom_preserved"], g["n"]), (500, 500))
    chk("statistics IS a union of single-cell facts", (g["st_union"], g["n"]), (500, 500))
    chk("control: algebra is NOT", g["alg_union"], PINS["g"]["alg_union"])
    n1i, n2i, gt = g5_registers()
    chk("N1 invariant -- membership register", (n1i, gt), (500, 500))
    chk("N2 invariant -- order register", n2i, PINS["g5"][1])

    print("\n §6d H -- the lawful skeleton (seed 19)")
    always, cnt = h_sweep()
    chk("containments holding in every world", always, PINS["h_always"])
    chk("and there are exactly seven", len(always), 7)
    chk("geometry vs order is NOT always", ("geometry", "order") in always, False)

    print("\n §8b / §8c -- the residual and the interpreter")
    pos, zero, una, exi, gap, ties = residual_and_logic()
    chk("statistical positions", pos, PINS["positions"])
    chk("close at E = 0", zero, PINS["zero"])
    chk("logic: unanimous", una, PINS["unanimous"])
    chk("logic: existential", exi, PINS["existential"])
    chk("logic: the tie-break gap", gap, PINS["gap"])
    chk("positions with tied languages", ties, PINS["ties"])
    chk("cannot close at E = 0", pos - zero, 110)
    chk("logic never refutes outright AT SEED 53", exi == pos, True)
    p77, _, _, e77, _, _ = residual_and_logic(seed=77)
    chk("...and DOES at seed 77 -- the withdrawal", (p77, p77 - e77),
        PINS["seed77"])

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
