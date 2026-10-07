#!/usr/bin/env python3
"""stability.py -- wall E (stability), worked as mathematics (M-RULINGS item 149: "work the math now").

First written quoting Aretakis's extremal-Kerr Theorem 3 (tau^(k-1)) as if general and using an asymptotic bound for
early times; corrected (STABILITY.md History).  The finite-time result now comes from an exact horizon identity.

The corridor: Bronnikov-Kim eq. (17) at r0 = 2m (plane.py), -F dt^2 + dr^2/H + r^2 dOmega^2, F = 1 - 2m/r,
H = (1 - 2m/r)^2 / (1 - 3m/2r).  In Aretakis's form g = -D dv^2 + 2 dv drho + r(rho)^2 dOmega^2, drho = sqrt(F/H) dr.

READ: Aretakis, arXiv:1206.6598v2: abstract ("do not decay along such horizons as advanced time tends to infinity, and
in fact, higher order derivatives blow up"); eqs. (6)-(8) p.10 (extremality D = D' = 0); Prop. 3.2 p.10 (the hierarchy
"provided" D''(r_H) = 2K(r_H), eq. 10; "extremal Reissner-Nordstrom satisfies the condition (10)", p.11); Theorem 1
p.11 (non-decay, under A1-A4 only); Theorem 2 p.12 (blow-up, conditional: "unless psi and the tangential to H+
derivatives of psi do not decay and H[psi] = 0").  Theorem 3 p.15 ("asympotically", sic) is for extremal Kerr.

  S1  the corridor's horizon is extremal: D'(rho_H) = 0.  Control: the r0 = 1.8m member, D' = sqrt(10)/(10m)
  S2  it meets condition (10) exactly: D'' = 1/(2m^2) = 2K.  Control (READ): extremal RN meets it
  S3  the corridor's clock m/c = r_min(N)/(2c): 6.6e-37 s at the example README
  S4  the exact horizon identities for a spherical wave (derived here from the wave operator, generic D(rho), r(rho)):
        d/dv (d psi/d rho) = 0                       -> H0 = d psi/d rho is conserved exactly (beta_0 = 0: the throat
                                                       sits on the horizon, r' = 0)
        d/dv (d^2 psi/d rho^2) = -(D''/2) H0 - (r''/r) d psi/dv,  with D''/2 = 1/(4m^2), r''/r = 1/(2m^2) here
      so over an advanced time v the second derivative changes by -H0 v/(4m^2) - (psi(v) - psi(0))/(2m^2): linear growth
      with an exact coefficient, no unknown constant.  Over one clock (v = m) the linear part is H0/(4m), a quarter of
      the second derivative's natural size H0/m
  S5  the white-hole half of the wall.  READ: Bianchi, Christodoulou, D'Ambrosio, Haggard & Rovelli, arXiv:1802.04264v2
      p.7 (a secondary citation; the primary sources are Eardley 1974 and Barrabes-Brady-Poisson 1993, both about
      non-extremal white holes): "Generically, white holes are known to be unstable under perturbations ... The
      instability arises because modes of short-wavelength are exponentially blue-shifted along the white hole
      horizon."  The exponential rate is the surface gravity kappa = D'(rho_H)/2.  The corridor's is zero (S1), so the
      exponential blueshift is absent.  Control: the r0 = 1.8m member, kappa = sqrt(10)/(20m), e-folds every
      2 sqrt(10) m ~ 6.3 m.  At r0 = 2m the entry's future horizon and the exit's past horizon are ONE null surface
      (P1's two horizons merge), so S4's identities hold on the exit too
  S5b what remains at kappa = 0 is a power law, and it is unbounded.  Rays hugging the white-hole surface (side 2,
      rho~ < 0) obey d rho~/dv = D/2 = rho~^2/(8m^2): rho~(v) = rho~0/(1 - rho~0 v/(8m^2)) -> -8m^2/v, approaching the
      surface without reaching it; their spacing shrinks as (1 - rho~0 v/(8m^2))^-2 ~ v^-2, a blueshift growing as v^2.
      Control: the non-extremal near-horizon law d rho~/dv = kappa rho~ gives spacing e^(kappa v).  So the exponential
      mechanism is absent and a v^2 blueshift remains; whether it destabilises the exit is OPEN
Imports copy/chain.py's exact throat coefficient by path.  Stdlib + sympy.  python3 stability.py [--selftest]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
C = 299792458.0
EXAMPLE_N = 2742570311524972

r, m, s, M = sp.symbols("r m s M", positive=True)


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def D_derivatives(r0v, rH):
    """D = F as a function of rho, d rho/dr = sqrt(F/H).  Returns D'(rho) and D''(rho) at r -> rH (limits)."""
    F = 1 - 2 * m / r
    H = (1 - 2 * m / r) * (1 - r0v / r) / (1 - sp.Rational(3, 2) * m / r)
    drho_dr = sp.sqrt(F / H)
    D1 = sp.diff(F, r) / drho_dr                                    # dD/drho
    D2 = sp.diff(D1, r) / drho_dr                                   # d2D/drho2
    lim = lambda e: sp.limit(sp.simplify(e.subs(r, rH + s)), s, 0, "+")
    return lim(D1), lim(D2)


def transport():
    """Derive, for generic D(rho), r(rho), the horizon identities of a spherical wave psi(v, rho)."""
    v, rho = sp.symbols("v rho")
    Df, Rf = sp.Function("D")(rho), sp.Function("R")(rho)
    psi = sp.Function("psi")(v, rho)
    box = (sp.diff(Rf**2 * sp.diff(psi, rho), v) + sp.diff(Rf**2 * (sp.diff(psi, v) + Df * sp.diff(psi, rho)), rho)) / Rf**2
    d0, d1, d2, r0_, r1, r2 = sp.symbols("d0 d1 d2 R0 R1 R2")
    sub = {sp.Derivative(Df, (rho, 2)): d2, sp.Derivative(Df, rho): d1, Df: d0,
           sp.Derivative(Rf, (rho, 2)): r2, sp.Derivative(Rf, rho): r1, Rf: r0_}
    hz = {d0: 0, d1: 0, r1: 0}
    first = sp.solve(sp.Eq(sp.expand(box.subs(sub).subs(hz)), 0), sp.Derivative(psi, v, rho))
    second = sp.solve(sp.Eq(sp.expand(sp.diff(box, rho).subs(sub).subs(hz)), 0), sp.Derivative(psi, v, (rho, 2)))
    return {"first": first, "second": second, "syms": (d2, r0_, r2), "psi": psi, "v": v, "rho": rho}


def r_second(rH):
    """r''(rho) at the horizon: r_rho = sqrt(H/F), so r_rhorho = (1/2) d(H/F)/dr there."""
    F = 1 - 2 * m / r
    H = (1 - 2 * m / r) ** 2 / (1 - sp.Rational(3, 2) * m / r)
    return sp.limit(sp.Rational(1, 2) * sp.diff(sp.simplify(H / F), r).subs(r, rH + s), s, 0, "+")


def white_hole():
    """S5b: the side-2 rays hugging the white-hole surface, at kappa = 0 and (control) at kappa > 0."""
    v, kap = sp.symbols("v kappa", positive=True)
    a = sp.Symbol("a", positive=True)
    x0 = -a                                                         # rho~0 < 0: side 2
    xv = x0 / (1 - x0 * v / (8 * m**2))
    ode_ok = sp.simplify(sp.diff(xv, v) - xv**2 / (8 * m**2)) == 0 and sp.simplify(xv.subs(v, 0) - x0) == 0
    spacing = sp.simplify(-sp.diff(xv, a))                          # d rho~ / d rho~0, rho~0 = -a
    blue = sp.limit(1 / (spacing * v**2), v, sp.oo)                 # blueshift / v^2 -> constant
    xc = x0 * sp.exp(kap * v)                                       # control: d rho~/dv = kappa rho~
    ctl_ok = sp.simplify(sp.diff(xc, v) - kap * xc) == 0
    return {"ode_ok": ode_ok, "limit": sp.limit(xv * v, v, sp.oo), "spacing": spacing, "blue_over_v2": blue,
            "spacing_control": sp.simplify(-sp.diff(xc, a)), "control_ok": ctl_ok}


def compute():
    d1, d2 = D_derivatives(2 * m, 2 * m)                            # the corridor
    K = 1 / (2 * m) ** 2
    c1, _ = D_derivatives(sp.Rational(9, 5) * m, 2 * m)            # control: r0 = 1.8 m, horizon at 2m
    Drn = (1 - M / r) ** 2                                          # extremal RN (READ)
    rn_ok = sp.simplify(sp.diff(Drn, r, 2).subs(r, M) - 2 / M**2) == 0
    ch = _load(os.path.join(D68, "copy", "chain.py"), "st_chain")
    r1 = float(sp.N(sp.sympify(ch.coefficients()["r_min_m_per_sqrt_bit"]["exact"]), 20))
    rN = EXAMPLE_N ** 0.5 * r1
    t_m = rN / (2 * C)
    tr = transport()
    d2s, r0s, r2s = tr["syms"]
    rpp = r_second(2 * m)
    second = tr["second"][0]
    coeff_H0 = sp.simplify(second.coeff(sp.Derivative(tr["psi"], tr["rho"])).subs({d2s: d2}))
    coeff_dv = sp.simplify(second.coeff(sp.Derivative(tr["psi"], tr["v"])).subs({r2s: rpp, r0s: 2 * m}))
    return {"D1": d1, "D2": d2, "K": K, "cond10": sp.simplify(d2 - 2 * K) == 0, "control_D1": c1, "rn_ok": rn_ok,
            "rN": rN, "t_m": t_m, "t_m_per_sqrt_bit": r1 / (2 * C), "first": tr["first"], "rpp": rpp,
            "coeff_H0": coeff_H0, "coeff_dv": coeff_dv,
            "kappa": sp.simplify(d1 / 2), "kappa_control": sp.simplify(c1 / 2), "wh": white_hole()}


def report(d):
    print("stability.py -- wall E, the corridor's horizon (item 149)\n")
    print("S1 corridor: D'(rho_H) = %s (extremal); control r0 = 1.8m: D'(rho_H) = %s" % (d["D1"], d["control_D1"]))
    print("S2 D''(rho_H) = %s, 2K = %s: Aretakis's condition (10) holds: %s; extremal RN meets it: %s"
          % (d["D2"], 2 * d["K"], d["cond10"], d["rn_ok"]))
    print("S3 the corridor's clock m/c = %.3e s at the example README (r_min = %.3e m); %.3e s x sqrt(N)"
          % (d["t_m"], d["rN"], d["t_m_per_sqrt_bit"]))
    print("S4 on the horizon: d/dv(d psi/d rho) = %s (conserved); r''(rho_H) = %s; d/dv(d2 psi/d rho2) = (%s) H0 + (%s) dpsi/dv"
          % (d["first"][0] if d["first"] else 0, d["rpp"], d["coeff_H0"], d["coeff_dv"]))
    print("   over one clock (v = m) the linear part of the change is H0/(4m): a quarter of the natural size H0/m")
    print("S5 white-hole blueshift rate kappa: corridor %s (exponential blueshift absent); control r0 = 1.8m: %s, "
          "e-folding %s" % (d["kappa"], d["kappa_control"], sp.simplify(1 / d["kappa_control"])))
    w = d["wh"]
    print("S5b side-2 rays at kappa = 0: rho~ v -> %s; spacing %s (blueshift ~ v^2 x %s); control kappa > 0: spacing %s"
          % (w["limit"], w["spacing"], w["blue_over_v2"], w["spacing_control"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("S1: the corridor's horizon is extremal, D'(rho_H) = 0", d["D1"] == 0)
    chk("S1 control: the r0 = 1.8m horizon member is not extremal, D'(rho_H) != 0", d["control_D1"] != 0)
    chk("S2: D''(rho_H) = 1/(2 m^2) = 2K -- Aretakis's condition (10) holds exactly", d["cond10"]
        and sp.simplify(d["D2"] - 1 / (2 * m**2)) == 0)
    chk("S2 control (READ): extremal Reissner-Nordstrom meets condition (10)", d["rn_ok"])
    chk("S3: the corridor's clock at the example README is ~6.6e-37 s", 6.0e-37 < d["t_m"] < 7.2e-37)
    chk("S4: on the horizon the first derivative is conserved exactly (d/dv of it is zero)", d["first"] == [0])
    chk("S4: the second derivative changes at -H0/(4 m^2) - (1/(2 m^2)) dpsi/dv, exactly (r'' = 1/m)",
        sp.simplify(d["coeff_H0"] + 1 / (4 * m**2)) == 0 and sp.simplify(d["coeff_dv"] + 1 / (2 * m**2)) == 0)
    chk("S5: the corridor's surface gravity is zero, so the white hole's exponential blueshift is absent; control: "
        "the r0 = 1.8m member e-folds every 2 sqrt(10) m", d["kappa"] == 0
        and sp.simplify(1 / d["kappa_control"] - 2 * sp.sqrt(10) * m) == 0)
    w = d["wh"]
    a, kap, v = sp.Symbol("a", positive=True), sp.Symbol("kappa", positive=True), sp.Symbol("v", positive=True)
    chk("S5b: side-2 rays approach the white-hole surface as -8m^2/v and their spacing shrinks as v^-2 (blueshift ~ v^2, "
        "unbounded); control: at kappa > 0 the spacing grows as e^(kappa v)",
        w["ode_ok"] and sp.simplify(w["limit"] + 8 * m**2) == 0 and w["blue_over_v2"].is_positive
        and w["blue_over_v2"] != sp.oo and w["control_ok"] and sp.simplify(w["spacing_control"] - sp.exp(kap * v)) == 0)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
