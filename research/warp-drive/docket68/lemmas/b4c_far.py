#!/usr/bin/env python3
"""b4c_far.py -- Warp Theorem lemma B4c (the far boundary T strictly untrapped, uniformly in time), rebuilt on an
ellipsoidal far surface.  A new owner beside lemmas/b4_global.py, which it imports by path and never copies.
Computed, READ and deduced; not verified; not seated; 2026-10-09.  Revised the same day on two reviews by separate AI
sessions inside this project (not an outside review); their findings are applied here, and this revision has not
itself had a separate-session check.  Note: lemmas/B4C-FAR.md.

WHY.  b4_global.py's B4c found a ROUND far surface untrapped only if ell > 2 R_reach, a bound that grows with the README
(N^(1/3)), and a tipped parabola that needs a depth growing as N^(2/3)/c.  The item-186 window checker -- a separate AI
session inside this project (lemmas/ITEM186-K-PER-CORRIDOR.md, section 8 and History), not an outside review -- found
the parabola's published signs to be sampling artefacts near the plane, and a convex ellipsoidal surface
(u/U)^2 + (w/W)^2 = 1, meeting the plane square-on, untrapped for W/U >= 1.74 at every c = ell/m it scanned (1e-6 to
1e9) and trapped at 1.70.  This instrument proves that exactly INSIDE THE BOARD'S FAR MODEL, finds the exact threshold,
and says what B4c then earns -- and why, on that model, it cannot turn green.

CLI   python3 b4c_far.py               the report (every row labelled)
      python3 b4c_far.py --selftest    every check, each able to fail (~1 min)
      python3 b4c_far.py --mutants     every named mutation of every check; each must make its check FAIL (exit 1 if
                                       any mutation passes)
      python3 b4c_far.py --json PATH   compute()'s rows as JSON

LABELS.  computed / READ (verbatim + page) / deduced / STRUCTURAL / standard-not-READ / OPEN.  M's words are quoted
verbatim from M-RULINGS-2026-10-03.md, typing kept; the board's readings are named H-... and kept apart from them.

M'S WORDS USED (verbatim)
  139 (1)  M answered "1 - yes" to the board's question whether position 2's plane is the negative-tension one, a
           quarter of ours, with ours positive (carried as H-P2-NEGATIVE-PLANE).
  152 (1)  "two separate positions connected by/reached through a dimension."
  152 (2)  "I had not considered this yet. It could very well be possible, so let's consider this an option and check it."
  157      "we already have at least half the model, our current universe."
  158 (2)  "Exactly as long as the write needs  I should think"
  160      "the corridor and the opening are the same object"
  162      "... The throat doesn't change size because the whole chain object only every takes on the size that contains
           the README upon opening. It is and always will be only the size that is needed to hold the object once and
           at once"
  163      M chose: "All together, one whole"  (the option text, the board's: the README carried in by the inflow,
           115 (c), and held as a single whole at the fixed size)
  166      M chose: "Both planes at once"  (to "Is the corridor's eq. (17) on position 2's plane?")
  179/180  "Let's approach this from a different angle. We know the corridor *does not sit on either position's plane,
           it only bridges them. So one could surmise that the corridor is exclusive to the bulk."
  183      M chose: "Yes: never violated as a pair"
  184      "There are no matter free planes"
  187 (3)  M chose: "Seat both" -- clauses (G) and (Z) in the board's wording: (G) "the corridor sits in the bulk, on
           neither plane (179/180), with eq. (17) kept only as a plane's possible reading of the corridor's mouth";
           (Z) "\"null energy never violated\" holds net along each light ray (183)"
  192      "this appears to be a question to put to the math language hierarchy cypher"
  194      "Disregard that last ruling. I want that question put to the cypher"  (item 193, H-PAIR-AXIOM, is withdrawn
           by 194 and not carried; input F5 is OPEN; nothing here uses 193)
  195      "The README is not a pair"
  196      "Review all tasks running. Stop any that are no longer relevant. All questions get works through the cypher"

THE BOARD'S READINGS USED (named, the board's; withdrawn if M corrects them)
  H-FAR-MODEL (b4_global.py): g = (ell/z)^2 (-dt^2 + du^2 + dw^2 + rho(u)^2 dOmega^2), z = ell + |w|, rho^2 = u^2 + a^2
    -- Randall-Sundrum II's conformal form with B4a's join (the board's reading of 152 (1), encoded as
    H-SEPARATE-JOINED-THROUGH-DIMENSION) carried as a throat column of conformal radius a at every depth.  A model, not a
    solution.  What it carries, all of it load-bearing somewhere below: (i) a throat ON OUR PLANE (its w = 0 slice is
    -dt^2 + du^2 + (u^2 + a^2) dOmega^2) joining position 1's sheet (u > 0) and position 2's (u < 0) under ONE
    positive-tension warp -- the on-plane configuration that seated (G) moves into the bulk, with position 2's sheet
    positive where 139 (1) has position 2's plane negative, and no bulk between two planes as in 166; (ii) the join
    column at every depth, which T's tip crosses; (iii) the RS-II warp and a matter-free plane on all of T; (iv) the
    model's causal structure everywhere inside T, the column at every depth included, as a well-posed prior state;
    (v) under 179 the corridor sits in the bulk, so its depth w_c must lie inside the cover (U >= 1.05 (R_core + w_c
    + 2T)); no ruling and no computation here bounds w_c, and a corridor reaching down the column to depth W would put
    T's tip inside the corridor itself -- OPEN.
  H-FAR-FIELD-EXTENSION (this file, for X8 and X11 only): a far field extended into the bulk isotropically in the
    coordinate distance from its centre (E1; centred on the plane in X8, at depth w_c in X11) or in g_uu alone (E2) --
    test extensions, not solutions.
  The cover U = 1.05 R_reach and R_reach = R_core + 2T (o3_write W3's picture: the README lay inside radius
    R_core + T when the write began, and its influence spreads at most T further by the closing).

RESULTS (units m = 1; c = ell/m; T_E = the ellipse {(u/U)^2 + (w/W)^2 = 1} x S^2, mirror-doubled, k = W/U)
  X0 OWNER AGREEMENT (computed).  The general level-set theta+ here -- b4_global's own recipe, div n over sqrt|g| with
     the lapse minus a_n, for any F and any static diagonal metric -- equals b4_global.far_boundary()'s closed form on
     the round T exactly (sympy), and b4_global.tipped_far_boundary()'s minimum on the owner's grid to 1e-12.
  X1 THE ELLIPSE IN CLOSED FORM (computed, exact).  On T_E, with D = sqrt(u^2/U^4 + w^2/W^4),
         P = 1/(U^2 W^2 D^2) + 2 u^2/(U^2 (u^2 + a^2)),      theta+ = -theta- = ((ell + w) P - 3 w/W^2) / (ell D),
     so theta+(tip) = (W^2 + W ell - 3U^2)/(U^2 ell) (the checker's form) and W = U gives the owner's round formula.
     T_E meets the plane square-on (dF/dw = 0 at w = 0), so the mirror and the warp's kink add no term.
  X2 THE THEOREM WITHIN H-FAR-MODEL (deduced from X1; its one inequality machine-checked by z3, with vacuity and encoding
     guards).  With K = k^2, x = (u/U)^2, b = (a/U)^2 and Q = W^2 P = K/(1 + (K - 1) x) + 2 K x/(x + b):
         K >= 3 and (K - 1) b <= 2   ==>   Q >= 3 on all of T_E   ==>   theta+ = (ell P + (w/W^2)(Q - 3))/(ell D)
         >= P/D >= kappa >= U/W^2 > 0  at every point and EVERY ell > 0.
     The side condition reads a <= U at W = sqrt(3) U.  At W = sqrt(3) U exactly the tip reads sqrt(3)/U for every ell.
  X3 SHARP (computed, exact).  For W < sqrt(3) U the tip is trapped whenever ell < (3U^2 - W^2)/W: sqrt(3) = 1.7320508...
     is the exact threshold for "untrapped at every ell" in the model, between the checker's 1.70 (trapped) and 1.74.
  X4 THE SCAN (computed, 30-digit, the general code, independent of X1's algebra).  At the example README and c = 1e-6
     ... 1e9: k = sqrt(3), 1.74, 2 untrapped with min theta+ >= U/W^2; k = 1.70 trapped exactly below X3's switch.
  X5 THE SHAPE IS FREE OF N AND ell; THE SIZE IS NOT (deduced + computed).  The threshold is a pure ratio; U(N) enters
     only through b = (a/U)^2 and U > a at every N.  But the surface's size U = 1.05 R_reach(N), and the depth where
     H-FAR-MODEL must hold (X9 (a)), both grow with the README.  Checked at N = 1e3, the example, 1e30.  Control: the
     owner's parabola needs a ratio W/U that itself grows with N.
  X6 THROUGH THE WRITE (deduced, conditional on W2 and on causal propagation -- the domain-of-dependence step,
     standard-not-READ; the cones STRUCTURAL; NOT PROVED).  The model's metric gives every causal vector
     du^2 + dw^2 <= dt^2 (checked from metric("model")); T_E keeps coordinate distance >= U from the origin (W >= U).
     With U = 1.05 R_reach, R_reach = R_core + 2T (R_core = 2, G3's r0, fixed by 162), no signal from the corridor or
     from the README's own matter (inside R_core + T when the write began, o3_write W3, and carried in, 163) reaches
     T_E before the closing (under 179, U must also cover the corridor's depth w_c, which is OPEN: H-FAR-MODEL (v)).
     That the region outside then keeps its prior static state needs global hyperbolicity
     (W2, non-green) and a causally propagating evolution; CGS Theorem 3.1's premises include "the null energy
     condition (NEC)" (READ, CGS pp.3-4, in bulk/CENSOR5D.md, which records Theorem 3.5, p.5, "on the same premises"),
     and the model's own column violates the NEC pointwise (X9 (c)).  Any finite hold works
     (X2 is free of U); E2's closing (DERIVED) and 158 (2) make it finite.
  X7 AFTER THE CLOSING (deduced, an estimate, NON-GREEN; Raychaudhuri and the area law standard-not-READ).  4D form:
     focusing ~ 2 E_rad/U^2, E_rad <= (5/4) m (ledger.py E4, computed on eq. (17)), against the floor U/W^2: margin
     U/(2.5 k^2).  5D form, for ell >> U (deduced, order of magnitude; G5 ~ G4 ell standard-not-READ): focusing
     ~ 8 pi G5 E_rad/(2 pi^2 U^3), margin ~ pi U^2/(15 c), below 1 for c above ~ pi U^2/15.  So the after-closing step
     brings back a condition on ell; "no condition on ell" holds only through the closing.
  X8 A FAR FIELD AT T_E (computed in the board's configuration -- the throat on our plane -- NOT in the configuration
     179 asks; deduced).  The lapse cancels from theta+ exactly; with a conformal far field of strength gamma m
     (eq. (17)'s gamma = 5/4, bulk/kscale.py) centred on the plane, the sufficient condition is k^2 (1 - 3 gamma m/U) > 3
     and the exact tip condition as ell -> 0 is k^2 - 3 - 3 gamma m/(k U + 2 gamma m) > 0.  So 1.74 suffices only for
     U above a threshold (small READMEs need a larger k); E1 traps exactly sqrt(3) at small c; E2 is scan evidence only
     at the seven c tested.  By X6 a field that arises at the opening (160, 162) cannot reach T_E before the closing,
     so X8 bears only on a far field present before the opening -- such as the README's own energy on our plane
     before it is carried in (163, 184; deduced, its bulk form not computed).
  X9 H-FAR-MODEL IS NOT DERIVED HERE, AND SEATED (Z) EXCLUDES ITS COLUMN (computed + STRUCTURAL + deduced).  (a) In the
     model's topology (the column at every depth), every T enclosing the reach crosses the join column (u = 0) at
     depth >= R_reach -- the tip.  (b) b4_static's banked bulk (built on eq. (17) as the plane's metric, F1) reaches
     r <= 32, y <= 16; the board's other computed bulks (model B's throat column on eq. (17), model C's two-sided
     bridge with flat planes, B4d stages 5-7) do not supply this column either (READ from lemmas/BULK-BALANCE.md and
     warptheorem.py's B4d row).  (c) For EVERY depth profile A(w) of the column's conformal radius (the constant a
     included), the full 5D Ricci gives R(k,k) = -2 A^2/(u^2 + A^2)^2 along k = d_t + d_u, an affine null geodesic of
     both g0 and g; Raychaudhuri's identity holds exactly with the cross-section's expansion 2u/rho^2, so the net
     along each radial light ray is -pi/A (computed) -- never zero.  Under Einstein's equations that is net negative
     null energy along each such ray, against seated (Z), and negative null energy at every point, against CGS's NEC
     premise (deduced).  So no column in the family the tip formula covers is admissible; a join consistent with (Z)
     is not a static traversable column of this family, and what T's tip does then is OPEN.  (d) Tip formula for any
     A(w): ((ell + W)/ell)(W/U^2 + 2 A'(W)/A(W)) - 3/ell (computed, exact); power-law columns A = a (z/ell)^p move the
     threshold to k^2 >= 3 - 2p.  These are statements about excluded columns.  (e) Against (G), 139 (1) and 166
     (STRUCTURAL, checked): the model's w = 0 slice has S^2 radius^2 u^2 + a^2, least at u = 0 with a^2 > 0 -- a throat
     ON our plane, against seated (G) as worded; the warp's jump across the plane, d_w ln Om at w = 0+, is -1/ell on
     both sheets u > 0 and u < 0 -- one positive tension for both positions, where 139 (1) has position 2's plane
     negative; and there is one plane, not the two of 166 with the bulk between them.
  X10 UNDER 184 (computed; deduced, an estimate).  H-FAR-MODEL's plane is matter-free.  Our plane's MEAN energy
     density over its RS tension is rho_crit c^2/lambda_RS = (H0 ell/c)^2/2 exactly, 2.65e-61 at ell = 1e-4 m.  That is
     a mean, not a bound: local matter up to nuclear density (address.RHO_NUCLEAR = 2.676e17 kg/m^3, DERIVED-FROM-ORDER;
     f1_audit.py bounds a plane's matter the same generous way, 2.3e17, under the board's H-OWN-MATTER-ONLY) gives
     ~8e-18 -- still negligible.
  X11 NO COLUMN (computed: z3, and a scan in the board's test extension; deduced).  With a = 0 our plane is throat-free
     and the model is Poincare AdS5 with the RS plane; then Q = K/(1 + (K - 1) x) + 2K >= 3 for K >= 1, so EVERY
     W >= U is untrapped at every ell.  With a bulk-centred conformal test field (E1 centred at depth w_c = U/2 inside
     T_E), k = sqrt(3) stays untrapped at both README sizes tested while the round surface (k = 1) is trapped at small
     c; a deduced sufficient condition for that field at every ell (both parts: 2/U >= 3 gamma m/d_min^2 and
     2(K - 1)/(K U) >= 3 gamma m/d_min^2, d_min the least distance from the field's centre to T_E, checked on the grid)
     holds at both sizes.  The sqrt(3) threshold is the column's alone.  Whether T in 179's configuration must cross a
     join or can enclose it (B4a's topology) is OPEN; a negative-tension position-2 plane (139 (1)) and the two
     planes of 166 are not computed here.

WHAT B4c EARNS.
  Within H-FAR-MODEL: X1-X5 PROVED (exact; z3) at every ell and every N for W >= sqrt(3) U; X6 deduced, conditional on W2
  and causal propagation; after the closing an ESTIMATE (non-green), needing c <~ pi U^2/15 in its 5D form.
  Status: READING.  NOT GREEN.  It rests on H-FAR-MODEL, whose join column -- in every depth profile the instrument
  covers -- seated (Z) excludes; and on W2, causal propagation and the after-closing estimate (and on
  H-FAR-FIELD-EXTENSION for the far-field clause).  On this model B4c cannot turn green: a join consistent with (Z) has
  to replace the column first, and that join is OPEN.

NOT HERE  W2 (the bulk regular, B4b/B4d); B4a's topology (b4_global.py); the cypher audit (192, 196) -- the question
"is H-FAR-MODEL derivable, and is its column consistent with (Z)" has not been put to the cypher.
Imports lemmas/b4_global.py, lemmas/o3_write.py, lemmas/ledger.py, bulk/kscale.py, ../cosmo.py and ../address.py by
path; reads the bank lemmas/b4_static.json (data).  Stdlib + sympy + mpmath + z3 (pip install z3-solver).
"""
import argparse
import contextlib
import importlib.util
import io
import json
import math
import os
import sys
import time

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
A_THROAT = 2                      # b4_global's a: the throat radius r0 = 2m (G3), corridor units
R_CORE = 2                        # B4D-STAGE2's convention: the core radius 2m
COVER = mp.mpf("1.05")            # U = 1.05 R_reach (the checker's cover)
C_SCAN = ("1e-6", "1e-3", "0.11", "1", "27.07", "4e5", "1e9")
LABELS = ("computed", "READ", "deduced", "STRUCTURAL", "standard-not-READ", "OPEN")
GREEN_STATUSES = ("PROVED", "DERIVED", "AXIOM")
mp.mp.dps = 30


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


_OWN = {}
_OWN_PATH = {"b4_global": os.path.join(HERE, "b4_global.py"), "o3_write": os.path.join(HERE, "o3_write.py"),
             "ledger": os.path.join(HERE, "ledger.py"), "kscale": os.path.join(D68, "bulk", "kscale.py"),
             "cosmo": os.path.join(WD, "cosmo.py"), "address": os.path.join(WD, "address.py")}


def owner(name):
    if name not in _OWN:
        _OWN[name] = _load(_OWN_PATH[name], "b4cfar_" + name)
    return _OWN[name]


# ---- symbols, metrics, the general level-set expansion ----------------------------------------------------------
u = sp.Symbol("u", real=True)
w = sp.Symbol("w", positive=True)                        # the side w > 0; the mirror w -> -w covers the other
ell, a, U, W, m, gam, R = sp.symbols("ell a U W m gamma R", positive=True)   # same names/assumptions as b4_global's
p = sp.Symbol("p", real=True)
tau = sp.Symbol("tau", positive=True)
wc = sp.Symbol("w_c", positive=True)
ALPHA = sp.Symbol("alpha")


def theta_plus(F, metric, mut=None):
    """theta+ of the level set of F (outward = grad F), static slice, b4_global's recipe generalized: div n over
    sqrt|g| (the lapse included) minus a_n.  metric = (lapse, g_uu, g_ww, g_OmegaOmega), all diagonal."""
    lapse, guu, gww, goo = metric
    sqrtg = (1 if mut == "lapse_dropped" else lapse) * sp.sqrt(guu * gww) * (sp.sqrt(goo) if mut == "s2_power" else goo)
    Fu, Fw = sp.diff(F, u), sp.diff(F, w)
    nrm = sp.sqrt(Fu**2 / guu + Fw**2 / gww)
    sgn = -1 if mut == "normal_in" else 1
    nu, nw = sgn * Fu / guu / nrm, sgn * Fw / gww / nrm
    div = (sp.diff(sqrtg * nu, u) + sp.diff(sqrtg * nw, w)) / sqrtg
    an = nu * sp.diff(sp.log(lapse), u) + nw * sp.diff(sp.log(lapse), w)
    return div + an if mut == "an_sign" else div - an


def metric(kind="model", mut=None):
    z = ell + w
    Om = z / ell if mut == "antiwarp" else ell / z
    rho2 = u**2 + a**2
    if kind == "model":                                   # H-FAR-MODEL
        s2 = -1 if mut == "s2_negative" else 1
        return (Om, Om**2, Om**2, s2 * Om**2 * rho2)
    if kind == "column":                                  # the column's conformal radius a (z/ell)^p
        pp = -p if mut == "p_sign" else p
        return (Om, Om**2, Om**2, Om**2 * (u**2 + a**2 * (z / ell)**(2 * pp)))
    if kind == "column_general":
        A = sp.Function("A")(w)
        return (Om, Om**2, Om**2, Om**2 * (u**2 + A**2))
    if kind == "E1c":                                     # X11: a conformal test field centred at depth w_c
        fc = 1 + 2 * gam * m / sp.sqrt(u**2 + (w - wc)**2)
        return (Om, Om**2 * fc, Om**2 * fc, Om**2 * fc * rho2)
    d = sp.sqrt(u**2 + w**2)
    f = 1 + 2 * gam * m / d                               # eq. (17)'s spatial far field, isotropic form, O(m)
    if kind == "E1":
        return (Om, Om**2 * f, Om**2 * f, Om**2 * f * rho2)
    if kind == "E1_lapse":
        return (Om * sp.sqrt(1 - 2 * m / d), Om**2 * f, Om**2 * f, Om**2 * f * rho2)
    if kind == "E2":
        return (Om, Om**2 * f, Om**2, Om**2 * rho2)
    raise ValueError(kind)


ELLIPSE = (u / U)**2 + (w / W)**2
PARABOLA = (u / U)**2 + w / W                             # b4_global's tipped family
CIRCLE = (u**2 + w**2) / R**2
ON_ELLIPSE = {u: U * (1 - tau**2) / (1 + tau**2), w: W * 2 * tau / (1 + tau**2)}
ON_CIRCLE = {u: R * (1 - tau**2) / (1 + tau**2), w: R * 2 * tau / (1 + tau**2)}


def desqrt(e):
    """sqrt((x)^2 y) with x > 0 is x sqrt(y): factor every half-integer power's base so sympy can see it."""
    return e.replace(lambda x: x.is_Pow and x.exp.is_Rational and x.exp.q == 2,
                     lambda x: sp.Pow(sp.factor(x.base), x.exp))


def is_zero(e):
    return sp.simplify(desqrt(sp.together(e))) == 0


def closed_form(mut=None):
    """X1's closed form on T_E, in (u, w)."""
    k3 = 2 if mut == "warp_count" else 3
    s2 = 1 if mut == "s2_coeff" else 2
    D = sp.sqrt(u**2 / U**4 + w**2 / W**4)
    P = 1 / (U**2 * W**2 * D**2) + s2 * u**2 / (U**2 * (u**2 + a**2))
    return ((ell + w) * P - k3 * w / W**2) / (ell * D), P, D


def owner_round_uw():
    fb = owner("b4_global").far_boundary()
    th = fb["theta"].subs({sp.cos(ALPHA): u / R, sp.sin(ALPHA): w / R})
    assert ALPHA not in th.free_symbols
    return th


def q_poly(K, x, b):
    """(Q - 3)(1 + (K - 1) x)(x + b): one source for both the sympy and the z3 forms (encoding-drift guard)."""
    return K * (x + b) + 2 * K * x * (1 + (K - 1) * x) - 3 * (1 + (K - 1) * x) * (x + b)


def q0_poly(K, x):
    """(Q - 3)(1 + (K - 1) x) at a = 0 (no column), Q = K/(1 + (K - 1) x) + 2K: one source for sympy and z3."""
    return K + (2 * K - 3) * (1 + (K - 1) * x)


def ricci5(g, X):
    """Ricci tensor of a diagonal 5D metric g in coordinates X (sympy, exact); returns ric(j, k)."""
    gi = g.inv()
    n = 5
    Gam = [[[sp.simplify(sum(gi[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
                             for l in range(n)) / 2) for k in range(n)] for j in range(n)] for i in range(n)]

    def ric(j, k):
        return sp.simplify(sum(sp.diff(Gam[i][j][k], X[i]) for i in range(n))
                           - sum(sp.diff(Gam[i][j][i], X[k]) for i in range(n))
                           + sum(Gam[i][i][l] * Gam[l][j][k] for i in range(n) for l in range(n))
                           - sum(Gam[i][k][l] * Gam[l][j][i] for i in range(n) for l in range(n)))
    return ric, Gam


# ---- numerics ---------------------------------------------------------------------------------------------------
_LAM = {}


def lam(family, kind, mut=None, extra=()):
    key = (family, kind, mut, extra)
    if key not in _LAM:
        F = {"ellipse": ELLIPSE, "parabola": PARABOLA}[family]
        _LAM[key] = sp.lambdify((u, w, ell, a, U, W) + tuple(extra), theta_plus(F, metric(kind, mut)), "mpmath")
    return _LAM[key]


def tgrid(n):
    pts = [mp.mpf(0)]
    for j in range(1, n + 1):
        pts.append(mp.pi / 2 * j / n)
        e = mp.power(10, -12 + 12 * mp.mpf(j) / n)
        pts.append(mp.pi / 2 * e)
        pts.append(mp.pi / 2 * (1 - e))
    return pts


def surface_min(fn, family, c, Uv, Wv, args=(), n=200, aval=A_THROAT):
    """min theta+ over the quadrant of the surface (u, w >= 0; the other three by the symmetries u -> -u, w -> -w)."""
    best, at = mp.inf, None
    for t in tgrid(n):
        if family == "ellipse":
            uv, wv = Uv * mp.cos(t), Wv * mp.sin(t)
        else:
            uv, wv = Uv * mp.cos(t), Wv * (1 - mp.cos(t)**2)
        v = fn(uv, wv, mp.mpf(c), aval, Uv, Wv, *args)
        if v < best:
            best, at = v, t
    return best, at


def reach(N):
    """T = o3_write's least write in clocks (Z = 108.75), clamped at 0.  R_reach = R_core + 2T: the README lay inside
    radius R_core + T when the write began (o3_write W3) and its influence, like the core's, spreads at most T further
    by the closing (deduced, the model's cones).  U = 1.05 R_reach."""
    ow = owner("o3_write")
    T = max(0.0, ow._num(ow.t_min(3), n=N))
    Rr = mp.mpf(R_CORE) + 2 * mp.mpf(T)
    return T, Rr, COVER * Rr


def example_N():
    return owner("o3_write").EXAMPLE_N


def n_for_U(Ut):
    """The README size N (bits) at which reach(N)'s U equals Ut (bisection in log N)."""
    lo, hi = mp.mpf(1), mp.mpf(60)                       # log10 N
    for _ in range(80):
        mid = (lo + hi) / 2
        if reach(float(mp.power(10, mid)))[2] < Ut:
            lo = mid
        else:
            hi = mid
    return float(mp.power(10, hi))


# ---- checks: each returns (ok, detail); mut=None is the true check ----------------------------------------------
def check_C1(mut=None):
    """X0 owner agreement, round T: the general code = b4_global.far_boundary() exactly."""
    th = theta_plus(CIRCLE, metric("model"), mut)
    own = owner_round_uw()
    ok = is_zero((th - own).subs(ON_CIRCLE))
    return ok, {"equal_to_owner_closed_form": ok}


def check_C2(mut=None):
    """X0 owner agreement, tipped parabola at b4_global's S3 point, on the owner's own grid."""
    own_min, own_dist = owner("b4_global").tipped_far_boundary(sp.Rational(11, 100), 24, 2.4e4)
    z = sp.Rational(11, 100) + w
    Om = sp.Rational(11, 100) / z
    F = (u / 24.0)**2 + w / 2.4e4
    g = (Om, Om**2, Om**2, Om**2 * (u**2 + 4))
    f = sp.lambdify((u, w), theta_plus(F, g, mut), "math")
    n = 4000
    pts = [(24.0 * math.cos(math.pi / 2 * j / n), 2.4e4 * (1 - math.cos(math.pi / 2 * j / n)**2)) for j in range(1, n)]
    mine = min(f(x, y) for x, y in pts)
    rel = abs(mine - float(own_min)) / abs(float(own_min))
    return rel < 1e-12, {"owner_min": float(own_min), "this_min": mine, "rel_diff": rel}


def check_C3(mut=None):
    """X1: the closed form on T_E (exact), its tip, W = U against the owner's round formula, the square-on foot."""
    th = theta_plus(ELLIPSE, metric("model"))
    cf, _, _ = closed_form(mut)
    ident = is_zero((th - cf).subs(ON_ELLIPSE))
    tip = sp.simplify(cf.subs(u, 0).subs(w, W))
    tip_ok = sp.simplify(tip - (W**2 + W * ell - 3 * U**2) / (U**2 * ell)) == 0
    round_ok = is_zero((cf.subs(W, U) - owner_round_uw().subs(R, U)).subs({u: U * (1 - tau**2) / (1 + tau**2),
                                                                          w: U * 2 * tau / (1 + tau**2)}))
    square_on = sp.diff(ELLIPSE, w).subs(w, 0) == 0 and sp.diff(PARABOLA, w).subs(w, 0) != 0
    ok = ident and tip_ok and round_ok and square_on
    return ok, {"identity_on_T_E": ident, "tip": str(tip), "tip_is_checker_form": tip_ok,
                "W=U_is_owner_round": round_ok, "meets_plane_square_on (parabola does not)": square_on}


def check_C4(mut=None):
    """X2: Q >= 3 under K >= 3, (K - 1) b <= 2 (z3, unsat of the negation), with guards; X3's sharpness."""
    import z3
    K, x, b = z3.Reals("K x b")
    kmin = z3.RealVal("29/10") if mut == "k_below_3" else z3.RealVal(3)
    side = 3 if mut == "side_dropped" else 2
    hyp = [K >= kmin, x >= 0, x <= 1, b > 0, (K - 1) * b <= side]
    s = z3.Solver()
    s.add(hyp + [q_poly(K, x, b) < 0])
    res = s.check()
    proved = res == z3.unsat
    cex = str(s.model()) if res == z3.sat else None
    sv = z3.Solver()
    sv.add(hyp)
    vacuity_ok = sv.check() == z3.sat
    sd = z3.Solver()
    sd.add([K >= 1, x >= 0, x <= 1, x + (1 - x) / K > 1])
    d_le = sd.check() == z3.unsat                         # U^2 D^2 = x + (1 - x)/K <= 1, i.e. D <= 1/U
    Ks, xs, bs = sp.symbols("K x b", positive=True)
    Q = Ks / (1 + (Ks - 1) * xs) + 2 * Ks * xs / (xs + bs)
    drift_ok = sp.expand((Q - 3) * (1 + (Ks - 1) * xs) * (xs + bs) - q_poly(Ks, xs, bs)) == 0 or \
        sp.simplify((Q - 3) * (1 + (Ks - 1) * xs) * (xs + bs) - q_poly(Ks, xs, bs)) == 0
    _, P, D = closed_form()
    q_on = sp.simplify((W**2 * P).subs(w, W * sp.sqrt(1 - u**2 / U**2)) -
                       Q.subs({Ks: W**2 / U**2, xs: u**2 / U**2, bs: a**2 / U**2}))
    q_ok = q_on == 0
    cf, _, _ = closed_form()
    G = (ell + w) * P - 3 * w / W**2
    g_ok = sp.simplify(G - ell * P - (w / W**2) * (W**2 * P - 3)) == 0 and sp.simplify(cf - G / (ell * D)) == 0
    qdiff = sp.factor(sp.together(Q - Ks))
    qd_ok = sp.simplify(qdiff - Ks * xs * (2 + (Ks - 1) * (xs - bs)) / ((xs + bs) * (1 + (Ks - 1) * xs))) == 0
    tip_num = W**2 + W * ell - 3 * U**2
    ell_star = sp.solve(sp.Eq(tip_num, 0), ell)[0]
    sharp = sp.simplify(ell_star - (3 * U**2 - W**2) / W) == 0
    ok = proved and vacuity_ok and d_le and drift_ok and q_ok and g_ok and qd_ok and sharp
    return ok, {"z3_Q_ge_3": proved, "counterexample": cex, "vacuity_guard": vacuity_ok, "D_le_1/U": d_le,
                "encoding_guard_poly": drift_ok, "encoding_guard_Q_is_W2P": q_ok, "G - ell P = (w/W^2)(Q - 3)": g_ok,
                "Q - K identity": qd_ok, "switch ell* = (3U^2 - W^2)/W": sharp}


def check_C5(mut=None):
    """X4: the scan at the example README with the general code; floors and the 1.70 switch."""
    _, Rr, Uv = reach(example_N())
    fn = lam("ellipse", "model", "antiwarp" if mut == "antiwarp" else None)
    rows, ok = {}, True
    for kname, kv in (("1.70", mp.mpf("1.70")), ("sqrt3", mp.sqrt(3)), ("1.74", mp.mpf("1.74")), ("2", mp.mpf(2))):
        Wv = kv * Uv
        floor = (3 / Uv) if mut == "floor_3_over_U" else Uv / Wv**2
        ell_star = Uv * (3 - kv**2) / kv
        for c in C_SCAN:
            v, at = surface_min(fn, "ellipse", c, Uv, Wv)
            rows["k=%s c=%s" % (kname, c)] = float(v)
            if kname == "1.70":
                ok = ok and ((v < 0) == (mp.mpf(c) < ell_star))
            else:
                ok = ok and v > 0 and v >= floor * (1 - mp.mpf("1e-12"))
    return ok, {"U": float(Uv), "R_reach": float(Rr), "switch_1.70": float(Uv * (3 - mp.mpf("1.70")**2) / mp.mpf("1.70")),
                "floor U/W^2 at sqrt3": float(1 / (3 * Uv)), "min_theta": rows}


def check_C6(mut=None):
    """X5: the shape free of N.  The theorem's hypotheses at three N; scans; the parabola's N-growing root as the
    contrast; the size U grows with N."""
    family = "parabola" if mut == "parabola" else "ellipse"
    fn = lam(family, "model")
    out, ok = {}, True
    sizes = []
    for N in (1e3, example_N(), 1e30):
        T, Rr, Uv = reach(N)
        sizes.append(Uv)
        side_ok = (3 - 1) * (A_THROAT / Uv)**2 <= 2 and (mp.mpf("1.79")**2 - 1) * (A_THROAT / Uv)**2 <= 2
        good = [surface_min(fn, family, c, Uv, mp.mpf("1.74") * Uv, n=150)[0] for c in ("1e-6", "1", "1e9")]
        bad = surface_min(fn, family, "1e-6", Uv, mp.mpf("1.70") * Uv, n=150)[0]
        ok = ok and side_ok and all(g > 0 for g in good) and bad < 0
        out["N=%.3g" % N] = {"T": T, "U": float(Uv), "side_condition": bool(side_ok),
                             "1.74 min (c=1e-6,1,1e9)": [float(g) for g in good], "1.70 min c=1e-6": float(bad)}
    size_grows = sizes[0] < sizes[1] < sizes[2]
    th = theta_plus(PARABOLA, metric("model"))
    foot = sp.factor(sp.limit(th.subs(u, U), w, 0))       # theta+ where the parabola meets the plane (exact)
    footf = sp.lambdify((W, U, ell, a), foot, "mpmath")
    roots = {}
    for N in (1e3, example_N(), 1e30):
        _, _, Uv = reach(N)
        g = lambda y: footf(y * Uv, Uv, 1, A_THROAT)       # c = 1; y = W/U
        hi = 10 * Uv
        lo = hi
        while g(lo) > 0 and lo > mp.mpf("1e-3"):          # walk down to the last trapped ratio
            lo = lo / 2
        for _ in range(200):                               # bisect the sign change (the largest root)
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if g(mid) <= 0 else (lo, mid)
        roots["N=%.3g" % N] = float(hi)
    grows = roots["N=1e+03"] < roots["N=%.3g" % example_N()] < roots["N=1e+30"]
    ok = ok and grows and size_grows
    out["parabola foot, needed W/U at c = 1"] = roots
    out["parabola needed W/U grows with N"] = grows
    out["the size U grows with N (the shape does not)"] = size_grows
    return ok, out


def check_C7(mut=None):
    """X6: the model's causal cones from metric("model") (STRUCTURAL), T_E's least distance on the grid, and the reach
    (core and the README's initial support) at the example README."""
    lapse, guu, gww, goo = metric("model", "s2_negative" if mut == "s2_negative" else None)
    # g(v, v) = lapse^2 (-vt^2 + vu^2 + vw^2) + goo (vth^2 + sin^2 vph^2) when guu = gww = lapse^2: causal => du^2 + dw^2
    # <= dt^2 exactly when the S^2 coefficient goo/lapse^2 is non-negative (a sum of squares).
    s2c = sp.simplify(goo / lapse**2)
    cone_ok = (sp.simplify(guu - lapse**2) == 0 and sp.simplify(gww - lapse**2) == 0 and s2c.is_nonnegative is True)
    k_ratio = mp.mpf("0.9") if mut == "oblate" else mp.sqrt(3)
    cover = mp.mpf("0.95") if mut == "short" else COVER
    T, Rr, _ = reach(example_N())
    r_for_U = (mp.mpf(R_CORE) + mp.mpf(T)) if mut == "inflow_omitted" else Rr
    Uv = cover * r_for_U
    Wv = k_ratio * Uv
    d2min = min((Uv * mp.cos(t))**2 + (Wv * mp.sin(t))**2 for t in tgrid(200))
    least_ok = d2min >= Uv**2 * (1 - mp.mpf("1e-25"))     # T_E's least distance from the origin is U
    least = mp.sqrt(d2min)
    margin = least - Rr
    ok = cone_ok and least_ok and margin > 0
    return ok, {"guu = gww = lapse^2 and S^2 coefficient >= 0 (from metric('model'))": cone_ok,
                "S^2 coefficient": str(s2c), "least distance of T_E is U": bool(least_ok),
                "R_reach = R_core + 2T": float(Rr), "U": float(Uv), "least distance of T": float(least),
                "clocks to spare at the closing": float(margin)}


def check_C8(mut=None):
    """X7: the radiation step's margin, 4D form with X2's exact floor and with the computed floor; the 5D form's
    condition on ell (an order of magnitude)."""
    e4 = owner("ledger").e4()
    mm = sp.Symbol("m", positive=True)
    far = sp.simplify(e4["far"] / mm)                     # 5/4 (E4's total, in units of m)
    e_rad = mp.mpf(float(far)) * (mp.mpf("1e5") if mut == "e_rad_big" else 1)
    T, Rr, Uv = reach(example_N())
    k = mp.sqrt(3)
    Wv = k * Uv
    floor_exact = Uv / Wv**2
    _, P, D = closed_form()
    pd = sp.lambdify((u, w, a, U, W), P / D, "mpmath")
    floor_comp = min(pd(Uv * mp.cos(t), Wv * mp.sin(t), A_THROAT, Uv, Wv) for t in tgrid(200))
    dth = 2 * e_rad / Uv**2
    m_exact, m_comp = floor_exact / dth, floor_comp / dth
    ow = owner("o3_write")
    Ns = sp.Symbol("N", positive=True)
    t_needed = (float(2.5 * k**2) / float(COVER) - R_CORE) / 2          # U = 1.05 (2 + 2T) = 2.5 k^2 at margin 1
    n_star = sp.solve(sp.Eq(ow.t_min(3).subs(ow.Z, ow.Z_HEAD).subs(ow.N, Ns), t_needed), Ns)
    n_star = float(n_star[0]) if n_star else None

    def m5(c):                                           # 5D: focusing 8 pi G5 E/(2 pi^2 U^3), G5 ~ G4 ell = c (m = 1)
        g5 = mp.mpf(1) if mut == "g5_no_ell" else mp.mpf(c)
        return floor_exact / (8 * mp.pi * g5 * e_rad / (2 * mp.pi**2 * Uv**3))
    scaling_ok = abs(m5(1) / m5(10) - 10) < mp.mpf("1e-20")
    c_fail = m5(1)                                       # m5(c) = m5(1)/c, so the 5D margin is 1 at c = m5(1)
    cf_ok = abs(c_fail / (mp.pi * Uv**2 / 15) - 1) < mp.mpf("1e-20")
    ok = (far == sp.Rational(5, 4) and m_exact > 1e4 and m_comp >= m_exact and n_star is not None and n_star < 1e3
          and scaling_ok and cf_ok and 1e9 < c_fail < 1e13)
    return ok, {"E_rad cap (units m, ledger E4)": str(far), "U": float(Uv), "floor exact U/W^2": float(floor_exact),
                "floor computed min P/D": float(floor_comp), "4D margin exact": float(m_exact),
                "4D margin computed": float(m_comp), "N below which the 4D exact-floor margin < 1": n_star,
                "5D margin ~ 1/c": bool(scaling_ok), "5D margin = 1 at c ~ pi U^2/15": float(c_fail),
                "5D margin at c = 1e9": float(m5("1e9"))}


def check_C9(mut=None):
    """X8: a far field at T_E in the board's configuration.  eq. (17)'s far field (kscale), lapse cancellation, the
    conformal-class bound, the exact tip as ell -> 0, the scans, and the small README where 1.74 fails."""
    fp = owner("kscale").fingerprint()
    g_floor = sp.nsimplify(fp["floor"]["gamma"])
    mm = sp.Symbol("m", positive=True)
    coef = sp.simplify(2 * g_floor * fp["M"] / mm)        # Eddington-Robertson g_rr = 1 + 2 gamma M/r (kscale), M = m
    rho_i = sp.Symbol("rho", positive=True)
    radial = sp.series((1 + 2 * g_floor * mm / (rho_i + g_floor * mm)) - (1 + 2 * g_floor * mm / rho_i), mm, 0, 2)
    angular = sp.series((rho_i + g_floor * mm)**2 - rho_i**2 * (1 + 2 * g_floor * mm / rho_i), mm, 0, 2)
    iso_ok = sp.simplify(radial.removeO()) == 0 and sp.simplify(angular.removeO()) == 0
    lapse_ok = is_zero(theta_plus(ELLIPSE, metric("E1_lapse")) - theta_plus(ELLIPSE, metric("E1")))
    d = sp.sqrt(u**2 + w**2)
    f = 1 + 2 * gam * m / d
    Fu, Fw = sp.diff(ELLIPSE, u), sp.diff(ELLIPSE, w)
    nn = sp.sqrt(Fu**2 + Fw**2)
    n0grad = (Fu * sp.diff(sp.log(sp.sqrt(f)), u) + Fw * sp.diff(sp.log(sp.sqrt(f)), w)) / nn
    Om = ell / (ell + w)
    conf_ok = is_zero(sp.sqrt(f) * theta_plus(ELLIPSE, metric("E1")) - theta_plus(ELLIPSE, metric("model"))
                      - 3 * n0grad / Om)
    delta_ok = is_zero(3 * n0grad + 3 * gam * m * ((u * Fu + w * Fw) / (d * nn)) / (d**2 + 2 * gam * m * d))
    # the exact tip as ell -> 0 (E1): ell theta+(tip) -> positive factor x (k^2 - 3 - 3 gamma m/(k U + 2 gamma m))
    ks = sp.Symbol("k", positive=True)
    tip = sp.simplify(theta_plus(ELLIPSE, metric("E1")).subs(u, 0).subs(w, W))
    lead = sp.simplify(sp.limit(tip * ell, ell, 0).subs(W, ks * U))
    tipform = ks**2 - 3 - 3 * gam * m / (ks * U + 2 * gam * m)
    ratio = sp.simplify(lead / tipform)
    tiplim_ok = sp.simplify(ratio - sp.sqrt(ks * U) / sp.sqrt(ks * U + 2 * gam * m)) == 0
    u_crit = mp.findroot(lambda Uv: mp.mpf("1.74")**2 - 3 - 3 * mp.mpf(5) / 4 / (mp.mpf("1.74") * Uv + mp.mpf(5) / 2),
                         70)
    n_crit = n_for_U(u_crit)
    _, Rr, Uv = reach(example_N())
    gv = mp.mpf(g_floor.p) / g_floor.q
    k_star = mp.sqrt(3 / (1 - 3 * gv / Uv))
    lam_max = (mp.mpf("1.74")**2 - 3) * Uv / (3 * gv * mp.mpf("1.74")**2)
    mval = {"field_x1e4": mp.mpf("1e4"), "no_field": mp.mpf(0)}.get(mut, mp.mpf(1))
    scans = {}
    good = True
    for kind in ("E1", "E2"):
        fn = lam("ellipse", kind, None, (m, gam))
        for c in C_SCAN:
            v, _ = surface_min(fn, "ellipse", c, Uv, mp.mpf("1.74") * Uv, (mval, gv), n=150)
            scans["%s k=1.74 c=%s" % (kind, c)] = float(v)
            good = good and v > 0
    fn = lam("ellipse", "E1", None, (m, gam))
    at_sqrt3, _ = surface_min(fn, "ellipse", "1e-6", Uv, mp.sqrt(3) * Uv, (mval, gv), n=150)
    scans["E1 k=sqrt3 c=1e-6"] = float(at_sqrt3)
    _, _, U1 = reach(1e3)                                 # a small README: 1.74 must fail at small c
    v_small, _ = surface_min(fn, "ellipse", "1e-6", U1, mp.mpf("1.74") * U1, (mval, gv), n=150)
    k_star_small = mp.sqrt(3 / (1 - 3 * gv / U1))
    scans["E1 k=1.74 c=1e-6 at N=1e3"] = float(v_small)
    small_ok = v_small < 0 and k_star_small > mp.mpf("1.74") and U1 < u_crit < Uv
    ok = (g_floor == sp.Rational(5, 4) and coef == 2 * g_floor and iso_ok and lapse_ok and conf_ok and delta_ok
          and tiplim_ok and mp.mpf("1.74") > k_star and lam_max > 100 and good and at_sqrt3 < 0 and small_ok)
    return ok, {"gamma at r0 = 2m (kscale)": str(g_floor), "eq. (17) g_rr = 1 + coef m/r, coef": str(coef),
                "isotropic psi^4 = 1 + 2 gamma m/rho with r = rho + gamma m, to O(m)": iso_ok,
                "lapse cancels from theta+": lapse_ok, "conformal identity": conf_ok, "delta closed form": delta_ok,
                "tip as ell -> 0 = positive x (k^2 - 3 - 3 gamma m/(k U + 2 gamma m))": tiplim_ok,
                "U above which 1.74 holds at the tip (gamma = 5/4)": float(u_crit),
                "N (bits) at that U": n_crit, "k* = sqrt(3/(1 - 3 gamma m/U)) at the example": float(k_star),
                "k* at N = 1e3": float(k_star_small), "U at N = 1e3": float(U1),
                "largest field multiple 1.74 survives at the example (bound)": float(lam_max), "scans": scans}


def model_vs_rulings(mut=None):
    """X9 (e), STRUCTURAL: what H-FAR-MODEL puts on our plane, read off metric('model').  (G): the w = 0 slice's S^2
    radius^2 is least at u = 0 with value a^2 > 0 -- a throat ON the plane.  139 (1): the warp's jump d_w ln Om at
    w = 0+ is the same, -1/ell, on position 1's sheet (u > 0) and position 2's (u < 0) -- one positive tension."""
    lapse, guu, gww, goo = metric("model")
    if mut == "a_zero":
        goo = goo.subs(a, 0)
    plane = sp.simplify(goo.subs(w, 0))
    throat = (sp.diff(plane, u).subs(u, 0) == 0 and sp.diff(plane, u, 2).subs(u, 0).is_positive is True
              and plane.subs(u, 0).is_positive is True)

    def om_sheet(sheet):                                  # the model's warp is u-independent: one plane for both sheets
        if mut == "p2_negative" and sheet < 0:            # position 2's sheet on a negative-tension plane (139 (1))
            return ell / (ell - w)
        return lapse
    jumps = [sp.simplify(sp.diff(sp.log(om_sheet(sg)), w).subs(w, 0)) for sg in (1, -1)]
    one_tension = all(sp.simplify(j + 1 / ell) == 0 for j in jumps)
    return throat and one_tension, {"plane's S^2 radius^2": str(plane), "throat on our plane (against (G))": throat,
                                    "warp jump d_w ln Om at w=0+, sheets u>0, u<0": [str(j) for j in jumps],
                                    "one positive tension on both sheets (against 139 (1))": one_tension}


def check_C10(mut=None):
    """X9: the model's own 5D Ricci (constant a), the general column A(w): R(k,k), the affine geodesic, Raychaudhuri's
    identity and the net per ray; the tip formulas; the power-law columns; the crossing depth against the bank; and
    (e) the model against (G) and 139 (1), STRUCTURAL."""
    mvr_ok, mvr = model_vs_rulings(mut)
    t_, th_, ph_ = sp.symbols("t theta phi")
    X = [t_, u, w, th_, ph_]
    aa = sp.Integer(0) if mut == "a_zero" else a
    z = ell + w
    Om = ell / z
    rho2 = u**2 + aa**2
    g = sp.diag(-Om**2, Om**2, Om**2, Om**2 * rho2, Om**2 * rho2 * sp.sin(th_)**2)
    ric, _ = ricci5(g, X)
    n = 5
    res = [sp.simplify(ric(i, i) + 4 / ell**2 * g[i, i]) for i in range(n)]
    off = sp.simplify(ric(1, 2))
    rkk = sp.simplify(ric(0, 0) + ric(1, 1))
    want = -2 * a**2 / (u**2 + a**2)**2
    ricci_ok = (sp.simplify(rkk - want) == 0 and all(sp.simplify(res[i]) == 0 for i in (0, 2, 3, 4))
                and sp.simplify(res[1] - want) == 0 and off == 0)
    ads_ok = all(sp.simplify(x.subs(a, 0)) == 0 for x in res)
    ray = sp.integrate(want, (u, -sp.oo, sp.oo))
    ray_ok = sp.simplify(ray + sp.pi / a) == 0
    # the general profile A(w), physical metric g and its conformal g0
    A = sp.Function("A")
    Aw = A(w)
    rhoA = u**2 + Aw**2
    gA = sp.diag(-Om**2, Om**2, Om**2, Om**2 * rhoA, Om**2 * rhoA * sp.sin(th_)**2)
    ricA, GamA = ricci5(gA, X)
    rkkA = sp.simplify(ricA(0, 0) + 2 * ricA(0, 1) + ricA(1, 1))
    wantA = (2 if mut == "general_sign" else -2) * Aw**2 / rhoA**2
    genA_ok = sp.simplify(rkkA - wantA) == 0
    kv = [1, 1, 0, 0, 0]
    geod_ok = all(sp.simplify(sum(GamA[i][j][l] * kv[j] * kv[l] for j in range(n) for l in range(n))) == 0
                  for i in range(n))                     # k = d_t + d_u is an affine null geodesic of g
    g0 = sp.diag(-1, 1, 1, rhoA, rhoA * sp.sin(th_)**2)
    ric0, _ = ricci5(g0, X)
    rkk0 = sp.simplify(ric0(0, 0) + 2 * ric0(0, 1) + ric0(1, 1))
    conf_inv = sp.simplify(rkk0 - rkkA) == 0              # R(k,k) is the same in g0 and g along these rays
    B = [sp.simplify(sp.diff(g0[i, i], u) / (2 * g0[i, i])) for i in (2, 3, 4)]   # expansion tensor of {w, S^2}
    theta_e = sp.simplify(sum(B))
    sigma2 = sp.simplify(sum(x**2 for x in B) - theta_e**2 / 3)
    raych_ok = sp.simplify(sp.diff(theta_e, u) + theta_e**2 / 3 + sigma2 + rkk0) == 0
    A0 = sp.Symbol("A_0", positive=True)
    net = sp.simplify(-sp.integrate((theta_e**2 / 3 + sigma2).subs(Aw, A0), (u, -sp.oo, sp.oo)))
    net_ok = sp.simplify(net + sp.pi / A0) == 0 and sp.simplify(sp.integrate(rkk0.subs(Aw, A0), (u, -sp.oo, sp.oo))
                                                                 - net) == 0
    thA = theta_plus(ELLIPSE, metric("column_general"))
    tip = sp.simplify(sp.simplify(thA.subs(u, 0)).subs(w, W))
    tip_want = ((ell + W) / ell) * (W / U**2 + 2 * sp.Derivative(A(W), W) / A(W)) - 3 / ell
    tipA_ok = sp.simplify(tip - tip_want) == 0
    thp = theta_plus(ELLIPSE, metric("column", "p_sign" if mut == "p_sign" else None))
    tip_p = sp.simplify(sp.simplify(thp.subs(u, 0)).subs(w, W))
    tipp_ok = sp.simplify(tip_p - (((ell + W) / ell) * (W / U**2 + 2 * p / (ell + W)) - 3 / ell)) == 0
    _, Rr, Uv = reach(example_N())
    fnc = lam("ellipse", "column", None, (p,))
    scan = {}
    for pv, kv_, expect in ((-1, mp.sqrt(5), "untrapped"), (-1, mp.mpf(2), "trapped at small c"),
                            (1, mp.sqrt(3), "untrapped"), (1, mp.mpf(1), "reported")):
        vals = [surface_min(fnc, "ellipse", c, Uv, kv_ * Uv, (pv,), n=120)[0] for c in ("1e-6", "1", "1e9")]
        scan["p=%+d k=%.4f" % (pv, float(kv_))] = ([float(v) for v in vals], expect)
    col_ok = (all(v > 0 for v in scan["p=-1 k=2.2361"][0]) and scan["p=-1 k=2.0000"][0][0] < 0
              and all(v > 0 for v in scan["p=+1 k=1.7321"][0]))
    bank = json.load(open(os.path.join(HERE, "b4_static.json")))
    r_max = float(max(sp.Rational(x) for x in bank["r"]))
    y_max = max(len(c_["A"]) for c_ in bank["cols"].values()) * bank["dy"]
    cross_ok = Rr > 1e3 * max(r_max, y_max)
    ok = (ricci_ok and ads_ok and ray_ok and genA_ok and geod_ok and conf_inv and raych_ok and net_ok and tipA_ok
          and tipp_ok and col_ok and cross_ok and mvr_ok)
    return ok, {"R(k,k), k = d_t + d_u (constant a)": str(rkk), "only R_uu departs from AdS5": ricci_ok,
                "a = 0 is AdS5": ads_ok, "net along a radial ray (constant a)": str(ray),
                "R(k,k) for every profile A(w)": str(rkkA), "general-profile R(k,k) = -2A^2/rho^4": genA_ok,
                "k affine null geodesic of g": geod_ok, "R(k,k) same in g0 and g": conf_inv,
                "Raychaudhuri identity, expansion 2u/rho^2": raych_ok, "net per ray = -int(theta^2/3 + sigma^2)":
                str(net), "net per ray = -pi/A, never zero": net_ok,
                "general column tip": str(tip), "general tip formula": tipA_ok, "power-law tip formula": tipp_ok,
                "column scans (excluded columns)": scan, "crossing depth >= R_reach": float(Rr),
                "b4_static bank reaches r <=, y <=": [r_max, y_max], "model against (G), 139 (1)": mvr}


def check_C11(mut=None):
    """X10: the 184 note.  rho_crit c^2/lambda_RS = (H0 ell/c)^2/2 (a mean), and a local bound at nuclear density."""
    ks, co = owner("kscale"), owner("cosmo")
    ellv = sp.Symbol("ell_SI", positive=True)
    H0 = sp.Symbol("H0", positive=True)
    rho_crit = 3 * H0**2 / (8 * sp.pi * ks.G)                         # kg/m^3, with kscale's exact G
    energy = rho_crit if mut == "no_c2" else rho_crit * ks.C**2
    ratio = sp.simplify(energy / ks.tension(ellv))
    ident = sp.simplify(ratio - (H0 * ellv / ks.C)**2 / 2) == 0
    sub = {H0: co.H0(), ellv: sp.Rational(1, 10**4)}
    val = float(ratio.subs(sub))
    rho_nuc = owner("address").RHO_NUCLEAR                            # 2.676e17 kg/m^3, DERIVED-FROM-ORDER
    rho_loc = float(rho_crit.subs(sub)) if mut == "nuc_as_mean" else rho_nuc
    val_nuc = float((rho_loc * ks.C**2 / ks.tension(ellv)).subs(sub))
    ok = ident and val < 1e-60 and val_nuc < 1e-15 and val_nuc > 1e30 * val
    return ok, {"identity (H0 ell/c)^2/2": ident, "mean-density ratio at ell = 1e-4 m": val,
                "rho_crit (kg/m^3)": float(rho_crit.subs(sub)), "nuclear density (address.py)": rho_nuc,
                "nuclear-density ratio at ell = 1e-4 m (a bound)": val_nuc, "H0 (1/s, cosmo.py)": co.H0()}


def check_C12(mut=None):
    """X11: no column (a = 0): Q >= 3 for K >= 1 (z3, guards), so every W >= U is untrapped at every ell; with a
    bulk-centred conformal test field (w_c = U/2), sqrt(3) stays untrapped and the round surface is trapped at small c."""
    import z3
    K, x = z3.Reals("K x")
    kmin = z3.RealVal("9/10") if mut == "k_below_1" else z3.RealVal(1)
    hyp = [K >= kmin, x >= 0, x <= 1]
    s = z3.Solver()
    s.add(hyp + [q0_poly(K, x) < 0])
    res = s.check()
    proved = res == z3.unsat
    cex = str(s.model()) if res == z3.sat else None
    sv = z3.Solver()
    sv.add(hyp)
    vacuity_ok = sv.check() == z3.sat
    Ks, xs = sp.symbols("K x", positive=True)
    Q0 = Ks / (1 + (Ks - 1) * xs) + 2 * Ks
    drift_ok = sp.expand((Q0 - 3) * (1 + (Ks - 1) * xs) - q0_poly(Ks, xs)) == 0 or \
        sp.simplify((Q0 - 3) * (1 + (Ks - 1) * xs) - q0_poly(Ks, xs)) == 0
    _, P, _ = closed_form()
    q_on = sp.simplify((W**2 * P.subs(a, 0)).subs(w, W * sp.sqrt(1 - u**2 / U**2)) -
                       Q0.subs({Ks: W**2 / U**2, xs: u**2 / U**2}))
    q_ok = q_on == 0                                      # Q0 is W^2 P at a = 0 (off the axis; the axis by continuity)
    aval = A_THROAT if mut == "column_restored" else 0
    fn = lam("ellipse", "E1c", None, (m, gam, wc))
    gv = mp.mpf(5) / 4 * (100 if mut == "field_x1e2" else 1)
    scans, ok_scan = {}, True
    for N in (1e3, example_N()):
        _, _, Uv = reach(N)
        Wv, wcv = mp.sqrt(3) * Uv, Uv / 2
        for c in ("1e-6", "1", "1e9"):
            v, _ = surface_min(fn, "ellipse", c, Uv, Wv, (mp.mpf(1), gv, wcv), n=150, aval=aval)
            scans["N=%.3g k=sqrt3 c=%s" % (N, c)] = float(v)
            ok_scan = ok_scan and v > 0
        v1, _ = surface_min(fn, "ellipse", "1e-6", Uv, Uv, (mp.mpf(1), gv, wcv), n=150, aval=aval)
        scans["N=%.3g k=1 c=1e-6 (round, field on)" % N] = float(v1)
        ok_scan = ok_scan and v1 < 0
        # deduced sufficient condition at every ell (the conformal identity, n0.grad d >= -1, f >= 1, D <= 1/U, and at
        # a = 0 P >= 2/U^2 and Q - 3 >= 2(K - 1)): 2/U >= 3 gamma m/d_min^2 (the ell part) and
        # 2(K - 1)/(K U) >= 3 gamma m/d_min^2 (the w/ell part), d_min the least distance from the centre to T_E
        dmin = mp.sqrt(min((Uv * mp.cos(t))**2 + (Wv * mp.sin(t) - wcv)**2 for t in tgrid(200)))
        part_ell = 2 / Uv >= 3 * gv / dmin**2
        part_w = 2 * (3 - 1) / (3 * Uv) >= 3 * gv / dmin**2
        bound = part_ell and part_w and dmin >= (Uv - wcv) * (1 - mp.mpf("1e-25"))
        scans["N=%.3g sufficient bound at sqrt3 (ell part, w part; d_min/U)" % N] = [bool(part_ell), bool(part_w),
                                                                                   float(dmin / Uv)]
        ok_scan = ok_scan and bound
    ok = proved and vacuity_ok and drift_ok and q_ok and ok_scan
    return ok, {"z3: Q >= 3 at a = 0 for K >= 1": proved, "counterexample": cex, "vacuity_guard": vacuity_ok,
                "encoding_guard_poly": drift_ok, "encoding_guard_Q0_is_W2P(a=0)": q_ok, "scans (test extension)": scans}


ALL_LABEL_KEYS = ("X0", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11", "STATUS")

NON_GREEN_INPUTS = [
    "H-FAR-MODEL (the board's reading): the throat on our plane joining both positions' sheets under one "
    "positive-tension warp (against seated (G), 139 (1), 166 as worded); the join column at every depth, crossed by "
    "T's tip at depth >= R_reach; the RS-II warp and a matter-free plane on T; the model's causal structure inside T. "
    "Its column, in every depth profile A(w), is excluded by seated (Z) and violates CGS's NEC premise (X9)",
    "W2 (B4b READING, B4d OPEN): global hyperbolicity, for the step through the write",
    "causal propagation / domain of dependence (standard-not-READ), for the step through the write",
    "the after-closing estimate: Raychaudhuri and the area law (standard-not-READ); in 5D it needs c <~ pi U^2/15",
    "H-FAR-FIELD-EXTENSION (the board's), for the far-field clause (X8) only",
]
GREEN_INPUTS = ["E2 (DERIVED): the closing exists, so the hold is finite",
                "162 (M's, H-FIXED-SIZE): R_core = 2m fixed"]


def rows_from(details):
    d = details
    return [
        {"id": "X0", "label": "computed", "claim": "the general level-set theta+ equals b4_global's far_boundary (exact) "
         "and tipped_far_boundary (owner grid)", "value": [d["C1"], d["C2"]]},
        {"id": "X1", "label": "computed (exact, sympy)", "claim": "theta+ on T_E = ((ell + w) P - 3w/W^2)/(ell D); tip "
         "(W^2 + W ell - 3U^2)/(U^2 ell); W = U is the owner's round formula; square-on at the plane", "value": d["C3"]},
        {"id": "X2", "label": "deduced from X1; computed (z3, guards)", "claim": "within H-FAR-MODEL: W >= sqrt(3) U and "
         "(W^2 - U^2) a^2 <= 2 U^4 give theta+ >= U/W^2 > 0 at every point and every ell", "value": d["C4"]},
        {"id": "X3", "label": "computed (exact)", "claim": "W < sqrt(3) U is trapped at the tip for ell < (3U^2 - "
         "W^2)/W: sqrt(3) is the exact threshold in the model", "value": d["C4"]["switch ell* = (3U^2 - W^2)/W"]},
        {"id": "X4", "label": "computed (30-digit scan, general code)", "claim": "example README: sqrt(3), 1.74, 2 "
         "untrapped above the floor at c = 1e-6..1e9; 1.70 trapped exactly below its switch", "value": d["C5"]},
        {"id": "X5", "label": "deduced; computed", "claim": "the shape ratio is free of N and ell; the surface's size and "
         "the depth where H-FAR-MODEL must hold grow with R_reach(N); the parabola's needed ratio grows with N",
         "value": d["C6"]},
        {"id": "X6", "label": "deduced, conditional on W2 and causal propagation (standard-not-READ); cones STRUCTURAL; "
         "not PROVED", "claim": "through the write: the corridor's and the README's influence stays inside R_core + 2T; "
         "T_E stays at distance >= U; the outside keeps its prior state only on W2 and causal propagation, while the "
         "model's column violates the NEC that CGS Thm 3.5's premises include", "value": d["C7"]},
        {"id": "X7", "label": "deduced, an estimate (non-green); standard-not-READ (Raychaudhuri; G5 ~ G4 ell)",
         "claim": "after the closing: 4D margin U/(2.5 k^2); in the 5D regime margin ~ pi U^2/(15 c), below 1 for c "
         "above ~ pi U^2/15 -- a condition on ell returns after the closing", "value": d["C8"]},
        {"id": "X8", "label": "computed in the board's configuration (throat on our plane), not in 179's; deduced",
         "claim": "a conformal far field gamma m at T_E needs k > k_tip(U); 1.74 only above U ~ 76.6 (small READMEs "
         "need more); E2 at the seven c tested only; bears only on a field present before the opening",
         "value": d["C9"]},
        {"id": "X9", "label": "computed; STRUCTURAL; deduced", "claim": "H-FAR-MODEL is not derived here, and its column "
         "is excluded by seated (Z): for every depth profile A(w), R(k,k) = -2A^2/rho^4 and the net per radial ray is "
         "-pi/A; pointwise against CGS's NEC premise; the tip formula covers only excluded columns; the model puts a "
         "throat on our plane and one positive tension on both sheets (against (G), 139 (1); STRUCTURAL)",
         "value": d["C10"]},
        {"id": "X10", "label": "computed; deduced, an estimate", "claim": "under 184: the mean-density ratio is "
         "(H0 ell/c)^2/2 = 2.65e-61 at 1e-4 m (a mean); a nuclear-density bound gives ~8e-18; negligible",
         "value": d["C11"]},
        {"id": "X11", "label": "computed (z3; scan in the board's test extension); deduced", "claim": "no column "
         "(a = 0): every W >= U untrapped at every ell; with a bulk-centred conformal test field sqrt(3) stays "
         "untrapped (scan; a deduced sufficient bound holds at both sizes), the round surface is trapped at small c: "
         "the sqrt(3) threshold is the column's alone",
         "value": d["C12"]},
        {"id": "STATUS", "label": "deduced", "claim": "B4c: within H-FAR-MODEL, X1-X5 PROVED (exact) at every ell and N "
         "for W >= sqrt(3) U; X6 deduced, conditional on W2 and causal propagation; after the closing an ESTIMATE "
         "(non-green); status READING; NOT GREEN; on this model it cannot turn green, since seated (Z) excludes the "
         "model's join column", "value": {
             "status": "READING", "green": False,
             "non_green_inputs": list(NON_GREEN_INPUTS), "green_inputs": list(GREEN_INPUTS),
             "no_longer_needs": ["a condition on ell through the closing", "a condition on the shape growing with N",
                                 "eq. (17)'s own metric on our plane (but H-FAR-MODEL keeps an on-plane throat)"]}},
    ]


CHECKS = {
    "C1": (check_C1, "X0 the general code = b4_global.far_boundary() on the round T (exact)",
           [("lapse_dropped", "sqrt|g| without the lapse, a_n kept"), ("an_sign", "a_n added, not subtracted"),
            ("s2_power", "the S^2 factor rho, not rho^2"), ("normal_in", "the inward normal (theta signs swapped)")]),
    "C2": (check_C2, "X0 the general code = b4_global.tipped_far_boundary() on the owner's grid",
           [("lapse_dropped", "sqrt|g| without the lapse"), ("an_sign", "a_n added, not subtracted")]),
    "C3": (check_C3, "X1 the ellipse's closed form, tip, W = U control, square-on foot",
           [("warp_count", "the warp's 3 (T's dimension) written 2"), ("s2_coeff", "the S^2's 2 written 1")]),
    "C4": (check_C4, "X2/X3 Q >= 3 by z3 with guards; the switch ell*",
           [("k_below_3", "K >= 29/10 in place of 3 (z3 must find a counterexample)"),
            ("side_dropped", "(K - 1) b <= 3 in place of 2 (z3 must find a counterexample)")]),
    "C5": (check_C5, "X4 the scan at the example README",
           [("antiwarp", "the warp inverted, Om = z/ell"), ("floor_3_over_U", "the floor claimed as 3/U")]),
    "C6": (check_C6, "X5 the shape free of N; the size grows; the parabola's needed ratio grows with N",
           [("parabola", "the owner's parabola in place of the ellipse at the same ratios")]),
    "C7": (check_C7, "X6 the model's cones (from metric('model')) and T_E's distance from the reach",
           [("oblate", "W = 0.9 U (an oblate surface)"), ("short", "U = 0.95 R_reach"),
            ("s2_negative", "the model's S^2 coefficient made negative (the cones no longer bound du, dw)"),
            ("inflow_omitted", "U sized on R_core + T, leaving out the README's initial support")]),
    "C8": (check_C8, "X7 the radiation step's margin, 4D and 5D",
           [("e_rad_big", "E_rad inflated by 1e5"), ("g5_no_ell", "G5 taken as G4, without the factor ell")]),
    "C9": (check_C9, "X8 a far field at T_E in the board's configuration",
           [("field_x1e4", "the far field inflated by 1e4"), ("no_field", "the far field switched off")]),
    "C10": (check_C10, "X9 why H-FAR-MODEL is not derived; (Z) against its column; the model against (G), 139 (1)",
            [("a_zero", "the column removed (a = 0) in the Ricci computation"),
             ("p_sign", "the column's depth power's sign flipped"),
             ("general_sign", "the general column's R(k,k) claimed positive, +2A^2/rho^4"),
             ("p2_negative", "position 2's sheet put on a negative-tension plane, as 139 (1) (the conflict vanishes)")]),
    "C11": (check_C11, "X10 the plane's matter against its tension (184)",
            [("no_c2", "the mass density used as an energy density"),
             ("nuc_as_mean", "the local density bound taken as the cosmic mean")]),
    "C12": (check_C12, "X11 no column: every W >= U untrapped; a bulk-centred test field",
            [("k_below_1", "K >= 9/10 in place of 1 (z3 must find a counterexample)"),
             ("column_restored", "the column put back (a = 2) in the scan"),
             ("field_x1e2", "the bulk-centred test field inflated by 100 (the sufficient bound must fail)")]),
}


def _doc_193_ok(text):
    """Every line naming item 193 must record it as withdrawn (194)."""
    return all(("withdrawn" in ln or "194" in ln) for ln in text.splitlines() if "193" in ln)


def check_CG(mut=None, details=None):
    """Guards: every row labelled from LABELS; every check has a mutant; the status agrees with M's green rule (GREEN
    only if PROVED, DERIVED or AXIOM with no non-green input); item 193 is never cited as standing."""
    rows = rows_from(details)
    if mut == "planted_label":
        rows[1]["label"] = "positive"
    if mut == "green_claimed":
        rows[-1]["value"]["green"] = True
    if mut == "inputs_dropped":
        rows[-1]["value"]["non_green_inputs"] = []
    lab_ok = all(any(r["label"].startswith(L) for L in LABELS) for r in rows)
    ids_ok = [r["id"] for r in rows] == list(ALL_LABEL_KEYS)
    mut_ok = all(len(v[2]) >= 1 for v in CHECKS.values())
    st = rows[-1]["value"]
    rule_green = st["status"] in GREEN_STATUSES and not st["non_green_inputs"]
    status_ok = (st["green"] is rule_green and st["green"] is False
                 and (st["status"] == "READING") == bool(st["non_green_inputs"]))
    doc = __doc__ + ("\n  193      M chose: \"An axiom of my theory\"" if mut == "193_live" else "")
    doc_ok = _doc_193_ok(doc)
    try:
        with open(os.path.join(HERE, "B4C-FAR.md"), encoding="utf-8") as fh:
            note = fh.read()
    except OSError:
        note = ""
    if mut == "193_live_note":
        note += "\n- **193:** you chose *\"An axiom of my theory\"*.\n"
    note_ok = bool(note) and _doc_193_ok(note)
    ok = lab_ok and ids_ok and mut_ok and status_ok and doc_ok and note_ok
    return ok, {"labels": lab_ok, "ids": ids_ok, "every check has a mutant": mut_ok,
                "status by M's green rule (READING iff a non-green input; not green)": status_ok,
                "193 only as withdrawn (docstring)": doc_ok, "193 only as withdrawn (B4C-FAR.md)": note_ok}


CG_MUTANTS = (("planted_label", "a row labelled 'positive'"), ("green_claimed", "the status row says green"),
              ("inputs_dropped", "the non-green inputs dropped while the status stays READING"),
              ("193_live", "a line citing 193 as standing"),
              ("193_live_note", "a line in B4C-FAR.md citing 193 as standing"))


def compute():
    details = {cid: fn(None)[1] for cid, (fn, _, _) in CHECKS.items()}
    return rows_from(details), details


def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (bool, int, str)) or o is None:
        return o
    if isinstance(o, float):
        return o
    try:
        return float(o)
    except (TypeError, ValueError):
        return str(o)


def report(rows):
    print("b4c_far.py -- Warp Theorem lemma B4c on an ellipsoidal far surface (computed, READ and deduced; not "
          "verified; not seated)\n")
    for r in rows:
        print("%-6s [%s] %s" % (r["id"], r["label"], r["claim"]))
        print("       %s" % json.dumps(_clean(r["value"]))[:1500])


def selftest():
    t0 = time.perf_counter()
    allok, details = True, {}
    for cid, (fn, what, _) in CHECKS.items():
        ok, det = fn(None)
        details[cid] = det
        allok = allok and ok
        print("%-4s %s  %s\n      %s" % (cid, "PASS" if ok else "FAIL", what, json.dumps(_clean(det))[:900]))
    ok, det = check_CG(None, details)
    allok = allok and ok
    print("%-4s %s  guards\n      %s" % ("CG", "PASS" if ok else "FAIL", json.dumps(_clean(det))))
    print("selftest %s: %d checks, wall %.1f s" % ("PASSED" if allok else "FAILED", len(CHECKS) + 1,
                                                  time.perf_counter() - t0))
    return allok


def mutants():
    t0 = time.perf_counter()
    n, passed, details = 0, [], {}
    print("b4c_far --mutants: each named mutation must make its check FAIL")
    for cid, (fn, what, muts) in CHECKS.items():
        details[cid] = fn(None)[1]
        for name, desc in muts:
            n += 1
            try:
                ok, det = fn(name)
            except Exception as exc:                       # a mutation that breaks the computation also fails it
                ok, det = False, {"raised": repr(exc)[:200]}
            if ok:
                passed.append((cid, name))
            print("%-4s [%s] %s: %s\n      %s" % (cid, name, desc, "MUTATION PASSES" if ok else
                                                 "check FAILS (as required)", json.dumps(_clean(det))[:600]))
    for name, desc in CG_MUTANTS:
        n += 1
        ok, det = check_CG(name, details)
        if ok:
            passed.append(("CG", name))
        print("%-4s [%s] %s: %s" % ("CG", name, desc, "MUTATION PASSES" if ok else "check FAILS (as required)"))
    print("mutants: %d run, %d caught, %d passed %s; wall %.1f s" % (n, n - len(passed), len(passed), passed,
                                                                     time.perf_counter() - t0))
    return not passed


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--mutants", action="store_true")
    ap.add_argument("--json", metavar="PATH")
    ar = ap.parse_args(argv)
    rc = 0
    if ar.selftest:
        rc |= 0 if selftest() else 1
    if ar.mutants:
        rc |= 0 if mutants() else 1
    if ar.json:
        rows, _ = compute()
        with open(ar.json, "w") as fh:
            json.dump(_clean(rows), fh, indent=1)
        print("wrote %s" % ar.json)
    if not (ar.selftest or ar.mutants or ar.json):
        report(compute()[0])
    return rc


if __name__ == "__main__":
    sys.exit(main())
