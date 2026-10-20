#!/usr/bin/env python3
"""bounce_close.py -- item 537: what item 536 left open, closed.  M: "should the ten rows on 273 rest on this
quantum-mechanical definition instead of transition5q? - yes and is probably supported by our current candidate
theory."; "what stays open: - let's finish closing everything please".  536 (bounce_qm.py) defined the bounce in
quantum mechanics and left five things open: where the bounce sits (the clock's spread), the small end's Lambda
spread, the uniform interior, the clock, and the reflection rule.  Each is closed here, or its remaining premise
named.  Labels: computed (exact unless marked), deduced, READ, M's.  Worked in the conversation; not verified; not
seated.  2026-10-20.

  C0 (M's) 537.
  C1 (computed, exact; READ) The clock.  Along the interior the bulk's clock T (twice the five-volume per cell) and
     proper time obey dT/dtau = 2 sqrt(xi) Y > 0: T is a monotone function of proper time, finite at the singularity
     (at Lambda = 0, T_left = (2 r_h tau - tau^2)^2/2 with tau the proper time left), and globally unbounded, the
     five-volume.  So it is a slow clock in Gotay and Demaret's sense and not a reparametrisation of a fast one -- the
     subtlety Gielen and Menendez-Pidal name (arXiv 2205.15387, READ: "the clock variable must be valued over the
     entire real line"; "unitarity for a clock that encounters a classical singularity at finite time implies quantum
     singularity resolution").  Deduced: with a fast clock the singularity is never reached and nothing continues past
     it, so the README would end at r = 0, against 491 (released whole at position 2) and 418 (the interior's map
     unitary on it); the record's own content requires a slow clock, and the bulk supplies one with no added matter.
  C2 (computed, exact; READ) The uniform interior.  Birkhoff in five dimensions with Lambda: for
     ds^2 = -e^(2a(t,r)) dt^2 + e^(2b(t,r)) dr^2 + r^2 dOmega_3^2 in vacuum, G_tr + Lambda g_tr = 0 forces d_t b = 0,
     the rest e^(-2b) = 1 - mu/r^2 - Lambda r^2/6 and a + b = a function of t alone: Schwarzschild-AdS5.  Inside the
     horizon the Killing field is spacelike, so the interior is exactly Kantowski-Sachs: bounce_qm's minisuperspace is
     the whole spherically symmetric sector, not a truncation of it (the record's 5D forms at both ends, as
     transition5q).  Off symmetry, the approach to a generic spacelike singularity is locally homogeneous (the BKL
     conjecture, READ through 2409.03006).
  C3 (computed) The reflection rule and the mass.  The five-dimensional mass function m = Y(1 + xi Y Y'^2)
     - Lambda Y^2/6 is exactly mu on every classical solution.  On the quantum state it is mu before and after the
     bounce, falls to <Y>(0) (about 0) at it, and returns in full: the quantum region's negative effective energy is the
     whole mass, paired by an equal positive one -- net zero, 273 (c)'s pairing under 183.  An asymmetric state comes
     out with a different mass (energy made at the bounce), which 386 (only information crosses) and 183 exclude.  So
     the extension is the mass-preserving one, the state symmetric under time reversal (273 (a)), and beta > 0 because
     E(N) > 0: the equal mass (H2) rests on these rulings and unitarity, not on 415's shared onset.
  C4 (computed; READ) Where the bounce sits: bounded below by effective field theory.  Before the bounce the quantum
     radius departs from the classical one by |delta Y|/Y = 1/(16 sigma^2 T^2) = 0.2736 (x/x_b)^2 (x the curvature
     variable, x_b its value at the bounce).  Gravity as an effective field theory (Donoghue, gr-qc/9405057, READ)
     admits quantum corrections of relative size l^2 R with order-one coefficients, important only near the Planck
     curvature; so x_b >= 0.27 for coefficient one, and at x_b = 1 the deviation 0.27 x^2 lies inside it.
  C5 (computed) The candidate theory supports it (M, 537).  At x_b = 1 the least sphere is transition5q's exactly
     (72^(1/4) sqrt(mu) l5); the curvature's maximum is 0.742 l5^(-4) here (the semiclassical limit, universal) against
     transition5q's 0.2917 (H7), the same order; both give one transition surface between two horizons, the white hole
     of the black hole's mass and 2 r_h/c.  The place x_b = 1 is the candidate theory's (415's scales), and effective
     field theory admits it.
  C6 (deduced) The small end's Lambda spread.  In minisuperspace the bounce's place maps to sigma_Lambda L_z, the
     fiducial cell's freedom, which is not physical; with the place fixed by curvature (C4, C5) nothing the rows use
     depends on the cell or on Lambda's spread, and inside the hole that spread is negligible for any cell above
     4.4e-26 m (bounce_qm Q8).  The 1.1e4 m bound was that reading's, superseded as the scale's source.

What remains beyond established physics, named: quantum mechanics applied to general relativity's own minisuperspace
(the Wheeler-DeWitt equation with unitarity in the bulk's clock), which is quantum mechanics and general relativity but
not an established theory of quantum gravity; and the place x_b = 1, the candidate theory's, which effective field
theory admits and bounds below.  The equal mass no longer rests on 415.

python3 bounce_close.py [--selftest | --mutants]
"""
import os, sys, math, importlib.util
import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
mp.mp.dps = 30


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


BQ = _load("bounce_qm.py", "bc_bq")


def clock():
    """C1: T against proper time along the interior"""
    mu, tau, Lam, k, x0, Y = sp.symbols("mu tau Lambda k xi0 Y", positive=True)
    Yt = 2 * sp.sqrt(mu) * tau - tau ** 2                         # Lambda = 0, k = 3: Y as a function of tau left
    s = Yt ** 2 / 2                                                # clock time left, Y^2 = 2 s
    xi = mu - Yt
    rate = sp.simplify(sp.diff(s, tau) - 2 * sp.sqrt(xi) * Yt)    # ds/dtau = 2 sqrt(xi) Y
    # the left side is (2 Y)(sqrt(mu) - tau), the right 2 Y sqrt((sqrt(mu) - tau)^2): equal for tau < sqrt(mu)
    ok = sp.simplify(rate.subs(tau, sp.sqrt(mu) / 3)) == 0 and sp.simplify(rate.subs(tau, sp.sqrt(mu) / 7)) == 0
    mono = sp.simplify(sp.diff(s, tau).subs(tau, sp.sqrt(mu) / 2)) > 0
    finite = s.subs(tau, 0) == 0 and Yt.subs(tau, sp.sqrt(mu)) == mu       # T and tau both finite across the interior
    # general Lambda: dT/dtau = 2 sqrt(xi) Y from g_TT = -1/(4 xi Y^2), positive wherever xi > 0, Y > 0
    return dict(rate=ok, mono=mono, finite=finite)


def birkhoff():
    """C2: spherically symmetric vacuum with Lambda in five dimensions is Schwarzschild-AdS5"""
    t, r, c, th, ph, Lam, mu = sp.symbols("t r chi theta phi Lambda mu")
    a, b = sp.Function("a")(t, r), sp.Function("b")(t, r)
    X = (t, r, c, th, ph)
    g = sp.diag(-sp.exp(2 * a), sp.exp(2 * b), r ** 2, r ** 2 * sp.sin(c) ** 2,
                r ** 2 * sp.sin(c) ** 2 * sp.sin(th) ** 2)
    gi, G, riem = BQ._curv(g, X)
    Ric = sp.zeros(5, 5)
    for i in range(5):
        for j in range(i, 5):
            Ric[i, j] = Ric[j, i] = sp.simplify(sum(riem(m, i, m, j) for m in range(5)))
    R = sp.simplify(sum(gi[i, i] * Ric[i, i] for i in range(5)))
    E = sp.simplify(Ric - R * g / 2 + Lam * g)
    Etr = sp.simplify(E[0, 1])
    tr_ok = sp.simplify(Etr + 3 * sp.diff(b, t) / r) == 0 or sp.simplify(Etr - 3 * sp.diff(b, t) / r) == 0
    # with d_t b = 0 and a = -b + c(t): the remaining equations hold for e^(-2b) = 1 - mu/r^2 - Lambda r^2/6
    f = 1 - mu / r ** 2 - Lam * r ** 2 / 6
    if "birkhoff_f" in MUT:
        f = 1 - mu / r - Lam * r ** 2 / 6
    cf = sp.Function("C")(t)
    sub = {b: -sp.log(f) / 2, a: sp.log(f) / 2 + cf}
    res = [sp.simplify((gi[i, i] * E[i, i]).subs(sub).doit()) for i in range(5)]
    return dict(tr=tr_ok, solved=all(x == 0 for x in res))


def mass():
    """C3: the mass function, classical and on the quantum states"""
    k, x0, Lam, s = sp.symbols("k xi0 Lambda s", positive=True)
    Y = sp.sqrt(2 * k * s / 3)
    xi = x0 + 3 / k ** 2 * (Lam * Y ** 2 / 2 - 3 * Y)
    Yd = -sp.diff(Y, s)                                             # d/dT = -d/ds
    m = Y * (1 + xi * Y * Yd ** 2) - Lam * Y ** 2 / 6
    cl = sp.simplify(m - x0 * k ** 2 / 9) == 0
    # the quantum symmetric state in the semiclassical limit (Lambda_c = 0)
    p = dict(kc=300.0, sk=2.0, Lc=0.0, sg=1e-7, xi0=1e6)
    kv = {a: BQ.kav(a, p) for a in (0.5, -1, -1.5)}
    xf = lambda T: BQ.xicf(T, p, kv); yf = lambda T: BQ.Ycf(T, p, kv)
    def meff(T):
        Y_, Yd_ = yf(T), mp.diff(yf, T)
        return Y_ * (1 + xf(T) * Y_ * Yd_ ** 2) - p["Lc"] * Y_ ** 2 / 6
    Tf = mp.mpf(60) / p["sg"]
    mu_cl = p["xi0"] * kv[2] / 9 if 2 in kv else p["xi0"] * BQ.kav(2, p) / 9
    m_in, m_out, m0 = meff(-Tf), meff(Tf), meff(mp.mpf(0))
    # the asymmetric state (bounce_qm's grid): xi0 in 0.7 -> out 1.3 at k_c = 30: the mass changes
    P = BQ.PAR; Gd = BQ.grid()
    cl0 = lambda T: float(BQ.xicf(T, P, {a: BQ.kav(a, P) for a in (0.5, -1, -1.5)}, beta=0.0))
    xin = 0.7 if "asym_equal" not in MUT else 1.0
    _, _, a_in = BQ.moments(-40.0, P, Gd, xin=xin)
    _, _, a_out = BQ.moments(40.0, P, Gd, xin=xin)
    dmu = ((a_out - cl0(40.0)) - (a_in - cl0(-40.0))) * P["kc"] ** 2 / 9
    return dict(classical=cl, m_in=m_in, m_out=m_out, m0=m0, mu=mu_cl, dmu_asym=dmu)


def eft():
    """C4: the quantum radius's departure before the bounce, against (x/x_b)^2"""
    p = dict(kc=300.0, sk=2.0, Lc=0.0, sg=1e-3, xi0=1e6)
    kv = {a: BQ.kav(a, p) for a in (0.5, -1, -1.5)}
    Ymin = BQ.Ycf(0, p, kv)
    rows = []
    for sT in (10, 30, 100):
        T = mp.mpf(sT) / p["sg"]
        Ycl = mp.sqrt(mp.mpf(2) / 3) * kv[0.5] * mp.sqrt(T)
        d = abs(BQ.Ycf(T, p, kv) / Ycl - 1)
        xr = Ymin ** 2 / Ycl ** 2
        rows.append(dict(sT=sT, d=d, pred=mp.mpf("0.2736") * xr ** 2, d16=1 / (16 * mp.mpf(sT) ** 2), xr=xr))
    coef = 1 / (16 * (mp.gamma(0.75) ** 2 / mp.pi) ** 2)            # 1/(16 (Gamma(3/4)^2/pi)^2)
    return dict(rows=rows, coef=coef, xb_min=coef, inside=all(coef * x ** 2 <= x for x in (0.1, 0.5, 1.0)))


def support():
    """C5: against transition5q at x_b = 1"""
    TQ = _load("transition5q.py", "bc_tq")
    s = TQ.scales(mp.mpf(10) ** 12)
    Kt = max(TQ.kret(s, s["TT"] + mp.mpf(j) / 10) for j in range(-20, 21))
    pmin = 2 * s["k"] * s["mu"]
    ybound = mp.mpf(72) ** 0.25 * mp.sqrt(s["mu"])                 # l5 = 1
    Kf = BQ.kretschmann_eff()
    p = dict(kc=300.0, sk=2.0, Lc=0.0, sg=1e-7, xi0=1e6)
    kv = {a: BQ.kav(a, p) for a in (0.5, -1, -1.5)}
    xf = lambda T: BQ.xicf(T, p, kv); yf = lambda T: BQ.Ycf(T, p, kv)
    d = [mp.diff(xf, 0, n) for n in (0, 1, 2)] + [mp.diff(yf, 0, n) for n in (0, 1, 2)]
    mu = p["xi0"] * BQ.kav(2, p) / 9
    ratio = abs(Kf(*d)) / (72 * mu ** 2 / yf(0) ** 4)
    return dict(K_t5q=Kt, pmin=pmin, ybound=ybound, ratio_qm=ratio)


def compute():
    return dict(clock=clock(), birk=birkhoff(), mass=mass(), eft=eft(), sup=support())


def checks(o):
    c1 = all(o["clock"].values())
    c2 = all(o["birk"].values())
    m = o["mass"]
    c3 = (m["classical"] and abs(m["m_in"] / m["m_out"] - 1) < 1e-8 and abs(m["m_in"] / m["mu"] - 1) < 1e-2
          and m["m0"] / m["mu"] < 1e-3 and abs(m["dmu_asym"] - 0.6 * 900 / 9) < 1.0)
    e = o["eft"]
    c4 = all(abs(r["d"] / r["d16"] - 1) < 2e-2 and abs(r["d"] / r["pred"] - 1) < 2e-2 for r in e["rows"]) and \
        abs(e["coef"] - 0.27355) < 1e-4 and e["inside"]
    sp_ = o["sup"]
    c5 = (abs(sp_["pmin"] / sp_["ybound"] - 1) < 1e-20 and abs(sp_["K_t5q"] - 0.2917) < 1e-3
          and abs(sp_["ratio_qm"] - 0.7424) < 2e-3 and 1 < sp_["ratio_qm"] / sp_["K_t5q"] < 3)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5)


def report(o=None):
    o = o or compute(); ck = checks(o)
    print("C0 (M's) 537: the ten rows on bounce_qm; close what 536 left open")
    print("C1 the clock: T monotone in proper time, finite at the singularity, the five-volume: %s %s"
          % (o["clock"], ck["C1"]))
    print("C2 Birkhoff in five dimensions with Lambda; the interior exactly Kantowski-Sachs: %s %s"
          % (o["birk"], ck["C2"]))
    m = o["mass"]
    print("C3 mass function: classical %s; quantum m_in/mu %.6f, m_out/m_in %.10f, at the bounce m/mu %.2e; "
          "asymmetric state dmu %.2f (k_c = 30): %s" % (m["classical"], m["m_in"] / m["mu"], m["m_out"] / m["m_in"],
                                                         m["m0"] / m["mu"], m["dmu_asym"], ck["C3"]))
    for r in o["eft"]["rows"]:
        print("   sigma T %4d: |dY|/Y %.4e, 1/(16 (sigma T)^2) %.4e, 0.2736 (x/x_b)^2 %.4e (x/x_b %.4f)"
              % (r["sT"], r["d"], r["d16"], r["pred"], r["xr"]))
    print("C4 coefficient %.4f; effective field theory bounds x_b >= %.2f; at x_b = 1 inside: %s"
          % (o["eft"]["coef"], o["eft"]["xb_min"], ck["C4"]))
    s = o["sup"]
    print("C5 least sphere transition5q/bounce_qm %.12f; l5^4 K max: transition5q %.4f, bounce_qm %.4f: %s"
          % (s["pmin"] / s["ybound"], s["K_t5q"], s["ratio_qm"], ck["C5"]))
    return ck


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0
    for m in ("birkhoff_f", "asym_equal"):
        MUT.clear(); MUT.add(m)
        try:
            ok = selftest(quiet=True)
        except Exception:
            ok = False
        caught += not ok
        print("mutant %-11s %s" % (m, "caught" if not ok else "MISSED"))
    MUT.clear()
    print("%d/2 caught" % caught)
    return caught == 2


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    if "--selftest" in sys.argv:
        r = selftest(); print("selftest:", "PASS" if r else "FAIL"); sys.exit(0 if r else 1)
    report()
