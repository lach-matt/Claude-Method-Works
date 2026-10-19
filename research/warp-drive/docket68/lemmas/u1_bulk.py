#!/usr/bin/env python3
"""u1_bulk.py -- item 446 (1): the U(1) gauge field in the bulk, assumed by M and proved with the math and outside art.
M: "1 - I would assume yes, prove with the math and outside art contributions".  The corridor of 445-446 needs a
five-dimensional U(1) (Maldacena and Milekhin's model); the record's bulk had gravity alone.  Labels: READ (verbatim,
SOURCES below), computed (sympy exact; the flow numerically, RK4), deduced.  Worked in the conversation; not verified;
not seated.  2026-10-16.

  U0 (read) M's words: 446 (1).
  U1 (READ) The outside art (SOURCES): the model with a five-dimensional U(1) (MM 2008.06618); its magnetic flow to
     AdS3 (D'Hoker and Kraus 0908.3875); the zero mode not localized (Pomarol hep-ph/9911294); the long-distance
     behaviour (Kaloper, Silverstein and Susskind hep-th/0006192); charged brane-world black holes (Chamblin, Reall,
     Shinkai and Shiromizu hep-th/0008177).
  U2 (computed, exact) Unexcited, it changes nothing.  The Maxwell stress tensor T_MN = (F_MP F_N^P - g_MN F^2/4)/g5^2
     is quadratic in F, so F = 0 gives T = 0 and Maxwell's equations hold trivially: the record's bulk and B6''s de
     Sitter plane (b6p_prove D0-D5) solve Einstein-Maxwell unchanged.
  U3 (computed, exact) It keeps the null condition at every point, excited or not.  In a null frame of five dimensions
     with k = e_+, T_MN k^M k^N = T_++ = (F_+1^2 + F_+2^2 + F_+3^2)/g5^2 >= 0, for every F; any null vector is e_+ of
     some frame.  So no lemma resting on the null condition moves (b5b_wall W2-W3, bounce_scope B1), and the
     corridor's negative energy cannot come from this field: it comes from the throat's AdS3, classical in five
     dimensions (MM, READ in BOUNCE-RESEARCH section 9).
  U4 (computed, exact) Its four-dimensional coupling runs.  For a y-independent zero mode in ds^2 = e^{2y/R5} dx^2 + dy^2
     the action's weight is sqrt(g) g^{mu mu'} g^{nu nu'} = 1 in y, so 1/g4^2 = s (R5/g5^2) ln(L_IR/R5) for s sides: it
     diverges as L_IR -> infinity, Pomarol's "not localized", reproduced.  The corridor needs it only near the mouths,
     cut off at l_B (MM 3.24-3.25).
  U5 (computed, exact; numerical where marked) The magnetic flow exists.  Einstein-Maxwell for MM's ansatz (3.18),
     derived here from the metric: the rho-rho component is MM's (A.28) at beta = 8 pi G5 B^2/g5^2 = 6 l_B^-4, and
     (2 E_tt - E_yy + E_rhorho)/3 is their (A.29).  Integrated (RK4) from the IR's growing mode (exponent sqrt(19) -
     sqrt(3), exact) outward, the flow reaches AdS5 (sigma' -> 1, lambda' -> 1) from AdS3 x R^2 (lambda' = sqrt(3), so
     R3 = R5/sqrt(3)); the tt component, which the integration does not use, holds along it (Bianchi), and halving the
     step moves the end value by under 1e-9.  Brown-Henneaux's 3 R3/(2 G3) with 1/G3 = R5^2 A/(G5 l_B^2) is MM's c_2 =
     sqrt(3) R5^3 A/(2 G5 l_B^2) exactly (3.21).
  U6 (deduced) What is proved, and what is not.  The bulk U(1) is consistent with the record (U2), keeps the null
     condition (U3), and supplies the flux whose flow (U5) turns the four-dimensional Casimir energy into classical
     five-dimensional energy; its zero mode is not localized (U4) and its long-distance fate in microscopic
     realizations is screening or a Higgs mechanism (KSS, READ), both outside the corridor's scales.  It is a field
     added to the theory, M's assumption (446 (1)), shown consistent and established in the literature -- not derived
     from first principles.  MM's dark sector meets the Standard Model only by gravity, so no measurement bounds it
     except through gravity.

python3 u1_bulk.py [--selftest | --mutants]
"""
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ("1 - I would assume yes, prove with the math and outside art contributions",)
SOURCES = {
    "MM": ("2008.06618", "We imagine that we have a five dimensional gravity theory with a five dimensional U(1) gauge "
                         "field, as in (3.17).", "This dark sector only interacts via gravity with the Standard Model."),
    "DK": ("0908.3875", "We construct asymptotically AdS_5 solutions of Einstein-Maxwell theory dual to N=4 SYM theory "
                        "on R^{3,1} in the presence of a background magnetic field.",
           "The solutions interpolate between AdS_5 and a near horizon AdS_3\\times T^2."),
    "POMAROL": ("hep-ph/9911294", "we find that the massless mode is not localized in the extra dimension"),
    "KSS": ("hep-th/0006192", "one might expect the gauge symmetry in d+1 dimensions to behave like a global symmetry "
                              "in d dimensions, despite the presence of gravity",
            "It turns over either to screening or the Higgs mechanism at long distances in the d-dimensional "
            "description of the system."),
    "CRSS": ("hep-th/0008177", "Such black holes can carry two types of ``charge'', one arising from the bulk Weyl "
                               "tensor and one from a gauge field trapped on the wall."),
}
CITED = ("MM", "DK", "POMAROL", "KSS", "CRSS")


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def u1():
    return all(k in SOURCES and len(SOURCES[k]) >= 2 and all(len(q) > 20 for q in SOURCES[k][1:]) for k in CITED)


def _metric5():
    """light-cone frame (+, -, 1, 2, 3): g_{+-} = -1, g_ii = 1"""
    g = sp.zeros(5, 5)
    g[0, 1] = g[1, 0] = -1
    for i in (2, 3, 4):
        g[i, i] = 1
    return g


def _field():
    F = sp.zeros(5, 5)
    for a in range(5):
        for b in range(a + 1, 5):
            s = sp.Symbol("F%d%d" % (a, b), real=True)
            F[a, b], F[b, a] = s, -s
    return F


def stress(F, g, g5=sp.Symbol("g5", positive=True)):
    gi = g.inv()
    Fup = gi * F * gi                                                    # F^{MN}
    F2 = sum(F[a, b] * Fup[a, b] for a in range(5) for b in range(5))
    T = (F * gi * F.T - g * F2 / 4) / g5 ** 2                          # F_MP g^PQ F_NQ
    if "flip" in MUT:
        T = (-F * gi * F.T - g * F2 / 4) / g5 ** 2
    return sp.simplify(T)


def u2():
    g, F = _metric5(), _field()
    T = stress(F, g)
    zero = all(sp.simplify(e) == 0 for e in T.subs({s: 0 for s in F.free_symbols}))
    lam = sp.Symbol("lam", positive=True)
    quad = sp.simplify(stress(lam * F, g) - lam ** 2 * T) == sp.zeros(5, 5)
    return zero and quad


def u3():
    g, F = _metric5(), _field()
    T = stress(F, g)
    g5 = sp.Symbol("g5", positive=True)
    target = sum(F[0, i] ** 2 for i in (2, 3, 4)) / g5 ** 2
    return sp.simplify(T[0, 0] - target) == 0, T[0, 0]


def u4():
    y, R5, L, s = sp.symbols("y R_5 L_IR s", positive=True)
    w = 4 if "no_warp" not in MUT else 2
    weight = sp.exp(w * y / R5) * sp.exp(-4 * y / R5)                   # sqrt(g) g^{mu mu'} g^{nu nu'}
    y_ir = R5 * sp.log(R5 / L)                                          # depth where the warp is R5/L_IR
    one_side = sp.integrate(weight, (y, y_ir, 0))
    closed = sp.simplify(one_side - R5 * sp.log(L / R5)) == 0
    diverges = sp.limit(one_side, L, sp.oo) == sp.oo
    return closed, diverges


def einstein():
    """the Einstein-Maxwell components for ds^2 = e^{2 lam}(-dt^2 + dx^2) + e^{2 sig}(dy1^2 + dy2^2) + drho^2 (R5 = 1),
    F = B dy1 ^ dy2, Lambda = -6, beta = 8 pi G5 B^2/g5^2: E_MM/g_MM for M = t, y1, rho"""
    t, x, y1, y2, r = sp.symbols("t x y1 y2 rho")
    X = (t, x, y1, y2, r)
    lam, sig = sp.Function("lam")(r), sp.Function("sig")(r)
    g = sp.diag(-sp.exp(2 * lam), sp.exp(2 * lam), sp.exp(2 * sig), sp.exp(2 * sig), 1)
    gi = g.inv()
    n = 5
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]

    def ric(b):
        return sp.simplify(sum(sp.diff(Gam[a][b][b], X[a]) for a in range(n))
                           - sum(sp.diff(Gam[a][b][a], X[b]) for a in range(n))
                           + sum(Gam[a][a][d] * Gam[d][b][b] for a in range(n) for d in range(n))
                           - sum(Gam[a][b][d] * Gam[d][b][a] for a in range(n) for d in range(n)))
    Rd = [ric(i) for i in range(n)]
    Rs = sp.simplify(sum(gi[i, i] * Rd[i] for i in range(n)))
    beta = sp.Symbol("beta")
    F2 = 2 * sp.exp(-4 * sig)                                           # F^2 / B^2
    out = {}
    for i, name in ((0, "tt"), (2, "yy"), (4, "rr")):
        T = (sp.exp(-2 * sig) if i in (2, 3) else 0) - g[i, i] * F2 / 4
        out[name] = sp.simplify((Rd[i] - g[i, i] * Rs / 2 - 6 * g[i, i] - beta * T) / g[i, i])
    d = {sp.Derivative(lam, (r, 2)): sp.Symbol("lpp"), sp.Derivative(sig, (r, 2)): sp.Symbol("spp")}
    d2 = {sp.Derivative(lam, r): sp.Symbol("lp"), sp.Derivative(sig, r): sp.Symbol("sp"), sig: sp.Symbol("s")}
    return {k: v.subs(d).subs(d2) for k, v in out.items()}


def u5_equations():
    E = einstein()
    lp, sp_, s, spp, beta = sp.symbols("lp sp s spp beta")
    a28 = -6 + 3 * sp.exp(-4 * s) + lp ** 2 + 4 * lp * sp_ + sp_ ** 2
    a29 = 4 - 4 * sp.exp(-4 * s) - 2 * lp * sp_ - 2 * sp_ ** 2 - spp
    ok28 = sp.simplify(E["rr"].subs(beta, 6) - a28) == 0
    comb = sp.simplify((2 * E["tt"] - E["yy"] + E["rr"]).subs(beta, 6) / 3)
    ok29 = sp.simplify(comb + a29) == 0
    return ok28, ok29, sp.lambdify(sp.symbols("s sp spp lp lpp"), E["tt"].subs(beta, 6), "math")


def flow(rho_end=12.0, h=1e-3, ett=None):
    """MM (A.28)-(A.29) with l_B = 1: sigma'' = 4 - 4 e^{-4 sigma} - 2 lambda' sigma' - 2 sigma'^2, lambda' from (A.28);
    the tt component checked along the way, lambda'' by the chain rule"""
    k = -math.sqrt(3) + math.sqrt(19)
    if "decaying" in MUT:
        k = -math.sqrt(3) - math.sqrt(19)
    c29 = 4.04 if "a29" in MUT else 4.0
    eps = 1e-7
    s, sp_ = eps, k * eps

    def lam_p(s, p):
        disc = 3 * p * p + 6 - 3 * math.exp(-4 * s)
        return -2 * p + math.sqrt(max(disc, 0.0))

    def acc(s, p):
        return c29 - 4 * math.exp(-4 * s) - 2 * lam_p(s, p) * p - 2 * p * p

    worst = 0.0
    lp0 = lam_p(s, sp_)
    for _ in range(int(round(rho_end / h))):                            # a fixed count: both steps end at rho_end
        k1s, k1p = sp_, acc(s, sp_)
        k2s, k2p = sp_ + h / 2 * k1p, acc(s + h / 2 * k1s, sp_ + h / 2 * k1p)
        k3s, k3p = sp_ + h / 2 * k2p, acc(s + h / 2 * k2s, sp_ + h / 2 * k2p)
        k4s, k4p = sp_ + h * k3p, acc(s + h * k3s, sp_ + h * k3p)
        s += h / 6 * (k1s + 2 * k2s + 2 * k3s + k4s)
        sp_ += h / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
        if ett is not None:
            D = 3 * sp_ * sp_ + 6 - 3 * math.exp(-4 * s)
            spp = acc(s, sp_)
            lpp = 6 * math.exp(-4 * s) / math.sqrt(D) * sp_ + (-2 + 3 * sp_ / math.sqrt(D)) * spp
            worst = max(worst, abs(ett(s, sp_, spp, lam_p(s, sp_), lpp)))
        if abs(s) > 50:
            break
    return dict(k=k, lam_ir=lp0, sigma_p=sp_, lam_p=lam_p(s, sp_), sigma=s, ett=worst)


def u5_exact():
    R5, G5, A, lB = sp.symbols("R_5 G_5 A l_B", positive=True)
    R3 = R5 / sp.sqrt(3)
    G3 = G5 * lB ** 2 / (R5 ** 2 * A)
    c2 = 3 * R3 / (2 * G3)
    ok = sp.simplify(c2 - sp.sqrt(3) * R5 ** 3 * A / (2 * G5 * lB ** 2)) == 0
    k = sp.Symbol("k")
    roots = sp.solve(k ** 2 + 2 * sp.sqrt(3) * k - 16, k)
    grow = [r for r in roots if r.is_positive][0]
    return ok, sp.simplify(grow - (sp.sqrt(19) - sp.sqrt(3))) == 0


def report():
    print("U0 M's words:", words())
    print("U1 outside art, every cited source quoted:", u1())
    print("U2 F = 0 leaves the record's bulk exact; T quadratic in F:", u2())
    ok3, t = u3()
    print("U3 T_++ = %s (a sum of squares): %s" % (t, ok3))
    print("U4 1/g4^2 = s (R5/g5^2) ln(L_IR/R5), diverging as L_IR -> oo: %s %s" % u4())
    o28, o29, ett = u5_equations()
    print("U5 Einstein-Maxwell derived: (A.28) %s, (A.29) %s" % (o28, o29))
    f, f2 = flow(ett=ett), flow(h=5e-4)
    print("   IR exponent %.4f, lambda' %.4f (sqrt 3 = %.4f); UV sigma' %.6f, lambda' %.6f; tt residual %.1e; "
          "halved step moves sigma by %.1e" % (f["k"], f["lam_ir"], math.sqrt(3), f["sigma_p"], f["lam_p"], f["ett"],
                                             abs(f["sigma"] - f2["sigma"])))
    print("   Brown-Henneaux = MM (3.21), and the IR exponent exact:", u5_exact())


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("U0 words: %s" % r)
    r = u1(); ok.append(r); say("U1 the outside art quoted: %s" % r)
    r = u2(); ok.append(r); say("U2 unexcited, nothing changes: %s" % r)
    r = u3()[0]; ok.append(r); say("U3 the null condition kept for every F: %s" % r)
    c, d = u4(); r = c and d; ok.append(r); say("U4 the zero mode's coupling runs, not localized: %s" % r)
    o28, o29, ett = u5_equations()
    r = o28 and o29; ok.append(r); say("U5 MM's (A.28) and (A.29) derived from the metric: %s" % r)
    f, f2 = flow(ett=ett), flow(h=5e-4)
    r = (abs(f["lam_ir"] - math.sqrt(3)) < 1e-6 and abs(f["sigma_p"] - 1) < 1e-3 and abs(f["lam_p"] - 1) < 1e-3
         and f["ett"] < 1e-8 and abs(f["sigma"] - f2["sigma"]) < 1e-9)
    ok.append(r); say("U5 the flow from AdS3 x R^2 to AdS5, the unused tt component held, converged: %s" % r)
    a, b = u5_exact(); r = a and b; ok.append(r); say("U5 c_2 by Brown-Henneaux, the IR exponent: %s" % r)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    names = ("flip", "no_warp", "decaying", "a29")
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-9s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
