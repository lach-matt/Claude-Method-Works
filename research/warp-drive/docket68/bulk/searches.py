#!/usr/bin/env python3
"""
searches.py -- the other routes to observing a second plane, READ at source and set against the board's two-plane
parameters (bulk.py, pairing.py).

Not seated; not yet verified.  M (rulings item 63): "read those now please. They are relevant" -- the collider and
short-range gravity searches that item 62 had left NAMED-NOT-READ.  Carried BESIDE M's H-UNOBSERVED-UNBUILT (item 62:
no two-plane geometry is observed because no device that allows the travel has been designed), never against it:
these searches look for a bulk WITHOUT travelling through it, and a null result in a searched range says nothing
outside that range.

    python3 searches.py              report
    python3 searches.py --selftest   checks, with CONTROLS
    python3 searches.py --json       the numbers as JSON

SOURCES (READ 2026-10-05 via alphaXiv, open arXiv copies; page numbers are the printed pages).  NOTE: the text layer of
the ATLAS paper drops decimal points ('144' for 1.44, '329 sigma' for 3.29 sigma); each such value is read from its
context and cross-checked where a second source prints it (the width law, below).

  ATLAS, arXiv:2102.13405v3 (Phys. Lett. B 822 (2021) 136651).  Diphoton, 139 fb^-1 at 13 TeV.  RS1 graviton (the
    lightest KK excitation) searched for k/M_Pl-bar = 0.01-0.1, m_G = 500-2800 GeV, limits extended to 5000 GeV (p.8).
    'The RS1 model is excluded for m_G below 2.2, 3.9 and 4.5 TeV for k/M_Pl-bar values of 0.01, 0.05 and 0.1' (p.9).
    Width Gamma = 1.44 (k/M_Pl-bar)^2 m_G (p.2).  'No significant deviation from the Standard Model is observed'
    (abstract); the largest excess, ~684 GeV, local 3.29 sigma, global 1.30-1.36 sigma (p.8).
  CMS, arXiv:2103.02708v2 (JHEP 07 (2021) 208).  Dileptons, 137 (ee) / 140 (mumu) fb^-1 at 13 TeV.  RS graviton samples
    generated at 250-4000 GeV (p.7); the limits reach 4.78 TeV.  Widths 0.01 %, 0.36 %, 1.42 % at k/M_Pl-bar = 0.01, 0.05, 0.10 (p.4).  Observed lower limits,
    ee + mumu: 2.47, 4.16, 4.78 TeV (Table 6, p.22).  ADD: Lambda_T (GRW) > 7.5 TeV combined; M_S 5.9-8.9 TeV by
    convention (pp.25, 28).  'No significant deviation is observed' (abstract).
  Davoudiasl, Hewett & Rizzo, hep-ph/9909255v1.  KK graviton masses m_n = k x_n e^{-k r_c pi}, x_n the roots of J_1
    (p.5); massive modes couple at 1/Lambda_pi with Lambda_pi = e^{-k r_c pi} M_Pl-bar (p.5); they take k/M_Pl-bar <= 1,
    string and curvature arguments favouring ~1e-2 (p.6, eq. 12); the narrow-width approximation 'is strictly valid
    only for values of k/M_Pl-bar <~ 0.3' (p.7); as k/M_Pl-bar grows 'the peaks become too wide to be identified as true
    resonances' and the tower looks like a contact interaction (p.9).
  Kapner et al., hep-ph/0611184v1 (PRL 98 021101).  Torsion balance, 55 um - 9.53 mm.  |alpha| = 1 Yukawa excluded for
    lambda > 56 um; 'an extra dimension must have a size R <= 44 um' (abstract, p.4).
  Lee, Adelberger, Cook, Fleischer & Heckel, arXiv:2002.11761v1.  Torsion balance, 52 um - 3.0 mm.  'Newtonian gravity
    gave an excellent fit' (abstract; chi^2 = 275.0 for nu = 285, p.4); gravitational-strength Yukawas need lambda < 38.6
    um, and 'the largest extra dimension must have a toroidal radius less than 30 um' (p.5).

WHAT IS COMPUTED
  (A) bulk.py's Randall-Sundrum point (k = 2e18 GeV, warp 1e15, asked of bulk.py) in the searches' own variables:
      k/M_Pl-bar (M_Pl-bar from G and hbar, asked of the board's constants), m_1 = x_1 k e^{-k pi r_c}, the width by
      ATLAS's law.  Whether a search covers that point is decided from the READ ranges, never assumed.
  (B) What the limits bound: at each searched coupling, m_1 >= m_lim gives k e^{-k pi r_c} >= m_lim / x_1, hence an
      UPPER bound on bulk.py's jump on our clock (hbar / (k e^{-k pi r_c}) = x_1 hbar / m_1) and on the warp.
  (C) The torsion-balance bound against the board's 1 mm gaps (bulk.MANYFOLD_GAP_M, bulk.CF['L_illustrative_m']): in a
      FLAT toroidal bulk of radius R the farthest two points are pi R apart (H-TORUS-BULK), so R < 30 um caps a gap at
      94 um.  A WARPED bulk is not bounded this way: RS1's 1/k is ~1e-34 m; pairing.py's Chung-Freese design 1/k values
      fall inside the 52 um - 3 mm span the balances tested, and whether CF's bulk alters brane gravity there is OPEN.

NAMED HYPOTHESES
  H-TORUS-BULK (the flat bulk is a torus, as Lee's bound is stated), H-CMS-RANGE (CMS's searched masses taken from its
  lowest generated sample, 250 GeV, to its highest READ limit, 4.78 TeV -- the search range is not printed as such),
  H-WIDTH-LAW (ATLAS's width law used outside the
  searched couplings, where DHR say the narrow-width approximation fails), with bulk.py's H-RS1, H-K-PLANCK, H-L-ILLUSTRATIVE,
  pairing.py's H-CF-STATIC, and M's H-UNOBSERVED-UNBUILT, H-HIGHER-CORRIDOR.
"""
import contextlib
import importlib.util
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _by_path(key, path):
    if key in sys.modules:
        return sys.modules[key]
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


with contextlib.redirect_stdout(io.StringIO()):
    bulk = _by_path("bulk_bulk", os.path.join(HERE, "bulk.py"))
    pairing = _by_path("bulk_pairing", os.path.join(HERE, "pairing.py"))

higgs = bulk.branelink.higgs
C = bulk.C
HBARC_GEV_M = bulk.HBARC_GEV_M

# READ values (see the docstring for page numbers).  Masses in GeV.
ATLAS = {"limits": {0.01: 2200.0, 0.05: 3900.0, 0.1: 4500.0}, "width_coeff": 1.44,
         "k_range": (0.01, 0.1), "m_range": (500.0, 5000.0)}
CMS = {"limits": {0.01: 2470.0, 0.05: 4160.0, 0.1: 4780.0}, "widths_pct": {0.01: 0.01, 0.05: 0.36, 0.1: 1.42},
       "k_range": (0.01, 0.1), "m_range": (250.0, 4780.0)}   # H-CMS-RANGE: lowest generated sample to highest limit
DHR = {"narrow_width_max": 0.3}
TORSION = {"kapner_R_m": 44e-6, "lee_R_m": 30e-6, "lee_lambda_m": 38.6e-6, "lee_span_m": (52e-6, 3.0e-3),
           "kapner_span_m": (55e-6, 9.53e-3)}


def m_pl_bar_gev():
    """The reduced Planck mass sqrt(hbar c / 8 pi G) c^2, from the board's G and hbar (higgs.py's constants)."""
    return math.sqrt(higgs.HBAR_C * C ** 4 / (8 * math.pi * higgs.G)) / higgs.GEV_IN_J


def bessel_j(nu, x, terms=60):
    return sum((-1) ** m * (x / 2) ** (2 * m + nu) / (math.factorial(m) * math.factorial(m + nu)) for m in range(terms))


def first_root(nu, lo, hi):
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if bessel_j(nu, lo) * bessel_j(nu, mid) <= 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def bessel_j_integral(n, x, steps=4000):
    """Bessel's integral J_n(x) = (1/pi) int_0^pi cos(n tau - x sin tau) d tau (Simpson) -- shares nothing with the
    series in bessel_j, so a root found by one and confirmed by the other is not a self-consistency check."""
    h = math.pi / steps
    acc = sum((1 if i in (0, steps) else (4 if i % 2 else 2)) * math.cos(n * i * h - x * math.sin(i * h))
              for i in range(steps + 1))
    return acc * h / 3 / math.pi


X1 = first_root(1, 3.0, 4.5)


def covered(search, k_over_mpl, m1):
    """IN-RANGE when the point lies inside the search's READ coupling and mass ranges; otherwise which range it leaves."""
    out = []
    if not (search["k_range"][0] <= k_over_mpl <= search["k_range"][1]):
        out.append("coupling outside %.2f-%.2f" % search["k_range"])
    if not (search["m_range"][0] <= m1 <= search["m_range"][1]):
        out.append("mass outside %.0f-%.0f GeV" % search["m_range"])
    return "IN-RANGE" if not out else "; ".join(out)


def verdict(search, k_over_mpl, m1):
    """EXCLUDED / ALLOWED only for a point inside a READ coupling; NOT-TESTED otherwise."""
    if k_over_mpl not in search["limits"]:
        return "NOT-TESTED (coupling not a READ limit)"
    if not (search["m_range"][0] <= m1 <= search["m_range"][1]):
        return "NOT-TESTED (mass outside the searched range)"
    return "EXCLUDED" if m1 < search["limits"][k_over_mpl] else "ALLOWED"


def point(k_gev, warp):
    mpl = m_pl_bar_gev()
    kvis = k_gev / warp
    m1 = X1 * kvis
    kr = k_gev / mpl
    return {"k_over_mpl": kr, "k_vis_GeV": kvis, "m1_GeV": m1, "Lambda_pi_GeV": kvis / kr,
            "width_frac_atlas_law": ATLAS["width_coeff"] * kr ** 2, "jump_ours_s": HBARC_GEV_M / kvis / C}


def compute():
    mpl = m_pl_bar_gev()
    board = point(bulk.RS["k_GeV"], bulk.RS["warp"])
    board["atlas"] = covered(ATLAS, board["k_over_mpl"], board["m1_GeV"])
    board["cms"] = covered(CMS, board["k_over_mpl"], board["m1_GeV"])
    bounds = []
    for kr in sorted(CMS["limits"]):
        for name, s in (("ATLAS", ATLAS), ("CMS", CMS)):
            mlim = s["limits"][kr]
            kvis_min = mlim / X1
            bounds.append({"search": name, "k_over_mpl": kr, "m1_min_GeV": mlim, "k_vis_min_GeV": kvis_min,
                           "jump_ours_max_s": HBARC_GEV_M / kvis_min / C, "warp_max": kr * mpl / kvis_min,
                           "Lambda_pi_min_GeV": kvis_min / kr})
    at_warp15 = []
    for kr in sorted(CMS["limits"]):
        p = point(kr * mpl, 1e15)
        at_warp15.append({"k_over_mpl": kr, "m1_GeV": p["m1_GeV"], "ATLAS": verdict(ATLAS, kr, p["m1_GeV"]),
                          "CMS": verdict(CMS, kr, p["m1_GeV"])})
    gap_max = {n: math.pi * TORSION[n] for n in ("lee_R_m", "kapner_R_m")}
    designs = [{"T_s": d["T_s"], "kL": d["kL_needed"], "inv_k_m": 1.0 / d["k_per_m"]} for d in pairing.compute()["designs"]]
    span = TORSION["lee_span_m"]
    for d in designs:
        d["inside_lee_span"] = span[0] <= d["inv_k_m"] <= span[1]
    rs_inv_k = HBARC_GEV_M / bulk.RS["k_GeV"]
    return {"M_pl_bar_GeV": mpl, "x1": X1, "board_rs": board, "bounds": bounds, "at_warp_1e15": at_warp15,
            "flat_gap_max_m": gap_max, "board_gaps_m": {"manyfold": bulk.MANYFOLD_GAP_M,
                                                        "cf_L": bulk.CF["L_illustrative_m"]},
            "flat_gap_crossing_max_s": gap_max["lee_R_m"] / C, "cf_designs": designs, "rs_inv_k_m": rs_inv_k}


def report():
    d = compute()
    b = d["board_rs"]
    print("searches.py -- the collider and short-range gravity searches, READ, against the board's two planes")
    print("  M_Pl-bar = %.4e GeV (from G, hbar); x_1 = %.6f (first zero of J_1)" % (d["M_pl_bar_GeV"], d["x1"]))
    print("\n(A) bulk.py's Randall-Sundrum point: k/M_Pl-bar = %.3f, k e^{-k pi r_c} = %.0f GeV, m_1 = %.2f TeV, "
          "width (ATLAS law, H-WIDTH-LAW) = %.0f %% of m_1" % (b["k_over_mpl"], b["k_vis_GeV"], b["m1_GeV"] / 1e3,
                                                              100 * b["width_frac_atlas_law"]))
    print("    ATLAS: %s\n    CMS:   %s" % (b["atlas"], b["cms"]))
    print("    -> NOT TESTED by either resonance search; at this coupling DHR say the tower is no longer resonances")
    print("\n(B) what the limits bound, at the searched couplings:")
    for r in d["bounds"]:
        print("    %-5s k/M = %.2f: m_1 >= %.2f TeV -> Lambda_pi >= %5.1f TeV, warp <= %.2e, jump on our clock <= %.2e s"
              % (r["search"], r["k_over_mpl"], r["m1_min_GeV"] / 1e3, r["Lambda_pi_min_GeV"] / 1e3, r["warp_max"],
                 r["jump_ours_max_s"]))
    print("    with the warp held at 1e15 (RS's own TeV hierarchy):")
    for r in d["at_warp_1e15"]:
        print("      k/M = %.2f: m_1 = %7.1f GeV  ATLAS %s; CMS %s" % (r["k_over_mpl"], r["m1_GeV"], r["ATLAS"], r["CMS"]))
    print("\n(C) torsion balances: a flat toroidal bulk (H-TORUS-BULK) caps a gap at pi R = %.1f um (Lee, R < 30 um), "
          "%.1f um (Kapner, R <= 44 um); the board's illustrative gaps are %.0f um" % (
              1e6 * d["flat_gap_max_m"]["lee_R_m"], 1e6 * d["flat_gap_max_m"]["kapner_R_m"],
              1e6 * d["board_gaps_m"]["manyfold"]))
    print("    a capped gap reads at most %.2e s on our clock" % d["flat_gap_crossing_max_s"])
    print("    RS1's 1/k = %.2e m: far below any balance.  pairing.py's Chung-Freese designs:" % d["rs_inv_k_m"])
    for r in d["cf_designs"]:
        print("      T = %9.0f s: kL = %5.2f, 1/k = %6.1f um  (inside the 52 um - 3 mm span tested: %s)" % (
            r["T_s"], r["kL"], 1e6 * r["inv_k_m"], r["inside_lee_span"]))


def selftest():
    n_pass = n_fail = n_ctl = 0
    structural = []

    def chk(label, ok, ctl=False):
        nonlocal n_pass, n_fail, n_ctl
        n_ctl += ctl
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else "", label))

    d = compute()
    # 1. two collaborations, one law: ATLAS's printed width coefficient reproduces CMS's printed widths
    pred = {k: 100 * ATLAS["width_coeff"] * k * k for k in CMS["widths_pct"]}
    chk("ATLAS's width law 1.44 (k/M)^2 reproduces CMS's printed widths %s %% within their rounding: %s" % (
        CMS["widths_pct"], {k: round(v, 3) for k, v in pred.items()}),
        all(abs(pred[k] - CMS["widths_pct"][k]) <= max(0.005, 0.02 * CMS["widths_pct"][k]) for k in pred))
    # 2. the first J_1 zero by the series root-finder, confirmed by Bessel's integral (an independent representation)
    j_at = bessel_j_integral(1, X1)
    chk("x_1 = %.6f found from the series is a zero of J_1 by Bessel's integral too (J_1(x_1) = %.1e)" % (X1, j_at),
        abs(j_at) < 1e-9)
    j_off = bessel_j_integral(1, X1 + 0.05)
    chk("Bessel's integral is not zero 0.05 away from x_1 (J_1 = %.2e), so the check above can fail" % j_off,
        abs(j_off) > 1e-3, ctl=True)
    # 3. the coverage verdicts reach every outcome: bulk.py's point is untested, a warp-1e15 point at 0.1 is excluded,
    #    a point above the limit inside the range is allowed
    b = d["board_rs"]
    v_board = verdict(CMS, b["k_over_mpl"], b["m1_GeV"])
    v_ex = verdict(ATLAS, 0.1, point(0.1 * d["M_pl_bar_GeV"], 1e15)["m1_GeV"])
    v_ok = verdict(ATLAS, 0.1, 4900.0)
    chk("the coverage verdict reaches all three outcomes: bulk.py's point %s; warp 1e15 at k/M = 0.1 %s; m_1 = 4.9 TeV at "
        "0.1 %s" % (v_board, v_ex, v_ok),
        v_board.startswith("NOT-TESTED") and v_ex == "EXCLUDED" and v_ok == "ALLOWED")
    chk("M_Pl-bar from the board's G and hbar is 2.435e18 GeV to 0.1 %% (%.4e)" % d["M_pl_bar_GeV"],
        abs(d["M_pl_bar_GeV"] / 2.435e18 - 1) < 1e-3, ctl=True)
    structural.append("the jump bound in (B) is bulk.py's jump read through the KK spectrum (hbar / k e^{-k pi r_c} = "
                      "x_1 hbar / m_1): arithmetic on READ limits, not a measurement of a jump")
    structural.append("a flat toroidal bulk's farthest points are pi R apart (H-TORUS-BULK), so R < 30 um caps a gap at "
                      "94 um; the board's 1 mm gaps are illustrative (H-L-ILLUSTRATIVE) and sit outside that cap")
    structural.append("every search READ here looks for a bulk without travelling through it; each reports no "
                      "significant deviation inside its searched range, which neither tests nor refutes "
                      "H-UNOBSERVED-UNBUILT")
    for s in structural:
        print("  STRUCTURAL: " + s)
    print("searches.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
