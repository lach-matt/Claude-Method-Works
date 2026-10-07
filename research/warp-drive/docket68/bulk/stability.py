#!/usr/bin/env python3
"""stability.py -- wall E (stability), worked as mathematics (M-RULINGS item 149: "work the math now").

The corridor: Bronnikov-Kim eq. (17) at r0 = 2m (plane.py), -F dt^2 + dr^2/H + r^2 dOmega^2, F = 1 - 2m/r,
H = (1 - 2m/r)^2 / (1 - 3m/2r).  M (items 86, 136 E): the hold is "instantaneous or near instantaneous".

READ: Aretakis, "Horizon instability of extremal black holes", arXiv:1206.6598v2:
  abstract: "translation invariant derivatives of generic solutions to the wave equation do not decay along such
      horizons as advanced time tends to infinity, and in fact, higher order derivatives blow up"
  eq. (6)-(8) p.10: in spherical symmetry g = -D(r) dv^2 + 2 dv dr + K^-1 g_S2, extremality D(r_H) = D'(r_H) = 0
  Prop. 3.2 p.10: the full hierarchy of conservation laws (every l) holds provided eq. (10), D''(r_H) = 2 K(r_H);
      "extremal Reissner-Nordstrom satisfies the condition (10)" (p.11)
  Theorem 3 p.15: "sup |Y^k psi| >= c |H0[psi]| tau^(k-1), asympotically along H+ for all k >= 2"

  S1  the corridor's horizon is extremal: written as -D dv^2 + 2 dv d(rho) + r^2 dOmega^2 (d rho = sqrt(F/H) dr), D has a
      double zero at the horizon, D'(rho_H) = 0 (surface gravity zero).  Control: a horizon member of eq. (17) off the
      corridor (r0 = 1.8m, plane.py's window) has D'(rho_H) != 0
  S2  it meets Aretakis's condition (10) exactly: D''(rho_H) = 1/(2m^2) = 2K, K = 1/r_H^2 -- so his whole hierarchy of
      conservation laws applies: the instability is the corridor's, as for extremal Reissner-Nordstrom.  Control
      (READ): extremal RN, D = (1 - M/r)^2, meets (10)
  S3  but it is asymptotic in advanced time, in units of the horizon scale m: the growth of the k-th derivative after a
      time T is of order (cT/m)^(k-1) (Theorem 3's power, its constant unknown).  The corridor's own clock m/c =
      r_min(N)/(2c) is 6.6e-37 s at the example README, growing as sqrt(N).  A hold no longer than that clock leaves the
      growth of order one: the instability cannot act within M's near-instantaneous hold
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
    return {"D1": d1, "D2": d2, "K": K, "cond10": sp.simplify(d2 - 2 * K) == 0, "control_D1": c1, "rn_ok": rn_ok,
            "rN": rN, "t_m": t_m, "t_m_per_sqrt_bit": r1 / (2 * C)}


def report(d):
    print("stability.py -- wall E, the corridor's horizon (item 149)\n")
    print("S1 corridor: D'(rho_H) = %s (extremal); control r0 = 1.8m: D'(rho_H) = %s" % (d["D1"], d["control_D1"]))
    print("S2 D''(rho_H) = %s, 2K = %s: Aretakis's condition (10) holds: %s; extremal RN meets it: %s"
          % (d["D2"], 2 * d["K"], d["cond10"], d["rn_ok"]))
    print("S3 the corridor's clock m/c = %.3e s at the example README (r_min = %.3e m); %.3e s x sqrt(N)"
          % (d["t_m"], d["rN"], d["t_m_per_sqrt_bit"]))
    for T in (1.0, 10.0, 1e3):
        print("   a hold of %g clock(s): growth of the 2nd derivative ~ %g, of the 3rd ~ %g (order, constant unknown)"
              % (T, T, T**2))


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
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
