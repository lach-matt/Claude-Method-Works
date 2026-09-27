#!/usr/bin/env python3
"""
DOCKET 67 -- re-derivation for 'adm-mass-definition'.

Definition used (EHLS arXiv:1110.2087v2 Def.3, n = 3; McCormick arXiv:2401.05128 Def.2.2):
    E = 1/(2(n-1) w_{n-1}) lim_{r->inf} oint_{|x|=r} sum_ij (g_ij,i - g_ii,j) nu^j dA
      = (1/16 pi) lim oint (g_ij,i - g_ii,j) nu^j dA     (n = 3, w_2 = 4 pi)

Checks
 C1  flux integrand for g_ij = (1 - 2 Phi(r)) delta_ij, computed in Cartesian components:
     E = lim r^2 Phi'(r).  With Phi = -M/r, E = M.
 C2  Schwarzschild isotropic spatial metric (1 + M/2r)^4 delta_ij  ->  E = M exactly.
 C3  concentric.py exterior Phi = m/sqrt(r^2+a^2) - m/r:
     r^2 Phi' -> 0; leading 3 m a^2/(2 r^2); Phi ~ -m a^2/(2 r^3)  (decay q = 3 > 1/2).
 C4  concentric.py's rejected potential (error 1): E = -m.
 C5  the printed numbers: Phi(1), Phi(1000) at the file's own (m=5e-3, a=0.02, R_s=200)
     versus the docstring's +4.4e-3 and -6.2e-13; and at a = 0.5.
 C6  Plummer core is not compactly supported: enclosed-mass deficit at R_s (stability.py's
     'vacuum exterior' / 'INTERIOR Schwarzschild M_in = -m' hypotheses).
 C7  stability.py junction: with M_in = -m and m_s = R(sqrt(1+2m/R) - 1), the Israel/Lake
     identity M_out - M_in = m_s sqrt(f_in) - m_s^2/(2R) gives M_out = 0 exactly;
     m_s = m - m^2/(2R) + O(m^3)  -- the proper shell mass is not m (ADM binding energy).
 C8  second-order (Newtonian binding) estimate for the linearised device's matter content:
     U = U_self(core) + U_self(shell) + U_int, relative to m, at the tree's m values.
     ESTIMATE ONLY (post-linear Newtonian), labelled as such.
"""
import math
import sympy as sp

ok = True
def check(label, cond):
    global ok
    ok &= bool(cond)
    print(("  ok   " if cond else "  FAIL ") + label)

x, y, z = sp.symbols('x y z', real=True)
r = sp.symbols('r', positive=True)
M, m, a, R = sp.symbols('M m a R', positive=True)
X = [x, y, z]
rr = sp.sqrt(x**2 + y**2 + z**2)

def adm_flux_radial(g_of_r):
    """g_ij = g(r) delta_ij. Return (1/16pi) * integrand * 4 pi r^2 as a function of r."""
    g = [[g_of_r(rr) if i == j else 0 for j in range(3)] for i in range(3)]
    integrand = 0
    for j in range(3):
        s = 0
        for i in range(3):
            s += sp.diff(g[i][j], X[i]) - sp.diff(g[i][i], X[j])
        integrand += s * X[j] / rr
    # evaluate on the +x axis (radial symmetry): integrand is constant on the sphere
    val = sp.simplify(integrand.subs({y: 0, z: 0}).subs(x, r))
    return sp.simplify(val * 4 * sp.pi * r**2 / (16 * sp.pi))

print("C1  weak-field isotropic metric g = (1 - 2 Phi) delta")
Phi = sp.Function('Phi')
E1 = adm_flux_radial(lambda s: 1 - 2 * Phi(s))
target = r**2 * sp.diff(Phi(r), r)
check("flux = r^2 Phi'(r)   [got %s]" % E1, sp.simplify(E1 - target) == 0)
E1M = sp.limit(adm_flux_radial(lambda s: 1 + 2 * M / s), r, sp.oo)
check("Phi = -M/r  ->  E = M   [got %s]" % E1M, sp.simplify(E1M - M) == 0)

print("C2  Schwarzschild isotropic spatial metric")
E2 = sp.limit(adm_flux_radial(lambda s: (1 + M / (2 * s))**4), r, sp.oo)
check("(1+M/2r)^4 delta  ->  E = M   [got %s]" % E2, sp.simplify(E2 - M) == 0)

print("C3  concentric.py exterior potential (r > R_s)")
Phi_ext = m / sp.sqrt(r**2 + a**2) - m / r
flux = sp.simplify(r**2 * sp.diff(Phi_ext, r))
check("r^2 Phi' = m[1 - r^3/(r^2+a^2)^(3/2)]",
      sp.simplify(flux - m * (1 - r**3 / (r**2 + a**2)**sp.Rational(3, 2))) == 0)
Elim = sp.limit(flux, r, sp.oo)
check("lim r^2 Phi' = 0  (M_ADM = 0 for the metric as written)   [got %s]" % Elim, Elim == 0)
lead = sp.limit(flux * r**2, r, sp.oo)
check("leading flux 3 m a^2/(2 r^2)   [got %s /r^2]" % lead, sp.simplify(lead - sp.Rational(3, 2) * m * a**2) == 0)
phil = sp.limit(Phi_ext * r**3, r, sp.oo)
check("Phi ~ -m a^2/(2 r^3), so g - delta = O(r^-3): inside the q > 1/2 window   [got %s /r^3]" % phil,
      sp.simplify(phil + m * a**2 / 2) == 0)
check("no 1/r term: lim r*Phi = 0", sp.limit(r * Phi_ext, r, sp.oo) == 0)

print("C4  the rejected first potential (constant -m/R_s applied everywhere)")
Phi_bad = m / sp.sqrt(r**2 + a**2) - m / R
Ebad = sp.limit(r**2 * sp.diff(Phi_bad, r), r, sp.oo)
check("E_bad = -m   [got %s]" % Ebad, sp.simplify(Ebad + m) == 0)

print("C5  printed numbers")
def phi_num(rv, mv, av, Rs):
    return mv / math.sqrt(rv * rv + av * av) - mv / max(rv, Rs)
p1 = phi_num(1.0, 5e-3, 0.02, 200.0)
p1000 = phi_num(1000.0, 5e-3, 0.02, 200.0)
p1_a05 = phi_num(1.0, 5e-3, 0.5, 200.0)
p1000_a05 = phi_num(1000.0, 5e-3, 0.5, 200.0)
exact1000 = float((Phi_ext.subs({m: sp.Rational(5, 1000), a: sp.Rational(2, 100), r: 1000})).evalf(30))
print("     file params (m=5e-3,a=0.02,R_s=200): Phi(1) = %+.6e   Phi(1000) = %+.4e  (exact %+.6e)"
      % (p1, p1000, exact1000))
print("     at a = 0.5                          : Phi(1) = %+.6e   Phi(1000) = %+.4e" % (p1_a05, p1000_a05))
print("     docstring concentric.py:50-51       : Phi(1) = +4.4e-3        Phi(1000) = -6.2e-13")
check("docstring -6.2e-13 is NOT the file's parameters (got %.2e)" % p1000, abs(p1000 + 6.2e-13) > 1e-13)
check("docstring pair reproduces at a = 0.5 (-6.25e-13, 4.45e-3)",
      abs(p1000_a05 + 6.2e-13) < 1e-14 and abs(round(p1_a05, 4) - 4.4e-3) < 1e-4 + 1e-12)
check("selftest near(4.9750e-3, tol 1e-6) passes, margin %.3e" % (1e-6 - abs(p1 - 4.975e-3)),
      abs(p1 - 4.975e-3) <= 1e-6)
check("selftest |Phi(1000)| < 1e-10 holds (%.1e) and would catch a monopole |M| > 1e-7" % abs(p1000),
      abs(p1000) < 1e-10 and 1e-7 / 1000 <= 1e-10)
print("     either value is >= 10^6 below a bare -m tail (m/1000 = 5e-6): conclusion unaffected")

print("C6  Plummer core is not compact (stability.py 'vacuum exterior')")
frac_out = 1 - R**3 / (R**2 + a**2)**sp.Rational(3, 2)
lead6 = sp.limit(frac_out * R**2, R, sp.oo)
check("core mass fraction outside R_s ~ 3a^2/(2R_s^2)   [got %s/R^2]" % lead6,
      sp.simplify(lead6 - sp.Rational(3, 2) * a**2) == 0)
fv = float(frac_out.subs({a: sp.Rational(2, 100), R: 200}))
print("     at a = 0.02, R_s = 200: fraction = %.4e  -> exterior mass at R_s+ = %.2e m, "
      "decaying to 0; interior M_in = -m(1 - %.2e)" % (fv, fv, fv))

print("C7  stability.py junction (exact GR, point core)")
s = sp.sqrt(1 + 2 * m / R)
ms = R * (s - 1)
Min, Mout = -m, sp.Integer(0)
lhs = Mout - Min
rhs = ms * sp.sqrt(1 - 2 * Min / R) - ms**2 / (2 * R)
check("M_out - M_in = m_s sqrt(f_in) - m_s^2/2R  with M_out = 0", sp.simplify(sp.expand(lhs - rhs)) == 0)
ser = sp.series(ms, m, 0, 3).removeO()
check("m_s = m - m^2/(2R) + O(m^3)   [got %s]" % sp.simplify(ser), sp.simplify(ser - (m - m**2 / (2 * R))) == 0)
sig = ms / (4 * sp.pi * R**2)
check("sigma = m_s/(4 pi R^2) = (1/4 pi R)[sqrt(1+2m/R) - 1] (stability.py:25)",
      sp.simplify(sig - (s - 1) / (4 * sp.pi * R)) == 0)

print("C8  second-order Newtonian binding estimate (ESTIMATE, not GR)")
rho = sp.Rational(3, 4) / sp.pi * a**2 / (r**2 + a**2)**sp.Rational(5, 2)   # unit-mass Plummer
PhiP = -1 / sp.sqrt(r**2 + a**2)                                            # its potential (G=1)
Uself_unit = sp.simplify(sp.Rational(1, 2) * sp.integrate(rho * PhiP * 4 * sp.pi * r**2, (r, 0, sp.oo)))
check("Plummer self-energy = -(3 pi/32) M^2/a   [got %s]" % Uself_unit,
      sp.simplify(Uself_unit + 3 * sp.pi / (32 * a)) == 0)
for mv in (1e-3, 5e-3, 1e-2, 2e-2, 4e-2):
    av, Rv = 0.02, 200.0
    Ucore = -(3 * math.pi / 32) * mv**2 / av      # quadratic in m: sign-blind
    Ushell = -mv**2 / (2 * Rv)
    Uint = (-mv) * (-mv / Rv)                     # core (-m) at shell interior potential -m/R
    Utot = Ucore + Ushell + Uint
    print("     m = %.0e : m/a = %.2f  U_total = %+.3e  = %+.3f m" % (mv, mv / av, Utot, Utot / mv))
print("     => the ADM mass equals the sum of source monopoles only to O(m/a); at the design")
print("        point the post-linear term is ~7 % of m, ~29 % at m = 2e-2.  For the metric AS")
print("        WRITTEN (C3) E = 0 exactly; a full-GR realisation with rest masses -m, +m would")
print("        need the shell retuned at this order to keep M_ADM = 0 (cf. C7, where it is).")

print("\nRESULT:", "ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
raise SystemExit(0 if ok else 1)
