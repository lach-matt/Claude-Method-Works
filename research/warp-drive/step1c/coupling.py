#!/usr/bin/env python3
"""
coupling.py -- Step 1c on the coupling route: the wave-3 A-B coupling priced as the device's link, demand against
present supply READ at source.

Not seated.  M (rulings item 38): "Take the coupling route" -- the channel is set aside as the device's link and the
wave-3 coupling (docket68/wave3/corridor.py, H = J(|A><B| + |B><A|), transfer time pi/(2J)) is priced instead.  Every
demand figure is IMPORTED (corridor.py, aperture.py, balance.py via demand.py); every supply figure is READ (source,
place, route, a short phrase with the number); every carried figure is COMPUTED from the READ inputs.

    python3 coupling.py              report
    python3 coupling.py --selftest   checks, with CONTROLS
    python3 coupling.py --json       the numbers as JSON

THE DEMAND (two arrangements of the same transfer, I qubits in time T)
  PARALLEL  I pairs, each with its own direct coupling across L: J_pair = pi/(2T) per pair.
  SERIAL    one coupling carrying all I in turn: J = I pi/(2T) (aperture.coupling_view: 312 keV at a year, species).
THE LOCALITY CEILING (H-LOCALITY)
  corridor.py shows a coupling is a channel (on/off keying moves the far side's statistics).  Under H-LOCALITY no
  channel completes across L in less than L/c, so pi/(2J) >= L/c, i.e. J <= pi c/(2L) per coupling -- which is
  corridor.before_light's threshold read the other way: the coupling route beats light iff it exceeds the locality
  ceiling.  Under H-LOCALITY the PARALLEL arrangement at the ceiling completes in exactly L/c (the light time), with
  I direct couplings each spanning L; the SERIAL one exceeds the ceiling by I L/(c T).
  A quasi-static coupling (the dipolar fields below) is the non-retarded limit of a field that travels at c: across L it
  exists only after L/c from switch-on (H-PREESTABLISHED: a coupling in place before the transfer begins).
THE SUPPLY
  The best measured J at a measured separation r for each mechanism, carried to L by the mechanism's own power law,
  J(L) = J0 (r0/L)^alpha (H-POWER-LAW-CARRY: the law the source states, held to 4.02e16 m -- far outside any range
  measured; a mediated coupling also needs its mediator to span L, H-MEDIATOR-SPANS).

THE NEAR-FIELD LIMIT (READ, and the finding that decides the supply)
  The direct couplings measured -- resonant electric dipole-dipole between Rydberg atoms, magnetic dipole between two
  ions -- are the quasi-static (near-field) limit of the electromagnetic interaction.  Barredo et al.'s supplement
  states the 1/R^3 form holds for R small compared to the wavelength of the transition (the electrostatic limit;
  1408.1055v2 p.6).  Their transition is at 9.131 GHz (p.2), lambda = c/f = 3.3 cm.  Beyond about lambda/(2 pi) the
  coupling is carried by radiation -- a propagating photon, which is the channel M set aside (item 38), bounded by
  L/c.  So H-POWER-LAW-CARRY to 4.02e16 m is outside the law's own stated validity; the carried figure is printed as
  FORMAL only (an upper bound on what the near-field law could give, if it held, which it does not).

NAMED HYPOTHESES
  H-LOCALITY, H-PREESTABLISHED, H-POWER-LAW-CARRY, H-NEAR-FIELD (R << lambda/(2 pi) for a quasi-static coupling),
  H-MEDIATOR-SPANS, H-DIRECT-COUPLING (wave 3), H-STATE-AS-BITS (one qubit per bit of the count), and demand.py's
  (H-SCHEDULE, H-UNIFORM-RATE, H-PARALLEL).

ROUTES.  Read by this session's coupling reader (2026-10-05) via alphaXiv answer_pdf_queries; Barredo et al.
  1408.1055v2 RE-READ by the lead (C3, exponent, Eq. (1), the electrostatic-limit condition, the 9.131 GHz transition).
  Two ids in the reader's brief were wrong and are recorded: 1411.2879 is not Barredo (it is 1408.1055); Magnard et
  al. 2008.01642v1 is a 5 m link, not 30 m.
"""
import contextlib
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()):
    import demand

C = demand.seat.C
HBAR = demand.aperture.HBAR
EV = 1.602176634e-19
L = demand.w3corridor.before_light()["L_m"]
YEAR_S = demand.YEAR_S


def ceiling_J():
    """The locality ceiling on one coupling across L: J = pi c / (2 L), rad/s; and hbar J in eV."""
    J = math.pi * C / (2.0 * L)
    return {"J_rad_s": J, "hbarJ_eV": HBAR * J / EV, "light_time_s": L / C}


def demand_rows():
    out = []
    ceil = ceiling_J()["J_rad_s"]
    for nm, T in zip(demand.SCHEDULE_NAMES, demand.SCHEDULES_S):
        Jp = math.pi / (2.0 * T)
        for n, b in demand.counts()[:1] + demand.counts()[2:3]:
            Js = b * math.pi / (2.0 * T)
            out.append({"schedule": nm, "T_s": T, "count": n, "pairs": b,
                        "J_pair_rad_s": Jp, "J_pair_over_ceiling": Jp / ceil,
                        "J_serial_rad_s": Js, "hbarJ_serial_eV": HBAR * Js / EV,
                        "J_serial_over_ceiling": Js / ceil})
    return out


# ============================================================================ READ: supply
SUPPLY = {
    "Rydberg_Barredo2015": {
        "source": "arXiv:1408.1055v2 (Barredo et al.)", "route": "READ via alphaXiv answer_pdf_queries, pp.1-2, 6 "
        "(coupling reader; re-read by the lead)", "kind": "measured", "mediator": "direct (electric dipole, near field)",
        "C3_Hz_um3": 7950e6, "C3_err_Hz_um3": 130e6, "exponent": (-2.93, 0.20), "r_max_um": 50.0,
        "transition_Hz": 9.131e9, "phrase": "C3exp = 7950 +- 130 MHz um3",
        "phrase_limit": "small compared to the wavelength of the relevant transitions",
        "hamiltonian": "per pair C3/R^3 (|ud><du| + h.c.); swap oscillation at 2E/h with E = C3/R^3, so J = 2 pi C3/R^3"},
    "Rydberg_Ravets2014": {
        "source": "arXiv:1405.7804v1 (Ravets et al.)", "route": "READ via alphaXiv answer_pdf_queries, p.3, Fig. 3c "
        "(coupling reader)", "kind": "measured (Forster resonance)", "mediator": "direct (electric dipole)",
        "C3_Hz_um3": 2.39e9, "exponent": (-3.0, 0.1), "r_max_um": 15.0, "phrase": "C3 = 2.39 +- 0.03 GHz um3"},
    "ions_magnetic_Kotler2014": {
        "source": "arXiv:1312.4881v1 (Kotler et al.)", "route": "READ via alphaXiv answer_pdf_queries, pp.6, 10, 12 "
        "(coupling reader)", "kind": "measured", "mediator": "direct (magnetic dipole)",
        "xi_Hz": 0.9e-3, "r_um": 2.4, "exponent": (-3.0, 0.4), "phrase": "yielding xi = 0.9(1) mHz",
        "hamiltonian": "H = 2 hbar xi (|ud><du| + h.c.), so J = 2 xi = 2 pi x 1.8 mHz",
        "note": "the qubit transition frequency (which sets this coupling's near-field range) was not read: OPEN"},
    "ions_phonon_Richerme2014": {
        "source": "arXiv:1401.5088v1 (Richerme et al.)", "route": "READ via alphaXiv answer_pdf_queries, pp.2, 5 "
        "(coupling reader)", "kind": "measured alpha 0.63-1.19; 0-3 claimed", "mediator": "phonons of the ion crystal",
        "J_max_Hz": 400.0, "alpha": (0.63, 0.83, 1.00, 1.19), "phrase": "J_max ~ 400 Hz",
        "note": "ion spacing not stated, so not carried; mediated: the crystal must span L (H-MEDIATOR-SPANS)"},
    "remote_Magnard2020": {
        "source": "arXiv:2008.01642v1 (Magnard et al.)", "route": "READ via alphaXiv answer_pdf_queries, pp.2-3 "
        "(coupling reader)", "kind": "measured", "mediator": "propagating microwave photon (a channel)",
        "link_m": 4.9 + 2 * 0.4, "propagation_s": 28e-9, "sequence_s": 311e-9, "process_fidelity": 0.795,
        "phrase": "propagates to node B in 28 ns"},
}


def J_rydberg(r_m, C3=None):
    """J (rad/s) = 2 pi C3 / R^3, C3 in Hz um^3 (Barredo Eq. (1), Fig. 2)."""
    C3 = SUPPLY["Rydberg_Barredo2015"]["C3_Hz_um3"] if C3 is None else C3
    return 2.0 * math.pi * C3 / (r_m * 1e6) ** 3


def near_field_limit_m(f_Hz):
    """lambda / (2 pi): beyond it a dipole coupling is radiative (H-NEAR-FIELD)."""
    return C / f_Hz / (2.0 * math.pi)


def supply_rows():
    b = SUPPLY["Rydberg_Barredo2015"]
    k = SUPPLY["ions_magnetic_Kotler2014"]
    m = SUPPLY["remote_Magnard2020"]
    r_nf = near_field_limit_m(b["transition_Hz"])
    J_k0 = 2.0 * (2.0 * math.pi * k["xi_Hz"])
    return {"rydberg_J_at_rmax_rad_s": J_rydberg(b["r_max_um"] * 1e-6),
            "rydberg_near_field_limit_m": r_nf, "rydberg_J_at_near_field_limit_rad_s": J_rydberg(r_nf),
            "rydberg_J_formal_at_L_rad_s": J_rydberg(L),
            "kotler_J_rad_s": J_k0, "kotler_J_formal_at_L_rad_s": J_k0 * (k["r_um"] * 1e-6 / L) ** 3,
            "magnard_speed_over_c": m["link_m"] / m["propagation_s"] / C,
            "magnard_transfer_at_L_s_min": L / C}


def collect():
    return {"ceiling": ceiling_J(), "demand": demand_rows(), "before_light": demand.w3corridor.before_light(),
            "supply": supply_rows(), "READ": SUPPLY,
            "locality_threshold_T_yr": ceiling_J()["light_time_s"] / YEAR_S}


def report():
    d = collect()
    c = d["ceiling"]
    print("Step 1c, coupling route -- demand against the locality ceiling, and present supply READ at source")
    print("  locality ceiling on one coupling across L = %.4g m: J = pi c/2L = %.3g rad/s, hbar J = %.3g eV; "
          "transfer >= L/c = %.4g yr" % (L, c["J_rad_s"], c["hbarJ_eV"], c["light_time_s"] / YEAR_S))
    for r in d["demand"]:
        print("  %-10s %-26s pairs %.3g: J per pair %.3g rad/s (%.3gx the ceiling); serial J %.3g rad/s = %.3g eV "
              "(%.3gx the ceiling)" % (r["schedule"], r["count"][:26], r["pairs"], r["J_pair_rad_s"],
                                       r["J_pair_over_ceiling"], r["J_serial_rad_s"], r["hbarJ_serial_eV"],
                                       r["J_serial_over_ceiling"]))
    print("  so under H-LOCALITY: PARALLEL needs T >= L/c = %.4g yr (a 1 yr schedule needs 4.25x the ceiling; a century "
          "0.0425x); SERIAL exceeds it at every schedule, by I L/(c T)" % d["locality_threshold_T_yr"])
    sp = d["supply"]
    print("\n  SUPPLY (direct couplings, measured; 1/R^3 near-field law):")
    print("    Rydberg exchange (Barredo, C3 = 7950 MHz um^3, measured to 50 um): J = %.3g rad/s at 50 um"
          % sp["rydberg_J_at_rmax_rad_s"])
    print("    its near-field limit lambda/2pi at 9.131 GHz = %.3g m, where J = %.3g rad/s; beyond it the coupling is a "
          "photon (the channel)" % (sp["rydberg_near_field_limit_m"], sp["rydberg_J_at_near_field_limit_rad_s"]))
    print("    FORMAL carry to L (outside the law's validity): Rydberg %.3g rad/s; magnetic dipole (Kotler, J = %.3g rad/s "
          "at 2.4 um) %.3g rad/s" % (sp["rydberg_J_formal_at_L_rad_s"], sp["kotler_J_rad_s"],
                                     sp["kotler_J_formal_at_L_rad_s"]))
    cen = [r for r in d["demand"] if r["schedule"] == "1 century"][0]
    print("    against the locality-compatible century demand (%.3g rad/s per pair): the formal Rydberg figure is %.2g "
          "times short" % (cen["J_pair_rad_s"], cen["J_pair_rad_s"] / sp["rydberg_J_formal_at_L_rad_s"]))
    print("    phonon-mediated ion couplings (alpha 0.63-1.19 measured): no spacing read, not carried; the crystal must "
          "span L")
    print("    photon-mediated remote transfer (Magnard, 5.7 m in 28 ns = %.2f c): a channel, >= L/c = %.4g yr at L"
          % (sp["magnard_speed_over_c"], sp["magnard_transfer_at_L_s_min"] / YEAR_S))


def selftest():
    n_ok = n_bad = n_ctl = 0

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-96s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:96], got))

    print("coupling.py selftest")
    d = collect()
    c = d["ceiling"]
    bl = demand.w3corridor.before_light()["hbarJ_min_eV_per_qubit"]
    chk("the locality ceiling equals corridor.before_light's threshold, asked of the owner (to 1e-9): the coupling "
        "route beats light iff it exceeds the ceiling", abs(c["hbarJ_eV"] / bl - 1.0) < 1e-9, True)
    by = dict(((r["schedule"], r["count"][:7]), r) for r in d["demand"])
    chk("PARALLEL under H-LOCALITY: a 1 yr schedule exceeds the ceiling (%.3gx) and a century does not (%.3gx); the "
        "threshold is L/c = %.3g yr" % (by[("1 yr", "species")]["J_pair_over_ceiling"],
                                        by[("1 century", "species")]["J_pair_over_ceiling"],
                                        d["locality_threshold_T_yr"]),
        (by[("1 yr", "species")]["J_pair_over_ceiling"] > 1, by[("1 century", "species")]["J_pair_over_ceiling"] < 1,
         4.2 < d["locality_threshold_T_yr"] < 4.3), (True, True, True))
    chk("SERIAL exceeds the ceiling at every schedule and count (by over 1e26)",
        all(r["J_serial_over_ceiling"] > 1e26 for r in d["demand"]), True)
    chk("  CONTROL: a SERIAL coupling carrying one qubit (I = 1) over a century is under the ceiling",
        (math.pi / (2.0 * demand.SCHEDULES_S[2])) / c["J_rad_s"] < 1, True, ctl=True)
    b = SUPPLY["Rydberg_Barredo2015"]
    # The tolerance is the paper's own: a 5% systematic on R (Barredo Fig. 2c caption, READ) is 1.05^3 - 1 = 15.8%
    # on C3/R^3.
    _tol = 1.05 ** 3 - 1.0
    chk("Barredo's measured point reproduced from the READ C3: J at 30 um gives a swap oscillation 2E/h within the "
        "paper's 5%% R calibration (%.1f%% in E) of the READ 0.52 MHz (%.3g MHz)"
        % (100 * _tol, 2 * J_rydberg(30e-6) / (2 * math.pi) / 1e6),
        abs(2 * J_rydberg(30e-6) / (2 * math.pi) / 1e6 / 0.52 - 1) < _tol, True)
    sp = d["supply"]
    # HISTORY: first asserted 'L is 1e19 times the limit or more'; it is 7.7e18 -- a guessed threshold failed, not a
    # finding.  The ratio is now printed and checked against 1e18.
    chk("the near-field limit at 9.131 GHz is millimetres (%.3g m); L is %.2g times it (over 1e18)"
        % (sp["rydberg_near_field_limit_m"], L / sp["rydberg_near_field_limit_m"]),
        (1e-3 < sp["rydberg_near_field_limit_m"] < 1e-2, L / sp["rydberg_near_field_limit_m"] > 1e18), (True, True))
    cen = by[("1 century", "species")]
    chk("even FORMALLY (outside its validity) the best direct coupling carried to L is over 1e40 short of the century "
        "demand per pair (%.2g)" % (cen["J_pair_rad_s"] / sp["rydberg_J_formal_at_L_rad_s"]),
        cen["J_pair_rad_s"] / sp["rydberg_J_formal_at_L_rad_s"] > 1e40, True)
    chk("  CONTROL: at the 50 um where it was measured the same coupling exceeds the century demand",
        sp["rydberg_J_at_rmax_rad_s"] > cen["J_pair_rad_s"], True, ctl=True)
    chk("the photon-mediated remote transfer propagated below c (%.2f c): a channel, bounded by L/c"
        % sp["magnard_speed_over_c"], 0 < sp["magnard_speed_over_c"] <= 1, True)
    chk("every READ record names a source, route, kind and mediator; every phrase under 15 words",
        ([k for k, v in SUPPLY.items() if not all(v.get(f) for f in ("source", "route", "kind", "mediator"))],
         [k for k, v in SUPPLY.items() for f in ("phrase", "phrase_limit") if f in v and len(v[f].split()) >= 15]),
        ([], []))
    print("  [STRUCTURAL] J_pair = pi/(2T) and J_serial = I pi/(2T): the transfer time of H = J(|A><B| + h.c.) set to T")
    print("  [STRUCTURAL] the ceiling pi c/2L is the demand pi/(2T) at T = L/c")
    print("\n%d/%d checks pass, %d of them controls; 2 STRUCTURAL printed, not counted" % (n_ok, n_ok + n_bad, n_ctl))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
