#!/usr/bin/env python3
"""stage3a_throat.py -- item 449, stage 3a of BOUNCE-RESEARCH section 13: the throat's five-dimensional section.  In
the throat the plane carries AdS2 x S^2 of radius r_e with the device's flux; the bulk beneath it flows from AdS5 to
AdS3 x S^2 (Maldacena and Milekhin 2008.06618, appendix A, eq. (A.30)).  This is the one-dimensional building block of
stage 3's two-dimensional solve, and its infrared is that solve's deep boundary condition.  M: "Continue".  Labels:
READ (MM, quoted in BOUNCE-RESEARCH section 9), computed (sympy exact; RK4 where marked), deduced.  Worked in the
conversation; not verified; not seated.  2026-10-16.

  T0 (read) M's word: 449.
  T1 (computed, exact) Einstein-Maxwell for ds^2 = e^{2 lam}(-dt^2 + dx^2) + e^{2 sig} dOmega_2^2 + drho^2 (R5 = 1),
     F = B sin(theta) dtheta ^ dphi, Lambda = -6, derived here from the metric: the rho-rho component is MM's first
     equation of (A.30) at beta = 8 pi G5 B^2/g5^2 = 6 lhat^-4, and (2 E_tt - E_thth + E_rhorho)/3 is their second.
  T2 (computed, exact) The infrared fixed point AdS3 x S^2: y = e^{-2 sig0} = (lhat^4 + sqrt(lhat^8 + 64 lhat^4))/8,
     so e^{-sig0} = lhat + lhat^3/16 + O(lhat^5) -- MM's (A.31) -- and lam'^2 = 3 + y/4 there: the AdS3 radius is
     R5/sqrt(3 + y/4), MM's R5/sqrt(3) with the sphere's correction.  The flow leaves it along the growing mode
     k = -sqrt(3 + y/4) + sqrt(19 + 9y/4) (exact; the planar exponent sqrt(19) - sqrt(3) at y = 0).
  T3 (computed, numerical; RK4) From that mode the flow reaches AdS5 (sig' -> 1, lam' -> 1) at every lhat taken; the
     tt component, which the integration does not use, holds along it, and halving the step moves the end by < 1e-9.
  T4 (computed) On our plane (R5 = ell), lhat = l_B/r_e with MM's (3.25) l_B (mmp_corridor): 0.513 at r_e = 10 ell,
     0.193 at 100 ell, 0.083 at the Earth cap; the sphere's correction to the AdS3 radius is -1.1%, -0.16% and -0.03%.
     MM's own case: lhat = 5.4e-6.
  T5 (deduced) The throat's five-dimensional section exists at the plane's numbers, as MM argue and now computed in
     one dimension: AdS5 at the plane, AdS3 x S^2 below it, the field-line circle to be closed through that AdS3 by
     the two-dimensional solve (stage 3b), whose discretization is put to M before it runs (414).

python3 stage3a_throat.py [--selftest | --mutants]
"""
import importlib.util
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ('"Continue"',)


def _load(name):
    spec = importlib.util.spec_from_file_location("s3a_" + name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def einstein_s2():
    t, x, th, ph, r = sp.symbols("t x theta phi rho")
    X = (t, x, th, ph, r)
    lam, sig = sp.Function("lam")(r), sp.Function("sig")(r)
    g = sp.diag(-sp.exp(2 * lam), sp.exp(2 * lam), sp.exp(2 * sig), sp.exp(2 * sig) * sp.sin(th) ** 2, 1)
    gi = g.inv()
    n = 5
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]

    def ric(b):
        return sp.simplify(sum(sp.diff(Gam[a][b][b], X[a]) for a in range(n))
                           - sum(sp.diff(Gam[a][b][a], X[b]) for a in range(n))
                           + sum(Gam[a][a][d] * Gam[d][b][b] for a in range(n) for d in range(n))
                           - sum(Gam[a][b][d] * Gam[d][b][a] for a in range(n) for d in range(n)))
    Rd = [ric(i) for i in range(n)]
    Rs = sp.simplify(sum(gi[i, i] * Rd[i] for i in range(n)))
    beta = sp.Symbol("beta")
    F2 = 2 * sp.exp(-4 * sig)                                           # F^2/B^2 (the sin^2 cancels)
    out = {}
    for i, name in ((0, "tt"), (2, "thth"), (4, "rr")):
        T = (sp.exp(-2 * sig) if i == 2 else 0) - g[i, i] * F2 / 4
        out[name] = sp.simplify((Rd[i] - g[i, i] * Rs / 2 - 6 * g[i, i] - beta * T) / g[i, i])
    d = {sp.Derivative(lam, (r, 2)): sp.Symbol("lpp"), sp.Derivative(sig, (r, 2)): sp.Symbol("spp")}
    d2 = {sp.Derivative(lam, r): sp.Symbol("lp"), sp.Derivative(sig, r): sp.Symbol("sp"), sig: sp.Symbol("s")}
    return {k: v.subs(d).subs(d2) for k, v in out.items()}


def t1():
    E = einstein_s2()
    lp, sp_, s, spp, beta, L = sp.symbols("lp sp s spp beta L")
    a1 = -6 - sp.exp(-2 * s) + 3 * L * sp.exp(-4 * s) + lp ** 2 + 4 * lp * sp_ + sp_ ** 2
    a2 = 4 + sp.exp(-2 * s) - 4 * L * sp.exp(-4 * s) - 2 * lp * sp_ - 2 * sp_ ** 2 - spp
    ok1 = sp.simplify(E["rr"].subs(beta, 6 * L) - a1) == 0
    ok2 = sp.simplify((2 * E["tt"] - E["thth"] + E["rr"]).subs(beta, 6 * L) / 3 + a2) == 0
    ett = sp.lambdify(sp.symbols("s sp spp lp lpp L"), E["tt"].subs(beta, 6 * L), "math")
    return ok1, ok2, ett


def fixed_point(lh):
    y = (lh ** 4 + math.sqrt(lh ** 8 + 64 * lh ** 4)) / 8
    if "planar" in MUT:
        y = lh ** 2
    lp0 = math.sqrt(3 + y / 4)
    k = -lp0 + math.sqrt(19 + 9 * y / 4)
    return y, lp0, k


def t2():
    lh, y = sp.symbols("lhat y", positive=True)
    L = 1 / lh ** 4
    yv = (lh ** 4 + sp.sqrt(lh ** 8 + 64 * lh ** 4)) / 8
    fp = sp.simplify((4 + yv - 4 * L * yv ** 2)) == 0                   # sig' = sig'' = 0 in (A.30)'s second
    ser = sp.series(sp.sqrt(yv), lh, 0, 6).removeO()
    a31 = sp.simplify(ser - (lh + lh ** 3 / 16)) == 0 or sp.simplify(sp.series(ser - lh - lh ** 3 / 16, lh, 0, 5)
                                                                         .removeO()) == 0
    lp2 = sp.simplify(6 + yv - 3 * L * yv ** 2 - (3 + yv / 4)) == 0     # the constraint at the fixed point
    a = sp.simplify(sp.diff(4 + sp.exp(-2 * sp.Symbol("s")) - 4 * L * sp.exp(-4 * sp.Symbol("s")), sp.Symbol("s"))
                    .subs(sp.Symbol("s"), -sp.log(yv) / 2))
    a_ok = sp.simplify(a - (16 + 2 * yv)) == 0                          # the linear coefficient, so k as stated
    return fp, a31, lp2, a_ok


def flow(lh, ett=None, rho_end=16.0, h=1e-3):
    """integrated in the deviation u = sig - sig0, with the fixed point's terms cancelled exactly (4 L y^2 = 4 + y):
    the forcing 4 + e^{-2 sig} - 4 L e^{-4 sig} = y expm1(-2u) - (4 + y) expm1(-4u), and the constraint's
    6 + e^{-2 sig} - 3 L e^{-4 sig} = (3 + y/4) + y expm1(-2u) - (3/4)(4 + y) expm1(-4u)"""
    L = lh ** -4
    y, lp0, k = fixed_point(lh)
    s0 = -0.5 * math.log(y)
    eps = 1e-7
    u, p = eps, k * eps

    def D(u, p):
        return 3 * p * p + (3 + y / 4) + y * math.expm1(-2 * u) - 0.75 * (4 + y) * math.expm1(-4 * u)

    def lam_p(u, p):
        return -2 * p + math.sqrt(max(D(u, p), 0.0))

    cs = -1.0 if "sphere_sign" in MUT else 1.0

    def acc(u, p):
        return cs * y * math.expm1(-2 * u) - (4 + y) * math.expm1(-4 * u) - 2 * lam_p(u, p) * p - 2 * p * p

    worst = 0.0
    for _ in range(int(round(rho_end / h))):
        k1s, k1p = p, acc(u, p)
        k2s, k2p = p + h / 2 * k1p, acc(u + h / 2 * k1s, p + h / 2 * k1p)
        k3s, k3p = p + h / 2 * k2p, acc(u + h / 2 * k2s, p + h / 2 * k2p)
        k4s, k4p = p + h * k3p, acc(u + h * k3s, p + h * k3p)
        u += h / 6 * (k1s + 2 * k2s + 2 * k3s + k4s)
        p += h / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
        if ett is not None:
            q = math.sqrt(D(u, p))
            spp = acc(u, p)
            e2, e4 = y * math.exp(-2 * u), y * y * math.exp(-4 * u)
            dls = (-2 * e2 + 12 * L * e4) / (2 * q)
            lpp = dls * p + (-2 + 3 * p / q) * spp
            worst = max(worst, abs(ett(s0 + u, p, spp, lam_p(u, p), lpp, L)))
    return dict(y=y, lp0=lp0, k=k, s0=s0, sig=s0 + u, u=u, sigma_p=p, lam_p=lam_p(u, p), ett=worst)


def plane_lhat():
    mc = _load("mmp_corridor")
    e = mc.ell()
    return {name: mc.point(r, e)["lB"] / r for name, r in (("10 ell", 10 * e), ("100 ell", 100 * e),
                                                          ("Earth cap", mc.R_EARTH_CAP))}, \
        mc.point(0.05 * mc.C, 50e-6)["lB"] / (0.05 * mc.C)


def report():
    print("T0 M's word:", words())
    o1, o2, ett = t1()
    print("T1 Einstein-Maxwell with the sphere derived: (A.30) first %s, second %s" % (o1, o2))
    print("T2 the fixed point, (A.31), lam'^2 = 3 + y/4, the growing mode (exact):", t2())
    lhs, mm = plane_lhat()
    for name, lh in list(lhs.items()) + [("MM's case", mm)]:
        f, f2 = flow(lh, ett), flow(lh, None, h=5e-4)
        print("T3-T4 %-9s lhat %.4g: e^-sig0 %.6g (lhat + lhat^3/16 = %.6g), R3/R5 %.6f (1/sqrt3 %.6f, %+.3f%%), "
              "k %.4f; AdS5 reached sig' %.6f lam' %.6f; tt %.1e; step-halving %.1e"
              % (name, lh, math.exp(-f["s0"]), lh + lh ** 3 / 16, 1 / f["lp0"], 1 / math.sqrt(3),
                 100 * (math.sqrt(3) / f["lp0"] - 1), f["k"], f["sigma_p"], f["lam_p"], f["ett"],
                 abs(f["u"] - f2["u"])))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("T0 words: %s" % r)
    o1, o2, ett = t1(); r = o1 and o2; ok.append(r); say("T1 MM's (A.30) derived from the metric: %s" % r)
    r = all(t2()); ok.append(r); say("T2 the infrared fixed point, (A.31), the AdS3 radius, the growing mode: %s" % r)
    lhs, mm = plane_lhat()
    r = abs(lhs["10 ell"] - 0.513) < 2e-3 and abs(lhs["Earth cap"] - 0.0832) < 5e-4 and abs(mm / 5.45e-6 - 1) < 1e-2
    ok.append(r); say("T4 lhat on the plane 0.513, 0.193, 0.083; MM's 5.4e-6: %s" % r)
    good = True
    for lh in list(lhs.values()) + [mm]:
        f, f2 = flow(lh, ett), flow(lh, None, h=5e-4)
        y, _, _ = fixed_point(lh)
        good &= (abs(f["sigma_p"] - 1) < 1e-4 and abs(f["lam_p"] - 1) < 1e-4 and f["ett"] < 1e-8
                 and abs(f["u"] - f2["u"]) < 1e-9
                 and abs(math.exp(-f["s0"]) - (lh + lh ** 3 / 16)) < 2 * lh ** 5 + 1e-15)
    ok.append(good); say("T3 the flow reaches AdS5 at every lhat, tt held, converged, (A.31) to O(lhat^5): %s" % good)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    names = ("planar", "sphere_sign")
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-11s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
