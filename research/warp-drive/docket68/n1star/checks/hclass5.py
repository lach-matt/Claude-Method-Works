#!/usr/bin/env python3
"""hclass5.py -- c5: the h-dependence of each conclusion drawn at the parameter point (N1STAR-PROOF.md section 10.54,
Proposition 10.44 (b)-(e); h = 1/gam_C, the point h_1 = 10^-6 with (v, e_C) = (1/2, 1/102400)), computed by class.

10.54 sorts the point's conclusions: (b) those inherited from the constraint damping, which uniform5.py H1-H2 computes
for every h in (0, h_1] (exact); (c) those free of h, or proportional to gam_C = 1/h and used through lower bounds or
signs only; (d) those holding off a countable set of h; (e) the horizon threshold, below an h_2 (section 10.79, D171).
Classes (b) and (e) are computed by their programs; this program computes (c) and (d).

  H1 (exact) Class (c): the quantities proportional to gam_C -- the I+ gap's upper end 3/2 + (1 - e_C)(1 - v) gam_C
     (10.44), dual5.py's 3 + 2 v gam_C (10.31), tface5.py's S_in = h^-1 (1 - e)(1 + v) (10.23), strap5.py's diagonal
     -2 (1 - e_C) gam, -2 gam, -4 gam times c_2 (10.26) -- are monotone in h on (0, h_1] (derivative of fixed sign) with
     their sign fixed there, so each is bounded below (in modulus) by its value at h_1: a lower bound or a sign used at
     the point holds at every smaller h.
  H2 (exact) Class (d): box^C's scalar sextic at lam + 1 (damping5.py, h symbolic, (v, e) at the point) gives, for each
     l in {0, 2, 3, ..., 20} and each integer n with |n| <= 52, the polynomial p(n; kappa_l, h) in h, and the
     discriminant in lam, a polynomial in h. Each is not identically zero (its value at h_1 is not 0), so it vanishes at
     finitely many h: the number of its roots in (0, h_1] is counted (Sturm). So simplicity (10.52(i)) and an integer
     root, hence eps_ind(h) > 0 in (8.13), fail at most at finitely many h for each (l, n), countably many in all; the
     roots in (0, h_1] found are printed. The physical roots and box^Ups's do not involve h (box^Ups's constant is z =
     4 e_U gam_U^2, a different parameter).
  Control: h itself, which falls with h, fails H1's 'bounded below by its value at h_1'; and lam = l + 2, a physical
     root, makes the polynomial (lam - l - 2) vanish for every h, which H2's test reports as identically zero.

Reach: H2 samples l <= 20 (the deduction for every l is 10.54 (d)'s: the polynomial's value at h_1 is nonzero for every
l by eind5.py E1 and eindcert5.py I1, so each is a nonzero polynomial). Labels: computed (exact, sympy).

Run: python3 checks/hclass5.py   (a few minutes; imports damping5.py)
"""
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import damping5 as D                                                             # noqa: E402

V, EC, H1 = sp.Rational(1, 2), sp.Rational(1, 102400), sp.Rational(1, 10**6)
h, lam, K = D.h, D.lam, D.K
LMAX, NMAX = 20, 52


def h1(control=False):
    gam = 1/h
    c2 = sp.Symbol("c_2", positive=True)
    qs = {"I+ gap upper end": sp.Rational(3, 2) + (1 - EC)*(1 - V)*gam, "dual5 3 + 2 v gam": 3 + 2*V*gam,
          "tface5 S_in": (1 - EC)*(1 + V)/h, "strap5 -2 (1 - e) gam c2": -2*(1 - EC)*gam*c2,
          "strap5 -2 gam c2": -2*gam*c2, "strap5 -4 gam c2": -4*gam*c2}
    if control:
        qs = {"h": h}
    ok = True
    rows = []
    for name, q in qs.items():
        dq = sp.diff(q, h)
        x = sp.Symbol("x", positive=True)                                # h = h_1 x, x in (0, 1]
        sign_d = sp.sign(sp.simplify(dq.subs(h, H1*x).subs(c2, 1)))
        sign_q = sp.sign(sp.simplify(q.subs(h, H1*x).subs(c2, 1)))
        mono = sign_d in (1, -1) and sign_q in (1, -1)
        grows = sp.simplify(sign_d*sign_q) == -1                          # |q| grows as h falls
        rows.append("%s: d/dh sign %s, sign %s, |q| grows as h falls %s" % (name, sign_d, sign_q, grows))
        ok &= mono and grows
    if control:
        return ok
    print("  H1: " + "; ".join(rows), flush=True)
    return ok


def nonzero_poly_roots(expr):
    """(identically zero?, roots in (0, h_1]) of a polynomial in h"""
    P = sp.Poly(sp.expand(expr), h)
    if P.is_zero:
        return True, None
    return False, P.count_roots(0, H1) - (1 if P.eval(0) == 0 else 0)


def h2(control=False):
    if control:
        zero, _ = nonzero_poly_roots(sp.expand((lam - 2 - 2).subs(lam, 4)))   # lam = l + 2 at l = 2, every h
        return not zero
    pk, p0, pv = D.polys(4, sp.Rational(2, 3))
    PK = sp.expand(pk.subs({D.v: V, D.e: EC}))
    P0 = sp.expand(p0.subs({D.v: V, D.e: EC}))
    ok, found, nint, ndisc = True, [], 0, 0
    for lv in [0] + list(range(2, LMAX + 1)):
        P = P0 if lv == 0 else PK.subs(K, lv*(lv + 2))
        P = sp.expand(P.subs(lam, lam + 1))                              # box^C at lam + 1, eind5.py's shift
        disc = sp.discriminant(sp.Poly(P, lam).as_expr(), lam)
        zero, cnt = nonzero_poly_roots(disc)
        ok &= not zero and sp.expand(disc).subs(h, H1) != 0
        ndisc += 1
        if cnt:
            found.append(("disc", lv, cnt))
        for n in range(-NMAX, NMAX + 1):
            if lv == 0 and n == 1:
                continue                                                 # box^C's Coulomb root 2 = lam + 1 at l = 0
            val = P.subs(lam, n)
            zero, cnt = nonzero_poly_roots(val)
            nint += 1
            ok &= not zero
            if cnt:
                found.append(("lam = %d" % n, lv, cnt))
    print("  H2: l = 0, 2, ..., %d: %d discriminants and %d integer values, each a nonzero polynomial in h; roots in (0,"
          " h_1]: %s" % (LMAX, ndisc, nint, found or "none"), flush=True)
    return ok


CHECKS = [("H1", h1), ("H2", h2)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
