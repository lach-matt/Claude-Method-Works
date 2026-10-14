#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for gr-qc/0209075#needs-solution.

Claim audited (tree, linstab.py:52-57, 273-276): AMM's linear-response equation
(3.4) is the first variation of the semiclassical equations (2.9) ABOUT A
SOLUTION of them.  AMM p. 8: expand the CTP effective action 'around a given
semi-classical geometry g_ab that solves eq. (2.9)' ... (3.3) 'where the first
variation vanishes by (2.9)'; p. 9: Pi^(ret) 'is evaluated in the background
geometry of the leading order solution of the semi-classical equations (2.9)'.

Checks (independent code; nothing imported from research/warp-drive):
  C1  generic action S(q): S(q0+eps h) to O(eps^2); stationarity in h gives
      E(q0) + K(q0) h = 0.  The homogeneous equation K h = 0 (the form of AMM
      (3.4)) is the first variation of E = 0 iff E(q0) = 0.  (sympy, symbolic)
  C2  GAUGE: for a diffeomorphism-covariant tensor E_ab[g] (here the Einstein
      tensor + Lambda g, the classical part of AMM's LHS (2.9)), the identity
      E'[g](L_X g) = L_X E[g] holds for every g.  Hence a pure-gauge h = L_X g
      (AMM (3.11)) solves the homogeneous linearised equation iff L_X E[g] = 0;
      at a solution E = 0 it does for EVERY X; off a solution it fails for
      some X.  So (3.4)'s stated gauge freedom (3.11) itself presupposes H1.
      Machine-checked on f = 1 - 2M/r - c r (c = 0: Schwarzschild, a vacuum
      solution; c != 0: not one), X = x(r) d_r.  (sympy)
  C3  the tree's witnesses W1, W2 (linstab.py:662-702) re-derived here from
      scratch: linearising about a non-equilibrium gives a boundedness verdict
      that disagrees with the true flow, in both directions.  (sympy)
  C4  control: at the equilibria of W1 the verdict agrees with the flow.
Exit 0 iff every check returns its expected value.
"""
import sys
import sympy as sp

results = []


def chk(name, got, want):
    ok = (got == want)
    results.append(ok)
    print("%-4s %-78s got=%s" % ("PASS" if ok else "FAIL", name, got))


# ------------------------------------------------------------------ C1
q1, q2, h1, h2, eps = sp.symbols('q1 q2 h1 h2 eps')
a = sp.symbols('a0:12')
# a generic quartic action in two variables (enough to carry a residual)
S = (a[0]*q1 + a[1]*q2 + a[2]*q1**2 + a[3]*q1*q2 + a[4]*q2**2 + a[5]*q1**3
     + a[6]*q1**2*q2 + a[7]*q2**3 + a[8]*q1**4 + a[9]*q1**2*q2**2 + a[10]*q2**4)
E = sp.Matrix([sp.diff(S, q1), sp.diff(S, q2)])          # equations of motion
K = sp.hessian(S, (q1, q2))                                # second variation
Sexp = sp.series(S.subs({q1: q1 + eps*h1, q2: q2 + eps*h2}), eps, 0, 3).removeO()
S2 = sp.expand(Sexp.subs(eps, 1))                          # keep O(h^2)
lin = sp.Matrix([sp.diff(S2, h1), sp.diff(S2, h2)])        # vary w.r.t. h
residual_form = sp.simplify(lin - (E + K*sp.Matrix([h1, h2])))
chk("C1a d/dh [S(q0+h) to O(h^2)] == E(q0) + K(q0) h  (identically)",
    residual_form == sp.zeros(2, 1), True)
# first variation of E=0 along h: E(q0+eps h) = E(q0) + eps K h + O(eps^2)
firstvar = sp.simplify(sp.Matrix([sp.diff(e.subs({q1: q1+eps*h1, q2: q2+eps*h2}), eps)
                                  for e in E]).subs(eps, 0) - K*sp.Matrix([h1, h2]))
chk("C1b d/deps E(q0+eps h)|0 == K(q0) h  (the operator of AMM (3.4))",
    firstvar == sp.zeros(2, 1), True)
# the stationarity equation reduces to K h = 0 iff E(q0) = 0: exhibit a q0 with
# E != 0 for generic coefficients, so the zeroth-order source is present there
Ez = E.subs({q1: 1, q2: 0})
chk("C1c off a solution the zeroth-order source E(q0) is not identically 0",
    Ez != sp.zeros(2, 1), True)

# ------------------------------------------------------------------ C2
t, r, th, ph = sp.symbols('t r theta phi')
M, c, Lam = sp.symbols('M c Lambda')
X = [t, r, th, ph]
xr = sp.Function('x')(r)


def christoffel(g, ginv):
    n = 4
    return [[[sum(ginv[i, l]*(sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j])
                              - sp.diff(g[j, k], X[l])) for l in range(n))/2
              for k in range(n)] for j in range(n)] for i in range(n)]


def ricci(g):
    ginv = g.inv()
    G = christoffel(g, ginv)
    n = 4
    R = sp.zeros(4, 4)
    for i in range(n):
        for j in range(n):
            R[i, j] = sum(sp.diff(G[k][i][j], X[k]) - sp.diff(G[k][i][k], X[j])
                          + sum(G[k][k][l]*G[l][i][j] - G[k][j][l]*G[l][i][k]
                                for l in range(n)) for k in range(n))
    return R, ginv


def einstein_lambda(g):
    R, ginv = ricci(g)
    Rs = sum(ginv[i, j]*R[i, j] for i in range(4) for j in range(4))
    return (R - Rs*g/2 + Lam*g)


def lie_metric(g, V):
    return sp.Matrix(4, 4, lambda a_, b_: sum(V[k]*sp.diff(g[a_, b_], X[k])
                                              + g[k, b_]*sp.diff(V[k], X[a_])
                                              + g[a_, k]*sp.diff(V[k], X[b_])
                                              for k in range(4)))


def lie_tensor(T, V):     # covariant rank-2
    return lie_metric(T, V)


f = 1 - 2*M/r - c*r
g0 = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
V = [0, xr, 0, 0]
hgauge = lie_metric(g0, V)
E0 = einstein_lambda(g0).applyfunc(sp.simplify)
geps = g0 + eps*hgauge
Eeps = einstein_lambda(geps)
Eprime = Eeps.applyfunc(lambda e: sp.simplify(sp.diff(e, eps).subs(eps, 0)))
LXE = lie_tensor(E0, V).applyfunc(sp.simplify)
ident = (Eprime - LXE).applyfunc(sp.simplify)
chk("C2a identity E'[g](L_X g) == L_X E[g] for all M, c, Lambda, x(r)",
    ident == sp.zeros(4, 4), True)
chk("C2b background is a solution of G + Lambda g = 0 at c = 0, Lambda = 0",
    E0.subs({c: 0, Lam: 0}).applyfunc(sp.simplify) == sp.zeros(4, 4), True)
chk("C2c ... so pure gauge solves the homogeneous linearised eq. at c=0, Lambda=0",
    Eprime.subs({c: 0, Lam: 0}).applyfunc(sp.simplify) == sp.zeros(4, 4), True)
off = Eprime.subs({Lam: 0}).applyfunc(sp.simplify)
chk("C2d off a solution (c != 0): E'[g](L_X g) != 0 for generic x(r)",
    off != sp.zeros(4, 4), True)
# concrete witness component, x(r) = r, c = 1, M = 0: not a solution, gauge fails
wit = sp.simplify(off.subs(xr, r).doit().subs({c: 1, M: 0}))
nz = [(i, j, wit[i, j]) for i in range(4) for j in range(4) if wit[i, j] != 0]
chk("C2e witness x(r)=r, c=1, M=0: some component of E'[g](L_X g) is nonzero",
    len(nz) > 0, True)
print("     witness nonzero components (i, j, value):", nz[:4])

# ------------------------------------------------------------------ C3, C4
tt = sp.Symbol('t', nonnegative=True)
d = sp.Function('d')
y = sp.Symbol('y')
# W1 logistic at x0 = 1/2
f1 = y*(1 - y)
X1 = 1/(1 + sp.exp(-tt))
chk("C3a W1 exact flow x=1/(1+e^-t) solves x'=x(1-x), x(0)=1/2, bounded (-> 1)",
    (sp.simplify(sp.diff(X1, tt) - f1.subs(y, X1)) == 0, X1.subs(tt, 0),
     sp.limit(X1, tt, sp.oo)), (True, sp.Rational(1, 2), 1))
fp1 = sp.diff(f1, y).subs(y, sp.Rational(1, 2))
r1 = f1.subs(y, sp.Rational(1, 2))
s1 = sp.dsolve(sp.Eq(d(tt).diff(tt), fp1*d(tt) + r1), d(tt), ics={d(0): 0}).rhs
chk("C3b W1 residual-kept linearisation: residual 1/4, d = t/4 unbounded",
    (r1, sp.simplify(s1 - tt/4), sp.limit(s1, tt, sp.oo)), (sp.Rational(1, 4), 0, sp.oo))
# W2 x' = 1/(1+x^2), x0 = 1
f2 = 1/(1 + y**2)
xs = sp.Symbol('xs', positive=True)
T_of_x = sp.integrate(1/f2.subs(y, xs), (xs, 1, xs))      # t as function of x
chk("C3c W2 exact flow: t(x) = x + x^3/3 - 4/3, t -> oo only as x -> oo (unbounded)",
    (sp.simplify(T_of_x - (xs + xs**3/3 - sp.Rational(4, 3))), sp.limit(T_of_x, xs, sp.oo),
     bool(f2.subs(y, xs).is_positive)), (0, sp.oo, True))
fp2 = sp.diff(f2, y).subs(y, 1)
r2 = f2.subs(y, 1)
sk = sp.dsolve(sp.Eq(d(tt).diff(tt), fp2*d(tt) + r2), d(tt), ics={d(0): 0}).rhs
sd = sp.dsolve(sp.Eq(d(tt).diff(tt), fp2*d(tt)), d(tt), ics={d(0): 1}).rhs
chk("C3d W2 linearisations: f'(1) = -1/2; kept -> 1 (bounded), dropped -> 0",
    (fp2, sp.limit(sk, tt, sp.oo), sp.limit(sd, tt, sp.oo)), (-sp.Rational(1, 2), 1, 0))
chk("C4  control: W1 equilibria 0 (f'=1 unstable) and 1 (f'=-1 stable) match flow",
    (f1.subs(y, 0), f1.subs(y, 1), sp.diff(f1, y).subs(y, 0), sp.diff(f1, y).subs(y, 1)),
    (0, 0, 1, -1))

print("\n%d/%d checks pass" % (sum(results), len(results)))
sys.exit(0 if all(results) else 1)
