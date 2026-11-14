#!/usr/bin/env python3
"""baire5: the 18 closed-graph, open-mapping and Banach-Steinhaus sites of proof5, each classified: is its constant
effective, by what replacement, what order or loss it hides, and how big it is (CONSTANTS5.md, Round 2, item (iii)).

The census is nrows5.py's (round 2 pattern: 18 sites, 10 B, 1 A, 6 R, 1 Q), imported, not copied. Labels: READ (the
sites), deduced (the replacements), computed (K1, K2: floating point on matrix models, with exact recursions).

  K1 (deduced; computed check) the classification below covers every site of the census and gives each B and A site a
     replacement. Effective as written: 1 (I4:274, the constructive bound printed beside the theorem). Effective by a
     replacement inside the calculus (a direct estimate whose constant is a dimensional constant times a finite symbol
     or coefficient seminorm): 6 (II.A:960; II.A2:130, 186, 188, 276, 281). Effective by reading the chained proofs
     (C_k a product of the constants of the composed statements): 2 (J3:41, 82). Effective given a base inverse bound
     (the SIGMA chain): 1 (III.H:425, K2). Not effective without a computed lower bound on an operator (as an N1 row):
     1 (II.F:1400, K3).
  K2 (deduced; computed on matrices) III.H:425's replacement. P(s) = P0 + s T + s^2 P2 (I.A (1.1)), R = P^-1 near an
     invertible s*: the Taylor coefficients satisfy c_i = -R*(A c_(i-1) + P2 c_(i-2)), A = T + 2 s* P2, so
     ||R^(i)(s*)||/i! <= ||R*|| [h^i] 1/(1 - a h - p h^2), a = ||R*|| ||A||, p = ||R*|| ||P2||: locally uniform, with
     no Banach-Steinhaus, polynomial of degree i + 1 in ||R*||. Checked on 200 random complex matrix families (n = 6),
     i <= 8. Size: given the base bound ||R*|| (a SIGMA/N1 constant, not computed), i! ||R*||^(i+1) (||T|| + ...)^i.
  K3 (computed on matrices; Round 3: the constants are now computed, not written in) II.F:1400's open-mapping constant
     is 1/(the least singular value of T on ker Pi), Pi Lemma 5.2's projection. For T = diag(0, eps), j = id: the
     inputs of the step -- the constant C of ||x|| <= C (||Tx|| + ||jx||) (computed as a supremum over the unit
     circle), ||T|| and ||Pi|| (computed) -- stay at 1, 1e-1.. and 1, while the output (computed by SVD on ker Pi) is
     1/eps: the step's output is not a function of its inputs, so the proof as written gives no bound there (the N1
     kind); a certified lower bound on sigma_min(T on ker Pi) is what has to be computed instead.
  K4 (READ, deduced) hidden orders and losses (V-m1): II.A:960 "for some d0" (the coefficient regularity); II.A2:188
     "C times a seminorm of X" (the seminorm's order M); J3:41 "a loss eps'(eps, k)" (a weight loss, read off the
     proofs to be independent of k, J3:42-46); J3:82 the loss d of a membership statement is fixed by its orders only
     when the statement's proof is a chain of explicit estimates. So the derivative loss d is unaffected only where
     these orders are fixed by explicit estimates.
  Controls (must fail, and do): C1 a planted site is unclassified; C2 K2's bound without its P2 term fails on a family
  with A = 0; C3 (Round 3, the verifier's m2: round 2's C3 used the hard-coded 1/eps) K3's computation run on the
  mutated family T = diag(0, 1), whose output does not grow, fails K3's test.

    python3 checks/baire5.py
"""
import os
import sys
import textwrap

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nrows5 as NR  # noqa: E402  (the census: pattern and classes, round 2)

# site -> (effectiveness, replacement, hidden order or loss, size)
CLASS = {
    ('PART-II-A-SETUP.md', 960): ('calculus', 'boundedness of multiplication by C^(d0)_e3b on H^s_e3b by the symbol '
                                  'calculus of S5-S8 (a direct estimate)', 'd0 (coefficient regularity)',
                                  'dimensional constant x a C^(d0) seminorm'),
    ('PART-II-A2-STANDARD.md', 130): ('calculus', 'integration by parts in the composition integral for uniformly '
                                      'separated essential supports', 'the residual order -N',
                                      'product of symbol seminorms x separation^-N'),
    ('PART-II-A2-STANDARD.md', 186): ('calculus', 'the separate bounds of the multilinear map made explicit (then C = '
                                      '2^r, printed)', 'the seminorms p_i',
                                      'C = 2^r times the explicit separate bounds'),
    ('PART-II-A2-STANDARD.md', 188): ('calculus', 'Calderon-Vaillancourt with an explicit seminorm order',
                                      'the seminorm order M', 'dimensional constant x a seminorm of order M'),
    ('PART-II-A2-STANDARD.md', 276): ('calculus', 'Calderon-Vaillancourt for Op(a) on variable-order spaces',
                                      'the seminorm order M', 'dimensional constant x ||a||_(M)'),
    ('PART-II-A2-STANDARD.md', 281): ('calculus', 'the composition remainder by Taylor\'s formula in the oscillatory '
                                      'integral', 'the seminorm order', 'product of seminorms'),
    ('PART-II-F-IOTA.md', 1400): ('N1-kind', 'a certified lower bound for T on ker Pi (its least singular value)',
                                  'none', '1/sigma_min(T|ker Pi): not bounded by the a priori constants (K3)'),
    ('PART-III-H-AUGMENT.md', 425): ('base', 'the Neumann series of K2', 'none',
                                     'i! ||R*||^(i+1) (||T|| + 2|s*| ||P2|| + ||P2||)^i, given ||R*||'),
    ('PART-III-I4-BOOST.md', 274): ('as written', 'III.I\' Proposition 2.1\'s constructive bound (printed beside it)',
                                    'none', 'that proposition\'s explicit bound'),
    ('PART-III-J3-TAME.md', 41): ('proofs', 'read each statement\'s bound off its proof (J3:42-46 does so for '
                                  'eps\')', 'eps\'(eps, k), a weight loss', 'product of the chained constants'),
    ('PART-III-J3-TAME.md', 82): ('proofs', 'the chain of explicit estimates of the membership statement',
                                  'the loss d of the statement', 'C_k: product of the chained constants'),
}


def say(s):
    for line in s.split('\n'):
        print(textwrap.fill(line, 121, subsequent_indent='      ', break_long_words=False, break_on_hyphens=False))


def taylor_coeffs(P0, T, P2, s0, imax):
    """exact recursion for the Taylor coefficients of P(s)^-1 at s0, P = P0 + s T + s^2 P2"""
    Ps = P0 + s0 * T + s0 * s0 * P2
    Rs = np.linalg.inv(Ps)
    A = T + 2 * s0 * P2
    c = [Rs]
    for i in range(1, imax + 1):
        prev2 = c[i - 2] if i >= 2 else np.zeros_like(Rs)
        c.append(-Rs @ (A @ c[i - 1] + P2 @ prev2))
    return Rs, A, c


def gen_bound(r, a, p, imax):
    """[h^i] r/(1 - a h - p h^2)"""
    b = [1.0]
    for i in range(1, imax + 1):
        b.append(a * b[i - 1] + (p * b[i - 2] if i >= 2 else 0.0))
    return [r * x for x in b]


def main():
    ok = {}
    hits = NR.baire_census()
    classes = {h: NR.BAIRE.get(h, '?') for h in hits}
    need = [h for h, c in classes.items() if c in ('B', 'A')]
    missing = [h for h in need if h not in CLASS]
    kinds = {}
    for h in need:
        kinds[CLASS[h][0]] = kinds.get(CLASS[h][0], 0) + 1
    ok['K1'] = len(hits) == 18 and not missing and kinds == {'calculus': 6, 'N1-kind': 1, 'base': 1, 'as written': 1,
                                                             'proofs': 2}
    say('  K1: %d sites; B and A sites %d, each classified: %s; by effectiveness: %s' % (len(hits), len(need),
                                                                                         not missing, kinds))
    for h in sorted(need):
        e, rep, hid, size = CLASS[h]
        say('      %s:%d [%s] %s; hides: %s; size: %s' % (h[0].replace('PART-', '').replace('.md', ''), h[1], e, rep,
                                                           hid,
                                                           size))
    rng = np.random.default_rng(4)
    worst = 0.0
    for _ in range(200):
        n = 6
        P0, T, P2 = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)) for _ in range(3))
        s0 = rng.normal() + 1j * rng.uniform(0, 1)
        Rs, A, c = taylor_coeffs(P0, T, P2, s0, 8)
        r = np.linalg.norm(Rs, 2)
        b = gen_bound(r, r * np.linalg.norm(A, 2), r * np.linalg.norm(P2, 2), 8)
        worst = max(worst, max(np.linalg.norm(c[i], 2) / b[i] for i in range(9)))
    # cross-check the recursion against finite differences of the inverse once
    P0, T, P2 = (rng.normal(size=(4, 4)) for _ in range(3))
    s0, h = 0.3, 1e-4
    inv = lambda s: np.linalg.inv(P0 + s * T + s * s * P2)  # noqa: E731
    fd2 = (inv(s0 + h) - 2 * inv(s0) + inv(s0 - h)) / h ** 2 / 2
    rec = taylor_coeffs(P0, T, P2, s0, 2)[2][2]
    ok['K2'] = worst <= 1 + 1e-9 and np.allclose(fd2, rec, rtol=1e-4, atol=1e-6)
    say('  K2: ||c_i|| / ([h^i] ||R*||/(1 - a h - p h^2)) over 200 random families, i <= 8: largest %.4f <= 1; the '
        'recursion equals finite differences of the inverse at i = 2: %s' % (worst, np.allclose(fd2, rec, rtol=1e-4,
                                                                                                   atol=1e-6)))
    # C2: drop P2's term in the bound; a family with A = 0 at s0 breaks it
    P2 = np.eye(3) * 5.0
    P0 = np.eye(3)
    T = np.zeros((3, 3))
    Rs, A, c = taylor_coeffs(P0, T, P2, 0.0, 4)
    r = np.linalg.norm(Rs, 2)
    bad = gen_bound(r, r * np.linalg.norm(A, 2), 0.0, 4)
    ok['C2'] = any(np.linalg.norm(c[i], 2) > bad[i] + 1e-12 for i in range(5))
    say('  C2 (control): without the P2 term the bound is violated (A = 0, P2 = 5 I): %s' % ok['C2'])
    # K3: II.F Lemma 5.2's construction on matrices, every constant computed
    def lemma52(T, j):
        n = T.shape[0]
        u, sv, vt = np.linalg.svd(T)
        ker = vt[np.abs(np.concatenate([sv, np.zeros(n - sv.size)])) < 1e-14].T
        E = j @ ker                                   # j e_k, independent (j injective)
        L = np.linalg.pinv(E)                         # functionals with L (j e_k) = delta_ik (Hahn-Banach in R^n)
        Pi = ker @ L @ j
        th = np.linspace(0, 2 * np.pi, 20001)
        X = np.stack([np.cos(th), np.sin(th)])
        Capri = np.max(1 / (np.linalg.norm(T @ X, axis=0) + np.linalg.norm(j @ X, axis=0)))
        u2, s2, v2 = np.linalg.svd(np.eye(n) - Pi)
        kerPi = u2[:, s2 > 1e-12]                     # range of 1 - Pi = ker Pi
        out = 1 / np.min(np.linalg.svd(T @ kerPi, compute_uv=False))
        return Capri, np.linalg.norm(T, 2), np.linalg.norm(Pi, 2), out

    def k3_test(rows):
        inputs_fixed = all(abs(r[0] - 1) < 1e-6 and r[1] <= 1 and abs(r[2] - 1) < 1e-9 for r in rows)
        return inputs_fixed and rows[0][3] < rows[1][3] < rows[2][3] and rows[2][3] >= 1e6

    rows = [lemma52(np.diag([0.0, eps]), np.eye(2)) for eps in (1e-1, 1e-3, 1e-6)]
    ok['K3'] = k3_test(rows)
    say('  K3: T = diag(0, eps), j = id: (C of the a priori estimate, ||T||, ||Pi||, open-mapping constant) = %s for '
        'eps = 1e-1, 1e-3, 1e-6 (computed): inputs fixed, output 1/eps' % [tuple('%.3g' % x for x in r) for r in rows])
    rows_m = [lemma52(np.diag([0.0, 1.0]), np.eye(2)) for _ in range(3)]
    ok['C3'] = not k3_test(rows_m)
    say('  C3 (control): K3\'s computation on T = diag(0, 1): output %s, not growing: K3 fails for it: %s'
        % (['%.3g' % r[3] for r in rows_m], ok['C3']))
    planted = NR.baire_census(extra=[('PART-PLANTED.md', 1)])
    ok['C1'] = [h for h in planted if h not in NR.BAIRE] == [('PART-PLANTED.md', 1)]
    say('  C1 (control): a planted site is unclassified: %s' % ok['C1'])
    say('  K4: hidden orders and losses: %s' % '; '.join('%s:%d %s' % (h[0].replace('PART-', '').replace('.md', ''),
                                                                       h[1], CLASS[h][2])
                                                         for h in sorted(CLASS) if CLASS[h][2] != 'none'))
    for k, v in ok.items():
        print(k, 'PASS' if v else 'FAIL')
    return 0 if all(ok.values()) else 1


if __name__ == '__main__':
    sys.exit(main())
