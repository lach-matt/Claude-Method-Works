#!/usr/bin/env python3
"""opening.py -- DOCKET 68, M-RULINGS item 113 (second of three): how the corridor opens and closes -- the two holds of
item 106 that no static Bronnikov-Kim member has.  Deduced, computed and READ; not verified; not seated.
Write-up: OPENING.md.

M's words (verbatim in the rulings file): item 106 "Three distinct holds in one fluid wave motion, horizon position 1
only as the corridor opens, ... upon the corridor closing the bits are then held only at the horizon of position 2";
item 109 "A horizon cannot exist without the object of which it needs to exist"; item 110 "Into position 2"; item 111
"one energy read from two sides"; item 86 answer 5 "I suspect it is incredibly short, maybe even immeasurable but not
zero".

THE BOARD'S READING (R-VAIDYA-HOLDS, ungraded).  The opening is energy falling in at position 1 and the closing energy
flowing out at position 2, each as null dust -- radiation moving at light speed, a "fluid wave": ingoing Vaidya at
position 1, ds^2 = -(1 - 2m(v)/r) dv^2 + 2 dv dr + r^2 dOmega^2, with m(v) rising from 0 to m_f; outgoing Vaidya at
position 2, ds^2 = -(1 - 2m(u)/r) du^2 - 2 du dr + r^2 dOmega^2, with m(u) falling from m_f to 0.  The metric is
written here and its curvature computed; nothing about it is READ.

WHAT FOLLOWS THE WORK (item 82)
  O1 BOTH HOLDS NEED ONLY POSITIVE ENERGY.  Ingoing: G_vv = 2 m'(v) / r^2, every other component zero (sympy), so the
     null energy condition holds exactly when m rises -- the opening.  Outgoing: G_uu = -2 m'(u) / r^2, so it holds
     exactly when m falls -- the closing.  Controls: the reverse (an opening that sheds mass, a closing that gains it)
     violates it.  Unlike the corridor's static neck, neither transition needs negative energy, so the board's duration
     inequality for negative energy (D7) does not bind them.
  O2 BOTH KEEP R = 0, LIKE THE CORRIDOR.  Null dust is traceless: R = 0 for both (sympy), the same condition as
     Bronnikov-Kim's eq. (17) (escape.py; section 8m).  The whole sequence -- opening, corridor, closing -- stays in the
     R = 0 class.
  O3 THE ENERGY IN IS THE ENERGY OUT.  The opening carries m_f c^4/G in at position 1 and the closing carries the same
     out into position 2 (the integral of m' over each hold, by construction); with m_f = r_min/2 that is the floor,
     4.59404002e8 J x sqrt(N) -- your item 110, energy into position 2, and item 111, one energy.  Position 2's horizon
     ends when its m reaches 0 (the apparent horizon r = 2m(u) shrinks to nothing) -- your item 109.
  O4 THE SHORTEST OPENING: IMMEASURABLY SHORT, NOT ZERO.  If no flow exceeds Gibbons' maximum tension times c
     (H-MAX-POWER: Gibbons hep-th/0210109 p.2 eq. 1, "The tension or force between two bodies cannot exceed
     F_g = c^4/4G", READ, a proposed principle; extending it to power, c^5/4G, is the board's step), then dm/dt <= c/4 and
     a hold delivering m_f lasts at least 4 m_f / c = 2 r_min / c = sqrt(2 N h G ln2 / (pi^2 c^5)) = 5.0647e-44 s x
     sqrt(N): 2.652e-36 s for the core README -- your item 86 answer 5, computed.  The bound is met by a constant flow;
     a smooth (1 - cos) profile needs pi r_min / c.

WHAT IS RULED OUT, AS THE BOUNDARY
  * An opening that removes mass, or a closing that adds it, with positive energy (O1's controls).
  * A hold shorter than 2 r_min / c, under H-MAX-POWER.
  * Classical white holes are unstable to infalling matter (Eardley 1974, NOT READ): position 2's outgoing hold is a
    white-hole horizon (plane.py P1) and its stability is OPEN.
  * How the ingoing hold at position 1 joins the corridor's interior and the outgoing hold at position 2 -- the junction
    through the throat, and how position 2's mass rises during the opening -- is not computed: OPEN.

NAMED HYPOTHESES
  M's: H-THREE-HOLDS (106), H-HORIZON-NEEDS-OBJECT (109), H-ENERGY-INTO-P2 (110), H-ONE-ENERGY-TWO-SIDES (111),
    H-BRIEF-HOLD (86.5).
  The board's: R-VAIDYA-HOLDS; H-MAX-POWER; H-HORIZON-HOLDS, H-STRONG-BOUND (m_f = r_min/2, chain.py); H-JUNCTION (the
    gluing, OPEN).

USAGE
    python3 opening.py | --selftest | --json
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

GIBBONS_READ = {
    "source": "Gibbons, 'The Maximum Tension Principle in General Relativity', hep-th/0210109v1",
    "route": "alphaXiv (answer_pdf_queries), 2026-10-06",
    "p1": "'I suggest that classical General Relativity in four spacetime dimensions incorporates a Principal of Maximal "
          "Tension and give arguments to show that the value of the maximal tension is c^4/4G'",
    "p2_eq1": "'The Principle of Maximum Tension: The tension or force between two bodies cannot exceed F_g = c^4/4G' "
              "(numerically 3.25e43 N)",
    "scope": "a proposed principle, argued from examples; the paper states force, not power",
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
    if not _CACHE:
        _CACHE["chain"] = _load(os.path.join(HERE, "chain.py"), "copy_chain_open")
    return _CACHE


def vaidya(sign):
    """sign = +1 ingoing (v advanced), -1 outgoing (v read as u, retarded).  Returns (R, G_00, other nonzero components)."""
    import sympy as sp
    v, r, th, ph = sp.symbols("v r theta phi", positive=True)
    m = sp.Function("m")
    g = sp.Matrix([[-(1 - 2 * m(v) / r), sign, 0, 0], [sign, 0, 0, 0], [0, 0, r ** 2, 0],
                   [0, 0, 0, r ** 2 * sp.sin(th) ** 2]])
    X = [v, r, th, ph]
    n = 4
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(n, n, lambda b, c: sp.simplify(sum(
        sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n)) for a in range(n))))
    R = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    G = sp.simplify(Ric - R * g / 2)
    others = [(i, j) for i in range(n) for j in range(n) if (i, j) != (0, 0) and sp.simplify(G[i, j]) != 0]
    mp = sp.Symbol("mprime")
    G00 = sp.simplify(G[0, 0].subs(sp.Derivative(m(v), v), mp))
    return {"R": str(R), "G00": str(G00), "others": others, "G00_expr": G00, "mp": mp, "r": r}


def nec_holds(vd, mprime_value):
    """For a radial null vector k with k^v != 0 the only term is T_vv (k^v)^2 = G_vv (k^v)^2 / 8 pi: the sign of G_vv."""
    import sympy as sp
    val = vd["G00_expr"].subs({vd["mp"]: mprime_value, vd["r"]: 1})
    return bool(val >= 0)


def compute():
    o = owners()
    ch = o["chain"]
    co = ch.coefficients()
    seat, fa = ch.owners()["uses"].owners()[0], ch.owners()["uses"].owners()[1]
    core = fa.identity_core()["total_bits"]
    fl = ch.corridor_floor(core)
    c = seat.C
    rmin = fl["r_m"]
    ing, out = vaidya(+1), vaidya(-1)
    tau_coeff = 2 * co["r_min_m_per_sqrt_bit"]["value"] / c
    return {
        "gibbons_read": GIBBONS_READ,
        "ingoing": {k: ing[k] for k in ("R", "G00", "others")}, "outgoing": {k: out[k] for k in ("R", "G00", "others")},
        "nec_open_rising": nec_holds(ing, +1), "nec_open_falling": nec_holds(ing, -1),
        "nec_close_falling": nec_holds(out, -1), "nec_close_rising": nec_holds(out, +1),
        "core_bits": core, "r_min_core_m": rmin, "E_hold_core_J": fl["E_J"],
        "tau_min_core_s": 2 * rmin / c, "tau_min_per_sqrt_bit_s": tau_coeff,
        "tau_cos_core_s": math.pi * rmin / c,
        "tau_exact_form": "2 r_min / c = sqrt(2 N h G ln2 / (pi^2 c^5))",
    }


def report(d):
    print("opening.py -- item 113 (2 of 3): the opening and closing holds as null dust (R-VAIDYA-HOLDS)")
    print("  ingoing (position 1): R = %s, G_vv = %s, other components %s" % (d["ingoing"]["R"], d["ingoing"]["G00"],
                                                                         d["ingoing"]["others"]))
    print("  outgoing (position 2): R = %s, G_uu = %s, other components %s" % (
        d["outgoing"]["R"], d["outgoing"]["G00"], d["outgoing"]["others"]))
    print("  energy in = energy out = %.9e J (core, the floor)" % d["E_hold_core_J"])
    print("  shortest hold under H-MAX-POWER: %s = %.6e s x sqrt(N); core %.6e s (smooth profile %.6e s)" % (
        d["tau_exact_form"], d["tau_min_per_sqrt_bit_s"], d["tau_min_core_s"], d["tau_cos_core_s"]))


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

    chk("O1: ingoing null dust has G_vv = %s and no other component (sympy): pure inflow" % d["ingoing"]["G00"],
        d["ingoing"]["G00"] == "2*mprime/r**2" and d["ingoing"]["others"] == [])
    chk("O1: outgoing null dust has G_uu = %s and no other component (sympy): pure outflow" % d["outgoing"]["G00"],
        d["outgoing"]["G00"] == "-2*mprime/r**2" and d["outgoing"]["others"] == [])
    chk("O1: the opening (mass rising at position 1) keeps the null energy condition", d["nec_open_rising"])
    chk("an opening that sheds mass violates it", not d["nec_open_falling"], ctl=True)
    chk("O1: the closing (mass falling at position 2) keeps the null energy condition", d["nec_close_falling"])
    chk("a closing that gains mass violates it", not d["nec_close_rising"], ctl=True)
    chk("O2: both holds have R = 0 (sympy: %s, %s), the corridor's own class" % (d["ingoing"]["R"],
                                                                                  d["outgoing"]["R"]),
        d["ingoing"]["R"] == "0" and d["outgoing"]["R"] == "0")
    structural.append("O4: the shortest hold under H-MAX-POWER, 2 r_min / c = %.6e s for the core; the smooth profile's "
                      "pi r_min / c = %.6e s (pi > 2: not counted)" % (d["tau_min_core_s"], d["tau_cos_core_s"]))
    structural.append("O3: energy in = energy out = m_f c^4/G = %.9e J for the core -- the integral of m' over each hold, "
                      "by construction" % d["E_hold_core_J"])
    structural.append("O4: the coefficient %.9e s per sqrt(bit) is 2 x chain.py's r_min coefficient / c (closed form %s)"
                      % (d["tau_min_per_sqrt_bit_s"], d["tau_exact_form"]))
    structural.append("H-MAX-POWER: Gibbons states a maximum force (p.2 eq. 1, a proposed principle); power c^5/4G is the "
                      "board's step")
    structural.append("H-JUNCTION: the joins through the throat, and position 2's rise during the opening, are OPEN")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("opening.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
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
