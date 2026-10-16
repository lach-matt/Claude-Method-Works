#!/usr/bin/env python3
"""c2_quantum.py -- item 445 (1), the re-posed C2 of BOUNCE-RESEARCH.md: does the quantum fields' stress tensor on the
null-shell collapse, multiplied by the plane, make an inner horizon?  M approved it ("1 - yes").  C1 (c1_inner.py) found
none in the classical background; the semiclassical mechanism of section 2 needs one.  Labels: computed (sympy, exact
where marked), imported (bounce_scope's central charge), estimate (marked), deduced.  Worked in the conversation; not
verified; not seated.  2026-10-16.

The approximation, stated once (it is the papers' own, 2011.07331 and 2506.04845, READ in BOUNCE-RESEARCH section 2):
the s-wave Polyakov stress tensor in ds^2 = -e^{2 rho} du dv, T_uu = -(hbar/(12 pi)) [(d_u rho)^2 - d_u^2 rho] + t_u
(likewise v), trace R/(24 pi), in the collapse's "in" vacuum (no flux from past null infinity; regular at the centre
before the shell), on the fixed background (first order in hbar), four-dimensional components T_ab/(4 pi r^2).

  Q0 (read) M's words: 445.
  Q1 (computed, exact) The incoming component.  Along an outgoing ray U after the shell, rho = (1/2) ln(f(r)/f(r_s))
     (r_s the radius at which U crossed the shell, C = -2 r_U), and T_vv = (hbar/(192 pi)) g(r) with g = 2 f f'' - f'^2;
     in four dimensions (hbar/(96 pi^2 r^2)) (-M/r^3 + 3 M^2/(2 r^4)): negative outside 3M/2 (the influx -L/(4 pi
     (2M)^2) at the horizon, L = hbar/(768 pi M^2), the Polyakov luminosity) and positive inside 3M/2.  In five
     dimensions (f = 1 - mu/r^2) positive inside sqrt(2/3) r_h.
  Q2 (computed, exact) The outgoing component in the in vacuum: T_UU/r_U^2 = (hbar/(48 pi)) (g(r) - g(r_s))/f(r)^2,
     an invariant ratio.  It returns the Hawking flux L at infinity on late rays (r_s -> 2M), and since g' = 2 f f'''
     with f''' > 0, g falls inward where f < 0: inside the trapped region T_UU > 0.
  Q3 (computed, exact) The trace: T_Uv/r_U = hbar R/(48 pi), R = -f'' > 0.  (The two mixed derivatives commute: the
     chart's integrability, checked as an encoding guard.)
  Q4 (computed, exact; deduced) The Misner-Sharp mass grows inward.  d_r m at fixed v = -(hbar/(48 pi)) B with
     B = -f'' - (g(r) - g(r_s))/(2 f(r)); B > 0 at every point of the trapped region, at both ends (f < 0 on (0, r_h),
     g monotone there, R > 0).  So m(v, r) > m(v, r_ah) for every r < r_ah and 2m/r > 1 down to the centre: no inner
     horizon.  Along outgoing rays dm/dv = (hbar/(192 pi)) (4 f f'' - f'^2): -L on the horizon, positive inside 7M/4.
     The plane's multiplier c scales every term and changes no sign.
  Q5 (computed; estimate where marked) Where the multiplier makes it large.  Near the centre B -> 7M/r^3 (5D: 10 mu/r^4),
     so the first-order mass gain is 7 hbar M/(96 pi r^2); with hbar l_P^2 -> c l_P^2 = pi ell^2/8 (bounce_scope B2)
     it equals M at r_1 = ell sqrt(7/768) = 0.0955 ell = 1.33 um -- inside ell, where the plane's hole is five-
     dimensional and the four-dimensional dual reading no longer applies (estimate: the first-order term is past its
     validity there, but it is positive all the way in).
  Q6 (deduced) What C2 settles.  The in vacuum's negative energy sits outside 3M/2 and shrinks the outer horizon; at
     the centre every component focuses.  So the neutral null delivery has no inner horizon classically (C1) nor at
     first order in the quantum fields, multiplied or not (Q4): Barcelo et al.'s growth (eqs. 64, 68) has nothing to
     amplify, and C3 does not run on it.  The proof needs the inner horizon from elsewhere, and the one established
     physics offers is a charge's: with a charge f''' changes sign inside (the "tidal" mutant), the trapped region
     stops short of the centre, and the stress tensor at that inner horizon is the one 2011.07331 and 2506.04845
     amplify into the black-to-white transition.  That is the near-extremal Reissner-Nordstrom mouth of 445 (2)'s
     device: route A continues through route B's mouths.

python3 c2_quantum.py [--selftest | --mutants]
"""
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
sys.path.insert(0, HERE)
import bounce_scope  # noqa: E402  -- the plane's central charge and constants, imported, not copied

MUT = set()
WORDS = ("2 - Should I compute this wormhole on the plane as the corridor? - yes",)
r, rs, M, mu = sp.symbols("r r_s M mu", positive=True)
P12 = 1 / (12 * sp.pi)                                                  # Polyakov's coefficient, hbar = 1, one field


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def fam(n):
    """f = 1 - mu/r^n: n = 1 the large end (mu = 2M, four dimensions), n = 2 the small (five)"""
    f = 1 - mu / r ** n
    if "tidal" in MUT and n == 1:                                       # a positive charge term: an inner horizon
        f = f + sp.Rational(3, 20) * mu ** 2 / r ** 2
    return f


def g_of(f):
    return 2 * f * sp.diff(f, r, 2) - sp.diff(f, r) ** 2


def components(f):
    """T_vv, T_UU/r_U^2, T_Uv/r_U (two-dimensional, hbar = 1) and the commutator of the mixed derivatives"""
    fs = f.subs(r, rs)
    rU, rsU, rho = -f / (2 * fs), -sp.Rational(1, 2), sp.log(f / fs) / 2   # r*(r) - r*(r_s) = (v - v0)/2; C = -2 r_U
    if "boulware" in MUT:                                               # vacuum w.r.t. Schwarzschild u, not the in one
        rU, rsU, rho = -f / 2, 0, sp.log(f) / 2
    DU = lambda e: sp.diff(e, r) * rU + sp.diff(e, rs) * rsU            # noqa: E731  along fixed v
    Dv = lambda e: sp.diff(e, r) * f / 2                                # noqa: E731  along fixed U (r_s fixed)
    Tvv = -P12 * (Dv(rho) ** 2 - Dv(Dv(rho)))
    TUU = -P12 * (DU(rho) ** 2 - DU(DU(rho)))
    TUv = -P12 * DU(Dv(rho))
    if "no_anomaly" in MUT:
        TUv = 0 * TUv
    comm = sp.simplify(DU(Dv(rho)) - Dv(DU(rho)))
    return sp.simplify(Tvv), sp.simplify(TUU / rU ** 2), sp.simplify(TUv / rU), comm


def q1():
    f = fam(1)
    Tvv, _, _, _ = components(f)
    ok_form = sp.simplify(Tvv - g_of(f) / (192 * sp.pi)) == 0
    T4 = sp.simplify((Tvv / (4 * sp.pi * r ** 2)).subs(mu, 2 * M))
    ok_4d = sp.simplify(T4 - (-M / r ** 3 + sp.Rational(3, 2) * M ** 2 / r ** 4) / (96 * sp.pi ** 2 * r ** 2)) == 0
    root = [s for s in sp.solve(sp.Eq(T4, 0), r) if s.is_positive]
    L = 1 / (768 * sp.pi * M ** 2)
    horizon = sp.simplify(T4.subs(r, 2 * M) + L / (4 * sp.pi * (2 * M) ** 2)) == 0
    f5 = fam(2)
    T5 = components(f5)[0]
    root5 = [s for s in sp.solve(sp.Eq(T5, 0), r) if s.is_positive]
    return ok_form and ok_4d, root, horizon, root5


def q2():
    out = {}
    for n in (1, 2):
        f = fam(n)
        _, TUUr, _, _ = components(f)
        out[n] = sp.simplify(TUUr - (g_of(f) - g_of(f).subs(r, rs)) / (48 * sp.pi * f ** 2)) == 0
    f = fam(1).subs(mu, 2 * M)
    _, TUUr, _, _ = components(fam(1))
    TuSuS = sp.simplify((TUUr * f ** 2 / 4).subs(mu, 2 * M))            # r_{u_S} = -f/2 outside
    hawking = sp.limit(sp.limit(TuSuS, rs, 2 * M), r, sp.oo)
    return out, sp.simplify(hawking - 1 / (768 * sp.pi * M ** 2)) == 0


def q3():
    out = {}
    for n in (1, 2):
        f = fam(n)
        _, _, TUvr, comm = components(f)
        out[n] = (sp.simplify(TUvr + sp.diff(f, r, 2) / (48 * sp.pi)) == 0, comm == 0)
    return out


def bracket(f):
    """B with d_r m|_v = -(hbar/(48 pi)) B, from the components as computed (not from the closed forms)"""
    Tvv, TUUr, TUvr, _ = components(f)
    Trv = TUvr - (f / 2) * TUUr                                          # T_rv = T_Uv/r_U - (r_v/r_U^2) T_UU
    return sp.simplify(48 * sp.pi * Trv), Tvv, TUvr


def q4():
    out = {}
    for n in (1, 2):
        f = fam(n)
        B, Tvv, TUvr = bracket(f)
        rh = [s for s in sp.solve(sp.Eq(f, 0), r) if s.is_positive]
        one_root = len(rh) == 1
        h = rh[0] if rh else mu
        inside_neg = bool(f.subs(r, h / 2) < 0) and one_root
        gp = sp.diff(g_of(f), r)
        gp_form = sp.simplify(gp - 2 * f * sp.diff(f, r, 3)) == 0
        gp_roots = [s for s in sp.solve(sp.Eq(gp, 0), r) if s.is_positive]
        g_monotone = gp_roots == rh and bool(gp.subs(r, h / 2) < 0)
        R_pos = bool(sp.simplify(-sp.diff(f, r, 2)).is_positive)
        Bf = sp.lambdify((r, rs, mu), B, "math")
        grid_ok, worst = True, float("inf")
        hv = float(h.subs(mu, 1))
        for i in range(1, 41):
            sv = hv * i / 40
            for j in range(1, 40):
                rv = sv * j / 40
                if rv >= sv:
                    continue
                b = Bf(rv, sv, 1.0)
                worst = min(worst, b)
                grid_ok = grid_ok and b > 0
        dmdv = sp.simplify(Tvv - TUvr * f / 2)
        out[n] = dict(trapped_to_centre=inside_neg, g_monotone=gp_form and g_monotone, R_pos=R_pos, grid=grid_ok,
                      worst=worst, dmdv=dmdv)
    d4 = sp.simplify(out[1]["dmdv"].subs(mu, 2 * M))
    roots = [s for s in sp.solve(sp.Eq(d4, 0), r) if s.is_positive]
    L = 1 / (768 * sp.pi * M ** 2)
    at_h = sp.simplify(d4.subs(r, 2 * M) + L) == 0
    return out, roots, at_h


def q5():
    B4 = bracket(fam(1))[0]
    B5 = bracket(fam(2))[0]
    lead4 = sp.limit(sp.simplify(B4.subs(mu, 2 * M)) * r ** 3, r, 0)
    lead5 = sp.limit(B5 * r ** 4, r, 0)
    c = bounce_scope.central_charge()
    eff = c * bounce_scope.LP ** 2                                       # hbar l_P^2 -> c l_P^2 = pi ell^2/8
    r1 = math.sqrt(7 * eff / (96 * math.pi))
    return lead4, lead5, c, r1, r1 / bounce_scope.ELL


def report():
    print("Q0 M's words:", words())
    ok, root, hor, root5 = q1()
    print("Q1 T_vv = g/(192 pi): %s; 4D zero at r = %s, the horizon influx -L/(16 pi M^2): %s; 5D zero at r = %s"
          % (ok, root, hor, root5))
    o2, hk = q2()
    print("Q2 T_UU/r_U^2 = (g(r) - g(r_s))/(48 pi f^2): 4D %s, 5D %s; Hawking flux L at infinity: %s"
          % (o2[1], o2[2], hk))
    o3 = q3()
    print("Q3 T_Uv/r_U = R/(48 pi), mixed derivatives commute: 4D %s, 5D %s" % (o3[1], o3[2]))
    o4, roots, at_h = q4()
    for n, tag in ((1, "4D"), (2, "5D")):
        d = o4[n]
        print("Q4 %s trapped to the centre %s, g monotone %s, R > 0 %s, B > 0 on the grid %s (least %.3g)"
              % (tag, d["trapped_to_centre"], d["g_monotone"], d["R_pos"], d["grid"], d["worst"]))
    print("   dm/dv along outgoing rays: zero at r = %s, -L on the horizon: %s" % (roots, at_h))
    l4, l5, c, r1, x = q5()
    print("Q5 B -> %s/r^3 (4D), %s/r^4 (5D); c = %.3e; the first-order gain reaches M at r_1 = %.3f um = %.4f ell"
          % (l4, l5, c, r1 * 1e6, x))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r1 = words(); ok.append(r1); say("Q0 words: %s" % r1)
    form, root, hor, root5 = q1()
    r1 = form and root == [sp.Rational(3, 2) * M] and hor and root5 == [sp.sqrt(6) * sp.sqrt(mu) / 3]; ok.append(r1)
    say("Q1 T_vv: negative outside 3M/2, the horizon influx, positive inside (5D: sqrt(2/3) r_h): %s" % r1)
    o2, hk = q2()
    r1 = o2[1] and o2[2] and hk; ok.append(r1); say("Q2 T_UU in the in vacuum, the Hawking flux: %s" % r1)
    o3 = q3()
    r1 = all(a and b for a, b in o3.values()); ok.append(r1); say("Q3 the trace, the chart's integrability: %s" % r1)
    o4, roots, at_h = q4()
    r1 = all(d["trapped_to_centre"] and d["g_monotone"] and d["R_pos"] and d["grid"] for d in o4.values())
    r1 = r1 and roots == [sp.Rational(7, 4) * M] and at_h; ok.append(r1)
    say("Q4 the mass grows inward at both ends; dm/dv -L on the horizon, positive inside 7M/4: %s" % r1)
    l4, l5, c, r1v, x = q5()
    r1 = l4 == 7 * M and l5 == 10 * mu and abs(x - math.sqrt(7 / 768)) < 1e-4 and abs(r1v * 1e6 - 1.333) < 2e-3
    ok.append(r1); say("Q5 B -> 7M/r^3 and 10 mu/r^4; r_1 = 0.0955 ell = 1.333 um: %s" % r1)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    names = ("tidal", "boulware", "no_anomaly")
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-10s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
