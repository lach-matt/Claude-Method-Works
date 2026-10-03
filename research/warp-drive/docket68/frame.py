#!/usr/bin/env python3
r"""
frame.py -- DOCKET 68, agent A2-frame.  H-FRAME ("a preferred frame exists, and messages may travel into the
past"), tested alone and with the curvature pairing the charter records.  NOT SEATED.  Reads the corpus, never
writes to it.

    python3 frame.py              the reading (all three parts)
    python3 frame.py --selftest   fixtures (READ or computed) and CONTROLS that must fail; exits 1 on any miss

Imports, never copies: corridors.py (and through it latticectc.py), frw_frame.py, nosig.py, nlcontrol.py and
../transit.py.  The pre-docket scripts print when imported; their output is captured, not shown (its length is
reported).  numpy, sympy and z3 are used (allowed by the charter); everything else is stdlib.

THE THREE PARTS (as the computed task put them):
 (i)  which corridor networks a preferred frame keyed to the cosmic rest frame admits; whether they close a causal
      curve (O-LOOP); what is lost (messages into the past) -- M's two clauses graded separately.
 (ii) Deutsch's fixed-point consistency on a qubit CTC for a simple circuit: existence, nonlinearity in the input,
      relation to H-SETTLE, and whether it signals.
 (iii) whether a preferred frame removes O-BITS.

WAVE 3 (2026-10-03, after the re-verifications RV-0 AGAINST M and RV-1 FOR M):
 * four_basis_c2_table: BHW's general construction (0811.1209v2 pp.3-4, READ) on four axes with an 8-dimensional
   CTC gives 2.000000 bits per pair under C2, zero error (C-verify-1 #7's figure, first cited 'not re-run', now run).
 * clause 2b: O-BITS REMOVED-IF {a CTC at Bob, H-DCTC, C2, H-DCTC-SELECT} with O-LOOP reintroduced; O-MAKE
   NOT-BOUND-IF {2b's CTC; Geroch-compact only}, Tipler still binding.  Wave 2 first said LEAVES / OPEN.
 * drift_ordering's 'Bob first gives 0' is printed STRUCTURAL (H = 0 on I/2); the rule is named as part of H-C2.
 * O-LOOP for corridors in exact FRW is credited to the geometry, to no hypothesis.

SOURCES (status as M-D67-2 requires; quotes kept to short phrases):
 * Deutsch, Phys. Rev. D 44, 3197 (1991) -- not on arXiv (pre-dates gr-qc).  READ-VIA-RESTATEMENT:
   Bennett-Leung-Smith-Smolin arXiv:0908.3023v2 p.1 eqs (1)-(2) (the consistency condition; "because the fixed
   point is allowed to be a mixed state, it always exists"; the induced map "is nonlinear") and Brun-Harrington-
   Wilde arXiv:0811.1209v2 p.1 eqs (1)-(2) ("does not necessarily have to be unique").
 * Novikov self-consistency: Novikov, Phys. Rev. D 45, 1989 (1992) NAMED-NOT-READ; READ-VIA-RESTATEMENT at
   Carlini-Frolov-Mensky-Novikov-Soleng arXiv:gr-qc/9506087v2 p.3 (the principle: only "globally
   self-consistent" solutions occur locally) and pp.13-14 (Echeverria-Klinkhammer-Thorne: multiple, even
   infinite, self-consistent solutions, "no evidence for non self-consistent trajectories"); Visser
   arXiv:gr-qc/0204022v2 p.5.
 * Hawking, "The chronology protection conjecture", Phys. Rev. D 46, 603 (1992) -- not on arXiv (an alphaXiv
   title query resolved to a different paper, 2607.22056).  READ-VIA-RESTATEMENT: Visser gr-qc/0204022v2 pp.2,
   6-12, 14 (chronology horizon, fountain, divergence of <T_mu nu>, Kay-Radzikowski-Wald, "we do not know for
   certain"); Bermudez-Leonhardt arXiv:2607.22056v1 p.11 and App. A (quotes Hawking's two sentences).
 * CMB dipole: the board's D67 grade cmb-dipole-370kms NARROWED (docket67-raw/GRADES.tsv:112; audit json):
   369.82 +/- 0.11 km/s, READ-VIA-RESTATEMENT of Planck 2018 (arXiv:1807.06205), hypotheses H1 (kinematic
   dipole) and H2 (Solar-System barycentre; Earth 340.65 .. 399.08 km/s over a year) carried here.
"""

import contextlib
import io
import math
import os
import random
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, ".."))

_IMPORT_LOG = {}


def _quiet(modname):
    """Import a pre-docket script without letting its top-level prints through."""
    if modname in sys.modules:
        return sys.modules[modname]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mod = __import__(modname)
    _IMPORT_LOG[modname] = len(buf.getvalue())
    return mod


# =====================================================================================================================
# PART (i) -- corridor networks under a preferred frame
# =====================================================================================================================
#
# MODEL (named): a corridor is an identification of positions by a translation xi (latticectc H1-H3: flat bulk,
# translation lattice acting freely, test branes).  "Keyed to the cosmic rest frame" = xi has zero time component in
# the frame u = (1,0,0,0) of the comoving (CMB-dipole-free) observers -- hypothesis H-CMB-IS-COSMIC (needs the
# dipole's kinematic reading, D67 H1).

def cosmic_keyed_rank_n_is_safe(rank, trials, seed=7, dim=3):
    """Exact.  Generators with t = 0: Gram matrix (Minkowski) = Euclidean Gram of the spatial parts.  Sylvester:
    all leading minors > 0 <=> positive definite <=> no nonzero causal vector in the SPAN, a fortiori in the
    lattice.  Returns (lattices tested, lattices with a non-positive-definite Gram)."""
    L = _quiet("corridors").L
    rng = random.Random(seed)
    tested = bad = 0
    while tested < trials:
        gens = [(Fr(0),) + tuple(Fr(rng.randint(-9, 9), rng.randint(1, 9)) for _ in range(dim))
                for _ in range(rank)]
        G = [[L.ip(a, b) for b in gens] for a in gens]
        if _det(G) == 0:          # spatial parts dependent: not a rank-n lattice acting freely (H2) -- skipped
            continue              # and counted below by the caller's design (independence is H2, not a result)
        tested += 1
        if not all(_det([row[:k] for row in G[:k]]) > 0 for k in range(1, rank + 1)):
            bad += 1
    return tested, bad


def _det(M):
    M = [row[:] for row in M]
    n, d = len(M), Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [M[r][k] - f * M[c][k] for k in range(n)]
    return d


def simultaneity_velocity(T, Lx):
    """A corridor xi = (T, Lx, 0, 0) (c = 1) has both ends at one moment of the frame moving with v = T/Lx along
    x (Lorentz: dt' = gamma (dt - v dx) = 0).  |T| < |Lx| <=> |v| < 1 <=> xi spacelike."""
    return Fr(T) / Fr(Lx)


def past_corridor_witness(T=Fr(1, 10), Lx=Fr(1), b=Fr(1, 100)):
    """M's clause 2 inside the model: ONE corridor that delivers a message into the cosmic past by T (xi_t = -T),
    beside ONE cosmic-keyed corridor (0, 1, b, 0).  Returns (span kind, lattice vector (m,n), its norm)."""
    L = _quiet("corridors").L
    xi_past = (-T, Lx, Fr(0), Fr(0))
    xi_cos = (Fr(0), Fr(1), b, Fr(0))
    kind = L.span_kind(xi_past, xi_cos)
    if kind != "timelike":
        return kind, None, None
    m, n = L.timelike_vector(xi_past, xi_cos)
    return kind, (m, n), L.nrm(L.add(xi_past, xi_cos, m, n))


def past_corridor_condition():
    """sympy: Gram determinant of xi1 = (-T, L, 0, 0), xi2 = (0, a, b, 0).  Timelike span (=> CTC, latticectc (c))
    iff det < 0 iff b^2 (L^2 - T^2) < T^2 a^2.  For every T > 0 there is such a b (b -> 0)."""
    import sympy as sp
    T, Lx, a, b = sp.symbols("T L a b", positive=True)
    A = Lx**2 - T**2
    C = a**2 + b**2
    H = Lx * a
    det = sp.expand(A * C - H**2)
    return det, sp.simplify(det - (b**2 * (Lx**2 - T**2) - T**2 * a**2))


# --------------------------------------------------------------------------------------------- the curvature pairing
def frw_killing_table():
    """frw_frame.lie_g, re-bound to the FRW metric.  FINDING (recorded, not repaired): frw_frame.py rebinds its
    module-global g to Minkowski for its control at the end of the script, so an importer calling
    frw_frame.lie_g gets the MINKOWSKI Lie derivative unless it restores g -- its printed output is unaffected."""
    import sympy as sp
    F = _quiet("frw_frame")
    t, x, y, z, a = F.t, F.x, F.y, F.z, F.a
    rebound_to_minkowski = (F.g == sp.diag(-1, 1, 1, 1))
    out = {"frw_frame_g_was_minkowski_after_import": bool(rebound_to_minkowski)}

    def killing(metric, xi):
        F.g = metric
        return F.lie_g(xi) == sp.zeros(4, 4)

    gen = sp.diag(-1, a**2, a**2, a**2)
    out["generic a(t): d_x"] = killing(gen, [0, 1, 0, 0])
    out["generic a(t): d_t"] = killing(gen, [1, 0, 0, 0])
    out["generic a(t): boost x d_t + t d_x"] = killing(gen, [x, t, 0, 0])
    # dilation-time-translation  d_t - c (x d_x + y d_y + z d_z): solve the Killing equation for a(t)
    c = sp.symbols("c", real=True)
    F.g = gen
    Lg = F.lie_g([1, -c * x, -c * y, -c * z])
    out["dilation: Killing iff"] = sp.simplify(Lg[1, 1])          # 2 a a' - 2 c a^2 = 0  <=>  a'/a = c
    H = sp.symbols("H", positive=True)
    out["de Sitter a=exp(Ht): d_t - H x.d_x"] = killing(sp.diag(-1, *(3 * [sp.exp(2 * H * t)])),
                                                        [1, -H * x, -H * y, -H * z])
    s = sp.sinh(t) ** sp.Rational(2, 3)                              # flat LambdaCDM (matter + Lambda), units 3H_L/2 = 1
    out["LambdaCDM a=sinh(t)^(2/3): d_t - x.d_x"] = killing(sp.diag(-1, s**2, s**2, s**2), [1, -x, -y, -z])
    out["LambdaCDM a=sinh(t)^(2/3): d_x"] = killing(sp.diag(-1, s**2, s**2, s**2), [0, 1, 0, 0])
    out["control Minkowski: boost"] = killing(sp.diag(-1, 1, 1, 1), [x, t, 0, 0])
    F.g = sp.diag(-1, 1, 1, 1)                                       # leave the module as it left itself
    return out


def de_sitter_identification_closes():
    """In exact de Sitter (a = e^{Ht}) the isometry phi: (t, x) -> (t + tau, e^{-H tau} x) fixes the worldline
    x = 0 and moves it forward by tau: the segment x = 0, t in [t0, t0 + tau] is timelike and its ends are
    identified -- a closed timelike curve in the quotient.  Returns (phi preserves the metric, image of (t0, 0),
    norm of the segment's tangent)."""
    import sympy as sp
    t, tau, H, X = sp.symbols("t tau H X", real=True)
    tp, Xp = t + tau, sp.exp(-H * tau) * X
    # pull back ds^2 = -dt^2 + e^{2Ht} dX^2 under phi (one spatial dimension suffices)
    dtp = sp.Matrix([sp.diff(tp, t), sp.diff(tp, X)])
    dXp = sp.Matrix([sp.diff(Xp, t), sp.diff(Xp, X)])
    pulled = -dtp * dtp.T + sp.exp(2 * H * tp) * dXp * dXp.T
    orig = sp.diag(-1, sp.exp(2 * H * t))
    isometry = sp.simplify(pulled - orig) == sp.zeros(2, 2)
    image = (sp.simplify(tp.subs(X, 0)), sp.simplify(Xp.subs(X, 0)))
    # wave 2: wave 1 first typed 'tangent_norm = -1' (a declared value in a check).  Now computed: the tangent of the
    # segment x = 0, t in [t0, t0 + tau] is (1, 0); its norm under the de Sitter metric at X = 0.
    tvec = sp.Matrix([1, 0])
    tangent_norm = sp.simplify((tvec.T * orig * tvec)[0].subs(X, 0))
    return isometry, image, tangent_norm


def frw_time_function_lemma():
    """z3, with the PROOF-ASSISTANT guards.  Claim: in ds^2 = -dt^2 + a^2 |dx|^2 with a > 0, every nonzero causal
    vector has v_t != 0 (so t is strictly monotone along every causal curve, and the quotient by comoving spatial
    translations -- which preserve t -- has no closed causal curve, at any rank, for any a(t) > 0).
    Returns dict with 'claim' ('unsat' = proved), 'vacuity' ('sat' = hypothesis non-empty), 'drift' (encoded norm
    vs frw_frame's metric at sample points, max |difference|)."""
    import z3
    import sympy as sp
    a, vt, vx, vy, vz = z3.Reals("a vt vx vy vz")

    def nrm_enc(a_, t_, x_, y_, z_):
        return -t_ * t_ + a_ * a_ * (x_ * x_ + y_ * y_ + z_ * z_)

    nonzero = z3.Or(vt != 0, vx != 0, vy != 0, vz != 0)
    hyp = z3.And(a > 0, nrm_enc(a, vt, vx, vy, vz) <= 0, nonzero)
    s = z3.Solver()
    s.add(hyp, vt == 0)
    claim = str(s.check())
    v = z3.Solver()
    v.add(hyp, vx != 0)                                               # non-trivial: a causal vector with motion
    vac = str(v.check())
    F = _quiet("frw_frame")
    g = sp.diag(-1, F.a**2, F.a**2, F.a**2)
    rng = random.Random(3)
    drift = 0.0
    for _ in range(50):
        av = rng.uniform(0.1, 5)
        vec = [rng.uniform(-2, 2) for _ in range(4)]
        ref = sum(float(g[i, i].subs(F.a, av)) * vec[i] ** 2 for i in range(4))
        drift = max(drift, abs(ref - nrm_enc(av, *vec)))
    # CONTROL: drop a > 0 (allow a = 0): the claim must FAIL (a = 0 makes (0, 1, 0, 0) null with v_t = 0)
    c = z3.Solver()
    c.add(a >= 0, nrm_enc(a, vt, vx, vy, vz) <= 0, nonzero, vt == 0)
    control = str(c.check())
    return {"claim": claim, "vacuity": vac, "drift": drift, "control_a_ge_0": control}


def cmb_coordinate_past(L_ly=1.0, v_kms=369.82):
    """A corridor keyed to the cosmic frame (both ends at one cosmic time), length L along the dipole direction.
    In the barycentre's frame (moving at v relative to the cosmic frame, D67 H2) its far end is reached at
    dt' = -gamma v L / c^2: the message arrives in that frame's COORDINATE past.  Returns seconds and v/c."""
    c = 299792.458
    beta = v_kms / c
    gamma = 1 / math.sqrt(1 - beta * beta)
    year = 365.25 * 86400.0
    return -gamma * beta * L_ly * year, beta


# =====================================================================================================================
# PART (ii) -- Deutsch's fixed-point consistency on a qubit CTC
# =====================================================================================================================
def _np():
    import numpy as np
    return np


def ptrace(rho, dims, keep):
    """Partial trace of rho on subsystems with dimensions dims, keeping the list keep."""
    np = _np()
    n = len(dims)
    r = rho.reshape(dims + dims)
    idx = list(range(n))
    for k in sorted([i for i in idx if i not in keep], reverse=True):
        r = np.trace(r, axis1=k, axis2=k + r.ndim // 2)
    dk = int(np.prod([dims[i] for i in keep]))
    return r.reshape(dk, dk)


def deutsch_T(U, rho, dc, dt):
    """sigma -> Tr_CR[ U (rho (x) sigma) U^dagger ]  (BLSS 0908.3023v2 eq (1); BHW 0811.1209v2 eq (1))."""
    np = _np()

    def T(sig):
        return ptrace(U @ np.kron(rho, sig) @ U.conj().T, [dc, dt], [1])
    return T


def deutsch_fixed_point(U, rho, dc, dt, N=4000):
    """Existence, constructively: T is CPTP and linear in sigma for fixed rho, so its Cesaro means
    (1/N) sum T^n(I/dt) converge to a fixed STATE (finite-dimensional mean ergodic theorem).  The Cesaro estimate is
    then projected onto the exact eigenvalue-1 eigenspace (SVD null space of M - I).  Returns (sigma, dimension of
    the fixed-point space, residual ||T(sigma) - sigma||, min eigenvalue of sigma)."""
    np = _np()
    T = deutsch_T(U, rho, dc, dt)
    basis = []
    for i in range(dt):
        for j in range(dt):
            E = np.zeros((dt, dt), complex)
            E[i, j] = 1
            basis.append(T(E).reshape(-1))
    M = np.array(basis).T
    Mn = np.eye(dt * dt, dtype=complex)
    acc = np.zeros((dt * dt, dt * dt), complex)
    for _ in range(N):
        acc += Mn
        Mn = M @ Mn
    P = acc / N
    v0 = (np.eye(dt) / dt).reshape(-1)
    est = P @ v0
    u, s, vh = np.linalg.svd(M - np.eye(dt * dt))
    null = vh[s < 1e-9].conj().T
    if null.shape[1]:
        coef, *_ = np.linalg.lstsq(null, est, rcond=None)
        est = null @ coef
    sig = est.reshape(dt, dt)
    sig = (sig + sig.conj().T) / 2
    sig = sig / np.trace(sig).real
    res = float(np.abs(T(sig) - sig).max())
    return sig, int(null.shape[1]), res, float(np.linalg.eigvalsh(sig).min())


def deutsch_output(U, rho, dc, dt):
    np = _np()
    sig, k, res, mn = deutsch_fixed_point(U, rho, dc, dt)
    out = ptrace(U @ np.kron(rho, sig) @ U.conj().T, [dc, dt], [0])
    return out, sig, k, res, mn


def bhw_circuit():
    """Brun-Harrington-Wilde 0811.1209v2 Fig. 1 (READ, p.2): SWAP(A, B) then controlled-Hadamard, A control, B
    target; A = chronology-respecting qubit (measured in the computational basis), B = CTC qubit."""
    np = _np()
    SW = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], complex)
    Hd = np.array([[1, 1], [1, -1]], complex) / math.sqrt(2)
    CH = np.block([[np.eye(2), np.zeros((2, 2))], [np.zeros((2, 2)), Hd]])
    return CH @ SW


KET = {"0": (1, 0), "1": (0, 1), "+": (2 ** -0.5, 2 ** -0.5), "-": (2 ** -0.5, -2 ** -0.5)}


def proj(label):
    np = _np()
    v = np.array(KET[label], complex)
    return np.outer(v, v.conj())


def bhw_p0(rho):
    """P(A reads 0) after the BHW circuit."""
    out, sig, k, res, mn = deutsch_output(bhw_circuit(), rho, 2, 2)
    return float(out[0, 0].real), k, res


def blss_epr_fixture():
    """BLSS 0908.3023v2 p.1 (READ): half of an EPR pair (B) swapped into the CTC; A untouched.  Deutsch gives
    rho_CTC = I/2 and rho'_AB = I/4."""
    np = _np()
    epr = np.array([1, 0, 0, 1], complex) / math.sqrt(2)
    rho_AB = np.outer(epr, epr.conj())
    SW = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], complex)
    U = np.kron(np.eye(2), SW)                                        # (A, B, CTC): swap B <-> CTC
    out, sig, k, res, mn = deutsch_output(U, rho_AB, 4, 2)
    return out, sig, k


def existence_census(trials=400, seed=11):
    """Random 2-qubit unitaries (CR qubit + CTC qubit, Haar via QR) and random mixed inputs: a fixed STATE found
    every time?  Returns (trials, failures, max residual, min eigenvalue seen, count with non-unique fixed point)."""
    np = _np()
    rng = np.random.default_rng(seed)
    fails, worst, mineig, nonuniq = 0, 0.0, 1.0, 0
    for _ in range(trials):
        Z = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
        Q, R = np.linalg.qr(Z)
        U = Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))
        G = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        rho = G @ G.conj().T
        rho /= np.trace(rho).real
        sig, k, res, mn = deutsch_fixed_point(U, rho, 2, 2, N=2000)
        worst, mineig = max(worst, res), min(mineig, mn)
        nonuniq += k > 1
        fails += (res > 1e-8) or (mn < -1e-9)
    return trials, fails, worst, mineig, nonuniq


def signalling_table():
    """Bob holds half of a singlet and feeds it to the BHW D-CTC circuit, then reads A.  Alice (spacelike) chooses
    to measure in z, in x, or not at all.  Two conventions for what the nonlinear map acts on -- a NAMED hypothesis,
    not a result:
      C1 (BLSS 'Universal Inclusion', 0908.3023v2 p.4): Deutsch's rule on the whole chronology-respecting system;
         with U = I_Alice (x) V_Bob,CTC the fixed point depends only on rho_Bob, which Alice cannot change.
      C2 (the 'linearity trap', ibid. p.2 Fig. 2): the map applied to each branch's pure state, then averaged.
    Returns P(Bob reads 0) per convention and Alice's choice, and the mutual information for a uniform z/x choice."""
    np = _np()
    sing = np.array([0, 1, -1, 0], complex) / math.sqrt(2)
    rho_AB = np.outer(sing, sing.conj())
    rho_B = ptrace(rho_AB, [2, 2], [1])
    res = {}
    # C1: the whole CR system is (Alice, Bob); U = I (x) V.  Alice's non-selective measurement in basis b.
    V = bhw_circuit()
    Ufull = np.kron(np.eye(2), V)

    def c1(rho_ab):
        out, sig, k, r, mn = deutsch_output(Ufull, rho_ab, 4, 2)
        return float(ptrace(out, [2, 2], [1])[0, 0].real)
    res[("C1", "none")] = c1(rho_AB)
    for basis, labels in (("z", "01"), ("x", "+-")):
        rho_m = sum(np.kron(proj(l), np.eye(2)) @ rho_AB @ np.kron(proj(l), np.eye(2)) for l in labels)
        res[("C1", basis)] = c1(rho_m)
    # C2: per-branch.  Singlet: Alice's outcome l leaves Bob in the orthogonal state.
    other = {"0": "1", "1": "0", "+": "-", "-": "+"}
    for basis, labels in (("z", "01"), ("x", "+-")):
        res[("C2", basis)] = sum(0.5 * bhw_p0(proj(other[l]))[0] for l in labels)
    res[("C2", "none")] = bhw_p0(rho_B)[0]          # no branches exist: C2 has nothing but the reduced state
    Hb = lambda p: -sum(q * math.log2(q) for q in (p, 1 - p) if q > 1e-15)
    for conv in ("C1", "C2"):
        pz, px = res[(conv, "z")], res[(conv, "x")]
        res[(conv, "MI bits")] = Hb((pz + px) / 2) - (Hb(pz) + Hb(px)) / 2
    return res


def settle_under_C1(eps=0.1):
    """H-SETTLE relation: nlcontrol.py's drift H = eps <X> Z, but with <X> = Tr(rho_B X) taken on Bob's reduced
    state (convention C1).  rho_B = I/2 for every choice of Alice's, so <X> = 0, H = 0, and Bob's state cannot
    depend on Alice's choice.  Returns max |rho_B(z) - rho_B(x)| after evolution (uses nlcontrol.U)."""
    np = _np()
    NL = _quiet("nlcontrol")
    sing = np.array([0, 1, -1, 0], complex) / math.sqrt(2)
    rho_AB = np.outer(sing, sing.conj())
    outs = []
    for labels in ("01", "+-"):
        rho_m = sum(np.kron(proj(l), np.eye(2)) @ rho_AB @ np.kron(proj(l), np.eye(2)) for l in labels)
        rb = ptrace(rho_m, [2, 2], [1])
        dt = 3.0 / 300
        for _ in range(300):
            ex = float(np.trace(rb @ NL.X).real)
            Uh = NL.U(eps * ex * NL.Z, dt)
            rb = Uh @ rb @ Uh.conj().T
        outs.append(rb)
    return float(np.abs(outs[0] - outs[1]).max())


# =====================================================================================================================
# PART (iii) -- does a preferred frame remove O-BITS?
# =====================================================================================================================
def ordering_test(n_angles=7):
    """nosig.py's singlet and projectors.  Two time orderings of the same spacelike pair of measurements -- Alice
    first (cosmic frame, say) and Bob first (another frame) -- computed as SEQUENTIAL Lueders updates.  Returns
    (max |P_Alice-first - P_Bob-first| over joint outcomes, max |P(Bob=+1 | a) - 1/2| over Alice's angles)."""
    np = _np()
    N = _quiet("nosig")
    s, P = N.s, N.P
    b = math.pi / 4
    worst_order = worst_bob = 0.0
    for a in np.linspace(0, math.pi, n_angles):
        pb_plus = 0.0
        for oa in (1, -1):
            for ob in (1, -1):
                PA, PB = np.kron(P(a, oa), np.eye(2)), np.kron(np.eye(2), P(b, ob))
                v1 = PB @ (PA @ s)                    # Alice first
                v2 = PA @ (PB @ s)                    # Bob first
                p1, p2 = float(np.vdot(v1, v1).real), float(np.vdot(v2, v2).real)
                worst_order = max(worst_order, abs(p1 - p2))
                if ob == 1:
                    pb_plus += p1
        worst_bob = max(worst_bob, abs(pb_plus - 0.5))
    return worst_order, worst_bob


def nonlocal_control():
    """CONTROL that must signal: Alice's choice c in {0, 1} applies X^c to her qubit, then a CNOT (Alice control,
    Bob target) -- a NON-local operation.  Bob's P(0) then depends on c.  Returns |P(0|c=0) - P(0|c=1)|."""
    np = _np()
    psi = np.kron(np.array([1, 0], complex), np.array([1, 0], complex))
    X = np.array([[0, 1], [1, 0]], complex)
    CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], complex)
    p = []
    for c in (0, 1):
        v = CNOT @ np.kron(np.linalg.matrix_power(X, c), np.eye(2)) @ psi
        p.append(float(ptrace(np.outer(v, v.conj()), [2, 2], [1])[0, 0].real))
    return abs(p[0] - p[1])


def transit_without_bits():
    """../transit.py: Bob's state when the two classical bits are withheld, for three inputs.  No time coordinate
    enters the computation, so no choice of frame can change it.  Returns max |rho_B - I/2|."""
    T = _quiet("transit")
    worst = 0.0
    for psi in ([1 + 0j, 0j], [2 ** -0.5 + 0j, 2 ** -0.5 + 0j], [0.6 + 0j, 0.8j]):
        r = T.b_state_without_bits(psi)
        worst = max(worst, max(abs(r[i][j] - (0.5 if i == j else 0)) for i in range(2) for j in range(2)))
    return worst


def reply_arrival(u, v=Fr(3, 5), L=Fr(1)):
    """An instantaneous reply keyed to the frame moving with velocity u (c = 1): it leaves B's event (t = 0, x = L)
    and reaches A's worldline x = 0 at the cosmic time t_A for which the two events share frame u's time coordinate,
    t' = gamma(u) (t - u x).  Solved with sympy from the Lorentz transformation, not typed.  v is B's velocity and
    enters only through which u the reply is keyed to."""
    import sympy as sp
    t, uu = sp.symbols("t u", real=True)
    gamma = 1 / sp.sqrt(1 - uu ** 2)
    tprime = lambda tt, xx: gamma * (tt - uu * xx)
    sol = sp.solve(sp.Eq(tprime(t, 0), tprime(0, sp.Rational(L.numerator, L.denominator))), t)
    val = sp.nsimplify(sol[0].subs(uu, sp.Rational(u.numerator, u.denominator)))
    return Fr(int(sp.numer(val)), int(sp.denom(val)))


def antitelephone(v=Fr(3, 5), L=Fr(1)):
    """H-FRAME paired with any superluminal channel.  A at rest at x = 0, B at x = L at t = 0 moving with v (c = 1).
    A's instantaneous signal (keyed to the cosmic slice) reaches B at t = 0.  B replies instantaneously, keyed to
    B's rest frame (u = v) or to the cosmic frame (u = 0).  BOTH values are computed by reply_arrival.  Wave 1 first
    returned 'v*(0-L), Fr(0)': the cosmic value was a typed literal 0 (C-verify-0 #6).
    Returns (reply arrival keyed to the sender's frame, keyed to the cosmic frame)."""
    return reply_arrival(v, v, L), reply_arrival(Fr(0), v, L)


def c2_needs_a_frame(sig):
    """C2 is frame-dependent: if Bob's D-CTC interaction precedes Alice's measurement (true in some frame for a
    spacelike pair), no branch exists and C2 returns the reduced-state value; if it follows, the branch value.
    Returns (P0 Bob-first, P0 Alice-first-z, P0 Alice-first-x).  NOTE (wave 2): this is the D-CTC circuit, which needs
    a closed timelike curve at Bob -- excluded by clause 1 (C-verify-0 #5).  The drift's own ordering dependence is
    drift_ordering below."""
    return sig[("C2", "none")], sig[("C2", "z")], sig[("C2", "x")]


def drift_ordering(eps=0.1, T=3.0, fracs=(0.0, 0.25, 0.5, 0.75, 1.0), n=3000):
    """Wave 2: 'C2 needs a frame' COMPUTED FOR THE DRIFT (nlcontrol's H = eps <X> Z, imported), not only for the
    D-CTC circuit.  Bob's drift window is [0, T] in some frame's time; Alice measures at t_A = frac * T in that same
    frame (frac = 1: Bob-first, Alice after the window).  Under C2 there is no branch before t_A: Bob's state is his
    reduced state I/2, <X> = 0 and the drift does nothing; from t_A it runs on the branch state for T - t_A.
    Returns {frac: Bob's <sigma_y>_x - <sigma_y>_z at the end}.  Frames that order the events differently give
    different values for the same events, so C2 is undefined without a preferred slicing.  Exact: tanh(2 eps (T - t_A))."""
    np = _np()
    NL = _quiet("nlcontrol")
    out = {}
    sing = np.array([0, 1, -1, 0], complex) / math.sqrt(2)
    for f in fracs:
        # before t_A: the drift is COMPUTED on Bob's reduced state (the only state C2 has before a branch exists);
        # the unitary it generates acts on Bob's qubit, and so on every later branch state
        rb = ptrace(np.outer(sing, sing.conj()), [2, 2], [1])
        Upre = np.eye(2, dtype=complex)
        steps = int(round(n * f))
        dt = T / n
        for _ in range(steps):
            ex = float(np.trace(rb @ NL.X).real)
            Uh = NL.U(eps * ex * NL.Z, dt)
            rb = Uh @ rb @ Uh.conj().T
            Upre = Uh @ Upre
        rest = (1.0 - f) * T
        ys = {}
        for b in ("x", "z"):
            vals = []
            for s0 in NL.ENS[b]:
                e = Upre @ np.array(s0, complex)
                if rest > 0:
                    e = NL.evolve(e, eps, False, T=rest, n=max(10, n - steps))
                vals.append(float(np.real(e.conj() @ NL.Y @ e)))
            ys[b] = sum(vals) / len(vals)
        out[f] = ys["x"] - ys["z"]
    return out


BB84_READ_MAP = {"0": "00", "1": "01", "+": "10", "-": "11"}   # BHW 0811.1209v2 p.2 (READ): |00>->|00>, |10>->|01>,
                                                                 # |+0>->|10>, |-0>->|11>; first output bit a = basis


def bhw_bb84_unitary():
    """BHW Fig. 2 / p.3 Theorem construction (READ): SWAP the two chronology-respecting qubits with the two CTC
    qubits, then the controlled unitary sum_k |k><k| (x) U_k (system controls, CTC targets), with BHW eq.(3):
    U00 = SWAP, U01 = X(x)X, U10 = (X(x)I)(H(x)I), U11 = (X(x)H) SWAP.  Ordering (sys1, sys2, ctc1, ctc2)."""
    np = _np()
    I2 = np.eye(2, dtype=complex)
    Xm = np.array([[0, 1], [1, 0]], complex)
    Hd = np.array([[1, 1], [1, -1]], complex) / math.sqrt(2)
    SW = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], complex)
    U = {0: SW, 1: np.kron(Xm, Xm), 2: np.kron(Xm, I2) @ np.kron(Hd, I2), 3: np.kron(Xm, Hd) @ SW}
    ctrl = sum(np.kron(np.outer(np.eye(4)[k], np.eye(4)[k]), U[k]) for k in range(4))
    swap_sys_ctc = np.zeros((16, 16), complex)
    for i in range(4):
        for j in range(4):
            swap_sys_ctc[j * 4 + i, i * 4 + j] = 1
    return ctrl @ swap_sys_ctc


def bb84_c2_table():
    """Wave 2: the per-pair capacity of the D-CTC under C2, COMPUTED from BHW's own construction (READ) through this
    file's Deutsch fixed point.  Wave 1 first said 'Per BHW p.2 (READ, not computed here), their BB84 circuit would
    let C2 carry 1 bit per pair' -- a derived figure labelled READ (C-verify-0 #8, C-verify-2 #2).
    Bob holds half a singlet; Alice measures z or x; under C2 Bob's input is his branch state (a BB84 state) with an
    ancilla |0>; he reads the first output bit a.  Under C1 his input is his reduced state I/2 (x) |0><0|, the same
    for both of Alice's choices.  Returns the READ-map reproduction, P(a = 1 | choice) per convention, I(choice; a)
    in bits per pair per convention, and the fixed-point dimensions seen."""
    np = _np()
    V = bhw_bb84_unitary()
    z0 = np.array([1, 0], complex)
    dims, repro = set(), {}
    for lab, want in BB84_READ_MAP.items():
        psi = np.kron(np.array(KET[lab], complex), z0)
        out, sig, k, res, mn = deutsch_output(V, np.outer(psi, psi.conj()), 4, 4)
        dims.add(k)
        repro[lab] = float(out[int(want, 2), int(want, 2)].real)
    other = {"0": "1", "1": "0", "+": "-", "-": "+"}

    def p_a1(rho_sys):
        out, *_ = deutsch_output(V, rho_sys, 4, 4)
        return float(out[2, 2].real + out[3, 3].real)
    res = {}
    for basis, labels in (("z", "01"), ("x", "+-")):
        acc = 0.0
        for l in labels:                      # Alice's outcome l leaves Bob (singlet) in other[l]
            psi = np.kron(np.array(KET[other[l]], complex), z0)
            acc += 0.5 * p_a1(np.outer(psi, psi.conj()))
        res[("C2", basis)] = acc
        rho_c1 = np.kron(np.eye(2) / 2, np.outer(z0, z0.conj()))
        res[("C1", basis)] = p_a1(rho_c1)
    Hb = lambda p: -sum(q * math.log2(q) for q in (p, 1 - p) if q > 1e-15)
    mi = {c: Hb((res[(c, "z")] + res[(c, "x")]) / 2) - (Hb(res[(c, "z")]) + Hb(res[(c, "x")])) / 2 for c in ("C1", "C2")}
    return {"read_map_reproduced": repro, "P(a=1)": res, "MI_bits_per_pair": mi, "fixed_point_dims": sorted(dims)}


def _bloch_ket(n):
    np = _np()
    x, y, z = n
    th = math.acos(max(-1.0, min(1.0, z)))
    ph = math.atan2(y, x)
    return np.array([math.cos(th / 2), complex(math.cos(ph), math.sin(ph)) * math.sin(th / 2)], complex)


def _gs(vecs, v, tol=1e-10):
    np = _np()
    for b in vecs:
        v = v - b * (b.conj() @ v)
    n = np.linalg.norm(v)
    return None if n < tol else v / n


def bhw_general_unitaries(states, tol=1e-9):
    """Wave 3.  BHW 0811.1209v2 p.3-4 (READ), the Theorem's construction for N distinct states in dimension N: for
    each k, U_k = sum_m |c_m><b_m| with b_1 = psi_k, c_1 = |k>; then repeatedly Gram-Schmidt an unused state into
    the next b, collect every unused state now inside span(b_1..b_t), and set c_t to the normalised sum of their |j>;
    complete both bases arbitrarily.  Conditions (p.3): U_k psi_k = |k>, and <j|U_k|psi_j> != 0 for all j, k
    (sufficient for a unique fixed point).  Returns the list U_k."""
    np = _np()
    N = len(states)
    I = np.eye(N, dtype=complex)
    Us = []
    for k in range(N):
        bs, cs, used = [states[k] / np.linalg.norm(states[k])], [I[k]], {k}
        while len(used) < N:
            t = min(j for j in range(N) if j not in used)
            bs.append(_gs(bs, states[t]))
            P = sum(np.outer(x, x.conj()) for x in bs)
            grp = [j for j in range(N) if j not in used and np.linalg.norm(P @ states[j] - states[j]) < tol]
            used |= set(grp)
            cs.append(sum(I[j] for j in grp) / math.sqrt(len(grp)))
        for basis in (bs, cs):
            for e in I:
                if len(basis) == N:
                    break
                v = _gs(basis, e)
                if v is not None:
                    basis.append(v)
        Us.append(sum(np.outer(c, b.conj()) for c, b in zip(cs, bs)))
    return Us


def bhw_general_V(Us):
    """SWAP(system, CTC), then sum_k |k><k| (x) U_k (system controls, CTC target).  Ordering (system, CTC)."""
    np = _np()
    N = len(Us)
    ctrl = sum(np.kron(np.outer(np.eye(N)[k], np.eye(N)[k]), Us[k]) for k in range(N))
    sw = np.zeros((N * N, N * N), complex)
    for i in range(N):
        for j in range(N):
            sw[j * N + i, i * N + j] = 1
    return ctrl @ sw


FOUR_AXES = ((0.0, 0.0, 1.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (3 ** -0.5, 3 ** -0.5, 3 ** -0.5))


def four_basis_c2_table(axes=FOUR_AXES):
    """Wave 3 (RV-0 unresolved #4; RV-1 unresolved #0; C-verify-1 #7's figure, cited by A2 wave 2 as 'not re-run',
    now COMPUTED).  Alice measures her singlet half along one of len(axes) axes (uniform prior); outcome s leaves
    Bob's qubit along -s n.  Bob appends a two-qubit ancilla |00> and runs BHW's general construction
    (bhw_general_unitaries) on the 8 branch states with an 8-dimensional CTC, through this file's Deutsch fixed point;
    he reads output j and decodes Alice's axis as j // 2.  C2: each branch is run separately (the rule per branch).
    C1: his input is his reduced state I/2 (x) |00><00| for every choice.  Returns the map reproduction (P(j | psi_j)),
    the BHW condition-2 minimum, fixed-point dimensions, P(axis' | axis) per convention and I(axis; axis') in bits."""
    np = _np()
    anc = np.zeros(4, complex)
    anc[0] = 1
    states = [np.kron(_bloch_ket(tuple(-s * c for c in n)), anc) for n in axes for s in (+1, -1)]
    N = len(states)
    if N != 8:
        raise ValueError("this table is built for four axes (8 branch states in C^8)")
    Us = bhw_general_unitaries(states)
    cond2 = min(abs((Us[k] @ states[j])[j]) for j in range(N) for k in range(N))
    V = bhw_general_V(Us)
    outs, dims, repro = {}, set(), {}
    for j, psi in enumerate(states):
        out, sig, kdim, res, mn = deutsch_output(V, np.outer(psi, psi.conj()), N, N)
        outs[j] = np.real(np.diag(out))
        dims.add(kdim)
        repro[j] = float(outs[j][j])
    nb = len(axes)
    pc2 = [[sum(0.5 * outs[2 * b + s][2 * bb + t] for s in (0, 1) for t in (0, 1)) for bb in range(nb)] for b in range(nb)]
    out1, *_ = deutsch_output(V, np.kron(np.eye(2) / 2, np.outer(anc, anc.conj())), N, N)
    d1 = np.real(np.diag(out1))
    pc1 = [[float(d1[2 * bb] + d1[2 * bb + 1]) for bb in range(nb)] for _ in range(nb)]

    def mi(P):
        H = lambda q: -sum(x * math.log2(x) for x in q if x > 1e-15)
        col = [sum(P[b][bb] for b in range(nb)) / nb for bb in range(nb)]
        return H(col) - sum(H(P[b]) for b in range(nb)) / nb
    return {"map_reproduced": repro, "cond2_min": float(cond2), "fixed_point_dims": sorted(dims),
            "P(axis'|axis) C2": pc2, "P(axis'|axis) C1": pc1, "MI_bits_per_pair": {"C2": mi(pc2), "C1": mi(pc1)}}


def four_basis_one_axis_control():
    """CONTROL (must give 0): the four 'choices' all name the SAME axis (z).  The branch states then repeat, so
    BHW's construction does not apply to 8 distinct states; the channel is evaluated directly: every choice gives
    Bob the same mixture, whatever circuit he runs, so I = 0 must come out of the same decoding code path.  Here the
    BB84 construction (bhw_bb84_unitary) is used on the repeated z-states."""
    np = _np()
    V = bhw_bb84_unitary()
    z0 = np.array([1, 0], complex)
    rows = []
    for _ in range(4):
        acc = np.zeros(4)
        for lab in "01":
            psi = np.kron(np.array(KET["1" if lab == "0" else "0"], complex), z0)
            out, *_ = deutsch_output(V, np.outer(psi, psi.conj()), 4, 4)
            acc += 0.5 * np.real(np.diag(out))
        rows.append([float(x) for x in acc])
    H = lambda q: -sum(x * math.log2(x) for x in q if x > 1e-15)
    col = [sum(r[i] for r in rows) / 4 for i in range(4)]
    return H(col) - sum(H(r) for r in rows) / 4


# =====================================================================================================================
# THE GRADES (data; the write-up is A2-frame.md)
# =====================================================================================================================
GRADES = {
    # Wave 2: clause 1 is M's 'a preferred frame exists'; 'corridors keyed to it' is the docket's modelling addition
    # (H-KEYING) -- EXCEPT in exact flat FRW, where frw_time_function_lemma shows only equal-cosmic-time
    # identifications are isometries, so the keying is FORCED by H-FRW-EXACT + H-NOT-DE-SITTER (C-verify-1 #6, #9).
    # Wave 3 (RV-0 #3, #12; RV-1 #2, #9): the FRW removal of corridor loops is credited to the GEOMETRY and to no
    # hypothesis, uniformly; under ITB + N_QTOPO the lemma and latticectc's theorem do not bind an ITB corridor.
    "H-FRAME clause 1 (a preferred frame exists)": {
        "O-LOOP": "REMOVED-IF {H-CORRIDOR-MODEL, H-KEYING} in the corridor-as-identification model (a keyed network "
                  "closes no causal curve at any rank: latticectc H1-H3, Sylvester); in exact flat FRW the corridor "
                  "removal is the GEOMETRY's, REMOVED-IF {H-FRW-EXACT, H-NOT-DE-SITTER, H-CORRIDOR-MODEL}, credited to "
                  "no hypothesis (clause 1 adds nothing for corridors there; fails in exact de Sitter); for SIGNALS "
                  "(only where a channel exists) REMOVED-IF {N_SIGKEY} (antitelephone computed: -3/5 vs 0)",
        "O-BITS": "LEAVES -- no-signalling holds in every ordering (sequential Lueders, deviation 0 to rounding)",
        "O-MAKE": "LEAVES -- and closes one escape: Geroch's kinematic theorem (board D67 NARROWED) allows "
                  "compact topology change only WITH a CTC; a global time function excludes that clause",
        "O-HOLD": "LEAVES -- says nothing about the throat's NEC",
        "O-MATTER": "LEAVES -- says nothing about the seat",
    },
    "H-FRAME clause 2 (messages into the past)": {
        "2a coordinate past of a moving frame": "ADMITTED by clause 1 (e.g. -1.23e-3 yr per light-year for the "
                                                "barycentre); no loop; M's sentence is satisfied by clause 1 + 2a",
        "2b past of the cosmic clock": "EXCLUDED by the docket's keying (H-KEYING) or, in exact FRW, by the geometry -- "
                                       "if corridors are the only route to the cosmic past (H-2B-VIA-CORRIDOR); "
                                       "inside the model ONE such corridor beside one suitably oriented cosmic "
                                       "corridor closes a causal curve for EVERY T > 0 (O-LOOP returns); Hawking's "
                                       "conjecture would forbid it but is a conjecture (OPEN); Deutsch/Novikov make a "
                                       "loop consistent, not absent",
        "2b O-BITS (wave 3, RV-1 #1)": "REMOVED-IF {a CTC at Bob, H-DCTC, H-DCTC-CONVENTION C2, H-DCTC-SELECT}: "
                                       "1.000000 bit per pair (BB84, 2 pairs per teleported qubit) and 2.000000 bits "
                                       "per pair (four axes, four_basis_c2_table: 1 pair per teleported qubit), both "
                                       "ZERO-ERROR (every fixed point unique, P = 1), with O-LOOP REINTRODUCED; under C1 "
                                       "0 bits.  Wave 2 first said 'LEAVES; a channel needs H-SETTLE under C2'",
        "2b O-MAKE (wave 3, RV-0 #7)": "NOT-BOUND-IF {clause 2b's CTC; Geroch's compact case only}: Geroch's 'no CTC' "
                                       "hypothesis fails, so it does not bind, and its conclusion is not shown false; "
                                       "Tipler's non-compact case still binds (a CTC does not escape it); bought with "
                                       "O-LOOP, which 2b reintroduces.  Wave 2 first said 'OPEN (a CTC reopens the "
                                       "Geroch clause)'",
    },
    "H-FRAME + H-SETTLE-W under C2 (the drift, not the D-CTC)": {
        "O-BITS": "REMOVED-IF {N_EPS (A1: eps > eps_any(L, N)), H-C2 (incl. its no-branch-before-t_A rule), "
                  "H-FRAME3b (= clause 1's substance: clause 1 is load-bearing here), H-COHERE, H-NLCONTROL-FORM, "
                  "H-BORN-AT-BOB, H-BLOCK}; window (exclusion) premises, separate: {H-MAP, H-TRANSFER, H-SPIN, "
                  "H-DILUTION, the NAMED-NOT-READ bound values}.  Pair counts from N x C >= 2 are FLOORS.  Wave 1 "
                  "first listed O-BITS under 'removes' unconditionally, grounded on the D-CTC's 0.0817 bits; wave 2 "
                  "listed H-MAP/H-TRANSFER/H-SPIN among the removal premises",
        "O-LOOP": "signals: REMOVED-IF {N_SIGKEY} (antitelephone: reply keyed to the cosmic frame arrives at t = 0, "
                  "computed); corridors: the geometry's, as above",
        "ordering": "computed for the drift (drift_ordering) GIVEN H-C2's rule (no branch before t_A, so the reduced "
                    "state): Bob's signal is tanh(2 eps (T - t_A)) -- 0.537 if Alice measures before Bob's window; "
                    "'0 if after' is that rule's output (STRUCTURAL, H = 0 on I/2), so 'C2 is undefined without a "
                    "slicing' is derived given the rule",
        "O-MAKE": "LEAVES", "O-HOLD": "LEAVES", "O-MATTER": "LEAVES",
    },
    "D-CTC (Deutsch) under C2 -- needs a CTC at Bob, so it cannot coexist with clause 1 (a clause-2b world)": {
        "O-BITS": "REMOVED-IF {a CTC at Bob, H-DCTC, H-DCTC-CONVENTION C2, H-DCTC-SELECT}: BHW circuit 0.0817 bits "
                  "per use; BHW BB84 1.000 bit per pair (2 pairs per teleported qubit); four axes 2.000 bits per pair "
                  "(1 pair per teleported qubit), zero-error; under C1 0 bits; BHW p.4 (READ): unbounded if CTC qubits "
                  "are a free resource",
        "O-LOOP": "REINTRODUCED -- the channel IS a closed timelike curve; M-S1A-P3 disqualifies it at the seat only",
    },
}

NAMED_HYPOTHESES = [
    "H-CORRIDOR-MODEL: a corridor is an identification of positions by a translation (latticectc H1-H3 in flat "
    "space; comoving spatial translations in FRW)",
    "H-FRW-EXACT: the universe is exactly spatially flat FRW (perturbations break even the translation symmetry; "
    "then no identification is an exact isometry)",
    "H-CMB-IS-COSMIC: the comoving frame is the CMB-dipole-free frame -- needs the dipole's kinematic reading (D67 "
    "H1, contested by the matter dipole, NAMED-NOT-READ) and the barycentre reference point (D67 H2)",
    "H-NOT-DE-SITTER: a(t) is not exactly exponential; in exact de Sitter a dilation-time-translation is an "
    "isometry and its quotient has a CTC",
    "H-KILLING-SEARCH: the Killing search covered d_x, d_t, the Minkowski-form boost, and the dilation family "
    "d_t - c x.d_x; x-dependent xi^t was not exhausted",
    "H-DCTC: Deutsch's model (consistency condition on density matrices) -- one model among several (P-CTCs, "
    "Svetlichny; BLSS refs 20-25), not established physics",
    "H-DCTC-CONVENTION: C1 (rule on the whole system / reduced state) vs C2 (rule per branch)",
    "H-DCTC-SELECT: where the fixed point is not unique, a selection rule is a further hypothesis (Deutsch's own "
    "rule NAMED-NOT-READ)",
    "H-LINEAR-QM for part (iii)",
    "H-KEYING (wave 2): corridors are keyed to the preferred frame -- the docket's modelling addition to M's "
    "sentence, not M's words; forced by the geometry only under H-FRW-EXACT + H-NOT-DE-SITTER",
    "H-2B-VIA-CORRIDOR (wave 2): corridors are the only route to the cosmic past (combine's B-2B); without it clause "
    "2b is not excluded by clause 1",
    "N_SIGKEY (wave 2): a superluminal signal is keyed to the same slice as the corridors (A1's H-SIG-COR)",
    "H-C2 / H-BORN-AT-BOB (wave 2): as in settle.py -- the drift acts on the branch state; Bob reads by the Born rule",
    "H-C2 rule (wave 3, RV-0 #11): part of H-C2 -- before Alice's measurement in the chosen slicing there is no branch, "
    "so the drift acts on Bob's reduced state; drift_ordering's 'Bob first gives 0' is this rule's output",
    "H-BLOCK (wave 3): reliable transfer is block-coded; pair counts from N x C >= 2 are floors (settle.zero_error_table)",
    "H-FRAME3b => F1 (wave 3, RV-0 #2): the drift's preferred slicing is clause 1's substance",
    "CTC at Bob (wave 3): clause 2b's D-CTC channel needs a closed timelike curve at Bob -- not shown to exist",
    "N_QTOPO / N_CORR clash (wave 3, RV-1 #2): an ITB corridor that is not a Lorentzian object (N_QTOPO) cannot also be "
    "a Lorentzian quotient by translation (N_CORR, H-CORRIDOR-MODEL); under ITB + N_QTOPO the FRW lemma and "
    "latticectc's theorem do not bind it: corridor O-LOOP NOT-BOUND-IF {N_QTOPO}; signal loops unchanged",
]


# =====================================================================================================================
def report():
    print("frame.py -- DOCKET 68, A2-frame: H-FRAME and the curvature pairing\n")
    print("(i) CORRIDOR NETWORKS UNDER A PREFERRED FRAME")
    for rank in (2, 3):
        n, bad = cosmic_keyed_rank_n_is_safe(rank, 300)
        print(f"  cosmic-keyed rank-{rank} lattices (exact Sylvester): {n} tested, non-positive-definite: {bad}")
    E1, E2 = _quiet("corridors").E1, _quiet("corridors").E2
    L = _quiet("corridors").L
    print(f"  CONTROL corridors.py two-frame witness: span {L.span_kind(E1, E2)}, CTC {L.box_has_causal(E1, E2)}"
          f"; E1 is keyed to the frame v = {simultaneity_velocity(E1[0], E1[1])}")
    kind, mn, nrm = past_corridor_witness()
    print(f"  clause 2b: a corridor 1/10 into the cosmic past + one cosmic corridor (0,1,1/100,0): span {kind}, "
          f"lattice vector {mn}, norm {nrm} -> closed causal curve")
    det, chk = past_corridor_condition()
    print(f"  general: Gram det = {det}  (identity check {chk}); <0 iff b^2 (L^2-T^2) < T^2 a^2: every T > 0 has one")
    kt = frw_killing_table()
    for k, v in kt.items():
        print(f"  Killing: {k}: {v}")
    iso, img, tn = de_sitter_identification_closes()
    print(f"  de Sitter: phi isometry {iso}; phi(t0, 0) = {img}; segment tangent norm {tn} -> CTC in the quotient")
    zl = frw_time_function_lemma()
    print(f"  z3 time-function lemma: claim {zl['claim']} (unsat = proved), vacuity {zl['vacuity']}, "
          f"drift {zl['drift']:.1e}, control a>=0 {zl['control_a_ge_0']} (sat = fails as it must)")
    dt, beta = cmb_coordinate_past()
    print(f"  CMB frame: a cosmic-simultaneous 1-light-year corridor along the dipole arrives dt' = {dt:.1f} s "
          f"({dt / 3600:.3f} h) in the barycentre's coordinate time (v/c = {beta:.5e})")
    for vk in (340.65, 399.08):
        print(f"    Earth at {vk} km/s: {cmb_coordinate_past(1.0, vk)[0]:.1f} s")
    print("\n(ii) DEUTSCH'S FIXED POINT ON A QUBIT CTC")
    for lab in ("0", "-", "1", "+"):
        p, k, r = bhw_p0(proj(lab))
        print(f"  BHW circuit, input |{lab}>: P(A=0) = {p:.6f}  fixed-point space dim {k}  residual {r:.1e}")
    np = _np()
    p_mix = bhw_p0(np.eye(2) / 2)[0]
    print(f"  input I/2: P(A=0) = {p_mix:.6f}; linear mixture of |0>,|1> outputs would give "
          f"{(bhw_p0(proj('0'))[0] + bhw_p0(proj('1'))[0]) / 2:.6f}  -> NONLINEAR")
    out, sig, k = blss_epr_fixture()
    print(f"  BLSS EPR fixture: rho_CTC = I/2 {np.allclose(sig, np.eye(2) / 2)}, rho'_AB = I/4 "
          f"{np.allclose(out, np.eye(4) / 4)}")
    print("  existence census (trials, failures, max residual, min eig, non-unique):", existence_census())
    sig_t = signalling_table()
    for conv in ("C1", "C2"):
        print(f"  {conv}: P(Bob=0 | Alice none/z/x) = {sig_t[(conv, 'none')]:.6f} / {sig_t[(conv, 'z')]:.6f} / "
              f"{sig_t[(conv, 'x')]:.6f}   I(choice; Bob) = {sig_t[(conv, 'MI bits')]:.6f} bits")
    bf, az, ax = c2_needs_a_frame(sig_t)
    print(f"  C2 is frame-dependent: Bob-first {bf:.6f} vs Alice-first {az:.6f} (z) / {ax:.6f} (x)")
    print(f"  H-SETTLE under C1 (nlcontrol drift on rho_B): max |rho_B(z) - rho_B(x)| = {settle_under_C1():.1e}")
    do = drift_ordering()
    print("  WAVE 2 -- the DRIFT's ordering dependence under C2 (Alice measures at t_A = frac x T of Bob's window):")
    print("    " + ", ".join(f"frac {f}: {v:.5f} (exact {math.tanh(2 * 0.1 * 3.0 * (1 - f)):.5f})" for f, v in do.items()))
    bb = bb84_c2_table()
    print(f"  WAVE 2 -- BHW BB84 construction (READ, p.2-3) through this file's Deutsch fixed point: READ map reproduced "
          f"{bb['read_map_reproduced']}; fixed-point dims {bb['fixed_point_dims']}")
    print(f"    P(a = 1 | Alice z / x): C2 {bb['P(a=1)'][('C2', 'z')]:.6f} / {bb['P(a=1)'][('C2', 'x')]:.6f};"
          f" C1 {bb['P(a=1)'][('C1', 'z')]:.6f} / {bb['P(a=1)'][('C1', 'x')]:.6f};  I = C2 {bb['MI_bits_per_pair']['C2']:.6f},"
          f" C1 {bb['MI_bits_per_pair']['C1']:.6f} bits per pair")
    fb = four_basis_c2_table()
    print(f"  WAVE 3 -- BHW general construction, four axes, 8-dim CTC: map reproduced (min) {min(fb['map_reproduced'].values()):.9f};"
          f" condition 2 min {fb['cond2_min']:.4f}; fixed-point dims {fb['fixed_point_dims']}")
    print(f"    I(axis; Bob) = C2 {fb['MI_bits_per_pair']['C2']:.6f}, C1 {fb['MI_bits_per_pair']['C1']:.6f} bits per pair;"
          f" CONTROL one axis named four times: {four_basis_one_axis_control():.2e}")
    print("\n(iii) DOES A PREFERRED FRAME REMOVE O-BITS?")
    wo, wb = ordering_test()
    print(f"  Alice-first vs Bob-first joint distributions: max diff {wo:.1e}; max |P(Bob=+1|a) - 1/2| {wb:.1e}")
    print(f"  CONTROL non-local CNOT: Bob's P(0) moves by {nonlocal_control():.3f} (must be > 0)")
    print(f"  transit.py without the two bits: max |rho_B - I/2| = {transit_without_bits():.1e}")
    sf, cf = antitelephone()
    print(f"  superluminal reply keyed to the sender's frame arrives at t = {sf}; keyed to the cosmic frame t = {cf}")
    print("\nGRADES"); [print(f"  {h}\n    " + "\n    ".join(f"{o}: {g}" for o, g in d.items())) for h, d in GRADES.items()]
    print("\npre-docket import output captured (chars):", _IMPORT_LOG)


# =====================================================================================================================
def selftest():
    np = _np()
    fails = []

    structural, n_checks, n_controls = [], [0], [0]

    def chk(label, got, want, tol=None):
        ok = (abs(got - want) <= tol) if tol is not None else (got == want)
        n_checks[0] += 1
        n_controls[0] += label.strip().startswith("CONTROL")
        print(f"  {'ok  ' if ok else 'FAIL'} {label}: got {got!r} want {want!r}")
        if not ok:
            fails.append(label)

    print("frame.py --selftest")
    print(" (i) corridors")
    for rank in (2, 3):
        chk(f"cosmic-keyed rank-{rank}: non-positive-definite Grams", cosmic_keyed_rank_n_is_safe(rank, 200)[1], 0)
    C = _quiet("corridors")
    chk("CONTROL two-frame witness E1,E2 closes (latticectc, board)", C.L.box_has_causal(C.E1, C.E2), True)
    chk("E1 is keyed to the frame v = 9/10", simultaneity_velocity(C.E1[0], C.E1[1]), Fr(9, 10))
    kind, mn, nrm = past_corridor_witness()
    chk("CONTROL clause-2b corridor + cosmic corridor: span", kind, "timelike")
    chk("CONTROL clause-2b lattice vector is causal (norm < 0)", nrm is not None and nrm < 0, True)
    chk("cosmic corridor alone beside its own multiples: no CTC (rank 1)",
        C.L.rank1_has_causal((Fr(0), Fr(1), Fr(1, 100), Fr(0))), False)
    det, ident = past_corridor_condition()
    chk("Gram-det identity b^2(L^2-T^2) - T^2 a^2", ident, 0)
    kt = frw_killing_table()
    chk("FINDING frw_frame.g is Minkowski after import", kt["frw_frame_g_was_minkowski_after_import"], True)
    chk("generic a(t): d_x Killing", kt["generic a(t): d_x"], True)
    chk("generic a(t): d_t not Killing", kt["generic a(t): d_t"], False)
    chk("generic a(t): boost not Killing", kt["generic a(t): boost x d_t + t d_x"], False)
    chk("CONTROL Minkowski boost Killing", kt["control Minkowski: boost"], True)
    chk("CONTROL de Sitter dilation-time-translation IS Killing", kt["de Sitter a=exp(Ht): d_t - H x.d_x"], True)
    chk("LambdaCDM sinh^(2/3): dilation not Killing", kt["LambdaCDM a=sinh(t)^(2/3): d_t - x.d_x"], False)
    chk("LambdaCDM sinh^(2/3): d_x Killing", kt["LambdaCDM a=sinh(t)^(2/3): d_x"], True)
    iso, img, tn = de_sitter_identification_closes()
    chk("CONTROL de Sitter identification is an isometry", iso, True)
    chk("  ... and maps (t0,0) to (t0+tau, 0)", str(img), "(t + tau, 0)")
    zl = frw_time_function_lemma()
    chk("z3 time-function lemma (unsat = proved)", zl["claim"], "unsat")
    chk("  vacuity guard: hypothesis satisfiable", zl["vacuity"], "sat")
    chk("  encoding-drift guard vs frw_frame metric", zl["drift"], 0.0, tol=1e-12)
    chk("  CONTROL with a >= 0 the claim fails", zl["control_a_ge_0"], "sat")
    dt, beta = cmb_coordinate_past()
    chk("CMB v/c at 369.82 km/s (D67 audit: 1.23357e-3)", beta, 1.23357e-3, tol=5e-8)
    chk("1-ly cosmic-simultaneous corridor: barycentre dt' (s)", dt, -38929.0, tol=2.0)
    print(" (ii) Deutsch")
    p0, k0, _ = bhw_p0(proj("0"))
    pm, km, _ = bhw_p0(proj("-"))
    chk("READ BHW 0811.1209 p.2: input |0> -> reads 0", p0, 1.0, tol=1e-9)
    chk("READ BHW p.2: input |-> -> reads 1", pm, 0.0, tol=1e-9)
    chk("READ BHW p.2: fixed point unique for |0>", k0, 1)
    chk("READ BHW p.2: fixed point unique for |->", km, 1)
    chk("computed: input |1> -> P0 = 1/3", bhw_p0(proj("1"))[0], 1 / 3, tol=1e-9)
    chk("computed: input |+> -> P0 = 2/3", bhw_p0(proj("+"))[0], 2 / 3, tol=1e-9)
    chk("computed: input I/2 -> P0 = 1/2 (linear would be 2/3)", bhw_p0(np.eye(2) / 2)[0], 0.5, tol=1e-9)
    out, sig, k = blss_epr_fixture()
    chk("READ BLSS 0908.3023 p.1: rho_CTC = I/2", bool(np.allclose(sig, np.eye(2) / 2)), True)
    chk("READ BLSS p.1: rho'_AB = I/4", bool(np.allclose(out, np.eye(4) / 4)), True)
    n, f, worst, mineig, nonu = existence_census(200)
    chk("existence: random U, random rho -- failures", f, 0)
    U_id = np.eye(4, dtype=complex)
    chk("CONTROL U = I: fixed point NOT unique (dim 4)", deutsch_fixed_point(U_id, np.eye(2) / 2, 2, 2)[1], 4)
    st = signalling_table()
    chk("C1: Alice none vs z vs x all 1/2", max(abs(st[("C1", b)] - 0.5) for b in ("none", "z", "x")), 0.0,
        tol=1e-9)
    chk("C1: I(choice; Bob) = 0", st[("C1", "MI bits")], 0.0, tol=1e-9)
    chk("CONTROL C2: Alice z -> 2/3", st[("C2", "z")], 2 / 3, tol=1e-9)
    chk("CONTROL C2: Alice x -> 1/3", st[("C2", "x")], 1 / 3, tol=1e-9)
    chk("CONTROL C2: I(choice; Bob) = 1 - H(2/3) bits", st[("C2", "MI bits")],
        1 - (-(2 / 3) * math.log2(2 / 3) - (1 / 3) * math.log2(1 / 3)), tol=1e-9)
    chk("H-SETTLE drift under C1: no dependence on Alice", settle_under_C1(), 0.0, tol=1e-12)
    print(" (iii) O-BITS")
    wo, wb = ordering_test()
    chk("orderings agree (Alice-first vs Bob-first)", wo, 0.0, tol=1e-12)
    chk("Bob's marginal 1/2 for all 7 of Alice's angles", wb, 0.0, tol=1e-12)
    chk("CONTROL non-local CNOT signals (|dP| = 1)", nonlocal_control(), 1.0, tol=1e-12)
    chk("transit.py: rho_B = I/2 without the bits", transit_without_bits(), 0.0, tol=1e-12)
    sf, cf = antitelephone()
    chk("CONTROL antitelephone keyed to sender's frame (computed by reply_arrival): arrives at -3/5", sf, Fr(-3, 5))
    chk("antitelephone keyed to cosmic frame (computed by reply_arrival, wave 1 typed 0): arrives at 0", cf, Fr(0))
    chk("reply_arrival at u = 1/2, L = 2 is -1 (independent value)", reply_arrival(Fr(1, 2), Fr(3, 5), Fr(2)), Fr(-1))
    print(" (wave 2) the drift's ordering dependence, BHW BB84 under C1/C2, de Sitter tangent")
    do = drift_ordering()
    chk("drift under C2, Alice first (frac 0): tanh(0.6)", do[0.0], math.tanh(0.6), tol=2e-4)
    chk("drift under C2, Alice at mid-window: tanh(0.3)", do[0.5], math.tanh(0.3), tol=2e-4)
    # Wave 3 (RV-0 #11): wave 2 first labelled this row 'CONTROL'.  It integrates the drift on I/2, where <X> = 0, so
    # H = 0 identically: it cannot be nonzero.  It is the output of H-C2's no-branch rule, printed STRUCTURAL.
    structural.append(("drift under C2, Bob's window over before Alice measures (H = 0 on I/2; H-C2's rule)", abs(do[1.0]) < 1e-12))
    print(f"  STRUCTURAL (cannot fail; not evidence) drift under C2, Bob first: got {do[1.0]!r}")
    bb = bb84_c2_table()
    chk("BHW BB84 construction reproduces the READ map for all four inputs", min(bb["read_map_reproduced"].values()), 1.0, tol=1e-9)
    chk("BHW BB84 fixed points unique (dim 1), as BHW p.2-3 claim", bb["fixed_point_dims"], [1])
    chk("D-CTC under C2: 1 bit per pair (computed, wave 1 labelled it READ)", bb["MI_bits_per_pair"]["C2"], 1.0, tol=1e-9)
    chk("CONTROL D-CTC under C1: 0 bits per pair", bb["MI_bits_per_pair"]["C1"], 0.0, tol=1e-9)
    chk("de Sitter segment tangent norm computed (wave 1 typed -1)", tn, -1)
    print(" (wave 3) BHW's general construction: four axes, an 8-dimensional CTC")
    fb = four_basis_c2_table()
    chk("four axes: BHW map psi_j -> |j> reproduced for all 8 branch states", min(fb["map_reproduced"].values()), 1.0, tol=1e-9)
    chk("four axes: BHW condition 2, min |<j|U_k|psi_j>| > 0", fb["cond2_min"] > 1e-3, True)
    chk("four axes: fixed points unique (dim 1)", fb["fixed_point_dims"], [1])
    chk("four axes under C2: 2 bits per pair, zero error (computed; C-verify-1 #7's figure re-run)", fb["MI_bits_per_pair"]["C2"], 2.0, tol=1e-9)
    chk("CONTROL four axes under C1: 0 bits per pair", fb["MI_bits_per_pair"]["C1"], 0.0, tol=1e-9)
    chk("CONTROL four 'choices' naming one axis: 0 bits per pair", four_basis_one_axis_control(), 0.0, tol=1e-9)
    bad_struct = [l for l, g in structural if not g]
    fails += bad_struct
    print(f"\n{'ALL PASS' if not fails else 'FAILURES: ' + ', '.join(fails)}  ({len(fails)} failed; {n_checks[0]} checks, "
          f"{n_controls[0]} controls; {len(structural)} printed STRUCTURAL, not counted, not evidence)")
    return 0 if not fails else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    report()
