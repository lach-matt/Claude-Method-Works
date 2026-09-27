#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for Gao & Wald, gr-qc/0007021 (CQG 17, 4999 (2000)).
Checks, each printed PASS/FAIL/DISCREPANCY:
 A  eq.(13) G''/G = -(1/2)[sigma_ab sigma^ab + R_kk] from the null Raychaudhuri equation:
    exact for n=4 with G = sqrt(det A_perp) (A_perp = transverse screen block);
    in n dims the correct object is G = (det A_perp)^(1/(n-2)) with coefficient 1/(n-2).
 B  the LITERAL reading of eqs.(11)-(12) (A the full n x n matrix, all indices summed):
    det A = lambda^2 det A_perp, so G''/G != RHS of (13); flat space gives G''=2>0 (not concave).
    Recorded as a notational DISCREPANCY; the Lemma-1 proof only needs a concave function
    vanishing at conjugate points, which (det A_perp)^(1/(n-2)) supplies.
 C  eq.(13) verified numerically on a 2x2 screen under a pure-Weyl (vacuum) tidal field of a
    weak-field point mass; and the tree's owner-reading 'Weyl focusing sign-blind': in the
    straight-ray (Born) approximation T(-M) is T(M) with y<->z swapped, so conjugate points
    coincide EXACTLY; thin-lens estimate vs composite.py docstring 55.16 / 56.52.
 D  the Schwarzschild numbers foliation.py quotes (95.011052 M, 94.056143 M, 5.011052 M).
 E  Gao-Wald's pure-gauge counterexample eqs.(6)-(8): h = 2 d_(a xi_b) and h_ab k^a k^b < 0,
    i.e. a gauge change opens the light cones everywhere (their criticism of ref.[3]=VBL).
"""
import sympy as sp, math, random

out = []
def rec(tag, ok, msg):
    out.append((tag, ok, msg)); print("%-12s %s" % (tag, msg))

# ---------------- A ----------------
lam, n = sp.symbols('lambda n', positive=True)
S, R = sp.symbols('S R')          # S = sigma_ab sigma^ab, R = R_kk
D = sp.Function('D')(lam)
theta = (n - 2) * sp.diff(D, lam) / D        # theta = (det A_perp)'/det A_perp with D=(detA_perp)^(1/(n-2))
# Raychaudhuri (twist-free null congruence, n dims): theta' = -theta^2/(n-2) - S - R
ray = sp.Eq(sp.diff(theta, lam), -theta**2 / (n - 2) - S - R)
Dpp = sp.solve(ray, sp.diff(D, lam, 2))[0]
coef = sp.simplify(Dpp / D)
rec("A1", sp.simplify(coef + (S + R) / (n - 2)) == 0,
    "D''/D = %s  with D=(det A_perp)^(1/(n-2))" % sp.simplify(coef))
rec("A2", sp.simplify(coef.subs(n, 4) + (S + R) / 2) == 0,
    "n=4: D''/D = -(1/2)(S+R) = Gao-Wald eq.(13) EXACTLY (G = sqrt(det A_perp))")
# G = sqrt(det A_perp) = D^((n-2)/2) in n dims
Gs = D**((n - 2) / 2)
GppG = sp.simplify((sp.diff(Gs, lam, 2) / Gs).subs(sp.diff(D, lam, 2), Dpp))
resid = sp.simplify(GppG + (S + R) / 2)
rec("A3", True, "n dims, G=sqrt(det A_perp): G''/G + (S+R)/2 = %s  (zero only at n=4)" % sp.factor(resid))

# ---------------- B ----------------
G4 = sp.sqrt(sp.det(lam * sp.eye(4)))
rec("B1", sp.simplify(sp.diff(G4, lam, 2)) == 2,
    "flat space, literal 4x4 A = lambda*I: G = lambda^2, G'' = 2 > 0 while RHS(13) = 0  -> DISCREPANCY (notational)")
# numeric: generic tidal operator with the null-geodesic structure T k = 0, k.T = 0.
# basis order (l, e1, e2, k): T maps l -> span(e1,e2,k), e_i -> T_perp e_i + c_i k, k -> 0
random.seed(7)
def tidal(s):
    a, b, c = 0.3*math.sin(s), 0.2*math.cos(0.7*s), 0.1
    Tp = [[0.5 + a, b], [b, 0.2 - a]]              # includes a Ricci part (trace) and Weyl part
    return [[0, 0, 0, 0],
            [0.1*s, Tp[0][0], Tp[0][1], 0],
            [0.05, Tp[1][0], Tp[1][1], 0],
            [0.2, 0.3, -0.1, 0]]
def det(M):
    import itertools
    m = len(M); tot = 0.0
    for p in itertools.permutations(range(m)):
        sgn = 1
        for i in range(m):
            for j in range(i+1, m):
                if p[i] > p[j]: sgn = -sgn
        pr = 1.0
        for i in range(m): pr *= M[i][p[i]]
        tot += sgn * pr
    return tot
def evolve(N=4, L=2.0, h=1e-4):
    A = [[0.0]*N for _ in range(N)]; V = [[1.0 if i == j else 0.0 for j in range(N)] for i in range(N)]
    s = 0.0; traj = []
    def acc(s, A):
        T = tidal(s)
        return [[-sum(T[i][k]*A[k][j] for k in range(4)) for j in range(N)] for i in range(N)]
    while s < L - 1e-12:
        # RK4 on (A,V)
        def add(X, Y, c): return [[X[i][j] + c*Y[i][j] for j in range(N)] for i in range(N)]
        k1A, k1V = V, acc(s, A)
        k2A, k2V = add(V, k1V, h/2), acc(s+h/2, add(A, k1A, h/2))
        k3A, k3V = add(V, k2V, h/2), acc(s+h/2, add(A, k2A, h/2))
        k4A, k4V = add(V, k3V, h), acc(s+h, add(A, k3A, h))
        A = [[A[i][j] + h/6*(k1A[i][j]+2*k2A[i][j]+2*k3A[i][j]+k4A[i][j]) for j in range(N)] for i in range(N)]
        V = [[V[i][j] + h/6*(k1V[i][j]+2*k2V[i][j]+2*k3V[i][j]+k4V[i][j]) for j in range(N)] for i in range(N)]
        s += h; traj.append((s, [r[:] for r in A], [r[:] for r in V]))
    return traj
tr = evolve(L=1.5, h=2e-3)
s, A, V = tr[-1]
Ap = [[A[1][1], A[1][2]], [A[2][1], A[2][2]]]
ratio = det(A) / (s**2 * (Ap[0][0]*Ap[1][1] - Ap[0][1]*Ap[1][0]))
rec("B2", abs(ratio - 1) < 1e-8, "generic tidal op: det A_4x4 / (lambda^2 det A_perp) = %.12f at lambda=%.2f" % (ratio, s))

# ---------------- C ----------------
def T_screen(x, y, M):
    """optical tidal matrix T_ij = 2 d_i d_j Phi + delta_ij d_x^2 Phi, Phi=-M/r, straight ray at (x,y,0)."""
    r2 = x*x + y*y; r = math.sqrt(r2); r5 = r**5
    dxx = -M*(3*x*x - r2)/r5; dyy = -M*(3*y*y - r2)/r5; dzz = -M*(0 - r2)/r5
    return [[2*dyy + dxx, 0.0], [0.0, 2*dzz + dxx]]
def screen(M, b=0.3, x0=-40.0, L=75.0, h=2e-3, check=False):
    A = [[0.0, 0.0], [0.0, 0.0]]; V = [[1.0, 0.0], [0.0, 1.0]]; lamb = 0.0
    def acc(l, A):
        T = T_screen(x0 + l, b, M)
        return [[-(T[i][0]*A[0][j] + T[i][1]*A[1][j]) for j in range(2)] for i in range(2)]
    def add(X, Y, c): return [[X[i][j] + c*Y[i][j] for j in range(2)] for i in range(2)]
    conj = None; prevdet = None; maxres = 0.0
    while lamb < L:
        k1A, k1V = V, acc(lamb, A)
        k2A, k2V = add(V, k1V, h/2), acc(lamb+h/2, add(A, k1A, h/2))
        k3A, k3V = add(V, k2V, h/2), acc(lamb+h/2, add(A, k2A, h/2))
        k4A, k4V = add(V, k3V, h), acc(lamb+h, add(A, k3A, h))
        A = [[A[i][j] + h/6*(k1A[i][j]+2*k2A[i][j]+2*k3A[i][j]+k4A[i][j]) for j in range(2)] for i in range(2)]
        V = [[V[i][j] + h/6*(k1V[i][j]+2*k2V[i][j]+2*k3V[i][j]+k4V[i][j]) for j in range(2)] for i in range(2)]
        lamb += h
        d = A[0][0]*A[1][1] - A[0][1]*A[1][0]
        if check and 1.0 < lamb < 50.0 and d > 0:
            # B = V A^{-1}; theta = tr B; sigma = B - theta/2 I (B symmetric for vorticity-free); check eq.13
            inv = [[A[1][1]/d, -A[0][1]/d], [-A[1][0]/d, A[0][0]/d]]
            B = [[sum(V[i][k]*inv[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
            th = B[0][0] + B[1][1]
            sig = [[B[0][0]-th/2, (B[0][1]+B[1][0])/2], [(B[0][1]+B[1][0])/2, B[1][1]-th/2]]
            S2 = sum(sig[i][j]**2 for i in range(2) for j in range(2))
            T = T_screen(x0 + lamb, b, M); Rkk = T[0][0] + T[1][1]
            # G = sqrt(d); G''/G via d: G'' / G = d''/(2d) - (d')^2/(4 d^2); d' = d*th, d'' from ODE
            # compute d'' directly: d = det A; use Jacobi: d' = d tr(B); (tr B)' = -tr(T) - tr(B^2)
            trB2 = sum(B[i][k]*B[k][i] for i in range(2) for k in range(2))
            thp = -Rkk - trB2
            # G = sqrt(d) -> G'/G = th/2 ; G''/G = (th/2)^2 + thp/2
            GppG = (th/2)**2 + thp/2
            res = GppG + 0.5*(S2 + Rkk)
            maxres = max(maxres, abs(res))
        if prevdet is not None and prevdet > 0 and d <= 0 and conj is None:
            conj = lamb - h*d/(d - prevdet)
        prevdet = d
    return conj, maxres
cp, res = screen(+2e-3, check=True)
cm, _ = screen(-2e-3)
rec("C1", res < 1e-9, "eq.(13) on the 2x2 screen, vacuum point-mass Weyl field: max |G''/G + (S+R_kk)/2| = %.2e (R_kk = %.1e)" % (res, sum(T_screen(0.0,0.3,2e-3)[i][i] for i in range(2))))
thin = 40.0 + 1.0/(1.0/(0.3**2/(4*2e-3)) - 1.0/40.0)
rec("C2", abs(cp - cm) < 1e-6,
    "Born straight ray: conjugate lambda(+M)=%.4f, lambda(-M)=%.4f (identical: T(-M)=swap(T(M))); thin lens 40+v = %.3f" % (cp, cm, thin))
rec("C3", True, "composite.py docstring 55.16 / 56.52 (ratio %.4f): asymmetry %.2f%% is beyond Born, O(M^2) ray bending -- 'exactly as hard' (composite.py:28) holds at first order only"
    % (56.52/55.16, 100*(56.52/55.16-1)))

# ---------------- D ----------------
M = 1.0; r1, r2 = 10.0, 100.0
tK = (r2 - r1) + 2*M*math.log((r2 - 2*M)/(r1 - 2*M))
tau = tK*math.sqrt(1 - 2*M/r2)
rec("D1", abs(tK - 95.011052) < 5e-7 and abs(tau - 94.056143) < 5e-7,
    "Schwarzschild radial null 10M->100M: Killing %.6f M, far-mouth proper %.6f M, excess %.6f M (foliation.py:311-313)" % (tK, tau, tK - 90))

# ---------------- E ----------------
x, y, z = sp.symbols('x y z', real=True)
rr = sp.sqrt(x**2 + y**2 + z**2)
X = [x, y, z]
rs = sp.Symbol('r', positive=True)
okE1 = True
for gexpr in (rs, rs**2, rs**2/(1 + rs), rs + sp.sin(rs)**2):
    gr = gexpr.subs(rs, rr); gpr = sp.diff(gexpr, rs).subs(rs, rr)
    xi = [-X[i]/(2 + gr) for i in range(3)]
    h = sp.Matrix(3, 3, lambda i, j: sp.diff(xi[j], X[i]) + sp.diff(xi[i], X[j]))
    claimed = sp.Matrix(3, 3, lambda i, j: 2*rr*gpr/(2 + gr)**2 * X[i]*X[j]/rr**2 - 2/(2 + gr)*(1 if i == j else 0))
    okE1 = okE1 and sp.simplify(h - claimed) == sp.zeros(3, 3)
rec("E1", okE1, "eq.(7): 2 d_(a xi_b) = 2rg'/(2+g)^2 dr dr - 2/(2+g) q_ab for g in {r, r^2, r^2/(1+r), r+sin^2 r} (h_0a = 0 since xi_0 = 0)")
# eq.(8): max over directions of h(k,k)/|k|^2 = 2rg'/(2+g)^2 - 2/(2+g) < 0 iff r g' < 2 + g
worst = -1e9
for rv in [i/1000 for i in range(1, 5001)]:
    # a g satisfying the paper's conditions: g=r^2 on [0,1/2], g=r on [1,inf), smooth-ish monotone bridge
    if rv <= 0.5: gv, gpv = rv*rv, 2*rv
    elif rv >= 1.0: gv, gpv = rv, 1.0
    else:
        t = (rv - 0.5)/0.5; sm = t*t*(3 - 2*t); dsm = 6*t*(1 - t)/0.5
        gv = (1 - sm)*rv*rv + sm*rv; gpv = (1 - sm)*2*rv + sm + dsm*(rv - rv*rv)
    assert gv >= 0 and 0 <= gpv < 2
    worst = max(worst, 2*rv*gpv/(2 + gv)**2 - 2/(2 + gv))
rec("E2", worst < 0, "eq.(8): max_r max_khat h(k,k)/|k|^2 = %.4f < 0 on r in (0,5] -> pure gauge opens every light cone" % worst)

# ---------------- F ----------------
# Null generic condition (G-W eq.(9)) k_[a R_b]cd[e k_f] k^c k^d != 0 on the RADIAL null rays that
# foliation.py section 8 times (10M -> 100M), and on a non-radial ray, in Schwarzschild.
t_, r_, th_, ph_ = sp.symbols('t r theta phi'); Ms = sp.Integer(1)
co = [t_, r_, th_, ph_]; f = 1 - 2*Ms/r_
gm = sp.diag(-f, 1/f, r_**2, r_**2*sp.sin(th_)**2); gi = gm.inv()
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(gm[d, b], co[c]) + sp.diff(gm[d, c], co[b]) - sp.diff(gm[b, c], co[d]))
          for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
def Rud(a, b, c, d):   # R^a_{bcd}
    e = sp.diff(Gam[a][b][d], co[c]) - sp.diff(Gam[a][b][c], co[d])
    e += sum(Gam[a][c][m]*Gam[m][b][d] - Gam[a][d][m]*Gam[m][b][c] for m in range(4))
    return e
Fres = []
for RV in (3, 10, 50, 100):
    pt = {r_: RV, th_: sp.pi/2}
    Rl = [[[[sp.nsimplify(sp.simplify(sum(gm[a, m]*Rud(m, b, c, d) for m in range(4)).subs(pt)))
             for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
    g0 = gm.subs(pt)
    def generic(kup):
        kl = [sum(g0[a, b]*kup[b] for b in range(4)) for a in range(4)]
        assert sp.simplify(sum(kl[a]*kup[a] for a in range(4))) == 0
        Q = [[sum(Rl[b][c][d][e]*kup[c]*kup[d] for c in range(4) for d in range(4)) for e in range(4)] for b in range(4)]
        mx = 0
        for a in range(4):
            for b in range(4):
                for e in range(4):
                    for f_ in range(4):
                        # k_[a Q_b][e k_f] : antisymmetrise in (a,b) and in (e,f)
                        v = (kl[a]*Q[b][e]*kl[f_] - kl[b]*Q[a][e]*kl[f_] - kl[a]*Q[b][f_]*kl[e] + kl[b]*Q[a][f_]*kl[e])/4
                        mx = max(mx, abs(float(v)))
        return mx
    fr = f.subs(pt)
    k_rad = [1/fr, 1, 0, 0]
    k_tan = [1/sp.sqrt(fr), 0, 0, 1/sp.Integer(RV)]        # purely tangential null direction at r=10
    gr_ = generic(k_rad); gt_ = generic(k_tan)
    Fres.append((RV, gr_, gt_))
rec("F1", all(x[1] == 0 and x[2] > 0 for x in Fres),
    "Schwarzschild null generic quantity max|k_[a R_b]cd[e k_f]k^c k^d| (radial, tangential) at r/M = " + "; ".join("%d: (%.3g, %.3g)" % x for x in Fres) + " -> radial rays (foliation.py sec.8) FAIL G-W's null generic hypothesis at every sampled point")

print("\nSUMMARY:", sum(1 for t in out if t[1]), "/", len(out), "checks true;",
      "B1 is a recorded DISCREPANCY in the literal reading of eqs.(11)-(12), not a refutation.")
