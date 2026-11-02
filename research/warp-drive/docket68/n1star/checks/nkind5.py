#!/usr/bin/env python3
"""nkind5: which steps behind lambda1 and delta admit no effective bound from the proof as written, why, and what
would have to be computed instead (CONSTANTS5.md, Round 3, item (iii)).

EFFECTIVE-LEDGER.tsv's 35 N-rows are of four kinds (EFFECTIVE-CONSTANTS.md section 3; nrows5.py R1). For each kind
the step is an argument with stated inputs (constants the proof does produce or could produce) and an output constant.
"No effective bound from this proof" is made precise here: the output is not a function of the inputs, shown by an
explicit family on which every input is fixed (computed) while the output is unbounded (computed). That is a statement
about the argument, not about the operator: a different argument (the effective replacement) may bound the same
constant, and for N2 and N4 the replacement is computed on the model. Labels: computed (exact rationals unless
said); deduced (the reduction of each record site to its model, read at the cited line); READ (the sites).

  K1 (N1: a compact error removed by injectivity; I.C:494-498, I.B:1685, I.B:1978, II.F:1393, III.F'':223,
     III.D:365). Inputs: ||u|| <= C (||P u|| + ||j u||) with j compact, ker P = 0, ||P||. Output: C' with ||u|| <= C'
     ||P u||. Family on R^n (n = 6): P_e = diag(e, 1, ..., 1), j = diag(1, 1/2, ..., 1/n). Computed exactly: the a
     priori constant is C = 1/min_i (|P_i| + |j_i|) = 1/(1 + e) <= 1 for every e < 1/6 (||P u|| + ||j u|| is concave
     in the weights u_i^2, so its minimum on the unit sphere is at an axis; random rational vectors checked below it),
     ||P_e|| = 1, ker P_e = 0; the output C' = 1/sigma_min(P_e) = 1/e. So the contradiction step
     gives no bound; the quantity to compute instead is a certified lower bound for sigma_min of the operator on the
     record's spaces (the inverse norm), which on the model is e.
  K2 (N2: uniformity in parameters by sequences; III.H'''':189, I.C:686, II.F:1063 and twelve more). Inputs: each P(p),
     p in [0, 1], invertible, and p -> P(p) Lipschitz with constant L in norm. Output: sup_p ||P(p)^-1||. Family:
     P_e(p) = diag(p + e, 1): L = 1, every pointwise bound finite (1/(p + e)), the output 1/e. Effective replacement,
     computed: certified base values M_i = ||P(p_i)^-1|| on a grid chosen by the Neumann series (|p - p_i| <= 1/(2 L
     M_i) gives ||P(p)^-1|| <= 2 M_i), which covers [0, 1] in finitely many explicit steps and bounds the supremum by
     2 max M_i; the quantity to compute is the base inverse norms (N1 values) and L in the record's norm.
  K3 (N3: semiclassical absorption at trapping by contradiction; I.B:1513). Inputs: an h-uniform estimate with an
     O(h) error and the absence of a trapped kernel. Output: C with ||u|| <= C h^-1 ||P_h u||. Family: P_{h,l} =
     diag(h l, 1) with the same inputs for every l > 0 and output 1/l: the constant is the inverse of the trapped
     set's expansion rate, which the argument does not produce. The quantity to compute: the explicit multiplier
     estimate at the photon sphere, whose rate is known at b0 (cover5.py: lambda_L^2 = 1/(2 mu)); E2-PILOT's
     sections 3e-3j certify it for the scalar wave in a cut-off norm.
  K4 (N4: finite covers of compact sets; I.A:1570, 1602, I.B:2046 and ten more). Inputs: a local estimate on some
     neighbourhood of each point. Output: the number of patches (and the largest constant over them). Family: radius
     e at every point of [0, 1]: count ceil(1/(2 e)), unbounded at fixed inputs. Effective replacement: explicit radii
     from K2's Neumann series, so the count is computed (the model's: printed).
  K5 (deduced, READ) the chain to lambda1 and delta. delta = eps/2 with eps <= eps_NM/A_2d and A_2d built from the
     tame constants of III.K's right inverses (EFFECTIVE-CONSTANTS.md Proposition 2.2), which rest on the N-rows by
     nrows5.py R3's order. By K2 and K4 the 28 N2 and N4 rows become effective once the N1 and N3 base values and
     the Lipschitz moduli are certified; by K1 and K3 the seven N1/N3 sites admit no effective bound from this proof.
     So a lower bound for delta and lambda1 from this proof needs exactly seven certified quantities (printed, with
     their operators and spaces), together with the calculus constants of the B-rows (baire5.py) and d. The upper
     bounds of deltacap5.py (log10 delta < -7.6666e16, lambda1 < delta) stand.
  Controls (must fail, and do): C1 K1's family with e held at 1 (the mutant): C' stays 1, so K1's test (unbounded
  output at fixed inputs) fails; C2 K2's Neumann cover run with the radius 1/(L M_i) in place of 1/(2 L M_i) at the
  edge loses the factor-2 bound (the computed bound at a midpoint exceeds 2 M_i); C3 K1's a priori constant computed
  with j = 0 (not injective on the kernel direction): the estimate fails (C = infinity at e_1 when e -> 0), so the
  inputs K1 fixes are the ones Lemma 5.2 uses; C4 K4 with radii from K2's cover: the count stays bounded as e
  varies over the grid's own values, so K4's test fails for the effective replacement, as it must.

    python3 checks/nkind5.py
"""
import builtins
import sys
import textwrap
from fractions import Fraction as Fr
from math import ceil

SITES = [
    ('PART-I-C-LOWENERGY.md', 497, 'N1', 'P-hat(0) at zero energy, X_0 -> Y (I.C Theorem 3.1 (4))',
     'sigma_min of P-hat(0) on the b-Sobolev pair of (3.2), b = b0'),
    ('PART-I-B-HIGHENERGY.md', 1685, 'N1', "P'_{h,z}: H^(2,0,0)_h -> L^2 (I.B Theorem 1.3 (b))",
     'the semiclassical inverse norm on the strip of Theorem 1.3'),
    ('PART-I-B-HIGHENERGY.md', 1978, 'N1', 'P-hat(sigma) on the variable-order spaces (I.B section 8.4)',
     '||P-hat(sigma)^-1|| for sigma in the middle range'),
    ('PART-II-F-IOTA.md', 1393, 'N1', 'T Fredholm with weak remainder (II.F Lemma 5.2)',
     'sigma_min of T on ker Pi (baire5.py K3)'),
    ('PART-III-F3-MODES.md', 223, 'N1', 'L-hat_b(sigma), sigma != 0 (III.F\'\' Proposition 3.1)',
     'the inverse norm of the linearised gauge-fixed operator off zero frequency'),
    ('PART-III-D-GAUGEPOT.md', 365, 'N1', 'box-hat(sigma), Im sigma >= 0, sigma != 0 (III.D Proposition 6.2)',
     'the inverse norm on X_sigma -> Y_sigma (E2-PILOT: cut-off L^2 bound, 3 <= sigma <= 384)'),
    ('PART-I-B-HIGHENERGY.md', 1513, 'N3', 'the trapping estimate (6.6) (I.B Proposition 6.4)',
     'the multiplier constant at the photon sphere (rate lambda_L^2 = 1/(2 mu), cover5.py)'),
]


def print(*a, **k):  # noqa: A001  (every printed line within 121 characters)
    for line in ' '.join(str(x) for x in a).split('\n'):
        builtins.print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False,
                                     break_on_hyphens=False), **k)


def diag_family(e, n=6):
    P = [Fr(1)] * n
    P[0] = e
    j = [Fr(1, i + 1) for i in range(n)]
    return P, j


def apriori_C(P, j):
    """sup over u != 0 of ||u|| / (||P u|| + ||j u||) for diagonal P, j: with w_i = u_i^2 on the simplex, ||P u|| =
    (sum w_i P_i^2)^(1/2) and ||j u|| are concave in w, so their sum is minimal at a vertex: the sup is
    max_i 1/(|P_i| + |j_i|), exact (None, no constant, if some P_i = j_i = 0)"""
    vals = []
    for p, q in zip(P, j):
        if p == 0 and q == 0:
            return None
        vals.append(Fr(1) / (abs(p) + abs(q)))
    return max(vals)


def apriori_C_lp(P, j, C):
    """the supremum checked on random rational vectors, exactly: ||u|| <= C (||P u|| + ||j u||) iff nu2/C^2 - pu2 - ju2
    <= 2 (pu2 ju2)^(1/2), decided by squaring when the left side is positive. Returns True if no sample violates it"""
    import random
    rnd = random.Random(11)
    for _ in range(400):
        u = [Fr(rnd.randint(-50, 50), rnd.randint(1, 20)) for _ in P]
        nu2 = sum(x * x for x in u)
        if nu2 == 0:
            continue
        pu2 = sum((p * x) ** 2 for p, x in zip(P, u))
        ju2 = sum((q * x) ** 2 for q, x in zip(j, u))
        lhs = nu2 / (C * C) - pu2 - ju2
        if lhs > 0 and lhs * lhs > 4 * pu2 * ju2:
            return False
    return True


def neumann_cover(e, L=Fr(1), factor=Fr(1, 2)):
    """K2's effective replacement on P(p) = diag(p + e, 1), p in [0, 1]: base points p_i with M_i = ||P(p_i)^-1||
    (exact), step 2 * factor/(L M_i) between centres; returns (count, sup bound 2 max M_i, worst true ratio)"""
    p = Fr(0)
    centres = []
    while True:
        M = max(1 / (p + e), Fr(1))
        r = factor / (L * M)
        centres.append((p, M, r))
        if p + r >= 1:
            break
        p = p + 2 * r
    # check the claimed bound ||P(q)^-1|| <= 2 M_i on each patch edge (the worst point is the left edge q = p_i - r_i)
    worst = Fr(0)
    for p_i, M_i, r_i in centres:
        q = max(Fr(0), p_i - r_i)
        true = max(1 / (q + e), Fr(1))
        worst = max(worst, true / (2 * M_i))
    return len(centres), 2 * max(M for _, M, _ in centres), worst


def main():
    ok = {}
    # K1
    rows = []
    for e in (Fr(1, 10), Fr(1, 1000), Fr(1, 10 ** 6)):
        P, j = diag_family(e)
        C = apriori_C(P, j)
        C_lp = apriori_C_lp(P, j, C)
        normP = max(abs(x) for x in P)
        Cp = 1 / min(abs(x) for x in P)
        rows.append((e, C, C_lp, normP, Cp))
    k1 = all(r[1] <= 1 and r[2] and r[3] == 1 for r in rows) and rows[0][4] < rows[1][4] < rows[2][4]
    ok['K1'] = k1 and rows[2][4] == 10 ** 6
    print('  K1 (N1): P_e = diag(e, 1, ..., 1), j = diag(1, 1/2, ..., 1/6): (e, a priori C, sampled ratios <= C, ||P||, '
          'output C\') = %s (exact): inputs bounded (C <= 1, ||P|| = 1), output 1/e'
          % [(str(r[0]), str(r[1]), r[2], str(r[3]), str(r[4])) for r in rows])
    P, j = diag_family(Fr(1))
    ok['C1'] = not (1 / min(P) > 1)
    print('  C1 (control): the mutant e = 1: C\' = %s, not growing: K1\'s test fails for it: %s' % (1 / min(P),
                                                                                               ok['C1']))
    P0 = [Fr(0)] + [Fr(1)] * 5
    j0 = [Fr(0)] + [Fr(1, i + 1) for i in range(1, 6)]
    ok['C3'] = apriori_C(P0, j0) is None
    print('  C3 (control): with e = 0 and j vanishing on e_1, the a priori estimate fails (no constant): %s'
          % ok['C3'])

    # K2
    k2 = []
    for e in (Fr(1, 10), Fr(1, 100), Fr(1, 1000)):
        cnt, sup_b, worst = neumann_cover(e)
        k2.append((e, cnt, sup_b, worst))
    ok['K2'] = all(w <= 1 for _, _, _, w in k2) and all(s >= 1 / e for e, _, s, _ in k2)
    print('  K2 (N2): P_e(p) = diag(p + e, 1), L = 1: pointwise bounds 1/(p + e) finite, the supremum 1/e; the Neumann '
          'cover (computed, exact): (e, base points, bound 2 max M_i, worst true/bound) = %s' % [
              (str(e), c, str(s), '%.3f' % float(w)) for e, c, s, w in k2])
    _, _, worst_m = neumann_cover(Fr(1, 100), factor=Fr(1))
    ok['C2'] = worst_m > 1
    print('  C2 (control): the cover with radius 1/(L M_i) in place of 1/(2 L M_i): worst true/bound %.3f > 1: the '
          'factor-2 bound fails for it: %s' % (float(worst_m), ok['C2']))

    # K3
    k3 = []
    h = Fr(1, 100)
    for lam in (Fr(1), Fr(1, 10), Fr(1, 1000)):
        P = [h * lam, Fr(1)]
        k3.append((lam, 1 / min(P) * h))
    ok['K3'] = k3[0][1] < k3[1][1] < k3[2][1] and k3[2][1] == 1000
    print('  K3 (N3): P_{h,l} = diag(h l, 1), h = 1/100: the constant C in ||u|| <= C h^-1 ||P u|| is %s for l = 1, '
          '1/10, 1/1000: 1/l, the inverse expansion rate, not produced by the argument' % [str(c) for _, c in k3])

    # K4
    k4 = [(e, ceil(1 / (2 * e))) for e in (Fr(1, 10), Fr(1, 1000), Fr(1, 10 ** 6))]
    ok['K4'] = k4[0][1] < k4[1][1] < k4[2][1]
    eff = [neumann_cover(e)[0] for e in (Fr(1, 10), Fr(1, 100), Fr(1, 1000))]
    print('  K4 (N4): radius e everywhere on [0, 1]: patch counts %s for e = 1/10, 1/1000, 1e-6 (unbounded at fixed '
          'inputs); with K2\'s explicit radii the counts are computed: %s for e = 1/10, 1/100, 1/1000' % (
              [c for _, c in k4], eff))
    ok['C4'] = not (eff[0] < eff[1] < eff[2] and eff[2] > 10 ** 6)
    print('  C4 (control): K4\'s unboundedness test on the effective counts (all below 1e6): fails, as it must: %s'
          % ok['C4'])

    # K5
    print('  K5: the seven sites at which this proof gives no number for the constants behind lambda1 and delta, and '
          'what has to be computed instead (READ at the cited lines; deduced):')
    for f, ln, kind, op, need in SITES:
        print('      %s:%d (%s) %s -> %s' % (f.replace('PART-', '').replace('.md', ''), ln, kind, op, need))
    ok['K5'] = len(SITES) == 7 and sum(1 for s in SITES if s[2] == 'N1') == 6
    for k, v in ok.items():
        builtins.print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
