#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key codata-2018-constants.

What is checked (exact rational arithmetic, sympy Rational, on decimal literals):
  1. TRANSCRIPTION: every constant the tree types (drivensource.py:278-280, tolman.py:1122-1133,
     candidates.py:315-317, nonstatic.py:254, ladder.py:53-55, achievable.py:299-303,
     spec.py:135-137, phase1.py:212, seatindex.py:128-129, foliation.py:579-580, higgs.py:205)
     against the NIST CODATA 2018 ASCII table as embedded verbatim in scipy.constants._codata
     (txt2018; scipy 1.17.1) -- the RMP paper itself (Tiesinga et al., RMP 93, 025010 (2021)) has
     no arXiv copy and is NAMED-NOT-READ.
  2. CURRENCY: the same constants against CODATA 2022 (arXiv:2409.03787 Table XXXII/XXXIII, READ;
     cross-checked against scipy txt2022). G: 2022 == 2018 ("identical", 2409.03787 Sec. I.B.11).
  3. INTERNAL CONSISTENCY of the tree's 2018 EM set: alpha from mu0; eps0 = 1/(mu0 c^2);
     a0 = hbar/(alpha m_e c); E_h = alpha^2 m_e c^2; E_h = 2 h c R_inf.
  4. SHIFTS 2018 -> 2022 in units of u(2018), against 2409.03787 Table XXXVIII's D_r column.
  5. l_P = sqrt(hbar G / c^3) from the tree's three constants against CODATA 1.616255(18)e-35.
  6. SENSITIVITY: each rests_on_it figure whose G-exponent is closed-form, moved by
     (a) CODATA's own 1 sigma, (b) published alternative consensus values of G
     (Merkatas et al. 1905.09551 Table 4: DL 6.67399, BMM 6.67408; Rinaldi et al. 2209.07416:
     6.6740 +-0.0015 at 90%), (c) the extremes of the 16 CODATA input data (Table XXX:
     BIPM-01 6.67559, LENS-14 6.67191). Measured by importing achievable.py / phase1.py /
     higgs.py READ-ONLY and patching the module attribute in memory (never on disk).
Reads research/warp-drive read-only (import with bytecode writing off); writes nothing there.
Exit 1 on any failed check.
"""
import sys, math, re
sys.dont_write_bytecode = True
from sympy import Rational as R, sqrt, pi, log, N, nsimplify
import scipy.constants._codata as cod

sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")

fails = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("   " + detail if detail else ""))
    if not ok:
        fails.append(name)

def Q(x):
    return R(repr(x)) if not isinstance(x, str) else R(x)

def table(txt):
    out = {}
    for line in txt.splitlines():
        if len(line) < 60 or line.startswith(("Quantity", "---", " ")):
            continue
        name = line[:60].strip()
        rest = line[60:].split()
        if not rest:
            continue
        val = rest[0]
        unc = rest[1] if len(rest) > 1 else "0"
        val = val.replace("...", "")
        unc = "0" if unc.startswith("(exact") else unc
        try:
            out[name] = (R(val.replace(" ", "")), R(unc))
        except Exception:
            pass
    return out

# the scipy table text keeps NIST's digit spacing; rebuild values from the parsed dicts instead
T18 = {k: (Q(v[0]), Q(v[2])) for k, v in cod._physical_constants_2018.items()}
T22 = {k: (Q(v[0]), Q(v[2])) for k, v in cod._physical_constants_2022.items()}

import drivensource, tolman, candidates, nonstatic, ladder, achievable, spec, phase1, seatindex
import foliation, higgs

rows = [  # (tree site, tree value, NIST name)
    ("drivensource.py:278 EPS0", drivensource.EPS0, "vacuum electric permittivity"),
    ("drivensource.py:279 C", drivensource.C, "speed of light in vacuum"),
    ("drivensource.py:280 G", drivensource.G, "Newtonian constant of gravitation"),
    ("tolman.py:1125 MU0", tolman.MU0, "vacuum mag. permeability"),
    ("tolman.py:1126 QE", tolman.QE, "elementary charge"),
    ("tolman.py:1127 M_E", tolman.M_E, "electron mass"),
    ("tolman.py:1128 A_BOHR", tolman.A_BOHR, "Bohr radius"),
    ("tolman.py:1129 E_HART", tolman.E_HART, "Hartree energy"),
    ("tolman.py:1133 L_PLANCK_CODATA", tolman.L_PLANCK_CODATA, "Planck length"),
    ("candidates.py:315 G", candidates.G, "Newtonian constant of gravitation"),
    ("candidates.py:316 C", candidates.C, "speed of light in vacuum"),
    ("nonstatic.py:254 G", nonstatic.G, "Newtonian constant of gravitation"),
    ("ladder.py:53 c", ladder.c, "speed of light in vacuum"),
    ("ladder.py:54 G", ladder.G, "Newtonian constant of gravitation"),
    ("achievable.py:301 C_SI", achievable.C_SI, "speed of light in vacuum"),
    ("achievable.py:302 G_SI", achievable.G_SI, "Newtonian constant of gravitation"),
    ("achievable.py:303 L_PLANCK", achievable.L_PLANCK, "Planck length"),
    ("spec.py:135 MU0", spec.MU0, "vacuum mag. permeability"),
    ("spec.py:136 G_SI", spec.G_SI, "Newtonian constant of gravitation"),
    ("phase1.py:212 C_SI", phase1.C_SI, "speed of light in vacuum"),
    ("phase1.py:212 G_SI", phase1.G_SI, "Newtonian constant of gravitation"),
    ("seatindex.py:128 C_SI", seatindex.C_SI, "speed of light in vacuum"),
    ("seatindex.py:129 G_SI", seatindex.G_SI, "Newtonian constant of gravitation"),
    ("foliation.py:579 C_LIGHT", foliation.C_LIGHT, "speed of light in vacuum"),
    ("foliation.py:580 G_NEWTON", foliation.G_NEWTON, "Newtonian constant of gravitation"),
]

print("1. TRANSCRIPTION against NIST CODATA 2018 (scipy txt2018)")
for site, v, name in rows:
    ref, u = T18[name]
    chk("%-34s = CODATA 2018 %s" % (site, name), Q(v) == ref, "tree %s ref %s" % (repr(v), N(ref, 14)))

print("\n   hbar: the tree types 1.054571817e-34 (candidates.py:317, ladder.py:55, achievable.py:299)")
h = R("6.62607015e-34")
hbar_exact = h / (2 * pi)
hb_tree = Q(candidates.HBAR)
rel_hbar = N((hb_tree - hbar_exact) / hbar_exact, 6)
print("   exact h/2pi = %s ; tree - exact relative = %s" % (N(hbar_exact, 17), rel_hbar))
chk("tree hbar is h/2pi truncated at 10 s.f. (DISCREPANCY of display, |rel| < 1e-9)",
    abs(float(rel_hbar)) < 1e-9 and float(rel_hbar) < 0)
chk("all three hbar sites agree", Q(candidates.HBAR) == Q(ladder.HBAR) == Q(achievable.HBAR))
chk("higgs.py:205 GEV_IN_J = e x 1e9 exactly", Q(higgs.GEV_IN_J) == T18["elementary charge"][0] * 10**9)
chk("e exact in 2018 and 2022 (u = 0)", T18["elementary charge"][1] == 0 == T22["elementary charge"][1])
chk("c exact in 2018 and 2022 (u = 0)", T18["speed of light in vacuum"][1] == 0)

print("\n2. CURRENCY: 2018 -> 2022 (2409.03787 Table XXXIII values, typed from the PDF text)")
pdf22 = {  # READ at arXiv:2409.03787 p.50-51
    "Newtonian constant of gravitation": (R("6.67430e-11"), R("0.00015e-11")),
    "vacuum mag. permeability": (R("1.25663706127e-6"), R("0.00000000020e-6")),
    "vacuum electric permittivity": (R("8.8541878188e-12"), R("0.0000000014e-12")),
    "electron mass": (R("9.1093837139e-31"), R("0.0000000028e-31")),
    "Bohr radius": (R("5.29177210544e-11"), R("0.00000000082e-11")),
    "Hartree energy": (R("4.3597447222060e-18"), R("0.0000000000048e-18")),
    "Planck length": (R("1.616255e-35"), R("0.000018e-35")),
    "Rydberg constant": (R("10973731.568157"), R("0.000012")),
}
for k, (v, u) in pdf22.items():
    chk("2409.03787 value == scipy txt2022: %s" % k, v == T22[k][0] and u == T22[k][1])
chk("G 2022 == G 2018 (value and uncertainty)",
    T18["Newtonian constant of gravitation"] == T22["Newtonian constant of gravitation"])
chk("l_P 2022 == l_P 2018", T18["Planck length"] == T22["Planck length"])

print("\n   shifts, 2022 - 2018, relative and in u(2018); Table XXXVIII D_r in brackets")
Dr_table = {"vacuum mag. permeability": R("-4.5"), "vacuum electric permittivity": R("4.5"),
            "Bohr radius": R("-4.5"), "electron mass": R("4.5"), "Hartree energy": R("-0.3"),
            "Rydberg constant": R("-0.3")}
shifts = {}
for k, dr in Dr_table.items():
    v18, u18 = T18[k]; v22, u22 = T22[k]
    rel = (v22 - v18) / v18
    d = (v22 - v18) / u18
    shifts[k] = float(rel)
    print("   %-30s rel %+.3e   D = %+.2f u(2018)   [table %s]" % (k, float(rel), float(d), dr))
    if abs(dr) > 1:
        chk("   sign and |D| within 0.2 of Table XXXVIII for %s" % k,
            (d > 0) == (dr > 0) and abs(abs(d) - abs(dr)) < R("0.2"))
    else:
        same_sign = (d > 0) == (dr > 0)
        chk("   sign agrees with Table XXXVIII for %s" % k, same_sign)
        print("      DISCREPANCY RECORDED: rounded published values give |D| = %.2f, Table XXXVIII prints"
              " %s ('calculated with extra digits'); not adjudicable here" % (abs(float(d)), dr))
chk("largest EM shift < 2e-9 relative", max(abs(s) for s in shifts.values()) < 2e-9)

print("\n3. INTERNAL CONSISTENCY of the tree's 2018 EM set")
c = R(299792458); e = R("1.602176634e-19")
mu0 = Q(tolman.MU0); eps0 = Q(drivensource.EPS0); me = Q(tolman.M_E)
a0 = Q(tolman.A_BOHR); Eh = Q(tolman.E_HART)
alpha = mu0 * e**2 * c / (2 * h)
a18 = T18["fine-structure constant"][0]
print("   alpha from tree mu0 = %s ; CODATA 2018 alpha = %s" % (N(alpha, 14), N(a18, 14)))
chk("alpha(mu0_tree) == CODATA 2018 alpha to < 1e-10 rel", abs((alpha - a18) / a18) < R("1e-10"))
chk("eps0_tree * mu0_tree * c^2 == 1 to < 2e-10", abs(eps0 * mu0 * c**2 - 1) < R("2e-10"),
    "%.3e" % float(eps0 * mu0 * c**2 - 1))
a0_d = hbar_exact / (a18 * me * c)
chk("a0 = hbar/(alpha m_e c) to < 2e-10 rel", abs(N((a0_d - a0) / a0, 20)) < 2e-10,
    "%.3e" % float(N((a0_d - a0) / a0, 20)))
Eh_d = a18**2 * me * c**2
chk("E_h = alpha^2 m_e c^2 to < 5e-10 rel", abs((Eh_d - Eh) / Eh) < R("5e-10"),
    "%.3e" % float((Eh_d - Eh) / Eh))
Eh_R = 2 * h * c * T18["Rydberg constant"][0]
chk("E_h = 2 h c R_inf(2018) to < 2e-12 rel", abs((Eh_R - Eh) / Eh) < R("2e-12"),
    "%.3e" % float((Eh_R - Eh) / Eh))

print("\n4. l_P from the tree's hbar, G, c against CODATA 1.616255(18)e-35")
G = R("6.67430e-11"); uG = R("0.00015e-11")
lP = sqrt(hb_tree * G / c**3)
rel_lP = N(lP / R("1.616255e-35") - 1, 8)
print("   l_P derived = %s ; rel to CODATA = %s ; CODATA u_r = 1.1e-5" % (N(lP, 10), rel_lP))
chk("derived l_P within CODATA 1 sigma", abs(float(rel_lP)) < 1.1e-5)
chk("tolman.py:2772 guard (|rel| < 1e-4) and :2774 (|rel| > 1e-9) both hold",
    1e-9 < abs(float(rel_lP)) < 1e-4)
chk("tolman.L_PLANCK equals this derivation", abs(tolman.L_PLANCK / float(lP) - 1) < 1e-15)

print("\n5. SENSITIVITY of rests_on_it figures to G (closed-form exponents)")
ur = uG / G
print("   CODATA u_r(G) = %.3e" % float(ur))
alts = {
    "CODATA +1 sigma": R("6.67445e-11"),
    "DL consensus (1905.09551 T4)": R("6.67399e-11"),
    "BMM consensus (1905.09551)": R("6.67408e-11"),
    "Rinaldi 90% upper (2209.07416)": R("6.6755e-11"),
    "Rinaldi 90% lower (2209.07416)": R("6.6725e-11"),
    "BIPM-01 (highest input)": R("6.67559e-11"),
    "LENS-14 (lowest input)": R("6.67191e-11"),
}
figs = [  # name, G exponent, base value, printed significant figures
    ("exchange rate c^2/(G Lambda) [phase1, ledger]", -1, 1.348948e26, 7),
    ("l_P [achievable, throatmass, tolman]", R(1, 2), 1.616255e-35, 7),
    ("Planck mass in GeV [higgs]", R(-1, 2), 1.220890e19, 7),
    ("xi_required = (M_red/v)^2 [higgs, excite]", -1, 9.7829068836e31, 11),
    ("T_COEFF = pi c^4/(4G) [seatindex]", -1, None, None),
    ("seating invariant sqrt(2 mu0 T_COEFF) [spec]", R(-1, 2), 1.54562e19, 6),
    ("tension bill 9.7773e40 Pa [tolman sec.9]", -1, 9.7773e40, 5),
]
worst = 0.0
for nm, k, base, sf in figs:
    line = "   %-48s G^%s:" % (nm, k)
    for an, Ga in alts.items():
        r = float((Ga / G) ** k - 1)
        worst = max(worst, abs(r))
        line += "  %s %+.1e" % (an.split(" (")[0].split(" ")[0], r)
    print(line)
    if sf:
        r1 = float((alts["CODATA +1 sigma"] / G) ** k - 1)
        digit_rel = 0.5 * 10 ** (1 - sf)
        print("      printed to %d s.f. (half-ulp %.1e); CODATA 1 sigma moves it %.1e -> %s"
              % (sf, digit_rel, abs(r1),
                 "PRINTED PRECISION EXCEEDS G's" if abs(r1) > digit_rel else "within printed precision"))
chk("largest G-driven relative move over all alternatives < 5e-4 (no figure moves an order)",
    worst < 5e-4, "%.2e" % worst)

print("\n   measured on the tree's own functions (in-memory patch, restored after)")
def patched(mod, attr, val, fn):
    old = getattr(mod, attr)
    setattr(mod, attr, val)
    try:
        return fn()
    finally:
        setattr(mod, attr, old)

base71 = math.log10(achievable.persistence_shortfall(1.0))
print("   achievable persistence_shortfall(1 m) = %.6f orders (tree prints 71.256)" % base71)
chk("71.256 reproduced to 3 decimals", abs(base71 - 71.256) < 5e-4)
for an, Ga in alts.items():
    o = patched(achievable, "G_SI", float(Ga), lambda: math.log10(achievable.persistence_shortfall(1.0)))
    print("      G = %-12s (%s): %.6f orders, moved %+.2e" % (N(Ga, 6), an, o, o - base71))
    chk("      71.256 moves < 1e-3 orders under %s" % an, abs(o - base71) < 1e-3)
ex0 = phase1.exchange_rate()
chk("phase1 exchange rate reproduces 1.348948e26 (7 s.f.)", abs(ex0 / 1.348948e26 - 1) < 5e-7,
    "%.7e" % ex0)
for an, Ga in alts.items():
    ex = patched(phase1, "G_SI", float(Ga), phase1.exchange_rate)
    print("      %s: exchange rate %.6e (%+.2e rel)" % (an, ex, ex / ex0 - 1))

print("\n6. EM 2018 -> 2022 on the tree's EM-dependent figures")
for nm, dep, k in [("tolman B^2/(2 mu0) magnetic pressure", "vacuum mag. permeability", -1),
                   ("spec seating invariant ~ sqrt(mu0)", "vacuum mag. permeability", R(1, 2)),
                   ("drivensource Q^2/(8 pi eps0 c^2)", "vacuum electric permittivity", -1),
                   ("tolman m_e^2 c^2/(e hbar) (Schwinger field)", "electron mass", 2),
                   ("tolman E_h/a0^3 (atomic pressure)", "Bohr radius", -3)]:
    r = (1 + shifts[dep]) ** float(k) - 1
    print("   %-46s moves %+.2e" % (nm, r))
    chk("   %s moves < 1e-8" % nm, abs(r) < 1e-8)

print("\n%d FAIL" % len(fails))
sys.exit(1 if fails else 0)
