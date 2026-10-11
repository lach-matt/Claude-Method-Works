#!/usr/bin/env python3
"""weight_cypher.py -- item 234: is the 5D bulk's ensemble weighted?  If it is, what supplies G, and how?  M: "put this to
the cypher, and if the answer is that the ensemble IS weighted, then ask the cypher what is supplying G and How".
Worked in the conversation (computed, exact where marked; deduced where marked; not verified by a separate session; not
seated); 2026-10-11.

The decision rule, fixed before the run (W0): the ensemble is WEIGHTED if (i) no unweighted ensemble is a probability over
the plausible bulk of item 233, and (ii) the target cell -- a normalisable measure, positive on every plausible universe --
is held by some candidate measure the record computes and not by the unweighted one.  Otherwise UNWEIGHTED, and the
second question is not asked.

  V0 (read) M's item-234 words, verbatim in the rulings file.
  V1 (computed, exact) Every candidate measure the record computes per universe -- each quantity of bulk5_index's K1
     and its inverse, the theorem's window share (K4), and the unweighted count -- as 2^(a i + b j) over the lattice of
     2b and 2P steps.  Summed over the plausible bulk it is finite exactly when b > 0 and a + b > 0 (relative floor) or
     b > 0 and a > 0 (absolute floor); confirmed by log-sums over growing sections.  The unweighted count, the window
     share, the README's capacity, its energy, the curvature radius and Lambda are not normalisable.  Every
     normalisable candidate rises with G in both lattice directions: G itself (alpha_G, the bit area), the corridor's
     mass (= 1/E1), and the 5D coupling's forms (kappa5^4, G5, l5); 1/sigma normalises under the relative floor only.
     The criterion is exact for every weight that is a power of the record's quantities (2^(a i + b j)), listed or not.
     A weight peaked at some universe (not a power) also normalises, but only with a width the record does not give: a
     broad coefficient (209), so not a candidate here.
  V2 (computed; the statistics language, register 1174: maximum entropy on the order-2 marginals) (a) With only the
     plausible bulk held, the maximum-entropy ensemble is uniform on what is held; on sections of growing size position
     1's share is 1/|section| and goes to 0: the unweighted ensemble gives our own universe no weight.  (b) With the
     positions held, the support is the seven position universes (E = 0, as bulk5_index K5), the five plausible
     compositions weigh 0: over the plausible box the ensemble is not uniform.
  V3 (computed; the cypher, roster 1173, audited) The candidate measures as cells over (rises along 2b, rises along 2P,
     normalisable relative, normalisable absolute).  The target (normalisable under both readings) is held by the
     candidates that rise along both directions, never by the unweighted one.  By W0: WEIGHTED.
  V4 (computed, exact) What supplies G.  As functions of G, the tension and the offset (the offset kept free -- the axis
     bulk5_index K7 found unseen), a set of the universe's quantities determines G when G's log-gradient lies in the
     span of theirs (exact Fractions, at our own offset ratio).  The plane alone (tension, offset) never determines G;
     the bulk alone (coupling, curvature) never does while the offset is not zero.  Every minimal set made only of the
     5D action's and the plane's own parameters holds one of each: {coupling, tension}, {curvature, tension, offset},
     {coupling, curvature, offset}.  With the offset exactly 0 (a flat plane), {coupling, curvature} also does.  The
     README's quantities (its energy, its mass, its capacity, the bit area) determine G alone, because each is G
     written with the shared SI constants -- G's equivalents, not suppliers.
  V5 (computed; the cypher, audited) The minimal determining sets as cells over (has a bulk parameter, has a plane
     parameter, has one of G's equivalents).  The target -- G fixed with a bulk parameter and no equivalent of G inside
     -- is held by exactly the three sets of V4, every one with a plane parameter.  The cypher finds G fixed by the bulk
     and the plane together; "supplies" is the direction the record gives -- the bulk does all the work (230), the
     bulk is the third body (232), and 4D gravity is the 5D gravity reduced onto the plane -- not one the cypher
     decides.
  V6 (computed, exact on every universe; READ) How: G = kappa5^4 sigma c^4 / (48 pi) -- the bulk's coupling carried onto
     the plane by its tension (Shiromizu-Maeda-Sasaki's relation, the one p2_gravity's sector already uses), exact for
     every offset; equivalently G = 3 c^4 / (4 pi ell^2 (sigma - 2 delta sigma)).  On the positions: 2b's G x 2 is the
     coupling x 2 at our tension; 2P's is the coupling x 8 against a tension x 1/4.  In a bulk of one coupling (no field,
     K6) G is proportional to each plane's tension alone.
  V7 (deduced from V1, V6) Among the record's powers, a normalisable weight rises with G in both directions, and
     G = kappa5^4 sigma / 48 pi, so such a weight rises with the bulk's coupling read through the plane's tension.  Which such
     weight the ensemble carries is not fixed by the record (several candidates normalise); that is the measure item
     233 found missing, now narrowed.

What this does not show.
  - The verdict rests on K3's open direction: the theorem's conditions leave weak gravity unbounded.  A condition that
    bounded it would make the unweighted count finite, and W0 would have to be run again.
  - The candidate list is every quantity bulk5_index K1 computes and its inverse, not every function of a universe.
  - V4's determination is local (the implicit function theorem); every relation here is a monomial or a monomial in
    (sigma - 2 delta sigma), so it is also global on the positive quadrant.
  - The bulk/plane/equivalent classes are the 5D action's (kappa5, Lambda5), the plane's (sigma, delta sigma), and
    quantities defined from G with the shared SI constants; the classification is READ from the braneworld setting,
    not computed.

Imports bulk5_index.py (and through it p2_planck.py), tools/cypher.py and index_audit.py by path.  Stdlib.
python3 weight_cypher.py [--selftest | --mutants]
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
M234 = ("put this to the cypher, and if the answer is that the ensemble IS weighted, then ask the cypher what is supplying "
        "G and How")
LANGS = ("order", "algebra", "geometry", "information", "statistics")
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}


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


B5 = _load(os.path.join(HERE, "bulk5_index.py"), "wc_b5")
PP = B5.PP


# ===================================================================================== V1 the candidate measures
def ij_exponents(e_gs):
    """a quantity's exponent of 2 as a function of (g, s) -> its (a, b) in (i, j): g = i + j, s = -2j"""
    dg, ds = e_gs
    return (F(dg), F(dg) - 2 * F(ds))


def quantity_gs():
    """each K1 quantity's exponent as (d/dg, d/ds), read off bulk5_index.exps at three points"""
    e00, e10, e01 = B5.exps(1, F(1)), B5.exps(2, F(1)), B5.exps(1, F(2))
    return {k: (e10[k] - e00[k], e01[k] - e00[k]) for k in e00}


def candidates():
    """every K1 quantity and its inverse, duplicates (same (a, b)) named together; the unweighted count"""
    out = {}
    for k, gs in quantity_gs().items():
        if k == "ell2":                                          # the radius itself, not its square
            k, gs = "ell", (gs[0] / 2, gs[1] / 2)
        a, b = ij_exponents(gs)
        for name, ab in ((k, (a, b)), ("1/" + k, (-a, -b))):
            if ab == (0, 0):
                continue
            out.setdefault(ab, []).append(name)
    out.setdefault((F(0), F(0)), []).append("unweighted")
    if MUT.get("drop_unweighted"):
        out[(F(0), F(0))].remove("unweighted")
    return out


def normalisable(ab, floor):
    a, b = ab
    if MUT.get("norm_wrong"):
        return b > 0
    return (b > 0 and a + b > 0) if floor == "rel" else (b > 0 and a > 0)


def log2_partial_sum(ab, k, floor, n):
    """log2 of the sum of 2^(a i + b j) x window share over the plausible universes with i, j >= -n -- the region's
    whole upper part always included (i <= W/2, j <= W), only the open directions cut"""
    a, b = float(ab[0]), float(ab[1])
    terms = []
    for i in range(-n, int(k["W"] // 2) + 2):
        for j in range(-n, int(k["W"]) + 2):
            w = B5.weight(i, j, k, floor)
            if w > 0:
                terms.append(a * i + b * j + math.log2(w))
    m = max(terms)
    return m + math.log2(sum(2 ** (t - m) for t in terms))


def v1():
    k = B5.constants()
    cand = candidates()
    rows = {}
    for ab, names in cand.items():
        num = {f: [log2_partial_sum(ab, k, f, n) for n in (60, 120, 240)] for f in ("rel", "abs")}
        conv = {f: num[f][2] - num[f][1] < 0.01 for f in ("rel", "abs")}       # a divergent sum gains >= ~1 bit
        rows[ab] = dict(names=sorted(names), rel=normalisable(ab, "rel"), abs=normalisable(ab, "abs"), num=num, conv=conv)
    return rows


# ========================================================================= V2 the statistics language's own weights
def ipf(held, box, pairs, sweeps=2000):
    """maximum entropy on the order-2 marginals of the uniform distribution over held cells (IPF from uniform on the box);
    op_statistics returns this distribution's support, and this its weights"""
    target = {}
    for S in pairs:
        cnt = {}
        for c in held:
            key = tuple(c[x] for x in S)
            cnt[key] = cnt.get(key, 0) + F(1, len(held))
        target[S] = cnt
    p = {c: 1.0 / len(box) for c in box}
    for _ in range(sweeps):
        for S in pairs:
            marg = {}
            for c, v in p.items():
                key = tuple(c[x] for x in S)
                marg[key] = marg.get(key, 0.0) + v
            for c in p:
                key = tuple(c[x] for x in S)
                t = float(target[S].get(key, 0))
                p[c] = 0.0 if t == 0 else p[c] * t / marg[key]
    return p


def v2(cy):
    k = B5.constants()
    sections = {}
    for n in (5, 10, 20):
        cells = [(i, j, law) for i in range(-n, n + 1) for j in range(-n, n + 1) for law in range(3)
                 if B5.w_interval(i, j, k, "rel")]
        ix = cy.Index("bulk_section", ["i", "j", "law"], [list(c) for c in cells])
        adm, _ = cy.ADMISSION["statistics"][0](ix, dict(OPTS))
        sections[n] = dict(n_cells=len(cells), stat_E=len(adm) - len(ix.cells), ours=1.0 / len(cells))
    # the positions held, 201's basis, each axis ordered away from ours (bulk5_index K5)
    fd = B5.five_d()
    f = lambda n: (B5.LAW_ORDER.index(fd[n]["law"]), int(fd[n]["e"]["sigma"]), int(fd[n]["e"]["sigma_planck"]))
    held = sorted({f(n) for n in B5.POSITIONS})
    box = sorted({(a, s, p) for a in range(3) for s in (0, -2) for p in (0, 2)})
    p = ipf(held, box, list(itertools.combinations(range(3), 2)))
    comp = {n: p[f(n)] for n in PP.MEMBERS}
    return dict(sections=sections, held=held, weights=comp,
                support=sorted(n for n, v in comp.items() if v > 1e-12),
                uniform_on_support=max(v for v in comp.values() if v > 1e-12) - min(v for v in comp.values() if v > 1e-12))


# ========================================================================================= V3 the decision index
def v3(cy, ia, rows):
    sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)
    cells = {}
    for ab, r in rows.items():
        cell = (sign(ab[0]), sign(ab[1]), int(r["rel"]), int(r["abs"]))
        cells.setdefault(cell, []).extend(r["names"])
    coords = ["rises_2b", "rises_2P", "norm_rel", "norm_abs"]
    held = sorted(cells)
    ix = cy.Index("weight_measures", coords, [list(c) for c in held],
                  value_order={"rises_2b": [-1, 0, 1], "rises_2P": [-1, 0, 1], "norm_rel": [0, 1], "norm_abs": [0, 1]})
    holders = sorted(n for c, ns in cells.items() if c[2] == 1 and c[3] == 1 for n in ns)
    unweighted_cell = next(c for c, ns in cells.items() if "unweighted" in ns) if any(
        "unweighted" in ns for ns in cells.values()) else None
    target_cells = [c for c in held if c[2] == 1 and c[3] == 1]
    return dict(cells=cells, holders=holders, target_cells=target_cells, unweighted_cell=unweighted_cell,
                run=cy.run(ix, "1173", dict(OPTS)), audit=ia.audit_index(coords, held))


def decide(rows, sec, d3):
    no_unweighted_probability = (not rows[(F(0), F(0))]["rel"]) and (not rows[(F(0), F(0))]["abs"])
    no_unweighted_probability &= sec[20]["ours"] < sec[10]["ours"] < sec[5]["ours"]
    target_by_weighted = bool(d3["holders"]) and "unweighted" not in d3["holders"]
    return "WEIGHTED" if (no_unweighted_probability and target_by_weighted) else "UNWEIGHTED"


# ======================================================================================= V4 what determines G
CLASSES = {"kappa5^4": "bulk", "G5": "bulk", "l5": "bulk", "ell": "bulk", "Lambda5": "bulk",
           "sigma": "plane", "delta_sigma": "plane",
           "sigma/sigma_P": "equiv", "N_max": "equiv", "E1": "equiv", "m1": "equiv", "A_bit": "equiv", "Lambda4": "equiv",
           "matter_law": "matter"}


def gradients(r):
    """d log Q / d (log G, log sigma, log delta_sigma) at offset ratio r = delta_sigma / sigma (exact Fractions)"""
    q = F(1) / (1 - 2 * r)
    g = {"kappa5^4": (1, -1, 0), "G5": (F(1, 2), F(-1, 2), 0), "l5": (F(1, 6), F(-1, 6), 0),
         "ell": (F(-1, 2), -q / 2, r * q), "Lambda5": (1, q, -2 * r * q),
         "sigma": (0, 1, 0), "delta_sigma": (0, 0, 1),
         "sigma/sigma_P": (2, 1, 0), "N_max": (-2, 0, -1), "E1": (F(-1, 2), 0, 0), "m1": (F(1, 2), 0, 0),
         "A_bit": (1, 0, 0), "Lambda4": (1, 0, 1), "matter_law": (0, 0, 0)}
    if MUT.get("sms_wrong"):
        g["kappa5^4"] = (1, 1, 0)
    return {k: tuple(F(x) for x in v) for k, v in g.items()}


def rank(rows):
    m = [list(r) for r in rows]
    rk, col = 0, 0
    nrows = len(m)
    ncols = len(m[0]) if m else 0
    for col in range(ncols):
        piv = next((x for x in range(rk, nrows) if m[x][col] != 0), None)
        if piv is None:
            continue
        m[rk], m[piv] = m[piv], m[rk]
        for x in range(nrows):
            if x != rk and m[x][col] != 0:
                fct = m[x][col] / m[rk][col]
                m[x] = [a - fct * b for a, b in zip(m[x], m[rk])]
        rk += 1
    return rk


def determines(names, grads):
    rows = [grads[n] for n in names]
    if not rows:
        return False
    return rank(rows + [(F(1), F(0), F(0))]) == rank(rows)


def v4():
    k = B5.constants()
    r_ours = F(PP.PG.DSIG) / F(k["S0"])
    out = {}
    for label, r in (("ours", r_ours), ("generic", F(1, 7)), ("flat", F(0))):
        grads = gradients(r)
        names = sorted(CLASSES)
        minimal = []
        for size in (1, 2, 3):
            for S in itertools.combinations(names, size):
                if determines(S, grads) and not any(set(m) <= set(S) for m in minimal):
                    minimal.append(S)
        out[label] = dict(r=r, minimal=minimal,
                          plane_alone=any(determines(S, grads) for z in (1, 2)
                                          for S in itertools.combinations(["sigma", "delta_sigma"], z)),
                          bulk_alone=any(determines(S, grads) for z in (1, 2, 3)
                                         for S in itertools.combinations(["kappa5^4", "G5", "l5", "ell", "Lambda5"], z)))
    return out


def primitive_minimal(minimal):
    """the minimal determining sets made only of bulk and plane parameters, by class"""
    sets = []
    for S in minimal:
        cl = [CLASSES[n] for n in S]
        if all(c in ("bulk", "plane") for c in cl):
            sets.append(S)
    return sets


def class_pattern(S):
    """a set's classes, the bulk's coupling forms (kappa5^4, G5, l5) as one parameter, its curvature forms (ell,
    Lambda5) as another"""
    pat = set()
    for n in S:
        pat.add({"kappa5^4": "coupling", "G5": "coupling", "l5": "coupling", "ell": "curvature",
                 "Lambda5": "curvature", "sigma": "tension", "delta_sigma": "offset"}.get(n, n))
    return tuple(sorted(pat))


# =========================================================================================== V5 the supplier index
def v5(cy, ia, minimal):
    cells = {}
    for S in minimal:
        cl = [CLASSES[n] for n in S]
        cell = (int("bulk" in cl), int("plane" in cl), int("equiv" in cl), len(S))
        cells.setdefault(cell, []).append(S)
    coords = ["has_bulk", "has_plane", "has_equiv", "size"]
    held = sorted(cells)
    ix = cy.Index("g_suppliers", coords, [list(c) for c in held])
    holders = sorted(class_pattern(S) for c, Ss in cells.items() if c[0] == 1 and c[2] == 0 for S in Ss)
    return dict(cells=cells, holders=sorted(set(holders)), all_plane=all(c[1] == 1 for c in cells if c[0] == 1 and c[2] == 0),
                run=cy.run(ix, "1173", dict(OPTS)), audit=ia.audit_index(coords, held))


# ========================================================================================== V6 how, on every universe
def v6():
    """G = kappa5^4 sigma c^4 / (48 pi) and G = 3 c^4 / (4 pi ell^2 (sigma - 2 delta sigma)) on the twelve members,
    numerically against p2_planck.sector, and exactly in exponents (g = (g - s) + s)"""
    c4 = PP.PG.C ** 4
    rows = {}
    for name, (law, gf, sf) in PP.MEMBERS.items():
        sec = PP.sector(gf, sf)
        sms = sec["k4"] * sec["sigma"] * c4 / (48 * math.pi)
        curv = 3 * c4 / (4 * math.pi * sec["ell"] ** 2 * (sec["sigma"] - 2 * sec["offset"]))
        e = B5.exps(gf, sf)
        rows[name] = dict(sms=abs(sms / sec["G"] - 1), curv=abs(curv / sec["G"] - 1), exact=e["G"] == e["k4"] + e["sigma"],
                          k4=e["k4"], sigma=e["sigma"])
    return rows


# ================================================================================================= compute, report
def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "wc_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "wc_ia")
    rows = v1()
    sec = v2(cy)
    d3 = v3(cy, ia, rows)
    verdict = decide(rows, sec["sections"], d3)
    out = dict(rows=rows, v2=sec, v3=d3, verdict=verdict)
    if verdict == "WEIGHTED" or MUT.get("ask_anyway"):
        d4 = v4()
        out.update(v4=d4, v5=v5(cy, ia, d4["ours"]["minimal"]), v6=v6())
    return out


def report(o):
    print("weight_cypher.py -- is the 5D bulk's ensemble weighted?  If so, what supplies G, and how (item 234)\n")
    print("V1 candidate measures 2^(a i + b j): normalisable (relative, absolute); log2 partial sums at n = 60, 120, 240")
    for ab, r in sorted(o["rows"].items(), key=lambda kv: (-(kv[1]["rel"] + kv[1]["abs"]), kv[0])):
        print("  (a, b) = (%5s, %5s)  rel %-5s abs %-5s  %s   rel %s" % (str(ab[0]), str(ab[1]), r["rel"], r["abs"],
              ", ".join(r["names"]), ["%.3f" % x for x in r["num"]["rel"]]))
    s = o["v2"]
    print("\nV2 (a) the plausible bulk alone, statistics' maximum entropy is uniform: %s" % {
        n: "%d cells, statistics E %d, position 1's share %.3e" % (v["n_cells"], v["stat_E"], v["ours"]) for n, v in s["sections"].items()})
    print("   (b) the positions held: support %s; weights %s" % (s["support"], {n: "%.4f" % v for n, v in s["weights"].items()}))
    d3 = o["v3"]
    print("\nV3 the decision index: target held by %s; the unweighted cell %s" % (d3["holders"], d3["unweighted_cell"]))
    print("   roster 1173: %s; audit %s" % ("; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"])
                                                    for v in d3["run"]["verdicts"]), d3["audit"]))
    print("\nVERDICT (W0's rule): %s" % o["verdict"])
    if "v4" in o:
        for lbl, d in o["v4"].items():
            print("\nV4 at offset ratio %s (%s): plane alone determines G %s; bulk alone %s" % (
                "%.3e" % float(d["r"]), lbl, d["plane_alone"], d["bulk_alone"]))
            print("   minimal sets of bulk and plane parameters: %s" % sorted({class_pattern(S) for S in primitive_minimal(d["minimal"])}))
            print("   minimal sets with one of G's equivalents: %s" % [S for S in d["minimal"] if any(CLASSES[n] == "equiv" for n in S)][:12])
        d5 = o["v5"]
        print("\nV5 the supplier index: target (a bulk parameter, no equivalent of G) held by %s; all of them with a plane "
              "parameter: %s" % (d5["holders"], d5["all_plane"]))
        print("   roster 1173: %s; audit %s" % ("; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"])
                                                        for v in d5["run"]["verdicts"]), d5["audit"]))
        print("\nV6 G = kappa5^4 sigma c^4/(48 pi), G = 3 c^4/(4 pi ell^2 (sigma - 2 delta sigma)) on the twelve:")
        for n, r in o["v6"].items():
            print("  %-13s kappa5^4 x 2^%s, sigma x 2^%s; SMS %.1e, curvature %.1e, exact %s" % (
                n, r["k4"], r["sigma"], r["sms"], r["curv"], r["exact"]))


# ================================================================================================== checks
def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("V0 M's item-234 words verbatim in the rulings file", M234 in rul)
    rows = o["rows"]
    norm = sorted(n for r in rows.values() if r["rel"] and r["abs"] for n in r["names"])
    ok = all(r["conv"]["rel"] == r["rel"] and r["conv"]["abs"] == r["abs"] for r in rows.values())
    ok &= not rows[(F(0), F(0))]["rel"] and not rows[(F(0), F(0))]["abs"]
    ok &= norm == sorted(["G", "k4", "G5", "l5", "m1", "1/E1"])
    ok &= all(ab[0] > 0 and ab[1] > 0 for ab, r in rows.items() if r["rel"] and r["abs"])
    nn = {n for r in rows.values() if not r["rel"] and not r["abs"] for n in r["names"]}
    ok &= {"unweighted", "N_max", "E1", "L5", "sigma_planck"} <= nn
    add("V1 the normalisable candidates (both floors) are exactly G, kappa5^4, G5, l5 and m1 (= 1/E1) -- all rising with G in both "
        "directions; the unweighted count, the capacity, the README's energy, Lambda5 and the Planck tension are not; the "
        "log-sums agree with the criterion on every candidate", ok)
    s = o["v2"]
    sec = s["sections"]
    ok = all(v["stat_E"] == 0 for v in sec.values()) and sec[20]["ours"] < sec[10]["ours"] < sec[5]["ours"]
    ok &= s["support"] == sorted(B5.POSITIONS) and s["uniform_on_support"] < 1e-9
    ok &= all(abs(s["weights"][n] - 1 / 7) < 1e-9 for n in B5.POSITIONS)
    add("V2 statistics: with the plausible bulk alone held its maximum entropy is uniform on what is held, position 1's "
        "share falling with the section (to 0); with the positions held the support is the seven, each 1/7, the five "
        "plausible compositions 0", ok)
    d3 = o["v3"]
    ok = d3["holders"] == sorted(["G", "k4", "G5", "l5", "m1", "1/E1"]) and d3["unweighted_cell"] not in d3["target_cells"]
    ok &= all(c[0] == 1 and c[1] == 1 for c in d3["target_cells"]) and bool(d3["run"]["verdicts"])
    ok &= not d3["audit"]["keys"]
    add("V3 the decision index (run and audited, no key): the target is held only by candidates rising along both 2b and "
        "2P, never by the unweighted count", ok)
    add("W0 the verdict by the rule fixed before the run: WEIGHTED", o["verdict"] == "WEIGHTED")
    if "v4" not in o:
        return res
    d4 = o["v4"]
    pats = {lbl: sorted({class_pattern(S) for S in primitive_minimal(d["minimal"])}) for lbl, d in d4.items()}
    ok = not d4["ours"]["plane_alone"] and not d4["ours"]["bulk_alone"] and not d4["generic"]["bulk_alone"]
    ok &= pats["ours"] == pats["generic"] == [("coupling", "curvature", "offset"), ("coupling", "tension"),
                                              ("curvature", "offset", "tension")]
    ok &= d4["flat"]["bulk_alone"] and ("coupling", "curvature") in pats["flat"]
    eq1 = sorted(S[0] for S in d4["ours"]["minimal"] if len(S) == 1)
    ok &= eq1 == ["A_bit", "E1", "m1"]
    add("V4 what determines G (exact, the offset free): neither the plane alone nor the bulk alone; every minimal set of "
        "bulk and plane parameters holds one of each -- {coupling, tension}, {curvature, tension, offset}, {coupling, "
        "curvature, offset}; with the offset exactly 0 {coupling, curvature} too; alone, only G's equivalents (A_bit, "
        "E1, m1)", ok)
    d5 = o["v5"]
    ok = d5["all_plane"] and d5["holders"] == pats["ours"] and bool(d5["run"]["verdicts"])
    add("V5 the supplier index (run and audited): the target -- a bulk parameter, no equivalent of G -- is held by exactly "
        "V4's three sets, each with a plane parameter: G is fixed by the bulk and the plane together", ok)
    v = o["v6"]
    ok = all(r["sms"] < 1e-12 and r["curv"] < 1e-9 and r["exact"] for r in v.values())
    ok &= (v["2b"]["k4"], v["2b"]["sigma"], v["2P"]["k4"], v["2P"]["sigma"]) == (1, 0, 3, -2)
    add("V6 how: G = kappa5^4 sigma c^4 / (48 pi) on all twelve to 1e-12 (exact in exponents), and G = 3 c^4 / (4 pi ell^2 "
        "(sigma - 2 delta sigma)); 2b is the coupling x 2 at our tension, 2P the coupling x 8 against a tension x 1/4", ok)
    return res


MUTANTS = {"norm_wrong": "normalisability read from b > 0 alone",
           "drop_unweighted": "the unweighted count left out of the candidates",
           "sms_wrong": "the coupling's gradient taken as G sigma (SMS misread)",
           "ask_anyway": "the second question asked regardless of the verdict (must not change any check)"}


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
        if kk == "ask_anyway":
            ok = not failed
            caught += ok
            print("  control %-15s %-60s %s" % (kk, desc, "no check moved" if ok else "MOVED " + ", ".join(failed)))
            continue
        caught += bool(failed)
        print("  mutant %-16s %-60s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught (the control counts when nothing moves)" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
