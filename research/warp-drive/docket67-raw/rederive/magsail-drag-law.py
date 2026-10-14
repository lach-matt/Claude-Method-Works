#!/usr/bin/env python3
"""
DOCKET 67 -- audit rederivation for key 'magsail-drag-law'.

Tree use (research/warp-drive/arrival.py:41-52): brake distance floor
    L = (gamma-1) m c^2 / (rho (beta c)^2 A),   drag F = rho v^2 A, A constant, C = 1.
Sources READ: Gros, arXiv:1707.02801v3 (J. Phys. Commun. 2017; v3 9 May 2018), eqs (1),(8)-(16),(19),(20),(31)
(local cached full text: scratchpad d67/src/casmag/all/1707.02801v3.txt -- alphaXiv quota was exhausted).
Zubrin & Andrews 1991 (J. Spacecraft Rockets 28:197) NAMED-NOT-READ: only Gros's restatement of it
(pressure balance eq (31); power-law A ~ (v/c)^alpha; I = 159e3 A, v = c/10) is used.

Every check prints and asserts; exit 0 = all assertions hold.
"""
import math, sys
import sympy as sp

ok = True
def chk(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "FAIL", label, detail))

c   = 299792458.0
AU  = 1.495978707e11
LY  = 9.4607304726e15
M_P = 1.67262192e-27
RHO = 1.0e6*M_P                     # the tree's N_ISM = 1 cm^-3

def gam(b): return 1.0/math.sqrt(1.0-b*b)
def L_tree(m, b, A, rho=RHO):       # arrival.py:51-52, verbatim formula
    return (gam(b)-1.0)*m*c**2/(rho*(b*c)**2*A)

print("== 1. The tree's own numbers, reproduced from its formula")
d = L_tree(1e6, 0.0476, 1e12)/AU
chk("selftest 2001.64 AU (1e6 kg, 0.0476 c, 1e12 m^2)", abs(d-2001.64) < 0.01, "%.4f AU" % d)
tab = {A: (L_tree(1e6,0.0476,A)/AU, L_tree(1e6,0.866,A)/LY) for A in (1e10,1e12,1e14)}
for A,(a1,a2) in tab.items(): print("     A=%.0e m^2: %9.1f AU  %8.3f ly" % (A,a1,a2))
chk("table 8.42 ly / 0.08 ly / 0.00 ly from 0.866 c", round(tab[1e10][1],2)==8.42 and round(tab[1e12][1],2)==0.08 and round(tab[1e14][1],2)==0.00)
A810 = 1e12*2001.64/810.0
A26  = 1e10*tab[1e10][1]/2.6
print("     area that would give the prose '810 AU' from 0.0476 c : %.3e m^2" % A810)
print("     area that would give the prose '2.6 ly'  from 0.866 c : %.3e m^2" % A26)
chk("prose pair (810 AU, 2.6 ly) is NOT one area (DISCREPANCY, recorded not graded)", A810/A26 > 10, "ratio %.1f" % (A810/A26))
chk("'2.6 ly' ~ A = pi*(100 km)^2 (radius reading of the 100 km row)", abs(A26/(math.pi*1e10)-1) < 0.05, "A26/(pi e10) = %.3f" % (A26/(math.pi*1e10)))

print("\n== 2. Constant-A, v^2 drag, non-relativistic: exact solution (sympy)")
x, m, rho, A, v0, v = sp.symbols('x m rho A v0 v', positive=True)
vf = sp.Function('vf')
sol = sp.dsolve(sp.Eq(m*vf(x)*vf(x).diff(x), -rho*A*vf(x)**2), vf(x), ics={vf(0): v0})
print("     v(x) =", sol.rhs)
chk("v(x) = v0 exp(-rho A x / m)", sp.simplify(sol.rhs - v0*sp.exp(-rho*A*x/m)) == 0)
chk("distance to REST is infinite (v>0 for all finite x)", sp.limit(sol.rhs, x, sp.oo) == 0 and sp.solve(sp.Eq(sol.rhs,0),x)==[])
Lnr = sp.Rational(1,2)*m*v0**2/(rho*v0**2*A)      # tree formula, beta->0
ratio_v = sp.simplify(sol.rhs.subs(x, Lnr)/v0)
chk("at the tree's L the ship keeps v/v0 = e^(-1/2) = 0.607", sp.simplify(ratio_v - sp.exp(-sp.Rational(1,2)))==0, "(KE fraction e^-1)")
chk("so 'floor' is TRUE under the tree's own constant-A hypothesis (vacuously: true value infinite)", True)
vins = 1.0e5                                          # Gros's insertion speed c/3000 = 100 km/s
x_ins = (1e6/(RHO*1e12))*math.log(0.0476*c/vins)/AU
print("     constant A=1e12, n=1: distance 0.0476 c -> 100 km/s = %.0f AU (= %.2f x the tree's floor)" % (x_ins, x_ins/2001.64))

print("\n== 3. Relativistic, constant A")
b = sp.symbols('beta', positive=True)
g = 1/sp.sqrt(1-b**2)
# (a) tree's force F = rho v^2 A (no relativistic drag correction): gamma^3 m c dbeta = -rho A beta c dx... per unit
#     dx = -(m/(rho A)) gamma^3 dbeta / beta
# (b) ship-frame ram flux gamma n v and momentum gamma m_p v per absorbed proton: F = gamma^2 rho v^2 A
#     (longitudinal force invariant) -> dx = -(m/(rho A)) gamma dbeta / beta
Fb = sp.log(b/(1+sp.sqrt(1-b**2)))          # closed form of int gamma/beta
Fa = Fb + g                                    # gamma^3 = gamma + beta^2 gamma^3, int beta gamma^3 = gamma
chk("d/dbeta of antiderivative (a) = gamma^3/beta", sp.simplify(sp.diff(Fa,b) - g**3/b)==0)
chk("d/dbeta of antiderivative (b) = gamma/beta",   sp.simplify(sp.diff(Fb,b) - g/b)==0)
def dist(F, b0, b1): return float(F.subs(b,b0) - F.subs(b,b1))
for b1 in (0.0476, 0.01):
    print("     0.866 c -> %.4f c, in units m/(rho A): (a) %.3f  (b) %.3f  tree L: %.3f"
          % (b1, dist(Fa,0.866,b1), dist(Fb,0.866,b1), (gam(0.866)-1)/0.866**2))
chk("both relativistic forms still diverge at beta->0 (log)", sp.limit(Fa, b, 0, '+') == -sp.oo and sp.limit(Fb, b, 0, '+') == -sp.oo)
chk("gamma^2 at 0.866 c = 4.0 (the initial ram drag the tree omits at high beta)", abs(gam(0.866)**2-4.0) < 1e-3)

print("\n== 4. Pressure balance (Gros eq (31), his restatement of Zubrin-Andrews [13]); DERIVED here, not a Z-A quote")
z, B0, R, mu0, n, mp = sp.symbols('z B0 R mu0 n m_p', positive=True)
zs = sp.solve(sp.Eq(n*mp*v**2/2, 2*B0**2*R**6/(mu0*z**6)), z)[0]
expo_z = sp.simplify(sp.diff(sp.log(zs), v)*v)
chk("standoff z ~ v^(-1/3)", sp.simplify(expo_z + sp.Rational(1,3))==0, str(expo_z))
Fpb = n*mp*v**2*sp.pi*zs**2
expo_F = sp.simplify(sp.diff(sp.log(Fpb), v)*v)
chk("drag F ~ rho v^2 * pi z^2 ~ v^(4/3): velocity-dependent area, NOT constant A", sp.simplify(expo_F - sp.Rational(4,3))==0, str(expo_F))
k = sp.symbols('k', positive=True)
xstop = sp.integrate(m*v/(k*v**sp.Rational(4,3)), (v, 0, v0))
Lest  = (m*v0**2/2)/(k*v0**sp.Rational(4,3))
chk("v^(4/3) law: stopping distance FINITE and = 3 x energy/initial-drag estimate", sp.simplify(xstop/Lest - 3)==0, "ratio %s" % sp.simplify(xstop/Lest))

print("\n== 5. Gros's momentum braking, eq (1) with full reflection and eq (8) A(v)=A_c log^3(I/(beta I_c))")
Ac, Ic, I, mt, npp, cc = sp.symbols('A_c I_c I m_tot n_p c', positive=True)
# eq (10): 1/log^2(v Ic/(c I)) = 1/log^2(v0 Ic/(c I)) + 4 m_p n_p A_c x / m_tot ; check it solves eq (9)
ell = sp.log(v*Ic/(cc*I))
xv = (1/sp.log(v0*Ic/(cc*I))**2 - 1/ell**2) * mt/(4*mp*npp*Ac)       # x(v) from eq (10) with x0=0: (x0 - x) term
# eq (9)/(1): m v dv/dx = -2 m_p n_p A(v) v^2  ->  dx/dv = -m/(2 m_p n_p A(v) v), A(v) = A_c (-ell)^3
dxdv_eom = -mt/(2*mp*npp*Ac*(-ell)**3*v)
chk("Gros eq (10) solves eq (1)+(8) (dx/dv matches, v < cI/I_c)", sp.simplify(sp.diff(xv, v) - dxdv_eom)==0)
a = sp.symbols('a', positive=True)
xmax = mt/(4*mp*npp*Ac*a**2)                                            # eq (11), a = log(cI/(v0 Ic))
Av0 = Ac*a**3
Ltr = mt/(2*mp*npp*Av0)                                                 # tree floor, beta->0, C=1, A = A(v0)
chk("x_max / L_tree = a/2 when the tree's A is read as A(v0)", sp.simplify(xmax/Ltr - a/2)==0)
Ltr_bare = mt/(2*mp*npp*(Ac/sp.Rational(81,1000)))                      # A read as the bare loop area pi R^2
chk("x_max / L_tree = 6.17/a^2 when the tree's A is read as the bare area pi R^2", abs(float((xmax/Ltr_bare).subs(a,1)) - 6.1728) < 1e-3)
print("     => the 'floor' label HOLDS for a<2.48 (bare-area reading) and FAILS for a<2 (A(v0) reading);")
print("        at Gros's optimum a=1: true stopping distance = 0.5 x floor (A(v0)) or 6.17 x floor (bare)")
# Gros's own numbers
chk("eq (16): I_opt = e*I_c*beta0 = 4.2e6 beta0 A", abs(math.e*1.55e6/1e6 - 4.21) < 0.01)
chk("eq (19): 1/(4*0.081) = 3.1", abs(1/(4*0.081) - 3.086) < 1e-3)
def xfrac(r, a=1.0): return 1 - a*a/(math.log(r)-a)**2               # eq (13)
chk("eq (13): v/v0=1/10 at 0.91 x_max; 1/300 at 0.98 x_max", round(xfrac(0.1),2)==0.91 and round(xfrac(1/300),2)==0.98)
# t = e^{-a}/v0 * int exp(a/sqrt(1-x/xmax)) dx? eq (14) as extracted: t = (e^{-a}/v0) int dx' exp(a/sqrt(1-x'/xmax))
def tau14(r, a=1.0, N=400000):
    X = xfrac(r,a); h = X/N; s = 0.0
    for i in range(N):
        u = (i+0.5)*h; s += math.exp(a/math.sqrt(1-u))
    return math.exp(-a)*s*h
t10, t300 = tau14(0.1), tau14(1/300)
chk("eq (14): tau(1/10) = 1.84, tau(1/300) = 5.2", round(t10,2)==1.84 and abs(t300-5.2)<0.05, "%.3f %.3f" % (t10,t300))
chk("eq (20): 4.2/(1+2*5.2)=0.37 ly, 39.5/(1+2*1.84)=8.44 ly", round(4.2/(1+2*5.2),2)==0.37 and round(39.5/(1+2*1.84),2)==8.44)

print("\n== 6. Gros's law applied to the tree's scenario (1e6 kg, 0.0476 c), bare area 1e12 m^2, a = 1")
for nn, lbl in ((1.0,"tree n=1"), (0.1,"Gros LIC f=0.1"), (0.005,"Local Bubble")):
    xm = 1e6/(4*M_P*nn*1e6*0.081*1e12)
    print("     %-15s x_max = %9.0f AU   (tree floor at that n: %9.0f AU)" % (lbl, xm/AU, L_tree(1e6,0.0476,1e12,M_P*nn*1e6)/AU))
Ireq = 0.866*1.55e6
print("     at 0.866 c: A(v)=0 unless I > beta*I_c = %.2e A; Gros integrates the NON-relativistic Lorentz force," % Ireq)
print("     so no READ model covers the tree's 0.87 c row -- outside every source's domain")
chk("0.866 c needs I > 1.34e6 A just to reflect (Gros eq (8) cutoff)", abs(Ireq-1.3423e6) < 1e3)
chk("Gros: Z-A's I=159e3 A at c/10 is at/below cutoff (beta*I_c = 1.55e5 A)", abs(0.1*1.55e6 - 1.55e5) < 1 and 159e3/(0.1*1.55e6) < 1.03)

print("\n  REDERIVE %s" % ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
