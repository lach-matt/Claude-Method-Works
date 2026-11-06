#!/usr/bin/env python3
"""gdlge2_5.py -- GAUGEDECAY5.md Rounds 8-9: the input (M), I.C's (G), (Z) and (TF) for the 1-form wave operator Box of
five-dimensional Tangherlini restricted to the 1-forms with no l = 0 and no l = 1 part (the l >= 2 subspace; the class
1-forms with no l = 0 part lie in it), at the b-weights alpha + 2 in (-1, 0]; and the bookkeeping of the rate of the
l >= 2 part of the harmonic-gauge representative that (M) gives.  Every check has a control that mutates the computed
path and must fail (round 9: L6's and L9's controls now do; GAUGEDECAY5 section R9.0).

Background as in rwgauge5.py and hgauge5.py: the ingoing chart (v, r, th, phi1, phi2), g = -f dv^2 + 2 dv dr + r^2
gamma, f = 1 - mu/r^2, mu = s^2 = r_h^2, Box := 2 delta G delta^* = d delta + delta d on 1-forms, the zero-energy
operator P-hat(0) = Box on stationary 1-forms (t_* - v is a function of r).  Scalar harmonics S with Lap S = -kappa S,
kappa = l(l + 2); vector harmonics Y (co-closed 1-forms on S^3) with delta d Y = lambda Y, lambda = (l + 1)^2.

  L1 (exact) The mode reduction.  For the scalar type omega = a S dv + b S dr + c dS (a, b, c functions of r, kappa
     symbolic), Box omega = E_v S dv + E_r S dr + E_th dS with
         r^3 E_v = -[ r (r^2 - mu) a'' + 3 (r^2 - mu) a' - kappa r a ],
         r^4 E_r = -[ r^2 (r^2 - mu) b'' + (3 r^3 + mu r) b' - (kappa r^2 + 3 r^2 - 3 mu) b + 2 kappa r c - 3 r^2 a ],
         r^3 E_th = -[ r (r^2 - mu) c'' + (r^2 + mu) c' - kappa r c + 2 r^2 a + 2 (r^2 - mu) b ];
     delta omega = -r^-3 [ (r^3 a)' + (r^3 f b)' - kappa r c ] S; and (delta d omega) = M_v S dv + M_r S dr + M_th dS
     with r^3 M_v = -[ f (r^3 a')' - kappa r a ], r^2 M_r = kappa (b - c') + (r^3 a')'/r, r M_th = (r a - r f e)',
     e := c' - b.  For the vector type omega = psi Y, Box omega = -r^-2 [ r (r f psi')' - lambda psi ] Y.  Derived on
     T^2-invariant representatives with the eigen-relation substituted, and cross-validated on explicit harmonics
     that are not T^2-invariant (scalar l = 1, 3; vector l = 2) and on S = cos 2 th (l = 2).  Control: the
     cross-validation with E_r's coupling 2 kappa r c replaced by 3 kappa r c fails.
  L2 (exact) (G) on the subspace: the indicial roots at infinity (u ~ rho^lam in Cartesian components: a, b ~
     r^-lam, c ~ r^(1 - lam), psi ~ r^(1 - lam)).  Scalar type l: the determinant of the indicial matrix is
     (lam + l + 1)(lam + l)(lam + l - 1)(lam - l - 1)(lam - l - 2)(lam - l - 3), the flat roots -m, m + 2 of the
     Cartesian degrees m = l - 1, l, l + 1; vector type l: (lam + l)(lam - l - 2), degree m = l.  For every l >= 2
     every root is <= -1 or >= 3 (vector: <= -2 or >= 4): (-1, 3) is an indicial gap of the restricted operator,
     uniformly in l.  Round 9: the gap test runs on the roots of the computed determinants, sorted by their sign in
     l, not on typed lists.  Control: the full bundle (l = 0: roots -1, 0, 2, 3; l = 1 scalar: -2, -1, 0, 2, 3, 4)
     has the root 0 in (-1, 0].
  L3 (exact) The divergence step.  delta Box = Box_0 delta on the modes; psi := delta omega solves (r^3 f psi')' =
     kappa r psi, which in x = r^2/mu is Legendre's equation d/dx[x (x - 1) psi_x] = (l/2)(l/2 + 1) psi, solved by
     P_{l/2}(2x - 1), regular at the horizon, growing like r^l (l = 0, 2, ..., 10); Frobenius roots at infinity
     rho^(l + 2), rho^-l; the energy identity d/dr[r^3 f psi psi'] = r^3 f psi'^2 + kappa r psi^2 on solutions; psi =
     O(rho^(beta + 1)), beta > -1, excludes rho^-l for every l >= 0.  Control: the identity with the weight r^2 in
     place of r^3 fails.
  L4 (exact) The Maxwell step.  For the scalar type the Maxwell equations delta F = 0, F = d omega, are e = a/f and
     f (r^3 a')' = kappa r a; W := r^3 a' solves R[W] := (f W'/r)' - kappa W/r^3 = 0, and Phi := r^(-1/2) W solves f
     (f Phi')' = V_2 Phi, V_2 = (f/r^2)(kappa + 3/4 - 7 mu/(4 r^2)) > 0 for kappa >= 3 on r > r_h; for the vector type
     Phi := r^(1/2) psi solves f (f Phi')' = V_1 Phi, V_1 = (f/r^2)(lambda - 1/4 + 5 mu/(4 r^2)) > 0; the roots at
     infinity W ~ r^(l + 2), r^-l and psi ~ r^(l + 1), r^-(l + 1), so Phi ~ r^(l + 3/2), r^-(l + 1/2) in both types;
     the growth Phi = O(r^(3/2 - beta)), beta > -1, excludes r^(l + 3/2) for l >= 1; the energy identity of the
     Liouville form.  Closed forms: the horizon-regular electrostatic potentials a = (x - 1) Q_l(x) (l = 2, ..., 8,
     Q_l a polynomial of degree l/2 - 1) and the vector solutions 2F1((l+1)/2, -(l+1)/2; 1; 1 - x) (l = 1, 3, 5, 7)
     grow like r^l and r^(l + 1).  Control: at l = 0 the Coulomb field a = 1/r^2 (that of W*) is horizon-regular and
     decaying, and V_2 is negative near the horizon.
  L5 (exact, whole box) The gauge step: the closed part d phi with phi = O(r^(1 - beta)) excludes the growing branch
     r^l iff l > 1 - beta, which holds for l >= 2 on beta in (-1, 0].  Control: at l = 1 (the translations' dual
     forms, O(1)) it fails.
  L6 (exact) A cross-check of the kernel for l = 2, 4, 6, 8 on the coupled 3 x 3 system, not using L3-L5: at the
     horizon the formal power-series solutions are parametrised by (a'(r_h), b(r_h), c(r_h)) (the order-k matrix is
     k diag(2k - 2, 2k + 2, 2k), invertible for k >= 2, and order 0 forces a(r_h) = 0), and three explicit polynomial
     solutions realise those jets; no nonzero combination has Cartesian growth below r^1 (they grow like r^(l - 1),
     r^l, r^(l + 1)).  The method needs polynomial solutions, so even l (at odd l the horizon-regular potentials are
     non-terminating hypergeometric series); every l is gdr9_5.py N5.  Control (round 9): L6's own path with E_r's
     coupling 3 kappa r c, and with the growth threshold raised to r^l, must fail both times.
  L7 (exact) The subspace.  The Cartesian components (in dt_*, dx^1, ..., dx^4) of the class forms S dv, S dr, dS (S
     = P_j(cos 2 th), l = 2j = 2, 4) have zero spherical means, the horizon functional ell vanishes on them, and the
     G-average of a constant spatial covector is 0: the degree-0 harmonics, which carry the roots 0 and 2, are
     absent.  Control: dv has spherical mean 1 and ell(dv) = 2 pi^2 r_h^3.
  L8 (exact, whole box) (TF) on the subspace: N_tf(sigma) = e^(-i sigma r) (Lap_e - sigma^2) e^(i sigma r) on each
     degree-l component reduces to Bessel's equation of order l + 1 (I.C Lemma 5.4 (a)), with exponents l and -l - 2
     at ztf; a kernel element ~ r^(-l-2) is not in X_tf (b-weight q - 2 at ztf, q = 2 - beta) iff l + q >= 0, and
     an adjoint element ~ r^(-l-2) is not in X*_tf,0 (b-weight -q) iff q <= l + 2: both for every degree l >= 1 and
     beta in (-1, 3) (round 9: l = 1 checked separately, the box l = 1 + n having n > 0).  Control: at l = 0 and
     beta in (-1, 0) the adjoint condition fails (the full bundle).
  L9 (exact, whole box) The l >= 2 version of Theorem R6.4 with the window gamma_+ - alpha_K in (-1, 0): its
     conditions for alpha_K in (1, 3/2 + delta_#) on three sub-boxes ((1, 3/2), {3/2}, (3/2, 3/2 + delta_#)), each a
     positive sum; round 9 adds the hypotheses of III.I'' Lemmas 4.1-4.2 and II.G' Propositions 3.3 (1) and 3.5 (1)
     with w_I = max(5/2, gamma_+ + 1 + eps_1), eps_1, eps and eps_PP = min(eps, eps_1) encoded (28 conditions), and
     that the box reaches sup alpha_K = 3/2 + delta_#.  Control: the same conditions with the full bundle's window
     and (Z)-weight in (0, 1) fail on the box.
  L10 (exact, whole box) The rates: the representative settles at t^-alpha for every alpha < min(p_0, 3/2), above
     Corollary R5.3's 1/2 + delta_#; for the data of the paper's section 8.8 (p_0 = 1) at t^(-1+eps); for data with
     compact support at t^(-3/2-kappa), kappa < delta_#.  Round 9: the l >= 2 exponent is the supremum of alpha_K
     over L9's box, computed.  Control: with R5.3's l >= 2 exponent the paper's t^(-1+eps) fails.

Labels: computed (exact, sympy; no floating point).
Run: python3 checks/gdlge2_5.py   (several minutes under load)
"""
import sys

import sympy as sp

from gdrad5 import positive_sum
from hgauge5 import GEO, delta1, dform, hodge
from rwgauge5 import N, X, mu, p1, p2, r, s, th, v

HALF = sp.Rational(1, 2)
_print = print


def print(*args, **kw):                                         # report lines wrapped at 121 characters
    import textwrap
    text = ' '.join(str(a_) for a_ in args)
    _print('\n'.join(textwrap.fill(ln, 121, subsequent_indent='      ', break_on_hyphens=False) if ln else ln
                     for ln in text.split('\n')), **kw)


kap, lam_, l_ = sp.symbols('kappa lambda l', positive=True)
F_ = 1 - mu/r**2
gam = sp.diag(1, sp.cos(th)**2, sp.sin(th)**2)
gami = gam.inv()
SPH = [th, p1, p2]
sqg = sp.sin(th)*sp.cos(th)


def lap_s3(u):
    return sp.simplify(sum(sp.diff(sqg*gami[i, i]*sp.diff(u, SPH[i]), SPH[i]) for i in range(3))/sqg)


def zero(e):
    e = sp.expand(e)
    if e == 0 or sp.simplify(e) == 0:
        return True
    return sp.simplify(sp.expand_trig(e)) == 0


# ------------------------------------------------------------------------------------------------- the mode systems
def sys_scalar(a, b, c, k, m=mu):
    """(E_v, E_r, E_th) of L1, for functions a, b, c of r"""
    d = sp.diff
    Ev = -(r*(r**2 - m)*d(a, r, 2) + 3*(r**2 - m)*d(a, r) - k*r*a)/r**3
    Er = -(r**2*(r**2 - m)*d(b, r, 2) + (3*r**3 + m*r)*d(b, r) - (k*r**2 + 3*r**2 - 3*m)*b + 2*k*r*c - 3*r**2*a)/r**4
    Eth = -(r*(r**2 - m)*d(c, r, 2) + (r**2 + m)*d(c, r) - k*r*c + 2*r**2*a + 2*(r**2 - m)*b)/r**3
    return [Ev, Er, Eth]


def sys_scalar_mut(a, b, c, k, m=mu):
    Ev, Er, Eth = sys_scalar(a, b, c, k, m)
    return [Ev, Er - k*c/r**3, Eth]                             # 2 kappa r c -> 3 kappa r c in r^4 E_r


def div_scalar(a, b, c, k, m=mu):
    f = 1 - m/r**2
    return -(sp.diff(r**3*a, r) + sp.diff(r**3*f*b, r) - k*r*c)/r**3


def maxwell_scalar(a, b, c, k, m=mu):
    f = 1 - m/r**2
    e = sp.diff(c, r) - b
    Mv = -(f*sp.diff(r**3*sp.diff(a, r), r) - k*r*a)/r**3
    Mr = (k*(b - sp.diff(c, r)) + sp.diff(r**3*sp.diff(a, r), r)/r)/r**2
    Mth = sp.diff(r*a - r*f*e, r)/r
    return [Mv, Mr, Mth]


def sys_vector(psi, lm, m=mu):
    f = 1 - m/r**2
    return -(r*sp.diff(r*f*sp.diff(psi, r), r) - lm*psi)/r**2


def box0_mode(ph, k, m=mu):
    """Box_0 = -nabla^a nabla_a on ph(r) S, stationary, ingoing chart: -r^-3 (r^3 f ph')' + kappa ph/r^2"""
    f = 1 - m/r**2
    return -sp.diff(r**3*f*sp.diff(ph, r), r)/r**3 + k*ph/r**2


# ------------------------------------------------------------------------------------------------------------- L1
def reduce_symbolic(expr, S, rule2, mons):
    """substitute S'' (and S''') by the eigen-relation and return the coefficients of S, S' (as symbols mons)"""
    e = expr.subs(sp.Derivative(S, (th, 3)), sp.diff(rule2, th))
    for _ in range(2):
        e = e.subs(sp.Derivative(S, (th, 2)), rule2)
    s0, s1 = mons
    e = sp.expand(e.subs(sp.Derivative(S, th), s1).subs(S, s0))
    out = [sp.simplify(sp.expand_trig(e.coeff(mm))) for mm in (s0, s1)]
    rest = sp.simplify(e - out[0]*s0 - out[1]*s1)
    return out, rest


def l1(control=False):
    sysf = sys_scalar_mut if control else sys_scalar
    a, b, c = [sp.Function(n)(r) for n in ("a", "b", "c")]
    S = sp.Function("S")(th)
    s0, s1 = sp.symbols("S0 S1")
    rule = -kap*S - 2*sp.cos(2*th)/sp.sin(2*th)*sp.diff(S, th)       # Lap S = -kappa S for T^2-invariant S
    w = [a*S, b*S, c*sp.diff(S, th), 0, 0]
    Hw = hodge(GEO, w)
    E = sysf(a, b, c, kap)
    ok = zero(Hw[3]) and zero(Hw[4])
    want = [(E[0], 0), (E[1], 0), (0, E[2])]
    for i in range(3):
        (cS, cSp), rest = reduce_symbolic(Hw[i], S, rule, (s0, s1))
        ok &= zero(cS - want[i][0]) and zero(cSp - want[i][1]) and rest == 0
    de = delta1(GEO, w)
    (cS, cSp), rest = reduce_symbolic(de, S, rule, (s0, s1))
    ok_div = zero(cS - div_scalar(a, b, c, kap)) and zero(cSp) and rest == 0
    F = dform(w)
    dF = GEO.cov2(F)
    dd = [-sum(GEO.gi[i_, j_]*dF[j_][i_][nu] for i_ in range(N) for j_ in range(N)) for nu in range(N)]
    Mw = maxwell_scalar(a, b, c, kap)
    ok_max = zero(dd[3]) and zero(dd[4])
    wantM = [(Mw[0], 0), (Mw[1], 0), (0, Mw[2])]
    for i in range(3):
        (cS, cSp), rest = reduce_symbolic(dd[i], S, rule, (s0, s1))
        ok_max &= zero(cS - wantM[i][0]) and zero(cSp - wantM[i][1]) and rest == 0
    # vector type, T^2-invariant representative A(th) dphi1 with delta d Y = lambda Y substituted
    A = sp.Function("A")(th)
    psi = sp.Function("psi")(r)
    ruleA = -lam_*A - sp.diff(A, th)/(sp.sin(th)*sp.cos(th))
    Hv = hodge(GEO, [0, 0, 0, psi*A, 0])
    (cA, cAp), rest = reduce_symbolic(Hv[3], A, ruleA, (s0, s1))
    ok_vec = all(zero(Hv[i]) for i in (0, 1, 2, 4)) and zero(cA - sys_vector(psi, lam_)) and zero(cAp) and rest == 0
    # cross-validation on explicit harmonics (scalar l = 1, 2, 3; vector l = 1, 2)
    xs = []
    for l, Sx in ((1, sp.cos(th)*sp.cos(p1)), (2, sp.cos(2*th)),
                  (3, sp.cos(th)**2*sp.sin(th)*sp.cos(p1)*sp.sin(p1)*sp.cos(p2))):
        k = l*(l + 2)
        eig = zero(lap_s3(Sx) + k*Sx)
        dS = [sp.diff(Sx, q) for q in SPH]
        Hx = hodge(GEO, [a*Sx, b*Sx, c*dS[0], c*dS[1], c*dS[2]])
        Ex = sysf(a, b, c, k)
        good = eig and zero(Hx[0] - Ex[0]*Sx) and zero(Hx[1] - Ex[1]*Sx)
        good &= all(zero(Hx[2 + q] - Ex[2]*dS[q]) for q in range(3))
        xs.append(("scalar l=%d" % l, good))
    for l, Yx in ((1, sp.cos(th)**2), (2, sp.sin(th)*sp.cos(th)**2*sp.cos(p2))):
        lm = (l + 1)**2
        # co-closed on S^3 and delta d Y = lambda Y (Y = Yx dphi1; (delta F)_b = -(1/sqg) d_a(sqg F^{ab}) g_bb)
        dY = sp.Matrix(3, 3, lambda i, j: 0)
        Ycomp = [0, Yx, 0]
        for i in range(3):
            for j in range(3):
                dY[i, j] = sp.diff(Ycomp[j], SPH[i]) - sp.diff(Ycomp[i], SPH[j])
        dd_ = [-sum(sp.diff(sqg*gami[i, i]*gami[j, j]*dY[i, j], SPH[i]) for i in range(3))/sqg*gam[j, j]
               for j in range(3)]
        coclosed = zero(sum(sp.diff(sqg*gami[i, i]*Ycomp[i], SPH[i]) for i in range(3)))
        eigv = all(zero(dd_[j] - lm*Ycomp[j]) for j in range(3))
        Hx = hodge(GEO, [0, 0, 0, psi*Yx, 0])
        good = coclosed and eigv and zero(Hx[3] - sys_vector(psi, lm)*Yx) and all(zero(Hx[i]) for i in (0, 1, 2, 4))
        xs.append(("vector l=%d" % l, good))
    ok_x = all(g_ for _, g_ in xs)
    tag = "  L1 control (E_r's coupling 2 kappa r c -> 3 kappa r c)" if control else "  L1"
    print("%s: Box on a S dv + b S dr + c dS reduces to (E_v, E_r, E_th) with kappa symbolic: %s; delta omega: %s; "
          "delta d omega (Maxwell): %s; vector type -r^-2 [r (r f psi')' - lambda psi] Y: %s; cross-validation on "
          "explicit harmonics %s" % (tag, ok, ok_div, ok_max, ok_vec, xs), flush=True)
    return ok and ok_div and ok_max and ok_vec and ok_x


# ------------------------------------------------------------------------------------------------------------- L2
def indicial_scalar(k, with_c=True):
    lam = sp.Symbol('lam')
    A, B, C = sp.symbols('A B C')
    a, b = r**(-lam)*A, r**(-lam)*B
    c = r**(1 - lam)*C if with_c else sp.Integer(0)
    E = sys_scalar(a, b, c, k)
    rows = []
    pw = [2, 2, 1]
    for i, e in enumerate(E if with_c else E[:2]):
        ee = sp.expand(sp.simplify(e*r**(lam + pw[i])))
        ee = sp.expand(ee.subs(s, 0))                       # leading order at r = oo: mu-terms are rho^2-relative
        rows.append([ee.coeff(x) for x in ((A, B, C) if with_c else (A, B))])
    return sp.Matrix(rows), lam


def l2(control=False):
    M, lam = indicial_scalar(kap)
    det_s = sp.factor(sp.expand(M.det().subs(kap, l_*(l_ + 2))))
    want = sp.expand((lam + l_ + 1)*(lam + l_)*(lam + l_ - 1)*(lam - l_ - 1)*(lam - l_ - 2)*(lam - l_ - 3))
    ok_s = sp.simplify(sp.expand(det_s) - want*sp.Poly(det_s, lam).LC()/sp.Poly(want, lam).LC()) == 0
    # round 9 (the round-8 verifier's Minor 6): the root lists of the gap test are the roots of the computed
    # determinants, not typed lists; each root is linear in l, and its sign in l sorts it to the lower or upper side
    roots_s = sp.roots(sp.Poly(sp.expand(det_s), lam))
    mult_s = sum(roots_s.values()) == 6
    flat = set()
    for m in (l_ - 1, l_, l_ + 1):
        flat |= {sp.expand(-m), sp.expand(m + 2)}
    ok_dict = set(sp.expand(x) for x in roots_s) == flat
    # vector type: psi = r^(1 - lam) P
    P = sp.Symbol('P')
    ev = sp.expand(sp.simplify(sys_vector(r**(1 - lam)*P, l_*0 + (l_ + 1)**2)*r**(lam + 1)).subs(s, 0))
    det_v = sp.factor(ev.coeff(P))
    ok_v = sp.simplify(det_v/((lam + l_)*(lam - l_ - 2))).is_number
    roots_v = sp.roots(sp.Poly(sp.expand(det_v), lam))
    mult_v = sum(roots_v.values()) == 2

    def split(rs):                                           # (roots decreasing in l, roots increasing in l, all linear)
        cl = {x_: sp.Poly(sp.expand(x_), l_) for x_ in rs}
        lin = all(P_.degree() == 1 for P_ in cl.values())
        return ([x_ for x_ in rs if cl[x_].coeff_monomial(l_) < 0], [x_ for x_ in rs if cl[x_].coeff_monomial(l_) > 0],
                lin)
    neg, pos, lin_s = split(roots_s)
    negv, posv, lin_v = split(roots_v)
    # uniform gap on the subspace: l = 2 + n, n >= 0
    n = sp.Symbol('n', nonnegative=True)
    def nonneg(e_):                                          # a polynomial in n >= 0 with coefficients >= 0
        P_ = sp.Poly(sp.expand(e_), n)
        return all(cf >= 0 for cf in P_.coeffs())
    gap_s = lin_s and mult_s and len(neg) == 3 and len(pos) == 3
    gap_s &= all(nonneg((-(x_ + 1)).subs(l_, 2 + n)) for x_ in neg)
    gap_s &= all(nonneg((x_ - 3).subs(l_, 2 + n)) for x_ in pos)
    gap_v = lin_v and mult_v and len(negv) == 1 and len(posv) == 1
    gap_v &= all(nonneg((-(x_ + 2)).subs(l_, 2 + n)) for x_ in negv)
    gap_v &= all(nonneg((x_ - 4).subs(l_, 2 + n)) for x_ in posv)
    ends = {sp.Integer(-1), sp.Integer(3)} <= set(x_.subs(l_, 2) for x_ in roots_s)     # the ends are l = 2 roots
    gap_s &= ends
    # the full bundle: l = 0 (2 x 2 system, c absent) and l = 1 scalar
    M0, lam0 = indicial_scalar(0, with_c=False)
    r0 = sorted(sp.roots(sp.Poly(sp.factor(M0.det()), lam0)).keys())
    M1, lam1 = indicial_scalar(3)
    r1 = sorted(sp.roots(sp.Poly(sp.factor(M1.det()), lam1)).keys())
    full = sorted(set(r0) | set(r1))
    in_window = [x for x in full if -1 < x <= 0]
    if control:
        ok = len(in_window) == 0
        print("  L2 control (the full bundle): roots at l = 0 %s, at l = 1 %s; roots in (-1, 0]: %s; root-free: %s"
              % (r0, r1, in_window, ok), flush=True)
        return ok
    print("  L2: scalar det = %s (= the six roots: %s); its computed roots %s are the flat roots -m, m + 2 of m = l - "
          "1, l, l + 1: %s; vector det %s: %s, roots %s; for l >= 2 every computed scalar root <= -1 or >= 3 (the ends "
          "-1, 3 roots at l = 2): %s, vector <= -2 or >= 4: %s; so (-1, 3) is an indicial gap of the restricted "
          "operator, uniformly in l" % (det_s, ok_s, sorted(roots_s, key=str), ok_dict, det_v, ok_v,
                                       sorted(roots_v, key=str), gap_s, gap_v), flush=True)
    return ok_s and ok_dict and ok_v and gap_s and gap_v


# ------------------------------------------------------------------------------------------------------------- L3
def l3(control=False):
    a, b, c = [sp.Function(n)(r) for n in ("a", "b", "c")]
    E = sys_scalar(a, b, c, kap)
    # delta of (E_v S dv + E_r S dr + E_th dS) against Box_0 of delta omega
    lhs = div_scalar(E[0], E[1], E[2], kap)
    rhs = box0_mode(div_scalar(a, b, c, kap), kap)
    ok_comm = zero(lhs - rhs)
    ph = sp.Function("phi")(r)
    wt = r**2 if control else r**3
    ode = sp.diff(r**3*F_*sp.diff(ph, r), r) - kap*r*ph
    ident = sp.diff(wt*F_*ph*sp.diff(ph, r), r) - (wt*F_*sp.diff(ph, r)**2 + kap*r*ph**2) - ph*ode
    ok_en = zero(ident)
    # Legendre: in x = r^2/mu, (r^3 f phi')' - kappa r phi = 4 sqrt(mu x) [ (x (x-1) phi_x)_x - (l/2)(l/2+1) phi ]
    x = sp.Symbol('x', positive=True)
    leg = []
    for l in range(0, 11, 2):
        P = sp.legendre(l//2, 2*x - 1)
        e = (sp.diff(r**3*F_*sp.diff(P.subs(x, r**2/mu), r), r) - l*(l + 2)*r*P.subs(x, r**2/mu))
        lead = sp.Poly(sp.expand(P), x).LC()
        leg.append(zero(e) and lead != 0)
    ok_leg = all(leg)
    # Frobenius at infinity: phi ~ rho^nu, nu^2 - 2 nu - kappa = 0
    nu = sp.Symbol('nu')
    rho = sp.Symbol('rho', positive=True)
    ex = sp.simplify(sp.expand((sp.diff(r**3*F_*sp.diff(r**(-nu), r), r) - kap*r*r**(-nu))*r**(nu - 1)))
    ind = sp.factor(sp.expand(ex.subs(s, 0)).subs(kap, l_*(l_ + 2)))
    roots = set(sp.roots(sp.Poly(ind, nu)).keys())
    ok_fr = roots == {l_ + 2, -l_}
    # psi = O(rho^(beta + 1)), beta + 1 > 0, excludes rho^-l (l >= 0): -l < beta + 1 for l >= 0
    bt = sp.Symbol('b', positive=True)                       # beta + 1 = b > 0
    ok_ex = True                                             # -l < b for l >= 0, b > 0: a positive sum
    ok_ex = positive_sum(bt + l_, [bt, l_]) and positive_sum(bt, [bt])
    tag = "  L3 control (energy weight r^2)" if control else "  L3"
    print("%s: delta Box = Box_0 delta on the modes: %s; energy identity: %s; P_{l/2}(2x - 1) solves the mode "
          "equation and grows like r^l, l = 0..10: %s; roots at infinity %s: %s; rho^-l excluded at beta > -1: %s"
          % (tag, ok_comm, ok_en, ok_leg, sorted(roots, key=str), ok_fr, ok_ex), flush=True)
    return ok_comm and ok_en and ok_leg and ok_fr and ok_ex


# ------------------------------------------------------------------------------------------------------------- L4
def coeffs3(e, Fn):
    P0, P1, P2 = sp.symbols('P0 P1 P2')
    e = sp.expand(e.subs(sp.Derivative(Fn, (r, 2)), P2).subs(sp.Derivative(Fn, r), P1).subs(Fn, P0))
    return [sp.simplify(e.coeff(p)) for p in (P2, P1, P0)]


def proportional(e1, e2, Fn):
    c1, c2 = coeffs3(e1, Fn), coeffs3(e2, Fn)
    q = [sp.simplify(x/y) for x, y in zip(c1, c2) if y != 0]
    return all(x == 0 for x, y in zip(c1, c2) if y == 0) and all(sp.simplify(q[0] - qq) == 0 for qq in q)


def l4(control=False):
    a, b, c = [sp.Function(n)(r) for n in ("a", "b", "c")]
    Mv, Mr, Mth = maxwell_scalar(a, b, c, kap)
    e = sp.diff(c, r) - b
    # with the v-equation, M_r = (kappa/r^2)(a/f - e)
    Mr_on = Mr.subs(sp.diff(r**3*sp.diff(a, r), r), kap*r*a/F_)
    ok_alg = zero(sp.simplify(Mr_on - kap/r**2*(a/F_ - e)))
    ok_th = zero(sp.simplify(Mth.subs(sp.diff(c, r), b + a/F_)))   # e = a/f makes M_th vanish identically
    W = sp.Function("W")(r)
    RW = sp.diff(F_*sp.diff(W, r)/r, r) - kap*W/r**3
    # if f (r^3 a')' = kappa r a and W = r^3 a', then a = f W'/(kappa r) and a' = W/r^3: R[W] = 0
    aW = F_*sp.diff(W, r)/(kap*r)
    ok_R = zero(sp.simplify(kap*(sp.diff(aW, r) - W/r**3) - RW))
    Phi = sp.Function("Phi")(r)
    V2 = F_/r**2*(kap + sp.Rational(3, 4) - (sp.Rational(5, 4) if control else sp.Rational(7, 4))*mu/r**2)
    ok_V2 = proportional(RW.subs(W, sp.sqrt(r)*Phi).doit(), F_*sp.diff(F_*sp.diff(Phi, r), r) - V2*Phi, Phi)
    psi = sp.Function("psi")(r)
    V1 = F_/r**2*(lam_ - sp.Rational(1, 4) + sp.Rational(5, 4)*mu/r**2)
    ok_V1 = proportional(sys_vector(psi, lam_).subs(psi, Phi/sp.sqrt(r)).doit(),
                         F_*sp.diff(F_*sp.diff(Phi, r), r) - V1*Phi, Phi)
    # positivity on r > r_h: r^2 = mu (1 + X), X > 0; kappa = 3 + K, K >= 0; lambda = 4 + L
    Xs, Ks, Ls = sp.symbols('X K L', positive=True)
    pos2 = positive_sum(sp.simplify((V2*r**2/F_).subs(r, sp.sqrt(mu*(1 + Xs))).subs(kap, 3 + Ks)), [Xs, Ks])
    pos1 = positive_sum(sp.simplify((V1*r**2/F_).subs(r, sp.sqrt(mu*(1 + Xs))).subs(lam_, 4 + Ls)), [Xs, Ls])
    # energy identity of the Liouville form: d/dr[f Phi' Phi] f = (f Phi')^2 + V Phi^2 on solutions (dr_* = dr/f)
    VV = sp.Symbol('V')
    Vf = sp.Function('Vf')(r)
    eq = F_*sp.diff(F_*sp.diff(Phi, r), r) - Vf*Phi
    ok_en = zero(F_*sp.diff(F_*sp.diff(Phi, r)*Phi, r) - ((F_*sp.diff(Phi, r))**2 + Vf*Phi**2) - Phi*eq)
    # roots at infinity
    nu = sp.Symbol('nu')
    exW = sp.expand(sp.simplify(RW.subs(W, r**nu).doit()*r**(3 - nu)).subs(s, 0)).subs(kap, l_*(l_ + 2))
    rW = set(sp.roots(sp.Poly(sp.factor(exW), nu)).keys())
    exP = sp.expand(sp.simplify(sys_vector(r**nu, (l_ + 1)**2)*r**(2 - nu)).subs(s, 0))
    rP = set(sp.roots(sp.Poly(sp.factor(exP), nu)).keys())
    ok_roots = rW == {l_ + 2, -l_} and rP == {l_ + 1, -l_ - 1}
    # growth exclusion: Phi_grow = r^(l + 3/2) (both types: W r^(-1/2), psi r^(1/2)) vs O(r^(3/2 - beta)), beta > -1:
    # l + 3/2 > 3/2 - beta  <=>  l + beta > 0, l >= 1, beta = -1 + B, B in (0, 1]
    Bs, Ln = sp.symbols('B Ln', positive=True)
    ok_gr = positive_sum((1 + Ln) + (-1 + Bs), [Ln, Bs])
    # closed forms: electrostatic regular potentials a = (x - 1) Q(x), and vector hypergeometric polynomials
    x = sp.Symbol('x', positive=True)
    el = []
    for l in (2, 4, 6, 8):
        k = l*(l + 2)
        qs = sp.symbols('q0:%d' % (l//2))
        Q = sum(qs[i]*x**i for i in range(l//2 - 1)) + x**(l//2 - 1)
        aa = (x - 1)*Q
        # f (r^3 a')' - kappa r a = 0 in x: 4 (x - 1) (x^2 a_x)_x - kappa x a = 0 (times sqrt(mu x))
        eqx = sp.expand(4*(x - 1)*sp.diff(x**2*sp.diff(aa, x), x) - k*x*aa)
        sol = sp.solve(sp.Poly(eqx, x).coeffs(), qs[:l//2 - 1], dict=True) if l > 2 else [{}]
        el.append(bool(sol) and zero(eqx.subs(sol[0]) if sol else 1))
    vecf = []
    for l in (1, 3, 5, 7):
        h = sp.hyper([sp.Rational(l + 1, 2), -sp.Rational(l + 1, 2)], [1], 1 - x)
        hp = sp.expand(sp.hyperexpand(h))
        eqv = sp.expand(4*x*sp.diff((x - 1)*sp.diff(hp, x), x) - (l + 1)**2*hp)
        vecf.append(eqv == 0 and sp.Poly(hp, x).degree() == (l + 1)//2 and sp.Poly(hp, x).LC() != 0)
    ok_cf = all(el) and all(vecf)
    if control:
        # l = 0: W* has a = 1/r^2 (its dv component), regular and decaying, f (r^3 a')' = 0; V_2 < 0 near r_h at
        # kappa = 0
        a0 = 1/r**2
        coul = zero(F_*sp.diff(r**3*sp.diff(a0, r), r))
        V20 = sp.simplify((F_/r**2*(sp.Rational(3, 4) - sp.Rational(7, 4)*mu/r**2)*r**2/F_).subs(r, s))
        print("  L4 control: Liouville form with 5/4 in place of 7/4: %s; at l = 0 the Coulomb a = 1/r^2 solves "
              "the electrostatic equation: %s, and r^2 V_2/f at r_h, kappa = 0, is %s (not positive)"
              % (ok_V2, coul, V20), flush=True)
        return ok_V2 and not coul
    print("  L4: Maxwell scalar type: M_r = (kappa/r^2)(a/f - e) on the v-equation: %s, e = a/f makes M_th vanish: "
          "%s; R[W] = 0 for W = r^3 a': %s; Liouville forms V_2: %s, V_1: %s; V_2 > 0 (kappa >= 3): %s, V_1 > 0: %s; "
          "energy identity: %s; roots at infinity W %s, psi %s: %s; r^(l + 3/2) excluded for l >= 1, beta > -1: %s; "
          "closed forms (electrostatic l = 2..8 %s, vector l = 1, 3, 5, 7 %s)"
          % (ok_alg, ok_th, ok_R, ok_V2, ok_V1, pos2, pos1, ok_en, sorted(rW, key=str), sorted(rP, key=str),
             ok_roots, ok_gr, el, vecf), flush=True)
    return all([ok_alg, ok_th, ok_R, ok_V2, ok_V1, pos2, pos1, ok_en, ok_roots, ok_gr, ok_cf])


# ------------------------------------------------------------------------------------------------------------- L5
def l5(control=False):
    # phi_l = O(r^(1 - beta)); the growing branch r^l is excluded iff l + beta - 1 > 0.  beta = -1 + B, B in (0, 1],
    # l = l_min + n, n >= 0: l + beta - 1 = l_min - 2 + n + B
    Bs, n = sp.symbols('B n', positive=True)
    lmin = 1 if control else 2
    expr = sp.expand(lmin - 2 + n + Bs)
    ok = positive_sum(expr, [Bs, n]) and positive_sum(expr.subs(n, 0), [Bs])
    tag = "  L5 control (l = 1)" if control else "  L5"
    print("%s: l + beta - 1 = %s > 0 for every l >= %d and beta in (-1, 0]: %s (at beta = -1/2, l = %d: %s)"
          % (tag, expr, lmin, ok, lmin, expr.subs({n: 0, Bs: HALF})), flush=True)
    return ok


# ------------------------------------------------------------------------------------------------------------- L6
def poly_basis(l, m=1, sysf=None):
    sysf = sysf or sys_scalar
    k = l*(l + 2)
    deg = l + 3
    q = sp.symbols('q0:%d' % (3*(deg + 1)))
    pa = sum(q[i]*r**i for i in range(deg + 1))
    pb = sum(q[deg + 1 + i]*r**i for i in range(deg + 1))
    pc = sum(q[2*deg + 2 + i]*r**i for i in range(deg + 1))
    E = sysf(pa, pb, pc, k, m)
    eqs = []
    for e, pw in zip(E, (3, 4, 3)):
        eqs += sp.Poly(sp.expand(sp.simplify(e*r**pw)), r).coeffs()
    sols = list(sp.linsolve(eqs, q))
    if not sols:
        return []
    sol = sols[0]
    free = sorted(set().union(*[sp.Tuple(x_).free_symbols for x_ in sol]), key=str)
    basis = []
    for f_ in free:
        sub = {g_: (1 if g_ == f_ else 0) for g_ in free}
        vec = [sp.expand(x_.subs(sub)) for x_ in sol]
        basis.append((sum(vec[i]*r**i for i in range(deg + 1)), sum(vec[deg + 1 + i]*r**i for i in range(deg + 1)),
                      sum(vec[2*deg + 2 + i]*r**i for i in range(deg + 1))))
    return basis


def horizon_free(l, K=7, m=1, sysf=None):
    """the formal power series solutions at r = 1 (mu = 1): unknowns U_0..U_K, the equations of orders 0..K-1; returns
    the nullspace dimension and the matrix of its (a_1, b_0, c_0) coordinates"""
    sysf = sysf or sys_scalar
    k = l*(l + 2)
    y = sp.Symbol('y')
    A = sp.symbols('A0:%d' % (K + 1))
    B = sp.symbols('B0:%d' % (K + 1))
    C = sp.symbols('C0:%d' % (K + 1))
    a = sum(A[i]*y**i for i in range(K + 1))
    b = sum(B[i]*y**i for i in range(K + 1))
    c = sum(C[i]*y**i for i in range(K + 1))
    E = sysf(a.subs(y, r - 1), b.subs(y, r - 1), c.subs(y, r - 1), k, m)
    eqs = []
    for e, pw in zip(E, (3, 4, 3)):
        P = sp.Poly(sp.expand(sp.simplify(e*r**pw).subs(r, y + 1)), y)
        cf = P.all_coeffs()[::-1]
        eqs += cf[:K]
    unknowns = list(A) + list(B) + list(C)
    Mx = sp.Matrix([[sp.expand(e_).coeff(u_) for u_ in unknowns] for e_ in eqs])
    ns = Mx.nullspace()
    idx = [unknowns.index(A[1]), unknowns.index(B[0]), unknowns.index(C[0])]
    sub = sp.Matrix([[vec[i] for i in idx] for vec in ns]) if ns else sp.zeros(0, 3)
    return len(ns), sub


def l6_path(ls, sysf=None, pmin=lambda l: 1):
    """L6's computed path: the polynomial solutions, the formal horizon data, the jets they realise, and the rank of
    the growth map on the coefficients of r^p, p >= pmin(l), of the Cartesian-normalised components a, b, c/r"""
    allok = True
    rep = []
    for l in ls:
        basis = poly_basis(l, sysf=sysf)
        dim, sub = horizon_free(l, sysf=sysf)
        jets = sp.Matrix([[sp.diff(bb[0], r).subs(r, 1), bb[1].subs(r, 1), bb[2].subs(r, 1)] for bb in basis]) \
            if basis else sp.zeros(0, 3)
        free_ok = dim == 3 and sub.shape == (3, 3) and sub.det() != 0
        jet_ok = jets.shape == (3, 3) and jets.det() != 0           # round 9: guarded (no crash on a short basis)
        cols = []
        for bb in basis:
            vec = []
            for comp, sh in ((bb[0], 0), (bb[1], 0), (bb[2], 1)):
                P = sp.Poly(sp.expand(comp), r)
                for p in range(pmin(l), l + 5):
                    vec.append(P.coeff_monomial(r**(p + sh)) if p + sh <= P.degree() else 0)
            cols.append(vec)
        rank_ok = bool(cols) and sp.Matrix(cols).T.rank() == 3
        lead = []
        for bb in basis:
            degs = [sp.Poly(bb[0], r).degree() if bb[0] != 0 else -99,
                    sp.Poly(bb[1], r).degree() if bb[1] != 0 else -99,
                    sp.Poly(bb[2], r).degree() - 1 if bb[2] != 0 else -99]
            lead.append(max(degs))
        rep.append((l, len(basis), free_ok, jet_ok, rank_ok, sorted(lead)))
        allok &= len(basis) == 3 and free_ok and jet_ok and rank_ok
    return allok, rep


def l6(control=False):
    if control:
        # round 9 (the round-8 verifier's Minor 8): the control runs L6's own path with a mutated input, twice, and
        # must fail both times: (i) the operator with E_r's coupling 2 kappa r c -> 3 kappa r c (L1's mutation);
        # (ii) the true operator with the growth threshold raised from r^1 to r^l, which the gauge solution
        # d((r^l + ...) S), growing like r^(l - 1), violates: the rank test sees the lowest growth
        ok1, rep1 = l6_path((2, 4), sysf=sys_scalar_mut)
        ok2, rep2 = l6_path((2, 4), pmin=lambda l: l)
        print("  L6 control (L6's path (i) with E_r's coupling 3 kappa r c: %s; (ii) with the growth threshold r^l: "
              "%s): passes %s, %s" % (rep1, rep2, ok1, ok2), flush=True)
        return ok1 or ok2
    allok, rep = l6_path((2, 4, 6, 8))
    print("  L6: (l, polynomial solutions, free formal data = (a'(r_h), b(r_h), c(r_h)), jets invertible, growth map "
          "rank 3, Cartesian growth exponents): %s" % rep, flush=True)
    return allok


# ------------------------------------------------------------------------------------------------------------- L7
def l7(control=False):
    x1, x2, x3, x4 = sp.symbols('x1:5', real=True)
    xs = [x1, x2, x3, x4]
    R2 = sum(q**2 for q in xs)
    hopf = {x1: sp.cos(th)*sp.cos(p1), x2: sp.cos(th)*sp.sin(p1), x3: sp.sin(th)*sp.cos(p2), x4: sp.sin(th)*sp.sin(p2)}

    def mean(u):                                             # spherical mean over S^3, Hopf measure
        u_ = sp.simplify(u.subs(hopf))
        I = sp.integrate(sp.integrate(sp.integrate(sp.expand(sp.expand_trig(u_*sp.sin(th)*sp.cos(th))),
                                                   (p1, 0, 2*sp.pi)), (p2, 0, 2*sp.pi)), (th, 0, sp.pi/2))
        return sp.simplify(I/(2*sp.pi**2))
    out = []
    ok = True
    for j in (1, 2):
        S = sp.legendre(j, (x1**2 + x2**2 - x3**2 - x4**2)/R2)
        forms = {"S dv (dt_*)": [S], "S dr": [S*q/sp.sqrt(R2) for q in xs], "dS": [sp.diff(S, q)*sp.sqrt(R2)
                                                                              for q in xs]}
        for name, comps in forms.items():
            ms = [mean(cp) for cp in comps]
            out.append((2*j, name, ms))
            ok &= all(m_ == 0 for m_ in ms)
        ok &= mean(S) == 0                                   # ell(S dv) = r_h^3 int S = 0
    # the G-average of a constant spatial covector: average over the torus and the two reflections of the matrix
    al, be = sp.symbols('alpha beta', real=True)
    Rt = sp.diag(sp.Matrix([[sp.cos(al), -sp.sin(al)], [sp.sin(al), sp.cos(al)]]),
                 sp.Matrix([[sp.cos(be), -sp.sin(be)], [sp.sin(be), sp.cos(be)]]))
    avg = (Rt.applyfunc(lambda e: sp.integrate(sp.integrate(e, (al, 0, 2*sp.pi)), (be, 0, 2*sp.pi)))/(4*sp.pi**2))
    ok &= avg == sp.zeros(4)
    if control:
        m_dv = mean(sp.Integer(1))
        ell_dv = s**3*2*sp.pi**2*m_dv
        print("  L7 control: dv has spherical mean %s and ell(dv) = %s: degree-0 part present" % (m_dv, ell_dv),
              flush=True)
        return m_dv == 0
    print("  L7: spherical means of the Cartesian components (l, form, means): %s; ell vanishes on them; the "
          "G-average of a constant spatial covector is %s: %s" % (out, list(avg), ok), flush=True)
    return ok


# ------------------------------------------------------------------------------------------------------------- L8
def l8(control=False):
    rh, sg = sp.symbols('rhat sigmahat', positive=True)
    u = sp.Function('u')(rh)
    L = sp.Symbol('L', positive=True)
    # e^(-i sg rh) (Lap_e - sg^2) e^(i sg rh) on u(rh) Y_l (Lap_e = -d^2 - (3/rh) d + l(l+2)/rh^2), against
    # (4.1) at S_0 = 0: 2 i sg rho (rho d_rho - 3/2) + rho^2 (-(rho d_rho)^2 + 2 rho d_rho + l(l+2)), rho = 1/rh
    lapu = lambda w: -sp.diff(w, rh, 2) - 3/rh*sp.diff(w, rh) + L*(L + 2)/rh**2*w
    conj = sp.simplify(sp.exp(-sp.I*sg*rh)*(lapu(sp.exp(sp.I*sg*rh)*u) - sg**2*sp.exp(sp.I*sg*rh)*u))
    rdr = lambda w: -rh*sp.diff(w, rh)                       # rho d_rho = -rh d_rh
    ntf = 2*sp.I*sg/rh*(rdr(u) - sp.Rational(3, 2)*u) + (-rdr(rdr(u)) + 2*rdr(u) + L*(L + 2)*u)/rh**2
    ok_conj = zero(conj - ntf)
    # Bessel: u = rh^-1 Z(sg rh) turns -u'' - 3u'/rh + l(l+2)u/rh^2 - sg^2 u = 0 into Bessel of order l + 1
    Z = sp.Function('Z')
    zz = sp.Symbol('z', positive=True)
    Zz = Z(zz)/zz                                            # u(rh) = sg Z(z)/z, z = sg rh, d/drh = sg d/dz
    eq = sg**3*(-sp.diff(Zz, zz, 2) - 3/zz*sp.diff(Zz, zz) + L*(L + 2)/zz**2*Zz - Zz)
    bes = -sg**3/zz**3*(zz**2*sp.diff(Z(zz), zz, 2) + zz*sp.diff(Z(zz), zz) + (zz**2 - (L + 1)**2)*Z(zz))
    ok_bes = zero(sp.simplify(eq - bes))
    # exponents at ztf: rh^nu, -nu(nu-1) - 3 nu + l(l+2) = 0
    nu = sp.Symbol('nu')
    ind = sp.factor(sp.expand(-nu*(nu - 1) - 3*nu + L*(L + 2)))
    ok_exp = set(sp.roots(sp.Poly(ind, nu)).keys()) == {L, -L - 2}
    # the two membership conditions on the box: beta in (-1, 3), q = 2 - beta, l = lval + n
    Bs, n = sp.symbols('B n', positive=True)
    if control:
        # l = 0, beta = -B' in (-1, 0): adjoint element ~ rh^-2 lies in X*_tf,0 iff q > l + 2 = 2, i.e. beta < 0
        beta = -Bs/(1 + Bs)
        q = 2 - beta
        adj_in = positive_sum(q - 2, [Bs])
        print("  L8 control (l = 0, beta in (-1, 0)): the adjoint element r^-2 lies in X*_tf,0 (q - 2 > 0): %s"
              % adj_in, flush=True)
        return not adj_in
    beta = -1 + 4*Bs/(1 + Bs)                                 # beta in (-1, 3)
    q = 2 - beta
    lval = 1 + n
    # round 9 (the round-8 verifier's nit): the box is l = 1 + n with n > 0 and, separately, n = 0 (l = 1 included)
    ker_e, adj_e = sp.simplify(lval + q), sp.simplify(lval + 2 - q)
    ker_out = positive_sum(ker_e, [Bs, n]) and positive_sum(ker_e.subs(n, 0), [Bs])   # l + q > 0: not in rh^(q-2) L^2
    adj_out = positive_sum(adj_e, [Bs, n]) and positive_sum(adj_e.subs(n, 0), [Bs])   # q < l + 2: not in rh^(-q) L^2
    print("  L8: N_tf(sigma) = e^(-i sigma r) (Lap_e - sigma^2) e^(i sigma r) on degree-l components: %s; Bessel "
          "order l + 1: %s; exponents at ztf {l, -l-2}: %s; on beta in (-1, 3), l >= 1: kernel element excluded "
          "(l + q > 0): %s, adjoint element excluded (q < l + 2): %s (both at l = 1 and on l = 1 + n, n > 0)"
          % (ok_conj, ok_bes, ok_exp, ker_out, adj_out),
          flush=True)
    return ok_conj and ok_bes and ok_exp and ker_out and adj_out


# ------------------------------------------------------------------------------------------------------------- L9
L9_SYMS = sp.symbols('D T U Wv Zv Qv Yv E1 Ep', positive=True)


def l9_cases():
    """the parameters of Theorem R8.10 / Corollary R8.11 on the box: delta_# in (0, 1/4), gamma_Upsilon in
    (delta_#, 1/4), and three sub-boxes covering alpha_K in (1, 3/2 + delta_#): (1, 3/2), {3/2} (round 9: the
    round-8 verifier's nit) and (3/2, 3/2 + delta_#), each with gamma_+ in (max(1/2, alpha_K - 1), 1/2 + delta_#)"""
    D, T, U, Wv, Zv, Qv, Yv, E1, Ep = L9_SYMS
    u01 = lambda S_: S_/(1 + S_)
    dsh = u01(D)/4                                            # delta_# in (0, 1/4)
    gU = dsh + (sp.Rational(1, 4) - dsh)*u01(Yv)               # gamma_Upsilon in (delta_#, 1/4)
    t_, u_ = u01(T), u01(U)
    cases = {
        "A: alpha_K in (1, 3/2)": (1 + t_/2, HALF + dsh*u_),
        "C: alpha_K = 3/2": (sp.Rational(3, 2), HALF + dsh*u_),
        "B: alpha_K in (3/2, 3/2 + delta_#)": (sp.Rational(3, 2) + dsh*t_, HALF + dsh*(t_ + (1 - t_)*u_)),
    }
    return dsh, gU, cases


def l9_run(gap):
    """Theorem R8.10's conditions, with the window and the (Z)-weight in the interval 'gap' ((-1, 0) on the
    subspace).  Round 9 (the round-8 verifier's Minor 9): w_I := max(5/2, gamma_+ + 1 + eps_1), eps_1 in (0, 1/2),
    eps > 0 and II.G' Proposition 3.3 (1)'s eps_PP := min(eps, eps_1) are encoded; a max on the left (a min on the
    right) is handled exactly, argument by argument, as T11 does"""
    D, T, U, Wv, Zv, Qv, Yv, E1, Ep = L9_SYMS
    pos = list(L9_SYMS)
    u01 = lambda S_: S_/(1 + S_)
    dsh, gU, cases = l9_cases()
    qh = sp.Rational(3, 2) + 2*gU + Qv                         # q > 3/2 + 2 gamma_Upsilon (K:54-57)
    w_, z_ = u01(Wv), u01(Zv)
    e1 = u01(E1)/2                                            # eps_1 in (0, 1/2)
    ep = u01(Ep)/4                                            # eps in (0, 1/4): "every small eps > 0"
    lo, hi = gap

    def nonneg(e):
        e = sp.simplify(e)
        return e == 0 or positive_sum(e, pos)

    def gt(e):
        return positive_sum(sp.simplify(e), pos)
    rep = {}
    allok = True
    for name, (aK, gp) in cases.items():
        bet = (gp - HALF) + (dsh - (gp - HALF))*w_                    # Theorem R4.3 at beta in (gamma_+ - 1/2, d#)
        eta = (HALF + dsh - gp)*z_
        WI = [sp.Rational(5, 2), gp + 1 + e1]                         # w_I = max(WI)
        EPP = [ep, e1]                                                # eps_PP = min(EPP)
        bp = (HALF + gp)/2                                            # the density pair b_+, b_I of II.F' (1.4)
        bI = (bp + sp.Rational(3, 2))/2
        maxge = lambda rhs: any(nonneg(a_ - rhs) for a_ in WI)        # max(WI) >= rhs
        cond = {
            "alpha_K - 1 > 0 (Taylor term, alpha_K not an integer)": gt(aK - 1),
            "2 - alpha_K > 0 (II.G' Props 2.8, 3.3, 3.5; Lemma R6.2 (a) zf)": gt(2 - aK),
            "(Z) weight gamma_+ - 1 > lower end of the gap": gt(gp - 1 - lo),
            "(Z) weight gamma_+ - 1 < upper end of the gap": gt(hi - (gp - 1)),
            "window gamma_+ - alpha_K < upper end of the gap": gt(hi - (gp - aK)),
            "window gamma_+ - alpha_K > lower end of the gap": gt(gp - aK - lo),
            "Lemma 4.1: w_I - 1 >= 3/2": maxge(sp.Rational(5, 2)),
            "Lemma 4.1: w_I >= gamma_+ + 1 + eps_1 (alpha_K > 1 - eps_1)": maxge(gp + 1 + e1) and gt(aK - 1 + e1),
            "Lemma 4.1: beta_iota + 2 = gamma_+ + 2 >= 5/2": nonneg(gp - HALF),
            "Prop 3.3 (1): eps_PP in (0, 1)": all(gt(e_) and gt(1 - e_) for e_ in EPP),
            "Prop 3.3 (1): w_I >= gamma_+ + 1 + eps_PP": any(maxge(gp + 1 + e_) for e_ in EPP),
            "Lemma 4.2: scf, w_I - eps_PP >= 5/2 - eps": any(maxge(sp.Rational(5, 2) - ep + e_) for e_ in EPP),
            "Lemma 4.2: scf, gamma_+ + 2 - eps_PP >= 5/2 - eps": any(nonneg(gp + 2 - (sp.Rational(5, 2) - ep + e_))
                                                                    for e_ in EPP),
            "Lemma 4.2: beta_scf = 3/2 - eps < 3/2, eps in (0, 1)": gt(ep) and gt(1 - ep),
            "Prop 3.5 (1): beta_scf = 3/2 - 2 eps >= gamma_+ (I-weight gamma_+ - eps)": nonneg(1 - 2*ep - gp + HALF),
            "density: 1/2 < b_+ < b_I < 3/2": gt(bp - HALF) and gt(bI - bp) and gt(sp.Rational(3, 2) - bI),
            "density: b_+ <= gamma_+": nonneg(gp - bp),
            "density: b_I + 1 <= w_I": maxge(bI + 1),
            "eta > 0": gt(eta),
            "cone source iota+: 5/2 + d# - eta > gamma_+ + 2": gt(HALF + dsh - eta - gp),
            "cone source K+: 2 - eta > alpha_K (w > 2)": gt(2 - eta - aK),
            "commutator iota+: 1/2 + beta > gamma_+": gt(HALF + bet - gp),
            "beta > 0": gt(bet),
            "beta < delta_#": gt(dsh - bet),
            "slab: 1/2 + beta < 3/2": gt(1 - bet),
            "slab: 1/2 + beta < q - 1": gt(qh - sp.Rational(3, 2) - bet),
            "h_>=2: w - eps' > alpha_K (w > 2)": gt(2 - aK),
            "the claim: alpha_K < 3/2 + delta_#": gt(sp.Rational(3, 2) + dsh - aK),
        }
        bad = [k_ for k_, val in cond.items() if not val]
        rep[name] = (len(cond), not bad, bad)
        allok &= not bad
    # the box reaches the claim: sup of alpha_K over sub-box B is 3/2 + delta_# (L10 uses this supremum)
    sup_B = sp.limit(cases["B: alpha_K in (3/2, 3/2 + delta_#)"][0], T, sp.oo)
    reach = sp.simplify(sup_B - (sp.Rational(3, 2) + dsh)) == 0
    return allok and reach, rep, reach, sup_B


def l9(control=False):
    # control (round 9: the round-8 verifier's Minor 8): the same conditions with the full bundle's gap, the window
    # and the (Z)-weight in (0, 1) (Theorem R6.4's), must fail on the box
    gap = (0, 1) if control else (-1, 0)
    ok, rep, reach, sup_B = l9_run(gap)
    tag = "  L9 control (the same conditions with the full bundle's window (0, 1))" if control else "  L9"
    print("%s: (sub-box, conditions, all positive sums, failing): %s; sub-box B reaches sup alpha_K = %s: %s"
          % (tag, rep, sup_B, reach), flush=True)
    return ok


# ------------------------------------------------------------------------------------------------------------ L10
def l10(control=False):
    D, Yv, P, K = sp.symbols('D Yv P K', positive=True)
    u01 = lambda S_: S_/(1 + S_)
    dsh9, gU9, cases = l9_cases()
    # round 9: the l >= 2 exponent is the supremum of alpha_K over L9's box, computed, not typed
    T9 = L9_SYMS[1]
    sups = [sp.limit(aK, T9, sp.oo) for aK, _ in cases.values()]
    top = [s_ for s_ in sups if all(sp.simplify(s_ - o_) == 0 or positive_sum(sp.simplify(s_ - o_), [L9_SYMS[0]])
                                    for o_ in sups)]
    e_box = top[0].subs(L9_SYMS[0], D) if top else sp.Integer(0)
    dsh = u01(D)/4
    gU = dsh + (sp.Rational(1, 4) - dsh)*u01(Yv)
    e_lge2 = (HALF + dsh) if control else e_box                # control: R5.3's exponent 1/2 + delta_#
    p0 = HALF + 2*gU + P                                      # p_0 > 1/2 + 2 gamma_Upsilon (Corollary R7.7 (a))
    cond = {
        "l >= 2 exponent above 3/2 (so min(p_0, 3/2) is the overall one)": e_lge2 - sp.Rational(3, 2),
        "overall exponent above R5.3's 1/2 + d# (via p_0)": p0 - HALF - dsh,
        "paper's data: l >= 2 exponent above p_0 = 1": e_lge2 - 1,
        "compact support: the l = 0 next term t^-2 below the l >= 2 exponent cap": 2 - e_lge2,
        "compact support: l >= 2 exponent above 3/2": e_lge2 - sp.Rational(3, 2),
        "the l >= 2 exponent is 3/2 + delta_# (Corollary R8.11)": sp.Integer(1) if sp.simplify(
            e_lge2 - sp.Rational(3, 2) - dsh) == 0 else sp.Integer(-1),
    }
    res = {k_: positive_sum(sp.simplify(e_), [D, Yv, P]) for k_, e_ in cond.items()}
    bad = [k_ for k_, val in res.items() if not val]
    tag = "  L10 control (R5.3's l >= 2 exponent 1/2 + delta_#)" if control else "  L10"
    print("%s: the l >= 2 exponent %s (the supremum of L9's box: %s); %d conditions, all positive sums: %s%s"
          % (tag, e_lge2, e_box, len(cond), not bad, "; failing %s" % bad if bad else ""), flush=True)
    return not bad


CHECKS = [("L1", l1), ("L2", l2), ("L3", l3), ("L4", l4), ("L5", l5), ("L6", l6), ("L7", l7), ("L8", l8),
          ("L9", l9), ("L10", l10)]


def main():
    only = sys.argv[1:]
    ok = True
    for name, fn in CHECKS:
        if only and name not in only:
            continue
        good = fn()
        ctl = fn(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    print("EXIT %d" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
