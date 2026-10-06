#!/usr/bin/env python3
"""coin.py -- DOCKET 68, M-RULINGS items 117-118: the test of M's coin (H-NEC-COIN) -- the null energy condition along
a whole path through the one-way corridor, from position 1's side to position 2's.  Deduced and computed; not
verified; not seated.  Write-up: COIN.md.

M's words (verbatim in the rulings file): item 117 "An NEC is never violated, between two entangled positions the NEC
is like a coin, each position sits on a separate side. That action is that the coin flips. The NEC appears broken, but
is not"; item 118 "Yes, run it".

THE TEST.  The corridor is Bronnikov-Kim's eq. (17) horizon member (plane.py; H-BK-CORRIDOR).  Along a radial null path
with affine parameter lambda and conserved energy E (k^t = E/f, k^r = +-E/sqrt(f h), f = 1 - 2m/r, h = g_rr), the
energy the path meets is G_ab k^a k^b = (E^2 / f)(G^r_r - G^t_t), and its average along the whole passage is the
integral of that over lambda (dlambda = sqrt(f h) dr / E), in from position 1's infinity to the throat and out to
position 2's (H-AVERAGED-NEC; the plane's reading, H-PLANE-READING).

WHAT THE WORK FINDS -- AGAINST THE COIN IN THE PLANE'S READING, BESIDE IT IN THE BULK (item 82: both shown)
  C1 THE ENERGY THE PATH MEETS HAS ONE SIGN THROUGH THE HORIZON.  G_kk = -2 E^2 (2 r0 - 3m) / (r (2r - 3m)^2) (sympy):
     regular at the horizon r = 2m, and negative everywhere for the horizon members (2 r0 > 3m).  The sign change the
     board offered as a candidate coin flip (OPENING.md, item 117 section: -0.0148 outside, +0.0519 inside) was the
     static frame's factor 1/f, which changes sign at the horizon; the null-contracted energy does not.  Withdrawn.
  C2 THE AVERAGE ALONG THE WHOLE PASSAGE IS NEGATIVE.  Each leg (infinity to throat, throat to infinity) gives
     -2 E (2 r0 - 3m) x integral_{r0}^{inf} sqrt((r - 3m/2)/(r - r0)) / (r (2r - 3m)^2) dr: for m = 1, r0 = 1.8 it is
     -0.957356 E (geometric units, m = 1), so the whole passage averages -1.914712 E.  In the plane's reading the
     violation is not local: it holds along the whole path.  Control: Schwarzschild (r0 = 3m/2) has G_kk = 0 exactly.
     The limit r0 -> 3m/2 from above gives -4/3 E per leg, not 0: the negative energy gathers at the throat.
  C3 THE BULK KEEPS THE CONDITION.  escape.py (section 8m, seated, S3): for these throats "the NEC holds -- on either
     sign of the tension. The bulk keeps only its vacuum energy (the NEC, saturated); E = -G carries the whole reading"
     -- locally, under H-RS1 (a global bulk is BULK5-O1, OPEN).  So: the condition appears broken from our plane, along
     the whole passage, and is not broken in the full spacetime the plane sits in.  That is the content of your coin the
     board can show; the flip itself (the action) is not computed.

NAMED HYPOTHESES
  M's: H-NEC-COIN (117), H-READING-ONLY (86.1), H-CORRIDOR-HORIZON (104).
  The board's: H-BK-CORRIDOR; H-AVERAGED-NEC (the test M approved); H-PLANE-READING (the 4D reading of the brane's
    projected stress); H-RS1 (the bulk statement's scope).

USAGE
    python3 coin.py | --selftest | --json
"""

import contextlib
import importlib.util
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
_CACHE = {}

ESCAPE_S3 = ("the NEC holds -- on either sign of the tension. The bulk keeps only its vacuum energy (the NEC, saturated); "
             "E = -G carries the whole reading")


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


def owners():
    """Imported, never copied: opening.py (the corridor's radial null combination, computed from eq. 17), escape.py (R = 0
    and its seated S3 text)."""
    if not _CACHE:
        _CACHE["opening"] = _load(os.path.join(HERE, "opening.py"), "copy_opening_coin")
        _CACHE["escape"] = _load(os.path.join(D68, "bulk", "escape.py"), "d68_escape_coin")
    return _CACHE


def g_kk():
    """G_ab k^a k^b for a radial null path, from opening.bk_radial_nec's combination times E^2 / f."""
    import sympy as sp
    o = owners()
    nec = o["opening"].bk_radial_nec()
    r, r0, m, E = sp.symbols("r r0 m E", positive=True)
    comb = sp.sympify(nec["comb"], locals={"r": r, "r0": r0, "m": m})
    f = 1 - 2 * m / r
    gkk = sp.factor(sp.simplify(E ** 2 / f * comb))
    target = -2 * E ** 2 * (2 * r0 - 3 * m) / (r * (2 * r - 3 * m) ** 2)
    at_horizon = sp.simplify(gkk.subs(r, 2 * m))
    vals = {rr: float(gkk.subs({E: 1, m: 1, r0: 1.8, r: rr})) for rr in (1.85, 1.9, 2.0, 3.0, 10.0)}
    return {"gkk": str(gkk), "matches": sp.simplify(gkk - target) == 0, "at_horizon": str(at_horizon),
            "values_m1_r1p8": vals, "frame_comb_values": (nec["outside_r3"], nec["inside_r1p9"]),
            "schwarzschild": str(sp.simplify(gkk.subs(r0, sp.Rational(3, 2) * m)))}


def anec_leg(m, r0):
    """-2 (2 r0 - 3m) x int_{r0}^inf sqrt((r - 3m/2)/(r - r0)) / (r (2r - 3m)^2) dr, per unit E; r = r0 + u^2."""
    import mpmath as mp
    mp.mp.dps = 30
    f = lambda u: 2 * mp.sqrt(r0 + u * u - 1.5 * m) / ((r0 + u * u) * (2 * (r0 + u * u) - 3 * m) ** 2)
    return float(-2 * (2 * r0 - 3 * m) * mp.quad(f, [0, 1, 10, mp.inf]))


def compute():
    o = owners()
    with contextlib.redirect_stdout(io.StringIO()):
        throats = o["escape"].bk_throats()
    src = open(os.path.join(D68, "bulk", "escape.py"), encoding="utf-8").read()
    gk = g_kk()
    legs = {"m=1,r0=1.8": anec_leg(1.0, 1.8), "m=1,r0=1.6": anec_leg(1.0, 1.6),
            "m=1,r0=1.5+1e-9": anec_leg(1.0, 1.5 + 1e-9)}
    return {"g_kk": gk, "legs": legs, "passage_m1_r1p8": 2 * legs["m=1,r0=1.8"],
            "bk_R": [str(t[0]) for t in throats],
            "escape_s3_in_source": " ".join(ESCAPE_S3.split()) in " ".join(src.split())}


def report(d):
    g = d["g_kk"]
    print("coin.py -- items 117-118: the null energy condition along the whole one-way passage")
    print("  G_kk = %s (at the horizon: %s)" % (g["gkk"], g["at_horizon"]))
    print("  values at m = 1, r0 = 1.8: %s;  the static-frame combination: %s" % (
        {k: round(v, 5) for k, v in g["values_m1_r1p8"].items()}, g["frame_comb_values"]))
    for k, v in d["legs"].items():
        print("  per-leg average (per E, geometric) %s: %.6f" % (k, v))
    print("  whole passage, m = 1, r0 = 1.8: %.6f E" % d["passage_m1_r1p8"])
    print("  escape.py S3 (seated), in its source: %s" % d["escape_s3_in_source"])


def selftest(d):
    n_pass = n_fail = n_ctl = n_con = 0
    structural = []

    def chk(label, ok, ctl=False, contrast=False):
        nonlocal n_pass, n_fail, n_ctl, n_con
        tag = "CONTROL: " if ctl else ("CONTRAST: " if contrast else "")
        print("  %s %s%s" % ("ok  " if ok else "FAIL", tag, label))
        n_pass += bool(ok)
        n_fail += not ok
        n_ctl += bool(ctl)
        n_con += bool(contrast)

    g = d["g_kk"]
    vals = g["values_m1_r1p8"]
    chk("C1: the energy a radial null path meets is %s (sympy, from opening.py's combination), finite at the horizon "
        "(%s)" % (g["gkk"], g["at_horizon"]), g["matches"] and "zoo" not in g["at_horizon"] and "oo" not in g["at_horizon"])
    chk("C1: it is negative on both sides of the horizon (m = 1, r0 = 1.8: %s) -- no flip" % (
        {k: round(v, 5) for k, v in vals.items()}), all(v < 0 for v in vals.values()))
    chk("the static-frame combination does change sign at the horizon (%.4f outside, %.4f inside): the board's candidate "
        "flip was the frame's factor 1/f" % g["frame_comb_values"],
        g["frame_comb_values"][0] < 0 < g["frame_comb_values"][1], contrast=True)
    chk("C2: the average along each leg is negative (m = 1, r0 = 1.8: %.6f; r0 = 1.6: %.6f) -- along the whole passage "
        "%.6f E" % (d["legs"]["m=1,r0=1.8"], d["legs"]["m=1,r0=1.6"], d["passage_m1_r1p8"]),
        d["legs"]["m=1,r0=1.8"] < 0 and d["legs"]["m=1,r0=1.6"] < 0)
    chk("Schwarzschild (r0 = 3m/2) meets no energy along the path: G_kk = %s" % g["schwarzschild"],
        g["schwarzschild"] == "0", ctl=True)
    chk("C3: escape.py's seated S3 text (the bulk keeps the NEC) is in its source, and eqs. (13), (17) have R = 0 (%s)" %
        d["bk_R"], d["escape_s3_in_source"] and d["bk_R"] == ["0", "0"])
    structural.append("C2: the limit r0 -> 3m/2 from above gives %.6f per leg (-4/3), not 0 -- the negative energy "
                      "gathers at the throat" % d["legs"]["m=1,r0=1.5+1e-9"])
    structural.append("C3's bulk statement is escape.py's analytic result (section 8m), locally under H-RS1; not "
                      "recomputed here")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("coin.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
    return n_fail == 0


def main(argv):
    d = compute()
    if "--json" in argv:
        print(json.dumps(d, indent=1, default=str))
        return 0
    if "--selftest" in argv:
        return 0 if selftest(d) else 1
    report(d)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
