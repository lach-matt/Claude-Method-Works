#!/usr/bin/env python3
"""d_minus.py -- item 231: the open mouth's other orientation, D-, computed.  M: "Do the computations for D-. I want to
say yes to D+, but we have no choice but to confirm by computing D-".  Worked in the conversation (computed; flat-limit
bank, with the warp part's sign deduced from two_sided.py T4; not verified by a separate session); 2026-10-11.

D+ is corridor_shape's orientation, the one in which the seated corridor is the open mouth's body (open_mouth O4, O5).
D- is the same sheet with its normal reversed: every flat-limit stress negated (O4).  A D- body needs, all along it
from the throat to a rim, energy and both null energies >= 0 -- in D+ terms, all three <= 0.  Only the radial part
depends on the shape's curvature Y''; the tangential is fixed by (r, Y, Y') alone (corridor_shape S1).  The warp part
adds to the energy and the radial null energy only, never to the tangential (two_sided T4: rho + p_theta = 0 from the
warp), so the tangential obstruction below holds with the warp included at that order.

  DM0 (read) M's item-231 words, verbatim in the rulings file.
  DM1 (computed) The marginal family in D-: 40 shoots (start depth 0.1-1.5m, start slope 0 to -4, the radial null
     energy held at 0 or at +0.002 in D-).  None is a D- body.  Every member has D-'s energy and tangential null energy
     negative somewhere along it, including the members that reach a rim inside the photon sphere.
  DM2 (computed, on the banked columns nearest the throat, no interpolation) A corridor flat at the throat -- the
     constant-depth corridor D+ flattens into (rim_profile P4b) -- has D-'s tangential null energy negative at every
     depth, close to -0.49 Y (2/kappa^2 per m) at r = 2.005m: -4.889e-3 at Y = 0.01m, -0.5027 at 1m.  D- keeps it
     non-negative only at a proper angle tan t >= tan t*, with tan t* = 0.983-0.991 Y at r = 2.005m, falling to
     0.854-0.866 Y at 2.1m: the corridor must tilt by at least its own depth.
  DM3 (computed; the limit deduced) So, going inward, a D- corridor's depth must grow.  The least steep admissible path,
     followed from r = 2.3m to the bank's first column, grows as (r - 2m)^-0.87 to (r - 2m)^-0.96: from 0.001m to
     0.053m, from 0.01m to 0.509m, from 0.05m to 1.724m.  With tan t* ~ Y and sqrt(B) ~ 1/(r - 2m) at the horizon,
     dY/dr <= -Y/(r - 2m) to leading order, so Y grows at least as (r - 2m)^-1 and is infinite at the throat.  No D-
     corridor reaches the throat at a finite depth.  Depth zero there is our plane itself, which item 179 excludes.
  DM5 (computed; the critic's check in the conversation) The other tilt: a slope > 0, the depth shrinking going in,
     never admits D-'s tangential null energy >= 0 -- at every banked column, depth 0.01-1m, slope 1e-3 to 1e6 (378
     points), it is negative, and more so than flat.  So DM2's steep negative tilt is the only admissible one, and DM3
     covers every D- path, not only the least steep: any admissible path from the same point lies at or above it going
     in (comparison, deduced).  A corridor whose depth shrank to zero at the throat would in any case be our plane
     there, which item 179 excludes.
  DM4 (deduced from DM1-DM3, DM5) D- has no body joined to the throat, so D+ is the only orientation in which the open
     mouth has one.  That is the computation M asked for before confirming D+ (item 231).  In D- the tangential null
     energy is negative along the corridor's whole length near the throat, so a partner would be needed on every
     grazing ray there; D+ needs none along its body (open_mouth O4, O5), and its rim's negative line is the one-sided
     view's appearance (two_sided T1, items 212, 214).

What this does not show.
  - The flat-limit bank as corridor_shape reads it.  The y-derivatives are interpolated between columns, with known
    errors near the throat (corridor_shape S0's note), so DM2 uses banked columns only.
  - DM3's limit beyond the bank's first column (2.005m) is deduced from the threshold law, not computed.
  - Static sheets, thin, Z2 at the joint as open_mouth.py has it.

Imports corridor_shape.py (its bank, curvature and stresses: D+ is its orientation, D- the same sheet with its normal
reversed, every flat-limit stress negated -- open_mouth.py O4) by path.  Stdlib + sympy (through corridor_shape).
python3 d_minus.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M231 = "Do the computations for D-. I want to say yes to D+, but we have no choice but to confirm by computing D-"


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


CS = _load(os.path.join(HERE, "corridor_shape.py"), "dm_cs")
KS = CS.curvature_exprs()
BULK = CS.Bulk(CS.load_bank())
COLS = [2.005, 2.01, 2.02, 2.04, 2.06, 2.08, 2.1]          # banked columns: exact values, no interpolation (S0)


def d_minus(r, Y, Y1, Y2):
    """D-'s stresses (rho, rho + p_r, rho + p_theta) in 2/kappa5^2 per m: the D+ sheet's, negated (open_mouth O4)"""
    s = CS.stresses(KS, BULK.at(r, Y), Y1, Y2)
    sgn = 1 if MUT.get("orientation_kept") else -1
    return tuple(sgn * v for v in s)


def tangential(r, Y, Y1):
    return d_minus(r, Y, Y1, 0.0)[2]                         # independent of Y'' (corridor_shape S1)


# ------------------------------------------------------------------------------------------- DM1 the marginal family
SHOOT_D = (0.1, 0.25, 0.5, 1.0, 1.5)
SHOOT_S = (0.0, -1.0, -2.0, -4.0)
SHOOT_M = (0.0, -0.002)


def marginal_family():
    """corridor_shape's marginal shoot (radial null energy held: D+'s = margin <= 0, so D-'s >= 0) over start depths,
    slopes and margins: is any member a D- body -- energy and both null energies >= 0 in D- all along, with a rim?"""
    out = {}
    for d in SHOOT_D:
        for s0 in SHOOT_S:
            for mg in SHOOT_M:
                m = CS.marginal(KS, BULK, d, margin=mg, slope0=s0, rmax=3.2)
                rows = m["rows"]
                sgn = 1 if MUT.get("orientation_kept") else -1
                worst = [min(sgn * row[k] for row in rows) for k in (3, 4, 5)] if rows else [None] * 3
                body = bool(rows) and m["rim"] is not None and all(w >= -1e-12 for w in worst)
                out[(d, s0, mg)] = dict(rim=m["rim"], worst=worst, body=body)
    return out


# ------------------------------------------------------------------------------------------- DM2 the throat joint
def flat_joint():
    """a corridor flat at the throat (slope 0, the constant-depth corridor D+ flattens into, rim_profile P4b): D-'s
    tangential null energy at the banked columns nearest the throat, over depth"""
    return {(r, Y): tangential(r, Y, 0.0) for r in COLS[:3] for Y in (0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 1.5)}


def threshold(r, Y):
    """the least steep slope (s < 0) at which D-'s tangential null energy is >= 0, and its proper angle tan t* =
    |s*|/sqrt(B); None if no slope reaches it"""
    lo, hi = -1e6, 0.0
    if tangential(r, Y, lo) < 0:
        return None
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if tangential(r, Y, mid) >= 0 else (lo, mid)
    B = BULK.at(r, Y)["B"][0]
    return dict(s=lo, tan=abs(lo) / math.sqrt(B))


def thresholds():
    return {(r, Y): threshold(r, Y) for r in COLS for Y in (0.01, 0.05, 0.1, 0.25)}


# ------------------------------------------------------------------------------------------- DM3 reaching the throat
def inward(Y0, r0=2.3, r_end=2.005):
    """the least steep admissible D- path followed inward from r0 toward the throat (going inward with slope s < 0 the
    depth grows): where does it go?"""
    r, Y, path = r0, Y0, [(r0, Y0)]
    while r > r_end + 1e-12:
        th = threshold(r, Y)
        if th is None:
            return dict(path=path, end="no admissible slope", Y_end=Y, r_end=r)
        h = min(0.002, (r - 2.0) / 50, r - r_end)
        s = th["s"] if not MUT.get("shallow_inward") else 0.0
        Y, r = Y - s * h, r - h
        path.append((r, Y))
        if Y > 2.5:
            return dict(path=path, end="left the verified layer", Y_end=Y, r_end=r)
    return dict(path=path, end="reached r_end", Y_end=Y, r_end=r)


POS_SLOPES = (1e-3, 1e-2, 0.1, 1.0, 10.0, 100.0, 1e3, 1e4, 1e6)
POS_DEPTHS = (0.01, 0.05, 0.1, 0.25, 0.5, 1.0)


def other_tilt():
    """DM5: D-'s tangential null energy at positive slopes (the depth shrinking going in), every banked column"""
    return {(r, Y, sl): tangential(r, Y, -sl if MUT.get("tilt_flipped") else sl)
            for r in COLS for Y in POS_DEPTHS for sl in POS_SLOPES}


def growth_exponent(res):
    """fit Y ~ (r - 2m)^-p over the path's inner half"""
    pts = [(math.log(r - 2.0), math.log(Y)) for r, Y in res["path"] if r < 2.15]
    n = len(pts)
    if n < 3:
        return float("nan")
    mx, my = sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n
    return -sum((p[0] - mx) * (p[1] - my) for p in pts) / sum((p[0] - mx) ** 2 for p in pts)


def compute():
    fam = marginal_family()
    paths = {Y0: inward(Y0) for Y0 in (0.001, 0.01, 0.05)}
    return dict(family=fam, flat=flat_joint(), thr=thresholds(), paths=paths, tilt=other_tilt(),
                exps={Y0: growth_exponent(p) for Y0, p in paths.items()})


def report(o):
    print("d_minus.py -- the open mouth's D- orientation (item 231)\n")
    fam = o["family"]
    print("DM1 the marginal family in D- (%d members): bodies %d" % (len(fam), sum(v["body"] for v in fam.values())))
    for k, v in fam.items():
        print("   d %.2f s0 %+.1f margin %+.3f rim %-6s min D- (rho, radial, tangential) %s" % (
            k[0], k[1], k[2], "%.3f" % v["rim"] if v["rim"] else "none", ["%+.3e" % w for w in v["worst"]]))
    print("\nDM2 a flat joint at the throat, D-'s tangential null energy (2/kappa^2 per m):")
    for r in COLS[:3]:
        print("   r %.3f: %s" % (r, "  ".join("Y %.2f %+.3e" % (Y, o["flat"][(r, Y)]) for Y in (0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 1.5))))
    print("   the proper angle D- needs, tan t* (and tan t*/Y):")
    for r in COLS:
        print("   r %.3f: %s" % (r, "  ".join("Y %.2f %.4f (%.3f)" % (Y, o["thr"][(r, Y)]["tan"], o["thr"][(r, Y)]["tan"] / Y)
                                             for Y in (0.01, 0.05, 0.1, 0.25))))
    print("\nDM3 the least steep admissible D- path followed inward from r = 2.3:")
    for Y0, p in o["paths"].items():
        print("   Y(2.3) = %.3f -> %s at r %.4f with Y %.3f; Y ~ (r - 2m)^-%.2f" % (Y0, p["end"], p["r_end"], p["Y_end"], o["exps"][Y0]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("DM0 M's item-231 words verbatim in the rulings file", M231 in rul)
    fam = o["family"]
    ok = len(fam) == 40 and not any(v["body"] for v in fam.values())
    ok &= all(v["worst"][0] < 0 and v["worst"][2] < 0 for v in fam.values() if v["worst"][0] is not None)
    ok &= any(v["rim"] is not None and v["rim"] < 3.0 for v in fam.values())
    add("DM1 none of the 40 marginal members is a D- body; every one has D-'s energy and tangential null energy negative "
        "somewhere, including members whose rim lies inside the photon sphere", ok)
    fl, th = o["flat"], o["thr"]
    ok = all(v < 0 for v in fl.values())
    ok &= ("%.3e" % fl[(2.005, 0.01)], "%.4f" % fl[(2.005, 1.0)]) == ("-4.889e-03", "-0.5027")
    ok &= all(0.48 < -fl[(2.005, Y)] / Y < 0.57 for Y in (0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 1.5))
    rat = lambda r: [th[(r, Y)]["tan"] / Y for Y in (0.01, 0.05, 0.1, 0.25)]
    ok = ok and all(v is not None for v in th.values())
    ok = ok and "%.3f-%.3f" % (min(rat(2.005)), max(rat(2.005))) == "0.983-0.991"
    ok = ok and "%.3f-%.3f" % (min(rat(2.1)), max(rat(2.1))) == "0.854-0.866"
    add("DM2 a flat joint at the throat has D-'s tangential null energy negative at every depth (-4.889e-3 at 0.01m, "
        "-0.5027 at 1m, near -0.49 Y); D- needs tan t >= 0.983-0.991 Y at 2.005m, 0.854-0.866 Y at 2.1m", ok)
    ps, ex = o["paths"], o["exps"]
    ok = all(p["end"] == "reached r_end" for p in ps.values())
    ok = ok and ["%.3f" % ps[Y0]["Y_end"] for Y0 in (0.001, 0.01, 0.05)] == ["0.053", "0.509", "1.724"]
    ok &= all(v == v for v in ex.values()) and "%.2f" % min(ex.values()) == "0.87" and "%.2f" % max(ex.values()) == "0.96"
    ok &= all(ps[Y0]["Y_end"] / Y0 > 30 for Y0 in (0.001, 0.01, 0.05))
    add("DM3 the least steep admissible D- path inward grows from 0.001 / 0.01 / 0.05m to 0.053 / 0.509 / 1.724m at "
        "2.005m, as (r - 2m)^-0.87 to ^-0.96: no D- corridor reaches the throat at a finite depth", ok)
    tl = o["tilt"]
    ok = len(tl) == 378 and all(v < 0 for v in tl.values())
    ok &= all(tl[(r, Y, sl)] < o["flat"][(r, Y)] for r in COLS[:3] for Y in POS_DEPTHS for sl in POS_SLOPES)
    add("DM5 the other tilt: at slopes > 0 (depth shrinking going in) D-'s tangential null energy is negative at all 378 "
        "points (7 columns, depth 0.01-1m, slope 1e-3 to 1e6), below the flat joint's: DM2's tilt is the only admissible "
        "one", ok)
    return res


MUTANTS = {"orientation_kept": "D- read without negating the stresses (D+ again)",
           "shallow_inward": "the inward path taken flat (slope 0), ignoring D-'s tangential threshold",
           "tilt_flipped": "the other tilt read with the slope's sign reversed"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-16s %-70s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
