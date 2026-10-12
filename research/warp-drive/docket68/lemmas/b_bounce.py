#!/usr/bin/env python3
"""b_bounce.py -- item 273: owed item (b) answered in kind -- the corridor's one object is a quantum bounce to position 2
(H-BOUNCE-TO-P2).  Its construction, where and when its quantum region appears (an estimate, labelled), the negative
null energy any bounce must carry, and 183's pairing.  Worked in the conversation (computed with sympy, exact where
marked; READ where marked; estimates marked; deduced where marked; not verified by a separate session; not seated);
2026-10-12.

  Q0 (read) M's item-273 words, verbatim in the rulings file.
  Q1 (computed, exact) The one object, two views.  The Kruskal form -F(UV) dU dV + r(UV)^2 dOmega^2 is invariant under
     (U, V) -> (-U, -V), which carries our exterior (U < 0 < V) onto position 2's (V < 0 < U), the future interior onto
     the past interior, and T = (U + V)/2 onto -T.  Haggard and Rovelli (arXiv:1407.0989, READ in b_interior B4) glue a
     collapsing half to its time reflection; with this map in place of the time reflection the expanding half -- the
     white hole -- lies in position 2's exterior: the black hole seen from our side and the white hole seen from position
     2's are images of one another under an isometry of the solution, "different views of the same object" (132).  The
     surface the map fixes, T = 0, is the bridge's slice through the throat, where the README crosses (251).
  Q2 (computed, exact; Haggard-Rovelli's rule carried to 5D) Where quantum effects first reach outside the horizon.
     Their classicality parameter grows as the curvature times a power b of the bounce time, the time dominated by the
     logarithm near the horizon; maximising over radius gives R_q = r_h sqrt(1 + b/4) in five dimensions -- 1.118 r_h at
     b = 1, on our plane too (its equator).  Control: the same rule in 4D gives 2m (1 + b/6), their eq. (16), READ.
  Q3 (estimate) When.  Haggard and Rovelli's 4D time is of order m^2/l_P (their eq. (2), READ), a number of clocks of
     order m/l_P.  Carried to 5D it is of order (r_h/l5)^p clocks, p = 1 if the leading quantum correction is l5^2 R^2
     (their form), 3/2 if it is l5^3 R^(5/2) -- 7.3e4 to 2.0e7 clocks at the example README, times an order-one
     coefficient this rule does not fix.  Two exact comparisons: the write's floor is 0.921 (r_h/l5) clocks exactly
     (write_small S3 against C2's r_h/l5) -- the same N^(1/3) as the p = 1 bounce, a coincidence of scaling named here and
     not explained -- and the hole's life, 8.57e14 clocks (hold_small L5), is far beyond either.
  Q4 (computed, exact) Every bounce carries net negative null energy.  For a shear- and twist-free null congruence in D
     dimensions dtheta/dlambda = -theta^2/(D - 2) - R_kk, so turning it from converging (theta_in < 0) to diverging
     (theta_out > 0) needs integral R_kk dlambda = theta_in - theta_out - integral theta^2/(D - 2) dlambda < 0 -- on every
     ray through the quantum region (shear only adds to it).  For the radial congruence turned within radius e in 5D,
     theta = -/+3/e at the region's edges: at least 6/e, and with the focusing term about 9/e.
  Q5 (computed, exact in its flat model; deduced) 183's pairing.  A README that falls as radial null flux cannot pair
     it: it is parallel to those rays (T_kk = 0, b_interior B5).  A README held as one whole (163) is a body, and in
     Haggard and Rovelli's construction the collapsing matter is what reaches the quantum region and bounces -- here the
     README (115 (c)).  Every ray through a region of radius e then crosses it: a body of energy E within radius e gives
     the ray 8 pi G5 integral T_kk dlambda = 32 G5 E/(pi e^3) = 12 r_h^2/e^3 (E = 3 pi r_h^2/(8 G5)), against the bounce's
     9/e -- the README outweighs it whenever e <= 1.155 r_h, by (4/3)(r_h/e)^2.  At the five-dimensional Planck density
     (G5 rho = 1/l5^2, the radius e = (3/(4 pi))^(1/4) (r_h l5)^(1/2); an estimate of where the bounce sits) the margin is
     2.0e5 at the example README.  So under 183 the README itself is the bounce's pair, per ray, where it passes.
  Q6 (named, not computed) What Q5 leaves.  Haggard and Rovelli's quantum region also leaks outside the horizon, to R_q
     (Q2), over the long time of Q3 -- the part that undoes the trapping.  Rays through that part, near the horizon, do
     not cross the README deep inside; whether their null energy is negative there, and what pairs it, is not computed:
     their region III is an ansatz, not a solution.

What this does not show.
  - The two-exterior bounce as a metric (Q1 gives the map, not the glued solution); Q3's coefficient; Q6.
  - Q5 puts the README as the matter that collapses and bounces -- the README forming the corridor (115 (c); 198, M's
    guess), C6's reading (ii).  C6's S4 and C5's L4 compared the hold with the life on reading (i) (the hole standing
    at its size through the write, 162-163; items 264, 267): on the bounce the hold runs from formation to the bounce,
    and that comparison is to be re-read with owed item (d).
  - The junction (owed item (c)) on the bounce: position 2's white-hole face exists from the bounce's emergence; its
    start and end follow from Q1-Q3 and are item (c)'s.

Imports nothing beyond sympy; reads the rulings file and imports write_small.py by path.  python3 b_bounce.py
[--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M273 = "Quantum bounce to pos 2 (Recommended)"
N_EX = 2742570311524972
Z_PLANE = sp.Rational(10675, 100)

U, V, r, rh, b, e, lam = sp.symbols("U V r r_h b e lambda", positive=True)


def isometry():
    Us, Vs = sp.symbols("U V", real=True)
    T = (Us + Vs) / 2
    img = {Us: -Us, Vs: -Vs}
    keeps_UV = sp.simplify((Us * Vs).subs(img, simultaneous=True) - Us * Vs) == 0
    flips_T = sp.simplify(T.subs(img, simultaneous=True) + T) == 0
    # region map by sign pattern (U, V): I (-, +) -> (+, -) II; F (+, +) -> (-, -) P
    regions = {"I": (-1, 1), "F": (1, 1), "II": (1, -1), "P": (-1, -1)}
    images = {k: next(n for n, s in regions.items() if s == (-v[0], -v[1])) for k, v in regions.items()}
    return dict(keeps_UV=keeps_UV, flips_T=flips_T, images=images)


def where(D):
    """Haggard-Rovelli's rule: maximise curvature x (f)^(b/2) over radius; curvature ~ r^-(D-1), f = 1 - (r_h/r)^(D-3)"""
    R = sp.Symbol("R", positive=True)
    f = 1 - (rh / R) ** (D - 3)
    expo = D - 1 if not MUT.get("wrong_curvature") else D
    g = R ** (-expo) * f ** (b / 2)
    sol = [s for s in sp.solve(sp.Eq(sp.diff(sp.log(g), R), 0), R) if s.is_positive]
    return sp.simplify(sol[0])


def when():
    PG_spec = importlib.util.spec_from_file_location("bb_ws", os.path.join(HERE, "write_small.py"))
    WS = importlib.util.module_from_spec(PG_spec)
    with contextlib.redirect_stdout(io.StringIO()):
        PG_spec.loader.exec_module(WS)
    N, Z = sp.symbols("N Z", positive=True)
    rh_over_l5 = (2 * N * sp.log(2) / sp.pi ** 2) ** sp.Rational(1, 3)
    floor_x = sp.Rational(3, 2) * (5 * N * sp.log(2) / Z) ** sp.Rational(1, 3)        # write_small S3, 1 + T
    ratio = sp.simplify(floor_x / rh_over_l5)
    rl = float(rh_over_l5.subs(N, N_EX))
    return dict(ratio=ratio, ratio_num=float(ratio.subs(Z, Z_PLANE)), p1=rl, p32=rl ** 1.5, head=WS.head_clocks())


def raychaudhuri(D=5):
    th = sp.Function("theta")(lam)
    Rkk = sp.Function("R_kk")(lam)
    eq = sp.Eq(sp.diff(th, lam), -th ** 2 / (D - 2) - Rkk)
    # integrate over [0, L]: theta(L) - theta(0) = -int theta^2/(D-2) - int R_kk
    th_in, th_out, I2, IR = sp.symbols("theta_in theta_out I_2 I_R", real=True)
    IR_sol = sp.solve(sp.Eq(th_out - th_in, -I2 / (D - 2) - IR), IR)[0]
    radial = sp.Rational(D - 2, 1) / e                    # |theta| = (D - 2)/r for the radial congruence at radius e
    least = 2 * radial                                    # theta from -3/e to +3/e
    return dict(eq=eq, IR=IR_sol, least=sp.simplify(least), with_focus=sp.Rational(9, 1) / e)


def pairing():
    G5 = sp.Symbol("G5", positive=True)
    E = 3 * sp.pi * rh ** 2 / (8 * G5)
    rho = E / (sp.pi ** 2 * e ** 4 / 2)                    # a body of energy E in the 4-ball of radius e
    chord = 2 * e if not MUT.get("half_chord") else e
    readme = sp.simplify(8 * sp.pi * G5 * rho * chord)     # T_kk = rho for k.u = -1, along the diameter
    need = sp.Rational(9, 1) / e
    crit = sp.solve(sp.Eq(readme, need), e)
    crit = [c for c in crit if c.is_positive][0]
    margin = sp.simplify(readme / need)
    # the Planck-density radius: G5 rho = 1/l5^2 -> e^4 = 2 G5 E l5^2/pi^2
    l5 = sp.Symbol("l5", positive=True)
    e_P = sp.simplify((2 * G5 * E * l5 ** 2 / sp.pi ** 2) ** sp.Rational(1, 4))
    rl = (2 * N_EX * math.log(2) / math.pi ** 2) ** (1 / 3)
    margin_P = float(margin.subs(e, e_P).subs({rh: rl, l5: 1, G5: 1}))
    return dict(readme=readme, crit=sp.simplify(crit), margin=margin, e_P=e_P, margin_P=margin_P)


def compute():
    return dict(iso=isometry(), R5=where(5), R4=where(4), when=when(), ray=raychaudhuri(), pair=pairing())


def report(o):
    i = o["iso"]
    print("b_bounce.py -- the quantum bounce to position 2 (item 273)\n")
    print("Q1 (U,V)->(-U,-V) keeps UV %s, flips T %s; regions %s" % (i["keeps_UV"], i["flips_T"], i["images"]))
    print("Q2 quantum effects first outside the horizon at R_q = %s (5D; b = 1: %.4f r_h); 4D control %s" % (
        o["R5"], float(o["R5"].subs({b: 1, rh: 1})), o["R4"]))
    w = o["when"]
    print("Q3 the write's floor / (r_h/l5) = %s = %.4f; bounce (r_h/l5)^p clocks: p = 1 %.3g, p = 3/2 %.3g (x O(1)); the "
          "write's floor %.0f" % (w["ratio"], w["ratio_num"], w["p1"], w["p32"], w["head"]))
    y = o["ray"]
    print("Q4 %s ; int R_kk = %s ; radial congruence turned at e: at least %s, with focusing ~ %s" % (
        y["eq"], y["IR"], y["least"], y["with_focus"]))
    p = o["pair"]
    print("Q5 the README held as one whole gives 8 pi G5 int T_kk = %s; outweighs 9/e for e <= %s; margin %s; at the "
          "Planck-density radius e = %s: %.3g" % (p["readme"], p["crit"], p["margin"], p["e_P"], p["margin_P"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("Q0 M's item-273 words verbatim in the rulings file", M273 in rul)
    i = o["iso"]
    add("Q1 (U,V) -> (-U,-V) is an isometry taking our exterior to position 2's, the future interior to the past, T to -T",
        i["keeps_UV"] and i["flips_T"] and i["images"] == {"I": "II", "F": "P", "II": "I", "P": "F"})
    m = sp.Symbol("m", positive=True)
    ok = sp.simplify(o["R5"] - rh * sp.sqrt(1 + b / 4)) == 0
    ok &= sp.simplify(o["R4"].subs(rh, 2 * m) - 2 * m * (1 + b / 6)) == 0
    add("Q2 R_q = r_h sqrt(1 + b/4) in 5D; the 4D control reproduces Haggard-Rovelli's 2m(1 + b/6)", ok)
    w = o["when"]
    Z = sp.Symbol("Z", positive=True)
    ok = sp.simplify(w["ratio"] - sp.Rational(3, 2) * (5 * sp.pi ** 2 / (2 * Z)) ** sp.Rational(1, 3)) == 0
    ok &= "%.3f" % w["ratio_num"] == "0.921" and "%.2g" % w["p1"] == "7.3e+04" and "%.2g" % w["p32"] == "2e+07"
    add("Q3 the write's floor is 0.921 (r_h/l5) exactly; the bounce estimate spans 7.3e4 to 2.0e7 clocks (x O(1))", ok)
    y = o["ray"]
    ti, to, I2 = sp.symbols("theta_in theta_out I_2", real=True)
    ok = sp.simplify(y["IR"] - (ti - to - I2 / 3)) == 0 and sp.simplify(y["least"] - 6 / e) == 0
    add("Q4 int R_kk = theta_in - theta_out - int theta^2/3 < 0 for a turning congruence; at least 6/e radially", ok)
    p = o["pair"]
    ok = sp.simplify(p["readme"] - 12 * rh ** 2 / e ** 3) == 0 and sp.simplify(p["crit"] - 2 * rh / sp.sqrt(3)) == 0
    ok &= sp.simplify(p["margin"] - sp.Rational(4, 3) * rh ** 2 / e ** 2) == 0 and "%.2g" % p["margin_P"] == "2e+05"
    add("Q5 the README held as one whole gives 12 r_h^2/e^3 on every ray through the region, outweighing the bounce's 9/e "
        "for e <= 1.155 r_h, by 2.0e5 at the Planck-density radius", ok)
    return res


MUTANTS = {"wrong_curvature": "the curvature taken one power too steep (r^-D)",
           "half_chord": "the README crossed over half its diameter"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-15s %-50s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
