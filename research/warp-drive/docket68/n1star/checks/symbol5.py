#!/usr/bin/env python3
"""symbol5.py -- CERTIFY-10L5-RESULT.md round 2, F5: the principal symbol of the linearised double-null system in the
class, in the formulation dnsolve5.py evolves and in the constraint-preserving one of cpsolve5.py.  Labels: deduced,
every identity exact (sympy, from dnsolve5's exact Ricci tensor of the ansatz).

The uv-system.  dnsolve5 solves, at every point, M (R, m, n, W)_uv = rhs, the rows being Ric_11, Ric_22, Ric_xx and
Ric(Y, d_v) = Ric_uv + (1 - x^2) s Ric_vx.  The second derivatives in these rows are f_uv, f_vx and f_xx (f = R, m,
n, W) and s_vx; M is the matrix of the f_uv coefficients, N of the f_xx ones, V of the f_vx ones.  So the principal part
of the linearised system is  D_u d_v f + K d_xx f  with  K = M^-1 N  and  D_u = d_u + (1 - x^2) s d_x  (Y0).

  Y0 M^-1 V = (1 - x^2) s I: in every row the mixed derivatives are D_u d_v f, the shift entering only through D_u.
  Y1 K = -Lambda A with Lambda = 4 (1 - x^2) e^{2W + 2(P + Q)}/R^2 = e^{2W}/Gx > 0 and A exact; its characteristic
     polynomial is l^2 (l + 1)^2; the eigenvalue -1 is semisimple (rank (A + I) = 2), with left eigenvectors
     (3/(R(1 + x)), 1, 0, 0) and (3/(R(1 - x)), 0, 1, 0): the two wave modes, d[3 log R/(1 +- x) + m or n], i.e.
     log(g11 sqrt g22) and log(sqrt g11 g22) over (1 +- x); the eigenvalue 0 is NOT semisimple (rank A = 3 < 4 - 2):
     a 2 x 2 Jordan block, with left null vector (2/R, (1 + x)/3, (1 - x)/3, 1) = d zeta, zeta = W + 2 log R + P + Q,
     and a generalised left vector eta with eta A = d zeta (computed and checked).
  Y2 the constraint-preserving rows (cpsolve5): Ric_11, Ric_22, Ric(Y, d_v) for (m, n, W)_uv with R given: their 3 x 3
     K3 = -Lambda I exactly (three uncoupled wave operators); R enters them through R_uv and R_xx only, with the exact
     coefficients printed; the Raychaudhuri row Ric_vv has the single second derivative R_vv (coefficient -3/R).
  Y3 no estimate for the weakly hyperbolic system (deduced; the identities exact).  Freeze the coefficients and take
     f = e^{ikx} (a(u, v) e0 + b(u, v) e1) in the Jordan basis (K e0 = 0, K e1 = -Lambda e0, rescaled): the principal
     system is a_uv = k^2 Lambda b, b_uv = 0.  The characteristic data b = 1, a = 0 on u = u0 and v = v0 give the exact
     solution b = 1, a = k^2 Lambda (u - u0)(v - v0) (checked).  The data have norm 1 at frequency k in every H^s(x)
     weighted alike, the solution norm k^2 Lambda (u - u0)(v - v0): so no estimate
         sup_{u, v} ||f(u, v)||_{H^s} <= F (||data||_{H^s} + ||source||)
     with F independent of k holds for any s, and none for the variable-coefficient linearisation either (a frozen-
     coefficient defect of strong hyperbolicity excludes well-posedness in such a scale: Kreiss; Strang).  Hence no
     Newton-Kantorovich argument closes in dnsolve5's formulation, whatever the residual.
     Control: the same construction in the semisimple block, f_uv = -k^2 Lambda f with data 1 on both cones, has the
     exact solution J_0(2k sqrt(Lambda (u - u0)(v - v0))) (checked), bounded by 1 for every k: the test separates.
  Y4 the left eigenvectors of Y1, applied to the rows: the wave-mode rows have principal part -Lambda times the second
     x-derivative of the mode itself (no other field's), and the zeta row has no second x-derivative at all (exact).

  Control (Y1): the constraint-preserving 3 x 3 block of Y2, put through Y1's Jordan test, must NOT show a Jordan
  block (it is diagonal), so the test is not satisfied by every matrix.

  python3 checks/symbol5.py
"""
import os, sys, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('dnsolve5', os.path.join(os.path.dirname(HERE), 'dnsolve5.py'))
d5 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(d5)
F = ['R', 'm', 'n', 'W']


def rows():
    Ric = d5.dn.ricci(d5.g, d5.C)
    E = {lab: sp.expand(d5.tosym(Ric[i, j])) for (i, j), lab in (((3, 3), 'E11'), ((4, 4), 'E22'), ((2, 2), 'Exx'),
                                                                   ((0, 1), 'Euv'), ((1, 2), 'Evx'), ((1, 1), 'Evv'))}
    x, s = d5.x, sp.Symbol('s')
    E['EYv'] = sp.expand(E['Euv'] + (1 - x ** 2) * s * E['Evx'])
    return E


def mats(E, labs):
    co = lambda e, suf: [e.coeff(sp.Symbol(f + suf)) for f in F]
    M = sp.Matrix([co(E[l], '_uv') for l in labs]); N = sp.Matrix([co(E[l], '_xx') for l in labs])
    V = sp.Matrix([co(E[l], '_vx') for l in labs])
    return M, N, V


def jordan_test(A, n_semisimple_eig=-1):
    """(charpoly, rank A, rank (A + I), Jordan block at 0?)"""
    l = sp.Symbol('l')
    cp = sp.factor(A.charpoly(l).as_expr())
    rA = A.rank(simplify=True); rI = sp.simplify(A + sp.eye(A.shape[0])).rank(simplify=True)
    alg0 = sp.Poly(A.charpoly(l).as_expr(), l).as_expr().subs(l, 0) == 0
    mult0 = 0
    p = sp.Poly(sp.factor(A.charpoly(l).as_expr()), l)
    while p.eval(0) == 0 and p.degree() > 0:
        p = sp.Poly(sp.quo(p.as_expr(), l), l); mult0 += 1
    jordan0 = mult0 > 0 and (A.shape[0] - rA) < mult0
    return cp, rA, rI, mult0, jordan0


def main():
    ok = True
    x, s = d5.x, sp.Symbol('s')
    R, W, m, n = [sp.Symbol(k) for k in ('R', 'W', 'm', 'n')]
    E = rows()
    labs = ['E11', 'E22', 'Exx', 'EYv']
    M, N, V = mats(E, labs)
    Minv = M.inv()
    y0 = sp.simplify(Minv * V - (1 - x ** 2) * s * sp.eye(4)) == sp.zeros(4)
    print('Y0 M^-1 V = (1 - x^2) s I:', 'PASS' if y0 else 'FAIL'); ok &= y0
    Lam = 4 * (1 - x ** 2) * sp.exp(2 * W + sp.Rational(2, 3) * ((1 + x) * m + (1 - x) * n)) / R ** 2
    A = sp.simplify(Minv * N / Lam)
    print('Y1 K = M^-1 N = Lambda A, A ='); sp.pprint(A)
    cp, rA, rI, mult0, jordan0 = jordan_test(A)
    l1 = sp.Matrix([[3 / (R * (1 + x)), 1, 0, 0]]); l2 = sp.Matrix([[3 / (R * (1 - x)), 0, 1, 0]])
    l0 = sp.Matrix([[2 / R, (1 + x) / 3, (1 - x) / 3, 1]])
    ev = all(sp.simplify(v * A + v) == sp.zeros(1, 4) for v in (l1, l2)) and sp.simplify(l0 * A) == sp.zeros(1, 4)
    eta = sp.Matrix([[sp.Symbol('e%d' % i) for i in range(4)]])
    sol = sp.solve(list(eta * A - l0), list(eta), dict=True)
    gen = bool(sol)
    good = (sp.expand(cp - sp.Symbol('l') ** 2 * (sp.Symbol('l') + 1) ** 2) == 0 and rA == 3 and rI == 2 and jordan0
            and ev and gen)
    print('   charpoly %s; rank A = %d, rank (A + I) = %d; eigenvalue 0 of algebraic multiplicity %d, Jordan block: %s'
          % (cp, rA, rI, mult0, jordan0))
    print('   left eigenvectors (eigenvalue -1) and left null vector d zeta check: %s; generalised vector eta A = d zeta'
          ' solvable: %s (eta = %s)' % (ev, gen, sol[0] if gen else None))
    print('Y1', 'PASS' if good else 'FAIL'); ok &= good
    # Y2: the constraint-preserving rows
    labs3 = ['E11', 'E22', 'EYv']
    M3f, N3f, _ = mats(E, labs3)
    M3, N3 = M3f[:, 1:], N3f[:, 1:]
    A3 = sp.simplify(M3.inv() * N3 / Lam)
    diag = sp.simplify(A3 + sp.eye(3)) == sp.zeros(3)
    cR = sp.simplify(M3.inv() * N3f[:, 0] / Lam); cRuv = sp.simplify(M3.inv() * M3f[:, 0])
    vv = [k for k in sp.expand(E['Evv']).free_symbols if str(k).endswith(('_vv', '_uv', '_uu', '_xx', '_ux', '_vx'))]
    ray = [str(k) for k in vv] == ['R_vv'] and sp.simplify(sp.expand(E['Evv']).coeff(sp.Symbol('R_vv')) + 3 / R) == 0
    print('Y2 constraint-preserving rows: M3^-1 N3 = -Lambda I: %s; R enters through R_xx with %s (times Lambda) and\n'
          '   R_uv with %s; the Raychaudhuri row has the single second derivative R_vv, coefficient -3/R: %s'
          % (diag, list(cR), list(cRuv), ray))
    cp3, rA3, rI3, mult03, jordan03 = jordan_test(A3)
    print('   control: Jordan test on the 3 x 3 block: charpoly %s, Jordan block at 0: %s ->' % (cp3, jordan03),
          'fails (good)' if not jordan03 else 'passed (bad)')
    good = diag and ray and not jordan03
    print('Y2', 'PASS' if good else 'FAIL'); ok &= good
    # Y3: the frozen-coefficient Goursat solutions
    u, v, u0, v0, k, L = sp.symbols('u v u0 v0 k Lambda', positive=True)
    a = k ** 2 * L * (u - u0) * (v - v0); b = sp.Integer(1)
    jord = (sp.simplify(sp.diff(a, u, v) - k ** 2 * L * b) == 0 and sp.diff(b, u, v) == 0
            and a.subs(u, u0) == 0 and a.subs(v, v0) == 0)
    f = sp.besselj(0, 2 * k * sp.sqrt(L * (u - u0) * (v - v0)))
    wave = (sp.simplify(sp.diff(f, u, v) + k ** 2 * L * f) == 0 and sp.simplify(f.subs(u, u0)) == 1
            and sp.simplify(f.subs(v, v0)) == 1)
    print('Y3 Jordan block: a = k^2 Lambda (u - u0)(v - v0), b = 1 solve a_uv = k^2 Lambda b, b_uv = 0 with data (0, 1):'
          ' %s; growth k^2 Lambda (u - u0)(v - v0), unbounded in k' % jord)
    print('   control (semisimple block): J_0(2k sqrt(Lambda (u - u0)(v - v0))) solves f_uv = -k^2 Lambda f with data 1:'
          ' %s; |J_0| <= 1 for every k -> the bounded case, as it must be' % wave)
    # the Jordan basis behind a_uv = k^2 Lambda b: K e0 = 0, K e1 = -Lambda e0 (right vectors of A)
    e0 = A.nullspace(simplify=True)[0]
    e1s = sp.Matrix(sp.symbols('q0:4'))
    sol1 = sp.solve(list(A * e1s + e0), list(e1s), dict=True)
    good = jord and wave and bool(sol1)
    print('   right Jordan chain A e0 = 0, A e1 = -e0 solvable: %s' % bool(sol1))
    print('Y3', 'PASS' if good else 'FAIL'); ok &= good
    # Y4: rows combined with the left vectors
    second = lambda e: {str(q) for q in e.free_symbols if str(q).endswith('_xx')}
    rowv = sp.Matrix([E[lab] for lab in labs])
    good = True
    for name, lv in (('mode 1', l1), ('mode 2', l2), ('zeta', l0)):
        comb = sp.expand((lv * Minv * rowv)[0])
        xx = {q: sp.simplify(comb.coeff(sp.Symbol(q))) for q in sorted(second(comb))}
        xx = {q: c for q, c in xx.items() if c != 0}
        if name == 'zeta':
            g = not xx
        else:
            mode = 'm' if name == 'mode 1' else 'n'
            g = (set(xx) == {'R_xx', mode + '_xx'} and sp.simplify(xx[mode + '_xx'] + Lam) == 0
                 and sp.simplify(xx['R_xx'] - xx[mode + '_xx'] * lv[0]) == 0)
        print('Y4 %s: second x-derivatives in the combined row: %s -> %s' % (name, sorted(xx), 'PASS' if g else 'FAIL'))
        good &= g
    ok &= good
    print('symbol5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
