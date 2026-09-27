#!/usr/bin/env python3
"""DOCKET 67 pass S, 32/35 -- pdg-light-quark-masses.

Re-derives address.py's QUARK_SUM_MEV = 8.990 (2 m_u + m_d, PDG MS-bar 2 GeV)
from PDG's OWN machine-readable releases (RPP 2018-2026), read here at source:
  * mass_width_<YEAR>.mcd/.txt  (Berkeley PDG MC table, FORTRAN layout
    4I8,2(1X,E18.0,1X,E8.0,1X,E8.0),1X,A21), shipped in scikit-hep particle
    0.21.2 / 0.24.0 / 1.0.1 (pypi);
  * pdg.sqlite, PDG's official API database, editions 2024 / 2025 / 2026,
    shipped in pypi 'pdg' 0.1.4 / 0.2.3 / 2026.0 -- including PDG's header
    text stating the scheme and scale.
Then computes every downstream number address.py rests on it, with the old
and the current datum, and checks whether the conclusion moves.
Read-only: imports nothing from research/; writes nothing.
"""
import glob, os, sqlite3, sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src", "pdgq")
SITE = "/usr/local/lib/python3.11/dist-packages/particle/data"
FAIL = []

def chk(name, got, want, tol=None):
    ok = (got == want) if tol is None else abs(got - want) <= tol * max(1, abs(want))
    print(("PASS " if ok else "FAIL ") + name + f": got {got!r} want {want!r}")
    if not ok:
        FAIL.append(name)

def parse_mc(path):
    """Return {mcid: (mass_GeV, +err, -err, name)} by PDG's stated columns."""
    out = {}
    for line in open(path, encoding="latin-1"):
        if line.startswith("*") or not line.strip():
            continue
        ids = [line[i:i+8].strip() for i in (0, 8, 16, 24)]
        m = line[33:51].strip()
        if not m:
            continue
        ep, en = line[52:60].strip(), line[61:69].strip()
        name = line[107:128].split()[0] if line[107:128].strip() else ""
        for i in ids:
            if i:
                out[int(i)] = (float(m), float(ep or 0), float(en or 0), name)
    return out

def edition_file(y):
    for cand in [os.path.join(SITE, f"mass_width_{y}.txt")] + sorted(
            glob.glob(os.path.join(SRC, "x", "*", "particle", "data", f"mass_width_{y}.*"))):
        if os.path.exists(cand):
            return cand
    return None

M_P = 938.27208816           # CODATA 2018, the tree's value (address.py:425)
M_P_2022 = 938.27208943      # CODATA 2022 (sibling audit codata-proton-mass, READ via scipy)
TREE_SUM = F("8.990")

print("== A. 2 m_u + m_d by RPP edition, from PDG's MC table (MeV)")
table = {}
for y in range(2018, 2027):
    f = edition_file(y)
    if not f:
        print(f"  {y}: no file"); continue
    d = parse_mc(f)
    mu, mup, mun, nu = d[2]; md, mdp, mdn, nd = d[1]
    assert nu == "u" and nd == "d", (nu, nd)
    s = 2 * F(repr(mu * 1000)).limit_denominator(10**6) + F(repr(md * 1000)).limit_denominator(10**6)
    s = F(round(2 * mu * 1e5) + round(md * 1e5), 100)   # exact to 0.01 MeV
    up = 2 * mup * 1e3 + mdp * 1e3; dn = abs(2 * mun * 1e3) + abs(mdn * 1e3)
    table[y] = (mu * 1e3, md * 1e3, s)
    print(f"  RPP {y}: m_u={mu*1e3:.3f} m_d={md*1e3:.3f}  2m_u+m_d={float(s):.3f} "
          f"(+{up:.2f}/-{dn:.2f} linear, file-rounded errors)  {os.path.basename(f)}")
match = [y for y, v in table.items() if v[2] == TREE_SUM]
print("  editions reproducing the tree's 8.990 exactly:", match)
chk("A1 8.990 = 2(2.16)+4.67 is RPP 2019-2023", match, [2019, 2020, 2021, 2022, 2023])
chk("A2 RPP 2024-2026 give 9.02", [float(table[y][2]) for y in (2024, 2025, 2026)], [9.02, 9.02, 9.02])
chk("A3 RPP 2018 gave 9.10 (2.2, 4.7)", float(table[2018][2]), 9.10)

print("\n== B. PDG API database (editions 2024/2025/2026): values and the scheme text")
dbs = {"2024": os.path.join(SRC, "db0.1.4", "pdg", "pdg.sqlite"),
       "2025": os.path.join(SRC, "db0.2.3", "pdg", "pdg.sqlite"),
       "2026": os.path.join(SRC, "db26", "pdg", "pdg.sqlite")}
cur = {}
for ed, p in dbs.items():
    c = sqlite3.connect(p)
    got = {}
    for pid in ("Q002M", "Q001M", "Q123MR4", "Q123MR0"):
        r = c.execute("select value,error_positive,error_negative from pdgdata "
                      "where pdgid=? and value_type='V'", (pid,)).fetchone()
        got[pid] = r
    cur[ed] = got
    print(f"  {ed}: m_u={got['Q002M']}  m_d={got['Q001M']}  mbar={got['Q123MR4']}  m_u/m_d={got['Q123MR0']}")
    if ed == "2026":
        txt = c.execute("select text from pdgtext where pdgid='Q123UM'").fetchone()[0]
        chk("B1 PDG 2026 text states MSbar", "mass- independent subtraction scheme such as MSbar" in txt, True)
        chk("B2 PDG 2026 text states mu = 2 GeV",
            "We have normalized the MSbar masses at a renormalization scale of mu = 2 GeV" in txt, True)
        chk("B3 PDG 2026 text: 'current-quark masses'", "current-quark masses" in txt, True)
        chk("B4 PDG 2026 text: 1 GeV results rescaled by dividing by 1.35", "dividing by 1.35" in txt, True)
        txt_d = c.execute("select text from pdgtext where pdgid='Q001M'").fetchone()[0]
        chk("B5 PDG 2026 caveat: u 'could be essentially massless' kept in text",
            "u quark could be essentially massless" in txt_d, True)

mu26, md26 = cur["2026"]["Q002M"], cur["2026"]["Q001M"]
S_cur = 2 * mu26[0] + md26[0]
sig_unc = ((2 * mu26[1]) ** 2 + md26[1] ** 2) ** 0.5
sig_lin = 2 * mu26[1] + md26[1]
print(f"  2026: 2m_u+m_d = {S_cur:.3f} +- {sig_unc:.3f} (uncorrelated) / +- {sig_lin:.2f} (linear)")
chk("B6 current sum 9.02", round(S_cur, 3), 9.02)
chk("B7 tree's 8.990 lies within current 1 sigma (uncorrelated)", abs(S_cur - 8.990) < sig_unc, True)
print(f"     tree - current = {8.990 - S_cur:+.3f} MeV = {(8.990 - S_cur)/sig_unc:+.2f} sigma")
# PDG-internal consistency: the same sum via mbar and the ratio r = m_u/m_d
mbar, r = cur["2026"]["Q123MR4"][0], cur["2026"]["Q123MR0"][0]
alt = 2 * mbar * (2 * r + 1) / (1 + r)
print(f"  via mbar & r: 2m_u+m_d = 2 mbar (2r+1)/(1+r) = {alt:.3f} MeV; "
      f"(m_u+m_d)/2 from the summary m_u, m_d = {(mu26[0]+md26[0])/2:.3f} vs mbar {mbar}")
chk("B8 DISCREPANCY (PDG-internal, not a refutation): summary m_u+m_d)/2 = 3.43 vs mbar 3.49",
    round((mu26[0] + md26[0]) / 2, 2), 3.43)

print("\n== C. What rests on it (address.py S_SCAN[0], NAIVE_CORRECTION_FACTOR, K_mu)")
b = F(2, 9)   # d ln Lambda / d ln v (address.py derives it; re-derived here)
# re-derive 2/9: Lambda_3 = Lambda_6^(7/9) (m_c m_b m_t)^(2/27) -> 3*2/27
b0 = lambda nf: F(11) - F(2, 3) * nf
# matching Lambda_{nf-1} = Lambda_nf^(b0(nf)/b0(nf-1)) m^(1 - b0(nf)/b0(nf-1))
expo = {}
lam = F(1); acc = {"L6": F(1)}
e_L, e_m = F(1), []
for nf in (6, 5, 4):
    k = b0(nf) / b0(nf - 1)
    e_m = [x * k for x in e_m] + [1 - k]
    e_L *= k
chk("C0 Lambda_3 exponents: Lambda_6^(7/9), each heavy mass^(2/27)", (e_L, e_m), (F(7, 9), [F(2, 27)] * 3))
chk("C0' d ln Lambda/d ln v = 2/9", sum(e_m), b)

def factor(S):  # higgs_fraction(S,'H1')/S = (2/9 + 7S/9)/S
    return (b + (1 - b) * S) / S
def K(S, h):
    return (b * (1 - S) + S - 1) if h == "H1" else (S - 1)

rows = [("tree 8.990 / CODATA2018", F("8.990") / F("938.27208816")),
        ("RPP2024-26 9.02 / CODATA2018", F("9.02") / F("938.27208816")),
        ("RPP2024-26 9.02 / CODATA2022", F("9.02") / F("938.27208943")),
        ("RPP2026 low 1s (9.02-0.157)", F(repr(S_cur - sig_unc)) / F("938.27208943")),
        ("RPP2026 high 1s (9.02+0.157)", F(repr(S_cur + sig_unc)) / F("938.27208943")),
        ("RPP2022 low (8.99-0.7)", F("8.29") / F("938.27208816")),
        ("RPP2022 high (8.99+1.5)", F("10.49") / F("938.27208816")),
        ("same sum at mu=1 GeV (x1.35, PDG's own factor)", F("8.990") * F("1.35") / F("938.27208816"))]
print(f"  {'input':46s} {'S':>9s} {'S %':>7s} {'factor':>8s} {'K_mu H1':>9s} {'K_mu H2':>9s}")
res = {}
for lab, S in rows:
    res[lab] = (float(S), float(factor(S)), float(K(S, 'H1')), float(K(S, 'H2')))
    print(f"  {lab:46s} {float(S):9.6f} {100*float(S):7.3f} {float(factor(S)):8.4f} "
          f"{float(K(S,'H1')):9.4f} {float(K(S,'H2')):9.4f}")
t = res["tree 8.990 / CODATA2018"]; n = res["RPP2024-26 9.02 / CODATA2018"]
chk("C1 tree's F6 pin 23.9708 reproduced at 8.990", round(t[1], 4), 23.9708)
chk("C2 at the current 9.02 the F6 factor is 23.894 (pin would move 0.32%)", round(n[1], 3), 23.894)
chk("C3 the tree's selftest tolerance 1e-5 would REJECT 9.02 (edition-specific pin)",
    abs(n[1] - 23.9708) / 23.9708 > 1e-5, True)
chk("C4 the looser pin (address.py:1324, 23.9 +- 2e-2) passes at 9.02", abs(n[1] - 23.9) / 23.9 <= 2e-2, True)
chk("C5 printed '0.96%' holds for both 8.990 and 9.02", (round(100*t[0], 2), round(100*n[0], 2)), (0.96, 0.96))
chk("C6 printed K_mu(H1) -0.7703 / K_mu(H2) -0.9904 unchanged at 4 dp",
    (round(t[2], 4), round(n[2], 4), round(t[3], 4), round(n[3], 4)), (-0.7703, -0.7703, -0.9904, -0.9904))
allK = [v for lab, v in res.items()]
chk("C7 K_mu O(1) and negative over every input incl. PDG ranges and mu=1 GeV",
    all(-1 < v[2] < -0.7 and -1 < v[3] < -0.9 for v in allK), True)
f1 = res["same sum at mu=1 GeV (x1.35, PDG's own factor)"]
print(f"  SCALE: the 'naive' S is RG-scale dependent: 0.96% at 2 GeV -> {100*f1[0]:.2f}% at 1 GeV; "
      f"factor 24.0 -> {f1[1]:.1f}")
chk("C8 factor at mu=1 GeV normalisation is ~18 (so '24' is a 2-GeV-convention number)", round(f1[1], 1), 18.0)

# PDG's own caveat (B5): "the u quark could be essentially massless".  Test it.
S0 = F("4.70") / F("938.27208943")
print(f"  m_u = 0 caveat: S = {float(S0):.6f}, factor = {float(factor(S0)):.2f}, "
      f"K_mu H1 = {float(K(S0,'H1')):.4f}, H2 = {float(K(S0,'H2')):.4f}")
chk("C9 even at PDG's m_u = 0 caveat K_mu stays O(1) negative", -1 < float(K(S0,'H1')) < -0.7, True)
c = sqlite3.connect(dbs["2026"])
bz = c.execute("select v.value,v.error_positive from pdgmeasurement m join pdgreference r on r.id=m.pdgreference_id "
               "join pdgmeasurement_values v on v.pdgmeasurement_id=m.id where m.pdgid='Q123UM' and r.document_id like 'BAZAVOV 2018%'").fetchone()
print(f"  BAZAVOV 2018 (in PDG 2026 average): m_u = {bz[0]} +- {bz[1]} MeV -> m_u = 0 excluded at {bz[0]/bz[1]:.0f} sigma (that one input)")
chk("C10 m_u = 0 excluded by a lattice input PDG averages (>50 sigma)", bz[0] / bz[1] > 50, True)

print("\nRESULT:", "ALL PASS" if not FAIL else f"{len(FAIL)} FAIL: {FAIL}")
sys.exit(1 if FAIL else 0)
