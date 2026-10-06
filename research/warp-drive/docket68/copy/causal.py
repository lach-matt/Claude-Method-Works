#!/usr/bin/env python3
"""
causal.py -- the causality thread (M-RULINGS item 94: "Do you want to take up the causality thread next? - yes").
Deduced, computed, READ.  Not seated; verified once (2026-10-06).  M's words are carried as hypotheses, never as
results.

M (item 94, verbatim): "their is no movement in warp travel, it is a teleportation that happens instantaneously
relative to the object teleporting, AND all observers of the same dimension of that objects existence".  Carried as
H-NO-MOVEMENT and H-INSTANTANEOUS.  NO SPEED OF THE TELEPORT IS PRICED: no carrier, no hold, no rate.  The only speeds
here are how fast observers or objects move relative to one another, which M's "all observers" invites.  The one
question asked is the one M said yes to -- what "instantaneous" does to "before" and "after" -- and it is asked of the
board's own frame.py (docket 68, agent A2-frame) and cmb/cmbframe.py, IMPORTED, never rebuilt.
First written: "NOTHING HERE PRICES A SPEED" and M's words retyped "there is no movement" (verifier).

WHAT FOLLOWS THE WORK
  * ONE SHARED "NOW" MAKES M'S TELEPORTATION CAUSALLY SAFE, HOWEVER OFTEN IT IS REPEATED (K1, K2).  If every teleport is
    instantaneous in ONE frame for the whole dimension (R-SHARED), no chain of teleports returns before it left:
    frame.antitelephone's reply keyed to that frame arrives at t = 0, never earlier; and every network of corridors
    keyed to one frame is free of closed causal curves (frame.cosmic_keyed_rank_n_is_safe; Sylvester's theorem, so the
    0-of-200 count is a regression on frame.py, not evidence).  So M's H-CORRIDOR-REPEATABLE (item 90) is safe on this
    reading, in the corridor-as-identification model (H-CORRIDOR-MODEL, H-KEYING; frame.py's grade).  The published
    resolution says the same: paradoxes need that "given an arbitrary reference frame, it is always possible to send a
    tachyon backward in time in that frame", and "there can be no paradox if, in one particular reference frame,
    tachyons can only propagate forward in time" (Liberati-Sonego-Visser, READ, p.12).
    First written: "is safe on this reading", without H-CORRIDOR-MODEL and H-KEYING.
  * THE BOARD ALREADY HOLDS A CANDIDATE FOR THAT FRAME, AND IN EXACT FRW THE GEOMETRY FORCES IT.  The cosmic rest frame
    (frame.py, H-CMB-IS-COSMIC; the CMB dipole 369.82 km/s, Planck 2018 I READ in cmbframe.py).  In exact flat FRW only
    equal-cosmic-time identifications are isometries, so R-SHARED is not the board's choice there: frame.py credits it
    to the geometry (H-FRW-EXACT, H-NOT-DE-SITTER), to no hypothesis.
  * M'S CHARTER CLAUSE 2 IS MET WITHOUT A LOOP.  H-FRAME clause 1 ("a preferred frame exists") is what R-SHARED needs.
    Clause 2 ("messages may travel into the past") survives in frame.py's sense 2a: K3's separation IS the message
    arriving in a moving observer's coordinate past, with no loop.  Only 2b, the past of the shared clock itself, is
    excluded.  First written: "H-FRAME ('a preferred frame exists') is exactly what R-SHARED needs" (clause 2 hidden).
  * WHAT "ALL OBSERVERS" COSTS (K3).  For two separated places, "instantaneous" holds for the observers of one family of
    frames only (the relativity of simultaneity: for spacelike-separated events "it is always possible to find another
    frame where E1 and E2 are simultaneous", LSV p.11).  Observers moving relative to the shared frame read the
    departure and arrival as apart by v.L/c^2 projected on the span: for the Sun's barycentre, along Proxima's actual
    direction (66 degrees off the dipole; cmbframe.lead), 6.7e4 s (0.77 day); for a span of Proxima's length laid along
    the dipole (H-ALONG-DIPOLE), the maximum, 1.65e5 s (1.9 days).  For observers on Earth the figure moves by the
    printed annual term.  On R-SHARED they disagree about the timing but never see a loop.
    First written: "over the board's Proxima span, 1.65e5 s (1.9 days)" -- the along-dipole maximum, unnamed.
  * Boundary (item 82): R-OBJECT -- each teleport instantaneous in its own object's REST FRAME -- is the reading the
    board cannot make safe.  Two objects in relative motion, each teleporting "instantaneously relative to" itself,
    close a loop, given that the second can teleport back at once (H-RETURN-AVAILABLE): frame.antitelephone's reply
    keyed to the replier's (B's) rest frame reaches the first sender before its message left (t = -3/5 at v = 3/5 c),
    at any nonzero relative speed for a suitable placement.  For two objects moving apart at 369.82 km/s along a
    Proxima-length span, the reply reaches the first sender 1.65e5 s before its message left.  This is LSV's tachyonic
    anti-telephone (p.12); whether chronology protection forbids it is OPEN.
    First written: "the reply keyed to the sender's frame" (the first sender is at rest in the shared frame; it is the
    replier's frame) and "the reply arrives 1.65e5 s before it was sent".

THE READINGS, AND THE QUESTION FOR M (pause for the answer).  Under the relativity of simultaneity (H-LORENZ-OBSERVERS),
"instantaneous" for two separated places cannot hold for observers moving relative to one another.  It can hold in
one shared frame (R-SHARED: other observers read a separation, K3, never a loop) or in each object's own frame
(R-OBJECT: loops).  Neither honours "all observers" literally; that needs H-LORENZ-OBSERVERS to fail, or a reading in
which departure and arrival are not two separated events:
  R-PROPER   "instantaneous relative to the object" as zero time on the object's own clock -- a statement about the
             object, no simultaneity claim; all the frame content sits in "all observers".  Compatible with R-SHARED
             and with R-IDENTIFY.
  R-IDENTIFY the corridor as an identification of two places (frame.py's own corridor model): departure and arrival are
             ONE point of the identified spacetime -- literally no movement, no duration for anyone to measure; only
             the labels of the two ends depend on the frame.  Its causal safety is exactly K2.
First written: "these agree only if one frame serves the whole dimension" (R-SHARED does not give "all observers"
either; verifier).

    python3 causal.py              report
    python3 causal.py --selftest   checks, CONTROLS and CONTRASTS marked, STRUCTURAL printed and not counted

K1 [computed, imported]  frame.reply_arrival / frame.antitelephone (sympy, exact): a reply keyed to frame u returns to
   the first sender's worldline at cosmic time -u L (c = 1; one closed form, evaluated at u = 3/5, 1e-6 and 0).
K2 [computed, imported]  frame.cosmic_keyed_rank_n_is_safe(rank, trials) (Sylvester: a regression on frame.py);
   frame.past_corridor_witness: ONE corridor keyed to another frame beside a shared-frame one spans a timelike vector.
K3 [computed, imported]  cmbframe.lead() (the barycentre's lead along Proxima's Gaia DR3 direction, with frame.py's
   formula scaled by cos theta beside it -- two owners' formulas, cross-checked); frame.cmb_coordinate_past for the
   along-dipole maximum; frame.GRADES for H-FRAME's clauses.
READ this pass: Liberati, Sonego, Visser, gr-qc/0107091v2, alphaXiv (verifier-READ again): p.10 (absolute simultaneity
   "essentially due to the introduction of a preferred frame"); p.11 (the frame where spacelike events are simultaneous;
   the signal "would appear to travel at an infinite speed"); p.12 (the anti-telephone; "there can be no paradox if, in
   one particular reference frame, tachyons can only propagate forward in time"; time-order disagreement "should not be
   more disturbing than the jet lag"); pp.12-13 footnote 16 ("good physical reasons", "can make good physical sense");
   p.16 (stable causality excludes closed timelike and null curves).

NAMED HYPOTHESES
  M's: H-NO-MOVEMENT, H-INSTANTANEOUS (item 94); H-CORRIDOR-REPEATABLE, H-CORRIDOR-CONTAINS-P2 (item 90); H-FRAME (the
  charter's, tested in frame.py).  The board's readings of H-INSTANTANEOUS: R-SHARED, R-OBJECT, R-PROPER, R-IDENTIFY
  (named, M to choose).  frame.py's: H-CMB-IS-COSMIC, H-CORRIDOR-MODEL (latticectc H1-H3), H-KEYING, H-FRW-EXACT,
  H-NOT-DE-SITTER.  cmbframe.py's: H-AT-REST-ENDPOINT.  This file's: H-LORENZ-OBSERVERS, H-ALONG-DIPOLE (for the
  maximum only), H-RETURN-AVAILABLE (R-OBJECT's loop).
"""

import contextlib
import importlib.util
import io
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)


def _load(name, path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    m = importlib.util.module_from_spec(spec)
    saved = list(sys.path)
    try:
        sys.path.insert(0, WD)
        sys.path.insert(0, D68)
        sys.path.insert(0, os.path.dirname(path))
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(m)
    finally:
        sys.path[:] = saved
    return m


_CACHE = {}


def owners():
    if not _CACHE:
        _CACHE["frame"] = _load("frame", os.path.join(D68, "frame.py"), "d68_frame_causal")
        _CACHE["cmbframe"] = _load("cmbframe", os.path.join(D68, "cmb", "cmbframe.py"), "d68_cmbframe_causal")
    return _CACHE["frame"], _CACHE["cmbframe"]


def compute():
    fr, cf = owners()
    saved = list(sys.path)
    sys.path[:0] = [D68, WD]          # frame.py imports corridors.py lazily, by bare name
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            return _compute(fr, cf)
    finally:
        sys.path[:] = saved


def _compute(fr, cf):
    g = cf.geometry()
    ld = cf.lead()
    L_ly = g["L_ly"]
    v = cf.DIPOLE["v_kms"][0]
    beta = v / cf.C_KMS
    obj_v, shared_v = fr.antitelephone()                               # v = 3/5, L = 1 (frame's own)
    tiny = Fr(1, 10 ** 6)
    b_frac = Fr(beta).limit_denominator(10 ** 12)
    obj_prox_yr = fr.reply_arrival(b_frac, b_frac, Fr(L_ly).limit_denominator(10 ** 9))
    tested, bad = fr.cosmic_keyed_rank_n_is_safe(3, 200)
    kind, vec, nrm = fr.past_corridor_witness()
    along = fr.cmb_coordinate_past(L_ly, v)[0]
    clause1 = fr.GRADES["H-FRAME clause 1 (a preferred frame exists)"]["O-LOOP"]
    clause2a = fr.GRADES["H-FRAME clause 2 (messages into the past)"]["2a coordinate past of a moving frame"]
    return {"L_ly": L_ly, "beta": beta, "theta_deg": g["theta_deg"], "cos_theta": g["cos_theta"],
            "R_object_reply": obj_v, "R_shared_reply": shared_v,
            "R_object_tiny": fr.reply_arrival(tiny, tiny), "R_shared_tiny": fr.reply_arrival(Fr(0), tiny),
            "R_object_proxima_s": float(obj_prox_yr) * cf.YEAR_S,
            "networks_tested": tested, "networks_with_loop": bad,
            "past_corridor_span": kind, "past_corridor_vector": vec, "past_corridor_norm": nrm,
            "K3_lead_s": ld["lead_s"], "K3_owner_scaled_s": ld["owner_scaled_s"],
            "K3_annual_earth_s": ld["annual_mod_earth_frame_s"], "K3_along_dipole_s": along,
            "grade_clause1": clause1, "grade_clause2a": clause2a}


def report():
    d = compute()
    print("causal.py -- the causality thread (M item 94; verified once; not seated).  No speed of the teleport is "
          "priced; the only speeds are how fast observers move relative to one another.\n")
    print("K1 a reply keyed to the replier's own frame (R-OBJECT) reaches the first sender at t = %s (v = 3/5 c, L = 1); "
          "at 1e-6 c, t = %s" % (d["R_object_reply"], d["R_object_tiny"]))
    print("   keyed to one shared frame (R-SHARED): t = %s and %s -- never before the first message left" % (
        d["R_shared_reply"], d["R_shared_tiny"]))
    print("   R-OBJECT, two objects moving apart at 369.82 km/s along a Proxima-length span (%.4f ly): the reply reaches "
          "the first sender %.4g s before its message left" % (d["L_ly"], -d["R_object_proxima_s"]))
    print("K2 corridor networks keyed to one frame: %d tested, %d with a closed causal curve (Sylvester; regression on "
          "frame.py); one corridor keyed to another frame beside them spans a %s vector %s (norm %s)" % (
              d["networks_tested"], d["networks_with_loop"], d["past_corridor_span"], d["past_corridor_vector"],
              d["past_corridor_norm"]))
    print("K3 Sun-barycentre observers read a shared-frame teleport to Proxima as %.4g s apart (%.2f d), Proxima %.1f "
          "degrees off the dipole; along the dipole (H-ALONG-DIPOLE) the maximum is %.4g s (%.2f d); for observers on "
          "Earth, +/- %.3g s over the year" % (-d["K3_lead_s"], -d["K3_lead_s"] / 86400.0, d["theta_deg"],
                                               -d["K3_along_dipole_s"], -d["K3_along_dipole_s"] / 86400.0,
                                               d["K3_annual_earth_s"]))
    print("   frame.py's grade, H-FRAME clause 2a: %s" % d["grade_clause2a"])


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

    d = compute()
    chk("K1 R-OBJECT: a reply keyed to the replier's (B's) rest frame reaches the first sender before its message left "
        "(t = %s at v = 3/5 c)" % d["R_object_reply"], d["R_object_reply"] < 0)
    chk("keyed to one shared frame the same construction never returns early (t = %s, %s)" % (
        d["R_shared_reply"], d["R_shared_tiny"]), d["R_shared_reply"] >= 0 and d["R_shared_tiny"] >= 0, ctl=True)
    chk("K2: %d random rank-3 corridor networks keyed to one frame, %d with a closed causal curve (Sylvester; a "
        "regression on frame.py)" % (d["networks_tested"], d["networks_with_loop"]),
        d["networks_tested"] == 200 and d["networks_with_loop"] == 0)
    chk("K2: one corridor keyed to a different frame beside a shared-frame one spans a timelike vector -- the loop "
        "returns (%s, norm %s)" % (d["past_corridor_span"], d["past_corridor_norm"]),
        d["past_corridor_span"] == "timelike", contrast=True)
    chk("K3: two owners agree on the barycentre's separation along Proxima's direction -- cmbframe's vector form "
        "%.6g s, frame.py's along-dipole form x cos theta %.6g s (within gamma)" % (-d["K3_lead_s"],
                                                                                   -d["K3_owner_scaled_s"]),
        abs(d["K3_lead_s"] / d["K3_owner_scaled_s"] - 1) < 1e-5 and d["K3_lead_s"] < 0)
    structural.append("K1 is one closed form, t = -u L: R-OBJECT at 1e-6 c gives %s (first counted as a second check)"
                      % d["R_object_tiny"])
    structural.append("R-OBJECT's early return over a Proxima-length span at 369.82 km/s (%.4g s) equals the "
                      "along-dipole separation (%.4g s) up to gamma: one formula, beta L / c (first counted)" % (
                          -d["R_object_proxima_s"], -d["K3_along_dipole_s"]))
    structural.append("the relativity of simultaneity (LSV p.11, READ): 'instantaneous' for two separated places holds "
                      "for the observers of one family of frames only (premise H-LORENZ-OBSERVERS)")
    structural.append("frame.py's grade, clause 1 O-LOOP: %s" % d["grade_clause1"][:160])
    structural.append("no speed of the teleport, carrier, hold or rate is priced here (M's objection, item 94)")
    structural.append("chronology protection for R-OBJECT is OPEN (Hawking's conjecture, READ-VIA-RESTATEMENT in "
                      "frame.py)")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("causal.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
    return n_fail == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    else:
        report()
