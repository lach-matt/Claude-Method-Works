#!/usr/bin/env python3
"""
localclock.py -- H-LOCAL-CLOCK: a clock at each position, relative to the matter-based observation there; conscious
observation as a perception of matter-observed time.

Seated in ledger.py section 8g (M-RULINGS item 54; first written "Not seated"); verified once (2026-10-05), its findings applied; first-written claims kept under HISTORY.  M (rulings item 52): "time is always relative, so the clock of the observer doesn't matter
in the second position, as time may move differently in the second position compared to the first. The clock is always
present relative to the position of measurement within its plane/dimension The clock is relative to the matter-based
observation. Consciousness observation is a perception of matter-observed time."  Carried as M's hypothesis
H-LOCAL-CLOCK, never as a result.  M (item 53): "READ, then model" -- READ done (2026-10-05); this is the model.

    python3 localclock.py              report
    python3 localclock.py --selftest   checks, with CONTROLS
    python3 localclock.py --json       the numbers as JSON

WHAT IS COMPUTED
  (1) The two local clocks.  Weak field (H-WEAK-FIELD): d tau / dt = 1 - Phi/c^2 - v^2/(2 c^2), each clock against a
      distant observer at rest with its OWN star (H-OWN-STAR-FRAME).  A: Earth's orbit (GM_sun, IAU 2015 B3, READ; 1 AU).
      B: Proxima b's orbit (Faria 2022's M_star and a, READ via seat.py).  For any Keplerian orbit <1/r> = 1/a and <v^2>
      = GM/a, so the secular offset is exactly 1.5 GM/(a c^2) (H-CIRCULAR costs nothing for the mean rate).  Checked
      against IAU L_C (READ), which includes every body; the potential term alone misses it (control).  The difference
      in seconds per year, with the error from M_star alone (a by Kepler III, H-KEPLER-A).  Terms of the size of that
      error bar are printed and left out (H-ORBIT-ONLY): Earth's own potential and rotation (IAU L_G, READ), Proxima b's
      surface (minimum mass, Brugger 2016's radii -- computed at 1.10-1.46 M_earth, H-B-SURFACE), and the frame term:
      comparing the two clocks needs a frame or a signal exchange, and in the Sun's frame Proxima's own motion adds
      v^2/2c^2.
  (2) The gradient term against measurement: Chou et al. 2010 (4.1 +- 1.6)e-17 for 33 cm (Science 329, 1630, NIST open
      reprint, Fig. 3) and Bothwell et al. -9.8(2.3)e-20 per mm (2109.12238v1 p.6; prediction p.5).  g h / c^2
      reproduces both within 1 sigma; the corridor extrapolates to absolute potentials ~1e-8 and to the v^2 term, under
      H-WEAK-FIELD.  Chou et al. also measured motional dilation at under 10 m/s (abstract, verifier-READ).
  (3) The stars' own motion in the CMB frame (reading 1; M's item 53 names the CMB frame as relating them): Sun 369.82
      km/s, Proxima |v_sun + v_rel|; the kinematic rate difference that frame assigns.  Gaia's RV is uncorrected for
      convective blueshift and gravitational redshift (H-GAIA-RV); Kervella's corrected RV is printed beside it.
  (4) A qubit of splitting dE shared across A and B picks up a relative phase dE (d tau)/hbar (Zych et al. 1105.4531v2
      eq. 12; eqs. 13-16 the visibility law; their setup excludes special-relativistic dilation, p.5; the move to the
      corridor is H-DELOCALISED-QUBIT).  d tau is FIXED: the phase is deterministic and calibratable by a phase scan.
      exp(-sigma^2/2) is the visibility averaged over a prior on d tau (H-GAUSSIAN-PHASE, an epistemic reading;
      1908.10165v2 p.2: clock-induced decoherence 'is (quantum) reference frame dependent').  Printed: the splitting
      below which the uncalibrated spread stays under 1 rad, and under V = 1/2.
  (5) A spread clock (Hohn-Smith-Lock 1912.00033v3 p.31, rho_S|B): S relative to B is an equal mixture of two branches,
      purity (1 + |<a|b>|^2)/2 by construction, at arbitrary illustrative inputs (H-CLOCK-SPREAD).  Covariance under a
      change of clock is STRUCTURAL (1908.10165v2 p.7 eqs. (10)-(11)).
  (6) Consciousness as perception of matter-observed time: Page's sensible quantum mechanics (gr-qc/9507024v1 pp.1-4)
      puts probabilities only in conscious perceptions, whose content includes memories (present records).  SQM 'does
      not describe any action of the perceptions back on the state' (p.9) -- an omission, not a denial: the same page
      argues survival 'does at least suggest that perceptions do have an action back on the quantum state', and p.12
      sketches how.  So H-LOCAL-CLOCK's last clause has a home in SQM, and H-CONSCIOUS-SELECTS would sit where Page's
      suggested back-action sits.  STRUCTURAL.

FOR H-LOCAL-CLOCK (READ; verifier-READ where marked)
  'time is not absolute but rather is defined by the reading of a clock moving along a specific world-line'
  (1908.10165v2 p.2); 'the time localisability of events becomes relative, depending on the reference frame' (p.1);
  'each quantum clock constitutes a legitimate temporal (quantum) reference frame' (p.7); 'localization in both space and
  time is only meaningful in relation to other physical systems, and not relative to absolute or external structures'
  (1912.00033v3 p.3, verifier-READ); 'temporal locality is frame dependent' (p.31); Page gr-qc/9303020v2: 'we cannot know
  the past except through its records in the present' (p.2), 'we cannot directly compare things at different locations
  either, so that all observations are really localized in space as well as in time' (p.3), coordinate time 'is
  completely unobservable' and 'the reading of a physical clock' is the condition whose dependence 'is then the
  observable time evolution' (pp.4-5) (verifier-READ); Zych et al. p.7: 'in quantum mechanics it makes no sense to speak
  about quantities without specifying how they are measured' (verifier-READ); Page gr-qc/9507024v1 p.10: perceptions are
  not associated with times or locations (verifier-READ).
SCOPE AND LIMITS
  Covariance makes no clock privileged -- which SUPPORTS 'the clock of the observer doesn't matter' -- while fixing the
  description by a calculable amount (1908.10165v2 p.7; 1912.00033v3 p.4).  The trinity's equivalence assumes a clock that
  does not interact with the system (p.3; the interacting case is open, p.37).  The one clock-interference experiment READ
  simulated the lag and 'is not accurate enough to be sensitive to special- or general-relativistic effects' (Margalit et
  al. 1505.05765v1 p.2); none other found in the READ.

NAMED HYPOTHESES
  H-WEAK-FIELD, H-OWN-STAR-FRAME, H-CIRCULAR, H-KEPLER-A, H-ORBIT-ONLY, H-B-SURFACE, H-GAIA-RV, H-DELOCALISED-QUBIT,
  H-GAUSSIAN-PHASE, H-CLOCK-SPREAD; with M's H-LOCAL-CLOCK.

HISTORY (first-written claims kept)
  * Before any report: the unknown-phase visibility was |cos(pi f sigma)| (0.983, 0.572) -- Zych's two-branch law on an
    uncertain phase; corrected to exp(-sigma^2/2).
  * Verifier (2026-10-05): '+- 0.021 from Faria's M_star error' held a fixed and independent -- a follows from M by Kepler
    III, so +- 0.014; 'the physical one' (each star's own frame) vs 'bookkeeping' (the CMB frame) -- each is a frame
    choice, and M's item 53 names the CMB frame; 'to stay coherent ... the splitting must be below 7.5 Hz' -- an
    unstated 1-rad criterion applied to ignorance of a fixed, calibratable phase; 'Earth's own potential (MEMORY)' -- READ
    as IAU L_G; the covariance check was true by construction, the spread-clock check near-vacuous, the swap control
    equivalent to the pin, the 32.4 km/s check circular (reading 2's 32.4 is this file's vector) -- the four replaced by
    the IAU L_C fixture, its potential-only control and a null-law control on Bothwell; 'perceptions do not act back
    (p.9)' and 'speculative extension' misread Page, who omits back-action, argues it is likely, and sketches it.
"""

import contextlib
import importlib.util
import io
import json
import math
import os
import sys

import numpy as np

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
    cmbframe = _by_path("cmb_cmbframe", os.path.join(HERE, "cmbframe.py"))

seat = cmbframe.seat
C = seat.C
AU = seat.AU
YEAR_S = seat.YEAR_S
HBAR = seat.HBAR
H_PL = seat.H
FARIA = seat.FARIA_2022
GM_SUN = 1.3271244e20             # IAU 2015 Resolution B3 nominal (arXiv:1510.07674v1 p.3), READ
GM_EARTH = 3.986004e14            # IAU 2015 B3 nominal (GM)_E, same page (verifier-READ); was labelled MEMORY
R_EARTH = 6.3781e6                # IAU 2015 B3 nominal equatorial radius R_eE, same page (verifier-READ); was 6.371e6
IAU_LC = 1.48082686741e-8         # IAU 2000 B1.5/B1.9: mean rate of TCG against TCB, i.e. a geocentre clock against the
                                  # barycentre's coordinate time, all bodies included (+- 2e-17).  READ: Firecrawl search
                                  # excerpts of iers.org IAU2000_Resolutions_B1-B3.pdf and USNO Circular 179 (2026-10-05)
IAU_LG = 6.969290134e-10          # IAU 2000 B1.9 (USNO Circular 179, same route): rate of TT against TCG -- a clock on
                                  # the rotating geoid against the geocentre; Earth's own potential plus rotation
CHOU = {"dh_m": 0.33, "measured": (4.1e-17, 1.6e-17), "g": 9.80,
        "source": "Chou, Hume, Rosenband & Wineland, Science 329, 1630 (2010), NIST open reprint, Fig. 3; eq. 2"}
BOTHWELL = {"measured_per_mm": (-9.8e-20, 2.3e-20), "a": -9.796, "predicted_per_mm": -1.09e-19,
            "source": "Bothwell et al., arXiv:2109.12238v1 p.6; a = -9.796 m/s^2 (p.19); Table 1 p.20"}
F_SR_HZ = 429.228e12              # an optical-clock qubit (illustrative; H-DELOCALISED-QUBIT)
F_CS_HZ = 9.192631770e9           # the caesium hyperfine splitting (the SI second's definition; illustrative)


def rate(gm, r):
    """1 - d tau/dt for a circular orbit of radius r about mass parameter gm (H-WEAK-FIELD, H-CIRCULAR)."""
    phi = gm / (r * C * C)
    v2 = gm / r
    return phi + v2 / (2 * C * C), phi, math.sqrt(v2)


def local_clocks():
    """Each offset is the clock's mean rate against a distant observer AT REST WITH ITS OWN STAR (H-OWN-STAR-FRAME).
    Comparing the two needs a frame or a signal exchange; the Sun-frame term for Proxima's own motion is printed beside
    it, since its size is set by that choice.  For any Keplerian orbit <1/r> = 1/a and <v^2> = GM/a, so the SECULAR
    offset is exactly 1.5 GM/(a c^2): H-CIRCULAR costs nothing for the mean rate (eccentricity adds a periodic term)."""
    off_a, phi_a, v_a = rate(GM_SUN, AU)
    gm_b = FARIA["M_star_sun"][0] * GM_SUN
    r_b = FARIA["b_a_au"] * AU
    off_b, phi_b, v_b = rate(gm_b, r_b)
    d = off_b - off_a
    s_rel = FARIA["M_star_sun"][1] / FARIA["M_star_sun"][0]
    # Faria's a follows from M_star and P by Kepler III (seat.py's own selftest checks it), so a ~ M^(1/3) and the offset
    # GM/a ~ M^(2/3) (H-KEPLER-A).  First written as off_b * s_rel -- a held fixed and independent -- giving 0.021 s/yr.
    sigma_d = off_b * (2.0 / 3.0) * s_rel
    v_rel = float(np.linalg.norm(proxima_velocity_vector())) * 1e3
    m_b = FARIA["b_msini_earth"][0]                                    # MINIMUM mass (seat.py)
    r_lo, r_hi = seat.BRUGGER_2016["radius_earth"]
    surf = lambda r: m_b * GM_EARTH / (r * R_EARTH * C * C)
    return {"A_offset": off_a, "A_phi": phi_a, "A_v_kms": v_a / 1e3, "B_offset": off_b, "B_phi": phi_b,
            "B_v_kms": v_b / 1e3, "B_minus_A": d, "seconds_per_year": d * YEAR_S,
            "sigma_seconds_per_year": sigma_d * YEAR_S,
            "sigma_first_written_seconds_per_year": off_b * s_rel * YEAR_S,
            "earth_own_term_LG": IAU_LG, "earth_own_seconds_per_year": IAU_LG * YEAR_S,
            "b_surface_seconds_per_year": (surf(r_hi) * YEAR_S, surf(r_lo) * YEAR_S),
            "sun_frame_motion_term_seconds_per_year": v_rel ** 2 / (2 * C * C) * YEAR_S,
            "A_vs_IAU_LC": off_a - IAU_LC, "A_potential_only_vs_IAU_LC": phi_a - IAU_LC}


def lab_checks():
    chou_pred = CHOU["g"] * CHOU["dh_m"] / C ** 2
    both_pred = BOTHWELL["a"] * 1e-3 / C ** 2
    return {"chou_predicted": chou_pred, "chou_measured": CHOU["measured"], "chou_within_1sigma":
            abs(chou_pred - CHOU["measured"][0]) <= CHOU["measured"][1],
            "bothwell_predicted": both_pred, "bothwell_measured": BOTHWELL["measured_per_mm"],
            "bothwell_within_1sigma": abs(both_pred - BOTHWELL["measured_per_mm"][0]) <= BOTHWELL["measured_per_mm"][1]}


def proxima_velocity_vector():
    """Proxima's velocity relative to the Sun (km/s, ICRS) from Gaia DR3's proper motion and radial velocity, as
    cmbframe holds them (READ)."""
    p = cmbframe.PROXIMA_DIR
    a, d = math.radians(p["ra_deg"]), math.radians(p["dec_deg"])
    n = np.array(cmbframe.N_PROXIMA)
    e_a = np.array([-math.sin(a), math.cos(a), 0.0])
    e_d = np.array([-math.sin(d) * math.cos(a), -math.sin(d) * math.sin(a), math.cos(d)])
    k = 4.740470446 * (1000.0 / p["plx_mas"][0]) / 1000.0              # km/s per (mas/yr)
    return p["rv_kms"][0] * n + k * (p["pm_mas_yr"][0] * e_a + p["pm_mas_yr"][1] * e_d)


def cmb_frame_kinematics():
    c = cmbframe.C_KMS
    v_sun = np.array(cmbframe.V_SUN_CMB)
    v_prox = v_sun + proxima_velocity_vector()
    k_sun = float(np.dot(v_sun, v_sun)) / (2 * c * c)
    k_prox = float(np.dot(v_prox, v_prox)) / (2 * c * c)
    return {"v_sun_cmb_kms": float(np.linalg.norm(v_sun)), "v_prox_cmb_kms": float(np.linalg.norm(v_prox)),
            "kinematic_offset_sun": k_sun, "kinematic_offset_prox": k_prox,
            "prox_minus_sun_seconds_per_year": (k_prox - k_sun) * YEAR_S,
            "prox_minus_sun_kervella_rv_seconds_per_year": _cmb_kervella(c, v_sun, k_sun)}


def _cmb_kervella(c, v_sun, k_sun):
    """The same with Kervella 2017's radial velocity (-22.204 km/s, corrected for convective blueshift and gravitational
    redshift, held in cmbframe) in place of Gaia's uncorrected -21.94 (H-GAIA-RV)."""
    dv = (-22.204 - cmbframe.PROXIMA_DIR["rv_kms"][0]) * np.array(cmbframe.N_PROXIMA)
    v = v_sun + proxima_velocity_vector() + dv
    return (float(np.dot(v, v)) / (2 * c * c) - k_sun) * YEAR_S


def delocalised_qubit(lc):
    """A qubit of splitting f shared across A and B: relative phase 2 pi f (d tau) per year (Zych et al. 1105.4531v2 eq.
    12; eqs. 13-16 are the two-branch visibility law, and Zych's setup excludes special-relativistic dilation, p.5 --
    the move to the corridor's orbits is H-DELOCALISED-QUBIT).  d tau is a FIXED number: every run gets the same phase,
    so ignorance of it shifts the fringe, it does not wash it out, and a phase scan calibrates it.  exp(-sigma^2/2) is
    the visibility AVERAGED OVER A PRIOR on d tau (H-GAUSSIAN-PHASE, epistemic); Castro-Ruiz et al. 1908.10165v2 p.2:
    clock-induced decoherence 'is (quantum) reference frame dependent'.  Printed: the splitting below which the
    uncalibrated phase spread stays under 1 rad (prior-averaged V = e^-1/2 = 0.61) and under sqrt(2 ln 2) rad (V = 1/2)."""
    rows = []
    sig = lc["sigma_seconds_per_year"]
    for name, f in (("optical (Sr, 429 THz)", F_SR_HZ), ("caesium hyperfine (9.19 GHz)", F_CS_HZ)):
        sp = 2 * math.pi * f * sig
        rows.append({"qubit": name, "phase_per_year_rad": 2 * math.pi * f * lc["seconds_per_year"],
                     "phase_spread_rad": sp, "log10_visibility_prior_averaged": -sp * sp / (2 * math.log(10)),
                     "visibility_prior_averaged": math.exp(-0.5 * sp * sp)})
    return {"rows": rows, "f_max_sigma_1rad_Hz": 1.0 / (2 * math.pi * sig),
            "f_max_visibility_half_Hz": math.sqrt(2 * math.log(2)) / (2 * math.pi * sig)}


def two_clocks(delta=0.6, tau=5.0, w=1.0, g=0.4):
    """B's clock spread over tau +- delta relative to A: the REDUCED state of S relative to B is the equal mixture of
    U(tau - delta)|0> and U(tau + delta)|0> (Hohn-Smith-Lock 1912.00033v3 p.31, rho_S|B, under their assumptions sigma << 1
    and psi_S not 2 delta-periodic; their eq. 72, p.30, is the PURE superposition of AS).  Its purity is (1 + |<a|b>|^2)/2
    BY CONSTRUCTION; delta, tau, w, g and |0> are arbitrary illustrative inputs (H-CLOCK-SPREAD), so the number
    illustrates the form, not a size.  First written with a covariance 'check' that set tau_B = r tau and evaluated
    U(tau_B / r) -- identically U(tau); it is now STRUCTURAL, resting on 1908.10165v2 p.7 eqs. (10)-(11)."""
    H = np.array([[w / 2, g / 2], [g / 2, -w / 2]], dtype=complex)
    ev, V = np.linalg.eigh(H)
    U = lambda t: V @ np.diag(np.exp(-1j * ev * t)) @ V.conj().T
    psi0 = np.array([1, 0], dtype=complex)
    def spread(dl):
        a, b = U(tau - dl) @ psi0, U(tau + dl) @ psi0
        rho = 0.5 * (np.outer(a, a.conj()) + np.outer(b, b.conj()))
        return float(np.real(np.trace(rho @ rho))), 0.5 * (1 + abs(np.vdot(a, b)) ** 2)
    return {"inputs": {"delta": delta, "tau": tau, "w": w, "g": g, "psi0": "|0>"},
            "purity_spread": spread(delta)[0], "purity_closed_form": spread(delta)[1]}


def compute():
    lc = local_clocks()
    return {"local_clocks": lc, "lab": lab_checks(), "cmb_frame": cmb_frame_kinematics(),
            "delocalised_qubit": delocalised_qubit(lc), "two_clocks": two_clocks()}


def report():
    d = compute()
    lc, lb, ck, dq, tc = (d[k] for k in ("local_clocks", "lab", "cmb_frame", "delocalised_qubit", "two_clocks"))
    print("H-LOCAL-CLOCK: a clock at each position (verified once; seated, ledger.py 8g)\n")
    print("(1) the two local clocks, each against a distant observer at rest with its own star (weak field; the secular "
          "rate is exact for any Keplerian orbit): A on Earth's orbit runs slow by %.3e (Phi %.3e, v %.2f km/s); B on "
          "Proxima b's orbit by %.3e (Phi %.3e, v %.2f km/s)" % (
              lc["A_offset"], lc["A_phi"], lc["A_v_kms"], lc["B_offset"], lc["B_phi"], lc["B_v_kms"]))
    print("    against IAU L_C (a geocentre clock vs barycentric coordinate time, all bodies): %.4e vs %.4e (diff %.1e); "
          "the potential term alone misses by %.1e" % (lc["A_offset"], IAU_LC, lc["A_vs_IAU_LC"],
                                                       lc["A_potential_only_vs_IAU_LC"]))
    print("    B's orbital offset exceeds A's by %.3e: %.3f s per year, +- %.4f from Faria's M_star error alone (a by "
          "Kepler III; first written +- %.3f with a held independent)" % (
              lc["B_minus_A"], lc["seconds_per_year"], lc["sigma_seconds_per_year"],
              lc["sigma_first_written_seconds_per_year"]))
    print("    terms the size of that error bar, left out: Earth's own potential and rotation (IAU L_G) %.3f s/yr; "
          "Proxima b's surface %.3f-%.3f s/yr (minimum mass, Brugger radii); comparing the two needs a frame -- in the "
          "Sun's, Proxima's own motion adds %.3f s/yr" % (
              lc["earth_own_seconds_per_year"], *lc["b_surface_seconds_per_year"],
              lc["sun_frame_motion_term_seconds_per_year"]))
    print("(2) the gradient term against measurement: Chou 33 cm predicted %.2e, measured %.1e +- %.1e (%s; null "
          "excluded at %.1f sigma); Bothwell per mm predicted %.3e, measured %.1e +- %.1e (%s; null excluded at %.1f "
          "sigma)" % (lb["chou_predicted"], *lb["chou_measured"],
                      "within 1 sigma" if lb["chou_within_1sigma"] else "outside",
                      CHOU["measured"][0] / CHOU["measured"][1], lb["bothwell_predicted"], *lb["bothwell_measured"],
                      "within 1 sigma" if lb["bothwell_within_1sigma"] else "outside",
                      abs(BOTHWELL["measured_per_mm"][0]) / BOTHWELL["measured_per_mm"][1]))
    print("(3) in the CMB frame (reading 1, M's item 53): Sun %.2f km/s, Proxima %.2f km/s (relative %.2f km/s, Gaia); "
          "that frame reckons Proxima's clock slower by %.3f s per year than the Sun's from motion alone (%.3f with "
          "Kervella's corrected RV)" % (ck["v_sun_cmb_kms"], ck["v_prox_cmb_kms"],
                                        float(np.linalg.norm(proxima_velocity_vector())),
                                        ck["prox_minus_sun_seconds_per_year"],
                                        ck["prox_minus_sun_kervella_rv_seconds_per_year"]))
    print("(4) a qubit shared across A and B (d tau fixed: the phase is calibratable; prior-averaged visibility shown):")
    for r in dq["rows"]:
        print("    %-28s relative phase %.2e rad per year; uncalibrated spread %.2e rad -> log10 V = %.1e" % (
            r["qubit"], r["phase_per_year_rad"], r["phase_spread_rad"], r["log10_visibility_prior_averaged"]))
    print("    with no calibration, the spread stays under 1 rad (V = 0.61) below %.1f Hz, and V stays above 1/2 below "
          "%.1f Hz" % (dq["f_max_sigma_1rad_Hz"], dq["f_max_visibility_half_Hz"]))
    print("(5) a spread clock (illustrative inputs %s): S relative to B has purity %.3f = (1 + |<a|b>|^2)/2 = %.3f by "
          "construction; covariance under a change of clock is STRUCTURAL (1908.10165v2 p.7)" % (
              tc["inputs"], tc["purity_spread"], tc["purity_closed_form"]))
    print("(6) consciousness as perception of matter-observed time: Page's sensible QM -- STRUCTURAL")


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
    lc, lb, ck, dq, tc = (d[k] for k in ("local_clocks", "lab", "cmb_frame", "delocalised_qubit", "two_clocks"))
    chk("the weak-field law on Earth's orbit reproduces IAU L_C = 1.48082686741e-8 (|diff| %.1e < 5e-12, the other "
        "planets' share)" % abs(lc["A_vs_IAU_LC"]), abs(lc["A_vs_IAU_LC"]) < 5e-12)
    chk("the potential term alone misses L_C (by %.1e > 1e-9): the v^2/2c^2 term is needed" %
        abs(lc["A_potential_only_vs_IAU_LC"]), abs(lc["A_potential_only_vs_IAU_LC"]) > 1e-9, ctl=True)
    chk("B's orbital offset exceeds A's by %.3f s per year (regression pin 0.708, re-derived by the verifier)" %
        lc["seconds_per_year"], abs(lc["seconds_per_year"] - 0.708) < 0.002)
    chk("the gradient law g h / c^2 reproduces Chou et al.'s 33 cm shift and Bothwell et al.'s per-mm gradient within "
        "1 sigma", lb["chou_within_1sigma"] and lb["bothwell_within_1sigma"])
    chk("a law ten times too large misses Chou et al. by more than 3 sigma",
        abs(10 * lb["chou_predicted"] - CHOU["measured"][0]) > 3 * CHOU["measured"][1], ctl=True)
    chk("a null law (no gravitational redshift) misses Bothwell et al. by more than 3 sigma",
        abs(BOTHWELL["measured_per_mm"][0]) > 3 * BOTHWELL["measured_per_mm"][1], ctl=True)
    structural.append("covariance: relative to another clock the system follows the same law rescaled (1908.10165v2 "
                      "p.7 eqs. (10)-(11), 'universal covariant form'); the choice of clock changes the description by a "
                      "calculable amount (1912.00033v3 p.4)")
    structural.append("a spread clock leaves S relative to B in an equal mixture, purity (1 + |<a|b>|^2)/2 < 1 for "
                      "distinct branches (1912.00033v3 p.31; %.3f at the illustrative inputs)" % tc["purity_spread"])
    structural.append("Page's sensible QM houses H-LOCAL-CLOCK's last clause: probabilities only in conscious perceptions "
                      "of present records (gr-qc/9507024v1 pp.1-4); SQM does not describe back-action, Page argues "
                      "perceptions likely do act back (p.9) and sketches how (p.12) -- where H-CONSCIOUS-SELECTS would sit")
    for s in structural:
        print("  STRUCTURAL: " + s)
    print("localclock.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
