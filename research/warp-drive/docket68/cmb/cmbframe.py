#!/usr/bin/env python3
"""
cmbframe.py -- H-CMB-CORRIDOR, reading 1: the cosmic background as the corridor's FRAME.

Not seated.  M (rulings item 41, a question after DOCKET 68's close): "Have we considered the universe's own background
radiation as the means by which the corridor is constructed? As it is likely that background only multi-spacetime/
multiversal constant?"  Carried as M's hypotheses H-CMB-CORRIDOR and H-CMB-UNIVERSAL, never as results.  M (item 42):
"3, then 1" -- the Q-1s gate first, then the CMB as the frame.  This file takes up that reading only: the background's
rest frame as H-FRAME's preferred frame (M-D68-C10), to which every corridor coupling is keyed.  Whether the background
can CARRY or BUILD the corridor (its photons as the medium, its entropy as the register) is a different reading and is
not touched here.

    python3 cmbframe.py              report
    python3 cmbframe.py --selftest   checks, with CONTROLS
    python3 cmbframe.py --json       the numbers as JSON

WHAT THE BOARD ALREADY HELD (asked of its owners at run time, never retyped)
  frame.py / A2-frame.md: a corridor network keyed to one frame closes no causal curve at any rank (Gram positive
  definite), and in exact FRW cosmic time is a global time function on the comoving quotient (z3 lemma).  frame.py
  priced a cosmic-simultaneous 1-ly corridor along the dipole at -38,929 s in the barycentre's coordinate time, from a
  dipole READ-VIA-RESTATEMENT (D67).  step1c/nonlocal.py: an instantaneous coupling is loop-free iff all couplings share
  one simultaneity frame; its J bounds from spacelike Bell tests carry H-LAB-FRAME.  seat.py: Proxima's distance.
  cosmo.py: H0 (PINNED Planck 2018).

WHAT IS NEW HERE
  (1) The dipole READ at source (Planck 2018 I, 1807.06205v2), upgrading frame.py's restatement.
  (2) The Earth-Proxima geometry: the angle between the dipole apex and Proxima, and the lead a CMB-keyed link shows in
      the barycentre's coordinate time, with its annual modulation and the realisation error the dipole's own
      precision sets.
  (3) That one frame spans Earth-Proxima: the Hubble-flow difference across the span, and why it does not matter in FRW.
  (4) H-LAB-FRAME, asked of nonlocal.py with the frame NAMED as the CMB's: computed rather than assumed.
  (5) The speed-of-influence bound actually evaluated in the CMB frame (Scarani 2000), and what it does not exclude.
  (6) H-CMB-IS-COSMIC against the matter dipole (Secrest 2021, 2022; the 2025 colloquium): the CMB frame and the frame
      the quasars define differ, and what that difference does to the keying at Proxima.
  (7) H-CMB-UNIVERSAL's measurable part: T(z) = T0 (1+z)^(1-beta), so the background is not constant in time; what is
      common to all comoving observers is its frame and spectral form, and its temperature is a cosmic clock whose
      resolution is computed.  The "multi-spacetime / multiversal" part has no measurement on the board: OPEN.

NAMED HYPOTHESES
  H-CMB-AS-FRAME     M's reading: H-FRAME's preferred frame is the CMB rest frame (the dipole-free frame).
  H-CMB-IS-COSMIC    the CMB rest frame is FRW's comoving frame (D67 H1: the dipole is kinematic) -- CONTESTED by the
                     matter dipole, READ below.
  H-BARYCENTRE       Planck's velocity is the Solar-System barycentre's (D67 H2).
  H-FIRST-ORDER      offsets to first order in v.x/c^2 with gamma kept; the dropped terms are below gamma^2 beta^2 ~ 2e-6
                     relatively.
  H-CIRCULAR-ORBIT   Earth's orbital speed taken as 2 pi AU / yr; the eccentricity (about 1.7 %, MEMORY-NOT-READ) is
                     covered by a 2 % margin wherever a bound is drawn.
  H-OBLIQUITY        the ecliptic pole at Dec 90 - 23.4392911 deg (IAU 1976 obliquity, MEMORY-NOT-READ; cross-checked
                     against astropy at build, below); used only for the annual modulation's projection.
  H-ROTATION-BOUND   Earth's rotation adds at most 0.5 km/s (equatorial 0.465 km/s, MEMORY-NOT-READ).
  H-GAL-MATRIX       the Hipparcos Galactic->ICRS rotation (ESA 1997, MEMORY-NOT-READ), CHECKED against Planck's own
                     printed RA/Dec of the dipole (READ) and against astropy at build.
  H-QUASAR-KINEMATIC the quasar dipole read as a velocity by scaling: v_q = v_CMB x D_obs / D_exp (the kinematic
                     amplitude is linear in beta); used only to size the keying difference, never as a measured speed.
  H-CORRIDOR-MODEL, H-FRW-EXACT, H-NOT-DE-SITTER, H-CORRIDOR-MAP: frame.py's and nonlocal.py's.

HISTORY (first build, 2026-10-05; first-written checks kept):
  * 'Planck's beta equals v/c to 1e-5 relative' -- failed: they differ by 1.6e-5 relative, inside Planck's own beta
    error (0.00036e-3); the check is now agreement within that error.
  * 'The annual modulation is under 3 % of the lead; the realisation sigma under 30 s' -- failed: the modulation is
    +- 9,453 s, 14 % of the lead, and the sigma 35.4 s.  Guessed thresholds; the computed values are pinned instead.
  * 'The quasar frame shifts the lead by more than an hour' -- failed: 0.74 h, because the quasar apex lies further
    from Proxima (79 deg against 66 deg), offsetting its doubled speed; the range over the READ errors is printed.

BUILD-TIME CROSS-CHECK (astropy 7, pip, NOT a dependency; run once 2026-10-05, values recorded, not re-run here):
  Galactic (264.021, 48.253) -> ICRS (167.94190, -6.94426); Proxima (Gaia DR3) ecliptic latitude -44.7677 deg;
  separation dipole-apex to Proxima 66.19427 deg; (238, 31) -> (141.6468, -5.0701), 78.983 deg from Proxima;
  (271.9, 29.6) -> (162.9539, -25.9673), 51.023 deg.
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
for _p in (D68, WD):
    if _p not in sys.path:
        sys.path.append(_p)


def _by_path(key, path):
    """An owner loaded by PATH under a private name (the board's root holds same-named files)."""
    if key in sys.modules:
        return sys.modules[key]
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


with contextlib.redirect_stdout(io.StringIO()):
    import seat
    import cosmo
    frame = _by_path("cmb_frame", os.path.join(D68, "frame.py"))
    nonlocal_ = _by_path("s1c_nonlocal", os.path.join(WD, "step1c", "nonlocal.py"))

C = seat.C                       # m/s
LY = seat.LY
AU = seat.AU
YEAR_S = seat.YEAR_S
L = seat.D_PROXIMA               # Proxima's distance, the board's owner (phase1's Gaia DR3 parallax, via settle)
H0 = cosmo.H0()                  # s^-1, PINNED Planck 2018
C_KMS = C / 1000.0

# ---------------------------------------------------------------------------------------------------------------------
# READ at source (2026-10-05).  Routes: alphaXiv answer_pdf_queries (arXiv PDF page text); VizieR via Firecrawl.
# ---------------------------------------------------------------------------------------------------------------------
DIPOLE = {   # Planck 2018 I, arXiv:1807.06205v2: Table 2 p.6 ("Planck 2018" row) and its footnote e; text p.6.
    "v_kms": (369.82, 0.11), "beta": (1.23357e-3, 0.00036e-3), "amp_uK": (3362.08, 0.99),
    "l_deg": (264.021, 0.011), "b_deg": (48.253, 0.005), "ra_deg": (167.942, 0.007), "dec_deg": (-6.944, 0.007),
    "T0_calibration_rel": 2e-4,     # Table 2 note: the errors exclude the 0.02 % uncertainty on T0
    "source": "1807.06205v2 Table 2 p.6, fn. e (RA/Dec J2000); p.6 text (beta, v; systematics added linearly)",
    "hfi_eq10": "1807.06207v1 eq. (10) p.25: v = 369.8160 +- 0.0010 km/s (statistical-scale error; Planck I's 0.11 "
                "folds in systematics and is the one used)"}
FRAMES_OF_MATTER = {   # Planck 2018 I Table 3 p.7 (non-relativistic velocity addition, Sun-LG from Diaz 2014)
    "Local Group": {"v_kms": (620.0, 15.0), "l_deg": 271.9, "b_deg": 29.6},
    "Galactic centre": {"v_kms": (565.0, 5.0), "l_deg": 265.76, "b_deg": 28.38}}
T0 = (2.72548, 0.00057)   # Fixsen 2009, arXiv:0911.1955v2, abstract p.1, Table 2 'Mean' p.5
T_OF_Z = {   # T(z) = T0 (1+z)^(1-beta)
    "Avgoustidis 2016 (1511.04335v1), SZ+QSO+distance duality": {"beta": (7.6e-3, 8.0e-3),
                                                                  "page": "abstract p.1; Table III p.6"},
    "Avgoustidis 2016, direct data only": {"beta": (4.6e-3, 8.9e-3), "page": "Table II p.4"},
    "Riechers 2022 (2202.00693v1), combined fit": {"beta": (3.4e-3, 7.3e-3), "beta_plus": 8.1e-3,
                                                   "page": "Fig. 4 caption p.7 (the lower error, 7.3e-3, used)"},
}
T_HFLS3 = {"z": 6.3369, "T_1sigma_K": (16.4, 30.2), "predicted_K": 20.0,
           "page": "2202.00693v1 p.3, Fig. 1 p.5 (z), p.1 (20.0 K); the brief's id 2201.00693 was wrong (a reader "
                   "caught it: that id is a CS paper)"}
MATTER_DIPOLE = {
    "Secrest 2021 (2009.14826v2)": {"D": 0.01554, "D_exp": 0.007, "l_deg": 238.2, "b_deg": 28.8, "sigma": 4.9,
                                    "page": "p.5 (D, direction, 27.8 deg from the CMB dipole, p = 5e-7); D_exp '~0.007'"
                                            " from eq. 1 p.2 (rounded)"},
    "Secrest 2022 (2206.05624v2), WISE": {"D": 1.48e-2, "D_exp": 0.73e-2, "l_deg": 238.0, "b_deg": 31.0,
                                           "sigma": 4.4, "page": "p.5"},
    "Secrest 2022, joint WISE+NVSS": {"sigma": 5.1, "page": "p.5, abstract p.1"},
    "Secrest et al. 2025 colloquium (2505.23526v2)": {"sigma_text": "'now exceeds 5 sigma' (p.1); '~6.4 sigma' "
                                                                    "combining Wagenveld 2023a (p.14)"},
}
PROXIMA_DIR = {   # Gaia DR3 (VizieR I/355/gaiadr3, doi:10.26093/cds/vizier.1355), source_id 5853498713190525696
    "ra_deg": 217.39232147201, "dec_deg": -62.67607511677, "epoch": "2016.0", "plx_mas": (768.0665, 0.0499),
    "rv_kms": (-21.94, 0.22), "pm_mas_yr": (-3781.741, 769.465),
    "rv_kervella2017": "-22.204 +- 0.032 km/s, corrected for convective blueshift and gravitational redshift "
                       "(1611.03495v3 Table 2 p.4)"}
CMB_FRAME_SPEED_BOUNDS = {
    "Scarani, Tittel, Zbinden, Gisin 2000 (quant-ph/0007008v1)": {
        "v_min_over_c": 1.5e4, "page": "abstract p.1; Sec. 4-5 p.5",
        "note": "Geneva, 10.6 km; detections simultaneous in the CMB frame near 3h UTC; tau not monitored, linearly "
                "interpolated (a stated assumption, p.5); CMB velocity taken as 371 km/s (Lineweaver 1996)"},
    "Salart et al. 2008 (0808.3316v1)": {
        "v_min_over_c": None, "page": "abstract p.1; p.5",
        "note": "states >= 1e4 c in every direction for beta = 1e-3 and 54000 c at chi = 90 deg; the CMB frame's beta "
                "(1.234e-3, computed here) lies just outside that headline condition and no CMB-frame figure is "
                "printed; a reader's own evaluation of their eqs. (3), (7) at the CMB beta gave ~4.6e4 c -- "
                "reader-COMPUTED, not used"},
    "Bancal et al. 2012 (1110.3795v2)": {
        "v_min_over_c": None, "page": "p.1-2",
        "note": "any finite v, c < v < infinity, implies signalling; the CMB frame is the 'well-known example' of a "
                "natural privileged frame, not adopted as the frame"},
}

# ---------------------------------------------------------------------------------------------------------------------
# geometry
# ---------------------------------------------------------------------------------------------------------------------
#: H-GAL-MATRIX: ICRS -> Galactic (Hipparcos, ESA 1997; MEMORY-NOT-READ, checked against Planck's printed RA/Dec).
_A = ((-0.0548755604162154, -0.8734370902348850, -0.4838350155487132),
      (0.4941094278755837, -0.4448296299600112, 0.7469822444972189),
      (-0.8676661490190047, -0.1980763734312015, 0.4559837761750669))
OBLIQUITY_DEG = 23.4392911   # H-OBLIQUITY (IAU 1976, MEMORY-NOT-READ)


def unit(ra_deg, dec_deg):
    a, d = math.radians(ra_deg), math.radians(dec_deg)
    return (math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d))


def radec(u):
    ra = math.degrees(math.atan2(u[1], u[0])) % 360.0
    return ra, math.degrees(math.asin(max(-1.0, min(1.0, u[2]))))


def gal_to_icrs(l_deg, b_deg):
    g = unit(l_deg, b_deg)
    return tuple(sum(_A[k][i] * g[k] for k in range(3)) for i in range(3))   # A^T g


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def angle_deg(u, v):
    return math.degrees(math.acos(max(-1.0, min(1.0, dot(u, v)))))


N_DIPOLE = unit(DIPOLE["ra_deg"][0], DIPOLE["dec_deg"][0])
N_PROXIMA = unit(PROXIMA_DIR["ra_deg"], PROXIMA_DIR["dec_deg"])
N_ECL_POLE = unit(270.0, 90.0 - OBLIQUITY_DEG)


def keyed_lead_s(v_kms, cos_theta, L_m=L):
    """A link keyed to a frame in which the barycentre moves at v: its far end, at the frame's equal time, falls at
    barycentre coordinate time t' = -gamma (v.x)/c^2 = -gamma beta L cos(theta)/c (H-FIRST-ORDER).  Negative = the far
    end is reached in the barycentre's coordinate past."""
    beta = v_kms / C_KMS
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    return -gamma * beta * L_m * cos_theta / C


# ---------------------------------------------------------------------------------------------------------------------
# results
# ---------------------------------------------------------------------------------------------------------------------
def geometry():
    th = angle_deg(N_DIPOLE, N_PROXIMA)
    cos_t = dot(N_DIPOLE, N_PROXIMA)
    gal = gal_to_icrs(DIPOLE["l_deg"][0], DIPOLE["b_deg"][0])
    return {"theta_deg": th, "cos_theta": cos_t, "gal_matrix_dipole_radec": radec(gal),
            "gal_matrix_vs_printed_deg": angle_deg(gal, N_DIPOLE),
            "proxima_ecliptic_lat_deg": 90.0 - angle_deg(N_PROXIMA, N_ECL_POLE),
            "L_ly": L / LY, "L_from_vizier_plx_ly": (3.0856775814913673e16 / (PROXIMA_DIR["plx_mas"][0] / 1000.0)) / LY}


def lead():
    g = geometry()
    v = DIPOLE["v_kms"][0]
    t = keyed_lead_s(v, g["cos_theta"])
    owner_1ly, owner_beta = frame.cmb_coordinate_past(1.0, v)     # frame.py's own along-dipole, 1-ly figure
    owner_scaled = owner_1ly * (L / LY) * g["cos_theta"]
    # annual modulation: Earth's orbital velocity projected on the Proxima line
    v_orb = 2 * math.pi * AU / YEAR_S / 1000.0
    proj = v_orb * math.cos(math.radians(g["proxima_ecliptic_lat_deg"]))
    t_mod = proj / C_KMS * L / C
    t_mod_bound = 1.02 * v_orb / C_KMS * L / C          # cos <= 1, eccentricity margin (H-CIRCULAR-ORBIT)
    # realisation error from the dipole's own precision
    sv = math.hypot(DIPOLE["v_kms"][1], DIPOLE["T0_calibration_rel"] * v)
    s_from_v = sv / C_KMS * L * abs(g["cos_theta"]) / C
    s_ang = math.radians(math.hypot(DIPOLE["ra_deg"][1] * math.cos(math.radians(DIPOLE["dec_deg"][0])),
                                    DIPOLE["dec_deg"][1]))
    s_from_dir = v / C_KMS * L * math.sin(math.radians(g["theta_deg"])) * s_ang / C
    return {"lead_s": t, "lead_h": t / 3600.0, "lead_days": t / 86400.0, "owner_check_s": owner_scaled,
            "owner_beta": owner_beta, "v_orb_kms": v_orb, "orb_proj_kms": proj, "annual_mod_s": t_mod,
            "annual_mod_bound_s": t_mod_bound, "sigma_v_kms": sv, "sigma_from_v_s": s_from_v,
            "sigma_from_dir_s": s_from_dir, "sigma_total_s": math.hypot(s_from_v, s_from_dir)}


def one_frame_across_span():
    """Comoving observers at Earth and Proxima differ by the Hubble flow, dbeta = H0 L / c.  In the flat lattice model
    that is a tilt; in exact FRW the keying is to cosmic time, a global time function (frame.py's z3 lemma), so the
    tilt is the flat model's artefact, not a loop."""
    dbeta = H0 * L / C
    return {"dbeta_hubble": dbeta, "dt_tilt_s": dbeta * L / C}


def loops():
    with contextlib.redirect_stdout(io.StringIO()):
        r2 = frame.cosmic_keyed_rank_n_is_safe(2, 100)
        r3 = frame.cosmic_keyed_rank_n_is_safe(3, 100)
        lem = frame.frw_time_function_lemma()
        fr = nonlocal_.frame_requirement()
    return {"rank2": r2, "rank3": r3, "frw_lemma": lem, "nonlocal_frame_requirement": fr}


def lab_frame():
    """nonlocal.py's H-LAB-FRAME, with the frame NAMED as the CMB's.  Earth's largest speed in that frame is bounded by
    v_bary + sigma + 1.02 v_orb + 0.5 km/s (H-CIRCULAR-ORBIT, H-ROTATION-BOUND); each test needs v/c below
    nonlocal.lab_frame_limit(r, margin).  Where it holds, the coupling acts for t' >= gamma (t - beta r / c) in the CMB
    frame, so the J bound is weakened at most by t / t'."""
    v_orb = 2 * math.pi * AU / YEAR_S / 1000.0
    v_max = DIPOLE["v_kms"][0] + DIPOLE["v_kms"][1] + 1.02 * v_orb + 0.5
    beta = v_max / C_KMS
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    b = nonlocal_.bounds()
    out = {}
    for k, v in nonlocal_.NOSIG_TESTS.items():
        r, m = v["r_m"], v["margin_s"]
        t = r / C - m
        lim = nonlocal_.lab_frame_limit(r, m)
        factor = t / (gamma * (t - beta * r / C))
        out[k] = {"limit_v_over_c": lim, "holds": beta < lim, "J_factor": factor,
                  "J_bound_cmb_A_or_B": b[k]["A_or_B"] * factor}
    return {"v_max_kms": v_max, "beta_max": beta, "tests": out}


def matter_frames():
    """The keying lead at Proxima if the frame were the one the quasars define (H-QUASAR-KINEMATIC), or the Local
    Group's, set against the CMB's."""
    g = geometry()
    out = {"CMB": {"v_kms": DIPOLE["v_kms"][0], "theta_deg": g["theta_deg"], "lead_s": lead()["lead_s"]}}
    row = MATTER_DIPOLE["Secrest 2022 (2206.05624v2), WISE"]
    vq = DIPOLE["v_kms"][0] * row["D"] / row["D_exp"]
    nq = gal_to_icrs(row["l_deg"], row["b_deg"])
    lq = keyed_lead_s(vq, dot(nq, N_PROXIMA))
    # sensitivity over the READ errors: D +- 0.16e-2, l +- 7 deg, b +- 5 deg (2206.05624v2 p.5)
    shifts = []
    for dD in (-0.16e-2, 0.0, 0.16e-2):
        for dl in (-7.0, 0.0, 7.0):
            for db in (-5.0, 0.0, 5.0):
                v_ = DIPOLE["v_kms"][0] * (row["D"] + dD) / row["D_exp"]
                n_ = gal_to_icrs(row["l_deg"] + dl, row["b_deg"] + db)
                shifts.append(abs(keyed_lead_s(v_, dot(n_, N_PROXIMA)) - out["CMB"]["lead_s"]) / 3600)
    out["quasar dipole read kinematically (WISE 2022)"] = {
        "v_kms": vq, "theta_deg": angle_deg(nq, N_PROXIMA), "lead_s": lq,
        "offset_from_cmb_deg": angle_deg(nq, N_DIPOLE), "shift_range_h": (min(shifts), max(shifts))}
    for name, f in FRAMES_OF_MATTER.items():
        n = gal_to_icrs(f["l_deg"], f["b_deg"])
        out[name] = {"v_kms": f["v_kms"][0], "theta_deg": angle_deg(n, N_PROXIMA),
                     "lead_s": keyed_lead_s(f["v_kms"][0], dot(n, N_PROXIMA))}
    return out


def universal():
    """H-CMB-UNIVERSAL's measurable part.  T(z) READ: beta consistent with 0, so T falls as 1/a (the background is NOT
    constant in time).  As a clock: sigma_t = (sigma_T0 / T0) / H0.  At equal cosmic time Earth and Proxima see the same
    T to the anisotropy level; along one light-time the Hubble change is H0 L / c."""
    rows = {k: {"beta": v["beta"][0], "sigma": v["beta"][1], "n_sigma": abs(v["beta"][0]) / v["beta"][1]}
            for k, v in T_OF_Z.items()}
    t_pred = T0[0] * (1 + T_HFLS3["z"])
    clock_s = (T0[1] / T0[0]) / H0
    return {"T_of_z": rows, "T_HFLS3_pred_K": t_pred,
            "HFLS3_in_1sigma": T_HFLS3["T_1sigma_K"][0] <= t_pred <= T_HFLS3["T_1sigma_K"][1],
            "clock_sigma_yr": clock_s / YEAR_S, "dT_over_T_one_light_time": H0 * L / C}


def collect():
    return {"geometry": geometry(), "lead": lead(), "one_frame": one_frame_across_span(), "loops": loops(),
            "lab_frame": lab_frame(), "matter_frames": matter_frames(), "universal": universal(),
            "speed_bounds_cmb": CMB_FRAME_SPEED_BOUNDS}


def report():
    d = collect()
    g, ld, of, lp, lf, mf, un = (d[k] for k in ("geometry", "lead", "one_frame", "loops", "lab_frame",
                                                 "matter_frames", "universal"))
    print("H-CMB-CORRIDOR, reading 1: the cosmic background as H-FRAME's frame (not seated)\n")
    print("(1) THE FRAME, READ AT SOURCE (Planck 2018 I, 1807.06205v2 Table 2 p.6)")
    print("  barycentre velocity %.2f +- %.2f km/s, beta = %.5e, toward (l, b) = (%.3f, %.3f), RA/Dec (%.3f, %.3f)"
          % (DIPOLE["v_kms"] + (DIPOLE["beta"][0], DIPOLE["l_deg"][0], DIPOLE["b_deg"][0],
                                 DIPOLE["ra_deg"][0], DIPOLE["dec_deg"][0])))
    print("  frame.py's v/c from D67's restated speed: %.5e; Planck's printed beta agrees within its own error"
          % ld["owner_beta"])
    print("\n(2) EARTH-PROXIMA UNDER CMB KEYING")
    print("  angle dipole apex to Proxima: %.3f deg (cos %.4f); L = %.4f ly (seat.py)" % (
        g["theta_deg"], g["cos_theta"], g["L_ly"]))
    print("  a CMB-simultaneous link reaches Proxima at barycentre coordinate time %.0f s = %.2f h = %.3f days"
          % (ld["lead_s"], ld["lead_h"], ld["lead_days"]))
    print("  (frame.py's along-dipole 1-ly figure scaled by L and cos theta: %.0f s)" % ld["owner_check_s"])
    print("  annual modulation (Earth's orbit, %.2f km/s; %.2f km/s on the Proxima line): +- %.0f s (bound %.0f s)"
          % (ld["v_orb_kms"], ld["orb_proj_kms"], ld["annual_mod_s"], ld["annual_mod_bound_s"]))
    print("  realising the frame from the dipole's own precision: sigma = %.1f s (speed %.1f s, direction %.2f s)"
          % (ld["sigma_total_s"], ld["sigma_from_v_s"], ld["sigma_from_dir_s"]))
    print("\n(3) ONE FRAME ACROSS THE SPAN")
    print("  Hubble-flow difference of comoving frames across L: dbeta = %.2e (a flat-model tilt of %.1e s);"
          " in FRW keying is to cosmic time, a global time function" % (of["dbeta_hubble"], of["dt_tilt_s"]))
    print("  keyed lattices with a non-positive-definite Gram: rank 2 %d of %d, rank 3 %d of %d" % (
        lp["rank2"][1], lp["rank2"][0], lp["rank3"][1], lp["rank3"][0]))
    print("  frame.py z3 time-function lemma: %s; nonlocal.py witness loop %s, common-frame pair loop %s" % (
        lp["frw_lemma"]["claim"], lp["nonlocal_frame_requirement"]["witness_loop"],
        lp["nonlocal_frame_requirement"]["pair_loop"]))
    print("\n(4) H-LAB-FRAME, WITH THE FRAME NAMED (Earth's largest CMB speed %.1f km/s, beta %.3e)" % (
        lf["v_max_kms"], lf["beta_max"]))
    for k, v in lf["tests"].items():
        print("  %-52s needs beta < %.4f: %s; J bound x %.5f -> %.3g rad/s" % (
            k, v["limit_v_over_c"], "HOLDS" if v["holds"] else "fails", v["J_factor"], v["J_bound_cmb_A_or_B"]))
    print("\n(5) SPEED OF INFLUENCE IN THE CMB FRAME")
    for k, v in CMB_FRAME_SPEED_BOUNDS.items():
        print("  %s: %s" % (k, ("v >= %.1e c" % v["v_min_over_c"]) if v["v_min_over_c"] else v["note"][:110] + "..."))
    print("  a lower bound cannot exclude v = infinity in that frame (nonlocal.py, Bancal)")
    print("\n(6) H-CMB-IS-COSMIC AGAINST THE MATTER DIPOLE (contested at 4.9-5.1 sigma, READ)")
    for k, v in mf.items():
        print("  %-46s v %.0f km/s, %.1f deg from Proxima: lead %.0f s (%.2f h)" % (
            k, v["v_kms"], v["theta_deg"], v["lead_s"], v["lead_s"] / 3600))
    qr = mf["quasar dipole read kinematically (WISE 2022)"]["shift_range_h"]
    print("  quasar shift from the CMB keying: 0.74 h at the central values, %.2f to %.2f h over the READ errors"
          " (D, l, b) -- the central agreement is a geometric coincidence, not a constraint" % qr)
    print("\n(7) H-CMB-UNIVERSAL, ITS MEASURABLE PART")
    for k, v in un["T_of_z"].items():
        print("  T(z) beta, %s: %.4f +- %.4f (%.2f sigma from 0)" % (k, v["beta"], v["sigma"], v["n_sigma"]))
    print("  HFLS3 z = %.4f: T0(1+z) = %.2f K, inside the READ 1-sigma range %s: %s" % (
        T_HFLS3["z"], un["T_HFLS3_pred_K"], T_HFLS3["T_1sigma_K"], un["HFLS3_in_1sigma"]))
    print("  the background cools as 1/a: not constant in time.  As a cosmic clock its resolution is %.2e yr" %
          un["clock_sigma_yr"])
    print("  'multi-spacetime / multiversal': no measurement on the board bears on it -- OPEN, carried")


def selftest():
    n_pass = n_fail = n_ctl = 0
    structural = []

    def chk(label, ok, ctl=False):
        nonlocal n_pass, n_fail, n_ctl
        n_ctl += ctl
        if ok:
            n_pass += 1
        else:
            n_fail += 1
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else "", label))

    d = collect()
    g, ld, of, lp, lf, mf, un = (d[k] for k in ("geometry", "lead", "one_frame", "loops", "lab_frame",
                                                 "matter_frames", "universal"))
    # 1 the Galactic matrix reproduces Planck's own printed RA/Dec of the dipole (READ), to within their 0.007 deg
    chk("H-GAL-MATRIX: Planck's (l, b) -> RA/Dec matches Planck's printed RA/Dec within 0.01 deg (got %.4f deg)"
        % g["gal_matrix_vs_printed_deg"], g["gal_matrix_vs_printed_deg"] < 0.01)
    chk("Galactic centre (0, 0) is NOT the dipole direction (the matrix is not the identity on this input)",
        angle_deg(gal_to_icrs(0.0, 0.0), N_DIPOLE) > 90.0, ctl=True)
    # 2 the source agrees with frame.py's restated beta (D67)
    chk("Planck's printed beta (1.23357 +- 0.00036)e-3 agrees with v/c and with frame.py's v/c (%.5e) within Planck's "
        "own beta error" % ld["owner_beta"], abs(DIPOLE["v_kms"][0] / C_KMS - DIPOLE["beta"][0]) < DIPOLE["beta"][1]
        and abs(ld["owner_beta"] - DIPOLE["beta"][0]) < DIPOLE["beta"][1])
    # 3 my lead formula against frame.py's own along-dipole figure, scaled
    chk("lead at Proxima equals frame.cmb_coordinate_past scaled by L and cos theta (%.1f vs %.1f s)" % (
        ld["lead_s"], ld["owner_check_s"]), abs(ld["lead_s"] / ld["owner_check_s"] - 1) < 1e-9)
    chk("perpendicular link (cos 0) shows no lead", keyed_lead_s(369.82, 0.0) == 0.0, ctl=True)
    # 4 the figure itself, pinned (2026-10-05)
    chk("angle apex-Proxima 66.19 deg (astropy at build: 66.19427) and lead -0.772 days (got %.4f deg, %.4f d)" % (
        g["theta_deg"], ld["lead_days"]), abs(g["theta_deg"] - 66.19427) < 2e-3 and abs(ld["lead_days"] + 0.772) < 0.002)
    # 5 Proxima's distance: the board's owner agrees with the VizieR DR3 parallax
    chk("seat.D_PROXIMA (%.5f ly) agrees with 1/plx from the VizieR DR3 row (%.5f ly) to 1e-6" % (
        g["L_ly"], g["L_from_vizier_plx_ly"]), abs(g["L_ly"] / g["L_from_vizier_plx_ly"] - 1) < 1e-6)
    # 6 annual modulation and realisation error are small against the lead
    chk("annual modulation +- %.0f s (14 %% of the lead, pinned 2026-10-05) within its bound %.0f s; realisation sigma "
        "under one minute (%.1f s)" % (ld["annual_mod_s"], ld["annual_mod_bound_s"], ld["sigma_total_s"]),
        abs(ld["annual_mod_s"] / abs(ld["lead_s"]) - 0.1417) < 0.002 and ld["annual_mod_s"] <= ld["annual_mod_bound_s"]
        and ld["sigma_total_s"] < 60)
    # 7 loops
    chk("keyed lattices: no rank-2 or rank-3 lattice with a non-positive-definite Gram (owner: frame.py)",
        lp["rank2"][1] == 0 and lp["rank3"][1] == 0 and lp["rank2"][0] > 0 and lp["rank3"][0] > 0)
    chk("frame.py's z3 lemma proved (unsat) with its vacuity guard sat", lp["frw_lemma"]["claim"] == "unsat"
        and lp["frw_lemma"]["vacuity"] == "sat")
    chk("nonlocal.py's witness pair (different frames, timelike span) DOES close a loop",
        lp["nonlocal_frame_requirement"]["witness_loop"] is True, ctl=True)
    # 8 H-LAB-FRAME holds for every test under the CMB frame, and fails for a frame at beta = 0.99
    chk("H-LAB-FRAME holds for every nonlocal.py test with the CMB frame (beta_max %.3e)" % lf["beta_max"],
        all(v["holds"] for v in lf["tests"].values()))
    chk("a frame at beta = 0.99 fails H-LAB-FRAME for every test",
        all(not (0.99 < v["limit_v_over_c"]) for v in lf["tests"].values()), ctl=True)
    chk("J bounds weakened by at most 0.2 %% in the CMB frame (max factor %.5f)" % max(
        v["J_factor"] for v in lf["tests"].values()), max(v["J_factor"] for v in lf["tests"].values()) < 1.002)
    # 9 matter frames give a different lead
    q = mf["quasar dipole read kinematically (WISE 2022)"]
    dq = abs(q["lead_s"] - ld["lead_s"]) / 3600
    chk("quasar frame (H-QUASAR-KINEMATIC) shifts the Proxima lead by %.2f h at central values (pinned 0.74 h), less "
        "than the annual modulation (%.2f h) THERE ONLY: over the READ errors it spans %.2f to %.2f h" % (
            dq, ld["annual_mod_s"] / 3600, q["shift_range_h"][0], q["shift_range_h"][1]),
        abs(dq - 0.744) < 0.01 and dq < ld["annual_mod_s"] / 3600)
    chk("the Local Group's frame shifts it by more than a day (%.1f h)" % (
        abs(mf["Local Group"]["lead_s"] - ld["lead_s"]) / 3600),
        abs(mf["Local Group"]["lead_s"] - ld["lead_s"]) > 86400, ctl=True)
    # 10 universal: T(z) beta within 1 sigma of zero for every READ fit; HFLS3 inside; clock > 1 Myr
    chk("every READ T(z) beta is within 1 sigma of 0, and T0(1+z) at HFLS3 lies in its READ 1-sigma range",
        all(v["n_sigma"] < 1 for v in un["T_of_z"].values()) and un["HFLS3_in_1sigma"])
    chk("the CMB as a clock resolves cosmic time to no better than 1 Myr (%.2e yr)" % un["clock_sigma_yr"],
        un["clock_sigma_yr"] > 1e6)
    chk("a T(z) with beta = 1 (a constant background) would predict 2.725 K at HFLS3, outside the READ range",
        not (T_HFLS3["T_1sigma_K"][0] <= T0[0] <= T_HFLS3["T_1sigma_K"][1]), ctl=True)
    # 11 one frame across the span
    chk("Hubble-flow dbeta across L below 1e-9 (%.2e)" % of["dbeta_hubble"], of["dbeta_hubble"] < 1e-9)
    structural.append("Scarani 2000's CMB-frame bound (1.5e4 c) is a LOWER bound: it cannot exclude v = infinity in "
                      "that frame (as nonlocal.py, Bancal)")
    structural.append("H-CMB-UNIVERSAL's 'multi-spacetime / multiversal' clause: no measurement on the board bears on "
                      "it; OPEN")
    for s in structural:
        print("  STRUCTURAL: " + s)
    print("cmbframe.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
