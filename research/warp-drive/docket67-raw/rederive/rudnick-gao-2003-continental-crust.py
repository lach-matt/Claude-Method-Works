#!/usr/bin/env python3
"""DOCKET 67 -- audit of Rudnick & Gao (2003) as stock.py / stockgate.py use it.

Read-only against research/warp-drive (imports the two owners by path, no
bytecode written).  Source values: pyrolite 0.3.7 refcomp CSVs
(BCC/UCC_RudnickGao2003.csv), a third-party machine-readable restatement of
R&G's Tables -- READ-VIA-RESTATEMENT, the Treatise chapter itself could not be
reached here (alphaXiv quota; academia/researchgate/ADS/arXiv egress-blocked).

Checks:
 1. reproduce the owners' crust numbers from their own tables;
 2. provenance: compare each CRUST entry with R&G bulk (BCC) and upper (UCC);
 3. substitute R&G values and recompute every conclusion that rests on them;
 4. thresholds: how far crust N, C, H can move before the binding element flips;
 5. sensitivity to the one later datum found (upper-crust N 150 ppm, Johnson &
    Goldblatt 2015 -- NAMED-NOT-READ, search-summary figure only).
Exit 0 always; prints PASS/DISCREPANCY lines.
"""
import csv, importlib.util, os, sys
sys.dont_write_bytecode = True
W = "/home/user/Claude-Method-Works/research/warp-drive"
D = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(D, "..", "src", "pyrolite_refcomp")

def load(name):
    spec = importlib.util.spec_from_file_location(name + "_ro", os.path.join(W, name + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

st = load("stock"); sg = load("stockgate")

AM = {"Si": 28.0855, "Ti": 47.867, "Al": 26.9815, "Fe": 55.845, "Mn": 54.938,
      "Mg": 24.305, "Ca": 40.078, "Na": 22.98977, "K": 39.0983, "P": 30.97376, "O": 15.9994}
OXIDE = {"SiO2": ("Si", 1, 2), "TiO2": ("Ti", 1, 2), "Al2O3": ("Al", 2, 3),
         "FeO": ("Fe", 1, 1), "MnO": ("Mn", 1, 1), "MgO": ("Mg", 1, 1),
         "CaO": ("Ca", 1, 1), "Na2O": ("Na", 2, 1), "K2O": ("K", 2, 1), "P2O5": ("P", 2, 5)}
SCALE = {"%": 1e-2, "ppm": 1e-6, "ppb": 1e-9}

def read_rg(fn):
    out, oxy = {}, 0.0
    for row in csv.DictReader(open(os.path.join(SRC, fn))):
        v, u = row["value"], row["units"]
        if not v or u not in SCALE: continue
        x = float(v) * SCALE[u]; k = row["var"]
        if k in OXIDE:
            el, n, no = OXIDE[k]
            mw = n * AM[el] + no * AM["O"]
            out[el] = x * n * AM[el] / mw; oxy += x * no * AM["O"] / mw
        else:
            out[k] = x
    out["O(stoich)"] = oxy
    return out

BCC = read_rg("BCC_RudnickGao2003.csv"); UCC = read_rg("UCC_RudnickGao2003.csv")
# The pyrolite BCC csv has "Na,56,ppm" among the trace rows -- Na is a major
# (Na2O 3.1 %), and UCC carries N 83 ppm in the N row.  The 56 ppm row is N
# mislabelled in the restatement (a discrepancy in the RESTATEMENT, recorded).
# The Na element value above came from Na2O and overwrote nothing: check.
na_row = [r for r in csv.DictReader(open(os.path.join(SRC, "BCC_RudnickGao2003.csv"))) if r["var"] in ("N", "Na")]
print("restatement rows N/Na:", [(r["var"], r["value"], r["units"]) for r in na_row])
BCC_N = 56e-6   # the mislabelled row, read as N (see note)
BCC["N"] = BCC_N
BCC["Na"] = 3.1e-2 * 2 * AM["Na"] / (2 * AM["Na"] + AM["O"])
UCC.setdefault("N", 83e-6)

def P(tag, cond, msg): print("%-12s %s" % (tag if cond else "DISCREPANCY", msg))

print("\n== 1. reproduce the owners' numbers from their own tables")
e, f = st.binding_element(st.HUMAN, st.CRUST)
P("PASS", e == "N" and abs(f - 428.05) < 0.01, "stock.py crust binds on %s at %.4e (tree 4.2805e2)" % (e, f))
fN = st.processing_factors(st.HUMAN, st.CRUST); rNP = fN["N"] / fN["P"]
P("PASS", abs(rNP - 40.4) < 0.05, "stock.py crust N/P factor ratio %.3f (tree 40.4)" % rNP)
eC, fC = st.binding_element(st.HUMAN, st.CHONDRITE)
P("PASS", round(f / fC) == 40, "stock.py crust/chondrite %.3f (tree 40.0)" % (f / fC))
hp = sg.payload("as-composed")
e2, f2 = sg.processing_factor(hp, sg.CRUST)
P("PASS", e2 == "N" and abs(f2 - 458.62) < 0.05, "stockgate crust binds on %s at %.4e (tree 4.5862e2)" % (e2, f2))
craft = sg._norm(sg.CRAFT); e3, f3 = sg.processing_factor(craft, sg.CRUST)
P("PASS", e3 == "Au" and abs(f3 / 2.6948e5 - 1) < 1e-4, "stockgate craft at crust binds on %s at %.4e (tree 2.6948e5)" % (e3, f3))

print("\n== 2. provenance: each CRUST entry vs R&G bulk (BCC) and upper (UCC), restated")
def prov(tab, name):
    rows = []
    for el, v in sorted(tab.items(), key=lambda kv: -kv[1]):
        if v <= 0: continue
        b, u = BCC.get(el), UCC.get(el)
        rb = v / b if b else None; ru = v / u if u else None
        if rb and abs(rb - 1) < 0.03: cls = "=BCC"
        elif ru and abs(ru - 1) < 0.03: cls = "=UCC"
        elif b is None and u is None: cls = "NOT-IN-R&G"
        else: cls = "neither"
        rows.append((el, v, b, u, cls))
    cnt = {}
    for r in rows: cnt[r[4]] = cnt.get(r[4], 0) + 1
    print("  %s: %s" % (name, cnt))
    for el, v, b, u, cls in rows:
        if cls != "=BCC":
            print("    %-3s tree %-10.4g BCC %-10s UCC %-10s %s" % (el, v, "%.4g" % b if b else "-", "%.4g" % u if u else "-", cls))
    return rows
rs = prov(st.CRUST, "stock.py CRUST (16)"); rg = prov(sg.CRUST, "stockgate.py CRUST")
print("  R&G-derived O by stoichiometry of the ten oxides: %.4f (tree O 0.461)" % BCC["O(stoich)"])

print("\n== 3. substitute R&G values; recompute what rests on them")
def rg_crust(base, rg, keep_non_rg=True):
    c = dict(base)
    for el in list(c):
        if el in rg: c[el] = rg[el]
    c["O"] = rg["O(stoich)"] if "O" in c else c.get("O")
    return c
res = {}
for lab, RG in (("BCC", BCC), ("UCC", UCC)):
    c1 = rg_crust(st.CRUST, RG); c2 = rg_crust(sg.CRUST, RG)
    e, f = st.binding_element(st.HUMAN, c1); fx = st.processing_factors(st.HUMAN, c1)
    e2, f2 = sg.processing_factor(hp, c2); e3, f3 = sg.processing_factor(craft, c2)
    rk = sg.ranked(hp, c2, 4)
    fchond_sg = sg.processing_factor(hp, sg.CHONDRITE)[1]
    res[lab] = dict(stock=(e, f), NP=fx["N"] / fx["P"], crust_over_chondrite=f / fC,
                    sg=(e2, f2), sg_over_chondrite=f2 / fchond_sg, craft=(e3, f3), ranked=rk)
    print("  [%s] stock.py: binds %s at %.4g (%.2f t/70kg); N/P %.2f; crust/chondrite %.2f"
          % (lab, e, f, 70 * f / 1000, fx["N"] / fx["P"], f / fC))
    print("  [%s] stockgate: binds %s at %.4g; crust/chondrite %.2f; craft binds %s at %.4g; top4 %s"
          % (lab, e2, f2, f2 / fchond_sg, e3, f3, [(k, round(v, 1)) for k, v in rk]))
for lab in res:
    P("PASS", res[lab]["stock"][0] == "N" and res[lab]["sg"][0] == "N",
      "[%s] binding element stays N in both owners" % lab)
    P("PASS", res[lab]["crust_over_chondrite"] > 10 and res[lab]["sg_over_chondrite"] > 10,
      "[%s] chondrite still beats crust by >10x (%.1f / %.1f)" % (lab, res[lab]["crust_over_chondrite"], res[lab]["sg_over_chondrite"]))
P("PASS", abs(res["BCC"]["NP"] - 40.4) < 0.5,
  "stock.py 'crust N is 40.4x crust P' under R&G BCC P: %.2f (UCC P: %.2f)" % (res["BCC"]["NP"], res["UCC"]["NP"]))

print("\n== 4. thresholds (stock.py HUMAN; others held at tree values)")
h = st.HUMAN; c = st.CRUST
Nstar_C = c["C"] * h["N"] / h["C"]; Nstar_H = c["H"] * h["N"] / h["H"]
print("  N stops binding when crust N exceeds min(C-limit %.0f ppm, H-limit %.0f ppm)" % (Nstar_C * 1e6, Nstar_H * 1e6))
Cstar = h["C"] * BCC_N / h["N"]
print("  with R&G N = 56 ppm, C takes over as binder if crust C < %.0f ppm (tree C = %.0f ppm; R&G tabulate NO C)" % (Cstar * 1e6, c["C"] * 1e6))
print("  with R&G UCC N = 83 ppm the C threshold is %.0f ppm" % (h["C"] * 83e-6 / h["N"] * 1e6))
c_lo = dict(c, C=2.0e-4, N=BCC_N)
print("  e.g. crust C = 200 ppm (an older compilation's figure, NOT READ here): binds %s at %.4g"
      % st.binding_element(h, c_lo))

print("\n== 5. later datum: upper-crust N 150 ppm (Johnson & Goldblatt 2015, NAMED-NOT-READ)")
for N in (56e-6, 83e-6, 150e-6):
    cc = dict(st.CRUST, N=N); e, f = st.binding_element(h, cc)
    cg = dict(sg.CRUST, N=N); e2, f2 = sg.processing_factor(hp, cg)
    print("  N = %3.0f ppm: stock.py binds %s at %.4g (crust/chondrite %.1f); stockgate binds %s at %.4g"
          % (N * 1e6, e, f, f / fC, e2, f2))
cc = dict(st.CRUST, N=150e-6); e, f = st.binding_element(h, cc)
P("PASS", e == "N", "at 150 ppm N still binds (runner-up C at %.4g)" % (h["C"] / cc["C"]))
