#!/usr/bin/env python3
"""sim1_transition.py -- B4d simulation, phase 1 (M-RULINGS item 167): a transition in one spacetime, as the board reads
it.  Computed, READ and deduced; verified once (findings applied, SIM1-TRANSITION.md History); not seated.  First headed
"... not verified; not seated" -- and first claiming the collapse endpoint as computed, one number as deciding every
inflow, and the ordering of outcomes as M's hierarchy of trajectories, none of which its verifiers let stand.

M's words (verbatim in the rulings file): item 167 "... Run it in phases. Start small, a transition in the same spacetime.
Then build on it, with independent directions one at a time. This incidently will also likely give you a hierarchy of
trajectories I would think. ..." (cut marked; the full text is item 167).  Items 115 (c) and 136 G (the README is the
inflow, and the energy); 162 (fixed size, H-FIXED-SIZE); 163 ("All together, one whole"); 157 (our universe).

The board's reading (H-PHASE1-IS-4D, offered for correction): one four-dimensional spacetime, no bulk, spherical
symmetry, directions (t, r); the start flat (H-FLAT-START, the board's gloss on 157's "our current universe"); the
README's energy carried in by a massless scalar field (H-SCALAR-CARRIER), one initial-data family (H-GAUSSIAN-FAMILY).
M's own usage points to another reading (items 116 (b), 117: "travel between two positions within one universe vs
travel between two counterfactual universes"; 118: law and history trajectories): that was put to M, and M chose it
(item 168: "My sense: positions, one universe") -- so H-PHASE1-IS-4D is withdrawn as a reading of M's words, and this
phase stands as the validated time-evolution tool the later phases build on (H-PHASES-BY-TRAJECTORY: phase 2 is the
corridor between two positions within one universe, through the extra dimension).

THE SIMULATION.  Polar-areal coordinates, G = 1, G_ab = 8 pi T_ab: the evolution eqs. (21)-(22), Hamiltonian constraint
  (23), slicing (24) and momentum constraint (25) of Gundlach & Martin-Garcia, arXiv:0711.4620, p.13 (READ); the lapse
  normalised alpha a = 1 at the outer boundary (Olabarrieta et al., arXiv:0708.0513, eq. (27), p.3, READ), which only
  relabels t.  The Hamiltonian constraint is solved each step from its closed integral form (1/a^2 by an integrating
  factor) by trapezoidal quadrature, second order; second-order differences, RK4, fourth-order Kreiss-Oliger
  dissipation, outgoing condition at r = 50.  Initial data: phi = p exp(-((r - 20)/3)^2), ingoing (Pi = Phi + phi/r).
  The momentum constraint is never imposed and is the check.  Polar-areal slicing cannot follow a black hole (it does
  not penetrate apparent horizons, 0708.0513 p.3, READ): every collapsing run is read at 2m/r = 0.95 (H-READOUT-095) and
  stopped; past that the hole drains away numerically (its verifier's continuation).

  S1 CONTROLS, BELOW THRESHOLD (computed; each can fail -- a mutation test by its verifier broke them).  Flat space
     (p = 1e-6) against the exact [f(t + r) - f(t - r)]/r: errors fall 4.2x and 4.0x per halving (t = 20, 40).  Strong
     field (p = 0.8 p*): convergence factor 3.99; the unimposed momentum constraint's residual 1.6e-3, 4.1e-4, 1.0e-4 of
     its scale at dr = 0.04, 0.02, 0.01; total mass conserved to 1.7e-5 on the finest grid.  Near threshold the code is
     checked only by the two-grid masses and by gamma (S2); the echoing period is not measured.
  S2 THE THRESHOLD AND THE MASS SCALING (computed; READ comparison).  Robust outcomes (classify): collapse when 2m/r
     reaches 0.95 at a radius >= 20 dr; dispersal only when the total mass is conserved and the centre empties.  At
     dr = 0.005: 0.01686, 0.01687, 0.016875 disperse, 0.016885 collapses (0.01688 crosses 0.8 at a few grid points and
     then drains -- a floor event, undecided); an independent fourth-order code (sim1_repro.json) puts p* = 0.01688 to
     four figures.  The masses at the 0.95 readout, 0.059-0.44, on the finest grid: a plain power law fixes gamma only
     with p*, from 0.42 at p* = 0.016875 to 0.24 at the bracket's top (best fit 0.40 at 0.016878); with the known wiggle of
     period Delta/(2 gamma) = 4.61 in ln(p - p*) (gr-qc/9604019 p.13, READ) fitted in, gamma = 0.371 at p* = 0.016881
     with a residual ten times smaller -- against READ gamma = 0.374 +- 0.001 (gr-qc/9604019, abstract p.1).  The two
     finest grids agree on the 0.8-readout masses to 0.35%; the 0.95-readout masses differ by 0-6% between dr = 0.01 and
     0.005 (both banked), the readout itself jumping between echoes in places.
  S3 WHAT THE OUTCOME DEPENDS ON (computed within the family; deduced beyond it).  The theory has no scale, so within a
     family of fixed shape one number decides: dispersal below the threshold, collapse above it with M ~ (p - p*)^gamma,
     one critical member between (an ordering of solutions -- the board's analogy, H-HIERARCHY-IS-OUTCOME-ORDER, not
     M's trajectories).  Across shapes it is not one number: a supercritical burst followed by a tail of any length
     still collapses (domain of dependence).  For a long write the deciding quantity is the inflow rate: at threshold
     this family carries its mass M_ADM = 0.59 in a duration ~ 2 delta, a rate ~ M/(2 delta) ~ 0.1 per mass unit.  The
     README's energy spread evenly over the write -- >= 2.0e5 clocks, o3_write.py W3's gas bound at the example README
     (computed there), carried in the option of item 163 -- is a rate ~ 5e-6, 2e4 times below: in this family that is
     p ~ 1.2e-4, deep in the computed dispersing range.  So such a write disperses (deduced for evenly spread writes);
     a write with any stretch above ~0.1 m per clock collapses, and is then held by a hole that grows.
  S3b A HORIZON OF FIXED SIZE ABSORBS NOTHING IN ONE SPACETIME (deduced; Raychaudhuri, standard, not READ).  Along a
     horizon's generators d theta/d lambda = -theta^2/2 - sigma^2 - R_kk; a horizon of fixed size (162) has theta = 0
     throughout, so R_kk = -sigma^2 <= 0, and with matter obeying the null energy condition R_kk = 0 = sigma: no flux
     crosses it.  Stage 5 F1's dm/dv = 0 at r = 2m is the same statement.  So in one spacetime the README cannot be
     carried into a horizon that keeps its size; the negative R_kk that would let it is S4's.
  S4 EQ. (17) IS OUT OF REACH OF ONE SPACETIME (computed; STRUCTURAL; partly a restatement of opening.py O3).  For any
     static -F dt^2 + dr^2/H: radial R_kk = (H/r) d ln(F/H)/dr (exact), so the null energy condition is F/H
     non-decreasing.  Eq. (17): d ln(F/H)/dr = -m/((2r - 3m)(r - 2m)) < 0, F/H falling from infinity at the horizon --
     and its zero surface gravity comes exactly from F/H -> infinity there.  So no static end state reached with matter
     obeying the condition is eq. (17), or close to it in F/H.  Pointwise: a scalar's R_kk = 8 pi (k.d phi)^2 >= 0, eq.
     (17)'s radial R_kk = -2m(r - 2m)/(r^2 (2r - 3m)^2) < 0, the shortfall largest (0.0443/m^2) at r = 2.295m.  The
     collapse end state, Schwarzschild outside (non-extremal), is Birkhoff's (standard, not READ; not computed here).
  S5 WHAT THE NEXT DIRECTION MUST SUPPLY (computed).  Read as an effective fluid on the plane, eq. (17)'s Weyl term has
     rho = m^2/(8 pi r^2 (2r - 3m)^2) > 0 (integrating to m/4 outside 2m -- ledger.py E4's 5m/4 - m, the control),
     p_r = -m/(8 pi r^2 (2r - 3m)) and p_t = m(r - m)/(8 pi r^2 (2r - 3m)^2): radial rho + p_r < 0, tangential rho + p_t > 0.
     It is anisotropic.  A Weyl term uniform along the plane is isotropic (dark radiation), so a plane-uniform phase 2
     cannot carry it; the bulk must supply an anisotropic, radially null-energy-breaking Weyl stress, along a trajectory
     that also holds the README.
  OUTSIDE THE BOARD (READ, sim_reads.json).  Eq. (17) is Casadio-Fabbri-Mazzacurati's Case I at its zero-temperature
     member (deduced from their READ eqs. (8) and (13), gr-qc/0111072 p.2); they call it "completely regular" and leave
     its bulk open (p.4).  For a different brane metric (tidal Reissner-Nordstrom, F = H, which excludes eq. (17)),
     Chamblin-Reall-Shinkai-Shiromizu (hep-th/0008177 p.7) found "the trace of the extrinsic curvature diverges at a
     finite distance from the brane" -- an analogue of stage 5 F2 (deduced).  Casadio-Mazzacurati (gr-qc/0205129 p.9,
     qualitative only at eq. (17)'s eta = 3/4) find the area growing into the bulk for eta > 0, "as one would indeed
     expect on a negative tension brane", and caustics: Gaussian coordinates that do not cover the bulk -- a caution on
     the chart stage 5 used, not a check of F6.  Wang-Choptuik (PRL 117, 011102; arXiv:1604.04832 pp.1-3) evolved
     collapse on an RS2 brane in (t, r, y): generalized-harmonic, the brane's constraints as boundary conditions, a hole
     of finite extent settling to an "apparently stationary" state -- though "the evolution inevitably departs from this
     configuration" (p.3).
  VERDICT (deduced).  Phase 1 gives a validated time-evolution tool and three statements about one spacetime: an evenly
     spread README write disperses; a horizon that keeps its size absorbs nothing; and eq. (17) cannot be an end state.
     All three point at the extra dimension, which must supply an anisotropic Weyl stress (S5).  Whether the next phase
     is the board's (y added, the plane uniform) or M's (two positions within one universe) is put to M.

Banked: sim1_bank.json (about 45 min to regenerate).  Needs numpy, sympy.
python3 sim1_transition.py [--selftest] [--regenerate]   (selftest about 1 min)
"""
import json
import math
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "sim1_bank.json")
R0, DELTA, ROUT = 20.0, 3.0, 50.0
P_STAR = 0.016878                       # fitted in S2 at dr = 0.005 (0.95 readout); bracketed by the banked runs
GAMMA_READ = 0.374                      # Gundlach, gr-qc/9604019, abstract p.1 (READ); the Living Review gives only ~0.37, p.19
WIGGLE_READ = 4.61                      # Delta/(2 gamma), the wiggle's period in ln(p - p*): gr-qc/9604019 p.13 (READ)
BRACKET = (0.016875, 0.016885)          # robust bracket at dr = 0.005 (classify): 0.016875 disperses, 0.016885 collapses
P_LIST = [0.01690, 0.01692, 0.01695, 0.01700, 0.01710, 0.01730, 0.01760, 0.01800, 0.01900, 0.02000, 0.02200]


# ------------------------------------------------------------------------------------------------ the simulation
def _cumtrapz(y, dx):
    c = np.empty_like(y)
    c[0] = 0.0
    c[1:] = np.cumsum(0.5 * (y[1:] + y[:-1])) * dx
    return c


def metric(Phi, Pi, r, dr):
    """The Hamiltonian constraint exactly: A = 1/a^2 solves A' + (1/r + 4 pi r S) A = 1/r, A(0) = 1, so
    A(r) = (1/(r E(r))) int_0^r E, E = exp(int 4 pi s S); then the slicing for alpha, alpha a = 1 at r = R."""
    S = Pi**2 + Phi**2
    L = _cumtrapz(4 * math.pi * r * S, dr)
    I = _cumtrapz(np.exp(L - L[-1]), dr)
    A = np.empty_like(r)
    A[0] = 1.0
    A[1:] = I[1:] * np.exp(L[-1] - L[1:]) / r[1:]
    a = 1 / np.sqrt(A)
    g = np.zeros_like(r)
    g[1:] = (a[1:]**2 - 1) / r[1:]
    J = _cumtrapz(g, dr)
    alpha = a * np.exp(J - J[-1]) / a[-1]**2
    return a, alpha, A


def rhs(Phi, Pi, r, dr, dt, eps=0.5):
    a, al, A = metric(Phi, Pi, r, dr)
    X, Y = al * Phi / a, al * Pi / a
    dPhi, dPi = np.zeros_like(Phi), np.zeros_like(Pi)
    dPhi[1:-1] = (Y[2:] - Y[:-2]) / (2 * dr)
    r2X, r3 = r**2 * X, r**3
    dPi[1:-1] = 3 * (r2X[2:] - r2X[:-2]) / (r3[2:] - r3[:-2])
    dPi[0] = 3 * X[1] / r[1]
    c = al[-1] / a[-1]
    for u, du in ((Phi, dPhi), (Pi, dPi)):
        du[-1] = -c * ((3 * u[-1] - 4 * u[-2] + u[-3]) / (2 * dr) + u[-1] / r[-1])
    for u, du, par in ((Phi, dPhi, -1), (Pi, dPi, 1)):                 # Phi odd, Pi even at r = 0
        ue = np.concatenate(([par * u[2], par * u[1]], u))
        d4 = ue[4:] - 4 * ue[3:-1] + 6 * ue[2:-2] - 4 * ue[1:-3] + ue[:-4]
        du[:-2] -= eps / (16 * dt) * d4[:len(du) - 2]
    return dPhi, dPi, a, al


def init(p, r):
    phi = p * np.exp(-((r - R0) / DELTA) ** 2)
    Phi = phi * (-2 * (r - R0) / DELTA**2)
    Pi = np.zeros_like(r)
    Pi[1:] = Phi[1:] + phi[1:] / r[1:]
    return Phi, Pi


def grid(dr):
    N = int(round(ROUT / dr))
    return np.arange(N + 1) * dr


def step(Phi, Pi, r, dr, dt):
    k1 = rhs(Phi, Pi, r, dr, dt)
    k2 = rhs(Phi + 0.5 * dt * k1[0], Pi + 0.5 * dt * k1[1], r, dr, dt)
    k3 = rhs(Phi + 0.5 * dt * k2[0], Pi + 0.5 * dt * k2[1], r, dr, dt)
    k4 = rhs(Phi + dt * k3[0], Pi + dt * k3[1], r, dr, dt)
    return (Phi + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
            Pi + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]), k1, k4)


def m_adm(p, dr=0.01):
    r = grid(dr)
    Phi, Pi = init(p, r)
    _, _, A = metric(Phi, Pi, r, dr)
    return r[-1] / 2 * (1 - A[-1])


def collapse_mass(p, dr, T=90.0, lam=0.25, thr=0.8):
    """Evolve; the mass when 2m/r first reaches thr (peak interpolated in r and t), or None if it never does (the
    run's peak 2m/r returned instead)."""
    r = grid(dr)
    dt = lam * dr
    Phi, Pi = init(p, r)
    t, peak, prev = 0.0, 0.0, None
    for _ in range(int(round(T / dt))):
        Phi, Pi, _, k4 = step(Phi, Pi, r, dr, dt)
        t += dt
        a = k4[2]
        c = np.zeros_like(r)
        c[1:] = 1 - 1 / a[1:] ** 2
        j = int(np.argmax(c))
        if 1 <= j < len(r) - 1:
            y0, y1, y2 = c[j - 1], c[j], c[j + 1]
            den = y0 - 2 * y1 + y2
            s = 0.5 * (y0 - y2) / den if den != 0 else 0.0
            cpk, rpk = y1 - 0.25 * (y0 - y2) * s, r[j] + s * dr
        else:
            cpk, rpk = c[j], r[j]
        if cpk >= thr:
            if prev is not None and prev[0] < thr:
                rpk = prev[1] + (thr - prev[0]) / (cpk - prev[0]) * (rpk - prev[1])
            return {"collapse": True, "M": rpk * thr / 2, "t": t}
        prev = (cpk, rpk)
        peak = max(peak, cpk)
    return {"collapse": False, "peak": peak}


def collapse_masses(p, dr, thrs=(0.8, 0.9, 0.95), T=150.0, lam=0.25):
    """As collapse_mass, recording the mass at each threshold crossing (peak interpolated in r and t)."""
    r = grid(dr)
    dt = lam * dr
    Phi, Pi = init(p, r)
    t, peak, prev, out = 0.0, 0.0, None, {}
    for _ in range(int(round(T / dt))):
        Phi, Pi, _, k4 = step(Phi, Pi, r, dr, dt)
        t += dt
        a = k4[2]
        c = np.zeros_like(r)
        c[1:] = 1 - 1 / a[1:] ** 2
        j = int(np.argmax(c))
        if 1 <= j < len(r) - 1:
            y0, y1, y2 = c[j - 1], c[j], c[j + 1]
            den = y0 - 2 * y1 + y2
            s = 0.5 * (y0 - y2) / den if den != 0 else 0.0
            cpk, rpk = y1 - 0.25 * (y0 - y2) * s, r[j] + s * dr
        else:
            cpk, rpk = c[j], r[j]
        for th in thrs:
            if th not in out and cpk >= th:
                rr = rpk
                if prev is not None and prev[0] < th:
                    rr = prev[1] + (th - prev[0]) / (cpk - prev[0]) * (rpk - prev[1])
                out[th] = {"M": rr * th / 2, "t": t}
        if len(out) == len(thrs):
            break
        prev = (cpk, rpk)
        peak = max(peak, cpk)
    return {"collapse": 0.8 in out or (thrs[0] in out), "masses": {str(k): v for k, v in out.items()}, "peak": peak}


def classify(p, dr, T=65.0, lam=0.25):
    """Robust outcome (its verifier's criterion).  COLLAPSE: 2m/r reaches 0.95 at a radius >= 20 dr.  DISPERSE: the
    total mass m(R) is conserved to 1e-3 to T, and at T m(r < 10) < 1e-3 m(R) and alpha(0) > 0.9 -- observed, not
    inferred from a low peak (a hole the slicing cannot hold drains away and takes m(R) with it).  Else FLOOR."""
    r = grid(dr)
    dt = lam * dr
    Phi, Pi = init(p, r)
    i10 = int(round(10 / dr))
    _, _, A0 = metric(Phi, Pi, r, dr)
    mR0 = r[-1] / 2 * (1 - A0[-1])
    t, peak, drift = 0.0, 0.0, 0.0
    for _ in range(int(round(T / dt))):
        Phi, Pi, _, k4 = step(Phi, Pi, r, dr, dt)
        t += dt
        a = k4[2]
        c = np.zeros_like(r)
        c[1:] = 1 - 1 / a[1:] ** 2
        j = int(np.argmax(c))
        peak = max(peak, c[j])
        if c[j] >= 0.95 and r[j] >= 20 * dr:
            return {"outcome": "collapse", "t": t, "r": float(r[j]), "peak": float(c[j])}
        mR = r[-1] / 2 * (1 - 1 / a[-1] ** 2)
        drift = max(drift, abs(mR / mR0 - 1))
    a, al, A = metric(Phi, Pi, r, dr)
    m10 = r[i10] / 2 * (1 - A[i10])
    ok = drift < 1e-3 and m10 < 1e-3 * mR0 and al[0] > 0.9
    return {"outcome": "disperse" if ok else "floor", "peak": float(peak), "drift": float(drift),
            "m10_over_mR": float(m10 / mR0), "alpha0": float(al[0])}


# ------------------------------------------------------------------------------------------------ S1 controls
def flat_exact(t, r, p):
    f = lambda x: x * p * np.exp(-((x - R0) / DELTA) ** 2)
    fp = lambda x: p * np.exp(-((x - R0) / DELTA) ** 2) * (1 - 2 * x * (x - R0) / DELTA**2)
    u, v = t + r, t - r
    return (fp(u) + fp(v)) / r - (f(u) - f(v)) / r**2, (fp(u) - fp(v)) / r


def flat_control(drs=(0.04, 0.02), ts=(20.0, 40.0), p=1e-6):
    out = {}
    for dr in drs:
        r = grid(dr)
        dt = 0.25 * dr
        Phi, Pi = init(p, r)
        t, errs = 0.0, {}
        for _ in range(int(round(max(ts) / dt))):
            Phi, Pi, _, _ = step(Phi, Pi, r, dr, dt)
            t += dt
            for T in ts:
                if abs(t - T) < dt / 2:
                    m = (r > 0.5) & (r < 45)
                    ePhi, ePi = flat_exact(T, r[m], p)
                    errs[T] = float(np.max(np.abs(Pi[m] - ePi)) / np.max(np.abs(ePi)))
        out[dr] = errs
    return out


def strong_control(p=0.8 * P_STAR, drs=(0.04, 0.02, 0.01), T=30.0, t_mom=25.0):
    """Three resolutions at p = 0.8 p*: convergence factor of Pi at T, the unimposed momentum constraint's rms residual
    at t_mom, and the drift of the total mass m(R) up to T."""
    res = {}
    for dr in drs:
        r = grid(dr)
        dt = 0.25 * dr
        Phi, Pi = init(p, r)
        t, mom, masses = 0.0, None, []
        for n in range(int(round(T / dt))):
            Phib, Pib = Phi, Pi
            Phi, Pi, k1, _ = step(Phi, Pi, r, dr, dt)
            t += dt
            if mom is None and t >= t_mom:
                a1, al1, _ = metric(Phi, Pi, r, dr)
                adot = (a1 - k1[2]) / dt
                src = 4 * math.pi * r * 0.5 * (al1 + k1[3]) * 0.5 * (Phi + Phib) * 0.5 * (Pi + Pib)
                m = (r > 0.2) & (r < 40)
                mom = (float(np.sqrt(np.mean((adot - src)[m] ** 2))), float(np.sqrt(np.mean(src[m] ** 2))))
            if n % int(round(1 / dt)) == 0:
                _, _, A = metric(Phi, Pi, r, dr)
                masses.append(r[-1] / 2 * (1 - A[-1]))
        res[dr] = {"Pi": Pi, "Phi": Phi, "mom": mom, "drift": float(np.max(np.abs(np.array(masses) - masses[0])) / masses[0])}
    r4 = grid(drs[0])
    m = (r4 > 0.2) & (r4 < 40)
    d1 = res[drs[0]]["Pi"] - res[drs[1]]["Pi"][::2]
    d2 = res[drs[1]]["Pi"][::2] - res[drs[2]]["Pi"][::4]
    factor = float(np.sqrt(np.mean(d1[m] ** 2)) / np.sqrt(np.mean(d2[m] ** 2)))
    return {"factor": factor, "mom": {dr: res[dr]["mom"] for dr in drs}, "drift": {dr: res[dr]["drift"] for dr in drs}}


# ------------------------------------------------------------------------------------------------ S2 the threshold and gamma
FINE_P = [0.016885, 0.01689, 0.016895, 0.0169, 0.01691, 0.01693, 0.01696, 0.0170, 0.0171, 0.0173, 0.0176, 0.0180]


def regenerate(fine=True):
    bank = {"p_list": P_LIST, "masses": {}}
    if fine:                                   # ~25 min: the masses at three readouts on the finest grid
        bank["fine005"] = {repr(p): collapse_masses(p, 0.005) for p in FINE_P}
        bank["sub005"] = {repr(p): collapse_masses(p, 0.005) for p in (0.01686, 0.01687)}
        bank["robust005"] = {repr(p): classify(p, 0.005) for p in (0.01686, 0.01687, 0.016875, 0.01688)}
        bank["m95_01"] = {repr(p): collapse_masses(p, 0.01) for p in (0.0169, 0.017, 0.0171, 0.0173, 0.0176, 0.018)}
    for dr in (0.02, 0.01):
        bank["masses"][str(dr)] = [collapse_mass(p, dr) for p in P_LIST]
    bank["sub"] = {str(dr): [collapse_mass(p, dr) for p in (0.0160, 0.0165, 0.0168)] for dr in (0.02, 0.01)}
    with open(BANK, "w") as f:
        json.dump(bank, f, indent=1)
    return bank


def load_bank():
    with open(BANK) as f:
        return json.load(f)


def fit_gamma(ps, Ms, lo=0.01670, hi=None, n=20000):
    """Least squares ln M = gamma ln(p - p*) + c with p* free inside [lo, min(hi, min(ps)))."""
    ps, Ms = np.array(ps), np.array(Ms)
    top = min(ps) - 1e-8 if hi is None else min(hi, min(ps) - 1e-8)
    best = None
    for ps_ in np.linspace(lo, top, n):
        x, y = np.log(ps - ps_), np.log(Ms)
        A = np.vstack([x, np.ones_like(x)]).T
        coef, *_ = np.linalg.lstsq(A, y, rcond=None)
        rss = float(np.sum((A @ coef - y) ** 2))
        if best is None or rss < best[0]:
            best = (rss, float(ps_), float(coef[0]), float(coef[1]))
    return {"rss": best[0], "p_star": best[1], "gamma": best[2], "c": best[3]}


def fit_fixed(ps, Ms, pstar, wiggle=None):
    """Slope at fixed p*; with wiggle = period in ln(p - p*), add A sin + B cos (READ: Delta/(2 gamma) ~ 4.61)."""
    x, y = np.log(np.array(ps) - pstar), np.log(np.array(Ms))
    cols = [x, np.ones_like(x)]
    if wiggle:
        cols += [np.sin(2 * np.pi * x / wiggle), np.cos(2 * np.pi * x / wiggle)]
    A = np.vstack(cols).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(coef[0]), float(np.sum((A @ coef - y) ** 2))


def fit_wiggle(ps, Ms, lo, hi, period=WIGGLE_READ, n=4000):
    best = None
    for ps_ in np.linspace(lo, min(hi, min(ps) - 1e-8), n):
        g, rss = fit_fixed(ps, Ms, ps_, period)
        if best is None or rss < best[0]:
            best = (rss, float(ps_), g)
    return {"rss": best[0], "p_star": best[1], "gamma": best[2]}


def fine_series(bank, th="0.95"):
    ps = sorted(float(k) for k in bank["fine005"])
    return ps, [bank["fine005"][repr(p)]["masses"][th]["M"] for p in ps]


def agreed(bank, tol=0.1):
    """The points both resolutions agree on (relative difference below tol) -- above the resolution floor."""
    m2, m1 = bank["masses"]["0.02"], bank["masses"]["0.01"]
    out = []
    for p, a, b in zip(bank["p_list"], m2, m1):
        if a["collapse"] and b["collapse"] and abs(a["M"] - b["M"]) / b["M"] < tol:
            out.append((p, b["M"]))
    return out


# ------------------------------------------------------------------------------------------------ S4 the endpoint
def eq17_rkk():
    """Radial null Ricci of eq. (17) (r in units of m) against the stage-1 closed form."""
    t, r, th, ph = sp.symbols("t r theta phi")
    F = 1 - 2 / r
    H = (1 - 2 / r) ** 2 / (1 - sp.Rational(3, 2) / r)
    g = sp.diag(-F, 1 / H, r**2, r**2 * sp.sin(th) ** 2)
    X = [t, r, th, ph]
    gi = g.inv()
    Gam = [[[sum(gi[a, k] * (sp.diff(g[k, b], X[c]) + sp.diff(g[k, c], X[b]) - sp.diff(g[b, c], X[k]))
                 for k in range(4)) / 2 for c in range(4)] for b in range(4)] for a in range(4)]

    def ric(b, c):
        return sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                               + sum(Gam[a][a][k] * Gam[k][b][c] - Gam[a][c][k] * Gam[k][b][a] for k in range(4))
                               for a in range(4)))
    # radial null k = (1/sqrt F, sqrt H, 0, 0): R_kk = R_tt/F + H R_rr
    Rkk = sp.simplify(ric(0, 0) / F + H * ric(1, 1))
    closed = -2 * (r - 2) / (r**2 * (2 * r - 3) ** 2)
    return Rkk, sp.simplify(Rkk - closed)


def scalar_nec():
    """For any scalar field, T_kk = (k.d phi)^2 for null k (the metric term drops): symbolic check on a general 2D null
    vector in the (t, r) plane of the polar-areal metric."""
    al, a, pt, pr, u = sp.symbols("alpha a phi_t phi_r u", real=True)
    k = sp.Matrix([1 / al, u / a])                 # null iff u^2 = 1
    g = sp.diag(-al**2, a**2)
    dphi = sp.Matrix([pt, pr])
    gk = (k.T * g * k)[0]
    T_kk = (k.T * dphi)[0] ** 2 - sp.Rational(1, 2) * gk * (-(pt / al) ** 2 + (pr / a) ** 2)
    return sp.simplify(T_kk.subs(u, 1) - ((k.T * dphi)[0].subs(u, 1)) ** 2), sp.simplify(gk.subs(u, 1))


def static_nec():
    """For any static -F dt^2 + dr^2/H + r^2 dOmega^2: radial R_kk = (H/r) d ln(F/H)/dr (exact), so the static null energy
    condition is F/H non-decreasing; for eq. (17), d ln(F/H)/dr = -m/((2r - 3m)(r - 2m)) < 0 (r in units of m)."""
    t, r, th, ph = sp.symbols("t r theta phi", positive=True)
    Ff, Hf = sp.Function("F")(r), sp.Function("H")(r)

    def rkk(F, H):
        g = sp.diag(-F, 1 / H, r**2, r**2 * sp.sin(th) ** 2)
        X = [t, r, th, ph]
        gi = g.inv()
        Gam = [[[sum(gi[a, k] * (sp.diff(g[k, b], X[c]) + sp.diff(g[k, c], X[b]) - sp.diff(g[b, c], X[k]))
                     for k in range(4)) / 2 for c in range(4)] for b in range(4)] for a in range(4)]

        def ric(b, c):
            return sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                                   + sum(Gam[a][a][k] * Gam[k][b][c] - Gam[a][c][k] * Gam[k][b][a] for k in range(4))
                                   for a in range(4)))
        return sp.simplify(ric(0, 0) / F + H * ric(1, 1)), [sp.simplify(gi[i, i] * ric(i, i)) for i in range(4)]
    gen, _ = rkk(Ff, Hf)
    F = 1 - 2 / r
    H = (1 - 2 / r) ** 2 / (1 - sp.Rational(3, 2) / r)
    _, mixed = rkk(F, H)
    Rs = sp.simplify(sum(mixed))
    Gt = [sp.simplify(mixed[i] - Rs / 2) for i in range(4)]
    rho, pr, pt = (sp.simplify(-Gt[0] / (8 * sp.pi)), sp.simplify(Gt[1] / (8 * sp.pi)), sp.simplify(Gt[2] / (8 * sp.pi)))
    return {"general": sp.simplify(gen - (Hf / r) * sp.diff(sp.log(Ff / Hf), r)),
            "dlnFH": sp.factor(sp.simplify(sp.diff(sp.log(F / H), r))), "R": Rs, "rho": sp.factor(rho),
            "pr": sp.factor(pr), "pt": sp.factor(pt), "radial": sp.factor(sp.simplify(rho + pr)),
            "tangential": sp.factor(sp.simplify(rho + pt)),
            "int_rho": sp.simplify(sp.integrate(4 * sp.pi * r**2 * rho, (r, 2, sp.oo)))}


def compute(live=True):
    d = {"bank": load_bank(), "rkk": eq17_rkk(), "nec": scalar_nec(), "madm_star": m_adm(P_STAR)}
    if live:
        d["flat"] = flat_control()
        d["strong"] = strong_control()
    pts = agreed(d["bank"])
    d["agreed"] = pts
    ps, Ms = fine_series(d["bank"])
    d["fine"] = (ps, Ms)
    lo, hi = BRACKET
    d["fit"] = fit_gamma(ps, Ms, lo, hi)
    d["fit_subsets"] = [fit_gamma(ps[a:b], Ms[a:b], lo, hi) for a, b in ((0, 9), (3, 12), (0, 7), (5, 12))]
    d["gamma_range"] = [fit_fixed(ps, Ms, x)[0] for x in np.linspace(lo + 1e-7, hi - 1e-7, 9)]
    d["wiggle"] = fit_wiggle(ps, Ms, lo, hi)
    d["static"] = static_nec()
    d["m95_01"] = d["bank"].get("m95_01", {})
    m01 = {p: x["M"] for p, x in zip(d["bank"]["p_list"], d["bank"]["masses"]["0.01"])}
    d["res_agree"] = [(p, m01[p], d["bank"]["fine005"][repr(p)]["masses"]["0.8"]["M"]) for p in (0.0169, 0.017, 0.0171,
                                                                                                 0.0173, 0.0176, 0.018)]
    d["T_star"] = 2 * DELTA / d["madm_star"]
    return d


def report(d):
    print("sim1_transition.py -- B4d simulation phase 1: a transition in one spacetime (the board's reading)\n")
    if "flat" in d:
        print("S1 flat control, max relative error in Pi (t = 20, 40): %s" % {k: {t: "%.2e" % e for t, e in v.items()}
                                                                           for k, v in d["flat"].items()})
        s = d["strong"]
        print("   strong field p = 0.8 p*: convergence factor %.3f; momentum residual/scale %s; mass drift %s" % (
            s["factor"], {k: "%.1e" % (v[0] / v[1]) for k, v in s["mom"].items()}, {k: "%.1e" % v for k, v in s["drift"].items()}))
    b = d["bank"]
    print("S2 robust outcomes at dr = 0.005: %s" % {k: v["outcome"] for k, v in sorted(b.get("robust005", {}).items())})
    ps, Ms = d["fine"]
    print("   dr = 0.005, 0.95 readout: %s" % ", ".join("%.6f:%.4f" % (p, M) for p, M in zip(ps, Ms)))
    m01 = d["m95_01"]
    print("   dr = 0.01 vs 0.005, 0.95 readout: %s" % ", ".join(
        "%s: %.4f/%.4f" % (k, v["masses"]["0.95"]["M"], b["fine005"][repr(float(k))]["masses"]["0.95"]["M"])
        for k, v in sorted(m01.items())))
    print("   dr = 0.01 vs 0.005, 0.8 readout: %s" % ", ".join("%.4f: %.4f/%.4f" % t for t in d["res_agree"]))
    print("   plain fit (p* in the bracket): gamma = %.3f at p* = %.6f; sub-ranges %s" % (
        d["fit"]["gamma"], d["fit"]["p_star"], ", ".join("%.3f" % f_["gamma"] for f_ in d["fit_subsets"])))
    print("   plain gamma across the bracket: %s" % ", ".join("%.3f" % g for g in d["gamma_range"]))
    print("   with the wiggle (period %.2f): gamma = %.3f at p* = %.6f, rss %.1e against plain %.1e; READ %.3f" % (
        WIGGLE_READ, d["wiggle"]["gamma"], d["wiggle"]["p_star"], d["wiggle"]["rss"], d["fit"]["rss"], GAMMA_READ))
    print("S3 M_ADM(p*) = %.4f; threshold duration ~ 2 delta/M_ADM = %.1f, rate ~ %.3f per mass unit; an even write over "
          "2.0e5 clocks: rate %.0e, family amplitude ~ %.1e" % (d["madm_star"], d["T_star"], 1 / d["T_star"], 1 / 2.0e5,
                                                                 P_STAR * math.sqrt(d["T_star"] / 2.0e5)))
    st = d["static"]
    print("S4 static: R_kk - (H/r) dln(F/H)/dr = %s; eq. (17) dln(F/H)/dr = %s" % (st["general"], st["dlnFH"]))
    print("   eq. (17) radial R_kk = %s (vs closed form %s); scalar T_kk - (k.dphi)^2 = %s" % (
        d["rkk"][0], d["rkk"][1], d["nec"][0]))
    print("S5 eq. (17)'s Weyl fluid (m = 1): rho = %s, p_r = %s, p_t = %s; R = %s" % (st["rho"], st["pr"], st["pt"], st["R"]))
    print("   rho + p_r = %s; rho + p_t = %s; int rho outside 2m = %s" % (st["radial"], st["tangential"], st["int_rho"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    f = d["flat"]
    chk("S1 control: flat space, p = 1e-6 -- the exact solution reproduced, error below 2e-3 at dr = 0.02, falling 3.5-4.5x "
        "per halving at t = 20 and 40", all(f[0.02][t] < 2e-3 and 3.5 < f[0.04][t] / f[0.02][t] < 4.5 for t in (20.0, 40.0)))
    s = d["strong"]
    chk("S1 control: strong field (p = 0.8 p*) -- convergence factor 3.7-4.3; the unimposed momentum constraint's residual "
        "below 2e-3 of its scale and falling 3.5-4.5x per halving; mass drift below 1e-3 and falling",
        3.7 < s["factor"] < 4.3 and all(v[0] / v[1] < 2e-3 for v in s["mom"].values())
        and 3.5 < s["mom"][0.04][0] / s["mom"][0.02][0] < 4.5 and 3.5 < s["mom"][0.02][0] / s["mom"][0.01][0] < 4.5
        and s["drift"][0.01] < s["drift"][0.02] < s["drift"][0.04] < 1e-3)
    b = d["bank"]
    rob = b.get("robust005", {})
    chk("S2: robust outcomes at dr = 0.005 -- 0.01686, 0.01687, 0.016875 disperse (mass conserved, centre emptied), "
        "0.016885 collapses (2m/r 0.95 at >= 20 grid points), bracketing p*; the independent code's 0.01688 lies inside",
        all(rob.get(repr(x), {}).get("outcome") == "disperse" for x in (0.01686, 0.01687, 0.016875))
        and b["fine005"][repr(0.016885)]["masses"]["0.95"]["M"] * 2 / 0.95 >= 20 * 0.005
        and BRACKET[0] < 0.01688 < BRACKET[1])
    chk("S2: the two finest grids agree on the 0.8-readout masses to 0.5% (p >= 0.0169); the 0.95-readout masses agree to "
        "within 7%", all(abs(x / y - 1) < 0.005 for _, x, y in d["res_agree"])
        and all(abs(v["masses"]["0.95"]["M"] / b["fine005"][repr(float(k))]["masses"]["0.95"]["M"] - 1) < 0.07
                for k, v in d["m95_01"].items()) and len(d["m95_01"]) == 6)
    w = d["wiggle"]
    chk("S2: a plain power law fixes gamma only with p* (0.42 to 0.24 across the bracket); fitting the READ wiggle "
        "(period 4.61) gives gamma within 5% of the READ 0.374 and a residual at least 3x smaller",
        max(d["gamma_range"]) - min(d["gamma_range"]) > 0.05 and abs(w["gamma"] / GAMMA_READ - 1) < 0.05
        and w["rss"] < d["fit"]["rss"] / 3)
    chk("S3: at threshold the family carries M_ADM ~ 0.59 over ~2 delta: duration ~10, rate ~0.1 per mass unit; an even "
        "write over 2.0e5 clocks is a rate 2e4 times smaller -- in this family an amplitude ~1e-4, between the computed "
        "dispersals at 1e-6 and 0.01686", 0.4 < d["madm_star"] < 0.8 and 5 < d["T_star"] < 20
        and 2.0e5 / d["T_star"] > 1e4 and 1e-6 < P_STAR * math.sqrt(d["T_star"] / 2.0e5) < 0.01686)
    st = d["static"]
    chk("S4 (exact): for any static metric radial R_kk = (H/r) d ln(F/H)/dr; eq. (17)'s d ln(F/H)/dr = -m/((2r - 3m)(r - 2m)) "
        "< 0; its radial R_kk matches the closed form; a scalar's T_kk = (k.d phi)^2",
        st["general"] == 0 and sp.simplify(st["dlnFH"] + 1 / ((2 * sp.Symbol("r", positive=True) - 3)
                                                             * (sp.Symbol("r", positive=True) - 2))) == 0
        and d["rkk"][1] == 0 and d["nec"][0] == 0 and d["nec"][1] == 0)
    rr = sp.Symbol("r", positive=True)
    chk("S5 (exact): eq. (17)'s Weyl fluid has R = 0, rho > 0 integrating to m/4 outside 2m (ledger.py E4's 5m/4 - m, the "
        "control), radial rho + p_r < 0 and tangential rho + p_t > 0 -- anisotropic",
        st["R"] == 0 and st["int_rho"] == sp.Rational(1, 4)
        and all(float(st["radial"].subs(rr, x)) < 0 < float(st["tangential"].subs(rr, x)) for x in (2.01, 2.5, 3, 5, 20)))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--regenerate" in sys.argv:
        regenerate()
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
