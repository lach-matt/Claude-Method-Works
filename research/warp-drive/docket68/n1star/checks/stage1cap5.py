#!/usr/bin/env python3
"""stage1cap5: what stage 1 can do to the lambda0 bound, and Lemma 6.4's principal constants at the background on
Sigma (CONSTANTS5.md, Round 6, item 2). Labels: computed (exact, sympy), certified (Arb balls, python-flint; exact
rationals), READ (cited lines and .out values), deduced (where said).

lambda0 < eps1/C_app (Step 3, N1STAR-PROOF.md:355-357 at D614 numbering) with C_app >= sup |g_1| over Omega x S^1,
g_1 = m_1 + W(X, th + phi_1(X)), W = W_TT + chi dv dv (:461-462, :548); round 4 used C_app >= sup |W_TT|_op >= 12.593309
(lzerotrace5.py T3). The stage-1 mean m_1 is what stage 1 adds.

  S1 (exact; deduced) the harmonic structure: from the closed forms (stage0bd5.py, READ), W_TT is a first harmonic in
     the phase s (cos s, sin s) and chi a second (sin 2s, cos 2s), so W_TT(s + pi) = -W_TT(s), chi(s + pi/2) = -chi(s),
     and for g(s) := M + W_TT(s) + chi(s) D (M, D independent of s)
        g(s) - g(s + pi) = 2 W_TT(s),   (g(s) + g(s + pi))/2 = M + chi(s) D,
        (g(s) + g(s + pi)) - (g(s + pi/2) + g(s + 3 pi/2)) = 4 chi(s) D            (sympy, symbolic M, D).
     Hence (deduced, triangle inequality in any norm) sup_s |g| >= max(sup_s |W_TT|, sup_s |M + chi D|, sup_s |chi D|),
     and every admissible C_app satisfies C_app >= max(sup |W_TT|, sup |m_1 + chi dv dv|) >= max(sup |W_TT|,
     2 sup |chi|), |dv dv|_op = |dv|^2 = 2 (Euclidean, dv = dtau + xhat.dx).
  S2 (exact; certified) stage 0's second harmonic does not move the bound: the angular factor of chi,
     (1/12) H^2 (16 cos^2 2th + sin^4 2th)^(1/2) with H^2 = 2/(1 + cos^2 2th), is at most 1/3 (exact: 4 (1 + q^2)^2 -
     16 q^2 - (1 - q^2)^2 = 3 (1 - q^2)^2 >= 0, q = cos 2th), with equality at q^2 = 1; the radial factor r^-2 -
     (v - tau0)^(-1/2) r^(-3/2) is positive and decreasing in r on r <= v - tau0 (its derivative vanishes only at
     r = 16 (v - tau0)/9), so on Omega sup is at r = a (the points (v - a, a), v in [1/2, 7/2], lie in Omega); and
     2 sup |chi| = (2/3) sup_v E(v)^2 (a^-2 - (v + 2)^(-1/2) a^(-3/2)) < 11.92 (Arb over 4000 cells of v, envelope
     c <= 1.32410349, READ envelope5.out E1), below 12.593309. So the m_1-free bound stays sup |W_TT|.
  S3 (deduced) the criterion: stage 1 lowers the certified lambda0 bound if and only if a certified lower bound for
     sup_{Omega x S^1} |m_1 + chi dv dv|_op exceeds 12.593309 (then lambda0 < eps1/that); an upper bound for m_1 (what
     Lemma 6.4's estimate would give) does not move it. With 2 sup|chi| near 11.9, an |m_1| of order 1 at the right
     point would.
  S4 (certified) Lemma 6.4's principal constants for stage 1's constraint solve at g0's data on Sigma = Sigma_tau0
     (Lemma 6.3 (a), closed forms READ there: alpha = theta^3 H = 3 r^3/(r^2 + mu)^2, angular principal coefficient
     (r^2 + mu)^-1, S A0 = diag(6, 1/(r^2 + mu)), c^2 = 2 (r^2 + mu)/(3 r^4)), r in [a, b(tau0)], mu in [mu0, mu_end]:
     alpha0, delta0, A00 and the largest speed, certified.
  Controls (each mutates the computed path; each must fail): C1 S1's identity with chi taken as a first harmonic: the
  four-point combination no longer isolates chi; C2 S2's angular bound claimed 1/4: refuted at q = 1; C3 S2 run at
  r = a/2 (outside Omega): the bound exceeds 12.593309, so S2's restriction to Omega is what makes it hold.

    python3 checks/stage1cap5.py       (seconds)
"""
import builtins
import sys
import textwrap
from fractions import Fraction as Fr

import flint
import sympy as sp

OK = {}
C_HI = flint.arb('1.32410349')                   # READ envelope5.out E1 (upper end of c)
CAPP = Fr(12593309, 10 ** 6)                     # READ lzerotrace5.out T3
MU0, MUEND = Fr(1), Fr(227, 192)                 # READ CONSTANTS5.md 1.4
TAU0 = -2
B_TAU0_HI = flint.arb('13.437208255')            # READ lzerotrace5.out / CONSTANTS5.md 1.4: b(tau0) = 13.437208254


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def s1(chi_harm=2):
    s = sp.Symbol('s', real=True)
    M, D, A1, B1, A2, B2 = sp.symbols('M D A1 B1 A2 B2')
    W = A1 * sp.cos(s) + B1 * sp.sin(s)
    chi = A2 * sp.cos(chi_harm * s) + B2 * sp.sin(chi_harm * s)
    g = lambda x: M + W.subs(s, x) + chi.subs(s, x) * D  # noqa: E731
    e1 = sp.simplify(g(s) - g(s + sp.pi) - 2 * W)
    e2 = sp.simplify((g(s) + g(s + sp.pi)) / 2 - (M + chi * D))
    e3 = sp.simplify((g(s) + g(s + sp.pi)) - (g(s + sp.pi / 2) + g(s + 3 * sp.pi / 2)) - 4 * chi * D)
    return e1 == 0 and e2 == 0 and e3 == 0


def stage0_forms():
    """READ stage0bd5.py's closed forms: W_TT's phase dependence and chi's"""
    s, th, r, v, E = sp.symbols('s theta r v E', real=True)
    H = sp.sqrt(2 / (1 + sp.cos(2 * th) ** 2))
    c, sn = sp.cos(th), sp.sin(th)
    K = E * H * r ** sp.Rational(-3, 2)
    P1 = K * (2 * c ** 2 * sp.cos(s) - sn ** 2 * sp.sin(s)) / 3
    P2 = K * (2 * sn ** 2 * sp.sin(s) - c ** 2 * sp.cos(s)) / 3
    chi = -sp.Rational(1, 12) * E ** 2 * H ** 2 * (4 * sp.cos(2 * th) * sp.sin(2 * s) + sp.sin(2 * th) ** 2
                                                   * sp.cos(2 * s)) * (r ** -2 - (v - TAU0) ** sp.Rational(-1, 2)
                                                                       * r ** sp.Rational(-3, 2))
    oddW = all(sp.simplify(P.subs(s, s + sp.pi) + P) == 0 for P in (P1, P2))
    oddchi = sp.simplify(chi.subs(s, s + sp.pi / 2) + chi) == 0
    return oddW, oddchi


def angular_bound(claim=Fr(1, 3)):
    q = sp.Symbol('q', real=True)
    g2 = (16 * q ** 2 + (1 - q ** 2) ** 2) / (36 * (1 + q ** 2) ** 2)      # [(1/12) H^2 (...)^(1/2)]^2
    diff = sp.factor(sp.expand(claim ** 2 * 36 * (1 + q ** 2) ** 2 - (16 * q ** 2 + (1 - q ** 2) ** 2)))
    at1 = g2.subs(q, 1)
    return diff, at1


def a_ball():
    q0 = flint.arb(9) / 1250
    q0 = q0 ** (flint.arb(1) / 8)
    return q0 / 2


def env_sq_hi(vlo, vhi):
    """upper bound of E(v)^2 on [vlo, vhi] (Arb), E = c cos^12(pi y/2) exp(-y^2/(1 - y^2)), y = (2 v - 4)/3"""
    ylo, yhi = (2 * vlo - 4) / 3, (2 * vhi - 4) / 3
    y = flint.arb((ylo + yhi) / 2, (yhi - ylo) / 2)
    ymax = max(abs(ylo), abs(yhi))
    if ymax >= Fr(999, 1000):                    # end cells: cos^12 <= cos^12(pi ymin/2), exp <= 1
        ymin = min(abs(ylo), abs(yhi)) if ylo * yhi > 0 else Fr(0)
        cmax = flint.arb(ymin) * flint.arb.pi() / 2
        e = C_HI * cmax.cos() ** 12
        return (e * e).upper()
    cpart = (flint.arb.pi() * y / 2).cos() ** 12
    ex = (-(y * y) / (1 - y * y)).exp()
    e = C_HI * cpart * ex
    return (e * e).upper()


def chi_sup(r_at, cells=4000):
    best = flint.arb(0)
    for i in range(cells):
        vlo, vhi = Fr(1, 2) + Fr(3 * i, cells), Fr(1, 2) + Fr(3 * (i + 1), cells)
        E2 = flint.arb(env_sq_hi(vlo, vhi))
        vb = flint.arb((vlo + vhi) / 2, (vhi - vlo) / 2)
        rad = r_at ** -2 - (vb + 2) ** flint.arb(-0.5) * r_at ** flint.arb(-1.5)
        val = flint.arb((flint.arb(2) / 3 * E2 * rad).upper())
        if val > best:
            best = val
    return best


def main():
    print('stage1cap5: stage 1 against the lambda0 bound; Lemma 6.4\'s principal constants at the background')
    OK['S1'] = s1()
    oddW, oddchi = stage0_forms()
    OK['S1'] = OK['S1'] and oddW and oddchi
    print('  S1: W_TT(s + pi) = -W_TT(s) and chi(s + pi/2) = -chi(s) on the closed forms (exact): %s, %s; the three '
          'identities for g = M + W_TT + chi D (exact): so C_app >= max(sup|W_TT|, sup|m_1 + chi dv dv|) >= max(sup|W_TT|,'
          ' 2 sup|chi|): %s' % (oddW, oddchi, OK['S1']))
    diff, at1 = angular_bound()
    OK['S2a'] = sp.simplify(diff - 3 * (1 - sp.Symbol('q', real=True) ** 2) ** 2) == 0 and at1 == Fr(1, 9)
    a = a_ball()
    sup2chi = chi_sup(a)
    OK['S2'] = OK['S2a'] and sup2chi < flint.arb('11.92') and sup2chi < flint.arb(CAPP.numerator) / CAPP.denominator
    print('  S2: angular factor squared <= 1/9 with 36 (1 + q^2)^2/9 - (16 q^2 + (1 - q^2)^2) = %s (exact), equality at '
          'q^2 = 1; a = q0/2 in %s; 2 sup_Omega |chi| <= %s (certified, Arb) < 12.593309: the second harmonic does not '
          'raise C_app\'s lower bound: %s' % (diff, a.str(10), sup2chi.str(6), OK['S2']))
    print('  S3 (deduced): stage 1 lowers the certified lambda0 bound iff a certified lower bound of sup |m_1 + chi dv dv|'
          '_op exceeds 12.593309; Lemma 6.4\'s estimate, an upper bound for m_1, cannot do it')
    # S4 principal constants on Sigma_tau0
    b = B_TAU0_HI
    mue = flint.arb(MUEND.numerator) / MUEND.denominator
    al_a = 3 * a ** 3 / (a * a + 1) ** 2                 # at r = a, v = tau0 + a < 1/2: mu = mu0 = 1
    al_b = 3 * b ** 3 / (b * b + mue) ** 2               # at r = b(tau0), v > 7/2: mu = mu_end
    # interior: alpha(r) >= 3 r^3/(r^2 + mu_end)^2, increasing on r < (3 mu_end)^(1/2) and decreasing beyond, so the
    # minimum over [a, b] of the lower bound is at an endpoint
    al_a_low = 3 * a ** 3 / (a * a + mue) ** 2
    alpha0 = min(al_a_low.lower(), al_b.lower())
    delta0 = (1 / (b * b + mue)).lower()
    A00 = delta0
    cmax = (2 * (a * a + mue) / (3 * a ** 4)).upper()
    OK['S4'] = alpha0 > 0 and delta0 > 0
    print('  S4 (certified): on Sigma_tau0, r in [a, b(tau0)], alpha = 3 r^3/(r^2 + mu)^2 >= alpha0 = %s (at r = a with '
          'mu_end; %s with mu0 = 1 there), angular ellipticity and A00 = min eig S A0 >= %s (at r = b(tau0)), the '
          'largest speed^2 2 (r^2 + mu)/(3 r^4) <= %s (at r = a): %s' % (
              flint.arb(alpha0).str(6), al_a.str(6), flint.arb(delta0).str(6), flint.arb(cmax).str(6), OK['S4']))
    # controls
    OK['C1'] = not s1(chi_harm=1)
    print('  C1 (control): chi taken as a first harmonic: S1\'s identities fail: %s' % OK['C1'])
    d14, _ = angular_bound(Fr(1, 4))
    q = sp.Symbol('q', real=True)
    OK['C2'] = sp.simplify(d14.subs(q, 1)) < 0
    print('  C2 (control): angular factor claimed <= 1/4: the difference at q = 1 is %s < 0: refuted: %s' % (
        sp.simplify(d14.subs(q, 1)), OK['C2']))
    sup_half = chi_sup(a / 2, cells=400)
    OK['C3'] = sup_half > flint.arb(CAPP.numerator) / CAPP.denominator
    print('  C3 (control): S2 at r = a/2 (outside Omega): 2 sup |chi| >= %s > 12.593309: %s' % (
        flint.arb(sup_half.lower()).str(6), OK['C3']))
    for k, v in OK.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
