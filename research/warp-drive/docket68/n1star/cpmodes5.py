#!/usr/bin/env python3
"""cpmodes5.py -- the five-dimensional steps of [Hin26a] section 6: the constraint propagation operator's structure at
infinity, its thresholds at the radial sets, and the weights by which his Theorem 6.2 follows from his Theorem 5.2
(N1STAR-PROOF.md section 10.21; ROUTES-OPEN.md 4.22; D66).  Labels: computed (exact, sympy), deduced, READ.

[Hin26a] (arXiv:2606.27658v2) Theorem 6.2 -- mode stability of box^C = 2 delta G (delta* + C_h) at sigma != 0 in the
outgoing class, and invertibility of its zero energy operator on weights l in [-C_0 - 3/2, -1/2) (density r^2 |dr dg|)
-- is deduced from his Theorem 5.2 (forward solvability on weighted 3b-spaces, alpha_sf < -1/2, alpha_K > alpha_sf +
1/2) by: a regular-singular ODE at infinity, (6.4), whose exponent 1 + min spec S-bar^C gives the outgoing part omega_1
in A^1; the initial data then in rho^(-3/2-eps) H_b (density r^2), so alpha_sf = -C_0 - 2; and the indicial roots of his
Theorem 4.9.  His Theorem B.1 (the transition face problem) has in (B.13) the l-window -1/2 - h^-1 (1 - e)(1 + v) < l <
-1/2 + h^-1 (1 - e)(1 - v) and the beta-range (1/2, 3/2 + C_0], which carries the density's shift.  C omega = h^-1 (c
(x) omega + omega (x) c - m (1 - e) g <c, omega>), c = r^-1 (dt - v dr), m = 2/(D - 2) (damping5.py U2); [Hin26] (7.5)
gives S-bar_{E-bar^C} = gam^C [[2(1 - v), 0, 0], [(1 - e)(1 + v), (1 - e)(1 - v), 0], [0, 0, 1 - v]] in four dimensions,
gam^C = 1/h.

  K1 (computed, exact) On 4+1 Minkowski in t* = t - r and the Cartesian frame, box^C at the weight 2/3 is -2 d_t* rho
     (rho d_rho - 3/2 - S-bar^C) plus a stationary operator -- the d_t* d_r coefficient 2 Id, no d_t* times a
     tangential derivative, no d_t*^2 term -- and spec S-bar^C = h^-1 {2 (1 - v), (1 - e)(1 - v), 1 - v (three
     times)}: his (7.5) with three angular copies, all positive for 0 < v < 1, 0 <= e < 1.
     Four-dimensional control: weight 1, the same with two copies.  Control: the weight 1 in five dimensions.
  K2 (computed, exact) At the incoming covector the first-order part of the zero energy operator satisfies A_w + S-bar^C
     = D S-bar^C(-v) D, D the radial reflection: spec (A_w + S-bar^C) = h^-1 {2 (1 + v), (1 - e)(1 + v), 1 + v (3x)}.
     Read off the computed spectra -- each least eigenvalue shown below the others -- vartheta_in = -2 min spec (A_w +
     S-bar^C) = -2 h^-1 (1 - e)(1 + v) and the bottom of spec S-bar^C is h^-1 (1 - e)(1 - v); deduced from these, as in
     10.19(a) ([Hin26c] (9.16b)-(9.16c), (9.32)), the l-window of his (B.13), -1/2 - h^-1 (1 - e)(1 + v) < l < -1/2 +
     h^-1 (1 - e)(1 - v), is the same in five dimensions (its beta-range carries the density's shift, not this); the
     identity is structural, the reflection of dr carrying c = r^-1 (dt - v dr) to r^-1 (dt + v dr).  Four-dimensional
     control: the same.  Control: A_w with its sign flipped (at R_out A_w does not enter), where -A_w + S-bar^C is not D
     S-bar^C(-v) D.
  K3 (computed, exact) The weights of his section 6 at n = 4.  A time slab 0 <= t <= T r adds 1/2 to the weight in any
     dimension (the integral of rho^(-2 a) r^(n-1) over t in [0, T r] is T rho^(-2 a - 1) r^(n-1)); the transport
     equation (rho d_rho - 3/2 - s) u = 0 has u = rho^(3/2 + s), so omega_1 lies in A^(3/2 + min spec S-bar^C - eps), in
     A^1; the data |omega^(0)| <= C r^-1, |omega^(1)| <= C then lie in rho^a L^2(r^3 dr) iff a < -1, a < -2: in
     rho^(-2-eps) H_b (density r^3), his rho^(-3/2-eps) (r^2); so alpha_sf + 1/2 < -2, alpha_sf = -C_0 - 5/2 (his -C_0 -
     2), within 10.13's five-dimensional (5.14), alpha_sf < 0, alpha_K = 1 > alpha_sf; and Theorem 6.2(2)'s range is l
     + 2 in [-C_0, 2), l in [-C_0 - 2, 0) for r^3 |dr dg|, the Coulomb root 2 of damping5.py U4 its top (his l + 3/2 in
     [-C_0, 1)).  Four-dimensional control: his -C_0 - 2 and [-C_0 - 3/2, -1/2).  Control: the four-dimensional data
     weight -3/2 claimed in five dimensions.

Deduced, not computed here: with 10.13 (the critical-set thresholds and (5.14) in five dimensions), 10.14 (c on
Tangherlini) and these, [Hin26a] Theorem 6.2 on five-dimensional Tangherlini follows from his Theorem 5.2 there, which
stays OPEN; the index 0 of part (2) by his direct route, the radial ODEs of a static metric with 10.14's c, of the form
a(r) dt + b(r) dr, and damping5.py's roots.

READ.  [Hin26a] pp. 1-3 (Theorem 1.1, (1.2)), 9-11 (section 1.2.2, Figure 1.1, Remark 1.4), 38-43 (Proposition 5.1,
Theorem 5.2, (5.14)-(5.18), Lemma 5.3, footnote 15, section 5.2.1), 47 (Proposition 5.8), 51 (Proposition 5.9), 54
(Proposition 5.11), 64 (Proposition 5.17), 66-69 (Definition 6.1, Theorem 6.2 and its proof, (6.1)-(6.4), Remarks
6.3-6.4), 87 ((B.13)-(B.17), Theorem B.1), 93 (Theorem B.4), 98 (section B.4); [Hin26] pp. 135 ((7.3)-(7.6)); alphaXiv,
2026-10-22.

sympy.  python3 cpmodes5.py [--selftest | --mutants]   (--verbose lists every sub-check)
"""
import sys
import time

import sympy as sp

from damping5 import Checklist

D = sp.diff
v, e, h = sp.symbols("v e h", positive=True)


def minkowski_c(n, m):
    """2 delta G (delta* + C) on 1-forms of (n+1)-Minkowski, Cartesian frame, coordinates (t*, x), t* = t - r"""
    Tt = sp.Symbol("T")
    x = sp.symbols("x1:%d" % (n + 1), real=True)
    r = sp.sqrt(sum(xi**2 for xi in x))
    N = n + 1
    eta = sp.diag(-1, *([1]*n))
    W = [sp.Function("W%d" % a)(Tt, *x) for a in range(N)]

    def d(fn, mu_):
        return D(fn, Tt) if mu_ == 0 else D(fn, x[mu_ - 1]) - x[mu_ - 1]/r*D(fn, Tt)

    c = [1/r] + [-v*xi/r**2 for xi in x]
    cw = sum(eta[a, a]*c[a]*W[a] for a in range(N))
    S = sp.Matrix(N, N, lambda a, b: (d(W[b], a) + d(W[a], b))/2 + (c[a]*W[b] + c[b]*W[a] - m*(1 - e)*eta[a, b]*cw)/h)
    trS = sum(eta[a, a]*S[a, a] for a in range(N))
    Gh = S - eta*trS/2
    P = [sp.expand(-2*sum(eta[k, k]*d(Gh[a, k], k) for k in range(N))) for a in range(N)]
    return dict(P=P, W=W, T=Tt, x=x, r=r, N=N)


def parts(Mk, n):
    P, W, Tt, x, r, N = Mk["P"], Mk["W"], Mk["T"], Mk["x"], Mk["r"], Mk["N"]
    pt = {x[0]: 1, **{xi: 0 for xi in x[1:]}}
    Sb = sp.Matrix(N, N, lambda a, b: sp.simplify((r/2*P[a].coeff(D(W[b], Tt))).subs(pt)) - (sp.Rational(n - 1, 2)
                                                                                           if a == b else 0))
    A = sp.Matrix(N, N, lambda a, b: sp.simplify(sum(P[a].coeff(D(W[b], x[i]))*x[i] for i in range(n)).subs(pt)))
    no_tt = all(sp.simplify(P[a].coeff(D(W[b], Tt, 2)).subs(pt)) == 0 for a in range(N) for b in range(N))
    # the d_t* d_r coefficient: 2 Id, and no d_t* times a tangential derivative (-2 d_t* rho (rho d_rho) = 2 d_t* d_r)
    mixed = all(sp.simplify(P[a].coeff(D(W[b], Tt, x[i])).subs(pt)) == (2 if a == b and i == 0 else 0)
                for a in range(N) for b in range(N) for i in range(n))
    return Sb, A, no_tt and mixed


def spec(M):
    return {sp.factor(k): mm for k, mm in M.eigenvals().items()}


def bottom(vals):
    """the least of eigenvalues that are rational functions of v, e, h, if one lies below all the others on 0 < v, e < 1:
    each difference is shown positive with v = 1/(1 + p), e = 1/(1 + q) and p, q, h > 0"""
    p_, q_ = sp.symbols("p q", positive=True)
    sub = {v: 1/(1 + p_), e: 1/(1 + q_)}
    for c in vals:
        if all(z == c or sp.factor(sp.together((z - c).subs(sub))).is_positive for z in vals):
            return c
    return None


def want(n, s):
    return {sp.factor(2*(1 + s*v)/h): 1, sp.factor((1 - e)*(1 + s*v)/h): 1, sp.factor((1 + s*v)/h): n - 1}


# ------------------------------------------------------------------------------------------------- K1
def k1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        m = sp.Rational(2, n - 1) if control != 1 else 1
        Sb, A, no_tt = parts(minkowski_c(n, m), n)
        sp_ = spec(Sb)
        chk(f"n + 1 = {n + 1}: no d_t*^2 term, d_t* d_r coefficient 2 Id; spec S-bar^C = h^-1 {{2 (1 - v), "
            f"(1 - e)(1 - v), 1 - v ({n - 1}x)}} (weight {m})", no_tt and sp_ == want(n, -1))
    return chk.ok


# ------------------------------------------------------------------------------------------------- K2
def k2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in ((4,) if control else (4, 3)):
        Sb, A, _ = parts(minkowski_c(n, sp.Rational(2, n - 1)), n)
        sgn = -1 if control == 1 else 1
        M = sgn*A + Sb
        Dm = sp.diag(1, -1, *([1]*(n - 1)))
        Sm = Sb.subs(v, -v)
        conj = (M - Dm*Sm*Dm).applyfunc(sp.simplify) == sp.zeros(n + 1, n + 1)
        sp_ = spec(M)
        b_in, b_out = bottom(list(sp_)), bottom(list(spec(Sb)))      # read off the computed spectra
        if b_in is None or b_out is None:
            chk(f"n + 1 = {n + 1}: a least eigenvalue at R_in and at R_out", False)
            continue
        th_in = -2*b_in
        th_out = 2*b_out
        lo, hi = (-1 + th_in)/2, (-1 + th_out)/2
        chk(f"n + 1 = {n + 1}: A_w + S-bar^C = D S-bar^C(-v) D, spec h^-1 {{2 (1 + v), (1 - e)(1 + v), 1 + v}}; "
            f"l-window (-1/2 - h^-1 (1 - e)(1 + v), -1/2 + h^-1 (1 - e)(1 - v)) from the least eigenvalues",
            conj and sp_ == want(n, 1) and sp.simplify(lo + sp.Rational(1, 2) + (1 - e)*(1 + v)/h) == 0
            and sp.simplify(hi + sp.Rational(1, 2) - (1 - e)*(1 - v)/h) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- K3
def k3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    rho, a, s, Tm, tt = sp.symbols("rho a s T t", positive=True)
    for n in ((4,) if control else (4, 3)):
        r = 1/rho
        slab = sp.integrate(rho**(-2*a)*r**(n - 1), (tt, 0, Tm*r))
        half = sp.simplify(slab - Tm*rho**(-2*a - 1)*r**(n - 1)) == 0
        u = rho**(sp.Rational(n - 1, 2) + s)
        transport = sp.simplify(rho*D(u, rho) - (sp.Rational(n - 1, 2) + s)*u) == 0
        # rho^k in rho^a L^2(r^(n-1) dr) near rho = 0 iff k > a + n/2, i.e. a < k - n/2
        aa = sp.Symbol("aa")                                             # |omega^(0)| ~ r^-1, |omega^(1)| ~ 1
        data = [sp.solve(sp.Eq(2*(k - aa) - n - 1, -1), aa)[0] for k in (1, 0)]  # rho^(2(k - a)) rho^(-n-1) d rho
        dw = min(data)
        if control == 1:
            dw = -sp.Rational(3, 2)
        a_sf = dw - sp.Rational(1, 2)                                    # alpha_sf + 1/2 < dw: alpha_sf = -C_0 + a_sf
        top = n - 2                                  # the Coulomb root, computed in damping5.py U3 (10.12), typed here
        rng = (-sp.Rational(n, 2), top - sp.Rational(n, 2))              # l + n/2 in [-C_0, top): l = -C_0 + rng[0] ...
        exp_ = {4: (-sp.Rational(5, 2), -2, 0), 3: (-2, -sp.Rational(3, 2), -sp.Rational(1, 2))}[n]
        ok = half and transport and dw == exp_[0] + sp.Rational(1, 2) and a_sf == exp_[0] and rng == exp_[1:]
        chk(f"n + 1 = {n + 1}: slab +1/2; transport rho^((n-1)/2 + s); data in rho^({dw}-eps) H_b (r^{n - 1}); "
            f"alpha_sf = -C_0 {a_sf}; Theorem 6.2(2): l in [-C_0 {rng[0]}, {rng[1]})", ok)
    return chk.ok


CHECKS = [("K1 box^C on 4+1 Minkowski: -2 d_t* rho (rho d_rho - 3/2 - S-bar^C), spec his (7.5), three angular copies",
           k1, 1),
          ("K2 the radial sets: A_w + S-bar^C = D S-bar^C(-v) D, his (B.13) l-window in five dimensions", k2, 1),
          ("K3 section 6's weights at n = 4: data rho^(-2-eps), alpha_sf = -C_0 - 5/2, l in [-C_0 - 2, 0)", k3, 1)]


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
    print(f"cpmodes5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            res = fn(control=k)
            caught += (not res)
            print(f"mutant {k} of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"cpmodes5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest(verbose="--verbose" in args) else 1)
