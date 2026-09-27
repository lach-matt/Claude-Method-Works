#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for arXiv:2102.06824 (Bobrick & Martire 2021, CQG 38 105009).
Checks the closed-form steps the tree's attribution (warpfolder.py:143-150, WARP-DRIVE.md:31,208-213)
and the source rest on.  sympy + mpmath only.  Prints 'N failure(s)'."""
import sympy as sp, mpmath as mp
fails = 0
def check(name, ok, detail=""):
    global fails
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    if not ok: fails += 1

r, th, rp, v, R, sig, r0, D, a = sp.symbols('r theta rp v R sigma r0 D alpha', positive=True)
m = sp.Function('m')
# (1) B-M eq 6/7: w = (1 - (r/Lambda)')/(8 pi r^2), Lambda = 1/(1-2m/r)  =>  w = m'/(4 pi r^2)
Lam = 1/(1 - 2*m(r)/r)
w = (1 - sp.diff(r/Lam, r))/(8*sp.pi*r**2)
check("eq6-7: w = m'(r)/(4 pi r^2) (positive density <=> enclosed mass increasing)",
      sp.simplify(w - sp.diff(m(r), r)/(4*sp.pi*r**2)) == 0)
# exterior Lambda > 1 iff m(r_out) > 0 (Birkhoff/Schwarzschild), and truncation (flat exterior) forces m(r_out)=0
M = sp.symbols('M', positive=True)
check("eq7: Lambda_out = 1/(1-2M/r) > 1 for M>0", sp.simplify(1/(1-2*M/r) - 1 - 2*M/(r-2*M)) == 0)
# truncation lemma: integral of w dV = m(r_out) - m(0); flat exterior => 0 => w changes sign unless w==0
check("truncation lemma: Int 4 pi r^2 w dr = m(r_out)-m(0)",
      sp.simplify(sp.integrate(4*sp.pi*r**2*(sp.diff(m(r),r)/(4*sp.pi*r**2)), r) - m(r)) == 0)

# (2) eq 9: N'/N = -P'/(P+rho) with rho=rho(P), P=0 at both boundaries => N(r_in)=N(r_out).
# Numeric: constant-density shell, TOV (G=c=1), check N(r_in)=N(r_out)=1-2M/r_out < 1 = N(inf).
rho0, rin, rout = mp.mpf('1e-3'), mp.mpf(1), mp.mpf(2)
def mass(x): return 4*mp.pi*rho0*(x**3 - rin**3)/3 if x > rin else mp.mpf(0)
Mtot = mass(rout)
# integrate TOV inward from rout with P(rout)=0: dP/dr = -(rho+P)(m+4 pi r^3 P)/(r(r-2m))
def dP(x, P): return -(rho0+P)*(mass(x)+4*mp.pi*x**3*P)/(x*(x-2*mass(x)))
# RK4 inward (mpmath odefun integrates forward only)
n = 4000; hstep = (rin - rout)/n; xx, P = rout, mp.mpf(0)
for _ in range(n):
    k1 = dP(xx, P); k2 = dP(xx+hstep/2, P+hstep*k1/2); k3 = dP(xx+hstep/2, P+hstep*k2/2); k4 = dP(xx+hstep, P+hstep*k3)
    P += hstep*(k1+2*k2+2*k3+k4)/6; xx += hstep
Pin = P
# lnN(rin) - lnN(rout) = -Int_{rin}^{rout} N'/N = Int P'/(P+rho) from rin to rout = ln((rho+P(rout))/(rho+P(rin)))
dlnN = mp.log((rho0+0)/(rho0+Pin))  # = lnN(rout) - lnN(rin) ... sign: N'/N=-P'/(P+rho) => lnN(rout)-lnN(rin) = ln((rho+Pin)/(rho+Pout))
dlnN = mp.log((rho0+Pin)/(rho0))
print("   constant-density shell: P(r_in)=%s (nonzero; B-M's 'P=0 at inner boundary' needs a non-trivial EOS/profile)" % mp.nstr(Pin,6))
check("eq9 caveat recorded: constant-density shell has P(r_in)!=0, so B-M's N(r_in)=N(r_out) needs P=0 at BOTH faces (their stated condition)",
      Pin > 0)
# FINDING (source-internal, recorded not repaired): integrate OUTWARD from r_in with P(r_in)=0 (vacuum interior),
# constant density.  If P never returns to 0 at r_out, B-M's isotropic-fluid 'P=0 at inner and outer boundary'
# premise (p.10) has no constant-density realisation; the conclusion 'time slows inside' is still reached for a
# thin shell by continuity of g_tt (junction condition), i.e. by another route.
def outward(rho):
    mm = lambda x: 4*mp.pi*rho*(x**3 - rin**3)/3
    ff = lambda x, P: -(rho+P)*(mm(x)+4*mp.pi*x**3*P)/(x*(x-2*mm(x)))
    n = 4000; hh = (rout-rin)/n; xx, P = rin, mp.mpf(0); Pmax = mp.mpf(0)
    for _ in range(n):
        k1 = ff(xx, P); k2 = ff(xx+hh/2, P+hh*k1/2); k3 = ff(xx+hh/2, P+hh*k2/2); k4 = ff(xx+hh, P+hh*k3)
        P += hh*(k1+2*k2+2*k3+k4)/6; xx += hh; Pmax = max(Pmax, P)
    return P, 2*mm(rout)/rout
allneg = True
for rho in ('1e-4', '1e-3', '1e-2', '2.5e-2'):
    Pout, comp = outward(mp.mpf(rho))
    print("   isotropic hollow shell, P(r_in)=0, rho=%s: P(r_out)=%s at 2M/r_out=%s" % (rho, mp.nstr(Pout,4), mp.nstr(comp,3)))
    allneg = allneg and Pout < 0
check("RECORDED: constant-density isotropic hollow shell cannot have P=0 at both faces (P(r_out)<0 for 2M/r_out in 0.003..0.73)", allneg,
      "B-M p.10 premise needs tension zones/anisotropy or a non-constant rho(P); not a refutation of the slowed-time conclusion")
# the general statement, symbolic: if rho=rho(P) and P(rin)=P(rout)=0 then Int P'/(P+rho(P)) dr = F(0)-F(0)=0
Ps = sp.symbols('P'); rhoF = sp.Function('rho')
F = sp.Integral(1/(Ps + rhoF(Ps)), (Ps, 0, 0))
check("eq9: Int_{P=0}^{P=0} dP/(P+rho(P)) = 0 => N(r_in)=N(r_out)", F.doit() == 0)
# B-M p.10 scale: 'Earth-mass shell of 10 m radius will slow down the rate of time by ... 4e-4'
GM_E = mp.mpf('3.986004418e14'); c = mp.mpf(299792458)
frac = GM_E/(10*c**2)
check("B-M p.10: Earth-mass 10 m shell slows time by ~4e-4", abs(frac - 4e-4)/4e-4 < 0.15, "GM/(Rc^2) = %s" % mp.nstr(frac,4))

# (3) Alcubierre total energy (eq 3, A.6 -> A.7): negative-definite, prefactor v^2/12
fp = sp.Function('fp')
ang = sp.integrate(sp.sin(th)**3, (th, 0, sp.pi))
check("A.7: Int sin^3 = 4/3 so (v^2/16)*(4/3) = v^2/12", sp.simplify(v**2/16*ang - v**2/12) == 0)
# from eq 3: T00 = -(1/8pi) rho^2 v^2/(4 r^2) f'^2, rho = r sin th, d3x = r^2 sin th dr dth dphi
integrand = -(1/(8*sp.pi))*(r*sp.sin(th))**2*v**2/(4*r**2)*r**2*sp.sin(th)*2*sp.pi
check("A.6->A.7: angular reduction gives -(v^2/12) r^2 f'^2", sp.simplify(sp.integrate(integrand,(th,0,sp.pi)) + v**2*r**2/12) == 0)
q = sp.Symbol('q', real=True)
check("SIGN (WARP-DRIVE.md:213 'none of that makes the energy positive'): integrand -(v^2/12) r^2 f'^2 is nonpositive for every real f'",
      (-(v**2/12)*r**2*q**2).is_nonpositive is True, "sympy assumption system; shape and flattening rescale |E| only")
# (4) Euler-Lagrange for L = r^2 f'^2: (r^2 f')' = 0 -> f = C + D/r; with f(r0)=1, f(inf)=0: f = r0/r; E_min = -(v^2/12) r0
f = sp.Function('f')
ode = sp.dsolve(sp.Eq(sp.diff(r**2*sp.diff(f(r), r), r), 0))
check("A.8: EL solution f = C1 + C2/r", sp.simplify(sp.diff(r**2*sp.diff(ode.rhs, r), r)) == 0, str(ode))
Emin = -(v**2/12)*sp.integrate(r**2*sp.diff(r0/r, r)**2, (r, r0, sp.oo))
check("E_min for f = min(r0/r,1): -(v^2/12) r0", sp.simplify(Emin + v**2*r0/12) == 0)

# (5) the 'about a factor of three' is PARAMETER-DEPENDENT: ratio tanh-profile energy / optimum at r0=R
def I_tanh(S, Rv=1):
    s = mp.mpf(S)
    fpr = lambda x: mp.diff(lambda y: (mp.tanh(s*(y+Rv)) - mp.tanh(s*(y-Rv)))/(2*mp.tanh(s*Rv)), x)
    return mp.quad(lambda x: x**2*fpr(x)**2, [0, Rv-4/s, Rv, Rv+4/s, Rv+40/s])
rows = []
for S in (2, 4, 8, 9, 20, 100):
    rat = I_tanh(S)/1  # optimum at r0 = R = 1 gives Int = r0 = 1
    rows.append((S, rat)); print("   sigma*R = %4s : E_Alc/E_opt(r0=R) = %s   (large-sigmaR asymptote sigma R/3 = %s)" % (S, mp.nstr(rat,4), mp.nstr(mp.mpf(S)/3,4)))
r8 = dict(rows)[8]
check("factor ~3 reproduced at sigma R = 8 (r0 = R; sigma R = 8 is Alcubierre 1994 Fig.1's value FROM MEMORY, and B-M's own comparison parameters are NOT stated on the pages read)", 2.3 < r8 < 3.3, mp.nstr(r8,4))
check("factor is NOT fixed: at sigma R = 100 it is ~33", dict(rows)[100] > 30, mp.nstr(dict(rows)[100],4))
# tree's case: P&F piecewise-linear wall, R = 100 m, Delta = 1 m: Int r^2 f'^2 = R^2/Delta + Delta/12
Rm, Dm = mp.mpf(100), mp.mpf(1)
I_lin = Rm**2/Dm + Dm/12
check("P&F linear wall: Int_{R-D/2}^{R+D/2} r^2/D^2 dr = R^2/D + D/12",
      sp.simplify(sp.integrate(r**2/D**2, (r, R-D/2, R+D/2)) - (R**2/D + D/12)) == 0)
ratio_tree = I_lin/(Rm - Dm/2)
print("   tree's Table-2 case (R=100 m, 1 m wall): E_wall/E_opt(r0=R-D/2) = %s (tree applies /3)" % mp.nstr(ratio_tree,5))
# absolute numbers, SI: E/c^2 = (v/c)^2 * (c^2/G) * Int / 12
G = mp.mpf('6.67430e-11'); GMsun = mp.mpf('1.32712440041e20'); Msun = GMsun/G
Mwall = (c**2/G)*I_lin/12/Msun
check("tree's 1 m wall bubble |E| = 0.564 Msun (WARP-DRIVE.md Table 2)", abs(Mwall-0.564)/0.564 < 0.005, mp.nstr(Mwall,5))
check("tree's 0.019 Msun = 0.564/3/10", abs(Mwall/30 - 0.019) < 0.0005, mp.nstr(Mwall/30,4))
Mopt = (c**2/G)*(Rm-Dm/2)/12/Msun
print("   variational optimum at r0 = 99.5 m: %s Msun; with /10 flattening: %s Msun  (tree: 0.019 -- conservative by x%s)"
      % (mp.nstr(Mopt,4), mp.nstr(Mopt/10,4), mp.nstr(0.019/(Mopt/10),3)))
check("tree's 0.019 overstates |E| relative to B-M's own optimum (direction: AGAINST M, not for)", Mopt/10 < 0.019)
# (6) flattening: r_s = sqrt(a^2 (x-xs)^2 + rho^2); density -(v^2/32pi)(d f/d rho)^2; x' = a x  => E_flat = E/a
x, rh = sp.symbols('x rho', real=True)
g = sp.Function('g')
dens = lambda aa: (sp.diff(g(sp.sqrt(aa**2*x**2 + rh**2)), rh))**2
sub = dens(a).subs(x, sp.Symbol('xp')/a)
check("flattening by alpha_X: substitution x'=alpha x gives E -> E/alpha (Jacobian 1/alpha, integrand form-invariant)",
      sp.simplify(sub - dens(1).subs(x, sp.Symbol('xp'))) == 0, "B-M p.14: alpha_X = 1+v^2 gives E -> E/(1+v^2); p.18: factor 10 -> proportionally smaller")
print("%d failure(s)" % fails)
