#!/usr/bin/env python3
"""r1_cover.py -- B4d / E-PASS: THE COVER (question r1-cover, put under M-RULINGS item 196).  Computed and deduced; not
verified (to be verified by a separate AI session in this project); not seated.  First headed "... not verified; not
seated" (2026-10-09).

THE QUESTION (the board's wording).  With nothing crossing the corridor's horizon (the README held, 195's reading, being
worked) or with a balanced pair (F5, OPEN), the corridor is stationary through the write.  Is the stationary corridor's
bulk regular on the README's causal past over the whole write (>= 2.0e5 clocks): does position 2's piece (172 (1)) keep
the singular depth y_s out of J^-(P_c) across the whole cover -- beyond the throat's O(x) range, out to the footprint
R_F and the far field -- and not only near the throat?

M's words used here (verbatim in the rulings file; quoted, never paraphrased as M's):
  161 "my inclination is yes"
  162 (excerpt) "It is and always will be only the size that is needed to hold the object once and at once"
  163 M chose "All together, one whole"
  172 (1) M chose "Yes, it may" to the board's "While the corridor holds, may position 2's piece of our plane carry the
      README's stress (stress that obeys the NEC)?"; (2) M chose "Yes, that is coinciding"; the record: "Not answered:
      which part of position 2's stress is its law"
  174 M chose "For the math" (three times)
  149 "I have given you everything I can. You have to work the math now"
  179/180 "We know the corridor *does not sit on either position's plane, it only bridges them. So one could surmise that
      the corridor is exclusive to the bulk."
  184 "There are no matter free planes"
  195 "The README is not a pair"
  196 "Review all tasks running. Stop any that are no longer relevant. All questions get works through the cypher"

CONDITIONS, NAMED (every one the board's unless marked).  F1: these columns take eq. (17) as the plane's own metric
(the board's configuration; seated clause (G) keeps eq. (17) only as a plane's possible reading of the mouth, so every
result here is conditional on the mouth lemma, H-PLANE-READS-MOUTH, OPEN).  Clause (B) in full on P1 (vacuum Lambda_5,
RS tension, matter-free: a limit under 184).  H-Z2-PIECES (P2 mirrored, one-sided toward the slab).  H-README-ON-P2
(M's 172 (1)).  H-CROSSABLE-HORIZON (adopted under 149 for P2's unanswered law: the smooth and band classes at the
horizon; S7's power laws excluded there and kept as the control).  H-PROFILE-CONTINUED (each sampled member's
near-throat formula continued literally beyond x_valid: the only global continuation computed here; no ruling fixes
P2's global shape).  H-QUASI-STATIC-CORRIDOR (stationary bulk through the write: the question's premise).
H-HOLD-IN-ADVANCED-TIME (X8's frame).  Raw Pade as evidence (S9's rule): VERIFIED means two Pade orders agree on A, B, C
to 1e-4 (b4_static S3's value rule) -- a convergence heuristic, not a bound.  The README a test event (SIM1 S3b).

  R1 THE CEILING (computed).  y_s(r) on the cover, per ell of ES2: the throat's y_s^th (sim2_facing.throat_bulk, the
     zeroth-order ODE to alpha = 1e-9); on each owner column (b4_static.series at order 32, sim2_facing.column_w
     unchanged: the 13 banked radii 2.005m-10m and three far radii 20, 50, 100m) the median Pade singularity where the
     three orders agree within 5% (ys_stable), and the verified top vtop.  R_F (X12's rule): the largest banked radius
     whose column is ys_stable.
  R2 THE CONE (computed; deduced).  A column point (r, y) reaches P_c by the vertical null leg at fixed r (advanced cost
     int_0^y dy/sqrt(A), raw Pade at two orders), the plane's ingoing null leg (dv = 0 by the definition of v) and the
     plane's horizon generator (v increasing to v_c).  So the advanced hold that places (r, y) in J^-(P_c) is at most
     that integral; near the throat X7's budgets (imported, verified) take over.
  R3 THE MEMBERS CONTINUED (computed).  Depth rows from X9 (sim2_passage.slab_rows, imported): 0 (coinciding), 0.1 y_s,
     d_+ (where it exists), y*, the band's midpoint.  Members: the smooth family at the adjudication's g2 (margin
     CO_MARGIN = 1) and at the NEC margin NEAR_MARGIN = 1e-2 (the board's choice); the level surface (band class, only
     where W1(d) >= 0); the power laws lam = 0.1, 0.25, 0.4 (controls).  Amplitude c = g1 = 0.05 (sim2_facing.DT_C).
     P2 = d + f(x), x = r - 2m.  Per node: CLOSED (P2 <= 0: the piece has met P1), DEEP (P2 >= y_s at a stable
     column), VERIFIED (0 < P2 <= vtop), UNDECIDED; between nodes the board's convention (P2's maximum on the interval
     against the lesser ceiling of its two ends; not a bound: y_s is not computed between columns).  After a CLOSED
     interval the piece is absent: a later column whose y_s is located (stable) is an UNCUT singular layer.
  R4 THE NEC ALONG THE CONTINUATION (computed).  P2's radial and angular NEC (rho + p_r, rho + p_th, Israel with the
     normal into the slab) at each open node, on the owner column, exact in the slope: k_t = [-kappa_t + F' d_r ln A /
     (2B)]/N, k_th likewise with C, k_r = [F'' - B kappa_r - F'(d_r ln B/2 + 2 F' kappa_r)]/(N (B + F'^2)) -- the same
     formula as sim2_facing._graph_k's docstring, here with the owner's A, B, C (checked equal to _graph_k on the throat
     metric).
  R5 THE CRITICAL AMPLITUDE (computed).  For each power law, c* over the cover to R_F = min over the throat (X9's c*)
     and the stable columns of (y_s - d)/x^lam; for the smooth family at its sampled g2, g1* = min (y_s - d - g2 x)/sqrt x.
  R6 CONTROLS (computed).  (a) A power law: excluded at the horizon by H-CROSSABLE-HORIZON (C11b: its crosser-frame
     stress diverges; imported), and at twice its c* it must FAIL the cover.  (b) A cut piece: a member that holds,
     ended at r = 2.05m, must FAIL (the columns beyond carry a located y_s, in J^-(P_c) by R2).
  R7 THE FAR FIELD (computed; deduced; OPEN).  The three far columns; and, deduced and checked with sympy, the radial NEC
     in pure AdS_5 reads F'' <= -e F'^2 (so a NEC piece far out deepens at most logarithmically in r: e^(eF) at most
     linear), against which a literal power law leaves the NEC class far out.

RESULTS (the full run, 2026-10-09: 144 columns = 16 radii x 9 ell at order 32; pinned below; labels as stated).
  R1 (computed).  The 117 banked columns reproduce sim2_bank.json (y_s, stability, vtop; worst 5e-13 after pinning) and
     X12's R_F table exactly: R_F = 2.2, 2.2, 2.2, 2.2, 2.15, 2.2, 2.1, 2.5, 10.0m at ell = inf ... m/4.  y_s(r) >= y_s^th
     at every stable column.  Beyond R_F no y_s is located at ell >= 4m (e <= 1/4) out to 100m (verified tops 2.3m at
     r = 2.3m rising to the 10m scan cap at r >= 10-20m for e <= 1/16).  At ell <= 2m a singular depth is located
     again in the far field: e = 1/2 at 100m (8.45m); e = 1 at 50m (3.98m) and 100m (4.52m); e = 2 at 20, 50, 100m
     (1.86, 2.16, 2.42m); e = 4 at 10, 20, 50, 100m (0.867, 0.989, 1.162, 1.299m) -- at r = 100m 4.2-5.2 ell deep.
  R2 (computed; deduced).  The largest vertical-leg hold over all 144 columns, to vtop or to 0.9 y_s, is 88.7 clocks
     (e = 1/2, r = 100m); floor/hold >= 2250 at every ell.  So every computed column point down to its ceiling lies in
     J^-(P_c) through the write (with X7's 389.3 clocks, imported, near the throat).  One located column is not counted:
     at e = 4, r = 20m the raw Pade's A is not positive to 0.9 y_s at either order, so its hold is not computed.
  R3 (computed, on H-PROFILE-CONTINUED).  Shallower than y_s: every crossable member at depth 0, 0.1 y_s and d_+ stays
     below y_s(r) at every node where it exists, at every ell (least y_s - P2 from 2.55m at ell = inf to 0.34m at
     m/4).  But a piece that meets P1 leaves the bulk beyond it uncut:
       smooth family at the adjudication's g2 (X9's member): at depth 0 it meets P1 at r = 2.0025m, inside x_valid(0) =
       0.04 (X9 compared P2 with y_s^th only, not with P1: a finding, recorded, not repaired), and FAILS (UNCUT) at
       r = 2.005m at every ell; at 0.1 y_s it meets P1 at 2.047-2.224m: verified to R_F at ell = inf, 32m, 16m, 4m, and
       FAILS (UNCUT) at 2.2, 2.15, 2.1, 2.1, 2.05m at e = 1/8, 1/2, 1, 2, 4.
       smooth family 1e-2 inside its NEC bound: at 0.1 y_s it is verified, with the NEC kept at all 10 settled nodes,
       to r = 3m at every ell (past R_F), then meets P1 at 3.205-3.734m; beyond, UNDECIDED at e <= 1/4 (nothing
       located), FAILS (UNCUT) at e = 1/2, 1, 2, 4 (at 100, 50, 20, 10m).  At depth 0 it is verified to 20m (10m at
       e = 2, 4), meets P1 at 27.0-13.1m, UNDECIDED beyond at e <= 1/4, FAILS (UNCUT) at e >= 1/2.
       level surface (band class): verified where its depth is, but it breaks the radial NEC at every settled node at
       r >= 2.05m (215 of 215; Lemma W), so it leaves 172 (1)'s class off the throat.
       deep rows (y*, the band's midpoint): margins thin (0.76m at ell = inf down to 1e-4m at m/4).  At ell >= 4m y* is
       verified to 100m for the level surface and the NEC-near smooth family (both breaking the NEC); the band's
       midpoint is verified to 100m only for the level surface (and some power laws) at ell = inf and 16m, and is
       otherwise UNDECIDED from 2.005-2.1m; at ell <= 2m every deep row is UNDECIDED from the first column (the slab
       passes the verified top) or FAILS.
       power laws (controls): verified to 100m at shallow depths at every ell, but excluded at the horizon and breaking
       the NEC along the continuation at most settled nodes; at y* and the band they FAIL at the throat for ell <= m/2
       (X9's 11 cases, reproduced as C10).
  R4 (computed).  The literally continued smooth family breaks the angular NEC once it heads back to P1 steeply (e.g.
     0.1 y_s, adjudication's g2: 2 of 7 settled nodes at ell = inf); the NEC-near member at 0.1 y_s keeps both parts at
     every settled node at every ell.
  R5 (computed).  c* over the cover to R_F (shallow rows) runs from about 5.0 (lam 0.4, ell = inf) to 0.36 (m/4).  The
     columns, not the throat, set it in every shallow case but one (e = 1, 0.1 y_s, lam 0.1: the throat, by 1%): the
     cover is tighter than X9's near-throat c* by up to a factor 1.9 at ell >= m/2 and 3.7 at m/4 (lam 0.4, R_F = 10m).
     All are far above the sampled 0.05.
  R6 (computed).  Both controls FAIL at every ell: the power law at 2 c* (DEEP, at 2.005-2.02m), the cut piece (UNCUT at
     2.1m).  Power laws' crosser-frame growth 6.3e4-1.6e7 (smooth: 1).
  R7 (deduced; sympy).  In pure AdS_5 the radial NEC reads F'' <= -e F'^2 exactly (control: a wrong warp leaves a
     residual); a literal power law leaves the NEC class beyond x_max = ((1 - lam)/(e c lam))^(1/lam) (154m for lam 0.4
     at m/4).  Whether a NEC piece can stay open at bounded depth far out is OPEN (not computed).
  VERDICT (on the board's configuration, F1; conditional on the mouth lemma; H-PROFILE-CONTINUED).  No: no sampled
     member of H-CROSSABLE-HORIZON keeps y_s out of J^-(P_c) across the whole computed cover at every ell.  The best,
     the smooth family 1e-2 inside its NEC bound at 0.1 y_s, does so with the NEC kept to r = 3m at every ell -- past R_F,
     not only near the throat -- and then meets P1; beyond it nothing is located at ell >= 4m (UNDECIDED) and a far
     singular depth is located and left uncut at ell <= 2m (FAILS).  What it shows is a property of the continued
     formulas; a piece shaped otherwise beyond 3m (P2's law is unanswered, 172) is not computed.  The cypher
     classifies; nothing here is a derived physical value.

Owners imported by path (never copied): sim2_passage.py (tb, slab_rows, write_floor, layer, crosser_frame), and through
it sim2_facing.py (column_w, raw_rational, pade_orders, throat_bulk, _ystar, _smooth_g2, _profile, _graph_k, israel,
x_valid, CO_MARGIN, DT_C, DT_LAMS, RADII2, ES2), b4d_stage5.py (warped), b4_static.py (series); tools/cypher.py for
--cypher (registered in sys.modules before exec_module).  The memo around b4_static.series inside column() changes no
value (one exact solve shared by column_w and the evaluations here).
Needs python-flint, sympy, numpy, scipy, mpmath.
python3 r1_cover.py [--selftest] [--mutants] [--full] [--cache PATH] [--json PATH] [--cypher DIR]
"""
import argparse
import contextlib
import importlib.util
import io
import json
import math
import os
import pickle
import sys
import time
from fractions import Fraction as Fr
from multiprocessing import Pool

import mpmath as mp
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
CYPHER_PATH = os.path.join(REPO, "tools", "cypher.py")


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


P = _load(os.path.join(HERE, "sim2_passage.py"), "r1cover_passage")
SF = P.SF
S5 = SF.S5
B4 = SF.B4
ES2 = list(SF.ES2)
N = SF.ORDER                                     # 32, the bank's order
BANK_RADII = tuple(SF.RADII2)                    # 2.005m ... 10m (sim2_bank.json's 13 radii)
FAR_RADII = ("20", "50", "100")                  # the far field computed here
RADII = BANK_RADII + FAR_RADII
DEPTH_KEYS = ("zero", "tenth", "d_plus", "y_star", "band_mid")
MEMBERS = (("smooth", "adj"), ("smooth", "near"), ("level",), ("pow", 0.1), ("pow", 0.25), ("pow", 0.4))
CROSSABLE = {"smooth adj", "smooth near", "level"}
NEAR_MARGIN = 1e-2                               # the smooth family 1e-2 inside its O(x) NEC bound (the board's choice)
CUT_RC = "41/20"                                 # R6 (b): the cut piece ends at r = 2.05m
CONTROL_AMP = 2.0                                # R6 (a): the power law at twice its c* over the cover
LIVE = (("41/20", "1/8"), ("11/5", "1/8"), ("10", "4"))     # the selftest's live columns
DPS = 30
GRID_N = 240                                     # P2 sampled per interval (log-spaced in x)
BANNED_KEYS = ("dist", "separation", "time", "redshift", "speed", "velocity", "length", "clock", "arrival")
NEC_SIGN = 1                                     # mutation hook: -1 flips the Israel normal (C6)
HOLD_POWER = 0.5                                 # mutation hook: 1/A**HOLD_POWER in the vertical leg (C3)


def mname(m):
    return "level" if m[0] == "level" else ("smooth " + m[1] if m[0] == "smooth" else "lam %g" % m[1])


def fmax(vals):
    """The larger finite value of a two-order pair (None if neither is finite)."""
    v = [x for x in (vals or []) if x is not None and math.isfinite(x)]
    return max(v) if v else None


# ------------------------------------------------------------------------------------------------- columns (R1, R2)
def _memo_series(rc, e, S):
    orig = B4.series

    def memo(rc_, N_, e_=Fr(0), data=B4._eq17):
        if rc_ == rc and N_ == N and Fr(e_) == Fr(e) and data is B4._eq17:
            return S
        return orig(rc_, N_, e_, data=data)
    return orig, memo


def raw_metric(S, e, o):
    """A, B, C with their y- and r-derivatives at depth y from the raw Pade (sim2_facing.raw_rational, no doublet
    removal: S9's convention) of the warp-divided series X~ = X e^(2ey) and of its r-derivative series."""
    W = S5.warped(S, e, N)
    R0 = {X: SF.raw_rational(W[X][0], o) for X in "ABC"}
    R1 = {X: SF.raw_rational(W[X][1], o) for X in "ABC"}
    ee = mp.mpf(Fr(e).numerator) / Fr(e).denominator

    def at(y):
        yy = mp.mpf(y)
        w = mp.exp(-2 * ee * yy)
        out = {}
        for X in "ABC":
            v = R0[X]["val"](yy)
            out[X] = w * v
            out[X + "y"] = out[X] * (R0[X]["ld"](yy) - 2 * ee)
            out[X + "r"] = w * R1[X]["val"](yy)
        return out
    return at


def graph_k(m, F1, F2):
    """Mixed extrinsic curvature (k_t, k_r, k_th) of y = F(r), normal into the slab, in dy^2 - A dt^2 + B dr^2 +
    C dOmega^2 (sim2_facing._graph_k's general formula, with the owner's A, B, C)."""
    A, B, C = m["A"], m["B"], m["C"]
    kt, kx, kq = m["Ay"] / (2 * A), m["By"] / (2 * B), m["Cy"] / (2 * C)
    dlA, dlB, dlC = m["Ar"] / A, m["Br"] / B, m["Cr"] / C
    F1, F2 = mp.mpf(F1), mp.mpf(F2)
    Nn = mp.sqrt(1 + F1**2 / B)
    k_t = (-kt + F1 * dlA / (2 * B)) / Nn
    k_q = (-kq + F1 * dlC / (2 * B)) / Nn
    k_x = (F2 - B * kx - F1 * (dlB / 2 + 2 * F1 * kx)) / (Nn * (B + F1**2))
    return k_t, k_x, k_q


def nec_parts(m, F1, F2):
    kt, kx, kq = graph_k(m, F1, F2)
    rho, ps = SF.israel([NEC_SIGN * kt, NEC_SIGN * kx, NEC_SIGN * kq, NEC_SIGN * kq], 1)
    return float(rho + ps[0]), float(rho + ps[1])


def hold(S, e, y):
    """R2: the vertical leg's advanced cost int_0^y dy/sqrt(A), raw Pade at the two verification orders."""
    if y is None or y <= 0:
        return [0.0, 0.0]
    W = S5.warped(S, e, N)
    ee = float(e)
    out = []
    for o in SF.pade_orders(N, e)[:2]:
        R = SF.raw_rational(W["A"][0], o)
        f = lambda t: 1 / (mp.exp(-2 * ee * t) * R["val"](t)) ** HOLD_POWER
        v = mp.quad(f, [0, y])
        out.append(float(mp.re(v)) if abs(mp.im(v)) < 1e-12 * abs(v) else float("nan"))
    return out


def column(rc, e, queries=(), S=None, col=None):
    """One owner column: sim2_facing.column_w unchanged (series memoised; or its cached output `col`, computed by the
    same call), the holds to vtop and to 0.9 y_s, and the NEC of each queried piece point (key, P2, F', F'') at the two
    verification orders."""
    mp.mp.dps = DPS
    e = Fr(e)
    t0 = time.monotonic()
    if S is None:
        S = B4.series(rc, N, e)
        col = None
    if col is None:
        orig, memo = _memo_series(rc, e, S)
        B4.series = memo
        try:
            col = SF.column_w(rc, e)
        finally:
            B4.series = orig
    mp.mp.dps = DPS
    ys = [float(v) for v in col["ys"]]
    stable = bool(col["ys_stable"])
    ysm = float(np.median(ys)) if stable else None
    out = {"rc": rc, "r": float(Fr(rc)), "e": str(e), "ys": ys, "ys_im": [float(v) for v in col["ys_im"]],
           "stable": stable, "ys_med": ysm, "vtop": float(col["vtop"]), "top": float(col["top"]),
           "hold_vtop": hold(S, e, float(col["vtop"])), "hold_ys90": hold(S, e, 0.9 * ysm) if stable else None}
    nec = {}
    if queries:
        ats = [raw_metric(S, e, o) for o in SF.pade_orders(N, e)[:2]]
        for key, y, F1, F2 in queries:
            nec[key] = [nec_parts(at(y), F1, F2) for at in ats]
    out["nec"] = nec
    out["cost"] = time.monotonic() - t0
    return out, S


def _job(args):
    rc, es, queries, S, keep = args[:5]
    col = args[5] if len(args) > 5 else None
    out, S = column(rc, Fr(es), queries, S, col)
    return out, (S if keep else None)


# ----------------------------------------------------------------------------------------------------- members (R3)
_SETUP = {}


def setup(e):
    """X9's depth rows and the throat at e (imported: sim2_passage.tb, slab_rows; sim2_facing._ystar)."""
    k = str(Fr(e))
    if k not in _SETUP:
        tbe = P.tb(e)
        yst, W1 = SF._ystar(tbe)
        rows = P.slab_rows(e, P.write_floor())
        _SETUP[k] = {"tb": tbe, "W1": W1, "y_star": yst, "ys_th": tbe["y_s"], "rows": rows}
    return _SETUP[k]


def profile(m, st, dep):
    """(F, F', F'') of member m at depth dep, or None where the member is not admitted (the level surface needs
    dep > 0 and W1(dep) >= 0); with g2 for the smooth family."""
    if m[0] == "level":
        if dep <= 0 or float(st["W1"](dep)) < -1e-9:
            return None, None
        return (lambda x: (0.0, 0.0, 0.0)), None
    if m[0] == "pow":
        return (lambda x, lam=m[1]: tuple(SF._profile(("pow", lam), x)[:3])), None
    g2 = SF._smooth_g2(st["tb"], dep, st["W1"])
    if m[1] == "near":
        g2 = g2 + SF.CO_MARGIN - NEAR_MARGIN
    return (lambda x, g2=g2: tuple(SF._profile(("smooth",), x, g2)[:3])), g2


def x_meet(m, dep, g2):
    """Where the continued piece meets P1 (dep + f(x) = 0, x > 0): only the smooth family with g2 < 0 does."""
    if m[0] != "smooth" or g2 is None or g2 >= 0:
        return None
    g1 = SF.DT_C
    s = (g1 + math.sqrt(g1 * g1 + 4 * abs(g2) * dep)) / (2 * abs(g2))
    return s * s


def node_status(P2, ys, vtop):
    if P2 <= 0:
        return "CLOSED"
    if ys is not None and P2 >= ys:
        return "DEEP"
    if P2 <= vtop:
        return "VERIFIED"
    return "UNDECIDED"


def nodes_for(cols, e):
    """The cover's nodes at e: the throat (x = 0: y_s^th, regular below it at zeroth order) and every column."""
    st = setup(e)
    out = [{"rc": "2", "x": 0.0, "ys": st["ys_th"], "vtop": st["ys_th"], "stable": True, "hold": None}]
    for rc in sorted(RADII, key=lambda v: float(Fr(v))):
        c = cols["%s|%s" % (rc, Fr(e))]
        out.append({"rc": rc, "x": float(Fr(rc)) - 2.0, "ys": c["ys_med"] if c["stable"] else None,
                    "vtop": c["vtop"], "stable": c["stable"],
                    "hold": fmax(c["hold_ys90"]) if c["stable"] else fmax(c["hold_vtop"])})
    return out


def r_f(cols, e):
    """X12's footprint: the largest banked radius whose column is ys_stable."""
    st = [float(Fr(rc)) for rc in BANK_RADII if cols["%s|%s" % (rc, Fr(e))]["stable"]]
    return max(st) if st else None


def cover(cols, e, m, dk, cut_x=None, amp=None):
    """R3: one member at one depth row, continued through every node.  cut_x ends the piece there (R6 b); amp scales
    the member's amplitude (R6 a; power laws only)."""
    st = setup(e)
    row = st["rows"].get(dk)
    if row is None:
        return None
    dep = row["depth"]
    prof, g2 = profile(m, st, dep)
    if prof is None:
        return None
    if amp is not None:
        base = prof
        prof = lambda x, b=base, a=amp: tuple(a * v for v in b(x))
    xm = x_meet(m, dep, g2) if amp is None else None
    if cut_x is not None:
        xm = cut_x if xm is None else min(xm, cut_x)
    nodes = nodes_for(cols, e)
    P2 = lambda x: dep + prof(x)[0]
    ivs, verdict, first_und, ver_to = [], None, None, 0.0
    closed_at = None
    for a, b in zip(nodes, nodes[1:]):
        lo = max(a["x"], 1e-14)
        xs = np.logspace(math.log10(lo), math.log10(b["x"]), GRID_N)
        if xm is not None and xm <= b["x"]:
            closed_at = xm
            ivs.append({"lo": a["rc"], "hi": b["rc"], "status": "CLOSED", "x_meet": xm,
                        "P2max": max(P2(x) for x in xs if x <= xm) if xm > lo else dep})
            break
        p2max = max(P2(x) for x in xs)
        yss = [n["ys"] for n in (a, b) if n["ys"] is not None]
        ys_i = min(yss) if yss else None
        vt_i = min(a["vtop"], b["vtop"])
        s = node_status(p2max, ys_i, vt_i)
        ivs.append({"lo": a["rc"], "hi": b["rc"], "status": s, "P2max": p2max, "ys": ys_i, "vtop": vt_i,
                    "margin_s": None if ys_i is None else ys_i - p2max, "margin_v": vt_i - p2max})
        if s == "DEEP" and verdict is None:
            verdict = ("FAILS", "DEEP", b["rc"])
        if s == "UNDECIDED" and first_und is None:
            first_und = b["rc"]
        if s == "VERIFIED" and first_und is None and verdict is None:
            ver_to = float(Fr(b["rc"]))
    if closed_at is not None and verdict is None:
        # beyond the closing the piece is absent: a located y_s whose column (to 0.9 y_s) lies in J^-(P_c) (R2: its
        # vertical-leg hold below the write's floor) is an uncut singular layer in the crossing's past
        later = [n for n in nodes if n["x"] > closed_at]
        floor = P.write_floor()
        uncut = next((n for n in later if n["ys"] is not None and n["hold"] is not None and n["hold"] < floor), None)
        if uncut is not None:
            verdict = ("FAILS", "UNCUT", uncut["rc"])
    # the throat's own segment: X9 (imported) -- margin to y_s^th over x <= x_valid(d), with its hits
    x9 = row["margins"].get("smooth" if m == ("smooth", "adj") else mname(m)) if amp is None else None
    if verdict is None and x9 is not None and x9 < 0:
        verdict = ("FAILS", "DEEP-THROAT", "2")
    if verdict is None:
        if first_und is not None:
            verdict = ("UNDECIDED", "from", first_und)
        elif closed_at is not None:
            verdict = ("UNDECIDED", "closed, no located y_s beyond", "%.6g" % (2 + closed_at))
        else:
            verdict = ("HOLDS", "verified at every node to", RADII[-1])
    ms = [iv["margin_s"] for iv in ivs if iv.get("margin_s") is not None]
    mv = [iv["margin_v"] for iv in ivs if iv["status"] != "CLOSED"]
    rf = r_f(cols, e)
    to_rf = [iv for iv in ivs if float(Fr(iv["hi"])) <= rf + 1e-12]
    return {"e": str(Fr(e)), "member": mname(m), "depth_key": dk, "depth": dep, "g2": g2,
            "x_meet": xm, "r_meet": None if xm is None else 2 + xm, "x_valid": row["x_valid"], "x9_margin": x9,
            "intervals": ivs, "verdict": verdict, "verified_to": ver_to, "R_F": rf,
            "holds_to_RF": (verdict[0] != "FAILS" and len(to_rf) > 0 and
                            all(iv["status"] == "VERIFIED" for iv in to_rf) and
                            (closed_at is None or closed_at > rf - 2)),
            "margin_s_min": min(ms) if ms else None, "margin_v_min": min(mv) if mv else None}


def nec_queries(e):
    """R4's queries at e: per column, the open point of every member at every depth row."""
    st = setup(e)
    q = {rc: [] for rc in RADII}
    for dk in DEPTH_KEYS:
        row = st["rows"].get(dk)
        if row is None:
            continue
        dep = row["depth"]
        for m in MEMBERS:
            prof, g2 = profile(m, st, dep)
            if prof is None:
                continue
            xm = x_meet(m, dep, g2)
            for rc in RADII:
                x = float(Fr(rc)) - 2.0
                if xm is not None and x >= xm:
                    continue
                F, F1, F2 = prof(x)
                q[rc].append(("%s|%s" % (dk, mname(m)), dep + F, F1, F2))
    return q


def nec_along(cols, e, m, dk):
    """R4: the NEC of the continued member at each open node: values at two orders, settled where both orders agree on
    the sign and the point is verified (P2 <= vtop)."""
    key = "%s|%s" % (dk, mname(m))
    rows = []
    for rc in sorted(RADII, key=lambda v: float(Fr(v))):
        c = cols["%s|%s" % (rc, Fr(e))]
        v = c.get("nec", {}).get(key)
        if v is None:
            continue
        st = setup(e)
        dep = st["rows"][dk]["depth"]
        prof, _ = profile(m, st, dep)
        y = dep + prof(float(Fr(rc)) - 2)[0]
        ver = y <= c["vtop"]
        sr = (v[0][0] > 0) == (v[1][0] > 0)
        sth = (v[0][1] > 0) == (v[1][1] > 0)
        rows.append({"rc": rc, "P2": y, "verified": ver, "nec_r": v[1][0], "nec_th": v[1][1],
                     "settled": ver and sr and sth, "holds": v[1][0] >= 0 and v[1][1] >= 0})
    settled = [z for z in rows if z["settled"]]
    br = next((z["rc"] for z in settled if not z["holds"]), None)
    return {"member": mname(m), "depth_key": dk, "rows": rows, "n_settled": len(settled),
            "n_broken": sum(not z["holds"] for z in settled), "first_broken": br}


def critical(cols, e, dk):
    """R5: c* per power law and g1* for the smooth family (adj, its g2 held) over the throat (X9) and the stable
    columns to R_F."""
    st = setup(e)
    row = st["rows"].get(dk)
    if row is None:
        return None
    dep = row["depth"]
    rf = r_f(cols, e)
    stab = [n for n in nodes_for(cols, e)[1:] if n["ys"] is not None and n["x"] <= rf - 2 + 1e-12]
    out = {}
    for lam in SF.DT_LAMS:
        th = row["c_crit"].get("lam %g" % lam)
        cols_c = min(((n["ys"] - dep) / n["x"]**lam for n in stab), default=None)
        out["lam %g" % lam] = {"throat": th, "columns": cols_c, "cover": min(v for v in (th, cols_c) if v is not None)}
    _, g2 = profile(("smooth", "adj"), st, dep)
    out["smooth adj"] = {"g2": g2, "columns": min(((n["ys"] - dep - g2 * n["x"]) / math.sqrt(n["x"]) for n in stab),
                                                  default=None)}
    return out


# ------------------------------------------------------------------------------------------------ R7 the AdS law
def ads_law():
    """R7 (deduced, sympy): in pure AdS_5 (A = B = e^(-2ey), C = r^2 e^(-2ey)) the radial NEC of y = F(r) is
    F'' <= -e F'^2 exactly (k_t - k_r >= 0 solved for F'').  Control: A = e^(-2ey), B = e^(-ey) (a wrong warp) does not
    give it."""
    y, r, ee, F1, F2 = sp.symbols("y r e F1 F2", real=True)

    def g_of(A, B, C):
        m = {"A": A, "B": B, "C": C, "Ay": sp.diff(A, y), "By": sp.diff(B, y), "Cy": sp.diff(C, y),
             "Ar": sp.diff(A, r), "Br": sp.diff(B, r), "Cr": sp.diff(C, r)}
        Nn = sp.sqrt(1 + F1**2 / B)
        kt = (-m["Ay"] / (2 * A) + F1 * (m["Ar"] / A) / (2 * B)) / Nn
        kx = (F2 - B * m["By"] / (2 * B) - F1 * ((m["Br"] / B) / 2 + 2 * F1 * m["By"] / (2 * B))) / (Nn * (B + F1**2))
        sol = sp.solve(sp.Eq(kt - kx, 0), F2)
        return sp.simplify(sol[0] + ee * F1**2)
    w = sp.exp(-2 * ee * y)
    good = g_of(w, w, r**2 * w)
    bad = g_of(w, sp.exp(-ee * y), r**2 * w)
    return {"residual": str(good), "holds": good == 0, "control_residual_zero": sp.simplify(bad) == 0}


def powerlaw_far_exit(e, lam, c=None):
    """R7 (deduced from the AdS law, F' and F'' of c x^lam): a literal power law meets F'' <= -e F'^2 only while
    x^lam <= (1 - lam)/(e c lam); beyond that x it leaves the NEC class (the B w_r term, negative, only tightens it)."""
    c = SF.DT_C if c is None else c
    ef = float(e)
    if ef == 0:
        return None
    return ((1 - lam) / (ef * c * lam)) ** (1 / lam)


# --------------------------------------------------------------------------------------------------------- compute
def columns(procs=4, cache=None, only=None, keep=False):
    """Every column at every e (or `only`, a list of (rc, es)), with R4's queries.  cache: a pickle of the exact series
    (written when keep=True; read when present, so the series are not re-solved)."""
    have = {}
    if cache and os.path.exists(cache):
        have = pickle.load(open(cache, "rb"))
    jobs = []
    pairs = only or [(rc, str(e)) for e in ES2 for rc in RADII]
    qs = {}
    for rc, es in pairs:
        if es not in qs:
            qs[es] = nec_queries(Fr(es))
        k = "%s|%s" % (rc, es)
        S = have.get(k, {}).get("S") if isinstance(have.get(k), dict) else None
        col = have.get(k, {}).get("col") if (S is not None and isinstance(have.get(k), dict)) else None
        jobs.append((rc, es, qs[es][rc], S, keep, col))
    jobs.sort(key=lambda j: (j[3] is not None, -float(Fr(j[1]))))
    out, series = {}, {}
    if procs > 1 and len(jobs) > 1:
        with Pool(min(procs, len(jobs))) as pool:
            res = pool.map(_job, jobs, chunksize=1)
    else:
        res = [_job(j) for j in jobs]
    for c, S in res:
        k = "%s|%s" % (c["rc"], c["e"])
        out[k] = c
        if S is not None:
            series[k] = {"S": S}
    if keep and cache:
        have.update(series)
        pickle.dump(have, open(cache, "wb"))
    return out


def analyse(cols):
    """R1-R7 from the columns (no series needed)."""
    t0 = time.monotonic()
    floor = P.write_floor()
    res = {"floor": floor, "per_e": {}, "ads": ads_law()}
    for e in ES2:
        es = str(Fr(e))
        st = setup(e)
        nodes = nodes_for(cols, e)
        cl = [cols["%s|%s" % (rc, es)] for rc in RADII]
        holds = [v for v in [fmax(c["hold_vtop"]) for c in cl] + [fmax(c["hold_ys90"]) for c in cl if c["hold_ys90"]]
                 if v is not None]
        pe = {"ys_th": st["ys_th"], "y_star": st["y_star"], "R_F": r_f(cols, e),
              "ceiling": [{"rc": n["rc"], "ys": n["ys"], "vtop": n["vtop"]} for n in nodes],
              "ys_ge_throat": all(n["ys"] >= st["ys_th"] - 1e-9 for n in nodes[1:] if n["ys"] is not None),
              "hold_max": max(holds), "floor_over_hold": floor / max(holds),
              "covers": [], "nec": [], "critical": {}, "far_exit": {}}
        for dk in DEPTH_KEYS:
            for m in MEMBERS:
                c = cover(cols, e, m, dk)
                if c is not None:
                    pe["covers"].append(c)
                    if any(cols["%s|%s" % (rc, es)].get("nec") for rc in RADII):
                        pe["nec"].append(nec_along(cols, e, m, dk))
            cr = critical(cols, e, dk)
            if cr is not None:
                pe["critical"][dk] = cr
        for lam in SF.DT_LAMS:
            pe["far_exit"]["lam %g" % lam] = powerlaw_far_exit(e, lam)
        # R6 controls
        ctrl_pl = None
        cr = pe["critical"].get("tenth", {}).get("lam 0.25")
        if cr:
            amp = CONTROL_AMP * cr["cover"] / SF.DT_C
            ctrl_pl = cover(cols, e, ("pow", 0.25), "tenth", amp=amp)
        holder = next((c for c in pe["covers"] if c["member"] == "smooth near" and c["depth_key"] == "tenth"), None)
        cut = cover(cols, e, ("smooth", "near"), "tenth", cut_x=float(Fr(CUT_RC)) - 2.0)
        pe["controls"] = {"power_law_amp": None if ctrl_pl is None else {"verdict": ctrl_pl["verdict"],
                                                                          "amp_over_c": CONTROL_AMP},
                          "cut_piece": {"verdict": cut["verdict"], "uncut_from": CUT_RC,
                                        "uncut_holder_verdict": holder["verdict"] if holder else None}}
        res["per_e"][es] = pe
    res["crosser"] = {k: v["growth"] for k, v in P.crosser_frame(Fr(1, 8)).items()}
    res["x7_upper_1e10"] = max(P.layer(e, 1e10)["upper"] for e in (Fr(0), Fr(1, 8), Fr(1)))
    if INJECT_KEY:
        res[INJECT_KEY] = 0.0
    res["seconds"] = time.monotonic() - t0
    return res


# ----------------------------------------------------------------------------------------------------------- report
def _v(v, f="%.4g"):
    return "-" if v is None else (f % v)


def report(res, cols):
    o = []
    o.append("r1_cover -- the cover: position 2's piece against y_s(r) over J^-(P_c) through the write")
    o.append("  (computed; deduced; not verified; not seated.  F1: eq. (17) as the plane's metric -- conditional on the "
             "mouth lemma.)")
    o.append("  write floor %.6g clocks (o3_write W3, imported)" % res["floor"])
    o.append("")
    o.append("R1/R2  ceiling and cone per ell (y_s^th; R_F; y_s(r) >= y_s^th at every stable column; largest vertical-"
             "leg hold over all columns; floor/hold)")
    for es, pe in res["per_e"].items():
        o.append("  e=%-5s y_s^th=%.4f R_F=%s ys>=ys_th:%s hold_max=%.3g floor/hold=%.3g" % (
            es, pe["ys_th"], _v(pe["R_F"], "%g"), pe["ys_ge_throat"], pe["hold_max"], pe["floor_over_hold"]))
        o.append("        " + "  ".join("%s:%s/%s" % (c["rc"], _v(c["ys"], "%.3f"), _v(c["vtop"], "%.3f"))
                                       for c in pe["ceiling"]))
    o.append("  X7 (imported): upper budget for layers to 1e10 K_bs within O(x): %.4g clocks" % res["x7_upper_1e10"])
    o.append("")
    o.append("R3  verdict per member and depth row (margin_s: least y_s - P2 at stable nodes; margin_v: least vtop - P2)")
    for es, pe in res["per_e"].items():
        o.append("  e=%s" % es)
        for c in pe["covers"]:
            o.append("    %-9s %-12s d=%.4f  %-34s ver_to=%-6g r_meet=%-8s ms=%-8s mv=%-8s" % (
                c["depth_key"], c["member"], c["depth"], " ".join(str(v) for v in c["verdict"]), c["verified_to"],
                _v(c["r_meet"], "%.4f"), _v(c["margin_s_min"]), _v(c["margin_v_min"])))
    o.append("")
    o.append("R4  NEC along the continuation (settled nodes; first broken radius)")
    for es, pe in res["per_e"].items():
        line = []
        for n in pe["nec"]:
            if n["n_settled"]:
                line.append("%s/%s:%d/%d%s" % (n["depth_key"], n["member"], n["n_broken"], n["n_settled"],
                                                "@" + n["first_broken"] if n["first_broken"] else ""))
        o.append("  e=%s  %s" % (es, "  ".join(line)))
    o.append("")
    o.append("R5  critical amplitudes over the cover to R_F (sampled c = g1 = %.3g)" % SF.DT_C)
    for es, pe in res["per_e"].items():
        o.append("  e=%s  " % es + "  ".join("%s:[%s]" % (dk, " ".join("%s=%s" % (k, _v(v.get("cover", v.get("columns"))))
                                                                     for k, v in cr.items()))
                                            for dk, cr in pe["critical"].items()))
    o.append("")
    o.append("R6  controls: power law at %gx c* (must FAIL); cut piece ended at r = %s (must FAIL)" % (
        CONTROL_AMP, CUT_RC))
    for es, pe in res["per_e"].items():
        c = pe["controls"]
        o.append("  e=%-5s power law: %-30s cut piece: %-30s (uncut holder: %s)" % (
            es, " ".join(map(str, c["power_law_amp"]["verdict"])) if c["power_law_amp"] else "-",
            " ".join(map(str, c["cut_piece"]["verdict"])), " ".join(map(str, c["cut_piece"]["uncut_holder_verdict"] or ()))))
    o.append("  crosser-frame growth at depth 0, x 1e-4 -> 1e-12 (C11b, imported): " +
             ", ".join("%s %.3g" % kv for kv in res["crosser"].items()))
    o.append("")
    o.append("R7  AdS law F'' <= -e F'^2: %s (control wrong warp gives zero residual: %s); literal power law leaves the "
             "NEC class beyond x_max:" % (res["ads"]["holds"], res["ads"]["control_residual_zero"]))
    for es, pe in res["per_e"].items():
        o.append("  e=%-5s " % es + "  ".join("%s:%s" % (k, _v(v, "%.3g")) for k, v in pe["far_exit"].items()))
    return "\n".join(o)


# --------------------------------------------------------------------------------------------------------- selftest
def checks(res, cols, live=None):
    out = []

    def add(cid, name, ok, note=""):
        out.append((cid, name, bool(ok), note))
    pe = res["per_e"]
    # C1 the columns reproduce sim2_bank.json (y_s, stability, vtop) and X12's R_F table
    bank = SF.load_bank()
    worst, n = 0.0, 0
    for k, b in bank["columns"].items():
        c = cols.get(k)
        if c is None:
            continue
        n += 1
        yb = b["ys"] if isinstance(b["ys"], list) else json.loads(b["ys"])
        if len(yb) != len(c["ys"]) or bool(b["ys_stable"] in (True, "True")) != c["stable"]:
            worst = math.inf
            continue
        worst = max([worst, abs(float(b["vtop"]) - c["vtop"])] + [abs(float(u) - v) for u, v in zip(yb, c["ys"])])
    add("C1a", "columns equal sim2_bank.json", n == 117 and worst < 1e-9, "%d columns, worst %.2g" % (n, worst))
    rf = [pe[str(e)]["R_F"] for e in ES2]
    add("C1b", "R_F = X12's table", rf == [2.2, 2.2, 2.2, 2.2, 2.15, 2.2, 2.1, 2.5, 10.0], str(rf))
    add("C1c", "y_s(r) >= y_s^th at every stable column", all(p["ys_ge_throat"] for p in pe.values()))
    # C2 the cone: every hold far below the write's floor; X7's 389.3 imported
    fh = min(p["floor_over_hold"] for p in pe.values())
    add("C2", "every column point to vtop / 0.9 y_s in J^-(P_c) within the floor", fh > 100, "least floor/hold %.4g" % fh)
    add("C2b", "X7's upper budget (imported) 389.3", abs(res["x7_upper_1e10"] - 389.3) < 0.1,
        "%.4g" % res["x7_upper_1e10"])
    # C3 the graph NEC formula equals sim2_facing._graph_k on the throat metric
    add("C3", "graph_k = sim2_facing._graph_k on the throat metric", graph_k_check() < 1e-25,
        "%.2g" % graph_k_check())
    # C4 the AdS law and its control
    add("C4", "AdS: F'' <= -e F'^2 exactly; wrong warp fails", res["ads"]["holds"] and not res["ads"]["control_residual_zero"])
    # C5 controls fail
    pl = [p["controls"]["power_law_amp"] for p in pe.values() if p["controls"]["power_law_amp"]]
    add("C5a", "power law at 2 c*: FAILS at every e", pl and all(c["verdict"][0] == "FAILS" for c in pl),
        str([c["verdict"][1:] for c in pl][:3]))
    cuts = [p["controls"]["cut_piece"] for p in pe.values()]
    add("C5b", "cut piece: FAILS (UNCUT) at every e where the holder does not", all(
        c["verdict"][0] == "FAILS" for c in cuts), str([c["verdict"] for c in cuts][:3]))
    gr = res["crosser"]
    add("C5c", "power laws excluded at the horizon (C11b growth > 1e3; smooth finite)",
        all(gr["lam %g" % l] > 1e3 for l in SF.DT_LAMS) and abs(gr["smooth"]) < 10, str({k: "%.3g" % v for k, v in gr.items()}))
    # C6 Lemma W at the level surface (rho + p_r = nu w_r there): every settled level node at r >= 2.05m breaks the
    # radial NEC (S9: w_r < 0 at 3906 of the 3910 verified sign-settled points at r >= 2.05m or ell <= 2m)
    lw = []
    for p in pe.values():
        for nrow in p["nec"]:
            if nrow["member"] == "level":
                lw += [z for z in nrow["rows"] if z["settled"] and float(Fr(z["rc"])) >= 2.05]
    add("C6", "level surface breaks the radial NEC at every settled node r >= 2.05m (Lemma W)",
        lw and all(z["nec_r"] < 0 for z in lw), "%d settled, %d with rho + p_r < 0" % (
            len(lw), sum(z["nec_r"] < 0 for z in lw)))
    # C7 pins: verdicts unchanged
    if PIN_VERDICTS:
        bad = []
        seen = 0
        for es, p in pe.items():
            for c in p["covers"]:
                k = "%s|%s|%s" % (es, c["depth_key"], c["member"])
                seen += k in PIN_VERDICTS
                if k in PIN_VERDICTS and PIN_VERDICTS[k] != list(map(str, c["verdict"])):
                    bad.append(k)
        add("C7", "verdicts equal the pinned full run", not bad and seen == len(PIN_VERDICTS),
            "%d of %d differ %s" % (len(bad), seen, bad[:3]))
    # C8 address guard
    keys = []

    def walk(o, path=""):
        if isinstance(o, dict):
            for k, v in o.items():
                keys.append(str(k))
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(res)
    hit = [k for k in keys if any(b in k.lower() for b in BANNED_KEYS)]
    add("C8", "no distance/time-like key in the output", not hit, str(hit[:3]))
    # C10 the throat segment is X9's (imported, verified): its 11 failing power-law cases at y* / the band's midpoint
    n11 = sum(1 for e in ES2 for dk in ("y_star", "band_mid") if setup(e)["rows"].get(dk)
              for k, v in setup(e)["rows"][dk]["margins"].items() if k.startswith("lam") and v is not None and v < 0)
    add("C10", "X9's 11 failing power-law cases (imported)", n11 == 11, str(n11))
    if live is not None:
        bad = []
        for k, c in live.items():
            pc = cols.get(k)
            if pc is None:
                bad.append(k)
                continue
            d = max([abs(a - b) for a, b in zip(c["ys"], pc["ys"])] + [abs(c["vtop"] - pc["vtop"])] +
                    [abs(a - b) / max(1, abs(b)) for a, b in zip(c["hold_vtop"], pc["hold_vtop"])
                     if a is not None and b is not None and math.isfinite(a)])
            for q, v in c["nec"].items():
                pv = pc.get("nec", {}).get(q)
                if pv is not None:
                    d = max(d, max(abs(a - b) / max(1e-3, abs(b)) for u, w in zip(v, pv) for a, b in zip(u, w)))
            if d > 1e-6:
                bad.append("%s %.2g" % (k, d))
        add("C9", "live columns equal the pinned/cached ones", not bad, str(bad[:3]))
    return out


def graph_k_check():
    mp.mp.dps = DPS
    e = Fr(1, 8)
    s = P.tb(e)
    worst = mp.mpf(0)
    for dep, xv, F1, F2 in ((0.3, 1e-3, 0.7, -3.0), (1.0, 1e-2, -0.2, 5.0), (0.05, 3e-4, 2.0, 100.0)):
        u = s["sol"].sol(dep)
        al, be, p, q, a1, b1, c1, da, db, dc = (mp.mpf(float(v)) for v in u)
        x = mp.mpf(xv)
        m = {"A": x / 2 * al**2 * (1 + x * a1), "B": al**2 / x**2 * (1 + x * b1), "C": 4 * be**2 * (1 + x * c1)}
        m["Ay"] = 2 * m["A"] * (p + x * da / (2 * (1 + x * a1)))
        m["By"] = 2 * m["B"] * (p + x * db / (2 * (1 + x * b1)))
        m["Cy"] = 2 * m["C"] * (q + x * dc / (2 * (1 + x * c1)))
        m["Ar"] = m["A"] * (1 / x + a1 / (1 + x * a1))
        m["Br"] = m["B"] * (-2 / x + b1 / (1 + x * b1))
        m["Cr"] = m["C"] * (c1 / (1 + x * c1))
        mine = graph_k(m, F1, F2)
        theirs = SF._graph_k(u, xv, F1, F2)
        worst = max([worst] + [abs(a - b) for a, b in zip(mine, theirs)])
    return float(worst)


def pinned_columns():
    """The full run's column summaries (PIN_COLUMNS), as compute() returns them, NEC values for the live columns only."""
    out = {}
    for k, v in PIN_COLUMNS.items():
        ys, stable, vtop, top, hv, h9 = v
        out[k] = {"rc": k.split("|")[0], "r": float(Fr(k.split("|")[0])), "e": k.split("|")[1], "ys": ys,
                  "stable": stable, "ys_med": float(np.median(ys)) if stable else None, "vtop": vtop, "top": top,
                  "hold_vtop": hv, "hold_ys90": h9, "nec": PIN_NEC.get(k, {})}
    return out


def selftest(live=True):
    t0 = time.monotonic()
    cols = pinned_columns()
    lv = None
    if live:
        lv = columns(procs=3, only=[(rc, es) for rc, es in LIVE])
    res = analyse(cols)
    rs = checks(res, cols, lv)
    for cid, name, good, note in rs:
        print("  %s  %s %s  %s" % ("PASS" if good else "FAIL", cid, name, note))
    n = sum(r[2] for r in rs)
    print("selftest %d/%d  (%.1f s)" % (n, len(rs), time.monotonic() - t0))
    return n == len(rs)


# ---------------------------------------------------------------------------------------------------------- mutants
@contextlib.contextmanager
def _patched(target, name, value):
    old = getattr(target, name)
    setattr(target, name, value)
    _SETUP.clear()
    try:
        yield
    finally:
        setattr(target, name, old)
        _SETUP.clear()


_ME = sys.modules[__name__]


def _status_no_deep(P2, ys, vtop):
    s = _ORIG_STATUS(P2, ys, vtop)
    return "VERIFIED" if s == "DEEP" else s


def _no_meet(m, dep, g2):
    return None


def _rf_least(cols, e):
    st = [float(Fr(rc)) for rc in BANK_RADII if cols["%s|%s" % (rc, Fr(e))]["stable"]]
    return min(st) if st else None


_ORIG_STATUS = node_status
INJECT_KEY = None                                # C8's mutation: a key added to the output

MUTANTS = [
    ("C5a", "a piece deeper than y_s read as VERIFIED (DEEP never reported)",
     lambda: _patched(_ME, "node_status", _status_no_deep)),
    ("C5b", "the cut ignored (the cut piece ended at 100m)", lambda: _patched(_ME, "CUT_RC", "100")),
    ("C7", "the smooth family never meets P1", lambda: _patched(_ME, "x_meet", _no_meet)),
    ("C3", "graph_k's F' d_r ln A/(2B) term sign flipped", lambda: _patched(_ME, "graph_k", _graph_k_wrong)),
    ("C6", "the Israel normal flipped (out of the slab)", lambda: _patched(_ME, "NEC_SIGN", -1)),
    ("C2", "the vertical leg integrand 1/sqrt(A) -> 1/A^4 (holds inflated)", lambda: _patched(_ME, "HOLD_POWER", 4.0)),
    ("C5c", "the crosser-frame growth read as 1 (power laws admitted at the horizon)",
     lambda: _patched(P, "crosser_frame", _crosser_wrong)),
    ("C1b", "R_F taken as the least stable radius", lambda: _patched(_ME, "r_f", _rf_least)),
    ("C10", "the sampled amplitude c = 0.05 -> 0.5 (sim2_facing.DT_C)", lambda: _patched(SF, "DT_C", 0.5)),
    ("C8", "a key 'arrival_hold' added to the output", lambda: _patched(_ME, "INJECT_KEY", "arrival_hold")),
]


@contextlib.contextmanager
def _multi(*items):
    with contextlib.ExitStack() as st:
        for t, n, v in items:
            st.enter_context(_patched(t, n, v))
        yield


def _graph_k_wrong(m, F1, F2):
    kt, kx, kq = _ORIG_GRAPH_K(m, -F1, F2)
    return kt, _ORIG_GRAPH_K(m, F1, F2)[1], kq


_ORIG_GRAPH_K = graph_k
_ORIG_CROSSER = P.crosser_frame


def _crosser_wrong(e, xs=(1e-4, 1e-8, 1e-12)):
    out = _ORIG_CROSSER(e, xs)
    return {k: {**v, "growth": 1.0} for k, v in out.items()}


def mutants(cache_cols=None):
    """Each mutant must make its named check (or another) FAIL; the live columns are not re-run under mutation."""
    cols = cache_cols or pinned_columns()
    killed = 0
    for cid, desc, ctx in MUTANTS:
        with ctx():
            try:
                cl = cols
                if getattr(_ME, "HOLD_POWER") != 0.5:              # the holds are recomputed only for the live columns
                    lv = columns(procs=3, only=[LIVE[0]])
                    cl = dict(cols)
                    cl.update(lv)
                if getattr(_ME, "NEC_SIGN") != 1:
                    lv = columns(procs=3, only=list(LIVE))
                    cl = dict(cols)
                    cl.update(lv)
                res = analyse(cl)
                rs = checks(res, cl, None)
                fails = [r[0] for r in rs if not r[2]]
            except Exception as ex:                               # a crash counts as killed
                fails = ["crash: %s" % ex]
        ok = bool(fails)
        killed += ok
        print("  %s  %-5s %s  -> failing: %s" % ("KILLED" if ok else "SURVIVED", cid, desc, fails[:4]))
    print("mutants %d/%d killed" % (killed, len(MUTANTS)))
    return killed == len(MUTANTS)


# ------------------------------------------------------------------------------------------------------------ pins
PIN_COLUMNS = {   # rc|e: [ys (three orders), ys_stable, vtop, top, hold to vtop (two orders), hold to 0.9 y_s or None] -- the full run, 2026-10-09
    '100|0': [[3521.868251899155, 7196.334184684689, 1595.548485557287], False, 10.0, 10.0, [10.101525874, 10.101525874], None],
    '101/50|0': [[2.602171109719, 2.590300702913, 2.600260775645], True, 2.284979156598, 2.470247736863, [30.950618746, 30.950592114], [32.632560007, 32.632424108]],
    '10|0': [[137.470694700202, 233.118203655023, 79.267351316795], False, 10.0, 10.0, [11.182512839, 11.182512839], None],
    '11/5|0': [[2.630284436001, 2.629309090006, 2.629746225769], True, 2.373345968757, 2.498258914481, [8.719762556, 8.719760963], [8.691668642, 8.691667306]],
    '201/100|0': [[2.594143925244, 2.577864337428, 2.592747921304], True, 2.278377235846, 2.463110525238, [44.099390043, 44.099373881], [46.555269111, 46.555205647]],
    '20|0': [[477.417045522158, 659.145310321446, 385.310962394595], False, 10.0, 10.0, [10.541169103, 10.541169103], None],
    '21/10|0': [[2.643676893626, 2.634655845456, 2.64150282923], True, 2.195749226798, 2.509427687769, [11.851107511, 11.851109571], [None, 13.436881775]],
    '23/10|0': [[7.59587991112, 3.906503451477, 4.215117707305], False, 2.28, 2.4, [6.683266765, 6.68326697], None],
    '3|0': [[], False, 3.2, 3.2, [5.599554947, 5.599554934], None],
    '401/200|0': [[2.590439739605, 2.573127468924, 2.589053931296], True, 2.275131142126, 2.459601234731, [62.602230634, 62.602209139], [66.129513092, 66.129430047]],
    '41/20|0': [[2.616112943617, 2.616857605581, 2.615829231738], True, 2.361041931614, 2.485307296436, [20.106523747, 20.10652967], [19.98811779, 19.988122941]],
    '43/20|0': [[2.582401800285, 2.581282314473, 2.582592522214], True, 2.269285582, 2.45328171027, [9.778890795, 9.778897757], [10.091489778, 10.091535247]],
    '4|0': [[28.111362346284], False, 5.7, 5.7, [8.07278526, 8.072785588], None],
    '5/2|0': [[11.868592612502, 15.320021684905, 10.54333024253], False, 2.75, 2.75, [6.34433849, 6.344330422], None],
    '50|0': [[2572.233202597837], False, 10.0, 10.0, [10.206214165, 10.206214165], None],
    '5|0': [[34.317491637506, 70.677783288473], False, 9.55, 9.55, [12.301079706, 12.301090168], None],
    '100|1': [[4.517626903745, 4.52703294286, 4.523678916253], True, 3.437995976352, 4.297494970441, [30.433735759, 30.433667984], [58.203429887, 58.214438776]],
    '101/50|1': [[0.93391550149, 0.933780361129, 0.934217187054], True, 0.865039233255, 0.887219726416, [17.603165911, 17.603150308], [16.186524732, 16.186522853]],
    '10|1': [[2.533836534996, 2.587289137405, 4.665376672505], False, 2.1, 2.1, [8.036570807, 8.036560303], None],
    '11/5|1': [[1.130685595812, 1.056669872436, 1.055927295069], False, 0.9, 0.9, [5.376850331, 5.376849604], None],
    '201/100|1': [[0.928397231477, 0.928265291309, 0.92863249466], True, 0.859927935655, 0.881977369903, [24.766740848, 24.76671982], [22.752707768, 22.752705234]],
    '20|1': [[16890202.183030758], False, 2.65, 2.65, [13.897474327, 13.897468183], None],
    '21/10|1': [[1.000169931238, 1.000085345952, 1.000429025834], True, 0.902653362942, 0.950161434676, [8.118379706, 8.118365705], [8.057330286, 8.057318953]],
    '23/10|1': [[1.490943620137, 1.118628651815, 1.441774046065], False, 0.95, 0.95, [4.77764694, 4.777641806], None],
    '3|1': [[6463.504061845113], False, 1.2, 1.2, [4.129107228, 4.129098444], None],
    '401/200|1': [[0.925782978254, 0.92565423047, 0.925992345654], True, 0.857506483608, 0.879493829341, [34.95227575, 34.952245909], [32.093460953, 32.093457358]],
    '41/20|1': [[0.953207946337, 0.953165649178, 0.953689446568], True, 0.882908860294, 0.90554754902, [11.404581037, 11.404560617], [10.505402806, 10.505400386]],
    '43/20|1': [[1.009600215745, 0.990446653889, 1.051002129279], False, 0.9, 0.9, [6.338486785, 6.338485406], None],
    '4|1': [[2.069301583444, 54.514617530052], False, 1.45, 1.45, [4.672947023, 4.672946306], None],
    '5/2|1': [[1.558246864471, 1.330714427819], False, 1.0, 1.0, [4.036309038, 4.03630761], None],
    '50|1': [[4.014194859749, 3.823736086954, 3.978322267007], True, 2.929039769084, 3.779406153657, [18.077870421, 18.077861199], [35.683597522, 35.814419327]],
    '5|1': [[51682.13356025621, 2.222955065587, 2.634156882091], False, 1.65, 1.65, [5.478344611, 5.478338202], None],
    '100|1/16': [[76.889134433965, 5667.833388674097], False, 10.0, 10.0, [14.032975811, 14.032975811], None],
    '101/50|1/16': [[2.266777314894, 2.264069851729, 2.266828357681], True, 2.045766526692, 2.153438449149, [29.845718031, 29.845702881], [29.648087538, 29.648074835]],
    '10|1/16': [[104.179288267823, 21.137479656576, 209.155219729551], False, 10.0, 10.0, [15.530867316, 15.530867307], None],
    '11/5|1/16': [[2.390779390072, 2.390953083424, 2.390926526264], True, 2.157811189953, 2.27138019995, [8.547905252, 8.547904016], [8.517828258, 8.517827215]],
    '201/100|1/16': [[2.257583890632, 2.255548473781, 2.257957205678], True, 2.037469461296, 2.144704696101, [42.4335645, 42.4335491], [42.146498466, 42.146485529]],
    '20|1/16': [[47.817727932222, 466.892128166293], False, 10.0, 10.0, [14.644212125, 14.644212125], None],
    '21/10|1/16': [[2.352661232272, 2.352551658566, 2.352237767362], True, 2.067304769965, 2.234924075637, [12.272651863, 12.272644173], [12.815128633, 12.815080861]],
    '23/10|1/16': [[6.513277047965, 4.19982352523, 2.851232996681], False, 2.2, 2.2, [6.974188384, 6.974191137], None],
    '3|1/16': [[], False, 3.15, 3.15, [6.096517196, 6.096516306], None],
    '401/200|1/16': [[2.253738045218, 2.251457573277, 2.253956099362], True, 2.033998585809, 2.141051142957, [60.216223885, 60.21619719], [59.804104999, 59.804082571]],
    '41/20|1/16': [[2.300040480658, 2.29706292817, 2.297092236216], True, 2.073125743185, 2.182237624405, [18.611703299, 18.611720358], [18.497083589, 18.497097528]],
    '43/20|1/16': [[2.335007660326, 2.336420261504, 2.33711815468], True, 2.053129304797, 2.219599248429, [9.493293597, 9.493280415], [9.826390978, 9.826353084]],
    '4|1/16': [[14.670145308987, 13.710797973436, 14.851281842724], False, 5.6, 5.6, [9.461424388, 9.461432579], None],
    '5/2|1/16': [[7.381570551087, 7.359583561083, 7.976075910909], False, 2.5, 2.5, [6.260029448, 6.260025049], None],
    '50|1/16': [[2227.301989695193], False, 10.0, 10.0, [14.178428049, 14.178428049], None],
    '5|1/16': [[14.825661428713, 14.481820792271, 15.935295895113], False, 7.35, 7.35, [12.00002676, 12.000054167], None],
    '100|1/2': [[8.454497634785, 8.340627947496, 8.451974619648], True, 6.022031916499, 8.029375888666, [39.010517337, 39.010493064], [88.465651459, 88.741814178]],
    '101/50|1/2': [[1.309067702715, 1.315941348505, 1.296939286152], True, 1.150343243761, 1.243614317579, [19.226726055, 19.226725481], [20.38717585, 20.387172953]],
    '10|1/2': [[188.124870766088], False, 3.65, 3.65, [11.658765059, 11.658776784], None],
    '11/5|1/2': [[1.620499089599, 1.621504917839, 1.624155277689], True, 1.309365221155, 1.540429671947, [6.959839347, 6.959842817], [8.523609183, 8.581767139]],
    '201/100|1/2': [[1.299569877561, 1.302498240189, 1.300874524496], True, 1.174039258357, 1.235830798271, [28.916388307, 28.916384079], [28.705955385, 28.705951913]],
    '20|1/2': [[807.585243039393], False, 4.9, 4.9, [22.39411608, 22.394178262], None],
    '21/10|1/2': [[1.402340657164, 1.400782189629, 1.400352371839], True, 1.230937349137, 1.330743080148, [9.313577045, 9.313578846], [9.845107185, 9.845118938]],
    '23/10|1/2': [[2.145130828816, 1.877572363414, 1.884010832617], False, 1.35, 1.35, [5.806160423, 5.806163184], None],
    '3|1/2': [[2.700613158793, 2.860972663529, 15.006050605333], False, 1.9, 1.9, [5.608372042, 5.60836895], None],
    '401/200|1/2': [[1.296091982867, 1.295887541441, 1.297459411687], True, 1.200505199131, 1.231287383724, [43.897261008, 43.897223771], [40.449560938, 40.449556667]],
    '41/20|1/2': [[1.338601185101, 1.33578121033, 1.332326474193], True, 1.205542542323, 1.268992149813, [13.200400723, 13.200405982], [13.108591271, 13.108595529]],
    '43/20|1/2': [[1.428840589548, 1.427851051748, 1.429419385013], True, 1.221658704063, 1.35739856007, [7.239909066, 7.239909738], [8.009080579, 8.009064182]],
    '4|1/2': [[3.703766691672, 3.647082895062], False, 2.4, 2.4, [6.606948216, 6.606948], None],
    '5/2|1/2': [[2.412955477954, 2.588385235686, 2.467034434615], False, 1.5, 1.5, [5.254645304, 5.254646076], None],
    '50|1/2': [[2761.525908999729], False, 5.45, 5.45, [29.109570513, 29.109625908], None],
    '5|1/2': [[74606.04597306921, 25.313287545855, 7.60909402761], False, 2.75, 2.75, [7.660364587, 7.660355157], None],
    '100|1/32': [[79.846062848848, 80.264333919089], False, 10.0, 10.0, [11.857993844, 11.857993844], None],
    '101/50|1/32': [[2.419351815054, 2.414191804764, 2.419381815403], True, 2.183465013086, 2.298384224301, [31.246561488, 31.246527875], [31.041120724, 31.0410925]],
    '10|1/32': [[3226.53222381736], False, 10.0, 10.0, [13.12651748, 13.12651748], None],
    '11/5|1/32': [[2.505678202227, 2.505355025091, 2.505623786684], True, 2.201816902549, 2.38034259735, [8.364066003, 8.364068438], [8.611987127, 8.61200078]],
    '201/100|1/32': [[2.410784620796, 2.405295724899, 2.410885619282], True, 2.175733120269, 2.290245389756, [44.498847975, 44.498816323], [44.199422111, 44.199395429]],
    '20|1/32': [[95.295635449879, 342.811526481431], False, 10.0, 10.0, [12.374243691, 12.374243691], None],
    '21/10|1/32': [[2.487466383065, 2.486775039891, 2.487466031567], True, 1.890474183991, 2.363092729988, [10.12197527, 10.121975316], [13.121059372, 13.120587343]],
    '23/10|1/32': [[7.208024246545, 3.853987640405], False, 2.3, 2.3, [7.035362086, 7.035365622], None],
    '3|1/32': [[], False, 3.3, 3.3, [6.084482645, 6.084482394], None],
    '401/200|1/32': [[2.406930003017, 2.401138138416, 2.406988586298], True, 2.172254327723, 2.286583502866, [63.17535556, 63.175308927], [62.74525289, 62.745213546]],
    '41/20|1/32': [[2.449420008228, 2.445478210703, 2.446980296861], True, 2.150283935867, 2.324631282018, [18.323002007, 18.323001496], [19.256137577, 19.256135731]],
    '43/20|1/32': [[2.449524614512, 2.441913869782, 2.449508901045], True, 2.094330110394, 2.327033455993, [9.268179449, 9.268181353], [9.94101893, 9.9418691]],
    '4|1/32': [[20.10383156757, 15.066298128577, 20.918913698007], False, 6.05, 6.05, [9.405361341, 9.405385284], None],
    '5/2|1/32': [[9.218476661621, 8.415689430994, 9.814765348297], False, 2.6, 2.6, [6.25683047, 6.256824996], None],
    '50|1/32': [[785370.8181610845], False, 10.0, 10.0, [11.98089114, 11.98089114], None],
    '5|1/32': [[19.003691719025, 20.810509185356], False, 7.35, 7.35, [10.656112309, 10.656113768], None],
    '100|1/4': [[26.221064266797, 3267.42897401182], False, 10.0, 10.0, [45.185196639, 45.18519676], None],
    '101/50|1/4': [[1.691449044103, 1.690410511114, 1.687079492058], True, 1.52559548628, 1.605889985558, [24.322055175, 24.322052259], [24.155432382, 24.15542997]],
    '10|1/4': [[13.337622325681, 22.353287392498, 143.08391061148], False, 6.05, 6.05, [15.826734427, 15.826700835], None],
    '11/5|1/4': [[1.811606744215, 1.93960596732, 1.855250555642], False, 1.65, 1.65, [7.601621678, 7.601621216], None],
    '201/100|1/4': [[1.68408992833, 1.681694174796, 1.682032438236], True, 1.557982545916, 1.597930816324, [36.969677322, 36.969670403], [34.191015394, 34.19101456]],
    '20|1/4': [[758.812855583694], False, 8.3, 8.3, [29.400830755, 29.400776871], None],
    '21/10|1/4': [[1.818638759719, 1.830295458818, 1.820747437965], True, 1.55673905946, 1.729710066067, [10.395194529, 10.395194464], [11.568330245, 11.568328169]],
    '23/10|1/4': [[2.040100704586, 3.26567264396, 3.451058701402], False, 1.65, 1.65, [6.059046989, 6.059045915], None],
    '3|1/4': [[], False, 2.6, 2.6, [6.42546706, 6.425478519], None],
    '401/200|1/4': [[1.67786436012, 1.674446114579, 1.677941116158], True, 1.554121863561, 1.593971142114, [52.343803314, 52.343798928], [48.374451231, 48.374450708]],
    '41/20|1/4': [[1.724164864361, 1.72449742723, 1.725763834723], True, 1.556358928075, 1.638272555868, [15.519854194, 15.519873235], [15.417922064, 15.417939677]],
    '43/20|1/4': [[1.846654273853, 1.839628933672, 1.846891075493], True, 1.622747443148, 1.75432156016, [8.794899667, 8.794891128], [9.176412255, 9.176380189]],
    '4|1/4': [[126.632049592308, 131.259729213274], False, 4.05, 4.05, [9.832801689, 9.832788039], None],
    '5/2|1/4': [[691.110523550895], False, 1.9, 1.9, [5.666691319, 5.666690971], None],
    '50|1/4': [[68530477.99481659], False, 9.35, 9.35, [38.199917053, 38.199916954], None],
    '5|1/4': [[58.511811884998, 131.591959012258], False, 4.0, 4.0, [8.877205084, 8.877205194], None],
    '100|1/8': [[168452319.3684761], False, 10.0, 10.0, [20.125022556, 20.125022556], None],
    '101/50|1/8': [[2.024733743649, 2.023363194313, 2.02473577506], True, 1.875409630055, 1.923497056466, [29.538708354, 29.538664724], [27.399955829, 27.399950063]],
    '10|1/8': [[18.65988716701, 17.830344472744, 21.851067384986], False, 8.8, 8.8, [17.91450954, 17.914510283], None],
    '11/5|1/8': [[2.365920570605, 2.369884972634, 2.373669453862], True, 1.969966883502, 2.251390724003, [8.307374127, 8.307374], [9.241904236, 9.241855965]],
    '201/100|1/8': [[2.014586963364, 2.032076205449, 2.015381764752], True, 1.818882042689, 1.914612676515, [39.135811693, 39.135795344], [38.86786837, 38.867854759]],
    '20|1/8': [[58.852146752197, 39.288698574112, 692.607983234142], False, 10.0, 10.0, [21.002961583, 21.002961583], None],
    '21/10|1/8': [[2.14191191327, 2.141549538755, 2.141967370404], True, 1.882205093786, 2.034816317607, [11.843099468, 11.843093707], [12.411002839, 12.410977717]],
    '23/10|1/8': [[2.552848647227, 4.771550633118, 2.553344908398], False, 1.95, 1.95, [6.532098723, 6.532104968], None],
    '3|1/8': [[], False, 3.0, 3.0, [6.376164156, 6.376174119], None],
    '401/200|1/8': [[2.010509787994, 2.013155176879, 2.011174565999], True, 1.815085045814, 1.910615837699, [55.463646913, 55.463637668], [55.080026789, 55.080019087]],
    '41/20|1/8': [[2.058972918964, 2.057798898616, 2.059095889267], True, 1.760421845714, 1.956024273016, [15.537438357, 15.537435346], [17.275982595, 17.276228342]],
    '43/20|1/8': [[2.154202390486, 2.169937451015, 2.138345694011], True, 1.944167657414, 2.046492270962, [9.726263015, 9.726264531], [9.683545349, 9.683546621]],
    '4|1/8': [[9.317294773079, 9.587950914888], False, 4.6, 4.6, [8.781974194, 8.781973847], None],
    '5/2|1/8': [[5.671350561126, 5.974225095192], False, 2.25, 2.25, [6.025881674, 6.02588641], None],
    '50|1/8': [[27.133372182032, 26.533147052955], False, 10.0, 10.0, [20.333741556, 20.333741556], None],
    '5|1/8': [[63.100386421416], False, 6.05, 6.05, [11.621954569, 11.621954127], None],
    '100|2': [[2.417124183338, 2.417344789751, 2.421941863539], True, 1.722358162698, 2.296477550264, [15.321454875, 15.321468401], [38.675597401, 38.680703888]],
    '101/50|2': [[0.618093047218, 0.623882819299, 0.624184790262], True, 0.548237027459, 0.592688678334, [11.589249897, 11.589249832], [12.361150709, 12.361150387]],
    '10|2': [[4326045.723062754, 1.507898369651, 1.505185933022], False, 1.2, 1.2, [5.621814196, 5.621814074], None],
    '11/5|2': [[0.704411541067, 0.708803574136, 0.704424990638], True, 0.619013460523, 0.669203741106, [4.581345372, 4.581346691], [4.88227392, 4.882282048]],
    '201/100|2': [[0.631792305156, 0.620335462709, 0.62070887055], True, 0.545447919996, 0.589673427023, [16.274358235, 16.274358023], [17.367888955, 17.367887917]],
    '20|2': [[1.848465596835, 1.912595595751, 1.859297093324], True, 1.36890748496, 1.766332238658, [7.62332456, 7.623317384], [None, 14.618106]],
    '21/10|2': [[0.657173697567, 0.65883690661, 0.658112343836], True, 0.593946390312, 0.625206726644, [6.112971108, 6.112980386], [6.065235489, 6.065243054]],
    '23/10|2': [[0.729633129636, 0.730229846672, 0.729802036336], True, 0.658646337794, 0.69331193452, [4.232457455, 4.232461313], [4.203001372, 4.203004539]],
    '3|2': [[30.835597177182], False, 0.75, 0.75, [3.106228209, 3.106228991], None],
    '401/200|2': [[0.624102176454, 0.618616446875, 0.619018310555], True, 0.5439623404, 0.588067395027, [22.925202718, 22.925202346], [24.471288405, 24.471286588]],
    '41/20|2': [[0.633286155404, 0.635465225761, 0.635426551849], True, 0.573472463044, 0.603655224257, [8.111697858, 8.111699017], [8.048378605, 8.048379559]],
    '43/20|2': [[0.687261527358, 0.687333029523, 0.687268988046], True, 0.603937623246, 0.652905538644, [5.072886444, 5.072880087], [5.419959111, 5.419919525]],
    '4|2': [[1.829105713649], False, 0.9, 0.9, [3.635359418, 3.635359923], None],
    '5/2|2': [[0.918326375527, 0.941550506083, 0.949034401891], True, 0.693216560104, 0.894472980779, [3.598359519, 3.598359046], [None, None]],
    '50|2': [[2.160884802883, 2.160547592387, 2.156837233724], True, 1.642016170214, 2.052520212767, [13.108832279, 13.108826782], [24.310595573, 24.435797792]],
    '5|2': [[1.138853090649, 1.22446991014], False, 1.0, 1.0, [4.178449626, 4.178455551], None],
    '100|4': [[1.284392589291, 1.298667428172, 1.30007677342], True, 0.98698724541, 1.233734056763, [12.836700646, 12.836723782], [26.834231437, 26.834965167]],
    '101/50|4': [[0.39726492124, 0.402302373981, 0.392745913078], True, 0.33966150766, 0.377401675178, [8.04943376, 8.049427625], [9.280903571, 9.281066447]],
    '10|4': [[0.866836723883, 0.86812260517, 0.866887287651], True, 0.617657192451, 0.823542923269, [3.030495222, 3.030495154], [6.271362311, 6.214916512]],
    '11/5|4': [[0.437901096373, 0.437906877577, 0.437859345068], True, 0.384805588438, 0.416006041555, [3.36277911, 3.362779632], [3.604328719, 3.604331177]],
    '201/100|4': [[0.395335497714, 0.399961989885, 0.389409027407], True, 0.338011850545, 0.375568722828, [11.280985121, 11.28098005], [13.016067991, 13.016548519]],
    '20|4': [[0.990001912949, 0.987306829271, 0.989369736811], True, 0.798916062475, 0.93990124997, [6.18228046, 6.182266621], [None, None]],
    '21/10|4': [[0.413861784174, 0.411191606064, 0.413288888526], True, 0.353361999689, 0.392624444099, [3.893255654, 3.893256031], [4.472633926, 4.472640221]],
    '23/10|4': [[0.465219553619, 0.46406091835, 0.464640047267], True, 0.397267240413, 0.441408044904, [2.936393958, 2.936393879], [3.408302236, 3.40829947]],
    '3|4': [[0.591775602515, 0.579506523788], False, 0.45, 0.45, [2.248804382, 2.248804606], None],
    '401/200|4': [[0.394379757181, 0.398831883093, 0.387576758408], True, 0.327828173157, 0.374660769322, [14.825224198, 14.825223488], [18.332958245, 18.333103774]],
    '41/20|4': [[0.403227138124, 0.410267627614, 0.401096975117], True, 0.344759203096, 0.383065781217, [5.239096496, 5.239098339], [6.030571157, 6.030601799]],
    '43/20|4': [[0.425415230344, 0.425030525654, 0.425360238669], True, 0.373785309731, 0.404092226736, [3.634210445, 3.63421128], [3.891161436, 3.891165041]],
    '4|4': [[0.717720791928, 0.673193986836, 0.706554704231], False, 0.5, 0.5, [2.286475566, 2.286475764], None],
    '5/2|4': [[0.513185192494, 0.509667465881, 0.513125178642], True, 0.402161858761, 0.48746891971, [2.336771187, 2.336771202], [3.417054801, 3.417261145]],
    '50|4': [[1.161596895346, 1.161160717481, 1.163472566281], True, 0.855225714199, 1.103517050579, [7.552337326, 7.552357246], [16.453556096, 16.46232443]],
    '5|4': [[0.764017722081, 0.750049244122, 0.700441224626], False, 0.5, 0.5, [2.070238022, 2.070238009], None],
}
PIN_NEC = {   # the live columns' NEC queries: depth|member: [[rho + p_r, rho + p_th] per order]
    '11/5|1/8': {'zero|smooth near': [[0.00064542323222, 0.006922160635554], [0.00064542323222, 0.006922160635554]], 'zero|lam 0.1': [[-0.000308289570191, 0.011046796242858], [-0.000308289570191, 0.011046796242858]], 'zero|lam 0.25': [[0.000717387438885, 0.009843117962578], [0.000717387438885, 0.009843117962578]], 'zero|lam 0.4': [[0.000540501010588, 0.008648867410059], [0.000540501010588, 0.008648867410059]], 'tenth|smooth near': [[0.003047698874437, 0.036691002310535], [0.003047698874437, 0.036691002310535]], 'tenth|lam 0.1': [[-0.009582951563845, 0.062280604464943], [-0.009582951563845, 0.062280604464943]], 'tenth|lam 0.25': [[-0.008441171290887, 0.060809959481453], [-0.008441171290887, 0.060809959481453]], 'tenth|lam 0.4': [[-0.008590186077277, 0.059386453979551], [-0.008590186077277, 0.059386453979551]], 'y_star|smooth adj': [[-0.155101801735482, 0.360931469311432], [-0.155101830077296, 0.360931469440267]], 'y_star|smooth near': [[-0.248354792273008, 0.662458722778262], [-0.248354781921047, 0.662458719867178]], 'y_star|level': [[-0.244658623890397, 0.639784137298115], [-0.244658616244018, 0.639784136765416]], 'y_star|lam 0.1': [[-0.270324365578215, 0.667907787588708], [-0.270324346610677, 0.667907783549642]], 'y_star|lam 0.25': [[-0.257582728126148, 0.669096790374826], [-0.257582714199323, 0.669096785899324]], 'y_star|lam 0.4': [[-0.251632194163044, 0.66824785571026], [-0.251632182799554, 0.668247851618685]], 'band_mid|smooth adj': [[-0.384530821608778, 0.474112576833319], [-0.38452974338255, 0.47411356067409]], 'band_mid|smooth near': [[-0.670715718168696, 0.854120078801802], [-0.670682778755648, 0.854133666646519]], 'band_mid|level': [[-0.513333038231853, 0.694679500368674], [-0.513331645779677, 0.694679274213604]], 'band_mid|lam 0.1': [[-0.608903469911117, 0.681268191523594], [-0.608898742585616, 0.681267721072437]], 'band_mid|lam 0.25': [[-0.572329945684718, 0.699417941663457], [-0.57232593623471, 0.69941792008706]], 'band_mid|lam 0.4': [[-0.551259988667433, 0.709480359351535], [-0.551256512996724, 0.709480527657433]]},
    '41/20|1/8': {'zero|smooth near': [[0.000217658259056, 0.006414317932506], [0.000217658259056, 0.006414317932506]], 'zero|lam 0.1': [[0.000737795381647, 0.016686426154066], [0.000737795381647, 0.016686426154066]], 'zero|lam 0.25': [[0.00108527079304, 0.012060818439517], [0.00108527079304, 0.012060818439517]], 'zero|lam 0.4': [[0.000479025076211, 0.008605655784055], [0.000479025076211, 0.008605655784055]], 'tenth|smooth adj': [[0.02171229566008, 0.040504316765501], [0.02171229566008, 0.040504316765501]], 'tenth|smooth near': [[0.000502581996917, 0.084534341331185], [0.000502581996917, 0.084534341331185]], 'tenth|lam 0.1': [[-0.003460690192862, 0.105574168926212], [-0.003460690192862, 0.105574168926212]], 'tenth|lam 0.25': [[-0.00306980683935, 0.100120196071804], [-0.00306980683935, 0.100120196071804]], 'tenth|lam 0.4': [[-0.003701721416789, 0.09610443541504], [-0.003701721416789, 0.09610443541504]], 'y_star|smooth adj': [[-0.001726717383557, 1.440042517131114], [-0.001726812399194, 1.440042417923906]], 'y_star|smooth near': [[-0.035687778392766, 1.73213562514075], [-0.035688218547954, 1.732135164131381]], 'y_star|level': [[-0.041532780627937, 1.678167271241924], [-0.041533096980546, 1.678166940007269]], 'y_star|lam 0.1': [[-0.03213199167479, 1.84293019664021], [-0.032133007440083, 1.842929133021399]], 'y_star|lam 0.25': [[-0.030093842563681, 1.789130590337509], [-0.030094506010949, 1.789129895447823]], 'y_star|lam 0.4': [[-0.033479248187316, 1.753183085295404], [-0.033479754987135, 1.753182554453061]], 'band_mid|smooth adj': [[-0.026744420087144, 2.717129250167136], [-0.027002608162625, 2.716865181972776]], 'band_mid|smooth near': [[-0.036143181559868, 3.635827362426409], [-0.043904833894929, 3.628029972926396]], 'band_mid|level': [[-0.048040670281587, 3.105654242034403], [-0.048866259818075, 3.104815864338386]], 'band_mid|lam 0.1': [[-0.023984941569242, 3.664041163576391], [-0.056005717292794, 3.631972253427167]], 'band_mid|lam 0.25': [[-0.015853470473721, 3.464304027972211], [-0.020719077572005, 3.459408746599816]], 'band_mid|lam 0.4': [[-0.023047253127948, 3.340024542721912], [-0.025346869965445, 3.337703046532999]]},
    '10|4': {'zero|smooth near': [[0.000362867133995, 0.000491377788637], [0.000362867133995, 0.000491377788637]], 'zero|lam 0.1': [[2.8191287306e-05, -3.791690278e-05], [2.8191287306e-05, -3.791690278e-05]], 'zero|lam 0.25': [[0.00017835062415, -0.000257924509904], [0.00017835062415, -0.000257924509904]], 'zero|lam 0.4': [[0.00026274117241, -0.000785152507819], [0.00026274117241, -0.000785152507819]], 'tenth|lam 0.1': [[-5.3022373396e-05, 5.481336557e-06], [-5.3022373396e-05, 5.481336557e-06]], 'tenth|lam 0.25': [[0.000111849853041, -0.000269421369901], [0.000111849853041, -0.000269421369901]], 'tenth|lam 0.4': [[0.000143405991724, -0.000935495971995], [0.000143405991724, -0.000935495971995]], 'y_star|level': [[-0.031621137100123, 0.019651905908992], [-0.031621137100175, 0.019651905908947]], 'y_star|lam 0.1': [[-0.084071951095333, 0.051598897952578], [-0.084071951115249, 0.051598897937463]], 'y_star|lam 0.25': [[-0.117375005327614, 0.069405418768201], [-0.117375005492823, 0.069405418649545]], 'y_star|lam 0.4': [[-0.192193007573402, 0.105215156052866], [-0.192193010406145, 0.105215154196576]], 'band_mid|level': [[-0.031813681109557, 0.019771163077758], [-0.031813681109611, 0.019771163077711]], 'band_mid|lam 0.1': [[-0.084585872488061, 0.051914010520086], [-0.084585872508689, 0.051914010504444]], 'band_mid|lam 0.25': [[-0.118101478724709, 0.06984283814374], [-0.118101478895722, 0.069842838021039]], 'band_mid|lam 0.4': [[-0.193379011695183, 0.10590357984933], [-0.193379014625839, 0.105903577931427]]},
}
PIN_VERDICTS = {   # e|depth|member: the full run's verdict
    '0|band_mid|lam 0.1': ['UNDECIDED', 'from', '21/10'],
    '1/16|band_mid|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/2|band_mid|lam 0.1': ['UNDECIDED', 'from', '401/200'],
    '1/32|band_mid|lam 0.1': ['UNDECIDED', 'from', '21/10'],
    '1/4|band_mid|lam 0.1': ['UNDECIDED', 'from', '401/200'],
    '1/8|band_mid|lam 0.1': ['UNDECIDED', 'from', '41/20'],
    '1|band_mid|lam 0.1': ['FAILS', 'DEEP', '401/200'],
    '2|band_mid|lam 0.1': ['FAILS', 'DEEP', '401/200'],
    '4|band_mid|lam 0.1': ['FAILS', 'DEEP', '401/200'],
    '0|band_mid|lam 0.25': ['UNDECIDED', 'from', '21/10'],
    '1/16|band_mid|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/2|band_mid|lam 0.25': ['UNDECIDED', 'from', '401/200'],
    '1/32|band_mid|lam 0.25': ['UNDECIDED', 'from', '21/10'],
    '1/4|band_mid|lam 0.25': ['UNDECIDED', 'from', '101/50'],
    '1/8|band_mid|lam 0.25': ['UNDECIDED', 'from', '41/20'],
    '1|band_mid|lam 0.25': ['UNDECIDED', 'from', '401/200'],
    '2|band_mid|lam 0.25': ['FAILS', 'DEEP', '401/200'],
    '4|band_mid|lam 0.25': ['FAILS', 'DEEP', '401/200'],
    '0|band_mid|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/16|band_mid|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/2|band_mid|lam 0.4': ['UNDECIDED', 'from', '401/200'],
    '1/32|band_mid|lam 0.4': ['UNDECIDED', 'from', '21/10'],
    '1/4|band_mid|lam 0.4': ['UNDECIDED', 'from', '101/50'],
    '1/8|band_mid|lam 0.4': ['UNDECIDED', 'from', '41/20'],
    '1|band_mid|lam 0.4': ['UNDECIDED', 'from', '401/200'],
    '2|band_mid|lam 0.4': ['FAILS', 'DEEP', '401/200'],
    '4|band_mid|lam 0.4': ['FAILS', 'DEEP', '401/200'],
    '0|band_mid|level': ['HOLDS', 'verified at every node to', '100'],
    '1/16|band_mid|level': ['HOLDS', 'verified at every node to', '100'],
    '1/2|band_mid|level': ['UNDECIDED', 'from', '401/200'],
    '1/32|band_mid|level': ['UNDECIDED', 'from', '21/10'],
    '1/4|band_mid|level': ['UNDECIDED', 'from', '101/50'],
    '1/8|band_mid|level': ['UNDECIDED', 'from', '41/20'],
    '1|band_mid|level': ['UNDECIDED', 'from', '401/200'],
    '2|band_mid|level': ['UNDECIDED', 'from', '401/200'],
    '4|band_mid|level': ['UNDECIDED', 'from', '401/200'],
    '0|band_mid|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '6.22271'],
    '1/16|band_mid|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '5.37575'],
    '1/2|band_mid|smooth adj': ['FAILS', 'UNCUT', '100'],
    '1/32|band_mid|smooth adj': ['UNDECIDED', 'from', '21/10'],
    '1/4|band_mid|smooth adj': ['UNDECIDED', 'from', '101/50'],
    '1/8|band_mid|smooth adj': ['UNDECIDED', 'from', '41/20'],
    '1|band_mid|smooth adj': ['FAILS', 'UNCUT', '50'],
    '2|band_mid|smooth adj': ['FAILS', 'UNCUT', '20'],
    '4|band_mid|smooth adj': ['FAILS', 'UNCUT', '43/20'],
    '0|band_mid|smooth near': ['UNDECIDED', 'from', '21/10'],
    '1/16|band_mid|smooth near': ['UNDECIDED', 'from', '50'],
    '1/2|band_mid|smooth near': ['FAILS', 'DEEP', '100'],
    '1/32|band_mid|smooth near': ['UNDECIDED', 'from', '21/10'],
    '1/4|band_mid|smooth near': ['UNDECIDED', 'from', '101/50'],
    '1/8|band_mid|smooth near': ['UNDECIDED', 'from', '41/20'],
    '1|band_mid|smooth near': ['FAILS', 'DEEP', '50'],
    '2|band_mid|smooth near': ['FAILS', 'UNCUT', '20'],
    '4|band_mid|smooth near': ['FAILS', 'UNCUT', '11/5'],
    '0|d_plus|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/32|d_plus|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '0|d_plus|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/32|d_plus|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '0|d_plus|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/32|d_plus|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '0|d_plus|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1/32|d_plus|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '2.55387'],
    '0|d_plus|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '27'],
    '1/32|d_plus|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '3.51979'],
    '0|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/16|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/2|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/32|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/4|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/8|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '2|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '4|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '0|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/16|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/2|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/32|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/4|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/8|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '2|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '4|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '0|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/16|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/2|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/32|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/4|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/8|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '2|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '4|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '0|tenth|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '2.2237'],
    '1/16|tenth|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '2.2007'],
    '1/2|tenth|smooth adj': ['FAILS', 'UNCUT', '43/20'],
    '1/32|tenth|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '2.21129'],
    '1/4|tenth|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '2.15872'],
    '1/8|tenth|smooth adj': ['FAILS', 'UNCUT', '11/5'],
    '1|tenth|smooth adj': ['FAILS', 'UNCUT', '21/10'],
    '2|tenth|smooth adj': ['FAILS', 'UNCUT', '21/10'],
    '4|tenth|smooth adj': ['FAILS', 'UNCUT', '41/20'],
    '0|tenth|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '3.20632'],
    '1/16|tenth|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '3.20546'],
    '1/2|tenth|smooth near': ['FAILS', 'UNCUT', '100'],
    '1/32|tenth|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '3.20511'],
    '1/4|tenth|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '3.22327'],
    '1/8|tenth|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '3.2092'],
    '1|tenth|smooth near': ['FAILS', 'UNCUT', '50'],
    '2|tenth|smooth near': ['FAILS', 'UNCUT', '20'],
    '4|tenth|smooth near': ['FAILS', 'UNCUT', '10'],
    '0|y_star|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/16|y_star|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/2|y_star|lam 0.1': ['UNDECIDED', 'from', '201/100'],
    '1/32|y_star|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/4|y_star|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/8|y_star|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1|y_star|lam 0.1': ['UNDECIDED', 'from', '401/200'],
    '2|y_star|lam 0.1': ['FAILS', 'DEEP', '401/200'],
    '4|y_star|lam 0.1': ['FAILS', 'DEEP', '401/200'],
    '0|y_star|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/16|y_star|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/2|y_star|lam 0.25': ['UNDECIDED', 'from', '201/100'],
    '1/32|y_star|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/4|y_star|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/8|y_star|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1|y_star|lam 0.25': ['UNDECIDED', 'from', '401/200'],
    '2|y_star|lam 0.25': ['FAILS', 'DEEP', '401/200'],
    '4|y_star|lam 0.25': ['FAILS', 'DEEP', '401/200'],
    '0|y_star|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/16|y_star|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/2|y_star|lam 0.4': ['UNDECIDED', 'from', '201/100'],
    '1/32|y_star|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/4|y_star|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/8|y_star|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1|y_star|lam 0.4': ['UNDECIDED', 'from', '401/200'],
    '2|y_star|lam 0.4': ['FAILS', 'DEEP', '401/200'],
    '4|y_star|lam 0.4': ['FAILS', 'DEEP', '401/200'],
    '0|y_star|level': ['HOLDS', 'verified at every node to', '100'],
    '1/16|y_star|level': ['HOLDS', 'verified at every node to', '100'],
    '1/2|y_star|level': ['UNDECIDED', 'from', '101/50'],
    '1/32|y_star|level': ['HOLDS', 'verified at every node to', '100'],
    '1/4|y_star|level': ['HOLDS', 'verified at every node to', '100'],
    '1/8|y_star|level': ['HOLDS', 'verified at every node to', '100'],
    '1|y_star|level': ['UNDECIDED', 'from', '401/200'],
    '2|y_star|level': ['UNDECIDED', 'from', '401/200'],
    '4|y_star|level': ['UNDECIDED', 'from', '401/200'],
    '0|y_star|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '3.85643'],
    '1/16|y_star|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '3.73553'],
    '1/2|y_star|smooth adj': ['FAILS', 'UNCUT', '100'],
    '1/32|y_star|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '3.79354'],
    '1/4|y_star|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '3.46107'],
    '1/8|y_star|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '3.63171'],
    '1|y_star|smooth adj': ['FAILS', 'UNCUT', '50'],
    '2|y_star|smooth adj': ['FAILS', 'UNCUT', '20'],
    '4|y_star|smooth adj': ['FAILS', 'UNCUT', '11/5'],
    '0|y_star|smooth near': ['HOLDS', 'verified at every node to', '100'],
    '1/16|y_star|smooth near': ['HOLDS', 'verified at every node to', '100'],
    '1/2|y_star|smooth near': ['FAILS', 'UNCUT', '100'],
    '1/32|y_star|smooth near': ['HOLDS', 'verified at every node to', '100'],
    '1/4|y_star|smooth near': ['HOLDS', 'verified at every node to', '100'],
    '1/8|y_star|smooth near': ['HOLDS', 'verified at every node to', '100'],
    '1|y_star|smooth near': ['FAILS', 'UNCUT', '50'],
    '2|y_star|smooth near': ['FAILS', 'UNCUT', '20'],
    '4|y_star|smooth near': ['FAILS', 'UNCUT', '5/2'],
    '0|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/16|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/2|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/32|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/4|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/8|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '2|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '4|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '0|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/16|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/2|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/32|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/4|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/8|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '2|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '4|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '0|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/16|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/2|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/32|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/4|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/8|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '2|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '4|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '0|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1/16|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1/2|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1/32|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1/4|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1/8|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '2|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '4|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '0|zero|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '27'],
    '1/16|zero|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '26.6139'],
    '1/2|zero|smooth near': ['FAILS', 'UNCUT', '100'],
    '1/32|zero|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '26.8058'],
    '1/4|zero|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '25.5078'],
    '1/8|zero|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '26.2367'],
    '1|zero|smooth near': ['FAILS', 'UNCUT', '50'],
    '2|zero|smooth near': ['FAILS', 'UNCUT', '20'],
    '4|zero|smooth near': ['FAILS', 'UNCUT', '50'],
}


# ---------------------------------------------------------------------------------------------------------- cypher
REGIONS = ("T", "C", "B", "F")          # throat to 2.005m; owner columns to R_F; R_F to 10m; the far columns to 100m
CY_COORDS = ["crossable", "throat", "to_RF", "past_RF", "far", "nec"]
CY_TARGET = (1, 2, 2, 2, 2, 1)          # the statement's YES: a crossable member verified everywhere, NEC kept
CY_TARGET_RF = (1, 2, 2, 1, 1, 1)       # the weaker cell: verified to R_F, undecided beyond, NEC kept


def region_of(rc, rf):
    r = float(Fr(rc))
    if r <= 2.005 + 1e-12:
        return "T"
    if r <= rf + 1e-12:
        return "C"
    if r <= 10 + 1e-12:
        return "B"
    return "F"


def regions(c, cols, e):
    """Per region the member's outcome: 0 a failure located there (DEEP, or an uncut located y_s after the piece has
    met P1), 1 undecided (an unverified interval, or the piece absent with no located y_s), 2 verified throughout."""
    rf = c["R_F"]
    out = {k: 2 for k in REGIONS}

    def worse(k, v):
        out[k] = min(out[k], v)
    closed = False
    for iv in c["intervals"]:
        k = region_of(iv["hi"], rf)
        s = iv["status"]
        if s == "DEEP":
            worse(k, 0)
        elif s == "UNDECIDED":
            worse(k, 1)
        elif s == "CLOSED":
            closed = True
            worse(k, 1)
    if closed:
        floor = P.write_floor()
        for n in nodes_for(cols, e):
            if n["x"] > c["x_meet"]:
                k = region_of(n["rc"], rf)
                located = n["ys"] is not None and n["hold"] is not None and n["hold"] < floor
                worse(k, 0 if located else 1)
    if c["verdict"][1] == "DEEP-THROAT":
        worse("T", 0)
    return out


def cypher_cells(res, cols, per_e=False):
    """The board's encoding (H-R1-CYPHER-INDEX, the board's): one cell per (member, depth row) -- or per (member, depth
    row, ell) with per_e -- over CY_COORDS: crossable (1: H-CROSSABLE-HORIZON's classes; 0: the power-law controls),
    the four region outcomes (worst over the ell scan unless per_e), nec (0 if the continued member breaks the NEC at a
    settled node at any ell, else 1)."""
    agg = {}
    for es, pe in res["per_e"].items():
        e = Fr(es)
        necs = {(n["depth_key"], n["member"]): n for n in pe["nec"]}
        for c in pe["covers"]:
            rg = regions(c, cols, e)
            n = necs.get((c["depth_key"], c["member"]))
            nec = 0 if (n is not None and n["n_broken"] > 0) else 1
            cell = [1 if c["member"] in CROSSABLE else 0] + [rg[k] for k in REGIONS] + [nec]
            key = (c["member"], c["depth_key"]) + ((es,) if per_e else ())
            if key in agg:
                agg[key] = [min(a, b) if i else a for i, (a, b) in enumerate(zip(agg[key], cell))]
            else:
                agg[key] = cell
    return agg


def cypher_spec(cells, name, extra=()):
    rows = [list(v) for v in cells.values()] + [list(x) for x in extra]
    return {"name": name, "coordinates": CY_COORDS, "cells": rows,
            "value_order": {"crossable": [0, 1], "throat": [0, 1, 2], "to_RF": [0, 1, 2], "past_RF": [0, 1, 2],
                            "far": [0, 1, 2], "nec": [0, 1]},
            "declared": {"analysis": {"speaks": True, "witness":
                                      "a continuous margin law: y_s(r) - d - c x^lam (power law) and "
                                      "y_s(r) - d - g1 sqrt(x) - g2 x (smooth family), continuous in (r, d, c); the cover "
                                      "holds at a node iff the margin is positive, so the law returns a magnitude "
                                      "(c* = min (y_s - d)/x^lam over the nodes), not a cell decision; y_s(r) is known "
                                      "only at the columns"}}}


def cypher_run(res, outdir, cols=None):
    """Write the index specs and ask each language of roster 1173 whether the target cells are admitted (cypher.py
    imported by path).  CONTROL: the same cells with the target inserted as if computed -- every operator-bearing
    language must then admit it (an encoding that can say YES)."""
    os.makedirs(outdir, exist_ok=True)
    spec = importlib.util.spec_from_file_location("r1cover_cypher", CYPHER_PATH)
    cy = importlib.util.module_from_spec(spec)
    sys.modules["r1cover_cypher"] = cy
    spec.loader.exec_module(cy)
    out = {}
    runs = (("main", cypher_spec(cypher_cells(res, cols), "r1-cover: members x depth rows, worst over ES2"), ()),
            ("control", cypher_spec(cypher_cells(res, cols), "CONTROL: target inserted as computed", [CY_TARGET]), ()),
            ("per_e", cypher_spec(cypher_cells(res, cols, per_e=True), "r1-cover: members x depth rows x ell"), ()))
    for tag, sp_, _ in runs:
        json.dump(sp_, open(os.path.join(outdir, "r1_%s.json" % tag), "w"), indent=1)
        ix = cy.Index(sp_["name"], sp_["coordinates"], sp_["cells"], sp_["value_order"], sp_["declared"])
        r = cy.run(ix, "1173", {"statistics_order": 2, "algebra_budget": 20000})
        enc = lambda t: tuple(ix.code[i][v] if v in ix.code[i] else None for i, v in enumerate(t))
        verdicts = {}
        for lang in cy.ROSTERS["1173"]["languages"]:
            if lang in cy.ADMISSION:
                adm, note = cy.ADMISSION[lang][0](ix, {"statistics_order": 2, "algebra_budget": 20000})
                if adm is None:
                    verdicts[lang] = {"state": "SILENT", "note": note}
                    continue
                row = {"state": "SPEAKS", "E": len(adm) - len(ix.cells)}
                for tname, t in (("target", CY_TARGET), ("target_RF", CY_TARGET_RF)):
                    et = enc(t)
                    row[tname] = ("NO (a value never seen in any cell: STRUCTURAL)" if None in et
                                  else ("YES" if et in adm else "NO"))
                verdicts[lang] = row
            else:
                d = ix.declared.get(lang)
                verdicts[lang] = {"state": "NOT-RUN" if d is None else ("SPEAKS" if d.get("speaks") else "SILENT"),
                                  "note": "" if d is None else d.get("witness", "")}
        r.pop("_verdicts", None)
        out[tag] = {"cells": len(ix.cells), "d": ix.d, "degenerate": r["degenerate"], "verdicts": verdicts,
                    "langclose_holds": r["langclose_holds"], "warnings": r["warnings"]}
        json.dump(out[tag], open(os.path.join(outdir, "r1_%s.out.json" % tag), "w"), indent=1)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--no-live", action="store_true")
    ap.add_argument("--mutants", action="store_true")
    ap.add_argument("--full", action="store_true", help="recompute every column (about 30-45 min on 4 CPUs)")
    ap.add_argument("--cache", default=None, help="pickle of exact series (read; written with --full)")
    ap.add_argument("--procs", type=int, default=4)
    ap.add_argument("--json", default=None)
    ap.add_argument("--cypher", default=None, help="directory for the cypher index specs and outputs")
    a = ap.parse_args(argv)
    if a.selftest:
        return 0 if selftest(live=not a.no_live) else 1
    if a.mutants:
        return 0 if mutants() else 1
    if a.full or a.cache:
        cols = columns(procs=a.procs, cache=a.cache, keep=bool(a.cache))
    else:
        cols = pinned_columns()
    res = analyse(cols)
    print(report(res, cols))
    if a.json:
        json.dump({"res": res, "cols": cols}, open(a.json, "w"), indent=1, default=str)
    if a.cypher:
        if not (a.full or a.cache):
            print("\nnote: pinned columns carry the NEC of the live columns only, so the cypher's nec coordinate is "
                  "partial; run with --cache PATH (the exact series) or --full for the full encoding")
        cy = cypher_run(res, a.cypher, cols)
        for tag, r in cy.items():
            print("\ncypher %s: %d cells, d = %d, degenerate %s, K.langclose %s" % (tag, r["cells"], r["d"],
                                                                                   r["degenerate"], r["langclose_holds"]))
            for lang, v in r["verdicts"].items():
                print("  %-12s %-8s %s" % (lang, v["state"], "  ".join("%s=%s" % (k, v[k]) for k in ("E", "target",
                                                                                                      "target_RF")
                                                                        if k in v) or v.get("note", "")[:90]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
