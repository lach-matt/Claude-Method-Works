#!/usr/bin/env python3
"""cont5.py -- CERTIFY-10L5-RESULT.md round 5, item 5 (the verifier of round 3, 2(b)): existence by continuity, so
that the compatibility relations of chib, omegab and eta + etab need not propagate.  Labels: deduced (exact: sympy for
C1, z3 over the reals for C2); READ for the local existence theorem it rests on.

Round 4 (prop5.py Q3) found that the hierarchy of null3.py N8 does not propagate the compatibility relations
    chib = e^-w (c_u + b c_x + b_x),   omegab = -e^-w (w_u + b w_x)/2,   eta + etab = 2 e^-c w_x
by any one-directional row, so solving the hierarchy is not by itself an existence scheme.  The route that does not
need them is the one of the literature: the metric is produced by a local existence theorem, and the hierarchy is used
only for a priori estimates of genuine metrics, for which the relations hold by definition.  [CTG23] says so of its own
doubled fields (p. 8, READ): "we do not need an existence theorem, but a system of equations where suitable estimates
apply.  Indeed, we start with a solution of the vacuum Einstein equations, define all the field as above, and thus the
equality ... hold everywhere."  The local theorem in five dimensions is [CTG23] Theorem 1.1 (pp. 2-3, READ): "The
maximal globally hyperbolic development of smooth initial data for vacuum Einstein equations with a (possibly zero)
cosmological constant Lambda in R, on two characteristic hypersurfaces intersecting transversally, contains a future
neighborhood of the initial data hypersurfaces" (higher dimensions; P.T. Chrusciel, R. Tagne Wafo, F. Gray,
arXiv:2305.07306).

What this program checks is the finite content of the continuity argument (CERTIFY-10L5-RESULT.md, round 5, Lemma 9.C):

  C1 (exact) for EVERY metric of the class (w, c, b arbitrary functions: no field equation imposed), the unknowns the
     hierarchy transports, computed from the metric's own connection, satisfy the three compatibility relations
     identically, and the rows N1-N2 hold with the metric's own Ricci frame components as their only source.  So for
     the difference of a genuine vacuum metric and the approximant the hierarchy's sources are the approximant's
     Einstein residual and the quadratic remainder, and no compatibility input enters.
     Control (k1): chib's relation without b_x is not an identity.
  C2 (exact, z3, nonlinear real arithmetic) the bootstrap step.  With y the norm of the difference on D_s, A = F r
     (r the residual's norm) and B = F G (G the quadratic constant), the a priori estimate is y <= A + B y^2.  If
     4 A B < 1 then (a) y <= A + B y^2 and y <= 2A imply y <= A + 4 A^2 B < 2A (the bound improves strictly), and
     (b) the set {y >= 0 : y <= A + B y^2} has no point in (2A, 1/(2B)): it is [0, y-] u [y+, inf) with
     y- <= 2A < 1/(2B) <= y+.  So a continuous y starting at y <= A stays <= 2A, which is the closedness and openness
     of the continuity set.  Vacuity guard: the hypotheses of (a) are satisfiable (z3 returns a model).
     Control (k2): with 4 A B < 2 in place of 4 A B < 1, z3 finds a counterexample to (a).
     Control (k3): with 3A in place of 2A in the conclusion of (a) the claim stays true (a weaker claim) but with
     A + 2 A^2 B in place of A + 4 A^2 B it is refuted: the improvement is exactly the one stated.

  python3 checks/cont5.py
"""
import os, sys, time, importlib.util
import sympy as sp
import z3

HERE = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location('null3', os.path.join(HERE, 'null3.py'))
N3 = importlib.util.module_from_spec(_s); _s.loader.exec_module(N3)
print = N3.print
u, v, x = N3.u, N3.v, N3.x
X3 = [u, v, x]


def c1():
    w, c, b = N3.w, N3.c, N3.b
    g = N3.metric(); G = N3.christoffel(g)
    E4 = sp.Matrix([0, sp.exp(-w), 0]); E3 = sp.Matrix([sp.exp(-w), 0, sp.exp(-w) * b])
    EX = sp.Matrix([0, 0, sp.exp(-c)])
    ip = lambda X, Y: (X.T * g * Y)[0]
    D = lambda X, Y: sp.Matrix([sum(X[n] * sp.diff(Y[m], X3[n]) for n in range(3))
                                + sum(G[m][n][l] * X[n] * Y[l] for n in range(3) for l in range(3)) for m in range(3)])
    vec = lambda X, F_: sum(X[n] * sp.diff(F_, X3[n]) for n in range(3))
    e4, e3 = (lambda F_: vec(E4, F_)), (lambda F_: vec(E3, F_))
    U = {'chi': ip(D(EX, E4), EX), 'chib': ip(D(EX, E3), EX), 'eta': -ip(D(E3, EX), E4) / 2,
         'etab': -ip(D(E4, EX), E3) / 2, 'omega': -ip(D(E4, E3), E4) / 4, 'omegab': -ip(D(E3, E4), E3) / 4}
    rel = {'chib': sp.exp(-w) * (sp.diff(c, u) + b * sp.diff(c, x) + sp.diff(b, x)),
           'omegab': -sp.exp(-w) * (sp.diff(w, u) + b * sp.diff(w, x)) / 2,
           'eta+etab': 2 * sp.exp(-c) * sp.diff(w, x)}
    got = {'chib': U['chib'], 'omegab': U['omegab'], 'eta+etab': U['eta'] + U['etab']}
    comp = {k: N3.zero(got[k] - rel[k]) for k in rel}
    k1 = N3.zero(got['chib'] - sp.exp(-w) * (sp.diff(c, u) + b * sp.diff(c, x)))
    # the metric recovery relations the hierarchy uses (d_v of c, w, b from chi, omega, eta - etab)
    rec = [N3.zero(sp.diff(c, v) - sp.exp(w) * U['chi']), N3.zero(sp.diff(w, v) + 2 * sp.exp(w) * U['omega']),
           N3.zero(sp.diff(b, v) + 2 * sp.exp(2 * w - c) * (U['eta'] - U['etab']))]
    Ric = N3.ricci(g, G)
    fr = {'4': E4, '3': E3, 'x': EX}
    Rf = {i + j: (fr[i].T * Ric * fr[j])[0] for i in '34x' for j in '34x'}
    chi, chib, eta, etab, om, omb = [U[k] for k in ('chi', 'chib', 'eta', 'etab', 'omega', 'omegab')]
    rows = [N3.zero(e4(chi) + chi ** 2 + 2 * om * chi + Rf['44']),
            N3.zero(e3(chib) + chib ** 2 + 2 * omb * chib + Rf['33']),
            N3.zero(e4(eta) + chi * (eta - etab) + Rf['x4']),
            N3.zero(e3(etab) + chib * (etab - eta) + Rf['x3'])]
    return comp, k1, rec, rows


def c2():
    A, B, y, q = z3.Reals('A B y q')
    hyp = z3.And(A > 0, B > 0, y >= 0, 4 * A * B < 1, y <= A + B * y * y, y <= 2 * A)

    def proved(claim, h=hyp):
        s = z3.Solver(); s.set('timeout', 60000); s.add(h, z3.Not(claim))
        r = s.check()
        return r == z3.unsat, r, (s.model() if r == z3.sat else None)
    res = {}
    res['a'] = proved(z3.And(y <= A + 4 * A * A * B, A + 4 * A * A * B < 2 * A))
    # (b) no admissible y in (2A, 1/(2B)); and the small root y- = (1 - q)/(2B), q = sqrt(1 - 4AB), lies in [A, 2A]
    hb = z3.And(A > 0, B > 0, y >= 0, 4 * A * B < 1, y <= A + B * y * y)
    res['b'] = proved(z3.Or(y <= 2 * A, y >= 1 / (2 * B)), hb)
    hq = z3.And(A > 0, B > 0, 4 * A * B < 1, q >= 0, q * q == 1 - 4 * A * B)
    res['b2'] = proved(z3.And((1 - q) / (2 * B) >= A, (1 - q) / (2 * B) <= 2 * A, 2 * A < 1 / (2 * B)), hq)
    s = z3.Solver(); s.add(hyp); vac = s.check()
    vac_model = s.model() if vac == z3.sat else None
    hk = z3.And(A > 0, B > 0, y >= 0, 4 * A * B < 2, y <= A + B * y * y, y <= 2 * A)
    k2 = proved(z3.And(y <= A + 4 * A * A * B, A + 4 * A * A * B < 2 * A), hk)
    k3w = proved(y < 3 * A)
    k3 = proved(y <= A + 2 * A * A * B)
    return res, (vac, vac_model), k2, k3w, k3


def main():
    t0 = time.time(); ok = True
    comp, k1, rec, rows = c1()
    g1 = all(comp.values()) and all(rec) and all(rows)
    print('C1 (exact) on the general metric of the class: compatibility relations %s; metric recovery d_v c, d_v w, '
          'd_v b %s; rows N1 (both), N2 (both) with the metric\'s own Ricci as source %s -> %s'
          % (comp, rec, rows, 'PASS' if g1 else 'FAIL'))
    print('   control (k1) chib without b_x:', 'identity (bad)' if k1 else 'not an identity (good)')
    ok &= g1 and not k1
    print('   (%.0f s)' % (time.time() - t0), flush=True)
    res, (vac, vm), k2, k3w, k3 = c2()
    ga = res['a'][0]; gb = res['b'][0] and res['b2'][0]
    print('C2 (z3) (a) 4AB < 1, y <= A + B y^2, y <= 2A  =>  y <= A + 4A^2 B < 2A:', 'PROVED (unsat)' if ga else
          'NOT PROVED %s' % (res['a'][1],))
    print('   (b) 4AB < 1, y <= A + B y^2  =>  y <= 2A or y >= 1/(2B):', 'PROVED' if res['b'][0] else 'NOT PROVED',
          '; the small root (1 - sqrt(1 - 4AB))/(2B) in [A, 2A] and 2A < 1/(2B):',
          'PROVED' if res['b2'][0] else 'NOT PROVED')
    print('   vacuity guard: hypotheses of (a) satisfiable:', vac, '(model %s)' % vm)
    ok &= ga and gb and vac == z3.sat
    print('   control (k2) 4AB < 2: %s' % ('counterexample found (good): %s' % k2[2] if k2[1] == z3.sat else
                                          'no counterexample (bad) %s' % k2[1]))
    print('   control (k3) y < 3A (weaker) %s; y <= A + 2A^2 B (sharper than proved) %s'
          % ('proved (good)' if k3w[0] else 'not proved (bad)',
             'refuted (good): %s' % k3[2] if k3[1] == z3.sat else 'not refuted (bad) %s' % k3[1]))
    ok &= k2[1] == z3.sat and k3w[0] and k3[1] == z3.sat
    print('cont5 (%.0f s): %s' % (time.time() - t0, 'all checks pass' if ok else 'A CHECK FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
