#!/usr/bin/env python3
"""check.py -- the machine checks behind "The parent-term wall and the Janet collapse".

Every number the paper prints is produced here, and every decidable claim is decided here.
Statuses printed, one line per obligation:

    EXHAUSTIVE       a decision procedure visited every case of a named finite family
    MACHINE-CHECKED  Z3 returned unsat on the negation over every subset of a named box,
                     after the two guards (non-vacuity, encoding fidelity) passed
    SAMPLED          a seeded pseudorandom sweep, size and seed stated (guards only)
    GUARD            a soundness guard; a failed guard suppresses the obligations it covers

    python3 check.py             # every obligation, exit 1 on any failure
    python3 check.py --selftest  # the same, plus negative controls that must be refuted

Instruments are imported BY PATH and never copied: the staircase operator of the atomic index
(tools/cypher.py), the ground configurations (method/members/LW1-ground.py), the core/Pauli/
collapse conventions (tools/populate.py), the channel-table reader (method/proofs/compendia4.py)
and the Z3 harness (research/warp-drive/prover.py).  Reference implementations for the guards
are written fresh here; the object under test is the seated one.  Exact arithmetic is Fraction.
"""
import collections
import csv
import importlib.util
import itertools
import math
import os
import random
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))


def load(name, rel):
    path = os.path.join(ROOT, rel)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


PROVER = load("prover", "research/warp-drive/prover.py")
CYPHER = load("cypher", "tools/cypher.py")
LW1 = load("lw1_ground", "method/members/LW1-ground.py")
POP = load("populate", "tools/populate.py")
C4 = load("compendia4", "method/proofs/compendia4.py")
import z3  # noqa: E402

SPECTRA = os.path.join(ROOT, "method/members/The_Method_1_6___Spectra_Compendium-2.md")
COORDS = os.path.join(ROOT, "drive/The Method Materials/COORDINATES-2_13.csv")

RESULTS = []
FAILS = []
NUMBERS = {}          # every figure the paper prints, by name


def rec(status, name, ok, detail=""):
    RESULTS.append((status, name, ok, detail))
    mark = "ok " if ok else "XX "
    print("  [%s] %-16s %-70s %s" % (mark, status, name, detail))
    if not ok:
        FAILS.append(name)
    return ok


def num(key, value):
    NUMBERS[key] = value
    return value


# =============================================================================================
# A. The reference staircase (fresh) and the seated operator
# =============================================================================================

def R_ref(X, d):
    """An independent implementation of the staircase closure over the observed box."""
    A = [sorted({x[i] for x in X}) for i in range(d)]
    out = set()
    for x in itertools.product(*A):
        good = True
        for i in range(d):
            for j in range(d):
                if i == j:
                    continue
                cand = [y[i] for y in X if y[j] <= x[j]]
                if not cand or x[i] > max(cand):
                    good = False
                    break
            if not good:
                break
        if good:
            out.add(x)
    return out


def R_seated(cells, coords):
    """The staircase as the seated instrument computes it (cypher.op_order), decoded."""
    ix = CYPHER.Index("x", coords, cells)
    adm, _ = CYPHER.op_order(ix, {})
    return {tuple(ix.decode[i][v] for i, v in enumerate(c)) for c in adm}


def E_of(cells, coords):
    S = R_seated(cells, coords)
    return S, len(S) - len(set(cells))


# =============================================================================================
# B. The periodic table as an index
# =============================================================================================

def periodic_cells(helium_group=18):
    occ = [(1, 1), (1, helium_group)]
    for p in (2, 3):
        occ += [(p, g) for g in (1, 2, 13, 14, 15, 16, 17, 18)]
    for p in (4, 5, 6, 7):
        occ += [(p, g) for g in range(1, 19)]
    return occ


def thirty_two_column_cells():
    occ = [(1, 1), (1, 32)]
    for p in (2, 3):
        occ += [(p, g) for g in (1, 2, 27, 28, 29, 30, 31, 32)]
    for p in (4, 5):
        occ += [(p, g) for g in list(range(1, 3)) + list(range(17, 33))]
    for p in (6, 7):
        occ += [(p, g) for g in range(1, 33)]
    return occ


def slot(p, g):
    """The subshell a (period, group) cell of the eighteen-column layout would hold, with the
    f-block set aside: groups 1-2 are the s slot (p, 0), 3-12 the d slot (p, 2), 13-18 the p slot
    (p, 1).  A slot is FORBIDDEN when l > n - 1 (no such orbital), DEFERRED otherwise."""
    l = 0 if g <= 2 else (2 if g <= 12 else 1)
    return (p, l)


def section_periodic():
    print("\nB. THE PERIODIC TABLE AS AN INDEX")
    seated = CYPHER._periodic()
    X = periodic_cells()
    rec("EXHAUSTIVE", "the seated fixture is the ninety-cell (period, group) index",
        sorted(seated.cells) == sorted((CYPHER._periodic().code[0][p], seated.code[1][g]) for p, g in X)
        and len(seated.cells) == 90, "cells=%d" % len(seated.cells))
    S, E = E_of(X, ["period", "group"])
    num("periodic_cells", len(set(X)))
    num("periodic_box", 7 * 18)
    num("periodic_E", E)
    rec("EXHAUSTIVE", "(period, group): 90 cells, box 126, E = 36 under the seated staircase",
        (len(set(X)), len(S), E) == (90, 126, 36), "|R|=%d E=%d" % (len(S), E))
    rec("EXHAUSTIVE", "fresh reference staircase agrees with the seated operator on the table",
        R_ref(set(X), 2) == S)
    # the cypher selftest fixture records E(order) = 36 on this object
    adm, _ = CYPHER.op_order(seated, {})
    rec("EXHAUSTIVE", "the seated fixture itself gives E = 36", len(adm) - len(seated.cells) == 36)
    admitted = sorted(S - set(X))
    byp = collections.defaultdict(list)
    for p, g in admitted:
        byp[p].append(g)
    num("periodic_admitted_by_period", {p: (min(v), max(v), len(v)) for p, v in byp.items()})
    rec("EXHAUSTIVE", "the 36 are period 1 groups 2-17, periods 2 and 3 groups 3-12",
        byp == {1: list(range(2, 18)), 2: list(range(3, 13)), 3: list(range(3, 13))},
        "%s" % {p: (min(v), max(v), len(v)) for p, v in byp.items()})
    # the two extreme corners, which is the whole of the corner lemma's hypothesis
    corners = [(1, 18), (7, 1)]
    num("periodic_corners", corners)
    rec("EXHAUSTIVE", "the table holds both extreme corners (period 1, group 18) and (period 7, group 1)",
        all(c in set(X) for c in corners) and min(p for p, g in X) == 1 and max(p for p, g in X) == 7
        and min(g for p, g in X) == 1 and max(g for p, g in X) == 18)
    # the two boundary functions
    phi_g = {p: max(g for (pp, g) in X if pp <= p) for p in range(1, 8)}
    phi_p = {g: max(pp for (pp, gg) in X if gg <= g) for g in range(1, 19)}
    rec("EXHAUSTIVE", "phi(group | period <= p) = 18 for every p, phi(period | group <= g) = 7 for every g",
        all(v == 18 for v in phi_g.values()) and all(v == 7 for v in phi_p.values()))
    # the physical decomposition of the 36
    forb = collections.Counter()
    defer = collections.Counter()
    for p, g in admitted:
        n, l = slot(p, g)
        name = "%d%s" % (n, "spdf"[l])
        (forb if l > n - 1 else defer)[name] += 1
    num("periodic_forbidden", dict(forb))
    num("periodic_deferred", dict(defer))
    rec("EXHAUSTIVE", "36 = 25 forbidden (1d 10, 1p 5, 2d 10) + 11 deferred (3d 10, 1s 1)",
        forb == {"1d": 10, "1p": 5, "2d": 10} and defer == {"3d": 10, "1s": 1},
        "forbidden=%s deferred=%s" % (dict(forb), dict(defer)))
    # helium at group 2
    X2 = periodic_cells(helium_group=2)
    S2, E2 = E_of(X2, ["period", "group"])
    num("periodic_E_he2", E2)
    rec("EXHAUSTIVE", "helium drawn at group 2: 90 cells, E = 20 (periods 2-3, groups 3-12)",
        E2 == 20 and sorted(S2 - set(X2)) == [(p, g) for p in (2, 3) for g in range(3, 13)],
        "E=%d" % E2)
    num("periodic_he_cost", E - E2)
    # thirty-two columns
    X32 = thirty_two_column_cells()
    S32, E32 = E_of(X32, ["period", "group"])
    num("periodic32_cells", len(set(X32)))
    num("periodic32_box", 7 * 32)
    num("periodic32_E", E32)
    rec("EXHAUSTIVE", "32-column layout: 118 cells, box 224, E = 106",
        (len(set(X32)), len(S32), E32) == (118, 224, 106), "cells=%d |R|=%d E=%d" % (len(set(X32)), len(S32), E32))
    # the plate's census
    rec("EXHAUSTIVE", "plate census: 90 held + 36 admitted = 126 = 7 x 18", 90 + 36 == 126 == 7 * 18)
    # the seated three-coordinate fixture, for the record of what E measures
    ix3 = CYPHER._periodic(True)
    adm3, _ = CYPHER.op_order(ix3, {})
    num("periodic3_E", len(adm3) - len(ix3.cells))
    rec("EXHAUSTIVE", "with a block coordinate adjoined (period, group, block) E rises to 100",
        len(adm3) - len(ix3.cells) == 100, "E=%d" % (len(adm3) - len(ix3.cells)))


# =============================================================================================
# C. Janet's left-step index
# =============================================================================================

JANET_ROWS_118 = [2, 2, 8, 8, 18, 18, 32, 30]     # elements per n+l row, Z <= 118
JANET_ROWS_120 = [2, 2, 8, 8, 18, 18, 32, 32]


def janet_cells(rows):
    cells, z = [], 1
    for r, k in enumerate(rows, 1):
        for _ in range(k):
            cells.append((r, z))
            z += 1
    return cells


def is_chain(X):
    X = list(X)
    for a, b in itertools.combinations(X, 2):
        if not (all(u <= v for u, v in zip(a, b)) or all(u >= v for u, v in zip(a, b))):
            return False
    return True


def section_janet():
    print("\nC. JANET'S LEFT-STEP INDEX")
    X = janet_cells(JANET_ROWS_118)
    num("janet_rows", JANET_ROWS_118)
    S, E = E_of(X, ["n+l", "Z"])
    num("janet_cells", len(X))
    num("janet_box", 8 * 118)
    num("janet_E", E)
    rec("EXHAUSTIVE", "(n+l, Z): 118 cells, box 944, E = 0 under the seated staircase",
        (len(X), 8 * 118, E) == (118, 944, 0) and S == set(X), "|R|=%d E=%d" % (len(S), E))
    rec("EXHAUSTIVE", "fresh reference staircase agrees", R_ref(set(X), 2) == S)
    rec("EXHAUSTIVE", "the 118 cells form a chain in the product order (C(118,2) = 6,903 pairs compared)",
        is_chain(X), "pairs=%d" % (118 * 117 // 2))
    starts = [z for (r, z) in X if r == 1 or (r - 1, z - 1) in set(X)]
    starts = sorted({min(z for (rr, z) in X if rr == r) for r in range(1, 9)})
    num("janet_starts", starts)
    rec("EXHAUSTIVE", "the rows open at Z = 1, 3, 5, 13, 21, 39, 57, 89",
        starts == [1, 3, 5, 13, 21, 39, 57, 89], "%s" % starts)
    # the row coordinate read from the observed ground configurations
    bad = []
    for Z in range(1, 109):
        top = max(n + l for n, l, o in LW1.expand(Z) if o > 0)
        row = [r for (r, z) in X if z == Z][0]
        if top != row:
            bad.append((Z, top, row))
    num("janet_rows_from_ground", 108 - len(bad))
    rec("EXHAUSTIVE", "the largest n+l occupied in the observed ground configuration (Z = 1..108) equals the row on all 108",
        not bad, "exceptions=%s" % bad[:5])
    diff_bad = []
    for Z in range(1, 109):
        cell = POP.janet_cell(Z)
        row = [r for (r, z) in X if z == Z][0]
        if cell is None or cell[0] != row:
            diff_bad.append(Z)
    num("janet_diff_exceptions", diff_bad)
    rec("EXHAUSTIVE", "read instead from the differentiating electron alone it fails at six elements (25, 30, 43, 47, 48, 80), "
        "each the successor of an s-to-d rearrangement", diff_bad == [25, 30, 43, 47, 48, 80], "%s" % diff_bad)
    # appending a cell that keeps the chain keeps the closure: E = 0 is a property of the SHAPE
    Xa = X + [(3, 13)]
    Sa, Ea = E_of(Xa, ["n+l", "Z"])
    num("janet_append_E", Ea)
    rec("EXHAUSTIVE", "appending (3, 13) leaves a chain of 119 cells and E stays 0 -- closure follows the shape, not the count",
        is_chain(Xa) and Ea == 0, "E=%d" % Ea)
    Xm = [c for c in X if c != (5, 30)] + [(2, 30)]
    Sm, Em = E_of(Xm, ["n+l", "Z"])
    num("janet_move_E", Em)
    rec("EXHAUSTIVE", "moving one element to the wrong row breaks the chain and E rises to 54",
        (not is_chain(Xm)) and Em == 54, "E=%d" % Em)
    X120 = janet_cells(JANET_ROWS_120)
    S120, E120 = E_of(X120, ["n+l", "Z"])
    num("janet120_E", E120)
    rec("EXHAUSTIVE", "with 119 and 120 admitted: 120 cells, box 960, E = 0",
        (len(X120), E120) == (120, 0) and len(S120) == 120)
    # the recovered bounds: Z <= b(r) and r <= rho(Z)
    b = {r: max(z for (rr, z) in X if rr == r) for r in range(1, 9)}
    rho = {z: max(rr for (rr, zz) in X if zz <= z) for z in range(1, 119)}
    num("janet_row_ends", [b[r] for r in range(1, 9)])
    rec("EXHAUSTIVE", "the two bounds the staircase recovers are the row ends (2, 4, 12, 20, 38, 56, 88, 118) "
        "and the row of Z; together they admit exactly the 118",
        [b[r] for r in range(1, 9)] == [2, 4, 12, 20, 38, 56, 88, 118]
        and {(r, z) for r in range(1, 9) for z in range(1, 119) if z <= b[r] and r <= rho[z]} == set(X))
    # the seated subshell fixture (n+l, l)
    J = CYPHER._janet()
    adm, _ = CYPHER.op_order(J, {})
    dec = {tuple(J.decode[i][v] for i, v in enumerate(c)) for c in J.cells}
    num("subshell_cells", len(J.cells))
    num("subshell_box", J.box)
    num("subshell_E", len(adm) - len(J.cells))
    rec("EXHAUSTIVE", "the subshell index (n+l, l), n <= 7, l <= 3: 22 cells, box 40, E = 0",
        (len(J.cells), J.box, len(adm) - len(J.cells)) == (22, 40, 0),
        "cells=%d box=%d E=%d" % (len(J.cells), J.box, len(adm) - len(J.cells)))
    f = {s: max(l for (ss, l) in dec if ss <= s) for s in range(1, 11)}
    g = {l: max(ss for (ss, ll) in dec if ll <= l) for l in range(0, 4)}
    rec("EXHAUSTIVE", "its recovered bounds are l <= min(floor((s-1)/2), 3) and s <= 7 + l",
        all(f[s] == min((s - 1) // 2, 3) for s in f) and all(g[l] == 7 + l for l in g))
    rec("EXHAUSTIVE", "and it is not a chain: (4,1) and (5,0) are incomparable", not is_chain(dec))


# =============================================================================================
# D. Machine checks (Z3): chains close, bi-monotone bounds close, corners fill the box
# =============================================================================================

def chain_formula(X, cells):
    cl = []
    for a in cells:
        for b in cells:
            if a < b:
                comp = all(u <= v for u, v in zip(a, b)) or all(u >= v for u, v in zip(a, b))
                if not comp:
                    cl.append(z3.Not(z3.And(X[a], X[b])))
    return z3.And(cl) if cl else z3.BoolVal(True)


def closed_under_R(X, cells, d):
    return z3.And([z3.Implies(PROVER.in_R(X, c, cells, d), X[c]) for c in cells])


def obl_chain(X, S, cells, d, shape):
    """Theorem 1: a chain that observes every value is fixed by the staircase."""
    hyp = z3.And(PROVER.observed(X, cells, shape), chain_formula(X, cells))
    return z3.Implies(hyp, closed_under_R(X, cells, d))


def obl_bimonotone(X, S, cells, d, shape):
    """Theorem 2 (d = 2): X = {x : x1 <= F(x2), x2 <= G(x1)} with F, G isotone is fixed by R.
    F and G are unknown integer tables, constrained isotone; X is DEFINED from them."""
    n1, n2 = shape
    F = [z3.Int("F_%d" % b) for b in range(n2)]
    G = [z3.Int("G_%d" % a) for a in range(n1)]
    rng = z3.And([z3.And(F[b] >= 0, F[b] <= n1 - 1) for b in range(n2)]
                 + [z3.And(G[a] >= 0, G[a] <= n2 - 1) for a in range(n1)])
    iso = z3.And([F[b] <= F[b + 1] for b in range(n2 - 1)] + [G[a] <= G[a + 1] for a in range(n1 - 1)])
    defn = z3.And([X[(a, b)] == z3.And(a <= F[b], b <= G[a]) for (a, b) in cells])
    hyp = z3.And(rng, iso, defn, PROVER.observed(X, cells, shape))
    return z3.Implies(hyp, closed_under_R(X, cells, d))


def obl_corner(X, S, cells, d, shape):
    """Lemma (corners): at d = 2, if X observes every value and holds the cells (a_min, b_max)
    and (a_max, b_min), the staircase admits the whole box."""
    n1, n2 = shape
    hyp = z3.And(PROVER.observed(X, cells, shape), X[(0, n2 - 1)], X[(n1 - 1, 0)])
    return z3.Implies(hyp, z3.And([PROVER.in_R(X, c, cells, d) for c in cells]))


def guard_encoding(trials=300, seed=7):
    """in_R, evaluated concretely, against the SEATED staircase; and a negative control."""
    rnd = random.Random(seed)
    shapes = [(3, 3), (4, 4), (5, 5), (3, 3, 3), (2, 2, 2, 2)]
    tot = bad = 0
    tot_neg = bad_neg = 0
    for _ in range(trials):
        shape = rnd.choice(shapes)
        d = len(shape)
        cells = PROVER.cells_of(shape)
        X = frozenset(rnd.sample(cells, rnd.randint(2, min(len(cells), 8))))
        seated = R_seated(list(X), ["c%d" % i for i in range(d)])
        A = [sorted({x[i] for x in X}) for i in range(d)]
        for x in itertools.product(*A):
            enc = all(any(y[j] <= x[j] and y[i] >= x[i] for y in X)
                      for i in range(d) for j in range(d) if i != j)
            wrong = all(any(y[j] < x[j] and y[i] >= x[i] for y in X)
                        for i in range(d) for j in range(d) if i != j)
            tot += 1
            bad += enc != (x in seated)
            tot_neg += 1
            bad_neg += wrong != (x in seated)
    return tot, bad, tot_neg, bad_neg


def section_z3(negative=False):
    print("\nD. MACHINE CHECKS (Z3 %s)" % z3.get_version_string())
    tot, bad, tn, bn = guard_encoding()
    g1 = rec("GUARD", "encoding fidelity: witness form of R against the seated op_order, 300 draws seed 7",
             bad == 0, "cells compared=%d disagreements=%d" % (tot, bad))
    g2 = rec("GUARD", "negative control: a strict-inequality staircase DISAGREES with the seated one",
             bn > 0, "disagreements=%d of %d" % (bn, tn))
    # non-vacuity: each hypothesis satisfiable with X strictly inside the box and at least two cells
    def strict(X, S, cells, d, shape):
        return z3.And(z3.Or([z3.Not(X[c]) for c in cells]), z3.AtLeast(*[X[c] for c in cells], 2))
    nv = []
    for shape in ((3, 3), (3, 3, 3)):
        nv.append(PROVER.non_vacuous(shape, lambda X, S, c, d, sh: z3.And(PROVER.observed(X, c, sh), chain_formula(X, c)), strict))
    nv.append(PROVER.non_vacuous((4, 4), lambda X, S, c, d, sh: z3.And(PROVER.observed(X, c, sh), X[(0, 3)], X[(3, 0)]), strict))
    # bi-monotone hypothesis: build it the same way the obligation does
    def bihyp(X, S, cells, d, shape):
        n1, n2 = shape
        F = [z3.Int("F_%d" % b) for b in range(n2)]
        G = [z3.Int("G_%d" % a) for a in range(n1)]
        return z3.And([z3.And(F[b] >= 0, F[b] <= n1 - 1) for b in range(n2)]
                      + [z3.And(G[a] >= 0, G[a] <= n2 - 1) for a in range(n1)]
                      + [F[b] <= F[b + 1] for b in range(n2 - 1)] + [G[a] <= G[a + 1] for a in range(n1 - 1)]
                      + [X[(a, b)] == z3.And(a <= F[b], b <= G[a]) for (a, b) in cells]
                      + [PROVER.observed(X, cells, shape)])
    nv.append(PROVER.non_vacuous((4, 4), bihyp, strict))
    g3 = rec("GUARD", "non-vacuity: chain, corner and bi-monotone hypotheses each satisfiable with X strictly inside the box",
             all(nv), "%s" % nv)
    if not (g1 and g2 and g3):
        rec("MACHINE-CHECKED", "obligations withheld: a guard failed", False)
        return
    boxes_chain = [(3, 3), (4, 4), (5, 5), (6, 6), (3, 3, 3), (2, 2, 2, 2)]
    ok = []
    for sh in boxes_chain:
        r = PROVER.prove("chain => R-closed, %s" % "x".join(map(str, sh)), sh, obl_chain, quiet=True)
        ok.append(r)
        rec("MACHINE-CHECKED", "Theorem 1 over every subset of the %s box (2^%d subsets)"
            % ("x".join(map(str, sh)), math.prod(sh)), r)
    num("z3_chain_boxes", ["x".join(map(str, s)) for s in boxes_chain])
    boxes_bi = [(3, 3), (4, 4), (5, 5)]
    for sh in boxes_bi:
        r = PROVER.prove("bi-monotone => R-closed, %s" % "x".join(map(str, sh)), sh, obl_bimonotone, quiet=True)
        ok.append(r)
        rec("MACHINE-CHECKED", "Theorem 2 (<=) over every isotone pair (F, G) on the %s box" % "x".join(map(str, sh)), r)
    num("z3_bi_boxes", ["x".join(map(str, s)) for s in boxes_bi])
    boxes_c = [(3, 3), (4, 4), (5, 5), (7, 18)]
    for sh in boxes_c:
        r = PROVER.prove("corners => full box, %s" % "x".join(map(str, sh)), sh, obl_corner, quiet=True)
        ok.append(r)
        rec("MACHINE-CHECKED", "Lemma 3 (corners) over every subset of the %s box (2^%d subsets)"
            % ("x".join(map(str, sh)), math.prod(sh)), r)
    num("z3_corner_boxes", ["x".join(map(str, s)) for s in boxes_c])
    num("z3_obligations", len(ok))
    num("z3_discharged", sum(ok))
    if negative:
        s = z3.Solver()
        cells = PROVER.cells_of((3, 3))
        X = PROVER.subset_vars(cells, "x")
        s.add(z3.Not(z3.Implies(PROVER.observed(X, cells, (3, 3)), closed_under_R(X, cells, 2))))
        rec("NEGATIVE", "control: 'every observing subset of the 3x3 box is R-closed' must be REFUTED (sat)",
            s.check() == z3.sat, str(s.check()))


# =============================================================================================
# E. LS terms of l^k, exhaustively, and the parent counts a core carries
# =============================================================================================

def ls_terms(l, k):
    """The LS terms of the configuration l^k, by exhaustive enumeration of every Slater determinant
    (every k-subset of the 2(2l+1) spin-orbitals) and peeling of the (M_L, M_S) table."""
    orbs = [(ml, ms) for ml in range(-l, l + 1) for ms in (-1, 1)]
    tab = collections.Counter()
    for det in itertools.combinations(orbs, k):
        tab[(sum(m for m, _ in det), sum(s for _, s in det))] += 1
    terms = collections.Counter()
    while any(v > 0 for v in tab.values()):
        ML, MS = max((key for key, v in tab.items() if v > 0), key=lambda t: (t[1], t[0]))
        terms[(ML, MS)] += 1
        for ml in range(-ML, ML + 1):
            for ms in range(-MS, MS + 1, 2):
                tab[(ml, ms)] -= 1
                assert tab[(ml, ms)] >= 0
    return terms


TERMS = {}


def section_terms():
    print("\nE. LS TERMS OF l^k (EXHAUSTIVE OVER EVERY DETERMINANT)")
    for l in range(4):
        for k in range(0, 4 * l + 3):
            TERMS[(l, k)] = sum(ls_terms(l, k).values())
    dets = sum(math.comb(4 * l + 2, k) for l in range(4) for k in range(4 * l + 3))
    num("term_counts", {l: [TERMS[(l, k)] for k in range(4 * l + 3)] for l in range(4)})
    num("determinants_enumerated", dets)
    rec("EXHAUSTIVE", "p^k terms 1,1,3,3,3,1,1; d^k 1,1,5,8,16,16,16,8,5,1,1; f^6 = f^7 = f^8 = 119 (%d determinants)" % dets,
        [TERMS[(1, k)] for k in range(7)] == [1, 1, 3, 3, 3, 1, 1]
        and [TERMS[(2, k)] for k in range(11)] == [1, 1, 5, 8, 16, 16, 16, 8, 5, 1, 1]
        and TERMS[(3, 6)] == TERMS[(3, 7)] == TERMS[(3, 8)] == 119)
    t = ls_terms(2, 4)
    num("d4_terms", 16)
    rec("EXHAUSTIVE", "d^4 carries 16 LS terms, 5D the highest multiplicity, 1I the highest L",
        sum(t.values()) == 16 and t[(2, 4)] == 1 and t[(6, 0)] == 1)
    rec("EXHAUSTIVE", "a single electron or a single hole in one subshell is one LS term",
        all(TERMS[(l, 1)] == 1 and TERMS[(l, 4 * l + 1)] == 1 for l in range(4)))


def core_terms(cfg):
    n = 1
    for _n, l, o in cfg:
        if 0 < o < 2 * (2 * l + 1):
            n *= TERMS[(l, o)]
    return n


# =============================================================================================
# F. The channel table: an exact parser, and the parent census
# =============================================================================================

DOTTED = re.compile(r"^\S*\.\(.*?\)\.")
SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹°", "0123456789*")
ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
         "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17}
SYMBOL = {v[0]: k for k, v in LW1.GROUND.items()}

# Ground configurations of three parent ions whose electron count, taken as a neutral atom,
# would give another configuration (NIST ASD ground levels: Ti IV 3d 2D3/2, Zn III 3d10 1S0,
# Hg III 5d10 1S0).  Every other core is the observed configuration at its electron count.
CORE_OVERRIDE = {"Ti III": "[Ar]3d", "Zn II": "[Ar]3d10", "Hg II": "[Xe]4f14 5d10"}


def channel_rows():
    lines = open(SPECTRA, encoding="utf-8").read().split("\n")
    a = next(i for i, l in enumerate(lines) if l.startswith("# II · THE CHANNELS"))
    b = next(i for i, l in enumerate(lines) if l.startswith("# III"))
    rows = []
    for i in range(a, b):
        l = lines[i]
        if not l.startswith("|"):
            continue
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) != 11 or set("".join(c)) <= set("-: "):
            continue
        rows.append((i + 1, c))
    return rows[0], rows[1:]


def species_of(c):
    return c[0].replace("*", "").strip()


JJPAIR = re.compile(r"\(\s*\d+/\d+\s*,\s*\d+/\d+\s*\)")


def label_form(s):
    if DOTTED.match(s):
        return "dotted"
    if s.startswith("("):
        return "bare-term"
    if "(" in s:
        return "other-paren"
    return "none"


def label_convention(s):
    """The five ways a parent is or is not written in a series label:
    dotted-config   `5p5.(2P*<3/2>).nd 2[3/2]* J=2`   a dotted core configuration, parent in ()
    run-on-config   `2s22p5(2P*3/2)nd 2[3/2]* J=1`    the same with no dots
    bare-term       `(3P)ns 4P J=5/2`                 the parent term alone, no configuration
    jj-pair         `nd (3/2,5/2)* J=3`               (j of the core, j of the electron)
    none            `nd 2D J=3/2`                     no parent written at all"""
    f = label_form(s)
    if f in ("dotted", "bare-term", "none"):
        return {"dotted": "dotted-config", "bare-term": "bare-term", "none": "none"}[f]
    return "jj-pair" if JJPAIR.search(s) else "run-on-config"


def normalise(label):
    return re.sub(r"\s+", " ", C4.PREFIX.sub("", label).translate(SUP)).strip()


def parent_key(label):
    """The parent as the label carries it: the core level (term, J) from a parenthesised group,
    or the core j from a jj pair.  Returns None when the label names no parent."""
    s = label.translate(SUP)
    m = re.search(r"\(([^)]*)\)", s)
    if not m:
        return None
    grp = m.group(1)
    if re.match(r"^\d/\d,", grp):                    # jj pair (j_core, j)
        return ("j", grp.split(",")[0])
    term = re.match(r"^\d[A-Z]\*?", grp)
    j = re.search(r"<(\d/\d)>|(\d/\d)$|_(\d)$", grp)
    jj = None
    if j:
        jj = j.group(1) or j.group(2) or j.group(3)
    return (term.group(0) if term else grp, jj)


def core_config(sp):
    el, rom = sp.split()
    Z, ch = SYMBOL[el], ROMAN[rom]
    core = Z - ch
    if core < 1:
        return Z, ch, []
    if sp in CORE_OVERRIDE:
        shells = CORE_OVERRIDE[sp]
        # expand through the seated member's own expander by borrowing its bracket cores
        cfg = []
        for sym, n, l, o in re.findall(r"\[([A-Z][a-z]?)\]|(\d)([spdf])(\d*)", shells):
            if sym:
                cfg += LW1.expand(LW1.CORE[sym])
            else:
                cfg.append((int(n), "spdf".index(l), int(o or 1)))
        return Z, ch, cfg
    return Z, ch, LW1.expand(core)


def core_class(cfg):
    if not cfg:
        return "bare"
    opn = [(n, l, o) for n, l, o in cfg if 0 < o < 2 * (2 * l + 1)]
    if not opn:
        return "closed"
    nt = core_terms(cfg)
    if nt == 1:
        return "one-term-2J" if (len(opn) == 1 and opn[0][1] > 0) else "one-term-1J"
    return "multi"


def section_channels():
    print("\nF. THE CHANNEL TABLE")
    hdr, data = channel_rows()
    num("rows", len(data))
    rec("EXHAUSTIVE", "596 data rows under the eleven-column header", len(data) == 596 and hdr[1][:2] == ["species", "series"],
        "rows=%d" % len(data))
    c4rows = C4.rows()
    rec("EXHAUSTIVE", "the seated reader (compendia4) returns the same 596 rows",
        len(c4rows) == 596 and [i for i, c in c4rows] == [i for i, c in data])
    sp = [species_of(c) for i, c in data]
    num("species", len(set(sp)))
    num("elements", len({s.split()[0] for s in sp}))
    num("starred", sum("*" in c[0] for i, c in data))
    num("levels", sum(int(c[3]) for i, c in data))
    num("interior", sum(int(c[4]) for i, c in data))
    rec("EXHAUSTIVE", "28 elements, 70 species, 119 two-member rows, 3,342 levels, 2,269 interior cells",
        (NUMBERS["elements"], NUMBERS["species"], NUMBERS["starred"], NUMBERS["levels"], NUMBERS["interior"])
        == (28, 70, 119, 3342, 2269))
    m = k = rb = nt = ut = 0
    for i, c in data:
        br = c[5]
        if "/" in br:
            x, y = br.split("/")
            m += int(x); k += int(y); rb += 1
        elif br == "no-triple":
            nt += 1
        elif br == "untested":
            ut += 1
    num("bracket_pass", m); num("bracket_cells", k); num("bracket_rows", rb); num("no_triple", nt); num("untested", ut)
    rec("EXHAUSTIVE", "bracket column: 1,577 of 1,738 cells on 392 rows; 78 no-triple; 126 untested; 392+78+126 = 596",
        (m, k, rb, nt, ut) == (1577, 1738, 392, 78, 126) and rb + nt + ut == 596)
    forms = collections.Counter(label_form(c[1]) for i, c in data)
    num("label_forms", dict(forms))
    num("paren_rows", sum("(" in c[1] for i, c in data))
    rec("EXHAUSTIVE", "label conventions: 80 dotted, 20 bare term, 39 other parenthesised (jj pairs and undotted "
        "configurations), 457 none; 139 carry a parenthesised group",
        forms == {"dotted": 80, "bare-term": 20, "other-paren": 39, "none": 457} and NUMBERS["paren_rows"] == 139,
        "%s" % dict(forms))
    conv = collections.Counter(label_convention(c[1]) for i, c in data)
    num("label_conventions", dict(conv))
    rec("EXHAUSTIVE", "five conventions: 80 dotted configuration, 9 run-on configuration, 20 bare term, "
        "30 jj pair, 457 none; 139 name a parent and 80 of them match the dotted pattern",
        conv == {"dotted-config": 80, "run-on-config": 9, "bare-term": 20, "jj-pair": 30, "none": 457}
        and sum(v for k, v in conv.items() if k != "none") == 139, "%s" % dict(conv))
    rec("EXHAUSTIVE", "a census run with the dotted pattern alone reports 80 of the 139 -- it undercounts by 59",
        forms["dotted"] == 80 and NUMBERS["paren_rows"] - forms["dotted"] == 59)
    # limits per species
    lims = collections.defaultdict(set)
    for i, c in data:
        lims[species_of(c)].add(c[10])
    F = lambda s: Fraction(s.replace(",", ""))
    parents, roundings = [], []
    for s, L in sorted(lims.items()):
        if len(L) < 2:
            continue
        v = sorted(F(x) for x in L)
        (roundings if v[-1] - v[0] < 1 else parents).append((s, [str(x) for x in sorted(L, key=F)], v[-1] - v[0]))
    num("two_limit_species", [(s, L, str(g)) for s, L, g in parents])
    num("rounding_species", [(s, L, str(g)) for s, L, g in roundings])
    rec("EXHAUSTIVE", "species printing two or more limits a wavenumber or more apart: Ba III, Ne I, Ne II, Si I",
        [s for s, L, g in parents] == ["Ba III", "Ne I", "Ne II", "Si I"])
    rec("EXHAUSTIVE", "and three whose two limits differ by less than a wavenumber (Ca II 0.010, Li I 0.036, Zn I 0.020)",
        [(s, g) for s, L, g in roundings] == [("Ca II", Fraction("0.010")), ("Li I", Fraction("0.036")), ("Zn I", Fraction("0.020"))])
    gaps = {s: g for s, L, g in parents}
    num("ba3_gap", str(gaps["Ba III"]))
    rec("EXHAUSTIVE", "Ba III: 306,650.000 - 289,100.000 = 17,550 exactly (Fraction)",
        gaps["Ba III"] == 17550 and sorted(lims["Ba III"], key=F) == ["289,100.000", "306,650.000"])
    g1, g2 = F("174,710.090") - F("173,929.750"), F("390,977.350") - F("173,929.750")
    num("ne1_gaps", ["%.2f" % float(g1), "%.2f" % float(g2)])
    num("ne2_gap", "%.3f" % float(gaps["Ne II"]))
    num("si1_gap", "%.3f" % float(gaps["Si I"]))
    rec("EXHAUSTIVE", "Ne I 780.34 and 217,047.60 above its first limit; Ne II 25,840.700; Si I 287.240 (Fraction)",
        g1 == Fraction("780.34") and g2 == Fraction("217047.6") and gaps["Ne II"] == Fraction("25840.7") and gaps["Si I"] == Fraction("287.24"))
    # every row of a two-limit species names its parent, and limit <-> parent is a bijection
    bij_ok = True
    limit_parent = {}
    for s, L, g in parents:
        for lim in L:
            keys = {parent_key(c[1]) for i, c in data if species_of(c) == s and c[10] == lim}
            if None in keys:
                bij_ok = False
            # collapse (term, j) and ("j", j) spellings onto the core J where one is present
            js = {kk[1] for kk in keys if kk and kk[1] is not None}
            terms = {kk[0] for kk in keys if kk and kk[0] != "j"}
            limit_parent[(s, lim)] = (sorted(terms), sorted(js))
    num("limit_parent", {"%s @ %s" % k: v for k, v in limit_parent.items()})
    want = {("Ba III", "289,100.000"): (["2P*"], ["3/2"]), ("Ba III", "306,650.000"): (["2P*"], ["1/2"]),
            ("Ne I", "173,929.750"): (["2P*"], ["3/2"]), ("Ne I", "174,710.090"): (["2P*"], ["1/2"]),
            ("Ne I", "390,977.350"): (["2S"], []),
            ("Ne II", "330,388.600"): (["3P"], []), ("Ne II", "356,229.300"): (["1D"], []),
            ("Si I", "65,747.760"): (["2P*"], ["1/2"]), ("Si I", "66,035.000"): (["2P*"], ["3/2"])}
    rec("EXHAUSTIVE", "in those four species every row names its parent, one parent per limit, distinct parents at distinct limits",
        bij_ok and limit_parent == want, "" if limit_parent == want else "%s" % limit_parent)
    # the outer label, with the parent prefix stripped, printed at two limits of one species:
    # the witness that the outer label does NOT determine the parent
    strip = collections.defaultdict(set)
    for i, c in data:
        strip[(species_of(c), normalise(c[1]))].add(c[10])
    amb = {kk: sorted(v) for kk, v in strip.items() if len(v) > 1}
    num("outer_label_two_limits", sorted((kk[0], kk[1], v) for kk, v in amb.items()))
    rec("EXHAUSTIVE", "exactly two outer labels are printed at two limits of one species, and only one is a "
        "parent case: Ba III nd 2[3/2]* J=2 at both its limits (the other is Ca II's 0.010 rounding)",
        len(amb) == 2 and sorted(kk[0] for kk in amb) == ["Ba III", "Ca II"]
        and amb[("Ba III", "nd 2[3/2]* J=2")] == ["289,100.000", "306,650.000"], "%s" % sorted(amb))
    rowcount = collections.Counter(species_of(c) for i, c in data)
    bylim = {s: dict(collections.Counter(c[10] for i, c in data if species_of(c) == s))
             for s in ("Ba III", "Ne I", "Ne II", "Si I")}
    num("two_limit_rows", {s: rowcount[s] for s in ("Ba III", "Ne I", "Ne II", "Si I")})
    num("rows_by_limit", bylim)
    rec("EXHAUSTIVE", "the four two-limit species carry 99 rows: Ba III 22 (20 + 2), Ne I 7 (4 + 2 + 1), "
        "Ne II 37 (29 + 8), Si I 33 (18 + 15)",
        [rowcount[s] for s in ("Ba III", "Ne I", "Ne II", "Si I")] == [22, 7, 37, 33]
        and sorted(bylim["Ba III"].values()) == [2, 20] and sorted(bylim["Ne I"].values()) == [1, 2, 4]
        and sorted(bylim["Ne II"].values()) == [8, 29] and sorted(bylim["Si I"].values()) == [15, 18])
    # the four Ar II notation duplicates
    g = collections.defaultdict(list)
    for i, c in data:
        g[(species_of(c), normalise(c[1]), c[2])].append((i, c))
    dup = {kk: v for kk, v in g.items() if len(v) > 1 and len({x[1][1] for x in v}) > 1}
    num("notation_duplicates", sorted((kk[0], kk[1], kk[2], [x[0] for x in v]) for kk, v in dup.items()))
    rec("EXHAUSTIVE", "one series printed under two notations: exactly 4 pairs, all Ar II, delta equal to four decimals, sigma differing",
        len(dup) == 4 and all(kk[0] == "Ar II" for kk in dup)
        and all(len({x[1][7] for x in v}) == 1 and len({x[1][8] for x in v}) == 2 for v in dup.values()))
    rec("EXHAUSTIVE", "Ar II prints one limit on all 44 of its rows", len(lims["Ar II"]) == 1 and sp.count("Ar II") == 44)
    # the two Ba III windows and the two Si I identical-key pairs
    w = collections.defaultdict(list)
    for i, c in data:
        w[(species_of(c), c[1], c[10])].append(c[2])
    ba = {kk: v for kk, v in w.items() if len(v) > 1 and kk[0] == "Ba III"}
    num("ba3_windows", sorted((kk[1], sorted(v)) for kk, v in ba.items()))
    rec("EXHAUSTIVE", "Ba III: two channels each fitted in two adjacent n-windows under one parent (5-7 / 8-22, 6-8 / 9-23)",
        sorted(tuple(sorted(v)) for v in ba.values()) == [("5–7", "8–22†"), ("6–8", "9–23")])
    key3 = collections.defaultdict(list)
    for i, c in data:
        key3[(c[0], c[1], c[2])].append(i)
    d3 = {kk: v for kk, v in key3.items() if len(v) > 1}
    num("identical_key_pairs", sorted((kk[0], kk[1], kk[2]) for kk in d3))
    rec("EXHAUSTIVE", "(species, series, n-range) repeats exactly twice, both Si I (20-50 and 20-56)",
        sorted((kk[0], kk[2]) for kk in d3) == [("Si I", "20–50"), ("Si I", "20–56")])
    # the core-class census
    cls = {}
    for s in set(sp):
        Z, ch, cfg = core_config(s)
        cls[s] = core_class(cfg)
    cen = collections.Counter(cls[s] for s in sp)
    named = collections.Counter((cls[species_of(c)], "(" in c[1]) for i, c in data)
    num("core_classes", dict(cen))
    num("named_by_class", {"%s/%s" % kk: v for kk, v in named.items()})
    rec("EXHAUSTIVE", "rows by core: 38 bare nucleus, 159 closed shell, 174 one term one level, 127 one term two levels, 98 several terms",
        cen == {"bare": 38, "closed": 159, "one-term-1J": 174, "one-term-2J": 127, "multi": 98}, "%s" % dict(cen))
    need = cen["one-term-2J"] + cen["multi"]
    have = named[("one-term-2J", True)] + named[("multi", True)]
    num("rows_needing_parent", need)
    num("rows_needing_named", have)
    num("rows_needing_unnamed", need - have)
    rec("EXHAUSTIVE", "225 rows have a core with more than one level; 132 of them name the parent in the label, 93 do not",
        (need, have) == (225, 132))
    # every unnamed row in those classes belongs to a species printing a single limit
    un = {species_of(c) for i, c in data if cls[species_of(c)] in ("one-term-2J", "multi") and "(" not in c[1]}
    num("unnamed_species", sorted(un))
    rec("EXHAUSTIVE", "and every one of the 93 belongs to a species printing exactly one limit (13 species)",
        all(len(lims[s]) == 1 for s in un) and len(un) == 13, "%s" % sorted(un))
    rec("EXHAUSTIVE", "rows whose core has a single level (371) need no parent in the label; 7 of them carry one anyway",
        cen["bare"] + cen["closed"] + cen["one-term-1J"] == 371
        and named[("closed", True)] + named[("one-term-1J", True)] + named[("bare", True)] == 7)
    # core_terms multiplies per-subshell term counts, which is the configuration's term count only
    # when at most ONE subshell is open.  That holds on every species here, so the census is exact.
    nopen = {s: len([1 for n, l, o in core_config(s)[2] if 0 < o < 2 * (2 * l + 1)]) for s in set(sp)}
    num("max_open_subshells", max(nopen.values()))
    num("open_shapes", sorted({(core_config(s)[2][-1][1], core_config(s)[2][-1][2])
                               for s in set(sp) if nopen[s] == 1}))
    rec("EXHAUSTIVE", "no core in the table has more than one open subshell, so a term count is a "
        "single-subshell count; the open shapes present are s1, p1, p2, p4, p5 and d1",
        max(nopen.values()) == 1
        and NUMBERS["open_shapes"] == [(0, 1), (1, 1), (1, 2), (1, 4), (1, 5), (2, 1)],
        "%s" % NUMBERS["open_shapes"])
    # the multi-term cores present are all three-term p^2 / p^4 cores
    mt = {s for s in set(sp) if cls[s] == "multi"}
    rec("EXHAUSTIVE", "every several-term core in the table is a p^2 or p^4 core (3 LS terms): %s" % ", ".join(sorted(mt)),
        all(core_terms(core_config(s)[2]) == 3 for s in mt))
    num("multi_species", sorted(mt))
    # the highest-charge open-shell ion, and the closed-shell ions at charge 15-16
    charges = {s: ROMAN[s.split()[1]] for s in set(sp)}
    open_max = max(charges[s] for s in set(sp) if cls[s] in ("one-term-2J", "multi"))
    num("open_shell_max_charge", open_max)
    top = sorted(s for s in set(sp) if cls[s] in ("one-term-2J", "multi") and charges[s] == open_max)
    num("open_shell_max_species", top)
    rec("EXHAUSTIVE", "no core with more than one level above spectrum number IV, and IV is reached once (Al IV); "
        "Fe XV carries a one-level core and Fe XVI a closed one",
        open_max == 4 and top == ["Al IV"] and cls["Fe XV"] == "one-term-1J" and cls["Fe XVI"] == "closed",
        "max=%d at %s" % (open_max, top))


# =============================================================================================
# G. The coordinate file
# =============================================================================================

def coord_rows():
    rows = list(csv.DictReader(open(COORDS, newline="", encoding="utf-8")))
    for r in rows:
        for kk in ("Z", "charge", "l", "mult"):
            r[kk] = int(r[kk])
        r["delta"] = Fraction(r["delta"])
        r["B"] = Fraction(r["B"])
    return rows


def section_coordinates(rows):
    print("\nG. THE COORDINATE FILE")
    num("cells", len(rows))
    keys = {(r["Z"], r["charge"], r["mult"]) for r in rows}
    pairs = {(r["Z"], r["charge"]) for r in rows}
    num("keys", len(keys)); num("pairs", len(pairs))
    rec("EXHAUSTIVE", "104,832 cells = 13,104 keys (Z, charge, 2S+1) x 8 values of l; 7,260 (Z, charge) pairs, Z <= 120",
        len(rows) == 104832 and len(keys) == 13104 and len(pairs) == 7260 and max(r["Z"] for r in rows) == 120
        and all(r["charge"] <= r["Z"] for r in rows)
        and collections.Counter(len({r["l"] for r in rows if (r["Z"], r["charge"], r["mult"]) == kk}) for kk in list(keys)[:0]) == collections.Counter())
    per_key = collections.Counter((r["Z"], r["charge"], r["mult"]) for r in rows)
    rec("EXHAUSTIVE", "every key carries all eight l", all(v == 8 for v in per_key.values()))
    grades = collections.Counter(r["grade"] for r in rows)
    num("grades", dict(grades))
    rec("EXHAUSTIVE", "grades: 929 exact, 358 measured, 103,545 computed",
        grades == {"exact": 929, "measured": 358, "computed": 103545})
    rec("EXHAUSTIVE", "measured and witnessed are the same 358 cells, cell by cell",
        all((r["grade"] == "measured") == (r["witness"] == "witnessed") for r in rows))
    num("witness_pct", "%.3f" % (100 * 358 / 104832))
    num("unwitnessed", 104832 - 358)
    tab = []
    for l in range(8):
        g = collections.Counter(r["grade"] for r in rows if r["l"] == l)
        ds = [r["delta"] for r in rows if r["l"] == l]
        tab.append((l, sum(g.values()), g["exact"], g["measured"], g["computed"], min(ds), max(ds)))
    num("per_l", [(l, n, e, m, c, "%.4f" % float(lo), "%.4f" % float(hi)) for l, n, e, m, c, lo, hi in tab])
    rec("EXHAUSTIVE", "per-l table: exact 115 (l<=4) / 118 (l>=5); measured 92, 81, 89, 59, 36, 1, 0, 0",
        [t[2] for t in tab] == [115] * 5 + [118] * 3 and [t[3] for t in tab] == [92, 81, 89, 59, 36, 1, 0, 0])
    bnd = collections.Counter(r["bound"] for r in rows)
    num("bounds", bnd.most_common())
    top = {"series unresolved above ng in any published analysis": 28526, "no long-lived isotope": 24312,
           "not keyable: no single 2S+1 (hole+electron or multi-valence)": 17626, "open-shell core, 16 parents": 11605,
           "open-shell core, 3 parents": 9756, "open-shell core, 119 parents": 5280,
           "no analysis located at this charge (NOT a bound on existence)": 2691,
           "derived by symmetry; no measurement required": 929, "-": 333,
           "none — separable series, simply not yet measured": 240}
    rec("EXHAUSTIVE", "22 distinct bound strings; the ten largest counts as printed (28,526 ... 240; 333 witnessed cells carry none)",
        len(bnd) == 22 and all(bnd[kk] == v for kk, v in top.items()) and bnd["no primordial isotope (R 1587)"] == 5)
    wb = sum(1 for r in rows if r["witness"] == "witnessed" and r["bound"] != "-")
    num("witnessed_with_bound", wb)
    rec("EXHAUSTIVE", "25 witnessed cells carry a bound, every one a named series limit outside a closed shell",
        wb == 25 and all(r["bound"].startswith("limit ") for r in rows if r["witness"] == "witnessed" and r["bound"] != "-"))
    # parent-count bounds map onto the block's maximum LS term count
    byb = collections.defaultdict(set)
    for r in rows:
        m = re.match(r"open-shell core, (\d+) parents", r["bound"])
        if m:
            core = r["Z"] - r["charge"]
            cfg = POP.aufbau_config(core)
            opn = [(n, l, o) for n, l, o in cfg if 0 < o < 2 * (2 * l + 1)]
            byb[int(m.group(1))].add((len(opn), opn[0][1] if opn else None, core_terms(cfg)))
    num("parent_bounds", {kk: sorted(v) for kk, v in byb.items()})
    rec("EXHAUSTIVE", "'3 parents' = one open p subshell with 3 terms; '16 parents' = one open d subshell (5, 8 or 16 terms); "
        "'119 parents' = one open f subshell (7 to 119 terms)",
        byb[3] == {(1, 1, 3)} and {t[1] for t in byb[16]} == {2} and {t[2] for t in byb[16]} == {5, 8, 16}
        and {t[1] for t in byb[119]} == {3} and {t[2] for t in byb[119]} == {7, 17, 47, 73, 119})
    # the multiplicity coordinate
    ms = collections.defaultdict(set)
    for r in rows:
        ms[(r["Z"], r["charge"])].add(r["mult"])
    byNe = collections.defaultdict(set)
    for (Z, c), mset in ms.items():
        byNe[Z - c + 1].add(frozenset(mset))
    rec("EXHAUSTIVE", "the admitted multiplicities at a pair depend on the electron count alone (7,260 pairs, 120 counts)",
        all(len(v) == 1 for v in byNe.values()) and len(byNe) == 120)

    def hund(cfg):
        S2 = sum(min(o, 2 * (2 * l + 1) - o) for n, l, o in cfg)
        return frozenset({S2 + 2} | ({S2} if S2 > 0 else set()))
    bad_m = [Ne for Ne in range(1, 121) if hund(POP.aufbau_config(Ne - 1) if Ne > 1 else []) != next(iter(byNe[Ne]))]
    bad_o = [Ne for Ne in range(2, 110) if hund(LW1.expand(Ne - 1)) != next(iter(byNe[Ne]))]
    num("hund_madelung_mismatch", bad_m); num("hund_observed_mismatch", bad_o)
    rec("EXHAUSTIVE", "they are Hund's rule on the core in Madelung order at all 120 counts; on the observed configuration "
        "six counts differ (25, 42, 43, 47, 65, 97)", bad_m == [] and bad_o == [25, 42, 43, 47, 65, 97], "%s" % bad_o)
    # sources
    kinds = collections.Counter()
    for r in rows:
        s = r["source"]
        kinds["equation" if s == "the channel equation" else "one-electron" if s.startswith("one electron")
              else "captured" if s == "captured levels" else "NIST" if s.startswith("NIST ASD")
              else "Theodosiou" if "Theodosiou" in s else "level files"] += 1
    num("source_kinds", dict(kinds))
    num("source_strings", len({r["source"] for r in rows}))
    rec("EXHAUSTIVE", "six provenances over 32 strings: 103,545 equation, 929 one-electron, 325 captured, 25 NIST, 3 level files, 5 Theodosiou",
        kinds == {"equation": 103545, "one-electron": 929, "captured": 325, "NIST": 25, "level files": 3, "Theodosiou": 5}
        and NUMBERS["source_strings"] == 32)
    # the Pauli bound
    nzB = sum(r["B"] != 0 for r in rows)
    niB = sum(r["B"].denominator != 1 for r in rows)
    num("B_nonzero", nzB); num("B_nonint", niB)
    rec("EXHAUSTIVE", "B is nonzero on 36,917 cells and non-integer on 25", (nzB, niB) == (36917, 25))
    meas = [r for r in rows if r["grade"] == "measured"]
    hold_printed = sum(math.floor(r["delta"]) <= r["B"] for r in meas)
    fails = [r for r in meas if math.floor(r["delta"]) > r["B"]]
    recomputed = []
    for r in meas:
        core = r["Z"] - r["charge"]
        Bc = POP.pauli_bound(r["Z"], r["charge"], r["l"], config=POP.aufbau_config(core)) if core >= 1 else 0
        recomputed.append((r, Bc))
    hold_rec = sum(math.floor(r["delta"]) <= Bc for r, Bc in recomputed)
    num("floorB_printed", hold_printed); num("floorB_recomputed", hold_rec)
    num("floorB_fail_cells", [(r["Z"], r["charge"], r["l"], "%.4f" % float(r["delta"]), str(r["B"])) for r in fails])
    rec("EXHAUSTIVE", "floor(delta) <= B on all 358 measured cells when B is read from the core in Madelung order; "
        "the printed B column fails on 11, all among the 25 non-integer entries",
        hold_rec == 358 and hold_printed == 347 and all(r["B"].denominator != 1 for r in fails))
    rec("EXHAUSTIVE", "the printed B equals the Madelung-order bound on 102,383 of 104,832 cells (the rest carry n0 read otherwise or the 25)",
        sum(1 for r in rows if r["Z"] - r["charge"] >= 1 and
            POP.pauli_bound(r["Z"], r["charge"], r["l"], config=POP.aufbau_config(r["Z"] - r["charge"])) == r["B"]) == 102383)
    # which cells can be measured: the chain with the cuts that reproduce the printed counts
    c1 = sum(r["Z"] <= 92 for r in rows)
    c2 = sum(r["Z"] <= 83 and r["charge"] <= 10 for r in rows)
    c3 = sum(r["Z"] <= 83 and r["charge"] <= 6 and r["l"] <= 4 for r in rows)
    single = {}
    for (Z, c) in pairs:
        core = Z - c
        single[(Z, c)] = True if core < 1 else core_terms(POP.aufbau_config(core)) == 1
    c4 = sum(r["Z"] <= 83 and r["charge"] <= 6 and r["l"] <= 4 and single[(r["Z"], r["charge"])] for r in rows)
    num("chain", [c1, c2, c3, c4])
    rec("EXHAUSTIVE", "Z <= 92: 61,152; Z <= 83 and charge <= 10: 11,416; Z <= 83, charge <= 6, l <= 4: 4,395; and a one-term core: 1,755",
        [c1, c2, c3, c4] == [61152, 11416, 4395, 1755], "%s" % [c1, c2, c3, c4])
    c2b = sum(r["Z"] <= 92 and r["charge"] <= 10 for r in rows)
    c3b = sum(r["Z"] <= 83 and r["charge"] <= 10 and r["l"] <= 4 for r in rows)
    num("chain_alt", [c2b, c3b])
    rec("EXHAUSTIVE", "(the same cuts held at Z <= 92 give 12,720 at charge <= 10, and at charge <= 10 give 7,135 at l <= 4)",
        [c2b, c3b] == [12720, 7135])


# =============================================================================================
# H. The Janet collapse, measured on the coordinate file
# =============================================================================================

def mann_whitney(a, b):
    """Two-sided Mann-Whitney U with the normal approximation and tie correction."""
    allv = sorted([(v, 0) for v in a] + [(v, 1) for v in b])
    n = len(allv)
    rk = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and allv[j + 1][0] == allv[i][0]:
            j += 1
        for kk in range(i, j + 1):
            rk[kk] = (i + j) / 2 + 1
        i = j + 1
    n1, n2 = len(a), len(b)
    R1 = sum(rk[kk] for kk in range(n) if allv[kk][1] == 0)
    U1 = R1 - n1 * (n1 + 1) / 2
    U = min(U1, n1 * n2 - U1)
    cnt = collections.Counter(v for v, _ in allv)
    T = sum(c ** 3 - c for c in cnt.values())
    sig = math.sqrt(n1 * n2 / 12 * ((n + 1) - T / (n * (n - 1))))
    zc = (U - n1 * n2 / 2) / sig
    return U, zc, math.erfc(abs(zc) / math.sqrt(2))


def section_collapse(rows):
    print("\nH. THE JANET COLLAPSE")
    thr = {2: 21, 3: 57}
    meas = [r for r in rows if r["grade"] == "measured" and r["l"] in (2, 3)]
    cand = []
    for r in meas:
        core = r["Z"] - r["charge"]
        p = POP.core_p(core, r["l"]) if core >= 1 else 0
        if p == 0:
            cand.append(r)
    num("p0_cells", len(cand)); num("measured_l23", len(meas))
    col = [r for r in cand if r["Z"] >= thr[r["l"]]]
    unc = [r for r in cand if r["Z"] < thr[r["l"]]]
    med = lambda v: sorted(v)[len(v) // 2] if len(v) % 2 else (sorted(v)[len(v) // 2 - 1] + sorted(v)[len(v) // 2]) / 2
    mc, mu = med([float(r["delta"]) for r in col]), med([float(r["delta"]) for r in unc])
    U, zc, p = mann_whitney([float(r["delta"]) for r in col], [float(r["delta"]) for r in unc])
    num("collapsed_n", len(col)); num("uncollapsed_n", len(unc))
    num("collapsed_median", "%.4f" % mc); num("uncollapsed_median", "%.4f" % mu)
    num("utest_U", U); num("utest_z", "%.2f" % zc); num("utest_p", "%.1e" % p)
    rec("EXHAUSTIVE", "128 of the 148 measured d and f cells have p = 0; 7 lie at or past the block boundary, 121 below",
        (len(meas), len(cand), len(col), len(unc)) == (148, 128, 7, 121))
    rec("EXHAUSTIVE", "medians 0.6202 (past) against 0.0335 (below); Mann-Whitney U = 74, z = -3.66, p = 2.5e-4",
        NUMBERS["collapsed_median"] == "0.6202" and NUMBERS["uncollapsed_median"] == "0.0335" and U == 74 and p < 1e-3,
        "U=%s z=%.2f p=%.1e" % (U, zc, p))
    num("collapsed_cells", sorted((r["Z"], r["charge"], r["l"], "%.4f" % float(r["delta"])) for r in col))
    rec("EXHAUSTIVE", "the seven: Sc III nd, Ti III nd (two rows), Ti IV nd, Fe VIII nd, Fe XV nd, Fe XVI nd",
        [(r["Z"], r["charge"]) for r in sorted(col, key=lambda r: (r["Z"], r["charge"]))]
        == [(21, 3), (22, 3), (22, 3), (22, 4), (26, 8), (26, 15), (26, 16)])
    named = {}
    for r in cand:
        named[(r["Z"], r["charge"], r["l"])] = named.get((r["Z"], r["charge"], r["l"]), []) + [float(r["delta"])]
    want = {(22, 4, 2): 0.6202, (38, 2, 3): 0.0618, (20, 1, 2): 0.9084, (56, 2, 3): 0.7559, (20, 2, 2): 0.6341, (19, 1, 2): 0.2460}
    got = {kk: max(named[kk]) for kk in want}
    num("named_defects", {"%d/%d/%d" % kk: "%.4f" % v for kk, v in got.items()})
    rec("EXHAUSTIVE", "Ti IV nd 0.6202, Sr II nf 0.0618, Ca I nd 0.9084, Ba II nf 0.7559, Ca II nd 0.6341, K I nd 0.2460",
        all(abs(got[kk] - v) < 5e-5 for kk, v in want.items()))
    num("ratio_ti_sr", "%.1f" % (0.6202 / 0.0618))
    rec("EXHAUSTIVE", "Ca I nd is the largest defect of the 128, and it sits below the boundary",
        max(cand, key=lambda r: r["delta"])["Z"] == 20 and max(cand, key=lambda r: r["delta"])["charge"] == 1)
    # the thresholds are the row openings of the (n+l, Z) index
    starts = NUMBERS["janet_starts"]
    rec("EXHAUSTIVE", "the thresholds 21, 57, 89 are the openings of rows n+l = 5, 7, 8",
        (starts[4], starts[6], starts[7]) == (21, 57, 89))
    # first Z whose differentiating electron is 3d / 4f / 5f, from the observed configurations
    first = {}
    for Z in range(2, 109):
        cell = POP.janet_cell(Z)
        now = {(n, l): o for n, l, o in LW1.expand(Z)}
        before = {(n, l): o for n, l, o in LW1.expand(Z - 1)}
        gained = sorted((n, l) for (n, l), o in now.items() if o > before.get((n, l), 0))
        for nl in gained:
            first.setdefault(nl, Z)
    num("first_occupation", {"3d": first[(3, 2)], "4f": first[(4, 3)], "5f": first[(5, 3)], "5d": first[(5, 2)], "6d": first[(6, 2)]})
    rec("EXHAUSTIVE", "3d first occupied at Z = 21; 4f at 58 (La takes 5d at 57); 5f at 91 (Ac, Th take 6d)",
        (first[(3, 2)], first[(4, 3)], first[(5, 3)], first[(5, 2)], first[(6, 2)]) == (21, 58, 91, 57, 89))
    # the ramp the equation uses, as the seated instrument carries it
    C = POP.collapse_C
    rec("EXHAUSTIVE", "the collapse coordinate of the channel equation is 0.5 at the boundary, 0 four below, 1 four above",
        all(C(z0, l) == 0.5 and C(z0 - 4, l) == 0.0 and C(z0 + 4, l) == 1.0 for l, z0 in ((2, 21), (3, 57))))
    num("C_ca", C(20, 2)); num("C_ba", C(56, 3))


# =============================================================================================
# I. Exact arithmetic
# =============================================================================================

def section_exact():
    print("\nI. EXACT ARITHMETIC")
    rec("EXHAUSTIVE", "E = |R(X)| - |X|: 126 - 90 = 36, 944 - 944 = 0, 224 - 118 = 106, 126 - 106 = 20",
        Fraction(126) - 90 == 36 and 224 - 118 == 106 and 126 - 106 == 20)
    rec("EXHAUSTIVE", "25 + 11 = 36 and 16 + 10 + 10 = 36", 25 + 11 == 36 and 16 + 10 + 10 == 36)
    rec("EXHAUSTIVE", "358 / 104,832 = 0.3415 per cent", abs(Fraction(358, 104832) * 100 - Fraction("0.3415")) < Fraction(1, 10000))
    rec("EXHAUSTIVE", "2 + 2 + 8 + 8 + 18 + 18 + 32 + 30 = 118; with 32 in the last row, 120",
        sum(JANET_ROWS_118) == 118 and sum(JANET_ROWS_120) == 120)
    rec("EXHAUSTIVE", "the Janet row lengths are 2(k')^2 with k' = 1,1,2,2,3,3,4,4",
        JANET_ROWS_120 == [2 * kk * kk for kk in (1, 1, 2, 2, 3, 3, 4, 4)])
    rec("EXHAUSTIVE", "the single-term cut removes 4,395 - 1,755 = 2,640 cells, and 139 - 80 = 59 rows "
        "separate the widest from the narrowest parent census",
        NUMBERS["chain"][2] - NUMBERS["chain"][3] == 2640
        and NUMBERS["paren_rows"] - NUMBERS["label_forms"]["dotted"] == 59)
    rec("EXHAUSTIVE", "the three parent-count obstacles cover 9,756 + 11,605 + 5,280 = 26,641 cells",
        dict(NUMBERS["bounds"])["open-shell core, 3 parents"]
        + dict(NUMBERS["bounds"])["open-shell core, 16 parents"]
        + dict(NUMBERS["bounds"])["open-shell core, 119 parents"] == 26641)


# =============================================================================================

def main(selftest=False):
    print("check.py -- The parent-term wall and the Janet collapse")
    print("=" * 100)
    section_periodic()
    section_janet()
    section_z3(negative=selftest)
    section_terms()
    section_channels()
    rows = coord_rows()
    section_coordinates(rows)
    section_collapse(rows)
    section_exact()
    if selftest:
        print("\nNEGATIVE CONTROLS (each must be refuted)")
        S, E = E_of(periodic_cells(), ["period", "group"])
        rec("NEGATIVE", "control: 'E(periodic) = 35' is refuted", E != 35, "E=%d" % E)
        # A cell MOVED off the chain, not one appended to it.  Appending (3, 13) leaves the
        # index a chain and therefore closed (recorded as an obligation in section C), so it
        # is no control at all; moving Z = 30 out of row 5 into row 2 breaks the chain.
        X = [c for c in janet_cells(JANET_ROWS_118) if c != (5, 30)] + [(2, 30)]
        S2, E2 = E_of(X, ["n+l", "Z"])
        rec("NEGATIVE", "control: the Janet index with one element moved to the wrong row is NOT closed",
            E2 > 0, "E=%d" % E2)
        rec("NEGATIVE", "control: a wrong term count (d^4 = 15) is refuted", TERMS[(2, 4)] != 15)
    print("\n" + "=" * 100)
    by = collections.Counter(s for s, n, ok, d in RESULTS if ok)
    print("summary: %s" % ", ".join("%s %d" % kv for kv in sorted(by.items())))
    print("obligations: %d, failed: %d" % (len(RESULTS), len(FAILS)))
    for f in FAILS:
        print("  FAILED: " + f)
    if "--numbers" in sys.argv:
        import json
        print(json.dumps(NUMBERS, indent=1, default=str))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main(selftest="--selftest" in sys.argv))
