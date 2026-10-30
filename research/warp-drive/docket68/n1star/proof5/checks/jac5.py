# Check of Part V Proposition 2.3: linear charge fluxes of the 15 linearisations of the Myers-Perry family
# (Kerr-Schild form, III.B Definition 3.2) at Tangherlini, n = 4. Numeric quadrature on S^3 at large radius.
import sympy as sp, numpy as np, itertools
t = sp.Symbol('t'); X = sp.symbols('x1:5'); mu = sp.Symbol('mu', positive=True)
n = 4
r = sp.sqrt(sum(xi**2 for xi in X)); xh = [xi / r for xi in X]
H = mu / r**2
# spacetime coords (t, x1..x4); base g = eta + H k k, k = dt + dr
k = [1] + xh
eta = sp.diag(-1, 1, 1, 1, 1)
co = [t] + list(X)
G0 = sp.Matrix(5, 5, lambda a, b: eta[a, b] + H * k[a] * k[b])
def data_lin(dG):
    """first-order data variation (dg, dK) on t = 0, given dG (5x5, may depend on t)"""
    g = sp.Matrix(4, 4, lambda i, j: G0[i+1, j+1]); gi = sp.eye(4) - (H / (1 + H)) * sp.Matrix(4, 4, lambda i, j: xh[i]*xh[j])
    beta = [G0[0, i+1] for i in range(4)]; betau = [sum(gi[i, j]*beta[j] for j in range(4)) for i in range(4)]
    N = 1 / sp.sqrt(1 + H)
    Gam = [[[sum(gi[l, m]*(sp.diff(g[j, m], X[i]) + sp.diff(g[i, m], X[j]) - sp.diff(g[i, j], X[m])) for m in range(4))/2
             for j in range(4)] for i in range(4)] for l in range(4)]
    Dbeta = sp.Matrix(4, 4, lambda i, j: sp.diff(beta[j], X[i]) - sum(Gam[l][i][j]*beta[l] for l in range(4)))
    K0 = sp.Matrix(4, 4, lambda i, j: -(Dbeta[i, j] + Dbeta[j, i]) / (2*N))
    dGt0 = dG.subs(t, 0)
    dg = sp.Matrix(4, 4, lambda i, j: dGt0[i+1, j+1]); dbeta = [dGt0[0, i+1] for i in range(4)]
    dtg = sp.Matrix(4, 4, lambda i, j: sp.diff(dG[i+1, j+1], t).subs(t, 0))
    dN = (-dGt0[0, 0] + 2*sum(betau[i]*dbeta[i] for i in range(4)) - sum(betau[i]*betau[j]*dg[i, j] for i in range(4) for j in range(4))) / (2*N)
    dGl = [[[ (sp.diff(dg[j, m], X[i]) + sp.diff(dg[i, m], X[j]) - sp.diff(dg[i, j], X[m]))/2 for m in range(4)] for j in range(4)] for i in range(4)]
    dGb = sp.Matrix(4, 4, lambda i, j: sum(betau[m]*dGl[i][j][m] for m in range(4))
                    - sum(betau[a]*dg[a, b]*Gam[b][i][j] for a in range(4) for b in range(4)))
    dDb = sp.Matrix(4, 4, lambda i, j: sp.diff(dbeta[j], X[i]) - sum(Gam[l][i][j]*dbeta[l] for l in range(4)) - dGb[i, j])
    dK = sp.Matrix(4, 4, lambda i, j: -dN/N*K0[i, j] + (dtg[i, j] - dDb[i, j] - dDb[j, i]) / (2*N))
    return dg, dK
def Lie(Z, G):
    return sp.Matrix(5, 5, lambda a, b: sum(Z[c]*sp.diff(G[a, b], co[c]) + G[c, b]*sp.diff(Z[c], co[a]) + G[a, c]*sp.diff(Z[c], co[b]) for c in range(5)))
dirs = []
dirs.append(('mu', sp.diff(G0, mu)))
for a, b in itertools.combinations(range(4), 2):
    A = sp.zeros(4); A[a, b] = 1; A[b, a] = -1
    Ax = [sum(A[i, j]*X[j] for j in range(4)) for i in range(4)]
    al = [0] + [Ax[i] / r**2 for i in range(4)]
    dG = sp.Matrix(5, 5, lambda p, q: H*(k[p]*al[q] + al[p]*k[q]))
    dirs.append(('A%d%d' % (a+1, b+1), dG))
for kk in range(4):
    Z = [X[kk]] + [t if i == kk else 0 for i in range(4)]
    dirs.append(('w%d' % (kk+1), Lie(Z, G0)))
for kk in range(4):
    Z = [0] + [1 if i == kk else 0 for i in range(4)]
    dirs.append(('c%d' % (kk+1), Lie(Z, G0)))
# KIDs (Y, N): N=1; Y=e_l; Y = W_ab x; N = x^l
kids = [('E', [0]*4, 1)]
for l in range(4): kids.append(('P%d' % (l+1), [1 if i == l else 0 for i in range(4)], 0))
for a, b in itertools.combinations(range(4), 2):
    W = sp.zeros(4); W[a, b] = 1; W[b, a] = -1
    kids.append(('J%d%d' % (a+1, b+1), [sum(W[i, j]*X[j] for j in range(4)) for i in range(4)], 0))
for l in range(4): kids.append(('C%d' % (l+1), [0]*4, X[l]))
# hyperspherical quadrature on S^3
def quad(m=24):
    gp, gw = np.polynomial.legendre.leggauss(m)
    psi = (gp + 1) * np.pi / 2; wpsi = gw * np.pi / 2
    th = (gp + 1) * np.pi / 2; wth = gw * np.pi / 2
    ph = np.arange(2*m) * np.pi / m; wph = np.full(2*m, np.pi / m)
    P, T, F = np.meshgrid(psi, th, ph, indexing='ij'); W = np.einsum('i,j,k->ijk', wpsi, wth, wph)
    W = W * np.sin(P)**2 * np.sin(T)
    om = np.stack([np.cos(P), np.sin(P)*np.cos(T), np.sin(P)*np.sin(T)*np.cos(F), np.sin(P)*np.sin(T)*np.sin(F)])
    return om.reshape(4, -1), W.reshape(-1)
om, Wq = quad()
mu0 = 1.0
res = {}
for dn, dG in dirs:
    dg, dK = data_lin(dG)
    trh = sum(dg[i, i] for i in range(4)); trK = sum(dK[i, i] for i in range(4))
    for kn, Y, Nf in kids:
        integ = 0
        for i in range(4):
            nu = X[i] / r
            integ += (Nf*(sum(sp.diff(dg[i, j], X[j]) for j in range(4)) - sp.diff(trh, X[i]))
                      - (sum(sp.diff(Nf, X[j])*dg[i, j] for j in range(4)) - sp.diff(Nf, X[i])*trh)
                      - 2*(sum(Y[j]*dK[i, j] for j in range(4)) - Y[i]*trK)) * nu
        f = sp.lambdify((X, mu), integ, 'numpy')
        vals = []
        for rho in (2e3, 4e3):
            v = f(tuple(rho*om), mu0); vals.append(float(np.sum(v * Wq) * rho**3))
        if abs(vals[-1]) > 1e-6: res[(kn, dn)] = vals
for key, v in sorted(res.items()):
    print(key, ['%.6f' % x for x in v], ' /pi^2 = %.6f' % (v[-1] / np.pi**2))
