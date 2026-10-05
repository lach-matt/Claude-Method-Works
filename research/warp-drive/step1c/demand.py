#!/usr/bin/env python3
"""
demand.py -- Step 1c: what each part of a device must DELIVER, on the balanced equation's own terms.

Not seated.  Nothing here edits the board.  M ruled the order 1a (the specification theorem), 1b (the balanced
equation), 1c the device (specthm.py section 0), and first framed the work as "balancing an equation with the theory and
math on one side, and the device engineering and materials on the other side" (ledger.py section 0).  Step 1b
(step1b/BALANCE.md) fixed the equation: I(A, before) = I(B, after), every matter and energy term an input or output.
A device is whatever performs those terms.  This file reads the device's SUBSYSTEMS off the equation's rows and prices
what each must deliver -- rates, powers, an opening, a stock -- per schedule.  It establishes no supply: what present
engineering delivers for each subsystem is NOT read here (that is the next step, and which subsystem first is M's).

    python3 demand.py              report
    python3 demand.py --selftest   checks, with CONTROLS
    python3 demand.py --json       the numbers as JSON

THE SUBSYSTEMS (each from balance.equation's rows; every figure IMPORTED from its owner, none retyped)
  READ-A      IN-A-READ: read I bits of the object at A.  Demand: I/T bits/s, N_atoms/T atoms/s.  Energy: the theorem
              floor is 0 (openterms T1); under H-PROBE the 1 A probe floors (photon, electron, neutron), as power.
  CHANNEL     IN-CHANNEL / IN-CHANNEL-E: carry I bits (R-CLASSICAL) or 2 bits per qubit (R-QUANTUM) A -> B.  Demand:
              the rate, seat.channel_floor's received-energy floor as power (H-EM-CARRIER, H-FEW-MODES, H-ONE-POL), and
              aperture.py's smallest opening (H-HALF-WAVE).
  COUPLING    the wave-3 alternative to CHANNEL (corridor.py): hbar J for the whole object in T (aperture.coupling_view)
              and the before-light condition (corridor.before_light).  Every speed-free route clashes with H-LOCALITY.
  ASSEMBLE-B  IN-B-ASSEMBLE / OUT-B-HEAT: place N_atoms in T and write I bits.  Demand: atoms/s; the register reset floor
              I k T_CMB ln 2 (H-RESET) as power; the chemical ceiling (openterms, H-VALENCE) as power -- a CEILING, not
              a value (H-STOCK-FORM).
  POWER-B     the collector at B (bsupply.py): the area that B's local terms need at Proxima b's flux, eta = 1
              (H-COLLECT, H-AT-ORBIT, H-STEADY), at Faria's central L* and at the low end.
  STOCK-B     IN-B-STOCK: D25's stock gate (balance.stock_terms): CI feedstock, binder, measured at Proxima or not.
  RETIRE-A    OUT-A-RESIDUE (H-RETIRE-A, M's hypothesis): A's matter retired as stock; its energy is OPEN.

NAMED HYPOTHESES (this file's own)
  H-SCHEDULE      the transfer completes in T, for T in balance.SCHEDULES_S and aperture.SCHEDULES_S (a day, a year,
                  a century): every rate is a schedule's, not the route's -- no subsystem has a rate independent of T.
  H-UNIFORM-RATE  each subsystem runs at a constant rate over T (a burst raises the peak, never lowers the mean).
  H-PARALLEL      the subsystems run concurrently; their times do not add.
  Those of the owners, as each names them (H-PROBE, H-EM-CARRIER, H-FEW-MODES, H-ONE-POL, H-HALF-WAVE, H-RESET,
  H-VALENCE, H-STOCK-FORM, H-COLLECT, H-AT-ORBIT, H-STEADY, H-CI-PROXY, H-RETIRE-A, H-LOCALITY).
"""
import contextlib
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.abspath(os.path.join(HERE, ".."))
S1B = os.path.join(WD, "step1b")
W3 = os.path.join(WD, "docket68", "wave3")
for _p in (os.path.join(WD, "docket68"), WD, S1B):
    if _p not in sys.path:
        sys.path.insert(0, _p)

with contextlib.redirect_stdout(io.StringIO()):
    import balance
    import openterms
    import placement
    import bsupply
    import seat
    import importlib.util as _ilu
    # wave 3's owners, by path: docket68/wave3/corridor.py shares its name with the board's corridor.py.
    def _bypath(name, fname):
        spec = _ilu.spec_from_file_location(name, os.path.join(W3, fname))
        m = _ilu.module_from_spec(spec)
        spec.loader.exec_module(m)
        return m
    sys.path.append(W3)
    w3corridor = _bypath("w3corridor", "corridor.py")
    aperture = _bypath("w3aperture", "aperture.py")

SCHEDULES_S = aperture.SCHEDULES_S            # a day, a year, a century (Julian)
SCHEDULE_NAMES = ("1 day", "1 yr", "1 century")
YEAR_S = seat.YEAR_S


def counts():
    return balance.counts()


def atoms():
    return openterms.atoms()


def read_a(T):
    rt = openterms.read_terms()
    return {"bits_per_s": dict((n, b / T) for n, b in counts()), "atoms_per_s": atoms() / T,
            "theorem_floor_W": 0.0,
            "probe_floor_W_1A": dict((r["carrier"], r["total_J"] / T) for r in rt["probe_floor"]
                                     if r["delta_m"] == 1e-10)}


def channel(T):
    out = {}
    for n, b in counts():
        cf = seat.channel_floor(b, T)
        ap = [r for r in aperture.streamed() if r["count"] == n and r["T_s"] == T][0]
        out[n] = {"bits_per_s": b / T, "floor_W_one_pol": cf["E_1d_one_pol_J"] / T,
                  "floor_W_two_pol": cf["E_1d_two_pol_J"] / T, "floor_J_one_pol": cf["E_1d_one_pol_J"],
                  "opening_m": ap["width_m"], "quantum_eV": ap["kT_eV"]}
    return out


def coupling(T):
    return {"hbarJ_eV": dict((r["count"], r["hbarJ_eV"]) for r in aperture.coupling_view() if r["T_s"] == T),
            "before_light_hbarJ_eV_per_qubit": w3corridor.before_light()["hbarJ_min_eV_per_qubit"]}


def assemble_b(T):
    reset = dict((n, placement.dissipation_floor(b, balance.T_FLOOR) / T) for n, b in counts())
    return {"atoms_per_s": atoms() / T, "reset_floor_W": reset,
            "chem_ceiling_W": openterms.chem_ceiling_j() / T}


def power_b(T):
    """Collector area for B's local terms at eta = 1: the chemical ceiling (a ceiling) and the reset floor (largest
    count), at Faria's central and low L*."""
    F = bsupply.flux_b()
    a = assemble_b(T)
    reset_max = max(a["reset_floor_W"].values())
    return dict((k, {"area_chem_ceiling_m2": a["chem_ceiling_W"] / F[k], "area_reset_floor_m2": reset_max / F[k]})
                for k in ("central", "low"))


def stock_b():
    st = balance.stock_terms()
    return {"ci_feedstock_kg": st["ci_feedstock_kg"], "binder": st["ci_binder"][0],
            "P_measured_in_proxima_system": st["P_measured_in_proxima_system"]}


def crossover_T(carrier, count_index=0):
    """The schedule T* at which the 1 A probe read floor (energy E_r, so power E_r/T) equals the channel's
    received-power floor (energy E_c(T) = K/T under seat.channel_floor's 1D law, so power K/T^2): T* = K / E_r.
    Shorter than T*, the channel floor is the larger power; longer, the read floor is.  None if E_r = 0."""
    n, b = counts()[count_index]
    K = seat.channel_floor(b, YEAR_S)["E_1d_one_pol_J"] * YEAR_S
    Er = [r["total_J"] for r in openterms.read_terms()["probe_floor"]
          if r["delta_m"] == 1e-10 and r["carrier"] == carrier][0]
    return K / Er if Er > 0 else None


def demand_table():
    return [{"schedule": nm, "T_s": T, "read_a": read_a(T), "channel": channel(T), "coupling": coupling(T),
             "assemble_b": assemble_b(T), "power_b": power_b(T)} for nm, T in zip(SCHEDULE_NAMES, SCHEDULES_S)]


def collect():
    return {"schedules": demand_table(), "stock_b": stock_b(), "atoms": atoms(), "counts": counts(),
            "crossover_yr": dict((c, crossover_T(c) / YEAR_S) for c in ("photon", "electron", "neutron"))}


def report():
    d = collect()
    sp = counts()[0][0]
    fine = counts()[2][0]
    print("Step 1c -- what each subsystem must deliver (demand only; no supply is read here)")
    print("  object: %.4g atoms; counts: %s" % (d["atoms"], "; ".join("%s %.4g bits" % c for c in d["counts"])))
    for s in d["schedules"]:
        T = s["T_s"]
        print("\n  schedule %s (T = %.4g s; H-SCHEDULE, H-UNIFORM-RATE, H-PARALLEL)" % (s["schedule"], T))
        r = s["read_a"]
        print("    READ-A      %.3g bits/s (species) to %.3g (0.1 A); %.3g atoms/s; theorem floor 0 W; 1 A probe "
              "floors: photon %.3g W, electron %.3g W, neutron %.3g W"
              % (r["bits_per_s"][sp], r["bits_per_s"][fine], r["atoms_per_s"], r["probe_floor_W_1A"]["photon"],
                 r["probe_floor_W_1A"]["electron"], r["probe_floor_W_1A"]["neutron"]))
        c = s["channel"][sp]
        print("    CHANNEL     species: %.3g bits/s; received-power floor %.3g W (one pol.), %.3g W (two); "
              "opening >= %.3g m; quantum %.3g eV" % (c["bits_per_s"], c["floor_W_one_pol"], c["floor_W_two_pol"],
                                                     c["opening_m"], c["quantum_eV"]))
        cp = s["coupling"]
        print("    COUPLING    hbar J %.3g eV (species) for the whole object in T; before light needs > %.2g eV per "
              "qubit (H-LOCALITY clashes with every speed-free route)"
              % (cp["hbarJ_eV"][sp], cp["before_light_hbarJ_eV_per_qubit"]))
        a = s["assemble_b"]
        print("    ASSEMBLE-B  %.3g atoms/s; reset floor %.3g W (species) to %.3g W (0.1 A); chemical ceiling %.3g W"
              % (a["atoms_per_s"], a["reset_floor_W"][sp], a["reset_floor_W"][fine], a["chem_ceiling_W"]))
        p = s["power_b"]
        print("    POWER-B     collector for the chemical ceiling: %.3g m^2 (central L*), %.3g m^2 (low); for the reset "
              "floor: %.3g m^2" % (p["central"]["area_chem_ceiling_m2"], p["low"]["area_chem_ceiling_m2"],
                                   p["central"]["area_reset_floor_m2"]))
    print("\n  READ-A against CHANNEL (species count, H-PROBE at 1 A, H-ONE-POL): the channel's power floor falls as 1/T^2, "
          "the read floor as 1/T; the FLOORS cross at T* = %s years -- shorter than T*, the channel floor is the larger "
          "(floors only: the transmitted power is not established, seat.channel_floor)"
          % ", ".join("%.3g (%s)" % (v, k) for k, v in d["crossover_yr"].items()))
    st = d["stock_b"]
    print("\n  STOCK-B     %.1f kg CI feedstock, binder %s, measured in the Proxima system: %s (OPEN)"
          % (st["ci_feedstock_kg"], st["binder"], st["P_measured_in_proxima_system"]))
    print("  RETIRE-A    OUT-A-RESIDUE under H-RETIRE-A; its energy OPEN (openterms T2)")


def selftest():
    n_ok = n_bad = n_ctl = 0

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-96s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:96], got))

    print("demand.py selftest")
    d = collect()
    chk("the subsystems' owners are the step1b and wave-3 files themselves (by path, wave 3's corridor not the "
        "board's)", (os.path.dirname(balance.__file__) == S1B, os.path.dirname(w3corridor.__file__) == W3,
                     os.path.dirname(aperture.__file__) == W3), (True, True, True))
    chk("CONTROL: the collector expression gives 1 m^2 for 1361 W at the 1 au flux (to 1e-3)",
        abs(1361.0 / bsupply.flux(bsupply.L_SUN, bsupply.AU) - 1.0) < 1e-3, True, ctl=True)
    s = dict((x["schedule"], x) for x in d["schedules"])
    sp = counts()[0][0]
    cy = d["crossover_yr"]
    chk("the crossovers of the FLOORS, computed: photon between 10 and 11 yr, electron between 800 and 900 yr, "
        "neutron over 1e6 yr (printed: %.4g, %.4g, %.3g)" % (cy["photon"], cy["electron"], cy["neutron"]),
        (10 < cy["photon"] < 11, 800 < cy["electron"] < 900, cy["neutron"] > 1e6), (True, True, True))
    _cmp = [(nm, s[nm]["channel"][sp]["floor_W_one_pol"] > s[nm]["read_a"]["probe_floor_W_1A"]["photon"])
            for nm in SCHEDULE_NAMES]
    chk("  read off the table independently of T*: the channel floor exceeds the 1 A photon read floor at 1 day and "
        "1 yr, and not at 1 century", _cmp, [("1 day", True), ("1 yr", True), ("1 century", False)])
    chk("POWER-B: at 1 yr a collector of under 2 m^2 covers the chemical ceiling at both Faria cases (central %.3g, "
        "low %.3g m^2); at 1 day it takes over 400 m^2" % (s["1 yr"]["power_b"]["central"]["area_chem_ceiling_m2"],
                                                         s["1 yr"]["power_b"]["low"]["area_chem_ceiling_m2"]),
        (s["1 yr"]["power_b"]["low"]["area_chem_ceiling_m2"] < 2.0,
         s["1 day"]["power_b"]["central"]["area_chem_ceiling_m2"] > 400), (True, True))
    _cmp_bad = [(nm, s[nm]["channel"][sp]["floor_W_one_pol"] > 1e3 * s[nm]["read_a"]["probe_floor_W_1A"]["photon"])
                for nm in SCHEDULE_NAMES]
    chk("  CONTROL: the same comparison with the read floor raised 1000x no longer gives that pattern",
        _cmp_bad == [("1 day", True), ("1 yr", True), ("1 century", False)], False, ctl=True)
    print("  [STRUCTURAL] every rate is the owner's quantity over T, so rate x T returns it (H-SCHEDULE)")
    print("  [STRUCTURAL] READ-A's and ASSEMBLE-B's atoms/s are the same object's atoms over the same T")
    print("  [STRUCTURAL] POWER-B's 1 yr area equals bsupply.gather_time_s(E, F, 1 m^2) in years: both are E/(F T)")
    print("  [STRUCTURAL] the channel power floor scales as 1/T^2 (LNM eq. 8, closed form); at T* the two floors are "
          "equal and at 2T* their ratio is 2, by T*'s definition")
    print("\nHISTORY (Step 1c verifier, applied): the bsupply agreement and its LOW-L* control, the 1/T^2 scaling, "
          "and the equality at T* and its 2T* control were first COUNTED (9 checks, 3 controls); each is an identity "
          "or restates another check, and is now STRUCTURAL.  The STRUCTURAL count printed 2 over one line.")
    print("\n%d/%d checks pass, %d of them controls; 4 STRUCTURAL printed, not counted" % (n_ok, n_ok + n_bad, n_ctl))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
