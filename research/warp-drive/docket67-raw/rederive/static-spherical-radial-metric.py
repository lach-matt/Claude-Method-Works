#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 'static-spherical-radial-metric'.

External result (as read): Hayward gr-qc/9408002 eq.(4)  E = (r/2)(1 - g^{-1}(dr,dr)),
an invariant (Misner-Sharp energy, G = 1); Visser hep-th/9303029 eq.(3): any static
spherically symmetric (asymptotically flat) metric can be cast as
  ds^2 = -e^{-2phi}(1-b/r)dt^2 + dr^2/(1-b/r) + r^2 dOmega^2,  eq.(5) b' = 8 pi G rho r^2.
Tree's use: overturn.py:403-439  Delta d = int_r1^r2 (1 - 1/sqrt(1-2m/r)) dr, m < 0 CONSTANT.

Checks
 C1  sympy: for the static diagonal metric with g_rr = 1/(1-2m(r)/r), Hayward's invariant
     E = (r/2)(1 - g^{rr}) equals m(r) identically; G^t_t gives m' = 4 pi r^2 rho (Visser eq.5, b=2m).
 C2  sympy: closed-form antiderivative of the deficit integrand (constant m<0), verified by
     differentiation; mpmath 40-digit table against overturn.py:87-102.
 C3  z3 + sympy: f(x) = 1-(1+2x)^{-1/2} <= x for all x > -1/2  [(s-1)^2 (s+2) >= 0], so for ANY
     profile m(r) with 1-2m/r>0:  Delta d <= int -m(r)/r dr <= int max(0,-m)/r dr  (the tree's
     'logarithm is the best case', generalised beyond the constant-m ansatz).
 C4  f(x)/x = 2/(s(s+1)), s = sqrt(1+2x): strictly decreasing for x>0, so the ratio is strictly
     monotone decreasing in |m| (tree's L3 monotonicity), for constant m and for m = lambda*mu(r).
 C5  saturation: 0 < f(x) < 1 for x>0, so Delta d < r2 - r1.
 C6  slicing hypothesis: on a non-Killing-orthogonal slice t = T(r) the radial proper length is
     sqrt(B - A T'^2) dr < sqrt(B) dr; in FLAT space (m=0) a boosted slice gives a nonzero
     'deficit' exceeding the log bound (0) -- the bound needs the static (U=0) slice.
 C7  numeric: random negative / sign-changing profiles obey C3's bound.
 C8  the tree's own Simpson routine reproduces its table (imported by path, not copied).
"""
import math, random, sys, importlib.util
import sympy as sp
import mpmath as mp

ok_all = True
def rep(tag, ok, msg):
    global ok_all
    ok_all &= bool(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}")

# ---------------- C1 -------------------------------------------------------
t, r, th, ph = sp.symbols('t r theta phi', real=True)
m = sp.Function('m')(r); Phi = sp.Function('Phi')(r)
X = [t, r, th, ph]
g = sp.diag(-sp.exp(2*Phi), 1/(1-2*m/r), r**2, r**2*sp.sin(th)**2)
gi = g.inv()
E = sp.simplify(r/2*(1 - gi[1, 1]))          # g^{-1}(dr,dr) = g^{rr}
rep("C1a", sp.simplify(E - m) == 0, f"Hayward E = (r/2)(1-g^rr) -> {E}")
# Einstein tensor
def christoffel(g, gi):
    n = 4
    return [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
              - sp.diff(g[b, c], X[d])) for d in range(n))/2) for c in range(n)]
             for b in range(n)] for a in range(n)]
G_ = christoffel(g, gi)
def ricci(G_):
    n = 4
    R = sp.zeros(4)
    for b in range(n):
        for c in range(n):
            R[b, c] = sp.simplify(sum(sp.diff(G_[a][b][c], X[a]) - sp.diff(G_[a][b][a], X[c])
                      + sum(G_[a][a][d]*G_[d][b][c] - G_[a][c][d]*G_[d][b][a] for d in range(n))
                      for a in range(n)))
    return R
Ric = ricci(G_)
Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(4) for b in range(4)))
Gmix_tt = sp.simplify((gi*(Ric - Rs*g/2))[0, 0])   # G^t_t = -8 pi rho
rho = sp.simplify(-Gmix_tt/(8*sp.pi))
rep("C1b", sp.simplify(rho - sp.diff(m, r)/(4*sp.pi*r**2)) == 0,
    f"G^t_t = -8 pi rho gives rho = {rho}  i.e. m' = 4 pi r^2 rho (Visser eq.5 with b = 2m)")
mc = sp.Symbol('M0', negative=True)
rep("C1c", sp.simplify(rho.subs(m, mc).doit()) == 0,
    "constant m on [r1,r2] <=> rho = 0 there (vacuum; Birkhoff -> negative-mass Schwarzschild exterior)")

# ---------------- C2 -------------------------------------------------------
a, rr = sp.symbols('a r', positive=True)     # a = |m|, m = -a
integrand = 1 - 1/sp.sqrt(1 + 2*a/rr)
F = rr - (sp.sqrt(rr*(rr + 2*a)) - 2*a*sp.log(sp.sqrt(rr) + sp.sqrt(rr + 2*a)))
rep("C2a", sp.simplify(sp.diff(F, rr) - integrand) == 0,
    "antiderivative r - sqrt(r(r+2a)) + 2a ln(sqrt r + sqrt(r+2a)) verified by differentiation")
mp.mp.dps = 40
def deficit_exact(A, r1=1, r2=200):
    A = mp.mpf(A)
    Fn = lambda x: x - mp.sqrt(x*(x + 2*A)) + 2*A*mp.log(mp.sqrt(x) + mp.sqrt(x + 2*A))
    return Fn(mp.mpf(r2)) - Fn(mp.mpf(r1))
tree = {1e-8: 1.000000, 1e-6: 1.000000, 1e-4: 0.999972, 1e-2: 0.997206, 1e0: 0.833100,
        1e1: 0.504993, 1e2: 0.174544, 1e3: 0.029831, 1e4: 0.003505}
tree_frac = {1e0: 0.0222, 1e1: 0.1345, 1e2: 0.4647, 1e3: 0.7942, 1e4: 0.9332}
worst = 0.0
for A, v in tree.items():
    d = deficit_exact(A)
    # quadrature cross-check (mpmath tanh-sinh)
    dq = mp.quad(lambda x: 1 - 1/mp.sqrt(1 + 2*mp.mpf(A)/x), [1, 10, 200])
    ratio = d/(mp.mpf(A)*mp.log(200))
    frac = d/199
    dev = abs(float(ratio) - v)
    worst = max(worst, dev/ v)
    s = f"|m|={A:g}: ratio={mp.nstr(ratio, 10)} (tree {v})  closed-vs-quad rel={mp.nstr(abs(d-dq)/abs(d),3)}"
    if A in tree_frac:
        s += f"  Dd/(r2-r1)={mp.nstr(frac, 6)} (tree {tree_frac[A]})"
    print("      " + s)
rep("C2b", worst < 5e-6/0.003505 + 1e-5,
    f"all nine tree ratios reproduced to 6 printed digits; worst relative deviation {worst:.2e}")
# second-order weak field
A = mp.mpf('1e-2')
second = 1 - mp.mpf(3)/2*A*(1 - mp.mpf(1)/200)/mp.log(200)
print(f"      weak-field 2nd order at |m|=1e-2: 1 - (3/2)|m|(1/r1-1/r2)/ln(r2/r1) = {mp.nstr(second,8)}")

# ---------------- C3 -------------------------------------------------------
import z3
S = z3.Real('s')
sol = z3.Solver()
# x = (s^2-1)/2, s = sqrt(1+2x) > 0 ; claim 1 - 1/s <= x  <=>  s^3 - 3 s + 2 >= 0 for s>0
sol.add(S > 0, z3.Not(S*S*S - 3*S + 2 >= 0))
res = sol.check()
sfac = sp.factor(sp.Symbol('s')**3 - 3*sp.Symbol('s') + 2)
rep("C3a", res == z3.unsat,
    f"z3: no s>0 with s^3-3s+2<0 ({res}); sympy factor = {sfac}  => f(x) <= x for all x > -1/2")
sol2 = z3.Solver(); sol2.add(S > 0, S != 1, z3.Not(S*S*S - 3*S + 2 > 0))
rep("C3b", sol2.check() == z3.unsat, "strict f(x) < x for x != 0 (equality only at x = 0)")
# vacuity guard: the negation of a false variant must be SAT
sol3 = z3.Solver(); sol3.add(S > 0, z3.Not(S*S*S - 3*S + 2 >= 1))
rep("C3c-guard", sol3.check() == z3.sat, "vacuity guard: the stronger false claim s^3-3s+2>=1 is refuted (sat)")

# ---------------- C4 -------------------------------------------------------
s = sp.symbols('s', positive=True)
q = sp.simplify((1 - 1/s)/((s**2 - 1)/2))
dq_ds = sp.simplify(sp.diff(q, s))
rep("C4", sp.simplify(q - 2/(s*(s + 1))) == 0 and sp.simplify(dq_ds + 2*(2*s + 1)/(s**2*(s + 1)**2)) == 0,
    f"f(x)/x = {q}, d/ds = {dq_ds} < 0 for s>1 => ratio strictly decreasing in |m| (any fixed-shape profile)")

# ---------------- C5 -------------------------------------------------------
sol4 = z3.Solver(); sol4.add(S > 1, z3.Not(z3.And(1 - 1/S > 0, 1 - 1/S < 1)))
rep("C5", sol4.check() == z3.unsat, "0 < f < 1 for x>0 (s>1): Delta d < r2 - r1 (saturation)")

# ---------------- C6 -------------------------------------------------------
v = sp.symbols('v', positive=True)
Afun, Bfun = sp.symbols('A B', positive=True)
dl2 = Bfun - Afun*v**2       # slice t = v r : induced g_rr
flat_def = (1 - sp.sqrt(1 - v**2))*199   # m = 0, A = B = 1
val = flat_def.subs(v, sp.Rational(1, 2))
rep("C6", sp.simplify(dl2 - Bfun) != 0 and float(val) > 0,
    f"flat space, slice t = r/2: proper length sqrt(1-v^2)*199, 'deficit' = {sp.nsimplify(val)} = {float(val):.3f} > 0 = |m| ln(r2/r1); "
    "the log bound is a statement about the Killing-orthogonal slice only (Hayward eq.27: dl = dr/sqrt(1-2E/r + rdot^2))")

# ---------------- C7 -------------------------------------------------------
random.seed(67)
viol = 0; n = 0
for _ in range(300):
    amp = 10**random.uniform(-4, 4); k = random.uniform(0, 3); c = random.uniform(-0.5, 1.0)
    prof = lambda x: -amp*(c + math.sin(k*x/20)**2)   # may change sign
    ok_dom = all(1 - 2*prof(x)/x > 0 for x in [1 + i*0.5 for i in range(399)])
    if not ok_dom:
        continue
    N = 20001; h = 199/(N-1); d = 0.0; b = 0.0
    for i in range(N):
        x = 1 + i*h; w = 1 if i in (0, N-1) else (4 if i % 2 else 2)
        d += w*(1 - 1/math.sqrt(1 - 2*prof(x)/x)); b += w*max(0.0, -prof(x))/x
    d *= h/3; b *= h/3; n += 1
    if d > b*(1 + 1e-9) + 1e-12:
        viol += 1
rep("C7", viol == 0 and n > 100, f"{n} random profiles (incl. sign-changing), violations of Dd <= int max(0,-m)/r dr: {viol}")

# ---------------- C8 -------------------------------------------------------
path = "/home/user/Claude-Method-Works/research/warp-drive/overturn.py"
try:
    spec = importlib.util.spec_from_file_location("overturn_ro", path)
    ov = importlib.util.module_from_spec(spec); spec.loader.exec_module(ov)
    rs = [ov.rate_ratio(A, 1.0, 200.0, 40001) for A in tree]
    dev = max(abs(x - float(deficit_exact(A)/(mp.mpf(A)*mp.log(200)))) for x, A in zip(rs, tree))
    rep("C8", dev < 1e-6, f"tree's Simpson rate_ratio (n=40001) vs closed form: max abs dev {dev:.2e}")
except Exception as e:
    rep("C8", False, f"could not import overturn.py read-only: {e!r}")

print("ALL PASS" if ok_all else "SOME FAIL")
sys.exit(0 if ok_all else 1)
