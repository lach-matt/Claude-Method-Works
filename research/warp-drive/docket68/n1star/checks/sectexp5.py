#!/usr/bin/env python3
"""sectexp5.py -- the outgoing expansion of an arbitrary T^2-invariant section of an ingoing cone, in dnsolve5.py's
double-null gauge, and the two monotonicity facts CERTIFY-10L5-RESULT.md section 1 rests on.  Labels: computed (exact,
sympy, unless marked floating point); the deductions drawn from them are in the note.

The metric (dnsolve5.py): g5 = -4 e^{2W} du dv + Gx (dx - beta du)^2 + R^2 (1+x)/2 e^{2P} dphi1^2 + R^2 (1-x)/2 e^{2Q}
dphi2^2, Gx = R^2 e^{-2(P+Q)}/(4(1-x^2)), beta = (1-x^2) s, P = (2(1+x)m - (1-x)n)/3, Q = (2(1-x)n - (1+x)m)/3.  The
sections S_{u,v} of the double-null foliation have volume density sqrt(det) = R^3/4 exactly, d_v is their outgoing null
normal and n := d_u + beta d_x their ingoing one.

  X1 (exact) Raychaudhuri along d_v: Ric_vv = -(3/R)(R_vv - 2 W_v R_v) - (P_v^2 + Q_v^2 + (P_v + Q_v)^2), with no s and
     no x-derivative.  So in vacuum d_v(e^{-2W} R_v) = -(R/3) e^{-2W} (P_v^2 + Q_v^2 + (P_v + Q_v)^2) <= 0 along every
     outgoing generator (u, x fixed).  Control: with 2 W_v replaced by W_v the identity fails.
  X2 (exact) a section of the cone {v = v*} given parametrically by u = U(xi), x = X(xi), invariant under T^2: its
     future outgoing null normal l = d_v + a d_u + c d_x (a = Gx w^2/(4 e^{2W}) >= 0, c = w + a beta,
     w = 2 e^{2W} U'/(Gx (X' - beta U'))), and its expansion theta[S] = l(ln sqrt(g11 g22)) + g(nabla_e l, e)/g(e, e),
     e = U' d_u + X' d_x.  Checked: (a) on a leaf (U' = 0) theta = 3 R_v/R; (b) where the section is tangent to a leaf
     (U' = 0, X' = 1, X'' = 0) theta = 3 R_v/R + 2 e^{2W} U''/Gx, so at a point where U is largest (the section's
     innermost point, U'' <= 0) the section's expansion is at most the leaf's there; (c) the expansion does not depend
     on the parametrisation (xi -> psi(xi), exact).  Control: without the derivative of l along the section, (b) fails.
  X3 (floating point) the formula against an independent computation: flat five-dimensional Minkowski space (R = (v -
     u)/2, e^{2W} = 1/4, m = n = s = 0) embedded in R^{4,1}, a non-round section u = f(x) of the cone v = 1, its null
     normals and mean-curvature vector by finite differences of the embedding, theta = -<l, H>; agreement to 1e-6 at
     twelve angles.  Control: the leaf's expansion 3 R_v/R in place of the formula disagrees there by more than 1e-2.

Run: python3 checks/sectexp5.py            (about a minute)
"""
import os, sys, importlib.util
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


d5 = load('dnsolve5')
u, v, x = d5.u, d5.v, d5.x
NAMES = d5.names                                     # R, m, n, W, s
SYM = {k: sp.Symbol(k) for k in NAMES}
DSYM = {(k, c): sp.Symbol(k + '_' + c) for k in NAMES for c in 'uvx'}
Rs, ms, ns, Ws, ss = [SYM[k] for k in NAMES]
Ps = (2*(1 + x)*ms - (1 - x)*ns)/3
Qs = (2*(1 - x)*ns - (1 + x)*ms)/3
Gxs = Rs**2*sp.exp(-2*(Ps + Qs))/(4*(1 - x**2))
bes = (1 - x**2)*ss
g11 = Rs**2*(1 + x)/2*sp.exp(2*Ps)
g22 = Rs**2*(1 - x)/2*sp.exp(2*Qs)
GS = sp.zeros(5)
GS[0, 1] = GS[1, 0] = -2*sp.exp(2*Ws); GS[2, 2] = Gxs; GS[0, 2] = GS[2, 0] = -Gxs*bes; GS[0, 0] = Gxs*bes**2
GS[3, 3] = g11; GS[4, 4] = g22


def D(expr, c):
    """the coordinate derivative d_c (c in u, v, x) of an expression in the field symbols and x"""
    out = sum(sp.diff(expr, SYM[k])*DSYM[(k, c)] for k in NAMES)
    if c == 'x':
        out += sp.diff(expr, x)
    return out


def christoffel():
    gi = sp.zeros(5)
    gi[:3, :3] = sp.simplify(GS[:3, :3].inv())
    gi[3, 3] = 1/GS[3, 3]; gi[4, 4] = 1/GS[4, 4]
    dg = {}
    for c, cn in enumerate('uvx'):
        dg[c] = GS.applyfunc(lambda e: D(e, cn))
    for c in (3, 4):
        dg[c] = sp.zeros(5)
    Gam = [[[0]*5 for _ in range(5)] for _ in range(5)]
    for a in range(5):
        for b in range(5):
            for c in range(5):
                Gam[a][b][c] = sum(gi[a, d]*(dg[b][d, c] + dg[c][d, b] - dg[d][b, c]) for d in range(5)
                                   if gi[a, d] != 0)/2
    return Gam


U1, X1, U2, X2 = sp.symbols('U1 X1 U2 X2', real=True)


def theta_expr(with_dl=True):
    """theta[S] for the section u = U(xi), x = X(xi) of {v = v*}; with_dl False drops e(l^mu) (the control)"""
    w = 2*sp.exp(2*Ws)*U1/(Gxs*(X1 - bes*U1))
    a = Gxs*w**2/(4*sp.exp(2*Ws))
    c = w + a*bes
    l = [a, sp.Integer(1), c, 0, 0]
    e = [U1, 0, X1, 0, 0]
    Gam = christoffel()

    def along(expr):            # d/dxi of an expression in the fields, x, U1, X1, at the point (U(xi), v*, X(xi))
        return (D(expr, 'u')*U1 + D(expr, 'x')*X1 + sp.diff(expr, U1)*U2 + sp.diff(expr, X1)*X2)
    nab = []
    for mu in range(5):
        t = sum(Gam[mu][r][s_]*e[r]*l[s_] for r in range(5) for s_ in range(5) if e[r] != 0 and l[s_] != 0)
        if with_dl:
            t += along(l[mu]) if l[mu] != 0 else 0
        nab.append(t)
    gee = sum(GS[i, j]*e[i]*e[j] for i in range(3) for j in range(3))
    term_e = sum(GS[i, j]*nab[i]*e[j] for i in range(3) for j in range(3))/gee
    lnphi = sp.log(g11*g22)/2
    term_phi = sum(l[i]*D(lnphi, 'uvx'[i]) for i in range(3))
    return term_phi + term_e


def simp0(e):
    return sp.simplify(sp.expand(e)) == 0


def x1(control=False):
    gsym = d5.g
    Ric = d5.dn.ricci(gsym, d5.C)
    Evv = d5.tosym(Ric[1, 1])
    S_ = sp.Symbol
    R_, W_ = S_('R'), S_('W')
    P_ = (2*(1 + x)*S_('m') - (1 - x)*S_('n'))/3
    Q_ = (2*(1 - x)*S_('n') - (1 + x)*S_('m'))/3
    Pv = sp.diff(P_, S_('m'))*S_('m_v') + sp.diff(P_, S_('n'))*S_('n_v')
    Qv = sp.diff(Q_, S_('m'))*S_('m_v') + sp.diff(Q_, S_('n'))*S_('n_v')
    k = 1 if control else 2
    claim = -(3/R_)*(S_('R_vv') - k*S_('W_v')*S_('R_v')) - (Pv**2 + Qv**2 + (Pv + Qv)**2)
    free = {str(a) for a in Evv.free_symbols}
    no_s = not any(f.startswith('s') for f in free) and not any('x' in f.split('_')[1] for f in free if '_' in f)
    return simp0(Evv - claim) and no_s


def x2(control=False):
    th = theta_expr(with_dl=not control)
    leaf = th.subs({U1: 0, X1: 1, U2: 0, X2: 0})
    ok_a = simp0(leaf - 3*DSYM[('R', 'v')]/Rs)
    tang = th.subs({U1: 0, X1: 1, X2: 0})
    ok_b = simp0(tang - (3*DSYM[('R', 'v')]/Rs + 2*sp.exp(2*Ws)*U2/Gxs))
    if control:
        return ok_b
    # (c) reparametrisation: xi = psi(eta), U1 -> U1 p1, U2 -> U2 p1^2 + U1 p2 (same for X)
    p1, p2 = sp.symbols('p1 p2', positive=True)
    th2 = th.subs({U1: U1*p1, X1: X1*p1, U2: U2*p1**2 + U1*p2, X2: X2*p1**2 + X1*p2}, simultaneous=True)
    vals = {}
    rng = np.random.default_rng(5)
    for sym in list(th.free_symbols) + [p1, p2]:
        vals[sym] = sp.Rational(int(rng.integers(1, 9)), int(rng.integers(2, 11)))
    vals[x] = sp.Rational(1, 3)
    vals[ss] = sp.Rational(1, 5)
    ok_c = abs(sp.N(th.subs(vals) - th2.subs(vals), 40)) < sp.Float('1e-30')
    print('    X2 (a) leaf %s, (b) tangent point %s, (c) reparametrisation %s' % (ok_a, ok_b, ok_c))
    return ok_a and ok_b and ok_c


def theta_numeric(with_dl=True):
    th = theta_expr(with_dl)
    args = [x] + [SYM[k] for k in NAMES] + [DSYM[(k, c)] for k in NAMES for c in 'uvx'] + [U1, X1, U2, X2]
    f = sp.lambdify(args, th, 'numpy', cse=True)

    def ev(xx, F, dF, U1_, X1_, U2_, X2_):
        """F[k], dF[(k, c)] arrays; returns theta"""
        return f(xx, *[F[k] for k in NAMES], *[dF[(k, c)] for k in NAMES for c in 'uvx'], U1_, X1_, U2_, X2_)
    return ev


def flat_embed(vs, fu, xx, ph1=0.3, ph2=1.1):
    t = (fu + vs)/2; r = (vs - fu)/2
    c = np.sqrt((1 + xx)/2); s = np.sqrt((1 - xx)/2)
    return np.array([t, r*c*np.cos(ph1), r*c*np.sin(ph1), r*s*np.cos(ph2), r*s*np.sin(ph2)])


def x3(control=False):
    ev = theta_numeric(True)
    eta = np.diag([-1.0, 1, 1, 1, 1])
    f = lambda q: -3 + 0.4*q + 0.3*q**2 + 0.15*np.sin(3*q)
    f1 = lambda q: 0.4 + 0.6*q + 0.45*np.cos(3*q)
    f2 = lambda q: 0.6 - 1.35*np.sin(3*q)
    vs = 1.0
    worst = 0.0
    for xx in np.linspace(-0.9, 0.9, 12):
        h = 1e-4
        X = lambda q, a, b: flat_embed(vs, f(q), q, a, b)
        p1, p2 = 0.3, 1.1
        Ex = (X(xx + h, p1, p2) - X(xx - h, p1, p2))/(2*h)
        E1 = (X(xx, p1 + h, p2) - X(xx, p1 - h, p2))/(2*h)
        E2 = (X(xx, p1, p2 + h) - X(xx, p1, p2 - h))/(2*h)
        E = np.array([Ex, E1, E2])
        gam = E @ eta @ E.T
        gi = np.linalg.inv(gam)
        H2 = {}
        H2[(0, 0)] = (X(xx + h, p1, p2) - 2*X(xx, p1, p2) + X(xx - h, p1, p2))/h**2
        H2[(1, 1)] = (X(xx, p1 + h, p2) - 2*X(xx, p1, p2) + X(xx, p1 - h, p2))/h**2
        H2[(2, 2)] = (X(xx, p1, p2 + h) - 2*X(xx, p1, p2) + X(xx, p1, p2 - h))/h**2
        H2[(0, 1)] = H2[(1, 0)] = (X(xx + h, p1 + h, p2) - X(xx + h, p1 - h, p2) - X(xx - h, p1 + h, p2)
                                   + X(xx - h, p1 - h, p2))/(4*h*h)
        H2[(0, 2)] = H2[(2, 0)] = (X(xx + h, p1, p2 + h) - X(xx + h, p1, p2 - h) - X(xx - h, p1, p2 + h)
                                   + X(xx - h, p1, p2 - h))/(4*h*h)
        H2[(1, 2)] = H2[(2, 1)] = (X(xx, p1 + h, p2 + h) - X(xx, p1 + h, p2 - h) - X(xx, p1 - h, p2 + h)
                                   + X(xx, p1 - h, p2 - h))/(4*h*h)
        Hv = sum(gi[i, j]*H2[(i, j)] for i in range(3) for j in range(3))
        # normal space: vectors orthogonal to E; null normals; pick the one not along d_u of the cone
        A = E @ eta
        _, _, Vt = np.linalg.svd(A)
        N1, N2 = Vt[-1], Vt[-2]
        # null combinations N1 + k N2
        a_, b_, c_ = N2 @ eta @ N2, 2*N1 @ eta @ N2, N1 @ eta @ N1
        ks = np.roots([a_, b_, c_]).real
        cand = [N1 + k*N2 for k in ks]
        # d_u at the point: (1/2)(d_t - d_r) in the embedding; d_v = (1/2)(d_t + d_r)
        rhat = np.r_[0, flat_embed(vs, f(xx), xx, p1, p2)[1:]]; rhat = rhat/np.linalg.norm(rhat[1:])
        du = 0.5*(np.r_[1, 0, 0, 0, 0] - rhat); dvv = 0.5*(np.r_[1, 0, 0, 0, 0] + rhat)
        # the outgoing one is the candidate not parallel to the cone's generator d_u
        par = [abs((cv @ eta @ du)) for cv in cand]
        l = cand[int(np.argmax(par))]
        # normalise: coefficient of d_v is 1, i.e. <l, d_u> = <d_v, d_u> = -1/2
        l = l*(-0.5)/(l @ eta @ du)
        th_emb = -(l @ eta @ Hv)
        F = {'R': (vs - f(xx))/2, 'm': 0.0, 'n': 0.0, 'W': np.log(0.5), 's': 0.0}
        dF = {(k, c): 0.0 for k in NAMES for c in 'uvx'}
        dF[('R', 'u')] = -0.5; dF[('R', 'v')] = 0.5
        if control:
            th_f = 3*0.5/F['R']
        else:
            th_f = float(ev(xx, F, dF, f1(xx), 1.0, f2(xx), 0.0))
        worst = max(worst, abs(th_f - th_emb))
    print('    X3 %s: max |theta_formula - theta_embedding| = %.2e' % ('control' if control else 'formula', worst))
    return worst < 1e-6 if not control else worst < 1e-2


CHECKS = [('X1', x1), ('X2', x2), ('X3', x3)]


def main():
    ok = True
    for name, fn in CHECKS:
        good = fn()
        ctl = fn(control=True)
        print('%s %s%s' % (name, 'PASS' if good and not ctl else 'FAIL', ' (control passed)' if ctl else ''), flush=True)
        ok &= good and not ctl
    print('sectexp5:', 'all checks pass' if ok else 'FAILURES')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
