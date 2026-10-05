#!/usr/bin/env python3
"""
signdim.py -- the sign of energy by dimension (M-RULINGS items 74-78): 'Perhaps positive energy is negative energy in the
dimension it's corridor moves through' (H-SIGN-BY-DIMENSION, item 74) and '- Alcubierre was measuring was partially
right' (H-ALCUBIERRE-PARTIAL, item 75).  Item 76, 'READ, then model': the brane-world effective field equations READ at
source, then deduced (M-DEDUCE) whether a warp's negative energy on our plane can be the plane's reading of a bulk that
satisfies the null energy condition.  Item 78: the one assumption S6 named (H-SAME-CONFIGURATION) was searched for in
the literature; it is found, READ, and replaced (HISTORY).

Seated in ledger.py section 8l (M: "Seat all three, then the bulk", item 79); first written "Not seated".  Verified once (2026-10-05), findings applied (HISTORY).  M's words are carried as hypotheses, never as
results.  O9 stays OPEN.

    python3 signdim.py              report
    python3 signdim.py --selftest   checks, with CONTROLS
    python3 signdim.py --json       the numbers as JSON

SOURCES READ (2026-10-05; route: alphaXiv answer_pdf_queries on open arXiv copies, printed pages; 'verifier-READ' marks a
quote the verifier also read)
  Shiromizu, Maeda & Sasaki gr-qc/9910076v3 (SMS): the brane equations G_mn = -Lambda_4 q_mn + 8 pi G_N tau_mn +
    kappa_5^4 pi_mn - E_mn (eq. 17), with Lambda_4 = (kappa_5^2/2)(Lambda + kappa_5^2 lambda^2/6) (eq. 18), G_N =
    kappa_5^4 lambda/48 pi (eq. 19) and pi_mn quadratic in tau (eq. 20); for a perfect fluid pi_mn = (1/12) rho (rho t t +
    (rho + 2P) h) (eq. 28).  E_mn = (5)C n n q q (eq. 9): 'Note that E_mn is traceless' (p.2, verifier-READ); its
    algebraic count (n-2)(n+1)/2 (eq. A5).  The bulk is T = -Lambda g + S delta(chi) (eq. 13), Z2-symmetric (p.3).  tau is
    conserved (eq. 21) and E's divergence is fixed by the matter (eq. 22); E^TT 'corresponds to gravitational waves or
    gravitons in 5 dimensions' and 'one must solve the gravitational field in the bulk at the same time in general' (p.4,
    verifier-READ).  'we would have the wrong sign of G_N if lambda < 0' (p.3); RS1's negative-tension brane 'is an
    anti-gravity world and hence should be excluded from the physical point of view' (abstract) -- a conclusion its first
    author later withdrew (Shiromizu & Koyama, below).  Normal matter 'should satisfy the local energy condition' (p.4).
    The pi and E^L terms are of order M^4/M_lambda^4 relative to the matter term (eqs. 23-24).
  Shiromizu & Koyama hep-th/0210066v3 (SK), the same covariant formalism applied to two branes: 'For the two brane
    systems, on the other hand, we have to carefully evaluate E_mn due to the existence of the radion fields. Otherwise,
    we have a wrong prediction on the gravity on the branes' and 'we learned from the linealised theory [Garriga-Tanaka]
    that E_mn is not negligible' (p.2).  On the negative-tension brane the Gauss equation reads G = -(kappa^2/l) T_2 - E
    (eq. 31); the tensions are 1/l = kappa^2 sigma_1/6 = -kappa^2 sigma_2/6 (eq. 22); E is then fixed by both branes'
    matter and the radion d_0 (eq. 33), and the effective equation (eq. 34) has coupling kappa^2/(l Phi) to our matter,
    Phi = e^{2 d_0/l} - 1, omega(Phi) = -(3/2) Phi/(1 + Phi).  'In Ref [13], we thought that the anti-gravity appears on
    the negative tension brane supposing E_mn is negligible. However, this is not correct and E_mn is not negligible even
    at the low energy' (p.4).  'it is supposed that the visible brane where we are is the negative tension one' (p.1);
    'the scalar coupling is not permitted from the experimental point of view' without stabilisation (p.4).
  Kanno & Soda hep-th/0207029v2 (KS): 'the radion plays an essential role to convert the non-local Einstein gravity with
    the generalized dark radiation to the local quasi-scalar-tensor gravity' (abstract); omega(Psi) = 3 Psi/2(1 - Psi)
    on the positive brane and omega(Phi) = -3 Phi/2(1 + Phi) on the negative (eqs. 52, 63); the dark-radiation tensor
    chi_mn 'is now a secondary entity' fixed by both branes' matter and the radion (eq. 53, p.7); their linearised result
    'is the same as the one derived by Garriga and Tanaka' (eq. B28, p.16).
  Chiba gr-qc/0001029v2: on the negative-tension brane 'G_eff -> 0 and omega -> -3/2' as k r_c -> infinity, which 'does
    not satisfy the constraint by the solar system experiment. This does not immediately mean that the scenario of [RS1]
    is not valid because we do not include massive degrees of freedom that may give rise to a stabilizing potential'
    (p.5).
  Garriga & Tanaka hep-th/9911055v4 (GT): with two branes of opposite tension, 'linearized Brans-Dicke (BD) gravity is
    recovered on either wall' (abstract); eq. 25, the linear field on each wall; G(+-) = G_5 l^-1 e^{+-d/l} /
    (2 sinh(d/l)) (eq. 26); omega(+-) = (3/2)(e^{+-2d/l} - 1) (eq. 27); 'Observations require that omega_BD > 3000',
    achieved on the positive-tension brane 'with d/l > 4' and 'even without stabilizing the dilaton'; on the negative
    'always negative but greater than -3/2'; 'the system of two branes is well behaved in spite of the negative tension'
    (p.7, all verifier-READ).  Shadow matter enters eq. 25's first term only, so 'for the same Newtonian mass the
    deflection of light rays caused by shadow matter is 25% smaller' (p.8).  Lambda = -6 l^-2, sigma = 3/(4 pi l G_5)
    (p.2).  The extracted text of eq. 25's last term reads 'sinh(d/l) e^{+-d/l}'; with e^{+d/l} on the positive wall it
    would not reduce to GT's own Einstein limit (eq. 24, 'the familiar 1/2'), so the exponent is RECONSTRUCTED as
    e^{-+d/l} (a discrepancy in the extraction, not a refutation; check 19 tests the reconstruction against eq. 27).
  Bronnikov & Kim gr-qc/0212112 (BK): the brane vacuum obeys G_mn = -E_mn (eq. 1); 'Due to its geometric origin, E_mn
    does not necessarily satisfy the energy conditions applicable to ordinary matter. Thus, examples are known [29,
    Vollick] when negative energies on the brane are induced by gravitational waves or black strings in the bulk' (p.1);
    'E_mn can be the most natural "matter" supporting wormholes' (p.2); R = 0 traversable wormholes with rho + p_rad < 0
    (eq. 18); 'they can appear with rho > 0, but only with comparatively large negative pressures' (p.6).  They quote
    Vollick [35]: 'any 4-dimensional space-time with R = 0 gives rise to a 3-brane world without surface stresses
    embedded in a 5-dimensional space-time', and add 'a complete model requires knowledge of the full 5-dimensional
    space-time' (p.6).
  Maartens gr-qc/0312059v2: 'the covariant formalism applies also to the two-brane case. In that case, the gravitational
    influence of the second brane is felt via its contribution to E_mn' (p.11); E acts as a Weyl 'fluid' with 'pressure
    rho_E/3' (eq. 3.47); E = 0 for a conformally flat bulk, 'including AdS_5' (eq. 3.48); 'inhomogeneous density requires
    nonzero E' (eq. 3.76); 'bulk effects on the brane are also carried by F_mn, which describes any 5D fields' (p.12);
    'In general the system of equations is not closed: there is no evolution equation for the KK anisotropic stress'
    (p.19).  The bulk F(R) = K + R^2/l^2 - m/R^2 (eq. 5.2), m = kappa^2 rho_E0 a_0^4/3 (eq. 5.12); '[By Eq. (5.2), it is
    possible to avoid a naked singularity with negative m when K = -1, provided |m| <= l^2/4.]' (p.26).  A charged bulk
    black hole (5D Einstein-Maxwell, eq. 5.47) imprints 'an effective negative energy density -3q^2/(kappa^2 a^6), which
    redshifts like stiff matter (w = 1)', 'from non-vacuum stresses in the bulk via the F_mn tensor' (p.32).  The
    tidal-charge metric F = 1 - 2GM/r + 2G l Q/r^2 (eq. 4.17), Q = -2M for r << l (eq. 4.20): 'Negative Q is in accord
    with the intuitive idea that the tidal charge strengthens the gravitational field' (p.21); it 'cannot describe the
    end-state of collapse' but 'could be a good approximation in the strong-field regime for small black holes' (p.21);
    for such brane solutions 'the bulk metric for these solutions has not been found' (p.20).  5D gravitational waves can
    take 'short-cuts' through the bulk (p.26).
  Alcubierre gr-qc/0009013 and Natario gr-qc/0110086, as READ in horizon.py: the Eulerian energy density is negative
    (Alcubierre eq. 19); 'Nonflat warp drive spacetimes violate either the weak or the strong energy condition' (Natario
    Thm 1.7).
  NAMED-NOT-READ: Vollick's papers (BK refs. 29, 35); Csaki et al. and Goldberger-Wise on radion stabilisation; the
  Campbell-Magaard embedding theorem.

DEDUCTIONS (each from the premises named)
  S1 THE BULK'S READING CANNOT CARRY A WARP'S TRACE.  [SMS eq. 9; the 4D Ricci scalar of Alcubierre's metric, computed]
     E is traceless, so the trace G^m_m = -R must come from Lambda_4, tau or pi.  Alcubierre's R is not zero (computed;
     it takes both signs across the wall), so his metric is not in BK's E-alone class (R = 0) nor in Vollick's
     embedding class (BK p.6).  Brane matter that satisfies the energy conditions can carry either sign of trace
     (-4 rho <= -rho + 3P <= 2 rho for |P| <= rho), so the trace is no energy-condition obstacle.
  S2 THE BULK'S READING CAN CARRY EVERY NULL PROJECTION.  [SMS eqs. 9, 17, 21, 22, A5]  E has 9 algebraic components, G
     has 10: all but the trace.  The NEC reading G_mn k^m k^n is blind to the trace, so it is entirely open to E.
     Alcubierre's G_kk is negative (computed): his metric violates the NEC as well as the WEC.  Locally, not just at a
     point: for any conserved brane matter tau of the right trace, E defined by eq. 17 satisfies eq. 22 identically (eq.
     22 follows from eqs. 17 and 21 and the Bianchi identity).  The brane equations alone therefore do not exclude his
     metric -- 'the system of equations is not closed' (Maartens p.19).  What is not shown: such a tau that also keeps
     the energy conditions, and a bulk whose Weyl projection is that E.
  S3 A BULK THAT SATISFIES THE NULL ENERGY CONDITION CAN BE READ ON THE PLANE AS VIOLATING IT (homogeneous; READ and
     computed).  (a) A vacuum bulk (T = -Lambda g, T_kk = 0: the NEC holds, saturated; its negative vacuum energy
     violates the WEC, as RS's bulk always does) with K = -1 and -l^2/4 <= m < 0: no naked singularity (Maartens p.26;
     the horizons are computed -- the inner one is a Cauchy horizon, and a regular bulk is not claimed), and dark
     radiation rho_E proportional to m is negative, with rho_E + p_E = (4/3) rho_E < 0.  (b) A charged bulk black hole:
     the 5D Maxwell field satisfies the NEC (computed), and the plane reads -3q^2/(kappa^2 a^6) with w = 1, so
     rho + p = 2 rho < 0.  Both are homogeneous; a warp needs a local reading.
  S4 AROUND A BRANE MASS, IN THE TIDAL-CHARGE SOLUTION, THE BULK'S READING IS A NEGATIVE ENERGY.  [Maartens eqs. 4.17,
     4.20, pp.20-21; computed]  The tidal-charge metric has R = 0 and, with Q = -2M < 0, an effective energy density that
     is negative and violates the NEC tangentially (rho + p_t = 2 rho < 0, rho + p_r = 0), while it STRENGTHENS the
     attraction.  Positive mass on the plane; negative energy in its bulk reflection ('reflected back on the brane by the
     negative bulk cosmological constant', p.21).  For the assumed metric the negative energy outside r is |q|/2r =
     2 l M/r at all r; within the scope r << l of Q = -2M that exceeds M (the Misner-Sharp mass inside r is
     M + 2 l M/r).  Its bulk 'has not been found' (p.20), so the bulk is not shown to satisfy the NEC.
  S5 ON A NEGATIVE-TENSION PLANE, THE PLANE'S OWN TERM READS POSITIVE ENERGY AS NEGATIVE.  [SMS eqs. 17-20, 28; H-RS1]
     With E = 0 and a perfect fluid, G_kk = (kappa_5^4/6)(rho + P)(lambda + rho)(t.k)^2 and G_00 = (kappa_5^4/6)
     rho (lambda + rho/2) (both computed; Maartens eqs. 3.55-3.56 give the same up to the factor kappa^4 lambda/6, whose
     sign is lambda's).  For lambda < 0 (RS1's visible brane: ours under H-RS1), NEC-respecting matter is read as
     NEC-violating whenever rho < |lambda|, and its energy density as negative whenever rho < 2|lambda| -- in our units
     |V_vis| = 1.2e52 J/m^3, from crossing.py's tension.  Lambda_4 is even in lambda: the plane cannot read its
     tension's sign through its vacuum energy, only through its own term's G_N -- which S6 shows is not what it measures.
     And RS1 already places WEC-violating vacuum energy on our plane (rho = -|lambda|, rho + p = 0), which GT find 'well
     behaved': in this framework the WEC is not the obstacle; the NEC is.
  S6 THE ATTRACTION ON OUR PLANE IS THE BULK'S READING.  (a) READ: Shiromizu & Koyama -- the S of SMS -- withdraw the
     anti-gravity conclusion because 'E_mn is not negligible even at the low energy' (SK p.4): on the negative-tension
     brane G = -(kappa^2/l) T_2 - E (SK eq. 31), and E, fixed by both branes' matter and the radion (SK eq. 33), turns it
     into attractive scalar-tensor gravity (SK eq. 34; KS eq. 62), which reproduces Garriga-Tanaka (KS eq. B28).
     Maartens p.11: the second brane 'is felt via its contribution to E_mn'.  (b) Computed: the three papers agree --
     SMS eq. 19 with SK eq. 22's tension gives SK eq. 31's coefficient -kappa^2/l; SK/KS's omega(Phi), omega(Psi) equal
     GT eq. 27 on each brane; SMS eq. 18 with GT's values gives Lambda_4 = 0.  From SK eqs. 31 and 34 (hidden plane
     empty), -E = (kappa^2/l)(1 + 1/Phi) T_2 + radion terms: the bulk's reading cancels the plane's own repulsive term to
     one part in Phi = 1e30 at the board's k pi r_c and adds the radion's attraction.  (c) A sign by direction (computed
     from GT eq. 25 as reconstructed, unstabilised): on our plane a positive mass gives an attractive Newtonian potential
     (G_eff = +G_5/3l in GT's units) but a spatial curvature of the plane term's repulsive sign: gamma_PPN = -1 +
     6e-30, and light bends at 3e-30 of the Newtonian expectation.  Observation excludes this unstabilised form (GT
     'omega_BD > 3000'; Chiba p.5).  (d) A form that needs neither GT nor H-UNSTABILISED: under H-RS1 and P-ATTRACT
     (gravity on our plane is observed to attract), with SMS eq. 17 exact and pi negligible at low density (SMS eq. 23),
     the plane's own term repels (G_N < 0), so the attraction must come from the bulk terms -- E, or F from a stabilising
     bulk field (Maartens p.12) -- whatever stabilises the radion.
  S7 WHAT ALCUBIERRE MEASURED (H-ALCUBIERRE-PARTIAL).  [S1-S6; Alcubierre eq. 19; Natario Thm 1.7]  His negative rho is
     G_nn/8 pi (check 1): the plane's TOTAL reading of the metric, which no split can change.  What a 4D computation
     cannot determine is what supplies it: 4D matter, or a bulk reading (E, or F from bulk fields) of a bulk that
     satisfies the NEC.  Natario's theorem binds the reading, not the bulk.  So 'partially right' has a deduced form:
     right about the reading, silent about the source.  The reading's size is fixed by the metric: on a positive-tension
     plane E_kk must supply at least the warp's whole G_kk; on a negative-tension plane S5's term can supply part.
     Whether the bulk needs any stress-energy beyond Lambda to produce it is OPEN -- E is vacuum Weyl curvature, and BK's
     wormholes need no brane matter.  The demand is relocated; whether it is reduced is not shown.
  S8 WHAT IS NOT SHOWN.  No bulk satisfying the NEC is known that induces a warp on the plane: BK leave the embedding
     open, and E = 0 for AdS -- the bulk must carry Weyl curvature (gravitational waves or black strings, BK p.1).
     Vollick's R = 0 embedding claim (BK p.6) does not reach Alcubierre (R != 0, S1).  Whether time-delay theorems
     (pairing.py's Gao-Wald scope) constrain such a bulk is OPEN; beside them, 5D graviton 'short-cuts' through the bulk
     (Maartens p.26) are READ.

NAMED HYPOTHESES AND PREMISES
  P-ATTRACT (gravity on our plane is observed to attract); P-BD-MAP (the linearised Brans-Dicke source T - (1+omega)/
  (3+2 omega) gamma T, Will, cited by GT [10]; NAMED-NOT-READ, used only to test the eq. 25 reconstruction); P-KAPPA
  (kappa^2 = 8 pi G_5, KS eq. 3's action normalisation); H-RS1, H-K-PLANCK (carried from bulk.py); H-STABILISED and
  H-UNSTABILISED (carried; S6c needs H-UNSTABILISED, S6d does not); H-ALCUBIERRE-ILLUSTRATIVE (sigma = 8, R = 1, v_s = 1,
  geometric units); and M's H-SIGN-BY-DIMENSION, H-ALCUBIERRE-PARTIAL, H-HIGHER-CORRIDOR, H-TWO-PERSPECTIVE-TENSION.

HISTORY (verifier and item 78, 2026-10-05; first-written claims kept)
  * S6 first rested on H-SAME-CONFIGURATION ('SMS's equations and GT's linear solution describe the same two-brane RS1
    at linear order, hidden plane empty').  On M's item 78 the literature was searched: Shiromizu & Koyama derive the
    two-brane result in SMS's own formalism and withdraw SMS's anti-gravity conclusion; Kanno & Soda reproduce GT.  The
    hypothesis is retired, replaced by READ.
  * S6 first said 'the sign with which matter gravitates is set by the bulk's reading'.  Too broad, and unscoped to the
    unstabilised system: the bulk reading flips the Newtonian (time) part; the spatial part keeps the plane term's sign
    (gamma = -1) -- now S6c, scoped to H-UNSTABILISED, with S6d the stabilisation-independent form.
  * The question, S3, S8 and 'For M' said 'energy conditions' where only the NEC holds: the AdS bulk violates the WEC.
  * S2 said 'Pointwise only: E's divergence is fixed by the matter' -- eq. 22 holds identically for E defined by eq. 17
    with conserved tau; H-POINTWISE is withdrawn.
  * S7 said E 'must supply the warp's whole null curvature' and 'the source is relocated, not reduced' -- the first hid
    the sign of the plane term (S5), the second undersold that E is vacuum curvature.
  * S4 said 'the negative energy outside radius r is 2l/r of M ... on the scope r << l' -- within that scope it exceeds
    M; and the md heading dropped 'in the tidal-charge solution'.
  * S5 said 'RS1's visible plane and so ours' (now under H-RS1), and that the plane reads its sign 'only through G_N'
    (contradicted by S6).
  * BK's 'examples are known' was dropped from the quote, making it general.
  * The selftest: control 2's label named a g_tt change while the code moves the shift to y; the ghost control ran a
    different code branch (now the Maxwell branch with a spacelike vector); the omega(-) and G(+-) checks were fixed by
    their own formulas (now STRUCTURAL, replaced by cross-paper checks); the 00 crossover was unchecked (now checked).
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
    """SMS eq. 17 with E = 0 and a perfect fluid in its rest frame: returns (G_kk - (kappa^4/6)(rho + P)(lambda + rho) for
    k = (1, 1, 0, 0), G_00 - (kappa^4/6) rho (lambda + rho/2)); both should simplify to 0."""
    import sympy as sp
    rho, P, lam, kap = sp.symbols("rho P lambda kappa", real=True)
    k = sp.Matrix([1, 1, 0, 0])
    q = sp.diag(-1, 1, 1, 1)
    tau = sp.diag(rho, P, P, P)
    pi = rho * (rho * sp.diag(1, 0, 0, 0) + (rho + 2 * P) * (q + sp.diag(1, 0, 0, 0))) / 12
    GN8pi = kap ** 4 * lam / 6                                       # 8 pi G_N from eq. 19
    Lam4 = sp.Symbol("Lambda_4")
    Gmn = GN8pi * tau + kap ** 4 * pi - Lam4 * q
    Gkk = (k.T * Gmn * k)[0]
    G00 = Gmn[0, 0] + Lam4 * q[0, 0]                                 # the matter part of G_00
    return (sp.simplify(Gkk - kap ** 4 / 6 * (rho + P) * (lam + rho)),
            sp.simplify(G00 - kap ** 4 / 6 * rho * (lam + rho / 2)))


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


def sms_plane_coefficient(brane=2, kap2=1.3, ell=0.7):
    """8 pi G_N of SMS eq. 19 (= kappa^4 lambda / 6) with SK eq. 22's tension sigma_1 = 6/(kappa^2 l) or sigma_2 =
    -6/(kappa^2 l); to be compared with SK eq. 31's coefficient -kappa^2/l on the negative-tension brane."""
    sigma = (6 if brane == 1 else -6) / (kap2 * ell)
    return kap2 ** 2 * sigma / 6, -kap2 / ell


def gt_G(sign, d_over_l, ell=1.0, G5=1.0):
    """GT eq. 26: G(+-) = G_5 l^-1 e^{+-d/l} / (2 sinh(d/l))."""
    return G5 / ell * math.exp(sign * d_over_l) / (2 * math.sinh(d_over_l))


def gt_omega(sign, d_over_l):
    """GT eq. 27: omega(+-) = (3/2)(e^{+-2d/l} - 1)."""
    return 1.5 * math.expm1(sign * 2 * d_over_l)


def ks_omega(sign, d_over_l, half=False):
    """SK eqs. 34-35 / KS eqs. 52, 63: omega(Psi) = (3/2) Psi/(1 - Psi), Psi = 1 - e^{-2d/l} (positive brane);
    omega(Phi) = -(3/2) Phi/(1 + Phi), Phi = e^{2d/l} - 1 (negative brane).  half: e^{d/l} in place of e^{2d/l}."""
    x = (1 if half else 2) * d_over_l
    if sign > 0:
        psi = -math.expm1(-x)
        return 1.5 * psi / (1 - psi)
    phi = math.expm1(x)
    return -1.5 * phi / (1 + phi)


def gt_source_a(sign, d_over_l, literal=False):
    """GT eq. 25 with the hidden source absent: (1/a^2) box h = -16 pi G(+-) [T - a gamma T], a = 1/3 -+ (1/3) sinh(d/l)
    e^{x d/l}.  RECONSTRUCTED x = -+1 (the positive wall then gives GT eq. 24's 1/2); literal: x = +-1 as extracted."""
    x = sign if literal else -sign
    return 1.0 / 3.0 + sign * math.sinh(d_over_l) * math.exp(x * d_over_l) / 3.0


def linear_static(a, G=1.0):
    """Static dust (T_00 = rho, T = -rho) in (1/a^2) box h = -16 pi G (T - a gamma T): h_00 propto 2 G (1 - a), h_ii
    propto 2 G a.  Returns (G_eff = 2 G (1 - a), gamma_PPN = a/(1 - a), gamma_PPN + 1 = 1/(1 - a), light ratio =
    (h_00 + h_yy)/(2 h_00) = 1/(2(1 - a)), the light deflection relative to Einstein's for the same Newtonian mass)."""
    return {"G_eff": 2 * G * (1 - a), "gamma": a / (1 - a), "gamma_plus_1": 1 / (1 - a), "light_ratio": 0.5 / (1 - a)}


def bd_a(omega):
    """P-BD-MAP: the linearised Brans-Dicke source T - (1 + omega)/(3 + 2 omega) gamma T."""
    return (1 + omega) / (3 + 2 * omega)


def bulk_horizon(m_over_l2, K=-1):
    """Maartens eq. 5.2, F(R) = K + R^2/l^2 - m/R^2 (l = 1): the real positive roots R^2 of R^4 + K R^2 - m = 0."""
    disc = K * K + 4 * m_over_l2
    if disc < 0:
        return []
    roots = [(-K + s * math.sqrt(disc)) / 2 for s in (1, -1)]
    return [r2 for r2 in roots if r2 > 0]


def maxwell_tkk(n=2000, spacelike=False, seed=7):
    """5D Minkowski (-++++): T_ab = F_ac F_b^c - (1/4) g_ab F_cd F^cd for random F.  Returns the minimum T_kk over n
    samples, k = (1, e) with |e| = 1 (null), or k = (1/2, e) (spacelike, a control: T_kk can then be negative)."""
    rng = random.Random(seed)
    eta = [-1, 1, 1, 1, 1]
    worst = float("inf")
    for _ in range(n):
        e = [rng.gauss(0, 1) for _ in range(4)]
        nrm = math.sqrt(sum(c * c for c in e))
        k = [0.5 if spacelike else 1.0] + [c / nrm for c in e]
        kk = sum(eta[a] * k[a] ** 2 for a in range(5))
        F = [[0.0] * 5 for _ in range(5)]
        for a in range(5):
            for b in range(a + 1, 5):
                F[a][b] = rng.gauss(0, 1)
                F[b][a] = -F[a][b]
        F2 = sum(eta[a] * eta[b] * F[a][b] ** 2 for a in range(5) for b in range(5))
        vvec = [sum(F[a][c] * k[a] for a in range(5)) for c in range(5)]         # F_kc (lower c)
        val = sum(eta[c] * vvec[c] ** 2 for c in range(5)) - 0.25 * kk * F2       # T_kk
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
    nkk, n00 = sms_null_reading()
    c2, c31 = sms_plane_coefficient(2)
    c1, _ = sms_plane_coefficient(1)
    ours = linear_static(gt_source_a(-1, d_l), gt_G(-1, d_l))
    plus = linear_static(gt_source_a(+1, d_l), gt_G(+1, d_l))
    phi = math.expm1(2 * d_l)
    omega_rows = [(dd, gt_omega(-1, dd), ks_omega(-1, dd), gt_omega(+1, dd), ks_omega(+1, dd),
                   ks_omega(-1, dd, half=True)) for dd in (0.5, 2.0)]
    recon = [(dd, gt_source_a(s_, dd), bd_a(gt_omega(s_, dd)), s_) for dd in (0.5, 2.0) for s_ in (+1, -1)]
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
        "null_factor_residual": str(nkk), "g00_factor_residual": str(n00),
        "lambda4_gt": lambda4_gt(), "lambda4_gt_half": lambda4_gt(0.5), "lambda4_gt_neg": lambda4_gt(sign=-1),
        "d_over_l": d_l,
        "GN_sms_pos": sms_GN(+1), "GN_sms_neg": sms_GN(-1),
        "G_gt_pos": gt_G(+1, d_l), "G_gt_neg": gt_G(-1, d_l),
        "sms_coef_neg": c2, "sk31_coef": c31, "sms_coef_pos": c1,
        "sk_sigma_vs_gt": (6 / (8 * math.pi * 1.0 * 1.0)) / (3 / (4 * math.pi * 1.0 * 1.0)),
        "omega_rows": omega_rows, "recon_rows": recon,
        "a_plus_literal": gt_source_a(+1, d_l, literal=True), "a_plus": gt_source_a(+1, d_l),
        "shadow": linear_static(1.0 / 3.0), "einstein": linear_static(0.5),
        "ours_G_eff": ours["G_eff"], "ours_gamma_plus_1": ours["gamma_plus_1"], "ours_light_ratio": ours["light_ratio"],
        "plus_gamma": plus["gamma"],
        "minusE_coef_over_plane": (1 + phi) / phi, "minusE_excess": 1 / phi, "Phi": phi,
        "omega_pos": gt_omega(+1, d_l), "omega_neg_plus_1p5": 1.5 * math.exp(-2 * d_l),
        "omega_pos_at_4": gt_omega(+1, 4.0), "omega_pos_at_3p5": gt_omega(+1, 3.5),
        "bulk_horizon_m_m0p2": bulk_horizon(-0.2), "bulk_horizon_m_m0p3": bulk_horizon(-0.3),
        "maxwell_min_Tkk": maxwell_tkk(), "maxwell_spacelike_min_Tkk": maxwell_tkk(spacelike=True),
        "V_vis_GeV4": tv, "V_hid_own_GeV4": th,
        "crossover_J_m3": abs(tv) * crossing.GEV4_TO_J_M3,
        "crossover_TeV": abs(tv) ** 0.25 / 1e3,
        "rho_crossover_J_m3": 2 * abs(tv) * crossing.GEV4_TO_J_M3,
    }


def report():
    d = compute()
    print("signdim.py -- the sign of energy by dimension (M items 74-78), by deduction (verified once; seated 8l)\n")
    print("S1 E is traceless; Alcubierre's R = %s ranges %.2f to %.2f across the bubble (%.1f on the wall ahead): not E "
          "alone" % (d["alc_R_expr"], d["alc_R_min"], d["alc_R_max"], d["alc_R_wall"]))
    print("S2 E carries 9 of G's 10 components, every null projection among them; Alcubierre's G_kk at the equator: %s "
          "(all < 0: the NEC is violated; rho there %.3f)" % (", ".join("%.2f" % g for g in d["alc_Gkk_at_equator"]),
                                                              d["alc_rho_at_equator"]))
    print("S3 a NEC-keeping bulk read as NEC-violating: K = -1, m = -0.2 l^2 has horizons at R^2 = %s (m = -0.3 l^2: %s); "
          "5D Maxwell min T_kk = %.2e >= 0; charged bulk reads w = 1, rho + p = 2 rho < 0" % (
              ", ".join("%.3f" % x for x in d["bulk_horizon_m_m0p2"]), d["bulk_horizon_m_m0p3"] or "none",
              d["maxwell_min_Tkk"]))
    print("S4 tidal charge (Q < 0): R = %s; rho = %s; at r = 3M, |q| = 0.5 M^2: rho = %.2e, rho + p_r = %.1e, rho + p_t "
          "= %.2e (NEC violated tangentially); GR's Q > 0 gives rho = %.2e" % (
              d["tidal_R"], d["tidal_rho_expr"], d["tidal_rho"], d["tidal_rho_plus_pr"], d["tidal_rho_plus_pt"],
              d["tidal_rho_Qpos"]))
    print("S5 negative-tension plane, E = 0: G_kk = (kappa^4/6)(rho+P)(lambda+rho)(t.k)^2; ours V_vis = %.2e GeV^4: the "
          "NEC reading flips below rho = |lambda| = (%.2f TeV)^4 = %.2e J/m^3, the energy reading below %.2e J/m^3" % (
              d["V_vis_GeV4"], d["crossover_TeV"], d["crossover_J_m3"], d["rho_crossover_J_m3"]))
    print("S6 SMS's plane term on ours: %+.4f = SK eq. 31's %+.4f (kappa^2 = 1.3, l = 0.7); -E = (1 + %.1e) x the plane "
          "term's magnitude, plus the radion; unstabilised: G_eff = %+.4f G_5/l, gamma + 1 = %.1e, light at %.1e of "
          "Einstein's; omega(-) = -3/2 + %.1e (needs > %.0f)" % (
              d["sms_coef_neg"], d["sk31_coef"], d["minusE_excess"], d["ours_G_eff"], d["ours_gamma_plus_1"],
              d["ours_light_ratio"], d["omega_neg_plus_1p5"], GT_OMEGA_OBS))
    print("S7 Alcubierre's rho is G_nn/8 pi, the plane's total reading (residual %.1e): right about the reading, silent "
          "about the source; the demand is relocated, whether it is reduced is not shown" % d["alc_Gnn_vs_printed"])
    print("S8 not shown: a bulk satisfying the NEC that induces a warp on the plane (BK: embedding open)")


ZERO4 = "Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])"


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
    chk("with the shift moved to y (dy - v f dt) while the bubble moves in x, it misses (residual %.1e)" %
        d["alc_Gnn_y_shift_vs_printed"], d["alc_Gnn_y_shift_vs_printed"] > 1e-3, ctl=True)
    chk("S1: Alcubierre's 4D Ricci scalar is not zero: it ranges %.2f to %.2f across the bubble" % (
        d["alc_R_min"], d["alc_R_max"]), max(abs(d["alc_R_min"]), abs(d["alc_R_max"])) > 1.0)
    chk("the same routine gives R = %s for the tidal-charge metric, whose energy density is not zero (%.2e)" % (
        d["tidal_R"], d["tidal_rho"]), d["tidal_R"] == "0" and d["tidal_R_plus"] == "0" and abs(d["tidal_rho"]) > 1e-6,
        ctl=True)
    chk("S2: Alcubierre's G_kk is negative for all four probe null directions at the equator (%s)" %
        ", ".join("%.2f" % g for g in d["alc_Gkk_at_equator"]), all(g < 0 for g in d["alc_Gkk_at_equator"]))
    chk("S3a: Maartens' bracket (p.26) checked: F(R) = -1 + R^2/l^2 - m/R^2 has horizons for m = -0.2 l^2 (R^2 = %s)" %
        ", ".join("%.3f" % x for x in d["bulk_horizon_m_m0p2"]), len(d["bulk_horizon_m_m0p2"]) > 0)
    chk("and none for m = -0.3 l^2 (|m| > l^2/4)", len(d["bulk_horizon_m_m0p3"]) == 0, ctl=True)
    chk("S3b: a 5D Maxwell field satisfies the NEC: min T_kk over 2000 random fields and null vectors = %.2e" %
        d["maxwell_min_Tkk"], d["maxwell_min_Tkk"] >= -1e-12)
    chk("the same code with a spacelike vector finds T_kk < 0 (min %.2f)" % d["maxwell_spacelike_min_Tkk"],
        d["maxwell_spacelike_min_Tkk"] < -0.1, ctl=True)
    chk("S4: tidal charge with Q < 0: rho = %.3e < 0, rho + p_r = %.1e, rho + p_t = %.3e < 0 -- the bulk's reading "
        "violates the NEC tangentially; with Q > 0 (GR's charge) rho = %.3e > 0" % (
            d["tidal_rho"], d["tidal_rho_plus_pr"], d["tidal_rho_plus_pt"], d["tidal_rho_Qpos"]),
        d["tidal_rho"] < 0 and abs(d["tidal_rho_plus_pr"]) < 1e-12 and d["tidal_rho_plus_pt"] < 0
        and d["tidal_rho_Qpos"] > 0)
    chk("S5: SMS eq. 20 for a perfect fluid gives eq. 28 exactly (residual zero)", d["pi_eq28_residual"] == ZERO4)
    chk("with eq. 20's 1/12 replaced by 1/6 it does not", d["pi_eq28_residual_c16"] != ZERO4, ctl=True)
    chk("S5: with E = 0, G_kk = (kappa^4/6)(rho + P)(lambda + rho) and G_00 = (kappa^4/6) rho (lambda + rho/2) "
        "(residuals %s, %s)" % (d["null_factor_residual"], d["g00_factor_residual"]),
        d["null_factor_residual"] == "0" and d["g00_factor_residual"] == "0")
    chk("S6: SMS eq. 18 with GT's Lambda = -6/l^2 and sigma = 3/(4 pi l G_5) gives Lambda_4 = %.1e" % d["lambda4_gt"],
        abs(d["lambda4_gt"]) < 1e-12)
    chk("with sigma/2 it gives %.2f" % d["lambda4_gt_half"], abs(d["lambda4_gt_half"]) > 1, ctl=True)
    chk("S6: SMS eq. 19 with SK eq. 22's negative tension gives the plane term %.6f = SK eq. 31's -kappa^2/l = %.6f; SK's "
        "tension 6/(kappa^2 l) is GT's 3/(4 pi l G_5) (ratio %.6f, P-KAPPA)" % (
            d["sms_coef_neg"], d["sk31_coef"], d["sk_sigma_vs_gt"]),
        abs(d["sms_coef_neg"] - d["sk31_coef"]) < 1e-12 and abs(d["sk_sigma_vs_gt"] - 1) < 1e-12)
    chk("with the positive tension it gives %+.6f, not eq. 31's" % d["sms_coef_pos"],
        abs(d["sms_coef_pos"] - d["sk31_coef"]) > 0.1, ctl=True)
    rows = d["omega_rows"]
    chk("S6: SK/KS's omega(Phi) and omega(Psi) equal GT eq. 27 on each brane: %s" % "; ".join(
        "d/l = %.1f: (-) %.6f vs %.6f, (+) %.6f vs %.6f" % (r_[0], r_[1], r_[2], r_[3], r_[4]) for r_ in rows),
        all(abs(r_[1] - r_[2]) < 1e-12 and abs(r_[3] / r_[4] - 1) < 1e-12 for r_ in rows))
    chk("with e^{d/l} in place of e^{2d/l} omega(Phi) misses (%s)" % ", ".join("%.4f" % r_[5] for r_ in rows),
        all(abs(r_[1] - r_[5]) > 1e-3 for r_ in rows), ctl=True)
    chk("S6c: GT eq. 25 as reconstructed reproduces eq. 27 through P-BD-MAP on both walls: %s" % "; ".join(
        "%s d/l = %.1f: a = %.6f vs %.6f" % ("+" if s_ > 0 else "-", dd, av, bv) for dd, av, bv, s_ in d["recon_rows"]),
        all(abs(av - bv) < 1e-12 for dd, av, bv, s_ in d["recon_rows"]))
    chk("eq. 25 as extracted (e^{+d/l} on the positive wall) misses GT eq. 24's Einstein limit a = 1/2: a = %.2e "
        "(reconstructed: %.6f)" % (d["a_plus_literal"], d["a_plus"]),
        abs(d["a_plus_literal"] - 0.5) > 1 and abs(d["a_plus"] - 0.5) < 1e-12, ctl=True)
    chk("S6c: GT's shadow matter (eq. 25's first term only, a = 1/3) bends light at %.2f of Einstein's for the same "
        "Newtonian mass -- their '25%% smaller' (p.8)" % d["shadow"]["light_ratio"],
        abs(d["shadow"]["light_ratio"] - 0.75) < 1e-12)
    chk("Einstein's source (a = 1/2) gives %.2f" % d["einstein"]["light_ratio"],
        abs(d["einstein"]["light_ratio"] - 1.0) < 1e-12, ctl=True)
    chk("S6c: on our plane (unstabilised) the Newtonian coupling is positive, G_eff = %.6f G_5/l, while gamma_PPN = -1 + "
        "%.1e: the spatial part keeps the plane term's sign" % (d["ours_G_eff"], d["ours_gamma_plus_1"]),
        d["ours_G_eff"] > 0 and 0 < d["ours_gamma_plus_1"] < 1e-20)
    chk("S6c: GT's omega(+) at d/l = 4 is %.0f > 3000 (their 'd/l > 4')" % d["omega_pos_at_4"],
        d["omega_pos_at_4"] > GT_OMEGA_OBS)
    chk("at d/l = 3.5 omega(+) = %.0f < 3000" % d["omega_pos_at_3p5"], d["omega_pos_at_3p5"] < GT_OMEGA_OBS, ctl=True)
    structural.append("E has (n-2)(n+1)/2 = 9 algebraic components at n = 5 (SMS eq. A5); a symmetric 4D tensor has 10: "
                      "E reaches all but the trace")
    structural.append("Lambda_4 is even in lambda (%.1e for -sigma), G_N is odd" % d["lambda4_gt_neg"])
    structural.append("a vacuum Lambda bulk has T_kk = -Lambda g_kk = 0 (NEC saturated) and T_uu = Lambda < 0 (WEC "
                      "violated); dark radiation has p = rho/3 (Maartens eq. 3.47), so rho_E + p_E = (4/3) rho_E, negative "
                      "with m; the charged bulk's term is READ as w = 1, so rho + p = 2 rho < 0")
    structural.append("S4: |q|/2r = 2 l M/r for q = 2 l Q = -4 l M (G = c = 1) at all r for the assumed metric; within "
                      "r << l it exceeds M, and the Misner-Sharp mass inside r is M + 2 l M/r")
    structural.append("S6b: from SK eqs. 31 and 34 with the hidden plane empty, -E's coefficient on our matter is (1 + "
                      "Phi)/Phi = 1 + %.1e times the plane term's (Phi = %.2e): algebra on two READ equations" % (
                          d["minusE_excess"], d["Phi"]))
    structural.append("on the positive plane SMS's G_N = %.6f and GT's G(+) = %.6f agree only as d/l -> infinity (G(+) = "
                      "G_N/(1 - e^{-2d/l})); omega(-) = -3/2 + %.1e at the board's d/l; GT's signs and G(+-) are fixed "
                      "by their formulas" % (d["GN_sms_pos"], d["G_gt_pos"], d["omega_neg_plus_1p5"]))
    structural.append("S6c's magnitudes are in GT's coordinate units; only signs and ratios (gamma, the light ratio %.1e) "
                      "are used" % d["ours_light_ratio"])
    structural.append("S7: the reading's size is fixed by the metric; whether the bulk needs stress-energy beyond Lambda "
                      "to produce it is OPEN")
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
