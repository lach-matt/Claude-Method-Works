#!/usr/bin/env python3
"""interior_large.py -- item 391: the large end's interior (rows O1b, O1c), first what M's rulings require of it and
what the record's own methods already give.  The small end's is o1c_oneway.py (O1cs, verified 337).  No test run
(M-NO-TESTS-UNTIL-NEEDED); worked in the conversation (computed with sympy, exact where marked; deduced where marked;
not verified by a separate session; not seated); 2026-10-14.

  I0 (read) The words the rows rest on, verbatim in the rulings file: 132, "different views of the same object"; 270,
     "You are forgetting that the passage is one-way only"; 273's option text M chose, "One-way, complete, README only,
     no Cauchy horizon" (option text, not M's own words: 337); 109, "A horizon cannot exist without the object of which
     it needs to exist"; 390, "it closes when there is nothing contained within the corridor".
  I1 (computed, exact) The 4D stretch.  At the large end the plane reads four-dimensional Schwarzschild to
     O(ell^2/r0^2) (C3; m1_large M4).  Its interior in its own time, -dT^2 + G dt^2 + R^2 dOmega_2^2 with
     G = r0/R - 1, is vacuum exactly where R'^2 = G.  With p_t = -E~ and L conserved, every causal geodesic there has
     Tdot^2 = eps + E~^2/G + L^2/R^2, so T is monotone along it.  Between the horizon and any R_c > 0 T spans less than
     pi r0/2, the E~ = 0 fall.  A null geodesic has Tdot^2 >= E~^2 R_c/(r0 - R_c) + L^2/r0^2 > 0, a finite affine length.
     This is o1c_oneway Z2 at the large end, with the same steps.
  I2 (computed) Where the bulk enters.  The plane's 4D form holds while the curvature radius exceeds ell.  Its
     Kretschmann scalar 12 r0^2/R^6 reaches 1/ell^4 at R_5 = 12^(1/6) (r0 ell^2)^(1/3): 3.26 ell at r0 = 10 ell, and
     7.02 ell at r0 = 100 ell.  Below R_5 the bulk dimension enters at leading order and I1 no longer applies.  The
     quantum region (273; its boundary where the curvature reaches the bulk's Planck scale, 273 (b)'s estimate) lies
     far below R_5.  Even on the 4D form it would sit at R_5 (l5/ell)^(2/3) = 4.95e-14 R_5, with ell at its ceiling.  So
     between I1's stretch and 273's region lies a five-dimensional stretch of the large hole's interior.
  I3 (computed, exact; 273's construction) The README's own route.  The README is the thin null shell (o1c_oneway Z2b,
     the construction M chose at 273), and inside it the geometry is flat.  The shell's generators are radial null
     geodesics of that flat side, at every dimension, affinely r = r0 - E~ lambda: from our face to any radius in
     finite affine parameter, with curvature zero on the inner side.  On the 4D outer side the same ray is a geodesic
     with the same affine parameter.  So the README reaches 273's region along a route that does not depend on the 5D
     stretch's interior, and by the reflection (132; b_bounce Q1) it leaves position 2's past interior the same way, by
     position 2's face, which then closes (390).
  I4 (deduced) What the rows need that the record does not hold.  O1c at the large end is "every causal route of the
     passage complete", and the passage includes the open interior behind the shell (o1c_oneway Z6).  O1b is "no
     curvature singularity on the passage".  I1 and I3 settle the 4D stretch and the README's own route.  The 5D stretch,
     from about R_5 to 273's region, is the large brane hole's interior where the bulk dimension enters.  The record
     holds no interior solution of it: C3 is the exterior, READ, and the large hole's interior was never computed
     (item 356).  Required of it, with sources:
       (a) a function strictly monotone along every future causal geodesic there, its rate bounded below away from our
           face -- what makes every route reach 273's region in finite affine parameter (I1's T plays it in the 4D
           stretch; o1c_oneway Z2's at the small end);
       (b) no Cauchy horizon -- no inner horizon before 273's region (273's option text);
       (c) curvature finite until 273's region (O1b), with no singularity forming off the shell before the README
           reaches the region;
       (d) on position 2's side the same, with its own r_s2 (240) and its own sigma2 (387, 388), the interior at our
           sigma (d_ours, forced where the junction rises: junction_own G6).
  I5 (deduced) Two routes to (a)-(c), and what each costs.
       - A proof for every static vacuum interior of the large brane hole, from Einstein's law in the bulk (324-328) and
         the plane at sigma > 0 (both meet the null energy condition). Light: worked in the conversation, no runs.
       - A computed interior: the two-dimensional (time, radius, bulk) problem the runs of 365-367 attempted and 384
         dropped. Heavy: hours of runs and much of a week's data. Worth it only once (a)-(c) say what it must show.
     The board's order, to be overruled by M at any point: the proof first.

What this does not claim.
  - The 5D stretch itself: nothing about (a)-(c) there is computed here.
  - O(ell^2/R^2) corrections inside the 4D stretch: I1 is the plane's leading form, as C3 gives it outside.
  - The quantum region's own boundary: 273 (b)'s order-of-magnitude rule, an estimate.

Imports p2_gravity.py by path.  Stdlib + sympy.  python3 interior_large.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((132, "different views of the same object"), (270, "You are forgetting that the passage is one-way only"),
         (273, "One-way, complete, README only, no Cauchy horizon"),
         (109, "A horizon cannot exist without the object of which it needs to exist"),
         (390, "it closes when there is nothing contained within the corridor"))


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def _item(n):
    text = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. (.*?)(?=^\d+\. )" % n, text, re.S | re.M)
    return " ".join((m.group(1) if m else text[text.find("\n%d. " % n):]).split())


def _einstein(g, x):
    n = len(x)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    ric = sp.Matrix(n, n, lambda b, c: sp.simplify(sum(
        sp.diff(Gam[a][b][c], x[a]) - sp.diff(Gam[a][b][a], x[c])
        + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n)) for a in range(n))))
    rs = sp.simplify(sum(gi[a, b] * ric[a, b] for a in range(n) for b in range(n)))
    return sp.simplify(ric - rs * g / 2)


def stretch4():
    """I1: the Schwarzschild interior in its own time; vacuum iff R'^2 = G; the geodesic first integral"""
    T, t, th, ph = sp.symbols("T t theta phi", real=True)
    r0, Rc, E, L = sp.symbols("r_0 R_c E L", positive=True)
    R = sp.Function("R")(T)
    G = r0 / R - 1
    if MUT.get("exterior_sign"):
        G = 1 - r0 / R                                            # the mutant: the exterior's sign inside
    g = sp.diag(-1, G, R ** 2, R ** 2 * sp.sin(th) ** 2)
    Ein = _einstein(g, [T, t, th, ph])
    Rp = sp.Symbol("Rp")
    on = {sp.Derivative(R, T): Rp}
    tt = sp.simplify(Ein[0, 0].subs(on))
    constraint = sp.solve(sp.Eq(tt, 0), Rp ** 2) if tt.has(Rp) else []
    Rs = sp.Symbol("R", positive=True)
    Gs = G.subs(R, Rs)
    eps = sp.Symbol("epsilon", nonnegative=True)
    tdot2 = eps + E ** 2 / Gs + L ** 2 / Rs ** 2                  # -1 = -Tdot^2 + G tdot^2 + R^2 phidot^2 (eps = 1)
    norm = sp.simplify(-tdot2 + Gs * (E / Gs) ** 2 + Rs ** 2 * (L / Rs ** 2) ** 2 + eps)
    fall = sp.integrate(1 / sp.sqrt(r0 / Rs - 1), (Rs, 0, r0))     # E~ = 0 fall: dT = dR / sqrt(G)
    null_lb = sp.simplify((E ** 2 / Gs).subs(Rs, Rc))
    return dict(constraint=[sp.simplify(c - Gs.subs(Rs, R)) for c in constraint], norm=norm, fall=sp.simplify(fall),
                null_lb=null_lb, r0=r0, Rc=Rc, E=E)


def where_bulk():
    """I2: the 4D Kretschmann scalar, R_5 where it reaches 1/ell^4, and the quantum region's position on the 4D form"""
    t, r, th, ph = sp.symbols("t r theta phi", positive=True)
    r0, ell, l5 = sp.symbols("r_0 ell l_5", positive=True)
    f = 1 - r0 / r
    g = sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2)
    x = [t, r, th, ph]
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                             for d in range(4)) / 2) for c in range(4)] for b in range(4)] for a in range(4)]
    def riem(a, b, c, d):
        return (sp.diff(Gam[a][b][d], x[c]) - sp.diff(Gam[a][b][c], x[d])
                + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(4)))
    Rm = {(a, b, c, d): sp.simplify(riem(a, b, c, d)) for a in range(4) for b in range(4) for c in range(4)
          for d in range(4)}
    K = sp.simplify(sum(sum(g[a, e] * Rm[(e, b, c, d)] for e in range(4))
                        * sum(gi[b, p] * gi[c, q] * gi[d, s] * Rm[(a, p, q, s)]
                              for p in range(4) for q in range(4) for s in range(4))
                        for a in range(4) for b in range(4) for c in range(4) for d in range(4)
                        if any(Rm[(e, b, c, d)] != 0 for e in range(4))))
    if MUT.get("kretschmann_48"):
        K = 48 * r0 ** 2 / r ** 6                                 # the mutant: 48 M^2 read with r0 for M
    R5 = sp.solve(sp.Eq(K, 1 / ell ** 4), r)
    Rq = sp.solve(sp.Eq(K, 1 / l5 ** 4), r)
    PG = _load("p2_gravity.py", "il_pg")
    lP = (PG.HBAR * PG.G / PG.C ** 3) ** 0.5
    l5v = (lP ** 2 * PG.ELL_MAX) ** (1 / 3)
    if MUT.get("lP_for_l5"):
        l5v = lP                                                  # the mutant: the 4D Planck length for the bulk's
    ratio = float((Rq[0] / R5[0]).subs({l5: l5v, ell: PG.ELL_MAX}))
    return dict(K=K, R5=R5[0], r0=r0, ell=ell, at10=float((R5[0] / ell).subs(r0, 10 * ell)),
                at100=float((R5[0] / ell).subs(r0, 100 * ell)), ratio=ratio, l5=l5v, ell_max=PG.ELL_MAX)


def readme_route():
    """I3: the shell's generators -- radial null geodesics of the flat inner side and the outer side, n = 2 and 3"""
    lam, E, r0 = sp.symbols("lambda E r_0", positive=True)
    out = {}
    for n in (2, 3):
        # ingoing Eddington form -f dv^2 + 2 dv dr + r^2 dOmega_n^2: a radial ray v = const has r(lambda) affine iff
        # r'' = 0 (the r-component of the geodesic equation along it, for any f); flat inside the shell, f = 1
        r = r0 - E * lam
        v, rr = sp.symbols("v r")
        for label, f in (("flat", sp.Integer(1)), ("outer", 1 - (r0 / rr) ** (n - 1))):
            g = sp.Matrix([[-f, 1], [1, 0]])
            x = [v, rr]
            gi = g.inv()
            Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                                                 - sp.diff(g[b, c], x[d])) for d in range(2)) / 2)
                     for c in range(2)] for b in range(2)] for a in range(2)]
            k = [0, -E]                                           # dv/dlambda = 0, dr/dlambda = -E
            if MUT.get("route_nonaffine") and label == "outer":
                k = [0, -E * (1 - r0 / rr)]
            acc = [sp.simplify(sp.diff(k[a], rr) * k[1] + sum(Gam[a][b][c] * k[b] * k[c] for b in range(2)
                                                               for c in range(2))) for a in range(2)]
            out[(n, label)] = dict(null=sp.simplify(sum(g[a, b] * k[a] * k[b] for a in range(2) for b in range(2))),
                                   geodesic=all(z == 0 for z in acc))
        out[(n, "length")] = sp.solve(sp.Eq(r, 0), lam)[0]
    return out


def compute():
    return dict(s4=stretch4(), wb=where_bulk(), rr=readme_route())


def report(o):
    print("interior_large.py -- the large end's interior: what the rulings require, what the record gives (item 391)\n")
    s = o["s4"]
    print("I1 vacuum iff R'^2 = G: %s; first integral holds: %s; E~ = 0 fall from r0: %s; null bound E~^2/G at R_c: %s"
          % (s["constraint"] == [0], s["norm"] == 0, s["fall"], s["null_lb"]))
    w = o["wb"]
    print("I2 Kretschmann %s; R_5 = %s: %.3g ell at r0 = 10 ell, %.3g ell at 100 ell; quantum region on the 4D form at "
          "%.3g R_5 (l5 = %.3g m)" % (w["K"], w["R5"], w["at10"], w["at100"], w["ratio"], w["l5"]))
    r = o["rr"]
    for n in (2, 3):
        print("I3 n = %d: flat side null %s geodesic %s; outer side null %s geodesic %s; reaches r = 0 at lambda = %s"
              % (n, r[(n, "flat")]["null"] == 0, r[(n, "flat")]["geodesic"], r[(n, "outer")]["null"] == 0,
                 r[(n, "outer")]["geodesic"], r[(n, "length")]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    s, w, r = o["s4"], o["wb"], o["rr"]
    add("I0 132, 270, 273, 109 and 390 verbatim in their items", all(" ".join(t.split()) in _item(n) for n, t in WORDS))
    add("I1 the 4D interior is vacuum iff R'^2 = G; T monotone; the E~ = 0 fall pi r0/2; null bound E~^2 R_c/(r0 - R_c)",
        s["constraint"] == [0] and s["norm"] == 0 and sp.simplify(s["fall"] - sp.pi * s["r0"] / 2) == 0
        and sp.simplify(s["null_lb"] - s["E"] ** 2 * s["Rc"] / (s["r0"] - s["Rc"])) == 0)
    add("I2 Kretschmann 12 r0^2/R^6; R_5 = 12^(1/6) (r0 ell^2)^(1/3): 3.26 ell at 10 ell, 7.02 at 100; the quantum "
        "region far below it", sp.simplify(w["K"] - 12 * w["r0"] ** 2 / sp.Symbol("r", positive=True) ** 6) == 0
        and "%.3g" % w["at10"] == "3.26" and "%.3g" % w["at100"] == "7.02" and "%.3g" % w["ratio"] == "4.95e-14")
    add("I3 the shell's generators are affine radial null geodesics on the flat side and the outer side, n = 2 and 3, "
        "reaching r = 0 at lambda = r0/E", all(r[(n, side)]["null"] == 0 and r[(n, side)]["geodesic"]
                                                for n in (2, 3) for side in ("flat", "outer"))
        and all(sp.simplify(r[(n, "length")] - sp.Symbol("r_0", positive=True) / sp.Symbol("E", positive=True)) == 0
                for n in (2, 3)))
    return res


MUTANTS = {"exterior_sign": "the exterior's G = 1 - r0/R used inside the horizon (I1)",
           "kretschmann_48": "48 M^2/r^6 read with r0 for M (I2)",
           "lP_for_l5": "the 4D Planck length taken for the bulk's l5 (I2)",
           "route_nonaffine": "the outer side's ray parametrized by Killing time, not affinely (I3)"}


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
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-16s %-62s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
