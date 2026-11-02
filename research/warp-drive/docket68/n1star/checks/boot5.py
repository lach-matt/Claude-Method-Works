"""boot5.py -- SETTLE-GLAM5 round 4, (B): the bootstrap on the wedge W at weight a (the continuation, its expansion
and its uniqueness), and why the weight a_0 < 1/2 bootstrap of rounds 2-3 does not close.

Setting: Cartesian Kerr-Schild (t, x1..x4), g_b0 := eta + mu r^-2 k k (k = dt + xhat.dx); W = {v >= v1, t <= f(r)}
(S = {t = f(r)}, |f'| <= 1/2 on r >= 4R); the slices Sigma~_sigma := {t - f(r) = sigma} cap W, sigma in [T, 0];
X := w(u) d_t, w := (u* - u)^(2a) (u := t - r, u* - u >= 1 on W, r <= u* - u <= 2r + C there); H := Sigma + h_R the
perturbation, Sigma := sum_(p in {2,5/2,3,7/2,4}) r^-p F_p(s), s := (v - v1)/r; Gamma in {d_t, L_Omega, Z},
Z := (t - v1) d_t + x.d_x; P_mu(h) := Ric^H(g_b0(mu) + h; g_b0(mu)).

  B1 (computed, 2000 random points) the flux through the slices: for g = g_b0 + H with |H| <= 1/50, r >= 4, mu = 1
     (mu/r^2 <= 1/16), |f'| <= 1/2, the quadratic form p -> T(d_t, -grad(t - f)) (T of a function with dphi = p) lies
     between c1 |p|^2 and c2 |p|^2 with c1 > 0.1, c2 < 3; sqrt|det g| in [0.9, 1.1]. Control: |f'| = 3/2 (S not
     spacelike) gives a negative value.
  B2 (computed) the bulk sign: g^-1(du, du) = -4 mu/r^2 for g_b0, and stays < 0 for |H| <= mu/(2 r^2) (2000 points),
     so -grad u and d_t are future timelike and T(grad w, d_t) = |w'| T(-grad u, d_t) >= 0. Control: |H| up to
     8 mu/r^2 makes du spacelike somewhere.
  B3 (exact; computed) the Hardy inequality on the slices (four space dimensions):
     int_R^oo r^(2a+1) phi^2 dr <= (a + 1)^-2 int_R^oo r^(2a+3) phi_r^2 dr, the boundary term at the inner edge of
     the good sign, the constant sharp (phi = r^(-a-1-eta): ratio 1/(a + 1 + eta)^2, exact). Control: the constant
     (a + 1)^-2 / 2 is violated by that family.
  B4 (exact) the radial derivatives from the commuted fields: x.d_x = Z - (t - v1) d_t; along a ray of
     Sigma~_sigma, d/dr = xhat.d_x + f' d_t; v increases along the ray (1 + f' >= 1/2); |t - v1| <= r on W. Control:
     with |f'| = 3/2 the ray can leave {v >= v1}.
  B5 (computed, mpmath 60 digits, central differences) the commuted equations' structure, from the exact identities
     (Z + 2) P(h) = DP(h)[Z h] - 2 mu d_mu P(h) (R3c) and d_t P(h) = DP(h)[d_t h] (scale5 Z2a), differentiated in h:
        (Z + 2) DP(h)[k] = DP(h)[Z k] + D^2P(h)[Z h, k] - 2 mu d_mu DP(h)[k],
        d_t (DP(h)[k]) = DP(h)[d_t k] + D^2P(h)[d_t h, k],
     all 15 components, two points, an explicit h of size 0.3 and an explicit k. By induction they give the equation
     of every Gamma^alpha h: DP(h)[Gamma^alpha h] = sum of D^mP(h)[Gamma^(alpha_1) h, ...] (m >= 2, each |alpha_i| >=
     1) and (mu d_mu)^j-terms. Controls: without the D^2P term both fail.
  B6 (exact) the kernel table of the weighted energy for Gamma^alpha h_R: every error term, its bound on
     Sigma~_sigma (r >= r_sigma >= |sigma| - C) and its time kernel (1 + |sigma|)^-q: residual P(Sigma) = O(lam
     r^(-13/2)) (q = 9/2 - a), explicit coefficients (q = 2, 3), first-order coefficients eps r^(-3/2-a) (q = 3/2 +
     a), zero-order through Hardy eps r^(-1/2-a) (q = a + 1/2), the bulk-sign error and the deformation (q = 3,
     3/2 + a), the mu d_mu second-order source (q = 2): all integrable exactly for a in (1/2, 7/2), so on R3.6's
     window (5/2, 3). Controls: a = 1/2 and a = 7/2 each leave one kernel non-integrable.
  B7 (exact, enumeration) the split of the commuted multilinear terms: every term (m >= 2 slots, |alpha_i| >= 1,
     sum <= k0, one slot with at most two derivatives) has one slot in L^2 (energy order <= k0) and the others in
     sup (order + 3, or + 4 with two derivatives, <= k0): true for every k0 >= 7 (k0 <= 60), and the same rule with
     k0 - 1 in place of k0 for the sup factors (the tame induction above a fixed k1) for every k >= 9. Controls:
     k0 = 6 fails; the rule with the largest slot in sup fails at every k0.
  B8 (exact) the residual's degree: P(g_b0 + Sigma) has its flat parts cancelled degree by degree, the degree -6
     terms (mu Sigma_2, Sigma_2 Sigma_2) cancelled by Sigma_4's equation, and its leading degree is -13/2 (mu
     Sigma_(5/2), Sigma_2 Sigma_(5/2)): ||w^(1/2) P(Sigma)|| on Sigma~_sigma ~ r_sigma^(a - 9/2). Control: without the
     p = 4 term the leading degree is -6.
  B9 (exact; computed) the self-similar terms are the fixed-v expansion: (a) the 2F1(p + l, p - l - 2; p - 1/2; s/2)
     coefficient ratio equals the flat recursion G_(2q)' = (Delta + (q - 1)(q - 3)) G_(2q-2)/(2q - 3) at q = p + m,
     Delta = -l(l + 2): (p + m - 1)(p + m - 3) - l(l + 2) = (p + m - l - 3)(p + m + l - 1), symbolic in p, l, m;
     (b) after the shell (G_3 = 0, G_4 and G_5 constant in v) the flat recursion makes G_k a polynomial in v of
     degree floor((k - 4)/2) (k <= 16); (c) max over s in [0, 3/2] of |2F1| grows at most polynomially in l
     (l <= 120, p in {2, 5/2, 3, 7/2}; log-log slope bounded). Control (a): third parameter p + 1/2 breaks it.
  B10 (exact; computed) the weight a_0 < 1/2 scheme of rounds 2-3 does not close: its top-order quasilinear term
     -(1/2)(Dg^-1[Gamma^alpha h]) d d h is bounded, by the quantities that scheme controls, only through Hardy for
     Gamma^alpha h and Sobolev for d d h, a kernel (1 + |sigma|)^(-(a_0 + 1/2)), not integrable for a_0 <= 1/2; and
     neither factor's bound can be improved in the class: Sobolev's is attained by the band family R^(-a-3/2)
     psi(r - R) (weighted energy bounded, R^(a+3/2) |phi| = psi(1/2) at r = R + 1/2), Hardy's constant by
     r^(-a-1-eta) (B3). Control: the same chain at a = 11/4 is integrable.
  B11 (exact) uniqueness at weight a_0 in (0, 1/2): for two solutions with the same data on N, the constructed one
     (weight a, h = Sigma + h_R) and any h' of the a_0-class (|d h'| <= C r^(-3/2-a_0)), the difference equation
     written with g' as principal part and d d h of the constructed solution as zero-order coefficient has kernels
     q = min(3, a + 1/2) (zero order, Hardy), 3/2 + a_0 (first order, deformation, bulk-sign error): all > 1; the
     cap energies at weight a_0 tend to 0 (Sigma: |sigma|^(2a_0 - 2); h_R: weight a > a_0). Control: with the
     zero-order coefficient taken from h' the kernel is q = a_0 + 1/2 <= 1.
  B12 (exact) the limit T -> -oo: the tails that bound E[h_T - h_T'] on Sigma~_T (N-flux beyond |T|:
     |T|^(2a - 7); cap: |T|^(2a - 6); residual: int_(-oo)^T |sigma|^(a - 9/2) = |T|^(a - 7/2)/(7/2 - a)) all tend to
     0 for a < 3. Control: at a = 7/2 the residual tail does not.
  B13 (exact) the means at past null infinity (Lemma R4.3): the sources of every stage have exponents >= 3 (the
     count of Theorem A_P), so the wave integration 2/(2q - 5) and the transport 1/(q - 5/2) never meet q = 5/2, and
     phi's transport 1/(q - 1) never meets q = 1 (its source starts at q = 2): no logarithm at any order (exponent
     closure to 12). Control: a source at q = 5/2 would give 2/(2q - 5) = oo.
Labels: computed (B1-B2 random sampling; B5 mpmath at 60 digits; B9(c) mpmath); the rest exact (sympy, integers).

    python3 checks/boot5.py
"""
import random
import sys
from fractions import Fraction as Fr
from functools import lru_cache

import mpmath as mp
import sympy as sp

import builtins as _builtins
import textwrap as _textwrap

_raw_print = _builtins.print


def print(*args, **kw):  # output lines are kept to 121 characters (wrapped, continuation indented)
    text = kw.pop("sep", " ").join(str(x) for x in args)
    for line in text.split("\n"):
        for piece in (_textwrap.wrap(line, 121, subsequent_indent="        ", break_long_words=True,
                                     replace_whitespace=False, drop_whitespace=True) or [""]):
            _raw_print(piece, **kw)


FAIL = []


def check(name, ok, msg=""):
    print(f"  {name}: {'pass' if ok else 'FAIL'} {msg}")
    if not ok:
        FAIL.append(name)


@lru_cache(maxsize=None)
def _integrable(q):
    s = sp.Symbol("s", positive=True)
    return sp.integrate(s**(-q), (s, 1, sp.oo)).is_finite


def integrable(q):
    """int_1^oo s^-q ds is finite (computed by sympy, cached)"""
    return _integrable(sp.nsimplify(q))


# ---------------------------------------------------------------- B1, B2: the metric's margins

def metric(r_, xh, mu_, H):
    k = [1.0] + xh
    eta = [-1, 1, 1, 1, 1]
    import numpy as np
    g = np.array([[(eta[i] if i == j else 0) + mu_/r_**2*k[i]*k[j] for j in range(5)] for i in range(5)]) + H
    return g


def b1():
    import numpy as np
    print("B1  the flux through the slices t - f(r) = sigma")
    rng = random.Random(5)
    lo, hi, detdev = 1e9, -1e9, 0.0
    ctl = 1e9
    for _ in range(2000):
        r_ = rng.uniform(4, 40)
        x = np.array([rng.gauss(0, 1) for _ in range(4)])
        xh = list(x/np.linalg.norm(x))
        A = np.array([[rng.uniform(-1, 1) for _ in range(5)] for _ in range(5)])
        H = (A + A.T)/2
        H *= (1/50)/max(abs(np.linalg.eigvalsh(H)))*rng.uniform(0, 1)
        g = metric(r_, xh, 1.0, H)
        gi = np.linalg.inv(g)
        X = np.array([1.0, 0, 0, 0, 0])
        for fp in (rng.uniform(-0.5, 0.5), 1.5):
            nu = np.array([1.0] + [-fp*c for c in xh])  # d(t - f(r))
            Y = -gi@nu
            gXY = X@g@Y
            M = (np.outer(X, Y) + np.outer(Y, X))/2 - 0.5*gXY*gi
            ev = np.linalg.eigvalsh(M)
            if fp == 1.5:
                ctl = min(ctl, ev[0])
            else:
                lo, hi = min(lo, ev[0]), max(hi, ev[-1])
        detdev = max(detdev, abs(np.sqrt(abs(np.linalg.det(g))) - 1))
    check("B1a c1 |p|^2 <= T(d_t, -grad(t - f)) <= c2 |p|^2 with c1 > 0.1, c2 < 3 (|H| <= 1/50, r >= 4, mu = 1, "
          "|f'| <= 1/2, 2000 points)", lo > 0.1 and hi < 3, f"c1 = {lo:.3f}, c2 = {hi:.3f}")
    check("B1b sqrt|det g| in [0.9, 1.1]", detdev < 0.1, f"max |sqrt|det g| - 1| = {detdev:.3f}")
    check("B1c control: |f'| = 3/2 (the slice not spacelike) gives a negative value", ctl < 0, f"min = {ctl:.3f}")


def b2():
    import numpy as np
    print("B2  the bulk sign: grad u timelike")
    rng = random.Random(9)
    worst, ctl = -1e9, -1e9
    for _ in range(2000):
        r_ = rng.uniform(4, 400)
        x = np.array([rng.gauss(0, 1) for _ in range(4)])
        xh = list(x/np.linalg.norm(x))
        A = np.array([[rng.uniform(-1, 1) for _ in range(5)] for _ in range(5)])
        Hs = (A + A.T)/2
        Hs /= max(abs(np.linalg.eigvalsh(Hs)))
        du = np.array([1.0] + [-c for c in xh])
        for th, store in ((0.5, "ok"), (8.0, "ctl")):
            g = metric(r_, xh, 1.0, th/r_**2*Hs)
            val = du@np.linalg.inv(g)@du*r_**2
            if store == "ok":
                worst = max(worst, val)
            else:
                ctl = max(ctl, val)
    g0i = np.linalg.inv(metric(5.0, [1.0, 0, 0, 0], 1.0, 0*np.eye(5)))
    du = np.array([1.0, -1, 0, 0, 0])
    exact = du@g0i@du*25
    check("B2a g_b0^-1(du, du) = -4 mu/r^2 (r = 5, mu = 1)", abs(exact + 4) < 1e-12, f"{exact:.12f} r^-2")
    check("B2b g^-1(du, du) r^2 < 0 for |H| <= mu/(2 r^2) (2000 points, r in [4, 400])", worst < 0,
          f"max {worst:.3f}")
    check("B2c control: |H| up to 8 mu/r^2 makes du spacelike somewhere", ctl > 0, f"max {ctl:.3f}")
    # Phi_W := v + 1/r: g_b0^-1(dPhi, dPhi) = -2 r^-2 + r^-4 (1 - mu r^-2) exactly, and < 0 for |H| <= r^-2/2
    rs, ms = sp.symbols("r mu", positive=True)
    gvv, gvr, grr = 0, 1, 1 - ms/rs**2       # g_b0^-1(dv, dv), (dv, dr), (dr, dr) (trunc5 T1b, T4a)
    exact = gvv + 2*(-rs**-2)*gvr + rs**-4*grr
    worstP, ctlP = -1e9, -1e9
    for _ in range(2000):
        r_ = rng.uniform(4, 400)
        x = np.array([rng.gauss(0, 1) for _ in range(4)])
        xh = list(x/np.linalg.norm(x))
        A = np.array([[rng.uniform(-1, 1) for _ in range(5)] for _ in range(5)])
        Hs = (A + A.T)/2
        Hs /= max(abs(np.linalg.eigvalsh(Hs)))
        dPhi = np.array([1.0] + [(1 - 1/r_**2)*c for c in xh])
        for th, store in ((0.5, "ok"), (4.0, "ctl")):
            g = metric(r_, xh, 1.0, th/r_**2*Hs*rng.uniform(0.5, 1))
            val = dPhi@np.linalg.inv(g)@dPhi*r_**2
            if store == "ok":
                worstP = max(worstP, val)
            else:
                ctlP = max(ctlP, val)
    check("B2d Phi_W := v + 1/r: g_b0^-1(dPhi, dPhi) = -2 r^-2 + r^-4 (1 - mu r^-2) (exact), and r^2 g^-1(dPhi, dPhi) "
          "< 0 for |H| <= r^-2/2 (2000 points): a time function on W for the perturbed metrics",
          sp.simplify(exact - (-2/rs**2 + (1 - ms/rs**2)/rs**4)) == 0 and worstP < 0, f"max {worstP:.3f}")
    check("B2e control: |H| up to 4 r^-2 makes dPhi_W spacelike somewhere", ctlP > 0, f"max {ctlP:.3f}")


# ---------------------------------------------------------------- B3, B4: Hardy, the radial derivatives

def b3():
    print("B3  the Hardy inequality on the slices")
    r, R, a, eta, c = sp.symbols("r R a eta c", positive=True)
    phi = r**(-a - 1 - eta)
    lhs = sp.integrate(r**(2*a + 1)*phi**2, (r, R, sp.oo), conds="none")
    rhs = sp.integrate(r**(2*a + 3)*sp.diff(phi, r)**2, (r, R, sp.oo), conds="none")
    ratio = sp.simplify(lhs/rhs)
    check("B3a phi = r^(-a-1-eta): ratio = 1/(a + 1 + eta)^2 -> (a + 1)^-2 (the constant is sharp)",
          sp.simplify(ratio - 1/(a + 1 + eta)**2) == 0, str(ratio))
    # integration by parts: int r^(2a+1) phi^2 = -R^(2a+2) phi(R)^2/(2a+2) - (1/(a+1)) int r^(2a+2) phi phi'
    f = sp.Function("f")
    ibp = sp.diff(r**(2*a + 2)*f(r)**2/(2*a + 2), r) - (r**(2*a + 1)*f(r)**2
                                                      + r**(2*a + 2)*f(r)*sp.diff(f(r), r)/(a + 1))
    check("B3b the integration by parts behind it: d/dr (r^(2a+2) f^2/(2a+2)) = r^(2a+1) f^2 + r^(2a+2) f f'/(a+1); the "
          "boundary term at the inner edge enters as -R^(2a+2) f(R)^2/(2a+2) <= 0", sp.simplify(ibp) == 0)
    rng = random.Random(4)
    worst = 0
    mp.mp.dps = 20
    for _ in range(100):
        av = rng.uniform(0.1, 3.5)
        cs = [rng.uniform(-1, 1) for _ in range(3)]
        bs = [av + 1 + rng.uniform(0.05, 2) for _ in range(3)]
        ph = lambda x: sum(cc*x**(-bb) for cc, bb in zip(cs, bs))
        dph = lambda x: sum(-bb*cc*x**(-bb - 1) for cc, bb in zip(cs, bs))
        L = mp.quad(lambda x: x**(2*av + 1)*ph(x)**2, [1, 10, mp.inf])
        Rr = mp.quad(lambda x: x**(2*av + 3)*dph(x)**2, [1, 10, mp.inf])
        worst = max(worst, L*(av + 1)**2/Rr)
    check("B3c 100 random phi = sum c_i r^(-b_i), b_i > a + 1 (quadrature on [1, oo)): ratio <= (a + 1)^-2",
          worst <= 1 + mp.mpf(10)**-12, "max ratio x (a+1)^2 = " + mp.nstr(worst, 6))
    bad = (ratio*2*(a + 1)**2).subs({a: 1, eta: sp.Rational(1, 100)})
    check("B3d control: the constant (a + 1)^-2 / 2 is violated by r^(-a-1-eta), eta = 1/100", bad > 1, str(bad))


def b4():
    print("B4  the radial derivatives from the commuted fields")
    t, v1, fp_ = sp.symbols("t v1 fp", real=True)
    X = sp.symbols("x1:5", real=True)
    r = sp.sqrt(sum(c**2 for c in X))
    u = sp.Function("u")(t, *X)
    Zu = (t - v1)*sp.diff(u, t) + sum(c*sp.diff(u, c) for c in X)
    xd = sum(c*sp.diff(u, c) for c in X)
    check("B4a x.d_x = Z - (t - v1) d_t on every function", sp.simplify(Zu - (t - v1)*sp.diff(u, t) - xd) == 0)
    rr, sig, tt = sp.symbols("rr sigma tt", real=True)
    fcon = 3 + 1/rr + sp.Rational(1, 2)/rr**2           # a concrete f with f' in |x|^-2 C^oo
    wcon = sp.sin(tt)*rr**2 + tt**3*sp.exp(-rr) + tt*rr  # a concrete function of (t, r)
    along = sp.diff(wcon.subs(tt, fcon + sig), rr)
    target = (sp.diff(wcon, rr) + sp.diff(fcon, rr)*sp.diff(wcon, tt)).subs(tt, fcon + sig)
    wrong = sp.diff(wcon, rr).subs(tt, fcon + sig)
    check("B4b along a ray of Sigma~_sigma: d/dr (w(f(r) + sigma, r)) = (d_r w + f' d_t w)(f(r) + sigma, r) (concrete "
          "f, w); control: d_r w alone is not it", sp.simplify(along - target) == 0 and sp.simplify(along - wrong) != 0)
    vprime = 1 + fp_
    check("B4c v = f(r) + sigma + r increases along the ray when |f'| <= 1/2 (v' = 1 + f' >= 1/2)",
          all(vprime.subs(fp_, c) >= sp.Rational(1, 2) for c in (sp.Rational(-1, 2), 0, sp.Rational(1, 2))))
    check("B4d control: with f' = -3/2 the ray turns back in v (v' = -1/2 < 0)",
          vprime.subs(fp_, -sp.Rational(3, 2)) < 0)
    # |t - v1| <= r on W: t - v1 >= -r from v >= v1; t - v1 <= r from t <= f(r), v1 = f(4R) + 4R, |f'| <= 1/2, r >= 4R
    Rv = sp.Symbol("R", positive=True)
    worst = -(sp.Rational(1, 2)*(rr - 4*Rv)) + 4*Rv + rr  # v1 + r - t >= f(4R) - f(r) + 4R + r >= -(r - 4R)/2 + 4R + r
    check("B4e |t - v1| <= r on W (r >= 4R, |f'| <= 1/2): v1 + r - t >= (r + 12 R)/2 > 0",
          sp.simplify(worst - (rr + 12*Rv)/2) == 0)


# ---------------------------------------------------------------- B5: the commuted equations' structure

TS, XS4 = sp.Symbol("t", real=True), sp.symbols("x1:5", real=True)
XS = (TS,) + XS4
MUS = sp.Symbol("mu", positive=True)
ES = sp.symbols("e1:6", real=True)
V1 = sp.Rational(7, 10)
RRs = sp.sqrt(sum(c**2 for c in XS4))
R5 = range(5)


def gb0(m):
    k = [sp.Integer(1)] + [c/RRs for c in XS4]
    return sp.diag(-1, 1, 1, 1, 1) + m/RRs**2*sp.Matrix(5, 5, lambda i, j: k[i]*k[j])


def h_explicit():
    q = ((TS - sp.Rational(3, 10))**2 + (XS4[0] - 1)**2 + (XS4[1] + sp.Rational(1, 2))**2 + XS4[2]**2
         + (XS4[3] - sp.Rational(7, 10))**2)/8
    cvals = [[3, -2, 1, 4, -1], [-2, 5, 2, -3, 1], [1, 2, -4, 1, 3], [4, -3, 1, 2, -2], [-1, 1, 3, -2, 6]]
    return sp.Matrix(5, 5, lambda i, j: sp.Rational(cvals[i][j], 20)*sp.exp(-q)*(1 + XS4[0]*TS/5))


def k_explicit():
    q = ((TS + sp.Rational(1, 5))**2 + XS4[0]**2 + (XS4[1] - 1)**2 + (XS4[2] - sp.Rational(1, 2))**2 + XS4[3]**2)/6
    cvals = [[1, 2, 0, -1, 3], [2, -1, 1, 0, 2], [0, 1, 3, -2, 1], [-1, 0, -2, 2, 1], [3, 2, 1, 1, -3]]
    return sp.Matrix(5, 5, lambda i, j: sp.Rational(cvals[i][j], 15)*sp.exp(-q))


def zop(H):
    return sp.Matrix(5, 5, lambda i, j: (TS - V1)*sp.diff(H[i, j], TS) + sum(c*sp.diff(H[i, j], c) for c in XS4))


def dtop(H):
    return sp.Matrix(5, 5, lambda i, j: sp.diff(H[i, j], TS))


class Op:
    def __init__(self, G, G0):
        self.f = {}
        args = (XS, MUS, ES)
        for name, M in (("g", G), ("g0", G0)):
            comp = {}
            for i in R5:
                for j in range(i, 5):
                    e = M[i, j]
                    comp[(i, j)] = sp.lambdify(args, e, "mpmath")
                    for a in R5:
                        ea = sp.diff(e, XS[a])
                        comp[(i, j, a)] = sp.lambdify(args, ea, "mpmath")
                        for b in range(a, 5):
                            comp[(i, j, a, b)] = sp.lambdify(args, sp.diff(ea, XS[b]), "mpmath")
            self.f[name] = comp

    def jets(self, name, X, m, E):
        c = self.f[name]
        g = mp.matrix(5, 5)
        dg = [[[0]*5 for _ in R5] for _ in R5]
        ddg = [[[[0]*5 for _ in R5] for _ in R5] for _ in R5]
        for i in R5:
            for j in range(i, 5):
                g[i, j] = g[j, i] = c[(i, j)](X, m, E)
                for a in R5:
                    dg[a][i][j] = dg[a][j][i] = c[(i, j, a)](X, m, E)
                    for b in range(a, 5):
                        v = c[(i, j, a, b)](X, m, E)
                        ddg[a][b][i][j] = ddg[a][b][j][i] = ddg[b][a][i][j] = ddg[b][a][j][i] = v
        return g, dg, ddg

    @staticmethod
    def christoffel(g, dg, ddg):
        gi = g**-1
        dgi = [[[-sum(gi[r, al]*dg[c][al][be]*gi[be, s] for al in R5 for be in R5) for s in R5] for r in R5]
               for c in R5]
        low = [[[(dg[a][s][b] + dg[b][s][a] - dg[s][a][b])/2 for b in R5] for a in R5] for s in R5]
        Gam = [[[sum(gi[r, s]*low[s][a][b] for s in R5) for b in R5] for a in R5] for r in R5]
        dlow = [[[[(ddg[c][a][s][b] + ddg[c][b][s][a] - ddg[c][s][a][b])/2 for b in R5] for a in R5] for s in R5]
                for c in R5]
        dGam = [[[[sum(dgi[c][r][s]*low[s][a][b] + gi[r, s]*dlow[c][s][a][b] for s in R5) for b in R5]
                  for a in R5] for r in R5] for c in R5]
        return gi, dgi, Gam, dGam

    def P(self, X, m, E):
        g, dg, ddg = self.jets("g", X, m, E)
        g0, dg0, ddg0 = self.jets("g0", X, m, E)
        gi, dgi, G, dG = self.christoffel(g, dg, ddg)
        _, _, G0, dG0 = self.christoffel(g0, dg0, ddg0)
        Ric = mp.matrix(5, 5)
        for a in R5:
            for b in R5:
                Ric[a, b] = (sum(dG[r][r][a][b] for r in R5) - sum(dG[b][r][a][r] for r in R5)
                             + sum(G[r][r][l]*G[l][a][b] for r in R5 for l in R5)
                             - sum(G[r][b][l]*G[l][a][r] for r in R5 for l in R5))
        dGam = [[[G[r][a][b] - G0[r][a][b] for b in R5] for a in R5] for r in R5]
        Dv = [sum(gi[a, b]*dGam[r][a][b] for a in R5 for b in R5) for r in R5]
        dD = [[sum(dgi[c][a][b]*dGam[r][a][b] + gi[a, b]*(dG[c][r][a][b] - dG0[c][r][a][b]) for a in R5 for b in R5)
               for r in R5] for c in R5]
        nab = [[dD[n][r] + sum(G0[r][n][l]*Dv[l] for l in R5) for r in R5] for n in R5]
        out = mp.matrix(5, 5)
        for m_ in R5:
            for n in R5:
                out[m_, n] = Ric[m_, n] - (sum(g[m_, r]*nab[n][r] for r in R5)
                                           + sum(g[n, r]*nab[m_][r] for r in R5))/2
        return out


def b5():
    print("B5  the commuted equations' structure: the differentiated identities (60 digits)")
    mp.mp.dps = 60
    h, k = h_explicit(), k_explicit()
    Zh, Zk, dth, dtk = zop(h), zop(k), dtop(h), dtop(k)
    G = gb0(MUS) + h + ES[0]*Zh + ES[1]*k + ES[2]*Zk + ES[3]*dth + ES[4]*dtk
    op = Op(G, gb0(MUS))
    dl = mp.mpf(10)**-15
    mu0 = mp.mpf("0.8")
    c = [V1, 0, 0, 0, 0]

    def E(**kw):
        v = [mp.mpf(0)]*5
        for key, val in kw.items():
            v[int(key[1]) - 1] = val
        return v

    def DPk(X, m=mu0):
        return (op.P(X, m, E(e2=dl)) - op.P(X, m, E(e2=-dl)))/(2*dl)

    worst1, worst2, size, ctl1, ctl2 = mp.mpf(0), mp.mpf(0), mp.mpf(0), mp.mpf(10)**9, mp.mpf(10)**9
    for X in ([mp.mpf("0.4"), mp.mpf("1.3"), mp.mpf("-0.6"), mp.mpf("0.9"), mp.mpf("1.1")],
              [mp.mpf("-0.8"), mp.mpf("0.7"), mp.mpf("1.4"), mp.mpf("-0.5"), mp.mpf("0.6")]):
        Xs = lambda s: [mp.mpf(c[a]) + s*(X[a] - mp.mpf(c[a])) for a in R5]
        base = DPk(X)
        ZDP = (DPk(Xs(1 + dl)) - DPk(Xs(1 - dl)))/(2*dl)
        DPZk = (op.P(X, mu0, E(e3=dl)) - op.P(X, mu0, E(e3=-dl)))/(2*dl)
        D2 = (op.P(X, mu0, E(e1=dl, e2=dl)) - op.P(X, mu0, E(e1=dl, e2=-dl)) - op.P(X, mu0, E(e1=-dl, e2=dl))
              + op.P(X, mu0, E(e1=-dl, e2=-dl)))/(4*dl**2)
        dmu = (DPk(X, mu0 + dl) - DPk(X, mu0 - dl))/(2*dl)
        lhs = ZDP + 2*base
        rhs = DPZk + D2 - 2*mu0*dmu
        worst1 = max(worst1, mp.mnorm(lhs - rhs, 1))
        size = max(size, mp.mnorm(lhs, 1), mp.mnorm(D2, 1))
        ctl1 = min(ctl1, mp.mnorm(lhs - (DPZk - 2*mu0*dmu), 1))
        Xt = lambda s: [X[0] + s] + X[1:]
        dtDP = (DPk(Xt(dl)) - DPk(Xt(-dl)))/(2*dl)
        DPdtk = (op.P(X, mu0, E(e5=dl)) - op.P(X, mu0, E(e5=-dl)))/(2*dl)
        D2t = (op.P(X, mu0, E(e4=dl, e2=dl)) - op.P(X, mu0, E(e4=dl, e2=-dl)) - op.P(X, mu0, E(e4=-dl, e2=dl))
               + op.P(X, mu0, E(e4=-dl, e2=-dl)))/(4*dl**2)
        worst2 = max(worst2, mp.mnorm(dtDP - DPdtk - D2t, 1))
        ctl2 = min(ctl2, mp.mnorm(dtDP - DPdtk, 1))
    check("B5a (Z + 2) DP(h)[k] = DP(h)[Z k] + D^2P(h)[Z h, k] - 2 mu d_mu DP(h)[k], 15 components, two points",
          worst1 < mp.mpf(10)**-20, "max |defect| " + mp.nstr(worst1, 3) + " against terms up to " + mp.nstr(size, 3))
    check("B5b d_t (DP(h)[k]) = DP(h)[d_t k] + D^2P(h)[d_t h, k]", worst2 < mp.mpf(10)**-20,
          "max |defect| " + mp.nstr(worst2, 3))
    check("B5c control: without D^2P(h)[Z h, k] the first fails at every point", ctl1 > mp.mpf(10)**-4,
          "min defect " + mp.nstr(ctl1, 3))
    check("B5d control: without D^2P(h)[d_t h, k] the second fails at every point", ctl2 > mp.mpf(10)**-4,
          "min defect " + mp.nstr(ctl2, 3))


# ---------------------------------------------------------------- B6: the kernel table

def kernels(a):
    half = sp.Rational(1, 2)
    return {
        "residual P(Sigma) = O(lam r^(-13/2)), L^2 with weight": sp.Rational(9, 2) - a,
        "explicit coefficients on d Gamma h_R ((lam + mu) r^-3)": sp.Integer(3),
        "explicit coefficients on d d Gamma^beta h_R (lam r^-2, |beta| < |alpha|)": sp.Integer(2),
        "explicit zero order with Hardy (lam r^-4 * r)": sp.Integer(3),
        "first order h_R coefficients (Q, Gamma[g], deformation: eps r^(-3/2-a))": sp.Rational(3, 2) + a,
        "zero order h_R with Hardy (r d d h_R <= eps r^(-1/2-a))": a + half,
        "bulk-sign error |w'||H|/w (r^-1 (lam r^-2 + eps r^(-1/2-a)))": sp.Min(3, sp.Rational(3, 2) + a),
        "mu d_mu second-order source (mu r^-2 d d Gamma^beta h_R)": sp.Integer(2),
        "multilinear terms: one L^2 factor, sup factors eps r^(-3/2-a) or eps r^(-1/2-a) r^-1 with Hardy":
            sp.Rational(3, 2) + a,
    }


def b6():
    print("B6  the kernel table of the weighted energy at weight a")
    ok = True
    for av in (sp.Rational(51, 20), sp.Rational(11, 4), sp.Rational(59, 20)):
        ok = ok and all(integrable(q) for q in kernels(av).values())
    check("B6a every kernel is integrable at a = 51/20, 11/4, 59/20 (R3.6's window (5/2, 3))", ok,
          str({kk[:40]: str(v) for kk, v in kernels(sp.Rational(11, 4)).items()}))
    grid = [sp.Rational(n, 100) for n in range(0, 501)]
    good = [av for av in grid if all(integrable(q) for q in kernels(av).values())]
    check("B6b on the grid a = 0, 1/100, ..., 5 the kernels are all integrable exactly for a in (1/2, 7/2)",
          min(good) == sp.Rational(51, 100) and max(good) == sp.Rational(349, 100) and
          len(good) == 349 - 51 + 1, f"[{min(good)}, {max(good)}], {len(good)} points")
    bad1 = [kk for kk, q in kernels(sp.Rational(1, 2)).items() if not integrable(q)]
    bad2 = [kk for kk, q in kernels(sp.Rational(7, 2)).items() if not integrable(q)]
    check("B6c control: at a = 1/2 the zero-order h_R kernel is not integrable", len(bad1) == 1 and "zero order h_R"
          in bad1[0], str(bad1))
    check("B6d control: at a = 7/2 the residual kernel is not integrable", len(bad2) == 1 and "residual" in bad2[0],
          str(bad2))


# ---------------------------------------------------------------- B7: the split of the commuted multilinear terms

def compositions(total, m):
    """tuples of m integers >= 1 with the given total"""
    if m == 1:
        yield (total,)
        return
    for first in range(1, total - m + 2):
        for rest in compositions(total - first, m - 1):
            yield (first,) + rest


def split_terms(k0, sobolev=3, avail=None, reverse=False):
    """every multilinear term at level |alpha| <= k0 has a split; avail = the highest energy order available for
    the sup factors (k0, or k0 - 1 in the tame induction)"""
    avail = k0 if avail is None else avail
    for tot in range(2, k0 + 1):
        for m in range(2, min(tot, 4) + 1):
            for comp in compositions(tot, m):
                for two in range(m):            # the slot with two derivatives (or none: two = -1 below)
                    for dvec in ((0,)*m,):
                        pass
                    ds = [1]*m
                    ds[two] = 2
                    for zero in range(-1, m):   # one slot may be undifferentiated (the coefficient slot)
                        dd = list(ds)
                        if zero >= 0 and zero != two:
                            dd[zero] = 0
                        def l2_ok(i):
                            o = comp[i] + (1 if dd[i] == 2 else 0)
                            return o <= k0
                        def sup_ok(i):
                            return comp[i] + sobolev + (1 if dd[i] == 2 else 0) <= avail
                        order = sorted(range(m), key=lambda i: comp[i] + (1 if dd[i] == 2 else 0))
                        cand = order[:1] if reverse else order[::-1]
                        if not any(l2_ok(i) and all(sup_ok(j) for j in range(m) if j != i) for i in cand):
                            return False
    return True


def b7():
    print("B7  the split of the commuted multilinear terms")
    ks = [k for k in range(2, 61) if split_terms(k)]
    mink = min(k for k in range(2, 61) if all(split_terms(kk) for kk in range(k, 61)))
    check("B7a every multilinear term has a split (largest slot in L^2, the rest in sup) for every k0 in [7, 60]; "
          "minimal k0 = 7", mink == 7, f"minimal k0 = {mink}")
    tame = all(split_terms(k, avail=k - 1) for k in range(9, 61))
    check("B7b the tame induction above k1: with the sup factors at energy order <= k - 1 every term splits for "
          "k = 9..60 (so the orders above k1 = d_1 + c need no smallness, only the lower ones)", tame)
    check("B7c control: k0 = 6 fails", not split_terms(6))
    check("B7d control: the rule reversed (smallest slot in L^2, largest in sup) fails at every k0 <= 60",
          not any(split_terms(k, reverse=True) for k in range(7, 61)))


# ---------------------------------------------------------------- B8: the residual's degree

def b8():
    print("B8  the degree of the residual P(g_b0 + Sigma)")
    half = Fr(1, 2)

    def residual_degrees(Pi):
        terms = []
        for p in Pi:                        # flat part: degree -p - 2, cancelled by construction for each p
            terms.append(("mu", -p - 4))    # the mu part of the linear operator: relative degree -2
        for i, p in enumerate(Pi):          # quadratic: -p - q - 2; cubic: -p - q - s - 2
            for q in Pi[i:]:
                terms.append(("quad", -p - q - 2))
                for s in Pi:
                    terms.append(("cubic", -p - q - s - 2))
        cancelled = {-6} if 4 in Pi else set()  # Sigma_4 solves the degree -6 equation with mu Sigma_2, Sigma_2^2
        return max(d for _, d in terms if d not in cancelled)

    Pi = [Fr(2), Fr(5, 2), Fr(3), Fr(7, 2), Fr(4)]
    d = residual_degrees(Pi)
    check("B8a with p in {2, 5/2, 3, 7/2, 4} the residual's leading degree is -13/2 (mu Sigma_(5/2), Sigma_2 "
          "Sigma_(5/2))", d == Fr(-13, 2), str(d))
    a, R = sp.symbols("a R", positive=True)
    r = sp.Symbol("r", positive=True)
    l2 = sp.sqrt(sp.integrate(r**(2*a)*r**(-13)*r**3, (r, R, sp.oo), conds="none"))
    check("B8b ||w^(1/2) r^(-13/2)||_(L^2(r >= R)) = R^(a - 9/2)/sqrt(9 - 2a)",
          sp.simplify(l2 - R**(a - sp.Rational(9, 2))/sp.sqrt(9 - 2*a)) == 0)
    d2 = residual_degrees([Fr(2), Fr(5, 2), Fr(3), Fr(7, 2)])
    check("B8c control: without the p = 4 term the leading degree is -6", d2 == Fr(-6), str(d2))


# ---------------------------------------------------------------- B9: the self-similar terms

def b9():
    print("B9  the self-similar terms and the fixed-v expansion")
    p, l, m = sp.symbols("p l m")
    lhs = (p + m - 1)*(p + m - 3) - l*(l + 2)
    rhs = (p + m - l - 3)*(p + m + l - 1)
    check("B9a (p + m - 1)(p + m - 3) - l(l + 2) = (p + m - l - 3)(p + m + l - 1) (symbolic)",
          sp.expand(lhs - rhs) == 0)
    # the ratio of consecutive Taylor coefficients of 2F1(p+l, p-l-2; c; s/2) is (p+l+m-1)(p-l+m-3)/(2 m (c+m-1));
    # the recursion gives (Delta + (q-1)(q-3))/(m (2q - 3)), q = p + m: equal iff c = p - 1/2
    cc = sp.Symbol("c")
    hyp = (p + l + m - 1)*(p - l + m - 3)/(2*m*(cc + m - 1))
    rec = rhs/(m*(2*(p + m) - 3))
    check("B9a' the 2F1 coefficient ratio equals the recursion's exactly at c = p - 1/2",
          sp.simplify((hyp - rec).subs(cc, p - sp.Rational(1, 2))) == 0)
    check("B9a'' control: c = p + 1/2 (round 1's C1) breaks it", sp.simplify((hyp - rec).subs(cc, p + sp.Rational(1, 2)))
          != 0)
    v = sp.Symbol("v")
    Lap = sp.Symbol("Lap")  # Delta on a harmonic: -l(l + 2)
    G = {3: sp.Integer(0), 4: sp.Symbol("G4"), 5: sp.Symbol("G5")}
    ok = True
    for k in range(6, 17):
        q = sp.Rational(k, 2)
        dG = (Lap + (q - 1)*(q - 3))*G[k - 2]/(2*q - 3)
        G[k] = sp.integrate(dG, v) + sp.Symbol(f"c{k}")
        deg = sp.degree(sp.expand(G[k]), v)
        ok = ok and deg == (k - 4)//2
    check("B9b after the shell (G_3 = 0, G_4, G_5 constant) the flat recursion makes G_k a polynomial in v of degree "
          "floor((k - 4)/2), k = 6..16 (so Sigma's fixed-v expansion reproduces it, by B9a)", ok)
    mp.mp.dps = 30
    ok3 = True
    info = []
    for pv in (2, 2.5, 3, 3.5):
        maxes = []
        for lv in (10, 20, 40, 80, 120):
            f = lambda s: abs(mp.hyp2f1(pv + lv, pv - lv - 2, pv - 0.5, s/2))
            maxes.append(max(f(mp.mpf(i)/40) for i in range(0, 61)))
        slopes = [mp.log(maxes[i + 1]/maxes[i])/mp.log(mp.mpf(2) if i < 3 else mp.mpf(1.5)) for i in range(4)]
        info.append((pv, mp.nstr(max(slopes), 3)))
        ok3 = ok3 and max(slopes) < 6
    check("B9c max_(s in [0, 3/2]) |2F1(p + l, p - l - 2; p - 1/2; s/2)| grows at most like a power of l (log-log "
          "slope < 6, l = 10..120): the harmonic-by-harmonic construction of F_p converges for smooth data", ok3,
          str(info))


# ---------------------------------------------------------------- B10: the a_0 < 1/2 scheme

def b10():
    print("B10  the weight a_0 < 1/2 scheme of rounds 2-3 does not close")
    a0 = sp.Symbol("a0", positive=True)
    chain = a0 + sp.Rational(1, 2)
    check("B10a the scheme's chain (Hardy on Gamma^alpha h, Sobolev on d d h) gives the kernel exponent a_0 + 1/2: "
          "not integrable at a_0 = 1/4, 2/5, 1/2", all(not integrable(chain.subs(a0, c)) for c in
                                                       (sp.Rational(1, 4), sp.Rational(2, 5), sp.Rational(1, 2))))
    r, R, a = sp.symbols("r R a", positive=True)
    y = r - R
    psi = (y*(1 - y))**2
    phi = R**(-a - sp.Rational(3, 2))*psi
    en = sp.integrate(sp.expand(r**3*sp.diff(phi, r)**2*R**(2*a)), (r, R, R + 1))
    # the weighted energy uses r^(2a) <= (R + 1)^(2a) on the band; with R^(2a) in place: bounded and -> int psi'^2
    lim = sp.limit(en.subs(a, sp.Rational(1, 4)), R, sp.oo)
    val = (R**(a + sp.Rational(3, 2))*phi).subs(r, R + sp.Rational(1, 2))
    check("B10b Sobolev's bound is attained in the class: phi_R = R^(-a-3/2) psi(r - R) (psi = (y(1 - y))^2) has "
          "weighted energy -> int psi'^2 = 1/105 and R^(a + 3/2) phi_R(R + 1/2) = psi(1/2) = 1/16",
          lim == sp.Rational(1, 105) and sp.simplify(val - sp.Rational(1, 16)) == 0, f"limit {lim}")
    eta = sp.Symbol("eta", positive=True)
    ph2 = r**(-a - 1 - eta)
    ratio = sp.simplify(sp.integrate(r**(2*a + 1)*ph2**2, (r, R, sp.oo), conds="none") /
                        sp.integrate(r**(2*a + 3)*sp.diff(ph2, r)**2, (r, R, sp.oo), conds="none"))
    check("B10c Hardy's constant is attained: the ratio for r^(-a-1-eta) tends to (a + 1)^-2 as eta -> 0",
          sp.limit(ratio, eta, 0) == 1/(a + 1)**2)
    check("B10d control: at a = 11/4 (the weight of (b2)) the same chain is integrable",
          integrable(chain.subs(a0, sp.Rational(11, 4))))


# ---------------------------------------------------------------- B11, B12: uniqueness and the limit

def b11():
    print("B11  uniqueness in the weight-a_0 class")
    a0s = (sp.Rational(1, 10), sp.Rational(1, 4), sp.Rational(49, 100))
    av = sp.Rational(11, 4)
    ok = True
    for a0 in a0s:
        qs = [sp.Min(3, av + sp.Rational(1, 2)), sp.Rational(3, 2) + a0, sp.Rational(3, 2) + a0]
        ok = ok and all(integrable(q) for q in qs)
    check("B11a the difference equation's kernels: zero order from the constructed solution (q = min(3, a + 1/2)), "
          "first order, deformation and bulk-sign error from h' (q = 3/2 + a_0): integrable for a_0 = 1/10, 1/4, 49/100",
          ok)
    r, S = sp.symbols("r S", positive=True)
    capS = [sp.integrate(r**(2*a0)*(r**-3)**2*r**3, (r, S, sp.oo)) for a0 in a0s]
    check("B11b Sigma's cap energy at weight a_0: int_S^oo r^(2a_0) r^-6 r^3 = S^(2a_0 - 2)/(2 - 2a_0) -> 0",
          all(sp.limit(c, S, sp.oo) == 0 for c in capS))
    check("B11c control: with the zero-order coefficient taken from h' (q = a_0 + 1/2) the kernel is not integrable "
          "at a_0 = 1/4, 1/2", not integrable(sp.Rational(3, 4)) and not integrable(1))


def b12():
    print("B12  the limit T -> -oo")
    a, T, r, s = sp.symbols("a T r s", positive=True)
    tails = {"N-flux beyond |T| (h_R = O(r^(-9/2)), ell-gain: tangential r^(-11/2))":
             sp.integrate(r**(2*a)*r**-11*r**3, (r, T, sp.oo), conds="none"),
             "cap (band, unit width, d h_R = O(r^(-9/2)))": sp.integrate(r**(2*a)*r**-9*r**3, (r, T, T + 1)),
             "residual tail int_(|T|)^oo s^(a - 9/2) ds": sp.integrate(s**(a - sp.Rational(9, 2)), (s, T, sp.oo),
                                                                       conds="none")}
    ok = True
    for av in (sp.Rational(51, 20), sp.Rational(11, 4), sp.Rational(59, 20)):
        ok = ok and all(sp.limit(e.subs(a, av), T, sp.oo) == 0 for e in tails.values())
    check("B12a every tail tends to 0 as T -> -oo at a = 51/20, 11/4, 59/20", ok,
          str({k[:30]: str(sp.simplify(v)) for k, v in tails.items()}))
    bad = sp.integrate(s**(sp.Rational(7, 2) - sp.Rational(9, 2)), (s, T, sp.oo), conds="none")
    check("B12b control: at a = 7/2 the residual tail is infinite", bad in (sp.oo, sp.zoo) or not bad.is_finite,
          str(bad))


# ---------------------------------------------------------------- B13: the means

def b13():
    print("B13  the means at past null infinity: no logarithm at any order")
    half = Fr(1, 2)
    # coefficient classes of the count of Theorem A_P (exponents of r^-1): W 3/2, chi 2, m 2, gh 2, phi 1,
    # ell phi 2, g0 - eta 2, Gamma[g0] 2 (mu' part) or 3, the operators ell and r^-1 Omega add 1, d_v adds 0
    # sources of (a) and (c): products of >= 2 profile factors or one factor with box~/Gamma: exponents >= 3;
    # (b): ell phi = (1/2)(m(ell, ell) + q): exponents >= 2.  Higher orders: exponents add halves.
    src_ac = {Fr(3) + j*half for j in range(0, 19)}
    src_b = {Fr(2) + j*half for j in range(0, 21)}
    wave_ok = all(2*q - 5 != 0 for q in src_ac)
    tr_ok = all(q - Fr(5, 2) != 0 for q in src_ac)
    phi_ok = all(q - 1 != 0 for q in src_b)
    # closure: the outputs (q - 1) feed the next order's sources only through products with exponents >= 3/2
    outs = {q - 1 for q in src_ac} | {q - 1 for q in src_b}
    prods = {o + Fr(3, 2) for o in outs}
    check("B13a the stage sources start at q = 3 ((a), (c)) and q = 2 ((b)); 2/(2q - 5), 1/(q - 5/2), 1/(q - 1) are "
          "finite at every exponent to 12, and products of outputs with the coefficient classes (>= 3/2) stay >= 5/2 "
          "for the transports' inputs", wave_ok and tr_ok and phi_ok and min(prods) >= Fr(5, 2) and
          all(q in src_ac or q < 3 for q in prods if q <= 12))
    check("B13b control: a source at q = 5/2 would give 2/(2q - 5) = 1/0 (a logarithm)", 2*Fr(5, 2) - 5 == 0)


def main():
    for f in (b3, b4, b6, b7, b8, b9, b10, b11, b12, b13, b1, b2, b5):
        f()
    print("FAILED:", FAIL if FAIL else "none")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
