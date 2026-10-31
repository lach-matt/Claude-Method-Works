#!/usr/bin/env python3
"""uniform5: Lemma 6.5''', the transfer bounded uniformly in l, at the record's point (BEYOND5 Q8, D437).

For every scalar- and vector-type harmonic l >= 2 of the record's full flat operator (harmonics5.py), write
x := kappa^(1/2), kappa = l(l + 2), and the reduced system in the basis normalised by the harmonic's size,
W = diag(1, 1, 1, 1, x, x, x^2) (scalar: a, b, c, d, e, f, k) and diag(1, 1, x) (vector: p, q, k), as

    m2 F'' + M1 F' + M0 F = 0,    m2 = s - s^2/2,   F(0) given (the regular branch at N),

and in T := int_0^s (m2)^(-1/2) ds' (s = 1 - cos(T/2^(1/2)), N at T = 0, I_0 at T1 = pi/2^(1/2)):

    F_TT + T_s A(s) F_T + M0 F = 0,    A(s) := M1(s) - (1 - s) I/2,   T_s = m2^(-1/2).

Checked here (exact unless marked):
  U1 the second-order part is m2 I; the x^2 coefficient of M0 is 1/2 on the diagonal and absent off it; M0 - x^2 I/2
     has x-degree <= 1 and M1 x-degree <= 0 (entries Laurent polynomials in x and polynomials in s).
  U2 A(0) does not depend on x, and at the record's point its eigenvalues are positive (1, 1.0099, 1.01, 1.02,
     ~1.5e6 twice, 3e6 on the scalar type; 1, 1.01, ~1.5e6 on the vector type).
  U3 the Lyapunov metric: H solves H A(0) + A(0)^T H = I (exact rationals), and H > 0 (all leading minors positive);
     its extreme eigenvalues are isolated exactly.
  U4 explicit constants for s in [0, 1], x >= 8^(1/2) (l >= 2): a1 >= sup |A'(s)|, n0 + n1 x >= sup |M0 - x^2 I/2|,
     from the absolute values of the coefficients (outward rounded).
  U5 the energy E := <F_T, H F_T> + (x^2/2 + 1) <F, H F> obeys dE/dT <= C_E E with
     C_E = (|H|/mu) (2 (s1/(1 - s1/2))^(1/2) a1 + n0 + 1 + 2^(1/2) n1), mu = lambda_min(H) (BEYOND5 Q8). Not to be
     confused with n1star/uniform5.py (D124's instrument); run this one by its path, checks/uniform5.py;
     so |F(s)| <= K0 |F(0)| on [0, s1] and |F_T| <= K0 (x^2/2 + 1)^(1/2) |F(0)| there (F_s = m2^(-1/2) F_T),
     K0 = cond(H)^(1/2) exp(C_E T(s1)/2), uniformly in l >= 2; for s1 = 1 (I_0) and s1 = 3/2 (a neighbourhood).
     The derivatives F^(k) at any s in [1/2, s1] then follow from the equation by induction, |F^(k)| <= K_k
     (1 + x^2)^(k/2) |F(0)| (BEYOND5 Q8).
  U6 (computed, a consistency check) the transfers of harmonics5 for l = 2 ... 6, in this basis, lie below K0, and the
     energy ratio E(T1)/E(0) of each lies below exp(C_E T1).
  Control: with A(0) replaced by -A(0) (anti-damped at N), no positive H exists (the Lyapunov solution is not
     positive definite).
"""
import pickle
import sys

import mpmath as mp
import numpy as np
import sympy as sp

sys.path.insert(0, __file__.rsplit("/", 1)[0])
sys.path.insert(0, __file__.rsplit("/", 2)[0])
import coulombL5 as C  # noqa: E402

S = C.S
kap, lam = sp.symbols("kappa lambda", positive=True)
x = sp.Symbol("x", positive=True)
XMIN2 = 8      # l >= 2: kappa = x^2 >= 8
T1 = sp.pi/sp.sqrt(2)


def load(cache=None):
    if cache:
        try:
            d = pickle.load(open(cache, "rb"))
            from sympy import (Add, Float, Function, Integer, Mul, Pow, Rational, Symbol, ImmutableDenseMatrix,  # noqa
                               MutableDenseMatrix)
            ns = {k: getattr(sp, k) for k in dir(sp) if not k.startswith("_")}
            return [eval(q, ns) for q in d["MS"]], [eval(q, ns) for q in d["MV"]]
        except Exception:
            pass
    import harmonics5 as H5
    eqsS, okS, _ = H5.reduce_scalar()
    MS, _ = H5.matrices_n(eqsS, H5.FS)
    eqsV, okV, _ = H5.reduce_vector()
    MV, _ = H5.matrices_n(eqsV, H5.FV)
    assert okS and okV
    return MS, MV


def laurent(e):
    """e as {(a, b): c} with e = sum c s^a x^b, exact"""
    e = sp.expand(sp.cancel(e))
    num, den = sp.fraction(sp.together(e))
    dp = sp.Poly(den, x, S)
    assert len(dp.terms()) == 1, "denominator is not a monomial in x: %s" % den
    (dmon, dc), = dp.terms()
    assert dmon[1] == 0
    out = {}
    for (bx, a), c in sp.Poly(sp.expand(num), x, S).terms():
        out[(a, bx - dmon[0])] = out.get((a, bx - dmon[0]), 0) + c/dc
    return out


def normalised(M, sub, W):
    n = M[0].shape[0]
    return [sp.Matrix(n, n, lambda i, j: sp.expand(sp.cancel(M[o][i, j].subs(sub)*W[i]/W[j]))) for o in range(3)]


def bounds(Mt, n, s1=1):
    """a1 >= sup_s |A'(s)|_F, (n0, n1) with |M0 - x^2/2|_F <= n0 + n1 x, for s in [0, s1], x^2 >= 8; exact
    rationals (powers of 8^(1/2) rounded up to rationals)"""
    r8 = sp.Rational(2829, 1000)     # > 8^(1/2) = 2.8284...
    def xpow(b):                      # an upper bound for x^b, b <= 0, x >= 8^(1/2)
        return sp.Integer(1) if b == 0 else (sp.Rational(1000, 2828))**(-b)
    a1sq, n0sq, n1sq = 0, 0, 0
    for i in range(n):
        for j in range(n):
            # A(s) = M1 - (1 - s) I/2, so A' = M1' + I/2
            L1 = laurent(Mt[1][i, j] + (sp.Rational(1, 2) if i == j else 0)*S)
            d1 = sum(abs(c)*a*s1**(a - 1)*xpow(b) for (a, b), c in L1.items() if a >= 1)
            assert all(b <= 0 for (a, b) in L1)
            a1sq += d1**2
            L0 = laurent(Mt[2][i, j] - (x**2/2 if i == j else 0))
            assert all(b <= 1 for (a, b) in L0)
            n1 = sum(abs(c)*s1**a for (a, b), c in L0.items() if b == 1)
            n0 = sum(abs(c)*s1**a*xpow(b) for (a, b), c in L0.items() if b <= 0)
            n0sq += n0**2
            n1sq += n1**2
    up = lambda q: sp.Rational(int(sp.ceiling(sp.sqrt(q)*10**6)), 10**6)
    return up(a1sq), up(n0sq), up(n1sq)


def lyapunov(A):
    """H with H A + A^T H = I, exact"""
    n = A.shape[0]
    hs = sp.symbols("h0:%d" % (n*n))
    H = sp.Matrix(n, n, lambda i, j: hs[min(i, j)*n + max(i, j)])
    eqs = list(H*A + A.T*H - sp.eye(n))
    sol = sp.solve(eqs, list(set(H)), dict=True)[0]
    return H.subs(sol)


def eig_bounds(H):
    """exact isolation of lambda_min, lambda_max of the symmetric rational H"""
    lam_ = sp.Symbol("l")
    p = sp.Poly(H.charpoly(lam_).as_expr(), lam_)
    roots = sp.Poly(p, lam_).intervals(eps=sp.Rational(1, 10**8))
    lo = min(sp.Rational(a) for (a, b), m in roots)
    hi = max(sp.Rational(b) for (a, b), m in roots)
    return lo, hi


def main():
    ok = {}
    cache = sys.argv[1] if len(sys.argv) > 1 else None
    sys.argv = sys.argv[:1]      # harmonics5 reads its own argument at import
    MS, MV = load(cache)
    out = {}
    for typ, M, sub, W in (("scalar", MS, {kap: x**2}, [1, 1, 1, 1, x, x, x**2]),
                           ("vector", MV, {lam: x**2 - 1}, [1, 1, x])):
        n = M[0].shape[0]
        Mt = normalised(M, sub, W)
        m2 = S - S**2/2
        u1 = sp.expand(Mt[0] - m2*sp.eye(n)) == sp.zeros(n)
        lc = [sp.limit(Mt[2][i, j]/x**2, x, sp.oo) for i in range(n) for j in range(n)]
        u1 = u1 and all(lc[i*n + j] == (sp.Rational(1, 2) if i == j else 0) for i in range(n) for j in range(n))
        try:
            for i in range(n):
                for j in range(n):
                    assert all(b <= 0 for (a, b) in laurent(Mt[1][i, j]))
                    assert all(b <= 1 for (a, b) in laurent(Mt[2][i, j] - (x**2/2 if i == j else 0)))
        except AssertionError:
            u1 = False
        A0 = sp.Matrix(n, n, lambda i, j: sp.expand(Mt[1][i, j].subs(S, 0))) - sp.eye(n)/2
        u2a = not any(x in A0[i, j].free_symbols for i in range(n) for j in range(n))
        A0p = sp.Matrix(n, n, lambda i, j: sp.nsimplify(A0[i, j].subs(C.POINT), rational=True))
        lam_ = sp.Symbol("l")
        cp = sp.Poly(A0p.charpoly(lam_).as_expr(), lam_)
        ivs = cp.intervals(eps=sp.Rational(1, 10**6))
        nreal = sum(m_ for (a_, b_), m_ in ivs)
        ev = sorted(float((a_ + b_)/2) for (a_, b_), m_ in ivs for _ in range(m_))
        u2 = u2a and nreal == n and all(a_ > 0 for (a_, b_), m_ in ivs)
        Hm = lyapunov(A0p)
        minors = [Hm[:k, :k].det() for k in range(1, n + 1)]
        u3 = all(m_ > 0 for m_ in minors)
        mu, hmax = eig_bounds(Hm)
        Hc = lyapunov(-A0p)
        ctl = not all(Hc[:k, :k].det() > 0 for k in range(1, n + 1))
        Mtp = [m_.subs(C.POINT) for m_ in Mt]
        mp.mp.dps = 30
        res = {}
        for s1 in (sp.Integer(1), sp.Rational(3, 2)):
            a1, n0, n1 = bounds(Mtp, n, s1)
            ts = sp.sqrt(s1/(1 - s1/2))                      # sup over [0, s1] of T_s s = (s/(1 - s/2))^(1/2)
            CE = hmax/mu*(2*ts*a1 + n0 + 1 + sp.sqrt(2)*n1)
            Ts1 = sp.sqrt(2)*(sp.asin(s1 - 1) + sp.pi/2)       # T(s1)
            lnK0 = mp.mpf(sp.N(sp.log(hmax/mu)/2 + CE*Ts1/2, 30))
            res[s1] = (a1, n0, n1, CE, lnK0, Ts1)
        a1, n0, n1, CE, lnK0, _ = res[sp.Integer(1)]
        out[typ] = dict(n=n, Mt=Mtp, H=Hm, mu=mu, hmax=hmax, CE=CE, lnK0=lnK0, res=res)
        ok["U1 %s" % typ] = u1
        ok["U2 %s" % typ] = u2
        ok["U3 %s" % typ] = u3 and mu > 0
        ok["control %s" % typ] = ctl
        print("  U1 %s: second-order part m2 I, M0 = x^2 I/2 + O(x), M1 = O(1): %s" % (typ, u1))
        print("  U2 %s: A(0) independent of x: %s; eigenvalues at the record's point: %s"
              % (typ, u2a, ", ".join("%.6g" % e for e in ev)))
        print("  U3 %s: H A(0) + A(0)^T H = I, H > 0 (leading minors): %s; lambda(H) in [%.4g, %.4g]"
              % (typ, u3, float(mu), float(hmax)))
        for s1, (a1_, n0_, n1_, CE_, lnK0_, Ts1_) in res.items():
            print("  U4 %s, s in [0, %s]: a1 = %.6g, n0 = %.6g, n1 = %.6g" % (typ, s1, float(a1_), float(n0_),
                                                                           float(n1_)))
            print("  U5 %s, s in [0, %s]: T(s1) = %.6g, C_E = %.6g, ln K0 = %s (|F(s)| <= K0 |F(0)|, every l >= 2)"
                  % (typ, s1, float(Ts1_), float(CE_), mp.nstr(lnK0_, 8)), flush=True)
        print("  control %s: with A(0) -> -A(0) the Lyapunov solution is not positive: %s" % (typ, ctl))
    # U6: consistency with harmonics5's transfers, l = 2 ... 6 (floating point)
    import harmonics5 as H5
    good = True
    for typ, M, par in (("scalar", MS, kap), ("vector", MV, lam)):
        o = out[typ]
        n = o["n"]
        for l in range(2, 7):
            kv = l*(l + 2)
            xv = kv**0.5
            Ml = [sp.Matrix(n, n, lambda i, j: M[q][i, j].subs(par, kv if typ == "scalar" else kv - 1))
                  for q in range(3)]
            T6, last, Td = H5.series_transfer_n(Ml, dict(C.POINT), 400, nder=1)
            Wn = np.diag([1, 1, 1, 1, xv, xv, xv**2] if typ == "scalar" else [1, 1, xv])
            Wi = np.linalg.inv(Wn)
            Tn = Wn @ np.array([[float(T6[i, j]) for j in range(n)] for i in range(n)]) @ Wi
            Td1 = Wn @ np.array([[float(Td[1][i, j]) for j in range(n)] for i in range(n)]) @ Wi
            Hn = np.array(o["H"].evalf(), dtype=float)
            ratio = 0.0
            for j in range(n):
                F0 = np.zeros(n)
                F0[j] = 1
                F1, dF1 = Tn[:, j], Td1[:, j]*np.sqrt(0.5)      # F_T = F_s m2^(1/2), m2(1) = 1/2
                k2 = float(l*(l + 2))/2 + 1
                E0 = k2*F0 @ Hn @ F0
                E1 = dF1 @ Hn @ dF1 + k2*F1 @ Hn @ F1
                ratio = max(ratio, E1/E0)
            nrm = float(np.linalg.norm(Tn, 2))
            good = good and np.log(nrm) <= float(o["lnK0"]) and np.log(ratio) <= float(o["CE"]*T1)
            print("  U6 %s l = %d: |T|_2 = %.4g, max E(T1)/E(0) = %.4g (bound exp(C_E T1))" % (typ, l, nrm, ratio))
    ok["U6"] = good
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    return 0 if all(ok.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
