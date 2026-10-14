#!/usr/bin/env python3
"""r1_cover.py -- B4d / E-PASS: THE COVER (question r1-cover, put under M-RULINGS item 196).  Computed and deduced; checked
once by two separate AI sessions in this project (a refute verifier and an overclaim verifier), findings applied
(lemmas/R1-COVER.md, History); not seated.  First headed "... not verified; not seated" (2026-10-09), with the
headline "No: no sampled member ... keeps y_s out"; that headline over-claimed and is withdrawn (VERDICT below).

THE QUESTION (the board's wording).  With nothing crossing the corridor's horizon (the README held, 195's reading, being
worked) or with a balanced pair (F5, OPEN), the corridor is stationary through the write.  Is the stationary corridor's
bulk regular on the README's causal past over the whole write (>= 2.0e5 clocks): does position 2's piece (172 (1)) keep
the singular depth y_s out of J^-(P_c) across the whole cover -- beyond the throat's O(x) range, out to the footprint
R_F and the far field -- and not only near the throat?  (Existential: "some piece of position 2 in H-CROSSABLE-HORIZON's
classes".  What is computed is a finite sample; see VERDICT.)

M's words used here (verbatim in the rulings file; quoted, never paraphrased as M's):
  161 "my inclination is yes"
  162 (excerpt) "It is and always will be only the size that is needed to hold the object once and at once"
  163 M chose "All together, one whole"
  172 (1) M chose "Yes, it may" to the board's "While the corridor holds, may position 2's piece of our plane carry the
      README's stress (stress that obeys the NEC)?"; (2) M chose "Yes, that is coinciding"; the record: "Not answered:
      which part of position 2's stress is its law"
  174 M chose "For the math" (three times); the strict rule for curvature singularities is the board's decision under 149
  149 "I have given you everything I can. You have to work the math now"
  179/180 "We know the corridor *does not sit on either position's plane, it only bridges them. So one could surmise that
      the corridor is exclusive to the bulk."
  183 M chose "Yes: never violated as a pair"; 187 (3) M chose "Seat both": clause (Z), "null energy never violated"
      holds net along each light ray (183)
  184 "There are no matter free planes"
  194 "Disregard that last ruling. I want that question put to the cypher" (193 withdrawn; not used here)
  195 "The README is not a pair"
  196 "Review all tasks running. Stop any that are no longer relevant. All questions get works through the cypher"
  197 "... - because it sees its own reflection, not the other plane"

CONDITIONS, NAMED (every one the board's unless marked).  F1: these columns take eq. (17) as the plane's own metric (the
board's configuration; the F1 audit, lemmas/F1-AUDIT.md, now carries this input as the theorem M1, OPEN -- every result
here is conditional on it).  Clause (B) in full on P1 (vacuum Lambda_5, RS tension, matter-free: a limit under 184).
H-Z2-PIECES (P2 mirrored, one-sided toward the slab: its Israel stress is the Z2 form; 197 bears on that construction,
and the board's reading of 197 is still to be worked; with position 2's own bulk beyond P2, F1-AUDIT D1 (iii), P2's
stress is not computed).  H-README-ON-P2 (M's 172 (1)).  H-CROSSABLE-HORIZON (adopted under 149 for P2's unanswered law:
the smooth and band classes at the horizon; S7's power laws excluded there and kept as the control).
H-PROFILE-CONTINUED (each sampled member's near-throat formula continued literally beyond x_valid: the only global
continuation computed here; no ruling fixes P2's global shape).  H-QUASI-STATIC-CORRIDOR (stationary bulk through the
write: the question's premise).  H-HOLD-IN-ADVANCED-TIME (X8's frame).  H-README-TEST-EVENT (the README treated as a test
event, SIM1 S3b; 195's record puts that framing with the board, not M; J^-(P_c) as computed does not depend on whether
the README is held or crossing).  H-POINTWISE-NEC-ON-P2 (172 (1)'s "stress that obeys the NEC" read pointwise: P2's own
Israel stress at each settled node; M's seated clause (Z) is net along each light ray, and a pointwise break counts
against (Z) only if nothing pairs it on the same rays -- that pairing is F5, OPEN since 194).  H-CURVATURE-SETTLED (added
after the verification: a located y_s is a C~ Pade pole -- b4d_stage5.nearest_real, "A scale for the depth, not a claim
that the singular point is real" -- and counts as a curvature singularity, where a piece can FAIL, only if the two
verification orders agree on K/K_bs to 1% (b4_static S3's K rule) over a contiguous prefix of depths on which K rises to
at least 100 (S3's mark of a large curvature); k_settled).  Raw Pade as evidence (S9's rule): VERIFIED and "settled" mean
two Pade orders agree (A, B, C to 1e-4; K to 1%) -- a convergence heuristic, not a bound.

  R1 THE CEILING (computed).  y_s(r) on the cover, per ell of ES2: the throat's y_s^th (sim2_facing.throat_bulk, the
     zeroth-order ODE to alpha = 1e-9; a curvature singularity, SIM2-FACING); on each owner column (b4_static.series at
     order 32, sim2_facing.column_w unchanged: the 13 banked radii 2.005m-10m and three far radii 20, 50, 100m) the
     median C~ Pade pole where three orders agree within 5% (ys_stable), and the verified top vtop.  R_F (X12's rule): the
     largest banked radius whose column is ys_stable.  The curvature scan (kscan): K/K_bs at 0.5-0.99 y_s, two orders.
  R2 THE CONE (computed; deduced).  A column point (r, y) reaches P_c by the vertical null leg at fixed r (advanced cost
     int_0^y dy/sqrt(A), raw Pade at two orders), the plane's ingoing null leg (dv = 0 by the definition of v) and the
     plane's horizon generator (v increasing to v_c).  So the advanced hold that places (r, y) in J^-(P_c) is at most
     that integral: to vtop on verified Pade; from vtop to 0.9 y_s on unverified raw Pade.  Only two-order holds place a
     y_s in J^-(P_c) (hold2); near the throat X7's budgets (imported, verified) take over.
  R3 THE MEMBERS CONTINUED (computed).  Depth rows from X9 (sim2_passage.slab_rows, imported): 0 (coinciding), 0.1 y_s,
     d_+ (only at ell = inf and 32m), y*, the band's midpoint.  Members: the smooth family at the adjudication's g2
     (margin CO_MARGIN = 1) and at the NEC margin NEAR_MARGIN = 1e-2 (the board's choice); the level surface (band class,
     only where W1(d) >= 0); the power laws lam = 0.1, 0.25, 0.4 (controls).  One amplitude, c = g1 = 0.05
     (sim2_facing.DT_C).  P2 = d + f(x), x = r - 2m.  Per node: CLOSED (P2 <= 0: the piece has met P1), DEEP (P2 >= y_s at
     a stable column whose y_s is a settled singularity), PAST-POLE (deeper than a located pole that is not settled:
     undecided), VERIFIED (0 < P2 <= vtop), UNDECIDED; between nodes the board's convention (P2's maximum on the interval
     against the lesser ceiling of its two ends; not a bound: y_s is not computed between columns).  After a CLOSED
     interval the piece is absent: a later column whose y_s is a settled singularity with a two-order hold below the floor
     is an UNCUT singular layer (FAILS); a later located pole that is not settled leaves the cover UNDECIDED.
  R4 THE NEC ALONG THE CONTINUATION (computed).  P2's radial and angular NEC (rho + p_r, rho + p_th, Israel with the
     normal into the slab, the Z2 form of H-Z2-PIECES) at each open node, on the owner column, exact in the slope: k_t =
     [-kappa_t + F' d_r ln A / (2B)]/N, k_th likewise with C, k_r = [F'' - B kappa_r - F'(d_r ln B/2 + 2 F' kappa_r)]/(N
     (B + F'^2)) -- the same formula as sim2_facing._graph_k's docstring, here with the owner's A, B, C (checked equal to
     _graph_k on the throat metric).  Pointwise (H-POINTWISE-NEC-ON-P2).
  R5 THE CRITICAL AMPLITUDE (computed).  For each power law, c* over the cover to R_F = min over the throat (X9's c*)
     and the stable columns of (y_s - d)/x^lam; for the smooth family at its sampled g2, g1* = min (y_s - d - g2 x)/sqrt x.
  R6 CONTROLS (computed).  (a) A power law: excluded at the horizon by H-CROSSABLE-HORIZON (C11b: its crosser-frame
     stress diverges; imported), and at twice its c* it must FAIL the cover.  (b) A cut piece: a member that holds,
     ended at r = 2.01m, must FAIL (UNCUT on a settled singularity at every ell).
  R7 THE FAR FIELD (deduced; sympy; OPEN).  The radial NEC only, in pure AdS_5: F'' <= -e F'^2 (so for e > 0 a NEC piece
     far out deepens at most logarithmically in r: e^(eF) at most linear; at ell = inf the law is F'' <= 0 and allows
     linear deepening).  The angular NEC is not part of it, and how near pure AdS_5 the far columns are is not computed.

RESULTS (the full run, 2026-10-09: 144 columns = 16 radii x 9 ell at order 32; re-analysed after the verification with
the curvature scan of the 74 located columns; pinned below; labels as stated).
  R1 (computed).  The 117 banked columns reproduce sim2_bank.json (y_s, stability, vtop; worst 5e-13 after pinning) and
     X12's R_F table exactly: R_F = 2.2, 2.2, 2.2, 2.2, 2.15, 2.2, 2.1, 2.5, 10.0m at ell = inf ... m/4.  y_s(r) >= y_s^th
     at every stable column.  Beyond R_F no y_s is located at ell >= 4m (e <= 1/4) out to 100m.  At ell <= 2m a C~ Pade
     pole is located again in the far field (8.45m at 100m, e = 1/2; 3.98, 4.52m at 50, 100m, e = 1; 1.86, 2.16, 2.42m at
     20, 50, 100m, e = 2; 0.867, 0.989, 1.162, 1.299m at 10, 20, 50, 100m, e = 4).  Curvature: 43 of the 74 located poles
     are settled singularities, all within r <= 2.2m; none of the 10 far poles is (K/K_bs about 1-2 at 0.8 y_s; from 0.85-
     0.9 y_s the two orders part, by factors up to 1.6e5 and sometimes in sign).  At 50m (ell = m) and 20m (ell = m/2) one
     order puts the pole off the real axis (Im 0.129, 0.046).
  R2 (computed; deduced).  Two-order holds: at most 88.74 clocks (e = 1/2, r = 100m, the doublet-free order; the other
     order crosses a Froissart doublet at y = 6.581), floor/hold >= 2250 at every ell.  So every column point down to vtop,
     and on 70 of the 74 located columns down to 0.9 y_s, lies in J^-(P_c) through the write (with X7's 389.3 clocks,
     imported, near the throat).  Two located columns rest on one order (21/10|0, 20|2) and two have none (5/2|2, 20|4):
     CONE_GAPS, never used for UNCUT.
  R3 (computed, on H-PROFILE-CONTINUED).  Shallower than y_s: every crossable member at depth 0, 0.1 y_s and d_+ stays
     shallower than y_s(r) at every node where y_s is located (least y_s - P2 over the shallow rows 2.296m at ell = inf,
     1.534m at 32m on the d_+ row, 0.345m at m/4).
       smooth family at the adjudication's g2 (X9's member): at depth 0 it meets P1 at r = 2.0025m, inside x_valid(0) =
       0.04 (X9 compared P2 with y_s^th only, not with P1: a finding, recorded, not repaired), and FAILS (UNCUT, on a
       settled singularity) at 2.005m at every ell but m/4 (2.15m there).  At 0.1 y_s it meets P1 at 2.047-2.224m and
       FAILS (UNCUT) at e = 1/8, 1/2, 1, 2, 4; UNDECIDED at the other ells.
       smooth family 1e-2 inside its NEC bound: at 0.1 y_s it is verified, with the NEC kept at all 10 settled nodes, to
       r = 3m at every ell -- past R_F at every ell but m/4 (R_F = 10m there: it meets P1 at 3.73m inside the footprint)
       -- then meets P1 at 3.205-3.734m; beyond, UNDECIDED at every ell (nothing located at e <= 1/4; at e >= 1/2 a far
       pole that is not settled).  At depth 0 it is verified to 20m (10m at e = 2, 4), meets P1 at 27.0-13.1m, UNDECIDED
       beyond at every ell.  Its closing at depth 0 is set by the margin (nearer the bound it stays open to 100m: cover()
       HOLDS at margin 1e-3 for ell >= m/2 and at 1e-5 for m/4); at 0.1 y_s by 2 alpha^2 W1(d) < 0 (3.2-4.3m for margins
       1e-2 to 1e-4).
       level surface (band class): verified to 100m at y* for ell >= 4m and at the band's midpoint for ell = inf and 16m,
       but it breaks the radial NEC at every settled node at r >= 2.05m (215 of 215; Lemma W).
       smooth near at y*: verified to 100m at ell >= 4m, breaking the radial NEC at 13-14 of 16 settled nodes.
       deep rows at ell <= 2m: UNDECIDED from the first columns (PAST-POLE or past the verified top), except smooth adj
       at the band's midpoint at m/4 (FAILS, UNCUT at 2.15m).
       power laws (controls): verified to 100m at the shallow rows at every ell, but excluded at the horizon and
       breaking the NEC along the continuation at most settled nodes; at y* and the band's midpoint they FAIL (DEEP at
       2.005m, on settled singularities) in 13 cases at ell <= m.
  R4 (computed).  The literally continued smooth family breaks the angular NEC once it heads back to P1 steeply (e.g.
     0.1 y_s, adjudication's g2: 2 of 7 settled nodes at ell = inf); the NEC-near member at 0.1 y_s keeps both parts at
     every settled node at every ell.
  R5 (computed).  c* over the cover to R_F (shallow rows) runs from about 5.0 (lam 0.4, ell = inf) to 0.36 (m/4), far
     above the sampled 0.05; the columns, not the throat, set it in every shallow case but one.
  R6 (computed).  Both controls FAIL at every ell: the power law at 2 c* (DEEP, at 2.005-2.15m), the cut piece (UNCUT at
     2.02m; 2.15m at m/4).  Ended at 2.05m instead, the cut piece is UNDECIDED at ell = inf (no y_s beyond 2.05m settles
     at the bank's order there; b4_static S2 settles r = 2.15m at order 60-80).  Power laws' crosser-frame growth
     6.3e4-1.6e7 (smooth: 1).
  R7 (deduced; sympy).  As above; a literal power law leaves the radial NEC class beyond x_max = ((1 - lam)/(e c lam))^
     (1/lam), as x = r - 2m (154 for lam 0.4 at m/4, 871 at m/2).  Whether a NEC piece can stay open at bounded depth far
     out is OPEN (not computed).
  VERDICT (on the board's configuration; conditional on F1 / M1, H-Z2-PIECES, H-PROFILE-CONTINUED and
     H-POINTWISE-NEC-ON-P2).  NOT SHOWN: no sampled member, continued literally, is verified across the cover with the
     NEC kept.  The members that keep the NEC close onto P1 and are then UNDECIDED at every ell (no settled singularity is
     located beyond them); the members verified across the whole cover (ell >= 4m) break the NEC; the adjudication's
     member at depth 0 FAILS at the throat's edge at every ell.  Whether any member of H-CROSSABLE-HORIZON's classes keeps
     y_s out of J^-(P_c) across the cover: OPEN.  The sample is six members at five depth rows, one amplitude and two
     margins; a piece shaped otherwise beyond 3m (P2's law is unanswered, 172) is not computed.  The cypher (--cypher)
     classifies the computed cells; its MAIN target is the top of its box, so order, algebra and information admit it by
     construction, and geometry and statistics refuse it because no computed cell keeps the NEC while open or verified
     past the footprint.  Nothing here is a derived physical value.

Owners imported by path (never copied): sim2_passage.py (tb, slab_rows, write_floor, layer, crosser_frame), and through
it sim2_facing.py (column_w, raw_rational, pade_orders, throat_bulk, _ystar, _smooth_g2, _profile, _graph_k, israel,
x_valid, CO_MARGIN, DT_C, DT_LAMS, RADII2, ES2), b4d_stage5.py (warped, evaluator, k_bs), b4_static.py (series);
tools/cypher.py for the cypher (registered in sys.modules before exec_module).  The memo around b4_static.series inside
column() changes no value (one exact solve shared by column_w and the evaluations here).  H-CYPHER-R1-COVER (the
cypher step's encoding, the board's) is carried here; with the curvature gate and the two-order hold switched off it
reproduces the cypher step's cells record for record.
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
CUT_RC = "201/100"                               # R6 (b): the cut piece ends at r = 2.01m (2.05m before the verification;
                                                 # History in R1-COVER.md: at 2.05m no y_s beyond is curvature-settled at
                                                 # ell = inf on the bank's order, so that cut could no longer fail there)
CONTROL_AMP = 2.0                                # R6 (a): the power law at twice its c* over the cover
LIVE = (("41/20", "1/8"), ("11/5", "1/8"), ("10", "4"))     # the selftest's live columns
DPS = 30
GRID_N = 240                                     # P2 sampled per interval (log-spaced in x)
BANNED_KEYS = ("dist", "separation", "time", "redshift", "speed", "velocity", "length", "clock", "arrival")
NEC_SIGN = 1                                     # mutation hook: -1 flips the Israel normal (C6)
HOLD_POWER = 0.5                                 # mutation hook: 1/A**HOLD_POWER in the vertical leg (C3)
K_FRACS = (0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.93, 0.95, 0.97, 0.99)   # the curvature scan's depths, as fractions of y_s
K_TOL = 0.01                                     # b4_static S3's K rule: two Pade orders agree on K to 1%
K_LARGE = 100.0                                  # b4_static S3's mark of a large curvature: the settled K must reach it
CONE_GAPS = ("20|2", "20|4", "21/10|0", "5/2|2")   # located columns whose hold to 0.9 y_s is not finite at both orders
FAR_LOCATED = ("10|4", "100|1", "100|1/2", "100|2", "100|4", "20|2", "20|4", "50|1", "50|2", "50|4")
K_CONTROLS = ("401/200|0", "41/20|0", "401/200|1", "21/10|2")      # near-throat layer columns that must settle (C11)


def mname(m):
    return "level" if m[0] == "level" else ("smooth " + m[1] if m[0] == "smooth" else "lam %g" % m[1])


def fmax(vals):
    """The larger finite value of a two-order pair (None if neither is finite)."""
    v = [x for x in (vals or []) if x is not None and math.isfinite(x)]
    return max(v) if v else None


def hold2(vals):
    """R2's hold, counted for the cone only where both verification orders give a finite value (the larger of the two).
    One-order holds are reported (CONE_GAPS), never used to place a y_s in J^-(P_c)."""
    v = [x for x in (vals or []) if x is not None and math.isfinite(x)]
    return max(v) if len(v) == 2 else None


def k_settled(ks):
    """H-CURVATURE-SETTLED (the board's, from b4_static S2/S3; added after the verification, RF2/RC-O4).  A located y_s is
    a C~ Pade pole -- b4d_stage5.nearest_real: "A scale for the depth, not a claim that the singular point is real".  It
    counts as a curvature singularity, a site where a piece can FAIL (DEEP or UNCUT), only if K/K_bs rises to K_LARGE
    over the contiguous prefix of K_FRACS on which the two verification orders agree on it to K_TOL (S3's 1% K rule),
    positive and not falling.  Returns (settled, depth fraction reached, K/K_bs there)."""
    best, prev = None, None
    for f, a, b in ks or []:
        if a is None or b is None or not (math.isfinite(a) and math.isfinite(b)) or a <= 0 or b <= 0:
            break
        if abs(a - b) / max(a, b) > K_TOL:
            break
        k = max(a, b)
        if prev is not None and k < prev * (1 - min(K_TOL, 1.0)):
            break
        prev, best = k, (f, k)
    return (best is not None and best[1] >= K_LARGE), (best[0] if best else None), (best[1] if best else None)


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


def kscan(S, e, rc, ysm):
    """H-CURVATURE-SETTLED's data: K/K_bs at K_FRACS of the located y_s, at the two verification orders, through the
    owner's b4d_stage5.evaluator (the route sim2_facing.column_w uses for K/K_bs; it removes Froissart doublets)."""
    e = Fr(e)
    W = S5.warped(S, e, N)
    Ks = [S5.evaluator(W, e, o)[0] for o in SF.pade_orders(N, e)[:2]]
    out = []
    for f in K_FRACS:
        y = f * ysm
        kb = S5.k_bs(e, float(Fr(rc)), y)
        row = [f]
        for K in Ks:
            try:
                row.append(float(K(y)) / kb)
            except Exception:                                        # a failed evaluation is not agreement
                row.append(float("nan"))
        out.append(row)
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
           "hold_vtop": hold(S, e, float(col["vtop"])), "hold_ys90": hold(S, e, 0.9 * ysm) if stable else None,
           "kscan": kscan(S, e, rc, ysm) if stable else None}
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
    """The cover's nodes at e: the throat (x = 0: y_s^th, regular below it at zeroth order; a curvature singularity,
    imported: SIM2-FACING, "the AdS2 factor shrinks to zero ... K rises") and every column, with H-CURVATURE-SETTLED's
    verdict on its located y_s (kset) and its two-order hold (hold2)."""
    st = setup(e)
    out = [{"rc": "2", "x": 0.0, "ys": st["ys_th"], "vtop": st["ys_th"], "stable": True, "hold": None, "hold2": None,
            "kset": True}]
    for rc in sorted(RADII, key=lambda v: float(Fr(v))):
        c = cols["%s|%s" % (rc, Fr(e))]
        out.append({"rc": rc, "x": float(Fr(rc)) - 2.0, "ys": c["ys_med"] if c["stable"] else None,
                    "vtop": c["vtop"], "stable": c["stable"],
                    "hold": fmax(c["hold_ys90"]) if c["stable"] else fmax(c["hold_vtop"]),
                    "hold2": hold2(c["hold_ys90"]) if c["stable"] else None,
                    "kset": bool(c["stable"] and k_settled(c.get("kscan"))[0])})
    return out


def uncut_site(n, floor):
    """A column where a piece that has met P1 FAILS (UNCUT): a located y_s that is a settled curvature singularity
    (H-CURVATURE-SETTLED) and whose column, to 0.9 y_s, lies in J^-(P_c) at both orders (R2: hold2 below the floor)."""
    return n["ys"] is not None and n["kset"] and n["hold2"] is not None and n["hold2"] < floor


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
        yss_k = [n["ys"] for n in (a, b) if n["ys"] is not None and n["kset"]]
        ys_i = min(yss) if yss else None
        vt_i = min(a["vtop"], b["vtop"])
        s = node_status(p2max, ys_i, vt_i)
        if s == "DEEP" and not (yss_k and p2max >= min(yss_k)):
            s = "PAST-POLE"              # deeper than a located C~ pole that is not a settled singularity: undecided
        ivs.append({"lo": a["rc"], "hi": b["rc"], "status": s, "P2max": p2max, "ys": ys_i, "vtop": vt_i,
                    "margin_s": None if ys_i is None else ys_i - p2max, "margin_v": vt_i - p2max})
        if s == "DEEP" and verdict is None:
            verdict = ("FAILS", "DEEP", b["rc"])
        if s in ("UNDECIDED", "PAST-POLE") and first_und is None:
            first_und = b["rc"]
        if s == "VERIFIED" and first_und is None and verdict is None:
            ver_to = float(Fr(b["rc"]))
    pole_beyond = None
    if closed_at is not None and verdict is None:
        # beyond the closing the piece is absent: a located y_s that is a settled curvature singularity and whose column
        # (to 0.9 y_s, both orders) lies in J^-(P_c) (R2: its vertical-leg hold below the write's floor) is an uncut
        # singular layer in P_c's past.  A located pole that is not settled leaves the cover UNDECIDED (174 (1)'s record:
        # the strict rule stands for curvature singularities).
        later = [n for n in nodes if n["x"] > closed_at]
        floor = P.write_floor()
        uncut = next((n for n in later if uncut_site(n, floor)), None)
        if uncut is not None:
            verdict = ("FAILS", "UNCUT", uncut["rc"])
        else:
            pole_beyond = next((n["rc"] for n in later if n["ys"] is not None), None)
    # the throat's own segment: X9 (imported) -- margin to y_s^th over x <= x_valid(d), with its hits
    x9 = row["margins"].get("smooth" if m == ("smooth", "adj") else mname(m)) if amp is None else None
    if verdict is None and x9 is not None and x9 < 0:
        verdict = ("FAILS", "DEEP-THROAT", "2")
    if verdict is None:
        if first_und is not None:
            verdict = ("UNDECIDED", "from", first_und)
        elif closed_at is not None and pole_beyond is not None:
            verdict = ("UNDECIDED", "closed, located pole beyond not settled", pole_beyond)
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
    pinned = PIN_NECROWS.get("%s|%s|%s" % (Fr(e), dk, mname(m)))
    for i, rc in enumerate(sorted(RADII, key=lambda v: float(Fr(v)))):
        c = cols["%s|%s" % (rc, Fr(e))]
        v = c.get("nec", {}).get(key)
        if v is None:
            # a pinned column without live NEC values: the full run's per-node summary (PIN_NECROWS; k kept, r radial
            # broken, t angular broken, x both, u unsettled, '-' no open point)
            ch = pinned[i] if pinned else "-"
            if ch == "-":
                continue
            rows.append({"rc": rc, "P2": None, "verified": None, "nec_r": None, "nec_th": None, "pinned": True,
                         "settled": ch != "u", "holds": ch in "ku", "radial_broken": ch in "rx",
                         "angular_broken": ch in "tx"})
            continue
        st = setup(e)
        dep = st["rows"][dk]["depth"]
        prof, _ = profile(m, st, dep)
        y = dep + prof(float(Fr(rc)) - 2)[0]
        ver = y <= c["vtop"]
        sr = (v[0][0] > 0) == (v[1][0] > 0)
        sth = (v[0][1] > 0) == (v[1][1] > 0)
        rows.append({"rc": rc, "P2": y, "verified": ver, "nec_r": v[1][0], "nec_th": v[1][1],
                     "settled": ver and sr and sth, "holds": v[1][0] >= 0 and v[1][1] >= 0,
                     "radial_broken": v[1][0] < 0, "angular_broken": v[1][1] < 0})
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
        h2 = [v for v in [hold2(c["hold_vtop"]) for c in cl] + [hold2(c["hold_ys90"]) for c in cl if c["hold_ys90"]]
              if v is not None]
        pe = {"ys_th": st["ys_th"], "y_star": st["y_star"], "R_F": r_f(cols, e),
              "ceiling": [{"rc": n["rc"], "ys": n["ys"], "vtop": n["vtop"], "kset": n["kset"]} for n in nodes],
              "ys_ge_throat": all(n["ys"] >= st["ys_th"] - 1e-9 for n in nodes[1:] if n["ys"] is not None),
              "hold_max": max(holds), "floor_over_hold": floor / max(holds), "hold2_max": max(h2),
              "cone_gaps": sorted("%s|%s" % (c["rc"], es) for c in cl if c["stable"] and hold2(c["hold_ys90"]) is None),
              "k_settled": sorted("%s|%s" % (n["rc"], es) for n in nodes[1:] if n["kset"]),
              "k_located": sorted("%s|%s" % (n["rc"], es) for n in nodes[1:] if n["ys"] is not None),
              "covers": [], "nec": [], "critical": {}, "far_exit": {}}
        for dk in DEPTH_KEYS:
            for m in MEMBERS:
                c = cover(cols, e, m, dk)
                if c is not None:
                    pe["covers"].append(c)
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
        cut_old = cover(cols, e, ("smooth", "near"), "tenth", cut_x=float(Fr("41/20")) - 2.0)
        pe["controls"] = {"power_law_amp": None if ctrl_pl is None else {"verdict": ctrl_pl["verdict"],
                                                                          "amp_over_c": CONTROL_AMP},
                          "cut_piece": {"verdict": cut["verdict"], "uncut_from": CUT_RC,
                                        "uncut_holder_verdict": holder["verdict"] if holder else None},
                          "cut_piece_at_2.05": {"verdict": cut_old["verdict"]}}
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
    o.append("  (computed; deduced; checked once by two separate AI sessions, findings applied; not seated.  F1: eq. (17) "
             "as the plane's metric -- conditional on M1, OPEN; H-Z2-PIECES; H-CURVATURE-SETTLED.)")
    o.append("  write floor %.6g clocks (o3_write W3, imported)" % res["floor"])
    o.append("")
    o.append("R1/R2  ceiling and cone per ell (y_s^th; R_F; y_s(r) >= y_s^th at every stable column; largest vertical-"
             "leg hold over all columns; floor/hold)")
    for es, pe in res["per_e"].items():
        o.append("  e=%-5s y_s^th=%.4f R_F=%s ys>=ys_th:%s hold_max=%.3g floor/hold=%.3g" % (
            es, pe["ys_th"], _v(pe["R_F"], "%g"), pe["ys_ge_throat"], pe["hold_max"], pe["floor_over_hold"]))
        o.append("        " + "  ".join("%s:%s%s/%s" % (c["rc"], _v(c["ys"], "%.3f"), "*" if c.get("kset") and c["ys"] else "",
                                                     _v(c["vtop"], "%.3f")) for c in pe["ceiling"]))
        o.append("        (* a settled curvature singularity, H-CURVATURE-SETTLED; located %d, settled %d; two-order hold "
                 "missing at %s; largest two-order hold %.3g)" % (len(pe["k_located"]), len(pe["k_settled"]),
                                                                  pe["cone_gaps"] or "none", pe["hold2_max"]))
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
        o.append("  e=%-5s power law: %-30s cut piece: %-30s (cut at 2.05m: %s; uncut holder: %s)" % (
            es, " ".join(map(str, c["power_law_amp"]["verdict"])) if c["power_law_amp"] else "-",
            " ".join(map(str, c["cut_piece"]["verdict"])), " ".join(map(str, c["cut_piece_at_2.05"]["verdict"])),
            " ".join(map(str, c["cut_piece"]["uncut_holder_verdict"] or ()))))
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
    # C2 the cone: every two-order hold far below the write's floor, and the located columns without one are exactly the
    # recorded gaps (so a column used for UNCUT always has both orders); X7's 389.3 imported
    fh = min(res["floor"] / p["hold2_max"] for p in pe.values())
    gaps = sorted(g for p in pe.values() for g in p["cone_gaps"])
    add("C2", "two-order holds (to vtop and to 0.9 y_s) within the floor; the located columns without one are the "
        "recorded four", fh > 100 and gaps == sorted(CONE_GAPS), "least floor/hold %.4g; gaps %s" % (fh, gaps))
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
    add("C5b", "cut piece (ended at r = 2.01m): FAILS (UNCUT, on a settled singularity) at every e", all(
        c["verdict"][:2] == ("FAILS", "UNCUT") for c in cuts), str([c["verdict"] for c in cuts][:3]))
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
    live_lw = [z for z in lw if not z.get("pinned")]
    add("C6", "level surface breaks the radial NEC at every settled node r >= 2.05m (Lemma W; live values where "
        "computed, the full run's summary elsewhere)", lw and all(z["radial_broken"] for z in lw),
        "%d settled (%d live), %d with rho + p_r < 0" % (len(lw), len(live_lw), sum(z["radial_broken"] for z in lw)))
    # C11 H-CURVATURE-SETTLED: the near-throat layer columns (b4_static S2's singular layer) settle -- a rule too strict
    # fails here -- and no far-field located pole settles -- a rule too loose fails here (RF2/RC-O4)
    kset = {k for p in pe.values() for k in p["k_settled"]}
    kloc = {k for p in pe.values() for k in p["k_located"]}
    add("C11", "curvature rule: the near-throat control columns settle; none of the 10 far located poles does; "
        "43 of 74 located settle", all(k in kset for k in K_CONTROLS) and not (kset & set(FAR_LOCATED))
        and set(FAR_LOCATED) <= kloc and (len(kset), len(kloc)) == (43, 74),
        "settled %d of %d; far settled %s; controls %s" % (len(kset), len(kloc), sorted(kset & set(FAR_LOCATED)),
                                                           [k in kset for k in K_CONTROLS]))
    # C12 the cypher on the computed cells (RF1): MAIN's target is the top of its box, so order, algebra and information
    # admit it by construction; geometry and statistics decide; CONTROL-B (inserted) is admitted by all five;
    # NEC-REVERSED makes the target not the top; every state, E and binary equals the pinned run
    try:
        cy = cypher_run(res, None, cols)
        mv = cy["main"]["verdicts"]
        add("C12a", "MAIN's target is the top of its box; order, algebra, information admit it (forced, RF1)",
            cy["main"]["target_is_top"]["target"] and all(mv[L].get("target") == "YES" for L in
                                                          ("order", "algebra", "information")))
        add("C12b", "geometry and statistics refuse MAIN's target; CONTROL-B admitted by all five",
            all(mv[L].get("target", "").startswith("NO") for L in ("geometry", "statistics")) and
            all(cy["control_b"]["verdicts"][L].get("target") == "YES" for L in CY_LANGS))
        add("C12c", "NEC-REVERSED: the target is not the top; all five refuse",
            not cy["nec_reversed"]["target_is_top"]["target"] and
            all(cy["nec_reversed"]["verdicts"][L].get("target", "").startswith("NO") for L in CY_LANGS))
        got = {tag: {"cells": r["cells"], "top": r["target_is_top"],
                     "langs": {L: [v["state"], v["E"]] + [v.get(t) for t in sorted(r["target_is_top"])]
                               for L, v in r["verdicts"].items() if L in CY_LANGS}} for tag, r in cy.items()}
        bad = [t for t in PIN_CYPHER if got.get(t) != PIN_CYPHER[t]]
        add("C12d", "cypher states, E and binaries equal the pinned run (MAIN, CONTROL-A/B, NEC-REVERSED, PER-ELL)",
            PIN_CYPHER and not bad, "differ: %s" % bad)
    except Exception as ex:                                            # a crash is a failure, not a pass
        add("C12", "cypher run", False, "crash: %s" % ex)
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
            # the curvature scan (H-CURVATURE-SETTLED) recomputed live against PIN_KSCAN (6 digits), and its verdict
            if c.get("kscan") is not None or pc.get("kscan") is not None:
                lk, pk = c.get("kscan") or [], pc.get("kscan") or []
                if len(lk) != len(pk):
                    d = math.inf
                for u, w in zip(lk, pk):
                    for a, b in zip(u[1:], w[1:]):
                        if a is None or b is None or not math.isfinite(a) or not math.isfinite(b):
                            d = max(d, 0.0 if (a is None or not math.isfinite(a)) == (b is None or not math.isfinite(b))
                                    else math.inf)
                        else:
                            d = max(d, abs(a - b) / max(1.0, abs(b)) * 1e-2)    # 6 printed digits: 1e-4 relative
                if k_settled(lk)[0] != k_settled(pk)[0]:
                    d = math.inf
            if d > 1e-6:
                bad.append("%s %.2g" % (k, d))
        add("C9", "live columns (summary, holds, NEC, curvature scan) equal the pinned ones", not bad, str(bad[:3]))
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
                  "hold_vtop": hv, "hold_ys90": h9, "nec": PIN_NEC.get(k, {}),
                  "kscan": [[f, a, b] for f, a, b in PIN_KSCAN[k]] if k in PIN_KSCAN else None}
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
    ("C11", "every located C~ pole read as a curvature singularity (a non-singular pole fed to UNCUT)",
     lambda: _multi((_ME, "K_TOL", 1e9), (_ME, "K_LARGE", 0.0))),
    ("C2", "a one-order hold admitted to the cone (fmax for hold2)", lambda: _patched(_ME, "hold2", fmax)),
    ("C12", "a NEC-kept, open, every-zone-verified power-law cell fed to MAIN as if computed",
     lambda: _patched(_ME, "INJECT_CELL", (0, 1, 4, 2, 2, 2, 2, 2))),
    ("C12", "an empty zone written as verified (the near zone at ell = m/4 kept at 2)",
     lambda: _patched(_ME, "EMPTY_ZONE_VERIFIED", True)),
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
PIN_VERDICTS = {   # e|depth|member: the full run's verdict (re-pinned after the verification: H-CURVATURE-SETTLED, two-order holds)
    '0|band_mid|lam 0.1': ['UNDECIDED', 'from', '21/10'],
    '1/32|band_mid|lam 0.1': ['UNDECIDED', 'from', '21/10'],
    '1/16|band_mid|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/8|band_mid|lam 0.1': ['UNDECIDED', 'from', '41/20'],
    '1/4|band_mid|lam 0.1': ['UNDECIDED', 'from', '401/200'],
    '1/2|band_mid|lam 0.1': ['UNDECIDED', 'from', '401/200'],
    '1|band_mid|lam 0.1': ['FAILS', 'DEEP', '401/200'],
    '2|band_mid|lam 0.1': ['FAILS', 'DEEP', '401/200'],
    '4|band_mid|lam 0.1': ['FAILS', 'DEEP', '401/200'],
    '0|d_plus|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/32|d_plus|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '0|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/32|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/16|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/8|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/4|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/2|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '2|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '4|tenth|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '0|y_star|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/32|y_star|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/16|y_star|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/8|y_star|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/4|y_star|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/2|y_star|lam 0.1': ['UNDECIDED', 'from', '201/100'],
    '1|y_star|lam 0.1': ['UNDECIDED', 'from', '401/200'],
    '2|y_star|lam 0.1': ['FAILS', 'DEEP', '401/200'],
    '4|y_star|lam 0.1': ['FAILS', 'DEEP', '401/200'],
    '0|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/32|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/16|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/8|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/4|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1/2|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '1|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '2|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '4|zero|lam 0.1': ['HOLDS', 'verified at every node to', '100'],
    '0|band_mid|lam 0.25': ['UNDECIDED', 'from', '21/10'],
    '1/32|band_mid|lam 0.25': ['UNDECIDED', 'from', '21/10'],
    '1/16|band_mid|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/8|band_mid|lam 0.25': ['UNDECIDED', 'from', '41/20'],
    '1/4|band_mid|lam 0.25': ['UNDECIDED', 'from', '101/50'],
    '1/2|band_mid|lam 0.25': ['UNDECIDED', 'from', '401/200'],
    '1|band_mid|lam 0.25': ['UNDECIDED', 'from', '401/200'],
    '2|band_mid|lam 0.25': ['FAILS', 'DEEP', '401/200'],
    '4|band_mid|lam 0.25': ['FAILS', 'DEEP', '401/200'],
    '0|d_plus|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/32|d_plus|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '0|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/32|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/16|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/8|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/4|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/2|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '2|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '4|tenth|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '0|y_star|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/32|y_star|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/16|y_star|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/8|y_star|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/4|y_star|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/2|y_star|lam 0.25': ['UNDECIDED', 'from', '201/100'],
    '1|y_star|lam 0.25': ['UNDECIDED', 'from', '401/200'],
    '2|y_star|lam 0.25': ['FAILS', 'DEEP', '401/200'],
    '4|y_star|lam 0.25': ['FAILS', 'DEEP', '401/200'],
    '0|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/32|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/16|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/8|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/4|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1/2|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '1|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '2|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '4|zero|lam 0.25': ['HOLDS', 'verified at every node to', '100'],
    '0|band_mid|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/32|band_mid|lam 0.4': ['UNDECIDED', 'from', '21/10'],
    '1/16|band_mid|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/8|band_mid|lam 0.4': ['UNDECIDED', 'from', '41/20'],
    '1/4|band_mid|lam 0.4': ['UNDECIDED', 'from', '101/50'],
    '1/2|band_mid|lam 0.4': ['UNDECIDED', 'from', '401/200'],
    '1|band_mid|lam 0.4': ['UNDECIDED', 'from', '401/200'],
    '2|band_mid|lam 0.4': ['FAILS', 'DEEP', '401/200'],
    '4|band_mid|lam 0.4': ['FAILS', 'DEEP', '401/200'],
    '0|d_plus|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/32|d_plus|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '0|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/32|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/16|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/8|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/4|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/2|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '2|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '4|tenth|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '0|y_star|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/32|y_star|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/16|y_star|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/8|y_star|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/4|y_star|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/2|y_star|lam 0.4': ['UNDECIDED', 'from', '201/100'],
    '1|y_star|lam 0.4': ['UNDECIDED', 'from', '401/200'],
    '2|y_star|lam 0.4': ['FAILS', 'DEEP', '401/200'],
    '4|y_star|lam 0.4': ['FAILS', 'DEEP', '401/200'],
    '0|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/32|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/16|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/8|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/4|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1/2|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '1|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '2|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '4|zero|lam 0.4': ['HOLDS', 'verified at every node to', '100'],
    '0|band_mid|level': ['HOLDS', 'verified at every node to', '100'],
    '1/32|band_mid|level': ['UNDECIDED', 'from', '21/10'],
    '1/16|band_mid|level': ['HOLDS', 'verified at every node to', '100'],
    '1/8|band_mid|level': ['UNDECIDED', 'from', '41/20'],
    '1/4|band_mid|level': ['UNDECIDED', 'from', '101/50'],
    '1/2|band_mid|level': ['UNDECIDED', 'from', '401/200'],
    '1|band_mid|level': ['UNDECIDED', 'from', '401/200'],
    '2|band_mid|level': ['UNDECIDED', 'from', '401/200'],
    '4|band_mid|level': ['UNDECIDED', 'from', '401/200'],
    '0|y_star|level': ['HOLDS', 'verified at every node to', '100'],
    '1/32|y_star|level': ['HOLDS', 'verified at every node to', '100'],
    '1/16|y_star|level': ['HOLDS', 'verified at every node to', '100'],
    '1/8|y_star|level': ['HOLDS', 'verified at every node to', '100'],
    '1/4|y_star|level': ['HOLDS', 'verified at every node to', '100'],
    '1/2|y_star|level': ['UNDECIDED', 'from', '101/50'],
    '1|y_star|level': ['UNDECIDED', 'from', '401/200'],
    '2|y_star|level': ['UNDECIDED', 'from', '401/200'],
    '4|y_star|level': ['UNDECIDED', 'from', '401/200'],
    '0|band_mid|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '6.22271'],
    '1/32|band_mid|smooth adj': ['UNDECIDED', 'from', '21/10'],
    '1/16|band_mid|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '5.37575'],
    '1/8|band_mid|smooth adj': ['UNDECIDED', 'from', '41/20'],
    '1/4|band_mid|smooth adj': ['UNDECIDED', 'from', '101/50'],
    '1/2|band_mid|smooth adj': ['UNDECIDED', 'from', '401/200'],
    '1|band_mid|smooth adj': ['UNDECIDED', 'from', '401/200'],
    '2|band_mid|smooth adj': ['UNDECIDED', 'from', '401/200'],
    '4|band_mid|smooth adj': ['FAILS', 'UNCUT', '43/20'],
    '0|d_plus|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1/32|d_plus|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '2.55387'],
    '0|tenth|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '2.2237'],
    '1/32|tenth|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '2.21129'],
    '1/16|tenth|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '2.2007'],
    '1/8|tenth|smooth adj': ['FAILS', 'UNCUT', '11/5'],
    '1/4|tenth|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '2.15872'],
    '1/2|tenth|smooth adj': ['FAILS', 'UNCUT', '43/20'],
    '1|tenth|smooth adj': ['FAILS', 'UNCUT', '21/10'],
    '2|tenth|smooth adj': ['FAILS', 'UNCUT', '21/10'],
    '4|tenth|smooth adj': ['FAILS', 'UNCUT', '43/20'],
    '0|y_star|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '3.85643'],
    '1/32|y_star|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '3.79354'],
    '1/16|y_star|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '3.73553'],
    '1/8|y_star|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '3.63171'],
    '1/4|y_star|smooth adj': ['UNDECIDED', 'closed, no located y_s beyond', '3.46107'],
    '1/2|y_star|smooth adj': ['UNDECIDED', 'from', '101/50'],
    '1|y_star|smooth adj': ['UNDECIDED', 'from', '401/200'],
    '2|y_star|smooth adj': ['UNDECIDED', 'from', '401/200'],
    '4|y_star|smooth adj': ['UNDECIDED', 'from', '401/200'],
    '0|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1/32|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1/16|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1/8|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1/4|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1/2|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '1|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '2|zero|smooth adj': ['FAILS', 'UNCUT', '401/200'],
    '4|zero|smooth adj': ['FAILS', 'UNCUT', '43/20'],
    '0|band_mid|smooth near': ['UNDECIDED', 'from', '21/10'],
    '1/32|band_mid|smooth near': ['UNDECIDED', 'from', '21/10'],
    '1/16|band_mid|smooth near': ['UNDECIDED', 'from', '50'],
    '1/8|band_mid|smooth near': ['UNDECIDED', 'from', '41/20'],
    '1/4|band_mid|smooth near': ['UNDECIDED', 'from', '101/50'],
    '1/2|band_mid|smooth near': ['UNDECIDED', 'from', '401/200'],
    '1|band_mid|smooth near': ['UNDECIDED', 'from', '401/200'],
    '2|band_mid|smooth near': ['UNDECIDED', 'from', '401/200'],
    '4|band_mid|smooth near': ['UNDECIDED', 'from', '401/200'],
    '0|d_plus|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '27'],
    '1/32|d_plus|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '3.51979'],
    '0|tenth|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '3.20632'],
    '1/32|tenth|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '3.20511'],
    '1/16|tenth|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '3.20546'],
    '1/8|tenth|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '3.2092'],
    '1/4|tenth|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '3.22327'],
    '1/2|tenth|smooth near': ['UNDECIDED', 'closed, located pole beyond not settled', '100'],
    '1|tenth|smooth near': ['UNDECIDED', 'closed, located pole beyond not settled', '50'],
    '2|tenth|smooth near': ['UNDECIDED', 'closed, located pole beyond not settled', '20'],
    '4|tenth|smooth near': ['UNDECIDED', 'closed, located pole beyond not settled', '10'],
    '0|y_star|smooth near': ['HOLDS', 'verified at every node to', '100'],
    '1/32|y_star|smooth near': ['HOLDS', 'verified at every node to', '100'],
    '1/16|y_star|smooth near': ['HOLDS', 'verified at every node to', '100'],
    '1/8|y_star|smooth near': ['HOLDS', 'verified at every node to', '100'],
    '1/4|y_star|smooth near': ['HOLDS', 'verified at every node to', '100'],
    '1/2|y_star|smooth near': ['UNDECIDED', 'from', '101/50'],
    '1|y_star|smooth near': ['UNDECIDED', 'from', '401/200'],
    '2|y_star|smooth near': ['UNDECIDED', 'from', '401/200'],
    '4|y_star|smooth near': ['UNDECIDED', 'from', '401/200'],
    '0|zero|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '27'],
    '1/32|zero|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '26.8058'],
    '1/16|zero|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '26.6139'],
    '1/8|zero|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '26.2367'],
    '1/4|zero|smooth near': ['UNDECIDED', 'closed, no located y_s beyond', '25.5078'],
    '1/2|zero|smooth near': ['UNDECIDED', 'closed, located pole beyond not settled', '100'],
    '1|zero|smooth near': ['UNDECIDED', 'closed, located pole beyond not settled', '50'],
    '2|zero|smooth near': ['UNDECIDED', 'closed, located pole beyond not settled', '20'],
    '4|zero|smooth near': ['UNDECIDED', 'closed, located pole beyond not settled', '20'],
}
PIN_KSCAN = {   # rc|e: [y/y_s, K/K_bs at the two verification orders] (owner b4d_stage5.evaluator; 6 digits)
    '100|1': [[0.5, 0.999934, 0.999251], [0.6, 1.00012, 0.999233], [0.7, 1.0058, 1.00464], [0.8, 1.18374, 1.18232], [0.85, 9.48955, 1.92558], [0.9, 2314400.0, 14.7535], [0.93, 65.3543, 23660.9], [0.95, 53.1807, 855.225], [0.97, 368.153, 1815570.0], [0.99, 48337.4, 21470.7]],
    '100|1/2': [[0.5, 0.999824, 0.999311], [0.6, 1.00031, 0.999943], [0.7, 1.01631, 1.01647], [0.8, 1.37965, 1.39892], [0.85, 2.53408, 2.88207], [0.9, 732.131, 2485.7], [0.93, 197115.0, 1114.77], [0.95, 320.304, 18434.5], [0.97, 498.408, 5409.63], [0.99, 32449.4, 3764960.0]],
    '100|2': [[0.5, 0.999963, 1.00007], [0.6, 1.00002, 1.00015], [0.7, 1.00208, 1.00222], [0.8, 1.08923, 1.08909], [0.85, 1.52405, 1.52813], [0.9, 13.4443, 9.03363], [0.93, 96062.4, 16797300.0], [0.95, -1900830.0, 209.918], [0.97, 216.209, 246.062], [0.99, 21070.0, 20086.5]],
    '100|4': [[0.5, 0.999643, 1.00006], [0.6, 0.999565, 1.00003], [0.7, 1.00045, 1.00094], [0.8, 1.05686, 1.05727], [0.85, 1.40423, 1.39562], [0.9, 10.0368, 7.52123], [0.93, 212597.0, 33005200.0], [0.95, -153.162, -3771960000.0], [0.97, 958.325, 180.892], [0.99, 388558000.0, 15423.2]],
    '101/50|0': [[0.5, 3.9312, 3.93233], [0.6, 7.71021, 7.71363], [0.7, 20.7437, 20.7595], [0.8, 93.275, 93.4365], [0.85, 286.181, 287.163], [0.9, 1508.41, 1524.44], [0.93, 7245.97, 7461.9], [0.95, 36773.6, 39126.1], [0.97, 984217.0, 957020.0], [0.99, 53778000.0, 124070000.0]],
    '101/50|1': [[0.5, 2.20753, 2.20756], [0.6, 3.93938, 3.93987], [0.7, 9.75877, 9.76084], [0.8, 42.9038, 42.9142], [0.85, 133.475, 133.506], [0.9, 718.672, 718.696], [0.93, 3459.38, 3455.93], [0.95, 17067.9, 16988.3], [0.97, 297142.0, 288647.0], [0.99, 19027600.0, -285612000.0]],
    '101/50|1/16': [[0.5, 4.30929, 4.30929], [0.6, 8.07926, 8.07926], [0.7, 20.8936, 20.8936], [0.8, 91.2249, 91.2249], [0.85, 276.705, 276.706], [0.9, 1442.17, 1442.17], [0.93, 6834.92, 6832.57], [0.95, 33832.3, 33733.4], [0.97, 642902.0, 621664.0], [0.99, 109249000.0, 157994000.0]],
    '101/50|1/2': [[0.5, 4.58582, 4.59089], [0.6, 8.24023, 8.25045], [0.7, 19.8578, 19.8783], [0.8, 82.1797, 82.1662], [0.85, 245.741, 245.23], [0.9, 1276.52, 1264.97], [0.93, 6082.58, 5934.71], [0.95, 30305.1, 28783.9], [0.97, 575861.0, 512317.0], [0.99, 103889000.0, -11845300000.0]],
    '101/50|1/32': [[0.5, 4.11287, 4.11257], [0.6, 7.87751, 7.87647], [0.7, 20.7819, 20.7778], [0.8, 92.2489, 92.225], [0.85, 282.044, 281.958], [0.9, 1485.75, 1484.78], [0.93, 7132.71, 7114.57], [0.95, 36078.7, 35361.7], [0.97, 777530.0, 686437.0], [0.99, 64089500.0, 131510000.0]],
    '101/50|1/4': [[0.5, 5.33518, 5.34399], [0.6, 9.3314, 9.34282], [0.7, 22.2773, 22.2977], [0.8, 90.5021, 90.5603], [0.85, 264.911, 265.026], [0.9, 1319.53, 1319.06], [0.93, 5962.03, 5943.05], [0.95, 27557.5, 27241.6], [0.97, 402761.0, 379901.0], [0.99, 2291460000.0, 12247400000.0]],
    '101/50|1/8': [[0.5, 4.72191, 4.72775], [0.6, 8.56619, 8.57611], [0.7, 21.4262, 21.4477], [0.8, 90.9637, 91.0361], [0.85, 272.372, 272.554], [0.9, 1397.88, 1398.45], [0.93, 6517.32, 6514.11], [0.95, 31440.7, 31314.6], [0.97, 533439.0, 516648.0], [0.99, 142911000.0, 402305000.0]],
    '101/50|2': [[0.5, 1.28762, 1.28701], [0.6, 1.85366, 1.85333], [0.7, 3.94295, 3.9436], [0.8, 16.6561, 16.6616], [0.85, 53.3249, 53.3274], [0.9, 305.545, 304.464], [0.93, 1577.85, 1547.47], [0.95, 8642.8, 8106.04], [0.97, 210228.0, 168548.0], [0.99, 142387000000.0, 20466700.0]],
    '101/50|4': [[0.5, 1.07131, 1.07322], [0.6, 1.26646, 1.26566], [0.7, 2.10177, 2.08074], [0.8, 7.66173, 7.41015], [0.85, 24.9227, 23.6503], [0.9, 158.021, 146.521], [0.93, 930.211, 875.735], [0.95, 6073.29, 6564.43], [0.97, 395707.0, 1246320.0], [0.99, 2169570.0, 207161.0]],
    '10|4': [[0.5, 1.00177, 1.00114], [0.6, 1.00793, 1.00615], [0.7, 1.07859, 1.0754], [0.8, 1.97704, 2.00858], [0.85, 7.99482, 9.43852], [0.9, 188418.0, 10452.4], [0.93, 1186660.0, 204.827], [0.95, 5932.52, 270.835], [0.97, 279579.0, 1836.29], [0.99, 84711.3, 1095410.0]],
    '11/5|0': [[0.5, 1.85373, 1.84524], [0.6, 3.33442, 3.29682], [0.7, 8.16337, 7.98383], [0.8, 29.4963, 28.4212], [0.85, 67.3089, 64.7297], [0.9, 150.011, 152.244], [0.93, 204.757, 234.619], [0.95, 17259.3, 17837.4], [0.97, 3544990.0, 3044510.0], [0.99, 8082740.0, 9157760.0]],
    '11/5|1/16': [[0.5, 2.20047, 2.19744], [0.6, 3.94866, 3.9437], [0.7, 9.79416, 9.78441], [0.8, 37.251, 37.2301], [0.85, 89.6666, 89.8782], [0.9, 759.65, 248.869], [0.93, 614.155, 5949.59], [0.95, 10215.5, 16454.1], [0.97, 163586.0, 67327.8], [0.99, 1512020.0, 140753.0]],
    '11/5|1/2': [[0.5, 3.42089, 3.40279], [0.6, 7.76573, 7.69934], [0.7, 31.0998, 30.6232], [0.8, 341.004, 325.497], [0.85, 1840.76, 1026.46], [0.9, 4350360000.0, 4216680.0], [0.93, -335397000.0, -35409.3], [0.95, 10997900.0, -13873.3], [0.97, 167666.0, 48234.9], [0.99, 83910500.0, 4627530.0]],
    '11/5|1/32': [[0.5, 2.02692, 2.01816], [0.6, 3.64315, 3.61566], [0.7, 8.98122, 8.87626], [0.8, 33.2272, 32.8313], [0.85, 77.7213, 78.1406], [0.9, 184.671, 224.16], [0.93, 250.137, 538.007], [0.95, 6009.53, 20205.8], [0.97, 171028.0, 33722400.0], [0.99, 672765.0, 476059.0]],
    '11/5|1/8': [[0.5, 3.11123, 3.11151], [0.6, 6.77115, 6.77176], [0.7, 23.2425, 23.2454], [0.8, 153.679, 153.981], [0.85, 453.287, 499.224], [0.9, 43718.3, 41020.3], [0.93, 54606.5, 57593.7], [0.95, 262966.0, 244682.0], [0.97, 229035000000.0, 1339730000000.0], [0.99, 2912850000.0, 9683360.0]],
    '11/5|2': [[0.5, 1.16268, 1.1633], [0.6, 1.56037, 1.55639], [0.7, 3.26007, 3.22722], [0.8, 16.3873, 16.0468], [0.85, 65.0197, 63.3736], [0.9, 541.903, 526.382], [0.93, 4165.61, 3939.26], [0.95, 43313.9, 37408.0], [0.97, 11958200.0, 3687850.0], [0.99, 4147790.0, 2306050.0]],
    '11/5|4': [[0.5, 1.04106, 1.04081], [0.6, 1.17361, 1.17308], [0.7, 1.80548, 1.80364], [0.8, 6.59687, 6.57751], [0.85, 23.7603, 23.6516], [0.9, 192.015, 195.032], [0.93, 1470.9, 1897.11], [0.95, 106332.0, 53432.6], [0.97, 26289900.0, 10912800.0], [0.99, 1229090.0, 1135770.0]],
    '201/100|0': [[0.5, 4.0075, 4.00737], [0.6, 7.71961, 7.71933], [0.7, 20.358, 20.3572], [0.8, 90.0084, 90.0043], [0.85, 274.986, 274.982], [0.9, 1453.78, 1454.6], [0.93, 7045.07, 7064.28], [0.95, 36377.1, 36548.9], [0.97, 868230.0, 793826.0], [0.99, 32607900.0, 369639000.0]],
    '201/100|1': [[0.5, 2.2718, 2.27182], [0.6, 4.06941, 4.06988], [0.7, 10.0626, 10.0645], [0.8, 43.8803, 43.8896], [0.85, 135.618, 135.644], [0.9, 723.694, 723.695], [0.93, 3456.75, 3453.38], [0.95, 16926.1, 16850.9], [0.97, 291058.0, 283143.0], [0.99, 121305000.0, 126465000.0]],
    '201/100|1/16': [[0.5, 4.41263, 4.41241], [0.6, 8.14461, 8.144], [0.7, 20.6583, 20.6563], [0.8, 88.3456, 88.3357], [0.85, 265.304, 265.272], [0.9, 1369.67, 1369.38], [0.93, 6453.01, 6447.61], [0.95, 31793.6, 31672.0], [0.97, 601334.0, 581790.0], [0.99, 84216700.0, 112738000.0]],
    '201/100|1/2': [[0.5, 4.75878, 4.76072], [0.6, 8.49927, 8.50308], [0.7, 20.2504, 20.2587], [0.8, 82.2654, 82.2881], [0.85, 242.667, 242.692], [0.9, 1234.92, 1233.57], [0.93, 5762.55, 5727.57], [0.95, 27994.9, 27451.9], [0.97, 488246.0, 455180.0], [0.99, 154189000.0, 153956000.0]],
    '201/100|1/32': [[0.5, 4.203, 4.20295], [0.6, 7.91566, 7.91548], [0.7, 20.471, 20.4704], [0.8, 89.1224, 89.1192], [0.85, 270.383, 270.377], [0.9, 1417.57, 1417.75], [0.93, 6805.95, 6808.17], [0.95, 34556.5, 34486.5], [0.97, 745763.0, 707621.0], [0.99, 45512400.0, 80551600.0]],
    '201/100|1/4': [[0.5, 5.5178, 5.51595], [0.6, 9.55759, 9.5546], [0.7, 22.5157, 22.5096], [0.8, 89.9785, 89.9605], [0.85, 260.97, 260.935], [0.9, 1286.28, 1286.56], [0.93, 5754.08, 5763.0], [0.95, 26205.1, 26329.1], [0.97, 366498.0, 370323.0], [0.99, 2956160000.0, 3917500000.0]],
    '201/100|1/8': [[0.5, 4.85691, 4.84307], [0.6, 8.69448, 8.65754], [0.7, 21.3678, 21.2292], [0.8, 88.8593, 87.8441], [0.85, 263.071, 258.493], [0.9, 1332.81, 1289.11], [0.93, 6148.38, 5793.34], [0.95, 29301.5, 26576.7], [0.97, 479840.0, 408714.0], [0.99, 310517000.0, 480064000.0]],
    '201/100|2': [[0.5, 1.30271, 1.30215], [0.6, 1.8933, 1.89235], [0.7, 4.06287, 4.06213], [0.8, 17.1809, 17.2446], [0.85, 54.609, 55.2877], [0.9, 304.342, 317.125], [0.93, 1492.24, 1627.06], [0.95, 7606.6, 8679.94], [0.97, 178545.0, 196876.0], [0.99, 9486100.0, 14727300.0]],
    '201/100|4': [[0.5, 1.07469, 1.07636], [0.6, 1.27724, 1.27638], [0.7, 2.14012, 2.12037], [0.8, 7.87349, 7.63814], [0.85, 25.6817, 24.4913], [0.9, 163.142, 152.748], [0.93, 956.07, 923.438], [0.95, 6021.29, 7107.61], [0.97, 235006.0, 1625140.0], [0.99, 40650400.0, 198774.0]],
    '20|2': [[0.5, 0.999765, 0.998213], [0.6, 1.00393, 1.001], [0.7, 1.06599, 1.06018], [0.8, 1.94941, 1.964], [0.85, 1181.55, 7.19513], [0.9, 8182.97, 6410.71], [0.93, 12570.6, 5839.33], [0.95, 6119.53, 33713.5], [0.97, 2080.36, 248.856], [0.99, 2036010.0, 285.906]],
    '20|4': [[0.5, 1.00103, 1.00149], [0.6, 1.00241, 1.00295], [0.7, 1.01915, 1.01985], [0.8, 1.31077, 1.3146], [0.85, 39.7565, 5.49778], [0.9, 49.1121, 91.6515], [0.93, 22944.9, 11622.6], [0.95, 1364.12, 691.923], [0.97, 9509040.0, 6252.89], [0.99, 36973.2, 126356.0]],
    '21/10|0': [[0.5, 2.99998, 3.01323], [0.6, 6.33659, 6.37923], [0.7, 19.301, 19.5063], [0.8, 103.796, 105.932], [0.85, 352.065, 364.514], [0.9, 1911.15, 2095.27], [0.93, 7929.95, 10476.5], [0.95, 33934.5, 67173.8], [0.97, 776453.0, 6326570.0], [0.99, 344258000.0, 1209430000.0]],
    '21/10|1': [[0.5, 1.9019, 1.90083], [0.6, 3.39185, 3.39188], [0.7, 9.04456, 9.05165], [0.8, 48.7982, 48.8948], [0.85, 185.292, 185.86], [0.9, 1457.29, 1462.92], [0.93, 11503.0, 11446.8], [0.95, 122039.0, 114131.0], [0.97, 52840800000.0, 775670000.0], [0.99, 14308900.0, 1317340000.0]],
    '21/10|1/16': [[0.5, 3.38597, 3.39067], [0.6, 6.90529, 6.92241], [0.7, 20.5714, 20.6565], [0.8, 112.465, 113.308], [0.85, 402.433, 406.961], [0.9, 2591.98, 2640.51], [0.93, 13562.0, 13789.4], [0.95, 60744.7, 57639.2], [0.97, 3664730.0, 2730900.0], [0.99, 127508000.0, 60119800.0]],
    '21/10|1/2': [[0.5, 3.64272, 3.64737], [0.6, 6.91169, 6.92374], [0.7, 18.7969, 18.8413], [0.8, 98.5967, 98.9337], [0.85, 364.026, 365.779], [0.9, 2743.85, 2775.25], [0.93, 19514.5, 20274.7], [0.95, 157241.0, 166241.0], [0.97, 174776000.0, 12487900.0], [0.99, 159807000.0, 677562000.0]],
    '21/10|1/32': [[0.5, 3.1957, 3.19173], [0.6, 6.63188, 6.62322], [0.7, 20.0002, 19.9805], [0.8, 108.842, 108.867], [0.85, 381.038, 381.694], [0.9, 2274.02, 2263.53], [0.93, 10462.1, 9153.9], [0.95, 42771.9, 760781.0], [0.97, 833836.0, 2454480.0], [0.99, 349272000000.0, 467613000000.0]],
    '21/10|1/4': [[0.5, 4.4066, 4.41835], [0.6, 8.57524, 8.60049], [0.7, 24.8664, 24.9241], [0.8, 145.18, 145.133], [0.85, 593.674, 592.209], [0.9, 5580.6, 5579.08], [0.93, 54177.5, 55177.2], [0.95, 594968.0, 595919.0], [0.97, 34930600000.0, 100075000000000.0], [0.99, 17089100.0, 5238930.0]],
    '21/10|1/8': [[0.5, 3.82607, 3.84045], [0.6, 7.68565, 7.72685], [0.7, 22.8937, 23.0716], [0.8, 131.482, 133.173], [0.85, 508.765, 518.556], [0.9, 4025.89, 4185.88], [0.93, 28957.4, 32004.6], [0.95, 325096.0, 284804.0], [0.97, 4102920000000000.0, 7081350000000.0], [0.99, 242965000.0, 1207890000.0]],
    '21/10|2': [[0.5, 1.21295, 1.21298], [0.6, 1.6725, 1.67261], [0.7, 3.4808, 3.48145], [0.8, 15.6098, 15.6178], [0.85, 54.3486, 54.3976], [0.9, 364.698, 365.579], [0.93, 2280.05, 2292.08], [0.95, 16769.8, 16645.8], [0.97, 2013330.0, 1497100.0], [0.99, 5158720.0, 3978600000.0]],
    '21/10|4': [[0.5, 1.05162, 1.0518], [0.6, 1.20348, 1.20363], [0.7, 1.87789, 1.87813], [0.8, 6.46083, 6.46491], [0.85, 20.814, 20.857], [0.9, 132.284, 133.753], [0.93, 787.53, 819.547], [0.95, 5404.38, 6014.01], [0.97, 1065770.0, 1203580.0], [0.99, 859629.0, 19238300.0]],
    '23/10|2': [[0.5, 1.11397, 1.11394], [0.6, 1.39038, 1.39024], [0.7, 2.5094, 2.50913], [0.8, 9.90258, 9.93749], [0.85, 32.0651, 32.6997], [0.9, 179.694, 224.87], [0.93, 377.045, 975.834], [0.95, 1556870.0, 5328.51], [0.97, 89222.1, 64338.0], [0.99, 1640780.0, 955024.0]],
    '23/10|4': [[0.5, 1.03639, 1.03731], [0.6, 1.1661, 1.16731], [0.7, 1.83617, 1.83869], [0.8, 7.77307, 7.8119], [0.85, 33.8763, 34.425], [0.9, 401.749, 447.127], [0.93, 5972.79, 11097.7], [0.95, 481394000000.0, 178691000000.0], [0.97, -50025700.0, 965008.0], [0.99, 1939380.0, 2681220.0]],
    '401/200|0': [[0.5, 4.042, 4.042], [0.6, 7.71544, 7.71544], [0.7, 20.1535, 20.1535], [0.8, 88.4322, 88.433], [0.85, 269.672, 269.698], [0.9, 1426.93, 1428.6], [0.93, 6940.16, 6977.54], [0.95, 36108.1, 36550.7], [0.97, 894190.0, 849769.0], [0.99, 26606100.0, 511102000.0]],
    '401/200|1': [[0.5, 2.30623, 2.30629], [0.6, 4.13898, 4.13954], [0.7, 10.2272, 10.2293], [0.8, 44.4474, 44.4567], [0.85, 137.028, 137.053], [0.9, 729.089, 729.076], [0.93, 3476.03, 3472.56], [0.95, 17005.4, 16929.4], [0.97, 293816.0, 285768.0], [0.99, 117140000.0, 141753000.0]],
    '401/200|1/16': [[0.5, 4.46491, 4.46498], [0.6, 8.17986, 8.18008], [0.7, 20.5719, 20.5726], [0.8, 87.3006, 87.3044], [0.85, 261.498, 261.508], [0.9, 1349.53, 1349.41], [0.93, 6374.16, 6367.94], [0.95, 31600.6, 31435.9], [0.97, 619779.0, 591272.0], [0.99, 63134500.0, 88920900.0]],
    '401/200|1/2': [[0.5, 4.83889, 4.83889], [0.6, 8.60325, 8.60325], [0.7, 20.3367, 20.3367], [0.8, 81.5294, 81.5295], [0.85, 237.891, 237.889], [0.9, 1187.26, 1187.03], [0.93, 5405.02, 5397.96], [0.95, 25339.1, 25199.2], [0.97, 394841.0, 381520.0], [0.99, 402550000.0, 591598000.0]],
    '401/200|1/32': [[0.5, 4.24656, 4.24658], [0.6, 7.93164, 7.93168], [0.7, 20.3257, 20.3258], [0.8, 87.7922, 87.7927], [0.85, 265.694, 265.7], [0.9, 1392.75, 1393.06], [0.93, 6704.78, 6708.65], [0.95, 34268.7, 34212.8], [0.97, 769745.0, 727609.0], [0.99, 37163300.0, 69070200.0]],
    '401/200|1/4': [[0.5, 5.60499, 5.60499], [0.6, 9.65976, 9.6598], [0.7, 22.6021, 22.6022], [0.8, 89.5816, 89.5818], [0.85, 258.617, 258.62], [0.9, 1268.11, 1268.38], [0.93, 5655.36, 5663.47], [0.95, 25743.5, 25878.4], [0.97, 382702.0, 367705.0], [0.99, 2706110000.0, 2913650000.0]],
    '401/200|1/8': [[0.5, 4.92202, 4.92202], [0.6, 8.75346, 8.75346], [0.7, 21.3396, 21.3396], [0.8, 87.9871, 87.9863], [0.85, 259.445, 259.424], [0.9, 1309.79, 1308.56], [0.93, 6033.45, 6005.47], [0.95, 28785.8, 28354.7], [0.97, 480168.0, 451875.0], [0.99, 201391000.0, 284464000.0]],
    '401/200|2': [[0.5, 1.31121, 1.30996], [0.6, 1.91152, 1.91192], [0.7, 4.1145, 4.11888], [0.8, 17.53, 17.498], [0.85, 56.374, 56.0608], [0.9, 322.962, 321.294], [0.93, 1630.69, 1648.76], [0.95, 8460.23, 8812.81], [0.97, 194131.0, 203357.0], [0.99, 9124060.0, 13902000.0]],
    '401/200|4': [[0.5, 1.07649, 1.07807], [0.6, 1.28297, 1.28207], [0.7, 2.16044, 2.14116], [0.8, 7.98647, 7.75724], [0.85, 26.0914, 24.9335], [0.9, 165.939, 156.109], [0.93, 968.204, 950.443], [0.95, 5876.73, 7440.04], [0.97, 127829.0, 1953040.0], [0.99, 25283300.0, 194726.0]],
    '41/20|0': [[0.5, 3.61912, 3.61912], [0.6, 7.40626, 7.40627], [0.7, 21.0405, 21.0405], [0.8, 99.2976, 99.2983], [0.85, 305.595, 305.604], [0.9, 1537.5, 1537.68], [0.93, 6730.95, 6735.12], [0.95, 29630.4, 29830.0], [0.97, 469231.0, 651956.0], [0.99, 3545180000000.0, 30439000000000.0]],
    '41/20|1': [[0.5, 2.04972, 2.04978], [0.6, 3.62436, 3.62456], [0.7, 9.07269, 9.0734], [0.8, 41.4577, 41.4613], [0.85, 133.598, 133.608], [0.9, 762.583, 762.366], [0.93, 3917.21, 3908.2], [0.95, 21064.2, 20866.5], [0.97, 479008.0, 452923.0], [0.99, 882097000.0, 20767900000.0]],
    '41/20|1/16': [[0.5, 3.98513, 3.97388], [0.6, 7.80271, 7.77283], [0.7, 21.473, 21.355], [0.8, 101.626, 100.673], [0.85, 323.226, 318.541], [0.9, 1779.75, 1724.97], [0.93, 8844.24, 8205.99], [0.95, 45846.0, 40678.9], [0.97, 1282340.0, 2647230.0], [0.99, 223620000.0, 325281000.0]],
    '41/20|1/2': [[0.5, 4.13807, 4.12159], [0.6, 7.55601, 7.51786], [0.7, 18.8141, 18.7136], [0.8, 82.3972, 82.0686], [0.85, 257.4, 256.78], [0.9, 1429.35, 1430.69], [0.93, 7266.51, 7329.91], [0.95, 38932.8, 40102.9], [0.97, 1063230.0, 1222440.0], [0.99, 30108200.0, 1425990000.0]],
    '41/20|1/32': [[0.5, 3.80216, 3.8008], [0.6, 7.62101, 7.61784], [0.7, 21.407, 21.3966], [0.8, 102.306, 102.249], [0.85, 323.781, 323.632], [0.9, 1740.67, 1741.93], [0.93, 8305.87, 8344.55], [0.95, 40315.3, 40594.3], [0.97, 1035430.0, 918503.0], [0.99, 2129240000.0, 662842000.0]],
    '41/20|1/4': [[0.5, 4.89572, 4.88394], [0.6, 8.82441, 8.80595], [0.7, 22.1464, 22.1072], [0.8, 97.3879, 97.2531], [0.85, 302.705, 302.346], [0.9, 1656.12, 1653.87], [0.93, 8272.81, 8244.14], [0.95, 43464.3, 42923.8], [0.97, 918927.0, 844062.0], [0.99, 517812000.0, 36176500000000.0]],
    '41/20|1/8': [[0.5, 4.35014, 4.35022], [0.6, 8.20153, 8.20185], [0.7, 21.7458, 21.7472], [0.8, 100.293, 100.31], [0.85, 317.483, 317.617], [0.9, 1756.8, 1759.75], [0.93, 8776.07, 8815.64], [0.95, 45615.4, 45926.4], [0.97, 1025690.0, 1000100.0], [0.99, 16551300000.0, 3524780000.0]],
    '41/20|2': [[0.5, 1.25224, 1.25224], [0.6, 1.76542, 1.76541], [0.7, 3.69777, 3.6977], [0.8, 15.7503, 15.7493], [0.85, 51.3083, 51.2995], [0.9, 302.822, 302.431], [0.93, 1603.5, 1593.06], [0.95, 8963.77, 8749.52], [0.97, 264866.0, 209669.0], [0.99, 31542900.0, 15394500.0]],
    '41/20|4': [[0.5, 1.06284, 1.0662], [0.6, 1.23878, 1.23863], [0.7, 2.0038, 1.97487], [0.8, 7.13716, 6.78766], [0.85, 23.1114, 21.394], [0.9, 146.501, 131.082], [0.93, 867.993, 774.161], [0.95, 5846.61, 5666.98], [0.97, 627830.0, 1099140.0], [0.99, 1665470.0, 227040.0]],
    '43/20|0': [[0.5, 2.21593, 2.22323], [0.6, 4.19411, 4.21792], [0.7, 11.0695, 11.1725], [0.8, 47.6539, 48.4091], [0.85, 137.994, 140.978], [0.9, 659.914, 679.474], [0.93, 3252.06, 3171.8], [0.95, 18828.2, 19365.0], [0.97, 61964500.0, 1673490.0], [0.99, 11343300.0, 17674300.0]],
    '43/20|1/16': [[0.5, 2.60865, 2.61053], [0.6, 4.9011, 4.90712], [0.7, 13.0394, 13.0678], [0.8, 58.4481, 58.7074], [0.85, 175.013, 176.23], [0.9, 854.741, 863.768], [0.93, 3812.37, 3846.15], [0.95, 24895.9, 25365.5], [0.97, 4330250.0, 215432.0], [0.99, 826333000.0, 623381000.0]],
    '43/20|1/2': [[0.5, 3.02824, 3.02855], [0.6, 5.52949, 5.52976], [0.7, 14.2838, 14.2858], [0.8, 67.4872, 67.515], [0.85, 218.098, 218.23], [0.9, 1150.45, 1151.54], [0.93, 4626.59, 4692.65], [0.95, 16343.9, 19499.6], [0.97, 83413.0, 324544.0], [0.99, 7438000.0, 3172220000000.0]],
    '43/20|1/32': [[0.5, 2.40402, 2.40947], [0.6, 4.52306, 4.53925], [0.7, 11.9519, 12.0154], [0.8, 52.2075, 52.5803], [0.85, 152.736, 153.679], [0.9, 726.352, 722.318], [0.93, 3223.42, 3132.74], [0.95, 23030.7, 21407.3], [0.97, 2072970.0, 331040.0], [0.99, 897786000000000.0, 1081540000.0]],
    '43/20|1/4': [[0.5, 3.58966, 3.59257], [0.6, 6.68487, 6.68835], [0.7, 18.1463, 18.1464], [0.8, 91.6398, 91.5788], [0.85, 311.886, 311.586], [0.9, 1803.48, 1804.11], [0.93, 8223.38, 8386.78], [0.95, 44746.4, 47638.9], [0.97, 2870190.0, 1190520.0], [0.99, 63315700000.0, 8258660000.0]],
    '43/20|1/8': [[0.5, 3.05526, 3.05132], [0.6, 5.79162, 5.783], [0.7, 15.8856, 15.8568], [0.8, 77.681, 77.4528], [0.85, 253.984, 252.649], [0.9, 1448.66, 1420.03], [0.93, 7939.63, 7279.99], [0.95, 66342.7, 47925.3], [0.97, 3224460.0, 2671600.0], [0.99, 881176000.0, 38906100000.0]],
    '43/20|2': [[0.5, 1.19407, 1.19491], [0.6, 1.64469, 1.64568], [0.7, 3.54826, 3.54886], [0.8, 18.2699, 18.2583], [0.85, 73.9326, 73.7876], [0.9, 674.146, 662.229], [0.93, 6586.19, 5753.49], [0.95, 106879.0, 112962.0], [0.97, 9595970000000000.0, 138424000.0], [0.99, 5707210.0, 179446000000000.0]],
    '43/20|4': [[0.5, 1.04542, 1.04405], [0.6, 1.18524, 1.18288], [0.7, 1.8283, 1.8244], [0.8, 6.42734, 6.41518], [0.85, 21.742, 21.683], [0.9, 155.133, 154.392], [0.93, 1127.42, 1119.17], [0.95, 12829.7, 12322.3], [0.97, 222816000.0, 51361000000.0], [0.99, 69609600.0, 16312300.0]],
    '5/2|2': [[0.5, 1.24552, 1.24549], [0.6, 2.24942, 2.2492], [0.7, 12.1038, 12.0926], [0.8, 10510.4, 1138.19], [0.85, 51586.8, 32471.6], [0.9, 2390.18, 2196.43], [0.93, 55946.0, 54184.6], [0.95, 42876600.0, 40108700.0], [0.97, 7985510.0, 16597.2], [0.99, 137117.0, 618340.0]],
    '5/2|4': [[0.5, 1.03123, 1.03136], [0.6, 1.16266, 1.16303], [0.7, 1.93966, 1.94336], [0.8, 11.258, 11.3457], [0.85, 70.5454, 69.1878], [0.9, 9164850.0, 2300250.0], [0.93, 18337800000.0, 35736500000000.0], [0.95, 265108.0, 401529.0], [0.97, 19841.5, 25146.9], [0.99, 585364.0, 54442500.0]],
    '50|1': [[0.5, 0.9998, 1.00008], [0.6, 1.00045, 1.00079], [0.7, 1.01689, 1.01734], [0.8, 1.58155, 1.33371], [0.85, 2.45276, 2.35085], [0.9, 34.2629, 52.1174], [0.93, 15630.3, 5596.85], [0.95, 3070.65, 3228.19], [0.97, 16740.2, 4815130.0], [0.99, 3654.14, 1495.32]],
    '50|2': [[0.5, 0.999881, 1.00003], [0.6, 1.00012, 1.00025], [0.7, 1.00743, 1.00755], [0.8, 1.63987, 1.2842], [0.85, 1.9377, 1.97797], [0.9, 8.3521, 12.9148], [0.93, 2554.74, 193553.0], [0.95, 338.099, 941.79], [0.97, 413.615, 44010.6], [0.99, 30511.5, 33888.2]],
    '50|4': [[0.5, 0.999969, 1.00022], [0.6, 1.00004, 1.00035], [0.7, 1.00293, 1.00326], [0.8, 1.10967, 1.10853], [0.85, 1.62257, 1.59142], [0.9, 19.7407, 7.24671], [0.93, 115929.0, 895117.0], [0.95, 70.2957, 467.129], [0.97, 268.239, 354.226], [0.99, 24194.2, 27735.6]],
}
PIN_NECROWS = {   # e|depth|member: per radius (2.005m ... 100m) k kept, r radial broken, t angular broken, x both, u unsettled, - no open point (the full run)
    '0|band_mid|lam 0.1': 'kkkkurrrrrrrrrrx',
    '0|band_mid|lam 0.25': 'kkkkurrrrrrrrrtt',
    '0|band_mid|lam 0.4': 'kkkkrrrrrrrrrxtt',
    '0|band_mid|level': 'kkkrrrrrrrrrrrrr',
    '0|band_mid|smooth adj': 'kkkkrrrrrrrk----',
    '0|band_mid|smooth near': 'kkkrurrurrxxxuuu',
    '0|d_plus|lam 0.1': 'kkkkkrrrrrrrtttt',
    '0|d_plus|lam 0.25': 'kkkkkkkkkkkttttt',
    '0|d_plus|lam 0.4': 'kkkkkkkkkktttttt',
    '0|d_plus|smooth adj': '----------------',
    '0|d_plus|smooth near': 'kkkkkkkkkkktkk--',
    '0|tenth|lam 0.1': 'krrrrrrrrrrrrxtt',
    '0|tenth|lam 0.25': 'krrrrrrrrrrrxttt',
    '0|tenth|lam 0.4': 'rrrrrrrrrrrrtttt',
    '0|tenth|smooth adj': 'kkkkktt---------',
    '0|tenth|smooth near': 'kkkkkkkkkk------',
    '0|y_star|lam 0.1': 'kkkrrrrrrrrrrrrx',
    '0|y_star|lam 0.25': 'kkkrrrrrrrrrrrtt',
    '0|y_star|lam 0.4': 'kkrrrrrrrrrrrxtt',
    '0|y_star|level': 'rrrrrrrrrrrrrrrr',
    '0|y_star|smooth adj': 'kkkkrrrrrr------',
    '0|y_star|smooth near': 'rrrrrrrrrrrrrkkk',
    '0|zero|lam 0.1': 'kkkkkrrrrrrrtttt',
    '0|zero|lam 0.25': 'kkkkkkkkkkkttttt',
    '0|zero|lam 0.4': 'kkkkkkkkkktttttt',
    '0|zero|smooth adj': '----------------',
    '0|zero|smooth near': 'kkkkkkkkkkktkk--',
    '1/16|band_mid|lam 0.1': 'kkkrrrrrrrrrrrrx',
    '1/16|band_mid|lam 0.25': 'kkkkrrrrrrrrrrtt',
    '1/16|band_mid|lam 0.4': 'kkkrrrrrrrrrrxtt',
    '1/16|band_mid|level': 'kkkrrrrrrrrrrrrr',
    '1/16|band_mid|smooth adj': 'kkkrrrrrrrrr----',
    '1/16|band_mid|smooth near': 'kkkrrrrrrrrxxxuu',
    '1/16|tenth|lam 0.1': 'kkrrrrrrrrrrrxtt',
    '1/16|tenth|lam 0.25': 'krrrrrrrrrrrtttt',
    '1/16|tenth|lam 0.4': 'rrrrrrrrrrrrtttt',
    '1/16|tenth|smooth adj': 'kkkkttt---------',
    '1/16|tenth|smooth near': 'kkkkkkkkkk------',
    '1/16|y_star|lam 0.1': 'kkkrrrrrrrrrrrrx',
    '1/16|y_star|lam 0.25': 'kkkrrrrrrrrrrrtt',
    '1/16|y_star|lam 0.4': 'kkrrrrrrrrrrrxtt',
    '1/16|y_star|level': 'rrrrrrrrrrrrrrrr',
    '1/16|y_star|smooth adj': 'kkkkrrrrrr------',
    '1/16|y_star|smooth near': 'rrrrrrrrrrrrrkkk',
    '1/16|zero|lam 0.1': 'kkkkkrrrrrrrtttt',
    '1/16|zero|lam 0.25': 'kkkkkkkkkkkttttt',
    '1/16|zero|lam 0.4': 'kkkkkkkkkkkttttt',
    '1/16|zero|smooth adj': '----------------',
    '1/16|zero|smooth near': 'kkkkkkkkkkktkk--',
    '1/2|band_mid|lam 0.1': 'uuuuuurrrrrrrrrx',
    '1/2|band_mid|lam 0.25': 'uuuuuurrrrrrrrxt',
    '1/2|band_mid|lam 0.4': 'uuuuuurrrrrrrxtt',
    '1/2|band_mid|level': 'uuuururrrrrrrrrr',
    '1/2|band_mid|smooth adj': 'uuurrrrrrr------',
    '1/2|band_mid|smooth near': 'uuuuuurrrrrrxxuu',
    '1/2|tenth|lam 0.1': 'kkrrrrrrrrrrrttt',
    '1/2|tenth|lam 0.25': 'kkrrrrrrrrrrtttt',
    '1/2|tenth|lam 0.4': 'rrrrrrrrrrrrtttt',
    '1/2|tenth|smooth adj': 'kkkkt-----------',
    '1/2|tenth|smooth near': 'kkkkkkkkkk------',
    '1/2|y_star|lam 0.1': 'kuurrrrrrrrrrrrx',
    '1/2|y_star|lam 0.25': 'kuurrrrrrrrrrrxt',
    '1/2|y_star|lam 0.4': 'kuurrrrrrrrrrxtt',
    '1/2|y_star|level': 'rrurrrrrrrrrrrrr',
    '1/2|y_star|smooth adj': 'kkurrrrrrr------',
    '1/2|y_star|smooth near': 'krurrrrrrrrrrrr-',
    '1/2|zero|lam 0.1': 'kkkkkrrrrrrrtttt',
    '1/2|zero|lam 0.25': 'kkkkkkkkkkkttttt',
    '1/2|zero|lam 0.4': 'kkkkkkkkkkkttttt',
    '1/2|zero|smooth adj': '----------------',
    '1/2|zero|smooth near': 'kkkkkkkkkkktkk--',
    '1/32|band_mid|lam 0.1': 'kkkkurrrrrrrrrrx',
    '1/32|band_mid|lam 0.25': 'kkkkurrrrrrrrrtt',
    '1/32|band_mid|lam 0.4': 'kkkkurrrrrrrrxtt',
    '1/32|band_mid|level': 'kkkrurrrrrrrrrrr',
    '1/32|band_mid|smooth adj': 'kkkkurrrrrrr----',
    '1/32|band_mid|smooth near': 'kkkruurrrrxxxxuu',
    '1/32|d_plus|lam 0.1': 'rrrrrrrrrrrrrrxt',
    '1/32|d_plus|lam 0.25': 'rrrrrrrrrrrrrxtt',
    '1/32|d_plus|lam 0.4': 'rrrrrrrrrrrrxttt',
    '1/32|d_plus|smooth adj': 'kkkkkkktt-------',
    '1/32|d_plus|smooth near': 'krrrrrrrkk------',
    '1/32|tenth|lam 0.1': 'kkrrrrrrrrrrrxtt',
    '1/32|tenth|lam 0.25': 'krrrrrrrrrrrxttt',
    '1/32|tenth|lam 0.4': 'rrrrrrrrrrrrtttt',
    '1/32|tenth|smooth adj': 'kkkkktt---------',
    '1/32|tenth|smooth near': 'kkkkkkkkkk------',
    '1/32|y_star|lam 0.1': 'kkkrrrrrrrrrrrrx',
    '1/32|y_star|lam 0.25': 'kkkrrrrrrrrrrrtt',
    '1/32|y_star|lam 0.4': 'kkrrrrrrrrrrrxtt',
    '1/32|y_star|level': 'rrrrrrrrrrrrrrrr',
    '1/32|y_star|smooth adj': 'kkkkrrrrrr------',
    '1/32|y_star|smooth near': 'rrrrrrrrrrrrrkkk',
    '1/32|zero|lam 0.1': 'kkkkkrrrrrrrtttt',
    '1/32|zero|lam 0.25': 'kkkkkkkkkkkttttt',
    '1/32|zero|lam 0.4': 'kkkkkkkkkkkttttt',
    '1/32|zero|smooth adj': '----------------',
    '1/32|zero|smooth near': 'kkkkkkkkkkktkk--',
    '1/4|band_mid|lam 0.1': 'uuuuurrrrrrrrrrx',
    '1/4|band_mid|lam 0.25': 'kkururrrrrrrrrxt',
    '1/4|band_mid|lam 0.4': 'kkurrrrrrrrrrxtt',
    '1/4|band_mid|level': 'kkurrrrrrrrrrrrr',
    '1/4|band_mid|smooth adj': 'kkkrrrrrrrr-----',
    '1/4|band_mid|smooth near': 'kkuuurrrrrrxxxuu',
    '1/4|tenth|lam 0.1': 'kkrrrrrrrrrrrxtt',
    '1/4|tenth|lam 0.25': 'kkrrrrrrrrrrtttt',
    '1/4|tenth|lam 0.4': 'rrrrrrrrrrrrtttt',
    '1/4|tenth|smooth adj': 'kkkktt----------',
    '1/4|tenth|smooth near': 'kkkkkkkkkk------',
    '1/4|y_star|lam 0.1': 'kkkrrrrrrrrrrrrx',
    '1/4|y_star|lam 0.25': 'kkkrrrrrrrrrrrtt',
    '1/4|y_star|lam 0.4': 'kkrrrrrrrrrrrxtt',
    '1/4|y_star|level': 'rrurrrrrrrrrrrrr',
    '1/4|y_star|smooth adj': 'kkkrrrrrrr------',
    '1/4|y_star|smooth near': 'rrrrrrrrrrrrrkkr',
    '1/4|zero|lam 0.1': 'kkkkkrrrrrrrtttt',
    '1/4|zero|lam 0.25': 'kkkkkkkkkkkttttt',
    '1/4|zero|lam 0.4': 'kkkkkkkkkkkttttt',
    '1/4|zero|smooth adj': '----------------',
    '1/4|zero|smooth near': 'kkkkkkkkkkktkk--',
    '1/8|band_mid|lam 0.1': 'kkkurrrrrrrrrrrx',
    '1/8|band_mid|lam 0.25': 'kkkurrrrrrrrrrtt',
    '1/8|band_mid|lam 0.4': 'kkkurrrrrrrrrxtt',
    '1/8|band_mid|level': 'kkkurrrrrrrrrrrr',
    '1/8|band_mid|smooth adj': 'kkkrrrrrrrr-----',
    '1/8|band_mid|smooth near': 'kkkurrrrrrrxxxuu',
    '1/8|tenth|lam 0.1': 'kkrrrrrrrrrrrxtt',
    '1/8|tenth|lam 0.25': 'krrrrrrrrrrrtttt',
    '1/8|tenth|lam 0.4': 'rrrrrrrrrrrrtttt',
    '1/8|tenth|smooth adj': 'kkkktt----------',
    '1/8|tenth|smooth near': 'kkkkkkkkkk------',
    '1/8|y_star|lam 0.1': 'kkkrrrrrrrrrrrrx',
    '1/8|y_star|lam 0.25': 'kkkrrrrrrrrrrrtt',
    '1/8|y_star|lam 0.4': 'kkrrrrrrrrrrrxtt',
    '1/8|y_star|level': 'rrrrrrrrrrrrrrrr',
    '1/8|y_star|smooth adj': 'kkkrrrrrrr------',
    '1/8|y_star|smooth near': 'rrrrrrrrrrrrrkkk',
    '1/8|zero|lam 0.1': 'kkkkkrrrrrrrtttt',
    '1/8|zero|lam 0.25': 'kkkkkkkkkkkttttt',
    '1/8|zero|lam 0.4': 'kkkkkkkkkkkttttt',
    '1/8|zero|smooth adj': '----------------',
    '1/8|zero|smooth near': 'kkkkkkkkkkktkk--',
    '1|band_mid|lam 0.1': 'uuuuuuurrrrrrrrr',
    '1|band_mid|lam 0.25': 'uuuuuuurrrrrrrxt',
    '1|band_mid|lam 0.4': 'uuuuuuurrrrrrxtt',
    '1|band_mid|level': 'uuuurrrrrrrrrrrr',
    '1|band_mid|smooth adj': 'uuurrrrrrr------',
    '1|band_mid|smooth near': 'uuuuuuurrrrrxxuu',
    '1|tenth|lam 0.1': 'kkkrrrrrrrrrrttt',
    '1|tenth|lam 0.25': 'kkkrrrrrrrrrtttt',
    '1|tenth|lam 0.4': 'rrrrrrrrrrrrtttt',
    '1|tenth|smooth adj': 'kkkt------------',
    '1|tenth|smooth near': 'kkkkkkkkkk------',
    '1|y_star|lam 0.1': 'uuuuuuurrrrrrrrx',
    '1|y_star|lam 0.25': 'uuuuuuurrrrrrrxt',
    '1|y_star|lam 0.4': 'uuuuruurrrrrrxtt',
    '1|y_star|level': 'uuurrrrrrrrrrrrr',
    '1|y_star|smooth adj': 'uuurrrrrr-------',
    '1|y_star|smooth near': 'uuuurrrrrrrrrr--',
    '1|zero|lam 0.1': 'kkkkkrrrrrrrtttt',
    '1|zero|lam 0.25': 'kkkkkkkkkkkttttt',
    '1|zero|lam 0.4': 'kkkkkkkkkkkttttt',
    '1|zero|smooth adj': '----------------',
    '1|zero|smooth near': 'kkkkkkkkkkkkkk--',
    '2|band_mid|lam 0.1': 'uuuuuuurrrrrrrrr',
    '2|band_mid|lam 0.25': 'uuuuuuurrrrrrrxt',
    '2|band_mid|lam 0.4': 'uuuuuuurrrrrrrxx',
    '2|band_mid|level': 'uuuuuurrrrrrrrrr',
    '2|band_mid|smooth adj': 'uuurrrrrx-------',
    '2|band_mid|smooth near': 'uuuuurrrrrrr----',
    '2|tenth|lam 0.1': 'kkkrrrrrrrrrrttt',
    '2|tenth|lam 0.25': 'kkkrrrrrrrrrtttt',
    '2|tenth|lam 0.4': 'krrrrrrrrrrrtttt',
    '2|tenth|smooth adj': 'kkkt------------',
    '2|tenth|smooth near': 'kkkkkkkkkk------',
    '2|y_star|lam 0.1': 'uuuuuuurrrrrrrrr',
    '2|y_star|lam 0.25': 'uuuuuuurrrrrrrxt',
    '2|y_star|lam 0.4': 'uuuuuuurrrrrrrxx',
    '2|y_star|level': 'uuuuuurrrrrrrrrr',
    '2|y_star|smooth adj': 'uuurrrrrx-------',
    '2|y_star|smooth near': 'uuuuurrrrrrr----',
    '2|zero|lam 0.1': 'kkkkkrrrrrrrtttt',
    '2|zero|lam 0.25': 'kkkkkkkkkkkttttt',
    '2|zero|lam 0.4': 'kkkkkkkkkkkttttt',
    '2|zero|smooth adj': '----------------',
    '2|zero|smooth near': 'kkkkkkkkkkkkk---',
    '4|band_mid|lam 0.1': 'uuuuuuuuurrrrrrr',
    '4|band_mid|lam 0.25': 'uuuuuuuuurrrrrrx',
    '4|band_mid|lam 0.4': 'uuuuuuuuurrrrrrx',
    '4|band_mid|level': 'uuuuuuurrrrrrrrr',
    '4|band_mid|smooth adj': 'uurrx-----------',
    '4|band_mid|smooth near': 'uuurrx----------',
    '4|tenth|lam 0.1': 'kkkrrrrrrrrrrttt',
    '4|tenth|lam 0.25': 'kkkrrrrrrrrrtttt',
    '4|tenth|lam 0.4': 'kkrrrrrrrrrrtttt',
    '4|tenth|smooth adj': 'kkk-------------',
    '4|tenth|smooth near': 'kkkkkkkkkk------',
    '4|y_star|lam 0.1': 'uuuuuuuuurrrrrrr',
    '4|y_star|lam 0.25': 'uuuuuuuuurrrrrrx',
    '4|y_star|lam 0.4': 'uuuuuuuuurrrrrrx',
    '4|y_star|level': 'uuuuuuurrrrrrrrr',
    '4|y_star|smooth adj': 'uuurrx----------',
    '4|y_star|smooth near': 'uuurrrrx--------',
    '4|zero|lam 0.1': 'kkkkkrrrrrrrtttt',
    '4|zero|lam 0.25': 'kkkkkkkkrrkttttt',
    '4|zero|lam 0.4': 'kkkkkkkkrkkttttt',
    '4|zero|smooth adj': '----------------',
    '4|zero|smooth near': 'kkkkkkkkkkkkk---',
}
PIN_CYPHER = {'main': {'cells': 13, 'top': {'target': True}, 'langs': {'order': ['SPEAKS', 151, 'YES'], 'algebra': ['SPEAKS', 151, 'YES'], 'geometry': ['SPEAKS', 83, 'NO'], 'information': ['SPEAKS', 34, 'YES'], 'statistics': ['SPEAKS', 22, 'NO']}}, 'control_b': {'cells': 14, 'top': {'target': True}, 'langs': {'order': ['SPEAKS', 150, 'YES'], 'algebra': ['SPEAKS', 150, 'YES'], 'geometry': ['SPEAKS', 108, 'YES'], 'information': ['SPEAKS', 33, 'YES'], 'statistics': ['SPEAKS', 25, 'YES']}}, 'control_a': {'cells': 13, 'top': {'target': True}, 'langs': {'order': ['SPEAKS', 74, 'YES'], 'algebra': ['SPEAKS', 74, 'YES'], 'geometry': ['SPEAKS', 58, 'YES'], 'information': ['SPEAKS', 18, 'YES'], 'statistics': ['SPEAKS', 14, 'YES']}}, 'nec_reversed': {'cells': 13, 'top': {'target': False}, 'langs': {'order': ['SPEAKS', 167, 'NO'], 'algebra': ['SPEAKS', 167, 'NO'], 'geometry': ['SPEAKS', 83, 'NO'], 'information': ['SPEAKS', 14, 'NO'], 'statistics': ['SPEAKS', 22, 'NO']}}, 'per_ell': {'cells': 90, 'top': {'target@e0': False, 'target@e1': False, 'target@e2': False, 'target@e3': False, 'target@e4': False, 'target@e5': False, 'target@e6': False, 'target@e7': False, 'target@e8': True}, 'langs': {'order': ['SPEAKS', 1656, 'YES', 'YES', 'YES', 'YES', 'YES', 'YES', 'YES', 'YES', 'YES'], 'algebra': ['SPEAKS', 1656, 'YES', 'YES', 'YES', 'YES', 'YES', 'YES', 'YES', 'YES', 'YES'], 'geometry': ['SPEAKS', 891, 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'], 'information': ['SPEAKS', 253, 'YES', 'YES', 'YES', 'YES', 'YES', 'YES', 'YES', 'YES', 'YES'], 'statistics': ['SPEAKS', 382, 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO']}}}



# ---------------------------------------------------------------------------------------------------------- cypher
# The board's encoding H-CYPHER-R1-COVER (built by the cypher step, a separate AI session in this project, and carried
# into the instrument after the verification), with H-CURVATURE-SETTLED applied.  The cypher CLASSIFIES the computed
# cells; an admitted cell that was not computed is a classification, never a configuration, and nothing here is a
# physical derivation.
ZONES = ("throat", "footprint", "near", "far")  # r <= 2.005m; to R_F(ell); R_F to 10m; 10m to 100m
CY_COORDS = ["crossable", "every_ell", "open", "throat", "footprint", "near", "far", "nec"]
CY_TARGET = (1, 1, 4, 2, 2, 2, 2, 2)    # the statement's YES: crossable, at every ell, never meets P1 within 100m,
#                                         every zone verified, the NEC kept at every settled node
CY_VO = {"crossable": [0, 1], "every_ell": [0, 1], "open": [0, 1, 2, 3, 4], "throat": [0, 1, 2],
         "footprint": [0, 1, 2], "near": [0, 1, 2], "far": [0, 1, 2], "nec": [0, 1, 2]}
CY_OPTS = {"statistics_order": 2, "algebra_budget": 200000}
CY_LANGS = ("order", "algebra", "geometry", "information", "statistics")
INJECT_CELL = None                       # C12's mutation: a cell fed to MAIN as if computed
EMPTY_ZONE_VERIFIED = False              # C12's mutation: an empty zone written as verified (the old regions())


def zone_of(r, rf):
    if r <= 2.005 + 1e-12:
        return "throat"
    if r <= rf + 1e-12:
        return "footprint"
    if r <= 10 + 1e-12:
        return "near"
    return "far"


def zones(c, cols, e, cut=None):
    """Zone outcomes of one cover record: 0 a failure located in the zone (a DEEP interval on a settled singularity;
    DEEP-THROAT; or, after the piece has met P1, an uncut_site); 1 undecided (an unverified interval, PAST-POLE, the
    closing interval, or the piece absent with no uncut_site); 2 every interval in it VERIFIED.  cut truncates the cover
    (Control A: the zones past R_F are not asked).  An empty zone (the near zone at ell = m/4, where R_F = 10m) takes
    the far zone's value: it is never written as verified (RC-O7)."""
    rf = c["R_F"]
    cap = math.inf if cut is None else cut
    out = {k: 2 for k in ZONES}
    seen = {k: False for k in ZONES}
    closed = False
    for iv in c["intervals"]:
        r = float(Fr(iv["hi"]))
        if r > cap + 1e-12:
            break
        k = zone_of(r, rf)
        seen[k] = True
        s = iv["status"]
        if s == "DEEP":
            out[k] = min(out[k], 0)
        elif s in ("UNDECIDED", "PAST-POLE", "CLOSED"):
            closed = closed or s == "CLOSED"
            out[k] = min(out[k], 1)
    if closed:
        floor = P.write_floor()
        for n in nodes_for(cols, e):
            r = float(Fr(n["rc"]))
            if n["x"] > c["x_meet"] and r <= cap + 1e-12:
                k = zone_of(r, rf)
                seen[k] = True
                out[k] = min(out[k], 0 if uncut_site(n, floor) else 1)
    if c["verdict"][1] == "DEEP-THROAT":
        out["throat"], seen["throat"] = 0, True
    asked = ZONES if cut is None else ("throat", "footprint")
    if not EMPTY_ZONE_VERIFIED and cut is None and not seen["near"]:
        out["near"] = out["far"]
    return {k: out[k] for k in asked}


def open_zone(c, cut=None):
    """Where the continued piece meets P1: the index of its zone among those asked; len(asked) if never within the
    (truncated) cover.  The P1 side of 'strictly between P1 and y_s(r)'."""
    asked = ZONES if cut is None else ("throat", "footprint")
    cap = 100.0 if cut is None else cut
    rm = c["r_meet"]
    if rm is None or rm > cap + 1e-12:
        return len(asked)
    return asked.index(zone_of(rm, c["R_F"]))


def nec_code(nrow, cut=None):
    """0 broken at a settled node; 1 no settled node (unmeasured -- never read as kept, RC-O7); 2 kept at every
    settled node.  H-POINTWISE-NEC-ON-P2: the board's reading of 172 (1)'s "stress that obeys the NEC" (pointwise, P2's
    own Israel stress at each settled node); M's seated clause (Z) reads net along each light ray (183)."""
    rows = [w for w in (nrow or {}).get("rows", []) if w["settled"] and (cut is None or float(Fr(w["rc"])) <= cut + 1e-12)]
    if not rows:
        return 1
    return 0 if any(not w["holds"] for w in rows) else 2


def cypher_cells(res, cols, per_e=False, control_a=False):
    """H-CYPHER-R1-COVER's cells: one per (member, depth row), worst over ES2 (min per coordinate), with every_ell; or
    per (member, depth row, ell) with per_e (coordinate e, ES2's position, in place of every_ell).  control_a truncates
    the cover at each ell's R_F (zones throat and footprint, open in {0, 1, 2}, the NEC at settled nodes r <= R_F)."""
    agg, pres = {}, {}
    for es, pe in res["per_e"].items():
        e = Fr(es)
        necs = {(n["depth_key"], n["member"]): n for n in pe["nec"]}
        for c in pe["covers"]:
            cut = c["R_F"] if control_a else None
            z = zones(c, cols, e, cut)
            cell = {"crossable": 1 if c["member"] in CROSSABLE else 0, "open": open_zone(c, cut)}
            cell.update(z)
            cell["nec"] = nec_code(necs.get((c["depth_key"], c["member"])), cut)
            key = (c["member"], c["depth_key"]) + ((es,) if per_e else ())
            pres.setdefault((c["member"], c["depth_key"]), set()).add(es)
            if key in agg:
                agg[key] = {k: (v if k == "crossable" else min(v, cell[k])) for k, v in agg[key].items()}
            else:
                agg[key] = cell
    es_list = list(res["per_e"])
    out = {}
    for key, cell in agg.items():
        if per_e:
            cell = dict(cell, e=es_list.index(key[2]))
        else:
            cell = dict(cell, every_ell=1 if len(pres[key[:2]]) == len(es_list) else 0)
        out[key] = cell
    return out


def cy_coords(per_e=False, control_a=False):
    zs = list(ZONES) if not control_a else ["throat", "footprint"]
    cs = ["crossable"] + ([] if per_e else ["every_ell"]) + ["open"] + zs + ["nec"] + (["e"] if per_e else [])
    vo = dict(CY_VO, open=list(range(len(zs) + 1)), e=list(range(len(ES2))))
    return cs, {k: vo[k] for k in cs}


def cy_target(coords, nz):
    t = {"crossable": 1, "every_ell": 1, "open": nz, "nec": 2}
    t.update({z: 2 for z in ZONES})
    return tuple(t[k] for k in coords if k != "e")


def cypher_spec(cells, coords, vo, name, extra=()):
    rows = [[c[k] for k in coords] for c in cells.values()] + [list(x) for x in extra]
    return {"name": name, "coordinates": coords, "cells": rows, "value_order": vo,
            "declared": {"analysis": {"speaks": True, "witness":
                                      "a continuous margin law: y_s(r) - d - c x^lam (power law) and "
                                      "y_s(r) - d - g1 sqrt(x) - g2 x (smooth family), continuous in (r, d, c); the cover "
                                      "holds at a node iff the margin is positive, so the law returns a magnitude "
                                      "(c* = min (y_s - d)/x^lam over the nodes), not a cell decision; y_s(r) is known "
                                      "only at the columns"}}}


def _cy():
    key = "r1cover_cypher"
    if key not in sys.modules:
        spec = importlib.util.spec_from_file_location(key, CYPHER_PATH)
        cy = importlib.util.module_from_spec(spec)
        sys.modules[key] = cy                                         # registered before exec_module
        spec.loader.exec_module(cy)
    return sys.modules[key]


def ask(sp, targets):
    """Every language of roster 1173 on one spec: state, E, and each target's membership; with whether each target is
    the top of the observed box (RF1: then order, algebra and information admit it by construction)."""
    cy = _cy()
    ix = cy.Index(sp["name"], sp["coordinates"], sp["cells"], sp["value_order"], sp["declared"])
    r = cy.run(ix, "1173", CY_OPTS)
    top = tuple(ix.decode[i][max(ix.alphabets[i])] for i in range(ix.d))
    out = {"cells": len(ix.cells), "d": ix.d, "box": ix.box, "degenerate": r["degenerate"],
           "langclose_holds": r["langclose_holds"], "verdicts": {},
           "target_is_top": {tn: tuple(t) == top for tn, t in targets.items()}}
    for v in r["_verdicts"]:
        row = {"state": v.state, "E": v.E}
        if v.language in cy.ADMISSION and v.state == cy.SPEAKS:
            adm, _ = cy.ADMISSION[v.language][0](ix, CY_OPTS)
            for tn, t in targets.items():
                et = tuple(ix.code[i].get(x) for i, x in enumerate(t))
                row[tn] = ("NO (a value never seen: STRUCTURAL)" if None in et else ("YES" if et in adm else "NO"))
        out["verdicts"][v.language] = row
    return out


def carriers(cells, coords, target):
    """RF1: which (member, depth row) records carry each target value (the leave-one-out notes, recast)."""
    return {k: sorted("|".join(key) for key, c in cells.items() if c[k] == t)
            for k, t in zip(coords, target) if k not in ("crossable",)}


def cypher_run(res, outdir=None, cols=None):
    """Ask each language of roster 1173 (tools/cypher.py imported by path) on: MAIN (worst over ES2); CONTROL-B (the
    target inserted as if computed: an encoding that can say YES); CONTROL-A (the cover truncated at R_F, the question's
    own contrast); NEC-REVERSED (MAIN with nec's value order reversed, kept lowest -- RF1's discriminating target, which
    is then not the top of the box); PER-ELL (one cell per ell)."""
    main_c = cypher_cells(res, cols)
    cs, vo = cy_coords()
    tgt = cy_target(cs, 4)
    extra = [INJECT_CELL] if INJECT_CELL else []
    a_c = cypher_cells(res, cols, control_a=True)
    acs, avo = cy_coords(control_a=True)
    atgt = cy_target(acs, 2)
    pe_c = cypher_cells(res, cols, per_e=True)
    pcs, pvo = cy_coords(per_e=True)
    runs = {
        "main": (cypher_spec(main_c, cs, vo, "r1-cover MAIN: members x depth rows, worst over ES2", extra), {"target": tgt}),
        "control_b": (cypher_spec(main_c, cs, vo, "CONTROL-B: the target inserted as computed", [tgt]), {"target": tgt}),
        "control_a": (cypher_spec(a_c, acs, avo, "CONTROL-A: the cover truncated at R_F(ell)"), {"target": atgt}),
        "nec_reversed": (cypher_spec(main_c, cs, dict(vo, nec=[2, 1, 0]), "NEC-REVERSED: nec kept lowest", extra),
                         {"target": tgt}),
        "per_ell": (cypher_spec(pe_c, pcs, pvo, "r1-cover PER-ELL: members x depth rows x ell"),
                    {"target@e%d" % i: tuple(list(cy_target(pcs, 4)) + [i]) for i in range(len(ES2))}),
    }
    out = {}
    for tag, (sp_, tg) in runs.items():
        out[tag] = ask(sp_, tg)
        if outdir:
            os.makedirs(outdir, exist_ok=True)
            json.dump(sp_, open(os.path.join(outdir, "r1_%s.json" % tag), "w"), indent=1)
            json.dump(out[tag], open(os.path.join(outdir, "r1_%s.out.json" % tag), "w"), indent=1)
    out["main"]["carriers"] = carriers(main_c, cs, tgt)
    out["main"]["cells_by_record"] = {"|".join(k): [c[x] for x in cs] for k, c in main_c.items()}
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
        cy = cypher_run(res, a.cypher, cols)
        for tag, r in cy.items():
            print("\ncypher %s: %d cells, d = %d, box %d, degenerate %s, K.langclose %s, target is the top: %s" % (
                tag, r["cells"], r["d"], r["box"], r["degenerate"], r["langclose_holds"], r["target_is_top"]))
            for lang, v in r["verdicts"].items():
                print("  %-12s %-8s E=%-6s %s" % (lang, v["state"], v["E"], "  ".join(
                    "%s=%s" % (k, v[k]) for k in sorted(r["target_is_top"]) if k in v)))
        print("\ncarriers of each MAIN target value: %s" % json.dumps(cy["main"]["carriers"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
