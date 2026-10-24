#!/usr/bin/env python3
"""uniform5.py -- the strong constraint damping of 10.12 for every small h, not only at the point (Phase B's B5;
N1STAR-PROOF.md section 10.54; D124).  Labels: computed (exact, sympy), READ.

[Hin26a] (arXiv:2606.27658v2) fixes no numerical h: its Theorem 4.9 (p. 37) reads "there exists e_0 = e_0(v) in (0, 1)
such that for all e in (0, e_0), there exists h_0 > 0 such that for all h in (0, h_0), all indicial roots ... satisfy
(1) Re lam >= 1 or Re lam < -C_0", and its Theorems 5.2 and 6.2 hold for every h below an h_0 their proofs do not make
explicit.  The record computed the five-dimensional roots at one point, h = 10^-6 (damping5.py U4), and so needed that
point below h_0.  Here, at the record's (v, e) = (1/2, 1/102400) and C_0 = 100, the same conclusions for every h in (0,
h_1], h_1 = 10^-6, so that any h below min(h_0, h_1) serves.

The argument is damping5.py U4's with h a second parameter.  For h > 0 the leading coefficient in lam of box^C's indicial
polynomial, -h^3 (scalar types l >= 1), h^2 (scalar type 0) or -h (vector type), does not vanish (D129), so its roots
move continuously over the connected region R = {kappa >= kappa_0, 0 < h <= h_1}; a root reaches the line Re lam = x only
where the shifted constant coefficient F_1 or the Hurwitz determinant F_2 (Orlando: it vanishes when two shifted roots
sum to zero) vanishes.  F_1 and F_2 are polynomials in (kappa, h); for fixed h the number of their roots kappa >= kappa_0
can change only at an h where their leading coefficient in kappa, their value at kappa_0 or their discriminant in kappa
vanishes.  None of these has a root in (0, h_1] (Sturm), and at h_1 neither has a root kappa >= kappa_0 (Sturm): so
neither vanishes on R, no root crosses either line, and the counts on each side are those at one point of R.

  H1 (computed, exact) The strip [-100, 19/10].  Scalar type l >= 1 (the sextic, kappa >= 3) and vector type (the
     quadratic, kappa >= 3): F_1, F_2 at Re lam = -100 and 19/10 vanish nowhere on R; scalar type 0 (the quartic, kappa
     = 0): F_1, F_2 are polynomials in h with no root in (0, h_1].  Counts (right | between | left, as 10.12) at
     (kappa, h) = (3, h_1) and at l = 0 (Routh): 3 | 0 | 3, 1 | 0 | 1, 2 | 0 | 2.  So for every h in (0, h_1] no
     indicial root of box^C at any l has real part in [-100, 19/10].
  H2 (computed, exact) Up to the Coulomb root.  At Re lam = 2: scalar types l >= 2 (kappa >= 8) and the vector type
     (kappa >= 3) as in H1, 3 | 0 | 3 and 1 | 0 | 1; at l = 1 and l = 0, lam = 2 divides the polynomial for every h
     (exactly), and the cofactors, a quintic and a cubic in lam with coefficients in h, have no crossing for h in (0,
     h_1] and do not vanish at lam = 2 there: 2 | 0 | 3 and 1 | 0 | 2.  So for every h in (0, h_1] the only roots with
     real part in [-100, 2] are lam = 2 at l = 0 and 1, simple.
  Mutant: h_1 = 10^-3, above e, where the upper roots fall below 2 (damping5.py U6) and the critical values appear.

sympy; imports damping5.py.  python3 uniform5.py [--selftest | --mutants]   (under a minute each)
"""
import sys
import time

import sympy as sp

import damping5 as D
from damping5 import Checklist

lam, K, mu = D.lam, D.K, D.mu_
HS = [s for s in D.PARAMS if s.name == "h"][0]
VE = {s: val for s, val in D.PARAMS.items() if s.name != "h"}
H1 = sp.Rational(1, 10**6)

_F = {}


def families():
    """box^C's indicial polynomials at (v, e), h symbolic: scalar l >= 1 (kappa), vector (kappa), scalar 0"""
    if not _F:
        pk, p0, pv = D.polys(4, sp.Rational(2, 3))
        _F["s"] = sp.expand(pk.subs(VE))
        _F["v"] = sp.expand(pv.subs(VE))
        _F["0"] = sp.expand(p0.subs(VE))
    return _F


def crossing(P, x):
    """the shifted constant coefficient and Hurwitz determinant of P (a polynomial in lam) at Re lam = x"""
    cs = sp.Poly(sp.expand(P.subs(lam, x + mu)), mu).all_coeffs()
    return [sp.expand(cs[-1]), sp.expand(D.hurwitz_det(cs, len(cs) - 2))]


def h_roots(expr, h1):
    """the number of roots of a polynomial in h in (0, h1]; a nonzero constant has none"""
    p = sp.Poly(expr, HS)
    if p.is_zero:
        return None
    while p.degree() > 0 and p.eval(0) == 0:
        p = sp.Poly(sp.quo(p.as_expr(), HS), HS)
    return 0 if p.degree() <= 0 else p.count_roots(0, h1)


def no_zero(F, k0, h1):
    """exact: F(kappa, h) != 0 for every kappa >= k0 and 0 < h <= h1 (F free of kappa: every 0 < h <= h1)"""
    if K not in F.free_symbols:
        return h_roots(F, h1) == 0
    FK = sp.Poly(F, K)
    crit = [FK.LC(), F.subs(K, k0)] + ([sp.discriminant(F, K)] if FK.degree() >= 2 else [])
    if any(h_roots(sp.expand(c), h1) != 0 for c in crit):
        return False
    at = sp.Poly(sp.expand(F.subs(HS, h1)), K)
    return not at.is_zero and at.count_roots(k0, None) == 0


def counts(P, x):
    """(roots right of Re lam = x, total) for a polynomial in lam with numeric coefficients"""
    P = sp.Poly(sp.expand(P), lam)
    return D.right_of(P.as_expr(), x), P.degree()


def h1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    hh = sp.Rational(1, 1000) if control == 1 else H1
    F = families()
    for nm, P, k0, want in (("scalar l >= 1", F["s"], 3, (3, 6)), ("vector", F["v"], 3, (1, 2)),
                            ("scalar 0", F["0"], 0, (2, 4))):
        ok = all(no_zero(Fi, k0, hh) for x in (-100, sp.Rational(19, 10)) for Fi in crossing(P, x))
        pt = P.subs(HS, H1).subs(K, k0) if K in P.free_symbols else P.subs(HS, H1)
        c1, n = counts(pt, sp.Rational(19, 10))
        c2, _ = counts(pt, -100)
        chk(f"{nm}: no crossing of Re lam = -100, 19/10 for kappa >= {k0}, 0 < h <= {hh}; at h_1 {c1} | "
            f"{c2 - c1} | {n - c2}", ok and (c1, n) == want and c2 == c1)
    return chk.ok


def h2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    hh = sp.Rational(1, 1000) if control == 1 else H1
    F = families()
    for nm, P, k0, want in (("scalar l >= 2", F["s"], 8, (3, 6)), ("vector", F["v"], 3, (1, 2))):
        ok = all(no_zero(Fi, k0, hh) for Fi in crossing(P, 2))
        c, n = counts(P.subs(HS, H1).subs(K, k0), 2)
        chk(f"{nm}: no crossing of Re lam = 2 for kappa >= {k0}, 0 < h <= {hh}; at h_1 {c} | 0 | {n - c}",
            ok and (c, n) == want)
    for nm, P, want in (("l = 1", F["s"].subs(K, 3), (2, 5)), ("l = 0", F["0"], (1, 3))):
        q, r = sp.div(sp.Poly(P, lam), sp.Poly(lam - 2, lam))
        cof = q.as_expr()
        ok = r.is_zero and all(no_zero(Fi, 0, hh) for Fi in crossing(cof, 2))
        c, n = counts(cof.subs(HS, H1), 2)
        chk(f"{nm}: lam - 2 divides for every h; the cofactor (degree {n}) has no crossing of Re lam = 2 and no root "
            f"at 2 for 0 < h <= {hh}; at h_1 {c} | 0 | {n - c}", ok and (c, n) == want)
    return chk.ok


CHECKS = [("H1 the strip [-100, 19/10] free for every h in (0, 10^-6], every type and l", h1),
          ("H2 [-100, 2] free but the Coulomb root 2 at l = 0, 1, simple, for every h in (0, 10^-6]", h2)]


def run(only=None, verbose=False):
    ok = True
    for k, (name, f) in enumerate(CHECKS, 1):
        if only and k != only:
            continue
        t0 = time.time()
        res = f(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    n = 1 if only else len(CHECKS)
    print(f"uniform5.py: {n if ok else 'not all'}/{n}")
    return ok


def mutants():
    caught = total = 0
    for name, f in CHECKS:
        total += 1
        res = f(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"uniform5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    vb = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=vb) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), vb) else 1)
    print(__doc__)
