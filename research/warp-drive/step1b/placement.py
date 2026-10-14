#!/usr/bin/env python3
"""
placement.py -- Step 1b: the energy of placing the object's atoms at B, and the energy column's FLOOR.

Not seated.  Nothing here edits the board: figures are IMPORTED (balance, openterms, measure, massform, stock, nopath).
M (2026-10-05): "Continue" -- placement was the last energy term openterms.py left OPEN.

    python3 placement.py              report
    python3 placement.py --selftest   checks, with CONTROLS; STRUCTURAL items printed, never counted
    python3 placement.py --json       the numbers as JSON

WHAT IT COMPUTES
  (P1) THE DISSIPATION OF THE DESCRIPTION -- ONE FLOOR FOR THE BITS; AND, SEPARATELY, THE STOCK'S ENTROPY.  Bennett (physics/0210005v2 p.1, READ by measure.py;
       its H-ERASE): a step costs heat only if it is logically irreversible.  With the description in hand (it arrived
       over the channel), lowering the stock's configurational freedom to the object's arrangement can be done
       reversibly; the irreversible step is discarding the description afterwards (or, equivalently, resetting the
       register it was written into).  Either way the floor is I k T ln 2 at the temperature the heat is dumped into,
       ONCE.  balance.py already carries it as OUT-B-HEAT (H-RESET): placement adds no second floor FOR THE BITS.
       BUT B's stock is not a blank: it is thermal, mixed matter.  Ordering it into the object's arrangement lowers the
       MATTER's entropy by Delta S = S_stock - S_object (given the description), which must leave B as heat >= T_B Delta S
       (or be paid as work).  That is a different quantity from I, local to B like the chemical deficit, and OPEN
       (H-STOCK-ENTROPY): for Delta S of the order of the thermal-entropy count it is ~7e5 J at T_CMB and ~8e7 J at
       310 K (illustrative, computed from measure's thermal count) -- far below the channel.  Computed: the bit floor at
       T_CMB (balance.T_FLOOR) and at 310 K (measure.T_BODY), for every count.
  (P2) THE ENERGY TO HOLD AN ATOM IN PLACE -- A LOAN, NOT A COST.  Holding an atom of mass m within a spread sigma
       costs, in a harmonic trap, the ground energy E0 = 3 hbar^2 / (4 m sigma^2) (the general uncertainty-principle
       floor is the kinetic part alone, 3 hbar^2 / (8 m sigma^2); harmless here, since it is a returned loan) (from
       sigma^2 = hbar / (2 m omega) and E0 = (3/2) hbar omega; a computed identity, checked).  It is returned when the
       trap is released (H-REVERSIBLE-TRAP), so it is energy on hand, not energy consumed.  Per element and over the
       object at each pitch (measure.GRID_PITCHES; sigma = delta, H-SIGMA-IS-PITCH).  Beside it, k T at 310 K: an
       atom's thermal energy at body temperature is far above E0 at 1 A, i.e. localisation to 1 A is not what bounds
       the energy -- the chemistry holds the atoms once placed (openterms.py T2/T3).
  (P3) THE ENERGY COLUMN'S FLOOR.  balance.py refuses the energy TOTAL while terms are OPEN or ranges.  A FLOOR can be
       stated under named conditions, every part computed:
          reading at A           0 (theorem floor; openterms T1)
          chemistry, A and B     0 in the global column when A's residue and B's stock share a form (openterms
                                 global_chem; H-STOCK-FORM) -- B's local deficit is a separate local supply (bsupply)
          placement + reset      I k T ln 2 at T_CMB, ONCE (P1)
          channel                seat.channel_floor per schedule (balance IN-CHANNEL-E): no floor independent of T
          record / copy at A     0 if kept; I' k T ln 2 at 310 K if erased (H-ERASE-RECORD), I' = 2I (R-QUANTUM)
                                 or I (R-CLASSICAL)
          stock entropy at B    OPEN (H-STOCK-ENTROPY): not in the floor; illustrative size above
       For each count, reading and schedule.  It is a FLOOR under the channel hypotheses seat.py names -- H-EM-CARRIER,
       H-FEW-MODES and H-ONE-POL (one polarisation); with two polarisations the channel floor halves (printed), and wider
       apertures add modes and lower it further.  Across counts and erasure the schedule-independent part runs from
       2.5e5 J (species, record kept) to 6.5e8 J (0.1 A grid, R-QUANTUM, record erased).

NAMED HYPOTHESES
  H-REVERSIBLE-TRAP  the holding energy is returned on release (a conservative trap).
  H-SIGMA-IS-PITCH   the spread an atom is held to equals the grid pitch of the count (measure.GRID_PITCHES).
  H-STOCK-FORM       (openterms.py) the chemistry cancels globally only when the forms match.
  H-RESET, H-ERASE-RECORD (balance.py).
  H-STOCK-ENTROPY    the matter-entropy export at B, floor T_B Delta S, Delta S = S_stock - S_object; OPEN.
  H-EM-CARRIER, H-FEW-MODES, H-ONE-POL (seat.py) the channel floor's own hypotheses.

HISTORY (Step 1b verifier, 2026-10-05): 'placement adds NO second dissipation floor' (true for the bits; the stock's
entropy is a separate local term -- now named, OPEN); 'the check confirms it appears exactly once' (it counts a string
id: STRUCTURAL); the channel floor stated without its hypotheses; 'no floor independent of the schedule beyond about
1e5-1e7 J' (it reaches 6.5e8 J); the E0 identity and its scalings counted (identities: STRUCTURAL).
"""
import contextlib
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.abspath(os.path.join(HERE, ".."))
for _p in (os.path.join(WD, "docket68"), WD, HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

with contextlib.redirect_stdout(io.StringIO()):
    import balance
    import openterms
    import measure
    import massform
    import stock
    import nopath

HBAR = nopath.HBAR
KB = nopath.KB
U = massform.U_KG
T_CMB = balance.T_FLOOR
T_BODY = measure.T_BODY
EV = openterms.EV


# ============================================================================ (P1) one dissipation floor
def dissipation_floor(bits, T):
    return measure.landauer_j(bits, T)


def p1_rows():
    return [{"count": n, "bits": b, "floor_J_TCMB": dissipation_floor(b, T_CMB),
             "floor_J_310K": dissipation_floor(b, T_BODY)} for n, b in balance.counts()]


def counted_once(terms):
    """The dissipation of making the order appears ONCE: OUT-B-HEAT, and no separate placement-heat term."""
    return sum(1 for x in terms if x[0] == "OUT-B-HEAT"), sum(1 for x in terms if x[0] == "OUT-B-PLACE-HEAT")


# ============================================================================ (P2) the holding loan
def e0_trap(m, sigma):
    return 3.0 * HBAR ** 2 / (4.0 * m * sigma ** 2)


def e0_identity_check(m=12.0, sigma=1e-10):
    """E0 = (3/2) hbar omega with omega = hbar / (2 m sigma^2) equals 3 hbar^2/(4 m sigma^2)."""
    mk = m * U
    omega = HBAR / (2.0 * mk * sigma ** 2)
    return abs(1.5 * HBAR * omega - e0_trap(mk, sigma)) / e0_trap(mk, sigma)


def p2_rows():
    N, _ = measure.atom_counts()
    out = []
    for delta in measure.GRID_PITCHES:
        per = {e: e0_trap(stock.ATOMIC_MASS[e] * U, delta) for e in N}
        total = sum(N[e] * per[e] for e in N)
        out.append({"sigma_m": delta, "per_element_eV": {e: v / EV for e, v in per.items()},
                    "H_eV": per["H"] / EV, "loan_total_J_all_at_once": total,
                    "kT_310K_eV": KB * T_BODY / EV,
                    "H_E0_over_kT310": per["H"] / (KB * T_BODY)})
    return out


# ============================================================================ (P3) the floor
def floor_total(bits, reading, schedule_index=0, erase_record=False):
    t = balance.equation(bits, reading)
    get = {x[0]: x[4] for x in t}
    channel = get["IN-CHANNEL-E"] if schedule_index == 0 else \
        balance.seat.channel_floor(get["IN-CHANNEL"], balance.SCHEDULES_S[schedule_index])["E_1d_one_pol_J"]
    sent_or_copy = get["IN-CHANNEL"] if reading == "R-QUANTUM" else bits
    parts = {"read_A": 0.0, "chemistry_global": openterms.global_chem(-openterms.chem_ceiling_j())["global_J"],
             "placement_and_reset_once": dissipation_floor(bits, T_CMB), "channel": channel,
             "record_or_copy": dissipation_floor(sent_or_copy, T_BODY) if erase_record else 0.0}
    two_pol = balance.seat.channel_floor(get["IN-CHANNEL"], balance.SCHEDULES_S[schedule_index])["E_1d_two_pol_J"]
    return {"parts": parts, "floor_J": sum(parts.values()), "schedule_s": balance.SCHEDULES_S[schedule_index],
            "reading": reading, "erase_record": erase_record, "channel_two_pol_J": two_pol,
            "schedule_independent_J": parts["placement_and_reset_once"] + parts["record_or_copy"]}


def stock_entropy_illustration():
    """H-STOCK-ENTROPY, illustrative: T Delta S for Delta S of the order of measure's thermal-entropy count."""
    thermo = [b for n, b in balance.counts() if n.startswith("thermal")][0]
    return {"T_CMB_J": dissipation_floor(thermo, T_CMB), "T_310K_J": dissipation_floor(thermo, T_BODY)}


def collect():
    rows = []
    for n, b in balance.counts():
        for r in ("R-CLASSICAL", "R-QUANTUM"):
            for si in (0, 1):
                for er in (False, True):
                    f = floor_total(b, r, si, er)
                    f["count"] = n
                    rows.append(f)
    return {"P1": p1_rows(), "P2": p2_rows(), "P3": rows}


def report():
    d = collect()
    print("Step 1b -- placement, and the energy column's FLOOR")
    print("\n(P1) the dissipation of making the order: I k T ln 2, ONCE (Bennett; already OUT-B-HEAT)")
    for r in d["P1"]:
        print("    %-42s %.4g bits: %.4g J at %.4g K, %.4g J at %.0f K"
              % (r["count"], r["bits"], r["floor_J_TCMB"], T_CMB, r["floor_J_310K"], T_BODY))
    print("\n(P2) holding each atom within sigma: a loan returned on release (H-REVERSIBLE-TRAP)")
    for r in d["P2"]:
        print("    sigma %.0e m: H %.4g eV (%.3g x kT at 310 K); all atoms at once %.4g J"
              % (r["sigma_m"], r["H_eV"], r["H_E0_over_kT310"], r["loan_total_J_all_at_once"]))
    print("\n(P3) the FLOOR of the energy column (every real term is at or above its entry)")
    for f in d["P3"]:
        if not f["count"].startswith("species"):
            continue
        p = f["parts"]
        print("    %-11s schedule %.3g s, record %-6s floor %.4g J  [channel %.3g, placement+reset %.3g, record %.3g]"
              % (f["reading"], f["schedule_s"], "erased" if f["erase_record"] else "kept", f["floor_J"],
                 p["channel"], p["placement_and_reset_once"], p["record_or_copy"]))
    print("    (species-sequence count shown; --json carries all four counts.  Under H-EM-CARRIER, H-FEW-MODES, H-ONE-POL")
    print("     the channel dominates every floor and falls as the schedule lengthens; the total stays refused.)")
    two = [f for f in d["P3"] if f["count"].startswith("species") and f["reading"] == "R-CLASSICAL"][0]
    print("    two polarisations: channel %.3g J instead of %.3g J (1 yr, R-CLASSICAL)"
          % (two["channel_two_pol_J"], two["parts"]["channel"]))
    si = [f["schedule_independent_J"] for f in d["P3"]]
    print("    schedule-independent part across counts and erasure: %.3g J to %.3g J" % (min(si), max(si)))
    se = stock_entropy_illustration()
    print("    H-STOCK-ENTROPY (OPEN, not in the floor): for Delta S ~ the thermal count, %.3g J at T_CMB, %.3g J at 310 K"
          % (se["T_CMB_J"], se["T_310K_J"]))


def selftest():
    n_ok = n_bad = n_ctl = 0
    structural = []

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-92s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:92], got))

    print("placement.py selftest")
    sp = balance.counts()[0][1]
    t = balance.equation(sp, "R-QUANTUM")
    structural.append("the bit dissipation appears once in balance.py's rows (OUT-B-HEAT, no OUT-B-PLACE-HEAT): %s -- "
                      "a string-id count, not a thermodynamic check" % (counted_once(t),))
    chk("P1's floor at T_CMB equals balance's OUT-B-HEAT value (one floor, the same number)",
        abs(dissipation_floor(sp, T_CMB) - [x[4] for x in t if x[0] == "OUT-B-HEAT"][0]) < 1e-6, True)
    p2 = p2_rows()
    structural.append("E0 = (3/2) hbar omega = 3 hbar^2/(4 m sigma^2) (identity, residual %.1e) and its 1/sigma^2, 1/m "
                      "scalings are the formula as written" % e0_identity_check())
    chk("at 1 A, hydrogen's holding energy is below k T at 310 K (thermal motion exceeds the localisation cost)",
        p2[0]["H_E0_over_kT310"] < 1.0, True)
    chk("CONTROL: at 0.1 A it is not (localisation to 0.1 A costs more than k T at 310 K for hydrogen)",
        p2[1]["H_E0_over_kT310"] < 1.0, False, ctl=True)
    f0 = floor_total(sp, "R-QUANTUM", 0, False)
    f1 = floor_total(sp, "R-QUANTUM", 1, False)
    chk("the floor falls as the schedule lengthens (the channel term has no floor independent of T)",
        f1["floor_J"] < f0["floor_J"], True)
    chk("erasing the record raises the floor by exactly the record's Landauer term",
        abs(floor_total(sp, "R-QUANTUM", 0, True)["floor_J"] - f0["floor_J"]
            - dissipation_floor(2 * sp, T_BODY)) < 1e-6 * f0["floor_J"], True)
    allf = collect()["P3"]
    si = [f["schedule_independent_J"] for f in allf]
    chk("the schedule-independent part runs from 2.5e5 J to 6.5e8 J across counts and erasure (each to 5%)",
        (abs(min(si) / 2.48e5 - 1) < 0.05, abs(max(si) / 6.5e8 - 1) < 0.05), (True, True))
    tp = [f for f in allf if f["count"].startswith("species") and f["reading"] == "R-CLASSICAL"][0]
    chk("with two polarisations the channel floor is half the one-polarisation figure (to 1%)",
        abs(tp["channel_two_pol_J"] / tp["parts"]["channel"] - 0.5) < 0.01, True)
    chk("the channel is the largest part of every species-sequence floor in this file",
        all(max(f["parts"], key=f["parts"].get) == "channel"
            for f in collect()["P3"] if f["count"].startswith("species")), True)
    chk("balance.py still refuses the total (the floor is not the total)",
        balance.energy_total(t), None)
    structural.append("chemistry_global = 0 is openterms.global_chem's built-in cancellation for matching forms "
                      "(H-STOCK-FORM): carried into the floor, not re-derived")
    for x in structural:
        print("  [STRUCTURAL] " + x)
    print("\n%d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted"
          % (n_ok, n_ok + n_bad, n_ctl, len(structural)))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
