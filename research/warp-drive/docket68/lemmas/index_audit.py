#!/usr/bin/env python3
"""index_audit.py -- every cypher index the open rows' instruments build, audited for what item 208 found in the ring's:
a coordinate that is a KEY (it individuates every cell; register 1356, forbidden as an axis) and a ONE-HOT code (two or more
two-valued coordinates with exactly one 'high' value in every cell: one distinction spread over several coordinates).  On
such an index a refusal or an admission is forced by how the index is built, not by the question.  Item 211 ("Keep moving
the open questions through the cypher"); computed by running each instrument's compute() with tools/cypher.py's Index
recorded (read only); not seated; 2026-10-10.

  A1 (computed) the indexes are recorded as the instruments build them -- no instrument is edited; the audit hooks the
     loader so each fresh copy of tools/cypher.py records its Index calls
  A2 (computed) KEYED -- a coordinate individuates every cell, so any verdict turning on a value only one cell holds is
     forced: z3b_cypher (ray_class), far_cypher (model, in its seven-coordinate indexes), g2_between (reading and g_ratio,
     on three and four cells), corridor_shape S6 (carrier and sufficient, on two and three cells), rim_readme (config,
     kind, meeting)
  A3 (computed) REDUNDANT -- two-valued coordinates carrying one distinction between them (a duplicate or complementary
     pair, or a one-hot code): far_cypher, g2_between, corridor_shape, forming_rim F7 and rim_profile P6 (phase with
     through_hold, and nec_t), m1x_cypher (beyond, z_p2, regular), close_cypher (side with ends_horizon), m1_cypher
     (b_exclusive with d_no_added, in its control), m1p2_cypher (WRITE with ARRIVAL), rim_readme, b5p_cypher.  This is
     "too much information" (item 208) in the cypher's own sense; a verdict is forced by it only where the tested cell
     breaks the group's pattern, which each instrument's target decides
  A4 (computed) CLEAN of both: arrival_cypher, write_cypher, close_object, b5b_cypher
  A5 (READ, the records) what each keyed verdict informed: Z3b (OPEN on the physics since item 208), FAR (OPEN), H2tx
     (DERIVED on g2_between's computations G3-G4, not on its cypher step G5), M1's record (corrected on item 208).  No
     seated status rests on a forced verdict alone: the keyed verdicts are void as evidence and are marked so in their
     instruments; no status moves
Imports the instruments and tools/cypher.py by path, read only.  Stdlib (+ whatever the instruments import).
python3 index_audit.py [--selftest | --mutants]
"""
import contextlib
import importlib.machinery
import importlib.util
import io
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
MUT = {}
LOG = []
CURRENT = [""]
AUDITED = ["z3b_cypher", "far_cypher", "g2_between", "corridor_shape", "forming_rim", "rim_profile", "m1x_cypher",
           "arrival_cypher", "write_cypher", "close_cypher", "close_object", "b5b_cypher", "m1_cypher", "m1p2_cypher",
           "rim_readme", "b5p_cypher"]
EXPECT_KEYED = {"z3b_cypher": {"ray_class"}, "far_cypher": {"model"}, "g2_between": {"reading", "g_ratio"},
                "corridor_shape": {"carrier", "sufficient"}, "rim_readme": {"config", "kind", "meeting"}}
EXPECT_REDUNDANT = {"far_cypher", "g2_between", "corridor_shape", "forming_rim", "rim_profile", "m1x_cypher",
                    "close_cypher", "m1_cypher", "m1p2_cypher", "rim_readme", "b5p_cypher"}
# what each KEYED verdict informed (READ from warptheorem.py's records), and what that row's status rests on
INFORMS = {"z3b_cypher": ("Z3b", "OPEN on the physics (item 208), not on the cypher"), "far_cypher": ("FAR", "OPEN"),
           "g2_between": ("H2tx", "DERIVED on g2_between G3-G4, not on its G5"),
           "corridor_shape": ("M1", "record corrected on item 208"), "rim_readme": ("M1", "record corrected on item 208")}
_installed = []


def _install():
    if _installed:
        return
    orig = importlib.machinery.SourceFileLoader.exec_module

    def exec_module(self, module):
        orig(self, module)
        if getattr(module, "__file__", "").endswith(os.path.join("tools", "cypher.py")) and hasattr(module, "Index") \
                and not getattr(module.Index, "_audited", False):
            init = module.Index.__init__

            def recorded(ix, name, coords, cells, *a, **k):
                init(ix, name, coords, cells, *a, **k)
                LOG.append((CURRENT[0], name, list(coords), [tuple(c) for c in cells]))
            module.Index.__init__ = recorded
            module.Index._audited = True
    importlib.machinery.SourceFileLoader.exec_module = exec_module
    _installed.append(True)


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def audit_index(coords, cells):
    cl = sorted(set(cells))
    d = len(coords)
    vals = [sorted({c[i] for c in cl}, key=str) for i in range(d)]
    keys = [coords[i] for i in range(d) if len(vals[i]) == len(cl) and len(cl) > 1 and not MUT.get("ignore_keys")]
    code = [{v: r for r, v in enumerate(vals[i])} for i in range(d)]
    coded = [tuple(code[i][c[i]] for i in range(d)) for c in cl]
    bins = [i for i in range(d) if len(vals[i]) == 2]
    onehot = []
    if not MUT.get("onehot_off"):
        for k in range(2, min(5, len(bins)) + 1):
            for S in itertools.combinations(bins, k):
                for flip in itertools.product((0, 1), repeat=k):     # either value may be the 'high' one
                    if all(sum((c[i] if f == 0 else 1 - c[i]) for i, f in zip(S, flip)) == 1 for c in coded):
                        onehot.append(tuple(coords[i] for i in S))
                        break
    return {"cells": len(cl), "d": d, "keys": keys, "onehot": sorted(set(onehot))}


def run():
    _install()
    out = {}
    for f in AUDITED:
        CURRENT[0] = f
        n0 = len(LOG)
        try:
            m = _load(os.path.join(HERE, f + ".py"), "ia_" + f)
            with contextlib.redirect_stdout(io.StringIO()):
                m.compute()
        except Exception as ex:
            out[f] = {"error": "%s: %s" % (type(ex).__name__, ex)}
            continue
        seen, raw = set(), []
        for (_, name, coords, cells) in LOG[n0:]:
            k = (name, tuple(coords), tuple(sorted(set(cells))))
            if k in seen:
                continue
            seen.add(k)
            raw.append((name, coords, cells))
        out[f] = {"raw": raw}
    return out


def summarise(audit):
    out = {}
    for f, v in audit.items():
        if "error" in v:
            out[f] = v
            continue
        res = [dict(audit_index(coords, cells), name=name, coords=coords) for name, coords, cells in v["raw"]]
        out[f] = {"indexes": res, "keys": sorted({x for r in res for x in r["keys"]}),
                  "onehot": sorted({g for r in res for g in r["onehot"]})}
    return out


def compute():
    return {"raw": run()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    a = summarise(d["raw"])
    add("A1 every audited instrument ran and its indexes were recorded", all("error" not in v and v["indexes"]
                                                                             for v in a.values()))
    keyed = {f for f, v in a.items() if v.get("keys")}
    add("A2 KEYED (a coordinate individuates every cell; register 1356): z3b_cypher (ray_class), far_cypher (model), "
        "g2_between (reading, g_ratio), corridor_shape S6 (carrier, sufficient), rim_readme (config, kind, meeting) -- and "
        "no other; every verdict that turns on a keyed value is forced",
        keyed == set(EXPECT_KEYED) and all(EXPECT_KEYED[f] <= set(a[f]["keys"]) for f in EXPECT_KEYED))
    red = {f for f, v in a.items() if v.get("onehot")}
    add("A3 REDUNDANT groups (two-valued coordinates with exactly one 'high' per cell, either value high -- a duplicate or "
        "complementary pair, or a one-hot code): far, g2_between, corridor_shape, forming_rim F7 and rim_profile P6 "
        "(phase with through_hold), m1x (beyond, z_p2, regular), close_cypher, m1_cypher, m1p2, rim_readme, b5p -- a "
        "verdict is forced only where the tested cell breaks the group's pattern", red == EXPECT_REDUNDANT
        and any(set(g) >= {"phase", "through_hold"} for g in a["forming_rim"]["onehot"])
        and any(set(g) == {"beyond", "z_p2", "regular"} for g in a["m1x_cypher"]["onehot"]))
    clean = [f for f in AUDITED if f not in keyed | red]
    add("A4 clean of both: arrival_cypher, write_cypher, close_object, b5b_cypher; b5p's main index is six cells over "
        "eight coordinates", sorted(clean) == sorted(["arrival_cypher", "write_cypher", "close_object", "b5b_cypher"])
        and any(r["cells"] == 6 and r["d"] == 8 for r in a["b5p_cypher"]["indexes"]))
    add("A5 every keyed instrument informs a row whose status does not rest on the forced verdict alone (records READ): "
        "Z3b, FAR, H2tx, M1 -- the forced verdicts are void as evidence; no status moves", set(INFORMS) == keyed)
    return res


MUTANTS = {"ignore_keys": "keys not detected", "onehot_off": "one-hot codes not detected"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    d = compute()                                                  # run once; the mutants re-audit the recorded cells
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        failed = [n.split()[0] for n, ok in checks(d) if not ok]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-12s %-30s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("index_audit.py -- keys and one-hot codes in the open rows' cypher indexes (item 211)\n")
    for f, v in summarise(d["raw"]).items():
        if "error" in v:
            print("%-15s ERROR %s" % (f, v["error"]))
            continue
        print("%-15s indexes %3d  keys %s  one-hot %s  informs %s" % (f, len(v["indexes"]), v["keys"] or "-",
                                                                     v["onehot"] or "-", INFORMS.get(f, ("-",))[0]))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
