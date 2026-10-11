#!/usr/bin/env python3
"""ledger_cypher.py -- item 238: which reading of the closing energy holds at the build, asked of the cypher.  M: "This is
a question to put to the cypher".  Worked in the conversation (computed, exact where marked; deduced where marked; not
verified by a separate session; not seated); 2026-10-11.

The readings.  P2: the build at position 2 uses the closing energy read with position 2's own G, E1(G2) sqrt(N).  P1: it
uses the energy read and defined at position 1, E1(G1) sqrt(N) (230).  ONE: one value read from both sides (111 (b)),
which makes E1(G2) = E1(G1), so position 2's G is ours for any README.

The decision rule, fixed before the run (L0): each reading is entered as cells, one per position-2 G (x 1/2, x 1, x 2,
at the ledger's bound for the example README, x 2^100) and per README size (T3's 600-bit control, the example), over four
computed attributes -- the rulings the cell keeps: 111 (a) (no sink: the energy at the build is at most the assembly
ceiling A), one value (111 (b) and 230: what position 2 absorbs equals what position 1 read), 226 (position 2 keeps its
own G), 237 (the reading bounds weak gravity).  The cypher selects a reading if exactly one reading holds the target
(every ruling kept) at the example README; failing that, if exactly one reading comes nearest (fewest rulings broken).
Otherwise it narrows to the nearest and names the rulings that conflict.

  L0 (read) M's item-238 words, verbatim in the rulings file.
  L1 (computed, exact) The energies: E1(G) sqrt(N) at each G; the ledger's bound G2 >= G N / N*0 with N*0 = (A / E1)^2 =
     676.28 bits -- 0.887 G for T3's 600-bit control, 4.055e12 G for the example README.
  L2 (computed) The cells.  At 600 bits every ruling can be kept: P2 and ONE at position 2's G = ours hold the target --
     the conflict is the example's size, as T3 found.  At the example README no cell holds it.
  L3 (computed; the cypher, roster 1173, audited) At the example README the rulings that no held cell keeps together are
     111 (a) and the one value (111 (b), 230): the no-sink build and the one value read at both sides -- T3's pull.  The
     nearest readings break one ruling each: P2 (at or above the bound) breaks the one value; ONE (and P2) at position
     2's G = ours break 111 (a).  P1 breaks two (111 (a), 237).  Every operator-bearing language's verdict on the target
     is reported with the audit.
  L4 (decision, by L0) No reading holds the target and two come nearest, so the cypher narrows: P1 is out (it breaks
     two, and leaves weak gravity unbounded, against 237); the choice between P2 and ONE is the choice between 111 (a)
     and the one value.  At the example README the cypher does not decide it: order, algebra and information admit the
     target, geometry and statistics refuse it (five cells, no key, no one-hot code).
  L5 (deduced from L2) What each leaves of position 2 for the example README.  ONE keeps the one value by fixing
     position 2's G at ours: a destination of 2a's kind (the matter law changed, G unchanged), with T3's absorber at
     the build.  P2 keeps the no-sink build by putting position 2's G at or above 4.055e12 x ours: none of 2a-2P's own
     addresses, though every such universe is like 2a-2P in 229's defining sense.  At position 2's G = ours the two are
     the same cell.

What this does not show.
  - A is T3's ceiling for the example's core; the bound scales as N / N*0 with it.
  - The attributes are the rulings' computable content; 230's "if it is not already contained" and 111 (b)'s
    entanglement are not entered beyond the one-value reading.

Imports wbound.py (and through it bulk5_index.py, p2_gravity.py), tools/cypher.py and index_audit.py by path.  Stdlib.
python3 ledger_cypher.py [--selftest | --mutants]
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
M238 = '"This is a question to put to the cypher"'
LANGS = ("order", "algebra", "geometry", "information", "statistics")
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
RULES = ["no_sink_111a", "one_value_111b_230", "own_G_226", "bounded_237"]


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


WB = _load(os.path.join(HERE, "wbound.py"), "lc_wb")
PG = WB.PG
A = PG.ASSEMBLY_MAX_J
E1_OURS = PG.corridor(PG.G)["E1"]
NSTAR0 = (A / E1_OURS) ** 2
READMES = {"600-bit control": 600, "example": WB.EXAMPLE_N}


def e_at(gratio, N):
    """the closing energy E1(G) sqrt(N) at G = gratio x ours (E1 ~ G^-1/2, exact)"""
    return E1_OURS * gratio ** -0.5 * math.sqrt(N)


def g_classes(N):
    bound = N / NSTAR0
    return {"x 1/2": 0.5, "x 1": 1.0, "x 2": 2.0, "at the bound": WB.ledger(N=N)["ratio"], "x 2^100": 2.0 ** 100}, bound


def cell(reading, gratio, N):
    """the four rulings this reading keeps at position-2 G = gratio x ours and README size N"""
    e1 = e_at(1.0, N)
    if reading == "P1":
        e_build, own = e1, 1
    elif reading == "P2":
        e_build, own = e_at(gratio, N), 1
    else:                                                # ONE: E1(G2) = E1(G1) forces G2 = ours
        e_build, own = e1, int(abs(gratio - 1.0) < 1e-12)
    no_sink = int(e_build <= A * (1 + 1e-12))
    one_value = int(abs(e_build / e1 - 1) < 1e-12)
    if MUT.get("one_value_ignored"):
        one_value = 1
    bounded = int(reading in ("P2", "ONE"))
    return (no_sink, one_value, own, bounded)


def build():
    rows = {}
    for nname, N in READMES.items():
        classes, bound = g_classes(N)
        for reading in ("P1", "P2", "ONE"):
            for cname, gr in classes.items():
                rows[(nname, reading, cname)] = cell(reading, gr, N)
    return rows


def conflicts(cells):
    """pairs of rulings no held cell keeps together"""
    return sorted((RULES[a], RULES[b]) for a, b in itertools.combinations(range(4), 2)
                  if not any(c[a] == 1 and c[b] == 1 for c in cells))


def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "lc_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "lc_ia")
    rows = build()
    out = dict(rows=rows, nstar0=NSTAR0, bounds={n: g_classes(N)[1] for n, N in READMES.items()})
    for nname in READMES:
        sub = {k: v for k, v in rows.items() if k[0] == nname}
        held = sorted(set(sub.values()))
        target = (1, 1, 1, 1)
        holders = sorted({k[1] for k, v in sub.items() if v == target})
        dist = {r: min(4 - sum(v) for k, v in sub.items() if k[1] == r) for r in ("P1", "P2", "ONE")}
        broken = {r: sorted({RULES[x] for k, v in sub.items() if k[1] == r and 4 - sum(v) == dist[r] for x in range(4)
                             if v[x] == 0}) for r in dist}
        res = dict(held=held, holders=holders, dist=dist, broken=broken, conflicts=conflicts(held))
        if len(held) >= 2:
            ix = cy.Index("ledger_" + nname.replace(" ", "_"), RULES, [list(c) for c in held])
            adm = {}
            for lg in LANGS:
                a, _ = cy.ADMISSION[lg][0](ix, dict(OPTS))
                adm[lg] = None if a is None else (tuple(ix.code[x][1] for x in range(4)) in a
                                                  if all(1 in ix.code[x] for x in range(4)) else False)
            res.update(target_admitted=adm, run=cy.run(ix, "1173", dict(OPTS)), audit=ia.audit_index(RULES, held))
        out[nname] = res
    ex = out["example"]
    nearest = [r for r, d in ex["dist"].items() if d == min(ex["dist"].values())]
    out["decision"] = (ex["holders"][0] if len(ex["holders"]) == 1 else
                       (nearest[0] if len(nearest) == 1 else "narrowed to " + " and ".join(sorted(nearest))))
    return out


def report(o):
    print("ledger_cypher.py -- which reading of the closing energy holds at the build (item 238)\n")
    print("L1 N*0 = %.2f bits; the ledger's bound G2/G >= %s" % (o["nstar0"], {n: "%.4g" % b for n, b in o["bounds"].items()}))
    print("\nL2 cells (no sink 111a, one value 111b/230, own G 226, bounded 237):")
    for k, v in o["rows"].items():
        print("  %-16s %-4s %-13s %s" % (k[0], k[1], k[2], v))
    for n in READMES:
        r = o[n]
        print("\nL3 %s: target held by %s; nearest (rulings broken): %s %s; conflicting pairs %s" % (
            n, r["holders"], r["dist"], r["broken"], r["conflicts"]))
        if "run" in r:
            print("   target admitted per language: %s" % r["target_admitted"])
            print("   roster 1173: %s; audit %s" % ("; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"])
                                                        for v in r["run"]["verdicts"]), r["audit"]))
    print("\nL4 decision by L0's rule: %s" % o["decision"])


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("L0 M's item-238 words verbatim in the rulings file", M238 in rul)
    ok = "%.2f" % o["nstar0"] == "676.28" and "%.3f" % o["bounds"]["600-bit control"] == "0.887"
    ok &= "%.4g" % o["bounds"]["example"] == "4.055e+12"
    add("L1 N*0 = 676.28 bits; the bound G N / N*0 = 0.887 G at 600 bits, 4.055e12 G at the example", ok)
    c6 = o["600-bit control"]
    ok = c6["holders"] == ["ONE", "P2"] and o["example"]["holders"] == []
    add("L2 at 600 bits P2 and ONE (at position 2's G = ours) hold every ruling; at the example no cell does", ok)
    ex = o["example"]
    ok = ex["conflicts"] == [("no_sink_111a", "one_value_111b_230")]
    ok &= ex["dist"] == {"P1": 2, "P2": 1, "ONE": 1}
    ok &= ex["broken"]["P1"] == ["bounded_237", "no_sink_111a"] and set(ex["broken"]["P2"]) == {"no_sink_111a",
                                                                                              "one_value_111b_230"}
    ok &= ex["broken"]["ONE"] == ["no_sink_111a"]
    add("L3 at the example the one conflicting pair is 111 (a) with the one value (T3's pull); P2 and ONE break one ruling "
        "each, P1 two (111 (a), 237)", ok)
    ok = o["decision"] == "narrowed to ONE and P2" and "run" in ex and bool(ex["run"]["verdicts"])
    add("L4 by L0's rule: no reading holds the target, two come nearest -- narrowed to P2 and ONE; P1 out", ok)
    return res


MUTANTS = {"one_value_ignored": "the one value read as always kept (111 (b), 230 dropped)"}


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
        print("  mutant %-18s %-56s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
