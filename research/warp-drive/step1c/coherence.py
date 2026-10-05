#!/usr/bin/env python3
"""
coherence.py -- Step 1c: H-COHERENCE priced -- how long each stored qubit must hold, against measured coherence times
READ at source.

Not seated.  M (rulings item 39): "3, then 2. Then 1 last please" -- 2 is this file.  coupling.py named H-COHERENCE
("no coherence time is priced anywhere else on the board"); here it is priced.

    python3 coherence.py              report
    python3 coherence.py --selftest   checks, with CONTROLS
    python3 coherence.py --json       the numbers as JSON

WHERE COHERENCE IS A DEMAND
  R-QUANTUM (balance.py's teleportation reading): Bob holds his half of each pair until Alice's two classical bits
  arrive.  With the pair source at the midpoint and Alice measuring on arrival (H-MIDPOINT-SOURCE, the arrangement that
  minimises the hold), Bob holds for L/c = 4.25 yr whatever the schedule.  The coupling route under H-LOCALITY is
  retarded and completes no sooner than L/c, so the same hold applies (coupling.py).
  R-CLASSICAL: only bits cross; a classical record does not dephase, so H-COHERENCE sets no demand there.
THE MODEL (named)
  H-PURE-DEPHASING with H-EXP-DECAY: a stored qubit's phase-flip probability after time t is p(t) = (1 - e^(-t/T2))/2.
  Without correction, all I qubits intact needs I p <= epsilon (H-NO-CORRECTION).  With correction at the dephasing
  channel's quantum capacity 1 - h2(p) (H-DEPHASING-CAPACITY, NAMED-NOT-READ: the standard degradable-channel result is
  not read at source here), the overhead is 1/(1 - h2(p)) and is finite only for p < 1/2.  H-NO-REFRESH: no active
  error correction or repeater refreshes the memory during the hold -- a fault-tolerant memory would change this, and
  whether one holds for years is OPEN.
THE SUPPLY (READ; see SUPPLY)
  The longest coherence times found, each with how it was obtained: an ensemble of 31P+ nuclear spins in 28Si, T2 = 180
  min at 1.2 K, measured single exponential, a lower bound limited by pulse errors (Saeedi et al. 2303.17734v1,
  re-read by the lead); an ensemble 151Eu3+ spin T2 = 2.68 h (Ma et al. 2012.14605v3); one 171Yb+ ion, 5487 s,
  EXTRAPOLATED from data to ~1000 s (Wang et al. 2008.00251v1); 151Eu3+ nuclear spins 370 min (Zhong et al. 2015,
  abstract only: Nature paywalled, method unknown); and the largest array, 6139 atoms held at once with T2 = 12.6 s
  (Manetsch et al. 2403.12021v4).  The reader's brief carried a wrong id (1301.6567 is Wolfowicz et al.; Saeedi et al.
  is 2303.17734v1), recorded.

NAMED HYPOTHESES
  H-MIDPOINT-SOURCE, H-PURE-DEPHASING, H-EXP-DECAY, H-NO-CORRECTION, H-DEPHASING-CAPACITY (NAMED-NOT-READ),
  H-NO-REFRESH, H-STATE-AS-BITS (one qubit per bit of the count), and demand.py's.
"""
import contextlib
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _sibling(name, fname):
    """A step1c owner, loaded by PATH under a private name: the board's root holds its own demand.py, supply.py and
    coupling.py, so a sibling is never imported by its bare name."""
    import importlib.util as _ilu
    key = "s1c_" + name
    if key in sys.modules:
        return sys.modules[key]
    spec = _ilu.spec_from_file_location(key, os.path.join(HERE, fname))
    mod = _ilu.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


with contextlib.redirect_stdout(io.StringIO()):
    coupling = _sibling("coupling", "coupling.py")
    demand = coupling.demand

L, C, YEAR_S = coupling.L, coupling.C, coupling.YEAR_S
T_HOLD = L / C

SUPPLY = {
    "P_in_28Si_Saeedi": {
        "source": "arXiv:2303.17734v1 (Saeedi et al.; Science 2013)", "route": "READ via alphaXiv answer_pdf_queries, "
        "p.3, Fig. 3 (coherence reader; re-read by the lead)", "kind": "measured single exponential; a lower bound "
        "(pulse errors)", "T2_s": 180 * 60.0, "qubits": "ensemble (~5e11 cm^-3), one stored state",
        "phrase": "follows a single exponential with a T2 of 180 min", "T_K": 1.2},
    "P_in_28Si_room": {
        "source": "arXiv:2303.17734v1", "route": "as above", "kind": "measured; a lower bound", "T2_s": 39 * 60.0,
        "qubits": "ensemble", "phrase": "a room temperature T2 decay of 39 min", "T_K": 298.0},
    "Eu_YSO_spin_Ma": {
        "source": "arXiv:2012.14605v3 (Ma et al.)", "route": "READ via alphaXiv answer_pdf_queries, Suppl. Note 3 "
        "(coherence reader)", "kind": "measured (Raman heterodyne, CPMG)", "T2_s": 2.68 * 3600.0,
        "qubits": "ensemble, one mode", "phrase": "2.68 +- 0.06 h", "T_K": 1.7},
    "Yb_ion_Wang": {
        "source": "arXiv:2008.00251v1 (Wang et al.)", "route": "READ via alphaXiv answer_pdf_queries, p.3, Fig. 3 "
        "(coherence reader)", "kind": "EXTRAPOLATED: exponential fit to Ramsey data up to ~16 min", "T2_s": 5487.0,
        "qubits": 1, "phrase": "have a coherence time of 5487 +- 667.6 s", "T_K": None},
    "Eu_YSO_Zhong": {
        "source": "Zhong et al., Nature 517, 177 (2015)", "route": "READ, abstract only, ANU research portal "
        "(coherence reader); full text paywalled, not routed around", "kind": "abstract only: measured or "
        "extrapolated not established", "T2_s": 370 * 60.0, "qubits": "ensemble",
        "phrase": "a coherence time of 370 +- 60 minutes was achieved at 2 kelvin", "T_K": 2.0},
    "Cs_array_Manetsch": {
        "source": "arXiv:2403.12021v4 (Manetsch et al.)", "route": "READ via alphaXiv answer_pdf_queries, p.5, "
        "Fig. 4c (coherence reader)", "kind": "measured, array-averaged", "T2_s": 12.6, "qubits": 6139,
        "phrase": "the measured dephasing time is T2 = 12.6(1) s", "T_K": None},
}


def h2(p):
    return 0.0 if p <= 0 or p >= 1 else -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def p_dephase(t, T2):
    """H-PURE-DEPHASING, H-EXP-DECAY."""
    return 0.5 * (1.0 - math.exp(-t / T2))


def capacity(p):
    """H-DEPHASING-CAPACITY (NAMED-NOT-READ): 1 - h2(p), floored at 0."""
    return max(0.0, 1.0 - h2(p))


def T2_for_p(t, p):
    """The T2 that gives phase-flip probability p after t."""
    return t / -math.log1p(-2.0 * p)       # log1p: 1 - 2p rounds to 1 at p ~ 1e-28


def qubits():
    return dict((n, b) for n, b in demand.counts())


def demand_T2():
    """T2 needed for the hold: with correction at p = 0.11 (capacity ~1/2, overhead ~2x), and with none for I qubits
    (expected one flip over all I: I p = 1)."""
    out = {"with_correction_p": 0.11, "with_correction_T2_s": T2_for_p(T_HOLD, 0.11),
           "with_correction_capacity": capacity(0.11)}
    out["no_correction_T2_s"] = dict((n, T2_for_p(T_HOLD, 1.0 / b)) for n, b in qubits().items())
    return out


def supply_rows():
    out = {}
    for k, v in SUPPLY.items():
        p = p_dephase(T_HOLD, v["T2_s"])
        out[k] = {"T2_s": v["T2_s"], "e_folds_in_hold": T_HOLD / v["T2_s"], "p_after_hold": p,
                  "capacity_after_hold": capacity(p), "kind": v["kind"]}
    return out


def collect():
    return {"T_hold_s": T_HOLD, "T_hold_yr": T_HOLD / YEAR_S, "demand": demand_T2(), "supply": supply_rows(),
            "READ": SUPPLY}


def report():
    d = collect()
    dm = d["demand"]
    print("Step 1c -- H-COHERENCE priced (R-QUANTUM and the retarded coupling; R-CLASSICAL sets no coherence demand)")
    print("  hold: L/c = %.4g s = %.4g yr (H-MIDPOINT-SOURCE)" % (d["T_hold_s"], d["T_hold_yr"]))
    print("  demand: with correction at p = 0.11 (capacity %.3f): T2 >= %.3g s = %.3g yr; with none, T2 >= %s"
          % (dm["with_correction_capacity"], dm["with_correction_T2_s"], dm["with_correction_T2_s"] / YEAR_S,
             "; ".join("%.3g s (%s)" % (v, n[:16]) for n, v in dm["no_correction_T2_s"].items())))
    print("  supply (READ):")
    best = max(v["T2_s"] for k, v in d["supply"].items() if not SUPPLY[k]["kind"].startswith(("EXTRAP", "abstract")))
    for k, v in d["supply"].items():
        print("    %-20s T2 %.4g s (%s): %.3g e-folds in the hold; p -> %.6f; capacity %.3g"
              % (k, v["T2_s"], SUPPLY[k]["kind"][:40], v["e_folds_in_hold"], v["p_after_hold"],
                 v["capacity_after_hold"]))
    print("  best measured (not extrapolated, not abstract-only): %.4g s -- %.3g short of the corrected demand; %.3g "
          "short of the uncorrected one (species)" % (best, dm["with_correction_T2_s"] / best,
                                                    list(dm["no_correction_T2_s"].values())[0] / best))
    print("  under H-NO-REFRESH no measured memory holds a qubit through the hold: every capacity above is 0.  A "
          "fault-tolerant memory that holds for years is OPEN.")


def selftest():
    n_ok = n_bad = n_ctl = 0

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-96s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:96], got))

    print("coherence.py selftest")
    d = collect()
    sp = d["supply"]
    chk("every READ memory, held for L/c, reaches p = 1/2 to within 1e-12 and capacity 0 (H-NO-REFRESH)",
        [k for k, v in sp.items() if abs(v["p_after_hold"] - 0.5) > 1e-12 or v["capacity_after_hold"] > 0], [])
    chk("  CONTROL: a memory with T2 = 10 L/c keeps p under 0.05 and capacity over 0.7",
        (p_dephase(T_HOLD, 10 * T_HOLD) < 0.05, capacity(p_dephase(T_HOLD, 10 * T_HOLD)) > 0.7), (True, True),
        ctl=True)
    dm = d["demand"]
    chk("with correction at p = 0.11 the hold needs T2 between 4 and 4.1 L/c (%.4g L/c), capacity about 1/2 (%.3f)"
        % (dm["with_correction_T2_s"] / T_HOLD, dm["with_correction_capacity"]),
        (4.0 < dm["with_correction_T2_s"] / T_HOLD < 4.1, 0.45 < dm["with_correction_capacity"] < 0.55),
        (True, True))
    best = SUPPLY["P_in_28Si_Saeedi"]["T2_s"]
    chk("the best measured T2 (180 min, a lower bound) is over 1e4 short of the corrected demand (%.3g)"
        % (dm["with_correction_T2_s"] / best), dm["with_correction_T2_s"] / best > 1e4, True)
    nc = list(dm["no_correction_T2_s"].values())[0]
    chk("without correction, all 9.5e27 qubits intact needs T2 over 1e35 s (%.3g s)" % nc, nc > 1e35, True)
    chk("the largest simultaneous array (6139 atoms, T2 = 12.6 s) is short of the corrected demand by over 1e7 (%.3g)"
        % (dm["with_correction_T2_s"] / SUPPLY["Cs_array_Manetsch"]["T2_s"]),
        dm["with_correction_T2_s"] / SUPPLY["Cs_array_Manetsch"]["T2_s"] > 1e7, True)
    chk("every READ record names a source, route and kind; phrases under 15 words; extrapolated and abstract-only "
        "figures are marked as such",
        ([k for k, v in SUPPLY.items() if not all(v.get(f) for f in ("source", "route", "kind"))],
         [k for k, v in SUPPLY.items() if len(v["phrase"].split()) >= 15],
         SUPPLY["Yb_ion_Wang"]["kind"].startswith("EXTRAPOLATED"),
         SUPPLY["Eu_YSO_Zhong"]["kind"].startswith("abstract only")), ([], [], True, True))
    print("  [STRUCTURAL] p(t) = (1 - e^(-t/T2))/2 and T2_for_p are inverses (H-PURE-DEPHASING, H-EXP-DECAY)")
    print("  [STRUCTURAL] the hold L/c is the light time: R-QUANTUM's two bits travel at c (H-MIDPOINT-SOURCE)")
    print("\n%d/%d checks pass, %d of them controls; 2 STRUCTURAL printed, not counted" % (n_ok, n_ok + n_bad, n_ctl))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
