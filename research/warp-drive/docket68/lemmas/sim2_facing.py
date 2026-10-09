#!/usr/bin/env python3
"""sim2_facing.py -- B4d simulation, phase 2, first instrument (M-RULINGS item 168): can two pieces of our one plane
face each other across a static bulk?  Computed, READ and deduced; verified (three verifiers and an adjudication,
2026-10-09: S7's first down-the-throat argument was refuted and is corrected), then re-verified (two re-verifiers,
2026-10-09; their findings applied: see SIM2-FACING.md, History); not seated.  First headed "... not verified; not
seated".  S15 (the coinciding limit) and its selftest C17 were added for M's item 172 after the re-verification and
are not yet verified.

M's words (verbatim in the rulings file; quoted in SIM2-FACING.md, never paraphrased as M's): item 168 "My sense:
positions, one universe"; 152 (1) "two separate positions connected by/reached through a dimension." and (2) "It could
very well be possible, so let's consider this an option and check it."; 126; 127 (1) "1 - yes"; 116 (a) "No, separate"
and (b); 117 and 120 (the NEC "appears broken, but is not"); 123 "forget the coin metaphor."; 118 "Yes: law and
history"; 119; 129 (1); 130 (1) "no added matter"; 136 (2) "released at position two at the closing of the horizon" and
(3) "It is a bridge, not a physical place."; 138; 139 (1), (2), (4); 140; 141 "I suggest the planes are static"; 143 A;
155 (2) "Yes, in bits"; 157; 158 (2), (3), (4); 161; 162; 166 "Both planes at once"; 101 (7); 172 (1) "Yes, it
may" and (2) "Yes, that is coinciding".  Items 169-171
(2026-10-09) bear on why this phase compares the pieces on one static slice: 169 (M's thought, offered for discussion:
no travel through time alone), 170 (carried as H-CLOCK-ABSORBED and H-OBJECT-KEEPS-P1-TIME), 171 (M's question; the
board's answer offered for discussion: space-only teleportation within one universe is this phase).  The static bulk
is the board's choice (158 (3) left it to the math; 141 fixes the planes).  The theorem's clause (G): eq. (17) on the
plane; clause (B): "A vacuum five-dimensional bulk carries the corridor. The plane is free of matter, at the
Randall-Sundrum tension."

THE SETUP.  Units m = 1, e = m/ell, nu = 2/kappa_5^2 (one-sided Israel factor).  Static SO(3) bulk, vacuum, Lambda_5 =
-6/ell^2: ds^2 = dy^2 - A dt^2 + B dr^2 + C dOmega^2, grown from eq. (17) on position 1's piece P1 (y = 0; clause
(G), at our tension: clause (B), 157) by b4_static.series (exact, rational).  kappa_X = (1/2) d_y ln X;
a = (kappa_t + kappa_r + 2 kappa_th)/4, a~ = a + 1/ell; the wall coefficients w_r = kappa_r - kappa_t,
w_th = kappa_th - kappa_t (the warp cancels from both and from a~).  Position 2's piece P2 is a second piece of the same mirrored plane, one-sided toward the slab
(H-Z2-PIECES); it faces P1 when its bulk nearest approach p2 = (r2, depth) is attained in the static region
(H-NEAREST-APPROACH).  A nearest approach only approached down the throat, never attained, is S7's class; since item
172 (2) it rests on M's H-COINCIDE-DOWN-THE-THROAT (127's coincidence is the endless approach down the object's
throat, never a reached point), which replaces the board's H-FACING-DOWN-THE-THROAT and H-COINCIDE-AS-LIMIT; its
depth -> 0 member is the coincidence itself (S15).  The depth of p2 is,
by construction, the two pieces' bulk separation at their nearest point: it is reported only as where in the bulk
facing can occur -- never as the corridor's length (155 (2): bits), never as anything the device sees (101 (7)), and
never optimised over or turned into a time or a speed (139 (4)).  C14 checks names only.  Junction, normal into the
slab: S^a_b = -nu (K^a_b - delta K); for a static P2, rho + p_i = nu (k_t - k_i) for any tension (the local Israel
lemma).

  S1  LEMMA T, THE RICCATI TRAP (deduced; T1 computed exactly on the owner's series).  a' = 1/ell^2 - a^2 - Pi.Pi/4
      (5D Raychaudhuri, R_yy = -4/ell^2); Pi.Pi >= 0 (static: K diagonal); a(0) = -1/ell (Gauss, R4 = 0); so a~ <= 0 at
      every depth the Gaussian chart reaches.  Anchor: a~ = -(R_ab R^ab/12)(y^3 + 5 e y^4) + O(y^5).
  S2  LEMMA C, COMPARISON AT THE NEAREST POINT (deduced; the comparison step standard-not-READ): k_t(P2) = -kappa_t,
      k_spatial(P2) >= -kappa_spatial at p2.
  S3  COROLLARY T5c (deduced): a matter-free mirrored P2 reads s2 <= ell a(depth) <= -1, every depth, every ell.  Under
      clause (B) two matter-free pieces of our plane cannot face each other across a static bulk (diagonal K, vacuum
      Lambda_5), on the board's H-Z2-PIECES and H-NEAREST-APPROACH; down the throat (M's H-COINCIDE-DOWN-THE-THROAT,
      item 172) the member closes too (deduced in the adjudication, using w_th > 0 computed on the throat bulk at the nine ell;
      illustrated on one profile by S7's umbilic member).  That closes this one way of building the corridor within one
      universe; E-PASS, E-NS, E-ROT and the other escapes of S14, E-FAR among them, stay open.
  S4  LEMMA W (deduced): a static mirrored P2 whose total stress obeys the NEC, nearest approach attained in the static
      region with no focal point of P1 before it (S2), needs w_r >= 0 and w_th >= 0 there -- any tension, any matter
      split, no bulk field equation used.
  S5  LEADING ORDERS (computed, exact): w_r = R_rad (y + 3 e y^2), w_th = R_tan (y + 3 e y^2) + O(y^3);
      R_rad = -2m(r - 2m)/(r^2 (2r - 3m)^2) < 0, R_tan = m/(r (2r - 3m)^2) > 0 (sim1_transition.static_nec).
  S6  THE THROAT (STRUCTURAL + computed): eq. (17) at r = 2m is AdS2(2m) x S2(2m); over it the bulk is homogeneous and
      w_r = 0 by the AdS2 boost.
  S7  THE THROAT BULK (computed by ODE; the constraint, measured on the zeroth-order solve, to 5e-13
      relative): y_s^th = 2.5536, 2.3744, 2.2247, 1.9868, 1.6591, 1.2803, 0.9139, 0.6101, 0.3864m at ell = inf, 32m,
      16m, 8m, 4m, 2m, m, m/2, m/4 (alpha -> 0; K diverges); a~ < 0 and w_th > 0 at all 3000 points (max a~/y^3 =
      -0.0208 to -0.0210, min w_th/y = 0.500 to 0.502: the near-plane limits -RR/12 and R_tan at r = 2m); the level-set
      stress rho = nu (p + 2q), rho + p_r = 0, rho + p_th = nu (q - p).  DOWN THE THROAT (computed, corrected after the
      physics verifier refuted the first build's f_ss <= x W1): along y = depth + f(u), u = ln x, the radial NEC is
      f'' - f'/2 <= alpha^2 x W1(depth), the f'/2 being the lapse-gradient term; down_throat_class checks f = c x^lam
      (0 < lam < 1/2) against the radial and angular NEC, exact in the slope, on the throat metric through O(x), and
      illustrates the umbilic (matter-free) member's closing (k_t - k_th -> w_th(depth) > 0: at x = 1e-14 an identity
      for any f -> 0; that the radial equation forces f' -> 0 is deduced, in the adjudication).  So in this class -- a
      nearest approach never attained, the horizon being degenerate and at infinite proper distance in the static
      slice; since item 172 M's H-COINCIDE-DOWN-THE-THROAT -- the NEC sets no lower edge in the approach (x -> 0): it holds at
      every sampled depth, 0.01 to 0.9 y_s^th, at every ell scanned (the adjudication: every depth in [0, y_s^th)).
      Past the crossover the NEC still bends the piece back (the re-verifier, deduced to first order in x and in the
      slope: where W1 < 0, f' e^(-u/2) cannot increase), so whether a member exists below y* is decided on the owner's
      bulk at r of about 2.03-2.7m (E-FAR, E-G), not at the throat.
      Positive energy in the class (the limiting level-set rho_m, at its best depth) needs ell > 27.07m
      (ell_w_class), not 49.86m; at depth -> 0 the limiting stress reads rho_m = -2 sigma_RS at every finite ell.
  S8  THE FIRST CORRECTION IN x = r - 2m (computed): w_r = x W1(y) + O(x^2); y* = first zero of W1 = 1.7901, 1.7286,
      1.6720, 1.5709, 1.4053, 1.1673, 0.8812, 0.6042, 0.3856m (y*/y_s 0.701 to 0.998); the band [y*, y_s^th) for an
      ATTAINED nearest point, at first order in x (the limit r -> 2m); K(y*)/K_bs 18.3 to 5.9e8; rho_m(y*) = +0.1215
      nu/m flat, -0.73 to -36.5 sigma_RS at finite ell; positive energy needs ell >= ell_W = 49.86m; the edge lies below
      30 K_bs for ell > 21.05m, below 100 K_bs for ell > 5.82m, never below 10.  On H-LAW-READ-BY-TRACE a facing piece
      at depth >= y* reads s <= ell a(y*) = -7.17 (32m) ... -3.36 (4m) ... -84.2 (m/4): a law that is not ours.  The
      O(x) expansion holds while x max(|a1|, |b1|, |c1|) <= 0.1: x <= 1.7e-2, 1.2e-2, 3.9e-3, 2.7e-4 at y* (ell = inf,
      4m, m, m/4), about half that at the band's midpoint, shrinking toward y_s.
  S9  THE MAP ON THE OWNER'S BULK (computed; raw Pade as evidence): 13 radii x 9 ell at order 32, banked.  Verified =
      b4_static S3's value rule; admissible = verified, the two orders agreeing on the SIGNS of w_r and w_th, both >= 0.
      (The first build's w-agreement rule sat in the verified prefix and cut each column where w_r changes sign; it is
      now a reported diagnostic only.)  4480 verified points (4479 sign-settled), 86 admissible.  Of the 3910 at
      r >= 2.05m or ell <= 2m: w_r < 0 at 3906 and >= 0 at 4 (r = 2.05m at ell = inf past 2.198m; r = 2.005m at
      ell = 2m past 1.186m); w_th > 0 at 3906 (w_th < 0 at four deep points of r = 2.5m, ell = inf, 32m, 16m, all with
      w_r < 0); a~ < 0 at all.  w_r turns positive at r = 2.005m past 1.821, 1.758, 1.700, 1.597, 1.428, 1.186m
      (ell = inf to 2m).  At ell = inf the three Pade orders are now distinct approximants (pade_orders).
  S10 THROAT AND OWNER AGREE (computed): the sign change extrapolated to x -> 0 meets y* to 0.07-0.15% (ell = inf to 4m);
      W1(1.088) to 0.5%; the x -> 0 extrapolation of w_th, a~ to 0.2%; y_s^th 0.3-3% below the near-throat columns' Pade
      singularity.
  S11 LEMMA N (deduced; sympy): Gamma^y_ab = -(1/2) d_y g_ab; a radial null ray tangent to a level set has
      y'' = w_r B r'^2.  Corollary W: warped products have w = 0 (the black string, RS2).
  S12 THE DECISION per ell (WIDE / THROAT-BAND / NONE), from S7-S9, for ATTAINED nearest points, on the verified map
      (13 radii to r = 10m, nine ell): THROAT-BAND at every
      ell -- CONFIRMED on the owner's bulk at ell >= 2m (the r = 2.005m column's first rising sign change of w_r lies
      1.6-1.8% from the throat's y*, x -> 0: the O(x) shift), EXPANSION-ONLY at ell <= m (the near-throat columns'
      verified tops lie below y*: not reached); regular at 30 and 100 K_bs for ell = inf, 32m, at 100 only for 16m, 8m,
      at none for ell <= 4m; positive energy only at ell >= 49.86m.  WIDE is excluded on the verified points only:
      decide() records, per ell, the unverified depths at r >= 2.1m (the board's line, a convention), where facing is
      unchecked, as it is for E-FAR.  The down-the-throat class (S7) has no lower edge in the approach (x -> 0), its
      shallow depths lie below 10 K_bs at every ell, and its positive-energy threshold is 27.07m.
  S13 THE HAND-OFF TO PHASE 3 (deduced): s_slab <= ell a(depth) <= -1 (equality for a level surface; in the limit down
      the throat), in units of sigma_RS at the slab's ell (ours within one universe: stage 7 K4's unit-ell_1 rows); the
      outer side needed for the -1/3 that 139 (1) said yes to (multiplane.py M4's figure) and for stage 7 K5's -1/6.
      The within-universe rows hold on H-SPLIT-AT-OUR-TENSION; on H-LAW-READ-BY-TRACE the NEC rows move to
      Delta s <= ell a(depth) - 1 < 0, phase 3's direction.
  S14 THE ESCAPES LEFT (STRUCTURAL / OPEN), now with E-Q (quantum or semiclassical stress; excluded only by
      H-NEC-NEVER-VIOLATED, 117/120) and E-FAR (a nearest approach reached only as r -> infinity, beyond r = 10m, or
      beyond a column's verified top, including the continuation of S7's approach below y*; open).
  S15 THE COINCIDING LIMIT (item 172; computed and deduced): S7's class with its approach depth -> 0 and x -> 0.  P2's
      stress tends to the RS1 sheet: rho -> -sigma_RS, rho + p_i -> 0, s = rho/sigma_RS and the trace reading -> -1
      (deduced from the throat data at depth 0; computed on four profiles at the nine ell), so rho_m -> -2 sigma_RS at
      every finite ell.  On H-SPLIT-AT-OUR-TENSION with H-POSITIVE-ON-P2 the WEC along any approach needs the level value
      nu (p + 2q - 3/ell) >= 0 at the approach depth (deduced, exact in the slope at x -> 0), so positive energy starts
      only at d_+ > 0 at every finite ell (computed: d_+ exists only for ell > 27.07m; 0.8395m at 32m; d_+ ~ 24 m^2/ell
      as ell -> infinity).  Flat limit: rho -> 0+ along the approach (c x^lam (1/4 - lam^2); -(3/4) g2 x on the smooth
      family): no positive margin at coincidence.  On H-LAW-READ-BY-TRACE the coinciding piece is a matter-free sheet of
      tension -1 at our ell: 139 (1)'s sign, a different law (phase 3).  Depths reported only as where facing occurs.
  The computed branch (S4, S7-S12, S15) rests on H-README-ON-P2, M's since item 172 (1) ("Yes, it may"): during the
  hold position 2's piece may carry the README's stress, obeying the NEC, and the theorem's clause (B), "The plane is
  free of matter", then holds in full on P1 and its tension half only on P2 -- a change to clause (B)'s scope, carried,
  not seated.  As M worded them, 129 (1), 130 (1) and 136 (2) had read against it.  Which part of P2's stress is its
  law was not answered (question 1 (b)): the results count as within one universe only on the board's
  H-SPLIT-AT-OUR-TENSION (position 2's law fixed at our tension; everything else in its stress, its trace included, the
  README's).  On H-LAW-READ-BY-TRACE instead the band's piece reads s <= ell a(y*) <= -1, and the coinciding piece
  s = -1: a law not ours (phase 3).
  It is necessary, not sufficient, and never B4d green.

Owners imported by path (never copied): b4_static.py (series, _eq17, _schwarzschild, pade), b4d_stage5.py (warped,
orders, _approx, nearest_real, evaluator for K only, k_bs, wall_exact; _clean only in C5's mutation), b4d_stage6.py
(sigma_over_rs), b4d_stage7.py (ricci_squared, slab_trace), sim1_transition.py (static_nec, eq17_rkk).
Needs python-flint, sympy, numpy, scipy, mpmath.
python3 sim2_facing.py [--selftest] [--regenerate]   (selftest about 2 min; regenerate about 14 min on 3 CPUs)
"""
import contextlib
import importlib.util
import inspect
import io
import json
import math
import os
import sys
import time
from fractions import Fraction as Fr
from multiprocessing import Pool

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
BANK = os.path.join(HERE, "sim2_bank.json")
ORDER = 32
ES2 = [Fr(0), Fr(1, 32), Fr(1, 16), Fr(1, 8), Fr(1, 4), Fr(1, 2), Fr(1), Fr(2), Fr(4)]
RADII2 = ["401/200", "201/100", "101/50", "41/20", "21/10", "43/20", "11/5", "23/10", "5/2", "3", "4", "5", "10"]
NGRID = 40                  # S9's y grid
VAL_TOL = 1e-4              # two Pade orders agree on A, B, C (b4_static S3's criterion): the verified prefix
W_ABS, W_REL = 1e-6, 1e-3   # the first build's w-agreement rule on w_r, w_th: a reported DIAGNOSTIC only, never part of
#                             the verified prefix (verifiers: near a zero of w_r it collapses to 1e-6 absolute and cut
#                             each column exactly where w_r changes sign).  Admissibility needs the two orders to agree on
#                             the SIGN of w_r and w_th instead (sign_ok).
DOUBLET = 2e-3              # a real pole with a zero this close is a Froissart doublet (b4d_stage5.nearest_real's rule)
CAP = 10.0                  # scan cap in m
WIDE_R = 2.1                # S12: WIDE needs an admissible point at r_c >= 2.1m
NEAR_R = 2.02               # S12: CONFIRMED needs an owner column at r_c <= 2.02m ...
CONFIRM_TOL = 0.05          # ... admissible within 5% of the throat's y*
KF = (10, 30, 100)          # thresholds of K/K_bs, reported together with the strict y < y_s
ALPHA_END = 1e-9            # y_s^th: alpha -> 0 (converged to 1e-7 m by alpha = 1e-6)
ALPHA_FULL = 1e-6           # the O(x) system is followed to alpha = 1e-6
BANNED_KEYS = ("dist", "separation", "time", "redshift", "speed", "velocity", "length", "clock", "arrival")
BANNED_ARGS = {"d", "D", "sep", "separation", "distance", "dist", "gap", "length", "time", "speed", "velocity",
               "redshift", "arrival"}


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


B4 = _load(os.path.join(HERE, "b4_static.py"), "sim2_b4static")
S5 = _load(os.path.join(HERE, "b4d_stage5.py"), "sim2_stage5")
S6 = _load(os.path.join(HERE, "b4d_stage6.py"), "sim2_stage6")
S7 = _load(os.path.join(HERE, "b4d_stage7.py"), "sim2_stage7")
SIM1 = _load(os.path.join(HERE, "sim1_transition.py"), "sim2_sim1")

_NEC = {}


def _nec():
    """sim1_transition.static_nec (eq. (17)'s Weyl fluid: rho, p_r, p_t and the radial/tangential NEC sums), cached."""
    if not _NEC:
        _NEC.update(SIM1.static_nec())
    return _NEC


_RKK = {}


def rkk_closed(rc):
    """sim1_transition.eq17_rkk: eq. (17)'s radial null Ricci R_kk (k = (1/sqrt F, sqrt H)), at r = rc -- R_rad's sign."""
    if not _RKK:
        Rkk, resid = SIM1.eq17_rkk()
        _RKK.update({"Rkk": Rkk, "resid": resid})
    rs = [s for s in _RKK["Rkk"].free_symbols if s.name == "r"][0]
    return sp.nsimplify(_RKK["Rkk"].subs(rs, sp.Rational(rc))), _RKK["resid"]


def r_hat(rc):
    """R_rad = R^r_r - R^t_t = 8 pi (rho + p_r) and R_tan = R^th_th - R^t_t = 8 pi (rho + p_t) of eq. (17), exact."""
    n = _nec()
    rs = [s for s in n["radial"].free_symbols if s.name == "r"][0]
    rv = sp.Rational(rc)
    return sp.nsimplify(8 * sp.pi * n["radial"].subs(rs, rv)), sp.nsimplify(8 * sp.pi * n["tangential"].subs(rs, rv))


# ------------------------------------------------------------------------------------------------ exact series helpers
def _deriv(c):
    return [k * c[k] for k in range(1, len(c))]


def _mul(a, b, n):
    return [sum((a[i] * b[k - i] for i in range(k + 1) if i < len(a) and k - i < len(b)), Fr(0)) for k in range(n + 1)]


def _div(a, b, n):
    out = []
    for k in range(n + 1):
        s = (a[k] if k < len(a) else Fr(0)) - sum((b[j] * out[k - j] for j in range(1, k + 1) if j < len(b)), Fr(0))
        out.append(s / b[0])
    return out


def kappas(rc, e, N):
    """Exact Taylor series (orders 0..N-1) of kappa_t, kappa_r, kappa_th = (1/2) d_y ln X on the owner's series."""
    S = B4.series(rc, N, e)
    out = {}
    for X in "ABC":
        c = [Fr(v) for v in S[X][0][:N + 1]]
        out[X] = [v / 2 for v in _div(_deriv(c), c, N - 1)]
    return out


# ------------------------------------------------------------------------------------------------ S1 Lemma T
def riccati_identity(rc, e, N=14, ryy_sign=-1):
    """T1 on the owner's exact series: the coefficients of a' - (1/ell^2 - a^2 - Pi.Pi/4) through y^(N-2).  ryy_sign is
    the sign of R_yy = ryy_sign 4/ell^2 (the vacuum has -1; +1 is C3's mutation)."""
    k = kappas(rc, e, N)
    n = N - 2
    a = [(k["A"][j] + k["B"][j] + 2 * k["C"][j]) / 4 for j in range(N)]
    Pi = {X: [k[X][j] - a[j] for j in range(N)] for X in "ABC"}
    PiPi = [u + v + 2 * w for u, v, w in zip(_mul(Pi["A"], Pi["A"], n), _mul(Pi["B"], Pi["B"], n),
                                              _mul(Pi["C"], Pi["C"], n))]
    aa = _mul(a, a, n)
    ee = Fr(e) ** 2
    rhs = [(-ryy_sign * ee if j == 0 else Fr(0)) - aa[j] - PiPi[j] / 4 for j in range(n + 1)]
    ap = _deriv(a)
    return [ap[j] - rhs[j] for j in range(n + 1)]


def lemma_t():
    """T1-T4 as symbolic statements: the Raychaudhuri split, the Riccati comparison and its fixed point at s1 = 1."""
    kt, kr, kq, ee, s1, Y = sp.symbols("k_t k_r k_q e s_1 Y", real=True)
    a = (kt + kr + 2 * kq) / 4
    split = sp.expand((kt**2 + kr**2 + 2 * kq**2) - (4 * a**2 + (kt - a)**2 + (kr - a)**2 + 2 * (kq - a)**2))
    ep = sp.Symbol("e", positive=True)
    comp = ep * sp.tanh(ep * Y - sp.atanh(s1))                 # solves b' = e^2 - b^2, b(0) = -e s1
    ode = sp.simplify(sp.diff(comp, Y) - (ep**2 - comp**2))
    start = sp.simplify(comp.subs(Y, 0) + ep * s1)
    fixed = sp.limit(comp, s1, 1, "-")                          # s1 = 1: the depth drops out
    return {"split": split, "ode": ode, "start": start, "fixed_point": sp.simplify(fixed / ep)}


# ------------------------------------------------------------------------------------------------ S3 Corollary T5c
def t5c(e):
    """s2 <= ell a(depth) <= -1 for a matter-free mirrored P2 facing P1 (one-universe law, s1 = 1); the general bound
    s2 <= tanh(depth/ell - artanh s1) for the controls.  Symbolic in the depth Y."""
    s1, Y = sp.symbols("s_1 Y", real=True)
    gen = sp.tanh(Y * sp.Rational(Fr(e).numerator, Fr(e).denominator) - sp.atanh(s1)) if e != 0 else None
    at_rs = sp.limit(gen, s1, 1, "-") if gen is not None else sp.Integer(-1)
    return {"general": gen, "at_s1_1": at_rs, "s2_max": sp.Integer(-1)}


# ------------------------------------------------------------------------------------------------ S4 Lemma W
def israel(K, nu=1, trace_from=0):
    """One-sided Israel: S^a_b = -nu (K^a_b - delta K); K the mixed diagonal (k_t, k_r, k_th, k_ph).  Returns rho and
    the pressures p_i = S^i_i.  trace_from = 1 (the trace over the spatial part only) is C2's mutation."""
    tr = sum(K[trace_from:])
    S = [-nu * (k - tr) for k in K]
    return -S[0], S[1:]


def level_set_k(e, n_y):
    """The mixed extrinsic curvature of an RS2 level set y = Y in dy^2 + e^(-2 e y) eta, computed from the warp:
    K^a_b = n^y (1/2) d_y ln(e^(-2 e y)) delta^a_b, for the normal n = n_y d_y (n_y = +1 or -1).  C1's RS1 control
    (n_y = -1, into a slab lying at y < Y) and its mutation (n_y = +1) both come through here, not through P1's literal
    K = -h/ell."""
    Y = sp.Symbol("Y", real=True)
    warp = sp.exp(-2 * e * Y)
    k = sp.simplify(n_y * sp.diff(warp, Y) / (2 * warp))
    return [k] * 4


def lemma_w(kt, kr, kth):
    """At a nearest point p2 with the bulk's kappa_t, kappa_r, kappa_th: Lemma W's necessary condition for a static
    mirrored P2 whose total stress obeys the NEC (any tension, any matter split)."""
    w_r, w_th = kr - kt, kth - kt
    return {"w_r": w_r, "w_th": w_th, "admissible": bool(w_r >= 0 and w_th >= 0)}


def lemma_w_proof(n_trials=20000, seed=7, flip=False):
    """W's step, exact and sampled: with k_t = -kappa_t and k_spatial = -kappa_spatial + H (H >= 0, any symmetric 3x3),
    k_t I - k_spatial = diag(w) - H, so NEC (k_t I >= k_spatial) forces diag(w) >= H >= 0.  Sampled over random kappa and
    H; flip = True reverses the comparison (H <= 0), which must produce counterexamples."""
    w1, w2 = sp.symbols("w_1 w_2", real=True)
    kt_, kr_, kq_ = sp.symbols("kappa_t kappa_r kappa_q", real=True)
    Hs = sp.Matrix(3, 3, lambda i, j: sp.Symbol("h%d%d" % (min(i, j), max(i, j)), real=True))
    lhs = (-kt_) * sp.eye(3) - (-sp.diag(kr_, kq_, kq_) + Hs)
    exact = sp.simplify(lhs - (sp.diag(kr_ - kt_, kq_ - kt_, kq_ - kt_) - Hs)) == sp.zeros(3, 3)
    rng = np.random.default_rng(seed)
    bad = nec = 0
    for _ in range(n_trials):
        kap = rng.normal(size=3)
        M = rng.normal(size=(3, 3))
        H = 0.3 * M @ M.T * (-1 if flip else 1)
        k_sp = -np.diag([kap[1], kap[2], kap[2]]) + H
        if np.all(np.linalg.eigvalsh((-kap[0]) * np.eye(3) - k_sp) >= 0):
            nec += 1
            if not (kap[1] - kap[0] >= 0 and kap[2] - kap[0] >= 0):
                bad += 1
    return {"exact": exact, "nec_samples": nec, "counterexamples": bad}


# ------------------------------------------------------------------------------------------------ S5 leading orders
def leading_coefficients(rc, e, N=8):
    """Exact y^0..y^4 coefficients of w_r, w_th and a~ on the owner's series, with eq. (17)'s R_rad, R_tan and
    R_ab R^ab."""
    k = kappas(rc, e, N)
    wr = [k["B"][j] - k["A"][j] for j in range(5)]
    wth = [k["C"][j] - k["A"][j] for j in range(5)]
    at = [(k["A"][j] + k["B"][j] + 2 * k["C"][j]) / 4 + (Fr(e) if j == 0 else 0) for j in range(5)]
    Rr, Rt = r_hat(rc)
    _, RR = S7.ricci_squared(sp.Rational(rc))
    return {"wr": wr, "wth": wth, "at": at, "R_rad": Rr, "R_tan": Rt, "RR": sp.nsimplify(RR)}


def check_leading(rc, e):
    """C4: S5's coefficients exact, and against the owners (wall_exact for w_r, slab_trace for a~)."""
    L = leading_coefficients(rc, e)
    ee = sp.Rational(Fr(e).numerator, Fr(e).denominator)
    q = lambda v: sp.Rational(v.numerator, v.denominator)
    ok = (q(L["wr"][0]) == 0 and q(L["wr"][1]) == L["R_rad"] and q(L["wr"][2]) == 3 * ee * L["R_rad"]
          and q(L["wth"][0]) == 0 and q(L["wth"][1]) == L["R_tan"] and q(L["wth"][2]) == 3 * ee * L["R_tan"]
          and all(q(L["at"][j]) == 0 for j in range(3)) and q(L["at"][3]) == -L["RR"] / 12
          and q(L["at"][4]) == -5 * ee * L["RR"] / 12)
    w0, w1, w2, R4 = S5.wall_exact(Fr(e), rc)
    own_w = (w0 == 0 and w1 == 0 and w2 == 0 and sp.nsimplify(R4) == L["R_rad"])
    st = S7.slab_trace(Fr(e), rc)
    own_a = all(sp.nsimplify(-st.coeff(S7.d, j) + (ee if j == 0 else 0)) == q(L["at"][j]) for j in range(5))
    rk, resid = rkk_closed(rc)
    own_w = own_w and rk == L["R_rad"] and resid == 0
    return ok, own_w, own_a, L


# ------------------------------------------------------------------------------------------------ geometry helpers (sympy)
def _ricci_diag(g, X):
    """Christoffels and Ricci R_bc of a diagonal metric g (list) in coordinates X."""
    n = len(X)
    gi = [1 / v for v in g]
    G = {}
    for a in range(n):
        for b in range(n):
            for c in range(b, n):
                v = 0
                if a == b:
                    v += sp.diff(g[a], X[c])
                if a == c:
                    v += sp.diff(g[a], X[b])
                if b == c:
                    v -= sp.diff(g[b], X[a])
                v = v * gi[a] / 2
                if v != 0:
                    G[(a, b, c)] = G[(a, c, b)] = v
    Gm = lambda a, b, c: G.get((a, b, c), 0)

    def R(b, c):
        s = 0
        for a in range(n):
            s += sp.diff(Gm(a, b, c), X[a]) - sp.diff(Gm(a, b, a), X[c])
            for k in range(n):
                s += Gm(a, a, k) * Gm(k, b, c) - Gm(a, c, k) * Gm(k, b, a)
        return s
    return R, gi, Gm


# ------------------------------------------------------------------------------------------------ S6 the throat
def near_horizon(data=None):
    """Eq. (17) at r = 2m: R^a_b from sim1_transition.static_nec (R = 0, so R^a_b = 8 pi T^a_b of the Weyl fluid); the
    expansions F = A ~ x/2, H = 1/B ~ x^2 (x = r - 2m); the AdS2 factor's curvature (-1/2: radius 2m) and the S2 radius."""
    n = _nec()
    rs = [s for s in n["rho"].free_symbols if s.name == "r"][0]
    Rmix = [sp.nsimplify(v.subs(rs, 2)) for v in (-8 * sp.pi * n["rho"], 8 * sp.pi * n["pr"], 8 * sp.pi * n["pt"])]
    x, t = sp.symbols("x t", positive=True)
    F, H = (data or B4._eq17)(2 + x)
    Fs = sp.series(F, x, 0, 3).removeO()
    Hs = sp.series(H, x, 0, 4).removeO()
    Rf, gi, _ = _ricci_diag([-sp.Rational(1, 2) * x, 1 / x**2], [t, x])
    R2 = sp.simplify(gi[0] * Rf(0, 0) + gi[1] * Rf(1, 1))
    return {"R_mixed": Rmix + [Rmix[2]], "F": Fs, "H": Hs, "F_lead": sp.limit(F / x, x, 0),
            "H_lead": sp.limit(H / x**2, x, 0), "AdS2_R": R2, "S2_radius": sp.sqrt((2 + x)**2).subs(x, 0)}


def throat_equations(s2=1):
    """C7: the throat ODEs re-derived from a sympy 5D Ricci of ds^2 = dy^2 + alpha^2 [-(x/2) dt^2 + dx^2/x^2]
    + 4 beta^2 dOmega^2 (vacuum, Lambda_5 = -6/ell^2), and the Kretschmann formula K_th.  s2 = -1 flips the S2 curvature
    in the coded system (the mutation)."""
    y, t, x, th, ph = sp.symbols("y t x theta phi", real=True)
    e = sp.Symbol("e", nonnegative=True)
    al, be = sp.Function("alpha")(y), sp.Function("beta")(y)
    g = [sp.Integer(1), -al**2 * x / 2, al**2 / x**2, 4 * be**2, 4 * be**2 * sp.sin(th)**2]
    X = [y, t, x, th, ph]
    R, gi, Gm = _ricci_diag(g, X)
    E = [sp.simplify(gi[i] * R(i, i) + 4 * e**2) for i in range(5)]
    p, q, P, Q, a, b = sp.symbols("p q P Q a b")
    sub = {sp.Derivative(al, (y, 2)): (P + p**2) * a, sp.Derivative(be, (y, 2)): (Q + q**2) * b,
           sp.Derivative(al, y): p * a, sp.Derivative(be, y): q * b}
    Es = [sp.simplify(v.subs(sub).subs({al: a, be: b})) for v in E]
    sol = sp.solve([Es[1], Es[3]], [P, Q], dict=True)[0]
    coded_P = 4 * e**2 - 2 * p**2 - 2 * p * q - 1 / (4 * a**2)
    coded_Q = 4 * e**2 - 2 * q**2 - 2 * p * q + s2 / (4 * b**2)
    cons = sp.expand(Es[0].subs(sol))
    coded_c = p**2 + q**2 + 4 * p * q - 6 * e**2 - 1 / (4 * b**2) + 1 / (4 * a**2)
    # Kretschmann of the same metric, all components
    import itertools
    n = 5
    Gam = [[[Gm(i, j, k) for k in range(n)] for j in range(n)] for i in range(n)]
    K = 0
    for i, j, k, l in itertools.product(range(n), repeat=4):
        if k >= l:
            continue
        Rv = (sp.diff(Gam[i][j][l], X[k]) - sp.diff(Gam[i][j][k], X[l])
              + sum(Gam[i][k][m] * Gam[m][j][l] - Gam[i][l][m] * Gam[m][j][k] for m in range(n)))
        if Rv != 0:
            K += 2 * Rv**2 * g[i] * gi[j] * gi[k] * gi[l]
    Ks = sp.simplify(K.subs(sub).subs({al: a, be: b}))
    coded_K = 4 * (2 * (P + p**2)**2 + 2 * (Q + q**2)**2 + (p**2 + 1 / (4 * a**2))**2 + (q**2 - 1 / (4 * b**2))**2
                   + 4 * p**2 * q**2)
    return {"P": sp.simplify(sol[P] - coded_P), "Q": sp.simplify(sol[Q] - coded_Q),
            "xx_tt": sp.simplify(Es[2] - Es[1]), "ph_th": sp.simplify(Es[4] - Es[3]),
            "constraint_ratio": sp.simplify(cons / coded_c), "yx": sp.simplify(R(0, 2)),
            "K": sp.simplify(Ks - coded_K)}


def throat_first_order():
    """C8: the O(x) equations re-derived: A = (x/2) alpha^2 (1 + x a1), B = (alpha^2/x^2)(1 + x b1),
    C = 4 beta^2 (1 + x c1); the tt, xx, thth equations at O(x) solved for a1'', b1'', c1'' against the coded ones; the
    momentum constraint (R_yx at O(1)) and the O(x) Hamiltonian constraint (yy); the data's O(x) terms from eq. (17)."""
    y, t, x, th, ph = sp.symbols("y t x theta phi", real=True)
    e = sp.Symbol("e", nonnegative=True)
    al, be = sp.Function("alpha")(y), sp.Function("beta")(y)
    a1, b1, c1 = sp.Function("a1")(y), sp.Function("b1")(y), sp.Function("c1")(y)
    A = x * al**2 / 2 * (1 + x * a1)
    B = al**2 / x**2 * (1 + x * b1)
    C = 4 * be**2 * (1 + x * c1)
    g = [sp.Integer(1), -A, B, C, C * sp.sin(th)**2]
    X = [y, t, x, th, ph]
    R, gi, _ = _ricci_diag(g, X)
    p, q, P, Q, a, b = sp.symbols("p q P Q a b")
    A1, B1, C1, dA, dB, dC, ddA, ddB, ddC = sp.symbols("A1 B1 C1 dA dB dC ddA ddB ddC")
    sub = {sp.Derivative(al, (y, 2)): (P + p**2) * a, sp.Derivative(be, (y, 2)): (Q + q**2) * b,
           sp.Derivative(al, y): p * a, sp.Derivative(be, y): q * b,
           sp.Derivative(a1, (y, 2)): ddA, sp.Derivative(b1, (y, 2)): ddB, sp.Derivative(c1, (y, 2)): ddC,
           sp.Derivative(a1, y): dA, sp.Derivative(b1, y): dB, sp.Derivative(c1, y): dC}
    fin = {al: a, be: b, a1: A1, b1: B1, c1: C1}
    bg = {P: 4 * e**2 - 2 * p**2 - 2 * p * q - 1 / (4 * a**2), Q: 4 * e**2 - 2 * q**2 - 2 * p * q + 1 / (4 * b**2)}
    out = {}
    for (i, j) in [(0, 0), (1, 1), (2, 2), (3, 3), (0, 2)]:
        Eij = gi[i] * R(i, j) + (4 * e**2 if i == j else 0)
        ser = sp.series(Eij.subs(sub).subs(fin).subs(bg), x, 0, 2).removeO()
        out[(i, j)] = (sp.simplify(ser.coeff(x, 0)), sp.simplify(ser.coeff(x, 1)))
    sol = sp.solve([out[(1, 1)][1], out[(2, 2)][1], out[(3, 3)][1]], [ddA, ddB, ddC], dict=True)[0]
    coded = {ddA: -(2 * A1 - B1 + C1) / a**2 - (3 * dA + dB + 2 * dC) * p - 2 * dA * q,
             ddB: -(2 * A1 - B1 + 2 * C1) / a**2 - (dA + 3 * dB + 2 * dC) * p - 2 * dB * q,
             ddC: -(dA + dB) * q - 2 * (p + 2 * q) * dC - C1 / (2 * b**2) - 3 * C1 / (2 * a**2)}
    mom = -sp.Rational(3, 4) * dA + dB / 4 - dC + C1 * (p - q)
    ham = sp.expand(out[(0, 0)][1].subs(sol))
    coded_ham = (2 * A1 / a**2 - B1 / a**2 + C1 / (2 * b**2) + 3 * C1 / a**2 + (dA + dB) * (p + 2 * q)
                 + 4 * dC * p + 2 * dC * q)
    xs = sp.Symbol("x", positive=True)
    F, H = B4._eq17(2 + xs)
    Aser = sp.series(F, xs, 0, 3).removeO()
    Bser = sp.series(1 / H * xs**2, xs, 0, 2).removeO()
    Cser = sp.series((2 + xs)**2 / 4, xs, 0, 2).removeO()
    data = (sp.simplify(Aser.coeff(xs, 2) / Aser.coeff(xs, 1)), Bser.coeff(xs, 1) / Bser.coeff(xs, 0),
            Cser.coeff(xs, 1) / Cser.coeff(xs, 0))
    return {"dd": [sp.simplify(sol[k] - coded[k]) for k in (ddA, ddB, ddC)],
            "mom_ratio": sp.simplify(out[(0, 2)][0] / mom), "ham": sp.simplify(ham - coded_ham),
            "O1_zero": [out[(i, i)][0] for i in (1, 2, 3)], "data": data}


# ------------------------------------------------------------------------------------------------ S7/S8 the throat bulk
def throat_rhs(y, u, e, s2=1.0, mut=0.0):
    """(alpha, beta, p, q) and the O(x) system (a1, b1, c1 and their y-derivatives).  s2 = -1 flips the S2 curvature
    (C7's mutation); mut != 0 perturbs the coded b1'' (C8's mutation)."""
    al, be, p, q, a1, b1, c1, da, db, dc = u
    P = 4 * e * e - 2 * p * p - 2 * p * q - 1 / (4 * al * al)
    Q = 4 * e * e - 2 * q * q - 2 * p * q + s2 / (4 * be * be)
    dda = -(2 * a1 - b1 + c1) / al**2 - (3 * da + db + 2 * dc) * p - 2 * da * q
    ddb = -(2 * a1 - b1 + 2 * c1) / al**2 - (da + 3 * db + 2 * dc) * p - 2 * db * q + mut * db * p
    ddc = -(da + db) * q - 2 * (p + 2 * q) * dc - c1 / (2 * be * be) - 3 * c1 / (2 * al * al)
    return [p * al, q * be, P, Q, da, db, dc, dda, ddb, ddc]


def kret_throat(u, e):
    """K_th = 4[2(p' + p^2)^2 + 2(q' + q^2)^2 + (p^2 + 1/(4 alpha^2))^2 + (q^2 - 1/(4 beta^2))^2 + 4 p^2 q^2] (C7)."""
    al, be, p, q = u[:4]
    P = 4 * e * e - 2 * p * p - 2 * p * q - 1 / (4 * al * al)
    Q = 4 * e * e - 2 * q * q - 2 * p * q + 1 / (4 * be * be)
    return 4 * (2 * (P + p * p)**2 + 2 * (Q + q * q)**2 + (p * p + 1 / (4 * al * al))**2
                + (q * q - 1 / (4 * be * be))**2 + 4 * p * p * q * q)


def throat_bulk(e, s2=1.0, mut=0.0, b1_0=2.5):
    """The throat bulk at e = m/ell: the zeroth-order system followed to alpha = 1e-9 (y_s^th), and the full system with
    the O(x) correction followed to alpha = 1e-6.  Start: alpha = beta = 1, p = q = -e; a1 = -1/2, b1 = 5/2, c1 = 1, all
    first derivatives 0 (eq. (17)'s data, C8)."""
    ef = float(e)
    u0 = [1.0, 1.0, -ef, -ef, -0.5, b1_0, 1.0, 0.0, 0.0, 0.0]

    def end0(y, u, *_):
        return u[0] - ALPHA_END
    end0.terminal = True

    def blow(y, u, *_):
        return abs(u[2]) + abs(u[3]) - 1e15
    blow.terminal = True

    def end1(y, u, *_):
        return u[0] - ALPHA_FULL
    end1.terminal = True
    f0 = lambda y, u: throat_rhs(y, list(u) + [0.0] * 6, ef, s2)[:4]
    # max_step: C7 measures the zeroth-order constraint on this solve (verifier).  Without a cap it took about 60 steps
    # below 0.95 y_s and held the constraint only to 2.3e-10 relative at ell = m/4 (the 10-variable solve, whose O(x)
    # variables force about 500 steps, had hidden this); at 0.005 it holds to about 5e-13 and y_s moves by <= 1.1e-11.
    sol0 = solve_ivp(f0, [0, 12], u0[:4], method="DOP853", rtol=1e-13, atol=1e-15, events=[end0, blow],
                     dense_output=True, max_step=0.005)
    sol = solve_ivp(lambda y, u: throat_rhs(y, u, ef, s2, mut), [0, 12], u0, method="DOP853", rtol=1e-13, atol=1e-15,
                    events=[end1, blow], dense_output=True)
    return {"e": ef, "y_s": float(sol0.t[-1]), "y_end": float(sol.t[-1]), "sol": sol, "sol0": sol0,
            "reached_alpha0": bool(sol0.status == 1 and len(sol0.t_events[0]) > 0)}


def _first_root(f, lo, hi, n=4000, rising=None):
    yy = np.linspace(lo, hi, n)
    v = np.array([f(z) for z in yy])
    s = np.sign(v)
    idx = np.where(s[:-1] * s[1:] < 0)[0]
    if rising is not None:
        idx = [i for i in idx if (v[i + 1] > v[i]) == rising]
    if not len(idx):
        return None
    i = idx[0]
    return float(brentq(f, yy[i], yy[i + 1], xtol=1e-13))


def _ystar(tb):
    s, ys, ye = tb["sol"], tb["y_s"], tb["y_end"]
    W1 = lambda y: float(s.sol(y)[8] - s.sol(y)[7]) / 2
    return _first_root(W1, 1e-3 * ys, ye * (1 - 1e-9), rising=True), W1


def _yK(tb, f):
    s, ys, ye, ef = tb["sol"], tb["y_s"], tb["y_end"], tb["e"]
    g = lambda y: kret_throat(s.sol(y), ef) - f * S5.k_bs(ef, 2.0, y)
    return _first_root(g, 1e-3 * ys, ye * (1 - 1e-9), rising=True)


def throat_row(e):
    """One row of S8's table at e = m/ell, with S7's checks."""
    tb = throat_bulk(e)
    s, ys, ye, ef = tb["sol"], tb["y_s"], tb["y_end"], tb["e"]
    yst, W1 = _ystar(tb)
    yK = {f: _yK(tb, f) for f in KF}
    U = lambda y: s.sol(y)
    rho = lambda y: float(U(y)[2] + 2 * U(y)[3] - 3 * ef)                  # rho_m in units of nu/m (level set)
    g95 = np.linspace(1e-3 * ys, 0.95 * ys, 3000)
    V = tb["sol0"].sol(g95)          # C7's constraint on the zeroth-order solve (not the 10-variable one: step control)
    al, be, p, q = V[0], V[1], V[2], V[3]
    cons = p * p + q * q + 4 * p * q - 6 * ef * ef - 1 / (4 * be * be) + 1 / (4 * al * al)
    scale = p * p + q * q + 1 / (4 * al * al) + 1 / (4 * be * be) + 6 * ef * ef
    g90 = np.linspace(1e-3 * ys, 0.9 * ys, 3000)
    Z = s.sol(g90)
    mom = -0.75 * Z[7] + Z[8] / 4 - Z[9] + Z[6] * (Z[2] - Z[3])
    ham = (2 * Z[4] / Z[0]**2 - Z[5] / Z[0]**2 + Z[6] / (2 * Z[1]**2) + 3 * Z[6] / Z[0]**2
           + (Z[7] + Z[8]) * (Z[2] + 2 * Z[3]) + 4 * Z[9] * Z[2] + 2 * Z[9] * Z[3])
    gall = np.linspace(1e-3 * ys, ye * (1 - 1e-6), 3000)
    A_ = s.sol(gall)
    wth_all, at_all = A_[3] - A_[2], (A_[2] + A_[3]) / 2 + ef
    row = {"e": str(Fr(e)), "ell": None if ef == 0 else 1 / ef, "y_s": ys, "y_star": yst,
           "frac": None if yst is None else yst / ys, "yK": {str(f): yK[f] for f in KF},
           "K_ratio": None if yst is None else kret_throat(U(yst), ef) / S5.k_bs(ef, 2.0, yst),
           "rho_m": None if yst is None else rho(yst),
           "rho_m_rs": None if (yst is None or ef == 0) else rho(yst) / (3 * ef),
           # interior extremes, not the grid's start (w_th ~ y/2 and a~ ~ -(RR/12) y^3 near the plane)
           "n_grid": int(len(gall)), "w_th_pos_all": bool(np.all(wth_all > 0)), "at_neg_all": bool(np.all(at_all < 0)),
           "w_th_over_y_min": float(np.min(wth_all / gall)), "at_over_y3_max": float(np.max(at_all / gall**3)),
           "cons_rel": float(np.max(np.abs(cons) / scale)), "mom": float(np.max(np.abs(mom))),
           "ham": float(np.max(np.abs(ham))), "reached": tb["reached_alpha0"],
           "W1_026": float(W1(0.26)) if 0.26 < ye else None, "W1_1088": float(W1(1.088)) if 1.088 < ye else None}
    if yst is not None:
        u = U(yst)
        row["level_set"] = {"rho": float(u[2] + 2 * u[3]), "rho_plus_pr": 0.0, "rho_plus_pth": float(u[3] - u[2])}
        band = np.linspace(yst, ye * (1 - 1e-6), 1500)
        row["rho_m_band_max"] = float(np.max(np.array([rho(z) for z in band])))
        # the O(x) expansion's range: x max(|a1|, |b1|, |c1|) <= 0.1, at y* and at the band's midpoint
        row["x_O1_ystar"] = x_valid(tb, yst)
        row["x_O1_mid"] = x_valid(tb, (yst + ye) / 2)
    return row


O1_BOUND = 0.1                   # the O(x) expansion is taken to hold while x max(|a1|, |b1|, |c1|) <= 0.1


def x_valid(tb, y):
    """The largest x = r - 2m (the column's areal coordinate, not a separation) at which the first correction stays
    small at depth y: x max(|a1|, |b1|, |c1|) <= O1_BOUND (physics verifier)."""
    u = tb["sol"].sol(y)
    return float(O1_BOUND / max(abs(u[4]), abs(u[5]), abs(u[6])))


def _ystar_or_nan(tb):
    yst, _ = _ystar(tb)
    return float("nan") if yst is None else yst


def _rho_at_ystar(e):
    tb = throat_bulk(e)
    yst = _ystar_or_nan(tb)
    if not math.isfinite(yst):
        return float("nan")
    u = tb["sol"].sol(yst)
    return float(u[2] + 2 * u[3] - 3 * float(e))


def _rho_band_max(e):
    tb = throat_bulk(e)
    yst = _ystar_or_nan(tb)
    if not math.isfinite(yst):
        return float("nan")
    s, ye = tb["sol"], tb["y_end"]
    band = np.linspace(yst, ye * (1 - 1e-6), 1500)
    V = s.sol(band)
    return float(np.max(V[2] + 2 * V[3] - 3 * float(e)))


def _edge_minus_yK(e, f):
    tb = throat_bulk(e)
    yst, yk = _ystar_or_nan(tb), _yK(tb, f)
    return float("nan") if yk is None else yst - yk


def ell_w(band=False):
    """ell_W: rho_m(y*) >= 0 iff ell >= ell_W (band=True: the maximum of rho_m over [y*, y_s)).  nan (never a crash)
    when y* does not exist at an end of the bracket or the bracket holds no sign change."""
    fn = _rho_band_max if band else _rho_at_ystar
    f0, f1 = fn(1e-4), fn(0.05)
    if not (math.isfinite(f0) and math.isfinite(f1)) or f0 * f1 > 0:
        return float("nan"), float("nan")
    ew = brentq(fn, 1e-4, 0.05, xtol=1e-10)
    return 1 / ew, ew


def ell_c(f):
    """ell_c(f): the band's shallow edge lies below f K_bs (y* < y_K(f)) iff ell > ell_c(f); None if never; nan when y*
    or y_K(f) does not exist at an end of the bracket."""
    g0 = _edge_minus_yK(1e-6, f)
    g1 = _edge_minus_yK(2.0, f)
    if not (math.isfinite(g0) and math.isfinite(g1)):
        return float("nan"), g0
    if g0 * g1 > 0:
        return None, g0
    ec = brentq(lambda e: _edge_minus_yK(e, f), 1e-6, 2.0, xtol=1e-10)
    return 1 / ec, g0


def throat_table(es=ES2, thresholds=True):
    """S8's table over ES2, ell_W (at y* and over the band) and ell_c(10, 30, 100)."""
    out = {"rows": [throat_row(e) for e in es]}
    if thresholds:
        out["ell_W"], out["e_W"] = ell_w()
        out["ell_W_band"], _ = ell_w(band=True)
        out["ell_c"] = {str(f): ell_c(f)[0] for f in KF}
        out["edge_minus_yK10_flat"] = _edge_minus_yK(1e-6, 10)
    return out


# ------------------------------------------------------------------------------------------------ S7 down the throat
DT_LAMS = (0.1, 0.25, 0.4)           # f = c x^lam with 0 < lam < 1/2
DT_LAM_CONTROL = 0.75                # the control, lam in (1/2, 1): must violate the radial NEC
DT_C = 0.05
DT_FRACS = (0.01, 0.25, 0.5, 0.75, 0.9)                 # sample depths, as fractions of y_s^th
DT_XS = tuple(10.0 ** k for k in range(-14, -2))        # x = r - 2m from 1e-14 to 1e-3 (capped at x_O1(depth))


def _graph_k(u, xv, F1, F2):
    """Exact mixed extrinsic curvature (k_t, k_x, k_th) of the static graph y = depth + F(x), normal into the slab
    (n_mu = -(dy - F' dx)/N, N = sqrt(1 + F'^2/B)), in the throat metric to first order in x taken as exact:
    A = (x/2) alpha^2 (1 + x a1), B = (alpha^2/x^2)(1 + x b1), C = 4 beta^2 (1 + x c1), with the fields
    u = (alpha, beta, p, q, a1, b1, c1, a1', b1', c1') at y = depth + F(x); F1 = F'(x), F2 = F''(x).
      k_t  = [-kappa_t + F' d_x ln A/(2B)]/N,   k_th = [-kappa_th + F' d_x ln C/(2B)]/N,
      k_x  = [F'' - B kappa_x - F'(d_x ln B/2 + 2 F' kappa_x)]/(N (B + F'^2)).
    (Cross-checked against a brute-force 5D projection with generic A, B, C to 1e-16 in the build's scratch.)"""
    al, be, p, q, a1, b1, c1, da, db, dc = (mp.mpf(float(v)) for v in u)
    x, F1, F2 = mp.mpf(xv), mp.mpf(F1), mp.mpf(F2)
    B = al**2 / x**2 * (1 + x * b1)
    kap_t = p + x * da / (2 * (1 + x * a1))
    kap_x = p + x * db / (2 * (1 + x * b1))
    kap_q = q + x * dc / (2 * (1 + x * c1))
    dlA, dlB, dlC = 1 / x + a1 / (1 + x * a1), -2 / x + b1 / (1 + x * b1), c1 / (1 + x * c1)
    N = mp.sqrt(1 + F1**2 / B)
    kt = (-kap_t + F1 * dlA / (2 * B)) / N
    kq = (-kap_q + F1 * dlC / (2 * B)) / N
    kx = (F2 - B * kap_x - F1 * (dlB / 2 + 2 * F1 * kap_x)) / (N * (B + F1**2))
    return kt, kx, kq


def down_throat_class(e, tb=None, lams=DT_LAMS, c=DT_C, fracs=DT_FRACS):
    """S7's asymptotic class, corrected (physics verifier, REFUTED item): a static piece y = depth + f, f > 0, f -> 0 as
    x -> 0, so that its infimum depth is approached only down the throat.  With u = ln x the radial NEC along the
    approach is

        f'' - f'/2 <= alpha^2 x W1(depth)        (' = d/du; first order in x and in the slope)

    -- the f'/2 is the lapse-gradient term n^u (1/2) d_u ln A (the static observers' acceleration), which the first
    build's f_ss <= x W1(depth) dropped.  Its homogeneous solutions are 1 and e^(u/2) (the lapse).  This function
    computes, and leaves the interpretation to the note:
      (i)   f = c x^lam, 0 < lam < 1/2: the radial and angular NEC (k_t - k_x >= 0, k_t - k_th >= 0, the local Israel
            lemma) of the graph, exact in the slope, on this ell's throat metric through O(x) (_graph_k), at depths
            fracs x y_s^th and x from 1e-14 to min(1e-3, x_O1(depth)); with the leading-order prediction
            k_t - k_x ~ x W1 + (f'/2 - f'')/alpha^2 at the graph's point.  The lapse term c lam (1/2 - lam) x^lam/alpha^2
            dominates as x -> 0; where W1(depth) < 0 the x W1 term overtakes it above the crossover
            x_c = [c lam (1/2 - lam)/(alpha^2 |W1|)]^(1/(1 - lam)), so the check is that every sample below x_c/2 holds
            and that any failure lies above x_c/2 (the profile is the class's approach x -> 0; above x_c the piece must
            bend otherwise, and the NEC still constrains how: SIM2-FACING.md S7, deduced by the re-verifier);
      (ii)  the control lam = 3/4 (must violate the radial NEC as x -> 0 at every depth), and the first build's dropped-
            term condition f'' <= alpha^2 x W1(depth), which excludes every convex f at depths where W1 < 0 (an identity
            below y*, where W1 < 0 by y*'s definition);
      (iii) the umbilic (matter-free) member, an illustration: the radial equality f'' - f'/2 = alpha^2 x W1(depth)
            with f -> 0 forces f' -> 0 (deduced, the adjudication; f = c sqrt(x) + 2 alpha^2 W1 x), so k_t - k_th ->
            w_th(depth) = q - p > 0 and umbilicity (k_t = k_x = k_th) fails.  It is evaluated at x = 1e-14, where the
            slope terms are below 1e-7, so k_t - k_th -> q - p there for any f -> 0: an identity, not a test of the
            radial equation.  The trace reading -ell (k_t + k_x + 2 k_th)/4 -> ell a(depth) is checked
            (trace_minus_ell_a)."""
    tb = tb if tb is not None else throat_bulk(e)
    s, ys, ye, ef = tb["sol"], tb["y_s"], tb["y_end"], tb["e"]
    yst, W1 = _ystar(tb)
    mp.mp.dps = 30
    out = {"e": str(Fr(e)), "y_star": yst, "lams": list(lams), "c": c, "depths": [], "n": 0, "n_below_xc": 0,
           "n_fail": 0}
    good_ok, ctrl_ok, consistent, dev = True, True, True, 0.0
    old_excl, fail_over_xc = 0, []
    for fr in fracs:
        dep = fr * ys
        u0 = s.sol(dep)
        al2, w1 = float(u0[0]) ** 2, float(W1(dep))
        xmax = min(1e-3, x_valid(tb, dep))
        xs = [xv for xv in DT_XS if xv <= xmax]
        rec = {"depth": dep, "frac": fr, "W1": w1, "below_ystar": bool(yst is not None and dep < yst), "x_max": xmax,
               "rad_min_below_xc": math.inf, "ang_min": math.inf, "x_c": {}, "first_fail": {},
               "ctrl_rad_at_xmin": None, "old_violated": False}
        for lam in tuple(lams) + (DT_LAM_CONTROL,):
            xc = math.inf if w1 >= 0 else (c * lam * (0.5 - lam) / (al2 * abs(w1))) ** (1 / (1 - lam))
            first_fail = None
            for xv in xs:
                F = c * xv**lam
                if dep + F >= ye * (1 - 1e-6):
                    continue
                F1, F2 = c * lam * xv**(lam - 1), c * lam * (lam - 1) * xv**(lam - 2)
                ug = s.sol(dep + F)
                kt, kx, kq = _graph_k(ug, xv, F1, F2)
                rad, ang = float(kt - kx), float(kt - kq)
                fu, fuu = c * lam * xv**lam, c * lam**2 * xv**lam
                if lam == DT_LAM_CONTROL:
                    if xv == xs[0]:
                        rec["ctrl_rad_at_xmin"] = rad
                        ctrl_ok = ctrl_ok and rad < 0
                    continue
                out["n"] += 1
                ok_here = rad >= 0 and ang >= 0
                rec["ang_min"] = min(rec["ang_min"], ang)
                if xv <= xc / 2:
                    out["n_below_xc"] += 1
                    rec["rad_min_below_xc"] = min(rec["rad_min_below_xc"], rad)
                    good_ok = good_ok and ok_here
                if not ok_here:
                    out["n_fail"] += 1
                    if first_fail is None:
                        first_fail = xv
                pred = xv * float(W1(dep + F)) + (fu / 2 - fuu) / float(ug[0]) ** 2
                if xv <= 1e-8:
                    dev = max(dev, abs(rad / pred - 1))
                if fuu > al2 * xv * w1:                       # the first build's condition (lapse term dropped)
                    rec["old_violated"] = True
            if lam != DT_LAM_CONTROL:
                rec["x_c"][str(lam)] = xc
                rec["first_fail"][str(lam)] = first_fail
                if first_fail is not None:
                    consistent = consistent and first_fail > xc / 2
                    fail_over_xc.append(first_fail / xc)
        old_excl += bool(rec["old_violated"] and rec["below_ystar"])
        # (iii) the umbilic member at this depth
        cu = c
        xu = DT_XS[0]
        Fu = cu * math.sqrt(xu) + 2 * al2 * w1 * xu
        F1u = cu / (2 * math.sqrt(xu)) + 2 * al2 * w1
        F2u = -cu / (4 * xu**1.5)
        kt, kx, kq = _graph_k(s.sol(dep + Fu), xu, F1u, F2u)
        wth = float(u0[3] - u0[2])
        rec["umbilic"] = {"kt_minus_kth": float(kt - kq), "w_th": wth, "ratio": float(kt - kq) / wth,
                          "kt_minus_kx_over_w_th": float(kt - kx) / wth,
                          "trace_read": None if ef == 0 else float(-(kt + kx + 2 * kq) / 4) / ef,
                          "ell_a": None if ef == 0 else float((u0[2] + u0[3]) / 2) / ef,
                          "a": float((u0[2] + u0[3]) / 2)}
        out["depths"].append(rec)
    um = [r_["umbilic"] for r_ in out["depths"]]
    out.update({"nec_holds": good_ok, "fails_only_above_xc": consistent,
                "fail_over_xc": [min(fail_over_xc), max(fail_over_xc)] if fail_over_xc else None,
                "control_fails": ctrl_ok, "lead_dev": dev, "old_excludes_below_ystar": old_excl,
                "n_below_ystar": sum(r_["below_ystar"] for r_ in out["depths"]),
                "umbilic_closes": all(v["w_th"] > 0 and abs(v["ratio"] - 1) < 1e-2 and abs(v["kt_minus_kx_over_w_th"]) < 1e-2
                                      for v in um),
                "umbilic_ratio_dev": max(abs(v["ratio"] - 1) for v in um),
                "umbilic_radial_dev": max(abs(v["kt_minus_kx_over_w_th"]) for v in um),
                "ell_a_max": None if ef == 0 else max(v["ell_a"] for v in um),
                "trace_minus_ell_a": None if ef == 0 else max(abs(v["trace_read"] - v["ell_a"]) for v in um)})
    return out


def _rho_class_max(e, detail=False):
    """The down-the-throat class's best energy at e = m/ell.  A piece whose nearest approach to depth y is reached only
    down the throat carries, as x -> 0, the level-set stress at that depth (its slope terms vanish), so its matter tends
    to rho_m = nu (p + 2q - 3/ell)(y).  The class has no lower edge in the approach (S7), so this is the maximum over
    every depth in (0, y_end), in nu/m.  detail=True also returns the best depth as a fraction of y_s^th and of y*, and
    K/K_bs there."""
    tb = throat_bulk(e)
    s, ys, ye, ef = tb["sol"], tb["y_s"], tb["y_end"], tb["e"]
    g = np.linspace(1e-6 * ye, ye * (1 - 1e-6), 3000)
    V = s.sol(g)
    i = int(np.argmax(V[2] + 2 * V[3] - 3 * ef))
    neg = lambda z: -float(s.sol(z)[2] + 2 * s.sol(z)[3] - 3 * ef)
    res = minimize_scalar(neg, bounds=(g[max(i - 1, 0)], g[min(i + 1, len(g) - 1)]), method="bounded",
                          options={"xatol": 1e-12})
    zb, rb = float(res.x), float(-res.fun)
    if not detail:
        return rb
    yst, _ = _ystar(tb)
    return {"rho_m_max": rb, "frac_ys": zb / ys, "frac_ystar": None if yst is None else zb / yst,
            "K_ratio": float(kret_throat(s.sol(zb), ef) / S5.k_bs(ef, 2.0, zb))}


def ell_w_class():
    """Positive energy in the down-the-throat class: the maximum over depth of the limiting rho_m is >= 0 iff ell >= this
    threshold (the adjudication: on the profiles the slope correction to rho, -f''/alpha^2, is negative, so at finite x
    the threshold is strict).  nan, never a crash, when the bracket holds no sign change."""
    nan = float("nan")
    f0, f1 = _rho_class_max(1e-4), _rho_class_max(0.1)
    if not (math.isfinite(f0) and math.isfinite(f1)) or f0 * f1 > 0:
        return {"ell": nan, "e": nan}
    ew = brentq(_rho_class_max, 1e-4, 0.1, xtol=1e-10)
    out = _rho_class_max(ew, detail=True)
    out.update({"ell": 1 / ew, "e": ew, "flat": _rho_class_max(0.0, detail=True)})
    return out


def depth_zero(e):
    """The down-the-throat class approaching depth 0 (first read as the board's H-COINCIDE-AS-LIMIT; since item 172 the
    coincidence of M's H-COINCIDE-DOWN-THE-THROAT, which S15 computes along the approach).  At
    y = 0 the throat data are alpha = beta = 1, p = q = -1/ell, so the limiting stress reads rho = nu (p + 2q) =
    -sigma_RS and rho_m = -2 sigma_RS at every finite ell (deduced); K/K_bs = 2(80 e^4 + 3)/(160 e^4 + 3) <= 2."""
    ef = float(e)
    u0 = [1.0, 1.0, -ef, -ef]
    return {"rho_m_rs": None if ef == 0 else (u0[2] + 2 * u0[3] - 3 * ef) / (3 * ef),
            "K_ratio": float(kret_throat(u0, ef) / S5.k_bs(ef, 2.0, 0.0)),
            "K_closed": 2 * (80 * ef**4 + 3) / (160 * ef**4 + 3)}


# ------------------------------------------------------------------------------------------------ S9 the map
def _mpc(c):
    return [mp.mpf(v.numerator) / v.denominator for v in reversed(c)]


def _dco(pp):
    n = len(pp) - 1
    return [c * (n - i) for i, c in enumerate(pp[:-1])] or [mp.mpf(0)]


def raw_rational(c, o):
    """Raw Pade (b4_static.pade through b4d_stage5._approx) of a warp-divided series: value and log-derivative
    p'/p - q'/q, with no doublet removal; and its real roots in (0, CAP] split into Froissart doublets and the rest."""
    p, q = S5._approx(c, o)
    pp, qq = _mpc(p), _mpc(q)
    dp, dq = _dco(pp), _dco(qq)
    rp = np.roots([float(v) for v in reversed(q)]) if len(q) > 1 else np.array([])
    rz = np.roots([float(v) for v in reversed(p)]) if len(p) > 1 else np.array([])
    real = lambda z: abs(z.imag) < 1e-8 * max(1.0, abs(z)) and 0 < z.real <= CAP
    near = lambda z, pool: len(pool) and min(abs(z - w) for w in pool) < DOUBLET * max(1.0, abs(z))
    block = sorted([z.real for z in rp if real(z) and not near(z, rz)] + [z.real for z in rz if real(z) and not near(z, rp)])
    doublets = sorted(z.real for z in rp if real(z) and near(z, rz))
    return {"val": lambda y: mp.polyval(pp, mp.mpf(y)) / mp.polyval(qq, mp.mpf(y)),
            "ld": lambda y: (mp.polyval(dp, mp.mpf(y)) / mp.polyval(pp, mp.mpf(y))
                             - mp.polyval(dq, mp.mpf(y)) / mp.polyval(qq, mp.mpf(y))),
            "block": block[0] if block else math.inf, "doublets": doublets}


def _w_at(Rs, y):
    lA, lB, lC = (Rs[X]["ld"](y) for X in "ABC")
    return float((lB - lA) / 2), float((lC - lA) / 2), float((lA + lB + 2 * lC) / 8)


def pade_orders(N, e):
    """The three Pade orders.  At e != 0, b4d_stage5.orders(N).  At e = 0 (ell = inf) the bulk is even in y, so the series
    holds only even powers and stage 5's (N/2 - 1, N/2) and (N/2 - 2, N/2 + 1) are one approximant ([N/4 - 1 / N/4] in
    y^2; numerics verifier): the three-order checks would rest on two.  There the orders are (N/2 - 2, N/2), (N/2, N/2),
    (N/2, N/2 - 2), three distinct approximants; the verification pair (the first two) is the same two approximants as
    before."""
    if Fr(e) == 0:
        return [(N // 2 - 2, N // 2), (N // 2, N // 2), (N // 2, N // 2 - 2)]
    return S5.orders(N)


def column_w(rc, e, N=ORDER, ngrid=NGRID, with_k=True):
    """One owner column: raw Pade of A~, B~, C~ at pade_orders(N, e); w_r, w_th, a~ on a 40-point y grid up to the scan
    top.  VERIFIED (the prefix): two orders agree on A, B, C to 1e-4, all positive, no real non-doublet pole or zero of
    the two orders below y -- b4_static S3's value rule, and nothing else.  ADMISSIBLE: verified, the two orders agree
    on the SIGN of w_r and of w_th (sign_ok), and both are >= 0 at both orders.  The first build's w-agreement rule
    (|w_o0 - w_o1| <= 1e-6 + 1e-3 |w|) is kept per point as a diagnostic (w_ok, and its own prefix ver_w and
    admissible set adm_w), never in the verified prefix.  K/K_bs at admissible points through b4d_stage5.evaluator at
    two orders."""
    t0 = time.process_time()
    mp.mp.dps = 40
    r = float(Fr(rc))
    S = B4.series(rc, N, e)
    W = S5.warped(S, e, N)
    ords = pade_orders(N, e)
    sing = [S5.nearest_real(W["C"][0], o) for o in ords]
    ysl = [float(z[0]) for z in sing if z]
    stable = bool(len(ysl) == 3 and (max(ysl) - min(ysl)) / float(np.median(ysl)) < 0.05)
    R = {o: {X: raw_rational(W[X][0], o) for X in "ABC"} for o in ords}
    block = min(R[o][X]["block"] for o in ords[:2] for X in "ABC")
    doublets = sorted({round(z, 4) for o in ords[:2] for X in "ABC" for z in R[o][X]["doublets"]})

    def point(y):
        vals = [[R[o][X]["val"](y) for X in "ABC"] for o in ords[:2]]
        okv = (y < block and all(v > 0 for row in vals for v in row)
               and all(abs(a - b) <= VAL_TOL * abs(b) for a, b in zip(vals[0], vals[1])))
        w = [_w_at(R[o], y) for o in ords]
        okw = all(abs(w[0][i] - w[1][i]) <= W_ABS + W_REL * abs(w[1][i]) for i in (0, 1))
        sign_ok = all(w[0][i] * w[1][i] > 0 for i in (0, 1))
        return okv, okw, sign_ok, w

    if stable:
        top = min(0.95 * float(np.median(ysl)), CAP)
    else:
        top = 0.0
        for y in np.linspace(CAP / 200, CAP, 200):
            okv, _, _, _ = point(float(y))
            if not okv:
                break
            top = float(y)
    grid = [top * k / ngrid for k in range(1, ngrid + 1)] if top > 0 else []
    rows, prefix, prefix_w = [], True, True
    for y in grid:
        okv, okw, sign_ok, w = point(y)
        prefix = prefix and okv
        prefix_w = prefix_w and okv and okw
        nonneg = all(w[i][0] >= 0 and w[i][1] >= 0 for i in (0, 1))
        rows.append({"y": y, "wr": w[1][0], "wth": w[1][1], "at": w[1][2],
                     "wr_spread": max(abs(w[i][0] - w[j][0]) for i in range(3) for j in range(3)),
                     "val_ok": okv, "w_ok": okw, "sign_ok": sign_ok, "ver": prefix, "adm": prefix and sign_ok and nonneg,
                     "ver_w": prefix_w, "adm_w": prefix_w and nonneg})
    ver = [z for z in rows if z["ver"]]
    vtop = ver[-1]["y"] if ver else 0.0
    # sign changes of w_r over the verified, sign-settled points (both directions; the first rising one is wr_zero)
    settled = [z for z in ver if z["sign_ok"]]
    f = lambda yy: float((R[ords[1]]["B"]["ld"](yy) - R[ords[1]]["A"]["ld"](yy)) / 2)
    wr_zeros = []
    for z0, z1 in zip(settled, settled[1:]):
        if (z0["wr"] < 0) != (z1["wr"] < 0):
            wr_zeros.append([float(brentq(f, z0["y"], z1["y"], xtol=1e-10)), 1 if z1["wr"] >= 0 else -1])
    rising = [z for z, s in wr_zeros if s > 0]
    wr_zero = rising[0] if rising else None
    kk = []
    adm = [z for z in rows if z["adm"]]
    if with_k and adm:
        Ks = [S5.evaluator(W, e, o)[0] for o in ords[:2]]
        pick = adm if len(adm) <= 12 else [adm[int(round(i * (len(adm) - 1) / 11))] for i in range(12)]
        for z in pick:
            kb = S5.k_bs(e, r, z["y"])
            kk.append([z["y"], Ks[0](z["y"]) / kb, Ks[1](z["y"]) / kb])
    return {"rc": rc, "r": r, "e": str(Fr(e)), "N": N, "orders": [list(o) for o in ords], "ys": ysl,
            "ys_im": [float(z[1]) for z in sing if z], "ys_stable": stable, "top": top,
            "block": None if block == math.inf else block, "doublets": doublets, "rows": rows, "vtop": vtop,
            "vtop_w": max([z["y"] for z in rows if z["ver_w"]], default=0.0), "wr_zero": wr_zero, "wr_zeros": wr_zeros,
            "kk": kk, "cost_s": time.process_time() - t0}


def _job(args):
    rc, es = args
    return column_w(rc, Fr(es))


def regenerate(procs=3):
    """S9 over RADII2 x ES2 at order 32 (multiprocessing.Pool(3)), and S8's table; writes sim2_bank.json."""
    jobs = [(rc, str(e)) for e in ES2 for rc in RADII2]
    jobs.sort(key=lambda j: (float(Fr(j[0])) > 2.05, -float(Fr(j[1]))))   # near-throat and steep columns first
    t0 = time.monotonic()
    with Pool(procs) as pool:
        cols = pool.map(_job, jobs, chunksize=1)
    table = throat_table()
    bank = {"note": "regenerated by lemmas/sim2_facing.py --regenerate", "N": ORDER, "radii": RADII2,
            "es": [str(e) for e in ES2], "grid": NGRID, "val_tol": VAL_TOL, "w_tol": [W_ABS, W_REL],
            "w_tol_role": "diagnostic only (w_ok, ver_w, adm_w); the verified prefix is the value rule, admissibility "
                          "needs sign_ok",
            "columns": {"%s|%s" % (c["rc"], c["e"]): c for c in cols}, "throat": table,
            "wall_s": time.monotonic() - t0}
    json.dump(bank, open(BANK, "w"), separators=(",", ":"), default=float)
    return bank


def load_bank():
    return json.load(open(BANK))


def admissible(bank, key="adm"):
    """The admissible set per ell: (r_c, r, y) with w_r >= 0, w_th >= 0 at two orders that agree on their signs, at a
    value-verified point.  key = 'adm_w' gives the first build's rule (the w-agreement prefix), a diagnostic."""
    out = {}
    for es in bank["es"]:
        out[es] = [(c["rc"], c["r"], z["y"]) for k, c in bank["columns"].items() if c["e"] == es
                   for z in c["rows"] if z[key]]
    return out


def map_summary(bank):
    """S9's statements over the verified points: signs of w_r, w_th, a~ by class of column.  The sign of w_r is counted
    only where the two orders agree on it (sign_ok); w_th and a~ over every verified point."""
    cols = list(bank["columns"].values())
    far = [(c, z) for c in cols for z in c["rows"] if z["ver"] and (c["r"] >= 2.05 or Fr(c["e"]) >= Fr(1, 2))]
    far_s = [(c, z) for c, z in far if z["sign_ok"]]
    allv = [(c, z) for c in cols for z in c["rows"] if z["ver"]]
    alls = [(c, z) for c, z in allv if z["sign_ok"]]
    pos = sorted({(c["rc"], c["e"]) for c, z in alls if z["wr"] >= 0}, key=lambda v: (Fr(v[1]), Fr(v[0])))
    far_pos = sorted({(c["rc"], c["e"]) for c, z in far_s if z["wr"] >= 0}, key=lambda v: (Fr(v[1]), Fr(v[0])))
    return {"n_ver": len(allv), "n_ver_settled": len(alls), "n_far": len(far), "n_far_settled": len(far_s),
            "far_wr_neg": sum(z["wr"] < 0 for _, z in far_s), "far_wr_pos": sum(z["wr"] >= 0 for _, z in far_s),
            "far_wth_pos": sum(z["wth"] > 0 for _, z in far), "far_at_neg": sum(z["at"] < 0 for _, z in far),
            "at_max": max(z["at"] for _, z in allv), "wth_min": min(z["wth"] for _, z in allv), "wr_pos_cols": pos,
            "far_wr_pos_cols": far_pos,
            "wth_nonpos": sorted([(c["rc"], c["e"], z["y"], z["wth"], z["sign_ok"], z["wr"]) for c, z in allv
                                  if z["wth"] <= 0],
                                 key=lambda v: (Fr(v[1]), Fr(v[0]), v[2])),
            "unsettled": sum(1 for _, z in allv if not z["sign_ok"]),
            # the first build's w-agreement rule, as a diagnostic
            "w_disagree": sum(1 for c in cols for z in c["rows"] if z["ver"] and not z["w_ok"]),
            "n_ver_w": sum(1 for c in cols for z in c["rows"] if z["ver_w"]),
            "n_adm": sum(1 for c in cols for z in c["rows"] if z["adm"]),
            "n_adm_w": sum(1 for c in cols for z in c["rows"] if z["adm_w"])}


# ------------------------------------------------------------------------------------------------ S11 Lemma N
def lemma_n(sign=-1):
    """Gamma^y_ab = sign (1/2) d_y g_ab is checked (sign = -1 is the true connection; +1 is the mutation), and the
    radial null ray tangent to a level set: y'' = -Gamma^y_tt t'^2 - Gamma^y_rr r'^2 with t'^2 = B r'^2/A, against
    w_r B r'^2.  Corollary W: a warped product has kappa_t = kappa_r = kappa_th."""
    y, t, r, th, ph, rdot = sp.symbols("y t r theta phi rdot", real=True)
    A, B, C = (sp.Function(n)(y, r) for n in "ABC")
    g = [sp.Integer(1), -A, B, C, C * sp.sin(th)**2]
    X = [y, t, r, th, ph]
    _, _, Gm = _ricci_diag(g, X)
    conn = all(sp.simplify(Gm(0, i, i) - sign * sp.Rational(1, 2) * sp.diff(g[i], y)) == 0 for i in range(1, 5))
    G = (lambda a_, b_, c_: sign * sp.Rational(1, 2) * sp.diff(g[b_], y) if (a_ == 0 and b_ == c_ and b_ > 0)
         else Gm(a_, b_, c_))
    tdot2 = B * rdot**2 / A
    ydd = -G(0, 1, 1) * tdot2 - G(0, 2, 2) * rdot**2
    w_r = (sp.diff(B, y) / B - sp.diff(A, y) / A) / 2
    ray = sp.simplify(ydd - w_r * B * rdot**2)
    f, F, H = sp.Function("f")(y), sp.Function("F")(r), sp.Function("H")(r)
    gw = [sp.exp(2 * f) * F, sp.exp(2 * f) / H, sp.exp(2 * f) * r**2]
    kap = [sp.simplify(sp.diff(v, y) / (2 * v)) for v in gw]
    return {"connection": conn, "ray": ray, "warped_w": [sp.simplify(kap[1] - kap[0]), sp.simplify(kap[2] - kap[0])]}


# ------------------------------------------------------------------------------------------------ C11 exact controls
def schwarzschild_control(rc="3", e=Fr(1), N=16):
    """Schwarzschild data: the warp-divided series terminates (the black string), so w_r = w_th = a~ = 0 exactly."""
    S = B4.series(rc, N, e, data=B4._schwarzschild)
    W = S5.warped(S, e, N)
    term = all(W[X][0][k] == 0 for X in "ABC" for k in range(1, N + 1))
    kap = {}
    for X in "ABC":
        c = [Fr(v) for v in S[X][0][:N + 1]]
        kap[X] = [v / 2 for v in _div(_deriv(c), c, N - 1)]
    wr = all(kap["B"][j] - kap["A"][j] == 0 for j in range(N))
    wth = all(kap["C"][j] - kap["A"][j] == 0 for j in range(N))
    at = all((kap["A"][j] + kap["B"][j] + 2 * kap["C"][j]) / 4 + (Fr(e) if j == 0 else 0) == 0 for j in range(N))
    return {"terminates": term, "w_r": wr, "w_th": wth, "at": at}


def wedge(warp="cosh"):
    """The AdS4-sliced wedge d rho^2 + cosh^2(rho/ell) g4 (g4 AdS4 of radius ell, Poincare chart): Einstein with
    Lambda_5 = -6/ell^2; a = tanh((y - rho*)/ell)/ell along y = rho + rho*; P1 at y = 0 reads s1 = tanh(rho*/ell), and a
    facing sheet at y = 2 rho* reads s2 = s1 (T5 equality).  warp = 'sinh' is the mutation."""
    rho, t, x1, x2, z = sp.symbols("rho t x1 x2 z", real=True)
    ell = sp.Symbol("ell", positive=True)
    c2 = (sp.cosh(rho / ell) if warp == "cosh" else sp.sinh(rho / ell))**2
    h = ell**2 / z**2
    g = [sp.Integer(1), -c2 * h, c2 * h, c2 * h, c2 * h]
    X = [rho, t, x1, x2, z]
    R, gi, _ = _ricci_diag(g, X)
    einstein = [sp.simplify(gi[i] * R(i, i) + 4 / ell**2) for i in range(5)]
    a = sp.simplify(sp.diff(c2, rho) / (2 * c2))
    u = sp.Symbol("u", positive=True)                                  # u = rho*/ell
    s1 = sp.simplify(-ell * a.subs(rho, -u * ell))
    s2 = sp.simplify(ell * a.subs(rho, u * ell))
    bound = sp.tanh(2 * u - sp.atanh(s1))
    num = ([abs(float(bound.subs(u, v)) - float(s2.subs(u, v))) for v in (0.1, 0.5, 1.3)] if warp == "cosh"
           else [float("nan")])
    return {"einstein": einstein, "a": a, "s1": s1, "s2": s2, "equal": sp.simplify(s2 - s1) == 0,
            "bound_gap": max(num)}


# ------------------------------------------------------------------------------------------------ S12 decision
def decide(bank, table):
    """Per ell: WIDE (an admissible verified point at r_c >= 2.1m), THROAT-BAND (y* < y_s^th, every admissible point at
    r_c < 2.1m; qualified CONFIRMED / EXPANSION-ONLY, regular at 10/30/100 K_bs, the strict y < y_s, WEC), NONE (no
    zero of W1 before y_s^th and no admissible point), else UNDECIDED.
    WIDE is decided on the VERIFIED points only: per ell, 'unverified_wide' records each column at r_c >= WIDE_R whose
    verified top lies below its Pade singular depth (median of the three orders' nearest real singularity of C~, where
    the three agree to 5%; the 10m scan cap otherwise), i.e. the depths at which this map cannot tell 'no admissible
    point' from 'not verified'.
    CONFIRMED compares an owner column's first rising sign change of w_r (x > 0) with the THROAT's y* (x -> 0); the
    offset is the O(x) shift, which S10's extrapolation to x -> 0 removes.  The first build's w-agreement rule is
    reported alongside as a diagnostic (n_adm_w, confirmed_w), never decisive."""
    adm = admissible(bank)
    adm_w = admissible(bank, "adm_w")
    rows = {r_["e"]: r_ for r_ in table["rows"]}
    out = {}
    for es in bank["es"]:
        row = rows[es]
        A = adm[es]
        wide = [a for a in A if a[1] >= WIDE_R]
        ys_, yst = row["y_s"], row["y_star"]
        d = {"y_s": ys_, "y_star": yst, "n_adm": len(A), "wide": wide[:5], "n_adm_w": len(adm_w[es])}
        if wide:
            d["class"] = "WIDE"
        elif yst is not None and yst < ys_:
            d["class"] = "THROAT-BAND"
        elif not A:
            d["class"] = "NONE"
        else:
            d["class"] = "UNDECIDED"
        far = sorted([c for c in bank["columns"].values() if c["e"] == es and c["r"] >= WIDE_R], key=lambda c: c["r"])
        unv = []
        for c in far:
            # the Pade singular depth only where the three orders agree on it (ys_stable); else the scan cap
            ysing = min(float(np.median(c["ys"])), CAP) if (c["ys"] and c["ys_stable"]) else None
            upper = ysing if ysing is not None else CAP
            if upper > c["vtop"] + 1e-9:
                unv.append((c["rc"], round(c["vtop"], 4), round(upper, 4), ysing is not None))
        d["unverified_wide"] = unv
        near = [c for c in bank["columns"].values() if c["e"] == es and c["r"] < WIDE_R]
        d["not_reached"] = sorted([(c["rc"], round(c["vtop"], 4)) for c in near
                                   if yst is not None and c["vtop"] < yst], key=lambda v: Fr(v[0]))
        conf, conf_w = [], []
        for c in near:
            if c["r"] <= NEAR_R + 1e-12 and any(z["adm"] for z in c["rows"]) and yst:
                edge = c["wr_zero"] if c["wr_zero"] is not None else min(z["y"] for z in c["rows"] if z["adm"])
                conf.append((c["rc"], edge, abs(edge - yst) / yst))
            if c["r"] <= NEAR_R + 1e-12 and any(z["adm_w"] for z in c["rows"]) and yst:
                edge = min(z["y"] for z in c["rows"] if z["adm_w"])
                conf_w.append((c["rc"], edge, abs(edge - yst) / yst))
        conf.sort(key=lambda v: v[2])
        conf_w.sort(key=lambda v: v[2])
        d["confirm"] = conf
        d["confirmed"] = bool(conf and conf[0][2] <= CONFIRM_TOL)
        d["confirm_against"] = "the throat's y* (x -> 0); the offset is the O(x) shift (S10's extrapolation removes it)"
        d["confirmed_w"] = bool(conf_w and conf_w[0][2] <= CONFIRM_TOL)
        if yst is not None:
            d["regular"] = {str(f): bool(row["yK"][str(f)] is not None and yst < row["yK"][str(f)]) for f in KF}
            d["strict"] = bool(yst < ys_)
            d["settled"] = len(set(d["regular"].values())) == 1
            d["wec"] = bool(row["rho_m"] >= 0)
        out[es] = d
    return out


# ------------------------------------------------------------------------------------------------ S13 hand-off
def delta_rows():
    """At any nearest point the slab side of a facing piece reads s_slab <= ell a(depth) <= -1, with equality for a
    level surface (Lemma C: tr K(P2) >= -4 a(depth), the Hessian adding a non-negative trace; T4).  These s are in
    units of sigma_RS at the slab's ell, which within one universe is ours: stage 7 K4's unit-ell_1 rows (in
    multiplane.py M4's own unit, ell_2, the required s_outer differ; the unit, K4, and the image count, K5, stay put to
    M).  Two-sided sigma_2/sigma_RS = (s_slab + s_outer)/2, so the -1/3 that 139 (1) said yes to (multiplane.py M4's
    figure) needs s_outer >= +1/3 and stage 7 K5's -1/6 needs s_outer >= +2/3 (both positive: the outer side decays,
    K4)."""
    s_slab = Fr(-1)
    need = {str(s2): 2 * s2 - s_slab for s2 in (Fr(-1, 3), Fr(-1, 6))}
    rows = [("(0, 0 | 0)", "EMPTY (S3, T5c; the down-the-throat member too)"),
            ("(0, 0 | NEC)", "attained: the throat band (S12); down the throat: every depth in the approach (S7)"),
            ("(0, 0 | NEC+WEC)", "attained: ell >= ell_W only; down the throat: ell > ell_W^class only, at approach "
                                 "depths >= d_+ > 0, so never coinciding (S15)")]
    return {"s_slab_max": s_slab,
            "s_slab_read": "s_slab <= ell a(depth) <= -1 (equality for a level surface; in the limit down the throat)",
            "unit": "sigma_RS at the slab's ell (ours within one universe: stage 7 K4's unit-ell_1 rows)",
            "s_outer_min": need, "rows": rows,
            "rows_on": "H-SPLIT-AT-OUR-TENSION",
            "on_trace": "on H-LAW-READ-BY-TRACE the NEC rows move to Delta s <= ell a(depth) - 1 < 0 (equality for a "
                        "level surface), phase 3's direction"}


# For the next instrument, sim2_passage (escape E-PASS): anchors two judges reproduced in the design phase, kept internal
# under 119 (the address is the input's) -- not computed here, never printed by this instrument.
PASSAGE_ANCHORS = {"r2_star": "116.34 ... 2.247m", "cycle": "2.75 -> 4.00939 -> 2.75000", "r_star": 3.191934,
                   "Y_max": 1.5946}

ESCAPES = [
    ("E-NS", "non-static (152 (2))", "scheduled as phase 2b-ii, the brief evolution"),
    ("E-ROT", "non-diagonal K (141's internal motion)", "open"),
    ("E-BULK", "Ric(n,n) < -4/ell^2", "T fails; W stands"),
    ("E-ASYM", "P2 not mirrored, with its own outer side", "phase 3"),
    ("E-PASS", "no second sheet; end 2 of our own plane reached through the horizon", "the next instrument, sim2_passage"),
    ("E-G", "global closure of P2", "phase 2b-i"),
    ("E-AN", "outside the analytic class", "open"),
    ("E-Q", "quantum or semiclassical stress violating the pointwise NEC on P2 or in the slab",
     "excluded only by H-NEC-NEVER-VIOLATED (117, 120)"),
    ("E-FAR", "nearest approach reached only as r -> infinity, beyond r = 10m, or beyond a column's verified top, "
              "including the continuation of S7's approach below y*",
     "open; the lapse-gradient term must be kept (cf. S7, down_throat_class)"),
]


# ------------------------------------------------------------------------------------------------ S15 coinciding (172)
# M's item 172 (2), "Yes, that is coinciding": 127's coincidence is the endless approach down the object's throat, never
# a reached point (H-COINCIDE-DOWN-THE-THROAT, M's; it replaces the board's H-FACING-DOWN-THE-THROAT and
# H-COINCIDE-AS-LIMIT).  S15 computes what position 2's piece carries there: S7's class y = depth + f(ln x), the
# approach depth going to 0 and, along the approach, x = r - 2m -> 0 (x is the plane's radial coordinate, not a
# separation).  The approach depth is reported only as where facing (coinciding) occurs.
CO_XS = (1e-4, 1e-8, 1e-14)                 # x along the approach
CO_FRACS = (1e-2, 1e-4, 0.0)                # approach depths going to 0, as fractions of y_s^th
CO_MARGIN = 1.0                             # the smooth family's NEC margin at O(x) (the adjudication's choice)
CO_KINDS = tuple(("pow", lam) for lam in DT_LAMS) + (("smooth",),)
ES_FAR = (Fr(1, 64), Fr(1, 128), Fr(1, 1024))   # d_+ as ell -> infinity


def _kind_name(kind):
    return "smooth" if kind[0] == "smooth" else "lam %g" % kind[1]


def _profile(kind, xv, g2=0.0):
    """A static piece y = depth + F(x) whose depth is approached only down the throat: S7's power law f = c x^lam
    (0 < lam < 1/2) or the adjudication's smooth family f = g1 sqrt(x) + g2 x, g1 = c (sqrt(x) is the regular coordinate
    across AdS2's degenerate horizon: standard-not-READ).  Returns F, F' = dF/dx, F'' and f_uu (u = ln x)."""
    c = DT_C
    if kind[0] == "pow":
        lam = kind[1]
        return c * xv**lam, c * lam * xv**(lam - 1), c * lam * (lam - 1) * xv**(lam - 2), c * lam * lam * xv**lam
    return (c * math.sqrt(xv) + g2 * xv, c / (2 * math.sqrt(xv)) + g2, -c / (4 * xv**1.5),
            c * math.sqrt(xv) / 4 + g2 * xv)


def _smooth_g2(tb, dep, W1):
    """The smooth family's g2 at an approach depth: the adjudication's NEC condition g2 < 2 alpha^2 W1 + p g1^2/2, with
    a margin CO_MARGIN (so k_t - k_x ~ x CO_MARGIN/(2 alpha^2) > 0)."""
    u = tb["sol"].sol(dep)
    return 2 * float(u[0])**2 * float(W1(dep)) + float(u[2]) * DT_C**2 / 2 - CO_MARGIN


def piece_stress(tb, dep, xv, kind, g2=0.0, nu=1, n_sign=1):
    """P2's surface stress at one point of a piece approaching depth dep down the throat, by the instrument's Israel
    convention (israel: S^a_b = -nu (K^a_b - delta K), the normal into the slab; K exact in the slope on the throat
    metric through O(x): _graph_k).  Returns rho, the NEC part rho + p_r and rho + p_th, and the trace tension
    tau = -S^a_a/4 (= rho - (rho + p) for a pure-tension sheet), in units of the true one-sided nu with m = 1.
    C17's mutations: nu = 1/2 (the two-sided factor) and n_sign = -1 (the normal out of the slab)."""
    F, F1, F2, _ = _profile(kind, xv, g2)
    kt, kx, kq = _graph_k(tb["sol"].sol(dep + F), xv, F1, F2)
    rho, ps = israel([n_sign * kt, n_sign * kx, n_sign * kq, n_sign * kq], nu)
    rho, pr, pq = float(rho), float(ps[0]), float(ps[1])
    return {"rho": rho, "nec_r": rho + pr, "nec_th": rho + pq, "tau": (rho - pr - 2 * pq) / 4}


def wec_window(tb):
    """S15, on H-SPLIT-AT-OUR-TENSION with H-POSITIVE-ON-P2: the approach depths down the throat at which P2's matter
    rho_m = rho - sigma_RS can be >= 0.  Along any approach the stress tends to the level set's, so rho_m -> the level
    value nu (p + 2q - 3/ell)(depth).  Deduced, exact in the slope at x -> 0 (the O(x) terms dropped): with
    rho/nu = [2q - (f_uu - alpha^2 p - 2p f_u^2)/(alpha^2 + f_u^2)]/N, N >= 1, rho_m >= 0 along the approach forces
    f_uu <= alpha^2 (p + 2q - 3e) + f_u^2 (2p + 2q - 3e), and 2p + 2q - 3e = 4a - 3e <= -7e (T4; a~ < 0 on the throat
    bulk, S7).  If the level value is negative at the approach depth, f_uu stays below a negative number as u -> -inf,
    so f -> -inf and the piece cannot approach that depth.  So for EVERY profile the WEC needs the level value >= 0 at
    the approach depth: d_plus is the shallowest such depth (0.0 in the flat limit, where the level value is 0 at depth
    0 and positive just below; None if there is none) and top the deepest before it turns negative again.  At finite
    ell the level value at depth 0 is -6 e nu < 0, so d_plus > 0 (deduced).  At d_plus itself the profile's first
    correction decides: (p' + 2q') f - f_uu/alpha^2, i.e. lam < lam_max = alpha sqrt(p' + 2q') on the power law, and
    the sign of (p' + 2q') - 1/(4 alpha^2) on the smooth family."""
    s, ys, ye, ef = tb["sol"], tb["y_s"], tb["y_end"], tb["e"]
    lv = lambda y: float(s.sol(y)[2] + 2 * s.sol(y)[3] - 3 * ef)          # the level value, nu/m
    hi = ye * (1 - 1e-6)
    yy = np.linspace(0.0, hi, 3000)
    vmax = float(max(lv(z) for z in yy))
    if abs(lv(0.0)) <= 1e-14 and lv(1e-6 * ys) > 0:
        dp = 0.0
    else:
        dp = _first_root(lv, 0.0, hi, rising=True)
    top = _first_root(lv, 0.0, hi, rising=False)
    yst, W1 = _ystar(tb)
    out = {"level_at_0": lv(0.0), "level_max": vmax, "d_plus": dp,
           "top": top, "frac_plus": None if dp is None else dp / ys, "frac_top": None if top is None else top / ys,
           "y_star": yst}
    if dp:
        u = s.sol(dp)
        al2 = float(u[0])**2
        P = 4 * ef * ef - 2 * u[2]**2 - 2 * u[2] * u[3] - 1 / (4 * u[0]**2)
        Q = 4 * ef * ef - 2 * u[3]**2 - 2 * u[2] * u[3] + 1 / (4 * u[1]**2)
        slope = float(P + 2 * Q)
        out.update({"W1_plus": float(W1(dp)), "slope": slope, "alpha2": al2,
                    "lam_max": math.sqrt(al2 * slope) if slope > 0 else 0.0, "smooth_coef": slope - 1 / (4 * al2)})
    return out


def wec_profiles(tb, w, xs=(1e-8, 1e-11, 1e-14)):
    """At finite ell with d_plus > 0: the WEC (rho_m >= 0, with the NEC) on the four profiles at x = 1e-14 at
    0.9, 0.99 and 1.01 d_plus, and along the approach (xs) at d_plus itself; and, as an illustration that a positive
    rho_m at finite x does not last along the approach, lam = 0.1 at 0.99 d_plus and x = 1e-4, 1e-7, 1e-14."""
    ef, (_, W1) = tb["e"], _ystar(tb)
    rs = 3 * ef
    res = {}
    for fac in (0.9, 0.99, 1.01):
        dep = fac * w["d_plus"]
        g2 = _smooth_g2(tb, dep, W1)
        res[str(fac)] = {_kind_name(k): (piece_stress(tb, dep, 1e-14, k, g2)["rho"] - rs) / rs for k in CO_KINDS}
    g2 = _smooth_g2(tb, w["d_plus"], W1)
    at = {}
    for k in CO_KINDS:
        sts = [piece_stress(tb, w["d_plus"], xv, k, g2) for xv in xs]
        at[_kind_name(k)] = all(st["rho"] - rs >= 0 and st["nec_r"] >= 0 and st["nec_th"] >= 0 for st in sts)
    res["at_d_plus"] = at
    dep = 0.99 * w["d_plus"]                       # finite x is not the approach: lam = 0.1 just below d_plus
    res["finite_x"] = [(xv, (piece_stress(tb, dep, xv, ("pow", 0.1), 0.0)["rho"] - rs) / rs) for xv in (1e-4, 1e-7, 1e-14)]
    res["below_fails"] = all(v < 0 for fac in ("0.9", "0.99") for v in res[fac].values())
    res["above_holds"] = all(v > 0 for v in res["1.01"].values())
    return res


def coinciding(e, tb=None, nu=1, n_sign=1, full=True):
    """S15 at e = m/ell: P2's stress as the approach depth -> 0 and x -> 0 (H-COINCIDE-DOWN-THE-THROAT, M's, item 172).
    Deduced: at depth 0 the throat data are alpha = beta = 1, p = q = -1/ell (C8's start), so the level set's k_t = k_x
    = k_th = 1/ell, S^a_b = (3 nu/ell) delta^a_b: rho -> -sigma_RS, rho + p_i -> 0, s = rho/sigma_RS = -1 -- the RS1
    sheet (C1's control) -- and rho_m = rho - sigma_RS -> -2 sigma_RS at every finite ell.  Along the approach, to
    first order in f, rho/nu + 3/ell ~ (p' + 2q')(0) f - f_uu/alpha^2 = f/4 - f_uu ((p' + 2q')(0) = -1/4 + 2/4 at every
    ell; alpha(0) = 1): c x^lam (1/4 - lam^2) on the power law (the adjudication's form, extended to finite ell), and
    -(3/4) g2 x on the smooth family in the flat limit (its sqrt(x) terms cancel; g2 < 0 there is the NEC's condition).
    Computed here: rho, s, the trace reading and the NEC part on the four profiles at depth 0 (CO_XS), s at approach
    depths CO_FRACS y_s^th (lam = 0.4, x = 1e-14), and (full) the WEC window with its profile checks."""
    tb = tb if tb is not None else throat_bulk(e)
    s, ys, ef = tb["sol"], tb["y_s"], tb["e"]
    _, W1 = _ystar(tb)
    mp.mp.dps = 30
    rs = 3 * ef                                                        # sigma_RS in nu/m (m = 1)
    u0 = s.sol(0.0)
    k0 = [-float(u0[2])] * 2 + [-float(u0[3])] * 2                     # the level set at depth 0: k = -kappa
    rho0, _ = israel(k0)                                               # the deduced limit (unmutated)
    out = {"e": str(Fr(e)), "rho_lim": float(rho0), "s_lim": float(rho0) / rs if ef else None,
           "rho_m_lim": (float(rho0) - rs) / rs if ef else None, "profiles": {}}
    g2_0 = _smooth_g2(tb, 0.0, W1)
    out["g2_0"] = g2_0
    for k in CO_KINDS:
        pts = []
        for xv in CO_XS:
            st = piece_stress(tb, 0.0, xv, k, g2_0, nu, n_sign)
            F, _, _, fuu = _profile(k, xv, g2_0)
            lead = F / 4 - fuu                                         # first order in f: rho/nu + 3/ell
            pts.append({"x": xv, "rho": st["rho"], "nec": max(abs(st["nec_r"]), abs(st["nec_th"])),
                        "nec_ok": st["nec_r"] >= 0 and st["nec_th"] >= 0, "lead": lead,
                        "lead_dev": abs((st["rho"] + rs) / lead - 1) if lead else None,
                        "s": st["rho"] / rs if ef else None, "s_tau": st["tau"] / rs if ef else None,
                        "tau": st["tau"]})
        out["profiles"][_kind_name(k)] = pts
    last = [v[-1] for v in out["profiles"].values()]
    fast = [out["profiles"][n][-1] for n in ("lam 0.4", "smooth")]   # the two that converge fastest in x
    if ef:
        out["worst_s"] = max(abs(v["s"] + 1) for v in fast)
        out["worst_tau"] = max(abs(v["s_tau"] + 1) for v in fast)
        out["worst_nec"] = max(v["nec"] for v in last) / rs
        out["worst_nec_fast"] = max(v["nec"] for v in fast) / rs
        out["rho_m_rs"] = max(((v["rho"] - rs) / rs for v in fast), key=lambda z: abs(z + 2))
        out["monotone"] = all(abs(p_[i + 1]["s"] + 1) < abs(p_[i]["s"] + 1)
                              for p_ in out["profiles"].values() for i in range(len(CO_XS) - 1))
    else:
        out["flat_pos"] = all(v["rho"] > 0 for p_ in out["profiles"].values() for v in p_)
        out["flat_to_0"] = all(p_[i + 1]["rho"] < p_[i]["rho"] for p_ in out["profiles"].values()
                               for i in range(len(CO_XS) - 1))
        out["flat_lead_dev"] = max(v["lead_dev"] for p_ in out["profiles"].values() for v in p_ if v["x"] <= 1e-8)
        out["worst_nec"] = max(v["nec"] for v in last)
        out["worst_nec_fast"] = max(v["nec"] for v in fast)
    out["nec_ok"] = all(v["nec_ok"] for p_ in out["profiles"].values() for v in p_)
    conv = []
    for fr in CO_FRACS:
        st = piece_stress(tb, fr * ys, 1e-14, ("pow", 0.4), 0.0, nu, n_sign)
        conv.append({"frac": fr, "rho": st["rho"], "s": st["rho"] / rs if ef else None})
    out["depths"] = conv
    if full:
        w = wec_window(tb)
        out["wec"] = w
        out["wec_profiles"] = wec_profiles(tb, w) if w["d_plus"] else None
    return out


def d_plus_scaling(es=ES_FAR):
    """S15: d_plus -> 0 only as ell -> infinity.  Deduced leading order: the level value nu (p + 2q - 3e) = nu (-6e +
    depth/4 + ...) at small depth ((p + 2q)'(0) = 1/4), so d_plus = 24 e m (1 + O(e)); computed d_plus/(24 e m)."""
    out = []
    for e in es:
        w = wec_window(throat_bulk(e))
        out.append({"e": str(Fr(e)), "d_plus": w["d_plus"], "ratio": None if not w["d_plus"] else
                    w["d_plus"] / (24 * float(e))})
    return out


# ------------------------------------------------------------------------------------------------ C14 address guard
def address_guard(extra_keys=None, extra_funcs=()):
    """No function of this instrument takes a plane separation (by signature), and no key of the bank or the report
    names a distance, time, redshift or speed (139 (4), 101 (7))."""
    mod = sys.modules[__name__]
    funcs = [f for _, f in inspect.getmembers(mod, inspect.isfunction) if f.__module__ == mod.__name__]
    funcs += list(extra_funcs)
    bad_args = sorted({(f.__name__, p) for f in funcs for p in inspect.signature(f).parameters if p in BANNED_ARGS})
    keys = set()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                keys.add(str(k))
                walk(v)
        elif isinstance(o, (list, tuple)):
            for v in o:
                walk(v)
    if os.path.exists(BANK):
        walk(load_bank())
    if extra_keys:
        walk(extra_keys)
    bad_keys = sorted(k for k in keys if any(b in k.lower() for b in BANNED_KEYS))
    return {"n_funcs": len(funcs), "bad_args": bad_args, "bad_keys": bad_keys, "n_keys": len(keys)}


# ------------------------------------------------------------------------------------------------ the owner-side checks
def owner_column(rc, e, N, o_index=1):
    """w_r, w_th, a~ from the raw Pade at one order -- for C5, C9, C10."""
    mp.mp.dps = 40
    W = S5.warped(B4.series(rc, N, e), e, N)
    o = S5.orders(N)[o_index]
    R = {X: raw_rational(W[X][0], o) for X in "ABC"}
    return W, o, R


def pade_honesty():
    """C5: at r = 2.15m, ell = m: the raw Pade at N = 24 against the partial sums of the exact series at orders 24, 28
    and 32 (a partial sum counts as converged at y where orders 28 and 32 agree to 1e-9), and the mutation through
    b4d_stage5._clean."""
    W, o, R = owner_column("43/20", Fr(1), 24)
    W32 = S5.warped(B4.series("43/20", 32, Fr(1)), Fr(1), 32)

    def psum(Wx, X, y, n):
        c = [float(v) for v in Wx[X][0][:n + 1]]
        return sum(k * c[k] * y**(k - 1) for k in range(1, len(c))) / sum(c[k] * y**k for k in range(len(c)))
    out = []
    for y in (0.02, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6):
        raw = _w_at(R, y)[0]
        ps = {n: (psum(W32, "B", y, n) - psum(W32, "A", y, n)) / 2 for n in (24, 28, 32)}
        out.append((y, raw, ps[24], ps[28], ps[32]))
    pq = {X: S5._approx(W[X][0], o) for X in "ABC"}
    cl = {}
    for X in "ABC":
        pp, qq, dz = S5._clean(*pq[X])
        dp, dq = _dco(pp), _dco(qq)

        def ld(yv, pp=pp, qq=qq, dp=dp, dq=dq, dz=dz):
            yv = mp.mpf(yv)
            v = mp.polyval(dp, yv) / mp.polyval(pp, yv) - mp.polyval(dq, yv) / mp.polyval(qq, yv)
            for pole, zero in dz:
                v += 1 / (yv - pole) - 1 / (yv - zero)
            return mp.re(v)
        cl[X] = ld
    clean = float((cl["B"](0.02) - cl["A"](0.02)) / 2)
    return {"rows": out, "clean_002": clean, "raw_002": out[0][1]}


def throat_vs_owner():
    """C9: at ell = 2m, columns 401/200 and 201/100 (N = 20) against the throat ODE at y = 0.13, 0.26 (w_th, a~), and the
    gap ratio (linear in x).  C10: W1(1.088) against w_r(2.005)/0.005 (flat, N = 24)."""
    tb = throat_bulk(Fr(1, 2))
    s = tb["sol"]
    ode = {y: (float(s.sol(y)[3] - s.sol(y)[2]), float((s.sol(y)[2] + s.sol(y)[3]) / 2 + 0.5)) for y in (0.13, 0.26)}
    own = {}
    for rc in ("401/200", "201/100"):
        _, _, R = owner_column(rc, Fr(1, 2), 20)
        own[rc] = {y: _w_at(R, y)[1:] for y in (0.13, 0.26)}
    rel = {rc: {y: [abs(own[rc][y][i] / ode[y][i] - 1) for i in (0, 1)] for y in ode} for rc in own}
    ratio = {y: [(own["201/100"][y][i] - ode[y][i]) / (own["401/200"][y][i] - ode[y][i]) for i in (0, 1)] for y in ode}
    tb0 = throat_bulk(Fr(0))
    W1 = float(tb0["sol"].sol(1.088)[8] - tb0["sol"].sol(1.088)[7]) / 2
    _, _, R0 = owner_column("401/200", Fr(0), 24)
    wr = _w_at(R0, 1.088)[0]
    return {"ode": ode, "own": own, "rel": rel, "ratio": ratio, "W1": W1, "wr_over_x": wr / 0.005}


# ------------------------------------------------------------------------------------------------ report
def _ell(es):
    e = Fr(es)
    return "inf" if e == 0 else ("%gm" % float(1 / e))


def compute_live():
    """The fast exact parts the report prints live (seconds)."""
    tbs = {str(e): throat_bulk(e) for e in ES2}
    return {"lead3": leading_coefficients("3", Fr(1, 2)), "lead215": leading_coefficients("43/20", Fr(1, 2)),
            "t5c": t5c(Fr(1)), "lemma_t": lemma_t(), "near": near_horizon(), "n": lemma_n(), "delta": delta_rows(),
            "wproof": lemma_w_proof(4000), "dt": {str(e): down_throat_class(e, tb=tbs[str(e)]) for e in ES2},
            "dt_wec": ell_w_class(), "depth0": {str(e): depth_zero(e) for e in ES2},
            "coin": {str(e): coinciding(e, tb=tbs[str(e)]) for e in ES2}, "dplus_far": d_plus_scaling()}


def report(bank, live):
    T = bank["throat"]
    dec = decide(bank, T)
    ms = map_summary(bank)
    print("sim2_facing.py -- B4d simulation phase 2: two pieces of our plane facing across a static bulk\n")
    lt = live["lemma_t"]
    print("S1 Lemma T (deduced; T1 exact on the owner's series, selftest C3): Raychaudhuri split residual %s; the "
          "comparison solution e tanh(e y - artanh s1) solves b' = e^2 - b^2 (residual %s), and at s1 = 1 is the fixed "
          "point %s/ell: a~ <= 0 at every depth" % (lt["split"], lt["ode"], lt["fixed_point"]))
    L3 = live["lead3"]
    print("   anchor r = 3m, ell = 2m: a~ = (%s) y^3 + (%s) y^4 + O(y^5) = -(R_ab R^ab/12)(y^3 + 5 e y^4), R_ab R^ab = %s"
          % (L3["at"][3], L3["at"][4], L3["RR"]))
    print("S2 Lemma C (deduced; comparison standard-not-READ): k_t(P2) = -kappa_t, k_spatial(P2) >= -kappa_spatial")
    tc = live["t5c"]
    print("S3 T5c (deduced): a matter-free mirrored P2 reads s2 <= ell a(depth) <= %s at every depth and ell; general "
          "bound s2 <= %s, which at s1 -> 1 is %s (the depth drops out).  DECIDED: under clause (B) two matter-free "
          "pieces of our plane cannot face each other across a static bulk (diagonal K, vacuum Lambda_5), on the board's "
          "H-Z2-PIECES and H-NEAREST-APPROACH; down the throat (M's H-COINCIDE-DOWN-THE-THROAT, item 172) the member "
          "closes too "
          "(deduced in the adjudication, with w_th > 0 computed on the throat bulk at the nine ell; illustrated in S7).  "
          "Not closed by this: E-PASS, E-NS, E-ROT and the other escapes of S14, E-FAR among them"
          % (tc["s2_max"], tc["general"], tc["at_s1_1"]))
    wp = live["wproof"]
    print("S4 Lemma W (deduced): k_t I - k_spatial = diag(w) - H exactly: %s; %d NEC-obeying random samples, %d "
          "counterexamples to w >= 0" % (wp["exact"], wp["nec_samples"], wp["counterexamples"]))
    L215 = live["lead215"]
    print("S5 leading orders (exact): r = 3m: R_rad %s, R_tan %s, y^2 terms at ell = 2m %s, %s; r = 2.15m: R_rad %s, "
          "R_tan %s" % (L3["R_rad"], L3["R_tan"], L3["wr"][2], L3["wth"][2], L215["R_rad"], L215["R_tan"]))
    nh = live["near"]
    print("S6 near horizon: R^a_b(r = 2m) = %s; F ~ %s x, H ~ %s x^2; AdS2 curvature %s (radius 2m), S2 radius %s"
          % (nh["R_mixed"], nh["F_lead"], nh["H_lead"], nh["AdS2_R"], nh["S2_radius"]))
    print("S7/S8 the throat bulk (ODE; the band [y*, y_s^th) for an ATTAINED nearest point, at first order in x; rho_m in "
          "nu/m, level set; K_bs = b4d_stage5.k_bs(e, 2, y); the constraint on the zeroth-order solve; x_O1 = the largest "
          "x = r - 2m with x max(|a1|,|b1|,|c1|) <= %g, at y* and at the band's midpoint; the depth of a nearest point is "
          "the two pieces' bulk separation there, and these depths are reported only as where facing can occur):"
          % O1_BOUND)
    print("   ell    y_s^th   y*      y*/y_s  y_K(10/30/100)          K(y*)/K_bs  rho_m(y*) nu/m  (sigma_RS)  "
          "x_O1(y*)  x_O1(mid)  min w_th/y  max a~/y^3  constraint")
    for r_ in T["rows"]:
        yk = r_["yK"]
        print("   %-5s  %.4f   %s  %s   %s  %10.3g  %+9.4f  %10s  %8s  %9s  %10.4f  %+10.5f  %.0e" % (
            _ell(r_["e"]), r_["y_s"], "%.4f" % r_["y_star"] if r_["y_star"] else "none  ",
            "%.3f" % r_["frac"] if r_["frac"] else "  -  ",
            " / ".join("%.3f" % yk[str(f)] if yk[str(f)] else "  -  " for f in KF), r_["K_ratio"] or float("nan"),
            r_["rho_m"] if r_["rho_m"] is not None else float("nan"),
            "" if r_["rho_m_rs"] is None else "(%+.3f)" % r_["rho_m_rs"],
            "%.1e" % r_["x_O1_ystar"] if r_.get("x_O1_ystar") else "-",
            "%.1e" % r_["x_O1_mid"] if r_.get("x_O1_mid") else "-",
            r_["w_th_over_y_min"], r_["at_over_y3_max"], r_["cons_rel"]))
    print("   w_th > 0 and a~ < 0 on all %d points of (0, y_end) at every ell: %s" % (
        T["rows"][0]["n_grid"], all(r_["w_th_pos_all"] and r_["at_neg_all"] for r_ in T["rows"])))
    print("   WEC in the band (rho_m(y*) >= 0): ell >= ell_W = %.2fm (e <= %.6f); maximum over the band gives %.2fm"
          % (T["ell_W"], T["e_W"], T["ell_W_band"]))
    lar = []
    for r_ in T["rows"]:
        ls_ = r_.get("level_set")
        if ls_ is None:
            continue
        a_ = ls_["rho"] / 3 - ls_["rho_plus_pth"] / 6        # a = (p + q)/2 from rho = p + 2q, rho + p_th = q - p
        ef_ = float(Fr(r_["e"]))
        lar.append("%s %+.2f" % (_ell(r_["e"]), a_ / ef_) if ef_ else "inf a(y*) = %+.4f/m (sigma_RS -> 0: no ratio)" % a_)
    print("   on H-LAW-READ-BY-TRACE a facing piece at depth >= y* reads s <= ell a(depth) <= ell a(y*) (a is non-increasing,"
          " T4): %s -- a law not ours; on H-SPLIT-AT-OUR-TENSION the tension is ours and the rest is the README's"
          % ", ".join(lar))
    print("   the band's shallow edge below f K_bs: f = 10 %s; f = 30 for ell > %s; f = 100 for ell > %s" % (
        "never (flat: K(y*)/K_bs = %.1f)" % T["rows"][0]["K_ratio"] if T["ell_c"]["10"] is None
        else "for ell > %.2fm" % T["ell_c"]["10"],
        "%.2fm" % T["ell_c"]["30"] if T["ell_c"]["30"] else "never", "%.2fm" % T["ell_c"]["100"] if T["ell_c"]["100"]
        else "never"))
    DT = live["dt"]
    print("S7 down the throat (computed; corrected; facing down the throat on M's H-COINCIDE-DOWN-THE-THROAT, item 172, "
          "which replaces the board's H-FACING-DOWN-THE-THROAT): radial NEC along "
          "y = depth + f(u), u = ln x: f'' - f'/2 <= alpha^2 x W1(depth) (f'/2: the lapse-gradient term the first build "
          "dropped).  f = %g x^lam, lam = %s, NEC exact in the slope on the throat metric through O(x), at depths %s "
          "y_s^th, x = 1e-14 .. min(1e-3, x_O1):" % (
              DT_C, "/".join("%g" % v for v in DT_LAMS), "/".join("%g" % v for v in DT_FRACS)))
    for es in bank["es"]:
        d = DT[es]
        print("   ell = %-5s %d samples, %d below the crossover x_c/2: radial and angular NEC hold there %s; failures %d, "
              "all above x_c/2 %s (first failure at %s x_c); leading order to %.1e at x <= 1e-8; control lam = %g fails "
              "at every depth %s; the first build's f'' <= alpha^2 x W1 excludes %d/%d sampled depths below y* (an "
              "identity: W1 < 0 there); umbilic member (an illustration at x = 1e-14, an identity for any f -> 0; the "
              "closing is deduced): k_t - k_th -> w_th(depth) to %.0e, k_t - k_x -> 0 to %.0e: %s%s" % (
                  _ell(es), d["n"], d["n_below_xc"], d["nec_holds"], d["n_fail"], d["fails_only_above_xc"],
                  "-" if not d["fail_over_xc"] else "%.1f-%.1f" % tuple(d["fail_over_xc"]), d["lead_dev"],
                  DT_LAM_CONTROL, d["control_fails"], d["old_excludes_below_ystar"], d["n_below_ystar"],
                  d["umbilic_ratio_dev"], d["umbilic_radial_dev"], d["umbilic_closes"],
                  "" if d["ell_a_max"] is None else "; its trace reads ell a(depth) <= %.6f (trace minus ell a: %.0e)"
                  % (d["ell_a_max"], d["trace_minus_ell_a"])))
    print("   so in this class (the nearest approach never attained: a degenerate horizon, at infinite proper distance in "
          "the static slice) the NEC sets no lower edge in the approach (x -> 0): it holds at every sampled depth, %g to "
          "%g y_s^th, at every ell -- including depths shallower than y_K(10), where K < 10 K_bs.  Past the crossover "
          "the NEC still bends the piece back (SIM2-FACING.md S7, deduced to first order): whether a member exists below "
          "y* is decided on the owner's bulk (E-FAR, E-G)" % (min(DT_FRACS), max(DT_FRACS)))
    cw = live["dt_wec"]
    print("   positive energy in the class (the limiting level-set rho_m, maximised over every depth in (0, y_s^th)): "
          "ell > ell_W^class = %.2fm (e < %.7f), best depth %.3f y_s^th (%.3f y*), K/K_bs %.2f there; at ell = inf the "
          "best is %+.4f nu/m at %.3f y_s^th (attained band: ell >= ell_W = %.2fm)" % (
              cw["ell"], cw["e"], cw["frac_ys"], cw["frac_ystar"], cw["K_ratio"], cw["flat"]["rho_m_max"],
              cw["flat"]["frac_ys"], T["ell_W"]))
    d0 = live["depth0"]
    print("   depth -> 0 (the coincidence, item 172; never reached at a point of the static region; along the approach: "
          "S15): the limiting stress reads "
          "rho_m/sigma_RS = %s at every finite ell (deduced: p = q = -1/ell at y = 0); K/K_bs (computed) = "
          "2(80 e^4 + 3)/(160 e^4 + 3) = %s (ell = inf .. m/4), max deviation from the closed form %.0e" % (
              ", ".join(sorted({"%+.6f" % v["rho_m_rs"] for v in d0.values() if v["rho_m_rs"] is not None})),
              "/".join("%.3f" % d0[es]["K_ratio"] for es in bank["es"]),
              max(abs(v["K_ratio"] - v["K_closed"]) for v in d0.values())))
    print("S9 the map (order 32, %d columns, raw Pade; verified = b4_static S3's value rule; admissible = verified, the two "
          "orders agree on the signs of w_r and w_th, both >= 0): %d verified points, %d with the sign of w_r and w_th "
          "settled, %d admissible" % (len(bank["columns"]), ms["n_ver"], ms["n_ver_settled"], ms["n_adm"]))
    print("   columns at r >= 2.05m or ell <= 2m: %d verified points (%d sign-settled); w_r < 0 at %d and >= 0 at %d of "
          "the sign-settled; w_th > 0 at %d, a~ < 0 at %d of the verified; sign-settled w_r >= 0 there: %s" % (
              ms["n_far"], ms["n_far_settled"], ms["far_wr_neg"], ms["far_wr_pos"], ms["far_wth_pos"], ms["far_at_neg"],
              ", ".join("%s@%s" % (rc, _ell(es)) for rc, es in ms["far_wr_pos_cols"]) or "none"))
    print("   over every verified point: max a~ %.2e, min w_th %.2e; columns with some verified, sign-settled w_r >= 0: "
          "%s" % (ms["at_max"], ms["wth_min"], ", ".join("%s@%s" % (rc, _ell(es)) for rc, es in ms["wr_pos_cols"])))
    print("   verified points with w_th <= 0 (%d; w_r < 0 at all of them: %s): %s" % (
        len(ms["wth_nonpos"]), all(v[5] < 0 for v in ms["wth_nonpos"]),
        "; ".join("%s@%s y = %.3f: w_th %+.2e%s" % (rc, _ell(es), y, w, "" if s else " (sign unsettled)")
                  for rc, es, y, w, s, _ in ms["wth_nonpos"]) or "none"))
    print("   diagnostic, the first build's w-agreement rule (1e-6 + 1e-3|w|, never decisive): it fails at %d verified "
          "points; as a prefix it would keep %d verified and %d admissible points" % (
              ms["w_disagree"], ms["n_ver_w"], ms["n_adm_w"]))
    for es in bank["es"]:
        cs = [bank["columns"]["%s|%s" % (rc, es)] for rc in ("401/200", "201/100", "101/50")]
        print("   ell = %-5s r = 2.005/2.01/2.02m: verified top %s (w-rule %s); w_r changes sign at %s; y_s(C~) %s" % (
            _ell(es), "/".join("%.3f" % c["vtop"] for c in cs), "/".join("%.3f" % c["vtop_w"] for c in cs),
            "/".join(",".join("%.3f(%s)" % (z, "+" if sg > 0 else "-") for z, sg in c["wr_zeros"]) or "-" for c in cs),
            "/".join("%.3f" % float(np.median(c["ys"])) if c["ys"] else "-" for c in cs)))
    farz = sorted([c for c in bank["columns"].values() if c["r"] > NEAR_R + 1e-12 and c["wr_zeros"]],
                  key=lambda c: (Fr(c["e"]), c["r"]))
    if farz:
        print("   sign changes of w_r at r > 2.02m (verified, sign-settled): %s" % "; ".join(
            "%s@%s %s" % (c["rc"], _ell(c["e"]), ",".join("%.3f(%s)" % (z, "+" if sg > 0 else "-")
                                                       for z, sg in c["wr_zeros"])) for c in farz))
    print("   orders: stage 5's at ell < inf; at ell = inf %s (three distinct approximants of the even series)" % (
        bank["columns"]["401/200|0"].get("orders")))
    print("   K/K_bs at the shallowest admissible point (two Pade orders, b4d_stage5.evaluator):")
    for es in bank["es"]:
        pts = sorted([(c["r"], c["rc"], k) for c in bank["columns"].values() if c["e"] == es and c["kk"]
                      for k in c["kk"][:1]])
        if pts:
            print("   ell = %-5s %s" % (_ell(es), "; ".join("r = %s: y = %.3f, %.1f/%.1f" % (rc, k[0], k[1], k[2])
                                                          for _, rc, k in pts)))
    print("S10 throat and owner: the sign change of w_r, extrapolated to x -> 0 (2 y0(2.005m) - y0(2.01m)), against y*:")
    for r_ in T["rows"]:
        c1 = bank["columns"]["401/200|%s" % r_["e"]]
        c2 = bank["columns"]["201/100|%s" % r_["e"]]
        if c1["wr_zero"] and c2["wr_zero"]:
            ex = 2 * c1["wr_zero"] - c2["wr_zero"]
            print("   ell = %-5s %.4f against y* %.4f (%.2f%%)" % (_ell(r_["e"]), ex, r_["y_star"],
                                                                 100 * abs(ex / r_["y_star"] - 1)))
    print("   y_s^th against the r = 2.005m column's C~ singularity (three Pade orders):")
    for r_ in T["rows"]:
        c = bank["columns"]["401/200|%s" % r_["e"]]
        print("   ell = %-5s %.4f against %s" % (_ell(r_["e"]), r_["y_s"],
                                                "/".join("%.4f" % v for v in c["ys"]) if c["ys"] else "-"))
    nl = live["n"]
    print("S11 Lemma N (sympy): Gamma^y_ab = -(1/2) d_y g_ab: %s; y'' - w_r B r'^2 = %s; warped products w = %s" % (
        nl["connection"], nl["ray"], nl["warped_w"]))
    print("S12 decision, for ATTAINED nearest points, on the verified map (WIDE on the verified points only: deeper than "
          "them at r >= %gm, the board's line, a convention, and for E-FAR, facing is unchecked; CONFIRMED against the "
          "throat's y* (x -> 0), the offset being the O(x) shift; the down-the-throat class has no lower edge in the "
          "approach, S7):" % WIDE_R)
    for es in bank["es"]:
        d = dec[es]
        line = "   ell = %-5s %s" % (_ell(es), d["class"])
        if d["class"] == "THROAT-BAND":
            cf = d["confirm"][0] if d["confirm"] else None
            line += (" %s%s; regular at 10/30/100 K_bs: %s (strict y < y_s: %s; settled: %s); WEC: %s; admissible "
                     "points %d (w-rule diagnostic: %d, %s)" % (
                         "CONFIRMED" if d["confirmed"] else "EXPANSION-ONLY",
                         " (%s, sign change %.4f vs the throat's y* %.4f: %.1f%%, the O(x) shift)"
                         % (cf[0], cf[1], d["y_star"], 100 * cf[2]) if cf else "",
                         "/".join("yes" if d["regular"][str(f)] else "no" for f in KF), d["strict"], d["settled"],
                         "yes" if d["wec"] else "no", d["n_adm"], d["n_adm_w"],
                         "CONFIRMED" if d["confirmed_w"] else "EXPANSION-ONLY"))
            if d["not_reached"]:
                line += "; not reached: %s" % ", ".join("%s (top %.3f)" % v for v in d["not_reached"])
        print(line)
        if d["unverified_wide"]:
            print("      not verified at r >= %gm (depths from the verified top to the Pade singular depth where the three "
                  "orders agree, else to the %gm cap (*); where facing is unchecked): %s" % (
                      WIDE_R, CAP, ", ".join("%s %.3f-%.3f%s" % (v[:3] + ("" if v[3] else "*",))
                                             for v in d["unverified_wide"])))
    dl = live["delta"]
    print("S13 hand-off: %s, in units of %s; s_outer needed: %s (both > 0: the outer side decays, stage 7 K4; the unit, "
          "K4, and the image count, K5, stay put to M); the within-universe rows, on %s: %s; %s" % (
              dl["s_slab_read"], dl["unit"], ", ".join("%s -> >= %s" % kv for kv in dl["s_outer_min"].items()),
              dl["rows_on"], "; ".join("%s %s" % r_ for r_ in dl["rows"]), dl["on_trace"]))
    print("S14 escapes: %s" % "; ".join("%s (%s): %s" % e_ for e_ in ESCAPES))
    print("   The depth of a nearest point is the two pieces' bulk separation there: it is reported only as where facing can "
          "occur, never as the corridor's length (bits: 155 (2), R4c) or as anything the device sees (101 (7)); no "
          "time, redshift or speed is computed (139 (4)).")
    CO = live["coin"]
    print("S15 the coinciding limit (item 172 (2), \"Yes, that is coinciding\": H-COINCIDE-DOWN-THE-THROAT, M's; the "
          "approach down the throat with its depth -> 0, never reached at a point of the static region; P2's stress by "
          "the instrument's Israel convention, normal into the slab, K exact in the slope on the throat metric through "
          "O(x); s = rho/sigma_RS and the trace reading s_tau = (ell/3 nu)(-S^a_a/4); profiles lam = %s (c = %g) and the "
          "smooth f = %g sqrt(x) + g2 x, g2 = 2 alpha^2 W1 + p g1^2/2 - %g; the approach depth is reported only as where "
          "facing occurs):" % ("/".join("%g" % v for v in DT_LAMS), DT_C, DT_C, CO_MARGIN))
    print("   deduced: at depth 0 the throat data are alpha = beta = 1, p = q = -1/ell, so k_t = k_x = k_th = 1/ell, "
          "S^a_b = (3 nu/ell) delta: rho -> -sigma_RS, rho + p_i -> 0, s = s_tau = -1 (the RS1 sheet: C1's control), "
          "rho_m = rho - sigma_RS -> -2 sigma_RS at every finite ell; along the approach, to first order in f, "
          "rho/nu + 3/ell = f/4 - f_uu ((p' + 2q')(0) = 1/4 at every ell): c x^lam (1/4 - lam^2) on the power law")
    for es in bank["es"]:
        c_ = CO[es]
        P_ = c_["profiles"]
        if c_["s_lim"] is not None:
            print("   ell = %-5s depth 0, x = %s: s = %s; |s + 1|, |s_tau + 1| at 1e-14 (lam 0.4, smooth) <= %.0e, %.0e; "
                  "NEC part (rho + p_i)/sigma_RS <= %.0e there (%.0e with lam 0.1, falling as x^lam), every sample "
                  "NEC-legal %s, |s + 1| falling along x on all four %s; rho_m/sigma_RS -> %.7f; approach depths %s y_s^th: "
                  "s = %s" % (
                      _ell(es), "/".join("%g" % v for v in CO_XS),
                      "; ".join("%s %s" % (n, " ".join("%.5f" % v["s"] for v in pts)) for n, pts in P_.items()),
                      c_["worst_s"], c_["worst_tau"], c_["worst_nec_fast"], c_["worst_nec"], c_["nec_ok"],
                      c_["monotone"], c_["rho_m_rs"], "/".join("%g" % v["frac"] for v in c_["depths"]),
                      "/".join("%.5f" % v["s"] for v in c_["depths"])))
        else:
            sm = P_["smooth"]
            print("   ell = %-5s (sigma_RS = 0: rho_m = rho, in nu/m) depth 0, x = %s: rho/nu = %s; against the first "
                  "order c x^lam (1/4 - lam^2) and, smooth, -(3/4) g2 x = %.4f x: within %.0e at x <= 1e-8; smooth "
                  "(rho/nu)/x = %s; rho > 0 at every sample %s and falling toward 0 along x %s; NEC part <= %.0e at "
                  "1e-14 (lam 0.4, smooth), every sample NEC-legal %s; approach depths %s y_s^th: rho/nu = %s" % (
                      _ell(es), "/".join("%g" % v for v in CO_XS),
                      "; ".join("%s %s" % (n, " ".join("%.3e" % v["rho"] for v in pts)) for n, pts in P_.items()),
                      -0.75 * c_["g2_0"], c_["flat_lead_dev"], "/".join("%.4f" % (v["rho"] / v["x"]) for v in sm),
                      c_["flat_pos"], c_["flat_to_0"], c_["worst_nec_fast"], c_["nec_ok"],
                      "/".join("%g" % v["frac"] for v in c_["depths"]), "/".join("%.3e" % v["rho"] for v in c_["depths"])))
    print("   on H-SPLIT-AT-OUR-TENSION with H-POSITIVE-ON-P2 (rho_m >= 0).  Deduced, exact in the slope at x -> 0: along "
          "any approach the WEC forces f_uu <= alpha^2 (p + 2q - 3/ell) + f_u^2 (4a - 3/ell), the last bracket <= -7/ell "
          "(T4), so it needs the level value nu (p + 2q - 3/ell) >= 0 at the approach depth, for every profile; at finite "
          "ell that value is -6 nu/ell = -2 sigma_RS at depth 0, so d_+ (the shallowest approach depth with rho_m >= 0) "
          "is > 0 (depths reported only as where positive-energy facing down the throat can occur).  Computed:")
    for es in bank["es"]:
        w = CO[es]["wec"]
        wp = CO[es]["wec_profiles"]
        if w["d_plus"] is None:
            print("   ell = %-5s no approach depth: the level value's maximum is %+.4f nu/m (%+.3f sigma_RS) < 0" % (
                _ell(es), w["level_max"], w["level_max"] / (3 * float(Fr(es)))))
        elif w["d_plus"] == 0.0:
            print("   ell = %-5s d_+ = 0 only as an infimum: the level value is %+.1e at depth 0 and > 0 from there to "
                  "%.4fm (%.4f y_s^th); at depth 0 itself rho -> 0+ along the approach (above): no positive margin at "
                  "coincidence" % (_ell(es), w["level_at_0"], w["top"], w["frac_top"]))
        else:
            print("   ell = %-5s d_+ = %.4fm (%.4f y_s^th; W1 = %+.4f < 0 there, so down the throat only, y* = %.4fm) to "
                  "%.4fm (%.4f y_s^th); on the four profiles at x = 1e-14 rho_m/sigma_RS at 0.9 d_+ %s, at 0.99 d_+ %s "
                  "(all < 0: %s), at 1.01 d_+ %s (all > 0: %s); at d_+ itself, along x = 1e-8 .. 1e-14 with the NEC: %s "
                  "(lam < lam_max = %.3f holds; the smooth family's first-order coefficient (p' + 2q') - 1/(4 alpha^2) "
                  "= %+.3f); finite x is not the approach: at 0.99 d_+, lam 0.1 reads %s" % (
                      _ell(es), w["d_plus"], w["frac_plus"], w["W1_plus"], w["y_star"], w["top"], w["frac_top"],
                      "/".join("%+.4f" % v for v in wp["0.9"].values()),
                      "/".join("%+.4f" % v for v in wp["0.99"].values()), wp["below_fails"],
                      "/".join("%+.4f" % v for v in wp["1.01"].values()), wp["above_holds"],
                      ", ".join("%s %s" % (n, "holds" if v else "fails") for n, v in wp["at_d_plus"].items()),
                      w["lam_max"], w["smooth_coef"],
                      ", ".join("%+.4f at x = %g" % (v, xv) for xv, v in wp["finite_x"])))
    print("   d_+ -> 0 only as ell -> infinity (deduced: the level value is nu (-6/ell + depth/4 + ...), so d_+ = 24 m^2/ell "
          "(1 + O(m/ell))); computed d_+/(24 m^2/ell) = %s" % ", ".join(
              ["%.4f (%s)" % (CO["1/32"]["wec"]["d_plus"] * 32 / 24, _ell("1/32"))]
              + ["%.4f (%s)" % (v["ratio"], _ell(v["e"])) for v in live["dplus_far"]]))
    print("   on H-LAW-READ-BY-TRACE: at coincidence the NEC part (the history) -> 0 and the trace reads s_tau -> -1: a "
          "matter-free sheet of tension -1 in sigma_RS at our ell, not our +1 -- a different law, so between universes "
          "on the board's H-ONE-UNIVERSE-ONE-LAW (phase 3).  Its sign is 139 (1)'s (position 2's plane negative); its "
          "magnitude, -1, is not multiplane.py M4's -1/3 of the one-plane value nor stage 7 K5's -1/6 per sheet: "
          "different setups and units (K4, K5), not identified.  On H-SPLIT-AT-OUR-TENSION the same limit is our tension "
          "plus README stress rho_m = -2 sigma_RS, p_m = +2 sigma_RS: NEC-marginal, and against H-POSITIVE-ON-P2 at every "
          "finite ell.  Question 1 (b) (not answered in item 172) decides which.")
    return dec


# ------------------------------------------------------------------------------------------------ selftest
PIN = {  # this instrument's own computed values (C13), pinned at its first regeneration
    "0": {"y_s": 2.55355, "y_star": 1.79006, "K_ratio": 18.3},
    "1": {"y_s": 0.91386, "y_star": 0.88119, "K_ratio": 2.69e4},
    "ell_W": 49.86, "ell_c30": 21.05,
    "ell_W_class": 27.07,   # added after the adjudication (down-the-throat class; its scratch gave 27.0665m)
    # C16, added after the re-verification: the map's rules, on the bank as regenerated after the w-rule fix
    "c16": {"wr_zero": 2.198, "n_adm": 3, "adm_from": 2.237, "edge_2m": 1.186,
            "n_ver": 4480, "n_settled": 4479, "n_adm_total": 86,
            "adm_per_ell": {"0": 24, "1/32": 21, "1/16": 18, "1/8": 14, "1/4": 8, "1/2": 1, "1": 0, "2": 0, "4": 0}},
    # C17, added for item 172 (S15, the coinciding limit): d_+ at ell = 32m and d_+/(24 m^2/ell) at ell = 1024m
    "c17": {"d_plus_32": 0.8395, "ratio_1024": 1.0001},
}


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))
        sys.stdout.flush()

    t0 = time.monotonic()
    # C1
    e = sp.Symbol("e", positive=True)
    rho1, _ = israel([-e] * 4)
    KL, KM = level_set_k(e, -1), level_set_k(e, +1)
    rhoL, _ = israel(KL)
    rhoM, _ = israel(KM)
    rhoT, _ = israel([-e] * 4, trace_from=1)
    s1 = sp.simplify(rho1 / (3 * e))
    sL = sp.simplify(rhoL / (3 * e))
    sM = sp.simplify(rhoM / (3 * e))
    sT = sp.simplify(rhoT / (3 * e))
    chk("C1 Israel calibration: P1 (n = +d_y, K = -h/ell) reads s = %s = b4d_stage6.sigma_over_rs(-e,-e,e) = %s; an RS2 "
        "level set, K = %s from the warp e^(-2eY) with n = -d_y, reads s = %s (RS1's negative sheet); mutations: the "
        "same level set read with n = +d_y (K = %s) gives %s, failing RS1; the trace over the spatial part only gives "
        "P1 s = %s" % (s1, S6.sigma_over_rs(-e, -e, e), KL[0], sL, KM[0], sM, sT),
        s1 == 1 and S6.sigma_over_rs(-e, -e, e) == 1 and sL == -1 and sM != -1 and sT != 1)
    # C2
    kt, kr, kq, kp, c, nu = sp.symbols("k_t k_r k_q k_p c nu", real=True)
    K = [kt + c, kr + c, kq + c, kp + c]
    rho, ps = israel(K, nu)
    li = [sp.simplify(rho + ps[i] - nu * (kt - [kr, kq, kp][i])) for i in range(3)]
    rho_m, ps_m = israel(K, nu / 2)
    li_m = [sp.simplify(rho_m + ps_m[i] - nu * (kt - [kr, kq, kp][i])) for i in range(3)]
    rho_t, ps_t = israel(K, nu, trace_from=1)
    li_t = [sp.simplify(rho_t + ps_t[i] - nu * (kt - [kr, kq, kp][i])) for i in range(3)]
    wp = lemma_w_proof()
    wf = lemma_w_proof(flip=True)
    chk("C2 local Israel lemma (identity, algebraic by construction: rho + p_i - nu (k_t - k_i) = %s for any added "
        "tension c); mutation (the two-sided factor nu/2) leaves %s; identity: the trace drops out of rho + p_i (a trace "
        "error leaves %s, so C1 catches it); Lemma W's step exact (identity: %s), %d NEC samples with %d "
        "counterexamples, and the reversed comparison produces %d"
        % (li, li_m[0], li_t[0], wp["exact"], wp["nec_samples"], wp["counterexamples"], wf["counterexamples"]),
        all(v == 0 for v in li) and any(v != 0 for v in li_m) and all(v == 0 for v in li_t) and wp["exact"]
        and wp["counterexamples"] == 0 and wp["nec_samples"] > 100 and wf["counterexamples"] > 0)
    # C3
    r0 = riccati_identity("43/20", Fr(0))
    r1 = riccati_identity("43/20", Fr(1))
    rm = riccati_identity("43/20", Fr(1), ryy_sign=+1)
    chk("C3 T1 exact on the owner's series at r = 2.15m: a' - (1/ell^2 - a^2 - Pi.Pi/4) = 0 through y^12 at ell = inf "
        "and m (%d and %d nonzero coefficients); mutation R_yy = +4/ell^2 leaves %s at y^0"
        % (sum(v != 0 for v in r0), sum(v != 0 for v in r1), rm[0]),
        len(r0) == 13 and all(v == 0 for v in r0) and all(v == 0 for v in r1) and rm[0] != 0)
    # C4
    res = [(rc, es, check_leading(rc, es)) for rc in ("3", "43/20") for es in (Fr(0), Fr(1, 2), Fr(1))]
    L3 = [L for rc, es, (_, _, _, L) in res if rc == "3" and es == Fr(1, 2)][0]
    L2 = [L for rc, es, (_, _, _, L) in res if rc == "43/20"][0]
    chk("C4 S5 exact at r = 3m and 2.15m, ell = inf, 2m, m: w_r = R_rad(y + 3ey^2), w_th = R_tan(y + 3ey^2), a~ = "
        "-(RR/12)(y^3 + 5ey^4); against b4d_stage5.wall_exact, sim1_transition.eq17_rkk and b4d_stage7.slab_trace; r = 3m: %s, %s (y^2 at ell = 2m: "
        "%s, %s); r = 2.15m: %s, %s" % (L3["R_rad"], L3["R_tan"], L3["wr"][2], L3["wth"][2], L2["R_rad"], L2["R_tan"]),
        all(a and b and c_ for _, _, (a, b, c_, _) in res) and L3["R_rad"] == sp.Rational(-2, 81)
        and L3["R_tan"] == sp.Rational(1, 27) and L3["wr"][2] == Fr(-1, 27) and L3["wth"][2] == Fr(1, 18)
        and L2["R_rad"] == sp.Rational(-12000, 312481) and L2["R_tan"] == sp.Rational(2000, 7267))
    # C5
    ph = pade_honesty()
    conv = [v for v in ph["rows"] if abs(v[3] - v[4]) <= 1e-9 * abs(v[4])]
    worst_conv = max(abs(v[1] - v[4]) / abs(v[4]) for v in conv)
    lit = {v[0]: abs(v[1] - v[2]) / abs(v[2]) for v in ph["rows"]}
    at6 = [v for v in ph["rows"] if v[0] == 0.6][0]
    pade32, sum24 = abs(at6[1] - at6[4]) / abs(at6[4]), abs(at6[2] - at6[4]) / abs(at6[4])
    dclean = abs(ph["clean_002"] - ph["raw_002"])
    chk("C5 Pade honesty (r = 2.15m, ell = m, N = 24): raw-Pade w_r equals the converged partial sums (orders 28 and 32 "
        "agree to 1e-9: y <= %.1f) to %.1e relative, and the order-24 partial sums to %.1e at y = 0.5; at y = 0.6 the "
        "order-24 sums have not converged (%.1e from order 32) and the raw Pade is nearer the order-32 sums (%.1e) -- "
        "the spec's 1e-7 at 0.6 fails on the partial sums, not the Pade (%.1e); mutation through b4d_stage5._clean "
        "differs by %.2e at y = 0.02 (%.0f%%)" % (max(v[0] for v in conv), worst_conv, lit[0.5], sum24, pade32, lit[0.6],
                                                 dclean, 100 * dclean / abs(ph["raw_002"])),
        worst_conv < 1e-7 and max(v[0] for v in conv) >= 0.4 and lit[0.5] < 1e-7 and pade32 < sum24 and dclean > 1e-4)
    # C6
    nh = near_horizon()
    nm = near_horizon(B4._schwarzschild)
    chk("C6 near horizon: R^a_b(r = 2m) = %s; F ~ %s x, H ~ %s x^2; AdS2 curvature %s (radius 2m); mutation "
        "(Schwarzschild data) gives H/x^2 -> %s" % (nh["R_mixed"], nh["F_lead"], nh["H_lead"], nh["AdS2_R"],
                                                   nm["H_lead"]),
        nh["R_mixed"] == [sp.Rational(-1, 4), sp.Rational(-1, 4), sp.Rational(1, 4), sp.Rational(1, 4)]
        and nh["F_lead"] == sp.Rational(1, 2) and nh["H_lead"] == 1 and nh["AdS2_R"] == sp.Rational(-1, 2)
        and nm["H_lead"] != 1)
    # C7
    te = throat_equations()
    tm = throat_equations(s2=-1)
    rows01 = {es: throat_row(Fr(es)) for es in ("0", "1")}
    rows_all = [throat_row(e_) for e_ in (Fr(1, 2), Fr(4))] + list(rows01.values())
    tbm = throat_bulk(Fr(1, 2), s2=-1.0)
    sm = tbm["sol0"]
    gm = np.linspace(0, 0.95 * sm.t[-1], 500)
    V = sm.sol(gm)
    consm = V[2]**2 + V[3]**2 + 4 * V[2] * V[3] - 1.5 - 1 / (4 * V[1]**2) + 1 / (4 * V[0]**2)
    scm = V[2]**2 + V[3]**2 + 1 / (4 * V[0]**2) + 1 / (4 * V[1]**2) + 1.5
    mutc = float(np.max(np.abs(consm) / scm))
    chk("C7 throat ODEs from a sympy 5D Ricci: p', q' residuals %s, %s; xx = tt (%s), phph = thth (%s); constraint = "
        "%s x coded; R_yx = %s; K_th residual %s; constraint held to %.1e relative below 0.95 y_s on the zeroth-order "
        "solve (ell = inf, 2m, m, m/4); mutation (S2 curvature flipped): coded q' residual %s, constraint %.2f relative"
        % (te["P"], te["Q"], te["xx_tt"], te["ph_th"], te["constraint_ratio"], te["yx"], te["K"],
           max(r_["cons_rel"] for r_ in rows_all), tm["Q"], mutc),
        te["P"] == 0 and te["Q"] == 0 and te["xx_tt"] == 0 and te["ph_th"] == 0 and te["constraint_ratio"] == 2
        and te["yx"] == 0 and te["K"] == 0 and max(r_["cons_rel"] for r_ in rows_all) < 1e-11 and tm["Q"] != 0
        and mutc > 0.1)
    # C8
    tf = throat_first_order()
    tbx = throat_bulk(Fr(1), mut=0.5)
    tbd = throat_bulk(Fr(1), b1_0=1.5)

    def maxcon(tb):
        s, ys = tb["sol"], tb["y_s"]
        Z = s.sol(np.linspace(1e-3 * ys, 0.9 * ys, 2000))
        mom = -0.75 * Z[7] + Z[8] / 4 - Z[9] + Z[6] * (Z[2] - Z[3])
        ham = (2 * Z[4] / Z[0]**2 - Z[5] / Z[0]**2 + Z[6] / (2 * Z[1]**2) + 3 * Z[6] / Z[0]**2
               + (Z[7] + Z[8]) * (Z[2] + 2 * Z[3]) + 4 * Z[9] * Z[2] + 2 * Z[9] * Z[3])
        return float(np.max(np.abs(mom))), float(np.max(np.abs(ham)))
    mx, hx = maxcon(tbx)
    md, hd = maxcon(tbd)
    chk("C8 O(x) equations from sympy: a1'', b1'', c1'' residuals %s; momentum constraint = %s x coded; O(x) "
        "Hamiltonian residual %s; data from eq. (17): a1, b1, c1 = %s; along the solution |mom| <= %.1e, |ham| <= %.1e "
        "below 0.9 y_s; mutations: b1'' perturbed gives |mom| %.2f, wrong data b1 = 3/2 gives |ham| %.2f"
        % (tf["dd"], tf["mom_ratio"], tf["ham"], tf["data"], max(r_["mom"] for r_ in rows_all),
           max(r_["ham"] for r_ in rows_all), mx, hd),
        all(v == 0 for v in tf["dd"]) and tf["mom_ratio"] == 1 and tf["ham"] == 0
        and tf["data"] == (sp.Rational(-1, 2), sp.Rational(5, 2), 1) and all(v == 0 for v in tf["O1_zero"])
        and max(r_["mom"] for r_ in rows_all) < 1e-6 and max(r_["ham"] for r_ in rows_all) < 1e-6
        and mx > 1e-3 and hd > 1e-3)
    # C9, C10
    tv = throat_vs_owner()
    ratios = [v for y in tv["ratio"] for v in tv["ratio"][y]]
    rich = [abs((2 * tv["own"]["401/200"][y][i] - tv["own"]["201/100"][y][i]) / tv["ode"][y][i] - 1)
            for y in tv["ode"] for i in (0, 1)]
    r005 = [v for y in tv["rel"]["401/200"] for v in tv["rel"]["401/200"][y]]
    r01 = [v for y in tv["rel"]["201/100"] for v in tv["rel"]["201/100"][y]]
    chk("C9 throat against owner (ell = 2m, N = 20, y = 0.13 and 0.26): w_th, a~ within %.1f%% of the ODE at r = 2.005m "
        "(a loose 5%% bound: the ratio and the extrapolation clauses carry the check) and %.1f%% at 2.01m; the gap is "
        "linear in x (ratio %s, 2 +- 0.3), and the x -> 0 extrapolation 2 own(2.005) - own(2.01) meets the ODE to "
        "%.2f%% (< 0.5%%)" % (100 * max(r005), 100 * max(r01), ", ".join("%.3f" % v for v in ratios), 100 * max(rich)),
        max(r005) < 0.05 and all(abs(v - 2) <= 0.3 for v in ratios) and max(rich) < 0.005)
    chk("C10 W1(1.088) = %.4f against w_r(2.005m)/0.005 = %.4f (flat, N = 24): %.2f%%"
        % (tv["W1"], tv["wr_over_x"], 100 * abs(tv["wr_over_x"] / tv["W1"] - 1)),
        abs(tv["wr_over_x"] / tv["W1"] - 1) < 0.02)
    # C11
    sc = schwarzschild_control()
    wd = wedge()
    wm = wedge("sinh")
    chk("C11 exact controls: Schwarzschild data (ell = m) terminate %s, w_r = w_th = a~ = 0 exactly %s; the AdS4-sliced "
        "wedge is Einstein (%s), a = %s, s1 = %s, s2 = %s, identity: equal %s (the reflection symmetry gives s2 = s1 for "
        "either warp; the sinh warp gives %s too), T5 bound gap %.1e; mutation sinh warp: caught by the Einstein "
        "residuals only, %s" % (sc["terminates"], sc["w_r"] and sc["w_th"] and sc["at"],
                                all(v == 0 for v in wd["einstein"]), wd["a"], wd["s1"], wd["s2"], wd["equal"],
                                wm["equal"], wd["bound_gap"], [v for v in wm["einstein"] if v != 0][:1]),
        sc["terminates"] and sc["w_r"] and sc["w_th"] and sc["at"] and all(v == 0 for v in wd["einstein"])
        and wd["equal"] and wd["bound_gap"] < 1e-14 and any(v != 0 for v in wm["einstein"]))
    # C12
    ln = lemma_n()
    lm = lemma_n(sign=+1)
    chk("C12 Lemma N: Gamma^y_ab = -(1/2) d_y g_ab %s; y'' - w_r B r'^2 = %s; identity: warped products w = %s (the "
        "three components share one factor e^(2f)); mutation (+1/2) connection %s, ray residual nonzero %s" % (
            ln["connection"], ln["ray"], ln["warped_w"], lm["connection"], lm["ray"] != 0),
        ln["connection"] and ln["ray"] == 0 and ln["warped_w"] == [0, 0] and not lm["connection"] and lm["ray"] != 0)
    # C13 (robust: a mutation that leaves W1 without a zero gives y* = None and nan thresholds -> FAIL, never a crash)
    nan = float("nan")
    try:
        lw, _ = ell_w()
        lc30, _ = ell_c(30)
        lw = nan if lw is None else float(lw)
        lc30 = nan if lc30 is None else float(lc30)
        r0_, r1_ = rows01["0"], rows01["1"]
        have = r0_["y_star"] is not None and r1_["y_star"] is not None
        g_ = lambda r_, k: nan if r_[k] is None else float(r_[k])
        vals = (g_(r0_, "y_s"), g_(r0_, "y_star"), g_(r0_, "K_ratio"), g_(r1_, "y_s"), g_(r1_, "y_star"),
                g_(r1_, "K_ratio"), lw, lc30)
        c13 = (have and abs(vals[0] - PIN["0"]["y_s"]) < 2e-5 and abs(vals[1] - PIN["0"]["y_star"]) < 2e-5
               and abs(vals[2] / PIN["0"]["K_ratio"] - 1) < 5e-3 and abs(vals[3] - PIN["1"]["y_s"]) < 2e-5
               and abs(vals[4] - PIN["1"]["y_star"]) < 2e-5 and abs(vals[5] / PIN["1"]["K_ratio"] - 1) < 5e-3
               and abs(lw - PIN["ell_W"]) <= 0.05 and abs(lc30 - PIN["ell_c30"]) <= 0.05)
        msg = ("C13 S8's table: ell = inf y_s %.5f, y* %.5f, K(y*)/K_bs %.3g; ell = m y_s %.5f, y* %.5f, K %.3g; "
               "ell_W = %.2fm; ell_c(30) = %.2fm (pinned: %s)"
               % (vals + ({k: PIN[k] for k in ("0", "1", "ell_W", "ell_c30")},)))
    except Exception as exc:                                   # report, never crash (C14 must still run)
        c13, msg = False, "C13 S8's table: raised %s: %s" % (type(exc).__name__, exc)
    chk(msg, bool(c13))
    # C14
    g = address_guard()

    def leak(separation):
        return separation
    gm_ = address_guard(extra_keys={"arrival_time": 1.0}, extra_funcs=(leak,))
    chk("C14 address guard: %d functions, no argument names a plane separation (%s); %d bank keys, none names a "
        "distance, time, redshift or speed (%s); mutation flags %s and %s" % (
            g["n_funcs"], g["bad_args"] or "none", g["n_keys"], g["bad_keys"] or "none", gm_["bad_args"],
            gm_["bad_keys"]),
        not g["bad_args"] and not g["bad_keys"] and g["n_keys"] > 10 and gm_["bad_args"] and gm_["bad_keys"])
    # C15
    dts = [down_throat_class(Fr(es)) for es in ("0", "1")]
    try:
        cw = ell_w_class()
    except Exception as exc:                                   # report, never crash
        cw = {"ell": float("nan"), "err": "%s: %s" % (type(exc).__name__, exc)}
    cw_ok = math.isfinite(cw["ell"]) and abs(cw["ell"] - PIN["ell_W_class"]) <= 0.05 and cw["ell"] < PIN["ell_W"]
    chk("C15 down the throat (S7, corrected): f = %g x^lam (lam %s) over the throat fields at ell = inf and m, the NEC "
        "exact in the slope on the throat metric through O(x): radial and angular NEC hold at the %s samples below the "
        "crossover x_c/2: %s; failures (%s) only above x_c/2: %s; leading order f'' - f'/2 <= alpha^2 x W1 to %s at "
        "x <= 1e-8; control: lam = 3/4 violates the radial NEC at every depth: %s; identity (W1 < 0 below y* by y*'s "
        "definition, f_uu > 0): the first build's f'' <= alpha^2 x W1 (lapse term dropped) excludes every sampled depth "
        "below y* (%s of %s); identity (at x = 1e-14 the slope terms are below 1e-7, so it holds for any f -> 0; that the "
        "radial equation forces f' -> 0 is deduced): the umbilic member's k_t - k_th -> w_th(depth) to %s, %s; its trace "
        "at ell = m reads ell a(depth) <= %.6f, trace minus ell a %.0e (< 1e-5): %s; positive energy in the class needs "
        "ell > %.2fm (pinned %.2f, below ell_W %.2f)" % (
            DT_C, "/".join("%g" % v for v in DT_LAMS), "/".join(str(d_["n_below_xc"]) for d_ in dts),
            all(d_["nec_holds"] for d_ in dts),
            "/".join(str(d_["n_fail"]) for d_ in dts), all(d_["fails_only_above_xc"] for d_ in dts),
            "/".join("%.1e" % d_["lead_dev"] for d_ in dts), all(d_["control_fails"] for d_ in dts),
            "/".join(str(d_["old_excludes_below_ystar"]) for d_ in dts), "/".join(str(d_["n_below_ystar"]) for d_ in dts),
            "/".join("%.0e" % d_["umbilic_ratio_dev"] for d_ in dts), all(d_["umbilic_closes"] for d_ in dts),
            dts[1]["ell_a_max"], dts[1]["trace_minus_ell_a"], dts[1]["trace_minus_ell_a"] < 1e-5,
            cw["ell"], PIN["ell_W_class"], PIN["ell_W"]),
        cw_ok and all(d_["nec_holds"] and d_["fails_only_above_xc"] and d_["control_fails"] and d_["umbilic_closes"]
            and d_["n_below_xc"] > 100 and d_["lead_dev"] < 0.05
            and d_["old_excludes_below_ystar"] == d_["n_below_ystar"] > 0 for d_ in dts)
        and dts[1]["ell_a_max"] <= -1 + 1e-9 and dts[1]["trace_minus_ell_a"] < 1e-5)
    # C16 (numerics re-verifier: no check exercised column_w, admissible, map_summary or decide).  One owner column
    # recomputed live, r = 2.05m at ell = inf (about 20 s): the verified prefix must be the value rule alone; under the
    # first build's prefix (value rule AND w-agreement) the prefix stops below the sign change of w_r and this column
    # has no admissible point.  decide(), admissible() and map_summary() on the bank, against pinned values.
    pc = PIN["c16"]
    try:
        col = column_w("41/20", Fr(0), with_k=False)
        rows_c = col["rows"]
        run_v, ver_run = True, True
        for z in rows_c:
            run_v = run_v and z["val_ok"]
            ver_run = ver_run and z["ver"] == run_v
        adm_cons = all(z["adm"] == (z["ver"] and z["sign_ok"] and z["wr"] >= 0 and z["wth"] >= 0) for z in rows_c)
        rising = [y_ for y_, sg in col["wr_zeros"] if sg > 0]
        adm_y = [z["y"] for z in rows_c if z["adm"]]
        wtop = max([z["y"] for z in rows_c if z["ver_w"]], default=0.0)
        bk = load_bank()
        bcol = bk["columns"]["41/20|0"]
        same = (len(bcol["rows"]) == len(rows_c)
                and all(a_["ver"] == b_["ver"] and a_["adm"] == b_["adm"] and abs(a_["y"] - b_["y"]) < 1e-12
                        for a_, b_ in zip(rows_c, bcol["rows"])))
        d2 = decide(bk, bk["throat"])["1/2"]
        cf2 = d2["confirm"][0] if d2["confirm"] else (None, float("nan"), float("nan"))
        ms_ = map_summary(bk)
        nadm = {es: len(v) for es, v in admissible(bk).items()}
        c16 = (len(rising) == 1 and abs(rising[0] - pc["wr_zero"]) <= 0.002 and len(adm_y) == pc["n_adm"]
               and abs(min(adm_y) - pc["adm_from"]) <= 0.002 and ver_run and adm_cons and same
               and d2["confirmed"] and cf2[0] == "401/200" and abs(cf2[1] - pc["edge_2m"]) <= 0.002
               and nadm == pc["adm_per_ell"] and ms_["n_ver"] == pc["n_ver"] and ms_["n_ver_settled"] == pc["n_settled"]
               and ms_["n_adm"] == pc["n_adm_total"] == sum(nadm.values()))
        msg = ("C16 the map's rules, live: column_w(r = 2.05m, ell = inf) recomputed: rising zeros of w_r %s (one, at "
               "%.3f +- 0.002), %d admissible points from y = %.3f (pinned %d from %.3f; the first build's w-prefix would "
               "stop at %.3f, below the zero, and admit none); verified = the running AND of the value rule: %s; "
               "admissible = verified, signs agreed and w >= 0: %s; rows equal to the bank's: %s.  On the bank: decide() "
               "at ell = 2m %s (%s, edge %.4f; pinned %.3f +- 0.002); admissible() per ell %s (pinned); map_summary "
               "%d verified, %d sign-settled, %d admissible (pinned %d/%d/%d)" % (
                   ", ".join("%.4f" % v for v in rising) or "none", pc["wr_zero"], len(adm_y),
                   min(adm_y) if adm_y else float("nan"), pc["n_adm"], pc["adm_from"], wtop, ver_run, adm_cons, same,
                   "CONFIRMED" if d2["confirmed"] else "not CONFIRMED", cf2[0], cf2[1], pc["edge_2m"],
                   "/".join(str(nadm[es]) for es in bk["es"]), ms_["n_ver"], ms_["n_ver_settled"], ms_["n_adm"],
                   pc["n_ver"], pc["n_settled"], pc["n_adm_total"]))
    except Exception as exc:                                   # report, never crash
        c16, msg = False, "C16 the map's rules, live: raised %s: %s" % (type(exc).__name__, exc)
    chk(msg, bool(c16))
    # C17 (item 172, S15): the coinciding limit.  At finite ell, along the approach to depth 0, P2's stress must tend to
    # the RS1 sheet: s = rho/sigma_RS -> -1 and the trace reading -> -1 (to 1e-5 on lam = 0.4 and the smooth family at
    # x = 1e-14), the NEC part -> 0, |s + 1| falling along x on all four profiles, rho_m -> -2 sigma_RS.  Mutations: the
    # two-sided Israel factor (nu/2: s -> -1/2) and the normal out of the slab (s -> +1) must fail the same test.  Flat
    # limit: rho > 0 at every sample and falling toward 0, on the first-order form to 1e-3.  The WEC window: d_+ at
    # ell = 32m pinned, 0 < d_+ < y*, the WEC failing at 0.9 and 0.99 d_+ and holding at 1.01 d_+ on all four profiles,
    # no d_+ at ell = m, d_+ = 0 (an infimum) at ell = inf, d_+/(24 m^2/ell) -> 1 at ell = 1024m.  S15's keys pass C14.
    pc = PIN["c17"]
    try:
        tbs17 = {k: throat_bulk(Fr(k)) for k in ("0", "1/32", "1")}
        co = {k: coinciding(Fr(k), tb=tb_) for k, tb_ in tbs17.items()}

        def lim_ok(c_):
            return (c_["worst_s"] < 1e-5 and c_["worst_tau"] < 1e-5 and c_["worst_nec_fast"] < 1e-5 and c_["monotone"]
                    and c_["nec_ok"] and abs(c_["rho_m_rs"] + 2) < 1e-5)
        base = all(lim_ok(co[k]) for k in ("1/32", "1"))
        m_nu = coinciding(Fr(1), tb=tbs17["1"], nu=0.5, full=False)
        m_n = coinciding(Fr(1), tb=tbs17["1"], n_sign=-1, full=False)
        caught = not lim_ok(m_nu) and not lim_ok(m_n)
        f0 = co["0"]
        flat_ok = (f0["flat_pos"] and f0["flat_to_0"] and f0["flat_lead_dev"] < 1e-3 and f0["nec_ok"]
                   and f0["wec"]["d_plus"] == 0.0)
        w32, wp32 = co["1/32"]["wec"], co["1/32"]["wec_profiles"]
        sc = d_plus_scaling((Fr(1, 1024),))[0]
        wec_ok = (w32["d_plus"] is not None and abs(w32["d_plus"] - pc["d_plus_32"]) <= 2e-3
                  and 0 < w32["d_plus"] < w32["y_star"] and wp32["below_fails"] and wp32["above_holds"]
                  and co["1"]["wec"]["d_plus"] is None and sc["ratio"] is not None
                  and abs(sc["ratio"] - pc["ratio_1024"]) < 1e-3)
        g17 = address_guard(extra_keys=co)
        c17 = base and caught and flat_ok and wec_ok and not g17["bad_keys"]
        sl = lambda c_: c_["profiles"]["lam 0.4"][-1]["s"]
        msg = ("C17 the coinciding limit (S15, item 172): along the approach to depth 0, x -> 1e-14, s = rho/sigma_RS -> -1 "
               "to %.0e (32m) and %.0e (m), the trace reading to %.0e/%.0e, the NEC part to %.0e/%.0e sigma_RS, rho_m -> "
               "%.6f sigma_RS: %s; mutations caught: the two-sided factor nu/2 gives s = %.4f, the normal out of the slab "
               "s = %+.4f: %s; flat: rho > 0 and falling toward 0 (rho/nu at 1e-14, lam 0.1: %.2e), on the first-order "
               "form to %.0e: %s; WEC window: d_+(32m) = %.4f (pinned %.4f +- 0.002), below y* %.4f, failing at 0.9/0.99 "
               "d_+ %s, holding at 1.01 d_+ %s; d_+(m) %s; d_+(inf) = %s; d_+/(24 m^2/ell) at 1024m = %.5f (pinned %.4f): "
               "%s; S15's keys name no distance, time or speed: %s" % (
                   co["1/32"]["worst_s"], co["1"]["worst_s"], co["1/32"]["worst_tau"], co["1"]["worst_tau"],
                   co["1/32"]["worst_nec_fast"], co["1"]["worst_nec_fast"], co["1/32"]["rho_m_rs"], base,
                   sl(m_nu), sl(m_n), caught, f0["profiles"]["lam 0.1"][-1]["rho"], f0["flat_lead_dev"], flat_ok,
                   w32["d_plus"] or float("nan"), pc["d_plus_32"], w32["y_star"], wp32["below_fails"],
                   wp32["above_holds"], "none" if co["1"]["wec"]["d_plus"] is None else co["1"]["wec"]["d_plus"],
                   f0["wec"]["d_plus"], sc["ratio"] or float("nan"), pc["ratio_1024"], wec_ok, g17["bad_keys"] or "none"))
    except Exception as exc:                                   # report, never crash
        c17, msg = False, "C17 the coinciding limit: raised %s: %s" % (type(exc).__name__, exc)
    chk(msg, bool(c17))
    print("selftest: %d/%d (%.0f s)" % (ok, n, time.monotonic() - t0))
    return ok == n


if __name__ == "__main__":
    if "--regenerate" in sys.argv:
        regenerate()
    elif "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    else:
        report(load_bank(), compute_live())
