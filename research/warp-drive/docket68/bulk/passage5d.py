#!/usr/bin/env python3
"""passage5d.py -- wall D, the theorem the record said would have to be proved: what the bulk makes of the passage
between the plane's two asymptotic regions.

DOORS.md OPEN 1: "A censorship theorem for passage between asymptotic regions of a plane in a bulk.  None was READ, so it
would have to be proved."  This proves what the corridor's own geometry decides, and names exactly what it leaves.

The setting: the corridor, Bronnikov-Kim eq. (17) at r0 = 2m, on a Randall-Sundrum plane (K = c g, c constant, either
sign) in a vacuum bulk with Lambda5 (localbulk.py: such a bulk exists near the plane; bulkseries.py computes it).  The
passage is the radial null geodesic of the plane from end 1 through the throat to end 2: in stability.py's chart
-D dv^2 + 2 dv drho + r^2 dOmega^2 it is v = const, affine parameter lambda = -rho, complete; with r = 2m + u^2,
d rho/du = 2 sqrt(m/2 + u^2) (localbulk L3), u > 0 is side 1 and u < 0 side 2.

THEOREM D.  Along the passage gamma:
  P1  gamma is a null geodesic of the bulk: its acceleration off the plane is K(k, k) = c g(k, k) = 0 (STRUCTURAL; UMBILIC
      U1)
  P2  the bulk's null energy along gamma is zero, and its tidal term toward the bulk is exactly the plane's deficit:
          R5(n,k,n,k) = -R4(k,k) = 2 r''/r = (m/2) / ((r - 3m/2)^2 r)  > 0.
      Proof: R5(k,k) = sum over the transverse frame of R5(e,k,e,k) = 0 in a vacuum-Lambda bulk (g(k,k) = 0); Gauss
      gives R5(e,k,e,k) = R4(e,k,e,k) for e tangent, because the K-terms are c^2 (g(e,e) g(k,k) - g(e,k)^2) = 0; and
      R4(k,k) = -2 r''/r for this congruence (Raychaudhuri, no shear).  Computed from the bulk series (bulkseries.py)
      rather than assumed.  Control: the black string reads 0 and 0.  Foil: a non-umbilic first order breaks the
      identity.  So the 5D generic condition holds along the whole passage (censor.py C3 left it "plausible")
  P3  integrated, Q = integral of R5(n,k,n,k) d lambda = 8/(3m) - (4/(3 sqrt3 m)) artanh(sqrt3/2) = 1.652872/m, exactly
      minus the plane's averaged null energy along both legs (coin.py's closed form, imported)
  P4  LEMMA (Sturm; proved here).  If q >= 0 is integrable on the whole line and its integral is positive, then
      J'' + q J = 0 has a solution with two zeros.  Proof: the quadratic form I[f] = integral (f'^2 - q f^2) is negative
      for f = 1 on [-L, L], falling linearly to 0 over a length L^2 beyond: I = 2/L^2 - integral q f^2 -> -Q < 0.  A
      negative form on an interval [a, b] with f(a) = f(b) = 0 means a conjugate pair inside (Jacobi).  The witness is
      computed for the corridor's q
  P5  the conjugate points, computed: a point p of the passage on side 1 has a conjugate point in the bulk direction iff
      it lies beyond r_* = 2.21007m (0.69107m of affine parameter before the throat).  Its conjugate point lies on side 2
      and tends to r_* on side 2 as p recedes to end 1's infinity.  Two routes give r_*: the limit from end 1, and the
      zero of end 2's asymptotically constant solution.  Points nearer than r_* on side 1, and all of side 2, have none
  P6  so gamma is not achronal in the bulk (Hawking-Ellis Prop. 4.5.12, standard, not READ: beyond a conjugate point a
      null geodesic is joined to its start by a timelike curve, inside any neighbourhood of the segment).  The Jacobi
      field's normal part is positive between the pair, so that curve runs on the bulk side, within the local bulk.
      Every point of end 1 beyond r_* is joined by a TIMELIKE curve through the bulk to points of end 2: the bulk is a
      faster route between the plane's two ends than the passage itself
COROLLARY (censorship).  In five dimensions the plane's two ends are chronologically connected through the bulk.  The
  composite plane's null energy holds (DOORS K1, positive tension, H-COMPOSITE-SURFACE) and the generic condition holds
  along the passage (P2).  So a five-dimensional topological censorship theorem, if one holds for a bulk bounded by a
  plane (none is READ or proved here), can be met by the corridor only through its remaining premises: global
  hyperbolicity of the five-dimensional spacetime, and the plane's two ends being distinct ends of it.  Those are wall
  C's global questions (GLOBALBULK.md)
Imports bulkseries.py and copy/coin.py by path.  Stdlib + sympy.  python3 passage5d.py [--selftest]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
M = 1.0                                                             # units m = 1


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


def tidal(first=None, schwarzschild=False):
    """R5(n,k,n,k) from the bulk series at y = 0, against -R4(k,k), for the radial null vector k^t = 1/F, k^r = sqrt(H/F)
    (Killing energy 1).  Gaussian normal: R5_{y mu y nu} = -(1/2) d_y^2 h + (1/4) h^-1 (d_y h)^2."""
    bs = _load(os.path.join(HERE, "bulkseries.py"), "p5_bulkseries")
    r = bs.r
    F = 1 - 2 / r
    H = F if schwarzschild else F**2 / (1 - sp.Rational(3, 2) / r)
    co = bs.solve(F, H, 2, first=first)
    a0, a1, a2 = co["A"][:3]
    b0, b1, b2 = co["B"][:3]
    R_yt = a2 - a1**2 / (4 * a0)                                    # h_tt = -A
    R_yr = -b2 + b1**2 / (4 * b0)
    n_kk = sp.simplify(R_yt / F**2 + R_yr * H / F)
    Ric = bs.ricci(bs.Series([F], 0), bs.Series([1 / H], 0), bs.Series([r**2], 0))
    R4_kk = sp.simplify(Ric["A"].c[0] / F**2 + Ric["B"].c[0] * H / F)
    s = sp.sqrt(H / F)                                              # dr/d rho
    rpp = sp.simplify(s * sp.diff(s, r))                            # r''
    return {"n_kk": n_kk, "R4_kk": R4_kk, "rpp": rpp, "r": r}


def q_of_u(u):
    """R5(n,k,n,k) along the passage, as a function of u (r = 2m + u^2): 2 r''/r with r'' = (m/4)/(m/2 + u^2)^2."""
    return (M / 2) / ((M / 2 + u * u) ** 2 * (2 * M + u * u))


def rho_u(u):
    return 2 * math.sqrt(M / 2 + u * u)


def rho_of(u):
    a = M / 2
    return u * math.sqrt(a + u * u) + a * math.asinh(u / math.sqrt(a))


def _rk4(u, J, P, h):
    def f(uu, JJ, PP):                                              # lambda = -rho; d/du of (J, dJ/dlambda)
        return -rho_u(uu) * PP, rho_u(uu) * q_of_u(uu) * JJ
    k1 = f(u, J, P)
    k2 = f(u + h / 2, J + h / 2 * k1[0], P + h / 2 * k1[1])
    k3 = f(u + h / 2, J + h / 2 * k2[0], P + h / 2 * k2[1])
    k4 = f(u + h, J + h * k3[0], P + h * k3[1])
    return J + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), P + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])


def conjugate(up, h=1e-3, umin=-3e3):
    """First zero (in u) of the Jacobi field J(up) = 0, dJ/dlambda = 1, followed toward end 2; None if it has none."""
    u, J, P = up, 0.0, 1.0
    while u > umin:
        hh = -h * max(1.0, abs(u) / 5)
        Jn, Pn = _rk4(u, J, P, hh)
        if Jn < 0:
            return u + hh * J / (J - Jn)
        u, J, P = u + hh, Jn, Pn
    return None


def threshold(h=2e-4, U=3e3):
    """The zero of the solution with J -> 1, J' -> 0 at end 2, followed back toward end 1."""
    u, J, P = -U, 1.0, 0.0
    while u < 5:
        hh = h * max(1.0, abs(u) / 5)
        Jn, Pn = _rk4(u, J, P, hh)
        if Jn < 0:
            return u + hh * J / (J - Jn)
        u, J, P = u + hh, Jn, Pn
    return None


def quadratic_form(L=6.0, n=20000):
    """I[f] for f = 1 on |lambda| <= L, linear to 0 over L^2 beyond, along the passage (lambda = -rho)."""
    def u_at(lam):                                                  # invert rho(u) = -lam by bisection
        lo, hi = -1e4, 1e4
        for _ in range(80):
            mid = (lo + hi) / 2
            if rho_of(mid) > -lam:
                hi = mid
            else:
                lo = mid
        return (lo + hi) / 2
    a, b = -(L + L * L), L + L * L
    I, dl = 0.0, (b - a) / n
    for i in range(n):
        lam = a + (i + 0.5) * dl
        d = abs(lam) - L
        f, fp = (1.0, 0.0) if d <= 0 else (1 - d / (L * L), -1 / (L * L))
        I += (fp * fp - q_of_u(u_at(lam)) * f * f) * dl
    return I


def compute():
    corr, bh = tidal(), tidal(schwarzschild=True)
    bs = _load(os.path.join(HERE, "bulkseries.py"), "p5_bulkseries_f")
    r, ell, delta = bs.r, bs.ell, sp.Symbol("delta", positive=True)
    F = 1 - 2 / r
    foil = tidal(first={"A": -2 * (1 + delta) * F / ell})
    coin = _load(os.path.join(D68, "copy", "coin.py"), "p5_coin")
    Q_closed = sp.Rational(8, 3) - 4 / (3 * sp.sqrt(3)) * sp.atanh(sp.sqrt(3) / 2)
    uq = sp.Symbol("u", real=True)
    Q_int = sp.Integral(2 * sp.sqrt(sp.Rational(1, 2) + uq**2) * sp.Rational(1, 2)
                        / ((sp.Rational(1, 2) + uq**2) ** 2 * (2 + uq**2)), (uq, -sp.oo, sp.oo))
    u_lim = conjugate(300.0)
    u_thr = threshold()
    return {"corr": corr, "bh": bh, "foil": foil, "Q_closed": float(Q_closed), "Q_int": float(Q_int.evalf(20)),
            "anec_leg": coin.anec_closed(1, 2), "form": quadratic_form(),
            "u_lim": u_lim, "u_thr": u_thr, "r_star": 2 * M + u_thr * u_thr, "affine_star": rho_of(u_thr),
            "conj_table": {up: conjugate(up) for up in (0.5, 1.0, 5.0, 30.0)},
            "none_at": {up: conjugate(up) for up in (0.3, 0.0, -0.5)}}


def report(d):
    c = d["corr"]
    print("passage5d.py -- wall D: Theorem D, the passage in the bulk (m = 1)\n")
    print("P1 the passage is a bulk null geodesic: K(k,k) = c g(k,k) = 0 (STRUCTURAL)")
    print("P2 from the bulk series: R5(n,k,n,k) = %s; -R4(k,k) = %s; 2r''/r = %s; black string: %s, %s; non-umbilic foil "
          "residual: %s" % (c["n_kk"], sp.simplify(-c["R4_kk"]), sp.simplify(2 * c["rpp"] / c["r"]),
                            d["bh"]["n_kk"], d["bh"]["R4_kk"], sp.simplify(d["foil"]["n_kk"] + d["foil"]["R4_kk"])))
    print("P3 Q = %.6f (closed form %.6f); minus the plane's ANEC over both legs (coin.py): %.6f"
          % (d["Q_int"], d["Q_closed"], -2 * d["anec_leg"]))
    print("P4 Sturm witness: I[f] = %.4f < 0" % d["form"])
    print("P5 r_* = %.5f (affine %.5f before the throat); limit of the conjugate point from end 1: u = %.5f; threshold "
          "from end 2: u = %.5f" % (d["r_star"], d["affine_star"], d["u_lim"], d["u_thr"]))
    for up, uc in d["conj_table"].items():
        print("   p at r = %.3f on side 1 -> conjugate at r = %.3f on side 2" % (2 + up * up, 2 + uc * uc))
    print("   no conjugate point from u = %s" % ", ".join("%.1f" % k for k, v in d["none_at"].items() if v is None))
    print("P6 so timelike curves through the bulk join end 1 (beyond r_*) to end 2 (Hawking-Ellis 4.5.12)")


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    c, r = d["corr"], d["corr"]["r"]
    chk("P2: from the bulk series, R5(n,k,n,k) = -R4(k,k) = 2r''/r = (1/2)/((r - 3/2)^2 r) exactly, positive",
        sp.simplify(c["n_kk"] + c["R4_kk"]) == 0 and sp.simplify(c["n_kk"] - 2 * c["rpp"] / r) == 0
        and sp.simplify(c["n_kk"] - sp.Rational(1, 2) / ((r - sp.Rational(3, 2)) ** 2 * r)) == 0)
    chk("P2 control: the black string reads 0 for both", d["bh"]["n_kk"] == 0 and d["bh"]["R4_kk"] == 0)
    chk("P2 foil: a non-umbilic first order breaks the identity",
        sp.simplify(d["foil"]["n_kk"] + d["foil"]["R4_kk"]) != 0)
    chk("P3: Q = 8/3 - (4/(3 sqrt3)) artanh(sqrt3/2) = 1.652872, minus the plane's ANEC on both legs (coin.py)",
        abs(d["Q_int"] - d["Q_closed"]) < 1e-12 and abs(d["Q_closed"] + 2 * d["anec_leg"]) < 1e-12)
    chk("P4: the Sturm witness is negative for the corridor's q", d["form"] < 0)
    chk("P5: the limit from end 1 and the threshold from end 2 agree, r_* = 2.2101 m on either side of the throat",
        abs(d["u_lim"] + d["u_thr"]) < 1e-4 and abs(d["r_star"] - 2.2101) < 1e-3)
    chk("P5: points beyond r_* on side 1 have conjugate points on side 2; the throat and side 2 have none",
        all(v is not None and v < 0 for v in d["conj_table"].values())
        and all(v is None for v in d["none_at"].values()))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
