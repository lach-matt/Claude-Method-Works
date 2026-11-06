#!/usr/bin/env python3
"""d0count5: the coefficient orders the write-out fixes by the closed graph theorem, counted (CONSTANTS5.md, Round 7,
item 1 and Appendix R7.A). Labels: computed (exact integer and rational bookkeeping), deduced (the estimates of R7.A,
whose derivative counts this program carries step by step), READ (cited lines, located by content).

The write-out fixes three things by the closed graph theorem and nothing else (Q0): II.A Lemma 8.5 (a)-(b) (the
multiplication and pseudolocality order d_*, PART-II-A-SETUP.md:955-967), II.A2 Lemma 1.2 and Proposition 2.4 (the
finite-regularity calculus order M, PART-II-A2-STANDARD.md:130, 276-281). Every other d_0 of Part II is a largest-of
or a fixed increment over those (Q5's census). R7.A replaces the three by explicit estimates in the local model R^n,
n = 5 (the dimension of M-tilde), with index-nu log factors absorbed into a loss delta (<log rho|^(nu j) <=
C_delta <zeta>^(delta j)):

  Q1 (deduced; computed exponents) R7.A Theorem A.1: ||Op(p)||_{L^2} <= C (A_x A_xi)^(1/2) with N = 2n + 1 pure x- and
     pure xi-derivatives (S^0_{delta,delta} weights), for 0 <= delta < 2/(2 + 5n): the Cotlar-Stein sums over the
     dyadic-shell lattice converge (adjacent shells: N/2 > n; distant shells: the exponent below is negative).
  Q2 (deduced; computed) Lemma A.5 (= II.A Lemma 8.5 (a)): D_a(t) = J + 2 M0, M0 = ceil(max(0, -t0)/2), t0 =
     floor(inf t) - 1, J the least integer with J (1 - delta) > sup t + 2 M0 + n + delta. Lemma A.6 (= 8.5 (b)):
     D_b(t, t') = Jb + sigma + 2 M1, sigma = max(0, ceil(sup t)), M1 from t', Jb (1 - delta) > sigma + 2 M1 + n + delta.
     Lemma 8.6: d_0 = max(D_a(s - m), D_b(s - m, -N - m)).
  Q3 (deduced; computed) Proposition A.7 (= II.A2 Proposition 2.4 (a)): Op(a): H^t -> H^(t - m) for a in
     C^(M) S-tilde^m once M >= M_a(t, m) = max(P1, ..., P5), the pieces of the conjugation Lambda_(t-m) Op(a) Lambda'_t
     (left expansion J1, right expansion J2, Theorem A.1 on the main terms, kernel bounds on the remainders with
     Peetre's inequality); (b)-(f): M_b = M_a + 1 + max(2L, 2L') + C_ch (one composition remainder, one change of
     chart); (d) one more; (e) the remainder at order -N_e. Each condition (remainder order below -n after its weight,
     Peetre exponent covered) is checked as an inequality, not assumed.
  Q4 (computed) the record's orders at III.I Theorem 5.3 (FWD), READ: II.C Proposition 5.1 with eta = m0 = 3 + delta +
     aleph = 5 (II.F2 Lemma 2.3, delta = 0, aleph = 2), theta_H < 2, theta_out >= 2 S-bar - 2 eps, S-bar = 0
     (II.C Lemma 2.6, III.C (4.3)), alpha_+ = beta_+ - 5/2 with beta_+ in (1/2, 3/2): s_in = 9 (an integer > 8.5),
     s_out = -8 (< -6 - beta_+ - eps for every admissible beta_+); s in [-8, 9], s0 = s - 2, s + 1, s_u = inf s - 2.
     The orders at which the closed-graph sites are invoked in D_0's chain lie in [-14, 11], N <= 14 (deduced from the
     cited statements: shifts by m <= 2, by 1 and 2, and error orders -N; the proofs' internal orders not all re-read).
  Q5 (computed; READ) the census: every line of Part II with a d_0 relation (89 lines) classified: a closed-graph site
     (replaced), a statement or largest-of (a max), an explicit increment d_0 - k (k <= 4), or an explicit constant
     (d_0 >= 2, 3, 5); the largest chain increment over M_a is +6 (II.D's symbols in C^(d_0 - 4), II.A2:722-723's
     d_0 - 2 >= M_2.4 + 2). So D_0 <= max(M_2.4 + 6, d_0(8.6) + 2, D_a + 2) over Q4's orders (deduced).
  Q6 (computed) d', d'' and the D_1 parts the record fixes in closed form at Q4's orders: d' = 8, d'' = 9; II.A
     Proposition 9.6 at s - 2: d_1 = 20, d-tilde = 33; II.E Proposition 4.4: d >= 35; every tame order in D_1 is
     d-tilde + 3 at orders in Q4's range, so D_1 <= 48 (deduced on that range). So FWD + BG = D_0 + D_1 + d' + d'' + 8
     <= 250, and c' = FWD + BG + the fixed MODs of a level, which this program does not bound.
  Controls (each mutates the computed path; each must fail): C1 Q2 with the Peetre/convergence term dropped (J one
  less): the remainder's integrability check fails; C2 Q1 at delta = 2/27: the distant-shell exponent is >= 0; C3 Q5
  with one table row removed: a line is unclassified; C4 Q3 with the right expansion's 2L dropped: the y-integrability
  check (2L > n) fails.

    python3 checks/d0count5.py       (seconds)
"""
import builtins
import math
import os
import re
import sys
import textwrap
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
P5 = os.path.join(HERE, '..', 'proof5')
OK = {}
n = 5
DELTA = Fr(1, 100)
NCV = 2 * n + 1


def print(*a, **k):  # noqa: A001
    for line in ' '.join(str(q) for q in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def ceil(x):
    return math.ceil(x) if not isinstance(x, Fr) else -((-x.numerator) // x.denominator)


def floor(x):
    return math.floor(x) if not isinstance(x, Fr) else x.numerator // x.denominator


def even_above(x):
    """the least even integer > x"""
    k = floor(x) + 1
    return k if k % 2 == 0 else k + 1


def least_J(rhs, rate):
    """the least integer J >= 0 with J * rate > rhs"""
    J = max(0, floor(rhs / rate))
    while J * rate <= rhs:
        J += 1
    return J


# ------------------------------------------------------------------------------------------------- Q1
def cv_exponent(delta, N=NCV):
    """the exponent of 2^k' in the distant-shell Cotlar-Stein sum (R7.A, A.1 step 5): delta n/4 + delta n +
    (1 - delta) n - (1 - delta) N/2; negative means the sum converges"""
    return delta * n / 4 + delta * n + (1 - delta) * n - (1 - delta) * Fr(N, 2)


# ------------------------------------------------------------------------------------------------- Q2
def D_a(t_lo, t_hi, delta=DELTA, drop=False):
    t0 = floor(t_lo) - 1
    M0 = ceil(Fr(max(0, -t0), 2))
    J = least_J(t_hi + 2 * M0 + n + delta, 1 - delta)
    if drop:
        J -= 1
    remainder_order = t_hi + delta - J * (1 - delta)          # of D_xi^beta lambda_t, |beta| = J
    conv = remainder_order + 2 * M0 < -n                      # the kernel integral converges
    D = J + 2 * M0
    return dict(D=max(D, abs(t0), J - 1), J=J, M0=M0, t0=t0, conv=conv)


def D_b(t_hi, tp_lo, delta=DELTA):
    sigma = max(0, ceil(t_hi))
    tp0 = floor(tp_lo) - 1
    M1 = ceil(Fr(max(0, -tp0), 2))
    Jb = least_J(sigma + 2 * M1 + n + delta, 1 - delta)
    conv = -Jb * (1 - delta) + delta + sigma + 2 * M1 < -n
    return dict(D=Jb + sigma + 2 * M1, Jb=Jb, sigma=sigma, M1=M1, conv=conv)


def d0_86(s_lo, s_hi, m, N):
    a = D_a(s_lo - m, s_hi - m)
    b = D_b(s_hi - m, -N - m)
    return max(a['D'], b['D']), a, b


# ------------------------------------------------------------------------------------------------- Q3
def M_a(t_lo, t_hi, m_lo, m_hi, delta=DELTA, drop2L=False):
    """Proposition A.7's pieces (R7.A): left expansion J1 (Lambda_(t-m) o Op(a)), right expansion J2 (o Lambda'_t),
    Theorem A.1 on the main terms, kernel bounds on the remainders; returns the count and the checks"""
    twoK = even_above(n)                                     # Schur decay: (1 + |x - y|)^-2K integrable, 2K > n
    M2 = ceil(Fr(max(0, t_hi), 2))                           # Lambda'_t: L^2 -> H^(-sup t)
    tm_hi = t_hi - m_lo
    # left: remainder order mu1 = (t - m)_hi + m_hi + delta - J1 (1 - 2 delta); need mu1 + 2 M2 < -n
    J1 = least_J(tm_hi + m_hi + delta + 2 * M2 + n, 1 - 2 * delta)
    mu_f1 = tm_hi - J1 * (1 - delta) + delta                 # the order of d_xi^alpha lambda, |alpha| = J1
    twoLp1 = even_above(n + abs(mu_f1))                      # Peetre: 2L' > n + |mu_f|
    conv1 = tm_hi + m_hi + delta - J1 * (1 - 2 * delta) + 2 * M2 < -n
    # right: remainder order mu2 = t_hi + delta - J2 (1 - 2 delta) - t_lo < -n
    J2 = least_J(t_hi - t_lo + n + delta, 1 - 2 * delta)
    twoL2 = 0 if drop2L else even_above(n)                   # eta-integration on the finite-regularity factor
    conv2 = t_hi + delta - J2 * (1 - 2 * delta) - t_lo < -n and twoL2 > n
    # the lower-order norm part (constant orders): tau0 = floor((t - m)_lo) - 1, right weight <xi>^(-t0)
    tau0 = floor(t_lo - m_hi) - 1
    t0 = floor(t_lo) - 1
    J3 = least_J(tau0 + m_hi + max(0, -t0) + n + delta, 1 - delta)
    mu_f3 = tau0 - J3
    twoLp3 = even_above(n + abs(mu_f3))
    P1 = (J1 - 1) + (J2 - 1) + NCV
    P2 = J1 + twoLp1 + twoK
    P3 = (J1 - 1) + J2 + twoL2 + twoK
    P4 = (J1 - 1) + NCV
    P5 = max((J3 - 1) + NCV, J3 + twoLp3 + twoK)
    return dict(M=max(P1, P2, P3, P4, P5), J1=J1, J2=J2, J3=J3, P=(P1, P2, P3, P4, P5), conv=conv1 and conv2,
                twoLp1=twoLp1)


def M_24(t_lo, t_hi, m1_hi, m2_hi, delta=DELTA):
    """Proposition 2.4 (b)-(f), R7.A Proposition A.8: the J = 1 composition remainder's derivatives cost 1 + max(2L,
    2L') more of each factor; a change of chart costs C_ch = 2 J1 + 2L'_1 + 2K xi-derivatives; (d) one more"""
    mu = m1_hi + m2_hi - 1 + delta
    base = M_a(t_lo, t_hi, mu, mu)
    twoL = even_above(n)
    twoLp = even_above(n + abs(m1_hi - 1) + delta)
    C_ch = 2 * base['J1'] + base['twoLp1'] + even_above(n)
    Mb = base['M'] + 1 + max(twoL, twoLp) + C_ch
    return dict(M=Mb + 1, Mb=Mb, base=base, C_ch=C_ch)


# ------------------------------------------------------------------------------------------------- Q5 census
PAT = re.compile(r'd_0')
DEF = re.compile(r'there is|there are|let \$d_0|largest|d_0\\ge|d_0 = |d_0 :=|d_0-|d_0\+|d_0 -|d_0 \+', re.I)
INC = re.compile(r'd_0-(\d)')
CONST = re.compile(r'd_0\\ge\s*(\d)|d_0 = (\d)|d_0\\ge(\d)')
CG = {('PART-II-A-SETUP.md', 941), ('PART-II-A-SETUP.md', 947), ('PART-II-A-SETUP.md', 967)}   # Lemma 8.5


def census(drop=None):
    rows, uncl = [], []
    files = sorted(f for f in os.listdir(P5) if f.startswith('PART-II-') and f.endswith('.md'))
    for f in files:
        for i, line in enumerate(open(os.path.join(P5, f), encoding='utf-8').read().split('\n'), 1):
            if not (PAT.search(line) and DEF.search(line)):
                continue
            key = (f, i)
            if drop and key == drop:
                uncl.append(key)
                continue
            inc = [int(x) for x in INC.findall(line)]
            cst = [int(next(x for x in g if x)) for g in CONST.findall(line)]
            if key in CG:
                cls = 'closed graph (Lemma A.5/A.6)'
            elif inc:
                cls = 'increment %d' % max(inc)
            elif cst:
                cls = 'constant %d' % max(cst)
            elif re.search(r'largest|there is|there are|let \$d_0|depending only|d_0 = d_0|d_0\$, depending', line,
                           re.I):
                cls = 'statement or largest-of'
            elif re.search(r'd_0\\ge d_1\+2|d_0\\ge d_1', line):
                cls = 'increment 2 over d_1'
            elif re.search(r'Definition 8\.1|C\^\{\(d_0|in\s*\$C\^\{d_0\}|d_0\\in', line):
                cls = 'definition or class'
            else:
                uncl.append(key)
                continue
            rows.append((key, cls))
    return rows, uncl


def main():
    print('d0count5: the closed-graph orders of Part II counted (Appendix R7.A), and D_0 at the record\'s orders')
    # Q0: the closed-graph sites (READ, by content)
    a_lines = open(os.path.join(P5, 'PART-II-A-SETUP.md'), encoding='utf-8').read().split('\n')
    a2_lines = open(os.path.join(P5, 'PART-II-A2-STANDARD.md'), encoding='utf-8').read().split('\n')
    sites = {'II.A Lemma 8.5': any('By the closed graph theorem (Fréchet to Banach)' in x for x in a_lines),
             'II.A2 Lemma 1.2': any('by the closed graph theorem, hence jointly' in x for x in a2_lines),
             'II.A2 Prop 2.4': any('has closed graph: if $a_j\\to a$' in x for x in a2_lines)}
    allcg = [(f, i) for f in sorted(os.listdir(P5)) if f.startswith('PART-II-')
             for i, x in enumerate(open(os.path.join(P5, f), encoding='utf-8').read().split('\n'), 1)
             if 'closed graph' in x]
    OK['Q0'] = all(sites.values()) and {f for f, _ in allcg} == {'PART-II-A-SETUP.md', 'PART-II-A2-STANDARD.md'}
    print('  Q0 (READ): the closed-graph sites found by content: %s; every "closed graph" line of Part II lies in '
          'II.A or '
          'II.A2 (%d lines): %s' % (sites, len(allcg), OK['Q0']))
    # Q1
    ex = cv_exponent(DELTA)
    thr = Fr(2, 2 + 5 * n)
    OK['Q1'] = ex < 0 and Fr(NCV, 2) > n and DELTA < thr
    print('  Q1: Theorem A.1 with N = %d pure derivatives each, delta = %s < 2/(2 + 5n) = %s: adjacent-shell sums need '
          'N/2 > n: %s; distant-shell exponent %s < 0: %s' % (NCV, DELTA, thr, Fr(NCV, 2) > n, float(ex), OK['Q1']))
    # Q4 orders
    s_in, s_out = 9, -8
    beta_hi = Fr(3, 2)
    bound_out = -6 - beta_hi                                      # s_out < -6 - beta_+ - eps for every beta_+ < 3/2
    bound_in = Fr(1, 2) + 2 + 5 + 1                               # s_in > 1/2 + theta_H + eta + 1 with theta_H <= 2
    OK['Q4'] = s_out < bound_out and s_in > bound_in and s_in >= 4
    T_LO, T_HI, NMAX = -14, 11, 14
    print('  Q4: s_in = %d > %s, s_out = %d < %s (eta = 5, theta_H <= 2, theta_out >= -2 eps, alpha_+ = beta_+ - 5/2): '
          '%s; s in [%d, %d], s0 = s - 2 in [%d, %d]; the chain\'s orders in [%d, %d], N <= %d' % (
              s_in, bound_in, s_out, bound_out, OK['Q4'], s_out, s_in, s_out - 2, s_in - 2, T_LO, T_HI, NMAX))
    # Q2
    da = D_a(T_LO, T_HI)
    db = D_b(T_HI, -NMAX - 2)
    d86, _, _ = d0_86(T_LO + 2, T_HI, 2, NMAX)
    OK['Q2'] = da['conv'] and db['conv']
    print('  Q2: D_a = %d (J = %d, M0 = %d, t0 = %d), D_b = %d (Jb = %d, sigma = %d, M1 = %d), Lemma 8.6 d_0 = %d; the '
          'remainder kernels converge: %s' % (da['D'], da['J'], da['M0'], da['t0'], db['D'], db['Jb'], db['sigma'],
                                              db['M1'], d86, OK['Q2']))
    # Q3
    ma = M_a(T_LO, T_HI, 0, 2)
    m24 = M_24(T_LO, T_HI, 2, 2)
    OK['Q3'] = ma['conv'] and m24['base']['conv']
    print('  Q3: M_a = %d (pieces P1..P5 = %s; J1 = %d, J2 = %d, J3 = %d); Proposition 2.4 (b)-(f) with chart changes: '
          'M_2.4 = %d (composition %d, C_ch = %d); every remainder condition holds: %s' % (
              ma['M'], ma['P'], ma['J1'], ma['J2'], ma['J3'], m24['M'], m24['Mb'], m24['C_ch'], OK['Q3']))
    # Q5 census
    rows, uncl = census()
    incs = [int(c.split()[1]) for _, c in rows if c.startswith('increment') and c.split()[1].isdigit()]
    OK['Q5'] = not uncl and len(rows) == 89 and max(incs) <= 4
    print('  Q5: %d d_0 lines classified, %d unclassified; classes %s; largest explicit increment d_0 - %d' % (
        len(rows), len(uncl), sorted({c for _, c in rows}), max(incs)))
    for k in uncl:
        print('      unclassified %s' % (k,))
    L3 = max(m24['M'] + 2, da['D'], d86)
    L4 = max(m24['M'] + 4, L3, d86, 2)
    D0 = max(m24['M'] + 6, d86 + 2, da['D'] + 2, L4)
    print('  D_0: (L3) d_0 <= %d, (L4) d_0 <= %d, II.D (symbols in C^(d_0 - 4)) <= %d; so D_0 <= %d (an explicit '
          'integer '
          'upper bound; deduced on Q4\'s order range and Q5\'s census)' % (L3, L4, m24['M'] + 6, D0))
    # Q6
    dp, dpp = max(0, ceil(-s_out)), s_in
    sb, su = max(0, ceil(s_in - 2)), max(0, ceil(-(s_out - 2)))
    d1 = sb + su + 3
    dt = d1 + su + 3
    dt_max = max(0, T_HI) + 2 * max(0, -T_LO) + 6                 # Proposition 9.6's d-tilde on Q4's whole range
    D1_hi = dt_max + 3
    OK['Q6'] = (dp, dpp, d1, dt) == (8, 9, 20, 33) and D1_hi == 48
    print('  Q6: d\' = %d, d\'\' = %d; II.A Proposition 9.6 at s - 2 (Lemma 2.8, Corollary 9.7): d_1 = %d, '
          'd-tilde = %d; '
          'II.E Proposition 4.4 d = d-tilde + 3 >= 35; every tame order of D_1 has the form d-tilde + 3 with '
          'd-tilde = s-bar + 2 max(s-under, s-under_0) + 6 at orders in Q4\'s range, so D_1 <= %d. FWD + BG = D_0 + D_1 '
          '+ d\' + d\'\' + 6 + 2 lies in [%d, %d]; c\' = that + the fixed MODs of a level (not bounded here): %s' % (
              dp, dpp, d1, dt, D1_hi, 35 + 8 + 9 + 8, D0 + D1_hi + 8 + 9 + 8, OK['Q6']))
    print('      at c\' = %d (MODs = 0): d <= 45661383902649727 + 106489470 x %d = %d' % (
        D0 + D1_hi + 25, D0 + D1_hi + 25, 45661383902649727 + 106489470 * (D0 + D1_hi + 25)))
    OK['D0'] = D0 > 0
    # controls
    dm = D_a(T_LO, T_HI, drop=True)
    OK['C1'] = not dm['conv']
    print('  C1 (control): Lemma A.5 with J one less: the remainder kernel converges: %s, so Q2 fails: %s' % (
        dm['conv'], OK['C1']))
    ex2 = cv_exponent(Fr(2, 27))
    OK['C2'] = not (ex2 < 0)
    print('  C2 (control): Theorem A.1 at delta = 2/27: exponent %s, not negative: %s' % (float(ex2), OK['C2']))
    r2, u2 = census(drop=rows[0][0])
    OK['C3'] = len(u2) == 1
    print('  C3 (control): census with the row %s removed: %d unclassified: %s' % (rows[0][0], len(u2), OK['C3']))
    mc = M_a(T_LO, T_HI, 0, 2, drop2L=True)
    OK['C4'] = not mc['conv']
    print('  C4 (control): Proposition A.7 with the right expansion\'s 2L dropped: conditions hold: %s: %s' % (
        mc['conv'], OK['C4']))
    for k, v in OK.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    return 0 if all(OK.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
