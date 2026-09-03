#!/usr/bin/env python3
"""cypher.py — the cypher analysis (§33) run as a program.

Given an index, ask each language of a declared roster whether it can speak of it,
and read the answer off the pattern of who answers and who does not.

    python3 tools/cypher.py --selftest
    python3 tools/cypher.py --index spec.json --roster 1173
    python3 tools/cypher.py --cells cells.tsv --name L_x --roster 33.1 --json

Three things this program refuses to do, each because the corpus paid to learn it:

  1. It never prints SILENT for a language that was never run. Register 1172 found five
     language/index pairs asserted rather than measured; NOT-RUN is a distinct state here.
  2. It never counts agreement at two coordinates as evidence. Register 1175: at d = 2 there
     is one pair, so pairwise consistency and the cell coincide and every language agrees for
     no reason. Such a run is marked DEGENERATE and its agreement is withheld.
  3. It never picks the roster for you. Which six (or seven) languages there are is docket
     20x-04/20x-09, open and unruled; --roster is required and the rosters are data.

Each operator carries a status. PINNED means the corpus defines it at the precision a program
needs. RECONSTRUCTED means the definition here was derived from the corpus's own pairings and
the cited literature, and is corroborated by reproducing recorded numbers (see --selftest) but
has not been ruled. Reports print the status beside every verdict.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import json
import sys
from dataclasses import dataclass, asdict

# --------------------------------------------------------------------- state

SPEAKS, SILENT, NOT_RUN = "SPEAKS", "SILENT", "NOT-RUN"
# PINNED   — the corpus defines the operator at the precision a program needs.
# ADOPTED  — reconstructed from the corpus's own language-pairings plus the cited literature,
#            corroborated against recorded numbers, and adopted by ruling. The provenance is
#            kept rather than flattened to PINNED: a later ruling can still move it.
# DECLARED — answers in a currency other than an admitted set; needs a witness.
PINNED, ADOPTED, DECLARED = "PINNED", "ADOPTED", "DECLARED"


@dataclass
class Verdict:
    language: str
    state: str
    status: str
    admitted: int | None = None
    E: int | None = None
    note: str = ""
    basis: str = ""

    def row(self) -> str:
        e = "-" if self.E is None else str(self.E)
        a = "-" if self.admitted is None else str(self.admitted)
        return f"  {self.language:<19} {self.state:<8} {self.status:<14} {a:>7} {e:>7}  {self.note}"


class Index:
    """A set of cells over ordinal coordinates."""

    def __init__(self, name, coords, cells, value_order=None, declared=None, outputs=None):
        self.name = name
        self.coords = list(coords)
        self.declared = declared or {}
        self.outputs = outputs or []
        self.warnings: list[str] = []

        raw = [tuple(c) for c in cells]
        if not raw:
            raise ValueError("index has no cells")
        for c in raw:
            if len(c) != len(self.coords):
                raise ValueError(f"cell {c} has {len(c)} values, expected {len(self.coords)}")

        # R is order-dependent (§20.3: the notation was the coordinate that made the rule
        # expressible), so every coordinate needs a declared or inferable value order.
        vo = dict(value_order or {})
        self.code: list[dict] = []
        for i, name_i in enumerate(self.coords):
            vals = {c[i] for c in raw}
            if name_i in vo:
                order = list(vo[name_i])
                missing = vals - set(order)
                if missing:
                    raise ValueError(f"coordinate {name_i}: declared order omits {sorted(missing)}")
            else:
                try:
                    order = sorted(vals, key=lambda v: (float(v), str(v)))
                except (TypeError, ValueError):
                    order = sorted(vals, key=str)
                    self.warnings.append(
                        f"coordinate {name_i!r}: no declared value order, fell back to "
                        f"lexicographic. R depends on this order — declare it (§20.3)."
                    )
            self.code.append({v: r for r, v in enumerate(order)})

        self.decode = [{r: v for v, r in m.items()} for m in self.code]
        self.cells = sorted({tuple(self.code[i][v] for i, v in enumerate(c)) for c in raw})
        if len(self.cells) != len(raw):
            self.warnings.append(f"{len(raw) - len(self.cells)} duplicate cells collapsed")
        self.d = len(self.coords)
        self.alphabets = [sorted({c[i] for c in self.cells}) for i in range(self.d)]
        self.box = 1
        for a in self.alphabets:
            self.box *= len(a)

    def ambient(self):
        return itertools.product(*self.alphabets)


# ----------------------------------------------------------------- operators
# Each returns (admitted set | None, note). None means the operator is SILENT — its
# precondition fails on this object, which is itself the finding (§33.2).

def op_order(ix, opts):
    """R, §32.4.1. R(X) = {x in box : x_i <= phi_ij(x_j) for all i != j},
    phi_ij(a) = max{y_i : y in X, y_j <= a}. Matches the seated instrument rclose.py."""
    if ix.d < 2:
        return None, "R needs at least two coordinates"
    X, D = ix.cells, ix.d
    phi = {}
    for i in range(D):
        for j in range(D):
            if i == j:
                continue
            for a in ix.alphabets[j]:
                cand = [y[i] for y in X if y[j] <= a]
                phi[(i, j, a)] = max(cand) if cand else None
    out = set()
    for x in ix.ambient():
        good = True
        for i in range(D):
            for j in range(D):
                if i == j:
                    continue
                p = phi[(i, j, x[j])]
                if p is None or x[i] > p:
                    good = False
                    break
            if not good:
                break
        if good:
            out.add(x)
    return out, "staircase closure over the ambient product"


def op_statistics(ix, opts):
    """Max-entropy on the order-k marginals. IPF sends a cell to zero exactly when one of its
    k-projections is unobserved, so the support is the k-wise marginal support (register 1174)."""
    k = opts.get("statistics_order", 2)
    if ix.d <= k:
        return None, f"needs more than {k} coordinates at order {k} (reg 1175)"
    subsets = list(itertools.combinations(range(ix.d), k))
    seen = {S: {tuple(x[i] for i in S) for x in ix.cells} for S in subsets}
    out = {x for x in ix.ambient()
           if all(tuple(x[i] for i in S) in seen[S] for S in subsets)}
    return out, f"max-entropy support on the order-{k} marginals"


def op_geometry(ix, opts):
    """Does it embed in a product? The integer points of the polytope A x <= b, relaxed to the
    two-variable rows the method's A actually has: admit x when every 2-D shadow (x_i, x_j) lies
    in the convex hull of that shadow of X. Caratheodory's bound at d = 2."""
    if ix.d < 2:
        return None, "needs at least two coordinates"
    hulls = {}
    for i, j in itertools.combinations(range(ix.d), 2):
        hulls[(i, j)] = _hull2({(x[i], x[j]) for x in ix.cells})
    out = {x for x in ix.ambient()
           if all(_in_hull2((x[i], x[j]), H) for (i, j), H in hulls.items())}
    return out, "integer points of the two-variable polytope"


def op_algebra(ix, opts):
    """Is it closed under an operation? The sublattice closure: iterate coordinatewise meet and
    join to a fixed point (§7.3; Birkhoff, Lattice Theory)."""
    budget = opts.get("algebra_budget", 20000)
    S = set(ix.cells)
    while True:
        if len(S) > budget:
            return None, f"sublattice closure exceeded {budget} cells; raise --algebra-budget"
        L = sorted(S)
        new = set()
        for a in range(len(L)):
            x = L[a]
            for b in range(a + 1, len(L)):
                y = L[b]
                mn = tuple(map(min, x, y))
                mx = tuple(map(max, x, y))
                if mn not in S:
                    new.add(mn)
                if mx not in S:
                    new.add(mx)
        if not new:
            return S, "closure under coordinatewise meet and join"
        S |= new


def op_information(ix, opts):
    """Does a coordinate add join-irreducibles? Its admission form is the seed and its regrowth:
    take the join-irreducible elements of X and close them under join. Birkhoff's representation
    theorem (1937) — every element of a finite distributive lattice is a join of join-irreducibles,
    so a distributive index regenerates from its seed exactly. The Math. Compendium states the same
    object: 'the matrix A and nothing more, from which all 976 cells regenerate'."""
    X = ix.cells
    Xs = set(X)
    seed = []
    for x in X:
        below = [y for y in Xs if y != x and all(a <= b for a, b in zip(y, x))]
        if not below:
            seed.append(x)
            continue
        sup = below[0] if len(below) == 1 else tuple(map(max, *below))
        if sup != x:
            seed.append(x)
    budget = opts.get("algebra_budget", 20000)
    S = set(seed)
    while True:
        if len(S) > budget:
            return None, f"join-closure exceeded {budget} cells; raise --algebra-budget"
        L = sorted(S)
        new = set()
        for a in range(len(L)):
            x = L[a]
            for b in range(a + 1, len(L)):
                z = tuple(map(max, x, L[b]))
                if z not in S:
                    new.add(z)
        if not new:
            return S, f"join-closure of {len(seed)} join-irreducibles"
        S |= new


def op_documentary(ix, opts):
    """No closure mechanism exists (P20's table; register 1173). Silent by construction — it
    returns a citation, not a binary, which is why it earns no operator row."""
    return None, "no closure mechanism exists"


ADMISSION = {
    "order": (op_order, PINNED,
              "R, §32.4.1; Moore 1910 (closure operator); Deville, Barette & Van Hentenryck 1999 "
              "(monotone staircases); seated instrument rclose.py"),
    "statistics": (op_statistics, PINNED,
                   "register 1174; Deming & Stephan 1940, Ireland & Kullback 1968 (IPF)"),
    "geometry": (op_geometry, ADOPTED,
                 "Math. Compendium 'the integer points of the polytope A x <= b are the lattice "
                 "exactly'; Caratheodory 1911; Schrijver 1986 (integer hull)"),
    "algebra": (op_algebra, ADOPTED,
                "Math. Compendium 'closed under coordinatewise join and meet', §7.3; "
                "Birkhoff, Lattice Theory (1940)"),
    "information": (op_information, ADOPTED,
                    "Math. Compendium 'the matrix A and nothing more, from which all 976 cells "
                    "regenerate'; Birkhoff 1937 (representation theorem); §33.3"),
    "documentary": (op_documentary, PINNED,
                    "P20's table; register 1173 — returns a citation, not a binary"),
}

# analysis is not an admission operator: it asks whether a continuous law exists, which is
# answered by a fit or by the absence of a derivative, and must be declared with a witness.
DECLARED_ONLY = {
    "analysis": "is there a continuous law here? declare with a witness (an R^2, or a reason "
                "none exists — e.g. a finite set of surds has no derivative)",
}


def _hull2(pts):
    """Monotone-chain hull of a 2-D integer point set; returns 1, 2 or >=3 points."""
    P = sorted(pts)
    if len(P) < 3:
        return P
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower = []
    for p in P:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(P):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    H = lower[:-1] + upper[:-1]
    # A collinear projection collapses to the segment [min, max], which is the correct hull;
    # only a genuinely empty chain falls back to the raw points.
    return H if len(H) >= 2 else P


def _in_hull2(p, H):
    if len(H) == 1:
        return p == H[0]
    if len(H) == 2:
        (x1, y1), (x2, y2) = H
        if (x2 - x1) * (p[1] - y1) - (y2 - y1) * (p[0] - x1) != 0:
            return False
        return min(x1, x2) <= p[0] <= max(x1, x2) and min(y1, y2) <= p[1] <= max(y1, y2)
    n = len(H)
    for i in range(n):
        a, b = H[i], H[(i + 1) % n]
        if (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) < 0:
            return False
    return True


def coordinate_report(ix):
    """Does a coordinate add anything? Per coordinate: the cells surviving its removal, and
    whether it individuates every cell — a coordinate that does is a key and not an axis
    (register 1356, the fault that voided Lambda_ladder's closure)."""
    rows = []
    for i, name in enumerate(ix.coords):
        kept = {tuple(v for j, v in enumerate(c) if j != i) for c in ix.cells}
        rows.append({
            "coordinate": name,
            "cells_without": len(kept),
            "adds_nothing": len(kept) == len(ix.cells),
            "values": len(ix.alphabets[i]),
        })
    keys = [r["coordinate"] for r in rows
            if r["values"] == len(ix.cells) and len(ix.cells) > 1]
    return rows, keys


# ------------------------------------------------------------------- rosters
# Data, not doctrine. Which languages there are is docket 20x-04/20x-09, open and unruled.

ROSTERS = {
    "1173": {
        "cite": "register 1173 — logic is the mechanism, not a language",
        "languages": ["order", "algebra", "analysis", "geometry", "information",
                      "statistics", "documentary"],
        "note": "five operator-bearing languages give C(5,2) = 10 combinations, "
                "plus statistics as a sixth and documentary as a seventh",
        "operator_bearing": ["order", "algebra", "analysis", "geometry", "information"],
        "pairs_claimed": 10,
    },
    "33.1": {
        "cite": "§33.1 — the six the cypher chapter asks",
        "languages": ["order", "analysis", "algebra", "geometry", "information", "statistics"],
        "note": "the roster the instrument's own chapter prints",
    },
    "20.2": {
        "cite": "§20.2 — the six the chapter §33.1 cites for its principle",
        "languages": ["order", "geometry", "arithmetic", "calculus", "logic",
                      "constraint-language"],
        "note": "shares only two names with §33.1's six; 'arithmetic', 'calculus', 'logic' and "
                "'constraint-language' have no ruled operator mapping (docket 20x-04)",
        "pairs_claimed": 10,
    },
}


def run(ix, roster_name, opts):
    roster = ROSTERS[roster_name]
    verdicts, admitted_sets = [], {}

    for lang in roster["languages"]:
        if lang in ADMISSION:
            fn, status, basis = ADMISSION[lang]
            out, note = fn(ix, opts)
            if out is None:
                verdicts.append(Verdict(lang, SILENT, status, note=note, basis=basis))
                continue
            if not set(ix.cells) <= out:
                lost = len(set(ix.cells) - out)
                verdicts.append(Verdict(lang, SPEAKS, status, len(out), None,
                                        f"NOT EXTENSIVE — drops {lost} of its own cells", basis))
                continue
            admitted_sets[lang] = out
            if lang == "information":
                rows, keys = coordinate_report(ix)
                dead = [r["coordinate"] for r in rows if r["adds_nothing"]]
                if dead:
                    note += " | adds nothing: " + ", ".join(dead)
                if keys:
                    note += f" | KEY not axis: {', '.join(keys)} (reg 1356)"
            verdicts.append(Verdict(lang, SPEAKS, status, len(out),
                                    len(out) - len(ix.cells), note, basis))

        elif lang in DECLARED_ONLY:
            d = ix.declared.get(lang)
            if d is None:
                verdicts.append(Verdict(lang, NOT_RUN, DECLARED,
                                        note="no witness declared — NOT measured (reg 1172)",
                                        basis=DECLARED_ONLY[lang]))
            else:
                st = SPEAKS if d.get("speaks") else SILENT
                verdicts.append(Verdict(lang, st, DECLARED,
                                        note=str(d.get("witness", "")),
                                        basis=DECLARED_ONLY[lang]))
        else:
            verdicts.append(Verdict(lang, NOT_RUN, DECLARED,
                                    note="roster names an operator this build does not "
                                         "implement (docket 20x-04)"))

    # K.langclose: E = 0 iff the languages agree (BFMY 1983 read as an equivalence).
    measured = {k: v for k, v in admitted_sets.items()}
    agree = None
    if len(measured) >= 2:
        agree = len({frozenset(v) for v in measured.values()}) == 1
    all_zero = all(len(v) == len(ix.cells) for v in measured.values()) if measured else None

    # Which languages are operator-bearing is not declared here: it is measured. A language is
    # operator-bearing on this index when it returned an admitted set — register 1173's own test,
    # "logic can operate on it and get a binary back" — and C(n,2) follows from what was measured.
    bearing = sorted(admitted_sets)
    pairs = [{"a": a, "b": b,
              "agree": frozenset(admitted_sets[a]) == frozenset(admitted_sets[b])}
             for a, b in itertools.combinations(bearing, 2)]

    degenerate = ix.d <= opts.get("statistics_order", 2)
    return {
        "operator_bearing_measured": bearing,
        "operator_bearing_claimed": roster.get("operator_bearing"),
        "pairs_claimed": roster.get("pairs_claimed"),
        "pairs": pairs,
        "pairs_agreeing": sum(p["agree"] for p in pairs),
        "index": ix.name,
        "coordinates": ix.coords,
        "d": ix.d,
        "cells": len(ix.cells),
        "box": ix.box,
        "roster": roster_name,
        "roster_cite": roster["cite"],
        "verdicts": [asdict(v) for v in verdicts],
        "languages_agree": agree,
        "all_E_zero": all_zero,
        "langclose_holds": None if agree is None or all_zero is None else (agree == all_zero),
        "agreement_withheld": bool(degenerate and agree),
        "degenerate": degenerate,
        "singleton_ok": len(ix.outputs) <= 1,
        "outputs": ix.outputs,
        "warnings": ix.warnings,
        "_verdicts": verdicts,
    }


def pairs_report(res):
    """The C(n,2) arithmetic, measured rather than declared."""
    o = [""]
    n = len(res["operator_bearing_measured"])
    cn2 = n * (n - 1) // 2
    claimed = res["operator_bearing_claimed"]
    if claimed:
        c = len(claimed)
        o.append(f"  operator-bearing, CLAIMED by roster {res['roster']} ({c}): "
                 f"{', '.join(claimed)}")
        o.append(f"      -> C({c},2) = {c*(c-1)//2}"
                 + (f", roster asserts {res['pairs_claimed']}"
                    if res.get("pairs_claimed") else ""))
    o.append(f"  operator-bearing, MEASURED on this index ({n}): "
             f"{', '.join(res['operator_bearing_measured'])}")
    o.append(f"      -> C({n},2) = {cn2}")
    if claimed:
        lost = [l for l in claimed if l not in res["operator_bearing_measured"]]
        gained = [l for l in res["operator_bearing_measured"] if l not in claimed]
        for l in lost:
            o.append(f"      claimed but returns no binary: {l}")
        for l in gained:
            o.append(f"      measured but not claimed:      {l}")
    o.append("")
    o.append(f"  {'pair':<28} verdict")
    o.append(f"  {'-'*28} {'-'*7}")
    for p in res["pairs"]:
        o.append(f"  {p['a'] + ' + ' + p['b']:<28} "
                 f"{'agree' if p['agree'] else 'DIFFER'}")
    o.append(f"\n  {res['pairs_agreeing']} of {cn2} pairs agree.")
    return "\n".join(o)


def report(res):
    o = []
    o.append(f"cypher — {res['index']}   d = {res['d']}   cells = {res['cells']}   "
             f"box = {res['box']}")
    o.append(f"roster {res['roster']}: {res['roster_cite']}")
    o.append("")
    o.append(f"  {'language':<19} {'state':<8} {'status':<14} {'admits':>7} {'E':>7}  note")
    o.append(f"  {'-'*19} {'-'*8} {'-'*14} {'-'*7} {'-'*7}  {'-'*4}")
    for v in res["_verdicts"]:
        o.append(v.row())
    o.append("")

    # Register 1175's trap is a FALSE AGREEMENT at low dimension: with one pair, pairwise
    # consistency and the cell coincide, so languages can agree for no reason. It is not a reason
    # to withhold a DISAGREEMENT — that is real information at any dimension.
    if res["langclose_holds"] is None:
        o.append("  K.langclose not testable — fewer than two languages were measured.")
    elif res["degenerate"] and res["languages_agree"]:
        o.append("  DEGENERATE — at this many coordinates pairwise consistency and the cell")
        o.append("  coincide, so the languages may agree for no reason. The agreement is NOT")
        o.append("  evidence (reg 1175), and no K.langclose verdict is recorded.")
    else:
        a = "agree" if res["languages_agree"] else "disagree"
        z = "E = 0" if res["all_E_zero"] else "E > 0"
        held = "holds" if res["langclose_holds"] else "FAILS"
        o.append(f"  K.langclose {held}: languages {a} and {z}.")
        if not res["langclose_holds"]:
            o.append("  A disagreement between languages at E = 0 is the one thing the cypher "
                     "forbids.")
        if res["degenerate"]:
            o.append("  (Low dimension: statistics is silent here and the disagreement rests on "
                     "the rest — reg 1175.)")

    not_run = [v.language for v in res["_verdicts"] if v.state == NOT_RUN]
    if not_run:
        o.append(f"  NOT RUN (asserted, not measured): {', '.join(not_run)}")
    if not res["singleton_ok"]:
        o.append(f"  SINGLETON FAILS — {len(res['outputs'])} outputs declared "
                 f"({', '.join(map(str, res['outputs']))}); §33.4 requires one.")
    for w in res["warnings"]:
        o.append(f"  warning: {w}")
    return "\n".join(o)


# ------------------------------------------------------------------- fixtures

def _lambda():
    rng = dict(n=range(1, 4), l=range(0, 2), k=range(1, 4), q=range(0, 4),
               e=range(1, 4), f=range(0, 2), g=range(0, 4), S=range(0, 4))
    order = ["n", "l", "k", "q", "e", "f", "g", "S"]
    cells = []
    for t in itertools.product(*[rng[c] for c in order]):
        d = dict(zip(order, t))
        if (d["l"] <= d["n"] - 1 and d["k"] <= 4 * d["l"] + 2 and d["q"] <= d["k"]
                and d["f"] <= d["e"] - 1 and d["g"] <= 4 * d["f"] + 2
                and d["g"] <= d["q"] and d["S"] <= d["k"] and d["k"] >= 1):
            cells.append(t)
    return Index("Lambda (8 coords, caps §7.4)", order, cells)


def _periodic(three=False):
    occ = []
    for g in (1, 18):
        occ.append((1, g))
    for p in (2, 3):
        for g in (1, 2, 13, 14, 15, 16, 17, 18):
            occ.append((p, g))
    for p in (4, 5, 6, 7):
        for g in range(1, 19):
            occ.append((p, g))
    if not three:
        return Index("periodic table (period x group)", ["period", "group"], occ)
    # register 1175 rebuilds at three by adjoining the block, non-monotone in the second
    # coordinate. Block is a function of group, which is the point: information says so.
    def block(g):
        return 0 if g <= 2 else (1 if g >= 13 else 2)          # s, p, d
    return Index("periodic table (period x group x block)",
                 ["period", "group", "block"], [(p, g, block(g)) for p, g in occ])


def _janet():
    """Janet: n+l against position within the n+l group — the left-step table."""
    cells = []
    for n in range(1, 8):
        for l in range(0, min(n, 4)):
            cells.append((n + l, l))
    return Index("Janet (n+l x l)", ["n+l", "l"], sorted(set(cells)))


def _calendar():
    """365 cells in a box of 372, E = 7 — February's missing 29th to 31st and the four
    thirty-day months' 31sts."""
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return Index("calendar (month, day)", ["month", "day"],
                 [(m + 1, d) for m, n in enumerate(days) for d in range(1, n + 1)])


def _box_ordering():
    """35 cells in a box of 125, E = 0 — register 1176's own agreeing fixture."""
    return Index("box ordering (l >= w >= h)", ["l", "w", "h"],
                 [t for t in itertools.product(range(5), repeat=3)
                  if t[0] >= t[1] >= t[2]])


def _kreuzer_skarke():
    """The KS list's chi = +/-6 points: Hodge pairs (h, h+3) and (h+3, h) for 13 <= h <= 128,
    excluding h = 102, 103, 115, 117 and 119-126. Candelas, de la Ossa, He & Szendroi,
    Triadophilia, ATMP 12 (2008) 429; §31.3.4."""
    ex = {102, 103, 115, 117} | set(range(119, 127))
    hs = [h for h in range(13, 129) if h not in ex]
    cells = sorted({(h, h + 3) for h in hs} | {(h + 3, h) for h in hs})
    return Index("Kreuzer-Skarke frontier (chi = +/-6 slice)", ["h11", "h21"], cells)


FIXTURES = [
    # (label, builder, expected E by language, expected scalars)
    ("Lambda", _lambda,
     {"order": 0, "geometry": 0, "algebra": 0, "statistics": 0, "information": 0},
     {"cells": 976, "box": 6912}),
    ("periodic table 2-D", _periodic, {"order": 36}, {"cells": 90}),
    ("periodic table 3-D", lambda: _periodic(True),
     {"order": 100, "statistics": 0, "information": 24}, {"cells": 90}),
    ("Janet 2-D", _janet, {"order": 0, "information": 0}, {}),
    ("calendar 2-D", _calendar, {"order": 7}, {"cells": 365, "box": 372}),
    ("box ordering", _box_ordering,
     {"order": 0, "geometry": 0, "algebra": 0, "statistics": 0, "information": 0},
     {"cells": 35, "box": 125}),
    ("Kreuzer-Skarke slice", _kreuzer_skarke, {"order": 540}, {"cells": 208}),
]


def selftest(opts):
    """Reproduce the corpus's own recorded numbers. Failures are reported, never tuned away."""
    print("cypher --selftest — against the numbers the corpus records\n")
    bad = 0
    for label, build, expect_E, extra in FIXTURES:
        ix = build()
        res = run(ix, "33.1", opts)
        got = {v.language: v.E for v in res["_verdicts"] if v.E is not None}
        line = [f"{label:<20} d={ix.d} cells={len(ix.cells)} box={ix.box}"]
        for k, want in extra.items():
            have = len(ix.cells) if k == "cells" else ix.box
            ok = have == want
            bad += not ok
            line.append(f"{k}={have}{'' if ok else f' != {want} MISMATCH'}")
        print("  " + "  ".join(line))
        for lang, want in expect_E.items():
            have = got.get(lang)
            ok = have == want
            bad += not ok
            print(f"      E({lang:<11}) = {have!s:<6} expected {want:<6} "
                  f"{'ok' if ok else 'MISMATCH'}")

    # register 1174's marginal orders, on Lambda
    ix = _lambda()
    for k, want in ((1, 6912), (2, 976)):
        out, _ = op_statistics(ix, {"statistics_order": k})
        ok = out is not None and len(out) == want
        bad += not ok
        print(f"  statistics order-{k} on Lambda admits "
              f"{'-' if out is None else len(out)} expected {want} "
              f"{'ok' if ok else 'MISMATCH'}   (reg 1174)")

    # register 1175's degeneracy guard must fire at d = 2 and not at d = 3
    for label, build, want in (("periodic 2-D", _periodic, True),
                               ("periodic 3-D", lambda: _periodic(True), False)):
        res = run(build(), "33.1", opts)
        ok = res["degenerate"] == want
        bad += not ok
        print(f"  degeneracy guard on {label:<14} = {res['degenerate']!s:<6} expected {want!s:<6} "
              f"{'ok' if ok else 'MISMATCH'}   (reg 1175)")

    # the KS slice states its join/meet failure counts and the shape of what R admits
    ix = _kreuzer_skarke()
    S = set(ix.cells)
    jf = sum(tuple(map(max, a, b)) not in S for a, b in itertools.combinations(ix.cells, 2))
    mf = sum(tuple(map(min, a, b)) not in S for a, b in itertools.combinations(ix.cells, 2))
    for what, have, want in (("join failures", jf, 498), ("meet failures", mf, 498)):
        bad += have != want
        print(f"  KS slice {what:<14} = {have:<6} expected {want:<6} "
              f"{'ok' if have == want else 'MISMATCH'}   (§31.3.4)")
    adm, _ = op_order(ix, opts)
    dec = [(ix.decode[0][a], ix.decode[1][b]) for a, b in sorted(set(adm) - set(ix.cells))]
    diag = [c for c in dec if c[0] == c[1]]
    for what, have, want in (("diagonal cells", len(diag), 112),
                             ("distinct chi", len({2 * (a - b) for a, b in dec}), 5),
                             ("min h11+h21", min(a + b for a, b in dec), 26),
                             ("max h11+h21", max(a + b for a, b in dec), 262)):
        bad += have != want
        print(f"  KS admits, {what:<14} = {have:<6} expected {want:<6} "
              f"{'ok' if have == want else 'MISMATCH'}   (§31.3.4)")

    # register 1176: "Lambda and a box ordering: E = 0 and every pair agrees"
    for label, build, want in (("Lambda", _lambda, True), ("box ordering", _box_ordering, True)):
        r = run(build(), "1173", opts)
        n = len(r["pairs"])
        ok = n > 0 and r["pairs_agreeing"] == n and want
        bad += not ok
        print(f"  all pairs agree on {label:<14} = {r['pairs_agreeing']}/{n} "
              f"{'ok' if ok else 'MISMATCH'}   (reg 1176)")

    print(f"\n{'SELFTEST OK' if not bad else f'SELFTEST FAILED — {bad} mismatch(es)'}")
    return 1 if bad else 0


# ----------------------------------------------------------------------- cli

def load_index(args):
    if args.index:
        spec = json.load(open(args.index, encoding="utf-8"))
        return Index(spec.get("name", args.index), spec["coordinates"], spec["cells"],
                     spec.get("value_order"), spec.get("declared"), spec.get("outputs"))
    rows = list(csv.reader(open(args.cells, encoding="utf-8"), delimiter="\t"))
    rows = [r for r in rows if r and not r[0].startswith("#")]
    return Index(args.name or args.cells, rows[0], rows[1:])


def main(argv=None):
    p = argparse.ArgumentParser(description="the cypher analysis (§33) run as a program")
    p.add_argument("--index", help="JSON index spec")
    p.add_argument("--cells", help="TSV of cells; first row is the coordinate names")
    p.add_argument("--name", help="index name when using --cells")
    p.add_argument("--roster", choices=sorted(ROSTERS), help="which language roster to ask")
    p.add_argument("--statistics-order", type=int, default=2, dest="statistics_order")
    p.add_argument("--algebra-budget", type=int, default=20000, dest="algebra_budget")
    p.add_argument("--json", action="store_true", help="machine-readable output for audits")
    p.add_argument("--pairs", action="store_true",
                   help="measure the operator-bearing set and its C(n,2) pairwise agreement")
    p.add_argument("--list-rosters", action="store_true")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args(argv)
    opts = {"statistics_order": a.statistics_order, "algebra_budget": a.algebra_budget}

    if a.selftest:
        return selftest(opts)
    if a.list_rosters:
        for k, v in sorted(ROSTERS.items()):
            print(f"{k:<8} {v['cite']}\n         {', '.join(v['languages'])}\n         {v['note']}\n")
        return 0
    if not (a.index or a.cells):
        p.error("need --index, --cells, --selftest or --list-rosters")
    if not a.roster:
        p.error("--roster is required: which languages there are is unruled "
                "(docket 20x-04/20x-09). Try --list-rosters.")

    res = run(load_index(a), a.roster, opts)
    if a.json:
        res.pop("_verdicts")
        print(json.dumps(res, indent=2))
    else:
        print(report(res))
        if a.pairs:
            print(pairs_report(res))
    return 0


if __name__ == "__main__":
    sys.exit(main())
