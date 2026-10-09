#!/usr/bin/env python3
"""epass_pairing.py -- E-PASS fix round, a standalone [FREE] owner: Lemma S (the pairing law at a horizon of fixed size)
and Lemma K (a net-flux crossing kinks the bulk horizon), with the two identities they rest on (the contracted Gauss
equation, SMS eq. (3), and null transport with Raychaudhuri).  Build specification: lemmas/EPASS-DESIGN-SPEC.md, X13,
X14 and checks C15-C19 of its section 8, as corrected by the verification of this module (findings F1-F9 of the
refutation, PO-1-PO-14 of the overclaim review; departures below).  sim2_passage.py imports this module by path for
its X13 and X14; it is never copied there.  Computed, READ and deduced; not verified; not seated; 2026-10-09.

CLI:  --selftest (every check, each able to fail; budget < 90 s)
      --mutants  (runs every named mutation of every check and shows that the check FAILS under it; exit 1 if any
                  mutation passes)
      --json PATH (writes compute(): every value X13 and X14 need, each row labelled)

LABELS.  Every result row carries one of: computed / READ (verbatim + PDF page) / deduced / STRUCTURAL /
standard-not-READ / OPEN.  The board's readings are named H-... and kept apart from M's words, which are quoted
verbatim with typing kept, from M-RULINGS-2026-10-03.md.  A negative result is reported as plainly as a positive one
(M-IRREFUTABLE, 135).  Tags: [FREE] holds whatever carries the corridor (a plane, a sheet, or the bulk alone);
[PLANE] uses eq. (17) as our plane's own metric (the board's pre-179 configuration, kept as its comparison case).

M'S WORDS USED (verbatim, typing kept; never paraphrased as M's):
  129 (1)  "1 - no. It contains matter, you, me, this current universe, just not a corridor for transit because the
           corridor is a bridge, so it adds nothing to either position."
  132      excerpt (M's restatement of the board's question omitted): "yes. And the passage is one way by nature, a
           black hole in and a white hole out, side views of the same corridor object"
           and, on M's next line, M's own correction: "*different views of the same object"
  139 (2)  "2 - positive, and you have to prove it."
  162      "Although the chain illustrates a corridor, I submit that it may be more like a black hole, containing both
           mouths and throat at once. The throat doesn't change size because the whole chain object only every takes on
           the size that contains the README upon opening. It is and always will be only the size that is needed to
           hold the object once and at once"
  172 (1)  M chose: "Yes, it may"  (position 2's piece may carry the README's stress)
  176      "But what if it is in fact entanglement?"
  177      M chose: "Yes, that is the appearance"
  179      "Let's approach this from a different angle. We know the corridor doesn't not sit on either position's plane,
           it only bridges them. So one could surmise that the corridor is exclusive to the bulk."
  180      "Let's approach this from a different angle. We know the corridor *does not sit on either position's plane,
           it only bridges them. So one could surmise that the corridor is exclusive to the bulk."
  183      M chose: "Yes: never violated as a pair"  (to the board's question on 117/120's "never violated")
  184      "There are no matter free planes"
  187 (3)  M chose: "Seat both"  (clauses (G) and (Z) of the Warp Theorem, as the board re-worded them)

WHAT IS COMPUTED HERE
  X13 LEMMA S [FREE] (computed as identities; deduced).
    (b) BULK FORM -- the primary statement under 179/180 (the corridor sits on neither plane, exclusive to the bulk).
        pairing_bulk(gvv) on the family D dy^2 + g_vv dv^2 + 2B dv du + C dOmega^2, g_vv = -A(y,u) u^2 (degenerate) or
        -A(y,u) u (non-degenerate), A, B, C, D arbitrary functions of (y, u) (no g_uu, no y- or angular cross terms,
        no rotation), NO field equation used: R(xi,xi)|_{u=0} = 0 (computed).  The same zero is computed on a
        NON-stationary member that keeps u = 0 null (g_vv -> g_vv (1 + eps sin v), B -> B (1 + eps sin v)): stationarity
        is NOT the premise.  The premise, computed: R(xi,xi)|_H = -dtheta/dv + kappa theta - theta^2/3 - sigma^2 (the
        Raychaudhuri route, from the cross-section's metric alone, agrees with the Riemann route on every variant), so on
        a non-expanding horizon (theta = 0) R(xi,xi) = -sigma^2 <= 0: shear at fixed volume gives -0.014138938637006316
        (eps = 1/10, v = 3/10, on the stand-ins; Wolfram agrees).
        With Einstein + Lambda_5 and g(xi,xi)|_H = 0, kappa_5^2 T5(xi,xi) = R(xi,xi) (deduced; not a separate test).
        So across a horizon that keeps its size (162, read as theta = 0 through H-FIXED-SIZE-AS-THETA-ZERO, the board's,
        put to M) the net 5D null flux along each generator is -sigma^2/kappa_5^2 <= 0: the README's positive flux must
        be cancelled by a partner at least as large, exactly as large iff the horizon is shear-free (deduced).  With
        H-NEC-NEVER-VIOLATED-AS-PAIR (183, carried as M's: zero net null energy along each light ray) sigma = 0 and the
        pair is exact (deduced).
    (a) SHEET FORM -- applies to whichever sheet the README is on (172 (1): position 2's piece may carry it).
        pairing_sheet(gvv): a sheet y = F(u) (F arbitrary) in dy^2 + g_vv dv^2 + 2 sqrt2 alpha(y)^2 dv du +
        4 beta(y)^2 dOmega^2 with alpha, beta arbitrary, g_vv = -alpha^2 u^2/2 (degenerate, u_H = 0) or
        -alpha^2 (u^2 - 1/9)/2 (non-degenerate, u_H = 1/3), and on the bulk family of (b): K(xi,xi)|_H = 0 (computed).
        The same zero is computed on non-stationary members that keep u_H null and on a horizon whose section GROWS
        (C -> C (1 + eps v)): the sheet form is blind to stationarity and to growth.  Its premise, computed: u = u_H null
        at every depth and the sheet tangent to xi (K(xi,xi) = -kappa n.xi: a tilted sheet y = F(u) + eps v gives
        K(xi,xi) != 0 where kappa != 0).  S(xi,xi) = -nu [K(xi,xi) - (xi.xi) K] = -nu K(xi,xi) on H (deduced, since
        g(xi,xi)|_H = 0).  So wherever the bulk null surface reaches the sheet along xi -- the brane horizon's generators
        are generators of a bulk null hypersurface C^2 up to the sheet (Lemma K's C^2 case) -- the net surface null flux
        across the horizon vanishes on that sheet, at any tension, any law, and with matter (the identity is
        law-independent; 184 makes the matter case the one that matters), whether or not the horizon grows: the
        README's T^R(xi,xi) >= 0 must be cancelled on the same sheet, generator by generator, by
        T^c(xi,xi) = -T^R(xi,xi) (computed for sheets y = F(u); deduced for any sheet tangent to xi).  A held
        AdS2-invariant stress has tau(xi,xi) = -rho g(xi,xi) and pi(xi,xi) proportional to g(xi,xi) (by construction:
        tau is proportional to g on the (v,u) block), so both vanish on the horizon; the premise is regularity (finite
        rho in the static frame -- a static stress with rho ~ 1/F, singular on the future horizon, could keep a finite
        T(xi,xi)).  So a regular held stress cannot be the partner: it must be a genuine negative null flux (deduced).
    (c) THE WEYL TERM GIVES NOTHING.  On the bulk family of (b), E~(xi,xi) = R(xi,n,xi,n)|_{u=0} = 0 (computed), so
        E(xi,xi) = E~(xi,xi) - R(xi,xi)/3 = 0 (SMS eq. (A10), first line, READ PDF p.6, contracted with null tangent
        xi), also on the null-preserving non-stationary member; a growing section gives E~ = 0 but E != 0 (C18b catches
        it through E).  On eq. (17)'s own data (owner B4._eq17 via sim2_facing, by path) R4(xi,xi)|_{r=2m} = 0
        (computed, [PLANE]); with SMS's own eq. (17) (READ PDF p.3; it assumes Z2 symmetry, eq. (16), and matter
        confined to the brane, eq. (13); its E is "the limiting value at chi = +0 or -0") and the held stress's
        tau(xi,xi) = pi(xi,xi) = 0, E(xi,xi) = 0 at chi -> +-0 there (deduced; H-Z2-PIECES, the board's, is the [PLANE]
        hypothesis).  A bulk field cannot change a sheet's surface flux (deduced).
    (d) THE PAIR AND THE READINGS.  The ledger (pair_crossing): README member T^R(xi,xi) = 2 per mu in eq. (17)'s
        ingoing chart ([PLANE] normalisation, l.xi = -sqrt2; the cancellation is [FREE]), partner -2, net 0 BY
        CONSTRUCTION (the partner is defined as -T^R; not a finding).  The full pair tensor, computed [PLANE] for a
        null-dust partner whose direction is tilted by b along the sphere (pair_tensor_eq17): nonzero for b != 0, and
        pi(xi,xi) of held stress + README + partner = -b^2 mu^2/2 by two routes (SMS eq. (20) on the full tensor; the
        null-dust algebra of the pair alone), independent of a static held stress (a held momentum flux tau_v theta = j
        would enter, and would cancel pi(xi,xi) at b = -sqrt2 j/(4 mu): C19c's mutation).  Deduced ([PLANE] with SMS (17)
        under Z2, H-Z2-PIECES, a static held stress, and the bulk near the plane in the family of (b), non-expanding and
        shear-free): R4(xi,xi) = 0 (C18c), E(xi,xi) = 0 (from the bulk side, C18b; not from (c)'s held-stress
        deduction, which assumed no README) and tau(xi,xi) = 0 (the pair) give pi(xi,xi) = 0, so b = 0 -- among
        null-dust partners only the README's exact reverse is admitted, and the pair's total stress tensor is then
        ZERO: the README's stress is cancelled outright, a plain negative (135).  The board notes, without claiming it
        as M's meaning, that this is the shape of 129 (1)'s "it adds nothing to either position" (carried in the record
        as H-BRIDGE-ADDS-NOTHING, about the corridor, not the README's crossing).
        READINGS: H-PAIR-CANCELS-ON-THE-HORIZON and H-PARTNER-IS-THE-COUPLING (the board's), re-read under 183: M chose
        "Yes: never violated as a pair"; the record carries H-NEC-NEVER-VIOLATED-AS-PAIR as M's (the gloss "zero net
        along each light ray" is the board's wording of the option M chose).  The exact +/- null pair Lemma S demands
        is then admitted under 177 through the board's H-PARTNER-IS-THE-COUPLING, so E-PASS's crossing at fixed size
        is OPEN (the partner's supply is beyond the board's instruments), NOT refuted.  The pair's total is ZERO per
        light ray; it is never reported as "positive" (spec pitfall 13; 139 (2)'s positivity is a separate question).
  X14 LEMMA K [FREE for sheets] (computed; deduced).
    tangent_deflection(Kvv): in Gaussian normal coordinates a null geodesic tangent to the sheet along the horizon
    generator has y'' = -Gamma^y_vv (from the connection) = K_vv, where K_vv = (1/2) Lie_n g_vv = (1/(2 lapse)) d_y g_vv
    is computed from the metric directly, with no Christoffel symbol (an independent route; with every Christoffel sign
    flipped the two disagree).  The computed content is the Gaussian-normal identity Gamma^y_vv = -K_vv (standard).  In
    a lapse-2 chart the proper normal displacement s = 2y obeys s'' = K_vv (computed); y'' itself is K_vv/2 (the chart
    mutation).  deflection_numeric(S_vv, nu=1) integrates that geodesic in an explicit Gaussian normal metric with
    h_vv = -u^2/2 + 2 y K_vv + y^2/3 (and warped cross and angular terms), K_vv = -S_vv/nu, and reports whether it stays
    on the sheet and in y >= 0 to 1e-12.  S_vv = 0 stays; S_vv > 0 leaves the kept side (positive brane null energy
    pulls bulk light onto the sheet); S_vv < 0 leaves the sheet into the bulk.  So a bulk horizon C^2 up to the sheet,
    with the brane horizon as its trace, carries no net flux there (deduced); a net-flux crossing is a five-dimensional
    event (E-NS): the bulk horizon creases at the sheet or separates from the brane horizon.  The smooth-horizon
    identity (design 4's Lemma A) holds where the horizon is smooth but cannot be integrated across the README's
    support: its B_start budget and its "q >= 0 absorbs classically" are WITHDRAWN.
  C15 (computed) contracted Gauss (SMS eq. (3)) on dy^2 - A dt^2 + B dr^2 + C dOmega^2 (explicit polynomials) at
      (t, r, theta) = (1/3, 5/2, 7/10): residual 0; the R(k,n,k,n)-sign mutation gives -0.62486.
  C16 (computed) transport R(k,e,k,e) + dB_ee/dlambda + B_ee^2 = 0 (e parallel) and Raychaudhuri on
      -2 du dv + a^2 dy^2 + b^2 dz1^2 + c^2 dz2^2, with sigma^2 the square of the trace-free part over the transverse
      count taken from the metric (3) and an isotropic control (a = b = c must give sigma^2 = 0); the coordinate
      derivative of the component B_yy leaves 2 a_v^2/a^2.

PREMISES, AS COMPUTED (this replaces spec pitfall 3's "Lemma S needs stationarity DURING the crossing", which the
verification refuted, F1/PO-1).  BULK FORM: a non-expanding horizon (theta = 0), with R(xi,xi) = -sigma^2 <= 0 and = 0
iff shear-free; stationarity is one sufficient case.  SHEET FORM: u = u_H null at every depth and the sheet tangent to
xi; it holds through growth.  So refusing H-STATIONARY-CROSSING while 162's fixed size is kept still demands the pair
(net <= 0 per generator in the bulk, exactly 0 on a sheet).  A net-flux crossing (E-NS) needs, in the bulk, expansion
of the generators (theta != 0: the horizon changes size, which 162 forbids as read through H-FIXED-SIZE, M's, and
H-FIXED-SIZE-AS-THETA-ZERO, the board's, put to M) or, on a sheet, a crease or separation of the bulk horizon at the
sheet (Lemma K); growth alone does not release a sheet's pair.  The pair must be exact to the order at which theta and
sigma are held at zero: a residual net flux delta S along a generator bends it off the sheet at second order in the
affine parameter (Lemma K).  These are statements about the families computed (deduced beyond them).

READS (verbatim, transliterated to ASCII; read on 2026-10-09 from the page text of arXiv gr-qc/9910076v3 served by
the alphaXiv connector -- a direct arXiv fetch was refused by the egress proxy; PDF pages as served):
  SMS PDF p.2: "The notation basically follows Wald's text [18]."
  SMS PDF p.2, eq. (3): "Contracting the Gauss equation (1) on alpha and gamma, we find (4)R_mu nu = (5)R_rho sigma
      q^rho_mu q^sigma_nu - (5)R^alpha_beta gamma delta n_alpha q^beta_mu n^gamma q^delta_nu + K K_mu nu -
      K^alpha_mu K_nu alpha. (3)"  (contracted with a null k tangent to the sheet: the C15 form.)
  SMS PDF p.3, eq. (13): "T_mu nu = -Lambda g_mu nu + S_mu nu delta(chi), (13)"; eq. (16): "Now we impose the
      Z2-symmetry on this spacetime, with the brane as the fixed point. ... K+_mu nu = -K-_mu nu = -1/2 kappa^2_5
      (S_mu nu - 1/3 q_mu nu S). (16)"; eq. (17): "(4)G_mu nu = -Lambda_4 q_mu nu + 8 pi G_N tau_mu nu + kappa^4_5
      pi_mu nu - E_mu nu, (17)" (SMS's own eq. (17), never the board's eq. (17) metric); eq. (20): "pi_mu nu = - 1/4
      tau_mu alpha tau^alpha_nu + 1/12 tau tau_mu nu + 1/8 q_mu nu tau_alpha beta tau^alpha beta - 1/24 q_mu nu
      tau^2"; and "It should be noted that E_mu nu in the above is the limiting value at chi = +0 or -0 but not the
      value exactly on the brane."
  SMS PDF p.6, eq. (A8): "E~_mu nu = (5)R_mu alpha nu beta n^alpha n^beta = -Lie_n K_mu nu + K_mu alpha K^alpha_nu";
      eq. (A10), first line: "E_mu nu = E~_mu nu - 1/3 q_mu nu (5)R_alpha beta n^alpha n^beta - 1/3 q^alpha_mu
      q^beta_nu (5)R_alpha beta + 1/12 q_mu nu (5)R" (algebraic; it does not need the a_mu = 0 the appendix assumes).
  standard-not-READ: R(xi,xi) = 0 on a Killing horizon (computed here for the families named); geodesic generators of
  a C^2 null hypersurface; the Raychaudhuri equation; Gamma^y_mn = -K_mn in Gaussian normal coordinates.

CROSS-CHECK: computed (Wolfram 15.0.1 through the connector, by the fix session, 2026-10-09; not run by this module;
the Wolfram inputs are kept verbatim in WOLFRAM_CROSSCHECK and WOLFRAM_CROSSCHECK_PAIR below, so they can be
re-run).  See WOLFRAM_CROSSCHECK_RESULT.

DEPARTURES FROM THE SPEC.  (1) C19's "leaves y >= 0 if and only if S_vv != 0" is corrected: the tangent geodesic
leaves the SHEET iff S_vv != 0; it leaves the kept side y >= 0 iff S_vv > 0; S_vv < 0 sends it into the bulk (y > 0),
which is the separation branch of Lemma K.  (2) Pitfall 3 ("Lemma S needs stationarity") is corrected as above; the
spec's mutation g_vv + eps y sin v (C17, C18) is caught because u = u_H stops being null (g(xi,xi) = eps y sin v there),
not because of v-dependence: it is kept, relabelled "off_null", beside mutations that keep u_H null and break the real
premise (shear, growth, a tilted sheet).  (3) Added checks: C18s (the bulk premise: Raychaudhuri route; shear at fixed
size gives R(xi,xi) = -sigma^2 < 0), C18b (X13 (c) on the general bulk), C18c (X13 (c) on the board's eq. (17) data),
C19b (the pair ledger through Lemma K; the integration is decisive and a stub integrator is caught), C19c (the pair
tensor's pi(xi,xi) [PLANE], two routes), CG (guards).  (4) A symbolic zero is accepted only with a numeric witness
< 1e-12 on concrete stand-in functions; a nonzero witness is the certificate that a mutation really is nonzero.

OWNERS IMPORTED BY PATH, NEVER COPIED: lemmas/sim2_facing.py (BANNED_ARGS, BANNED_KEYS, B4._eq17 = b4_static's eq. (17)
data, lemma_n for the cross-reference of Lemma N's connection).  BANNED_KEYS of lemmas/sim2_passage.py are read from
its source text with ast (that file is being edited by another run, so it is parsed, never executed).
Conventions: R^a_bcd = d_c G^a_bd - d_d G^a_bc + G^a_ce G^e_bd - G^a_de G^e_bc, R_bd = R^a_bad: standard-not-READ that
this agrees with Wald's on R_abcd and R_ab; SMS PDF p.2 (READ): "The notation basically follows Wald's text".  Units
m = 1.  No argument names a separation; no output key names a distance, time, redshift or speed (139 (4), 101 (7)).
"""
import argparse
import ast
import contextlib
import functools
import importlib.util
import inspect
import io
import json
import math
import os
import re
import sys
import time as _wall
from fractions import Fraction as Fr

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
SF_PATH = os.path.join(HERE, "sim2_facing.py")
SP_PATH = os.path.join(HERE, "sim2_passage.py")
LABELS = ("computed", "READ", "deduced", "STRUCTURAL", "standard-not-READ", "OPEN")
ZERO_TOL = 1e-12            # the spec's tolerance for "stays" and for a numeric zero witness


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, os.path.dirname(D68)]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        return mod
    finally:
        sys.path[:] = saved


SF = _load(SF_PATH, "epass_pairing_sim2_facing")


def _passage_banned_keys():
    """sim2_passage.BANNED_KEYS, read from the source text (never executed: another run edits that file)."""
    try:
        tree = ast.parse(open(SP_PATH).read())
        for node in tree.body:
            if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "BANNED_KEYS" for t in node.targets):
                return tuple(ast.literal_eval(node.value))
    except (OSError, SyntaxError, ValueError):
        pass
    return ()


BANNED_ARGS = set(SF.BANNED_ARGS)
BANNED_KEYS = tuple(sorted(set(SF.BANNED_KEYS) | set(_passage_banned_keys())))

# ------------------------------------------------------------------------------------------------ symbols
y, v, u, th, ph = sp.symbols("y v u theta phi", real=True)
EPS = sp.Symbol("epsilon", real=True)
LAM5 = sp.Symbol("Lambda_5", real=True)
TILT = sp.Symbol("b", real=True)                 # a direction parameter of the partner (never a boost, never a speed)
X5 = [y, v, u, th, ph]
ALPHA, BETA = sp.Function("alpha")(y), sp.Function("beta")(y)
FSH = sp.Function("F")
A_, B_, C_, DD_ = (sp.Function(n)(y, u) for n in ("A", "B", "C", "Dfun"))
NS_FACTOR = 1 + EPS * sp.sin(v)                  # a v-dependence that keeps u = u_H null (multiplies g_vv and g_vu)
# concrete smooth stand-ins, used ONLY to evaluate a numeric witness of a symbolic result (a nonzero witness certifies
# that a mutated expression is truly nonzero; a symbolic zero is also required for the clean checks)
WIT_FUNCS = {ALPHA.func: sp.Lambda(y, 1 + y / 3), BETA.func: sp.Lambda(y, 1 + y / 5),
             A_.func: sp.Lambda((y, u), 1 + y / 3 + u / 5 + y * u / 7),
             B_.func: sp.Lambda((y, u), sp.sqrt(2) * (1 + y / 4 + u / 9)),
             C_.func: sp.Lambda((y, u), 4 + y + u**2 / 3), DD_.func: sp.Lambda((y, u), 1 + y**2 / 5 + u / 11)}
WIT_SHEET = sp.Rational(2, 5) + u / 7 + u**2 / 11
WIT_POINT = {v: sp.Rational(3, 10), EPS: sp.Rational(1, 10), th: sp.Rational(7, 10)}


# ------------------------------------------------------------------------------------------------ geometry engine
def _connection(g, X):
    """Inverse metric and Christoffel symbols G[a][b][c] = Gamma^a_bc of g in coordinates X (no simplification)."""
    n = len(X)
    gi = g.inv().applyfunc(sp.cancel)
    dg = [[[sp.diff(g[a, b], X[c]) for c in range(n)] for b in range(n)] for a in range(n)]
    low = [[[(dg[a][b][c] + dg[a][c][b] - dg[b][c][a]) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    G = [[[sum(gi[a, e] * low[e][b][c] for e in range(n) if gi[a, e] != 0) for c in range(n)] for b in range(n)]
         for a in range(n)]
    return gi, G


def _riemann(G, X):
    """R^a_bcd as a function of the four indices."""
    n = len(X)

    def R(a, b, c, e4):
        return (sp.diff(G[a][b][e4], X[c]) - sp.diff(G[a][b][c], X[e4])
                + sum(G[a][c][e] * G[e][b][e4] - G[a][e4][e] * G[e][b][c] for e in range(n)))
    return R


def _witness(expr, sheet_at=None):
    """A float value of a symbolic expression with the concrete stand-ins substituted (functions, then the point)."""
    ex = sp.sympify(expr)
    for f, lam in WIT_FUNCS.items():
        ex = ex.replace(f, lam)
    if sheet_at is not None:
        ex = ex.replace(FSH, sp.Lambda(u, WIT_SHEET))
    ex = ex.doit().subs(WIT_POINT)
    if sheet_at is not None:
        ex = ex.subs(y, WIT_SHEET.subs(u, sheet_at))
    else:
        ex = ex.subs(y, sp.Rational(2, 7))
    ex = ex.subs(u, 0) if ex.has(u) else ex
    return float(sp.N(ex, 30))


def _zero(expr, wit):
    return expr == 0 and abs(wit) < ZERO_TOL


def _settle(ex, wit):
    """Simplify only when the numeric witness is zero (then a symbolic zero is required); a nonzero witness already
    certifies a nonzero expression, which is returned unsimplified."""
    return sp.simplify(ex) if abs(wit) < ZERO_TOL else ex


# ------------------------------------------------------------------------------------------------ X13 Lemma S
def sheet_gvv(kind="degenerate"):
    """The spec's two sheet-form g_vv: degenerate -alpha^2 u^2/2 (horizon u = 0) and non-degenerate
    -alpha^2 (u^2 - 1/9)/2 (horizon u = 1/3).  Returns (g_vv, u_H)."""
    if kind == "degenerate":
        return -ALPHA**2 * u**2 / 2, sp.Integer(0)
    return -ALPHA**2 * (u**2 - sp.Rational(1, 9)) / 2, sp.Rational(1, 3)


def bulk_gvv(kind="degenerate"):
    """The spec's two bulk-form g_vv: -A(y,u) u^2 (degenerate) and -A(y,u) u (non-degenerate); horizon u = 0."""
    return (-A_ * u**2 if kind == "degenerate" else -A_ * u), sp.Integer(0)


def non_stationary(gvv):
    """The spec's mutation, kept under the spec's name: g_vv + eps y sin v.  What it breaks is NULLNESS, not
    stationarity: g(xi,xi) = eps y sin v on u = u_H, so u = u_H is no longer null at y != 0 (verification F2/PO-1).
    The checks call it "off_null".  A v-dependence that keeps u_H null is nonstationary_null_kept()."""
    return gvv + EPS * y * sp.sin(v)


def nonstationary_null_kept(gvv):
    """A non-stationary member that keeps u = u_H null: g_vv -> g_vv (1 + eps sin v), with g_vu multiplied by the same
    factor.  Returns (g_vv, gvu_factor).  Lemma S's zeros hold on it (computed): stationarity is not their premise."""
    return gvv * NS_FACTOR, NS_FACTOR


def _sheet_metric(gvv, metric, grow=0, gvu_factor=1):
    g = sp.zeros(5)
    if metric == "throat":
        g[0, 0] = 1
        g[1, 2] = g[2, 1] = sp.sqrt(2) * ALPHA**2 * gvu_factor
        g[3, 3] = 4 * BETA**2 * (1 + grow * v)
    else:
        g[0, 0] = DD_
        g[1, 2] = g[2, 1] = B_ * gvu_factor
        g[3, 3] = C_ * (1 + grow * v)
    g[4, 4] = g[3, 3] * sp.sin(th)**2
    g[1, 1] = gvv
    return g


@functools.lru_cache(maxsize=None)
def pairing_sheet(gvv, u_h=0, metric="throat", tilt=0, grow=0, gvu_factor=1):
    """Lemma S, sheet form.  For the sheet y = F(u) + tilt v (F arbitrary; tilt = 0 makes the sheet tangent to
    xi = d_v; tilt != 0 is a mutation) in the metric `metric` ("throat": dy^2 + g_vv dv^2 + 2 sqrt2 alpha(y)^2 dv du +
    4 beta(y)^2 dOmega^2; "general": the bulk form's D dy^2 + g_vv dv^2 + 2B dv du + C dOmega^2), with the angular part
    times (1 + grow v) and g_vu times gvu_factor (scope controls), returns K(xi,xi) = xi^a xi^b nabla_a n_b and
    S(xi,xi)/nu = -[K(xi,xi) - (xi.xi) trK] (one-sided Israel, S_ab = -nu (K_ab - h_ab K); equal to -K(xi,xi) on H,
    deduced) on the horizon u = u_h and on the sheet, with trK = div n (the unit normal field of the foliation
    y - F(u) - tilt v = const), and g(xi,xi) on u = u_h (the premise: it must vanish at every depth)."""
    u_h = sp.sympify(u_h)
    g = _sheet_metric(gvv, metric, grow, gvu_factor)
    gi, G = _connection(g, X5)
    F = FSH(u)
    nl0 = [sp.Integer(1), -sp.sympify(tilt), -sp.diff(F, u), sp.Integer(0), sp.Integer(0)]
    norm = sp.sqrt(sum(gi[a, b] * nl0[a] * nl0[b] for a in range(5) for b in range(5)))
    nl = [c / norm for c in nl0]
    Kxx = sp.diff(nl[1], v) - sum(G[c][1][1] * nl[c] for c in range(5))
    nup = [sum(gi[a, b] * nl[b] for b in range(5)) for a in range(5)]
    sg = sp.sqrt(-g.det())
    trK = sum(sp.diff(sg * nup[a], X5[a]) for a in range(3)) / sg
    Sxx = -(Kxx - g[1, 1] * trK)
    out = {}
    for key, ex in (("K_xixi", Kxx), ("S_xixi_over_nu", Sxx), ("trK", trK)):
        on = ex.subs(u, u_h)
        out[key + "_witness"] = _witness(on, sheet_at=u_h)
        out[key] = _settle(on, out[key + "_witness"]) if key != "trK" else on
    out["trK_finite"] = bool(math.isfinite(out["trK_witness"]) and not out["trK"].has(sp.zoo, sp.nan, sp.oo))
    out["xixi_on_H"] = sp.simplify(g[1, 1].subs(u, u_h))
    return out


@functools.lru_cache(maxsize=None)
def pairing_bulk(gvv, u_h=0, grow=0, grow_y=0, gvu_factor=1, shear=0):
    """Lemma S, bulk form (179/180's corridor exclusive to the bulk).  The family
    D (1 + grow_y v) (1 + shear v)^2 dy^2 + g_vv dv^2 + 2 B gvu_factor dv du + C (1 + grow v)/(1 + shear v) dOmega^2;
    A, B, C, D arbitrary functions of (y, u); no field equation used.  grow (the section grows along v), grow_y (the
    y-extent grows) and shear (shear at fixed volume: theta = 0, sigma != 0) are mutations; gvu_factor with a matching
    g_vv is the null-preserving non-stationary scope control.  Returns, on u = u_h:
      R(xi,xi) (the Riemann route); E~(xi,xi) = R(xi,n,xi,n) with n = d_y/sqrt(g_yy) (normal to the sheets y = const,
      orthogonal to xi); E(xi,xi) = E~(xi,xi) - R(xi,xi)/3 (SMS (A10), first line, contracted with null tangent xi, READ
      PDF p.6); the Ricci scalar (finite?); kappa_5^2 T5(xi,xi) = R(xi,xi) - (R/2 - Lambda_5) g(xi,xi) (Einstein +
      Lambda_5; equal to R(xi,xi) once g(xi,xi)|_H = 0, deduced);
      and the Raychaudhuri route, from the metric of the cross-section (y, theta, phi) of u = u_h alone: the deformation
      B_ij = (1/2) d_v q_ij along xi, theta = tr B, sigma^2 = the square of B's trace-free part over the transverse count
      len(X) - 2 = 3, kappa from nabla_xi xi = kappa xi (Gamma^v_vv), and the residual
      R(xi,xi) + dtheta/dv - kappa theta + theta^2/3 + sigma^2, which must vanish (the non-affine Raychaudhuri equation,
      vorticity zero), so that theta = 0 gives R(xi,xi) = -sigma^2 <= 0."""
    u_h = sp.sympify(u_h)
    g = sp.zeros(5)
    g[0, 0] = DD_ * (1 + grow_y * v) * (1 + shear * v)**2
    g[1, 1] = gvv
    g[1, 2] = g[2, 1] = B_ * gvu_factor
    g[3, 3] = C_ * (1 + grow * v) / (1 + shear * v)
    g[4, 4] = g[3, 3] * sp.sin(th)**2
    gi, G = _connection(g, X5)
    R = _riemann(G, X5)
    Rxx = sum(R(a, 1, a, 1) for a in range(5))
    Ryy = sum(g[1, e] * R(e, 0, 1, 0) for e in range(5)) / g[0, 0]
    gi0 = gi.subs(u, u_h)
    Rs = sum(gi0[b, c] * sum(R(a, b, a, c) for a in range(5)).subs(u, u_h)
             for b in range(5) for c in range(5) if gi0[b, c] != 0)
    out = {}
    Rxx0, Et0 = Rxx.subs(u, u_h), Ryy.subs(u, u_h)
    out["R_xixi_witness"] = _witness(Rxx0)
    out["R_xixi"] = _settle(Rxx0, out["R_xixi_witness"])
    out["Etilde_xixi_witness"] = _witness(Et0)
    out["Etilde_xixi"] = _settle(Et0, out["Etilde_xixi_witness"])
    E0 = Et0 - Rxx0 / 3
    out["E_xixi_witness"] = _witness(E0)
    out["E_xixi"] = _settle(E0, out["E_xixi_witness"])
    out["R_scalar_witness"] = _witness(Rs)
    out["R_scalar_finite"] = bool(math.isfinite(out["R_scalar_witness"]) and not Rs.has(sp.zoo, sp.nan, sp.oo))
    xixi = g[1, 1].subs(u, u_h)
    out["xixi_on_H"] = sp.simplify(xixi)
    T5 = Rxx0 - (Rs / 2 - LAM5) * xixi
    out["kappa2_T5_xixi_witness"] = _witness(T5.subs(LAM5, -6))
    out["kappa2_T5_xixi"] = _settle(T5, out["kappa2_T5_xixi_witness"])
    # the Raychaudhuri route (no Riemann tensor): the cross-section's metric, its deformation along xi, and kappa
    tr_idx = [0, 3, 4]
    q = sp.Matrix(3, 3, lambda i, j: g[tr_idx[i], tr_idx[j]]).subs(u, u_h)
    Bmix = q.inv() * q.diff(v) / 2
    n_s = len(X5) - 2
    theta = sp.simplify(Bmix.trace())
    sig = Bmix - theta * sp.eye(3) / n_s
    sig2 = sp.simplify((sig * sig).trace())
    kap = sp.simplify(G[1][1][1].subs(u, u_h))
    ray = Rxx0 + sp.diff(theta, v) - kap * theta + theta**2 / n_s + sig2
    out["theta"] = theta
    out["sigma2"] = sig2
    out["sigma2_witness"] = _witness(sig2)
    out["kappa"] = kap
    out["raychaudhuri_residual_witness"] = _witness(ray)
    out["raychaudhuri_residual"] = _settle(ray, out["raychaudhuri_residual_witness"])
    out["R_plus_sigma2_witness"] = _witness(Rxx0 + sig2)
    return out


def _eq17_ingoing(data=None, grow=0):
    """Eq. (17) (owner: sim2_facing.B4._eq17, i.e. b4_static's data) in the ingoing chart r = 2 + u^2, v = t + r*(r):
    -F dv^2 + 2 u sqrt(F/H) . 2 dv du + r^2 (1 + grow v) dOmega^2 (4D; grow is the growth mutation)."""
    r = 2 + u**2
    F, H = (data or SF.B4._eq17)(r)
    guv = 2 * sp.sqrt(sp.factor(sp.cancel(u**2 * F / H)))
    X4 = [v, u, th, ph]
    g = sp.zeros(4)
    g[0, 0] = -sp.cancel(F)
    g[0, 1] = g[1, 0] = guv
    g[2, 2] = r**2 * (1 + grow * v)
    g[3, 3] = r**2 * (1 + grow * v) * sp.sin(th)**2
    return g, X4, sp.cancel(F)


@functools.lru_cache(maxsize=None)
def weyl_eq17(u_at=0, grow=0):
    """X13 (c) on eq. (17)'s data [PLANE]: R4(xi,xi) of eq. (17) at u = u_at in the ingoing chart (xi = d_v); u_at = 0
    is the horizon r = 2m.  With SMS's own eq. (17) (the effective equation, READ PDF p.3, which assumes Z2 symmetry,
    eq. (16), and matter confined to the brane, eq. (13); not the board's eq. (17) metric) contracted with null xi
    (Lambda_4 drops): E(xi,xi) = 8 pi G tau(xi,xi) + kappa^4 pi(xi,xi) - R4(xi,xi) at chi -> +-0; the held stress terms
    are horizon_stress_eq17's."""
    u_at = sp.sympify(u_at)
    g, X4, F = _eq17_ingoing(grow=grow)
    gi, G = _connection(g, X4)
    R = _riemann(G, X4)
    Rxx = sum(R(a, 0, a, 0) for a in range(4)).subs(u, u_at)
    val = sp.simplify(Rxx.subs(WIT_POINT))
    return {"R4_xixi": val, "R4_xixi_float": float(sp.N(val, 30)), "g_vu_on_H": sp.simplify(g[0, 1].subs(u, 0)),
            "xixi": sp.simplify(g[0, 0].subs(u, u_at))}


@functools.lru_cache(maxsize=None)
def horizon_stress_eq17(u_at=0, with_readme=False):
    """On eq. (17)'s ingoing chart at u = u_at: a held AdS2-invariant stress tau_ab = -rho g_ab on the (v,u) block and
    p_t g_ab on the sphere (the static stress regular at the horizon: rho + p_r = 0 there), optionally plus the README
    as null dust mu l_a l_b with l = -d_u (future directed, crossing from end 1, u > 0, to end 2, u < 0).  Returns
    tau(xi,xi) and pi(xi,xi) of SMS eq. (20) (READ PDF p.3), and l.xi.  BY CONSTRUCTION the held stress's
    tau(xi,xi) = -rho g(xi,xi) (= rho F in the static frame) and its pi(xi,xi) is proportional to g(xi,xi), which
    vanishes on the horizon: these zeros are deduced from g(xi,xi)|_H = 0 given finite rho, not tests."""
    u_at = sp.sympify(u_at)
    rho, pt, mu = sp.symbols("rho p_t mu", real=True)
    g, X4, F = _eq17_ingoing()
    g = g.subs(u, u_at).subs(WIT_POINT)
    gi = g.inv()
    tau = sp.zeros(4)
    for a in range(2):
        for b in range(2):
            tau[a, b] = -rho * g[a, b]
    for a in (2, 3):
        tau[a, a] = pt * g[a, a]
    lup = sp.Matrix([0, -1, 0, 0])
    llow = g * lup
    if with_readme:
        tau = tau + mu * llow * llow.T
    xi = sp.Matrix([1, 0, 0, 0])
    tmix = gi * tau
    trt = sum(tmix[i, i] for i in range(4))
    tt = sum((tau * gi * tau)[i, j] * gi[i, j] for i in range(4) for j in range(4))
    pi = (-sp.Rational(1, 4) * tau * gi * tau + sp.Rational(1, 12) * trt * tau + sp.Rational(1, 8) * g * tt
          - sp.Rational(1, 24) * g * trt**2)
    return {"tau_xixi": sp.simplify((xi.T * tau * xi)[0]), "pi_xixi": sp.simplify((xi.T * pi * xi)[0]),
            "l_dot_xi": sp.simplify((xi.T * llow)[0]), "l_null": sp.simplify((lup.T * g * lup)[0])}


def readme_flux(mu=1):
    """The README as null dust (H-README-AS-NULL-DUST, the board's): T^R(xi,xi) = mu (l.xi)^2 on eq. (17)'s horizon,
    l = -d_u.  Computed from the chart's metric (l.xi = -g_vu(0) = -sqrt2), so T^R(xi,xi) = 2 mu > 0 for mu > 0.  The
    magnitude 2 is the [PLANE] chart's normalisation of xi and l; only the sign is [FREE]."""
    hs = horizon_stress_eq17(0, True)
    held = horizon_stress_eq17(0, False)
    mu_s = [s for s in hs["tau_xixi"].free_symbols if s.name == "mu"]
    val = sp.simplify(hs["tau_xixi"] - held["tau_xixi"])
    if mu_s:
        val = val.subs(mu_s[0], sp.sympify(mu))
    return val


def pair_crossing(T_readme=None, partner_fraction=1, nu=1, deflect=None, lam_end=1.0):
    """Lemma S's pair on a sheet: the README's member T^R(xi,xi) (readme_flux(1) by default), a partner
    T^c = -partner_fraction T^R, and the net sheet null flux S(xi,xi) = T^R + T^c (the tension and the held stress add
    nothing to S(xi,xi) on the horizon: g(xi,xi) = 0 and horizon_stress_eq17).  net = 0 at partner_fraction = 1 holds
    BY CONSTRUCTION (not a finding).  Lemma K's deflection (deflection_numeric, or `deflect` -- a mutation hook) shows
    what the net does to the horizon generator.  The total is reported as zero or nonzero, never as "positive" (spec
    pitfall 13)."""
    TR = sp.nsimplify(readme_flux(1) if T_readme is None else T_readme)
    Tc = -sp.nsimplify(partner_fraction) * TR
    net = sp.nsimplify(TR + Tc)
    defl = (deflect or deflection_numeric)(float(net), nu=nu, lam_end=lam_end)
    return {"readme_member": TR, "partner_member": Tc, "net": net,
            "net_status": "zero net per light ray (not positive)" if net == 0 else "nonzero net",
            "lemma_s_admits": bool(net == 0), "deflection": defl}


@functools.lru_cache(maxsize=None)
def pair_tensor_eq17(tilt=TILT, held_vtheta=0, partner_norm=0):
    """[PLANE] The full pair tensor on eq. (17)'s ingoing chart at the horizon u = 0: the README mu l (x) l with
    l = -d_u, and a partner -mu' l' (x) l' with l'^u = -1, l'^theta = tilt/r (a direction tilted along the sphere;
    l'.l' = partner_norm, 0 for null dust, -1 a massive-partner mutation), mu' fixed by the pair condition
    T^pair(xi,xi) = 0; plus a held static AdS2-invariant stress (rho, p_t; held_vtheta adds a held momentum flux
    tau_v theta, a non-static mutation).  Returns the pair tensor, T^pair(xi,xi), and pi(xi,xi) by two routes:
    SMS eq. (20) (READ PDF p.3) on the full tensor (held + README + partner), and the null-dust algebra of the pair
    alone, pi(xi,xi) = (1/2) mu mu' (l.xi)(l'.xi)(l.l') (from SMS (20) with g(xi,xi) = 0 = tau(xi,xi) and null l, l';
    it holds whenever the held stress has tau(xi, .) proportional to xi)."""
    rho, pt, mu = sp.symbols("rho p_t mu", real=True)
    g, X4, F = _eq17_ingoing()
    g = g.subs(u, 0).subs(WIT_POINT)
    gi = g.inv()
    r = sp.sqrt(g[2, 2])
    a_ = sp.Symbol("a_l")
    l = sp.Matrix([0, -1, 0, 0])
    lp = sp.Matrix([a_, -1, sp.sympify(tilt) / r, 0])
    lp = lp.subs(a_, sp.solve(sp.Eq((lp.T * g * lp)[0], partner_norm), a_)[0])
    xi = sp.Matrix([1, 0, 0, 0])
    lxi, lpxi = (xi.T * g * l)[0], (xi.T * g * lp)[0]
    mup = sp.simplify(mu * lxi**2 / lpxi**2)
    ll, lpl = g * l, g * lp
    held = sp.zeros(4)
    for i in range(2):
        for j in range(2):
            held[i, j] = -rho * g[i, j]
    for i in (2, 3):
        held[i, i] = pt * g[i, i]
    held[0, 2] = held[2, 0] = held_vtheta
    pair = (mu * ll * ll.T - mup * lpl * lpl.T).applyfunc(sp.simplify)
    T = held + pair
    trt = (gi * T).trace()
    tt = sum((T * gi * T)[i, j] * gi[i, j] for i in range(4) for j in range(4))
    pi = -T * gi * T / 4 + trt * T / 12 + g * tt / 8 - g * trt**2 / 24
    route1 = sp.factor(sp.simplify((xi.T * pi * xi)[0]))
    route2 = sp.factor(sp.simplify(mu * mup * lxi * lpxi * (l.T * g * lp)[0] / 2))
    held_syms = {rho, pt} | (sp.sympify(held_vtheta).free_symbols if held_vtheta != 0 else set())
    return {"pair_xixi": sp.simplify((xi.T * pair * xi)[0]), "pair_tensor": pair,
            "pair_is_zero": bool(pair == sp.zeros(4)), "pi_xixi_sms20": route1, "pi_xixi_nulldust": route2,
            "routes_differ_by": sp.simplify(route1 - route2),
            "held_stress_enters": sorted(str(s) for s in route1.free_symbols & held_syms)}


# ------------------------------------------------------------------------------------------------ C15, C16 identities
@functools.lru_cache(maxsize=None)
def gauss_residual(sign_knkn=1, drop_quadratic=False):
    """C15: contracted Gauss, SMS eq. (3) (READ PDF p.2) contracted with a null k tangent to y = 0:
    R4(k,k) = R5(k,k) - R(k,n,k,n) + K K(k,k) - K(k,.)K(.,k), on dy^2 - A dt^2 + B dr^2 + C dOmega^2 with explicit
    polynomials A, B, C at (t, r, theta) = (1/3, 5/2, 7/10), n = d_y.  sign_knkn = -1 and drop_quadratic are mutations."""
    t, r = sp.symbols("t r", real=True)
    A = 1 + y + 2 * y**2 * t + r * y / 3 + t / 5
    Bf = 2 + r * y - y**2 / 2 + t * y / 7 + r / 4
    C = r**2 * (1 + y / 3 + t * y**2 / 5) + 1
    X = [y, t, r, th, ph]
    g5 = sp.diag(1, -A, Bf, C, C * sp.sin(th)**2)
    _, G5 = _connection(g5, X)
    R5 = _riemann(G5, X)
    h = sp.diag(-A, Bf, C, C * sp.sin(th)**2).subs(y, 0)
    X4 = [t, r, th, ph]
    hi, G4 = _connection(h, X4)
    R4 = _riemann(G4, X4)
    pt = {y: 0, t: sp.Rational(1, 3), r: sp.Rational(5, 2), th: sp.Rational(7, 10), ph: 0}
    kt, kr = 1 / sp.sqrt(A.subs(y, 0)), 1 / sp.sqrt(Bf.subs(y, 0))
    k4, k5 = [kt, kr, 0, 0], [0, kt, kr, 0, 0]
    R4kk = sum(R4(a, b, a, c) * k4[b] * k4[c] for a in range(4) for b in range(2) for c in range(2))
    R5kk = sum(R5(a, b, a, c) * k5[b] * k5[c] for a in range(5) for b in (1, 2) for c in (1, 2))
    Rknkn = sum(g5[0, 0] * R5(0, b, 0, c) * k5[b] * k5[c] for b in (1, 2) for c in (1, 2))
    K = sp.Matrix(4, 4, lambda i, j: sp.diff(sp.diag(-A, Bf, C, C * sp.sin(th)**2)[i, j], y) / 2).subs(y, 0)
    Kmix = hi * K
    trK = sum(Kmix[i, i] for i in range(4))
    Kkk = sum(K[i, j] * k4[i] * k4[j] for i in range(4) for j in range(4))
    KK = sum(K[i, c] * Kmix[c, j] * k4[i] * k4[j] for i in range(4) for j in range(4) for c in range(4))
    quad = 0 if drop_quadratic else (trK * Kkk - KK)
    rhs = R5kk - sign_knkn * Rknkn + quad
    vals = {k_: sp.N(ex.subs(pt), 30) for k_, ex in (("R4_kk", R4kk), ("R5_kk", R5kk), ("R_knkn", Rknkn),
                                                       ("quadratic_K", trK * Kkk - KK))}
    res = sp.N((R4kk - rhs).subs(pt), 30)
    null = sp.simplify(sum(h[i, j] * k4[i] * k4[j] for i in range(4) for j in range(4)))
    return {"residual": float(res), **{k_: float(x) for k_, x in vals.items()}, "k_null": null}


@functools.lru_cache(maxsize=None)
def transport_residual(mode="covariant", nperp=None, sigma="tracefree", rkk_sign=1, iso=False):
    """C16: on -2 du dv + a(v,y)^2 dy^2 + b(v,y)^2 dz1^2 + c(v,y)^2 dz2^2 (iso=True: b = c = a, an isotropic congruence),
    k = d_v (affine), e = d_y/a: R(k,e,k,e) + dB_ee/dlambda + B_ee^2 with B_ij = Gamma^u_ij, the derivative taken
    covariantly along k (mode "covariant": e parallel, so d/dlambda of B(e,e)) or, the mutation, as the coordinate
    derivative of the component B_yy (mode "coordinate"); also e's parallel-transport residual, and Raychaudhuri
    dtheta/dlambda + theta^2/n + sigma^2 + R(k,k) with B^i_j = (1/2) q^ik d_v q_kj on the transverse block, theta = tr B,
    and sigma^2 the square of B's trace-free part over the count n (sigma = "tracefree"; n = len(X) - 2 = 3 from the
    metric when nperp is None).  Mutations: nperp = 2 (a wrong count, used consistently); sigma = "formula" (the old
    sigma^2 := sum x^2 - theta^2/n, which hides a consistent wrong count from the residual -- only the isotropic
    control catches it); rkk_sign = -1."""
    uu, vv, yy, z1, z2 = sp.symbols("u v y z1 z2", real=True)
    a = sp.Function("a")(vv, yy)
    b, c = (a, a) if iso else (sp.Function("b")(vv, yy), sp.Function("c")(vv, yy))
    X = [uu, vv, yy, z1, z2]
    g = sp.zeros(5)
    g[0, 1] = g[1, 0] = -1
    g[2, 2], g[3, 3], g[4, 4] = a**2, b**2, c**2
    _, G = _connection(g, X)
    R = _riemann(G, X)
    R_keke = sp.simplify(sum(g[1, e] * R(e, 2, 1, 2) for e in range(5)) / a**2)     # R_vyvy / a^2 = R(k,e,k,e)
    Byy = G[0][2][2]
    Bee = sp.simplify(Byy / a**2)
    if mode == "covariant":
        dB = sp.diff(Bee, vv)
    else:
        dB = sp.diff(Byy, vv) / a**2
    res_t = sp.simplify(R_keke + dB + Bee**2)
    par = [sp.simplify((sp.diff(1 / a, vv) if i == 2 else 0) + G[i][1][2] / a) for i in range(5)]
    Rkk = sp.simplify(sum(R(e, 1, e, 1) for e in range(5)))
    q = g[2:, 2:]
    Bmix = q.inv() * q.diff(vv) / 2
    n_s = (len(X) - 2) if nperp is None else nperp
    theta = Bmix.trace()
    if sigma == "tracefree":
        s_ = Bmix - theta * sp.eye(3) / n_s
        sig2 = (s_ * s_).trace()
    else:
        sig2 = sum(Bmix[i, i]**2 for i in range(3)) - theta**2 / n_s
    res_r = sp.simplify(sp.diff(theta, vv) + theta**2 / n_s + sig2 + rkk_sign * Rkk)
    return {"transport_residual": res_t, "e_parallel": par, "raychaudhuri_residual": res_r, "R_keke": R_keke,
            "sigma2": sp.simplify(sig2), "n_transverse": n_s,
            "expected_coordinate_leftover": sp.simplify(2 * sp.diff(a, vv)**2 / a**2)}


# ------------------------------------------------------------------------------------------------ X14 Lemma K
@functools.lru_cache(maxsize=None)
def tangent_deflection(Kvv, lapse=1, conn_sign=1):
    """Lemma K's kinematics.  Gaussian normal chart (lapse = 1): lapse^2 dy^2 + h_vv dv^2 + 2 h_vu dv du + h_uu du^2
    + h_ang dOmega^2, h_vv = -u^2/2 + 2 y Kvv + y^2 P(y,u), h_vu = sqrt2 + y Q(y,u), h_uu = y W(y,u),
    h_ang = 4 + y Z(y,u) (P, Q, W, Z arbitrary).  The generator of the brane horizon is y = 0 = u with k = d_v.
    Returns ydd = y'' = -Gamma^y_ab k^a k^b from the connection (conn_sign = -1 flips every Christoffel symbol: a
    mutation), and K_vv = (1/2) Lie_n g_vv = (1/(2 lapse)) d_y g_vv, n = d_y/lapse, computed from the metric with no
    Christoffel symbol (the independent route), their difference, and s_dd = lapse * y'' (the proper normal
    displacement s = lapse y).  In Gaussian normal coordinates y'' = K_vv; in the lapse-2 chart s'' = K_vv while
    y'' = K_vv/2."""
    P, Q, W, Z = (sp.Function(n)(y, u) for n in ("P", "Q", "W", "Z"))
    lap = sp.sympify(lapse)
    g = sp.zeros(5)
    g[0, 0] = lap**2
    g[1, 1] = -u**2 / 2 + 2 * y * Kvv + y**2 * P
    g[1, 2] = g[2, 1] = sp.sqrt(2) + y * Q
    g[2, 2] = y * W
    g[3, 3] = 4 + y * Z
    g[4, 4] = (4 + y * Z) * sp.sin(th)**2
    gi, G = _connection(g, X5)
    at = {y: 0, u: 0}
    ydd = sp.simplify((-conn_sign * G[0][1][1]).subs(at))
    K_vv = sp.simplify((sp.diff(g[1, 1], y) / (2 * lap)).subs(at))
    return {"ydd": ydd, "K_vv": K_vv, "difference": sp.simplify(ydd - K_vv), "s_dd": sp.simplify(lap * ydd),
            "k_null": sp.simplify(g[1, 1].subs(at))}


@functools.lru_cache(maxsize=None)
def _geodesic_rhs(kvv_val):
    """Numeric Christoffels (5D) of the explicit Gaussian normal metric of deflection_numeric, K_vv = kvv_val."""
    K = sp.nsimplify(kvv_val)
    g = sp.zeros(5)
    g[0, 0] = 1
    g[1, 1] = -u**2 / 2 + 2 * y * K + y**2 / 3
    g[1, 2] = g[2, 1] = sp.sqrt(2) * (1 + y / 5)
    g[3, 3] = 4 * (1 + y / 7)**2
    g[4, 4] = 4 * (1 + y / 7)**2 * sp.sin(th)**2
    _, G = _connection(g, X5)
    Gf = sp.lambdify([y, v, u, th, ph], [[[G[a][b][c] for c in range(5)] for b in range(5)] for a in range(5)],
                     "numpy")
    gf = sp.lambdify([y, v, u, th, ph], g, "numpy")
    return Gf, gf


def deflection_numeric(S_vv, nu=1, israel_sign=1, lam_end=1.0):
    """Lemma K, numerically.  Integrates the null geodesic of the explicit Gaussian normal metric
    dy^2 + (-u^2/2 + 2 y K_vv + y^2/3) dv^2 + 2 sqrt2 (1 + y/5) dv du + 4 (1 + y/7)^2 dOmega^2,
    K_vv = -israel_sign S_vv/nu (one-sided Israel, normal into the kept side y >= 0; israel_sign = -1 is the flipped
    mutation), from y = u = 0 with k = d_v (null there: the brane horizon's generator), over affine parameter
    [0, lam_end] (DOP853, rtol 1e-12).  Reports y at the end, min and max of y, whether it stays on the sheet
    (|y| <= 1e-12) and in the kept side (y >= -1e-12), the null-norm drift, and the leading-order y = K_vv lam^2/2.
    For K_vv = 0, y = u = 0 is itself a geodesic of this metric, so "stays" there is immediate."""
    Kvv = -israel_sign * S_vv / nu + 0.0     # + 0.0 turns -0.0 into 0.0
    Gf, gf = _geodesic_rhs(float(Kvv))

    def rhs(_lam, s):
        x, xd = s[:5], s[5:]
        G = np.array(Gf(*x), dtype=float)
        acc = -np.einsum("abc,b,c->a", G, xd, xd)
        return np.concatenate([xd, acc])
    s0 = np.array([0.0, 0.0, 0.0, math.pi / 2, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0])
    sol = solve_ivp(rhs, (0.0, lam_end), s0, method="DOP853", rtol=1e-12, atol=1e-15, dense_output=True)
    lam = np.linspace(0.0, lam_end, 401)
    ys = sol.sol(lam)[0]
    xe = sol.y[:, -1]
    norm_end = float(xe[5:] @ np.array(gf(*xe[:5]), dtype=float) @ xe[5:])
    return {"S_vv": S_vv, "K_vv": Kvv, "lam_end": lam_end, "y_end": float(ys[-1]), "y_min": float(ys.min()),
            "y_max": float(ys.max()), "stays_on_sheet": bool(np.max(np.abs(ys)) <= ZERO_TOL),
            "stays_kept_side": bool(ys.min() >= -ZERO_TOL), "null_norm_end": norm_end,
            "leading_order_y_end": Kvv * lam_end**2 / 2, "ok": bool(sol.success)}


# ------------------------------------------------------------------------------------------------ words and readings
def m_words():
    """M's words used, verbatim from M-RULINGS-2026-10-03.md (typing kept)."""
    src = "M-RULINGS-2026-10-03.md"
    return [
        {"item": "129 (1)", "verbatim": "1 - no. It contains matter, you, me, this current universe, just not a corridor "
         "for transit because the corridor is a bridge, so it adds nothing to either position.", "source": src},
        {"item": "132", "verbatim": "yes. And the passage is one way by nature, a black hole in and a white hole out, "
         "side views of the same corridor object", "source": src + " (excerpt: M's restatement of the board's question "
         "that precedes it is omitted)"},
        {"item": "132", "verbatim": "*different views of the same object", "source": src + " (M's own correction, on "
         "the next line)"},
        {"item": "139 (2)", "verbatim": "2 - positive, and you have to prove it.", "source": src},
        {"item": "162", "verbatim": "Although the chain illustrates a corridor, I submit that it may be more like a "
         "black hole, containing both mouths and throat at once. The throat doesn't change size because the whole chain "
         "object only every takes on the size that contains the README upon opening. It is and always will be only the "
         "size that is needed to hold the object once and at once", "source": src},
        {"item": "172 (1)", "verbatim": "Yes, it may", "source": src + " (M's choice among the board's options)"},
        {"item": "176", "verbatim": "But what if it is in fact entanglement?", "source": src},
        {"item": "177", "verbatim": "Yes, that is the appearance", "source": src + " (M's choice)"},
        {"item": "179", "verbatim": "Let's approach this from a different angle. We know the corridor doesn't not sit on "
         "either position's plane, it only bridges them. So one could surmise that the corridor is exclusive to the "
         "bulk.", "source": src},
        {"item": "180", "verbatim": "Let's approach this from a different angle. We know the corridor *does not sit on "
         "either position's plane, it only bridges them. So one could surmise that the corridor is exclusive to the "
         "bulk.", "source": src},
        {"item": "183", "verbatim": "Yes: never violated as a pair", "source": src + " (M's choice; the option's gloss "
         "\"zero net along each light ray; the negative member is the appearance; E-PASS stays OPEN through 177's "
         "coupling\" is the board's wording)"},
        {"item": "184", "verbatim": "There are no matter free planes", "source": src},
        {"item": "187 (3)", "verbatim": "Seat both", "source": src + " (M's choice: clauses (G) and (Z) of the Warp "
         "Theorem, as the board re-worded them)"},
    ]


def readings():
    """The readings this module's results bear on, with whose they are and their standing after 183, 184 and 187."""
    return [
        {"name": "H-NEC-NEVER-VIOLATED-AS-PAIR", "whose": "carried as M's in the record (183); the gloss is the board's "
         "wording of the option M chose", "content": "117/120's \"never violated\" holds net per light ray: zero net "
         "null energy along each light ray; a negative member paired along the same light rays is the appearance",
         "bearing": "admits Lemma S's exact pair; with theta = 0 it forces sigma = 0 (deduced: R(xi,xi) = -sigma^2 must "
         "vanish); clause (Z) of the Warp Theorem is seated as re-worded (187 (3)); axiom Z3's re-read as net per light "
         "ray is the board's work, listed in 183 as to be worked"},
        {"name": "H-PAIR-CANCELS-ON-THE-HORIZON", "whose": "the board's (offered for 176/178)", "content": "the "
         "README's positive null energy and its partner's equal negative one sum to zero along every crossed generator; "
         "the NEC \"appears broken\" on one member and holds for the pair", "bearing": "under 183 this is the pair M "
         "chose to allow; Lemma S says it is not optional but required at a horizon of fixed size, whether or not the "
         "corridor is stationary"},
        {"name": "H-PARTNER-IS-THE-COUPLING", "whose": "the board's (decided under 149; admitted under 183 per the "
         "record)", "content": "177's appearance covers the exact negative null flux Lemma S requires along the "
         "horizon (the coupled-ends mechanism of Maldacena-Qi and Gao-Jafferis-Wall)", "bearing": "E-PASS's "
         "crossing at fixed size is OPEN through 177, not refuted; the partner's supply is beyond the board's "
         "instruments"},
        {"name": "H-README-AS-NULL-DUST", "whose": "the board's (opening.py)", "content": "the README is null dust "
         "T = mu l (x) l", "bearing": "readme_flux: T^R(xi,xi) = mu (l.xi)^2 > 0"},
        {"name": "H-FIXED-SIZE", "whose": "M's (162)", "content": "the throat never changes size: the object takes the "
         "size that holds the README upon opening and keeps it", "bearing": "read on the crossed horizon through "
         "H-FIXED-SIZE-AS-THETA-ZERO"},
        {"name": "H-FIXED-SIZE-AS-THETA-ZERO", "whose": "the board's (spec 4.3; put to M; no answer in the record)",
         "content": "162's fixed size, read on the horizon the README crosses as zero expansion of its generators "
         "through the crossing", "bearing": "the bulk form's premise: with theta = 0, R(xi,xi) = -sigma^2 <= 0 "
         "(computed), so the pair is demanded (net <= 0 per generator); refused, the horizon grows (the standard "
         "accretion picture, against 162 as worded)"},
        {"name": "H-STATIONARY-CROSSING", "whose": "the board's (spec 4.3)", "content": "the corridor (bulk and "
         "sheets) is stationary while the README crosses (H-QUASI-STATIC-CORRIDOR, the board's; 141; 162)",
         "bearing": "NOT Lemma S's premise (computed: its zeros hold on null-preserving non-stationary horizons); "
         "refused while 162's fixed size is kept, the pair is still demanded (net <= 0 per generator in the bulk, "
         "exactly 0 on a sheet); only expansion (which 162 forbids, read through H-FIXED-SIZE-AS-THETA-ZERO) or a "
         "crease or separation of the bulk horizon at the sheet (Lemma K) releases it"},
        {"name": "H-Z2-PIECES", "whose": "the board's", "content": "the plane's two sides are mirror images (Z2)",
         "bearing": "the [PLANE] hypothesis under which SMS's eq. (17) is used (X13 (c) on eq. (17); the pair tensor's "
         "b = 0)"},
        {"name": "H-CORRIDOR-IN-BULK", "whose": "M's (179/180)", "content": "the corridor sits on neither position's "
         "plane; it only bridges them, and is exclusive to the bulk", "bearing": "Lemma S's bulk form is primary"},
        {"name": "H-NO-MATTER-FREE-PLANES", "whose": "M's (184)", "content": "every plane carries matter",
         "bearing": "Lemma S is law- and tension-independent and holds with matter; matter-free results are limits"},
        {"name": "H-BRIDGE-ADDS-NOTHING", "whose": "M's (129 (1))", "content": "the corridor is a bridge, so it adds "
         "nothing to either position", "bearing": "about the corridor, not the README's crossing; the [PLANE] pair "
         "tensor's zero is noted beside it without being claimed as M's meaning"},
    ]


# ------------------------------------------------------------------------------------------------ the report
def _s(x):
    return str(x) if isinstance(x, sp.Basic) else x


def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(x) for k, x in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(x) for x in o]
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    return _s(o)


def _bulk_variants(kind):
    """The bulk-form variants used by compute() and the checks: name -> pairing_bulk keyword arguments."""
    gb, ub = bulk_gvv(kind)
    gn, fn = nonstationary_null_kept(gb)
    return {"stationary": dict(gvv=gb, u_h=ub), "nonstationary_null_kept": dict(gvv=gn, u_h=ub, gvu_factor=fn),
            "shear_fixed_volume": dict(gvv=gb, u_h=ub, shear=EPS), "section_growth": dict(gvv=gb, u_h=ub, grow=EPS),
            "depth_growth": dict(gvv=gb, u_h=ub, grow_y=EPS), "off_null": dict(gvv=non_stationary(gb), u_h=ub)}


def compute():
    """Every value X13 and X14 need, each row labelled; [FREE]/[PLANE] tags."""
    rows = {}
    sh = {}
    for kind in ("degenerate", "nondegenerate"):
        gvv, uh = sheet_gvv(kind)
        sh["throat_" + kind] = pairing_sheet(gvv, uh, "throat")
        gb, ub = bulk_gvv(kind)
        sh["general_" + kind] = pairing_sheet(gb, ub, "general")
    rows["X13a_sheet"] = {"label": "computed; deduced (S(xi,xi) = -nu K(xi,xi) on H, since g(xi,xi)|_H = 0)",
                          "tag": "[FREE]", "what": "K(xi,xi) and S(xi,xi)/nu on the horizon for sheets y = F(u); no "
                          "field equation, no tension, no law",
                          "cases": {k_: {"K_xixi": o["K_xixi"], "S_xixi_over_nu": o["S_xixi_over_nu"],
                                         "trK_finite": o["trK_finite"], "xixi_on_H": o["xixi_on_H"]}
                                    for k_, o in sh.items()}}
    scope = {}
    for kind in ("degenerate", "nondegenerate"):
        gvv, uh = sheet_gvv(kind)
        gn, fn = nonstationary_null_kept(gvv)
        scope["throat_" + kind + "_nonstationary_null_kept"] = pairing_sheet(gn, uh, "throat", 0, 0, fn)["K_xixi"]
        scope["throat_" + kind + "_section_growth"] = pairing_sheet(gvv, uh, "throat", 0, EPS)["K_xixi"]
        scope["throat_" + kind + "_tilted_sheet"] = pairing_sheet(gvv, uh, "throat", EPS)["K_xixi_witness"]
    rows["X13a_scope"] = {"label": "computed", "tag": "[FREE]", "K_xixi": scope,
                          "statement": "the sheet zero also holds on a non-stationary horizon that keeps u_H null and on "
                          "a horizon whose section grows (C -> C (1 + eps v)): stationarity and fixed size are not its "
                          "premise.  A sheet tilted off xi (y = F(u) + eps v) gives K(xi,xi) = -kappa n.xi: nonzero in "
                          "the non-degenerate case, 0 in the degenerate case where kappa = 0 (witnesses)"}
    rows["X13a_statement"] = {"label": "deduced", "tag": "[FREE]", "statement": "Wherever the bulk null surface "
                              "reaches the sheet along xi (the brane horizon's generators are generators of a bulk null "
                              "hypersurface C^2 up to the sheet: Lemma K's C^2 case), the net surface null flux across "
                              "the horizon vanishes on that sheet -- kappa = 0 and kappa != 0, any tension or law, with "
                              "matter (law-independent; 184 makes the matter case the one that matters), whether or not "
                              "the horizon grows: T^c(xi,xi) = -T^R(xi,xi) on the README's own sheet, generator by "
                              "generator.  Computed for sheets y = F(u); deduced for any sheet tangent to xi.  Applies "
                              "to whichever sheet the README is on (172 (1))."}
    held = horizon_stress_eq17(0, False)
    off = horizon_stress_eq17(sp.Rational(1, 2), False)
    rows["X13a_held_stress"] = {"label": "computed; deduced (cannot be the partner)",
                                "tag": "[PLANE] chart; [FREE] by the deduction g(xi,xi) = 0",
                                "tau_xixi_on_H": held["tau_xixi"], "pi_xixi_on_H": held["pi_xixi"],
                                "tau_xixi_at_u_half": off["tau_xixi"], "statement": "a held AdS2-invariant stress has "
                                "tau(xi,xi) = -rho g(xi,xi) and pi(xi,xi) proportional to g(xi,xi) by construction, so "
                                "both vanish on the horizon for finite rho in the static frame (regularity; a static "
                                "stress with rho ~ 1/F, singular on the future horizon, could keep a finite T(xi,xi)): a "
                                "regular held stress cannot be the partner; the partner must be a genuine negative null "
                                "flux"}
    wr = horizon_stress_eq17(0, True)
    rows["X13a_readme_flux"] = {"label": "computed", "tag": "[PLANE] chart (sign [FREE]: (l.xi)^2 > 0 for any "
                                "transverse null l)", "T_R_xixi_per_mu": readme_flux(1), "l_dot_xi": wr["l_dot_xi"],
                                "l_null": wr["l_null"], "pi_xixi_with_readme": wr["pi_xixi"],
                                "reading": "H-README-AS-NULL-DUST (the board's)"}
    bk = {kind: {name: pairing_bulk(**kw) for name, kw in _bulk_variants(kind).items()}
          for kind in ("degenerate", "nondegenerate")}
    rows["X13b_bulk"] = {"label": "computed (identity); deduced (the T5 line, with Einstein + Lambda_5)",
                         "tag": "[FREE]; the primary statement under 179/180",
                         "cases": {k_: {"R_xixi": o["stationary"]["R_xixi"],
                                        "kappa2_T5_xixi": o["stationary"]["kappa2_T5_xixi"],
                                        "R_scalar_finite": o["stationary"]["R_scalar_finite"],
                                        "xixi_on_H": o["stationary"]["xixi_on_H"],
                                        "R_xixi_nonstationary_null_kept": o["nonstationary_null_kept"]["R_xixi"]}
                                   for k_, o in bk.items()},
                         "statement": "for the family named (D dy^2 + g_vv dv^2 + 2B dv du + C dOmega^2, A, B, C, D "
                         "arbitrary of (y, u); no g_uu, no cross terms, no rotation): R(xi,xi) = 0 on its horizon with "
                         "no field equation, on the stationary members and on the null-preserving non-stationary one; "
                         "with Einstein + Lambda_5 and g(xi,xi)|_H = 0, kappa_5^2 T5(xi,xi) = R(xi,xi) = 0 (deduced): "
                         "the README's 5D null flux must be cancelled by an equal negative null flux along the same "
                         "generators"}
    rows["X13b_premise"] = {"label": "computed; deduced (the net flux bound, with Einstein + Lambda_5)", "tag": "[FREE]",
                            "cases": {k_: {nm: {"theta": o[nm]["theta"], "sigma2_witness": o[nm]["sigma2_witness"],
                                                "R_xixi_witness": o[nm]["R_xixi_witness"],
                                                "raychaudhuri_residual": o[nm]["raychaudhuri_residual"]}
                                           for nm in ("stationary", "nonstationary_null_kept", "shear_fixed_volume",
                                                      "section_growth", "depth_growth")}
                                      for k_, o in bk.items()},
                            "statement": "the Raychaudhuri route (from the cross-section's metric, no Riemann tensor) "
                            "agrees with the Riemann route on every variant: R(xi,xi) = -dtheta/dv + kappa theta - "
                            "theta^2/3 - sigma^2.  So the bulk form's premise is a non-expanding horizon: with theta = 0, "
                            "R(xi,xi) = -sigma^2 <= 0 (shear at fixed volume: -0.014138938637006316 at eps = 1/10, "
                            "v = 3/10), = 0 iff shear-free.  Across a horizon that keeps its size the net 5D null flux "
                            "per generator is -sigma^2/kappa_5^2 <= 0: the partner must be at least as large as the "
                            "README's flux, exactly as large iff shear-free (deduced; 162 read through "
                            "H-FIXED-SIZE-AS-THETA-ZERO, the board's, put to M).  With H-NEC-NEVER-VIOLATED-AS-PAIR "
                            "(183, M's) sigma = 0 and the pair is exact (deduced)"}
    rows["X13b_label_note"] = {"label": "standard-not-READ", "statement": "R(xi,xi) = 0 on any Killing horizon is a "
                               "standard result; here it is computed for the family named, not READ"}
    w17 = weyl_eq17(0)
    rows["X13c_weyl"] = {"label": "computed; READ (SMS gr-qc/9910076v3 eq. (A10), first line, PDF p.6); deduced",
                         "tag": "[FREE]",
                         "cases": {k_: {nm: {"Etilde_xixi": o[nm]["Etilde_xixi"], "E_xixi": o[nm]["E_xixi"]}
                                        for nm in ("stationary", "nonstationary_null_kept")} for k_, o in bk.items()},
                         "section_growth_E_xixi_witness": {k_: o["section_growth"]["E_xixi_witness"]
                                                           for k_, o in bk.items()},
                         "statement": "E~(xi,xi) = R(xi,n,xi,n) = 0 and E(xi,xi) = E~(xi,xi) - R(xi,xi)/3 = 0 on the "
                         "family's horizon (stationary or null-preserving non-stationary): the bulk's Weyl term "
                         "supplies nothing along the generators; a bulk field cannot change a sheet's surface flux.  A "
                         "growing section gives E~ = 0 but E != 0"}
    rows["X13c_eq17"] = {"label": "computed; READ (SMS eq. (17), PDF p.3, which assumes Z2 symmetry, eq. (16), and "
                         "matter confined to the brane, eq. (13)); deduced",
                         "tag": "[PLANE]", "R4_xixi_on_H": w17["R4_xixi"], "g_vu_on_H": w17["g_vu_on_H"],
                         "R4_xixi_at_u_half": weyl_eq17(sp.Rational(1, 2))["R4_xixi_float"],
                         "statement": "the board's eq. (17) metric (owner B4._eq17): R4(xi,xi) = 0 at r = 2m (computed); "
                         "with SMS's own eq. (17) and the held stress's tau(xi,xi) = pi(xi,xi) = 0, E(xi,xi) = 0 at "
                         "chi -> +-0 there (deduced; H-Z2-PIECES, the board's, is the hypothesis).  The matter-free "
                         "plane is a limit only (184); with held matter the same zero holds"}
    pc = pair_crossing()
    rows["X13d_pair"] = {"label": "computed (the ledger); deduced (Lemma S)",
                         "tag": "[PLANE] chart normalisation (l.xi = -sqrt2); the cancellation [FREE]",
                         "readme_member": pc["readme_member"], "partner_member": pc["partner_member"],
                         "net": pc["net"], "net_status": pc["net_status"],
                         "stays_on_sheet": pc["deflection"]["stays_on_sheet"],
                         "note": "net = 0 by construction (the partner is defined as -T^R); not a finding; the content "
                         "is C19b's mutations.  stays_on_sheet is immediate: y = u = 0 is a geodesic of "
                         "deflection_numeric's metric when K_vv = 0"}
    pt_b = pair_tensor_eq17(TILT)
    rows["X13d_pair_tensor"] = {"label": "computed; deduced (with SMS (17) under Z2, H-Z2-PIECES, and a static held "
                                "stress)", "tag": "[PLANE]",
                                "pair_xixi": pt_b["pair_xixi"], "pair_is_zero_at_b": pt_b["pair_is_zero"],
                                "pair_is_zero_at_b0": pair_tensor_eq17(0)["pair_is_zero"],
                                "pi_xixi_sms20": pt_b["pi_xixi_sms20"], "pi_xixi_nulldust": pt_b["pi_xixi_nulldust"],
                                "held_stress_enters": pt_b["held_stress_enters"],
                                "statement": "for a null-dust partner tilted by b along the sphere, the pair tensor is "
                                "nonzero for b != 0 and pi(xi,xi) of held stress + README + partner is -b^2 mu^2/2 by two "
                                "routes, independent of the static held stress (computed).  With R4(xi,xi) = 0 (C18c), "
                                "E(xi,xi) = 0 from the bulk side (C18b; the bulk near the plane taken in the family of "
                                "(b), non-expanding and shear-free) and tau(xi,xi) = 0 (the pair), SMS (17) gives "
                                "pi(xi,xi) = 0, so b = 0: among null-dust partners only the README's exact reverse is "
                                "admitted, and the pair's total stress tensor is then zero -- the README's stress is "
                                "cancelled outright (deduced; a held momentum flux tau_v theta = j along the sphere would "
                                "enter and could cancel pi(xi,xi) at b = -sqrt2 j/(4 mu), C19c's mutation).  A paired "
                                "crossing leaves S(xi,xi) unchanged by construction; the other components are those "
                                "computed here, for null-dust partners only"}
    rows["X13d_readings"] = {"label": "OPEN", "statement": "H-PAIR-CANCELS-ON-THE-HORIZON and H-PARTNER-IS-THE-COUPLING "
                             "(the board's), re-read under 183: the exact +/- null pair is admitted under 177; E-PASS's "
                             "crossing at fixed size is OPEN (supply beyond the board's instruments), NOT refuted.  The "
                             "board notes, without claiming it as M's meaning, that the [PLANE] pair's zero total stress "
                             "tensor is the shape of 129 (1)'s words (carried as H-BRIDGE-ADDS-NOTHING, about the "
                             "corridor, not the README's crossing).", "readings": readings()}
    rows["X13_limit"] = {"label": "deduced", "statement": "premises as computed (replacing pitfall 3's 'Lemma S needs "
                         "stationarity'): bulk form, a non-expanding horizon (theta = 0), with R(xi,xi) = -sigma^2 <= 0; "
                         "sheet form, u = u_H null at every depth and the sheet tangent to xi, through growth.  Refusing "
                         "stationarity while 162's fixed size is kept still demands the pair.  A net-flux crossing "
                         "(E-NS) needs expansion (bulk; 162 forbids it as read through H-FIXED-SIZE-AS-THETA-ZERO) or a "
                         "crease or separation of the bulk horizon at the sheet (Lemma K).  The pair must be exact to "
                         "the order at which theta and sigma are held at zero.  Statements about the families computed; "
                         "deduced beyond them"}
    td = tangent_deflection(sp.Symbol("K_vv"))
    tdl = tangent_deflection(sp.Symbol("K_vv"), 2)
    rows["X14_tangent"] = {"label": "computed (the Gaussian normal identity Gamma^y_vv = -K_vv; standard)",
                           "tag": "[FREE for sheets]", "ydd_connection": td["ydd"], "K_vv_lie": td["K_vv"],
                           "difference": td["difference"], "lapse2_ydd": tdl["ydd"], "lapse2_K_vv_lie": tdl["K_vv"],
                           "lapse2_s_dd": tdl["s_dd"],
                           "statement": "y'' from the connection equals K_vv = (1/2) Lie_n g_vv computed with no "
                           "Christoffel symbol; in the lapse-2 chart the proper normal displacement s = 2y obeys "
                           "s'' = K_vv, while y'' = K_vv/2 (the symbol K_vv here is the coefficient in h_vv = 2 y K_vv)",
                           "israel": "K_vv = -S_vv/nu (one-sided, normal into the kept side)",
                           "owner_lemma_n_connection": bool(SF.lemma_n()["connection"])}
    rows["X14_numeric"] = {"label": "computed", "tag": "[FREE for sheets]",
                           "cases": {name: deflection_numeric(s) for name, s in
                                     (("S_vv=0", 0.0), ("S_vv=+1", 1.0), ("S_vv=-1", -1.0), ("S_vv=1e-6", 1e-6))}}
    rows["X14_consequence"] = {"label": "deduced", "tag": "[FREE for sheets]", "statement": "the null normal of a C^1 "
                               "null hypersurface through the brane horizon is k, and a C^2 null hypersurface has "
                               "geodesic generators; so a bulk horizon C^2 up to the sheet, with that trace, has "
                               "S(k,k) = 0 there.  A net-flux crossing is a five-dimensional event (E-NS): S(k,k) > 0 "
                               "creases the bulk horizon at the sheet, S(k,k) < 0 separates it from the brane horizon."}
    rows["X14_withdrawn"] = {"label": "deduced", "statement": "WITHDRAWN: the smooth-horizon identity's B_start budget "
                             "and design 4's O-C \"a sheet with q >= 0 absorbs classically\"; the identity's algebra is "
                             "kept only as C15 and C16"}
    rows["C15_gauss"] = {"label": "computed; READ (SMS eq. (3), PDF p.2)", **gauss_residual(1),
                         "mutant_sign_flipped": gauss_residual(-1)["residual"]}
    tr = transport_residual("covariant")
    rows["C16_transport"] = {"label": "computed", "transport_residual": tr["transport_residual"],
                             "raychaudhuri_residual": tr["raychaudhuri_residual"], "R_keke": tr["R_keke"],
                             "n_transverse": tr["n_transverse"],
                             "isotropic_sigma2": transport_residual("covariant", iso=True)["sigma2"],
                             "mutant_coordinate_leftover": transport_residual("coordinate")["transport_residual"]}
    rows["E_PASS_status"] = {"label": "OPEN", "statement": "E-PASS (the crossing at fixed size) is OPEN through 177 under "
                             "183 (H-PARTNER-IS-THE-COUPLING admitted); not refuted.  A net-flux crossing (E-NS) needs "
                             "expansion or a crease or separation of the bulk horizon at the sheet."}
    rows["cross_check"] = {"label": "computed (Wolfram 15.0.1 through the connector, by the fix session; not run by "
                           "this module; inputs kept in WOLFRAM_CROSSCHECK and WOLFRAM_CROSSCHECK_PAIR)",
                           "result": WOLFRAM_CROSSCHECK_RESULT}
    return _clean({"module": "epass_pairing", "status": "computed, READ and deduced; not verified; not seated; "
                   "2026-10-09", "m_words": m_words(), "results": rows})


# ------------------------------------------------------------------------------------------------ Wolfram cross-check
WOLFRAM_CROSSCHECK = r"""
coords = {y, v, u, th, ph};
A[y_, u_] := 1 + y/3 + u/5 + y u/7; B[y_, u_] := Sqrt[2] (1 + y/4 + u/9);
Cc[y_, u_] := 4 + y + u^2/3; Dd[y_, u_] := 1 + y^2/5 + u/11;
met[gvv_, f_, gr_, gy_, sh_] := Module[{g = ConstantArray[0, {5, 5}]},
  g[[1, 1]] = Dd[y, u] (1 + gy v) (1 + sh v)^2; g[[2, 2]] = gvv; g[[2, 3]] = g[[3, 2]] = B[y, u] f;
  g[[4, 4]] = Cc[y, u] (1 + gr v)/(1 + sh v); g[[5, 5]] = g[[4, 4]] Sin[th]^2; g];
rxx[g_] := Module[{gi = Inverse[g], G},
  G = Table[Sum[gi[[a, e]] (D[g[[e, b]], coords[[c]]] + D[g[[e, c]], coords[[b]]] - D[g[[b, c]], coords[[e]]])/2,
     {e, 5}], {a, 5}, {b, 5}, {c, 5}];
  Sum[D[G[[a, 2, 2]], coords[[a]]] - D[G[[a, 2, a]], coords[[2]]] +
     Sum[G[[a, a, e]] G[[e, 2, 2]] - G[[a, 2, e]] G[[e, 2, a]], {e, 5}], {a, 5}]];
sig2[g_] := Module[{q = g[[{1, 4, 5}, {1, 4, 5}]] /. u -> 0, bm, th0},
  bm = Inverse[q].D[q, v]/2; th0 = Tr[bm]; Tr[(bm - th0 IdentityMatrix[3]/3).(bm - th0 IdentityMatrix[3]/3)]];
pt = {y -> 2/7, v -> 3/10, th -> 7/10, eps -> 1/10};
cases = {{"deg stationary", -A[y, u] u^2, 1, 0, 0, 0}, {"deg null-kept", -A[y, u] u^2 (1 + eps Sin[v]), 1 + eps Sin[v], 0, 0, 0},
  {"deg shear", -A[y, u] u^2, 1, 0, 0, eps}, {"deg growth", -A[y, u] u^2, 1, eps, 0, 0},
  {"nondeg null-kept", -A[y, u] u (1 + eps Sin[v]), 1 + eps Sin[v], 0, 0, 0}, {"nondeg shear", -A[y, u] u, 1, 0, 0, eps},
  {"nondeg growth", -A[y, u] u, 1, eps, 0, 0}};
Table[With[{g = met[c[[2]], c[[3]], c[[4]], c[[5]], c[[6]]]},
  {c[[1]], N[(rxx[g] /. u -> 0) /. pt, 20], N[sig2[g] /. pt, 20]}], {c, cases}]
"""
WOLFRAM_CROSSCHECK_PAIR = r"""
g = {{0, Sqrt[2], 0, 0}, {Sqrt[2], 0, 0, 0}, {0, 0, 4, 0}, {0, 0, 0, 4 Sin[7/10]^2}}; gi = Inverse[g];
l = {0, -1, 0, 0}; lp0 = {aa, -1, bb/2, 0}; sol = Solve[lp0.g.lp0 == 0, aa][[1]]; lp = lp0 /. sol;
xi = {1, 0, 0, 0}; mup = mu (xi.g.l)^2/(xi.g.lp)^2;
held = {{-rho g[[1, 1]], -rho g[[1, 2]], 0, 0}, {-rho g[[2, 1]], -rho g[[2, 2]], 0, 0}, {0, 0, pt g[[3, 3]], 0},
  {0, 0, 0, pt g[[4, 4]]}};
T = held + mu Outer[Times, g.l, g.l] - mup Outer[Times, g.lp, g.lp];
trt = Tr[gi.T]; tt = Tr[T.gi.T.gi];
pi = -T.gi.T/4 + trt T/12 + g tt/8 - g trt^2/24;
{Simplify[xi.pi.xi], Simplify[xi.T.xi], Simplify[mu Outer[Times, g.l, g.l] - mup Outer[Times, g.lp, g.lp] /. bb -> 0]}
"""
WOLFRAM_CROSSCHECK_RESULT = (
    "Wolfram 15.0.1 (connector, 2026-10-09), R(xi,xi)|_{u=0} and sigma^2 at y = 2/7, v = 3/10, theta = 7/10, "
    "eps = 1/10 on the WIT_FUNCS stand-ins, 20 digits: degenerate stationary 0, 0; degenerate null-kept 0, 0; "
    "degenerate shear -0.014138938637006315393, 0.014138938637006315393; degenerate growth 0.0047129795456687717975, "
    "0.0015709931818895905992; non-degenerate null-kept 0 (to 70 digits), 0; non-degenerate shear "
    "-0.014138938637006315393, 0.014138938637006315393; non-degenerate growth 0.039801341934645240107, "
    "0.0015709931818895905992.  All agree with this module's sympy witnesses to every printed digit.  The earlier "
    "builder session's cross-check (C15's R(k,n,k,n) = 0.3124288156984969, residual 0, sign-flipped "
    "-0.6248576313969938, quadratic-dropped -0.1075040888002711; the off-null witnesses) had no input in the tree "
    "and is superseded by this one for the bulk values; C15 was not re-run in Wolfram.  WOLFRAM_CROSSCHECK_PAIR "
    "(eq. (17)'s "
    "horizon metric at u = 0, g_vu = sqrt2, written out by hand; SMS eq. (20) on held + README + tilted partner) gives "
    "pi(xi,xi) = -bb^2 mu^2/2 with rho and p_t absent, T(xi,xi) = 0, and the pair tensor zero at bb = 0, agreeing with "
    "pair_tensor_eq17.")


# ------------------------------------------------------------------------------------------------ guard
def _keys(o, acc):
    if isinstance(o, dict):
        for k_, x in o.items():
            acc.add(str(k_))
            _keys(x, acc)
    elif isinstance(o, (list, tuple)):
        for x in o:
            _keys(x, acc)
    return acc


def _label_ok(lab):
    parts, depth, cur = [], 0, ""
    for ch in str(lab):                     # split on ';' outside parentheses only
        depth += (ch == "(") - (ch == ")")
        if ch == ";" and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    parts.append(cur.strip())
    return all(any(p == L or p.startswith(L + " ") for L in LABELS) for p in parts)


_TOTAL_WORDS = r"(?:pair|pairs|net|total|totals|sum|sums|summed)"
_POS = re.compile(r"\bpositive\b", re.I)


def _positive_total(text):
    """Does a sentence call a pair total, a net or a sum 'positive'?  A 'positive' within 40 characters after one of
    pair/net/total/sum, or within 12 characters before total/net/sum, in the same clause; 'not positive', 'never ...
    positive' and 'non-positive' are not callings."""
    hits = []
    for clause in re.split(r"[.;:()\[\]]", str(text)):
        for m in _POS.finditer(clause):
            before, after = clause[:m.start()], clause[m.end():]
            if re.search(r"(\bnot\s+|\bnever\b[^,]*|\bnon-)[\"']?$", before, re.I):
                continue
            if re.search(r"\b" + _TOTAL_WORDS + r"\b[^,]{0,40}$", before, re.I) or \
                    re.match(r"^[^,]{0,12}\b(?:total|net|sum)\b", after, re.I):
                hits.append(clause.strip())
    return hits


def _zero_called_positive(o, acc, path=""):
    """Pitfall 13: (i) in any dict carrying a numeric zero 'net', a string value calling it positive; (ii) anywhere in
    the report, a string that calls a pair total, a net or a sum 'positive' (_positive_total)."""
    if isinstance(o, dict):
        net = o.get("net")
        try:
            is_zero = net is not None and float(sp.sympify(net)) == 0.0
        except (TypeError, ValueError, sp.SympifyError):
            is_zero = False
        if is_zero:
            for k_, x in o.items():
                if isinstance(x, str) and "positive" in x.lower() and "not positive" not in x.lower():
                    acc.append(k_)
        for k_, x in o.items():
            _zero_called_positive(x, acc, path + "/" + str(k_))
    elif isinstance(o, (list, tuple)):
        for i, x in enumerate(o):
            _zero_called_positive(x, acc, path + f"[{i}]")
    elif isinstance(o, str) and _positive_total(o):
        acc.append(path)
    return acc


def address_guard(out, extra_funcs=(), extra_keys=None):
    """Keys of `out` against BANNED_KEYS (sim2_facing's and sim2_passage's); this module's function signatures (and
    extra_funcs) against sim2_facing.BANNED_ARGS (names only, labelled as such); every result row's label among the six;
    no pair total, net or sum described as positive anywhere in the report (pitfall 13).  The module's functions are
    enumerated from its globals, so the guard works however the module was imported by path."""
    funcs = []
    for f in list(globals().values()):
        f = getattr(f, "__wrapped__", f)          # lru_cache-wrapped functions are checked through their wrapped body
        if inspect.isfunction(f) and f.__module__ == __name__:
            funcs.append(f)
    funcs += list(extra_funcs)
    bad_args = sorted({(f.__name__, p) for f in funcs for p in inspect.signature(f).parameters if p in BANNED_ARGS})
    keys = _keys(out, set())
    if extra_keys:
        keys |= _keys(extra_keys, set())
    bad_keys = sorted(k_ for k_ in keys if any(b in k_.lower() for b in BANNED_KEYS))
    rows = out.get("results", {}) if isinstance(out, dict) else {}
    bad_labels = sorted(k_ for k_, r in rows.items() if not _label_ok(r.get("label", "")))
    zero_pos = _zero_called_positive(out, [])
    return {"n_funcs": len(funcs), "bad_args": bad_args, "bad_keys": bad_keys, "bad_labels": bad_labels,
            "zero_called_positive": zero_pos, "n_keys": len(keys), "banned_keys_used": list(BANNED_KEYS),
            "check": "names only"}


# ------------------------------------------------------------------------------------------------ checks
def check_C15(mut=None):
    """Contracted Gauss residual 0 at the point."""
    o = gauss_residual(-1 if mut == "sign" else 1, mut == "drop_quadratic")
    return abs(o["residual"]) < ZERO_TOL and o["k_null"] == 0, {"residual": o["residual"], "R_knkn": o["R_knkn"]}


def check_C16(mut=None):
    """Transport (covariant, e parallel) and Raychaudhuri residuals 0, with sigma^2 the trace-free square over the
    metric's transverse count; the isotropic control (a = b = c) must give sigma^2 = 0 and a zero residual."""
    kw = {"mode": "coordinate" if mut == "coordinate" else "covariant",
          "nperp": 2 if mut in ("nperp2", "formula_count2") else None,
          "sigma": "formula" if mut == "formula_count2" else "tracefree",
          "rkk_sign": -1 if mut == "rkk_sign" else 1}
    o = transport_residual(**kw)
    iso = transport_residual(**kw, iso=True)
    ok = (o["transport_residual"] == 0 and all(p == 0 for p in o["e_parallel"]) and o["raychaudhuri_residual"] == 0
          and iso["sigma2"] == 0 and iso["raychaudhuri_residual"] == 0)
    det = {"transport_residual": str(o["transport_residual"]), "raychaudhuri_residual": str(o["raychaudhuri_residual"]),
           "isotropic_sigma2": str(iso["sigma2"]), "n_transverse": o["n_transverse"]}
    if mut == "coordinate":
        det["leftover_is_2av2_over_a2"] = bool(sp.simplify(o["transport_residual"] - o["expected_coordinate_leftover"])
                                              == 0)
    return ok, det


def check_C17(mut=None):
    """Lemma S, sheet form: K(xi,xi)|_H = 0 (symbolic zero and numeric witness) for sheets y = F(u), degenerate and
    non-degenerate, throat and general metrics, trK finite; and, as scope controls that must also give 0, the same
    sheets on a non-stationary horizon that keeps u_H null and on a horizon whose section grows (the sheet form does not
    rest on stationarity or fixed size).  S(xi,xi)/nu = -K(xi,xi) on H is deduced and reported, not tested."""
    ok, det = True, {}
    for metric in ("throat", "general"):
        for kind in ("degenerate", "nondegenerate"):
            gvv, uh = sheet_gvv(kind) if metric == "throat" else bulk_gvv(kind)
            gn, fn = nonstationary_null_kept(gvv)
            if mut == "off_null":
                runs = {"main": pairing_sheet(non_stationary(gvv), uh, metric)}
            elif mut == "tilt":
                runs = {"main": pairing_sheet(gvv, uh, metric, EPS)}
            else:
                runs = {"main": pairing_sheet(gvv, uh, metric),
                        "nonstationary_null_kept": pairing_sheet(gn, uh, metric, 0, 0, fn),
                        "section_growth": pairing_sheet(gvv, uh, metric, 0, EPS)}
            for nm, o in runs.items():
                c = _zero(o["K_xixi"], o["K_xixi_witness"]) and o["trK_finite"]
                ok = ok and c
            det[metric + "_" + kind] = {nm: {"K_xixi_witness": o["K_xixi_witness"],
                                             "S_xixi_over_nu_witness": o["S_xixi_over_nu_witness"]}
                                        for nm, o in runs.items()}
    return ok, det


def check_C18(mut=None):
    """Lemma S, bulk form: R(xi,xi)|_{u=0} = 0 (symbolic zero and witness; R finite), both g_vv forms, on the
    stationary family and, as a scope control, on the null-preserving non-stationary member.  kappa^2 T5(xi,xi) equals
    R(xi,xi) there (g(xi,xi)|_H = 0) and is reported, not tested."""
    ok, det = True, {}
    for kind in ("degenerate", "nondegenerate"):
        V = _bulk_variants(kind)
        names = {"off_null": ["off_null"], "growth": ["section_growth"], "depth_growth": ["depth_growth"],
                 "shear": ["shear_fixed_volume"]}.get(mut, ["stationary", "nonstationary_null_kept"])
        det[kind] = {}
        for nm in names:
            o = pairing_bulk(**V[nm])
            c = _zero(o["R_xixi"], o["R_xixi_witness"]) and o["R_scalar_finite"]
            ok = ok and c
            det[kind][nm] = {"R_xixi_witness": o["R_xixi_witness"], "kappa2_T5_xixi_witness": o["kappa2_T5_xixi_witness"],
                             "xixi_on_H": str(o["xixi_on_H"])}
    return ok, det


def check_C18s(mut=None):
    """The bulk form's premise: the Raychaudhuri route (cross-section metric, no Riemann tensor) agrees with the
    Riemann route on every null-preserving variant (residual 0), and on a horizon sheared at fixed volume theta = 0
    identically while R(xi,xi) = -sigma^2 < 0 (a fixed-size horizon demands net <= 0 per generator)."""
    ok, det = True, {}
    for kind in ("degenerate", "nondegenerate"):
        V = _bulk_variants(kind)
        for nm in ("stationary", "nonstationary_null_kept", "section_growth", "depth_growth", "shear_fixed_volume"):
            o = pairing_bulk(**V[nm])
            ok = ok and _zero(o["raychaudhuri_residual"], o["raychaudhuri_residual_witness"])
        sh = dict(V["shear_fixed_volume"])
        if mut == "no_shear":
            sh["shear"] = 0
        elif mut == "growth":
            sh = dict(V["section_growth"])
        o = pairing_bulk(**sh)
        c = (o["theta"] == 0 and abs(o["R_plus_sigma2_witness"]) < ZERO_TOL and o["R_xixi_witness"] < -1e-6)
        ok = ok and c
        det[kind] = {"theta": str(o["theta"]), "sigma2_witness": o["sigma2_witness"],
                     "R_xixi_witness": o["R_xixi_witness"], "R_plus_sigma2_witness": o["R_plus_sigma2_witness"]}
    return ok, det


def check_C18b(mut=None):
    """X13 (c), bulk: E~(xi,xi) = R(xi,n,xi,n) = 0 and E(xi,xi) = 0 on the horizon, both g_vv forms, stationary and (scope
    control) null-preserving non-stationary.  E = E~ - R(xi,xi)/3 carries content where R(xi,xi) != 0: the growth
    mutation leaves E~ = 0 and is caught through E."""
    ok, det = True, {}
    for kind in ("degenerate", "nondegenerate"):
        V = _bulk_variants(kind)
        names = {"off_null": ["off_null"], "depth_growth": ["depth_growth"],
                 "growth": ["section_growth"]}.get(mut, ["stationary", "nonstationary_null_kept"])
        det[kind] = {}
        for nm in names:
            o = pairing_bulk(**V[nm])
            c = _zero(o["Etilde_xixi"], o["Etilde_xixi_witness"]) and _zero(o["E_xixi"], o["E_xixi_witness"])
            ok = ok and c
            det[kind][nm] = {"Etilde_xixi_witness": o["Etilde_xixi_witness"], "E_xixi_witness": o["E_xixi_witness"]}
    return ok, det


def check_C18c(mut=None):
    """X13 (c) on eq. (17)'s data [PLANE]: R4(xi,xi) = 0 at the horizon r = 2m (the check's content).  The held
    stress's tau(xi,xi) and pi(xi,xi) are reported: they vanish there by construction (tau proportional to g on the
    (v,u) block, g(xi,xi)|_H = 0), so they are deduced, not tested."""
    u_at = sp.Rational(1, 2) if mut == "off_horizon" else 0
    w = weyl_eq17(u_at, EPS if mut == "growth" else 0)
    hs = horizon_stress_eq17(u_at, False)
    ok = w["R4_xixi"] == 0 and abs(w["R4_xixi_float"]) < ZERO_TOL
    return ok, {"R4_xixi": w["R4_xixi_float"], "tau_xixi_deduced": str(hs["tau_xixi"]),
                "pi_xixi_deduced": str(hs["pi_xixi"])}


def check_C19(mut=None):
    """Lemma K: in Gaussian normal coordinates y'' (connection) = K_vv (Lie-derivative route, no Christoffel symbol)
    = the coefficient K_vv; scope control: in the lapse-2 chart the proper normal displacement obeys s'' = K_vv.
    Numeric: S_vv = 0 stays on the sheet to 1e-12; S_vv > 0 leaves the kept side; S_vv < 0 leaves the sheet into the
    bulk (stays in y >= 0); null norm conserved."""
    Kv = sp.Symbol("K_vv")
    t = tangent_deflection(Kv, 2 if mut == "lapse2" else 1, -1 if mut == "connection_sign" else 1)
    t2 = tangent_deflection(Kv, 2, -1 if mut == "connection_sign" else 1)
    sym_ok = t["difference"] == 0 and t["ydd"] == Kv and t["k_null"] == 0 and t2["s_dd"] == t2["K_vv"]
    isg = -1 if mut == "flipped_israel" else 1
    s0 = 1e-6 if mut == "pair_off" else 0.0
    z, pz, nz = (deflection_numeric(s, israel_sign=isg) for s in (s0, 1.0, -1.0))
    num_ok = (z["stays_on_sheet"] and (not pz["stays_kept_side"]) and pz["y_end"] < -1e-6
              and nz["stays_kept_side"] and (not nz["stays_on_sheet"]) and nz["y_end"] > 1e-6
              and all(abs(q["null_norm_end"]) < 1e-9 for q in (z, pz, nz)))
    return sym_ok and num_ok, {"ydd": str(t["ydd"]), "K_vv_lie": str(t["K_vv"]), "lapse2_s_dd": str(t2["s_dd"]),
                               "lapse2_K_vv_lie": str(t2["K_vv"]), "y_end_S0": z["y_end"], "y_end_S+1": pz["y_end"],
                               "y_end_S-1": nz["y_end"]}


def _stub_integrator(S_vv, nu=1, israel_sign=1, lam_end=1.0):
    """A broken integrator (C19b's harness mutation): it always reports that the generator stays on the sheet."""
    return {"S_vv": S_vv, "y_end": 0.0, "stays_on_sheet": True, "stays_kept_side": True, "leading_order_y_end": 0.0}


def check_C19b(mut=None):
    """The pair through Lemma K, with the integration decisive: the exact pair's generator stays on the sheet in
    deflection_numeric's integration; a control (the README alone at mu = 1/1000, no partner, integrated to affine
    parameter 1/4) must leave the sheet toward y < 0 with y_end within 1% of the independent leading order
    K_vv lam^2/2 (the explicit metric's other terms add a K_vv-independent 0.17% there, 2.8% at lam = 1); no zero
    total is called positive.
    The exact pair's net = 0 holds by construction and is reported, not tested.  Mutations: the exact pair replaced by
    a pair off by 1e-6 or by the README alone (the integration must see them leave), and a stub integrator that always
    'stays' (the control must catch it)."""
    deflect = _stub_integrator if mut == "stub_integrator" else None
    frac = {"pair_off": 1 - Fr(1, 10**6), "no_partner": 0}.get(mut, 1)
    o = pair_crossing(partner_fraction=frac, deflect=deflect)
    ctl = pair_crossing(T_readme=readme_flux(Fr(1, 1000)), partner_fraction=0, deflect=deflect, lam_end=0.25)
    cd = ctl["deflection"]
    ctl_ok = (not cd["stays_on_sheet"]) and cd["y_end"] < 0 and cd["leading_order_y_end"] != 0 and \
        abs(cd["y_end"] / cd["leading_order_y_end"] - 1) < 0.01
    ok = o["deflection"]["stays_on_sheet"] and ctl_ok and not _zero_called_positive(_clean({"x": o}), [])
    return ok, {"net": str(o["net"]), "y_end": o["deflection"]["y_end"], "net_status": o["net_status"],
                "control_net": str(ctl["net"]), "control_y_end": cd["y_end"],
                "control_leading_order": cd["leading_order_y_end"]}


def check_C19c(mut=None):
    """[PLANE] The pair tensor: for a partner tilted by b (symbolic), pi(xi,xi) from SMS eq. (20) on the full tensor
    (held stress + README + partner) equals the null-dust algebra of the pair alone, so the static held stress does not
    enter; T^pair(xi,xi) = 0; and pi(xi,xi) vanishes only at b = 0.  Mutations: a massive partner (l'.l' = -1; the
    null-dust route no longer applies) and a held momentum flux along the sphere (a non-static held stress)."""
    o = pair_tensor_eq17(TILT, sp.Symbol("j_held") if mut == "held_flux" else 0, -1 if mut == "massive_partner" else 0)
    zeros_b = sp.solve(o["pi_xixi_sms20"], TILT)
    ok = (o["routes_differ_by"] == 0 and not o["held_stress_enters"] and o["pair_xixi"] == 0 and zeros_b == [0])
    return ok, {"pi_xixi_sms20": str(o["pi_xixi_sms20"]), "pi_xixi_nulldust": str(o["pi_xixi_nulldust"]),
                "routes_differ_by": str(o["routes_differ_by"]), "held_stress_enters": o["held_stress_enters"],
                "zeros_in_b": [str(z) for z in zeros_b]}


_OUT_CACHE = {}


def _out():
    if "out" not in _OUT_CACHE:
        _OUT_CACHE["out"] = compute()
    return _OUT_CACHE["out"]


def check_CG(mut=None):
    """Guards: no banned argument name (sim2_facing.BANNED_ARGS) in this module's signatures, no banned key in the
    report, every row labelled with one of the six labels, no pair total, net or sum called positive anywhere."""
    out = json.loads(json.dumps(_out()))
    extra_funcs = ()
    if mut == "planted_key":
        out["results"]["X13d_pair"]["hold_time"] = 1
    elif mut == "planted_arg":
        def planted(gap):            # a planted signature: must be caught
            return gap
        extra_funcs = (planted,)
    elif mut == "planted_label":
        out["results"]["X13d_pair"]["label"] = "positive"
    elif mut == "zero_called_positive":
        out["results"]["X13d_pair"]["net_status"] = "positive"
    elif mut == "planted_statement":
        out["results"]["E_PASS_status"]["statement"] = "the README and its partner sum to a positive total per light ray"
    gd = address_guard(out, extra_funcs)
    ok = not (gd["bad_args"] or gd["bad_keys"] or gd["bad_labels"] or gd["zero_called_positive"])
    return ok, {k_: gd[k_] for k_ in ("bad_args", "bad_keys", "bad_labels", "zero_called_positive", "n_funcs")}


CHECKS = {
    "C15": (check_C15, "contracted Gauss (SMS eq. (3)) residual 0 at (1/3, 5/2, 7/10)",
            [("sign", "sign of R(k,n,k,n) flipped (spec: gives -0.6249)"),
             ("drop_quadratic", "the quadratic K terms dropped")]),
    "C16": (check_C16, "null transport (covariant, e parallel) and Raychaudhuri residuals 0; isotropic sigma^2 = 0",
            [("coordinate", "coordinate derivative of the component B_yy (spec: leaves 2 a_v^2/a^2)"),
             ("nperp2", "transverse count 2 used consistently (theta^2/2 and the trace-free part over 2)"),
             ("formula_count2", "the old sigma^2 := sum x^2 - theta^2/2 with theta^2/2 (a consistent wrong count the "
              "residual cannot see; the isotropic control must)"),
             ("rkk_sign", "sign of R(k,k) flipped")]),
    "C17": (check_C17, "Lemma S sheet: K(xi,xi)|_H = 0 for sheets y = F(u), degenerate and non-degenerate (scope: "
            "also non-stationary with u_H null, and growing)",
            [("off_null", "the spec's g_vv + eps y sin v: u = u_H no longer null, g(xi,xi)|_H = eps y sin v"),
             ("tilt", "the sheet tilted off xi, y = F(u) + eps v (K = -kappa n.xi: caught where kappa != 0)")]),
    "C18": (check_C18, "Lemma S bulk: R(xi,xi)|_{u=0} = 0 on the family named, stationary and null-preserving "
            "non-stationary",
            [("off_null", "the spec's g_vv + eps y sin v: u = 0 no longer null"),
             ("growth", "the section grows along v, C -> C (1 + eps v) (expansion; 162 forbids, read through "
              "H-FIXED-SIZE, M's, and H-FIXED-SIZE-AS-THETA-ZERO, the board's, put to M)"),
             ("depth_growth", "the y-extent grows along v, D -> D (1 + eps v) (expansion)"),
             ("shear", "shear at fixed volume, D -> D (1 + eps v)^2, C -> C/(1 + eps v) (theta = 0, sigma != 0)")]),
    "C18s": (check_C18s, "the bulk premise: Raychaudhuri route = Riemann route on every variant; shear at fixed size "
             "gives R(xi,xi) = -sigma^2 < 0",
             [("no_shear", "the shear removed (R(xi,xi) = 0: the strict inequality is the shear's)"),
              ("growth", "growth in place of shear (theta != 0 and R(xi,xi) > 0: the bound needs theta = 0)")]),
    "C18b": (check_C18b, "X13 (c): E~(xi,xi) = R(xi,n,xi,n) = 0 and E(xi,xi) = 0 on the bulk family's horizon",
             [("off_null", "the spec's g_vv + eps y sin v: u = 0 no longer null"),
              ("depth_growth", "the y-extent grows along v, D -> D (1 + eps v)"),
              ("growth", "the section grows along v, C -> C (1 + eps v): E~ = 0 but E != 0 (the E conjunct's content)")]),
    "C18c": (check_C18c, "X13 (c) on eq. (17)'s data: R4(xi,xi) = 0 at r = 2m",
             [("off_horizon", "evaluated off the horizon, u = 1/2 (r = 9/4 m): the zero is the horizon's"),
              ("growth", "the sphere grows along v, r^2 -> r^2 (1 + eps v) (162 forbids, read through H-FIXED-SIZE and "
               "H-FIXED-SIZE-AS-THETA-ZERO)")]),
    "C19": (check_C19, "Lemma K: y'' = K_vv (two routes); lapse-2 s'' = K_vv; S_vv = 0 stays to 1e-12; S_vv > 0 leaves "
            "y >= 0; S_vv < 0 leaves the sheet into the bulk",
            [("flipped_israel", "flipped Israel, K_vv = +S_vv/nu (must deflect the other way)"),
             ("lapse2", "a non-Gaussian chart (lapse 2) with y'' compared to K_vv unrescaled"),
             ("connection_sign", "every Christoffel symbol's sign flipped (the Lie-derivative route must disagree)"),
             ("pair_off", "the S_vv = 0 case given a residual net flux 1e-6 (a pair off by 1e-6)")]),
    "C19b": (check_C19b, "the exact pair: the integrated generator stays on the sheet; the README-alone control leaves "
             "it at the leading order; the zero total never 'positive'",
             [("pair_off", "partner = -(1 - 1e-6) T^R"), ("no_partner", "the README alone, no partner"),
              ("stub_integrator", "deflection_numeric replaced by a stub that always 'stays'")]),
    "C19c": (check_C19c, "[PLANE] the pair tensor: pi(xi,xi) by SMS (20) = null-dust route; held stress absent; zero "
             "only at b = 0",
             [("massive_partner", "a massive partner, l'.l' = -1"),
              ("held_flux", "a held momentum flux tau_v theta (a non-static held stress)")]),
    "CG": (check_CG, "guards: argument names, report keys, labels, pitfall 13",
           [("planted_key", "a planted key 'hold_time'"), ("planted_arg", "a planted function argument 'gap'"),
            ("planted_label", "a row labelled 'positive'"),
            ("zero_called_positive", "a zero pair total described as 'positive'"),
            ("planted_statement", "'sum to a positive total' planted in a statement row with no 'net' key")]),
}


def selftest():
    t0 = _wall.perf_counter()
    allok = True
    lines = []
    for cid, (fn, what, _m) in CHECKS.items():
        ok, det = fn(None)
        allok = allok and ok
        lines.append(f"{cid:5s} {'PASS' if ok else 'FAIL'}  {what}\n      {json.dumps(_clean(det))}")
    wall = _wall.perf_counter() - t0
    print("epass_pairing selftest (computed, READ and deduced; not verified; not seated)")
    print("\n".join(lines))
    print(f"selftest {'PASSED' if allok else 'FAILED'}: {len(CHECKS)} checks, wall {wall:.1f} s")
    return allok


def mutants():
    t0 = _wall.perf_counter()
    passed_mutants = []
    n = 0
    print("epass_pairing --mutants: each named mutation must make its check FAIL")
    for cid, (fn, what, muts) in CHECKS.items():
        for name, desc in muts:
            n += 1
            ok, det = fn(name)
            verdict = "check FAILS (as required)" if not ok else "MUTATION PASSES (the check cannot fail this way)"
            if ok:
                passed_mutants.append((cid, name))
            print(f"{cid:5s} [{name}] {desc}: {verdict}\n      {json.dumps(_clean(det))}")
    wall = _wall.perf_counter() - t0
    print(f"mutants: {n} run, {n - len(passed_mutants)} caught, {len(passed_mutants)} passed {passed_mutants}; "
          f"wall {wall:.1f} s")
    return not passed_mutants


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--mutants", action="store_true")
    ap.add_argument("--json", metavar="PATH")
    a = ap.parse_args(argv)
    rc = 0
    if a.selftest:
        rc |= 0 if selftest() else 1
    if a.mutants:
        rc |= 0 if mutants() else 1
    if a.json:
        out = _out()
        gd = address_guard(out)
        out["guard"] = gd
        with open(a.json, "w") as fh:
            json.dump(out, fh, indent=1)
        print(f"wrote {a.json}")
    if not (a.selftest or a.mutants or a.json):
        print(json.dumps(_out()["results"], indent=1)[:20000])
    return rc


if __name__ == "__main__":
    sys.exit(main())
