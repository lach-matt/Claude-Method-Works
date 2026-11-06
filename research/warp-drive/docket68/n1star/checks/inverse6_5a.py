#!/usr/bin/env python3
"""inverse6_5a: the assembly of lambda1 and delta from their inputs, with every input's status (INVERSE5-SIX.md round 2;
CONSTANTS5.md R10.5's open items). Labels: READ (quotes found by content in pinned files), computed (exact or 60-digit),
deduced (where said).

The chain is EFFECTIVE-CONSTANTS.md Propositions 2.1-2.2 (READ, quoted below): with alpha = 8d + 2 and N = 21d + 6,
  theta0 = max{16, 16 eta_G^-2, (4 K3/delta_G)^(1/(6d+2)), 1 + K4, C1 K5 + C2 K3^2/2},  eps_NM = theta0^-alpha,
  eps <= min{1, eps_NM/A_2d, eps_NM^G/A_2d, eps_dat},  delta = eps/2,
  lambda1 = min(lambda_1.1, eta_gl/C_R, eps/(4 C_R)),
K1 = C_d (1 + delta_G) <= 2 C_d (delta_G <= 1; used so), K2 = C_(N-2d)(C_(N-d) + 1), K3 = C_(3d,d) K1,
K4 = 2 C_(N,N-2d) K2, K5 = 2 C_(3d,N-2d) K2,
delta_G = min(delta_K, eps_m), eta_G = 1. So explicit lower bounds for delta and lambda1 need explicit upper bounds for
the constants (C_k, k <= N, the smoothing constants, C1, C2, A_2d, C_R, the G-equivalence constants in eps_NM^G) and
explicit lower bounds for the thresholds (delta_K, eps_m, eps_dat, lambda_1.1, eta_gl).

  A0 (READ) the quotes: EFFECTIVE-CONSTANTS.md's theta0, eps, delta and lambda1 lines and its list "What is not
     explicit"; PART-VI4-PARAMS.md's h_* = min(10^-6, h_0, h_tf), gamma_Ups,H in (0, eps_0], and "outside the proved
     set" for the record's computational point gamma_C = 10^6; PART-III-D2-ZEROENERGY.md Proposition 4.1's "There is
     eps_0 > 0"; CONSTANTS5.md R10.1's d <= 46,236,449,175,331,158. Each file's md5 is printed.
  A1 (proved by inspection; checked at 60 digits) the formula is monotone: with K1 <= 2 C_d every K_i is
     nondecreasing in the constants, theta0 is a max of nondecreasing functions of the constants and of eta_G^-2 and
     (4 K3/delta_G)^(1/(6d+2)), eps_NM = theta0^-alpha, and delta, lambda1 are mins of nonincreasing functions of the
     constants and nondecreasing functions of the thresholds (Round 3: the label was "computed"; the verifier's n6).
     Checked on 3000 random input points and at engineered points where each branch binds: raising any upper-bound
     constant never raises delta or lambda1, raising any threshold never lowers them. So certified one-sided bounds of
     the inputs give certified lower bounds of delta and lambda1 (deduced).
  A2 (computed) at d = d_bar = 46,236,449,175,331,158 (R10.1, deduced on its reading; a larger loss is admissible) and
     every other input at its floor (constants 1, thresholds 1, eta_G = 1): theta0 = 16 exactly and log10 delta =
     -(8 d_bar + 2) log10 16 - log10 2, pinned; and the general lower bound
     log10 delta >= -(8 d_bar + 2) log10 theta0_bar - log10 (2 A_bar) when eps_NM/A_2d is the least term (deduced
     from A1), at sample values.
  A3 (READ; deduced) the inventory: each input of the chain with its status (certified / explicit / explicit on a
     reading / not computed) and the inverse bounds of INVERSE5-SIX.md that feed it.
  A4 (exact) R6's hypothesis for box on functions at b0: for Phi solving -Phi'' + (V - sigma^2 - i s q) Phi = 0,
     s = sgn sigma, q >= 0, the identity Im int (equation) conj(Phi) = -Im[Phi' conj(Phi)] - s int q |Phi|^2 (an exact
     derivative, sympy), and at the class's ends Im[Phi' conj Phi] = sigma |c_+|^2 (outgoing) and -sigma |c_-|^2 (regular
     at the future horizon): so 0 = -sigma (|c_+|^2 + |c_-|^2) - s int q |Phi|^2, both terms of the sign of -sigma, and
     c_+ = 0 forces Phi = 0 (the outgoing Jost solution); with Fredholm index 0 (a compactly supported multiplication is
     compact X_sigma -> Y_sigma) the absorbed problem is invertible at every real sigma != 0 (deduced).
  Controls (each must fail): C1 lambda1 with eta_gl C_R in place of eta_gl/C_R: A1's monotonicity test fails; C2 alpha
  = 8d: A2's exact value check fails; C3 the absorption with the wrong sign (s = -sgn sigma): the two terms can cancel
  (an
  exact instance with c_+ != 0 is exhibited), so A4's argument fails; C4 a quote mutated ("inside the proved set"):
  A0 does not find it.

    python3 checks/inverse6_5a.py [--selftest]          (seconds)
"""
import builtins
import hashlib
import os
import random
import re
import sys
import textwrap

import sympy as sp
from mpmath import mp, mpf, log10

mp.dps = 60
HERE = os.path.dirname(os.path.abspath(__file__))
TOP = os.path.dirname(HERE)
OK = {}
D_BAR = 46236449175331158
A2_PIN = ('-4.4540', '-4.4539')          # log10 delta at d_bar, every other input at its floor, in units of 1e17


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


QUOTES = [
    ('EFFECTIVE-CONSTANTS.md', 'θ0 := max{ 16, 16 η_G⁻², (4K3/δ_G)^{1/(6d+2)}, 1 + K4, C1 K5 + ½ C2 K3² }'),
    ('EFFECTIVE-CONSTANTS.md', 'ε ≤ min{ 1, ε_NM / A_2d, ε_NM^G / A_2d, ε_dat }'),
    ('EFFECTIVE-CONSTANTS.md', 'Part VII section 4 puts δ := ε/2'),
    ('EFFECTIVE-CONSTANTS.md', 'λ1 := min(λ_1.1, η_gl/C_R, ε/(4C_R))'),
    ('EFFECTIVE-CONSTANTS.md', '**What is not explicit.**'),
    ('proof5/PART-VI4-PARAMS.md', r'$h_* = \min(10^{-6},h_0,h_{\mathrm{tf}})$'),
    ('proof5/PART-VI4-PARAMS.md', r'$\gamma_{\Upsilon,H}\in(0,\epsilon_0]$'),
    ('proof5/PART-VI4-PARAMS.md', r'$\gamma_C = 10^6$, outside the proved set'),
    ('proof5/PART-III-D2-ZEROENERGY.md', r'There is $\epsilon_0>0$ such that'),
    ('CONSTANTS5.md', 'd <= 46,236,449,175,331,158'),
]


def norm_ws(s):
    return re.sub(r'\s+', ' ', s)


def a0(quotes=QUOTES):
    good, md5s = True, {}
    for fn, q in quotes:
        path = os.path.join(TOP, fn)
        txt = open(path, encoding='utf-8').read()
        md5s[fn] = hashlib.md5(open(path, 'rb').read()).hexdigest()
        good &= norm_ws(q) in norm_ws(txt)
    return good, md5s


# ------------------------------------------------------------------------------------------------- the formula
def log_delta_lambda(d, C, C1, C2, A, AG, delta_G, eps_dat, eta_G, lam11, eta_gl, CR, mutant=False):
    """log10 delta and log10 lambda1 from Propositions 2.1-2.2; C bounds every C_k and smoothing constant (>= 1)"""
    d, C, C1, C2, A, AG = mpf(d), mpf(C), mpf(C1), mpf(C2), mpf(A), mpf(AG)
    K1 = 2 * C                     # C_d (1 + delta_G) <= 2 C_d, as delta_G <= 1: so delta_G enters monotonically
    K2 = C * (C + 1)
    K3 = C * K1
    K4 = 2 * C * K2
    K5 = 2 * C * K2
    theta0 = max(mpf(16), 16 / mpf(eta_G) ** 2, (4 * K3 / delta_G) ** (1 / (6 * d + 2)), 1 + K4,
                 C1 * K5 + C2 * K3 ** 2 / 2)
    alpha = 8 * d + 2
    lNM = -alpha * log10(theta0)
    leps = min(mpf(0), lNM - log10(A), lNM - log10(AG), log10(eps_dat))
    ldel = leps - log10(2)
    if mutant:
        llam = min(log10(lam11), log10(eta_gl) + log10(CR), leps - log10(4 * CR))
    else:
        llam = min(log10(lam11), log10(eta_gl) - log10(CR), leps - log10(4 * CR))
    return ldel, llam, theta0


def a1(mutant=False, n=3000, seed=7):
    rnd = random.Random(seed)
    ups = ['C', 'C1', 'C2', 'A', 'AG', 'CR']               # upper-bound constants
    ths = ['delta_G', 'eps_dat', 'eta_G', 'lam11', 'eta_gl']   # thresholds
    good = True
    fixed = [dict(d=1, C=1.0, C1=1.0, C2=1.0, A=1.0, AG=1.0, delta_G=1.0, eps_dat=1.0, eta_G=1.0, lam11=1.0,
                  eta_gl=1e-20, CR=2.0),                       # the gluing term binds lambda1
             dict(d=1, C=1.0, C1=1.0, C2=1.0, A=1.0, AG=1.0, delta_G=1.0, eps_dat=1e-30, eta_G=1.0, lam11=1e-40,
                  eta_gl=1.0, CR=1.0)]                         # eps_dat binds delta, lambda_1.1 binds lambda1
    cases = [(dict(fp), k) for fp in fixed for k in ups + ths]          # every input at the engineered points
    for _ in range(n):
        cases.append((dict(d=rnd.choice([1, 3, 7, 50]), C=10 ** rnd.uniform(0, 3), C1=10 ** rnd.uniform(0, 3),
                           C2=10 ** rnd.uniform(0, 3), A=10 ** rnd.uniform(0, 3), AG=10 ** rnd.uniform(0, 3),
                           delta_G=10 ** rnd.uniform(-3, 0), eps_dat=10 ** rnd.uniform(-30, 0),
                           eta_G=10 ** rnd.uniform(-1, 0), lam11=10 ** rnd.uniform(-30, 0),
                           eta_gl=10 ** rnd.uniform(-5, 0), CR=10 ** rnd.uniform(0, 3)), rnd.choice(ups + ths)))
    for p, k in cases:
        base = log_delta_lambda(mutant=mutant, **p)
        q = dict(p)
        q[k] = p[k] * (1 + rnd.uniform(0.01, 3)) if k in ups else min(1.0, p[k] * (1 + rnd.uniform(0.01, 3)))
        new = log_delta_lambda(mutant=mutant, **q)
        if k in ups:
            good &= new[0] <= base[0] + mpf(10) ** -40 and new[1] <= base[1] + mpf(10) ** -40
        else:
            good &= new[0] >= base[0] - mpf(10) ** -40 and new[1] >= base[1] - mpf(10) ** -40
    return good


def a2(alpha_shift=0):
    one = 1
    ldel, llam, th = log_delta_lambda(D_BAR, one, one, one, one, one, mpf(1), mpf(1), mpf(1), mpf(1), mpf(1), one)
    if alpha_shift:
        ldel = ldel + 2 * log10(th)             # alpha = 8d instead of 8d + 2
    val = ldel / mpf(10) ** 17
    pinned = mpf(A2_PIN[0]) <= val <= mpf(A2_PIN[1])
    exact = abs(ldel - (-(8 * mpf(D_BAR) + 2) * log10(16) - log10(2))) < mpf(10) ** -30
    # the general lower bound at sample values theta0_bar, A_bar (deduced from A1): the eps_NM/A_2d branch
    samples = []
    for th_bar, A_bar in ((mpf(10) ** 6, mpf(10) ** 12), (mpf(10) ** 30, mpf(10) ** 100)):
        samples.append((th_bar, A_bar, (-(8 * mpf(D_BAR) + 2) * log10(th_bar) - log10(2 * A_bar)) / mpf(10) ** 17))
    return pinned and exact and th == 16, val, samples


INVENTORY = [
    ('d (the loss), N = 21 d + 6', 'explicit on a reading', 'd <= 46,236,449,175,331,158 (CONSTANTS5 R10.1; deduced on '
     'its reading, two avoidance conditions undecided)', '-'),
    ('C_k (k <= N), C_(s,t), C1, C2', 'not computed', 'III.K map and right inverses; smoothing constants explicit in '
     'principle (EFFECTIVE-CONSTANTS section 2)', 'B1-B6 and I.C:497 through III.J\'s inverses and the linear theory'),
    ('A_2d', 'not computed', 'III.K Lemma 2.2 (d)', 'the same'),
    ('delta_K, eps_dat (the admissible pair)', 'not computed', 'thresholds of III.K sections 1-4, two further '
     'Nash-Moser thresholds eps_ext, eps_slab (Parts IV-IV\'\'\'), the data map\'s modulus', 'the linear theory'),
    ('eps_NM^G (G-sup norms)', 'explicit in principle', 'equivalence constants of the G-sup norms', '-'),
    ('eps_m, eps_t, eps_K', 'given / chosen', 'VI.C rows w1-w2', '-'),
    ('C_J, lambda_1.1, eta_gl, C_R', 'not computed', 'Part VII (gluing by an implicit function theorem, [CD03])', '-'),
    ('gauge and damping parameters', 'not explicit in the record', 'gamma_Ups,H <= eps_0, e_Ups < eps_1, eps_L, '
     'gamma_Ups < gamma_1, gamma_C = 1/h, h < min(1e-6, h_0, h_tf), off countable sets (VI.C rows u2-u5, c2)',
     'every operator of B1-B6 is fixed only once these are'),
    ('I.C:497, scalar-type blocks', 'not computed (in progress, scalarblock5.py)', 'sigma_min uniform in l', '-'),
    ('B1 (C, h_0) in I.B (6.6)', 'not computed', 'symbol data at b0 certified/exact (inverse6_5 K1-K3)', '-'),
    ('B2 C_a, B3 C_8.1', 'not computed', 'absorption and interpolation explicit (R3, R4; F <= 1.002659)', 'B1'),
    ('B4, B5 cut-off parts C_D', 'certified on the master operators and the tensor-, vector-type blocks; not computed '
     'for the reconstruction', 'inverse6_5m M1-M7', 'gauge operators box^C, box^Ups'),
    ('B4, B5 C_ext(sigma)', 'not computed; invertibility of the absorbed problem proved for box on functions (A4)',
     'R6', 'the write-out\'s norms'),
    ('B6', 'eliminated at the site (R1); parametrix norms and N^0(sigma) injectivity not computed', 'R1', '-'),
]


def a4():
    x, sig, s = sp.symbols('x sigma s', real=True)
    u, v, V, q = [sp.Function(n_, real=True)(x) for n_ in ('u', 'v', 'V', 'q')]
    # Phi = u + i v with u, v real: eq = a + i b, and Im(eq conj Phi) = b u - a v, Im(Phi' conj Phi) = v' u - u' v
    a_ = -sp.diff(u, x, 2) + (V - sig**2) * u + s * q * v
    b_ = -sp.diff(v, x, 2) + (V - sig**2) * v - s * q * u
    lhs = b_ * u - a_ * v
    rhs = -sp.diff(sp.diff(v, x) * u - sp.diff(u, x) * v, x) - s * q * (u**2 + v**2)
    ident = sp.expand(lhs - rhs) == 0
    c = sp.Symbol('c')
    out = sp.exp(sp.I * sig * x) * c
    ends = sp.simplify(sp.im(sp.expand(sp.diff(out, x) * sp.conjugate(out))))
    hor = sp.exp(-sp.I * sig * x) * c
    endh = sp.simplify(sp.im(sp.expand(sp.diff(hor, x) * sp.conjugate(hor))))
    cc = sp.Symbol('cc', positive=True)
    ok_ends = sp.simplify(ends.subs(c, cc) - sig * cc**2) == 0 and sp.simplify(endh.subs(c, cc) + sig * cc**2) == 0
    return ident and ok_ends


def c3():
    """with s = -sgn sigma the balance -sigma (|c+|^2 + |c-|^2) - s int q |Phi|^2 = 0 admits c+ != 0 (an exact
    instance)"""
    sigma, cp2, cm2, Q = sp.Rational(1), sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(1)
    s = -1                                          # wrong sign for sigma > 0
    return -sigma * (cp2 + cm2) - s * Q == 0 and cp2 != 0


def main():
    good0, md5s = a0()
    OK['A0'] = good0
    print('  A0 (READ): the ten quotes found by content: %s; md5: %s' % (good0, '; '.join(
        '%s %s' % (k, v) for k, v in md5s.items())))
    OK['A1'] = a1()
    print('  A1 (proved by inspection; checked at 60 digits): on 3000 random points and at engineered points raising an '
          'upper-bound constant never raises delta or lambda1 and raising a threshold never lowers them: %s' % OK['A1'])
    good2, val, samples = a2()
    OK['A2'] = good2
    print('  A2 (computed): at d_bar = %d with every other input at its floor theta0 = 16 and log10 delta = -(8 d_bar + '
          '2) log10 16 - log10 2 = %s x 10^17 (pinned in [%s, %s]): %s' % (D_BAR, mp.nstr(val, 8), A2_PIN[0], A2_PIN[1],
                                                                           good2))
    for th_bar, A_bar, v in samples:
        print('  A2 the lower bound when eps_NM/A_2d binds: theta0_bar = 10^%d, A_bar = 10^%d: log10 delta >= %s x 10^17'
              % (int(log10(th_bar)), int(log10(A_bar)), mp.nstr(v, 6)))
    OK['A3'] = len(INVENTORY) == 14
    print('  A3 (READ; deduced) the inventory (input | status | what it is | fed by):')
    for row in INVENTORY:
        print('      %s | %s | %s | %s' % row)
    OK['A4'] = a4()
    print('  A4 (exact): Im int (-Phi\'\' + (V - sigma^2 - i s q) Phi) conj Phi = -Im[Phi\' conj Phi] - s int q |Phi|^2 '
          'as an exact derivative, and the end values sigma |c_+|^2 (outgoing), -sigma |c_-|^2 (horizon): %s; so with '
          's = sgn sigma, q >= 0 the absorbed problem has trivial kernel on every mode, and is invertible (deduced)'
          % OK['A4'])
    OK['C1'] = not a1(mutant=True, n=600)
    print('  C1 (control): lambda1 with eta_gl C_R: monotonicity fails: %s' % OK['C1'])
    g2m, valm, _ = a2(alpha_shift=1)
    OK['C2'] = not g2m
    print('  C2 (control): alpha = 8d: log10 delta = %s x 10^17 (2 log10 16 above A2\'s), A2\'s exact check fails: %s'
          % (mp.nstr(valm, 8), OK['C2']))
    OK['C3'] = c3()
    print('  C3 (control): absorption sign -sgn sigma: -sigma (1/3 + 2/3) + 1 = 0 with |c_+|^2 = 1/3: the balance no '
          'longer forces c_+ = 0: %s' % OK['C3'])
    bad = QUOTES[:7] + [('proof5/PART-VI4-PARAMS.md', r'$\gamma_C = 10^6$, inside the proved set')]
    OK['C4'] = not a0(bad)[0]
    print('  C4 (control): the quote mutated to "inside the proved set": not found: %s' % OK['C4'])
    for k_, v_ in OK.items():
        builtins.print(k_, 'PASS' if v_ else 'FAIL')
    if '--selftest' in sys.argv:
        sys.exit(0 if all(OK.values()) else 1)


if __name__ == '__main__':
    main()
