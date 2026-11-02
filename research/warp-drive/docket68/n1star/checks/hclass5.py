#!/usr/bin/env python3
"""hclass5.py -- c5: the h-dependence of each conclusion drawn at the parameter point (N1STAR-PROOF.md section 10.54,
Proposition 10.44 (b)-(e); h = 1/gam_C, the point h_1 = 10^-6 with (v, e_C) = (1/2, 1/102400)), computed by class.

10.54 sorts the point's conclusions: (b) those inherited from the constraint damping, which uniform5.py H1-H2 computes
for every h in (0, h_1] (exact); (c) those free of h, or proportional to gam_C = 1/h and used through lower bounds or
signs only; (d) those holding off a countable set of h; (e) the horizon threshold, below an h_2 (section 10.79, D171).
Classes (b) and (e) are computed by their programs; this program computes (c), and of (d) simplicity and integer
roots. (8.13) as h varies is NOT checked here: a non-real root can have integer real part (at l = 1000 one does, at
an h near 6.65 x 10^-7), so 10.54(d)'s "(8.13) at every h" is false; checks/re813.py computes it (R1 the failure, R2
that it holds off a countable set).

  H1 (exact) Class (c): the quantities proportional to gam_C -- A_0's diagonal 2 (1 - v) gam_C, (1 - v) gam_C,
     (1 - e_C)(1 - v) gam_C (10.35(i), 10.54(c)'s first item), the I+ gap's upper end 3/2 + (1 - e_C)(1 - v) gam_C
     (10.44), dual5.py's 3 + 2 v gam_C (10.31), tface5.py's S_in = h^-1 (1 - e)(1 + v) (10.23), strap5.py's diagonal
     -2 (1 - e_C) gam c_2, -2 gam c_2, -4 gam c_2 (10.26), with the record's c_2 = -g^-1(c_C, e_0) < 0 (a negative
     symbol; -1 where a value is needed) -- each is positive on (0, h_1] (for strap5's: the record's 'every diagonal
     block is >= 0'), with derivative in h of fixed sign there making |q| grow as h falls, so each is bounded below by
     its value at h_1: a lower bound or a sign used at the point holds at every smaller h. Signs are printed.
  H2 (exact) Class (d), simplicity and integer roots only. damping5.py's polynomials at lam + 1 (eind5.py's shift; h
     symbolic, (v, e) at the point), for each l in {0, 1, ..., 20}, kappa = l (l + 2):
     (a) box^C's scalar sextic (the quartic at l = 0): its discriminant in lam (simplicity) and its value P(n) at each
         integer |n| <= 52 (an integer root) are polynomials in h, each checked not identically zero, the discriminant
         also nonzero at h_1; the roots of each in (0, h_1] are counted (Sturm). Skipped, as identically zero in h:
         n = 1 at l = 0 and at l = 1 (the root lam + 1 = 2 for every h; printed).
     (b) the vector quadratic (l >= 1) the same way; skipped as identically zero: n = 2 at l = 1 (printed). Printed
         example beyond the sample: at l = 1000, n = 3 it is 1001992 h - 1, a root h = 1/1001992 in (0, h_1].
     (c) box^C's resultant with Q(lam - 1) (10.52(i)'s simplicity condition; Q as at 10.52, z = 4 x 10^-6) as a
         polynomial in h for l >= 1: not identically zero, nonzero at h_1, roots in (0, h_1] counted. At l = 0 it is
         identically zero (Q(lam - 1) at kappa = 0 has the root lam = 1, box^C's Coulomb root), so l = 0 is left out.
     The roots found in (0, h_1] are printed. The physical roots and box^Ups's do not involve h.
  Controls: H1 on h itself, which falls with h (fails 'bounded below by its value at h_1'); H2 on the mutant P (lam - 3)
     of damping5.py's sextic at l = 2, which has the integer root 3 at every h, so its P(3) is identically zero and the
     test must report it.

Reach: H2 samples l <= 20 and |n| <= 52; at each sampled (l, n) a nonzero polynomial vanishes at finitely many h.
For every l, eind5.py E1 and eindcert5.py I1 bound box^C's scalar P(n) and its discriminant at h_1 only: that makes
those polynomials in h nonzero, and locates none of their roots in (0, h_1); they cover nothing else as h varies.
(8.13): see checks/re813.py. Labels: computed (exact, sympy).

Run: python3 checks/hclass5.py   (a few minutes; imports damping5.py)
"""
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import damping5 as D                                                             # noqa: E402

V, EC, H1 = sp.Rational(1, 2), sp.Rational(1, 102400), sp.Rational(1, 10**6)
Z_UPS = 4*sp.Rational(1, 100)*sp.Rational(1, 100)**2                    # z = 4 e_Ups gam_Ups^2 = 4 x 10^-6
h, lam, K = D.h, D.lam, D.K
LMAX, NMAX = 20, 52


def h1(control=False):
    gam = 1/h
    c2 = sp.Symbol("c_2", negative=True)                                 # the record's c_2 = -g^-1(c_C, e_0) < 0
    qs = {"A_0 2 (1 - v) gam": 2*(1 - V)*gam, "A_0 (1 - v) gam": (1 - V)*gam,
          "A_0 (1 - e) (1 - v) gam": (1 - EC)*(1 - V)*gam,
          "I+ gap upper end": sp.Rational(3, 2) + (1 - EC)*(1 - V)*gam, "dual5 3 + 2 v gam": 3 + 2*V*gam,
          "tface5 S_in": (1 - EC)*(1 + V)/h, "strap5 -2 (1 - e) gam c2": -2*(1 - EC)*gam*c2,
          "strap5 -2 gam c2": -2*gam*c2, "strap5 -4 gam c2": -4*gam*c2}
    if control:
        qs = {"h": h}
    x = sp.Symbol("x", positive=True)                                    # h = h_1 x, x in (0, 1]
    ok, rows = True, []
    for name, q in qs.items():
        qx = q.subs(h, H1*x)
        sign_d = sp.sign(sp.simplify(sp.diff(q, h).subs(h, H1*x)))      # c_2 < 0 symbolic: no value substituted
        sign_q = sp.sign(sp.simplify(qx))
        sign_q1 = sp.sign(qx.subs({x: 1, c2: -1}))
        grows = sign_d in (1, -1) and sp.simplify(sign_d*sign_q) == -1  # |q| grows as h falls
        rows.append("%s: sign %s (c_2 = -1 at h_1: %s), d/dh sign %s, grows as h falls %s"
                    % (name, sign_q, sign_q1, sign_d, grows))
        ok &= sign_q == 1 and sign_q1 == 1 and grows                      # the record's sign: each >= 0, here > 0
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


def families():
    pk, p0, pv = D.polys(4, sp.Rational(2, 3))
    sub = {D.v: V, D.e: EC}
    return [sp.expand(p.subs(sub).subs(lam, lam + 1)) for p in (pk, p0, pv)]   # box^C at lam + 1, eind5.py's shift


def Q(lm, kap, z=Z_UPS):
    return (lm*(lm - 1))**2 - (2 + 2*kap + z)*lm*(lm - 1) + kap*(kap + 1) + z*kap


def scan(P, tag, lv, out, nint=True, disc=True, qres=False):
    """P a polynomial in (lam, h) at this l; records into out; returns ok"""
    ok = True
    tests = []
    if disc:
        tests.append(("disc", sp.discriminant(sp.Poly(P, lam).as_expr(), lam)))
    if qres:
        tests.append(("Q-res", sp.resultant(P, sp.expand(Q(lam - 1, lv*(lv + 2))), lam)))
    for name, pol in tests:
        zero, cnt = nonzero_poly_roots(pol)
        ok &= not zero and sp.expand(pol).subs(h, H1) != 0
        out["count"][name] = out["count"].get(name, 0) + 1
        if zero or cnt:
            out["found"].append((tag, name, lv, "identically 0" if zero else cnt))
    if nint:
        for n in range(-NMAX, NMAX + 1):
            zero, cnt = nonzero_poly_roots(P.subs(lam, n))
            if zero:
                out["skipped"].append((tag, lv, n))
                continue
            out["count"]["P(n)"] = out["count"].get("P(n)", 0) + 1
            if cnt:
                out["found"].append((tag, "n = %d" % n, lv, cnt))
    return ok


SKIP = {("scalar", 0, 1), ("scalar", 1, 1), ("vector", 1, 2)}           # identically zero in h: lam + 1 = 2, 3


def h2(control=False):
    PK, P0, PV = families()
    out = {"count": {}, "found": [], "skipped": []}
    if control:                                                          # damping5's sextic times (lam - 3), at l = 2
        scan(sp.expand(PK.subs(K, 8)*(lam - 3)), "mutant", 2, out, disc=False)
        return ("mutant", 2, 3) not in out["skipped"]
    ok = True
    for lv in range(LMAX + 1):
        P = P0 if lv == 0 else sp.expand(PK.subs(K, lv*(lv + 2)))
        ok &= scan(P, "scalar", lv, out, qres=lv >= 1)  # l = 0: Q(lam - 1) has lam = 1 too
        if lv >= 1:
            ok &= scan(sp.expand(PV.subs(K, lv*(lv + 2))), "vector", lv, out)
    ok &= set(out["skipped"]) == SKIP
    ex = sp.expand(PV.subs(K, 1000*1002).subs(lam, 3))
    _, exc = nonzero_poly_roots(ex)
    print("  H2: l = 0, 1, ..., %d (simplicity and integer roots; (8.13) is checks/re813.py's): counted %s, each a "
          "nonzero polynomial in h; skipped as identically zero (type, l, n): %s; roots in (0, h_1]: %s"
          % (LMAX, out["count"], sorted(out["skipped"]), out["found"] or "none"), flush=True)
    print("  H2 example beyond the sample: vector quadratic at l = 1000, n = 3: %s, %d root(s) in (0, h_1] (h = %s)"
          % (ex, exc, sp.solve(ex, h)), flush=True)
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
