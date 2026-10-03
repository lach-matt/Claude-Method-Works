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
    tangent_norm = -1                                                 # d/dt along x = 0: g_tt = -1
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


def antitelephone(v=Fr(3, 5), L=Fr(1)):
    """H-FRAME paired with any superluminal channel (e.g. H-SETTLE under C2).  A at rest at x = 0, B at x = L at
    t = 0 moving with v (c = 1).  A's instantaneous signal reaches B at t = 0.  B replies instantaneously:
      keyed to B's rest frame (simultaneity t = v (x - L)): reaches A at t = -v L  -- before A sent: a loop;
      keyed to the cosmic frame (t = const):                reaches A at t = 0     -- never before.
    Returns (reply arrival keyed to the sender's frame, keyed to the cosmic frame)."""
    return v * (0 - L), Fr(0)


def c2_needs_a_frame(sig):
    """C2 is frame-dependent: if Bob's D-CTC interaction precedes Alice's measurement (true in some frame for a
    spacelike pair), no branch exists and C2 returns the reduced-state value; if it follows, the branch value.
    Returns (P0 Bob-first, P0 Alice-first-z, P0 Alice-first-x)."""
    return sig[("C2", "none")], sig[("C2", "z")], sig[("C2", "x")]


# =====================================================================================================================
# THE GRADES (data; the write-up is A2-frame.md)
# =====================================================================================================================
GRADES = {
    "H-FRAME clause 1 (a preferred frame; corridors keyed to it)": {
        "O-LOOP": "REMOVES -- in the corridor-as-identification model (latticectc H1-H3) and in exact flat FRW "
                  "(comoving identifications): cosmic time is a global time function; no closed causal curve at "
                  "any rank, any a(t) > 0 (z3, exact)",
        "O-BITS": "LEAVES -- no-signalling holds in every ordering (sequential Lueders, deviation 0 to rounding)",
        "O-MAKE": "LEAVES -- and closes one escape: Geroch's kinematic theorem (board D67 NARROWED) allows "
                  "compact topology change only WITH a CTC; a global time function excludes that clause",
        "O-HOLD": "LEAVES -- says nothing about the throat's NEC",
        "O-MATTER": "LEAVES -- says nothing about the seat",
    },
    "H-FRAME clause 2 (messages into the past)": {
        "2a coordinate past of a moving frame": "ADMITTED by clause 1 (e.g. -1.23e-3 yr per light-year for the "
                                                "barycentre); no loop",
        "2b past of the cosmic clock": "EXCLUDED by clause 1; inside the model, ONE such corridor beside one "
                                       "suitably oriented cosmic corridor closes a causal curve for EVERY T > 0 "
                                       "(O-LOOP returns); Hawking's conjecture would forbid it but is a "
                                       "conjecture (OPEN); Deutsch/Novikov make a loop consistent, not absent",
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

    def chk(label, got, want, tol=None):
        ok = (abs(got - want) <= tol) if tol is not None else (got == want)
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
    chk("CONTROL antitelephone keyed to sender's frame: arrives at -3/5", sf, Fr(-3, 5))
    chk("antitelephone keyed to cosmic frame: arrives at 0 (never earlier)", cf, Fr(0))
    print(f"\n{'ALL PASS' if not fails else 'FAILURES: ' + ', '.join(fails)}  ({len(fails)} failed)")
    return 0 if not fails else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    report()
