#!/usr/bin/env python3
"""
placement.py -- Step 1b: the energy of placing the object's atoms at B, and the energy column's FLOOR.

Not seated.  Nothing here edits the board: figures are IMPORTED (balance, openterms, measure, massform, stock, nopath).
M (2026-10-05): "Continue" -- placement was the last energy term openterms.py left OPEN.

    python3 placement.py              report
    python3 placement.py --selftest   checks, with CONTROLS; STRUCTURAL items printed, never counted
    python3 placement.py --json       the numbers as JSON

WHAT IT COMPUTES
  (P1) THE DISSIPATION OF MAKING THE ORDER -- ONE FLOOR, NOT TWO.  Bennett (physics/0210005v2 p.1, READ by measure.py;
       its H-ERASE): a step costs heat only if it is logically irreversible.  With the description in hand (it arrived
       over the channel), lowering the stock's configurational freedom to the object's arrangement can be done
       reversibly; the irreversible step is discarding the description afterwards (or, equivalently, resetting the
       register it was written into).  Either way the floor is I k T ln 2 at the temperature the heat is dumped into,
       ONCE.  balance.py already carries it as OUT-B-HEAT (H-RESET).  So placement adds NO second dissipation floor:
       counting both would double-count the same bits.  Computed: the floor at T_CMB (balance.T_FLOOR) and at 310 K
       (measure.T_BODY), for every count.
  (P2) THE ENERGY TO HOLD AN ATOM IN PLACE -- A LOAN, NOT A COST.  Holding an atom of mass m within a spread sigma
       costs at least the ground energy of a 3D harmonic trap with that spread: E0 = 3 hbar^2 / (4 m sigma^2) (from
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
       For each count, reading and schedule.  It is a FLOOR: every real term is at or above its entry.

NAMED HYPOTHESES
  H-REVERSIBLE-TRAP  the holding energy is returned on release (a conservative trap).
  H-SIGMA-IS-PITCH   the spread an atom is held to equals the grid pitch of the count (measure.GRID_PITCHES).
  H-STOCK-FORM       (openterms.py) the chemistry cancels globally only when the forms match.
  H-RESET, H-ERASE-RECORD (balance.py).
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
    return {"parts": parts, "floor_J": sum(parts.values()), "schedule_s": balance.SCHEDULES_S[schedule_index],
            "reading": reading, "erase_record": erase_record}


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
    print("    (species-sequence count shown; --json carries all four counts.  The channel dominates every floor and")
    print("     falls as the schedule lengthens; the total itself stays refused in balance.py.)")


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
    chk("the dissipation of making the order is carried ONCE (OUT-B-HEAT), with no second placement-heat term",
        counted_once(t), (1, 0))
    chk("CONTROL: a second placement-heat term planted is caught (counted twice)",
        counted_once(t + [("OUT-B-PLACE-HEAT",) + t[0][1:]]), (1, 1), ctl=True)
    chk("P1's floor at T_CMB equals balance's OUT-B-HEAT value (one floor, the same number)",
        abs(dissipation_floor(sp, T_CMB) - [x[4] for x in t if x[0] == "OUT-B-HEAT"][0]) < 1e-6, True)
    chk("E0 = (3/2) hbar omega with sigma^2 = hbar/(2 m omega) equals 3 hbar^2/(4 m sigma^2) (to 1e-12)",
        e0_identity_check() < 1e-12, True)
    p2 = p2_rows()
    chk("E0 falls as 1/sigma^2: 10x the pitch, 1/100 the energy (to 1e-12)",
        abs(p2[0]["H_eV"] / p2[1]["H_eV"] - 0.01) < 1e-12, True)
    chk("E0 falls as 1/m: O's E0 is H's x m_H/m_O (to 1e-12)",
        abs(p2[0]["per_element_eV"]["O"] / p2[0]["per_element_eV"]["H"]
            - stock.ATOMIC_MASS["H"] / stock.ATOMIC_MASS["O"]) < 1e-12, True)
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
