#!/usr/bin/env python3
"""
qet.py -- DOCKET 66, wave 1, work item A3-qet: H-QET-EXOTIC tested, without presuming it.

Not seated.  Nothing here edits the board.  Every board figure is IMPORTED from the instrument that owns it --
../achievable.py (duration_bound, FEWSTER_C, HBAR, C_SI), ../wormhole.py (throat_mass, G), docket68/geometry.py
(r_quantum: the D68 R-QUANTUM fraction of a 1 m throat's deficit), docket68/measure.py (H, LN2, landauer_j,
bekenstein_floor_j), ../massform.py (PAYLOAD_KG, rest_energy_j), ../phase1.py (L_PROXIMA), ../transit.py
(BEATS_LIGHT), ../specthm.py (the seat classes, derived by z3 at run time) and ../ledger.py (M's words M-D65-1,
read as text) -- never retyped.  M's hypothesis is read from CHARTER.md.

    python3 qet.py              report
    python3 qet.py --selftest   counted checks, with CONTROLS (cases built to fail, which must fail);
                                checks that cannot fail are printed STRUCTURAL and are not counted
    python3 qet.py --json       the report's numbers and grades as JSON

M, verbatim (ledger M-D65-1, CHARTER.md): "consider the idea that the introduction of information into a space that
never previously contained it would be considered exotic matter".  Carried as H-QET-EXOTIC, a hypothesis, never a
result.  The ledger records that the question's parenthetical ("information arriving at the destination creates a
local negative-energy region there") was the question's description as put to M, NOT READ; it is tested here.

SOURCES, READ at source through alphaXiv (answer_pdf_queries, open arXiv PDFs) on 2026-10-04.  No paywall or login wall
was met; no 403.  PAGE CONVENTION (D66-fix, V66-2 #6): for Hotta 1002.0200v2 the pages below are the PRINTED page
numbers (the PDF's page minus one), re-read at D66-fix; wave 1 cited 'even before the start' to p.3 and eq.(8) to p.7,
off by one from the printed p.2 and p.8.  The other sources keep the pages A3 recorded.
  Hotta, arXiv:0803.2272v3 (16 Jul 2008) = PRD 78 045006, "Quantum Measurement Information as a key to Energy
      Extraction from Local Vacuums".  1+1 massless scalar; Alice measures, Bob acts after the classical message, "at
      t = T (>= t_o)" when Alice's wavepackets "have already passed by" (p.11); eq.(25) <H_B> = -eta^2/(2 xi) < 0 (p.14);
      the energy density before Bob's step is exactly zero (local vacuum, p.14); eq.(10) l <= hbar/(12 pi |E_n|) for
      the shock state (p.9); negative energy "sustained by a quantum correlation effect with positive-energy
      excitations" (p.9); the classical channel's speed is bounded by light (p.2).  Hotta's spin-chain QET is
      arXiv:0803.0348 (cited there, ref [14]); NOT READ here.
  Hotta, arXiv:1002.0200v2 (25 Jun 2010) = PLA 374 3416, "Energy Entanglement Relation for QET": the MINIMAL MODEL
      eqs (1)-(3) p.3; E_A eq.(4) p.5; no mu-independent operation on B extracts energy, eq.(5) p.5; max E_B eq.(8)
      p.8; Delta S_AB defined p.10, eqs (9) and (10) p.11 (D66-repro residual: first 'eqs (9)-(10) pp.10-11') (= the
      mutual information between pointer and B, p.10); inequalities (12)
      p.12 and (15) p.14; "The amount of output energy from B is upper bounded by the amount of input energy to A"
      (p.2); the output energy "existed not at A but at B even before the start of the protocol" (p.2).
  Ikeda, arXiv:2301.02666v5 (22 Aug 2023): the minimal model eqs (1)-(5) p.2, protocol eqs (6)-(14) p.2-3, analytic
      values Table I p.6 and Table II p.11 (the fixtures below), eq.(A7) p.10 (no unitary after the measurement alone
      extracts), eq.(A9) p.10 (free evolution), eqs (A10)-(A12) p.10.
  Funai & Martin-Martinez, arXiv:1701.03805v2 (19 Mar 2025): eq.(7) p.3 (Alice's term), eq.(1)-(2) the couplings p.2-3;
      Bob "only receives the information ... when he enters the lightcone of Alice" (p.3); the well sits between two
      positive peaks and cannot precede the wavepacket for a massless field (p.7); scaling eqs (34)-(36) p.11 and the
      quantum-interest statement p.11; eq.(23) the 3+1 form p.5.  The 1+1 energy density computed below is the
      review's eq.(116) (2505.04689v3 p.21), which restates FMM's eq.(11) and (7).
  Ragula & Martin-Martinez, arXiv:2505.04689v3 (11 Jul 2025), review: minimal QET eqs (10)-(19) p.4; "the energy given
      away is always less than or equal to the energy that was injected" p.6; eq.(34) p.6; eq.(116) p.21; scaling
      eqs (135)-(137) p.26; QET as "an operational pathway to engineer quantum states of exotic matter" p.26.
  Zachary, arXiv:2506.19878v1 (23 Jun 2025): eq.(3) p.5 a Gaussian MODEL of <T00>, not derived from a protocol; App.
      B.4 p.25 "We assume a fiducial energy scale" eps ~ 1e-11 J/m^3 "yielding" dR_peak ~ 1e-36 m^-2; eq.(A.3) p.23
      dR = 8 pi G d<T00> and eq.(B.2) p.25 dR = -8 pi G <T00> (opposite signs); QIX-C "do not enable superluminal
      travel" (p.20).
  Flanagan, arXiv:gr-qc/9706006v2 (16 Jul 1997): eq.(1.8) p.2 E_T,min = E_S,min = -(1/24 pi) int rho'^2/rho for the
      free massless scalar in 1+1 Minkowski; eq.(2.5) p.2 the right-moving sector alone: -(1/48 pi) int rho'^2/rho
      (hbar = c = 1); the minimising state is a squeezed vacuum (p.4); holds for every smooth normalised sampler.

WHAT IT COMPUTES
  (A) Hotta's minimal two-qubit model, exactly (numpy): the zero-mean ground state; Alice's sigma_x measurement and
      E_A; Bob's mu-conditioned rotation and the energy E_B he extracts (= minus the local energy <H_B + V> left at B);
      Ikeda's analytic Table I/II values reproduced; Hotta eq.(8) against a numeric optimum over all of Bob's SU(2)
      operations; Hotta eq.(5) (no mu-independent operation extracts); no-signalling (B's reduced state unchanged by
      Alice's measurement); the k = 0 product case; E_B <= E_A and its supremum over (h, k); the DURATION of the
      negative local energy under free evolution; Delta S_AB and Hotta's inequalities (12), (15).
  (B) the information-to-energy exchange: Alice's bit through a binary symmetric channel (flip eps); E_B against the
      classical mutual information I(mu; mu') in bits, numeric and from Hotta eq.(8) with q/p = 1 - 2 eps; the slope
      dE_B/dI at I -> 0; and the scaling E_B(s h, s k) = s E_B(h, k) at fixed information -- bits fix no joules.
  (C) the field: the 1+1 massless scalar QET state of FMM / the review's eq.(116), computed with Gaussian smearings
      (the principal-value integral in closed form via Dawson's function, checked against Cauchy quadrature): the
      negative well's depth, width, integrated energy and the time a fixed observer sees it; total energy >= 0;
      Flanagan's 1+1 QEI applied to the computed right-moving flux; FMM's scaling law (34)-(36).
  (D) the timing against light: the bit is a signal; at a destination D away Bob acts no earlier than D/c.
  (E) the board figures it is graded against: the 1 m throat's deficit (wormhole.throat_mass), D68 R-QUANTUM's
      fraction (geometry.r_quantum, via achievable.duration_bound), the 70 kg payload's rest energy (massform).
  (F) grades of H-QET-EXOTIC per D68 obstruction (O-BITS, O-MAKE-TOPO, O-MAKE-DIST, O-HOLD, O-SEAT, O-LOOP) in two
      readings, in docket68/B-combine.md's vocabulary (REMOVED / REMOVED-IF / NOT-BOUND-IF / OPEN / LEFT / LEFT-IF /
      SILENT), and against the seat's own conditions (specthm's classes, the Sturm condition, M-S1A-P3 (i)).

NAMED HYPOTHESES (every limitation carried by name; D68 names imported are used in D68's sense)
  H-MINIMAL       the two-qubit model (Hotta 1002.0200 eqs (1)-(3)) stands for QET's structure; energies are the model's raw
                  values at the stated (h, k) -- NOT in units of h (D66-fix, V66-2 #5: wave 1 labelled them 'h').
  H-PROJ          Alice's measurement is projective (q = +-p); the general POVM family is computed where named.
  H-INSTANT       local operations are instantaneous against 1/k (Hotta p.4-5; Ikeda p.2: t << 1/k).
  H-GROUND        the shared state is the ground state (strong local passivity: no local operation at B extracts).
  H-ACT           Bob performs a local operation conditioned on the bit; his device absorbs E_B.
  H-CORR          the ground state is entangled across A|B (k > 0); the bit is correlated with B's fluctuation.
  H-1+1           the field computation is the 1+1 massless scalar (FMM / review eq.(116)); 3+1 is NOT computed here.
  H-GAUSS         Gaussian smearings (FMM's case 2); their tails are not compact, so causality is checked on an
                  effective support of 4 widths (H-EFF-SUPPORT).
  H-DELTA-SWITCH  delta switching (FMM eq.(1)-(2)); the detector gap plays no role.
  H-SAMPLER       Flanagan's bound is tested on Gaussian samplers only: a pass is necessary, not sufficient.
  H-QET-HADAMARD  the states QET makes (coherent superpositions of the vacuum) lie in the class the duration bound
                  covers (Hadamard states of the free massless minimally coupled scalar).  Not proved here; a short
                  check by the standard argument (displaced vacua with smooth smearings), not run: OPEN (N_QETHAD).
  H_flat, H-PATH, H-MIN-SCALAR   geometry.r_quantum's (D68 R-QUANTUM), imported with the fraction.
  H-QET-BUDGET    E_B <= E_A (Hotta 1002.0200 p.2; review p.6; computed for the minimal model).
  H-1+1-TO-3+1    any comparison of a 1+1 energy with a 3+1 throat is dimensional, not a bound.  Context only.
  N_QET-NMC       wave 1's name for QET with a nonminimally coupled scalar (xi > 0).  D66-fix (V66-0 #7): that branch,
                  and the curved-space one, are the BOARD's R-QUANTUM pathways (N_XI, N_QEIC), present with or without
                  QET; QET's own OPEN pathway on O-HOLD is N_QETHAD (H-QET-HADAMARD unchecked).
  N_QTOPO, ITB    D68's (an information layer beneath geometry), carried unchanged.

stdlib + numpy + scipy (+ z3 via specthm).
"""
import contextlib
import io
import json
import math
import os
import re
import sys

import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm, sqrtm
from scipy.optimize import minimize, minimize_scalar
from scipy.special import dawsn

HERE = os.path.dirname(os.path.abspath(__file__))
BOARD = os.path.dirname(HERE)
D68 = os.path.join(BOARD, "docket68")
for _p in (BOARD, D68):
    if _p not in sys.path:
        sys.path.insert(0, _p)


def _quiet_import(name):
    with contextlib.redirect_stdout(io.StringIO()):
        return __import__(name)


achievable = _quiet_import("achievable")
wormhole = _quiet_import("wormhole")
geometry = _quiet_import("geometry")
measure = _quiet_import("measure")
massform = _quiet_import("massform")
phase1 = _quiet_import("phase1")
transit = _quiet_import("transit")

HBAR, C = achievable.HBAR, achievable.C_SI
G = wormhole.G
YEAR_S = 365.25 * 86400.0          # Julian year, a unit definition

HISTORY = [
    ("R-LIT's label", "M's words read alone",
     "the question's parenthetical read as arrival alone; M's sentence read operationally is R-QET", "V66-1 #7"),
    ("item 3 of the answer", "genuine negative energy density ... 'exotic matter' in the standard sense",
     "a local negative energy density (pointwise WEC violation), which the review calls a pathway to exotic matter "
     "(p.26); offset by positive energy (FMM p.3), obeying the QEIs (C6; FMM p.11), not the averaged violation a throat "
     "needs", "V66-0 #6"),
    ("O-HOLD's open branch", "OPEN on the xi > 0 branch via N_QET-NMC",
     "N_XI and N_QEIC are the board's R-QUANTUM pathways, with or without QET; QET's own is N_QETHAD, a short check",
     "V66-0 #7"),
    ("duration", "t* = 0.1450/k at (1.5, 1) and 0.1855/k at (1, 1)",
     "0.1449/k and 0.1854/k by bisection (the grid's first point >= 0 was printed)", "V66-2 #4"),
    ("units", "E_B = 0.1425 h, E_A = 1.2481 h, 0.494 h per nat, 0.2036 h per bit, E_B = -0.079 h",
     "raw model values at (h, k) = (1.5, 1): E_B = 0.14252 (E_B/h = 0.0950), E_A = 1.2481 (E_A/h = 0.832)", "V66-2 #5"),
    ("Hotta 1002.0200v2 pages", "'even before the start' p.3; eq.(8) p.7",
     "printed p.2 and p.8", "V66-2 #6"),
]

# ===================================================================================== (A) the minimal model
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
K = np.kron

#: Ikeda 2301.02666v5, Table II p.11 (analytic rows), (h, k) -> (E_0, <V>, <H_1>, <E_1>); 4 decimals as printed.
IKEDA_ANALYTIC = {
    (1.0, 0.1): (0.9950, -0.0193, 0.0144, -0.0049),
    (1.0, 0.2): (0.9806, -0.0701, 0.0521, -0.0180),
    (1.0, 0.5): (0.8944, -0.2598, 0.1873, -0.0726),
    (1.0, 1.0): (0.7071, -0.3746, 0.2598, -0.1147),
    (1.5, 1.0): (1.2481, -0.4905, 0.3480, -0.1425),
}


def model(h, k):
    """Hotta 1002.0200 eqs (1)-(3) / Ikeda eqs (1)-(3): H = H_A + H_B + V with the zero-mean constants."""
    s = math.hypot(h, k)
    HA = h * K(SZ, I2) + (h * h / s) * np.eye(4)
    HB = h * K(I2, SZ) + (h * h / s) * np.eye(4)
    V = 2 * k * K(SX, SX) + (2 * k * k / s) * np.eye(4)
    H = HA + HB + V
    w, vec = np.linalg.eigh(H)
    return {"HA": HA, "HB": HB, "V": V, "H": H, "g": vec[:, 0], "E0": w[0], "gap": w[1] - w[0], "h": h, "k": k}


def ev(rho, O):
    return float(np.real(np.trace(rho @ O)))


def proj_A(mu):
    return K((I2 + mu * SX) / 2, I2)


def phi_opt(h, k):
    """Ikeda eqs (11)-(12): cos 2phi = (h^2+2k^2)/R, sin 2phi = hk/R."""
    return 0.5 * math.atan2(h * k, h * h + 2 * k * k)


def ry_B(angle):
    """exp(-i angle Y) on B (Ikeda eq.(10): U_1(mu) = cos phi - i mu sin phi Y)."""
    return K(I2, expm(-1j * angle * SY))


def post_alice(m):
    """Alice's non-selective sigma_x measurement on |g>: sum_mu P(mu)|g><g|P(mu)."""
    g = m["g"]
    return sum(np.outer(proj_A(mu) @ g, (proj_A(mu) @ g).conj()) for mu in (1, -1))


def qet_state(m, phi=None, flip=0.0, bob=None):
    """Bob applies U(mu') with mu' the received bit (flip probability `flip`).  bob(mu') -> 4x4 unitary on B
    overrides the rotation.  Returns the averaged state."""
    g = m["g"]
    phi = phi_opt(m["h"], m["k"]) if phi is None else phi
    rho = np.zeros((4, 4), dtype=complex)
    for mu in (1, -1):
        s0 = proj_A(mu) @ g
        for mup, pr in ((mu, 1.0 - flip), (-mu, flip)):
            if pr == 0.0:
                continue
            U = bob(mup) if bob is not None else ry_B(mup * phi)
            s = U @ s0
            rho += pr * np.outer(s, s.conj())
    return rho


def minimal_values(h, k):
    m = model(h, k)
    rho = qet_state(m)
    EA = ev(post_alice(m), m["H"])
    EB = -ev(rho, m["HB"] + m["V"])
    return {"h": h, "k": k, "E_A": EA, "E_A_closed": h * h / math.hypot(h, k), "V": ev(rho, m["V"]),
            "H1": ev(rho, m["HB"]), "E1_local_at_B": -EB, "E_B": EB, "E_B_over_E_A": EB / EA,
            "E_B_hotta8": hotta8(h, k, [(0.5, 0.5), (0.5, -0.5)]), "total_after": ev(rho, m["H"])}


def hotta8(h, k, pq):
    """Hotta 1002.0200 eq.(8): max E_B for a POVM Pi(mu) = p(mu) + q(mu) sigma_x (pairs (p, q))."""
    s = math.hypot(h, k)
    a = h * h + 2 * k * k
    return a / s * sum(p * (math.sqrt(1 + h * h * k * k * q * q / (a * a * p * p)) - 1) for p, q in pq if p > 0)


def su2(params):
    """A general SU(2): exp(-i (a X + b Y + c Z))."""
    a, b, c = params
    return expm(-1j * (a * SX + b * SY + c * SZ))


def numeric_max_EB(m, povm, starts=12, seed=1):
    """max over Bob's mu-dependent SU(2) operations of E_B, for Alice's POVM operators povm[mu] (2x2 on A)."""
    g = m["g"]
    rng = np.random.default_rng(seed)
    branches = [K(M, I2) @ g for M in povm]

    def negEB(x):
        tot = 0.0
        for i, s0 in enumerate(branches):
            s = K(I2, su2(x[3 * i:3 * i + 3])) @ s0
            tot += float(np.real(s.conj() @ (m["HB"] + m["V"]) @ s))
        return tot                      # = <H_B + V> = -E_B
    best = None
    for _ in range(starts):
        r = minimize(negEB, rng.normal(scale=1.0, size=3 * len(branches)), method="BFGS")
        if best is None or r.fun < best.fun:
            best = r
    return -best.fun


def numeric_min_mu_independent(m, trials=400, seed=2):
    """min over random mu-INDEPENDENT unitaries W_B of the energy change Tr[W rho_M W^+ H] - E_A (Hotta eq.(5))."""
    rng = np.random.default_rng(seed)
    rhoM = post_alice(m)
    EA = ev(rhoM, m["H"])
    out = []
    for _ in range(trials):
        W = K(I2, su2(rng.normal(scale=2.0, size=3)))
        out.append(ev(W @ rhoM @ W.conj().T, m["H"]) - EA)
    r = minimize(lambda x: ev(K(I2, su2(x)) @ rhoM @ K(I2, su2(x)).conj().T, m["H"]) - EA,
                 rng.normal(size=3), method="BFGS")
    return min(min(out), r.fun)


def ptrace_A(rho):
    return np.einsum("ijik->jk", rho.reshape(2, 2, 2, 2))


def no_signalling(m):
    rg = np.outer(m["g"], m["g"].conj())
    return float(np.abs(ptrace_A(post_alice(m)) - ptrace_A(rg)).max())


def duration(h, k, tmax_over_k=3.0, n=6001):
    """Free evolution under H after Bob's step: the first time <H_B + V>(t) >= 0, in units of 1/k."""
    m = model(h, k)
    rho0 = qet_state(m)
    w, vec = np.linalg.eigh(m["H"])
    ts = np.linspace(0.0, tmax_over_k / k, n)
    vals = []
    for t in ts:
        U = vec @ np.diag(np.exp(-1j * w * t)) @ vec.conj().T
        vals.append(ev(U @ rho0 @ U.conj().T, m["HB"] + m["V"]))
    vals = np.array(vals)
    idx = int(np.argmax(vals >= 0.0))

    def f(t):
        U = vec @ np.diag(np.exp(-1j * w * t)) @ vec.conj().T
        return ev(U @ rho0 @ U.conj().T, m["HB"] + m["V"])
    lo, hi = float(ts[idx - 1]), float(ts[idx])          # D66-fix (V66-2 #4): bisect inside the grid bracket
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) >= 0.0:
            hi = mid
        else:
            lo = mid
    t_star = 0.5 * (lo + hi)
    return {"t_star": t_star, "t_star_k": t_star * k, "t_grid_k": float(ts[idx] * k), "f_at_t_star": f(t_star),
            "f_at_grid": float(vals[idx]), "E_local_at_0": float(vals[0]), "min": float(vals.min())}


def alice_only_evolution(h, k, t):
    """Ikeda eq.(A9): <H_1(t)>, <V(t)> after Alice's measurement alone."""
    m = model(h, k)
    rho = post_alice(m)
    w, vec = np.linalg.eigh(m["H"])
    U = vec @ np.diag(np.exp(-1j * w * t)) @ vec.conj().T
    r = U @ rho @ U.conj().T
    return ev(r, m["HB"]), ev(r, m["V"])


def povm_ops(r):
    """Alice's POVM with Pi(mu) = 1/2 (1 + mu r sigma_x), r in [0, 1]; M(mu) = sqrt(Pi(mu))."""
    return [np.array(sqrtm((I2 + mu * r * SX) / 2), dtype=complex) for mu in (1, -1)]


def entropy_nats(rho2):
    w = np.linalg.eigvalsh(rho2)
    return -sum(x * math.log(x) for x in w if x > 1e-15)


def delta_S(m, povm):
    """Delta S_AB = S(rho_B) - sum_mu p(mu) S(rho_B(mu)) (Hotta 1002.0200 p.10), from the states themselves."""
    g = m["g"]
    SB = entropy_nats(ptrace_A(np.outer(g, g.conj())))
    tot = 0.0
    for M in povm:
        s = K(M, I2) @ g
        p = float(np.real(s.conj() @ s))
        if p > 1e-15:
            tot += p * entropy_nats(ptrace_A(np.outer(s, s.conj())) / p)
    return SB - tot


def delta_S_formula(h, k, r):
    """Hotta eqs (9)-(10) with p = 1/2, q = +-r/2."""
    cs = h / math.hypot(h, k)
    sn = k / math.hypot(h, k)

    def ent(y):
        a, b = (1 + y) / 2, (1 - y) / 2
        return -sum(x * math.log(x) for x in (a, b) if x > 0)
    return ent(cs) - ent(math.sqrt(cs * cs + sn * sn * r * r))


def hotta12_rhs(h, k, EB, coef_scale=1.0):
    cs = h / math.hypot(h, k)
    sn = k / math.hypot(h, k)
    return coef_scale * (1 + sn * sn) / (2 * cs ** 3) * math.log((1 + cs) / (1 - cs)) * EB / math.hypot(h, k)


def hotta15_rhs(h, k, dS):
    cs = h / math.hypot(h, k)
    num = 2 * math.hypot(h, k) * (math.sqrt(4 - 3 * cs * cs) - 2 + cs * cs)
    den = (1 + cs) * math.log(2 / (1 + cs)) + (1 - cs) * math.log(2 / (1 - cs))
    return num / den * dS


def entanglement_table(h=1.5, k=1.0, rs=(0.05, 0.2, 0.5, 0.8, 1.0)):
    m = model(h, k)
    rows = []
    for r in rs:
        pv = povm_ops(r)
        EB = numeric_max_EB(m, pv, starts=6)
        dS = delta_S(m, pv)
        rows.append({"r": r, "max_E_B_numeric": EB, "max_E_B_hotta8": hotta8(h, k, [(0.5, r / 2), (0.5, -r / 2)]),
                     "dS_nats": dS, "dS_formula": delta_S_formula(h, k, r), "rhs12": hotta12_rhs(h, k, EB),
                     "rhs15": hotta15_rhs(h, k, dS), "E_B_per_nat": EB / dS if dS > 0 else None})
    return rows


def sup_ratio(n=4001):
    """E_B / E_A over k/h in [1e-3, 1e3] (projective), from Hotta eq.(8) and eq.(4)."""
    best = (0.0, None)
    for x in np.logspace(-3, 3, n):
        EB = hotta8(1.0, x, [(0.5, 0.5), (0.5, -0.5)])
        r = EB / (1.0 / math.hypot(1.0, x))
        if r > best[0]:
            best = (r, x)
    return {"sup": best[0], "at_k_over_h": best[1]}


# ===================================================================================== (B) information -> energy
def h2_bits(eps):
    return measure.H([eps, 1 - eps]) / measure.LN2


def bsc_row(h, k, eps):
    m = model(h, k)
    res = minimize_scalar(lambda ph: ev(qet_state(m, phi=ph, flip=eps), m["HB"] + m["V"]),
                          bounds=(-math.pi / 2, math.pi / 2), method="bounded", options={"xatol": 1e-12})
    EBnum = -res.fun
    q = 1 - 2 * eps
    return {"eps": eps, "I_bits": 1.0 - h2_bits(eps), "E_B_numeric": EBnum,
            "E_B_hotta8_q": hotta8(h, k, [(0.5, q / 2), (0.5, -q / 2)]),
            "E_B_fixed_phi": -ev(qet_state(m, flip=eps), m["HB"] + m["V"])}


def bsc_table(h=1.5, k=1.0, epss=(0.0, 0.05, 0.11, 0.2, 0.3, 0.4, 0.45, 0.5)):
    return [bsc_row(h, k, e) for e in epss]


def slope_at_zero_info(h, k):
    """dE_B/dI at I -> 0 (bits): E_B ~ a q^2 / 2 with a = h^2k^2/((h^2+2k^2) sqrt(h^2+k^2)), I ~ q^2/(2 ln 2)."""
    a = h * h * k * k / ((h * h + 2 * k * k) * math.hypot(h, k))
    return a * measure.LN2


# ===================================================================================== (C) the 1+1 field
SQ2PI = math.sqrt(2 * math.pi)


def lam(x, l0, d):
    return l0 * np.exp(-x * x / (2 * d * d)) / SQ2PI


def lamp(x, l0, d):
    return -x / (d * d) * lam(x, l0, d)


def pp_closed(v, l0, d):
    """PP int lam'(y)/(y - v) dy for the Gaussian lam, via Dawson's D:  PP int e^{-z^2}/(z - a) dz = -2 sqrt(pi) D(a)
    and d/dv PP int f(y)/(y - v) dy = PP int f'(y)/(y - v) dy."""
    a = v / (math.sqrt(2) * d)
    return l0 / SQ2PI * (-2 * math.sqrt(math.pi)) * (1 - 2 * a * dawsn(a)) / (math.sqrt(2) * d)


def pp_numeric(v, l0, d):
    return quad(lambda y: lamp(y, l0, d), -40 * d, 40 * d, weight="cauchy", wvar=v, limit=400)[0]


def field_cfg(Ups=1.0, db=0.1, T=10.0, m0=None, kqet=1.0, sgn=1.0, d=1.0):
    """A QET configuration (hbar = c = 1, length unit = Alice's width d).  FMM's scaling (34)-(36) is applied with Ups:
    lam -> lam(Ups x) (n = 2: amplitude Ups^0), mu -> Ups mu(Ups x), times / Ups."""
    l0 = math.sqrt(math.pi)            # maximises l0 exp(-l0^2/2 pi), the QET term's Alice factor
    return {"l0": l0, "d": d / Ups, "db": db / Ups, "xb": T / Ups, "T": T / Ups, "m0": m0, "Ups": Ups,
            "kqet": kqet, "sgn": sgn}


def overlap(l0):
    """e^{-2||alpha||}, ||alpha|| = int dk |alpha_k|^2 = l0^2/(4 pi) for the Gaussian (independent of d)."""
    return math.exp(-2 * l0 * l0 / (4 * math.pi))


def mu_b(x, cfg):
    return cfg["m0"] * np.exp(-((x - cfg["xb"]) ** 2) / (2 * cfg["db"] ** 2)) / SQ2PI


def rho_R(v, cfg):
    """Right-moving energy density after Bob's step (review eq.(116)), v = x - t, t > T:
    1/4 lam'(v)^2 + 1/4 mu(v + T)^2 + s e^{-2||a||}/(2 pi) mu(v + T) PP int lam'(y)/(y - v)."""
    l0, d = cfg["l0"], cfg["d"]
    mu = mu_b(v + cfg["T"], cfg)
    pp = np.array([pp_closed(x, l0, d) for x in np.atleast_1d(v)])
    return 0.25 * lamp(v, l0, d) ** 2 + 0.25 * mu ** 2 + cfg["kqet"] * cfg["sgn"] * overlap(l0) / (2 * math.pi) * mu * pp


def rho_L(u, cfg):
    """Left-moving density, u = x + t: 1/4 lam'(u)^2 + 1/4 mu(u - T)^2 + s e^{-2||a||}/(2 pi) mu(u - T) PP(u)."""
    l0, d = cfg["l0"], cfg["d"]
    mu = mu_b(u - cfg["T"], cfg)
    pp = np.array([pp_closed(x, l0, d) for x in np.atleast_1d(u)])
    return 0.25 * lamp(u, l0, d) ** 2 + 0.25 * mu ** 2 + cfg["kqet"] * cfg["sgn"] * overlap(l0) / (2 * math.pi) * mu * pp


def grid(cfg, half=15.0, n=30001):
    return np.linspace(-half * cfg["d"] * 1.0, half * cfg["d"] * 1.0, n)


def optimise_m0(cfg):
    """Bob's coupling strength chosen to make the right-moving well deepest (FMM's optimisation, one parameter)."""
    v = np.linspace(-3 * cfg["d"], 3 * cfg["d"], 6001)

    def depth(m0):
        c = dict(cfg, m0=m0)
        return float(rho_R(v, c).min())
    r = minimize_scalar(depth, bounds=(1e-4, 20.0 * cfg["Ups"]), method="bounded", options={"xatol": 1e-10})
    return dict(cfg, m0=r.x)


def well(cfg):
    v = grid(cfg)
    dv = v[1] - v[0]
    r = rho_R(v, cfg)
    neg = r < 0
    u = np.linspace(-15 * cfg["d"], 2 * cfg["T"] + 15 * cfg["d"], 60001)
    du = u[1] - u[0]
    rl = rho_L(u, cfg)
    return {"min_density": float(r.min()), "v_at_min": float(v[np.argmin(r)]),
            "neg_energy": float(r[neg].sum() * dv), "neg_width": float(neg.sum() * dv),
            "right_total": float(r.sum() * dv), "left_total": float(rl.sum() * du),
            "total": float(r.sum() * dv + rl.sum() * du), "v": v, "rho": r}


def flanagan_test(cfg, w=None):
    """max over Gaussian samplers f (centre c, width s) of  [int f rho_R dv] / [-(1/48 pi) int f'^2/f]  (Flanagan
    eq.(2.5), right-moving sector; int f'^2/f = 1/s^2 for a unit-mass Gaussian).  <= 1 is the bound."""
    w = w or well(cfg)
    v, r = w["v"], w["rho"]
    dv = v[1] - v[0]
    worst = (0.0, None, None)
    for c in np.linspace(-1.0, 1.0, 41) * cfg["d"]:
        for s in np.logspace(-2.5, 1.0, 71) * cfg["d"]:
            f = np.exp(-(v - c) ** 2 / (2 * s * s)) / (SQ2PI * s)
            val = float((f * r).sum() * dv)
            bound = -1.0 / (48 * math.pi * s * s)
            if val / bound > worst[0]:
                worst = (val / bound, float(c), float(s))
    return {"max_ratio": worst[0], "at_centre": worst[1], "at_width": worst[2]}


def field_table():
    base = optimise_m0(field_cfg())
    wb = well(base)
    fl = flanagan_test(base, wb)
    hbarc = HBAR * C
    si = {"length_unit_m": 1.0, "neg_energy_J": wb["neg_energy"] * hbarc / 1.0,
          "duration_at_a_point_s": wb["neg_width"] * 1.0 / C, "min_density_J_per_m": wb["min_density"] * hbarc / 1.0}
    return {"cfg": {k: v for k, v in base.items()}, "well": {k: v for k, v in wb.items() if k not in ("v", "rho")},
            "flanagan": fl, "SI_at_d_1m": si}


def scaling_check(base, Ups):
    """FMM eq.(34): rho_Ups(x) = Ups^2 rho_1(Ups x) in 1+1 (n = 2)."""
    c2 = dict(field_cfg(Ups=Ups), m0=base["m0"] * Ups)
    v1 = np.linspace(-3, 3, 241)
    a = rho_R(v1 / Ups, c2)
    b = Ups ** 2 * rho_R(v1, base)
    return float(np.abs(a - b).max() / np.abs(b).max())


# ===================================================================================== (D)-(E) timing, board
def board_figures():
    rq = geometry.r_quantum()
    return {"throat_deficit_J_1m": wormhole.throat_mass(1.0) * C ** 2,
            "r_quantum_fraction": rq["fraction_covered"], "r_quantum_required_Pa": rq["required_Pa"],
            "r_quantum_allowed_Pa": rq["allowed_Pa"], "hold_time_s": rq["hold_time_s"],
            "payload_kg": massform.PAYLOAD_KG, "payload_rest_J": massform.PAYLOAD_KG * C ** 2,
            "proxima_light_time_yr": phase1.L_PROXIMA / C / YEAR_S, "BEATS_LIGHT": transit.BEATS_LIGHT,
            "duration_bound_1ns_Pa": achievable.duration_bound(1e-9),
            "landauer_1bit_TCMB_J": measure.landauer_j(1, 2.7255), "bekenstein_1bit_1m_J": measure.bekenstein_floor_j(1, 1.0)}


def zachary_check():
    """2506.19878v1 App. B.4 p.25: eps ~ 1e-11 J/m^3 'yielding' dR_peak ~ 1e-36 m^-2; its eq.(B.3) is dR = 8 pi G eps
    exp(...).  With c restored (SI): 8 pi G eps / c^4."""
    eps = 1e-11
    si = 8 * math.pi * G * eps / C ** 4
    return {"eps_J_m3": eps, "dR_SI_m^-2": si, "printed_m^-2": 1e-36, "printed_over_SI": 1e-36 / si,
            "8piG_eps_over_c2_s^-2": 8 * math.pi * G * eps / C ** 2}


# ===================================================================================== the board's text
def m_words():
    led = _quiet_import("ledger")
    for r in led.RULED_BY_M:
        if r[0] == "M-D65-1":
            return " ".join(r)
    return ""


def charter_hypothesis():
    txt = open(os.path.join(HERE, "CHARTER.md"), encoding="utf-8").read()
    m = re.search(r"\| H-QET-EXOTIC \| (.+?) \| (.+?) \|", txt)
    return (m.group(1), m.group(2)) if m else (None, None)


_SPEC = {}


def specthm_verdicts():
    """The seat and throat class verdicts, derived by specthm's own z3 at run time (about 45 s)."""
    if not _SPEC:
        with contextlib.redirect_stdout(io.StringIO()):
            spec = _quiet_import("specthm")
            mdl = spec.build()
            v = spec.derive(mdl)
        _SPEC.update({k: v[k]["verdict"] for k in v})
        _SPEC["_M-S1A-P3_ruled"] = spec.ruled("M-S1A-P3")
        _SPEC["_sturm_member_diameter"] = spec.sturm_over_ball(min(mdl["F"]["soc"]))["member_diameter"]
    return dict(_SPEC)


# ===================================================================================== (F) grades
VERDICT_WORDS = ("REMOVED", "REMOVED-IF", "NOT-BOUND-IF", "OPEN", "LEFT", "LEFT-IF", "SILENT")
OBSTRUCTIONS = ("O-BITS", "O-MAKE-TOPO", "O-MAKE-DIST", "O-HOLD", "O-SEAT", "O-LOOP")


def grades(spec=None, bf=None, ft=None, sr=None):
    spec = spec or specthm_verdicts()
    bf = bf or board_figures()
    ft = ft or field_table()
    sr = sr or sup_ratio()
    mv = minimal_values(1.5, 1.0)
    seat = ("specthm's seat classes are not moved (S-1 %s, S-2 %s, S-3 %s, Rec %s; z3 at run time). The Sturm condition "
            "is SUFFICIENT and needs T_kk large and POSITIVE along a chord; QET supplies negative T_kk, so it can only "
            "lower that left-hand side: it certifies no seating and refuses none. M-S1A-P3 (i): SATISFIED-IF "
            "{H-FLAT-QFT}: QET is a protocol of Minkowski QFT whose step at the seat follows the bit, so it introduces "
            "no closed causal curve and no Borde pathology at the seat"
            % (spec.get("S-1"), spec.get("S-2"), spec.get("S-3"), spec.get("Rec")))
    hold = ("LEFT-IF {H_flat, H-PATH, H-MIN-SCALAR, H-QET-HADAMARD}: the states QET makes are states of the free field, "
            "so the duration bound binds them exactly as it binds any state; QET can at most saturate it (FMM p.11, "
            "the review p.26: QET 'saturates' the quantum-interest scaling; computed here in 1+1: the QET flux sits at "
            "%.3f of Flanagan's bound). The fraction of the 1 m throat's deficit (%.4e J) the bound covers is %.3e "
            "(geometry.r_quantum, imported), and QET does not move it. QET's own OPEN pathway is N_QETHAD: "
            "H-QET-HADAMARD is unchecked -- a short check, not a hard open question: the post-protocol state is a finite "
            "mixture of finite superpositions of Weyl-displaced vacua with smooth smearings, whose two-point function "
            "is, by the standard argument, the vacuum's plus a finite sum of products of smooth classical solutions; "
            "not run here, so OPEN. The xi > 0 and curved-space branches are the BOARD's R-QUANTUM pathways (N_XI, "
            "N_QEIC), present with or without QET, not QET's (wave 1 first said 'OPEN on the xi > 0 branch via "
            "N_QET-NMC'). Under ITB the geometric form is NOT-BOUND-IF {N_QTOPO} (the board's, D68); QET adds "
            "nothing to it"
            % (ft["flanagan"]["max_ratio"], bf["throat_deficit_J_1m"], bf["r_quantum_fraction"]))
    seat_ob = ("LEFT-IF {H-QET-BUDGET, H-MINIMAL for the ratio}: as a supply route QET relocates energy that was "
               "injected at the source, at no more than E_A (READ, Hotta 1002.0200 p.2; review p.6) -- computed in "
               "the minimal model E_B/E_A < %.4f over k/h in [1e-3, 1e3] (supremum 1/4, approached as k/h -> inf) -- "
               "and gated by the bit at <= c; it forms no substance. A 70 kg payload's rest energy %.4e J would need "
               "an injection above %.4e J at the source under H-MINIMAL. The board's O-SEAT stays OPEN via N_S5 (D68): "
               "QET moves no grade. Hotta 1002.0200v2 p.2 places the extracted energy 'at B even before the start' -- in the "
               "seat's own zero-point fluctuation, read as 'from the seat' -- but it is borrowed: the local energy "
               "left at the seat is -E_B until A's positive energy arrives"
               % (sr["sup"] + 5e-5, bf["payload_rest_J"], bf["payload_rest_J"] / 0.25))
    rq = {
        "reading": "R-QET: the operational reading -- information (Alice's measurement bit) arriving at the destination, "
                   "used there by a local operation conditioned on it, in an entangled ground state, leaves a local "
                   "negative-energy region (the question's parenthetical, now READ)",
        "verdict_on_own_content": "TRUE-IF {H-GROUND, H-CORR, H-ACT, H-INSTANT}; the parenthetical as put to M is "
                                  "INEXACT: the arrival alone creates nothing (computed: <H_B+V> = 0 after the bit "
                                  "arrives and before Bob acts); the conditioned operation does",
        "per": {"O-BITS": "LEFT: QET needs the classical bit (computed: no-signalling, B's reduced state moves by "
                          "<= 1e-15; without the bit no operation extracts, Hotta eq.(5), min change >= 0)",
                "O-MAKE-TOPO": "SILENT: QET makes no topology",
                "O-MAKE-DIST": "SILENT: QET consumes correlation that already exists (Delta S_AB > 0, computed) and "
                               "distributes none",
                "O-HOLD": hold,
                "O-SEAT": seat_ob,
                "O-LOOP": "SILENT: the protocol is causal (Bob's step follows the bit; FMM p.3) and closes no loop"},
        "seat_conditions": seat,
    }
    rl = {
        "reading": "R-LIT: the question's parenthetical read as arrival alone ('information arriving at the "
                   "destination creates a local negative-energy region there'), with no conditioned operation and no "
                   "prior correlation.  M's sentence ('the introduction of information into a space that never "
                   "previously contained it') names an act, and read operationally it is R-QET.  Wave 1 first "
                   "labelled R-LIT 'M's words read alone' (V66-1 #7)",
        "verdict_on_own_content": "FALSE-IF {H-MINIMAL or H-1+1 as the test models, linear QM}: three computed "
                                  "counterexamples -- the bit arrives and Bob does nothing: local energy 0; the bit "
                                  "arrives with no correlation (k = 0): max E_B = 0; a bit uncorrelated with B (eps = "
                                  "1/2): E_B = 0 and any fixed operation costs energy. And the same one bit yields "
                                  "E_B = s * E_B(h, k) under (h, k) -> (s h, s k): information fixes no amount of "
                                  "energy, so information is not itself an energy density of either sign. "
                                  "'Never previously contained': what B held before is the correlation; what is new "
                                  "at B is the classical record (Hotta 1002.0200v2 p.2)",
        "per": {o: "SILENT (its operative content is R-QET's)" for o in OBSTRUCTIONS},
        "seat_conditions": seat,
    }
    return [rq, rl]


# ===================================================================================== report / json
def compute_all(with_spec=True):
    mins = {"%g,%g" % hk: minimal_values(*hk) for hk in IKEDA_ANALYTIC}
    sr = sup_ratio()
    bf = board_figures()
    ft = field_table()
    out = {
        "charter_hypothesis": charter_hypothesis()[0],
        "minimal": mins,
        "sup_E_B_over_E_A": sr,
        "duration_1.5_1": duration(1.5, 1.0),
        "duration_1_1": duration(1.0, 1.0),
        "no_signalling_maxdiff": no_signalling(model(1.5, 1.0)),
        "entanglement": entanglement_table(),
        "bsc": bsc_table(),
        "slope_dEB_dI_bits_1.5_1": slope_at_zero_info(1.5, 1.0),
        "field": ft,
        "board": bf,
        "zachary": zachary_check(),
        "history": HISTORY,
    }
    out["context_dimensional_ratio_1p1_well_over_throat"] = abs(ft["SI_at_d_1m"]["neg_energy_J"]) / bf["throat_deficit_J_1m"]
    if with_spec:
        spec = specthm_verdicts()
        out["specthm"] = spec
        out["grades"] = grades(spec, bf, ft, sr)
    return out


def report():
    d = compute_all()
    print("DOCKET 66 / A3-qet -- H-QET-EXOTIC (not seated)\n")
    print("M (CHARTER):", d["charter_hypothesis"])
    print("\n(A) Hotta's minimal model, (h, k) -> E_A, <V>, <H_1>, <E_1> = local energy at B, E_B, Hotta (8), E_B/E_A")
    for k_, r in d["minimal"].items():
        print("  (%s)  E_A %.4f  V %.4f  H1 %.4f  E1 %.4f  E_B %.4f (Hotta (8) %.4f)  E_B/E_A %.4f" % (
            k_, r["E_A"], r["V"], r["H1"], r["E1_local_at_B"], r["E_B"], r["E_B_hotta8"], r["E_B_over_E_A"]))
    print("  sup E_B/E_A over k/h in [1e-3,1e3]: %.6f at k/h = %.3g" % (d["sup_E_B_over_E_A"]["sup"],
                                                                        d["sup_E_B_over_E_A"]["at_k_over_h"]))
    for key in ("duration_1.5_1", "duration_1_1"):
        r = d[key]
        print("  %s: negative local energy at B lasts t* = %.6f / k by bisection (grid value %.4f; starts at %.4f)"
              % (key, r["t_star_k"], r["t_grid_k"], r["E_local_at_0"]))
    print("  no-signalling: max |rho_B(after Alice) - rho_B(ground)| = %.2e" % d["no_signalling_maxdiff"])
    print("\n  Entanglement consumed (POVM r) vs max E_B, Hotta (12) and (15):")
    for r in d["entanglement"]:
        print("   r %.2f  E_B %.5f (eq.8 %.5f)  dS %.5f nats (eq.10 %.5f)  rhs12 %.5f <= dS  rhs15 %.5f <= E_B" % (
            r["r"], r["max_E_B_numeric"], r["max_E_B_hotta8"], r["dS_nats"], r["dS_formula"], r["rhs12"],
            r["rhs15"]))
    print("\n(B) the bit through a binary symmetric channel (h, k) = (1.5, 1):")
    for r in d["bsc"]:
        print("   eps %.2f  I %.4f bit  E_B %.5f (model units at (h, k) = (1.5, 1); eq.8, q = 1-2eps: %.5f; phi not "
              "re-optimised: %.5f)" % (
            r["eps"], r["I_bits"], r["E_B_numeric"], r["E_B_hotta8_q"], r["E_B_fixed_phi"]))
    print("   dE_B/dI at I -> 0: %.5f per bit; E_B at I = 1 bit: %.5f (model units at (h, k) = (1.5, 1); divide by "
          "h = 1.5 for units of h)" % (d["slope_dEB_dI_bits_1.5_1"], d["bsc"][0]["E_B_numeric"]))
    f = d["field"]
    print("\n(C) 1+1 field QET (hbar = c = 1, unit = Alice's width):", {k: round(v, 6) for k, v in f["well"].items()})
    print("   Flanagan right-moving bound: max achieved/allowed = %.4f (centre %.3f, width %.4f)" % (
        f["flanagan"]["max_ratio"], f["flanagan"]["at_centre"], f["flanagan"]["at_width"]))
    print("   at width 1 m: negative energy %.4e J, seen at a point for %.4e s" % (
        f["SI_at_d_1m"]["neg_energy_J"], f["SI_at_d_1m"]["duration_at_a_point_s"]))
    b = d["board"]
    print("\n(D)-(E) board:", {k: v for k, v in b.items()})
    print("   context (H-1+1-TO-3+1, not a bound): |1+1 well at 1 m| / 1 m throat deficit = %.3e"
          % d["context_dimensional_ratio_1p1_well_over_throat"])
    print("   2506.19878 check:", d["zachary"])
    print("\n(F) grades")
    for g in d["grades"]:
        print("  ", g["reading"])
        print("     own content:", g["verdict_on_own_content"])
        for o in OBSTRUCTIONS:
            print("     %-12s %s" % (o, g["per"][o]))
        print("     seat:", g["seat_conditions"])


# ===================================================================================== selftest
def selftest():
    n = {"pass": 0, "fail": 0, "control": 0, "structural": 0}

    def chk(name, ok, control=False):
        n["pass" if ok else "fail"] += 1
        if control:
            n["control"] += 1
        print(("PASS " if ok else "FAIL ") + ("[CONTROL] " if control else "") + name)

    def structural(name, ok):
        n["structural"] += 1
        print("STRUCTURAL (not counted) %s: %s" % (name, ok))

    # ---------------------------------------------------------------- (A)
    m15 = model(1.5, 1.0)
    g = m15["g"]
    chk("A1 zero-mean ground state: <H_A>, <H_B>, <V>, E_0 all |.| < 1e-12 (Hotta 1002.0200v2 p.3, Ikeda eq.(5))",
        all(abs(float(np.real(g.conj() @ O @ g))) < 1e-12 for O in (m15["HA"], m15["HB"], m15["V"]))
        and abs(m15["E0"]) < 1e-12)
    ok = True
    for (h, k), (e0, v, h1, e1) in IKEDA_ANALYTIC.items():
        r = minimal_values(h, k)
        ok &= all(abs(a - b) < 1.0e-4 for a, b in ((r["E_A"], e0), (r["V"], v), (r["H1"], h1),
                                                    (r["E1_local_at_B"], e1)))
    chk("A2 Ikeda Table II analytic E_0, <V>, <H_1>, <E_1> reproduced within one unit of the last printed digit, all "
        "5 (h, k) (the table truncates rather than rounds in places, and its (1.5, 1) <V> = -0.4905 is its printed "
        "E_1 - H_1; computed -0.490600)", ok)
    r = minimal_values(1.5, 1.0)
    chk("A3 a fixture shifted by 1e-3 is NOT reproduced (the comparison can fail)",
        not abs(r["E1_local_at_B"] - (IKEDA_ANALYTIC[(1.5, 1.0)][3] + 1e-3)) < 1.0e-4, control=True)
    chk("A4 E_B (Ikeda's phi) = Hotta eq.(8) at the projective POVM, all 5 (h, k)",
        all(abs(minimal_values(*hk)["E_B"] - minimal_values(*hk)["E_B_hotta8"]) < 1e-12 for hk in IKEDA_ANALYTIC))
    proj = [(I2 + mu * SX) / 2 for mu in (1, -1)]
    nm = numeric_max_EB(m15, proj)
    chk("A5 numeric max over all mu-dependent SU(2) on B (12 BFGS starts) = Hotta eq.(8) (%.8f vs %.8f)"
        % (nm, r["E_B_hotta8"]), abs(nm - r["E_B_hotta8"]) < 1e-7)
    mi = numeric_min_mu_independent(m15)
    chk("A6 Hotta eq.(5): no mu-INDEPENDENT unitary on B extracts (min energy change %.2e >= -1e-12)" % mi, mi >= -1e-12)
    m_ = model(1.5, 1.0)
    wrong = -ev(qet_state(m_, phi=-phi_opt(1.5, 1.0)), m_["HB"] + m_["V"])
    chk("A7 Bob using the bit with the WRONG sign extracts nothing (E_B %.4f < 0)" % wrong, wrong < 0, control=True)
    ns = no_signalling(m15)
    chk("A8 no-signalling: B's reduced state after Alice's measurement equals the ground's (%.1e)" % ns, ns < 1e-14)
    U2 = expm(-1j * 0.7 * (K(SX, SY) + K(SY, SX)))
    rgl = U2 @ np.outer(g, g.conj()) @ U2.conj().T
    chk("A9 a two-site (non-local) operation DOES move B's reduced state (the no-signalling test can fail)",
        float(np.abs(ptrace_A(rgl) - ptrace_A(np.outer(g, g.conj()))).max()) > 1e-3, control=True)
    loc = ev(post_alice(m15), m15["HB"] + m15["V"])
    chk("A10 the bit has arrived and Bob has not acted: local energy at B = %.1e (|.| < 1e-12) -- arrival alone creates "
        "no negative energy" % loc, abs(loc) < 1e-12)
    m0k = model(1.0, 0.0)
    e0k = numeric_max_EB(m0k, proj, starts=6)
    chk("A11 k = 0 (no ground-state entanglement): max E_B over all conditioned operations = %.1e (<= 1e-10)" % e0k,
        e0k <= 1e-10)
    chk("A12 k > 0 gives E_B > 0 (the k = 0 null can fail)", numeric_max_EB(model(1.0, 0.2), proj, starts=4) > 1e-3,
        control=True)
    sr = sup_ratio()
    chk("A13 E_B <= E_A over k/h in [1e-3, 1e3]; supremum %.6f < 1/4, approached at the grid's end (k/h = %.0f)"
        % (sr["sup"], sr["at_k_over_h"]), sr["sup"] < 0.25 and sr["sup"] > 0.2499 and sr["at_k_over_h"] > 999)
    ok = True
    for t in (0.1, 0.37, 1.3):
        hb, vv = alice_only_evolution(1.5, 1.0, t)
        ok &= abs(hb - 1.5 ** 2 * (1 - math.cos(4 * t)) / (2 * math.hypot(1.5, 1.0))) < 1e-12 and abs(vv) < 1e-12
    chk("A14 Ikeda eq.(A9): after Alice alone <H_1(t)> = h^2(1 - cos 4kt)/(2 sqrt(h^2+k^2)), <V(t)> = 0", ok)
    du = duration(1.5, 1.0)
    chk("A15 the negative local energy at B ends under free evolution at t* k = %.6f, by bisection (in (0, pi/4); "
        "starts at -E_B; V66-2: 0.144941)" % du["t_star_k"], 0 < du["t_star_k"] < math.pi / 4 and
        abs(du["E_local_at_0"] + r["E_B"]) < 1e-12 and abs(du["t_star_k"] - 0.144941) < 5e-6 and abs(du["f_at_t_star"]) < 1e-12)
    du1 = duration(1.0, 1.0)
    chk("A15b at (h, k) = (1, 1), t* k = %.6f (V66-2: 0.185373); wave 1 printed the grid's first point >= 0, 0.1450 "
        "and 0.1855" % du1["t_star_k"], abs(du1["t_star_k"] - 0.185373) < 5e-6)
    chk("A15c CONTROL the grid value wave 1 printed is not the crossing: <H_B + V> there is %.2e, not 0" % du["f_at_grid"],
        abs(du["f_at_grid"]) > 1e-6 and du["t_grid_k"] > du["t_star_k"], control=True)
    et = entanglement_table()
    chk("A16 numeric max E_B = Hotta eq.(8) on the POVM family r in {0.05..1}", all(
        abs(x["max_E_B_numeric"] - x["max_E_B_hotta8"]) < 1e-7 for x in et))
    chk("A17 Delta S_AB from the states = Hotta eqs (9)-(10)", all(abs(x["dS_nats"] - x["dS_formula"]) < 1e-10
                                                                   for x in et))
    chk("A18 Hotta (12): Delta S_AB >= coef * max E_B / sqrt(h^2+k^2), and (15): max E_B >= coef' * Delta S_AB, all r",
        all(x["dS_nats"] >= x["rhs12"] - 1e-12 and x["max_E_B_numeric"] >= x["rhs15"] - 1e-12 for x in et))
    small = et[0]
    chk("A19 Hotta (12) with its coefficient x1.5 FAILS at small r (the inequality is tight as r -> 0)",
        small["dS_nats"] < hotta12_rhs(1.5, 1.0, small["max_E_B_numeric"], 1.5), control=True)
    # ---------------------------------------------------------------- (B)
    bt = bsc_table()
    chk("B1 channel: re-optimised E_B(eps) = Hotta eq.(8) with q/p = 1 - 2eps, all eps", all(
        abs(x["E_B_numeric"] - x["E_B_hotta8_q"]) < 1e-9 for x in bt))
    chk("B2 at I = 0 (eps = 1/2) E_B = 0; E_B increases with I", abs(bt[-1]["E_B_numeric"]) < 1e-12 and all(
        bt[i]["E_B_numeric"] > bt[i + 1]["E_B_numeric"] for i in range(len(bt) - 1)))
    chk("B3 with phi not re-optimised, a noisy bit (eps = 0.4) COSTS energy (E_B %.4f < 0)" % bt[5]["E_B_fixed_phi"],
        bt[5]["E_B_fixed_phi"] < 0, control=True)
    e1 = bsc_row(1.5, 1.0, 0.4999)
    sl = slope_at_zero_info(1.5, 1.0)
    chk("B4 dE_B/dI at I -> 0 = ln2 h^2k^2/((h^2+2k^2) sqrt(h^2+k^2)) = %.6f per bit, model units (numeric %.6f at eps = 0.4999)"
        % (sl, e1["E_B_numeric"] / e1["I_bits"]), abs(e1["E_B_numeric"] / e1["I_bits"] / sl - 1) < 1e-3)
    s3 = minimal_values(4.5, 3.0)["E_B"] / minimal_values(1.5, 1.0)["E_B"]
    chk("B5 same one bit, (h, k) x 3: E_B x %.12f -- information fixes no joules" % s3, abs(s3 - 3.0) < 1e-10)
    # ---------------------------------------------------------------- (C)
    chk("C1 PP integral in closed form (Dawson) = Cauchy quadrature at 4 points",
        all(abs(pp_closed(v, 1.3, 0.8) - pp_numeric(v, 1.3, 0.8)) < 1e-8 for v in (0.0, 0.31, -1.7, 4.2)))
    base = optimise_m0(field_cfg())
    w = well(base)
    chk("C2 the 1+1 QET state has a negative well on Alice's outgoing pulse (min %.5f at v = %.4f)"
        % (w["min_density"], w["v_at_min"]), w["min_density"] < 0 and abs(w["v_at_min"]) < 0.5)
    nos = well(dict(base, sgn=0.0))
    chk("C3 with Alice's information erased (<sigma_y> = 0: Bob's coupling uninformed) the density is >= 0 everywhere",
        nos["min_density"] >= 0, control=True)
    chk("C4 total field energy after the protocol >= 0 (%.5f)" % w["total"], w["total"] > 0)
    chk("C5 causality on the effective support (H-EFF-SUPPORT, 4 widths): Bob's support at T lies inside the future "
        "of Alice's", base["xb"] + 4 * base["db"] <= base["T"] + 4 * base["d"])
    fl = flanagan_test(base, w)
    chk("C6 Flanagan (gr-qc/9706006 eq.(2.5)): the computed right-moving flux obeys the 1+1 QEI on every Gaussian "
        "sampler tried (max achieved/allowed %.4f <= 1)" % fl["max_ratio"], fl["max_ratio"] <= 1.0)
    over = optimise_m0(field_cfg(kqet=10.0))
    flo = flanagan_test(over)
    chk("C7 the QET cross-term inflated x10 (not a state) VIOLATES Flanagan (ratio %.3f > 1): the QEI test can fail"
        % flo["max_ratio"], flo["max_ratio"] > 1.0, control=True)
    e2, e3 = scaling_check(base, 2.0), scaling_check(base, 3.0)
    chk("C8 FMM eq.(34): rho_Ups(x) = Ups^2 rho_1(Ups x) at Ups = 2, 3 (rel. dev. %.1e, %.1e)" % (e2, e3),
        e2 < 1e-9 and e3 < 1e-9)
    c2bad = dict(field_cfg(Ups=2.0), m0=base["m0"] * math.sqrt(2.0))
    v1 = np.linspace(-3, 3, 241)
    dev = float(np.abs(rho_R(v1 / 2.0, c2bad) - 4.0 * rho_R(v1, base)).max() / np.abs(4.0 * rho_R(v1, base)).max())
    chk("C9 the wrong amplitude exponent (mu -> Ups^(1/2) mu) breaks the scaling (dev %.2f)" % dev, dev > 0.05,
        control=True)
    w2 = well(optimise_m0(field_cfg(Ups=2.0)))
    chk("C10 under Ups = 2 the integrated negative energy doubles and the width halves (E x width invariant: %.6f vs %.6f)"
        % (w2["neg_energy"] * w2["neg_width"], w["neg_energy"] * w["neg_width"]),
        abs(w2["neg_energy"] / w["neg_energy"] - 2) < 1e-3 and abs(w2["neg_width"] / w["neg_width"] - 0.5) < 2e-3)
    # ---------------------------------------------------------------- (D)-(E)
    bf = board_figures()
    chk("D1 board: the 1 m throat's deficit wormhole.throat_mass(1) c^2 = 4.8155e42 J (A3-measure prints it)",
        abs(bf["throat_deficit_J_1m"] / 4.8155e42 - 1) < 1e-4)
    chk("D2 board: geometry.r_quantum's fraction is 2.08e-68 (combine's B-HELD)", abs(bf["r_quantum_fraction"] /
                                                                                     2.08e-68 - 1) < 5e-3)
    chk("D3 board: the light time to Proxima (phase1.L_PROXIMA) is 4.2465 yr to 4 decimals and transit.BEATS_LIGHT "
        "is False -- the bit, and so Bob's step, arrives no earlier",
        abs(bf["proxima_light_time_yr"] - 4.2465) < 5e-5 and bf["BEATS_LIGHT"] is False)
    zc = zachary_check()
    chk("D4 2506.19878 App. B.4: its eps does NOT yield its printed dR in SI (8 pi G eps/c^4 = %.3e m^-2; printed 1e-36, "
        "ratio %.2e)" % (zc["dR_SI_m^-2"], zc["printed_over_SI"]), zc["printed_over_SI"] > 1e10)
    # ---------------------------------------------------------------- text and seat
    mw = m_words()
    chk("E1 ledger M-D65-1 carries M's words verbatim", "the introduction of information into a space that never "
                                                       "previously contained it would be considered exotic matter" in mw)
    chk("E2 ledger M-D65-1 records the parenthetical as NOT READ", "not READ" in mw)
    hyp = charter_hypothesis()
    chk("E3 CHARTER carries H-QET-EXOTIC with source M-D65-1", hyp[0] is not None and "M-D65-1" in (hyp[1] or ""))
    spec = specthm_verdicts()
    chk("E4 specthm (z3, run time): S-1 NONEMPTY, S-2 / S-3 / Rec OPEN", spec.get("S-1") == "NONEMPTY" and all(
        spec.get(x) == "OPEN" for x in ("S-2", "S-3", "Rec")))
    chk("E5 specthm: M-S1A-P3 ruled", bool(spec.get("_M-S1A-P3_ruled")))
    gr = grades(spec, bf, None, sr)
    ok = all(any(gr[0]["per"][o].startswith(wd) for wd in VERDICT_WORDS) for o in OBSTRUCTIONS)
    chk("E6 every R-QET grade opens with a B-combine verdict word", ok)
    chk("E7 no grade reads REMOVED or REMOVED-IF (QET removes nothing here) and none reads NOT-BOUND-IF as its own",
        not any(gr[0]["per"][o].startswith("REMOVED") or gr[0]["per"][o].startswith("NOT-BOUND-IF")
                for o in OBSTRUCTIONS))
    structural("the grade text quotes the run-time specthm verdicts and the imported fractions (built from them)", True)
    structural("R-LIT's per-obstruction SILENT is assigned, not computed", True)
    print("\n%d counted checks: %d pass, %d fail; %d controls; %d STRUCTURAL not counted" % (
        n["pass"] + n["fail"], n["pass"], n["fail"], n["control"], n["structural"]))
    return n["fail"] == 0


def _json_safe(x):
    if isinstance(x, dict):
        return {str(k): _json_safe(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_json_safe(v) for v in x]
    if isinstance(x, (np.floating, np.integer)):
        return x.item()
    if isinstance(x, np.ndarray):
        return x.tolist()
    return x


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(_json_safe(compute_all()), indent=1))
    else:
        report()
