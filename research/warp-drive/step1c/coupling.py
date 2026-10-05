#!/usr/bin/env python3
"""
coupling.py -- Step 1c on the coupling route: the wave-3 A-B coupling priced as the device's link, demand against
present supply READ at source.

Not seated.  M (rulings item 38): "Take the coupling route" -- the channel is set aside as the device's link and the
wave-3 coupling (docket68/wave3/corridor.py, H = J(|A><B| + |B><A|), transfer time pi/(2J)) is priced instead.  Every
demand figure is IMPORTED (corridor.py, aperture.py, balance.py via demand.py); every supply figure is READ (source,
place, route, a short phrase with the number); every carried figure is COMPUTED from the READ inputs.  Verified in both
directions on 2026-10-05; the findings are applied and the first-written claims kept under HISTORY.

    python3 coupling.py              report
    python3 coupling.py --selftest   checks, with CONTROLS
    python3 coupling.py --json       the numbers as JSON

THE DEMAND (two arrangements of the same transfer, I qubits in time T)
  PARALLEL  I pairs, each with its own direct coupling across L: J_pair = pi/(2T) per pair.
  SERIAL    one coupling carrying all I in turn: J = I pi/(2T) (aperture.coupling_view: 312 keV at a year, species).
WHAT LOCALITY BOUNDS (H-LOCALITY) -- TIME, NOT J
  corridor.signalling_coupled shows the coupling is a channel: under a FIXED J, A's starting state changes B's
  statistics.  An INSTANTANEOUS coupling across L therefore gives B the probability sin^2(J t) > 0 for every t < L/c and
  every J > 0 -- a signal outside the light cone.  So under microcausality an instantaneous coupling across spacelike L
  is excluded at EVERY J > 0, a coupling set up in advance included (H-PREESTABLISHED does not rescue it: A's state
  alone signals).  A RETARDED coupling is allowed at any J and completes no sooner than L/c.  Hence: schedules T < L/c
  are excluded whatever J is; T >= L/c needs a retarded coupling -- which, for the electromagnetic couplings measured,
  is photon exchange, i.e. the channel M set aside.  corridor.before_light's threshold J = pi c/(2L) is where an
  instantaneous coupling would COMPLETE before light; it is not a ceiling on J (printed STRUCTURAL).
THE SUPPLY, AND WHERE THE DIRECT LAW STOPS
  The direct couplings measured are near-field dipolar exchange, 1/R^3, valid for R small compared to the transition's
  wavelength (Barredo et al.'s electrostatic limit, 1408.1055v2 p.6); the boundary is lambda/(2 pi), where the 1/R^3 and
  1/R terms of the retarded resonant dipole-dipole interaction are equal.  Barredo's 9.131 GHz transition puts it at
  5.2 mm; Kotler et al.'s 12.34 MHz Larmor splitting at 3.9 m.  Beyond it the coupling is the retarded far-field term,
  J_far = 2 pi C3 k^2 / L (H-FAR-FIELD-ORIENTATION: the transverse-dipole maximum), which acts only after L/c -- photon
  exchange, the channel -- and decays by the excited state's lifetime (H-COHERENCE: no coherence time is priced
  elsewhere; Barredo's Rydberg states live about 100 us, READ).
  WHAT A NEAR-FIELD COUPLING AT L WOULD TAKE (computed): lambda/(2 pi) = L needs f = c/(2 pi L); the century J at L by
  near-field exchange needs a dipole d = sqrt(4 pi eps0 hbar J L^3) -- for charge e, a separation larger than L itself.

NAMED HYPOTHESES
  H-LOCALITY, H-PREESTABLISHED (named, and shown not to rescue an instantaneous coupling), H-NEAR-FIELD,
  H-FAR-FIELD-ORIENTATION, H-COHERENCE, H-POWER-LAW-CARRY (the formal 1/R^3 carry, outside its validity, kept as
  history), H-MEDIATOR-SPANS, H-DIRECT-COUPLING (wave 3), H-STATE-AS-BITS, and demand.py's (H-SCHEDULE,
  H-UNIFORM-RATE, H-PARALLEL).

ROUTES.  Read by this session's coupling reader (2026-10-05) via alphaXiv answer_pdf_queries; Barredo et al.
  1408.1055v2 RE-READ by the lead (C3, exponent, Eq. (1), the electrostatic-limit condition, the 9.131 GHz transition,
  the 101 and 135 us Rydberg lifetimes, the 0.52 MHz swap at 30 um); Kotler et al. 1312.4881v1 and Magnard et al.
  2008.01642v1 re-read by the coupling verifier (Kotler's B = 0.44 mT and 12.34 MHz splitting; Magnard's 28 ns is
  ESTIMATED from group velocities, p.3 S3).  Two ids in the reader's brief were wrong and are recorded: 1411.2879 is
  not Barredo (it is 1408.1055); Magnard et al. 2008.01642v1 is a 5 m link, not 30 m.

HISTORY (coupling verifier, 2026-10-05; first-written claims kept):
  * First stated 'J <= pi c/(2L)' as a LOCALITY CEILING on J, with 'a 1 yr schedule needs 4.25x the ceiling' and 'a
    century 0.0425x: not excluded', citing 'on/off keying' -- corridor.signalling_coupled varies A's state under a fixed
    J, not J itself.  An instantaneous coupling at the century J already gives B 4.4e-3 by L/c: locality bounds T, not
    J, and excludes an instantaneous coupling at every J.  'A century is not excluded' is WITHDRAWN for an
    instantaneous coupling; for a retarded one it holds, as the channel.
  * First printed the best direct coupling carried to L by 1/R^3 as 7.7e-58 rad/s, 6.5e47 short of the century demand.
    Outside its validity, and it understated the coupling: the retarded far-field term is (kL)^2 = 5.9e37 larger,
    J_far = 4.6e-20 rad/s, 1.1e10 short -- and retarded, and void over years at a 100 us lifetime.
  * First said no present mechanism couples two qubits directly beyond millimetres; the measured range is <= 50 um, and
    Kotler's near-field range is 3.9 m.  Replaced by the measured range and the dipole argument.
  * Counted as checks: the ceiling = before_light (one formula, an identity); three restatements of (L/c)/T; a CONTROL
    duplicating one; Magnard 'propagated below c' (estimated from group velocities, below c by construction).  Moved
    to STRUCTURAL or dropped.  The 0.52 MHz reproduction had no READ record; it has one now.
  * A guessed threshold ('L is 1e19 times the near-field limit or more') failed at 7.7e18 -- a guess, not a finding.
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
E_CHARGE = 1.602176634e-19
EPS0 = 8.8541878128e-12              # CODATA 2018
L = demand.w3corridor.before_light()["L_m"]
YEAR_S = demand.YEAR_S

# ============================================================================ READ: supply
SUPPLY = {
    "Rydberg_Barredo2015": {
        "source": "arXiv:1408.1055v2 (Barredo et al.)", "route": "READ via alphaXiv answer_pdf_queries, pp.1-3, 6 "
        "(coupling reader; re-read by the lead)", "kind": "measured", "mediator": "direct (electric dipole, near field)",
        "C3_Hz_um3": 7950e6, "C3_err_Hz_um3": 130e6, "exponent": (-2.93, 0.20), "r_max_um": 50.0,
        "transition_Hz": 9.131e9, "lifetimes_s": (101e-6, 135e-6), "R_calibration": 0.05,
        "swap_at_30um_Hz": 0.52e6, "phrase": "C3exp = 7950 +- 130 MHz um3",
        "phrase_swap": "with a frequency 2E/h = 0.52 MHz",
        "phrase_limit": "small compared to the wavelength of the relevant transitions",
        "hamiltonian": "per pair C3/R^3 (|ud><du| + h.c.); swap oscillation at 2E/h with E = C3/R^3, so J = 2 pi C3/R^3"},
    "Rydberg_Ravets2014": {
        "source": "arXiv:1405.7804v1 (Ravets et al.)", "route": "READ via alphaXiv answer_pdf_queries, p.3, Fig. 3c "
        "(coupling reader)", "kind": "measured (Forster resonance)", "mediator": "direct (electric dipole)",
        "C3_Hz_um3": 2.39e9, "exponent": (-3.0, 0.1), "r_max_um": 15.0, "phrase": "C3 = 2.39 +- 0.03 GHz um3"},
    "ions_magnetic_Kotler2014": {
        "source": "arXiv:1312.4881v1 (Kotler et al.)", "route": "READ via alphaXiv answer_pdf_queries, pp.6, 10, 12 "
        "(coupling reader; re-read, with the field and splitting, by the coupling verifier)", "kind": "measured",
        "mediator": "direct (magnetic dipole)", "xi_Hz": 0.9e-3, "r_um": 2.4, "exponent": (-3.0, 0.4),
        "larmor_Hz": 12.34e6, "B_T": 0.44e-3, "phrase": "yielding xi = 0.9(1) mHz",
        "hamiltonian": "H = 2 hbar xi (|ud><du| + h.c.), so J = 2 xi = 2 pi x 1.8 mHz"},
    "ions_phonon_Richerme2014": {
        "source": "arXiv:1401.5088v1 (Richerme et al.)", "route": "READ via alphaXiv answer_pdf_queries, pp.2, 5 "
        "(coupling reader)", "kind": "measured alpha 0.63-1.19; 0-3 claimed", "mediator": "phonons of the ion crystal",
        "J_max_Hz": 400.0, "alpha": (0.63, 0.83, 1.00, 1.19), "phrase": "J_max ~ 400 Hz",
        "note": "ion spacing not stated, so not carried; mediated: the crystal must span L (H-MEDIATOR-SPANS)"},
    "remote_Magnard2020": {
        "source": "arXiv:2008.01642v1 (Magnard et al.)", "route": "READ via alphaXiv answer_pdf_queries, pp.2-3 "
        "(coupling reader; re-read by the coupling verifier)",
        "kind": "measured sequence; the 28 ns propagation ESTIMATED from group velocities (p.3, S3)",
        "mediator": "propagating microwave photon (a channel)",
        "link_m_without_circulator": 4.9 + 2 * 0.4, "propagation_s_estimated": 28e-9, "sequence_s": 311e-9,
        "process_fidelity": 0.795, "phrase": "propagates to node B in 28 ns"},
}


# ============================================================================ demand
def threshold_J():
    """corridor.before_light's threshold: an INSTANTANEOUS coupling with J = pi c/(2L) would complete at L/c."""
    J = math.pi * C / (2.0 * L)
    return {"J_rad_s": J, "hbarJ_eV": HBAR * J / EV, "light_time_s": L / C}


def demand_rows():
    out = []
    for nm, T in zip(demand.SCHEDULE_NAMES, demand.SCHEDULES_S):
        Jp = math.pi / (2.0 * T)
        for n, b in demand.counts()[:1] + demand.counts()[2:3]:
            Js = b * math.pi / (2.0 * T)
            out.append({"schedule": nm, "T_s": T, "count": n, "pairs": b, "T_over_light_time": T / (L / C),
                        "J_pair_rad_s": Jp, "J_serial_rad_s": Js, "hbarJ_serial_eV": HBAR * Js / EV})
    return out


def instantaneous_signal(J, t=None):
    """B's probability sin^2(J t) under an instantaneous coupling, at t = L/c by default (corridor.py's model)."""
    t = L / C if t is None else t
    return math.sin(J * t) ** 2


# ============================================================================ supply
def J_rydberg(r_m, C3=None):
    """Near field: J (rad/s) = 2 pi C3 / R^3, C3 in Hz um^3 (Barredo Eq. (1), Fig. 2)."""
    C3 = SUPPLY["Rydberg_Barredo2015"]["C3_Hz_um3"] if C3 is None else C3
    return 2.0 * math.pi * C3 / (r_m * 1e6) ** 3


def J_far_rydberg(r_m):
    """Far field (retarded, transverse maximum): J = 2 pi C3 k^2 / R, k = 2 pi f / c (H-FAR-FIELD-ORIENTATION)."""
    b = SUPPLY["Rydberg_Barredo2015"]
    k = 2.0 * math.pi * b["transition_Hz"] / C
    return 2.0 * math.pi * (b["C3_Hz_um3"] * 1e-18) * k * k / r_m


def near_field_limit_m(f_Hz):
    """lambda / (2 pi): beyond it a dipole coupling is radiative (H-NEAR-FIELD)."""
    return C / f_Hz / (2.0 * math.pi)


def dipole_needed(J):
    """The electric dipole whose near-field exchange at L gives J: d = sqrt(4 pi eps0 hbar J L^3); and, for charge e,
    the separation d/e."""
    d = math.sqrt(4.0 * math.pi * EPS0 * HBAR * J * L ** 3)
    return {"d_Cm": d, "separation_m": d / E_CHARGE, "separation_over_L": d / E_CHARGE / L}


def supply_rows():
    b = SUPPLY["Rydberg_Barredo2015"]
    k = SUPPLY["ions_magnetic_Kotler2014"]
    return {"rydberg_J_at_rmax_rad_s": J_rydberg(b["r_max_um"] * 1e-6),
            "rydberg_near_field_limit_m": near_field_limit_m(b["transition_Hz"]),
            "kotler_near_field_limit_m": near_field_limit_m(k["larmor_Hz"]),
            "rydberg_J_far_at_L_rad_s": J_far_rydberg(L),
            "rydberg_decay_rate_s": 1.0 / b["lifetimes_s"][0],
            "rydberg_ln_survival_century": -demand.SCHEDULES_S[2] / b["lifetimes_s"][0],
            "formal_near_field_at_L_rad_s": J_rydberg(L),
            "kotler_J_rad_s": 2.0 * (2.0 * math.pi * k["xi_Hz"]),
            "f_near_field_at_L_Hz": C / (2.0 * math.pi * L)}


def collect():
    cen = [r for r in demand_rows() if r["schedule"] == "1 century"][0]
    return {"threshold": threshold_J(), "demand": demand_rows(), "supply": supply_rows(), "READ": SUPPLY,
            "instantaneous_signal_at_light_time_century_J": instantaneous_signal(cen["J_pair_rad_s"]),
            "dipole_needed_century": dipole_needed(cen["J_pair_rad_s"])}


def report():
    d = collect()
    th = d["threshold"]
    print("Step 1c, coupling route -- demand, what locality bounds, and present supply READ at source")
    print("  L = %.4g m, light time L/c = %.4g yr; corridor.before_light's threshold pi c/2L = %.3g rad/s (hbar J = "
          "%.3g eV): where an instantaneous coupling would COMPLETE before light" % (L, th["light_time_s"] / YEAR_S,
                                                                                    th["J_rad_s"], th["hbarJ_eV"]))
    for r in d["demand"]:
        print("  %-10s %-26s pairs %.3g, T = %.3g x L/c: J per pair %.3g rad/s; serial J %.3g rad/s = %.3g eV"
              % (r["schedule"], r["count"][:26], r["pairs"], r["T_over_light_time"], r["J_pair_rad_s"],
                 r["J_serial_rad_s"], r["hbarJ_serial_eV"]))
    print("  LOCALITY BOUNDS TIME, NOT J: an instantaneous coupling at the century J already gives B %.2g by L/c -- a "
          "signal outside the light cone, excluded at every J > 0; a retarded coupling completes at >= L/c (T < L/c "
          "excluded at any J)" % d["instantaneous_signal_at_light_time_century_J"])
    sp = d["supply"]
    print("\n  SUPPLY (direct couplings, measured to <= 50 um; 1/R^3 near-field law):")
    print("    Rydberg exchange (Barredo, C3 = 7950 MHz um^3): J = %.3g rad/s at 50 um; near-field limit lambda/2pi at "
          "9.131 GHz = %.3g m" % (sp["rydberg_J_at_rmax_rad_s"], sp["rydberg_near_field_limit_m"]))
    print("    magnetic dipole (Kotler, J = %.3g rad/s at 2.4 um): near-field limit at the 12.34 MHz splitting = %.3g m"
          % (sp["kotler_J_rad_s"], sp["kotler_near_field_limit_m"]))
    cen = [r for r in d["demand"] if r["schedule"] == "1 century"][0]
    print("    beyond the limit, the retarded far-field term at L: J_far = %.3g rad/s -- %.2g short of the century "
          "demand per pair (%.3g), acting only after L/c (photon exchange: the channel)"
          % (sp["rydberg_J_far_at_L_rad_s"], cen["J_pair_rad_s"] / sp["rydberg_J_far_at_L_rad_s"], cen["J_pair_rad_s"]))
    print("    and void over years: the Rydberg state decays at %.3g /s (%.2g x J_far); ln survival over a century %.3g "
          "(H-COHERENCE)" % (sp["rydberg_decay_rate_s"], sp["rydberg_decay_rate_s"] / sp["rydberg_J_far_at_L_rad_s"],
                             sp["rydberg_ln_survival_century"]))
    dn = d["dipole_needed_century"]
    print("    a near-field coupling AT L: needs f <= %.3g Hz (lambda/2pi = L), and for the century J a dipole of %.3g C m "
          "-- charge e separated by %.3g m = %.2g L" % (sp["f_near_field_at_L_Hz"], dn["d_Cm"], dn["separation_m"],
                                                      dn["separation_over_L"]))
    print("    mediated: phonon-coupled ions (alpha 0.63-1.19 measured) need the crystal to span L, spacing not read; "
          "photon-mediated remote transfer (Magnard, 5 m) is a channel")
    print("    history: the formal 1/R^3 carry to L gave %.3g rad/s (outside its validity; the far field is (kL)^2 larger)"
          % sp["formal_near_field_at_L_rad_s"])


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
    sp = d["supply"]
    cen = [r for r in d["demand"] if r["schedule"] == "1 century"][0]
    sig = d["instantaneous_signal_at_light_time_century_J"]
    chk("an instantaneous coupling at the century J gives B a probability over 1e-3 by L/c (%.3g): a signal outside "
        "the light cone, so H-LOCALITY excludes it at that J too" % sig, sig > 1e-3, True)
    chk("  CONTROL: with J = 0 B gets nothing (the signal is the coupling's)", instantaneous_signal(0.0), 0.0, ctl=True)
    b = SUPPLY["Rydberg_Barredo2015"]
    _tol = (1.0 + b["R_calibration"]) ** 3 - 1.0
    _pred = 2 * J_rydberg(30e-6) / (2 * math.pi)
    chk("Barredo's measured swap at 30 um (READ, %.2g MHz) reproduced from the READ C3 within the paper's 5%% R "
        "calibration (%.1f%% in E): %.3g MHz" % (b["swap_at_30um_Hz"] / 1e6, 100 * _tol, _pred / 1e6),
        abs(_pred / b["swap_at_30um_Hz"] - 1) < _tol, True)
    chk("the near-field limits, computed from the READ frequencies: millimetres at 9.131 GHz (%.3g m), metres at "
        "12.34 MHz (%.3g m); L is over 1e16 times either" % (sp["rydberg_near_field_limit_m"],
                                                             sp["kotler_near_field_limit_m"]),
        (1e-3 < sp["rydberg_near_field_limit_m"] < 1e-2, 1 < sp["kotler_near_field_limit_m"] < 10,
         L / sp["kotler_near_field_limit_m"] > 1e16), (True, True, True))
    _short = cen["J_pair_rad_s"] / sp["rydberg_J_far_at_L_rad_s"]
    chk("the retarded far-field coupling at L (%.3g rad/s) is between 1e9 and 1e11 short of the century demand per "
        "pair (%.3g)" % (sp["rydberg_J_far_at_L_rad_s"], _short), 1e9 < _short < 1e11, True)
    chk("  CONTROL: at the 50 um where it was measured the near-field coupling exceeds the century demand",
        sp["rydberg_J_at_rmax_rad_s"] > cen["J_pair_rad_s"], True, ctl=True)
    chk("over years the far-field coupling is void: the Rydberg decay rate exceeds it by over 1e20 (%.3g)"
        % (sp["rydberg_decay_rate_s"] / sp["rydberg_J_far_at_L_rad_s"]),
        sp["rydberg_decay_rate_s"] / sp["rydberg_J_far_at_L_rad_s"] > 1e20, True)
    dn = d["dipole_needed_century"]
    chk("a near-field exchange giving the century J at L needs a dipole whose charge-e separation exceeds L itself "
        "(%.2g L)" % dn["separation_over_L"], dn["separation_over_L"] > 1.0, True)
    chk("every READ record names a source, route, kind and mediator; every phrase under 15 words",
        ([k for k, v in SUPPLY.items() if not all(v.get(f) for f in ("source", "route", "kind", "mediator"))],
         [k for k, v in SUPPLY.items() for f in ("phrase", "phrase_limit", "phrase_swap")
          if f in v and len(v[f].split()) >= 15]), ([], []))
    print("  [STRUCTURAL] J_pair = pi/(2T) and J_serial = I pi/(2T): the transfer time of H = J(|A><B| + h.c.) set to T")
    print("  [STRUCTURAL] before_light's pi c/2L is the demand pi/(2T) at T = L/c (the same formula, the same constants)")
    print("  [STRUCTURAL] J_far / J_near at the same R is (kR)^2: the two terms are equal at lambda/2pi by definition")
    print("\n%d/%d checks pass, %d of them controls; 3 STRUCTURAL printed, not counted" % (n_ok, n_ok + n_bad, n_ctl))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
