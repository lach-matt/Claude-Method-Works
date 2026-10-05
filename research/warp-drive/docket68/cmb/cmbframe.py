#!/usr/bin/env python3
"""
cmbframe.py -- H-CMB-CORRIDOR, reading 1: the cosmic background as the corridor's FRAME.

Not seated.  Verified once in both directions (2026-10-05); the findings are applied and the first-written claims kept
under HISTORY.  M (rulings item 41, a question after DOCKET 68's close): "Have we considered the universe's own
background radiation as the means by which the corridor is constructed? As it is likely that background only
multi-spacetime/multiversal constant?"  Carried as M's hypotheses H-CMB-CORRIDOR and H-CMB-UNIVERSAL, never as results.
M (item 42): "3, then 1" -- the Q-1s gate first, then the CMB as the frame.  M, after the first build: "The physics as
it applies to the frame is what matters."  This file takes up that reading only: the background's rest frame as
H-FRAME's preferred frame (M-D68-C10), to which every corridor coupling is keyed.  Whether the background can CARRY or
BUILD the corridor (its photons as the medium, its entropy as the register) is a different reading, not touched here.

    python3 cmbframe.py              report
    python3 cmbframe.py --selftest   checks, with CONTROLS
    python3 cmbframe.py --json       the numbers as JSON

THE PHYSICS OF THE FRAME
  The CMB is a free-streaming thermal photon gas.  A gas has one frame in which its momentum density vanishes, the one
  frame in which it is isotropic.  An observer moving at beta sees T(theta) = T0 / [gamma (1 - beta cos theta)]; the
  dipole's amplitude over T0 IS beta, so each observer measures its own velocity against the gas locally, with no
  signal exchanged.  In FRW the gas cools as 1/a, so the surfaces of equal CMB temperature are the surfaces of equal
  cosmic time: the background defines a simultaneity as well as a direction.  That is a property of the STATE of the
  universe, not of its laws; nothing in physics makes a coupling key to it (H-CMB-AS-FRAME, M's).

WHAT THE BOARD ALREADY HELD (asked of its owners at run time, never retyped)
  frame.py / A2-frame.md: a network keyed to ONE frame closes no causal curve at any rank (a theorem, by Sylvester, true
  of ANY single frame); in exact FRW cosmic time is a global time function on the comoving quotient (z3 lemma); in the de
  Sitter limit the geometry stops selecting a frame and "the cosmic frame is selected by the matter content (the CMB)"
  (A2-frame.md (i)); frame.py priced a cosmic-simultaneous 1-ly corridor along the dipole from a dipole
  READ-VIA-RESTATEMENT (D67).  step1c/nonlocal.py: an instantaneous coupling is loop-free iff all couplings share one
  simultaneity frame; its J bounds from spacelike Bell tests carry H-LAB-FRAME.  seat.py: Proxima's distance.  cosmo.py:
  H0 (PINNED Planck 2018).  CLOSE.md section 1: under H-SETTLE x H-FRAME, O-BITS is REMOVED-IF {W2, F1}.

WHAT IS NEW HERE
  (1) The dipole READ at source (Planck 2018 I, 1807.06205v2), upgrading frame.py's READ-VIA-RESTATEMENT; the identity
      beta = amplitude / T0 checked across two READ papers.
  (2) Earth-Proxima: the apex-Proxima angle and the lead a CMB-keyed link shows in barycentre coordinate time; the
      modulation in Earth's momentary rest frame (annual, diurnal); the realisation error the dipole's precision sets,
      and the epoch, light-time, radial-velocity and parallax terms beside it.
  (3) One frame across the span: the Hubble-flow difference, and why in FRW it does not matter.
  (4) H-LAB-FRAME, asked of nonlocal.py with the frame NAMED as the CMB's: computed, under named conditions.
  (5) The speed-of-influence bound actually evaluated in the CMB frame (Scarani 2000), and what it does not exclude.
  (6) H-CMB-IS-COSMIC and the matter dipole: two readings carried -- (a) intrinsic matter anisotropy, the CMB frame
      stays the kinematic frame (the source's own preferred reading, and it supports M); (b) kinematic, the frames
      differ, and the keying difference at Proxima is sized.  The Local Group and Galactic-centre frames priced.
  (7) H-CMB-UNIVERSAL's measurable part: T(z) = T0 (1+z)^(1-beta), so the background is not constant in time; its frame
      and spectral form are shared by all comoving observers; its temperature cannot synchronise the corridor's ends
      (the differential precision needed is computed), its dipole with light signals can.  The "multi-spacetime /
      multiversal" part has no measurement on the board: OPEN.

NAMED HYPOTHESES
  H-CMB-AS-FRAME     M's reading: H-FRAME's preferred frame is the CMB rest frame (the dipole-free frame).
  H-CMB-IS-COSMIC    the CMB rest frame is FRW's comoving frame (D67 H1: the dipole is kinematic).
  H-BARYCENTRE       Planck's velocity is the Solar-System barycentre's (D67 H2).
  H-AT-REST-ENDPOINT the far end at rest in the barycentre frame at the instant priced; then t' = -v.x'/c^2 is exact
                     (no gamma); Proxima's own motion enters as the epoch and radial-velocity terms.
  H-EPOCH            Gaia DR3's epoch 2016.0 reckoned to 2026.0 for the epoch terms.
  H-CIRCULAR-ORBIT   Earth's orbital speed taken as 2 pi AU / yr; perihelion speed is about 1.017 x that (MEMORY-NOT-
                     READ), covered by a 2 % margin wherever a bound is drawn.
  H-OBLIQUITY        the ecliptic pole at Dec 90 - 23.4392911 deg (IAU 1976 obliquity, MEMORY-NOT-READ; cross-checked
                     against astropy at build, below); used only for the annual modulation's projection.
  H-ROTATION         Earth's equatorial rotation speed 0.465 km/s (MEMORY-NOT-READ); the bound uses 0.5 km/s.
  H-GAL-MATRIX       the Hipparcos Galactic->ICRS rotation (ESA 1997, MEMORY-NOT-READ), CHECKED against Planck's own
                     printed RA/Dec of the dipole (READ) and against astropy at build.
  H-LINEAR-ERRORS    Planck's errors are linear sums of statistical and systematic parts (Table 2 fn e, p.6), not
                     Gaussian 1-sigma; the realisation term treats them as 1-sigma.
  H-QUASAR-KINEMATIC reading (b) only: the WHOLE quasar dipole is kinematic, its axis the velocity axis, and
                     v_q = v_CMB x D_obs / D_exp (D = [2 + x(1+alpha)] beta is linear in beta; Secrest's D_exp is
                     computed at v = 369.82 km/s with the sample's x, alpha); D_exp's two printed digits (about +-0.7 %
                     in v_q) are not propagated.
  H-INSTANTANEOUS-IN-FRAME, H-J-PER-FRAME-TIME  for (4): the coupling is instantaneous (v = infinity) in the CMB frame,
                     and J is defined per CMB-frame time.
  H-CORRIDOR-MODEL, H-FRW-EXACT, H-NOT-DE-SITTER (frame.py); H-CORRIDOR-MAP, H-SETTING-DEPENDENCE, H-UNIVERSAL-COUPLING,
  H-J-DISTANCE-FREE (nonlocal.py).

HISTORY (first build and the verifier, 2026-10-05; first-written claims kept):
  * 'Planck's beta equals v/c to 1e-5 relative' -- failed at the first build: they differ by 1.36e-5 relative (first
    written here as 1.6e-5; the verifier's figure is the right one), inside Planck's own beta error.  The next check
    compared v/c with frame.py's v/c -- a tautology (frame.py was handed Planck's v); now the check is the physics
    identity beta = amplitude / T0 across two READ papers.
  * 'The annual modulation is under 3 % of the lead; the realisation sigma under 30 s' -- failed at the first build;
    then 'Earth's orbit modulates this [the barycentre-time lead] by +- 9,453 s' -- WRONG FRAME (verifier): in
    barycentre coordinate time the lead does not modulate (Earth's offset adds <= 0.6 s); +- 9,453 s is the modulation
    in Earth's momentary rest frame.
  * 'The quasar frame shifts the lead by more than an hour' -- failed at the first build (0.74 h); then '0.28 to 13.3 h
    over the READ errors' -- a GRID ARTEFACT (verifier): the signed shift crosses zero inside the box, so the range is
    0 to 13.3 h.
  * 'The Local Group's frame shifts the lead by 30 h' -- WRONG VELOCITY (verifier): the lead needs the barycentre's
    velocity relative to the keyed frame, v_Sun-CMB - v_LG-CMB (which reproduces Planck Table 3's Sun-LG row), not
    v_LG-CMB.  Corrected: the LG-keyed lead is in the barycentre's coordinate FUTURE and the shift is 48 h.
  * 'Realisation sigma 35.4 s' -- OVERSTATED (verifier): the 0.02 % T0 term applies to the amplitude in uK, not to the
    velocity (Planck I p.6), and only the direction error in the apex-Proxima plane moves cos theta.  It is a
    dipole-precision term only; the epoch, diurnal, light-time and radial-velocity terms are of the same size or larger.
  * 'It can name the frame, but it cannot synchronise the corridor's ends' -- conflated the temperature clock with the
    frame (verifier): the temperature cannot (it would need dT/T ~ 1e-13); the dipole with light signals can, to the
    dipole term.
  * 'H-CMB-IS-COSMIC is contested by READ data' -- OVERSTATED (verifier): Secrest 2022 rejects matter's isotropy in the
    CMB frame and itself reads it as intrinsic anisotropy there; both readings are now carried.
  * The lead carried gamma (as frame.py does, for a CMB-frame displacement); with L measured in the barycentre frame the
    exact form has none.  The difference is 0.05 s.
  * Vacuous checks (verifier): a perpendicular-link 'control' (multiplies by 0), a 'Galactic centre is not the dipole'
    control, the keyed-lattice sample (a theorem for ANY frame, now STRUCTURAL), a beta = 0.99 control that never ran
    lab_frame(), and the Local Group 'control'.  Replaced by real ones.  The HFI ' +- 0.0010 km/s' was described as
    'statistical-scale' -- that is a reader's description, not the source's.

BUILD-TIME CROSS-CHECK (astropy 7, pip, NOT a dependency; run once 2026-10-05, values recorded, not re-run here):
  Galactic (264.021, 48.253) -> ICRS (167.94190, -6.94426); Proxima (Gaia DR3) ecliptic latitude -44.7677 deg;
  separation dipole-apex to Proxima 66.19427 deg.  The verifier recomputed the pins independently and agreed.
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
PC_M = 3.0856775814913673e16

# ---------------------------------------------------------------------------------------------------------------------
# READ at source (2026-10-05).  Routes: alphaXiv answer_pdf_queries (arXiv PDF page text); VizieR via Firecrawl.
# Planck I Table 2/3 re-read by the verifier.
# ---------------------------------------------------------------------------------------------------------------------
DIPOLE = {   # Planck 2018 I, arXiv:1807.06205v2: Table 2 p.6 ("Planck 2018" row) and its footnote e; text p.6.
    "v_kms": (369.82, 0.11), "beta": (1.23357e-3, 0.00036e-3), "amp_uK": (3362.08, 0.99),
    "l_deg": (264.021, 0.011), "b_deg": (48.253, 0.005), "ra_deg": (167.942, 0.007), "dec_deg": (-6.944, 0.007),
    "source": "1807.06205v2 Table 2 p.6, fn. e (RA/Dec J2000; errors are stat + syst added linearly and exclude the "
              "0.02 % T0 uncertainty, which applies to the amplitude in uK, p.6); p.6 text (beta, v)",
    "hfi_eq10": "1807.06207v1 eq. (10) p.25: v = 369.8160 +- 0.0010 km/s, an error the source does not label and that "
                "does not match the amplitude's linear sum (verifier); Planck I's +- 0.11 km/s is used"}
SUN_LG_TABLE3 = {"v_kms": (299.0, 15.0), "l_deg": (98.4, 3.6), "b_deg": (-5.9, 3.0),
                 "page": "1807.06205v2 Table 3 p.7 (Sun-LG from Diaz et al. 2014; re-read by the verifier)"}
FRAMES_OF_MATTER = {   # Planck 2018 I Table 3 p.7: velocity of the frame's origin relative to the CMB
    "Local Group": {"v_kms": (620.0, 15.0), "l_deg": 271.9, "b_deg": 29.6},
    "Galactic centre": {"v_kms": (565.0, 5.0), "l_deg": 265.76, "b_deg": 28.38}}
T0 = (2.72548, 0.00057)   # Fixsen 2009, arXiv:0911.1955v2, abstract p.1, Table 2 'Mean' p.5
T_OF_Z = {   # T(z) = T0 (1+z)^(1-beta)
    "Avgoustidis 2016 (1511.04335v1), SZ+QSO+distance duality": {"beta": (7.6e-3, 8.0e-3),
                                                                  "page": "abstract p.1; Table III p.6"},
    "Avgoustidis 2016, direct data only": {"beta": (4.6e-3, 8.9e-3), "page": "Table II p.4"},
    "Riechers 2022 (2202.00693v1), combined fit": {"beta": (3.4e-3, 7.3e-3), "beta_plus": 8.1e-3,
                                                   "page": "Fig. 4 caption p.7 (the lower error, 7.3e-3, used: the "
                                                           "side toward 0)"},
}
T_HFLS3 = {"z": 6.3369, "T_1sigma_K": (16.4, 30.2), "predicted_K": 20.0,
           "page": "2202.00693v1 p.3, Fig. 1 p.5 (z), p.1 (20.0 K); the id first given to the reader, 2201.00693, "
                   "was wrong (a CS paper; the reader caught it)"}
MATTER_DIPOLE = {
    "Secrest 2021 (2009.14826v2)": {"D": 0.01554, "D_exp": 0.007, "l_deg": 238.2, "b_deg": 28.8, "sigma": 4.9,
                                    "page": "p.5 (D, direction, 27.8 deg from the CMB dipole, p = 5e-7); D_exp '~0.007'"
                                            " from eq. 1 p.2 (rounded)"},
    "Secrest 2022 (2206.05624v2), WISE": {"D": (1.48e-2, 0.16e-2), "D_exp": 0.73e-2, "l_deg": (238.0, 7.0),
                                           "b_deg": (31.0, 5.0), "sigma": 4.4, "page": "p.5 (re-read by the verifier)"},
    "Secrest 2022, joint WISE+NVSS": {"sigma": 5.1, "page": "p.5, abstract p.1"},
    "Secrest 2022, the source's own reading": {
        "text": "consistency improves on boosting to the CMB frame assuming the CMB dipole fully kinematic, 'suggesting "
                "... intrinsic anisotropy in this frame' (abstract p.1; p.6; conclusion 3 p.7; verifier-READ)"},
    "Secrest et al. 2025 colloquium (2505.23526v2)": {"sigma_text": "'now exceeds 5 sigma' (p.1); '~6.4 sigma' "
                                                                    "combining Wagenveld 2023a (p.14)"},
}
PROXIMA_DIR = {   # Gaia DR3 (VizieR I/355/gaiadr3, doi:10.26093/cds/vizier.1355), source_id 5853498713190525696
    "ra_deg": 217.39232147201, "dec_deg": -62.67607511677, "epoch": 2016.0, "plx_mas": (768.0665, 0.0499),
    "rv_kms": (-21.94, 0.22), "pm_mas_yr": (-3781.741, 769.465),
    "rv_kervella2017": "-22.204 +- 0.032 km/s, corrected for convective blueshift and gravitational redshift "
                       "(1611.03495v3 Table 2 p.4)"}
CMB_FRAME_SPEED_BOUNDS = {
    "Scarani, Tittel, Zbinden, Gisin 2000 (quant-ph/0007008v1)": {
        "v_min_over_c": 1.5e4, "page": "abstract p.1; Sec. 4-5 p.5",
        "note": "Geneva, 10.6 km; detections simultaneous in the CMB frame near 3h UTC; tau not monitored, linearly "
                "interpolated (a stated assumption, p.5); CMB velocity taken as 371 km/s (Lineweaver 1996, p.3)"},
    "Salart et al. 2008 (0808.3316v1)": {
        "v_min_over_c": None, "page": "abstract p.1; p.5; Fig. 5 caption",
        "note": "states >= 1e4 c in every direction for beta = 1e-3 and 54000 c at chi = 90 deg; Earth's CMB-frame "
                "beta (computed below) lies just outside that headline condition and no CMB-frame figure is printed; "
                "a reader's own evaluation at the CMB beta (~4.6e4 c) is reader-COMPUTED, not used"},
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
V_ROT_KMS = 0.465            # H-ROTATION (MEMORY-NOT-READ)


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def scale(u, s):
    return tuple(a * s for a in u)


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def norm(u):
    return math.sqrt(dot(u, u))


def unit(ra_deg, dec_deg):
    a, d = math.radians(ra_deg), math.radians(dec_deg)
    return (math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d))


def radec(u):
    n = norm(u)
    ra = math.degrees(math.atan2(u[1], u[0])) % 360.0
    return ra, math.degrees(math.asin(max(-1.0, min(1.0, u[2] / n))))


def _AT(g):
    return tuple(sum(_A[k][i] * g[k] for k in range(3)) for i in range(3))


def gal_to_icrs(l_deg, b_deg, transpose=True):
    """A^T g (the inverse rotation).  transpose=False applies A instead -- the CONTROL that must miss."""
    g = unit(l_deg, b_deg)
    if transpose:
        return _AT(g)
    return tuple(sum(_A[i][k] * g[k] for k in range(3)) for i in range(3))


def icrs_to_gal(u):
    return tuple(sum(_A[i][k] * u[k] for k in range(3)) for i in range(3))


def angle_deg(u, v):
    return math.degrees(math.acos(max(-1.0, min(1.0, dot(u, v) / (norm(u) * norm(v))))))


N_DIPOLE = unit(DIPOLE["ra_deg"][0], DIPOLE["dec_deg"][0])
N_PROXIMA = unit(PROXIMA_DIR["ra_deg"], PROXIMA_DIR["dec_deg"])
N_ECL_POLE = unit(270.0, 90.0 - OBLIQUITY_DEG)
V_SUN_CMB = scale(N_DIPOLE, DIPOLE["v_kms"][0])          # km/s, ICRS


def lead_from_velocity(v_vec_kms, n=N_PROXIMA, L_m=L):
    """H-AT-REST-ENDPOINT: the keyed frame's simultaneity hyperplane, seen from the barycentre frame moving at v
    relative to it, is t' = -v.x'/c^2 -- exact for an endpoint at rest in the barycentre frame at x' = L n.  Negative =
    the far end is reached in the barycentre's coordinate past (clause 2a, spacelike, no loop)."""
    return -dot(v_vec_kms, n) * 1000.0 * L_m / (C * C)


# ---------------------------------------------------------------------------------------------------------------------
# results
# ---------------------------------------------------------------------------------------------------------------------
def physics():
    """beta = amplitude / T0 (two READ papers); the Doppler-shifted temperature ahead, across, behind."""
    beta = DIPOLE["amp_uK"][0] * 1e-6 / T0[0]
    sb = beta * math.hypot(DIPOLE["amp_uK"][1] / DIPOLE["amp_uK"][0], T0[1] / T0[0])
    g = 1.0 / math.sqrt(1.0 - beta * beta)
    temps = {th: T0[0] / (g * (1.0 - beta * math.cos(math.radians(th)))) for th in (0, 90, 180)}
    return {"beta_from_amp_over_T0": beta, "sigma": sb, "beta_printed": DIPOLE["beta"], "T_ahead_across_behind": temps}


def geometry():
    th = angle_deg(N_DIPOLE, N_PROXIMA)
    gal = gal_to_icrs(DIPOLE["l_deg"][0], DIPOLE["b_deg"][0])
    bad = gal_to_icrs(DIPOLE["l_deg"][0], DIPOLE["b_deg"][0], transpose=False)
    return {"theta_deg": th, "cos_theta": dot(N_DIPOLE, N_PROXIMA), "gal_matrix_dipole_radec": radec(gal),
            "gal_matrix_vs_printed_deg": angle_deg(gal, N_DIPOLE),
            "untransposed_vs_printed_deg": angle_deg(bad, N_DIPOLE),
            "proxima_ecliptic_lat_deg": 90.0 - angle_deg(N_PROXIMA, N_ECL_POLE),
            "L_ly": L / LY, "L_from_vizier_plx_ly": (PC_M / (PROXIMA_DIR["plx_mas"][0] / 1000.0)) / LY}


def _dir_sigma_rad():
    """The dipole-direction error projected on the great circle from the apex toward Proxima (only that component
    moves cos theta), from Planck's (l, b) errors (H-LINEAR-ERRORS)."""
    l, b = math.radians(DIPOLE["l_deg"][0]), math.radians(DIPOLE["b_deg"][0])
    e_l = _AT((-math.sin(l), math.cos(l), 0.0))
    e_b = _AT((-math.sin(b) * math.cos(l), -math.sin(b) * math.sin(l), math.cos(b)))
    c = dot(N_DIPOLE, N_PROXIMA)
    t = sub(N_PROXIMA, scale(N_DIPOLE, c))
    t = scale(t, 1.0 / norm(t))
    s_l = math.radians(DIPOLE["l_deg"][1]) * math.cos(b) * dot(t, e_l)
    s_b = math.radians(DIPOLE["b_deg"][1]) * dot(t, e_b)
    return math.hypot(s_l, s_b)


def epoch_terms():
    """H-EPOCH: Gaia's 2016.0 direction and distance moved to 2026.0 by the READ proper motion and radial velocity;
    the light-time term (the geometric position is 4.25 yr of proper motion ahead of the apparent one); parallax."""
    a, d = math.radians(PROXIMA_DIR["ra_deg"]), math.radians(PROXIMA_DIR["dec_deg"])
    e_a = (-math.sin(a), math.cos(a), 0.0)
    e_d = (-math.sin(d) * math.cos(a), -math.sin(d) * math.sin(a), math.cos(d))
    mas = math.radians(1.0 / 3.6e6)
    pa, pd = PROXIMA_DIR["pm_mas_yr"]

    def moved(years):
        n = tuple(N_PROXIMA[i] + (pa * e_a[i] + pd * e_d[i]) * mas * years for i in range(3))
        return scale(n, 1.0 / norm(n))
    base = lead_from_velocity(V_SUN_CMB)
    pm10 = lead_from_velocity(V_SUN_CMB, moved(10.0)) - base
    lt = lead_from_velocity(V_SUN_CMB, moved(L / C / YEAR_S)) - base
    L10 = L + PROXIMA_DIR["rv_kms"][0] * 1000.0 * 10.0 * YEAR_S
    rv10 = lead_from_velocity(V_SUN_CMB, N_PROXIMA, L10) - base
    plx = abs(base) * PROXIMA_DIR["plx_mas"][1] / PROXIMA_DIR["plx_mas"][0]
    return {"proper_motion_2016_to_2026_s": pm10, "light_time_position_s": lt, "radial_velocity_per_decade_s": rv10,
            "parallax_sigma_s": plx}


def lead():
    g = geometry()
    v = DIPOLE["v_kms"][0]
    t = lead_from_velocity(V_SUN_CMB)
    owner_1ly, owner_beta = frame.cmb_coordinate_past(1.0, v)      # frame.py keeps gamma (a CMB-frame displacement)
    owner_scaled = owner_1ly * (L / LY) * g["cos_theta"]
    # modulation in Earth's MOMENTARY REST FRAME; in barycentre coordinate time the lead is fixed
    v_orb = 2 * math.pi * AU / YEAR_S / 1000.0
    proj = v_orb * math.cos(math.radians(g["proxima_ecliptic_lat_deg"]))
    t_mod = proj / C_KMS * L / C
    t_mod_bound = 1.02 * v_orb / C_KMS * L / C
    bary_offset = v * 1000.0 * AU / (C * C)                       # Earth's offset from the barycentre, <= this
    diurnal_eq = V_ROT_KMS * math.cos(math.radians(PROXIMA_DIR["dec_deg"])) / C_KMS * L / C
    # dipole-precision term only (H-LINEAR-ERRORS)
    s_from_v = DIPOLE["v_kms"][1] / C_KMS * L * abs(g["cos_theta"]) / C
    s_from_dir = v / C_KMS * L * math.sin(math.radians(g["theta_deg"])) * _dir_sigma_rad() / C
    return {"lead_s": t, "lead_h": t / 3600.0, "lead_days": t / 86400.0, "owner_scaled_s": owner_scaled,
            "owner_beta": owner_beta, "v_orb_kms": v_orb, "orb_proj_kms": proj, "annual_mod_earth_frame_s": t_mod,
            "annual_mod_bound_s": t_mod_bound, "barycentre_time_offset_bound_s": bary_offset,
            "diurnal_equator_earth_frame_s": diurnal_eq, "sigma_from_v_s": s_from_v, "sigma_from_dir_s": s_from_dir,
            "sigma_dipole_s": math.hypot(s_from_v, s_from_dir), "epoch_terms": epoch_terms()}


def one_frame_across_span():
    """Comoving observers at Earth and Proxima differ by the Hubble flow, dbeta = H0 L / c.  In the flat lattice model
    that is a tilt; in exact FRW the keying is to cosmic time, a global time function (frame.py's z3 lemma)."""
    dbeta = H0 * L / C
    return {"dbeta_hubble": dbeta, "dt_tilt_s": dbeta * L / C}


def loops():
    with contextlib.redirect_stdout(io.StringIO()):
        r2 = frame.cosmic_keyed_rank_n_is_safe(2, 100)
        r3 = frame.cosmic_keyed_rank_n_is_safe(3, 100)
        lem = frame.frw_time_function_lemma()
        fr = nonlocal_.frame_requirement()
    return {"rank2": r2, "rank3": r3, "frw_lemma": lem, "nonlocal_frame_requirement": fr}


def earth_cmb_speed_range():
    v_orb = 2 * math.pi * AU / YEAR_S / 1000.0
    v = DIPOLE["v_kms"][0]
    return {"min_kms": v - DIPOLE["v_kms"][1] - 1.02 * v_orb - 0.5,
            "max_kms": v + DIPOLE["v_kms"][1] + 1.02 * v_orb + 0.5}


def lab_frame(v_max_kms=None):
    """nonlocal.py's H-LAB-FRAME, with the frame NAMED as the CMB's.  v_max is an UPPER BOUND on Earth's speed in that
    frame (H-CIRCULAR-ORBIT margin, H-ROTATION bound; A2-frame.md's D67 range is 340.65-399.08 km/s).  Each test needs
    v/c below nonlocal.lab_frame_limit(r, margin).  Under H-INSTANTANEOUS-IN-FRAME and H-J-PER-FRAME-TIME, Alice's
    setting at frame time 0 and Bob's measurement at gamma (t - beta r / c) give J <= asin(sqrt(delta)) / that, so the
    bound is weakened at most by t / [gamma (t - beta r / c)] (frame moving along the A-B axis: the worst case)."""
    if v_max_kms is None:
        v_max_kms = earth_cmb_speed_range()["max_kms"]
    beta = v_max_kms / C_KMS
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    b = nonlocal_.bounds()
    out = {}
    for k, v in nonlocal_.NOSIG_TESTS.items():
        r, m = v["r_m"], v["margin_s"]
        t = r / C - m
        lim = nonlocal_.lab_frame_limit(r, m)
        holds = beta < lim
        factor = t / (gamma * (t - beta * r / C)) if holds else float("inf")
        out[k] = {"limit_v_over_c": lim, "holds": holds, "J_factor": factor,
                  "J_bound_cmb_A_or_B": b[k]["A_or_B"] * factor}
    return {"v_max_kms": v_max_kms, "beta_max": beta, "tests": out}


def matter_frames():
    """Reading (b): the keying lead at Proxima if the frame were another.  The barycentre's velocity RELATIVE TO the
    keyed frame enters: v_Sun-CMB - v_frame-CMB for the Table 3 frames; for the quasar frame read kinematically
    (H-QUASAR-KINEMATIC) the quasar dipole IS the barycentre's velocity relative to it."""
    base = lead_from_velocity(V_SUN_CMB)
    out = {"CMB": {"v_rel_kms": DIPOLE["v_kms"][0], "lead_s": base, "shift_h": 0.0}}
    for name, f in FRAMES_OF_MATTER.items():
        v_f = scale(gal_to_icrs(f["l_deg"], f["b_deg"]), f["v_kms"][0])
        rel = sub(V_SUN_CMB, v_f)
        lg, bg = radec(icrs_to_gal(rel))
        ld = lead_from_velocity(rel)
        out[name] = {"v_rel_kms": norm(rel), "rel_l_b_deg": (lg, bg), "lead_s": ld, "shift_h": (ld - base) / 3600}
    row = MATTER_DIPOLE["Secrest 2022 (2206.05624v2), WISE"]
    D, sD = row["D"]
    l0, sl = row["l_deg"]
    b0, sbb = row["b_deg"]

    def q_lead(Dv, lv, bv):
        vq = DIPOLE["v_kms"][0] * Dv / row["D_exp"]
        return lead_from_velocity(scale(gal_to_icrs(lv, bv), vq))
    lq = q_lead(D, l0, b0)
    shifts = [(q_lead(D + i * sD, l0 + j * sl, b0 + k * sbb) - base) / 3600
              for i in (-1, 0, 1) for j in (-1, 0, 1) for k in (-1, 0, 1)]
    out["quasar dipole read kinematically (WISE 2022)"] = {
        "v_rel_kms": DIPOLE["v_kms"][0] * D / row["D_exp"],
        "offset_from_cmb_deg": angle_deg(gal_to_icrs(l0, b0), N_DIPOLE), "lead_s": lq, "shift_h": (lq - base) / 3600,
        "signed_shift_range_h": (min(shifts), max(shifts)), "crosses_zero": min(shifts) < 0 < max(shifts)}
    return out


def universal():
    """H-CMB-UNIVERSAL's measurable part.  T(z) READ: beta consistent with 0, so T falls as 1/a.  As a clock: the
    absolute calibration resolves cosmic time to (sigma_T0/T0)/H0 (shared by both ends); the DIFFERENTIAL precision a
    temperature synchronisation of the ends would need is H0 x (the interval to resolve)."""
    rows = {k: {"beta": v["beta"][0], "sigma": v["beta"][1], "n_sigma": abs(v["beta"][0]) / v["beta"][1]}
            for k, v in T_OF_Z.items()}
    t_pred = T0[0] * (1 + T_HFLS3["z"])
    ld = lead()
    rel = T0[1] / T0[0]
    return {"T_of_z": rows, "T_HFLS3_pred_K": t_pred,
            "HFLS3_in_1sigma": T_HFLS3["T_1sigma_K"][0] <= t_pred <= T_HFLS3["T_1sigma_K"][1],
            "clock_absolute_sigma_yr": rel / H0 / YEAR_S, "dT_over_T_per_second": H0,
            "fixsen_relative_precision": rel, "slicing_gap_orders": math.log10(rel / H0),
            "dT_over_T_to_resolve_lead": H0 * abs(ld["lead_s"]),
            "dT_over_T_to_resolve_dipole_sigma": H0 * ld["sigma_dipole_s"],
            "dT_over_T_one_light_time": H0 * L / C}


def collect():
    return {"physics": physics(), "geometry": geometry(), "lead": lead(), "one_frame": one_frame_across_span(),
            "loops": loops(), "earth_cmb_speed": earth_cmb_speed_range(), "lab_frame": lab_frame(),
            "matter_frames": matter_frames(), "universal": universal(), "speed_bounds_cmb": CMB_FRAME_SPEED_BOUNDS}


def report():
    d = collect()
    ph, g, ld, of, lp, es, lf, mf, un = (d[k] for k in ("physics", "geometry", "lead", "one_frame", "loops",
                                                         "earth_cmb_speed", "lab_frame", "matter_frames", "universal"))
    print("H-CMB-CORRIDOR, reading 1: the cosmic background as H-FRAME's frame (verified once; not seated)\n")
    print("(1) THE FRAME, READ AT SOURCE (Planck 2018 I, 1807.06205v2 Table 2 p.6) -- upgrades frame.py's D67 "
          "READ-VIA-RESTATEMENT")
    print("  barycentre velocity %.2f +- %.2f km/s, beta = %.5e, toward (l, b) = (%.3f, %.3f), RA/Dec (%.3f, %.3f)"
          % (DIPOLE["v_kms"] + (DIPOLE["beta"][0], DIPOLE["l_deg"][0], DIPOLE["b_deg"][0],
                                 DIPOLE["ra_deg"][0], DIPOLE["dec_deg"][0])))
    print("  the physics: beta = dipole amplitude / T0 = %.2f uK / %.5f K = %.6e (+- %.1e); Planck prints %.5e" % (
        DIPOLE["amp_uK"][0], T0[0], ph["beta_from_amp_over_T0"], ph["sigma"], DIPOLE["beta"][0]))
    print("  an observer moving at that beta sees %.5f K ahead, %.5f K across, %.5f K behind" % tuple(
        ph["T_ahead_across_behind"][k] for k in (0, 90, 180)))
    print("\n(2) EARTH-PROXIMA UNDER CMB KEYING")
    print("  angle dipole apex to Proxima: %.3f deg (cos %.4f); L = %.4f ly (seat.py)" % (
        g["theta_deg"], g["cos_theta"], g["L_ly"]))
    print("  a CMB-simultaneous link reaches Proxima at barycentre coordinate time %.0f s = %.2f h (clause 2a: "
          "coordinate past, spacelike, no loop)" % (ld["lead_s"], ld["lead_h"]))
    print("  in barycentre time the lead is fixed (Earth's offset from the barycentre adds <= %.2f s)" %
          ld["barycentre_time_offset_bound_s"])
    print("  in Earth's MOMENTARY REST FRAME: annual +- %.0f s (orbit %.2f km/s, %.2f on the Proxima line; bound "
          "%.0f s); diurnal up to +- %.0f s at the equator" % (
              ld["annual_mod_earth_frame_s"], ld["v_orb_kms"], ld["orb_proj_kms"], ld["annual_mod_bound_s"],
              ld["diurnal_equator_earth_frame_s"]))
    print("  dipole-precision term only: sigma = %.1f s (speed %.1f s, direction in the apex-Proxima plane %.1f s)"
          % (ld["sigma_dipole_s"], ld["sigma_from_v_s"], ld["sigma_from_dir_s"]))
    e = ld["epoch_terms"]
    print("  beside it (H-EPOCH): proper motion 2016->2026 %+.1f s; light-time position %+.1f s; radial velocity "
          "%+.1f s per decade; parallax sigma %.1f s" % (e["proper_motion_2016_to_2026_s"], e["light_time_position_s"],
                                                          e["radial_velocity_per_decade_s"], e["parallax_sigma_s"]))
    print("\n(3) ONE FRAME ACROSS THE SPAN")
    print("  Hubble-flow difference of comoving frames across L: dbeta = %.2e (a flat-model tilt of %.1e s); in FRW "
          "keying is to cosmic time, a global time function" % (of["dbeta_hubble"], of["dt_tilt_s"]))
    print("  frame.py z3 time-function lemma: %s (vacuity %s, control %s)" % (
        lp["frw_lemma"]["claim"], lp["frw_lemma"]["vacuity"], lp["frw_lemma"]["control_a_ge_0"]))
    print("  nonlocal.py: witness pair (two frames, timelike span) loop %s; common-frame pair loop %s" % (
        lp["nonlocal_frame_requirement"]["witness_loop"], lp["nonlocal_frame_requirement"]["pair_loop"]))
    print("\n(4) H-LAB-FRAME, WITH THE FRAME NAMED (Earth's CMB speed %.1f-%.1f km/s; upper bound used, beta %.3e)" % (
        es["min_kms"], es["max_kms"], lf["beta_max"]))
    for k, v in lf["tests"].items():
        print("  %-52s needs beta < %.4f: %s; J bound x %.5f -> %.3g rad/s" % (
            k, v["limit_v_over_c"], "HOLDS" if v["holds"] else "fails", v["J_factor"], v["J_bound_cmb_A_or_B"]))
    print("  given H-CMB-AS-FRAME, H-BARYCENTRE, H-INSTANTANEOUS-IN-FRAME, H-J-PER-FRAME-TIME, and nonlocal.py's "
          "H-SETTING-DEPENDENCE, H-UNIVERSAL-COUPLING, H-J-DISTANCE-FREE")
    print("\n(5) SPEED OF INFLUENCE IN THE CMB FRAME (Earth's CMB beta %.2e-%.2e)" % (
        es["min_kms"] / C_KMS, es["max_kms"] / C_KMS))
    for k, v in CMB_FRAME_SPEED_BOUNDS.items():
        print("  %s: %s" % (k, ("v >= %.1e c" % v["v_min_over_c"]) if v["v_min_over_c"] else v["note"][:110] + "..."))
    print("  a lower bound cannot exclude v = infinity in that frame (nonlocal.py, Bancal)")
    print("\n(6) H-CMB-IS-COSMIC AND THE MATTER DIPOLE (matter's isotropy in the CMB frame rejected at 4.9-5.1 sigma)")
    print("  reading (a), the source's own: intrinsic matter anisotropy in the CMB frame -- the CMB frame stays the "
          "kinematic frame")
    print("  reading (b), kinematic: the frames differ; the lead at Proxima under each frame:")
    for k, v in mf.items():
        print("    %-46s barycentre at %.0f km/s relative to it: lead %+.0f s (%+.2f h), shift from CMB %+.2f h" % (
            k, v["v_rel_kms"], v["lead_s"], v["lead_s"] / 3600, v["shift_h"]))
    q = mf["quasar dipole read kinematically (WISE 2022)"]
    print("  quasar shift over a +-1 sigma box in (D, l, b) (corners at sqrt(3) sigma): %+.2f to %+.2f h -- crosses "
          "zero, so 0 to %.1f h; the central 0.74 h is a geometric coincidence, not a constraint" % (
              q["signed_shift_range_h"][0], q["signed_shift_range_h"][1],
              max(abs(x) for x in q["signed_shift_range_h"])))
    print("  Local Group check: v_Sun - v_LG = %.1f km/s toward (l, b) = (%.1f, %.1f); Table 3 prints Sun-LG 299 +- 15 "
          "at (98.4, -5.9)" % ((mf["Local Group"]["v_rel_kms"],) + mf["Local Group"]["rel_l_b_deg"]))
    print("\n(7) H-CMB-UNIVERSAL, ITS MEASURABLE PART")
    for k, v in un["T_of_z"].items():
        print("  T(z) beta, %s: %.4f +- %.4f (%.2f sigma from 0)" % (k, v["beta"], v["sigma"], v["n_sigma"]))
    print("  HFLS3 z = %.4f: T0(1+z) = %.2f K, inside the READ 1-sigma range %s: %s" % (
        T_HFLS3["z"], un["T_HFLS3_pred_K"], T_HFLS3["T_1sigma_K"], un["HFLS3_in_1sigma"]))
    print("  the background cools as 1/a: not constant in time.  Equal-temperature surfaces are equal cosmic time:")
    print("  one second of cosmic time moves T by %.1e of itself; T0 is known to %.1e -- %.1f orders short" % (
        un["dT_over_T_per_second"], un["fixsen_relative_precision"], un["slicing_gap_orders"]))
    print("  to synchronise the ends by temperature would need dT/T ~ %.1e (to resolve the lead) or %.1e (the "
          "dipole term); the dipole with light signals does it to %.0f s" % (
              un["dT_over_T_to_resolve_lead"], un["dT_over_T_to_resolve_dipole_sigma"], ld["sigma_dipole_s"]))
    print("  absolute calibration (shared by both ends): %.2e yr" % un["clock_absolute_sigma_yr"])
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
    ph, g, ld, of, lp, lf, mf, un = (d[k] for k in ("physics", "geometry", "lead", "one_frame", "loops",
                                                     "lab_frame", "matter_frames", "universal"))
    chk("H-GAL-MATRIX: Planck's (l, b) -> RA/Dec matches Planck's printed RA/Dec within 0.01 deg (%.4f deg)"
        % g["gal_matrix_vs_printed_deg"], g["gal_matrix_vs_printed_deg"] < 0.01)
    chk("the untransposed matrix misses Planck's printed RA/Dec by more than 1 deg (%.1f deg)" %
        g["untransposed_vs_printed_deg"], g["untransposed_vs_printed_deg"] > 1.0, ctl=True)
    chk("the physics: dipole amplitude / T0 (Planck, Fixsen) = %.6e equals Planck's printed beta within the errors"
        % ph["beta_from_amp_over_T0"],
        abs(ph["beta_from_amp_over_T0"] - DIPOLE["beta"][0]) < math.hypot(ph["sigma"], DIPOLE["beta"][1]))
    chk("Local Group: v_Sun-CMB - v_LG-CMB reproduces Planck Table 3's Sun-LG row within its errors (%.1f km/s at "
        "(%.1f, %.1f))" % ((mf["Local Group"]["v_rel_kms"],) + mf["Local Group"]["rel_l_b_deg"]),
        abs(mf["Local Group"]["v_rel_kms"] - SUN_LG_TABLE3["v_kms"][0]) < SUN_LG_TABLE3["v_kms"][1]
        and abs(mf["Local Group"]["rel_l_b_deg"][0] - SUN_LG_TABLE3["l_deg"][0]) < SUN_LG_TABLE3["l_deg"][1]
        and abs(mf["Local Group"]["rel_l_b_deg"][1] - SUN_LG_TABLE3["b_deg"][0]) < SUN_LG_TABLE3["b_deg"][1])
    chk("the first build's LG velocity (v_LG-CMB alone) does NOT reproduce Table 3's Sun-LG row",
        abs(FRAMES_OF_MATTER["Local Group"]["v_kms"][0] - SUN_LG_TABLE3["v_kms"][0]) > SUN_LG_TABLE3["v_kms"][1],
        ctl=True)
    chk("sign: the lead agrees in sign with frame.py's along-dipole figure (both negative toward the apex), and a "
        "link toward the anti-apex shows a positive lead",
        ld["lead_s"] < 0 and ld["owner_scaled_s"] < 0 and lead_from_velocity(V_SUN_CMB, scale(N_PROXIMA, -1.0)) > 0)
    chk("regression pins (verifier recomputed independently): angle 66.194 deg, lead -66,725 s (%.4f deg, %.1f s)" % (
        g["theta_deg"], ld["lead_s"]), abs(g["theta_deg"] - 66.19427) < 2e-3 and abs(ld["lead_s"] + 66725) < 2)
    chk("seat.D_PROXIMA (%.5f ly) agrees with 1/plx from the VizieR DR3 row (%.5f ly) to 1e-6" % (
        g["L_ly"], g["L_from_vizier_plx_ly"]), abs(g["L_ly"] / g["L_from_vizier_plx_ly"] - 1) < 1e-6)
    chk("Earth-frame annual modulation +- %.0f s (pinned 14.17 %% of the lead) within its bound %.0f s; barycentre-"
        "time offset under 1 s (%.2f s)" % (ld["annual_mod_earth_frame_s"], ld["annual_mod_bound_s"],
                                           ld["barycentre_time_offset_bound_s"]),
        abs(ld["annual_mod_earth_frame_s"] / abs(ld["lead_s"]) - 0.1417) < 0.002
        and ld["annual_mod_earth_frame_s"] <= ld["annual_mod_bound_s"] and ld["barycentre_time_offset_bound_s"] < 1)
    chk("dipole-precision term %.1f s (pinned 26.6 s: the verifier's 26.6-27.2 s)" % ld["sigma_dipole_s"],
        abs(ld["sigma_dipole_s"] - 26.6) < 0.7)
    chk("frame.py's z3 lemma proved (unsat), its vacuity guard sat and its control (a >= 0) sat",
        lp["frw_lemma"]["claim"] == "unsat" and lp["frw_lemma"]["vacuity"] == "sat"
        and lp["frw_lemma"]["control_a_ge_0"] == "sat")
    chk("nonlocal.py's witness pair (different frames, timelike span) DOES close a loop",
        lp["nonlocal_frame_requirement"]["witness_loop"] is True, ctl=True)
    chk("H-LAB-FRAME holds for every nonlocal.py test at Earth's upper-bound CMB speed (beta %.3e)" % lf["beta_max"],
        all(v["holds"] for v in lf["tests"].values()))
    hi = lab_frame(0.99 * C_KMS)
    chk("lab_frame() run at beta = 0.99: H-LAB-FRAME fails for every test",
        all(not v["holds"] for v in hi["tests"].values()), ctl=True)
    chk("J bounds weakened by at most 0.2 %% in the CMB frame (max factor %.5f)" % max(
        v["J_factor"] for v in lf["tests"].values()), max(v["J_factor"] for v in lf["tests"].values()) < 1.002)
    q = mf["quasar dipole read kinematically (WISE 2022)"]
    chk("reading (b): the quasar-frame shift crosses zero over the +-1 sigma box (%.2f to %.2f h), max |shift| 13.3 h"
        % q["signed_shift_range_h"], q["crosses_zero"]
        and abs(max(abs(x) for x in q["signed_shift_range_h"]) - 13.27) < 0.05)
    chk("Local Group keying: lead in the barycentre's coordinate FUTURE (%+.1f h), shift %+.1f h (verifier: +29.9 h, "
        "48.4 h)" % (mf["Local Group"]["lead_s"] / 3600, mf["Local Group"]["shift_h"]),
        mf["Local Group"]["lead_s"] > 0 and abs(abs(mf["Local Group"]["shift_h"]) - 48.4) < 0.2)
    chk("every READ T(z) beta is within 1 sigma of 0, and T0(1+z) at HFLS3 lies in its READ 1-sigma range",
        all(v["n_sigma"] < 1 for v in un["T_of_z"].values()) and un["HFLS3_in_1sigma"])
    chk("a constant background (T(z) = T0) would read 2.725 K at HFLS3, outside the READ range",
        not (T_HFLS3["T_1sigma_K"][0] <= T0[0] <= T_HFLS3["T_1sigma_K"][1]), ctl=True)
    chk("temperature cannot synchronise the ends: the precision needed (%.1e) is >= 9 orders finer than T0's (%.1e)"
        % (un["dT_over_T_to_resolve_lead"], un["fixsen_relative_precision"]),
        un["fixsen_relative_precision"] / un["dT_over_T_to_resolve_lead"] > 1e9)
    chk("Hubble-flow dbeta across L below 1e-9 (%.2e)" % of["dbeta_hubble"], of["dbeta_hubble"] < 1e-9)
    structural.append("keyed lattices rank 2 (%d/%d) and rank 3 (%d/%d) with a positive-definite Gram: a theorem by "
                      "Sylvester for ANY single frame, not evidence for the CMB's" % (
                          lp["rank2"][0] - lp["rank2"][1], lp["rank2"][0], lp["rank3"][0] - lp["rank3"][1],
                          lp["rank3"][0]))
    structural.append("frame.py's along-dipole figure scaled (%.2f s) = this lead x gamma (%.2f s): frame.py keeps "
                      "gamma for a CMB-frame displacement; the difference is O(beta^2)" % (
                          ld["owner_scaled_s"], ld["lead_s"] / math.sqrt(1 - (DIPOLE["v_kms"][0] / C_KMS) ** 2)))
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
