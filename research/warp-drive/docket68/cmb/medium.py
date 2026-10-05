#!/usr/bin/env python3
"""
medium.py -- H-CMB-CORRIDOR, reading 2: the cosmic background as the corridor's MEDIUM or CARRIER.

Seated in ledger.py section 8g (M-RULINGS item 54; first written "Not seated").  Verified once in both directions (2026-10-05); the findings are applied and the first-written claims kept
under HISTORY.  M (rulings item 45): "Seat it, then medium".  M (item 47, on H-CONTRACT, item 46): "2, then 1" -- the
status of a contracting universe READ first, then folded in (section (H)).  M's hypotheses H-CMB-CORRIDOR,
H-CMB-UNIVERSAL (item 41) and H-CONTRACT (item 46) are carried, never results.  H-UNOBSERVED-MEDIUM (item 48) and
H-TWO-OBSERVERS (item 49) are carried and taken up in their own reading (M item 49: READ, then a model).

    python3 medium.py              report
    python3 medium.py --selftest   checks, with CONTROLS
    python3 medium.py --json       the numbers as JSON

WHAT "MEDIUM" IS TAKEN TO MEAN (five readings, each priced; none dismissed; each says what would change it)
  (A) the photon gas itself: number, energy and entropy densities from T0 (READ);
  (B) a MEDIUM in the acoustic sense: needs the photons to interact -- the photon-photon mean free path against the
      Hubble length; before decoupling it WAS such a medium (the photon-baryon fluid), READ;
  (C) a passive CARRIER: background photons already heading from A toward B -- the photon budget (etendue) and the
      contrast available;
  (D) the background as NOISE (where it dominates; the board's floor quantum) and as the coldest HEAT SINK (Landauer
      at T0 against the board's channel floor; a sky-facing radiator sized);
  (E) a SHARED RESOURCE: the field's spatial coherence across the span, and the common sky (shared classical
      randomness, which carries no message -- nosig.py).

NAMED HYPOTHESES
  H-CMB-BLACKBODY     the background is a blackbody at T0 (Fixsen's combined value).
  H-OMEGA-CM          King & Heinzl's omega is each photon's energy in the pair's centre-of-mass frame (the source's
                      threshold 'omega = m'): for lab energies E1, E2 at angle theta, omega^2 = E1 E2 (1 - cos)/2.  The
                      MEAN scattering rate per photon is c n sigma0 (kT/m)^6 <(1-mu)((1-mu)/2)^3> <x^3>^2 (isotropic
                      angles; x over the photon-number spectrum) -- computed exactly; <x^6> >= <x^3>^2 (Jensen) and
                      0.4 <= 1 make the first build's figure an upper bound on that mean.  A single tail photon scatters
                      faster than the mean (rate ~ x^3); its figure is printed beside.
  H-ALPHA             alpha = 7.2973525643e-3 as settle.py types it (CODATA 2022 value, MEMORY-level here); pinned by
                      the standard sigma(omega = 1 eV) = 7.27e-66 cm^2 (selftest).
  H-ISOTROPIC-FLUX    the background's intensity is isotropic (dipole only in the contrast, (C)).
  H-APERTURES         equal apertures at A and B, 1 m^2 and 1 km^2 priced.
  H-PASSIVE           a lossless redirector, or an absorber in equilibrium at T0 (Kirchhoff): contrast bounded by the
                      background's own anisotropy (the dipole, apex against anti-apex, bolometric).  A shutter COLDER
                      than T0 reaches contrast up to 1, at a refrigeration cost.  Either way the photon budget is capped
                      by conservation of radiance (etendue): (n c / 4 pi) A_A A_B / L^2.
  H-SCALAR-COHERENCE  the TRACE of the blackbody coherence tensor (sin kr / kr per frequency, Henkel et al.
                      physics/0008028v1 p.4, p.6) averaged over the Planck energy spectrum (energy weighting is right for
                      the equal-time field correlation): exactly 15/(pi^4 rho^4) - (15/(pi rho)) csch^2(pi rho)
                      coth(pi rho).  The LONGITUDINAL component falls only as 45/(2 pi^3 rho^3) (the transverse-delta
                      1/r^3 tail; Mohanty cond-mat/0005233v1 eq. 8 gives its per-frequency form): printed beside.
  H-LSS-DISTANCE      the last-scattering surface lies beyond the Hubble radius c/H0 (bounds the parallax).
  H-MODES             the shared sky's independent modes counted as Planck's TT multipoles 2..2508 (all m; no f_sky,
                      no noise cut).
  -- section (H), H-CONTRACT (M item 46; READ first, item 47) --
  H-CONTRACT          M's: the universe contracts as well as expands.  Carried; not shown, not excluded.
  H-EFFECTIVE-METRIC  a nonsingular bounce described by an effective FRW metric with a > 0 throughout, so frame.py's z3
                      lemma applies to it.
  H-RADIATION-AT-BOUNCE the bounce temperature priced with radiation (photons alone) holding LQC's maximum density -- the
                      source's own radiation model (Ashtekar & Singh 1108.0893v2 sec. VII.D, pp.113-114); an upper figure
                      for the photon temperature (photons hold only part of the radiation there).
  H-T-SCALES          T ~ 1/a in both phases (constant radiation entropy, T^3 a^3 = const: Novello & Perez Bergliaffa
                      0802.1634v1 p.86).  Across e+e- and earlier annihilations T a is not constant (g*s changes, about
                      106.75/3.91), so a_bounce/a_now is about 3 times the photon-only figure.  Each temperature below the
                      bounce's occurs twice per cycle.
  H-IONISED-IGM       (OPEN reading) baryons stay diffuse and ionised on contraction, so the gas couples (Thomson depth
                      per Hubble time 1) far below 2973 K -- the verifier's estimate a ~ 0.02-0.025, T ~ 110-140 K,
                      c_s ~ 0.15 c, NOT computed here; Luu, Qiu & Tye (p.12) expect collapse into black holes instead.

HISTORY (verifier, 2026-10-05; first-written claims kept):
  * collisionless(): 'omega taken as the lab energy (the CM energy is never larger)' -- FALSE photon by photon (a head-on
    pair's CM energy per photon reaches sqrt(E1 E2), above the softer photon's lab energy) and the flux factor (1 - cos)
    was dropped.  The figure survives only as an upper bound on the MEAN rate (Jensen, and 0.4 <= 1); the exact mean is
    now computed (10^53.1 Hubble lengths against the first-printed 10^51.9).
  * 'it is the noise only near its own peak, where the occupation is 0.063' -- WRONG: the occupation grows toward low
    frequency (about 1/x), exceeds 1 below x = ln 2 (about 39 GHz) and is 56 at 1 GHz.
  * 'tensor components differ ... but not in their power-law fall-off' -- WRONG: the longitudinal component falls as
    rho^-3 (6.6e-60 at L), not rho^-4 (the trace's 3e-80).  Both negligible; 'no correlation' is now 'negligible'.
  * 'Any contraction lies at least about 4 Gyr away' -- OVERSTATED: 0.27/H0 is AIS's minimum at m_Pl/m = 10 only;
    steeper potentials give sooner times (their Fig. 4, values figure-only, OPEN).
  * 'the medium returns ... a phase of the cycle, the hot one' -- held only for compression (LQC's symmetric bounce,
    LQT's recollapse); Ijjas-Steinhardt's slow contraction (alpha = 2 (m/m_Pl)^2 = 0.02, AIS p.5) shrinks a by about 17
    even as H rises by 1e61, so the old background reaches tens of K -- the hot phase there comes from reheating at the
    bounce.  Split by model; the hot coupled phase recurs in every model read.
  * 'LQC: radiation passes through (the reader's INFERENCE, not printed)' -- UNDERSOLD: Ashtekar & Singh print it
    (sec. VII.D pp.113-114: rho ~ a^-4 through the bounce; the photon temperature maximal at the bounce, finite).
  * H-PASSIVE: the dipole bound holds for a lossless redirector or an absorber at T0; a colder shutter reaches contrast 1.
  * shared_sky: the dominant difference between the two skies is kinematic (Proxima's ~32 km/s: aberration ~1.1e-4 rad,
    about 9 % of the ell = 2508 scale), not parallax -- reading 1's frame corrects it.
  * Vacuous checks: an '8 times the photons at 2 T0' control (true by construction), a 'coherence at zero is 1' control
    that never called coherence(), a T_max < T_Pl check (a tautology: the ratio is (15 x 0.41 / pi^2)^(1/4) = 0.888 for
    any constants), and an asymptote check passing through a float round trip.  Replaced by pins and real controls.
    'Handling' the bits at T0 now reads 'erasing' (Landauer prices irreversible erasure only, nopath's caution).
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
    if key in sys.modules:
        return sys.modules[key]
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


with contextlib.redirect_stdout(io.StringIO()):
    cmbframe = _by_path("cmb_cmbframe", os.path.join(HERE, "cmbframe.py"))
    demand = _by_path("s1c_demand", os.path.join(WD, "step1c", "demand.py"))
    import nopath

seat = cmbframe.seat
cosmo = cmbframe.cosmo
C = seat.C
HBAR = seat.HBAR
H_PL = seat.H
KB = nopath.KB
L = cmbframe.L
H0 = cmbframe.H0
YEAR_S = seat.YEAR_S
EV = 1.602176634e-19
T0 = cmbframe.T0[0]                 # Fixsen 2009, READ (via cmbframe)
ALPHA = 7.2973525643e-3             # H-ALPHA
ME_C2_EV = 0.51099895069e6          # CODATA 2022, READ (arXiv:2409.03787v1 Table XXXIII; Q1s-signed.md)
SIGMA_SB = math.pi ** 2 * KB ** 4 / (60 * HBAR ** 3 * C ** 2)      # Stefan-Boltzmann, from the constants

# ---------------------------------------------------------------------------------------------------------------------
# READ at source (2026-10-05; alphaXiv answer_pdf_queries; the verifier re-read King & Heinzl, Hu & Dodelson,
# Ashtekar & Singh, AIS, LQT, Dovekie and Ong et al.)
# ---------------------------------------------------------------------------------------------------------------------
GAMMA_GAMMA = {"coef": 973.0 / (10125.0 * math.pi), "power": 6,
               "form": "sigma = (973/(10125 pi)) alpha^4 (omega/m)^6 lambdabar_e^2, omega << m",
               "source": "King & Heinzl, arXiv:1510.08456v1 p.3 (after eq. 9), citing Berestetskii-Lifshitz-"
                         "Pitaevskii (NAMED-NOT-READ); lambdabar_e = hbar/(m c) (p.2)"}
ACOUSTIC = {"form": "c_s^2 = (1/3) / (1 + R), R = 3 rho_b / (4 rho_gamma)",
            "source": "Hu & Sugiyama, astro-ph/9407093v1 p.5 eq. (6), p.4 eq. (3)",
            "R_star": (0.60, 0.06), "R_star_source": "Hu & Dodelson, astro-ph/0110414v1 p.26 (observed, citing Knox "
                                                     "et al. 2001)"}
Z_STAR = (1089.92, 0.25)            # Planck 2018 VI, arXiv:1807.06209v4 Table 2 p.16 (TT,TE,EE+lowE+lensing)
ELL_MAX_TT = 2508                   # Planck 2018 V, arXiv:1907.12875v2 Table 23 p.88 (Plik TT 30-2508; 2-29 low-ell)
APERTURES_M2 = (1.0, 1.0e6)         # H-APERTURES


def _zeta(s, n=200000):
    return sum(k ** -s for k in range(1, n)) + n ** (1 - s) / (s - 1)


def _simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b) + sum((4 if i % 2 else 2) * f(a + i * h) for i in range(1, n))
    return s * h / 3


def _occ(x):
    return 1.0 / math.expm1(x)


# ---------------------------------------------------------------------------------------------------------------------
# (A) the photon gas
# ---------------------------------------------------------------------------------------------------------------------
def gas(T=T0, polarisations=2):
    """Densities from the Planck distribution, integrated numerically; the closed forms are the check."""
    lam = HBAR * C / (KB * T)
    In = _simpson(lambda x: x * x / math.expm1(x) if x > 0 else 0.0, 0.0, 60.0)
    Iu = _simpson(lambda x: x ** 3 / math.expm1(x) if x > 0 else 0.0, 0.0, 60.0)
    pref = polarisations / (2 * math.pi ** 2)
    n = pref * In / lam ** 3
    u = pref * Iu * KB * T / lam ** 3
    s = 4.0 / 3.0 * u / T
    return {"T_K": T, "thermal_length_m": lam, "n_per_m3": n, "n_per_cm3": n * 1e-6, "u_J_m3": u,
            "s_J_K_m3": s, "s_bits_m3": s / (KB * math.log(2)), "mean_E_eV": u / n / EV,
            "closed_n_per_m3": 2 * _zeta(3) / math.pi ** 2 / lam ** 3,
            "closed_u_J_m3": math.pi ** 2 / 15 * KB * T / lam ** 3,
            "bits_per_photon": (s / (KB * math.log(2))) / n, "tube_bits_1m2": s / (KB * math.log(2)) * 1.0 * L,
            "number_intensity": n * C / (4 * math.pi)}


# ---------------------------------------------------------------------------------------------------------------------
# (B) a medium in the acoustic sense
# ---------------------------------------------------------------------------------------------------------------------
def sigma_gg(omega_eV):
    """King & Heinzl's low-energy cross-section (m^2) at CM photon energy omega."""
    lbar = HBAR / (ME_C2_EV * EV / C)
    return GAMMA_GAMMA["coef"] * ALPHA ** 4 * (omega_eV / ME_C2_EV) ** 6 * lbar ** 2


def collisionless(T=T0):
    """H-OMEGA-CM.  Mean rate per photon: c n sigma0 (kT/m)^6 x <(1-mu)^4/8> x <x^3>^2, with <(1-mu)^4/8> = 2/5 over
    isotropic angles and <x^3> = Gamma(6) zeta(6) / (Gamma(3) zeta(3)) over the photon-number spectrum.  The first
    build's <x^6> = Gamma(9) zeta(9)/(Gamma(3) zeta(3)) without the angular factor is an upper bound on it (Jensen).  A
    tail photon at x: rate ~ x^3 <x^3> x 2/5."""
    g = gas(T)
    s0 = sigma_gg(KB * T / EV)                                  # sigma at omega = kT
    ang = 0.4
    x3 = math.factorial(5) * _zeta(6) / (math.factorial(2) * _zeta(3))
    x6 = math.factorial(8) * _zeta(9) / (math.factorial(2) * _zeta(3))
    rate_mean = C * g["n_per_m3"] * s0 * ang * x3 * x3
    rate_bound = C * g["n_per_m3"] * s0 * x6
    rate_tail30 = C * g["n_per_m3"] * s0 * ang * 30.0 ** 3 * x3
    hubble = C / H0
    o = lambda r: math.log10((C / r) / hubble)
    return {"x3_mean": x3, "x6_mean": x6, "angular": ang, "mfp_mean_m": C / rate_mean,
            "orders_mean": o(rate_mean), "orders_bound": o(rate_bound), "orders_tail_x30": o(rate_tail30),
            "hubble_m": hubble, "sigma_1eV_cm2": sigma_gg(1.0) * 1e4}


def acoustic_past():
    R, sR = ACOUSTIC["R_star"]
    cs = 1.0 / math.sqrt(3.0 * (1.0 + R))
    return {"cs_over_c_at_R_star": cs, "cs_range": (1.0 / math.sqrt(3.0 * (1.0 + R + sR)),
                                                    1.0 / math.sqrt(3.0 * (1.0 + R - sR))),
            "cs_over_c_no_baryons": 1.0 / math.sqrt(3.0), "T_decoupling_K": T0 * (1.0 + Z_STAR[0]),
            "a_decoupling": 1.0 / (1.0 + Z_STAR[0])}


# ---------------------------------------------------------------------------------------------------------------------
# (C) a passive carrier
# ---------------------------------------------------------------------------------------------------------------------
def carrier():
    """Etendue: no passive redirector can send more background photons from A into B than (n c / 4 pi) A_A A_B / L^2.
    Set against the board's demand (step1c/demand.py, species count, 1 yr)."""
    g = gas()
    T1 = demand.SCHEDULES_S[1]
    name, bits = demand.counts()[0]
    rate = bits / T1
    beta = cmbframe.DIPOLE["beta"][0]
    rows = []
    for A in APERTURES_M2:
        nd = g["number_intensity"] * A * A / (L * L)
        rows.append({"aperture_m2": A, "photons_per_s": nd, "bits_per_photon_needed": rate / nd,
                     "photons_in_a_year": nd * T1})
    return {"count": name, "bits": bits, "rate_bits_s": rate, "rows": rows,
            "contrast_dipole": ((1 + beta) / (1 - beta)) ** 4 - 1, "contrast_cold_shutter_max": 1.0}


# ---------------------------------------------------------------------------------------------------------------------
# (D) noise and heat sink
# ---------------------------------------------------------------------------------------------------------------------
def noise_and_sink():
    T1 = demand.SCHEDULES_S[1]
    ch = demand.channel(T1)
    name = demand.counts()[0][0]
    E_q = ch[name]["quantum_eV"] * EV
    x = E_q / (KB * T0)
    bits = demand.counts()[0][1]
    land = nopath.landauer_energy(bits, T0)
    floor = ch[name]["floor_J_one_pol"]
    # a sky-facing radiator at 2 T0 dumping the erasure heat of the count over a year (net emission 15 sigma T0^4)
    p_erase_2T0 = nopath.landauer_energy(bits, 2 * T0) / T1
    net = SIGMA_SB * ((2 * T0) ** 4 - T0 ** 4)
    return {"quantum_eV": ch[name]["quantum_eV"], "x_over_kT": x, "log10_occupation": -x / math.log(10),
            "occupation_at_peak": _occ(2.821439), "nu_occupation_1_GHz": math.log(2) * KB * T0 / H_PL / 1e9,
            "occupation_at_1GHz": _occ(H_PL * 1e9 / (KB * T0)), "landauer_J": land, "channel_floor_J": floor,
            "floor_over_landauer": floor / land, "landauer_per_bit_J": KB * T0 * math.log(2),
            "sigma_T0_4": SIGMA_SB * T0 ** 4, "erase_power_2T0_W": p_erase_2T0, "radiator_m2": p_erase_2T0 / net}


# ---------------------------------------------------------------------------------------------------------------------
# (E) a shared resource
# ---------------------------------------------------------------------------------------------------------------------
def coherence_rho(rho):
    """The trace's exact closed form (H-SCALAR-COHERENCE); 1 at rho = 0."""
    if rho == 0:
        return 1.0
    if rho > 50:
        return 15.0 / (math.pi ** 4 * rho ** 4)
    pr = math.pi * rho
    return 15.0 / (math.pi ** 4 * rho ** 4) - (15.0 / pr) * math.cosh(pr) / math.sinh(pr) ** 3


def coherence(r_m, T=T0):
    rho = r_m * KB * T / (HBAR * C)
    return {"rho": rho, "trace": coherence_rho(rho), "longitudinal_asymptote": 45.0 / (2 * math.pi ** 3 * rho ** 3)
            if rho > 0 else 1.0}


def shared_sky():
    """Parallax below L / (c/H0) (H-LSS-DISTANCE); the dominant difference is the aberration from Proxima's velocity
    relative to the Sun (Gaia DR3's proper motion and radial velocity, via cmbframe) -- reading 1's frame corrects it."""
    p = cmbframe.PROXIMA_DIR
    mu_as = math.hypot(*p["pm_mas_yr"]) / 1000.0
    d_pc = 1000.0 / p["plx_mas"][0]
    vt = 4.740470446 * mu_as * d_pc                             # km/s (AU per yr over km/s, exact definition)
    v = math.hypot(vt, p["rv_kms"][0])
    return {"parallax_bound_rad": L * H0 / C, "modes": (ELL_MAX_TT + 1) ** 2 - 4, "v_proxima_sun_kms": v,
            "aberration_rad": v / (C / 1000.0), "ell_scale_rad": math.pi / ELL_MAX_TT}


# ---------------------------------------------------------------------------------------------------------------------
# (H) H-CONTRACT
# ---------------------------------------------------------------------------------------------------------------------
CONTRACT_READ = {
    "accelerating now": "Riess et al. 1998 (astro-ph/9805201v1): q0 < 0 at 2.8-3.9 sigma, q0 = -1.0 +- 0.4 (p.16); "
                        "DESI DR1 (2404.03002v3, printed p.32): acceleration required at z < 0.7 in LCDM, wCDM, w0waCDM",
    "evolving dark energy": "DESI DR2 (2503.14738v3 Table VI p.24): w0 > -1, wa < 0 preferred at 2.8-4.2 sigma "
                            "(frequentist); DES-Dovekie recalibration (2511.07517v3 p.1): 3.2 sigma, 'only a weak "
                            "preference' (Bayesian); Ong, Yallup & Handley (2511.10631v3 Table I p.2): log Bayes factor "
                            "-0.30 +- 0.19 with Dovekie (no evidence)",
    "recollapse fits": "only in models with a negative vacuum or potential: Luu, Qiu & Tye (2506.24011v2, on the "
                       "pre-recalibration DES data, p.3): best fit a_max ~ 1.69, turnaround ~11 Gyr from now, lifespan "
                       "33.3 Gyr (eq. 4.8 p.8), ending in a -> 0 (pp.1, 7) -- the best fit lies outside 1 sigma of the "
                       "mean and Omega_Lambda = 0 is consistent (p.10); Andrei, Ijjas & Steinhardt (2201.07704v2 p.8): "
                       "end of expansion no sooner than 0.27/H0 at the 2 sigma fit for m_Pl/m = 10, sooner for steeper "
                       "potentials (Fig. 4); Gialamas et al. (2506.21542v2 p.9): negative vacuum preferred at 93.8 % "
                       "(pre-recalibration DESY5)",
    "bounce, nonsingular": "LQC: V_min = 2 sqrt(V+ V-)/||chi||^2 > 0 for every state (Ashtekar & Singh 1108.0893v2 eq. "
                           "3.23 p.39), rho_max ~ 0.41 rho_Pl (p.32, eq. 5.7 p.73); time relational (p.33).  Ijjas & "
                           "Steinhardt: the scale factor 'shrinks to a finite critical size' (1803.01961v1 printed p.7)",
    "bounce, singular": "Steinhardt & Turok (hep-th/0111098v2): in the 4d Einstein frame the scale factor 'collapses to "
                        "zero at the big crunch' (p.7), curvature diverges (p.18); the resolution is postulated in five "
                        "dimensions (p.3).  LQT's crunch is a -> 0 too",
    "radiation through the bounce": "LQC: printed -- a radiation-filled k = 0 model keeps rho ~ a^-4 through the bounce "
                                    "and the photon temperature is maximal there and finite (Ashtekar & Singh sec. "
                                    "VII.D, pp.113-114, eqs. 7.16-7.19; verifier-READ).  Ijjas & Steinhardt (1904.08022v1 "
                                    "pp.3-4): created at each bounce, the old diluted, 'the entropy observed within the "
                                    "Hubble radius is the same from cycle to cycle' (p.4); slow contraction a ~ |1/H|^alpha"
                                    ", alpha = 2 (m/m_Pl)^2 (AIS 2201.07704v2 p.5, verifier-READ); reheating above the "
                                    "electroweak scale at the bounce (AIS p.9, verifier-READ).  Steinhardt & Turok (pp.12,"
                                    " 20): generated at the bounce, the prior diluted",
}
A_MAX_LQT = 1.69                    # Luu, Qiu & Tye 2506.24011v2 p.8 (best fit only)
AIS_END_OVER_H0 = 0.27              # Andrei, Ijjas & Steinhardt 2201.07704v2 p.8 (minimum, m_Pl/m = 10)
AIS_M_OVER_MPL = 0.1                # the same case (m_Pl/m = 10)
LQC_RHO_MAX_OVER_PL = 0.41          # Ashtekar & Singh 1108.0893v2 p.32, eq. 5.7 p.73; rho_Pl = 1/(G^2 hbar), c = 1


def contraction():
    """(H1) loop-freedom through a bounce (frame.py's z3 lemma, asked: a > 0 only; its vacuity and drift guards
    asserted in the selftest).  (H2) the temperature label and LQC's ceiling (H-RADIATION-AT-BOUNCE).  (H3) the hot
    coupled phase, by model: compression (LQC, LQT) reaches T0 (1 + z*); Ijjas-Steinhardt's slow contraction does not
    (a shrinks by (H_bounce/H0)^alpha), and the hot phase there is reheating.  (H4) the corridor's schedules."""
    with contextlib.redirect_stdout(io.StringIO()):
        lem = cmbframe.frame.frw_time_function_lemma()
    G = cosmo._G
    u_pl = C ** 7 / (HBAR * G * G)
    u_max = LQC_RHO_MAX_OVER_PL * u_pl
    T_max = (15.0 * u_max * (HBAR * C) ** 3 / math.pi ** 2) ** 0.25 / KB
    T_pl = math.sqrt(HBAR * C ** 5 / G) / KB
    ap = acoustic_past()
    t_h = cosmo.hubble_time_gyr()
    alpha = 2 * AIS_M_OVER_MPL ** 2
    H_pl = 1.0 / math.sqrt(HBAR * G / C ** 5)                   # Planck rate, 1/s
    shrink_slow = (H_pl / H0) ** alpha
    return {"lemma": lem, "T_bounce_max_K": T_max, "T_planck_K": T_pl, "T_max_over_T_pl": T_max / T_pl,
            "a_bounce_over_now_photon": T0 / T_max, "a_bounce_over_now_gstar": 3.0 * T0 / T_max,
            "T_at_turnaround_K_LQT": T0 / A_MAX_LQT, "a_recouple": ap["a_decoupling"], "T_recouple_K": ap["T_decoupling_K"],
            "contraction_factor_LQT_to_recouple": A_MAX_LQT / ap["a_decoupling"],
            "slow_alpha": alpha, "slow_shrink_to_planck_rate": shrink_slow, "slow_T_reached_K": T0 * shrink_slow,
            "AIS_end_of_expansion_Gyr_mPl_m_10": AIS_END_OVER_H0 * t_h, "hubble_time_Gyr": t_h,
            "dT_over_T_per_century_now": H0 * 100 * YEAR_S}


def collect():
    return {"gas": gas(), "collisionless": collisionless(), "acoustic_past": acoustic_past(), "carrier": carrier(),
            "noise_and_sink": noise_and_sink(),
            "coherence": {k: coherence(r) for k, r in (("1 mm", 1e-3), ("1 cm", 1e-2), ("1 m", 1.0), ("L", L))},
            "shared_sky": shared_sky(), "contraction": contraction()}


def report():
    d = collect()
    g, cl, ap, ca, ns, co, sk, ct = (d[k] for k in ("gas", "collisionless", "acoustic_past", "carrier",
                                                     "noise_and_sink", "coherence", "shared_sky", "contraction"))
    print("H-CMB-CORRIDOR, reading 2: the cosmic background as MEDIUM or CARRIER (verified once; seated, ledger.py 8g)\n")
    print("(A) THE PHOTON GAS at T0 = %.5f K (Fixsen, READ)" % T0)
    print("  %.1f photons/cm^3; %.3e J/m^3; entropy %.3e bits/m^3 (%.2f bits per photon); mean photon %.3f meV; "
          "thermal length %.3f mm" % (g["n_per_cm3"], g["u_J_m3"], g["s_bits_m3"], g["bits_per_photon"],
                                      g["mean_E_eV"] * 1e3, g["thermal_length_m"] * 1e3))
    print("  a 1 m^2 tube from Earth to Proxima holds %.2e bits of background entropy" % g["tube_bits_1m2"])
    print("\n(B) A MEDIUM IN THE ACOUSTIC SENSE")
    print("  photon-photon mean free path (mean over the spectrum, exact): %.1e m, 10^%.1f Hubble lengths (bound first "
          "printed: 10^%.1f); a tail photon at x = 30: 10^%.1f -- collisionless, no collective mode today" % (
              cl["mfp_mean_m"], cl["orders_mean"], cl["orders_bound"], cl["orders_tail_x30"]))
    print("  before decoupling it WAS a medium: the photon-baryon fluid, c_s = %.3f c at R* = 0.60 (%.3f-%.3f c); "
          "decoupling at T0(1+z*) = %.0f K" % (ap["cs_over_c_at_R_star"], ap["cs_range"][0], ap["cs_range"][1],
                                              ap["T_decoupling_K"]))
    print("\n(C) A PASSIVE CARRIER (%s, %.2e bits; %.2e bits/s at 1 yr)" % (ca["count"], ca["bits"], ca["rate_bits_s"]))
    for r in ca["rows"]:
        print("  apertures %.0e m^2 each: at most %.2e background photons/s from A into B (etendue) -- %.1e bits per "
              "photon needed" % (r["aperture_m2"], r["photons_per_s"], r["bits_per_photon_needed"]))
    print("  contrast: %.2e from the dipole for a lossless redirector or an absorber at T0; up to 1 for a shutter colder "
          "than T0 (refrigerated)" % ca["contrast_dipole"])
    print("\n(D) NOISE AND HEAT SINK")
    print("  the background is the dominant noise at and below its peak (occupation %.3f there), above 1 below %.1f GHz "
          "(%.0f at 1 GHz); at the board's floor quantum (%.0f keV) it is 10^%.3g" % (
              ns["occupation_at_peak"], ns["nu_occupation_1_GHz"], ns["occupation_at_1GHz"], ns["quantum_eV"] / 1e3,
              ns["log10_occupation"]))
    print("  Landauer at T0: erasing a bit costs %.2e J, the species count %.2e J -- the board's 1-yr channel floor "
          "(%.2e J) is %.1e times that" % (ns["landauer_per_bit_J"], ns["landauer_J"], ns["channel_floor_J"],
                                            ns["floor_over_landauer"]))
    print("  the sink in practice: sigma T0^4 = %.2e W/m^2; erasing the count at 2 T0 over a year (%.3f W) needs a "
          "sky-facing radiator of %.0f m^2" % (ns["sigma_T0_4"], ns["erase_power_2T0_W"], ns["radiator_m2"]))
    print("\n(E) A SHARED RESOURCE")
    for k, v in co.items():
        print("  coherence over %-4s (rho = %.2e): trace %.2e; longitudinal component %.2e" % (
            k, v["rho"], v["trace"], v["longitudinal_asymptote"] if v["rho"] > 50 else float("nan")))
    print("  the two skies: parallax below %.1e rad; aberration from Proxima's %.1f km/s, %.2e rad (%.0f %% of the ell = "
          "%d scale) -- reading 1's frame corrects it; %d independent modes: shared classical randomness, which carries "
          "no message" % (sk["parallax_bound_rad"], sk["v_proxima_sun_kms"], sk["aberration_rad"],
                          100 * sk["aberration_rad"] / sk["ell_scale_rad"], ELL_MAX_TT, sk["modes"]))
    print("\n(H) H-CONTRACT (M item 46; status READ first, item 47)")
    for k, v in CONTRACT_READ.items():
        print("  READ, %s: %s" % (k, v[:150] + ("..." if len(v) > 150 else "")))
    print("  loop-freedom: frame.py's z3 lemma needs a > 0 only (claim %s, control a >= 0 %s) -- a nonsingular bounce "
          "keeps the keyed network loop-free; a crunch to a = 0 (4d ekpyrotic, LQT's end) breaks the premise" % (
              ct["lemma"]["claim"], ct["lemma"]["control_a_ge_0"]))
    print("  temperature label: T ~ 1/a both ways, each T below the bounce's occurs twice per cycle; LQC's bounce caps "
          "the photon temperature near %.2e K (= %.3f T_Pl for any constants); a_bounce/a_now ~ %.1e photon-only, ~%.1e "
          "with g*s" % (ct["T_bounce_max_K"], ct["T_max_over_T_pl"], ct["a_bounce_over_now_photon"],
                        ct["a_bounce_over_now_gstar"]))
    print("  the hot coupled phase, by model: compression (LQC, LQT) heats the background to %.0f K at a = %.2e, where "
          "it re-couples (from LQT's turnaround, a_max 1.69 at %.2f K: a factor %.0f); Ijjas-Steinhardt's slow "
          "contraction (alpha = %.2f) shrinks a only %.0f-fold even to the Planck rate (the old background to ~%.0f "
          "K) -- the hot phase there is regenerated at the bounce" % (
              ct["T_recouple_K"], ct["a_recouple"], ct["T_at_turnaround_K_LQT"],
              ct["contraction_factor_LQT_to_recouple"], ct["slow_alpha"], ct["slow_shrink_to_planck_rate"],
              ct["slow_T_reached_K"]))
    print("  timescales: AIS's minimum end of expansion is %.1f Gyr at m_Pl/m = 10 (0.27/H0, the board's H0 time %.1f "
          "Gyr; the paper's own 14 Gyr gives 3.8), sooner for steeper potentials (Fig. 4, OPEN); today T changes by "
          "%.1e of itself per century -- the corridor's schedules are untouched unless contraction began within one" % (
              ct["AIS_end_of_expansion_Gyr_mPl_m_10"], ct["hubble_time_Gyr"], ct["dT_over_T_per_century_now"]))


def selftest():
    n_pass = n_fail = n_ctl = 0
    structural = []

    def chk(label, ok, ctl=False):
        nonlocal n_pass, n_fail, n_ctl
        n_ctl += ctl
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else "", label))

    d = collect()
    g, cl, ap, ca, ns, co, sk, ct = (d[k] for k in ("gas", "collisionless", "acoustic_past", "carrier",
                                                     "noise_and_sink", "coherence", "shared_sky", "contraction"))
    chk("photon density by numerical integration equals 2 zeta(3)/pi^2 (kT/hbar c)^3 to 1e-6 (%.4f /cm^3)" %
        g["n_per_cm3"], abs(g["n_per_m3"] / g["closed_n_per_m3"] - 1) < 1e-6)
    chk("pin: the isotropic number intensity n c / 4 pi = 9.80e15 m^-2 s^-1 sr^-1 (verifier) (%.3e)" %
        g["number_intensity"], abs(g["number_intensity"] / 9.80e15 - 1) < 5e-3)
    chk("one polarisation (1/(2 pi^2)) misses that pin by a factor 2",
        abs(gas(T0, 1)["number_intensity"] / 9.80e15 - 1) > 0.4, ctl=True)
    chk("pin: sigma(omega = 1 eV) = 7.27e-66 cm^2, the standard low-energy value (%.3e) -- fixes alpha^4, (omega/m)^6"
        % cl["sigma_1eV_cm2"], abs(cl["sigma_1eV_cm2"] / 7.27e-66 - 1) < 0.01)
    chk("alpha^8 in place of alpha^4 misses that pin by 18 orders",
        abs(math.log10(cl["sigma_1eV_cm2"] * ALPHA ** 4 / 7.27e-66)) > 5, ctl=True)
    chk("angular factor <(1-mu)^4/8> = 2/5 by quadrature (%.6f)" % (
        _simpson(lambda m: (1 - m) ** 4 / 8 / 2, -1.0, 1.0, 2000)),
        abs(_simpson(lambda m: (1 - m) ** 4 / 8 / 2, -1.0, 1.0, 2000) - 0.4) < 1e-9)
    chk("mean photon-photon mean free path 10^%.1f Hubble lengths (verifier 10^53.1); the first bound (10^%.1f) is below "
        "it; a tail photon at x = 30 still above 10^50 (10^%.1f)" % (cl["orders_mean"], cl["orders_bound"],
                                                                      cl["orders_tail_x30"]),
        abs(cl["orders_mean"] - 53.1) < 0.1 and cl["orders_bound"] < cl["orders_mean"] and cl["orders_tail_x30"] > 50)
    chk("before decoupling the medium's sound speed lies below c/sqrt(3) (%.3f c)" % ap["cs_over_c_at_R_star"],
        ap["cs_over_c_at_R_star"] < ap["cs_over_c_no_baryons"])
    r1 = ca["rows"][0]
    chk("pin: etendue budget at 1 m^2 apertures 6.07e-18 photons/s (%.3e); 1 km^2 needs 5.0e25 bits per photon (%.2e)" % (
        r1["photons_per_s"], ca["rows"][1]["bits_per_photon_needed"]),
        abs(r1["photons_per_s"] / 6.07e-18 - 1) < 0.01 and abs(ca["rows"][1]["bits_per_photon_needed"] / 5.0e25 - 1) < 0.02)
    chk("noise: occupation 1 at x = ln 2, i.e. %.1f GHz (verifier 39.4); %.0f at 1 GHz (verifier 56)" % (
        ns["nu_occupation_1_GHz"], ns["occupation_at_1GHz"]),
        abs(ns["nu_occupation_1_GHz"] - 39.4) < 0.1 and abs(ns["occupation_at_1GHz"] - 56) < 1)
    chk("at the board's floor quantum the occupation is 10^%.3g (verifier -4.86e8)" % ns["log10_occupation"],
        abs(ns["log10_occupation"] / -4.86e8 - 1) < 0.01)
    chk("Landauer: the board's 1-yr channel floor is %.2e times the erasure cost at T0 (verifier 5.6e8); radiator %.0f m^2 "
        "(verifier ~335)" % (ns["floor_over_landauer"], ns["radiator_m2"]),
        abs(ns["floor_over_landauer"] / 5.6e8 - 1) < 0.02 and abs(ns["radiator_m2"] - 335) < 10)
    num = _simpson(lambda x: (x ** 3 / math.expm1(x)) * (math.sin(x * 1.19) / (x * 1.19)) if x > 0 else 0.0,
                   0.0, 60.0, 200000) / (math.pi ** 4 / 15.0)
    chk("the trace's exact closed form equals the spectral integral at rho = 1.19 to 1e-9 (%.10f vs %.10f)" % (
        coherence_rho(1.19), num), abs(coherence_rho(1.19) / num - 1) < 1e-9)
    chk("coherence(0) is 1", coherence(0.0)["trace"] == 1.0, ctl=True)
    chk("across Earth-Proxima: trace %.1e, longitudinal %.1e -- both negligible (below 1e-50)" % (
        co["L"]["trace"], co["L"]["longitudinal_asymptote"]),
        co["L"]["trace"] < 1e-50 and co["L"]["longitudinal_asymptote"] < 1e-50)
    chk("shared sky: %d modes; parallax below 1e-9 rad; aberration %.2e rad (verifier ~1.1e-4, ~9 %% of the ell scale)" % (
        sk["modes"], sk["aberration_rad"]),
        sk["modes"] == 6295077 and sk["parallax_bound_rad"] < 1e-9 and abs(sk["aberration_rad"] / 1.1e-4 - 1) < 0.05)
    chk("H-CONTRACT: frame.py's z3 lemma (a > 0) proved with vacuity sat and drift below 1e-9; its control (a >= 0) "
        "fails as it must", ct["lemma"]["claim"] == "unsat" and ct["lemma"]["vacuity"] == "sat"
        and ct["lemma"]["drift"] < 1e-9 and ct["lemma"]["control_a_ge_0"] == "sat")
    chk("compression re-couples the background at %.0f K; Ijjas-Steinhardt slow contraction reaches only %.0f K even at the "
        "Planck rate (a shrinks %.0f-fold)" % (ct["T_recouple_K"], ct["slow_T_reached_K"],
                                              ct["slow_shrink_to_planck_rate"]),
        2900 < ct["T_recouple_K"] < 3050 and ct["slow_T_reached_K"] < 100)
    structural.append("T_max / T_Pl = (15 x 0.41 / pi^2)^(1/4) = %.3f for any constants (H-RADIATION-AT-BOUNCE)"
                      % ct["T_max_over_T_pl"])
    structural.append("shared randomness carries no message: no-signalling (nosig.py) -- a common reference, not a "
                      "channel")
    structural.append("H-CONTRACT is carried, not shown and not excluded: the READ fits that recollapse need a negative "
                      "vacuum or potential, and the Bayesian evidence for evolving dark energy is weak or null after "
                      "Dovekie")
    for s in structural:
        print("  STRUCTURAL: " + s)
    print("medium.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
