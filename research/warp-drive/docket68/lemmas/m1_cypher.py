#!/usr/bin/env python3
"""m1_cypher.py -- M1, the plane's reading of the corridor's mouth, clause by clause through the cypher (M: "Let's put M1
through the cypher next"; computed by import, deduced; flat limit; static; not verified by a separate session; not
seated; 2026-10-10).

M1 as F1-AUDIT.md states it: an ell in the window and a static five-dimensional spacetime B with (M1-a) a vacuum bulk;
(M1-b) the corridor exclusive to the bulk, B bounded by our plane P1 and, in the bridge form, position 2's piece P2;
(M1-c) on P1, within the reach, the induced metric eq. (17) at r0 = 2m to an order; (M1-d) no added matter on P1 (the
board's reading H-OWN-MATTER-ONLY: the RS tension and our universe's matter only); (M1-e) regular -- no curvature
singularity in B's closure, a smooth Killing horizon tangent to P1; (M1-f) P2 admissible -- positive, NEC net per ray.
F1-AUDIT D1 named what decides it: a P2 hypersurface below the static bulk's singular surface, with an admissible stress.

  M1 (computed, imported) within one universe the board now has a candidate for D1: the symmetric junction (202, 203)
     -- P1 at y = 0, the corridor at depth Y(r), P2 its mirror at 2Y -- with the marginal corridor of corridor_shape.py
     (corrected, S0-S3), its throat joint (rim_profile P4b), and the rim balanced by a ring in the Z2 double cover
     (forming_rim F0, F3b (ii)).  Clause by clause:
     (a) the bulk on each side is eq. (17)'s static vacuum bulk (b4_static.py's series; the bank corridor_shape reads)
     (b) the corridor stays in the bulk, Y > 0, from the throat to its rim at 3.4-5.3m, meeting the planes only along its
         edge there (rim_profile P4)
     (c) P1 reads eq. (17) by construction: the bulk is eq. (17)'s own static bulk
     (e) B's closure, from P1 to P2 at 2Y, lies inside b4_static's verified layer (y_top) at every radius of every
         member, by 0.21-1.88m, the curvature finite there (|K| <= 89); the corridor flattens into the throat (P4b);
         the horizon is extremal and smooth (O2)
     (f) P2 within one universe carries our tension (202: the same values), positive, and a crossing ray picks up
         sigma sin a >= 0 (TS)
     balance: a ring of lambda = a sigma (1 - cos theta)(1 + 2 cos theta) > 0 at the rim (0.013-0.10 a sigma)
     (d) the ring is the one thing (d) has to say about: it is neither the RS tension nor our universe's matter -- its
         surface density is of the plane's tension's order (~0.05 sigma per unit length of a), past any matter.  The
         board's reading H-RING-IS-THE-FOLD: it is the fold's own tension where our plane and position 2's piece rejoin
         -- the plane's own structure (202: "any plane has its own structure in the same fashions that we do"), not
         added matter.  Entered UNKNOWN in the index; the reading runs as the control
  M2 (cypher) the computed configurations as cells over (universe, a, b, c, d, e, f, balance), no per-cell key:
     the single plane capped on its own image (ITEM197: 8.02 sigma of added matter), the facing form between universes
     (m1x_cypher), the mirrored cuts and S15 (m1p2_cypher), the symmetric junction without a ring (balance fails, F5),
     and with the ring.  Target M1 within one universe: every clause met.  Statistics refuses it already at order 2,
     blocked by the one pair (d, balance): no computed configuration has both no added matter and a balanced rim --
     the rim balances only with the ring, and the ring is (d)'s question.  Control: (d) met for the ring cell (H-RING-IS-THE-FOLD) -- the target is data, all five admit.
     Between universes M1 stays refused (m1x_cypher's findings, unchanged)
So: within one universe M1's static existence is met in the analytic class -- every clause computed -- except (d),
which turns on what the ring at the fold is.  Proposal, for seating after this pass (206): M1 splits into M1u (within
one universe, 168's class: READING on H-RING-IS-THE-FOLD, otherwise computed) and M1x (between universes, OPEN).
[Item 207 put the ring to the cypher (ring_cypher.py): it refuses the ring's nature, and H-RING-IS-THE-FOLD is refuted
as stated -- a thin pure-tension fold carries no line tension.  So M1u would be OPEN on (d), not READING; the split
moves no row and is not seated.  The M2 control above runs the refuted reading, as a control only.  Item 208: the
positive ring itself rested on R5's -sigma at the rim; with the corridor's own tension the junction is in compression
(ring_consistent.py), so the 'balance' column's ring cell is the refuted count's.]
What it does not show, recorded: the static bulk is eq. (17)'s in the flat limit, by its series and Pade columns; the
global bulk beyond the reach (FAR, B4c) and the write (WRITE, B4d) are other inputs; F0: the rim is realised only in the
Z2 double cover.
Imports corridor_shape.py, rim_profile.py, forming_rim.py and tools/cypher.py by path; reads b4_static.json.  Stdlib +
sympy + mpmath (through corridor_shape).  python3 m1_cypher.py [--selftest | --mutants]
"""
import bisect
import contextlib
import importlib.util
import io
import itertools
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
MUT = {}
U = 2
_C = {}


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), os.path.dirname(os.path.dirname(path))]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def rp():
    if "rp" not in _C:
        _C["rp"] = _load(os.path.join(HERE, "rim_profile.py"), "m1c_rim_profile")
    return _C["rp"]


# ---------------------------------------------------------------------------------------------------------- M1
def clause_e(fam_rows):
    """B's closure (0 to 2Y) against b4_static's verified layer and curvature"""
    d = json.load(open(os.path.join(HERE, "b4_static.json")))
    dy, rs, cols = d["dy"], d["r"], d["cols"]
    rv = [eval(r) for r in rs]
    top = {r: cols[s]["top"] * dy for r, s in zip(rv, rs)}

    def j_of(r):
        return max(0, min(len(rv) - 2, bisect.bisect_right(rv, r) - 1))
    margins, kmaxes = [], []
    for rows in fam_rows.values():
        m_, k_ = 1e9, 0.0
        for (r, Y, *_rest) in rows:
            j = j_of(r)
            yt = min(top[rv[j]], top[rv[j + 1]])
            depth = 2 * Y if not MUT.get("p2_at_y") else Y
            if MUT.get("p2_deep"):
                depth = 2 * Y + 2.0
            m_ = min(m_, yt - depth)
            i = int(depth / dy) + 1
            k_ = max(k_, max(map(abs, cols[rs[j]]["K"][:i + 1])), max(map(abs, cols[rs[j + 1]]["K"][:i + 1])))
        margins.append(m_)
        kmaxes.append(k_)
    return {"margin_min": min(margins), "margin_max": max(margins), "kmax": max(kmaxes)}


def configuration():
    r = rp()
    cs, ks, bulk = r.shape()
    fam, rows = {}, {}
    for dd, s in r.FAMILY:
        R = cs.marginal(ks, bulk, dd, 0.0, s, rmax=12.0)
        rows[(dd, s)] = R["rows"]
        fam[(dd, s)] = {"rim": R["rim"], "ymin": min(x[1] for x in R["rows"]),
                        "tan": min(x[5] for x in R["rows"]), "rho": min(x[3] for x in R["rows"]),
                        "rad": min(x[4] for x in R["rows"])}
    jt = r.joint()
    e = clause_e(rows)
    rings = [v["ring"] for (m, d_, s), v in r.family(margins=(0.0,)).items()]
    return {"fam": fam, "joint": jt, "e": e, "rings": rings}


# ---------------------------------------------------------------------------------------------------------- M2
CO = ["universe", "a_vacuum", "b_exclusive", "c_trace", "d_no_added", "e_regular", "f_p2", "balance"]


def cells(conf):
    e_ok = int(conf["e"]["margin_min"] > 0 and math.isfinite(conf["e"]["kmax"]))
    b_ok = int(all(v["rim"] and v["ymin"] > 0 for v in conf["fam"].values()))
    ring_ok = int(all(x > 0 for x in conf["rings"]))
    d_ring = U if not MUT.get("decide_ring") else 1
    out = [
        (0, 1, 0, 1, 0, 1, U, U),        # one plane capped on its own image (ITEM197): 8.02 sigma added matter; no P2, no rim
        (1, 1, 1, 0, 1, 1, U, U),        # facing form between universes, P2 at -sigma/4 (m1x_cypher): mouth not read where
                                         #   positive; crossing rays on P2 not computed
        (0, 1, 1, 0, 1, 1, 1, U),        # mirrored cut, near-horizon class (m1p2_cypher CUT-NH): unequal radii
        (0, 1, 1, 1, 1, 1, 0, U),        # mirrored cut, full bulk (CUT-FULL): rho + p_r < 0 on P2
        (0, 1, 1, 1, 1, 1, 0, U),        # S15 coincidence (sim2_facing): rho_m = -2 sigma on P2
        (0, 1, b_ok, 1, 1, e_ok, 1, 0),  # symmetric junction, marginal corridor, no ring: balance fails (forming_rim F5)
        (0, 1, b_ok, 1, d_ring, e_ok, 1, ring_ok),   # the same with Z2 images and a ring (this file, M1)
    ]
    return out


def cypher(cs):
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "m1c_cypher")
    tgt_u = (0, 1, 1, 1, 1, 1, 1, 1)
    tgt_x = (1, 1, 1, 1, 1, 1, 1, 1)

    def adm(cl, lang, k=2):
        cl = sorted(set(cl))
        vo = {n: [x for x in (0, 1, U) if x in {c[i] for c in cl}] for i, n in enumerate(CO)}
        ix = cy.Index("m1", CO, [list(c) for c in cl], value_order=vo)
        out, _ = cy.ADMISSION[lang][0](ix, {"statistics_order": k} if lang == "statistics" else {})
        return None if out is None else {tuple(ix.decode[i][x[i]] for i in range(len(CO))) for x in out}

    def blocking(cl, t, k):
        return [tuple(CO[i] for i in S) for S in itertools.combinations(range(len(CO)), k)
                if not any(all(c[i] == t[i] for i in S) for c in cl)]
    refuse = None
    for k in (2, 3, 4, 5):
        if tgt_u not in (adm(cs, "statistics", k) or set()):
            refuse = k
            break
    ctrl = [c if not (c[0] == 0 and c[4] == U and c[7] == 1) else c[:4] + (1,) + c[5:] for c in cs]
    langs = ("order", "algebra", "geometry", "information", "statistics")
    return {"refuse_order": refuse, "block": blocking(cs, tgt_u, refuse) if refuse else [],
            "ctrl_all": {l: tgt_u in (adm(ctrl, l) or set()) for l in langs},
            "x_refused": tgt_x not in (adm(cs, "statistics", 2) or set()) or tgt_x not in (adm(cs, "statistics", 3) or set())}


def compute():
    conf = configuration()
    cs = cells(conf)
    return {"conf": conf, "cells": cs, "cy": cypher(cs)}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    f = d["conf"]["fam"]
    add("M1 (b) the marginal corridor stays in the bulk (Y > 0) from the throat to its rim at 3.4-5.3m, radial held at "
        "zero, tangential and energy positive (rim_profile, corrected)", all(v["rim"] and 3.39 < v["rim"] < 5.3
        and v["ymin"] > 0 and v["tan"] > 0 and v["rho"] > 0 and v["rad"] > -1e-10 for v in f.values()))
    e = d["conf"]["e"]
    add("M1 (e) B's closure, P1 to P2 at 2Y, lies inside b4_static's verified layer at every radius of every member, by "
        "0.21-1.88m, the curvature finite (|K| <= 89); the corridor flattens into the throat (P4b)",
        0.2 < e["margin_min"] < 0.25 and 1.85 < e["margin_max"] < 1.9 and e["kmax"] < 100
        and all(abs(rows[-1][2]) < 0.002 for rows in d["conf"]["joint"].values()))
    add("M1 balance: the ring's tension is positive for every member (0.013-0.10 a sigma)",
        all(0.01 < x < 0.11 for x in d["conf"]["rings"]))
    cy = d["cy"]
    add("M2 cypher: statistics refuses M1 within one universe at order 2, blocked by the one pair (d_no_added, balance) "
        "-- the rim balances only with the ring, whose nature is (d)'s", cy["refuse_order"] == 2
        and cy["block"] == [("d_no_added", "balance")])
    add("M2 control: (d) met for the ring cell (H-RING-IS-THE-FOLD) -- the target is data, admitted by all five",
        all(cy["ctrl_all"].values()))
    add("M2 between universes M1 stays refused (m1x_cypher's cells)", cy["x_refused"])
    return res


MUTANTS = {"p2_at_y": "P2 placed at the corridor's depth, not its mirror at 2Y",
           "p2_deep": "P2 placed 2m deeper (past the verified layer)",
           "decide_ring": "the ring's nature decided in code ((d) entered as met)"}


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
        print("  mutant %-12s %-54s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("m1_cypher.py -- M1 clause by clause\n")
    for k, v in d["conf"]["fam"].items():
        print("family %s: %s" % (k, v))
    print("(e)", d["conf"]["e"], " rings", ["%.3f" % x for x in d["conf"]["rings"]])
    print("cells", d["cells"])
    print("cypher", d["cy"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
