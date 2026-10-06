#!/usr/bin/env python3
"""plane.py -- DOCKET 68, M-RULINGS item 101: the walls under M's answers, and the corridor's cost as "total our plane
can read" (answer 11).  Deduced, computed and READ; not verified; not seated.  Write-up: PLANE.md.

M's words, item 101 (verbatim in the rulings file): "11 - total our plane can read"; "1 - I suspect that a corridor can
be made under the same conditions used to make one larger"; "6 - ... assess the README size and widen the corridor to
the necessary size, no more and no less"; "7 - distance is irrelevant. The device only sees the two positions as one";
"5 - no. The mouths can be in separate universes".  Item 86 answer 1: the warp must "appear to contain" negative
energy (H-READING-ONLY).

WHAT FOLLOWS THE WORK (item 82: lead with what passes)
  P1 BY YOUR MEASURE, A CORRIDOR CAN COST ZERO, AT ANY README SIZE.  Bronnikov-Kim's static throat, eq. (17) (READ here:
     "a symmetric wormhole geometry for any r0 > 2m >= 0, or for any r0 > 0 in case m < 0", p.6 per escape.py), has
     total energy as our plane reads it (ADM, from the spatial metric at infinity) E_total = (m/4 + r0/2) c^4 / G
     (sympy, derived here).  At m = -2 r0 -- a wormhole by BK's own condition, m < 0 -- E_total = 0 exactly, whatever
     r0.  With r0 set by the README (r0 = r_min(N), chain.py) the plane's total is zero for every N.
  P2 THE NECK STILL HOLDS THE README, AND THE PLANE READS NEGATIVE ENERGY AROUND IT -- YOUR ITEM 86.1.  The Misner-Sharp
     energy at the throat is r0 c^4 / (2G) for every m (sympy): the neck carries chain.py's floor, 4.59404002e8 J x
     sqrt(N), unchanged.  The surroundings carry the opposite: the pull our plane reads (Komar, from g_tt) is
     m c^4 / G = -2 r0 c^4 / G = -1.83761601e9 J x sqrt(N), a negative reading.  The corridor contains positive energy
     at its neck, totals zero, and appears to contain negative energy: "must appear to contain" (item 86 answer 1).
  P3 IT NEEDS NO MATTER ON EITHER PLANE.  Eq. (17) has R = 0 for every m (escape.bk_throats, imported; section 8m):
     the plane's reading is carried by the bulk term E = -G, not by matter.
  P4 MAKING IS ENLARGING (YOUR ANSWER 1).  The zero-total family m = -2 r0 runs continuously in r0: a larger corridor
     is the same corridor with r0 raised, at zero total throughout.  As r0 -> 0 it tends to flat space, and a throat
     opening from r0 = 0 is a pinch, topology change (chain.py PINCH-IS-TOPO).  Under item 100 with ER=EPR every pair
     already has a bridge (ENTANGLE.md), so making starts from r0 > 0 and is enlargement throughout -- chain.py's route
     R1, consistent and safe.  Whether a Planckian, quantum bridge enlarges into this classical family is OPEN
     (Maldacena-Susskind p.17: pair bridges "probably" not classical geometry).
  P5 NO MORE AND NO LESS (YOUR ANSWER 6): THE DEVICE SIZES THE NECK TO THE FLOOR.  A neck of area
     7.24277891e-70 m^2 x N is the least that holds N bits (chain.py, ENTANGLE.md); "no more, no less" is that bound
     met with equality.  How the twelve trajectories set the size (H-TWELVE-TRAJECTORIES) is not modelled: OPEN.
  P6 DISTANCE IS IRRELEVANT (YOUR ANSWER 7) -- IN EVERY FORMULA HERE.  The floor, the neck, the plane's total and the
     Komar reading depend on N alone: no separation enters any of them (each is computed with no distance argument).
  P8 THE NEGATIVE PART IS THE NECK'S EXACT INVERSE (ITEM 102).  At m = -2 r0 the energy outside the neck (the ADM
     total minus the throat's Misner-Sharp energy) is -r0 c^4 / (2G) = -4.59404002e8 J x sqrt(N): the additive inverse
     of the neck's, and set by the same README size N.  Read with H-INFORMATION-IS-INVERSE-MASS (additive reading):
     the corridor that holds an N-bit README is a positive neck and its negative inverse, both defined by N.
  P7 THE MOUTHS MAY BE IN SEPARATE UNIVERSES (YOUR ANSWER 5).  Eq. (17) is symmetric and joins two asymptotic regions
     (escape.py S4): it does not make them one universe, which BULK5-O1 asked for and your answer drops.

WHAT IS RULED OUT, AS THE BOUNDARY
  * Inside BK's other range (r0 > 2m >= 0) the plane's total is at least r0 c^4 / (2G) -- the neck's floor; zero needs
    m < 0 (contrast).
  * If "total our plane can read" meant the pull (Komar) rather than the total energy (ADM), zero needs m = 0, BK's
    eq. (13), and the energy total is then the floor r0 c^4/(2G).  No member of the family reads zero in both (z3 over
    the two linear forms: m = 0 and m/4 + r0/2 = 0 force r0 = 0, no throat).

NAMED HYPOTHESES
  M's: H-PLANE-TOTAL-COST (11), H-MADE-AS-WIDENED (1), H-DEVICE-SIZES (6), H-TWELVE-TRAJECTORIES (6),
    H-DISTANCE-IRRELEVANT (7), H-SEPARATE-UNIVERSES (5), H-READING-ONLY (86.1), H-UNIVERSAL-ENTANGLEMENT (100).
  The board's: H-TOTAL-IS-ADM (the plane's "total" is the ADM energy; its alternative, the Komar pull, is the boundary);
    H-BK-CORRIDOR (the corridor is Bronnikov-Kim's eq. (17) throat, static, at its throat radius r0); H-NECK-HOLDS (the
    bits sit at the neck, bounded by the neck's energy -- chain.py); H-STRONG-BOUND (chain.py); H-RS1 (the brane
    reading behind E = -G, section 8m); BULK5-O1's global bulk, OPEN (BK p.6: "a complete model requires knowledge of
    the full 5-dimensional space-time").

USAGE
    python3 plane.py | --selftest | --json
"""

import contextlib
import importlib.util
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
_CACHE = {}

BK_READ = {
    "source": "Bronnikov & Kim, 'Possible wormholes in a brane world', gr-qc/0212112v1",
    "route": "arXiv PDF via Firecrawl (query, direct quote), 2026-10-06",
    "eq_17": "ds^2 = (1 - 2m/r) dt^2 - (1 - 3m/(2r)) dr^2 / ((1 - 2m/r)(1 - r0/r)) - r^2 dOmega^2",
    "range": "'This is evidently a symmetric wormhole geometry for any r0 > 2m >= 0, or for any r0 > 0 in case m < 0. "
             "The Schwarzschild metric is restored from (17) in the special case r0 = 3m/2.'",
    "page": "p.6 (eqs. 13 and 17 as escape.py cites them)",
}


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
    """Imported, never copied: chain.py (the floor and its constants), escape.py (Bronnikov-Kim's R = 0)."""
    if not _CACHE:
        _CACHE["chain"] = _load(os.path.join(HERE, "chain.py"), "copy_chain_plane")
        _CACHE["escape"] = _load(os.path.join(D68, "bulk", "escape.py"), "d68_escape_plane")
    return _CACHE


def bk_masses():
    """Eq. (17) in geometric units: the ADM mass (coefficient of 1/r in g_rr = 1 + 2 M_ADM / r + ...), the Komar mass
    (coefficient in -g_tt = 1 - 2 M_K / r), and the Misner-Sharp mass at the throat, (r/2)(1 - g^rr) at r = r0."""
    import sympy as sp
    r, r0 = sp.symbols("r r0", positive=True)
    m = sp.symbols("m", real=True)
    u = sp.symbols("u", positive=True)                       # u = 1/r
    grr = (1 - sp.Rational(3, 2) * m / r) / ((1 - 2 * m / r) * (1 - r0 / r))
    gtt = 1 - 2 * m / r
    grr_u = sp.series(grr.subs(r, 1 / u), u, 0, 2).removeO()
    M_adm = sp.simplify(sp.expand(grr_u).coeff(u, 1) / 2)
    M_k = sp.simplify(-sp.expand(gtt.subs(r, 1 / u)).coeff(u, 1) / 2)
    ms = sp.simplify((r / 2) * (1 - 1 / grr))
    ms_throat = sp.simplify(sp.limit(ms, r, r0))
    zero = sp.solve(sp.Eq(M_adm, 0), m)
    return {"M_adm": M_adm, "M_komar": M_k, "MS_throat": ms_throat, "m_zero_adm": zero,
            "syms": (r, r0, m), "grr": grr, "gtt": gtt}


def wormhole_ok(m_over_r0, n=2000):
    """Numerically on r in (r0, 50 r0]: g_tt > 0 (no horizon) and g_rr > 0, with g_rr -> infinity at r0 (the throat)."""
    r0 = 1.0
    m = m_over_r0 * r0
    ok = True
    for i in range(1, n + 1):
        r = r0 * (1 + 49.0 * i / n)
        gtt = 1 - 2 * m / r
        grr = (1 - 1.5 * m / r) / ((1 - 2 * m / r) * (1 - r0 / r))
        ok &= gtt > 0 and grr > 0
    r = r0 * (1 + 1e-9)
    near = (1 - 1.5 * m / r) / ((1 - 2 * m / r) * (1 - r0 / r))
    return ok and near > 1e8


def z3_both_zero():
    """Can one member read zero in both the ADM total and the Komar pull?  M_K = m = 0 and m/4 + r0/2 = 0, r0 > 0."""
    import z3
    m, r0 = z3.Reals("m r0")
    s = z3.Solver()
    s.add(r0 > 0, m == 0, m / 4 + r0 / 2 == 0)
    both = s.check() == z3.sat
    s2 = z3.Solver()
    s2.add(r0 > 0, m / 4 + r0 / 2 == 0, m < 0)
    adm_zero_m_negative = s2.check() == z3.sat
    s3 = z3.Solver()
    s3.add(r0 > 2 * m, m >= 0, m / 4 + r0 / 2 <= r0 / 2 - 1e-30 * r0)
    below_floor_nonneg = s3.check() == z3.sat
    return {"both_zero_sat": both, "adm_zero_with_m_negative_sat": adm_zero_m_negative,
            "adm_below_floor_with_m_nonneg_sat": below_floor_nonneg}


def compute():
    import sympy as sp
    o = owners()
    ch, esc = o["chain"], o["escape"]
    bk = bk_masses()
    r, r0, m = bk["syms"]
    co = ch.coefficients()
    seat = ch.owners()["uses"].owners()[0]
    fa = ch.owners()["uses"].owners()[1]
    core = fa.identity_core()["total_bits"]
    fl = ch.corridor_floor(core)
    c4G = seat.C ** 4 / seat.G
    r0c = fl["r_m"]
    m_zero = float(bk["m_zero_adm"][0].subs(r0, r0c))
    with contextlib.redirect_stdout(io.StringIO()):
        throats = esc.bk_throats()
    # M-COEFF: the Komar reading per sqrt(bit) at m = -2 r0, exact: -2 r_min c^4/G = -4 x E_min
    komar_per_sqrt_bit = -4 * co["E_min_J_per_sqrt_bit"]["value"]
    return {
        "bk_read": BK_READ, "M_adm": str(bk["M_adm"]), "M_komar": str(bk["M_komar"]),
        "MS_throat": str(bk["MS_throat"]), "m_zero_adm": [str(z) for z in bk["m_zero_adm"]],
        "M_adm_at_m0": str(sp.simplify(bk["M_adm"].subs(m, 0))),
        "core_bits": core, "r0_core_m": r0c, "m_zero_core_m": m_zero,
        "E_neck_core_J": float(bk["MS_throat"].subs(r0, r0c)) * c4G,
        "E_total_core_J": float(bk["M_adm"].subs({m: m_zero, r0: r0c})) * c4G,
        "E_komar_core_J": float(bk["M_komar"].subs({m: m_zero, r0: r0c})) * c4G,
        "outside_neck_geom": str(sp.simplify((bk["M_adm"] - bk["MS_throat"]).subs(m, bk["m_zero_adm"][0]))),
        "E_outside_core_J": float((bk["M_adm"] - bk["MS_throat"]).subs({m: m_zero, r0: r0c})) * c4G,
        "floor_core_J": fl["E_J"], "komar_per_sqrt_bit_J": komar_per_sqrt_bit,
        "komar_exact": "-2 r_min c^4 / G = -sqrt(2 N h c^5 ln2 / (pi^2 G)) = -4 x sqrt(N h c^5 ln2 / (8 pi^2 G))",
        "E_min_per_sqrt_bit_J": co["E_min_J_per_sqrt_bit"]["value"], "u_r_G": co["E_min_J_per_sqrt_bit"]["u_r"],
        "bk_R": [str(t[0]) for t in throats],
        "wormhole_m_minus_2r0": wormhole_ok(-2.0), "wormhole_m_0": wormhole_ok(0.0),
        "wormhole_control_m_0p6r0": wormhole_ok(0.6),
        "z3": z3_both_zero(),
        "floor_takes_distance": "distance" in ch.corridor_floor.__code__.co_varnames
                                or "L" in ch.corridor_floor.__code__.co_varnames,
    }


def report(d):
    print("plane.py -- M-RULINGS item 101: the corridor's cost as 'total our plane can read'")
    print("Bronnikov-Kim eq. (17), READ: %s" % d["bk_read"]["range"])
    print("  ADM (the plane's total) M = %s;  Komar (the pull) M = %s;  Misner-Sharp at the throat = %s (geometric)" % (
        d["M_adm"], d["M_komar"], d["MS_throat"]))
    print("  the total is zero at m = %s; at m = 0 it is %s" % (d["m_zero_adm"], d["M_adm_at_m0"]))
    print("  core README (%.6e bits), r0 = %.9e m, m = %.9e m:" % (d["core_bits"], d["r0_core_m"], d["m_zero_core_m"]))
    print("    neck %.9e J (chain's floor %.9e J); plane's total %.3e J; Komar reading %.9e J" % (
        d["E_neck_core_J"], d["floor_core_J"], d["E_total_core_J"], d["E_komar_core_J"]))
    print("  M-COEFF: Komar reading = %s = %.9e J x sqrt(N) (u_r %.1e)" % (d["komar_exact"],
                                                                         d["komar_per_sqrt_bit_J"], d["u_r_G"]))
    print("  R for eqs. (13), (17) (escape.bk_throats, imported): %s" % d["bk_R"])
    print("  z3: %s" % d["z3"])


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

    import sympy as sp
    r0s = sp.Symbol("r0", positive=True)
    ms = sp.Symbol("m", real=True)
    chk("P1: eq. (17)'s ADM total is m/4 + r0/2 (sympy: %s) and vanishes at m = -2 r0 (%s)" % (
        d["M_adm"], d["m_zero_adm"]),
        sp.simplify(sp.sympify(d["M_adm"], locals={"m": ms, "r0": r0s}) - (ms / 4 + r0s / 2)) == 0 and
        d["m_zero_adm"] == ["-2*r0"])
    chk("P1: at m = -2 r0 the geometry is a wormhole on r in (r0, 50 r0] (no horizon, g_rr > 0, throat at r0) -- BK's "
        "'any r0 > 0 in case m < 0'", d["wormhole_m_minus_2r0"])
    chk("a horizon inside the range (m = 0.6 r0 > r0/2: g_tt changes sign at r = 1.2 r0) fails the same test",
        not d["wormhole_control_m_0p6r0"], ctl=True)
    chk("P1: for the core README the plane's total is zero (%.3e J against a neck of %.6e J)" % (
        d["E_total_core_J"], d["E_neck_core_J"]), abs(d["E_total_core_J"]) < 1e-6 * d["E_neck_core_J"])
    chk("P2: the Misner-Sharp energy at the throat is r0/2 for every m (sympy: %s), so the neck carries chain.py's "
        "floor (%.9e J vs %.9e J)" % (d["MS_throat"], d["E_neck_core_J"], d["floor_core_J"]),
        d["MS_throat"] == "r0/2" and abs(d["E_neck_core_J"] / d["floor_core_J"] - 1) < 1e-9)
    chk("P2: the Komar reading at m = -2 r0 is negative and equals -4 x the floor (%.9e J vs %.9e J)" % (
        d["E_komar_core_J"], -4 * d["floor_core_J"]),
        d["E_komar_core_J"] < 0 and abs(d["E_komar_core_J"] / (-4 * d["floor_core_J"]) - 1) < 1e-9)
    chk("P8 (item 102): at m = -2 r0 the energy outside the neck (ADM total minus the throat's Misner-Sharp) is %s, "
        "the exact negative of the neck's: %.9e J against %.9e J" % (d["outside_neck_geom"], d["E_outside_core_J"],
                                                                      d["E_neck_core_J"]),
        d["outside_neck_geom"] == "-r0/2" and abs(d["E_outside_core_J"] / d["E_neck_core_J"] + 1) < 1e-9)
    chk("M-COEFF: the Komar coefficient %.9e J per sqrt(bit) reproduces the core's reading" % d["komar_per_sqrt_bit_J"],
        abs(d["komar_per_sqrt_bit_J"] * math.sqrt(d["core_bits"]) / d["E_komar_core_J"] - 1) < 1e-9)
    chk("P3: eqs. (13) and (17) have R = 0 (escape.bk_throats, imported: %s)" % d["bk_R"], d["bk_R"] == ["0", "0"])
    chk("boundary: inside BK's range r0 > 2m >= 0 no member reads a total below the neck's floor r0/2 (z3 unsat)",
        not d["z3"]["adm_below_floor_with_m_nonneg_sat"], contrast=True)
    chk("boundary: no member reads zero in both the ADM total and the Komar pull (z3 unsat); with m < 0 the ADM total "
        "alone can be zero (z3 sat)", (not d["z3"]["both_zero_sat"]) and d["z3"]["adm_zero_with_m_negative_sat"])
    structural.append("P6: chain.corridor_floor takes no distance argument (%s) and none of eq. (17)'s masses has one "
                      "-- distance enters no formula here, by construction" % (not d["floor_takes_distance"]))
    structural.append("H-TOTAL-IS-ADM: 'total our plane can read' read as the ADM energy; the Komar pull is the boundary")
    structural.append("P4: the zero-total family m = -2 r0 is continuous in r0 and tends to flat space at r0 = 0 (read off "
                      "eq. 17); opening from r0 = 0 is a pinch (chain.py PINCH-IS-TOPO)")
    structural.append("BK's global bulk is OPEN (BULK5-O1; BK p.6); M's answer 5 drops only its one-universe clause")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("plane.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
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
