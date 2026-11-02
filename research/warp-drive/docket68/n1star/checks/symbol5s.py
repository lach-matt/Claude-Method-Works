#!/usr/bin/env python3
"""symbol5s.py -- CERTIFY-10L5-RESULT.md round 3, the verifier of round 2's M1: the principal symbol of the record's
free formulation WITH the shift's second derivatives, and what is left of round 2's obstruction.  Labels: deduced,
every identity exact (sympy, from dnsolve5.py's exact Ricci tensor of the ansatz, via symbol5.py's rows); computed
(floating point) for S6.

symbol5.py Y1 took the 4 x 4 system (R, m, n, W)_uv with the shift held fixed.  Here all five unknowns
(R, m, n, W, s) and all five rows (Ric_11, Ric_22, Ric_xx, Ric(Y, d_v), Ric_vx) are kept.

  S1 (exact) which second derivatives of s enter which row: s_vx in Ric_xx and Ric(Y, d_v), s_vv in Ric_vx, none in
     Ric_11 and Ric_22; no s_uu, s_uv, s_ux, s_xx anywhere.  The f_vx coefficients of Ric_vx are -d zeta (zeta = W +
     2 log R + P + Q, symbol5.py Y1's left null vector).
  S2 (exact) eliminate s at principal order through Ric_vx (c_s xi_v^2 s^ = xi_v xi_x d zeta . f^): the four rows'
     xi_x^2 matrix becomes N_eff = N + n d zeta / c_s (n the s_vx column).  A_eff = M^-1 N_eff / Lambda.
  S3 (exact) A_eff's characteristic polynomial is l^2 (l + 1)^2, as before, but rank A_eff = 2 and rank(A_eff + I) = 2:
     both eigenvalues are semisimple.  NO Jordan block: round 2's Y1/Y3 obstruction is the frozen shift's.
  Control (must fail): the same Jordan test on the frozen-shift system (n -> 0) finds the block (rank A = 3).
  S4 (exact) the shift's first derivative s_x (and s itself) in the four rows, projected on A_eff's eigenvalue-0 left
     eigenvectors (the sector with no x-derivative at principal order).  At high angular frequency k with u, v-scales
     fixed, s ~ k (from s_v ~ d zeta . f_x), so s_x ~ k^2: these terms are of principal size there (Y5's loss).  The
     projections are printed; a nonzero one means the eigenvalue-0 sector is driven by k^2 int (d zeta . f) dv.
  S5 (exact) the constraint-preserving block (cpsolve5: Ric_11, Ric_22, Ric(Y, d_v) for (m, n, W), Ric_vx for s, R
     given) with s_vx eliminated likewise: characteristic polynomial and Jordan test; whether W keeps a W_xx term.
  S6 (computed) a frozen-coefficient check of S4 at a spherical background point: the eigenvalue-0 sector's model
     z_uv = -kappa k^2 int_v z, with kappa = the S4 projection times d zeta's weight on that sector, solved exactly by
     its series; its response at k = 2 .. 32 against the frozen-shift Jordan model's k^2.

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
    present = {lab: [d for d in TWO if co(E[lab], 's_' + d) != 0] for lab in LAB + ['Evx']}
    nvec = sp.Matrix([sp.simplify(co(E[lab], 's_vx')) for lab in LAB])
    cs = sp.simplify(co(E['Evx'], 's_vv'))
    cvec = sp.Matrix([[sp.simplify(co(E['Evx'], f + '_vx')) for f in F4]])
    dz = sp.Matrix([[2 / R, (1 + x) / 3, (1 - x) / 3, 1]])
    good = (present['E11'] == [] and present['E22'] == [] and present['Exx'] == ['vx'] and present['EYv'] == ['vx']
            and present['Evx'] == ['vv'] and sp.simplify(cvec + dz) == sp.zeros(1, 4))
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
    # S6: frozen-coefficient model of the eigenvalue-0 sector driven by s_x
    print('S6 (computed) the model z_uv = -kappa k^2 Z, Z_v = z, data z = 1 on u = 0 and v = 0 (Goursat), solved by its')
    print('   series Z = sum (-kappa k^2)^j u^j v^(2j+1)/(j! (2j+1)!) + ...; |z(1, 1)| against the Jordan model k^2:')
    for kap in (1.0, -1.0):
        row = []
        for k in (2, 4, 8, 16, 32):
            a = -kap * k * k
            # z = d/dv of Z with Z = sum_j a^j u^j v^(2j+1)/(j! (2j+1)!) solves Z_uvv = a Z, Z(0, v) = v, Z(u, 0) = 0
            z = sum(a ** j / (math.factorial(j) * math.factorial(2 * j)) for j in range(0, 400) if abs(a) ** j < 1e300)
            row.append('k = %d: %.3g' % (k, z))
        print('   kappa = %+.0f: %s' % (kap, ', '.join(row)))
    print('   (kappa > 0: bounded, oscillatory; kappa < 0: grows like exp(c k^(2/3)), faster than any power of k --')
    print('    no estimate with finite loss.  Which sign holds on the record\'s solution is not computed here.)')
    print('symbol5s:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
