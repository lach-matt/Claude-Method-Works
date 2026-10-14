#!/usr/bin/env python3
"""D67 re-derivation for arXiv:1404.3565 (D'Onofrio, Rummukainen, Tranberg, PRL 113 (2014) 141602).
Source text: scratchpad/d67/src/1404.3565.cached.txt (alphaXiv page text, pp.1-5, v1).
Checks every closed-form step the tree (massform.py) takes from it, and re-solves
the freeze-out equation (9) from the source's own printed inputs.  Exits 1 on a failed check."""
import math, sys
import sympy as sp
import mpmath as mp

fails = []
def chk(name, got, want, tol):
    ok = abs(got - want) <= tol
    print("%-4s %-70s got %.6g want %.6g (tol %.3g)" % ("PASS" if ok else "FAIL", name, got, want, tol))
    if not ok: fails.append(name)

# ---- (1) the READ fit, eq.(7) p.3: ln(Gamma/T^4) = a T/GeV - b
a, b = 0.83, 147.7
fit = lambda T: a * T - b
chk("fit at T* = 131.7 (tree: -38.39)", fit(131.7), -38.389, 1e-9)
chk("fit at 155 (tree: -19.05)", fit(155.0), -19.05, 1e-9)
chk("rate at T* = exp(-38.389) (tree: 2.13e-17)", math.exp(fit(131.7)), 2.13e-17, 0.01e-17)
# 'log' in eq.(7) is natural log: check against Fig.3 axis (-45..-10) and against the symmetric value
ln_symm = math.log(8.0e-7)
print("     ln(8.0e-7) = %.3f ; fit at T_c=159: %.3f ; gap %.3f (fit/symm = %.3f)"
      % (ln_symm, fit(159.0), ln_symm - fit(159.0), math.exp(fit(159.0) - ln_symm)))
# a log10 reading would give log10 rate at 159 = -15.73, i.e. 1.9e-16, 3.6e9 below the symmetric
# rate at the crossover -- incompatible with a smooth crossover; the natural-log reading gives
# a factor ~5 below the plateau at T_c, compatible.  (Consistency, not proof, of the reading.)
chk("natural-log reading: fit at 159 within a factor 10 of plateau", abs(fit(159.0) - ln_symm) < math.log(10), 1, 0)

# ---- (2) eq.(8) p.4: 8.0(1.3)e-7 ~ (18 +/- 3) alpha_W^5
aw_implied = (8.0e-7 / 18) ** 0.2
print("     alpha_W implied by 8.0e-7/18: %.5f = 1/%.2f" % (aw_implied, 1 / aw_implied))
# PDG 2024 m_W (CDF excluded) 80.3692 GeV; v from G_F = 1.1663788e-5 GeV^-2: v = (sqrt2 G_F)^-1/2
GF = 1.1663788e-5; v = (math.sqrt(2) * GF) ** -0.5
mW = 80.3692
g = 2 * mW / v; aw = g * g / (4 * math.pi)
print("     v = %.4f GeV ; alpha_W(m_W,v) = %.6f = 1/%.4f" % (v, aw, 1 / aw))
chk("18 alpha_W^5 at current m_W, G_F (tree: 8.07e-7)", 18 * aw ** 5, 8.07e-7, 0.01e-7)
chk("  lies inside 8.0 +/- 1.3 e-7", abs(18 * aw ** 5 - 8.0e-7) <= 1.3e-7, 1, 0)
# relative errors: 3/18 = 16.7 %, 1.3/8.0 = 16.3 % -- the two printed forms carry the same error
print("     rel err 3/18 = %.3f ; 1.3/8.0 = %.3f" % (3 / 18, 1.3 / 8.0))

# ---- (3) re-solve eq.(9) p.4: Gamma(T*)/T*^3 = alpha H(T*),  alpha = 0.1015,
#      H^2 = pi^2 g* T^4 / (90 M^2), g* = 106.75.  => a T - b = ln(alpha sqrt(pi^2 g*/90)/M) + ln T
alpha, gstar = 0.1015, 106.75
M_full = 1.220890e19   # G^-1/2 in GeV (CODATA/PDG)
M_red = M_full / math.sqrt(8 * math.pi)
T = sp.symbols('T', positive=True)
def Tstar(M, a=a, b=b, alpha=alpha, gstar=gstar):
    c = alpha * math.sqrt(math.pi ** 2 * gstar / 90) / M
    # a T - b = ln c + ln T  <=>  T e^{-aT} = e^{-b}/c  <=>  T = -W_{-1}(-a e^{-b}/c)/a
    z = -a * math.exp(-b) / c
    r = -mp.lambertw(z, -1) / a
    return float(mp.re(r))
T_red = Tstar(M_red); T_full = Tstar(M_full)
print("     T* with M = reduced Planck mass %.4e : %.3f GeV" % (M_red, T_red))
print("     T* with M = G^-1/2 = %.4e inserted literally : %.3f GeV" % (M_full, T_full))
# sympy cross-check of the Lambert-W root by direct root finding
c_red = alpha * math.sqrt(math.pi ** 2 * gstar / 90) / M_red
root = sp.nsolve(a * T - b - sp.log(c_red) - sp.log(T), T, 131)
chk("sympy nsolve agrees with Lambert-W (reduced M)", float(root), T_red, 1e-6)
# The physical H of a radiation universe is H^2 = 8 pi G rho/3 = 8 pi^3 g* T^4/(90 M_full^2)
# = pi^2 g* T^4/(90 M_red^2): the printed formula is the physical one iff M is the REDUCED mass.
chk("printed H formula with M_red == 8 pi G rho/3 with M_full (ratio)",
    (math.pi**2*gstar/(90*M_red**2)) / (8*math.pi**3*gstar/(90*M_full**2)), 1.0, 1e-12)
chk("T* (reduced reading) reproduces printed 131.7 within its +/-2.3", abs(T_red - 131.7) <= 2.3, 1, 0)
chk("T* (reduced reading) within 0.5 GeV of 131.7", abs(T_red - 131.7) <= 0.5, 1, 0)
print("     literal-G^-1/2 reading lies %.2f GeV from 131.7 (inside +/-2.3: %s)"
      % (T_full - 131.7, abs(T_full - 131.7) <= 2.3))
# error propagation: b +/- 1.9 dominates
for db in (-1.9, 1.9):
    print("     b = %.1f -> T* = %.3f" % (b + db, Tstar(M_red, b=b + db)))
for da in (-0.01, 0.01):
    print("     a = %.2f -> T* = %.3f" % (a + da, Tstar(M_red, a=a + da)))
dT_db = Tstar(M_red, b=b + 1.9) - T_red
chk("b +/- 1.9 alone gives ~ the printed +/- 2.3 GeV", dT_db, 2.3, 0.1)
# data sensitivity: g* (footnote 1: top becoming massive neglected), alpha to 0.5 %
for gs in (100.0, 96.25, 106.75):
    print("     g* = %.2f -> T* = %.3f" % (gs, Tstar(M_red, gstar=gs)))
print("     alpha x 1.005 -> T* = %.3f" % Tstar(M_red, alpha=alpha * 1.005))
chk("g* 106.75 -> 96.25 (top removed entirely) moves T* by < 0.1 GeV",
    abs(Tstar(M_red, gstar=96.25) - T_red), 0.0, 0.1)
# M_Planck: CODATA 2018 1.220890(14)e19 -- relative 1e-5, negligible

# ---- (4) Higgs mass: source used 125-126 GeV (p.1, p.4). Current: PDG 2024 125.20 +/- 0.11;
#      1508.07161 cites ATLAS+CMS 1503.07589 125.1 +/- 0.3 (READ there, p.1).
mH_now, dmH = 125.20, 0.11
chk("PDG-2024 m_H (+/-1 sigma) lies inside the source's 125-126 GeV", (125.0 <= mH_now - dmH) and (mH_now + dmH <= 126.0), 1, 0)

# ---- (5) the dropped hypothesis: T* is a HUBBLE freeze-out.  Replace H by 1/tau (a device
#      cooling on timescale tau) in the source's own condition (9) -- ILLUSTRATION under a named
#      assumption H-COOL, not a claim about any device.  hbar = 6.582119569e-25 GeV s.
hbar = 6.582119569e-25
H_Tstar = math.sqrt(math.pi**2 * gstar / 90) * 131.7**2 / M_red
print("     H(131.7 GeV) = %.3e GeV = 1/(%.3e s)" % (H_Tstar, hbar / H_Tstar))
for tau in (1e-11, 1e-15, 1e-20, 1e-23):
    rate_needed = alpha * hbar / tau          # Gamma/T^3 = alpha/tau  (GeV)
    # solve a T - b = ln(rate_needed) - ln T  ... i.e. Gamma/T^4 = alpha/(tau T)
    f = lambda TT: a * TT - b - math.log(alpha * hbar / tau) + math.log(TT)
    lo, hi = 50.0, 400.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0: hi = mid
        else: lo = mid
    Tf = 0.5 * (lo + hi)
    inside = 130.0 <= Tf <= 159.0
    print("     tau = %.0e s -> freeze-out T = %.2f GeV (%s)" % (tau, Tf,
          "inside the fit's range" if inside else "OUTSIDE the fit's 130-159 range; not computable from this source"))

print()
print("FAILED: %s" % fails if fails else "ALL CHECKS PASS")
sys.exit(1 if fails else 0)
