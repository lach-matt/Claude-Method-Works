#!/usr/bin/env python3
"""b4c_far.py -- Warp Theorem lemma B4c (the far boundary T strictly untrapped, uniformly in time), rebuilt on an
ellipsoidal far surface.  A new owner beside lemmas/b4_global.py, which it imports by path and never copies.
Computed, READ and deduced; not verified; not seated; 2026-10-09.  Note: lemmas/B4C-FAR.md.

WHY.  b4_global.py's B4c found a ROUND far surface untrapped only if ell > 2 R_reach, a bound that grows with the README
(N^(1/3)), and a tipped parabola that needs a depth growing as N^(2/3)/c (the item-186 window checker, which also found
the parabola's published signs to be sampling artefacts near the plane).  The same checker found a convex ellipsoidal
surface (u/U)^2 + (w/W)^2 = 1, meeting the plane square-on, untrapped for W/U >= 1.74 at every c = ell/m it scanned
(1e-6 to 1e9) and trapped at 1.70.  This instrument proves that exactly, finds the exact threshold, and says what B4c
then earns.

CLI   python3 b4c_far.py               the report (every row labelled)
      python3 b4c_far.py --selftest    every check, each able to fail (~1 min)
      python3 b4c_far.py --mutants     every named mutation of every check; each must make its check FAIL (exit 1 if
                                       any mutation passes)
      python3 b4c_far.py --json PATH   compute()'s rows as JSON

LABELS.  computed / READ (verbatim + page) / deduced / STRUCTURAL / standard-not-READ / OPEN.  M's words are quoted
verbatim from M-RULINGS-2026-10-03.md, typing kept; the board's readings are named H-... and kept apart from them.

M'S WORDS USED (verbatim)
  152 (1)  "two separate positions connected by/reached through a dimension."
  152 (2)  "I had not considered this yet. It could very well be possible, so let's consider this an option and check it."
  157      "we already have at least half the model, our current universe."
  158 (2)  "Exactly as long as the write needs  I should think"
  162      "... The throat doesn't change size because the whole chain object only every takes on the size that contains
           the README upon opening. It is and always will be only the size that is needed to hold the object once and
           at once"
  179/180  "Let's approach this from a different angle. We know the corridor *does not sit on either position's plane,
           it only bridges them. So one could surmise that the corridor is exclusive to the bulk."
  183      M chose: "Yes: never violated as a pair"
  184      "There are no matter free planes"
  187 (3)  M chose: "Seat both"  (clauses (G) and (Z) as the board re-worded them)
  192      "this appears to be a question to put to the math language hierarchy cypher"
  193      M chose: "An axiom of my theory"  (H-PAIR-AXIOM: for the README crossing the corridor's fixed-size horizon)

THE BOARD'S READINGS USED (named, the board's; withdrawn if M corrects them)
  H-FAR-MODEL (b4_global.py): the far geometry is g = (ell/z)^2 (-dt^2 + du^2 + dw^2 + rho(u)^2 dOmega^2), z = ell + |w|,
    rho^2 = u^2 + a^2 -- Randall-Sundrum II's conformal form with B4a's join (152 (1) encoded as
    H-SEPARATE-JOINED-THROUGH-DIMENSION) carried as a throat column of conformal radius a at every depth.  A model, not
    a solution (X9 below computes how far from one).
  H-FAR-FIELD-EXTENSION (this file, for the 179 note only): eq. (17)'s far field on the plane extended into the bulk
    either isotropically in the coordinate distance d = sqrt(u^2 + w^2) (E1) or in g_uu alone (E2) -- two test
    extensions, not solutions.

RESULTS (units m = 1; c = ell/m; T_E = the ellipse {(u/U)^2 + (w/W)^2 = 1} x S^2, mirror-doubled, k = W/U)
  X0 OWNER AGREEMENT (computed).  The general level-set theta+ here -- b4_global's own recipe, div n over sqrt|g| with
     the lapse minus a_n, for any F and any static diagonal metric -- equals b4_global.far_boundary()'s closed form on
     the round T exactly (sympy), and b4_global.tipped_far_boundary()'s minimum on the owner's grid to 1e-12.
  X1 THE ELLIPSE IN CLOSED FORM (computed, exact).  On T_E, with D = sqrt(u^2/U^4 + w^2/W^4),
         P = 1/(U^2 W^2 D^2) + 2 u^2/(U^2 (u^2 + a^2)),      theta+ = -theta- = ((ell + w) P - 3 w/W^2) / (ell D),
     so theta+(tip) = (W^2 + W ell - 3U^2)/(U^2 ell) (the checker's form) and W = U gives the owner's round formula.
     T_E meets the plane square-on (dF/dw = 0 at w = 0), so the mirror and the warp's kink add no term.
  X2 THE THEOREM (deduced from X1; its one inequality machine-checked by z3, with vacuity and encoding guards).  With
     K = k^2, x = (u/U)^2, b = (a/U)^2 and Q = W^2 P = K/(1 + (K - 1) x) + 2 K x/(x + b):
         K >= 3 and (K - 1) b <= 2   ==>   Q >= 3 on all of T_E   ==>   theta+ = (ell P + (w/W^2)(Q - 3))/(ell D)
         >= P/D >= kappa >= U/W^2 > 0  at every point and EVERY ell > 0.
     The side condition reads a <= U at W = sqrt(3) U, which any T enclosing the throat meets, and allows any W/U up to
     sqrt(1 + 2 U^2/a^2) (~1e5 at the example README).  So T_E is strictly untrapped at every ell, with a floor U/W^2
     that does not depend on ell.  At W = sqrt(3) U exactly the tip reads sqrt(3)/U for every ell.
  X3 SHARP (computed, exact).  For W < sqrt(3) U the tip is trapped whenever ell < (3U^2 - W^2)/W: so sqrt(3) =
     1.7320508... is the exact threshold for "untrapped at every ell", between the checker's 1.70 (trapped) and 1.74.
  X4 THE SCAN (computed, 30-digit, the general code, independent of X1's algebra).  At the example README (U = 1.05 x
     (2 + 199702.187)) and c = 1e-6 ... 1e9: k = sqrt(3), 1.74, 2 untrapped with min theta+ >= U/W^2; k = 1.70 trapped
     exactly for the c below X3's switch.
  X5 FREE OF N (deduced + computed).  The threshold is a pure ratio; U(N) enters only through b = (a/U)^2, and U >=
     1.05 x 2 > a at every N.  Checked at N = 1e3, the example, 1e30.  Control: the owner's parabola needs W/U above a
     root that grows with N (its exact foot condition, ~3U/(4c)).
  X6 UNIFORMLY IN TIME THROUGH THE WRITE (STRUCTURAL + deduced; domain of dependence standard-not-READ).  The model's
     causal vectors obey du^2 + dw^2 <= dt^2 (STRUCTURAL); T_E keeps coordinate distance >= U from the origin; so with
     U = 1.05 (R_core + T_hold), R_core = 2 (G3's r0 = 2m) fixed by 162, no signal from the corridor reaches T_E before
     the closing, and the region outside its reach keeps the prior static state (domain of dependence; rests on global
     hyperbolicity, W2, as CGS's Theorem 3.5 itself does).  Any finite hold works (X2 is free of U): 158 (2) and E2's
     closing (DERIVED) make it finite; o3_write.py's >= 2.0e5 clocks is an illustration, not an input.
  X7 AFTER THE CLOSING (deduced, an estimate; Raychaudhuri standard-not-READ; b4_global's step with X2's floor).  The
     radiation's focusing ~ 2 E_rad/U^2 with E_rad <= (5/4) m (ledger.py E4, computed on eq. (17)) against the floor
     U/W^2: margin U/(2.5 k^2) = 2.8e4 at the example README (1.45e5 with the computed floor sqrt(3)/U); the exact floor's
     margin falls below 1 only for N below ~126 bits.  The 4D area law used for a 5D surface is the estimate's weak point.
  X8 UNDER 179: F1 IS NOT AN INPUT (computed).  Nothing in X1-X6 uses eq. (17).  With the corridor in the bulk and our
     plane carrying only eq. (17)'s far field (gamma = 5/4, bulk/kscale.py; spatial factor 1 + 2 gamma m/r, conformally
     flat to O(m)), the lapse cancels from theta+ exactly; any conformal far field whose gradient is at most that one
     keeps T_E untrapped at every ell if k^2 (1 - 3 gamma m/U) > 3 (deduced from X2), i.e. k > 1.7320663 at the example;
     scans with E1 and E2 keep 1.74 untrapped at every c, and E1 traps the tip at k = sqrt(3) exactly for small c (the
     field is real; the threshold moves by ~1e-5).
  X9 H-FAR-MODEL IS NOT DERIVED, AND WHY (computed + STRUCTURAL).  (a) Every T enclosing the reach crosses the join
     column (u = 0) at depth >= R_reach (~2.0e5 m at the example) -- the tip; (b) the only bulk the board has derived
     (b4_static's bank, built on eq. (17) as the plane's metric, F1) reaches r <= 32, y <= 16; (c) the model's column
     is not a solution: its 5D Ricci (computed) gives R(k,k) = -2 a^2/rho^4 along k = d_t + d_u, AdS5 exactly at a = 0,
     and along every radial light ray through the column the integral is -pi/a in g0's affine parameter (computed), so
     -(z/ell)^2 pi/a in the physical one (deduced: null affine parameters rescale by Om^2, standard-not-READ).  Taken as
     an exact geometry, Einstein's equations would give the column net negative null energy along each of those rays,
     against seated clause (Z) (deduced); H-PAIR-AXIOM (193) is for the README crossing the corridor's horizon and is
     not stretched to this column.  (d) Keeping the rest of the model, the tip's theta+ for ANY depth profile A(w) of
     the column's conformal radius is ((ell + W)/ell)(W/U^2 + 2 A'(W)/A(W)) - 3/ell (computed, exact): the verdict
     turns on the column's depth slope at depth W, which no ruling and no READ solution gives.  Power-law columns
     A = a (z/ell)^p move the tip threshold to k^2 >= 3 - 2p (exact); p = -1 and +1 scanned.
  X10 UNDER 184 (computed).  H-FAR-MODEL's plane is matter-free.  Our plane's mean energy density over its RS tension
     is rho_crit c^2/lambda_RS = (H0 ell/c)^2/2 exactly (cosmo.py's H0, kscale.tension), <= 2.7e-61 for ell <= 1e-4 m:
     the plane's matter enters the far bulk at that relative order (deduced, an estimate).

WHAT B4c EARNS.  PROVED within H-FAR-MODEL, from before the opening through the closing (X1-X6), at every ell and every
  N, on a surface of fixed shape -- W = sqrt(3) U in the model; W = 1.74 U also covers eq. (17)'s far field under 179
  (X8) -- with the domain-of-dependence step resting on W2, as CGS's theorem does; after the closing, the radiation
  step is derived as an estimate (X7).
  Its status stays READING: it rests on H-FAR-MODEL, now narrowed to the join column's geometry at depth >= R_reach
  (X9), which only the complete bulk (B3, OPEN; B4d) can supply.  NOT GREEN.  What it no longer needs: a condition on
  ell, a condition growing with N, eq. (17) on our plane (F1).  When B4d gives a column, X9 (d)'s tip formula and the
  general level-set code here decide at once whether an ellipse works.

NOT HERE  W2 (the bulk regular, B4b/B4d); B4a's topology (b4_global.py); the cypher audit (192) itself.
Imports lemmas/b4_global.py, lemmas/o3_write.py, lemmas/ledger.py, bulk/kscale.py and ../cosmo.py by path; reads the
bank lemmas/b4_static.json (data).  Stdlib + sympy + mpmath + z3 (pip install z3-solver).
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
R_CORE = 2                        # B4D-STAGE2's convention R_reach = (2 + hold) m
COVER = mp.mpf("1.05")            # U = 1.05 R_reach (the checker's cover)
C_SCAN = ("1e-6", "1e-3", "0.11", "1", "27.07", "4e5", "1e9")
LABELS = ("computed", "READ", "deduced", "STRUCTURAL", "standard-not-READ", "OPEN")
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
             "cosmo": os.path.join(WD, "cosmo.py")}


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
        return (Om, Om**2, Om**2, Om**2 * rho2)
    if kind == "column":                                  # the column's conformal radius a (z/ell)^p
        pp = -p if mut == "p_sign" else p
        return (Om, Om**2, Om**2, Om**2 * (u**2 + a**2 * (z / ell)**(2 * pp)))
    if kind == "column_general":
        A = sp.Function("A")(w)
        return (Om, Om**2, Om**2, Om**2 * (u**2 + A**2))
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


def surface_min(fn, family, c, Uv, Wv, args=(), n=200):
    """min theta+ over the quadrant of the surface (u, w >= 0; the other three by the symmetries u -> -u, w -> -w)."""
    best, at = mp.inf, None
    for t in tgrid(n):
        if family == "ellipse":
            uv, wv = Uv * mp.cos(t), Wv * mp.sin(t)
        else:
            uv, wv = Uv * mp.cos(t), Wv * (1 - mp.cos(t)**2)
        v = fn(uv, wv, mp.mpf(c), A_THROAT, Uv, Wv, *args)
        if v < best:
            best, at = v, t
    return best, at


def reach(N):
    """R_reach = R_core + T, T = o3_write's least write in clocks (Z = 108.75), clamped at 0; U = 1.05 R_reach."""
    ow = owner("o3_write")
    T = max(0.0, ow._num(ow.t_min(3), n=N))
    return T, mp.mpf(R_CORE) + mp.mpf(T), COVER * (mp.mpf(R_CORE) + mp.mpf(T))


def example_N():
    return owner("o3_write").EXAMPLE_N


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
                "min_theta": rows}


def check_C6(mut=None):
    """X5: free of N.  The theorem's hypotheses at three N; scans; the parabola's N-growing root as the contrast."""
    family = "parabola" if mut == "parabola" else "ellipse"
    fn = lam(family, "model")
    out, ok = {}, True
    for N in (1e3, example_N(), 1e30):
        T, Rr, Uv = reach(N)
        side_ok = (3 - 1) * (A_THROAT / Uv)**2 <= 2 and (mp.mpf("1.79")**2 - 1) * (A_THROAT / Uv)**2 <= 2
        good = [surface_min(fn, family, c, Uv, mp.mpf("1.74") * Uv, n=150)[0] for c in ("1e-6", "1", "1e9")]
        bad = surface_min(fn, family, "1e-6", Uv, mp.mpf("1.70") * Uv, n=150)[0]
        ok = ok and side_ok and all(g > 0 for g in good) and bad < 0
        out["N=%.3g" % N] = {"T": T, "U": float(Uv), "side_condition": bool(side_ok),
                             "1.74 min (c=1e-6,1,1e9)": [float(g) for g in good], "1.70 min c=1e-6": float(bad)}
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
    ok = ok and grows
    out["parabola foot, needed W/U at c = 1"] = roots
    out["parabola needed W/U grows with N"] = grows
    return ok, out


def check_C7(mut=None):
    """X6: the model's causal cones (STRUCTURAL), T_E's least distance, and the reach at the example README."""
    vt, vu, vw, vth, vph, th_ = sp.symbols("v_t v_u v_w v_th v_ph theta", real=True)
    z = ell + w
    Om = ell / z
    gvv = Om**2 * (-1 + vu**2 + vw**2 + (u**2 + a**2) * (vth**2 + sp.sin(th_)**2 * vph**2))
    extra = sp.simplify(gvv / Om**2 - (-1 + vu**2 + vw**2))
    cone_ok = sp.simplify(extra - (u**2 + a**2) * (vth**2 + sp.sin(th_)**2 * vph**2)) == 0   # a sum of squares >= 0
    k_ratio = mp.mpf("0.9") if mut == "oblate" else mp.sqrt(3)
    cover = mp.mpf("0.95") if mut == "short" else COVER
    dist2 = sp.simplify((U * sp.cos(ALPHA))**2 + (W * sp.sin(ALPHA))**2 - (U**2 + (W**2 - U**2) * sp.sin(ALPHA)**2))
    least_ok = dist2 == 0
    T, Rr, _ = reach(example_N())
    Uv = cover * Rr
    Wv = k_ratio * Uv
    least = min(Uv, Wv)
    margin = least - Rr
    ok = cone_ok and least_ok and margin > 0
    return ok, {"causal => du^2 + dw^2 <= dt^2": cone_ok, "u^2 + w^2 = U^2 + (W^2 - U^2) sin^2 on T_E": least_ok,
                "R_reach": float(Rr), "least distance of T": float(least),
                "clocks before the radiation can reach T": float(margin)}


def check_C8(mut=None):
    """X7: the radiation step's margin with X2's exact floor and with the computed floor."""
    e4 = owner("ledger").e4()
    mm = sp.Symbol("m", positive=True)
    far = sp.simplify(e4["far"] / mm)                     # 5/4 (E4's total, in units of m)
    e_rad = float(far) * (1e5 if mut == "e_rad_big" else 1)
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
    t_needed = float(2.5 * k**2) / float(COVER) - R_CORE                 # U = 2.5 k^2 at margin 1
    n_star = sp.solve(sp.Eq(ow.t_min(3).subs(ow.Z, ow.Z_HEAD).subs(ow.N, Ns), t_needed), Ns)
    n_star = float(n_star[0]) if n_star else None
    ok = far == sp.Rational(5, 4) and m_exact > 1e4 and m_comp >= m_exact and n_star is not None and n_star < 1e3
    return ok, {"E_rad cap (units m, ledger E4)": str(far), "floor exact U/W^2": float(floor_exact),
                "floor computed min P/D": float(floor_comp), "margin exact": float(m_exact),
                "margin computed": float(m_comp), "N below which the exact-floor margin < 1": n_star}


def check_C9(mut=None):
    """X8: the 179 note.  eq. (17)'s far field (kscale), lapse cancellation, the conformal-class bound, the scans."""
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
    _, Rr, Uv = reach(example_N())
    gv = mp.mpf(g_floor.p) / g_floor.q
    k_star = mp.sqrt(3 / (1 - 3 * gv / Uv))
    lam_max = (mp.mpf("1.74")**2 - 3) * Uv / (3 * gv * mp.mpf("1.74")**2)
    mval = mp.mpf("1e4") if mut == "field_x1e4" else mp.mpf(1)
    scans = {}
    good = True
    for kind in ("E1", "E2"):
        fn = lam("ellipse", kind, None, (m, gam))
        for c in C_SCAN:
            v, _ = surface_min(fn, "ellipse", c, Uv, mp.mpf("1.74") * Uv, (mval, gv), n=150)
            scans["%s k=1.74 c=%s" % (kind, c)] = float(v)
            good = good and v > 0
    fn = lam("ellipse", "E1", None, (m, gam))
    at_sqrt3, _ = surface_min(fn, "ellipse", "1e-6", Uv, mp.sqrt(3) * Uv, (mp.mpf(1), gv), n=150)
    scans["E1 k=sqrt3 c=1e-6"] = float(at_sqrt3)
    ok = (g_floor == sp.Rational(5, 4) and coef == 2 * g_floor and iso_ok and lapse_ok and conf_ok and delta_ok
          and mp.mpf("1.74") > k_star and lam_max > 100 and good and at_sqrt3 < 0)
    return ok, {"gamma at r0 = 2m (kscale)": str(g_floor), "eq. (17) g_rr = 1 + coef m/r, coef": str(coef),
                "isotropic psi^4 = 1 + 2 gamma m/rho with r = rho + gamma m, to O(m)": iso_ok,
                "lapse cancels from theta+": lapse_ok, "conformal identity": conf_ok, "delta closed form": delta_ok,
                "k* = sqrt(3/(1 - 3 gamma m/U))": float(k_star), "largest field multiple 1.74 survives (bound)":
                float(lam_max), "scans": scans}


def check_C10(mut=None):
    """X9: why H-FAR-MODEL is not derived -- the model's own 5D Ricci, the ray integral, the general column's tip,
    the power-law columns, and the crossing depth against the board's derived bulk."""
    t_, th_, ph_ = sp.symbols("t theta phi")
    X = [t_, u, w, th_, ph_]
    aa = sp.Integer(0) if mut == "a_zero" else a
    z = ell + w
    Om = ell / z
    rho2 = u**2 + aa**2
    g = sp.diag(-Om**2, Om**2, Om**2, Om**2 * rho2, Om**2 * rho2 * sp.sin(th_)**2)
    gi = g.inv()
    n = 5
    Gam = [[[sum(gi[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
                 for l in range(n)) / 2 for k in range(n)] for j in range(n)] for i in range(n)]

    def ric(j, k):
        return sp.simplify(sum(sp.diff(Gam[i][j][k], X[i]) for i in range(n))
                           - sum(sp.diff(Gam[i][j][i], X[k]) for i in range(n))
                           + sum(Gam[i][i][l] * Gam[l][j][k] for i in range(n) for l in range(n))
                           - sum(Gam[i][k][l] * Gam[l][j][i] for i in range(n) for l in range(n)))
    res = [sp.simplify(ric(i, i) + 4 / ell**2 * g[i, i]) for i in range(n)]
    off = sp.simplify(ric(1, 2))
    rkk = sp.simplify(ric(0, 0) + ric(1, 1))
    want = -2 * a**2 / (u**2 + a**2)**2
    ricci_ok = (sp.simplify(rkk - want) == 0 and all(sp.simplify(res[i]) == 0 for i in (0, 2, 3, 4))
                and sp.simplify(res[1] - want) == 0 and off == 0)
    ads_ok = all(sp.simplify(x.subs(a, 0)) == 0 for x in res)
    ray = sp.integrate(want, (u, -sp.oo, sp.oo))
    ray_ok = sp.simplify(ray + sp.pi / a) == 0
    thA = theta_plus(ELLIPSE, metric("column_general"))
    A = sp.Function("A")
    tip = sp.simplify(sp.simplify(thA.subs(u, 0)).subs(w, W))
    tip_want = ((ell + W) / ell) * (W / U**2 + 2 * sp.Derivative(A(W), W) / A(W)) - 3 / ell
    tipA_ok = sp.simplify(tip - tip_want) == 0
    thp = theta_plus(ELLIPSE, metric("column", "p_sign" if mut == "p_sign" else None))
    tip_p = sp.simplify(sp.simplify(thp.subs(u, 0)).subs(w, W))
    tipp_ok = sp.simplify(tip_p - (((ell + W) / ell) * (W / U**2 + 2 * p / (ell + W)) - 3 / ell)) == 0
    _, Rr, Uv = reach(example_N())
    fnc = lam("ellipse", "column", None, (p,))
    scan = {}
    for pv, kv, expect in ((-1, mp.sqrt(5), "untrapped"), (-1, mp.mpf(2), "trapped at small c"),
                           (1, mp.sqrt(3), "untrapped"), (1, mp.mpf(1), "reported")):
        vals = [surface_min(fnc, "ellipse", c, Uv, kv * Uv, (pv,), n=120)[0] for c in ("1e-6", "1", "1e9")]
        scan["p=%+d k=%.4f" % (pv, float(kv))] = ([float(v) for v in vals], expect)
    col_ok = (all(v > 0 for v in scan["p=-1 k=2.2361"][0]) and scan["p=-1 k=2.0000"][0][0] < 0
              and all(v > 0 for v in scan["p=+1 k=1.7321"][0]))
    bank = json.load(open(os.path.join(HERE, "b4_static.json")))
    r_max = float(max(sp.Rational(x) for x in bank["r"]))
    y_max = max(len(c_["A"]) for c_ in bank["cols"].values()) * bank["dy"]
    cross_ok = Rr > 1e3 * max(r_max, y_max)
    ok = ricci_ok and ads_ok and ray_ok and tipA_ok and tipp_ok and col_ok and cross_ok
    return ok, {"R(k,k), k = d_t + d_u": str(rkk), "only R_uu departs from AdS5": ricci_ok, "a = 0 is AdS5": ads_ok,
                "net along a radial ray (conformal)": str(ray), "general column tip": str(tip),
                "general tip formula": tipA_ok, "power-law tip formula": tipp_ok, "column scans": scan,
                "crossing depth >= R_reach": float(Rr), "derived static bulk reaches r <=, y <=": [r_max, y_max]}


def check_C11(mut=None):
    """X10: the 184 note.  rho_crit c^2/lambda_RS = (H0 ell/c)^2/2, and its size for ell <= 1e-4 m."""
    ks, co = owner("kscale"), owner("cosmo")
    ellv = sp.Symbol("ell_SI", positive=True)
    H0 = sp.Symbol("H0", positive=True)
    rho_crit = 3 * H0**2 / (8 * sp.pi * ks.G)                         # kg/m^3, with kscale's exact G
    energy = rho_crit if mut == "no_c2" else rho_crit * ks.C**2
    ratio = sp.simplify(energy / ks.tension(ellv))
    ident = sp.simplify(ratio - (H0 * ellv / ks.C)**2 / 2) == 0
    val = float(ratio.subs({H0: co.H0(), ellv: sp.Rational(1, 10**4)}))
    ok = ident and val < 1e-60
    return ok, {"identity (H0 ell/c)^2/2": ident, "ratio at ell = 1e-4 m": val, "H0 (1/s, cosmo.py)": co.H0()}


ALL_LABEL_KEYS = ("X0", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "STATUS")


def rows_from(details):
    d = details
    return [
        {"id": "X0", "label": "computed", "claim": "the general level-set theta+ equals b4_global's far_boundary (exact) "
         "and tipped_far_boundary (owner grid)", "value": [d["C1"], d["C2"]]},
        {"id": "X1", "label": "computed (exact, sympy)", "claim": "theta+ on T_E = ((ell + w) P - 3w/W^2)/(ell D); tip "
         "(W^2 + W ell - 3U^2)/(U^2 ell); W = U is the owner's round formula; square-on at the plane", "value": d["C3"]},
        {"id": "X2", "label": "deduced from X1; computed (z3, guards)", "claim": "W >= sqrt(3) U and (W^2 - U^2) a^2 <= "
         "2 U^4 give theta+ >= U/W^2 > 0 at every point and every ell", "value": d["C4"]},
        {"id": "X3", "label": "computed (exact)", "claim": "W < sqrt(3) U is trapped at the tip for ell < (3U^2 - "
         "W^2)/W: sqrt(3) is the exact threshold", "value": d["C4"]["switch ell* = (3U^2 - W^2)/W"]},
        {"id": "X4", "label": "computed (30-digit scan, general code)", "claim": "example README: sqrt(3), 1.74, 2 "
         "untrapped above the floor at c = 1e-6..1e9; 1.70 trapped exactly below its switch", "value": d["C5"]},
        {"id": "X5", "label": "deduced; computed", "claim": "free of N (pure ratio; U >= 2.1 > a at every N); the "
         "parabola's needed ratio grows with N", "value": d["C6"]},
        {"id": "X6", "label": "STRUCTURAL; deduced; standard-not-READ (domain of dependence, on W2)",
         "claim": "untrapped through the write: the corridor's influence stays inside the coordinate disc R_core + t, "
         "T_E stays at distance >= U; any finite hold", "value": d["C7"]},
        {"id": "X7", "label": "deduced, an estimate; standard-not-READ (Raychaudhuri)", "claim": "after the closing the "
         "radiation cannot trap T_E: margin U/(2.5 k^2)", "value": d["C8"]},
        {"id": "X8", "label": "computed; deduced", "claim": "under 179 eq. (17) on our plane is not an input; with "
         "only its far field 1.74 stays untrapped at every c", "value": d["C9"]},
        {"id": "X9", "label": "computed; STRUCTURAL", "claim": "H-FAR-MODEL is not derived: T must cross the join "
         "column at depth >= R_reach; the model's column has R(k,k) = -2a^2/rho^4, net -pi/a per radial ray; the "
         "tip turns on the column's depth slope", "value": d["C10"]},
        {"id": "X10", "label": "computed; deduced, an estimate", "claim": "under 184 the plane's matter enters at "
         "(H0 ell/c)^2/2 <= 2.7e-61", "value": d["C11"]},
        {"id": "STATUS", "label": "deduced", "claim": "B4c: PROVED within H-FAR-MODEL before the opening through the "
         "closing at every ell and N (W = sqrt(3) U in the model, 1.74 U with eq. (17)'s far field); after the closing "
         "DERIVED as an estimate; status READING (H-FAR-MODEL narrowed to the join column at depth >= R_reach); NOT "
         "GREEN", "value": {
             "status": "READING", "green": False,
             "rests_on": ["H-FAR-MODEL (the board's): the join column's geometry at depth >= R_reach",
                          "W2 for the domain-of-dependence step (as CGS Thm 3.5 itself)",
                          "E2 (DERIVED): the closing exists, so the hold is finite",
                          "162 (M's): the corridor's size is fixed, R_core = 2m",
                          "Raychaudhuri (standard-not-READ) for the after-closing estimate"],
             "no_longer_needs": ["a condition on ell", "a condition growing with N", "eq. (17) on our plane (F1)"]}},
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
    "C6": (check_C6, "X5 free of N; the parabola's needed ratio grows with N",
           [("parabola", "the owner's parabola in place of the ellipse at the same ratios")]),
    "C7": (check_C7, "X6 the model's cones and T_E's distance from the reach",
           [("oblate", "W = 0.9 U (an oblate surface)"), ("short", "U = 0.95 R_reach")]),
    "C8": (check_C8, "X7 the radiation step's margin",
           [("e_rad_big", "E_rad inflated by 1e5")]),
    "C9": (check_C9, "X8 eq. (17)'s far field only (179)",
           [("field_x1e4", "the far field inflated by 1e4")]),
    "C10": (check_C10, "X9 why H-FAR-MODEL is not derived",
            [("a_zero", "the column removed (a = 0) in the Ricci computation"),
             ("p_sign", "the column's depth power's sign flipped")]),
    "C11": (check_C11, "X10 the plane's matter against its tension (184)",
            [("no_c2", "the mass density used as an energy density")]),
}


def check_CG(mut=None, details=None):
    """Guards: every row labelled from LABELS; every check has a mutant; the status row says READING, not green."""
    rows = rows_from(details)
    if mut == "planted_label":
        rows[1]["label"] = "positive"
    if mut == "green_claimed":
        rows[-1]["value"]["green"] = True
    lab_ok = all(any(r["label"].startswith(L) for L in LABELS) for r in rows)
    ids_ok = [r["id"] for r in rows] == list(ALL_LABEL_KEYS)
    mut_ok = all(len(v[2]) >= 1 for v in CHECKS.values())
    st = rows[-1]["value"]
    status_ok = st["status"] == "READING" and st["green"] is False
    ok = lab_ok and ids_ok and mut_ok and status_ok
    return ok, {"labels": lab_ok, "ids": ids_ok, "every check has a mutant": mut_ok, "status READING, not green":
                status_ok}


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
    for name, desc in (("planted_label", "a row labelled 'positive'"), ("green_claimed", "the status row says green")):
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
