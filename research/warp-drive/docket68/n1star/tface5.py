#!/usr/bin/env python3
"""tface5.py -- the five-dimensional inputs of [Hin26a] Theorem B.1, the invertibility of the dilation-invariant model
of the constraint propagation operator on Minkowski space (the transition face problem), and the weights by which
[Hin26] Theorem 7.1(4) follows from it (N1STAR-PROOF.md section 10.23; ROUTES-OPEN.md 4.24; D69, D71).  Labels: computed
(exact, sympy), deduced, READ.

[Hin26a] (arXiv:2606.27658v2) Appendix B, on R_t x R^3: box^C = 2 delta G (delta* + C_h) with c = r^-1 (dt - v dr) is
homogeneous of degree -2 under dilations ((B.2), (B.10)); its spectral family at sigma in e^(i[0, pi]) is a scattering
operator near infinity and a weighted b-operator near the origin r = 0 ((B.12)); Theorem B.1 makes it invertible on
H_sc,b^(s,(l, beta)) for -1/2 - h^-1 (1 - e)(1 + v) < l < -1/2 + h^-1 (1 - e)(1 - v) and beta in (1/2, 3/2 + C_0]
((B.13)), the density being r^2 |dr dg/|; its proof is Proposition B.2 (Fredholm, index 0, "also ... from [Hin26b,
Theorem 9.38]", that is [Hin26c]'s), Theorem B.4 (solvability on edge-b spaces for alpha_sf < -1/2 and alpha_cf > 1/2,
by the arguments of Theorem 5.2: positivity at cf "from (4.5) (with beta_K - beta_sf replaced by alpha_cf - 1)", -(1/2)
r^2 l(dr/r) "is thus positive definite", an energy estimate in tau = t/r, Proposition 5.11 at the sink), and section
B.4's choice l = -1/2, beta = 7/2, alpha_sf = -5/2, alpha_cf = 5/2, C_0 >= 2.  [Hin26] Theorem 7.1(4) (tf-admissibility
for every weight beta in [-C_0, 1)) follows from it with beta' := -beta + 3/2 - eps, "the shift by 3/2 in the weights
being due to the weight rho^-3 of this density" (p. 137).

  F1 (computed, exact) The dilation structure in five dimensions: on 4+1 Minkowski in t* = t - r, the coefficient of
     every k-th order derivative in box^C, at the trace weight 2/3, is homogeneous of degree k - 2 in x -- checked on
     every term, d_t* counted as a derivative, with r an independent symbol and d_i = d/dx_i + (x_i/r) d/dr -- so box^C
     is dilation invariant of degree -2, (B.10).  Deduced from it: every term of r^2 box^C(sigma) carrying sigma
     carries a positive power of r, so at r = 0 it is r^2 box^C(0), (B.12), whose indicial roots in r are minus those in
     rho = 1/r.  Four-dimensional control: weight 1.  Control: c = r^-1 dt - v dr, not homogeneous.
  F2 (computed, exact; what follows "so" is deduced) The beta-range at the origin: r^mu lies in r^beta L^2(r^(n-1) dr)
     near r = 0 iff mu > beta - n/2; the rho-roots at infinity avoid [-C_0, n - 2) -- 10.12's Proposition 10.9 at n = 4
     (C_0 <= 100), his Theorem 4.9 at n = 3, the top n - 2 the Coulomb root, typed from there -- so the r-roots avoid
     (-(n - 2), C_0] and the b-Fredholm weights at the origin are beta in (n/2 - (n - 2), n/2 + C_0]: (0, 2 + C_0] in
     five dimensions.  Four-dimensional control: his (1/2, 3/2 + C_0].  Control: his range claimed in five dimensions.
  F3 (computed, exact; what follows "so" is deduced) Theorem B.4's thresholds in five dimensions at (v, e) = (1/2,
     1/102400): at cf, dw/w = (alpha_cf - 1) dr/r (his "beta_K - beta_sf replaced by alpha_cf - 1"), so r^2 (-l(dw/w) +
     S) is T at rho_K = 0 with d = b_sf - b_K = 1 - alpha_cf, built here from semiclass5.py for any n and equal at n = 4
     to cform5.py's: det T(d) = c (2 - d)^3 q(d, 0), with q(d, 0) = 204795 d^2 - 409605 d + 204801 derived (C7's), and
     an eigenvalue first reaches 0 at d = b* = 0.99340731..., the smaller root of q(d, 0); T is positive definite at
     alpha_cf = 5/2 and at d = 0.9934, not at d = 0.9935 -- so the threshold alpha_cf > 1 - b*; as e -> 0 (B is singular
     at e = 0: e symbolic, then the limit) its eigenvalues are 2 - d (three times), 1 - d and 2 - 2 d, the threshold d <
     1 of 10.13 (W3); at the sink, alpha_sf < b* - 1 (10.22).  And -(1/2) r^2 l(dr/r) has characteristic polynomial
     (lam - v)^(n-1) (lam^2 - (3 - e) v lam + (2 - e) v^2 - e), his matrix [[v, -1], [-e, (2 - e) v]] with n - 1 copies
     of v, with positive eigenvalues at this point and at e = 0 -- "and is thus positive definite (with respect to the
     fiber inner product from Lemma 3.3)", he concludes from the eigenvalues (READ, p. 96; deduced in five dimensions).
     Four-dimensional control, computed: as e -> 0 the eigenvalues 1 - 2 d, 1/2 - d and 3/2 - d (twice), so d < 1/2, his
     alpha_cf > 1/2 ((4.7)); at e = 1/102400 the first zero at d = 0.4956; and the matrix with two copies of v.
     Controls: alpha_cf = 0; the characteristic polynomial with n - 2 copies of v.
  F4 (computed, exact; what follows "so" is deduced) Section B.4 and the weights of [Hin26] Theorem 7.1(4) in five
     dimensions: (alpha_sf, alpha_cf) = (-5/2, 5/2) meets F3's computed thresholds (in four dimensions too, at d* =
     0.4956); the closing integral int_1^oo t^(2 (alpha_sf + alpha_cf)) dt, from rho_sf = 1/t, rho_cf = r/t and the
     density |dt dx|, diverges; l = -1/2 lies inside the l-window for every h > 0 and 0 < v, e < 1; beta = 7/2 lies in
     F2's range iff C_0 >= 7/2 - n/2 = 3/2 (his C_0 >= 2); the data obey (B.33): |dg| = r^n |dt (dr/r) dg/| is r times
     X's r^(n-1) |dr dg/| in (tau = t/r, r) -- the one time direction, whatever n -- so the traces lie in
     rho_sf^(alpha_sf + 1/2) rho_cf^(alpha_cf - 1/2) L^2, and l - 1 >= alpha_sf + 1/2, beta >= alpha_cf - 1/2 (the l - 1
     of his sc-to-b inclusion READ); a kernel element of size rho^((n - 1)/2 + S-bar - eps) lies in rho^l L^2(r^(n-1)
     dr) iff l < -1/2 + S-bar - eps, the -1/2 dimension-free; the adjoint half: an element of the adjoint kernel of size
     rho^((n - 1)/2 + S_in - eps) at R_in, S_in = h^-1 (1 - e)(1 + v) the bottom of spec (A_w + S-bar^C) (10.21 K2,
     typed from there), lies in rho^(-l-1) L^2 iff l > -1/2 - S_in + eps, the l-window's lower end; and beta' = -beta +
     n/2 - eps lies in F2's range for every sufficiently small eps > 0 iff beta in [-C_0, n - 2) (the endpoints tested
     with symbolic eps and delta: -C_0 in, -C_0 - delta out, n - 2 out, n - 2 - delta in) -- so the weights of
     tf-admissibility are [-C_0, 2) in five dimensions, his [-C_0, 1) (10.23(e)).  Four-dimensional control: his
     numbers.  Controls: alpha_cf = -alpha_sf - 1, where the closing integral converges; his top 1 claimed in five
     dimensions.
  F5 (computed, exact; what follows "so" is deduced) Proposition B.2's index 0 in five dimensions, his relative index
     argument (p. 91): the free 1-form wave operator 2 delta G delta* (gaugepot5.py's box at gamma = 0) has at the
     origin the r-roots, minus its rho-roots at infinity, -3, -2 | 0, 1 at l = 0, -l - 3, -l - 2, -l - 1 | l - 1, l, l +
     1 for scalar type l >= 1 and -l - 2 | l for vector type, so the window of beta - 2 between the two groups contains
     (-2, 0), where the free operator is invertible ([Hin26c] Proposition 9.40 at n = 4, 10.20), and rising into it from
     below crosses 2, 3 and 1 roots -- as many as the damped operator's roots with real part >= 2 at Proposition 10.9's
     point that his argument crosses the other way (10.12's counts, typed from there).  Four-dimensional control: his
     -l - 2, -l - 1, -l | l - 1, l, l + 1 and window (-l, l - 1) for beta - 3/2, with his Theorem 4.9(3)'s counts.
     Control: his window claimed in five dimensions.

Deduced, not computed here: with 10.21's K1-K2 (S-bar^C, the radial sets, the l-window) and F1-F5, the inputs of
[Hin26a] Appendix B are in hand in five dimensions; on the readings of 10.19-10.20 ([Hin26c] section 9, Theorem 9.38 at
n = 4) and of 10.22 (his 3b-analysis, here its edge-b version), Proposition B.2 (Fredholm, and of index 0 by F5),
Theorem B.4 and Theorem B.1 hold on 4+1 Minkowski with beta in (0, 2 + C_0], for C_0 <= 100 (Proposition 10.9's range),
at (v, e) = (1/2, 1/102400) and h = 10^-6 if that lies below the h_0 of Theorems B.4 and 5.2 (not explicit), and [Hin26]
Theorem 7.1(4), both halves of tf-admissibility, with every beta in [-C_0, 2).

READ.  [Hin26a] pp. 85-91 (Appendix B: (B.1)-(B.17), Theorem B.1, Proposition B.2 and its proof -- the beta-range from
Theorem 4.9 on p. 89, the radial thresholds, the index 0 on p. 91), 93-94 (Theorem B.4 with (B.31)-(B.33), the energy
estimate (B.34)-(B.37)), 96-98 (the cf positivity, (B.38)-(B.41), the eigenvalues of -(1/2) r^2 l(dr/r), the remark on
Proposition 5.11, section B.4: (B.42)-(B.45) and the closing integral); [Hin26] pp. 136-137 (Theorem 7.1 and its proof
of part (4), both halves); alphaXiv, 2026-10-22 and 2026-10-23.  [Hin26c] Definition 5.10 (p. 104) and Theorem 9.38(5)
(p. 195), as the thirty-first verifier read at source.

sympy.  python3 tface5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

import cform5 as CF
import gaugepot5 as GP
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
HALF = sp.Rational(1, 2)
E5 = sp.Rational(1, 102400)
_T = {}


def sf_T(n, e_=E5):
    """T = r^2 (-l(dw/w) + S) on sf, as cform5.py's sf_symbol but for any n and e, at v = 1/2"""
    if (n, e_) not in _T:
        S, _ = SC.S_matrix(n, SC.c_far(n), e_, SC.at_radius(n, SC.T))
        cvec = sp.Matrix([1/SC.R, -SC.v/SC.R] + [0]*(n - 1))
        zeta = sp.Matrix([-SC.rk*SC.bk/SC.R, -(SC.bs - SC.bk)/SC.R] + [0]*(n - 1))
        _T[(n, e_)] = (SC.R**2*(-SC.ell(n, cvec, zeta, e_) + S)).applyfunc(sp.cancel).subs(SC.v, HALF).applyfunc(
            sp.cancel)
    return _T[(n, e_)]


def T_cf(n, d_, e_=E5):
    """T at cf: rho_K = 0, d = b_sf - b_K = 1 - alpha_cf"""
    return sf_T(n, e_).subs(SC.rk, 0).subs({SC.bs: d_, SC.bk: 0})


def posdef(M):
    """all eigenvalues real and positive (exact: the real roots of the characteristic polynomial, with multiplicity)"""
    lm = sp.Symbol("lm")
    P = sp.Poly((M - lm*sp.eye(M.shape[0])).det(), lm)
    rts = sp.real_roots(P)
    return len(rts) == P.degree() and all(z > 0 for z in rts)


def threshold(n):
    """the first d at which an eigenvalue of T at cf reaches 0, at e = 1/102400: the least real root of det T(d)"""
    d = sp.Symbol("d")
    P = sp.Poly(sp.cancel(T_cf(n, d).det()), d)
    return min(sp.real_roots(P)), P


def eigen_e0(n):
    """the eigenvalues of T at cf as e -> 0 (B is singular at e = 0, so e is kept symbolic and the limit taken)"""
    es, d, lm = sp.symbols("e_s d lm", positive=True)
    cp = sp.factor(sp.limit(sp.cancel((T_cf(n, d, es) - lm*sp.eye(n + 1)).det()), es, 0))
    return sp.roots(sp.Poly(cp, lm)), d


def bstar():
    b, P = threshold(4)
    d = P.gens[0]
    q0 = sp.Poly(sp.cancel(P.as_expr()/(2 - d)**3), d)
    q0 = sp.Poly(q0.as_expr()*204795/q0.LC(), d)                          # normalised to C7's leading coefficient
    return b, q0


def f3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    lm = sp.Symbol("lm")
    a_cf = sp.Rational(5, 2) if control != 1 else sp.Integer(0)
    if control == 1:
        chk("at alpha_cf = 0 T at cf is positive definite", posdef(T_cf(4, 1 - a_cf)))
        return chk.ok
    if control != 2:
        same = sp.simplify(sf_T(4) - CF.sf_symbol()[0]) == sp.zeros(5, 5)
        b_star, q0 = bstar()
        d = q0.gens[0]
        q0_ok = sp.expand(q0.as_expr() - (204795*d**2 - 409605*d + 204801)) == 0
        d_lo, d_hi = sp.Rational(9934, 10000), sp.Rational(9935, 10000)
        thr_ok = d_lo < b_star < d_hi and posdef(T_cf(4, d_lo)) and not posdef(T_cf(4, d_hi))
        pos = posdef(T_cf(4, 1 - a_cf))
        chk(f"n + 1 = 5: T as cform5.py's; det T(d) = c (2 - d)^3 q(d, 0), q(d, 0) = 204795 d^2 - 409605 d + 204801 "
            f"(C7's); first zero eigenvalue at d = b* = {sp.N(b_star, 9)}, the smaller root; positive definite at "
            f"alpha_cf = 5/2 and at d = 0.9934, not at d = 0.9935: alpha_cf > 1 - b* = {sp.N(1 - b_star, 6)}",
            same and q0_ok and thr_ok and pos)
        ev5, d5 = eigen_e0(4)
        lim5 = min(sp.solve(z, d5)[0] for z in ev5)                       # an eigenvalue reaches 0 first at d = 1
        chk(f"n + 1 = 5: as e -> 0 the eigenvalues of T at cf are {sorted(ev5.items(), key=str)}: threshold d < "
            f"{lim5}, 10.13's (W3)", lim5 == 1)
        b4, _ = threshold(3)
        pos4 = posdef(T_cf(3, 1 - a_cf))
        ev4, d4 = eigen_e0(3)
        lim4 = min(sp.solve(z, d4)[0] for z in ev4)
        chk(f"n + 1 = 4 (control, computed): as e -> 0 the eigenvalues are {sorted(ev4.items(), key=str)}, threshold d "
            f"< {lim4}, his alpha_cf > 1/2 ((4.7)); at e = 1/102400 the first zero is at d = {sp.N(b4, 6)}; positive "
            f"definite at alpha_cf = 5/2", lim4 == HALF and b4 < HALF and pos4)
    for n in (4, 3):
        R = sp.Symbol("R", positive=True)
        cvec = sp.Matrix([1/R, -v/R] + [0]*(n - 1))
        zeta = sp.Matrix([0, 1/R] + [0]*(n - 1))
        Mx = (-R**2*SC.ell(n, cvec, zeta, e)/2).applyfunc(sp.simplify)
        cpx = sp.factor((Mx - lm*sp.eye(n + 1)).det())
        copies = (n - 1) if control != 2 else (n - 2)                     # control 2: one copy of v too few
        want = (lm - v)**copies*(lm**2 - (3 - e)*v*lm + (2 - e)*v**2 - e)
        same = sp.expand(cpx - want) == 0 or sp.expand(cpx + want) == 0
        at_pt = sp.Poly(want.subs({v: HALF, e: E5}), lm).count_roots(None, 0) == 0
        at_e0 = all(z.is_positive for z in sp.solve(want.subs(e, 0), lm))         # roots v, 2v for every v > 0
        chk(f"n + 1 = {n + 1}: -(1/2) r^2 l(dr/r) has characteristic polynomial (lam - v)^{copies} (lam^2 - (3 - e) v "
            f"lam + (2 - e) v^2 - e); positive eigenvalues at (1/2, 1/102400) and at e = 0", same and at_pt and at_e0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- F4
def f4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    C0, eps, Sb, dl = sp.symbols("C_0 epsilon Sbar delta", positive=True)
    p_, q_ = sp.symbols("p q", positive=True)
    for n in ((4,) if control else (4, 3)):
        dstar, _ = threshold(n)
        a_sf, a_cf = -sp.Rational(5, 2), sp.Rational(5, 2)
        if control == 1:
            a_cf = -a_sf - 1
        l_, be = -HALF, sp.Rational(7, 2)
        thr = (a_sf < dstar - 1) and (a_cf > 1 - dstar)                   # b_sf < d*, b_K - b_sf > -d*
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
        lo_w = -HALF - (1 - e)*(1 + v)/h
        hi_w = -HALF + (1 - e)*(1 - v)/h
        in_win = sp.factor((l_ - lo_w).subs(sub)).is_positive and sp.factor((hi_w - l_).subs(sub)).is_positive
        lo, hi, shift = origin_range(n, C0)
        c0_min = sp.solve(sp.Eq(be, hi), C0)[0]
        data = k_ == 1 and (l_ - 1 >= a_sf + sh_sf) and (be >= a_cf + sh_cf)
        aa = sp.Symbol("aa")
        lmax = sp.solve(sp.Eq(2*((sp.Rational(n - 1, 2) + Sb - eps) - aa) - n - 1, -1), aa)[0]  # rho^k in rho^l L^2
        dimfree = sp.simplify(lmax - (-HALF + Sb - eps)) == 0
        # the adjoint half: decay (n - 1)/2 + S_in - eps at R_in, S_in the bottom of spec(A_w + S-bar^C) (10.21 K2)
        S_in = (1 - e)*(1 + v)/h
        lmax_in = lmax.subs(Sb, S_in)                                          # rho^(-l-1) needs -l - 1 < lmax_in
        adj = sp.simplify((-1 - lmax_in.subs(eps, 0)) - lo_w) == 0             # -l - 1 < ... iff l > lo_w (+ eps)
        # the tf weights: beta' = -beta + n/2 - eps in (lo, hi] for every sufficiently small eps > 0
        b_ = sp.Symbol("b", real=True)
        bp = -b_ + shift - eps
        top = (n - 2) if control != 2 else 1                                    # control 2: his top 1 claimed
        ends = (sp.simplify((bp - hi).subs(b_, -C0)) == -eps                    # -C_0 in for every eps
                and sp.simplify((bp - hi).subs(b_, -C0 - dl)) == dl - eps        # -C_0 - delta out once eps < delta
                and sp.simplify((bp - lo).subs(b_, top)) == -eps + (n - 2 - top)  # the top out for every eps (iff n-2)
                and sp.simplify((bp - lo).subs(b_, top - dl)) == dl - eps + (n - 2 - top))
        ends = ends and top == n - 2
        want_c0 = {4: sp.Rational(3, 2), 3: 2}[n]
        chk(f"n + 1 = {n + 1}: (alpha_sf, alpha_cf) = ({a_sf}, {a_cf}) above the computed thresholds (d* = "
            f"{sp.N(dstar, 6)}), int_1^oo {integrand} dt diverges; l = -1/2 in the l-window; beta = 7/2 in the origin "
            f"range iff C_0 >= {c0_min}; data in (B.33), shifts ({sh_sf}, {sh_cf}); l < -1/2 + S-bar - eps "
            f"dimension-free; the adjoint's R_in threshold the l-window's lower end; for every small eps tf weights "
            f"beta in [-C_0, {top})",
            bool(thr) and closing and bool(in_win) and c0_min == want_c0 and data and dimfree and adj and ends)
    return chk.ok


# ------------------------------------------------------------------------------------------------- F5
def f5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    lam_, L_ = GP.lam, GP.L
    for n in ((4,) if control else (4, 3)):
        s0, sl, vl = [sp.factor(q.subs(GP.gam, 0)) for q in GP.indicial(n, sp.Rational(2, n - 1))]
        damped = {"s0": 2, "sl": 3, "vl": 1}       # roots with Re >= n - 2: 10.12 (n = 4), his Theorem 4.9(3) (n = 3)
        tfr = (-(n - 2), 0)                         # beta - n/2 for the free operator ([Hin26c] Proposition 9.40)
        ok = True
        info = []
        for name, P in (("s0", s0), ("sl", sl), ("vl", vl)):
            rr_ = [-z for z in sp.roots(sp.Poly(P, lam_)).keys()]                    # r-roots at the origin
            def below(z):                                                         # Re z <= -(n - 2) for every l >= 1
                z1 = sp.expand(z)
                return z1.subs(L_, 1) <= -(n - 2) and sp.diff(z1, L_) <= 0
            def above(z):
                z1 = sp.expand(z)
                return z1.subs(L_, 1) >= 0 and sp.diff(z1, L_) >= 0
            lower = [z for z in rr_ if below(z)]
            upper = [z for z in rr_ if above(z)]
            win_lo = max(lower, key=lambda z: z.subs(L_, 1))
            win_hi = min(upper, key=lambda z: z.subs(L_, 1))
            good = len(lower) + len(upper) == len(rr_) and len(lower) == damped[name]
            if control == 1 and n == 4 and name == "sl":
                win_lo, win_hi = -L_, L_ - 1                                     # control: his window in 5D
            good &= sp.expand(win_lo - (lower and max(lower, key=lambda z: z.subs(L_, 1)))) == 0
            good &= all((win_lo - tfr[0]).subs(L_, k) <= 0 and (win_hi - tfr[1]).subs(L_, k) >= 0
                        for k in (1, 2, 5))                                       # the window contains (-(n-2), 0)
            good &= all(sp.expand(z - win_lo).subs(L_, 1) <= 0 for z in lower)
            ok &= good
            info.append(f"{name}: {sorted(lower, key=lambda z: z.subs(L_, 1))} | "
                        f"{sorted(upper, key=lambda z: z.subs(L_, 1))}")
        if n == 3:
            his = {-L_ - 2, -L_ - 1, -L_, L_ - 1, L_, L_ + 1}
            ok &= set(sp.expand(-z) for z in sp.roots(sp.Poly(sl, lam_)).keys()) == his
        chk(f"n + 1 = {n + 1}: free r-roots " + "; ".join(info) + f"; the windows contain beta - {sp.Rational(n, 2)} in "
            f"{tfr}, the counts below equal the damped operator's", ok)
    return chk.ok


CHECKS = [("F1 box^C on 4+1 Minkowski dilation invariant of degree -2, d_t* counted: (B.10)", f1, 1),
          ("F2 the beta-range at the origin in five dimensions: (0, 2 + C_0], his (1/2, 3/2 + C_0]", f2, 1),
          ("F3 Theorem B.4's thresholds: alpha_cf > 1 - b* at cf; -(1/2) r^2 l(dr/r) has positive eigenvalues", f3, 2),
          ("F4 section B.4's choice; the weights of Theorem 7.1(4), both halves, in five dimensions: [-C_0, 2)", f4, 2),
          ("F5 Proposition B.2's index 0 in five dimensions: the free operator's roots, windows and counts", f5, 1)]


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
