#!/usr/bin/env python3
"""symbol5s.py -- CERTIFY-10L5-RESULT.md round 3, the verifier of round 2's M1: the principal symbol of the record's
free formulation WITH the shift's second derivatives, and what is left of round 2's obstruction.  Labels: deduced,
every identity exact (sympy, from dnsolve5.py's exact Ricci tensor of the ansatz, via symbol5.py's rows); computed
(floating point) for S6.

symbol5.py Y1 took the 4 x 4 system (R, m, n, W)_uv with the shift held fixed.  Here all five unknowns
(R, m, n, W, s) and all five rows (Ric_11, Ric_22, Ric_xx, Ric(Y, d_v), Ric_vx) are kept.

  S1 (exact) which second derivatives of s enter which row: s_vx in Ric_xx and Ric(Y, d_v), s_vv in Ric_vx, none in
     Ric_11 and Ric_22; no s_uu, s_uv, s_ux, s_xx anywhere (Ric_uv's s_vv cancels in Ric(Y, d_v)).  The f_vx
     coefficients of Ric_vx are -d zeta (zeta = W + 2 log R + P + Q, symbol5.py Y1's left null vector).
  S2 (exact) eliminate s at principal order through Ric_vx (c_s xi_v^2 s^ = xi_v xi_x d zeta . f^): the four rows'
     xi_x^2 matrix becomes N_eff = N + n d zeta / c_s (n the s_vx column).  A_eff = M^-1 N_eff / Lambda.
  S3 (exact) A_eff's characteristic polynomial is l^2 (l + 1)^2, as before, but rank A_eff = 2 and rank(A_eff + I) = 2:
     both eigenvalues are semisimple.  NO Jordan block: round 2's Y1/Y3 obstruction is the frozen shift's.
  Control (must fail): the same Jordan test on the frozen-shift system (n -> 0) finds the block (rank A = 3).
  S4 (exact) the shift's first derivative s_x in the four rows, projected on A_eff's eigenvalue-0 left eigenvectors
     l_0 = (1, 0, 0, 0) (delta R) and l_1 (with d zeta = l_1 + (2/R) l_0).  At angular frequency k with the u, v scales
     fixed, Ric_vx gives s_v = zeta_x/c_s + O(1), so s ~ (ik/c_s) int (d zeta . f) dv and s_x ~ k^2: these "lower-order"
     terms are of principal size in the eigenvalue-0 sector (Y5's loss).  On spherical states: d zeta . M^-1 (s_x
     column) = 0 exactly (delta zeta does not drive itself), but l_0 . M^-1 (s_x column) = R_v (1 - x^2) != 0.
  S5 (exact) the constraint-preserving block (cpsolve5: Ric_11, Ric_22, Ric(Y, d_v) for (m, n, W), Ric_vx for s, R
     given) with s_vx eliminated likewise: charpoly l (l + 1)^2, no Jordan block, W has no W_xx; but its W row carries
     s_x, so on spherical states W (d zeta . e_W = 1) is driven by k^2 int W dv: the eigenvalue-0 mode drives itself.
  S6 (deduced; computed for the model) the two frozen-coefficient consequences.  Free formulation: delta zeta = Z is
     not driven at order k^2, so delta R obeys R_uv = kappa_R k^2 int Z dv, kappa_R = R_v (1 - x^2)/c_s, and grows
     like k^2 u v^2/2: an estimate without loss fails there still, by the shift's Levi term instead of a Jordan block.
     Constraint-preserving formulation: W obeys the model z_uv = -kappa k^2 int z dv, whose Goursat solution (exact
     series, mpmath, k = 2 .. 64) grows faster than any power of k for either sign of kappa: a model only (variable
     coefficients and every O(k) term left out), but it says the metric formulation's loss is not one derivative.
     Neither touches null3.py's frame hierarchy, where s enters only through eta, etab (b_v) and chib (b_x), each
     transported (null3.py N8, N10; linest5.py E2).

  python3 checks/symbol5s.py
"""
import os, sys, importlib.util, math
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('symbol5', os.path.join(HERE, 'symbol5.py'))
S5 = importlib.util.module_from_spec(_s); _s.loader.exec_module(S5)
print = S5.print
F4 = ['R', 'm', 'n', 'W']
LAB = ['E11', 'E22', 'Exx', 'EYv']
TWO = ('uu', 'uv', 'ux', 'vv', 'vx', 'xx')


def jordan(A, n):
    l = sp.Symbol('l')
    cp = sp.factor(A.charpoly(l).as_expr())
    rA = A.rank(simplify=True)
    rI = sp.simplify(A + sp.eye(n)).rank(simplify=True)
    p = sp.Poly(A.charpoly(l).as_expr(), l)
    mult0 = 0
    while p.degree() > 0 and p.eval(0) == 0:
        p = sp.Poly(sp.quo(p.as_expr(), l), l); mult0 += 1
    return cp, rA, rI, mult0, (mult0 > 0 and n - rA < mult0)


def main():
    ok = True
    x, s = S5.d5.x, sp.Symbol('s')
    R, W, m, n = [sp.Symbol(k) for k in ('R', 'W', 'm', 'n')]
    E = S5.rows()
    co = lambda e, name: sp.expand(e).coeff(sp.Symbol(name))
    # S1
    present = {lab: [d for d in TWO if sp.simplify(co(E[lab], 's_' + d)) != 0] for lab in LAB + ['Evx']}
    nvec = sp.Matrix([sp.simplify(co(E[lab], 's_vx')) for lab in LAB])
    cs = sp.simplify(co(E['Evx'], 's_vv'))
    cvec = sp.Matrix([[sp.simplify(co(E['Evx'], f + '_vx')) for f in F4]])
    dz = sp.Matrix([[2 / R, (1 + x) / 3, (1 - x) / 3, 1]])
    euv_svv = sp.simplify(co(E['Euv'], 's_vv') + (1 - x ** 2) * s * cs)
    good = (present['E11'] == [] and present['E22'] == [] and present['Exx'] == ['vx']
            and present['EYv'] == ['vx'] and euv_svv == 0
            and present['Evx'] == ['vv'] and sp.simplify(cvec + dz) == sp.zeros(1, 4))
    print('   Ric_uv carries s_vv with coefficient -(1 - x^2) s c_s (exact: %s), which (1 - x^2) s Ric_vx cancels in '
          'Ric(Y, d_v)' % (euv_svv == 0))
    print('S1 second derivatives of s by row:', present, '; s_vx column (E11, E22, Exx, EYv):', list(nvec),
          '; Ric_vx: s_vv coefficient', cs, ', f_vx coefficients = -d zeta:', sp.simplify(cvec + dz) == sp.zeros(1, 4),
          '->', 'PASS' if good else 'FAIL')
    ok &= good
    # S2-S3
    M, N, V = S5.mats(E, LAB)
    Lam = 4 * (1 - x ** 2) * sp.exp(2 * W + sp.Rational(2, 3) * ((1 + x) * m + (1 - x) * n)) / R ** 2
    Neff = N - nvec * cvec / cs
    Minv = M.inv()
    A0 = sp.simplify(Minv * N / Lam)
    Aeff = sp.simplify(Minv * Neff / Lam)
    cp, rA, rI, m0, jb = jordan(Aeff, 4)
    print('S2 A_eff = M^-1 (N + n dzeta/c_s)/Lambda ='); print(sp.pretty(Aeff, num_columns=118))
    good = sp.expand(cp - sp.Symbol('l') ** 2 * (sp.Symbol('l') + 1) ** 2) == 0 and rA == 2 and rI == 2 and not jb
    print('S3 charpoly %s; rank A_eff = %d, rank(A_eff + I) = %d; Jordan block at 0: %s ->' % (cp, rA, rI, jb),
          'PASS (no Jordan block)' if good else 'FAIL')
    ok &= good
    cp0, rA0, rI0, m00, jb0 = jordan(A0, 4)
    print('   control (n -> 0, the frozen shift of symbol5.py): rank A = %d, Jordan block: %s ->' % (rA0, jb0),
          'the no-Jordan test fails (good)' if jb0 else 'passes (bad)')
    ok &= jb0
    # S4: left eigenvectors of A_eff at 0, and the s_x, s projections
    L0 = Aeff.T.nullspace(simplify=True)
    sig1 = sp.Matrix([sp.simplify(co(E[lab], 's_x')) for lab in LAB])
    sig0 = sp.Matrix([sp.simplify(co(E[lab], 's')) for lab in LAB])
    R0 = Aeff.nullspace(simplify=True)
    print('S4 eigenvalue-0 left eigenvectors of A_eff:', [list(sp.simplify(q.T)) for q in L0])
    print('   eigenvalue-0 right eigenvectors:', [list(sp.simplify(q.T)) for q in R0])
    sph = {m: 0, n: 0, s: 0}
    sph.update({sp.Symbol(k): 0 for k in ('m_u', 'm_v', 'm_x', 'n_u', 'n_v', 'n_x', 's_u', 's_v', 's_x')})
    proj = []
    for i, lv in enumerate(L0):
        p1 = sp.simplify((lv.T * Minv * sig1)[0])
        p1s = sp.simplify(p1.subs(sph))
        wts = [sp.simplify((dz * rv)[0]) for rv in R0]
        proj.append((p1, p1s, wts))
        print('   left vector %d: l . M^-1 (s_x column) = %s; on spherical states (m = n = s = 0, their derivatives 0): '
              '%s; d zeta on the right eigenvectors: %s' % (i, sp.count_ops(p1), p1s, wts))
    nz = any(p[1] != 0 for p in proj)
    print('   so the eigenvalue-0 sector %s driven by s_x on spherical states (the Levi term of Y5).' % (
        'IS' if nz else 'is NOT'))
    # d zeta = l_1 + (2/R) l_0: the combination that s itself carries
    dzp = sp.simplify((dz * Minv * sig1)[0].subs(sph))
    evx_sx = sp.simplify(co(E['Evx'], 's_x').subs(sph)); evx_s = sp.simplify(co(E['Evx'], 's').subs(sph))
    print('   d zeta . M^-1 (s_x column) on spherical states: %s  (so delta zeta is not driven at order k^2 by its own '
          'shift; delta R, the l_0 component, is: l_0 . M^-1 (s_x column) = %s)' % (dzp, proj[0][1]))
    print('   Ric_vx\'s own s_x and s coefficients on spherical states: %s, %s  (zero: there s_v = zeta_x/c_s + O(1) '
          'and s ~ (ik/c_s) int (d zeta . f) dv at angular frequency k)' % (evx_sx, evx_s))
    ok &= dzp == 0
    S4res = (proj[0][1], cs.subs(sph))
    # S5: the constraint-preserving block with s_vx
    lab3 = ['E11', 'E22', 'EYv']
    M3f, N3f, _ = S5.mats(E, lab3)
    n3 = sp.Matrix([sp.simplify(co(E[lab], 's_vx')) for lab in lab3])
    c3 = cvec[:, 1:]
    N3eff = N3f[:, 1:] - n3 * c3 / cs
    A3 = sp.simplify(M3f[:, 1:].inv() * N3eff / Lam)
    cp3, rA3, rI3, m03, jb3 = jordan(A3, 3)
    wxx = sp.simplify((M3f[:, 1:].inv() * N3eff)[2, 2])
    print('S5 constraint-preserving block with s_vx: A3 ='); print(sp.pretty(A3, num_columns=118))
    print('   charpoly %s, rank A3 = %d, rank(A3 + I) = %d, Jordan block: %s; the W row\'s own W_xx coefficient: %s' % (
        cp3, rA3, rI3, jb3, wxx))
    sig3 = sp.Matrix([sp.simplify(co(E[lab], 's_x')) for lab in lab3])
    pW = sp.simplify((M3f[:, 1:].inv() * sig3)[2].subs(sph))
    print('   the W row (after M3^-1) carries s_x with coefficient %s on spherical states; with s ~ (ik/c_s) int '
          '(d zeta . f) and d zeta . e_W = 1, W is driven by k^2 int W dv there: the eigenvalue-0 mode drives itself.'
          % pW)
    good3 = not jb3 and wxx == 0 and pW != 0
    print('S5', 'PASS' if good3 else 'FAIL'); ok &= good3
    # S6: frozen-coefficient consequences
    import mpmath as mp
    mp.mp.dps = 60
    kR, csph = S4res
    print('S6 (deduced) free formulation, spherical states: delta R_uv = kappa_R k^2 int Z dv, kappa_R = %s, '
          'Z = delta zeta undriven at order k^2: delta R ~ kappa_R k^2 u v^2/2, growth k^2 (no estimate without loss).'
          % (
              sp.simplify(kR / csph)))
    print('   (computed, model) constraint-preserving W: z_uv = -kappa k^2 int z dv, Goursat data z = 1 on u = 0 and '
          'v = 0;')
    print('   exact series z(u, v) = sum_j a^j u^j v^(2j)/(j! (2j)!), a = -kappa k^2; |z(1, 1)| against k^2:')
    grow = {}
    for kap in (1.0, -1.0):
        vals = []
        for k in (2, 4, 8, 16, 32, 64):
            a_ = mp.mpf(-kap * k * k)
            z = mp.nsum(lambda j: a_ ** j / (mp.factorial(j) * mp.factorial(2 * j)), [0, mp.inf])
            vals.append((k, float(abs(z))))
        grow[kap] = vals
        print('   kappa = %+.0f: %s' % (kap, ', '.join('k = %d: %.3g' % kv for kv in vals)))
    sup_pow = all(v2 / v1 > (k2 / k1) ** 2 for (k1, v1), (k2, v2) in zip(grow[-1.0][-3:-1], grow[-1.0][-2:]))
    sup_pow2 = grow[1.0][-1][1] / grow[1.0][-2][1] > 4
    print('   both signs outgrow k^2 at the top of the range: %s, %s (the series grows like exp(c k^(2/3)))' % (
        sup_pow, sup_pow2))
    ok &= sup_pow and sup_pow2
    print('symbol5s:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
