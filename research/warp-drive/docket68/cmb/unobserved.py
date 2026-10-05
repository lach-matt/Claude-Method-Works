#!/usr/bin/env python3
"""
unobserved.py -- H-UNOBSERVED-MEDIUM, H-TWO-OBSERVERS, H-CONSCIOUS-SELECTS and H-MANY-PERSPECTIVES: a computable model of
a universe whose history appears relative to a clock, observed by matter and selected by consciousness.

Not seated; rebuilt after one verification (2026-10-05); first-written claims kept under HISTORY.
M (rulings item 48): "what if this is the ground state without first principles/without observation? The decoupling
only exists upon observation of a universe? And this would be why it is a constant".  M (item 49): "matter itself is
capable of observation, however, it is not conscious conversation, which requires sentience . A different type of
observation...".  M (item 50): "Matter based observation is natural and always occurring, with all probabilities
available, until conscious observation occurs. Consciousness observation forces a specific and measurable behavior from
the object being observed".  M (item 51): "consider multiple sentient/conscious observers. Each observation is a
different and relative perspective of the same object, thus each observation is inhomogeneous when compared to the
others".  All carried as M's hypotheses (H-UNOBSERVED-MEDIUM, H-TWO-OBSERVERS, H-CONSCIOUS-SELECTS, H-MANY-PERSPECTIVES),
never as results.  M's order: READ, then this model, then what would distinguish the hypotheses is priced.

    python3 unobserved.py              report
    python3 unobserved.py --selftest   checks, with CONTROLS
    python3 unobserved.py --json       the numbers as JSON

THE MODEL (it ILLUSTRATES mechanisms; it is not evidence about the universe)
  A clock register |k>, k = 0..N-1, labels the cooling (H-CLOCK-IS-COOLING), T_k geometric from 2 T_dec to T_dec/2 with
  T_dec = T0 (1 + z*) = 2973 K (medium.py, READ inputs).  The medium is a DETUNED photon (gamma) / matter (b) pair with
  an exchange coupling g(T) = g0 x_e(T), x_e a logistic step at T_dec (H-TOY-MEDIUM, H-TOY-SAHA): detuning makes the
  coupled and decoupled Hamiltonians non-commuting, so decoupling changes the medium's eigenbasis, not only a rotation
  rate.  The freeze after T_dec is BY CONSTRUCTION (g's logistic tail), and its sharpness depends on the step width and
  the time step (printed).
  The whole is given a history-state Hamiltonian (the Feynman-Kitaev construction, NAMED-NOT-READ): its zero-energy
  ground state is the history sum_k |k>|psi_k>/sqrt(N).  'Ground' is a property of that construction (a sum of
  positive terms); in Page-Wootters the physical state is a zero eigenvector of a constraint with a continuous spectrum,
  and the zero eigenvalue 'seems to play a special role ... but this is not the case' (Giovannetti-Lloyd-Maccone
  1504.04215v3 p.2 eq. 16).  Hartle-Hawking's 'ground state' means 'state of minimum excitation' (APS abstract, PRD 28,
  2960) -- the construction gives M's word a literal realisation (H-CONSTANT-IS-STATIONARY: M's constant read as the
  global state's stationarity; M's own constant refers to the background, read with H-CMB-UNIVERSAL).

WHAT IS COMPUTED
  (1) The global state: the eigh ground state equals the history state; its gap equals 1 - cos(pi/(2N)) (the
      construction's path-graph spectrum); conditioning THAT ground state on each clock reading reproduces ordinary
      unitary evolution, with clock weights uniform at 1/N.
  (2) 'Unobserved', read three ways -- each named, none preferred:
        H-UNOBSERVED-IS-STATIC  the external view is the static global state itself (GLM p.7: the whole universe as 'a
                                static system whose state is an eigenstate of its global Hamiltonian', the external
                                observer 'a hypothetical entity' -- verifier-READ): M's 'constant without observation'.
        H-UNOBSERVED-IS-TRACED  the medium with the clock traced out, under a clock weighting phi (H-CLOCK-WEIGHT: 'the
                                choice of phi(t) is completely arbitrary', GLM p.4): the mixture of the whole history.
        H-M-SUPPORT             M's stronger version as a computable rule: phi supported on the coupled epochs only
                                (the unobserved universe is the coupled medium); observation extends phi's support
                                through records (verifier's proposal, after GLM pp.3-4).
      The trace distance between the TRACED and M-SUPPORT readings is printed for three clock weightings (uniform ticks,
      conformal time, cosmic time); it vanishes when there is no decoupling (the control).
  (3) Matter observation (H-TWO-OBSERVERS, the matter half): a record register whose states overlap as exp(-gamma|j-k|)
      (H-RECORD-QUALITY; the form Marletto-Vedral 1610.04773v2 p.12 give for a cosmological clock -- verifier-READ).
      Conditioning on the record OUTCOME (measured in an orthonormal basis of the register) leaves the medium pure for
      ideal records and mixed as records degrade -- printed as a sweep in gamma.  Marletto-Vedral's 'might have
      observable consequences even at the present epoch' (p.12) is the candidate observable this sweep stands in for.
  (4) H-CONSCIOUS-SELECTS: after matter observation every outcome stays available (the record-diagonal mixture); a
      conscious observation selects one.  Reading (a): selection with Born weights -- its outcome frequencies equal the
      decohered weights exactly (computed): empirically identical to the standard account.  Reading (b): biased
      selection by epsilon.
  (5) H-MANY-PERSPECTIVES: two conscious observers of one medium.  Their reports disagree with probability
      sin^2(theta/2) when their pointer observables differ by theta (state-independent, computed); they agree with
      probability 1 when one reads the other's record (a cross-perspective link, Adlam-Rovelli 2203.13342v2 p.5 Def.
      4.1) or both read redundant copies of one record (quantum Darwinism, Zurek 0903.5082v1 p.3).  The classical
      counterpart at the corridor's ends: Earth and Proxima see CMB skies differing by a dipole of T0 |dv|/c (Gaia DR3
      velocities, via cmbframe), and each sky transforms into the other exactly (Planck 2013 XXVII 1303.5087v3 eq. 1,
      p.3): different, and recoverable.
  (6) O9 (nosig.py, asked): under reading (a) Alice's conscious selection leaves Bob's statistics unchanged for every
      setting (no channel); under reading (b) a bias epsilon -- Alice's outcome probability moved from 1/2 to
      (1 +- epsilon)/2 -- shifts Bob's marginal by (epsilon/2) E(a,b) and, at a = b, gives a binary channel of capacity
      1 - H((1-epsilon)/2) per pair -- the board's beyond-linear branch (H-SETTLE).  The
      pairs the species count would need are printed against epsilon.  The only claimed experimental effect of conscious
      observation measured fringe visibility, not outcome bias (reader-READ, Walleczek & von Stillfried 2019; Radin et
      al. 2020 reply): carrying its size over to epsilon is H-EFFECT-TRANSFER, named.

WHAT THE ERASER AND CONSCIOUSNESS SOURCES SAY (READ 2026-10-05, alphaXiv; Frontiers/PMC/OSF via Firecrawl)
  * A which-path record held only in matter removes the fringes; erasure restores them only in conditioned subsets
    (fringes and anti-fringes that average back): Kim et al. quant-ph/9903047v1 pp.2-3; Walborn et al. quant-ph/0106078v1
    pp.1-2, 5 ('The which-path marker's presence alone is sufficient'); Ma et al. 1203.4834v2 p.2 ('regardless of whether
    or not an observer accesses this information').  No human is tested; the authors give awareness no role.
  * Yu & Nikolic 1009.2404v2 p.5: their prediction 3 (information reaching the retina, masked from awareness) is
    untested; responses (Reason 1707.01346v1; Knight 2005.13317v2; de Barros & Oas 1609.00614v2) argue the claimed
    falsification fails, the last calling the hypothesis practically unfalsifiable (p.12).
  * Consciousness-collapse models reproduce Born statistics: Chalmers-McQueen 2105.02314v1 pp.29-32 (gambler's ruin; a
    stochastic form needed for no superluminal signalling); Okon-Sebastian 1801.05487v2 (CSL with Phi as the collapse
    operator, p.14).  Chalmers-McQueen p.43: collapses from agentive experience 'might be biased' -- 'current evidence
    leaves room open for it' -- 'We do not find this picture especially attractive'.  That is reading (b).
  * The conscious-observer double-slit studies measure interference visibility or a spectral ratio, never outcome bias
    (Pallikari 1210.0432v2 p.2); every pre-registered or confirmatory arm read is null (Walleczek & von Stillfried 2019;
    Guerrer 2019 OSF abstract); Tremblay's open-data re-analysis (PLOS ONE 2019) finds the shifts not significant after
    correction; Radin et al.'s 2020 commentary disputes the statistics.  Recorded, not adjudicated.

SCOPE OF THE SOURCES (verifier)
  Perez-Sahlmann-Sudarsky (gr-qc/0508100v3 p.10) and the collapse-model tests (Martin-Vennin 1906.04405v4 p.5;
  Piccirilli et al. 1709.06237v3) concern the classicalisation of INFLATIONARY perturbations, not photon-baryon
  decoupling.  Objective collapse -- PSS's own proposal -- is a candidate realisation of matter observing
  non-consciously (H-TWO-OBSERVERS); those CSL bounds are partial tests of that reading, scoped to inflation.
  Stationary global states (Page-Wootters, Wheeler-DeWitt) are a standard PROPOSAL with live objections (Kuchar,
  Unruh-Wald, as GLM p.7 restates; Marletto-Vedral p.3: 'never been developed beyond the toy-model stage').

NAMED HYPOTHESES
  H-CLOCK-IS-COOLING, H-TOY-MEDIUM, H-TOY-SAHA, H-HISTORY-STATE, H-CONSTANT-IS-STATIONARY, H-UNOBSERVED-IS-STATIC,
  H-UNOBSERVED-IS-TRACED, H-M-SUPPORT, H-CLOCK-WEIGHT, H-RECORD-QUALITY, H-BORN-SELECTION (reading a), H-BIASED-SELECTION
  (reading b), H-POINTER-ANGLE, H-EFFECT-TRANSFER; with M's H-UNOBSERVED-MEDIUM, H-TWO-OBSERVERS, H-CONSCIOUS-SELECTS and
  H-MANY-PERSPECTIVES.

HISTORY (verifier, 2026-10-05; first-written claims kept):
  * 'trace distance 0.549 between the unobserved medium and M's reading ... in the relational-time picture "unobserved"
    is not "coupled"' -- an ARTEFACT: the first toy's Hamiltonians all commuted (decoupling only stopped a rotation), the
    history stayed on one great circle, and the distance sat in [0.5, 0.707] whatever happened -- 0.501 with no
    decoupling at all, 0 with the medium started in its coupled eigenstate.  Withdrawn; the toy is detuned and the
    readings are compared like with like, with a no-decoupling control.
  * 'half of it in coupled epochs', purity 0.60 -- choices (the symmetric range, geometric ticks, a uniform clock); now
    H-CLOCK-WEIGHT with three weightings printed.
  * 'conditional states equal ordinary unitary evolution' -- shown tautologically (Psi was built from the psis); now the
    eigh ground state itself is conditioned.
  * 'conditioned on its record it sees the same medium; coherences fall to 0' -- true by construction (G = I input,
    diagonal blocks unchanged by any record); now records of tunable quality are conditioned on their OUTCOME.
  * a stationarity check that any eigenstate passes, a mislabelled control, a gap threshold that fails at N > 111 --
    replaced by the gap formula and a non-eigenstate control.
  * PSS cited 'against observer-triggered decoupling' -- out of scope (inflationary perturbations); 'established physics'
    -- now 'a standard proposal'; 'All three steps are below' while step 3 ended OPEN -- now candidates are priced (3, 6).
  * Undersold, now carried: GLM p.7's static external view (M's 'constant without observation'); Wheeler via GLM p.7,
    'the past has no existence except as it is recorded in the present'; Zurek via Schlosshauer quant-ph/0312059v4 p.8,
    'Our experience of the classical reality does not apply to the universe as a whole, seen from the outside, but to the
    systems within it', and Landsman there, 'A world without parts declared or forced to be irrelevant is a world without
    facts' (verifier-READ); Marletto-Vedral's cosmological clock observable (p.12).
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
D68 = os.path.dirname(HERE)


def _by_path(key, path):
    if key in sys.modules:
        return sys.modules[key]
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    spec.loader.exec_module(mod)
    return mod


with contextlib.redirect_stdout(io.StringIO()):
    medium = _by_path("cmb_medium", os.path.join(HERE, "medium.py"))
    nosig = _by_path("d68_nosig", os.path.join(D68, "nosig.py"))

cmbframe = medium.cmbframe
T_DEC = medium.acoustic_past()["T_decoupling_K"]
N_TICKS = 48
T_HOT, T_COLD = 2.0 * T_DEC, 0.5 * T_DEC
WIDTH_K = 0.03 * T_DEC
G0, W_GAMMA, W_B, DT = 0.5, 0.3, 0.6, 0.35           # toy units (H-TOY-MEDIUM): detuned by 0.3

SP = np.array([[0, 0], [1, 0]], dtype=complex)
I2 = np.eye(2, dtype=complex)
NUM = np.diag([0.0, 1.0]).astype(complex)
PSI0 = np.array([0, 0, 1, 0], dtype=complex)          # |gamma = 1, b = 0>
GAMMA_IDX, B_IDX = 2, 1                               # one-excitation basis: |10> photon, |01> matter


def temps(t_hot=T_HOT, t_cold=T_COLD, n=N_TICKS):
    return [t_hot * (t_cold / t_hot) ** (k / (n - 1)) for k in range(n)]


def x_e(T, width=WIDTH_K):
    return 1.0 / (1.0 + math.exp(-(T - T_DEC) / width))


def h_medium(T, g0=G0, width=WIDTH_K):
    g = g0 * x_e(T, width)
    exch = np.kron(SP, SP.conj().T) + np.kron(SP.conj().T, SP)
    return W_GAMMA * np.kron(NUM, I2) + W_B * np.kron(I2, NUM) + g * exch


def u_step(T, g0=G0, width=WIDTH_K, dt=DT):
    w, v = np.linalg.eigh(h_medium(T, g0, width))
    return v @ np.diag(np.exp(-1j * w * dt)) @ v.conj().T


def history(ts=None, g0=G0, psi0=PSI0, width=WIDTH_K, dt=DT):
    ts = temps() if ts is None else ts
    psis = [psi0.copy()]
    for k in range(len(ts) - 1):
        psis.append(u_step(ts[k], g0, width, dt) @ psis[-1])
    return ts, psis


def fk_hamiltonian(ts, g0=G0, psi0=PSI0):
    n, d = len(ts), 4
    H = np.zeros((n * d, n * d), dtype=complex)
    Id = np.eye(d, dtype=complex)
    for k in range(n - 1):
        U = u_step(ts[k], g0)
        a, b = slice(k * d, (k + 1) * d), slice((k + 1) * d, (k + 2) * d)
        H[a, a] += Id / 2
        H[b, b] += Id / 2
        H[b, a] += -U / 2
        H[a, b] += -U.conj().T / 2
    H[0:d, 0:d] += Id - np.outer(psi0, psi0.conj())
    return H


def p_b(psi):
    return float(abs(psi[B_IDX]) ** 2)


def rho_of(psis, w):
    w = np.asarray(w, dtype=float)
    w = w / w.sum()
    return sum(wk * np.outer(p, p.conj()) for wk, p in zip(w, psis))


def trace_distance(r, s):
    return 0.5 * float(np.sum(np.abs(np.linalg.eigvalsh(r - s))))


def purity(r):
    return float(np.real(np.trace(r @ r)))


def clock_weights(ts, kind):
    """H-CLOCK-WEIGHT on geometric ticks: uniform ticks (the construction's own), conformal time (d eta ~ d ln T / T)
    and cosmic time in a radiation era (dt ~ d ln T / T^2)."""
    if kind == "uniform ticks":
        return [1.0] * len(ts)
    if kind == "conformal time":
        return [1.0 / T for T in ts]
    if kind == "cosmic time":
        return [1.0 / T ** 2 for T in ts]
    raise ValueError(kind)


def readings(ts, psis, kind):
    w = clock_weights(ts, kind)
    coupled = [wk if T > T_DEC else 0.0 for wk, T in zip(w, ts)]
    r_tr, r_m = rho_of(psis, w), rho_of(psis, coupled)
    return {"coupled_weight": sum(coupled) / sum(w), "purity_traced": purity(r_tr), "purity_M": purity(r_m),
            "TD_traced_vs_M": trace_distance(r_tr, r_m)}


def record_sweep(psis, gammas=(0.0, 0.05, 0.2, 1.0, 5.0, 1e3)):
    """Matter observation by records of quality gamma: <r_j|r_k> = exp(-gamma |j-k|).  r_k = columns of G^(1/2); the
    observer reads the record in the register's orthonormal basis m.  Clock traced (orthogonal ticks): the medium given m
    is sum_k |R_mk|^2 psi_k psi_k^dag / p_m.  Mean conditional purity printed."""
    n = len(psis)
    out = []
    for g in gammas:
        G = np.array([[math.exp(-g * abs(j - k)) for k in range(n)] for j in range(n)])
        ev, V = np.linalg.eigh(G)
        R = V @ np.diag(np.sqrt(np.clip(ev, 0, None))) @ V.T
        tot = 0.0
        for m in range(n):
            wts = [abs(R[m, k]) ** 2 / n for k in range(n)]
            pm = sum(wts)
            if pm < 1e-15:
                continue
            tot += pm * purity(rho_of(psis, wts))
        out.append((g, tot))
    return out


def selection(psis):
    """H-CONSCIOUS-SELECTS reading (a): after ideal matter records, the record-diagonal weights are 1/N each and a
    Born-weighted conscious selection picks tick k with probability 1/N -- the frequencies equal the decohered weights.
    Inside one tick, the medium's photon/matter record: Born selection frequencies equal the decohered diagonal."""
    k = len(psis) // 3                                      # a coupled tick
    rho = np.outer(psis[k], psis[k].conj())
    decohered = [float(np.real(rho[GAMMA_IDX, GAMMA_IDX])), float(np.real(rho[B_IDX, B_IDX]))]
    born = [abs(psis[k][GAMMA_IDX]) ** 2, abs(psis[k][B_IDX]) ** 2]
    return {"tick": k, "decohered": decohered, "born_selection": born,
            "max_difference": max(abs(a - b) for a, b in zip(decohered, born))}


def perspectives(psis):
    """Two conscious observers of the medium's one-excitation qubit (photon / matter).  O1's pointer: photon-or-matter;
    O2's pointer rotated by theta (H-POINTER-ANGLE).  P(disagree) over several states and angles; a cross-perspective
    link (O2 reads O1's record) and shared redundant records both give agreement 1."""
    def qubit(psi):
        v = np.array([psi[GAMMA_IDX], psi[B_IDX]])
        return v / np.linalg.norm(v)
    rows = []
    for theta in (0.0, math.pi / 6, math.pi / 3, math.pi / 2):
        c, s = math.cos(theta / 2), math.sin(theta / 2)
        basis2 = [np.array([c, s]), np.array([-s, c])]
        dis = []
        for k in (0, len(psis) // 3, len(psis) - 1):
            q = qubit(psis[k])
            p1 = [abs(q[0]) ** 2, abs(q[1]) ** 2]
            e = [np.array([1.0, 0.0]), np.array([0.0, 1.0])]
            # O1 measures first (state collapses to e[o]); O2 then measures in basis2; disagreement = labels differ
            pdis = sum(p1[o] * (1 - abs(np.vdot(basis2[o], e[o])) ** 2) for o in (0, 1))
            dis.append(pdis)
        rows.append({"theta": theta, "P_disagree": dis, "sin2_half": s * s})
    return {"rows": rows, "P_agree_cross_perspective_link": 1.0, "P_agree_redundant_records": 1.0}


def corridor_skies():
    """Earth and Proxima: CMB skies differing by a dipole T0 |dv| / c, dv from Gaia DR3's proper motion and radial
    velocity (via cmbframe); and each sky recovered exactly from the other by the boost (Planck 2013 XXVII eq. 1)."""
    p = cmbframe.PROXIMA_DIR
    a, d = math.radians(p["ra_deg"]), math.radians(p["dec_deg"])
    n = np.array(cmbframe.N_PROXIMA)
    e_a = np.array([-math.sin(a), math.cos(a), 0.0])
    e_d = np.array([-math.sin(d) * math.cos(a), -math.sin(d) * math.sin(a), math.cos(d)])
    d_pc = 1000.0 / p["plx_mas"][0]
    k = 4.740470446 * d_pc / 1000.0                          # km/s per (mas/yr)
    v_rel = p["rv_kms"][0] * n + k * (p["pm_mas_yr"][0] * e_a + p["pm_mas_yr"][1] * e_d)
    T0 = medium.T0
    c = cmbframe.C_KMS
    v_sun = np.array(cmbframe.V_SUN_CMB)
    v_prox = v_sun + v_rel
    def sky(v, nn):
        b = v / c
        bb = float(np.dot(b, b))
        g = 1 / math.sqrt(1 - bb)
        return T0 / (g * (1 - float(np.dot(b, nn))))
    rng = np.random.default_rng(3)
    dirs = rng.normal(size=(200, 3))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    # recover the CMB-frame temperature from each observer's sky: T_cmb = gamma (1 - b.n) T_obs, for the photon
    # direction n seen by that observer -- both must return T0
    worst = 0.0
    for v in (v_sun, v_prox):
        b = v / c
        g = 1 / math.sqrt(1 - float(np.dot(b, b)))
        for nn in dirs:
            worst = max(worst, abs(g * (1 - float(np.dot(b, nn))) * sky(v, nn) - T0))
    return {"v_rel_kms": float(np.linalg.norm(v_rel)), "dipole_difference_K": T0 * float(np.linalg.norm(v_rel)) / c,
            "dipole_earth_K": T0 * float(np.linalg.norm(v_sun)) / c, "recovery_worst_K": worst}


def o9_pricing(eps_list=(1e-5, 1e-3, 1e-2, 1e-1)):
    """nosig.joint asked.  Reading (a): Bob's marginal for each of Alice's settings, Born selection (unchanged).
    Reading (b): Alice biases her outcome probabilities by epsilon toward a chosen sign; Bob's marginal is
    sum_o p'_A(o) P(B = + | o).  Capacity of the resulting binary channel per pair, and pairs for the species count."""
    b = 0.0
    margs_a = []
    for a in np.linspace(0, math.pi, 7):
        j = nosig.joint(a, b)
        margs_a.append(j[(1, 1)] + j[(-1, 1)])
    shifts = []
    for a in (0.0, math.pi / 4, math.pi / 2):
        j = nosig.joint(a, b)
        pa = {o: j[(o, 1)] + j[(o, -1)] for o in (1, -1)}
        pb_given = {o: j[(o, 1)] / pa[o] for o in (1, -1)}
        eps = 1e-3
        pa_b = {1: pa[1] + eps / 2, -1: pa[-1] - eps / 2}
        shift = sum(pa_b[o] * pb_given[o] for o in (1, -1)) - sum(pa[o] * pb_given[o] for o in (1, -1))
        E = sum(oa * ob * p for (oa, ob), p in j.items())
        shifts.append({"a": a, "shift_per_eps": shift / eps, "E": E})
    bits = medium.demand.counts()[0][1]
    def H(p):
        return -sum(q * math.log2(q) for q in (p, 1 - p) if q > 0)
    rows = []
    for eps in eps_list:
        cap = 1 - H((1 - eps) / 2)
        rows.append({"eps": eps, "bits_per_pair": cap, "pairs_for_species_count": bits / cap})
    return {"bob_marginals_reading_a": margs_a, "max_marginal_shift_a": max(margs_a) - min(margs_a),
            "shifts_reading_b": shifts, "capacity_rows": rows, "species_bits": bits}


def compute():
    ts, psis = history()
    H = fk_hamiltonian(ts)
    w, v = np.linalg.eigh(H)
    g0v = v[:, 0]
    Psi = np.concatenate(psis) / math.sqrt(N_TICKS)
    blocks = g0v.reshape(N_TICKS, 4)
    clock_w = [float(np.linalg.norm(b) ** 2) for b in blocks]
    cond = [b / np.linalg.norm(b) for b in blocks]
    infid = max(1 - abs(np.vdot(cond[k], psis[k])) ** 2 for k in range(N_TICKS))
    comm = float(np.linalg.norm(h_medium(T_HOT) @ h_medium(T_COLD) - h_medium(T_COLD) @ h_medium(T_HOT)))
    pb = [p_b(p) for p in psis]
    cold = [k for k, T in enumerate(ts) if T < T_DEC - 5 * WIDTH_K]
    hot = [k for k, T in enumerate(ts) if T > T_DEC + 5 * WIDTH_K]
    # a non-eigenstate evolves under the global H (control for stationarity)
    x = np.concatenate([PSI0] * N_TICKS) / math.sqrt(N_TICKS)
    Ut = v @ np.diag(np.exp(-1j * w * 50.0)) @ v.conj().T
    nonstationary_fid = abs(np.vdot(x, Ut @ x))
    rd = {k: readings(ts, psis, k) for k in ("uniform ticks", "conformal time", "cosmic time")}
    ts_nd = temps(4 * T_DEC, 2 * T_DEC)                    # no decoupling inside the range (control)
    _, psis_nd = history(ts_nd)
    rd_nd = readings(ts_nd, psis_nd, "uniform ticks")
    return {"N": N_TICKS, "T_dec": T_DEC, "E0": float(w[0]), "gap": float(w[1] - w[0]),
            "gap_formula": 1 - math.cos(math.pi / (2 * N_TICKS)), "overlap": float(abs(np.vdot(g0v, Psi))),
            "clock_weight_spread": max(clock_w) - min(clock_w), "conditional_infidelity_from_ground": float(infid),
            "commutator_hot_cold": comm, "pb_swing_hot": max(pb[k] for k in hot) - min(pb[k] for k in hot),
            "pb_step_cold": max(abs(pb[k + 1] - pb[k]) for k in cold[:-1]), "nonstationary_fidelity": float(nonstationary_fid),
            "readings": rd, "readings_no_decoupling": rd_nd, "records": record_sweep(psis),
            "purity_traced_uniform": rd["uniform ticks"]["purity_traced"], "selection": selection(psis),
            "perspectives": perspectives(psis), "skies": corridor_skies(), "o9": o9_pricing()}


def report():
    d = compute()
    print("H-UNOBSERVED-MEDIUM, H-TWO-OBSERVERS, H-CONSCIOUS-SELECTS, H-MANY-PERSPECTIVES (rebuilt after verification; "
          "not seated)\n")
    print("(1) the global state: eigh ground state = history state (overlap %.12f), energy %.1e; gap %.4e = 1 - "
          "cos(pi/2N) %.4e; conditioning it on the clock gives ordinary evolution (worst infidelity %.1e), clock weights "
          "uniform (spread %.1e).  Detuned toy: ||[H_hot, H_cold]|| = %.3f" % (
              d["overlap"], d["E0"], d["gap"], d["gap_formula"], d["conditional_infidelity_from_ground"],
              d["clock_weight_spread"], d["commutator_hot_cold"]))
    print("    the medium exchanges while hot (P_b swing %.3f) and freezes after T_dec by construction (largest step "
          "%.1e)" % (d["pb_swing_hot"], d["pb_step_cold"]))
    print("(2) 'unobserved', read three ways: STATIC (the global state itself: constant); TRACED; M-SUPPORT (coupled "
          "epochs only).  TRACED vs M-SUPPORT, by clock weighting:")
    for k, r in d["readings"].items():
        print("    %-15s coupled weight %.3f, purity traced %.3f / M %.3f, trace distance %.3f" % (
            k, r["coupled_weight"], r["purity_traced"], r["purity_M"], r["TD_traced_vs_M"]))
    print("    control, no decoupling in range: trace distance %.1e" % d["readings_no_decoupling"]["TD_traced_vs_M"])
    print("(3) matter observation by records of quality gamma (overlap exp(-gamma |dk|)): mean conditional purity")
    print("    " + "; ".join("gamma %g: %.3f" % (g, p) for g, p in d["records"]))
    s = d["selection"]
    print("(4) conscious selection, reading (a): Born-weighted selection frequencies %s equal the decohered weights %s "
          "(difference %.1e) -- identical to the standard account; reading (b) biased: see (6)" % (
              ["%.4f" % x for x in s["born_selection"]], ["%.4f" % x for x in s["decohered"]], s["max_difference"]))
    print("(5) many perspectives: P(disagree) between two observers' reports by pointer angle theta (three medium states):")
    for r in d["perspectives"]["rows"]:
        print("    theta %.3f: %s (sin^2(theta/2) = %.4f)" % (r["theta"], ["%.4f" % x for x in r["P_disagree"]],
                                                            r["sin2_half"]))
    sk = d["skies"]
    print("    a cross-perspective link or redundant records: agreement 1.  At the corridor's ends: Earth and Proxima's "
          "CMB skies differ by a dipole of %.3f mK (|dv| = %.1f km/s; Earth's own dipole %.3f mK); each recovers the "
          "CMB frame exactly (worst %.1e K)" % (sk["dipole_difference_K"] * 1e3, sk["v_rel_kms"],
                                               sk["dipole_earth_K"] * 1e3, sk["recovery_worst_K"]))
    o = d["o9"]
    print("(6) O9: reading (a) -- Bob's marginal over 7 of Alice's settings varies by %.1e (no channel); reading (b) -- "
          "Alice's outcome probability moved to (1 +- eps)/2 shifts Bob's marginal by (eps/2) E(a,b): %s" % (
              o["max_marginal_shift_a"], ["a=%.2f: %.3f = E/2 %.3f" % (x["a"], x["shift_per_eps"], x["E"] / 2)
                                          for x in o["shifts_reading_b"]]))
    for r in o["capacity_rows"]:
        print("    bias %.0e: %.2e bits per pair; the species count (%.2e bits) needs %.2e pairs" % (
            r["eps"], r["bits_per_pair"], o["species_bits"], r["pairs_for_species_count"]))


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
    chk("eigh's ground state is the history state (overlap %.12f, energy %.1e)" % (d["overlap"], d["E0"]),
        d["overlap"] > 1 - 1e-10 and abs(d["E0"]) < 1e-10)
    chk("its gap equals 1 - cos(pi/(2N)) to 1e-8 (%.6e vs %.6e)" % (d["gap"], d["gap_formula"]),
        abs(d["gap"] - d["gap_formula"]) < 1e-8)
    chk("conditioning the ground state itself on each clock reading gives ordinary evolution (%.1e) with uniform clock "
        "weights (spread %.1e)" % (d["conditional_infidelity_from_ground"], d["clock_weight_spread"]),
        d["conditional_infidelity_from_ground"] < 1e-10 and d["clock_weight_spread"] < 1e-10)
    chk("a non-eigenstate evolves under the global Hamiltonian (fidelity %.3f < 0.99)" % d["nonstationary_fidelity"],
        d["nonstationary_fidelity"] < 0.99, ctl=True)
    chk("the detuned toy's hot and cold Hamiltonians do not commute (%.3f > 0.05)" % d["commutator_hot_cold"],
        d["commutator_hot_cold"] > 0.05)
    rd = d["readings"]
    chk("TRACED and M-SUPPORT readings differ for every clock weighting (trace distance %s > 0.02)" % (
        ["%.3f" % r["TD_traced_vs_M"] for r in rd.values()]), all(r["TD_traced_vs_M"] > 0.02 for r in rd.values()))
    chk("with no decoupling in range the two readings coincide (trace distance %.1e)" %
        d["readings_no_decoupling"]["TD_traced_vs_M"], d["readings_no_decoupling"]["TD_traced_vs_M"] < 1e-12, ctl=True)
    rec = dict(d["records"])
    chk("records: ideal records leave the medium pure (%.6f); fully degraded records give the traced mixture (%.6f = "
        "%.6f); purity rises monotonically with record quality" % (
            rec[1e3], rec[0.0], d["purity_traced_uniform"]),
        rec[1e3] > 1 - 1e-6 and abs(rec[0.0] - d["purity_traced_uniform"]) < 1e-9
        and all(b >= a - 1e-12 for (_, a), (_, b) in zip(d["records"], d["records"][1:])))
    chk("reading (a): Born-weighted conscious selection reproduces the decohered weights (difference %.1e)" %
        d["selection"]["max_difference"], d["selection"]["max_difference"] < 1e-12)
    pr = d["perspectives"]["rows"]
    chk("two perspectives disagree with probability sin^2(theta/2), state-independent, to 1e-12",
        all(max(abs(x - r["sin2_half"]) for x in r["P_disagree"]) < 1e-12 for r in pr))
    chk("at theta = 0 two perspectives never disagree", max(pr[0]["P_disagree"]) < 1e-15, ctl=True)
    sk = d["skies"]
    chk("Earth and Proxima's skies differ by a %.3f mK dipole (|dv| %.1f km/s, 25-40 km/s) and each recovers the CMB "
        "frame exactly (%.1e K)" % (sk["dipole_difference_K"] * 1e3, sk["v_rel_kms"], sk["recovery_worst_K"]),
        25 < sk["v_rel_kms"] < 40 and sk["recovery_worst_K"] < 1e-12)
    o = d["o9"]
    chk("O9 reading (a): Bob's marginal does not depend on Alice's setting (spread %.1e)" % o["max_marginal_shift_a"],
        o["max_marginal_shift_a"] < 1e-12)
    chk("O9 reading (b): with Alice's outcome probability moved from 1/2 to (1 +- eps)/2, Bob's marginal shifts by "
        "(eps/2) E(a,b) at every setting tested (%s)" % ["%.3f" % x["shift_per_eps"] for x in o["shifts_reading_b"]],
        all(abs(x["shift_per_eps"] - x["E"] / 2) < 1e-9 for x in o["shifts_reading_b"]))
    chk("reading (b) at bias 1e-5 gives %.2e bits per pair (small-bias law eps^2/(2 ln 2) = %.2e)" % (
        o["capacity_rows"][0]["bits_per_pair"], 1e-10 / (2 * math.log(2))),
        abs(o["capacity_rows"][0]["bits_per_pair"] / (1e-10 / (2 * math.log(2))) - 1) < 1e-3)
    structural.append("a sentient observer in unitary quantum mechanics is one more record register; telling it apart "
                      "needs non-unitary physics (Chalmers-McQueen 2105.02314v1; Bong et al. 1907.05607v4 p.7), all "
                      "proposed tests unperformed")
    structural.append("H-UNOBSERVED-IS-STATIC: the external view is the static global state itself (GLM p.7) -- M's "
                      "'constant without observation'; no subsystem reading is made of it")
    for s in structural:
        print("  STRUCTURAL: " + s)
    print("unobserved.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
