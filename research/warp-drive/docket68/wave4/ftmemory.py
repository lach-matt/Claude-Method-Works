#!/usr/bin/env python3
"""
ftmemory.py -- DOCKET 68 wave 4, W4B: H-FT-MEMORY priced -- a fault-tolerant memory holding the quantum payload for the
stored hold, on MEASURED surface-code figures READ at source.

Not seated.  M (rulings item 40): "2 then 1 please".  step1c/coherence.py left H-FT-MEMORY OPEN and unpriced: active
error correction below threshold gives logical lifetimes growing exponentially with code distance, so years are not
excluded in principle; the open question was the operations and energy.  This file prices them.

    python3 ftmemory.py              report
    python3 ftmemory.py --selftest   checks, with CONTROLS
    python3 ftmemory.py --json       the numbers as JSON

WHERE IT APPLIES
  Only to a QUANTUM payload with the pair source away from Alice (coherence.py: the stored hold is 2x/c; 0 with the
  source at Alice, 0 for a bit payload).  At the midpoint the hold is L/c.
THE MODEL (each input READ or imported)
  Surface-code memory, Google Quantum AI 2408.13687v1 (READ by the QEC reader, re-read by the lead): logical error per
  cycle eps_7 = 1.43e-3 at distance 7; suppression Lambda = eps_d / eps_{d+2} = 2.14; cycle time 1.1 us; 2 d^2 - 1
  physical qubits per logical qubit; d^2 - 1 measure qubits measured and reset each cycle (derived from the layout);
  and a MEASURED logical error floor of about 1e-10 per cycle from correlated bursts once an hour (repetition codes,
  origin not understood).
  eps_d = eps_7 / Lambda^((d - 7)/2) (H-LAMBDA-HOLDS: the measured suppression continues to the distance needed --
  extrapolated far beyond d = 7).  The distance is the least odd d with N_logical x cycles x eps_d <= 1
  (H-ONE-FAILURE: at most one expected logical failure over the whole payload and hold).
  Energy: a LANDAUER FLOOR on resetting the measure qubits, (d^2 - 1) kT ln 2 per logical qubit per cycle at the
  coldest bath on the board, T_CMB (H-LANDAUER-FLOOR: real dissipation, and the Carnot cost of refrigeration, are
  larger and excluded).  Mass: at least one atom of 1 u per physical qubit (H-ONE-ATOM-PER-QUBIT), against the
  object's own mass.
NAMED HYPOTHESES
  H-LAMBDA-HOLDS, H-ONE-FAILURE, H-LANDAUER-FLOOR, H-ONE-ATOM-PER-QUBIT, H-NO-BURST-FLOOR (the measured 1e-10 floor is
  removed -- without it the memory fails), and coherence.py's (H-MIDPOINT-SOURCE, H-STATE-AS-BITS) and demand.py's.
"""
import contextlib
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.abspath(os.path.join(HERE, "..", ".."))
S1C = os.path.join(WD, "step1c")


def _by_path(key, path):
    import importlib.util as _ilu
    if key in sys.modules:
        return sys.modules[key]
    spec = _ilu.spec_from_file_location(key, path)
    mod = _ilu.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


with contextlib.redirect_stdout(io.StringIO()):
    coherence = _by_path("s1c_coherence", os.path.join(S1C, "coherence.py"))
    demand = coherence.demand
    massform = demand.balance.massform
    nopath = demand.balance.nopath

KB = nopath.KB
T_BATH = demand.balance.T_FLOOR                 # T_CMB, the coldest bath the board holds (balance.py)
U_KG = massform.U_KG

QEC = {"source": "arXiv:2408.13687v1 (Google Quantum AI)",
       "route": "READ via alphaXiv answer_pdf_queries, pp.1-3, 6 (QEC reader; re-read by the lead)",
       "kind": "measured (Lambda, eps_7, cycle time, floor); 2d^2 - 1 stated", "eps7": 1.43e-3, "Lambda": 2.14,
       "cycle_s": 1.1e-6, "floor_per_cycle": 1e-10, "phrase": "suppressed by a factor of Lambda = 2.14 +- 0.02",
       "phrase_floor": "set a current error floor of 10^-10"}


def eps(d):
    """H-LAMBDA-HOLDS."""
    return QEC["eps7"] / QEC["Lambda"] ** ((d - 7) / 2.0)


def distance_needed(n_logical, cycles):
    """Least odd d with n_logical x cycles x eps_d <= 1 (H-ONE-FAILURE)."""
    need = 1.0 / (n_logical * cycles)
    steps = math.ceil(math.log(QEC["eps7"] / need) / math.log(QEC["Lambda"]))
    return 7 + 2 * max(0, steps)


def memory(n_logical, hold_s):
    cycles = hold_s / QEC["cycle_s"]
    d = distance_needed(n_logical, cycles)
    phys = n_logical * (2 * d * d - 1)
    resets = n_logical * (d * d - 1) * cycles
    E = resets * KB * T_BATH * math.log(2.0)
    return {"hold_s": hold_s, "cycles": cycles, "d": d, "eps_d": eps(d), "physical_qubits": phys,
            "landauer_J": E, "landauer_W": E / hold_s, "mass_kg_min": phys * U_KG,
            "failures_at_floor": n_logical * cycles * QEC["floor_per_cycle"]}


def collect():
    hold = coherence.T_HOLD_MIDPOINT()
    out = {"hold_s": hold, "object_kg": massform.PAYLOAD_KG, "by_count": {}}
    for n, b in demand.counts():
        out["by_count"][n] = memory(b, hold)
    out["QEC"] = QEC
    return out


def report():
    d = collect()
    print("D68 wave 4, W4B -- a fault-tolerant memory for the quantum payload over the midpoint hold (%.4g s)"
          % d["hold_s"])
    print("  measured: eps_7 = %.3g, Lambda = %.3g, cycle %.3g s, floor %.0e per cycle (2408.13687v1)"
          % (QEC["eps7"], QEC["Lambda"], QEC["cycle_s"], QEC["floor_per_cycle"]))
    for n, m in d["by_count"].items():
        print("  %-40s cycles %.3g; distance %d (eps_d %.3g); physical qubits %.3g; Landauer floor %.3g J = %.3g W; "
              "mass >= %.3g kg (%.3g x the object)" % (n, m["cycles"], m["d"], m["eps_d"], m["physical_qubits"],
                                                       m["landauer_J"], m["landauer_W"], m["mass_kg_min"],
                                                       m["mass_kg_min"] / d["object_kg"]))
        print("    with the measured 1e-10 floor: %.3g expected logical failures (H-NO-BURST-FLOOR needed)"
              % m["failures_at_floor"])


def selftest():
    n_ok = n_bad = n_ctl = 0

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-96s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:96], got))

    print("ftmemory.py selftest")
    d = collect()
    sp = list(d["by_count"].values())[0]
    chk("species count over the midpoint hold: the distance meets one expected failure and the next-smaller odd "
        "distance does not (d = %d)" % sp["d"],
        (list(demand.counts())[0][1] * sp["cycles"] * eps(sp["d"]) <= 1,
         list(demand.counts())[0][1] * sp["cycles"] * eps(sp["d"] - 2) > 1), (True, True))
    chk("  CONTROL: one logical qubit held for one cycle needs no more than distance 7",
        distance_needed(1.0, 1.0), 7, ctl=True)
    chk("the distance is over 200 (%d) and the physical qubits over 1e32 (%.3g)" % (sp["d"], sp["physical_qubits"]),
        (sp["d"] > 200, sp["physical_qubits"] > 1e32), (True, True))
    chk("with the MEASURED 1e-10 burst floor the memory fails: over 1e30 expected logical failures (%.3g)"
        % sp["failures_at_floor"], sp["failures_at_floor"] > 1e30, True)
    chk("the memory's minimum mass (one 1 u atom per physical qubit) exceeds the object's by over 1e4 (%.3g x)"
        % (sp["mass_kg_min"] / d["object_kg"]), sp["mass_kg_min"] / d["object_kg"] > 1e4, True)
    chk("the Landauer floor at T_CMB over the hold is over 1e23 J (%.3g J; %.3g W)" % (sp["landauer_J"],
                                                                                    sp["landauer_W"]),
        sp["landauer_J"] > 1e23, True)
    chk("the QEC record names its route and kind; phrases under 15 words",
        (bool(QEC["route"] and QEC["kind"]), len(QEC["phrase"].split()) < 15, len(QEC["phrase_floor"].split()) < 15),
        (True, True, True))
    print("  [STRUCTURAL] eps_d = eps_7 / Lambda^((d-7)/2) is the suppression law extrapolated (H-LAMBDA-HOLDS)")
    print("  [STRUCTURAL] 2d^2 - 1 physical and d^2 - 1 reset qubits per logical qubit (the rotated surface code)")
    print("\n%d/%d checks pass, %d of them controls; 2 STRUCTURAL printed, not counted" % (n_ok, n_ok + n_bad, n_ctl))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
