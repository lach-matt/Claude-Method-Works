#!/usr/bin/env python3
"""vacuum.py -- DOCKET 68 WAVE 2, work item W2B-vacuum.  N_VAC: can the vacuum's own entanglement supply the pairs that
W2 x F1 and teleportation consume, with no distribution (O-MAKE-DIST)?  Not seated.  Write-up: W2B-vacuum.md.

M's words (CHARTER.md, verbatim): "What if information is faster than light, not because us moves faster, but because
is already exists everywhere?"  combine.py carries the reading as the OPEN pathway N_VAC: "pre-existing entanglement
(of the vacuum) usable as the channel's pairs with no distribution".  Wave 1 said: O-MAKE-DIST "OPEN via N_VAC only";
"whether any setup supplies the pairs a qubit needs faster than distribution is NOT computed".  This file computes it.

READ AT SOURCE (route recorded with each; short phrases only):
  R1 Reznik, quant-ph/0212044v2 -- READ via alphaXiv (answer_pdf_queries, full text): p.10 eq.(19) (the entanglement
     condition for inertial probes switched on for T < L/c), p.11 eq.(20) the window "cos^2(t), |t| <= 1/2" (the text
     layer drops a pi: see READING NOTE), Fig.1 p.11 ("Eq.(12) is satisfied for 8 < Omega < 11", L = T = 1), Fig.2 p.12
     (T = 1, Omega = 9.5: "extends up to L/T < 1.1"), p.13 ("purify ... approach gradually to a perfect pure EPR-Bohm pair").
  R2 Reznik, Retzker & Silman, quant-ph/0310058v2 -- READ via alphaXiv, pp.1-4: for "arbitrarily far-apart regions"
     the negativity is bounded below by exp(-(L/cT)^3) (eq.8, superoscillating windows) and "N >= e^-(L/T)^2"
     (numerical, p.3); local filters eq.(9)-(10) bring the state "as close as we like to a pure, maximally entangled
     state" at the price of "reducing the detectors' entanglement (negativity)" (p.4); distillation "feasible for any
     inseparable 2 x 2 mixed state" (p.4, citing Horodecki 1997).
  R3 Pozas-Kerstjens & Martin-Martinez, arXiv:1506.03081v7 -- READ via alphaXiv, pp.3-8, 14-15: eq.(13) the detector
     state, eq.(22) chi(t) = exp(-(t - t_nu)^2/T^2), eq.(33) L_AA, eq.(34) L_AB, eq.(37) M_coinc (gamma = 0), eq.(68)
     N(2) = |M| - L_mumu; p.11 the fourth-order analysis "does not add significatively new results".
  R4 Tjoa & Martin-Martinez, arXiv:2109.11561v3 -- READ via alphaXiv, pp.1-8, 13: the commutator part of M is
     state-independent and carries communication; "harvesting" only when the detectors cannot communicate; eq.(38)
     N+ = max(0, |M+| - L_jj); strong support [-3.5T, 3.5T] (eq.28); compact (truncated Gaussian) switching gives
     "essentially the same result" (p.13).
  R5 Bennett, Brassard, Popescu, Schumacher, Smolin & Wootters (BBPSSW), quant-ph/9511027v2 -- READ via alphaXiv,
     pp.1-4: eq.(7) the recurrence F'(F); "local operations and two-way classical communication"; eq.(8) hashing/
     breeding yield 1 - S(W_F), "positive for F > 0.8107".
  R6 Bennett, DiVincenzo, Smolin & Wootters (BDSW), quant-ph/9604024v2 -- READ via alphaXiv, pp.1, 6-11, 22-42:
     "EPPs require classical communication" (abstract); eqs.(42)-(43) the recurrence on Bell-diagonal states; the
     twirl; recurrence-hashing "D2(W_5/8) > 0.00457" (p.42); "D1(W_F) = 0 for all F < 3/4" (Knill-Laflamme, p.42).
  R7 Vidal & Werner, quant-ph/0102117v1 -- READ via alphaXiv, pp.1-7: N = (||rho^TA||_1 - 1)/2; Prop.3 (N does not
     increase under LOCC, on average over outcomes); eq.(39) F_opt <= (1 + 2N)/m; Prop.7 E_D <= E_N = log2||rho^TA||_1.
  R8 Verstraete & Verschelde, quant-ph/0203073v3 -- READ via alphaXiv, pp.1-4: Thm 1 F <= (1 + N_VV)/2 with
     N_VV = max(0, -2 lambda_min) (= 2 N of R7), equality iff the negative eigenvector is maximally entangled.
  R9 Chen, Ji, Kribs, Lutkenhaus & Zeng, arXiv:1310.3530v2 -- READ via alphaXiv, pp.1-4: Thm 1 a two-qubit rho_AB is
     symmetric extendible iff tr(rho_B^2) >= tr(rho_AB^2) - 4 sqrt(det rho_AB); p.1 a symmetric-extendible state
     admits no distillation "by protocols only involving local operations and one-way classical communication (from
     A to B)"; p.4 the Werner boundary p = 2/3, "fidelity 3/4".
  R10 Horodecki x3, quant-ph/9607009 and quant-ph/9801069 -- READ (abstract) via Firecrawl inspect_paper: any
     inseparable 2 x 2 state can be distilled (filtering + BBPSSW); a distillable state must violate the
     partial-transposition criterion (NPT).
  R11 Marcovitch, Retzker, Plenio & Reznik, arXiv:0811.1288 -- READ (abstract) via Firecrawl inspect_paper: in the 1D
     Klein-Gordon vacuum "long range entanglement decays exponentially for separations larger than the size of the
     segments".  Corroboration for the field itself; not used in any number.

READING NOTE (R1 eq.20).  The text layer prints the window as cos^2(t) on |t| <= 1/2.  That window jumps at
|t| = 1/2, its transform falls as 1/omega, and the emission integral int omega |chi~(Omega+omega)|^2 d omega then
diverges logarithmically for a pointlike probe (computed: `sudden_window_divergence`).  Reznik says the windows "act as
cutoff functions" (p.12), which needs a continuous window.  cos^2(pi t) is continuous with a continuous derivative;
with it Fig.1 and Fig.2 are reproduced (section A).  The reading is DERIVED (by reproduction), as in cosmin.py's note.

NAMED HYPOTHESES (every limitation is one):
  H-UDW        the probes are pointlike two-level Unruh-DeWitt detectors linearly coupled to a massless scalar in 3+1
               flat space (R1-R4's model).  Atoms and the electromagnetic field are not computed here.
  H-PERTURB    the detector state is the second-order (lambda^2) state of R3 eq.(13); lambda is the dimensionless
               coupling, lambda << 1.  Every negativity below is per lambda^2.  R3 p.11 (READ): fourth order "does not
               add significatively new results" for the phenomenology; non-perturbative harvesting is not computed.
  H-O4-FLOOR   the O(lambda^4) element rho_ee,ee is set to max(|M|, |L_AB|)^2 / (1 - 2 L_AA), the least value that
               makes the state positive and the second partial-transpose eigenvalue non-negative (R3 p.11: E2 "not
               always negative"; generally it does not become negative).  The symmetric-extension and fidelity
               verdicts are checked to hold with that element at the floor and at 10x the floor.
  H-MINK-VAC   the field is in the Minkowski vacuum (no curvature, no thermal bath, no boundary).
  H-SPACELIKE  "harvesting" means the probes cannot communicate (R4): compact windows with L > cT (section A, C), or
               Gaussian windows whose strong supports [-3.5T, 3.5T] (R4 eq.28) are spacelike, beta = L/cT >= 7.  For
               beta < 7 the Gaussian numbers include communication; N+ (R4 eq.38) is reported beside N.
  H-LOCC       linear quantum mechanics: what the two ends can do is LOCC (R5-R9 are theorems of linear QM).  Under
               W2 (a state-dependent drift) local maps are not linear; whether a drift could distil locally is OPEN
               (N_NLDIST, below).
  H-IID        repeated harvests give independent identical copies (every distillation rate below needs it; whether
               successive harvests at the same probes are independent is not computed).
  H-NEARMAX    the consuming channel needs near-maximal pairs: teleportation well above the classical 2/3, or W2 with
               branch states as separated as a Bell pair's.  Without it the weak harvested pair is consumed as it is,
               and its value is computed (teleportation 2/3 + 2N/3; W2 signal <= rho_perp).
  H-PROBE-OPERATED  the probes at both ends are operated devices (switched on a schedule, measured, their results
               sent): matter merely present at the far end is not a probe.  The probes therefore cross at <= c, priced
               as D23 prices a pair source (settle.first_transit_times, imported).
  H-PROTOCOL   BBPSSW's recurrence with hashing is ONE protocol; its round count prices that protocol, not the
               minimum.  The floor that holds for every protocol is at least one exchange (>= L/c) after the window
               (R7 Prop.3 / R8 Thm 1: no message, no near-maximal pair), each way for the computed states (R9), and
               Vidal-Werner's copies >= 1/E_N.  The window itself is family-specific; with none assumed the floor is
               t_hold + L/c (W2-fix, window_free_floor).
  H-SIMUL      one round of a two-way protocol costs L/c: both parties broadcast at once.
  H-LAMBDA-ILLUSTRATIVE  where a total (not per lambda^2) is printed, lambda = 0.1 and 0.01 are illustrations, not
               values of any device.

OPEN PATHWAYS NAMED HERE (none assumed in any removal):
  N_NLDIST   a state-dependent (non-linear) local operation that raises the pair's entanglement without communication.
             Not computed: under H-C2 the drift needs a branch, i.e. a measurement that consumes the pair.
  N_W2WEAK   W2 drawing a usable signal from many weak pairs (beyond this file's per-pair bound).  Not computed.
  N_VACNP    harvesting outside H-UDW / H-PERTURB (other detectors, other fields, non-perturbative couplings) that
             breaks the Gaussian-in-distance decay.  No READ source found this pass.

W2-FIX (2026-10-04; the two re-verifications W2V-0 / W2V-1, wave2/WAVE2-RESULT.json key result.verify):
  * The window bound T > 0.9097 L/c and the floors 2.41-3.00 L/c are SCOPED to the window families computed: Reznik's
    cos^2(pi t) with Omega T in [2, 40], and the Gaussian at beta = 7.  R2 harvests with cT << L at every L, so with
    no window assumption the floor is t_hold + L/c (window_free_floor, computed from D23): >= 1.50 L/c from a
    midpoint, >= 2.00 L/c from one end, at a negativity R2 guarantees only down to exp(-(L/cT)^3) (checks I3-I5).
    Every floor is still after the light time and after a midpoint pair source (0.50 L/c); no grade moves.  Wave 2
    first said 'the floor for ANY protocol is 2.41-3.00 L/c' and 'the window itself lasts >= 0.91 L/c (compact)'.
  * R6 p.29 (READ) NAMES the rotation: Macchiavello's 'deterministic bilateral B_x rotation' for the twirl T'.  Checked
    against R6 Table 1 p.24 (READ, BDSW_TABLE1): literally B_x is 00 <-> 01 in eq.(40) labels; conjugated by item 5's
    sigma_y (the step that makes T' fix Phi+) it is exactly 10 <-> 11, swap_post's map; both reproduce 0.00457
    (checks G6-G8; control: B_y gives 0.0029).  Wave 2 first said the map 'was IDENTIFIED by search ... not READ'.

Run:  python3 vacuum.py            (report)
      python3 vacuum.py --json PATH (report also written as JSON)
      python3 vacuum.py --selftest  (counted checks; STRUCTURAL items printed, not counted)
"""
import contextlib
import io
import json
import math
import os
import sys

import numpy as np
from scipy import integrate, optimize, special

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, ".."))

TWO_PI = 2.0 * math.pi
FOUR_PI2 = 4.0 * math.pi ** 2

_OWNERS = {}


def _owner(name):
    """Import an owner module once, quietly (the docket's scripts print at import).  Never copied."""
    if name not in _OWNERS:
        with contextlib.redirect_stdout(io.StringIO()):
            _OWNERS[name] = __import__(name)
    return _OWNERS[name]


# ============================================================================ A. Reznik's inertial probes (R1, p.10-12)
# Window (R1 eq.20, read as cos^2(pi t), T = 1): chi(t) = cos^2(pi t) on |t| <= 1/2.  chi~(w) = int chi e^{iwt} dt.
def chi_tilde(w):
    w = np.asarray(w, dtype=float)
    return 0.5 * np.sinc(w / TWO_PI) + 0.25 * (np.sinc((w + TWO_PI) / TWO_PI) + np.sinc((w - TWO_PI) / TWO_PI))


def chi_tilde_sudden(w):
    """The literal text-layer window cos^2(t) on |t| <= 1/2 (no pi): a sudden switch.  chi~ = int cos^2 t e^{iwt}."""
    w = np.asarray(w, dtype=float)
    s = lambda a: np.sinc(a / TWO_PI) * 0.5           # sin(a/2)/a
    return s(w) + 0.5 * (s(w + 2.0) + s(w - 2.0))


def emission(Om, kmax=4000.0, n=400001, ct=chi_tilde):
    """R1 eq.(19) right-hand side: int_0^inf w |chi~(Omega + w)|^2 dw  (= 4 pi^2 L_AA / lambda^2)."""
    k = np.linspace(0.0, kmax, n)
    return float(integrate.simpson(k * ct(Om + k) ** 2, x=k))


def exchange_momentum(Om, L, kmax=4000.0, n=800001):
    """R1 eq.(19) left-hand side: int_0^inf sin(wL)/L chi~(w - Omega) chi~(w + Omega) dw  (= 4 pi^2 |M| / lambda^2)."""
    k = np.linspace(0.0, kmax, n)
    return float(integrate.simpson(np.sin(k * L) / L * chi_tilde(k - Om) * chi_tilde(k + Om), x=k))


def exchange_time(Om, L, n=400):
    """The same amplitude by a second route: int int chi(t) chi(t') e^{i Omega (t + t')} / (L^2 - (t - t')^2) dt dt'.
    Valid for L > 1 (the supports are spacelike, the commutator vanishes, no i-epsilon is needed)."""
    x, w = np.polynomial.legendre.leggauss(n)
    t, w = 0.5 * x, 0.5 * w
    T1, T2 = np.meshgrid(t, t, indexing="ij")
    ch = np.cos(np.pi * T1) ** 2 * np.cos(np.pi * T2) ** 2
    val = np.sum(np.outer(w, w) * ch * np.exp(1j * Om * (T1 + T2)) / (L ** 2 - (T1 - T2) ** 2))
    return complex(val)


def reznik_ratio(Om, L):
    """|<0|X_AB>| / |E_A|^2 -- the quantity R1 plots in Fig.1 and Fig.2 (entangled iff > 1)."""
    return abs(exchange_momentum(Om, L)) / emission(Om)


def reznik_reproduction():
    f1 = lambda Om: reznik_ratio(Om, 1.0) - 1.0
    lo, hi = optimize.brentq(f1, 7.0, 9.0, xtol=1e-6), optimize.brentq(f1, 9.5, 12.0, xtol=1e-6)
    f2 = lambda L: reznik_ratio(9.5, L) - 1.0
    Lx = optimize.brentq(f2, 1.0, 1.3, xtol=1e-7)
    peak = optimize.minimize_scalar(lambda Om: -reznik_ratio(Om, 1.0), bounds=(7.0, 12.0), method="bounded",
                                    options={"xatol": 1e-4})
    return {"fig1_omega_window_computed": (lo, hi), "fig1_READ": "8 < Omega < 11 (R1 p.11)",
            "fig1_peak": (float(peak.x), float(-peak.fun)),
            "fig2_L_crossing_computed": Lx, "fig2_READ": "L/T < 1.1 (R1 p.12)",
            "window_T_over_light_time": (1.0 / Lx, 1.0),
            "combine_N_VAC_window_DERIVED_FROM_READ": (1.0 / 1.1, 1.0),
            "fig2_samples": {L: reznik_ratio(9.5, L) for L in (1.0, 1.05, 1.1, 1.2, 1.3)}}


def sudden_window_divergence():
    """READING NOTE control: the literal cos^2(t) window's emission integral grows with the cutoff (log divergence);
    the cos^2(pi t) window's does not."""
    a = [emission(9.5, kmax=K, n=int(200 * K) + 1, ct=chi_tilde_sudden) for K in (500.0, 2000.0, 8000.0)]
    b = [emission(9.5, kmax=K, n=int(200 * K) + 1, ct=chi_tilde) for K in (500.0, 2000.0, 8000.0)]
    return {"sudden_cos2t": a, "smooth_cos2pit": b, "sudden_growth": a[2] / a[0], "smooth_growth": b[2] / b[0]}


# =============================================== B. Gaussian switching, pointlike (R3 eqs.33, 34, 37; R4's split)
# alpha = Omega T, beta = L/(cT), gamma = 0.  All per lambda^2.
def L_AA(a):
    return (math.exp(-a * a / 2.0) - math.sqrt(math.pi / 2.0) * a * special.erfc(a / math.sqrt(2.0))) / (4.0 * math.pi)


def M_plus(a, b):
    """Anticommutator (state-dependent, harvesting) part of R3 eq.(37): the erfi term."""
    return math.exp(-a * a / 2.0) / (4.0 * math.sqrt(TWO_PI) * b) * math.exp(-b * b / 2.0) * special.erfi(b / math.sqrt(2.0))


def M_minus(a, b):
    """Commutator (state-independent, communication) part of R3 eq.(37): the -i term."""
    return math.exp(-a * a / 2.0) / (4.0 * math.sqrt(TWO_PI) * b) * math.exp(-b * b / 2.0)


def M_abs(a, b):
    return math.hypot(M_plus(a, b), M_minus(a, b))


def L_AB(a, b):
    """R3 eq.(34) at gamma = 0, through the Faddeeva function w(z) = e^{-z^2} erfc(-iz)."""
    z1, z2 = (b - 1j * a) / math.sqrt(2.0), (b + 1j * a) / math.sqrt(2.0)
    val = 1j * math.exp(-a * a / 2.0) / (8.0 * math.sqrt(TWO_PI) * b) * (special.wofz(-z1) - special.wofz(z2))
    return complex(val)


def L_AA_numeric(a):
    """Independent route: L_AA = (1/4 pi^2) int_0^inf k |chi~(Omega + k)|^2 dk with chi~ = sqrt(pi) T e^{-w^2 T^2/4}."""
    return integrate.quad(lambda k: k * math.pi * math.exp(-(a + k) ** 2 / 2.0), 0, np.inf)[0] / FOUR_PI2


def M_numeric(a, b):
    """Independent route (derived here): with u = t + t', s = t - t', the time-ordered amplitude is
    M = -sqrt(2 pi) e^{-a^2/2}/(4 pi^2) int_0^inf e^{-s^2/2} / ((b + s)(b - s + i0)) ds; principal value by
    scipy's Cauchy weight, the delta term separately."""
    pre = math.sqrt(TWO_PI) * math.exp(-a * a / 2.0) / FOUR_PI2
    S = b + 40.0
    pv = integrate.quad(lambda s: -math.exp(-s * s / 2.0) / (b + s), 0, S, weight="cauchy", wvar=b, limit=400)[0]
    pv += integrate.quad(lambda s: math.exp(-s * s / 2.0) / ((b + s) * (b - s)), S, np.inf)[0]
    delta = math.pi * math.exp(-b * b / 2.0) / (2.0 * b)
    return pre * pv, pre * delta


def L_AB_numeric(a, b):
    """Independent route: L_AB = (1/(4 pi beta)) int_0^inf sin(k beta) e^{-(k + a)^2/2} dk (R3 eq.A13, delta = 0)."""
    f = lambda k: math.sin(k * b) * math.exp(-(k + a) ** 2 / 2.0)
    return integrate.quad(f, 0, a + 40.0, limit=2000, epsabs=0.0, epsrel=1e-13)[0] / (4.0 * math.pi * b)


def negativity_gauss(a, b, plus_only=False):
    m = M_plus(a, b) if plus_only else M_abs(a, b)
    return max(0.0, m - L_AA(a))


def nmax_gauss(b, plus_only=True):
    fn = lambda a: -((M_plus(a, b) if plus_only else M_abs(a, b)) - L_AA(a))
    r = optimize.minimize_scalar(fn, bounds=(0.01, max(40.0, 3 * b)), method="bounded", options={"xatol": 1e-10})
    return float(r.x), max(0.0, float(-r.fun))


def nmax_asymptote(b):
    """DERIVED here (large beta): |M+| ~ e^{-a^2/2}(1 + 1/b^2 + 3/b^4)/(4 pi b^2), L_AA ~ e^{-a^2/2}(1/a^2 - 3/a^4)/(4 pi);
    with a^2 = b^2 + d the bracket is (4 + d) e^{-d/2}/b^4, maximal at d = -2:  N+_max ~ (e / 2 pi) e^{-b^2/2} b^-4."""
    return math.e / TWO_PI * math.exp(-b * b / 2.0) / b ** 4


def nmax_asymptote_wrong(b):
    """The first hand derivation (kept as the control the selftest must reject): dropped the 1/b^4 and 3/a^4 terms."""
    return math.exp(-b * b / 2.0) / (2.0 * math.pi * math.e * b ** 4)


def gauss_scaling(betas=(0.5, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14)):
    rows = []
    for b in betas:
        a_p, n_p = nmax_gauss(b, True)
        a_t, n_t = nmax_gauss(b, False)
        rows.append({"beta=L/cT": b, "alpha_opt (N+)": a_p, "sqrt(beta^2-2)": math.sqrt(max(b * b - 2, 0.0)),
                     "N+_max/lambda^2": n_p, "N_max/lambda^2 (incl. commutator)": n_t,
                     "asymptote (e/2pi)e^{-b^2/2}b^-4": nmax_asymptote(b),
                     "ratio N+/asymptote": n_p / nmax_asymptote(b) if n_p > 0 else 0.0,
                     "strong supports spacelike (beta >= 7, R4)": b >= 7})
    return rows


# ===================================================== C. compact window, strictly spacelike (L > cT), every gap
_EMISSION_CACHE = {}


def _emission_cached(Om):
    key = round(Om, 9)
    if key not in _EMISSION_CACHE:
        _EMISSION_CACHE[key] = emission(Om, kmax=3000.0, n=300001)
    return _EMISSION_CACHE[key]


def compact_nmax(L, oms=None):
    """max over Omega of (|X| - E^2)/(4 pi^2): the per-lambda^2 negativity of Reznik's probes at separation L >= T."""
    oms = np.linspace(2.0, 40.0, 153) if oms is None else oms
    best = (None, -np.inf)
    for Om in oms:
        X = abs(exchange_time(Om, L, n=220)) if L > 1.0 + 1e-9 else abs(exchange_momentum(Om, L))
        v = (X - _emission_cached(Om)) / FOUR_PI2
        if v > best[1]:
            best = (float(Om), float(v))
    return best


def compact_boundary():
    """The separation beyond which no gap in [2, 40] harvests with Reznik's window: bisection on max_Omega(|X| - E^2),
    the Omega grid refined (step 0.05) where the optimum sits."""
    oms = np.concatenate([np.linspace(2.0, 7.0, 21), np.linspace(7.0, 13.0, 121), np.linspace(13.0, 40.0, 55)])
    g = lambda L: compact_nmax(L, oms)[1]
    Lb = optimize.brentq(g, 1.0, 1.1, xtol=1e-5)
    return {"L/T boundary (Omega T in [2, 40])": Lb, "T/(L/c) at the boundary": 1.0 / Lb,
            "best Omega T just inside": compact_nmax(Lb - 1e-3, oms)[0]}


def compact_scan(Ls=(1.0, 1.05, 1.1, 1.15, 1.2, 1.3, 1.45, 1.6)):
    rows = [{"L/T": L, "best Omega T": om, "N_max/lambda^2": max(0.0, v), "raw |X|-E^2 (/4pi^2)": v}
            for L, (om, v) in ((L, compact_nmax(L)) for L in Ls)]
    last = max((r["L/T"] for r in rows if r["N_max/lambda^2"] > 0), default=None)
    return {"rows": rows, "largest L/T in grid with harvest (Omega T in [2, 40])": last}


# ===================================================== D. the harvested state, its fidelity, teleportation
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def harvested_state(P, M, Lab, eps_scale=1.0):
    """R3 eq.(13), written in the kron ordering used by every routine here (A first): |gg>, |ge>, |eg>, |ee> with
    |ge> = A in g, B in e.  R3 orders |eA gB> before |gA eB>, so its L_AB sits here as rho[2,1] (= conj at [1,2]).
    rho_ee,ee at H-O4-FLOOR x eps_scale; trace kept 1."""
    eps = eps_scale * max(abs(M), abs(Lab)) ** 2 / (1.0 - 2.0 * P)
    r = np.zeros((4, 4), dtype=complex)
    r[0, 0] = 1.0 - 2.0 * P - eps
    r[1, 1] = r[2, 2] = P
    r[3, 3] = eps
    r[0, 3], r[3, 0] = np.conj(M), M
    r[2, 1], r[1, 2] = Lab, np.conj(Lab)
    return r


def _xblocks(r):
    """For an X-state: diagonal d0..d3, |rho_03| = m, |rho_12| = l."""
    d = [float(np.real(r[i, i])) for i in range(4)]
    return d, float(abs(r[0, 3])), float(abs(r[1, 2]))


def _lam_min(a, b, z):
    """Smallest eigenvalue of [[a, z], [z*, b]] without cancellation: (ab - |z|^2)/lambda_max."""
    lmax = (a + b) / 2.0 + math.sqrt(((a - b) / 2.0) ** 2 + z * z)
    return (a * b - z * z) / lmax


def negativity_x(r):
    """Exact for an X-state (the partial transpose swaps the two coherences between the blocks): precision-safe when
    N is far below double-precision resolution of an eigensolver on the full matrix (N ~ 1e-17 here)."""
    d, m, l = _xblocks(r)
    return max(0.0, -_lam_min(d[1], d[2], m)) + max(0.0, -_lam_min(d[0], d[3], l))


def fef_x(r):
    """Fully entangled fraction of an X-state: local phases set the phases of rho_03 and rho_12 independently, so
    f = max((d0 + d3)/2 + m, (d1 + d2)/2 + l); R8 Thm 1 caps it at 1/2 + N (checked against the SVD formula
    where double precision resolves it)."""
    d, m, l = _xblocks(r)
    return max((d[0] + d[3]) / 2.0 + m, (d[1] + d[2]) / 2.0 + l)


def fef_minus_half_x(r):
    """f - 1/2 without forming 1 - 2P: (d0 + d3)/2 - 1/2 = -(d1 + d2)/2 by the trace."""
    d, m, l = _xblocks(r)
    return max(m - (d[1] + d[2]) / 2.0, (d[1] + d[2]) / 2.0 + l - 0.5)


def sym_ext_margin_x(r, extend="B"):
    """R9 Thm 1 margin for an X-state, written without the O(1) cancellation of tr(rho_B^2) - tr(rho_AB^2):
    on B: 2(d0 d2 + d1 d3 - m^2 - l^2) + 4 sqrt(det);  on A: 2(d0 d1 + d2 d3 - m^2 - l^2) + 4 sqrt(det),
    det = (d0 d3 - m^2)(d1 d2 - l^2)."""
    d, m, l = _xblocks(r)
    det = max(0.0, (d[0] * d[3] - m * m) * (d[1] * d[2] - l * l))
    cross = d[0] * d[2] + d[1] * d[3] if extend == "B" else d[0] * d[1] + d[2] * d[3]
    return 2.0 * (cross - m * m - l * l) + 4.0 * math.sqrt(det)


def ptranspose_B(r):
    return r.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)


def negativity(r):
    ev = np.linalg.eigvalsh(ptranspose_B(r))
    return float(-sum(e for e in ev if e < 0))


def log_negativity(r):
    return math.log2(1.0 + 2.0 * negativity(r))


def fully_entangled_fraction(r):
    """Horodecki's formula as R8 p.1 restates it: f = (1 + l1 + l2 - sgn(det R) l3)/4, R_ij = tr(rho s_i x s_j)."""
    S = (SX, SY, SZ)
    R = np.array([[np.real(np.trace(r @ np.kron(a, b))) for b in S] for a in S])
    sv = np.linalg.svd(R, compute_uv=False)
    return float((1.0 + sv[0] + sv[1] - np.sign(np.linalg.det(R)) * sv[2]) / 4.0)


def _bell_phi_plus():
    v = np.zeros(4, dtype=complex)
    v[0] = v[3] = 1 / math.sqrt(2)
    return v


def teleport_fidelity(resource):
    """Standard protocol (Bell measurement on input + Alice's half, two classical bits, Pauli correction), averaged over
    the six axis states (a 3-design, exact for this quadratic average).  resource is on (A, B), Phi+ convention."""
    phi = _bell_phi_plus()
    bells = [phi, np.array([0, 1, 1, 0]) / math.sqrt(2), np.array([1, 0, 0, -1]) / math.sqrt(2),
             np.array([0, 1, -1, 0]) / math.sqrt(2)]
    corr = [I2, SX, SZ, SZ @ SX]
    states = [np.array(v, dtype=complex) / np.linalg.norm(v) for v in
              ([1, 0], [0, 1], [1, 1], [1, -1], [1, 1j], [1, -1j])]
    tot = 0.0
    for psi in states:
        rin = np.kron(np.outer(psi, psi.conj()), resource)           # qubits: input, A, B
        out = np.zeros((2, 2), dtype=complex)
        for b, c in zip(bells, corr):
            proj = np.kron(np.outer(b, b.conj()), I2)
            post = proj @ rin @ proj
            rb = np.einsum("ijik->jk", post.reshape(4, 2, 4, 2))     # trace out input + A
            out += c @ rb @ c.conj().T
        tot += float(np.real(psi.conj() @ out @ psi))
    return tot / len(states)


def phase_align(r):
    """Bob's local phase diag(1, e^{i phi}) chosen so <Phi+|rho|Phi+> is maximal (rho_ee,gg real positive)."""
    ph = np.angle(r[3, 0])
    U = np.kron(I2, np.diag([1.0, np.exp(-1j * ph)]))
    return U @ r @ U.conj().T


# ===================================================== E. no communication: local operations alone
def random_local_channel(rng, k=2):
    """Random qubit channel from a Haar-ish random isometry C^2 -> C^2 x C^k (Stinespring)."""
    A = rng.normal(size=(2 * k, 2)) + 1j * rng.normal(size=(2 * k, 2))
    V, _ = np.linalg.qr(A)
    return [V[i::k, :] for i in range(k)]                            # Kraus operators K_i (2 x 2)


def apply_local(r, KA, KB):
    out = np.zeros((4, 4), dtype=complex)
    for a in KA:
        for b in KB:
            K = np.kron(a, b)
            out += K @ r @ K.conj().T
    return out


def amplitude_damping(g):
    return [np.array([[1, 0], [0, math.sqrt(1 - g)]], dtype=complex),
            np.array([[0, math.sqrt(g)], [0, 0]], dtype=complex)]


def lo_test(r, trials=3000, seed=68):
    """Local operations with no communication: the negativity never rises (R7 Prop.3), and the fidelity never passes
    1/2 + N (R7 eq.39, R8 Thm 1).  Random channels plus the amplitude-damping family on one side and on both."""
    rng = np.random.default_rng(seed)
    N0, f0 = negativity(r), fully_entangled_fraction(r)
    dN, df = -np.inf, -np.inf
    for _ in range(trials):
        out = apply_local(r, random_local_channel(rng), random_local_channel(rng))
        dN = max(dN, negativity(out) - N0)
        df = max(df, fully_entangled_fraction(out) - (0.5 + N0))
    for g in np.linspace(0.0, 1.0, 41):
        for out in (apply_local(r, amplitude_damping(g), [I2]), apply_local(r, amplitude_damping(g), amplitude_damping(g))):
            dN = max(dN, negativity(out) - N0)
            df = max(df, fully_entangled_fraction(out) - (0.5 + N0))
    return {"N0": N0, "f0": f0, "max rise of N under LO": dN, "max of f - (1/2 + N0) under LO": df}


def global_controls(r):
    """Controls that MUST break the LO bounds: a global unitary (not LO) and a CNOT on a product state."""
    # global unitary taking |gg> to Phi+ and |ee> to Phi-: f jumps to ~1
    phi_p, phi_m = _bell_phi_plus(), np.array([1, 0, 0, -1], dtype=complex) / math.sqrt(2)
    U = np.zeros((4, 4), dtype=complex)
    U[:, 0], U[:, 3] = phi_p, phi_m
    U[:, 1], U[:, 2] = np.array([0, 1, 0, 0]), np.array([0, 0, 1, 0])
    f_glob = fully_entangled_fraction(U @ r @ U.conj().T)
    plus0 = np.kron(np.array([1, 1]) / math.sqrt(2), np.array([1, 0])).astype(complex)
    cnot = np.eye(4, dtype=complex)[[0, 1, 3, 2]]
    prod = np.outer(plus0, plus0.conj())
    return {"f after a global unitary": f_glob, "bound 1/2 + N": 0.5 + negativity(r),
            "N(product)": negativity(prod), "N(CNOT product)": negativity(cnot @ prod @ cnot.conj().T)}


def filtering(r, eta2):
    """R2 eq.(9)-(10): each probe passes the local filter diag(eta, 1) in (g, e) -- R2's f = diag(1, eta) in (up, down)
    attenuates the ground level.  Four joint outcomes; the heralded one (both pass) is what R2 brings near a pure
    maximally entangled state.  Each party sees only its own outcome."""
    eta = math.sqrt(eta2)
    fpass = np.diag([eta, 1.0]).astype(complex)
    ffail = np.diag([math.sqrt(1 - eta2), 0.0]).astype(complex)
    outs = []
    for KA, la in ((fpass, "A pass"), (ffail, "A fail")):
        for KB, lb in ((fpass, "B pass"), (ffail, "B fail")):
            K = np.kron(KA, KB)
            o = K @ r @ K.conj().T
            p = float(np.real(np.trace(o)))
            if p > 0:
                rr = o / p
                outs.append({"outcome": (la, lb), "p": p, "N": negativity(rr), "f": fully_entangled_fraction(rr)})
    avgN = sum(o["p"] * o["N"] for o in outs)
    her = [o for o in outs if o["outcome"] == ("A pass", "B pass")][0]
    return {"eta^2": eta2, "outcomes": outs, "sum p_i N_i": avgN, "N before": negativity(r),
            "heralded p": her["p"], "heralded f": her["f"], "heralded N": her["N"], "unfiltered f": fully_entangled_fraction(r)}


# ===================================================== F. one-way distillation is impossible (R9)
def sym_ext_margin(r, extend="B"):
    """R9 Thm 1: rho_AB has a symmetric extension on B iff tr(rho_B^2) - tr(rho_AB^2) + 4 sqrt(det rho_AB) >= 0.
    extend='A' tests the extension on A (the B -> A direction) by swapping the parties."""
    if extend == "A":
        S = np.eye(4)[[0, 2, 1, 3]]
        r = S @ r @ S.T
    rB = np.einsum("ijik->jk", r.reshape(2, 2, 2, 2))
    det = max(float(np.real(np.linalg.det(r))), 0.0)
    return float(np.real(np.trace(rB @ rB)) - np.real(np.trace(r @ r)) + 4.0 * math.sqrt(det))


def werner(F):
    """Werner state of singlet fidelity F (R5 eq.4), written with Phi+ as the singlet's local-unitary image."""
    phi = _bell_phi_plus()
    P = np.outer(phi, phi.conj())
    return F * P + (1 - F) / 3.0 * (np.eye(4) - P)


# ===================================================== G. distillation with two-way messages: price of one protocol
def H2bits(p):
    return -sum(float(x) * math.log2(float(x)) for x in p if x > 0)


def bbpssw_map(F):
    """R5 eq.(7)."""
    return (F * F + (1 - F) ** 2 / 9) / (F * F + 2 * F * (1 - F) / 3 + 5 * (1 - F) ** 2 / 9)


def bdsw_step(p):
    """R6 eqs.(42)-(43): p = (p00, p01, p10, p11), Phi+ = 00; returns passed-subset probabilities and p_pass."""
    p00, p01, p10, p11 = p
    pp = p00 ** 2 + p01 ** 2 + p10 ** 2 + p11 ** 2 + 2 * p00 * p10 + 2 * p01 * p11
    return ((p00 ** 2 + p10 ** 2) / pp, (p01 ** 2 + p11 ** 2) / pp, 2 * p00 * p10 / pp, 2 * p01 * p11 / pp), pp


def hashing_yield(p):
    return 1.0 - H2bits(p)


def twirl_post(q):
    return (q[0],) + ((1 - q[0]) / 3,) * 3


def swap_post(q):
    """A fixed bilateral rotation applied after each step: R6 p.29 (READ) names it -- C. Macchiavello's 'deterministic
    bilateral B_x rotation' substituted for the twirl T' (ref. [34]).  The component map used here is 10 <-> 11 (Phi- <->
    Psi-) in R6's eq.(40) labels.  W2-fix: checked against R6 Table 1 p.24 (READ) in bdsw_bx_from_table1(): Table 1's
    B_x row, written with Psi- as the standard state, is Phi+ <-> Psi+ (00 <-> 01); conjugated by the unilateral sigma_y
    of R6 item 5 (the step that makes T' fix Phi+) it is exactly 10 <-> 11, and so is sigma_x B_x (R6 p.58 item 4: 'flip
    the low bit iff the high bit is one').  Both forms give the same W_5/8 yield, 0.0045700549, because they differ by
    the relabelling (00 <-> 01)(10 <-> 11), a symmetry of eqs.(42)-(43) and of the hashing entropy.  Wave 2 first said:
    'the component map used here, 10 <-> 11, was IDENTIFIED by search over the six maps that fix 00 ... not READ'."""
    return (q[0], q[1], q[3], q[2])


#: R6 (BDSW) Table 1 p.24, READ via alphaXiv (answer_pdf_queries on quant-ph/9604024v2): each row maps the source
#: Bell states (Psi-, Phi-, Phi+, Psi+) to the states listed.  Phases are dropped, as Table 1 drops them (Table 4 p.73
#: restores them; a density matrix diagonal in the Bell basis does not see them).
BDSW_TABLE1_SOURCE = ("Psi-", "Phi-", "Phi+", "Psi+")
BDSW_TABLE1 = {
    "sigma_x": ("Phi-", "Psi-", "Psi+", "Phi+"),
    "sigma_y": ("Phi+", "Psi+", "Psi-", "Phi-"),
    "sigma_z": ("Psi+", "Phi+", "Phi-", "Psi-"),
    "B_x": ("Psi-", "Phi-", "Psi+", "Phi+"),
    "B_y": ("Psi-", "Psi+", "Phi+", "Phi-"),
    "B_z": ("Psi-", "Phi+", "Phi-", "Psi+"),
}
#: The route of W2-fix's re-read of R6 (Table 1 p.24, p.29 B_x), recorded as data so the LEDGER's route census
#: (ledger.d68_w2_routes, M-D68-16) can ask it; the pages lie inside R6's recorded pp.22-42 (the W2 reproduction).
BDSW_TABLE1_ROUTE = ("READ via alphaXiv (answer_pdf_queries on quant-ph/9604024v2), Table 1 p.24 and p.29 (B_x named), "
                     "W2-fix re-read 2026-10-04")
#: R6 eq.(40) p.26 (READ): Phi+ = 00, Psi+ = 01, Phi- = 10, Psi- = 11 -- the index order of every p tuple here.
BDSW_EQ40 = {"Phi+": 0, "Psi+": 1, "Phi-": 2, "Psi-": 3}


def _bdsw_perm(op):
    """Table 1's row as a permutation of eq.(40) indices: image[i] = index the state with index i is sent to."""
    img = [None] * 4
    for src, dst in zip(BDSW_TABLE1_SOURCE, BDSW_TABLE1[op]):
        img[BDSW_EQ40[src]] = BDSW_EQ40[dst]
    return tuple(img)


def _compose(*ops):
    """Apply ops left to right (first op first) as permutations of eq.(40) indices."""
    img = list(range(4))
    for op in ops:
        P = _bdsw_perm(op)
        img = [P[i] for i in img]
    return tuple(img)


def _post_from_perm(img):
    """The probability map a state-permutation induces: the weight of state i moves to img[i]."""
    def post(q):
        out = [0.0] * 4
        for i, j in enumerate(img):
            out[j] = q[i]
        return tuple(out)
    return post


def bdsw_bx_from_table1():
    """W2-fix: which component map is R6's B_x in eq.(40) labels, computed from Table 1 (READ), and what yield each
    reading gives for W_5/8 against R6's printed 0.00457.  Also checks the transcription of Table 1 against R6's prose:
    B_y 'interchanges the high and low bits' (p.58 item 2; p.37), and sigma_x B_x flips the low bit iff the high bit is
    one (p.58 item 4)."""
    W58 = (5 / 8,) + ((1 - 5 / 8) / 3,) * 3
    lit = _bdsw_perm("B_x")
    conj = _compose("sigma_y", "B_x", "sigma_y")
    sxbx = _compose("B_x", "sigma_x")
    by = _bdsw_perm("B_y")
    swap_img = (0, 1, 3, 2)
    perms = list(__import__("itertools").permutations(range(4)))
    ys = [recurrence_hashing_yield(W58, _post_from_perm(pm))[0] for pm in perms]
    return {"B_x literal (Table 1, Psi- standard) as eq.40 permutation": lit,
            "B_x literal fixes Phi+ (00)": lit[0] == 0,
            "sigma_y B_x sigma_y (item 5 conjugation) as eq.40 permutation": conj,
            "sigma_x B_x (p.58 item 4) as eq.40 permutation": sxbx,
            "swap_post map (10 <-> 11)": swap_img,
            "conjugated B_x equals swap_post map": conj == swap_img,
            "sigma_x B_x equals swap_post map": sxbx == swap_img,
            "B_y swaps the high and low bits (01 <-> 10; p.58 item 2) [transcription check]": by == (0, 2, 1, 3),
            "W_5/8 yield, B_x literal": recurrence_hashing_yield(W58, _post_from_perm(lit)),
            "W_5/8 yield, B_x conjugated (= swap_post)": recurrence_hashing_yield(W58, _post_from_perm(conj)),
            "W_5/8 yield, B_y (CONTROL: a READ bilateral rotation that is not B_x)": recurrence_hashing_yield(W58, _post_from_perm(by)),
            "permutations of the four Bell labels reproducing 0.00457 (of 24)": sum(abs(y - 0.00457) < 5e-6 for y in ys),
            "distinct yields over all 24 permutations": sorted({round(y, 10) for y in ys})}


def recurrence_hashing_yield(p, post, maxr=80):
    best = (hashing_yield(p), 0)
    frac = 1.0
    for r in range(1, maxr):
        q, pp = bdsw_step(p)
        frac *= pp / 2.0
        p = post(q)
        y = frac * hashing_yield(p)
        if y > best[0]:
            best = (y, r)
    return best


def hashing_threshold():
    W = lambda F: (F,) + ((1 - F) / 3,) * 3
    return optimize.brentq(lambda F: hashing_yield(W(F)), 0.6, 0.95, xtol=1e-12)


def rounds_from(N0, post="twirl", target=None, dps=60, maxr=4000):
    """Rounds of R6's recurrence needed before hashing pays (yield > 0), starting from a Werner state F = 1/2 + N0 (the
    harvested state twirled; R5's step A3).  High precision: N0 can be 1e-20.  Returns rounds, pairs consumed per
    surviving pair (prod 2/p_pass), and the hashing yield at the switch."""
    import mpmath as mp
    mp.mp.dps = dps
    F = mp.mpf(1) / 2 + mp.mpf(N0)
    p = [F] + [(1 - F) / 3] * 3
    target = 0.8107 if target is None else target
    cost = mp.mpf(1)
    for r in range(1, maxr):
        p00, p01, p10, p11 = p
        pp = p00 ** 2 + p01 ** 2 + p10 ** 2 + p11 ** 2 + 2 * p00 * p10 + 2 * p01 * p11
        q = [(p00 ** 2 + p10 ** 2) / pp, (p01 ** 2 + p11 ** 2) / pp, 2 * p00 * p10 / pp, 2 * p01 * p11 / pp]
        cost *= 2 / pp
        p = [q[0]] + [(1 - q[0]) / 3] * 3 if post == "twirl" else [q[0], q[1], q[3], q[2]]
        hy = 1 - sum(-x * mp.log(x, 2) for x in p if x > 0)
        if hy > 0:
            return {"rounds": r, "log10 pairs per surviving pair": float(mp.log10(cost)), "hashing yield then": float(hy),
                    "p00 then": float(p[0])}
    return {"rounds": None}


# ===================================================== H. W2 on a harvested pair (settle.bloch_exact, imported)
def bob_branches(r, axis="x"):
    """Alice measures her probe along x or z; Bob's branch probabilities and Bloch vectors."""
    proj = {"x": [(I2 + SX) / 2, (I2 - SX) / 2], "z": [(I2 + SZ) / 2, (I2 - SZ) / 2]}[axis]
    out = []
    for Pa in proj:
        o = np.kron(Pa, I2) @ r @ np.kron(Pa, I2)
        rb = np.einsum("ijik->jk", o.reshape(2, 2, 2, 2))
        p = float(np.real(np.trace(rb)))
        rb = rb / p
        out.append((p, tuple(float(np.real(np.trace(rb @ s))) for s in (SX, SY, SZ))))
    return out


def w2_signal(r, eps, T):
    """H-C2 + H-NLCONTROL-FORM (settle's law for H = eps <X> Z, imported): Bob's ensemble Bloch vector after the drift,
    Alice's x basis against her z basis; the signal is the length of the difference."""
    ST = _owner("settle")
    means = {}
    for ax in ("x", "z"):
        acc = np.zeros(3)
        for p, v in bob_branches(r, ax):
            acc += p * np.array(ST.bloch_exact(v, eps, T))
        means[ax] = acc
    rperp = max(math.hypot(v[0], v[1]) for _, v in bob_branches(r, "x"))
    # settle's law keeps z constant, so the signal is the transverse difference (z differs only by rounding here)
    return float(np.linalg.norm((means["x"] - means["z"])[:2])), rperp


# ===================================================== I. the timeline, D23 imported
def timeline(L_m, N0, window_frac):
    """Times from launch.  Probes leave a midpoint (or one end) at c and hold position from t_bob_holds
    (settle.first_transit_times, LEDGER D23 as corrected in DOCKET 67).  Harvest window = window_frac x L/c: the
    Gaussian strong support 7T = 7 L/(beta c) (R4), or Reznik's compact window T (section C).  Then two-way rounds
    (H-SIMUL, L/c each),
    then hashing (one-way, L/c).  The 'floor' key is one exchange (>= L/c) after THIS window: it is the floor for any
    protocol GIVEN the window family and gap computed (Reznik's cos^2(pi t) with Omega T in [2, 40]; the Gaussian at
    beta = 7).  The floor with no window assumption is window_free_floor() (W2-fix): t_hold + L/c, i.e. 1.50 L/c from a
    midpoint and 2.00 L/c from one end.  Wave 2 first said: 'The floor for ANY protocol is one exchange (>= L/c) after
    the window (R9)'."""
    ST = _owner("settle")
    c = ST.C_LIGHT
    tw = window_frac * L_m / c
    out = {}
    for src in ("midpoint", "one-end"):
        ft = ST.first_transit_times(L_m, 0.0, source=src)
        t0 = ft["t_bob_holds"]
        rr, rs = rounds_from(N0), rounds_from(N0, post="swap")
        R = rr["rounds"] or float("nan")
        Rs = rs["rounds"] or float("nan")
        out[src] = {"probes hold from (D23, imported)": t0, "harvest window": tw,
                    "floor: one two-way exchange (R9)": t0 + tw + L_m / c,
                    "BBPSSW recurrence + hashing (H-PROTOCOL)": t0 + tw + (R + 1) * L_m / c,
                    "recurrence with the 10<->11 rotation + hashing (H-PROTOCOL)": t0 + tw + (Rs + 1) * L_m / c,
                    "rounds": R, "rounds (rotation)": Rs, "light time L/c": L_m / c,
                    "midpoint pair source ready (D23)": L_m / (2 * c)}
    return out


def rrs_lower_bound(L_over_cT):
    """R2 eq.(8) (READ): N >= exp(-(L/cT)^3) for R2's superoscillating windows of duration T (cT << L).  A LOWER bound
    on what R2's construction guarantees; no READ UPPER bound covers 3+1 detectors with every window (OPEN)."""
    return math.exp(-L_over_cT ** 3)


def window_free_floor(L_m, cT_over_L=(1.0, 0.5, 0.25, 0.1)):
    """W2-fix (verifiers W2V-0 problem 1, W2V-1 problem 1): the vacuum route's floor with NO window-family assumption.
    Times from launch, the same accounting as timeline(): probes move at c and hold from t_bob_holds
    (settle.first_transit_times, imported: L/2c from a midpoint, L/c from one end), the harvest window T_window, then
    at least one classical exchange (>= L/c).  T_window -> 0 is admissible: R2 harvests with cT << L at every L.  So the
    floor is t_hold + L/c, approached as T_window -> 0, at a negativity R2 guarantees only down to exp(-(L/cT)^3).
    The exchange is required for ANY state, whatever window made it: with no message, local operations raise neither
    N (R7 Prop.3) nor f above 1/2 + N (R7 eq.39, R8 Thm 1), so a near-maximal pair (H-NEARMAX) needs at least one
    message, which takes >= L/c (H-LOCC).  R9's two-way requirement is computed only for the Gaussian and Reznik states
    (section D); for R2's windows it is not computed, and the floor here does not use it."""
    ST = _owner("settle")
    c = ST.C_LIGHT
    out = {}
    for src in ("midpoint", "one-end"):
        t0 = ST.first_transit_times(L_m, 0.0, source=src)["t_bob_holds"]
        out[src] = {"probes hold from (D23, imported)": t0, "harvest window (limit)": 0.0,
                    "window-free floor t_hold + L/c": t0 + L_m / c, "light time L/c": L_m / c,
                    "midpoint pair source ready (D23)": L_m / (2 * c),
                    "floor with a window cT = x L (x: floor in L/c)": {x: (t0 + x * L_m / c + L_m / c) / (L_m / c)
                                                                     for x in cT_over_L},
                    "R2 guaranteed N >= exp(-(L/cT)^3) at cT = x L": {x: rrs_lower_bound(1.0 / x) for x in cT_over_L}}
    return out


# ===================================================== J. assembly, grades
CASES = {  # Gaussian windows at the optimal gap (N+), and Reznik's compact window at L = T (touching, its best point)
    "gauss beta=3 (communication not excluded)": 3.0,
    "gauss beta=5 (communication not excluded)": 5.0,
    "gauss beta=7 (strong supports spacelike, R4)": 7.0,
}


def build_cases():
    out = {}
    for name, b in CASES.items():
        a, n = nmax_gauss(b, True)
        P, Mp, Mm, Lab = L_AA(a), M_plus(a, b), M_minus(a, b), L_AB(a, b)
        M = complex(Mp, Mm)                       # the -i term carries the commutator; kept so the state is R3's
        out[name] = {"alpha": a, "beta": b, "L_AA": P, "|M+|": Mp, "|M-|": Mm, "|L_AB|": abs(Lab), "N+/lambda^2": n}
    return out


def state_for(case, lam):
    P = case["L_AA"] * lam ** 2
    M = complex(case["|M+|"], case["|M-|"]) * lam ** 2
    Lab = case["|L_AB|"] * lam ** 2
    return harvested_state(P, M, Lab)


GRADES = {
    "N_VAC as combine carries it ('pre-existing entanglement usable as the channel's pairs with no distribution')":
        "SPLIT, computed.  (i) The vacuum's entanglement reaches probes that cannot communicate: TRUE given "
        "{H-UDW, H-PERTURB, H-MINK-VAC, H-SPACELIKE} (R1, R2, R3, R4 READ; R1's two figures reproduced).  No entangled "
        "carrier crosses.  (ii) Usable as the channel's pairs with nothing crossing at <= c first: FALSE given "
        "{H-LOCC, H-NEARMAX, H-PROBE-OPERATED} -- the probes cross (D23), a near-maximal pair needs at least one "
        "classical message (R7 Prop.3 / R8 Thm 1, any state) and, in the two computed families, messages in BOTH "
        "directions (R9: the harvested state there is symmetric extendible both ways, so zero-way and one-way "
        "distillation are impossible; R9 is not computed for R2's windows), and the window itself lasts >= 0.91 L/c for Reznik's cos^2(pi t) window with "
        "Omega T in [2, 40], or 7T = 7L/(beta c) for the Gaussian at beta = 7 -- those two families only.  With no "
        "window assumption (R2 harvests with cT << L at every L) the floor is t_hold + L/c: >= 1.50 L/c from a midpoint, "
        ">= 2.00 L/c from one end (window_free_floor), still after the light time and after a midpoint pair source "
        "(0.50 L/c), at a negativity R2 guarantees only down to exp(-(L/cT)^3).  Wave 2 first said 'the window itself "
        "lasts >= 0.91 L/c (compact) or 7T = 7L/(beta c)', unscoped, and 'a near-maximal pair needs classical "
        "messages in BOTH directions', with no family scope.",
    "O-MAKE-DIST":
        "LEFT-IF {H-UDW, H-PERTURB, H-O4-FLOOR, H-MINK-VAC, H-SPACELIKE, H-LOCC, H-IID, H-NEARMAX, H-PROBE-OPERATED}: "
        "the distribution is not removed but relocated -- from the pairs to the probes (<= c, D23) and to at least "
        "one classical message (>= L/c after the window; two-way (R9) in the two computed families, the Gaussian and "
        "Reznik's; for R2's windows only >= 1 message is shown, R7 Prop.3 / R8 Thm 1; the window is ~ L/c in the two "
        "families computed and -> 0 admissible in R2's, so the floor is >= 1.50 L/c midpoint / 2.00 L/c one end, "
        "which needs only the one message).  OPEN outside that set via "
        "N_NLDIST, N_W2WEAK, N_VACNP, "
        "none computed.  Wave 2 first said 'relocated ... to two-way classical messages', with no family scope.  "
        "Wave 1 said: OPEN via N_VAC only.",
    "weak pairs consumed as they are (H-NEARMAX dropped)":
        "teleportation fidelity (2f + 1)/3 = 2/3 + 2N/3 (computed; f = 1/2 + N for the harvested state, the R8 "
        "Thm 1 / R7 eq.39 ceiling for any LOCC on one copy, so no processing of a single copy does better): at "
        "beta = 7, lambda = 0.1 the excess over the classical 2/3 is 2.7e-17.  W2 (settle.bloch_exact, H-C2, "
        "H-NLCONTROL-FORM): Bob's branch transverse length rho_perp = 3.1e-15 and the signal is SECOND order in it, "
        "<= 2 eps T rho_perp^2 (5.8e-30 at eps = 0.1, T = 3, against 0.537 for a Bell pair).  Neither is zero; neither "
        "moves O-BITS (the two classical bits are untouched by any of this).",
    "scaling with distance":
        "at fixed window T the harvested negativity falls faster than any power of L in both computed families: "
        "Gaussian N+_max ~ (e/2pi) e^{-beta^2/2} beta^-4 at alpha^2 ~ beta^2 - 2 (DERIVED; within 1% at beta = 14); "
        "Reznik's compact window harvests for no gap in [2, 40] beyond L/T ~ 1.0975.  R2's superoscillating windows "
        "harvest at every L, with LOWER bounds e^{-(L/cT)^3} (analytic) and e^{-(L/T)^2} (numerical) -- also falling.  "
        "No READ upper bound for 3+1 detectors over all windows: OPEN (R11 is 1D and about the field's regions).  The "
        "massless model has no scale of its own: N depends only on (Omega T, L/cT), so a fixed negativity at any L "
        "needs a window T proportional to L -- the harvest itself lasts a fixed fraction of the light time.",
}


def build():
    R = {}
    R["A_reznik"] = reznik_reproduction()
    R["A_reading_note"] = sudden_window_divergence()
    checks_b = []
    for a, b in ((1.0, 1.0), (3.0, 2.0), (5.0, 4.0), (7.0, 7.0)):
        mn = M_numeric(a, b)
        checks_b.append({"alpha": a, "beta": b, "L_AA closed": L_AA(a), "L_AA numeric": L_AA_numeric(a),
                         "M+ closed": M_plus(a, b), "M+ numeric": mn[0], "M- closed": M_minus(a, b), "M- numeric": mn[1],
                         "L_AB closed": L_AB(a, b), "L_AB numeric": L_AB_numeric(a, b)})
    R["B_closed_vs_numeric"] = checks_b
    R["B_scaling"] = gauss_scaling()
    R["C_compact"] = compact_scan()
    R["C_boundary"] = compact_boundary()
    R["cases"] = build_cases()
    per = {}
    for name, c in R["cases"].items():
        row = {}
        for lam in (0.1, 0.01):
            r = state_for(c, lam)
            N = negativity_x(r)
            f = fef_x(r)
            fmh = fef_minus_half_x(r)
            EN = math.log1p(2.0 * N) / math.log(2.0)
            r10 = harvested_state(float(r[1, 1].real), complex(r[3, 0]), complex(r[2, 1]), 10.0)
            row[f"lambda={lam}"] = {
                "N": N, "E_N (bits)": EN, "f": f, "f - 1/2": fmh, "1/2 + N": 0.5 + N,
                "teleport fidelity (2f+1)/3": (2 * f + 1) / 3, "teleport excess over 2/3": 2 * fmh / 3,
                "copies per ebit >= 1/E_N (R7 Prop.7)": (1.0 / EN) if N > 0 else float("inf"),
                "sym-ext margin on B (floor rho_ee)": sym_ext_margin_x(r, "B"),
                "sym-ext margin on A (floor rho_ee)": sym_ext_margin_x(r, "A"),
                "sym-ext margin on B (10x floor)": sym_ext_margin_x(r10, "B"),
                "sym-ext margin on A (10x floor)": sym_ext_margin_x(r10, "A"),
                "2 L_AA (leading-order margin)": 2.0 * float(r[1, 1].real),
                "BBPSSW rounds before hashing pays (twirl)": rounds_from(N),
                "rounds with the 10<->11 rotation": rounds_from(N, post="swap"),
            }
        per[name] = row
    R["D_states"] = per
    c7 = R["cases"]["gauss beta=7 (strong supports spacelike, R4)"]
    r7 = state_for(c7, 0.1)
    # a state whose N double precision resolves (beta = 3, lambda = 0.3): the theorem checks and the X-state formulas
    r3 = state_for(R["cases"]["gauss beta=3 (communication not excluded)"], 0.3)
    R["D_resolvable_beta3_lambda0.3"] = {
        "N eig": negativity(r3), "N exact-X": negativity_x(r3), "f SVD (Horodecki)": fully_entangled_fraction(r3),
        "f X-formula": fef_x(r3), "teleport simulated (phase-aligned)": teleport_fidelity(phase_align(r3)),
        "(2f+1)/3": (2 * fef_x(r3) + 1) / 3, "sym-ext B generic": sym_ext_margin(r3, "B"),
        "sym-ext B X-formula": sym_ext_margin_x(r3, "B"), "sym-ext A generic": sym_ext_margin(r3, "A"),
        "sym-ext A X-formula": sym_ext_margin_x(r3, "A")}
    R["E_lo"] = lo_test(r3)
    R["E_controls"] = global_controls(r3)
    a_over = 3.0 * c7["beta"]                   # gap well above the optimum: |M|/L_AA larger, |M| exponentially smaller
    Pv, Mpv, Mmv, Lv = L_AA(a_over), M_plus(a_over, 7.0), M_minus(a_over, 7.0), L_AB(a_over, 7.0)
    r_over = harvested_state(Pv * 0.01, complex(Mpv, Mmv) * 0.01, abs(Lv) * 0.01)
    R["E_filter_opt_gap"] = filtering(r3, abs(r3[3, 0]))
    R["E_filter_high_gap"] = dict(filtering(r_over, abs(r_over[3, 0])), alpha=a_over, ratio_M_over_LAA=Mpv / Pv)
    R["F_werner_boundary"] = {F: sym_ext_margin(werner(F)) for F in (0.70, 0.74, 0.7499, 0.7501, 0.76, 0.80)}
    R["F_bell"] = sym_ext_margin(werner(1.0))
    R["G_hashing_threshold"] = hashing_threshold()
    W58 = (5 / 8,) + ((1 - 5 / 8) / 3,) * 3
    R["G_W58"] = {"twirl recurrence + hashing": recurrence_hashing_yield(W58, twirl_post),
                  "10<->11 rotation + hashing": recurrence_hashing_yield(W58, swap_post),
                  "no rotation (control)": recurrence_hashing_yield(W58, lambda q: q),
                  "READ": "D2(W_5/8) > 0.00457 (R6 p.42, recurrence-hashing D_M)"}
    R["G_eq7_vs_eq42"] = max(abs(bbpssw_map(F) - bdsw_step((F,) + ((1 - F) / 3,) * 3)[0][0]) for F in np.linspace(0.3, 0.99, 50))
    R["G_rounds_vs_N0"] = {N0: rounds_from(N0) for N0 in (1e-2, 1e-4, 1e-8, 1e-12, 1e-17, 1e-20)}
    R["G_bdsw_bx"] = bdsw_bx_from_table1()
    # H. W2 on harvested pairs
    ST = _owner("settle")
    bell = np.outer(_bell_phi_plus(), _bell_phi_plus().conj())
    w2 = {}
    for eps, T in ((0.1, 3.0), (0.3, 3.0), (1.0, 30.0)):
        sb, _ = w2_signal(bell, eps, T)
        sh, rp = w2_signal(r7, eps, T)
        w2[f"eps={eps}, T={T}"] = {"Bell signal": sb, "settle.bob_y_exact (imported law)": ST.bob_y_exact(eps, T),
                                   "harvested signal (beta=7, lambda=0.1)": sh, "rho_perp of Bob's branches": rp,
                                   "signal / (2 eps T rho_perp^2)": sh / (2 * eps * T * rp * rp)}
    R["H_w2"] = w2
    # I. timeline at the board's distances
    R["I_timeline"] = {}
    Nc = [r for r in R["C_compact"]["rows"] if r["L/T"] == 1.05][0]["N_max/lambda^2"] * 0.01   # lambda = 0.1
    R["I_inputs"] = {"gauss beta=7, lambda=0.1": {"N0": negativity_x(r7), "window/(L/c)": 7.0 / 7.0},
                     "Reznik compact window at L/T = 1.05, lambda=0.1": {"N0": Nc, "window/(L/c)": 1.0 / 1.05},
                     "every-gap compact boundary T/(L/c)": R["C_boundary"]["T/(L/c) at the boundary"]}
    for lab, Lm in (("1 AU", ST.AU_M), ("1 ly", ST.LY_M)):
        R["I_timeline"][lab] = {k: timeline(Lm, v["N0"], v["window/(L/c)"]) for k, v in R["I_inputs"].items()
                                if isinstance(v, dict)}
        R["I_timeline"][lab]["years per second"] = 1.0 / ST.YEAR_S
    R["I_window_free"] = {lab: window_free_floor(Lm) for lab, Lm in (("1 AU", ST.AU_M), ("1 ly", ST.LY_M))}
    TR = _owner("transit")
    R["I_board"] = {"transit.TRAVERSAL_IS_REMOVED": TR.TRAVERSAL_IS_REMOVED,
                    "transit.CLASSICAL_BITS_PER_QUBIT": TR.CLASSICAL_BITS_PER_QUBIT,
                    "transit.READING_CARRIES_NOTHING_ALONE": TR.READING_CARRIES_NOTHING_ALONE}
    R["GRADES"] = GRADES
    return R


RPK = "rho_perp of Bob's branches"


def _fmt(R):
    L = []
    A = R["A_reznik"]
    L.append("A. Reznik quant-ph/0212044v2, inertial probes, window cos^2(pi t) (READING NOTE), T = 1")
    lo, hi = A["fig1_omega_window_computed"]
    L.append(f"   Fig.1 (L = T): entangled for {lo:.3f} < Omega < {hi:.3f}  [READ: 8 < Omega < 11]; peak ratio "
             f"{A['fig1_peak'][1]:.3f} at Omega = {A['fig1_peak'][0]:.2f}")
    L.append(f"   Fig.2 (Omega = 9.5): entangled for L/T < {A['fig2_L_crossing_computed']:.4f}  [READ: L/T < 1.1]")
    L.append(f"   => window T/(L/c) in ({A['window_T_over_light_time'][0]:.4f}, 1)  [combine's DERIVED-FROM-READ 0.909]")
    rn = R["A_reading_note"]
    L.append(f"   reading note: emission integral cutoff 500 -> 8000: sudden x{rn['sudden_growth']:.3f}, smooth x{rn['smooth_growth']:.6f}")
    L.append("B. Gaussian switching (Pozas-Kerstjens & Martin-Martinez eqs.33, 34, 37), per lambda^2; N+ = harvested only (Tjoa-MM)")
    for row in R["B_scaling"]:
        L.append(f"   beta={row['beta=L/cT']:>5}: alpha_opt={row['alpha_opt (N+)']:.3f}  N+_max={row['N+_max/lambda^2']:.3e}"
                 f"  N_max={row['N_max/lambda^2 (incl. commutator)']:.3e}  N+/asym={row['ratio N+/asymptote']:.4f}"
                 f"{'  [spacelike supports]' if row['strong supports spacelike (beta >= 7, R4)'] else ''}")
    L.append("C. Reznik's compact window, strictly spacelike, best gap in [2, 40]:")
    for row in R["C_compact"]["rows"]:
        L.append(f"   L/T={row['L/T']:<5} best Omega T={row['best Omega T']:.2f}  N_max/lambda^2={row['N_max/lambda^2']:.3e}")
    L.append(f"   largest L/T in the grid with any harvest: {R['C_compact']['largest L/T in grid with harvest (Omega T in [2, 40])']}; "
             f"boundary {R['C_boundary']['L/T boundary (Omega T in [2, 40])']:.4f} (best gap just inside {R['C_boundary']['best Omega T just inside']:.2f})")
    L.append("D. harvested states (gap at the N+ optimum), lambda = 0.1 and 0.01 (H-LAMBDA-ILLUSTRATIVE)")
    for name, row in R["D_states"].items():
        for lam, d in row.items():
            rr, rs = d["BBPSSW rounds before hashing pays (twirl)"], d["rounds with the 10<->11 rotation"]
            L.append(f"   {name}, {lam}: N={d['N']:.3e}  f-1/2={d['f - 1/2']:.3e}  teleport-2/3={d['teleport excess over 2/3']:.3e}"
                     f"  copies/ebit>={d['copies per ebit >= 1/E_N (R7 Prop.7)']:.3e}  symext(B,A)=({d['sym-ext margin on B (floor rho_ee)']:.2e},"
                     f"{d['sym-ext margin on A (floor rho_ee)']:.2e})  rounds twirl={rr.get('rounds')} (10^{rr.get('log10 pairs per surviving pair', float('nan')):.0f} pairs)"
                     f" rot={rs.get('rounds')} (10^{rs.get('log10 pairs per surviving pair', float('nan')):.0f})")
    e = R["E_lo"]
    L.append(f"E. local operations only (3000 random channels + amplitude damping): max rise of N {e['max rise of N under LO']:.2e}; "
             f"max f - (1/2 + N) {e['max of f - (1/2 + N0) under LO']:.2e}")
    g = R["E_controls"]
    L.append(f"   controls: global unitary f = {g['f after a global unitary']:.4f} (bound {g['bound 1/2 + N']:.6f}); CNOT on a product: N "
             f"{g['N(product)']:.1f} -> {g['N(CNOT product)']:.3f}")
    for k in ("E_filter_opt_gap", "E_filter_high_gap"):
        fl = R[k]
        L.append(f"   filter ({k}): heralded p = {fl['heralded p']:.3e}, heralded f = {fl['heralded f']:.4f} (unfiltered {fl['unfiltered f']:.6f}); "
                 f"sum p_i N_i = {fl['sum p_i N_i']:.3e} <= N = {fl['N before']:.3e}")
    L.append("F. symmetric extension (Chen et al. Thm 1): Werner margins " +
             ", ".join(f"F={F}: {v:+.4f}" for F, v in R["F_werner_boundary"].items()) + f"; Bell {R['F_bell']:+.3f}")
    L.append(f"G. hashing threshold {R['G_hashing_threshold']:.5f} [READ 0.8107]; W_5/8: " +
             "; ".join(f"{k} {v if isinstance(v, str) else f'{v[0]:.6f} ({v[1]} rounds)'}" for k, v in R["G_W58"].items()))
    L.append("   rounds before hashing pays, from F = 1/2 + N0 (twirl): " +
             ", ".join(f"N0={k:g}: {v['rounds']}" for k, v in R["G_rounds_vs_N0"].items()))
    L.append("H. W2 (settle.bloch_exact, H-C2, H-NLCONTROL-FORM) on a Bell pair and on a harvested pair (beta = 7, lambda = 0.1):")
    for k, v in R["H_w2"].items():
        L.append(f"   {k}: Bell {v['Bell signal']:.6f} (law {v['settle.bob_y_exact (imported law)']:.6f}); harvested "
                 f"{v['harvested signal (beta=7, lambda=0.1)']:.3e} <= rho_perp {v[RPK]:.3e}")
    L.append("I. timeline (seconds; probes from a midpoint / one end, D23 via settle.first_transit_times):")
    for lab, d in R["I_timeline"].items():
        for w, tl in ((k, v) for k, v in d.items() if isinstance(v, dict)):
            for src, t in tl.items():
                L.append(f"   {lab} {w} {src}: hold {t['probes hold from (D23, imported)']:.4g}, window {t['harvest window']:.4g}, "
                         f"floor {t['floor: one two-way exchange (R9)']:.4g} ({t['floor: one two-way exchange (R9)'] / t['light time L/c']:.3f} L/c), "
                         f"BBPSSW {t['BBPSSW recurrence + hashing (H-PROTOCOL)'] / t['light time L/c']:.1f} L/c, rotation "
                         f"{t['recurrence with the 10<->11 rotation + hashing (H-PROTOCOL)'] / t['light time L/c']:.1f} L/c; midpoint pairs "
                         f"{t['midpoint pair source ready (D23)'] / t['light time L/c']:.2f} L/c")
    gb = R["G_bdsw_bx"]
    L.append(f"   B_x from R6 Table 1 (READ): literal {gb['B_x literal (Table 1, Psi- standard) as eq.40 permutation']} "
             f"(fixes 00: {gb['B_x literal fixes Phi+ (00)']}); sigma_y-conjugated "
             f"{gb['sigma_y B_x sigma_y (item 5 conjugation) as eq.40 permutation']} = swap_post: "
             f"{gb['conjugated B_x equals swap_post map']}; "
             f"W_5/8 yields: literal {gb['W_5/8 yield, B_x literal'][0]:.10f}, conjugated "
             f"{gb['W_5/8 yield, B_x conjugated (= swap_post)'][0]:.10f}, B_y (control) "
             f"{gb['W_5/8 yield, B_y (CONTROL: a READ bilateral rotation that is not B_x)'][0]:.10f}; "
             f"{gb['permutations of the four Bell labels reproducing 0.00457 (of 24)']} of 24 label permutations reproduce 0.00457")
    L.append("I'. window-free floor (W2-fix; R2: T_window -> 0 admissible): t_hold + L/c, in L/c")
    for lab, d in R["I_window_free"].items():
        for src, t in d.items():
            L.append(f"   {lab} {src}: {t['window-free floor t_hold + L/c'] / t['light time L/c']:.3f} L/c (midpoint pair source "
                     f"{t['midpoint pair source ready (D23)'] / t['light time L/c']:.2f}); with cT = xL: " +
                     ", ".join(f"x={x}: {v:.3f} L/c, R2 N >= {t['R2 guaranteed N >= exp(-(L/cT)^3) at cT = x L'][x]:.3g}"
                               for x, v in t["floor with a window cT = x L (x: floor in L/c)"].items()))
    L.append("GRADES:")
    for k, v in R["GRADES"].items():
        L.append(f"   {k}: {v}")
    return "\n".join(L)


def selftest():
    R = build()
    checks = []
    ok = lambda name, cond, detail="": checks.append((name, bool(cond), detail))
    structural = lambda name, cond, detail="": checks.append(("STRUCTURAL (cannot fail; not evidence) " + name, bool(cond), detail))
    A = R["A_reznik"]
    lo, hi = A["fig1_omega_window_computed"]
    ok("A1 Reznik Fig.1 lower edge reproduced (READ 8): computed in [7.5, 8.5]", 7.5 <= lo <= 8.5, f"{lo:.4f}")
    ok("A2 Reznik Fig.1 upper edge reproduced (READ 11): computed in [10.0, 11.5]", 10.0 <= hi <= 11.5, f"{hi:.4f}")
    ok("A3 Reznik Fig.2 edge reproduced (READ L/T < 1.1): computed in [1.05, 1.15]",
       1.05 <= A["fig2_L_crossing_computed"] <= 1.15, f"{A['fig2_L_crossing_computed']:.5f}")
    worst = max(abs(exchange_momentum(Om, L) - exchange_time(Om, L).real) / abs(exchange_time(Om, L))
                for Om, L in ((9.5, 1.1), (6.0, 1.3), (14.0, 1.05)))
    ok("A4 exchange amplitude: momentum route = time route (two independent integrals)", worst < 1e-6, f"rel {worst:.1e}")
    imag = max(abs(exchange_time(Om, L).imag) for Om, L in ((9.5, 1.1), (6.0, 1.3)))
    structural("A4b the time-route amplitude is real for a symmetric window (symmetry)", imag < 1e-12, f"{imag:.1e}")
    rn = R["A_reading_note"]
    ok("A5 CONTROL (reading note): the literal cos^2(t) window's emission integral grows with the cutoff, the "
       "cos^2(pi t) window's does not", rn["sudden_growth"] > 1.05 and abs(rn["smooth_growth"] - 1) < 1e-4,
       f"sudden x{rn['sudden_growth']:.3f}, smooth x{rn['smooth_growth']:.7f}")
    wrongP = max(abs(exchange_momentum(Om, 1.0)) / (2 * emission(Om)) for Om in np.linspace(7, 12, 11))
    ok("A6 CONTROL: a factor-2 error in the emission term would erase Fig.1's window (max ratio < 1)", wrongP < 1.0,
       f"{wrongP:.3f}")
    rel = []
    for row in R["B_closed_vs_numeric"]:
        rel += [abs(row["L_AA closed"] - row["L_AA numeric"]) / row["L_AA closed"],
                abs(row["M+ closed"] - row["M+ numeric"]) / row["M+ closed"],
                abs(row["M- closed"] - row["M- numeric"]) / row["M- closed"],
                abs(abs(row["L_AB closed"]) - abs(row["L_AB numeric"])) / max(abs(row["L_AB numeric"]), 1e-300)]
    ok("B1 PKMM eqs.33, 34, 37 = independent integrals (L_AA, M+, M-, L_AB) at four (alpha, beta)", max(rel) < 1e-5,
       f"max rel {max(rel):.1e}")
    reim = max(abs(row["L_AB closed"].imag) for row in R["B_closed_vs_numeric"])
    structural("B1b L_AB at gamma = 0 is real: w(-z1) = conj(w(z2)), so i x (conj(w) - w) is real (identity). "
               "Wave-2 draft first said 'purely imaginary'; B1 caught the draft's loose numeric route, not this", reim < 1e-12,
               f"{reim:.1e}")
    sc = {row["beta=L/cT"]: row for row in R["B_scaling"]}
    ok("B2 asymptote (e/2pi) e^{-b^2/2} b^-4 approached: ratio within 2% at beta = 12 and 14, moving toward 1",
       abs(sc[14]["ratio N+/asymptote"] - 1) < 0.02 and abs(sc[12]["ratio N+/asymptote"] - 1) < 0.025
       and abs(sc[14]["ratio N+/asymptote"] - 1) < abs(sc[8]["ratio N+/asymptote"] - 1),
       f"{sc[8]['ratio N+/asymptote']:.4f}, {sc[12]['ratio N+/asymptote']:.4f}, {sc[14]['ratio N+/asymptote']:.4f}")
    wr = sc[14]["N+_max/lambda^2"] / nmax_asymptote_wrong(14)
    ok("B3 CONTROL: the first hand derivation (no 1/b^4, 3/a^4 terms) is off by ~e^2 and is rejected", abs(wr - math.e ** 2) < 0.3,
       f"ratio {wr:.3f} vs e^2 = {math.e ** 2:.3f}")
    ok("B4 optimal gap alpha^2 ~ beta^2 - 2 at large beta (DERIVED): within 0.02 at beta = 14",
       abs(sc[14]["alpha_opt (N+)"] - sc[14]["sqrt(beta^2-2)"]) < 0.02, f"{sc[14]['alpha_opt (N+)']:.4f} vs {sc[14]['sqrt(beta^2-2)']:.4f}")
    dec = all(sc[b1]["N+_max/lambda^2"] > sc[b2]["N+_max/lambda^2"] for b1, b2 in ((1, 2), (2, 3), (3, 5), (5, 7), (7, 10), (10, 14)))
    ok("B5 harvested negativity at the best gap falls with beta at every step", dec)
    comm = sc[1]["N_max/lambda^2 (incl. commutator)"] / max(sc[1]["N+_max/lambda^2"], 1e-300)
    ok("B6 at beta = 1 the commutator (communication) part matters (Tjoa-MM); at beta = 7 it does not",
       comm > 1.5 and abs(sc[7]["N_max/lambda^2 (incl. commutator)"] / sc[7]["N+_max/lambda^2"] - 1) < 1e-6,
       f"beta=1 N/N+ = {comm:.2f}")
    C = R["C_compact"]
    rows = {r["L/T"]: r for r in C["rows"]}
    cb = R["C_boundary"]["L/T boundary (Omega T in [2, 40])"]
    ok("C2 compact window: the every-gap boundary lies at or just beyond Fig.2's single-gap edge (Omega = 9.5)",
       A["fig2_L_crossing_computed"] - 1e-4 <= cb <= 1.1, f"{cb:.5f} vs {A['fig2_L_crossing_computed']:.5f}")
    ok("C1 compact window: harvest at L = T (best gap), none at L/T = 1.6 for any gap in [2, 40]",
       rows[1.0]["N_max/lambda^2"] > 0 and rows[1.6]["N_max/lambda^2"] == 0.0,
       f"{rows[1.0]['N_max/lambda^2']:.3e}, last L/T with harvest {C['largest L/T in grid with harvest (Omega T in [2, 40])']}")
    for name, row in R["D_states"].items():
        for lam, d in row.items():
            structural(f"D0 {name} {lam}: f - 1/2 = N for this X-state (identical probes: an identity)",
                       abs(d["f - 1/2"] - d["N"]) <= 1e-9 * d["N"] + 1e-300, f"{d['f - 1/2']:.3e} vs {d['N']:.3e}")
            ok(f"D2 {name} {lam}: symmetric extendible on B and on A, at the rho_ee floor and at 10x -> no zero- or "
               f"one-way distillation (R9); margin ~ 2 L_AA",
               min(d["sym-ext margin on B (floor rho_ee)"], d["sym-ext margin on A (floor rho_ee)"],
                   d["sym-ext margin on B (10x floor)"], d["sym-ext margin on A (10x floor)"]) > 0
               and abs(d["sym-ext margin on B (floor rho_ee)"] / d["2 L_AA (leading-order margin)"] - 1) < 0.01,
               f"{d['sym-ext margin on B (floor rho_ee)']:.3e} vs 2L_AA {d['2 L_AA (leading-order margin)']:.3e}")
    rz = R["D_resolvable_beta3_lambda0.3"]
    ok("D1 resolvable state (beta 3, lambda 0.3): eigensolver N = exact X-state N", abs(rz["N eig"] - rz["N exact-X"]) < 1e-14 * 1e3,
       f"{rz['N eig']:.6e} vs {rz['N exact-X']:.6e}")
    ok("D1b resolvable state: Horodecki SVD f = X-state f = 1/2 + N (R8 Thm 1 saturated)",
       abs(rz["f SVD (Horodecki)"] - rz["f X-formula"]) < 1e-12 and abs(rz["f X-formula"] - 0.5 - rz["N exact-X"]) < 1e-12)
    ok("D1c resolvable state: simulated teleportation = (2f+1)/3 (protocol vs formula)",
       abs(rz["teleport simulated (phase-aligned)"] - rz["(2f+1)/3"]) < 1e-12 and rz["(2f+1)/3"] > 2 / 3)
    ok("D1d resolvable state: generic symmetric-extension margin = X-state formula, both directions",
       abs(rz["sym-ext B generic"] - rz["sym-ext B X-formula"]) < 1e-12 and abs(rz["sym-ext A generic"] - rz["sym-ext A X-formula"]) < 1e-12)
    TR = _owner("transit")
    bell = np.outer(_bell_phi_plus(), _bell_phi_plus().conj())
    psi = [complex(0.6, 0.0), complex(0.0, 0.8)]
    tr_f = min(TR.fidelity(psi, v) for _, v in TR.teleport(psi))
    ok("D3 CONTROL: a Bell resource teleports at fidelity 1, as transit.teleport (imported) does",
       abs(teleport_fidelity(bell) - 1) < 1e-12 and abs(tr_f - 1) < 1e-12)
    gg = np.zeros((4, 4), dtype=complex)
    gg[0, 0] = 1
    ok("D4 CONTROL: a product resource gives the classical 2/3", abs(teleport_fidelity(gg) - 2 / 3) < 1e-12)
    e = R["E_lo"]
    ok("E1 local operations alone never raise the negativity (R7 Prop.3), 3000 random channels + damping",
       e["max rise of N under LO"] < 1e-12, f"{e['max rise of N under LO']:.1e}")
    ok("E2 local operations alone never pass f = 1/2 + N (R7 eq.39, R8 Thm 1)", e["max of f - (1/2 + N0) under LO"] < 1e-12,
       f"{e['max of f - (1/2 + N0) under LO']:.1e}")
    g = R["E_controls"]
    ok("E3 CONTROL: a global unitary passes the bound (the test can fail)", g["f after a global unitary"] > g["bound 1/2 + N"] + 0.4)
    ok("E4 CONTROL: a CNOT (not local) raises N on a product state", g["N(product)"] < 1e-12 and g["N(CNOT product)"] > 0.49)
    for k in ("E_filter_opt_gap", "E_filter_high_gap"):
        fl = R[k]
        ok(f"E5 {k}: filtering does not raise the average negativity (R7 Prop.3)", fl["sum p_i N_i"] <= fl["N before"] * (1 + 1e-9))
    fh = R["E_filter_high_gap"]
    ok("E6 high-gap filter (R2): heralded f well above the unfiltered f, success probability ~ |M|^2 (exponentially small)",
       fh["heralded f"] > fh["unfiltered f"] + 0.2 and fh["heralded p"] < 1e-30, f"f {fh['heralded f']:.4f}, p {fh['heralded p']:.2e}")
    wb = R["F_werner_boundary"]
    ok("F1 CONTROL (R9 p.4): Werner states extendible below F = 3/4, not above", wb[0.7499] > 0 and wb[0.7501] < 0 and wb[0.70] > 0 and wb[0.80] < 0)
    ok("F2 CONTROL: a Bell state has no symmetric extension", R["F_bell"] < 0)
    ok("G1 hashing threshold 1 - S(W_F) = 0 at F = 0.8107 (R5 eq.8 READ)", abs(R["G_hashing_threshold"] - 0.8107) < 5e-5,
       f"{R['G_hashing_threshold']:.6f}")
    ok("G2 R5 eq.7 = R6 eqs.42-43 under the twirl (two READ forms agree)", R["G_eq7_vs_eq42"] < 1e-14)
    gw = R["G_W58"]
    ok("G3 recurrence-hashing yield of W_5/8 with the 10<->11 rotation = R6's printed 0.00457",
       abs(gw["10<->11 rotation + hashing"][0] - 0.00457) < 5e-6, f"{gw['10<->11 rotation + hashing'][0]:.7f}")
    ok("G4 CONTROL: with no rotation the same procedure does not reproduce it", gw["no rotation (control)"][0] < 1e-4)
    gb = R["G_bdsw_bx"]
    ok("G6 (W2-fix) R6 Table 1 (READ) transcribed consistently with R6's prose: B_y swaps the high and low bits (p.58 item 2) "
       "and sigma_x B_x flips the low bit iff the high bit is one (p.58 item 4) -- both in eq.(40) labels",
       gb["B_y swaps the high and low bits (01 <-> 10; p.58 item 2) [transcription check]"]
       and gb["sigma_x B_x (p.58 item 4) as eq.40 permutation"] == (0, 1, 3, 2))
    ok("G7 (W2-fix) R6's B_x (p.29, READ) against Table 1 (READ): literally 00 <-> 01 (it moves Phi+); conjugated by item 5's "
       "sigma_y it is exactly swap_post's 10 <-> 11; both reproduce 0.00457 (they differ by a symmetry of eqs.42-43)",
       gb["B_x literal (Table 1, Psi- standard) as eq.40 permutation"] == (1, 0, 2, 3)
       and gb["conjugated B_x equals swap_post map"]
       and abs(gb["W_5/8 yield, B_x literal"][0] - 0.00457) < 5e-6
       and abs(gb["W_5/8 yield, B_x conjugated (= swap_post)"][0] - gb["W_5/8 yield, B_x literal"][0]) < 1e-15,
       f"literal {gb['W_5/8 yield, B_x literal'][0]:.10f}, conjugated {gb['W_5/8 yield, B_x conjugated (= swap_post)'][0]:.10f}")
    ok("G8 CONTROL (must fail): B_y, a READ bilateral rotation that is not B_x, does NOT reproduce 0.00457; the yield "
       "separates the 24 label maps into 3 classes, 8 of which reproduce",
       abs(gb["W_5/8 yield, B_y (CONTROL: a READ bilateral rotation that is not B_x)"][0] - 0.00457) > 1e-3
       and gb["permutations of the four Bell labels reproducing 0.00457 (of 24)"] == 8
       and len(gb["distinct yields over all 24 permutations"]) == 3,
       f"B_y {gb['W_5/8 yield, B_y (CONTROL: a READ bilateral rotation that is not B_x)'][0]:.6f}; "
       f"{gb['distinct yields over all 24 permutations']}")
    rv = R["G_rounds_vs_N0"]
    mono = [rv[k]["rounds"] for k in (1e-2, 1e-4, 1e-8, 1e-12, 1e-17, 1e-20)]
    ok("G5 rounds before hashing pays grow as N0 falls (about log(1/N0)/log 1.2 near F = 1/2)",
       all(x < y for x, y in zip(mono, mono[1:])) and abs((mono[-1] - mono[-2]) - math.log(1e3) / math.log(1.2)) < 3,
       f"{mono}")
    for k, v in R["H_w2"].items():
        ok(f"H1 {k}: settle's law on a Bell pair reproduced through bloch_exact (import check)",
           abs(v["Bell signal"] - v["settle.bob_y_exact (imported law)"]) < 1e-9)
        ok(f"H2 {k}: the harvested pair's W2 signal is bounded by Bob's branch rho_perp, is second order in it "
           f"(<= 2 eps T rho_perp^2), and is < 1e-12 of the Bell signal",
           v["harvested signal (beta=7, lambda=0.1)"] <= v["rho_perp of Bob's branches"] * (1 + 1e-9)
           and v["signal / (2 eps T rho_perp^2)"] <= 1.0 + 1e-6
           and v["harvested signal (beta=7, lambda=0.1)"] < 1e-12 * v["Bell signal"], f"{v['signal / (2 eps T rho_perp^2)']:.4f}")
    for lab, d in R["I_timeline"].items():
        for w, tl in d.items():
            if not isinstance(tl, dict):
                continue
            m = tl["midpoint"]
            ok(f"I1 {lab} {w}: the vacuum route's floor arrives after the light time; the midpoint pair source before it",
               m["floor: one two-way exchange (R9)"] > m["light time L/c"] and m["midpoint pair source ready (D23)"] < m["light time L/c"]
               and abs(m["probes hold from (D23, imported)"] - m["light time L/c"] / 2) < 1e-9 * m["light time L/c"])
    for lab, d in R["I_window_free"].items():
        m, e1 = d["midpoint"], d["one-end"]
        lt = m["light time L/c"]
        ok(f"I3 (W2-fix) {lab}: the window-free floor (T_window -> 0, R2) is 1.50 L/c from a midpoint and 2.00 L/c from one "
           f"end -- computed from D23 (imported) -- after the light time and after the midpoint pair source (0.50 L/c)",
           abs(m["window-free floor t_hold + L/c"] / lt - 1.5) < 1e-12 and abs(e1["window-free floor t_hold + L/c"] / lt - 2.0) < 1e-12
           and m["window-free floor t_hold + L/c"] > lt > m["midpoint pair source ready (D23)"],
           f"{m['window-free floor t_hold + L/c'] / lt:.3f} / {e1['window-free floor t_hold + L/c'] / lt:.3f} L/c")
    tlr = R["I_timeline"]["1 ly"]
    wf = R["I_window_free"]["1 ly"]
    structural("I4 (a drift guard, not a control; W2-fix first labelled it 'CONTROL (must change)' and counted it): the "
       "computed families' floors are the window-free floor plus their window exactly -- Gaussian beta = 7 (window L/c) "
       "2.50 / 3.00, Reznik L/T = 1.05 (0.952 L/c) 2.45 / 2.95.  It holds by construction: timeline() and "
       "window_free_floor() use the same imported t_hold and the same t0 + tw + L/c, so it can catch a drift between "
       "the two functions but cannot fail on content",
       all(abs(tl[src]["floor: one two-way exchange (R9)"] - wf[src]["window-free floor t_hold + L/c"] - tl[src]["harvest window"])
           < 1e-9 * tl[src]["light time L/c"] and tl[src]["floor: one two-way exchange (R9)"] - wf[src]["window-free floor t_hold + L/c"]
           > 0.9 * tl[src]["light time L/c"]
           for tl in (v for v in tlr.values() if isinstance(v, dict)) for src in ("midpoint", "one-end")))
    rb = wf["midpoint"]["R2 guaranteed N >= exp(-(L/cT)^3) at cT = x L"]
    ok("I5 (W2-fix) R2 eq.(8)'s guarantee falls faster than any power as T_window -> 0: e^-1 at cT = L, e^-8 at L/2, "
       "e^-64 at L/4, e^-1000 (underflow to 0 in double) at L/10 -- the price of the window-free floor",
       abs(rb[1.0] - math.exp(-1)) < 1e-15 and abs(rb[0.5] - math.exp(-8)) < 1e-18 and abs(rb[0.25] - math.exp(-64)) < 1e-40
       and rb[0.1] < 1e-300, f"{rb}")
    structural("I2 transit.TRAVERSAL_IS_REMOVED is False (a declared board constant, read not tested)",
               R["I_board"]["transit.TRAVERSAL_IS_REMOVED"] is False)
    counted = [c for c in checks if not c[0].startswith("STRUCTURAL")]
    nctrl = sum(1 for c in counted if "CONTROL" in c[0])
    for name, passed, detail in checks:
        print(("PASS " if passed else "FAIL ") + name + (f"  [{detail}]" if detail else ""))
    npass = sum(1 for c in counted if c[1])
    print(f"\n{npass}/{len(counted)} counted checks pass ({nctrl} controls); "
          f"{len(checks) - len(counted)} STRUCTURAL items printed, not counted")
    return npass == len(counted), R


def to_jsonable(o):
    if isinstance(o, dict):
        return {str(k): to_jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [to_jsonable(v) for v in o]
    if isinstance(o, complex):
        return {"re": o.real, "im": o.imag}
    if isinstance(o, (np.floating, np.integer)):
        return o.item()
    if isinstance(o, float) and (math.isinf(o) or math.isnan(o)):
        return str(o)
    return o


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        good, _ = selftest()
        sys.exit(0 if good else 1)
    R = build()
    print(_fmt(R))
    if "--json" in sys.argv:
        with open(sys.argv[sys.argv.index("--json") + 1], "w") as fh:
            json.dump(to_jsonable(R), fh, indent=1)
