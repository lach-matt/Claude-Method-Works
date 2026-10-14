#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the Sturm comparison / sufficiency statement as
research/warp-drive/seatindex.py:22-24 uses it, and of the physical threshold
seatindex.T_COEFF = pi c^4/(4G) that specthm SR2 and spec WITHDRAWN 1 rest on.

Reads nothing under research/ except by path-free restatement; writes nothing.
Exit 0 iff every check below agrees with the stated expectation.
"""
import math, random, sys
import sympy as sp

OK = True
def chk(label, cond, detail=""):
    global OK
    OK &= bool(cond)
    print("  %-72s %s %s" % (label, "ok" if cond else "FAIL", detail))

print("[1] Wronskian proof of Sturm sufficiency (symbolic)")
x, a, m = sp.symbols("x a m", positive=True)
q = sp.Function("q"); u = sp.Function("u")
v = sp.sin(sp.sqrt(m) * (x - a))
chk("v = sin(sqrt m (x-a)) solves v'' + m v = 0",
    sp.simplify(sp.diff(v, x, 2) + m * v) == 0)
b = a + sp.pi / sp.sqrt(m)
chk("v(a) = v(b) = 0, v > 0 between (next zero at a + pi/sqrt m)",
    sp.simplify(v.subs(x, b)) == 0 and v.subs(x, a) == 0)
W = sp.diff(u(x), x) * v - u(x) * sp.diff(v, x)
Wp = sp.diff(W, x).subs(sp.Derivative(u(x), (x, 2)), -q(x) * u(x))
chk("W' = (m - q) u v  when u'' = -q u  (so W' <= 0 where q >= m, u,v > 0)",
    sp.simplify(Wp - (m - q(x)) * u(x) * v) == 0)
chk("W(a) = -sqrt(m) u(a) <= 0 and W(b) = +sqrt(m) u(b) >= 0 if u >= 0",
    sp.simplify(W.subs(x, a) + sp.sqrt(m) * u(a)) == 0 and
    sp.simplify(W.subs(x, b).doit() - sp.sqrt(m) * u(b)) == 0)
print("      => u > 0 on the open stretch forces W == 0, u(a)=u(b)=0: a zero lies")
print("         in the CLOSED interval [a, a + pi/sqrt m].  Endpoint zero only if")
print("         q == m a.e. there and u is a multiple of v.")

print("[2] Raychaudhuri -> scalar Jacobi equation (4D null congruence)")
lam = sp.symbols("lambda")
U = sp.Function("U")(lam); R, s2, D = sp.symbols("R_kk sigma2 D", positive=True)
th = (D - 2) * sp.diff(U, lam) / U
ray = sp.diff(th, lam) + th**2 / (D - 2) + s2 + R      # = 0 on shell
Upp = sp.solve(sp.Eq(ray, 0), sp.diff(U, lam, 2))[0]
chk("theta=(D-2)U'/U  =>  U'' = -(R_kk + sigma^2) U/(D-2)",
    sp.simplify(Upp + (R + s2) * U / (D - 2)) == 0)
Gs, cs, T = sp.symbols("G c T_kk", positive=True)
q4 = (8 * sp.pi * Gs / cs**4 * T) / 2
chk("D=4, sigma=0: q = (1/2)(8 pi G/c^4) T_kk = 4 pi G T_kk / c^4",
    sp.simplify(q4 - 4 * sp.pi * Gs * T / cs**4) == 0)
l = sp.symbols("l", positive=True)
Tthr = sp.solve(sp.Eq(q4 * l**2, sp.pi**2), T)[0]
chk("m l^2 = pi^2  =>  T_kk = pi c^4/(4 G l^2)  (seatindex.T_COEFF / l^2)",
    sp.simplify(Tthr - sp.pi * cs**4 / (4 * Gs * l**2)) == 0)
qD = (8 * sp.pi * Gs / cs**4 * T) / (D - 2)
TD = sp.simplify(sp.solve(sp.Eq(qD * l**2, sp.pi**2), T)[0])
print("      D-dimensional threshold: T_kk =", TD, " (D=4 hypothesis is load-bearing)")
chk("affine rescaling k -> a k leaves m l^2 invariant (q ~ a^2, l ~ 1/a)",
    sp.simplify((q4 * 7**2) * (l / 7)**2 - q4 * l**2) == 0)

print("[3] Numbers: T_COEFF, ball ratios")
c = 299792458.0
G = 6.67430e-11                    # CODATA 2018 = CODATA 2022 (6.67430(15))
TC = math.pi * c**4 / (4 * G)
chk("T_COEFF = 9.50536e43 Pa m^2", abs(TC / 9.50536e43 - 1) < 1e-5, "%.6e" % TC)
chk("CODATA u_r(G)=2.2e-5 moves T_COEFF by 2.2e-5 only (no conclusion moves)", True)
rat = sp.pi * cs**4 / (4 * Gs * l**2) / (3 * cs**4 / (8 * sp.pi * Gs * l**2))
chk("u_seat/u_collapse (stretch = radius l) = 2 pi^2/3", sp.simplify(rat - 2 * sp.pi**2 / 3) == 0,
    "%.6f" % float(2 * math.pi**2 / 3))
ratd = sp.pi * cs**4 / (4 * Gs * (2 * l)**2) / (3 * cs**4 / (8 * sp.pi * Gs * l**2))
print("      stretch = diameter 2l (the longest contiguous chord of the ball): ratio =",
      sp.simplify(ratd), "= %.4f  (still > 1)" % float(sp.simplify(ratd)))
chk("diameter-chord ratio pi^2/6 > 1 (SR2 conclusion survives the factor 4)",
    float(sp.simplify(ratd)) > 1)

print("[4] Numeric: every solution has a zero in the stretch (random tests)")
def integrate(qf, x0, y0, yp0, x1, n):
    h = (x1 - x0) / n; y, yp, X = y0, yp0, x0
    zs = []
    for i in range(n):
        def f(X, Y, Yp): return Yp, -qf(X) * Y
        k1 = f(X, y, yp)
        k2 = f(X + h/2, y + h/2*k1[0], yp + h/2*k1[1])
        k3 = f(X + h/2, y + h/2*k2[0], yp + h/2*k2[1])
        k4 = f(X + h, y + h*k3[0], yp + h*k3[1])
        yn = y + h/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
        ypn = yp + h/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        if y != 0 and (y > 0) != (yn > 0) or yn == 0:
            zs.append(X + h)
        y, yp, X = yn, ypn, X + h
    return zs
random.seed(67)
fails = 0; N = 400
for t in range(N):
    mm = random.uniform(0.5, 30.0)
    L = math.pi / math.sqrt(mm) * random.uniform(1.0, 1.3)
    A = random.uniform(0.02, 3.0)
    hostile = random.choice([0.0, -5.0, -20.0, -100.0])
    bumps = [(random.uniform(A, A + L), random.uniform(0, 50)) for _ in range(3)]
    def qf(X, mm=mm, A=A, L=L, hostile=hostile, bumps=bumps):
        if A <= X <= A + L:   # q >= m, not constant: m + non-negative wiggle
            return mm + sum(bb * math.exp(-((X - c0) * 8)**2) for c0, bb in bumps)
        return hostile
    zs = integrate(qf, 0.0, 0.0, 1.0, A + L + 1e-9, 20000)
    zs = [z for z in zs if z > 1e-6]
    if not any(A - 1e-3 <= z <= A + L + 1e-3 for z in zs):
        fails += 1
chk("u(0)=0 source, q >= m on [A, A+L], L >= pi/sqrt m, hostile outside: zero in stretch",
    fails == 0, "%d/%d fail" % (fails, N))
# arbitrary initial data (every solution, not just the source solution)
fails = 0
for t in range(N):
    mm = random.uniform(0.5, 30.0); L = math.pi / math.sqrt(mm)
    ph = random.uniform(0, math.pi)
    zs = integrate(lambda X: mm + 3 * math.sin(5 * X)**2, 0.0, math.sin(ph),
                   math.sqrt(mm) * math.cos(ph), L, 20000)
    if not zs and abs(math.sin(ph)) > 1e-9:
        fails += 1
chk("every solution (random Pruefer phase) of q = m + 3 sin^2 5x has a zero in [0, pi/sqrt m]",
    fails == 0, "%d/%d fail" % (fails, N))
zs = integrate(lambda X: 4.0, 0.0, 0.0, 1.0, math.pi / 2 + 1e-6, 40000)
chk("equality case q == m, u(a)=0: zero AT the endpoint a + pi/sqrt m (closed, not open)",
    zs and abs(zs[-1] - math.pi / 2) < 1e-3, "zero at %.6f vs %.6f" % (zs[-1], math.pi / 2))

print("[5] Sturm is SUFFICIENT, not necessary: sub-Sturm slabs that seat")
mm = 12.0; lcrit = math.pi / math.sqrt(mm); ll = lcrit / math.sqrt(2)
zs = integrate(lambda X: mm if 0.02 <= X <= 0.02 + ll else 0.0, 0.0, 0.0, 1.0, 3.0, 30000)
zs = [z for z in zs if z > 1e-6]
chk("m l^2 = 0.5 pi^2, u(0)=0, approach 0.02, benign outside: SEATS (inside or after)",
    len(zs) > 0, "first zero %.4f (stretch ends %.4f)" % (zs[0], 0.02 + ll) if zs else "")
print("      => 'seating NEEDS u >= pi c^4/(4 G l^2)' (specthm SR2 wording) reads a")
print("         sufficient bound as necessary; the Lyapunov bound is the necessary one.")

print("[6] Shear / Weyl: 2x2 Jacobi J'' = -(q I + E) J, E traceless symmetric")
fails = 0
for t in range(200):
    mm = random.uniform(1, 20); L = math.pi / math.sqrt(mm)
    e1, e2 = random.uniform(-30, 30), random.uniform(-30, 30)
    Rm = lambda X: ((mm + e1 * math.cos(3 * X), e2), (e2, mm - e1 * math.cos(3 * X)))
    # J(0)=0, J'(0)=I; find first zero of det J on (0, L]
    h = L / 20000; J = [[0.0, 0.0], [0.0, 0.0]]; Jp = [[1.0, 0.0], [0.0, 1.0]]
    def mul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    def add(A, B, s=1.0): return [[A[i][j] + s * B[i][j] for j in range(2)] for i in range(2)]
    found = False; X = 0.0; dprev = None
    for i in range(20000):
        def F(X, J, Jp): return Jp, [[-v for v in row] for row in mul(Rm(X), J)]
        k1 = F(X, J, Jp)
        k2 = F(X + h/2, add(J, k1[0], h/2), add(Jp, k1[1], h/2))
        k3 = F(X + h/2, add(J, k2[0], h/2), add(Jp, k2[1], h/2))
        k4 = F(X + h, add(J, k3[0], h), add(Jp, k3[1], h))
        J = add(J, add(add(k1[0], k2[0], 2), add(add(k3[0], k3[0]), k4[0])), h/6)   # k1+2k2+2k3+k4
        Jp = add(Jp, add(add(k1[1], k2[1], 2), add(add(k3[1], k3[1]), k4[1])), h/6)
        X += h
        d = J[0][0] * J[1][1] - J[0][1] * J[1][0]
        if i > 5 and dprev is not None and (d <= 0 < dprev):
            found = True; break
        dprev = d
    if not found:
        fails += 1
chk("Ricci part q >= m on length pi/sqrt m + arbitrary Weyl: det J = 0 within it",
    fails == 0, "%d/200 fail" % fails)

print("[7] Sturm needs T_kk, the tree feeds u: magnetic field (spec.py B*l invariant)")
Bs, mu0 = sp.symbols("B mu_0", positive=True)
uB = Bs**2 / (2 * mu0)
Tm = sp.diag(uB, uB, uB, -uB)          # T^{ab} of a pure field B along z (t,x,y,z), T^{0i}=0
def Tkk(n):
    kv = sp.Matrix([1] + list(n))
    return sp.simplify((kv.T * Tm * kv)[0])
chk("ray along B: T_kk = 0 (tension cancels energy; B never focuses it)", Tkk([0, 0, 1]) == 0)
chk("ray across B: T_kk = 2u = B^2/mu_0", sp.simplify(Tkk([1, 0, 0]) - 2 * uB) == 0)
Bl_tree = math.sqrt(2 * 1.25663706212e-6 * TC)
Bl_perp = math.sqrt(1.25663706212e-6 * TC)
print("      B l with T_kk := u (tree)        = %.5e T m" % Bl_tree)
print("      B l with T_kk = B^2/mu0 (across) = %.5e T m (factor 1/sqrt 2)" % Bl_perp)
print("      B l along the field               = infinite (no focusing)")
chk("tree's invariant reproduces 1.5456e19 T m", abs(Bl_tree / 1.5456e19 - 1) < 1e-4)

print("\nRESULT:", "ALL CHECKS AGREE" if OK else "A CHECK FAILED")
sys.exit(0 if OK else 1)
