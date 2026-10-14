"""DOCKET 67 -- rederive: physical-constants-and-proxima (owner specthm.py).

Reads the tree READ-ONLY (regex on source; no import of any tree module, so
nothing under research/ can be written).  Sources, md5-asserted:
  scipy 1.17.1 scipy/constants/_codata.py  -- NIST CODATA 2006..2022 ASCII tables
  arXiv:2409.03787v1 page text (CODATA 2022)
  arXiv:2104.14972v2 page text (Reyle+2021, Table 1: Gaia EDR3 row of Proxima)
  arXiv:2512.08533v1 page text (Libralato+2025, HST parallax of Proxima)
  arXiv:1510.07674v1 page text (IAU 2015 B3 nominal solar constants)
Exit 0 iff every check passes.
"""
import hashlib, math, re, sys
import sympy as sp

D = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
T = "/home/user/Claude-Method-Works/research/warp-drive"
SRC = {
    "codata": (D + "/src/codata/x/scipy/constants/_codata.py", "f65f9f0ee37f0d491374f1c629019d55"),
    "c22": (D + "/src/casmag/all/2409.03787v1.txt", "cc640485b0d9f0fe202f38989dac6a2b"),
    "reyle": (D + "/src/casmag/all/2104.14972v2.txt", "2611290dc8122d292dcf04cb92dac4a0"),
    "hst": (D + "/src/casmag/all/2512.08533v1.txt", "77b26d62f6204a311f6a39e77ff83bda"),
    "iau": (D + "/src/casmag/all/1510.07674v1.txt", "6bdffaf89a7a45b40be462d8b910098f"),
}
fails = []


def chk(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  -- " + detail if detail else ""))
    if not ok:
        fails.append(label)


def text(k):
    p, m = SRC[k]
    b = open(p, "rb").read()
    chk("md5 %s" % k, hashlib.md5(b).hexdigest() == m, p)
    return b.decode("utf-8", "replace")


def tree_literal(fn, name):
    s = open(T + "/" + fn, encoding="utf-8").read()
    m = re.search(r"^%s\s*=\s*([0-9.eE+-]+)" % re.escape(name), s, re.M)
    return float(m.group(1)), m.group(1)


# ---------------------------------------------------------------- 0. sources
cod = text("codata"); c22 = text("c22"); rey = text("reyle"); hst = text("hst"); iau = text("iau")


def table(year):
    m = re.search(r'txt%d = """(.*?)"""' % year, cod, re.S)
    rows = {}
    for line in m.group(1).splitlines():
        parts = re.split(r"\s{2,}", line.strip())
        if len(parts) >= 3:
            rows[parts[0]] = (parts[1], parts[2])
    return rows


def num(s):
    s = s.replace(" ", "").replace("...", "")
    return float(s) if s not in ("(exact)",) else 0.0


TAB = {y: table(y) for y in (2006, 2010, 2014, 2018, 2022)}

print("\n== 1. tree literals against CODATA (NIST tables) ==")
C_SI, _ = tree_literal("achievable.py", "C_SI")
G_SI, _ = tree_literal("achievable.py", "G_SI")
HBAR, hs = tree_literal("achievable.py", "HBAR")
LP, _ = tree_literal("achievable.py", "L_PLANCK")
chk("c = CODATA exact 299792458", C_SI == 299792458.0 and TAB[2022]["speed of light in vacuum"][1] == "(exact)")
for y in (2018, 2022):
    g, ug = TAB[y]["Newtonian constant of gravitation"]
    chk("G(tree) = CODATA %d G %s(%s)" % (y, g, ug), num(g) == G_SI)
    l, ul = TAB[y]["Planck length"]
    chk("l_P(tree) = CODATA %d l_P %s(%s)" % (y, l, ul), abs(num(l) - LP) < 1e-45)
    chk("CODATA %d: h exact 6.626 070 15e-34; hbar exact" % y,
        TAB[y]["Planck constant"] == ("6.626 070 15 e-34", "(exact)")
        and TAB[y]["reduced Planck constant"][1] == "(exact)")
for y in (2006, 2010, 2014):
    print("   history: G %d = %s(%s);  l_P = %s(%s)" % ((y,) + TAB[y]["Newtonian constant of gravitation"]
                                                      + TAB[y]["Planck length"]))
chk("CODATA 2022 text prints G 6.674 30(15) and 'the 2022 and 2018 recommended values of G are therefore identical'",
    "6.674 30(15)" in c22 and "recommended values of G are therefore" in c22 and "3.9 expansion factor" in c22)
chk("CODATA 2022 text prints hbar 1.054 571 817 ... exact", "1.054 571 817 . . ." in c22)

h = sp.Rational(662607015, 10**42)
hbar_exact = h / (2 * sp.pi)
rel_hbar = float((sp.Rational(hs) - hbar_exact) / hbar_exact)
print("   hbar exact = h/2pi = %s" % sp.N(hbar_exact, 20))
chk("tree HBAR 1.054571817e-34 = h/2pi truncated at 10 s.f. (rel %.3e, below 1e-9)" % rel_hbar,
    -1e-9 < rel_hbar < 0)
lp_calc = float(sp.sqrt(sp.Rational(hs) * sp.Rational("6.67430e-11") / sp.Integer(299792458) ** 3))
u_lp = 0.000018e-35 / LP
chk("sqrt(HBAR G/c^3) = %.7e agrees with L_PLANCK to %.2e (< u_r(l_P) %.1e)"
    % (lp_calc, lp_calc / LP - 1, u_lp), abs(lp_calc / LP - 1) < u_lp)
uG = 0.00015e-11 / 6.67430e-11

print("\n== 2. FEWSTER_C, computed at high precision ==")
mu = sp.nsolve(sp.cos(sp.Symbol("m")) * sp.cosh(sp.Symbol("m")) - 1, sp.Symbol("m"), 4.73, prec=40)
Cx = mu ** 4 / (16 * sp.pi ** 2)
FC_tree = 3.169857938310467       # achievable.py selftest pin
print("   mu_1 = %s,  C = %s" % (sp.N(mu, 25), sp.N(Cx, 25)))
chk("C = mu_1^4/(16 pi^2) = 3.16985793831... matches the tree's 3.169857938310467 (rel %.1e)"
    % float(FC_tree / Cx - 1), abs(float(FC_tree / Cx) - 1) < 1e-14)

print("\n== 3. D7 figure S1 (K1 route) and its constant sensitivity ==")
M_OVER_B, A_OVER_B = 5.0e-3, 0.02
S_closed = lambda b, m, a, G=G_SI, hb=HBAR: 3 * m * b * b * C_SI ** 3 / (4 * math.pi * float(Cx) * a ** 3 * hb * G)
S1 = S_closed(1.0, M_OVER_B, A_OVER_B)
chk("S1 = %.6e reproduces specthm figures() 1.8019047628764e71" % S1, abs(S1 / 1.8019047628764015e71 - 1) < 1e-12)
dlog = max(abs(math.log10(S_closed(1.0, M_OVER_B, A_OVER_B, G=G_SI * f) / S1)) for f in (1 - 3.9 * uG, 1 + 3.9 * uG))
dlog_hist = max(abs(math.log10(S_closed(1.0, M_OVER_B, A_OVER_B, G=num(TAB[y]["Newtonian constant of gravitation"][0])) / S1))
                for y in (2006, 2010, 2014))
chk("log10 S1 = %.4f; G at +-3.9 sigma moves it %.2e orders, every CODATA G since 2006 %.2e orders -- the 71-order refusal cannot move"
    % (math.log10(S1), dlog, dlog_hist), dlog < 1e-3 and math.log10(S1) > 70)
k = M_OVER_B / ((4 / 3) * math.pi * A_OVER_B ** 3)
bx = math.sqrt(float(Cx) * HBAR * G_SI / (k * C_SI ** 3))
chk("b_x/l_P = %.8f reproduces specthm 0.14575524841714768; G-sensitivity of the ratio via the literal l_P: %.2e"
    % (bx / LP, 0.5 * uG), abs(bx / LP / 0.14575524841714768 - 1) < 1e-12)

print("\n== 4. Proxima (Gaia EDR3 = DR3) and the printed light time ==")
plx = float(re.search(r"Trigonometric parallax (\d+\.\d+)", rey).group(1))
eplx = float(re.search(r"Parallax uncertainty (\d+\.\d+)", rey).group(1))
chk("Reyle+2021 Table 1 prints EPOCH 2016.0 and parallax %.12f +- %.9f mas" % (plx, eplx),
    "Epoch for position 2016.0" in rey and plx == 768.066539187357)
chk("HST 2025 prints 768.373 and the DR3 768.067 +-0.050 beside it", "768.373" in hst and "768.067" in hst)
LY = 299792458 * 365.25 * 86400
PC = 648000 / math.pi * 1.495978707e11
d_ly = 1000.0 / plx * PC / LY
lo, hi = 1000 / (plx + eplx) * PC / LY, 1000 / (plx - eplx) * PC / LY
PROX, _ = tree_literal("foliation.py", "PROXIMA_LY")
chk("1/parallax = %.7f ly (J2016.0), rounds to the tree's 4.2465" % d_ly, round(d_ly, 4) == PROX)
print("   formal 1-sigma interval %.5f .. %.5f ly" % (lo, hi))
p = lambda x: "%.4g" % x
print("   specthm prints '%%.4g years at Proxima' -> tree 4.2465 prints %s; J2016 exact %s; 1-sigma ends %s / %s"
      % (p(PROX), p(d_ly), p(lo), p(hi)))
t_now = 2026 + (268.0 / 365.25)                # 2026-09-26
vr = -22.345e3
d_now = (d_ly * LY + vr * (t_now - 2016.0) * 365.25 * 86400) / LY
print("   radial approach (RV -22.345 km/s, Reyle Table 1 via Barnes+2014): d(2026.74) = %.5f ly -> prints %s"
      % (d_now, p(d_now)))
chk("the printed 4th figure is NOT fixed by the datum: 1-sigma interval spans two printed values",
    p(lo) != p(hi))
chk("light time in Julian years = distance in ly identically (ly := c x Julian year)", LY == 9460730472580800)
plx_dr2 = 768.529
print("   DR2 (Kervella+2020) 768.529 mas -> %.5f ly prints %s; HST 768.373 -> %.5f ly prints %s"
      % (1000 / plx_dr2 * PC / LY, p(1000 / plx_dr2 * PC / LY), 1000 / 768.373 * PC / LY, p(1000 / 768.373 * PC / LY)))
worst = max(abs(x / PROX - 1) for x in (d_now, lo, hi, 1000 / plx_dr2 * PC / LY, 1000 / 768.373 * PC / LY))
chk("every read or computed alternative moves the light time by <= %.1e relative (conclusion 'a setup of ~4.25 yr' intact)"
    % worst, worst < 1e-3)

print("\n== 5. exchange rate c^2/(G Lambda) ==")
LAM, _ = tree_literal("overturn.py", "LAMBDA")
ex = C_SI ** 2 / (G_SI * LAM)
chk("exchange = %.9e reproduces 1.348948e26 (ledger comment) and specthm's 1.3489476444317511e26" % ex,
    abs(ex / 1.3489476444317511e26 - 1) < 1e-14)
prints = sorted({"%.6g" % (C_SI ** 2 / (G_SI * f * LAM)) for f in (1 - uG, 1, 1 + uG)})
chk("specthm prints it '%%.6g' -> %s at G -1s/0/+1s: the 6th printed figure is not fixed by G" % prints, len(prints) == 3)

print("\n== 6. S-1 focal length (spec.py constants) ==")
GMN = 1.3271244e20
RN = float(re.search(r"= (6\.957) ×", iau.replace("\n", " ").replace("× 10 8", "× 10")).group(1)) * 1e8 \
    if re.search(r"= 6\.957 ×", iau.replace("\n", " ")) else 6.957e8
chk("IAU 2015 B3 text prints R_sun^N = 6.957e8 m", "6.957 × 10" in iau and RN == 6.957e8)
chk("spec.LENSES Sun row is ('Sun', 1.989e30, 6.957e8): radius = IAU nominal R_sun^N",
    '("Sun", 1.989e30, 6.957e8)' in open(T + "/spec.py", encoding="utf-8").read())
chk("spec.C_SI, spec.G_SI equal achievable's", tree_literal("spec.py", "C_SI")[0] == C_SI
    and tree_literal("spec.py", "G_SI")[0] == G_SI)
chk("double rounding: tree 4.2465 prints 4.247 but the datum 4.24646 prints 4.246 at the same '%.4g'",
    p(PROX) == "4.247" and p(d_ly) == "4.246")
Msun_tree = 1.989e30
AU_tree, _ = tree_literal("spec.py", "AU")
LYs, _ = tree_literal("spec.py", "LIGHT_YEAR")
f_tree = RN ** 2 * C_SI ** 2 / (4 * G_SI * Msun_tree)
f_nom = RN ** 2 * C_SI ** 2 / (4 * GMN)
print("   spec M_sun 1.989e30 vs GM^N/G = %.6e (rel %+.2e, inside u(G)? %s)"
      % (GMN / G_SI, Msun_tree / (GMN / G_SI) - 1, abs(Msun_tree / (GMN / G_SI) - 1) < uG))
chk("f_sun(tree) = %.3f AU reproduces specthm 547.5949; G-free nominal R^2c^2/(4GM^N) = %.3f AU (rel %+.2e)"
    % (f_tree / AU_tree, f_nom / 1.495978707e11, f_tree / AU_tree / (f_nom / 1.495978707e11) - 1),
    abs(f_tree / AU_tree / 547.594928566667 - 1) < 1e-12)
chk("both round to the published '~550 AU' at 2 s.f.", round(f_tree / AU_tree, -1) == 550 == round(f_nom / 1.495978707e11, -1))
print("   spec.AU %.7e vs IAU 2012 exact 1.495978707e11 (rel %+.2e); spec.LIGHT_YEAR 9.4607e15 vs exact (rel %+.2e)"
      % (AU_tree, AU_tree / 1.495978707e11 - 1, LYs / LY - 1))

print("\n%d failure(s)" % len(fails))
sys.exit(1 if fails else 0)
