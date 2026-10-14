#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of Anglada et al. 2017 (arXiv:1711.00578v1), sec. 3.2-3.3.

Every input below is READ from the paper (v1) or from the later paper named beside it.
Checks:
  A. the prefactor 0.5 in m_dust/M_E = 0.5 (S/Jy)(T/K)^-1 (d/pc)^2 (nu/230GHz)^-2, from
     M = S d^2 / (kappa B_nu(T)) in the Rayleigh-Jeans limit, kappa = 2 cm^2/g   [sympy + numeric]
  B. the size-law exponent: n(D) ~ D^-3.5  =>  m(<Dmax) ~ Dmax^0.5            [sympy]
  C. the paper's numbers: T_d(1-4 au), m_dust(1-4 au belt), 2200 factor, m_tot ~ 1e-2 M_E;
     30 au belt (1.4e-4, 0.33 M_E); warm 0.4 au component (5.5e-7, 1e-3 M_E)
  D. Rayleigh-Jeans validity at 230 GHz for T = 40, 90, 10 K (a hypothesis the formula carries)
  E. sensitivity to the moved stellar data (d, L) -- Gaia / Boyajian 2012 via Faria+2022 Table 1
  F. the moved datum that matters: MacGregor+2018's time-resolved ACA fluxes -- is a flare-only
     reading arithmetically consistent with the combined 334 +/- 48 uJy?  (approximate:
     inverse-variance weighting of the two sub-images whose rms the paper gives)
Exit 1 if any check disagrees beyond its stated tolerance.
"""
import math, sys
import sympy as sp

fails = []
def chk(name, ok, detail):
    print(("PASS " if ok else "FAIL ") + name + " :: " + detail)
    if not ok:
        fails.append(name)

# ---------------------------------------------------------------- A. prefactor
S, d, c, kap, nu, k, T, x = sp.symbols("S d c kappa nu k T x", positive=True)
B_RJ = 2 * nu**2 * k * T / c**2
M = S * d**2 / (kap * B_RJ)
vals = {S: 1e-23, d: 3.0857e18, c: 2.99792458e10, kap: 2.0, nu: 230e9, k: 1.380649e-16, T: 1.0}
M_g = float(M.subs(vals))
M_E_g = 5.9722e27
pref = M_g / M_E_g
chk("A prefactor 0.5", abs(pref - 0.5) / 0.5 < 0.05,
    "M(1 Jy,1 K,1 pc,230 GHz,kappa=2)/M_E = %.4f (paper: 0.5)" % pref)

# ---------------------------------------------------------------- B. exponent
D, Dmin, Dmax, q = sp.symbols("D D_min D_max q", positive=True)
mass = sp.integrate(D**3 * D**sp.Rational(-7, 2), (D, Dmin, Dmax))
lead = sp.limit(mass / sp.sqrt(Dmax), Dmax, sp.oo)
chk("B m(<Dmax) ~ Dmax^0.5 for q=-3.5", sp.simplify(lead - 2) == 0,
    "int D^3 D^-3.5 dD = %s ; leading ~ %s * Dmax^0.5" % (sp.simplify(mass), lead))
ratio = math.sqrt(50e3 / 1e-2)   # 50 km / 1 cm
chk("B (50 km / 1 cm)^0.5 ~ 2200", abs(ratio - 2200) / 2200 < 0.03,
    "(Dmax/Ddust)^0.5 = %.0f (paper: 2200)" % ratio)

# ---------------------------------------------------------------- C. the paper's numbers
L, d_pc, nu_GHz = 0.0015, 1.3, 230.0      # READ sec 1 (Ribas 2017), sec 1 (van Leeuwen 2007)
def Td(r_au, Lsun=L):
    return 278.0 * Lsun**0.25 * r_au**-0.5
def mdust(S_Jy, T_K, dpc=d_pc, nuG=nu_GHz):
    return 0.5 * S_Jy / T_K * dpc**2 * (nuG / 230.0)**-2
t1, t4, t2 = Td(1), Td(4), Td(2)
chk("C T_d(1-4 au) ~ 40 K", t4 < 40 < t1,
    "T_d(1 au)=%.1f, T_d(2 au)=%.1f, T_d(4 au)=%.1f K (paper: ~40 K)" % (t1, t2, t4))
md = mdust(200e-6, 40.0)
chk("C m_dust(belt) ~ 4e-6 M_E", abs(md - 4e-6) / 4e-6 < 0.15,
    "S=200 uJy, T=40 K: m_dust = %.2e M_E (paper: 4e-6); with the full 270 uJy excess: %.2e"
    % (md, mdust(270e-6, 40.0)))
mt = md * ratio
chk("C m_tot ~ 1e-2 M_E", 0.5e-2 < mt < 2e-2, "m_tot = %.2e M_E (paper: ~1e-2)" % mt)
mo = mdust(1.7e-3, 10.0)
chk("C 30 au belt m_dust ~ 1.4e-4", abs(mo - 1.4e-4) / 1.4e-4 < 0.1,
    "S=1.7 mJy, T=10 K: %.2e M_E; m_tot = %.2f M_E (paper: 1.4e-4, 0.33); T_d(30 au)=%.1f K"
    % (mo, mo * ratio, Td(30)))
mw = mdust(30e-6, 90.0)
# the paper prints 5.5e-7 for this component; recorded, not asserted either way
disc = mw / 5.5e-7
print("NOTE C warm 0.4 au component: S=30 uJy, T=90 K gives m_dust = %.2e M_E, m_tot = %.2e M_E; "
      "paper prints 5.5e-7 and ~1e-3 (ratio recomputed/printed = %.2f). T_d(0.4 au) = %.1f K. "
      "A DISCREPANCY in arXiv v1, not a refutation; the journal version (ApJL 850 L6) is not read." %
      (mw, mw * ratio, disc, Td(0.4)))
S_needed = 5.5e-7 * 90.0 / (0.5 * d_pc**2)
print("NOTE C  flux that would give the printed 5.5e-7 at 90 K: %.0f uJy" % (S_needed * 1e6))

# ---------------------------------------------------------------- D. Rayleigh-Jeans validity
h, kB = 6.62607015e-27, 1.380649e-16
for TT in (40.0, 90.0, 10.0):
    xx = h * 230e9 / (kB * TT)
    corr = xx / math.expm1(xx)          # B_Planck / B_RJ
    print("NOTE D T=%4.0f K: h nu/kT = %.3f, B_Planck/B_RJ = %.3f -> RJ mass underestimated by x%.2f"
          % (TT, xx, corr, 1 / corr))

# ---------------------------------------------------------------- E. moved stellar data
d_new, L_new = 1.3012, 0.0016   # Faria+2022 Table 1 (Gaia; Boyajian 2012)
f = (d_new / d_pc)**2 * (L_new / L)**-0.25
chk("E moved d, L shift m_tot by < 5%", abs(f - 1) < 0.05,
    "d 1.3->%.4f pc, L 0.0015->%.4f Lsun: m_tot x %.3f" % (d_new, L_new, f))

# ---------------------------------------------------------------- F. the flare datum
# MacGregor+2018 sec 3.2: first 12 ACA sessions rms 68 uJy/beam, no >3 sigma source, ~2 sigma
# central peak; final session rms 150 uJy/beam, 1.17 +/- 0.10 mJy; all 13 combined 334 +/- 48 uJy.
w12, wl = 1 / 68.0**2, 1 / 150.0**2
for S12 in (74.0, 101.0, 136.0):     # photosphere; 12-m quiescent; the ~2 sigma peak
    comb = (S12 * w12 + 1170.0 * wl) / (w12 + wl)
    print("NOTE F inverse-variance combination, S(first 12)=%.0f uJy: combined = %.0f uJy "
          "(measured 334 +/- 48)" % (S12, comb))
comb_hi = (136.0 * w12 + 1170.0 * wl) / (w12 + wl)
comb_lo = (74.0 * w12 + 1170.0 * wl) / (w12 + wl)
chk("F flare-only reading reproduces combined ACA flux within 1.5 sigma",
    abs(comb_hi - 334) < 1.5 * 48 or abs(comb_lo - 334) < 1.5 * 48,
    "range %.0f-%.0f uJy vs 334 +/- 48 (approximate weighting; combined rms here %.0f vs 47 printed)"
    % (comb_lo, comb_hi, (w12 + wl)**-0.5))
# Anglada's model in the quiescent sub-image: star 74 + belt ~200 (+ warm ~30, unresolved by ACA)
pred = 74.0 + 200.0 + 30.0
print("NOTE F Anglada's three-component flux in the ACA beam, quiescent: ~%.0f uJy; the first-12 "
      "image shows at most a ~2 sigma (~%.0f uJy) peak: tension ~ %.1f sigma (approximate)"
      % (pred, 2 * 68.0, (pred - 136.0) / 68.0))

print()
print("RESULT:", "ALL CHECKS PASS" if not fails else "FAILED: " + ", ".join(fails))
sys.exit(1 if fails else 0)
