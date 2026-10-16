#!/usr/bin/env python3
"""qr_paper_check.py -- the machine check of EVERYTHING-IS-RELATIVE.md.

Every number and every identity the paper prints as computed is asserted here, either by running the instrument that
carries it (imported by path from ../docket68/lemmas/, never copied) or by a computation of this file's own, marked
"(this paper)" in the paper.  Each claim also asserts that its printed form appears in the paper's text, so the paper
and the check cannot drift apart silently.

  python3 qr_paper_check.py              report every claim
  python3 qr_paper_check.py --selftest   exit 0 iff every claim holds and every instrument's own checks pass
  python3 qr_paper_check.py --mutants    each mutant must be caught by the claim it targets

Stdlib + sympy.  Run with PYTHONDONTWRITEBYTECODE=1 so nothing is written beside the instruments.
"""
import importlib.util
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
LEMMAS = os.path.join(os.path.dirname(HERE), "docket68", "lemmas")
PAPER = os.path.join(HERE, "EVERYTHING-IS-RELATIVE.md")
MUT = set()
_CACHE = {}


def load(name):
    if name not in _CACHE:
        spec = importlib.util.spec_from_file_location("qr_" + name, os.path.join(LEMMAS, name + ".py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _CACHE[name] = mod
    return _CACHE[name]


_RUNS = {}


def run(name):
    """an instrument's compute() and its own checks, cached unless a mutant touches that instrument"""
    key = (name, "inst_gb_double" in MUT and name == "gb_cone")
    if key not in _RUNS:
        mod = load(name)
        mod.MUT.clear()
        if key[1]:
            mod.MUT["gb_double"] = True
        if name == "quantum_onset":
            out, ok = None, mod.selftest(quiet=True)
        else:
            out = mod.compute()
            ok = all(v for _, v in mod.checks(out))
        mod.MUT.clear()
        _RUNS[key] = (out, ok)
    return _RUNS[key]


def paper_text():
    t = " ".join(open(PAPER, encoding="utf-8").read().split())
    if "paper_drift" in MUT:
        t = t.replace("537/461", "537/460")
    return t


# ---------------------------------------------------------------- computations of this paper's own

def no_signalling():
    """Lemma 5 (this paper): no local operation of Alice changes Bob's reduced state, for any two-qubit pure state"""
    a = sp.symbols("a0:4", complex=True)
    psi = sp.Matrix(a)
    rho = psi * psi.H
    th, ph = sp.symbols("theta phi", real=True)
    U = sp.Matrix([[sp.cos(th), -sp.exp(-sp.I * ph) * sp.sin(th)], [sp.exp(sp.I * ph) * sp.sin(th), sp.cos(th)]])
    I2 = sp.eye(2)
    if "signal" in MUT:                                       # the mutant: a non-local gate (CNOT) passed off as local
        UA = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    else:
        UA = sp.kronecker_product(U, I2)

    def ptrace_A(r):
        return sp.Matrix(2, 2, lambda i, j: sum(r[2 * k + i, 2 * k + j] for k in range(2)))
    before = ptrace_A(rho)
    after_unitary = ptrace_A(UA * rho * UA.H)
    # a non-selective projective measurement by Alice in the basis U|0>, U|1>
    P = [sp.kronecker_product(U * sp.Matrix([[1, 0], [0, 0]]) * U.H, I2),
         sp.kronecker_product(U * sp.Matrix([[0, 0], [0, 1]]) * U.H, I2)]
    if "signal" in MUT:
        P = [UA * p * UA.H for p in P]
    after_meas = ptrace_A(sum((p * rho * p for p in P), sp.zeros(4)))
    d1 = sp.simplify(sp.expand(after_unitary - before))
    d2 = sp.simplify(sp.expand(after_meas - before))
    return d1 == sp.zeros(2) and d2 == sp.zeros(2)


def dispersion():
    """Lemma 1: E^2 = p^2 c^2 + m^2 c^4, and E = p c at m = 0"""
    p, m, c = sp.symbols("p m c", nonnegative=True)
    E = sp.sqrt(p ** 2 * c ** 2 + m ** 2 * c ** 4)
    return sp.simplify(E.subs(m, 0) - p * c) == 0


def lovelock_counts():
    return {n: (n - 1) // 2 for n in (4, 5, 6, 7)}


def cone_algebra():
    """Lemma 6 on the Boulware-Deser hole, from the cones the instrument computes: sum rule and the excess"""
    al, m, r, q = sp.symbols("alpha m r q", positive=True)
    A = 1 - 8 * al * m / (r ** 4 * q ** 2)
    cT, cV, cS = 3 - 2 * A, A, 2 * A - 1
    w = (1, 1, 1) if "sum_weights" in MUT else (2, 2, 1)       # the mutant: the polarisations counted once each
    s = sp.simplify(w[0] * (cT - 1) + w[1] * (cV - 1) + w[2] * (cS - 1))
    exT = sp.simplify(cT - 1 - 16 * al * m / (r ** 4 * q ** 2))
    exS = sp.simplify(cS - 1 + 16 * al * m / (r ** 4 * q ** 2))
    return s == 0 and exT == 0 and exS == 0


def wave_sum():
    eps, al = sp.symbols("epsilon alpha")
    om = [8 * al * eps] + [4 * al * eps] * 2 + [-8 * al * eps] * 2
    return sp.simplify(sum(om)) == 0


def sgb_numbers():
    """Lemma 7, the cosmology point: 8 f.. and c_T^2 - 1 from c_T^2 = 537/461 and 8 H f. = -1/25"""
    cT2 = sp.Rational(537, 461)
    eHf = 8 * 1 * (sp.Rational(-1, 480) * sp.Rational(12, 5))
    efdd = cT2 * (1 + eHf) - 1
    return eHf == sp.Rational(-1, 25) and efdd == sp.Rational(1363, 11525) and cT2 - 1 == sp.Rational(76, 461)


def buckingham_4d():
    """Section 12 (this paper): {G, hbar, c, R} in four dimensions -- rank 3, one group, l_P^2 R"""
    dims = [(-1, 3, -2), (1, 2, -1), (0, 1, -1), (0, -2, 0)]       # G, hbar, c, R in (M, L, T)
    A = sp.Matrix([[d[k] for d in dims] for k in range(3)])
    ns = A.nullspace()
    v = sp.Matrix([1, 1, -3, 1])                                   # G hbar c^-3 R = l_P^2 R
    return A.rank() == 3 and len(ns) == 1 and (A * v).is_zero_matrix


def onset_corrected():
    """corrected onset: a term l5 ell R reaches one at R* = 1/(l5 ell), where x = l5^2 R* = l5/ell"""
    l5, ell, R = sp.symbols("l_5 ell R", positive=True)
    Rs = sp.solve(sp.Eq(l5 * ell * R, 1), R)[0]
    x = sp.sqrt(l5 ** 2 * Rs) if "onset_sqrt" in MUT else l5 ** 2 * Rs  # the mutant: the refuted value
    return sp.simplify(x - l5 / ell) == 0


def hr_relation():
    """Section 12 (this paper): Haggard and Rovelli's q = l_P R tau at tau = R^(-1/2) is (l_P^2 R)^(1/2)"""
    lP, R = sp.symbols("l_P R", positive=True)
    q = lP * R * R ** sp.Rational(-1, 2)
    return sp.simplify(q - sp.sqrt(lP ** 2 * R)) == 0


# ---------------------------------------------------------------- the claims, each with its printed form

def claims():
    rel = lambda: run("relativity")
    gbc = lambda: run("gb_cone")
    sgb = lambda: run("sgb_cone")
    qo = lambda: run("quantum_onset")
    C = []
    add = lambda cid, text, fn: C.append((cid, text, fn))
    add("I1 instrument relativity.py: its own checks pass", "M1 (special and general relativity)", lambda: rel()[1])
    add("I2 instrument gb_cone.py: its own checks pass", "M2 (the Gauss–Bonnet cones)", lambda: gbc()[1])
    add("I3 instrument sgb_cone.py: its own checks pass", "M3 (scalar–Gauss–Bonnet)", lambda: sgb()[1])
    add("I4 instrument quantum_onset.py: its own selftest passes", "M4 (the quantum onset)", lambda: qo()[1])
    add("L1 E = pc at m = 0", "E^2 = p^2 c^2 + m^2 c^4", dispersion)
    add("L2 boost invariants for every kind", "Λ^T η Λ = η",
        lambda: all(rel()[0]["sr"][k] for k in ("keeps", "null_kept", "future", "mass_kept", "below_c", "scalar",
                                                  "gauge", "gauge_dual", "vacuum", "sheet")))
    add("L3 geodesics carry no mass", "independent of m", lambda: rel()[0]["gr"]["mass_free"])
    add("L3 bending 1.751 arcsec", "1.751",
        lambda: abs(rel()[0]["gr"]["deflection_arcsec"] - 1.751) < 0.0005)
    add("L4 Lovelock p(4) = 1, p(5) = 2", "p = ⌊(n − 1)/2⌋",
        lambda: rel()[0]["lv"]["counts"] == {4: 1, 5: 2} and lovelock_counts() == {4: 1, 5: 2, 6: 2, 7: 3})
    add("L5 no signalling (this paper)", "ρ_B is unchanged", no_signalling)
    add("L6 Einstein's law: every front null", "every characteristic front is null",
        lambda: gbc()[0]["hole"]["einstein_null"])
    add("L6 three cones on a static bulk, radially null, 1 on AdS", "(1 + 4αK₁)/(1 + 4αK₂)",
        lambda: gbc()[0]["hole"]["cones_ok"] and gbc()[0]["hole"]["radial_null"] and gbc()[0]["hole"]["ads_null"])
    add("L6 Boulware-Deser cones c_T = 3 - 2A, c_V = A, c_S = 2A - 1", "c_T = 3 − 2A",
        lambda: gbc()[0]["hole"]["bd_ok"])
    add("L6 sum rule and excess 16|alpha| m/(r^4 q^2)", "2(c_T − 1) + 2(c_V − 1) + (c_S − 1) = 0",
        lambda: gbc()[0]["hole"]["sum_rule"] == 0 and gbc()[0]["hole"]["A_minus_1"] == 0 and cone_algebra())
    add("L6 type N wave omegas 8, 4, 4, -8, -8 (alpha eps), sum zero", "ω = 8αε",
        lambda: wave_sum() and gbc()[1])
    add("L6 on AdS the omegas divided by 1 - 4 alpha k^2", "1 − 4αk²", lambda: gbc()[1])
    add("L7 sGB tensor cone (1 + 8 f..)/(1 + 8 H f.), Reall's eq. (91)", "(1 + 8f̈)/(1 + 8Hḟ)",
        lambda: sgb()[0]["cosmo"]["tensor_ok"] and sgb()[0]["cosmo"]["reall_ok"])
    add("L7 sGB exact points: c_T^2 = 537/461", "537/461",
        lambda: all(p["cT"] == sp.Rational(537, 461) and p["weak"] == sp.Rational(1, 25)
                    for p in sgb()[0]["cosmo"]["points"].values()) and sgb_numbers())
    add("L7 8 f.. = 1363/11525, c_T^2 - 1 = 76/461", "1363/11525", sgb_numbers)
    add("L7 sGB wave: mixed fronts |xi|^2/(1 -+ 8 sqrt2 f' eps)", "|ξ|²/(1 ∓ 8√2 f′ε)",
        lambda: all(d["ok"] for d in sgb()[0]["wave"]["dirs"].values()) and sgb()[0]["wave"]["solves"])
    add("Q1 Buckingham in 5D: rank 3, two groups", "rank 3", lambda: qo()[1])
    add("Q1 Buckingham in 4D (this paper): one group l_P^2 R", "l_P² R", buckingham_4d)
    add("Q6 corrected: x = l5/ell at the counterfactual onset", "x = l₅/ℓ", onset_corrected)
    add("HR q = l_P R tau at tau = R^-1/2 is (l_P^2 R)^1/2 (this paper)", "(l_P² R)^{1/2}", hr_relation)
    return C


def evaluate():
    txt = paper_text()
    out = []
    for cid, text, fn in claims():
        printed = " ".join(text.split()) in txt
        try:
            ok = bool(fn())
        except Exception as ex:                                   # a crash is a failure, named
            ok = False
            cid += " [raised %s]" % type(ex).__name__
        out.append((cid, printed, ok))
    return out


def report():
    for cid, printed, ok in evaluate():
        print("  [%s] %s%s" % ("ok" if printed and ok else "FAIL", cid, "" if printed else "  (form not in paper)"))


def selftest():
    res = evaluate()
    for cid, printed, ok in res:
        print("  [%s] %s%s" % ("ok" if printed and ok else "FAIL", cid, "" if printed else "  (form not in paper)"))
    n = sum(p and o for _, p, o in res)
    print("selftest: %d/%d" % (n, len(res)))
    return n == len(res)


MUTANTS = {"paper_drift": ("the paper's 537/461 altered to 537/460", "L7 sGB exact points"),
           "signal": ("a non-local gate passed off as Alice's local operation", "L5 no signalling"),
           "onset_sqrt": ("the refuted (l5/ell)^(1/2) used for x", "Q6 corrected"),
           "sum_weights": ("the cone sum rule with weights 1, 1, 1", "L6 sum rule"),
           "inst_gb_double": ("gb_cone.py run with its own gb_double mutant", "I2 instrument gb_cone.py")}


def mutants():
    caught = 0
    for mk, (desc, target) in MUTANTS.items():
        MUT.clear()
        MUT.add(mk)
        failed = [cid for cid, p, o in evaluate() if not (p and o)]
        MUT.clear()
        hit = any(c.startswith(target) for c in failed)
        caught += hit
        print("  mutant %-14s %-58s %s" % (mk, desc, ("caught by " + "; ".join(c.split(" ")[0] for c in failed))
                                            if hit else "NOT CAUGHT by " + target))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
