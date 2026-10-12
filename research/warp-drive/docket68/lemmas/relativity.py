#!/usr/bin/env python3
"""relativity.py -- item 324: "everything that can exist with or without mass is subject to relativity. - this must be
proved for us to continue."  Item 323 left general relativity in the bulk as the record's framework, taken as given;
M confirms 276's reading (a presence that changed ours would be position 2 acting on ours) and orders the framework
proved.  Proved here kind by kind -- what can exist, how it moves, how it gravitates, what law the one metric obeys,
and what carries information -- with the one constant relativity leaves open in five dimensions computed through to
item 322's offset.  Worked in the conversation (computed with sympy, exact where marked; READ where marked; deduced
where marked; estimates labelled; not verified by a separate session; not seated); 2026-10-12.

  U0 (read) The words this rests on, verbatim in the rulings file: M's item 324; 101, "information is a form of
     energy"; 136 (G), "the README is the energy, not separate"; 120, "it only changes geometric state"; 137, "matter
     is neither created nor destroyed"; 320, "information or matter"; 276, "The passage is one-way in all aspects";
     and 137's record of "exactE.py's identity 4 pi r_min^2 = N A_bit".
  U1 (deduced; computed; READ) What can exist carries energy and momentum.  The record holds matter -- particles,
     scalar fields and gauge fields (pointwise P1-P3), with mass or without -- vacuum energy (the offsets, 201), the
     planes' tension, the bulk's geometry, and information, which M rules a form of energy (101) and the README the
     energy itself (136 (G)).  Each has a stress tensor: P1-P3's; -rho g for a vacuum; -tau h for a tension (pointwise
     P10); and information through its carrier -- Peres and Terno (quant-ph/0212023, READ): "information needs a
     material carrier, and the latter must obey the laws of physics.  Information is physical".  With or without
     mass alike: E^2 = p^2 c^2 + m^2 c^4, at m = 0 E = p c (computed).
  U2 (computed, exact; READ) Special relativity holds for every kind.  Under a Lorentz boost of any rapidity: the
     metric is kept (Lambda^T eta Lambda = eta); a particle's p.p is kept, so a massless one stays on the light cone,
     moving at c in every frame, and a massive one stays inside it, below c in every frame, both staying future-
     pointing; a scalar's Lagrangian, the gauge field's F^2 and E.B, a vacuum's stress -rho eta and a sheet's
     Nambu-Goto density sqrt(-det h) (boosts along the sheet) are each unchanged (computed).  Tested (READ): gravity and
     light travel at one speed to "-3 x 10^-15 and +7 x 10^-16" (GW170817 with GRB 170817A, arXiv:1710.05834); local
     Lorentz invariance is "well supported" (Will, arXiv:1403.7377).
  U3 (READ; computed) Gravitation is universal, with mass or without.  Will (READ): "if EEP is valid, then gravitation
     must be a 'curved spacetime' phenomenon", so "the only theories of gravity that can fully embody EEP" are metric
     theories, every non-gravitational field coupling to the one metric.  Deser (gr-qc/0411023, READ): a massless spin-2
     field coupled to matter must couple to the total stress tensor, its own included, which sums to Einstein's equations
     -- "Consistency has therefore led us to universal coupling, which implies the equivalence principle". The one
     metric's geodesics carry no mass and no composition: the equations of motion of m (1/2) g x'x' are those of (1/2) g
     x'x' for every m (computed), and light follows the same law with g x'x' = 0.  Its weak-field bending is (1 + gamma)
     2 G M/(c^2 b), 1.751 arcsec at the Sun's limb with gamma = 1 (computed).  Tested (READ): bodies of titanium and
     platinum fall alike to eta = [-1.5 +- 2.3 (stat) +- 1.5 (syst)] x 10^-15 (MICROSCOPE, arXiv:2209.15487); light is
     bent and delayed as general relativity says, gamma_EM - 1 = (2.1 +- 2.3) x 10^-5 (Cassini, quoted in
     arXiv:1710.05834); and gravity's own waves feel the same Shapiro delay as light, -2.6 x 10^-7 <= gamma_GW - gamma_EM
     <= 1.2 x 10^-6 (arXiv:1710.05834).  So the massless are gravitated as the massive are, and gravity itself is.
  U4 (READ; computed) The law of the one metric.  Lovelock's theorem (READ, Navarro and Navarro, arXiv:1005.2386):
     the symmetric, divergence-free second-order natural tensors of a metric in n dimensions are L_0, ..., L_p, p = the
     integer part of (n - 1)/2 -- in four dimensions the metric and Einstein's tensor (p = 1), so Einstein's equations
     with a cosmological constant are the only field equations our planes' world can have; in five, one more, the
     Gauss-Bonnet (Lanczos) tensor (p = 2) (computed).  Charmousis and Dufaux (hep-th/0202107, READ): R + 12 k^2 + alpha
     (Gauss-Bonnet) "is the most general action that will yield second order partial differential equations ... in 5
     dimensions"; "the Gauss-Codazzi integrability conditions are universal", while Israel's condition is generalised.
     So relativity fixes the bulk's law up to one constant, alpha, which Deser's consistency does not require and which
     Charmousis and Dufaux call "the leading order quantum correction".  Its effect on the record, computed: from their
     eq. (22) on its stable branch (READ), each side carries Sigma = 6 s sqrt(X) + 16 alpha X^(3/2), X = H^2 + q, s =
     sqrt(1 - 8 alpha k^2), q = (1 - s)/(4 alpha) (computed; per side, the junction being a sum of one-sided terms in
     each side's extrinsic curvature on the shared induced metric -- standard, not READ); p2_assume Q2's one-way split
     and Q3's flatness carry over in form (deduced); and item 322's offset becomes x+ = (d1/2)(1 - 4 alpha k1^2 +
     O(alpha^2)) (computed), positive for every alpha with which the bulk vacuum exists (8 alpha k1^2 <= 1, Charmousis
     and Dufaux) and our Newton constant is positive (alpha k1^2 > -3/8: below it our side's response (6 - 3 s)/sqrt(q)
     turns negative, gravity repelling) (computed; on a 400-point grid of that range) -- so B5a holds whatever alpha
     is, and d1/2 holds to the fraction 4 alpha k1^2, about 4e-39 if alpha is set by the five-dimensional Planck length
     the record's ell implies (estimate).  [Item 325: the estimate is withdrawn.  alpha is evaluated exactly in
     gb_alpha.py: B6''s coefficient 3/(4 pi), exact as 201 made it, reads (2 + s)/(4 pi (2 - s)) with alpha, so s = 1 and
     alpha = 0 in our bulk, and 201's k_R = k_L/2 with flatness gives alpha = 0 in position 2's; the factor here is 1.]
  U5 (READ; deduced) Information is subject to relativity.  Peres and Terno (READ): "relativistic causality cannot be
     violated by quantum measurements", and entanglement transmits nothing faster than light.  140's universal
     entanglement therefore signals nothing on its own; the README passes through the corridor's geometry, the bulk's
     causal structure (B4's light-reach), within relativity.  And the record's information gravitates: the README is
     its energy (136 (G)), and its N bits are an area of the throat, 4 pi r_min^2 = N A_bit (137) -- a gravitational
     quantity (deduced).
  U6 (deduced) The statement, proved.  Everything that can exist -- with mass or without: matter, light, gravity
     itself, vacuum energy, tension, information -- carries energy and momentum (U1), keeps the light cone in every
     frame (U2), couples to the one metric with one strength, falling alike and gravitating (U3), and carries
     information only so (U5); the one metric obeys Einstein's law in four dimensions and Einstein's law with at most
     one constant more in five (U4), whose effect on the record is computed and changes no sign.  General relativity in
     the bulk is therefore not assumed: the record's Israel and Gauss-Codazzi conditions are its law at the
     two-derivative order, exact if alpha = 0 and correct to the fraction alpha k^2 otherwise.  [Item 326, a finding
     recorded: this statement's two halves hold together only at alpha = 0.  "Gravity itself ... keeps the light cone"
     fails for alpha != 0 -- gravity's waves then travel on cones split from the light cone wherever the Weyl
     curvature is not zero, one outside it for either sign of alpha (gb_cone.py C4-C5) -- so U6 itself fixes the one
     constant U4 left: alpha = 0, and the law in five dimensions is Einstein's exactly.]
  U7 (the cypher NOT-RUN, stated) Universality is proved kind by kind; an index of (kind, Lorentz, couples, falls
     alike) rows would carry 1 in every cell -- a constant column on every axis, from which no language can measure
     anything, and the answer as its own column, a key (211).  Not run, and said.

What this does not prove.
  - Anything beyond the experiments' reach: U2's and U3's tests bound departures to their precision (1e-15 and the
    like); Lovelock's and Deser's theorems are exact on their premises (locality, second order, consistency).
  - The value of alpha: U4 computes its effect and shows no sign turns on it; the 4e-39 is an estimate.
    [Item 325: evaluated, alpha = 0 exactly on 201's definitions (gb_alpha.py B2-B3); the estimate is withdrawn.]
    [Item 326: and from U6 alone, without 201: gb_cone.py C7.]
  - A kind of thing with no energy and momentum at all: it would act on nothing and carry nothing, and the record admits
    none -- information is energy (101) and the bulk always holds information or matter (320).

Imports nothing from the record but the rulings file.  Stdlib + sympy.  python3 relativity.py [--selftest | --mutants]
"""
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ("everything that can exist with or without mass is subject to relativity. - this must be proved for us to "
         "continue.", "information is a form of energy", "the README is the energy, not separate",
         "it only changes geometric state", "matter is neither created nor destroyed", "information or matter",
         "The passage is one-way in all aspects", "exactE.py's identity 4 pi r_min^2 = N A_bit")
ETA = sp.diag(-1, 1, 1, 1)
y = sp.Symbol("y", real=True)                               # rapidity


def boost():
    if MUT.get("galilean"):
        v = sp.tanh(y)                                      # the mutant: a Galilean boost, t' = t, x' = x - v t
        return sp.Matrix([[1, 0, 0, 0], [-v, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    return sp.Matrix([[sp.cosh(y), sp.sinh(y), 0, 0], [sp.sinh(y), sp.cosh(y), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


def special():
    """U1-U2: E^2 = p^2 + m^2; every kind's invariants under a boost"""
    L = boost()
    keeps = sp.simplify(L.T * ETA * L - ETA) == sp.zeros(4)
    p, m = sp.symbols("p m", nonnegative=True)
    E = sp.sqrt(p ** 2 + m ** 2)
    massless = sp.simplify(E.subs(m, 0) - p) == 0
    px, py, pz = sp.symbols("p_x p_y p_z", real=True)
    k = sp.Matrix([sp.sqrt(px ** 2 + py ** 2 + pz ** 2), px, py, pz])
    kp = L * k
    null_kept = sp.simplify((kp.T * ETA * kp)[0]) == 0
    En = sp.Symbol("E_n", positive=True)
    kx = sp.Matrix([En, En, 0, 0])                          # a massless particle along x, the worst case
    future = sp.simplify((L * kx)[0] - En * sp.exp(y)) == 0  # E e^y > 0 for every y
    mm = sp.Symbol("mu", positive=True)
    q = sp.Matrix([sp.sqrt(px ** 2 + mm ** 2), px, 0, 0])
    qp = L * q
    mass_kept = sp.simplify((qp.T * ETA * qp)[0] + mm ** 2) == 0
    speed2 = sp.simplify((qp[1] ** 2 + qp[2] ** 2 + qp[3] ** 2) / qp[0] ** 2)
    below_c = sp.simplify(1 - speed2 - mm ** 2 / qp[0] ** 2) == 0  # 1 - v'^2 = mu^2/E'^2 > 0
    Li = L.inv()
    d = sp.Matrix(sp.symbols("d0:4", real=True))
    V = sp.Symbol("V", real=True)
    Ls = lambda dd: -(dd.T * ETA.inv() * dd)[0] / 2 - V
    scalar = sp.simplify(Ls(Li.T * d) - Ls(d)) == 0
    E3 = sp.Matrix(sp.symbols("E_x E_y E_z", real=True))
    B3 = sp.Matrix(sp.symbols("B_x B_y B_z", real=True))
    F = sp.zeros(4)
    for i in range(3):
        F[0, i + 1], F[i + 1, 0] = -E3[i], E3[i]
    F[1, 2], F[2, 1], F[2, 3], F[3, 2], F[3, 1], F[1, 3] = B3[2], -B3[2], B3[0], -B3[0], B3[1], -B3[1]
    Fp = Li.T * F * Li
    gi = ETA.inv()
    F2 = lambda G: sum(G[a, b] * (gi * G * gi)[a, b] for a in range(4) for b in range(4))
    gauge = sp.simplify(F2(Fp) - F2(F)) == 0
    eps = sp.LeviCivita
    FF = lambda G: sum(eps(a, b, c, e) * G[a, b] * G[c, e] for a in range(4) for b in range(4) for c in range(4)
                       for e in range(4))
    gauge_dual = sp.simplify(FF(Fp) - FF(F)) == 0           # E.B up to a constant
    rho = sp.Symbol("rho", real=True)
    T = -rho * ETA
    vacuum = sp.simplify(Li.T * T * Li - T) == sp.zeros(4)
    h = sp.diag(-1, 1, 1)                                   # the sheet's own 1 + 2 dimensions
    L3 = L[:3, :3]
    sheet = sp.simplify(-(L3.T * h * L3).det() - (-h.det())) == 0
    return dict(keeps=keeps, massless=massless, null_kept=null_kept, future=future, mass_kept=mass_kept,
                below_c=below_c, scalar=scalar, gauge=gauge, gauge_dual=gauge_dual, vacuum=vacuum, sheet=sheet)


def gravity():
    """U3: geodesics carry no mass; light bending with gamma"""
    t, r, ph = sp.symbols("t r phi", cls=sp.Function)
    s = sp.Symbol("s")
    f = sp.Function("f")
    m = sp.Symbol("m", positive=True)
    xs = [t(s), r(s), ph(s)]
    g = sp.diag(-f(r(s)), 1 / f(r(s)), r(s) ** 2)          # any static spherical metric, equatorial
    vel = sp.Matrix([x.diff(s) for x in xs])
    lag = lambda mass: mass * (vel.T * g * vel)[0] / 2
    extra = sp.Symbol("q", positive=True) * r(s) if MUT.get("mass_coupling") else 0   # the mutant: a force that knows m
    eqs = lambda lg: [sp.simplify(sp.diff(lg, x.diff(s)).diff(s) - sp.diff(lg, x)) for x in xs]
    e1 = eqs(lag(m) + extra)
    e0 = eqs(lag(1))
    mass_free = all(sp.simplify(a / m - b) == 0 for a, b in zip(e1, e0))
    G, M, c, b, gam = 6.67430e-11, 1.98841e30, 299792458.0, 6.957e8, 1.0
    defl = (1 + gam) * 2 * G * M / (c ** 2 * b) * 180 / math.pi * 3600
    return dict(mass_free=mass_free, deflection_arcsec=defl)


def lovelock():
    """U4: Lovelock's count p = floor((n - 1)/2); the Gauss-Bonnet side function and item 322's offset"""
    p = (lambda n: n // 2) if MUT.get("lovelock_count") else (lambda n: (n - 1) // 2)
    counts = {n: p(n) for n in (4, 5)}
    al, k = sp.symbols("alpha k", positive=True)
    X = sp.Symbol("X", positive=True)
    sgn = -1 if MUT.get("gb_sign") else 1                  # the mutant: the cubic term with the other sign
    s_ = sp.sqrt(1 - 8 * al * k ** 2)
    q_ = (1 - s_) / (4 * al)
    Fside = lambda kk, XX: 6 * sp.sqrt(1 - 8 * al * kk ** 2) * sp.sqrt(XX) + sgn * 16 * al * XX ** sp.Rational(3, 2)
    qk = lambda kk: (1 - sp.sqrt(1 - 8 * al * kk ** 2)) / (4 * al)
    einstein = sp.simplify(sp.limit(Fside(k, X), al, 0) - 6 * sp.sqrt(X)) == 0       # (kappa^2 = 1) Sigma = 6 sqrt(X)
    flat0 = sp.simplify(sp.limit(qk(k), al, 0) - k ** 2) == 0
    # first order in alpha: background F(k2, q2) = F(k1, q1)/2, response dF/dX at X = q, offset ratio
    k1 = sp.Symbol("k1", positive=True)
    a_ = sp.Symbol("a", real=True)                          # alpha k1^2, small
    ser = lambda e: sp.series(e, al, 0, 2).removeO()
    Fbg = lambda kk: ser(Fside(kk, qk(kk)))
    c1 = sp.Symbol("c1", real=True)
    k2 = k1 / 2 + c1 * al * k1 ** 3
    eq = sp.expand(ser(Fbg(k2) - Fbg(k1) / 2))
    c1v = sp.solve(sp.Eq(eq.coeff(al, 1), 0), c1)[0]
    resp = lambda kk: ser(sp.diff(Fside(kk, X), X).subs(X, qk(kk)))
    ratio = sp.simplify(ser(resp(k2.subs(c1, c1v)) / resp(k1)))
    xfrac = sp.expand(ser((ratio - 1) / 2) * 2)            # x+/(d1/2)
    first = sp.simplify(xfrac - (1 - 4 * al * k1 ** 2)) == 0
    # the full range: u = alpha k1^2 from -1 to 1/8 (vacuum exists for 8 alpha k^2 <= 1), k1 = 1
    def Fnum(u, kk):
        sv = math.sqrt(1 - 8 * u * kk ** 2)
        qv = (1 - sv) / (4 * u) if u != 0 else kk ** 2
        return 6 * sv * math.sqrt(qv) + sgn * 16 * u * qv ** 1.5, sv, qv
    def respnum(u, kk):
        _, sv, qv = Fnum(u, kk)
        if qv <= 0:
            return float("-inf")                            # no bulk curvature left: not a solution
        return 3 * sv / math.sqrt(qv) + sgn * 24 * u * math.sqrt(qv)
    pos, worst = True, None
    # the physical range: the bulk vacuum exists (8 u <= 1) and our Newton constant is positive, our side's response
    # 3 s/sqrt(q) + 24 alpha sqrt(q) = (6 - 3 s)/sqrt(q) > 0 for alpha < 0, i.e. u > -3/8 (computed below)
    g_sign = sp.simplify((3 * s_ + 24 * al * q_) - (6 - 3 * s_)) == 0
    u_floor = float(sp.solve(sp.Eq(6 - 3 * sp.sqrt(1 - 8 * a_), 0), a_)[0])
    grid = [u_floor + 1e-6 + i * ((0.125 - u_floor - 1e-6) / 400) for i in range(401)]
    for u in grid:
        if abs(u) < 1e-12:
            continue
        target = Fnum(u, 1.0)[0] / 2
        lo, hi = 1e-9, 1.0
        for _ in range(200):
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if Fnum(u, mid)[0] < target else (lo, mid)
        k2v = (lo + hi) / 2
        r1, r2 = respnum(u, 1.0), respnum(u, k2v)
        if r1 <= 0 or r2 <= 0:                              # a side whose gravity repels: outside the physical range
            pos = False
            continue
        xf = r2 / r1 - 1                                    # x+/(d1/2)
        if xf <= 0:
            pos = False
        worst = xf if worst is None or xf < worst else worst
    worst = worst if worst is not None else float("nan")
    # the natural size: alpha ~ l5^2, M5^3 = Mbar_Pl^2/ell (one-plane relation), k1 = 1/ell
    hbarc = 1.973269804e-16                                 # GeV m, standard
    ell = 13.964e-6 / hbarc                                 # GeV^-1, B6P-SCALE's ell (p2_gravity)
    Mpl_red = 2.435e18                                      # GeV, standard
    M5 = (Mpl_red ** 2 / ell) ** (1 / 3)
    u_nat = (1 / M5) ** 2 / ell ** 2
    return dict(counts=counts, einstein=einstein, flat0=flat0, xfrac=xfrac, first=first, pos=pos, worst=worst,
                g_sign=g_sign, u_floor=u_floor, M5=M5, u_nat=u_nat, shift=4 * u_nat)


def compute():
    return dict(sr=special(), gr=gravity(), lv=lovelock())


def report(o):
    sr, gr, lv = o["sr"], o["gr"], o["lv"]
    print("relativity.py -- everything that can exist, with or without mass, is subject to relativity (item 324)\n")
    print("U1 E = p c at m = 0: %s" % sr["massless"])
    print("U2 boost keeps eta %s; null kept %s, future %s; massive kept %s, below c %s; scalar %s; F^2 %s; E.B %s; "
          "vacuum %s; sheet %s" % (sr["keeps"], sr["null_kept"], sr["future"], sr["mass_kept"], sr["below_c"],
                                   sr["scalar"], sr["gauge"], sr["gauge_dual"], sr["vacuum"], sr["sheet"]))
    print("U3 geodesics carry no mass: %s; bending at the Sun's limb with gamma = 1: %.3f arcsec" % (
        gr["mass_free"], gr["deflection_arcsec"]))
    print("U4 Lovelock count p(4) = %s, p(5) = %s; side function -> Einstein %s, q -> k^2 %s; x+/(d1/2) = %s (first "
          "order %s); our G > 0 for alpha k1^2 > %.4f (%s); positive on that range to 1/8 %s (least %.3f); M5 = %.3g "
          "GeV, alpha k1^2 ~ %.2g, shift ~ %.2g (estimate)" % (
              lv["counts"][4], lv["counts"][5], lv["einstein"], lv["flat0"], lv["xfrac"], lv["first"], lv["u_floor"],
              lv["g_sign"], lv["pos"], lv["worst"], lv["M5"], lv["u_nat"], lv["shift"]))


def checks(o):
    sr, gr, lv = o["sr"], o["gr"], o["lv"]
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("U0 item 324, 101, 136 (G), 120, 137, 320, 276 and the exactE identity verbatim in the rulings file",
        all(w in rul for w in WORDS))
    add("U1-U2 a boost keeps the metric; the massless stay on the light cone and future, the massive inside it below c",
        sr["massless"] and sr["keeps"] and sr["null_kept"] and sr["future"] and sr["mass_kept"] and sr["below_c"])
    add("U2 a scalar's Lagrangian, F^2 and E.B, a vacuum's stress and a sheet's Nambu-Goto density are boost-invariant",
        sr["scalar"] and sr["gauge"] and sr["gauge_dual"] and sr["vacuum"] and sr["sheet"])
    add("U3 the one metric's geodesics carry no mass; light bending 1.751 arcsec with gamma = 1",
        gr["mass_free"] and abs(gr["deflection_arcsec"] - 1.751) < 0.002)
    add("U4 Lovelock: p(4) = 1, p(5) = 2; the Gauss-Bonnet side reduces to Einstein's; x+ = (d1/2)(1 - 4 alpha k1^2)",
        lv["counts"] == {4: 1, 5: 2} and lv["einstein"] and lv["flat0"] and lv["first"])
    add("U4 x+ positive for every alpha with a bulk vacuum and a positive Newton constant, -3/8 < alpha k1^2 <= 1/8 "
        "(B5a whatever alpha); the natural shift below 1e-37", lv["pos"] and lv["g_sign"]
        and abs(lv["u_floor"] + 0.375) < 1e-12 and lv["shift"] < 1e-37)
    return res


MUTANTS = {"galilean": "a Galilean boost in place of Lorentz's (U2)",
           "mass_coupling": "a force on bodies that knows their mass (U3)",
           "lovelock_count": "Lovelock's count read as floor(n/2) (U4)",
           "gb_sign": "the Gauss-Bonnet cubic term with the other sign (U4)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-15s %-50s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
