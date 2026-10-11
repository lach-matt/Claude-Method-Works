#!/usr/bin/env python3
"""bounds.py -- item 241: the bounds, in M's three kinds, indexed to see how they interact and whether they identify or
mitigate one another.  M: "There are likely relativity bounds such as survivability, and structural bounds such as a
universe's own laws/rules/exceptions, and universal bounds that directly apply to the 5D bulk. Index the bounds to see
how they interact and if they identify or mitigate other bounds".  Worked in the conversation (computed, exact where
marked; READ where marked; deduced where marked; not verified by a separate session; not seated); 2026-10-11.

The address space (item 241 (a)): i, j -- a universe's 2b and 2P steps (G x 2^(i+j), tension x 2^(-2j)); w -- our
tension's place in its window, S0 x 2^w, w in [0, W]; z -- log2 of the offset's ratio to the tension against ours (item
233 K7's unseen axis); n -- log2 of the README's bits; law -- the matter law, ordered by how far it moves chemistry (ours
0, min 1, mirror 2); mu -- the object's means of mitigation, in doublings; field -- 1 if a field varies the 5D coupling
across the bulk.  Each bound is a slack, c0 + sum a_v v >= 0, exact in these variables where the bound is log-linear.

  B0 (read) M's item-241 words, verbatim in the rulings file.
  B1 (computed; each sourced) The bounds.  Universal (the 5D bulk): the corridor inside the bulk's curvature (ITEM197,
     the top), the README's capacity, the plane's positivity (229), one 5D coupling unless a field varies it (item 233
     K6), the null energy per ray (183) and the shared SI (225 A) -- the last two invariants, binding everywhere alike.
     Structural (a universe's own laws): the table-top floor (relative and absolute readings), the matter law's
     exceptions (Cu2 binds only off the mirror law, 221), the G ceiling where a universe's window closes (233), and the
     regime in which matter's own density governs its gravity at the throat (236 R4).  Relativity (the object against
     position 2, 240): survivability's tolerances on gravity, dark energy, the closing energy and chemistry, and the
     README match (a relation).  Not run: "not already contained" (230) -- no instrument decides it; withdrawn: T3's
     ceiling as the build's need (239).
  B2 (computed, exact) Identification.  The G ceiling is the top plus the relative floor, exactly (W - i - j = (W - w -
     2i) + (w + i - j)): it is identified by them, not a bound of its own.  The README's capacity is the plane's
     positivity plus the throat's matter regime, plus log2(4/3) exactly: N_max / N = (4/3) (sigma / 2 delta sigma)
     (rho_E / 2 sigma) for every universe and README (the constants cancel symbolically; checked at random points to
     1e-12) -- a universal bound identified by a universal and a structural one.  The capacity also follows from the
     top whenever z + n <= log2 N_max0 - W + w = 209.06 + w (the example README sits 157.78 inside).  The closing
     energy's tolerance acts along the gravity floor's direction at half its rate (E2/E = (G2/G)^-1/2).
  B3 (computed) The open direction (item 233's 2P step, j -> -infinity at fixed i).  No structural bound closes it.
     Four close it: survivability's gravity floor, its closing-energy tolerance and its dark-energy ceiling (relativity:
     Lambda4 ~ 2^(i - j + z) grows along the step), and one 5D coupling without a field (universal: kappa5^4 ~ 2^(i + 3j)
     falls).  The dark-energy ceiling leaves the diagonal open (both steps reversed together, Lambda4 unchanged); the
     gravity floor and one coupling make the region finite.  With M's field (230: the bulk does the work) the coupling
     is lifted, so the bound item 237 found missing is relativity's: survivability's gravity floor, finite for any object
     whose tolerance is finite.
  B4 (computed) Mitigation and trade, by shared variables.  The offset's ratio z relaxes the capacity, the positivity
     and survivability's dark-energy ceiling together (a smaller offset at position 2 compensates its Lambda4); our
     tension's place w trades the top against the floors (raising it loosens a floor and tightens the top: their meeting
     is the G ceiling); the README's size n tightens the capacity and leaves the throat's matter regime sooner; the
     object's means mu relax every relativity bound and no other.
  B5 (computed; the record's bodies) A structural bound mitigating a relativity bound: the matter law changes how hard
     gravity presses at a body's surface at fixed G (density): for Cu, Ag and Au it tightens survivability's gravity
     tolerance (surface gravity x 1.04-1.25), for Cr it relaxes it (x 0.97 / 0.96 under min / mirror, a less dense
     solid).  Which way depends on the object's material.
  B6 (computed; the cypher, roster 1173, audited) The bounds as cells over (kind, and the sign each variable moves its
     slack); seventeen cells, no key, no one-hot code.  M's three kinds are not contradicted by how the bounds act: no
     two acting bounds of different kinds act alike, and the object's means enter exactly the relativity bounds.  The
     three invariants (the null energy per ray, the shared SI, the README match) act on no variable, so their kind is by
     meaning, not by action.  The critic's limit, recorded: with every acting bound acting differently, any labelling
     would pass this test, and mu enters only relativity bounds because survivability is defined against the object --
     so the cypher fails to refute the three kinds; it does not confirm them.  The interactions are B2-B5's, computed.

What this does not show.
  - mu is the object's and is not computed; survivability's tolerances are symbols, their signs exact.
  - The matter law enters as an ordinal; its effects are element by element (B5), not one sign.
  - "Not already contained" (230) and the corridor's own energy against the README's (203) are not computed.

Imports bulk5_index.py, ledger_cypher.py (and through them p2_gravity.py), p2_matter.py, tools/cypher.py and
index_audit.py by path.  Stdlib.  python3 bounds.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M241 = ("There are likely relativity bounds such as survivability, and structural bounds such as a universe's own "
        "laws/rules/exceptions, and universal bounds that directly apply to the 5D bulk.")
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
VARS = ["i", "j", "w", "z", "n", "law", "mu", "field"]
KINDS = {"universal": 0, "structural": 1, "relativity": 2}


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


B5M = _load(os.path.join(HERE, "bulk5_index.py"), "bd_b5")
PG = B5M.PG
K = B5M.constants()
W = K["W"]
N_EX = 2742570311524972


def constants():
    nmax0 = PP_sector_nmax()
    c_pos = math.log2(K["S0"] / (2 * PG.DSIG))
    E = PG.corridor(PG.G)["E1"] * math.sqrt(N_EX)
    r0 = 2 * PG.G * E / PG.C ** 4
    rho_E = E / (4 / 3 * math.pi * r0 ** 3)
    return dict(W=W, lognmax0=math.log2(nmax0), c_pos=c_pos, n_ex=math.log2(N_EX),
                c_reg=math.log2(rho_E / (2 * K["S0"])) + math.log2(N_EX))


def PP_sector_nmax():
    return B5M.PP.sector(1, F(1))["N_max"]


# ================================================================================ B1 the bounds
def bounds(c):
    """name: (kind, source, slack coefficients {const, var: a}, note).  A slack >= 0 is inside the bound."""
    b = {
        "top (corridor inside the curvature)": ("universal", "ITEM197; 233 K3", {"const": c["W"], "i": -2, "w": -1}, ""),
        "README capacity": ("universal", "N <= N_max; 233 K3", {"const": c["lognmax0"], "i": -2, "z": -1, "n": -1}, ""),
        "plane positivity": ("universal", "229; sigma > 2 delta sigma", {"const": c["c_pos"], "w": 1, "z": -1}, ""),
        "one coupling, above": ("universal", "233 K6", {"const": 0, "i": -1, "j": -3, "field": 1}, "lifted by a field"),
        "one coupling, below": ("universal", "233 K6", {"const": 0, "i": 1, "j": 3, "field": 1}, "lifted by a field"),
        "null energy per ray": ("universal", "183 (Z)", {"const": 1}, "invariant"),
        "shared SI": ("universal", "225 A", {"const": 1}, "invariant"),
        "table-top floor (relative)": ("structural", "233 K3", {"const": 0, "i": 1, "j": -1, "w": 1}, ""),
        "table-top floor (absolute)": ("structural", "233 K3", {"const": 0, "j": -2, "w": 1}, ""),
        "matter exceptions (Cu2 off mirror)": ("structural", "221", {"const": F(3, 2), "law": -1}, ""),
        "G ceiling": ("structural", "233", {"const": c["W"], "i": -1, "j": -1}, "derived"),
        "throat matter regime": ("structural", "236 R4", {"const": c["c_reg"], "n": -1, "i": -2, "w": -1}, "a regime"),
        "survive: gravity, above": ("relativity", "240", {"const": 0, "i": -1, "j": -1, "mu": 1}, ""),
        "survive: gravity, below": ("relativity", "240", {"const": 0, "i": 1, "j": 1, "mu": 1}, ""),
        "survive: dark energy, above": ("relativity", "240", {"const": 0, "i": -1, "j": 1, "z": -1, "mu": 1}, ""),
        "survive: dark energy, below": ("relativity", "240", {"const": 0, "i": 1, "j": -1, "z": 1, "mu": 1}, ""),
        "survive: closing energy": ("relativity", "240; copy_p2 C1", {"const": 0, "i": F(1, 2), "j": F(1, 2), "mu": 1}, ""),
        "survive: chemistry": ("relativity", "240", {"const": 0, "law": -1, "mu": 1}, ""),
        "README match": ("relativity", "240 (b); copy_p2 C1", {"const": 1}, "a relation"),
    }
    if MUT.get("floor_sign"):
        b["table-top floor (relative)"] = ("structural", "", {"const": 0, "i": 1, "j": 1, "w": 1}, "")
    return b


NOT_RUN = {"not already contained": "230 -- no instrument decides it", "T3's ceiling as the need": "withdrawn, 239"}


def vec(coef):
    return [F(coef.get(v, 0)) for v in VARS]


def sign(x):
    return (x > 0) - (x < 0)


# ================================================================================ B2 identification
def identities(b):
    """a bound identified by two others: its variable coefficients the sum of theirs (non-negative multiples) and its
    constant at least theirs combined -- exact"""
    out = []
    names = [n for n in b if any(vec(b[n][2]))]
    for cname in names:
        cv, c0 = vec(b[cname][2]), F(b[cname][2].get("const", 0))
        for a, d in itertools.combinations([n for n in names if n != cname], 2):
            av, bv = vec(b[a][2]), vec(b[d][2])
            # solve cv = la av + lb bv on the first two non-zero coordinates, check the rest
            for la in (F(1), F(1, 2), F(2)):
                for lb in (F(1), F(1, 2), F(2)):
                    if all(cv[k] == la * av[k] + lb * bv[k] for k in range(len(VARS))):
                        resid = c0 - la * F(b[a][2].get("const", 0)) - lb * F(b[d][2].get("const", 0))
                        if resid >= 0:
                            out.append((cname, a, d, la, lb, resid))
    return out


def capacity_identity(points=((1.0, 1.0, 1.0, 1e15), (2.0, 0.25, 3.0, 7e9), (0.37, 5.0, 0.01, 1e40))):
    """N_max / N against (4/3)(sigma / 2 delta sigma)(rho_E / 2 sigma) at (G factor, sigma factor, offset factor, N)"""
    out = []
    for gf, sf, of, N in points:
        Gx = PG.G * gf
        sig, ds = K["S0"] * sf, PG.DSIG * of
        sP = PG.C ** 7 / (PG.HBAR * Gx ** 2)
        nmax = sP / (8 * math.log(2) * ds)
        r0 = math.sqrt(N * 2 * PG.H * Gx * math.log(2) / (math.pi * PG.C ** 3) / (4 * math.pi))
        E = r0 * PG.C ** 4 / (2 * Gx)
        rho = E / (4 / 3 * math.pi * r0 ** 3)
        out.append((nmax / N) / ((4 / 3) * (sig / (2 * ds)) * (rho / (2 * sig))))
    return out


def capacity_vs_top(c):
    """capacity - top = (log2 N_max0 - W) + w - z - n: the capacity follows from the top while that is >= 0"""
    margin0 = c["lognmax0"] - c["W"]
    return dict(margin0=margin0, at_example=margin0 - c["n_ex"])


# ================================================================================ B3 the open direction
def closes_open_direction(b):
    """a bound closes j -> -infinity at fixed i (the 2P step toward weak gravity) when its slack falls with it: a_j > 0"""
    return sorted(n for n, (k, s, coef, note) in b.items() if F(coef.get("j", 0)) > 0)


def finite_with(names, b, mu=40, field=1):
    """is the lattice region finite with these bounds plus the top and the relative floor (w = W/2, z = 0, n = n_ex)?"""
    vals = dict(w=W / 2, z=0, n=math.log2(N_EX), law=0, mu=mu, field=field * 10 ** 6)
    base = ["top (corridor inside the curvature)", "table-top floor (relative)"] + list(names)
    edge = False
    for i in range(-400, 101):
        for j in range(-400, 201):
            vals.update(i=i, j=j)
            if all(float(b[n][2].get("const", 0)) + sum(float(b[n][2].get(v, 0)) * vals[v] for v in VARS) >= 0 for n in base):
                if i == -400 or j == -400:
                    edge = True
    return not edge


# ================================================================================ B4 mitigation and trade
def relations(b):
    """for each pair of bounds and each variable they share: the same sign relaxes both (mitigates), opposite signs
    trade them"""
    rel = {}
    names = list(b)
    for a, d in itertools.combinations(names, 2):
        for v in VARS:
            sa, sd = sign(F(b[a][2].get(v, 0))), sign(F(b[d][2].get(v, 0)))
            if sa and sd:
                rel.setdefault((a, d), []).append((v, "mitigates" if sa == sd else "trades"))
    return rel


# ================================================================================ B5 the matter law against survivability
def matter_vs_gravity():
    pm = _load(os.path.join(HERE, "p2_matter.py"), "bd_pm")
    o = pm.compute()
    out = {}
    for el in ("Cu", "Ag", "Au", "Cr"):
        s0 = o["sol"][(el, "ours")]
        g0 = PG.body(1e22, s0["rho"], s0["B0"] * 1e9, s0["Bp"], PG.G)["g"]
        out[el] = {law: PG.body(1e22, o["sol"][(el, law)]["rho"], o["sol"][(el, law)]["B0"] * 1e9, o["sol"][(el, law)]["Bp"],
                                PG.G)["g"] / g0 for law in ("min", "mirror")}
    return out


# ================================================================================ B6 the cypher
def cypher_index(cy, ia, b):
    cells = {}
    for n, (k, s, coef, note) in b.items():
        cells.setdefault(tuple([KINDS[k]] + [sign(F(coef.get(v, 0))) for v in VARS]), []).append(n)
    coords = ["kind"] + VARS
    held = sorted(cells)
    vo = {"kind": [0, 1, 2]}
    vo.update({v: sorted({c[x + 1] for c in held}, key=lambda t: (abs(t), t)) for x, v in enumerate(VARS)})
    ix = cy.Index("bounds", coords, [list(c) for c in held], value_order=vo)
    rows, keys = cy.coordinate_report(ix)
    kind_free = {tuple(c[1:]) for c in held}
    acting = [c for c in held if any(c[1:])]
    collide = sorted({n for c in held if not any(c[1:]) for n in cells[c]})
    return dict(cells=cells, n=len(held), adds_nothing=[r["coordinate"] for r in rows if r["adds_nothing"]], keys=keys,
                kind_determined=len(kind_free) == len({tuple(c[1:]) + (c[0],) for c in held}),
                kind_determined_acting=len({tuple(c[1:]) for c in acting}) == len(acting), invariants=collide,
                rel_is_mu=all((c[0] == 2) == (c[VARS.index("mu") + 1] != 0) for c in acting),
                run=cy.run(ix, "1173", dict(OPTS)), audit=ia.audit_index(coords, held))


# ================================================================================ compute, report
def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "bd_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "bd_ia")
    c = constants()
    b = bounds(c)
    closers = closes_open_direction(b)
    return dict(c=c, b=b, ids=identities(b), cap=capacity_vs_top(c), closers=closers, cap_id=capacity_identity(),
                finite={"none": finite_with([], b), "gravity floor": finite_with(["survive: gravity, below"], b),
                        "dark-energy ceiling": finite_with(["survive: dark energy, above"], b),
                        "one coupling, no field": finite_with(["one coupling, above", "one coupling, below"], b, field=0)},
                rel=relations(b), mvg=matter_vs_gravity(), cy=cypher_index(cy, ia, b))


def report(o):
    c = o["c"]
    print("bounds.py -- the bounds in three kinds, and how they interact (item 241)\n")
    print("constants: W %.3f, log2 N_max0 %.3f, positivity %.3f, throat regime %.3f, example README n %.3f" % (
        c["W"], c["lognmax0"], c["c_pos"], c["c_reg"], c["n_ex"]))
    print("\nB1 the bounds (kind; source; slack):")
    for n, (k, s, coef, note) in o["b"].items():
        print("  %-38s %-10s %-26s %s %s" % (n, k, s, {v: str(a) if not isinstance(a, float) else "%.3f" % a for v, a in coef.items()},
                                             note))
    print("  not run / withdrawn: %s" % NOT_RUN)
    print("\nB2 identified exactly (bound = la x A + lb x B, residual constant):")
    for cname, a, d, la, lb, r in o["ids"]:
        print("  %s = %s x [%s] + %s x [%s], residual %.4g" % (cname, la, a, lb, d, float(r)))
    print("  capacity follows from the top while z + n <= %.3f + w (the example sits %.3f inside)" % (
        o["cap"]["margin0"], o["cap"]["at_example"]))
    print("\nB3 bounds closing the open direction (j -> -inf): %s" % o["closers"])
    print("   region finite with (top, relative floor) plus: %s" % o["finite"])
    print("\nB4 by variable -- bounds that mitigate one another / trade:")
    by_v = {}
    for (a, d), rs in o["rel"].items():
        for v, kind in rs:
            by_v.setdefault((v, kind), []).append((a, d))
    for (v, kind), pairs in sorted(by_v.items()):
        print("  %-5s %-9s %d pairs, e.g. %s" % (v, kind, len(pairs), pairs[:2]))
    print("\nB5 a 1e22 kg body's surface gravity at our G under the law, against ours: %s" % {
        el: {l: "%.4f" % v for l, v in d.items()} for el, d in o["mvg"].items()})
    y = o["cy"]
    print("\nB6 the cypher: %d cells; adds nothing %s; keys %s; kind determined by the signs: %s (acting bounds only: %s; "
          "invariants %s; relativity = the mu-relaxed bounds: %s); audit %s" % (
              y["n"], y["adds_nothing"], y["keys"], y["kind_determined"], y["kind_determined_acting"], y["invariants"],
              y["rel_is_mu"], y["audit"]))
    print("   capacity identity N_max/N over (4/3)(sigma/2 dsigma)(rho_E/2 sigma) at three points: %s" % [
        "%.15f" % x for x in o["cap_id"]])
    print("   roster 1173: %s" % "; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"]) for v in y["run"]["verdicts"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("B0 M's item-241 words verbatim in the rulings file", M241 in rul)
    b = o["b"]
    kinds = {k: sum(1 for v in b.values() if v[0] == k) for k in KINDS}
    add("B1 nineteen bounds entered -- universal %d, structural %d, relativity %d -- and two not run or withdrawn"
        % (kinds["universal"], kinds["structural"], kinds["relativity"]),
        len(b) == 19 and kinds == {"universal": 7, "structural": 5, "relativity": 7} and len(NOT_RUN) == 2)
    ids = {(cn, a, d) for cn, a, d, la, lb, r in o["ids"]}
    ok = ("G ceiling", "top (corridor inside the curvature)", "table-top floor (relative)") in ids
    g = [r for cn, a, d, la, lb, r in o["ids"] if cn == "G ceiling" and a == "top (corridor inside the curvature)"]
    ok &= bool(g) and g[0] == 0
    ok &= "%.2f" % o["cap"]["margin0"] == "209.06" and "%.2f" % o["cap"]["at_example"] == "157.78"
    cid = [r for cn, a, d, la, lb, r in o["ids"] if cn == "README capacity"]
    ok &= bool(cid) and abs(float(cid[0]) - math.log2(4 / 3)) < 1e-9 and all(abs(x - 1) < 1e-12 for x in o["cap_id"])
    add("B2 the G ceiling is exactly the top plus the relative floor (residual 0); the capacity is positivity plus the "
        "throat regime plus log2(4/3) (N_max/N = (4/3)(sigma/2 delta sigma)(rho_E/2 sigma), to 1e-12 at three points); "
        "the capacity follows from the top while z + n <= 209.06 + w (the example 157.78 inside)", ok)
    ok = o["closers"] == ["one coupling, below", "survive: closing energy", "survive: dark energy, above",
                          "survive: gravity, below"]
    f = o["finite"]
    ok &= not f["none"] and f["gravity floor"] and not f["dark-energy ceiling"] and f["one coupling, no field"]
    ok &= all(o["b"][n][0] != "structural" for n in o["closers"])
    add("B3 no structural bound closes the open direction; four do (the gravity floor, the closing-energy tolerance, the "
        "dark-energy ceiling, one coupling without a field); the gravity floor and one coupling make the region finite, "
        "the dark-energy ceiling leaves the diagonal open", ok)
    rel = o["rel"]
    z_mit = [p for p, rs in rel.items() if ("z", "mitigates") in rs]
    ok = ("README capacity", "plane positivity") in z_mit and ("README capacity", "survive: dark energy, above") in z_mit
    ok &= ("top (corridor inside the curvature)", "table-top floor (relative)") in [p for p, rs in rel.items()
                                                                                    if ("w", "trades") in rs]
    ok &= all(b[a][0] == "relativity" and b[d][0] == "relativity" for (a, d), rs in rel.items() if ("mu", "mitigates") in rs)
    add("B4 the offset's ratio relaxes capacity, positivity and the dark-energy ceiling together; our tension's place "
        "trades the top against the floor; the object's means relax only relativity bounds", ok)
    m = o["mvg"]
    ok = all(m[el][l] > 1 for el in ("Cu", "Ag", "Au") for l in ("min", "mirror")) and all(m["Cr"][l] < 1 for l in ("min", "mirror"))
    add("B5 the matter law tightens the gravity tolerance for Cu, Ag, Au (surface gravity up) and relaxes it for Cr (down)",
        ok)
    y = o["cy"]
    ok = bool(y["run"]["verdicts"]) and y["n"] == 17 and not y["audit"]["keys"] and not y["audit"]["onehot"]
    ok &= not y["kind_determined"] and y["kind_determined_acting"] and y["rel_is_mu"]
    ok &= y["invariants"] == ["README match", "null energy per ray", "shared SI"]
    add("B6 the cypher (17 cells, no key, no one-hot): the kinds are not contradicted by how the bounds act (bar the three "
        "invariants, which act on no variable); a test any labelling of distinct rows would pass -- it fails to refute "
        "the kinds, it does not confirm them", ok)
    return res


MUTANTS = {"floor_sign": "the relative floor's j-sign reversed"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-12s %-50s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
