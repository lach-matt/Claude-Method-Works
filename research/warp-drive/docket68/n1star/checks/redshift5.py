#!/usr/bin/env python3
"""redshift5.py -- supplement Proposition 10.1 (iv), repaired at D622: the red-shift commutation for the class's
master fields on five-dimensional Tangherlini (Lemmas 10.1a-10.1b), and the D622 amendments of sections 8, 9 and 10.3;
computed.  Labels: computed (exact, sympy, unless marked numerical), READ (verbatim, identifier and page).

Background: f = 1 - mu/r^2, r_h = mu^(1/2), x = mu/r^2, the ingoing chart (v, r) of [HKW18] (16), g_2 = -f dv^2 +
2 dv dr, so box~ = 2 d_v d_r + d_r (f d_r) on functions of (v, r).  A mode of the class: k^2 = l (l + 2), l even,
m = k^2 - 3, H = m + 6x; master field Phi(v, r), u_j := d_r^j Phi at fixed v (d_r is transversal to the horizon).

  R1 (exact; READ) The master quantities.  [HKW18]'s (51) at n = 3 applied to a(t, r) times a transverse traceless
     harmonic ((42): eigenvalue 2 - l(l + 2)), with (134)'s potential U = 2 r^-2 and a = r^(1/2) Phi, is r^(1/2) (box~
     Phi - W_T Phi) exactly, W_T = (k^2 + 3/4 + 9x/4)/r^2, which is [KI03] (5.6)/f at n = 3 and settle5.py's tensor
     potential / f; on a scalar-derived harmonic ((36): eigenvalue 6 - k^2) with a = r^(1/2) Phi ((173), k = (4 - n)/2)
     the first-order terms of (51) cancel, so (174) is the scalar equation (170) mode by mode; (170)-(172)'s potential at
     n = 3 is settle5.py's scalar potential / f: W_S = Q/(16 r^2 H^2).  Control: (51) without its first-order term
     (n - 4) r^-1 r^A D_A leaves a residual.
  R2 (exact; READ) The surface gravity.  f'(r_h)/2 = 1/r_h, which is [HKW18] (20) kappa_n = (n - 1)/(2 r_h) at n = 3
     and [Sch13] (3.11) kappa_n = (n - 2)/(2 (2m)^(1/(n-2))) at n = 4 (r_h = (2m)^(1/2)); and f' = 2 mu/r^3 > 0 on r > 0.
     Control: the degenerate lapse (1 - mu/r^2)^2 (an extremal horizon) has kappa = 0, and the positivity test fails.
  R3 (exact) The commutation, for general f(r) and W(r).  With L := d_v + (f/2) d_r: box~ = 2 L d_r + f' d_r, and
     d_r^j (box~ Phi - W Phi) = 2 (L u_(j+1) + ((j + 1) f'/2) u_(j+1) - F_j) with F_j free of every v-derivative and of
     u_(j+1), u_(j+2) (j = 0, ..., 4); F_1 = (1/2)(W' u_0 + (W - f'') u_1); the top coefficient (j + 1) f'/2 does not
     involve W; and box~ (Y Phi) - Y (box~ Phi) = f' Y^2 Phi + (lower order) for Y = -d_r, f'(r_h) = 2 kappa ([DR08]
     Theorem 7.2's kappa_k > 0).  Control: the operator with f d_r^2 in place of d_r (f d_r) (its first-order part
     dropped) leaves u_1 in F_0: the j = 0 coefficient is not f'/2.
  R4 (exact) The energy identity and its boundaries.  For L u + a u = F: d_v (u^2) + d_r ((f/2) u^2) + (2a - f'/2) u^2
     - 2 u F = 0, with 2a - f'/2 = (2j + 1) f'/2 > 0 at a = (j + 1) f'/2; on a leaf {v = tau + s(r)} the flux density is
     (1 - s' f/2) u^2, and g^-1(dw, dw) = s'(s' f - 2) for w = v - s(r): for [HKW18]'s {t = const} (s' = 1/f) and
     {t_* = const} (s' = 1) the leaf is spacelike and the density 1/2 and 1 - f/2; on the outgoing null leaf (s' = 2/f)
     both vanish; an outgoing null ray (rho' = f/2) carries flux J^r - rho' J^v = 0; the horizon (f = 0) none.
     Control: the density with the orientation reversed, (1 + s' f/2), does not vanish on the null leaf.
  R5 (numerical, 30 digits) The divergence theorem on {0 <= v - r <= 1, r_h <= r <= 2 r_h} for a manufactured u, F :=
     L u + f' u (j = 1), mu = 1: Q(1) - Q(0) + outflow + bulk - int int 2 u F = 0 to 1e-25.  Control: the density
     (1 + s' f/2) leaves a residual.
  R6 (numerical) The Gronwall kernel: (1 + tau)^2 int_0^tau e^(-c (tau - w)) (1 + w)^-2 dw <= C_c := max(1, 16 e^(c/2 -
     2)/c^2) + 4/c for c in {0.01, 0.1, 0.5, 1, 3, 10, 30} and tau on a grid to 10^4; and the comparison lemma on two
     inequalities' extremal solutions.  Control: the bound without its first term fails.
  R7 (exact, certified) The potentials, uniformly in l.  q_S := Q/(16 H^2) = m + R(x, 1/H) exactly, R = 15/4 - 39x/4 +
     24 x (5x - 3)/H - 288 x^2 (x - 1)/H^2; on x in [0, 1], 1/H in [0, 1/5] (H >= m >= 5) |(x d_x)^i R| <= B_i, i <= 3
     (certified: coefficient sums), so every r-derivative of W_S = q_S/r^2 and W_T is O(1 + k^2) on r >= r_h, uniformly
     in l.  Control: the denominator m - 6x in place of m + 6x vanishes on the box (at m = 5, x = 5/6).
  R8 (exact) Lemma 10.1b (b).  For Phi = e^(-sigma v) R(r) the equation is f R'' + (f' - 2 sigma) R' - W R = 0; its
     indicial roots at r_h are 0 and sigma/kappa for W_S and W_T at l = 2 and l = 4, symbolic in sigma; at sigma/kappa =
     5/4 the Frobenius recursion's denominators 2 kappa n (n + 5/4) do not vanish and the first coefficient is computed;
     R' ~ (r - r_h)^(1/4) is square integrable and R'' ~ (r - r_h)^(-3/4) is not, its leading coefficient q (q - 1), q
     = sigma/kappa, computed from (r - r_h)^q and not 0 (D625, the confirming reader's check gap: at q = 1 it vanishes,
     R is z times an analytic function and R'' is bounded, which is why sigma/kappa = 1 is excluded).  Control:
     sigma/kappa = 7/4 makes R'' square integrable, so it is no counterexample.
  R9 (exact) Proposition 9.9's bootstrap (D622, minor 4).  With H, Q' <= B t^(-1/2) (T/t)^beta and D0, D1, D2 <= B
     t^(1/2) (T/t)^beta substituted, each integral of (9.9) is int_t^T t'^(-1-a) (T/t')^beta dt' <= t^(-a) (T/t)^beta/
     (beta + a) times B; the exponents a are computed per term: a = 0 for the Q'-line's t^-1 H and t^-2 D1 and the
     D0/D1-line's H (factor 1/beta), a = -1 for the D2-line's H (factor 1/(beta - 1)), a > 0 for the rest; so the
     largest factor is C/(beta - 1), and beta0 = max(2, 4C + 1) gives C/(beta0 - 1) <= 1/4.  Control: the D2 line read
     with an extra integrable power (a = 1/2) is not the computed kernel.
  R10 (exact) Theorem A_P's classes (D622, nit): the transport (d_r + 3/(2r)) Z = r^(-7/2) s with r^(3/2) Z -> 0 has Z =
     -r^(-5/2) s: in E_(5/2) with ell Z in E_(7/2), not in E_3 (so gh~ is not in O_(5/2)); gh_(m+1) = r^-2 G + Z is in
     O_2.  Control: the claim r^3 Z bounded fails.
  R11 (exact) Lemma 8.2 (D622, nit): the induced action (g_j, phi_j) -> ((-1)^j sigma^* g_j(., c - .), (-1)^j sigma^*
     phi_j) commutes with the fixed-phase Taylor rewriting of section 5.4 for every phi_j, to order lam^3, generic
     functions (model sigma: x -> -x); the fixed point at j = 1 needs sigma^* phi1 = -phi1.  Control: phi_j ->
     sigma^* phi_j without the sign does not commute.
  R12 (exact) Proposition 8.1 (D622, nit): with the monotonicity slope s >= 3/(4 mu_max) and |theta(sqrt mu)| <= C0 lam,
     the zero lies within C' lam = (4 mu_max/3) C0 lam of sqrt mu, and at r = sqrt mu - 2 C' lam the expansion is <= -C0
     lam < 0, while at sqrt mu - C' lam it can vanish.  Control: (c) with C' in place of 2 C' is not strict.
  R14 (certified, Z3 over the reals) Lemma 9.4's Jacobian (D622, from the D623 reading of Lemma 2.2).  Phi(x) = (r + 2
     lam sigma) xhat on A_P(tau), thickness Delta >= d0 >= 1, r >= r_in >= 1, |sigma0'| <= 7, |sigma| <= 1: for every lam
     with 0 < lam <= 1/10 and lam <= d0/20 the radial eigenvalue 1 + 2 lam sigma0'/Delta lies in [3/10, 1] and the
     angular ones 1 + 2 lam sigma/r in [4/5, 6/5].  Control: without lam <= d0/20 (lam <= lam1 <= 1/10 alone) Z3 finds
     a point with a negative radial eigenvalue (at lam = 1/10, Delta = 1 it is 1 - 1.4).
  R13 (text) The paper's replacement blocks (D622; D625: the 8.2 block restricts "that datum is needed" to the scalar
     type and names the measure dr dsigma, and the Proposition 3.3 proof block, two lines wider, says when its value at
     mu0 is positive -- the confirming reader's m1, m5 and nit): each old text occurs exactly once in
     paper/RESPONSE-HL-5D.md and its new text not at all; every line of the blocks and of this file is at most 121
     characters; and in N1STAR-PROOF.md the D622 text is seated: "N-th order" occurs only inside an [amended D622
     note, and Lemmas 10.1a-10.1b are present.  Control: a block whose old text is mutated does not occur.

READ (alphaXiv, 2026-11-06).  [HKW18] P.-K. Hung, J. Keller, M.-T. Wang, arXiv:1809.05144v1: p. 6, (16) "-(1 - mu)
dv-bar^2 + 2 dv-bar dR + R^2 sigma-ring", (20) "Along the event horizon, the Schwarzschild-Tangherlini solution has
positive surface gravity kappa_n := (n - 1)/(2 r_h)"; p. 12, (51) "box-slash_L(-2) t_ab = box~ t_ab + (n - 4) r^-1 r^A
D~_A t_ab + r^-2 Delta-ring t_ab + (6 - 2n) r^-2 r^A r_A t_ab - 2 r^-1 (box~ r) t_ab"; p. 8, (36) "Delta-ring
Y_ab = (2n - l(l + n - 1)) Y_ab"; p. 9, (42) "Delta-ring U_ab = (2 - l(l + n - 1)) U_ab"; p. 38, "Y|_(r=r_h) =
-d/dR", "kappa_n = (n - 1) M/r_h^n is the surface gravity"; p. 39, "We define the strictly timelike red-shift multiplier
N := T + Y", (114)-(115) and (116) (D625: (116) is on p. 39, not p. 40); p. 47, (129)-(131), "K := {T, Omega_i}";
p. 49, (134)-(135), "U := 2 r^-2";
p. 60, (170)-(172); pp. 60-61, (173) with "k := (4 - n)/2"; p. 61, (174).  [KI03] H. Kodama, A. Ishibashi,
arXiv:hep-th/0305147v3, p. 13, (5.4)-(5.6).  [DR08] M. Dafermos, I. Rodnianski, Lectures on black holes and linear
waves, arXiv:0811.0354v1: p. 40, Proposition 3.3.2, "box_g (Y-hat psi) = (2/r) Y-hat (Y-hat (psi)) - (4/r) (Y-hat (T
psi)) + P_1 psi ... the sign of the first term on the right hand side of (28) is important. We will interpret this
computation geometrically in terms of the sign of the surface gravity in Theorem 7.2"; p. 41, "Commuting repeatedly
with T, Y-hat, the above scheme plus elliptic estimates yield natural H^m estimates for all m"; p. 87, Theorem 7.2,
"Under the assumptions of the above theorem, if psi satisfies box_g psi = 0, then for all k >= 1 ... on H^+, where
kappa_k > 0", and its proof, "2 Y-pi^(alpha beta) nabla_alpha nabla_beta psi = kappa nabla^2_(YY) psi + ...".
[Sch13] V. Schlue, arXiv:1012.5963v1, p. 15, Lemma 3.2 (surface gravity), (3.11) "kappa_n = (1/2)(n - 2)/(2m)^(1/(n -
2)) > 0"; p. 16, Proposition 3.3 (redshift).

python3 checks/redshift5.py [R1 R2 ...]   (about two minutes; writes nothing; R14 needs z3-solver)
"""
import math
import os
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAPER = os.path.join(ROOT, "..", "..", "paper", "RESPONSE-HL-5D.md")
PROOF = os.path.join(ROOT, "N1STAR-PROOF.md")


def say(msg):
    print(msg, flush=True)


# ---------------------------------------------------------------- R1: the master quantities
def r1(control=False):
    t, r, mu, l = sp.symbols("t r mu l", positive=True)
    f = 1 - mu/r**2
    P = sp.Function("P")(t, r)
    n = 3

    def boxt(a):                                   # the orbit d'Alembertian of -f dt^2 + dr^2/f (sqrt|g| = 1)
        return -sp.diff(a, t, 2)/f + sp.diff(f*sp.diff(a, r), r)

    def slash(a, lap):                             # [HKW18] (51) on a(t, r) times an eigensection of Delta-ring
        first = 0 if control else sp.Rational(n - 4)/r*f*sp.diff(a, r)      # r^A D_A a = g^rr d_r a = f d_r a
        return boxt(a) + first + lap/r**2*a + sp.Rational(6 - 2*n)/r**2*f*a - 2/r*sp.diff(f, r)*a

    k2 = l*(l + 2)
    x = mu/r**2
    WT = (k2 + sp.Rational(3, 4) + sp.Rational(9, 4)*x)/r**2
    a = sp.sqrt(r)*P
    resT = sp.simplify(sp.expand((slash(a, 2 - k2) - 2/r**2*a)/sp.sqrt(r)) - (boxt(P) - WT*P))
    VT_KI = f/r**2*((k2 - 2) + 2 + sp.Rational(3, 4) + sp.Rational(9, 2)*(mu/2)/r**2)   # (5.6), K = 1, 2M = mu
    settleT = f*(((2*l + 3)*(2*l + 1))/sp.Integer(4) + sp.Rational(9, 4)*x)/r**2
    ki_ok = sp.simplify(VT_KI/f - WT) == 0 and sp.simplify(settleT/f - WT) == 0
    # scalar-derived harmonic: (51) on r^(1/2) Phi, eigenvalue 6 - k^2; first-order terms must cancel (k = 1/2)
    S = sp.expand(slash(a, 6 - k2)/sp.sqrt(r))
    rest = sp.expand(S - boxt(P))
    dP = sp.Derivative(P, r)
    first = sp.simplify(rest.coeff(dP))
    scal_first_cancel = first == 0
    # (170)-(172) at n = 3 against settle5.py's scalar potential / f
    m = k2 - 3
    H = m + 6*x
    Q = (n**4*(n + 1)**2*x**3 + n*(n + 1)*(4*(2*n*n - 3*n + 4)*m + n*(n - 2)*(n - 4)*(n + 1))*x**2
         - 12*n*((n - 4)*m + n*(n + 1)*(n - 2))*m*x + 16*m**3 + 4*n*(n + 2)*m**2)
    Vtilde = Q/(16*r**2*H**2)                         # [HKW18] (171), q + n(n + 1) mu/2 with q = m, 2M/r^2 = x
    sys.path.insert(0, ROOT)
    import settle5
    for ll in (2, 4, 6):
        rr, rh, Vs = settle5.potentials(ll, "scalar")
        eq = sp.simplify(Vs/(1 - rh**2/rr**2) - Vtilde.subs({l: ll, mu: rh**2, r: rr}))
        ki_ok &= eq == 0
    ok = resT == 0 and ki_ok and scal_first_cancel
    say("  R1%s: (134) via (51), (42) with r^(1/2) Phi gives box~ Phi = W_T Phi exactly: %s; W_T = [KI03] (5.6)/f = "
        "settle5's tensor/f, and (171)-(172) = settle5's scalar/f at l = 2, 4, 6: %s; on a scalar-derived harmonic "
        "the first-order terms of (51) cancel at k = 1/2: %s" % (" control (no first-order term)" if control else "",
                                                                resT == 0, ki_ok, scal_first_cancel))
    return bool(ok)


# ---------------------------------------------------------------- R2: the surface gravity
def r2(control=False):
    r, mu = sp.symbols("r mu", positive=True)
    rh = sp.sqrt(mu)
    f = (1 - mu/r**2)**2 if control else 1 - mu/r**2
    kappa = sp.simplify(sp.diff(f, r).subs(r, rh)/2)
    hkw = sp.Rational(3 - 1, 2)/rh                                    # (20) at n = 3
    m_ = sp.Symbol("m", positive=True)                                # [Sch13]: n = 4 spatial, r_h = (2m)^(1/2)
    sch = sp.Rational(1, 2)*(4 - 2)/(2*m_)**sp.Rational(1, 2)
    sch_ok = sp.simplify(sch.subs(m_, mu/2) - 1/rh) == 0
    fp_pos = sp.simplify(sp.diff(f, r) - 2*mu/r**3) == 0
    ok = sp.simplify(kappa - 1/rh) == 0 and sp.simplify(hkw - 1/rh) == 0 and sch_ok and fp_pos and kappa.is_positive
    say("  R2%s: kappa = f'(r_h)/2 = %s; [HKW18] (20) at n = 3: %s; [Sch13] (3.11) at n = 4: %s; f' = 2 mu/r^3 > 0: "
        "%s" % (" control (degenerate lapse)" if control else "", kappa, sp.simplify(hkw), sch_ok, fp_pos))
    return bool(ok)


# ---------------------------------------------------------------- R3: the commutation
V_, R_ = sp.symbols("v r", real=True)


def _ingoing_box(Phi, f, drop_first=False):
    """box~ of g_2 = -f dv^2 + 2 dv dr from its inverse (g^vv = 0, g^vr = 1, g^rr = f; sqrt|g| = 1)"""
    g = sp.Matrix([[-f, 1], [1, 0]])
    gi = g.inv()
    X = [V_, R_]
    sq = sp.sqrt(-g.det())
    out = sum(sp.diff(sq*gi[a, b]*sp.diff(Phi, X[b]), X[a]) for a in range(2) for b in range(2))/sq
    out = sp.expand(out)
    if drop_first:                                                   # the mutation: f d_r^2 in place of d_r(f d_r)
        out = sp.expand(out - sp.diff(f, R_)*sp.diff(Phi, R_))
    return out


def _derivs(expr, Phi):
    return [d for d in expr.atoms(sp.Derivative) if d.expr == Phi]


def r3(control=False):
    f = sp.Function("f")(R_)
    W = sp.Function("W")(R_)
    Phi = sp.Function("Phi")(V_, R_)
    fp = sp.diff(f, R_)
    box = _ingoing_box(Phi, f, drop_first=control)
    box_ok = sp.simplify(box - (2*sp.diff(Phi, V_, R_) + sp.diff(f*sp.diff(Phi, R_), R_))) == 0
    E = box - W*Phi

    def L(u):
        return sp.diff(u, V_) + f/2*sp.diff(u, R_)

    fact_ok = sp.simplify(sp.expand(2*L(sp.diff(Phi, R_)) + fp*sp.diff(Phi, R_)) - box) == 0
    ok = fact_ok
    rows = []
    for j in range(5):
        u = sp.diff(Phi, R_, j + 1)
        a = (j + 1)*fp/2
        F = sp.expand(L(u) + a*u - sp.diff(E, R_, j)/2)
        ds = _derivs(F, Phi)
        vfree = all(all(xx != V_ for xx, _ in d.variable_count) for d in ds)
        rord = max([sum(c for xx, c in d.variable_count if xx == R_) for d in ds] + [0])
        ok &= vfree and rord <= j
        rows.append((j, vfree, rord))
    F1 = sp.expand(L(sp.diff(Phi, R_, 2)) + fp*sp.diff(Phi, R_, 2) - sp.diff(E, R_)/2)
    F1_ok = sp.simplify(F1 - (sp.diff(W, R_)*Phi + (W - sp.diff(f, R_, 2))*sp.diff(Phi, R_))/2) == 0
    # the potential never reaches u_(j+1): d_r^j (W Phi) has no u_(j+1)
    noW = all(sp.expand(sp.diff(W*Phi, R_, j)).coeff(sp.diff(Phi, R_, j + 1)) == 0 for j in range(5))
    # [DR08]'s form: box~(Y Phi) - Y(box~ Phi), Y = -d_r: its Y^2 Phi = d_r^2 Phi coefficient is f'
    Yphi = -sp.diff(Phi, R_)
    comm = sp.expand(_ingoing_box(Yphi, f, drop_first=control) + sp.diff(box, R_))
    c_YY = sp.simplify(comm.coeff(sp.diff(Phi, R_, 2)))
    dr_ok = sp.simplify(c_YY - fp) == 0
    ok &= F1_ok and noW and dr_ok and box_ok
    say("  R3%s: box~ from g_2's inverse = 2 d_v d_r + d_r (f d_r): %s; box~ = 2 L d_r + f' d_r: %s; F_j free of d_v "
        "and of u_(j+1) (j, v-free, top r-order): %s; F_1 = (W' u_0 + (W - f'') u_1)/2: %s; d_r^j (W Phi) never "
        "reaches u_(j+1): %s; box~(Y Phi) - Y(box~ Phi) has Y^2 Phi coefficient f' (= 2 kappa at r_h): %s"
        % (" control (first-order part dropped)" if control else "", box_ok, fact_ok, rows, F1_ok, noW, dr_ok))
    return bool(ok)


# ---------------------------------------------------------------- R4: the energy identity and its boundaries
def r4(control=False):
    f = sp.Function("f")(R_)
    u = sp.Function("u")(V_, R_)
    fp = sp.diff(f, R_)
    j = sp.Symbol("j", nonnegative=True)
    a = (j + 1)*fp/2
    F = sp.diff(u, V_) + f/2*sp.diff(u, R_) + a*u
    ident = sp.simplify(sp.diff(u**2, V_) + sp.diff(f/2*u**2, R_) + (2*a - fp/2)*u**2 - 2*u*F)
    bulk = sp.simplify(2*a - fp/2 - (2*j + 1)*fp/2) == 0
    sp_ = sp.Symbol("sp")                                             # s'
    sgn = -1 if control else 1
    density = 1 - sgn*sp_*f/2                                          # J^v - s' J^r over u^2 (control: reversed)
    norm = sp.expand(0 - 2*sp_*1 + sp_**2*f)                          # g^vv - 2 s' g^vr + s'^2 g^rr
    rr, mu = sp.symbols("rr mu", positive=True)
    fx = 1 - mu/rr**2
    leaves = {"t = const (s' = 1/f)": 1/fx, "t_* = const (s' = 1)": sp.Integer(1), "u = const (s' = 2/f)": 2/fx}
    vals = {}
    for name, s1 in leaves.items():
        dens = sp.simplify(density.subs({sp_: s1, f: fx}))
        nrm = sp.simplify(norm.subs({sp_: s1, f: fx}))
        vals[name] = (dens, nrm)
    t_ok = sp.simplify(vals["t = const (s' = 1/f)"][0] - sp.Rational(1, 2)) == 0
    ts_ok = sp.simplify(vals["t_* = const (s' = 1)"][0] - (1 - fx/2)) == 0
    null_ok = sp.simplify(vals["u = const (s' = 2/f)"][0]) == 0 and sp.simplify(vals["u = const (s' = 2/f)"][1]) == 0
    spacelike = all(sp.simplify(vals[k_][1]).subs({rr: 3, mu: 1}) < 0 for k_ in list(leaves)[:2])
    rp_ = sp.Symbol("rho_p")
    rho_p = sp.solve(sp.Eq(-f + 2*rp_, 0), rp_)[0]                     # g_2((1, rho'), (1, rho')) = 0: outgoing
    ray = sp.simplify(f/2*u**2 - rho_p*u**2) == 0                      # J^r - rho' J^v on r = rho(v)
    ok = ident == 0 and bulk and t_ok and ts_ok and null_ok and spacelike and ray
    say("  R4%s: d_v(u^2) + d_r((f/2)u^2) + (2a - f'/2)u^2 - 2uF = %s; bulk (2j + 1) f'/2: %s; leaf densities and "
        "g^-1(dw, dw): %s; spacelike t, t_* leaves: %s; null leaf density 0: %s; outgoing ray flux 0: %s"
        % (" control (orientation reversed)" if control else "", ident, bulk,
           {k_: (str(vv[0]), str(sp.factor(vv[1]))) for k_, vv in vals.items()}, spacelike, null_ok, ray))
    return bool(ok)


# ---------------------------------------------------------------- R5: the divergence theorem by quadrature
def r5(control=False):
    mp.mp.dps = 30
    mu, rh, r2_ = mp.mpf(1), mp.mpf(1), mp.mpf(2)
    f = lambda r: 1 - mu/r**2
    fp = lambda r: 2*mu/r**3
    s = lambda r: r                                                   # the leaves t_* = v - r = const
    sp_ = lambda r: mp.mpf(1)
    u = lambda v, r: mp.exp(-v/3)*(1 + r**2 + mp.sin(v + 2*r)/2)
    ur = lambda v, r: mp.diff(lambda rr: u(v, rr), r)
    uv = lambda v, r: mp.diff(lambda vv: u(vv, r), v)
    a = lambda r: fp(r)                                               # j = 1: a = (j + 1) f'/2 = f'
    F = lambda v, r: uv(v, r) + f(r)/2*ur(v, r) + a(r)*u(v, r)
    sg = -1 if control else 1
    Q = lambda tau: mp.quad(lambda r: (1 - sg*sp_(r)*f(r)/2)*u(tau + s(r), r)**2, [rh, r2_])
    outflow = mp.quad(lambda w: f(r2_)/2*u(w + s(r2_), r2_)**2, [0, 1])
    horizon = mp.quad(lambda w: f(rh)/2*u(w + s(rh), rh)**2, [0, 1])
    bulk = mp.quad(lambda w, r: ((2*a(r) - fp(r)/2)*u(w + s(r), r)**2 - 2*u(w + s(r), r)*F(w + s(r), r)),
                   [0, 1], [rh, r2_])
    res = Q(1) - Q(0) + outflow - horizon + bulk
    ok = abs(res) < mp.mpf(10)**-25 and abs(horizon) == 0
    say("  R5%s: Q(1) - Q(0) + outflow - horizon + bulk - int int 2uF = %s (horizon flux %s)"
        % (" control (density 1 + s'f/2)" if control else "", mp.nstr(res, 5), mp.nstr(horizon, 3)))
    return bool(ok)


# ---------------------------------------------------------------- R6: the Gronwall kernel and the comparison
def r6(control=False):
    mp.mp.dps = 20
    worst = []
    ok = True
    for c in (0.01, 0.1, 0.5, 1.0, 3.0, 10.0, 30.0):
        c = mp.mpf(c)
        Cc = (0 if control else max(1, 16*mp.e**(c/2 - 2)/c**2)) + 4/c
        ratio = mp.mpf(0)
        for tau in [mp.mpf(x) for x in (0.01, 0.1, 0.5, 1, 2, 5, 10, 30, 100, 300, 1000, 3000, 10000)]:
            val = mp.quad(lambda w: mp.e**(-c*(tau - w))*(1 + w)**-2, [0, max(tau - 50/c, 0), tau]) \
                if tau > 50/c else mp.quad(lambda w: mp.e**(-c*(tau - w))*(1 + w)**-2, [0, tau])
            ratio = max(ratio, (1 + tau)**2*val/Cc)
        worst.append((float(c), float(ratio)))
        ok &= ratio <= 1
    # the comparison: Q' = -bQ/2 + (2/b)G is the extremal; a Q with Q' <= -bQ/2 + (2/b)G stays below it (Euler, exact
    # recursion with a nonnegative defect)
    b, G = mp.mpf(3)/8, lambda w: (1 + w)**-2
    h, Qx, Qe = mp.mpf(1)/100, mp.mpf(5), mp.mpf(5)
    below = True
    for i in range(4000):
        w = i*h
        Qe = Qe + h*(-b*Qe/2 + 2/b*G(w))
        Qx = Qx + h*(-b*Qx/2 + 2/b*G(w) - mp.mpf(1)/10*abs(mp.sin(w)))
        below &= Qx <= Qe
    ok &= below
    say("  R6%s: max over tau of (1 + tau)^2 int e^(-c(tau - w))(1 + w)^-2 / C_c, per c: %s; a defect-forced Q stays "
        "below the extremal: %s" % (" control (C_c = 4/c)" if control else "",
                                    [(c_, round(x_, 4)) for c_, x_ in worst], below))
    return bool(ok)


# ---------------------------------------------------------------- R7: the potentials, uniformly in l
def r7(control=False):
    m, x, y = sp.symbols("m x y", positive=True)
    n = 3
    H = m - 6*x if control else m + 6*x
    Q = (n**4*(n + 1)**2*x**3 + n*(n + 1)*(4*(2*n*n - 3*n + 4)*m + n*(n - 2)*(n - 4)*(n + 1))*x**2
         - 12*n*((n - 4)*m + n*(n + 1)*(n - 2))*m*x + 16*m**3 + 4*n*(n + 2)*m**2)
    Rxy = sp.Rational(15, 4) - sp.Rational(39, 4)*x + 24*x*(5*x - 3)*y - 288*x**2*(x - 1)*y**2
    ident = sp.simplify(Q/(16*(m + 6*x)**2) - m - Rxy.subs(y, 1/(m + 6*x))) == 0
    # the premise H >= 5 on m >= 5, 0 <= x <= 1 (H linear in x: its minimum is at an end of [0, 1], at m = 5)
    Hmin = min(H.subs({m: 5, x: 0}), H.subs({m: 5, x: 1}), H.subs({m: 5, x: sp.Rational(5, 6)}))
    premise = Hmin >= 5
    bounds = []
    expr = Rxy
    for i in range(4):
        P = sp.Poly(sp.expand(expr), x, y)
        B = sum(abs(cf)*sp.Rational(1, 5)**mon[1] for mon, cf in P.terms())     # |x| <= 1, |y| <= 1/5
        bounds.append(B)
        expr = sp.expand(x*(sp.diff(expr, x) + sp.diff(expr, y)*(-6*y**2)))     # x d_x at fixed m, y = 1/H
    k2 = sp.Symbol("k2", positive=True)
    WT_r2 = k2 + sp.Rational(3, 4) + sp.Rational(9, 4)*x
    tens = all(sp.Poly(sp.expand(WT_r2 - k2), x).coeffs()[i_] >= 0 for i_ in range(2))
    ok = ident and premise and tens and all(B_.is_Rational for B_ in bounds)       # l-independent constants
    say("  R7%s: Q/(16 H^2) = m + R(x, 1/H) exactly: %s; H >= 5 on the box (min %s): %s; |(x d_x)^i R| <= %s on x in "
        "[0, 1], 1/H in [0, 1/5] (certified); W_T r^2 - k^2 = 3/4 + 9x/4 in [3/4, 3]: %s"
        % (" control (H = m - 6x)" if control else "", ident, Hmin, premise, [str(B_) for B_ in bounds], tens))
    return bool(ok)


# ---------------------------------------------------------------- R8: Lemma 10.1b (b)
def r8(control=False):
    r, mu, sig = sp.symbols("r mu sigma", positive=True)
    rh = sp.sqrt(mu)
    f = 1 - mu/r**2
    kap = sp.diff(f, r).subs(r, rh)/2
    roots_ok = True
    rho = sp.Symbol("rho")
    for kind in ("scalar", "tensor"):
        for l in (2, 4):
            k2 = l*(l + 2)
            mm = k2 - 3
            x = mu/r**2
            W = ((16*mm**3 + 36*mm**2*x + 60*mm**2 + 624*mm*x**2 - 432*mm*x + 1296*x**3 - 144*x**2)
                 / (16*(mm + 6*x)**2)/r**2) if kind == "scalar" else (k2 + sp.Rational(3, 4) + sp.Rational(9, 4)*x)/r**2
            # indicial: leading behaviour of f R'' + (f' - 2 sigma) R' - W R at r = r_h on R = (r - r_h)^rho
            ind = sp.expand(sp.diff(f, r).subs(r, rh)*rho*(rho - 1) + (sp.diff(f, r).subs(r, rh) - 2*sig)*rho)
            sols = sp.solve(ind, rho)
            roots_ok &= set(sp.simplify(s_) for s_ in sols) == {0, sp.simplify(sig/kap)}
            # W is smooth at r_h, so it does not enter the indicial polynomial (W R is one order higher)
            roots_ok &= sp.simplify(W.subs(r, rh)).is_finite
    ratio = sp.Rational(7, 4) if control else sp.Rational(5, 4)
    nn = sp.Symbol("n", positive=True, integer=True)
    denom = sp.factor(2*kap*(ratio + nn)**2 - 2*kap*ratio*(ratio + nn))          # indicial polynomial at rho + n
    denom_ok = sp.simplify(denom - 2*kap*nn*(nn + ratio)) == 0
    # first Frobenius coefficient at l = 2, scalar type, mu = 1: R = (r - 1)^ratio (1 + a1 (r - 1) + ...)
    z, a1 = sp.symbols("z a1")
    mu1 = 1
    rr = 1 + z
    f1 = 1 - mu1/rr**2
    mm = 5
    x1 = mu1/rr**2
    W1 = ((16*mm**3 + 36*mm**2*x1 + 60*mm**2 + 624*mm*x1**2 - 432*mm*x1 + 1296*x1**3 - 144*x1**2)
          / (16*(mm + 6*x1)**2)/rr**2)
    s1 = ratio*1                                                       # sigma = ratio * kappa, kappa = 1 at mu = 1
    Rz = z**ratio*(1 + a1*z)
    ode = sp.diff(Rz, z, 2)*f1 + (sp.diff(f1, z) - 2*s1)*sp.diff(Rz, z) - W1*Rz
    lead = sp.series(sp.simplify(ode/z**(ratio - 1)), z, 0, 2).removeO()
    c0 = sp.simplify(lead.coeff(z, 0))
    c1 = sp.simplify(lead.coeff(z, 1))
    a1v = sp.solve(c1, a1)
    frob_ok = c0 == 0 and len(a1v) == 1
    # integrability near r_h of R' ~ z^(ratio - 1) and R'' ~ z^(ratio - 2)
    e1, e2 = 2*(ratio - 1), 2*(ratio - 2)
    Rp_L2 = e1 > -1
    Rpp_notL2 = e2 <= -1
    # D625: R'' ~ z^(ratio - 2) needs its leading coefficient q (q - 1), q = ratio, to be nonzero (computed from z^q)
    qq1 = sp.simplify(sp.diff(z**ratio, z, 2)/z**(ratio - 2))
    lead_ok = qq1 != 0
    ok = roots_ok and denom_ok and frob_ok and Rp_L2 and Rpp_notL2 and lead_ok
    say("  R8%s: indicial roots {0, sigma/kappa} for W_S, W_T at l = 2, 4: %s; recursion denominators 2 kappa n (n + "
        "%s): %s; Frobenius a1 at l = 2 = %s; R' in L^2: %s; R'' not in L^2: %s, its leading coefficient q (q - 1) = %s "
        "!= 0: %s"
        % (" control (sigma/kappa = 7/4)" if control else "", roots_ok, ratio, denom_ok, a1v, Rp_L2, Rpp_notL2, qq1,
           lead_ok))
    return bool(ok)


# ---------------------------------------------------------------- R9: Proposition 9.9's bootstrap factors
def r9(control=False):
    t, T, beta = sp.symbols("t T beta", positive=True)
    tp = sp.Symbol("tp", positive=True)
    h = sp.Rational(1, 2)
    Hq, Dd = -h, h                                         # H, Q' ~ t^(-1/2), D0-D2 ~ t^(1/2), times B (T/t)^beta
    # (line, term, the power of t' in the integrand without (T/t')^beta, the power of t in the line's target)
    terms = [("H", "t^-3/2 (H + Q')", -3*h + Hq, Hq), ("H", "t^-5/2 D1", -5*h + Dd, Hq),
             ("H", "t^-3 (D0 + D2)", -3 + Dd, Hq),
             ("D0/D1", "t^-1/2 H", -h + Hq, 0), ("D2", "t^1/2 H", h + Hq, 1),
             ("Q'", "t^1/2 t^-1 H", h - 1 + Hq, 0), ("Q'", "t^1/2 t^-2 D1", h - 2 + Dd, 0),
             ("Q'", "t^1/2 t^-3/2 (H + Q')", h - 3*h + Hq, 0), ("Q'", "t^1/2 t^-3 (D0 + D2)", h - 3 + Dd, 0)]
    table, ok = [], True
    for line, name, e, target in terms:
        a = -1 - e                                                    # the integrand is t'^(-1-a) (T/t')^beta
        if control and line == "D2":
            a = h
        for bv in (sp.Rational(5, 2), 3, 7):                          # the bound int <= t^(-a) (T/t)^beta/(beta + a)
            exact = sp.integrate(tp**(-1 - a)*(T/tp)**bv, (tp, t, T))
            bound = t**(-a)*(T/t)**bv/(bv + a)
            for tv, Tv in ((1, 2), (2, 7), (3, 100)):
                ok &= bool(exact.subs({t: tv, T: Tv}) <= bound.subs({t: tv, T: Tv}))
        p = -a - target                                               # the factor t^p beyond 1/(beta + a)
        table.append((line, name, a, p))
    exact_rows = [(ln, nm, a) for ln, nm, a, p in table if p == 0]
    a_D2 = [a for ln, nm, a, p in table if ln == "D2"][0]
    ok &= sorted(set(a for _, _, a in exact_rows)) == [-1, 0] and a_D2 == -1 and all(p < 0 for *_, p in table if p != 0)
    ok &= all(p <= 0 for *_, p in table)
    C = sp.Symbol("C", positive=True)
    quarter = all(sp.N(c_/(max(2, 4*c_ + 1) - 1)) <= 0.25 + 1e-15 for c_ in (0.01, 0.25, 1, 7, 1000))
    ok &= quarter
    say("  R9%s: (line, term, a, extra power p) with integrand t'^(-1-a)(T/t')^beta and factor t^p/(beta + a): %s; "
        "the terms with no extra power: %s; C/(beta0 - 1) <= 1/4 for beta0 = max(2, 4C + 1): %s"
        % (" control (D2 read with an extra power)" if control else "", [(ln, a, p) for ln, nm, a, p in table],
           exact_rows, quarter))
    return bool(ok)


# ---------------------------------------------------------------- R10: Theorem A_P's classes
def r10(control=False):
    r, rp, s = sp.symbols("r rp s", positive=True)
    Z = -r**sp.Rational(-3, 2)*sp.integrate(rp**sp.Rational(3, 2)*rp**sp.Rational(-7, 2)*s, (rp, r, sp.oo))
    solves = sp.simplify(sp.diff(Z, r) + sp.Rational(3, 2)/r*Z - r**sp.Rational(-7, 2)*s) == 0
    decays = sp.limit(r**sp.Rational(3, 2)*Z, r, sp.oo) == 0
    is_exact = sp.simplify(Z + r**sp.Rational(-5, 2)*s) == 0
    E52 = sp.limit(r**sp.Rational(5, 2)*Z, r, sp.oo) == -s
    ellE72 = sp.limit(r**sp.Rational(7, 2)*sp.diff(Z, r), r, sp.oo) == sp.Rational(5, 2)*s
    weight = sp.Rational(5, 2) if control else 3
    notE = sp.limit(sp.Abs(r**weight*Z/s), r, sp.oo) == sp.oo
    ok = solves and decays and is_exact and E52 and ellE72 and notE
    say("  R10%s: Z = %s solves (d_r + 3/(2r)) Z = r^(-7/2) s with r^(3/2) Z -> 0: %s; r^(5/2) Z bounded: %s; r^(7/2) "
        "d_r Z bounded: %s; r^%s Z unbounded: %s" % (" control (weight 5/2)" if control else "", Z, solves and decays
                                                     and is_exact, E52, ellE72, weight, notE))
    return bool(ok)


# ---------------------------------------------------------------- R11: Lemma 8.2 and the Taylor rewriting
def r11(control=False):
    x, th, lam, c = sp.symbols("x theta lam c")
    g = [None] + [sp.Function("g%d" % j) for j in (1, 2, 3)]
    ph = [None] + [sp.Function("p%d" % j) for j in (1, 2, 3)]

    def full(gs, ps):                                                # sum lam^j g_j(x, th + phi1 + lam phi2 + ...)
        phase = th + ps[1](x) + lam*ps[2](x) + lam**2*ps[3](x)
        return sum(lam**j*gs[j](x, phase) for j in (1, 2, 3))

    def S_unknowns(gs, ps):                                          # the induced action on (g_j, phi_j)
        sgn = (lambda j: 1) if control else (lambda j: (-1)**j)
        Gs = [None] + [sp.Lambda((sp.Symbol("X"), sp.Symbol("Y")),
                                 (-1)**j*gs[j](-sp.Symbol("X"), c - sp.Symbol("Y"))) for j in (1, 2, 3)]
        Ps = [None] + [sp.Lambda(sp.Symbol("X"), sgn(j)*ps[j](-sp.Symbol("X"))) for j in (1, 2, 3)]
        return Gs, Ps

    def S_function(F):                                               # the action on a two-scale function
        return F.subs({x: -x, th: c - th, lam: -lam}, simultaneous=True)

    def taylor(F, order=3):
        return sp.series(F, lam, 0, order + 1).removeO()

    lhs = taylor(full(*S_unknowns(g, ph)))
    rhs = taylor(S_function(full(g, ph)))
    diff = sp.simplify(sp.expand(lhs - rhs))
    ok = diff == 0
    say("  R11%s: the Taylor rewriting to lam^3 commutes with the induced action for generic g_j, phi_j: %s"
        % (" control (phi_j -> sigma^* phi_j)" if control else "", ok))
    return bool(ok)


# ---------------------------------------------------------------- R12: Proposition 8.1's constants
def r12(control=False):
    C0, lam, mumax, sm = sp.symbols("C0 lam mu_max s", positive=True)
    Cp = sp.Rational(4, 3)*mumax*C0                                   # (b)'s constant: |R - sqrt mu| <= C' lam
    smin = 3/(4*mumax)
    worst = lambda d: C0*lam - smin*d                                  # sup of theta at sqrt mu - d, theta linear
    zero_dist = sp.simplify(C0*lam/smin - Cp*lam) == 0
    at_C = sp.simplify(worst(Cp*lam))
    mult = 1 if control else 2
    at_2C = sp.simplify(worst(mult*Cp*lam))
    ok = zero_dist and at_C == 0 and sp.simplify(at_2C + C0*lam) == 0
    say("  R12%s: the zero within C' lam = (4 mu_max/3) C0 lam: %s; sup theta at sqrt mu - C' lam = %s (can vanish); at "
        "sqrt mu - %d C' lam = %s" % (" control (C')" if control else "", zero_dist, at_C, mult, at_2C))
    return bool(ok)


# ---------------------------------------------------------------- R14: Lemma 9.4's Jacobian
def r14(control=False):
    import z3
    lam, d0, D, r, sp_, sg = z3.Reals("lam d0 D r sp sg")
    hyp = [lam > 0, 10*lam <= 1, d0 >= 1, D >= d0, r >= 1, sp_ >= -7, sp_ <= 0, sg >= -1, sg <= 1]
    if not control:
        hyp.append(20*lam <= d0)
    S = z3.Solver()
    S.set("timeout", 120000)
    S.add(*hyp)
    S.add(z3.Or(10*(D + 2*lam*sp_) < 3*D, D + 2*lam*sp_ > D, 5*(r + 2*lam*sg) < 4*r, 5*(r + 2*lam*sg) > 6*r))
    res = S.check()
    cert = res == z3.unsat
    witness = None
    if res == z3.sat:
        M = S.model()
        val = lambda e: float(M.eval(e, model_completion=True).as_fraction())
        witness = (val(lam), val(D), val(sp_), 1 + 2*val(lam)*val(sp_)/val(D))
    worst = 1 + 2*sp.Rational(1, 10)*(-7)/1                                     # lam = 1/10, Delta = 1, sigma0' = -7
    say("  R14%s: Z3: radial eigenvalue in [3/10, 1] and angular in [4/5, 6/5] for 0 < lam <= min(1/10, d0/20), "
        "Delta >= d0 >= 1, r >= 1: %s (%s)%s; at lam = 1/10, Delta = 1, sigma0' = -7 the radial eigenvalue is %s"
        % (" control (lam <= 1/10 only)" if control else "", cert, res,
           "" if witness is None else "; witness (lam, Delta, sigma0', radial eigenvalue) = %s" % (witness,), worst))
    return bool(cert)


# ---------------------------------------------------------------- R13: the paper's blocks and the seated text
OLD82 = """\
So in
that Regge–Wheeler-type gauge, with the l = 0 gauge fixed to the mass change, every metric component of a perturbation
in the class settles to a change of mass at [HKW18]'s rate on each region r ≤ R, uniformly in l with a constant growing
as a power of R (uniformly in r it is not shown), with the loss of two derivatives so counted."""

NEW82 = """\
So in
that Regge–Wheeler-type gauge, with the l = 0 gauge fixed to the mass change K = r^(−2) dv², v the ingoing time (the
static chart's mass change is singular at the horizon), every metric component of a perturbation in the class settles
to a change of mass on each region r ≤ R, the horizon included, uniformly in l, with the loss of two derivatives so
counted, in two data classes (supplement Proposition 10.1 (iv), repaired). For Hintz's data it settles pointwise, with
all derivatives, at Part VIII's rate O(t*^(−2−ε)) (supplement GAUGEDECAY5 Theorem 1.5, a proof from Part VIII and Part
IX, independently verified). For [HKW18]'s data it settles at their rate τ^(−2) in energy, the squared L² norm of the
components against dr dσ (dσ the unit three-sphere's measure), with a constant growing as R⁵, once one more datum is
finite: the master fields' second derivative transversal to the horizon, square integrable on the initial slice near
it. For the scalar type that datum is needed (the tensor type's components carry no derivative of its master field),
because [HKW18]'s energies are those of the red-shift multiplier
N = T + Y ((115), p. 39), first order, and at the horizon, where the master equation's coefficient of that derivative
vanishes, the equation does not give it; their class does not bound it, since solutions with every one of their
energies finite can have it infinite. Given the datum, the red-shift commutation of Dafermos and Rodnianski ([DR08]
Theorem 7.2, p. 87) carries it at the master fields' rate, because the surface gravity 1/r_h is positive ([HKW18]
(20), p. 6): in the class it is exact, a transport along the outgoing null direction whose damping j f′/2 on the j-th
transversal derivative does not involve the potential (computed: `docket68/n1star/checks/redshift5.py`). Uniformly in
r the energy statement fails, and what holds instead is sharp (supplement RWGAUGE5,
`docket68/n1star/checks/rwgauge5u.py`). In the frame of the static observers, on the outgoing part of [HKW18]'s leaves,
the orbit-space components of the scalar type can grow as, and no faster than, r^(1/2): for every leaf there is a
single-mode perturbation of the class, with finite [HKW18] data of every order, whose component h(e_0, e_0) is
B r^(1/2) f^(−1) S on the outgoing part of that leaf, B ≠ 0 a constant, f = 1 − μ/r² and S its harmonic (Theorem 1,
proved; the components computed exactly). With that weight they settle, and the angular components and the tensor type
settle without it, uniformly in r and l on the outgoing part of the leaves, in ‖·‖, the L² norm on the unit
three-sphere at fixed (τ, r): r^(−1/2)‖h(e_a, e_b)‖ and r^(1/2)‖h(e_i, e_j)‖ decay at least as τ^(δ−1/2) for every
δ ∈ (0, 1/2], r^(−1)‖h(e_a, e_b)‖ and ‖h(e_i, e_j)‖ at least as τ^(−1), and ∫ (r^(−3)‖h(e_a, e_b)‖² + r^(−1)‖h(e_i,
e_j)‖²) dr over the outgoing part at least as τ^(−2), [HKW18]'s rate, for data with two more commutations with T and
the rotations (Theorem 2, proved from [HKW18]'s Theorems 2, 16 and 18 as READ; every coefficient and exponent
computed). The powers r^(±1/2) are attained, so the weights cannot be improved."""

OLDT7 = """\
7. **Mean mass.** For every sphere S_(v,r) of the domain, its Hawking mass satisfies |M[S](g_λ) − μ(v)| ≤ C λ² before and
   after the shell (v ≤ v_start or v ≥ v_end), and ≤ C λ within it (Proposition 3.4)."""

NEWT7 = """\
7. **Mean mass.** For every sphere S_(v,r) in D_T ∩ {τ ≥ τ0}, its Hawking mass satisfies |M[S](g_λ) − μ(v)| ≤ C λ²
   before and after the shell (v ≤ v_start or v ≥ v_end), and ≤ C λ within it (Proposition 3.4)."""

OLD33 = """\
H1–H3; supplement Proposition 8.1).** Let μ0 > √72 l5², K ≥ 6, and let θ⁺_λ(v, r, ω) be the outgoing null expansion, for
g_λ, of the sphere S_(v,r) := {τ = v − r, |x| = r} at its point of angle ω. There are λ_H ∈ (0, λ0] and C, δ1 > 0 such
that for λ ≤ λ_H: on every column (v and ω fixed, r varying, within D_T ∩ {τ ≥ τ0}) θ⁺_λ has at most one zero, positive
above it and negative below; on the columns with √μ(v) ≤ v − τ0 − δ1 it has exactly one, R_λ(v, ω), with |R_λ − √μ(v)| ≤
C λ; and the spheres with r ≤ √μ(v) − C λ are trapped, those with r ≥ √μ(v) + C λ untrapped."""

NEW33 = """\
H1–H3; supplement Proposition 8.1).** Let μ0 ≥ √72 l5², K ≥ 6, and let θ⁺_λ(v, r, ω) be the outgoing null expansion, for
g_λ, of the sphere S_(v,r) := {τ = v − r, |x| = r} at its point of angle ω. There are λ_H ∈ (0, λ0] and C, δ1, δ2 > 0
such that for λ ≤ λ_H: on every column (v and ω fixed, r varying, within D_T ∩ {τ ≥ τ0}) θ⁺_λ has at most one zero,
positive above it and negative below; if μ0 > √72 l5², on the columns with √μ(v) ≤ v − τ0 − δ1 it has exactly one,
R_λ(v, ω), with |R_λ − √μ(v)| ≤ C λ, and the spheres with r ≤ √μ(v) − C λ are trapped, those with r ≥ √μ(v) + C λ
untrapped (C twice the constant that places the zero, so that the spheres at distance C λ are strictly trapped)."""

# D625: widened by two lines to carry the confirming reader's nit on the positivity at mu0 = sqrt72 l5^2
OLD33b = """\
strictly increasing in r; √μ(v) − r_q(v) = μ^(1/4)(μ^(1/4) − (√72 l5²)^(1/4)) ≥ its value at μ0 > 0, the right side
increasing for μ > √72 l5²/16 (computed, `docket68/n1star/checks/support3.py` D1). The intermediate value theorem and the
monotonicity give the zero and its uniqueness. If μ0 = √72 l5², the first statement holds on every column, and the others
on the columns with μ(v) ≥ μ0 + δ1. ∎"""

NEW33b = """\
strictly increasing in r; √μ(v) − r_q(v) = μ^(1/4)(μ^(1/4) − (√72 l5²)^(1/4)) ≥ its value at μ0, which is positive when
μ0 > √72 l5², the right side increasing for μ > √72 l5²/16 (computed, `docket68/n1star/checks/support3.py` D1). The
intermediate value theorem and the monotonicity give the zero and its uniqueness. If μ0 = √72 l5², the first statement
holds on every column, and the others on the columns with μ(v) ≥ μ0 + δ2 that satisfy √μ(v) ≤ v − τ0 − δ1. ∎"""

OLD82o = """\
and in it the metric components are [KI03]'s (3.14), the master field normalised as r^(3/2) Φ and its derivatives to"""

NEW82o = """\
and in it the metric components, in an ingoing chart and the spheres' orthonormal frame, are [KI03]'s (3.14), the
master field normalised as r^(3/2) Φ and its derivatives to"""

OLDT2 = """\
   derivatives, at most ε_P t^(−3/2) for a small ε_P > 0 (supplement Lemma 9.1 (f)), and whose energy on the slices"""

NEWT2 = """\
   derivatives, at most ε_U t^(−3/2) for a small ε_U > 0 (within the margin of supplement Lemma 9.1 (f)), and whose
   energy on the slices"""

OLDR1 = """\
  4.21–4.22 and (5.18)–(5.22); (4.64), (4.67), (4.71) and Corollary 4.18, pp. 38–39 and 43.
- [Hin21]"""

NEWR1 = """\
  4.21–4.22 and (5.18)–(5.22); (4.64), (4.67), (4.71) and Corollary 4.18, pp. 38–39 and 43.
- [DR08] M. Dafermos, I. Rodnianski, *Lectures on black holes and linear waves*, arXiv:0811.0354v1. READ 2026-11-06:
  p. 40, Proposition 3.3.2 (the commutation with Ŷ and the sign of its first term); p. 41; p. 87, Theorem 7.2 and its
  proof (the commutation with the red-shift field Y, with κ_k > 0 on the horizon).
- [Hin21]"""

OLDR2 = """\
  (Theorem 22). READ 2026-10-21: section 7 (pp. 28–48), 9.3.2 (pp. 54–57), 10.4.2–10.5 (pp. 66–67)."""

NEWR2 = """\
  (Theorem 22). READ 2026-10-21: section 7 (pp. 28–48), 9.3.2 (pp. 54–57), 10.4.2–10.5 (pp. 66–67). READ 2026-11-06:
  p. 6, (16) and (20); pp. 8–9, (36) and (42); p. 12, (51); p. 49, (134)–(135); pp. 60–61, (170)–(174)."""

BLOCKS = [("8.2", OLD82, NEW82), ("Theorem 1 item 7", OLDT7, NEWT7), ("Proposition 3.3", OLD33, NEW33),
          ("Proposition 3.3 proof", OLD33b, NEW33b), ("8.2 orthonormal", OLD82o, NEW82o),
          ("Theorem 2 item 5", OLDT2, NEWT2), ("references [DR08]", OLDR1, NEWR1), ("references [HKW18]", OLDR2, NEWR2)]


def r13(control=False):
    paper = open(PAPER, encoding="utf-8").read()
    rows, ok = [], True
    for name, old, new in BLOCKS:
        if control:
            old = old[:-1] + "#"
        n_old, n_new = paper.count(old), paper.count(new)
        width = max(len(ln) for ln in (old + "\n" + new).splitlines())
        rows.append((name, n_old, n_new, width))
        ok &= n_old == 1 and n_new == 0 and width <= 121
    self_width = max(len(ln) for ln in open(os.path.abspath(__file__), encoding="utf-8").read().splitlines())
    proof = open(PROOF, encoding="utf-8").read()
    nth = [i for i in range(len(proof)) if proof.startswith("N-th order", i)]
    nth_ok = True
    for i in nth:                                                     # inside a quotation of an [amended D622 note
        start = proof.rfind("[amended D622", 0, i)
        para = proof.rfind("\n\n", 0, i)
        nth_ok &= start > para and proof.count('"', start, i) % 2 == 1
    seated = all(s_ in proof for s_ in ("**Lemma 10.1a (the red-shift commutation", "**Lemma 10.1b (the red-shift datum",
                                        "(iv-a) *Part VIII's data class", "(iv-b) *[HKW18]'s data class"))
    ok &= self_width <= 121 and nth_ok and seated
    say("  R13%s: (block, old count, new count, widest line): %s; this file's widest line %d; 'N-th order' in "
        "N1STAR-PROOF.md %d time(s), each inside an [amended D622 note: %s; Lemmas 10.1a-10.1b and (iv-a), (iv-b) "
        "seated: %s" % (" control (old text mutated)" if control else "", rows, self_width, len(nth), nth_ok, seated))
    return bool(ok)


CHECKS = [("R1", r1), ("R2", r2), ("R3", r3), ("R4", r4), ("R5", r5), ("R6", r6), ("R7", r7), ("R8", r8),
          ("R9", r9), ("R10", r10), ("R11", r11), ("R12", r12), ("R14", r14), ("R13", r13)]


def main():
    only = sys.argv[1:]
    ok = True
    for name, fn in CHECKS:
        if only and name not in only:
            continue
        good = fn()
        ctl = fn(control=True)
        say("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    say("EXIT %d" % (0 if ok else 1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
