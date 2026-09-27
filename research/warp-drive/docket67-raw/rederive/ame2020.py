#!/usr/bin/env python3
"""DOCKET 67 / ame2020 -- re-derive mu_min (least nuclear mass per nucleon among
AME2020's measured nuclides) and the pair-floor ratio 1.9975, independently of
the tree's own reader (gravity.nuclides / massform.mu_min_mev).

Witnesses:
  W1  the tree's capture extracted/archives/restore-point-2-13/captures/
      AME2020-TableI.tsv (Wang et al., CPC 45 030003 (2021), Table I, rounded
      published table; mass excess in keV, quality M/E) -- parsed HERE, not via
      gravity.py.
  W2  an independent copy of AME2020 massround.mas20 (atomic masses in u),
      as shipped in the pypi package periodictable 2.1.0 (periodictable/mass.py,
      docstring: 'From https://www-nds.iaea.org/amdc/ame2020/massround.mas20.txt
      (2023-07-06)').  The AMDC hosts are refused by the egress proxy; pypi is
      not.
Constants:
  CODATA 2018 u = 931.49410242 MeV (the value AME2020 itself uses; the tree's
  gravity.U_KG = 1.66053906660e-27 kg is CODATA 2018); CODATA 2022 u =
  931.49410372 MeV; m_e 2018 = 0.51099895000 MeV, 2022 = 0.51099895069 MeV.
  (Constants typed from memory of CODATA -> status NAMED-NOT-READ here.)
Exit 1 on any failed check.
"""
import os, re, sys, zipfile, glob

ROOT = "/home/user/Claude-Method-Works"
CAP = os.path.join(ROOT, "extracted/archives/restore-point-2-13/captures/AME2020-TableI.tsv")
HERE = os.path.dirname(os.path.abspath(__file__))
WHEEL = glob.glob(os.path.join(HERE, "..", "src", "pkgs", "periodictable-*.whl"))

U18, U22 = 931.49410242, 931.49410372          # MeV
ME18, ME22 = 0.51099895000, 0.51099895069      # MeV
ME_TREE = 0.510998951                          # PDG-2026 capture as massform reads it
MN, MH = 939.56542052, 938.78307               # neutron; 1H atom (m_p + m_e - 13.6 eV) MeV
MP = 938.27208816

fails = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("   " + detail if detail else ""))
    if not ok:
        fails.append(name)

# ---------------------------------------------------------------- W1 capture
rows = []
for ln in open(CAP, encoding="utf-8"):
    if ln.startswith("#") or ln.startswith("Z\t"):
        continue
    p = ln.rstrip("\n").split("\t")
    if len(p) < 7:
        continue
    Z, N, A = int(p[0]), int(p[1]), int(p[2])
    if A != Z + N:
        continue
    rows.append((Z, N, A, p[3], float(p[4]), float(p[5]), p[6]))
print("W1 rows:", len(rows), " measured(M):", sum(r[6] == "M" for r in rows))

def mu_nuc(Z, A, d_kev, u=U18, me=ME_TREE, be_kev=0.0):
    return (A * u + d_kev / 1000.0 - Z * me + be_kev / 1000.0) / A

def ranked(rs, f):
    return sorted(((f(r), r) for r in rs if r[2] >= 2), key=lambda t: t[0])

meas = [r for r in rows if r[6] == "M"]
rk = ranked(meas, lambda r: mu_nuc(r[0], r[2], r[4]))
best = rk[0]
print("W1 least nuclear mass/nucleon (M rows, CODATA18 u, tree m_e): %.7f MeV  %d%s"
      % (best[0], best[1][2], best[1][3]))
for v, r in rk[:6]:
    print("     %.7f  %3d%-3s  dm = %s keV +/- %s" % (v, r[2], r[3], r[4], r[5]))
chk("W1 argmin is 56Fe", (best[1][3], best[1][2]) == ("Fe", 56))
chk("W1 mu_min rounds to 930.1746 (massform.py:491)", round(best[0], 4) == 930.1746,
    "%.7f" % best[0])
margin = rk[1][0] - rk[0][0]
print("     margin to runner-up %d%s: %.3f keV/nucleon" % (rk[1][1][2], rk[1][1][3], margin * 1e3))

# all rows incl. extrapolated (E): does any lie lower?
rk_all = ranked(rows, lambda r: mu_nuc(r[0], r[2], r[4]))
chk("W1 no extrapolated (E) row lies below 56Fe either", rk_all[0][1][2:4] == (56, "Fe"))

# atomic mass per nucleon (electrons INCLUDED) -- also 56Fe
rka = ranked(meas, lambda r: (r[2] * U18 + r[4] / 1000.0) / r[2])
chk("W1 least ATOMIC mass/nucleon is also 56Fe", rka[0][1][2:4] == (56, "Fe"),
    "%.6f MeV; runner-up %d%s" % (rka[0][0], rka[1][1][2], rka[1][1][3]))

# binding energy per nucleon maximum -- 62Ni, not 56Fe (the tree's quantity is
# mass per nucleon, which is the correct one for a mass floor)
def ba(r):
    Z, N, A, d = r[0], r[1], r[2], r[4] / 1000.0
    return (Z * (MH - U18) + N * (MN - U18) - d) / A      # atomic-mass BE, MeV
rkb = sorted(((ba(r), r) for r in meas if r[2] >= 2), key=lambda t: -t[0])
chk("max B/A among measured is 62Ni (distinct from least mass/nucleon)",
    rkb[0][1][2:4] == (62, "Ni"),
    "62Ni %.4f vs 56Fe %.4f MeV" % (rkb[0][0], ba([r for r in meas if r[2:4] == (56, 'Fe')][0])))

# electron binding (Lunney-Pearson-Thibault 2003 eq. A4 form, NAMED-NOT-READ)
def be_el_kev(Z):
    return (14.4381 * Z ** 2.39 + 1.55468e-6 * Z ** 5.35) / 1000.0
rkbe = ranked(meas, lambda r: mu_nuc(r[0], r[2], r[4], be_kev=be_el_kev(r[0])))
chk("with electron binding restored the argmin is still 56Fe", rkbe[0][1][2:4] == (56, "Fe"),
    "%.7f MeV (+%.4f keV/nucleon vs dropped)" % (rkbe[0][0], (rkbe[0][0] - best[0]) * 1e3))
chk("dropping electron binding LOWERS mu (floor stays a floor)", rkbe[0][0] > best[0])

# CODATA 2022 constants
fe = [r for r in meas if r[2:4] == (56, "Fe")][0]
m22 = mu_nuc(fe[0], fe[2], fe[4], u=U22, me=ME22)
m18 = mu_nuc(fe[0], fe[2], fe[4], u=U18, me=ME18)
print("56Fe mu: CODATA18 %.7f  CODATA22 %.7f  shift %.3e MeV" % (m18, m22, m22 - m18))
chk("CODATA 2022 move leaves mu_min at 930.1746 to 4 d.p.", round(m22, 4) == 930.1746)
unc = fe[5] / 1000.0 / 56
print("56Fe mass-excess uncertainty 0.27 keV -> %.2e MeV per nucleon" % unc)

# ---------------------------------------------------------------- W2 witness
if WHEEL:
    txt = zipfile.ZipFile(WHEEL[0]).read("periodictable/mass.py").decode("iso-8859-15")
    w2 = {}
    for m in re.finditer(r"^(\d+)-([A-Za-z]+)-(\d+),([0-9.]+)\(", txt, re.M):
        Z, sym, A, mu = int(m.group(1)), m.group(2), int(m.group(3)), float(m.group(4))
        w2[(Z, A)] = (sym, mu)
    print("W2 isotopes parsed:", len(w2))
    d56 = (w2[(26, 56)][1] - 56) * U18 * 1000.0
    chk("W2 56Fe mass excess agrees with W1 (-60607.16 keV) within 0.05 keV",
        abs(d56 - fe[4]) < 0.05, "W2 %.3f keV" % d56)
    # compare every common measured nuclide
    worst = 0.0; n = 0
    for r in meas:
        k = (r[0], r[2])
        if k in w2:
            dd = (w2[k][1] - r[2]) * U18 * 1000.0 - r[4]
            s = abs(dd) / max(r[5], 1e-9)
            worst = max(worst, s); n += 1
    print("W2 vs W1 over %d measured nuclides: worst |diff|/sigma = %.3f" % (n, worst))
    w2rk = sorted((((A * U18 + (mu - A) * U18) - Z * ME_TREE) / A, Z, A, s)
                  for (Z, A), (s, mu) in w2.items() if A >= 2)
    chk("W2 (all isotopes it lists) least nuclear mass/nucleon is 56Fe",
        w2rk[0][2:] == (56, "Fe"), "%.7f MeV; next %d%s" % (w2rk[0][0], w2rk[1][2], w2rk[1][3]))

    # Z per element (gravity.symbol_to_Z, massform.py:1753): W1 symbol->Z vs W2
    z1 = {}
    for r in rows:
        z1.setdefault(r[3], r[0])
    z2 = {}
    for (Z, A), (sym, mu) in w2.items():
        z2.setdefault(sym, Z)
    common = sorted(set(z1) & set(z2))
    bad = [(s, z1[s], z2[s]) for s in common if z1[s] != z2[s]]
    chk("Z per element: W1 symbol->Z agrees with W2 on every common symbol",
        not bad, "%d symbols compared, %d disagree %s" % (len(common), len(bad), bad[:5]))
    # the 14 stock.HUMAN elements, conventional Z
    human = {"O": 8, "C": 6, "H": 1, "N": 7, "Ca": 20, "P": 15, "K": 19, "S": 16,
             "Na": 11, "Cl": 17, "Mg": 12, "Fe": 26, "F": 9, "Zn": 30}
    chk("Z per element: conventional Z for common payload elements",
        all(z1.get(k) == v for k, v in human.items()))
else:
    print("W2 wheel not present; W2 checks skipped")

# ---------------------------------------------------------------- the floor ratio
MEV_J = 1.602176634e-13
C = 299792458.0
B = 4.210860155904025e28      # massform.COUNTS['B'] (stock.HUMAN, 70 kg) -- not AME's
M = 70.0
ratio = 1 + B * best[0] * MEV_J / (M * C ** 2)
chk("pair floor ratio 1 + B mu_min c^2/(M c^2) rounds to 1.9975", round(ratio, 4) == 1.9975,
    "%.7f" % ratio)
# sensitivity: how far would mu have to fall to move the 4th decimal / to cross 1.5
dratio_dmu = B * MEV_J / (M * C ** 2)
print("d(ratio)/d(mu) = %.3e per MeV; a 1 MeV lower mu moves ratio by %.5f" % (dratio_dmu, dratio_dmu))
for mu_alt in (930.1746, 920.0, 900.0, 800.0):
    print("   if the cheapest baryon carrier were %.1f MeV/baryon: ratio %.4f" %
          (mu_alt, 1 + B * mu_alt * MEV_J / (M * C ** 2)))

# what datum shift would move the printed figures
lo = (round(ratio, 4) - 0.00005 - ratio) / dratio_dmu
hi = (round(ratio, 4) + 0.00005 - ratio) / dratio_dmu
print("ratio stays 1.9975 for mu in [%+.4f, %+.4f] MeV of mu_min, i.e. a 56Fe mass-excess shift of"
      " [%+.0f, %+.0f] keV (sigma 0.27 keV)" % (lo, hi, lo * 56e3, hi * 56e3))
print("mu_min's 4th decimal: 930.1745822 needs %+.1f / %+.1f eV per nucleon, i.e. %+.2f / %+.2f keV on dm(56Fe)"
      % ((930.17455 - best[0]) * 1e6, (930.17465 - best[0]) * 1e6,
         (930.17455 - best[0]) * 56e3, (930.17465 - best[0]) * 56e3))
print("argmin: 60Ni would need its mass excess lowered by %.0f keV (sigma 0.4 keV) to overtake 56Fe"
      % (margin * 60e3))
grav = 6.67430e-11 * M / (1.0 * C ** 2)
chk("gravitational binding order G M/(R c^2) at R = 1 m is 5.2e-26", round(grav, 27) == 5.2e-26 or abs(grav - 5.198e-26) < 1e-28,
    "%.4e" % grav)
chk("mu_min < m_p (and < m_n): bound nucleons are lighter", best[0] < MP < MN)

print()
print("FAILS:", fails if fails else "none")
sys.exit(1 if fails else 0)
