#!/usr/bin/env python3
"""
support.py -- H-M-SUPPORT's dynamics: how observation extends the clock's support, read with H-LOCAL-CLOCK.

Not seated; not yet verified.  M (rulings item 54): "3, then 2, then 1 please" -- M-SUPPORT's dynamics first.  M-SUPPORT
(unobserved.py) is M's stronger reading of item 48 as a computable rule: the clock's support is the coupled epochs, and
observation extends it through records.  Item 52 (H-LOCAL-CLOCK) is carried as M's answer to its open dynamics: "The
clock is relative to the matter-based observation".  Carried as M's hypotheses, never as results.

    python3 support.py              report
    python3 support.py --selftest   checks, with CONTROLS
    python3 support.py --json       the numbers as JSON

THE READING (H-SUPPORT-IS-RECORDS)
  Matter observes the photons by scattering them: every Thomson scattering leaves a record in an electron's momentum.
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
      clock-rate offset, a temporal shift delta t/t = Psi (Hu & Dodelson astro-ph/0110414v1 p.7; White & Hu
      astro-ph/9609105v1 p.1 eq. 3 'in a gravitational potential clocks run slow'); each place decouples at the same
      LOCAL reading, at a shifted time; that gives an intrinsic Theta = -2 Psi/3 (matter era, eq. 13 p.8), the climb out
      gives Psi, the observed sum is Psi/3 (Sachs-Wolfe).  COBE's 28 microK (Hu & Dodelson p.30, citing Smoot et al.
      1992) sets the size; the time spread of local decoupling is computed.  The time-shift picture is a FRAME choice:
      in the fluid's rest frame 'proper time coincides with coordinate time' and the intrinsic term vanishes (White & Hu
      p.1); the observed Psi/3 is the same in both.  STRUCTURAL on that point.
  (6) Today's observation: a telescope's detection is one more matter record, at clock reading T0 = 2.7255 K; its
      content is the photon's state since its last record.  A conscious reading of it is a perception of that record
      (Page; localclock.py).  STRUCTURAL.

NAMED HYPOTHESES
  H-SUPPORT-IS-RECORDS, H-RECFAST-H, H-HEI-SAHA, H-TM-EQUALS-TR, H-REION-TANH, H-HE-MASS-4, H-MASSLESS-NU, H-BOHR-LEVELS,
  H-TOY-BINNING; with H-TOY-MEDIUM, H-CLOCK-WEIGHT (unobserved.py) and M's H-UNOBSERVED-MEDIUM, H-M-SUPPORT (as M's rule)
  and H-LOCAL-CLOCK.
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
                   "that gives x_e -> f at low z, (y_re - y), is used"}
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


def history(saha_only=False, with_he=True, z_re=None):
    zs, xp = recombination(saha_only=saha_only)
    xe = []
    for z, x in zip(zs, xp):
        h1, he2 = reion_xe(z, z_re=z_re)
        rec = x + (saha_he(z) if with_he else 0.0)
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
    z_tau1 = _interp_cross(za, tau, 1.0)
    i_pk = int(np.argmax(np.where(za > 100, g, 0)))
    half = g[i_pk] / 2
    i100 = int(np.searchsorted(za, 100.0))
    lo = _interp_cross(za[i100:i_pk + 1], g[i100:i_pk + 1], half)
    hi = _interp_cross(za[i_pk:], g[i_pk:], half)
    gam_h = lambda z, x: x * n_h(z) * SIGMA_T * C / hubble(z)
    i30 = int(np.searchsorted(za, 30.0))
    i200 = int(np.searchsorted(za, 200.0))
    tau_re = float(tau[i30])
    out = {"z_tau1": z_tau1, "z_peak": float(za[i_pk]), "fwhm": hi - lo,
           "z_gamma_eq_H": _interp_cross(za[za > 100], [gam_h(z, x) for z, x in zip(za[za > 100], xa[za > 100])], 1.0),
           "x_e_200": float(xa[i200]), "tau_reion": tau_re,
           "last_record_reion": 1 - math.exp(-tau_re),
           "last_record_recomb": math.exp(-tau_re) - math.exp(-float(tau[-1])),
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
    rows["tick_z_range"] = (ts[0] / T0 - 1, ts[-1] / T0 - 1)
    assert ts[0] / T0 - 1 < Z_START, "the record grid must cover the toy's ticks"
    return rows


# ---------------------------------------------------------------------------------------------------------------------
# (5) local clocks at last scattering
# ---------------------------------------------------------------------------------------------------------------------
def local_clocks_at_decoupling(z_star):
    t_star = age_at(z_star)
    dt_over_t = COBE_DT_K / T0              # observed Delta T / T on COBE's scales
    psi = 3 * dt_over_t                     # observed = Psi/3 (Sachs-Wolfe), so |Psi| = 3 Delta T/T
    return {"t_star_yr": t_star / YEAR_S, "dT_over_T": dt_over_t, "Psi": psi,
            "intrinsic_Theta": 2 * psi / 3, "climb_out": psi, "observed": psi / 3,
            "decoupling_time_spread_yr": psi * t_star / YEAR_S}


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
    print("H-M-SUPPORT's dynamics: the support as matter's records of the light (not verified; not seated)\n")
    print("(1) ionisation history (RECFAST hydrogen, Saha He I, Planck tanh reionisation): sigma_T %.5e m^2, chi_H %.3f "
          "eV, n_H0 %.4f m^-3, f_He %.4f" % (d["inputs"]["sigma_T"], d["inputs"]["chi_H_eV"], d["inputs"]["n_H0"],
                                              d["inputs"]["f_He"]))
    print("    tau = 1 at z %.1f (Planck z* %.2f); Saha-only control %.1f; without helium %.1f" % (
        r["z_tau1"], PLANCK18["z_star"][0], d["control_saha_z_tau1"], d["no_helium_z_tau1"]))
    print("    age %.3f Gyr (Planck %.3f; no-Lambda control %.2f); sound horizon r* %.2f Mpc (Planck %.2f)" % (
        d["age_gyr"], PLANCK18["age_gyr"][0], d["control_age_no_lambda_gyr"], d["r_star_mpc"],
        PLANCK18["r_star_mpc"][0]))
    print("(2) matter's observation of the light: last record peaks at z %.1f, FWHM %.1f; Gamma/H = 1 at z %.1f; "
          "x_e(200) %.2e" % (r["z_peak"], r["fwhm"], r["z_gamma_eq_H"], r["x_e_200"]))
    print("    Gamma/H (records per photon per e-fold): " + ", ".join(
        "z %s: %.3g" % (k, v) for k, v in r["gamma_over_H"].items()))
    print("    reionisation tau %.4f (Planck %.4f +- %.4f; z_re = 11 control %.4f)" % (
        r["tau_reion"], PLANCK18["tau"][0], PLANCK18["tau"][1], d["control_tau_reion_z11"]))
    print("    LAST-RECORD: of today's photons, %.4f last recorded at recombination, %.4f at reionisation (t = %.0f Myr), %.2e in "
          "the dark ages (30 < z < 200)" % (r["last_record_recomb"], r["last_record_reion"], d["t_reion_myr"],
                                            r["last_record_dark_ages"]))
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
    print("(5) local clocks at last scattering: t* %.0f yr; COBE dT/T %.2e -> |Psi| %.2e; intrinsic %.2e, climb-out "
          "%.2e, observed %.2e; local decoupling spread over %.1f yr" % (
              lc["t_star_yr"], lc["dT_over_T"], lc["Psi"], lc["intrinsic_Theta"], lc["climb_out"], lc["observed"],
              lc["decoupling_time_spread_yr"]))
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
    chk("the recombination history puts tau = 1 at z %.1f, within 0.5 %% of Planck's z* %.2f" % (r["z_tau1"], zs),
        abs(r["z_tau1"] - zs) / zs < 0.005)
    chk("Saha equilibrium (no n = 2 bottleneck) misses z* by more than 10 %% (%.1f)" % d["control_saha_z_tau1"],
        abs(d["control_saha_z_tau1"] - zs) / zs > 0.10, ctl=True)
    chk("the background reproduces Planck's age (%.3f vs %.3f Gyr, within 0.3 %%) and r* (%.2f vs %.2f Mpc, within 1 %%)"
        % (d["age_gyr"], PLANCK18["age_gyr"][0], d["r_star_mpc"], PLANCK18["r_star_mpc"][0]),
        abs(d["age_gyr"] / PLANCK18["age_gyr"][0] - 1) < 0.003 and abs(d["r_star_mpc"] / PLANCK18["r_star_mpc"][0] - 1)
        < 0.01)
    chk("without Lambda the age misses by more than 20 %% (%.2f Gyr)" % d["control_age_no_lambda_gyr"],
        abs(d["control_age_no_lambda_gyr"] / PLANCK18["age_gyr"][0] - 1) > 0.2, ctl=True)
    chk("Planck's tanh model at z_re 7.67 reproduces Planck's tau within 1 sigma (%.4f vs %.4f +- %.4f)" % (
        r["tau_reion"], PLANCK18["tau"][0], PLANCK18["tau"][1]),
        abs(r["tau_reion"] - PLANCK18["tau"][0]) < PLANCK18["tau"][1])
    chk("reionisation at z_re = 11 misses Planck's tau by more than 3 sigma (%.4f)" % d["control_tau_reion_z11"],
        abs(d["control_tau_reion_z11"] - PLANCK18["tau"][0]) > 3 * PLANCK18["tau"][1], ctl=True)
    chk("stationarity: on the fully coupled ticks the weighting does not matter (flat vs cubic, TD %.1e < 1e-6)" %
        t["control_full_coupling_TD"], t["control_full_coupling_TD"] < 1e-6, ctl=True)
    structural.append("the growth law d(support)/d ln a = Gamma/H is the Thomson rate per e-fold BY DEFINITION; that "
                      "it is M-SUPPORT's dynamics is H-SUPPORT-IS-RECORDS")
    structural.append("the local-clock reading of the Sachs-Wolfe effect is the Newtonian frame's; in the fluid's rest "
                      "frame the intrinsic term vanishes and the observed Psi/3 is unchanged (White & Hu p.1)")
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
