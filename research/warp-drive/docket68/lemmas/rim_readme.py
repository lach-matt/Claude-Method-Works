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
  R5 (computed, imported m1_facing.py) the coincidence law: a corridor approaching our plane carries minus the plane's
     stress (e2 -> -sigma, P2 -> +sigma at y2 -> 0, at every ell tested; SIM2-FACING S15's "exactly minus P1's").  So a
     corridor leaving the plane tangentially where the plane carries the README's stress carries minus that stress near
     the rim: its null energy there is -(rho + p) of the README's, negative.  The reading H-CORRIDOR-IS-THE-README-SHEET
     (the corridor as the README's sheet peeling off the plane tangentially) fails (Z) at the rim
  R6 (cypher) the whole static rim -- plane, corridor and rim together, with the NEC in both directions, finite energy
     and force balance at the rim (standard-not-READ: sheets meeting along a line balance their tensions; in the flat
     limit our plane's own tension is negligible beside the corridor's) -- against every arrangement computed or
     deduced: the marginal (steep) corridor, constant depth, the tangent README sheet, the README on the plane without an
     edge, the throat region.  The target is in no cell; see the run for which languages refuse and which over-reach
  R7 (deduced; standard-not-READ force balance) at finite ell, within one universe the two sheets of our plane enclose
     the corridor and rejoin at the rim; balancing tensions along their conormals, sigma (outside) = sigma (inside, ours)
     + sigma (inside, position 2's) + T_corridor, at the meeting angle.  With the coincidence law (R5: the corridor
     carries -sigma where it meets the plane) the rim balances exactly with pure tensions: sigma = sigma + sigma - sigma
     -- provided the corridor arrives tangentially (any meeting angle breaks it; sympy: theta = 0 the only root)
  R8 (computed, p2_full.py) a corridor near the plane has radial null energy proportional to its depth: at r = 2.1m,
     -0.0079, -0.016, -0.032 at depths 0.25, 0.5, 1m (linear), of the sign of eq. (17)'s own 4D radial null deficit
     (R4(k,k) = -2r''/r < 0, F1-AUDIT C1).  So the tangential arrival R7 requires carries eq. (17)'s negative radial null
     energy onto the corridor near the rim -- (Z) through TS fails there, unless something on the same rays carries the
     opposite
  R9 (cypher) the finite-ell rim: the tangent meeting with pure tensions (balance holds, radial NEC fails), the steep
     meeting (balance fails, tangential NEC fails), and the tangent meeting with the README's stress on our plane near
     the rim cancelling the corridor's negative radial null energy along the same grazing rays (balance and (Z) net per
     ray, as 183 reads it) -- whose compatibility with 195 ("The README is not a pair") and 198 is M's to say, not the
     cypher's; that cell is entered with its compatibility unknown.  Statistics admits no closing rim under any of the
     six codings of the nominal meeting axis; order, algebra, geometry and information each invent one, but which meeting
     they close moves with the coding -- an artefact of ordering a nominal axis, not a reading.  Ignoring compatibility,
     all five admit the README-cancelling cell; marked compatible, all five admit it, statistics included
So, in the flat limit and static, no arrangement computed or deduced closes the rim: the steep corridor misses the
tangential null energy and an unbalanced pull normal to the plane; the tangent one carries minus the README's stress; the
README alone on the plane needs an edge.  What could still close it is named in the note, not chosen here.  Imports tools/cypher.py by path.  Stdlib + sympy.
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


def coincidence():
    spec = importlib.util.spec_from_file_location("rr_m1f", os.path.join(HERE, "m1_facing.py"))
    m = importlib.util.module_from_spec(spec)
    sys.modules["rr_m1f"] = m
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return {x: m.facing(x, 20000)["first"][1:3] for x in (0.0739, 0.5)}


def cypher_rim():
    spec = importlib.util.spec_from_file_location("rr_cypher2", os.path.join(ROOT, "tools", "cypher.py"))
    cy = importlib.util.module_from_spec(spec)
    sys.modules["rr_cypher2"] = cy
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(cy)
    C = ["config", "nec_radial", "nec_tangential", "finite_energy", "balance", "whole"]
    # config: 0 marginal (steep) corridor, 1 constant depth, 2 tangent README sheet, 3 README on the plane without an edge,
    # 4 the throat region; balance: 0 fails, 1 holds, 2 no rim (does not meet the plane)
    cells = [(0, 1, 0, 1, 0, 1), (1, 0, 1, 1, 2, 1), (2, 1, 0, 1, 0, 1), (3, 1, 1, 0, 2, 1), (4, 1, 1, 1, 2, 0)]
    if MUT.get("seat_rim"):
        cells.append((5, 1, 1, 1, 1, 1))
    ok = lambda h: h[1] == 1 and h[2] == 1 and h[3] == 1 and h[4] == 1 and h[5] == 1

    def ask(cs):
        cl = sorted(set(cs))
        ix = cy.Index("rim", C, [list(c) for c in cl])
        inv = [{v: k for k, v in ix.code[i].items()} for i in range(len(C))]
        res = {}
        for lang in ("order", "algebra", "geometry", "information", "statistics"):
            out, _ = cy.ADMISSION[lang][0](ix, {})
            res[lang] = None if out is None else any(all(c[i] in inv[i] for i in range(len(C)))
                                                     and ok(tuple(inv[i][c[i]] for i in range(len(C)))) for c in out)
        return res
    return ask(cells)


def rim_balance():
    """R7: outside sheet (tension sigma) along +x; the two inside sheets (ours, position 2's, sigma each) along -x; the
    corridor (coincidence law: -sigma, or T free) leaving at angle theta to the plane.  Balance both components."""
    s, th, T = sp.symbols("sigma theta T", real=True)
    Tc = -s if not MUT.get("corridor_plus") else s
    fx = s - 2 * s - Tc * sp.cos(th)
    fy = -Tc * sp.sin(th)
    sol = sp.solve([fx, fy], th, dict=True)
    free = sp.solve([s - 2 * s - T * sp.cos(th), -T * sp.sin(th)], [T, th], dict=True)
    return {"theta": sorted({sp.nsimplify(d[th]) for d in sol}, key=str), "free": free}


def depth_law():
    spec = importlib.util.spec_from_file_location("rr_p2f", os.path.join(HERE, "p2_full.py"))
    p = importlib.util.module_from_spec(spec)
    sys.modules["rr_p2f"] = p
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(p)
    b4 = p._b4()
    rows = p.column(b4, "21/10")
    return {r["y2"]: r["nec_r"] for r in rows if r["y2"] in (0.25, 0.5, 1.0)}


def cypher_finite():
    spec = importlib.util.spec_from_file_location("rr_cypher3", os.path.join(ROOT, "tools", "cypher.py"))
    cy = importlib.util.module_from_spec(spec)
    sys.modules["rr_cypher3"] = cy
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(cy)
    C = ["meeting", "balance", "nec_radial", "nec_tangential", "compatible"]
    # meeting 0 tangent pure tensions, 1 steep, 2 tangent with the README cancelling on the same rays; compatible 2 = unknown
    cells = [(0, 1, 0, 1, 1), (1, 0, 1, 0, 1), (2, 1, 1, 1, 2)]
    if MUT.get("decide_compat"):
        cells[2] = (2, 1, 1, 1, 1)                                  # M's question decided in code
    ok = lambda h: h[1] == 1 and h[2] == 1 and h[3] == 1 and h[4] == 1
    okq = lambda h: h[1] == 1 and h[2] == 1 and h[3] == 1          # ignoring compatibility
    langs = ("order", "algebra", "geometry", "information", "statistics")

    def ask(cs, test):
        """per language: the meeting kinds (decoded back to 0/1/2) of the admitted cells that pass the test, or None"""
        cl = sorted(set(cs))
        ix = cy.Index("finite_rim", C, [list(c) for c in cl])
        inv = [{v: k for k, v in ix.code[i].items()} for i in range(len(C))]
        res = {}
        for lang in langs:
            out, _ = cy.ADMISSION[lang][0](ix, {})
            if out is None:
                res[lang] = None
                continue
            dec = {tuple(inv[i][c[i]] for i in range(len(C))) for c in out if all(c[i] in inv[i] for i in range(len(C)))}
            res[lang] = sorted(h[0] for h in dec if test(h))
        return res

    def recode(perm, cs):
        return [(perm[c[0]],) + tuple(c[1:]) for c in cs]

    # the meeting coordinate is nominal: put every one of its six codings to the cypher, decode back, and keep what moves
    by_coding = {}
    for perm in __import__("itertools").permutations(range(3)):
        back = {perm[k]: k for k in range(3)}
        r = ask(recode(perm, cells), ok)
        by_coding[perm] = {l: (None if v is None else sorted(back[m] for m in v)) for l, v in r.items()}
    return {"compatible_target": by_coding[(0, 1, 2)], "by_coding": by_coding, "physics_only": ask(cells, okq),
            "ctrl_compatible": ask(cells[:2] + [(2, 1, 1, 1, 1)], ok)}


def compute():
    return {"g": gauss(), "t": tail_bound(), "cy": cypher_plane(), "co": coincidence(), "rim": cypher_rim(),
            "rb": rim_balance(), "dl": depth_law(), "fin": cypher_finite()}


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
    co = d["co"]
    add("R5 the coincidence law: the corridor at y2 -> 0 carries minus the plane's stress (e2 -> -sigma, P2 -> +sigma)",
        all(abs(v[0] + 1) < 2e-3 and abs(v[1] - 1) < 2e-3 for v in co.values()))
    add("R6 cypher: the whole static rim (NEC both ways, finite energy, balance) is admitted by no language on the "
        "computed and deduced arrangements", d["rim"]["statistics"] is False and d["rim"]["geometry"] is False)
    rb = d["rb"]
    add("R7 the finite-ell rim with pure tensions balances only with the corridor carrying -sigma and arriving "
        "tangentially (theta = 0)", rb["theta"] == [0] and all(f.get(sp.Symbol("theta", real=True)) in (0, None)
        for f in rb["free"]))
    dl = d["dl"]
    add("R8 a corridor near the plane: radial null energy < 0 and linear in depth at r = 2.1m (ratios 2.0 +- 0.1)",
        all(v < 0 for v in dl.values()) and 1.9 < dl[0.5] / dl[0.25] < 2.1 and 1.9 < dl[1.0] / dl[0.5] < 2.1)
    f = d["fin"]
    bc = f["by_coding"]
    stat_refuses = all(v["statistics"] == [] for v in bc.values())
    others_move = all(len({tuple(v[l]) for v in bc.values()}) > 1 for l in ("order", "algebra", "geometry", "information"))
    add("R9 cypher: with compatibility required, statistics admits no closing finite-ell rim under any of the six codings "
        "of the nominal meeting axis; order, algebra, geometry and information each admit one, but which meeting closes "
        "moves with the coding (an artefact of ordering a nominal axis, not a reading)", stat_refuses and others_move)
    add("R9 ignoring compatibility, every language admits the README-cancelling tangent rim (meeting 2); control: that cell "
        "marked compatible is admitted by all five, statistics included", all(2 in (f["physics_only"][l] or [])
        for l in f["physics_only"]) and all(2 in (f["ctrl_compatible"][l] or []) for l in f["ctrl_compatible"]))
    return res


MUTANTS = {"seat_rim": "a closing rim seated as data", "trace_half": "the trace term taken with 1/2 instead of 1/3", "fast_tail": "the tail made to decay faster",
           "corridor_plus": "the corridor given +sigma (the coincidence law's sign flipped)",
           "decide_compat": "the README cell marked compatible (M's 195/198 question decided in code)"}


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
