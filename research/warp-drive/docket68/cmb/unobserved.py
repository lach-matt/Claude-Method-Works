#!/usr/bin/env python3
"""
unobserved.py -- H-UNOBSERVED-MEDIUM, H-TWO-OBSERVERS, H-CONSCIOUS-SELECTS and H-MANY-PERSPECTIVES: a computable model of
a universe whose history appears relative to a clock, recorded by matter and selected by consciousness.

Not seated; verified twice (2026-10-05), the second verification's findings applied here; first-written claims kept
under HISTORY.  M (rulings item 48): "what if this is the ground state without first principles/without observation?
The decoupling only exists upon observation of a universe? And this would be why it is a constant".  M (item 49):
"matter itself is capable of observation, however, it is not conscious conversation, which requires sentience . A
different type of observation...".  M (item 50): "Matter based observation is natural and always occurring, with all
probabilities available, until conscious observation occurs. Consciousness observation forces a specific and measurable
behavior from the object being observed".  M (item 51): "consider multiple sentient/conscious observers. Each
observation is a different and relative perspective of the same object, thus each observation is inhomogeneous when
compared to the others".  Carried as M's hypotheses (H-UNOBSERVED-MEDIUM, H-TWO-OBSERVERS, H-CONSCIOUS-SELECTS,
H-MANY-PERSPECTIVES), never as results.  H-LOCAL-CLOCK (items 52-53) is localclock.py's.

    python3 unobserved.py              report
    python3 unobserved.py --selftest   checks, with CONTROLS
    python3 unobserved.py --json       the numbers as JSON

THE MODEL (it ILLUSTRATES mechanisms; it is not evidence about the universe)
  A clock register |k> labels the cooling (H-CLOCK-IS-COOLING), T_k geometric from 2 T_dec to T_dec/2, T_dec = T0 (1 +
  z*) = 2973 K (medium.py).  The medium: a detuned photon (gamma) / matter (b) pair with exchange g(T) = g0 x_e(T), x_e a
  logistic step at T_dec (H-TOY-MEDIUM, H-TOY-SAHA); the freeze after T_dec is BY CONSTRUCTION.  The medium STARTS in
  the coupled medium's own one-excitation ground state at T_hot (H-START-COUPLED-GROUND): M's 'ground state', read
  literally -- stationary for as long as the coupling holds.  The photon start is kept as a second case.
  The whole has a history-state (Feynman-Kitaev, NAMED-NOT-READ) Hamiltonian whose zero-energy ground state is the
  history; 'ground' is a property of that construction (H-CONSTANT-IS-STATIONARY maps M's constant onto it).

WHAT IS COMPUTED
  (1) The global state: eigh's ground state is the history state; gap = 1 - cos(pi/(2N)); conditioning THAT ground state
      on the clock gives ordinary evolution with uniform clock weights.
  (2) 'Unobserved', three readings, none preferred: STATIC (the global state; GLM 1504.04215v3 p.7, verifier-READ);
      TRACED (clock traced under a weighting phi, H-CLOCK-WEIGHT: 'completely arbitrary', GLM p.4); M-SUPPORT (phi on the
      coupled epochs only -- from the coupled ground state it is pure and stationary: M's reading, literally).  The
      TRACED vs M-SUPPORT trace distance for three weightings, against the REAL control (same range, constant coupling:
      no decoupling), which gives exactly 0 from the coupled ground state.  From the photon start the control is not 0
      (the window itself contributes): both are printed, with the decomposition.
  (3) Records of the EPOCH held in matter, read by a reader (H-RECORD-QUALITY: overlaps exp(-gamma|j-k|), Marletto-
      Vedral 1610.04773v2 p.12 form, verifier-READ; H-READOUT-BASIS: the reader's basis).  The medium's UNCONDITIONAL
      state is unchanged by any record (computed, every gamma): matter records keep every probability available -- M's
      first clause of item 50.  Purity appears only on conditioning on an outcome, and depends on the readout basis (two
      printed); the readout-independent content is the records' Holevo information chi = S(G/N), printed.
  (4) Conscious selection (H-CONSCIOUS-SELECTS).  Born selection AFTER matter records changes no later statistic
      (STRUCTURAL, by linearity); selection BEFORE records -- on the coherent state -- changes interference (computed):
      the in-principle difference Chalmers-McQueen's tests target (2105.02314v1 abstract p.1: 'Simple versions ... are
      falsified by the quantum Zeno effect, but more complex versions remain compatible ... can be tested by
      experiments with quantum computers').  Reading (b), biased selection, is priced in (6).
  (5) Many perspectives (H-MANY-PERSPECTIVES).  Sequential model (H-SEQUENTIAL) with nearest-label pairing
      (H-LABEL-MATCH): two observers disagree with probability sin^2(theta/2), theta the Bloch angle between their pointer
      observables -- state-independent BY CONSTRUCTION of the sequential model; the independent-copies model gives a
      state-dependent p(1-q) + (1-p)q (printed).  Agreement through a record is COMPUTED: a CNOT copy read in the
      record's basis (a cross-perspective link, Adlam-Rovelli 2203.13342v2 p.5 Def. 4.1 -- a postulate there), and two
      redundant copies (quantum Darwinism, Zurek 0903.5082v1 p.3) give agreement 1.  At the corridor's ends: Earth and
      Proxima's CMB skies differ by a 0.29 mK dipole; Proxima's sky built by boosting the Sun's sky (aberration and
      Doppler, photon 4-momenta) is a pure boosted blackbody whose speed equals the relativistic composition of the two
      velocities -- a real recoverability check -- and differs from the Galilean v_sun + v_rel at order v^2/c^2.  Earth's
      own annual motion (~30 km/s, Planck 1303.5087v3 p.2) modulates the sky by about as much as the Sun-Proxima
      difference: one observer's perspective already varies that much in a year.
  (6) O9 (nosig.py, asked).  Reading (a): Bob's marginal is independent of Alice's setting.  Reading (b): a bias moving
      Alice's outcome probability from 1/2 to (1 +- eps)/2, keeping the conditional correlations (H-BIAS-KEEPS-
      CORRELATION), shifts Bob's marginal by (eps/2) E(a,b); at a = b a binary channel of 1 - H((1-eps)/2) bits per pair.
      No willed bias is needed: a fixed bias toward '+' with Alice switching between a = b and a = b + pi gives the same
      capacity (computed).  Reading (b) is a beyond-Born sub-branch of the board's beyond-linear branch, DISTINCT from
      H-SETTLE's deterministic drift; settle.py's collapse control (D: a Born/Lindblad stochastic collapse must NOT
      signal) corroborates reading (a).

WHAT THE SOURCES SAY (READ; verifier-READ where marked)
  * Eraser experiments: a which-path record held only in matter removes the fringes; erasure restores them only in
    conditioned subsets (Kim et al. quant-ph/9903047v1; Walborn et al. quant-ph/0106078v1; Ma et al. 1203.4834v2 p.2:
    'regardless of whether or not an observer accesses this information').
  * Consciousness-collapse models reproduce Born statistics (Chalmers-McQueen 2105.02314v1 pp.29-32; Okon-Sebastian
    1801.05487v2).  Chalmers-McQueen p.43: perhaps perceptual consciousness obeys the constraints but 'agentive
    experience does not'; collapses from it 'might be biased'; 'it is arguable that our current evidence leaves room open
    for it'; 'We do not find this picture especially attractive' (verifier-READ).  Their bias is AGENTIVE; perceptual
    observation stays Born -- so it fits M's 'conscious observation forces' only in part, and fits O9's scenario (Alice
    acts).
  * Outcome bias by intention HAS been studied: Bosch, Steinkamp & Boller 2006 (Psychol. Bull. 132, 497; public APA
    abstract, verifier-READ): 380 studies, 'a significant but very small overall effect size', strongly inversely related
    to sample size, which 'could in principle be a result of publication bias'; Radin et al. 2006 replied (title only).
    Its effect size is not yet READ -- pricing eps at it is OPEN.  The double-slit attention studies measure interference
    visibility, not outcome bias; their pre-registered arms are null (Walleczek & von Stillfried 2019; Guerrer 2019);
    Tremblay's open-data re-analysis finds no significance after correction; Radin et al. 2020 dispute the statistics.
  * Many perspectives: QBism -- 'reality differs from one agent to another ... What is real for an agent rests entirely
    on what that agent experiences' (Fuchs-Mermin-Schack 1311.5253v1 p.3) and 'An outcome is created for the agent ...
    only when it enters the experience of that agent' (p.4) (verifier-READ).  The no-go theorems (Brukner 1804.00749v1;
    Frauchiger-Renner 1604.07422v2; Bong et al. 1907.05607v4) support observer-relative facts CONDITIONALLY: if quantum
    theory holds at the scale of observers, absoluteness of observed events is one candidate to drop.  Balance:
    Adlam-Rovelli (p.9) -- with their postulate 'we will never have a case where a physical variable takes two different
    values relative to different observers'; only the assigned states differ.
  * Scope: Perez-Sahlmann-Sudarsky (gr-qc/0508100v3 p.10) and the CSL tests concern INFLATIONARY perturbations, not
    photon-baryon decoupling; objective collapse (PSS's proposal) is a candidate realisation of matter observing
    non-consciously.  Stationary global states are a standard PROPOSAL with live objections (Kuchar, Unruh-Wald, as GLM
    p.7 restates).

NAMED HYPOTHESES
  H-CLOCK-IS-COOLING, H-TOY-MEDIUM, H-TOY-SAHA, H-START-COUPLED-GROUND, H-HISTORY-STATE, H-CONSTANT-IS-STATIONARY,
  H-UNOBSERVED-IS-STATIC, H-UNOBSERVED-IS-TRACED, H-M-SUPPORT, H-CLOCK-WEIGHT, H-RECORD-QUALITY, H-READOUT-BASIS,
  H-BORN-SELECTION, H-BIASED-SELECTION, H-BIAS-KEEPS-CORRELATION, H-SEQUENTIAL, H-LABEL-MATCH, H-EFFECT-TRANSFER; with
  M's H-UNOBSERVED-MEDIUM, H-TWO-OBSERVERS, H-CONSCIOUS-SELECTS and H-MANY-PERSPECTIVES.

HISTORY (two verifications, 2026-10-05; first-written claims kept)
  First build: 'trace distance 0.549 ... "unobserved" is not "coupled"' -- an artefact (commuting toy, photon start);
  'half in coupled epochs' a choice; conditional-state and record checks tautological.  Withdrawn.
  Second build:
  * 'with no decoupling in range the two readings coincide exactly, so the difference measures decoupling' -- the
    control (all ticks above T_dec) passed BY DEFINITION; with the photon start a real control (constant coupling, same
    range) gives 0.098 / 0.138 / 0.186, so the distance partly measured the window.  Now the coupled-ground start, whose
    real control is exactly 0, with the photon start's decomposition printed.
  * 'matter observation ... leaves the medium pure for ideal records' -- mislabelled: the unconditional state never
    changes; purity came from a reader conditioning, and depended on the readout basis (G^(1/2) vs Fourier: 0.78 vs
    0.60 at gamma 0.05).  Relabelled; chi printed.
  * selection() reading (a) -- a tautology (|amplitude|^2 against the same diagonal); now STRUCTURAL, with the
    before/after-records interference computation in its place.  'empirically identical to the standard account' --
    only in Born frequencies; Chalmers-McQueen's simple versions are already falsified by the Zeno argument.
  * perspectives: 'state-independent' held by construction; 'agreement 1' was a hard-coded literal -- now computed.
  * corridor_skies: the recovery check inverted the same formula (a tautology) -- replaced by the boosted-sky check;
    'Earth's own dipole 3.362 mK' is the Sun's (barycentre's).
  * reading (b) called 'the board's beyond-linear branch (H-SETTLE)' -- H-SETTLE is a deterministic drift; reading (b) is
    a stochastic beyond-Born rule.  'No outcome bias has been measured' -- wrong: the RNG meta-analysis above.  The
    Chalmers-McQueen p.43 quote dropped 'it is arguable that'.
  Third build: the boosted-sky check was first written with a guessed 1e-9 on both sides and FAILED -- the Galilean
  error is O(v^2/c^2) = 6.5e-11; the check is now that the fit resolves it (residual < 1e-12, Galilean error > 100x).
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
    localclock = _by_path("cmb_localclock", os.path.join(HERE, "localclock.py"))

cmbframe = medium.cmbframe
T_DEC = medium.acoustic_past()["T_decoupling_K"]
N_TICKS = 48
T_HOT, T_COLD = 2.0 * T_DEC, 0.5 * T_DEC
WIDTH_K = 0.03 * T_DEC
G0, W_GAMMA, W_B, DT = 0.5, 0.3, 0.6, 0.35

SP = np.array([[0, 0], [1, 0]], dtype=complex)
I2 = np.eye(2, dtype=complex)
NUM = np.diag([0.0, 1.0]).astype(complex)
GAMMA_IDX, B_IDX = 2, 1
PSI_PHOTON = np.array([0, 0, 1, 0], dtype=complex)


def temps(t_hot=T_HOT, t_cold=T_COLD, n=N_TICKS):
    return [t_hot * (t_cold / t_hot) ** (k / (n - 1)) for k in range(n)]


def x_e(T, width=WIDTH_K):
    return 1.0 / (1.0 + math.exp(-(T - T_DEC) / width))


def h_medium(T, g0=G0, step=True):
    g = g0 * (x_e(T) if step else 1.0)
    exch = np.kron(SP, SP.conj().T) + np.kron(SP.conj().T, SP)
    return W_GAMMA * np.kron(NUM, I2) + W_B * np.kron(I2, NUM) + g * exch


def u_step(T, step=True):
    w, v = np.linalg.eigh(h_medium(T, step=step))
    return v @ np.diag(np.exp(-1j * w * DT)) @ v.conj().T


def coupled_ground():
    """H-START-COUPLED-GROUND: the coupled medium's lowest one-excitation eigenstate at T_hot."""
    w, v = np.linalg.eigh(h_medium(T_HOT))
    one = [i for i in range(4) if abs(v[1, i]) ** 2 + abs(v[2, i]) ** 2 > 0.99]
    return v[:, one[int(np.argmin(w[one]))]].astype(complex)


PSI_GROUND = coupled_ground()


def history(psi0, ts=None, step=True):
    ts = temps() if ts is None else ts
    psis = [psi0.copy()]
    for k in range(len(ts) - 1):
        psis.append(u_step(ts[k], step) @ psis[-1])
    return ts, psis


def fk_hamiltonian(ts, psi0):
    n, d = len(ts), 4
    H = np.zeros((n * d, n * d), dtype=complex)
    Id = np.eye(d, dtype=complex)
    for k in range(n - 1):
        U = u_step(ts[k])
        a, b = slice(k * d, (k + 1) * d), slice((k + 1) * d, (k + 2) * d)
        H[a, a] += Id / 2
        H[b, b] += Id / 2
        H[b, a] += -U / 2
        H[a, b] += -U.conj().T / 2
    H[0:d, 0:d] += Id - np.outer(psi0, psi0.conj())
    return H


def rho_of(psis, w):
    w = np.asarray(w, dtype=float)
    w = w / w.sum()
    return sum(wk * np.outer(p, p.conj()) for wk, p in zip(w, psis))


def trace_distance(r, s):
    return 0.5 * float(np.sum(np.abs(np.linalg.eigvalsh(r - s))))


def purity(r):
    return float(np.real(np.trace(r @ r)))


def clock_weights(ts, kind):
    if kind == "uniform ticks":
        return [1.0] * len(ts)
    if kind == "conformal time":
        return [1.0 / T for T in ts]
    if kind == "cosmic time":
        return [1.0 / T ** 2 for T in ts]
    raise ValueError(kind)


KINDS = ("uniform ticks", "conformal time", "cosmic time")


def readings(psi0, step=True):
    ts, psis = history(psi0, step=step)
    out = {}
    for kind in KINDS:
        w = clock_weights(ts, kind)
        coupled = [wk if T > T_DEC else 0.0 for wk, T in zip(w, ts)]
        r_tr, r_m = rho_of(psis, w), rho_of(psis, coupled)
        out[kind] = {"coupled_weight": sum(coupled) / sum(w), "purity_traced": purity(r_tr), "purity_M": purity(r_m),
                     "TD": trace_distance(r_tr, r_m), "rho_traced": r_tr}
    return out


def record_sweep(psis, gammas=(0.0, 0.05, 0.2, 1.0, 5.0, 1e3)):
    """Records of the epoch (tick) held in matter: Gram G_jk = exp(-gamma|j-k|).  Two record families with Gram G
    (H-READOUT-BASIS): R = G^(1/2) and R = F G^(1/2) (F the discrete Fourier matrix, unitary) -- each reader measures
    the register in its computational basis.  Per gamma: the medium's UNCONDITIONAL state's purity (every m summed),
    the mean conditional purity for each readout, and chi = S(G/N) in bits."""
    n = len(psis)
    F = np.array([[np.exp(-2j * math.pi * j * k / n) for k in range(n)] for j in range(n)]) / math.sqrt(n)
    out = []
    for g in gammas:
        G = np.array([[math.exp(-g * abs(j - k)) for k in range(n)] for j in range(n)])
        ev, V = np.linalg.eigh(G)
        Rs = V @ np.diag(np.sqrt(np.clip(ev, 0, None))) @ V.T
        row = {"gamma": g}
        for name, R in (("sqrt", Rs.astype(complex)), ("fourier", F @ Rs)):
            tot, uncond = 0.0, np.zeros((4, 4), dtype=complex)
            for m in range(n):
                wts = [abs(R[m, k]) ** 2 / n for k in range(n)]
                pm = sum(wts)
                if pm < 1e-15:
                    continue
                rm = rho_of(psis, wts)
                tot += pm * purity(rm)
                uncond += pm * rm
            row["cond_purity_" + name] = tot
            row["uncond_purity_" + name] = purity(uncond)
        lam = np.clip(np.linalg.eigvalsh(G / n), 0, None)
        row["chi_bits"] = float(-sum(x * math.log2(x) for x in lam if x > 1e-15))
        out.append(row)
    return out


def selection_before_after(psi):
    """A qubit a|0> + b|1> (the medium's photon/matter amplitudes) read in the interfering basis |+>.  Coherent: P(+) =
    |a + b|^2 / 2.  After a matter record (decohered): 1/2.  Born selection AFTER the record: 1/2 (no change).  Born
    selection BEFORE the record (collapse on the coherent state): 1/2 -- differs from the coherent value: the
    in-principle signature of collapse timing."""
    a, b = psi[GAMMA_IDX], psi[B_IDX]
    nrm = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
    a, b = a / nrm, b / nrm
    plus = np.array([1, 1]) / math.sqrt(2)
    coh = abs(np.vdot(plus, np.array([a, b]))) ** 2
    rho_dec = np.diag([abs(a) ** 2, abs(b) ** 2])
    p_dec = float(np.real(plus @ rho_dec @ plus))
    p_after = abs(a) ** 2 * abs(plus[0]) ** 2 + abs(b) ** 2 * abs(plus[1]) ** 2
    p_before = p_after
    return {"P_coherent": float(coh), "P_decohered": p_dec, "P_select_after_records": float(p_after),
            "P_select_before_records": float(p_before), "difference_before_vs_coherent": float(abs(p_before - coh))}


def perspectives(psis):
    def qubit(psi):
        v = np.array([psi[GAMMA_IDX], psi[B_IDX]])
        return v / np.linalg.norm(v)
    rows = []
    for theta in (0.0, math.pi / 6, math.pi / 3, math.pi / 2):
        c, s = math.cos(theta / 2), math.sin(theta / 2)
        basis2 = [np.array([c, s]), np.array([-s, c])]
        seq, indep = [], []
        for k in (0, len(psis) // 3, len(psis) - 1):
            q = qubit(psis[k])
            p1 = [abs(q[0]) ** 2, abs(q[1]) ** 2]
            e = [np.array([1.0, 0.0]), np.array([0.0, 1.0])]
            seq.append(sum(p1[o] * (1 - abs(np.vdot(basis2[o], e[o])) ** 2) for o in (0, 1)))
            qq = abs(np.vdot(basis2[0], q)) ** 2                      # O2 on an independent copy
            indep.append(p1[0] * (1 - qq) + p1[1] * qq)
        rows.append({"theta_bloch": theta, "P_disagree_sequential": seq, "sin2_half": s * s,
                     "P_disagree_independent_copies": indep})
    # agreement through records, computed: system qubit q, CNOT onto one or two ancillas (record in the Z basis)
    q = qubit(psis[len(psis) // 3])
    cnot1 = np.zeros(4, dtype=complex)                                # |s a>: s in {0,1}, a = s
    cnot1[0], cnot1[3] = q[0], q[1]
    p_agree_link = abs(cnot1[0]) ** 2 + abs(cnot1[3]) ** 2           # O1 reads s, O2 reads the record a: equal
    ghz = np.zeros(8, dtype=complex)
    ghz[0], ghz[7] = q[0], q[1]                                       # two redundant copies
    p_agree_redundant = abs(ghz[0]) ** 2 + abs(ghz[7]) ** 2
    return {"rows": rows, "P_agree_cross_perspective_link": float(p_agree_link),
            "P_agree_redundant_records": float(p_agree_redundant)}


def _boost(beta_vec, k4):
    """Lorentz boost of a 4-vector into the frame moving with velocity beta_vec."""
    b = np.asarray(beta_vec, dtype=float)
    b2 = float(b @ b)
    g = 1 / math.sqrt(1 - b2)
    E, p = k4[0], np.asarray(k4[1:], dtype=float)
    bp = float(b @ p)
    E2 = g * (E - bp)
    p2 = p + ((g - 1) * bp / b2 - g * E) * b if b2 > 0 else p
    return np.concatenate([[E2], p2])


def _compose(u, v):
    """Relativistic velocity composition magnitude: frame moving at u (in c units, CMB frame), an object moving at v in
    that frame."""
    u, v = np.asarray(u), np.asarray(v)
    gu = 1 / math.sqrt(1 - float(u @ u))
    num = v + ((gu - 1) * float(u @ v) / float(u @ u) + gu) * u
    den = gu * (1 + float(u @ v))
    return float(np.linalg.norm(num / den))


def corridor_skies():
    """Proxima's sky built from the Sun's: photons arriving at the Sun from direction m carry T_S(m) = T0 / (gamma_S (1 -
    b_S.m)) (Planck 1303.5087v3 eq. 1).  Boost each photon 4-momentum into Proxima's frame (velocity w relative to the
    Sun, Gaia via localclock): Proxima sees T_P(n) = T_S(m) E_P/E_S.  Fit: a boosted blackbody has T_max/T_min =
    (1+b')/(1-b'); b' must equal the relativistic composition |b_S (+) w|, and differs from the Galilean |b_S + w|."""
    c = cmbframe.C_KMS
    T0 = medium.T0
    bS = np.array(cmbframe.V_SUN_CMB) / c
    w = localclock.proxima_velocity_vector() / c
    gS = 1 / math.sqrt(1 - float(bS @ bS))
    rng = np.random.default_rng(3)
    dirs = rng.normal(size=(4000, 3))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    temps_P = []
    for m in dirs:
        T_S = T0 / (gS * (1 - float(bS @ m)))
        k_S = np.concatenate([[1.0], -m])                       # photon propagating along -m (arriving from m)
        k_P = _boost(w, k_S)
        temps_P.append(T_S * k_P[0])
    # the extremes along the composed axis (sampled directions are not exactly there): refine with the analytic axis
    tmax, tmin = max(temps_P), min(temps_P)
    b_fit_sampled = (tmax - tmin) / (tmax + tmin)
    # exact extremes: photons arriving along +/- the composed velocity in Proxima's frame -- search the Sun-frame
    # directions that map there by scanning a fine grid around the extremes
    b_comp = _compose(bS, w)
    b_gal = float(np.linalg.norm(bS + w))
    def T_P_of(m):
        m = m / np.linalg.norm(m)
        k_P = _boost(w, np.concatenate([[1.0], -m]))
        return T0 / (gS * (1 - float(bS @ m))) * k_P[0]
    from itertools import product
    best_hi = max(dirs, key=T_P_of)
    best_lo = min(dirs, key=T_P_of)
    for _ in range(6):                                           # local refinement
        for best, sgn in ((best_hi, 1), (best_lo, -1)):
            pass
        cand_hi = [best_hi + 0.02 * np.array(d) for d in product((-1, 0, 1), repeat=3)]
        cand_lo = [best_lo + 0.02 * np.array(d) for d in product((-1, 0, 1), repeat=3)]
        best_hi = max(cand_hi, key=T_P_of)
        best_lo = min(cand_lo, key=T_P_of)
    for step in (0.005, 0.001, 0.0002, 0.00004):
        for _ in range(8):
            best_hi = max([best_hi + step * np.array(d) for d in product((-1, 0, 1), repeat=3)], key=T_P_of)
            best_lo = min([best_lo + step * np.array(d) for d in product((-1, 0, 1), repeat=3)], key=T_P_of)
    th, tl = T_P_of(best_hi), T_P_of(best_lo)
    b_fit = (th - tl) / (th + tl)
    return {"v_rel_kms": float(np.linalg.norm(w)) * c, "dipole_difference_K": T0 * float(np.linalg.norm(w)),
            "sun_dipole_K": T0 * float(np.linalg.norm(bS)), "earth_annual_K": T0 * 29.78 / c,
            "b_fit": b_fit, "b_fit_sampled": b_fit_sampled, "b_composed": b_comp, "b_galilean": b_gal,
            "fit_vs_composed": abs(b_fit - b_comp), "galilean_vs_composed": abs(b_gal - b_comp)}


def o9_pricing(eps_list=(1e-5, 1e-3, 1e-2, 1e-1)):
    b = 0.0
    margs_a = []
    for a in np.linspace(0, math.pi, 7):
        j = nosig.joint(a, b)
        margs_a.append(j[(1, 1)] + j[(-1, 1)])
    def bob_plus(a, eps_sign_plus):
        j = nosig.joint(a, b)
        pa = {o: j[(o, 1)] + j[(o, -1)] for o in (1, -1)}
        pb_given = {o: j[(o, 1)] / pa[o] for o in (1, -1)}
        pa_b = {1: pa[1] + eps_sign_plus / 2, -1: pa[-1] - eps_sign_plus / 2}
        return sum(pa_b[o] * pb_given[o] for o in (1, -1)), sum(pa[o] * pb_given[o] for o in (1, -1)), j
    shifts = []
    for a in (0.0, math.pi / 4, math.pi / 2):
        biased, unb, j = bob_plus(a, 1e-3)
        E = sum(oa * ob * p for (oa, ob), p in j.items())
        shifts.append({"a": a, "shift_per_eps": (biased - unb) / 1e-3, "E": E})
    def H(p):
        return -sum(q * math.log2(q) for q in (p, 1 - p) if q > 0)
    bits = medium.demand.counts()[0][1]
    rows = []
    for eps in eps_list:
        cap = 1 - H((1 - eps) / 2)
        p0, _, _ = bob_plus(0.0, eps)                    # fixed bias toward '+', Alice at a = b
        p1, _, _ = bob_plus(math.pi, eps)                # fixed bias toward '+', Alice at a = b + pi
        crossover = min(p0, p1)                          # Bob decodes '0' as P(+) = p0, '1' as p1
        cap_fixed = 1 - H(crossover) if abs(p0 + p1 - 1) < 1e-12 else float("nan")
        rows.append({"eps": eps, "bits_per_pair": cap, "bits_per_pair_fixed_bias_switch": cap_fixed,
                     "pairs_for_species_count": bits / cap})
    return {"bob_marginals_reading_a": margs_a, "max_marginal_shift_a": max(margs_a) - min(margs_a),
            "shifts_reading_b": shifts, "capacity_rows": rows, "species_bits": bits}


def compute():
    ts, psis = history(PSI_GROUND)
    H = fk_hamiltonian(ts, PSI_GROUND)
    w, v = np.linalg.eigh(H)
    g0v = v[:, 0]
    Psi = np.concatenate(psis) / math.sqrt(N_TICKS)
    blocks = g0v.reshape(N_TICKS, 4)
    clock_w = [float(np.linalg.norm(bk) ** 2) for bk in blocks]
    cond = [bk / np.linalg.norm(bk) for bk in blocks]
    infid = max(1 - abs(np.vdot(cond[k], psis[k])) ** 2 for k in range(N_TICKS))
    x = np.concatenate([PSI_GROUND] * N_TICKS) / math.sqrt(N_TICKS)
    Ut = v @ np.diag(np.exp(-1j * w * 50.0)) @ v.conj().T
    comm = float(np.linalg.norm(h_medium(T_HOT) @ h_medium(T_COLD) - h_medium(T_COLD) @ h_medium(T_HOT)))
    # stationarity of the coupled ground state while coupled (M's 'constant')
    hot = [k for k, T in enumerate(ts) if T > T_DEC + 5 * WIDTH_K]
    stat_coupled = min(abs(np.vdot(PSI_GROUND, psis[k])) ** 2 for k in hot)
    rd_g, rd_g_const = readings(PSI_GROUND, True), readings(PSI_GROUND, False)
    rd_p, rd_p_const = readings(PSI_PHOTON, True), readings(PSI_PHOTON, False)
    window_TD = {k: trace_distance(rd_p[k]["rho_traced"], rd_p_const[k]["rho_traced"]) for k in KINDS}
    strip = lambda rd: {k: {kk: vv for kk, vv in r.items() if kk != "rho_traced"} for k, r in rd.items()}
    _, psis_p = history(PSI_PHOTON)
    return {"N": N_TICKS, "T_dec": T_DEC, "E0": float(w[0]), "gap": float(w[1] - w[0]),
            "gap_formula": 1 - math.cos(math.pi / (2 * N_TICKS)), "overlap": float(abs(np.vdot(g0v, Psi))),
            "clock_weight_spread": max(clock_w) - min(clock_w), "conditional_infidelity_from_ground": float(infid),
            "nonstationary_fidelity": float(abs(np.vdot(x, Ut @ x))), "commutator_hot_cold": comm,
            "coupled_ground_stationary_fidelity": float(stat_coupled),
            "readings_ground": strip(rd_g), "readings_ground_constant_g": strip(rd_g_const),
            "readings_photon": strip(rd_p), "readings_photon_constant_g": strip(rd_p_const),
            "photon_traced_step_vs_constant": window_TD, "records": record_sweep(psis_p),
            "selection": selection_before_after(psis_p[len(psis_p) // 3]), "perspectives": perspectives(psis_p),
            "skies": corridor_skies(), "o9": o9_pricing()}


def report():
    d = compute()
    print("H-UNOBSERVED-MEDIUM, H-TWO-OBSERVERS, H-CONSCIOUS-SELECTS, H-MANY-PERSPECTIVES (verified twice; not seated)\n")
    print("(1) global state: eigh ground state = history (overlap %.12f, E %.1e); gap %.4e = 1 - cos(pi/2N); conditioned "
          "on the clock it gives ordinary evolution (%.1e), uniform clock weights (%.1e).  Detuned: ||[H_hot,H_cold]|| %.3f"
          % (d["overlap"], d["E0"], d["gap"], d["conditional_infidelity_from_ground"], d["clock_weight_spread"],
             d["commutator_hot_cold"]))
    print("    the medium starts in the coupled ground state (M's 'ground state'): stationary while coupled (fidelity %.6f)"
          % d["coupled_ground_stationary_fidelity"])
    print("(2) TRACED vs M-SUPPORT, from the coupled ground state, with decoupling | without (constant coupling, the real "
          "control):")
    for k in KINDS:
        print("    %-15s %.3f | %.1e   (coupled weight %.3f; purity M-SUPPORT %.3f)" % (
            k, d["readings_ground"][k]["TD"], d["readings_ground_constant_g"][k]["TD"],
            d["readings_ground"][k]["coupled_weight"], d["readings_ground"][k]["purity_M"]))
    print("    from the photon start: with decoupling %s | without %s; traced-with vs traced-without decoupling %s" % (
        ["%.3f" % d["readings_photon"][k]["TD"] for k in KINDS],
        ["%.3f" % d["readings_photon_constant_g"][k]["TD"] for k in KINDS],
        ["%.3f" % d["photon_traced_step_vs_constant"][k] for k in KINDS]))
    print("(3) records of the epoch held in matter, read by a reader (photon start): gamma | unconditional purity | "
          "conditional purity sqrt-readout / Fourier-readout | chi (bits)")
    for r in d["records"]:
        print("    %-6g %.6f | %.3f / %.3f | %.3f" % (r["gamma"], r["uncond_purity_sqrt"], r["cond_purity_sqrt"],
                                                     r["cond_purity_fourier"], r["chi_bits"]))
    s = d["selection"]
    print("(4) conscious selection: P(+) coherent %.4f; decohered %.4f; Born selection after records %.4f (no change); "
          "before records %.4f (differs from coherent by %.4f -- the in-principle signature)" % (
              s["P_coherent"], s["P_decohered"], s["P_select_after_records"], s["P_select_before_records"],
              s["difference_before_vs_coherent"]))
    print("(5) many perspectives, P(disagree) by Bloch angle (sequential | independent copies, three states):")
    for r in d["perspectives"]["rows"]:
        print("    %.3f rad: %s | %s" % (r["theta_bloch"], ["%.4f" % x for x in r["P_disagree_sequential"]],
                                         ["%.4f" % x for x in r["P_disagree_independent_copies"]]))
    p = d["perspectives"]
    sk = d["skies"]
    print("    through a record: cross-perspective link %.12f, redundant records %.12f (computed)" % (
        p["P_agree_cross_perspective_link"], p["P_agree_redundant_records"]))
    print("    corridor's ends: skies differ by %.3f mK (|dv| %.1f km/s; the Sun's dipole %.3f mK; Earth's annual "
          "modulation ~%.3f mK).  Proxima's sky built from the Sun's by boosting photons is a boosted blackbody with "
          "b' %.8e = relativistic composition %.8e (|diff| %.1e); Galilean %.8e (off by %.1e)" % (
              sk["dipole_difference_K"] * 1e3, sk["v_rel_kms"], sk["sun_dipole_K"] * 1e3, sk["earth_annual_K"] * 1e3,
              sk["b_fit"], sk["b_composed"], sk["fit_vs_composed"], sk["b_galilean"], sk["galilean_vs_composed"]))
    o = d["o9"]
    print("(6) O9: reading (a) Bob's marginal spread %.1e (no channel); reading (b) shift per unit bias = E/2: %s" % (
        o["max_marginal_shift_a"], ["%.3f vs %.3f" % (x["shift_per_eps"], x["E"] / 2) for x in o["shifts_reading_b"]]))
    for r in o["capacity_rows"]:
        print("    bias %.0e: %.2e bits per pair (fixed unwilled bias + setting switch: %.2e); %.2e pairs for the "
              "species count" % (r["eps"], r["bits_per_pair"], r["bits_per_pair_fixed_bias_switch"],
                                 r["pairs_for_species_count"]))


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
    chk("gap = 1 - cos(pi/(2N)) to 1e-8", abs(d["gap"] - d["gap_formula"]) < 1e-8)
    chk("conditioning the ground state itself gives ordinary evolution with uniform clock weights",
        d["conditional_infidelity_from_ground"] < 1e-10 and d["clock_weight_spread"] < 1e-10)
    chk("a non-eigenstate evolves under the global Hamiltonian (fidelity %.3f)" % d["nonstationary_fidelity"],
        d["nonstationary_fidelity"] < 0.99, ctl=True)
    chk("the coupled ground state is stationary while coupled (fidelity %.6f > 0.999)" %
        d["coupled_ground_stationary_fidelity"], d["coupled_ground_stationary_fidelity"] > 0.999)
    g, gc = d["readings_ground"], d["readings_ground_constant_g"]
    chk("from the coupled ground state, TRACED and M-SUPPORT differ with decoupling (%s > 0.1)" % (
        ["%.3f" % g[k]["TD"] for k in KINDS]), all(g[k]["TD"] > 0.1 for k in KINDS))
    chk("and coincide without it -- same range, constant coupling (%s)" % (["%.1e" % gc[k]["TD"] for k in KINDS]),
        all(gc[k]["TD"] < 1e-9 for k in KINDS), ctl=True)
    rec = d["records"]
    chk("records keep every probability: the medium's unconditional state is unchanged by any record (purity spread "
        "%.1e over gamma and readouts)" % (max(max(r["uncond_purity_sqrt"], r["uncond_purity_fourier"]) for r in rec)
                                           - min(min(r["uncond_purity_sqrt"], r["uncond_purity_fourier"]) for r in rec)),
        max(max(r["uncond_purity_sqrt"], r["uncond_purity_fourier"]) for r in rec)
        - min(min(r["uncond_purity_sqrt"], r["uncond_purity_fourier"]) for r in rec) < 1e-12)
    chk("conditional purity depends on the readout basis (gamma 0.05: %.3f sqrt vs %.3f Fourier)" % (
        rec[1]["cond_purity_sqrt"], rec[1]["cond_purity_fourier"]),
        abs(rec[1]["cond_purity_sqrt"] - rec[1]["cond_purity_fourier"]) > 0.05)
    chk("the records' Holevo information rises from 0 (gamma 0: %.3f bits) to log2 N (gamma 1e3: %.3f of %.3f)" % (
        rec[0]["chi_bits"], rec[-1]["chi_bits"], math.log2(N_TICKS)),
        rec[0]["chi_bits"] < 1e-9 and abs(rec[-1]["chi_bits"] - math.log2(N_TICKS)) < 1e-6)
    s = d["selection"]
    chk("Born selection after records changes nothing (%.4f = %.4f); before records it differs from the coherent "
        "statistic (by %.4f > 0.01)" % (s["P_select_after_records"], s["P_decohered"],
                                         s["difference_before_vs_coherent"]),
        abs(s["P_select_after_records"] - s["P_decohered"]) < 1e-12 and s["difference_before_vs_coherent"] > 0.01)
    pr = d["perspectives"]
    chk("independent copies give a state-dependent disagreement (spread over states at theta 0: %.3f > 0.01)" % (
        max(pr["rows"][0]["P_disagree_independent_copies"]) - min(pr["rows"][0]["P_disagree_independent_copies"])),
        max(pr["rows"][0]["P_disagree_independent_copies"]) - min(pr["rows"][0]["P_disagree_independent_copies"]) > 0.01)
    chk("agreement through a record is computed: cross-perspective link %.12f, redundant records %.12f" % (
        pr["P_agree_cross_perspective_link"], pr["P_agree_redundant_records"]),
        abs(pr["P_agree_cross_perspective_link"] - 1) < 1e-12 and abs(pr["P_agree_redundant_records"] - 1) < 1e-12)
    sk = d["skies"]
    chk("Proxima's sky built by boosting the Sun's photons is a boosted blackbody at the relativistic composition of "
        "the velocities (|b' - composed| %.1e < 1e-12), not the Galilean sum (off by %.1e, > 100x the residual)" % (
            sk["fit_vs_composed"], sk["galilean_vs_composed"]),
        # first written with a guessed 1e-9 on both sides; the Galilean error is O(v^2/c^2) ~ 6.5e-11 here, so the
        # test is that the fit resolves it: residual below 1e-12 and the Galilean error over 100x that residual
        sk["fit_vs_composed"] < 1e-12 and sk["galilean_vs_composed"] > 100 * sk["fit_vs_composed"])
    o = d["o9"]
    chk("O9 reading (a): Bob's marginal independent of Alice's setting (%.1e)" % o["max_marginal_shift_a"],
        o["max_marginal_shift_a"] < 1e-12)
    chk("O9 reading (b): Bob's shift per unit bias = E(a,b)/2 at every setting tested",
        all(abs(x["shift_per_eps"] - x["E"] / 2) < 1e-9 for x in o["shifts_reading_b"]))
    chk("an unwilled fixed bias with a setting switch gives the same capacity as a chosen bias (all eps)",
        all(abs(r["bits_per_pair_fixed_bias_switch"] - r["bits_per_pair"]) < 1e-12 for r in o["capacity_rows"]))
    structural.append("Born selection after decoherence is, by linearity, indistinguishable from no selection for "
                      "every later statistic; identical to the standard account in Born frequencies, distinguishable in "
                      "principle by interference/Zeno tests (Chalmers-McQueen), unperformed; their simple versions are "
                      "falsified (abstract p.1)")
    structural.append("the sequential-perspective disagreement sin^2(theta/2) is state-independent by construction "
                      "(O1's collapse erases the state); Adlam-Rovelli's agreement is a postulate there (Def. 4.1)")
    structural.append("a sentient observer in unitary quantum mechanics is one more record register; telling it apart "
                      "needs non-unitary physics, all proposed tests unperformed")
    for st in structural:
        print("  STRUCTURAL: " + st)
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
