#!/usr/bin/env python3
"""DOCKET 67 -- audit of the external datum 'codata-proton-mass'.

Sources READ here (READ-VIA-RESTATEMENT, the CODATA papers themselves were not
reachable: alphaXiv quota exhausted, arxiv.org / physics.nist.gov egress-blocked):
  * scipy 1.17.1  scipy/constants/_codata.py : txt2018 and txt2022, the NIST
    ASCII tables of the CODATA 2018 and 2022 adjustments, as parsed by scipy
    (_physical_constants_2018 / _physical_constants_2022).
  * astropy 7.1.0 astropy/constants/codata2018.py (independent restatement of
    the 2018 m_p), extracted from the pypi wheel into ../pkgs/.

Checks:
  1. the tree's two literals against CODATA 2018 / 2022;
  2. the 2018 -> 2022 shift, in units of each adjustment's sigma;
  3. RE-DERIVATION of m_p from the chain m_p = A_r(p) m_u, m_u = m_e / A_r(e),
     m_e = 2 h R_inf / (c alpha^2), for both adjustments, and a sympy log-derivative
     decomposition of the shift into alpha, R_inf, A_r(e), A_r(p);
  4. what the shift and the arrival.py truncation do to every tree number
     resting on it (baryons_in(100 kg), magsail distances);
  5. the tree's added hypothesis 'every baryon counted at the proton mass'
     against mass-per-baryon of H, 4He, 12C atoms computed from CODATA 2022;
  6. a discrepancy found in passing in arrival.py (prose vs computed magsail).
Exit 0 iff every assertion holds.
"""
import math, os, re, sys
import sympy as sp
import scipy
import scipy.constants._codata as cod

ok = True
def chk(label, cond, detail=""):
    global ok
    ok &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "FAIL", label, detail))

C18, C22 = cod._physical_constants_2018, cod._physical_constants_2022
def v(tab, k): return tab[k][0]
def u(tab, k): return tab[k][2]

print("scipy", scipy.__version__, "| current set:", cod._current_codata)
TREE_WF = 1.67262192369e-27     # warpfolder.py:190, wavecorridor.py:196
TREE_AR = 1.67262192e-27        # arrival.py:25, gate1.py:16, stock.py:234, stockgate.py:419

mp18, ump18 = v(C18, "proton mass"), u(C18, "proton mass")
mp22, ump22 = v(C22, "proton mass"), u(C22, "proton mass")
print("\n1. THE LITERALS")
print("  CODATA 2018 m_p = %.11e +- %.2e kg (rel %.1e)" % (mp18, ump18, ump18 / mp18))
print("  CODATA 2022 m_p = %.11e +- %.2e kg (rel %.1e)" % (mp22, ump22, ump22 / mp22))
chk("warpfolder.py:190 == CODATA 2018 exactly", TREE_WF == mp18)
chk("warpfolder.py:190 != CODATA 2022 (superseded)", TREE_WF != mp22)
# astropy independent restatement of 2018
here = os.path.dirname(os.path.abspath(__file__))
ap = os.path.join(here, "..", "pkgs", "astropy", "constants", "codata2018.py")
if os.path.exists(ap):
    m = re.search(r'"m_p", "Proton mass", ([0-9.e-]+), "kg", ([0-9.e-]+)', open(ap).read())
    chk("astropy 7.1.0 codata2018 m_p == scipy txt2018 m_p",
        float(m.group(1)) == mp18 and abs(float(m.group(2)) - ump18) < 1e-40,
        "(%s +- %s)" % (m.group(1), m.group(2)))
else:
    print("  (astropy restatement not extracted; skipped)")
rt = (TREE_AR - mp18) / mp18
chk("arrival.py:25 is CODATA 2018 truncated to 9 s.f.", "%.8e" % mp18 == "%.8e" % TREE_AR,
    "rel diff %.2e (= %.1f sigma_2018)" % (rt, (TREE_AR - mp18) / ump18))

print("\n2. THE 2018 -> 2022 SHIFT")
d = mp22 - mp18
print("  delta = %.3e kg, rel %.3e, = %.2f sigma_2018 = %.2f sigma_2022"
      % (d, d / mp18, d / ump18, d / ump22))
chk("shift exceeds 4 sigma of the 2018 value", d / ump18 > 4.0)
chk("shift is below 2e-9 relative", abs(d / mp18) < 2e-9)

print("\n3. RE-DERIVATION  m_p = A_r(p) * (2 h R_inf / (c alpha^2)) / A_r(e)")
a, R, h, c, Are, Arp = sp.symbols("alpha R_inf h c A_re A_rp", positive=True)
mp_expr = Arp * (2 * h * R / (c * a**2)) / Are
for name, tab, mptab, ump in (("2018", C18, mp18, ump18), ("2022", C22, mp22, ump22)):
    subs = {a: sp.Float(v(tab, "fine-structure constant"), 30),
            R: sp.Float(v(tab, "Rydberg constant"), 30),
            h: sp.Float(v(tab, "Planck constant"), 30),
            c: sp.Float(v(tab, "speed of light in vacuum"), 30),
            Are: sp.Float(v(tab, "electron relative atomic mass"), 30),
            Arp: sp.Float(v(tab, "proton relative atomic mass"), 30)}
    mp_chain = float(mp_expr.subs(subs))
    chk("%s chain reproduces tabulated m_p within 0.2 sigma" % name,
        abs(mp_chain - mptab) < 0.2 * ump,
        "chain %.12e vs table %.11e (%.3f sigma)" % (mp_chain, mptab, (mp_chain - mptab) / ump))
    mu = v(tab, "atomic mass constant")
    chk("%s A_r(p)*m_u reproduces m_p within 0.2 sigma" % name,
        abs(v(tab, "proton relative atomic mass") * mu - mptab) < 0.2 * ump)
# decomposition of the relative shift: dln m_p = dln A_rp + dln R - 2 dln alpha - dln A_re
terms = {}
for sym, key in ((a, "fine-structure constant"), (R, "Rydberg constant"),
                 (Are, "electron relative atomic mass"), (Arp, "proton relative atomic mass")):
    exp_ = sp.simplify(sym * sp.diff(sp.log(mp_expr), sym))    # elasticity
    rel = (v(C22, key) - v(C18, key)) / v(C18, key)
    terms[key] = float(exp_) * rel
    print("  %-32s elasticity %+d  rel change %+.3e  contribution %+.3e"
          % (key, int(exp_), rel, terms[key]))
tot = sum(terms.values())
print("  sum %+.4e   observed %+.4e" % (tot, d / mp18))
chk("log-derivative decomposition reproduces the observed shift to 2%",
    abs(tot - d / mp18) < 0.02 * abs(d / mp18))
chk("alpha carries >95% of the shift",
    terms["fine-structure constant"] / tot > 0.95,
    "(%.1f%%)" % (100 * terms["fine-structure constant"] / tot))

print("\n4. WHAT THE MOVE DOES TO THE TREE'S NUMBERS")
for lbl, mp in (("tree WF (2018)", TREE_WF), ("tree AR (trunc)", TREE_AR), ("CODATA 2022", mp22)):
    print("  %-16s baryons_in(100 kg) = %.6e" % (lbl, 100.0 / mp))
chk("warpfolder chkrel 5.979e28 @1e-3 holds under 2022 too",
    abs(100.0 / mp22 - 5.979e28) / 5.979e28 < 1e-3)
cl = 299792458.0; AU = 1.495978707e11; LY = 9.4607304726e15
def mag(m, b, A, mp):
    g = 1 / math.sqrt(1 - b * b)
    return (g - 1) * m * cl**2 / (1e6 * mp * (b * cl)**2 * A)
d_ar, d_22 = mag(1e6, 0.0476, 1e12, TREE_AR) / AU, mag(1e6, 0.0476, 1e12, mp22) / AU
print("  magsail 1e6 kg, 0.0476c, 1e12 m^2: arrival %.6f AU, CODATA2022 %.6f AU, rel %.1e"
      % (d_ar, d_22, (d_22 - d_ar) / d_ar))
chk("arrival.py selftest pin 2001.64 AU @1e-4 holds under 2022", abs(d_22 - 2001.64) / 2001.64 < 1e-4)

print("\n5. ADDED HYPOTHESIS: every baryon counted at the proton mass")
Arp22, Are22 = v(C22, "proton relative atomic mass"), v(C22, "electron relative atomic mass")
Ara22 = v(C22, "alpha particle relative atomic mass")
per = {"1H atom (p+e)": Arp22 + Are22,
       "4He atom (alpha+2e)": (Ara22 + 2 * Are22) / 4,
       "12C atom (A_r = 12 exactly)": 12.0 / 12}
# electron binding energies (<= ~1 keV total for C) are < 1e-7 u per baryon: neglected, stated.
for k, mb in per.items():
    ratio = Arp22 / mb
    print("  %-28s mass/baryon %.9f u  N_true/N_tree = %.5f  100 kg -> %.4e baryons"
          % (k, mb, ratio, 100.0 / (mb * v(C22, "atomic mass constant"))))
r_c = Arp22 / per["12C atom (A_r = 12 exactly)"]
chk("12C: counting at m_p undercounts by >0.7%", r_c - 1 > 0.007, "(%.3f%%)" % (100 * (r_c - 1)))
chk("1H: counting at m_p overcounts by <0.06%", 1 - Arp22 / per["1H atom (p+e)"] < 6e-4)
chk("tree's printed 5.98e28 is not the 3-s.f. count for 12C (6.02e28)",
    "%.2e" % (100.0 / (1.0 * v(C22, "atomic mass constant"))) != "5.98e+28")

print("\n6. DISCREPANCY IN PASSING (arrival.py prose vs computed), not from m_p")
d1 = mag(1e6, 0.0476, 1e12, TREE_AR) / AU
d2 = mag(1e6, 0.866, 1e12, TREE_AR) / LY
print("  computed: %.0f AU from 0.048c, %.3f ly from 0.866c; prose: 810 AU, 2.6 ly" % (d1, d2))
k1, k2 = d1 / 810.0, d2 / 2.6
print("  density factor needed: %.3f (for 810 AU) vs %.4f (for 2.6 ly)" % (k1, k2))
chk("no single change of m_p (or rho) reconciles both prose figures", abs(k1 / k2 - 1) > 1)
chk("m_p would have to move by >100% -- the CODATA datum cannot be the cause", abs(k1 - 1) > 1)

print("\nREDERIVE %s" % ("OK" if ok else "FAILED"))
sys.exit(0 if ok else 1)
