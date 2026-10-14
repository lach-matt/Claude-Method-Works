#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for Olum, 'Superluminal travel requires negative energies',
gr-qc/9805003v2 (PRL 81, 3567 (1998)).  READ at source (arXiv v2 full text via alphaXiv).

What is finite / closed-form here, and is checked:
  C1  Eq.(1) is flat space: x' = x(1-t^2) gives ds^2 = -dt^2 + dx'^2          (sympy)
  C2  Eq.(2) null rays; x = t/(1-t^2) is a right-going null ray; arrival at x=1
      solves t^2+t-1=0 -> t = (sqrt5-1)/2 = 0.618.  The arXiv text layer prints
      '(1 + sqrt5)/2 ~ 0.618'; (1+sqrt5)/2 = 1.618.  RECORDED AS A TEXT-LAYER
      DISCREPANCY (possibly a dropped minus in extraction), not a refutation;
      the numeral 0.618 is right and nothing downstream uses the expression.
  C3  Extrinsic flatness at A: a surface made of geodesics through A has II(X,X)=0
      for every X in T_A Sigma, hence II = 0 by polarisation, hence theta-hat(A)=0 (sympy)
  C4  The contradiction step Eqs.(4)-(8) as a finite propositional/linear problem (z3):
      WEC/NEC on P + generic => theta(B) < 0 ; Condition 1 => K1;1 >= 0, K2;2 >= 0 ;
      theta = K1;1 + K2;2  -> UNSAT.  And the vacuity guard: drop NEC -> SAT.
  C5  Casimir Eqs.(9)-(10): T traceless, R_ab K^a K^b = 8 pi T_ab K^a K^b = -2 pi^3/(45 d^4) (sympy)
  C6  Linearised optical tidal matrix T_ij = R_{iKjK} for g = diag(-(1+2Phi), (1-2Phi) delta)
      computed from the Riemann tensor to first order (sympy) -- used by C7.
  C7  THE NARROWING, SHOWN: a smooth negative-mass ball (linearised, prescribed, as
      composite.py prescribes M<0).  A ray passing OUTSIDE the ball arrives EARLY
      against flat space (a Shapiro LEAD) while T_ab = 0 -- WEC and NEC hold -- at
      every point of that ray.  So 'a lead requires negative energy POINTWISE ON THE
      PATH' is NOT Olum's theorem.  Consistency with Olum is also shown: that ray is
      not a Condition-1 path (theta-hat(B) < 0, and a neighbouring ray nearer the
      centre arrives earlier), while the locally EARLIEST ray (b = 0) passes through
      the negative-energy region and is defocused (theta-hat(B) > 0).  Both halves.
"""
import math, sys
import sympy as sp

ok = True
def rep(tag, cond, msg):
    global ok
    ok &= bool(cond)
    print(f"[{'PASS' if cond else 'FAIL'}] {tag}: {msg}")

# ---------------- C1, C2 ----------------
t, x = sp.symbols('t x', real=True)
dt, dx = sp.symbols('dt dx')
ds2 = (-1 + 4*t**2*x**2)*dt**2 - 4*t*x*(1 - t**2)*dx*dt + (1 - t**2)**2*dx**2
xp = x*(1 - t**2)
dxp = sp.diff(xp, t)*dt + sp.diff(xp, x)*dx
rep("C1", sp.expand(ds2 - (-dt**2 + dxp**2)) == 0, "Eq.(1) == -dt^2 + dx'^2 with x'=x(1-t^2)")
v = sp.symbols('v')
roots = sp.solve(sp.Eq(ds2.subs({dt: 1, dx: v}), 0), v)
want = {sp.simplify((1 + 2*t*x)/(1 - t**2)), sp.simplify((-1 + 2*t*x)/(1 - t**2))}
rep("C2a", {sp.simplify(r) for r in roots} == want, f"null slopes dx/dt = (+-1+2tx)/(1-t^2): {roots}")
xr = t/(1 - t**2)
rep("C2b", sp.simplify(sp.diff(xr, t) - (1 + 2*t*xr)/(1 - t**2)) == 0, "x=t/(1-t^2) is a right-going null ray")
tarr = [r for r in sp.solve(sp.Eq(xr, 1), t) if r.is_positive][0]
rep("C2c", sp.simplify(tarr - (sp.sqrt(5) - 1)/2) == 0 and abs(float(tarr) - 0.618) < 1e-3,
    f"arrival t = {tarr} = {float(tarr):.6f}; text layer's (1+sqrt5)/2 = {float((1+sp.sqrt(5))/2):.6f}"
    " -> DISCREPANCY in printed expression, value 0.618 correct")

# ---------------- C3 ----------------
a, b, c, p, q = sp.symbols('a b c p q', real=True)
quad = sp.expand(a*p**2 + 2*b*p*q + c*q**2)          # II(X,X), X = (p,q)
sol = sp.solve([sp.Poly(quad, p, q).coeff_monomial(m) for m in (p**2, p*q, q**2)], [a, b, c], dict=True)
rep("C3", sol == [{a: 0, b: 0, c: 0}], "II(X,X)=0 for all X  =>  II = 0  (polarisation)  => theta-hat(A)=0")

# ---------------- C4 (z3) ----------------
import z3
RKK, sig2, thB, K11, K22, K3, Z3b, KZZ1, KZZ2 = z3.Reals('RKK sig2 thB K11 K22 K3 Z3b KZZ1 KZZ2')
def core(with_nec=True):
    s = z3.Solver()
    # theta(B) = -INT (RKK + 2 sigma^2 + theta^2/2) dv, theta(A)=0, finite (no focal point);
    # encoded on its sign content: with NEC (RKK>=0) and generic (sigma^2>0 somewhere) theta(B) < 0.
    if with_nec:
        s.add(RKK >= 0)
    s.add(sig2 > 0)
    s.add(z3.Implies(z3.And(RKK >= 0, sig2 > 0), thB < 0))
    # Condition 1 at B, Eqs.(5)-(7): K^a;b Z_a Z_b = -K3 Z3;b Z^b, K3>0, Z3;bZ^b <= 0, for Z = E1, E2
    s.add(K3 > 0, Z3b <= 0, KZZ1 == -K3*Z3b, KZZ2 == -K3*Z3b)
    s.add(K11 == KZZ1, K22 == KZZ2, thB == K11 + K22)          # Eq.(8)
    if not with_nec:
        s.add(RKK < 0)
    return s.check()
r1, r2 = core(True), core(False)
rep("C4a", r1 == z3.unsat, f"NEC-on-P + generic + Condition 1 : {r1} (contradiction, as Olum)")
rep("C4b", r2 == z3.sat, f"vacuity guard, NEC dropped on P : {r2} (Condition 1 then satisfiable)")

# ---------------- C5 ----------------
d = sp.symbols('d', positive=True)
eta = sp.diag(-1, 1, 1, 1)
T = sp.pi**2/(720*d**4)*sp.diag(-1, 1, 1, -3)
K = sp.Matrix([1, 0, 0, 1])
trace = sum(eta.inv()[i, i]*T[i, i] for i in range(4))
RKKc = sp.simplify(8*sp.pi*(K.T*T*K)[0])   # R_ab K^a K^b = 8pi(T_ab - T g_ab/2)K^aK^b, T traceless, K null
rep("C5a", sp.simplify(trace) == 0, "Casimir T_ab traceless")
rep("C5b", sp.simplify(RKKc + 2*sp.pi**3/(45*d**4)) == 0, f"R_ab K^a K^b = {RKKc} (paper Eq.10: -2pi^3/(45 d^4))")
rep("C5c", T[0, 0].is_negative, f"energy density T_00 = {T[0,0]} < 0 (WEC and NEC violated between plates)")

# ---------------- C6 ----------------
eps = sp.symbols('epsilon')
X = sp.symbols('t x y z', real=True)
Phi = sp.Function('Phi')(*X[1:])
g = sp.diag(-(1 + 2*eps*Phi), 1 - 2*eps*Phi, 1 - 2*eps*Phi, 1 - 2*eps*Phi)
ginv = g.inv()
def trunc(e): return sp.series(sp.simplify(e), eps, 0, 2).removeO()
Gam = [[[trunc(sum(ginv[a_, dd]*(sp.diff(g[dd, b_], X[c_]) + sp.diff(g[dd, c_], X[b_]) - sp.diff(g[b_, c_], X[dd]))
                   for dd in range(4))/2) for c_ in range(4)] for b_ in range(4)] for a_ in range(4)]
def Riem_up(a_, b_, c_, d_):   # R^a_{bcd}, first order: drop Gamma*Gamma (O(eps^2))
    return sp.diff(Gam[a_][b_][d_], X[c_]) - sp.diff(Gam[a_][b_][c_], X[d_])
Kv = [1, 1, 0, 0]
def Tij(i, j):   # R_{i a j b} K^a K^b = eta_ii R^i_{a j b} K^a K^b at first order
    return sp.expand(sum(Riem_up(i, a_, j, b_)*Kv[a_]*Kv[b_] for a_ in range(4) for b_ in range(4)))
Tyy, Tzz, Tyz = Tij(2, 2), Tij(3, 3), Tij(2, 3)
H = lambda u, w: sp.diff(Phi, u, w)
xs, ys, zs = X[1:]
rep("C6a", sp.simplify(Tyy - eps*(2*H(ys, ys) + H(xs, xs))) == 0, f"T_yy = {sp.factor(Tyy)}")
rep("C6b", sp.simplify(Tzz - eps*(2*H(zs, zs) + H(xs, xs))) == 0, f"T_zz = {sp.factor(Tzz)}")
rep("C6c", sp.simplify(Tyz - eps*2*H(ys, zs)) == 0, f"T_yz = {sp.factor(Tyz)}; trace = 2 lap(Phi) = R_KK")

# ---------------- C7 ----------------
def hess(M, R, px, py):
    r = math.hypot(px, py)
    if r >= R:
        d1, d2 = M/r**2, -2*M/r**3
    else:
        d1, d2 = M*r/R**3, M/R**3
    n = (px/r, py/r) if r > 0 else (0.0, 0.0)
    Hxx = d2*n[0]**2 + d1/r*(1 - n[0]**2) if r > 0 else d2
    Hyy = d2*n[1]**2 + d1/r*(1 - n[1]**2) if r > 0 else d2
    Hzz = d1/r if r > 0 else d2
    return Hxx, Hyy, Hzz
def phi(M, R, r):
    return -M/r if r >= R else -M*(3*R**2 - r**2)/(2*R**3)
def ray(M, R, bimp, L=400.0, N=40000):
    """integrate B' = -B^2 - T (2x2 transverse, diagonal here since z=0 plane), B(-L)=0,
    and the Shapiro delay dt/dx - 1 = -2 Phi, along x in [-L, L] at y = bimp."""
    h = 2*L/N
    B = [0.0, 0.0]; delay = 0.0; rho_min_on_path = 0.0
    def f(xx, B):
        Hxx, Hyy, Hzz = hess(M, R, xx, bimp)
        Tyy_, Tzz_ = 2*Hyy + Hxx, 2*Hzz + Hxx
        return [-B[0]**2 - Tyy_, -B[1]**2 - Tzz_]
    xx = -L
    for _ in range(N):
        k1 = f(xx, B); k2 = f(xx+h/2, [B[i]+h/2*k1[i] for i in range(2)])
        k3 = f(xx+h/2, [B[i]+h/2*k2[i] for i in range(2)]); k4 = f(xx+h, [B[i]+h*k3[i] for i in range(2)])
        B = [B[i] + h/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i]) for i in range(2)]
        xm = xx + h/2
        delay += -2*phi(M, R, math.hypot(xm, bimp))*h
        if math.hypot(xm, bimp) < R:
            rho_min_on_path = min(rho_min_on_path, 3*M/(4*math.pi*R**3))
        xx += h
    return B[0] + B[1], delay, rho_min_on_path
M, R = -1e-3, 1.0
res = {}
for bimp in (0.0, 0.5, 2.0, 2.5):
    th, dl, rmin = ray(M, R, bimp)
    res[bimp] = (th, dl, rmin)
    print(f"      M={M:+.0e} R={R} b={bimp:<4}: theta-hat(B) = {th:+.3e}   Shapiro (t - t_flat) = {dl:+.4e}"
          f"   min rho on path = {rmin:+.2e}")
th2, dl2, r2m = res[2.0]
rep("C7a", dl2 < 0 and r2m == 0.0,
    "ray b=2 > R: a LEAD against flat space (t - t_flat < 0) with rho = 0, T_ab = 0 -- WEC/NEC HOLD at every point of the path")
rep("C7b", th2 < 0 and res[0.5][1] < dl2,
    "that ray is NOT a Condition-1 path: theta-hat(B) < 0 (Weyl focusing, sign-blind), and a neighbour nearer the centre arrives earlier")
th0, dl0, r0m = res[0.0]
rep("C7c", th0 > 0 and r0m < 0 and dl0 == min(v[1] for v in res.values()),
    "the locally EARLIEST ray b=0 crosses the negative-energy region (rho<0 on P) and is DEFOCUSED: Olum's conclusion, on that path")
thp, dlp, _ = ray(+1e-3, R, 2.0)
rep("C7d", thp < 0 and dlp > 0, f"control M=+1e-3, b=2: delay {dlp:+.4e} > 0, theta-hat(B) {thp:+.3e} < 0 (Weyl focusing sign-blind)")

print("\nALL PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
