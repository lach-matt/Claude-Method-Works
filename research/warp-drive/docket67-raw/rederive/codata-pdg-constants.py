#!/usr/bin/env python3
"""DOCKET 67 -- audit of 'codata-pdg-constants' (address.py:424-429).

READ-ONLY with respect to the tree: imports research/warp-drive/higgs.py for
m_h only (bytecode writing disabled), never writes there.

Checks, in order:
  A. the NIST CODATA tables (2006/2010/2014/2018/2022) as embedded in scipy
     1.17.1 _codata.py (md5 asserted) -- the tree's five literals are CODATA
     2018 EXACTLY; the 2022 values and the historical r_p series are printed.
  B. the PDG RPP mass tables (particle 1.0.1 wheel: mass_width_2024/2025/2026,
     md5 asserted) -- m_e, m_p in PDG 2024/2025 = CODATA 2018; PDG 2026 =
     CODATA 2022.
  C. internal consistency: a_0 = hbar/(alpha m_e c), m_e c^2/e in MeV, from
     the same table's own m_e (kg) and alpha, for 2018 and 2022.
  D. sympy: an independent derivation of K = d ln[nu(1S-2S)/nu(2P-3D)]/d ln x
     from CODATA 2022 eq. (50) (READ, p.15), with and without its (m_r/m_e)^3
     factor, against the tree's closed form 28x^2/(14x^2-9).
  E. every rests_on_it number recomputed under every vintage and under the
     contested scattering radii; the tree's own pins re-tested.
  F. sympy: d ln alpha(0)/d ln m = -alpha(0) d(alpha^-1)/d ln m, so the
     one-loop K_alpha takes the LOW-ENERGY alpha as its input exactly.
"""
import hashlib, math, os, re, sys, zipfile
sys.dont_write_bytecode = True
import sympy as sp

D67 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67"
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
CODATA_PY = "/usr/local/lib/python3.11/dist-packages/scipy/constants/_codata.py"
CODATA_MD5 = "f65f9f0ee37f0d491374f1c629019d55"
WHEEL = D67 + "/pkg/particle-1.0.1-py3-none-any.whl"
PAPER = D67 + "/src/casmag/all/2409.03787v1.txt"
PAPER_MD5 = "cc640485b0d9f0fe202f38989dac6a2b"

FAIL = []
def chk(label, cond):
    print("  [%s] %s" % ("ok" if cond else "FAIL", label))
    if not cond:
        FAIL.append(label)

def md5(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()

# ------------------------------------------------------------------ A. CODATA
print("A. NIST CODATA tables (scipy _codata.py)")
chk("scipy _codata.py md5 = %s" % CODATA_MD5, md5(CODATA_PY) == CODATA_MD5)
src = open(CODATA_PY).read()
blocks = dict(re.findall(r'txt(\d{4})\s*=\s*"""(.*?)"""', src, re.S))
chk("tables 2006 2010 2014 2018 2022 present",
    all(y in blocks for y in ("2006", "2010", "2014", "2018", "2022")))

def val(year, name):
    # fixed-width NIST allascii layout: (name, value, uncertainty) columns
    c1, c2, c3 = (55, 77, 99) if int(year) < 2018 else (60, 85, 110)
    for line in blocks[year].splitlines():
        if line[:c1].rstrip() == name:
            v = float(line[c1:c2].replace(" ", "").replace("...", ""))
            u = line[c2:c3].replace(" ", "")
            u = 0.0 if "exact" in u else float(u)
            return v, u
    raise KeyError((year, name))

NAMES = {"m_e_MeV": "electron mass energy equivalent in MeV",
         "m_p_MeV": "proton mass energy equivalent in MeV",
         "r_p_m": "proton rms charge radius",
         "a0_m": "Bohr radius",
         "inv_alpha": "inverse fine-structure constant",
         "m_e_kg": "electron mass",
         "alpha": "fine-structure constant"}
TABLE = {y: {k: val(y, n) for k, n in NAMES.items()}
         for y in ("2006", "2010", "2014", "2018", "2022")}

TREE_LIT = {"m_e_MeV": 0.51099895000, "m_p_MeV": 938.27208816,
            "r_p_m": 0.8414e-15, "a0_m": 5.29177210903e-11,
            "inv_alpha": 137.035999084}
# the literals are also read from address.py itself, not only typed here
atext = open(TREE + "/address.py").read()
for k, pat in (("m_e_MeV", r"M_E_MEV = ([0-9.e+-]+)"),
               ("m_p_MeV", r"M_P_MEV = ([0-9.e+-]+)"),
               ("r_p_m", r"R_PROTON_M = ([0-9.e+-]+)"),
               ("a0_m", r"A_BOHR_M = ([0-9.e+-]+)"),
               ("inv_alpha", r"ALPHA_EM = 1\.0 / ([0-9.e+-]+)")):
    chk("address.py literal %s = %r" % (k, TREE_LIT[k]),
        float(re.search(pat, atext).group(1)) == TREE_LIT[k])
for k in TREE_LIT:
    v18, u18 = TABLE["2018"][k]
    v22, u22 = TABLE["2022"][k]
    chk("tree %s == CODATA 2018 exactly" % k, v18 == TREE_LIT[k])
    rel = v22 / v18 - 1.0
    print("      2018 %.12g (%.2g)   2022 %.12g (%.2g)   rel %+.3e   = %+.2f u2018"
          % (v18, u18, v22, u22, rel, (v22 - v18) / u18))
print("   r_p across CODATA vintages (fm):")
for y in ("2006", "2010", "2014", "2018", "2022"):
    v, u = TABLE[y]["r_p_m"]
    print("      %s  %.5f(%.5f)" % (y, v * 1e15, u * 1e15))
v14, u14 = TABLE["2014"]["r_p_m"]; v18, u18 = TABLE["2018"]["r_p_m"]
sep = (v14 - v18) / math.hypot(u14, u18)
print("   2014 -> 2018 move: %+.3f%%, %.2f combined sigma" % ((v18 / v14 - 1) * 100, sep))
chk("2014->2018 r_p move exceeds 5 combined sigma (the proton-radius puzzle)", sep > 5)

# CODATA 2022 paper text (arXiv:2409.03787v1, saved page text)
if os.path.exists(PAPER):
    chk("2409.03787v1 page-text md5", md5(PAPER) == PAPER_MD5)
    ptxt = re.sub(r"\s+", " ", open(PAPER).read())
    chk("paper prints r_p 8.4075(64) x 10^-16 m", "8.4075(64)" in ptxt)
    chk("paper prints 1/alpha 137.035 999 177(21)", "137.035 999 177(21)" in ptxt)
    chk("paper prints m_e c^2 0.510 998 950 69(16) MeV", "0.510 998 950 69(16)" in ptxt)
    chk("paper prints m_p c^2 938.272 089 43(29) MeV", "938.272 089 43(29)" in ptxt)
    chk("paper: scattering r_p 'should not be included in the 2022 adjustment'",
        "should not be in- cluded in the 2022 adjustment" in ptxt
        or "should not be included in the 2022 adjustment" in ptxt)
    chk("paper Table XXXVIII row '13 r p -0.4 2.91'", "13 r p  −0.4 2.91" in ptxt
        or "13 r p −0.4 2.91" in ptxt)
else:
    print("   (paper text absent -- section skipped)")

# ------------------------------------------------------------------ B. PDG
print("B. PDG RPP mass tables (particle 1.0.1 wheel)")
PDG_MD5 = {"2024": "c98c429456c398279b8ce8fcdffcbdcf",
           "2025": "76ac6db60e0d654b64d64b9e7857ad91",
           "2026": "e96a23be061430adc72d5b2ea5a93764"}
PDG = {}
with zipfile.ZipFile(WHEEL) as z:
    for y, m in PDG_MD5.items():
        raw = z.read("particle/data/mass_width_%s.txt" % y)
        chk("mass_width_%s.txt md5" % y, hashlib.md5(raw).hexdigest() == m)
        rows = {}
        for line in raw.decode().splitlines():
            if line.startswith("*"):
                continue
            f = line.split()
            if f and f[0] in ("11", "2212"):
                rows[f[0]] = float(f[1]) * 1e3          # GeV -> MeV
        PDG[y] = rows
for y in ("2024", "2025"):
    chk("PDG %s m_e = tree = CODATA 2018" % y, abs(PDG[y]["11"] - TREE_LIT["m_e_MeV"]) < 1e-14)
    chk("PDG %s m_p = tree = CODATA 2018" % y, abs(PDG[y]["2212"] - TREE_LIT["m_p_MeV"]) < 1e-9)
chk("PDG 2026 m_e = CODATA 2022", abs(PDG["2026"]["11"] - TABLE["2022"]["m_e_MeV"][0]) < 1e-14)
chk("PDG 2026 m_p = CODATA 2022", abs(PDG["2026"]["2212"] - TABLE["2022"]["m_p_MeV"][0]) < 1e-9)

# ------------------------------------------------------------------ C. consistency
print("C. internal consistency of each table")
HBAR = 6.62607015e-34 / (2 * math.pi); C = 299792458.0; E = 1.602176634e-19
for y in ("2018", "2022"):
    t = TABLE[y]
    a0 = HBAR / (t["alpha"][0] * t["m_e_kg"][0] * C)
    mec2 = t["m_e_kg"][0] * C ** 2 / E / 1e6
    chk("%s a_0 = hbar/(alpha m_e c) to 1e-10 (got %+.2e)" % (y, a0 / t["a0_m"][0] - 1),
        abs(a0 / t["a0_m"][0] - 1) < 1e-10)
    chk("%s m_e c^2/e = MeV value to 1e-10 (got %+.2e)" % (y, mec2 / t["m_e_MeV"][0] - 1),
        abs(mec2 / t["m_e_MeV"][0] - 1) < 1e-10)
    chk("%s alpha * inv_alpha = 1 to 1e-10" % y,
        abs(t["alpha"][0] * t["inv_alpha"][0] - 1) < 1e-10)

# ------------------------------------------------------------------ D. sympy
print("D. sympy: finite-size K from CODATA 2022 eq. (50)")
x, rho = sp.symbols("x rho", positive=True)      # rho = m_r/m_e
# eq.(50): E4 = (2/3) m_e c^2 (Z alpha)^4/n^3 (m_r/m_e)^3 (r_N/lambda_C)^2 delta_l0
# with lambda_C = alpha a_0 and E_h = m_e c^2 alpha^2: E4 = (2/3) E_h rho^3 x^2/n^3
# gross levels E_n = -rho E_h/(2 n^2); units of E_h.
def lev(n, l, with_rho):
    r = rho if with_rho else sp.Integer(1)   # sp.Integer, not int: -1/(2n^2) must stay exact
    return -r / (2 * n ** 2) + (sp.Rational(2, 3) * r ** 3 * x ** 2 / n ** 3 if l == 0 else 0)
def K_of(with_rho):
    nu1 = lev(2, 0, with_rho) - lev(1, 0, with_rho)
    nu2 = lev(3, 2, with_rho) - lev(2, 1, with_rho)
    return sp.simplify(x * sp.diff(sp.log(nu1 / nu2), x))
K_tree_form = 28 * x ** 2 / (14 * x ** 2 - 9)
K0 = K_of(False); K1 = K_of(True)
chk("eq.(50) with m_r = m_e reproduces the tree's 28x^2/(14x^2-9) exactly",
    sp.simplify(K0 - K_tree_form) == 0)
chk("eq.(50) with its (m_r/m_e)^3 factor gives 28 rho^2 x^2/(14 rho^2 x^2 - 9)",
    sp.simplify(K1 - 28 * rho ** 2 * x ** 2 / (14 * rho ** 2 * x ** 2 - 9)) == 0)

# ------------------------------------------------------------------ E. rests_on_it
print("E. rests_on_it under every vintage")
sys.path.insert(0, TREE)
import higgs                                     # read-only: m_h
M_H_GEV = higgs.M_HIGGS
HB = higgs.HBAR; CC = higgs.c; GEV_J = higgs.GEV_IN_J
lam = HB * CC / (M_H_GEV * GEV_J)
print("   m_h (tree, READ) = %.5f GeV, lambda_h = %.6e m" % (M_H_GEV, lam))
Kf = lambda rp, a0, r=1.0: 28 * (r * rp / a0) ** 2 / (14 * (r * rp / a0) ** 2 - 9)

def rests(t, rp=None):
    me, mp, a0, ia = t["m_e_MeV"][0], t["m_p_MeV"][0], t["a0_m"][0], t["inv_alpha"][0]
    rp = t["r_p_m"][0] if rp is None else rp
    ceil = (me / (M_H_GEV * 1e3)) ** 2          # (m c^2/E)^2 at p = m_h c ~ (m/m_h)^2
    mkg = me * 1e6 * E / CC ** 2
    p = HB / lam
    En = math.sqrt((p * CC) ** 2 + (mkg * CC ** 2) ** 2)
    ceil_exact = (mkg * CC ** 2 / En) ** 2
    return {"K_finite": Kf(rp, a0), "K_alpha_H1": 43 / 54 / ia / math.pi,
            "(m_e/m_h)^2": ceil, "probe_ceiling": ceil_exact,
            "eps_probe": 3.0e-16 / ceil_exact, "a0/lambda_h": a0 / lam,
            "lambda_h/r_p": lam / rp, "S_SCAN[0]": 8.990 / mp}
T18 = dict(TABLE["2018"]); T22 = dict(TABLE["2022"])
R18 = rests(T18); R22 = rests(T22)
for k in R18:
    print("      %-14s 2018 %.6e   2022 %.6e   rel %+.3e" % (k, R18[k], R22[k], R22[k] / R18[k] - 1))
MH = M_H_GEV / 125.20
chk("tree pin W10 K_finite -7.8654e-10 @1e-4 holds on CODATA 2018",
    abs(R18["K_finite"] / -7.8654e-10 - 1) < 1e-4)
chk("tree pin K_alpha(H1) 1.849653e-3 @1e-6 holds on CODATA 2018",
    abs(R18["K_alpha_H1"] / 1.849653e-3 - 1) < 1e-6)
print("   pins re-tested on CODATA 2022 (a pin failing is a numeric pin, not a verdict):")
pins = [("K_finite -7.8654e-10 @1e-4", R22["K_finite"], -7.8654e-10, 1e-4),
        ("K_alpha(H1) 1.849653e-3 @1e-6", R22["K_alpha_H1"], 1.849653e-3, 1e-6),
        ("lambda_h/r_p 1.8732e-3 @1e-3", R22["lambda_h/r_p"], 1.8732e-3, 1e-3),
        ("a0/lambda_h 3.3575e7 @1e-3", R22["a0/lambda_h"], 3.3575e7, 1e-3),
        ("probe ceiling 1.665833e-11*MH^-2 @1e-5", R22["probe_ceiling"], 1.665833e-11 * MH ** -2, 1e-5)]
P22 = {}
for lab, got, want, tol in pins:
    r = got / want - 1
    P22[lab] = abs(r) < tol
    print("      %-40s rel %+.3e  %s" % (lab, r, "holds" if abs(r) < tol else "FAILS"))
chk("CODATA 2022 fails exactly two numeric pins, both through r_p: W10 K_finite and lambda_h/r_p",
    sorted(l for l, ok in P22.items() if not ok)
    == sorted(["K_finite -7.8654e-10 @1e-4", "lambda_h/r_p 1.8732e-3 @1e-3"]))
r18 = R18["lambda_h/r_p"] / 1.8732e-3 - 1
print("   (lambda_h/r_p pin already sits at %+.3e on CODATA 2018 through m_h 125.20 -> 125.13;" % r18)
print("    r_p 2022 adds %+.3e and crosses the 1e-3 tolerance)" % (R22["lambda_h/r_p"] / R18["lambda_h/r_p"] - 1))
print("   K_finite under contested / historical r_p (a_0 = 2018):")
a018 = T18["a0_m"][0]
RP = [("CODATA 2006", TABLE["2006"]["r_p_m"][0]), ("CODATA 2010", TABLE["2010"]["r_p_m"][0]),
      ("CODATA 2014", TABLE["2014"]["r_p_m"][0]), ("CODATA 2018", T18["r_p_m"][0]),
      ("CODATA 2022", T22["r_p_m"][0]),
      ("e-p scattering, Mainz A1 0.879 fm (NAMED-NOT-READ)", 0.879e-15),
      ("e-p scattering, PRad 0.831 fm (NAMED-NOT-READ)", 0.831e-15)]
KS = {}
for lab, rp in RP:
    KS[lab] = Kf(rp, a018)
    print("      %-52s r_p %.5f fm  K %.5e  rel %+.3f%%  lam/r_p %.5e"
          % (lab, rp * 1e15, KS[lab], (KS[lab] / R18["K_finite"] - 1) * 100, lam / rp))
chk("K_finite is negative and nonzero for EVERY r_p in the span (W10 verdict invariant)",
    all(k < 0 for k in KS.values()))
span = max(abs(k) for k in KS.values()) / min(abs(k) for k in KS.values())
print("   |K| span over all radii: factor %.4f" % span)
chk("|K| moves by < 12%% over every radius considered (got %.2f%%)" % ((span - 1) * 100), span < 1.12)
chk("atom does not fit in lambda_h for every vintage (a0/lambda_h > 1e7)",
    all(TABLE[y]["a0_m"][0] / lam > 1e7 for y in TABLE))
chk("nor a proton (r_p/lambda_h > 1e2) for every radius",
    all(rp / lam > 1e2 for _, rp in RP))
# reduced-mass factor from eq.(50), which the tree's formula omits
mr = 1 / (1 + T18["m_e_MeV"][0] / T18["m_p_MeV"][0])
Kr = Kf(T18["r_p_m"][0], a018, mr)
print("   eq.(50)'s (m_r/m_e)^3 factor: m_r/m_e = %.9f, K %.6e, rel %+.4e vs tree form"
      % (mr, Kr, Kr / R18["K_finite"] - 1))
chk("the omitted (m_r/m_e) factor moves K by -0.109% (shrinks |K|; exceeds the 1e-4 pin)",
    abs((Kr / R18["K_finite"] - 1) - (mr ** 2 - 1)) < 1e-6 and -1.2e-3 < Kr / R18["K_finite"] - 1 < -1.0e-3)

# ------------------------------------------------------------------ F. alpha(0)
print("F. sympy: the one-loop K_alpha takes alpha(0) exactly")
a, lnm, b = sp.symbols("alpha lnm b", positive=True)
inv = sp.Function("inv")(lnm)                 # alpha^-1(0) as a function of ln m
alpha0 = 1 / inv
lhs = sp.diff(sp.log(alpha0), lnm)
rhs = -alpha0 * sp.diff(inv, lnm)
chk("d ln alpha(0)/d ln m == -alpha(0) d(alpha^-1(0))/d ln m (identity)", sp.simplify(lhs - rhs) == 0)
print("   so with a one-loop threshold d(alpha^-1)/d ln m = -b/(2 pi) (alpha-independent),")
print("   the input alpha in 43 alpha/(54 pi) is alpha(0): the CODATA (Thomson-limit) value.")

print()
print("FAILURES:", FAIL if FAIL else "none")
sys.exit(1 if FAIL else 0)
