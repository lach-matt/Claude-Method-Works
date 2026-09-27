#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the Stefan-Boltzmann result as the tree uses it
(noise.py:114, 613, 1026-1027; fluctuation.py:84-85, 461-464):
  one free massless real scalar, thermal (KMS) state at inverse temperature beta,
  flat Minkowski space, infinite volume, normal-ordered w.r.t. the Minkowski vacuum:
  rho = pi^2/(30 beta^4), p = rho/3, and g(0) = <:phidot^2:>_beta = rho.
Independent of the tree: nothing is imported from research/warp-drive.
Every check prints PASS/FAIL; exit 1 on any FAIL."""
import sys
import sympy as sp
import mpmath as mp

fails = []
def chk(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok:
        fails.append(name)

beta, k, u, T, xi = sp.symbols('beta k u T xi', positive=True)
n = sp.symbols('n', integer=True, positive=True)
RHO = sp.pi**2 / (30 * beta**4)

# (1) Route A: Bose mode sum.  rho = INT d^3k/(2pi)^3 omega n_B(omega), omega = |k|, k = x/beta.
#     sympy cannot integrate the Bose integrand in closed form, so it is done term by term:
#     1/(e^x - 1) = SUM_{n>=1} e^{-n x}  (x > 0), INT_0^oo x^s e^{-n x} dx = s!/n^(s+1)  -- both by sympy -- and
#     the result is cross-checked by mpmath quadrature of the untouched integrand.
x = sp.symbols('x', positive=True)
def bose(s):   # INT_0^oo x^s/(e^x - 1) dx
    term = sp.integrate(x**s * sp.exp(-n * x), (x, 0, sp.oo), conds='none')
    return sp.simplify(sp.summation(term, (n, 1, sp.oo)))
I3 = bose(3)
mp.mp.dps = 30
I3num = mp.quad(lambda y: y**3 / (mp.exp(y) - 1), [0, mp.inf])
chk("A: INT x^3/(e^x-1) = 6 zeta(4) = pi^4/15 (sympy series), = quadrature to 1e-25",
    sp.simplify(I3 - sp.pi**4 / 15) == 0 and abs(I3num - mp.pi**4 / 15) < mp.mpf('1e-25'))
rhoA = 4 * sp.pi * I3 / beta**4 / (2 * sp.pi)**3
chk("A: mode sum (1/2pi^2) INT k^3/(e^{beta k}-1) dk = pi^2/(30 beta^4)", sp.simplify(rhoA - RHO) == 0)
pA = 4 * sp.pi * (I3 / 3) / beta**4 / (2 * sp.pi)**3      # kinetic stress k^2/(3 omega) = k/3
chk("A: p = rho/3 from the kinetic stress k^2/(3 omega)", sp.simplify(pA / rhoA - sp.Rational(1, 3)) == 0)
# thermodynamic route: f = (1/beta) INT d^3k/(2pi)^3 ln(1-e^{-beta k}); ln(1-e^{-x}) = -SUM e^{-nx}/n
L2 = sp.simplify(-sp.summation(sp.integrate(x**2 * sp.exp(-n * x), (x, 0, sp.oo), conds='none') / n, (n, 1, sp.oo)))
L2num = mp.quad(lambda y: y**2 * mp.log(1 - mp.exp(-y)), [0, mp.inf])
chk("A': INT x^2 ln(1-e^-x) = -2 zeta(4) = -pi^4/45 (sympy series), = quadrature to 1e-25",
    sp.simplify(L2 + sp.pi**4 / 45) == 0 and abs(L2num + mp.pi**4 / 45) < mp.mpf('1e-25'))
f = 4 * sp.pi * L2 / beta**3 / (2 * sp.pi)**3 / beta
rhoTh = sp.diff(beta * f, beta)
chk("A': thermodynamic p = -f = pi^2/(90 beta^4)", sp.simplify(-f - sp.pi**2 / (90 * beta**4)) == 0)
chk("A': thermodynamic rho = d(beta f)/d beta = pi^2/(30 beta^4)  (Boltzmann's rho = 3p follows)", sp.simplify(rhoTh - RHO) == 0)

# (2) Route B: imaginary-time image sum of the free massless Wightman function
#     W(x) = 1/(4 pi^2 sigma), sigma = -(t)^2 + r^2, thermal = SUM_{n != 0} W(t + i n beta)  (renormalised: n=0 dropped).
dt, dx, dy, dz = sp.symbols('dt dx dy dz', real=True)
D = (dt, dx, dy, dz)
sig = -(dt + sp.I * n * beta)**2 + dx**2 + dy**2 + dz**2
G = sp.zeros(4, 4)
for A in range(4):
    for B in range(A, 4):
        t = -sp.diff(1 / (4 * sp.pi**2 * sig), D[A], D[B])      # <:d_A phi d_B phi:> term, x'->x
        t = sp.simplify(t.subs({dt: 0, dx: 0, dy: 0, dz: 0}))
        G[A, B] = G[B, A] = sp.simplify(2 * sp.summation(t, (n, 1, sp.oo)))
rhoB = sp.simplify((G[0, 0] + G[1, 1] + G[2, 2] + G[3, 3]) / 2)   # T00 = (phidot^2 + |grad phi|^2)/2
chk("B: image-sum rho = pi^2/(30 beta^4)", sp.simplify(rhoB - RHO) == 0)
pB = [sp.simplify(G[i, i] + (G[0, 0] - sum(G[j, j] for j in (1, 2, 3))) / 2) for i in (1, 2, 3)]
chk("B: image-sum p_i = rho/3, i = 1,2,3", all(sp.simplify(p / rhoB - sp.Rational(1, 3)) == 0 for p in pB))
chk("B: <:phidot^2:> = <:|grad phi|^2:> (massless equipartition), so g(0) = rho",
    sp.simplify(G[0, 0] - (G[1, 1] + G[2, 2] + G[3, 3])) == 0 and sp.simplify(G[0, 0] - RHO) == 0)
chk("B: off-diagonal G_AB = 0 (isotropy, rest frame)",
    all(sp.simplify(G[A, B]) == 0 for A in range(4) for B in range(4) if A != B))
# canonical (minimal) trace T^mu_mu = -(d phi)^2 -> <:.:> = G00 - sum Gii = 0
chk("B: minimal-coupling trace <:T^mu_mu:> = <:phidot^2:> - <:|grad phi|^2:> = 0", sp.simplify(G[0, 0] - sum(G[i, i] for i in (1, 2, 3))) == 0)

# (3) xi-independence in flat space.  Improvement term xi (eta_mn Box - d_m d_n) <:phi^2:>_beta:
phi2 = sp.simplify(2 * sp.summation(1 / (4 * sp.pi**2 * (n * beta)**2), (n, 1, sp.oo)))
chk("C: <:phi^2:>_beta = 1/(12 beta^2)  (x-independent)", sp.simplify(phi2 - 1 / (12 * beta**2)) == 0)
chk("C: improvement term vanishes -> flat-space thermal rho is xi-INDEPENDENT (derivatives of a constant)",
    all(sp.diff(phi2, v) == 0 for v in D))
# 2512.15610 eq (33) prints |T00| = pi^2 (1+xi)/(30 beta^4); at xi = 1/6 that is 7/6 of the value derived here.
ratio = (1 + sp.Rational(1, 6))
chk("C: 2512.15610 eq(33) at xi=1/6 differs from the xi-independent value by factor 7/6 (DISCREPANCY there, not in the tree: tree uses xi=0)",
    ratio == sp.Rational(7, 6))

# (4) noise.py's closed form g(u) = -(1/2pi^2) d^3/du^3 [(pi/2beta)coth(pi u/beta) - 1/(2u)]
base = sp.pi / (2 * beta) * sp.coth(sp.pi * u / beta) - 1 / (2 * u)
g = -sp.diff(base, u, 3) / (2 * sp.pi**2)
chk("D: lim_{u->0} g(u) = pi^2/(30 beta^4)", sp.simplify(sp.limit(g.subs(beta, 1), u, 0) - sp.pi**2 / 30) == 0)
chk("D: lim_{u->oo} u^4 g(u) = -3/(2 pi^2)", sp.simplify(sp.limit(g.subs(beta, 1) * u**4, u, sp.oo) + 3 / (2 * sp.pi**2)) == 0)
mp.mp.dps = 30
uu = mp.mpf('0.7')
direct = mp.quad(lambda kk: kk**3 * mp.cos(kk * uu) / (mp.exp(kk) - 1), [0, mp.inf]) / (2 * mp.pi**2)
gf = sp.lambdify(u, g.subs(beta, 1), 'mpmath')
chk("D: closed form g(0.7) = its mode integral (1/2pi^2) INT k^3 cos(ku)/(e^k-1) dk, 1e-20", abs(gf(uu) - direct) < mp.mpf('1e-20'))

# (5) Hypotheses matter: mass lowers rho (so 'massless' is load-bearing), photons are 2 dof.
def rho_massive(mT):
    m = mp.mpf(mT)
    return mp.quad(lambda kk: kk**2 * mp.sqrt(kk**2 + m**2) / (mp.exp(mp.sqrt(kk**2 + m**2)) - 1), [0, mp.inf]) / (2 * mp.pi**2)
r1 = rho_massive(1) / (mp.pi**2 / 30)
print("      massive scalar, m/T = 1: rho/rho_SB = %s" % mp.nstr(r1, 12))
chk("E: m/T = 1 gives rho < rho_SB (massless hypothesis is load-bearing)", r1 < 1)
chk("E: m/T -> 0 recovers rho_SB (1e-6 at m/T = 1e-4)", abs(rho_massive('1e-4') / (mp.pi**2 / 30) - 1) < mp.mpf('1e-6'))
# photon: 2 polarisations -> u = pi^2 T^4/15 ; sigma = c u /(4 T^4) in SI with exact 2019-SI h, k, c
h = mp.mpf('6.62607015e-34'); kB = mp.mpf('1.380649e-23'); c = mp.mpf('299792458')
sigma = 2 * mp.pi**5 * kB**4 / (15 * h**3 * c**2)
print("      sigma (2019 SI, exact inputs) = %s W m^-2 K^-4" % mp.nstr(sigma, 12))
chk("E: sigma = 2 pi^5 k^4/(15 h^3 c^2) = 5.670374419e-8 (CODATA-quoted, 10 sig. fig.)", abs(sigma / mp.mpf('5.670374419e-8') - 1) < mp.mpf('1e-9'))
# the scalar-per-dof coefficient is half the photon coefficient
chk("E: per-dof coefficient pi^2/30 = (photon pi^2/15)/2", sp.Rational(1, 30) * 2 == sp.Rational(1, 15))

# (6) consequence the tree draws from it: thermal Delta' = 2/3 (fluctuation.py:87-95, 465-468)
#     Delta' = SUM_AB G_AB^2 / (2 rho^2) for a zero-mean Gaussian state (KF (3.40)-(3.43), normal-ordered, coincident)
Dp = sp.simplify(sum(G[A, B]**2 for A in range(4) for B in range(4)) / (2 * rhoB**2))
chk("F: thermal Delta' = 2/3, Delta = Delta'/(1+Delta') = 2/5", Dp == sp.Rational(2, 3) and sp.simplify(Dp / (1 + Dp)) == sp.Rational(2, 5))

# (7) SCOPE, not SB itself: the tree calls the scalar model "ordinary blackbody radiation" (fluctuation.py:89)
#     and its quanta "photons" (noise.py:136).  Same Gaussian machinery for the free EM field:
#     for a zero-mean Gaussian vector v with (normal-ordered) covariance C, Var(v^T v / 2) = tr(C^2)/2 (Wick).
#     Control: scalar v = (phidot, grad phi), C = G  ->  Var/rho^2 must reproduce 2/3.
rho = sp.symbols('rho', positive=True)
def wick_var(C):
    return sp.simplify(sum(C[a, b]**2 for a in range(C.shape[0]) for b in range(C.shape[1])) / 2)
Cs = sp.diag(rho, rho / 3, rho / 3, rho / 3)
chk("G: Wick Var(v^T v/2) = tr C^2/2 reproduces the scalar Delta' = 2/3 (control)", sp.simplify(wick_var(Cs) / rho**2) == sp.Rational(2, 3))
# explicit Wick check of Var(v^T v/2) = tr C^2/2 on a generic symmetric 2x2 (4th moments of a Gaussian)
a11, a12, a22 = sp.symbols('a11 a12 a22', real=True)
C2 = sp.Matrix([[a11, a12], [a12, a22]])
def m4(i, j, k, l):  # Isserlis
    return C2[i, j] * C2[k, l] + C2[i, k] * C2[j, l] + C2[i, l] * C2[j, k]
EX2 = sum(m4(i, i, j, j) for i in range(2) for j in range(2)) / 4
EX = (a11 + a22) / 2
chk("G: Isserlis: Var(v^T v/2) = tr C^2/2 for a generic 2x2 covariance", sp.expand(EX2 - EX**2 - wick_var(C2)) == 0)
# EM thermal, coincident, isotropic, rest frame: <:E_iE_j:> = <:B_iB_j:> = delta_ij rho/3, <:E_iB_j:> = 0
Cem = sp.diag(*([rho / 3] * 6))
DpEM = sp.simplify(wick_var(Cem) / rho**2)
print("      EM thermal: Delta' = %s, Delta = %s   (scalar: 2/3, 2/5)" % (DpEM, sp.simplify(DpEM / (1 + DpEM))))
chk("G: EM thermal Delta' = 1/3, Delta = 1/4 -- still O(1), but NOT the scalar 2/3, 2/5 (scalar-model numbers do not transfer)",
    DpEM == sp.Rational(1, 3) and sp.simplify(DpEM / (1 + DpEM)) == sp.Rational(1, 4))
# EM analogue of T1: 6 components, tr C = 2 rho -> tr C^2 >= (2 rho)^2/6 -> Delta' >= 1/3; thermal EM saturates it
chk("G: EM Cauchy-Schwarz floor tr C^2/2 >= (tr C)^2/12 = rho^2/3, saturated by thermal EM", sp.simplify(wick_var(Cem) - (6 * rho / 3)**2 / 12) == 0)

print("\n%d FAIL" % len(fails))
sys.exit(1 if fails else 0)
