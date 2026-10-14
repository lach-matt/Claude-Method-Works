#!/usr/bin/env python3
"""isotopes.py -- the isotope index: every nuclide of the mass table on (Z, N).

The repository holds one nuclear table: AME2020 Table I, the published atomic
mass table, captured at extracted/archives/restore-point-2-13/captures/
AME2020-TableI.tsv with its md5 recorded in extracted/LEDGER.tsv. It holds no
NUBASE table, so no spin, parity or half-life is READ anywhere here, and this
instrument does not invent them. What the one table gives is what the index
charts:

    Z    the proton number          READ
    N    the neutron number         READ

Every row of the table is a member, the neutron (0, 1) included, and the chart
is injective: 3,558 members on 3,558 cells. That is the whole index. Everything
else the table carries -- the mass excess and its uncertainty, the quality flag,
the binding energy that follows from three of the table's own entries -- rides
on the member and is REFUSED as a coordinate, each refusal made against a
measurement and not a preference.

The cell is measured here exactly. On two coordinates the containment order is
the product order on (Z, N), so the height is the longest chain (a
non-decreasing run of N over the members sorted by (Z, N)) and the width the
largest antichain (a strictly decreasing run of N, one member per Z), both by
patience sorting, and both witnessed: the instrument returns the chain and the
antichain that attain them. The join-closure deficit E is computed directly:
the cells (max Z, max N) demanded by pairs of members and held by no member.
It is 0 -- the chart of nuclides is join-closed -- so the index demands nothing
and draws no ghost.

The closure channel K is NOT computed here. It needs the five closure operators
of the hierarchy law, which are the research tree's instruments and are
imported by the site build (tools/webindex.py), never copied; the build records
K beside this instrument's own height and width and asserts the two agree.

Binding energy is DERIVED from the table alone, with nothing added:

    B(Z, N) = Z Delta(1H) + N Delta(n) - Delta(Z, N)

in keV, over atomic mass excesses, so the electrons cancel exactly; S_n, S_p,
S_2n and S_2p are differences of B where the neighbour is in the table and
None where it is not, which is counted. The mass in u is A + Delta / (u c^2)
with u c^2 = 931 494.10242 keV (CODATA 2018, the value the evaluation itself
uses); that one constant is EMPIRICAL and named.

This is an index of the site, built from the table the repository holds. It is
not a row of the research tree's register of seated indexes, and it says so.

Usage:
    python3 tools/isotopes.py                # the report
    python3 tools/isotopes.py --selftest     # fixtures: the table's own census
    python3 tools/isotopes.py --member 56Fe  # one member's record
    python3 tools/isotopes.py --json         # the whole block, for a reader
"""

import argparse
import bisect
import hashlib
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AME_REL = "extracted/archives/restore-point-2-13/captures/AME2020-TableI.tsv"
AME = os.path.join(REPO, AME_REL)
LEDGER = os.path.join(REPO, "extracted", "LEDGER.tsv")

CITATION = ("Meng Wang, W. J. Huang, F. G. Kondev, G. Audi and S. Naimi, "
            "The AME 2020 atomic mass evaluation (II), Chinese Physics C 45, 030003 (2021), Table I")
DOI = "10.1088/1674-1137/abddaf"

U_KEV = 931494.10242      # u c^2 in keV, CODATA 2018 -- EMPIRICAL, the evaluation's own value
U_KEV_STATUS = "EMPIRICAL"

# The published census this instrument reproduces, pinned by --selftest.
FIXTURES = {
    "rows": 3558, "md5": "9540ebcd3ef5b9801ca1e859bff46629",
    "measured": 2550, "estimated": 1008,
    "Z": (0, 118), "N": (0, 177), "A": (1, 295),
    "height": 295, "width": 18, "E": 0,
    "carbon_12_u": 12.0,
    "neutron_keV": 8071.3181, "hydrogen_keV": 7288.97106,
    "B_per_A_max": ("62Ni", 8794.555),   # the most tightly bound nuclide, keV per nucleon, from the rounded table's own rows (the evaluation's unrounded file gives 8794.553)
    "S_n_undefined": 119, "S_p_undefined": 179,
}

COORDINATES = [
    {"name": "Z", "meaning": "the proton number, the element", "status": "READ"},
    {"name": "N", "meaning": "the neutron number", "status": "READ"},
]


# ------------------------------------------------------------------ the table

def md5_of(path=AME):
    with open(path, "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()


def ledger_md5(rel=AME_REL, ledger=LEDGER):
    """The md5 extracted/LEDGER.tsv records for the table, or None."""
    if not os.path.isfile(ledger):
        return None
    with open(ledger, encoding="utf-8") as fh:
        for ln in fh:
            p = ln.rstrip("\n").split("\t")
            if len(p) >= 6 and p[5] == rel and p[4] == "EXTRACTED":
                return p[3]
    return None


def read(path=AME):
    """[(Z, N, A, symbol, mass_excess_keV, unc_keV, quality)], A checked as Z + N."""
    rows = []
    with open(path, encoding="utf-8") as fh:
        for ln in fh:
            if ln.startswith("#") or not ln.strip():
                continue
            Z, N, A, sym, dm, unc, q = ln.rstrip("\n").split("\t")
            Z, N, A = int(Z), int(N), int(A)
            if A != Z + N:
                raise ValueError("A != Z + N on %s%s: the table is not what it says" % (A, sym))
            if q not in ("M", "E"):
                raise ValueError("quality flag %r on %s%s" % (q, A, sym))
            rows.append((Z, N, A, sym, float(dm), float(unc), q))
    seen = {}
    for r in rows:
        if r[:2] in seen:
            raise ValueError("two rows at (Z, N) = %s" % (r[:2],))
        seen[r[:2]] = r
    return rows


def index(rows=None):
    """The chart: every (Z, N)."""
    rows = read() if rows is None else rows
    return frozenset((Z, N) for Z, N, *_ in rows)


# ------------------------------------------------------ the cell, exactly, in 2-D

def _lnds(seq):
    """Longest non-decreasing subsequence: (length, indices), patience sorting."""
    tails, tails_idx, prev = [], [], [None] * len(seq)
    for i, v in enumerate(seq):
        k = bisect.bisect_right(tails, v)
        if k == len(tails):
            tails.append(v)
            tails_idx.append(i)
        else:
            tails[k] = v
            tails_idx[k] = i
        prev[i] = tails_idx[k - 1] if k else None
    out, i = [], tails_idx[-1] if tails_idx else None
    while i is not None:
        out.append(i)
        i = prev[i]
    return len(tails), out[::-1]


def _lsds(seq):
    """Longest strictly decreasing subsequence, by negation into a strictly increasing one."""
    neg = [-v for v in seq]
    tails, tails_idx, prev = [], [], [None] * len(neg)
    for i, v in enumerate(neg):
        k = bisect.bisect_left(tails, v)
        if k == len(tails):
            tails.append(v)
            tails_idx.append(i)
        else:
            tails[k] = v
            tails_idx[k] = i
        prev[i] = tails_idx[k - 1] if k else None
    out, i = [], tails_idx[-1] if tails_idx else None
    while i is not None:
        out.append(i)
        i = prev[i]
    return len(tails), out[::-1]


def height2(X):
    """Longest chain in the product order on (Z, N), with a witness chain.

    Sorted by (Z, N), two members are comparable exactly when N does not fall,
    so a chain is a non-decreasing run of N and the height is the longest one.
    """
    S = sorted(X)
    n, idx = _lnds([N for _Z, N in S])
    return n, [S[i] for i in idx]


def width2(X):
    """Largest antichain on (Z, N), with a witness.

    Two members are incomparable exactly when Z rises and N strictly falls, so
    an antichain takes one member per Z with N strictly decreasing; sorted by
    (Z, N) that is a strictly decreasing run of N, and the width is the longest.
    """
    S = sorted(X)
    n, idx = _lsds([N for _Z, N in S])
    return n, [S[i] for i in idx]


def cell2(X):
    """(height, width): the two axes of the cell this instrument measures itself."""
    return height2(X)[0], width2(X)[0]


# --------------------------------------------- the cell, generically, for refusals

def _le(a, b):
    return all(p <= q for p, q in zip(a, b))


def height(X):
    """Longest chain in the product order, any arity; O(n^2)."""
    S = sorted(X)
    best = [1] * len(S)
    for j in range(len(S)):
        sj, bj = S[j], 1
        for i in range(j):
            if best[i] + 1 > bj and _le(S[i], sj):
                bj = best[i] + 1
        best[j] = bj
    return max(best) if best else 0


def width(X):
    """Largest antichain, any arity: n minus a maximum matching of the
    comparability graph (Dilworth by Konig), greedy first, then augmenting."""
    S = sorted(X)
    n = len(S)
    adj = [[j for j in range(i + 1, n) if _le(S[i], S[j])] for i in range(n)]
    mt = {}                                    # right vertex -> left vertex
    ml = [None] * n                            # left vertex -> right vertex
    for i in range(n):                         # greedy
        for j in adj[i]:
            if j not in mt:
                mt[j], ml[i] = i, j
                break
    for i in range(n):                         # augment, iteratively
        if ml[i] is not None:
            continue
        seen, stack, parent = set(), [(i, iter(adj[i]))], {}
        found = None
        while stack and found is None:
            u, it = stack[-1]
            for j in it:
                if j in seen:
                    continue
                seen.add(j)
                parent[j] = u
                if j not in mt:
                    found = j
                    break
                stack.append((mt[j], iter(adj[mt[j]])))
                break
            else:
                stack.pop()
        if found is not None:                  # flip the path
            j = found
            while True:
                u = parent[j]
                nxt = ml[u]
                mt[j], ml[u] = u, j
                if nxt is None:
                    break
                j = nxt
    return n - len(mt)


# ------------------------------------------------------------------ the closures

def join_closure(X):
    """(J(X), demanded): the join-closure of the chart and the cells it demands."""
    S = set(X)
    while True:
        new = {(max(a[0], b[0]), max(a[1], b[1])) for a in S for b in S} - S
        if not new:
            return frozenset(S), sorted(frozenset(S) - frozenset(X))
        S |= new


def join_deficit(X):
    """E: the cells the join-closure demands and the table does not hold.

    Computed without the pairwise sweep: the chart is join-closed exactly when,
    for every Z, the set of N is an up-set within the chart's own N-ranges --
    for members (Z1, N1) and (Z2, N2) the join (max Z, max N) must be held.
    Both routes are run; the sweep is the check.
    """
    by_z = {}
    for Z, N in X:
        by_z.setdefault(Z, set()).add(N)
    zs = sorted(by_z)
    demanded = set()
    for i, z1 in enumerate(zs):
        for z2 in zs[i:]:
            for n1 in by_z[z1]:
                for n2 in by_z[z2]:
                    m = max(n1, n2)
                    if m not in by_z[z2]:
                        demanded.add((z2, m))
    return len(demanded), sorted(demanded)


def meet_deficit(X):
    """The meet-closure's demand: (min Z, min N) over pairs, not held. Reported
    as a measurement of the chart's shape, not as a language's closure."""
    by_z = {}
    for Z, N in X:
        by_z.setdefault(Z, set()).add(N)
    zs = sorted(by_z)
    demanded = set()
    for i, z1 in enumerate(zs):
        for z2 in zs[:i + 1]:
            for n1 in by_z[z1]:
                for n2 in by_z[z2]:
                    m = min(n1, n2)
                    if m not in by_z[z2]:
                        demanded.add((z2, m))
    return len(demanded), sorted(demanded)


# ------------------------------------------------------------------ the members

def binding(rows):
    """{(Z, N): B_keV} from three of the table's own entries per member."""
    dm = {(Z, N): d for Z, N, _A, _s, d, _u, _q in rows}
    dh, dn = dm[(1, 0)], dm[(0, 1)]
    return {(Z, N): Z * dh + N * dn - dm[(Z, N)] for Z, N in dm}


def members(rows=None):
    """One record per row of the table, every derived figure from the table alone."""
    rows = read() if rows is None else rows
    B = binding(rows)

    def sep(Z, N, dz, dn):
        k = (Z - dz, N - dn)
        return round(B[(Z, N)] - B[k], 3) if k in B else None

    out = []
    for Z, N, A, sym, dm, unc, q in sorted(rows):
        key = "%s-%d" % (sym, A)
        out.append({
            "name": "%d%s" % (A, sym), "key": key, "coords": [Z, N],
            "extra": {"A": A, "sym": sym, "Z": Z, "N": N, "dm_keV": dm, "unc_keV": unc, "quality": q,
                      "M_u": round(A + dm / U_KEV, 9),
                      "B_keV": round(B[(Z, N)], 3), "B_per_A_keV": round(B[(Z, N)] / A, 3),
                      "S_n": sep(Z, N, 0, 1), "S_p": sep(Z, N, 1, 0), "S_2n": sep(Z, N, 0, 2), "S_2p": sep(Z, N, 2, 0)},
        })
    return out


def member(name, rows=None):
    """One record by name: 56Fe, Fe-56, Fe56 or ^56Fe."""
    t = name.strip().lstrip("^").replace("-", "").replace(" ", "")
    digits = "".join(c for c in t if c.isdigit())
    sym = "".join(c for c in t if c.isalpha())
    for m in members(rows):
        if m["extra"]["sym"].lower() == sym.lower() and str(m["extra"]["A"]) == digits:
            return m
    return None


# ------------------------------------------------------------------- the census

def census(rows=None):
    rows = read() if rows is None else rows
    by_z, by_n, by_a = {}, {}, {}
    for Z, N, A, *_ in rows:
        by_z[Z] = by_z.get(Z, 0) + 1
        by_n[N] = by_n.get(N, 0) + 1
        by_a[A] = by_a.get(A, 0) + 1
    zmax = max(by_z.items(), key=lambda kv: (kv[1], -kv[0]))
    nmax = max(by_n.items(), key=lambda kv: (kv[1], -kv[0]))
    amax = max(by_a.items(), key=lambda kv: (kv[1], -kv[0]))
    ms = members(rows)
    top = max(ms, key=lambda m: m["extra"]["B_per_A_keV"])
    return {
        "rows": len(rows),
        "measured": sum(1 for r in rows if r[6] == "M"), "estimated": sum(1 for r in rows if r[6] == "E"),
        "Z": [min(by_z), max(by_z)], "N": [min(by_n), max(by_n)], "A": [min(by_a), max(by_a)],
        "elements": len(by_z), "isotone_lines": len(by_n), "isobar_lines": len(by_a),
        "most_isotopes": {"Z": zmax[0], "count": zmax[1]},
        "most_isotones": {"N": nmax[0], "count": nmax[1]},
        "most_isobars": {"A": amax[0], "count": amax[1]},
        "most_bound": {"name": top["name"], "B_per_A_keV": top["extra"]["B_per_A_keV"]},
        "S_n_undefined": sum(1 for m in ms if m["extra"]["S_n"] is None),
        "S_p_undefined": sum(1 for m in ms if m["extra"]["S_p"] is None),
        "S_n_negative": sum(1 for m in ms if m["extra"]["S_n"] is not None and m["extra"]["S_n"] < 0),
        "S_p_negative": sum(1 for m in ms if m["extra"]["S_p"] is not None and m["extra"]["S_p"] < 0),
    }


# ----------------------------------------------------------------- the refusals

def refused(rows=None, charts=True):
    """Every candidate coordinate the table could supply, refused against a measurement.

    charts=False skips the three generic-arity charts (about a minute), leaving
    their measurements None; the verdicts do not depend on them.
    """
    rows = read() if rows is None else rows
    X = index(rows)
    h, w = cell2(X)
    c = census(rows)
    dms = [r[4] for r in rows]
    out = []
    a_chart = tz_chart = q_chart = None
    if charts:
        XA = frozenset((Z, N, Z + N) for Z, N in X)
        a_chart = {"cells": len(XA), "height": height(XA), "width": width(XA)}
        XT = frozenset((Z, N, N - Z) for Z, N in X)
        tz_chart = {"cells": len(XT), "height": height(XT), "width": width(XT)}
        XQ = frozenset((Z, N, 0 if q == "M" else 1) for Z, N, _A, _s, _d, _u, q in rows)
        q_chart = {"cells": len(XQ), "height": height(XQ), "width": width(XQ)}
    out.append({"coordinate": "A, the mass number", "verdict": "REFUSED",
                "why": "a function of the two coordinates held, A = Z + N on every row; a third axis that is the sum of the first two changes no comparison, so the chart on (Z, N, A) has the same height and width as the chart on (Z, N), and the table's own printed A was used as a check and matched on every row",
                "measurement": {"rows_with_A_equal_Z_plus_N": len(rows), "of": len(rows), "chart_ZN": {"height": h, "width": w}, "chart_ZNA": a_chart},
                "status": "DERIVED"})
    out.append({"coordinate": "T_z, the isospin projection (N − Z)/2", "verdict": "REFUSED",
                "why": "a function of the two coordinates held; as a third axis it does change the order, because N − Z can fall where Z and N both rise, but it separates no two members the chart does not already separate, and a coordinate that adds no member and no cell is a relabelling; charted anyway so the refusal is made against a number",
                "measurement": {"chart_ZN": {"cells": len(X), "height": h, "width": w}, "chart_ZN_Tz": tz_chart},
                "status": "DERIVED"})
    out.append({"coordinate": "the mass excess Δ", "verdict": "REFUSED",
                "why": "a magnitude in keV, continuous and signed, not a quantum number; every member carries it and none is placed by it",
                "measurement": {"distinct_values": len(set(dms)), "rows": len(rows), "range_keV": [min(dms), max(dms)]},
                "status": "READ"})
    out.append({"coordinate": "the quality flag (M measured, E estimated)", "verdict": "REFUSED",
                "why": "a fact about the measurement, not about the nuclide: the same nuclide would sit on the same cell under either flag; the flag rides on the member as the status of its mass and is coloured on the lattice, not charted; charted anyway so the refusal is made against a number",
                "measurement": {"measured": c["measured"], "estimated": c["estimated"], "chart_ZN_flag": q_chart},
                "status": "READ"})
    out.append({"coordinate": "the binding energy B, and B/A", "verdict": "REFUSED",
                "why": "derived from three of the table's own entries and a magnitude; it rides on every member",
                "measurement": {"formula": "B = Z Δ(¹H) + N Δ(n) − Δ(Z, N)", "most_bound": c["most_bound"]},
                "status": "DERIVED"})
    out.append({"coordinate": "the separation energies S_n and S_p (and their signs)", "verdict": "REFUSED",
                "why": "magnitudes, and not total: a separation energy is a difference with a neighbour, and where the neighbour is not in the table there is no value; a coordinate must place every member",
                "measurement": {"S_n_undefined": c["S_n_undefined"], "S_p_undefined": c["S_p_undefined"], "S_n_negative": c["S_n_negative"], "S_p_negative": c["S_p_negative"]},
                "status": "DERIVED"})
    out.append({"coordinate": "spin, parity and half-life", "verdict": "NOT HELD",
                "why": "the repository holds no NUBASE table and no level table for nuclides, so none of the three is READ anywhere here; this instrument does not invent them, and a seated table would be a new index beside this one, not a coordinate added to it",
                "measurement": {"tables_held": [AME_REL]},
                "status": "READ"})
    return out


# ------------------------------------------------------------------- the block

def block(charts=True, rows=None):
    """Everything the site carries, in one object."""
    rows = read() if rows is None else rows
    X = index(rows)
    h, hw = height2(X)
    w, ww = width2(X)
    E, dem = join_deficit(X)
    J, dem2 = join_closure(X)
    assert dem == dem2 and len(J) == len(X) + E, "the two join routes disagree"
    mE, mdem = meet_deficit(X)
    measured = md5_of()
    recorded = ledger_md5()
    ms = members(rows)
    return {
        "id": "isotopes", "title": "The isotope index: every nuclide of the mass table on (Z, N)",
        "member": "a nuclide of the 2020 atomic mass evaluation's Table I, the neutron included: the element by its proton number and the isotope by its neutron number; the nuclide's own numbers and nothing else the table prints",
        "site_own": True,
        "site_own_note": "an index of this site, built from the one nuclear table the repository holds; it is not a row of the register of seated indexes and that register's count does not include it",
        "coordinates": COORDINATES,
        "members": len(ms), "charted": len(ms), "unplaced": [], "unplaced_why": "",
        "cells": len(X), "injective": len(X) == len(ms),
        "own_cell": {"height": h, "width": w, "status": "DERIVED",
                     "note": "measured here exactly: on two coordinates the height is the longest non-decreasing run of N over the members sorted by (Z, N) and the width the longest strictly decreasing one, one member per Z, both by patience sorting"},
        "witness": {"chain": [list(c) for c in hw], "antichain": [list(a) for a in ww],
                    "chain_note": "a chain attaining the height: %d members from %s to %s, each containing the one before on both coordinates" % (h, "(%d, %d)" % hw[0], "(%d, %d)" % hw[-1]),
                    "antichain_note": "an antichain attaining the width: %d members, one per Z, N strictly falling as Z rises, no two comparable" % w},
        "demand": {"E": E, "cells": [list(c) for c in dem], "status": "DERIVED",
                   "note": "the join-closure of the chart: for every two members the cell (max Z, max N) is held, so the index demands nothing and draws no ghost; the chart of nuclides is join-closed",
                   "meet_deficit": mE, "meet_cells": [list(c) for c in mdem[:12]],
                   "meet_note": "the meet-closure asks the other corner, (min Z, min N); its deficit is a measurement of the chart's shape and is not a language's closure"},
        "rows": ms,
        "census": census(rows),
        "refused": refused(rows, charts),
        "constants": [{"symbol": "u c²", "value_keV": U_KEV, "status": U_KEV_STATUS, "source": "CODATA 2018, the value the evaluation itself uses", "meaning": "the atomic mass unit in keV; the one constant the mass in u needs"}],
        "formulas": {"mass_u": "M = A + Δ / (u c²)", "binding_keV": "B = Z Δ(¹H) + N Δ(n) − Δ(Z, N)", "separation": "S_n = B(Z, N) − B(Z, N−1); S_p = B(Z, N) − B(Z−1, N); S_2n, S_2p likewise",
                     "status": "DERIVED", "note": "over atomic mass excesses, so the electrons cancel exactly; a separation energy is None where the neighbour is not in the table"},
        "source": {"citation": CITATION, "doi": DOI, "path": AME_REL, "md5": measured, "md5_recorded": recorded, "ok": measured == recorded,
                   "columns": ["Z", "N", "A", "symbol", "mass_excess_keV", "unc_keV", "quality"], "status": "READ",
                   "note": "the published rounded table, captured from the PDF; the capture's own header records that A was recomputed as N + Z and matched the printed A on every row"},
        "instrument": "tools/isotopes.py",
    }


# ----------------------------------------------------------------- the selftest

def selftest():
    """Fixtures are the table's own census and the exact 2-D measurements. Reports, never repairs."""
    fail = 0
    print("isotopes.py --selftest   fixtures: AME2020 Table I, its ledger md5, and the exact 2-D cell")
    print()

    def chk(name, got, want):
        nonlocal fail
        ok = got == want
        fail += 0 if ok else 1
        print("  [%s] %-70s %s" % ("ok" if ok else "FAIL", name, "" if ok else "got %r want %r" % (got, want)))

    F = FIXTURES
    rows = read()
    X = index(rows)
    chk("rows: the table's row count", len(rows), F["rows"])
    chk("md5: the file is the ledger's own", (md5_of(), ledger_md5()), (F["md5"], F["md5"]))
    c = census(rows)
    chk("quality: measured and estimated", (c["measured"], c["estimated"]), (F["measured"], F["estimated"]))
    chk("ranges: Z, N, A", (tuple(c["Z"]), tuple(c["N"]), tuple(c["A"])), (F["Z"], F["N"], F["A"]))
    chk("injective: as many cells as rows", len(X), len(rows))
    h, hw = height2(X)
    w, ww = width2(X)
    chk("height, exactly, with a witness chain of that length", (h, len(hw)), (F["height"], F["height"]))
    chk("the witness chain is a chain", all(_le(hw[i], hw[i + 1]) for i in range(len(hw) - 1)), True)
    chk("width, exactly, with a witness antichain of that size", (w, len(ww)), (F["width"], F["width"]))
    chk("the witness antichain is an antichain", all(not _le(a, b) and not _le(b, a) for i, a in enumerate(ww) for b in ww[i + 1:]), True)
    # the generic-arity functions agree with the exact 2-D ones on a small chart, so a refusal's chart is measured by a checked tool
    small = frozenset((Z, N) for Z, N in X if Z <= 12)
    chk("generic height and width agree with the exact ones on Z <= 12", (height(small), width(small)), cell2(small))
    E, dem = join_deficit(X)
    J, dem2 = join_closure(X)
    chk("E: the chart is join-closed, by both routes", (E, dem == dem2, len(J) - len(X)), (F["E"], True, F["E"]))
    dm = {(Z, N): d for Z, N, _A, _s, d, _u, _q in rows}
    chk("the neutron and the proton, as the table prints them", (dm[(0, 1)], dm[(1, 0)]), (F["neutron_keV"], F["hydrogen_keV"]))
    ms = members(rows)
    c12 = next(m for m in ms if m["key"] == "C-12")
    chk("carbon 12 reconstructs to 12 u exactly", c12["extra"]["M_u"], F["carbon_12_u"])
    chk("the binding energy of the neutron and the proton is zero", (next(m for m in ms if m["key"] == "n-1")["extra"]["B_keV"], next(m for m in ms if m["key"] == "H-1")["extra"]["B_keV"]), (0.0, 0.0))
    chk("the most tightly bound nuclide, from the rows alone", (c["most_bound"]["name"], c["most_bound"]["B_per_A_keV"]), F["B_per_A_max"])
    chk("separation energies undefined where the neighbour is absent", (c["S_n_undefined"], c["S_p_undefined"]), (F["S_n_undefined"], F["S_p_undefined"]))
    d2 = next(m for m in ms if m["key"] == "H-2")
    chk("the deuteron's S_n is its binding energy", d2["extra"]["S_n"], d2["extra"]["B_keV"])
    chk("member lookup accepts 56Fe, Fe-56, Fe56 and ^56Fe", len({member(s)["key"] for s in ("56Fe", "Fe-56", "Fe56", "^56Fe")}), 1)
    print()
    print("  %d failure(s)" % fail if fail else "  all fixtures pass")
    return fail


def report(charts=False):
    b = block(charts)
    c = b["census"]
    print("isotopes.py -- %s" % b["title"])
    print("  source   %s" % b["source"]["citation"])
    print("  file     %s  md5 %s  ledger %s" % (b["source"]["path"], b["source"]["md5"][:12], "match" if b["source"]["ok"] else "DRIFT"))
    print("  members  %d, on %d cells (injective: %s)" % (b["members"], b["cells"], b["injective"]))
    print("  census   Z %s, N %s, A %s; %d measured, %d estimated" % (c["Z"], c["N"], c["A"], c["measured"], c["estimated"]))
    print("  cell     height %d, width %d (measured here, exactly); the channel K is the site build's, from the hierarchy law's operators" % (b["own_cell"]["height"], b["own_cell"]["width"]))
    print("  demand   E = %d: %s" % (b["demand"]["E"], "join-closed" if b["demand"]["E"] == 0 else "%d cells demanded" % b["demand"]["E"]))
    print("  meet     %d cells the meet-closure asks for (a shape measurement, not a closure)" % b["demand"]["meet_deficit"])
    print("  chain    %s ... %s" % (b["witness"]["chain"][0], b["witness"]["chain"][-1]))
    print("  antichain %s" % " ".join("(%d,%d)" % tuple(a) for a in b["witness"]["antichain"]))
    print("  most bound %s at %.3f keV per nucleon; S_n undefined on %d, S_p on %d" % (c["most_bound"]["name"], c["most_bound"]["B_per_A_keV"], c["S_n_undefined"], c["S_p_undefined"]))
    print("  refused  %d candidate coordinates, each against a measurement%s" % (len(b["refused"]), "" if charts else " (the three generic charts skipped; --charts runs them)"))
    for r in b["refused"]:
        print("    %-52s %s" % (r["coordinate"], r["verdict"]))
    print("  %s" % b["site_own_note"])


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--json", action="store_true", help="print the whole block")
    ap.add_argument("--charts", action="store_true", help="also measure the three refused charts (about a minute)")
    ap.add_argument("--member", help="one member: 56Fe, Fe-56, ^56Fe")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    if a.member:
        m = member(a.member)
        if m is None:
            print("no such nuclide in the table: %s" % a.member)
            return 1
        print(json.dumps(m, indent=1, ensure_ascii=False))
        return 0
    if a.json:
        b = block(a.charts)
        print(json.dumps(b, ensure_ascii=False))
        return 0
    report(a.charts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
