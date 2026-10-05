#!/usr/bin/env python3
"""
support.py -- H-M-SUPPORT's dynamics: how observation extends the clock's support, read with H-LOCAL-CLOCK.

Seated in ledger.py section 8h (M-RULINGS item 55; first written "Not seated"); verified once (2026-10-05), its findings applied; first-written claims kept under HISTORY.  M (rulings item 54): "3, then 2, then 1 please" -- M-SUPPORT's dynamics first.  M-SUPPORT
(unobserved.py) is M's stronger reading of item 48 as a computable rule: the clock's support is the coupled epochs, and
observation extends it through records.  Item 52 (H-LOCAL-CLOCK) is carried as M's answer to its open dynamics: "The
clock is relative to the matter-based observation".  Carried as M's hypotheses, never as results.

    python3 support.py              report
    python3 support.py --selftest   checks, with CONTROLS
    python3 support.py --json       the numbers as JSON

THE READING (H-SUPPORT-IS-RECORDS)
  On this hypothesis, matter observes the photons by scattering them (M's H-TWO-OBSERVERS, item 49: 'matter itself is
  capable of observation'), each Thomson scattering a record (H-RECORD-DURABLE).
  The rate at which matter records a given photon is Gamma = n_e sigma_T c; per e-fold of expansion it is Gamma/H.  So
  the support's growth law is
        d(support)/d ln a = Gamma / H = n_e sigma_T c / H        (records per photon per e-fold)
  and two supports follow from it, both standard cosmology under a new name:
    ALL-RECORDS   the epochs at which matter recorded the photons, weighted by d tau (tau the Thomson optical depth);
    LAST-RECORD   the epoch at which today's photon was last recorded by matter: the visibility function
                  g(z) = exp(-tau) d tau/dz.  Its weight over [a, b] is exp(-tau(a)) - exp(-tau(b)).
  'Decoupling' is then where matter stops recording the photons faster than the universe expands, Gamma/H = 1, and
  where the last record peaks.  M's item 48 ('The decoupling only exists upon observation of a universe') reads here as:
  decoupling IS the edge of matter's observation of the light -- a property of records.  This mapping is a NAMED
  hypothesis; the physics under it is not.

WHAT IS COMPUTED
  (1) The ionisation history: hydrogen recombination by the effective three-level atom with RECFAST's fudge factor
      (Seager, Sasselov & Scott astro-ph/9909275v2 eq. 1, eq. 3, p.3-4: Lambda_2s = 8.22458 /s, lambda_Lya = 121.5682
      nm, alpha_B fit a = 4.309, b = -0.6166, c = 0.6703, d = 0.5300, F = 1.14, beta from alpha by detailed balance,
      K = lambda^3/(8 pi H)), Saha until x_p < 0.99, implicit Euler after; helium I by Saha (H-HEI-SAHA: Seager p.1-2
      find He I slower than Saha); T_M = T_R (H-TM-EQUALS-TR: Seager p.4 recommend eq. 5 at low z).  Reionisation by
      Planck's redshift-symmetric tanh in y = (1+z)^(3/2), delta z = 0.5, helium's first ionisation with hydrogen and
      its second at z = 3.5 (Planck XLVII 1605.03507v3 eq. 2 p.5).  Planck 2018 inputs (1807.06209v4 Table 1 p.15,
      Table 2 p.16): Omega_b h^2 0.02237, Omega_m 0.3153, H0 67.36, tau 0.0544, z_re 7.67, Y_P 0.2454 (caption).
      Checked against Planck's z* (tau = 1), age and r*; Saha equilibrium is the control.
  (2) Matter's observation of the light: Gamma/H through the history; tau; the two supports; Planck's reionisation
      tau reproduced from z_re (a control at z_re = 11 misses).
  (3) The dynamics, as M-SUPPORT's growth: the support counted from a 'present' z_now grows at Gamma/H per e-fold --
      fast while coupled, nearly halted after decoupling, resumed at reionisation, still 0.2 % per Hubble time today.
  (4) Into the toy (unobserved.py): the clock weighting GLM leave 'completely arbitrary' (H-CLOCK-WEIGHT) replaced by the
      record weightings, binned onto the toy's ticks; the medium's state under each against static M-SUPPORT and TRACED.
  (5) Local clocks at last scattering (H-LOCAL-CLOCK at cosmic scale): in the Newtonian frame a potential Psi is a
      clock-rate offset, a temporal shift delta t/t = Psi (Hu & Dodelson astro-ph/0110414v1 printed p.14; White & Hu
      astro-ph/9609105v1 p.1 eq. 3 'in a gravitational potential clocks run slow'); each place decouples at the same
      LOCAL reading, at a shifted time; that gives an intrinsic Theta = -2 Psi/3 (matter era, eq. 13 printed p.15), the climb out
      gives Psi, the observed sum is Psi/3 (Sachs-Wolfe).  COBE's 28 microK (Hu & Dodelson p.30, citing Smoot et al.
      1992) sets the size; the time spread of local decoupling is computed.  The time-shift picture is a FRAME choice:
      in the fluid's rest frame 'proper time coincides with coordinate time' and 'The intrinsic term is negligible' (White
      & Hu p.1; their Phi has the opposite sign to Hu & Dodelson's Psi); the observed Psi/3 is the same in both.  STRUCTURAL on that point.
  (6) Today's observation: a telescope's detection is one more matter record, at clock reading T0 = 2.7255 K; its
      content is the photon's state since its last record.  A conscious reading of it is a perception of that record
      (Page; localclock.py).  STRUCTURAL.

NAMED HYPOTHESES
  H-SUPPORT-IS-RECORDS (its warrant for matter as an observer is M's own H-TWO-OBSERVERS, item 49), H-RECORD-DURABLE
  (an electron's momentum is re-thermalised at once by Coulomb collisions and ~1e9 photons per baryon; in decoherence
  physics the durable record of a scattering sits in the outgoing photon -- NAMED-NOT-READ), H-RECFAST-H, H-HEI-SAHA,
  H-TM-EQUALS-TR, H-REION-TANH, H-HE-MASS-4, H-MASSLESS-NU (Planck's Omega_m includes one 0.06 eV neutrino, Table 1
  caption p.15), H-BOHR-LEVELS, H-TOY-BINNING, H-MATTER-ERA (w_eff = 0.081 at z*, printed), H-SW-ONLY (no integrated
  Sachs-Wolfe term); with H-TOY-MEDIUM, H-CLOCK-WEIGHT (unobserved.py) and M's H-UNOBSERVED-MEDIUM, H-M-SUPPORT (as M's rule)
  and H-LOCAL-CLOCK.


HISTORY (verifier, 2026-10-05; first-written claims kept)
  * z* was first taken as tau = 1 WITH reionisation (1085.6, '-0.40 % ... about 17 sigma ... the named
    simplifications'); Planck/CAMB leave reionisation out: 1090.28, +0.03 %, 1.4 sigma.  The check is now 0.1 %.
  * 'ALL-RECORDS reproduces static M-SUPPORT to 5e-4 ... a dynamical origin' -- mostly by construction: the toy's T_dec
    is the tau = 1 temperature, and a record-free T^8 weighting does as well (3.9e-4); M-SUPPORT's own reweighting
    ambiguity is 2.3e-3.  What it shows: records stop where the coupling stops (without recombination: 0.111).
  * the LAST-RECORD 'recombination' share counted the dark ages twice (shares summed to 100.15 %); '5.28 % at
    reionisation, at t = 672 Myr' -- 672 Myr is the midpoint; the last records spread to today (median z 4.57).
  * 'local decoupling spread over 11.4 yr' -- an rms offset, in the Newtonian frame only; 'literally ... measured on the
    sky' withdrawn: only Psi/3 is measured.  White & Hu say 'negligible', not 'vanishes'.
  * the tau check allowed 1 sigma for a 0.0002 match; now 0.001.
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
WD = os.path.dirname(os.path.dirname(HERE))


def _by_path(key, path):
    if key in sys.modules:
        return sys.modules[key]
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


with contextlib.redirect_stdout(io.StringIO()):
    unobserved = _by_path("cmb_unobserved", os.path.join(HERE, "unobserved.py"))
    arrival = _by_path("wd_arrival", os.path.join(WD, "arrival.py"))
medium = unobserved.medium
cmbframe = medium.cmbframe
cosmo = cmbframe.cosmo
seat = cmbframe.seat

C = seat.C
HBAR = seat.HBAR
H_PL = seat.H
KB = medium.KB
EV = medium.EV
ALPHA = medium.ALPHA
ME = medium.ME_C2_EV * EV / C ** 2
MP = arrival.M_P                                  # CODATA 2018, as arrival.py holds it
G_N = cosmo._G
MPC = cosmo.MPC
YEAR_S = seat.YEAR_S
T0 = cmbframe.T0[0]
SIGMA_T = 8 * math.pi / 3 * (ALPHA * HBAR / (ME * C)) ** 2          # Thomson, from the constants

PLANCK18 = {"ombh2": (0.02237, 0.00015), "H0": cosmo.H0_KMSMPC, "Om": cosmo.OMEGA_M, "tau": (0.0544, 0.0073),
            "z_re": (7.67, 0.73), "z_star": medium.Z_STAR, "age_gyr": (13.797, 0.023), "r_star_mpc": (144.43, 0.26),
            "Y_P": 0.2454, "N_eff": cosmo.N_EFF,
            "source": "arXiv:1807.06209v4 Table 1 p.15 and Table 2 p.16 (TT,TE,EE+lowE+lensing); Y_P from Table 2's "
                      "caption; READ via alphaXiv 2026-10-05"}
RECFAST = {"Lambda_2s": 8.22458, "lambda_Lya_m": 121.5682e-9, "a": 4.309, "b": -0.6166, "c": 0.6703, "d": 0.5300,
           "F": 1.14, "chi_HeI_eV": 24.6,
           "source": "Seager, Sasselov & Scott, astro-ph/9909275v2 eq. 1 and 3 p.3, constants p.4, He I 24.6 eV p.3; "
                     "READ via alphaXiv 2026-10-05"}
REION = {"delta_z": 0.5, "z_He2": 3.5, "delta_z_He2": 0.5,
         "source": "Planck XLVII, arXiv:1605.03507v3 eq. 2 p.5 (tanh in y = (1+z)^1.5, delta y = 1.5 (1+z)^0.5 delta "
                   "z), delta z = 0.5 and He II at z = 3.5 p.5; READ via alphaXiv 2026-10-05.  DISCREPANCY: the "
                   "extracted text reads tanh((y - y_re)/delta y), which would ionise the EARLY universe; the sign "
                   "that gives x_e -> f at low z, (y_re - y), is used -- the same page describes the transition as "
                   "'from an essentially vanishing ionized fraction x_e at early times, to a value of unity at low "
                   "redshifts', and CAMB's reionization.f90 uses (WindowVarMid - (1+z)**Tanh_zexp) (verifier-READ): a "
                   "misprint or extraction artefact in the paper.  A second deviation: the paper evaluates delta y at "
                   "z, the code (as CAMB) at z_re; tau moves 0.05414 -> 0.05426 (verifier-computed)"}
COBE_DT_K = 28e-6           # Hu & Dodelson astro-ph/0110414v1 p.30 eq. 25, 'The observed COBE fluctuation of dT ~ 28
                            # microK (Smoot et al 1992)'; READ via alphaXiv 2026-10-05

E_LYA = H_PL * C / RECFAST["lambda_Lya_m"]
CHI_H = E_LYA * 4.0 / 3.0                         # H-BOHR-LEVELS: E_Lya = (3/4) chi_H; chi_H from the READ lambda
B2 = CHI_H / 4.0                                  # the n = 2 binding energy


# ---------------------------------------------------------------------------------------------------------------------
# (1) the background and the ionisation history
# ---------------------------------------------------------------------------------------------------------------------
def densities():
    h = PLANCK18["H0"] / 100.0
    rho_crit_h2 = 3 * (100e3 / MPC) ** 2 / (8 * math.pi * G_N)
    rho_b = PLANCK18["ombh2"][0] * rho_crit_h2
    rho_g = (math.pi ** 2 / 15) * (KB * T0) ** 4 / (HBAR * C) ** 3 / C ** 2     # kg/m^3
    om_g = rho_g / (rho_crit_h2 * h * h)
    om_r = om_g * (1 + PLANCK18["N_eff"] * (7.0 / 8.0) * (4.0 / 11.0) ** (4.0 / 3.0))      # H-MASSLESS-NU
    y = PLANCK18["Y_P"]
    n_h0 = (1 - y) * rho_b / (MP + ME)
    f_he = y / (4 * (1 - y))                                                    # H-HE-MASS-4
    return {"h": h, "rho_b0": rho_b, "rho_g0": rho_g, "Om_g": om_g, "Om_r": om_r, "Om": PLANCK18["Om"],
            "OL": 1 - PLANCK18["Om"] - om_r, "n_H0": n_h0, "f_He": f_he, "H0": cosmo.H0()}


DEN = densities()


def hubble(z, den=DEN, lam=True):
    zp = 1.0 + z
    ol = den["OL"] if lam else 0.0
    om = den["Om"] if lam else 1.0 - den["Om_r"]
    return den["H0"] * math.sqrt(om * zp ** 3 + den["Om_r"] * zp ** 4 + ol)


def n_h(z):
    return DEN["n_H0"] * (1 + z) ** 3


def _thermal(T):
    return (2 * math.pi * ME * KB * T / H_PL ** 2) ** 1.5


def alpha_b(T):
    t = T / 1e4
    r = RECFAST
    return r["F"] * 1e-19 * r["a"] * t ** r["b"] / (1 + r["c"] * t ** r["d"])


def beta_b(T):
    return alpha_b(T) * _thermal(T) * math.exp(-B2 / (KB * T))


def saha_h(z):
    T = T0 * (1 + z)
    s = _thermal(T) * math.exp(-CHI_H / (KB * T)) / n_h(z)
    return 0.5 * (-s + math.sqrt(s * s + 4 * s))          # x^2/(1-x) = s


def saha_he(z):
    """He I -> He II by Saha (Seager eq. 7, H-HEI-SAHA), with hydrogen fully ionised: electrons from helium per H."""
    T = T0 * (1 + z)
    f = DEN["f_He"]
    s = 4 * _thermal(T) * math.exp(-RECFAST["chi_HeI_eV"] * EV / (KB * T)) / n_h(z)
    # (x - 1) x / (1 + f - x) = s with x = 1 + y, y in [0, f]:  y (1 + y) = s (f - y)
    b = 1 + s
    y = 0.5 * (-b + math.sqrt(b * b + 4 * s * f))
    return y


def _rhs(x, z):
    T = T0 * (1 + z)
    nh = n_h(z)
    hz = hubble(z)
    k = RECFAST["lambda_Lya_m"] ** 3 / (8 * math.pi * hz)
    lam = RECFAST["Lambda_2s"]
    b = beta_b(T)
    cr = (1 + k * lam * nh * (1 - x)) / (1 + k * (lam + b) * nh * (1 - x))
    return (x * x * nh * alpha_b(T) - b * (1 - x) * math.exp(-E_LYA / (KB * T))) * cr / (hz * (1 + z))


_REC_CACHE = {}


Z_START = 2500.0      # above the toy's highest tick (z 2181); first written 1700, which left the toy's ticks above it
                      # with zero record weight (np.interp clamps)


def recombination(z_start=Z_START, dz=0.25, saha_only=False):
    key = (z_start, dz, saha_only)
    if key not in _REC_CACHE:
        _REC_CACHE[key] = _recombination(z_start, dz, saha_only)
    return _REC_CACHE[key]


def _recombination(z_start, dz, saha_only):
    """x_p(z) on a descending grid to z = 0: Saha while x_p >= 0.99, implicit Euler on Seager eq. 1 after.  The control
    (saha_only) keeps Saha throughout -- recombination with no n = 2 bottleneck."""
    zs, xs = [z_start], [saha_h(z_start)]
    ode = False
    n = int(round(z_start / dz))
    for k in range(1, n + 1):
        zn = z_start - k * dz
        x = xs[-1]
        xsaha = saha_h(zn) if zn > 1.0 else 0.0
        if saha_only or (not ode and xsaha >= 0.99):
            xs.append(xsaha)
            zs.append(zn)
            continue
        ode = True
        xn = x
        for _ in range(60):
            g = xn - x + dz * _rhs(xn, zn)
            e = 1e-7 * max(xn, 1e-8)
            dg = 1 + dz * (_rhs(xn + e, zn) - _rhs(xn - e, zn)) / (2 * e)
            step = g / dg
            xn = min(max(xn - step, 1e-12), 1.0)
            if abs(step) < 1e-12 * max(xn, 1e-8):
                break
        xs.append(xn)
        zs.append(zn)
    return np.array(zs), np.array(xs)


def reion_xe(z, z_re=None, delta_z=None):
    z_re = PLANCK18["z_re"][0] if z_re is None else z_re
    dz = REION["delta_z"] if delta_z is None else delta_z
    f = 1 + DEN["f_He"]
    y, yr = (1 + z) ** 1.5, (1 + z_re) ** 1.5
    dy = 1.5 * math.sqrt(1 + z_re) * dz
    h1 = 0.5 * f * (1 + math.tanh((yr - y) / dy))
    y2, yr2 = (1 + z) ** 1.5, (1 + REION["z_He2"]) ** 1.5
    dy2 = 1.5 * math.sqrt(1 + REION["z_He2"]) * REION["delta_z_He2"]
    he2 = 0.5 * DEN["f_He"] * (1 + math.tanh((yr2 - y2) / dy2))
    return h1, he2


def history(saha_only=False, with_he=True, z_re=None, reion=True):
    zs, xp = recombination(saha_only=saha_only)
    xe = []
    for z, x in zip(zs, xp):
        rec = x + (saha_he(z) if with_he else 0.0)
        if not reion:
            xe.append(rec)
            continue
        h1, he2 = reion_xe(z, z_re=z_re)
        xe.append(max(rec, h1) + he2)                  # reionisation matched to the relic fraction (1605.03507 fn 3)
    return zs, xp, np.array(xe)


def optical_depth(zs, xe):
    """tau(z) from 0 up (zs descending in, ascending out): d tau/dz = n_e sigma_T c / ((1+z) H)."""
    za, xa = zs[::-1], xe[::-1]
    dtdz = np.array([x * n_h(z) * SIGMA_T * C / ((1 + z) * hubble(z)) for z, x in zip(za, xa)])
    tau = np.concatenate([[0.0], np.cumsum(0.5 * (dtdz[1:] + dtdz[:-1]) * np.diff(za))])
    return za, xa, dtdz, tau


def _interp_cross(xs, ys, target):
    for i in range(len(ys) - 1):
        if (ys[i] - target) * (ys[i + 1] - target) <= 0 and ys[i] != ys[i + 1]:
            return xs[i] + (target - ys[i]) * (xs[i + 1] - xs[i]) / (ys[i + 1] - ys[i])
    return float("nan")


def age_at(z, lam=True, n=20000):
    """t(z) = int_z^inf dz'/((1+z') H(z')), in ln(1+z')."""
    lo, hi = math.log1p(z), math.log1p(1e8)
    h = (hi - lo) / n
    s = 0.0
    for i in range(n + 1):
        u = lo + i * h
        zz = math.expm1(u)
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w / hubble(zz, lam=lam)
    return s * h / 3


def sound_horizon(z_star, n=20000):
    """r_s = int c_s dz / H from z* to infinity, c_s = c / sqrt(3 (1 + R)), R = 3 rho_b / (4 rho_gamma) (Hu & Sugiyama
    astro-ph/9407093v1 eq. 6, held in medium.ACOUSTIC)."""
    lo, hi = math.log1p(z_star), math.log1p(1e8)
    h = (hi - lo) / n
    s = 0.0
    for i in range(n + 1):
        u = lo + i * h
        zz = math.expm1(u)
        r = 3 * DEN["rho_b0"] / (4 * DEN["rho_g0"] * (1 + zz))
        cs = C / math.sqrt(3 * (1 + r))
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * cs * (1 + zz) / hubble(zz)
    return s * h / 3 / MPC


def records(saha_only=False, with_he=True):
    zs, xp, xe = history(saha_only=saha_only, with_he=with_he)
    za, xa, dtdz, tau = optical_depth(zs, xe)
    g = np.exp(-tau) * dtdz
    # z* as Planck/CAMB define it: tau = 1 with reionisation LEFT OUT (CAMB results.f90 'noreion_optdepth', verifier-
    # READ).  First written with reionisation in tau -- 1085.6, -0.40 %, wrongly put down to the simplifications.
    _, xe_nr = history(saha_only=saha_only, with_he=with_he, reion=False)[1:]
    za_nr, _, _, tau_nr = optical_depth(zs, xe_nr)
    z_tau1 = _interp_cross(za_nr, tau_nr, 1.0)
    z_tau1_total = _interp_cross(za, tau, 1.0)
    i_pk = int(np.argmax(np.where(za > 100, g, 0)))
    half = g[i_pk] / 2
    i100 = int(np.searchsorted(za, 100.0))
    lo = _interp_cross(za[i100:i_pk + 1], g[i100:i_pk + 1], half)
    hi = _interp_cross(za[i_pk:], g[i_pk:], half)
    gam_h = lambda z, x: x * n_h(z) * SIGMA_T * C / hubble(z)
    i30 = int(np.searchsorted(za, 30.0))
    i200 = int(np.searchsorted(za, 200.0))
    tau_re = float(tau[i30])
    reion_total = 1 - math.exp(-tau_re)
    zq = {}
    for q in (0.1, 0.5, 0.9):
        cum = [(1 - math.exp(-t)) / reion_total for t in tau[:i30 + 1]]
        zq[q] = _interp_cross(za[:i30 + 1], cum, q)
    obs = {}
    for zn in (0.0, 30.0, 200.0, 600.0, 900.0):
        j = int(np.searchsorted(za, zn))
        g_o = np.exp(-(tau[j:] - tau[j])) * dtdz[j:]
        obs[str(zn)] = float(za[j:][int(np.argmax(np.where(za[j:] > max(zn, 100), g_o, 0)))])
    out = {"z_tau1": z_tau1, "z_tau1_with_reion": z_tau1_total, "z_peak": float(za[i_pk]), "fwhm": hi - lo,
           "reion_last_record_z_10_50_90": (zq[0.1], zq[0.5], zq[0.9]),
           "reion_last_record_t_myr_10_50_90": tuple(age_at(zq[q]) / YEAR_S / 1e6 for q in (0.1, 0.5, 0.9)),
           "observer_relative_peak_z": obs,
           "z_gamma_eq_H": _interp_cross(za[za > 100], [gam_h(z, x) for z, x in zip(za[za > 100], xa[za > 100])], 1.0),
           "x_e_200": float(xa[i200]), "tau_reion": tau_re,
           "last_record_reion": 1 - math.exp(-tau_re),
           "last_record_recomb": math.exp(-float(tau[i200])) - math.exp(-float(tau[-1])),
           # first written e^-tau(30) - e^-tau_max, which counted the dark ages twice (shares summed to 100.15 %)
           "last_record_dark_ages": math.exp(-tau_re) - math.exp(-float(tau[i200])),
           "records_dark_ages": float(tau[i200] - tau[i30]),
           "tau_max": float(tau[-1])}
    out["gamma_over_H"] = {str(z): gam_h(z, float(np.interp(z, za, xa))) for z in (1500, 1090, 800, 200, 20, 7.67, 0)}
    out["_grid"] = (za, xa, dtdz, tau, g)
    return out


# ---------------------------------------------------------------------------------------------------------------------
# (3) the dynamics, and (4) into the toy
# ---------------------------------------------------------------------------------------------------------------------
def support_growth(rec):
    """The support as it stands at a present z_now: the mean number of records per photon laid down between the grid's
    start (z = 2500) and z_now (ALL-RECORDS), and its growth per e-fold, Gamma/H, at z_now.  First written as tau(z_now)
    -- the records laid down AFTER z_now, the reverse of what was labelled."""
    za, xa, dtdz, tau, g = rec["_grid"]
    rows = []
    for zn in (1500, 1200, 1090, 900, 600, 200, 30, 7.67, 0):
        i = int(np.searchsorted(za, zn))
        rows.append({"z_now": zn, "support_records": float(tau[-1] - tau[i]),
                     "growth_per_efold": rec["gamma_over_H"].get(str(zn), float(np.interp(zn, za, xa)) * n_h(zn)
                                                                 * SIGMA_T * C / hubble(zn))})
    return rows


def toy_weights(rec, ts):
    """Bin the record weightings onto the toy's ticks (H-TOY-BINNING): tick k at T_k <-> z_k = T_k/T0 - 1; bin edges at
    geometric midpoints."""
    za, xa, dtdz, tau, g = rec["_grid"]
    zk = [T / T0 - 1 for T in ts]
    lz = np.log1p(zk)
    edges = np.concatenate([[lz[0] + 0.5 * (lz[0] - lz[1])], 0.5 * (lz[1:] + lz[:-1]), [lz[-1] - 0.5 * (lz[-2] - lz[-1])]])
    ze = np.expm1(edges)
    taue = np.interp(ze, za, tau)
    all_rec = [abs(taue[i] - taue[i + 1]) for i in range(len(ts))]
    last_rec = [abs(math.exp(-taue[i + 1]) - math.exp(-taue[i])) for i in range(len(ts))]
    return all_rec, last_rec


def toy(rec):
    ts, psis = unobserved.history(unobserved.PSI_GROUND)
    all_rec, last_rec = toy_weights(rec, ts)
    static = [1.0 if T > unobserved.T_DEC else 0.0 for T in ts]
    r_static = unobserved.rho_of(psis, static)
    rows = {}
    for name, w in (("ALL-RECORDS", all_rec), ("LAST-RECORD", last_rec)):
        r = unobserved.rho_of(psis, w)
        coupled = sum(wk for wk, T in zip(w, ts) if T > unobserved.T_DEC) / sum(w)
        rows[name] = {"coupled_share": coupled, "purity": unobserved.purity(r),
                      "TD_vs_static_M_SUPPORT": unobserved.trace_distance(r, r_static),
                      "TD_vs_traced": {k: unobserved.trace_distance(r, unobserved.rho_of(
                          psis, unobserved.clock_weights(ts, k))) for k in unobserved.KINDS}}
    # control: on ticks where the coupling is full (x_e > 1 - 1e-8), two very different weightings give the same state
    # (stationarity of the coupled ground state); near T_dec the coupling is already falling, so no such equality holds
    full = [unobserved.x_e(T) > 1 - 1e-8 for T in ts]
    flat = [1.0 if f else 0.0 for f in full]
    uneven = [(k + 1) ** 3 if f else 0.0 for k, f in enumerate(full)]
    rows["control_full_coupling_TD"] = unobserved.trace_distance(unobserved.rho_of(psis, uneven),
                                                                 unobserved.rho_of(psis, flat))
    rows["full_coupling_ticks"] = sum(full)
    # what the agreement does and does not show: M-SUPPORT's own reweighting ambiguity (flat vs cubic over every tick
    # above T_dec); a record-free weighting concentrated above T_dec (T^8); and the Thomson weight WITHOUT recombination
    # (x_e = 1), which shows that what matters is that records stop where the coupling stops
    above = [T > unobserved.T_DEC for T in ts]
    rows["M_SUPPORT_reweighting_ambiguity"] = unobserved.trace_distance(
        unobserved.rho_of(psis, [(k + 1) ** 3 if a else 0.0 for k, a in enumerate(above)]), r_static)
    rows["record_free_T8_TD"] = unobserved.trace_distance(unobserved.rho_of(psis, [T ** 8 for T in ts]), r_static)
    za, xa, dtdz, tau, g = rec["_grid"]
    full = dtdz / xa
    tau_full = np.concatenate([[0.0], np.cumsum(0.5 * (full[1:] + full[:-1]) * np.diff(za))])
    zk = [T / T0 - 1 for T in ts]
    lz = np.log1p(zk)
    edges = np.expm1(np.concatenate([[lz[0] + 0.5 * (lz[0] - lz[1])], 0.5 * (lz[1:] + lz[:-1]),
                                     [lz[-1] - 0.5 * (lz[-2] - lz[-1])]]))
    tf = np.interp(edges, za, tau_full)
    rows["no_recombination_thomson_TD"] = unobserved.trace_distance(
        unobserved.rho_of(psis, [abs(tf[i] - tf[i + 1]) for i in range(len(ts))]), r_static)
    rows["tick_z_range"] = (ts[0] / T0 - 1, ts[-1] / T0 - 1)
    assert ts[0] / T0 - 1 < Z_START, "the record grid must cover the toy's ticks"
    return rows


# ---------------------------------------------------------------------------------------------------------------------
# (5) local clocks at last scattering
# ---------------------------------------------------------------------------------------------------------------------
def local_clocks_at_decoupling(z_star):
    t_star = age_at(z_star)
    dt_over_t = COBE_DT_K / T0              # observed Delta T / T on COBE's scales
    psi = 3 * dt_over_t                     # observed = Psi/3 (Sachs-Wolfe, H-SW-ONLY), so |Psi| = 3 Delta T/T
    zp = 1 + z_star
    rm, rr = DEN["Om"] * zp ** 3, DEN["Om_r"] * zp ** 4
    w = (rr / 3) / (rm + rr)                # the effective equation of state at z* (radiation still 1/4 of matter)
    return {"t_star_yr": t_star / YEAR_S, "dT_over_T": dt_over_t, "Psi": psi,
            "intrinsic_Theta": 2 * psi / 3, "climb_out": psi, "observed": psi / 3,
            "w_eff_z_star": w, "intrinsic_factor_at_w": 2 / (3 * (1 + w)),
            "decoupling_time_offset_rms_yr": psi * t_star / YEAR_S}


def compute():
    rec = records()
    rec_saha = records(saha_only=True)
    rec_nohe = records(with_he=False)
    z_star = PLANCK18["z_star"][0]
    zs, xp, xe11 = history(z_re=11.0)
    tau11 = optical_depth(zs, xe11)
    i30 = int(np.searchsorted(tau11[0], 30.0))
    out = {"inputs": {"sigma_T": SIGMA_T, "chi_H_eV": CHI_H / EV, "B2_eV": B2 / EV, "n_H0": DEN["n_H0"],
                      "f_He": DEN["f_He"], "Om_r": DEN["Om_r"], "OL": DEN["OL"]},
           "records": {k: v for k, v in rec.items() if not k.startswith("_")},
           "control_saha_z_tau1": rec_saha["z_tau1"], "no_helium_z_tau1": rec_nohe["z_tau1"],
           "control_tau_reion_z11": float(tau11[3][i30]),
           "age_gyr": age_at(0.0) / YEAR_S / 1e9, "control_age_no_lambda_gyr": age_at(0.0, lam=False) / YEAR_S / 1e9,
           "r_star_mpc": sound_horizon(z_star), "t_reion_myr": age_at(PLANCK18["z_re"][0]) / YEAR_S / 1e6,
           "growth": support_growth(rec), "toy": toy(rec), "local": local_clocks_at_decoupling(z_star)}
    return out


def report():
    d = compute()
    r, t, lc = d["records"], d["toy"], d["local"]
    print("H-M-SUPPORT's dynamics: the support as matter's records of the light (verified once; seated, ledger.py 8h)\n")
    print("(1) ionisation history (RECFAST hydrogen, Saha He I, Planck tanh reionisation): sigma_T %.5e m^2, chi_H %.3f "
          "eV, n_H0 %.4f m^-3, f_He %.4f" % (d["inputs"]["sigma_T"], d["inputs"]["chi_H_eV"], d["inputs"]["n_H0"],
                                              d["inputs"]["f_He"]))
    print("    z* (tau = 1, reionisation left out, as Planck/CAMB define it) %.2f (Planck %.2f +- %.2f: %+.2f %%, %.1f "
          "sigma); with reionisation in tau %.1f; Saha-only control %.1f; without helium %.2f" % (
              r["z_tau1"], PLANCK18["z_star"][0], PLANCK18["z_star"][1],
              100 * (r["z_tau1"] / PLANCK18["z_star"][0] - 1), abs(r["z_tau1"] - PLANCK18["z_star"][0]) /
              PLANCK18["z_star"][1], r["z_tau1_with_reion"], d["control_saha_z_tau1"], d["no_helium_z_tau1"]))
    print("    age %.3f Gyr (Planck %.3f; no-Lambda control %.2f); sound horizon at Planck's z*: r* %.2f Mpc (Planck %.2f)" % (
        d["age_gyr"], PLANCK18["age_gyr"][0], d["control_age_no_lambda_gyr"], d["r_star_mpc"],
        PLANCK18["r_star_mpc"][0]))
    print("(2) matter's observation of the light: last record peaks at z %.1f, FWHM %.1f; Gamma/H = 1 at z %.1f; "
          "x_e(200) %.2e" % (r["z_peak"], r["fwhm"], r["z_gamma_eq_H"], r["x_e_200"]))
    print("    Gamma/H (records per photon per e-fold): " + ", ".join(
        "z %s: %.3g" % (k, v) for k, v in r["gamma_over_H"].items()))
    print("    reionisation tau %.4f (Planck %.4f +- %.4f; z_re = 11 control %.4f)" % (
        r["tau_reion"], PLANCK18["tau"][0], PLANCK18["tau"][1], d["control_tau_reion_z11"]))
    zq, tq = r["reion_last_record_z_10_50_90"], r["reion_last_record_t_myr_10_50_90"]
    print("    LAST-RECORD: of today's photons, %.4f last recorded at z > 200, %.2e at 30 < z < 200, %.4f at z < 30 -- "
          "since reionisation (midpoint t = %.0f Myr), median z %.2f (t %.0f Myr), 10-90 %% z %.2f-%.2f (t %.0f-%.0f "
          "Myr)" % (r["last_record_recomb"], r["last_record_dark_ages"], r["last_record_reion"], d["t_reion_myr"],
                    zq[1], tq[1], zq[2], zq[0], tq[2], tq[0]))
    print("    observer-relative: the last record's peak for an observer at z_now " + ", ".join(
        "%s: z %.1f" % (k, v) for k, v in r["observer_relative_peak_z"].items()))
    print("    ALL-RECORDS: %.3g records per photon since z = 2500; %.3g in the dark ages" % (r["tau_max"], r["records_dark_ages"]))
    print("(3) the support as it stands at a present z_now (records per photon laid down since z = 2500 | growth per "
          "e-fold):")
    for row in d["growth"]:
        print("    z_now %7.2f   %10.4f | %.3g" % (row["z_now"], row["support_records"], row["growth_per_efold"]))
    print("(4) into the toy (ticks z %.0f -> %.0f, coupled ground start):" % t["tick_z_range"])
    for name in ("ALL-RECORDS", "LAST-RECORD"):
        row = t[name]
        print("    %-12s coupled share %.4f, purity %.4f, TD vs static M-SUPPORT %.3e, vs TRACED %s" % (
            name, row["coupled_share"], row["purity"], row["TD_vs_static_M_SUPPORT"],
            ", ".join("%s %.3f" % (k, v) for k, v in row["TD_vs_traced"].items())))
    print("    control: on the %d fully coupled ticks, flat and cubic weightings give the same state (TD %.1e)" % (
          t["full_coupling_ticks"], t["control_full_coupling_TD"]))
    print("    what the agreement shows: M-SUPPORT's own reweighting ambiguity (flat vs cubic above T_dec) %.1e; a "
          "record-free T^8 weighting %.1e; the Thomson weight WITHOUT recombination (x_e = 1) %.3f" % (
              t["M_SUPPORT_reweighting_ambiguity"], t["record_free_T8_TD"], t["no_recombination_thomson_TD"]))
    print("(5) local clocks at last scattering (Newtonian frame; H-MATTER-ERA, H-SW-ONLY): t* %.0f yr; COBE dT/T %.2e "
          "(an rms amplitude) -> |Psi| %.2e; intrinsic %.2e, climb-out %.2e, observed %.2e; rms offset of local "
          "decoupling %.1f yr; at z* w_eff = %.3f, so the intrinsic factor is %.3f, not 2/3" % (
              lc["t_star_yr"], lc["dT_over_T"], lc["Psi"], lc["intrinsic_Theta"], lc["climb_out"], lc["observed"],
              lc["decoupling_time_offset_rms_yr"], lc["w_eff_z_star"], lc["intrinsic_factor_at_w"]))
    print("(6) today's telescope: a matter record at clock reading T0 = %.4f K -- STRUCTURAL" % T0)


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
    r, t = d["records"], d["toy"]
    zs = PLANCK18["z_star"][0]
    chk("the recombination history puts z* (tau = 1, reionisation left out) at %.2f, within 0.1 %% of Planck's %.2f "
        "(first written with reionisation in tau and 0.5 %%)" % (r["z_tau1"], zs), abs(r["z_tau1"] - zs) / zs < 0.001)
    chk("Saha equilibrium (no n = 2 bottleneck) misses z* by more than 10 %% (%.1f)" % d["control_saha_z_tau1"],
        abs(d["control_saha_z_tau1"] - zs) / zs > 0.10, ctl=True)
    chk("the background reproduces Planck's age (%.3f vs %.3f Gyr, within 0.3 %%) and r* (%.2f vs %.2f Mpc, within 1 %%)"
        % (d["age_gyr"], PLANCK18["age_gyr"][0], d["r_star_mpc"], PLANCK18["r_star_mpc"][0]),
        abs(d["age_gyr"] / PLANCK18["age_gyr"][0] - 1) < 0.003 and abs(d["r_star_mpc"] / PLANCK18["r_star_mpc"][0] - 1)
        < 0.01)
    chk("without Lambda the age misses by more than 20 %% (%.2f Gyr)" % d["control_age_no_lambda_gyr"],
        abs(d["control_age_no_lambda_gyr"] / PLANCK18["age_gyr"][0] - 1) > 0.2, ctl=True)
    chk("Planck's tanh model at z_re 7.67 reproduces Planck's tau to 0.001 (%.4f vs %.4f; first written 1 sigma)" % (
        r["tau_reion"], PLANCK18["tau"][0]), abs(r["tau_reion"] - PLANCK18["tau"][0]) < 0.001)
    chk("reionisation at z_re = 11 misses Planck's tau by more than 3 sigma (%.4f)" % d["control_tau_reion_z11"],
        abs(d["control_tau_reion_z11"] - PLANCK18["tau"][0]) > 3 * PLANCK18["tau"][1], ctl=True)
    chk("stationarity: on the fully coupled ticks the weighting does not matter (flat vs cubic, TD %.1e < 1e-6)" %
        t["control_full_coupling_TD"], t["control_full_coupling_TD"] < 1e-6, ctl=True)
    chk("ALL-RECORDS (%.1e) and a record-free T^8 weighting (%.1e) both lie within M-SUPPORT's own reweighting "
        "ambiguity (%.1e): the agreement is not specific to records" % (
            t["ALL-RECORDS"]["TD_vs_static_M_SUPPORT"], t["record_free_T8_TD"], t["M_SUPPORT_reweighting_ambiguity"]),
        max(t["ALL-RECORDS"]["TD_vs_static_M_SUPPORT"], t["record_free_T8_TD"]) < t["M_SUPPORT_reweighting_ambiguity"])
    chk("the Thomson weight WITHOUT recombination (x_e = 1) departs by more than 10x that ambiguity (%.3f): what the "
        "agreement shows is that records stop where the coupling stops" % t["no_recombination_thomson_TD"],
        t["no_recombination_thomson_TD"] > 10 * t["M_SUPPORT_reweighting_ambiguity"], ctl=True)
    structural.append("the growth law d(support)/d ln a = Gamma/H is the Thomson rate per e-fold BY DEFINITION; that "
                      "it is M-SUPPORT's dynamics is H-SUPPORT-IS-RECORDS")
    structural.append("the local-clock reading of the Sachs-Wolfe effect is the Newtonian frame's; in the fluid's rest "
                      "frame 'The intrinsic term is negligible' and proper time coincides with coordinate time (White & Hu p.1); "
                      "decoupling is a surface of constant local temperature in every frame; the observed Psi/3 is the "
                      "same in both")
    structural.append("a telescope's detection is a matter record; its conscious reading is a perception of it "
                      "(Page, gr-qc/9507024v1 pp.1-4, localclock.py)")
    for s in structural:
        print("  STRUCTURAL: " + s)
    print("support.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
