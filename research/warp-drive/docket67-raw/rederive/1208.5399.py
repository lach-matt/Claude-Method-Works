#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key 1208.5399 (Fewster, Lectures on QEIs).

Checks, each printed PASS/FAIL, exit 1 on any FAIL:
  A. Eq.(4): the least eigenvalue of d^4/dt^4 on [0,1] with clamped ends
     (g = g' = 0 at both ends) is mu_1^4 with cos(mu) cosh(mu) = 1 (sympy
     determinant of the 4x4 boundary system), mu_1 to 30 digits, and
     C = mu_1^4/(16 pi^2) reproduces Fewster's printed 'C ~ 3.17' and
     '0.20/l^4' (C/16).  Independently: a Galerkin Rayleigh-quotient upper
     bound over W^{2,2}_0 polynomials x^2(1-x)^2 P(x) converges DOWN onto
     mu_1^4 (the variational content of Eq.(4)).
  B. The constant c_2 = 16 pi^2 of the Fewster-Teo form (gr-qc/9908073
     eq. 1.3, m = 2) equals the 16 pi^2 of Fewster's Eq.(3).
  C. Casimir density for the massless MINIMALLY coupled scalar between
     Dirichlet plates at z = +-L/2:
       (i)  <phi^2>_ren by the image sum = 1/(48 L^2) - 1/(16 L^2 cos^2(pi z/L))
            (numeric check of sum_n 1/(u-n)^2 = pi^2/sin^2(pi u));
       (ii) T00^min = T00^conf + (1/6) d^2/dz^2 <phi^2>  (flat, static,
            signature +---, improvement term -xi Laplacian phi^2; sign fixed
            by tracelessness at xi = 1/6, checked symbolically);
       (iii) the uniform conformal part: zeta-regularised mode sum gives
            E/A = -pi^2/(1440 L^3) (Dirichlet) and the periodic a = 2L image
            family gives -pi^2/(90 a^4) = -pi^2/(1440 L^4);
     => the constant is 1440.  Fewster's text layer prints 1140; the tree
     copies 1140 (bounds.py:347,350).  RECORDED AS A DISCREPANCY.
  D. The fraction rho_Casimir / (C/(2l)^4), l = L/2 - |z|, with 1140 and
     with 1440: midpoint, z/L = 0.2, 0.4, the plate limit 16/mu_1^4
     (closed form), monotonicity, and whether Fewster's '3-7%' holds.
     Also bounds.py's selftest pin near(mid, 0.0682, rel 1e-2) under each.
  E. The tree's downstream arithmetic that imports C (achievable.py):
     allowed C hbar/(c^3 T^4) at T = b/c, b = 1 m; demanded
     3 mu c^4/(4 pi G alpha^3 b^2); log10 ratio = 71.256; with CODATA 2022.
"""
import sys
import mpmath as mp
import sympy as sp

mp.mp.dps = 40
FAILS = []


def check(name, cond, detail=""):
    print("  [%s] %s %s" % ("PASS" if cond else "FAIL", name, detail))
    if not cond:
        FAILS.append(name)


print("A. Eq.(4): clamped-beam eigenvalue and C")
t, k = sp.symbols('t k', positive=True)
# general solution of g'''' = k^4 g
a1, a2, a3, a4 = sp.symbols('a1:5')
g = a1*sp.cos(k*t) + a2*sp.sin(k*t) + a3*sp.cosh(k*t) + a4*sp.sinh(k*t)
eqs = [g.subs(t, 0), sp.diff(g, t).subs(t, 0), g.subs(t, 1), sp.diff(g, t).subs(t, 1)]
M = sp.Matrix([[sp.diff(e, v) for v in (a1, a2, a3, a4)] for e in eqs])
det = sp.simplify(sp.expand_trig(M.det()))
target = 2*k**2*(1 - sp.cos(k)*sp.cosh(k))  # det = 2 k^2 (1 - cos k cosh k)
ratio = sp.simplify(det/target)
print("     det(boundary matrix) =", det, "; det / [2k^2(1 - cos k cosh k)] =", ratio)
check("A1 boundary determinant vanishes iff cos(k)cosh(k) = 1",
      ratio.is_constant() and ratio != 0)
mu1 = mp.findroot(lambda m: mp.cos(m)*mp.cosh(m) - 1, 4.73)
C = mu1**4/(16*mp.pi**2)
print("     mu_1 =", mp.nstr(mu1, 30))
print("     C    =", mp.nstr(C, 30))
check("A2 mu_1 matches tree FEWSTER_MU1 = 4.730040744862704",
      abs(mu1 - mp.mpf('4.730040744862704')) < 1e-14)
check("A3 C matches tree FEWSTER_C = 3.169857938310467",
      abs(C - mp.mpf('3.169857938310467')) < 1e-14)
check("A4 C rounds to Fewster's printed 'C ~ 3.17'", round(float(C), 2) == 3.17)
check("A5 C/16 rounds to Fewster's printed '0.20/l^4'", round(float(C/16), 2) == 0.20,
      "(C/16 = %.5f)" % float(C/16))
# no smaller root on (0, 4.73): scan sign of cos cosh - 1
xs = [mp.mpf(i)/1000 for i in range(1, 4730)]
signs = [mp.sign(mp.cos(x)*mp.cosh(x) - 1) for x in xs]
check("A6 no root of cos(k)cosh(k)=1 on (0, mu_1): mu_1 is the FIRST",
      all(s == signs[0] for s in signs))
# Galerkin Rayleigh quotient over x^2(1-x)^2 * polynomials, degree N
x = sp.symbols('x')
lam_mu4 = mu1**4
prev = None
galerkin = []
for N in (1, 2, 4, 6, 8):
    basis = [x**2*(1-x)**2*x**j for j in range(N)]
    A = sp.Matrix(N, N, lambda i, j: sp.integrate(sp.diff(basis[i], x, 2)*sp.diff(basis[j], x, 2), (x, 0, 1)))
    B = sp.Matrix(N, N, lambda i, j: sp.integrate(basis[i]*basis[j], (x, 0, 1)))
    Am = mp.matrix([[mp.mpf(sp.Rational(A[i, j]).p)/sp.Rational(A[i, j]).q for j in range(N)] for i in range(N)])
    Bm = mp.matrix([[mp.mpf(sp.Rational(B[i, j]).p)/sp.Rational(B[i, j]).q for j in range(N)] for i in range(N)])
    # generalized eigenproblem via Cholesky of B
    Lc = mp.cholesky(Bm)
    Li = Lc**-1
    S = Li*Am*Li.T
    ev = mp.eigsy(S)[0]
    lmin = min(ev[i] for i in range(N))
    galerkin.append((N, lmin))
    print("     Galerkin N=%d: min Rayleigh quotient = %s  (mu_1^4 = %s)" %
          (N, mp.nstr(lmin, 15), mp.nstr(lam_mu4, 15)))
    check("A7.%d Rayleigh upper bound >= mu_1^4 (variational)" % N, lmin >= lam_mu4 - mp.mpf('1e-20'))
    if prev is not None:
        check("A8.%d monotone decrease toward mu_1^4" % N, lmin <= prev + mp.mpf('1e-25'))
    prev = lmin
check("A9 Galerkin N=8 within 1e-8 relative of mu_1^4",
      abs(galerkin[-1][1]/lam_mu4 - 1) < 1e-8, "(rel %s)" % mp.nstr(galerkin[-1][1]/lam_mu4 - 1, 3))
# N=1 closed form: g = x^2(1-x)^2 gives 504 (> 500.56)
check("A10 N=1 trial x^2(1-x)^2 gives exactly 504", abs(galerkin[0][1] - 504) < 1e-25)

print("B. Fewster-Teo c_2")
m = 2
c2 = m*sp.pi**(sp.Rational(2*m-1, 2))*2**(2*m)*sp.gamma(m - sp.Rational(1, 2))
check("B1 c_2 = 16 pi^2", sp.simplify(c2 - 16*sp.pi**2) == 0, "(c_2 = %s)" % sp.simplify(c2))

print("C. Casimir density, massless minimally coupled scalar, Dirichlet plates")
# (i) image sum identity, numerically at several u
for u in (mp.mpf('0.1'), mp.mpf('0.37'), mp.mpf('0.5')):
    lhs = mp.nsum(lambda n: 1/(u-n)**2, [-mp.inf, mp.inf])
    rhs = mp.pi**2/mp.sin(mp.pi*u)**2
    check("C1 sum 1/(u-n)^2 = pi^2/sin^2(pi u) at u=%s" % mp.nstr(u, 3), abs(lhs-rhs) < 1e-25)
# <phi^2>_ren(xp) = (1/4pi^2)[ sum_{n!=0} 1/(2nL)^2 - sum_n 1/(2xp-2nL)^2 ]
#   = (1/(16 pi^2 L^2))[ pi^2/3 - pi^2/sin^2(pi xp/L) ],  xp = z + L/2
z, L, xi = sp.symbols('z L xi', real=True)
phi2 = sp.Rational(1, 48)/L**2 - 1/(16*L**2*sp.cos(sp.pi*z/L)**2)
xp_check = sp.simplify((sp.pi**2/3 - sp.pi**2/sp.sin(sp.pi*(z + L/2)/L)**2)/(16*sp.pi**2*L**2) - phi2)
check("C2 image-sum <phi^2> = 1/(48L^2) - 1/(16 L^2 cos^2(pi z/L))", xp_check == 0)
check("C2b zeta(2) term: 2 zeta(2)/(16 pi^2) = 1/48", sp.simplify(2*sp.zeta(2)/(16*sp.pi**2) - sp.Rational(1, 48)) == 0)
# (ii) improvement-term sign: trace of T_ab^xi on shell, flat +---
# T_ab = d_a phi d_b phi - 1/2 eta_ab (dphi)^2 + xi (eta_ab box - d_a d_b) phi^2
# trace: -(dphi)^2 + 3 xi box(phi^2) = -(dphi)^2 + 6 xi (dphi)^2 on shell
dphi2 = sp.symbols('dphi2')
trace = -dphi2 + 3*xi*(2*dphi2)
check("C3 improvement sign: trace vanishes iff xi = 1/6", sp.solve(trace, xi) == [sp.Rational(1, 6)])
# T00 improvement (static) = xi (eta_00 box - d_t^2) phi^2 = -xi Laplacian phi^2
min_minus_conf = sp.Rational(1, 6)*sp.diff(phi2, z, 2)
fewster_term = -sp.pi**2/(48*L**4)*(3 - 2*sp.cos(sp.pi*z/L)**2)/sp.cos(sp.pi*z/L)**4
check("C4 T00^min - T00^conf = -pi^2/(48 L^4)(3 - 2cos^2)/cos^4 (Fewster's second term, sign and all)",
      sp.simplify(min_minus_conf - fewster_term) == 0)
# (iii) the constant
a = sp.symbols('a', positive=True)
EA_dir = -(1/(12*sp.pi))*(sp.pi/L)**3*sp.zeta(-3)  # (1/2) sum_n int d^2k/(2pi)^2 sqrt(k^2+(n pi/L)^2), n>=1
check("C5 Dirichlet zeta mode sum: E/A = -pi^2/(1440 L^3)", sp.simplify(EA_dir + sp.pi**2/(1440*L**3)) == 0)
EA_per = -(1/(12*sp.pi))*2*(2*sp.pi/a)**3*sp.zeta(-3)  # periodic, n in Z\{0}
rho_per = sp.simplify(EA_per/a)
check("C6 periodic image family: rho = -pi^2/(90 a^4)", sp.simplify(rho_per + sp.pi**2/(90*a**4)) == 0)
check("C7 at a = 2L: -pi^2/(1440 L^4)", sp.simplify(rho_per.subs(a, 2*L) + sp.pi**2/(1440*L**4)) == 0)
# single-plate reflected images carry zero conformal T by symmetry (T_zz const by conservation,
# O(1/z^4) by dimension => T_zz = 0; T_ab = A eta_ab/z^4 on (t,x,y); traceless => A = 0): recorded, not coded.
check("C8 the correct constant is 1440, NOT the 1140 printed (DISCREPANCY, recorded)", 1440 != 1140)

print("D. Fraction of Fewster's a priori bound")
def frac(zL, const):
    zL = mp.mpf(zL)
    rho = -mp.pi**2/const - mp.pi**2/48*(3 - 2*mp.cos(mp.pi*zL)**2)/mp.cos(mp.pi*zL)**4
    ell = mp.mpf(1)/2 - abs(zL)
    return rho/(-C/(2*ell)**4)

plate_limit = 16/mu1**4
print("     plate limit 16/mu_1^4 = %s" % mp.nstr(plate_limit, 12))
for const in (1140, 1440):
    vals = {zl: frac(zl, const) for zl in ('0', '0.2', '0.4', '0.49', '0.4999')}
    print("     const %d: " % const + ", ".join("z/L=%s -> %.6f" % (k_, float(v)) for k_, v in vals.items()))
    grid = [frac(mp.mpf(i)/2000, const) for i in range(0, 1000)]
    mono = all(grid[i+1] < grid[i] for i in range(len(grid)-1))
    check("D1.%d fraction decreases monotonically from midpoint to plate" % const, mono)
    check("D2.%d range [plate limit, midpoint] within Fewster's '3-7%%'" % const,
          0.03 <= float(plate_limit) and float(vals['0']) <= 0.07,
          "(%.4f%% .. %.4f%%)" % (100*float(plate_limit), 100*float(vals['0'])))
    check("D3.%d plate limit is 16/mu_1^4 (const-independent)" % const,
          abs(frac('0.499999', const) - plate_limit) < 1e-8)
    rel = abs(float(vals['0'])/0.0682 - 1)
    print("     bounds.py pin near(mid, 0.0682, rel 1e-2) under %d: |rel| = %.4f -> %s"
          % (const, rel, "passes" if rel <= 1e-2 else "WOULD FAIL"))
m1140, m1440 = frac('0', 1140), frac('0', 1440)
check("D4 tree's midpoint 0.067597 reproduced with 1140", abs(m1140 - mp.mpf('0.067597')) < 5e-7,
      "(%.7f)" % float(m1140))
check("D5 tree's z/L=0.4 value 0.031976 reproduced with 1140", abs(frac('0.4', 1140) - mp.mpf('0.031976')) < 5e-7)
print("     misprint moves midpoint %.4f%% -> %.4f%% (delta %.4f points); '3-7%%' unmoved"
      % (100*float(m1140), 100*float(m1440), 100*float(m1140 - m1440)))
check("D6 pin 0.0682 passes on 1140 and would fail on 1440 (a selftest keyed to the misprint)",
      abs(float(m1140)/0.0682 - 1) <= 1e-2 and abs(float(m1440)/0.0682 - 1) > 1e-2)

print("E. Tree's imported downstream arithmetic (achievable.py), CODATA 2022")
hbar = mp.mpf('1.054571817e-34')   # exact (SI 2019)
c = mp.mpf(299792458)              # exact
G = mp.mpf('6.67430e-11')          # CODATA 2018 = CODATA 2022 central value
mu_, alpha, b = mp.mpf('5e-3'), mp.mpf('0.02'), mp.mpf(1)
T = b/c
allowed = C*hbar/(c**3*T**4)
demanded = 3*mu_*c**4/(4*mp.pi*G*alpha**3*b**2)
S = demanded/allowed
print("     allowed  = %s Pa ; demanded = %s Pa ; log10 S = %s"
      % (mp.nstr(allowed, 10), mp.nstr(demanded, 10), mp.nstr(mp.log10(S), 8)))
check("E1 allowed matches tree 1.002159073400914e-25", abs(allowed/mp.mpf('1.002159073400914e-25') - 1) < 1e-12)
check("E2 demanded matches tree 1.8057952e46", abs(demanded/mp.mpf('1.8057952e46') - 1) < 1e-7)
check("E3 log10 S = 71.256 (3 d.p.)", round(float(mp.log10(S)), 3) == 71.256)
# G uncertainty 1.5e-15 relative 2.2e-5 -> shift in log10 S
dlog = float(mp.log10(1 + mp.mpf('2.2e-5')))
check("E4 CODATA G uncertainty moves log10 S by < 1e-4", dlog < 1e-4, "(%.2e)" % dlog)

print()
print("RESULT: %d FAIL(s)%s" % (len(FAILS), (": " + ", ".join(FAILS)) if FAILS else ""))
sys.exit(1 if FAILS else 0)
