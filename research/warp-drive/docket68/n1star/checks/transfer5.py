#!/usr/bin/env python3
"""transfer5: Lemma 6.5''s transfer F(0) -> F(1) at the record's damping gamma_C = 10^6 (BEYOND5 Q4, D433).

coulombL5.py Q4 computed the transfer of the l = 0 self-similar system (h = r^-2 F(s), s = v/r, F = (a, b, c, d))
from N (s = 0) to I_0 (s = 1) at gamma_C = 1 only. Here, at the record's point otherwise (coulombL5.POINT:
e_U = gam_U = 1/100, e_C = 1/102400, v = 1/2):

  T1 for gamma_C = 1, 10^2, 10^4, 10^5 and 10^6: the regular Frobenius series at s = 0 summed at s = 1 with 400 and
     600 terms (radius 2: the only other singular point is s = 2) agree; up to 10^4 a stiff integrator (Radau,
     from s = 10^-3 started by the series) agrees with them too (at 10^6 it did not finish in 25 minutes). The
     exponents at N besides 0 scale with gamma_C and are negative, so the stiff modes are the singular ones at N,
     absent from the regular branch, and the transfer stays well conditioned.
  T2 the limit gamma_C -> infinity: the successive differences T(10^4) - T(10^2), T(10^5) - T(10^4) and
     T(10^6) - T(10^5).
  T3 against the undamped transfer (gamma_U = gamma_C = 0), Lemma 6.5's: in the basis a, b, c - d, (c + 3d)/4 it is
     diag(1, 0, -1/3, 1) (coulombL5 Q3).

Computed (series at 30 digits; Radau in floating point, rtol 1e-11), not certified.
"""
import sys

import mpmath as mp
import numpy as np
import sympy as sp

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import coulombL5 as C  # noqa: E402

BASIS = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, -1], [0, 0, sp.Rational(1, 4), sp.Rational(3, 4)]], dtype=float)


def in_basis(T):
    """the transfer in the basis a, b, c - d, (c + 3d)/4: B T B^-1"""
    return BASIS @ T @ np.linalg.inv(BASIS)


def main():
    ok = {}
    eqs = C.reduce()
    M, rest = C.matrices(eqs[:4])
    assert all(r_ == 0 for r_ in rest)
    res = {}
    for gc in (1, 10**2, 10**4, 10**5, 10**6):
        sub = dict(C.POINT)
        sub[C.gC] = gc
        T4, last4 = C.series_transfer(M, sub, nterms=400, dps=30)
        T8, last8 = C.series_transfer(M, sub, nterms=600, dps=30)
        To = C.ode_transfer(M, sub) if gc <= 10**4 else None
        A4 = np.array([[float(T4[i, j]) for j in range(4)] for i in range(4)])
        A8 = np.array([[float(T8[i, j]) for j in range(4)] for i in range(4)])
        d48 = float(max(abs(T4[i, j] - T8[i, j]) for i in range(4) for j in range(4)))
        dso = float(np.max(np.abs(A8 - To))) if To is not None else float("nan")
        m10 = np.array(sp.Matrix(M[1].subs(C.S, 0).subs(sub)).evalf(), dtype=float)
        expo = sorted((1 - np.linalg.eigvals(m10)).real)
        res[gc] = (A8, d48, dso, float(last8), expo)
        print("  T1: gamma_C = %g: series 400 vs 600 terms %.1e (last term %.1e); series vs Radau %.1e; exponents at N "
              "besides 0: %s" % (gc, d48, float(last8), dso, ", ".join("%.4g" % x for x in expo)), flush=True)
    ok["T1"] = all(v[1] < 1e-12 for v in res.values()) and all(res[g][2] < 1e-6 for g in (1, 10**2, 10**4))
    print("  T1: transfer at gamma_C = 10^6, rows a, b, c, d, columns F(0) = e_a ... e_d:")
    for i in range(4):
        print("      " + "  ".join("%+.8f" % res[10**6][0][i, j] for j in range(4)))
    print("      in the basis a, b, c - d, (c + 3d)/4:")
    Bm = in_basis(res[10**6][0])
    for i in range(4):
        print("      " + "  ".join("%+.8f" % Bm[i, j] for j in range(4)))
    d1 = float(np.max(np.abs(res[10**4][0] - res[10**2][0])))
    d2 = float(np.max(np.abs(res[10**5][0] - res[10**4][0])))
    d3 = float(np.max(np.abs(res[10**6][0] - res[10**5][0])))
    print("  T2: max |T(10^4) - T(10^2)| = %.3e, |T(10^5) - T(10^4)| = %.3e, |T(10^6) - T(10^5)| = %.3e" % (d1, d2, d3))
    ok["T2"] = d3 < d2 < d1
    sub0 = dict(C.POINT)
    sub0[C.gC] = 0
    sub0[C.gU] = 0
    T0, _ = C.series_transfer(M, sub0, nterms=400)
    A0 = np.array([[float(T0[i, j]) for j in range(4)] for i in range(4)])
    B0 = in_basis(A0)
    q3 = np.max(np.abs(B0 - np.diag([1, 0, -1/3, 1]))) < 1e-12
    dev = float(np.max(np.abs(Bm - B0)))
    print("  T3: undamped, in that basis diag(1, 0, -1/3, 1): %s; the record's point departs from it by up to %.4f"
          % (q3, dev))
    ok["T3"] = q3 and dev > 1e-3
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
