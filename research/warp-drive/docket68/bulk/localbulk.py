#!/usr/bin/env python3
"""localbulk.py -- wall C, first theorem-level piece: a five-dimensional vacuum bulk in which the corridor is an exact
Randall-Sundrum plane with no matter on it is shown to EXIST near the plane, unique among analytic solutions up to
diffeomorphism.

First written saying the bulk "exists near the plane, and is unique there", that "Dahia-Romero give the same", with a
reach of order r0 and one control that never tested the Gauss formula.  The verifier qualified uniqueness (analytic
only, up to diffeomorphism), required constraint propagation to be named, showed Dahia-Romero do NOT give the same (they
leave the extrinsic curvature, hence the plane's matter, uncontrolled), put the reach at ~min(r0, ell), and supplied the
genuine control (dS slicing of AdS5) now in L1c (LOCALBULK.md History).

The plane: a single vacuum Randall-Sundrum plane whose induced metric is the corridor, Bronnikov-Kim eq. (17) at
r0 = 2m.  Its identification with the face-to-face pair at SHORT range is the board's hypothesis H-ONE-PLANE-NEAR:
static.py S2b shows one RS II plane only at long range (zero modes).  Extrinsic curvature K_mu nu = -(1/ell) g_mu nu
(Maartens-Koyama eq. 68 with T = 0, mirror symmetry and the RS tension; READ in throatbulk.py).  Bulk: vacuum,
Lambda5 = -6/ell^2.

  L1  Gauss constraint: for a timelike surface in a bulk with R_AB = (2 Lambda5/3) g_AB, R(4) = 2 Lambda5 + K^2 - K.K.
      For K = c h: K^2 - K.K = 12 c^2.  With c = -1/ell the right side is 0 (STRUCTURAL), so the constraint is
      R(4) = 0, and eq. (17) has R(4) = 0 exactly (computed).
      L1b control: Schwarzschild-de Sitter (R = 12/L^2) fails it.
      L1c genuine control of the formula itself: the dS slicing of AdS5, dy^2 + ell^2 sinh^2(y/ell) dS4(unit), has
      c = a'/a = coth(y/ell)/ell and R(4) = 12/(ell^2 sinh^2) = 2 Lambda5 + 12 coth^2/ell^2; a wrong sign on the K
      terms fails it.
      L1d (STRUCTURAL) the check is blind to the sign of K (c = +1/ell passes too) and holds side by side for any ell:
      Z2 is not needed -- unequal sides k_L != k_R pass, each with K = -g/ell_side
  L2  Codazzi, D^mu K_mu nu - D_nu K = R_AB n^A e^B_nu = 0, holds identically for K = c g with c constant (STRUCTURAL;
      no check)
  L3  the data are analytic.  rho is stability.py's chart, d rho = sqrt(F/H) dr; with r = 2m + u^2 the closed form is
      d rho/du = 2 sqrt(m/2 + u^2) (computed exactly), so rho - rho_H is odd in u and r(rho) even, minimum at the
      horizon: continuation through it leads into a SECOND r > 2m exterior, not into r < 2m.  The u-series converges
      for |u| < sqrt(m/2) (branch point u^2 = -m/2, i.e. r = 3m/2).  The strip 3m/2 < r < 2m is Riemannian (all four
      metric entries positive) and is not in the Lorentzian domain.  For r > 2m the data are rational in r or the root
      of a positive analytic function, so H-ANALYTIC-DATA is established, not assumed
  L4  (g, K) is analytic Cauchy data on a non-characteristic (timelike) surface meeting both constraints.  In Gaussian
      normal gauge the Cauchy-Kovalevskaya theorem (standard, not READ) solves the mu-nu evolution equations; the yy and
      y-mu constraints then stay zero off the plane by the contracted Bianchi identities -- the constraint-propagation
      lemma of Campbell-Magaard with Lambda, as used by Dahia-Romero (READ in BULKWARP.md).  So a local vacuum bulk
      exists, unique among ANALYTIC solutions up to diffeomorphism; Maartens-Koyama's formal series eq. (148) is that
      solution's Taylor series, and converges near the plane.  By uniqueness the bulk inherits the data's staticity
      and spherical symmetry.  The board's addition over Dahia-Romero is K = -g/ell: the plane is vacuum with RS tension
  L5  how far: imported from throatbulk.py T6 (MK eq. 148 at the throat), g~_thth = 4m^2 + y^2 + 2y^3/ell, i.e. the
      corrections are (y/r0)^2 and (y/r0)^2 (2y/ell); with the warp e^{-2y/ell} and the uncomputed O(y^4) terms the
      reach is ~min(r0, ell) -- an estimate, not a bound, conditional on ell against r0 (throatbulk T4 puts them of one
      order; under H-ONE-BIT-SCALE r_min/ell = sqrt(N) and the reach is ~ell)
Imports throatbulk.py by path.  Stdlib + sympy.  python3 localbulk.py [--selftest]
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

t, r, th, ph, m, u, L, ell, y = sp.symbols("t r theta phi m u L ell y", positive=True)


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


def ricci_scalar(F, H):
    g = sp.diag(-F, 1 / H, r**2, r**2 * sp.sin(th)**2)
    X = [t, r, th, ph]
    gi = g.inv()
    n = 4
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = [sp.simplify(sum(sp.diff(Gam[a][b][b], X[a]) - sp.diff(Gam[a][b][a], X[b])
                           + sum(Gam[a][a][d] * Gam[d][b][b] - Gam[a][b][d] * Gam[d][b][a] for d in range(n))
                           for a in range(n))) for b in range(n)]
    return sp.simplify(sum(gi[i, i] * Ric[i] for i in range(n)))


def gauss_rhs(c, lam5, sign=1):
    """2 Lambda5 + sign (K^2 - K.K) for K_mu nu = c h_mu nu in four dimensions; sign = -1 is the deliberately wrong form."""
    K2 = (4 * c) ** 2
    KK = 4 * c**2
    return sp.simplify(2 * lam5 + sign * (K2 - KK))


def compute():
    lam5 = -6 / ell**2
    F = 1 - 2 * m / r
    H = (1 - 2 * m / r) ** 2 / (1 - sp.Rational(3, 2) * m / r)
    R_corr = ricci_scalar(F, H)
    Fs = 1 - 2 * m / r - r**2 / L**2
    R_sds = ricci_scalar(Fs, Fs)
    # L1c: dS slicing of AdS5; the slice is dS4 of radius a = ell sinh(y/ell), static patch F = H = 1 - r^2/a^2
    a = ell * sp.sinh(y / ell)
    c_ds = sp.simplify(sp.diff(a, y) / a)
    R_ds4 = sp.simplify(ricci_scalar(1 - r**2 / a**2, 1 - r**2 / a**2))
    ds_ok = sp.simplify((R_ds4 - gauss_rhs(c_ds, lam5)).rewrite(sp.exp)) == 0
    ds_wrong = sp.simplify((R_ds4 - gauss_rhs(c_ds, lam5, sign=-1)).rewrite(sp.exp)) == 0
    # L1d: sign blindness; and a side with its own ell
    ellL = sp.Symbol("ell_L", positive=True)
    side = gauss_rhs(-1 / ellL, -6 / ellL**2)
    # L3: the chart and the closed form
    drho_dr = sp.sqrt(F / H)
    g_u = sp.simplify((drho_dr * sp.diff(2 * m + u**2, u)).subs(r, 2 * m + u**2))
    closed = 2 * sp.sqrt(m / 2 + u**2)
    closed_ok = sp.simplify(g_u - closed) == 0
    even = sp.simplify(closed.subs(u, -u) - closed) == 0
    lead = closed.subs(u, 0)
    # the strip 3m/2 < r < 2m: signs of g_tt = -F and g_rr = 1/H at r = 7m/4
    strip = {"g_tt": sp.simplify((-F).subs(r, sp.Rational(7, 4) * m)), "g_rr": sp.simplify((1 / H).subs(r, sp.Rational(7, 4) * m))}
    # L5: imported from throatbulk.py T6
    tb = _load(os.path.join(HERE, "throatbulk.py"), "lb_throatbulk")
    gt0 = tb.t6()["g_tilde"]
    yt = [s for s in gt0.free_symbols if s.name == "y"][0]
    gt = sp.expand(gt0.subs({yt: y, tb.m: m, tb.ell: ell}))
    return {"gauss": gauss_rhs(-1 / ell, lam5), "gauss_plus": gauss_rhs(1 / ell, lam5), "gauss_side": side,
            "R_corr": R_corr, "R_sds": R_sds, "c_ds": c_ds, "R_ds4": R_ds4, "ds_ok": ds_ok, "ds_wrong": ds_wrong,
            "drho_du": g_u, "closed_ok": closed_ok, "even": even, "lead": lead, "strip": strip, "g_tilde": gt}


def report(d):
    print("localbulk.py -- wall C: a local vacuum-RS bulk carrying the corridor\n")
    print("L1  Gauss with K = -g/ell: R(4) must equal %s; eq. (17) has R(4) = %s" % (d["gauss"], d["R_corr"]))
    print("L1b control SdS: R(4) = %s, not 0" % d["R_sds"])
    print("L1c control, dS slicing of AdS5: c = %s, R(4) = %s; Gauss formula holds: %s; wrong-sign form holds: %s"
          % (d["c_ds"], d["R_ds4"], d["ds_ok"], d["ds_wrong"]))
    print("L1d sign-blind: c = +1/ell gives %s; a side with its own ell_L gives %s (Z2 not needed)"
          % (d["gauss_plus"], d["gauss_side"]))
    print("L2  Codazzi holds identically for K = c g, c constant (STRUCTURAL)")
    print("L3  d rho/du = %s (closed form 2 sqrt(m/2 + u^2): %s; even: %s; leading %s); strip 3m/2<r<2m at r = 7m/4: "
          "g_tt = %s, g_rr = %s (Riemannian)" % (d["drho_du"], d["closed_ok"], d["even"], d["lead"],
                                                 d["strip"]["g_tt"], d["strip"]["g_rr"]))
    print("L4  analytic data, both constraints, timelike surface, Bianchi propagation -> a local vacuum bulk, unique "
          "among analytic solutions up to diffeomorphism")
    print("L5  MK eq. 148 at the throat (throatbulk T6): g~_thth = %s -> reach ~min(r0, ell) (estimate)" % d["g_tilde"])


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("L1 (STRUCTURAL): with K = -g/ell the Gauss constraint demands R(4) = 0", d["gauss"] == 0)
    chk("L1: the corridor, eq. (17) at r0 = 2m, has R(4) = 0 -- the constraint holds", d["R_corr"] == 0)
    chk("L1b control: Schwarzschild-de Sitter (R = 12/L^2) fails the same constraint",
        sp.simplify(d["R_sds"] - 12 / L**2) == 0)
    chk("L1c control: the dS slicing of AdS5 satisfies the Gauss formula, and the wrong-sign form fails it",
        d["ds_ok"] and not d["ds_wrong"])
    chk("L1d (STRUCTURAL): sign-blind (c = +1/ell passes) and side by side for any ell (Z2 not needed)",
        d["gauss_plus"] == 0 and d["gauss_side"] == 0)
    chk("L3: d rho/du = 2 sqrt(m/2 + u^2) exactly -- even, analytic through the horizon, beginning sqrt(2m)",
        d["closed_ok"] and d["even"] and sp.simplify(d["lead"] - sp.sqrt(2 * m)) == 0)
    chk("L3: the strip 3m/2 < r < 2m is Riemannian (g_tt > 0 and g_rr > 0), not in the Lorentzian domain",
        d["strip"]["g_tt"].is_positive and d["strip"]["g_rr"].is_positive)
    gt = d["g_tilde"]
    chk("L5: MK eq. 148 at the throat gives corrections (y/r0)^2 and (y/r0)^2 (2y/ell), r0 = 2m",
        gt is not None and sp.simplify(gt - (4 * m**2 + y**2 + 2 * y**3 / ell)) == 0)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
