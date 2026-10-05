#!/usr/bin/env python3
"""
unobserved.py -- H-UNOBSERVED-MEDIUM and H-TWO-OBSERVERS: a computable model of a timeless universe whose history,
decoupling included, appears only relative to a clock.

Not seated; not yet verified.  M (rulings item 48): "what if this is the ground state without first principles/without
observation? The decoupling only exists upon observation of a universe? And this would be why it is a constant".  M
(item 49): "1. Also, yes, matter itself is capable of observation, however, it is not conscious conversation, which
requires sentience . A different type of observation...".  Carried as M's hypotheses H-UNOBSERVED-MEDIUM and
H-TWO-OBSERVERS, never as results.  M's order: READ (done, 2026-10-05: relational time, the CMB's classicality, the two
kinds of observation), then this model, then what would distinguish the hypothesis is priced.

    python3 unobserved.py              report
    python3 unobserved.py --selftest   checks, with CONTROLS
    python3 unobserved.py --json       the numbers as JSON

THE MODEL (each piece named; it ILLUSTRATES a mechanism, it is not evidence about the universe)
  A clock register |k>, k = 0..N-1, labels the cooling: T_k from T_hot to T_cold (H-CLOCK-IS-COOLING: the scale factor
  as internal time, as Kiefer 1401.3578v1 printed p.23 defines an intrinsic time from it).  The medium is a toy photon
  (gamma) and matter (b) pair of two-level modes with an exchange coupling g(T) = g0 x_e(T): a logistic ionisation
  fraction stepping down at T_dec = T0 (1 + z*) = 2973 K (medium.py, READ) -- H-TOY-MEDIUM, H-TOY-SAHA (not Saha's
  equation).  One clock step evolves the medium by U_k = exp(-i H(T_k) dt).
  The whole is given a HISTORY-STATE Hamiltonian (the Feynman-Kitaev construction; Feynman 1985 and Kitaev, NAMED-NOT-
  READ): H = sum_k [ |k><k| + |k+1><k+1| - |k+1><k| U_k - |k><k+1| U_k^dag ] / 2 + |0><0| (1 - |psi0><psi0|).  Its
  ground state has energy 0 and is the history state |Psi> = sum_k |k>|psi_k>/sqrt(N), psi_{k+1} = U_k psi_k -- a
  timeless 'ground state' (Hartle-Hawking's word for theirs, APS abstract PRD 28, 2960, quotation marks theirs) that
  CONTAINS the whole history as correlations, as Page-Wootters' global states do (Giovannetti-Lloyd-Maccone 1504.04215v3
  p.2 eqs. 1-5; Marletto-Vedral 1610.04773v2 p.4).

WHAT IS COMPUTED
  (1) The global state is constant: H |Psi> = 0, unique (a gap above it), unchanged by its own evolution exp(-iHt).
  (2) Relative to the clock -- any reading of it -- the medium is coupled before T_dec and decoupled after: the
      conditional states equal ordinary unitary evolution to machine precision (empirical equivalence, as GLM p.2 eq. 5,
      Marletto-Vedral p.4, Page gr-qc/9303020v2 p.6 state it).
  (3) The UNOBSERVED medium (the clock traced out) is the time-average mixture over the whole history -- coupled and
      decoupled epochs weighted by their clock ticks -- not the coupled medium alone.  So in the Page-Wootters reading,
      'unobserved' is not 'coupled'.  M's reading (the unobserved universe IS the coupled medium; observation brings the
      clock and with it decoupling) is a DIFFERENT hypothesis, computed here as the medium frozen at T_hot: it differs
      from the traced history by a trace distance printed below.  Both are carried.
  (4) Two kinds of observer (H-TWO-OBSERVERS): a MATTER observer -- a record register that copies the clock reading
      (einselection, Zurek 0903.5082v1 p.2: observers 'eavesdrop on the environment') -- makes the clock classical
      (the clock-medium state becomes block-diagonal) and, conditioned on its record, sees exactly the same medium as
      the clock projection.  A SENTIENT observer, in unitary quantum mechanics, is one more record register (Zurek
      quant-ph/0105127v3 p.43-44) and sees the same; telling the two apart needs physics beyond unitary quantum
      mechanics (Chalmers-McQueen 2105.02314v1 p.34-35; Bong et al. 1907.05607v4 p.7), and every proposed discriminating
      experiment is unperformed.  STRUCTURAL, not counted.
  (5) What would distinguish H-UNOBSERVED-MEDIUM from the standard account: OPEN.  Marletto-Vedral (p.4): global
      stationarity is empirically indistinguishable from a non-stationary universe.  Against observer-triggered
      decoupling, Perez-Sahlmann-Sudarsky (gr-qc/0508100v3 p.10) argue circularity -- our existence depends on the
      inhomogeneities, 'and thus our actions could not be their cause' -- recorded as a source's argument, not a
      refutation.  No paper read tests observer-triggered collapse against CMB data (objective collapse is tested:
      Martin-Vennin 1906.04405v4 p.5 rule one CSL version out; Piccirilli et al. 1709.06237v3 p.17-21 find others
      compatible).

NAMED HYPOTHESES
  H-CLOCK-IS-COOLING, H-TOY-MEDIUM, H-TOY-SAHA (above); H-HISTORY-STATE (the global state is the history-state
  Hamiltonian's ground state); H-UNOBSERVED-IS-HOT (M's reading as modelled: the medium frozen at T_hot, no clock);
  H-RECORD (the matter observer is an ideal copy of the clock reading).  Plus H-UNOBSERVED-MEDIUM and H-TWO-OBSERVERS
  (M's).
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

T_DEC = medium.acoustic_past()["T_decoupling_K"]      # T0 (1 + z*), READ inputs
N_TICKS = 48
T_HOT, T_COLD = 2.0 * T_DEC, 0.5 * T_DEC
WIDTH_K = 0.03 * T_DEC                                 # H-TOY-SAHA: the step's width
G0, OMEGA, DT = 1.0, 0.3, 0.35                         # toy units (H-TOY-MEDIUM)

# two qubits: gamma (first) and b (second); basis |gamma b> = 00, 01, 10, 11
SP = np.array([[0, 0], [1, 0]], dtype=complex)        # raising |0> -> |1>
I2 = np.eye(2, dtype=complex)
NUM = np.diag([0.0, 1.0]).astype(complex)


def temps():
    return [T_HOT * (T_COLD / T_HOT) ** (k / (N_TICKS - 1)) for k in range(N_TICKS)]


def x_e(T):
    return 1.0 / (1.0 + math.exp(-(T - T_DEC) / WIDTH_K))


def h_medium(T, g0=G0):
    g = g0 * x_e(T)
    exch = np.kron(SP, SP.conj().T) + np.kron(SP.conj().T, SP)
    return OMEGA * (np.kron(NUM, I2) + np.kron(I2, NUM)) + g * exch


def u_step(T, g0=G0):
    w, v = np.linalg.eigh(h_medium(T, g0))
    return v @ np.diag(np.exp(-1j * w * DT)) @ v.conj().T


PSI0 = np.array([0, 0, 1, 0], dtype=complex)          # |gamma = 1, b = 0>: the excitation starts in the photon


def history(g0=G0):
    ts = temps()
    psis = [PSI0.copy()]
    for k in range(N_TICKS - 1):
        psis.append(u_step(ts[k], g0) @ psis[-1])
    return ts, psis


def fk_hamiltonian(g0=G0):
    """The history-state Hamiltonian on clock (N) x medium (4), with the input penalty fixing psi_0."""
    ts = temps()
    d = 4
    H = np.zeros((N_TICKS * d, N_TICKS * d), dtype=complex)
    Id = np.eye(d, dtype=complex)
    for k in range(N_TICKS - 1):
        U = u_step(ts[k], g0)
        a, b = slice(k * d, (k + 1) * d), slice((k + 1) * d, (k + 2) * d)
        H[a, a] += Id / 2
        H[b, b] += Id / 2
        H[b, a] += -U / 2
        H[a, b] += -U.conj().T / 2
    H[0:d, 0:d] += Id - np.outer(PSI0, PSI0.conj())
    return H


def global_state(g0=G0):
    ts, psis = history(g0)
    return np.concatenate(psis) / math.sqrt(N_TICKS), ts, psis


def p_b(psi):
    return float(abs(psi[1]) ** 2 + abs(psi[3]) ** 2)    # matter excited (b = 1)


def reduced_medium(Psi):
    blocks = Psi.reshape(N_TICKS, 4)
    return blocks.T @ blocks.conj()                       # sum_k psi_k psi_k^dag (Psi already 1/sqrt(N) normalised)


def trace_distance(r, s):
    return 0.5 * float(np.sum(np.abs(np.linalg.eigvalsh(r - s))))


def compute():
    H = fk_hamiltonian()
    w, v = np.linalg.eigh(H)
    Psi, ts, psis = global_state()
    ground = v[:, 0]
    overlap = abs(np.vdot(ground, Psi))
    # (1) stationarity under the global evolution
    ww, vv = w, v
    Ut = vv @ np.diag(np.exp(-1j * ww * 5.0)) @ vv.conj().T
    stationary_fid = abs(np.vdot(Psi, Ut @ Psi))
    # (2) conditional states (project the clock on k, renormalise) against direct unitary evolution
    blocks = Psi.reshape(N_TICKS, 4)
    cond = [blocks[k] / np.linalg.norm(blocks[k]) for k in range(N_TICKS)]
    infid = max(1 - abs(np.vdot(cond[k], psis[k])) ** 2 for k in range(N_TICKS))
    pb = [p_b(c) for c in cond]
    hot = [k for k, T in enumerate(ts) if T > T_DEC + 5 * WIDTH_K]
    cold = [k for k, T in enumerate(ts) if T < T_DEC - 5 * WIDTH_K]
    swing_hot = max(pb[k] for k in hot) - min(pb[k] for k in hot)
    step_cold = max(abs(pb[k + 1] - pb[k]) for k in cold[:-1])
    # (3) the unobserved medium: the traced history, against M's reading (frozen at T_hot) and the coupled epochs alone
    rho_u = reduced_medium(Psi)
    purity = float(np.real(np.trace(rho_u @ rho_u)))
    coupled_frac = sum(1 for T in ts if T > T_DEC) / N_TICKS
    rho_coupled_only = sum(np.outer(psis[k], psis[k].conj()) for k in range(N_TICKS) if ts[k] > T_DEC)
    rho_coupled_only = rho_coupled_only / np.trace(rho_coupled_only)
    # M's reading as modelled: no clock, the medium in the coupled ground state at T_hot (H-UNOBSERVED-IS-HOT)
    wh, vh = np.linalg.eigh(h_medium(T_HOT))
    one_exc = [i for i in range(4) if abs(vh[1, i]) ** 2 + abs(vh[2, i]) ** 2 > 0.99]
    g_state = vh[:, one_exc[int(np.argmin(wh[one_exc]))]]   # the coupled medium's lowest one-excitation state
    rho_hot = np.outer(g_state, g_state.conj())
    td_hot = trace_distance(rho_u, rho_hot)
    td_coupled = trace_distance(rho_u, rho_coupled_only)
    # (4) a matter observer: an explicit record register R that copied the clock (H-RECORD), traced out numerically.
    #     Record states r_k with overlaps <r_j|r_k> = eps^|j-k|-free: ideal (orthonormal) or imperfect (a control).
    def with_record(eps):
        R = np.eye(N_TICKS, dtype=complex)
        if eps:
            R = R + eps * (np.ones((N_TICKS, N_TICKS)) - np.eye(N_TICKS))     # non-orthogonal record states
            R = R / np.linalg.norm(R, axis=0)                                   # unit columns: r_k = R[:, k]
        # Psi' = sum_k |k> |r_k> |psi_k> / sqrt(N); trace R:  rho_cm[(j,a),(k,b)] = <r_k|r_j> psi_j[a] psi_k[b]* / N
        G = R.conj().T @ R                                                      # Gram: G[k, j] = <r_k|r_j>
        rho = np.zeros((4 * N_TICKS, 4 * N_TICKS), dtype=complex)
        for j in range(N_TICKS):
            for k in range(N_TICKS):
                rho[4 * j:4 * j + 4, 4 * k:4 * k + 4] = G[k, j] * np.outer(blocks[j], blocks[k].conj())
        return rho
    rho_cm = np.outer(Psi, Psi.conj())
    rho_cm_dec = with_record(0.0)
    rho_cm_leaky = with_record(0.2)
    offd = lambda r: max(float(np.abs(r[4 * i:4 * i + 4, 4 * j:4 * j + 4]).max())
                         for i in range(N_TICKS) for j in range(N_TICKS) if i != j)
    offdiag_before, offdiag_after, offdiag_leaky = offd(rho_cm), offd(rho_cm_dec), offd(rho_cm_leaky)
    rec_cond_fid = min(abs(np.vdot(cond[k], rho_cm_dec[4 * k:4 * k + 4, 4 * k:4 * k + 4] @ cond[k])) /
                       float(np.real(np.trace(rho_cm_dec[4 * k:4 * k + 4, 4 * k:4 * k + 4])))
                       for k in range(N_TICKS))
    # control: no coupling -> the excitation never leaves the photon
    _, psis0 = history(g0=0.0)
    pb_uncoupled = max(p_b(p) for p in psis0)
    return {"N": N_TICKS, "T_dec": T_DEC, "E0": float(w[0]), "gap": float(w[1] - w[0]), "overlap": float(overlap),
            "stationary_fidelity": float(stationary_fid), "conditional_infidelity": float(infid),
            "pb": pb, "temps": ts, "swing_hot": swing_hot, "step_cold": step_cold,
            "purity_unobserved": purity, "coupled_fraction": coupled_frac,
            "trace_distance_unobserved_vs_hot": td_hot, "trace_distance_unobserved_vs_coupled_only": td_coupled,
            "offdiag_before": offdiag_before, "offdiag_after_record": offdiag_after, "offdiag_leaky_record": offdiag_leaky,
            "record_conditioned_fidelity": float(rec_cond_fid), "pb_uncoupled_max": pb_uncoupled}


def report():
    d = compute()
    print("H-UNOBSERVED-MEDIUM and H-TWO-OBSERVERS: a timeless universe whose history appears relative to a clock "
          "(not verified; not seated)\n")
    print("(1) the global state: ground energy %.1e, gap %.2e above it, overlap with the history state %.12f; unchanged "
          "by its own evolution (fidelity %.12f)" % (d["E0"], d["gap"], d["overlap"], d["stationary_fidelity"]))
    print("(2) relative to the clock: conditional states equal ordinary unitary evolution (worst infidelity %.1e); the "
          "medium exchanges while hot (P_b swings by %.3f) and freezes after T_dec = %.0f K (largest step %.1e)" % (
              d["conditional_infidelity"], d["swing_hot"], d["T_dec"], d["step_cold"]))
    print("(3) the unobserved medium (clock traced): a mixture (purity %.3f) of the whole history, %.0f %% of it in "
          "coupled epochs -- trace distance %.3f from M's reading as modelled (frozen hot), %.3f from the coupled "
          "epochs alone" % (d["purity_unobserved"], 100 * d["coupled_fraction"], d["trace_distance_unobserved_vs_hot"],
                            d["trace_distance_unobserved_vs_coupled_only"]))
    print("(4) a matter observer (a record of the clock): clock-medium coherences %.2e -> %.1e (classical clock); "
          "conditioned on its record it sees the same medium (fidelity %.12f).  A sentient observer, in unitary quantum "
          "mechanics, is one more record: the same" % (d["offdiag_before"], d["offdiag_after_record"],
                                                         d["record_conditioned_fidelity"]))
    print("(5) what would distinguish H-UNOBSERVED-MEDIUM: OPEN (global stationarity is empirically indistinguishable, "
          "Marletto-Vedral p.4; Perez-Sahlmann-Sudarsky p.10 argue observer-triggered decoupling is circular)")


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
    chk("the global state is the history-state Hamiltonian's ground state: energy %.1e, overlap %.12f" % (
        d["E0"], d["overlap"]), abs(d["E0"]) < 1e-10 and d["overlap"] > 1 - 1e-10)
    chk("it is unique: a gap %.4f above it" % d["gap"], d["gap"] > 1e-4)
    chk("it is constant under its own evolution exp(-iHt) (fidelity %.12f)" % d["stationary_fidelity"],
        d["stationary_fidelity"] > 1 - 1e-10)
    Psi, ts, psis = global_state()
    H = fk_hamiltonian()
    chk("a state that is NOT the history (the clock frozen at tick 0 for every k) has energy above zero",
        float(np.real(np.vdot(np.concatenate([PSI0] * N_TICKS) / math.sqrt(N_TICKS),
                              H @ (np.concatenate([PSI0] * N_TICKS) / math.sqrt(N_TICKS))))) > 1e-3, ctl=True)
    chk("relative to the clock the conditional states equal ordinary unitary evolution (infidelity %.1e)" %
        d["conditional_infidelity"], d["conditional_infidelity"] < 1e-10)
    chk("hot epochs exchange (P_b swings by %.3f > 0.2); cold epochs are frozen (largest step %.1e < 1e-3)" % (
        d["swing_hot"], d["step_cold"]), d["swing_hot"] > 0.2 and d["step_cold"] < 1e-3)
    chk("with no coupling the excitation never leaves the photon (max P_b %.1e)" % d["pb_uncoupled_max"],
        d["pb_uncoupled_max"] < 1e-12, ctl=True)
    chk("the unobserved medium is mixed (purity %.3f < 0.99) and differs from M's reading as modelled (trace distance "
        "%.3f > 0.05) and from the coupled epochs alone (%.3f > 0.05)" % (
            d["purity_unobserved"], d["trace_distance_unobserved_vs_hot"],
            d["trace_distance_unobserved_vs_coupled_only"]),
        d["purity_unobserved"] < 0.99 and d["trace_distance_unobserved_vs_hot"] > 0.05
        and d["trace_distance_unobserved_vs_coupled_only"] > 0.05)
    chk("a matter observer's record makes the clock classical (coherences %.2e -> %.1e) and, conditioned on it, the "
        "medium is the same (fidelity %.12f)" % (d["offdiag_before"], d["offdiag_after_record"],
                                                  d["record_conditioned_fidelity"]),
        d["offdiag_before"] > 1e-3 and d["offdiag_after_record"] < 1e-15 and d["record_conditioned_fidelity"] > 1 - 1e-10)
    chk("an imperfect record (non-orthogonal record states) leaves clock coherences (%.2e > 1e-4)" %
        d["offdiag_leaky_record"], d["offdiag_leaky_record"] > 1e-4, ctl=True)
    structural.append("a sentient observer in unitary quantum mechanics is one more record register and sees the same "
                      "(Zurek quant-ph/0105127v3 p.43-44); distinguishing it needs non-unitary physics (Chalmers-McQueen "
                      "2105.02314v1; Bong et al. 1907.05607v4 p.7), all proposed tests unperformed")
    structural.append("what would distinguish H-UNOBSERVED-MEDIUM from the standard account is OPEN: global stationarity "
                      "is empirically indistinguishable (Marletto-Vedral 1610.04773v2 p.4)")
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
