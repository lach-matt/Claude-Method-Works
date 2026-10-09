"""Independent check (not reusing modelc.py): Israel junction for a static plane r=R in
ds^2 = -f dt^2 + dr^2/f + r^2 dOmega_k^2 (5D), plus a second route via the moving-plane
energy equation, the RS control and its mutation, flat/mirrored/k=1/k=-1 closed forms.

Route 1: K_ab = -Gamma^lam_ab n_lam computed from the metric's Christoffels (sympy, generic f).
Route 2: F(R,X) = sum_j eps_j sqrt(f_j(R)+X) - lam R = 0 defines X = Rdot^2; static <=> X(R0)=0, X'(R0)=0.
Convention: S^a_b = -(1/kappa^2) sum_sides (K^a_b - delta K), normal pointing INTO each kept side.
eps = +1 'decaying' (kept side r<R, normal -d_r), eps = -1 'growing' (kept side r>R).
"""
import sympy as sp

t, r, th, ph, ps = sp.symbols('t r theta phi psi')
kk = sp.Symbol('k')          # slicing curvature (0, +1, -1)
F = sp.Function('f')

def christoffel(g, X):
    n = len(X); gi = g.inv()
    G = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                G[a][b][c] = sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                                       - sp.diff(g[b, c], X[d])) for d in range(n))/2)
    return G

# 3-space of constant curvature k:  dpsi^2 + S_k(psi)^2 (dth^2 + sin^2 th dph^2); use k=+1 form sin(psi),
# but only the r-components of Gamma matter and they are k-independent apart from gamma_ij; we check k=1, 0 explicitly
def K_mixed(Sk, s):
    """s=+1: normal along +r; returns K^t_t, K^psi_psi, K^th_th."""
    X = [t, r, ps, th, ph]
    g = sp.diag(-F(r), 1/F(r), r**2, r**2*Sk**2, r**2*Sk**2*sp.sin(th)**2)
    G = christoffel(g, X)
    n_low = [0, s/sp.sqrt(F(r)), 0, 0, 0]
    Kl = lambda a, b: -sum(G[l][a][b]*n_low[l] for l in range(5))
    return [sp.simplify(Kl(i, i)/g[i, i]) for i in (0, 2, 3)]

R = sp.Symbol('R', positive=True)
out = {}
for name, Sk in (('k=1', sp.sin(ps)), ('k=0', ps)):
    Kt, Kp, Kth = K_mixed(Sk, +1)
    out[name] = (sp.simplify(Kt - sp.diff(F(r), r)/(2*sp.sqrt(F(r)))), sp.simplify(Kp - sp.sqrt(F(r))/r),
                 sp.simplify(Kth - sp.sqrt(F(r))/r))
print("Route 1, K^t_t - f'/(2 sqrt f), K^psi_psi - sqrt f/r, K^th_th - sqrt f/r  (normal +r):", out)

# junction from route 1 with general f_j, eps_j, per-sheet
def junction(fs, epss, Rv):
    """returns (rho, p) * kappa^2 from sum over sides of -(K - delta K), normal into kept side: s = -eps."""
    rho = 0; p = 0
    for f, eps in zip(fs, epss):
        s = -eps
        Kt = s*sp.diff(f, r)/(2*sp.sqrt(f)); Ka = s*sp.sqrt(f)/r
        Ktr = Kt + 3*Ka
        St = -(Kt - Ktr); Sa = -(Ka - Ktr)    # kappa^2 S^a_b
        rho += -St; p += Sa
    return sp.simplify(rho.subs(r, Rv)), sp.simplify(p.subs(r, Rv))

mu, ell, lam, X = sp.symbols('mu ell lam X', positive=True)
def fSAdS(k, m, l): return k + r**2/l**2 - m/r**2

# generic check of TENSION and BALANCE forms
for k in (0, 1, -1):
    for e1 in (1, -1):
        for e2 in (1, -1):
            m1, m2, l1, l2 = sp.symbols('m1 m2 l1 l2', positive=True)
            f1, f2 = fSAdS(k, m1, l1), fSAdS(k, m2, l2)
            rho, p = junction([f1, f2], [e1, e2], R)
            # claimed: kappa^2 rho = (3/R) sum eps sqrt f ; kappa^2 (rho+p) = (1/R) sum eps (k-2m/R^2)/sqrt f
            c1 = sp.simplify(rho - 3/R*(e1*sp.sqrt(f1.subs(r, R)) + e2*sp.sqrt(f2.subs(r, R))))
            c2 = sp.simplify(rho + p - (e1*(k - 2*m1/R**2)/sp.sqrt(f1.subs(r, R))
                                        + e2*(k - 2*m2/R**2)/sp.sqrt(f2.subs(r, R)))/R)
            assert c1 == 0 and c2 == 0, (k, e1, e2, c1, c2)
print("Route 1: TENSION lam R = sum eps sqrt f and kappa^2(rho+p) = B/R hold for k in {0,1,-1}, all eps: OK")

# Route 2: energy equation
for k in (0, 1, -1):
    for e1 in (1, -1):
        for e2 in (1, -1):
            m1, m2, l1, l2 = sp.symbols('m1 m2 l1 l2', positive=True)
            f1, f2 = fSAdS(k, m1, l1).subs(r, R), fSAdS(k, m2, l2).subs(r, R)
            Fn = e1*sp.sqrt(f1 + X) + e2*sp.sqrt(f2 + X) - lam*R
            # implicit: dX/dR = -F_R/F_X ; static: F=0 at X=0 and F_R=0 at X=0
            FR = sp.diff(Fn, R).subs(X, 0)
            lam_static = (e1*sp.sqrt(f1) + e2*sp.sqrt(f2))/R
            Bclaim = e1*(k - 2*m1/R**2)/sp.sqrt(f1) + e2*(k - 2*m2/R**2)/sp.sqrt(f2)
            # F_R at lam_static should be -(1/(2R)) * B ... check proportionality
            ratio = sp.simplify(FR.subs(lam, lam_static)/Bclaim)
            assert sp.simplify(ratio + 1/R) == 0, (k, e1, e2, ratio)
print("Route 2: d/dR of energy equation at X=0 and lam=lam_static equals -B/R: OK (static <=> B=0)")

# RS control
fA = r**2/ell**2
rho, p = junction([fA, fA], [1, 1], R)
print("RS control (k=0, mu=0, both decaying): kappa^2 rho =", rho, " kappa^2(rho+p) =", sp.simplify(rho+p))
rho, p = junction([fA, fA], [1, -1], R)
print("Mutation (one side flipped): kappa^2 rho =", rho, " kappa^2(rho+p) =", sp.simplify(rho+p))

# Flat with bridge
fs = r**2/ell**2 - mu/r**2
rho, p = junction([fs, fs], [1, 1], R)
print("Flat mirrored bridge side: kappa^2(rho+p) =", sp.factor(sp.simplify(rho+p)))
rho, p = junction([fs, fA], [1, 1], R)
print("Flat two-sided (outer AdS decaying): kappa^2(rho+p) =", sp.factor(sp.simplify(rho+p)))
rho, p = junction([fs, fA], [1, -1], R)
print("Flat two-sided (outer AdS growing): kappa^2(rho+p) =", sp.factor(sp.simplify(rho+p)))
# Rdot^2 at exact RS tension, mirrored
Xs = sp.solve(sp.Eq(2*sp.sqrt(fs.subs(r, R) + X), 2*R/ell), X)
print("Flat mirrored at RS tension lam=2/ell: Rdot^2 =", Xs)
# acceleration from rest, mirrored: kappa^2(rho+p) for moving plane = sum eps[sqrt(f+X)/R - (Rdd + f'/2)/sqrt(f+X)]
Rdd = sp.Symbol('Rdd')
acc = sp.solve(sp.Eq(2*(sp.sqrt(fs.subs(r, R))/R - (Rdd + sp.diff(fs, r).subs(r, R)/2)/sp.sqrt(fs.subs(r, R))), 0), Rdd)
print("Flat mirrored, momentarily at rest, pure tension: Rddot =", [sp.simplify(a) for a in acc])

# Mirrored any k
for k in (1, 0, -1):
    f = fSAdS(k, mu, ell).subs(r, R)
    B = 2*(k - 2*mu/R**2)/sp.sqrt(f)
    print(f"Mirrored k={k}: B = {sp.simplify(B)}")
f1m = fSAdS(1, R**2/2, ell).subs(r, R)
print("Mirrored k=1 at mu=R^2/2: (lam/2)^2 =", sp.expand(f1m/R**2))
lamv = 2*sp.sqrt(f1m)/R
V = fSAdS(1, mu, ell) - (lamv*r/2)**2
print("V''(R) at mu=R^2/2:", sp.simplify(sp.diff(V, r, 2).subs(mu, R**2/2).subs(r, R)))
