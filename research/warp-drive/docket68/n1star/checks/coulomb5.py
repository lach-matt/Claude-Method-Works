"""coulomb5.py -- BEYOND5 Lemma 6.5 (D406): the Coulomb part of the means, carried from the cone N to spatial infinity.

On five-dimensional Minkowski space in the ingoing chart (v, r), ds^2 = -dv^2 + 2 dv dr + r^2 dOmega_3^2, the wave
operator on phi = F(v, r) Y_l (Y_l a harmonic of S^3, -Delta Y_l = l(l + 2) Y_l) is

    box phi = (2 d_v d_r + (3/r) d_v + d_r^2 + (3/r) d_r - l(l + 2)/r^2) F.

On a(v) r^(-p) it gives (3 - 2p) a' r^(-p-1) + (p(p - 2) - l(l + 2)) a r^(-p-2), so with F = sum_j a_j(v) r^(-2-j) the
equation is (1 + 2j) a_j' = -(l + 1 - j)(l + 1 + j) a_(j-1), and it terminates at j = l + 1: the radial order in four
space dimensions is the integer l + 1. With a_0 = M and a_j(v1) = 0 for j >= 1,

    phi_l = M r^(-2) 2F1(-l, l + 2; 3/2; (v - v1)/(2r)) Y_l,

a polynomial in (v - v1)/r of degree l: the solution whose data on the ingoing cone N = {v = v1} are M r^(-2) Y_l and
whose radiation field at past null infinity, lim r^(3/2) phi at fixed v, vanishes.

  K1 (exact) box phi_l = 0 identically, l = 0, ..., 10.
  K2 (exact) on N, phi_l = M r^(-2); at fixed v, r^(3/2) phi_l -> 0 (no incoming radiation).
  K3 (exact) at fixed t (v = t + r), r^2 phi_l is a polynomial in 1/r of degree <= l (so phi_l is in rho^2 C^oo at
     spatial infinity, rho = 1/r), and its value at rho = 0 is cos(pi l/2)/(l + 1): 1, 0, -1/3, 0, 1/5, ...
  K4 (exact) 2F1(-l, l + 2; 3/2; s/2) = U_l(1 - s)/(l + 1), U_l the Chebyshev polynomial of the second kind (the
     Gegenbauer polynomial of S^3), so |r^2 phi_l| <= M wherever 0 <= (v - v1)/r <= 2, uniformly in l.
  K5 (exact) on Tangherlini, ds^2 = -f dv^2 + 2 dv dr + r^2 dOmega_3^2, f = 1 - mu/r^2, box gains exactly
     -mu r^-3 d_r(r d_r F), and the recursion becomes (1 + 2j) a_j' = -(l + 1 - j)(l + 1 + j) a_(j-1) - mu (j - 1)^2
     a_(j-3). The factor 1 + 2j never vanishes, so no logarithm enters; the mu terms have degree <= j - 2 in
     v - v1, so the top degrees, and with them the flat polynomial of K1-K4, are unchanged. Checked: box of the
     truncated sum leaves only powers r^-p with p beyond the truncation, l <= 3, mu symbolic.
  K6 (computed, exact rationals) at mu = 1 on t = const (v1 - t = 1): r^2 phi summed to j = 20, 40, 60 at r = 5,
     10, 40 agrees to better than 1e-8 between 40 and 60 terms, l = 0, ..., 3: the series converges out to spatial
     infinity, and r^2 phi tends to the flat value cos(pi l/2)/(l + 1) with an O(rho^2) correction.
  Control: with the sign of the cross term flipped (the recursion (1 + 2j) a_j' = +(l + 1 - j)(l + 1 + j) a_(j-1)),
     the polynomial so built is not a solution at l >= 1, and its limit at rho = 0 grows (2, 5, 14, ...).
Labels: computed (exact, sympy).

    python3 checks/coulomb5.py [--selftest]      (about five minutes, K6 most of it)
"""
import sys

import sympy as sp

v, r, t, v1, M, rho = sp.symbols("v r t v1 M rho", real=True)


def box(F, l):
    return sp.expand(2*sp.diff(F, v, r) + 3*sp.diff(F, v)/r + sp.diff(F, r, 2) + 3*sp.diff(F, r)/r
                     - l*(l + 2)*F/r**2)


def phi(l, sign=-1):
    """r^-2 sum_j a_j r^-j with (1 + 2j) a_j' = sign (l + 1 - j)(l + 1 + j) a_(j-1), a_0 = M, a_j(v1) = 0"""
    a = [M]
    for j in range(1, l + 1):
        a.append(sp.integrate(sign*(l + 1 - j)*(l + 1 + j)*a[-1]/(1 + 2*j), (v, v1, v)))
    return sum(aj*r**(-2 - j) for j, aj in enumerate(a))


def boxT(F, l, mu):
    return sp.expand(box(F, l) - mu*sp.diff(r*sp.diff(F, r), r)/r**3)


def coeffs_T(l, mu, J):
    a = [M]
    for j in range(1, J + 1):
        rhs = -(l + 1 - j)*(l + 1 + j)*a[j - 1] - (mu*(j - 1)**2*a[j - 3] if j >= 3 else 0)
        a.append(sp.expand(sp.integrate(sp.expand(rhs/(1 + 2*j)), (v, v1, v))))
    return a


def tang_checks():
    mu = sp.symbols("mu", positive=True)
    k5 = True
    for l in range(4):
        J = 8
        a = coeffs_T(l, mu, J)
        F = sum(aj*r**(-2 - j) for j, aj in enumerate(a))
        # the residual of the truncated sum has only powers r^-p, p >= J + 4: times r^(J+4) it is a polynomial in 1/r
        res = sp.expand(sp.expand(boxT(F, l, mu)*r**(J + 4)).subs(r, 1/rho))
        try:
            sp.Poly(res, rho)
            poly_ok = True
        except sp.PolynomialError:
            poly_ok = False
        k5 &= poly_ok and sp.expand(F.subs(mu, 0) - phi(l)) == 0
    k6, rows = True, []
    for l in range(4):
        a = [sp.expand(c.subs({M: 1, v1: 0})) for c in coeffs_T(l, 1, 60)]
        for rr in (5, 10, 40):
            vals = []
            for J in (20, 40, 60):
                vv = sp.Rational(rr) - 1          # v = t + r with t = v1 - 1 = -1
                vals.append(sum(aj.subs(v, vv)*sp.Rational(rr)**(-j) for j, aj in enumerate(a[:J + 1])))
            d = abs(float(vals[2] - vals[1]))
            k6 &= d < 1e-8
            rows.append((l, rr, float(vals[2]), d))
    return k5, k6, rows


def main():
    ok = {"K1": True, "K2": True, "K3": True, "K4": True, "control": True}
    s = sp.symbols("s", real=True)
    vals = []
    for l in range(11):
        F = phi(l)
        hyp = M*r**-2*sp.hyper([-l, l + 2], [sp.Rational(3, 2)], (v - v1)/(2*r))
        ok["K1"] &= box(F, l) == 0 and sp.simplify(sp.hyperexpand(hyp) - F) == 0
        ok["K2"] &= sp.simplify(F.subs(v, v1) - M/r**2) == 0 and sp.limit(r**sp.Rational(3, 2)*F, r, sp.oo) == 0
        G = sp.expand((r**2*F).subs(v, t + r).subs(r, 1/rho))
        poly = sp.Poly(G, rho)
        lim = sp.simplify(G.subs(rho, 0)/M)
        vals.append(lim)
        ok["K3"] &= poly.degree() <= l and sp.simplify(lim - sp.cos(sp.pi*l/2)/(l + 1)) == 0
        P = sp.expand(sp.hyperexpand(sp.hyper([-l, l + 2], [sp.Rational(3, 2)], s/2)))
        ok["K4"] &= sp.expand(P - sp.chebyshevu(l, 1 - s)/(l + 1)) == 0
        if l >= 1:
            Fc = phi(l, sign=+1)
            limc = sp.simplify(sp.limit(sp.expand(r**2*Fc.subs(v, t + r)), r, sp.oo)/M)
            ok["control"] &= box(Fc, l) != 0 and abs(limc) > 1
    k5, k6, rows = tang_checks()
    ok["K5"], ok["K6"] = k5, k6
    for l, rr, val, d in rows:
        print("  K6: l = %d, r = %2d: r^2 phi = %+.8f (flat limit %+.4f), |sum_60 - sum_40| = %.1e"
              % (l, rr, val, float(sp.cos(sp.pi*l/2)/(l + 1)), d))
    print("  K1-K4: box phi_l = 0, data M r^-2 on N, no incoming radiation, rho^2 C^oo at fixed t, U_l form;"
          " r^2 phi_l at rho = 0:")
    print("        ", ", ".join(str(q) for q in vals))
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
