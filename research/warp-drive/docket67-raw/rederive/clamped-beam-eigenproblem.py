#!/usr/bin/env python3
"""DOCKET 67 audit -- clamped-beam (Euler-Bernoulli) fundamental, as fewsterteo.py uses it.

Checks, each able to fail:
  A  (sympy) the tree's mode g = cosh - cos - sigma(sinh - sin) solves g'''' = mu^4 g;
     g(0) = g'(0) = g(1) = 0 identically; g'(1)(sinh mu - sin mu)/mu = 2(cos mu cosh mu - 1),
     so the mode is clamped IFF cos mu cosh mu = 1.
  B  (sympy) the 4x4 clamped boundary determinant of the general solution is
     proportional to (1 - cos mu cosh mu): the positive spectrum is EXACTLY {mu_n^4}.
     lambda = 0 has only the zero clamped solution; lambda < 0 excluded by the IBP identity.
  C  (sympy) the IBP identity (g g''' - g'g'')' = g g'''' - g''^2.
  D  mu_1 is the SMALLEST positive root: alternating-series proof on (0, 4.5],
     cos < 0 on [4.5, 3pi/2], f' > 0 on (3pi/2, 2pi); cross-checked by mpmath interval arithmetic.
  E  mu_1 to 50 digits vs achievable.FEWSTER_MU1 = 4.730040744862704, C = mu^4/(16 pi^2)
     vs 3.169857938310467; achievable.py imported read-only if importable.
  F  Rayleigh quotient of the mode = mu_1^4 by quadrature (30 dps); fewsterteo._sampler's
     exponential decomposition reproduces the mode pointwise.
  G  minimality: Ritz upper bounds in the H^2_0 polynomial basis t^2(1-t)^2 t^k decrease to mu_1^4
     from above; a C-infinity bump gives a strictly larger quotient.
  H  Parseval route: (1/16 pi^3) INT_0^oo u^4 |ghat|^2 du = mu_1^4/(16 pi^2) by Fourier quadrature.
  CONTROLS: second root 7.853 gives a different quotient; mu = 4.8 is not clamped;
     unclamped g = sin(pi t) makes the Fourier integral diverge.
"""
import math, sys
import sympy as sp
import mpmath as mp
import numpy as np

RES = []
def chk(name, ok, detail=""):
    RES.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ("   " + str(detail) if detail != "" else ""))

# ---------------- A, B, C : symbolic
t = sp.Symbol('t', real=True)
mu = sp.Symbol('mu', positive=True)
sig = (sp.cosh(mu) - sp.cos(mu)) / (sp.sinh(mu) - sp.sin(mu))
g = sp.cosh(mu*t) - sp.cos(mu*t) - sig*(sp.sinh(mu*t) - sp.sin(mu*t))
chk("A1 g'''' - mu^4 g == 0", sp.simplify(sp.diff(g, t, 4) - mu**4*g) == 0)
chk("A2 g(0) == 0", sp.simplify(g.subs(t, 0)) == 0)
chk("A3 g'(0) == 0", sp.simplify(sp.diff(g, t).subs(t, 0)) == 0)
chk("A4 g(1) == 0 (by sigma)", sp.simplify(g.subs(t, 1)) == 0)
gp1 = sp.diff(g, t).subs(t, 1)
expr = sp.simplify(sp.expand(sp.simplify(gp1*(sp.sinh(mu) - sp.sin(mu))/mu)).rewrite(sp.exp))
target = (2*(sp.cos(mu)*sp.cosh(mu) - 1)).rewrite(sp.exp)
chk("A5 g'(1)(sinh mu - sin mu)/mu == 2(cos mu cosh mu - 1)", sp.simplify(sp.expand(expr - target)) == 0)
chk("A6 g''(0) == 2 mu^2 (nonzero: the mode is W^{2,2} but not smooth at the ends)",
    sp.simplify(sp.diff(g, t, 2).subs(t, 0) - 2*mu**2) == 0)

A, B, Cc, D = sp.symbols('A B C D')
basis = [sp.cosh(mu*t), sp.sinh(mu*t), sp.cos(mu*t), sp.sin(mu*t)]
rows = []
for pt in (0, 1):
    rows.append([b.subs(t, pt) for b in basis])
    rows.append([sp.diff(b, t).subs(t, pt) for b in basis])
M = sp.Matrix(rows)
det = sp.simplify(M.det())
ratio = sp.simplify((det / (mu**2*(1 - sp.cos(mu)*sp.cosh(mu)))).rewrite(sp.exp))
chk("B1 clamped determinant = const * mu^2 (1 - cos mu cosh mu)", ratio.is_number and ratio != 0,
    "det/(mu^2(1-cos cosh)) = %s" % ratio)
a0, a1, a2, a3 = sp.symbols('a0:4')
cub = a0 + a1*t + a2*t**2 + a3*t**3
sol = sp.solve([cub.subs(t, 0), sp.diff(cub, t).subs(t, 0), cub.subs(t, 1), sp.diff(cub, t).subs(t, 1)],
               [a0, a1, a2, a3])
chk("B2 lambda = 0: only the zero clamped cubic", all(v == 0 for v in sol.values()), sol)
f = sp.Function('f')(t)
ibp = sp.simplify(sp.diff(f*sp.diff(f, t, 3) - sp.diff(f, t)*sp.diff(f, t, 2), t)
                  - (f*sp.diff(f, t, 4) - sp.diff(f, t, 2)**2))
chk("C1 (f f''' - f'f'')' - (f f'''' - f''^2) == 0", ibp == 0)
# lambda < 0 excluded: for a clamped eigenfunction INT g''^2 = lambda INT g^2 >= 0 by C1 with
# every boundary term f f''' - f'f'' zero (f = f' = 0 at both ends): so lambda >= 0, and B2 kills 0.

# ---------------- D : mu_1 is the smallest positive root
x = sp.Rational(9, 2)
chk("D1 first-ratio 4x^4/1680 < 1 at x = 9/2 (terms of cos x cosh x - 1 = sum_{k>=1} (-4)^k x^{4k}/(4k)! "
    "decrease from a negative first term, so f < 0 on (0, 9/2])", 4*x**4/1680 < 1, float(4*x**4/1680))
kser = sp.Symbol('k', integer=True, nonnegative=True)
series_ok = all(sp.simplify(sp.series(sp.cos(t)*sp.cosh(t), t, 0, 26).removeO().coeff(t, 4*k_)
                            - sp.Integer(-4)**k_/sp.factorial(4*k_)) == 0 for k_ in range(7))
chk("D2 cos x cosh x = sum (-4)^k x^{4k}/(4k)!  (coefficients through x^24)", series_ok)
chk("D3 9/2 > pi/2 and 9/2 < 3pi/2 (so cos < 0 on [9/2, 3pi/2], f < -1 there)",
    bool(sp.Rational(9, 2) > sp.pi/2) and bool(sp.Rational(9, 2) < 3*sp.pi/2))
# f' = cos sinh - sin cosh > 0 on (3pi/2, 2pi) since cos > 0, sin < 0 there; f(3pi/2) = -1, f(2pi) > 0
chk("D4 f(3pi/2) = -1 and f(2pi) = cosh(2pi) - 1 > 0 (unique root in (3pi/2, 2pi), f' > 0 there)",
    sp.simplify(sp.cos(3*sp.pi/2)*sp.cosh(3*sp.pi/2) - 1) == -1 and
    float(sp.cosh(2*sp.pi) - 1) > 0)
# interval-arithmetic cross-check on [0.05, 4.7300], adaptive bisection (series proof covers (0, 9/2])
mp.iv.dps = 30
def ivf(a, b):
    I = mp.iv.mpf([a, b])
    return mp.iv.cos(I)*(mp.iv.exp(I) + mp.iv.exp(-I))/2 - 1
stack = [(mp.mpf('0.05'), mp.mpf('4.7300'), 0)]; cells = 0; unresolved = 0
while stack:
    a, b, d = stack.pop()
    if ivf(a, b).b < 0:
        cells += 1
    elif d > 40:
        unresolved += 1
    else:
        m_ = (a + b)/2; stack += [(a, m_, d + 1), (m_, b, d + 1)]
chk("D5 interval arithmetic: cos x cosh x - 1 < 0 on all of [0.05, 4.7300] (adaptive cells, rigorous enclosures)",
    unresolved == 0, "%d cells, %d unresolved" % (cells, unresolved))

# ---------------- E : digits
mp.mp.dps = 50
mu1 = mp.findroot(lambda m: mp.cos(m)*mp.cosh(m) - 1, mp.mpf('4.73'))
C50 = mu1**4/(16*mp.pi**2)
print("   mu_1 (50 dps) =", mp.nstr(mu1, 45))
print("   C    (50 dps) =", mp.nstr(C50, 45))
chk("E1 mu_1 agrees with achievable.FEWSTER_MU1 = 4.730040744862704 (1e-15)",
    abs(mu1 - mp.mpf('4.730040744862704')) < mp.mpf('1e-15'))
chk("E2 C = mu_1^4/(16 pi^2) agrees with the pinned 3.169857938310467 (2e-15: the pin is a 16-digit print of a double)",
    abs(C50 - mp.mpf('3.169857938310467')) < mp.mpf('2e-15'), mp.nstr(C50 - mp.mpf('3.169857938310467'), 3))
chk("E3 C rounds to Fewster's printed 'C ~ 3.17'", round(float(C50), 2) == 3.17)
try:
    sys.path.insert(0, '/home/user/Claude-Method-Works/research/warp-drive')
    import achievable
    chk("E4 achievable.FEWSTER_MU1 (bisection, imported) vs 50-dps root (2e-15)",
        abs(achievable.FEWSTER_MU1 - float(mu1)) < 2e-15, achievable.FEWSTER_MU1)
    chk("E5 achievable.FEWSTER_C == mu^4/(16 pi^2) of its own mu (same closed form: the agreement is NOT independent)",
        achievable.FEWSTER_C == achievable.FEWSTER_MU1**4/(16*math.pi**2), achievable.FEWSTER_C)
except Exception as e:
    print("   (achievable not importable here: %r)" % e)

# ---------------- F : Rayleigh quotient, the tree's exponential sampler
mp.mp.dps = 30
m1 = mp.findroot(lambda m: mp.cos(m)*mp.cosh(m) - 1, mp.mpf('4.73'))
def mode(m):
    s = (mp.cosh(m) - mp.cos(m))/(mp.sinh(m) - mp.sin(m))
    G = lambda tt: mp.cosh(m*tt) - mp.cos(m*tt) - s*(mp.sinh(m*tt) - mp.sin(m*tt))
    G2 = lambda tt: m**2*(mp.cosh(m*tt) + mp.cos(m*tt) - s*(mp.sinh(m*tt) + mp.sin(m*tt)))
    return s, G, G2
s1, G, G2 = mode(m1)
RQ = mp.quad(lambda tt: G2(tt)**2, [0, 0.5, 1])/mp.quad(lambda tt: G(tt)**2, [0, 0.5, 1])
chk("F1 INT g''^2 / INT g^2 = mu_1^4 (30 dps, rel 1e-25)", abs(RQ/m1**4 - 1) < mp.mpf('1e-25'),
    mp.nstr(RQ, 20))
bc = max(abs(v) for v in (G(0), mp.diff(G, 0), G(1), mp.diff(G, 1)))
chk("F2 clamped at mu_1: max|g,g'| at ends < 1e-25", bc < mp.mpf('1e-25'), mp.nstr(bc, 3))
# fewsterteo._sampler, reproduced exactly as printed at fewsterteo.py:224-230
muf = float(m1)
sg = (math.cosh(muf) - math.cos(muf))/(math.sinh(muf) - math.sin(muf))
aa = (muf, -muf, 1j*muf, -1j*muf)
cc = (0.5 - 0.5*sg, 0.5 + 0.5*sg, -0.5 - 0.5j*sg, -0.5 + 0.5j*sg)
dev = max(abs(sum(c*np.exp(a*tt) for a, c in zip(aa, cc)) - float(G(tt))) for tt in np.linspace(0, 1, 101))
chk("F3 fewsterteo._sampler sum c_k e^{a_k t} == the mode (101 points, 1e-12)", dev < 1e-12, dev)

# ---------------- G : minimality (variational)
def ritz(n):
    ks = range(n)
    phi = [t**2*(1 - t)**2*t**k for k in ks]
    K = sp.Matrix(n, n, lambda i, j: sp.integrate(sp.diff(phi[i], t, 2)*sp.diff(phi[j], t, 2), (t, 0, 1)))
    Mm = sp.Matrix(n, n, lambda i, j: sp.integrate(phi[i]*phi[j], (t, 0, 1)))
    Kn = mp.matrix(K.tolist()); Mn = mp.matrix(Mm.tolist())
    L = mp.cholesky(Mn); Li = mp.inverse(L)
    E = mp.eigsy(Li*Kn*Li.T)[0]
    return min(E[i] for i in range(n))
mp.mp.dps = 40
vals = [ritz(n) for n in (1, 2, 3, 4, 6, 8, 10)]
print("   Ritz lowest eigenvalue, n = 1,2,3,4,6,8,10:", [mp.nstr(v, 12) for v in vals])
mu14 = mu1**4
chk("G1 n = 1 (t^2(1-t)^2) gives exactly 504", abs(vals[0] - 504) < mp.mpf('1e-20'))
chk("G2 every Ritz value >= mu_1^4 (upper bounds; the infimum is not below mu_1^4)",
    all(v >= mu14 - mp.mpf('1e-20') for v in vals))
chk("G3 Ritz values non-increasing and converge to mu_1^4 (n = 10 within 1e-8 rel)",
    all(vals[i] >= vals[i+1] - mp.mpf('1e-25') for i in range(len(vals)-1)) and abs(vals[-1]/mu14 - 1) < 1e-8,
    mp.nstr(vals[-1] - mu14, 5))
mp.mp.dps = 30
bump = lambda tt: mp.exp(-1/(tt*(1 - tt))) if 0 < tt < 1 else mp.mpf(0)
bq = mp.quad(lambda tt: mp.diff(bump, tt, 2)**2, [0, 0.25, 0.5, 0.75, 1])/mp.quad(lambda tt: bump(tt)**2, [0, 0.5, 1])
chk("G4 C-infinity bump quotient strictly above mu_1^4", bq > m1**4, mp.nstr(bq, 10))

# ---------------- H : Parseval route on the Fourier side (double precision)
def ghat(u):
    z = np.zeros_like(u, dtype=complex)
    for a, c in zip(aa, cc):
        w = a - 1j*u
        z += c*(np.exp(w) - 1)/w
    return z
U = 4000.0
uu = np.linspace(1e-9, U, 4_000_001)
integrand = uu**4*np.abs(ghat(uu))**2
Ipart = np.trapezoid(integrand, uu) if hasattr(np, 'trapezoid') else np.trapz(integrand, uu)
g2_0 = 2*muf**2
g2_1 = float(G2(1))
tail = (g2_0**2 + g2_1**2)/U           # averaged 1/u^2 tail
four = (Ipart + tail)/(16*math.pi**3)
target = muf**4/(16*math.pi**2)
chk("H1 (1/16pi^3) INT_0^oo u^4|ghat|^2 du = mu_1^4/(16 pi^2) (rel 1e-5, quadrature + 1/u^2 tail)",
    abs(four/target - 1) < 1e-5, "%.10f vs %.10f rel %.2e" % (four, target, four/target - 1))
chk("H2 |g''(1)| = |g''(0)| = 2 mu^2 (symmetric mode; the tail coefficient used in H1)",
    abs(abs(g2_1) - g2_0) < 1e-9, g2_1)

# ---------------- controls
s2, Gb, G2b = mode(mp.findroot(lambda m: mp.cos(m)*mp.cosh(m) - 1, mp.mpf('7.85')))
RQ2 = mp.quad(lambda tt: G2b(tt)**2, [0, 0.5, 1])/mp.quad(lambda tt: Gb(tt)**2, [0, 0.5, 1])
mu2 = mp.findroot(lambda m: mp.cos(m)*mp.cosh(m) - 1, mp.mpf('7.85'))
chk("K1 CONTROL second root (7.853) gives a different, larger quotient = mu_2^4", RQ2 > RQ and abs(RQ2/mu2**4 - 1) < mp.mpf('1e-20'), mp.nstr(RQ2, 10))
s3, Gc, _ = mode(mp.mpf('4.8'))
chk("K2 CONTROL mu = 4.8 is NOT clamped (g'(1) != 0)", abs(mp.diff(Gc, 1)) > mp.mpf('0.1'),
    mp.nstr(mp.diff(Gc, 1), 5))
def box_int(Ucut):
    u = np.linspace(1e-9, Ucut, int(Ucut*200))
    gh = (1 - np.exp(-1j*u))/(1j*u)     # g = 1 on [0,1]: not W^{2,2}
    return np.trapezoid(u**4*np.abs(gh)**2, u)
r = box_int(400)/box_int(200)
chk("K3 CONTROL unclamped box: Fourier integral grows ~U^3 on doubling (ratio ~8)", 7 < r < 9, "%.3f" % r)

npass = sum(ok for _, ok in RES); nfail = len(RES) - npass
print("\n%d PASS, %d FAIL" % (npass, nfail))
sys.exit(1 if nfail else 0)
