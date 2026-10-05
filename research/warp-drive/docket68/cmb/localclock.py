#!/usr/bin/env python3
"""
localclock.py -- H-LOCAL-CLOCK: a clock at each position, relative to the matter-based observation there; conscious
observation as a perception of matter-observed time.

Not seated; not yet verified.  M (rulings item 52): "time is always relative, so the clock of the observer doesn't matter
in the second position, as time may move differently in the second position compared to the first. The clock is always
present relative to the position of measurement within its plane/dimension The clock is relative to the matter-based
observation. Consciousness observation is a perception of matter-observed time."  Carried as M's hypothesis
H-LOCAL-CLOCK, never as a result.  M (item 53): "READ, then model" -- READ done (2026-10-05); this is the model.

    python3 localclock.py              report
    python3 localclock.py --selftest   checks, with CONTROLS
    python3 localclock.py --json       the numbers as JSON

WHAT IS COMPUTED
  (1) The two local clocks.  Weak field (H-WEAK-FIELD): d tau / dt = 1 - Phi/c^2 - v^2/(2 c^2) in each star's rest
      frame.  A: Earth's orbit (GM_sun, IAU 2015 B3, READ; 1 AU; circular speed).  B: Proxima b's orbit (Faria 2022's
      M_star and a, READ via seat.py; circular speed).  Their difference in seconds per year.  Earth's own potential and
      rotation, and b's eccentricity, are left out (H-ORBIT-ONLY, sizes printed).
  (2) The same law against measurement: Chou et al. 2010 measured (4.1 +- 1.6)e-17 for 33 cm (Science 329, 1630,
      NIST's open reprint, Fig. 3) and Bothwell et al. -9.8(2.3)e-20 per mm (2109.12238v1 p.6): the law g h / c^2
      reproduces both within their errors.
  (3) The stars' own motion: in the CMB frame (reading 1, cmbframe.py) the Sun moves at 369.82 km/s and Proxima at
      |v_sun + v_rel|; the kinematic rate difference that frame assigns -- a frame-dependent figure (another frame
      assigns another), as relativity requires.
  (4) What a local clock costs a delocalised quantum state: a qubit of energy splitting dE shared across A and B picks
      up a relative phase dE (d tau)/hbar (Zych et al.'s proper-time phase, 1105.4531v2 eqs. 13-16, applied to the
      corridor's span); it is deterministic and correctable if d tau is known.  An UNKNOWN phase with Gaussian spread
      sigma leaves visibility exp(-sigma^2/2) (H-GAUSSIAN-PHASE); the READ uncertainty in d tau (Faria's M_star error)
      sets the largest splitting that stays coherent over a year (H-DELOCALISED-QUBIT).
      HISTORY: first printed as |cos(pi f sigma)| -- Zych's two-branch law applied to an uncertain phase, which is
      meaningless at spreads of 1e9-1e13 rad (it printed 0.983 and 0.572); corrected before any report.
  (5) Two clocks for one system (Castro-Ruiz et al. 1908.10165v2 eq. 1, 6-8; Hohn-Smith-Lock 1912.00033v3 sec. VII C):
      relative to B's clock, ticking at a rate r against A's, the system evolves as exp(-i H tau_B / r) -- covariant,
      the same law rescaled; if B's clock is spread over readings tau +- Delta relative to A, the system relative to B
      is a superposition U(tau - Delta) + U(tau + Delta), 'temporally nonlocal' -- computed (purity loss).
  (6) Consciousness as perception of matter-observed time: Page's sensible quantum mechanics (gr-qc/9507024v1 pp.1-4)
      puts probabilities only in conscious perceptions, whose content includes memories (present records); 'we cannot
      know the past except through its records in the present' (Page gr-qc/9303020v2 p.2).  In SQM perceptions do not
      act back on the quantum state (p.9); back-action appears only in Page's speculative 'Sensational' extension
      (p.12).  So H-LOCAL-CLOCK's last clause fits SQM directly (a perception of a matter record), and H-CONSCIOUS-SELECTS
      reading (b) would need the speculative extension.  STRUCTURAL.

FAIR SIDES (READ)
  For: time as a clock reading tied to a worldline (1908.10165v2 p.2); 'each quantum clock constitutes a legitimate
  temporal (quantum) reference frame' (p.7); 'temporal locality is frame dependent' (1912.00033v3 p.31); rate
  differences measured over 33 cm and within 1 mm.  Against the letter of 'the clock of the observer doesn't matter':
  clock relations are lawful and covariant -- the choice of clock changes the description by a calculable amount
  (1908.10165v2 p.7; 1912.00033v3 p.4); the trinity's equivalence assumes the clock does not interact with the system
  (p.3; the interacting case is open, p.37); the only clock-interference experiment simulated the lag and was not
  sensitive to relativity (Margalit et al. 1505.05765v1 p.2).

NAMED HYPOTHESES
  H-WEAK-FIELD, H-ORBIT-ONLY (Earth's own potential, GM_earth/(R c^2) with MEMORY-NOT-READ values, printed for size
  only), H-CIRCULAR, H-DELOCALISED-QUBIT, H-GAUSSIAN-PHASE, H-CLOCK-SPREAD; with M's H-LOCAL-CLOCK.
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
    off_a, phi_a, v_a = rate(GM_SUN, AU)
    gm_b = FARIA["M_star_sun"][0] * GM_SUN
    r_b = FARIA["b_a_au"] * AU
    off_b, phi_b, v_b = rate(gm_b, r_b)
    d = off_b - off_a
    s_rel = FARIA["M_star_sun"][1] / FARIA["M_star_sun"][0]           # relative error in M_star (both terms ~ M)
    sigma_d = off_b * s_rel
    return {"A_offset": off_a, "A_phi": phi_a, "A_v_kms": v_a / 1e3, "B_offset": off_b, "B_phi": phi_b,
            "B_v_kms": v_b / 1e3, "B_minus_A": d, "seconds_per_year": d * YEAR_S,
            "sigma_seconds_per_year": sigma_d * YEAR_S,
            "earth_own_potential": 3.986004e14 / (6.371e6 * C * C)}    # GM_earth / R_earth c^2 (MEMORY, size only)


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
            "prox_minus_sun_seconds_per_year": (k_prox - k_sun) * YEAR_S}


def delocalised_qubit(lc):
    """A qubit of splitting f shared across A and B: relative phase 2 pi f (d tau) per year; the READ uncertainty in d
    tau gives a phase spread 2 pi f sigma; the largest f that keeps that spread below 1 rad over a year."""
    rows = []
    for name, f in (("optical (Sr, 429 THz)", F_SR_HZ), ("caesium hyperfine (9.19 GHz)", F_CS_HZ)):
        rows.append({"qubit": name, "phase_per_year_rad": 2 * math.pi * f * lc["seconds_per_year"],
                     "phase_spread_rad": 2 * math.pi * f * lc["sigma_seconds_per_year"],
                     "visibility_if_unknown": math.exp(-0.5 * (2 * math.pi * f * lc["sigma_seconds_per_year"]) ** 2)})
    f_max = 1.0 / (2 * math.pi * lc["sigma_seconds_per_year"])
    return {"rows": rows, "f_max_coherent_Hz": f_max}


def two_clocks(r=1.0 + 3.7e-8 * 1e6, delta=0.6, tau=5.0):
    """A qubit system S with H = (w/2) sigma_z + (g/2) sigma_x.  (i) relative to B's clock ticking at rate r against A's,
    S's conditional evolution is U(tau_B / r): checked against A's description at the matching reading.  (ii) B's clock
    spread over tau +- delta relative to A: S relative to B is the equal mixture-of-branches U(tau - delta) and
    U(tau + delta) (Hohn-Smith-Lock eqs. 69-72) -- its purity is printed; control: delta = 0 gives a pure state.
    The rate r is exaggerated by 1e6 for visibility (H-CLOCK-SPREAD); the law does not depend on its size."""
    w, g = 1.0, 0.4
    H = np.array([[w / 2, g / 2], [g / 2, -w / 2]], dtype=complex)
    ev, V = np.linalg.eigh(H)
    U = lambda t: V @ np.diag(np.exp(-1j * ev * t)) @ V.conj().T
    psi0 = np.array([1, 0], dtype=complex)
    tau_B = r * tau                                                    # B's reading when A reads tau
    covariance = 1 - abs(np.vdot(U(tau) @ psi0, U(tau_B / r) @ psi0)) ** 2
    def spread_purity(dl):
        a, b = U(tau - dl) @ psi0, U(tau + dl) @ psi0
        rho = 0.5 * (np.outer(a, a.conj()) + np.outer(b, b.conj()))
        return float(np.real(np.trace(rho @ rho)))
    return {"rate_r": r, "covariance_infidelity": float(covariance), "purity_spread": spread_purity(delta),
            "purity_no_spread": spread_purity(0.0)}


def compute():
    lc = local_clocks()
    return {"local_clocks": lc, "lab": lab_checks(), "cmb_frame": cmb_frame_kinematics(),
            "delocalised_qubit": delocalised_qubit(lc), "two_clocks": two_clocks()}


def report():
    d = compute()
    lc, lb, ck, dq, tc = (d[k] for k in ("local_clocks", "lab", "cmb_frame", "delocalised_qubit", "two_clocks"))
    print("H-LOCAL-CLOCK: a clock at each position (not verified; not seated)\n")
    print("(1) the two local clocks (weak field, circular orbits): A on Earth's orbit runs slow by %.3e (Phi %.3e, v %.2f "
          "km/s); B on Proxima b's orbit by %.3e (Phi %.3e, v %.2f km/s)" % (
              lc["A_offset"], lc["A_phi"], lc["A_v_kms"], lc["B_offset"], lc["B_phi"], lc["B_v_kms"]))
    print("    B runs slower than A by %.3e: %.3f s per year (+- %.3f from Faria's M_star error); Earth's own potential "
          "(%.1e, left out) is %.0f %% of the difference" % (lc["B_minus_A"], lc["seconds_per_year"],
                                                            lc["sigma_seconds_per_year"], lc["earth_own_potential"],
                                                            100 * lc["earth_own_potential"] / lc["B_minus_A"]))
    print("(2) the law against measurement: Chou 33 cm predicted %.2e, measured %.1e +- %.1e (%s); Bothwell per mm "
          "predicted %.3e, measured %.1e +- %.1e (%s)" % (
              lb["chou_predicted"], *lb["chou_measured"], "within 1 sigma" if lb["chou_within_1sigma"] else "outside",
              lb["bothwell_predicted"], *lb["bothwell_measured"],
              "within 1 sigma" if lb["bothwell_within_1sigma"] else "outside"))
    print("(3) in the CMB frame (reading 1): Sun %.2f km/s, Proxima %.2f km/s; that frame reckons Proxima's clock "
          "slower by %.3f s per year than the Sun's from motion alone -- a frame-dependent figure" % (
              ck["v_sun_cmb_kms"], ck["v_prox_cmb_kms"], ck["prox_minus_sun_seconds_per_year"]))
    print("(4) a qubit shared across A and B:")
    for r in dq["rows"]:
        print("    %-28s relative phase %.2e rad per year (deterministic, correctable if known); spread from the READ "
              "uncertainty %.2e rad -> visibility exp(-sigma^2/2) = %.1e" % (
                  r["qubit"], r["phase_per_year_rad"], r["phase_spread_rad"], r["visibility_if_unknown"]))
    print("    to stay coherent over a year at today's knowledge of d tau the splitting must be below %.1f Hz" %
          dq["f_max_coherent_Hz"])
    print("(5) two clocks for one system: relative to B's clock (rate %.6f) the system follows the same law rescaled "
          "(infidelity %.1e); with B's clock spread over +- delta the system relative to B is temporally nonlocal "
          "(purity %.3f; %.3f without spread)" % (tc["rate_r"], tc["covariance_infidelity"], tc["purity_spread"],
                                                  tc["purity_no_spread"]))
    print("(6) consciousness as perception of matter-observed time: Page's sensible QM (probabilities only in "
          "perceptions of present records; no back-action, p.9) -- STRUCTURAL")


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
    chk("Earth-orbit clock offset 1.48e-8 (= 1.5 GM/(a c^2) for a circular orbit) (%.4e)" % lc["A_offset"],
        abs(lc["A_offset"] - 1.5 * GM_SUN / (AU * C * C)) < 1e-18 and abs(lc["A_offset"] - 1.48e-8) < 0.01e-8)
    chk("B runs slower than A by %.3f s per year (pinned 0.708, verified on the spot earlier with the same inputs)" %
        lc["seconds_per_year"], abs(lc["seconds_per_year"] - 0.708) < 0.002)
    chk("swapping the two orbits flips the sign", rate(GM_SUN, AU)[0] - rate(FARIA["M_star_sun"][0] * GM_SUN,
                                                                           FARIA["b_a_au"] * AU)[0] < 0, ctl=True)
    chk("the law g h / c^2 reproduces Chou et al.'s 33 cm shift and Bothwell et al.'s per-mm gradient within 1 sigma",
        lb["chou_within_1sigma"] and lb["bothwell_within_1sigma"])
    chk("a law ten times too large misses Chou et al. by more than 3 sigma",
        abs(10 * lb["chou_predicted"] - CHOU["measured"][0]) > 3 * CHOU["measured"][1], ctl=True)
    chk("Proxima's speed relative to the Sun from Gaia: %.2f km/s (32.4 in reading 2)" % float(
        np.linalg.norm(proxima_velocity_vector())), abs(float(np.linalg.norm(proxima_velocity_vector())) - 32.4) < 0.2)
    chk("a qubit coherent across A and B over a year needs a splitting below 1 kHz at today's knowledge of d tau "
        "(%.1f Hz); an optical or caesium qubit's visibility is below 1e-100 if the phase is not corrected" % (
            dq["f_max_coherent_Hz"]), dq["f_max_coherent_Hz"] < 1e3
        and all(r["visibility_if_unknown"] < 1e-100 for r in dq["rows"]))
    chk("relative to B's clock the system follows the same law rescaled (covariance infidelity %.1e)" %
        tc["covariance_infidelity"], tc["covariance_infidelity"] < 1e-12)
    chk("a spread clock makes the system temporally nonlocal (purity %.3f < 0.99); no spread, pure (%.6f)" % (
        tc["purity_spread"], tc["purity_no_spread"]), tc["purity_spread"] < 0.99 and tc["purity_no_spread"] > 1 - 1e-12)
    structural.append("Page's sensible QM: probabilities only in conscious perceptions of present records; perceptions do "
                      "not act back on the state (gr-qc/9507024v1 p.9) -- H-LOCAL-CLOCK's last clause fits it; "
                      "H-CONSCIOUS-SELECTS reading (b) would need Page's speculative 'Sensational' extension (p.12)")
    structural.append("clock relations are lawful and covariant (1908.10165v2 p.7; 1912.00033v3 p.4): the choice of "
                      "clock changes the description by a calculable amount")
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
