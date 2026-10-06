#!/usr/bin/env python3
"""
causal.py -- the causality thread (M-RULINGS item 94: "Do you want to take up the causality thread next? - yes").
Deduced, computed, READ.  Not seated; not verified.  M's words are carried as hypotheses, never as results.

M (item 94, verbatim): "there is no movement in warp travel, it is a teleportation that happens instantaneously
relative to the object teleporting, AND all observers of the same dimension of that objects existence".  Carried as
H-NO-MOVEMENT and H-INSTANTANEOUS.  NOTHING HERE PRICES A SPEED: no carrier, no hold, no rate.  The only question asked
is the one M said yes to -- what "instantaneous" does to "before" and "after" -- and it is asked of the board's own
frame.py (docket 68, agent A2-frame; IMPORTED, never rebuilt), which already holds the test.

WHAT FOLLOWS THE WORK
  * ONE SHARED "NOW" MAKES M'S TELEPORTATION CAUSALLY SAFE, HOWEVER OFTEN IT IS REPEATED (K2).  If every teleport is
    instantaneous in ONE frame for the whole dimension (R-SHARED), no chain of teleports can return before it left:
    frame.antitelephone's reply keyed to that frame arrives at t = 0, never earlier; and every network of corridors
    keyed to one frame is free of closed causal curves (frame.cosmic_keyed_rank_n_is_safe: 0 of 200 random rank-3
    networks, exact arithmetic).  So M's H-CORRIDOR-REPEATABLE (item 90) is safe on this reading.  This is the
    published resolution: paradoxes need that "given an arbitrary reference frame, it is always possible to send a
    tachyon backward in time in that frame", and "there can be no paradox if, in one particular reference frame,
    tachyons can only propagate forward in time" (Liberati-Sonego-Visser, READ, p.12).
  * THE BOARD ALREADY HOLDS A CANDIDATE FOR THAT FRAME: the cosmic rest frame (frame.py, H-CMB-IS-COSMIC; the CMB dipole
    369.82 km/s, READ-VIA-RESTATEMENT of Planck 2018).  M's charter hypothesis H-FRAME ("a preferred frame exists") is
    exactly what R-SHARED needs.
  * WHAT "ALL OBSERVERS" COSTS (K3).  For two places apart, "instantaneous" can hold exactly in one frame only (the
    relativity of simultaneity: for spacelike-separated events "it is always possible to find another frame where E1
    and E2 are simultaneous" and others where the order reverses, LSV p.11).  Observers moving relative to the shared
    frame read the departure and the arrival as apart by gamma v L / c^2: for the Sun's barycentre against the cosmic
    frame, over the board's Proxima span, 1.65e5 s (1.9 days), 1.52e5 to 1.78e5 s over Earth's year (frame.py's
    annual range).  On R-SHARED those observers disagree about the timing but never see a loop.
  * Boundary (item 82): R-OBJECT -- each teleport instantaneous in its OWN object's rest frame -- is the reading the
    board cannot make safe.  Two objects in relative motion, each teleporting "instantaneously relative to" itself,
    close a loop: frame.antitelephone's reply keyed to the sender's frame arrives BEFORE the first message left
    (t = -3/5 at v = 3/5 c), and at ANY nonzero relative speed (computed down to 1e-6 c).  Over Proxima at the
    Sun's cosmic speed the return would arrive 1.65e5 s before it was sent.  This is LSV's tachyonic anti-telephone
    (p.12); whether chronology protection forbids it is OPEN (Hawking's conjecture, READ-VIA-RESTATEMENT in frame.py).

THE QUESTION FOR M (pause for the answer): M's words name both "relative to the object teleporting" and "all
observers of the same dimension".  Under the relativity of simultaneity these agree only if one frame serves the
whole dimension.  Is the "now" of the teleport one shared now for the dimension (R-SHARED: safe), or each object's own
(R-OBJECT: loops)?

    python3 causal.py              report
    python3 causal.py --selftest   checks, CONTROLS and CONTRASTS marked, STRUCTURAL printed and not counted

K1 [computed, imported]  frame.reply_arrival / frame.antitelephone (sympy, exact): a reply keyed to frame u returns to
   the sender's worldline at cosmic time -u L (c = 1).  R-OBJECT is u = the replier's velocity; R-SHARED is u = 0.
K2 [computed, imported]  frame.cosmic_keyed_rank_n_is_safe(rank, trials): corridors with no time component in one frame
   span no causal vector (Sylvester), so no closed causal curve; frame.past_corridor_witness: ONE corridor keyed to
   another frame beside a shared-frame one spans a timelike vector (the loop) -- the contrast.
K3 [computed, imported]  frame.cmb_coordinate_past(L_ly, v_kms) with L = phase1's Proxima span (imported) and frame.py's
   velocities (369.82 km/s; the annual 340.65 .. 399.08 km/s).
READ this pass: Liberati, Sonego, Visser, "Faster-than-c signals, special relativity, and causality", gr-qc/0107091v2,
   alphaXiv: p.11 (no absolute order for spacelike events; the frame where they are simultaneous), p.12 (the
   anti-telephone; "there can be no paradox if, in one particular reference frame, tachyons can only propagate forward
   in time"), pp.12-13 footnote 16 (a preferred frame "can make good physical sense" with "good physical reasons"),
   p.10 (absolute simultaneity "essentially due to the introduction of a preferred frame"), p.16 (stable causality:
   a global time function excludes closed timelike curves).

NAMED HYPOTHESES
  M's: H-NO-MOVEMENT, H-INSTANTANEOUS (item 94); H-CORRIDOR-REPEATABLE, H-CORRIDOR-CONTAINS-P2 (item 90); H-FRAME (the
  charter's, tested in frame.py).  The board's readings of H-INSTANTANEOUS: R-SHARED, R-OBJECT (named, M to choose).
  frame.py's: H-CMB-IS-COSMIC (H1, H2 of D67).  H-LORENZ-OBSERVERS: observers in the dimension relate by Lorentz
  transformations (the premise of K3; if M's dimension's observers do not, K3 does not apply).
"""

import contextlib
import importlib.util
import io
import math
import os
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)

V_CMB_KMS = 369.82               # frame.py's value (its header; D67 grade cmb-dipole-370kms)
V_ANNUAL_KMS = (340.65, 399.08)  # frame.py's annual range (its header, D67 H2)
C_KMS = 299792.458
YEAR_S = 365.25 * 86400.0        # frame.cmb_coordinate_past's own year
LY_M = 9.4607304725808e15        # IAU light year (standard), to express phase1's span in ly


def _load(name, path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    m = importlib.util.module_from_spec(spec)
    saved = list(sys.path)
    try:
        sys.path.insert(0, WD)
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
        _CACHE["phase1"] = _load("phase1", os.path.join(WD, "phase1.py"), "wd_phase1_causal")
    return _CACHE["frame"], _CACHE["phase1"]


def compute():
    fr, p1 = owners()
    saved = list(sys.path)
    sys.path[:0] = [D68, WD]          # frame.py imports corridors.py lazily, by bare name
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            return _compute(fr, p1)
    finally:
        sys.path[:] = saved


def _compute(fr, p1):
    L_ly = p1.L_PROXIMA / LY_M
    beta = V_CMB_KMS / C_KMS
    obj_v, shared_v = fr.antitelephone()                               # v = 3/5, L = 1 (frame's own)
    tiny = Fr(1, 10 ** 6)
    obj_tiny = fr.reply_arrival(tiny, tiny)
    shared_tiny = fr.reply_arrival(Fr(0), tiny)
    b_frac = Fr(beta).limit_denominator(10 ** 12)
    obj_prox_yr = fr.reply_arrival(b_frac, b_frac, Fr(L_ly).limit_denominator(10 ** 9))
    tested, bad = fr.cosmic_keyed_rank_n_is_safe(3, 200)
    kind, vec, nrm = fr.past_corridor_witness()
    k3 = fr.cmb_coordinate_past(L_ly, V_CMB_KMS)[0]
    k3_annual = [fr.cmb_coordinate_past(L_ly, v)[0] for v in V_ANNUAL_KMS]
    return {"L_ly": L_ly, "beta": beta, "R_object_reply": obj_v, "R_shared_reply": shared_v,
            "R_object_tiny": obj_tiny, "R_shared_tiny": shared_tiny,
            "R_object_proxima_s": float(obj_prox_yr) * YEAR_S,
            "networks_tested": tested, "networks_with_loop": bad,
            "past_corridor_span": kind, "past_corridor_vector": vec, "past_corridor_norm": nrm,
            "K3_proxima_s": k3, "K3_annual_s": k3_annual}


def report():
    d = compute()
    print("causal.py -- the causality thread (M item 94; not verified; not seated).  No speed is priced.\n")
    print("K1 a reply keyed to the replier's own frame (R-OBJECT) returns at t = %s (v = 3/5 c, L = 1); at 1e-6 c, t = %s"
          % (d["R_object_reply"], d["R_object_tiny"]))
    print("   keyed to one shared frame (R-SHARED): t = %s and %s -- never before the first message left" % (
        d["R_shared_reply"], d["R_shared_tiny"]))
    print("   R-OBJECT over Proxima (%.4f ly) at the Sun's cosmic speed: the reply arrives %.4g s before it was sent" % (
        d["L_ly"], -d["R_object_proxima_s"]))
    print("K2 corridor networks keyed to one frame: %d tested, %d with a closed causal curve; one corridor keyed to another "
          "frame beside them spans a %s vector %s (norm %s)" % (d["networks_tested"], d["networks_with_loop"],
                                                                 d["past_corridor_span"], d["past_corridor_vector"],
                                                                 d["past_corridor_norm"]))
    print("K3 observers moving with the Sun's barycentre read a shared-frame teleport to Proxima as %.4g s apart (%.2f d); "
          "over Earth's year %.4g to %.4g s" % (-d["K3_proxima_s"], -d["K3_proxima_s"] / 86400.0,
                                                -d["K3_annual_s"][0], -d["K3_annual_s"][1]))


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
    chk("K1 R-OBJECT: a reply keyed to the replier's own frame arrives before the first message left (t = %s at "
        "v = 3/5 c)" % d["R_object_reply"], d["R_object_reply"] < 0)
    chk("K1 R-OBJECT: and at any nonzero relative speed (t = %s at 1e-6 c)" % d["R_object_tiny"],
        d["R_object_tiny"] < 0)
    chk("keyed to one shared frame the same construction never returns early (t = %s, %s)" % (
        d["R_shared_reply"], d["R_shared_tiny"]), d["R_shared_reply"] >= 0 and d["R_shared_tiny"] >= 0, ctl=True)
    chk("K2: %d random rank-3 corridor networks keyed to one frame, %d with a closed causal curve (exact)" % (
        d["networks_tested"], d["networks_with_loop"]), d["networks_tested"] == 200 and d["networks_with_loop"] == 0)
    chk("K2: one corridor keyed to a different frame beside a shared-frame one spans a timelike vector -- the loop "
        "returns (%s, norm %s)" % (d["past_corridor_span"], d["past_corridor_norm"]),
        d["past_corridor_span"] == "timelike", contrast=True)
    chk("K3: over the Proxima span, Sun-barycentre observers read a shared-frame teleport as %.4g s apart, matching "
        "beta L / c (%.4g s) to gamma" % (-d["K3_proxima_s"], d["beta"] * d["L_ly"] * YEAR_S),
        abs(-d["K3_proxima_s"] / (d["beta"] * d["L_ly"] * YEAR_S) - 1) < 1e-5)
    chk("K1: R-OBJECT over Proxima at the Sun's cosmic speed returns %.4g s early, equal to K3's separation within "
        "gamma" % (-d["R_object_proxima_s"]), abs(d["R_object_proxima_s"] / d["K3_proxima_s"] - 1) < 1e-5)
    structural.append("the relativity of simultaneity (LSV p.11, READ): two separated events are simultaneous in "
                      "exactly one family of frames -- 'instantaneous for all observers' holds in one frame (premise "
                      "H-LORENZ-OBSERVERS)")
    structural.append("no speed, carrier, hold or rate is priced here (M's objection, item 94)")
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
