#!/usr/bin/env python3
"""check.py -- the machine checks behind PAPER.md (paper 03, the bracket).

Every number the paper prints is produced here, and every decidable claim is
discharged here, in one of four ways:

  PROVED / exact grid    an identity in Fraction arithmetic, checked on a rational
                         grid exceeding its degree in every variable, so a residual
                         that vanishes is a proof and not a sample (the method of
                         research/warp-drive/proofs.py, imported by path)
  MACHINE-CHECKED        Z3 returns `unsat` on the negation of an obligation over
                         linear real arithmetic; both guards run first (non-vacuity
                         of the hypothesis, encoding fidelity against an independent
                         concrete implementation with a negative control)
  EXHAUSTIVE             every case of a stated finite family visited
  MEASURED               computed from the level tables held in the tree, with the
                         seated instrument imported by path as the object under test
                         and an independent implementation of the rule as its reference
  ARITHMETIC             a proved closed form evaluated at stated points and printed to
                         a stated precision (floating point, or a float rendering of an
                         exact value); it carries no proof status of its own -- the
                         status is the theorem's -- and is never counted as PROVED
  GUARD                  a precondition of a MACHINE-CHECKED or MEASURED row; if a guard
                         fails, the rows it guards are reported as failed, not as ok

    python3 check.py              every obligation, one line each, summary, exit 1 on failure
    python3 check.py --selftest   the same plus the negative controls
    python3 check.py --json       also writes results.json for figures.py

Stdlib + z3 only. Python 3.12 (export PATH="$PWD/method/bin:$PATH").
"""
import glob
import importlib.util
import itertools
import json
import math
import os
import random
import re
import statistics
import sys
from decimal import Decimal, localcontext
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

try:
    import z3
except ImportError:                                            # pragma: no cover
    print("check.py needs z3:  pip install z3-solver")
    sys.exit(2)


def load_by_path(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


PROOFS = load_by_path("proofs", "research/warp-drive/proofs.py")       # rational_grid, verify
RULED = load_by_path("ruled_bracket", "method/members/ruled_bracket.py")  # the seated test

R_INF = F("109737.31568")          # cm^-1, CODATA 2018 (Tiesinga et al. 2021)
R_FLOAT = 109737.31568
R_EV = 13.605693122994             # eV, the Rydberg energy R_inf h c, CODATA 2018
R_HARTREE = 0.5                    # hartree, exact

# ------------------------------------------------------------------ bookkeeping

ROWS = []          # (id, status, ok, label, detail)
NUMS = {}          # every number the paper prints, by name
FAILS = []


def ob(oid, status, ok, label, detail=""):
    ROWS.append((oid, status, bool(ok), label, detail))
    if not ok:
        FAILS.append(oid)
    print("  [%s] %-6s %-14s %s%s" % ("ok" if ok else "XX", oid, status, label,
                                     ("  -- " + detail) if detail else ""))


def num(name, value):
    NUMS[name] = value
    return value


def grid_identity(oid, label, bounds, order, resid):
    """A polynomial identity, exact on a rational grid above its degree."""
    n, ok = PROOFS.verify((oid, "", "", [], bounds, resid, order))
    ob(oid, "PROVED", ok, label, "exact on %d rational grid points, degrees %s"
       % (n, ", ".join("%s<=%d" % (v, bounds[v]) for v in order)))
    return ok


# ------------------------------------------------------------------ the objects

def T(A, nu):
    """The Rydberg term Z^2 R / nu^2, with A = Z^2 R carried as one variable."""
    return A / (nu * nu)


def w_e(A, nu, h):
    """Bracket width and linear-interpolation error at (nu-h, nu, nu+h)."""
    lo, mid, hi = T(A, nu - h), T(A, nu), T(A, nu + h)
    w = lo - hi
    e = (lo + hi) / 2 - mid
    return w, e


def V_exact(r):
    """V as a function of r = nu/h."""
    return 4 * r ** 3 / (3 * r * r - 1)


# =============================================================================
# PART 1 -- identities, exact
# =============================================================================

def part1():
    print("\n1. THE COST SURFACE -- exact identities (Fraction, grid above degree)")

    # T1: w and e in closed form
    grid_identity("I1", "w = 4 A nu h / (nu^2 - h^2)^2",
                  {"A": 2, "nu": 8, "h": 8}, ("A", "nu", "h"),
                  lambda A, nu, h: w_e(A, nu, h)[0] * (nu * nu - h * h) ** 2 - 4 * A * nu * h)
    grid_identity("I2", "e = A h^2 (3 nu^2 - h^2) / (nu^2 (nu^2 - h^2)^2)",
                  {"A": 2, "nu": 10, "h": 8}, ("A", "nu", "h"),
                  lambda A, nu, h: w_e(A, nu, h)[1] * nu * nu * (nu * nu - h * h) ** 2
                  - A * h * h * (3 * nu * nu - h * h))
    # T1: V exact, Z and R cancel
    grid_identity("I3", "V = w/e = 4 nu^3 / (h (3 nu^2 - h^2)); A = Z^2 R cancels",
                  {"A": 2, "nu": 10, "h": 8}, ("A", "nu", "h"),
                  lambda A, nu, h: (lambda w, e: w * h * (3 * nu * nu - h * h) - 4 * nu ** 3 * e)(*w_e(A, nu, h)))
    # Corollary: an additive constant and a scale leave V unchanged (y = a + b/x^2)
    def resid_affine(a, b, nu, h):
        y = lambda x: a + b / (x * x)
        w = y(nu - h) - y(nu + h)
        e = (y(nu - h) + y(nu + h)) / 2 - y(nu)
        return w * h * (3 * nu * nu - h * h) - 4 * nu ** 3 * e
    grid_identity("I4", "y = a + b/x^2 has the same exact V (delta-bracket = T-bracket price)",
                  {"a": 2, "b": 2, "nu": 10, "h": 8}, ("a", "b", "nu", "h"), resid_affine)
    # asymptote with exact remainder
    grid_identity("I5", "V(r) = 4r/3 + 4/(9r) + 4/(9 r (3r^2 - 1))",
                  {"r": 6}, ("r",),
                  lambda r: V_exact(r) - (4 * r / 3 + 4 / (9 * r) + 4 / (9 * r * (3 * r * r - 1))))
    # monotonicity of V in r: the difference identity
    grid_identity("I6", "V(r2) - V(r1) = 4 (r2 - r1)(3 r1^2 r2^2 - r1^2 - r1 r2 - r2^2) / ((3r1^2-1)(3r2^2-1))",
                  {"r1": 6, "r2": 6}, ("r1", "r2"),
                  lambda r1, r2: (V_exact(r2) - V_exact(r1)) * (3 * r1 * r1 - 1) * (3 * r2 * r2 - 1)
                  - 4 * (r2 - r1) * (3 * r1 * r1 * r2 * r2 - r1 * r1 - r1 * r2 - r2 * r2))
    # the fractional forms
    def resid_wT(A, nu, h):
        w, e = w_e(A, nu, h)
        s = h / nu
        return w / T(A, nu) - 4 * s / (1 - s * s) ** 2
    def resid_eT(A, nu, h):
        w, e = w_e(A, nu, h)
        s = h / nu
        return e / T(A, nu) - s * s * (3 - s * s) / (1 - s * s) ** 2
    grid_identity("I7", "w/T = 4s/(1-s^2)^2, s = h/nu", {"A": 2, "nu": 10, "h": 8}, ("A", "nu", "h"), resid_wT)
    grid_identity("I8", "e/T = s^2 (3 - s^2)/(1-s^2)^2", {"A": 2, "nu": 10, "h": 8}, ("A", "nu", "h"), resid_eT)

    # the floor: exact values and the minimum over the family r >= 2
    vals = {nu: V_exact(F(nu)) for nu in (2, 3, 4, 5, 10)}
    want = {2: F(32, 11), 3: F(54, 13), 4: F(256, 47), 5: F(250, 37), 10: F(4000, 299)}
    ob("I9", "PROVED", vals == want, "V at nu = 2,3,4,5,10 (h=1) is 32/11, 54/13, 256/47, 250/37, 4000/299 exactly")
    fam = [(nu, h) for h in range(1, 5) for nu in range(2 * h, 401)]
    vmin = min(V_exact(F(nu, h)) for nu, h in fam)
    ob("I10", "EXHAUSTIVE", vmin == F(32, 11),
       "min V over every (nu, h) with h = 1..4, nu = 2h..400 is 32/11", "%d cases" % len(fam))
    num("V_floor", F(32, 11)); num("V_floor_f", float(F(32, 11)))
    num("V_floor_asym_2", F(26, 9))
    low = 1 - F(26, 9) / F(32, 11)
    num("asym_low_pct_at_2", float(low) * 100)
    ob("I11", "PROVED", low == F(1, 144),
       "asymptote 4r/3 + 4/(9r) at nu = 2 is 26/9, low by exactly 1/144 = %.3f%%" % (float(low) * 100))
    d10 = V_exact(F(10)) - (F(40, 3) + F(4, 90))
    num("asym_gap_at_10", float(d10))
    ob("I12", "PROVED", d10 == F(4, 9 * 10 * 299) and F(1, 10000) < d10 < F(1, 1000),
       "gap at nu = 10 is exactly 4/26910 = %.2e, between 10^-4 and 10^-3: exact to three decimals, not four" % float(d10))
    num("V_20", float(V_exact(F(20)))); num("V_10", float(V_exact(F(10)))); num("V_40", float(V_exact(F(40))))
    # depth and step interchangeable
    same = {V_exact(F(nu, h)) for nu, h in ((20, 1), (40, 2), (60, 3), (80, 4))}
    same10 = {V_exact(F(nu, h)) for nu, h in ((10, 1), (40, 4))}
    ob("I13", "PROVED", len(same) == 1 and len(same10) == 1,
       "V(20,1) = V(40,2) = V(60,3) = V(80,4) = %.6f ; V(10,1) = V(40,4) = %.6f"
       % (float(V_exact(F(20))), float(V_exact(F(10)))))
    # fractional-form table
    tab = []
    for nu, h in ((20, 1), (40, 1), (40, 2)):
        w, e = w_e(R_INF, F(nu), F(h))
        tab.append((nu, h, float(w / T(R_INF, F(nu))), 4 * h / nu, float(e / T(R_INF, F(nu))), 3 * (h / nu) ** 2))
    num("frac_table", tab)
    ob("I14", "ARITHMETIC", all(abs(a - b) < 2e-3 and abs(c - d) < 4e-5 for _, _, a, b, c, d in tab),
       "fractional forms at (20,1), (40,1), (40,2): w/T = %.6f, e/T = %.3e at (20,1)" % (tab[0][2], tab[0][4]))

    # the bits
    num("bits_10", math.log2(float(V_exact(F(10))))); num("bits_40", math.log2(float(V_exact(F(40)))))
    num("bits_floor", math.log2(32 / 11))
    ob("I15", "ARITHMETIC", abs(NUMS["bits_10"] - 3.742) < 1e-3 and abs(NUMS["bits_40"] - 5.737) < 1e-3
       and abs(NUMS["bits_floor"] - 1.5406) < 1e-4,
       "log2 V = %.3f bits at nu = 10, %.3f at nu = 40; log2(32/11) = %.4f" % (NUMS["bits_10"], NUMS["bits_40"], NUMS["bits_floor"]))


# =============================================================================
# PART 2 -- Newton decrement, self-concordance, Aitken, the gaps
# =============================================================================

def part2():
    print("\n2. THE DECREMENT, THE GAPS, AITKEN -- exact")
    Tp = lambda A, nu: -2 * A / nu ** 3
    Tpp = lambda A, nu: 6 * A / nu ** 4
    Tppp = lambda A, nu: -24 * A / nu ** 5
    grid_identity("I16", "lambda^2 = (T')^2 / T'' = (2/3) T", {"A": 2, "nu": 8}, ("A", "nu"),
                  lambda A, nu: Tp(A, nu) ** 2 - F(2, 3) * T(A, nu) * Tpp(A, nu))
    # Newton step decrease = lambda^2 / 2
    def resid_newton(A, nu):
        t = -Tp(A, nu) / Tpp(A, nu)
        model_drop = -(Tp(A, nu) * t + Tpp(A, nu) * t * t / 2)
        return model_drop - Tp(A, nu) ** 2 / (2 * Tpp(A, nu))
    grid_identity("I17", "the quadratic model falls by lambda^2/2 under a full Newton step",
                  {"A": 2, "nu": 8}, ("A", "nu"), resid_newton)
    num("lam2_10", float(F(2, 3) * T(R_INF, F(10)))); num("lam2_100", float(F(2, 3) * T(R_INF, F(100))))
    ob("I18", "ARITHMETIC", abs(NUMS["lam2_10"] - 731.5821) < 1e-3 and abs(NUMS["lam2_100"] - 7.31582) < 1e-4,
       "lambda^2 = %.4f cm^-1 at nu = 10, %.4f at nu = 100 (Z = 1)" % (NUMS["lam2_10"], NUMS["lam2_100"]))
    # self-concordance: 4 (T'')^3 - (T''')^2 = (576 A^2 / nu^12) (3A/2 - nu^2)
    grid_identity("I19", "4(T'')^3 - (T''')^2 = (576 A^2/nu^12)(3A/2 - nu^2): self-concordant iff nu^2 <= 3A/2",
                  {"A": 4, "nu": 14}, ("A", "nu"),
                  lambda A, nu: 4 * Tpp(A, nu) ** 3 - Tppp(A, nu) ** 2 - 576 * A * A / nu ** 12 * (F(3, 2) * A - nu * nu))
    # the squared ratio is nu^2 / (3A/2): the self-concordance ratio scales as A^(-1/2), i.e. with the unit
    grid_identity("I19b", "(T''')^2 / (4 (T'')^3) = nu^2 / (3A/2): the ratio |T'''|/(2 (T'')^(3/2)) is nu / sqrt(3A/2), not unit-free",
                  {"A": 4, "nu": 14}, ("A", "nu"),
                  lambda A, nu: Tppp(A, nu) ** 2 * (F(3, 2) * A) - 4 * Tpp(A, nu) ** 3 * nu * nu)
    sc = {Z: math.sqrt(1.5 * Z * Z * R_FLOAT) for Z in (1, 2, 6)}
    num("sc_bounds", sc)
    sc_units = {"cm^-1": math.sqrt(1.5 * R_FLOAT), "eV": math.sqrt(1.5 * R_EV), "hartree": math.sqrt(1.5 * R_HARTREE)}
    num("sc_bound_units", sc_units)
    ratio55 = (24 * R_FLOAT / 55 ** 5) / (2 * (6 * R_FLOAT / 55 ** 4) ** 1.5)
    ratio2 = (24 * R_FLOAT / 2 ** 5) / (2 * (6 * R_FLOAT / 2 ** 4) ** 1.5)
    num("sc_ratio_55", ratio55); num("sc_ratio_2", ratio2)
    ob("I20", "ARITHMETIC", abs(sc[1] - 405.7) < 0.1 and abs(sc[2] - 811.4) < 0.1 and abs(sc[6] - 2434.2) < 0.2
       and abs(ratio55 - 0.1356) < 1e-3 and abs(sc_units["hartree"] - math.sqrt(0.75)) < 1e-12,
       "nu <= sqrt(3A/2) with R in cm^-1: %.1f (Z=1), %.1f (Z=2), %.1f (Z=6); the same bound at Z = 1 with R in eV: %.2f, in hartree: %.3f; ratio |T'''|/2(T'')^1.5 in cm^-1 = %.4f at nu = 2, %.4f at nu = 55"
       % (sc[1], sc[2], sc[6], sc_units["eV"], sc_units["hartree"], ratio2, ratio55))
    # the two gaps and the derivative between them
    gp = lambda A, nu: T(A, nu) - T(A, nu + 1)
    gm = lambda A, nu: T(A, nu - 1) - T(A, nu)
    grid_identity("I21", "g+ = A(2nu+1)/(nu^2 (nu+1)^2), g- = A(2nu-1)/(nu^2 (nu-1)^2)",
                  {"A": 2, "nu": 8}, ("A", "nu"),
                  lambda A, nu: (gp(A, nu) - A * (2 * nu + 1) / (nu * nu * (nu + 1) ** 2)) ** 2
                  + (gm(A, nu) - A * (2 * nu - 1) / (nu * nu * (nu - 1) ** 2)) ** 2)
    # sandwich, exhaustive on integers and on the rational grid (proof in text)
    D = lambda A, nu: 2 * A / nu ** 3
    fam = [F(k, 4) for k in range(5, 801)]            # nu = 1.25 .. 200 step 1/4
    okk = all(gp(F(1), nu) < D(F(1), nu) < gm(F(1), nu) for nu in fam)
    ob("I22", "EXHAUSTIVE", okk, "g+ < 2A/nu^3 < g- at every nu in {5/4, 6/4, ..., 200}", "%d cases" % len(fam))
    # and w/2 against D: w/2 = D (1 + 3 s^2 + ...) exactly w/2 = 2 A nu h/(nu^2-h^2)^2
    ob("I23", "EXHAUSTIVE", all(w_e(F(1), nu, F(1))[0] / 2 > D(F(1), nu) for nu in fam),
       "w/2 > 2A/nu^3 at every nu in {5/4, 6/4, ..., 200} (the general statement follows from I24)", "%d cases" % len(fam))
    grid_identity("I24", "w/2 = h (2A/nu^3) / (1 - h^2/nu^2)^2", {"A": 2, "nu": 8, "h": 8}, ("A", "nu", "h"),
                  lambda A, nu, h: w_e(A, nu, h)[0] / 2 - h * (2 * A / nu ** 3) / (1 - h * h / (nu * nu)) ** 2)
    # the two gaps at step h against w and e: the larger gap is w/2 + e, the smaller w/2 - e
    def resid_gaps(A, nu, h):
        w, e = w_e(A, nu, h)
        gminus = T(A, nu - h) - T(A, nu); gplus = T(A, nu) - T(A, nu + h)
        return (gminus - (w / 2 + e)) ** 2 + (gplus - (w / 2 - e)) ** 2 + (gminus - A * h * (2 * nu - h) / (nu * nu * (nu - h) ** 2)) ** 2
    grid_identity("I39", "g- = w/2 + e = A h (2nu - h)/(nu^2 (nu-h)^2) and g+ = w/2 - e: the larger gap exceeds the half-width by e",
                  {"A": 2, "nu": 10, "h": 8}, ("A", "nu", "h"), resid_gaps)
    grid_identity("I40", "g- = (w/2)(1 + 2/V): the excess of the deductive bound over the half-width is the fraction 2/V",
                  {"A": 2, "nu": 10, "h": 8}, ("A", "nu", "h"),
                  lambda A, nu, h: (lambda w, e: (T(A, nu - h) - T(A, nu)) * w - (w / 2) * (w + 2 * e))(*w_e(A, nu, h)))
    ex = {r: float(2 / V_exact(F(r))) for r in (2, 10, 64)}
    num("bound_excess", ex)
    ob("I41", "ARITHMETIC", abs(ex[2] - 0.6875) < 1e-9 and abs(ex[64] - 0.0234) < 1e-3,
       "2/V, the excess of the larger gap over w/2: %.4f at r = 2 (exactly 11/16), %.4f at r = 10, %.4f at r = 64" % (ex[2], ex[10], ex[64]))
    # critical depth table
    tab = {}
    for dT in (3000, 1000, 100, 10):
        tab[dT] = {Z: (2 * Z * Z * R_FLOAT / dT) ** (1 / 3) for Z in (1, 2)}
    num("nu_fail", tab)
    ob("I25", "ARITHMETIC", abs(tab[3000][1] - 4.18) < 0.01 and abs(tab[3000][2] - 6.64) < 0.01 and abs(tab[10][2] - 44.4) < 0.1,
       "nu_fail = (2Z^2R/|dT|)^(1/3): %.1f/%.1f (3000), %.1f/%.1f (1000), %.1f/%.1f (100), %.1f/%.1f (10) at Z = 1/2"
       % tuple(tab[d][Z] for d in (3000, 1000, 100, 10) for Z in (1, 2)))
    # nu_V
    # D12 at k = 1 reads |Delta^2 T| > 5 * 2^2 q = 20 q; the leading-order second difference is T'' = 6A/nu^4
    # (twice e = 3A/nu^4), so 6A/nu^4 > 20 q  <=>  nu < (3A/(10 q))^(1/4)
    nuV = {q: (3 * R_FLOAT / (10 * q)) ** 0.25 for q in (0.0001, 0.001, 0.01)}
    nuV5 = {q: (3 * R_FLOAT / (5 * q)) ** 0.25 for q in (0.0001, 0.001, 0.01)}    # the e > 5q form, for the record
    num("nu_V", nuV); num("nu_V_5q", nuV5)
    ob("I26", "ARITHMETIC", abs(nuV[0.0001] - 134.7) < 0.1 and abs(nuV[0.001] - 75.7) < 0.1 and abs(nuV[0.01] - 42.6) < 0.1
       and all(abs(nuV5[q] / nuV[q] - 2 ** 0.25) < 1e-9 for q in nuV),
       "nu_V = (3Z^2R/(10q))^(1/4) from D12 at k = 1 (6A/nu^4 > 20q) = %.1f, %.1f, %.1f at q = 10^-4, 10^-3, 10^-2 (Z = 1); the form 3A/nu^4 > 5q would give %.1f, %.1f, %.1f, larger by 2^(1/4)"
       % (nuV[0.0001], nuV[0.001], nuV[0.01], nuV5[0.0001], nuV5[0.001], nuV5[0.01]))
    # Aitken on the centred triple: closed form and the limit T/3
    def aitken(A, n):
        a, b, c = T(A, n - 1), T(A, n), T(A, n + 1)
        return a - (b - a) ** 2 / (c - 2 * b + a)
    grid_identity("I27", "Aitken on (n-1, n, n+1) = T(n) (2n^2 - 1)/(6n^2 - 2)", {"A": 2, "n": 10}, ("A", "n"),
                  lambda A, n: aitken(A, n) - T(A, n) * (2 * n * n - 1) / (6 * n * n - 2))
    tab = [(n, float(T(R_INF, F(n))), float(aitken(R_INF, F(n))), float(T(R_INF, F(n)) / 3)) for n in (10, 20, 40, 80)]
    num("aitken_table", tab)
    ob("I28", "ARITHMETIC", abs(tab[0][2] - 365.1793) < 1e-4 and abs(tab[1][2] - 91.4096) < 1e-4,
       "Aitken (n, T, A-hat, T/3): " + "; ".join("%d %.4f %.4f %.4f" % row for row in tab))
    num("aitken_bias_20", tab[1][1] - tab[1][2]); num("aitken_bias_40", tab[2][1] - tab[2][2])


# =============================================================================
# PART 3 -- power laws, higher order
# =============================================================================

def Vpow(x, p, h):
    """Exact V for y = x^p, integer p (Fraction)."""
    y = lambda t: t ** p if p >= 0 else 1 / t ** (-p)
    lo, mid, hi = y(x - h), y(x), y(x + h)
    w = abs(hi - lo)
    e = abs((lo + hi) / 2 - mid)
    return w / e


def part3():
    print("\n3. POWER LAWS AND HIGHER ORDER")
    x, h = F(20), F(1)
    tab = {}
    for p in (-3, -2, 2, 3, 4, 7, 11):
        tab[p] = (float(Vpow(x, p, h)), float(4 * x / (h * abs(p - 1))))
    tab["11/6"] = ((21 ** (11 / 6) - 19 ** (11 / 6)) / abs((21 ** (11 / 6) + 19 ** (11 / 6)) / 2 - 20 ** (11 / 6)),
                   4 * 20 / (1 * abs(11 / 6 - 1)))
    num("Vpow_20", {str(k): v for k, v in tab.items()})
    dev = max(abs(a / b - 1) for a, b in tab.values())
    num("Vpow_maxdev", 100 * dev)
    order = [11, 7, -3, -2, 4, 3, 2, "11/6"]
    num("Vpow_dev", {str(k): 100 * abs(tab[k][0] / tab[k][1] - 1) for k in tab})
    dev5 = max(NUMS["Vpow_dev"][k] for k in ("-3", "-2", "2", "4", "7"))
    num("Vpow_dev_marked", dev5)
    ob("I29", "EXHAUSTIVE", abs(tab[-2][0] - 26.6889) < 1e-3 and abs(tab[11][0] - 8.18) < 0.01 and 0.02 < dev < 0.025,
       "V at x = 20, h = 1 (p: exact, 4x/(h|p-1|), dev): "
       + "; ".join("%s: %.2f, %.2f, %.2f%%" % (k, tab[k][0], tab[k][1], NUMS["Vpow_dev"][str(k)]) for k in order)
       + "; max deviation %.2f%% at p = 11, %.2f%% over p in {-3,-2,2,4,7}" % (100 * dev, dev5))
    big = {p: float(Vpow(x, p, h)) for p in (50, 300, 10000)}
    num("Vpow_big", big)
    ob("I30", "EXHAUSTIVE", abs(big[50] - 2.39) < 0.01 and abs(big[300] - 2) < 1e-3 and abs(big[10000] - 2) < 1e-6,
       "V at p = 50, 300, 10000: %.2f, %.4f, %.6f -- the exact V tends to 2, the asymptote does not apply" % (big[50], big[300], big[10000]))
    # every V > 2 over an exhaustive family of integer p and x/h
    fam = [(p, xx) for p in range(-8, 30) if p not in (0, 1) for xx in range(2, 41)]
    ok = all(Vpow(F(xx), p, F(1)) > 2 for p, xx in fam)
    ob("I31", "EXHAUSTIVE", ok, "V > 2 for every integer p in [-8, 29] \\ {0, 1}, x = 2..40, h = 1", "%d cases" % len(fam))
    # the second-order coefficient (p-2)(p+1)/12 of hV|p-1|/(4x) - 1, verified as a limit of exact ratios
    ok = True
    for p in (-3, -2, 2, 3, 4, 7, 11):
        c = F((p - 2) * (p + 1), 12)
        est = [(Vpow(F(1000), p, F(1) / k) * (F(1) / k) * abs(p - 1) / 4000 - 1) * (1000 * k) ** 2 for k in (1, 2)]
        if abs(float(est[1] - c)) > 1e-3 or abs(float(est[0] - est[1])) > 4 * abs(float(est[1] - c)) + 1e-6:
            ok = False
    ob("I32", "ARITHMETIC", ok, "hV|p-1|/(4x) = 1 + (p-2)(p+1)/12 (h/x)^2 + O((h/x)^4): coefficient recovered from exact rational values at h/x = 10^-3 (the proof is in the text)")
    # signs of the differences of T
    fam = [(nu, j) for j in range(1, 8) for nu in range(2, 201)]
    def diff(vals):
        return [b - a for a, b in zip(vals, vals[1:])]
    ok = True
    for nu, j in fam:
        vals = [T(F(1), F(nu + i)) for i in range(j + 1)]
        for _ in range(j):
            vals = diff(vals)
        if (vals[0] > 0) != (j % 2 == 0):
            ok = False
    ob("I33", "EXHAUSTIVE", ok, "sign(Delta^j T) = (-1)^j for j = 1..7, nu = 2..200", "%d cases" % len(fam))
    # the ordered bracket: sign of f(nu) - p(nu) is (-1)^(k+1+m), m nodes above
    def lagrange(nodes, vals, x):
        s = F(0)
        for i, xi in enumerate(nodes):
            term = vals[i]
            for j, xj in enumerate(nodes):
                if j != i:
                    term *= (x - xj) / (xi - xj)
            s += term
        return s
    cases = 0; ok = True; contain = 0
    for nu in range(8, 120):
        for k in range(1, 6):
            signs = {}
            for m in range(0, k + 2):
                below = k + 1 - m
                nodes = [F(nu - i) for i in range(below, 0, -1)] + [F(nu + i) for i in range(1, m + 1)]
                vals = [T(F(1), t) for t in nodes]
                err = T(F(1), F(nu)) - lagrange(nodes, vals, F(nu))
                want = 1 if (k + 1 + m) % 2 == 0 else -1
                cases += 1
                if (err > 0) != (want > 0):
                    ok = False
                signs[m] = want
            # two-sided bracket: an m with lower-bound sign and one with upper-bound sign
            if 1 in signs.values() and -1 in signs.values():
                contain += 1
    ob("I34", "EXHAUSTIVE", ok and contain == 112 * 5,
       "ordered bracket: sign(f - p) = (-1)^(k+1+m) at every nu = 8..119, k = 1..5, m = 0..k+1",
       "%d sign checks; %d two-sided brackets, one per (nu, k), automatic since m = 0 and m = 1 have opposite parity" % (cases, contain))
    num("ordered_cases", cases); num("ordered_brackets", contain)
    # the noise bound 2^(k+1)
    ok = all(sum(math.comb(k + 1, i) for i in range(k + 2)) == 2 ** (k + 1) for k in range(0, 12))
    ob("I35", "EXHAUSTIVE", ok, "sum of |binomial| weights of Delta^(k+1) is 2^(k+1), k = 0..11")
    # the synthetic containment test at four defects, and the widths at delta = 0.35
    rows = []
    allok = True
    for d in (F(0), F(35, 100), F(135, 100), F(265, 100)):
        Tn = {n: R_INF / (n - d) ** 2 for n in range(4, 15)}
        held = sum(1 for n in range(5, 14) if min(Tn[n - 1], Tn[n + 1]) <= Tn[n] <= max(Tn[n - 1], Tn[n + 1]))
        rows.append((float(d), 9, held, float(Tn[14]), float(Tn[4])))
        allok &= held == 9
    num("synthetic", rows)
    ob("I36", "EXHAUSTIVE", allok and abs(rows[0][3] - 559.9) < 0.1 and abs(rows[0][4] - 6858.6) < 0.1,
       "containment 36 of 36 at delta = 0, 0.35, 1.35, 2.65 (n = 4..14); energies %.1f to %.1f at delta = 0" % (rows[0][3], rows[0][4]))
    d = F(35, 100)
    Tn = {n: R_INF / (n - d) ** 2 for n in range(3, 14)}
    widths = [float(Tn[n - 1] - Tn[n + 1]) for n in range(5, 13)]      # n = 5..12; the first seven are observed
    ratios = [widths[i + 1] / widths[i] for i in range(6)]              # the six ratios among the seven
    presumed = widths[6] * ratios[-1]                                   # the pattern's guess for n = 12
    true_next = widths[7]
    law = (float(11 - d) / float(12 - d)) ** 3
    num("widths", widths[:7]); num("width_ratios", ratios[:6]); num("width_presumed", presumed)
    num("width_true", true_next); num("width_err_pct", 100 * (true_next - presumed) / true_next); num("width_law_ratio", law)
    ob("I37", "ARITHMETIC", abs(widths[0] - 4799) < 1.5 and abs(presumed - 274.1) < 0.2 and abs(true_next - 281.7) < 0.1 and abs(law - 0.764) < 1e-3,
       "widths at delta = 0.35, n = 5..11: %s; ratios %s; presumed next %.1f, true %.1f (%.2f%% low); the law's ratio %.3f against the last observed %.3f"
       % (", ".join("%.0f" % w for w in widths[:7]), ", ".join("%.3f" % r for r in ratios[:6]), presumed, true_next, NUMS["width_err_pct"], law, ratios[5]))
    # the Sc VI deduction, as arithmetic
    d4, d5, lim, Z = F("1.0057"), F("0.9812"), F(892700), 6
    d2 = (d4 - d5) / (F(1, 16) - F(1, 25)); dinf = d4 - d2 / 16; d6 = dinf + d2 / 36
    E = lambda dd: float(lim - Z * Z * R_INF / (6 - dd) ** 2)
    conv = 2 * d5 - d4
    num("scvi", {"d2": float(d2), "dinf": float(dinf), "d6": float(d6), "E6": E(d6), "E_lo": E(d5), "E_hi": E(dinf),
                 "d_conv": float(conv), "E_hi_conv": E(conv), "width": E(dinf) - E(d5), "width_conv": E(conv) - E(d5)})
    s = NUMS["scvi"]
    ob("I38", "ARITHMETIC", abs(s["d2"] - 1.0889) < 1e-4 and abs(s["E6"] - 736688) < 3 and abs(s["E_lo"] - 735860) < 3 and abs(s["E_hi_conv"] - 737380) < 3,
       "two-point solve: delta2 = %.4f, delta_inf = %.4f, delta(6s) = %.4f; E(6s) = %.0f in [%.0f, %.0f]; with convexity [%.0f, %.0f]"
       % (s["d2"], s["dinf"], s["d6"], s["E6"], s["E_lo"], s["E_hi"], s["E_lo"], s["E_hi_conv"]))


# =============================================================================
# PART 4 -- Z3 obligations over linear real arithmetic, with guards
# =============================================================================

def zmin(a, b):
    return z3.If(a <= b, a, b)


def zmax(a, b):
    return z3.If(a >= b, a, b)


def zabs(a):
    return z3.If(a >= 0, a, -a)


def contained_z3(c, a, b):
    return z3.And(zmin(a, b) <= c, c <= zmax(a, b))


def contained_py(c, a, b):
    lo, hi = sorted((a, b))
    return lo <= c <= hi


GUARDS_OK = {"G1": None, "G2": None}


def z3_prove(oid, label, hyp, concl, vars_):
    failed = [g for g, v in GUARDS_OK.items() if v is not True]
    if failed:
        ob(oid, "MACHINE-CHECKED", False, label, "NOT REPORTED: guard %s failed" % ", ".join(failed))
        return False
    s = z3.Solver()
    s.add(z3.Not(z3.Implies(hyp, concl)))
    r = s.check()
    ok = r == z3.unsat
    ob(oid, "MACHINE-CHECKED", ok, label, "Z3 %s on the negation, %d real variables, linear real arithmetic (complete)" % (r, len(vars_)))
    if r == z3.sat:
        print("        counterexample:", s.model())
    return ok


def part4(selftest=False):
    print("\n4. MACHINE-CHECKED (Z3 %s) -- guards first" % z3.get_version_string())
    I, a, b, c, d = z3.Reals("I a b c d")
    d0, d1 = z3.Reals("d0 d1")
    # guard 1: encoding fidelity of `contained` against an independent implementation
    rnd = random.Random(3)
    bad = tot = 0
    for _ in range(400):
        va, vb, vc = (F(rnd.randint(-50, 50), rnd.randint(1, 7)) for _ in range(3))
        if rnd.random() < 0.2:
            vc = va
        s = z3.Solver()
        s.add(contained_z3(z3.RealVal(str(vc)), z3.RealVal(str(va)), z3.RealVal(str(vb))))
        enc = s.check() == z3.sat
        tot += 1
        bad += enc != contained_py(vc, va, vb)
    GUARDS_OK["G1"] = bad == 0
    ob("G1", "GUARD", bad == 0, "encoding fidelity: z3 `contained` agrees with a sorted-interval implementation", "%d seeded random rational triples (seed 3), %d disagreements" % (tot, bad))
    if selftest:
        wrong = lambda c, a, b: (lambda lo, hi: lo < c < hi)(*sorted((a, b)))     # strict: wrong at the edges
        rnd = random.Random(3); badw = 0
        for _ in range(400):
            va, vb, vc = (F(rnd.randint(-50, 50), rnd.randint(1, 7)) for _ in range(3))
            if rnd.random() < 0.2:
                vc = va
            s = z3.Solver(); s.add(contained_z3(z3.RealVal(str(vc)), z3.RealVal(str(va)), z3.RealVal(str(vb))))
            badw += (s.check() == z3.sat) != wrong(vc, va, vb)
        ob("N1", "NEGATIVE", badw > 0, "negative control: a strict-inequality reference is caught by the guard", "%d disagreements" % badw)
    # guard 2: non-vacuity of every hypothesis
    hyps = {
        "M1": z3.BoolVal(True),
        "M2": z3.And(d0 > 0, d1 > 0, d0 != d1),
        "M3": z3.And(a > c, c > b),
        "M4": z3.Or(z3.And(a >= c, c >= b), z3.And(a <= c, c <= b)),
    }
    allsat = True
    for k, hh in hyps.items():
        s = z3.Solver(); s.add(hh)
        # non-triviality: ask for a model where nothing coincides
        s.add(a != b, a != c, b != c, d0 != d1)
        allsat &= s.check() == z3.sat
    GUARDS_OK["G2"] = allsat
    ob("G2", "GUARD", allsat, "non-vacuity: every hypothesis is satisfiable with all variables distinct")
    # M1 limit-free
    z3_prove("M1", "containment is invariant under T = I - E: min(a,b)<=c<=max(a,b) iff min(I-a,I-b)<=I-c<=max(I-a,I-b)",
             z3.BoolVal(True), contained_z3(c, a, b) == contained_z3(I - c, I - a, I - b), (I, a, b, c))
    # M2 floor
    z3_prove("M2", "V > 2: d0, d1 > 0, d0 != d1 implies 2(d0+d1) > 2|d0-d1|  (so w/e > 2 with w = d0+d1, e = |d0-d1|/2)",
             hyps["M2"], 2 * (d0 + d1) > 2 * zabs(d0 - d1), (d0, d1))
    # M3 failure condition, exact: a > c > b unperturbed, middle displaced by d
    z3_prove("M3", "a > c > b: c + d contained in [b, a] iff -(c - b) <= d <= a - c",
             hyps["M3"], contained_z3(c + d, a, b) == z3.And(-(c - b) <= d, d <= a - c), (a, b, c, d))
    # M4 monotone triple <=> contained
    z3_prove("M4", "a monotone triple is contained, and a contained triple is monotone",
             z3.BoolVal(True), contained_z3(c, a, b) == hyps["M4"], (a, b, c))
    if selftest:
        s = z3.Solver(); s.add(hyps["M2"]); s.add(z3.Not(2 * (d0 + d1) > 3 * zabs(d0 - d1)))
        ob("N2", "NEGATIVE", s.check() == z3.sat, "negative control: the false claim V > 3 is refuted with a witness", str(s.model()) if s.check() == z3.sat else "")


# =============================================================================
# PART 5 -- the data: the strict test on the level tables held in the tree
# =============================================================================

RAW = os.path.join(ROOT, "extracted/archives/restore-point-2-13/spectra_raw")
Q2 = os.path.join(ROOT, "extracted/archives/spectra-levels-store/deliver/queue2")
DRV = os.path.join(ROOT, "drive/The Method Materials")
SIX = {"Bi III": ("BiIII_asd.tsv", "BiIII_asd"), "C I": ("CI_full.tsv", "CI_full"), "Cd II": ("CdII_full.tsv", "CdII_full"),
       "Hg II": ("HgII_full.tsv", "HgII_full"), "N I": ("NI_full.tsv", "NI_full"), "Sc III": ("ScIII_asd.tsv", "ScIII_asd")}
# four level tables of the later intake whose thresholds every channel row of that species states identically
Q2LIM = {"AlI": (48278.480, 1), "GaI": (48387.634, 1), "NaI": (41449.451, 1), "KII": (255072.8, 2)}
SP_MD = os.path.join(ROOT, "method/members/The_Method_1_6___Spectra_Compendium-2.md")


def load_dict(src, key):
    i = src.index(key + " = {"); depth, j = 0, i + len(key) + 3
    while True:
        if src[j] == "{":
            depth += 1
        elif src[j] == "}":
            depth -= 1
            if depth == 0:
                break
        j += 1
    return eval(src[i + len(key) + 3:j + 1])


def load_names():
    return load_dict(open(os.path.join(DRV, "channels.py"), encoding="utf-8").read(), "NAME")


def load_limits():
    src = open(os.path.join(DRV, "channels.py"), encoding="utf-8").read()
    i = src.index("LIM = {"); depth, j = 0, i + 6
    while True:
        if src[j] == "{":
            depth += 1
        elif src[j] == "}":
            depth -= 1
            if depth == 0:
                break
        j += 1
    return eval(src[i + 6:j + 1])


def qfloor(s):
    s = s.strip()
    return 0.5 * 10 ** -(len(s.split(".")[1]) if "." in s else 0)


def load_table(path):
    """Every series (prefix, l, term, J) -> [(n, E, E-as-printed)]. Bracketed (derived) and
    non-numeric entries are not levels and are skipped."""
    ser = {}
    for line in open(path, encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        p = line.rstrip("\n").split("\t")
        if len(p) < 4:
            continue
        mm = re.match(r"^(.*?)(\d+)([spdfghik])$", p[0].strip())
        if not mm:
            continue
        try:
            E = float(p[3])
        except ValueError:
            continue
        ser.setdefault((mm.group(1), mm.group(3), p[1].strip(), p[2].strip()), []).append((int(mm.group(2)), E, p[3].strip()))
    return ser


def ref_series(members, lim, Z):
    """Reference implementation of D8, written from the definition and not from the instrument.
    It differs from the instrument in every mechanical respect: exact decimal arithmetic at 40
    digits (the instrument uses binary floats); the test is taken in quantum-defect space and the
    floor is carried across by the exact inverse of Lemma 2's map (the instrument tests in energy
    space); the floor is read from the decimal exponent of the printed string (the instrument
    counts characters after the point); the admissibility ratio is formed from the level's own
    term T as 2 T sqrt(T) / (q Z sqrt(R)) (the instrument forms 2 Z^2 R / (nu^3 q)); and members
    are addressed by n (the instrument walks list positions).
    Returns (pass, fail, refused, cells) where cells = [(n, nu, verdict, lo, hi, E, q)]."""
    with localcontext() as ctx:
        ctx.prec = 40
        Rd = Decimal("109737.31568"); Id = Decimal(repr(lim)); Zd = Decimal(Z)
        byn = {}
        for n, E, s_ in members:
            s_ = s_.strip()
            Ed = Decimal(s_)
            exp = Ed.as_tuple().exponent
            q = Decimal(5) * Decimal(10) ** (exp - 1)          # half a unit in the last printed place
            byn[n] = (Ed, q)

        def delta_of(n, E):                                    # Lemma 2's map, inverted: E -> delta at fixed n
            return Decimal(n) - Zd * (Rd / (Id - E)).sqrt()

        def energy_of(n, d):                                   # delta -> E at fixed n
            return Id - Zd * Zd * Rd / (Decimal(n) - d) ** 2

        p = f = r = 0; cells = []
        for n in sorted(byn):
            if (n - 1) not in byn or (n + 1) not in byn:
                continue
            E, q = byn[n]
            d_lo = min(delta_of(n - 1, byn[n - 1][0]), delta_of(n + 1, byn[n + 1][0]))
            d_hi = max(delta_of(n - 1, byn[n - 1][0]), delta_of(n + 1, byn[n + 1][0]))
            E_lo, E_hi = energy_of(n, d_hi), energy_of(n, d_lo)   # D5 with the labels ordered: E_lo <= E_hi
            Tn = Id - E
            r_adm = 2 * Tn * Tn.sqrt() / (q * Zd * Rd.sqrt())     # = 2 Z^2 R / (nu^3 q)
            nu = Zd * (Rd / Tn).sqrt()
            if r_adm < 5:
                r += 1; cells.append((n, float(nu), "REFUSED", float(E_lo), float(E_hi), float(E), float(q))); continue
            # D8 in delta space: E >= E_lo - q  <=>  delta(E) <= delta(E_lo - q), delta decreasing in E (Lemma 2);
            # E <= E_hi + q  <=>  delta(E) >= delta(E_hi + q), vacuous when E_hi + q reaches the threshold
            dn = delta_of(n, E)
            ok_low = dn <= delta_of(n, E_lo - q)
            ok_high = True if E_hi + q >= Id else dn >= delta_of(n, E_hi + q)
            if ok_low and ok_high:
                p += 1; cells.append((n, float(nu), "pass", float(E_lo), float(E_hi), float(E), float(q)))
            else:
                f += 1; cells.append((n, float(nu), "FAIL", float(E_lo), float(E_hi), float(E), float(q)))
        return p, f, r, cells


def series_rows():
    rows = {}
    for l in open(SP_MD, encoding="utf-8"):
        if l.startswith("| ") and re.search(r"\| [+-]\d\.\d+(?:e-\d+)? \|", l):
            c = [x.strip() for x in l.strip().strip("|").split("|")]
            rows[(c[0].replace(" *", ""), c[1])] = c
    return rows


def part5(results):
    print("\n5. THE DATA -- the strict test on the level tables held here (obligations E*)")
    LIM = load_limits()
    # ---- the store: every table with a threshold on hand
    store = []      # (label, species, key, members, lim, Z)
    tables = 0; skipped = []
    for path in sorted(glob.glob(os.path.join(RAW, "*.tsv"))):
        nm = os.path.basename(path)[:-4]
        if nm not in LIM:
            skipped.append(nm); continue
        lim, Z = LIM[nm]; tables += 1
        for key, v in load_table(path).items():
            store.append((nm, nm, key, sorted({(n, E, s) for n, E, s in v if E < lim}), lim, Z))
    for sp, (fn, lname) in SIX.items():
        lim, Z = LIM[lname]; tables += 1
        for key, v in load_table(os.path.join(DRV, fn)).items():
            store.append((lname, sp, key, sorted({(n, E, s) for n, E, s in v if E < lim}), lim, Z))
    for nm, (lim, Z) in Q2LIM.items():
        tables += 1
        for key, v in load_table(os.path.join(Q2, nm + ".tsv")).items():
            store.append((nm, nm, key, sorted({(n, E, s) for n, E, s in v if E < lim}), lim, Z))
    q2_all = [f[:-4] for f in os.listdir(Q2) if f.endswith(".tsv")]
    num("tables_used", tables); num("raw_skipped", skipped); num("q2_without_threshold", len(q2_all) - len(Q2LIM))
    NAMES = load_names()
    for sp in SIX:
        NAMES.setdefault(SIX[sp][1], sp)
    for nm in Q2LIM:
        NAMES.setdefault(nm, re.sub(r"([a-z])([IVX])", r"\1 \2", nm))
    spectra_all = {NAMES.get(lname, lname) for lname, *_ in store}
    num("spectra_in_tables", len(spectra_all))
    skipped_levels = [x for x in skipped if x != "QD-CHECK"]
    num("raw_skipped_levels", len(skipped_levels)); num("raw_skipped_other", [x for x in skipped if x == "QD-CHECK"])
    ob("E0", "MEASURED", tables == 86 and "QD-CHECK" in skipped,
       "the collection: %d level tables with a threshold, covering %d distinct spectra; %d level tables and %d cross-check file without a threshold set aside, and %d of a later intake"
       % (tables, len(spectra_all), len(skipped_levels), len(skipped) - len(skipped_levels), len(q2_all) - len(Q2LIM)))
    # ---- Run B: every series with three consecutive members, seated instrument vs reference
    P = Fl = Rf = 0; cells_all = []; nser = 0; agree = True; triv_ok = triv_n = 0
    for lname, sp, key, mem, lim, Z in store:
        if len(mem) < 3:
            continue
        p, f, r, det = RULED.run_series(mem, lim, Z)
        p2, f2, r2, cells = ref_series(mem, lim, Z)
        if (p, f, r) != (p2, f2, r2) or [x[2] for x in cells] != [("pass" if x[1] == "pass" else x[1]) for x in det]:
            agree = False
        if p + f + r:
            nser += 1
        P += p; Fl += f; Rf += r
        for cnum, nu, verdict, lo, hi, E, q in cells:
            byn = {n: E for n, E, s in mem}
            cells_all.append(dict(species=sp, series=" ".join(key), n=cnum, nu=nu, verdict=verdict, lo=lo, hi=hi, E=E, q=q, Z=Z, lim=lim,
                                  Em=byn[cnum - 1], Ep=byn[cnum + 1]))
            triv_n += 1
            if byn[cnum - 1] <= E <= byn[cnum + 1]:
                triv_ok += 1
    ob("E1", "GUARD", agree, "the seated instrument and the independent reference agree cell for cell on every series", "%d cells" % len(cells_all))
    tot = P + Fl + Rf
    num("B_series", nser); num("B_cells", tot); num("B_pass", P); num("B_fail", Fl); num("B_refused", Rf)
    num("B_pass_pct", 100.0 * P / (P + Fl)); num("B_labels", len({c["species"] for c in cells_all}))
    num("B_species", len({NAMES.get(c["species"], c["species"]) for c in cells_all}))
    ob("E2", "MEASURED", tot > 0, "whole store, strict test: %d series across %d spectra (%d table labels), %d cells: %d pass, %d fail, %d refused (%.1f%% of tested pass)"
       % (nser, NUMS["B_species"], NUMS["B_labels"], tot, P, Fl, Rf, NUMS["B_pass_pct"]))
    num("B_triv_ok", triv_ok); num("B_triv_n", triv_n)
    ob("E3", "MEASURED", triv_ok == triv_n, "the T-bracket (containment between neighbours) on the same cells: %d of %d" % (triv_ok, triv_n))
    # ---- Run A: the 285 tabulated series with cells, member for member
    rows = series_rows()
    keys = []
    rec = json.load(open(os.path.join(ROOT, "method/members/run489_final.json")))["rec"]
    for k, v in rec.items():
        if v[0] == "run":
            sp, se, nr = k.split("|"); keys.append((sp, se, nr, "A250"))
    for k, v in json.load(open(os.path.join(ROOT, "method/members/run489_45.json"))).items():
        if v[0] == "run":
            sp, se = k.split("|"); keys.append((sp, se, rows[(sp, se)][2], "A45"))
    agg = {"A250": [0, 0, 0, 0], "A45": [0, 0, 0, 0]}
    byspecies = {}
    for sp, se, nr, grp in keys:
        name = sp.replace(" ", "")
        if sp in SIX:
            path = os.path.join(DRV, SIX[sp][0]); lim, Z = LIM[SIX[sp][1]]
        else:
            path = os.path.join(RAW, name + ".tsv"); lim, Z = LIM[name]
        m = re.match(r"^(.*?)n([spdfghik])\s+(\S+)\s+J=(\S+)$", se)
        pre, lch, term, J = m.groups()
        nl, nh = (int(x) for x in re.match(r"(\d+)[–-](\d+)", nr).groups())
        ser = load_table(path)
        mem = sorted({(n, E, s) for kk, vals in ser.items() if kk == (pre, lch, term, J) for n, E, s in vals if nl <= n <= nh and E < lim})
        if len(mem) < 3:
            continue
        p, f, r, det = RULED.run_series(mem, lim, Z)
        p2, f2, r2, _ = ref_series(mem, lim, Z)
        assert (p, f, r) == (p2, f2, r2)
        a = agg[grp]; a[0] += p; a[1] += f; a[2] += r; a[3] += (p + f + r > 0)
        s = byspecies.setdefault(sp, [0, 0]); s[0] += p; s[1] += f
    num("A250", agg["A250"]); num("A45", agg["A45"])
    A = [agg["A250"][i] + agg["A45"][i] for i in range(4)]
    num("A_pass", A[0]); num("A_fail", A[1]); num("A_refused", A[2]); num("A_series", A[3]); num("A_cells", A[0] + A[1] + A[2])
    num("A_pass_pct", 100.0 * A[0] / (A[0] + A[1]))
    ob("E4", "MEASURED", agg["A250"] == [658, 155, 0, 250] and agg["A45"] == [75, 6, 0, 35],
       "tabulated series, member for member: %d + %d = %d series, %d cells: %d pass, %d fail, %d refused (%.1f%%)"
       % (agg["A250"][3], agg["A45"][3], A[3], A[0] + A[1] + A[2], A[0], A[1], A[2], NUMS["A_pass_pct"]))
    worst = sorted(byspecies.items(), key=lambda kv: kv[1][0] / max(1, sum(kv[1])))[:6]
    num("A_worst", worst)
    ob("E4b", "MEASURED", worst[0][1][0] == 0,
       "the six species with the lowest pass rate in the tabulated run (pass/cells): "
       + ", ".join("%s %d/%d" % (sp, v[0], v[0] + v[1]) for sp, v in worst))
    # ---- V on measured cells (h = 1 and h = 2)
    def vcells(h):
        out = []
        for lname, sp, key, mem, lim, Z in store:
            byn = {n: E for n, E, s in mem}; byq = {n: qfloor(s) for n, E, s in mem}
            for n in byn:
                if n - h in byn and n + h in byn:
                    Tm, T0, Tp = lim - byn[n - h], lim - byn[n], lim - byn[n + h]
                    w = Tm - Tp; e = abs((Tm + Tp) / 2 - T0)
                    if T0 <= 0 or w <= 0:
                        continue
                    q = max(byq[n - h], byq[n], byq[n + h])
                    if e < 10 * q:                      # curvature not resolved at the quotation floor
                        continue
                    nu = Z * math.sqrt(R_FLOAT / T0); r = nu / h
                    out.append((w / e, V_exact(r), nu, r, sp))
        return out
    v1, v2 = vcells(1), vcells(2)
    med1 = statistics.median(abs(a / b - 1) for a, b, *_ in v1) * 100
    med2 = statistics.median(abs(a / b - 1) for a, b, *_ in v2) * 100
    medall = statistics.median(abs(a / b - 1) for a, b, *_ in v1 + v2) * 100
    num("V_pairs_h1", len(v1)); num("V_pairs_h2", len(v2)); num("V_med_h1", med1); num("V_med_h2", med2); num("V_med_all", medall)
    num("V_pairs_all", len(v1) + len(v2))
    ob("E5", "MEASURED", len(v1) > 0 and len(v2) > 0, "V measured against 4r^3/(3r^2-1): %d pairs at h = 1 (median deviation %.2f%%), %d at h = 2 (%.2f%%), %d in all (%.2f%%)"
       % (len(v1), med1, len(v2), med2, len(v1) + len(v2), medall))
    results["vpairs"] = [(a, b, nu, r, h) for h, vv in ((1, v1), (2, v2)) for a, b, nu, r, sp in vv]
    # ---- the yardstick: measured gaps against 2 Z^2 R / nu^3
    lower = []; upper = []
    for c in cells_all:
        if c["verdict"] == "REFUSED":
            continue
        D = 2 * c["Z"] ** 2 * R_FLOAT / c["nu"] ** 3
        lower.append((c["E"] - c["Em"]) / D); upper.append((c["Ep"] - c["E"]) / D)
    num("gap_lower_med", statistics.median(lower)); num("gap_upper_med", statistics.median(upper)); num("gap_pairs", len(lower))
    ob("E6", "MEASURED", NUMS["gap_lower_med"] > 1 > NUMS["gap_upper_med"],
       "measured gaps over 2Z^2R/nu^3 at %d cells: lower gap median %.3f, upper gap median %.3f (the derivative lies between)"
       % (len(lower), NUMS["gap_lower_med"], NUMS["gap_upper_med"]))
    # ---- the bound in the silence: the larger observed gap, max(E - E-, E+ - E), per held cell (Corollary 2)
    bounds = []; toward_lower = 0
    for c in cells_all:
        if c["verdict"] == "pass":
            g_lower, g_upper = c["E"] - c["Em"], c["Ep"] - c["E"]
            toward_lower += g_lower >= g_upper
            bounds.append((max(g_lower, g_upper), 2 * c["Z"] ** 2 * R_FLOAT / c["nu"] ** 3, c["nu"], c["Z"], c["species"], c["series"], c["n"],
                           (c["Ep"] - c["Em"]) / 2))
    bounds.sort()
    num("bound_cells", len(bounds)); num("bound_tightest", bounds[:5]); num("bound_median", statistics.median(b[0] for b in bounds))
    num("bound_toward_lower", toward_lower); num("halfwidth_tightest", min(b[7] for b in bounds))
    num("halfwidth_median", statistics.median(b[7] for b in bounds))
    ob("E7", "MEASURED", len(bounds) > 0 and all(b[0] >= b[7] for b in bounds),
       "%d held cells each bound the displacement of their level relative to its neighbours by the larger observed gap; tightest %.3f cm^-1 (%s %s n=%d, nu = %.1f, where 2Z^2R/nu^3 = %.3f); median %.0f; the larger gap is toward n - 1 at %d of %d cells (Lemma 3); for the record, w/2 would read tightest %.3f, median %.0f"
       % (len(bounds), bounds[0][0], bounds[0][4], bounds[0][5], bounds[0][6], bounds[0][2], bounds[0][1], NUMS["bound_median"],
          toward_lower, len(bounds), NUMS["halfwidth_tightest"], NUMS["halfwidth_median"]))
    results["bounds"] = bounds
    # ---- the floor's share of the verdicts (sensitivity of the split to the tolerance)
    tested = [c for c in cells_all if c["verdict"] != "REFUSED"]
    floor_only = sum(1 for c in tested if c["verdict"] == "pass" and not (c["lo"] <= c["E"] <= c["hi"]))
    near = {}
    for k in (2, 5):
        near[k] = sum(1 for c in tested if c["verdict"] == "FAIL" and c["lo"] - k * c["q"] <= c["E"] <= c["hi"] + k * c["q"])
    narrow = [c for c in tested if c["hi"] - c["lo"] < 2 * c["q"]]
    narrow_held = sum(1 for c in narrow if c["verdict"] == "pass")
    split = {}
    for k in (0, 1, 2, 5):
        pk = sum(1 for c in tested if c["lo"] - k * c["q"] <= c["E"] <= c["hi"] + k * c["q"])
        split[k] = (pk, len(tested) - pk)
    num("floor_only_passes", floor_only); num("fails_within", near); num("narrow_intervals", len(narrow)); num("narrow_held", narrow_held)
    num("split_by_tolerance", split)
    ob("E12", "MEASURED", split[1] == (P, Fl) and floor_only >= 0,
       "the floor's share: %d of %d passes hold only because of the floor (E outside [E_lo, E_hi], inside [E_lo - q, E_hi + q]); %d of %d fails lie within 2q of an edge and %d within 5q; %d cells have E_hi - E_lo < 2q (%d of them held); pass/fail at tolerance 0, q, 2q, 5q: %d/%d, %d/%d, %d/%d, %d/%d"
       % (floor_only, P, near[2], Fl, near[5], len(narrow), narrow_held, *split[0], *split[1], *split[2], *split[5]))
    # ---- order-k census with the admissibility rule
    census = {}
    for k in range(1, 7):
        adm = ref = unres = 0
        for lname, sp, key, mem, lim, Z in store:
            byn = {n: (lim - E) for n, E, s in mem}; byq = {n: qfloor(s) for n, E, s in mem}
            for n0 in sorted(byn):
                ns = list(range(n0, n0 + k + 2))
                if not all(n in byn for n in ns):
                    continue
                vals = [byn[n] for n in ns]
                for _ in range(k + 1):
                    vals = [b - a for a, b in zip(vals, vals[1:])]
                dd = vals[0]; q = max(byq[n] for n in ns)
                if abs(dd) <= 5 * 2 ** (k + 1) * q:
                    unres += 1
                elif (dd > 0) != ((k + 1) % 2 == 0):
                    ref += 1
                else:
                    adm += 1
        census[k] = (adm, ref, unres)
    num("order_census", census)
    ob("E8", "MEASURED", census[1][0] > 0, "order-k census (admitted / wrong sign / unresolved): " + "; ".join("k=%d %d/%d/%d" % (k, *census[k]) for k in census))
    results["cells"] = cells_all
    # ---- the hydrogenic thresholds: Dirac term against the deficit
    alpha = 7.2973525693e-3; me_u = 5.48579909065e-4
    # the thresholds the tree holds, each with its provenance and its stated uncertainty
    ladder = os.path.join(ROOT, "extracted/archives/method16-rp-b-data/LADDER-H-Ar-I-III.tsv")
    li_asd = None
    for line in open(ladder, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) >= 9 and p[1] == "Li III":
            li_asd = (float(p[6]), float(p[8]))
    assert li_asd is not None
    thr = {  # species: (Z, atomic mass u [AME2020], I, +/-, source)
        "Li III (ASD)": (3, 7.016003437, li_asd[0], li_asd[1], "NIST ASD 5.12 ionization energy, theoretical, retrieved 2026-08-10"),
        "Li III (fit)": (3, 7.016003437, LIM["LiIII"][0], 0.36, "fitted to the series of theoretical levels (Yerokhin and Shabaev 2015)"),
        "Be IV": (4, 9.012183065, LIM["BeIV"][0], 0.0008, "NIST ASD 5.12, theoretical"),
        "B V": (5, 11.009305167, LIM["BV"][0], None, "fitted to the series of theoretical levels; no published uncertainty held"),
    }
    assert abs(thr["Be IV"][2] - 1756018.8100) < 1e-6 and abs(thr["B V"][2] - 2744111.38) < 1e-6 and abs(thr["Li III (fit)"][2] - 987662.29) < 1e-6
    rel = {}
    for sp, (Z, M_atom, lim, unc, src) in thr.items():
        M_nuc = M_atom - Z * me_u
        RM = R_FLOAT / (1 + me_u / M_nuc)
        deficit = lim - Z * Z * RM
        dirac = Z ** 4 * alpha ** 2 * RM / 4
        rel[sp] = (deficit, dirac, deficit / dirac, lim - Z * Z * R_FLOAT, lim, unc, src)
    num("relativity", rel)
    ratios = [v[2] for v in rel.values()]
    ob("E9", "MEASURED", all(0.85 < x < 0.92 for x in ratios) and abs(rel["Li III (ASD)"][4] - 987661.0139) < 1e-6,
       "hydrogenic thresholds I against Z^2 R_M (I, +/-; deficit; Dirac Z^4 a^2 R_M/4; ratio): "
       + "; ".join("%s %.4f +/- %s, %.2f, %.2f, %.3f" % (k, v[4], ("%.4f" % v[5]) if v[5] is not None else "n/a", v[0], v[1], v[2]) for k, v in rel.items())
       + "; Li III (fit) against 9 R_inf is %.2f cm^-1, Li III (ASD) %.2f" % (rel["Li III (fit)"][3], rel["Li III (ASD)"][3]))
    # a threshold error dI shifts every quantum defect of the ion by d(delta) = dI nu^3 / (2 Z^2 R): the 9 R_inf error for Li III
    dI = rel["Li III (fit)"][3]
    coef = dI / (2 * 9 * R_FLOAT)
    num("delta_err_coef", coef); num("delta_err_n7", coef * 7 ** 3); num("delta_err_n2", coef * 8)
    ob("E9b", "ARITHMETIC", abs(coef * 343 - 0.0046) < 2e-4,
       "a threshold written as 9 R_inf for Li III shifts delta by -(%.2f nu^3)/(2 Z^2 R) = -%.2e nu^3: -%.4f at n = 2, -%.4f at n = 7" % (dI, coef, coef * 8, coef * 343))
    # the reduced mass: R_inf against R_M for the lightest species in the collection (lithium)
    mM = me_u / (7.016003437 - 3 * me_u)
    num("li_me_over_M", mM); num("li_nu_shift_per_nu", mM / 2); num("li_triple_spread", mM / 2)
    ob("E13", "ARITHMETIC", 7e-5 < mM < 9e-5,
       "reduced mass, lithium: m_e/M = %.2e; using R_inf for R_M shifts nu by nu (m_e/M)/2 = %.1e nu (%.1e at nu = 10), the same shift to within h (m_e/M)/2 = %.1e across a triple at h = 1"
       % (mM, mM / 2, 5 * mM, mM / 2))
    # ---- rank one across power laws (fifteen exponents)
    exps = [-3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 11, 15, 1.5, 2.5, 11 / 6]
    nus = [10 + 2 * i for i in range(40)]
    M = [[p * math.log(nu) for nu in nus] for p in exps]
    rowmeans = [sum(r) / len(r) for r in M]
    M = [[x - rowmeans[i] for x in r] for i, r in enumerate(M)]
    import numpy as np
    sv = np.linalg.svd(np.array(M), compute_uv=False)
    num("sv1", float(sv[0])); num("sv2", float(sv[1]))
    ob("E10", "ARITHMETIC", sv[1] / sv[0] < 1e-12, "numerical corroboration of Lemma 7 (floating-point SVD): centred log-matrix of 15 power laws over 40 values of nu: sigma1 = %.2f, sigma2/sigma1 = %.1e" % (sv[0], sv[1] / sv[0]))
    # ---- the depth of the collection, and self-concordance across it
    def sc_ratio(Z, nu):
        A = Z * Z * R_FLOAT
        return (24 * A / nu ** 5) / (2 * (6 * A / nu ** 4) ** 1.5)
    nu_min = min(c["nu"] for c in cells_all); nu_max = max(c["nu"] for c in cells_all)
    below2 = [c for c in cells_all if c["nu"] < 2]
    worst = max(cells_all, key=lambda c: sc_ratio(c["Z"], c["nu"]))
    sc_worst = sc_ratio(worst["Z"], worst["nu"])
    num("nu_min_cell", nu_min); num("nu_max_cell", nu_max)
    num("cells_below_2", [(c["species"], c["series"], c["n"], c["nu"], c["Z"]) for c in below2])
    num("sc_worst", sc_worst); num("sc_margin", 1 / sc_worst)
    num("sc_worst_where", (worst["species"], worst["series"], worst["n"], worst["nu"], worst["Z"]))
    sc_worst_hartree = sc_worst * math.sqrt(R_FLOAT / R_HARTREE)      # the same cell with A in hartree: the ratio scales as A^(-1/2)
    num("sc_worst_hartree", sc_worst_hartree)
    ob("E11", "MEASURED", sc_worst < 1 and len(below2) <= 1 and sc_worst_hartree > 1,
       "depth of the tested cells: nu from %.5f to %.2f; %d cell(s) below nu = 2 (%s n=%d); the ratio |T'''|/2(T'')^1.5 at the deepest cell, nu = %.2f, Z = %d, is %.4f with R in cm^-1 and %.1f with R in hartree (the same cell); V at the shallowest cell is below 32/11 by %.1e"
       % (nu_min, nu_max, len(below2), below2[0]["species"] if below2 else "-", below2[0]["n"] if below2 else 0,
          worst["nu"], worst["Z"], sc_worst, sc_worst_hartree,
          num("V_deficit_shallowest", 1 - V_exact(nu_min) / float(F(32, 11)))))


# =============================================================================

def selftest_negative():
    print("\nN. NEGATIVE CONTROLS")
    n, ok = PROOFS.verify(("NX", "", "", [], {"r": 6}, lambda r: V_exact(r) - 4 * r ** 3 / (3 * r * r + 1), ("r",)))
    ob("N3", "NEGATIVE", ok is False, "a wrong identity (V = 4r^3/(3r^2+1)) is refuted on the grid")
    # a displaced level beyond its gap must fail the strict containment
    Tn = {n: float(R_INF / F(n) ** 2) for n in (9, 10, 11)}
    disp = Tn[10] + (Tn[9] - Tn[10]) * 1.01
    ob("N4", "NEGATIVE", not contained_py(disp, Tn[9], Tn[11]), "a level displaced past its upper gap leaves the interval (Theorem 3 witness)")
    # the seated test refuses a cell whose floor is too coarse
    mem = [(n, float(R_INF / F(n) ** 2), "%.0f" % float(R_INF / F(n) ** 2)) for n in (59, 60, 61)]
    mem = [(n, -E + 200000.0, "%.0f" % (-E + 200000.0)) for n, E, s in mem]
    p, f, r, det = RULED.run_series(mem, 200000.0, 1)
    ob("N5", "NEGATIVE", r == 1, "a cell quoted to 1 cm^-1 at nu = 60 (r = %.2f) is REFUSED by the seated instrument, not passed" % det[0][2])


def main():
    selftest = "--selftest" in sys.argv
    print("check.py -- paper 03, the bracket")
    results = {}
    part1(); part2(); part3(); part4(selftest); part5(results)
    if selftest:
        selftest_negative()
    print()
    counts = {}
    for oid, st, ok, label, det in ROWS:
        counts[st] = counts.get(st, 0) + 1
    print("SUMMARY  " + "  ".join("%s %d" % kv for kv in sorted(counts.items())) + "  | %d obligations, %d failed" % (len(ROWS), len(FAILS)))
    if "--json" in sys.argv:
        out = {"numbers": {k: (str(v) if isinstance(v, F) else v) for k, v in NUMS.items()},
               "rows": ROWS, "results": {k: v for k, v in results.items() if k != "cells"},
               "cells": results.get("cells", [])}
        json.dump(out, open(os.path.join(HERE, "results.json"), "w"), indent=0, default=str)
        print("wrote results.json")
    if FAILS:
        print("FAILED:", ", ".join(FAILS))
        return 1
    print("CHECK PASS" + (" (selftest)" if selftest else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
