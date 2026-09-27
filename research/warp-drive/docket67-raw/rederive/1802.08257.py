#!/usr/bin/env python3
"""DOCKET 67 re-derivation: MacGregor et al. 2018 (arXiv:1802.08257v1).

Every input below is READ at source (page cited).  Nothing here repairs the
paper; a mismatch is printed as a DISCREPANCY, not an error.  Exit 0 always
unless an internal assertion of the arithmetic itself fails.

Sources read (alphaXiv, 2026-09-26):
  M18 = 1802.08257v1  (MacGregor, Weinberger, Wilner, Kowalski, Cranmer 2018)
  A17 = 1711.00578v1  (Anglada et al. 2017)
  C15 = 1502.00640v3  (Carniani et al. 2015), Table 3 Schechter fit at 1.3 mm
  G20 = 2002.07199v1  (Gonzalez-Lopez et al. 2020, ASPECS 1.2 mm), Table 4
  B25 = 2503.21890v1  (Burton et al. 2025), Sec 1.2, Table 2
"""
import math
import mpmath as mp

PC = 3.0857e18          # cm
AU = 1.495979e13        # cm
JY = 1e-23              # erg s^-1 cm^-2 Hz^-1
LSUN = 3.828e33         # erg s^-1 (IAU nominal)

out = []
def rec(tag, msg):
    out.append((tag, msg)); print(f"[{tag}] {msg}")

# ---------------------------------------------------------------- 1 flare fluence
# M18 p.3: peak 100+-4 mJy, FWHM 30 s, ~1 min total; final obs = 7 scans x 6.58 min;
# final-obs image flux 1.17+-0.10 mJy.
peak, fwhm = 100.0, 30.0
T_final = 7 * 6.58 * 60
flu_gauss = peak * fwhm * math.sqrt(math.pi / (4 * math.log(2)))    # Gaussian shape
tau = fwhm / math.log(2)                                              # instant rise, exp decay
flu_exp = peak * tau
avg_lo, avg_hi = flu_gauss / T_final, flu_exp / T_final
rec("AGREES" if avg_lo - 0.2 <= 1.17 <= avg_hi + 0.2 else "DISCREPANCY",
    f"flare fluence {flu_gauss:.0f}-{flu_exp:.0f} mJy s over the {T_final:.0f} s final obs "
    f"-> {avg_lo:.2f}-{avg_hi:.2f} mJy; M18 measures 1.17+-0.10 mJy (p.3)")

# ---------------------------------------------------------------- 2 dilution into 334 uJy
# M18 p.3: first-12 image rms 68 uJy/beam with a '~2 sigma' central peak (0..136 uJy);
# final-obs rms 150; combined image 334+-48 uJy, rms 47.
w_final = (1 / 150**2) / (1 / 68**2 + 1 / 150**2)
comb_lo = 0 * (1 - w_final) + 1170 * w_final
comb_hi = 136 * (1 - w_final) + 1170 * w_final
rec("AGREES" if comb_lo - 48 <= 334 <= comb_hi + 48 else "DISCREPANCY",
    f"inverse-variance weight of final obs = {w_final:.3f}; combined = {comb_lo:.0f}-{comb_hi:.0f} uJy "
    f"vs measured 334+-48 (within 1 sigma at the upper end)")
w_needed = [(334 - p12) / (1170 - p12) for p12 in (0, 136)]
rec("NOTE", f"weight the final obs needs to give 334 uJy: {w_needed[1]:.2f}-{w_needed[0]:.2f}; "
    f"uniform 1/13 = {1/13:.3f} would give {1170/13:.0f}-{1170/13+136*12/13:.0f} uJy")
rms_comb = 1 / math.sqrt(1 / 68**2 + 1 / 150**2)
rec("DISCREPANCY", f"quoted rms 68 (first 12) and 150 (final) combine to {rms_comb:.0f} uJy/beam, "
    f"not the quoted 47 -- the three noise quotes are not mutually consistent under inverse "
    f"variance (flare artefacts / noise region); not load-bearing: the conclusion rests on "
    f"per-observation imaging and the 2-s light curve, reproduced independently by B25")
T_rest = 19 * 3600
rec("NOTE", f"a uniform time average of the fluence over 'the remaining ~19 hours' gives "
    f"{flu_gauss/(T_rest+T_final)*1e3:.0f}-{flu_exp/(T_rest+T_final)*1e3:.0f} uJy, not 340: "
    f"the M18 p.6 sentence is heuristic; the 340 is reproduced by image weighting (item 2)")

# ---------------------------------------------------------------- 3 the cold-belt test
# A17 p.5: ~270 uJy ACA excess over the 74 uJy photosphere, ~200 uJy of it in the 1-4 au belt
# (unresolved by ACA: 1-4 au at 1.3 pc = 0.77-3.1 arcsec vs 7.3x5.5 arcsec beam).
d = 1.3
belt_arcsec = (1 / d, 4 / d)
pred_belt200 = 74 + 200
pred_A17 = 340
obs_first12, rms12 = 2 * 68, 68          # '~2 sigma' peak, M18 p.3 (value approximate)
z200 = (pred_belt200 - obs_first12) / rms12
zA17 = (pred_A17 - obs_first12) / rms12
z_nobelt = (obs_first12 - (74 + 30)) / rms12
rec("MEASURED", f"belt at {belt_arcsec[0]:.2f}-{belt_arcsec[1]:.2f} arcsec is unresolved by ACA; "
    f"first-12 data vs star+200uJy belt: {z200:.1f} sigma low; vs A17's full 340: {zA17:.1f} sigma low; "
    f"vs no belt (photosphere + 30 uJy corona): {z_nobelt:+.1f} sigma")
rec("NARROWS", "the ACA data DISFAVOUR the belt at A17's flux at ~2 sigma; they do not exclude a "
    "fainter belt.  M18's words are 'no need to posit' (p.6) / 'no need to invoke' (p.7): the "
    "EVIDENCE is removed, the belt is not shown absent")

# ---------------------------------------------------------------- 4 12-m excess
ex = 101 - 74; ex_e = math.hypot(9, 4)
exA = 106 - 74; exA_e = math.hypot(12, 4)
rec("AGREES", f"12-m excess {ex}+-{ex_e:.1f} uJy ({ex/ex_e:.1f} sigma); A17 values {exA}+-{exA_e:.1f} "
    f"({exA/exA_e:.1f} sigma): M18's '~30 uJy' reproduced")

# ---------------------------------------------------------------- 5 luminosities
def Lnu(F_jy, dpc): return 4 * math.pi * (dpc * PC)**2 * F_jy * JY
Lpk = Lnu(0.100, 1.3)
rec("AGREES" if abs(Lpk / 2.04e14 - 1) < 0.02 else "DISCREPANCY",
    f"peak L_nu at 1.3 pc = {Lpk:.3e} erg/s/Hz (M18: 2.04+-0.15e14); at Gaia 1.3020 pc: {Lnu(0.100,1.3020):.3e}")
Lsun_f = 4 * math.pi * AU**2 * 7e8 * JY
rec("AGREES", f"solar flare 7e8 Jy at 1 au -> {Lsun_f:.2e} erg/s/Hz (M18: ~2e13); ratio {Lpk/Lsun_f:.1f} (M18: 10x)")
Lq_nu = Lnu(30e-6, 1.3)
nuLnu = Lq_nu * 233e9
band = 1e21 / Lq_nu
Lbol = 0.0015 * LSUN                     # A17 p.2 citing Ribas 2017
rec("DISCREPANCY", f"30 uJy quiescent excess: L_nu = {Lq_nu:.2e}; flat spectrum 0..233 GHz gives "
    f"nu*L_nu = {nuLnu:.2e} erg/s ({nuLnu/Lbol:.1e} L_bol), not 1e21; M18's 1e21 needs an "
    f"integration band of {band/1e9:.0f} GHz (~ the 224-242 GHz observed span -> "
    f"{Lq_nu*18e9:.1e}).  Definitional (band unstated), not load-bearing; M18's '< 1e-9 L_bol' "
    f"holds only for the band reading ({1e21/Lbol:.1e})")

# ---------------------------------------------------------------- 6 electron index
alpha, s_alpha = -1.77, 0.45
delta = (1.22 - alpha) / 0.9
s_delta = s_alpha / 0.9
rec("AGREES" if abs(delta - 3.32) < 0.01 else "DISCREPANCY", f"delta = (1.22-alpha)/0.9 = {delta:.2f} (M18: 3.32)")
rec("DISCREPANCY", f"linear propagation of sigma_alpha = 0.45 gives sigma_delta = {s_delta:.2f}, "
    f"M18 prints 0.83 (p.5); method unstated; not used by the tree")

# ---------------------------------------------------------------- 7 background counts
# M18 p.6: N(>150 uJy) in the ACA primary beam (FWHM ~39") = 13 +10 -8, from Carniani 2015.
# C15 Table 3, 1.3 mm Schechter: phi* = (1.8+-0.4)e3 deg^-2, S* = 1.7+-0.2 mJy, alpha = -2.08+-0.11
# dN/dS dS = phi* (S/S*)^a exp(-S/S*) d(S/S*)  ->  N(>S) = phi* Gamma(a+1, S/S*)
def N_schechter(S, phi, Ss, a):
    return phi * float(mp.gammainc(a + 1, S / Ss, mp.inf))
N_c = N_schechter(0.15, 1.8e3, 1.7, -2.08)
N_c_hi = N_schechter(0.15, 2.2e3, 1.5, -2.19)
N_c_lo = N_schechter(0.15, 1.4e3, 1.9, -1.97)
# G20 Table 4 (1.2 mm): N(>=125.9 uJy)=14800, N(>=158.5)=10600 deg^-2; S_1.2 = S_1.3/0.95 (G20 K_1.3=0.95)
S12 = 0.150 / 0.95
N_g = 14800 * (10600 / 14800) ** ((math.log10(S12 * 1e3) - math.log10(125.9)) /
                                   (math.log10(158.5) - math.log10(125.9)))
ARCSEC2_DEG2 = 1 / 3600**2
areas = {
    "disk r = FWHM/2 = 19.5\"": math.pi * 19.5**2,
    "disk r = 23\" (the 30 au ring radius, A17 p.6)": math.pi * 23**2,
    "disk to PB = 20% (r = 29.7\", A17 Fig 1 extent)": math.pi * (19.5 * math.sqrt(math.log(5) / math.log(2)))**2,
    "disk to first null r = 46\" (A17 p.2)": math.pi * 46**2,
    "Gaussian PB-weighted area (integral of PB)": math.pi * 19.5**2 / math.log(2),
}
rec("MEASURED", f"N(>150 uJy, 1.3 mm) = {N_c:.3g} deg^-2 (C15 Schechter; +-1sig corner range "
    f"{N_c_lo:.3g}-{N_c_hi:.3g}); ASPECS 2020: {N_g:.3g} deg^-2")
for k, A in areas.items():
    Adeg = A * ARCSEC2_DEG2
    rec("MEASURED", f"{k}: {A:.0f} arcsec^2 -> C15 {N_c*Adeg:.1f} "
        f"[{N_c_lo*Adeg:.1f}-{N_c_hi*Adeg:.1f}], ASPECS-2020 {N_g*Adeg:.1f}  (M18: 13 +10 -8)")
A_needed = 13 / N_c / ARCSEC2_DEG2
rec("DISCREPANCY", f"13 sources needs {A_needed:.0f} arcsec^2 at the C15 density, a disk of radius "
    f"{math.sqrt(A_needed/math.pi):.0f}\" -- beyond the ~46\" first null; the literal 'within the "
    f"primary beam (FWHM ~39\")' reading gives ~{N_c*areas[list(areas)[0]]*ARCSEC2_DEG2:.1f}. "
    f"M18 states neither the area nor the formula; the figure is NOT REPRODUCED here, and is not "
    f"thereby refuted (cosmic variance, Galactic-plane sources, a different count model)")

ok = [t for t, _ in out]
print("\nSUMMARY:", {t: ok.count(t) for t in sorted(set(ok))})
