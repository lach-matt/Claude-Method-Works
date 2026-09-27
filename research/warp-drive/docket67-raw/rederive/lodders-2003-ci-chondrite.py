#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation for key lodders-2003-ci-chondrite.

Lodders (2003), ApJ 591, 1220 -- CI chondrite bulk composition, as used by
research/warp-drive/stockgate.py (CHONDRITE :395-414, SOURCES['L03'] :284) and
stock.py (CHONDRITE :216-219, SOURCES['chondrite'] :195).  Read-only on the tree.

Provenance of every comparison column (status words are part of the data):
  TREE   stockgate.CHONDRITE / stock.CHONDRITE, imported (never copied).
  L03    Lodders 2003 Table 3 CI weighted means, ppm.  NOT READ BY THIS AGENT:
         alphaXiv returned 'assistant quota exceeded' on every call and arxiv.org,
         iopscience.iop.org, ui.adsabs.harvard.edu, link.springer.com and
         ntrs.nasa.gov are egress-blocked.  The values are the sibling DOCKET-67
         audit's transcription (audits/lodders-2003-apj-591-1220.json,
         rederive/lodders-2003-apj-591-1220.py), read there at source (p.1225).
         Status here: CARRIED-FROM-SIBLING-AUDIT.
  MS95   McDonough & Sun (1995) Chem. Geol. 120, 223, CI column, READ from the
         pypi package pyrolite 0.3.7, data/geochem/refcomp/CH_McDonoughSun1995.csv.
         That file prints N as '3.18 ppm' and P as '1.08 ppm' beside C '3.5 %':
         a units anomaly in the package (3.18 ppm N is ~1000x below every CI
         value in the other three columns); read here as 3180 and 1080 ppm and
         FLAGGED.  Uncertainty column: 'F2' = factor of 2 (N, C, Cl, As...).
  PON14  Palme & O'Neill (2014) Treatise on Geochem. 2nd ed. 3, 1, CI column,
         READ from pyrolite CH_PalmeONeill2014.csv (column unc_2sigma).
  LBP25  Lodders, Bergemann & Palme (2025) SSRv 221, 23 (arXiv:2502.10575),
         Table 4, ppm.  NOT READ BY THIS AGENT; carried from the sibling audit
         (N 1965 +- 970).  A web-search snippet (not a read) gives 1965 +- 447:
         the uncertainty is itself unsettled between the two relays.

Exit 0 when every CHECK passes.  DISCREPANCY lines are recorded, not repaired.
"""
import csv
import os
import sys

sys.dont_write_bytecode = True
TREE = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, TREE)
import stockgate as sg  # noqa: E402
import stock as st      # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
PYRO = os.path.join(HERE, "..", "src", "pyrolite_ch")
FAIL = []


def chk(label, ok):
    print(("CHECK PASS  " if ok else "CHECK FAIL  ") + label)
    if not ok:
        FAIL.append(label)


def load_pyrolite(fn, fix=None):
    unit = {"%": 1e-2, "ppm": 1e-6, "ppb": 1e-9}
    out, unc = {}, {}
    with open(os.path.join(PYRO, fn)) as fh:
        for row in csv.reader(fh):
            if len(row) < 3 or row[2] not in unit or not row[1]:
                continue
            out[row[0]] = float(row[1]) * unit[row[2]]
            if len(row) > 3 and row[3]:
                try:
                    unc[row[0]] = float(row[3]) * unit[row[2]]
                except ValueError:
                    pass
            if len(row) > 6 and row[6]:
                unc.setdefault(row[0] + "_txt", row[6])
    for e, v in (fix or {}).items():
        out[e] = v
    return out, unc


L03 = {k: v * 1e-6 for k, v in {
    "H": 21015, "C": 35180, "N": 2940, "O": 458200, "F": 60.6, "Na": 5010,
    "Mg": 95870, "Al": 8500, "Si": 106500, "P": 920, "S": 54100, "Cl": 704,
    "K": 530, "Ca": 9070, "Sc": 5.83, "Ti": 440, "V": 55.7, "Cr": 2590,
    "Mn": 1910, "Fe": 182800, "Co": 502, "Ni": 10640, "Cu": 127, "Zn": 310,
    "Ga": 9.51, "Ge": 33.2, "As": 1.73, "Se": 19.7, "Br": 3.43, "Rb": 2.13,
    "Sr": 7.74, "Y": 1.53, "Zr": 3.96, "Nb": 0.265, "Mo": 1.02, "Ag": 0.201,
    "Li": 1.46, "B": 0.713, "Be": 0.0252}.items()}
LBP25 = {k: v * 1e-6 for k, v in {
    "H": 18598, "Li": 1.48, "Be": 0.0225, "B": 0.744, "C": 37813, "N": 1965,
    "O": 465700, "F": 92, "Na": 4960, "Mg": 95600, "Al": 8470, "Si": 106600,
    "P": 989, "S": 51800, "Cl": 717, "K": 544, "Ca": 9148, "Sc": 5.76,
    "Ti": 442, "V": 53.1, "Cr": 2616, "Mn": 1936, "Fe": 185000, "Co": 514,
    "Ni": 11180, "Cu": 133, "Zn": 310, "Ga": 9.54, "Ge": 33.5, "As": 1.75,
    "Se": 21.5, "Br": 3.77, "Rb": 2.26, "Sr": 8.04, "Y": 1.52, "Zr": 3.65,
    "Nb": 0.271, "Mo": 0.947, "Ag": 0.206, "Cd": 0.682, "In": 0.0781,
    "Sn": 1.67}.items()}


def substituted(alt):
    """Tree CHONDRITE with every element alt tabulates replaced by alt's value."""
    d = {e: v for e, v in sg.CHONDRITE.items() if not e.endswith("_")}
    for e in d:
        if e in alt:
            d[e] = alt[e]
    return d


def main():
    MS95, ms_unc = load_pyrolite("CH_McDonoughSun1995.csv",
                                 fix={"N": 3180e-6, "P": 1080e-6})
    PON14, pon_unc = load_pyrolite("CH_PalmeONeill2014.csv")
    TREEC = {e: v for e, v in sg.CHONDRITE.items() if not e.endswith("_")}

    print("=== 1. the tree's figures, reproduced by import")
    e, f = sg.binding_under("as-composed 59", "CI chondrite")
    chk("stockgate binding_under('as-composed 59','CI chondrite') = ('P', 10.7012) [%s %.6f]"
        % (e, f), e == "P" and abs(f - 10.7012) < 5e-4)
    e2, f2 = st.binding_element(st.HUMAN, st.CHONDRITE)
    chk("stock.binding_element(HUMAN, CHONDRITE) = ('P', 1.0701e1) [%s %.6f]; 70 kg -> %.2f kg"
        % (e2, f2, 70 * f2), e2 == "P" and abs(f2 - 10.701) < 1e-3)
    same = all(abs(st.CHONDRITE[k] - sg.CHONDRITE[k]) == 0 for k in st.CHONDRITE)
    chk("stock.CHONDRITE (16 elements) equals stockgate.CHONDRITE on every shared element", same)
    r = sg.ranked(sg.PAYLOADS["as-composed 59"](), sg.CHONDRITE, 2)
    print("  runner-up %s at %.4f; P/N margin %.4f" % (r[1][0], r[1][1], r[0][1] / r[1][1]))
    s = sum(TREEC.values())
    print("  sum of stockgate.CHONDRITE mass fractions = %.6f (not renormalised)" % s)
    ce, cf = sg.binding_under("craft 1000 kg (DECLARED)", "CI chondrite")
    print("  craft binder %s at %.5g; craft/human %.2f" % (ce, cf, sg.craft_vs_human()))

    print("\n=== 2. WHOSE TABLE IS IT?  tree vs L03 (sibling transcription), MS95, PON14")
    cols = (("L03", L03), ("MS95", MS95), ("PON14", PON14))
    within = {c: [0, 0] for c, _ in cols}
    nearest = {c: 0 for c, _ in cols}
    exact = {c: [] for c, _ in cols}
    for el in sorted(TREEC, key=lambda k: -TREEC[k]):
        t = TREEC[el]
        rs = []
        for c, d in cols:
            if el in d and d[el] > 0:
                rr = t / d[el]
                rs.append((c, rr))
                within[c][1] += 1
                if abs(rr - 1) <= 0.005:
                    within[c][0] += 1
                    exact[c].append(el)
        if rs:
            best = min(rs, key=lambda x: abs(x[1] - 1))
            nearest[best[0]] += 1
            if el in ("O", "Fe", "Si", "Mg", "S", "C", "H", "Ca", "Al", "Na",
                      "N", "Ni", "P", "K", "Cl", "Zn", "Li", "Ta", "Au", "As"):
                print("  %-3s tree %.4g  " % (el, t)
                      + "  ".join("%s x%.3f" % (c, rr) for c, rr in rs))
    for c, _ in cols:
        print("  %-5s: %d of %d tree elements within 0.5%%: %s; nearest source for %d"
              % (c, within[c][0], within[c][1], ",".join(exact[c]), nearest[c]))
    print("  DISCREPANCY (attribution): the tree labels the table L03, but it is not"
          " L03 Table 3 as transcribed; it matches MS95 exactly on %d elements and"
          " PON14 on %d; it is a blend not identified here." % (within["MS95"][0], within["PON14"][0]))
    chk("attribution check ran on >= 30 elements per column",
        all(within[c][1] >= 30 for c, _ in cols))

    print("\n=== 3. THE BINDER under each CI compilation (as-composed 59 payload)")
    pay = sg.PAYLOADS["as-composed 59"]()
    hN, hP = pay["N"], pay["P"]
    res = {}
    for name, alt in (("TREE", {}), ("L03", L03), ("MS95", MS95),
                      ("PON14", PON14), ("LBP25", LBP25)):
        d = substituted(alt)
        be, bf = sg.processing_factor(pay, d)
        rk = sg.ranked(pay, d, 2)
        res[name] = (be, bf)
        print("  %-6s N %6.0f ppm  P %5.0f ppm  -> binder %s  factor %.4f  70 kg -> %.1f kg"
              "  (runner-up %s %.4f)" % (name, d["N"] * 1e6, d["P"] * 1e6, be, bf,
                                          70 * bf, rk[1][0], rk[1][1]))
    chk("binder is P under TREE, L03, MS95, PON14",
        all(res[k][0] == "P" for k in ("TREE", "L03", "MS95", "PON14")))
    chk("binder flips to N under LBP25 (carried datum)", res["LBP25"][0] == "N")

    print("\n=== 4. the crossover, closed form (sympy)")
    import sympy as sp
    NCI, PCI, hn, hp = sp.symbols("N_CI P_CI h_N h_P", positive=True)
    ncross = sp.solve(sp.Eq(hn / NCI, hp / PCI), NCI)[0]
    print("  N binds iff N_CI < %s" % ncross)
    for name, pv in (("TREE", TREEC["P"]), ("L03", L03["P"]), ("MS95", MS95["P"]),
                     ("PON14", PON14["P"]), ("LBP25", LBP25["P"])):
        nc = float(ncross.subs({hn: hN, hp: hP, PCI: pv}))
        print("  P = %4.0f ppm -> N crossover %.0f ppm" % (pv * 1e6, nc * 1e6))
    nc_tree = float(ncross.subs({hn: hN, hp: hP, PCI: TREEC["P"]}))
    chk("closed-form crossover at tree P reproduces 2400 ppm (+-5)",
        abs(nc_tree * 1e6 - 2400) < 5)
    print("  uncertainty bands on CI N against that crossover:")
    print("    MS95  3180 ppm, 'F2' (factor 2): %.0f..%.0f ppm -> spans crossover: %s"
          % (1590, 6360, 1590 < nc_tree * 1e6 < 6360))
    pu = pon_unc.get("N", 0)
    print("    PON14 %.0f ppm +- %.0f (2 sigma): %.0f..%.0f -> spans crossover at PON14 P %.0f: %s"
          % (PON14["N"] * 1e6, pu * 1e6, (PON14["N"] - pu) * 1e6, (PON14["N"] + pu) * 1e6,
             float(ncross.subs({hn: hN, hp: hP, PCI: PON14["P"]})) * 1e6,
             PON14["N"] - pu < float(ncross.subs({hn: hN, hp: hP, PCI: PON14["P"]}))))
    print("    L03   2940 +- 20 (carried): does not span")
    print("    LBP25 1965 +- 970 (carried) or +- 447 (search snippet): central value below;"
          " +970 band spans, +447 band tops at 2412 vs crossover %.0f"
          % (float(ncross.subs({hn: hN, hp: hP, PCI: LBP25["P"]})) * 1e6))
    chk("PON14 N 2-sigma band spans the crossover (read datum, no carried value used)",
        PON14["N"] - pu < float(ncross.subs({hn: hN, hp: hP, PCI: PON14["P"]})))

    print("\n=== 5. the P datum sets the figure: factor range over compilations")
    fs = {k: v[1] for k, v in res.items() if v[0] == "P"}
    lo, hi = min(fs.values()), max(fs.values())
    print("  P-bound factor spans %.3f..%.3f (70 kg: %.0f..%.0f kg); tree 10.701"
          % (lo, hi, 70 * lo, 70 * hi))
    print("  vs cosmic: stellar photosphere factor %.4g -> advantage %.1f..%.1f x"
          % (sg.binding_under("as-composed 59", "stellar photosphere")[1],
             sg.binding_under("as-composed 59", "stellar photosphere")[1] / max(hi, res["LBP25"][1]),
             sg.binding_under("as-composed 59", "stellar photosphere")[1] / lo))

    print("\n=== 6. craft binder Ta: tree 10 ppb against MS95 13.6 / PON14 15 ppb")
    cp = sg._norm(sg.CRAFT)
    for name, ta in (("TREE", TREEC["Ta"]), ("MS95", MS95["Ta"]), ("PON14", PON14["Ta"])):
        d = dict(TREEC); d["Ta"] = ta
        be, bf = sg.processing_factor(cp, d)
        print("  Ta %.1f ppb -> craft binder %s factor %.4g" % (ta * 1e9, be, bf))
    chk("craft binder stays Ta under MS95 and PON14 Ta",
        all(sg.processing_factor(cp, dict(TREEC, Ta=ta))[0] == "Ta"
            for ta in (MS95["Ta"], PON14["Ta"])))

    print("\n=== 7. 'retained its volatiles' (stockgate :175-177): CI vs solar, per Si, by number")
    sol = sg.solar_hybrid()
    am = sg.ATOMIC_MASS
    for el in ("H", "C", "N", "O", "P", "S", "Zn", "Fe", "Mg"):
        ci = (TREEC[el] / am[el]) / (TREEC["Si"] / am["Si"])
        so = (sol[el] / am[el]) / (sol["Si"] / am["Si"])
        print("  %-2s CI/solar = %.4f  (%s)" % (el, ci / so,
              "depleted x%.0f" % (so / ci) if ci / so < 0.5 else "~solar"))
    nci = (TREEC["N"] / am["N"]) / (TREEC["Si"] / am["Si"])
    nso = (sol["N"] / am["N"]) / (sol["Si"] / am["Si"])
    chk("CI N is depleted > 20x relative to solar (tree's own tables)", nso / nci > 20)
    print("  => a CI chondrite retained its MODERATELY volatile elements near solar and lost"
          " most of its most-volatile ones (N, C, H); the binder argument needs only"
          " CI N/P > payload N/P = %.3f, not 'retained its volatiles'." % (hN / hP))

    print("\nRESULT: %s" % ("ALL CHECKS PASS" if not FAIL else "FAILED: %s" % FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
