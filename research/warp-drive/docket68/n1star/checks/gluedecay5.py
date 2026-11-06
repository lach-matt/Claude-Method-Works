#!/usr/bin/env python3
"""gluedecay5.py -- the norms, exponents and the distance kappa of GLUEDECAY5.md (which decaying perturbations
Theorem 4 (ii) reaches, directly or through gluing). Rounds 2-4 (R2.0-R4.0): every check runs against named mutants
of the code under test, each of which must fail.

The paper's section 8.7 (paper/RESPONSE-HL-5D.md) left open whether a perturbation decaying like r^(-a), 3/2 < a,
agrees on a ball B_R with data to which Theorem 4 (ii) applies, with smallness uniform as R -> oo. GLUEDECAY5.md
settles it. The norm is Hintz's (READ, [Hin26] (1.5) p. 2, Definition 2.6 p. 47, Definition 2.8 p. 48): coefficients of
rho^2, rho^3 in H^d(S^3) plus the remainder in rho^(l0) H_b^d with the b-density dr/r dw (PART-III-A-PREREQ.md 1.1).

  E1 (exact, sympy) Proposition 1 and the threshold. int_{r1}^R r^(2(l0 - a)) dr/r: finite as R -> oo iff a > l0,
     equal to r1^(2(l0-a))/(2(a - l0)); log(R/r1) at a = l0; (R^2 - r1^2)/2 at (a, l0) = (5/2, 7/2). With r = e^t,
     d_t^j (e^(-a t) psi(t)) = e^(-a t) sum_k C(j,k) (-a)^(j-k) psi^(k)(t), j <= 3, psi generic: b-derivatives keep
     the order. A rho^2 or rho^3 term is never a remainder: 2 l0 - 4 > 0, 2 l0 - 6 > 0. Mutant 'lebesgue': the
     density |dx| = r^4 dr/r dw, which moves the threshold to l0 + 2.
  E2 (exact; certified, mpmath interval arithmetic) Lemma 3.1. The Wronskian of e^(z_j u), j = 1..4, is
     e^((z_1+..+z_4) u) prod_(j<k) (z_k - z_j) (symbolic z). All ten entries of the closed-form Gram matrix of
     s^q cos log s, s^q sin log s, s^p1, s^p2 in L^2((1/2, 1), ds/s) agree with sympy's exact integrals and with
     quadrature (to 1e-35, at (a, l0) = (5/2, 7/2)). kappa(5/2, 7/2) from the closed forms equals kappa from a direct
     quadrature of the Gram matrix in s (no closed form), to 1e-25, and 7.6546e-4 to 1e-8 (the verifier's value).
     kappa^2 = lambda_min of the Schur complement is certified > 0 on the grid l0 = 13/4, 7/2, 15/4, a = 8/5, 2, 5/2,
     3, (3 + l0)/2, l0. Mutants: 'no_osc' (the class profile s^(l0-2) in place of the oscillating one: distance 0,
     the certificate fails), 'ss_sign' (the sign of the closed-form <f_s, f_s> flipped), 'lam_max' (lambda_max
     returned for lambda_min).
  E3 (exact; and pointwise and quadrature checks) Proposition 3's example. For Psi(x) = phi(|x|) x/|x| and
     gamma = A(r) xh xh + B(r) (delta - xh xh), generic phi, A, B: Psi^* gamma = A(phi) phi'^2 xh xh + B(phi)
     (phi/r)^2 (delta - xh xh), at three points of R^4 (r = 5, 7, 2). With phi = r + eps v, v = r^(1-a) cos log r:
     tr(Psi^* delta - delta) = 2 eps r^(-a) ((4 - a) cos log r - sin log r) + eps^2 (v'^2 + 3 v^2/r^2), exactly. With
     the Tangherlini term alpha = mu/r^2, exactly, r^(2+a) d_eps E|_0 = -2 mu (a c + s) and r^(2+2a) d_eps^2 E|_0 =
     mu (2 ((1-a) c - s)^2 - 8 c ((1-a) c - s) + 6 c^2), c = cos log r, s = sin log r; and, after log r -> t alone,
     neither has an r left. Pointwise, at r = 10^2, 10^3, a = 5/2, eps = 10^-6: (tau_mu - tau_0) r^(2+a)/(eps mu) is
     within 10^-3 of -2 (a c + s). Quadrature at (a, l0) = (5/2, 7/2) and (7/2, 7/2), eps = 1/100, mu = 1, R = 10^2,
     10^3, 10^4: D_R/(eps R^(l0-a)) within a relative 10^-2 of 2 A_a dist(log R + phi_a) and above 2 A_a kappa
     (1 - 10^-2), D_R the least-squares remainder of r^(l0) tau on (R/2, R) against r^(l0-2), r^(l0-3). Mutants:
     'coef3' (the three-dimensional coefficient 3 - a), 'second_r3' (the second-order expression times r^3), 'mu0'
     (mu = 0 in the pointwise and quadrature checks).
  E4 (exact) Proposition 4 and Corollary 4.3. (i) The fluxes: for explicit profiles of order a (energy: h = x x
     r^(-a-2); momentum: K = x1 delta r^(-a-2); centre of mass, N = x1: h = x1 x x r^(-a-3), and h = x1 delta r^(-a-1),
     whose terms in the gradient of N do not vanish; angular momentum, Y = W_12 x: K = (x (W x) + (W x) x) r^(-a-3))
     the flux over S_rho is computed exactly (sympy, exact moments of
     S^3) as c_d(a) rho^(2+d-a), c_d(a) != 0; so it tends to 0 iff a > 2 + d. (ii) The exponents, piecewise linear in
     (a, l0) on 3/2 <= a <= l0, 3 <= l0 <= 4, cut at a = 2, 3, checked at every vertex of each piece: the gluing
     terms' exponents below the box exponent min(0, 2 + d - a); the box radius not decaying where a charge of the
     perturbation need not vanish (a <= 2 + d); theta = O(eps R^(-a)); every piece of the glued norm O(eps
     R^(l0-a)); and the exponents of (5.2) derived from the box radii, p2exp = box(d = 0) and p3exp = max_d box(d),
     at every vertex. The fluxes' constants are asserted: c_d = 6 pi^2, 3 pi^2, (3/2) pi^2, (3/2) (a + 1) pi^2,
     2 pi^2. Mutants:
     'no_decouple' (mass and boost bounded only as the degree-1 charges), 'box_strong' (box exponent min(0, 1 + d - a):
     true as an inequality on T, but it decays where the charges need not vanish), 'energy_trsign' and 'mom_drop_x'
     (a sign and an index of the flux integrands), 'p3_strong' (p3exp = min(0, 2 - a)), 'box_weak' (box exponent
     min(0, 3 + d - a)), 'drop_lapse' (the terms in the gradient of N dropped).
  E5 (exact, sympy series) Lemma 4.1's inputs. (a) The spin enters the Kerr-Schild metric at rho^3: every component of
     h k k at spins (1/3, 1/5) minus that at zero spin starts at rho^3 or later, some at rho^3 (checks/mpdata5.py's
     mp_ingredients, one rational point of S^3). (b) A translation enters at rho^3. (c) A radial Hessian carries no
     momentum and no angular momentum: (d_i d_j f - Lap f delta_ij) x^i = -3 (f'/r) x_j (odd), (W x) . Hess f . x = 0.
     (d) Hintz's surface is not a Kerr-Schild slice: f' = 2 mu/(r^2 - mu) (III.B (3.3)) gives tr Hess f = 2 mu r^-3
     + O(r^-5). Mutants: 'mass' (a different mass in place of the spins: the difference starts at rho^2; a failed
     series raises instead of counting as a failure), 'dim3' (the three-dimensional Laplacian in (d): 0 at rho^3).
  E6 (text) GLUEDECAY5.md: every line at most 121 characters, and so every new block's line; section 8.5's blocks
     (a)-(h), against paper/RESPONSE-HL-5D.md (or the copy given by --paper) in either state, which it names (md5
     digits blanked, so a refreshed md5 column still matches). Every run checks both texts: the paper before seating
     and the paper seated, the one it is not in built from the other (all blocks applied, the zero md5 filled; or every
     new block replaced by its old). Before seating: each old block exactly once and no new block, the old blocks
     disjoint, (a) immediately followed by (b); with all blocks applied, section 8.7 still cites support8b.py M3 and
     cites GLUEDECAY5.md, and section 9's computational-support list, Appendix A, Appendix C (the source map) and
     Appendix D (the run list, the imports, the md5 table) carry gluedecay5.py and the note, no line over 121. Seated:
     each new block exactly once, disjoint, (a) immediately followed by (b), the old texts of (a)-(e), (g) gone, and
     the same places checked. Mutants, each acting on both texts in either state: 'char_a', 'char_b' (one character of
     the old and the new block changed), 'drop_c' (the seated text with old (c) in place of new (c)), 'drop_m3' (new
     (b) without its citation of support8b.py M3), 'seated_keep_old_a' (the seated text still holding old (a)).

Labels: computed (exact, sympy; E2's positivity certified by interval arithmetic; E3's instances by mpmath at 30
digits). Reach: E3's quadrature is an instance of Proposition 3, not its proof; E4 checks the exponents and the
flux scalings, not the constants C_1, C_P, R_P, R_G, L; E5 checks the expansions that Lemma 4.1 uses, not the gluing.

Run: python3 checks/gluedecay5.py [--paper PATH]   (about ninety seconds; E3 and E5 most of it). --paper checks
another copy of the paper, for instance one with section 8.5's blocks seated.
"""
import os
import sys
import textwrap
from fractions import Fraction as Fr

import mpmath as mpm
import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER = os.path.join(HERE, "..", "..", "paper", "RESPONSE-HL-5D.md")
DOC = os.path.join(HERE, "GLUEDECAY5.md")
MUT = None                                                             # the mutant under test, or None


def say(text):
    """print a report wrapped to 118 columns, continuation lines indented"""
    if MUT is not None:
        return
    for k, para in enumerate(text.split("\n")):
        print(textwrap.fill(para.strip(), 118, initial_indent="  " if k == 0 else "      ",
                            subsequent_indent="      "), flush=True)


# ---------------------------------------------------------------------------------------------------------- E1
def e1():
    r, r1, R, l0 = sp.symbols("r r1 R l0", positive=True)
    a = sp.symbols("a", positive=True)
    dens = (r**4 if MUT == "lebesgue" else 1) / r                      # the b-density dr/r
    ok = True
    for L0 in (sp.Rational(13, 4), sp.Rational(7, 2), sp.Rational(15, 4)):
        for A_ in (L0 + sp.Rational(1, 4), L0 + 1, sp.Rational(4)):
            I = sp.integrate(r**(2 * L0) * r**(-2 * A_) * dens, (r, r1, sp.oo))
            fin = bool(I.is_finite) if not isinstance(I, sp.Piecewise) else False
            ok &= fin and sp.simplify(I - r1**(2 * (L0 - A_)) / (2 * (A_ - L0))) == 0
    if not ok:
        return False
    Ieq = sp.integrate(r**(2 * l0) * r**(-2 * l0) * dens, (r, r1, R))
    ok &= sp.simplify(sp.expand_log(Ieq - sp.log(R / r1), force=True)) == 0
    Ibl = sp.integrate(r**(2 * sp.Rational(7, 2) - 2 * sp.Rational(5, 2)) * dens, (r, r1, R))
    ok &= sp.simplify(Ibl - (R**2 - r1**2) / 2) == 0
    psi = sp.Function("psi")
    t = sp.symbols("t", real=True)
    g = sp.exp(-a * t) * psi(t)                                        # r = e^t: r d_r = d_t
    bder = True
    for j in range(1, 4):
        g = sp.diff(g, t)
        claim = sp.exp(-a * t) * sum(sp.binomial(j, k) * (-a)**(j - k) * sp.diff(psi(t), t, k) for k in range(j + 1))
        bder &= sp.simplify(g - claim) == 0
    uniq = all(2 * L0 - 4 > 0 and 2 * L0 - 6 > 0 for L0 in (Fr(301, 100), Fr(7, 2), Fr(399, 100)))
    say("E1: int_r1^oo r^(2(l0-a)) dr/r = r1^(2(l0-a))/(2(a-l0)) at a > l0 (9 instances, l0 = 13/4, 7/2, 15/4), "
        "log(R/r1) at a = l0 and (R^2 - r1^2)/2 at (a, l0) = (5/2, 7/2): %s; d_t^j [e^(-at) psi] = e^(-at) sum_k C(j,k) "
        "(-a)^(j-k) psi^(k), j <= 3: %s; rho^2, rho^3 terms never remainders (2 l0 - 4, 2 l0 - 6 > 0): %s"
        % (ok, bder, uniq))
    return ok and bder and uniq


# ---------------------------------------------------------------------------------------------------------- E2
def gram_closed(q, p1, p2, ivm=mpm.iv):
    """Gram matrix of (f_c, f_s, g1, g2) = (e^(qu) cos u, e^(qu) sin u, e^(p1 u), e^(p2 u)) on u in (-log 2, 0)"""
    L = ivm.log(2)

    def cint(c, w):                                                    # int_{-L}^0 e^((c + i w) u) du = (Re, Im)
        E, co, si = ivm.exp(-c * L), ivm.cos(w * L), ivm.sin(w * L)
        if c == 0 and w == 0:
            return L, ivm.mpf(0)
        den = c * c + w * w
        return ((c * (1 - E * co) + w * E * si) / den, (c * E * si - w * (1 - E * co)) / den)
    cc = (cint(2 * q, 0)[0] + cint(2 * q, 2)[0]) / 2
    ss = (cint(2 * q, 0)[0] - cint(2 * q, 2)[0]) / 2
    if MUT == "ss_sign":
        ss = -ss
    cs = cint(2 * q, 2)[1] / 2
    rows = [[cc, cs], [cs, ss]]
    cg = [[cint(q + p, 1)[0], cint(q + p, 1)[1]] for p in (p1, p2)]   # <g_p, f_c>, <g_p, f_s>
    gg = [[cint(pa + pb, 0)[0] for pb in (p1, p2)] for pa in (p1, p2)]
    return rows, cg, gg


def schur(rows, cg, gg):
    det = gg[0][0] * gg[1][1] - gg[0][1] * gg[1][0]
    inv = [[gg[1][1] / det, -gg[0][1] / det], [-gg[1][0] / det, gg[0][0] / det]]
    S = [[None, None], [None, None]]
    for i in range(2):
        for j in range(2):
            corr = sum(cg[k][i] * inv[k][l] * cg[l][j] for k in range(2) for l in range(2))
            S[i][j] = rows[i][j] - corr
    return S


def lam_min(S, ivm=mpm.mp):
    tr, det = S[0][0] + S[1][1], S[0][0] * S[1][1] - S[0][1] * S[1][0]
    sgn = 1 if MUT == "lam_max" else -1
    return tr / 2 + sgn * ivm.sqrt((tr / 2)**2 - det), det


def kappa_closed(a_, l0_, ivm=mpm.mp):
    S = schur(*gram_closed(ivm.mpf(l0_) - ivm.mpf(a_), ivm.mpf(l0_) - 2, ivm.mpf(l0_) - 3, ivm))
    lam, det = lam_min(S, ivm)
    return S, det, lam


def kappa_quad(a_, l0_):
    """kappa from a direct quadrature of the Gram matrix in s on (1/2, 1), ds/s: no closed form"""
    q, p1, p2 = l0_ - a_, l0_ - 2, l0_ - 3
    fs = [lambda s: s**q * mpm.cos(mpm.log(s)), lambda s: s**q * mpm.sin(mpm.log(s)), lambda s: s**p1,
          lambda s: s**p2]
    G = [[mpm.quad(lambda s: fs[i](s) * fs[j](s) / s, [mpm.mpf(1) / 2, 1]) for j in range(4)] for i in range(4)]
    S = schur([G[0][:2], G[1][:2]], [G[2][:2], G[3][:2]], [G[2][2:], G[3][2:]])
    tr, det = S[0][0] + S[1][1], S[0][0] * S[1][1] - S[0][1] * S[1][0]
    return mpm.sqrt(tr / 2 - mpm.sqrt((tr / 2)**2 - det))


def e2():
    mpm.iv.dps = 50
    mpm.mp.dps = 50
    if MUT == "no_osc":                                                # s^(l0-2) itself: distance from the span
        l0_ = mpm.iv.mpf(7) / 2
        p1, p2 = l0_ - 2, l0_ - 3
        L = mpm.iv.log(2)

        def g(c):
            return (1 - mpm.iv.exp(-c * L)) / c
        G = [[g(2 * p1), g(p1 + p2), g(p1 + p1)], [g(p1 + p2), g(2 * p2), g(p2 + p1)],
             [g(p1 + p1), g(p1 + p2), g(2 * p1)]]                       # (g1, g2, s^(l0-2) = g1): rank 2
        d2 = G[2][2] - (G[2][0] * (G[1][1] * G[0][2] - G[0][1] * G[1][2])
                        + G[2][1] * (G[0][0] * G[1][2] - G[1][0] * G[0][2])) / (G[0][0] * G[1][1] - G[0][1]**2)
        return d2.a > 0                                                # certified positive? it is not (contains 0)
    z = sp.symbols("z1:5")
    u = sp.symbols("u")
    W = sp.Matrix(4, 4, lambda k, j: sp.diff(sp.exp(z[j] * u), u, k))
    vdm = sp.prod([z[k] - z[j] for j in range(4) for k in range(j + 1, 4)])
    wr = sp.simplify(W.det() - sp.exp(sum(z) * u) * vdm) == 0
    # all ten closed-form entries against sympy's exact integrals and quadrature, at (a, l0) = (5/2, 7/2)
    q, p1, p2 = sp.Rational(1), sp.Rational(3, 2), sp.Rational(1, 2)
    Ls = sp.log(2)
    fns = {"c": sp.exp(q * u) * sp.cos(u), "s": sp.exp(q * u) * sp.sin(u), "1": sp.exp(p1 * u), "2": sp.exp(p2 * u)}
    pairs = ["cc", "ss", "cs", "1c", "1s", "2c", "2s", "11", "12", "22"]
    rows, cg, gg = gram_closed(mpm.mpf(1), mpm.mpf(3) / 2, mpm.mpf(1) / 2, mpm.mp)
    vals = {"cc": rows[0][0], "ss": rows[1][1], "cs": rows[0][1], "1c": cg[0][0], "1s": cg[0][1], "2c": cg[1][0],
            "2s": cg[1][1], "11": gg[0][0], "12": gg[0][1], "22": gg[1][1]}
    cf = True
    for pq in pairs:
        ex = sp.N(sp.integrate(fns[pq[0]] * fns[pq[1]], (u, -Ls, 0)), 45)
        fa, fb = sp.lambdify(u, fns[pq[0]], "mpmath"), sp.lambdify(u, fns[pq[1]], "mpmath")
        qd = mpm.quad(lambda x: fa(x) * fb(x), [-mpm.log(2), 0])
        cf &= abs(ex - vals[pq]) < mpm.mpf(10)**-35 and abs(qd - vals[pq]) < mpm.mpf(10)**-35
    kc = mpm.sqrt(kappa_closed(mpm.mpf(5) / 2, mpm.mpf(7) / 2)[2])
    kq = kappa_quad(mpm.mpf(5) / 2, mpm.mpf(7) / 2)
    kok = abs(kc - kq) < mpm.mpf(10)**-25 and abs(kc - mpm.mpf("7.6546e-4")) < mpm.mpf(10)**-8
    cert, table = True, []
    for L0 in (Fr(13, 4), Fr(7, 2), Fr(15, 4)):
        for A_ in (Fr(8, 5), Fr(2), Fr(5, 2), Fr(3), (3 + L0) / 2, L0):
            ai, li = mpm.iv.mpf(A_.numerator) / A_.denominator, mpm.iv.mpf(L0.numerator) / L0.denominator
            S, det, _ = kappa_closed(ai, li, mpm.iv)
            pos = S[0][0].a > 0 and det.a > 0
            cert &= pos
            lam = kappa_closed(mpm.mpf(A_.numerator) / A_.denominator, mpm.mpf(L0.numerator) / L0.denominator)[2]
            table.append((L0, A_, lam))
    say("E2: Wronskian of e^(z_j u) = e^(sum z u) prod (z_k - z_j), symbolic: %s; all ten Gram closed forms = sympy "
        "exact = quadrature (1e-35): %s; kappa(5/2, 7/2) = %s from the closed forms, %s from a direct quadrature in s "
        "(agree to 1e-25, and with 7.6546e-4 to 1e-8): %s; kappa^2 = lambda_min(Schur), certified > 0 at every grid "
        "point: %s" % (wr, cf, mpm.nstr(kc, 8), mpm.nstr(kq, 8), kok, cert))
    if MUT is None:
        for L0 in (Fr(13, 4), Fr(7, 2), Fr(15, 4)):
            row = ["a = %s: kappa = %s" % (A_, mpm.nstr(mpm.sqrt(lam), 4)) for (l_, A_, lam) in table if l_ == L0]
            print("      l0 = %-5s " % L0 + "  ".join(row[:3]) + "\n" + " " * 17 + "  ".join(row[3:]), flush=True)
    return wr and cf and kok and cert


# ---------------------------------------------------------------------------------------------------------- E3
def trh(x, a_, e_, m_):
    """the exact trace of Psi^*(gamma) - gamma, gamma = (1 + m/r^2) dr^2 + r^2 dOmega^2, phi = r + e r^(1-a) cos log r"""
    vv = x**(1 - a_) * mpm.cos(mpm.log(x))
    dv = x**(-a_) * ((1 - a_) * mpm.cos(mpm.log(x)) - mpm.sin(mpm.log(x)))
    p_, dp_ = x + e_ * vv, 1 + e_ * dv
    return dp_**2 * (1 + m_ / p_**2) - 1 - m_ / x**2 + 3 * ((p_ / x)**2 - 1)


def e3():
    r, a, eps, mu = sp.symbols("r a epsilon mu", positive=True)
    c_, s_ = sp.cos(sp.log(r)), sp.sin(sp.log(r))
    v = r**(1 - a) * c_
    ph = r + eps * v
    dph = sp.diff(ph, r)
    lhs = dph**2 - 1 + 3 * ((ph / r)**2 - 1)
    coef = (3 - a) if MUT == "coef3" else (4 - a)
    rhs = 2 * eps * r**(-a) * (coef * c_ - s_) + eps**2 * (sp.diff(v, r)**2 + 3 * (v / r)**2)
    trok = sp.simplify(sp.expand(lhs - rhs)) == 0
    if not trok:
        return False
    E = mu * dph**2 / ph**2 - mu / r**2                                # alpha(phi) phi'^2 - alpha(r), alpha = mu/r^2
    E1 = sp.simplify(r**(2 + a) * sp.diff(E, eps).subs(eps, 0))
    E2_ = sp.simplify(r**(2 + 2 * a) * sp.diff(E, eps, 2).subs(eps, 0))
    if MUT == "second_r3":
        E2_ = E2_ * r**3
    w = (1 - a) * c_ - s_
    first = sp.simplify(E1 - (-2 * mu * (a * c_ + s_))) == 0
    second = sp.simplify(sp.expand(E2_ - mu * (2 * w**2 - 8 * c_ * w + 6 * c_**2))) == 0
    tt = sp.symbols("tt", real=True)
    rfree = all(not sp.simplify(sp.powsimp(sp.expand(e_), force=True).subs(sp.log(r), tt)).has(r) for e_ in (E1, E2_))
    if not (first and second and rfree):
        return False
    mpm.mp.dps = 30
    m_pt = mpm.mpf(0) if MUT == "mu0" else mpm.mpf(1)
    pt_ok, A5 = True, mpm.mpf(5) / 2
    for x in (mpm.mpf(10)**2, mpm.mpf(10)**3):
        e_ = mpm.mpf(10)**-6
        val = (trh(x, A5, e_, m_pt) - trh(x, A5, e_, 0)) * x**(2 + A5) / e_
        pred = -2 * (A5 * mpm.cos(mpm.log(x)) + mpm.sin(mpm.log(x)))
        pt_ok &= abs(val - pred) < mpm.mpf(10)**-3
    if not pt_ok:
        return False
    X = sp.symbols("x1:5", real=True)
    rr = sp.sqrt(sum(xi**2 for xi in X))
    phi, A, B = sp.Function("phi"), sp.Function("A"), sp.Function("B")
    t = sp.symbols("t", positive=True)
    Psi = sp.Matrix([phi(rr) * xi / rr for xi in X])
    J = Psi.jacobian(sp.Matrix(X))
    Pyy = Psi * Psi.T / phi(rr)**2                                     # yhat yhat at y = Psi(x), |y| = phi(r) > 0
    gam = A(phi(rr)) * Pyy + B(phi(rr)) * (sp.eye(4) - Pyy)
    pull = J.T * gam * J
    xh = sp.Matrix([xi / rr for xi in X])
    P = xh * xh.T
    dphi = sp.diff(phi(t), t).subs(t, rr)
    claim = A(phi(rr)) * dphi**2 * P + B(phi(rr)) * (phi(rr) / rr)**2 * (sp.eye(4) - P)
    pullok = True
    for pt in ((1, 2, 2, 4), (2, 3, 6, 0), (1, 1, 1, 1)):
        D = (pull - claim).subs(dict(zip(X, pt))).doit()
        pullok &= all(sp.simplify(e_) == 0 for e_ in D)
    inst_ok, lines = True, []
    for (A_, L0) in ((mpm.mpf(5) / 2, mpm.mpf(7) / 2), (mpm.mpf(7) / 2, mpm.mpf(7) / 2)):
        Aa = mpm.sqrt((4 - A_)**2 + 1)
        pha = mpm.atan2(1, 4 - A_)                                     # (4-a) cos x - sin x = A_a cos(x + phi_a)
        S = schur(*gram_closed(L0 - A_, L0 - 2, L0 - 3, mpm.mp))
        trS, detS = S[0][0] + S[1][1], S[0][0] * S[1][1] - S[0][1]**2
        kap = mpm.sqrt(trS / 2 - mpm.sqrt((trS / 2)**2 - detS))
        e_ = mpm.mpf(1) / 100
        for RR in (mpm.mpf(10)**2, mpm.mpf(10)**3, mpm.mpf(10)**4):
            fns = [lambda s: (RR * s)**L0 * trh(RR * s, A_, e_, m_pt), lambda s: s**(L0 - 2), lambda s: s**(L0 - 3)]
            G = [[mpm.quad(lambda s: fns[i](s) * fns[j](s) / s, [mpm.mpf(1) / 2, 1]) for j in range(3)]
                 for i in range(3)]
            sol = mpm.lu_solve(mpm.matrix([[G[1][1], G[1][2]], [G[2][1], G[2][2]]]), mpm.matrix([G[0][1], G[0][2]]))
            D2 = G[0][0] - (sol[0] * G[0][1] + sol[1] * G[0][2])
            ratio = mpm.sqrt(D2) / (e_ * RR**(L0 - A_))
            th = mpm.log(RR) + pha
            vv2 = (mpm.cos(th), -mpm.sin(th))
            pred = 2 * Aa * mpm.sqrt(sum(vv2[i] * S[i][j] * vv2[j] for i in range(2) for j in range(2)))
            inst_ok &= abs(ratio / pred - 1) < mpm.mpf(10)**-2 and ratio > 2 * Aa * kap * (1 - mpm.mpf(10)**-2)
            lines.append("(a, l0) = (%s, %s), R = %s: D_R/(eps R^(l0-a)) = %s, 2 A_a dist = %s, 2 A_a kappa %s"
                         % (mpm.nstr(A_, 3), mpm.nstr(L0, 3), mpm.nstr(RR, 3), mpm.nstr(ratio, 6),
                            mpm.nstr(pred, 6), mpm.nstr(2 * Aa * kap, 6)))
    say("E3: tr(Psi^* delta - delta) identity: %s; r^(2+a) d_eps E|_0 = -2 mu (a c + s): %s; r^(2+2a) d_eps^2 E|_0 = "
        "mu (2 w^2 - 8 c w + 6 c^2), w = (1-a) c - s: %s; both free of r once log r -> t: %s; pointwise Tangherlini "
        "term (r = 10^2, 10^3): %s; Psi^* of a radial tensor (generic phi, A, B, three points): %s; quadrature "
        "instance of Proposition 3 (within 1e-2 of the prediction, above the kappa bound): %s"
        % (trok, first, second, rfree, pt_ok, pullok, inst_ok))
    if MUT is None:
        for ln in lines:
            print("      " + ln, flush=True)
    return pullok and inst_ok


# ---------------------------------------------------------------------------------------------------------- E4
PIECES = [[(Fr(3, 2), Fr(3)), (Fr(3, 2), Fr(4)), (Fr(2), Fr(3)), (Fr(2), Fr(4))],
          [(Fr(2), Fr(3)), (Fr(2), Fr(4)), (Fr(3), Fr(3)), (Fr(3), Fr(4))],
          [(Fr(3), Fr(3)), (Fr(3), Fr(4)), (Fr(4), Fr(4))]]           # 3/2 <= a <= 2, 2 <= a <= 3, 3 <= a <= l0


def holds(fun, strict, excl=(), where=lambda a_, l_: True):
    """fun(a, l0) <= 0 at every vertex of each piece (linear there) where 'where' holds; < 0 at the vertices off the
    excluded faces"""
    ok = True
    for pc in PIECES:
        for (a_, l_) in pc:
            if not where(a_, l_):
                continue
            val = fun(a_, l_)
            ok &= val <= 0
            if strict and not any(face(a_, l_) for face in excl):
                ok &= val < 0
    return ok


def s3_moment(alpha):
    """int over S^3 of w^alpha (exact)"""
    if any(k % 2 for k in alpha):
        return sp.Integer(0)
    b = [sp.Rational(k + 1, 2) for k in alpha]
    return 2 * sp.prod([sp.gamma(x) for x in b]) / sp.gamma(sum(b))


def sphere_flux(expr, X, w, rho):
    """the flux over S_rho of expr dS, expr a function of x: |x|^2 -> rho^2, then x = rho w, and the monomials in w
    integrated exactly over S^3"""
    e0 = expr.subs(sum(xi**2 for xi in X), rho**2)
    e_ = sp.expand(sp.powsimp(sp.expand(e0.subs({X[i]: rho * w[i] for i in range(4)})), force=True))
    poly = sp.Poly(e_, *w)
    tot = sum(cf * s3_moment(mon) for mon, cf in poly.terms())
    return sp.simplify(tot * rho**3)


def fluxes():
    """exact fluxes of explicit order-a profiles: (energy, momentum, centre of mass, angular momentum)"""
    X = sp.symbols("x1:5", real=True)
    a, rho = sp.symbols("a rho", positive=True)
    w = sp.symbols("w1:5", real=True)
    rr = sp.sqrt(sum(xi**2 for xi in X))
    nu = [xi / rr for xi in X]
    out = {}
    h = sp.Matrix(4, 4, lambda i, j: X[i] * X[j] * rr**(-a - 2))                       # order a, energy
    tr_h = sum(h[i, i] for i in range(4))
    sg = 1 if MUT == "energy_trsign" else -1
    be = sum((sum(sp.diff(h[i, j], X[j]) for j in range(4)) + sg * sp.diff(tr_h, X[i])) * nu[i] for i in range(4))
    out["energy (d = 0)"] = (be, 0)
    K = sp.Matrix(4, 4, lambda i, j: (X[0] if i == j else 0) * rr**(-a - 2))           # order a + 1, momentum e_1
    trK = sum(K[i, i] for i in range(4))
    jj = 1 if MUT == "mom_drop_x" else 0
    bm = -2 * sum((K[0, j] - (trK if j == jj else 0)) * nu[j] for j in range(4))
    out["momentum (d = 0)"] = (bm, 0)
    N = X[0]
    lapse = 0 if MUT == "drop_lapse" else 1                            # the terms with the gradient of N = x1

    def b_com(hh):
        trh_ = sum(hh[i, i] for i in range(4))
        return sum((N * (sum(sp.diff(hh[i, j], X[j]) for j in range(4)) - sp.diff(trh_, X[i]))
                    - lapse * (sum(sp.diff(N, X[j]) * hh[i, j] for j in range(4)) - sp.diff(N, X[i]) * trh_)) * nu[i]
                   for i in range(4))
    h3 = sp.Matrix(4, 4, lambda i, j: X[0] * X[i] * X[j] * rr**(-a - 3))               # order a, centre of mass
    out["centre of mass (d = 1)"] = (b_com(h3), 1)
    h4 = sp.Matrix(4, 4, lambda i, j: (X[0] if i == j else 0) * rr**(-a - 1))           # order a: its N-gradient terms
    out["centre of mass, x1 delta (d = 1)"] = (b_com(h4), 1)                            # do not vanish
    Wx = [X[1], -X[0], 0, 0]                                                           # Y = W_12 x (a rotation)
    Ka = sp.Matrix(4, 4, lambda i, j: (X[i] * Wx[j] + X[j] * Wx[i]) * rr**(-a - 3))   # order a + 1
    trKa = sum(Ka[i, i] for i in range(4))
    Yv = [-X[1], X[0], 0, 0]                                                           # Y = W x with W_12 = 1
    ba = -2 * sum((sum(Yv[j] * Ka[i, j] for j in range(4)) - Yv[i] * trKa) * nu[i] for i in range(4))
    out["angular momentum (d = 1)"] = (ba, 1)
    res = {}
    for name, (expr, d) in out.items():
        fl = sphere_flux(expr, X, w, rho)
        coef = sp.simplify(fl / rho**(2 + d - a))
        res[name] = (d, coef, not coef.has(rho) and all(sp.simplify(coef.subs(a, sp.Rational(k_, 4))) != 0
                                                         for k_ in (7, 10, 14)))
    return res, a, rho


def e4():
    res, a, rho = fluxes()
    want = {"energy (d = 0)": 6 * sp.pi**2, "momentum (d = 0)": 3 * sp.pi**2,
            "centre of mass (d = 1)": sp.Rational(3, 2) * sp.pi**2, "angular momentum (d = 1)": 2 * sp.pi**2,
            "centre of mass, x1 delta (d = 1)": sp.Rational(3, 2) * sp.pi**2 * (a + 1)}
    flux_ok = all(v[2] for v in res.values()) and all(sp.simplify(res[k_][1] - w_) == 0 for k_, w_ in want.items())
    lim_ok = True
    for name, (d, coef, _) in res.items():
        for A_ in (Fr(8, 5), Fr(2), Fr(5, 2), Fr(3), Fr(13, 4), Fr(7, 2)):
            cA = coef.subs(a, sp.Rational(A_.numerator, A_.denominator))
            L = sp.limit(cA * rho**(2 + d - sp.Rational(A_.numerator, A_.denominator)), rho, sp.oo)
            lim_ok &= (L == 0) == (A_ > 2 + d) and cA != 0
    m0 = lambda x: min(Fr(0), x)                                       # noqa: E731
    p2exp = (lambda a_: m0(3 - a_)) if MUT == "no_decouple" else (lambda a_: m0(2 - a_))
    if MUT == "p3_strong":
        p3exp = lambda a_: m0(2 - a_)                                  # noqa: E731
    else:
        p3exp = lambda a_: m0(3 - a_)                                  # noqa: E731
    on_a32 = lambda a_, l_: a_ == Fr(3, 2)                            # noqa: E731
    on_al0 = lambda a_, l_: a_ == l_                                  # noqa: E731
    res_i = {}
    for d in (0, 1):
        if MUT == "box_strong":
            box = lambda a_, d=d: m0(1 + d - a_)                      # noqa: E731
        else:
            box = lambda a_, d=d: m0((3 if MUT == "box_weak" else 2) + d - a_)   # noqa: E731
        res_i["T: d-a<0 (d=%d)" % d] = holds(lambda a_, l_, d=d: d - a_, True, (on_a32,))
        res_i["T: d+2-2a<0 (d=%d)" % d] = holds(lambda a_, l_, d=d: d + 2 - 2 * a_, True, (on_a32,))
        for name, ex in (("d-2+p2", lambda a_, d=d: d - 2 + p2exp(a_)), ("d-3+p3", lambda a_, d=d: d - 3 + p3exp(a_)),
                         ("d-a", lambda a_, d=d: d - a_), ("d+2-2a", lambda a_, d=d: d + 2 - 2 * a_)):
            res_i["box %s < box exponent (d=%d)" % (name, d)] = holds(lambda a_, l_, ex=ex, box=box: ex(a_) - box(a_),
                                                                     True, (on_a32,))
        res_i["box radius constant where a <= 2+d (d=%d, def.)" % d] = holds(lambda a_, l_, box=box: -box(a_), False,
                                                            where=lambda a_, l_, d=d: a_ <= 2 + d)
    boxes = [(lambda a_, d=d: m0((1 if MUT == "box_strong" else (3 if MUT == "box_weak" else 2)) + d - a_))
             for d in (0, 1)]
    verts = {v_ for pc in PIECES for v_ in pc}
    res_i["(5.2): p2exp = box(d=0) at every vertex"] = all(p2exp(a_) == boxes[0](a_) for (a_, l_) in verts)
    res_i["(5.2): p3exp = max_d box(d) at every vertex"] = all(p3exp(a_) == max(b_(a_) for b_ in boxes)
                                                             for (a_, l_) in verts)
    res_i["theta: p2 - 2 <= -a"] = holds(lambda a_, l_: p2exp(a_) - 2 + a_, False)
    res_i["theta: p3 - 3 <= -a"] = holds(lambda a_, l_: p3exp(a_) - 3 + a_, False)
    res_i["norm: p2 + l0 - 2 <= l0 - a"] = holds(lambda a_, l_: p2exp(a_) + l_ - 2 - (l_ - a_), False)
    res_i["norm: p3 + l0 - 3 <= l0 - a"] = holds(lambda a_, l_: p3exp(a_) + l_ - 3 - (l_ - a_), False)
    res_i["norm: p3 + l0 - 4 <= l0 - a (outer)"] = holds(lambda a_, l_: p3exp(a_) + l_ - 4 - (l_ - a_), False)
    res_i["norm: 0 <= l0 - a (coefficients, compact part)"] = holds(lambda a_, l_: -(l_ - a_), False)
    res_i["norm: l0 - a > 0 off a = l0"] = holds(lambda a_, l_: -(l_ - a_), True, (on_al0,))
    say("E4: exact fluxes over S_rho of order-a profiles are c_d rho^(2+d-a), with c_d = 6 pi^2, 3 pi^2, (3/2) pi^2, "
        "(3/2) (a + 1) pi^2 and 2 pi^2 asserted: %s; they tend to 0 iff a > 2 + d (a = 8/5, 2, 5/2, 3, 13/4, 7/2): %s"
        % (flux_ok, lim_ok))
    if MUT is None:
        for name, (d, coef, _) in res.items():
            print("        %-34s c(a) = %s" % (name, sp.factor(coef)), flush=True)
        print("      the exponent inequalities:", flush=True)
        for k_, v_ in res_i.items():
            print("        %-48s %s" % (k_, v_), flush=True)
    return flux_ok and lim_ok and all(res_i.values())


# ---------------------------------------------------------------------------------------------------------- E5
_E5 = {}


def e5():
    sys.path.insert(0, os.path.join(HERE, "checks"))
    import mpdata5 as md
    rho, mu = md.rho, md.mu
    if MUT != "mass" and "series" in _E5:                              # the series do not depend on 'dim3'
        lows, tl = _E5["series"]
        return e5_rest(lows, tl)
    om = md.POINTS[1]
    if MUT == "mass":                                                  # a mass change in place of the spins
        u, h, k, _ = md.mp_ingredients(om, 0, 0)
        h = h.subs(mu, 2 * mu)
    else:
        u, h, k, _ = md.mp_ingredients(om, sp.Rational(1, 3), sp.Rational(1, 5))
    u0, h0, k0, _ = md.mp_ingredients(om, 0, 0)
    kk, kk0 = [sp.Integer(1)] + k, [sp.Integer(1)] + k0
    lows = []
    for i in range(5):
        for j in range(i, 5):
            okp, lo = md.powers(h * kk[i] * kk[j] - h0 * kk0[i] * kk0[j], rho, 5)
            if not okp:
                raise RuntimeError("E5 (a): a series with a log or a fractional power, component %d %d" % (i, j))
            lows.append(99 if lo is None else lo)
    spin = min(lows) >= 3 and 3 in lows
    if not spin:
        return False
    c = (1, -2, sp.Rational(1, 3), 0)
    x = [om[i] / rho for i in range(4)]
    xc = [x[i] + c[i] for i in range(4)]
    n2, n2c = sum(e_**2 for e_ in x), sum(e_**2 for e_ in xc)
    tl = []
    for i in range(4):
        for j in range(i, 4):
            ok_, lo = md.powers(mu * xc[i] * xc[j] / n2c**2 - mu * x[i] * x[j] / n2**2, rho, 5)
            if not ok_:
                raise RuntimeError("E5 (b): a series with a log or a fractional power")
            tl.append(99 if lo is None else lo)
    if MUT is None:
        _E5["series"] = (lows, tl)
    return e5_rest(lows, tl)


def e5_rest(lows, tl):
    spin = min(lows) >= 3 and 3 in lows
    trans = min(tl) == 3
    X = sp.symbols("x1:5", real=True)
    rr = sp.sqrt(sum(e_**2 for e_ in X))
    H = sp.hessian(sp.Function("f")(rr), X)
    lap = sum(H[i, i] for i in range(4))
    t = sp.symbols("t", positive=True)
    fp = sp.diff(sp.Function("f")(t), t).subs(t, rr)
    mom = all(sp.simplify((sum((H[i, j] - (lap if i == j else 0)) * X[i] for i in range(4))
                           + 3 * fp * X[j] / rr).doit()) == 0 for j in range(4))
    Wm = sp.Matrix(4, 4, lambda i, j: 1 if (i, j) == (0, 1) else (-1 if (i, j) == (1, 0) else 0))
    Wm2 = sp.Matrix(4, 4, lambda i, j: 1 if (i, j) == (1, 3) else (-1 if (i, j) == (3, 1) else 0))
    ang = all(sp.simplify(((W_ * sp.Matrix(X)).T * H * sp.Matrix(X))[0, 0]) == 0 for W_ in (Wm, Wm2))
    r, m = sp.symbols("r m", positive=True)
    f1 = 2 * m / (r**2 - m)
    nlap = 2 if MUT == "dim3" else 3
    trH = sp.series(sp.diff(f1, r) + nlap * f1 / r, r, sp.oo, 6).removeO()
    graph = sp.simplify(sp.limit(r**3 * trH, r, sp.oo) - 2 * m) == 0
    say("E5: (a) spin enters the Kerr-Schild metric at rho^%s (15 components, one point, spins (1/3, 1/5)): %s; (b) "
        "translation at rho^%s: %s; (c) radial Hessian: (Hess f - Lap f delta) x = -3 (f'/r) x and (W x) . Hess f . x "
        "= 0: %s, %s; (d) tr Hess f = 2 mu r^-3 + ... for f' = 2 mu/(r^2 - mu): %s"
        % (min(lows), spin, min(tl), trans, mom, ang, graph))
    return spin and trans and mom and ang and graph


# ---------------------------------------------------------------------------------------------------------- E6
def block(lines, tag):
    """the fenced block after the line equal to tag (which must occur once)"""
    idx = [k for k, l_ in enumerate(lines) if l_.strip() == tag]
    if len(idx) != 1:
        raise RuntimeError("E6: %s occurs %d times in GLUEDECAY5.md" % (tag, len(idx)))
    j = idx[0] + 1
    while not lines[j].startswith("```"):
        j += 1
    k = j + 1
    while not lines[k].startswith("```"):
        k += 1
    return "\n".join(lines[j + 1:k])


TAGS = "abcdefgh"                                                      # the current blocks; (a), (b) adjacent
GONE = "abcdeg"                       # blocks whose old text is gone once seated ((f), (h) keep theirs inside the new)
SECTION = "8.5"                                                        # the section of GLUEDECAY5.md holding them


def norm(t):
    """md5 digits blanked, length kept, so that a seated paper whose md5 column was refreshed still matches"""
    import re
    return re.sub(r"`[0-9a-f]{32}`", lambda m_: "`" + "x" * 32 + "`", t)


def apparatus(text):
    """the places that must carry the change, in a paper with the blocks in place"""
    import re

    def part(start, end):
        a0 = text.find(start)
        return text[a0:text.find(end, a0 + len(start))] if a0 >= 0 else ""
    s87 = part("### 8.7 ", "### 8.8 ")
    s9 = part("- **Computational support.**", "\n\n")                 # the item ends at a blank line
    sA = part("## Appendix A.", "## Appendix B.")
    sC = part("## Appendix C.", "## Appendix D.")
    sD = part("## Appendix D.", "The paper's own md5")
    return {
        "8.7 cites support8b.py M3 and GLUEDECAY5.md": "`docket68/n1star/checks/support8b.py` M3" in s87
        and "GLUEDECAY5.md" in s87,
        "section 9 lists gluedecay5.py": "`checks/gluedecay5.py`" in s9,
        "Appendix A has its entry": "- `checks/gluedecay5.py` E1–E6" in sA,
        "Appendix C maps it and the note": "checks/gluedecay5.py` E1–E6 |" in sC and "GLUEDECAY5.md" in sC,
        "Appendix D runs it and records its import": "python3 checks/gluedecay5.py" in sD
        and "`checks/gluedecay5.py` import" in sD,
        "Appendix D's md5 rows": all(re.search(r"^\| `docket68/n1star/%s` \| `[0-9a-f]{32}` \|$" % re.escape(f_),
                                               sD, re.M)
                                     for f_ in ("checks/gluedecay5.py", "checks/gluedecay5.out", "GLUEDECAY5.md",
                                                "proof5/PART-V-GLUING.md")),
        "lines <= 121": max(len(l_) for l_ in text.split("\n")) <= 121,
    }


def seated_ok(text, news, olds):
    """the seated state: every new block once, disjoint, (a) then (b), the old texts of GONE absent, the apparatus"""
    T = norm(text)
    N = {t_: norm(news[t_]) for t_ in TAGS}
    if not all(T.count(N[t_]) == 1 for t_ in TAGS) or any(T.count(norm(olds[t_])) for t_ in GONE):
        return False
    spans = sorted((T.find(N[t_]), T.find(N[t_]) + len(N[t_])) for t_ in TAGS)
    disjoint = all(spans[k][1] < spans[k + 1][0] for k in range(len(spans) - 1))
    adj = T.find(N["a"]) + len(N["a"]) + 1 == T.find(N["b"])
    return disjoint and adj and all(apparatus(text).values())


def swap(text, frm, to):
    """text with its one occurrence of frm (located with md5 digits blanked) replaced by to; None if not exactly one"""
    T, F = norm(text), norm(frm)
    if T.count(F) != 1:
        return None
    k = T.find(F)
    return text[:k] + to + text[k + len(frm):]


def pre_ok(text, olds, news):
    """the state before seating: each old block once, no new block, disjoint, (a) then (b); and the places checked in
    a copy with all blocks applied"""
    T = norm(text)
    if not all(T.count(norm(olds[t_])) == 1 for t_ in TAGS) or any(T.count(norm(news[t_])) for t_ in TAGS):
        return False, {}
    spans = sorted((T.find(norm(olds[t_])), T.find(norm(olds[t_])) + len(olds[t_]), t_) for t_ in TAGS)
    disjoint = all(spans[k][1] < spans[k + 1][0] for k in range(len(spans) - 1))
    adj = T.find(norm(olds["a"])) + len(olds["a"]) + 1 == T.find(norm(olds["b"]))
    applied = text
    for (s0, s1, t_) in reversed(spans):
        applied = applied[:s0] + news[t_] + applied[s1:]
    need = apparatus(applied)
    return disjoint and adj and all(need.values()), need


def e6():
    doc = open(DOC, encoding="utf-8").read()
    paper = open(PAPER, encoding="utf-8").read()
    dl = doc.split("\n")
    long_ = [i + 1 for i, l_ in enumerate(dl) if len(l_) > 121]
    olds = {t_: block(dl, "Old (%s):" % t_) for t_ in TAGS}
    news = {t_: block(dl, "New (%s):" % t_) for t_ in TAGS}
    newlong = [l_ for t_ in TAGS for l_ in news[t_].split("\n") if len(l_) > 121]
    P = norm(paper)
    # the state the paper is in, and the two texts every run checks: the paper before seating and seated
    if all(P.count(norm(olds[t_])) == 1 for t_ in TAGS) and not any(P.count(norm(news[t_])) for t_ in TAGS):
        state, t_pre, t_seat = "before seating", paper, paper
        for t_ in TAGS:
            t_seat = swap(t_seat, olds[t_], news[t_]) if t_seat is not None else None
        if t_seat is not None:                                         # the zero md5, as --update-md5 would fill it
            t_seat = t_seat.replace("`" + "0" * 32 + "`", "`" + "0123456789abcdef" * 2 + "`")
    elif seated_ok(paper, news, olds):
        state, t_pre, t_seat = "seated", paper, paper
        for t_ in TAGS:                                                # rebuild the text before seating
            t_pre = swap(t_pre, news[t_], olds[t_]) if t_pre is not None else None
    else:
        state, t_pre, t_seat = "neither", None, None
    # the mutants act on both texts, whichever state was found
    if MUT in ("char_a", "char_b"):
        t_ = MUT[-1]
        olds[t_] = olds[t_].replace("ρ", "p", 1)
        news[t_] = news[t_].replace("ρ", "p", 1)
    if MUT == "drop_m3":
        news["b"] = news["b"].replace("support8b.py` M3", "support8b.py`")
    if MUT == "drop_c" and t_seat is not None:
        t_seat = swap(t_seat, news["c"], olds["c"])
    if MUT == "seated_keep_old_a" and t_seat is not None:
        t_seat = t_seat + "\n" + olds["a"] + "\n"
    p_ok, need = pre_ok(t_pre, olds, news) if t_pre is not None else (False, {})
    s_ok = seated_ok(t_seat, news, olds) if t_seat is not None else False
    lines_at = (", ".join("%s %d" % (t_, paper[:norm(paper).find(norm(olds[t_]))].count("\n") + 1) for t_ in TAGS)
                if state == "before seating" else
                ", ".join("%s %d" % (t_, paper[:norm(paper).find(norm(news[t_]))].count("\n") + 1) for t_ in TAGS)
                if state == "seated" else "none")
    say("E6: GLUEDECAY5.md lines over 121 characters: %s; new block lines over 121: %d; section %s's blocks; state of "
        "the paper found: %s, the blocks at lines %s. Before seating (%s): each old block once, no new block, disjoint, "
        "(a) immediately followed by (b), and with all blocks applied: %s. Seated (%s): each new block once, disjoint, "
        "(a) then (b), old (a)-(e), (g) gone, the same places in place: %s"
        % (long_ or "none", len(newlong), SECTION, state, lines_at,
           "the paper" if state == "before seating" else "rebuilt from the seated paper", "; ".join(
               "%s %s" % kv for kv in need.items()) if need else p_ok,
           "the paper" if state == "seated" else "a copy with all blocks applied, its zero md5 filled", s_ok))
    return not long_ and not newlong and state != "neither" and p_ok and s_ok


CHECKS = [("E1", e1, ["lebesgue"]), ("E2", e2, ["no_osc", "ss_sign", "lam_max"]),
          ("E3", e3, ["coef3", "second_r3", "mu0"]),
          ("E4", e4, ["no_decouple", "box_strong", "energy_trsign", "mom_drop_x", "p3_strong", "box_weak",
                      "drop_lapse"]),
          ("E5", e5, ["mass", "dim3"]),
          ("E6", e6, ["char_a", "char_b", "drop_c", "drop_m3", "seated_keep_old_a"])]


def main():
    global MUT, PAPER
    if "--paper" in sys.argv:                                          # check another copy of the paper
        PAPER = os.path.abspath(sys.argv[sys.argv.index("--paper") + 1])
    ok = True
    for name, f, mutants in CHECKS:
        MUT = None
        good = f()
        survived = []
        for m_ in mutants:
            MUT = m_
            if f():
                survived.append(m_)
        MUT = None
        print(textwrap.fill("%s %s (mutants failing as they must: %s%s)" % (
            name, "PASS" if good and not survived else "FAIL",
            ", ".join(m_ for m_ in mutants if m_ not in survived) or "none",
            "; survived: " + ", ".join(survived) if survived else ""), 118, subsequent_indent="      "), flush=True)
        ok &= good and not survived
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
