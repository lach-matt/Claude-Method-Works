#!/usr/bin/env python3
"""DOCKET 67 re-derivation for key 1807.06209 (Planck 2018 VI): eta ~ 6.1e-10 (warpfolder.py)
and H_0 = 67.36 km/s/Mpc (cosmo.py -> permute.py).  Reads the tree READ-ONLY (no bytecode written).
Sources READ: cached alphaXiv page text of 1807.06209v4 (pp.1-2,13-17,24,26-27,39-43,62,71),
2112.04510v3 (SH0ES) and 2503.14738v3 (DESI DR2) at scratchpad d67/src/casmag/all/.
"""
import sys, ast, math, os, re, random
sys.dont_write_bytecode = True
import sympy as sp
from scipy import constants as C
from scipy.integrate import quad

TREE = "/home/user/Claude-Method-Works/research/warp-drive"
SRC = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/src/casmag/all/"
ok = True
def chk(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  [%s] %s %s" % ("PASS" if cond else "FAIL", label, detail))

print("A. TRANSCRIPTION against the READ source text")
pl = open(SRC + "1807.06209v4.txt").read()
flat = re.sub(r"\s+", " ", pl)
chk("Table 2 TT,TE,EE+lowE+lensing H0 = 67.36 +- 0.54 printed", "67.27 ± 0.60 67.36 ± 0.54 67.66 ± 0.42" in flat)
chk("Table 2 Omega_b h^2 = 0.02237 +- 0.00015 printed", "0.02236 ± 0.00015 0.02237 ± 0.00015 0.02242 ± 0.00014" in flat)
chk("Table 2 Age 13.797 +- 0.023 printed", "13.800 ± 0.024 13.797 ± 0.023 13.787 ± 0.020" in flat)
chk("abstract: H0 'inferred (model-dependent)' assuming base-LCDM", "inferred (model-dependent) late-Universe parameters" in flat)
chk("abstract: 3.6 sigma tension with local H0", "3.6 σ, tension with local measurements of the Hubble constant" in flat)
chk("conclusions: 4.4 sigma tension with Riess et al. (2019)", "4.4 σ ten- sion with the latest local determination" in flat)
chk("Table 2 caption: Y_P ~ 0.2454 predicted by BBN", "Y P ≈ 0.2454" in flat)
chk("T_CMB = 2.7255 K (Fixsen 2009) adopted", "2.7255K (Fixsen 2009)" in flat)
eta_printed = re.search(r"baryon-to-photon|η\s*=\s*6\.|η 10", flat)
print("     eta printed anywhere in the 17 READ pages: %s (Sec. 7.6, p.52, is NOT in the read set)"
      % ("yes" if eta_printed else "NO"))

cosmo_src = open(os.path.join(TREE, "cosmo.py")).read()
chk("cosmo.py:34 H0_KMSMPC = 67.36 equals Table 2", re.search(r"H0_KMSMPC\s*=\s*67\.36\b", cosmo_src) is not None)
chk("cosmo.py:35 AGE_GYR = 13.797 equals Table 2", re.search(r"AGE_GYR\s*=\s*13\.797\b", cosmo_src) is not None)

print("\nB. SI CONVERSION and theta = 3 H_0 (permute.py:31)")
au = 149597870700                       # m, IAU 2012 exact
pc = sp.Rational(648000) / sp.pi * au   # IAU 2015 exact definition
MPC = float(pc * 10**6)
chk("MPC = 3.0856775814913673e22 m equals IAU 648000/pi au", abs(MPC - 3.0856775814913673e22) / MPC < 1e-15, "%.16e" % MPC)
H0 = 67.36e3 / MPC
theta = 3 * H0
print("     H0 = %.6e /s   theta = %.6e /s   Hubble time = %.4f Gyr" % (H0, theta, 1 / H0 / 3.15576e16))
chk("theta printed '6.549e-18' reproduced", "%.3e" % theta == "6.549e-18")

print("\nC. permute.py:404-406 'cross-checked by the Hubble time' is a tautology, not a cross-check")
chk("cosmo YR = 3.15576e7 is exactly 365.25*86400", 365.25 * 86400.0 == 3.15576e7)
bad = 0
for _ in range(10000):
    h = random.uniform(1, 200) * 1e3 / MPC
    a = 1.0 / h / (1e9 * 365.25 * 86400.0); b = 1.0 / h / (1e9 * 3.15576e7)
    bad += abs(a - b) > 1e-6 * max(1, b)
chk("identity holds for EVERY H0 in 1..200 km/s/Mpc (so it can never fail)", bad == 0, "failures=%d/10000" % bad)

print("\nD. eta FROM Omega_b h^2 (symbolic, then CODATA via scipy.constants)")
Ob, G, k, hbar, c, T, mb, H100 = sp.symbols("Omega_bh2 G k hbar c T m_b H100", positive=True)
rho_c = 3 * H100**2 / (8 * sp.pi * G)                        # per h^2
n_gam = 2 * sp.zeta(3) / sp.pi**2 * (k * T / (hbar * c))**3
eta_expr = sp.simplify(Ob * rho_c / mb / n_gam)
print("     eta =", eta_expr)
chk("sympy: eta is linear in Omega_b h^2 and ~ T^-3", sp.simplify(sp.diff(sp.log(eta_expr), T) * T) == -3
    and sp.simplify(sp.diff(eta_expr, Ob, 2)) == 0)
Y = 0.2454
mH = 1.00782503223 * C.atomic_mass; mHe = 4.00260325413 * C.atomic_mass
m_per_baryon = 1.0 / ((1 - Y) / mH + Y / (mHe / 4))
subs = {G: C.G, k: C.k, hbar: C.hbar, c: C.c, T: 2.7255, H100: 100e3 / MPC}
coef = {}
for name, m in (("m_p", C.m_p), ("m_u", C.atomic_mass), ("mean, Y_P=0.2454", m_per_baryon)):
    coef[name] = float(eta_expr.subs(subs).subs({mb: m, Ob: 1})) * 1e10
    print("     eta_10 / (Omega_b h^2) with %-18s = %.2f" % (name, coef[name]))
cY = coef["mean, Y_P=0.2454"]
rows = (("Table 2 TT,TE,EE+lowE+lensing", 0.02237, 0.00015),
        ("abstract", 0.0224, 0.0001),
        ("Table 2 +BAO", 0.02242, 0.00014),
        ("Table 2 TT+lowE (lowest)", 0.02212, 0.00022),
        ("Table 2 EE+lowE (highest)", 0.0240, 0.0012))
for name, v, e in rows:
    print("     %-32s Omega_b h^2 = %.5f -> eta = (%.3f +- %.3f)e-10" % (name, v, cY * v / 10, cY * e / 10))
eta0 = cY * 0.02237 * 1e-10
chk("tree's 6.1e-10 equals Planck-derived eta at 2 s.f.", "%.1e" % eta0 == "6.1e-10", "(%.4e)" % eta0)
chk("tree's 6.1e-10 inside the 68%% band of the baseline", abs(6.1e-10 - eta0) < 1.0 * cY * 0.00015e-10 * 1.0 + 0.03e-10,
    "(offset %.2e, sigma %.2e; offset is the 2-s.f. rounding)" % (6.1e-10 - eta0, cY * 0.00015e-10))
dT = 3 * 0.0006 / 2.7255
print("     T_CMB +-0.0006 K moves eta by +-%.3f%%; the m_p-vs-mean-mass choice moves it %.2f%%"
      % (100 * dT, 100 * (coef["m_p"] / cY - 1)))

print("\nE. LOAD-BEARING: does any flag in warpfolder.py depend on ETA_BARYON?")
wsrc = open(os.path.join(TREE, "warpfolder.py")).read()
tree = ast.parse(wsrc)
uses = [n.lineno for n in ast.walk(tree) if isinstance(n, ast.Name) and n.id == "ETA_BARYON"]
print("     ETA_BARYON Name nodes at lines:", uses)
flag = [n for n in tree.body if isinstance(n, ast.Assign) and any(getattr(t, "id", "") == "BLUEPRINT_SOURCES_BARYON_NUMBER" for t in n.targets)]
chk("BLUEPRINT_SOURCES_BARYON_NUMBER is a literal constant (no computation)", len(flag) == 1 and isinstance(flag[0].value, ast.Constant) and flag[0].value.value is False)
chk("ETA_BARYON used only in its assignment and one print (report())", len(uses) == 2)

print("\nF. permute.py's falsification under every H0 value READ (tree imported read-only, cosmo patched in memory)")
sys.path.insert(0, TREE)
import cosmo, permute
readvals = (("Planck 2018 TT,TE,EE+lowE+lensing", 67.36, 0.54),
            ("Planck 2018 +BAO", 67.66, 0.42),
            ("SH0ES 2112.04510v3 baseline", 73.04, 1.04),
            ("DESI DR2+BBN 2503.14738v3 eq.19", 68.51, 0.58),
            ("DESI DR2+CMB 2503.14738v3", 68.17, 0.28))
orig = cosmo.H0_KMSMPC
for name, v, e in readvals:
    cosmo.H0_KMSMPC = v
    th = permute.expansion_scalar()
    print("     %-34s H0 = %6.2f +- %.2f -> theta = %.4e /s, %5.0f sigma from 0, is_a_permutation=%s"
          % (name, v, e, th, v / e, permute.is_a_permutation(th)))
    ok &= (permute.is_a_permutation(th) is False)
cosmo.H0_KMSMPC = 0.0
chk("the verdict flips ONLY at H0 = 0 exactly (the conclusion depends on sign(H0), not its value)",
    permute.is_a_permutation(permute.expansion_scalar()) is True)
cosmo.H0_KMSMPC = orig
spread = (73.04 - 67.36) / 67.36
print("     the PRINTED 6.549e-18 moves by %.1f%% across the READ tension; the verdict does not" % (100 * spread))

print("\nG. ANCILLARY (cosmo.py:22 companions, same source): age and comoving particle horizon in flat base-LCDM")
h = 0.6736; Om = 0.3153
Og = float(sp.pi**2 / 15 * (C.k * 2.7255)**4 / (C.hbar * C.c)**3 / C.c**2 / (3 * (100e3 / MPC)**2 / (8 * math.pi * C.G))) / h**2
Or = Og * (1 + 3.046 * 7 / 8 * (4 / 11)**(4 / 3))
OL = 1 - Om - Or
Hs = h * 100e3 / MPC
E = lambda a: math.sqrt(Or / a**4 + Om / a**3 + OL)
age = quad(lambda a: 1 / (a * E(a)), 0, 1, limit=200)[0] / Hs / 3.15576e16
chi = quad(lambda a: 1 / (a * a * E(a)), 0, 1, limit=200)[0] * C.c / Hs / MPC / 1e3
print("     Omega_gamma h^2 = %.4e; age = %.3f Gyr (Planck 13.797); horizon = %.2f Gpc (cosmo.py 14.26)"
      % (Og * h * h, age, chi))
chk("age reproduced to 0.1% (massless-neutrino approximation)", abs(age - 13.797) / 13.797 < 1e-3)
zs = 1089.92
Dstar = quad(lambda a: 1 / (a * a * E(a)), 1 / (1 + zs), 1, limit=200)[0] * C.c / Hs / MPC
Dplanck = 144.43 / (1.04110 / 100)          # r_* / theta_*, Table 2 (READ)
print("     integrator check: comoving distance to z_* = %.1f Mpc vs Planck r_*/theta_* = %.1f Mpc" % (Dstar, Dplanck))
chk("integrator reproduces Planck's own r_*/theta_* to 0.3%", abs(Dstar - Dplanck) / Dplanck < 3e-3)
print("     conformal horizon at z_* adds %.0f Mpc; horizon today = %.3f Gpc" % (chi * 1e3 - Dstar, chi))
disc = (14.26 - chi) / chi
print("     RECORDED DISCREPANCY (not a refutation; outside this key's load path): cosmo.py:22/36 'HORIZON_GPC = 14.26 PINNED'")
print("       is %.2f%% above the flat base-LCDM value %.2f Gpc derived from the same Planck 2018 column;" % (100 * disc, chi))
print("       14.26 Gpc is NOT printed in the 17 READ pages.  Its origin is NAMED-NOT-READ.")
for lab, hh, om in (("h=0.6774, Om=0.3089 (Planck 2015 values, NAMED-NOT-READ)", 0.6774, 0.3089),
                    ("h=0.70, Om=0.30 (round values)", 0.70, 0.30), ("h=0.71, Om=0.27 (WMAP-era, NAMED-NOT-READ)", 0.71, 0.27)):
    orr = Og * h * h / hh**2 * (1 + 3.046 * 7 / 8 * (4 / 11)**(4 / 3)); ol = 1 - om - orr
    Ee = lambda a: math.sqrt(orr / a**4 + om / a**3 + ol)
    x = quad(lambda a: 1 / (a * a * Ee(a)), 0, 1, limit=200)[0] * C.c / (hh * 100e3 / MPC) / MPC / 1e3
    print("       what-if %-58s horizon = %.2f Gpc" % (lab, x))
print("\nALL PASS" if ok else "\nSOME CHECK FAILED")
sys.exit(0 if ok else 1)
