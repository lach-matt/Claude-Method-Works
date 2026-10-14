#!/usr/bin/env python3
"""D67 audit 1807.06209-zrec -- re-derivation of z_* = 1089.92 (Planck 2018 VI, Table 2)
as permute.py uses it (Z_REC, permute.py:179; 'factor of 1,091', permute.py:66-73, 537).

Sections
  A  source transcription: the cached verbatim alphaXiv page text of 1807.06209v4 carries
     the z_* row of Table 2 (Plik) and Table A.1 (CamSpec); the tree's 1089.92 is the
     TT,TE,EE+lowE+lensing column.
  B  the tree, imported READ-ONLY (bytecode writing disabled): Z_REC, 1+z, T_rec.
  C  sympy: permute.ratio_from_temperature is identically 1+z -- an identity, not a measurement.
  D  CAMB 2.0.4 (pip --target scratchpad, not vendored) recomputes z_* at the Planck 2018
     Plik best-fit point (Table 1): independent Boltzmann-code re-derivation of the number.
  E  CAMB: z_* moves with the expansion-history inputs (N_eff, omega_c) -> z_* is a derived
     parameter of a model of a(t), not 'independent of any model of a(t)'.
  F  CAMB + Saha: 'recombination' by other conventional definitions (x_e = 0.5, Saha 50%)
     lies at a different redshift from z_* (optical-depth/visibility definition).
  G  robustness: every column and every variant keeps 1+z ~ 10^3 >> 1; the tree's qualitative
     conclusion (a dimensionless ratio changed) does not move; rounding of 'factor 1,091'.
Exit 0 iff every check passes.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
SP = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
CACHE = SP + "/src/casmag/all/1807.06209v4.txt"
DESI = SP + "/src/casmag/all/2503.14738v3.txt"
sys.path.insert(0, SP + "/pkgs/camb")

FAIL = []


def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  -- " + detail if detail else ""))
    if not ok:
        FAIL.append(name)


# ------------------------------------------------------------------ A
print("\n== A. source transcription (cached verbatim pages of 1807.06209v4)")
txt = open(CACHE, encoding="utf-8").read()
p16 = txt.split("===== PAGE 16 =====")[1].split("===== PAGE 17 =====")[0]
chk("Table 2 caption: 'Parameter 68 % intervals for the base-ΛCDM model'",
    "Parameter 68 % intervals for the base-ΛCDM model" in p16)
chk("Table 2 caption: 'The middle group lists derived parameters'",
    "The middle group lists derived parameters" in p16)
chk("Table 2 caption: Y_P from BBN ('helium mass fraction used is predicted by BBN')",
    "helium mass fraction" in p16 and "predicted by BBN" in p16)
PLIK = {"TT+lowE": (1090.30, 0.41), "TE+lowE": (1089.57, 0.42), "EE+lowE": (1087.8, 1.65),
        "TT,TE,EE+lowE": (1089.95, 0.27), "TT,TE,EE+lowE+lensing": (1089.92, 0.25),
        "+BAO": (1089.80, 0.21)}
CAMSPEC = {"TT+lowE": (1090.26, 0.41), "TE+lowE": (1089.51, 0.42), "EE+lowE": (1088.8, None),
           "TT,TE,EE+lowE": (1089.99, 0.28), "TT,TE,EE+lowE+lensing": (1089.99, 0.26),
           "+BAO": (1089.88, 0.22)}
chk("z_* row (Plik) '1090.30 ± 0.41 1089.57 ± 0.42 1087.8' present",
    "1090.30 ± 0.41 1089.57 ± 0.42 1087.8" in p16)
chk("z_* row (Plik) '1089.95 ± 0.27 1089.92 ± 0.25 1089.80 ± 0.21' present",
    "1089.95 ± 0.27 1089.92 ± 0.25 1089.80 ± 0.21" in p16)
pA1 = txt.split("===== PAGE 71 =====")[1]
chk("Table A.1 (CamSpec) z_* '1089.99 ± 0.28 1089.99 ± 0.26 1089.88 ± 0.22' present",
    "1089.99 ± 0.28 1089.99 ± 0.26 1089.88 ± 0.22" in pA1)
chk("baseline is TT,TE,EE+lowE+lensing ('Our baseline results are based on Planck')",
    "Our baseline results are based on Planck" in p16)
p15 = txt.split("===== PAGE 15 =====")[1].split("===== PAGE 16 =====")[0]
chk("Table 1 caption: 'around 0.5 σ may be more realistic, and values should not be overinterpreted'",
    "around 0.5 σ may be more realistic, and values should not be overinterpreted" in p15)
chk("T_CMB = 2.7255 K (Fixsen 2009) adopted", "2.7255K (Fixsen 2009)" in txt)
chk("Planck calls r_* 'the comoving sound hori- zon at recombination'",
    "zon at recombination" in txt)
d = open(DESI, encoding="utf-8").read()
chk("DESI DR2 (2503.14738v3 p.5) 'end of recombina- tion, at redshift z ∗  ≈ 1089'",
    "tion, at redshift z" in d and "≈ 1089" in d)

# ------------------------------------------------------------------ B
print("\n== B. the tree, imported read-only")
sys.path.insert(0, TREE)
import permute  # noqa: E402

chk("permute.Z_REC == 1089.92 (Planck Table 2 baseline column)", permute.Z_REC == 1089.92)
chk("permute.T_CMB == 2.7255", permute.T_CMB == 2.7255)
onez = permute.scale_ratio_since()
chk("1 + z = 1090.92", abs(onez - 1090.92) < 1e-9, "%.6f" % onez)
Trec = permute.temperature_at()
chk("T_rec = T0(1+z) = 2973.30 K (tree prints 2973.3)", abs(Trec - 2973.3025) < 1e-3, "%.4f K" % Trec)
chk("CamSpec baseline would give 1+z = 1090.99 (+0.07, 0.27 sigma)",
    abs((1 + CAMSPEC["TT,TE,EE+lowE+lensing"][0]) - 1090.99) < 1e-9)

# ------------------------------------------------------------------ C
print("\n== C. sympy: ratio_from_temperature is an identity")
import sympy as sp  # noqa: E402

z, T0 = sp.symbols("z T0", positive=True)
expr = (T0 * (1 + z)) / T0 - (1 + z)
chk("T0(1+z)/T0 - (1+z) == 0 identically (for every T0, z)", sp.simplify(expr) == 0)
vals = [permute.ratio_from_temperature(1089.92, t) for t in (1.0, 2.7255, 1000.0)]
chk("tree's ratio_from_temperature returns 1+z whatever T0 is (T0 = 1, 2.7255, 1000 K)",
    all(abs(v - 1090.92) < 1e-9 for v in vals), str(vals))
print("     -> 'ratio from the CMB temperature alone' re-reads the input z; T_rec is computed")
print("        from z (temperature_at), not measured. The check at permute.py:428 is a tautology.")

# ------------------------------------------------------------------ D
print("\n== D. CAMB recomputation at the Planck 2018 Plik best fit (Table 1)")
try:
    import camb  # noqa: E402
    import numpy as np  # noqa: E402
    HAVE_CAMB = True
except Exception as e:  # pragma: no cover
    HAVE_CAMB = False
    chk("CAMB importable from scratchpad pkgs/camb", False, repr(e))

BF = dict(cosmomc_theta=1.040909e-2, ombh2=0.022383, omch2=0.12011, mnu=0.06, omk=0, tau=0.0543)


def zstar(**kw):
    q = dict(BF)
    q.update(kw)
    p = camb.CAMBparams()
    p.set_cosmology(**q)
    p.InitPower.set_params(As=math.exp(3.0448) * 1e-10, ns=0.96605)
    r = camb.get_background(p)
    return r.get_derived_params()["zstar"], r, p


if HAVE_CAMB:
    print("     CAMB", camb.__version__)
    zs, res, par = zstar()
    chk("CAMB z_* at best fit within 0.25 (1 sigma) of 1089.92", abs(zs - 1089.92) < 0.25,
        "z_* = %.3f, H0 = %.3f, YHe = %.4f, TCMB = %.4f" % (zs, par.H0, par.YHe, par.TCMB))
    der = res.get_derived_params()
    chk("CAMB z_drag within 0.30 of Table 2's 1059.94", abs(der["zdrag"] - 1059.94) < 0.30,
        "%.3f" % der["zdrag"])
    chk("CAMB 100 theta_* within 0.0003 of Table 1 best fit 1.041085",
        abs(der["thetastar"] - 1.041085) < 3e-4, "%.6f" % der["thetastar"])

    # -------------------------------------------------------------- E
    print("\n== E. z_* depends on the expansion history (model of a(t))")
    rows = []
    for lab, kw in (("N_eff = 2.0", dict(nnu=2.0)), ("N_eff = 4.0", dict(nnu=4.0)),
                    ("omega_c -10%", dict(omch2=0.12011 * 0.9)),
                    ("omega_c +10%", dict(omch2=0.12011 * 1.1)),
                    ("omega_b -10%", dict(ombh2=0.022383 * 0.9)),
                    ("omega_b +10%", dict(ombh2=0.022383 * 1.1))):
        zz = zstar(**kw)[0]
        rows.append((lab, zz))
        print("     %-14s z_* = %8.2f   shift = %+6.2f  (%+.2f sigma of Table 2)" %
              (lab, zz, zz - zs, (zz - zs) / 0.25))
    chk("z_* moves by > 1 sigma (0.25) when only the expansion-rate inputs (N_eff, omega_c) change",
        all(abs(zz - zs) > 0.25 for lab, zz in rows[:4]))
    chk("but every variant keeps z_* within 1% of 1089.9",
        all(abs(zz - zs) / zs < 0.01 for lab, zz in rows))

    # -------------------------------------------------------------- F
    print("\n== F. 'recombination' by other definitions")
    zg = np.linspace(800, 1700, 9001)
    ev = res.get_background_redshift_evolution(zg, ["x_e", "visibility"], format="array")
    xe, vis = ev[:, 0], ev[:, 1]
    zpeak = zg[np.argmax(vis)]
    i = np.where(np.diff(np.sign(xe - 0.5)))[0]
    zhalf = float(zg[i[0]])
    xe_at = float(np.interp(zs, zg, xe))
    chk("visibility-function peak within 2 of z_*", abs(zpeak - zs) < 2, "peak z = %.1f" % zpeak)
    chk("CAMB x_e = 0.5 (half of H recombined) at z ~ 1275, well above z_*",
        1260 < zhalf < 1290, "z(x_e=0.5) = %.1f; x_e(z_*) = %.3f" % (zhalf, xe_at))

# Saha (equilibrium; named approximation -- overestimates the recombination redshift)
k_B, hbar, m_e, c = 1.380649e-23, 1.054571817e-34, 9.1093837015e-31, 2.99792458e8
eV, m_p, G = 1.602176634e-19, 1.67262192369e-27, 6.67430e-11
B_H = 13.605693122994 * eV
MPC = 3.0856775814913673e22
rho_crit_h2 = 3 * (100e3 / MPC) ** 2 / (8 * math.pi * G)       # kg/m^3 per h^2


def z_saha_half(B=B_H, ombh2=0.02237, YP=0.2454, T0=2.7255):
    nH0 = (1 - YP) * ombh2 * rho_crit_h2 / m_p
    f = lambda zz: _x(zz, B, nH0, T0) - 0.5
    lo, hi = 1000.0, 2500.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def _x(zz, B, nH0, T0):
    T = T0 * (1 + zz)
    nH = nH0 * (1 + zz) ** 3
    S = (m_e * k_B * T / (2 * math.pi * hbar ** 2)) ** 1.5 * math.exp(-B / (k_B * T)) / nH
    return (-S + math.sqrt(S * S + 4 * S)) / 2       # x^2/(1-x) = S


zS = z_saha_half()
chk("Saha 50% H recombination at z ~ 1370 with Planck omega_b, Y_P (textbook ~1380, T ~ 3700-3800 K)", 1350 < zS < 1410,
    "z = %.1f, T = %.0f K" % (zS, 2.7255 * (1 + zS)))
zS1 = z_saha_half(B=1.01 * B_H)
chk("(1+z_rec) scales ~ linearly with the binding energy m_e alpha^2 c^2/2 (+1% B -> ~+1%)",
    0.8 < ((1 + zS1) / (1 + zS) - 1) / 0.01 < 1.2, "d ln(1+z)/d ln B = %.3f" % (((1 + zS1) / (1 + zS) - 1) / 0.01))

# ------------------------------------------------------------------ G
print("\n== G. robustness of the tree's conclusion and of the rounding")
allz = [v[0] for v in PLIK.values()] + [v[0] for v in CAMSPEC.values()]
if HAVE_CAMB:
    allz += [zz for lab, zz in rows] + [zhalf, zS]
chk("every READ column / computed variant / definition gives 1+z in [1088, 1400]: >> 1",
    all(1088 <= 1 + v <= 1400 for v in allz), "min %.1f max %.1f" % (1 + min(allz), 1 + max(allz)))
chk("'factor of 1,091' = round(1+z) at the baseline 1089.92", round(1 + 1089.92) == 1091)
rnd = sorted({round(1 + v) for v in allz[:12]})
print("     round(1+z) over the 12 Planck columns (Plik+CamSpec):", rnd)
chk("'1,091' holds for 10 of 12 Planck columns (EE+lowE: 1089 Plik, 1090 CamSpec)",
    sum(1 for v in allz[:12] if round(1 + v) == 1091) == 10)

print("\n%d FAIL" % len(FAIL) if FAIL else "\nALL PASS")
sys.exit(1 if FAIL else 0)
