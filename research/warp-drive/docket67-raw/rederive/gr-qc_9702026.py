#!/usr/bin/env python3
"""DOCKET 67 re-derivation: Pfenning & Ford, gr-qc/9702026 (CQG 14 (1997) 1743).

Every step of the paper that is closed-form is re-derived symbolically (sympy),
and every printed number is recomputed from the paper's own formula with CODATA
2022 constants.  Nothing here edits the research tree.  Exit 0 iff all symbolic
identities hold; numeric discrepancies are RECORDED (printed), not failed.

Units: G = c = hbar = 1 (the paper's), converted with CODATA 2022.
"""
import sys
import sympy as sp

ok = True
def check(label, cond):
    global ok
    ok &= bool(cond)
    print("  %-70s %s" % (label, "ok" if cond else "FAIL"))

print("1. SYMBOLIC STEPS")
t, t0, beta, rho, v, f, Delta, alpha, R, r, th = sp.symbols(
    't t0 beta rho v f Delta alpha R r theta', positive=True)

# eq (8)->(10): insert <T00> = -(1/32pi) v^2 rho^2/r_s^2 f'^2 into eq (9)
# t0/pi * Int(-(1/32pi) v^2 rho^2 X /(t^2+t0^2)) >= -3/(32 pi^2 t0^4)
# <=> t0 * Int(v^2 X /(t^2+t0^2)) <= 3/(rho^2 t0^4): multiply by -32pi^2/rho^2
lhs9 = -sp.Rational(1, 32) / sp.pi**2 * rho**2          # coefficient of t0*Int(v^2 X/(..))
rhs9 = -sp.Rational(3, 32) / sp.pi**2 / t0**4
check("eq(10): QI(9) with <T00>(8) gives t0*Int <= 3/(rho^2 t0^4)",
      sp.simplify(rhs9 / lhs9 - 3 / (rho**2 * t0**4)) == 0)

# eq (16): contour integral
I16 = sp.integrate(1 / ((t**2 + beta**2) * (t**2 + t0**2)), (t, -sp.oo, sp.oo))
check("eq(16): Int dt/((t^2+b^2)(t^2+t0^2)) = pi/(t0 b (t0+b))",
      sp.simplify(I16 - sp.pi / (t0 * beta * (t0 + beta))) == 0)

# eq (12)-(15): with f' = -1/Delta, r_s^2 = v^2(1-f)^2 (t^2+beta^2), beta = rho/(v(1-f))
b = rho / (v * (1 - f))
rs2 = (v * t)**2 * (f - 1)**2 + rho**2
check("eq(12)/(15): r_s^2 = v^2 (1-f)^2 (t^2+beta^2)",
      sp.simplify(rs2 - v**2 * (1 - f)**2 * (t**2 + b**2)) == 0)
# eq (10) becomes t0 * Int(1/(Delta^2 (1-f)^2 (t^2+b^2)(t^2+t0^2))) <= 3/(rho^2 t0^4)
# => t0*Int <= 3 Delta^2 (1-f)^2 /(rho^2 t0^4) = 3 Delta^2/(v^2 t0^4 beta^2)  [eq 14]
check("eq(14): RHS 3 Delta^2 (1-f)^2/(rho^2 t0^4) == 3 Delta^2/(v^2 t0^4 beta^2)",
      sp.simplify(3 * Delta**2 * (1 - f)**2 / (rho**2 * t0**4)
                  - 3 * Delta**2 / (v**2 * t0**4 * b**2)) == 0)
# eq (17): pi/(beta (t0+beta)) <= 3 Delta^2/(v^2 t0^4 beta^2)
#  <=> pi/3 <= Delta^2/(v^2 t0^4) * (t0/beta + 1)
ratio17 = (3 * Delta**2 / (v**2 * t0**4 * b**2)) / (sp.pi / (b * (t0 + b)))
check("eq(17): pi/3 <= Delta^2/(v^2 t0^4) [v t0 (1-f)/rho + 1]",
      sp.simplify(ratio17 * sp.pi / 3
                  - Delta**2 / (v**2 * t0**4) * (v * t0 * (1 - f) / rho + 1)) == 0)

# eq (18)-(19): |R_tyty| = 3 v^2 y^2/(4 rho^2) f'^2 at y = rho, f' = 1/Delta
Rt = sp.Rational(3, 4) * v**2 / Delta**2
rmin = 1 / sp.sqrt(Rt)
check("eq(19): r_min = 2 Delta/(sqrt(3) v)", sp.simplify(rmin - 2 * Delta / (sp.sqrt(3) * v)) == 0)

# eq (20)-(22): t0 = alpha r_min, drop the (1-f) term (eq 21), solve for Delta
t0a = alpha * rmin
ineq = sp.pi / 3 - Delta**2 / (v**2 * t0a**4)      # must be <= 0
Dmax = sp.solve(sp.Eq(ineq, 0), Delta)
Dmax = [d for d in Dmax if d.is_positive][0]
coef = sp.simplify(Dmax * alpha**2 / v)
print("     derived eq(22): Delta <= %s * v_b/alpha^2  = %.6f v_b/alpha^2" % (coef, float(coef)))
check("eq(22) coefficient == (3/4) sqrt(3/pi)",
      sp.simplify(coef - sp.Rational(3, 4) * sp.sqrt(3 / sp.pi)) == 0)
alt = sp.Rational(3, 4) * sp.sqrt(3) * sp.pi
print("     (the arXiv text layer reads '3/4 sqrt3 pi'; the reading (3/4)sqrt(3/pi) is the one the")
print("      algebra gives; (3/4)sqrt(3)pi = %.4f would give %.0f v_b L_P at alpha=0.1)" % (float(alt), float(alt) * 100))
D_alpha01 = float(coef) / 0.1**2
print("     alpha = 1/10: Delta <= %.2f v_b L_P  (paper: '10^2 v_b L_Planck')" % D_alpha01)
check("eq(23): alpha=1/10 gives Delta within [10^1.5, 10^2.5] v_b L_P", 10**1.5 < D_alpha01 < 10**2.5)
# consistency of eq (21): Delta/rho ~ v t0/rho << 1 requires alpha-scaled t0 = alpha*2Delta/(sqrt3 v)
print("     sensitivity: Delta_max scales as alpha^-2 -> alpha=1/3: %.1f, alpha=1/30: %.0f v_b L_P"
      % (float(coef) * 9, float(coef) * 900))

# eq (25)-(28): energy
ang = 2 * sp.pi * sp.integrate(sp.sin(th)**2 * sp.sin(th), (th, 0, sp.pi))
check("eq(26): angular Int rho^2/r^2 dOmega = 8pi/3", sp.simplify(ang - 8 * sp.pi / 3) == 0)
check("eq(26): -(v^2/32pi)(8pi/3) = -v^2/12", sp.simplify(-v**2 / (32 * sp.pi) * ang + v**2 / 12) == 0)
rad = sp.integrate(r**2 / Delta**2, (r, R - Delta / 2, R + Delta / 2))
check("eq(28): Int_{R-D/2}^{R+D/2} r^2/D^2 dr = R^2/D + D/12", sp.simplify(rad - (R**2 / Delta + Delta / 12)) == 0)

print("\n2. NUMBERS, FROM THE PAPER'S OWN eq(28), CODATA 2022")
LP = 1.616255e-35      # m
mP = 2.176434e-8       # kg
Gc2 = 6.67430e-11 / 299792458.0**2   # m/kg
MSUN = 1.98841e30      # kg (IAU nominal GM_sun / G)
def E_kg(R_m, D_m, vb=1.0):
    geo = vb**2 / 12.0 * (R_m**2 / D_m + D_m / 12.0)   # metres (G=c=1)
    return geo / Gc2
D_used = 100.0 * LP    # eq (23) at v_b = 1
E100 = E_kg(100.0, D_used)
E100_LP = (1.0 / 12.0) * (100.0 / LP)**2 / 100.0
print("  R=100 m, Delta=10^2 L_P, v_b=1:")
print("    E = %.3e L_P (G=c=1)   paper eq(29): 6.2e70 v_b L_P   ratio paper/computed = %.2f"
      % (E100_LP, 6.2e70 / E100_LP))
print("    E = %.3e kg = %.3e g   paper eq(29): 6.2e65 g         ratio = %.2f"
      % (E100, E100 * 1e3, 6.2e65 / (E100 * 1e3)))
print("    (paper's L_P->grams step 6.2e70 -> 6.2e65 implies 1e-5 g per L_P; m_P = %.3e g)" % (mP * 1e3))
Mgal_paper = 2e45 / 1e3
print("    E/M_galaxy (paper's 2e45 g) = %.2e    paper eq(31): 3e20" % (E100 / Mgal_paper))
for Mmw in (0.8e12, 1.0e12, 1.5e12):
    print("    E/M_MW with M_MW = %.1e M_sun (current range)   = %.2e" % (Mmw, E100 / (Mmw * MSUN)))
# visible universe (Planck 2018: H0=67.4, Omega_b=0.0493, Omega_m=0.315), comoving radius 46.5 Gly
H0 = 67.4e3 / 3.0857e22
rho_c = 3 * H0**2 / (8 * 3.141592653589793 * 6.67430e-11)
Rh = 46.5e9 * 9.4607e15
Vol = 4.0 / 3.0 * 3.141592653589793 * Rh**3
Mb, Mm = 0.0493 * rho_c * Vol, 0.315 * rho_c * Vol
import math
print("    observable-universe baryons %.2e kg, all matter %.2e kg" % (Mb, Mm))
print("    orders of magnitude E/M_baryon = %.2f, E/M_matter = %.2f  (paper: 'roughly ten')"
      % (math.log10(E100 / Mb), math.log10(E100 / Mm)))
check("'roughly ten orders' vs baryons within 9-11", 9 <= math.log10(E100 / Mb) <= 11)

lamC = 2.42631023538e-12
Ec = E_kg(lamC, D_used)
print("  R = electron Compton wavelength %.4e m: E = %.3e kg = %.0f M_sun   paper: ~400 M_sun  ratio %.2f"
      % (lamC, Ec, Ec / MSUN, 400 / (Ec / MSUN)))
Ecr = E_kg(lamC / (2 * math.pi), D_used)
print("    (reduced Compton wavelength %.3e m would give %.1f M_sun)" % (lamC / (2 * math.pi), Ecr / MSUN))
E1m = E_kg(100.0, 1.0)
print("  R=100 m, Delta=1 m, v_b=1: E = %.2f M_sun   paper: 'on the order of a quarter of a solar mass'" % (E1m / MSUN))
print("  Van Den Broeck 1999 cross-check eq(8)-(9): R=3e-15 m, Delta=10^2 L_P ->", end=" ")
Evdb = (1 / 12.0) * ((3e-15 + D_used / 2)**2 / D_used + D_used / 12) / Gc2
print("%.2e kg (VdB prints 6.3e29 v_s kg)" % Evdb)
check("VdB eq(9) reproduced by 1/12 formula within 5%", abs(Evdb / 6.3e29 - 1) < 0.05)
check("paper eq(29) grams reproduced within factor 1.5", 1 / 1.5 < 6.2e65 / (E100 * 1e3) < 1.5)
ratio400 = (Ec / MSUN) / 400.0
print("  DISCREPANCY (recorded, not failed): the paper's '~ -400 M_sun' for R = electron Compton")
print("    wavelength is NOT reproduced by its own eq(28)+eq(23) at v_b=1: computed %.3g M_sun, ratio %.0f (10^%.2f)"
      % (Ec / MSUN, ratio400, math.log10(ratio400)))
print("    400 M_sun would need R = %.3e m (=%.4f lambda_C) at v_b=1, or v_b = %.2e at R = lambda_C"
      % (lamC * math.sqrt(1 / ratio400), math.sqrt(1 / ratio400), 1 / ratio400))
print("    cross-check via Van Den Broeck's eq(9) scaled by R^2: %.3g M_sun" % (6.3e29 * (lamC / 3e-15)**2 / MSUN))
check("DISCREPANCY stands: own-formula value exceeds 400 M_sun by > 100x", ratio400 > 100)
print("  tree comparison: nullbound.py D_pf = 1.616255e-33 m = 100 L_P ->", 100 * LP)

print("\n3. FIRST-ORDER CURVATURE CORRECTION SIZE (Kontou-Olum 1410.0665 eq.130 structure)")
# In the wall, |G_00| ~ v^2/(4 Delta^2)*... ; R_max t0^2 with t0 = alpha r_min, R_max ~ 3v^2/(4 Delta^2)
Rmax_t02 = sp.simplify(Rt * t0a**2)
print("     Riemann_max * t0^2 = %s  -> at alpha=0.1: %.3f" % (Rmax_t02, float(Rmax_t02.subs(alpha, 0.1))))
print("     Kontou-Olum Gaussian bound: 3.76 + 2.63 R_max t0^2 + ...: relative first-order correction ~ %.3f"
      % (2.63 * float(Rmax_t02.subs(alpha, 0.1)) / 3.76))

print("\nRESULT:", "ALL SYMBOLIC STEPS AGREE" if ok else "A CHECK FAILED")
sys.exit(0 if ok else 1)
