#!/usr/bin/env python3
"""DOCKET 67 -- audit of the tree's ATOMIC_MASS tables (stockgate.py:314-328, stock.py:206-209)
against the CIAAW/IUPAC Standard Atomic Weights 2024 (READ at www.ciaaw.org/atomic-weights.htm,
abridged-atomic-weights.htm, isotopic-abundances.htm via alphaXiv answer_pdf_queries, 2026-09-26).
Read-only: imports the owners with bytecode writing off; writes nothing under research/.

Checks
  A  every tree value against the CIAAW 2024 standard atomic weight (interval or value(U))
  B  independent re-derivation: sum_i x_i m_i with x_i = CIAAW 2024 representative isotopic
     composition (READ) and m_i = AME2020 Table I (the tree's own READ capture)
  C  hypothesis 'normal (terrestrial) material': recompute every stockgate/stock verdict with
     solar-system isotopic compositions (Asplund et al. 2009 Table 3, arXiv:0909.0948, READ)
  D  massform H-A: |mean nucleon number - round(tree weight)| < 1/2 for stock.HUMAN's 14 elements
"""
import sys, io, contextlib
sys.dont_write_bytecode = True
WD = "/home/user/Claude-Method-Works/research/warp-drive"
sys.path.insert(0, WD)
AME = "/home/user/Claude-Method-Works/extracted/archives/restore-point-2-13/captures/AME2020-TableI.tsv"
KEV_PER_U = 931494.10242          # CODATA 2018, as the u the AME table uses

# ---- CIAAW 2024 standard atomic weights (READ). ('I', lo, hi, abridged) or ('V', value, U, abridged)
C24 = {
 "H": ("I", 1.00784, 1.00811, 1.0080), "He": ("V", 4.002602, 0.000002, 4.0026),
 "Li": ("I", 6.938, 6.997, 6.94), "Be": ("V", 9.0121831, 0.0000005, 9.0122),
 "B": ("I", 10.806, 10.821, 10.81), "C": ("I", 12.0096, 12.0116, 12.011),
 "N": ("I", 14.00643, 14.00728, 14.007), "O": ("I", 15.99903, 15.99977, 15.999),
 "F": ("V", 18.998403162, 0.000000005, 18.998), "Ne": ("V", 20.1797, 0.0006, 20.180),
 "Na": ("V", 22.98976928, 0.00000002, 22.990), "Mg": ("I", 24.304, 24.307, 24.305),
 "Al": ("V", 26.9815384, 0.0000003, 26.982), "Si": ("I", 28.084, 28.086, 28.085),
 "P": ("V", 30.973761998, 0.000000005, 30.974), "S": ("I", 32.059, 32.076, 32.06),
 "Cl": ("I", 35.446, 35.457, 35.45), "Ar": ("I", 39.792, 39.963, 39.95),
 "K": ("V", 39.0983, 0.0001, 39.098), "Ca": ("V", 40.078, 0.004, 40.078),
 "Sc": ("V", 44.955907, 0.000004, 44.956), "Ti": ("V", 47.867, 0.001, 47.867),
 "V": ("V", 50.9415, 0.0001, 50.942), "Cr": ("V", 51.9961, 0.0006, 51.996),
 "Mn": ("V", 54.938043, 0.000002, 54.938), "Fe": ("V", 55.845, 0.002, 55.845),
 "Co": ("V", 58.933194, 0.000003, 58.933), "Ni": ("V", 58.6934, 0.0004, 58.693),
 "Cu": ("V", 63.546, 0.003, 63.546), "Zn": ("V", 65.38, 0.02, 65.38),
 "Ga": ("V", 69.723, 0.001, 69.723), "Ge": ("V", 72.630, 0.008, 72.630),
 "As": ("V", 74.921595, 0.000006, 74.922), "Se": ("V", 78.971, 0.008, 78.971),
 "Br": ("I", 79.901, 79.907, 79.904), "Rb": ("V", 85.4678, 0.0003, 85.468),
 "Sr": ("V", 87.62, 0.01, 87.62), "Y": ("V", 88.905838, 0.000002, 88.906),
 "Zr": ("V", 91.222, 0.003, 91.222), "Nb": ("V", 92.90637, 0.00001, 92.906),
 "Mo": ("V", 95.95, 0.01, 95.95), "Ag": ("V", 107.8682, 0.0002, 107.87),
 "Cd": ("V", 112.414, 0.004, 112.41), "In": ("V", 114.818, 0.001, 114.82),
 "Sn": ("V", 118.710, 0.007, 118.71), "Sb": ("V", 121.760, 0.001, 121.76),
 "Te": ("V", 127.60, 0.03, 127.60), "I": ("V", 126.90447, 0.00003, 126.90),
 "Cs": ("V", 132.90545196, 0.00000006, 132.91), "Ba": ("V", 137.327, 0.007, 137.33),
 "La": ("V", 138.90547, 0.00007, 138.91), "Ce": ("V", 140.116, 0.001, 140.12),
 "Nd": ("V", 144.242, 0.003, 144.24), "Sm": ("V", 150.36, 0.02, 150.36),
 "Ta": ("V", 180.94788, 0.00002, 180.95), "W": ("V", 183.84, 0.01, 183.84),
 "Au": ("V", 196.966570, 0.000004, 196.97), "Hg": ("V", 200.592, 0.003, 200.59),
 "Tl": ("I", 204.382, 204.385, 204.38), "Pb": ("I", 206.14, 207.94, 207.2),
 "Bi": ("V", 208.98040, 0.00001, 208.98), "Th": ("V", 232.0377, 0.0004, 232.04),
 "U": ("V", 238.02891, 0.00003, 238.03),
}
# pre-2017 / pre-2024 single values, for the two stale entries (historical, from the
# CIAAW 2013 table as the tree's digits reproduce it -- NOT READ here; labelled as such)
PRIOR_NOT_READ = {"Ar": "39.948(1) (standard value before the 2017 interval)",
                  "Zr": "91.224(2) (standard value before the 2024 revision)"}

# ---- CIAAW 2024 representative isotopic compositions (READ); intervals -> midpoints, renormalised
ISO24 = {
 "H": {1: (0.99972, 0.99999), 2: (0.00001, 0.00028)}, "He": {3: 0.000002, 4: 0.999998},
 "Li": {6: (0.019, 0.078), 7: (0.922, 0.981)}, "C": {12: (0.9884, 0.9904), 13: (0.0096, 0.0116)},
 "N": {14: (0.99578, 0.99663), 15: (0.00337, 0.00422)},
 "O": {16: (0.99738, 0.99776), 17: (0.000367, 0.000400), 18: (0.00187, 0.00222)},
 "Ne": {20: 0.9048, 21: 0.0027, 22: 0.0925}, "Na": {23: 1.0},
 "Mg": {24: (0.7888, 0.7905), 25: (0.09988, 0.10034), 26: (0.1096, 0.1109)}, "Al": {27: 1.0},
 "Si": {28: (0.92191, 0.92318), 29: (0.04645, 0.04699), 30: (0.03037, 0.03110)}, "P": {31: 1.0},
 "S": {32: (0.9441, 0.9529), 33: (0.00729, 0.00797), 34: (0.0396, 0.0477), 36: (0.000129, 0.000187)},
 "Cl": {35: (0.755, 0.761), 37: (0.239, 0.245)},
 "K": {39: 0.932581, 40: 0.000117, 41: 0.067302},
 "Ca": {40: 0.96941, 42: 0.00647, 43: 0.00135, 44: 0.02086, 46: 0.00004, 48: 0.00187},
 "Fe": {54: 0.05845, 56: 0.91754, 57: 0.02119, 58: 0.00282},
 "Zn": {64: 0.4917, 66: 0.2773, 67: 0.0404, 68: 0.1845, 70: 0.0061},
}
# ---- Asplund et al. 2009 Table 3, solar-system representative isotopic fractions, % (READ)
A09T3 = {
 "H": {1: 99.998, 2: 0.002}, "He": {3: 0.0166, 4: 99.9834}, "Li": {6: 7.59, 7: 92.41},
 "C": {12: 98.8938, 13: 1.1062}, "N": {14: 99.771, 15: 0.229},
 "O": {16: 99.7621, 17: 0.0379, 18: 0.2000}, "Ne": {20: 92.9431, 21: 0.2228, 22: 6.8341},
 "Na": {23: 100.0}, "Mg": {24: 78.99, 25: 10.00, 26: 11.01}, "Al": {27: 100.0},
 "Si": {28: 92.2297, 29: 4.6832, 30: 3.0872}, "P": {31: 100.0},
 "S": {32: 94.93, 33: 0.76, 34: 4.29, 36: 0.02}, "Cl": {35: 75.78, 37: 24.22},
 "Ar": {36: 84.5946, 38: 15.3808, 40: 0.0246}, "K": {39: 93.132, 40: 0.147, 41: 6.721},
 "Ca": {40: 96.941, 42: 0.647, 43: 0.135, 44: 2.086, 46: 0.004, 48: 0.187},
 "Fe": {54: 5.845, 56: 91.754, 57: 2.119, 58: 0.282},
 "Zn": {64: 48.63, 66: 27.90, 67: 4.10, 68: 18.75, 70: 0.62},
}


def ame():
    m = {}
    for ln in open(AME, encoding="utf-8"):
        if ln.startswith("#") or ln.startswith("Z\t"):
            continue
        p = ln.rstrip("\n").split("\t")
        if len(p) < 7:
            continue
        Z, N, A = int(p[0]), int(p[1]), int(p[2])
        if A != Z + N:
            continue
        m[(p[3], A)] = A + float(p[4]) / KEV_PER_U
    return m


def comp(d, scale=1.0):
    x = {A: ((v[0] + v[1]) / 2 if isinstance(v, tuple) else v) / scale for A, v in d.items()}
    t = sum(x.values())
    return {A: v / t for A, v in x.items()}


def weight(el, d, M, scale=1.0):
    return sum(f * M[(el, A)] for A, f in comp(d, scale).items())


def main():
    import stock, stockgate
    M = ame()
    fails = 0
    out = []
    P = lambda *a: out.append(" ".join(str(x) for x in a))

    # ---------------- A
    P("A. tree value vs CIAAW 2024 standard atomic weight (READ)")
    tables = {"stockgate.py:314-328": stockgate.ATOMIC_MASS, "stock.py:206-209": stock.ATOMIC_MASS}
    for k in stock.ATOMIC_MASS:
        assert stock.ATOMIC_MASS[k] == stockgate.ATOMIC_MASS[k], k
    P("   stock.py's 18 values are identical to stockgate.py's for the same symbols: True")
    n_in = 0; flags = []
    for el, x in stockgate.ATOMIC_MASS.items():
        kind, a, b, abr = C24[el]
        if kind == "I":
            ok = (a <= x <= b) or x == abr      # the abridged (conventional) value is IUPAC's own
            if x == abr and not (a <= x <= b):
                P("   note: %s tree %s = CIAAW abridged conventional value, outside [%s, %s] by rounding only"
                  % (el, x, a, b))
        else:
            dec = len(repr(x).split(".")[1]) if "." in repr(x) else 0
            ok = abs(x - a) <= b + 0.5 * 10 ** (-dec) + 1e-12
        n_in += ok
        if not ok:
            fails += 1
        if x != abr and not (kind == "V" and abs(x - a) <= 0.5 * 10 ** (-len(repr(x).split('.')[1])) + 1e-12):
            flags.append((el, x, C24[el]))
    P("   entries consistent with the 2024 standard (in interval, or within U + tree rounding): %d / %d"
      % (n_in, len(stockgate.ATOMIC_MASS)))
    P("   entries that are neither the 2024 abridged value nor the 2024 value correctly rounded:")
    for el, x, c in flags:
        P("     %-2s tree %-8s 2024 %s  prior: %s" % (el, x, c, PRIOR_NOT_READ.get(el, "-")))

    # ---------------- B
    P("\nB. re-derivation: CIAAW 2024 isotopic composition (READ) x AME2020 masses (tree capture)")
    worst = 0.0
    for el, d in ISO24.items():
        w = weight(el, d, M)
        x = stock.ATOMIC_MASS[el]
        kind, a, b, abr = C24[el]
        tol = (b - a) if kind == "I" else max(b, 5e-4) * 3
        good = abs(w - x) <= max(tol, 1e-3)
        fails += (not good)
        worst = max(worst, abs(w - x) / x)
        P("   %-2s  sum x_i m_i = %.5f   tree %-7s  |d| = %.5f  %s" % (el, w, x, abs(w - x), "ok" if good else "FAIL"))
    P("   worst relative difference, re-derived vs tree: %.2e" % worst)

    # ---------------- C
    P("\nC. 'normal material' hypothesis: solar-system isotopes (A09 Table 3, READ) x AME2020")
    sol = {el: weight(el, d, M, 100.0) for el, d in A09T3.items()}
    for el in ("H", "He", "N", "Ne", "Ar", "K"):
        P("   %-2s solar-system weight %.5f  vs tree %-7s  relative %+.3e"
          % (el, sol[el], stockgate.ATOMIC_MASS[el], sol[el] / stockgate.ATOMIC_MASS[el] - 1))
    base = dict(stockgate.ATOMIC_MASS)
    alt24 = {el: C24[el][3] for el in base}
    altsol = dict(base); altsol.update(sol)

    def verdicts():
        v = {}
        for pk in stockgate.PAYLOADS:
            for dk in stockgate.DESTS:
                v[("binding", pk, dk)] = stockgate.binding_under(pk, dk)
        v["regimes"] = [(r[0], r[1], r[4]) for r in stockgate.volatility_regime()]
        v["Z_hybrid"] = stockgate.metallicity()
        v["condensed"] = stockgate.condensed_budget()
        ph = stockgate.solar("photospheric")
        v["XYZ_photospheric"] = (ph["H"], ph["He"], 1 - ph["H"] - ph["He"])
        v["stock_binding"] = stock.binding_element()
        v["stock_rank"] = [(r[0], r[1]) for r in stock.rank_destinations()]
        v["stock_rank_f"] = [r[2] for r in stock.rank_destinations()]
        v["Ar_massfrac"] = stockgate.solar_hybrid().get("Ar")
        with contextlib.redirect_stdout(io.StringIO()) as s:
            rc_g = stockgate.selftest()
        v["stockgate_selftest"] = rc_g
        with contextlib.redirect_stdout(io.StringIO()) as s2:
            rc_s = stock.selftest()
        v["stock_selftest"] = rc_s
        v["_st_g_fail_lines"] = [l for l in s.getvalue().splitlines() if "FAIL" in l]
        v["_st_s_fail_lines"] = [l for l in s2.getvalue().splitlines() if "FAIL" in l]
        return v

    def run(tab):
        for mod in (stockgate, stock):
            for el in list(mod.ATOMIC_MASS):
                mod.ATOMIC_MASS[el] = tab[el]
        try:
            return verdicts()
        finally:
            for mod in (stockgate, stock):
                for el in list(mod.ATOMIC_MASS):
                    mod.ATOMIC_MASS[el] = base[el]

    V0, V24, VS = run(base), run(alt24), run(altsol)
    P("   tree baseline selftests: stockgate rc=%s, stock rc=%s" % (V0["stockgate_selftest"], V0["stock_selftest"]))
    for name, V in (("CIAAW-2024 abridged", V24), ("solar-system isotopes", VS)):
        flips = [k for k in V0 if isinstance(k, tuple) and V0[k][0] != V[k][0]]
        rel = max(abs(V[k][1] / V0[k][1] - 1) for k in V0 if isinstance(k, tuple)
                  and V0[k][1] not in (0.0, float("inf")))
        P("   %-22s binder flips over %d (payload x destination) cells: %d ; max |rel. shift| of factor %.2e"
          % (name, sum(isinstance(k, tuple) for k in V0), len(flips), rel))
        P("   %-22s regimes equal: %s ; stock binding %s vs %s ; stock rank order equal: %s"
          % ("", V["regimes"] == V0["regimes"], V["stock_binding"], V0["stock_binding"],
             V["stock_rank"] == V0["stock_rank"]))
        P("   %-22s Z_hybrid %.6f vs %.6f ; XYZ_photospheric %s vs %s"
          % ("", V["Z_hybrid"], V0["Z_hybrid"], tuple(round(q, 5) for q in V["XYZ_photospheric"]),
             tuple(round(q, 5) for q in V0["XYZ_photospheric"])))
        P("   %-22s Ar mass fraction %.4e vs %.4e (rel %+.3f)" % ("", V["Ar_massfrac"], V0["Ar_massfrac"],
                                                             V["Ar_massfrac"] / V0["Ar_massfrac"] - 1))
        cd = max(abs(V["condensed"][k] / V0["condensed"][k] - 1) for k in V0["condensed"])
        P("   %-22s condensed budget max rel shift %.2e ; selftests under this table: stockgate rc=%s fails=%s, stock rc=%s fails=%s"
          % ("", cd, V["stockgate_selftest"], V["_st_g_fail_lines"], V["stock_selftest"], V["_st_s_fail_lines"]))
        fails += len(flips) + (V["regimes"] != V0["regimes"]) + (V["stock_binding"][0] != V0["stock_binding"][0])
    P("   A09 (arXiv:0909.0948 sec 3.12, READ) present-day photosphere X=0.7381 Y=0.2485 Z=0.0134;"
      " the tree's photospheric column gives %s" % (tuple(round(q, 4) for q in V0["XYZ_photospheric"]),))

    # ---------------- D
    P("\nD. massform H-A: A_e = round(stock.ATOMIC_MASS[e]); mean nucleon number within 1/2 (CIAAW 2024 compositions)")
    minmargin = 1.0
    for el in stock.HUMAN:
        abar = sum(A * f for A, f in comp(ISO24[el]).items())
        ae = round(stock.ATOMIC_MASS[el])
        margin = 0.5 - abs(abar - ae)
        minmargin = min(minmargin, margin)
        good = margin > 0
        fails += (not good)
        P("   %-2s A_e=%3d  Abar=%.4f  margin to 1/2: %.4f %s" % (el, ae, abar, margin, "ok" if good else "FAIL"))
    P("   smallest margin: %.4f" % minmargin)

    # ---------------- E
    P("\nE. interval elements flattened to one conventional value: verdicts at the interval ends")
    lo = {el: (C24[el][1] if C24[el][0] == "I" else C24[el][3]) for el in base}
    hi = {el: (C24[el][2] if C24[el][0] == "I" else C24[el][3]) for el in base}

    def light(tab):
        for mod in (stockgate, stock):
            for el in list(mod.ATOMIC_MASS):
                mod.ATOMIC_MASS[el] = tab[el]
        try:
            v = {(pk, dk): stockgate.binding_under(pk, dk) for pk in stockgate.PAYLOADS for dk in stockgate.DESTS}
            v["stock"] = stock.binding_element()
            v["rank"] = [(r[0], r[1]) for r in stock.rank_destinations()]
            return v
        finally:
            for mod in (stockgate, stock):
                for el in list(mod.ATOMIC_MASS):
                    mod.ATOMIC_MASS[el] = base[el]
    L0 = light(base)
    for name, tab in (("all interval elements at lower bound", lo), ("all at upper bound", hi)):
        L = light(tab)
        flips = [k for k in L0 if isinstance(k, tuple) and L0[k][0] != L[k][0]]
        rel = max(abs(L[k][1] / L0[k][1] - 1) for k in L0 if isinstance(k, tuple) and L0[k][1] not in (0.0, float("inf")))
        P("   %-38s binder flips %d ; stock binding %s ; rank equal %s ; max |rel. shift| %.2e"
          % (name, len(flips), L["stock"][0], L["rank"] == L0["rank"], rel))
        fails += len(flips) + (L["stock"][0] != L0["stock"][0])
    # H-A for Cl and Zn across the whole CIAAW composition interval / uncertainty
    cl_lo = 35 * 0.761 + 37 * 0.239; cl_hi = 35 * 0.755 + 37 * 0.245
    P("   Cl mean nucleon number over the CIAAW interval: [%.4f, %.4f]; |Abar - 35| < 1/2 throughout: %s"
      % (cl_lo, cl_hi, max(abs(cl_lo - 35), abs(cl_hi - 35)) < 0.5))
    fails += not (max(abs(cl_lo - 35), abs(cl_hi - 35)) < 0.5)

    print("\n".join(out))
    print("\nRESULT: %s (%d failures)" % ("PASS" if fails == 0 else "FAIL", fails))
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
