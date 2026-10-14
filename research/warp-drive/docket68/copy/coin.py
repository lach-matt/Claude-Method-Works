#!/usr/bin/env python3
"""coin.py -- DOCKET 68, M-RULINGS items 117-118: the test of M's coin (H-NEC-COIN) -- the null energy condition along
a whole path through the one-way corridor, from position 1's side to position 2's.  Deduced, computed and READ;
verified once; SEATED (ledger.py section 8p).  Write-up: COIN.md.

M's words (verbatim in the rulings file): item 117 "An NEC is never violated, between two entangled positions the NEC
is like a coin, each position sits on a separate side. That action is that the coin flips. The NEC appears broken, but
is not"; item 118 "Yes, run it".

THE TEST.  The corridor is Bronnikov-Kim's eq. (17) horizon member (plane.py; H-BK-CORRIDOR).  Along a radial null path
with affine parameter lambda and conserved energy E (k^t = E/f, k^r = +-E/sqrt(f h), f = 1 - 2m/r, h = g_rr), the
energy the path meets is G_ab k^a k^b = (E^2 / f)(G^r_r - G^t_t), and its average along the whole passage is the
integral of that over lambda (dlambda = sqrt(f h) dr / E), in from position 1's infinity to the throat and out to
position 2's (H-AVERAGED-NEC; the plane's reading, H-PLANE-READING).

WHAT THE WORK FINDS -- THE APPEARANCE ALONG THE WHOLE PATH IN THE PLANE'S READING; KEPT IN THE BULK NEAR THE PLANE
  C1 THE NULL-CONTRACTED EINSTEIN TENSOR HAS ONE SIGN THROUGH THE HORIZON.  G_kk = -2 E^2 (2 r0 - 3m) / (r (2r - 3m)^2)
     (sympy): regular at r = 2m, where it is E^2 (3m - 2 r0)/m^3 (-0.6 E^2 for m = 1, r0 = 1.8), and negative at every r
     for every member with 2 r0 > 3m.  The board's candidate coin flip (OPENING.md, item 117 section: -0.0148 outside,
     +0.0519 inside) was the static frame's factor 1/f; opening.py's O3 had already said "where the inequality
     reverses".  Withdrawn.  The zero of the static combination at r = 2m is the same artifact: the condition fails at
     the horizon too.
  C2 THE ANEC INTEGRAL ALONG THE WHOLE PASSAGE IS NEGATIVE, IN CLOSED FORM.  Per leg (infinity to throat, or throat to
     infinity), integral G_kk dlambda = -(4E/3m) [1 - ((c^2 - 1)/c) artanh(1/c)], c = sqrt(2 r0 / 3m) (closed form
     derived by the verifier; agrees with the quadrature to 15 digits at six members).  m = 1, r0 = 1.8: -0.957356 E/m
     per leg, -1.914712 E/m per passage (G = c = 1); as the plane's effective T_kk = G_kk/8pi, -0.0380920 and -0.0761840.
     Since artanh x < x/(1 - x^2) on (0, 1), the bracket lies in (0, 1): -4E/(3m) < leg < 0 for EVERY member with
     2 r0 > 3m -- the two-way members r0 > 2m included (r0 = 3: -0.502366), m = 0 giving exactly -4E/(3 r0).  So the
     horizon plays no part in the sign: this test cannot tell the one-way corridor from a two-way member.  The most
     negative value is at the Schwarzschild edge r0 -> 3m/2.  This goes against the board's first-written expectation
     (OPENING: "if it holds, the pointwise violation is an appearance along the whole passage too") -- averaging does
     not remove it -- and not against H-NEC-COIN, whose "appears broken" is this reading.
  C3 THE BULK NEAR THE PLANE KEEPS THE CONDITION.  escape.py (section 8m, seated, S3): "With tau = 0: K = -a q exactly,
     the scalar Gauss equation reads R = 0 (met), Codazzi holds, the NEC holds -- on either sign of the tension.  The
     bulk keeps only its vacuum energy (the NEC, saturated); E = -G carries the whole reading".  So: no matter on the
     plane (tau = 0, its NEC trivially kept) and only vacuum in the bulk (NEC saturated) -- locally, under H-RS1, with
     Anderson's objection carrying; a global bulk is BULK5-O1 (existence carried on M's path, item 120).
  C4 THE APPEARANCE IS FORCED (READ).  Friedman, Schleich & Witt, gr-qc/9305017v2, Thm 1 p.3: "If an asymptotically
     flat, globally hyperbolic spacetime (M, g_ab) satisfies the averaged null energy condition, then every causal curve
     from J- to J+ is deformable to gamma0 rel J"; Lemma 2 p.5: no strongly outer trapped surface meets J-(J+_alpha);
     the proof runs on null focusing, so on the plane the binding quantity is G_kk.  PLANE point 1 gives a causal curve
     from P1's J- to P2's J+, both ends flat; so ANY 4D reading of a one-way passage must violate ANEC somewhere, unless
     global hyperbolicity fails (H-GLOBAL-HYPERBOLIC, OPEN).  C2 is what the theorem requires, not a contingent fact
     about this family.  Whether a 5D censorship theorem binds the bulk is NOT READ, OPEN.
  C5 THE CANDIDATE BOTH-FACES CURVE (OPEN).  K = -a q makes the plane umbilic, so K_mn k^m k^n = 0 and the passage's null
     geodesic would also be a bulk null geodesic (standard, NOT READ), along which a Lambda_5 vacuum gives R5_kk = 0:
     one curve reading -1.914712 E/m in the plane and 0 in the bulk.  H-UMBILIC-GEODESIC, the board's, OPEN.
  C6 WHAT THE BOARD ALREADY HOLDS.  Maldacena-Susskind fn.1 p.2 (READ in geometry.py): non-traversability "can be shown
     using the integrated null energy condition"; "If this were not true, the ER=EPR connection would be wrong".  The
     horizon member is one-way traversable and C2 has the integrated condition failing in the plane's reading, so under
     H-ER=EPR the corridor between two entangled positions lies outside Maldacena-Susskind's ER=EPR in that reading
     (bears on geometry.py's O-HOLD grading; not re-graded here).  Gao-Wald fn.3 p.12 (READ in geometry.py): Borde's
     averaged condition may replace the NEC -- its premise fails on the plane and holds, saturated, in the bulk.
  The flip is a metaphor (M's item 120): not an event to compute.  M's "each position on a separate side" is untested:
  in the plane both positions read alike (G_kk depends on r only; equal legs); the causal asymmetry -- a future
  (black-hole) horizon at P1, a past (white-hole) one at P2 -- is the board's candidate for the two sides, OPEN.

NAMED HYPOTHESES
  M's: H-NEC-COIN (117, a metaphor by 120), H-COMPLETE-BULK (120), H-READING-ONLY (86.1), H-CORRIDOR-HORIZON (104).
  The board's: H-BK-CORRIDOR; H-AVERAGED-NEC (the test M approved); H-PLANE-READING (the 4D reading of the brane's
    projected stress); H-RS1 (the bulk statement's scope); H-GLOBAL-HYPERBOLIC, H-ASYMPTOTIC-FLAT-ENDS (C4's premises);
    H-UMBILIC-GEODESIC (C5); H-ER=EPR (MS fn.1, below).

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

ESCAPE_S3 = ("With tau = 0: K = -a q exactly, the scalar Gauss equation reads R = 0 (met), Codazzi holds, the NEC holds "
             "-- on either sign of the tension.  The bulk keeps only its vacuum energy (the NEC, saturated); E = -G "
             "carries the whole reading")
MEMBERS = ((1.0, 1.8), (1.0, 1.6), (1.0, 2.5), (1.0, 3.0), (2.0, 3.6), (1.0, 100.0))


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


def anec_closed(m, r0):
    """-(4/3m) [1 - ((c^2 - 1)/c) artanh(1/c)], c = sqrt(2 r0/3m), per unit E (the verifier's closed form); m = 0 gives
    -4/(3 r0)."""
    import mpmath as mp
    if m == 0:
        return -4.0 / (3 * r0)
    c = mp.sqrt(mp.mpf(2) * r0 / (3 * m))
    return float(-(mp.mpf(4) / (3 * m)) * (1 - ((c * c - 1) / c) * mp.atanh(1 / c)))


def schwarzschild_control():
    """opening._einstein on an independently written Schwarzschild metric: every component of G must vanish."""
    import sympy as sp
    t, r, th, ph, m = sp.symbols("t r theta phi m", positive=True)
    f = 1 - 2 * m / r
    G, R, _ = owners()["opening"]._einstein(sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2), [t, r, th, ph])
    return all(sp.simplify(G[i, j]) == 0 for i in range(4) for j in range(4)) and sp.simplify(R) == 0


def compute():
    import math
    o = owners()
    with contextlib.redirect_stdout(io.StringIO()):
        throats = o["escape"].bk_throats()
    src = open(os.path.join(D68, "bulk", "escape.py"), encoding="utf-8").read()
    gk = g_kk()
    legs = {"m=1,r0=1.8": anec_leg(1.0, 1.8), "m=1,r0=1.6": anec_leg(1.0, 1.6),
            "m=1,r0=1.5+1e-9": anec_leg(1.0, 1.5 + 1e-9)}
    pairs = [(m, r0, anec_leg(m, r0), anec_closed(m, r0)) for m, r0 in MEMBERS]
    sweep = [(r0, anec_leg(1.0, r0)) for r0 in (1.5001, 1.55, 1.7, 1.9, 2.0, 2.2, 4.0, 10.0, 1e3)]
    return {"g_kk": gk, "legs": legs, "passage_m1_r1p8": 2 * legs["m=1,r0=1.8"],
            "T_leg_m1_r1p8": legs["m=1,r0=1.8"] / (8 * math.pi), "T_passage_m1_r1p8": legs["m=1,r0=1.8"] / (4 * math.pi),
            "closed_vs_quad": pairs, "m0": (anec_leg(0.0, 5.0), anec_closed(0, 5.0)), "sweep_m1": sweep,
            "schwarzschild_einstein_zero": schwarzschild_control(),
            "bk_R": [str(t[0]) for t in throats],
            "escape_s3_in_source": " ".join(ESCAPE_S3.split()) in " ".join(src.split())}


def report(d):
    g = d["g_kk"]
    print("coin.py -- items 117-118: the null energy condition along the whole one-way passage")
    print("  G_kk = %s (at the horizon: %s)" % (g["gkk"], g["at_horizon"]))
    print("  values at m = 1, r0 = 1.8: %s;  the static-frame combination: %s" % (
        {k: round(v, 5) for k, v in g["values_m1_r1p8"].items()}, g["frame_comb_values"]))
    for k, v in d["legs"].items():
        print("  ANEC integral of G_kk per leg (E/m, G = c = 1) %s: %.6f" % (k, v))
    print("  whole passage, m = 1, r0 = 1.8: %.6f E/m;  as T_kk = G_kk/8pi: leg %.7f, passage %.7f" % (
        d["passage_m1_r1p8"], d["T_leg_m1_r1p8"], d["T_passage_m1_r1p8"]))
    for m, r0, q, c in d["closed_vs_quad"]:
        print("  m = %g, r0 = %g: quadrature %.12f, closed form %.12f" % (m, r0, q, c))
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
    chk("C1: G_kk for a radial null path is %s (sympy, from opening.py's combination), finite at the horizon (%s)" % (
        g["gkk"], g["at_horizon"]), g["matches"] and "zoo" not in g["at_horizon"] and "oo" not in g["at_horizon"])
    chk("C1: it is negative on both sides of the horizon and at it (m = 1, r0 = 1.8: %s) -- no flip" % (
        {k: round(v, 5) for k, v in vals.items()}), all(v < 0 for v in vals.values()))
    chk("the Einstein pipeline (opening._einstein) gives G = 0, R = 0 on an independently written Schwarzschild metric",
        d["schwarzschild_einstein_zero"], ctl=True)
    worst = max(abs(q - c) for _, _, q, c in d["closed_vs_quad"])
    chk("the quadrature agrees with the closed form at six members, two of them two-way (r0 > 2m) (worst |diff| %.1e)"
        % worst, worst < 1e-12, ctl=True)
    chk("the quadrature at m = 0 gives %.12f against the exact -4/(3 r0) = %.12f (r0 = 5)" % d["m0"],
        abs(d["m0"][0] - d["m0"][1]) < 1e-12, ctl=True)
    chk("C2: the ANEC integral per leg is negative (m = 1, r0 = 1.8: %.6f E/m; r0 = 1.6: %.6f) -- the whole passage "
        "%.6f E/m" % (d["legs"]["m=1,r0=1.8"], d["legs"]["m=1,r0=1.6"], d["passage_m1_r1p8"]),
        d["legs"]["m=1,r0=1.8"] < 0 and d["legs"]["m=1,r0=1.6"] < 0)
    chk("C2: -4/(3m) < leg < 0 on a sweep r0 = 1.5001 ... 1000 (m = 1), through the horizon members and the two-way "
        "ones -- the horizon plays no part in the sign", all(-4.0 / 3 < v < 0 for _, v in d["sweep_m1"]))
    chk("C3: eqs. (13), (17) have R = 0 (computed by escape.bk_throats: %s)" % d["bk_R"], d["bk_R"] == ["0", "0"])
    chk("C3 (READ check): escape.py's seated S3 text from 'With tau = 0' is in its source", d["escape_s3_in_source"])
    structural.append("C1: the static-frame combination changes sign at the horizon (%.4f outside, %.4f inside) -- the "
                      "1/f is inserted by definition in G_kk = (E^2/f) comb, so this restates it (first counted as a "
                      "contrast)" % g["frame_comb_values"])
    structural.append("Schwarzschild (r0 = 3m/2): G_kk = %s -- the factor (2 r0 - 3m) of check 1, so it cannot fail when "
                      "check 1 passes (first counted as a control); there is no throat or passage there" %
                      g["schwarzschild"])
    structural.append("C2: the limit r0 -> 3m/2 from above gives %.6f per leg (-4/3), not 0 -- the negative energy "
                      "gathers at the throat" % d["legs"]["m=1,r0=1.5+1e-9"])
    structural.append("C2: the bracket lies in (0, 1) for c > 1 since 0 < artanh x < x/(1 - x^2) on (0, 1) (term by "
                      "term) -- the analytic form of the sweep")
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
