#!/usr/bin/env python3
"""DOCKET 67 audit re-derivation: pdg-2026-capture.

Reads (never writes) research/warp-drive/captures/PDG-2026.tsv and compares it
against (a) PDG's own machine-readable mass_width_{2024,2025,2026}.txt shipped
in scikit-hep `particle` 1.0.1, parsed here by the FORTRAN column layout the
file's own header states (independent of pdgcapture.py and of `particle`'s
Python loader); (b) CODATA 2018 and 2022 as tabulated in scipy 1.17.1's
_codata.py (NIST ASCII tables).  Then recomputes every derived figure the tree
uses and the sensitivity of the W-mass-dependent quantities to the contested
W mass.  Exit 0 on all checks passing; prints every number.
"""
import csv, math, os, re, sys, hashlib
import particle

TREE = "/home/user/Claude-Method-Works/research/warp-drive"
CAP = os.path.join(TREE, "captures", "PDG-2026.tsv")
D = os.path.join(os.path.dirname(particle.__file__), "data")
SCIPY = ("/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-"
         "527dc14c2847/scratchpad/d67/src/codata/x/scipy/constants/_codata.py")
fails = []
def chk(label, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
    if not ok: fails.append(label)

IDS = {"e": 11, "mu": 13, "tau": 15, "d": 1, "u": 2, "s": 3, "c": 4, "b": 5,
       "t": 6, "p": 2212, "n": 2112, "W": 24, "Z": 23, "H": 25}

def md5(p): return hashlib.md5(open(p, "rb").read()).hexdigest()

def parse_mw(year):
    out = {}
    for line in open(os.path.join(D, "mass_width_%d.txt" % year)):
        if line.startswith("*") or not line.strip(): continue
        ids = [line[i:i+8].strip() for i in (0, 8, 16, 24)]
        m, ep, em = line[33:51].strip(), line[52:60].strip(), line[61:69].strip()
        if not m: continue
        ep = ep or "0"; em = em or "0"
        for i in ids:
            if i: out[int(i)] = (float(m) * 1000.0, float(ep) * 1000.0, float(em) * 1000.0)
    return out  # MeV

def parse_capture():
    rows = [r for r in csv.DictReader(
        (l for l in open(CAP) if not l.startswith("#")), delimiter="\t")]
    return rows

def codata(block, name):
    txt = open(SCIPY).read()
    start = txt.index("txt%s = \"\"\"" % block)
    body = txt[start:txt.index('"""', start + 20)]
    for line in body.splitlines():
        if line.startswith(name + " "):
            f = re.split(r"\s{2,}", line.strip())
            return float(f[1].replace(" ", "")), float(f[2].replace(" ", ""))
    raise KeyError(name)

print("== provenance")
chk("mass_width_2026.txt md5 = capture header e96a23be...",
    md5(os.path.join(D, "mass_width_2026.txt")) == "e96a23be061430adc72d5b2ea5a93764")
chk("particle2026.csv md5 = capture header b6f460a1...",
    md5(os.path.join(D, "particle2026.csv")) == "b6f460a16e4cd93a5cc721f3aee1d6c2")

mw = {y: parse_mw(y) for y in (2024, 2025, 2026)}
cap = parse_capture()
bypid = {int(r["pdgid"]): r for r in cap}

print("\n== capture vs PDG 2026 file (independent FORTRAN-column parse)")
print("%-4s %-18s %-20s %-10s %-9s %-14s %-14s" % (
    "q", "capture MeV", "PDG2026 MeV", "+-err", "gap/sig", "PDG2025", "PDG2024"))
for k, pid in IDS.items():
    capm = float(bypid[pid]["mass_MeV"])
    m26, e26, _ = mw[2026][pid]
    gap = abs(capm - m26)
    ns = gap / e26 if e26 else float("inf")
    print("%-4s %-18r %-20r %-10.3g %-9.3f %-14r %-14r" % (
        k, capm, m26, e26, ns, mw[2025][pid][0], mw[2024][pid][0]))
    chk("%s: capture = PDG2026 to 9 significant figures (pdgcapture.py:137 '%%.9g')" % k,
        float("%.9g" % m26) == capm)
    chk("%s: 9-s.f. rounding gap <= 2 sigma of PDG's stated error" % k,
        e26 == 0 or ns <= 2.0, "gap %.3g MeV = %.2f sigma" % (gap, ns))

print("\n== CODATA cross-check (scipy _codata.py tables)")
moves = {}
for k, nm in (("e", "electron mass energy equivalent in MeV"),
              ("p", "proton mass energy equivalent in MeV"),
              ("n", "neutron mass energy equivalent in MeV")):
    v22, u22 = codata("2022", nm); v18, u18 = codata("2018", nm)
    print("  %s CODATA2018 %.11f(%g)  CODATA2022 %.11f(%g)  PDG2026 %.11f  PDG2024 %.11f" % (
        k, v18, u18, v22, u22, mw[2026][IDS[k]][0], mw[2024][IDS[k]][0]))
    chk("%s: PDG2026 = CODATA 2022" % k, abs(mw[2026][IDS[k]][0] - v22) < 1e-9 * v22)
    chk("%s: PDG2024 = CODATA 2018" % k, abs(mw[2024][IDS[k]][0] - v18) < 1e-9 * v18)
    # RECORDED, not a check of the tree: the datum moved between editions.
    print("  RECORD %s: CODATA 2018->2022 move %+.3g MeV = %.2f sigma(2018), %.2g relative" % (
        k, v22 - v18, abs(v22 - v18) / u18, (v22 - v18) / v18))
    moves[k] = (v18, v22)

r18 = moves["e"][0] / moves["p"][0]; r22 = moves["e"][1] / moves["p"][1]
chk("m_e/m_p fixture 5.446170e-4 (1e-6 rel) holds under CODATA 2018 AND 2022",
    abs(r18 / 5.446170e-4 - 1) < 1e-6 and abs(r22 / 5.446170e-4 - 1) < 1e-6, "%.10e / %.10e" % (r18, r22))
mN18 = (moves["p"][0] + moves["n"][0]) / 2; mN22 = (moves["p"][1] + moves["n"][1]) / 2
print("  m_N CODATA2018 %.9f  CODATA2022 %.9f  (move %.2g MeV; tree fixture tolerance 1e-12 rel = %.2g MeV)" % (
    mN18, mN22, mN22 - mN18, 938.9187555e-12))

print("\n== derived figures as the tree states them")
me, mp, mn = (float(bypid[i]["mass_MeV"]) for i in (11, 2212, 2112))
mN = (mp + mn) / 2
mN_full = (mw[2026][2212][0] + mw[2026][2112][0]) / 2
chk("m_N from capture = 938.9187555 (massform.py:4850)", abs(mN - 938.9187555) < 1e-9, repr(mN))
print("  m_N from unrounded PDG2026: %.9f  (diff %.2g MeV)" % (mN_full, mN_full - mN))
chk("m_e/m_p = 5.446170e-4 to 1e-6 rel (massform.py:4848)",
    abs(me / mp / 5.446170e-4 - 1) < 1e-6, "%.9e" % (me / mp))
GF, uGF = codata("2022", "Fermi coupling constant")
v = (math.sqrt(2) * GF) ** -0.5
print("  v = (sqrt2 G_F)^-1/2 = %.5f GeV (G_F CODATA2022 %.7e)" % (v, GF))
chk("v agrees with higgs fixture 246.2196 to 1e-5", abs(v / 246.2196 - 1) < 1e-5)
yt = math.sqrt(2) * 172.6 / v; ye = math.sqrt(2) * me / 1000 / v
chk("y_t = 0.9914 (massform.py:217)", round(yt, 4) == 0.9914, "%.6f" % yt)
chk("y_e = 2.935e-6 (massform.py:217)", round(ye * 1e6, 3) == 2.935, "%.5e" % ye)
for lab, mt in (("PDG2024 172.57", 172.57), ("PDG2025 172.56", 172.56),
                ("PDG2026 172.60", 172.60), ("MSbar m_t(m_t)~162.5 NAMED-NOT-READ", 162.5)):
    print("  y_t with m_t = %-36s -> %.4f" % (lab, math.sqrt(2) * mt / v))

baryons = sorted((float(r["mass_MeV"]), r["name"]) for r in cap
                 if r["family"] == "baryon" and r["mass_MeV"] != "?")
chk("lightest baryon in capture is p", baryons[0][1] == "p", str(baryons[:2]))
cl = [r["name"] for r in cap if r["family"] == "lepton" and r["Q3"] == "-3"]
chk("charged leptons (Q3=-3) in capture = e-, mu-, tau- -> N_F = 3", sorted(cl) == ["e-", "mu-", "tau-"], str(cl))
st4 = [r for r in csv.reader(l for l in open(os.path.join(D, "particle2026.csv")) if not l.startswith("#"))
       if r and r[0] in ("17", "-17", "18", "-18")]
chk("tau'/nu(tau') carry status 4 in particle2026.csv (col 15)", all(r[14] == "4" for r in st4) and len(st4) == 4,
    str([(r[0], r[14], r[15]) for r in st4]))
chk("tau' has no mass in particle2026.csv (never measured)", all(r[1] == "-1" for r in st4))

print("\n== W-mass sensitivity (alpha_W = g^2/4pi, g = 2 m_W/v; E_sph ~ 2 m_W/alpha_W x B)")
def aw(mW): g = 2 * mW / v; return g * g / (4 * math.pi)
ref = 80.362
rows = [("capture/PDG2026", 80.362), ("PDG2024/2025 file", 80.369),
        ("CMS 2024 80360.2+-9.9 (NAMED-NOT-READ)", 80.3602),
        ("CDF 2022 80433.5+-9.4 (NAMED-NOT-READ)", 80.4335)]
a0 = aw(ref); L0 = -(4 * math.pi / a0) / math.log(10); E0 = 2 * ref / a0
for lab, m in rows:
    a = aw(m); L = -(4 * math.pi / a) / math.log(10); E = 2 * m / a
    print("  %-40s alpha_W %.6f  log10 exp(-4pi/aW) %.3f (d %.3f)  E_sph/E_sph(capture) %.5f" % (
        lab, a, L, L - L0, E / E0))
aC = aw(80.4335); LC = -(4 * math.pi / aC) / math.log(10)
chk("CDF value shifts the instanton log10 suppression by < 1 unit (of ~-160)", abs(LC - L0) < 1.0,
    "%.3f vs %.3f" % (LC, L0))
chk("CDF value shifts E_sph by < 0.2%", abs(2 * 80.4335 / aC / E0 - 1) < 2e-3)

print("\n== quark-mass scheme note (as the capture carries it)")
for k in ("u", "d", "s", "c", "b", "t"):
    m, e, _ = mw[2026][IDS[k]]
    print("  %s %.6g +- %.2g MeV  (2024: %.6g)" % (k, m, e, mw[2024][IDS[k]][0]))
chk("m_u > 0 at > 20 sigma in PDG2026 (consideration needs m>0 only)",
    mw[2026][2][0] / mw[2026][2][1] > 20, "%.1f sigma" % (mw[2026][2][0] / mw[2026][2][1]))

print("\nRESULT: %d failure(s)" % len(fails))
for f in fails: print("  FAIL", f)
sys.exit(1 if fails else 0)
