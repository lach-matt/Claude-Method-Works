#!/usr/bin/env python3
"""dnull5.py -- the class in double-null gauge: the five-dimensional characteristic structure behind the a posteriori
route at 10 l5 (CERTIFY-10L5.md, step F1; ROUTES-OPEN.md 2 and 4.3).  Labels: computed (exact, sympy).

The metric of the class (paper (2.1)) in double-null gauge, after [Wu26] (1.1) (READ, p. 2) with three-dimensional
sections:
    g5 = -2 Omega^2 (du dv + dv du) + gamma (dth - b du)^2 + e^(2A) dphi1^2 + e^(2B) dphi2^2,
with Omega, b, gamma, A, B functions of (u, v, th).  The sections S_{u,v} are the T^2-symmetric 3-spheres; on the round
sphere th in (0, pi/2) is the Hopf angle, and A, B are the logarithms of the two orbit circles' radii.  Frame:
e3 = Omega^-1 (d_u + b d_th), e4 = Omega^-1 d_v.

  D1 (computed, exact) e3, e4 are null, g(e3, e4) = -2, and both are orthogonal to the sections.
  D2 (computed, exact) The outgoing Raychaudhuri equation in five dimensions.  With the section's principal null
     expansions k1 = d_v gamma/(2 gamma), k2 = d_v A, k3 = d_v B, X := Omega tr chi = k1 + k2 + k3 and
     Omega omega := -(1/2) d_v log Omega,
         Ric(d_v, d_v) = -d_v X - 4 (Omega omega) X - (1/3) X^2 - |Omega chi^|^2,  |Omega chi^|^2 = sum k_i^2 - X^2/3:
     [Wu26]'s fresh check of the outgoing constraint (p. 12) with 1/2 replaced by 1/3, one over the section's
     dimension.  Control: the four-dimensional coefficient 1/2 is not an identity here.
  D3 (computed, exact) The ingoing one, with the shift.  With Y := d_u + b d_th, kb1 = Y(gamma)/(2 gamma) + d_th b,
     kb2 = Y(A), kb3 = Y(B), Xb = sum kb_i and Omega omegab := -(1/2) Y(log Omega),
         Ric(Y, Y) = -Y(Xb) - 4 (Omega omegab) Xb - sum kb_i^2.
     Control: dropping d_th b from kb1 (the shift's contribution to the ingoing second fundamental form) fails.
  D4 (computed, exact) Five-dimensional Tangherlini in Eddington-Finkelstein double-null coordinates, F = 1 - mu/r^2,
     4 Omega^2 = F, b = 0, gamma = r^2, A = log(r cos th), B = log(r sin th), d_v r = F/2, d_u r = -F/2: every
     component of Ric(g5) vanishes.  Control: the four-dimensional F = 1 - mu/r does not.
  D5 (computed, exact) The characteristic hierarchy.  Ric(d_v, d_v) contains no u-derivative and Ric(Y, Y) no second
     v-derivative, so on an outgoing cone u = u0 the data (gamma, A, B) and Omega are tied by an ODE in v alone, and on
     an ingoing cone v = v0 by an ODE in u: the characteristic constraints of [Wu26] Theorem 2.1 (READ, p. 6) keep
     their form in the class in five dimensions.
"""
import sys
import sympy as sp

u, v, th, p1, p2 = sp.symbols('u v theta phi1 phi2', real=True)
X5 = [u, v, th, p1, p2]


def ricci(g, coords):
    n = len(coords)
    gi = sp.zeros(n)
    blk = g[:3, :3].inv()
    for i in range(3):
        for j in range(3):
            gi[i, j] = blk[i, j]
    for i in range(3, n):
        gi[i, i] = 1 / g[i, i]
    G = [[[sp.S(0)] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b_ in range(n):
            for c in range(b_, n):
                s = 0
                for d in range(n):
                    if gi[a, d] != 0:
                        s += gi[a, d] * (sp.diff(g[d, c], coords[b_]) + sp.diff(g[d, b_], coords[c])
                                         - sp.diff(g[b_, c], coords[d]))
                G[a][b_][c] = G[a][c][b_] = sp.together(s / 2)
    R = sp.zeros(n)
    for b_ in range(n):
        for d in range(b_, n):
            s = 0
            for a in range(n):
                s += sp.diff(G[a][b_][d], coords[a]) - sp.diff(G[a][b_][a], coords[d])
                for e in range(n):
                    s += G[a][a][e] * G[e][b_][d] - G[a][d][e] * G[e][b_][a]
            R[b_, d] = R[d, b_] = s
    return R


def metric(Om, b, ga, A, B):
    g = sp.zeros(5)
    g[0, 1] = g[1, 0] = -2 * Om**2
    g[0, 0] = ga * b**2
    g[0, 2] = g[2, 0] = -ga * b
    g[2, 2] = ga
    g[3, 3] = sp.exp(2 * A)
    g[4, 4] = sp.exp(2 * B)
    return g


def zero(e):
    return sp.simplify(sp.expand(sp.together(e))) == 0


def main():
    ok = True
    F = [sp.Function(n)(u, v, th) for n in ('Omega', 'b', 'gamma', 'A', 'B')]
    Om, b, ga, A, B = F
    g = metric(*F)
    # D1
    e3 = sp.Matrix([1, 0, b, 0, 0]) / Om
    e4 = sp.Matrix([0, 1, 0, 0, 0]) / Om
    dth = sp.Matrix([0, 0, 1, 0, 0])
    ip = lambda x, y: sp.simplify((x.T * g * y)[0])
    d1 = [ip(e3, e3), ip(e4, e4), ip(e3, e4) + 2, ip(e3, dth), ip(e4, dth)]
    r = all(x == 0 for x in d1)
    print('D1 e3, e4 null, g(e3, e4) = -2, orthogonal to the sections:', 'PASS' if r else 'FAIL', d1)
    ok &= r
    R = ricci(g, X5)
    # D2
    k = [sp.diff(ga, v) / (2 * ga), sp.diff(A, v), sp.diff(B, v)]
    X = sum(k)
    Omw = -sp.diff(sp.log(Om), v) / 2
    chih2 = sum(x**2 for x in k) - X**2 / 3
    rhs = -sp.diff(X, v) - 4 * Omw * X - X**2 / 3 - chih2
    r2 = zero(R[1, 1] - rhs)
    ctrl = zero(R[1, 1] - (-sp.diff(X, v) - 4 * Omw * X - X**2 / 2 - chih2))
    print('D2 outgoing Raychaudhuri with 1/3:', 'PASS' if r2 else 'FAIL', '| control with 1/2 is an identity:', ctrl)
    ok &= r2 and not ctrl
    # D3
    Y = lambda f: sp.diff(f, u) + b * sp.diff(f, th)
    kb = [Y(ga) / (2 * ga) + sp.diff(b, th), Y(A), Y(B)]
    Xb = sum(kb)
    Omwb = -Y(sp.log(Om)) / 2
    RYY = R[0, 0] + 2 * b * R[0, 2] + b**2 * R[2, 2]
    r3 = zero(RYY - (-Y(Xb) - 4 * Omwb * Xb - sum(x**2 for x in kb)))
    kbc = [Y(ga) / (2 * ga), Y(A), Y(B)]
    Xc = sum(kbc)
    ctrl3 = zero(RYY - (-Y(Xc) - 4 * Omwb * Xc - sum(x**2 for x in kbc)))
    print('D3 ingoing Raychaudhuri with the shift:', 'PASS' if r3 else 'FAIL',
          '| control without d_th b is an identity:', ctrl3)
    ok &= r3 and not ctrl3
    # D5
    hasu = any(isinstance(d, sp.Derivative) and u in d.variables for d in R[1, 1].atoms(sp.Derivative))
    hasvv = any(isinstance(d, sp.Derivative) and list(d.variables).count(v) >= 2
                for d in sp.expand(RYY).atoms(sp.Derivative))
    r5 = (not hasu) and (not hasvv)
    print('D5 Ric(d_v,d_v) has no d_u; Ric(Y,Y) has no d_v^2:', 'PASS' if r5 else 'FAIL')
    ok &= r5
    # D4
    mu = sp.symbols('mu', positive=True)
    for label, Ff, want in (('5D', lambda r: 1 - mu / r**2, True), ('4D control', lambda r: 1 - mu / r, False)):
        rr = sp.Function('r')(u, v)
        Fr = Ff(rr)
        gT = metric(sp.sqrt(Fr) / 2, sp.S(0), rr**2, sp.log(rr * sp.cos(th)), sp.log(rr * sp.sin(th)))
        RT = ricci(gT, X5)
        s = sp.Symbol('s', positive=True)
        Fs, dF = Ff(s), sp.diff(Ff(s), s)
        sub2 = {sp.Derivative(rr, (v, 2)): (dF * Fs / 4).subs(s, rr),
                sp.Derivative(rr, u, v): (-dF * Fs / 4).subs(s, rr),
                sp.Derivative(rr, v, u): (-dF * Fs / 4).subs(s, rr),
                sp.Derivative(rr, (u, 2)): (dF * Fs / 4).subs(s, rr)}
        sub1 = {sp.Derivative(rr, v): Fs.subs(s, rr) / 2, sp.Derivative(rr, u): -Fs.subs(s, rr) / 2}
        allz = all(zero(RT[i, j].subs(sub2).subs(sub1)) for i in range(5) for j in range(i, 5))
        good = allz == want
        print('D4 Tangherlini in double-null,', label, ': Ric = 0 is', allz, '->', 'PASS' if good else 'FAIL')
        ok &= good
    print('dnull5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
