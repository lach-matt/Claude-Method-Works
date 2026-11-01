#!/usr/bin/env python3
"""uniform3_5.py -- BEYOND5 3(b) (D492): Lemma 6.5''' at degree -3, so the strip's rho^3 coefficient (D487, D491) is
bounded uniformly in l.

checks/uniform5.py (D437) proves for the degree -2 reduction of the record's full flat operator that |F(s)| <= K0 |F(0)|
on [0, s1], uniformly in l >= 2, in the basis normalised by each harmonic's size (W = diag(1, 1, 1, 1, x, x, x^2) on the
scalar type, diag(1, 1, x) on the vector type, x = kappa^(1/2)), from: U1 the second-order part m2 I, M0 = x^2 I/2 +
O(x), M1 = O(1) in x; U2 A(0) = M1(0) - I/2 independent of x with positive eigenvalues; U3 a Lyapunov metric H for A(0);
U4-U5 explicit constants. At degree -3 (checks/stripfull5.py's reduction) M1 gains (1 - s) I (verifier 208, D491) and
M0 terms of x-degree 0 only, so the same steps can be run on the degree -3 matrices, and are, here:

  V1-V5 uniform5's U1-U5 at degree -3 (its functions, on stripfull5's matrices): the structure; A_3(0), independent of x,
        with A_3(0) = A_2(0) + I exactly; its eigenvalues at the record's point; the Lyapunov metric; the constants and
        K0_3, so |F(1)| <= K0_3 |F(0)| for every l >= 2.
  V6    jump: J := M1_3(0) - I = M1_2(0) in the normalised basis, exactly, so J is independent of x; |J^-1|_2 at the
        record's point (from J's least singular value at 50 digits, rounded up). Hence |K|_2 <= K0_3 |J^-1|_2 for every l
        >= 2, K = T_3 J^-1 the strip's rho^3 coefficient in the normalised basis: bounded uniformly in l. (K4 = -(1/2)
        T_3' J^-1 is bounded by the derivative estimate, |F_s(1)| <= 2^(1/2) K0_3 (x^2/2 + 1)^(1/2) |F(0)|: at most
        linear in l, not uniform.)
  V7    (computed) stripfull5's K at l = 2 ... 6, normalised, lies below K0_3 |J^-1|: a consistency check, which at
        a bound of e^(6e13) cannot fail (verifier 212, D500).
  Control: with A_3(0) -> -A_3(0) no positive Lyapunov solution (as uniform5's).

Measured (D492): every check passes (V4-V5 judged since D500: every constant finite and positive; before, they
were printed only). A_3(0)'s eigenvalues 2, 2.0099, 2.01, 2.02, 1.5e6, 1.5e6, 3e6 (scalar) and 2, 2.01,
1.5e6 (vector); lambda(H) in [1.62e-7, 0.565] and [3.33e-7, 0.276]; C_E = 5.39e13 and 5.28e12; ln K0_3 = 5.99e13 and
5.87e12; |J^-1|_2 <= 0.993 and 0.698; stripfull5's K at l = 2 ... 6 in this basis 2.21 to 2.39 (scalar) and 0.342 to
1.008 (vector).

Labels: V1-V5 exact (constants outward rounded, as uniform5's), V6 exact but for |J^-1|_2 (50 digits), V7 computed.
Only uniform5's s1 = 1 case is run at degree -3; its s1 = 3/2 case and the derivative induction K_k are not, so K and
K4, which need F(1) and F_s(1) only, are covered, and the rho^5 and later width coefficients are not (D500). For s
<= 1 uniform5's derivative induction needs only s1 = 1, so they are bounded by polynomials in l (D508, deduced). J's
eigenvalues, 1.5, 1.5099, 1.51, 1.52 and the damping's, do not depend on x, so M1_3(0) = J + I has every real part > 1
at every l >= 2. 'Normalised' here is uniform5's W; harmonics5.weights, which stripfull5 uses, differs from it by
factors in [0.645, 1.732] (scalar) and [1.118, 1.414] (vector) at every l, so the uniformity holds in either (D500).
Uniform, not sharp: K0 is astronomical.
"""
import sys
import time

import mpmath as mp
import numpy as np
import sympy as sp

_argv, sys.argv = sys.argv, sys.argv[:1]
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import uniform5 as U  # noqa: E402
import stripfull5 as SF  # noqa: E402
import harmonics5 as H5  # noqa: E402
import coulombL5 as C  # noqa: E402
sys.argv = _argv

S, x, kap, lam = U.S, U.x, U.kap, U.lam


def main():
    t0 = time.time()
    ok = {}
    red = {}
    for p in (2, 3):
        es, oks = SF.reduce_scalar_p(p)
        ev_, okv = SF.reduce_vector_p(p)
        red[p] = (H5.matrices_n(es, H5.FS)[0], H5.matrices_n(ev_, H5.FV)[0])
        assert oks and okv
    print("    reductions done (%.0f s)" % (time.time() - t0), flush=True)
    for k, (typ, sub, W) in enumerate((("scalar", {kap: x**2}, [1, 1, 1, 1, x, x, x**2]),
                                       ("vector", {lam: x**2 - 1}, [1, 1, x]))):
        M3, M2_ = red[3][k], red[2][k]
        n = M3[0].shape[0]
        Mt = U.normalised(M3, sub, W)
        Mt2 = U.normalised(M2_, sub, W)
        m2 = S - S**2/2
        v1 = sp.expand(Mt[0] - m2*sp.eye(n)) == sp.zeros(n)
        lc = [sp.limit(Mt[2][i, j]/x**2, x, sp.oo) for i in range(n) for j in range(n)]
        v1 = v1 and all(lc[i*n + j] == (sp.Rational(1, 2) if i == j else 0) for i in range(n) for j in range(n))
        try:
            for i in range(n):
                for j in range(n):
                    assert all(b <= 0 for (a, b) in U.laurent(Mt[1][i, j]))
                    assert all(b <= 1 for (a, b) in U.laurent(Mt[2][i, j] - (x**2/2 if i == j else 0)))
        except AssertionError:
            v1 = False
        A3 = sp.Matrix(n, n, lambda i, j: sp.expand(Mt[1][i, j].subs(S, 0))) - sp.eye(n)/2
        A2 = sp.Matrix(n, n, lambda i, j: sp.expand(Mt2[1][i, j].subs(S, 0))) - sp.eye(n)/2
        v2a = not any(x in A3[i, j].free_symbols for i in range(n) for j in range(n))
        shift = sp.expand(A3 - A2 - sp.eye(n)) == sp.zeros(n)
        A0p = sp.Matrix(n, n, lambda i, j: sp.nsimplify(A3[i, j].subs(C.POINT), rational=True))
        lam_ = sp.Symbol("l")
        ivs = sp.Poly(A0p.charpoly(lam_).as_expr(), lam_).intervals(eps=sp.Rational(1, 10**6))
        nreal = sum(m_ for (a_, b_), m_ in ivs)
        ev = sorted(float((a_ + b_)/2) for (a_, b_), m_ in ivs for _ in range(m_))
        v2 = v2a and shift and nreal == n and all(a_ > 0 for (a_, b_), m_ in ivs)
        Hm = U.lyapunov(A0p)
        v3 = all(Hm[:q, :q].det() > 0 for q in range(1, n + 1))
        mu, hmax = U.eig_bounds(Hm)
        ctl = not all(U.lyapunov(-A0p)[:q, :q].det() > 0 for q in range(1, n + 1))
        Mtp = [m_.subs(C.POINT) for m_ in Mt]
        mp.mp.dps = 30
        a1, n0, n1 = U.bounds(Mtp, n, sp.Integer(1))
        ts = sp.sqrt(sp.Integer(1)/(1 - sp.Rational(1, 2)))
        CE = hmax/mu*(2*ts*a1 + n0 + 1 + sp.sqrt(2)*n1)
        Ts1 = sp.sqrt(2)*(sp.asin(0) + sp.pi/2)
        lnK0 = mp.mpf(sp.N(sp.log(hmax/mu)/2 + CE*Ts1/2, 30))
        # V6: the jump J = M1_3(0) - I = M1_2(0), normalised
        J3 = sp.Matrix(n, n, lambda i, j: sp.expand(Mt[1][i, j].subs(S, 0))) - sp.eye(n)
        J2 = sp.Matrix(n, n, lambda i, j: sp.expand(Mt2[1][i, j].subs(S, 0)))
        v6a = sp.expand(J3 - J2) == sp.zeros(n) and \
            not any(x in J3[i, j].free_symbols for i in range(n) for j in range(n))
        Jp = sp.Matrix(n, n, lambda i, j: sp.nsimplify(J3[i, j].subs(C.POINT), rational=True))
        free = set().union(*[Jp[i, j].free_symbols for i in range(n) for j in range(n)])
        v6a = v6a and not free
        mp.mp.dps = 50                                                  # |J^-1|_2 = 1/sigma_min(J), at 50 digits
        Jm = mp.matrix([[mp.mpf(sp.Rational(Jp[i, j]).p)/sp.Rational(Jp[i, j]).q for j in range(n)] for i in range(n)])
        smin = min(mp.svd_r(Jm, compute_uv=False))
        jnorm = float(1/smin)*(1 + 1e-10)
        mp.mp.dps = 30
        lnKb = lnK0 + mp.log(jnorm)
        ok["V1 " + typ], ok["V2 " + typ], ok["V3 " + typ], ok["control " + typ] = v1, v2, v3 and mu > 0, ctl
        ok["V6 " + typ] = v6a
        print("  V1 %s (degree -3): second-order part m2 I, M0 = x^2 I/2 + O(x), M1 = O(1): %s" % (typ, v1))
        print("  V2 %s: A_3(0) independent of x: %s; A_3(0) = A_2(0) + I exactly: %s; eigenvalues at the record's point: "
              "%s" % (typ, v2a, shift, ", ".join("%.6g" % e for e in ev)))
        print("  V3 %s: H A_3(0) + A_3(0)^T H = I, H > 0: %s; lambda(H) in [%.4g, %.4g]; control (-A_3(0)) not "
              "positive: %s" % (typ, v3, float(mu), float(hmax), ctl))
        print("  V4-V5 %s, s in [0, 1]: a1 = %.6g, n0 = %.6g, n1 = %.6g; C_E = %.6g, ln K0_3 = %s"
              % (typ, float(a1), float(n0), float(n1), float(CE), mp.nstr(lnK0, 8)))
        ok["V4-V5 " + typ] = all(0 < float(q) < float("inf") for q in (a1, n0, n1, CE, lnK0))
        print("  V6 %s: J = M1_3(0) - I = M1_2(0), independent of x: %s; |J^-1|_2 <= %.6g; so ln |K|_2 <= %s for every "
              "l >= 2" % (typ, v6a, jnorm, mp.nstr(lnKb, 8)), flush=True)
        # V7: consistency with stripfull5's K, l = 2 ... 6
        good = True
        for l in range(2, 7):
            par = {kap: l*(l + 2)} if typ == "scalar" else {lam: l*(l + 2) - 1}
            Ml = [sp.Matrix(n, n, lambda i, j: M3[o][i, j].subs(par)) for o in range(3)]
            K, _, _, _ = SF.kmap(Ml, dict(C.POINT), 400)
            xv = (l*(l + 2))**0.5
            Wn = np.diag([1, 1, 1, 1, xv, xv, xv**2] if typ == "scalar" else [1, 1, xv])
            Kn = Wn @ np.array([[float(K[i, j]) for j in range(n)] for i in range(n)]) @ np.linalg.inv(Wn)
            nk = float(np.linalg.norm(Kn, 2))
            good &= np.log(nk) <= float(lnKb)
            print("    V7 %s l = %d: |K|_2 = %.5g (ln %.4g <= %s)" % (typ, l, nk, np.log(nk), mp.nstr(lnKb, 6)),
                  flush=True)
        ok["V7 " + typ] = good
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    print("  %s (%.0f s)" % ("all pass" if all(ok.values()) else "FAILED", time.time() - t0))
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
