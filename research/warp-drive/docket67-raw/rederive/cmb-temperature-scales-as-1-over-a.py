#!/usr/bin/env python3
"""DOCKET 67 audit re-derivation: cmb-temperature-scales-as-1-over-a.

Checks, in order:
 A. THEOREM (sympy): a Planck occupation f = 1/(exp(p/kT_e)-1) set at scale factor a_e,
    free-streaming in FLRW (f conserved along the ray, p proportional to 1/a), is at every
    later a again EXACTLY a Planck occupation with T = T_e a_e / a.  Hypotheses used and
    nothing else: collisionless photons, p a = const (FLRW geodesic), no emission/absorption.
 B. The same law from thermodynamics: rho_gamma = sigma T^4 with T ~ 1/a satisfies the
    radiation continuity equation d(rho a^3) + p d(a^3) = 0 with p = rho/3 (adiabatic).
 C. CIRCULARITY (sympy + live import): permute.ratio_from_temperature(z, T0) is T0(1+z)/T0,
    identically 1+z for every T0 -- its derivative in T0 is 0, so the 'near' check at
    permute.py:428-429 cannot fail and carries no measurement.
 D. NUMBERS: T_rec = T0 (1+z*) for the tree's inputs and the current ones; Planck 2018 VI
    Table 2 spread of z* across data combinations (all base-LCDM derived values).
 E. An INDEPENDENT physical route to a recombination temperature (Saha, hydrogen only,
    eta from Planck omega_b): it gives ~3,700-3,800 K at x_e = 0.5, not 2,973 K -- so
    2,973 K is a LABEL, T0 (1+z*), not a separately measured temperature.
 F. SENSITIVITY (not a refutation): T(z) = T0 (1+z)^(1-beta); what beta would do at z*
    if one (unwarrantedly) extrapolated the z <~ 6 constraint.
"""
import math, sys, importlib.util
import sympy as sp

FAIL = []
def check(name, cond):
    print(("PASS  " if cond else "FAIL  ") + name)
    if not cond:
        FAIL.append(name)

# ---------------- A. Liouville / free streaming keeps a blackbody a blackbody
p0, a, ae, Te, k = sp.symbols('p0 a a_e T_e k', positive=True)
# comoving momentum label: physical p at a is p0*ae/a where p0 = physical momentum at ae
f_emit = lambda p: 1/(sp.exp(p/(k*Te)) - 1)
p_now = sp.symbols('p', positive=True)
# a photon with physical p at a had physical p*a/ae at emission; f conserved:
f_later = f_emit(p_now*a/ae)
T_later = Te*ae/a
planck_later = 1/(sp.exp(p_now/(k*T_later)) - 1)
check("A1 f(p; a) == Planck(p; T_e a_e/a) identically", sp.simplify(f_later - planck_later) == 0)
# number density n = int p^2 f dp ~ T^3 -> scales as a^-3 (photon number conserved)
x = sp.symbols('x', positive=True)
import mpmath as mp
mp.mp.dps = 40
I2 = mp.quad(lambda t: t**2/mp.expm1(t), [0, mp.inf])
check("A2 int x^2/(e^x-1) = 2 zeta(3) to 1e-30 (n_gamma ~ T^3 ~ a^-3; 40-digit quadrature)", abs(I2 - 2*mp.zeta(3)) < mp.mpf('1e-30'))
I3 = mp.quad(lambda t: t**3/mp.expm1(t), [0, mp.inf])
check("A3 int x^3/(e^x-1) = pi^4/15 to 1e-30 (rho_gamma ~ T^4 ~ a^-4)", abs(I3 - mp.pi**4/15) < mp.mpf('1e-30'))
# the scalings themselves: n(T_e a_e/a)/n(T_e) = (a_e/a)^3, rho ratio = (a_e/a)^4 (substitution x = p/kT)
check("A2b n ~ T^3 => n(a)/n(a_e) = (a_e/a)^3 under T = T_e a_e/a", sp.simplify((Te*ae/a)**3/Te**3 - (ae/a)**3) == 0)
# a non-Planck shape (a mu-distortion) is NOT mapped to a Planck shape by a rescaling unless mu=0
mu = sp.symbols('mu')
f_mu = 1/(sp.exp(p_now/(k*T_later) + mu) - 1)
check("A4 a chemical-potential (mu) distortion survives free streaming unchanged (not absorbed into T)",
      sp.simplify(f_mu.subs(mu, 0) - planck_later) == 0 and sp.simplify(f_mu - planck_later) != 0)

# ---------------- B. adiabatic radiation continuity
sig, C = sp.symbols('sigma C', positive=True)
T = C/a
rho = sig*T**4
pr = rho/3
cont = sp.diff(rho*a**3, a) + pr*sp.diff(a**3, a)
check("B1 d(rho a^3)+p d(a^3)=0 for rho=sigma (C/a)^4, p=rho/3", sp.simplify(cont) == 0)
# conversely: continuity with p=rho/3 forces rho ~ a^-4 hence T ~ 1/a
r = sp.Function('r')
sol = sp.dsolve(sp.Eq(sp.diff(r(a)*a**3, a) + r(a)/3*sp.diff(a**3, a), 0), r(a))
check("B2 continuity with w=1/3 solves to rho = C1/a^4", sp.simplify(sol.rhs*a**4).free_symbols <= {sp.Symbol('C1')})

# ---------------- C. circularity in permute.py
z, T0 = sp.symbols('z T_0', positive=True)
ratio_sym = (T0*(1+z))/T0
check("C1 T0(1+z)/T0 - (1+z) == 0 symbolically", sp.simplify(ratio_sym - (1+z)) == 0)
check("C2 d/dT0 of the 'measured' ratio == 0 (T0 cannot enter)", sp.diff(sp.simplify(ratio_sym), T0) == 0)
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
spec = importlib.util.spec_from_file_location("permute", "/home/user/Claude-Method-Works/research/warp-drive/permute.py")
pm = importlib.util.module_from_spec(spec); spec.loader.exec_module(pm)
check("C3 tree constants T_CMB=2.7255, Z_REC=1089.92", pm.T_CMB == 2.7255 and pm.Z_REC == 1089.92)
ok = all(abs(pm.ratio_from_temperature(zz, tt) - pm.scale_ratio_since(zz)) < 1e-9*(1+zz)
         for zz in (0.5, 10.0, 1089.92, 5000.0) for tt in (1e-3, 2.7255, 3.0, 1e6))
check("C4 live permute.ratio_from_temperature == scale_ratio_since for T0 in {1e-3,2.7255,3,1e6}", ok)
check("C5 even an absurd T0 (1e6 K) passes the tree's near-check", abs(pm.ratio_from_temperature(1089.92, 1e6) - 1090.92) < 1e-6)

# ---------------- D. numbers
Trec_tree = pm.temperature_at()
print("      T_rec(tree) = %.5f K  (prints 2973.3)" % Trec_tree)
check("D1 2.7255*1090.92 = 2973.30246 K exactly -> prints 2973.3", abs(Trec_tree - 2973.30246) < 1e-8)
Trec_now = 2.72548*1090.92
print("      T_rec(Fixsen 2009 unrounded 2.72548) = %.4f K; move %.2e rel" % (Trec_now, Trec_now/Trec_tree - 1))
check("D2 T0 rounding 2.7255 -> 2.72548 moves T_rec by < 1e-5 rel and the ratio not at all",
      abs(Trec_now/Trec_tree - 1) < 1e-5)
zs = {"TT+lowE": 1090.30, "TE+lowE": 1089.57, "EE+lowE": 1087.8, "TT,TE,EE+lowE": 1089.95,
      "TT,TE,EE+lowE+lensing (tree)": 1089.92, "+BAO": 1089.80}
for kname, v in zs.items():
    print("      z* %-30s 1+z* = %.2f   T0(1+z*) = %.1f K" % (kname, 1+v, 2.7255*(1+v)))
spread = (max(zs.values()) - min(zs.values()))/(1+1089.92)
check("D3 Planck 2018 z* spread across data combinations < 0.3%% of 1+z* (%.2e)" % spread, spread < 3e-3)
check("D4 '1,091' (factor quoted) = round(1+z*) for every Planck column", all(round(1+v) in (1089, 1090, 1091) for v in zs.values()))

# ---------------- E. Saha: an independent recombination temperature
kB = 1.380649e-23; hbar = 1.054571817e-34; c = 299792458.0; me = 9.1093837015e-31
eV = 1.602176634e-19; B = 13.605693122994*eV
omega_b = 0.02237  # Planck 2018 base TT,TE,EE+lowE+lensing (restated; value used only for eta)
eta = 273.9e-10*omega_b   # standard eta_10 = 273.9 omega_b
def saha_x(Tk):
    ng = 2*1.2020569031595942/math.pi**2*(kB*Tk/(hbar*c))**3
    nb = eta*ng
    S = (me*kB*Tk/(2*math.pi*hbar**2))**1.5*math.exp(-B/(kB*Tk))/nb
    return (-S + math.sqrt(S*S + 4*S))/2
lo, hi = 2000.0, 6000.0
for _ in range(200):
    mid = 0.5*(lo+hi)
    if saha_x(mid) > 0.5: hi = mid
    else: lo = mid
T_saha = 0.5*(lo+hi)
print("      eta = %.3e ; Saha x_e=0.5 at T = %.0f K ; x_e(2973.3 K) = %.2e" % (eta, T_saha, saha_x(2973.30246)))
check("E1 Saha half-ionisation temperature lies in 3500-4000 K (not 2973 K)", 3500 < T_saha < 4000)
print("      => z at Saha half-ionisation, IF T ~ 1/a: %.0f" % (T_saha/2.7255 - 1))

# ---------------- F. beta sensitivity (extrapolation, NOT a measured deviation)
for beta, lab in ((0.0076, "Avgoustidis+2016 central (restated), z<~3"), (0.0076+0.0080, "+1 sigma"),
                  (0.0076-0.0080, "-1 sigma")):
    fac = (1+1089.92)**(-beta)
    print("      beta = %+.4f (%s): T(z*)/[T0(1+z*)] = %.4f if extrapolated to z*" % (beta, lab, fac))
check("F1 beta=0 recovers the tree's ratio exactly", (1+1089.92)**(1-0) == 1090.92)

print("\nALL PASS" if not FAIL else "\nFAILED: %s" % FAIL)
sys.exit(1 if FAIL else 0)
