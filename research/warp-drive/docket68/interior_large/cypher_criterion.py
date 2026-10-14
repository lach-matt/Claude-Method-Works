"""cypher_criterion.py -- item 412: the cypher run over 405-3's cells.

M, 412: "Have the cypher run over it".  The cells are criterion_large.py's: one requirement at one node of one slice,
with a verdict -- violated (its quantity <= 0), undecided (its measured error at least its size) or decided.  Three
indexes go to tools/cypher.py, every roster it holds (which roster applies is the open docket 20x-04/20x-09, so none
is picked), with the declared witness the board's instruments give analysis:
  INSIDE  -- the large hole's interior over the first half, item 411's cells: the error is the two meshes'
             disagreement plus the two static starts' (coordinates slice, node, requirement, verdict);
  OUTSIDE -- the control: the record's static solution outside the horizon (s = 0.1, 0.25, 0.5, 0.75), judged by the
             same four requirements, its error the N = 24 and N = 28 solutions' disagreement.  Outside, s is spacelike
             and the static direction timelike, so (a) N^2 > 0 and (b) g_tt > 0 must fail there: the control flips;
  BOTH    -- the two together, with region as a coordinate and the node dropped (the regions' grids differ).
Beside the cypher's verdicts, logic's binary (b6p_scale.determined, imported by path, never copied) asks which
coordinates fix the verdict.  The law: inside, the verdict is one value (every cell decided) and is fixed by nothing;
outside, it is fixed by the requirement; together, by region and requirement.

python3 cypher_criterion.py              -- the three indexes through the cypher; CYPHER-412.json
python3 cypher_criterion.py --selftest | --mutants
"""
import sys, os, json, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CYPHER_PATH = os.path.join(HERE, "..", "..", "..", "..", "tools", "cypher.py")
B6P_PATH = os.path.join(HERE, "..", "lemmas", "b6p_scale.py")
CY_OPTS = {"statistics_order": 2, "algebra_budget": 20000}
OUT_SLICES = (0.1, 0.25, 0.5, 0.75)
VERDICTS = ["violated", "undecided", "decided"]
MUT = set()
_C = {}


def _load(path, name):
    if name not in _C:
        spec = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(spec)
        sys.modules[name] = m; spec.loader.exec_module(m); _C[name] = m
    return _C[name]


def verdict(q, err):
    if q <= 0:
        return "violated"
    return "undecided" if err >= abs(q) else "decided"


def inside_cells():
    import criterion_large as K, zeno_run as Z, deturck_exact as D, mpmath as mp
    R5, I5 = K.scheme(K.FIFTH); R4, I4 = K.scheme(K.FOURTH); Rb, Ib = K.scheme(K.FROM28); xs = I5.xn; cells = []
    for sv in K.SLICES:
        X5 = K.at(R5, I5, sv)[0]; X4, Xs4, _ = K.at(R4, I4, sv); Xb = K.at(Rb, Ib, sv)[0]
        parts = D.parts_of(I4, X4, Xs4); X4i = np.zeros_like(X5)
        for j, xv in enumerate(xs):
            p = next(pp for pp in parts if pp["lo"] - 1e-12 <= xv <= pp["hi"] + 1e-12)
            for e, n in enumerate(D.NAMES):
                X4i[e, j] = float(D.poly_at(p["nodes"], p["w"], p["vals"][n], mp.mpf(xv))[0])
        q5, q4, qb = (K.quantities(sv, xs, X, Z.B) for X in (X5, X4i, Xb))
        for r in K.REQS:
            err = np.abs(q5[r] - q4[r]) + np.abs(q5[r] - qb[r])
            for j in range(len(xs)):
                cells.append(["%.2f" % sv, "%d" % j, r, verdict(q5[r][j], err[j])])
    return cells


def outside_cells():
    import criterion_large as K, core_fw as C
    U24, U28 = np.load(os.path.join(HERE, C.static_file(1.0, 24, 24))), np.load(os.path.join(HERE,
                                                                                       C.static_file(1.0, 28, 28)))
    xs = C.lobatto01(24)[1:]                                       # the N = 24 x-nodes off the axis
    def fields(U, N, sv):
        n = (N + 1) ** 2; sn, xn = C.radau01(N), C.lobatto01(N)
        return np.array([C.bary_interp(xn, C.bary_interp(sn, U[e * n:(e + 1) * n].reshape(N + 1, N + 1), [sv])[0],
                                       xs).ravel() for e in range(5)])
    cells = []
    for sv in OUT_SLICES:
        qa = K.quantities(sv, xs, fields(U24, 24, sv), 1.0); qb = K.quantities(sv, xs, fields(U28, 28, sv), 1.0)
        for r in K.REQS:
            err = np.abs(qa[r] - qb[r])
            for j in range(len(xs)):
                v = verdict(qa[r][j], err[j])
                if "flipcontrol" in MUT and r in ("N2", "gtt"):
                    v = "decided"
                cells.append(["%.2f" % sv, "%d" % j, r, v])
    return cells


def run_index(title, coords, cells, rosters=None):
    cy = _load(CYPHER_PATH, "cc_cypher")
    vo = {c: sorted({cl[i] for cl in cells}, key=(lambda v: VERDICTS.index(v)) if c == "verdict" else
                    ((lambda v: ["N2", "gtt", "S", "B"].index(v)) if c == "requirement" else
                     ((lambda v: ["inside", "outside"].index(v)) if c == "region" else float)))
          for i, c in enumerate(coords)}
    out = {"index": title, "coords": coords, "cells": len(cells), "rosters": {}}
    rows = keys = None
    for rn in (rosters or sorted(cy.ROSTERS)):
        ix = cy.Index(title, coords, cells, vo, {"analysis": {"speaks": True,
                                                         "witness": "item 405-3's sign conditions"}})
        res = cy.run(ix, rn, CY_OPTS); rows, keys = cy.coordinate_report(ix)
        out["rosters"][rn] = {"verdicts": [{"language": v.language, "state": v.state, "admitted": v.admitted, "E": v.E}
                                           for v in res["_verdicts"]],
                              "agree": res["languages_agree"], "all_E_zero": res["all_E_zero"],
                              "degenerate": res["degenerate"], "bearing": res["operator_bearing_measured"]}
    out["adds_nothing"] = [r["coordinate"] for r in rows if r["adds_nothing"]]
    out["keys"] = keys
    return out


def fixes(cells, coords, target="verdict"):
    det = _load(B6P_PATH, "cc_b6p").determined
    cands = [[], ["requirement"], ["region"], ["region", "requirement"], ["slice", "requirement"],
             ["slice", "node", "requirement"]]
    return {"+".join(b) or "nothing": det(cells, coords, b, target) for b in cands if all(c in coords for c in b)}


def compute(quiet=False):
    ins = inside_cells(); outs = outside_cells()
    c4 = ["slice", "node", "requirement", "verdict"]
    # BOTH drops the node: the two regions' grids differ (96 nodes inside, 24 outside), and a box over both alphabets
    # demands cells that neither grid has -- an artifact of the grids, not a finding (measured: E > 0 with it kept)
    c5 = ["region", "slice", "requirement", "verdict"]
    both = sorted({("inside", c[0], c[2], c[3]) for c in ins} | {("outside", c[0], c[2], c[3]) for c in outs})
    both = [list(c) for c in both]
    if "keepnode" in MUT:
        c5 = ["region"] + c4; both = [["inside"] + c for c in ins] + [["outside"] + c for c in outs]
    res = {}
    for title, coords, cells in (("INSIDE", c4, ins), ("OUTSIDE", c4, outs), ("BOTH", c5, both)):
        r = run_index(title, coords, cells)
        r["verdict_counts"] = {v: sum(1 for c in cells if c[-1] == v) for v in VERDICTS}
        r["fixed_by"] = fixes(cells, coords)
        if title == "OUTSIDE":
            r["by_requirement"] = {q: sorted({c[3] for c in cells if c[2] == q}) for q in ("N2", "gtt", "S", "B")}
        res[title] = r
        if not quiet:
            print("%s: %d cells, verdicts %s; the verdict fixed by %s; adds nothing: %s" % (
                title, r["cells"], r["verdict_counts"], ", ".join(k for k, v in r["fixed_by"].items() if v) or "none",
                ", ".join(r["adds_nothing"]) or "none"), flush=True)
            if title == "OUTSIDE":
                print("    by requirement: %s" % r["by_requirement"], flush=True)
            for rn, rr in r["rosters"].items():
                print("    roster %-5s %s; languages agree: %s; all E = 0: %s" % (
                    rn, "  ".join("%s %s%s" % (v["language"], v["state"], "" if v["E"] is None else " E=%d" % v["E"])
                                 for v in rr["verdicts"]), rr["agree"], rr["all_E_zero"]), flush=True)
    return res


def run():
    res = compute()
    json.dump(res, open(os.path.join(HERE, "CYPHER-412.json"), "w"), indent=1, default=str)
    return res


# ---------------------------------------------------------------------------------------------- selftest / mutants
def selftest(quiet=False):
    ok = []
    def say(m):
        if not quiet:
            print(m, flush=True)
    res = compute(quiet=True); I, O, B = res["INSIDE"], res["OUTSIDE"], res["BOTH"]
    k1 = I["verdict_counts"] == {"violated": 0, "undecided": 0, "decided": 3456} and "verdict" in I["adds_nothing"]
    k1 = k1 and B["cells"] == 52
    ok.append(k1); say("K1 inside: all 3,456 cells decided, the verdict a coordinate that adds nothing: %s" % k1)
    k2 = (O["by_requirement"]["N2"] == ["violated"] and O["by_requirement"]["gtt"] == ["violated"]
          and O["by_requirement"]["S"] == ["decided"] and O["by_requirement"]["B"] == ["decided"])
    ok.append(k2); say("K2 the control flips: outside, (a) and (b) violated at every cell, S and B decided: %s" % k2)
    k3 = (I["fixed_by"]["nothing"] and not O["fixed_by"]["nothing"] and O["fixed_by"]["requirement"]
          and not B["fixed_by"]["requirement"] and B["fixed_by"]["region+requirement"])
    ok.append(k3); say("K3 logic's binary: the verdict fixed by nothing inside, by the requirement outside, by region "
                       "and requirement together: %s" % k3)
    k4 = all(rr["all_E_zero"] in (True, None) for rr in I["rosters"].values())
    ok.append(k4); say("K4 every speaking language of every roster has E = 0 on the inside index: %s" % k4)
    return all(ok)


def mutants():
    caught = 0; names = ["flipcontrol", "keepnode"]
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-12s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    run()
