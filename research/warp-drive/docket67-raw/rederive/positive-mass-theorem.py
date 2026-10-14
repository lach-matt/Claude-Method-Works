#!/usr/bin/env python3
"""
DOCKET 67 -- rederivation for key 'positive-mass-theorem'.

Checks (G = c = 1, n = 3):
 C1  ADM energy E = (1/16pi) lim oint (g_ij,i - g_ii,j) nu^j dS  [EHLS 1110.2087 Def.3, n=3]
     for conformally flat slices g = psi(r) delta: E = lim -(1/2) r^2 psi'(r).
     Applied to (a) composite.py/concentric.py slice psi = 1 - 2 Phi with
     Phi = m/sqrt(r^2+a^2) - m/max(r,R_s)  -> E = 0 exactly;
     (b) concentric.py's 'first (wrong) potential'  -> E = -m;
     (c) linearised Schwarzschild Phi = -M/r -> E = M;
     (d) isotropic Schwarzschild psi = (1+M/2rho)^4 -> E = M for either sign of M.
 C2  Scalar curvature of the static slice g = dr^2/(1-2m(r)/r) + r^2 dOmega^2 is 4 m'/r^2.
     Constant NEGATIVE density ball (m = -(4pi/3) rho0 r^3 inside R, M<0 outside):
     smooth regular centre, complete, asymptotically flat, E_ADM = M < 0, and
     mu = R/2 = 8 pi rho < 0: DEC (indeed R >= 0) fails.  An explicit datum
     with NEGATIVE ADM mass that the positive mass theorem does not forbid.
 C3  Exact scalar curvature of the concentric slice g = psi delta, psi = 1-2Phi(r):
     R = 4 Lap(Phi)/psi^2 + 6 |grad Phi|^2/psi^3 (sympy, radial), evaluated at the
     tree's design point (m=5e-3, a=0.02, R_s=200): R < 0 at the core, so the
     time-symmetric hypothesis R_g >= 0 (the DEC on a K=0 slice) FAILS.
 C4  z3: the theorem as an implication H -> (E>=0 and (E=0 -> flat)); which
     of the tree's four uses follow.
 C5  overturn.py two-zone numbers and the 2m/r of that profile read as areal data.
 C6  concentric.py numbers: Phi(1) at m=5e-3, Phi(1000), bad(1000).
"""
import math, sys
import sympy as sp
import z3

ok = True
def chk(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "FAIL", label, detail))

r, m, a, Rs, M, rho0, R = sp.symbols('r m a R_s M rho0 R', positive=True)
Ms = sp.symbols('M_s', real=True)

print("C1  ADM energy of conformally flat slices")
# generic: g_ij = psi(r) delta_ij in Cartesian; g_ij,i - g_ii,j = psi_,j - 3 psi_,j = -2 psi_,j
psi = sp.Function('psi')
x, y, z = sp.symbols('x y z', real=True)
rr = sp.sqrt(x**2+y**2+z**2)
g = sp.eye(3)*psi(rr)
X = [x, y, z]
flux = [sum(sp.diff(g[i, j], X[i]) for i in range(3)) - sum(sp.diff(g[i, i], X[j]) for i in range(3)) for j in range(3)]
nu_flux = sp.simplify(sum(flux[j]*X[j]/rr for j in range(3)))
# nu.flux should be -2 psi'(r)
test = sp.simplify(nu_flux.subs(psi(rr), sp.Function('q')(rr)))
radial = sp.simplify(nu_flux.subs({x: r, y: 0, z: 0}))
print("   nu^j (g_ij,i - g_ii,j) at (r,0,0) =", radial)
chk("flux integrand = -2 psi'(r)", sp.simplify(radial + 2*sp.diff(psi(r), r)) == 0)
E_of = lambda ps: sp.limit(-sp.Rational(1, 2)*r**2*sp.diff(ps, r), r, sp.oo)  # (1/16pi)*4pi r^2*(-2psi')
Phi_out = m/sp.sqrt(r**2+a**2) - m/r          # concentric, r > R_s
E_conc = E_of(1-2*Phi_out)
chk("(a) concentric slice, r > R_s: E_ADM = 0", sp.simplify(E_conc) == 0, "E = %s" % E_conc)
Phi_bad = m/sp.sqrt(r**2+a**2) - m/Rs
E_bad = E_of(1-2*Phi_bad)
chk("(b) first (wrong) potential: E_ADM = -m", sp.simplify(E_bad + m) == 0, "E = %s" % E_bad)
E_lin = E_of(1-2*(-M/r))
chk("(c) linearised Schwarzschild Phi=-M/r: E = M", sp.simplify(E_lin - M) == 0)
E_iso = E_of((1+Ms/(2*r))**4)
chk("(d) isotropic Schwarzschild, either sign of M: E = M", sp.simplify(E_iso - Ms) == 0, "E = %s" % E_iso)
# fall-off of g - delta for the concentric slice: -2 Phi_out ~ m a^2 / r^3
lead = sp.series(-2*Phi_out, r, sp.oo, 4)
print("   g - delta for r > R_s ~", lead)
chk("concentric g - delta = O(r^-3): within EHLS q in (1/2,1)",
    sp.limit(r**3*(-2*Phi_out), r, sp.oo) == m*a**2)

print("\nC2  negative-mass constant-density ball is admissible data with E < 0")
mf = sp.Function('mf')
th, ph = sp.symbols('theta phi')
def scalar_curv(gmat, coords):
    n = len(coords); gi = gmat.inv()
    Gam = [[[sum(gi[l, s]*(sp.diff(gmat[s, i], coords[j]) + sp.diff(gmat[s, j], coords[i]) - sp.diff(gmat[i, j], coords[s]))
                 for s in range(n))/2 for j in range(n)] for i in range(n)] for l in range(n)]
    Ric = sp.zeros(n)
    for i in range(n):
        for j in range(n):
            Ric[i, j] = sum(sp.diff(Gam[l][i][j], coords[l]) - sp.diff(Gam[l][i][l], coords[j])
                            + sum(Gam[l][l][s]*Gam[s][i][j] - Gam[l][j][s]*Gam[s][i][l] for s in range(n))
                            for l in range(n))
    return sp.simplify(sum(gi[i, j]*Ric[i, j] for i in range(n) for j in range(n)))
gMS = sp.diag(1/(1-2*mf(r)/r), r**2, r**2*sp.sin(th)**2)
Rms = scalar_curv(gMS, [r, th, ph])
chk("R[dr^2/(1-2m/r) + r^2 dOmega^2] = 4 m'/r^2", sp.simplify(Rms - 4*sp.diff(mf(r), r)/r**2) == 0, "R = %s" % Rms)
m_in = -sp.Rational(4, 3)*sp.pi*rho0*r**3
chk("inside the ball R = -16 pi rho0 < 0 (mu = R/2 < 0: DEC fails)",
    sp.simplify(4*sp.diff(m_in, r)/r**2 + 16*sp.pi*rho0) == 0)
chk("1 - 2m/r = 1 + (8pi/3) rho0 r^2 > 0 everywhere: no horizon, regular centre (m = O(r^3))",
    sp.simplify(1 - 2*m_in/r - (1 + sp.Rational(8, 3)*sp.pi*rho0*r**2)) == 0)
Mval = sp.limit(m_in, r, R)   # = M < 0, the exterior Schwarzschild mass, = E_ADM by C1(d)
print("   E_ADM = m(R) = %s  (< 0)" % Mval)
chk("ADM energy negative", sp.simplify(Mval).subs({rho0: 1, R: 1}) < 0)
# numeric: rho0 = 1e-3, R = 1 -> M, check g_rr finite and positive on a grid
rho0n, Rn = 1e-3, 1.0
Mn = -4/3*math.pi*rho0n*Rn**3
grr = [1/(1-2*(-4/3*math.pi*rho0n*rv**3 if rv < Rn else Mn)/rv) for rv in [1e-3*k for k in range(1, 5001)]]
chk("g_rr in (0,1] on r in (0,5]: the slice CONTRACTS (certify.py's m<0 signature)",
    all(0 < v <= 1 for v in grr), "M = %.6e" % Mn)

print("\nC3  scalar curvature of the concentric slice g = (1-2Phi) delta")
Phi = sp.Function('Phi')
gC = sp.diag(1-2*Phi(r), (1-2*Phi(r))*r**2, (1-2*Phi(r))*r**2*sp.sin(th)**2)
RC = scalar_curv(gC, [r, th, ph])
lap = sp.diff(Phi(r), r, 2) + 2*sp.diff(Phi(r), r)/r
formula = 4*lap/(1-2*Phi(r))**2 + 6*sp.diff(Phi(r), r)**2/(1-2*Phi(r))**3
chk("R = 4 Lap Phi/psi^2 + 6 |Phi'|^2/psi^3", sp.simplify(RC - formula) == 0)
mn, an, Rsn = 5e-3, 0.02, 200.0
Phi_in = m/sp.sqrt(r**2+a**2) - m/Rs                  # r < R_s
Rin = sp.simplify(formula.subs(Phi(r), Phi_in).doit())
fR = sp.lambdify(r, Rin.subs({m: mn, a: an, Rs: Rsn}), 'math')
R0 = fR(1e-9)
est = -12*mn/an**3/(1-2*(mn/an - mn/Rsn))**2
print("   R(r->0) = %.6e ; closed form 4*Lap(Phi)(0)/psi(0)^2 = -12 m/a^3/(1-2m/a+2m/R_s)^2 = %.6e" % (R0, est))
chk("R < 0 at the core: the static (K=0) hypothesis R_g >= 0 fails", R0 < 0)
chk("R(0) equals the closed form (psi(0) = 0.5: Phi_max = m/a = 0.25 is NOT small)", abs(R0/est - 1) < 1e-6, "ratio %.9f" % (R0/est))
Rcorr = fR(1.0)
print("   R(r=1, the corridor) = %+.4e  (> 0 there: the 6|Phi'|^2 term and the Plummer tail)" % Rcorr)
# integrated sign: int R dV_g over the core region r < 10 a
vol = lambda rv: (1-2*float(Phi_in.subs({m: mn, a: an, Rs: Rsn, r: rv})))**1.5*4*math.pi*rv*rv
N = 4000; h = 10*an/N
I = sum(fR((k+0.5)*h)*vol((k+0.5)*h)*h for k in range(N))
print("   int_{r<10a} R dV = %.6e" % I)
chk("core integral of R negative", I < 0)

print("\nC4  z3: what the theorem, as an implication, licenses")
H, Flat = z3.Bools('H Flat')          # H: complete, AF, DEC (K=0: R_g >= 0)
E = z3.Real('E')
PMT = z3.Implies(H, z3.And(E >= 0, z3.Implies(E == 0, Flat)))
def sat(*f):
    s = z3.Solver(); s.add(*f); return s.check() == z3.sat
def valid(prem, concl):
    s = z3.Solver(); s.add(prem, z3.Not(concl)); return s.check() == z3.unsat
chk("(i) PMT & not H & E<0 is SATISFIABLE: 'bare negative mass forbidden by PMT' needs H",
    sat(PMT, z3.Not(H), E < 0))
chk("(ii) PMT & E<0  |=  not H : every negative-mass configuration already violates DEC",
    valid(z3.And(PMT, E < 0), z3.Not(H)))
chk("(iii) PMT & E=0 & not Flat |= not H : the rigidity use (concentric.py:51-53, pair.py) is valid",
    valid(z3.And(PMT, E == 0, z3.Not(Flat)), z3.Not(H)))
chk("(iv) PMT & E>=0 does NOT entail H: 'M_ADM >= 0, so the theorem is satisfied' certifies nothing",
    sat(PMT, E >= 0, z3.Not(H)))
chk("(v) PMT & not H: both E<0 and E=0,non-flat are consistent -> the theorem does not "
    "discriminate bare-negative from concentric once H fails in both",
    sat(PMT, z3.Not(H), E < 0) and sat(PMT, z3.Not(H), E == 0, z3.Not(Flat)))

print("\nC5  overturn.py two-zone profile")
r0v, Rv, bv, av = 1.0, 2.0, 1.0, 1.5
mR = 4/3*math.pi*(av*(Rv**3-r0v**3) - bv*r0v**3)
mr0 = -4/3*math.pi*bv*r0v**3
chk("m(R) = (4/3)pi(9.5) = 39.7935069", abs(mR - 39.7935069) < 1e-6, "%.7f" % mR)
chk("m(r0) = -4.1887902", abs(mr0 + 4.1887902) < 1e-6)
mfun = lambda rv: (4/3*math.pi*(-bv*rv**3) if rv < r0v else
                   4/3*math.pi*(-bv*r0v**3 + av*(min(rv, Rv)**3 - r0v**3)))
mx = max(2*mfun(k*1e-3)/(k*1e-3) for k in range(1, 4001))
print("   max_r 2m(r)/r = %.4f  (read as areal static data in G=c=1 units this is trapped;"
      " rho must be scaled by < %.4f; overturn.py:209-211 disclaims any field-equation solution)" % (mx, 1/mx))
chk("two-zone numbers as printed exceed 2m/r = 1 (a units/scale note, not a PMT issue)", mx > 1)

print("\nC6  concentric.py numbers")
P = lambda rv, mm=5e-3: mm/math.sqrt(rv*rv+0.02**2) - mm/max(rv, 200.0)
chk("Phi(1) at m=5e-3 = 4.9750e-3", abs(P(1.0) - 4.9750e-3) < 1e-6, "%.6e" % P(1.0))
chk("|Phi(1000)| < 1e-10", abs(P(1000.0)) < 1e-10, "%.3e" % P(1000.0))
bad = 5e-3/math.sqrt(1000.0**2+0.02**2) - 5e-3/200.0
chk("|bad(1000)| > 1e-6 (ADM -m)", abs(bad) > 1e-6, "%.4e" % bad)
Pa = lambda rv, aa, RR, mm=5e-3: mm/math.sqrt(rv*rv+aa*aa) - mm/max(rv, RR)
print("   docstring (concentric.py:50) 'Phi(1000) = -6.2e-13, Phi(1) = +4.4e-3' vs this file's a=0.02,R_s=200:"
      " Phi(1000) = %.3e, Phi(1) = %.4e" % (P(1000.0), P(1.0)))
print("   the docstring pair is reproduced by a = 0.5, R_s = 200, m = 5e-3: Phi(1000) = %.3e, Phi(1) = %.4e"
      % (Pa(1000.0, 0.5, 200.0), Pa(1.0, 0.5, 200.0)))
chk("DISCREPANCY (recorded, not repaired): docstring values match a=0.5 not the seated a=0.02; M_ADM=0 is a-independent (C1a)",
    abs(Pa(1000.0, 0.5, 200.0) + 6.2e-13) < 0.1e-13 and abs(Pa(1.0, 0.5, 200.0) - 4.4e-3) < 0.05e-3)

print("\nOVERALL %s" % ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
