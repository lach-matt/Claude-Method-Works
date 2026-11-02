#!/usr/bin/env python3
"""re813.py -- [Hin26] (8.13) as h = 1/gam_C varies (N1STAR-PROOF.md 10.54(d); D607: a verifier found the case R1).

(8.13) asks d(Re lam, Z) >= eps_ind > 0 for the non-integer indicial roots with |lam| <= 50. 10.54(d) said it holds at
every h in (0, 10^-6] with its own eps_ind(h) > 0, "each non-integer one lying off Z". That is false: a non-real root
can have integer real part. Here box^C's roots in L's variable (box^C's less 1, eind5.py's shift; damping5.py's
polynomials with h symbolic and (v, e_C) = (1/2, 1/102400)): for an integer n, P(n + iy) = A(y^2) + i y B(y^2) with
A, B real polynomials, and a non-real root of real part n is a common root t = y^2 > 0 of A and B, so it occurs only
where the resultant R_n = Res_t(A, B), a polynomial in (kappa, h), vanishes (A's leading coefficient is +-h^3, h^2 or
h, nonzero for h > 0).

  R1 (exact, then 60 digits) At l = 1000 and n = 2, R_2 has one root h in (0, 10^-6] (Sturm; h = 0 is a triple root),
     isolated to 10^-30; at one of them L has a non-real root of real part 2 with |lam| <= 50, so (8.13) fails at that h
     for every eps_ind.
  R2 (exact) For the scalar sextic (every l >= 1), the vector quadratic (every l >= 1) and the scalar quartic (l = 0),
     and each integer n with |n| <= 50: R_n is not identically zero at any l. For the l >= 1 families the greatest
     common divisor in Q[kappa] of R_n's coefficients in h has no root kappa = l (l + 2) with l >= 1 integer; so at each
     l and n, R_n(kappa_l, h) vanishes at finitely many h.
  R3 (exact) The top coefficient in kappa is free of lam and nonzero for h > 0 (h^3 kappa^3 in the sextic, h kappa in
     the quadratic), so at each h only finitely many l carry a root with |lam| <= 50.
  Controls: R1 at h = 10^-6 itself, where the non-real root nearest Re lam = 2 lies 0.25 from it (the record's point
     satisfies (8.13), 10.52); R2 on (lam - 2)^2 + 1 + kappa h, whose roots 2 +- i (1 + kappa h)^(1/2) have real part
     2 at every h, so R_2 vanishes identically, and on (lam - 2)^2 + 1 + (kappa - 8) h, for which it vanishes only at
     kappa = 8 (l = 2, the gcd branch): the test must report both; R3 on the sextic plus lam h^3 kappa^3,
     whose top coefficient involves lam.

Deduced (from R2-R3): (8.13) holds at every h in (0, 10^-6] outside a countable set (finitely many h for each l and n,
countably many (l, n)), with eps_ind(h) > 0 there; box^Ups's roots do not involve h (10.52(ii): l <= 52). R1 shows the
set is not empty. Labels: computed (R1-R3, exact; R1's root located in 60-digit arithmetic), deduced (the countable
set).

Run: python3 checks/re813.py   (about a minute; imports damping5.py)
"""
import os
import sys
import time

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import damping5 as D                                                             # noqa: E402

V, EC, H1 = sp.Rational(1, 2), sp.Rational(1, 102400), sp.Rational(1, 10**6)
h, lam, K = D.h, D.lam, D.K
n, t = sp.symbols("n t")
NMAX = 50


def families():
    pk, p0, pv = D.polys(4, sp.Rational(2, 3))
    sub = {D.v: V, D.e: EC}
    return [(name, sp.expand(p.subs(sub).subs(lam, lam + 1))) for name, p in
            [("scalar sextic", pk), ("vector quadratic", pv), ("scalar quartic (l = 0)", p0)]]


def split(P):
    """A(t), B(t) with P(n + i y) = A(y^2) + i y B(y^2), t = y^2"""
    A, B = 0, 0
    for j in range(sp.Poly(P, lam).degree() + 1):
        c = sp.expand(sp.diff(P, lam, j).subs(lam, n)/sp.factorial(j))
        if j % 2 == 0:
            A += c*(-t)**(j//2)
        else:
            B += c*(-t)**((j - 1)//2)
    return sp.expand(A), sp.expand(B)


def resultant(P, nv):
    A, B = split(P)
    A, B = sp.Poly(A.subs(n, nv), t), sp.Poly(B.subs(n, nv), t)
    if B.degree() <= 0:                                                       # quadratic: Res = B^deg A
        return sp.expand(B.as_expr()**A.degree())
    return sp.expand(sp.resultant(A, B))


def bad_l(R):
    """l >= 1 with R(kappa_l, h) identically zero in h: the integer l whose kappa = l (l + 2) is a root of the gcd"""
    if R == 0:
        return "identically zero"
    cs = [sp.Poly(c, K) for c in sp.Poly(R, h).all_coeffs()]
    g = cs[0]
    for c in cs[1:]:
        g = sp.gcd(g, c)
        if g.degree() == 0:
            return []
    out = []
    for r in sp.Poly(g, K).real_roots():
        lv = sp.sqrt(1 + r) - 1
        if lv.is_integer and lv >= 1:
            out.append(int(lv))
    return out


def roots_at(P, kv, hv, dps=60):
    mp.mp.dps = dps
    q = sp.Poly(P.subs(K, kv).subs(h, hv), lam)
    return mp.polyroots([mp.mpf(sp.Rational(c).p)/mp.mpf(sp.Rational(c).q) for c in q.all_coeffs()],
                        maxsteps=400, extraprec=400)


def r1(control=False):
    P = families()[0][1]
    lv, nv = 1000, 2
    kv = lv*(lv + 2)
    if control:
        rs = roots_at(P, kv, H1)
        d = min(abs(r.real - nv) for r in rs if abs(r.imag) > 1e-20 and abs(r) <= 50)
        return d < mp.mpf(10)**-20
    R = sp.Poly(resultant(P, nv).subs(K, kv), h)
    cnt = R.count_roots(0, H1) - (1 if R.eval(0) == 0 else 0)
    hits = []
    for (a, b), _ in R.intervals(eps=sp.Rational(1, 10**30), inf=0, sup=H1):
        if a <= 0:
            continue
        hm = (a + b)/2
        for r in roots_at(P, kv, hm):
            if abs(r.real - nv) < mp.mpf(10)**-20:
                hits.append((a, b, r))
    nonreal = [x for x in hits if abs(x[2].imag) > 1e-3 and abs(x[2]) <= 50]
    for a, b, r in hits:
        print("  R1: l = %d, n = %d: R_n has a root h in (%s, %s); there L has the root %s (|lam| = %s)"
              % (lv, nv, mp.nstr(mp.mpf(a.p)/a.q, 15), mp.nstr(mp.mpf(b.p)/b.q, 15), mp.nstr(r, 12),
                 mp.nstr(abs(r), 6)), flush=True)
    nh = len({(a, b) for a, b, _ in nonreal})
    print("  R1: %d root(s) h of R_2 in (0, 10^-6]; at %d of them L has a conjugate pair of non-real roots of real part"
          " 2 with |lam| <= 50, so (8.13) fails there" % (cnt, nh), flush=True)
    return cnt >= 1 and nh >= 1


def r2(control=False):
    t0 = time.time()
    if control:                       # both branches: R identically zero, and zero only at kappa = 8 (l = 2)
        Pa = sp.expand((lam - 2)**2 + 1 + K*h)
        Pb = sp.expand((lam - 2)**2 + 1 + (K - 8)*h)
        return bad_l(resultant(Pa, 2)) == [] or bad_l(resultant(Pb, 2)) == []
    ok, rows = True, []
    for name, P in families():
        zero = []
        for nv in range(-NMAX, NMAX + 1):
            R = resultant(P, nv)
            if K in P.free_symbols:
                b = bad_l(R)
                if b:
                    zero.append((nv, b))
            elif R == 0 or sp.Poly(R, h).is_zero:
                zero.append((nv, "identically zero"))
        rows.append("%s: %s" % (name, "R_n not identically zero at any l, for each |n| <= %d" % NMAX if not zero
                                else "identically zero at %s" % zero))
        ok &= not zero
    print("  R2: " + "; ".join(rows) + " [%.0fs]" % (time.time() - t0), flush=True)
    return ok


def r3(control=False):
    fam = families()[:2]
    if control:                                                              # a top coefficient that involves lam
        fam = [(name, sp.expand(P + lam*h**3*K**3)) for name, P in fam[:1]]
    out, ok = [], True
    for name, P in fam:
        Pk = sp.Poly(P, K)
        top = sp.factor(Pk.LC())
        free = lam not in top.free_symbols
        out.append("%s: top coefficient in kappa (degree %d) %s, free of lam: %s" % (name, Pk.degree(), top, free))
        ok &= free and top.subs(h, H1) != 0 and sp.Poly(top, h).count_roots(0, H1) == (1 if top.subs(h, 0) == 0
                                                                                        else 0)
    if not control:
        print("  R3: " + "; ".join(out), flush=True)
    return ok


CHECKS = [("R1", r1), ("R2", r2), ("R3", r3)]


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
