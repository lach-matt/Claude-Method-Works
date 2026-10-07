#!/usr/bin/env python3
"""localbulk.py -- wall C, first theorem-level piece: a five-dimensional bulk carrying the corridor EXISTS near the
plane, and is unique there.

The plane: one Randall-Sundrum II plane with no matter on it (static.py S2b, the face-to-face composite), its induced
metric the corridor, Bronnikov-Kim eq. (17) at r0 = 2m.  On such a plane, with mirror symmetry, the extrinsic curvature
is K_mu nu = -(1/ell) g_mu nu (Maartens-Koyama eq. 68 with T = 0 and the Randall-Sundrum tension, READ in throatbulk.py).
The bulk: vacuum with Lambda5 = -6/ell^2.

  L1  the Gauss constraint.  For a timelike surface in a bulk with R_AB = (2 Lambda5/3) g_AB, R(4) = 2 Lambda5 + K^2 - K.K.
      With K = -g/ell: 2 Lambda5 + 16/ell^2 - 4/ell^2 = 0, so the constraint is R(4) = 0 -- and eq. (17) has R(4) = 0
      exactly (computed).  Control: a brane metric with R(4) != 0 (Schwarzschild-de Sitter, R = 12/L^2) fails it
  L2  the Codazzi constraint, D^mu K_mu nu - D_nu K = 0, holds identically for K proportional to g (STRUCTURAL)
  L3  the data are analytic: in horizon coordinates (u = sqrt(r - 2m)) d rho/du is a power series beginning sqrt(2m),
      so rho, r(rho) and D(rho) are analytic through the horizon (computed)
  L4  so (g, K) is analytic Cauchy data on a non-characteristic (timelike) surface satisfying both constraints; by the
      Cauchy-Kovalevskaya theorem (standard, not READ) the 5D Einstein-Lambda equations have a unique local analytic
      solution off the plane -- a local bulk exists, and with it the corridor is an exact vacuum Randall-Sundrum plane.
      Dahia-Romero (READ in BULKWARP.md) give the same for any analytic metric, without fixing K
  L5  how far the local solution is controlled: the first correction off the plane, -E y^2 (MK eq. 148), is at the
      throat y^2 against r0^2 = 4m^2, so the expansion is of order one by y ~ r0 (an estimate, not a bound)
Stdlib + sympy.  python3 localbulk.py [--selftest]
"""
import sys

import sympy as sp

t, r, th, ph, m, u, L, ell = sp.symbols("t r theta phi m u L ell", positive=True)


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


def gauss_rhs():
    lam5 = -6 / ell**2
    K2 = (4 * (-1 / ell)) ** 2                                       # (trace K)^2, K = -g/ell in 4D
    KK = 4 * (1 / ell) ** 2                                         # K_mu nu K^mu nu
    return sp.simplify(2 * lam5 + K2 - KK)


def compute():
    F = 1 - 2 * m / r
    H = (1 - 2 * m / r) ** 2 / (1 - sp.Rational(3, 2) * m / r)
    R_corr = ricci_scalar(F, H)
    Fs = 1 - 2 * m / r - r**2 / L**2
    R_sds = ricci_scalar(Fs, Fs)
    # L3: s = r - 2m = u^2; d rho/du = sqrt(F/H) * 2u
    s = sp.Symbol("s", positive=True)
    Fsr = s / (s + 2 * m)
    Hsr = s**2 / ((s + 2 * m) ** 2 * (1 - sp.Rational(3, 2) * m / (s + 2 * m)))
    g = sp.simplify(sp.sqrt(sp.simplify(Fsr / Hsr)).subs(s, u**2) * 2 * u)
    ser = sp.series(g, u, 0, 6).removeO()
    lead = sp.limit(g, u, 0)
    odd_free = all(sp.simplify(ser.coeff(u, k)) == 0 for k in (1, 3, 5))
    return {"gauss": gauss_rhs(), "R_corr": R_corr, "R_sds": R_sds, "drho_du_series": ser, "lead": lead,
            "even_series": odd_free}


def report(d):
    print("localbulk.py -- wall C: a local bulk carrying the corridor\n")
    print("L1 Gauss constraint with K = -g/ell: R(4) must equal %s; eq. (17) has R(4) = %s; control SdS: R(4) = %s"
          % (d["gauss"], d["R_corr"], d["R_sds"]))
    print("L2 Codazzi holds identically for K proportional to g")
    print("L3 d rho/du = %s + ...  (leading %s; analytic, even in u)" % (d["drho_du_series"], d["lead"]))
    print("L4 analytic data, both constraints, timelike surface -> a unique local analytic bulk (Cauchy-Kovalevskaya)")
    print("L5 the first correction off the plane is of order one by y ~ r0 (estimate)")


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
    chk("L1 control: Schwarzschild-de Sitter (R = 12/L^2) fails the same constraint",
        sp.simplify(d["R_sds"] - 12 / L**2) == 0)
    chk("L3: d rho/du is analytic through the horizon, beginning sqrt(2m), even in u",
        sp.simplify(d["lead"] - sp.sqrt(2 * m)) == 0 and d["even_series"])
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
