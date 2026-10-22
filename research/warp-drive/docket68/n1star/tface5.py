#!/usr/bin/env python3
"""tface5.py -- the five-dimensional inputs of [Hin26a] Theorem B.1, the invertibility of the dilation-invariant model
of the constraint propagation operator on Minkowski space (the transition face problem), and the weights by which
[Hin26] Theorem 7.1(4) follows from it (N1STAR-PROOF.md section 10.23; ROUTES-OPEN.md 4.24; D69).  Labels: computed
(exact, sympy), deduced, READ.

[Hin26a] (arXiv:2606.27658v2) Appendix B, on R_t x R^3: box^C = 2 delta G (delta* + C_h) with c = r^-1 (dt - v dr)
is homogeneous of degree -2 under dilations ((B.2), (B.10)); its spectral family at sigma in e^(i[0, pi]) is a
scattering operator near infinity and a weighted b-operator near the origin r = 0 ((B.12)); Theorem B.1 makes it
invertible on H_sc,b^(s,(l, beta)) for -1/2 - h^-1 (1 - e)(1 + v) < l < -1/2 + h^-1 (1 - e)(1 - v) and beta in (1/2,
3/2 + C_0] ((B.13)), the density being r^2 |dr dg/|; its proof is Proposition B.2 (Fredholm, index 0, "also ... from
[Hin26b, Theorem 9.38]", that is [Hin26c]'s), Theorem B.4 (solvability on edge-b spaces for alpha_sf < -1/2 and
alpha_cf > 1/2, by the arguments of Theorem 5.2: positivity at cf "from (4.5) (with beta_K - beta_sf replaced by
alpha_cf - 1)", -(1/2) r^2 l(dr/r) positive definite, an energy estimate in tau = t/r, Proposition 5.11 at the sink),
and section B.4's choice l = -1/2, beta = 7/2, alpha_sf = -5/2, alpha_cf = 5/2, C_0 >= 2.  [Hin26] Theorem 7.1(4)
(tf-admissibility for every weight beta in [-C_0, 1)) follows from it with beta' := -beta + 3/2 - eps, "the shift by
3/2 in the weights being due to the weight rho^-3 of this density" (p. 137).

  F1 (computed, exact) The dilation structure in five dimensions: on 4+1 Minkowski in t* = t - r, the coefficient of
     every k-th order derivative in box^C, at the trace weight 2/3, is homogeneous of degree k - 2 in x -- checked on
     every term, d_t* counted as a derivative, with r an independent symbol and d_i = d/dx_i + (x_i/r) d/dr -- so box^C
     is dilation invariant of degree -2, (B.10).  Deduced from it: every term of r^2 box^C(sigma) carrying sigma
     carries a positive power of r, so at r = 0 it is r^2 box^C(0), (B.12), whose indicial roots in r are minus those in
     rho = 1/r.  Four-dimensional control: weight 1.  Control: c = r^-1 dt - v dr, not homogeneous.
  F2 (computed, exact) The beta-range at the origin: r^mu lies in r^beta L^2(r^(n-1) dr) near r = 0 iff mu > beta -
     n/2; the rho-roots at infinity avoid [-C_0, n - 2) -- 10.12's Proposition 10.9 at n = 4 (C_0 <= 100), his Theorem
     4.9 at n = 3, the top n - 2 the Coulomb root, typed from there -- so the r-roots avoid (-(n - 2), C_0] and the
     weights at the origin are beta in (n/2 - (n - 2), n/2 + C_0]: (0, 2 + C_0] in five dimensions.  Four-dimensional
     control: his (1/2, 3/2 + C_0].  Control: his range claimed in five dimensions.
  F3 (computed, exact) Theorem B.4's thresholds in five dimensions at (v, e) = (1/2, 1/102400): at cf, dw/w = (alpha_cf -
     1) dr/r (his "beta_K - beta_sf replaced by alpha_cf - 1"), so r^2 (-l(dw/w) + S) is cform5.py's T at rho_K = 0 with
     d = b_sf - b_K = 1 - alpha_cf: positive definite at alpha_cf = 5/2, and on either side of the threshold alpha_cf =
     1 - b* (b* = 0.99340731..., the root of cform5.py C7's q(d, 0)) positive at d = 0.9934 and not at d = 0.9935; at
     the sink, alpha_sf < b* - 1 (10.22).  And -(1/2) r^2 l(dr/r) has characteristic polynomial (lam - v)^(n-1) (lam^2 -
     (3 - e) v lam + (2 - e) v^2 - e), his matrix [[v, -1], [-e, (2 - e) v]] with n - 1 copies of v, with positive
     eigenvalues at this point and at e = 0 -- positive definite with respect to his Lemma 3.3's fiber inner product,
     as he concludes from the eigenvalues (READ, p. 96; deduced in five dimensions).  Four-dimensional control: the
     same with two copies.  Control: alpha_cf = 0.
  F4 (computed, exact) Section B.4 and [Hin26] Theorem 7.1(4) in five dimensions: (alpha_sf, alpha_cf) = (-5/2, 5/2)
     meets F3's thresholds; the closing integral int_1^oo t^(2 (alpha_sf + alpha_cf)) dt, from rho_sf = 1/t, rho_cf =
     r/t and the density |dt dx|, diverges; l = -1/2 lies inside the l-window for every h > 0 and 0 < v, e < 1; beta =
     7/2 lies in F2's range iff C_0 >= 7/2 - n/2 = 3/2 (his C_0 >= 2); the data obey (B.33): |dg| = r^n |dt (dr/r) dg/|
     is r times X's r^(n-1) |dr dg/| in (tau = t/r, r) -- the one time direction, whatever n -- so the traces lie in
     rho_sf^(alpha_sf + 1/2) rho_cf^(alpha_cf - 1/2) L^2, and l - 1 >= alpha_sf + 1/2, beta >= alpha_cf - 1/2 (the l - 1
     of his sc-to-b inclusion READ); a kernel element of size rho^((n - 1)/2 + S-bar - eps) lies in rho^l L^2(r^(n-1)
     dr) iff l < -1/2 + S-bar - eps, the -1/2 dimension-free; and beta' = -beta + n/2 - eps lies in F2's range iff beta
     in [-C_0, n - 2) as eps -> 0: tf-admissibility for every beta in [-C_0, 2) in five dimensions, his [-C_0, 1).
     Four-dimensional control: his numbers.  Control: alpha_cf = -alpha_sf - 1, where the closing integral converges.

Deduced, not computed here: with 10.21's K1-K2 (S-bar^C, the l-window) and F1-F4, the inputs of [Hin26a] Appendix B are
in hand in five dimensions; on the readings of 10.19-10.20 ([Hin26c] section 9, Theorem 9.38 at n = 4) and of 10.22
(his 3b-analysis, here its edge-b version), Proposition B.2, Theorem B.4 and Theorem B.1 hold on 4+1 Minkowski with
beta in (0, 2 + C_0], for C_0 <= 100 (Proposition 10.9's range), at (v, e) = (1/2, 1/102400) and h = 10^-6 if that
lies below the h_0 of Theorems B.4 and 5.2 (not explicit), and [Hin26] Theorem 7.1(4) with every beta in [-C_0, 2).

READ.  [Hin26a] pp. 85-88 (Appendix B: (B.1)-(B.17), Theorem B.1, Proposition B.2 and its proof's start), 93-94
(Theorem B.4 with (B.31)-(B.33), the energy estimate (B.34)-(B.37)), 96-98 (the cf positivity, (B.38)-(B.41), the
eigenvalues of -(1/2) r^2 l(dr/r) "and thus positive definite (with respect to the fiber inner product from Lemma 3.3)",
the remark on Proposition 5.11, section B.4: (B.42)-(B.45) and the closing integral); [Hin26] pp. 136-137
(Theorem 7.1 and its proof of part (4)); alphaXiv, 2026-10-22.

sympy.  python3 tface5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

import cform5 as CF
import semiclass5 as SC
from damping5 import Checklist

D = sp.diff
v, e, h, lam = sp.symbols("v e h lam", positive=True)


def box_c(n, m, cfar=True):
    """2 delta G (delta* + C) on 1-forms of (n+1)-Minkowski, Cartesian frame, (t*, x), r an independent symbol"""
    Tt = sp.Symbol("T")
    x = sp.symbols("x1:%d" % (n + 1), real=True)
    r = sp.Symbol("r", positive=True)
    N = n + 1
    eta = sp.diag(-1, *([1]*n))
    W = [sp.Function("W%d" % a)(Tt, *x) for a in range(N)]

    def d(fn, mu_):
        if mu_ == 0:
            return D(fn, Tt)
        i = mu_ - 1
        return D(fn, x[i]) + x[i]/r*D(fn, r) - x[i]/r*D(fn, Tt)

    c = ([1/r] + [-v*xi/r**2 for xi in x]) if cfar else ([1/r] + [-v*xi/r for xi in x])
    cw = sum(eta[a, a]*c[a]*W[a] for a in range(N))
    S = sp.Matrix(N, N, lambda a, b: (d(W[b], a) + d(W[a], b))/2 + (c[a]*W[b] + c[b]*W[a] - m*(1 - e)*eta[a, b]*cw)/h)
    trS = sum(eta[a, a]*S[a, a] for a in range(N))
    Gh = S - eta*trS/2
    P = [sp.expand(-2*sum(eta[k, k]*d(Gh[a, k], k) for k in range(N))) for a in range(N)]
    return P, W, x, r


def terms(P, W):
    """{(a, dep): coefficient}, dep a W or one of its derivatives"""
    out = {}
    for a, Pa in enumerate(P):
        for t in sp.Add.make_args(Pa):
            deps = [f for f in t.atoms(sp.Derivative, sp.Function) if f.func in [w.func for w in W] or
                    (isinstance(f, sp.Derivative) and f.expr in W)]
            deps = [f for f in deps if not any(f != g and f in g.atoms(sp.Function) and isinstance(g, sp.Derivative)
                                               for g in deps)]
            dep = [f for f in deps if isinstance(f, sp.Derivative)] or deps
            assert len(dep) == 1, t
            out[(a, dep[0])] = out.get((a, dep[0]), 0) + t/dep[0]
    return out


def order(dep):
    return sum(cnt for _, cnt in dep.variable_count) if isinstance(dep, sp.Derivative) else 0


# ------------------------------------------------------------------------------------------------- F1
def f1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        P, W, x, r = box_c(n, sp.Rational(2, n - 1), cfar=control != 1)
        tm = terms(P, W)
        scl = {**{xi: lam*xi for xi in x}, r: lam*r}
        bad = [k for k, cf in tm.items() if sp.cancel(cf.subs(scl, simultaneous=True) - lam**(order(k[1]) - 2)*cf) != 0]
        nT = sum(1 for (a, dep) in tm if isinstance(dep, sp.Derivative) and sp.Symbol("T") in dep.variables)
        chk(f"n + 1 = {n + 1}: {len(tm)} terms ({nT} with d_t*), the coefficient of each k-th order derivative "
            f"homogeneous of degree k - 2{'' if not bad else ' (fails at %d)' % len(bad)}", not bad and nT > 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- F2
def origin_range(n, C0):
    mu_, be = sp.symbols("mu beta", real=True)
    thr = sp.solve(sp.Eq(2*(mu_ - be) + n - 1, -1), mu_)[0]            # r^(2(mu - beta)) r^(n-1) dr near 0
    shift = sp.simplify(be - thr)
    top = n - 2                                    # the Coulomb root: 10.12 (n = 4), his Theorem 4.9 (n = 3), typed
    # r-roots mu = -lam avoid (-top, C0]; Fredholm at the origin iff beta - shift avoids them: beta - shift in (-top, C0]
    return shift - top, shift + C0, shift


def f2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    C0 = sp.Symbol("C_0", positive=True)
    for n in ((4,) if control else (4, 3)):
        lo, hi, shift = origin_range(n, C0)
        want = {4: (0, 2 + C0), 3: (sp.Rational(1, 2), sp.Rational(3, 2) + C0)}[n]
        if control == 1:
            want = (sp.Rational(1, 2), sp.Rational(3, 2) + C0)                  # control: his range in five dimensions
        chk(f"n + 1 = {n + 1}: r^mu in r^beta L^2(r^{n - 1} dr) near 0 iff mu > beta - {shift}; beta in ({lo}, {hi}]",
            sp.simplify(lo - want[0]) == 0 and sp.simplify(hi - want[1]) == 0 and shift == sp.Rational(n, 2))
    return chk.ok


# ------------------------------------------------------------------------------------------------- F3
def bstar():
    d = sp.Symbol("d")
    q0 = sp.Poly(204795*d**2 - 409605*d + 204801, d)                       # cform5.py C7's q(d, 0)
    return [z for z in sp.real_roots(q0) if z < 1][0], q0


def f3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    Tm, _ = CF.sf_symbol()
    bk, bs, rk = SC.bk, SC.bs, SC.rk
    acf = sp.Symbol("alpha_cf", real=True)
    lm = sp.Symbol("lm")
    def posdef(d_):                                                       # T at rho_K = 0, d = b_sf - b_K
        T0 = Tm.subs(rk, 0).subs({bs: d_, bk: 0})
        return sp.Poly((T0 - lm*sp.eye(5)).det(), lm).count_roots(None, 0) == 0

    a_cf = sp.Rational(5, 2) if control != 1 else sp.Integer(0)
    pos = posdef(1 - a_cf)                                                 # d = 1 - alpha_cf
    b_star, q0 = bstar()
    d_lo, d_hi = sp.Rational(9934, 10000), sp.Rational(9935, 10000)
    thr_ok = q0.count_roots(d_lo, d_hi) == 1 and posdef(d_lo) and not posdef(d_hi)
    if control == 1:
        chk("at alpha_cf = 0 T at cf is positive definite", pos)
        return chk.ok
    chk(f"at cf T = r^2 (-l(dw/w) + S) with d = 1 - alpha_cf is positive definite at alpha_cf = 5/2; the threshold "
        f"alpha_cf > 1 - b* = {sp.N(1 - b_star, 6)}: positive at d = {d_lo}, not at d = {d_hi}", pos and thr_ok)
    for n in (4, 3):
        R = sp.Symbol("R", positive=True)
        cvec = sp.Matrix([1/R, -v/R] + [0]*(n - 1))
        zeta = sp.Matrix([0, 1/R] + [0]*(n - 1))
        Mx = (-R**2*SC.ell(n, cvec, zeta, e)/2).applyfunc(sp.simplify)
        cpx = sp.factor((Mx - lm*sp.eye(n + 1)).det())
        want = (lm - v)**(n - 1)*(lm**2 - (3 - e)*v*lm + (2 - e)*v**2 - e)
        same = sp.expand(cpx - want) == 0 or sp.expand(cpx + want) == 0
        at_pt = sp.Poly(want.subs({v: sp.Rational(1, 2), e: sp.Rational(1, 102400)}), lm).count_roots(None, 0) == 0
        at_e0 = all(z.is_positive for z in sp.solve(want.subs(e, 0), lm))         # roots v, 2v for every v > 0
        chk(f"n + 1 = {n + 1}: -(1/2) r^2 l(dr/r) has characteristic polynomial (lam - v)^{n - 1} (lam^2 - (3 - e) v "
            f"lam + (2 - e) v^2 - e); positive eigenvalues at (1/2, 1/102400) and at e = 0", same and at_pt and at_e0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- F4
def f4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    C0, eps, Sb = sp.symbols("C_0 epsilon Sbar", positive=True)
    p_, q_ = sp.symbols("p q", positive=True)
    b_star, _ = bstar()
    for n in ((4,) if control else (4, 3)):
        a_sf, a_cf = -sp.Rational(5, 2), sp.Rational(5, 2)
        if control == 1:
            a_cf = -a_sf - 1
        l_, be = -sp.Rational(1, 2), sp.Rational(7, 2)
        half = sp.Rational(1, 2)
        thr = (a_sf < b_star - 1) and (a_cf > 1 - b_star) if n == 4 else (a_sf < -half and a_cf > half)
        tt, rr, tau = sp.symbols("t r tau", positive=True)
        # rho_sf = 1/t, rho_cf = r/t in t >= 1, r <= t, at a fixed r
        integrand = sp.powsimp(((1/tt)**(-2*a_sf)*(rr/tt)**(-2*a_cf)).subs(rr, 1), force=True)
        closing = sp.integrate(integrand, (tt, 1, sp.oo)) == sp.oo                              # density |dt dx|
        J = sp.Matrix([tau*rr, rr]).jacobian([tau, rr]).det()                                  # t = tau r
        # |dg| = r^n |dt dr/r dg/| over X's r^(n-1) |dr dg/|, in (tau, r)
        k_ = sp.degree(sp.simplify(rr**n/rr*J/rr**(n - 1)), rr)
        # the traces lie in r^(-k/2) rho^alpha L^2, with rho_sf = 1/r and rho_cf = r on X
        sh_sf, sh_cf = sp.Rational(k_, 2), -sp.Rational(k_, 2)
        sub = {v: 1/(1 + p_), e: 1/(1 + q_)}
        lo_w = -sp.Rational(1, 2) - (1 - e)*(1 + v)/h
        hi_w = -sp.Rational(1, 2) + (1 - e)*(1 - v)/h
        in_win = sp.factor((l_ - lo_w).subs(sub)).is_positive and sp.factor((hi_w - l_).subs(sub)).is_positive
        lo, hi, shift = origin_range(n, C0)
        c0_min = sp.solve(sp.Eq(be, hi), C0)[0]
        data = k_ == 1 and (l_ - 1 >= a_sf + sh_sf) and (be >= a_cf + sh_cf)
        aa = sp.Symbol("aa")
        lmax = sp.solve(sp.Eq(2*((sp.Rational(n - 1, 2) + Sb - eps) - aa) - n - 1, -1), aa)[0]  # rho^k in rho^l L^2
        dimfree = sp.simplify(lmax - (-sp.Rational(1, 2) + Sb - eps)) == 0
        b_ = sp.Symbol("b", real=True)
        bp = -b_ + shift - eps
        tf_lo = sp.solve(sp.Eq(bp, hi), b_)[0].subs(eps, 0)                # beta' <= hi  <=>  beta >= -C0 - eps
        tf_hi = sp.solve(sp.Eq(bp, lo), b_)[0].subs(eps, 0)                # beta' > lo   <=>  beta < (n - 2) - eps
        want_c0 = {4: sp.Rational(3, 2), 3: 2}[n]
        chk(f"n + 1 = {n + 1}: (alpha_sf, alpha_cf) = ({a_sf}, {a_cf}) above the thresholds, int_1^oo {integrand} dt "
            f"diverges; l = -1/2 in the l-window; beta = 7/2 in the origin range iff C_0 >= {c0_min}; data in (B.33), "
            f"shifts ({sh_sf}, {sh_cf}); l < -1/2 + S-bar - eps dimension-free; tf weights beta in [{tf_lo}, {tf_hi})",
            bool(thr) and closing and bool(in_win) and c0_min == want_c0 and data and dimfree
            and sp.simplify(tf_lo + C0) == 0 and tf_hi == n - 2)
    return chk.ok


CHECKS = [("F1 box^C on 4+1 Minkowski dilation invariant of degree -2, d_t* counted: (B.10)", f1, 1),
          ("F2 the beta-range at the origin in five dimensions: (0, 2 + C_0], his (1/2, 3/2 + C_0]", f2, 1),
          ("F3 Theorem B.4's thresholds: alpha_cf > 1 - b* at cf; -(1/2) r^2 l(dr/r) has positive eigenvalues", f3, 1),
          ("F4 section B.4's choice and Theorem 7.1(4)'s weights in five dimensions: beta in [-C_0, 2)", f4, 1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<112} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"tface5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"tface5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
