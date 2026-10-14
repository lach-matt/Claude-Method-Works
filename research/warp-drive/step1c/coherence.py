#!/usr/bin/env python3
"""
coherence.py -- Step 1c: H-COHERENCE priced -- how long a stored qubit must hold, in which arrangement, against measured
coherence times READ at source.

Not seated.  M (rulings item 39): "3, then 2. Then 1 last please" -- 2 is this file.  coupling.py named H-COHERENCE;
here it is priced.  Verified in both directions on 2026-10-05; the findings are applied and the first-written claims
kept under HISTORY.

    python3 coherence.py              report
    python3 coherence.py --selftest   checks, with CONTROLS
    python3 coherence.py --json       the numbers as JSON

WHERE COHERENCE IS A DEMAND -- IT DEPENDS ON THE ARRANGEMENT AND THE PAYLOAD
  R-QUANTUM (balance.py's teleportation reading), source of pairs a distance x from Alice along the A-B line: Bob's half
  arrives at (L - x)/c; Alice measures on arrival of hers at x/c; her two bits reach Bob at (x + L)/c.  Bob's STORED
  hold is 2x/c (H-STORED-HOLD: the hold is on a stored memory).  x = 0 (source at Alice): 0 -- Bob's half is in FLIGHT
  for L/c instead, and a photon in vacuum has no dephasing environment (H-VACUUM-FLIGHT: dispersion and Faraday
  rotation are unitary and calibratable), so the burden moves to LOSS, which is the link budget's (supply.py's
  link_at_proxima).  x = L/2 (H-MIDPOINT-SOURCE): L/c.  x = L: 2L/c.
  And under H-STATE-AS-BITS (the payload is the object's bits) Bob measures in the computational basis only: he can
  measure on arrival and apply the X correction to the recorded outcome when Alice's bits come (Z does not change a
  computational-basis result) -- a hold of 0 at any x.  So a stored hold is a demand only for a QUANTUM payload with
  the source away from Alice.
  The retarded coupling route: the state must stay coherent for the whole interaction, about pi/(2J); at the far-field
  J (coupling.py) that is far beyond L/c -- L/c is only its floor.
  R-CLASSICAL: only bits cross; dephasing sets no demand.  If bits are stored, retention errors are classical error-rate
  costs, correctable without a capacity cliff (H-CLASSICAL-RETENTION).
THE MODEL (named)
  H-PURE-DEPHASING with H-EXP-DECAY: phase-flip probability after t is p(t) = (1 - e^(-t/T2))/2.  Bias: for t >> T2 a
  stretched exponential (n > 1, spectral diffusion) decays faster, so the pure exponential is LENIENT to the memory;
  T1 is ignored.  At 6e3 e-folds or more p saturates under any of these.
  Correction: the dephasing channel is degradable, so its quantum capacity is its single-letter coherent information
  (Devetak & Shor, quant-ph/0311131v3 p.13 App. B, READ by the coherence verifier); the closed form 1 - h2(p) for
  phase-flip probability p is COMPUTED here (H-DEPHASING-CAPACITY), for an asymptotic block code with ideal encode and
  decode, compatible with H-NO-REFRESH.  An overhead k (encoded qubits per logical qubit) needs capacity 1/k.  The
  demand is printed as a function of k, which multiplies the number of memories too.
  H-NO-REFRESH: no active error correction refreshes the memory during the hold.  Active fault-tolerant correction
  below threshold gives logical lifetimes growing exponentially with code distance, so years are not excluded in
  principle; the open question is an operations and energy demand on 9.5e27 x k physical qubits (H-FT-MEMORY, OPEN,
  unpriced).  Every supply T2 below is already measured under active dynamical decoupling, which is control, not
  correction.
THE SUPPLY (READ; see SUPPLY)
  31P+ ensemble in 28Si, T2 = 180 min at 1.2 K, measured single exponential, a lower bound (pulse errors) -- Saeedi et
  al. 2303.17734v1, re-read by the lead; 151Eu3+ spin T2 = 2.68 h (Ma et al. 2012.14605v3); one 171Yb+ ion 5487 s,
  EXTRAPOLATED (Wang et al. 2008.00251v1); 151Eu3+ 370 min, abstract only (Zhong et al. 2015, paywalled); 6139 atoms at
  once, T2 = 12.6 s under XY16 at reduced trap depth (3.19 s at full depth; Manetsch et al. 2403.12021v4, spot-checked
  by the verifier).  An ensemble stores ONE state in many spins: the spins per stored qubit are unpriced
  (H-ENSEMBLE-PER-QUBIT), which favours the device.

NAMED HYPOTHESES
  H-STORED-HOLD, H-MIDPOINT-SOURCE (a modelling choice, not the minimum), H-VACUUM-FLIGHT, H-PURE-DEPHASING,
  H-EXP-DECAY, H-DEPHASING-CAPACITY (degradability READ, closed form COMPUTED), H-NO-REFRESH, H-FT-MEMORY (OPEN),
  H-ENSEMBLE-PER-QUBIT, H-CLASSICAL-RETENTION, H-STATE-AS-BITS, and demand.py's.

HISTORY (coherence verifier, 2026-10-05; first-written claims kept):
  * 'H-MIDPOINT-SOURCE, the arrangement that minimises the hold' -- wrong: the hold is 2x/c, 0 with the source at
    Alice; and 0 at any x for a bit payload.  The midpoint hold L/c is a modelling choice, not the minimum (it was
    printed STRUCTURAL as 'the light time'; demoted).
  * 'The retarded coupling route has the same hold' -- understated: L/c is its floor; the interaction time is longer.
  * '5.0e4 short' rested on p = 0.11 (overhead 2) alone; now a function of the overhead (1.8e3 at 1e6, ~4e2 at 1e27).
  * H-DEPHASING-CAPACITY was NAMED-NOT-READ; degradability is now READ (Devetak & Shor), the closed form COMPUTED.
  * Counted as checks: 'T2 between 4 and 4.1 L/c' and 'capacity about 1/2' -- functions of the constant 0.11 only;
    moved to STRUCTURAL.  The control recomputed p analytically and never exercised check 1's predicate; it now injects
    a supply row.
  * '1.24e4 e-folds short of the hold' -- mis-worded: the hold spans 1.24e4 e-folds of T2.
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
OVERHEADS = (2.0, 1e6, 1e12, 1e27, 1e100)

SUPPLY = {
    "P_in_28Si_Saeedi": {
        "source": "arXiv:2303.17734v1 (Saeedi et al.; Science 2013)", "route": "READ via alphaXiv answer_pdf_queries, "
        "p.3, Fig. 3 (coherence reader; re-read by the lead)", "kind": "measured single exponential; a lower bound "
        "(pulse errors)", "T2_s": 180 * 60.0, "qubits": "ensemble (density ~5e11 cm^-3), one stored state",
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
        "Fig. 4c (coherence reader; spot-checked by the verifier)", "kind": "measured, array-averaged, under XY16 "
        "dynamical decoupling at reduced trap depth (3.19 s at full depth)", "T2_s": 12.6, "qubits": 6139,
        "phrase": "the measured dephasing time is T2 = 12.6(1) s", "T_K": None},
}


def stored_hold(x):
    """Bob's stored hold, source at distance x from Alice (H-STORED-HOLD): 2x/c."""
    return 2.0 * x / C


def T_HOLD_MIDPOINT():
    return stored_hold(L / 2.0)


def h2(p):
    return 0.0 if p <= 0 or p >= 1 else -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def p_dephase(t, T2):
    """H-PURE-DEPHASING, H-EXP-DECAY."""
    return 0.5 * (1.0 - math.exp(-t / T2))


def capacity(p):
    """H-DEPHASING-CAPACITY: 1 - h2(p) (computed; degradability READ), floored at 0."""
    return max(0.0, 1.0 - h2(p))


def T2_for_p(t, p):
    """The T2 that gives phase-flip probability p after t."""
    return t / -math.log1p(-2.0 * p)       # log1p: 1 - 2p rounds to 1 at p ~ 1e-28


def p_for_overhead(k):
    """The phase-flip probability at which capacity is 1/k: bisection on 1 - h2(p) = 1/k over (0, 1/2); for large k
    the analytic form near p = 1/2, 1 - h2(1/2 - eps) ~ (2/ln 2) eps^2, so eps = sqrt(ln 2 / (2 k))."""
    eps = math.sqrt(math.log(2.0) / (2.0 * k))
    if eps < 1e-6:
        return 0.5 - eps, eps
    lo, hi = 0.0, 0.5
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if 1.0 - h2(mid) > 1.0 / k:
            lo = mid
        else:
            hi = mid
    return lo, 0.5 - lo


def T2_for_overhead(t, k):
    """T2 needed for a hold t at overhead k: e^(-t/T2) = 1 - 2p = 2 eps."""
    _p, eps = p_for_overhead(k)
    return t / math.log(1.0 / (2.0 * eps))


def qubits():
    return dict((n, b) for n, b in demand.counts())


def demand_T2():
    t = T_HOLD_MIDPOINT()
    out = {"hold_by_source": {"x = 0 (source at Alice)": stored_hold(0.0), "x = L/2 (midpoint)": stored_hold(L / 2),
                              "x = L (source at Bob)": stored_hold(L)},
           "coupling_interaction_s": math.pi / (2.0 * coupling.supply_rows()["rydberg_J_far_at_L_rad_s"]),
           "by_overhead_T2_s": dict((k, T2_for_overhead(t, k)) for k in OVERHEADS)}
    out["no_correction_T2_s"] = dict((n, T2_for_p(t, 1.0 / b)) for n, b in qubits().items())
    return out


def supply_rows(supply=None):
    t = T_HOLD_MIDPOINT()
    out = {}
    for k, v in (SUPPLY if supply is None else supply).items():
        p = p_dephase(t, v["T2_s"])
        out[k] = {"T2_s": v["T2_s"], "hold_in_T2_e_folds": t / v["T2_s"], "p_after_hold": p,
                  "capacity_after_hold": capacity(p), "kind": v["kind"]}
    return out


def saturated(rows):
    """[memory] that reaches p = 1/2 and capacity 0 over the midpoint hold (check 1's predicate)."""
    return [k for k, v in rows.items() if abs(v["p_after_hold"] - 0.5) <= 1e-12 and v["capacity_after_hold"] == 0]


def best_measured():
    return max(v["T2_s"] for v in SUPPLY.values() if not v["kind"].startswith(("EXTRAP", "abstract")))


def collect():
    return {"T_hold_midpoint_s": T_HOLD_MIDPOINT(), "demand": demand_T2(), "supply": supply_rows(), "READ": SUPPLY,
            "shortfall_by_overhead": dict((k, v / best_measured())
                                          for k, v in demand_T2()["by_overhead_T2_s"].items())}


def report():
    d = collect()
    dm = d["demand"]
    print("Step 1c -- H-COHERENCE priced (a QUANTUM payload with the source away from Alice; see the docstring)")
    print("  Bob's stored hold, source at x from Alice (2x/c): %s"
          % "; ".join("%s %.3g s" % kv for kv in dm["hold_by_source"].items()))
    print("  zero-hold routes: source at Alice (flight in vacuum, H-VACUUM-FLIGHT; loss is the link budget's), or a bit "
          "payload (H-STATE-AS-BITS: measure on arrival)")
    print("  the retarded coupling route: coherent for the interaction, pi/(2 J_far) = %.3g s (>> L/c)"
          % dm["coupling_interaction_s"])
    print("  demand at the midpoint hold (%.4g s) by overhead k (capacity 1/k; k also multiplies the memories):"
          % d["T_hold_midpoint_s"])
    for k, v in dm["by_overhead_T2_s"].items():
        print("    k = %-8.3g T2 >= %.3g s (%.3g yr): %.3g x the best measured" % (k, v, v / YEAR_S,
                                                                             d["shortfall_by_overhead"][k]))
    print("  with no correction, all I qubits intact: T2 >= %s" % "; ".join(
        "%.3g s (%s)" % (v, n[:16]) for n, v in dm["no_correction_T2_s"].items()))
    print("  supply (READ):")
    for k, v in d["supply"].items():
        print("    %-20s T2 %.4g s (%s): the hold spans %.3g e-folds of it; p -> %.6f; capacity %.3g"
              % (k, v["T2_s"], SUPPLY[k]["kind"][:44], v["hold_in_T2_e_folds"], v["p_after_hold"],
                 v["capacity_after_hold"]))
    print("  under H-NO-REFRESH no measured memory carries a quantum payload through a midpoint hold; a fault-tolerant "
          "memory (H-FT-MEMORY) is OPEN and unpriced")


def selftest():
    n_ok = n_bad = n_ctl = 0
    n_struct = 0

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-96s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:96], got))

    def structural(text):
        nonlocal n_struct
        n_struct += 1
        print("  [STRUCTURAL] " + text)

    print("coherence.py selftest")
    d = collect()
    chk("every READ memory, over the midpoint hold, reaches p = 1/2 and capacity 0 (H-NO-REFRESH)",
        sorted(saturated(d["supply"])), sorted(SUPPLY))
    _fake = dict(SUPPLY)
    _fake["fake_long"] = dict(SUPPLY["P_in_28Si_Saeedi"], T2_s=10 * T_HOLD_MIDPOINT())
    chk("  CONTROL: a supply row with T2 = 10 x the hold is NOT flagged by the same predicate",
        "fake_long" in saturated(supply_rows(_fake)), False, ctl=True)
    sh = d["shortfall_by_overhead"]
    chk("the best measured T2 falls short at every overhead up to 1e27 by over 1e2 (k=2: %.3g; 1e6: %.3g; 1e12: %.3g; "
        "1e27: %.3g), and the shortfall falls as the overhead grows" % (sh[2.0], sh[1e6], sh[1e12], sh[1e27]),
        (all(sh[k] > 1e2 for k in (2.0, 1e6, 1e12, 1e27)), sh[2.0] > sh[1e6] > sh[1e12] > sh[1e27]), (True, True))
    chk("  at an overhead of 1e100 the shortfall is still over 1e1 (%.3g) -- not 'at any overhead'" % sh[1e100],
        sh[1e100] > 1e1, True)
    nc = list(d["demand"]["no_correction_T2_s"].values())[0]
    chk("without correction, all 9.5e27 qubits intact needs T2 over 1e35 s (%.3g s)" % nc, nc > 1e35, True)
    hb = d["demand"]["hold_by_source"]
    chk("the stored hold depends on the source: 0 at Alice, L/c at the midpoint, 2L/c at Bob",
        (hb["x = 0 (source at Alice)"], round(hb["x = L/2 (midpoint)"] / (L / C), 12),
         round(hb["x = L (source at Bob)"] / (L / C), 12)), (0.0, 1.0, 2.0))
    chk("the retarded coupling route's interaction time exceeds L/c by over 1e10 (%.3g)"
        % (d["demand"]["coupling_interaction_s"] / (L / C)), d["demand"]["coupling_interaction_s"] / (L / C) > 1e10,
        True)
    chk("every READ record names a source, route and kind; phrases under 15 words; extrapolated and abstract-only "
        "figures are marked and excluded from the best measured",
        ([k for k, v in SUPPLY.items() if not all(v.get(f) for f in ("source", "route", "kind"))],
         [k for k, v in SUPPLY.items() if len(v["phrase"].split()) >= 15],
         SUPPLY["Yb_ion_Wang"]["kind"].startswith("EXTRAPOLATED"),
         SUPPLY["Eu_YSO_Zhong"]["kind"].startswith("abstract only"), best_measured() == 180 * 60.0),
        ([], [], True, True, True))
    structural("p(t) = (1 - e^(-t/T2))/2 and T2_for_p are inverses (H-PURE-DEPHASING, H-EXP-DECAY)")
    structural("at k = 2 (p = 0.11) T2 = t / -ln(0.78) = 4.025 t and capacity ~1/2: functions of the constant alone "
               "(first counted)")
    structural("the stored hold 2x/c follows from the arrival times (L - x)/c and (x + L)/c")
    print("\n%d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted"
          % (n_ok, n_ok + n_bad, n_ctl, n_struct))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
