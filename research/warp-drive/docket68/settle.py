#!/usr/bin/env python3
"""settle.py -- DOCKET 68, work item A1-settle.  H-SETTLE (deterministic drift) alone, H-12's carriers as
drifting parameters, and the stochastic (collapse-type) control.  Not seated.  Write-up: A1-settle.md.

M's definition (CHARTER.md): quantum easing / quantum settling is DETERMINISTIC DRIFT -- "the state's own value
steers its evolution, smoothly and the same every time".  Carried as a hypothesis, never as a result.

WHAT THIS FILE COMPUTES (every number below is computed here, or READ at the locator given):
  A. The signal Bob receives under nlcontrol.py's drift H = eps <X> Z (imported, never copied), versus eps and T.
     EXACT LAW, derived here and checked against nlcontrol's own integrator: for Alice's x-basis ensemble Bob's
     <sigma_y> = tanh(2 eps T); for her z-basis ensemble it is 0.  General closed form for any Bloch vector:
       y(T) = rho_perp * tanh(atanh(y0/rho_perp) + 2 eps rho_perp T),  x keeps its sign,  z constant.
  B. What that signal is worth: bits per pair (mutual information, channel capacity, Holevo chi), the rate per
     pair-second, and the pairs needed per teleported qubit (two classical bits, transit.py).
  C. The published bounds, by FAMILY:
       KR family (Kaplan-Rajendran causal nonlinearity, 2106.10576v2): |eps_gamma| < 1.15e-12 (2411.09611v1),
         4.7e-11 (2204.11875v1), 5.4e-12 (2206.12976v1) -- all READ.  KR's evolution of separated systems
         factorises (2106.10576v2 sec. 2.3, pp.7-8): Bob's statistics move only through retarded Green's functions.
         => the largest SUPERLUMINAL signal this family permits at Bob is 0 for every eps.  O-BITS untouched.
       Weinberg family (deterministic, local on pure states -- the family Gisin's theorem covers and nlcontrol's
         drift belongs to): Majumder et al. 1990 (201Hg) |eps|/2pi <= 3.8 uHz, Walsworth et al. 1990 (H maser)
         3.7e-20 eV (8.9 uHz).  NAMED-NOT-READ: PRLs not on arXiv; the figures are from abstract metadata seen
         through a search index (pmid 10042736, 10041761); no READ arXiv paper restates the numbers.  Bollinger
         1989 (9Be+) and Chupp-Hoare 1990 (21Ne): value OPEN.  Every number derived from them is CONDITIONAL.
  D. The collapse-model control: a stochastic norm-preserving nonlinear equation (QMUPL form, 1204.4325v3
     eq. 23, READ) whose ensemble obeys the LINEAR Lindblad equation (1204.4325v3 p.89, READ) -- must NOT signal,
     while each trajectory changes nonlinearly (vacuity guard).  Must-signal controls: deterministic drift, and
     deterministic drift WITH collapse noise (noise does not launder a deterministic nonlinearity).
  E. H-12: which of V = [M, R, K, T, CP, alpha_s, Z0, Lambda, G, G_F, G_theta, v] could carry a state-dependent
     drift at all, and the measured bound on each one's variation where a READ source has it.
  F. H-SETTLE x H-FRAME: corridors.py imported -- signals keyed to ONE frame close no causal curve.

NAMED HYPOTHESES (every limitation is one):
  H-MAP      the bounded state-dependent precession shift is nlcontrol's 2 eps (full swing of <X>); reading A
             eps = 2 pi f, reading B eps = pi f.  Both reported; neither favoured.
  H-TRANSFER a bound measured on a nuclear/atomic spin applies to Bob's carrier.
  H-SPIN     Weinberg's experiments used spins > 1/2; whether a qubit can carry Weinberg's nonlinearity is OPEN
             here (nlcontrol's eps<X>Z is not rotation-invariant; it is a torsion-class term, cf. 2112.09005v3
             eq. 99 and p.23 "frequency 2 J1 x", READ).
  H-FRAME3b  Gisin's protocol needs the remote preparation on a fixed spacelike hypersurface (2412.20854v1 p.6,
             assumption (3b), READ) -- a preferred slicing.
  H-COHERE   Bob holds coherence for the drift time T.
  H-DILUTION KR p.13 (READ): nonlinear effects can be diluted by cosmic history (eps -> eps/N).
  H-SIG-COR  a signal keyed to a frame is modelled as latticectc's identification (corridors.py's model choice).
  The bound is an UPPER LIMIT measured consistent with ZERO: "not excluded" is never "found".

Run:  python3 settle.py            (report)
      python3 settle.py --selftest (fixtures computed or READ; controls that must fail do)
      python3 settle.py --json PATH
"""
import contextlib
import io
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, ".."))
with contextlib.redirect_stdout(io.StringIO()):      # the pre-docket scripts print at import; keep the report clean
    import nlcontrol as NL                           # H = eps <X> Z, its integrator and ensembles
    import corridors as CO                           # latticectc's THEOREM applied to corridors

X, Y, Z = NL.X, NL.Y, NL.Z
LN2 = math.log(2.0)

# ----------------------------------------------------------------------------------------------- constants
# SI-2019 exact h, e, c; alpha CODATA 2018 -- all via scipy.constants (the restatement D67 recorded as READ).
try:
    import scipy.constants as SC
    H_PLANCK, E_CHARGE, C_LIGHT, ALPHA = SC.h, SC.e, SC.c, SC.fine_structure
    Z0_SCIPY = SC.physical_constants["characteristic impedance of vacuum"][0]
    AU_M, LY_M, YEAR_S = SC.au, SC.light_year, SC.Julian_year
except Exception:                                    # pragma: no cover -- the values themselves, same source
    H_PLANCK, E_CHARGE, C_LIGHT, ALPHA = 6.62607015e-34, 1.602176634e-19, 299792458.0, 7.2973525643e-3
    Z0_SCIPY, AU_M, LY_M, YEAR_S = 376.730313412, 1.495978707e11, 9.4607304725808e15, 365.25 * 86400

# ----------------------------------------------------------------------------------------------- fixtures
# nlcontrol.py's own printed numbers (CHARTER.md line 288, pre-docket, computed): Bob's <sigma_y>, Alice x, T = 3.
NLCONTROL_PRINTED = {1e-3: 0.00600, 1e-2: 0.05993, 1e-1: 0.53706}

BOUNDS_KR = {   # dimensionless eps_gamma, causal (KR) family -- all READ
    "Melnychuk+ 2024 (cryogenic RF)": (1.15e-12, "2411.09611v1 p.1 abstract, p.7 'new bound on |eps| set at <~1.15e-12 at 90.0% CL'"),
    "Brož+ 2022 (trapped-ion Ramsey)": (5.4e-12, "2206.12976v1 p.1 abstract, p.5 '5 +- 5.4e-12' (1 s.d.)"),
    "Polkovnikov+ 2022 (Everett phone, voltage)": (4.7e-11, "2204.11875v1 p.1, p.3 '|eps_gamma| < 4.7e-11, 90% CL'"),
    "KR 2022 ion-trap estimate (eps>0 only)": (1e-5, "2106.10576v2 p.14"),
    "KR 2022 Lamb-shift estimate (as printed in KR v2)": (1e-4, "2106.10576v2 p.14 '|eps_gamma| <~ 1e-4'"),
    "KR Lamb-shift estimate (as restated by Brož)": (1e-2, "2206.12976v1 p.2 'modest bound of |gamma| <~ 1e-2'; p.5"),
}
BOUNDS_WEINBERG = {  # state-dependent precession frequency f (Hz) -- NAMED-NOT-READ, abstract metadata only
    "Majumder+ 1990, 201Hg, PRL 65 2931": {"f_Hz": 3.8e-6, "status": "NAMED-NOT-READ (abstract metadata, pmid 10042736; '|eps|/2pi <= 3.8 uHz')"},
    "Walsworth+ 1990, H maser, PRL 64 2599": {"f_Hz": 8.9e-6, "eV": 3.7e-20,
                                              "status": "NAMED-NOT-READ (abstract metadata, pmid 10041761; '3.7x10^{20} eV (8.9 uHz)' -- exponent sign lost in the text layer)"},
    "Bollinger+ 1989, 9Be+, PRL 63 1031": {"f_Hz": None, "status": "OPEN (abstract truncated before the value; not on arXiv; no READ restatement with the number)"},
    "Chupp & Hoare 1990, 21Ne, PRL 64 2261": {"f_Hz": None, "status": "OPEN (abstract carries no value; not on arXiv)"},
}


# ======================================================================================= A. the drift signal
def bob_y_exact(eps, T):
    """Bob's <sigma_y> after drift time T, Alice measured x (z gives exactly 0).  Derived in derive_law()."""
    return math.tanh(2.0 * eps * T)


def bloch_exact(r0, eps, T):
    """Closed form for H = eps <X> Z on any pure/mixed single-qubit Bloch vector r0 = (x0, y0, z0).
    rho_perp = sqrt(x0^2 + y0^2) is conserved; phi' = 2 eps rho_perp cos(phi);  y = rho_perp tanh(atanh(y0/rho_perp)
    + 2 eps rho_perp T); x keeps its sign (phi never crosses x = 0, a fixed line); z constant."""
    x0, y0, z0 = r0
    rp = math.hypot(x0, y0)
    if rp == 0.0 or x0 == 0.0:
        return (x0, y0, z0)
    s = max(-1.0 + 1e-15, min(1.0 - 1e-15, y0 / rp))
    y = rp * math.tanh(math.atanh(s) + 2.0 * eps * rp * T)
    x = math.copysign(math.sqrt(max(rp * rp - y * y, 0.0)), x0)
    return (x, y, z0)


def bloch_of(psi):
    return tuple(float(np.real(psi.conj() @ s @ psi)) for s in (X, Y, Z))


def bob_numeric(basis, eps, T, obs, lin=False, n=None):
    n = n or max(3000, int(4000 * T))
    return float(np.mean([np.real(e.conj() @ obs @ e) for e in (NL.evolve(s, eps, lin, T=T, n=n) for s in NL.ENS[basis])]))


def derive_law():
    """sympy: phi(t) = 2 atan(tanh(eps t)) solves phi' = 2 eps cos(phi), phi(0) = 0, and sin(phi) = tanh(2 eps t)."""
    import sympy as sp
    e, t = sp.symbols("epsilon t", positive=True)
    phi = 2 * sp.atan(sp.tanh(e * t))
    ode = sp.simplify(sp.diff(phi, t) - 2 * e * sp.cos(phi))
    ident = sp.simplify(sp.sin(phi) - sp.tanh(2 * e * t))
    pts = [(0.1, 3.0), (1e-3, 3.0), (0.37, 0.9), (2.0, 1.3), (5e-2, 40.0)]
    num_ode = max(abs(float(sp.diff(phi, t).subs({e: a, t: b}) - 2 * a * sp.cos(phi.subs({e: a, t: b})))) for a, b in pts)
    num_id = max(abs(float(ident.subs({e: a, t: b}))) for a, b in pts)
    return {"ode_residual_symbolic": str(ode), "identity_residual_symbolic": str(ident),
            "ode_residual_numeric": num_ode, "identity_residual_numeric": num_id}


def ensemble_mean(n_vec, eps, T):
    """Alice measures along unit vector n; Bob (singlet) is left in -n or +n, each w.p. 1/2."""
    a = bloch_exact(tuple(-c for c in n_vec), eps, T)
    b = bloch_exact(tuple(n_vec), eps, T)
    return tuple((p + q) / 2 for p, q in zip(a, b))


def best_basis(eps, T, grid=91):
    """Over Alice's measurement axes (whole sphere, grid), the largest Bob-side Bloch displacement relative to her
    z-basis ensemble (whose mean is 0 for all eps).  Trace distance = |dr|/2."""
    best = (0.0, None)
    for i in range(grid):
        th = math.pi * i / (grid - 1)
        for j in range(2 * grid):
            ph = math.pi * j / grid
            n = (math.sin(th) * math.cos(ph), math.sin(th) * math.sin(ph), math.cos(th))
            m = ensemble_mean(n, eps, T)
            L = math.sqrt(sum(c * c for c in m))
            if L > best[0]:
                best = (L, n)
    return best


# ======================================================================================= B. what the signal is worth
def h2(p):
    return 0.0 if p <= 0.0 or p >= 1.0 else -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def mi(D, q=0.5):
    """Alice picks x (prob q) or z; Bob measures sigma_y.  P(+|z) = 1/2, P(+|x) = (1 + D)/2."""
    p0, p1 = 0.5, (1 + D) / 2
    return h2(q * p1 + (1 - q) * p0) - q * h2(p1) - (1 - q) * h2(p0)


def capacity(D):
    lo, hi = 0.0, 1.0                                 # I(q) is concave in q: golden section
    g = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        a, b = hi - g * (hi - lo), lo + g * (hi - lo)
        if mi(D, a) < mi(D, b):
            lo = a
        else:
            hi = b
    q = (lo + hi) / 2
    return mi(D, q), q


def holevo(D, q=0.5):
    """chi for {z: I/2, x: Bloch (0, D, 0)} with prior q: S(avg) - sum q S."""
    S = lambda L: h2((1 + L) / 2)
    return S(q * D) - q * S(D) - (1 - q) * S(0.0)


def rate_optimum(eps, Tmax_factor=50.0):
    """Maximise capacity(tanh(2 eps T))/T over T: bits per pair per second of Bob's holding time."""
    best = (0.0, 0.0)
    for k in range(1, 4001):
        T = (Tmax_factor / eps) * k / 4000
        r = capacity(math.tanh(2 * eps * T))[0] / T
        if r > best[0]:
            best = (r, T)
    return best


CMAX = capacity(1.0)[0]                               # the D -> 1 ceiling of this two-input family


def eps_to_remove(L_m, N_pairs, frac=0.5):
    """Smallest eps such that N pairs, each held for T = frac * L/c, carry >= 2 bits (one teleported qubit) --
    arriving before light would.  None if N * CMAX < 2 (impossible at any eps)."""
    T = frac * L_m / C_LIGHT
    if N_pairs * CMAX < 2.0:
        return None
    lo, hi = 1e-30, 1e6
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if N_pairs * capacity(math.tanh(2 * mid * T))[0] >= 2.0:
            hi = mid
        else:
            lo = mid
    return hi


def eps_readings(f_Hz):
    return {"A (eps = 2 pi f)": 2 * math.pi * f_Hz, "B (eps = pi f)": math.pi * f_Hz}


# ======================================================================================= D. collapse control
def lindblad_super(H, A, lam):
    I2 = np.eye(2)
    A2 = A @ A
    return (-1j * (np.kron(H, I2) - np.kron(I2, H.T))
            - 0.5 * lam * (np.kron(A2, I2) + np.kron(I2, A2.T) - 2 * np.kron(A, A.T)))


def expm(M):
    nrm = np.linalg.norm(M, 1)
    s = max(0, int(math.ceil(math.log2(nrm))) + 1) if nrm > 0 else 0
    Ms = M / (2 ** s)
    out, term = np.eye(M.shape[0], dtype=complex), np.eye(M.shape[0], dtype=complex)
    for k in range(1, 30):
        term = term @ Ms / k
        out = out + term
    for _ in range(s):
        out = out @ out
    return out


def lindblad_evolve(rho, H, A, lam, T):
    v = expm(lindblad_super(H, A, lam) * T) @ rho.reshape(4)
    return v.reshape(2, 2)


def sde_ensemble(psi0, H, A, lam, T, eps=0.0, n=400, N=4000, seed=11):
    """QMUPL-form stochastic Schrodinger equation (1204.4325v3 eq. 23 with q -> A), Euler-Maruyama, renormalised,
    optionally plus nlcontrol's deterministic drift eps <X> Z.  Returns final states (N x 2)."""
    rng = np.random.default_rng(seed)
    dt = T / n
    P = np.tile(psi0.astype(complex), (N, 1))
    for _ in range(n):
        dW = rng.normal(0.0, math.sqrt(dt), N)
        m = np.real(np.einsum("ni,ij,nj->n", P.conj(), A, P))
        ex = np.real(np.einsum("ni,ij,nj->n", P.conj(), X, P))
        AP = P @ A.T - m[:, None] * P
        A2P = AP @ A.T - m[:, None] * AP
        HP = P @ H.T + eps * ex[:, None] * (P @ Z.T)
        P = P - 1j * HP * dt + math.sqrt(lam) * AP * dW[:, None] - 0.5 * lam * A2P * dt
        P /= np.linalg.norm(P, axis=1)[:, None]
    return P


def bloch_stats(P):
    vals = [np.real(np.einsum("ni,ij,nj->n", P.conj(), s, P)) for s in (X, Y, Z)]
    return [float(v.mean()) for v in vals], [float(v.std() / math.sqrt(len(v))) for v in vals], vals


def signal_detector(stats_z, stats_x):
    """Same detector for every case: largest |difference| of Bob's mean Bloch components between Alice's z and x
    choices, in units of the combined MC standard error (exact cases pass sigma = 0)."""
    (mz, sz), (mx, sx) = stats_z, stats_x
    diffs = [abs(a - b) for a, b in zip(mz, mx)]
    sig = [math.hypot(a, b) for a, b in zip(sz, sx)]
    k = int(np.argmax(diffs))
    return diffs[k], sig[k], (diffs[k] / sig[k] if sig[k] > 0 else (math.inf if diffs[k] > 1e-12 else 0.0))


def collapse_control(seed=11):
    om, lam, T = 0.7, 1.0, 2.0
    H, A = om * Y, X                                 # A = sigma_x collapse, H breaks every reflection symmetry
    states = {"0": np.array([1, 0]), "1": np.array([0, 1]),
              "+": np.array([1, 1]) / math.sqrt(2), "-": np.array([1, -1]) / math.sqrt(2)}
    rows, worst_z = {}, 0.0
    for k, psi in states.items():
        P = sde_ensemble(psi, H, A, lam, T, seed=seed + ord(k))
        mean, se, vals = bloch_stats(P)
        rho_l = lindblad_evolve(np.outer(psi, psi.conj()).astype(complex), H, A, lam, T)
        lin = [float(np.real(np.trace(rho_l @ s))) for s in (X, Y, Z)]
        zsc = max(abs(a - b) / max(s, 1e-12) for a, b, s in zip(mean, lin, se))
        worst_z = max(worst_z, zsc)
        rows[k] = {"mc_mean": mean, "mc_se": se, "lindblad": lin, "max_z": zsc,
                   "mean_abs_x_per_trajectory": float(np.mean(np.abs(vals[0])))}
    # ensemble averages for Alice's two choices
    def ens(keys):
        m = [np.mean([rows[k]["mc_mean"][i] for k in keys]) for i in range(3)]
        s = [math.sqrt(sum(rows[k]["mc_se"][i] ** 2 for k in keys)) / len(keys) for i in range(3)]
        return m, s
    det = signal_detector(ens(["0", "1"]), ens(["+", "-"]))
    # exact: Lindblad of each ensemble's average
    rz = (lindblad_evolve(np.diag([1, 0]).astype(complex), H, A, lam, T) + lindblad_evolve(np.diag([0, 1]).astype(complex), H, A, lam, T)) / 2
    pp, mm = np.outer(states["+"], states["+"]).astype(complex), np.outer(states["-"], states["-"]).astype(complex)
    rx = (lindblad_evolve(pp, H, A, lam, T) + lindblad_evolve(mm, H, A, lam, T)) / 2
    return {"params": {"omega": om, "lambda": lam, "T": T, "A": "sigma_x", "H": "omega sigma_y"},
            "per_state": rows, "worst_mc_vs_lindblad_z": worst_z,
            "exact_ensemble_difference": float(np.abs(rz - rx).max()), "mc_detector": det}


def drift_plus_collapse(seed=5):
    eps, lam, T = 0.3, 0.2, 3.0
    out = {}
    for b in ("z", "x"):
        Ps = [sde_ensemble(np.array(s), np.zeros((2, 2)), Z, lam, T, eps=eps, n=600, N=5000, seed=seed + i) for i, s in enumerate(NL.ENS[b])]
        P = np.vstack(Ps)
        m, s, _ = bloch_stats(P)
        out[b] = (m, s)
    return {"params": {"eps": eps, "lambda": lam, "T": T, "A": "sigma_z"}, "z": out["z"], "x": out["x"],
            "detector": signal_detector(out["z"], out["x"]), "noise_free_tanh": math.tanh(2 * eps * T)}


# ======================================================================================= E. H-12
def z0_from_alpha():
    return 2 * ALPHA * H_PLANCK / E_CHARGE ** 2      # SI-2019: Z0 = mu0 c = 2 alpha h / e^2, so dlnZ0 = dln alpha


S_SPAN = (0.0466, 0.0935)   # Feynman-Hellmann S = sum sigma_q/m_p, board span READ via D67 audit 0705.3704


def v_drift_from_mu(mu_dot=-8e-18, mu_sig=36e-18):
    """mu = m_p/m_e, m_e ∝ v (fixed Yukawa -- named).  dln m_p/dln v = S (board H2) or 2/9 + 7S/9 (board H1)."""
    out = {}
    for hyp, kp in (("H2", lambda S: S), ("H1", lambda S: 2 / 9 + 7 * S / 9)):
        for S in S_SPAN:
            k = kp(S) - 1.0                           # dln mu / dln v
            out[f"{hyp}, S={S}"] = (mu_dot / k, mu_sig / abs(k))
    return out


H12 = [  # (symbol, what the taxonomy PDF says it is, class, carrier, can carry a state-dependent drift?, bound, source)
    ("M", "Madelung (n+l) subshell ordering (Lemma I)", "EMERGENT (many-electron atomic structure)", "none -- a readout of alpha, m_e",
     "NO independent carrier: inherits alpha and v", "inherits alpha, mu bounds below", "taxonomy PDF p.1 (Drive, READ)"),
    ("R", "relativistic inert-pair contraction (Lemma II)", "EMERGENT (function of Z alpha)", "none -- a readout of alpha",
     "NO independent carrier: inherits alpha", "inherits alpha bound", "taxonomy PDF p.1"),
    ("K", "Kondo temperature T_K (Lemma III)", "MATERIAL PROPERTY (per material, exponential in exchange x DOS)", "none",
     "NO: not a constant of nature; varies by material", "no 'variation of a constant' bound applies (category)", "taxonomy PDF p.1"),
    ("T", "TA-phonon Grueneisen parameter (Lemma IV)", "MATERIAL PROPERTY", "none",
     "NO: not a constant of nature", "no bound applies (category)", "taxonomy PDF p.1"),
    ("CP", "CKM phase delta_CP (Lemma V)", "LAGRANGIAN PARAMETER (phase of the Yukawa matrices)", "Higgs-fermion Yukawa sector",
     "CONDITIONAL: only if the Yukawa matrix is itself a field (named)", "OPEN (no READ variation bound)", "--"),
    ("alpha_s", "strong coupling (Lemma VI)", "LAGRANGIAN PARAMETER", "gluon field (KR eps_S)",
     "YES in KR form; KR fn.5: 'no non-trivial bounds can be placed' on eps_S", "proxy X_s = m_s/Lambda_QCD: |Xs_dot/Xs| < 1e-18 /yr (Oklo)",
     "0705.3704v2 p.1, p.4 (READ); 2106.10576v2 p.13 fn.5 (READ)"),
    ("Z0", "vacuum impedance sqrt(mu0/eps0) (Lemma IX)", "DERIVED: Z0 = 2 alpha h/e^2 (computed), i.e. alpha", "photon field A_mu (KR eps_gamma)",
     "YES -- the ONLY carrier with a measured STATE-DEPENDENT bound: |eps_gamma| < 1.15e-12 (90% CL)",
     "alpha_dot/alpha = 1.0(1.1)e-18 /yr; (c^2/alpha) dalpha/dPhi = 14(11)e-9",
     "2411.09611v1 p.1,7; 2010.06620v2 p.1, Table II (READ)"),
    ("Lambda", "vacuum energy density (Lemma X)", "CONSTANT in GR; a field only if dark energy is dynamical (named)", "metric / a dark-energy field",
     "CONDITIONAL", "OPEN (no READ variation bound)", "--"),
    ("G", "Newton's constant (Lemma XI)", "COUPLING of the metric field", "metric g_mu_nu (KR eps_G)",
     "YES in KR form; 'not aware of any current experimental data ... to constrain eps_G' (KR p.14)",
     "G_dot/G = (4 +- 9)e-13 /yr (LLR)", "1009.5514v1 p.71 eq.133 restating Williams-Turyshev-Boggs 2004 (READ-VIA-RESTATEMENT); 2106.10576v2 p.14"),
    ("G_F", "Fermi constant (Lemma VII)", "LAGRANGIAN-DERIVED (W exchange; tree level 1/(sqrt2 v^2), named, not READ)", "W/Z fields",
     "YES in principle (bosonic field); no KR-type bound located", "OPEN (no READ numeric bound); tied to v at tree level", "--"),
    ("G_theta", "QCD vacuum angle (Lemma XII)", "LAGRANGIAN PARAMETER; a field only if an axion exists (2001.11966 p.1 refs 10-11)", "axion (named)",
     "CONDITIONAL on an axion", "static: |d_n| < 1.8e-26 e cm (90% CL); theta-bar conversion OPEN; variation OPEN", "2001.11966v1 p.6 (READ)"),
    ("v", "Higgs vev (Lemma VIII)", "EXPECTATION VALUE OF A BOSONIC FIELD -- KR's construction applies literally (KR eq. 4, Yukawa)", "Higgs field",
     "YES in KR form; no state-dependent bound located", "via mu = m_p/m_e: mu_dot/mu = -8(36)e-18 /yr (see v_drift_from_mu)", "2010.06620v2 p.1, Table II (READ)"),
]


# ======================================================================================= report
def build():
    R = {}
    # A
    R["law"] = derive_law()
    R["nlcontrol_vs_law"] = {e: (NLCONTROL_PRINTED[e], bob_y_exact(e, 3.0)) for e in NLCONTROL_PRINTED}
    grid = []
    for e in (1e-3, 1e-2, 1e-1, 0.3):
        for T in (0.5, 3.0, 10.0):
            num = bob_numeric("x", e, T, Y) - bob_numeric("z", e, T, Y)
            grid.append((e, T, num, bob_y_exact(e, T)))
    R["grid"] = grid
    R["linear_control"] = bob_numeric("x", 0.1, 3.0, Y, lin=True) - bob_numeric("z", 0.1, 3.0, Y, lin=True)
    R["best_basis"] = best_basis(0.1, 3.0)
    # B
    R["info"] = {D: (mi(D), capacity(D), holevo(D)) for D in (1e-3, 1e-2, 0.1, 0.5, 0.9, 1.0)}
    R["CMAX"] = CMAX
    R["min_pairs_per_qubit"] = 2.0 / CMAX
    # C
    R["walsworth_check_eV"] = H_PLANCK * 8.9e-6 / E_CHARGE
    R["kr_ratio_quoted_nearly_50"] = 4.7e-11 / 1.15e-12
    cond = {}
    f = BOUNDS_WEINBERG["Majumder+ 1990, 201Hg, PRL 65 2931"]["f_Hz"]
    for lab, eps in eps_readings(f).items():
        rows = []
        for T in (1.0, 60.0, 3600.0, 86400.0):
            D = bob_y_exact(eps, T)
            rows.append((T, D, capacity(D)[0], (3.0 / D) ** 2))
        r, Topt = rate_optimum(eps)
        rem = {}
        for Lname, L in (("1 AU", AU_M), ("1 ly", LY_M), ("4.24 ly (illustrative)", 4.24 * LY_M)):
            for N in (1, 7, 1e3, 1e6):
                em = eps_to_remove(L, N)
                rem[(Lname, N)] = (em, None if em is None else em <= eps)
        cond[lab] = {"eps_max": eps, "rows": rows, "rate_opt": (r, Topt), "removal": rem,
                     "T_half": math.atanh(0.5) / (2 * eps)}
    R["conditional"] = cond
    # D
    R["collapse"] = collapse_control()
    R["drift_collapse"] = drift_plus_collapse()
    # E
    R["Z0"] = (z0_from_alpha(), Z0_SCIPY)
    R["v_drift"] = v_drift_from_mu()
    R["alpha_dot_improvement"] = 0.8e-16 / 1.1e-18   # Flambaum 2007 sigma / Lange 2021 sigma
    # F
    R["frame"] = {"pairs_one_frame": CO.n, "closed_one_frame": CO.bad,
                  "two_frames_closed": bool(CO.L.box_has_causal(CO.E1, CO.E2)),
                  "one_corridor_closed": bool(CO.L.rank1_has_causal(CO.E1))}
    return R


def report(R):
    p = print
    p("=" * 110)
    p("settle.py -- DOCKET 68 / A1-settle: H-SETTLE (deterministic drift), the collapse control, H-12 carriers")
    p("=" * 110)
    p("\nA. THE SIGNAL AT BOB under nlcontrol's drift H = eps <X> Z (imported)")
    L = R["law"]
    p(f"   exact law <sigma_y>_x - <sigma_y>_z = tanh(2 eps T): sympy ODE residual {L['ode_residual_symbolic']}, "
      f"identity residual {L['identity_residual_symbolic']}; numeric {L['ode_residual_numeric']:.1e}, {L['identity_residual_numeric']:.1e}")
    for e, (pr, ex) in R["nlcontrol_vs_law"].items():
        p(f"   nlcontrol printed (T=3) eps={e:<6}: {pr:.5f}   tanh(2 eps T) = {ex:.6f}")
    p("   grid (nlcontrol integrator vs exact):")
    for e, T, num, ex in R["grid"]:
        p(f"     eps={e:<6} T={T:<5} numeric {num:+.6f}   exact {ex:+.6f}   diff {num - ex:+.1e}")
    p(f"   LINEAR control (H = eps Z): signal {R['linear_control']:+.2e}")
    bb = R["best_basis"]
    p(f"   best Alice axis over the sphere (eps=0.1, T=3): |dr| = {bb[0]:.6f} at n = ({bb[1][0]:+.3f},{bb[1][1]:+.3f},{bb[1][2]:+.3f});"
      f" x-basis gives {math.tanh(0.6):.6f}")
    p("\nB. WHAT IT IS WORTH (Bob measures sigma_y; Alice picks x or z)")
    for D, (m, (c, q), chi) in R["info"].items():
        p(f"   D={D:<6} I(uniform) {m:.4e} bits  capacity {c:.4e} (q*={q:.3f})  Holevo(uniform) {chi:.4e}  D^2/(8 ln2) {D*D/(8*LN2):.4e}")
    p(f"   ceiling at D -> 1: {R['CMAX']:.6f} bits/pair = log2(1.25) = {math.log2(1.25):.6f};  pairs per teleported qubit >= {R['min_pairs_per_qubit']:.3f}")
    p("   (ceiling of THIS two-choice protocol; mean y >= 0 for every Alice axis, so no antipodal letter exists.  Any protocol on a")
    p("    qubit is capped at 1 bit per pair by Holevo's bound -- NAMED-NOT-READ here -- so >= 2 pairs per teleported qubit always.)")
    p("\nC. BOUNDS")
    p("   KR (causal) family -- dimensionless eps_gamma, READ:")
    for k, (v, src) in BOUNDS_KR.items():
        p(f"     {k:<52} {v:.3g}   [{src}]")
    p(f"     2411.09611 says 'nearly a factor of 50' over 4.7e-11; computed ratio {R['kr_ratio_quoted_nearly_50']:.2f}  (wording discrepancy, not a refutation)")
    p("     KR's Lamb-shift estimate: printed 1e-4 in KR v2 p.14, restated as 1e-2 by Brož p.2 -- DISCREPANCY between the two READ texts, recorded.")
    p("     => superluminal signal at Bob permitted by this family: 0 for every eps (KR sec. 2.3: evolution of separated systems factorises).")
    p("   Weinberg family -- NAMED-NOT-READ (abstract metadata):")
    for k, d in BOUNDS_WEINBERG.items():
        p(f"     {k:<40} f = {d['f_Hz']}   {d['status']}")
    p(f"     consistency: h x 8.9 uHz = {R['walsworth_check_eV']:.3e} eV (abstract: 3.7e-20 eV)")
    for lab, c in R["conditional"].items():
        p(f"   CONDITIONAL on H-MAP reading {lab}, H-TRANSFER, H-SPIN, H-COHERE, H-FRAME3b, eps AT the Majumder upper limit:")
        p(f"     eps_max = {c['eps_max']:.4e} /s;  drift time to D = 0.5: {c['T_half']:.4e} s = {c['T_half']/3600:.2f} h")
        for T, D, C, Nd in c["rows"]:
            p(f"     T = {T:>8.0f} s: D = {D:.4e}, capacity {C:.4e} bits/pair, pairs for a 3-sigma detection {Nd:.3e}")
        r, To = c["rate_opt"]
        p(f"     best rate per pair: {r:.4e} bits/s at T = {To:.4e} s ({To/3600:.2f} h)")
        for (Ln, N), (em, ok) in c["removal"].items():
            if em is None:
                p(f"     O-BITS at {Ln:<24} with N = {N:<8g}: IMPOSSIBLE at any eps (N x {CMAX:.4f} < 2 bits)")
            else:
                p(f"     O-BITS at {Ln:<24} with N = {N:<8g}: needs eps >= {em:.4e} /s  -> {'NOT EXCLUDED' if ok else 'EXCLUDED'} by the (unread) bound")
    p("\nD. COLLAPSE-TYPE (STOCHASTIC) DRIFT -- the control that must NOT signal")
    C = R["collapse"]
    for k, r in C["per_state"].items():
        p(f"   |{k}>: MC mean {np.round(r['mc_mean'],4)}  Lindblad {np.round(r['lindblad'],4)}  max z {r['max_z']:.2f}  "
          f"per-trajectory <|x|> {r['mean_abs_x_per_trajectory']:.3f}")
    p(f"   exact (Lindblad) difference between Alice's ensembles: {C['exact_ensemble_difference']:.2e}")
    d, s, zz = C["mc_detector"]
    p(f"   MC detector: |diff| {d:.4f} +- {s:.4f}  ({zz:.2f} sigma)  -> {'NO SIGNAL' if zz < 4 else 'SIGNAL'}")
    DC = R["drift_collapse"]
    d, s, zz = DC["detector"]
    p(f"   must-signal control, drift + collapse (eps=0.3, lambda=0.2, T=3): |diff| {d:.4f} +- {s:.4f} ({zz:.1f} sigma); "
      f"noise-free tanh {DC['noise_free_tanh']:.4f}")
    p("\nE. H-12 -- which of the twelve could carry a state-dependent drift")
    p(f"   Z0 = 2 alpha h / e^2 = {R['Z0'][0]:.9f} ohm (scipy CODATA: {R['Z0'][1]:.9f}) -> Z0's variation IS alpha's.")
    for row in H12:
        p(f"   {row[0]:<8} {row[2]}\n            carrier: {row[3]} | drift: {row[4]}\n            bound: {row[5]}  [{row[6]}]")
    p("   v from mu (fixed Yukawa, named):")
    for k, (c, s) in R["v_drift"].items():
        p(f"     {k:<14}: v_dot/v = {c:+.2e} +- {s:.2e} /yr")
    p(f"   alpha_dot sigma improved {R['alpha_dot_improvement']:.0f}x from Flambaum 2007 (0.8e-16) to Lange 2021 (1.1e-18)")
    p("   NAMED LIMIT: a time-variation bound bounds a drift common to all states; it does not bound STATE-dependence.")
    p("\nF. H-SETTLE x H-FRAME (corridors.py imported)")
    F = R["frame"]
    p(f"   one corridor closes a causal curve: {F['one_corridor_closed']}; two frames: {F['two_frames_closed']}; "
      f"{F['pairs_one_frame']} one-frame pairs, closed: {F['closed_one_frame']}")
    p("   Gisin's protocol needs a fixed slicing (2412.20854 assumption 3b): keyed to ONE frame it closes no loop in this model.")


# ======================================================================================= selftest
def selftest():
    R = build()
    checks = []
    ok = lambda name, cond, detail="": checks.append((name, bool(cond), detail))
    for e, (pr, ex) in R["nlcontrol_vs_law"].items():
        rerun = bob_numeric("x", e, 3.0, Y, n=3000) - bob_numeric("z", e, 3.0, Y, n=3000)
        ok(f"A1a nlcontrol's integrator (n=3000) reproduces its printed {pr}", round(rerun, 5) == pr, f"{rerun:.7f}")
        ok(f"A1b printed {pr} vs exact tanh(2*{e}*3) within the integrator's O(dt) error",
           abs(pr - ex) < 2e-5, f"exact {ex:.7f}, offset {pr - ex:+.1e}")
    L = R["law"]
    ok("A2 sympy: phi = 2 atan(tanh(eps t)) solves phi' = 2 eps cos phi", L["ode_residual_numeric"] < 1e-12)
    ok("A2 sympy: sin(phi) = tanh(2 eps t)", L["identity_residual_numeric"] < 1e-12)
    ok("A3 grid: integrator agrees with exact law", max(abs(n - x) for _, _, n, x in R["grid"]) < 2e-3)
    # encoding-drift guard: a wrong law must be caught by the same comparison
    wrong = max(abs(n - math.tanh(e * T)) for e, T, n, _ in R["grid"])
    ok("A4 CONTROL (must fail): wrong law tanh(eps T) disagrees with the integrator", wrong > 1e-2, f"{wrong:.3f}")
    ok("A5 CONTROL: linear H = eps Z gives zero signal", abs(R["linear_control"]) < 1e-12)
    rng = np.random.default_rng(3)
    worst = 0.0
    for _ in range(12):
        v = rng.normal(size=2) + 1j * rng.normal(size=2)
        v /= np.linalg.norm(v)
        e, T = rng.uniform(0.01, 0.4), rng.uniform(0.5, 4.0)
        num = bloch_of(NL.evolve(v, e, False, T=T, n=6000))
        ex = bloch_exact(bloch_of(v), e, T)
        worst = max(worst, max(abs(a - b) for a, b in zip(num, ex)))
    ok("A6 general closed form vs nlcontrol integrator, 12 random states", worst < 2e-3, f"{worst:.1e}")
    bb = R["best_basis"]
    ok("A7 best Alice axis is the x axis (|n_x| ~ 1) and equals tanh(2 eps T)",
       abs(abs(bb[1][0]) - 1) < 1e-3 and abs(bb[0] - math.tanh(0.6)) < 1e-9, f"{bb}")
    ok("A7 z and y axes give zero signal", max(abs(c) for c in ensemble_mean((0, 0, 1), .1, 3) + ensemble_mean((0, 1, 0), .1, 3)) < 1e-15)
    ys = [ensemble_mean((math.sin(t) * math.cos(f), math.sin(t) * math.sin(f), math.cos(t)), 0.1, 3.0)[1]
          for t in np.linspace(0, math.pi, 37) for f in np.linspace(0, 2 * math.pi, 73)]
    ok("A8 Bob's mean y >= 0 for every Alice axis (tanh u + tanh v = sinh(u+v)/(cosh u cosh v))", min(ys) >= -1e-15, f"min {min(ys):.1e}")
    m, (c, q), chi = R["info"][1e-3]
    ok("B1 small-D law I = D^2/(8 ln 2)", abs(m / (1e-6 / (8 * LN2)) - 1) < 1e-3)
    ok("B2 ceiling capacity(D=1) = log2(1.25) (Z-channel, crossover 1/2)", abs(R["CMAX"] - math.log2(1.25)) < 1e-9)
    ok("B3 Holevo(uniform) = measured MI (states commute)", all(abs(v[0] - v[2]) < 1e-12 for v in R["info"].values()))
    ok("B4 capacity >= uniform MI", all(v[1][0] >= v[0] - 1e-15 for v in R["info"].values()))
    ok("B5 N < 2/log2(1.25) = 6.21 pairs per qubit is impossible", eps_to_remove(LY_M, 6) is None and eps_to_remove(LY_M, 7) is not None)
    ok("C1 Walsworth abstract: h * 8.9 uHz = 3.68e-20 eV ~ printed 3.7e-20", abs(R["walsworth_check_eV"] / 3.7e-20 - 1) < 0.02)
    ok("C2 2411.09611 'nearly a factor of 50': computed 40.87 (wording discrepancy recorded)", abs(R["kr_ratio_quoted_nearly_50"] - 40.87) < 0.01)
    ok("C3 KR Lamb-shift figure: KR v2 (1e-4) and Brož's restatement (1e-2) DIFFER -- discrepancy kept",
       BOUNDS_KR["KR 2022 Lamb-shift estimate (as printed in KR v2)"][0] != BOUNDS_KR["KR Lamb-shift estimate (as restated by Brož)"][0])
    for lab, cnd in R["conditional"].items():
        ems = [v[0] for (Ln, N), v in cnd["removal"].items() if v[0] is not None and Ln == "1 AU"]
        ok(f"C4 removal eps decreases with more pairs ({lab})", all(a >= b for a, b in zip(ems, ems[1:])))
    C = R["collapse"]
    ok("D1 collapse: MC ensemble average matches the LINEAR Lindblad map for every initial state (< 5 sigma)",
       C["worst_mc_vs_lindblad_z"] < 5, f"{C['worst_mc_vs_lindblad_z']:.2f}")
    ok("D2 collapse: exact ensemble difference between Alice's choices = 0", C["exact_ensemble_difference"] < 1e-12)
    ok("D3 collapse: MC detector sees no signal (< 4 sigma)", C["mc_detector"][2] < 4, f"{C['mc_detector'][2]:.2f}")
    ok("D4 VACUITY GUARD: each trajectory moves nonlinearly (per-trajectory <|x|> > 0.5 for |0>, Lindblad |x| < 0.5)",
       C["per_state"]["0"]["mean_abs_x_per_trajectory"] > 0.5 and abs(C["per_state"]["0"]["lindblad"][0]) < 0.5)
    DC = R["drift_collapse"]
    ok("D5 CONTROL (must signal): drift + collapse noise, same detector, > 10 sigma", DC["detector"][2] > 10, f"{DC['detector'][2]:.1f}")
    ok("D6 CONTROL (must signal): pure deterministic drift, same detector",
       signal_detector(([0, 0, 0], [0, 0, 0]), ([0, math.tanh(0.6), 0], [0, 0, 0]))[2] == math.inf)
    ok("E1 Z0 = 2 alpha h / e^2 equals CODATA Z0", abs(R["Z0"][0] / R["Z0"][1] - 1) < 1e-9, f"{R['Z0']}")
    ok("E2 twelve rows in H-12, four without an independent carrier", len(H12) == 12 and sum(r[4].startswith("NO") for r in H12) == 4)
    F = R["frame"]
    ok("F1 corridors: one corridor no loop; two frames close; one frame never", (not F["one_corridor_closed"]) and F["two_frames_closed"]
       and F["closed_one_frame"] == 0 and F["pairs_one_frame"] > 0)
    w = max(len(n) for n, _, _ in checks)
    for n, good, det in checks:
        print(f"  [{'PASS' if good else 'FAIL'}] {n:<{w}} {det}")
    bad = [n for n, g, _ in checks if not g]
    print(f"\n{len(checks) - len(bad)}/{len(checks)} checks pass")
    return 0 if not bad else 1


def to_jsonable(o):
    if isinstance(o, dict):
        return {str(k): to_jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [to_jsonable(v) for v in o]
    if isinstance(o, (np.floating, np.integer)):
        return o.item()
    if isinstance(o, float) and math.isinf(o):
        return "inf"
    return o


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    R = build()
    report(R)
    if "--json" in sys.argv:
        path = sys.argv[sys.argv.index("--json") + 1]
        with open(path, "w") as fh:
            json.dump(to_jsonable(R), fh, indent=1)
