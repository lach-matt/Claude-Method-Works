#!/usr/bin/env python3
"""
escape.py -- the four routes past bulkwarp.py's test, tested exhaustively (M-RULINGS item 80: 'a field in the bulk (the
field that would stabilise the distance between our planes is one), a faster-than-light bubble, matter that radiates,
and a thick brane ... - exhaustively test these').  READ where sources exist, deduced (M-DEDUCE), and -- where the
plane's matter problem cannot be settled by hand -- posed exactly and solved numerically.

Seated in ledger.py section 8m (M-RULINGS item 83, 2026-10-06; first written 'Not seated'); verified once, findings
applied (HISTORY at the end; first written 'not verified').  M's words are carried
as hypotheses, never as results.  O9 stays OPEN.  Item 82: the board leads with what follows its work; what is ruled out
is kept as the boundary that gives it strength.  Items 81-82: the warp's v is read as the shape's STRENGTH (Alcubierre's
v_s sets its curvature, R proportional to v_s^2) -- first written 'speed'.

WHAT FOLLOWS THE WORK (each from the sections below)
  * A SHAPE WITH R = 0 EVERYWHERE NEEDS NO MATTER ON EITHER PLANE, OURS INCLUDED (route S; ours under H-RS1).  First
    written 'a shape that does not move'.  Bronnikov-Kim's static throats have R = 0 (computed) and read on the plane as
    NEC-violating, G_kk < 0 (computed); the plane's matter tau = 0 meets the Gauss trace, conservation and the NEC
    exactly, for either sign of the tension, locally: the bulk's Weyl term carries the whole reading, the bulk holding
    only its vacuum energy.  Here the demand is removed, not relocated -- this answers signdim.py S7's OPEN question
    locally, for R = 0 shapes.  A moving irrotational shape with R = 0 would pass the same way (S2, OPEN).
  * WHAT DECIDES A MOVING SHAPE'S TOTAL IS ITS VORTICITY (route S).  For every warp of Alcubierre's and Natario's kind
    (unit lapse, flat slices, any shift N falling off faster than 1/r^2, any time dependence), R = (1/2)|curl N|^2 +
    total derivatives (computed, exact), so int R d^3x = (1/2) int |curl N|^2 >= 0 at every strength.  The integral
    statement is Santiago-Schuster-Visser's eq. 7.17 (verifier-READ); the pointwise identity for R is the board's.
    Reading int R as the plane matter's total energy uses bulkwarp W3, so holds at leading order in v; above light
    strength the result rests on the engine, and pointwise strength does appear (route B).  First written 'not its speed
    ... light speed does not enter'.
  * A FIELD IN THE BULK CAN CARRY A SHAPE ON EITHER PLANE, LOCALLY (route A; Anderson's objection carries): a field with
    a potential at every strength (A2'), a gradient-only field on the negative plane below light strength (A2), and --
    as a pointwise relaxation -- above it (A2'').  Below light strength the field's net excess Psi is positive, of the
    order of the warp's negative energy: positive energy located in the bulk, read on the plane as the warp's.  This is a
    literal instance of item 74's form (H-SIGN-BY-DIMENSION, a candidate under this second reading).
  * A THICK PLANE MUST BE POSITIVE (route D): the bulk keeps the NEC only where the warp factor bends down.
  * Ruled out, as boundary: matter keeping the NEC carrying a vortical shape on a vacuum-bulk negative-tension plane
    (bulkwarp W5), at every strength tried on the exact metric (route B); sustained radiation as a way round it (C).

    python3 escape.py                 report (coarse grid)
    python3 escape.py --selftest      checks, with CONTROLS and CONTRASTS marked (coarse grid, about 2 min)
    python3 escape.py --full          the resolution study at v = 0.1 and the strength sweep (several minutes)
    python3 escape.py --study NAME    table | controls | field | all: every number in ESCAPE.md's table and section 3,
                                      one JSON line per run (table about 1 h)
    python3 escape.py --json          the numbers as JSON

THE EXACT PROBLEM (THE ENGINE).  On a Z2 plane in a bulk whose stress near the plane is T5 (SMS eqs. 1, 2, 8, 10, 16 --
READ in signdim.py; bulkwarp.py W2), the plane's matter tau must satisfy, exactly in the warp strength v and to first
order in tau/lambda:
    conservation   nabla^nu tau_{mu nu} = -2 T5_{n mu}            (Codazzi; zero for a vacuum bulk)
    trace          tau^mu_mu = -(R + 2 kappa^2 delta T5_nn)/(8 pi G_N)   (the scalar Gauss equation)
    NEC            tau_{mu nu} k^mu k^nu >= 0 for every null k      (P-NEC-BRANE)
    localised      tau = 0 on the edge of the box                    (H-LOCALISED)
with R the 4D Ricci scalar of Alcubierre's metric in the bubble's frame (X = x - v t, cylindrical s about the axis):
ds^2 = -dt^2 + (dX + beta dt)^2 + ds^2 + s^2 dphi^2, beta = v (1 - f(r)), stationary and axisymmetric.  These are linear
in tau, so the existence of such matter is a LINEAR PROGRAM: finite volumes for the conservation law on an (X, s) grid,
the trace in every cell, the NEC on a sphere of sampled null directions, and the minimum total NEC violation
V = min sum_cells,directions w * max(0, -tau_kk) as the measure (V = 0: such matter exists on the grid; V > 0: it does
not).  Sampling the NEC is weaker than the full NEC, so V > 0 is conservative (a lower bound on the true violation).
Why the restriction to stationary, axisymmetric tau with tau_{a phi} = 0, and directions with e_phi >= 0, loses
nothing: the metric is invariant under rotation about the axis, under phi -> -phi, and (in this frame) under time
translation, and the constraints are linear with a convex measure, so averaging any feasible tau over those
symmetries (time on average, under H-BOUNDED) gives a feasible tau of no larger V; with tau_{a phi} = 0, tau_kk sees
e_phi only through e_phi^2.  Edge rows force zero face-flux into the next-in cells (stricter than a ghost-zero
condition).  The bound M = 200 max|target| on each component is named and reported (bound_active); it is reached in
none of the main runs.  bulkwarp.py's W3 predicts, for a negative-tension plane at small v, V -> N_dir * int R /
|8 pi G_N| (the Laue deficit spread over the sampled directions).  CONTROL: a conserved, localised, NEC-keeping tau with
nonzero energy (the engine's own witness: maximise int tau_nn with the NEC exact and no trace condition) has its trace
imposed as the target; the engine must return V = 0 on it, which shows a positive V is not built into the problem
(edge forcing, discretisation).  It does not settle H-GRID's continuum question.

SOURCES READ (route: alphaXiv answer_pdf_queries on open arXiv copies, printed pages)
  Goldberger & Wise hep-ph/9907447v2: the stabilising field is a bulk scalar with 'interaction terms that are localized
    to the two 3-branes' lambda (Phi^2 - v^2)^2 (eqs. 3-5, p.3); its boundary conditions at the planes (eqs. 9, 10,
    p.4) are not d_n Phi = 0; 'As long as v_h^2/M^3 and v_v^2/M^3 are small, T_s^AB can be neglected in comparison to
    the stress tensor induced by the bulk cosmological constant. It is therefore safe to ignore the influence of the
    scalar field on the background geometry for the computation of V(r_c)' (p.5; verifier-READ in full -- first
    quoted without its last five words, which carry its scope); 'It may be worthwile to work out ... the back reaction
    of the scalar field' (p.7).
  DeWolfe, Freedman, Gubser & Karch hep-th/9909134v4: A'' = -(2/3) phi'^2 - (2/3) sum sigma delta (eq. 6, p.5); 'Only
    positive tension brane configurations can be smoothed in this way. A negative tension brane effectively has negative
    energy which cannot be modeled in a conventional gravitational theory. Nevertheless a negative tension brane is
    consistent with micro-' (p.3; the sentence runs onto p.4, not READ); with an orientifold 'string theory allows one
    of these two branes to have negative tension', which 'does not introduce difficulties with negative kinetic terms or
    unboundedness of energy because it is just part of a background, not something which can be dynamically created
    anywhere in space' (p.7, READ 2026-10-06); 'it is possible to demonstrate A'' <= 0 using only the weakest of
    positive energy conditions' (p.23); jump conditions A'|jump = -(2/3) sigma(phi), phi'|jump = d sigma/d phi (eq. 7).
  Maartens gr-qc/0312059v2 (READ in signdim.py): a bulk scalar 'The junction conditions on the field imply that
    d_y phi(x, 0) = 0' and then 'matter conservation continues to hold on the brane in this simple case' (eqs. 5.60,
    5.61, pp.33-34); with null radiation in the bulk, nabla^nu T_mu nu = -2 psi u_mu, 'the brane loses (psi > 0) or gains
    (psi < 0) energy in exchange with the bulk black hole' (eqs. 5.54, 5.55, p.33).
  Seahra & Wesson gr-qc/0302015v4 (READ in bulkwarp.py): the thick Z2 brane has K = 0 on its central surface and 'cannot
    embed arbitrary spacetimes if the bulk contains only vacuum energy' (p.11).
  Santiago, Schuster & Visser 2105.03079 (verifier-READ): 'the Eulerian energy density is always the sum of a
    3-divergence plus a quantity that is negative semi-definite' (eq. 4.6, p.11); int rho d^3x = -(1/32 pi) int
    omega.omega <= 0 (eq. 7.17, p.23); zero vorticity gives int rho d^3x = 0 (eq. 7.14, p.22); irrotational warps
    (Lentz; Fell-Heisenberg; shift v = grad Phi) violate the NEC in 4D (p.28).  Since int R = -16 pi int rho, S1's
    integral statement is their eq. 7.17.

ROUTE A -- A FIELD IN THE BULK.
  A1 [P-GC; computed]  A bulk field enters the plane's matter problem only through T5_nn (the trace) and T5_n mu
     (conservation).  The NEC does not fix T5_nn's sign: a scalar with a gradient along the plane has T5_kk >= 0 for every
     null k (computed) and T5_nn < 0.
  A2 [Maartens 5.60-5.61; A1; bulkwarp W3]  A GRADIENT-ONLY bulk scalar (delta V = 0) uncoupled to the plane
     (d_n phi = 0) keeps the plane's matter conserved and adds psi = -delta T5_nn = (1/2)(d_par phi)^2 to the trace, with
     Psi = 2 l psi.  For a field static in the bubble's frame, (d_par phi)^2 = (1 - beta^2) phi_X^2 + phi_s^2: Psi >= 0
     wherever beta <= 1, so at v <= 1 everywhere.  On a negative-tension plane the Laue deficit becomes
     E = int(Psi - R)/|8 pi G_N|, so matter keeping the NEC needs int Psi >= int R at leading order: stated as
     l int psi|_plane >= |E_Alc| in SMS's units (first written 'within about one bulk curvature length l of the plane',
     an assumed profile).  Engine (coarse): the least int Psi is about twice int R at v = 0.1 and 0.5, and 2.7 x at 0.9.
  A2'' [engine; relaxation]  Above light strength beta > 1 outside the bubble and a gradient-only field's psi takes
     either sign there (its gradient is timelike in the bubble's frame: a pattern moving faster than light, made of a
     field that keeps the NEC).  First written 'above light speed a gradient-only field does not rescue the negative
     plane (engine: infeasible at v = 1.5)' -- that imposed Psi >= 0 where the physics does not.  With Psi free where
     beta > 1 the negative plane is feasible at v = 1.5 and 3 (--study field), a pointwise relaxation: whether a field
     phi realises that Psi is OPEN.  A candidate place where light strength enters (item 81).
  A2' [P-GC; Maartens 5.60-5.61]  A bulk scalar WITH A POTENTIAL needs no plane matter at all.  Since psi =
     (1/2)(d_par phi)^2 + delta V takes either sign, the choice tau = 0 (K = -a q exactly) with -2 kappa^2 delta T5_nn =
     R, i.e. Psi = R pointwise, meets the Gauss trace, conservation (d_n phi = 0) and -- trivially -- the plane's NEC, at
     every strength, locally: the warp is carried by the bulk field (through F) and the Weyl term.  The field's net
     excess is int Psi = int R > 0: positive in total, negative where R < 0 (delta V below the background there); the
     bulk's NEC holds for any potential (A1).  Below light strength, in A2 and A2', the field holds net positive Psi of
     order |E_Alc| (in units of the bulk curvature length): the warp's demand is relocated into the bulk, not reduced.
     [H-SIGN-BY-DIMENSION, under its second reading: positive energy located in the higher dimension, read on the plane
     as the warp's negative energy -- here it is genuinely the bulk's (bulkwarp W4's positive energy was the plane's).]
  A3 [Goldberger-Wise eqs. 4-5, 9-10; DFGK eq. 7]  The stabilising field itself couples to the planes (d_n Phi != 0):
     then T5_n mu = d_n Phi d_mu Phi exchanges energy with the plane and the plane's tension depends on Phi -- both are
     further freedom, not obstruction.  Whether Goldberger-Wise's own profile, with its back-reaction (neglected by its
     authors for the computation of V(r_c)), can supply A2's amount is OPEN; its stress is of order v^2/M^3 against
     the bulk's (p.5).
  A4 [deduced]  Realisability: a static Psi >= 0 is (1/2)|grad phi|^2 for some phi (an eikonal, solvable locally), and
     the bulk field then exists locally by the same analytic theorems as bulkwarp's W1 (Anderson's objection carries).

ROUTE B -- A SHAPE STRONGER THAN LIGHT SPEED (first headed 'A FASTER-THAN-LIGHT BUBBLE'; v is the shape's strength).
  B1 [computed, exact]  int R d^3x = (v^2/2) int (f_y^2 + f_z^2) > 0 at every v: the remaining terms of R are total
     derivatives (bulkwarp.py).  The trace target's sign is the same at every strength.
  B2 [flat-space identity, exact in flat space; bulkwarp W3]  For comoving localised matter int tau^mu_mu = (v^2 - 1) E:
     above light strength the integrated trace and the energy have the SAME sign, so the deficit moves: if the flat
     identity governed, a negative-tension plane would pass above light strength and a positive-tension plane would
     fail.  But the warp metric is not a small perturbation of flat space when v >= 1 (its shift reaches v), so this is
     not a result -- the engine settles it on the exact metric: the negative plane still fails; the flat-space reversal
     does not occur (first written 'nothing changes'; V / (N int R) falls from 1.1-1.2 at v = 0.1 to 0.43-0.49 at
     v = 1.5 and 0.79 at v = 3).
  B3 [engine, exact metric]  The linear program at v = 0.1 ... 3 for both tensions (--full, --study table).

ROUTE C -- MATTER THAT RADIATES.
  C1 [bulkwarp W2, pointwise]  tau^mu_mu = -R/(8 pi G_N) holds at every point, and R = 0 away from the wall: anything
     that leaves the wall must be traceless.  Massive ejecta of one kind (trace -rho + sum p < 0 for dust) are excluded;
     massless radiation and traceless mixtures keeping the NEC (dust with stiff matter, for example) can escape.  First
     written 'only massless radiation can escape'.
  C2 [computed]  For the total stress the general virial holds: d^2 I/dt^2 = 2 int tau_ii (I = int tau_00 r^2, flat
     space, conserved).  For traceless, separately conserved escaping matter int tau_ii = E, so I'' = 2E.  Radiation
     emitted with any history P(t): from the origin I_r'' = 2 E_r; from the wall at R_b, I_r'' = 2 E_r + 2 R_b P +
     R_b^2 P' (both computed), the extra terms being the exchange with the massive part.  First written 'the massive
     part obeys the ordinary virial exactly as if nothing radiated', which holds only for emission from the origin.
  C3 [energy conservation; C2]  Radiation carries positive energy away for as long as it flows; the plane's matter is
     conserved (vacuum bulk), so sustained radiation must be paid from the massive part, whose energy then falls without
     bound.  Radiation that stops leaves the long-time average unchanged.  So radiation does not evade the test unless
     something supplies energy without limit: on the plane nothing does; from the bulk only T5_n mu does (route A).
     Route C reduces to route A.
  C4 [verifier's note in bulkwarp.py]  Stresses with an r^-3 tail break Laue's identity, but keeping the NEC then needs
     rho >~ r^-3, and the energy diverges (logarithmically): not finite matter.

ROUTE S -- A SHAPE WITH R = 0, AND WHAT DECIDES A MOVING ONE (item 82).
  S1 [computed, exact]  For ds^2 = -dt^2 + (dx^i + N^i dt)^2 with any N(t, x): R = (1/2)|curl N|^2 + d_i(N_i K +
     N_j d_j N_i) - 2 d_t K, K = d_i N_i.  Hence int R d^3x = (1/2) int |curl N|^2 d^3x >= 0 at every instant, for every
     strength and every time dependence, when N and d_t N fall off faster than 1/r^2 (the surface terms then vanish;
     int K d^3x is a surface term).  Prior art: SSV eq. 7.17 is the same integral statement.  Alcubierre: |curl N|^2 =
     v^2 (f_y^2 + f_z^2), the integral bulkwarp.py found.  With bulkwarp's W2-W4 (P-LEADING, H-BOUNDED, H-LOCALISED,
     P-VACUUM-BULK): the plane's matter needs total energy int |curl N|^2/(16 pi G_N) at leading order -- positive on a
     positive-tension plane, negative (ruled out) on a negative one.
  S2 [S1; bulkwarp W3, with its premises P-LEADING, H-BOUNDED, H-LOCALISED, P-VACUUM-BULK]  An irrotational shape
     (curl N = 0) has int R = 0: the plane's matter then has zero total energy, and matter keeping the NEC with zero
     total energy vanishes (the static Laue argument), so it needs R = 0 at every point.  Irrotational warps exist in the
     literature (Lentz; Fell-Heisenberg; SSV p.28 shows they violate the NEC in 4D -- that binds the plane's reading,
     not the plane's matter).  First written NAMED-NOT-READ.  Whether a localised moving irrotational shape with R = 0
     everywhere exists is OPEN.
  S3 [Bronnikov-Kim eqs. 13, 17, p.6; computed]  The static throats: R = 0, and the plane reads them as violating the
     NEC (G_kk < 0, geometric and independent of G_N's sign; example 1: rho + p_r = -r_0/(8 pi r^3)).  With tau = 0:
     K = -a q exactly, the scalar Gauss equation reads R = 0 (met), Codazzi holds, the NEC holds -- on either sign of the
     tension.  The bulk keeps only its vacuum energy (the NEC, saturated); E = -G carries the whole reading.  Locally the
     bulk exists by the analytic theorems (bulkwarp W1; Anderson's objection carries); globally 'a complete model
     requires knowledge of the full 5-dimensional space-time' (BK p.6) -- OPEN.
  S4 [named; M's hypotheses]  In the board's terms: a throat joins two asymptotic regions with no motion of the shape;
     they are two places in one universe only if identified, which the static solution does not supply (first written
     'joins two positions').  A candidate counterpart of H-HIGHER-CORRIDOR's 'position 1, then position 2' and of
     H-NO-SPEED (nothing travels the shape: the sharper statement is that what passes is R = 0); its NEC-violating
     reading on our plane is the bulk's (H-SIGN-BY-DIMENSION, under the named reading); signals still cross it at light
     speed locally.  Candidates, not results.

ROUTE D -- A THICK BRANE.
  D1 [computed]  For ds^2 = e^{2A(y)} eta + dy^2, G_ab k^a k^b = -3 A'' for the null k = e^{-A} d_t + d_y: the bulk keeps
     the NEC only where A'' <= 0 -- DFGK's 'A'' <= 0 using only the weakest of positive energy conditions' (p.23).  A
     negative-tension plane is a minimum of the warp factor, A'' > 0: its thick version breaks the bulk's NEC.  'Only
     positive tension brane configurations can be smoothed' (DFGK p.3) -- and DFGK hold the thin negative-tension plane
     consistent as 'just part of a background' (p.7).
  D2 [D1; H-RS1]  So a thick version of our plane cannot keep the NEC: a thick brane does not rescue the negative-tension
     plane -- it moves the NEC violation from the plane's matter into the bulk.
  D3 [Seahra-Wesson p.11; P-GC]  A thick positive-tension plane has K = 0 at its centre, where the Gauss equation gives
     R = -2 kappa^2 T5_nn pointwise: its 'matter' is the bulk field's T5_nn, which the NEC leaves free (A1).  It returns
     the question to the positive-tension plane (bulkwarp W6), which the engine tests.

NAMED HYPOTHESES AND PREMISES
  P-VACUUM-BULK and its relaxations (routes A, D), P-LEADING (tau/lambda small; the strength is exact in the engine),
  H-LOCALISED, H-BOUNDED, H-ESC-ILLUSTRATIVE (sigma = 4, R = 1: a smoother wall than signdim.py's sigma = 8, for the grid),
  H-GRID (the finite-volume discretisation; the resolution, direction and box studies are its tests, the witness its
  control), P-SCIPY (scipy's HiGHS solver), the bound M (reported), H-RS1 (carried); and M's H-SIGN-BY-DIMENSION (under
  the named readings: the plane's tension sign; positive energy located in the bulk), H-ALCUBIERRE-PARTIAL,
  H-HIGHER-CORRIDOR, H-NO-SPEED.

HISTORY (verifier, 2026-10-06; first-written claims kept where they stood)
  Reproducibility: the table's finer-grid, direction, box and field numbers were run outside this file; --study now
  prints every one.  Psi >= 0 was imposed at v > 1, where a gradient-only field's psi takes either sign (A2'').  'Light
  speed does not enter' / 'the whole content of the energy test' overreached (S1 and the summary).  'A shape that does
  not move' replaced by 'R = 0'; 'joins two positions' by 'two asymptotic regions'.  'Nothing changes above light speed'
  (B2).  C1-C2 too strong.  Quotes restored (GW p.5, DFGK pp.3, 7).  Premises named (S2, A2, H-RS1).  Prior art cited
  (SSV).  Selftest labels: two 'controls' were contrasts (they evaluate the same formula on another case and cannot
  fail on their own), B1's v^2 ratio an identity (now STRUCTURAL), and 'CONTROL: ENGINE CONTROL:' doubled; a genuine
  feasibility control (the witness) was added.
"""
import json
import math
import sys
import time

SIGMA, RB = 4, 1                      # H-ESC-ILLUSTRATIVE
COARSE = (20, 10, 14)                 # (NX, NS, directions) for the selftest
FULL_GRIDS = [(20, 10), (28, 14), (40, 20)]
SPEEDS = [0.1, 0.5, 0.9, 1.5, 3.0]
BOX = 3.0
COMPS = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3)]


# ------------------------------------------------------------------ the warp metric in the bubble's frame
_SYM = {}


def _symbols():
    """Metric, inverse, Christoffels and Ricci scalar of the comoving Alcubierre metric, symbolic in v (cached)."""
    if _SYM:
        return _SYM
    import sympy as sp
    T, X, S, P = sp.symbols("t X s phi", real=True)
    v = sp.Symbol("v", positive=True)
    r = sp.sqrt(X ** 2 + S ** 2)
    f = (sp.tanh(SIGMA * (r + RB)) - sp.tanh(SIGMA * (r - RB))) / (2 * sp.tanh(SIGMA * RB))
    beta = v * (1 - f)
    crd = [T, X, S, P]
    g = sp.Matrix([[-1 + beta ** 2, beta, 0, 0], [beta, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, S ** 2]])
    gi = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], crd[c]) + sp.diff(g[d, c], crd[b])
                                         - sp.diff(g[b, c], crd[d])) for d in range(4)) / 2)
             for c in range(4)] for b in range(4)] for a in range(4)]
    Ric = sp.Matrix(4, 4, lambda b, c: sum(
        sp.diff(Gam[a][b][c], crd[a]) - sp.diff(Gam[a][b][a], crd[c])
        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(4)) for a in range(4)))
    R = sum(gi[a, b] * Ric[a, b] for a in range(4) for b in range(4))
    _SYM.update(dict(X=X, S=S, v=v, beta=beta, g=g, gi=gi, Gam=Gam, R=R))
    return _SYM


def _numeric(vv):
    import sympy as sp
    sy = _symbols()
    L = lambda e: sp.lambdify((sy["X"], sy["S"]), e.subs(sy["v"], vv), "numpy")
    return {"g": [[L(sy["g"][a, b]) for b in range(4)] for a in range(4)],
            "gi": [[L(sy["gi"][a, b]) for b in range(4)] for a in range(4)],
            "Gam": [[[L(sy["Gam"][a][b][c]) for c in range(4)] for b in range(4)] for a in range(4)],
            "R": L(sy["R"]), "beta": L(sy["beta"])}


def int_R(vv, NX=400, NS=200):
    """int R d^3x on the comoving t = const slice (axisymmetric Simpson, box [-BOX, BOX] x [0, BOX])."""
    import numpy as np
    R = _numeric(vv)["R"]
    xs = np.linspace(-BOX, BOX, NX + 1)
    ss = np.linspace(1e-7, BOX, NS + 1)
    XX, SS = np.meshgrid(xs, ss, indexing="ij")
    w = lambda n: np.array([1 if i in (0, n) else (4 if i % 2 else 2) for i in range(n + 1)])
    W = np.outer(w(NX), w(NS))
    val = R(XX, SS) * np.ones_like(XX)
    return float((W * val * 2 * math.pi * SS).sum() * (xs[1] - xs[0]) * (ss[1] - ss[0]) / 9)


# ------------------------------------------------------------------ the engine: a linear program for the plane's matter
def engine(vv, sign, NX=COARSE[0], NS=COARSE[1], ndir=COARSE[2], field=False, minimise_field=False, box=None,
           signed_field=False, target=None, bound=None, witness=False):
    """Minimum total NEC violation V of conserved, localised plane matter with the Gauss trace, on the exact comoving
    warp metric at strength vv; sign = sign of 8 pi G_N (the tension), |8 pi G_N| = 1.  field: a gradient-only bulk
    scalar uncoupled to the plane adds Psi to the trace (route A), Psi >= 0 where the frame's g^XX = 1 - beta^2 >= 0;
    signed_field: Psi free in sign where beta > 1 (a static gradient-only field's psi = (1/2)[(1 - beta^2) phi_X^2 +
    phi_s^2] takes either sign there -- a pointwise relaxation: infeasible rules out, feasible is necessary only).
    minimise_field: require V = 0 and minimise int Psi (int |Psi| when signed) instead.  box: the half-width (default BOX).  target: replace the
    trace target -sign R by this array (the feasibility control).  bound: the box bound M on each tau component
    (default 200 max|target|, named; whether it is reached is reported as bound_active).  witness: no trace condition,
    the NEC exact, maximise the matter's energy int tau_nn -- returns its trace (the control's known feasible target).
    Returns dict(V, V_theory_neg, int_R, int_Psi, status, bound_active)."""
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix
    B = BOX if box is None else box
    nm = _numeric(vv)
    Xe = np.linspace(-B, B, NX + 1)
    Se = np.linspace(0, B, NS + 1)
    xs, ss = (Xe[:-1] + Xe[1:]) / 2, (Se[:-1] + Se[1:]) / 2
    dX, dS = Xe[1] - Xe[0], Se[1] - Se[0]
    XX, SS = np.meshgrid(xs, ss, indexing="ij")
    one = np.ones_like(XX)
    gi = [[nm["gi"][a][b](XX, SS) * one for b in range(4)] for a in range(4)]
    Gm = [[[nm["Gam"][a][b][c](XX, SS) * one for c in range(4)] for b in range(4)] for a in range(4)]
    Rn = nm["R"](XX, SS) * one
    bet = nm["beta"](XX, SS) * one
    nc = NX * NS
    cell = lambda i, j: i * NS + j
    edge = np.zeros((NX, NS), bool)
    edge[0, :] = edge[-1, :] = True
    edge[:, -1] = True
    k_ = np.arange(ndir) + 0.5
    th = np.arccos(1 - 2 * k_ / ndir)
    ph = math.pi * (1 + 5 ** 0.5) * k_
    dirs = np.stack([np.cos(th), np.sin(th) * np.cos(ph), np.abs(np.sin(th) * np.sin(ph))], 1)
    nt = 7 * nc
    npsi = nc if field else 0
    nu = ndir * nc
    naux = nc if (field and signed_field and minimise_field) else 0      # |Psi| for the L1 measure
    nv = nt + npsi + nu + naux
    tid = lambda c, i, j: c * nc + cell(i, j)
    pid = lambda i, j: nt + cell(i, j)
    uid = lambda d, i, j: nt + npsi + d * nc + cell(i, j)

    def tcomp(a, b):
        key = (min(a, b), max(a, b))
        return COMPS.index(key) if key in COMPS else None

    def mixed(m, n):
        out = {}
        for a in range(4):
            c = tcomp(a, n)
            if c is not None:
                out[c] = out.get(c, 0) + gi[m][a]
        return out

    rows, cols, vals = [], [], []
    beq = np.zeros(4 * nc)
    for n in range(3):
        mX, mS = mixed(1, n), mixed(2, n)
        gm = {}
        for l in range(4):
            for m in range(4):
                for a in range(4):
                    c = tcomp(a, l)
                    if c is not None:
                        gm[c] = gm.get(c, 0) + Gm[l][m][n] * gi[m][a]
        for i in range(NX):
            for j in range(NS):
                r_ = n * nc + cell(i, j)
                s = ss[j]
                sp_, sm_ = s + dS / 2, s - dS / 2
                for c, co in mX.items():
                    if i + 1 < NX:
                        rows.append(r_), cols.append(tid(c, i + 1, j)), vals.append(0.5 * s * co[i + 1, j] * dS)
                    if i - 1 >= 0:
                        rows.append(r_), cols.append(tid(c, i - 1, j)), vals.append(-0.5 * s * co[i - 1, j] * dS)
                for c, co in mS.items():
                    rows.append(r_), cols.append(tid(c, i, j)), vals.append(0.5 * (sp_ - max(sm_, 0.0)) * co[i, j] * dX)
                    if j + 1 < NS:
                        rows.append(r_), cols.append(tid(c, i, j + 1)), vals.append(0.5 * sp_ * co[i, j + 1] * dX)
                    if j - 1 >= 0:
                        rows.append(r_), cols.append(tid(c, i, j - 1)), vals.append(-0.5 * sm_ * co[i, j - 1] * dX)
                for c, co in gm.items():
                    rows.append(r_), cols.append(tid(c, i, j)), vals.append(-s * co[i, j] * dX * dS)
    if target is None:
        target = -sign * Rn                                   # tau_tr = -R/(8 pi G_N)
    for i in range(NX):
        for j in range(NS):
            if witness:                                       # no trace condition
                continue
            r_ = 3 * nc + cell(i, j)
            for c, (a, b) in enumerate(COMPS):
                rows.append(r_), cols.append(tid(c, i, j)), vals.append(gi[a][b][i, j] * (1 if a == b else 2))
            if field:                                         # tau_tr = -(R - Psi)/(8 pi G_N)
                rows.append(r_), cols.append(pid(i, j)), vals.append(-sign)
            beq[r_] = 0.0 if edge[i, j] else target[i, j]
    Aeq = coo_matrix((vals, (rows, cols)), shape=(4 * nc, nv)).tocsr()
    rows, cols, vals = [], [], []
    for d, (eX, eS, eP) in enumerate(dirs):
        for i in range(NX):
            for j in range(NS):
                kk = (1.0, -bet[i, j] + eX, eS, eP / ss[j])
                r_ = d * nc + cell(i, j)
                for c, (a, b) in enumerate(COMPS):
                    rows.append(r_), cols.append(tid(c, i, j)), vals.append(-kk[a] * kk[b] * (1 if a == b else 2))
                rows.append(r_), cols.append(uid(d, i, j)), vals.append(-1.0)
    for q in range(naux):                                     # Psi - a <= 0, -Psi - a <= 0
        rows += [nu + 2 * q, nu + 2 * q, nu + 2 * q + 1, nu + 2 * q + 1]
        cols += [nt + q, nt + npsi + nu + q, nt + q, nt + npsi + nu + q]
        vals += [1.0, -1.0, -1.0, -1.0]
    Aub = coo_matrix((vals, (rows, cols)), shape=(nu + 2 * naux, nv)).tocsr()
    bub = np.zeros(nu + 2 * naux)
    wcell = 2 * math.pi * SS * dX * dS
    cobj = np.zeros(nv)
    M = bound if bound is not None else 200 * max(np.abs(target).max(), 1e-12)
    bounds = [(-M, M)] * nt + [(0, None)] * npsi + [(0, None)] * nu + [(0, None)] * naux
    for i in range(NX):
        for j in range(NS):
            if field and signed_field and bet[i, j] > 1:
                bounds[pid(i, j)] = (None, None)
            if edge[i, j]:
                for c in range(7):
                    bounds[tid(c, i, j)] = (0, 0)
                if field:
                    bounds[pid(i, j)] = (0, 0)
    if witness:                                               # maximise int tau_nn, n = (1, -beta, 0, 0); NEC exact
        nvec = (np.ones_like(bet), -bet, 0 * bet, 0 * bet)
        for c, (a, b) in enumerate(COMPS):
            co = -(nvec[a] * nvec[b] * (1 if a == b else 2) * wcell).ravel()
            for q in range(nc):
                cobj[c * nc + q] = co[q]
        for q in range(nu):
            bounds[nt + npsi + q] = (0, 0)
    elif minimise_field:
        for i in range(NX):
            for j in range(NS):
                cobj[(nt + npsi + nu + cell(i, j)) if naux else pid(i, j)] = wcell[i, j]
        for q in range(nu):
            bounds[nt + npsi + q] = (0, 0)
    else:
        for d in range(ndir):
            for i in range(NX):
                for j in range(NS):
                    cobj[uid(d, i, j)] = wcell[i, j]
    res = linprog(cobj, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
    IR = float((Rn * wcell).sum())
    out = {"status": int(res.status), "int_R": IR, "V_theory_neg": ndir * IR, "grid": (NX, NS, ndir), "v": vv,
           "sign": sign, "box": B}
    if res.status == 0:
        x = res.x
        out["V"] = float((x[nt + npsi:nt + npsi + nu] * np.tile(wcell.ravel(), ndir)).sum())
        out["bound_active"] = bool(np.abs(x[:nt]).max() >= 0.999 * M)
        if field:
            out["int_Psi"] = float((x[nt:nt + npsi] * wcell.ravel()).sum())
            out["int_Psi_neg"] = float((np.minimum(x[nt:nt + npsi], 0) * wcell.ravel()).sum())
            out["int_abs_Psi"] = float((np.abs(x[nt:nt + npsi]) * wcell.ravel()).sum())
        if witness:
            tau = x[:nt].reshape(7, NX, NS)
            out["energy"] = -float(res.fun)
            out["trace"] = sum(gi[a][b] * tau[c] * (1 if a == b else 2) for c, (a, b) in enumerate(COMPS))
    return out


# ------------------------------------------------------------------ routes A, C, D by hand (sympy)
def scalar_nec_tnn(n=2000, seed=11):
    """5D Minkowski: a scalar with gradient (dphi) and T_ab = d_a phi d_b phi - g_ab ((1/2)(dphi)^2 + V).  Returns
    (min over random null k of T_kk, T_nn for a gradient along the plane only, with V = 0)."""
    import random
    rng = random.Random(seed)
    eta = [-1, 1, 1, 1, 1]
    worst = float("inf")
    for _ in range(n):
        e = [rng.gauss(0, 1) for _ in range(4)]
        nrm = math.sqrt(sum(c * c for c in e))
        k = [1.0] + [c / nrm for c in e]
        dphi = [rng.gauss(0, 1) for _ in range(5)]
        worst = min(worst, sum(k[a] * dphi[a] for a in range(5)) ** 2)    # the g_kk term is zero
    dphi = [0.0, 0.7, 0.2, 0.0, 0.0]                                       # gradient along the plane; index 4 = n
    sq = sum(eta[a] * dphi[a] ** 2 for a in range(5))
    tnn = dphi[4] ** 2 - 0.5 * sq
    return worst, tnn


def radiation_moment():
    """Radiation emitted with arbitrary power P(t') moves out at r = R_b + t - t'.  I_r(t) = int P(t') (R_b + t - t')^2
    dt'.  Returns: I_r'' - 2 E_r from the origin (R_b = 0; zero); I_r'' - 2 E_r - 2 R_b P - R_b^2 P' from the wall
    (zero: emission from the wall adds the source terms 2 R_b P + R_b^2 P'); and, for a control, the origin case with
    massive ejecta at speed u = 1/2 (r = u (t - t'): I'' - 2 u^2 E, not 2 E)."""
    import sympy as sp
    t, tp, t0 = sp.symbols("t t' t_0", real=True)
    Rb = sp.Symbol("R_b", positive=True)
    P = sp.Function("P")
    E = sp.Integral(P(tp), (tp, t0, t))
    I = sp.Integral(P(tp) * (t - tp) ** 2, (tp, t0, t))
    rad = sp.simplify(sp.diff(I, t, 2).doit() - 2 * E.doit())
    Iw = sp.Integral(P(tp) * (Rb + t - tp) ** 2, (tp, t0, t))
    wall = sp.simplify(sp.diff(Iw, t, 2).doit() - 2 * E.doit() - 2 * Rb * P(t) - Rb ** 2 * sp.diff(P(t), t))
    u = sp.Rational(1, 2)
    Iu = sp.Integral(P(tp) * (u * (t - tp)) ** 2, (tp, t0, t))
    mass = sp.simplify(sp.diff(Iu, t, 2).doit() - 2 * E.doit())
    return rad, wall, mass


def thick_nec(minimum=False):
    """ds^2 = e^{2A(y)}(-dt^2 + dx^2 + ...) + dy^2: G_ab k^a k^b for k = e^{-A} d_t + d_y, symbolic, and its value at a
    warp maximum (A = -|y| smoothed: A = -log cosh y) or a minimum (A = +log cosh y)."""
    import sympy as sp
    t, x1, x2, x3, y = sp.symbols("t x1 x2 x3 y", real=True)
    A = sp.Function("A")(y)
    X = [t, x1, x2, x3, y]
    g = sp.diag(-sp.exp(2 * A), sp.exp(2 * A), sp.exp(2 * A), sp.exp(2 * A), 1)
    gi = g.inv()
    n = 5
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(n, n, lambda b, c: sum(
        sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n)) for a in range(n)))
    k = [sp.exp(-A), 0, 0, 0, 1]
    Gkk = sp.simplify(sum(Ric[a, b] * k[a] * k[b] for a in range(n) for b in range(n)))   # g_kk = 0
    ratio = sp.simplify(Gkk / sp.diff(A, y, 2))
    prof = (1 if minimum else -1) * sp.log(sp.cosh(y))
    at0 = sp.simplify(Gkk.subs(A, prof).doit().subs(y, 0))
    return ratio, float(at0)


def vorticity_identity():
    """R - (1/2)|curl N|^2 - d_i(N_i K + N_j d_j N_i) + 2 d_t K for a general shift N(t, x) (zero), and the same without
    the -2 d_t K term (a control)."""
    import importlib.util, os
    import sympy as sp
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location("bulk_signdim_esc", os.path.join(here, "signdim.py"))
    sd = importlib.util.module_from_spec(spec)
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(sd)
    t, x, y, z = sp.symbols("t x y z", real=True)
    X = [t, x, y, z]
    N = [sp.Function("N%d" % i)(t, x, y, z) for i in range(3)]
    g = sp.zeros(4)
    g[0, 0] = -1 + sum(n ** 2 for n in N)
    for i in range(3):
        g[0, i + 1] = g[i + 1, 0] = N[i]
        g[i + 1, i + 1] = 1
    _, R, _, _ = sd.curvature(g, X)
    sx = [x, y, z]
    K = sum(sp.diff(N[i], sx[i]) for i in range(3))
    curl = [sp.diff(N[2], y) - sp.diff(N[1], z), sp.diff(N[0], z) - sp.diff(N[2], x), sp.diff(N[1], x) - sp.diff(N[0], y)]
    div = sum(sp.diff(N[i] * K + sum(N[j] * sp.diff(N[i], sx[j]) for j in range(3)), sx[i]) for i in range(3))
    base = sp.expand(R - sum(c ** 2 for c in curl) / 2 - div)
    return sp.simplify(base + 2 * sp.diff(K, t)), sp.simplify(base)


def bk_throats():
    """Bronnikov-Kim's static throats (eqs. 13 and 17): (R, rho + p_r) for each, symbolic."""
    import sympy as sp
    t, r, th, ph = sp.symbols("t r theta phi", positive=True)
    r0, m = sp.symbols("r_0 m", positive=True)
    out = []
    for gtt, grr in ((-1, 1 / (1 - r0 / r)),
                     (-(1 - 2 * m / r), (1 - sp.Rational(3, 2) * m / r) / ((1 - 2 * m / r) * (1 - r0 / r)))):
        g = sp.diag(gtt, grr, r ** 2, r ** 2 * sp.sin(th) ** 2)
        X = [t, r, th, ph]
        gi = g.inv()
        n = 4
        Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                     for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
        Ric = sp.Matrix(n, n, lambda b, c: sum(
            sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
            + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n)) for a in range(n)))
        R = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
        G = Ric - R * g / 2
        mixed = gi * G
        rho = -mixed[0, 0] / (8 * sp.pi)
        pr = mixed[1, 1] / (8 * sp.pi)
        out.append((sp.simplify(R), sp.simplify(rho + pr)))
    return out


def compute(full=False):
    import sympy as sp
    t0 = time.time()
    d = {}
    d["int_R_by_v"] = dict((vv, int_R(vv)) for vv in (0.1, 1.0, 3.0))
    worst, tnn = scalar_nec_tnn()
    d["scalar_min_Tkk"], d["scalar_Tnn"] = worst, tnn
    rad, wall, mass = radiation_moment()
    d["radiation_residual"], d["radiation_wall_residual"], d["ejecta_residual"] = str(rad), str(wall), str(mass)
    ratio, at_max = thick_nec()
    _, at_min = thick_nec(minimum=True)
    d["thick_Gkk_over_App"], d["thick_Gkk_at_max"], d["thick_Gkk_at_min"] = str(ratio), at_max, at_min
    grids = FULL_GRIDS if full else [COARSE[:2]]
    d["resolution"] = []
    for NX, NS in grids:
        for sign in (1, -1):
            d["resolution"].append(engine(0.1, sign, NX, NS))
    speeds = SPEEDS if full else [0.1, 1.5]
    d["speeds"] = []
    for vv in speeds:
        for sign in (1, -1):
            d["speeds"].append(engine(vv, sign))
    d["field_neg"] = engine(0.1, -1, field=True, minimise_field=True)
    d["field_neg_fast"] = engine(1.5, -1, field=True, minimise_field=True)                    # Psi >= 0 imposed
    d["field_neg_fast_signed"] = engine(1.5, -1, field=True, minimise_field=True, signed_field=True)
    wit = engine(0.5, 1, witness=True, bound=1.0)                    # a known conserved NEC-keeping tau, nonzero trace
    d["witness"] = {"status": wit["status"], "energy": wit.get("energy"),
                    "trace_min": float(wit["trace"].min()), "trace_max": float(wit["trace"].max())}
    d["witness_control"] = [engine(0.5, s, target=wit["trace"], bound=1.0) for s in (1, -1)]
    vi, vi_ctl = vorticity_identity()
    d["vorticity_residual"], d["vorticity_residual_no_dt"] = str(vi), ("0" if vi_ctl == 0 else "nonzero")
    bk = bk_throats()
    d["bk_R"] = [str(a) for a, _ in bk]
    d["bk_nec_ex1"] = str(bk[0][1])
    d["seconds"] = time.time() - t0
    return d


def _row(e):
    return "v = %.1f, %s tension, grid %s: V = %s (Laue deficit N_dir int R = %.3e)" % (
        e["v"], "positive" if e["sign"] > 0 else "negative", "x".join(map(str, e["grid"][:2])),
        ("%.3e" % e["V"]) if "V" in e else "status %d" % e["status"], e["V_theory_neg"])


def report(full=False):
    d = compute(full)
    print("escape.py -- the four routes past bulkwarp.py's test (M item 80), by deduction and computation "
          "(verified once; seated 8m)\n")
    print("THE ENGINE (exact warp metric, linear program for the plane's matter):")
    for e in d["resolution"]:
        print("  " + _row(e))
    print("B (strength):")
    for e in d["speeds"]:
        print("  " + _row(e))
    fnf, fns = d["field_neg_fast"], d["field_neg_fast_signed"]
    print("A (gradient-only bulk scalar, negative plane): least int Psi = %.3e against int R = %.3e (v = 0.1); at v = 1.5 "
          "with Psi >= 0 imposed: status %d; with Psi free where beta > 1 (relaxation): status %d, net int Psi = %.3e, "
          "int |Psi| = %.3e" % (d["field_neg"].get("int_Psi", float("nan")), d["field_neg"]["int_R"], fnf["status"],
                                fns["status"], fns.get("int_Psi", float("nan")), fns.get("int_abs_Psi", float("nan"))))
    print("A1 a scalar keeps the bulk NEC (min T_kk = %.2e) with T_nn = %.3f < 0" % (d["scalar_min_Tkk"], d["scalar_Tnn"]))
    print("C2 radiation: I'' - 2E = %s from the origin; I'' - 2E - 2 R_b P - R_b^2 P' = %s from the wall (massive ejecta "
          "at u = 1/2: %s)" % (d["radiation_residual"], d["radiation_wall_residual"], d["ejecta_residual"]))
    print("D1 thick plane: G_kk/A'' = %s; at a warp maximum %.2f (keeps the NEC), at a minimum %.2f (breaks it)" % (
        d["thick_Gkk_over_App"], d["thick_Gkk_at_max"], d["thick_Gkk_at_min"]))
    print("B1 int R by v: %s" % ", ".join("v = %.1f: %.4e" % kv for kv in d["int_R_by_v"].items()))
    print("feasibility control (v = 0.5): witness energy %.3e, trace in [%.3f, %.3f]; engine V on its trace: %s" % (
        d["witness"]["energy"], d["witness"]["trace_min"], d["witness"]["trace_max"],
        ", ".join("%.2e" % e.get("V", float("nan")) for e in d["witness_control"])))
    print("(%.0f s)" % d["seconds"])


def selftest():
    n_pass = n_fail = n_ctl = n_con = 0
    structural = []

    def chk(label, ok, ctl=False, contrast=False):
        nonlocal n_pass, n_fail, n_ctl, n_con
        n_ctl += ctl
        n_con += contrast
        n_pass += bool(ok)
        n_fail += (not ok)
        print("  %s %s%s" % ("ok  " if ok else "FAIL", "CONTROL: " if ctl else ("CONTRAST: " if contrast else ""), label))

    d = compute(False)
    pos = [e for e in d["resolution"] if e["sign"] > 0][0]
    neg = [e for e in d["resolution"] if e["sign"] < 0][0]
    chk("ENGINE: at v = 0.1 on the coarse grid the negative-tension plane's least NEC violation (%.3e) is at least the "
        "Laue deficit bulkwarp.py's W3 predicts, N_dir int R = %.3e (ratio %.2f)" % (
            neg["V"], neg["V_theory_neg"], neg["V"] / neg["V_theory_neg"]), neg["V"] >= 0.95 * neg["V_theory_neg"])
    chk("ENGINE: the positive plane's violation (%.3e) is below half that deficit (%.2f of it): no Laue deficit "
        "(its residue is H-GRID's question)" % (pos["V"], pos["V"] / neg["V_theory_neg"]),
        pos["V"] < 0.5 * neg["V_theory_neg"], contrast=True)
    chk("ENGINE: the negative plane violates more than three times as much as the positive (%.1f x)" % (
        neg["V"] / pos["V"]), neg["V"] > 3 * pos["V"], contrast=True)
    wc = d["witness_control"]
    chk("ENGINE: a known conserved, localised, NEC-keeping tau (the engine's own witness, energy %.3e, trace in "
        "[%.2f, %.2f]) imposed as the trace target gives V = %s on both tensions -- the engine returns zero when matter "
        "exists, so a positive V is not built into the problem" % (
            d["witness"]["energy"], d["witness"]["trace_min"], d["witness"]["trace_max"],
            " and ".join("%.1e" % e.get("V", float("nan")) for e in wc)),
        d["witness"]["status"] == 0 and d["witness"]["energy"] > 0 and d["witness"]["trace_min"] < 0 <
        d["witness"]["trace_max"] and all(e["status"] == 0 and e["V"] < 1e-6 for e in wc), ctl=True)
    fn = d["field_neg"]
    chk("A2: with a gradient-only bulk scalar the negative plane's matter keeps the NEC (V forced to 0, solved: status "
        "%d) with int Psi = %.3e >= int R = %.3e" % (fn["status"], fn.get("int_Psi", float("nan")), fn["int_R"]),
        fn["status"] == 0 and fn["int_Psi"] >= 0.999 * fn["int_R"])
    chk("A1: a bulk scalar keeps the NEC (min T_kk over 2000 random null vectors and gradients = %.2e) while T_nn = %.3f "
        "< 0 for a gradient along the plane" % (d["scalar_min_Tkk"], d["scalar_Tnn"]),
        d["scalar_min_Tkk"] >= 0 and d["scalar_Tnn"] < 0)
    chk("C2: radiation emitted from the origin with ANY history P(t) has I_r'' = 2 E_r (residual %s); from the wall at "
        "R_b, I_r'' = 2 E_r + 2 R_b P + R_b^2 P' (residual %s)" % (d["radiation_residual"], d["radiation_wall_residual"]),
        d["radiation_residual"] == "0" and d["radiation_wall_residual"] == "0")
    chk("massive ejecta at u = 1/2 do not (residual %s)" % d["ejecta_residual"], d["ejecta_residual"] != "0", ctl=True)
    chk("D1: G_kk = %s x A'' for the thick plane's null vector; a warp maximum keeps the NEC (%.2f >= 0)" % (
        d["thick_Gkk_over_App"], d["thick_Gkk_at_max"]), d["thick_Gkk_over_App"] == "-3" and d["thick_Gkk_at_max"] > 0)
    chk("a warp minimum (a negative-tension plane, thickened) breaks it (%.2f < 0)" % d["thick_Gkk_at_min"],
        d["thick_Gkk_at_min"] < 0, contrast=True)
    chk("S1: for ANY shift N(t, x), R = (1/2)|curl N|^2 + d_i(N_i K + N_j d_j N_i) - 2 d_t K (residual %s): int R = "
        "(1/2) int |curl N|^2 >= 0 when N falls off faster than 1/r^2" % d["vorticity_residual"],
        d["vorticity_residual"] == "0")
    chk("without the -2 d_t K term the identity fails (%s)" % d["vorticity_residual_no_dt"],
        d["vorticity_residual_no_dt"] != "0", ctl=True)
    chk("S3: Bronnikov-Kim's static throats have R = %s and %s; example 1 reads rho + p_r = %s < 0 on the plane (G_kk < 0) "
        "-- tau = 0 then meets the Gauss trace, conservation and the NEC on either tension" % (
            d["bk_R"][0], d["bk_R"][1], d["bk_nec_ex1"]),
        d["bk_R"] == ["0", "0"] and d["bk_nec_ex1"].startswith("-"))
    fns = d["field_neg_fast_signed"]
    chk("A2 above light strength: with Psi >= 0 imposed the negative plane at v = 1.5 is infeasible (status %d), but that "
        "bound is not physics there; with Psi free where beta > 1 (a gradient-only field's psi takes either sign) it is "
        "feasible (status %d; net int Psi = %.3e, int |Psi| = %.3e, against int R = %.3e) -- a relaxation" % (
            d["field_neg_fast"]["status"], fns["status"], fns.get("int_Psi", float("nan")),
            fns.get("int_abs_Psi", float("nan")), fns["int_R"]),
        d["field_neg_fast"]["status"] == 2 and fns["status"] == 0)
    for e in d["speeds"]:
        structural.append("ENGINE (coarse): " + _row(e))
    structural.append("B1: int R d^3x > 0 at v = 0.1, 1 and 3 (%s); ratio v=3 to v=1 %.4f (an identity: R is exactly "
                      "proportional to v^2)" % (", ".join("%.3e" % x for x in d["int_R_by_v"].values()),
                                                d["int_R_by_v"][3.0] / d["int_R_by_v"][1.0]))
    structural.append("the NEC is sampled on %d directions: a violation found is a lower bound on the true one; the "
                      "resolution, direction and box studies (--study) are H-GRID's tests" % COARSE[2])
    structural.append("the box bound M on tau is reached in none of the engine's main runs here: %s" % (
        "true" if not any(e.get("bound_active") for e in d["resolution"] + d["speeds"]) else "FALSE -- it is"))
    structural.append("C3: sustained radiation needs an unbounded energy supply; on a vacuum-bulk plane nothing supplies "
                      "it, so route C reduces to route A (T5_n mu)")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("escape.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted "
          "(%.0f s)" % (n_pass, n_pass + n_fail, n_ctl, n_con, len(structural), d["seconds"]))
    return n_fail == 0


STUDIES = {
    # every number in ESCAPE.md's table and section 3 is printed by one of these (one JSON line per run)
    "table": [dict(vv=vv, sign=s, NX=NX, NS=NS)
              for vv, grids in ((0.1, FULL_GRIDS), (0.5, FULL_GRIDS), (0.9, FULL_GRIDS[:1]), (1.5, FULL_GRIDS[:2]),
                                (3.0, FULL_GRIDS[:1]))
              for NX, NS in grids for s in (1, -1)],
    "controls": [dict(vv=0.1, sign=1, NX=28, NS=14, ndir=26), dict(vv=0.1, sign=1, NX=37, NS=19, box=4.0)],
    "field": [dict(vv=vv, sign=s, field=True, minimise_field=True, signed_field=signed)
              for vv in SPEEDS for s in (-1, 1) for signed in ((False, True) if vv > 1 else (False,))],
}


def study(name):
    """Run a named study (or 'all'); each run prints one JSON line with its configuration and result."""
    names = list(STUDIES) if name == "all" else [name]
    for nm_ in names:
        for kw in STUDIES[nm_]:
            t0 = time.time()
            r = engine(**kw)
            r.update(study=nm_, config={k: v for k, v in kw.items()}, seconds=round(time.time() - t0, 1))
            print(json.dumps(r), flush=True)


if __name__ == "__main__":
    if "--study" in sys.argv:
        study(sys.argv[sys.argv.index("--study") + 1])
    elif "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(compute("--full" in sys.argv), indent=1, default=str))
    else:
        report("--full" in sys.argv)
