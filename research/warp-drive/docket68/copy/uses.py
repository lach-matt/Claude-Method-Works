#!/usr/bin/env python3
"""
uses.py -- uses priced against the first trip (M-RULINGS item 88, link 1: S5 against D23; DOCKET 56's owed instrument,
on the faithful-copy path).  Deduced and computed.  Not seated; not verified.  M's words are carried as hypotheses,
never as results.

S5 (reconstruction from stock at the destination) pays a setup once -- the device at position 2 must itself travel at
or below c (D23; M's answer 4, H-ADDRESS-INPUT) -- and then a price per use.  Sending the thing itself pays the full
trip every time.  seat.py (imported, never retyped) holds the identity: with K = (gamma-1) c^2 (H-KINETIC),
    k* = m_set K / (m_pay K - E_rec),   -> m_set / m_pay as E_rec -> 0,   and no k* once E_rec >= m_pay K.
M ruled (item 89, verbatim): "No costlier. Stock is stock. The cost is in how much information is transferred as a
README (how big the file is)."  Carried as H-STOCK-IS-STOCK and H-COST-IN-README.  This file prices E_rec under that
ruling, with the README sized by faithful.py (imported) and the channel by seat.channel_floor (LNM, READ there).

WHAT FOLLOWS THE WORK
  * UNDER M'S RULING THE BREAK-EVEN IS A MASS RATIO (U1, U2).  The README's received-energy floor for the identity core
    (2.74e15 bits) over one year is 1.15e-11 J (seat.channel_floor, 1D, one polarisation), 27 orders below the trip it
    replaces (3.17e16 J for 70 kg at 0.1 c).  So k* = m_set / m_pay to better than one part in 10^27: the route beats
    sending the thing itself after m_set / 70 kg uses, whatever the speed, while E_rec counts only the README.  What
    moves k* is the device's mass, which no instrument specifies (seat: m_set "NOT SPECIFIED ANYWHERE").
  * M'S "HOW BIG THE FILE IS" HAS AN EXACT FORM (U3).  On the 1D floor the energy goes as N^2 / T: double the file and
    the cost quadruples; double the time and it halves.  Distance does not enter the 1D floor; it enters only the time.
  * THE README HAS A BUDGET, AND THE CORE IS FAR INSIDE IT (U4).  The file can grow to 1.4e28 bits (at 0.1 c, over one
    year) before its cost moves k* by 1 %; at 0.01 c, to 1.4e27.  The unpriced recipe and the brain outside the cortex
    (faithful.py OPEN 1-2) fit inside that budget unless they exceed the core by more than twelve orders (at 0.1 c).
  * THE SNAPSHOT IS THE CONTRAST (U5).  The board's largest snapshot count (1.09e29 bits) over one year costs 1.8e16 J
    on the same floor: at 0.01 c that exceeds the trip it replaces, so on that schedule S5 never pays back; at 0.1 c
    it multiplies k* by 2.3.  Over 100 years it pays back again (k* 2.4 x the mass ratio at 0.01 c), since the floor
    falls as 1/T.  The identity core pays back at every speed and schedule computed, at the mass ratio.  On a given
    schedule the README's size decides whether the route can pay at all; the device's mass decides when.
  * EACH USE HAS A TIME BUDGET (U6).  After the first, a use beats shipping in time when transmission + build is less
    than (D/c)(1/beta - 1): 38.2 years at 0.1 c, 1.06 years at 0.8 c, none at c.  Through a gravitational port it never
    is: carrier.py's fastest rotor loads the core in 6.7e12 s at the capacity ceiling, past even the 0.01 c budget
    (420 years).  An electromagnetic README fits, since its transmission time is a schedule chosen against U3's 1/T.
    First written: "fits that budget at 0.1 c only for a rotor arm of 13.5 m or more (one bit per graviton)" --
    zeromode's H-BIT-PER-GRAVITON ladder, which fails above an arm of 1.8 m (carrier.py, verified).
  * The first use is no faster than the first trip: the device must arrive first, at the same speeds (D23).

Boundary (item 82): what this does not price.  E_rec here counts the README only.  The fabrication energy E_fab is
NOT COMPUTED ANYWHERE on the board (seat.DOCKET56_OWED); under M's ruling it is borne at position 2 from local supply
(H-FAB-LOCAL).  If it had to be shipped it would enter E_rec, and seat.erec_ceiling is the line it would have to stay
under.  The 1D figure floors RECEIVED energy only (seat's H-FEW-MODES); transmitted energy, with diffraction loss, is
not floored -- U4 states how large the loss factor may be before k* moves by 1 %.

    python3 uses.py              report
    python3 uses.py --selftest   checks, CONTROLS and CONTRASTS marked, STRUCTURAL printed and not counted
    python3 uses.py --json       the numbers as JSON

U1 [imported]  seat.breakeven(m_set, beta, E_rec), seat.breakeven_symbolic(), seat.erec_ceiling(): the identity and the
   ceiling, on seat's 70 kg payload (massform.PAYLOAD_KG) and Proxima span (D_PROXIMA = 4.0175e16 m).
U2 [computed]  E_rec := E_tx, the README's received-energy floor seat.channel_floor(N, T)["E_1d_one_pol_J"]
   (H-COST-IN-README, H-FAB-LOCAL, H-EM-CARRIER, H-ONE-POL, H-FEW-MODES; seat's), with N = faithful.identity_core()
   (H-README-IS-CORE: the README's size is the cortical wiring core; the recipe is not priced) and a DECLARED T.
U3 [computed]  The scaling of E_1d in N and T, measured on the imported function, not assumed.
U4 [computed]  N_budget(f, beta, T): the README size at which E_1d = f x m_pay K, so that k* = (m_set/m_pay)/(1 - f).
   Loss budget: the transmitted/received factor at which the transmitted energy reaches 1 % of m_pay K.
U5 [computed]  The same with N = the board's snapshot counts (measure.object_bits via faithful._measure, imported).
U6 [computed]  Time per use after the first: D/c + T_tx + t_build against D/(beta c); t_build OPEN.  Port time from
   carrier.port / carrier.best_arm / carrier.min_arm_within (imported): zeromode's rotors at the g(N) ceiling
   (Giovannetti et al., READ there; H-BANDWIDTH-F).

NAMED HYPOTHESES
  M's: H-STOCK-IS-STOCK, H-COST-IN-README (item 89); H-ADDRESS-INPUT (item 86).  The file's own: H-FAB-LOCAL,
  H-README-IS-CORE, H-SAME-SPEED (the device travels at the payload's speed, as seat's identity assumes),
  M_SET_ILLUSTRATIVE (values of m_set DECLARED for illustration, not designs).  seat's: H-KINETIC, H-EM-CARRIER, H-ONE-POL,
  H-FEW-MODES.  faithful's: H-WIRING-SUFFICES and the inputs of the identity core.  carrier's: H-BANDWIDTH-F.
"""

import contextlib
import importlib.util
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)

M_SET_ILLUSTRATIVE = (70.0, 700.0, 7.0e3, 7.0e4)       # kg, DECLARED: device mass of 1, 10, 100, 1000 payloads
BETAS = (0.8, 0.2, 0.1, 0.01)                          # DECLARED speeds; 0.2, 0.1, 0.01 are seat.erec_ceiling's own
T_DECLARED_YR = (1.0, 100.0)                           # seat.collect's own schedules
F_BUDGET = 0.01                                        # "moves k* by 1 %"


def _load(name, path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    m = importlib.util.module_from_spec(spec)
    saved = list(sys.path)
    try:
        sys.path.insert(0, WD)
        sys.path.insert(0, os.path.dirname(path))
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(m)
    finally:
        sys.path[:] = saved
    return m


_CACHE = {}


def owners():
    if not _CACHE:
        _CACHE["seat"] = _load("seat", os.path.join(D68, "seat.py"), "d68_seat_uses")
        _CACHE["faithful"] = _load("faithful", os.path.join(HERE, "faithful.py"), "copy_faithful_uses")
        _CACHE["carrier"] = _load("carrier", os.path.join(HERE, "carrier.py"), "copy_carrier_uses")
    return _CACHE["seat"], _CACHE["faithful"], _CACHE["carrier"]


def trip_energy(beta):
    """m_pay (gamma-1) c^2: seat.erec_ceiling's own formula, called for any beta."""
    seat, _, _ = owners()
    return seat.erec_ceiling((beta,))[beta]


def e_tx(N, T_yr):
    seat, _, _ = owners()
    return seat.channel_floor(N, T_yr * seat.YEAR_S)


def n_budget(f, beta, T_yr, N_ref):
    """README size at which the 1D received floor equals f x the trip energy.  Found by bisection on the imported
    floor, so the N^2/T law is used only as U3 measures it, never assumed."""
    target = f * trip_energy(beta)
    lo, hi = N_ref * 1e-6, N_ref * 1e30
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if e_tx(mid, T_yr)["E_1d_one_pol_J"] >= target:
            hi = mid
        else:
            lo = mid
    return hi


def time_budget_s(beta):
    """After the first use, a use beats shipping in time iff T_tx + t_build < D/(beta c) - D/c."""
    seat, _, _ = owners()
    return seat.D_PROXIMA / seat.C * (1.0 / beta - 1.0)


def compute():
    seat, fa, ca = owners()
    kstar_sym, lim, lim_ok = seat.breakeven_symbolic()
    core = fa.identity_core()["total_bits"]
    snap = fa._measure()
    snap_lo, snap_hi = snap["species"], snap["grid_0p1A"]
    rows = {}
    for T in T_DECLARED_YR:
        Ec = e_tx(core, T)["E_1d_one_pol_J"]
        El = e_tx(snap_lo, T)["E_1d_one_pol_J"]
        Eh = e_tx(snap_hi, T)["E_1d_one_pol_J"]
        for b in BETAS:
            Et = trip_energy(b)
            rows[(T, b)] = {
                "trip_J": Et, "E_core_J": Ec, "E_snap_lo_J": El, "E_snap_hi_J": Eh,
                "core_over_trip": Ec / Et, "snap_lo_over_trip": El / Et, "snap_hi_over_trip": Eh / Et,
                "kstar_core": {m: seat.breakeven(m, b, Ec) for m in M_SET_ILLUSTRATIVE},
                "kstar_snap_lo": {m: seat.breakeven(m, b, El) for m in M_SET_ILLUSTRATIVE},
                "kstar_snap_hi": {m: seat.breakeven(m, b, Eh) for m in M_SET_ILLUSTRATIVE},
                "N_budget_1pct": n_budget(F_BUDGET, b, T, core),
                "loss_budget_1pct": F_BUDGET * Et / Ec,
            }
    # U3: the scaling measured on the imported floor
    E0 = e_tx(core, 1.0)["E_1d_one_pol_J"]
    scale_N = e_tx(2 * core, 1.0)["E_1d_one_pol_J"] / E0
    scale_T = e_tx(core, 2.0)["E_1d_one_pol_J"] / E0
    scale_d = (seat.channel_floor(core, seat.YEAR_S, d=seat.D_PROXIMA * 10)["E_1d_one_pol_J"] / E0)
    times = {}
    for b in BETAS + (1.0,):
        tb = time_budget_s(b)
        times[b] = {"ship_s": seat.D_PROXIMA / (b * seat.C), "light_s": seat.D_PROXIMA / seat.C, "budget_s": tb,
                    "min_arm_core_m": ca.min_arm_within(tb, core) if tb > 0 else None}
    arm, port_best = ca.best_arm(core)
    return {"kstar_symbolic": str(kstar_sym), "kstar_limit": str(lim), "limit_is_mass_ratio": lim_ok,
            "core_bits": core, "snap_lo_bits": snap_lo, "snap_hi_bits": snap_hi,
            "rows": rows, "scale_N2": scale_N, "scale_T2": scale_T, "scale_d10": scale_d, "times": times,
            "erec_ceiling": seat.erec_ceiling(), "payload_kg": seat.PAYLOAD_KG, "D_m": seat.D_PROXIMA,
            "year_s": seat.YEAR_S, "port_best_arm_m": arm, "port_best_load_s": port_best,
            "rest_energy_J": seat.PAYLOAD_KG * seat.C ** 2}


def _fmt_k(k):
    return "none" if k is None else "%.6g" % k


def report():
    d = compute()
    print("uses.py -- uses priced against the first trip (M item 88, link 1; not verified; not seated)\n")
    print("U1 k* = %s ; as E_rec -> 0, k* -> %s (mass ratio: %s)" % (d["kstar_symbolic"], d["kstar_limit"],
                                                                    d["limit_is_mass_ratio"]))
    print("U2 README = identity core, %.3e bits; snapshot counts %.3e to %.3e bits" % (
        d["core_bits"], d["snap_lo_bits"], d["snap_hi_bits"]))
    for (T, b), r in d["rows"].items():
        print("   T = %g yr, beta = %g: trip %.3e J; README floor core %.3e J (%.1e of trip), snapshot %.3e to %.3e J" % (
            T, b, r["trip_J"], r["E_core_J"], r["core_over_trip"], r["E_snap_lo_J"], r["E_snap_hi_J"]))
        print("      k* (core) by m_set %s ; k* (largest snapshot) %s" % (
            ", ".join("%g kg: %s" % (m, _fmt_k(k)) for m, k in r["kstar_core"].items()),
            ", ".join("%g kg: %s" % (m, _fmt_k(k)) for m, k in r["kstar_snap_hi"].items())))
        print("      README budget (k* moves 1 %%): %.3e bits; loss budget %.2e" % (r["N_budget_1pct"],
                                                                                r["loss_budget_1pct"]))
    print("U3 scaling on the imported floor: 2N -> x%.6f ; 2T -> x%.6f ; 10 d -> x%.6f" % (
        d["scale_N2"], d["scale_T2"], d["scale_d10"]))
    print("U6 time per use after the first: budget = (D/c)(1/beta - 1); carrier's fastest gravitational port loads the "
          "core in %.3g s (%.3g yr, arm %.2f m, at the g(N) ceiling)" % (d["port_best_load_s"],
                                                                         d["port_best_load_s"] / d["year_s"],
                                                                         d["port_best_arm_m"]))
    for b, t in d["times"].items():
        print("   beta %g: ship %.3f yr, budget %.3f yr, smallest rotor arm for the core %s" % (
            b, t["ship_s"] / d["year_s"], t["budget_s"] / d["year_s"],
            "-" if t["min_arm_core_m"] is None else "%.2f m" % t["min_arm_core_m"]))


def selftest():
    n_pass = n_fail = n_ctl = n_con = 0
    structural = []

    def chk(label, ok, ctl=False, contrast=False):
        nonlocal n_pass, n_fail, n_ctl, n_con
        n_ctl += ctl
        n_con += contrast
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else ("CONTRAST: " if contrast else ""), label))

    seat, fa, ca = owners()
    d = compute()
    r1 = d["rows"][(1.0, 0.1)]
    r01 = d["rows"][(1.0, 0.01)]
    chk("U1: seat's identity tends to the mass ratio m_set/m_pay as E_rec -> 0 (sympy: %s)" % d["kstar_limit"],
        d["limit_is_mass_ratio"] is True)
    chk("U1: the trip energy reproduces seat.erec_ceiling at 0.1 c (%.4e J)" % r1["trip_J"],
        abs(r1["trip_J"] / seat.erec_ceiling()[0.1] - 1) < 1e-12)
    chk("U2: the core's README floor over one year (%.3e J) is below 1e-25 of the 0.1 c trip (%.1e)" % (
        r1["E_core_J"], r1["core_over_trip"]), r1["core_over_trip"] < 1e-25)
    ok = all(abs(k / (m / d["payload_kg"]) - 1) < 1e-12 for m, k in r1["kstar_core"].items())
    chk("U2: so k* = m_set / 70 kg at 0.1 c for every illustrative m_set (%s)" % ", ".join(
        _fmt_k(k) for k in r1["kstar_core"].values()), ok)
    chk("U3: on the imported 1D floor, doubling N multiplies the energy by %.6f (N^2)" % d["scale_N2"],
        abs(d["scale_N2"] - 4) < 1e-6)
    chk("U3: doubling T multiplies it by %.6f (1/T); ten times the distance by %.6f (none)" % (
        d["scale_T2"], d["scale_d10"]), abs(d["scale_T2"] - 0.5) < 1e-6 and abs(d["scale_d10"] - 1) < 1e-9)
    nb = r1["N_budget_1pct"]
    chk("U4: at the README budget (%.3e bits) the floor is 1 %% of the trip, so k* = 1.0101 x the mass ratio" % nb,
        abs(seat.breakeven(70.0, 0.1, e_tx(nb, 1.0)["E_1d_one_pol_J"]) / (1 / (1 - F_BUDGET)) - 1) < 1e-6)
    chk("U5: the largest snapshot over one year (%.3e J) exceeds the 0.01 c trip (%.3e J): no k* at any m_set" % (
        r01["E_snap_hi_J"], r01["trip_J"]), all(k is None for k in r01["kstar_snap_hi"].values()), contrast=True)
    chk("U5: the identity core pays back at every speed and schedule computed",
        all(all(k is not None for k in r["kstar_core"].values()) for r in d["rows"].values()))
    chk("with E_rec set at the trip energy (0.1 c), seat.breakeven returns no k* -- the test can fail",
        seat.breakeven(70.0, 0.1, r1["trip_J"]) is None, ctl=True)
    t = d["times"]
    chk("U6: after the first use the time budget at 0.1 c is %.2f yr = 9 x the light time" % (
        t[0.1]["budget_s"] / d["year_s"]), abs(t[0.1]["budget_s"] / t[0.1]["light_s"] - 9) < 1e-12)
    chk("at beta = 1 the time budget is zero -- no use can beat shipping at c on time",
        t[1.0]["budget_s"] == 0.0, ctl=True)
    chk("U6: no rotor of zeromode's family loads the core inside the time budget at any speed computed (fastest %.3g s "
        "against the 0.01 c budget %.3g s)" % (d["port_best_load_s"], t[0.01]["budget_s"]),
        all(t[b]["min_arm_core_m"] is None for b in BETAS) and d["port_best_load_s"] > t[0.01]["budget_s"])
    structural.append("E_fab (fabrication energy) is NOT COMPUTED ANYWHERE (seat.DOCKET56_OWED); under H-FAB-LOCAL it "
                      "is not in E_rec")
    structural.append("m_set is NOT SPECIFIED ANYWHERE (seat.DOCKET56_OWED); the m_set values are DECLARED")
    structural.append("the 1D floor bounds RECEIVED energy (seat's H-FEW-MODES); transmitted energy is not floored")
    structural.append("the README is the cortical core (H-README-IS-CORE); the recipe is unpriced (faithful OPEN 2)")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("uses.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        d = compute()
        d["rows"] = {"T=%g,beta=%g" % k: v for k, v in d["rows"].items()}
        print(json.dumps(d, indent=1, default=str))
    else:
        report()
