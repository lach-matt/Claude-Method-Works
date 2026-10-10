#!/usr/bin/env python3
"""ring_cypher.py -- the ring's nature, put to the cypher (item 207: "Ask the cypher").  Pass 3 of the cycle (items
204-207); computed, deduced and READ as labelled; not verified by a separate session; not seated; 2026-10-10.

m1_cypher.py found M1 within one universe met on every clause but (d), no added matter: the rim balances only with a
ring of positive tension lambda = a sigma (1 - cos theta)(1 + 2 cos theta), 0.013-0.10 a sigma over rim_profile's
family (P5).  The board read that tension as the fold's own, part of the plane's structure (H-RING-IS-THE-FOLD, after
202); M answered the question with "Ask the cypher" (207).

  R1 (computed, by import of rim_profile.py) the ring's attributes: positive over the whole family; it vanishes with
     the fold (lambda -> 0 as theta -> 0: it exists only with the corridor); its only other zero is theta = 120 deg,
     the Plateau angle at which three equal tensions balance with no ring; the family meets the plane at 5-16 deg; its
     tension is SOLVED from the rim's balance (forming_rim F3b), not fixed by any constant; the board models it as a
     ring of energy density equal to its tension (pure tension along it, P5's reading)
  R2 (computed, sympy) a thin pure-tension sheet carries NO line tension at a fold: its stress sigma h_ab is supported
     on the sheet with bounded density, so across a band of width w about the fold line it integrates to O(w) -> 0;
     rounding a fold of turning angle theta at radius w changes the line energy by sigma w (theta - 2 tan(theta/2)),
     which is negative on (0, pi) and vanishes as w -> 0.  The plane as the board models it (201: a tension and an
     offset, both pure tension, thin) gives its own fold zero line tension, never the ring's positive one.  So the
     reading's identification of the ring with the fold is refuted in the thin-plane model
  R3 (READ, read 2026-10-10 through alphaXiv) the junctions physics records.  Csaki and Shirman, "Brane junctions in
     the Randall-Sundrum scenario" (hep-th/9908186): a static junction of branes exists "only if the mechanical forces
     acting on the junction exactly cancel", sum V_i n_i = 0 (their (3.10)), with no junction tension; a tension on the
     intersection is a separate parameter ("the tension of the 3-brane at the intersection (a quantity which we did
     not consider ...)"), on which fields may be localised.  Carroll, Hellerman and Trodden, "Domain wall junctions are
     1/4-BPS states" (hep-th/9905217): "not only do the 'spokes' of the junction have a tension associated with them,
     but the 'hub' has its own non-vanishing contribution to the total energy", the junction mass "proportional to
     the area in field space" -- the walls' own field fixes it, beyond the walls' tension.  In both the junction is
     straight and the walls' angles cancel the force by themselves; neither records a junction tension solved from a
     balance
  R4 (cypher, index A: carriers whose nature M has ruled) cells over (support, with_corridor, pure_tension, fixed_by,
     matter): 129's matter, 201-202's tension and offset (not matter: Shiromizu-Maeda-Sasaki's split T = -sigma g +
     tau, READ, and the board's note under 130 that tau = 0 on eq. (17)), the fold (that tension where the corridor
     bends the plane), 130's mouth ("a black hole is not matter"), the corridor (129/130: the bridge adds no matter;
     H-BRIDGE-ADDS-NO-MATTER), and the ring with its matter unknown.  On the ring as computed (a line, tension solved
     from the balance) geometry, information and statistics REFUSE under every coding (order and algebra fall every
     way across codings, an artefact): no ruled carrier is a line, and none has a tension solved from a balance --
     statistics blocked at orders 2-4, for 'not matter' by (support, matter) and (fixed_by, matter)
  R5 (cypher) on the reading's description (the ring entered as the fold: a sheet, tension fixed by sigma) statistics
     decides 'not matter' at orders 2-4 and no language admits 'matter' alone -- because that is the fold's own tuple
     (without the fold, order 2 only); R2 shows the fold carries none of the ring's tension, so this decision is the
     reading restated, and its premise refuted
  R6 (cypher, index B: the junctions of R3, the sheets they join, and the ring; target: of the sheets' own structure)
     on the ring as computed statistics refuses at orders 2-4, blocked for 'own structure' by (fixed_by, own) alone;
     entered as a line tension FIXED by the sheets' structure (the hub's case) statistics decides 'own structure' at
     orders 2-4, by Carroll-Hellerman-Trodden's hub alone (without it, refused).  On M's carriers that same entry is
     refused, blocked by (support, matter) alone: no carrier M has ruled is a line.
     That is the decisive cell: whether a plane's structure fixes a tension where it meets another.  201's two numbers
     do not (R2); 202's "the same definitions as we do" carries no third
  R7 control: the ring's nature entered (either way) -- every language admits it, so the refusals are the ring's, not
     the index's
So the cypher does not decide the ring's nature: it refuses it, and names the cell that would decide it.  The board's
reading H-RING-IS-THE-FOLD is refuted as stated (R2), not dropped (206): the thin plane's fold has no tension of its
own.  Clause (d) of M1 within one universe stays OPEN, now on a sharper question -- either the plane has structure
beyond its tension and offset that gives a junction its own tension (a stiffness, or a thickness, as a domain wall's
field gives its hub energy), or the rim closes without a ring (the Plateau angle, 120 deg, which the family's 5-16 deg
does not reach), or the ring is something M's model already holds.
Imports rim_profile.py (and through it corridor_shape.py, forming_rim.py) and tools/cypher.py by path.  Stdlib +
sympy (+ mpmath through corridor_shape).  python3 ring_cypher.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
U = 2
_C = {}


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def cy():
    if "cy" not in _C:
        _C["cy"] = _load(os.path.join(ROOT, "tools", "cypher.py"), "ring_cypher_cy")
    return _C["cy"]


# ================================================================================================ R0 M's words
WORDS = {
    "129": "It contains matter, you, me, this current universe, just not a corridor for transit because the",
    "130": "in my model a black hole is not matter, it is what the mouth at position 1 looks",
    "130i": "1 - i - no added matter.",
    "201": "σ and its dark-energy offset",
    "202": "consider\n    that any plane has its own structure in the same fashions that we do, the same definitions as we do",
    "207": "\"Ask the cypher\"",
}


def words():
    text = open(RULINGS, encoding="utf-8").read()
    w = dict(WORDS)
    if MUT.get("misquote"):
        w["130"] = "in my model a black hole is matter"
    return {k: v in text for k, v in w.items()}


# ======================================================================================= R1 the ring's attributes
def ring_attributes():
    """rim_profile's family at margin 0 (imported, re-run): every member's ring and meeting angle"""
    import sympy as sp
    if "fam" not in _C:
        rp = _load(os.path.join(HERE, "rim_profile.py"), "ring_rim_profile")
        _C["fam"] = rp.family(margins=(0.0,))
    fam = _C["fam"]
    th = sp.symbols("theta", real=True)
    lam = (1 - sp.cos(th)) * (1 + 2 * sp.cos(th))                       # forming_rim F3b, B-images, in units a sigma
    zeros = sorted(float(z) for z in sp.solveset(sp.Eq(lam, 0), th, sp.Interval(0, sp.pi)))
    rings = [v["ring"] for v in fam.values()]
    thetas = [math.degrees(v["theta"]) for v in fam.values()]
    return {"rings": rings, "thetas": thetas, "zeros_deg": [math.degrees(z) for z in zeros],
            "vanishes_with_fold": sp.limit(lam, th, 0) == 0,
            "positive": all(r > 0 for r in rings), "range": (min(rings), max(rings)), "theta_range": (min(thetas), max(thetas))}


# =========================================================================== R2 a thin pure-tension sheet's fold
def fold_line_tension():
    """the line energy of a fold in a thin sheet of pure tension sigma: rounded at radius w with turning angle theta,
    the arc w theta replaces the two straight legs 2 w tan(theta/2); the sheet's stress sigma h_ab has bounded density,
    so its integral over a band of width w about the fold line is at most sigma w"""
    import sympy as sp
    w, th, sg = sp.symbols("w theta sigma", positive=True)
    dE = sg * (w * th - 2 * w * sp.tan(th / 2))                          # change in line energy per unit length
    if MUT.get("fold_tension"):
        dE = dE + sg * sp.Rational(1, 25)                                # a fold given a tension of its own
    band = sg * 2 * w                                                    # |integral of sigma h_ab over the band| <= sigma * 2w
    neg = all(float(dE.subs({sg: 1, w: 1, th: t})) < 0 for t in (0.05, 0.3, 1.0, 2.0, 3.0))
    series = sp.series((th - 2 * sp.tan(th / 2)), th, 0, 5).removeO()
    return {"limit": sp.limit(dE, w, 0), "band_limit": sp.limit(band, w, 0), "negative": neg,
            "series": sp.simplify(series - (-th ** 3 / 12)) == 0}


# ============================================================================================ R4-R7 the cypher
CA = ["support", "with_corridor", "pure_tension", "fixed_by", "matter"]
# support: 0 a sheet or a volume, 1 a line (a junction).  fixed_by: 0 a constant of its own, 1 the plane's
# definition (201: sigma, delta sigma), 2 the README input (131, 203), 3 solved from the rim's balance (F3b)
RULED = {
    "matter (129)": (0, 0, 0, 0, 1),
    "our plane's tension (201, 202; SMS split)": (0, 0, 1, 1, 0),
    "the dark-energy offset (201)": (0, 0, 1, 1, 0),
    "position 2's plane's tension (202)": (0, 0, 1, 1, 0),
    "the fold: our plane's tension where the corridor bends it (202)": (0, 1, 1, 1, 0),
    "the mouth's black hole (130)": (0, 1, 0, 2, 0),
    "the corridor's own stress (129, 130 i, 203; H-BRIDGE-ADDS-NO-MATTER)": (0, 1, 0, 2, 0),
}
RING = {"computed": (1, 1, 1, 3), "reading": (0, 1, 1, 1), "hub": (1, 1, 1, 1)}
# index B: the junctions physics records (R3), the sheets they join, and the ring; target own = of the sheets' structure
CB = ["support", "with_corridor", "pure_tension", "fixed_by", "own"]
READ_B = {
    "a domain wall (CHT 2000)": (0, 0, 1, 1, 1),
    "a Randall-Sundrum brane (CS 1999)": (0, 0, 1, 1, 1),
    "a domain-wall junction's hub (CHT 2000)": (1, 1, 1, 1, 1),
    "the tension of an intersection brane (CS 1999)": (1, 0, 1, 0, 0),
}


def _vo(cells, nominal):
    """value orders: each nominal coordinate under the permutation given; the target with U last"""
    vals = [sorted({c[i] for c in cells}) for i in range(len(cells[0]))]
    return [list(nominal[i]) if i < len(nominal) else vals[i] for i in range(len(vals))]


def admitted(coords, cells, test, lang, k=2, orders=None):
    """the decoded tuples the language admits that pass test (None: silent)"""
    cl = sorted(set(cells))
    vo = {}
    for i, name in enumerate(coords):
        present = sorted({c[i] for c in cl})
        vo[name] = [x for x in (orders[i] if orders else present) if x in present]
    ix = cy().Index("ring", coords, [list(c) for c in cl], value_order=vo)
    out, _ = cy().ADMISSION[lang][0](ix, {"statistics_order": k} if lang == "statistics" else {})
    if out is None:
        return None
    return {h for h in {tuple(ix.decode[i][x[i]] for i in range(len(coords))) for x in out} if test(h)}


def verdict(coords, cells, attrs, lang, k=2, orders=None):
    a = admitted(coords, cells, lambda h: h[:-1] == attrs and h[-1] in (0, 1), lang, k, orders)
    if a is None:
        return "silent"
    d0, d1 = attrs + (0,) in a, attrs + (1,) in a
    return {(True, False): "0", (False, True): "1", (True, True): "both", (False, False): "refused"}[(d0, d1)]


def codings(cells):
    """every value order of every coordinate (the target's 0/1 both ways, U last)"""
    alph = [sorted({c[i] for c in cells}) for i in range(len(cells[0]))]
    per = [list(itertools.permutations(a)) for a in alph[:-1]]
    tgt = [tuple(x for x in o if x in alph[-1]) for o in ((0, 1, U), (1, 0, U))]
    for combo in itertools.product(*per):
        for t in tgt:
            yield list(combo) + [t]


def blocking(cells, target, k):
    cs = list(cells)
    return [tuple(S) for S in itertools.combinations(range(len(target)), k)
            if (len(target) - 1) in S and not any(all(x[i] == target[i] for i in S) for x in cs)]


def index_a(desc):
    cells = list(RULED.values())
    if MUT.get("drop_support"):
        cells = [c[1:] for c in cells]
    attrs = RING[desc] if not MUT.get("ring_as_fold") or desc != "computed" else RING["reading"]
    if MUT.get("drop_support"):
        attrs = attrs[1:]
    seat = MUT.get("seat_ring")
    ring = attrs + ((0 if seat else U),)
    return cells + [ring], attrs


def run_index(coords, cells, attrs, langs=("order", "algebra", "geometry", "information", "statistics")):
    per = {}
    for lg in langs:
        if lg == "statistics":
            per[lg] = {verdict(coords, cells, attrs, lg, 2)}
        else:
            per[lg] = {verdict(coords, cells, attrs, lg, 2, o) for o in codings(cells)}
    stat = {k: verdict(coords, cells, attrs, "statistics", k) for k in range(2, len(coords))}
    return {"per": per, "stat_by_order": stat,
            "block0": blocking(cells, attrs + (0,), 2), "block1": blocking(cells, attrs + (1,), 2)}


def cypher():
    out = {}
    coords = CA if not MUT.get("drop_support") else CA[1:]
    for desc in ("computed", "reading", "hub"):
        cells, attrs = index_a(desc)
        out["A_" + desc] = run_index(coords, cells, attrs)
    # leave the fold out of the reading's description: what decides it
    cells, attrs = index_a("reading")
    nofold = [c for c in cells if c[:-1] != attrs or c[-1] == U] if not MUT.get("drop_support") else cells
    out["A_reading_nofold"] = {k: verdict(coords, nofold, attrs, "statistics", k) for k in range(2, len(coords))}
    # index B
    rb = list(READ_B.values())
    for desc in ("computed", "hub"):
        attrs = RING[desc]
        out["B_" + desc] = run_index(CB, rb + [attrs + (U,)], attrs)
    out["B_hub_nohub"] = verdict(CB, [c for c in rb if c[0] != 1 or c[-1] != 1] + [RING["hub"] + (U,)],
                                 RING["hub"], "statistics", 2)
    # R7 control: the ring's nature entered
    ctrl = {}
    for v in (0, 1):
        cells = list(RULED.values()) + [RING["computed"] + (v,)]
        ctrl[v] = all(RING["computed"] + (v,) in (admitted(CA, cells, lambda h: True, lg, 2, None) or set())
                      for lg in ("order", "algebra", "geometry", "information", "statistics"))
    out["control"] = ctrl
    return out


def compute():
    return {"words": words(), "ring": ring_attributes(), "fold": fold_line_tension(), "cy": cypher()}


def _names(coords, blocks):
    return sorted(tuple(coords[i] for i in S) for S in blocks)


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("R0 M's words verbatim in the rulings file: 129, 130 (black hole not matter; i, no added matter), 201, 202, 207",
        all(d["words"].values()))
    r = d["ring"]
    add("R1 the ring is positive over the family (0.01-0.11 a sigma), vanishes with the fold (theta -> 0) and otherwise "
        "only at 120 deg (the Plateau angle); the family meets the plane at 5-16 deg, far from it",
        r["positive"] and 0.01 < r["range"][0] and r["range"][1] < 0.11 and r["vanishes_with_fold"]
        and [round(z) for z in r["zeros_deg"]] == [0, 120] and 5 < r["theta_range"][0] and r["theta_range"][1] < 16)
    f = d["fold"]
    add("R2 a thin pure-tension sheet's fold carries no line tension: the band integral and the rounding correction "
        "sigma w (theta - 2 tan(theta/2)) vanish as w -> 0, the correction negative on (0, pi), -sigma w theta^3/12 to "
        "leading order -- the plane as modelled gives its fold zero, never the ring's positive tension",
        f["limit"] == 0 and f["band_limit"] == 0 and f["negative"] and f["series"])
    c = d["cy"]
    A = c["A_computed"]
    robust = ("geometry", "information", "statistics")
    add("R4 index A, the ring as computed (a line, tension solved from the balance): geometry, information and "
        "statistics refuse it under every coding; order and algebra fall every way across codings (coding-dependent, "
        "an artefact); statistics refuses at orders 2-4, blocked for 'not matter' by (support, matter) and "
        "(fixed_by, matter)",
        all(A["per"][lg] == {"refused"} for lg in robust)
        and all(A["per"][lg] == {"0", "1", "both", "refused"} for lg in ("order", "algebra"))
        and set(A["stat_by_order"].values()) == {"refused"}
        and _names(CA, A["block0"]) == [("fixed_by", "matter"), ("support", "matter")])
    R = c["A_reading"]
    add("R5 index A, the reading's description (the ring entered as the fold): statistics decides 'not matter' at "
        "orders 2-4 -- the fold's own tuple; no language admits 'matter' alone under any coding; with the fold left "
        "out, decided at order 2 and refused at order 3",
        set(R["stat_by_order"].values()) == {"0"} and all(v <= {"0", "both"} and "0" in v for v in R["per"].values())
        and c["A_reading_nofold"][2] == "0" and c["A_reading_nofold"][3] == "refused")
    B, H, BH = c["B_computed"], c["A_hub"], c["B_hub"]
    add("R6 the ring as a line tension fixed by the plane (the hub's case): on M's carriers refused by geometry, "
        "information and statistics under every coding, blocked by (support, matter) alone; on the junctions physics "
        "records, statistics decides 'own structure' at orders 2-4 (no language 'separate' alone), and refuses the "
        "ring as computed, blocked for 'own structure' by (fixed_by, own) alone; without Carroll-Hellerman-Trodden's "
        "hub, refused",
        all(H["per"][lg] == {"refused"} for lg in robust) and _names(CA, H["block0"]) == [("support", "matter")]
        and set(BH["stat_by_order"].values()) == {"1"} and all(v <= {"1", "both"} for v in BH["per"].values())
        and set(B["stat_by_order"].values()) == {"refused"} and _names(CB, B["block1"]) == [("fixed_by", "own")]
        and c["B_hub_nohub"] == "refused")
    add("R7 control: the ring's nature entered, either way, is admitted by every language -- the refusals are the "
        "ring's, not the index's", c["control"][0] and c["control"][1])
    return res


MUTANTS = {"misquote": "M's 130 quoted as 'a black hole is matter'",
           "fold_tension": "the thin fold given a line tension of its own",
           "ring_as_fold": "the ring as computed replaced by the reading's description",
           "drop_support": "the support coordinate (sheet or line) dropped",
           "seat_ring": "the ring entered as not matter (the answer seated)"}


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
        print("  mutant %-13s %-55s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("ring_cypher.py -- the ring's nature (item 207)\n")
    print("words", d["words"])
    r = d["ring"]
    print("R1 ring %.3f-%.3f a sigma, meeting angle %.1f-%.1f deg, zeros of lambda(theta) at %s deg"
          % (r["range"] + r["theta_range"] + ([round(z, 1) for z in r["zeros_deg"]],)))
    print("R2 fold line tension as w -> 0:", d["fold"]["limit"], " rounding correction negative:", d["fold"]["negative"])
    c = d["cy"]
    for key in ("A_computed", "A_reading", "A_hub", "B_computed", "B_hub"):
        v = c[key]
        coords = CA if key.startswith("A") else CB
        print("%-11s per language %s" % (key, {k: sorted(x) for k, x in v["per"].items()}))
        print("            statistics by order %s; blocking pairs for 0: %s; for 1: %s"
              % (v["stat_by_order"], _names(coords, v["block0"]), _names(coords, v["block1"])))
    print("A_reading without the fold:", c["A_reading_nofold"], "  B_hub without the hub:", c["B_hub_nohub"])
    print("control (the ring's nature entered):", c["control"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
