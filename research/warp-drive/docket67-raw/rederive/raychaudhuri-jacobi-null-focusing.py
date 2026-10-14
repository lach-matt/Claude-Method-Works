#!/usr/bin/env python3
"""
DOCKET 67 -- rederivation for key raychaudhuri-jacobi-null-focusing
(seatindex.py:14-15, 47-50: u'' = -q u, q = 4 pi T_kk, u(0) = 0, turn = next zero,
shear dropped).

Checks (each prints PASS/FAIL; exit 1 on any FAIL):
 S1  null Raychaudhuri (Kontou-Sanders 2003.01815 eq.17, n dims) with theta = (n-2) u'/u
     gives u'' = -(R_kk + sigma^2 - omega^2)/(n-2) u exactly; n = 4 -> the tree's 1/2.
 S2  Einstein eq (with Lambda, trace term) contracted on a null k: R_kk = 8 pi T_kk,
     for random T_ab and random null k (exact rationals) -> q = R_kk/2 = 4 pi T_kk (n=4);
     in n dims the coefficient is 8 pi/(n-2) (so 4 pi is 4D-specific).
 S3  full 2x2 Jacobi (optical tidal matrix = (q) I + W, W traceless = Weyl part), point data
     A(0)=0, A'(0)=I.  (a) W = 0: A stays u I and sqrt(det A) = u to integrator precision --
     the reduction is EXACT when the Weyl term vanishes; (b) W != 0: first zero of det A is
     never later than the Ricci-only first zero (Sturm comparison, 200 random profiles);
     (c) vacuum q = 0, W = diag(w,-w): conjugate point at pi/sqrt(w) while the scalar
     reduction has none -- Lyapunov necessity fails with shear (the tree already strikes it).
 S4  Gao-Wald eq.(13) along S3(b) trajectories: G''/G = -(sigma^2 + R_kk)/2 with G = sqrt det A,
     sigma^2 computed from the shear of B = A' A^-1 (residual).
 S5  normalisation: under k -> alpha k, lambda -> lambda/alpha, T_kk -> alpha^2 T_kk; the
     dimensionless q l^2 is invariant but the SI threshold T_kk >= pi c^4/(4 G l^2) is a
     statement in the frame where k^0 = 1 and l is measured (hidden hypothesis).
 S6  T_COEFF = pi c^4/(4G): value with CODATA 2018/2022 G; the docstring's 9.5054e43.
 S7  seatindex.seats() against analytic pi/sqrt(m) for constant q (imports the owner, read only).
 S8  neutron-star/nuclear comparison: T_kk = rho c^2 + p for k = (1, n) in the fluid frame;
     saturation energy density vs the tree's 1e35 Pa; crossing length l* for each.
"""
import math, random, sys, importlib.util
import sympy as sp

FAILS = []
def rep(tag, ok, msg):
    print("%-4s %s  %s" % (tag, "PASS" if ok else "FAIL", msg))
    if not ok:
        FAILS.append(tag)

# ---------------------------------------------------------------- S1
lam, n = sp.symbols('lambda n', positive=True)
u = sp.Function('u')(lam)
Rkk, sig2, om2 = sp.symbols('R_kk sigma2 omega2', real=True)
theta = (n - 2) * sp.diff(u, lam) / u
ray = sp.diff(theta, lam) - (-Rkk - sig2 + om2 - theta**2 / (n - 2))
upp = sp.solve(sp.Eq(ray, 0), sp.diff(u, lam, 2))[0]
target = -(Rkk + sig2 - om2) / (n - 2) * u
rep("S1", sp.simplify(upp - target) == 0 and sp.simplify(target.subs(n, 4) + (Rkk + sig2 - om2) / 2 * u) == 0,
    "u'' = %s ; n=4 -> -(R_kk+sigma^2-omega^2)/2 u" % sp.simplify(upp / u))

# ---------------------------------------------------------------- S2
random.seed(67)
def rnd(): return sp.Rational(random.randint(-9, 9), random.randint(1, 7))
ok2 = True
for dim in (4, 5, 6):
    eta = sp.diag(*([-1] + [1] * (dim - 1)))
    for trial in range(20):
        T = sp.Matrix(dim, dim, lambda i, j: 0)
        for i in range(dim):
            for j in range(i, dim):
                T[i, j] = T[j, i] = rnd()
        # null k: k = (|s|, s) with s rational unit vector via Pythagorean construction
        a, b = random.randint(1, 9), random.randint(1, 9)
        s = [sp.Rational(a*a - b*b, a*a + b*b), sp.Rational(2*a*b, a*a + b*b)] + [0] * (dim - 3)
        k = sp.Matrix([1] + s)
        assert (k.T * eta * k)[0] == 0
        Lam = rnd()
        Tr = sum((eta.inv() * T)[i, i] for i in range(dim))
        # Einstein: R_ab = 8 pi (T_ab - T g_ab/(n-2)) + 2 Lambda g_ab/(n-2)
        R = 8 * sp.pi * (T - Tr * eta / (dim - 2)) + 2 * Lam * eta / (dim - 2)
        Rk = sp.simplify((k.T * R * k)[0]); Tk = (k.T * T * k)[0]
        if sp.simplify(Rk - 8 * sp.pi * Tk) != 0:
            ok2 = False
        q = Rk / (dim - 2)
        if sp.simplify(q - 8 * sp.pi * Tk / (dim - 2)) != 0:
            ok2 = False
rep("S2", ok2, "R_kk = 8 pi T_kk in n = 4,5,6 (Lambda and trace drop); q = 8 pi T_kk/(n-2) -> 4 pi T_kk at n = 4 only")

# ---------------------------------------------------------------- matrix Jacobi integrator
def mat_mul(X, Y): return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]],
                          [X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]
def det(X): return X[0][0]*X[1][1]-X[0][1]*X[1][0]

def jacobi(qf, wf, L, N=20000):
    """A'' = -M A, M = q I + W(lambda) (W symmetric traceless 2x2).  RK4.  Returns first zero of det A."""
    h = L / N
    A = [[0.0, 0.0], [0.0, 0.0]]; P = [[1.0, 0.0], [0.0, 1.0]]
    def acc(x, A):
        q = qf(x); w1, w2 = wf(x)
        M = [[q + w1, w2], [w2, q - w1]]
        MA = mat_mul(M, A)
        return [[-MA[i][j] for j in range(2)] for i in range(2)]
    def add(X, Y, c): return [[X[i][j] + c*Y[i][j] for j in range(2)] for i in range(2)]
    x = 0.0; dprev = None; trprev = None
    for i in range(N):
        k1A, k1P = P, acc(x, A)
        k2A, k2P = add(P, k1P, h/2), acc(x+h/2, add(A, k1A, h/2))
        k3A, k3P = add(P, k2P, h/2), acc(x+h/2, add(A, k2A, h/2))
        k4A, k4P = add(P, k3P, h), acc(x+h, add(A, k3A, h))
        A = [[A[r][c] + h/6*(k1A[r][c]+2*k2A[r][c]+2*k3A[r][c]+k4A[r][c]) for c in range(2)] for r in range(2)]
        P = [[P[r][c] + h/6*(k1P[r][c]+2*k2P[r][c]+2*k3P[r][c]+k4P[r][c]) for c in range(2)] for r in range(2)]
        x += h
        d = det(A)
        if i > 5 and d <= 0.0:
            # simple conjugate point (multiplicity 1): det changes sign; interpolate
            return x - h * d / (d - dprev), A, P
        # multiplicity-2 conjugate point (A -> 0 as a whole, e.g. W = 0): det touches 0
        # without changing sign; detect via the trace of A, which does change sign then
        tr = A[0][0] + A[1][1]
        if i > 5 and trprev is not None and tr <= 0.0 < trprev and abs(d) < 1e-6:
            return x - h * tr / (tr - trprev), A, P
        dprev = d; trprev = tr
    return None, A, P

def scalar(qf, L, N=20000):
    h = L / N; u, up, x = 0.0, 1.0, 0.0
    for i in range(N):
        def f(x, y): return (y[1], -qf(x) * y[0])
        y = (u, up)
        k1 = f(x, y); k2 = f(x+h/2, (y[0]+h/2*k1[0], y[1]+h/2*k1[1]))
        k3 = f(x+h/2, (y[0]+h/2*k2[0], y[1]+h/2*k2[1])); k4 = f(x+h, (y[0]+h*k3[0], y[1]+h*k3[1]))
        un = u + h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]); up = up + h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
        x += h
        if i > 5 and un <= 0.0:
            return x - h * un / (un - u)
        u = un
    return None

# ---------------------------------------------------------------- S3a
qa = lambda x: 2.0 if 1.0 <= x <= 3.0 else -0.3
za, A, P = jacobi(qa, lambda x: (0.0, 0.0), 10.0)
zs = scalar(qa, 10.0)
rep("S3a", za is not None and zs is not None and abs(za - zs) < 1e-6,
    "W = 0: first zero of det A %.9f vs scalar u %.9f (reduction exact when Weyl vanishes)" % (za, zs))

# ---------------------------------------------------------------- S3b
random.seed(1955)
worse = 0; both = 0; shear_only = 0; margins = []
for t in range(200):
    c1, c2, c3 = random.uniform(0, 2), random.uniform(0.2, 3), random.uniform(-1, 3)
    wa, wb, wc = random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(0.2, 3)
    qf = lambda x, c1=c1, c2=c2, c3=c3: c3 * math.exp(-((x - 2*c1) / c2) ** 2) + 0.2 * c3
    wf = lambda x, wa=wa, wb=wb, wc=wc: (wa * math.sin(wc * x), wb * math.cos(0.7 * wc * x))
    L = 12.0
    zm, _, _ = jacobi(qf, wf, L, N=6000)
    zr = scalar(qf, L, N=6000)
    if zr is not None:
        both += 1
        if zm is None or zm > zr + 1e-6:
            worse += 1
        else:
            margins.append(zr - zm)
    elif zm is not None:
        shear_only += 1
rep("S3b", worse == 0,
    "200 random (q, Weyl) profiles: Ricci-only focuses in %d; full Jacobi zero later in %d (must be 0); "
    "full seats where Ricci-only does not in %d; min advance %.3g" % (both, worse, shear_only, min(margins) if margins else float('nan')))

# ---------------------------------------------------------------- S3c
w = 0.36
zc, _, _ = jacobi(lambda x: 0.0, lambda x: (w, 0.0), 20.0)
zcs = scalar(lambda x: 0.0, 20.0)
rep("S3c", zcs is None and zc is not None and abs(zc - math.pi / math.sqrt(w)) < 1e-6,
    "vacuum q=0, W=diag(%.2f,-%.2f): full conjugate point %.9f = pi/sqrt(w) = %.9f; scalar reduction: %s "
    "(Lyapunov number 0 yet it seats)" % (w, w, zc, math.pi / math.sqrt(w), zcs))

# ---------------------------------------------------------------- S4
def gw_residual(qf, wf, L, N=20000):
    """Non-tautological check: G = sqrt(det A) sampled on the grid, G'' by central
    differences, compared with -(sigma^2 + R_kk)/2 G where sigma^2 is the shear of
    B = A' A^-1; also the twist |B01 - B10| (point data => twist-free)."""
    h = L / N
    A = [[0.0, 0.0], [0.0, 0.0]]; P = [[1.0, 0.0], [0.0, 1.0]]; x = 0.0
    def acc(x, A):
        q = qf(x); w1, w2 = wf(x); M = [[q + w1, w2], [w2, q - w1]]
        MA = mat_mul(M, A); return [[-MA[i][j] for j in range(2)] for i in range(2)]
    def add(X, Y, c): return [[X[i][j] + c*Y[i][j] for j in range(2)] for i in range(2)]
    Gs, rhs, twist = [], [], 0.0
    for i in range(N):
        k1A, k1P = P, acc(x, A)
        k2A, k2P = add(P, k1P, h/2), acc(x+h/2, add(A, k1A, h/2))
        k3A, k3P = add(P, k2P, h/2), acc(x+h/2, add(A, k2A, h/2))
        k4A, k4P = add(P, k3P, h), acc(x+h, add(A, k3A, h))
        A = [[A[r][c] + h/6*(k1A[r][c]+2*k2A[r][c]+2*k3A[r][c]+k4A[r][c]) for c in range(2)] for r in range(2)]
        P = [[P[r][c] + h/6*(k1P[r][c]+2*k2P[r][c]+2*k3P[r][c]+k4P[r][c]) for c in range(2)] for r in range(2)]
        x += h
        d = det(A)
        if d <= 1e-4:
            if x > 0.5: break
            Gs.append(None); rhs.append(None); continue
        Ai = [[A[1][1]/d, -A[0][1]/d], [-A[1][0]/d, A[0][0]/d]]
        B = mat_mul(P, Ai)
        twist = max(twist, abs(B[0][1] - B[1][0]))
        th = B[0][0] + B[1][1]
        sh = [[B[0][0]-th/2, (B[0][1]+B[1][0])/2], [(B[0][1]+B[1][0])/2, B[1][1]-th/2]]
        s2 = sum(sh[a][b]**2 for a in range(2) for b in range(2))
        G = math.sqrt(d)
        Gs.append(G); rhs.append(-0.5 * (s2 + 2 * qf(x)) * G)
    worst = 0.0
    for k in range(1, len(Gs) - 1):
        if None in (Gs[k-1], Gs[k], Gs[k+1]): continue
        if Gs[k] < 0.2: continue       # finite differences are ill-conditioned at the caustic
        gpp = (Gs[k+1] - 2*Gs[k] + Gs[k-1]) / (h*h)
        worst = max(worst, abs(gpp - rhs[k]) / max(1.0, abs(rhs[k])))
    return worst, twist
prof = (lambda x: 0.5 + 0.3 * math.sin(x), lambda x: (0.4 * math.cos(1.3 * x), 0.2), 6.0)
res1, tw = gw_residual(*prof, N=10000)
res2, _ = gw_residual(*prof, N=20000)
res4, _ = gw_residual(*prof, N=40000)
rep("S4", res4 < 1e-5 and tw < 1e-9 and 3.0 < res1 / res2 < 5.0 and 3.0 < res2 / res4 < 5.0,
    "Gao-Wald eq.(13) G''/G = -(sigma^2 + R_kk)/2, G'' by central differences (G >= 0.2) on a sheared "
    "trajectory: rel residual %.2e / %.2e / %.2e at N = 1e4/2e4/4e4 (ratios %.2f, %.2f: pure O(h^2) "
    "truncation -> 0); twist |B01-B10| max %.1e (point data => omega = 0)" % (res1, res2, res4, res1/res2, res2/res4, tw))

# ---------------------------------------------------------------- S5
al, T0, l0 = sp.symbols('alpha T0 l0', positive=True)
q0 = 4 * sp.pi * T0
invariant = sp.simplify((4 * sp.pi * al**2 * T0) * (l0 / al)**2 - q0 * l0**2) == 0
not_inv = sp.simplify(al**2 * T0 - T0) != 0
rep("S5", invariant and not_inv,
    "q l^2 invariant under k -> alpha k (T_kk -> alpha^2 T_kk, l -> l/alpha); T_kk itself is not: "
    "the SI threshold presupposes k^0 = 1 in the frame where l is measured")

# ---------------------------------------------------------------- S6
c = 299792458.0
for tag, G in (("CODATA 2018", 6.67430e-11), ("CODATA 2022", 6.67430e-11)):
    coef = math.pi * c**4 / (4 * G)
    print("     T_COEFF (%s, G=%.5e) = %.6e Pa m^2" % (tag, G, coef))
coef = math.pi * c**4 / (4 * 6.67430e-11)
rel = 1.5e-15 / 6.67430e-11
rep("S6", abs(coef - 9.50532e43) / coef < 1e-5 and abs(round(coef / 1e39) - 95053) <= 1,
    "pi c^4/(4G) = %.5e; docstring/verdict print 9.5054e43 (rounds to 9.5053e43: last-digit discrepancy, "
    "rel %.1e); G's CODATA 2022 rel. uncertainty %.1e moves it by the same" % (coef, abs(9.5054e43 - coef) / coef, rel))

# ---------------------------------------------------------------- S7
spec = importlib.util.spec_from_file_location("seatindex", "/home/user/Claude-Method-Works/research/warp-drive/seatindex.py")
si = importlib.util.module_from_spec(spec); spec.loader.exec_module(si)
worst7 = 0.0
for m in (0.5, 1.0, 4.0, 16.0):
    z = si.seats(lambda x, m=m: m, 10.0 if m >= 0.5 else 20.0, n=40000)
    worst7 = max(worst7, abs(z - math.pi / math.sqrt(m)) / (math.pi / math.sqrt(m)))
rep("S7", worst7 < 1e-3, "seatindex.seats() constant q vs pi/sqrt(q): worst rel err %.2e (grid-limited)" % worst7)

# ---------------------------------------------------------------- S8
MeV_fm3 = 1.602176634e-13 / 1e-45      # J/m^3 per MeV/fm^3
n0 = 0.16                               # fm^-3 saturation (standard value)
eps0 = n0 * 939.57 * MeV_fm3           # rest-mass energy density, Pa
lstar_sat = math.sqrt(coef / eps0)
lstar_tree = math.sqrt(coef / 1e35)
treq100 = coef / 1e10
rep("S8", treq100 < eps0 and lstar_sat < 1e5 and lstar_tree < 1e5,
    "saturation rho c^2 = %.3e Pa (tree uses ~1e35 Pa = %.1fx saturation); T_req(100 km) = %.3e Pa; "
    "crossing l* = %.1f km (saturation) / %.1f km (tree's 1e35): 'below nuclear density beyond about 100 km' holds for both"
    % (eps0, 1e35 / eps0, treq100, lstar_sat / 1e3, lstar_tree / 1e3))

print("\n%d FAIL" % len(FAILS) if FAILS else "\nALL PASS")
sys.exit(1 if FAILS else 0)
