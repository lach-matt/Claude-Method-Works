#!/usr/bin/env python3
"""rim_readme.py -- where the README's stress can sit to close the corridor's rim gap, step by step through the cypher
(computed, deduced; flat limit; not verified by a separate session; not seated; 2026-10-10).

corridor_shape.py left one gap: the tangential null energy on the corridor's last stretch before the rim, at most 1/68
of E, which only the README has the energy to cover.  This works out where it can sit.

  R1 (deduced) not on the corridor alone: a thin surface's stress IS the jump in extrinsic curvature, and the two bulks
     are fixed by the planes' data, so "the README on the corridor" relabels the same stress.  It must change the
     planes' data: the README's stress on the planes near the mouth -- 172 (1) allowed it on position 2's piece, and
     within one universe that piece is our plane, symmetric by 202
  R2 (computed, sympy) keeping eq. (17) exactly (R4 = 0) with a flat-limit vacuum bulk, Gauss on the plane is
     K^2 - K.K = -(1/4)(tau.tau - T^2/3) = 0: the README's stress lies on the cone
     p_theta = p_r - rho +- sqrt(3) sqrt(-p_r rho), so p_r <= 0.  On the + branch with -rho <= p_r <= 0 the NEC holds in
     both directions; its edge p_r = -rho is the AdS2-type stress a regular held stress has at a horizon (Lemma S)
  R3 (cypher) "a README stress on our plane keeping eq. (17) and obeying the NEC": statistics and geometry admit only
     the + branch and nothing when it is left out; order, algebra, information also admit the - branch (over-reach)
  R4 (deduced, analytic; checked numerically) static conservation on eq. (17), with p_r = -u rho (0 < u <= 1):
     rho'/rho = [-u' + (1 - u)/(r(r - 2m)) + 2(1 - sqrt3 sqrt u)/r]/u >= -u'/u + 2(1 - sqrt3)/r, the last term's minimum
     over u being at u = 1.  So rho falls no faster than r^(2 - 2 sqrt3) = r^-1.464 and int rho r^2 dr diverges: the
     README's stress on the plane cannot have finite energy without an edge.  At the rim, where the corridor meets our
     plane, the stress must end -- and an edge of a stressed plane needs a force there: a ring at the rim
So the rim gap is closed, if at all, by the README's stress on our plane near the mouth (the + cone), ending at the rim
on a ring whose force balance is the next computation.  Imports tools/cypher.py by path.  Stdlib + sympy.
python3 rim_readme.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
MUT = {}


def gauss():
    rho, pr, pt = sp.symbols("rho p_r p_theta", real=True)
    T = -rho + pr + 2 * pt
    third = sp.Rational(1, 3) if not MUT.get("trace_half") else sp.Rational(1, 2)
    K = [-(sp.Rational(1, 2)) * (x - T * third) for x in (-rho, pr, pt, pt)]
    g = sp.expand(sum(K) ** 2 - sum(k ** 2 for k in K))
    Q = sp.expand(rho ** 2 + pr ** 2 + 2 * pt ** 2 - T ** 2 / 3)
    cone = sp.solve(sp.Eq(Q, 0), pt)
    plus = max(cone, key=lambda e: e.subs({rho: 1, pr: sp.Rational(-1, 2)}))
    # NEC on the + branch across -rho <= p_r <= 0 (rho = 1)
    grid = [sp.Rational(-k, 10) for k in range(0, 11)]
    nec = all(sp.N(1 + plus.subs({rho: 1, pr: v})) >= -1e-12 for v in grid)
    minus = min(cone, key=lambda e: e.subs({rho: 1, pr: sp.Rational(-1, 2)}))
    nec_minus = all(sp.N(1 + minus.subs({rho: 1, pr: v})) >= 0 for v in grid[1:])
    edge = sp.simplify(plus.subs(pr, -rho).subs(rho, 1))
    return {"ratio": sp.simplify(g / Q), "plus_nec": nec, "minus_nec": nec_minus, "edge": edge}


def tail_bound():
    u = sp.Symbol("u", positive=True)
    f = 2 * (1 - sp.sqrt(3) * sp.sqrt(u)) / u
    crit = sp.solve(sp.diff(f, u), u)
    decreasing = all(sp.N(sp.diff(f, u).subs(u, v)) < 0 for v in (0.05, 0.3, 0.6, 0.99))
    fmin = sp.simplify(f.subs(u, 1))
    # numerical check: integrate rho'/rho for several u profiles from r = 2.5 to 1e4; fitted decay never beats r^fmin
    worst = []
    for prof in (lambda r: 1.0, lambda r: 0.5, lambda r: 0.2 + 0.8 * math.exp(-(r - 2.5)),
                 lambda r: 1 - 0.7 * math.exp(-(r - 2.5) / 3)):
        r, lr, h = 2.5, 0.0, 1e-3
        while r < 1e4:
            uu = prof(r); du = (prof(r + 1e-6) - prof(r - 1e-6)) / 2e-6
            rate = (-du + (1 - uu) / (r * (r - 2)) + 2 * (1 - math.sqrt(3) * math.sqrt(uu)) / r) / uu
            lr += rate * h
            r += h
            h = min(r * 1e-3, 50.0)
        worst.append(lr / math.log(1e4 / 2.5))
    if MUT.get("fast_tail"):
        worst = [w - 1.0 for w in worst]
    return {"fmin": fmin, "decreasing": decreasing, "slopes": worst}


def cypher_plane():
    spec = importlib.util.spec_from_file_location("rr_cypher", os.path.join(ROOT, "tools", "cypher.py"))
    cy = importlib.util.module_from_spec(spec)
    sys.modules["rr_cypher"] = cy
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(cy)
    C = ["kind", "keeps_eq17", "nec_radial", "nec_tangential"]
    cells = [(0, 0, 1, 1), (1, 0, 1, 1), (2, 0, 1, 1), (3, 0, 1, 1), (4, 1, 1, 1), (5, 1, 1, 0), (6, 1, 1, 1)]
    ok = lambda h: h[1] == 1 and h[2] == 1 and h[3] == 1

    def ask(cs):
        cl = sorted(set(cs))
        ix = cy.Index("plane", C, [list(c) for c in cl])
        inv = [{v: k for k, v in ix.code[i].items()} for i in range(len(C))]
        res = {}
        for lang in ("order", "algebra", "geometry", "information", "statistics"):
            out, _ = cy.ADMISSION[lang][0](ix, {})
            res[lang] = None if out is None else sorted({inv[0][c[0]] for c in out
                                                         if all(c[i] in inv[i] for i in range(4)) and ok(tuple(inv[i][c[i]] for i in range(4)))})
        return res
    return {"all": ask(cells), "leave": ask([c for c in cells if c[0] not in (4, 6)])}


def compute():
    return {"g": gauss(), "t": tail_bound(), "cy": cypher_plane()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    g = d["g"]
    add("R2 K^2 - K.K = -(1/4)(tau.tau - T^2/3): keeping eq. (17) puts the README's stress on the cone", g["ratio"] == sp.Rational(-1, 4))
    add("R2 the + branch obeys the NEC for -rho <= p_r <= 0; the - branch breaks it tangentially; the edge is "
        "(rho, -rho, (sqrt3 - 2) rho)", g["plus_nec"] and not g["minus_nec"] and sp.simplify(g["edge"] - (sp.sqrt(3) - 2)) == 0)
    c = d["cy"]
    add("R3 cypher: statistics and geometry admit only the + branch and nothing when it is left out; order, algebra, "
        "information over-reach to the - branch", c["all"]["statistics"] == [4, 6] and c["leave"]["statistics"] == []
        and c["leave"]["geometry"] == [] and 5 in c["all"]["order"])
    t = d["t"]
    add("R4 the decay bound: 2(1 - sqrt3 sqrt u)/u is decreasing on (0, 1], minimum 2(1 - sqrt3) = -1.464 at u = 1; every "
        "integrated profile decays no faster than r^-1.464 (to the integrator's 2e-3), so int rho r^2 dr diverges",
        t["decreasing"] and abs(float(t["fmin"]) + 1.4641) < 1e-3 and all(s >= -1.4641 - 2e-3 for s in t["slopes"]))   # 2e-3: the Euler step error
    return res


MUTANTS = {"trace_half": "the trace term taken with 1/2 instead of 1/3", "fast_tail": "the tail made to decay faster"}


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
        print("  mutant %-11s %-44s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    d = compute()
    print("cone ratio:", d["g"]["ratio"], " edge p_theta/rho:", d["g"]["edge"])
    print("tail: min exponent", d["t"]["fmin"], " fitted slopes", ["%.3f" % s for s in d["t"]["slopes"]])
    print("cypher:", d["cy"])
