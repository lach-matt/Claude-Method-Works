#!/usr/bin/env python3
"""coupled5.py -- the coupled estimate for the last two components of the gauge vector on five-dimensional Tangherlini:
[Hun19] section 6 in five dimensions (N1STAR-PROOF.md section 10.10; D52).  Labels: computed (exact, sympy), deduced,
READ.

Section 10.7 leaves the pair (X_1-hat, X_L-hat), X_1 := f X_r, solving a system box_l X - A X = G with the zeroth-order
matrix of (10.29) and a source in the norm (10.16): with box_s := -f^-1 d_t^2 + r^-3 d_r(r^3 f d_r) the quotient wave
operator and V := (k^2/r^2) I + A,
    box_s X = V X + G,   A = (1/r^2) [[3 (1 - 3 x), 2k (1 - 2x)], [2k, -(1 + x)]],   x := mu/r^2,
[Hun19]'s (6.1) W = A_W W + G in five dimensions.  His section 6 estimates it by the T-energy, red-shift, Morawetz and
r^p currents for the pair, the non-self-adjoint part of A_W handled in the compact region by the identities (6.8)-(6.10)
that express derivatives of W through quantities already controlled.  This instrument computes the five-dimensional
form of each ingredient.

  K1 (computed, exact) The identities, [Hun19] (6.8)-(6.10) in five dimensions, and one more.  For the scalar-type
     one-form X = X_t S dt + X_r S dr + X_L r S_i dz^i (S_i = -d_th S/k) with S := div X, P := (dX)_tr/S, Q_t :=
     -(dX)_{t th}/S' and Q_r := -(dX)_{r th}/S' (W6's definitions), at l = 2:
         d_r X_1 + (3/r) X_1 + (k/r) X_L = S + f^-1 d_t X_t,            f d_r X_L + (f/r) X_L + (k/r) X_1 = (k f/r) Q_r,
         d_t X_1 = f (P + d_r X_t),                                     d_t X_L = (k/r)(Q_t - X_t),
     and with W6's (box X)_r and (box X)_t, under box X = J: Q_r = (r^2/k^2)(d_r S - f^-1 d_t P - J_r), Q_t =
     (r^2/k^2)(d_t S - (f/r^3) d_r(r^3 P) - J_t) -- so both time derivatives and both radial derivatives of the pair are
     zeroth order in it modulo S, P, X_t and J, the rungs below; Hung has the time derivative of W_1 only.  W6 is re-run
     here.  Control: the coupling k/r in the second identity doubled.
  K2 (computed, exact) The pair's matrix.  r^2 V -> [[k^2 + 3, 2k], [2k, k^2 - 1]] at infinity, with the eigenvalues (l +
     1)(l + 3) and (l - 1)(l + 1) at k^2 = l(l + 2): the flat decomposition into the modes l +- 1, positive definite for
     every l >= 2 (3 at l = 2), where Hung's [[Lambda + 2, -2 sqrt Lambda], [-2 sqrt Lambda, Lambda]] has (l + 1)(l + 2)
     and l(l - 1), the eigenvalues {0, 6} at l = 1 that force his care (READ).  The antisymmetric part of A is (k mu/r^4)
     [[0, -2], [2, 0]] exactly; A_12 vanishes at the photon sphere r^2 = 2 mu (his 1 - 3M/r at r = 3M) and changes sign
     there, so no diagonal rescaling symmetrises A.  Control: the eigenvalue (l - 1)(l + 1) claimed to be l^2.
  K3 (computed, exact) The T-current.  For C = diag(c_1, c_2) and N symmetric, J := sum_i c_i T[X_i](d_t, .) - (1/2)
     (X.N.X) g(d_t, .) has div J = d_t X.(C V - N) X + d_t X.C G (measure r^3).  With C = diag(10, 1) and N_in := [[10
     V_11, V_21], [V_21, V_22]] -- Hung's J_1,1 + J_1,2 with his weight 9 + 1 -- the error is d_t X_1 (10 V_12 - V_21)
     X_L, the time derivative of X_1 only, and N_in >= (k^2/4) r^-2 I on the whole exterior for every k^2 >= 8; with C =
     I and N_ex := sym(V) taking V_12 off the diagonal, the error is (4 k mu/r^4) d_t X_L X_1 and N_ex >= (k^2/4) r^-2 I
     for r^2 >= 2 mu.  Positivity exact: each determinant a polynomial in (x, k^2) with every coefficient in k^2 - 8
     positive on the stated x-interval (Sturm).  Control: c_1 = 1, N_in then indefinite at the horizon at k^2 = 8.
  K4 (computed, exact) The Morawetz current for the pair.  With M symmetric (generic) and T_ab = sum_i d_a X_i d_b X_i -
     (1/2) g_ab (sum_i dX_i.dX_i + X.M.X), J := T(F d_r*, .) + (1/4) omega d|X|^2 - (1/4) (d omega)|X|^2 + F' beta |X|^2
     dr* has, for box_s X = V X + G with V arbitrary,
         div J = (dF/dr) |f d_r X + beta X|^2 + X.W_M.X + (F f d_r X + (omega/2) X).((V - M) X + G),
         W_M := s_0 I - (1/2) F f dM/dr - (mu/r^3) F M,   s_0 := -(1/4) box omega + F'' beta/f + F'(beta'/f + 3 beta/r -
         beta^2/f):
     rungs5.py M1 for a system; and the g-current of M5 likewise, with X.V.X = X.sym(V).X.  Control: the sign of the beta
     term reversed.
  K5 (computed, exact) The Morawetz bulk for the pair is positive without Hung's compact-region substitution.  With M =
     sym(V), F and beta = 1/(2 sqrt mu) of rungs5.py M2: the cross term F f d_r X.(V - M) X is -(2 k mu F/r^4)(X_L Y_1 -
     X_1 Y_L), Y := f d_r X + beta X, exactly (the beta parts cancel by antisymmetry), which completes into the first
     term at the cost (k^2 mu^2 F^2/((dF/dr) r^8))|X|^2; keeping a tenth of the angular term k^2 F (1 - 2 mu/r^2)/r^3 for
     the bulk's angular control,
         W_rest := W_M - (1/10)(k^2 F (1 - 2 mu/r^2)/r^3) I - (k^2 mu^2 F^2/((dF/dr) r^8)) I >= (1/40) r^-3 I
     on the whole exterior for every real k^2 >= 8: in y = sqrt(mu)/r, r^3 W_rest - I/40 = [[p_1 + e K, k q], [k q, p_2 +
     e K]] (K = k^2) with e >= 0, p_i + 8 e > 0, and its determinant d_0 + d_1 (K - 8) + e^2 (K - 8)^2 with d_0 > 0, and
     4 d_0 e^2 - d_1^2 > 0 wherever d_1 < 0 (Sturm on the numerators, the photon-sphere factor divided out).  The minimum
     of r^3 W_rest at l = 2 is reported.  Hung needs (6.8)-(6.9) on [2M, bM] because his matrix is only semi-definite at
     l = 1; in five dimensions the class starts at l = 2 and the pair is definite there.  Control: half of the angular
     term kept, which fails at l = 2.
  K6 (computed, exact) The r^p current for the pair.  Psi := r^(3/2) X solves L Lbar Psi = -f Vcal Psi - f r^(3/2) G with
     Vcal = V + (3/4 + 9 mu/(4 r^2)) r^-2 I; V_inf := lim r^2 Vcal = [[k^2 + 15/4, 2k], [2k, k^2 - 1/4]] has the
     eigenvalues (l + 3/2)(l + 5/2) and (l - 1/2)(l + 1/2) > 0; sym(Vcal) - V_inf/r^2 = O(mu/r^4) and the antisymmetric
     part is (k mu/r^4)[[0, -2], [2, 0]]: (10.7) for the pair, V_inf positive definite.  Control: V_inf without the 3/4.

READ (alphaXiv, 2026-10-21).  [Hun19] section 6 pp. 38-55 in full: (6.1)-(6.37), Proposition 6.1 and Decay[W], the
assumption (6.3), the identities (6.8)-(6.11) with F_1, F_2, F_3, the T-current J_1 = J_1,1 + J_1,2 with A_W,in, A_W,ex,
A_W,aux and the positivity matrices (the eigenvalues {0, 6} at l = 1; Lambda + 1 - 5 s^-1 +- (1 - 3 s^-1) sqrt(4 Lambda
+ 1); 6 Lambda - 2 +- 4 sqrt(Lambda (Lambda + 1))), the Morawetz current J_3,1 with A_W,Mor, the matrices M_[bM,oo) and
M_[2M,bM] and the polynomials p_1, p_2, p_3, the f-bar current J_3,2, the r^p current J^p_4 with A_W,main and A_W,sub,
section 6.5 with C_1, epsilon_2, epsilon_4, R_T, b, and the dyadic argument (6.35)-(6.37); Lemma 4.10.

sympy.  python3 coupled5.py [--selftest | --mutants]   (about a minute; --verbose lists every sub-check)
"""
import os
import sys
import time

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wavegauge5 as WG                                       # the metric, the covariant derivative, W6

t, r, th, mu, f = WG.t, WG.r, WG.th, WG.mu, WG.f
kk = sp.Symbol("k", positive=True)
K = sp.Symbol("K", positive=True)                                                  # k^2
yv = sp.Symbol("y", positive=True)                                                 # sqrt(mu)/r
xv = sp.Symbol("x", nonnegative=True)                                              # mu/r^2
D = sp.diff
fp = D(f, r)


class Checklist:
    def __init__(self, verbose, quiet=False):
        self.ok, self.verbose, self.quiet = True, verbose, quiet

    def __call__(self, name, good):
        self.ok &= bool(good)
        if self.verbose or (not good and not self.quiet):
            print("      [%s] %s" % ("ok" if good else "FAIL", name), flush=True)


def A_of(k, muv=mu):
    x = muv/r**2
    return sp.Matrix([[3*(1 - 3*x), 2*k*(1 - 2*x)], [2*k, -(1 + x)]])/r**2


def V_of(k, muv=mu):
    return k**2/r**2*sp.eye(2) + A_of(k, muv)


# ------------------------------------------------------------------------------------------------- polynomial positivity
def _num_den(e, var):
    nu, de = sp.fraction(sp.together(sp.expand(e)))
    return sp.Poly(sp.expand(nu), var), sp.Poly(sp.expand(de), var)


def _strip(p, var, factors):
    """divide p by the maximal powers of the given factors; return (quotient, {factor: power})"""
    powers = {}
    for fac in factors:
        fp_ = sp.Poly(fac, var)
        n = 0
        while not p.is_zero:
            q, rem = sp.div(p, fp_)
            if not rem.is_zero:
                break
            p, n = q, n + 1
        powers[fac] = n
    return p, powers


def positive_on(e, var, a, b, allow_zero_at=()):
    """e (rational in var) > 0 on [a, b], except that it may vanish to even order at the roots of allow_zero_at
    (polynomials, >= 0 on [a, b] to even power) -- exact: the denominator and the stripped numerator have no root in
    [a, b] and are positive at the midpoint"""
    nu, de = _num_den(e, var)
    if nu.is_zero:
        return False
    nu, pw = _strip(nu, var, allow_zero_at)
    if any(n % 2 for n in pw.values()):
        return False
    mid = (sp.Rational(a) + sp.Rational(b))/2
    for p in (nu, de):
        if p.count_roots(a, b) != 0:
            return False
    return (nu.eval(mid)*de.eval(mid)) > 0


def coeffs_in(P, var, shift):
    """the coefficients of P (polynomial in var) in powers of (var - shift)"""
    Ps = sp.Poly(sp.expand(P.subs(var, var + shift)), var)
    return [Ps.coeff_monomial(var**j) for j in range(Ps.degree() + 1)]


# ------------------------------------------------------------------------------------------------- K1
def k1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    S, k2 = WG.harmonic(2)
    k = sp.sqrt(k2)
    Sth = D(S, th)
    Si = -Sth/k
    Xt, Xr, XL = [sp.Function(nm)(t, r) for nm in ("Xt", "Xr", "XL")]
    Xv = [Xt*S, Xr*S, XL*r*Si, 0, 0]
    Sd = sum(WG.gi[a, b]*WG.D1(Xv, a, b) for a in range(WG.N) for b in range(WG.N) if WG.gi[a, b] != 0)/S
    P = D(Xr, t) - D(Xt, r)
    Qt = (D(Xv[2], t) - D(Xv[0], th))/(-Sth)
    Qr = (D(Xv[2], r) - D(Xv[1], th))/(-Sth)
    X1 = f*Xr
    cK = 2*k if control == 1 else k
    items = [("d_r X_1 + (3/r) X_1 + (k/r) X_L = S + f^-1 d_t X_t (Hung's (6.8))",
              D(X1, r) + 3/r*X1 + k/r*XL - (Sd + D(Xt, t)/f)),
             ("f d_r X_L + (f/r) X_L + (k/r) X_1 = (k f/r) Q_r (his (6.9))", f*D(XL, r) + f/r*XL + cK/r*X1 - k*f/r*Qr),
             ("d_t X_1 = f (P + d_r X_t) (his (6.10))", D(X1, t) - f*(P + D(Xt, r))),
             ("d_t X_L = (k/r)(Q_t - X_t) (new: the time derivative of the angular component)",
              D(XL, t) - k/r*(Qt - Xt))]
    for name, e in items:
        chk("l = 2: " + name, sp.simplify(sp.expand(e.doit())) == 0)
    if control == 0:
        chk("W6 re-run at l = 2: (box X)_r = d_r S - f^-1 d_t P - (k^2/r^2) Q_r and (box X)_t = d_t S - (f/r^3) d_r(r^3 "
            "P) - (k^2/r^2) Q_t among its seven identities", WG.w6())
    return chk.ok


# ------------------------------------------------------------------------------------------------- K2
def k2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    l = sp.Symbol("l", positive=True)
    Minf = sp.Matrix([[kk**2 + 3, 2*kk], [2*kk, kk**2 - 1]])
    chk("r^2 V -> [[k^2 + 3, 2k], [2k, k^2 - 1]] at infinity",
        all(sp.simplify(sp.limit((V_of(kk)*r**2)[i, j], r, sp.oo) - Minf[i, j]) == 0
            for i in range(2) for j in range(2)))
    lam = sp.Symbol("lam")
    charp = sp.expand((Minf - lam*sp.eye(2)).det().subs(kk**2, l*(l + 2)))
    low = l**2 if control == 1 else (l - 1)*(l + 1)
    chk("its eigenvalues at k^2 = l(l + 2) are (l + 1)(l + 3) and (l - 1)(l + 1): positive definite for l >= 2",
        sp.expand(charp.subs(lam, (l + 1)*(l + 3))) == 0 and sp.expand(charp.subs(lam, low)) == 0)
    Lam = l*(l + 1)
    H4 = sp.Matrix([[Lam + 2, -2*sp.sqrt(Lam)], [-2*sp.sqrt(Lam), Lam]])
    ch4 = sp.expand((H4 - lam*sp.eye(2)).det())
    chk("Hung's leading matrix [[Lambda + 2, -2 sqrt Lambda], [-2 sqrt Lambda, Lambda]] has (l + 1)(l + 2) and l(l - 1),"
        " {0, 6} at l = 1 (READ)", sp.expand(ch4.subs(lam, (l + 1)*(l + 2))) == 0 and sp.expand(ch4.subs(lam, l*(l - 1)))
        == 0 and sp.expand(ch4.subs(l, 1).subs(lam, 0)) == 0)
    A = A_of(kk)
    anti = (A - A.T)/2
    chk("the antisymmetric part of A is (k mu/r^4) [[0, -2], [2, 0]]",
        sp.simplify(anti - kk*mu/r**4*sp.Matrix([[0, -2], [2, 0]])) == sp.zeros(2))
    chk("A_12 = 2k (1 - 2 mu/r^2)/r^2 vanishes at r^2 = 2 mu and changes sign: no diagonal symmetriser",
        sp.simplify(A[0, 1].subs(r, sp.sqrt(2*mu))) == 0 and sp.sign(A[0, 1].subs(r, sp.sqrt(mu)).subs(mu, 1)) == -1
        and sp.sign(A[0, 1].subs(r, 2*sp.sqrt(mu)).subs(mu, 1)) == 1)
    return chk.ok


# ------------------------------------------------------------------------------------------------- the quotient
def _setup(Vm, G):
    X = [sp.Function("X1")(t, r), sp.Function("XL")(t, r)]
    Xtt = [sp.expand(f*(f*D(X[i], r, 2) + (fp + 3*f/r)*D(X[i], r) - sum(Vm[i, j]*X[j] for j in range(2)) - G[i]))
           for i in range(2)]
    g = sp.diag(-f, 1/f)
    gi = g.inv()
    return X, Xtt, g, gi


def _div(Jl, gi, X, Xtt):
    Ju = gi*Jl
    div = (D(r**3*Ju[0], t) + D(r**3*Ju[1], r))/r**3
    return sp.expand(div.subs({D(X[0], t, 2): Xtt[0], D(X[1], t, 2): Xtt[1]}).doit())


def _generic():
    v = sp.Matrix(2, 2, lambda i, j: sp.Function("v%d%d" % (i, j))(r))
    G = [sp.Function("G1")(t, r), sp.Function("GL")(t, r)]
    return v, G


# ------------------------------------------------------------------------------------------------- K3
def k3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    v, G = _generic()
    X, Xtt, g, gi = _setup(v, G)
    c1, c2 = sp.symbols("c1 c2", positive=True)
    n11, n12, n22 = [sp.Function(nm)(r) for nm in ("n11", "n12", "n22")]
    Nm = sp.Matrix([[n11, n12], [n12, n22]])
    C = sp.diag(c1, c2)

    def Tu(u):
        grad = [D(u, t), D(u, r)]
        sq = sum(gi[a, b]*grad[a]*grad[b] for a in range(2) for b in range(2))
        return sp.Matrix(2, 2, lambda a, b: grad[a]*grad[b] - g[a, b]*sq/2)
    Tv = sp.Matrix([1, 0])
    XNX = (sp.Matrix(X).T*Nm*sp.Matrix(X))[0, 0]
    Jl = sp.Matrix([c1*(Tu(X[0])*Tv)[a] + c2*(Tu(X[1])*Tv)[a] - XNX*(g*Tv)[a]/2 for a in range(2)])
    div = _div(Jl, gi, X, Xtt)
    dX = sp.Matrix([D(X[0], t), D(X[1], t)])
    want = (dX.T*(C*v - Nm)*sp.Matrix(X))[0, 0] + (dX.T*C*sp.Matrix(G))[0, 0]
    chk("div J = d_t X.(C V - N) X + d_t X.C G for J = sum c_i T[X_i](d_t, .) - (1/2)(X.N.X) g(d_t, .)",
        sp.simplify(sp.expand(div - want)) == 0)
    # the five-dimensional choices, in x = mu/r^2 and K = k^2 (r^2 V)
    V = (V_of(kk)*r**2).subs(mu, xv*r**2).applyfunc(sp.expand)
    c1v = 1 if control == 1 else 10
    Nin = sp.Matrix([[c1v*V[0, 0], V[1, 0]], [V[1, 0], V[1, 1]]])
    Nex = sp.Matrix([[V[0, 0], V[0, 1]], [V[0, 1], V[1, 1]]])
    err_in = sp.expand(c1v*V[0, 1] - V[1, 0])
    err_ex = sp.expand(V[1, 0] - V[0, 1])
    chk("the inner error is d_t X_1 (10 V_12 - V_21) X_L and the outer one (4 k mu/r^4) d_t X_L X_1",
        sp.simplify(err_in - (10*V[0, 1] - V[1, 0])) == 0 and sp.simplify(err_ex - 4*kk*xv) == 0)

    def posdef(Nmat, lower, xa, xb):
        """Nmat - lower I > 0 for x in [xa, xb] and every K = k^2 >= 8: the diagonal entries and the determinant, each
        a polynomial in (x, K) whose coefficients in powers of K - 8 are positive on [xa, xb]"""
        Mm = (Nmat - lower*sp.eye(2)).applyfunc(lambda e: sp.expand(e.subs(kk, sp.sqrt(K))))
        good = True
        for e in (Mm[0, 0], Mm[1, 1], sp.expand(Mm.det())):
            P = sp.Poly(e, K)
            cs = coeffs_in(P.as_expr(), K, 8)
            good &= positive_on(cs[0], xv, xa, xb)
            good &= all(c == 0 or positive_on(c, xv, xa, xb) for c in cs[1:])
        return good
    chk("N_in := [[%d V_11, V_21], [V_21, V_22]] >= (k^2/4) r^-2 I on the whole exterior (x in [0, 1]) for every k^2 "
        ">= 8" % c1v, posdef(Nin, K/4, 0, 1))
    chk("N_ex := [[V_11, V_12], [V_12, V_22]] >= (k^2/4) r^-2 I for r^2 >= 2 mu (x in [0, 1/2]) for every k^2 >= 8",
        posdef(Nex, K/4, 0, sp.Rational(1, 2)))
    return chk.ok


# ------------------------------------------------------------------------------------------------- K4
def k4(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    v, G = _generic()
    X, Xtt, g, gi = _setup(v, G)
    F, beta = sp.Function("F")(r), sp.Function("beta")(r)
    m11, m12, m22 = [sp.Function(nm)(r) for nm in ("m11", "m12", "m22")]
    Mm = sp.Matrix([[m11, m12], [m12, m22]])
    drs = lambda e: f*D(e, r)                                                       # noqa: E731
    Xc = sp.Matrix(X)
    sqX = sum(xi**2 for xi in X)
    XMX = (Xc.T*Mm*Xc)[0, 0]
    T = sp.Matrix(2, 2, lambda a, b: sum(D(xi, [t, r][a])*D(xi, [t, r][b]) for xi in X)
                  - g[a, b]*(sum(gi[c, d]*D(xi, [t, r][c])*D(xi, [t, r][d]) for xi in X for c in range(2)
                                 for d in range(2)) + XMX)/2)
    Xv = sp.Matrix([0, F*f])
    omega = drs(F) + 3*f*F/r
    sgn = -1 if control == 1 else 1
    Jl = sp.Matrix([sum(T[a, b]*Xv[b] for b in range(2)) + omega*D(sqX, [t, r][a])/4 - D(omega, [t, r][a])*sqX/4
                    + sgn*drs(F)*beta*sqX*sp.Matrix([0, 1/f])[a] for a in range(2)])
    div = _div(Jl, gi, X, Xtt)
    boxw = D(r**3*f*D(omega, r), r)/r**3
    s0 = -boxw/4 + drs(drs(F))*beta/f + drs(F)*(drs(beta)/f + 3*beta/r - beta**2/f)
    WM = s0*sp.eye(2) - F*f*Mm.diff(r)/2 - mu/r**3*F*Mm
    Y = sp.Matrix([f*D(xi, r) + beta*xi for xi in X])
    lead = sp.Matrix([F*f*D(xi, r) + omega*xi/2 for xi in X])
    want = (D(F, r)*(Y.T*Y)[0, 0] + (Xc.T*WM*Xc)[0, 0] + (lead.T*((v - Mm)*Xc + sp.Matrix(G)))[0, 0])
    chk("div J = (dF/dr)|f d_r X + beta X|^2 + X.W_M.X + (F f d_r X + (omega/2) X).((V - M) X + G), W_M = s_0 I - (1/2) "
        "F f M' - (mu/r^3) F M (rungs5 M1 for the pair)", sp.simplify(sp.expand(div - want)) == 0)
    gg = sp.Function("g")(r)
    Jg = sp.Matrix([D(gg, [t, r][a])*sqX/4 - gg*D(sqX, [t, r][a])/4 for a in range(2)])
    divg = _div(Jg, gi, X, Xtt)
    boxg = D(r**3*f*D(gg, r), r)/r**3
    wantg = (boxg*sqX/4 + gg/(2*f)*sum(D(xi, t)**2 for xi in X) - gg/2*(f*sum(D(xi, r)**2 for xi in X)
                                                                         + (Xc.T*v*Xc)[0, 0])
             - gg/2*(Xc.T*sp.Matrix(G))[0, 0])
    chk("the g-current: div((1/4)(dg)|X|^2 - (1/4) g d|X|^2) = (1/4)(box g)|X|^2 + (1/2) g f^-1 |d_t X|^2 - (1/2) g (f "
        "|d_r X|^2 + X.V.X) - (1/2) g X.G (rungs5 M5 for the pair)", sp.simplify(sp.expand(divg - wantg)) == 0)
    return chk.ok


# ------------------------------------------------------------------------------------------------- K5
F_HKW = (1 - 2*mu/r**2)*(1 - mu/(2*r**2) + mu**2/(5*r**4))
BETA_HKW = 1/(2*sp.sqrt(mu))
KEEP = sp.Rational(1, 10)
FLOOR = sp.Rational(1, 40)


def w_rest(keep=KEEP, muv=1):
    """r^3 W_rest in y = sqrt(mu)/r at mu = 1 (W scales as mu^(-3/2)), k symbolic"""
    sub = {mu: muv}
    Fm, bm, fm = F_HKW.subs(sub), BETA_HKW.subs(sub), f.subs(sub)
    drs = lambda e: fm*D(e, r)                                                      # noqa: E731
    omega = drs(Fm) + 3*fm*Fm/r
    boxw = D(r**3*fm*D(omega, r), r)/r**3
    s0 = -boxw/4 + drs(drs(Fm))*bm/fm + drs(Fm)*(3*bm/r - bm**2/fm)
    Vm = V_of(kk, muv)
    Ms = (Vm + Vm.T)/2
    WM = s0*sp.eye(2) - Fm*fm*Ms.diff(r)/2 - muv/r**3*Fm*Ms
    Fr = D(Fm, r)
    W = WM - keep*kk**2*Fm*(1 - 2*muv/r**2)/r**3*sp.eye(2) - kk**2*muv**2*Fm**2/(Fr*r**8)*sp.eye(2)
    return (W*r**3).applyfunc(lambda e: sp.simplify(sp.expand(e).subs(r, 1/yv)))


def k5(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    # the cross term
    X1, XL, Y1, YL, Fs, bs = sp.symbols("X1 XL Y1 YL F beta")
    E = (A_of(kk) - A_of(kk).T)/2
    dr = sp.Matrix([(Y1 - bs*X1)/f, (YL - bs*XL)/f])                               # d_r X from Y = f d_r X + beta X
    cross = sp.expand((Fs*f*dr.T*E*sp.Matrix([X1, XL]))[0, 0])
    chk("the cross term F f d_r X.(V - sym V) X = -(2 k mu F/r^4)(X_L Y_1 - X_1 Y_L), the beta parts cancelling",
        sp.simplify(cross + 2*kk*mu*Fs/r**4*(XL*Y1 - X1*YL)) == 0)
    Frs = sp.Symbol("Fr", positive=True)
    sq = sp.expand(Frs*(Y1**2 + YL**2) - 2*kk*mu*Fs/r**4*(XL*Y1 - X1*YL)
                   - Frs*((Y1 - kk*mu*Fs/(Frs*r**4)*XL)**2 + (YL + kk*mu*Fs/(Frs*r**4)*X1)**2))
    chk("and it completes the square at the cost (k^2 mu^2 F^2/((dF/dr) r^8))|X|^2",
        sp.simplify(sq + kk**2*mu**2*Fs**2/(Frs*r**8)*(X1**2 + XL**2)) == 0)
    keep = sp.Rational(1, 2) if control == 1 else KEEP
    W = w_rest(keep)
    a11 = sp.expand(W[0, 0].subs(kk, sp.sqrt(K)))
    a22 = sp.expand(W[1, 1].subs(kk, sp.sqrt(K)))
    e1, e2 = sp.diff(a11, K), sp.diff(a22, K)
    p1, p2 = sp.simplify(a11 - e1*K) - FLOOR, sp.simplify(a22 - e2*K) - FLOOR
    q = sp.simplify(W[0, 1]/kk)
    good = (sp.simplify(e1 - e2) == 0 and sp.diff(e1, K) == 0 and kk not in q.free_symbols
            and K not in p1.free_symbols and K not in p2.free_symbols)
    chk("r^3 W_rest - I/40 = [[p_1 + e k^2, k q], [k q, p_2 + e k^2]] with a common slope e", good)
    if not good:
        return False
    e = sp.simplify(e1)
    ps = 1 - 2*yv**2                                                                 # the photon-sphere factor
    good = positive_on(e, yv, 0, 1, allow_zero_at=(ps,)) or sp.simplify(e) == 0
    chk("e >= 0 on the exterior (a double zero at the photon sphere)", good)
    a1, a2 = sp.simplify(p1 + 8*e), sp.simplify(p2 + 8*e)
    chk("p_1 + 8 e > 0 and p_2 + 8 e > 0 on the exterior", positive_on(a1, yv, 0, 1) and positive_on(a2, yv, 0, 1))
    d0 = sp.simplify(a1*a2 - 8*q**2)
    d1 = sp.simplify(e*(a1 + a2) - q**2)
    d2 = sp.simplify(e**2)
    chk("the determinant's coefficient d_0 (at k^2 = 8) > 0 on the exterior", positive_on(d0, yv, 0, 1))
    disc = sp.simplify(4*d0*d2 - d1**2)
    nu1, de1 = _num_den(d1, yv)
    nu1s, _ = _strip(nu1, yv, (ps,))
    roots = [iv for iv in nu1s.intervals() if iv[0][1] >= 0 and iv[0][0] <= 1]
    cuts = sorted({sp.Rational(0)} | {sp.Rational(1)} | {sp.Rational(iv[0][0]) for iv in roots}
                  | {sp.Rational(iv[0][1]) for iv in roots})
    cuts = [c for c in cuts if 0 <= c <= 1]
    good = True
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        mid = (lo + hi)/2
        if sp.sign(d1.subs(yv, mid)) >= 0 and nu1s.count_roots(lo, hi) == 0:
            continue                                                                  # d_1 >= 0 here
        good &= positive_on(disc, yv, lo, hi, allow_zero_at=(ps,))
    chk("where d_1 < 0 the discriminant 4 d_0 e^2 - d_1^2 > 0 (the photon-sphere factor divided out): the determinant "
        "is positive for every real k^2 >= 8", good)
    # the minimum at l = 2, reported
    W8 = W.subs(kk, sp.sqrt(8))
    fns = [sp.lambdify(yv, W8[i, j]) for i, j in ((0, 0), (0, 1), (1, 1))]
    best = (1e9, None)
    for i in range(1, 2001):
        y = i/2000
        a, b, c = (fn(y) for fn in fns)
        lam = (a + c)/2 - ((a - c)**2/4 + b*b)**0.5
        best = min(best, (lam, 1/y))
    chk("l = 2: the minimum of the least eigenvalue of r^3 W_rest is %.4f, at r = %.3f r_h" % best,
        best[0] > float(FLOOR))
    return chk.ok


# ------------------------------------------------------------------------------------------------- K6
def k6(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    v, G = _generic()
    X, Xtt, g, gi = _setup(v, G)
    Psi = [r**sp.Rational(3, 2)*xi for xi in X]
    V0 = (sp.Rational(3, 4) + 9*mu/(4*r**2))/r**2
    good = True
    for i in range(2):
        LLb = sp.expand((D(Psi[i], t, 2) - f*D(f*D(Psi[i], r), r)).subs(D(X[i], t, 2), Xtt[i]).doit())
        want = -f*(sum(v[i, j]*Psi[j] for j in range(2)) + V0*Psi[i]) - f*r**sp.Rational(3, 2)*G[i]
        good &= sp.simplify(sp.expand(LLb - want)) == 0
    chk("L Lbar Psi = -f Vcal Psi - f r^(3/2) G, Psi = r^(3/2) X, Vcal = V + (3/4 + 9 mu/(4 r^2)) r^-2 I", good)
    shift = 0 if control == 1 else sp.Rational(3, 4)
    Vcal = V_of(kk) + (shift + 9*mu/(4*r**2))/r**2*sp.eye(2)
    Vinf = (Vcal*r**2).applyfunc(lambda e: sp.limit(e, r, sp.oo))
    l = sp.Symbol("l", positive=True)
    lam = sp.Symbol("lam")
    charp = sp.expand((Vinf - lam*sp.eye(2)).det().subs(kk**2, l*(l + 2)))
    chk("V_inf = [[k^2 + 15/4, 2k], [2k, k^2 - 1/4]] with the eigenvalues (l + 3/2)(l + 5/2) and (l - 1/2)(l + 1/2)",
        sp.simplify(Vinf - sp.Matrix([[kk**2 + sp.Rational(15, 4), 2*kk], [2*kk, kk**2 - sp.Rational(1, 4)]]))
        == sp.zeros(2) and sp.expand(charp.subs(lam, (l + sp.Rational(3, 2))*(l + sp.Rational(5, 2)))) == 0
        and sp.expand(charp.subs(lam, (l - sp.Rational(1, 2))*(l + sp.Rational(1, 2)))) == 0)
    rem = ((Vcal + Vcal.T)/2 - Vinf/r**2).applyfunc(lambda e: sp.limit(sp.simplify(e*r**4), r, sp.oo))
    anti = ((Vcal - Vcal.T)/2).applyfunc(sp.simplify)
    chk("sym(Vcal) - V_inf/r^2 = O(mu/r^4) (r^4 times it has the limit %s) and the antisymmetric part is (k mu/r^4)"
        "[[0, -2], [2, 0]]" % list(rem), not any(e.has(sp.oo, -sp.oo, sp.zoo, sp.nan) for e in rem)
        and sp.simplify(anti - kk*mu/r**4*sp.Matrix([[0, -2], [2, 0]])) == sp.zeros(2))
    return chk.ok


CHECKS = [("K1 the identities: Hung's (6.8)-(6.10) in five dimensions and d_t X_L = (k/r)(Q_t - X_t); W6 re-run", k1, 1),
          ("K2 the pair's matrix: eigenvalues (l + 1)(l + 3), (l - 1)(l + 1) at infinity; A_12 = 0 at the photon sphere",
           k2, 1),
          ("K3 the T-current: div J = d_t X.(C V - N) X + ...; N_in, N_ex >= (k^2/4) r^-2 I; errors in d_t X_1 only", k3,
           1),
          ("K4 the Morawetz current and the g-current for the pair (rungs5 M1, M5 for a system)", k4, 1),
          ("K5 the Morawetz bulk is positive without Hung's substitution: W_rest >= r^-3/40 for every k^2 >= 8", k5, 1),
          ("K6 the r^p current: V_inf with eigenvalues (l + 3/2)(l + 5/2), (l - 1/2)(l + 1/2); remainder O(mu/r^4)", k6,
           1)]


def selftest(verbose=False):
    ok_all = True
    for name, fn, nc in CHECKS:
        t0 = time.time()
        good = fn(verbose=verbose)
        control = any(fn(control=k) for k in range(1, nc + 1))
        state = "PASS" if good and not control else "FAIL"
        ok_all &= state == "PASS"
        print(f"{name:<110} {state}  {time.time() - t0:.0f}s" + ("" if not control else "  (control passed: vacuous)"),
              flush=True)
    print(f"coupled5.py: {len(CHECKS) if ok_all else 'FAILED'}/{len(CHECKS)}")
    return ok_all


def mutants():
    caught = total = 0
    for name, fn, nc in CHECKS:
        for k in range(1, nc + 1):
            total += 1
            m = fn(control=k)
            caught += (not m)
            print(f"mutant {k} of {name[:2]}: {'caught' if not m else 'NOT caught'}", flush=True)
    print(f"coupled5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest("--verbose" in sys.argv) else 1)
