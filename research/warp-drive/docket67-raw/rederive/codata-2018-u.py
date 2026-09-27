#!/usr/bin/env python3
"""DOCKET 67 audit, key codata-2018-u.

Checks, READ-ONLY against research/warp-drive (imports, monkeypatches in memory,
writes nothing there; run with PYTHONDONTWRITEBYTECODE=1):

 1. gravity.U_KG against the CODATA 2018 table as transcribed verbatim from NIST
    in scipy.constants._codata.txt2018 (and txt2022 for the current value).
 2. Internal consistency of CODATA 2018: m_u = m_e / A_r(e).
 3. stock.ATOMIC_MASS against CIAAW 2021 standard atomic weights (Prohaska et al.
    2022, Pure Appl. Chem. 94) as transcribed in periodictable 2.1.0 mass.py.
 4. H-A: the natural mean nucleon number <A> of each listed element, from the
    CIAAW isotopic compositions (periodictable), and its distance from
    round(ATOMIC_MASS[e]); for interval elements, the extremes of the interval.
 5. The counts B, N_e, N_n and the three H-A booleans massform's selftest checks
    (largest central reading < 0.5, pair floor > 1.9 Mc^2, extra leptons > 0)
    under: the tree's inputs; CODATA 2022 u; CIAAW 2021 full-precision weights;
    exact <A> in place of round(A_r); and the interval extremes of H, C, N, O.
"""
import os, sys, re, json
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "pylib"))
WD = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, WD)
sys.dont_write_bytecode = True

import scipy, scipy.constants._codata as cod
import periodictable as pt
import periodictable.mass as ptm
import gravity, stock
import massform as mf

out = {"scipy": scipy.__version__, "periodictable": pt.__version__}

def table_value(txt, name):
    for line in txt.split("\n"):
        if line.startswith(name + "  "):
            rest = line[len(name):].strip()
            parts = re.split(r"\s{2,}", rest)
            v = float(parts[0].replace(" ", "").replace("...", ""))
            u = float(parts[1].replace(" ", "")) if parts[1].strip() != "(exact)" else 0.0
            return v, u, line
    raise KeyError(name)

# ---------------------------------------------------------------- 1, 2
u18, s18, l18 = table_value(cod.txt2018, "atomic mass constant")
u22, s22, l22 = table_value(cod.txt2022, "atomic mass constant")
me18, _, _ = table_value(cod.txt2018, "electron mass")
are18, _, _ = table_value(cod.txt2018, "electron relative atomic mass")
mev18, smev18, _ = table_value(cod.txt2018, "atomic mass constant energy equivalent in MeV")
out["codata2018_line"] = l18.strip()
out["codata2022_line"] = l22.strip()
out["tree_U_KG"] = gravity.U_KG
out["tree_equals_2018"] = (gravity.U_KG == u18)
out["tree_U_MEV"] = mf.U_MEV
out["U_MEV_minus_2018_MeV_equiv"] = mf.U_MEV - mev18
out["U_MEV_diff_over_2018_sigma"] = (mf.U_MEV - mev18) / smev18
out["me_over_Are_2018"] = me18 / are18
out["me_over_Are_rel_diff"] = me18 / are18 / u18 - 1
out["u22_minus_u18_rel"] = u22 / u18 - 1
out["u22_minus_u18_in_sigma18"] = (u22 - u18) / s18
out["u22_minus_u18_in_sigma22"] = (u22 - u18) / s22

# ---------------------------------------------------------------- 3
aw = {}
for el in stock.ATOMIC_MASS:
    e = getattr(pt, el)
    aw[el] = {"tree": stock.ATOMIC_MASS[el], "ciaaw2021": e.mass,
              "abs_diff": stock.ATOMIC_MASS[el] - e.mass,
              "rel_diff": stock.ATOMIC_MASS[el] / e.mass - 1}
out["atomic_weights"] = aw
out["max_rel_diff_weights_all"] = max(abs(v["rel_diff"]) for v in aw.values())
out["max_rel_diff_weights_HUMAN"] = max(abs(aw[e]["rel_diff"]) for e in stock.HUMAN)

# ---------------------------------------------------------------- 4 (H-A)
# periodictable parses an interval "[a,b]" to its midpoint; for the extremes
# we re-parse the raw CIAAW text held in periodictable.mass.isotope_abundance.
raw = {}
z = None
for line in ptm.isotope_abundance.split("\n"):
    if not line.strip():
        continue
    if line[0] not in " \t":
        z = int(line.split()[0]); raw[z] = {}
    else:
        p = line.split()
        m = re.match(r"\[([0-9.]+),([0-9.]+)\]", p[1])
        if m:
            raw[z][int(p[0])] = (float(m.group(1)), float(m.group(2)))
        else:
            v = float(p[1].split("(")[0]); raw[z][int(p[0])] = (v, v)

def mean_A(el):
    e = getattr(pt, el)
    isos = [(iso.isotope, iso.abundance / 100.0) for iso in e if iso.abundance > 0]
    if el == "H":   # periodictable carries H abundance via isotopes 1,2
        pass
    tot = sum(a for _, a in isos)
    return sum(A * a for A, a in isos) / tot

def mean_A_extremes(el):
    """min and max of <A> over abundance vectors inside the CIAAW intervals and
    summing to 1 (a linear programme solved greedily: push weight to the
    heaviest / lightest isotope first)."""
    Z = getattr(pt, el).number
    if Z not in raw:
        a = mean_A(el); return a, a
    iv = raw[Z]
    isos = sorted(iv)
    res = []
    for heavy_first in (False, True):
        lo = {A: iv[A][0] for A in isos}
        rem = 1.0 - sum(lo.values())
        order = sorted(isos, reverse=heavy_first)
        x = dict(lo)
        for A in order:
            add = min(iv[A][1] - iv[A][0], max(rem, 0.0))
            x[A] += add; rem -= add
        res.append(sum(A * x[A] for A in isos) / sum(x.values()))
    return min(res), max(res)

ha = {}
for el in stock.HUMAN:
    Ae = round(stock.ATOMIC_MASS[el])
    mA = mean_A(el)
    lo, hi = mean_A_extremes(el)
    ha[el] = {"A_e": Ae, "mean_A_ciaaw": mA, "mean_A_min": lo, "mean_A_max": hi,
              "margin_to_half": 0.5 - max(abs(lo - Ae), abs(hi - Ae), abs(mA - Ae))}
out["H_A"] = ha
out["H_A_holds_all"] = all(v["margin_to_half"] > 0 for v in ha.values())
out["H_A_tightest"] = min(ha, key=lambda k: ha[k]["margin_to_half"])

# ---------------------------------------------------------------- 5
E = mf.rest_energy_j()

def booleans(cc):
    return {"largest_central_reading": mf.largest_central_reading(mf.share_rows(cc)),
            "C2_ge_half": mf.largest_central_reading(mf.share_rows(cc)) >= 0.5,
            "floor_over_Mc2": mf.pair_floor_j(cc) / E,
            "floor_gt_1.9": mf.pair_floor_j(cc) / E > 1.9,
            "extra_leptons": mf.extra_leptons(cc),
            "extra_leptons_gt_0": mf.extra_leptons(cc) > 0}

def counts_exact(weights, amean, u):
    M = Fraction(repr(float(mf.PAYLOAD_KG)))
    uu = Fraction(repr(u))
    B = Ne = Fraction(0)
    for el, f in stock.HUMAN.items():
        atoms = Fraction(repr(f)) * M / (Fraction(repr(weights[el])) * uu)
        B += atoms * Fraction(repr(amean[el]))
        Ne += atoms * mf.Z_OF[el]
    listed = sum(Fraction(repr(f)) for f in stock.HUMAN.values())
    return {"B": float(B), "N_e": float(Ne), "N_p": float(Ne), "N_n": float(B - Ne),
            "B_minus_L": float(B - Ne), "listed": float(listed), "unlisted": float(1 - listed)}

tree_w = dict(stock.ATOMIC_MASS)
ciaaw_w = {el: getattr(pt, el).mass for el in stock.HUMAN}
int_A = {el: round(stock.ATOMIC_MASS[el]) for el in stock.HUMAN}
exact_A = {el: mean_A(el) for el in stock.HUMAN}

scen = {}
def run(name, w, A, u):
    saved = (mf.U_KG, mf.U_MEV, mf.MU_MIN)
    try:
        mf.U_KG = u; mf.U_MEV = u / mf.MEV_KG; mf.MU_MIN = mf.mu_min_mev()
        cc = counts_exact(w, A, u)
        r = {k: cc[k] for k in ("B", "N_e", "N_n")}
        r["mu_min_MeV"] = mf.MU_MIN[0]
        r.update(booleans(cc))
    finally:
        mf.U_KG, mf.U_MEV, mf.MU_MIN = saved
    scen[name] = r

run("tree", tree_w, int_A, gravity.U_KG)
# identity check against massform's own COUNTS
scen["tree"]["matches_massform_COUNTS"] = all(
    abs(scen["tree"][k] / mf.COUNTS[k] - 1) < 1e-15 for k in ("B", "N_e", "N_n"))
run("u_CODATA2022", tree_w, int_A, u22)
run("weights_CIAAW2021", ciaaw_w, int_A, gravity.U_KG)
run("exact_meanA", tree_w, exact_A, gravity.U_KG)
run("all_current", ciaaw_w, exact_A, u22)
# interval extremes for the four dominant interval elements
iv_w = {"H": (1.00784, 1.00811), "C": (12.0096, 12.0116),
        "N": (14.00643, 14.00728), "O": (15.99903, 15.99977)}
lo_w = dict(tree_w); hi_w = dict(tree_w)
for el, (a, b) in iv_w.items():
    lo_w[el] = a; hi_w[el] = b
run("weights_interval_low_HCNO", lo_w, int_A, gravity.U_KG)
run("weights_interval_high_HCNO", hi_w, int_A, gravity.U_KG)
base = scen["tree"]
for k, v in scen.items():
    v["rel_dB"] = v["B"] / base["B"] - 1
    v["rel_dNe"] = v["N_e"] / base["N_e"] - 1
    v["rel_dNn"] = v["N_n"] / base["N_n"] - 1
    v["booleans_same_as_tree"] = (v["C2_ge_half"], v["floor_gt_1.9"], v["extra_leptons_gt_0"]) == \
        (base["C2_ge_half"], base["floor_gt_1.9"], base["extra_leptons_gt_0"])
out["scenarios"] = scen
out["data_used_as_stated"] = {"B": 4.2109e28, "N_e": 2.3132e28, "N_n": 1.8977e28}
out["data_used_reproduced"] = all(
    abs(float("%.4e" % base[k]) - v) / v < 1e-9 for k, v in out["data_used_as_stated"].items())
out["all_booleans_stand"] = all(v["booleans_same_as_tree"] for v in scen.values())

print(json.dumps(out, indent=1, default=str))
ok = (out["tree_equals_2018"] and out["data_used_reproduced"] and out["all_booleans_stand"]
      and out["H_A_holds_all"] and scen["tree"]["matches_massform_COUNTS"])
print("VERDICT-INPUT:", "AGREES" if ok else "DISAGREES")
_EXIT = 0 if ok else 1

# ---------------------------------------------------------------- 6 (appended)
# The binding closure (nucleon + electron rest - listed payload), which the tree
# itself names as "the one figure H-A moves materially" (massform.py:1829-1830).
_cc_tree = counts_exact(tree_w, int_A, gravity.U_KG)
_cc_exact = counts_exact(tree_w, exact_A, gravity.U_KG)
_bt = mf.payload_masses(_cc_tree)["binding (closure)"]
_be = mf.payload_masses(_cc_exact)["binding (closure)"]
_bp = mf.payload_masses(mf.counts(a_shift=Fraction(1, 2)))["binding (closure)"]
_bm = mf.payload_masses(mf.counts(a_shift=Fraction(-1, 2)))["binding (closure)"]
print("BINDING-CLOSURE kg: tree(H-A integer) %.6f  exact<A> %.6f  tree bracket A-1/2 %.6f  A+1/2 %.6f"
      % (_bt, _be, _bm, _bp))
print("BINDING-CLOSURE exact inside the tree's own +/-1/2 bracket:", min(_bm, _bp) <= _be <= max(_bm, _bp))
print("B at 5 s.f.: tree %.4e  exact<A> %.4e ; N_n tree %.4e exact<A> %.4e"
      % (_cc_tree["B"], _cc_exact["B"], _cc_tree["N_n"], _cc_exact["N_n"]))

# ---------------------------------------------------------------- 7 (appended)
# Decomposition of the 2018 -> 2022 move in u, from the two tables alone:
# m_u = m_e / A_r(e) and m_e = 2 h R_inf / (c alpha^2) (h, c exact), so
# d ln u = d ln R_inf - 2 d ln alpha - d ln A_r(e).
import math
def tv(t, n): return table_value(t, n)[0]
d = {}
for n in ("fine-structure constant", "Rydberg constant", "electron relative atomic mass", "electron mass"):
    d[n] = math.log(tv(cod.txt2022, n) / tv(cod.txt2018, n))
pred = d["Rydberg constant"] - 2 * d["fine-structure constant"] - d["electron relative atomic mass"]
print("DECOMP d ln u: from tables %.4e ; predicted R - 2 alpha - A_r(e) = %.4e ; parts: dlnR %.3e, -2 dln alpha %.3e, -dln A_r(e) %.3e"
      % (math.log(u22 / u18), pred, d["Rydberg constant"], -2 * d["fine-structure constant"], -d["electron relative atomic mass"]))
a18, sa18, _ = table_value(cod.txt2018, "fine-structure constant")
a22, sa22, _ = table_value(cod.txt2022, "fine-structure constant")
print("ALPHA 2018 %.13e (%.1e)  2022 %.13e (%.1e)  shift/sigma18 %.2f" % (a18, sa18, a22, sa22, (a22 - a18) / sa18))

sys.exit(_EXIT)
