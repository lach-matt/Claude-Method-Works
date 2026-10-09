#!/usr/bin/env python3
"""epass_pairing.py -- E-PASS fix round, a standalone [FREE] owner: Lemma S (the stationary pairing law) and Lemma K (a
net-flux crossing kinks the bulk horizon), with the two identities they rest on (the contracted Gauss equation, SMS
eq. (3), and null transport with Raychaudhuri).  Build specification: lemmas/EPASS-DESIGN-SPEC.md, X13, X14 and checks
C15-C19 of its section 8.  sim2_passage.py imports this module by path for its X13 and X14; it is never copied there.
Computed, READ and deduced; not verified; not seated; 2026-10-09.

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
  132      "yes. And the passage is one way by nature, a black hole in and a white hole out, side views of the same
           corridor object" and "*different views of the same object"
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

WHAT IS COMPUTED HERE
  X13 LEMMA S [FREE] (computed as identities; deduced).
    (b) BULK FORM -- the primary statement under 179/180 (the corridor sits on neither plane, exclusive to the bulk).
        pairing_bulk(gvv): for a general stationary 5D metric D dy^2 + g_vv dv^2 + 2B dv du + C dOmega^2 with
        g_vv = -A(y,u) u^2 (degenerate) or -A(y,u) u (non-degenerate), A, B, C, D arbitrary functions of (y, u), NO
        field equation used: R(xi,xi)|_{u=0} = 0.  With Einstein + Lambda_5 (g(xi,xi) = 0 there, R finite, computed):
        kappa_5^2 T5(xi,xi) = 0 (deduced).  The README's 5D null flux across a stationary bulk horizon must be cancelled
        by an equal negative null flux along the same generators.
    (a) SHEET FORM -- applies to whichever sheet the README is on (172 (1): position 2's piece may carry it).
        pairing_sheet(gvv): a general sheet y = F(u) (F arbitrary) in dy^2 + g_vv dv^2 + 2 sqrt2 alpha(y)^2 dv du +
        4 beta(y)^2 dOmega^2 with alpha, beta arbitrary: K(xi,xi)|_H = 0, and with one-sided Israel
        S(xi,xi) = -nu [K(xi,xi) - (xi.xi) K] = 0 on the horizon, for g_vv = -alpha^2 u^2/2 (degenerate, u_H = 0) and
        -alpha^2 (u^2 - 1/9)/2 (non-degenerate, u_H = 1/3); also on the general metric of (b).  So, while the corridor
        is stationary, the net surface null flux across its horizon vanishes on every sheet tangent to xi, at any
        tension, any law and with matter (184): the README's T^R(xi,xi) >= 0 must be cancelled on the same sheet,
        generator by generator, by T^c(xi,xi) = -T^R(xi,xi).  A held static stress has T(xi,xi) = rho F -> 0 on the
        horizon (computed on eq. (17)'s chart), so the partner cannot be held stress: it must be a genuine negative null
        flux.
    (c) THE WEYL TERM GIVES NOTHING.  On the general stationary bulk of (b), E~(xi,xi) = R(xi,n,xi,n)|_{u=0} = 0
        (computed identity), so E(xi,xi) = E~(xi,xi) - R(xi,xi)/3 = 0 (SMS eq. (A10), READ PDF p.6, contracted with
        null xi).  On eq. (17)'s own data (owner B4._eq17 via sim2_facing, by path) R4(xi,xi)|_{r=2m} = 0 (computed,
        [PLANE]), which with the contracted Gauss equation (SMS eq. (3), READ PDF p.2) gives E(xi,xi) = 0 there
        (deduced).  A bulk field cannot change a sheet's surface flux (deduced).
    (d) READINGS (the board's): H-PAIR-CANCELS-ON-THE-HORIZON and H-PARTNER-IS-THE-COUPLING, re-read under 183: M chose
        "Yes: never violated as a pair"; the record carries H-NEC-NEVER-VIOLATED-AS-PAIR as M's ("never violated" holds
        net per light ray -- the board's wording of the option M chose).  The exact +/- null pair Lemma S demands is
        then admitted under 177 through the board's H-PARTNER-IS-THE-COUPLING, so E-PASS's stationary crossing is OPEN
        (the partner's supply is beyond the board's instruments), NOT refuted.  The pair's total is ZERO per light ray;
        it is never reported as "positive" (spec pitfall 13; 139 (2)'s positivity is a separate question).  The board
        notes, without claiming it as M's meaning, that a paired crossing changes S not at all -- the shape of
        129 (1)'s "it adds nothing to either position".
  X14 LEMMA K [FREE for sheets] (computed; deduced).
    tangent_deflection(Kvv): in Gaussian normal coordinates a null geodesic tangent to the sheet along the horizon
    generator has y'' = -Gamma^y_vv = K_vv (computed from the metric's connection and, independently, from the unit
    normal's covariant derivative; the lapse-2 chart is the control).  deflection_numeric(S_vv, nu=1) integrates that
    geodesic in an explicit Gaussian normal metric with h_vv = 2 y K_vv (+ y^2/3, and warped cross and angular terms),
    K_vv = -S_vv/nu, and reports whether it stays on the sheet and in y >= 0 to 1e-12.  S_vv = 0 stays; S_vv > 0 leaves
    the kept side (positive brane null energy pulls bulk light onto the sheet); S_vv < 0 leaves the sheet into the
    bulk.  So a bulk horizon C^2 up to the sheet, with the brane horizon as its trace, carries no net flux there
    (deduced); a net-flux crossing is a five-dimensional event (E-NS): the bulk horizon creases at the sheet or
    separates from the brane horizon.  The smooth-horizon identity (design 4's Lemma A) holds where the horizon is
    smooth but cannot be integrated across the README's support: its B_start budget and its "q >= 0 absorbs
    classically" are WITHDRAWN.
  C15 contracted Gauss (SMS eq. (3)) on dy^2 - A dt^2 + B dr^2 + C dOmega^2 (explicit polynomials) at
      (t, r, theta) = (1/3, 5/2, 7/10): residual 0; the R(k,n,k,n)-sign mutation gives -0.62486.
  C16 transport R(k,e,k,e) + dB_ee/dlambda + B_ee^2 = 0 (e parallel) and Raychaudhuri on
      -2 du dv + a^2 dy^2 + b^2 dz1^2 + c^2 dz2^2; the coordinate derivative of the component B_yy leaves 2 a_v^2/a^2.

STATED LIMIT (spec pitfall 3).  Lemma S needs stationarity DURING the crossing.  Stage 5 F1's quasi-static inflow is
small, but 162 forbids any growth ("The throat doesn't change size"), and the pair must be exact to the order at which
the corridor is held fixed: a residual net flux delta S along a generator bends it off the sheet at second order in
the affine parameter (Lemma K), and a growing section gives R(xi,xi) != 0 (C18's growth mutation).  Lemma S says
nothing about a corridor that changes; that case is E-NS (Lemma L, elsewhere).

OWNERS IMPORTED BY PATH, NEVER COPIED: lemmas/sim2_facing.py (BANNED_ARGS, BANNED_KEYS, B4._eq17 = b4_static's eq. (17)
data, lemma_n for the cross-reference of Lemma N's connection).  BANNED_KEYS of lemmas/sim2_passage.py are read from
its source text with ast (that file is being edited by another run, so it is parsed, never executed).
Conventions: R^a_bcd = d_c G^a_bd - d_d G^a_bc + G^a_ce G^e_bd - G^a_de G^e_bc, R_bd = R^a_bad (agrees with Wald's,
which SMS follow, on R_abcd and R_ab).  Units m = 1.  No argument names a separation; no output key names a distance,
time, redshift or speed (139 (4), 101 (7)).
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
X5 = [y, v, u, th, ph]
ALPHA, BETA = sp.Function("alpha")(y), sp.Function("beta")(y)
FSH = sp.Function("F")
A_, B_, C_, DD_ = (sp.Function(n)(y, u) for n in ("A", "B", "C", "Dfun"))
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
    ex = expr
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
    """The spec's mutation: g_vv + eps y sin v (d_y g_vv != 0 and d_v g_vv != 0 on the horizon)."""
    return gvv + EPS * y * sp.sin(v)


def _sheet_metric(gvv, metric):
    g = sp.zeros(5)
    if metric == "throat":
        g[0, 0] = 1
        g[1, 2] = g[2, 1] = sp.sqrt(2) * ALPHA**2
        g[3, 3] = 4 * BETA**2
        g[4, 4] = 4 * BETA**2 * sp.sin(th)**2
    else:
        g[0, 0] = DD_
        g[1, 2] = g[2, 1] = B_
        g[3, 3] = C_
        g[4, 4] = C_ * sp.sin(th)**2
    g[1, 1] = gvv
    return g


@functools.lru_cache(maxsize=None)
def pairing_sheet(gvv, u_h=0, metric="throat"):
    """Lemma S, sheet form.  For the sheet y = F(u) (F arbitrary, so the sheet is tangent to xi = d_v) in the metric
    `metric` ("throat": dy^2 + g_vv dv^2 + 2 sqrt2 alpha(y)^2 dv du + 4 beta(y)^2 dOmega^2; "general": the bulk form's
    D dy^2 + g_vv dv^2 + 2B dv du + C dOmega^2), returns K(xi,xi) = xi^a xi^b nabla_a n_b and
    S(xi,xi)/nu = -[K(xi,xi) - (xi.xi) trK] (one-sided Israel, S_ab = -nu (K_ab - h_ab K)) on the horizon u = u_h and
    on the sheet, with trK = div n (the unit normal field of the foliation y - F(u) = const)."""
    u_h = sp.sympify(u_h)
    g = _sheet_metric(gvv, metric)
    gi, G = _connection(g, X5)
    F = FSH(u)
    nl0 = [sp.Integer(1), sp.Integer(0), -sp.diff(F, u), sp.Integer(0), sp.Integer(0)]
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
def pairing_bulk(gvv, u_h=0, grow=0, grow_y=0):
    """Lemma S, bulk form (179/180's corridor exclusive to the bulk).  General stationary metric
    D dy^2 + g_vv dv^2 + 2B dv du + C (1 + grow v) dOmega^2 with D -> D (1 + grow_y v); A, B, C, D arbitrary functions of
    (y, u); no field equation used.  grow and grow_y are mutations (a section growing along v, which 162 forbids).
    Returns, on u = u_h: R(xi,xi); E~(xi,xi) = R(xi,n,xi,n) with n = d_y/sqrt(D) (normal to the sheets y = const,
    orthogonal to xi); E(xi,xi) = E~(xi,xi) - R(xi,xi)/3 (SMS (A10) contracted with null xi, READ PDF p.6); the Ricci
    scalar (finite?); and kappa_5^2 T5(xi,xi) = R(xi,xi) - (R/2 - Lambda_5) g(xi,xi) (Einstein + Lambda_5)."""
    u_h = sp.sympify(u_h)
    g = sp.zeros(5)
    g[0, 0] = DD_ * (1 + grow_y * v)
    g[1, 1] = gvv
    g[1, 2] = g[2, 1] = B_
    g[3, 3] = C_ * (1 + grow * v)
    g[4, 4] = C_ * (1 + grow * v) * sp.sin(th)**2
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
    is the horizon r = 2m.  With SMS eq. (17) contracted with null xi (Lambda_4 drops):
    E(xi,xi) = 8 pi G tau(xi,xi) + kappa^4 pi(xi,xi) - R4(xi,xi); the held stress terms are horizon_stress_eq17's."""
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
    tau(xi,xi) and pi(xi,xi) of SMS eq. (20) (READ PDF p.3), and l.xi.  The held stress's tau(xi,xi) = rho F (static
    frame) and pi(xi,xi) are proportional to g(xi,xi), which vanishes on the horizon."""
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
    l = -d_u.  Computed from the chart's metric (l.xi = -g_vu(0) = -sqrt2), so T^R(xi,xi) = 2 mu > 0 for mu > 0."""
    hs = horizon_stress_eq17(0, True)
    held = horizon_stress_eq17(0, False)
    mu_s = [s for s in hs["tau_xixi"].free_symbols if s.name == "mu"]
    val = sp.simplify(hs["tau_xixi"] - held["tau_xixi"])
    if mu_s:
        val = val.subs(mu_s[0], sp.sympify(mu))
    return val


def pair_crossing(T_readme=None, partner_fraction=1, nu=1):
    """Lemma S's pair on a sheet: the README's member T^R(xi,xi) (readme_flux(1) by default), a partner
    T^c = -partner_fraction T^R, and the net sheet null flux S(xi,xi) = T^R + T^c (the tension and the held stress add
    nothing to S(xi,xi) on the horizon: g(xi,xi) = 0 and horizon_stress_eq17).  Lemma S requires net = 0; Lemma K's
    deflection_numeric(net) shows what a nonzero net does.  The total is reported as zero or nonzero, never as
    "positive" (spec pitfall 13)."""
    TR = sp.nsimplify(readme_flux(1) if T_readme is None else T_readme)
    Tc = -sp.nsimplify(partner_fraction) * TR
    net = sp.nsimplify(TR + Tc)
    defl = deflection_numeric(float(net), nu=nu)
    return {"readme_member": TR, "partner_member": Tc, "net": net,
            "net_status": "zero net per light ray (not positive)" if net == 0 else "nonzero net",
            "lemma_s_admits": bool(net == 0), "deflection": defl}


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
def transport_residual(mode="covariant", nperp=3):
    """C16: on -2 du dv + a(v,y)^2 dy^2 + b(v,y)^2 dz1^2 + c(v,y)^2 dz2^2, k = d_v (affine), e = d_y/a:
    R(k,e,k,e) + dB_ee/dlambda + B_ee^2 with B_ij = Gamma^u_ij, the derivative taken covariantly along k (mode
    "covariant": e parallel, so d/dlambda of B(e,e)) or, the mutation, as the coordinate derivative of the component
    B_yy (mode "coordinate"); also e's parallel-transport residual, and Raychaudhuri
    dtheta/dlambda + theta^2/nperp + sigma^2 + R(k,k) (nperp = 3 is the true transverse count; 2 is a mutation)."""
    uu, vv, yy, z1, z2 = sp.symbols("u v y z1 z2", real=True)
    a, b, c = (sp.Function(n)(vv, yy) for n in "abc")
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
    exps = [sp.diff(f, vv) / f for f in (a, b, c)]
    theta = sum(exps)
    sig2 = sum(x**2 for x in exps) - theta**2 / 3
    res_r = sp.simplify(sp.diff(theta, vv) + theta**2 / nperp + sig2 + Rkk)
    return {"transport_residual": res_t, "e_parallel": par, "raychaudhuri_residual": res_r, "R_keke": R_keke,
            "expected_coordinate_leftover": sp.simplify(2 * sp.diff(a, vv)**2 / a**2)}


# ------------------------------------------------------------------------------------------------ X14 Lemma K
@functools.lru_cache(maxsize=None)
def tangent_deflection(Kvv, lapse=1):
    """Lemma K's kinematics.  Gaussian normal chart (lapse = 1): lapse^2 dy^2 + h_vv dv^2 + 2 h_vu dv du + h_uu du^2
    + h_ang dOmega^2, h_vv = -u^2/2 + 2 y Kvv + y^2 P(y,u), h_vu = sqrt2 + y Q(y,u), h_uu = y W(y,u),
    h_ang = 4 + y Z(y,u) (P, Q, W, Z arbitrary).  The generator of the brane horizon is y = 0 = u with k = d_v.
    Returns y'' = -Gamma^y_ab k^a k^b from the connection, and K_vv = k^a k^b nabla_a n_b from the unit normal
    n_b = lapse delta^y_b, independently; in Gaussian normal coordinates y'' = K_vv.  lapse = 2 (a non-Gaussian chart
    compared without rescaling) is the control: there y'' = K_vv/2."""
    P, Q, W, Z = (sp.Function(n)(y, u) for n in ("P", "Q", "W", "Z"))
    g = sp.zeros(5)
    g[0, 0] = sp.sympify(lapse)**2
    g[1, 1] = -u**2 / 2 + 2 * y * Kvv + y**2 * P
    g[1, 2] = g[2, 1] = sp.sqrt(2) + y * Q
    g[2, 2] = y * W
    g[3, 3] = 4 + y * Z
    g[4, 4] = (4 + y * Z) * sp.sin(th)**2
    gi, G = _connection(g, X5)
    at = {y: 0, u: 0}
    ydd = sp.simplify((-G[0][1][1]).subs(at))
    nlow = [sp.sympify(lapse), 0, 0, 0, 0]
    K_vv = sp.simplify((-sum(G[c][1][1] * nlow[c] for c in range(5))).subs(at))
    return {"ydd": ydd, "K_vv": K_vv, "difference": sp.simplify(ydd - K_vv), "k_null": sp.simplify(g[1, 1].subs(at))}


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
    (|y| <= 1e-12) and in the kept side (y >= -1e-12), the null-norm drift, and the leading-order y = K_vv lam^2/2."""
    Kvv = -israel_sign * S_vv / nu
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
         "side views of the same corridor object / *different views of the same object", "source": src},
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
    ]


def readings():
    """The readings this module's results bear on, with whose they are and their standing after 183 and 184."""
    return [
        {"name": "H-NEC-NEVER-VIOLATED-AS-PAIR", "whose": "carried as M's in the record (183); the gloss is the board's "
         "wording of the option M chose", "content": "117/120's \"never violated\" holds net per light ray: zero net "
         "null energy along each light ray; a negative member paired along the same light rays is the appearance",
         "bearing": "admits Lemma S's exact pair; axiom Z3 re-read as net per light ray"},
        {"name": "H-PAIR-CANCELS-ON-THE-HORIZON", "whose": "the board's (offered for 176/178)", "content": "the "
         "README's positive null energy and its partner's equal negative one sum to zero along every crossed generator; "
         "the NEC \"appears broken\" on one member and holds for the pair", "bearing": "under 183 this is the pair M "
         "chose to allow; Lemma S says it is not optional but required for a stationary crossing"},
        {"name": "H-PARTNER-IS-THE-COUPLING", "whose": "the board's (decided under 149; admitted under 183 per the "
         "record)", "content": "177's appearance covers the exact negative null flux Lemma S requires along the "
         "horizon (the coupled-ends mechanism of Maldacena-Qi and Gao-Jafferis-Wall)", "bearing": "E-PASS's "
         "stationary crossing is OPEN through 177, not refuted; the partner's supply is beyond the board's "
         "instruments"},
        {"name": "H-README-AS-NULL-DUST", "whose": "the board's (opening.py)", "content": "the README is null dust "
         "T = mu l (x) l", "bearing": "readme_flux: T^R(xi,xi) = mu (l.xi)^2 > 0"},
        {"name": "H-STATIONARY-CROSSING", "whose": "the board's (spec 4.3)", "content": "the corridor (bulk and "
         "sheets) is stationary while the README crosses (H-QUASI-STATIC-CORRIDOR, 141, 162)", "bearing": "Lemma S's "
         "premise; refused, the crossing is E-NS (Lemma K)"},
        {"name": "H-CORRIDOR-IN-BULK", "whose": "M's (179/180)", "content": "the corridor sits on neither position's "
         "plane; it only bridges them, and is exclusive to the bulk", "bearing": "Lemma S's bulk form is primary"},
        {"name": "H-NO-MATTER-FREE-PLANES", "whose": "M's (184)", "content": "every plane carries matter",
         "bearing": "Lemma S is law- and tension-independent and holds with matter; matter-free results are limits"},
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


def compute():
    """Every value X13 and X14 need, each row labelled; [FREE]/[PLANE] tags."""
    rows = {}
    sh = {}
    for kind in ("degenerate", "nondegenerate"):
        gvv, uh = sheet_gvv(kind)
        sh["throat_" + kind] = pairing_sheet(gvv, uh, "throat")
        gb, ub = bulk_gvv(kind)
        sh["general_" + kind] = pairing_sheet(gb, ub, "general")
    rows["X13a_sheet"] = {"label": "computed", "tag": "[FREE]", "what": "K(xi,xi) and S(xi,xi)/nu on the horizon for a "
                          "general sheet y = F(u); no field equation, no tension, no law",
                          "cases": {k_: {"K_xixi": o["K_xixi"], "S_xixi_over_nu": o["S_xixi_over_nu"],
                                         "trK_finite": o["trK_finite"], "xixi_on_H": o["xixi_on_H"]}
                                    for k_, o in sh.items()}}
    rows["X13a_statement"] = {"label": "deduced", "tag": "[FREE]", "statement": "While the corridor is stationary the "
                              "net surface null flux across its horizon vanishes on every sheet tangent to xi (P1, "
                              "position 2's piece at any depth, any profile), kappa = 0 and kappa != 0, any tension or "
                              "law, with matter (184): T^c(xi,xi) = -T^R(xi,xi) on the README's own sheet, generator by "
                              "generator.  Applies to whichever sheet the README is on (172 (1))."}
    held = horizon_stress_eq17(0, False)
    off = horizon_stress_eq17(sp.Rational(1, 2), False)
    rows["X13a_held_stress"] = {"label": "computed", "tag": "[PLANE] chart; [FREE] by the deduction g(xi,xi) = 0",
                                "tau_xixi_on_H": held["tau_xixi"], "pi_xixi_on_H": held["pi_xixi"],
                                "tau_xixi_at_u_half": off["tau_xixi"], "statement": "a held AdS2-invariant stress has "
                                "tau(xi,xi) = 0 and pi(xi,xi) = 0 on the horizon: it cannot be the partner; the partner "
                                "must be a genuine negative null flux"}
    wr = horizon_stress_eq17(0, True)
    rows["X13a_readme_flux"] = {"label": "computed", "tag": "[PLANE] chart (sign [FREE]: (l.xi)^2 > 0 for any "
                                "transverse null l)", "T_R_xixi_per_mu": readme_flux(1), "l_dot_xi": wr["l_dot_xi"],
                                "l_null": wr["l_null"], "pi_xixi_with_readme": wr["pi_xixi"],
                                "reading": "H-README-AS-NULL-DUST (the board's)"}
    bk = {}
    for kind in ("degenerate", "nondegenerate"):
        gb, ub = bulk_gvv(kind)
        bk[kind] = pairing_bulk(gb, ub)
    rows["X13b_bulk"] = {"label": "computed (identity); deduced (the T5 line, with Einstein + Lambda_5)",
                         "tag": "[FREE]; the primary statement under 179/180",
                         "cases": {k_: {"R_xixi": o["R_xixi"], "kappa2_T5_xixi": o["kappa2_T5_xixi"],
                                        "R_scalar_finite": o["R_scalar_finite"], "xixi_on_H": o["xixi_on_H"]}
                                   for k_, o in bk.items()},
                         "statement": "R(xi,xi) = 0 on a stationary bulk horizon with no field equation; with Einstein "
                         "+ Lambda_5, T5(xi,xi) = 0: the README's 5D null flux must be cancelled by an equal negative "
                         "null flux along the same generators"}
    rows["X13b_label_note"] = {"label": "standard-not-READ", "statement": "R(xi,xi) = 0 on any Killing horizon is a "
                               "standard result; here it is computed for the general family named, not READ"}
    w17 = weyl_eq17(0)
    rows["X13c_weyl"] = {"label": "computed; READ (SMS gr-qc/9910076v3 eq. (A10), PDF p.6); deduced", "tag": "[FREE]",
                         "cases": {k_: {"Etilde_xixi": o["Etilde_xixi"], "E_xixi": o["E_xixi"]}
                                   for k_, o in bk.items()},
                         "statement": "E~(xi,xi) = R(xi,n,xi,n) = 0 and E(xi,xi) = E~(xi,xi) - R(xi,xi)/3 = 0 on the "
                         "stationary bulk horizon: the static bulk's Weyl term supplies nothing along the generators; a "
                         "bulk field cannot change a sheet's surface flux"}
    rows["X13c_eq17"] = {"label": "computed; READ (SMS eq. (3), PDF p.2; eq. (17), PDF p.3); deduced",
                         "tag": "[PLANE]", "R4_xixi_on_H": w17["R4_xixi"], "g_vu_on_H": w17["g_vu_on_H"],
                         "R4_xixi_at_u_half": weyl_eq17(sp.Rational(1, 2))["R4_xixi_float"],
                         "statement": "eq. (17)'s own data (owner B4._eq17): R4(xi,xi) = 0 at r = 2m; with Gauss and "
                         "the held stress's tau(xi,xi) = pi(xi,xi) = 0, E(xi,xi) = 0 there.  The matter-free plane is a "
                         "limit only (184); with held matter the same zero holds"}
    pc = pair_crossing()
    rows["X13d_pair"] = {"label": "computed (the ledger); deduced (Lemma S)", "tag": "[FREE]",
                         "readme_member": pc["readme_member"], "partner_member": pc["partner_member"],
                         "net": pc["net"], "net_status": pc["net_status"],
                         "stays_on_sheet": pc["deflection"]["stays_on_sheet"]}
    rows["X13d_readings"] = {"label": "OPEN", "statement": "H-PAIR-CANCELS-ON-THE-HORIZON and H-PARTNER-IS-THE-COUPLING "
                             "(the board's), re-read under 183: the exact +/- null pair is admitted under 177; E-PASS's "
                             "stationary crossing is OPEN (supply beyond the board's instruments), NOT refuted.  The "
                             "board notes, without claiming it as M's meaning, that a paired crossing changes S not at "
                             "all -- the shape of 129 (1)'s words.", "readings": readings()}
    rows["X13_limit"] = {"label": "deduced", "statement": "stated limit (pitfall 3): Lemma S needs stationarity during "
                         "the crossing; 162 forbids growth; the pair must be exact to the order at which the corridor "
                         "is held fixed"}
    td = tangent_deflection(sp.Symbol("K_vv"))
    tdl = tangent_deflection(sp.Symbol("K_vv"), 2)
    rows["X14_tangent"] = {"label": "computed (Gaussian normal identity)", "tag": "[FREE for sheets]",
                           "ydd": td["ydd"], "K_vv": td["K_vv"], "difference": td["difference"],
                           "control_lapse2_ydd": tdl["ydd"], "control_lapse2_K_vv": tdl["K_vv"],
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
                             "mutant_coordinate_leftover": transport_residual("coordinate")["transport_residual"]}
    rows["E_PASS_status"] = {"label": "OPEN", "statement": "E-PASS (stationary crossing) is OPEN through 177 under 183 "
                             "(H-PARTNER-IS-THE-COUPLING admitted); not refuted.  A net-flux crossing is E-NS."}
    return _clean({"module": "epass_pairing", "status": "computed, READ and deduced; not verified; not seated; "
                   "2026-10-09", "m_words": m_words(), "results": rows})


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


def _zero_called_positive(o, acc):
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
        for x in o.values():
            _zero_called_positive(x, acc)
    elif isinstance(o, (list, tuple)):
        for x in o:
            _zero_called_positive(x, acc)
    return acc


def address_guard(out, extra_funcs=(), extra_keys=None):
    """Keys of `out` against BANNED_KEYS (sim2_facing's and sim2_passage's); this module's function signatures (and
    extra_funcs) against sim2_facing.BANNED_ARGS (names only, labelled as such); every result row's label among the six;
    no zero pair total described as positive (pitfall 13)."""
    mod = sys.modules[__name__]
    funcs = []
    for _, f in inspect.getmembers(mod):
        f = getattr(f, "__wrapped__", f)          # lru_cache-wrapped functions are checked through their wrapped body
        if inspect.isfunction(f) and f.__module__ == mod.__name__:
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
    """Transport (covariant, e parallel) and Raychaudhuri residuals 0."""
    o = transport_residual("coordinate" if mut == "coordinate" else "covariant", 2 if mut == "nperp2" else 3)
    ok = o["transport_residual"] == 0 and all(p == 0 for p in o["e_parallel"]) and o["raychaudhuri_residual"] == 0
    det = {"transport_residual": str(o["transport_residual"]), "raychaudhuri_residual": str(o["raychaudhuri_residual"])}
    if mut == "coordinate":
        det["leftover_is_2av2_over_a2"] = bool(sp.simplify(o["transport_residual"] - o["expected_coordinate_leftover"])
                                              == 0)
    return ok, det


def check_C17(mut=None):
    """Lemma S, sheet form: K(xi,xi)|_H = 0 and S(xi,xi)|_H = 0 (symbolic zero and numeric witness), degenerate and
    non-degenerate, throat and general metrics; trK finite."""
    ok, det = True, {}
    for metric in ("throat", "general"):
        for kind in ("degenerate", "nondegenerate"):
            gvv, uh = sheet_gvv(kind) if metric == "throat" else bulk_gvv(kind)
            if mut == "non_stationary":
                gvv = non_stationary(gvv)
            o = pairing_sheet(gvv, uh, metric)
            c = (_zero(o["K_xixi"], o["K_xixi_witness"]) and _zero(o["S_xixi_over_nu"], o["S_xixi_over_nu_witness"])
                 and o["trK_finite"])
            ok = ok and c
            det[metric + "_" + kind] = {"K_xixi_witness": o["K_xixi_witness"],
                                        "S_xixi_over_nu_witness": o["S_xixi_over_nu_witness"]}
    return ok, det


def check_C18(mut=None):
    """Lemma S, bulk form: R(xi,xi)|_{u=0} = 0 and kappa^2 T5(xi,xi) = 0 (R finite), both g_vv forms."""
    ok, det = True, {}
    for kind in ("degenerate", "nondegenerate"):
        gvv, uh = bulk_gvv(kind)
        if mut == "v_dependence":
            gvv = non_stationary(gvv)
        o = pairing_bulk(gvv, uh, EPS if mut == "growth" else 0)
        c = (_zero(o["R_xixi"], o["R_xixi_witness"]) and _zero(o["kappa2_T5_xixi"], o["kappa2_T5_xixi_witness"])
             and o["R_scalar_finite"])
        ok = ok and c
        det[kind] = {"R_xixi_witness": o["R_xixi_witness"], "kappa2_T5_xixi_witness": o["kappa2_T5_xixi_witness"]}
    return ok, det


def check_C18b(mut=None):
    """X13 (c), bulk: E~(xi,xi) = R(xi,n,xi,n) = 0 and E(xi,xi) = 0 on the horizon, both g_vv forms."""
    ok, det = True, {}
    for kind in ("degenerate", "nondegenerate"):
        gvv, uh = bulk_gvv(kind)
        if mut == "v_dependence":
            gvv = non_stationary(gvv)
        o = pairing_bulk(gvv, uh, 0, EPS if mut == "depth_growth" else 0)
        c = _zero(o["Etilde_xixi"], o["Etilde_xixi_witness"]) and _zero(o["E_xixi"], o["E_xixi_witness"])
        ok = ok and c
        det[kind] = {"Etilde_xixi_witness": o["Etilde_xixi_witness"], "E_xixi_witness": o["E_xixi_witness"]}
    return ok, det


def check_C18c(mut=None):
    """X13 (c) on eq. (17)'s data [PLANE]: R4(xi,xi) = 0 at the horizon r = 2m, and the held stress's tau(xi,xi) and
    pi(xi,xi) vanish there."""
    u_at = sp.Rational(1, 2) if mut == "off_horizon" else 0
    w = weyl_eq17(u_at, EPS if mut == "growth" else 0)
    hs = horizon_stress_eq17(u_at, False)
    ok = w["R4_xixi"] == 0 and abs(w["R4_xixi_float"]) < ZERO_TOL and hs["tau_xixi"] == 0 and hs["pi_xixi"] == 0
    return ok, {"R4_xixi": w["R4_xixi_float"], "tau_xixi": str(hs["tau_xixi"]), "pi_xixi": str(hs["pi_xixi"])}


def check_C19(mut=None):
    """Lemma K: y'' = K_vv (Gaussian normal); S_vv = 0 stays on the sheet to 1e-12; S_vv > 0 leaves the kept side;
    S_vv < 0 leaves the sheet into the bulk (stays in y >= 0)."""
    lapse = 2 if mut == "lapse2" else 1
    Kv = sp.Symbol("K_vv")
    t = tangent_deflection(Kv, lapse)
    sym_ok = t["difference"] == 0 and t["ydd"] == Kv and t["k_null"] == 0
    isg = -1 if mut == "flipped_israel" else 1
    s0 = 1e-6 if mut == "pair_off" else 0.0
    z, pz, nz = (deflection_numeric(s, israel_sign=isg) for s in (s0, 1.0, -1.0))
    num_ok = (z["stays_on_sheet"] and (not pz["stays_kept_side"]) and pz["y_end"] < -1e-6
              and nz["stays_kept_side"] and (not nz["stays_on_sheet"]) and nz["y_end"] > 1e-6
              and all(abs(q["null_norm_end"]) < 1e-9 for q in (z, pz, nz)))
    return sym_ok and num_ok, {"ydd": str(t["ydd"]), "K_vv": str(t["K_vv"]), "y_end_S0": z["y_end"],
                               "y_end_S+1": pz["y_end"], "y_end_S-1": nz["y_end"]}


def check_C19b(mut=None):
    """The pair through Lemma K: the exact pair gives net 0 (exact), a generator that stays on the sheet, and a status
    that never calls the zero total positive."""
    frac = {"pair_off": 1 - Fr(1, 10**6), "no_partner": 0}.get(mut, 1)
    o = pair_crossing(partner_fraction=frac)
    ok = (o["net"] == 0 and o["lemma_s_admits"] and o["deflection"]["stays_on_sheet"]
          and not _zero_called_positive(_clean({"x": o}), []))
    return ok, {"net": str(o["net"]), "y_end": o["deflection"]["y_end"], "net_status": o["net_status"]}


_OUT_CACHE = {}


def _out():
    if "out" not in _OUT_CACHE:
        _OUT_CACHE["out"] = compute()
    return _OUT_CACHE["out"]


def check_CG(mut=None):
    """Guards: no banned argument name (sim2_facing.BANNED_ARGS) in this module's signatures, no banned key in the
    report, every row labelled with one of the six labels, no zero pair total called positive."""
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
    gd = address_guard(out, extra_funcs)
    ok = not (gd["bad_args"] or gd["bad_keys"] or gd["bad_labels"] or gd["zero_called_positive"])
    return ok, {k_: gd[k_] for k_ in ("bad_args", "bad_keys", "bad_labels", "zero_called_positive", "n_funcs")}


CHECKS = {
    "C15": (check_C15, "contracted Gauss (SMS eq. (3)) residual 0 at (1/3, 5/2, 7/10)",
            [("sign", "sign of R(k,n,k,n) flipped (spec: gives -0.6249)"),
             ("drop_quadratic", "the quadratic K terms dropped")]),
    "C16": (check_C16, "null transport (covariant, e parallel) and Raychaudhuri residuals 0",
            [("coordinate", "coordinate derivative of the component B_yy (spec: leaves 2 a_v^2/a^2)"),
             ("nperp2", "theta^2/2 in place of theta^2/3 (wrong transverse count)")]),
    "C17": (check_C17, "Lemma S sheet: K(xi,xi)|_H = 0 = S(xi,xi)|_H, general sheet, degenerate and non-degenerate",
            [("non_stationary", "g_vv + eps y sin v (non-stationary)")]),
    "C18": (check_C18, "Lemma S bulk: R(xi,xi)|_{u=0} = 0 and kappa^2 T5(xi,xi) = 0, general stationary metric",
            [("v_dependence", "g_vv + eps y sin v (v-dependence)"),
             ("growth", "angular section grows along v, C -> C (1 + eps v) (162 forbids)")]),
    "C18b": (check_C18b, "X13 (c): E~(xi,xi) = R(xi,n,xi,n) = 0 and E(xi,xi) = 0 on the stationary bulk horizon",
             [("v_dependence", "g_vv + eps y sin v (v-dependence)"),
              ("depth_growth", "the y-extent grows along v, D -> D (1 + eps v)")]),
    "C18c": (check_C18c, "X13 (c) on eq. (17)'s data: R4(xi,xi) = 0 at r = 2m; held tau(xi,xi) = pi(xi,xi) = 0",
             [("off_horizon", "evaluated off the horizon, u = 1/2 (r = 9/4 m)"),
              ("growth", "the sphere grows along v, r^2 -> r^2 (1 + eps v) (162 forbids)")]),
    "C19": (check_C19, "Lemma K: y'' = K_vv; S_vv = 0 stays to 1e-12; S_vv > 0 leaves y >= 0; S_vv < 0 leaves the "
            "sheet into the bulk",
            [("flipped_israel", "flipped Israel, K_vv = +S_vv/nu (must deflect the other way)"),
             ("lapse2", "a non-Gaussian chart (lapse 2) compared without rescaling"),
             ("pair_off", "the S_vv = 0 case given a residual net flux 1e-6 (a pair off by 1e-6)")]),
    "C19b": (check_C19b, "the exact pair: net 0, the generator stays on the sheet, the zero total never 'positive'",
             [("pair_off", "partner = -(1 - 1e-6) T^R"), ("no_partner", "the README alone, no partner")]),
    "CG": (check_CG, "guards: argument names, report keys, labels, pitfall 13",
           [("planted_key", "a planted key 'hold_time'"), ("planted_arg", "a planted function argument 'gap'"),
            ("planted_label", "a row labelled 'positive'"),
            ("zero_called_positive", "a zero pair total described as 'positive'")]),
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
