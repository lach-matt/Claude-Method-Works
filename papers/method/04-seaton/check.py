#!/usr/bin/env python3
"""check.py -- the machine checks behind papers/method/04-seaton/PAPER.md.

Every number the paper prints is produced here, or is CITED.  Exact arithmetic
(fractions.Fraction, decimal at 40 digits for the one square root) throughout;
Z3 for the two real-arithmetic obligations; stdlib otherwise.

    python3 check.py              every obligation, one line each, a summary; exit 1 on failure
    python3 check.py --selftest   the same, plus five negative controls that must be REFUTED

Instruments are imported by path and never copied:
  recovered/ritz.py            the level data of the thirteen series (read with ast, since the
                               file's own imports need scipy, which is absent here)
  tools/populate.py            core_p -- the core's orbital count at l, from the observed
                               ground configurations of LW1-ground.py (register 1306)
  research/warp-drive/prover.py   require_z3 (no lattice obligation arises in this paper)

Statuses, as PAPER-SPEC.md defines them (and three the check adds for its own bookkeeping):
  PROVED           a written derivation, verified exactly on a grid above its degree
  EXHAUSTIVE       a decision procedure over a stated finite family (size printed)
  MACHINE-CHECKED  Z3 unsat on the negation, box named, both guards passed
  MEASURED         a number computed from the cited levels by the stated procedure
  CROSS-CHECK      two implementations of the same computation compared (not a status of the paper)
  SOURCE           a figure the source states, compared with what is recomputed here
  REFUTED          a negative control of --selftest, which must fail
"""
import ast
import importlib.util
import itertools
import math
import os
import random
import statistics
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RITZ = os.path.join(REPO, "recovered", "ritz.py")
POPULATE = os.path.join(REPO, "tools", "populate.py")
PROVER = os.path.join(REPO, "research", "warp-drive", "prover.py")
RAW = os.path.join(REPO, "extracted", "archives", "restore-point-2-13", "spectra_raw")
CAPTURE = {"Cd I": os.path.join(RAW, "CdI.tsv"), "Rb I": os.path.join(RAW, "RbI.tsv"),
           "Sr II": os.path.join(RAW, "SrII.tsv"),
           "In I": os.path.join(REPO, "extracted", "archives", "spectra-levels-store", "deliver", "queue2", "InI.tsv")}

getcontext().prec = 40

RESULTS = []          # (status, name, ok, detail)
FIGURES = {}          # every number the paper prints, by key


def report(status, name, ok, detail=""):
    RESULTS.append((status, name, ok, detail))
    print("  [%s] %-16s %-58s %s" % ("ok" if ok else "XX", status, name, detail))
    return ok


# ---------------------------------------------------------------- imports by path

def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_series():
    """The thirteen series, read from recovered/ritz.py by AST.  The file executes
    scipy on import, so its data are read as literals rather than by exec; nothing
    is transcribed."""
    tree = ast.parse(open(RITZ, encoding="utf-8").read())
    got = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            nm = node.targets[0].id
            if nm in ("S", "LM", "Rinf", "mp"):
                got[nm] = ast.literal_eval(node.value)
    S, LM = got["S"], got["LM"]
    Rinf, mp = got["Rinf"], got["mp"]
    out = []
    for nm, (c, A, lim, levels) in S.items():
        sp, lc = nm.rsplit(" ", 1)
        out.append(dict(name=nm, species=sp, lsym=lc, l=LM[lc], c=c, A=A, lim=lim,
                        levels={int(k): v for k, v in levels.items()}))
    return out, Rinf, mp


# ------------------------------------------------------------- hydrogenic <r^-4>

def laguerre(k, alpha):
    """Generalised Laguerre L_k^{(alpha)}(x) as exact rational coefficients in x."""
    co = []
    for j in range(k + 1):
        co.append(F((-1) ** j * math.comb(k + alpha, k - j), math.factorial(j)))
    return co


def radial_poly(n, l):
    """P(r) with R_nl(r) = N P(r) e^{-r/n}: r^l L_{n-l-1}^{(2l+1)}(2r/n), Z = 1, a.u."""
    L = laguerre(n - l - 1, 2 * l + 1)
    co = {}
    for j, cj in enumerate(L):
        co[l + j] = cj * F(2, n) ** j
    return co


def poly_mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, 0) + x * y
    return out


def expect_power(n, l, s):
    """<r^s> for the hydrogenic state (n, l), Z = 1, exactly.  Uses
    int_0^inf r^k e^{-2r/n} dr = k! (n/2)^{k+1}, valid for integer k >= 0."""
    P2 = poly_mul(radial_poly(n, l), radial_poly(n, l))
    def integ(shift):
        tot = F(0)
        for k, ck in P2.items():
            kk = k + shift
            if kk < 0:
                raise ValueError("divergent")
            tot += ck * math.factorial(kk) * F(n, 2) ** (kk + 1)
        return tot
    return integ(2 + s) / integ(2)


def r4_formula(n, l):
    """Bethe-Salpeter closed form: [3n^2 - l(l+1)] / [2 n^5 (l+3/2)(l+1)(l+1/2) l (l-1/2)]."""
    D = (F(l) + F(3, 2)) * (l + 1) * (F(l) + F(1, 2)) * l * (F(l) - F(1, 2))
    return F(3 * n * n - l * (l + 1)) / (2 * n ** 5 * D)


def K(l):
    return l * (l + 1) * (2 * l - 1) * (2 * l + 1) * (2 * l + 3)


def ob_r4(nmax=30, wrong=False):
    fam = 0
    bad = 0
    for n in range(2, nmax + 1):
        for l in range(1, n):
            fam += 1
            lhs = expect_power(n, l, -4)
            rhs = r4_formula(n, l)
            if wrong:
                rhs = F(3 * n * n + l * (l + 1)) / (2 * n ** 5) / ((F(l) + F(3, 2)) * (l + 1) * (F(l) + F(1, 2)) * l * (F(l) - F(1, 2)))
            if lhs != rhs:
                bad += 1
    FIGURES["r4_family"] = fam
    FIGURES["r4_nmax"] = nmax
    return fam, bad


def ob_r2_sanity(nmax=30):
    """<r^-2> = 1 / (n^3 (l + 1/2)) -- a second closed form checked the same way, so the
    integration itself is tested against something the <r^-4> formula does not share."""
    fam = bad = 0
    for n in range(2, nmax + 1):
        for l in range(1, n):
            fam += 1
            if expect_power(n, l, -2) != 1 / (n ** 3 * (F(l) + F(1, 2))):
                bad += 1
    return fam, bad


def r2_formula(n, l):
    return 1 / (n ** 3 * (F(l) + F(1, 2)))


def r3_formula(n, l):
    """<r^-3> = 1 / (n^3 l (l+1/2) (l+1))."""
    return 1 / (n ** 3 * l * (F(l) + F(1, 2)) * (l + 1))


def ob_recursion(nmax=12):
    """The Kramers-Pasternack recursion (Pasternack 1937), for every hydrogenic (n, l) with
    n <= nmax, 1 <= l <= n-1, and every integer s with -2l <= s <= 4 (the range on which all
    three moments converge):
        (s+1)/n^2 <r^s> - (2s+1) <r^{s-1}> + (s/4) [(2l+1)^2 - s^2] <r^{s-2}> = 0,
    each moment computed exactly from the Laguerre integral."""
    tot = bad = 0
    for n in range(2, nmax + 1):
        for l in range(1, n):
            for s in range(-2 * l, 5):
                lhs = (F(s + 1, n * n) * expect_power(n, l, s) - (2 * s + 1) * expect_power(n, l, s - 1)
                       + F(s, 4) * ((2 * l + 1) ** 2 - s * s) * expect_power(n, l, s - 2))
                tot += 1
                if lhs != 0:
                    bad += 1
    return tot, bad


def ob_r1_r3(nmax=30):
    """<r^-1> = 1/n^2 and <r^-3> = 1/(n^3 l (l+1/2)(l+1)), the two inputs Lemma 1's proof
    draws through the recursion, each checked against the exact integral on 435 states."""
    fam = b1 = b3 = 0
    for n in range(2, nmax + 1):
        for l in range(1, n):
            fam += 1
            if expect_power(n, l, -1) != F(1, n * n):
                b1 += 1
            if expect_power(n, l, -3) != r3_formula(n, l):
                b3 += 1
    return fam, b1, b3


def ob_lemma1_algebra():
    """Lemma 1's proof, as algebra: the recursion at s = -1 gives <r^-3> = <r^-2>/(l(l+1)); at
    s = -2 it gives <r^-4> = 2 [3 <r^-3> - <r^-2>/n^2] / ((2l-1)(2l+3)).  With <r^-2> =
    1/(n^3 (l+1/2)) substituted, both must equal the closed forms, as rational identities in
    n and l.  Cleared of denominators each is polynomial of degree <= 5 in n and <= 6 in l;
    checked on a 7 x 8 grid of rationals, above the degree in both."""
    pts = 0
    for n in grid(7):
        for l in grid(8, 9):
            r2 = 1 / (n ** 3 * (l + F(1, 2)))
            r3 = r2 / (l * (l + 1))
            r4 = 2 * (3 * r3 - r2 / (n * n)) / ((2 * l - 1) * (2 * l + 3))
            if r3 != 1 / (n ** 3 * l * (l + F(1, 2)) * (l + 1)):
                return pts, False
            if r4 != 4 * (3 * n * n - l * (l + 1)) / (n ** 5 * l * (l + 1) * (2 * l - 1) * (2 * l + 1) * (2 * l + 3)):
                return pts, False
            pts += 1
    return pts, True


def r5_formula(n, l):
    L = l * (l + 1)
    return F(4 * (5 * n * n - 3 * L + 1), n ** 5 * K(l) * (L - 2))


def r6_formula(n, l):
    """<r^-6> = 4 [35 n^4 - 5 (6L-5) n^2 + 3 L (L-2)] / (n^7 K(l) (L-2) (4L-15)), L = l(l+1), l >= 2."""
    L = l * (l + 1)
    return F(4 * (35 * n ** 4 - 5 * (6 * L - 5) * n * n + 3 * L * (L - 2)), n ** 7 * K(l) * (L - 2) * (4 * L - 15))


def ob_r6(nmax=30):
    """Lemma 4's closed forms for <r^-5> and <r^-6>, against the exact integral on every
    (n, l) with n <= nmax and 2 <= l <= n-1 (406 states)."""
    fam = b5 = b6 = 0
    for n in range(2, nmax + 1):
        for l in range(2, n):
            fam += 1
            if expect_power(n, l, -5) != r5_formula(n, l):
                b5 += 1
            if expect_power(n, l, -6) != r6_formula(n, l):
                b6 += 1
    return fam, b5, b6


def ob_lemma4_algebra():
    """Lemma 4's proof as algebra: the recursion at s = -3 and s = -4, with the closed forms
    of <r^-3> and <r^-4> substituted, gives the closed forms of <r^-5> and <r^-6>; and the
    n^-2 / constant ratio of n^7 <r^-6> is -(6L-5)/7.  Rational identities in n and l,
    checked on a 9 x 10 grid of rationals (degree <= 7 in n, <= 8 in l after clearing)."""
    pts = 0
    for n in grid(9):
        for l in grid(10, 11):
            L = l * (l + 1)
            Kl = l * (l + 1) * (2 * l - 1) * (2 * l + 1) * (2 * l + 3)
            r3 = 1 / (n ** 3 * l * (l + F(1, 2)) * (l + 1))
            r4 = 4 * (3 * n * n - L) / (n ** 5 * Kl)
            r5 = (5 * r4 - 2 * r3 / (n * n)) * 4 / (3 * ((2 * l + 1) ** 2 - 9))
            r6 = (7 * r5 - 3 * r4 / (n * n)) / ((2 * l + 1) ** 2 - 16)
            if r5 != 4 * (5 * n * n - 3 * L + 1) / (n ** 5 * Kl * (L - 2)):
                return pts, False
            if r6 != 4 * (35 * n ** 4 - 5 * (6 * L - 5) * n * n + 3 * L * (L - 2)) / (n ** 7 * Kl * (L - 2) * (4 * L - 15)):
                return pts, False
            pts += 1
    return pts, True


def quad_ratio(l):
    """The n^-2 / constant coefficient ratio of the first-order quadrupole defect at l."""
    L = l * (l + 1)
    return F(-(6 * L - 5), 7)


# --------------------------------------------------------- the algebraic identities

def grid(n, start=2):
    out, k = [], start
    while len(out) < n:
        out.append(F(k, k + 1) + k)
        k += 1
    return out


def ob_energy_expansion():
    """-z^2/(2(n-d)^2) + z^2/(2n^2)  ==  -z^2 d (2n - d) / (2 n^2 (n - d)^2), as a polynomial
    identity after clearing 2 n^2 (n-d)^2: degree 2 in n, 2 in d, 2 in z -> grid 4 x 4 x 4."""
    pts = 0
    for n in grid(4):
        for d in grid(4, 7):
            for z in grid(4, 11):
                lhs = (-z * z / (2 * (n - d) ** 2) + z * z / (2 * n * n)) * 2 * n * n * (n - d) ** 2
                rhs = -z * z * d * (2 * n - d)
                if lhs != rhs:
                    return pts, False
                pts += 1
    return pts, True


def ob_defect_rearrangement(wrong=False):
    """Lemma 2's rearrangement, the two identities the lemma prints:
      (i)  2 (n-d)^2 / (n (2n-d))  ==  1 - (3 n d - 2 d^2) / (n (2n-d)),
           polynomial after clearing n(2n-d): degree 2 in n, 2 in d -> grid 4 x 4;
      (ii) d  ==  -(n^3/z^2) * DE(n, d, z) * 2 (n-d)^2 / (n (2n-d)),
           with DE = -z^2 d (2n-d) / (2 n^2 (n-d)^2) the identity of Lemma 2; after clearing,
           degree 6 in n, 4 in d, 2 in z -> grid 7 x 5 x 3.
    wrong=True drops the factor 2 (the printed error the audit found) and must fail."""
    two = 2 if not wrong else 1
    pts = 0
    for n in grid(4):
        for d in grid(4, 7):
            lhs = two * (n - d) ** 2
            rhs = n * (2 * n - d) - (3 * n * d - 2 * d * d)
            if lhs != rhs:
                return pts, False
            pts += 1
    for n in grid(7):
        for d in grid(5, 9):
            for z in grid(3, 15):
                DE = -z * z * d * (2 * n - d) / (2 * n * n * (n - d) ** 2)
                rhs = -(n ** 3 / (z * z)) * DE * two * (n - d) ** 2 / (n * (2 * n - d))
                if rhs != d:
                    return pts, False
                pts += 1
    return pts, True


def ob_ritz_vs_n2():
    """d2/(n-d0)^2 - d2/n^2  ==  d2 d0 (2n - d0) / (n^2 (n-d0)^2): the Ritz denominator differs
    from 1/n^2 by a term of order d0 d2, second order in the polarisability (Lemma 3).
    Cleared of n^2 (n-d0)^2 it is polynomial: degree 2 in n, 2 in d0, 1 in d2 -> grid 4 x 5 x 3."""
    pts = 0
    for n in grid(4):
        for d0 in grid(5, 7):
            for d2 in grid(3, 13):
                lhs = (d2 / (n - d0) ** 2 - d2 / (n * n)) * n * n * (n - d0) ** 2
                rhs = d2 * d0 * (2 * n - d0)
                if lhs != rhs:
                    return pts, False
                pts += 1
    return pts, True


def seaton_coeffs(alpha, z, l):
    """First-order polarisation defect delta(n) = c0 + c2 / n^2 with
    c0 = 6 alpha z^2 / K(l),  c2 = -2 alpha z^2 l(l+1) / K(l).  (Theorem 1.)"""
    c0 = 6 * alpha * z * z / F(K(l))
    c2 = -2 * alpha * z * z * l * (l + 1) / F(K(l))
    return c0, c2


def ob_ratio_identity():
    """delta(n) = (alpha/2) z^2 n^3 <r^-4>_n  ==  c0 + c2/n^2 with c2/c0 = -l(l+1)/3, for every
    (n, l) in the exhausted family, on a grid of alpha and z above the degree (1 and 2)."""
    fam = 0
    for n in range(2, 21):
        for l in range(1, n):
            r4 = r4_formula(n, l)
            for alpha in grid(3):
                for z in grid(4, 9):
                    c0, c2 = seaton_coeffs(alpha, z, l)
                    lhs = alpha / 2 * z * z * n ** 3 * r4
                    if lhs != c0 + c2 / (n * n):
                        return fam, False
                    if 3 * c2 != -l * (l + 1) * c0:
                        return fam, False
                    fam += 1
    return fam, True


# ------------------------------------------------------------------ Z3 obligations

Z3_SEED = 5


def ob_z3(lmax=8, wrong=False):
    """Theorem 1 from its PREMISE.  For each l in {1..lmax} the term
        D(n) := (alpha/2) z^2 n^3 * 4 (3 n^2 - l(l+1)) / (n^5 K(l))
    is the first-order defect with Lemma 1's <r^-4> substituted -- the hypothesis of the
    theorem, not its conclusion.  Z3 is asked, for ALL real alpha, z and all real n1, n2, n3 >= 2
    with n1 != n2: define c2 := (D(n1) - D(n2)) / (1/n1^2 - 1/n2^2) and c0 := D(n1) - c2/n1^2
    (the affine-in-1/n^2 coefficients any two points determine); then
        3 c2 = -l(l+1) c0,   D(n3) = c0 + c2/n3^2   (the form IS affine in 1/n^2),
        and alpha > 0, z != 0  =>  c0 > 0, c2 < 0.
    Negation asserted under the hypothesis, unsat expected.  Guards: non-vacuity (the
    hypothesis with alpha > 0, z != 0 is satisfiable) and encoding fidelity (the Z3 term D(n),
    evaluated at 200 seeded random rational (alpha, z, n, l), equals (alpha/2) z^2 n^3 times
    the Laguerre-integral <r^-4> of expect_power -- an implementation that shares no formula
    with the encoding)."""
    prover = _load("prover", PROVER)
    prover.require_z3()
    import z3
    a, z, n1, n2, n3 = z3.Reals("alpha z n1 n2 n3")

    def D(n, l):
        L = l * (l + 1)
        return (a / 2) * z * z * n ** 3 * 4 * (3 * n * n - L) / (n ** 5 * K(l))

    hyp = z3.And(n1 >= 2, n2 >= 2, n3 >= 2, n1 != n2)
    results = []
    for l in range(1, lmax + 1):
        L = l * (l + 1)
        c2 = (D(n1, l) - D(n2, l)) / (1 / (n1 * n1) - 1 / (n2 * n2))
        c0 = D(n1, l) - c2 / (n1 * n1)
        target = -L if not wrong else -2 * L
        claim = z3.And(3 * c2 == target * c0,
                       D(n3, l) == c0 + c2 / (n3 * n3),
                       z3.Implies(z3.And(a > 0, z != 0), z3.And(c0 > 0, c2 < 0)))
        s = z3.Solver()
        s.add(hyp)
        s.add(z3.Not(claim))
        results.append(s.check() == z3.unsat)
    # guard 1: non-vacuity
    s = z3.Solver(); s.add(hyp, a > 0, z != 0)
    nonvac = s.check() == z3.sat
    # guard 2: encoding fidelity against the Laguerre integral, which shares no formula with D
    rnd = random.Random(Z3_SEED)
    compared = disagree = 0
    for _ in range(200):
        n = rnd.randint(2, 20)
        l = rnd.randint(1, min(lmax, n - 1))
        av = F(rnd.randint(-50, 50), rnd.randint(1, 9))
        zv = F(rnd.randint(-6, 6), rnd.randint(1, 3))
        term = z3.simplify(z3.substitute(D(n1, l), (a, z3.RealVal(str(av))), (z, z3.RealVal(str(zv))),
                                         (n1, z3.RealVal(str(n)))))
        independent = av / 2 * zv * zv * n ** 3 * expect_power(n, l, -4)
        compared += 1
        if F(term.as_fraction()) != independent:
            disagree += 1
    return all(results), nonvac, compared, disagree


def ob_z3_quadrupole(lmax=8):
    """Lemma 4's consequence, for each l in {2..lmax}: with r_d = -l(l+1)/3 the dipole ratio and
    r_q = -(6 l(l+1) - 5)/7 the quadrupole ratio, for ALL real c0 > 0 and q0 > 0 the combined
    n^-2 / constant ratio (r_d c0 + r_q q0)/(c0 + q0) lies strictly between r_q and r_d, so its
    ratio to r_d exceeds 1.  Negation unsat expected.  Guards: non-vacuity of c0 > 0, q0 > 0;
    fidelity of the Z3 ratio terms against Fraction arithmetic at 200 seeded random points."""
    prover = _load("prover", PROVER)
    prover.require_z3()
    import z3
    c0, q0 = z3.Reals("c0 q0")
    results = []
    for l in range(2, lmax + 1):
        rd = z3.RealVal(str(F(-l * (l + 1), 3)))
        rq = z3.RealVal(str(quad_ratio(l)))
        mix = (rd * c0 + rq * q0) / (c0 + q0)
        claim = z3.And(rq < mix, mix < rd, mix / rd > 1)
        s = z3.Solver(); s.add(c0 > 0, q0 > 0); s.add(z3.Not(claim))
        results.append(s.check() == z3.unsat)
    s = z3.Solver(); s.add(c0 > 0, q0 > 0)
    nonvac = s.check() == z3.sat
    rnd = random.Random(Z3_SEED)
    compared = disagree = 0
    for _ in range(200):
        l = rnd.randint(2, lmax)
        cv = F(rnd.randint(1, 60), rnd.randint(1, 9))
        qv = F(rnd.randint(1, 60), rnd.randint(1, 9))
        rd = z3.RealVal(str(F(-l * (l + 1), 3))); rq = z3.RealVal(str(quad_ratio(l)))
        term = z3.simplify(z3.substitute((rd * c0 + rq * q0) / (c0 + q0), (c0, z3.RealVal(str(cv))), (q0, z3.RealVal(str(qv)))))
        indep = (F(-l * (l + 1), 3) * cv + quad_ratio(l) * qv) / (cv + qv)
        compared += 1
        if F(term.as_fraction()) != indep:
            disagree += 1
    return all(results), nonvac, compared, disagree


def ob_prefactor_rb(wrong=False):
    """Theorem 1's prefactor tested on a series outside the sample, in exact arithmetic on CITED values.
    Rb ng: delta_g(n = 30) = 0.00405(6) (Afrousheh, Bohlouli-Zanjani, Petrus and Martin 2006);
    alpha_d(Rb+) = 9.116(9) a0^3 and alpha_q = 38.4(6) a0^5 (Berl, Sackett, Gallagher and Nunkaew 2020);
    alpha_d = 9.11 a0^3 by relativistic coupled cluster (Lim, Laerdahl and Schwerdtfeger 2000).
    The dipole limit is 6 alpha/K(4) under Theorem 1 and 3 alpha/K(4) under the working record's form;
    the n-dependent value at n = 30 adds c2/n^2 and the first-order quadrupole shift of -alpha_q/(2 r^6),
    alpha_q n^3 <r^-6>/2 with <r^-6> from Lemma 4's closed form (z = 1).  With wrong=True the 3/K form
    is carried through the same arithmetic and must miss the measurement (a negative control)."""
    l, n = 4, 30
    a, aq = F(9116, 1000), F(384, 10)
    a_rcc = F(911, 100)
    meas, unc = F(405, 100000), F(6, 100000)
    Kl = K(l)
    six, three = 6 * a / Kl, 3 * a / Kl
    c0 = three if wrong else six
    c2 = c0 * F(-l * (l + 1), 3)
    quad = aq * n ** 3 * r6_formula(n, l) / 2
    full = c0 + c2 / F(n * n) + quad
    ok = (abs(full - meas) <= unc and F(100, 100) < meas / six < F(105, 100)
          and F(19, 10) < meas / three < F(21, 10) and F(100, 100) < meas / (6 * a_rcc / Kl) < F(105, 100))
    return {"six": six, "three": three, "full": full, "meas": meas, "unc": unc, "ok": ok, "K": Kl,
            "rcc": 6 * a_rcc / Kl}


def ob_published(rows):
    """§5.7: the implied polarisabilities of the p = 0 series against published values, and the Rb fits
    against published Rydberg-Ritz coefficients.  Exact arithmetic on CITED inputs: Cd+ 25.2(6) (Li, Yu and
    Sahoo 2018), In+ 24.33 (Yu et al. 2015; 24.01 Safronova et al. as quoted there), Sr2+ 5.813 RRPA and 5.792
    RCCSDT (Mitroy, Safronova and Clark 2010, Table IV); 85Rb ns 3.1311804(10), 0.1784(6); nd3/2
    1.3480917(4), -0.6029(3); nd5/2 1.3464657(3), -0.5960(2) (Li et al. 2003, as tabulated by Mack et al. 2011)."""
    pub = {"Cd I f": [F(252, 10)], "In I f": [F(2433, 100), F(2401, 100)], "Sr II f": [F(5813, 1000), F(5792, 1000)]}
    by = {r["name"]: r for r in rows}
    out = {}
    for name, vals in pub.items():
        r = by[name]
        imp = r["d0"] * K(r["l"]) / (6 * r["c"] ** 2)
        out[name] = {"implied": imp, "ratios": [imp / v for v in vals], "ratios3": [2 * imp / v for v in vals]}
    ok_alpha = (F(95, 100) < out["Cd I f"]["ratios"][0] < F(105, 100)
                and all(F(105, 100) < x < F(110, 100) for x in out["In I f"]["ratios"])
                and all(F(17, 10) < x < F(18, 10) for x in out["Sr II f"]["ratios"])
                and all(x > F(19, 10) for n in out for x in out[n]["ratios3"]))
    rb = {"s": (F(31311804, 10 ** 7), F(1784, 10 ** 4)),
          "d3/2": (F(13480917, 10 ** 7), F(-6029, 10 ** 4)), "d5/2": (F(13464657, 10 ** 7), F(-5960, 10 ** 4))}
    s, d = by["Rb I s"], by["Rb I d"]
    dd0 = {"s": s["d0"] - rb["s"][0], "d3/2": d["d0"] - rb["d3/2"][0], "d5/2": d["d0"] - rb["d5/2"][0]}
    rd2 = {"s": (s["d2"] - rb["s"][1]) / rb["s"][1], "d3/2": (d["d2"] - rb["d3/2"][1]) / rb["d3/2"][1],
           "d5/2": (d["d2"] - rb["d5/2"][1]) / rb["d5/2"][1]}
    ok_rb = abs(dd0["s"]) < F(4, 10 ** 4) and all(abs(dd0[k]) < F(4, 10 ** 3) for k in ("d3/2", "d5/2")) \
        and all(abs(x) < F(3, 10) for x in rd2.values())
    return out, ok_alpha, dd0, rd2, ok_rb


def ob_prefactor():
    """The prefactor identity behind Theorem 1's displayed constant:
        6 / K(l)  ==  (3/4) / [ (l-1/2) l (l+1/2) (l+1) (l+3/2) ],
    a polynomial identity of degree 5 in l after clearing, checked at every l in 1..200 (a grid
    far above the degree, so it holds for all l); and l^5 * 6/K(l) < 3/4, strictly increasing,
    at every consecutive pair of l in 1..200 (EXHAUSTIVE over that family)."""
    fam = 0
    ok = True
    for l in range(1, 201):
        lhs = F(6, K(l))
        rhs = F(3, 4) / ((F(l) - F(1, 2)) * l * (F(l) + F(1, 2)) * (l + 1) * (F(l) + F(3, 2)))
        if lhs != rhs:
            ok = False
        fam += 1
    tail = [F(l) ** 5 * F(6, K(l)) for l in range(1, 201)]
    mono = all(a < b for a, b in zip(tail, tail[1:])) and all(t < F(3, 4) for t in tail)
    return fam, ok, mono, float(tail[-1])


def ob_limit_sensitivity():
    """A shift dI in the ionisation limit moves the defect by about n*^3 dI / (2 z^2 R_M).
    Checked against the exact recomputation on every level of every series, at dI = 0.01 cm^-1:
    the predicted and the recomputed shift agree to better than 1 part in 10^4."""
    series, Rinf, mp = load_series()
    worst = 0.0
    tot = 0
    for ser in series:
        RM = Decimal(repr(Rinf)) / (1 + 1 / (Decimal(repr(ser["A"])) * Decimal(repr(mp))))
        for n in sorted(ser["levels"]):
            E = Decimal(repr(ser["levels"][n]))
            I = Decimal(repr(ser["lim"]))
            dI = Decimal("0.01")
            ns0 = Decimal(ser["c"]) * dec_sqrt(RM / (I - E))
            ns1 = Decimal(ser["c"]) * dec_sqrt(RM / (I + dI - E))
            actual = (Decimal(n) - ns1) - (Decimal(n) - ns0)          # change in delta
            pred = ns0 ** 3 * dI / (2 * Decimal(ser["c"]) ** 2 * RM)
            worst = max(worst, abs(float((actual - pred) / pred)))
            tot += 1
    return tot, worst


def ob_separating_cores():
    """Where p and l part company, read from the same observed ground configurations as D3:
      - an argon-like core (18 electrons) holds no d orbital, so p = 0 at l = 2, where the
        krypton-like core of this sample has p = 1; the electron counts with p = 0 at l = 2;
      - the cores with an occupied f subshell (p >= 1 at l = 3), which begin at 58 electrons;
      - no core in the table holds a g orbital, so p = 0 at l = 4 on every one of them.
    Returns (p at l=2 for 18 e, for 36 e, the list of e-counts with p = 0 at l = 2, the list
    with p >= 1 at l = 3, the table's electron-count range, the count of g-occupied cores)."""
    pop = _load("populate", POPULATE)
    ar_d = pop.core_p(18, 2)           # Ca II nd converges on Ca2+, argon-like
    kr_d = pop.core_p(36, 2)           # Sr II nd converges on Sr2+, krypton-like
    table = [ne for ne in range(1, 200) if pop.config_of(ne, "observed") is not None]
    d0 = [ne for ne in table if pop.core_p(ne, 2) == 0]
    fcores = [ne for ne in table if pop.core_p(ne, 3) >= 1]
    gcores = [ne for ne in table if pop.core_p(ne, 4) >= 1]
    return ar_d, kr_d, d0, fcores, (min(table), max(table)), len(gcores)


# -------------------------------------------------------------- the classification

def ob_p_table():
    pop = _load("populate", POPULATE)
    cores = {"Cd I": 47, "In I": 48, "Rb I": 36, "Sr II": 36}   # Z - charge
    table = {}
    for sp, ne in cores.items():
        table[sp] = {l: pop.core_p(ne, l) for l in range(0, 4)}
    expect = {"Cd I": {0: 5, 1: 3, 2: 2, 3: 0}, "In I": {0: 5, 1: 3, 2: 2, 3: 0},
              "Rb I": {0: 4, 1: 3, 2: 1, 3: 0}, "Sr II": {0: 4, 1: 3, 2: 1, 3: 0}}
    ok = table == expect
    FIGURES["p_table"] = table
    # on these four cores p = 0 iff l >= 3 (the sample cannot separate p from l)
    same = all((table[sp][l] == 0) == (l >= 3) for sp in cores for l in range(4))
    FIGURES["p_iff_l3"] = same
    return ok, same, table


# ------------------------------------------------------------- the quantum defects

def dec_sqrt(x):
    return Decimal(x).sqrt()


def defects(ser, Rinf, mp):
    """delta_n = n - c sqrt(R_M / (I - E_n)),  R_M = R_inf / (1 + 1/(A m_p)).  Exact
    rationals except the one square root, taken to 40 significant digits."""
    RM = Decimal(repr(Rinf)) / (1 + 1 / (Decimal(repr(ser["A"])) * Decimal(repr(mp))))
    out = []
    for n in sorted(ser["levels"]):
        E = Decimal(repr(ser["levels"][n]))
        I = Decimal(repr(ser["lim"]))
        nstar = ser["c"] * dec_sqrt(RM / (I - E))
        out.append((n, F(n) - F(nstar)))
    return out, RM


def profile_fit(pts, ritz=True):
    """Least squares for delta(n) = d0 + d2 / (n - d0)^2  (ritz=True) or d0 + d2 / n^2.
    For fixed d0 the model is linear in d2, so d2*(d0) is exact and S(d0) is a rational
    function; the minimiser is located by an exact scan, then a ternary search in exact
    rationals, and certified: S at the minimiser is below S at every scanned point and at
    both ends of the final bracket."""
    ns = [F(n) for n, _ in pts]
    ds = [d for _, d in pts]

    def S_and_d2(d0):
        w = [1 / (n - d0) ** 2 if ritz else 1 / (n * n) for n in ns]
        r = [d - d0 for d in ds]
        d2 = sum(ri * wi for ri, wi in zip(r, w)) / sum(wi * wi for wi in w)
        S = sum((ri - d2 * wi) ** 2 for ri, wi in zip(r, w))
        return S, d2

    lo, hi = min(ds) - 1, max(ds) + 1
    if hi >= min(ns) - F(1, 2):
        hi = min(ns) - F(1, 2)
    steps = 400
    best = None
    scanned = []
    for i in range(steps + 1):
        d0 = lo + (hi - lo) * i / steps
        S, _ = S_and_d2(d0)
        scanned.append((d0, S))
        if best is None or S < best[1]:
            best = (d0, S)
    h = (hi - lo) / steps
    a, b = best[0] - h, best[0] + h
    # ternary search, exact
    for _ in range(90):
        m1 = a + (b - a) / 3
        m2 = b - (b - a) / 3
        if S_and_d2(m1)[0] <= S_and_d2(m2)[0]:
            b = m2
        else:
            a = m1
    d0 = (a + b) / 2
    S, d2 = S_and_d2(d0)
    certified = all(S <= s for _, s in scanned) and S <= S_and_d2(a)[0] and S <= S_and_d2(b)[0]
    # count the local minima on the scan, so a second basin would be reported
    basins = 0
    for i in range(1, len(scanned) - 1):
        if scanned[i][1] < scanned[i - 1][1] and scanned[i][1] < scanned[i + 1][1]:
            basins += 1
    return d0, d2, S, certified, basins, float(b - a)


def capture_levels(species):
    """Every (n, l-symbol, energy) the species' NIST ASD capture file holds, as strings."""
    out = set()
    for line in open(CAPTURE[species], encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        f = line.rstrip("\n").split("\t")
        cfg = f[0].split(".")[-1]
        import re
        m = re.match(r"(\d+)([spdfgh])$", cfg)
        if not m:
            continue
        val = f[3].strip("[]")
        try:
            out.add((int(m.group(1)), m.group(2), float(val)))
        except ValueError:
            pass
    return out


def ob_captures(rows):
    """Each level the instrument tabulates occurs, at the same n and l, in the species'
    capture file -- a second copy of the same NIST retrieval held in the tree."""
    tot = 0
    missing = []
    for r in rows:
        cap = capture_levels(r["species"])
        for n, E in r["levels"].items():
            tot += 1
            if (n, r["lsym"], E) not in cap:
                missing.append((r["name"], n, E))
    return tot, missing


# the source's own printed fit, (d0, d2), four decimals, as the instrument printed it
SOURCE_FIT = {
    "Cd I f": (0.0393, -0.1808), "In I f": (0.0416, -0.1838), "Sr II f": (0.0648, -0.4054),
    "Rb I d": (1.3504, -0.7418), "Sr II d": (1.4514, 0.5152), "Cd I d": (2.0837, 0.1403),
    "In I d": (2.3009, -1.0075), "Cd I p": (3.0522, -0.0082), "Rb I p": (2.6540, 0.3258),
    "Rb I s": (3.1308, 0.1980), "Sr II s": (2.7055, 0.3394), "Cd I s": (3.6551, 0.3354),
    "In I s": (3.7193, 0.3168),
}
SOURCE_STAT = {"p0_median": 1.150, "p0_sd": 0.206, "p1_median": -0.015, "p1_sd": 0.177,
               "p0_series": 3, "p1_series": 10}
# the channel table's Cd I rows (species, series, n-range, members, median delta, spread, limit)
SOURCE_CDI = {"d": ("nd 3D J=1", (5, 11), 7, 2.0898, 0.0049), "f": ("nf 3F* J=3", (4, 10), 7, 0.0346, 0.0034),
              "s": ("ns 3S J=1", (6, 16), 11, 3.6677, 0.0188), "p": ("np 1P* J=1", (6, 12), 7, 3.0515, 0.0005)}


def r3(x):
    return round(float(x), 3)


def r4(x):
    return round(float(x), 4)


def pstdev(xs):
    m = sum(xs) / len(xs)
    return math.sqrt(float(sum((x - m) ** 2 for x in xs) / len(xs)))


def sstdev(xs):
    m = sum(xs) / len(xs)
    return math.sqrt(float(sum((x - m) ** 2 for x in xs) / (len(xs) - 1)))


def run_fits(perturb=None):
    series, Rinf, mp = load_series()
    pop = _load("populate", POPULATE)
    cores = {"Cd I": 47, "In I": 48, "Rb I": 36, "Sr II": 36}
    rows = []
    for ser in series:
        if perturb and ser["name"] == perturb[0]:
            ser = dict(ser, levels=dict(ser["levels"]))
            ser["levels"][perturb[1]] += perturb[2]
        pts, RM = defects(ser, Rinf, mp)
        if len(pts) < 4:
            continue
        d0, d2, S, cert, basins, width = profile_fit(pts)
        d0n, d2n, Sn, certn, _, _ = profile_fit(pts, ritz=False)
        l = ser["l"]
        p = pop.core_p(cores[ser["species"]], l)
        seat = F(-l * (l + 1), 3)
        rho = (d2 / d0) / seat if seat != 0 else None
        rho_n2 = (d2n / d0n) / seat if seat != 0 else None
        rows.append(dict(name=ser["name"], species=ser["species"], l=l, lsym=ser["lsym"], p=p, c=ser["c"],
                         A=ser["A"], lim=ser["lim"], RM=RM, n_lo=pts[0][0], n_hi=pts[-1][0], members=len(pts),
                         pts=pts, d0=d0, d2=d2, rms=math.sqrt(float(S) / len(pts)), certified=cert,
                         basins=basins, width=width, seat=seat, rho=rho, d0_n2=d0n, d2_n2=d2n, rho_n2=rho_n2,
                         levels=ser["levels"]))
    return rows


def stats(rows):
    p0 = [r for r in rows if r["p"] == 0]
    p1 = [r for r in rows if r["p"] >= 1]
    p0r = [r["rho"] for r in p0 if r["rho"] is not None]
    p1r = [r["rho"] for r in p1 if r["rho"] is not None]
    out = dict(p0_series=len(p0), p1_series=len(p1), p0_defined=len(p0r), p1_defined=len(p1r),
               p0_median=statistics.median(p0r), p0_sd=pstdev(p0r), p0_mean=sum(p0r) / len(p0r), p0_ssd=sstdev(p0r),
               p1_median=statistics.median(p1r), p1_sd=pstdev(p1r), p1_mean=sum(p1r) / len(p1r), p1_ssd=sstdev(p1r),
               p0_min=min(p0r), p0_max=max(p0r), p1_min=min(p1r), p1_max=max(p1r),
               p0_rho=p0r, p1_rho=p1r)
    p1n = [r["rho_n2"] for r in p1 if r["rho_n2"] is not None]
    p0n = [r["rho_n2"] for r in p0 if r["rho_n2"] is not None]
    out.update(p0_median_n2=statistics.median(p0n), p0_sd_n2=pstdev(p0n),
               p1_median_n2=statistics.median(p1n), p1_sd_n2=pstdev(p1n))
    # leave-one-out on the p = 0 class
    loo = []
    for i in range(len(p0r)):
        rest = p0r[:i] + p0r[i + 1:]
        loo.append(statistics.median(rest))
    out["p0_loo"] = loo
    # sign rule
    sign = {}
    for r in rows:
        sign.setdefault(r["p"], [0, 0])
        sign[r["p"]][0 if r["d2"] > 0 else 1] += 1
    out["sign"] = sign
    return out


# ------------------------------------------------- the independent fitter and sensitivities

def gauss_newton(pts, iters=200):
    """A second, independent solution of the least-squares problem of D2: undamped
    Gauss-Newton in floating point on the two parameters (d0, d2) of
    delta(n) = d0 + d2 / (n - d0)^2, from the start (mean delta, 0), with the analytic
    Jacobian dr/dd0 = -1 - 2 d2/(n-d0)^3, dr/dd2 = -1/(n-d0)^2.  It shares no code and no
    formulation with profile_fit (which profiles d2 out exactly and scans d0)."""
    ns = [float(n) for n, _ in pts]
    ds = [float(d) for _, d in pts]
    d0 = sum(ds) / len(ds)
    d2 = 0.0
    it = 0
    for it in range(1, iters + 1):
        r = [d - d0 - d2 / (n - d0) ** 2 for n, d in zip(ns, ds)]
        J0 = [-1 - 2 * d2 / (n - d0) ** 3 for n in ns]
        J2 = [-1 / (n - d0) ** 2 for n in ns]
        a00 = sum(x * x for x in J0); a02 = sum(x * y for x, y in zip(J0, J2)); a22 = sum(y * y for y in J2)
        b0 = -sum(x * ri for x, ri in zip(J0, r)); b2 = -sum(y * ri for y, ri in zip(J2, r))
        det = a00 * a22 - a02 * a02
        s0 = (b0 * a22 - b2 * a02) / det
        s2 = (a00 * b2 - a02 * b0) / det
        d0 += s0; d2 += s2
        if abs(s0) < 1e-15 and abs(s2) < 1e-15:
            break
    return d0, d2, it


def quoted_levels(species):
    """Every level of the species' capture file as NIST prints it: (n, l-symbol, float) -> string,
    so Table 2 can carry each level at its quoted precision."""
    import re
    out = {}
    for line in open(CAPTURE[species], encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        f = line.rstrip("\n").split("\t")
        cfg = f[0].split(".")[-1]
        m = re.match(r"(\d+)([spdfgh])$", cfg)
        if not m:
            continue
        val = f[3].strip("[]").strip()
        try:
            out[(int(m.group(1)), m.group(2), float(val))] = val
        except ValueError:
            pass
    return out


def rho_of_series(ser, Rinf, mp):
    pts, _ = defects(ser, Rinf, mp)
    d0, d2, S, cert, basins, width = profile_fit(pts)
    l = ser["l"]
    return float((d2 / d0) / F(-l * (l + 1), 3)), d0, d2


def ob_sensitivity():
    """For each p = 0 series: rho with its lowest member left out; the quotation-floor
    sensitivity, sum over members of |rho(E_i + h_i) - rho| with h_i half of one unit in the
    last digit NIST quotes for that level (a linearised worst case); rho with the limit
    moved by +0.1 cm^-1; and, for Cd I, rho at the limit's published +/- 0.13 cm^-1.
    Also the polarisability the fitted d0 implies through Theorem 1, d0 K(l) / (6 z^2)."""
    series, Rinf, mp = load_series()
    pop = _load("populate", POPULATE)
    cores = {"Cd I": 47, "In I": 48, "Rb I": 36, "Sr II": 36}
    out = []
    for ser in series:
        if pop.core_p(cores[ser["species"]], ser["l"]) != 0:
            continue
        base, d0, d2 = rho_of_series(ser, Rinf, mp)
        lo = min(ser["levels"])
        loo, _, _ = rho_of_series(dict(ser, levels={k: v for k, v in ser["levels"].items() if k != lo}), Rinf, mp)
        q = quoted_levels(ser["species"])
        floor = 0.0
        hs = []
        for n, E in ser["levels"].items():
            st = q.get((n, ser["lsym"], E), "%.3f" % E)
            dec = len(st.split(".")[1]) if "." in st else 0
            h = 0.5 * 10 ** (-dec)
            hs.append(h)
            s3 = dict(ser, levels=dict(ser["levels"])); s3["levels"][n] = E + h
            floor += abs(rho_of_series(s3, Rinf, mp)[0] - base)
        lim1, _, _ = rho_of_series(dict(ser, lim=ser["lim"] + 0.1), Rinf, mp)
        row = dict(name=ser["name"], rho=base, loo=loo, floor=floor, hs=hs, dlim=lim1 - base,
                   alpha=float(d0 * K(ser["l"]) / (6 * ser["c"] ** 2)))
        if ser["species"] == "Cd I":
            row["lim_pm"] = (rho_of_series(dict(ser, lim=ser["lim"] - 0.13), Rinf, mp)[0],
                             rho_of_series(dict(ser, lim=ser["lim"] + 0.13), Rinf, mp)[0])
        out.append(row)
    return out


# ------------------------------------------------------------------------- main

def main(selftest=False):
    print("papers/method/04-seaton -- check.py")
    print()
    allok = True

    # 1  the hydrogenic moments (Lemma 1, Lemma 4)
    fam, bad = ob_r4()
    allok &= report("EXHAUSTIVE", "Lemma 1: <r^-4> closed form", bad == 0,
                    "%d states (n <= %d, 1 <= l <= n-1), %d disagree" % (fam, FIGURES["r4_nmax"], bad))
    fam2, bad2 = ob_r2_sanity()
    allok &= report("EXHAUSTIVE", "<r^-2> = 1/(n^3 (l+1/2))", bad2 == 0, "%d states, %d disagree" % (fam2, bad2))
    famr, badr = ob_recursion()
    allok &= report("EXHAUSTIVE", "Kramers-Pasternack recursion", badr == 0,
                    "%d (n, l, s) triples, n <= 12, -2l <= s <= 4, %d disagree" % (famr, badr))
    fam13, b1, b3 = ob_r1_r3()
    allok &= report("EXHAUSTIVE", "<r^-1> = 1/n^2 and <r^-3> = 1/(n^3 l(l+1/2)(l+1))", b1 == 0 and b3 == 0,
                    "%d states, %d and %d disagree" % (fam13, b1, b3))
    pts1, ok1 = ob_lemma1_algebra()
    allok &= report("PROVED", "Lemma 1: recursion at s = -1, -2 gives the closed form", ok1,
                    "rational identity in (n, l), grid 7x8 above degree, %d points" % pts1)
    fam6, b5, b6 = ob_r6()
    allok &= report("EXHAUSTIVE", "Lemma 4: <r^-5> and <r^-6> closed forms", b5 == 0 and b6 == 0,
                    "%d states (n <= 30, 2 <= l <= n-1), %d and %d disagree" % (fam6, b5, b6))
    pts4, ok4 = ob_lemma4_algebra()
    allok &= report("PROVED", "Lemma 4: recursion at s = -3, -4 gives the closed forms", ok4,
                    "rational identity in (n, l), grid 9x10 above degree, %d points; quadrupole ratio -(6l(l+1)-5)/7 = %s at l = 2, %s at l = 3 (%.3f)"
                    % (pts4, quad_ratio(2), quad_ratio(3), float(quad_ratio(3))))

    # 2  the algebraic identities (Lemmas 2, 3, the prefactor)
    pts, ok = ob_energy_expansion()
    allok &= report("PROVED", "Lemma 2: exact energy-defect identity", ok, "grid 4x4x4 above degree (2,2,2), %d points" % pts)
    ptsr, okr = ob_defect_rearrangement()
    allok &= report("PROVED", "Lemma 2: rearrangement 2(n-d)^2/(n(2n-d)) = 1 - (3nd-2d^2)/(n(2n-d))", okr,
                    "grid 4x4 and 7x5x3 above degree, %d points" % ptsr)
    pts3, ok3b = ob_ritz_vs_n2()
    allok &= report("PROVED", "Lemma 3: Ritz denominator vs 1/n^2, exact identity", ok3b, "grid 4x5x3 above degree (2,2,1), %d points" % pts3)
    famp, okp, monop, tail = ob_prefactor()
    allok &= report("PROVED", "Theorem 1's prefactor 6/K(l) = (3/4)/[(l-1/2)l(l+1/2)(l+1)(l+3/2)]", okp,
                    "degree 5 in l, checked at %d values of l" % famp)
    allok &= report("EXHAUSTIVE", "l^5 6/K(l) < 3/4 and strictly increasing over l in 1..200", monop,
                    "%d values; reaches %.6f at l = 200" % (famp, tail))
    rb = ob_prefactor_rb()
    allok &= report("MEASURED", "the prefactor on Rb ng (outside the sample): 6a/K(4) against 3a/K(4), CITED inputs", rb["ok"],
                    "K(4) = %d; 6a/K = %.6f (a = 9.116), %.6f (a = 9.11); 3a/K = %.6f; with c2/n^2 and the quadrupole term at n = 30: %.6f; measured %.5f +/- %.5f"
                    % (rb["K"], float(rb["six"]), float(rb["rcc"]), float(rb["three"]), float(rb["full"]), float(rb["meas"]), float(rb["unc"])))

    # 3  Theorem 1
    fam3, ok3 = ob_ratio_identity()
    allok &= report("PROVED", "Theorem 1: c2/c0 = -l(l+1)/3", ok3, "%d (n,l,alpha,z) grid points, exact" % fam3)
    FIGURES["ratio_grid"] = fam3
    z3ok, nonvac, compared, disagree = ob_z3()
    allok &= report("MACHINE-CHECKED", "Theorem 1 from its premise, l in {1..8}; alpha, z, n1, n2, n3 real", z3ok and nonvac and disagree == 0,
                    "8 obligations unsat; non-vacuity %s; encoding vs Laguerre integral: %d compared (seed %d), %d disagree"
                    % ("ok" if nonvac else "FAIL", compared, Z3_SEED, disagree))
    q3ok, qnonvac, qcmp, qdis = ob_z3_quadrupole()
    allok &= report("MACHINE-CHECKED", "Lemma 4: a positive quadrupole term puts the ratio below -l(l+1)/3, l in {2..8}", q3ok and qnonvac and qdis == 0,
                    "7 obligations unsat; non-vacuity %s; encoding %d compared (seed %d), %d disagree"
                    % ("ok" if qnonvac else "FAIL", qcmp, Z3_SEED, qdis))

    # 4  p, and where p and l part company
    okp, same, table = ob_p_table()
    allok &= report("EXHAUSTIVE", "D3: p for the four cores from the ground configurations", okp,
                    "; ".join("%s %s" % (sp, [table[sp][l] for l in range(4)]) for sp in table))
    allok &= report("EXHAUSTIVE", "on these cores p = 0 iff l >= 3, over l in {0,1,2,3}", same, "16 (core, l) cells")
    ar_d, kr_d, d0cores, fcores, rng, ng = ob_separating_cores()
    allok &= report("EXHAUSTIVE", "cores that separate p from l, over every core in the configuration table",
                    ar_d == 0 and kr_d == 1 and ng == 0 and min(fcores) == 58 and d0cores == list(range(1, 21)),
                    "table covers %d-%d electrons; p = 0 at l = 2 for %d-%d electrons (argon-like 18 e: %d; krypton-like 36 e: %d); "
                    "p >= 1 at l = 3 from %d electrons upward (%d cores); %d cores hold a g orbital"
                    % (rng[0], rng[1], min(d0cores), max(d0cores), ar_d, kr_d, min(fcores), len(fcores), ng))

    # 5  the fits
    rows = run_fits()
    FIGURES["rows"] = rows
    allok &= report("MEASURED", "thirteen series loaded", len(rows) == 13, "%d series, %d levels" % (len(rows), sum(r["members"] for r in rows)))
    FIGURES["levels_total"] = sum(r["members"] for r in rows)
    _, Rinf_v, mp_v = load_series()
    pop_c = _load("populate", POPULATE)
    print()
    print("      Table 1 -- R_inf = %s cm^-1, m_p/m_e = %s; R_M = R_inf / (1 + 1/(A m_p/m_e))" % (Rinf_v, mp_v))
    print("      %-9s %-22s %2s %2s %2s %6s %3s %12s %8s %12s" %
          ("series", "core ground config", "l", "p", "z", "n", "N", "I (cm^-1)", "A", "R_M (cm^-1)"))
    cfgmap = {"Cd I": 47, "In I": 48, "Rb I": 36, "Sr II": 36}
    cfgtxt = {}
    for sp, ne in cfgmap.items():
        cfg = pop_c.config_of(ne, "observed")
        cfgtxt[sp] = " ".join("%d%s%d" % (n, "spdfg"[l], o) for n, l, o in cfg)
    short = {sp: (t.replace("1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6", "[Kr]")) for sp, t in cfgtxt.items()}
    for r in sorted(rows, key=lambda r: (r["p"], r["l"], r["name"])):
        print("      %-9s %-22s %2d %2d %2d %2d-%-3d %3d %12.3f %8s %12.3f" %
              (r["name"], short[r["species"]], r["l"], r["p"], r["c"], r["n_lo"], r["n_hi"], r["members"],
               r["lim"], r["A"], r["RM"]))
    print("      core ground configurations in full:")
    for sp in sorted(cfgtxt):
        print("        %-6s (%d electrons)  %s" % (sp, cfgmap[sp], cfgtxt[sp]))
    print()
    print("      Table 2 -- every level as NIST quotes it (the one level absent from the captures printed as held):")
    for r in sorted(rows, key=lambda r: r["name"]):
        q = quoted_levels(r["species"])
        cells = ["%d %s" % (n, q.get((n, r["lsym"], E), "%.3f" % E)) for n, E in sorted(r["levels"].items())]
        print("        %-8s %s" % (r["name"] + ":", "; ".join(cells)))
    certs = all(r["certified"] for r in rows)
    bmin = min(r["basins"] for r in rows); bmax = max(r["basins"] for r in rows)
    allok &= report("MEASURED", "each least-squares minimiser certified", certs and bmin == 1 and bmax == 1,
                    "401-point exact scan on [min d - 1, min(max d + 1, n_min - 1/2)] + 90 ternary steps; bracket width <= %.1e; local minima per scan: min %d, max %d"
                    % (max(r["width"] for r in rows), bmin, bmax))
    print()
    print("      %-9s %2s %2s %5s %3s %10s %10s %10s %9s %9s %10s %8s" % ("series", "l", "p", "n", "N", "d0", "d2", "d2/d0", "Seaton", "rho", "rms", "alpha"))
    for r in sorted(rows, key=lambda r: (r["p"], r["l"], r["name"])):
        alpha = ("%8.2f" % float(r["d0"] * K(r["l"]) / (6 * r["c"] ** 2))) if r["p"] == 0 else "       -"
        print("      %-9s %2d %2d %2d-%-2d %3d %10.4f %10.4f %10.4f %9.3f %9s %10.5f %s"
              % (r["name"], r["l"], r["p"], r["n_lo"], r["n_hi"], r["members"], r["d0"], r["d2"], r["d2"] / r["d0"],
                 float(r["seat"]), ("%.3f" % r["rho"]) if r["rho"] is not None else "undef", r["rms"], alpha))
    print("      alpha: the dipole polarisability (a0^3) the fitted d0 implies through Theorem 1, d0 K(l) / (6 z^2)")
    print()
    ngn = 0
    for r in rows:
        g0, g2, it = gauss_newton(r["pts"])
        if round(g0, 4) == round(float(r["d0"]), 4) and round(g2, 4) == round(float(r["d2"]), 4):
            ngn += 1
        else:
            print("        Gauss-Newton disagrees on %s: %.6f %.6f vs %.6f %.6f" % (r["name"], g0, g2, float(r["d0"]), float(r["d2"])))
    allok &= report("CROSS-CHECK", "Gauss-Newton (float, unprofiled) agrees with the exact profile fit to 4 dp", ngn == 13,
                    "%d of 13 series, 26 coefficients" % ngn)
    nsrc = 0
    for r in rows:
        s0, s2 = SOURCE_FIT[r["name"]]
        if abs(r4(r["d0"]) - s0) <= 0.00011 and abs(r4(r["d2"]) - s2) <= 0.00011:
            nsrc += 1
    allok &= report("SOURCE", "fits agree with the source's printed (d0, d2) to 4 dp", nsrc == 13, "%d of 13" % nsrc)

    # 6  the statistics
    st = stats(rows)
    FIGURES["stats"] = st
    allok &= report("MEASURED", "class sizes", st["p0_series"] == 3 and st["p1_series"] == 10,
                    "p = 0: %d series; p >= 1: %d series" % (st["p0_series"], st["p1_series"]))
    allok &= report("MEASURED", "ratios defined", st["p0_defined"] == 3 and st["p1_defined"] == 6,
                    "p = 0: %d; p >= 1: %d (the four l = 0 series have the polarisation value 0, rho undefined)"
                    % (st["p0_defined"], st["p1_defined"]))
    line = "p = 0: median %.3f, sd %.3f (mean %.3f, sample sd %.3f); p >= 1: median %.3f, sd %.3f (mean %.3f, sample sd %.3f)" % (
        st["p0_median"], st["p0_sd"], st["p0_mean"], st["p0_ssd"], st["p1_median"], st["p1_sd"], st["p1_mean"], st["p1_ssd"])
    okst = (r3(st["p0_median"]) == SOURCE_STAT["p0_median"] and r3(st["p0_sd"]) == SOURCE_STAT["p0_sd"]
            and r3(st["p1_median"]) == SOURCE_STAT["p1_median"] and r3(st["p1_sd"]) == SOURCE_STAT["p1_sd"])
    allok &= report("SOURCE", "the four statistics reproduce (median, population sd)", okst, line)
    print("        p = 0 ratios: %s" % ", ".join("%.3f" % x for x in st["p0_rho"]))
    print("        p >= 1 ratios: %s" % ", ".join("%.3f" % x for x in st["p1_rho"]))
    print("        leave-one-out medians, p = 0: %s" % ", ".join("%.3f" % x for x in st["p0_loo"]))
    print("        with a 1/n^2 denominator instead of 1/(n-d0)^2: p = 0 median %.3f sd %.3f; p >= 1 median %.3f sd %.3f"
          % (st["p0_median_n2"], st["p0_sd_n2"], st["p1_median_n2"], st["p1_sd_n2"]))
    sign = st["sign"]
    print("        sign of d2 by p: %s" % "; ".join("p=%d %d+ %d-" % (p, sign[p][0], sign[p][1]) for p in sorted(sign)))
    signok = sign[0] == [0, 3] and sign[5] == [2, 0] and sign[4] == [2, 0] and all(sign[p] == [1, 1] for p in (1, 2, 3))
    allok &= report("EXHAUSTIVE", "sign rule: 0 of 3 positive at p = 0; 2 of 2 at p = 4 and 5; 1 of 2 at p = 1, 2, 3", signok, "13 series, six values of p")
    fr = [sign[p][0] / sum(sign[p]) for p in sorted(sign)]
    allok &= report("MEASURED", "positive fraction non-decreasing in p", all(a <= b for a, b in zip(fr, fr[1:])),
                    " ".join("%.2f" % f for f in fr))

    # 7  sensitivities of the p = 0 ratios
    sens = ob_sensitivity()
    for s_ in sens:
        extra = ("; limit -0.13/+0.13 cm^-1: rho %.3f / %.3f" % s_["lim_pm"]) if "lim_pm" in s_ else ""
        print("        %-8s rho %.3f; lowest member out: %.3f; quotation floor (h = %s): sum |d rho| = %.4f; limit +0.1 cm^-1: d rho = %+.4f%s; implied alpha %.2f a0^3"
              % (s_["name"], s_["rho"], s_["loo"], "/".join(sorted(set("%g" % h for h in s_["hs"]))), s_["floor"], s_["dlim"], extra, s_["alpha"]))
    allok &= report("MEASURED", "p = 0 sensitivities: lowest member out, quotation floor, limit", len(sens) == 3,
                    "lowest-out rho %s; floor sums %s" % (", ".join("%.3f" % s_["loo"] for s_ in sens), ", ".join("%.4f" % s_["floor"] for s_ in sens)))
    FIGURES["sens"] = sens

    ind = [r for r in rows if r["name"] == "In I d"][0]
    ind_ds = [float(d) for _, d in ind["pts"]]
    rising = all(a < b for a, b in zip(ind_ds, ind_ds[1:]))
    allok &= report("MEASURED", "In I d: the one series whose residual is an order above the rest", rising,
                    "rms %.5f against %.5f next largest; defect rises monotonically %.2f (n=%d) to %.2f (n=%d)"
                    % (ind["rms"], max(r["rms"] for r in rows if r["name"] != "In I d"),
                       ind_ds[0], ind["n_lo"], ind_ds[-1], ind["n_hi"]))
    nl, worst = ob_limit_sensitivity()
    pubs, ok_alpha, dd0, rd2, ok_rb = ob_published(rows)
    allok &= report("MEASURED", "5.7: implied polarisabilities against published values (CITED), and doubled under 3/K", ok_alpha,
                    "; ".join("%s %.2f: ratios %s, under 3/K %s" % (n, float(v["implied"]),
                              ", ".join("%.3f" % float(x) for x in v["ratios"]), ", ".join("%.2f" % float(x) for x in v["ratios3"]))
                              for n, v in pubs.items()))
    allok &= report("MEASURED", "5.7: Rb I fits against the published 85Rb Rydberg-Ritz coefficients (CITED)", ok_rb,
                    "d0 - published: " + ", ".join("%s %+.4f" % (k, float(v)) for k, v in dd0.items())
                    + "; d2 relative: " + ", ".join("%s %+.1f%%" % (k, 100 * float(v)) for k, v in rd2.items()))
    allok &= report("MEASURED", "limit sensitivity: d(delta) = n*^3 dI / (2 z^2 R_M)", worst < 1e-4,
                    "%d levels, dI = 0.01 cm^-1, worst relative error %.2e" % (nl, worst))

    # 8  the levels against the capture files, and Cd I against the channel table
    print()
    tot, missing = ob_captures(rows)
    expected_missing = [("Cd I p", 5, 43692.384)]
    allok &= report("EXHAUSTIVE", "levels occur in the species' NIST capture files", missing == expected_missing,
                    "%d levels, %d found; not held: %s" % (tot, tot - len(missing), ", ".join("%s n=%d %.3f" % m for m in missing)))
    FIGURES["capture_found"] = tot - len(missing)
    for r in rows:
        if r["species"] != "Cd I":
            continue
        row = SOURCE_CDI[r["lsym"]]
        ds = [float(d) for _, d in r["pts"]]
        med, mean = statistics.median(ds), sum(ds) / len(ds)
        same_range = (r["n_lo"], r["n_hi"]) == row[1] and r["members"] == row[2]
        note = "n %d-%d, %d members: median %.4f, mean %.4f; channel table %s n %d-%d, %d members, %.4f%s" % (
            r["n_lo"], r["n_hi"], r["members"], med, mean, row[0], row[1][0], row[1][1], row[2], row[3],
            "" if same_range else " (different n-range)")
        if same_range:
            okmean = abs(round(mean, 4) - row[3]) <= 0.00011
            okmed = abs(round(med, 4) - row[3]) <= 0.00011
            allok &= report("SOURCE", "Cd I %s: the channel table's delta is the MEAN of these members" % r["lsym"],
                            okmean, note + "; median %s, mean %s" % ("agrees" if okmed else "differs", "agrees" if okmean else "differs"))
        else:
            print("        Cd I %s: %s" % (r["lsym"], note))

    # -- selftest: negative controls
    if selftest:
        print()
        print("  negative controls (each must be REFUTED):")
        fam, bad = ob_r4(nmax=8, wrong=True)
        allok &= report("REFUTED", "control: wrong <r^-4> (3n^2 + l(l+1)) fails the family", bad > 0, "%d of %d disagree" % (bad, fam))
        ptsw, okw = ob_defect_rearrangement(wrong=True)
        allok &= report("REFUTED", "control: Lemma 2's factor without the 2, (n-d)^2/(n(2n-d)), fails", not okw,
                        "fails at grid point %d" % ptsw)
        z3ok, nonvac, _, _ = ob_z3(lmax=3, wrong=True)
        allok &= report("REFUTED", "control: Z3 finds a model against c2/c0 = -2l(l+1)/3", not z3ok, "sat, as it must be")
        rows_p = run_fits(perturb=("Cd I f", 4, 5.0))
        stp = stats(rows_p)
        moved = r3(stp["p0_median"]) != SOURCE_STAT["p0_median"] or r3(stp["p0_sd"]) != SOURCE_STAT["p0_sd"]
        allok &= report("REFUTED", "control: Cd I 4f raised by 5 cm^-1 moves the p = 0 statistic", moved,
                        "median %.3f sd %.3f" % (stp["p0_median"], stp["p0_sd"]))
        rbw = ob_prefactor_rb(wrong=True)
        allok &= report("REFUTED", "control: the 3a/K(4) prefactor carried through the Rb ng arithmetic misses the measurement", not rbw["ok"],
                        "gives %.6f against %.5f +/- %.5f" % (float(rbw["full"]), float(rbw["meas"]), float(rbw["unc"])))

    print()
    n = len(RESULTS)
    nok = sum(1 for r in RESULTS if r[2])
    by = {}
    for r in RESULTS:
        by[r[0]] = by.get(r[0], 0) + 1
    print("%d of %d obligations discharged%s  (%s)" % (nok, n, "" if allok else " -- FAILURES ABOVE",
                                                       ", ".join("%s %d" % kv for kv in sorted(by.items()))))
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main("--selftest" in sys.argv))
