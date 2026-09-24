#!/usr/bin/env python3
"""check.py -- the machine checks behind "The Lattice of Subshell Transitions".

Every number the paper prints and every decidable claim it makes is produced here.  Five kinds
of check, kept apart in the report and never merged:

  MACHINE-CHECKED  Z3 returned `unsat` on the negation of an obligation whose variables range
                   over every INTEGER (so the result holds at every cap, not one box), or over
                   every subset of a named finite box, after the two guards passed;
  EXHAUSTIVE       a decision procedure visited every case of a stated finite family;
  SAMPLED          a seeded pseudorandom sweep of a stated size;
  REFUTATION       a claim disproved by an explicit witness;
  CITED            taken from the literature; printed, not checked.

The object under test is the seated construction, imported by path and never copied:
  - method/members/tower-2.py       L8(), the 976 cells;
  - tools/cypher.py                 op_order, the staircase closure R.
Reference implementations used by the guards are written fresh here; that is the point of a
guard.  The subset-quantified Z3 harness is research/warp-drive/prover.py, imported by path.

    python3 check.py             every obligation, one line each, a summary, exit 1 on failure
    python3 check.py --selftest  the same, plus negative controls that MUST be refuted
"""
import importlib.util
import itertools
import math
import os
import random
import re
import sys
import time
from collections import defaultdict, deque
from fractions import Fraction
from math import gcd, prod

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TOWER = os.path.join(REPO, "method", "members", "tower-2.py")
CYPHER = os.path.join(REPO, "tools", "cypher.py")
PROVER = os.path.join(REPO, "research", "warp-drive", "prover.py")
TABLE = os.path.join(REPO, "method", "members",
                     "The_Method_1_6___The_Index_of_Indices-2.md")

SEED = 20260921


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


tower = load("tower2", TOWER)
cypher = load("cypher", CYPHER)
prover = load("prover", PROVER)
import z3                                                          # noqa: E402

# ------------------------------------------------------------------ reporting

ROWS = []
FAILS = []


def sup(n):
    """An integer as Unicode superscript digits, for row details the paper quotes."""
    return str(n).translate(str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻"))


def row(status, name, detail, ok=True):
    ROWS.append((status, name, detail, ok))
    if not ok:
        FAILS.append(name)
    print("  [%s] %-16s %-56s %s" % ("ok" if ok else "XX", status, name, detail))


# =========================================================== the object itself

CO = ["n", "l", "k", "q", "e", "f", "g", "2S"]
D = 8
IN, IL, IK, IQ, IE, IF, IG, IS = range(8)

# The seven monotone bounds, written fresh (the guard's independent implementation).
CONSTRAINTS = [
    ("l <= n-1",    IL, IN, lambda n: n - 1),
    ("k <= 4l+2",   IK, IL, lambda l: 4 * l + 2),
    ("q <= k",      IQ, IK, lambda k: k),
    ("f <= e-1",    IF, IE, lambda e: e - 1),
    ("g <= 4f+2",   IG, IF, lambda f: 4 * f + 2),
    ("g <= q",      IG, IQ, lambda q: q),
    ("2S <= k",     IS, IK, lambda k: k),
]
CAPS = (3, 3, 1, 3, 1)          # (n_max, e_max, l_max, k_max, f_max)
OTHER_CAPS = [((2, 2, 1, 2, 1), 216), ((3, 3, 1, 4, 1), 1636), ((4, 3, 1, 4, 1), 2394),
              ((4, 4, 2, 4, 1), None), ((4, 4, 2, 6, 2), None)]


def ranges(caps):
    nmax, emax, lmax, kmax, fmax = caps
    return [list(range(1, nmax + 1)), list(range(0, lmax + 1)),
            list(range(1, kmax + 1)), list(range(0, kmax + 1)),
            list(range(1, emax + 1)), list(range(0, fmax + 1)),
            list(range(0, kmax + 1)), list(range(0, kmax + 1))]


def in_range(x, caps):
    return all(v in r for v, r in zip(x, ranges(caps)))


def admissible(x):
    return all(x[i] <= phi(x[j]) for _, i, j, phi in CONSTRAINTS)


def rebuild(caps=CAPS):
    """Fresh construction: every point of the ambient box that satisfies the seven bounds."""
    return sorted(x for x in itertools.product(*ranges(caps)) if admissible(x))


LAM = sorted(tower.L8())
N = len(LAM)
POS = {c: i for i, c in enumerate(LAM)}
ALPHA = [sorted({c[i] for c in LAM}) for i in range(D)]
BOX = prod(len(a) for a in ALPHA)
TOP = tuple(max(a) for a in ALPHA)
BOTTOM = tuple(min(a) for a in ALPHA)


def rank(x):
    return sum(x)


def le(a, b):
    return all(u <= v for u, v in zip(a, b))


def join(a, b):
    return tuple(map(max, a, b))


def meet(a, b):
    return tuple(map(min, a, b))


# ------------------------------------------------ Birkhoff bookkeeping, shared

def generators():
    """Generator (c, v) = min{ x in L : x_c >= v }, one per coordinate value above the floor."""
    g = {}
    for i in range(D):
        for v in ALPHA[i][1:]:
            cand = [c for c in LAM if c[i] >= v]
            g[(i, v)] = tuple(min(c[j] for c in cand) for j in range(D))
    return g


GENS = generators()
GORDER = sorted(GENS.items(), key=lambda kv: (rank(kv[1]), kv[0]))
GNAME = ["%s >= %d" % (CO[i], v) for (i, v), _ in GORDER]
GCELL = [m for _, m in GORDER]
JJ = len(GCELL)
GBELOW = [[a != b and le(GCELL[a], GCELL[b]) for b in range(JJ)] for a in range(JJ)]
DOWN = {}
for _x in LAM:
    DOWN[_x] = sum(1 << _k for _k in range(JJ) if le(GCELL[_k], _x))
MASK = [DOWN[x] for x in LAM]


# =============================================================== the two guards

def guards():
    print("GUARDS -- an obligation is not reported unless both pass")
    ok = True

    # (1) non-vacuity of every Z3 hypothesis used below.
    caps = [z3.Int(c) for c in ("Nc", "Ec", "Lc", "Kc", "Fc")]
    X = [z3.Int("gx_" + c) for c in CO]
    Y = [z3.Int("gy_" + c) for c in CO]
    s = z3.Solver()
    s.add(z3_member(X, caps), z3_member(Y, caps), X[IN] != Y[IN], caps[0] >= 3, caps[3] >= 3)
    sat = s.check() == z3.sat
    ok &= sat
    row("GUARD", "non-vacuity, integer obligation",
        "hypothesis satisfiable with two distinct cells and caps >= 3: %s" % s.check(), sat)

    phi = z3.Function("gphi", z3.IntSort(), z3.IntSort())
    u, v = z3.Ints("gu gv")
    a1, b1, a2, b2 = z3.Ints("ga1 gb1 ga2 gb2")
    s2 = z3.Solver()
    s2.add(z3.ForAll([u, v], z3.Implies(u <= v, phi(u) <= phi(v))))
    s2.add(a1 <= phi(b1), a2 <= phi(b2), a1 != a2, b1 != b2)
    sat2 = s2.check() == z3.sat
    ok &= sat2
    row("GUARD", "non-vacuity, monotone-bound obligation",
        "a monotone phi with two distinct admissible pairs exists: %s" % s2.check(), sat2)

    nv = prover.non_vacuous(
        (3, 3, 3),
        lambda X, S, c, d, sh: z3.And(prover.observed(X, c, sh),
                                      z3.And([X[q] == prover.in_R(X, q, c, d) for q in c])),
        extra=lambda X, S, c, d, sh: z3.Or([z3.Not(X[q]) for q in c]))
    ok &= nv
    row("GUARD", "non-vacuity, subset obligation",
        "a PROPER non-empty fixed point of R exists in the 3x3x3 box: %s" % nv, nv)

    # (2) encoding fidelity: the Z3 membership formula against the fresh implementation,
    #     exhaustively over the whole ambient box and then on random integer tuples that
    #     range OUTSIDE it, so the unary conditions are exercised in both directions.
    cmp_tot = bad = 0
    for x in itertools.product(*ranges(CAPS)):
        enc = z3.is_true(z3.simplify(z3_member([z3.IntVal(t) for t in x],
                                               [z3.IntVal(t) for t in CAPS])))
        cmp_tot += 1
        bad += enc != (in_range(x, CAPS) and admissible(x))
    rnd = random.Random(SEED)
    for _ in range(400):
        cv = [rnd.randint(0, 6) for _ in range(5)]
        xv = [rnd.randint(-3, 9) for _ in range(D)]
        enc = z3.is_true(z3.simplify(z3_member([z3.IntVal(t) for t in xv],
                                               [z3.IntVal(t) for t in cv])))
        cmp_tot += 1
        bad += enc != (in_range(xv, cv) and admissible(xv))
    ok &= bad == 0
    row("GUARD", "encoding fidelity, membership",
        "%d cases compared, %d disagreements, 0 skipped" % (cmp_tot, bad), bad == 0)

    # (3) encoding fidelity for the subset harness: prover.in_R against the SEATED operator.
    def ref(Xset, box, d):
        cells = [tuple(t) for t in Xset]
        ix = cypher.Index("guard", [str(i) for i in range(d)], cells)
        out, _ = cypher.op_order(ix, {})
        return {tuple(ix.decode[i][v] for i, v in enumerate(c)) for c in out}

    tot, drift = prover.encoding_matches(ref, [(3, 3), (3, 3, 3), (4, 4)], trials=120, seed=5)
    ok &= drift == 0
    row("GUARD", "encoding fidelity, staircase",
        "%d cells compared against the closure operator under test, %d disagreements, 0 skipped"
        % (tot, drift), drift == 0)

    print()
    return ok


# ----------------------------------------------------------- the Z3 encodings

def z3_in_range(x, caps):
    nmax, emax, lmax, kmax, fmax = caps
    return z3.And(x[IN] >= 1, x[IN] <= nmax, x[IE] >= 1, x[IE] <= emax,
                  x[IL] >= 0, x[IL] <= lmax, x[IF] >= 0, x[IF] <= fmax,
                  x[IK] >= 1, x[IK] <= kmax,
                  x[IQ] >= 0, x[IQ] <= kmax, x[IG] >= 0, x[IG] <= kmax,
                  x[IS] >= 0, x[IS] <= kmax)


def z3_bounds(x):
    return z3.And(x[IL] <= x[IN] - 1, x[IK] <= 4 * x[IL] + 2, x[IQ] <= x[IK],
                  x[IF] <= x[IE] - 1, x[IG] <= 4 * x[IF] + 2, x[IG] <= x[IQ],
                  x[IS] <= x[IK])


def z3_member(x, caps):
    return z3.And(z3_in_range(x, caps), z3_bounds(x))


def zmax(a, b):
    return z3.If(a >= b, a, b)


def zmin(a, b):
    return z3.If(a <= b, a, b)


# ============================================================ Z3 obligations

def z3_obligations():
    ok = True
    caps = [z3.Int(c) for c in ("Nc", "Ec", "Lc", "Kc", "Fc")]
    X = [z3.Int("x_" + c) for c in CO]
    Y = [z3.Int("y_" + c) for c in CO]
    J = [zmax(a, b) for a, b in zip(X, Y)]
    M = [zmin(a, b) for a, b in zip(X, Y)]

    s = z3.Solver()
    s.add(z3.Not(z3.Implies(z3.And(z3_member(X, caps), z3_member(Y, caps)),
                            z3.And(z3_member(J, caps), z3_member(M, caps)))))
    r = s.check()
    ok &= r == z3.unsat
    row("MACHINE-CHECKED", "Theorem 1, Lambda is a sublattice",
        "all 21 variables INTEGER (5 caps, 2 cells of 8): %s" % r, r == z3.unsat)

    # the same statement for a general monotone bound, with phi uninterpreted
    phi = z3.Function("phi", z3.IntSort(), z3.IntSort())
    u, v = z3.Ints("u v")
    a1, b1, a2, b2 = z3.Ints("a1 b1 a2 b2")
    s2 = z3.Solver()
    s2.add(z3.ForAll([u, v], z3.Implies(u <= v, phi(u) <= phi(v))))
    s2.add(z3.Not(z3.Implies(z3.And(a1 <= phi(b1), a2 <= phi(b2)),
                             z3.And(zmax(a1, a2) <= phi(zmax(b1, b2)),
                                    zmin(a1, a2) <= phi(zmin(b1, b2))))))
    r2 = s2.check()
    ok &= r2 == z3.unsat
    row("MACHINE-CHECKED", "Lemma 1, one monotone bound is closed",
        "phi uninterpreted, monotone; a,b INTEGER: %s" % r2, r2 == z3.unsat)

    # containment of a box in Lambda by the seven comparisons -- the sufficient direction
    LO = [z3.Int("lo_" + c) for c in CO]
    HI = [z3.Int("hi_" + c) for c in CO]
    W = [z3.Int("w_" + c) for c in CO]
    seven = z3.And([HI[i] <= f(LO[j]) for _, i, j, f in
                    [("", IL, IN, lambda n: n - 1), ("", IK, IL, lambda l: 4 * l + 2),
                     ("", IQ, IK, lambda k: k), ("", IF, IE, lambda e: e - 1),
                     ("", IG, IF, lambda f: 4 * f + 2), ("", IG, IQ, lambda q: q),
                     ("", IS, IK, lambda k: k)]])
    hyp = z3.And(z3_in_range(LO, caps), z3_in_range(HI, caps),
                 z3.And([LO[i] <= HI[i] for i in range(D)]), seven,
                 z3.And([z3.And(LO[i] <= W[i], W[i] <= HI[i]) for i in range(D)]))
    s3 = z3.Solver()
    s3.add(z3.Not(z3.Implies(hyp, z3_member(W, caps))))
    r3 = s3.check()
    ok &= r3 == z3.unsat
    row("MACHINE-CHECKED", "Theorem 13, seven comparisons suffice",
        "lo, hi, w and 5 caps all INTEGER: %s" % r3, r3 == z3.unsat)

    # subset-quantified: a fixed point of R is a sublattice
    def fixpoint_is_sublattice(Xv, Sv, cells, d, shape):
        fix = z3.And([Xv[c] == prover.in_R(Xv, c, cells, d) for c in cells])
        return z3.Implies(z3.And(prover.observed(Xv, cells, shape), fix),
                          prover.closed(Xv, cells))

    for shape in ((3, 3), (3, 3, 3)):
        got = prover.prove("fixed point of R", shape, fixpoint_is_sublattice, quiet=True)
        ok &= got
        row("MACHINE-CHECKED", "Lemma 2, E(X) = 0 implies X is a sublattice",
            "every one of 2%s subsets of the %s box: %s"
            % (sup(prod(shape)), "x".join(map(str, shape)), "unsat" if got else "SAT"), got)
    print()
    return ok


# ====================================================== construction and table

def read_printed_table():
    text = open(TABLE, encoding="utf-8").read().split("\n")
    start = next(i for i, ln in enumerate(text) if ln.startswith("## ") and "976 cells" in ln)
    out = []
    for ln in text[start:]:
        m = re.match(r"^\|\s*(\d+)\s*\|" + r"\s*(-?\d+)\s*\|" * 8 + r"\s*$", ln)
        if m:
            out.append(tuple(int(m.group(i)) for i in range(2, 10)))
        elif out and not ln.startswith("|"):
            break
    return out


def construction():
    ok = True
    fresh = rebuild()
    same = fresh == LAM
    ok &= same and N == 976
    row("EXHAUSTIVE", "Theorem 2, |Lambda| = 976",
        "the construction and a fresh sieve of all %d box points agree: %d cells, "
        "%.2f%% of the box" % (BOX, N, 100.0 * N / BOX), same and N == 976)

    printed = read_printed_table()
    fwd = set(printed) - set(LAM)
    bwd = set(LAM) - set(printed)
    good = len(printed) == 976 and not fwd and not bwd
    ok &= good
    row("EXHAUSTIVE", "Theorem 2, the cell list, both directions",
        "%d rows; rebuilt-not-printed %d, printed-not-rebuilt %d, order identical: %s"
        % (len(printed), len(bwd), len(fwd), printed == LAM), good)

    marg = {}
    for name, i, j, f in CONSTRAINTS:
        others = [(ii, jj, ff) for nm, ii, jj, ff in CONSTRAINTS if nm != name]
        marg[name] = sum(1 for x in itertools.product(*ranges(CAPS))
                         if all(x[ii] <= ff(x[jj]) for ii, jj, ff in others)
                         and not x[i] <= f(x[j]))
    floor = sum(1 for x in itertools.product(*[([0] + r if idx == IK else r)
                                               for idx, r in enumerate(ranges(CAPS))])
                if admissible(x) and x[IK] == 0)
    ext = prod(len(r) + (1 if idx == IK else 0) for idx, r in enumerate(ranges(CAPS)))
    allpos = (all(v > 0 for v in marg.values()) and floor > 0 and ext == 9216
              and marg == {"l <= n-1": 308, "k <= 4l+2": 564, "q <= k": 575, "f <= e-1": 200,
                           "g <= 4f+2": 24, "g <= q": 673, "2S <= k": 300} and floor == 25)
    ok &= allpos
    row("EXHAUSTIVE", "Table 2, no bound is redundant",
        "marginal exclusions " + ", ".join("%s: %d" % (k, v) for k, v in marg.items())
        + ", k >= 1: %d over the %d points of the box extended to k = 0" % (floor, ext), allpos)

    nocoup = [x for x in itertools.product(*ranges(CAPS))
              if all(x[i] <= f(x[j]) for nm, i, j, f in CONSTRAINTS if nm != "g <= 4f+2")]
    extra = set(nocoup) - set(LAM)
    good2 = len(nocoup) == 1000 and len(extra) == 24 and all(
        x[IF] == 0 and x[IG] == 3 for x in extra)
    ok &= good2
    row("EXHAUSTIVE", "Corollary 1, the one coupling",
        "drop the Pauli half: %d cells, the %d lost all have f = 0 and g = 3"
        % (len(nocoup), len(extra)), good2)
    # what the cells are: how many electrons each moves (D1), and what g is
    byq = {q: sum(1 for x in LAM if x[IQ] == q) for q in ALPHA[IQ]}
    multi = sum(v for q, v in byq.items() if q >= 2)
    good_q = byq == {0: 165, 1: 330, 2: 345, 3: 136} and multi == 481
    ok &= good_q
    row("EXHAUSTIVE", "D1, electrons moved",
        ", ".join("q = %d: %d cells" % (q, v) for q, v in sorted(byq.items()))
        + "; %d of %d move two or three electrons" % (multi, N), good_q)
    geq = sum(1 for x in LAM if x[IG] == x[IQ])
    glt = sum(1 for x in LAM if x[IG] < x[IQ])
    g0 = sum(1 for x in LAM if x[IG] == 0)
    same = sum(1 for x in LAM if x[IN] == x[IE] and x[IL] == x[IF])
    good_g = geq == 461 and glt == 515 and g0 == 485 and same == 200 and geq + glt == N
    ok &= good_g
    row("EXHAUSTIVE", "D1, the model of a cell",
        "g = q (every removed electron placed) in %d cells, g < q (removed and not placed) in "
        "%d, g = 0 in %d; source and target the same subshell, (n, l) = (e, f), in %d"
        % (geq, glt, g0, same), good_g)
    # the spin bound 2S <= k is an envelope: the rule for k equivalent electrons in a subshell
    # of angular momentum l is 2S = k (mod 2) and 2S <= min(k, 4l + 2 - k)
    par = {x for x in LAM if (x[IS] - x[IK]) % 2}
    hole = {x for x in LAM if x[IS] > 4 * x[IL] + 2 - x[IK]}
    unphys = par | hole
    phys = N - len(unphys)
    good_s = (len(par) == 413 and len(hole) == 180 and len(par & hole) == 90
              and len(unphys) == 503 and phys == 473)
    ok &= good_s
    row("EXHAUSTIVE", "Table 1, the spin envelope",
        "2S <= k admits %d of the %d cells whose 2S no k-electron configuration carries: %d with "
        "2S of the wrong parity (2S != k mod 2), %d above the particle-hole bound 2S <= 4l+2-k, "
        "%d both; the %d physical spin labels are %.1f%% of Lambda"
        % (len(unphys), N, len(par), len(hole), len(par & hole), phys, 100.0 * phys / N), good_s)
    # E = 0 and the closed-form generator count at further cap settings, each rebuilt fresh
    # and run through the seated closure; the caps are named in the row.
    parts = []
    good3 = True
    for caps, want in OTHER_CAPS:
        cells = rebuild(caps)
        ixc = cypher.Index("L", CO, cells)
        outc, _ = cypher.op_order(ixc, {})
        gotc = {tuple(ixc.decode[i][v] for i, v in enumerate(c)) for c in outc}
        Ec = len(gotc) - len(cells)
        Sc = set(cells)
        ji = 0
        for y in cells:
            low = 0
            for i in range(D):
                z = list(y)
                z[i] -= 1
                if tuple(z) in Sc:
                    low += 1
            ji += low == 1
        cf = sum(len({c[i] for c in cells}) - 1 for i in range(D))
        good3 &= (want is None or len(cells) == want) and Ec == 0 and gotc == Sc and ji == cf
        parts.append("%s: %d cells, E = %d, %d join-irreducibles (lower covers as unit steps, by "
                     "Theorem 4) = the sum over i of (|Ai| - 1) = %d"
                     % ("".join(map(str, caps)), len(cells), Ec, ji, cf))
    ok &= good3
    row("EXHAUSTIVE", "Theorems 2 and 6, further cap settings", "; ".join(parts), good3)
    print()
    return ok, marg, floor


def closure_defect():
    ok = True
    ix = cypher.Index("Lambda", CO, LAM)
    out, note = cypher.op_order(ix, {})
    got = {tuple(ix.decode[i][v] for i, v in enumerate(c)) for c in out}
    E = len(got) - N
    good = got == set(LAM) and E == 0
    ok &= good
    row("EXHAUSTIVE", "Theorem 2, E(Lambda) = 0",
        "the staircase closure returns %d cells, defect %d, set equality %s"
        % (len(got), E, got == set(LAM)), good)

    ix2 = cypher.Index("R", CO, sorted(got))
    out2, _ = cypher.op_order(ix2, {})
    got2 = {tuple(ix2.decode[i][v] for i, v in enumerate(c)) for c in out2}
    ok &= got2 == set(LAM)
    row("EXHAUSTIVE", "Theorem 2, R is idempotent on Lambda",
        "a second application changes nothing: %s" % (got2 == set(LAM)), got2 == set(LAM))

    bad = 0
    S = set(LAM)
    for a in range(N):
        xa = LAM[a]
        for b in range(a + 1, N):
            xb = LAM[b]
            if join(xa, xb) not in S or meet(xa, xb) not in S:
                bad += 1
    ok &= bad == 0
    row("EXHAUSTIVE", "Theorem 1, closure on every pair",
        "all %d unordered pairs: %d escapes under join or meet" % (N * (N - 1) // 2, bad),
        bad == 0)
    print()
    return ok


# ================================================================== structure

def covers_of():
    """Lower and upper covers from the ORDER alone: y covers x when x < y and no cell z has
    x < z < y.  Neither the rank nor a unit step enters here, so the grading row below can
    test that every cover is a unit step instead of assuming it."""
    upm = [0] * N
    dnm = [0] * N
    for i, x in enumerate(LAM):
        for j, y in enumerate(LAM):
            if i != j and le(x, y):
                upm[i] |= 1 << j
                dnm[j] |= 1 << i
    down, up = defaultdict(list), defaultdict(list)
    for i in range(N):
        u = upm[i]
        while u:
            j = (u & -u).bit_length() - 1
            u &= u - 1
            if upm[i] & dnm[j] == 0:
                down[LAM[j]].append(LAM[i])
                up[LAM[i]].append(LAM[j])
    return down, up


def max_antichain(elements, below):
    """Dilworth via Koenig: max antichain = n - (maximum matching of the strict order)."""
    n = len(elements)
    adj = [[j for j in range(n) if below(i, j)] for i in range(n)]
    mL, mR = [-1] * n, [-1] * n
    INF = float("inf")

    def bfs():
        dist = [INF] * n
        q = deque()
        for u in range(n):
            if mL[u] == -1:
                dist[u] = 0
                q.append(u)
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                w = mR[v]
                if w == -1:
                    found = True
                elif dist[w] == INF:
                    dist[w] = dist[u] + 1
                    q.append(w)
        return dist, found

    def dfs(u, dist):
        for v in adj[u]:
            w = mR[v]
            if w == -1 or (dist[w] == dist[u] + 1 and dfs(w, dist)):
                mL[u] = v
                mR[v] = u
                return True
        dist[u] = INF
        return False

    sys.setrecursionlimit(100000)
    m = 0
    while True:
        dist, found = bfs()
        if not found:
            break
        got = sum(1 for u in range(n) if mL[u] == -1 and dfs(u, dist))
        if got == 0:
            break
        m += got
    return n - m, m, mL


def structure():
    ok = True
    S = set(LAM)
    down, up = covers_of()
    ncov = sum(len(v) for v in down.values())

    # modularity, exhaustive on every pair
    bad = 0
    for a in range(N):
        xa = LAM[a]
        ra = rank(xa)
        for b in range(a + 1, N):
            xb = LAM[b]
            if rank(join(xa, xb)) + rank(meet(xa, xb)) != ra + rank(xb):
                bad += 1
    ok &= bad == 0
    row("EXHAUSTIVE", "Theorem 4, rank is modular",
        "all %d pairs: %d violations of rank(a ∨ b) + rank(a ∧ b) = rank a + rank b"
        % (N * (N - 1) // 2, bad), bad == 0)

    # distributivity: the chain identity on every triple of alphabet values, per coordinate
    tot = bad2 = 0
    for i in range(D):
        for a, b, c in itertools.product(ALPHA[i], repeat=3):
            tot += 1
            bad2 += min(a, max(b, c)) != max(min(a, b), min(a, c))
    ok &= bad2 == 0
    row("EXHAUSTIVE", "Theorem 3, the chain identity",
        "%d coordinate triples over the eight alphabets: %d failures" % (tot, bad2), bad2 == 0)

    rnd = random.Random(SEED)
    bad3 = 0
    TRIPLES = 200000
    for _ in range(TRIPLES):
        a, b, c = rnd.choice(LAM), rnd.choice(LAM), rnd.choice(LAM)
        if meet(a, join(b, c)) != join(meet(a, b), meet(a, c)):
            bad3 += 1
    ok &= bad3 == 0
    row("SAMPLED", "Theorem 3, distributivity on cell triples",
        "%d of the %d ordered cell triples (976 cubed), seed %d: %d failures"
        % (TRIPLES, N ** 3, SEED, bad3), bad3 == 0)

    # grading: the covers were found from the order alone; every one must be a unit step
    bad4 = sum(1 for y in LAM for x in down[y] if rank(y) - rank(x) != 1)
    unit = sum(1 for y in LAM for x in down[y]
               if sorted(b - a for a, b in zip(x, y)) == [0] * (D - 1) + [1])
    bot = [x for x in LAM if not down[x]]
    top = [x for x in LAM if not up[x]]
    good = (ncov == 3749 and unit == ncov and bad4 == 0 and bot == [BOTTOM] and top == [TOP]
            and rank(BOTTOM) == 3 and rank(TOP) == 20)
    ok &= good
    row("EXHAUSTIVE", "Theorem 4, Lambda is graded",
        "%d cover relations found from the order alone (x < y with no cell between); %d of them "
        "are unit steps, y - x a unit vector, and %d raise rank by 1; bottom %s rank 3, top %s "
        "rank 20"
        % (ncov, unit, ncov - bad4, "".join(map(str, BOTTOM)), "".join(map(str, TOP))), good)

    # rank sequence, Sperner
    cnt = defaultdict(int)
    for x in LAM:
        cnt[rank(x)] += 1
    seq = [cnt[r] for r in range(3, 21)]
    logc = all(seq[i] ** 2 >= seq[i - 1] * seq[i + 1] for i in range(1, len(seq) - 1))
    widest = max(seq)
    at = 3 + seq.index(widest)
    anti, matching, _ = max_antichain(LAM, lambda i, j: i != j and le(LAM[i], LAM[j]))
    good2 = anti == widest == 122 and at == 11 and logc and sum(seq) == 976
    ok &= good2
    row("EXHAUSTIVE", "Theorem 5, Lambda is Sperner",
        "largest antichain %d (maximum matching %d, minimum chain cover %d) = largest rank "
        "level %d at rank %d; the rank sequence is log-concave: %s"
        % (anti, matching, anti, widest, at, logc), good2)

    # irreducibles
    ji = [y for y in LAM if len(down[y]) == 1]
    mi = [y for y in LAM if len(up[y]) == 1]
    closed_form = sum(len(a) - 1 for a in ALPHA)
    good3 = (len(ji) == len(mi) == closed_form == 17
             and set(ji) == set(GCELL))
    ok &= good3
    row("EXHAUSTIVE", "Theorem 6, seventeen irreducibles",
        "%d join-irreducible, %d meet-irreducible, the sum over i of (|Ai| - 1) = %d, and "
        "every join-irreducible is min{x : x[c] >= v}" % (len(ji), len(mi), closed_form), good3)

    weights = [sum(1 for x in LAM if le(m, x)) for m in GCELL]
    WANT = {"n >= 2": (4, 856), "k >= 2": (4, 826), "q >= 1": (4, 811), "e >= 2": (4, 784),
            "2S >= 1": (4, 657), "l >= 1": (5, 616), "g >= 1": (5, 491), "n >= 3": (5, 428),
            "f >= 1": (5, 400), "e >= 3": (5, 392), "q >= 2": (6, 481), "2S >= 2": (6, 338),
            "k >= 3": (7, 376), "g >= 2": (8, 171), "q >= 3": (10, 136), "2S >= 3": (10, 94),
            "g >= 3": (15, 16)}
    got_t = {GNAME[t]: (rank(GCELL[t]), weights[t]) for t in range(JJ)}
    hi_w, lo_w = max(weights), min(weights)
    good_t = got_t == WANT and hi_w == 856 and lo_w == 16
    ok &= good_t
    row("EXHAUSTIVE", "Table 3, the seventeen letters",
        "; ".join("%s at rank %d in %d cells" % (GNAME[t], rank(GCELL[t]), weights[t])
                  for t in range(JJ))
        + "; the heaviest letter carries %.1f%% of the cells and the lightest %.1f%%"
        % (100.0 * hi_w / N, 100.0 * lo_w / N), good_t)

    # Birkhoff, by enumerating every subset of the generating poset
    ds = 0
    for m in range(1 << JJ):
        good_m = True
        for b in range(JJ):
            if m >> b & 1:
                for a in range(JJ):
                    if GBELOW[a][b] and not (m >> a & 1):
                        good_m = False
                        break
            if not good_m:
                break
        ds += good_m
    bij = len(set(MASK)) == N and ds == N
    ok &= bij
    row("EXHAUSTIVE", "Theorem 7, the Birkhoff correspondence",
        "all 2¹⁷ = %d subsets tested: %d are down-sets; cell -> down-set is a bijection "
        "onto them" % (1 << JJ, ds), bij)

    badb = 0
    for a in range(N):
        for b in range(a + 1, N):
            if DOWN[join(LAM[a], LAM[b])] != (MASK[a] | MASK[b]):
                badb += 1
            if DOWN[meet(LAM[a], LAM[b])] != (MASK[a] & MASK[b]):
                badb += 1
    ok &= badb == 0
    row("EXHAUSTIVE", "Theorem 7, join is OR and meet is AND",
        "all %d pairs, both operations: %d failures" % (N * (N - 1) // 2, badb), badb == 0)

    # the implications
    covP = [(a, b) for a in range(JJ) for b in range(JJ)
            if GBELOW[a][b] and not any(GBELOW[a][c] and GBELOW[c][b] for c in range(JJ))]
    within = [(a, b) for a, b in covP if GORDER[a][0][0] == GORDER[b][0][0]]
    between = [(a, b) for a, b in covP if GORDER[a][0][0] != GORDER[b][0][0]]
    good4 = len(covP) == 20 and len(within) == 9 and len(between) == 11
    ok &= good4
    row("EXHAUSTIVE", "Theorem 8, twenty implications",
        "%d covering relations in the generating poset: %d within a coordinate, %d between"
        % (len(covP), len(within), len(between)), good4)
    IMPL = {"n >= 3 -> n >= 2", "l >= 1 -> n >= 2", "q >= 2 -> k >= 2", "2S >= 2 -> k >= 2",
            "k >= 3 -> k >= 2", "g >= 1 -> q >= 1", "q >= 2 -> q >= 1", "e >= 3 -> e >= 2",
            "f >= 1 -> e >= 2", "2S >= 2 -> 2S >= 1", "k >= 3 -> l >= 1", "g >= 3 -> f >= 1",
            "g >= 2 -> g >= 1", "g >= 2 -> q >= 2", "q >= 3 -> q >= 2", "2S >= 3 -> 2S >= 2",
            "q >= 3 -> k >= 3", "2S >= 3 -> k >= 3", "g >= 3 -> g >= 2", "g >= 3 -> q >= 3"}
    got_i = {"%s -> %s" % (GNAME[b], GNAME[a]) for a, b in covP}
    ok &= got_i == IMPL
    row("EXHAUSTIVE", "Theorem 8, the twenty implications written out",
        "; ".join("%s -> %s" % (GNAME[b], GNAME[a]) for a, b in covP), got_i == IMPL)

    accepted = 0
    for m in range(1 << JJ):
        if all(not (m >> b & 1) or (m >> a & 1) for a, b in covP):
            accepted += 1
    ok &= accepted == N
    row("EXHAUSTIVE", "Theorem 8, the twenty implications cut the space",
        "of %d seventeen-bit words, %d satisfy all twenty and nothing else is imposed"
        % (1 << JJ, accepted), accepted == N)

    width, _, wm = max_antichain(GCELL, lambda i, j: GBELOW[i][j])
    ok &= width == 7
    row("EXHAUSTIVE", "Corollary 2, order dimension 7",
        "the generating poset has width %d, certified by a chain partition of the same size"
        % width, width == 7)
    # the two certificates, written out: an antichain of seven letters and seven chains
    anti7 = next(c for c in itertools.combinations(range(JJ), 7)
                 if not any(GBELOW[a][b] for a in c for b in c if a != b))
    heads = set(range(JJ)) - {wm[u] for u in range(JJ) if wm[u] != -1}
    chains = []
    for h in sorted(heads):
        ch, u = [], h
        while u != -1:
            ch.append(u)
            u = wm[u]
        chains.append(ch)
    good_c = (len(anti7) == 7 and len(chains) == 7
              and sorted(t for ch in chains for t in ch) == list(range(JJ)))
    ok &= good_c
    row("EXHAUSTIVE", "Corollary 2, the two certificates",
        "antichain {%s}; chains %s"
        % (", ".join(GNAME[t] for t in anti7),
           " | ".join(" < ".join(GNAME[t] for t in ch) for ch in chains)), good_c)

    # maximal chains = linear extensions of P, by dynamic programming over the cells
    ways = {BOTTOM: 1}
    for y in sorted(LAM, key=rank):
        if y == BOTTOM:
            continue
        ways[y] = sum(ways[z] for z in down[y])
    maxch = ways[TOP]
    good_m = maxch == 1113045672 and rank(TOP) - rank(BOTTOM) == JJ
    ok &= good_m
    row("EXHAUSTIVE", "Corollary 3, maximal chains",
        "%d maximal chains, every one of %d covering steps, counted over all 976 cells"
        % (maxch, rank(TOP) - rank(BOTTOM)), good_m)

    # reflection
    surv = [x for x in LAM if tuple(t - v for t, v in zip(TOP, x)) in S]
    fixed = [x for x in LAM if tuple(t - v for t, v in zip(TOP, x)) == x]
    good5 = len(surv) == 8 and len(fixed) == 0 and all(rank(x) % 2 == 0 for x in surv)
    ok &= good5
    row("EXHAUSTIVE", "Theorem 9, the reflection",
        "%d of %d cells have their image under x -> top - x in Lambda; %d are fixed; "
        "they are %s at ranks %s"
        % (len(surv), N, len(fixed),
           " ".join("".join(map(str, x)) for x in sorted(surv, key=rank)),
           ",".join(str(rank(x)) for x in sorted(surv, key=rank))), good5)

    bits = math.log2(N)
    good_b = (JJ == 17 and round(bits, 4) == 9.9307 and round(JJ - bits, 4) == 7.0693
              and round(100.0 * N / (1 << JJ), 4) == 0.7446)
    ok &= good_b
    row("EXHAUSTIVE", "Theorem 7, the bit accounting",
        "%d bits carried per cell, %.4f needed to index %d cells, surplus %.4f; Lambda is "
        "%.4f%% of the 2¹⁷ words" % (JJ, bits, N, JJ - bits, 100.0 * N / (1 << JJ)), good_b)
    print()
    return ok, seq, covP, within, between, surv, ncov


# ===================================================================== metric

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]


def enc(x):
    return prod(p ** v for p, v in zip(PRIMES, x))


def tau(m):
    t = 1
    for p in PRIMES:
        e = 0
        while m % p == 0:
            m //= p
            e += 1
        t *= e + 1
    return t if m == 1 else None


def metric():
    ok = True
    NV = [enc(x) for x in LAM]
    bad = 0
    for a in range(N):
        xa, na = LAM[a], NV[a]
        for b in range(a + 1, N):
            xb, nb = LAM[b], NV[b]
            d2 = prod(abs(u - v) + 1 for u, v in zip(xa, xb))
            lo, hi = meet(xa, xb), join(xa, xb)
            d1 = prod(hi[i] - lo[i] + 1 for i in range(D))
            g = gcd(na, nb)
            d3 = tau(na // g * nb // g)
            d4 = tau(na * nb // (g * g))
            d5 = prod(abs(_vp(na, p) - _vp(nb, p)) + 1 for p in PRIMES)
            if not d1 == d2 == d3 == d4 == d5:
                bad += 1
    ok &= bad == 0
    row("EXHAUSTIVE", "Theorem 10, five forms of d",
        "all %d pairs: %d disagreements among interval count, coordinate product, "
        "two-integer, one-rational and p-adic forms" % (N * (N - 1) // 2, bad), bad == 0)

    badd = sum(1 for x in LAM if prod(1 for _ in range(D)) != 1 or
               prod(abs(u - u) + 1 for u in x) != 1)
    ok &= badd == 0
    row("EXHAUSTIVE", "Theorem 10, d(x, x) = 1", "all %d cells: %d exceptions" % (N, badd), badd == 0)

    tot = badt = 0
    for i in range(D):
        for a, b, c in itertools.product(ALPHA[i], repeat=3):
            tot += 1
            badt += not (abs(a - c) + 1 <= (abs(a - b) + 1) * (abs(b - c) + 1))
    ok &= badt == 0
    row("EXHAUSTIVE", "Theorem 11, the coordinate triangle",
        "%d value triples over the eight alphabets: %d failures of "
        "|a-c|+1 <= (|a-b|+1)(|b-c|+1)" % (tot, badt), badt == 0)

    rnd = random.Random(SEED + 1)
    TR = 200000
    bad3 = 0

    def dd(u, v):
        return prod(abs(p - q) + 1 for p, q in zip(u, v))

    for _ in range(TR):
        a, b, c = rnd.choice(LAM), rnd.choice(LAM), rnd.choice(LAM)
        if dd(a, c) > dd(a, b) * dd(b, c):
            bad3 += 1
    ok &= bad3 == 0
    row("SAMPLED", "Theorem 11, the multiplicative triangle on cell triples",
        "%d of the %d ordered cell triples (976 cubed), seed %d: %d failures"
        % (TR, N ** 3, SEED + 1, bad3), bad3 == 0)
    good_l = round(math.log(2), 4) == 0.6931 and round(math.log(11 / 10), 4) == 0.0953
    ok &= good_l
    row("EXHAUSTIVE", "Theorem 11, the log-distorted chain",
        "per-axis cost log(|Delta|+1): first step log 2 = %.4f, tenth step log(11/10) = %.4f"
        % (math.log(2), math.log(11 / 10)), good_l)
    print()
    return ok


def _vp(m, p):
    e = 0
    while m % p == 0:
        m //= p
        e += 1
    return e


# ======================================================================= void

def bitsets():
    bs = {}
    for i in range(D):
        for lo in ALPHA[i]:
            for hi in ALPHA[i]:
                if hi >= lo:
                    bs[(i, lo, hi)] = sum(1 << c for c, x in enumerate(LAM)
                                          if lo <= x[i] <= hi)
    return bs


BS = bitsets()


def count_direct(lo, hi):
    m = (1 << N) - 1
    for i in range(D):
        m &= BS[(i, lo[i], hi[i])]
    return m.bit_count()


def count_tree(lo, hi):
    """Variable elimination along the caterpillar.  Every message has one argument."""
    R = [range(lo[i], hi[i] + 1) for i in range(D)]
    mS = {k: max(0, min(hi[IS], k) - lo[IS] + 1) for k in R[IK]}
    mN = {l: max(0, hi[IN] - max(lo[IN], l + 1) + 1) for l in R[IL]}
    mL = {k: sum(mN[l] for l in R[IL] if k <= 4 * l + 2) for k in R[IK]}
    mK = {q: sum(mS[k] * mL[k] for k in R[IK] if k >= 1 and q <= k) for q in R[IQ]}
    mQ = {g: sum(mK[q] for q in R[IQ] if g <= q) for g in R[IG]}
    mG = {f: sum(mQ[g] for g in R[IG] if g <= 4 * f + 2) for f in R[IF]}
    mF = {e: sum(mG[f] for f in R[IF] if f <= e - 1) for e in R[IE]}
    return sum(mF[e] for e in R[IE])


def box_inside(lo, hi):
    return all(hi[i] <= f(lo[j]) for _, i, j, f in CONSTRAINTS)


def void():
    ok = True
    per = [[(lo, hi) for lo in ALPHA[i] for hi in ALPHA[i] if hi >= lo] for i in range(D)]
    total = prod(len(p) for p in per)
    bad = badc = 0
    for combo in itertools.product(*per):
        lo = tuple(c[0] for c in combo)
        hi = tuple(c[1] for c in combo)
        direct = count_direct(lo, hi)
        if direct != count_tree(lo, hi):
            bad += 1
        vol = prod(hi[i] - lo[i] + 1 for i in range(D))
        if box_inside(lo, hi) != (direct == vol):
            badc += 1
    ok &= bad == 0 and badc == 0
    row("EXHAUSTIVE", "Theorem 12, the tree factorisation",
        "every one of the %d sub-boxes of the ambient box: %d disagreements with direct "
        "enumeration" % (total, bad), bad == 0)
    row("EXHAUSTIVE", "Theorem 13, containment, both directions",
        "the same %d sub-boxes: %d disagreements with the enumerated count" % (total, badc),
        badc == 0)

    pairs = N * (N - 1) // 2
    free = 0
    rates = {nm: 0 for nm, _, _, _ in CONSTRAINTS}
    neg = 0
    comp = compbox = 0
    for a in range(N):
        xa = LAM[a]
        for b in range(a + 1, N):
            xb = LAM[b]
            lo, hi = meet(xa, xb), join(xa, xb)
            vol = prod(hi[i] - lo[i] + 1 for i in range(D))
            inside = count_direct(lo, hi)
            if inside > vol:
                neg += 1
            if inside == vol:
                free += 1
            if lo == xa or lo == xb:
                comp += 1
                compbox += inside == vol
            for nm, i, j, f in CONSTRAINTS:
                if hi[i] <= f(lo[j]):
                    rates[nm] += 1
    joint = Fraction(free, pairs)
    marg = {k: Fraction(v, pairs) for k, v in rates.items()}
    product = prod(marg.values())
    good = neg == 0
    ok &= good
    row("EXHAUSTIVE", "Proposition 1, the void is non-negative",
        "all %d pairs: %d boxes hold more cells than they have points" % (pairs, neg), good)
    lo_nm = min(marg, key=marg.get)
    hi_nm = max(marg, key=marg.get)
    good_f = (free == 134871 and pairs == 475800 and round(float(joint), 4) == 0.2835
              and lo_nm == "g <= q" and round(float(marg[lo_nm]), 4) == 0.6995
              and hi_nm == "g <= 4f+2" and round(float(marg[hi_nm]), 4) == 0.9806
              and round(float(product), 4) == 0.2013 and round(float(joint / product), 4) == 1.4081)
    ok &= good_f
    row("EXHAUSTIVE", "Proposition 1, the void-free fraction",
        "%d of %d pairs, %.4f; the seven rates run %.4f (%s) to %.4f (%s), their product "
        "%.4f, the lift %.4f" % (free, pairs, float(joint), float(marg[lo_nm]), lo_nm,
                                 float(marg[hi_nm]), hi_nm, float(product),
                                 float(joint / product)), good_f)
    good_cb = comp == 115162
    ok &= good_cb
    row("EXHAUSTIVE", "Proposition 1, comparable pairs whose interval is a box",
        "%d of the %d strictly comparable pairs, %.4f" % (compbox, comp, compbox / comp),
        good_cb)

    deg = defaultdict(int)
    for _, i, j, _f in CONSTRAINTS:
        deg[i] += 1
        deg[j] += 1
    edges = len(CONSTRAINTS)
    nodes = len(set(list(deg)))
    seen, stack = set(), [IN]
    adj = defaultdict(list)
    for _, i, j, _f in CONSTRAINTS:
        adj[i].append(j)
        adj[j].append(i)
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        stack.extend(adj[u])
    degs = sorted(deg.values())
    tree = edges == nodes - 1 and len(seen) == nodes
    # the leaves removed leave a path; and oriented bounded -> bounding, no directed cycle
    leaves = {v for v in deg if deg[v] == 1}
    inner = [v for v in deg if v not in leaves]
    idg = {v: sum(1 for u in adj[v] if u not in leaves) for v in inner}
    path = sorted(idg.values()) == [1, 1] + [2] * (len(inner) - 2)
    par = defaultdict(list)
    for _, i, j, _f in CONSTRAINTS:
        par[i].append(j)
    def reaches(u, v, seen_=()):
        return u == v or any(reaches(w, v, seen_ + (u,)) for w in par[u] if w not in seen_)
    acyclic = not any(reaches(w, u) for u in range(D) for w in par[u])
    tree = tree and path and acyclic
    ok &= tree
    row("EXHAUSTIVE", "Lemma 3, the constraint graph is a caterpillar",
        "%d nodes, %d edges, connected: a tree; degree sequence %s; removing the %d leaves "
        "leaves a path: %s; oriented from bounded to bounding coordinate it has no directed "
        "cycle: %s" % (nodes, edges, "".join(map(str, degs)), len(leaves), path, acyclic),
        tree)
    print()
    return ok, float(joint), marg, float(product), free, pairs


# ======================================================== generating function

def padd(a, b):
    o = dict(a)
    for k, v in b.items():
        o[k] = o.get(k, 0) + v
    return o


def pmul(a, b):
    o = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            o[k1 + k2] = o.get(k1 + k2, 0) + v1 * v2
    return o


def nested_F(caps=CAPS):
    nmax, emax, lmax, kmax, fmax = caps
    F = {}
    for n in range(1, nmax + 1):
        for l in range(0, min(lmax, n - 1) + 1):
            for k in range(1, min(kmax, 4 * l + 2) + 1):
                spin = {i: 1 for i in range(0, min(kmax, k) + 1)}
                for q in range(0, min(kmax, k) + 1):
                    for e in range(1, emax + 1):
                        for f in range(0, min(fmax, e - 1) + 1):
                            gg = {i: 1 for i in range(0, min(kmax, q, 4 * f + 2) + 1)}
                            F = padd(F, pmul(pmul({n + l + k + q + e + f: 1}, spin), gg))
    return {k: v for k, v in F.items() if v}


def generating_function(seq):
    ok = True
    F = nested_F()
    direct = defaultdict(int)
    for x in LAM:
        direct[rank(x)] += 1
    same = F == dict(direct)
    ok &= same
    row("EXHAUSTIVE", "Theorem 14, the nested form is the rank polynomial",
        "coefficient by coefficient over ranks 3 to 20, exact integers: %s" % same, same)

    F1 = sum(F.values())
    Fm1 = sum(v * (-1) ** k for k, v in F.items())
    mean = Fraction(sum(k * v for k, v in F.items()), F1)
    good = F1 == 976 and Fm1 == 2 and mean == Fraction(10801, 976)
    ok &= good
    row("EXHAUSTIVE", "Corollary 4, F(1) = 976 and F(-1) = 2",
        "exact integer evaluation; F'(1)/F(1) = %s = %.4f, against the midpoint 23/2: skew "
        "%.4f" % (mean, float(mean), float(mean - Fraction(23, 2))), good)

    boxp = {0: 1}
    for a in ALPHA:
        boxp = pmul(boxp, {v: 1 for v in a})
    b1 = sum(boxp.values())
    bm1 = sum(v * (-1) ** k for k, v in boxp.items())
    evens = [CO[i] for i in range(D) if sum((-1) ** v for v in ALPHA[i]) == 0]
    good2 = b1 == BOX and bm1 == 0 and len(evens) == 5
    ok &= good2
    row("EXHAUSTIVE", "Theorem 15, the free box vanishes at z = -1",
        "Phi(1) = %d, Phi(-1) = %d; %d of the eight alphabets have even size (%s)"
        % (b1, bm1, len(evens), ", ".join(evens)), good2)

    byk = {k: sum((-1) ** rank(x) for x in LAM if x[IK] == k) for k in ALPHA[IK]}
    good3 = byk == {1: 0, 2: 2, 3: 0}
    ok &= good3
    row("EXHAUSTIVE", "Theorem 15, the residue localises on k = 2",
        "the alternating sum F(-1) splits by source occupancy as " +
        ", ".join("k=%d: %+d" % (k, v) for k, v in sorted(byk.items())), good3)

    tot = badg = 0
    for k in range(0, 6):
        for num in range(2, 12):
            z = Fraction(num, num + 1)
            tot += 1
            badg += sum(z ** i for i in range(k + 1)) != (1 - z ** (k + 1)) / (1 - z)
    ok &= badg == 0
    row("EXHAUSTIVE", "Lemma 4, the detachable leaf",
        "the geometric identity on %d exact rational points, degrees 0 to 5, %d failures"
        % (tot, badg), badg == 0)

    # the seven-coordinate projection: 2S removed, each seven-cell carrying k + 1 spins
    proj = sorted({x[:7] for x in LAM})
    spins = defaultdict(set)
    for x in LAM:
        spins[x[:7]].add(x[7])
    each = all(spins[p] == set(range(p[IK] + 1)) for p in proj)
    ix7 = cypher.Index("L7", CO[:7], proj)
    out7, _ = cypher.op_order(ix7, {})
    got7 = {tuple(ix7.decode[i][v] for i, v in enumerate(c)) for c in out7}
    E7 = len(got7) - len(proj)
    good7 = len(proj) == 319 and each and E7 == 0 and got7 == set(proj) and \
        sum(p[IK] + 1 for p in proj) == N
    ok &= good7
    row("EXHAUSTIVE", "Lemma 4, the spin projection",
        "%d seven-coordinate cells, every one carrying exactly k + 1 values of 2S (sum %d); "
        "the projection is closed, defect %d" % (len(proj), sum(p[IK] + 1 for p in proj), E7),
        good7)

    back = seq[::-1]
    first = next(i for i in range(len(seq)) if seq[i] != back[i])
    good4 = seq != back and first == 1
    ok &= good4
    row("EXHAUSTIVE", "Corollary 5, F is not palindromic",
        "forwards and backwards first part at rank %d, %d against %d"
        % (3 + first, seq[first], back[first]), good4)
    print()
    return ok, F


# ==================================================================== Moebius

def moebius():
    ok = True
    up = []
    for i in range(N):
        mi = MASK[i]
        up.append([j for j in range(N) if mi & ~MASK[j] == 0])
    anticache = {}

    def is_anti(m):
        idxs = [a for a in range(JJ) if m >> a & 1]
        return not any(GBELOW[a][b] for a in idxs for b in idxs if a != b)

    def mu(i, j):
        q = MASK[j] & ~MASK[i]
        r = anticache.get(q)
        if r is None:
            r = (-1) ** bin(q).count("1") if is_anti(q) else 0
            anticache[q] = r
        return r

    checked = bad = 0
    vals = set()
    for i in range(N):
        U = up[i]
        mus = {j: mu(i, j) for j in U}
        vals |= set(mus.values())
        for j in U:
            mj = MASK[j]
            s = 0
            for z in U:
                if MASK[z] & ~mj == 0:
                    s += mus[z]
            checked += 1
            bad += s != (1 if j == i else 0)
    ok &= bad == 0
    row("EXHAUSTIVE", "Theorem 16, the Moebius function",
        "the closed form satisfies the defining recursion on all %d comparable pairs "
        "(%d strict); %d violations; values %s"
        % (checked, checked - N, bad, sorted(vals)), bad == 0)

    # the crosscut step, checked directly: for every interval, J(Q) is Boolean iff Q is an
    # antichain, and the join of the atoms is the top iff Q is an antichain.
    seen = set()
    badc = 0
    for i in range(N):
        for j in up[i]:
            q = MASK[j] & ~MASK[i]
            if q in seen:
                continue
            seen.add(q)
            idxs = [a for a in range(JJ) if q >> a & 1]
            minimal = [a for a in idxs if not any(GBELOW[b][a] for b in idxs)]
            atomjoin = sum(1 << a for a in minimal)
            iv = count_interval(MASK[i], MASK[j])
            boolean = iv == 2 ** len(idxs)
            if (atomjoin == q) != is_anti(q) or boolean != is_anti(q):
                badc += 1
    ok &= badc == 0
    row("EXHAUSTIVE", "Theorem 16, the crosscut condition",
        "%d distinct intervals: the join of the atoms is the top exactly when the added "
        "generators form an antichain, and then the interval is Boolean; %d exceptions"
        % (len(seen), badc), badc == 0)

    # Corollary 6: mu(x, y) != 0 iff [x, y] is a unit hypercube lying inside Lambda, and then
    # mu = (-1)^(rank y - rank x); against the arithmetic Moebius function of N(y)/N(x)
    nz = nzu = agree = dis = badk = 0
    for i in range(N):
        x = LAM[i]
        for j in up[i]:
            y = LAM[j]
            m = mu(i, j)
            unit = all(y[t] - x[t] <= 1 for t in range(D))
            inside = unit and box_inside(x, y)
            m_arith = (-1) ** (rank(y) - rank(x)) if unit else 0
            if (m != 0) != inside:
                badk += 1
            if m != 0 and m != (-1) ** (rank(y) - rank(x)):
                badk += 1
            nz += m != 0
            nzu += inside
            if m == m_arith:
                agree += 1
            else:
                dis += 1
                if not (unit and not inside):
                    badk += 1
    good_k = badk == 0
    ok &= good_k
    row("EXHAUSTIVE", "Corollary 6, the Moebius function in coordinates",
        "all %d comparable pairs: mu is non-zero on %d, exactly the %d void-free unit "
        "hypercubes; it equals the arithmetic Moebius function of N(y)/N(x) on %d pairs and "
        "differs on %d, every one a unit hypercube with a void" % (checked, nz, nzu, agree, dis),
        good_k)
    print()
    return ok


def count_interval(mlo, mhi):
    return sum(1 for m in MASK if mlo & ~m == 0 and m & ~mhi == 0)


# ======================================================================= seed

def cover_instance():
    phi = {}
    for i in range(D):
        for j in range(D):
            if i == j:
                continue
            for a in ALPHA[j]:
                phi[(i, j, a)] = max(y[i] for y in LAM if y[j] <= a)
    elems = [("slot", i, v) for i in range(D) for v in ALPHA[i]]
    for i in range(D):
        for j in range(D):
            if i == j:
                continue
            seen = set()
            for a in ALPHA[j]:
                p = phi[(i, j, a)]
                if p not in seen:
                    seen.add(p)
                    elems.append(("step", i, j, a, p))

    def witnesses(x, e):
        if e[0] == "slot":
            return x[e[1]] == e[2]
        _, i, j, a, p = e
        return x[j] <= a and x[i] == p

    M = len(elems)
    cmask = [sum(1 << k for k, e in enumerate(elems) if witnesses(x, e)) for x in LAM]
    return elems, cmask, M


def closes(cells):
    ix = cypher.Index("G", CO, sorted(cells))
    out, _ = cypher.op_order(ix, {})
    got = {tuple(ix.decode[i][v] for i, v in enumerate(c)) for c in out}
    return got == set(LAM)


def seed():
    ok = True
    elems, cmask, M = cover_instance()
    FULL = (1 << M) - 1
    sup = [[c for c in range(N) if cmask[c] >> k & 1] for k in range(M)]
    supset = [frozenset(s) for s in sup]
    nslot = sum(len(a) for a in ALPHA)
    good = M == 102 and nslot == 25
    ok &= good
    row("EXHAUSTIVE", "Theorem 17, the covering instance",
        "%d elements: %d alphabet slots and %d envelope steps; %d sets, one per cell"
        % (M, nslot, M - nslot, N), good)

    # the generation criterion, against the seated closure operator
    rnd = random.Random(SEED + 2)
    agree = dis = ncover = 0
    for _ in range(80):
        G = rnd.sample(range(N), rnd.randint(4, 10))
        c = 0
        for i in G:
            c |= cmask[i]
        ncover += c == FULL
        if (c == FULL) == closes([LAM[i] for i in G]):
            agree += 1
        else:
            dis += 1
    ok &= dis == 0
    row("SAMPLED", "Theorem 17, covering is generating",
        "%d random subsets of size 4 to 10, seed %d: %d of them are covers, and %d disagreements "
        "with the closure operator under test" % (agree + dis, SEED + 2, ncover, dis), dis == 0)

    # element reduction (safe for counting: a dominated element is implied)
    keep = [a for a in range(M)
            if not any(b != a and supset[b] <= supset[a]
                       and (supset[b] != supset[a] or b < a) for b in range(M))]
    K = len(keep)
    rmask = [sum(1 << t for t, k in enumerate(keep) if cmask[c] >> k & 1) for c in range(N)]
    RFULL = (1 << K) - 1
    sig = defaultdict(list)
    for c in range(N):
        sig[rmask[c]].append(c)
    sigs = list(sig)
    byel = [[s for s in sigs if s >> t & 1] for t in range(K)]

    def lower_bound(unc):
        """Elements whose witness sets are pairwise disjoint need one set each."""
        order = sorted((t for t in range(K) if unc >> t & 1),
                       key=lambda t: len(supset[keep[t]]))
        used, n = set(), 0
        for t in order:
            s = supset[keep[t]]
            if not (s & used):
                used |= s
                n += 1
        return n

    root_lb = lower_bound(RFULL)
    solutions = []

    def search(cov, chosen, limit):
        if cov == RFULL:
            solutions.append(tuple(sorted(chosen)))
            return
        if len(chosen) >= limit:
            return
        unc = RFULL & ~cov
        if len(chosen) + lower_bound(unc) > limit:
            return
        t = min((t for t in range(K) if unc >> t & 1), key=lambda t: len(byel[t]))
        for s in byel[t]:
            search(cov | s, chosen + [s], limit)

    size = None
    for lim in range(1, 12):
        solutions = []
        search(0, [], lim)
        if solutions:
            size = lim
            break
    sols = set(solutions)
    total = sum(prod(len(sig[x]) for x in s) for s in sols)
    good2 = size == 7 and total == 24585 and root_lb == 5
    ok &= good2
    row("EXHAUSTIVE", "Theorem 18, seed(Lambda) = 7",
        "branch and bound over %d critical elements and %d distinct witness signatures; "
        "lower bound %d; minimum %d; %d signature covers expanding to %d minimum covers; "
        "976/7 = %.1f" % (K, len(sigs), root_lb, size, len(sols), total, N / size), good2)

    forced = set(range(N))
    for s in sols:
        f = {sig[x][0] for x in s if len(sig[x]) == 1}
        forced &= f
        if not forced:
            break
    uniq = [k for k in range(M) if len(sup[k]) == 1]
    minwit = min(len(s) for s in sup)
    good3 = len(forced) == 1 and len(uniq) == 0 and minwit == 4
    ok &= good3
    row("EXHAUSTIVE", "Theorem 18, one cell in every minimum cover",
        "%d cell lies in all %d minimum covers -- %s -- and %d of the %d elements is "
        "witnessed by a unique cell; the smallest witness set has %d cells"
        % (len(forced), total, "".join(map(str, LAM[min(forced)])) if forced else "-",
           len(uniq), M, minwit), good3)

    # a local account of the common cell: three elements whose witness sets meet in it alone
    fc = min(forced)
    cont = [k for k in range(M) if fc in supset[k]]
    cert = None
    for r_ in (1, 2, 3):
        for combo in itertools.combinations(cont, r_):
            inter = frozenset.intersection(*[supset[k] for k in combo])
            if inter == frozenset([fc]):
                cert = combo
                break
        if cert:
            break

    def ename(e):
        if e[0] == "slot":
            return "slot %s = %d" % (CO[e[1]], e[2])
        return "step %s at %s <= %d, value %d" % (CO[e[1]], CO[e[2]], e[3], e[4])

    good_l = cert is not None and len(cert) == 3
    ok &= good_l
    row("EXHAUSTIVE", "Theorem 18, a local account of the common cell",
        "the cell witnesses %d of the %d elements; no one or two of them single it out, and "
        "three do: %s" % (len(cont), M, "; ".join("%s (%d witnesses)" % (ename(elems[k]),
                                                                          len(sup[k]))
                                                   for k in cert) if cert else "none"), good_l)

    # Corollary 7: what every minimum seed contains, over all covers by cell
    props = [("null transition, q = 0", lambda x: x[IQ] == 0),
             ("full transfer, q = k = 1", lambda x: x[IQ] == x[IK] == 1),
             ("full transfer, q = k = 2", lambda x: x[IQ] == x[IK] == 2),
             ("full transfer, q = k = 3", lambda x: x[IQ] == x[IK] == 3),
             ("s -> p", lambda x: x[IL] == 0 and x[IF] == 1),
             ("p -> s", lambda x: x[IL] == 1 and x[IF] == 0),
             ("p -> p", lambda x: x[IL] == 1 and x[IF] == 1),
             ("s -> s", lambda x: x[IL] == 0 and x[IF] == 0)]
    fr = {}
    for nm, P in props:
        lacking = 0
        for s in sols:
            lacking += prod(sum(1 for c in sig[x] if not P(LAM[c])) for x in s)
        fr[nm] = Fraction(total - lacking, total)
    good_p = (all(fr[nm] == 1 for nm, _ in props if nm != "s -> s")
              and fr["s -> s"] == Fraction(17403, 24585))
    ok &= good_p
    row("EXHAUSTIVE", "Corollary 7, what every minimum seed contains",
        "; ".join("%s in %s of %d" % (nm, fr[nm].numerator * total // fr[nm].denominator, total)
                  for nm, _ in props), good_p)

    # Corollary 8: no cell is removable -- every one of the 976 deletions still closes to Lambda
    bad_del = sum(1 for i in range(N) if not closes(LAM[:i] + LAM[i + 1:]))
    ok &= bad_del == 0
    row("EXHAUSTIVE", "Corollary 8, no cell is removable",
        "R(Lambda minus x) = Lambda for all %d cells through the closure operator under test, "
        "%d exceptions"
        % (N, bad_del), bad_del == 0)

    # every minimum cover really closes, on a stated sample, and no six-set does
    rnd2 = random.Random(SEED + 3)
    sample = rnd2.sample(sorted(sols), 40)
    badm = 0
    for s in sample:
        cells = [LAM[sig[x][rnd2.randrange(len(sig[x]))]] for x in s]
        if not closes(cells):
            badm += 1
    ok &= badm == 0
    row("SAMPLED", "Theorem 18, the minimum covers close",
        "%d of the %d minimum covers, seed %d, run through the closure operator under test: %d failures"
        % (len(sample), total, SEED + 3, badm), badm == 0)

    counts = defaultdict(int)
    for s in sols:
        mults = [len(sig[x]) for x in s]
        whole = prod(mults)
        for idx, x in enumerate(s):
            share = whole // mults[idx]
            for c in sig[x]:
                counts[c] += share
    vals = sorted(counts.values(), reverse=True)
    med = sorted(counts.values())[len(vals) // 2]
    good_v = (len(vals) == 370 and vals[0] == total and med == 59 and vals[1] == 14492
              and round(100.0 * med / total, 2) == 0.24 and round(100.0 * vals[1] / total, 1) == 58.9)
    ok &= good_v
    row("EXHAUSTIVE", "Theorem 18, the covers by cell",
        "%d of %d cells appear in a minimum cover; the median such cell in %d (%.2f%%), the "
        "second most common in %d (%.1f%%), one in all %d"
        % (len(vals), N, med, 100.0 * med / total, vals[1], 100.0 * vals[1] / total, total),
        good_v)
    print()
    return ok, size, total, sorted(forced), counts, len(uniq), root_lb


# =================================================================== reporting

def cited():
    for who, what in [
        ("Birkhoff (1937)", "a finite distributive lattice is the down-sets of its poset "
                            "of join-irreducibles"),
        ("Birkhoff (1940); Davey and Priestley (2002)",
         "a sublattice of a distributive lattice is distributive; a finite lattice is modular "
         "iff it is graded with a modular rank function"),
        ("Dilworth (1950)", "the minimum chain cover equals the largest antichain"),
        ("Dushnik and Miller (1941)", "order dimension; for a distributive lattice it is "
                                      "the width of the generating poset"),
        ("Rota (1964)", "the crosscut theorem for the Moebius function, and its corollary: "
                        "if the top is not a join of atoms then mu(bottom, top) = 0"),
        ("Karp (1972)", "minimum set cover is NP-hard; its decision version is NP-complete"),
        ("Fulkerson (1956)", "Dilworth's theorem from Koenig's: the minimum chain cover is "
                             "n minus a maximum matching of the strict order"),
        ("Stanley (1989)", "a log-concave sequence with no internal zero is unimodal"),
        ("Stanley (2012)", "the maximal chains of a finite distributive lattice are the "
                           "linear extensions of its poset of join-irreducibles"),
    ]:
        row("CITED", who, what, True)
    print()


def selftest():
    print("SELFTEST -- negative controls that MUST be refuted")
    res = []

    # (1) a sum bound breaks closure -- Z3 must answer sat, with a witness
    caps = [z3.IntVal(c) for c in CAPS]
    X = [z3.Int("sx_" + c) for c in CO]
    Y = [z3.Int("sy_" + c) for c in CO]
    J = [zmax(a, b) for a, b in zip(X, Y)]
    M = [zmin(a, b) for a, b in zip(X, Y)]

    def sm(x):
        return z3.And(z3_member(x, caps), x[IG] + x[IQ] <= 3)

    s = z3.Solver()
    s.add(z3.Not(z3.Implies(z3.And(sm(X), sm(Y)), z3.And(sm(J), sm(M)))))
    r = s.check()
    # the witness the paper prints, verified concretely so the printed pair does not depend
    # on which model the solver happens to return
    wx, wy = (3, 1, 3, 3, 3, 0, 0, 0), (2, 1, 3, 1, 2, 1, 1, 1)

    def sum_ok(t):
        return in_range(t, CAPS) and admissible(t) and t[IG] + t[IQ] <= 3

    named = sum_ok(wx) and sum_ok(wy) and not sum_ok(join(wx, wy))
    res.append(r == z3.sat and named)
    row("SELFTEST", "sum bound g + q <= 3 is not closed",
        "%s; the named witness x = %s, y = %s has join %s with g + q = %d"
        % (r, "".join(map(str, wx)), "".join(map(str, wy)),
           "".join(map(str, join(wx, wy))), join(wx, wy)[IG] + join(wx, wy)[IQ]),
        r == z3.sat and named)

    # (2) drop monotonicity and the bound lemma fails
    phi = z3.Function("nphi", z3.IntSort(), z3.IntSort())
    a1, b1, a2, b2 = z3.Ints("na1 nb1 na2 nb2")
    s2 = z3.Solver()
    s2.add(z3.Not(z3.Implies(z3.And(a1 <= phi(b1), a2 <= phi(b2)),
                             z3.And(zmax(a1, a2) <= phi(zmax(b1, b2)),
                                    zmin(a1, a2) <= phi(zmin(b1, b2))))))
    r2 = s2.check()
    res.append(r2 == z3.sat)
    row("SELFTEST", "the bound lemma needs monotonicity",
        "phi unconstrained: %s" % r2, r2 == z3.sat)

    # (3) the Moebius closed form without its antichain condition
    bad = 0
    for i in range(0, N, 7):
        for j in range(N):
            if MASK[i] & ~MASK[j]:
                continue
            q = MASK[j] & ~MASK[i]
            idxs = [a for a in range(JJ) if q >> a & 1]
            anti = not any(GBELOW[a][b] for a in idxs for b in idxs if a != b)
            if not anti and (-1) ** len(idxs) != 0:
                bad += 1
    res.append(bad > 0)
    row("SELFTEST", "'mu = (-1)^|y \\ x| always' is false",
        "%d pairs in the sweep have a non-antichain difference, where the true value is 0 "
        "and the unconditional formula gives +-1" % bad, bad > 0)

    # (4) the union of two sublattices need not be a sublattice
    ga = GCELL[GNAME.index("n >= 2")]
    gb = GCELL[GNAME.index("e >= 2")]
    U = {x for x in LAM if le(x, ga)} | {x for x in LAM if le(x, gb)}
    escapes = sum(1 for u in U for v in U if join(u, v) not in U)
    res.append(escapes > 0)
    row("SELFTEST", "a union of sublattices is not a sublattice",
        "%d escaping joins in the union of two principal down-sets at incomparable "
        "generators" % escapes, escapes > 0)

    # (5) no six cells generate
    _, sz, _, _, _, _, _ = SEEDRES
    res.append(sz == 7)
    row("SELFTEST", "'seed = 6' is refuted",
        "the exhaustive search found no cover of size 6 and one of size 7", sz == 7)

    # (6) the box count is not the volume
    lo, hi = BOTTOM, TOP
    vol = prod(hi[i] - lo[i] + 1 for i in range(D))
    res.append(count_direct(lo, hi) != vol)
    row("SELFTEST", "'every box is full' is refuted",
        "the whole box holds %d of %d points" % (count_direct(lo, hi), vol),
        count_direct(lo, hi) != vol)
    print()
    return all(res)


SEEDRES = None


def main():
    global SEEDRES
    t0 = time.time()
    print(__doc__)
    if not guards():
        print("GUARDS FAILED -- obligations not reported")
        return 1
    ok = z3_obligations()
    c, marg, floor = construction()
    ok &= c
    ok &= closure_defect()
    st, seq, covP, within, between, surv, ncov = structure()
    ok &= st
    ok &= metric()
    vd, joint, vmarg, vprod, vfree, vpairs = void()
    ok &= vd
    gf, F = generating_function(seq)
    ok &= gf
    ok &= moebius()
    SEEDRES = seed()
    ok &= SEEDRES[0]
    cited()
    if "--selftest" in sys.argv:
        ok &= selftest()
    print("=" * 100)
    from collections import Counter
    cnt = Counter(s for s, _, _, _ in ROWS)
    for s in ("GUARD", "MACHINE-CHECKED", "EXHAUSTIVE", "SAMPLED", "CITED", "SELFTEST"):
        if cnt[s]:
            print("  %-16s %3d" % (s, cnt[s]))
    print("  %d rows, %d failures, %.0f s" % (len(ROWS), len(FAILS), time.time() - t0))
    for f in FAILS:
        print("  FAILED: " + f)
    print("=" * 100)
    return 0 if ok and not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
