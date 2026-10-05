#!/usr/bin/env python3
"""
medium.py -- H-CMB-CORRIDOR, reading 2: the cosmic background as the corridor's MEDIUM or CARRIER.

Not seated; not yet verified.  M (rulings item 45): "Seat it, then medium" -- after reading 1 (cmbframe.py, the
background's rest frame as H-FRAME's frame) was seated, this reading asks whether the background can be what the
corridor's information travels ON.  M (item 47, on H-CONTRACT, item 46): "2, then 1" -- the status of a contracting
universe READ first, then folded into this reading (section (H) below).  M's hypotheses H-CMB-CORRIDOR and
H-CMB-UNIVERSAL (item 41) and H-CONTRACT (item 46) are carried, never results.

    python3 medium.py              report
    python3 medium.py --selftest   checks, with CONTROLS
    python3 medium.py --json       the numbers as JSON

WHAT "MEDIUM" IS TAKEN TO MEAN (five readings, each priced; none is dismissed, each says what would change it)
  (A) the photon gas itself: its number, energy and entropy densities from T0 (READ) -- what is there to use;
  (B) a MEDIUM in the acoustic sense, carrying a collective mode: needs the photons to interact; the photon-photon
      mean free path is set against the Hubble length.  Before decoupling it WAS such a medium (the photon-baryon
      fluid, sound speed c / sqrt(3(1+R))), READ;
  (C) a passive CARRIER: background photons already heading from A toward B, redirected or modulated at A -- the
      photon budget through the two apertures and the contrast an isotropic background allows;
  (D) the background as the NOISE of an active link at the board's floor quantum, and as the coldest heat sink
      (Landauer at T0) set against the board's channel floor;
  (E) a SHARED RESOURCE between the ends: the field's spatial coherence across the span (quantum correlation), and
      the common sky both ends see (shared classical randomness, which carries no message -- nosig.py).

NAMED HYPOTHESES
  H-CMB-BLACKBODY     the background is a blackbody at T0 (Fixsen's combined value) -- its spectrum's distortions are
                      not modelled.
  H-OMEGA-CM          King & Heinzl's omega in the low-energy gamma-gamma cross-section is the photon energy in the
                      centre-of-mass frame (the source's threshold statement 'omega = m' implies per photon; the
                      reader's inference, not printed); bounded above by the lab energy for the rate.
  H-ALPHA             alpha = 7.2973525643e-3 as settle.py types it (CODATA 2022 value, MEMORY-level here); the
                      collisionless margin spans tens of orders, so its precision cannot matter.
  H-ISOTROPIC-FLUX    the background's intensity is isotropic (dipole and anisotropy only in the contrast, (C)).
  H-APERTURES         equal apertures at A and B, 1 m^2 and 1 km^2 priced.
  H-PASSIVE           a passive modulator redirects background photons; its contrast is bounded by the background's
                      own anisotropy (the dipole, 8 beta for apex against anti-apex, bolometric).
  H-SCALAR-COHERENCE  the degree of coherence taken as the TRACE of the coherence tensor (sin kr / kr per frequency,
                      Henkel et al. physics/0008028v1 p.4, p.6), averaged over the Planck energy spectrum; tensor
                      components differ (Mohanty cond-mat/0005233v1 eq. 8) but not in their power-law fall-off.
  H-LSS-DISTANCE      the last-scattering surface lies beyond the Hubble radius c/H0 (used only to bound the parallax
                      between the ends' skies).
  H-MODES             the shared sky's independent modes counted as Planck's TT multipoles 2..2508 (all m).
  -- section (H), H-CONTRACT (M item 46; READ first, item 47) --
  H-CONTRACT          M's: the universe contracts as well as expands.  Carried; not shown, not excluded (READ, below).
  H-EFFECTIVE-METRIC  a nonsingular bounce described by an effective FRW metric with a > 0 throughout (LQC's effective
                      equations; Ijjas-Steinhardt's classical bounce), so frame.py's z3 lemma applies to it.
  H-RADIATION-AT-BOUNCE the bounce temperature priced as if radiation held the whole of LQC's maximum density (an upper
                      figure for the background's temperature there).
  H-T-SCALES          T proportional to 1/a in both phases (constant radiation entropy, T^3 a^3 = const: Novello & Perez
                      Bergliaffa arXiv:0802.1634v1 p.86); the step from rho ~ a^-4 to T ~ 1/a is standard, labelled.
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
KB = nopath.KB
L = cmbframe.L
H0 = cmbframe.H0
YEAR_S = seat.YEAR_S
EV = 1.602176634e-19
T0 = cmbframe.T0[0]                 # Fixsen 2009, READ (via cmbframe)
ALPHA = 7.2973525643e-3             # H-ALPHA
ME_C2_EV = 0.51099895069e6          # CODATA 2022, READ (arXiv:2409.03787v1 Table XXXIII; Q1s-signed.md)

# ---------------------------------------------------------------------------------------------------------------------
# READ at source (2026-10-05; alphaXiv answer_pdf_queries)
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
COHERENCE_SOURCE = ("Henkel, Joulain, Carminati & Greffet, arXiv:physics/0008028v1: far-field blackbody coherence "
                    "'(sin ks)/ks' (p.4), Fig. 3(a) caption (p.6); coherence length lambda/2 (p.1, citing Mandel & "
                    "Wolf, NAMED-NOT-READ)")
APERTURES_M2 = (1.0, 1.0e6)         # H-APERTURES


def _zeta(s, n=200000):
    return sum(k ** -s for k in range(1, n)) + n ** (1 - s) / (s - 1)


def _simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b) + sum((4 if i % 2 else 2) * f(a + i * h) for i in range(1, n))
    return s * h / 3


# ---------------------------------------------------------------------------------------------------------------------
# (A) the photon gas
# ---------------------------------------------------------------------------------------------------------------------
def gas(T=T0):
    """Densities from the Planck distribution, integrated numerically; the closed forms are the check."""
    lam = HBAR * C / (KB * T)                                   # thermal length hbar c / kT
    In = _simpson(lambda x: x * x / math.expm1(x) if x > 0 else 0.0, 0.0, 60.0)     # 2 zeta(3)
    Iu = _simpson(lambda x: x ** 3 / math.expm1(x) if x > 0 else 0.0, 0.0, 60.0)    # pi^4/15
    n = In / (math.pi ** 2) / lam ** 3                          # two polarisations: 2/(2 pi^2) = 1/pi^2
    u = Iu / (math.pi ** 2) * KB * T / lam ** 3
    s = 4.0 / 3.0 * u / T
    return {"T_K": T, "thermal_length_m": lam, "n_per_m3": n, "n_per_cm3": n * 1e-6, "u_J_m3": u,
            "s_J_K_m3": s, "s_bits_m3": s / (KB * math.log(2)), "mean_E_eV": u / n / EV,
            "closed_n_per_m3": 2 * _zeta(3) / math.pi ** 2 / lam ** 3,
            "closed_u_J_m3": math.pi ** 2 / 15 * KB * T / lam ** 3,
            "bits_per_photon": (s / (KB * math.log(2))) / n,
            "tube_bits_1m2": s / (KB * math.log(2)) * 1.0 * L}


# ---------------------------------------------------------------------------------------------------------------------
# (B) a medium in the acoustic sense
# ---------------------------------------------------------------------------------------------------------------------
def collisionless(T=T0):
    """Upper bound on a background photon's gamma-gamma scattering rate: Gamma <= c n <sigma>, with omega taken as the
    lab energy (H-OMEGA-CM: the CM energy is never larger) and <(E/m)^6> over the photon-number spectrum, i.e.
    (kT/m)^6 Gamma(9) zeta(9) / (Gamma(3) zeta(3)).  The mean free path is set against the Hubble length c/H0."""
    g = gas(T)
    lbar = HBAR / (ME_C2_EV * EV / C)                           # reduced Compton wavelength, m
    kT_over_m = KB * T / (ME_C2_EV * EV)
    x6 = math.factorial(8) * _zeta(9) / (math.factorial(2) * _zeta(3))
    sigma_eff = GAMMA_GAMMA["coef"] * ALPHA ** 4 * kT_over_m ** 6 * x6 * lbar ** 2
    mfp = 1.0 / (g["n_per_m3"] * sigma_eff)
    hubble = C / H0
    return {"sigma_eff_m2": sigma_eff, "x6_mean": x6, "mfp_m": mfp, "hubble_m": hubble,
            "orders_beyond_hubble": math.log10(mfp / hubble)}


def acoustic_past():
    """Before decoupling the background WAS a medium: the photon-baryon fluid, c_s = c / sqrt(3(1+R)) (READ), at the
    observed R* (READ).  Decoupling temperature T0 (1 + z*) (Planck z*, READ; T(z) scaling READ in cmbframe)."""
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
    """Background photons that leave aperture A heading into aperture B: Ndot = (n c / 4 pi) A_A A_B / L^2
    (H-ISOTROPIC-FLUX).  Set against the board's demand (step1c/demand.py, species count, 1 yr): the bits each such
    photon would have to carry.  The contrast a passive modulator has to work with (H-PASSIVE): redirecting the apex
    patch instead of the anti-apex changes the bolometric intensity by ((1+b)/(1-b))^4 - 1."""
    g = gas()
    T1 = demand.SCHEDULES_S[1]
    name, bits = demand.counts()[0]
    rate = bits / T1
    beta = cmbframe.DIPOLE["beta"][0]
    rows = []
    for A in APERTURES_M2:
        nd = g["n_per_m3"] * C / (4 * math.pi) * A * A / (L * L)
        rows.append({"aperture_m2": A, "photons_per_s": nd, "bits_per_photon_needed": rate / nd,
                     "photons_in_a_year": nd * T1})
    return {"count": name, "bits": bits, "rate_bits_s": rate, "rows": rows,
            "contrast_dipole": ((1 + beta) / (1 - beta)) ** 4 - 1, "bits_per_photon_thermal": g["bits_per_photon"]}


# ---------------------------------------------------------------------------------------------------------------------
# (D) noise and heat sink
# ---------------------------------------------------------------------------------------------------------------------
def noise_and_sink():
    """The background's mean occupation at the board's floor quantum (step1c/demand.py's channel, species, 1 yr) and at
    its own peak; the Landauer cost of the species count at T0 (nopath.landauer_energy, asked) against the board's
    1-yr channel-floor energy."""
    T1 = demand.SCHEDULES_S[1]
    ch = demand.channel(T1)
    name = demand.counts()[0][0]
    E_q = ch[name]["quantum_eV"] * EV
    x = E_q / (KB * T0)
    bits = demand.counts()[0][1]
    land = nopath.landauer_energy(bits, T0)
    floor = ch[name]["floor_J_one_pol"]
    return {"quantum_eV": ch[name]["quantum_eV"], "x_over_kT": x, "log10_occupation": -x / math.log(10),
            "occupation_at_peak": 1.0 / math.expm1(2.821439), "landauer_J": land, "channel_floor_J": floor,
            "floor_over_landauer": floor / land, "landauer_per_bit_J": KB * T0 * math.log(2)}


# ---------------------------------------------------------------------------------------------------------------------
# (E) a shared resource
# ---------------------------------------------------------------------------------------------------------------------
def coherence(r_m, T=T0):
    """Degree of spatial coherence of the background between two points r apart (H-SCALAR-COHERENCE): the sinc kernel
    averaged over the Planck energy spectrum, gamma(rho) = (15/pi^4) int x^3/(e^x-1) sin(x rho)/(x rho) dx, rho =
    r kT/(hbar c).  For rho >= 5 the asymptote 15/(pi^4 rho^4) is used (checked against the integral in the
    selftest)."""
    rho = r_m * KB * T / (HBAR * C)
    if rho >= 5.0:
        return rho, 15.0 / (math.pi ** 4 * rho ** 4)
    f = lambda x: (x ** 3 / math.expm1(x)) * (math.sin(x * rho) / (x * rho)) if x > 0 else 0.0
    return rho, _simpson(f, 0.0, 60.0, 200000) / (math.pi ** 4 / 15.0)


def shared_sky():
    """Both ends see the same sky: the parallax of the last-scattering surface between them is below L / (c/H0)
    (H-LSS-DISTANCE); the independent modes up to Planck's ell_max (H-MODES).  Shared randomness carries no message
    (nosig.py: no-signalling) -- it is a common reference, not a channel."""
    modes = (ELL_MAX_TT + 1) ** 2 - 4
    return {"parallax_bound_rad": L * H0 / C, "modes": modes}


# ---------------------------------------------------------------------------------------------------------------------
# (H) H-CONTRACT: what the READ status says, and what contraction does to the background as frame and medium
# ---------------------------------------------------------------------------------------------------------------------
CONTRACT_READ = {
    "accelerating now": "Riess et al. 1998 (astro-ph/9805201v1): q0 < 0 at 2.8-3.9 sigma, q0 = -1.0 +- 0.4 (p.16); "
                        "DESI DR1 (2404.03002v3, printed p.32): acceleration required at z < 0.7 in LCDM, wCDM, w0waCDM",
    "evolving dark energy": "DESI DR2 (2503.14738v3 Table VI p.24): w0 > -1, wa < 0 preferred at 2.8-4.2 sigma "
                            "(frequentist); DES-Dovekie recalibration (2511.07517v3 p.1): 3.2 sigma, 'only a weak "
                            "preference' (Bayesian); Ong, Yallup & Handley (2511.10631v3 Table I p.2): log Bayes factor "
                            "-0.30 +- 0.19 with Dovekie (no evidence)",
    "recollapse fits": "only in models with a negative vacuum or potential: Luu, Qiu & Tye (2506.24011v2): best fit "
                       "a_max ~ 1.69, turnaround ~11 Gyr from now, lifespan 33.3 Gyr (eq. 4.8 p.8) -- the best fit lies "
                       "outside 1 sigma of the mean and Omega_Lambda = 0 is consistent (p.10); Andrei, Ijjas & "
                       "Steinhardt (2201.07704v2 p.8): end of expansion no sooner than 0.27/H0 at the 2 sigma fit "
                       "(m_Pl/m = 10); Gialamas et al. (2506.21542v2 p.9): negative vacuum preferred at 93.8 % (with "
                       "the pre-recalibration DESY5)",
    "bounce, nonsingular": "LQC: V_min = 2 sqrt(V+ V-)/||chi||^2 > 0 for every state (Ashtekar & Singh 1108.0893v2 eq. "
                           "3.23 p.39), rho_max ~ 0.41 rho_Pl (p.32, eq. 5.7 p.73); time relational (p.33).  Ijjas & "
                           "Steinhardt: the scale factor 'shrinks to a finite critical size' (1803.01961v1 printed p.7)",
    "bounce, singular": "Steinhardt & Turok (hep-th/0111098v2): in the 4d Einstein frame the scale factor 'collapses to "
                        "zero at the big crunch' (p.7), curvature diverges (p.18); the resolution is postulated in five "
                        "dimensions (p.3)",
    "radiation through the bounce": "Ijjas & Steinhardt (1904.08022v1 pp.3-4): created at each bounce, the old diluted; "
                                    "'the entropy observed within the Hubble radius is the same from cycle to cycle' "
                                    "(p.4).  Steinhardt & Turok (pp.12, 20): generated at the bounce, the prior diluted.  "
                                    "LQC: the conservation law is unchanged (eq. 5.10 p.74), so a radiation fluid would "
                                    "pass through (the reader's INFERENCE, not printed)",
}
A_MAX_LQT = 1.69                    # Luu, Qiu & Tye 2506.24011v2 p.8 (best fit only)
AIS_END_OVER_H0 = 0.27              # Andrei, Ijjas & Steinhardt 2201.07704v2 p.8 (minimum, m_Pl/m = 10)
LQC_RHO_MAX_OVER_PL = 0.41          # Ashtekar & Singh 1108.0893v2 p.32, eq. 5.7 p.73


def contraction():
    """(H1) loop-freedom through a bounce: frame.py's z3 lemma needs a > 0 only -- asked; a nonsingular bounce keeps it
    (H-EFFECTIVE-METRIC), a crunch to a = 0 breaks its premise (the lemma's own control).  (H2) the temperature label:
    T ~ 1/a both ways (H-T-SCALES), so below the bounce temperature each T occurs twice; LQC's ceiling priced
    (H-RADIATION-AT-BOUNCE).  (H3) the medium returns: re-coupling at T0 (1 + z*).  (H4) timescales against the
    corridor's schedules."""
    with contextlib.redirect_stdout(io.StringIO()):
        lem = cmbframe.frame.frw_time_function_lemma()
    G = cosmo._G
    u_pl = C ** 7 / (HBAR * G * G)                               # Planck energy density, J/m^3
    u_max = LQC_RHO_MAX_OVER_PL * u_pl
    T_max = (15.0 * u_max * (HBAR * C) ** 3 / math.pi ** 2) ** 0.25 / KB
    ap = acoustic_past()
    t_h = cosmo.hubble_time_gyr()
    century = 100 * YEAR_S
    return {"lemma": lem, "T_bounce_max_K": T_max, "u_max_J_m3": u_max,
            "a_bounce_over_now": T0 / T_max, "T_at_turnaround_K_LQT": T0 / A_MAX_LQT,
            "a_recouple": ap["a_decoupling"], "T_recouple_K": ap["T_decoupling_K"],
            "contraction_factor_LQT_to_recouple": A_MAX_LQT / ap["a_decoupling"],
            "AIS_end_of_expansion_Gyr": AIS_END_OVER_H0 * t_h, "hubble_time_Gyr": t_h,
            "dT_over_T_per_century_now": H0 * century, "preimages_of_T_below_max": 2}


def collect():
    return {"contraction": contraction(), "gas": gas(), "collisionless": collisionless(), "acoustic_past": acoustic_past(), "carrier": carrier(),
            "noise_and_sink": noise_and_sink(),
            "coherence": {k: coherence(r) for k, r in (("1 mm", 1e-3), ("1 cm", 1e-2), ("1 m", 1.0), ("L", L))},
            "shared_sky": shared_sky()}


def report():
    d = collect()
    g, cl, ap, ca, ns, co, sk = (d[k] for k in ("gas", "collisionless", "acoustic_past", "carrier", "noise_and_sink",
                                                 "coherence", "shared_sky"))
    print("H-CMB-CORRIDOR, reading 2: the cosmic background as MEDIUM or CARRIER (not verified; not seated)\n")
    print("(A) THE PHOTON GAS at T0 = %.5f K (Fixsen, READ)" % T0)
    print("  %.1f photons/cm^3; %.3e J/m^3; entropy %.3e bits/m^3 (%.2f bits per photon); mean photon %.3f meV; "
          "thermal length %.3f mm" % (g["n_per_cm3"], g["u_J_m3"], g["s_bits_m3"], g["bits_per_photon"],
                                      g["mean_E_eV"] * 1e3, g["thermal_length_m"] * 1e3))
    print("  a 1 m^2 tube from Earth to Proxima holds %.2e bits of background entropy" % g["tube_bits_1m2"])
    print("\n(B) A MEDIUM IN THE ACOUSTIC SENSE")
    print("  photon-photon mean free path >= %.1e m: %.0f orders beyond the Hubble length (%.2e m) -- collisionless, "
          "no collective mode today" % (cl["mfp_m"], cl["orders_beyond_hubble"], cl["hubble_m"]))
    print("  before decoupling it WAS a medium: the photon-baryon fluid, c_s = %.3f c at R* = 0.60 (%.3f-%.3f c); "
          "decoupling at T0(1+z*) = %.0f K" % (ap["cs_over_c_at_R_star"], ap["cs_range"][0], ap["cs_range"][1],
                                              ap["T_decoupling_K"]))
    print("\n(C) A PASSIVE CARRIER (%s, %.2e bits; %.2e bits/s at 1 yr)" % (ca["count"], ca["bits"], ca["rate_bits_s"]))
    for r in ca["rows"]:
        print("  apertures %.0e m^2 each: %.2e background photons/s leave A into B -- %.1e bits per photon needed"
              % (r["aperture_m2"], r["photons_per_s"], r["bits_per_photon_needed"]))
    print("  a passive modulator's contrast is bounded by the dipole: %.2e (apex against anti-apex, bolometric)"
          % ca["contrast_dipole"])
    print("\n(D) NOISE AND HEAT SINK")
    print("  at the board's floor quantum (%.0f keV) the background's occupation is 10^%.3g: it is not the noise there; "
          "at its own peak it is %.3f" % (ns["quantum_eV"] / 1e3, ns["log10_occupation"], ns["occupation_at_peak"]))
    print("  Landauer at T0: %.2e J per bit, %.2e J for the species count -- the board's 1-yr channel floor (%.2e J) "
          "is %.1e times that" % (ns["landauer_per_bit_J"], ns["landauer_J"], ns["channel_floor_J"],
                                   ns["floor_over_landauer"]))
    print("\n(E) A SHARED RESOURCE")
    for k, (rho, gm) in co.items():
        print("  degree of coherence over %-4s (rho = %.2e): %.2e" % (k, rho, gm))
    print("  the two skies differ by a parallax below %.1e rad; %d independent modes to ell = %d -- shared classical "
          "randomness, which carries no message (no-signalling)" % (sk["parallax_bound_rad"], sk["modes"], ELL_MAX_TT))
    ct = d["contraction"]
    print("\n(H) H-CONTRACT (M item 46; status READ first, item 47)")
    for k, v in CONTRACT_READ.items():
        print("  READ, %s: %s" % (k, v[:150] + ("..." if len(v) > 150 else "")))
    print("  loop-freedom: frame.py's z3 lemma needs a > 0 only (claim %s, control a >= 0 %s) -- a nonsingular bounce "
          "keeps the keyed network loop-free; a crunch to a = 0 (the 4d ekpyrotic frame) breaks the premise" % (
              ct["lemma"]["claim"], ct["lemma"]["control_a_ge_0"]))
    print("  temperature label: T ~ 1/a both ways, so below the bounce temperature each T occurs twice; LQC caps it near "
          "%.1e K (a_bounce/a_now ~ %.1e, if radiation held the whole density)" % (ct["T_bounce_max_K"],
                                                                                 ct["a_bounce_over_now"]))
    print("  the medium returns: contracting to a = %.2e the background reaches %.0f K and re-couples to matter "
          "(c_s ~ 0.46 c); from LQT's best-fit turnaround (a_max 1.69, T %.2f K) that is a contraction by %.0f" % (
              ct["a_recouple"], ct["T_recouple_K"], ct["T_at_turnaround_K_LQT"],
              ct["contraction_factor_LQT_to_recouple"]))
    print("  timescales: expansion ends no sooner than %.1f Gyr from now in AIS's 2-sigma fit (0.27/H0, H0 time %.1f "
          "Gyr); over a century today T changes by %.1e of itself -- contraction does not touch the corridor's "
          "schedules" % (ct["AIS_end_of_expansion_Gyr"], ct["hubble_time_Gyr"], ct["dT_over_T_per_century_now"]))


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
    g, cl, ap, ca, ns, co, sk = (d[k] for k in ("gas", "collisionless", "acoustic_past", "carrier", "noise_and_sink",
                                                 "coherence", "shared_sky"))
    chk("photon density by numerical integration equals the closed form 2 zeta(3)/pi^2 (kT/hbar c)^3 to 1e-6 "
        "(%.4f /cm^3)" % g["n_per_cm3"], abs(g["n_per_m3"] / g["closed_n_per_m3"] - 1) < 1e-6)
    chk("energy density equals (pi^2/15)(kT)^4/(hbar c)^3 to 1e-6", abs(g["u_J_m3"] / g["closed_u_J_m3"] - 1) < 1e-6)
    chk("the gas at twice T0 has 8 times the photons (a control on the T^3 law)",
        abs(gas(2 * T0)["n_per_m3"] / g["n_per_m3"] - 8) < 1e-6, ctl=True)
    chk("photon-photon mean free path exceeds the Hubble length by more than 30 orders (%.0f)" %
        cl["orders_beyond_hubble"], cl["orders_beyond_hubble"] > 30)
    hot = collisionless(T0 * 1e7)
    chk("at 1e7 T0 (kT ~ 2 keV) the same bound no longer certifies collisionless over a Hubble length (%.1f orders)"
        % hot["orders_beyond_hubble"], hot["orders_beyond_hubble"] < 30, ctl=True)
    chk("before decoupling the medium's sound speed lies below c/sqrt(3) (%.3f c)" % ap["cs_over_c_at_R_star"],
        ap["cs_over_c_at_R_star"] < ap["cs_over_c_no_baryons"])
    r1 = ca["rows"][0]
    chk("passive carrier: at 1 m^2 apertures fewer than 1e-10 background photons/s go A -> B (%.2e)" %
        r1["photons_per_s"], r1["photons_per_s"] < 1e-10)
    chk("even at 1 km^2 apertures each photon would have to carry more than 1e20 bits (%.1e)" %
        ca["rows"][1]["bits_per_photon_needed"], ca["rows"][1]["bits_per_photon_needed"] > 1e20)
    chk("the background is not the noise at the board's floor quantum: occupation below 1e-1000 (10^%.3g)" %
        ns["log10_occupation"], ns["log10_occupation"] < -1000)
    chk("the board's 1-yr channel floor exceeds the Landauer cost at T0 of the same bits by more than 1e6 (%.1e)" %
        ns["floor_over_landauer"], ns["floor_over_landauer"] > 1e6)
    rho5 = 5.0 / (KB * T0 / (HBAR * C))
    f = lambda x: (x ** 3 / math.expm1(x)) * (math.sin(x * 5.0) / (x * 5.0)) if x > 0 else 0.0
    direct = _simpson(f, 0.0, 60.0, 200000) / (math.pi ** 4 / 15.0)
    chk("the coherence asymptote 15/(pi^4 rho^4) matches the integral at rho = 5 to 1e-6 (%.6e vs %.6e)" % (
        direct, coherence(rho5)[1]), abs(direct / coherence(rho5)[1] - 1) < 1e-6)
    chk("degree of coherence across Earth-Proxima below 1e-70 (%.1e)" % co["L"][1], co["L"][1] < 1e-70)
    chk("at zero separation the coherence is 1 (control on the normalisation)",
        abs(_simpson(lambda x: x ** 3 / math.expm1(x) if x > 0 else 0.0, 0.0, 60.0) / (math.pi ** 4 / 15) - 1) < 1e-6,
        ctl=True)
    chk("shared sky: %d modes to ell = %d; parallax below 1e-9 rad (%.1e)" % (sk["modes"], ELL_MAX_TT,
                                                                             sk["parallax_bound_rad"]),
        sk["modes"] == 6295077 and sk["parallax_bound_rad"] < 1e-9)
    ct = d["contraction"]
    chk("H-CONTRACT: frame.py's z3 lemma (a > 0) proved, its control (a >= 0) fails as it must: nonsingular bounce "
        "loop-free, crunch not covered", ct["lemma"]["claim"] == "unsat" and ct["lemma"]["control_a_ge_0"] == "sat")
    chk("the background re-couples on contraction to a = 1/(1+z*) at %.0f K, between 2900 and 3050 K" %
        ct["T_recouple_K"], 2900 < ct["T_recouple_K"] < 3050)
    T_pl = math.sqrt(HBAR * C ** 5 / cosmo._G) / KB
    chk("LQC's bounce caps the background's temperature below the Planck temperature sqrt(hbar c^5/G)/k = %.3e K "
        "(%.2e K)" % (T_pl, ct["T_bounce_max_K"]), 1e30 < ct["T_bounce_max_K"] < T_pl)
    chk("over a century today T changes by less than 1e-7 of itself (%.1e): contraction is irrelevant to the schedules"
        % ct["dT_over_T_per_century_now"], ct["dT_over_T_per_century_now"] < 1e-7)
    structural.append("shared randomness carries no message: no-signalling (nosig.py) -- a common reference, not a "
                      "channel")
    structural.append("H-CONTRACT is carried, not shown and not excluded: the READ fits that recollapse need a negative "
                      "vacuum or potential, and the Bayesian evidence for evolving dark energy is weak or null after "
                      "Dovekie")
    structural.append("a passive modulator of an isotropic background has contrast only from its anisotropy (H-PASSIVE)")
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
