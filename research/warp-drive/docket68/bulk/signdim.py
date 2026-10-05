#!/usr/bin/env python3
"""
signdim.py -- the sign of energy by dimension (M-RULINGS items 74-76): 'Perhaps positive energy is negative energy in the
dimension it's corridor moves through' (H-SIGN-BY-DIMENSION, item 74) and '- Alcubierre was measuring was partially
right' (H-ALCUBIERRE-PARTIAL, item 75).  Item 76, 'READ, then model': the brane-world effective field equations READ at
source, then deduced (M-DEDUCE) whether a warp's negative energy on our plane can be the plane's reading of a bulk that
satisfies the energy conditions.

Not seated; not verified.  M's words are carried as hypotheses, never as results.  O9 stays OPEN.

    python3 signdim.py              report
    python3 signdim.py --selftest   checks, with CONTROLS
    python3 signdim.py --json       the numbers as JSON

SOURCES READ (2026-10-05; route: alphaXiv answer_pdf_queries on open arXiv copies, printed pages)
  Shiromizu, Maeda & Sasaki gr-qc/9910076v3 (SMS): the brane equations G_mn = -Lambda_4 q_mn + 8 pi G_N tau_mn +
    kappa_5^4 pi_mn - E_mn (eq. 17), with Lambda_4 = (kappa_5^2/2)(Lambda + kappa_5^2 lambda^2/6) (eq. 18), G_N =
    kappa_5^4 lambda/48 pi (eq. 19) and pi_mn quadratic in tau (eq. 20); for a perfect fluid pi_mn = (1/12) rho (rho t t +
    (rho + 2P) h) (eq. 28).  E_mn = (5)C n n q q (eq. 9): 'Note that E_mn is traceless' (p.2); its algebraic count
    (n-2)(n+1)/2 (eq. A5).  The bulk is T = -Lambda g + S delta(chi) (eq. 13), Z2-symmetric (p.3).  tau is conserved
    (eq. 21) and 'E_mn is not freely specifiable but its divergence is constrained by the matter term' (eq. 22); E^TT
    'corresponds to gravitational waves or gravitons in 5 dimensions' and 'one must solve the gravitational field in the
    bulk at the same time in general' (p.4).  'we would have the wrong sign of G_N if lambda < 0' (p.3); RS1's
    negative-tension brane 'is an anti-gravity world and hence should be excluded from the physical point of view'
    (abstract).  Normal matter 'should satisfy the local energy condition' (p.4).  With E = 0, 'an inhomogeneous perfect
    fluid is rejected' (eq. 30).
  Garriga & Tanaka hep-th/9911055v4 (GT): with two branes of opposite tension, 'linearized Brans-Dicke (BD) gravity is
    recovered on either wall, with different BD parameters' (abstract); G(+-) = G_5 l^-1 e^{+-d/l} / (2 sinh(d/l))
    (eq. 26); omega(+-) = (3/2)(e^{+-2d/l} - 1) (eq. 27); 'Observations require that omega_BD > 3000', achieved on the
    positive-tension brane 'with d/l > 4' (p.7); 'In the negative tension brane, we find that the BD parameter is always
    negative but greater than -3/2', and 'the system of two branes is well behaved in spite of the negative tension in
    one of the branes' (p.7).  The bulk is AdS with Lambda = -6 l^-2 and sigma = 3/(4 pi l G_5) (p.2).
  Bronnikov & Kim gr-qc/0212112 (BK): the brane vacuum obeys G_mn = -E_mn (eq. 1); 'Due to its geometric origin, E_mn
    does not necessarily satisfy the energy conditions applicable to ordinary matter' (p.1); 'negative energies on the
    brane are induced by gravitational waves or black strings in the bulk' [their ref. 29, Vollick] (p.1); 'E_mn can be
    the most natural "matter" supporting wormholes' (p.2); R = 0 traversable wormholes with ρ + p_rad < 0 (eq. 18); 'they
    can appear with rho > 0, but only with comparatively large negative pressures' (p.6); embedding in a 5D bulk is an
    open problem (pp.2, 6).
  Maartens gr-qc/0312059v2: E acts as a Weyl 'fluid' with energy density rho_E and 'pressure rho_E/3' (eq. 3.47);
    E = 0 for a conformally flat bulk, 'including AdS_5' (eq. 3.48); 'inhomogeneous density requires nonzero E' (eq.
    3.76); 'bulk effects on the brane are also carried by F_mn, which describes any 5D fields' (p.12).  The bulk F(R) =
    K + R^2/l^2 - m/R^2 (eq. 5.2), m = kappa^2 rho_E0 a_0^4/3 (eq. 5.12); 'In order to avoid a naked singularity, we
    assume that the black hole mass is non-negative ... [By Eq. (5.2), it is possible to avoid a naked singularity with
    negative m when K = -1, provided |m| <= l^2/4.]' (p.26).  A charged bulk black hole (5D Einstein-Maxwell, eq. 5.47):
    'The field lines that terminate on the brane imprint on the brane an effective negative energy density
    -3q^2/(kappa^2 a^6), which redshifts like stiff matter (w = 1)', arising 'from non-vacuum stresses in the bulk via
    the F_mn tensor' (p.32).  The tidal-charge brane metric F = 1 - 2GM/r + 2G l Q/r^2 (eq. 4.17), 'there is no electric
    field on the brane', Q = -2M in the small-scale limit r << l (eq. 4.20); 'Negative Q is in accord with the intuitive
    idea that the tidal charge strengthens the gravitational field' (p.21); it 'cannot describe the end-state of
    collapse' (p.21).  5D gravitational waves can take 'short-cuts' through the bulk (p.26).
  Alcubierre gr-qc/0009013 and Natario gr-qc/0110086, as READ in horizon.py: the Eulerian energy density is negative
    (Alcubierre eq. 19); 'Nonflat warp drive spacetimes violate either the weak or the strong energy condition' (Natario
    Thm 1.7).
  NAMED-NOT-READ: Vollick (BK's ref. 29).

DEDUCTIONS (each from the premises named)
  S1 E CANNOT CARRY A WARP'S TRACE.  [SMS eq. 9; the 4D Ricci scalar of Alcubierre's metric, computed]  E is traceless,
     so the trace G^m_m = -R must come from Lambda_4, tau or pi.  Alcubierre's R is not zero (computed; it takes both
     signs across the wall), so his metric is not in BK's E-alone class (R = 0).  A brane matter that satisfies the
     energy conditions can carry either sign of trace (-4 rho <= -rho + 3P <= 2 rho for |P| <= rho), so the trace is no
     energy-condition obstacle -- but tau must be conserved (SMS eq. 21).
  S2 E CAN CARRY EVERY NULL PROJECTION.  [SMS eqs. 9, A5]  E has 9 algebraic components, G has 10: all but the trace.
     The NEC reading G_mn k^m k^n is blind to the trace, so it is entirely open to E.  Alcubierre's G_kk is negative
     (computed): his metric violates the NEC as well as the WEC.  Pointwise, the brane equations therefore admit his
     metric with ordinary brane matter (the trace) and a bulk Weyl reading (the null part).  Pointwise only: E's
     divergence is fixed by the matter (SMS eq. 22), and its TT part must come from solving the bulk.
  S3 A BULK THAT SATISFIES THE NEC CAN BE READ ON THE PLANE AS NEC-VIOLATING (homogeneous; READ, and computed).
     (a) A vacuum bulk (T = -Lambda g, T_kk = 0) with K = -1 and -l^2/4 <= m < 0: no naked singularity (Maartens p.26;
     the horizon is computed), and dark radiation rho_E proportional to m is negative, with rho_E + p_E = (4/3) rho_E < 0.
     (b) A charged bulk black hole: the 5D Maxwell field satisfies the NEC (computed), and the plane reads -3q^2/
     (kappa^2 a^6) with w = 1, so rho + p = 2 rho < 0.  Both are homogeneous; a warp needs a local reading.
  S4 AROUND A BRANE MASS, IN THE TIDAL-CHARGE SOLUTION, THE BULK'S READING IS A NEGATIVE ENERGY.  [Maartens eqs. 4.17,
     4.20, p.21; computed]  The
     tidal-charge metric has R = 0 and, with Q = -2M < 0, an effective energy density that is negative and violates the
     NEC in the tangential direction, while it STRENGTHENS the attraction.  Positive mass on the plane; negative energy
     in its bulk reflection ('reflected back on the brane by the negative bulk cosmological constant', p.21).  The
     negative energy outside radius r is 2l/r of M (G = c = 1), on the scope r << l and for an assumed metric form.
  S5 ON A NEGATIVE-TENSION PLANE, THE PLANE'S OWN TERM READS POSITIVE ENERGY AS NEGATIVE.  [SMS eqs. 17-20, 28]  With
     E = 0 and a perfect fluid, G_kk = (kappa_5^4/6)(rho + P)(lambda + rho)(t.k)^2 (computed; Maartens eqs. 3.55-3.56
     give the same rho_tot + p_tot).  For lambda < 0 (RS1's visible brane: ours), NEC-respecting matter is read as
     NEC-violating whenever rho < |lambda|, and its energy density as negative whenever rho < 2|lambda| -- in our units
     |V_vis| = 1.2e52 J/m^3, from crossing.py's tension.  Lambda_4 is even in lambda: the plane cannot read its
     tension's sign through its vacuum energy, only through G_N.
  S6 BUT THE ATTRACTION ON OUR PLANE IS THE BULK'S READING.  [SMS eq. 19, GT eqs. 26-27; H-SAME-CONFIGURATION]  The
     conventions agree where they should: SMS eq. 18 with GT's Lambda and sigma gives Lambda_4 = 0, and SMS's G_N = G_5/l
     equals GT's G(+) on the positive plane (computed).  On the negative plane SMS's brane term has G_N = -G_5/l < 0,
     while GT find attraction, G(-) > 0, with omega(-) = -1.5 (computed at the board's k pi r_c).  SMS eq. 17 is exact
     given its premises, so the difference is carried by E: on our plane, if RS1, the sign with which matter gravitates is
     set by the bulk's reading, not by the plane's own term.  omega(-) = -1.5 fails 'omega_BD > 3000' unless the radion is
     stabilised (H-STABILISED).
  S7 WHAT ALCUBIERRE MEASURED (H-ALCUBIERRE-PARTIAL).  [S1-S6; Alcubierre eq. 19; Natario Thm 1.7]  His negative rho is
     G_nn/8 pi (check 1): the plane's TOTAL reading of the metric, which no split can change.  What a 4D computation
     cannot determine is what supplies it: 4D matter, or a bulk reading (E, or F from bulk fields) of a bulk that
     satisfies the energy conditions.  Natario's theorem binds the reading, not the bulk.  So 'partially right' has a
     deduced form: right about the reading, silent about the source.  The magnitude stays: E_kk must supply the warp's
     G_kk -- the source is relocated, not reduced.
  S8 WHAT IS NOT SHOWN.  No bulk satisfying the NEC is known that induces a warp on the plane: BK leave the embedding
     open, SMS give no construction, and E = 0 for AdS -- the bulk must carry Weyl curvature (gravitational waves or
     black strings, BK p.1).  Whether time-delay theorems (pairing.py's Gao-Wald scope) constrain such a bulk is OPEN.

NAMED HYPOTHESES
  H-SAME-CONFIGURATION (SMS's equations and GT's linear solution describe the same two-brane RS1 at linear order, hidden
  plane empty); H-POINTWISE (S2 is algebra at a point, not a solution); H-STABILISED and H-UNSTABILISED (carried); H-RS1,
  H-K-PLANCK (carried from bulk.py); H-ALCUBIERRE-ILLUSTRATIVE (sigma = 8, R = 1, v_s = 1, geometric units); and M's
  H-SIGN-BY-DIMENSION, H-ALCUBIERRE-PARTIAL, H-HIGHER-CORRIDOR, H-TWO-PERSPECTIVE-TENSION.
"""
import contextlib
import importlib.util
import io
import json
import math
import os
import random
import sys

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


_saved = list(sys.path)
try:
    sys.path.insert(0, WD)
    with contextlib.redirect_stdout(io.StringIO()):
        bulk = _by_path("bulk_bulk", os.path.join(HERE, "bulk.py"))
        crossing = _by_path("bulk_crossing", os.path.join(HERE, "crossing.py"))
finally:
    sys.path[:] = _saved

ALC = {"sigma": 8, "R": 1, "v": 1}           # H-ALCUBIERRE-ILLUSTRATIVE, horizon.py's Figure 1 parameters
GT_OMEGA_OBS = 3000.0                         # READ, GT p.7
PROBE = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1)]


# ------------------------------------------------------------------ curvature of a 4D metric (sympy)
def curvature(g, X):
    """(Ricci tensor, Ricci scalar, Einstein tensor, inverse metric) of the metric matrix g in coordinates X."""
    import sympy as sp
    n = len(X)
    gi = sp.simplify(g.inv())
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(n, n, lambda b, c: sum(
        sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n)) for a in range(n)))
    R = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    return Ric, R, Ric - R * g / 2, gi


def alcubierre(axis=1):
    """Alcubierre's metric ds^2 = -dt^2 + (dx - v f dt)^2 + dy^2 + dz^2 with x_s = v t and f a general function of
    (x - v t, y, z); the curvature is evaluated at t = 0 and then for his tanh form.  axis = 2 moves the shift to the y
    direction (dy - v f dt) with the bubble still centred on x - v t: a control on the direction of motion."""
    import sympy as sp
    t, x, y, z, v = sp.symbols("t x y z v", real=True)
    F = sp.Function("F")
    f = F(x - v * t, y, z)
    X = [t, x, y, z]
    g = sp.zeros(4)
    g[0, 0] = -1 + v ** 2 * f ** 2
    g[0, axis] = g[axis, 0] = -v * f
    g[1, 1] = g[2, 2] = g[3, 3] = 1
    _, R, G, _ = curvature(g, X)
    nvec = [1, 0, 0, 0]
    nvec[axis] = v * f                                        # Eulerian observer: lapse 1, shift beta = -v f along axis
    Gnn = sp.simplify(sum(G[a, b] * nvec[a] * nvec[b] for a in range(4) for b in range(4)).subs(t, 0))
    Gkk = []
    for e in PROBE:                                           # k = n + e, e a unit spatial vector: null
        k = [1, v * f + e[0], e[1], e[2]]
        Gkk.append(sp.simplify(sum(G[a, b] * k[a] * k[b] for a in range(4) for b in range(4)).subs(t, 0)))
    Rs = sp.simplify(R.subs(t, 0))
    rs = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    s, Rb = ALC["sigma"], ALC["R"]
    fn = (sp.tanh(s * (rs + Rb)) - sp.tanh(s * (rs - Rb))) / (2 * sp.tanh(s * Rb))
    r_ = sp.Symbol("r", positive=True)
    fp = sp.diff(fn.subs(rs, r_), r_).subs(r_, rs)
    printed = -v ** 2 * fp ** 2 * (y ** 2 + z ** 2) / (32 * sp.pi * rs ** 2)    # Natario p.4 = Alcubierre eq. 19

    def numeric(expr):
        e = expr.subs(F(x, y, z), fn).doit().subs(v, ALC["v"])
        return sp.lambdify((x, y, z), e, "math")

    return {"R": Rs, "Gnn": Gnn, "Gkk": Gkk, "R_num": numeric(Rs), "Gnn_num": numeric(Gnn),
            "Gkk_num": [numeric(e) for e in Gkk],
            "printed_num": sp.lambdify((x, y, z), printed.subs(v, ALC["v"]), "math")}


def tidal_charge(Qe2_sign=-1):
    """Maartens eq. 4.17 in G = c = 1: ds^2 = -A dt^2 + dr^2/A + r^2 dOmega^2, A = 1 - 2M/r + q/r^2 with q = 2 l Q.
    Returns (R, rho, p_r, p_t) from G^m_n = 8 pi T^m_n, evaluated for q = Qe2_sign * |q|."""
    import sympy as sp
    t, r, th, ph = sp.symbols("t r theta phi", positive=True)
    M, qa = sp.symbols("M qa", positive=True)
    q = Qe2_sign * qa
    A = 1 - 2 * M / r + q / r ** 2
    g = sp.diag(-A, 1 / A, r ** 2, r ** 2 * sp.sin(th) ** 2)
    _, R, G, gi = curvature(g, [t, r, th, ph])
    mixed = gi * G
    rho = sp.simplify(-mixed[0, 0] / (8 * sp.pi))
    pr = sp.simplify(mixed[1, 1] / (8 * sp.pi))
    pt = sp.simplify(mixed[2, 2] / (8 * sp.pi))
    return {"R": sp.simplify(R), "rho": rho, "p_r": pr, "p_t": pt, "symbols": (r, M, qa)}


# ------------------------------------------------------------------ SMS algebra
def sms_pi_perfect_fluid(c12=None):
    """SMS eq. 20 for tau = rho t t + P h, in the rest frame (q = diag(-1,1,1,1)); returns pi_mn - eq. 28 (should be 0).
    c12 replaces eq. 20's 1/12 coefficient of tau tau_mn (a control)."""
    import sympy as sp
    rho, P = sp.symbols("rho P", real=True)
    q = sp.diag(-1, 1, 1, 1)
    tau = sp.diag(rho, P, P, P)                                   # lower indices
    tau_up = q.inv() * tau * q.inv()
    trace = sum((q.inv() * tau)[i, i] for i in range(4))           # tau = -rho + 3P
    tau2 = sum(tau[a, b] * tau_up[a, b] for a in range(4) for b in range(4))
    mix = tau * q.inv() * tau                                       # tau_ma tau^a_n
    c = sp.Rational(1, 12) if c12 is None else c12
    pi = -mix / 4 + c * trace * tau + q * tau2 / 8 - q * trace ** 2 / 24
    tt = sp.diag(1, 0, 0, 0)
    h = q + tt
    eq28 = rho * (rho * tt + (rho + 2 * P) * h) / 12
    return sp.simplify(pi - eq28)


def sms_null_reading():
    """G_kk from SMS eq. 17 with E = 0, a perfect fluid, and k = (1, 1, 0, 0) in the fluid's rest frame (t.k = -1):
    returns G_kk - (kappa^4/6)(rho + P)(lambda + rho), which should simplify to 0."""
    import sympy as sp
    rho, P, lam, kap = sp.symbols("rho P lambda kappa", real=True)
    k = sp.Matrix([1, 1, 0, 0])
    q = sp.diag(-1, 1, 1, 1)
    tau = sp.diag(rho, P, P, P)
    pi = rho * (rho * sp.diag(1, 0, 0, 0) + (rho + 2 * P) * (q + sp.diag(1, 0, 0, 0))) / 12
    GN8pi = kap ** 4 * lam / 6                                       # 8 pi G_N from eq. 19
    Lam4 = sp.Symbol("Lambda_4")
    Gmn = -Lam4 * q + GN8pi * tau + kap ** 4 * pi
    Gkk = (k.T * Gmn * k)[0]
    target = kap ** 4 / 6 * (rho + P) * (lam + rho)
    return sp.simplify(Gkk - target)


def lambda4_gt(sigma_factor=1.0, sign=1, ell=1.0, G5=1.0):
    """SMS eq. 18 in curvature units (Lambda_SMS = Lambda_GT / kappa^2): Lambda_4 = (1/2)(Lambda_GT + kappa^4 lambda^2
    /6), with GT's Lambda = -6/l^2, sigma = 3/(4 pi l G_5), kappa = 8 pi G_5."""
    kap = 8 * math.pi * G5
    sigma = sign * sigma_factor * 3 / (4 * math.pi * ell * G5)
    return 0.5 * (-6 / ell ** 2 + kap ** 2 * sigma ** 2 / 6)


def sms_GN(sign=1, ell=1.0, G5=1.0):
    """SMS eq. 19, G_N = kappa^4 lambda / 48 pi, with GT's sigma."""
    kap = 8 * math.pi * G5
    return kap ** 2 * sign * 3 / (4 * math.pi * ell * G5) / (48 * math.pi)


def gt_G(sign, d_over_l, ell=1.0, G5=1.0):
    """GT eq. 26: G(+-) = G_5 l^-1 e^{+-d/l} / (2 sinh(d/l))."""
    return G5 / ell * math.exp(sign * d_over_l) / (2 * math.sinh(d_over_l))


def gt_omega(sign, d_over_l):
    """GT eq. 27: omega(+-) = (3/2)(e^{+-2d/l} - 1)."""
    return 1.5 * math.expm1(sign * 2 * d_over_l)


def bulk_horizon(m_over_l2, K=-1):
    """Maartens eq. 5.2, F(R) = K + R^2/l^2 - m/R^2 (l = 1): the real positive roots R^2 of R^4 + K R^2 - m = 0."""
    disc = K * K + 4 * m_over_l2
    if disc < 0:
        return []
    roots = [(-K + s * math.sqrt(disc)) / 2 for s in (1, -1)]
    return [r2 for r2 in roots if r2 > 0]


def maxwell_nec(n=2000, ghost=False, seed=7):
    """5D Minkowski (-++++): T_ab = F_ac F_b^c - (1/4) g_ab F^2 for random F; T_kk = (F_kc)(F_k^c) for null k.  Returns the
    minimum T_kk / |k|^2-scale over n samples.  ghost: a scalar with the wrong-sign kinetic term, T_kk = -(k.dphi)^2."""
    rng = random.Random(seed)
    eta = [-1, 1, 1, 1, 1]
    worst = float("inf")
    for _ in range(n):
        e = [rng.gauss(0, 1) for _ in range(4)]
        nrm = math.sqrt(sum(c * c for c in e))
        k = [1.0] + [c / nrm for c in e]                          # null: -1 + 1 = 0
        if ghost:
            dphi = [rng.gauss(0, 1) for _ in range(5)]
            val = -sum(k[a] * dphi[a] for a in range(5)) ** 2
        else:
            F = [[0.0] * 5 for _ in range(5)]
            for a in range(5):
                for b in range(a + 1, 5):
                    F[a][b] = rng.gauss(0, 1)
                    F[b][a] = -F[a][b]
            vvec = [sum(F[a][c] * k[a] for a in range(5)) for c in range(5)]     # F_kc (lower c)
            val = sum(eta[c] * vvec[c] ** 2 for c in range(5))                    # F_kc F_k^c
        worst = min(worst, val)
    return worst


# ------------------------------------------------------------------ the numbers
def compute():
    import sympy as sp
    a = alcubierre()
    pts = [(-1.0, 0.3, 0.0), (1.0, 0.3, 0.0), (0.7, 0.5, 0.0), (-1.3, 0.2, 0.1)]
    gnn_res = max(abs(a["Gnn_num"](*p) / (8 * math.pi) - a["printed_num"](*p)) for p in pts)
    aw = alcubierre(axis=2)
    gnn_wrong = max(abs(aw["Gnn_num"](*p) / (8 * math.pi) - a["printed_num"](*p)) for p in pts)
    grid = [(x / 20.0 + 0.025, y / 20.0 + 0.025, 0.0) for x in range(-30, 30) for y in range(0, 30)]   # off the centre
    Rvals = [a["R_num"](*p) for p in grid]
    nec_pt = (0.0, 1.0, 0.0)
    gkk = [fn(*nec_pt) for fn in a["Gkk_num"]]
    tc = tidal_charge(-1)
    tcp = tidal_charge(+1)
    r, M, qa = tc["symbols"]
    sub = {r: 3.0, M: 1.0, qa: 0.5}
    d_l = bulk.rs_geometry()["k_pi_rc"]
    th, tv = crossing.tensions(True)
    return {
        "alc_R_expr": str(a["R"]), "alc_Gnn_expr": str(a["Gnn"]),
        "alc_Gnn_vs_printed": gnn_res, "alc_Gnn_y_shift_vs_printed": gnn_wrong,
        "alc_R_min": min(Rvals), "alc_R_max": max(Rvals), "alc_R_wall": a["R_num"](1.0, 0.0, 0.0),
        "alc_Gkk_at_equator": gkk, "alc_rho_at_equator": a["Gnn_num"](*nec_pt) / (8 * math.pi),
        "tidal_R": str(tc["R"]), "tidal_R_plus": str(tcp["R"]),
        "tidal_rho": float(tc["rho"].subs(sub)), "tidal_rho_plus_pr": float((tc["rho"] + tc["p_r"]).subs(sub)),
        "tidal_rho_plus_pt": float((tc["rho"] + tc["p_t"]).subs(sub)),
        "tidal_rho_Qpos": float(tcp["rho"].subs(sub)),
        "tidal_rho_expr": str(tc["rho"]),
        "pi_eq28_residual": str(sms_pi_perfect_fluid()), "pi_eq28_residual_c16": str(sms_pi_perfect_fluid(sp.Rational(1, 6))),
        "null_factor_residual": str(sms_null_reading()),
        "lambda4_gt": lambda4_gt(), "lambda4_gt_half": lambda4_gt(0.5), "lambda4_gt_neg": lambda4_gt(sign=-1),
        "d_over_l": d_l,
        "GN_sms_pos": sms_GN(+1), "GN_sms_neg": sms_GN(-1),
        "G_gt_pos": gt_G(+1, d_l), "G_gt_neg": gt_G(-1, d_l),
        "omega_pos": gt_omega(+1, d_l), "omega_neg": gt_omega(-1, d_l),
        "omega_pos_at_4": gt_omega(+1, 4.0), "omega_pos_at_3p5": gt_omega(+1, 3.5),
        "bulk_horizon_m_m0p2": bulk_horizon(-0.2), "bulk_horizon_m_m0p3": bulk_horizon(-0.3),
        "maxwell_min_Tkk": maxwell_nec(), "ghost_min_Tkk": maxwell_nec(ghost=True),
        "V_vis_GeV4": tv, "V_hid_own_GeV4": th,
        "crossover_J_m3": abs(tv) * crossing.GEV4_TO_J_M3,
        "crossover_TeV": abs(tv) ** 0.25 / 1e3,
        "rho_crossover_J_m3": 2 * abs(tv) * crossing.GEV4_TO_J_M3,
        "omega_neg_deficit": 1.5 * math.exp(-2 * d_l),
    }


def report():
    d = compute()
    print("signdim.py -- the sign of energy by dimension (M items 74-76), by deduction (not verified; not seated)\n")
    print("S1 E is traceless; Alcubierre's R = %s ranges %.2f to %.2f across the bubble (%.1f on the wall ahead): not E "
          "alone" % (d["alc_R_expr"], d["alc_R_min"], d["alc_R_max"], d["alc_R_wall"]))
    print("S2 E carries 9 of G's 10 components, every null projection among them; Alcubierre's G_kk at the equator: %s "
          "(all < 0: the NEC is violated; rho there %.3f)" % (", ".join("%.2f" % g for g in d["alc_Gkk_at_equator"]),
                                                              d["alc_rho_at_equator"]))
    print("S3 a NEC bulk read as NEC-violating: K = -1, m = -0.2 l^2 has horizon(s) at R^2 = %s (m = -0.3 l^2: %s); "
          "5D Maxwell min T_kk = %.2e >= 0; charged bulk reads w = 1, rho + p = 2 rho < 0" % (
              ", ".join("%.3f" % x for x in d["bulk_horizon_m_m0p2"]), d["bulk_horizon_m_m0p3"] or "none",
              d["maxwell_min_Tkk"]))
    print("S4 tidal charge (Q < 0): R = %s; rho = %s; at r = 3M, |q| = 0.5 M^2: rho = %.2e, rho + p_r = %.1e, rho + p_t "
          "= %.2e (NEC violated tangentially); GR's Q > 0 gives rho = %.2e" % (
              d["tidal_R"], d["tidal_rho_expr"], d["tidal_rho"], d["tidal_rho_plus_pr"], d["tidal_rho_plus_pt"],
              d["tidal_rho_Qpos"]))
    print("S5 negative-tension plane, E = 0: G_kk = (kappa^4/6)(rho+P)(lambda+rho)(t.k)^2 (residual %s); ours V_vis = "
          "%.2e GeV^4: the NEC reading flips below rho = |lambda| = (%.2f TeV)^4 = %.2e J/m^3; Lambda_4 is even in lambda (%.1e both signs)" % (
              d["null_factor_residual"], d["V_vis_GeV4"], d["crossover_TeV"], d["crossover_J_m3"], d["lambda4_gt_neg"]))
    print("S6 at d/l = k pi r_c = %.2f: SMS G_N = %+.6f (+), %+.6f (-); GT G(+) = %.6f, G(-) = %.2e > 0; omega(+) = %.2e, "
          "omega(-) = %.4f (needs > %.0f)" % (d["d_over_l"], d["GN_sms_pos"], d["GN_sms_neg"], d["G_gt_pos"],
                                               d["G_gt_neg"], d["omega_pos"], d["omega_neg"], GT_OMEGA_OBS))
    print("S7 Alcubierre's rho is G_nn/8 pi, the plane's total reading (residual %.1e): right about the reading, silent "
          "about the source; the magnitude is relocated, not reduced" % d["alc_Gnn_vs_printed"])
    print("S8 not shown: a bulk satisfying the NEC that induces a warp on the plane (BK: embedding open)")


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
    chk("S7: G_nn/8 pi from the Einstein tensor of Alcubierre's metric equals his eq. 19 / Natario's printed rho (max "
        "residual %.1e)" % d["alc_Gnn_vs_printed"], d["alc_Gnn_vs_printed"] < 1e-9)
    chk("with g_tt = -1 - v^2 f^2 it misses (residual %.1e)" % d["alc_Gnn_y_shift_vs_printed"],
        d["alc_Gnn_y_shift_vs_printed"] > 1e-3, ctl=True)
    chk("S1: Alcubierre's 4D Ricci scalar is not zero: it ranges %.2f to %.2f across the bubble" % (
        d["alc_R_min"], d["alc_R_max"]), max(abs(d["alc_R_min"]), abs(d["alc_R_max"])) > 1.0)
    chk("the same routine gives R = %s for the tidal-charge metric, whose energy density is not zero (%.2e)" % (
        d["tidal_R"], d["tidal_rho"]), d["tidal_R"] == "0" and d["tidal_R_plus"] == "0" and abs(d["tidal_rho"]) > 1e-6,
        ctl=True)
    chk("S2: Alcubierre's G_kk is negative for all four probe null directions at the equator (%s)" %
        ", ".join("%.2f" % g for g in d["alc_Gkk_at_equator"]), all(g < 0 for g in d["alc_Gkk_at_equator"]))
    chk("S3a: Maartens' bracket (p.26) checked: F(R) = -1 + R^2/l^2 - m/R^2 has a horizon for m = -0.2 l^2 (R^2 = %s)" %
        ", ".join("%.3f" % x for x in d["bulk_horizon_m_m0p2"]), len(d["bulk_horizon_m_m0p2"]) > 0)
    chk("and none for m = -0.3 l^2 (|m| > l^2/4)", len(d["bulk_horizon_m_m0p3"]) == 0, ctl=True)
    chk("S3b: a 5D Maxwell field satisfies the NEC: min T_kk over 2000 random fields and null vectors = %.2e" %
        d["maxwell_min_Tkk"], d["maxwell_min_Tkk"] >= -1e-12)
    chk("a wrong-sign (ghost) scalar violates it: min T_kk = %.2f" % d["ghost_min_Tkk"], d["ghost_min_Tkk"] < -0.1,
        ctl=True)
    chk("S4: tidal charge with Q < 0: rho = %.3e < 0, rho + p_r = %.1e, rho + p_t = %.3e < 0 -- the bulk's reading "
        "violates the NEC tangentially; with Q > 0 (GR's charge) rho = %.3e > 0" % (
            d["tidal_rho"], d["tidal_rho_plus_pr"], d["tidal_rho_plus_pt"], d["tidal_rho_Qpos"]),
        d["tidal_rho"] < 0 and abs(d["tidal_rho_plus_pr"]) < 1e-12 and d["tidal_rho_plus_pt"] < 0
        and d["tidal_rho_Qpos"] > 0)
    chk("S5: SMS eq. 20 for a perfect fluid gives eq. 28 exactly (residual %s)" % d["pi_eq28_residual"].replace("\n", " "),
        d["pi_eq28_residual"] == "Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])")
    chk("with eq. 20's 1/12 replaced by 1/6 it does not", "Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])"
        != d["pi_eq28_residual_c16"], ctl=True)
    chk("S5: with E = 0, G_kk = (kappa^4/6)(rho + P)(lambda + rho) for k = (1,1,0,0) (residual %s)" %
        d["null_factor_residual"], d["null_factor_residual"] == "0")
    chk("S6: SMS eq. 18 with GT's Lambda = -6/l^2 and sigma = 3/(4 pi l G_5) gives Lambda_4 = %.1e" % d["lambda4_gt"],
        abs(d["lambda4_gt"]) < 1e-12)
    chk("with sigma/2 it gives %.2f" % d["lambda4_gt_half"], abs(d["lambda4_gt_half"]) > 1, ctl=True)
    chk("S6: on the positive plane SMS's G_N = %.12f equals GT's G(+) = %.12f; on ours SMS's brane term has G_N = %.3f "
        "< 0 while GT's G(-) = %.2e > 0" % (d["GN_sms_pos"], d["G_gt_pos"], d["GN_sms_neg"], d["G_gt_neg"]),
        abs(d["GN_sms_pos"] / d["G_gt_pos"] - 1) < 1e-12 and d["GN_sms_neg"] < 0 < d["G_gt_neg"])
    chk("S6: GT's omega(+) at d/l = 4 is %.0f > 3000 (their 'd/l > 4'); omega(-) at the board's d/l = %.2f is -3/2 + %.1e, in "
        "(-3/2, 0)" % (d["omega_pos_at_4"], d["d_over_l"], d["omega_neg_deficit"]),
        d["omega_pos_at_4"] > GT_OMEGA_OBS and d["omega_neg_deficit"] > 0 and d["omega_neg"] < 0)
    chk("at d/l = 3.5 omega(+) = %.0f < 3000" % d["omega_pos_at_3p5"], d["omega_pos_at_3p5"] < GT_OMEGA_OBS, ctl=True)
    structural.append("E has (n-2)(n+1)/2 = 9 algebraic components at n = 5 (SMS eq. A5); a symmetric 4D tensor has 10: "
                      "E reaches all but the trace")
    structural.append("Lambda_4 is even in lambda (%.1e for -sigma), G_N is odd: the plane reads its tension's sign only "
                      "through G_N" % d["lambda4_gt_neg"])
    structural.append("a vacuum Lambda bulk has T_kk = -Lambda g_kk = 0: the NEC holds (saturated); dark radiation has p "
                      "= rho/3 (Maartens eq. 3.47), so rho_E + p_E = (4/3) rho_E, negative with m; the charged bulk's term "
                      "is READ as w = 1, so rho + p = 2 rho < 0")
    structural.append("S4's negative energy outside radius r is |q|/(2r) = 2 l M / r for q = 2 l Q = -4 l M (G = c = 1), "
                      "on the scope r << l of Q = -2M (Maartens eq. 4.20) and for an assumed metric form")
    structural.append("S6's sign comparison holds in GT's coordinate units on the negative plane; only the signs are used")
    structural.append("S7: the magnitude stays -- E_kk must supply the warp's G_kk; the source is relocated, not reduced")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("signdim.py: %d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute(), indent=1, default=str))
    else:
        report()
