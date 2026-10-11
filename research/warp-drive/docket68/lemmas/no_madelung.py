#!/usr/bin/env python3
"""no_madelung.py -- item 219: position 2 is "a universe where the madelung exceptions didn't exist. That is the principle
difference between ours and theirs, all other differences are built from that condition."  Computed on the record's own
element data -- register 1306's observed ground configurations (method/members/LW1-ground.py, imported read-only) and
the Register's lattice (registers 11, 49, 66, 67) -- with M's Löwdin solution (method/members/THE-LOWDIN-SOLUTION-2.md,
read-only) and tools/cypher.py; worked in the conversation; seated under 206; 2026-10-11.

  N1 (computed) "the Madelung exceptions" has three readings on register 1306's data, and the record uses all three:
     configurations -- 20 elements whose observed ground configuration is not the (n + l, n) aufbau one (Cr Cu Nb Mo Ru
     Rh Pd Ag La Ce Gd Pt Au Ac Th Pa U Np Cm Lr); channel openings -- 2 of 19 (La opens 5d before 4f, Ac 6d before 5f:
     register 1307); the differentiating electron -- exactly 3, La, Ac and Th, entering d while the f channel of equal
     n + l has never been opened.  The last is M's paper's own count ("except at exactly three elements, La (Z=57), Ac
     (Z=89), and Th (Z=90)"); the primary rule (smaller n + l first) holds at every element in all three
  N2 (computed) position 2's table: M's chain (the paper's algorithm, cfg(Z) = cfg(Z-1) + one electron in the entrant)
     with every entrant the (n + l, n) channel is the Madelung aufbau table exactly, and the configuration reading gives
     the same table.  Its shape is ours: the first s openings are at Z = 1, 3, 11, 19, 37, 55, 87 in both, period
     lengths 2, 8, 8, 18, 18, 32, 32, and the period x group cells are the cypher's own fixture (90 cells) in both -- so
     the periodic-table index (E = 36; 100/0/24 at three coordinates) is the same cell for both universes
  N3 (computed) the Method's lattice (registers 11, 12: 630 = 180 void + 240 reactive + 92 reserved + 118 occupied):
     the SAME 118 cells in both universes -- an order ideal (register 66), 19 columns saturated and 6 empty (register 67)
     -- and the cypher gives the same E on it (order 38, algebra 38, geometry 0, information 38, statistics(2) 0).  They
     differ only in which element sits in which cell.  Register 49 states 28 inversions against (n + l, n, k) and
     tau = 0.992, caused by "the known lanthanide and actinide irregularities"; the labelling La 5d1, Ce-Lu 4f1-14, Ac
     6d1, Th-Lr 5f1-14 reproduces both exactly (tau = 6847/6903) -- RECONSTRUCTED, since the Register gives the count
     and the cause, not the table.  M's chain has 42 (tau = 2273/2301); position 2 has 0 (tau = 1).  Each exception
     costs exactly 14 = 2(2*3 + 1) inversions
  N4 (computed) the labelling as an index, (Madelung rank, Z), through the cypher: position 2 closes in all four
     lattice languages (E = 0 -- its labelling is a chain); ours (register 49) gives order 238, algebra 238, geometry
     1054, information 28; M's chain 267, 267, 1102, 42.  Information's E is the inversion count in each
  N5 (computed) on the observed configurations (Z = 1-108): ours occupies 98 cells, not an order ideal (197 violations,
     5 gapped subshells, 6 elements dropping a subshell), cypher order 58, algebra 58, geometry 14, information 56, and
     statistics(2) over-reaches by 8 (3d4 4d3 4d6 4d9 4f2 5f1 5f5 7p2); position 2 occupies 108 -- one new cell per
     element -- an order ideal with no gap and no drop, statistics(2) E = 0, geometry 2, order/algebra/information 48.
     208's audit: no key and no one-hot group in either
  N6 (computed, then deduced) built from that condition: M's chain is causal in Z (step Z reads only cfg(Z-1)).  With
     the three exceptions and without, the chains differ at exactly 29 elements, Z = 57-70 and 89-103, and meet again
     exactly at Lu (71) and Rf (104), where f completes; nothing below Z = 57 changes.  So the eight configuration
     anomalies below La (Cr Cu Nb Mo Ru Rh Pd Ag) cannot be built from a condition at the f openings, and M's paper
     classes the d-block anomalies as "total-energy rearrangements within an already-opened block", not exceptions
     to the rule (READ).  M's "all other differences are built from that condition" fits the differentiating-electron
     reading, where the one condition is the paper's own mechanism: orbital collapse at the first f openings -- in
     position 2 the f channel is collapsed and deeper than d at Z = 57 and Z = 89.  The board's reading (a) of 219
     (the configurations) is kept on record and computed (N1, N5); under it the condition is twenty conditions, eight
     of them below La, which the chain cannot build from one.  A single condition of the other kind -- a different
     constant in the equation -- would reach every Z; the paper's two values of c (ours, and c -> infinity) both keep
     La, Ac and Th (READ), so neither is position 2
  N7 (deduced) by the warp theory's defining values -- sigma and the offset (201), G, ell, the README mass m -- position
     2 differs in nothing: the theory computes none of them from an electron configuration.  In the bulk index the two positions are the
     same cell; telling them apart needs the labelling as a coordinate, as 218 needed cosmic time
So position 2's precise values, for this experiment: the Madelung table (every element in its (n + l, n) cell, tau = 1,
opening sequence 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p); the same periodic table, the same lattice of
118 cells, the same E in every language; different ground configurations at 29 elements (57-70, 89-103) in M's chain,
listed by the report, and none elsewhere.
What this does not show: no field is computed here.  What physical difference makes the collapse come first is not
computed here -- M's paper enters one constant, c = 137.035999, and READS that with c taken to infinity eleven entrants
change (Mn Zn Ag Cd Nd Pm Sm Lu Hg Lr Rf) and La, Ac, Th do not, so position 2 is not ours with relativity removed.
(Item 220: the chain was since rebuilt from the chats and the question computed -- madelung_field.py: no value of c
removes La's and Ac's exceptions; Th's goes above c of about 164.  The paper's eleven-element c -> infinity list is
drawn from a walk the record itself voided, F54.2/F59.3 -- madelung_field.py F7 -- so it is READ here as the paper's
statement, not as a measurement.)  Position 2's ground-state
rearrangements at Z >= 57 (Ce Gd Pt Au Pa U Np Cm Lr in ours) are not computable here.  An object holding elements of
Z = 57-70 or 89-103 would have other ground states at position 2, and so a mass differing at the binding-energy level;
the theory's m is given, not built from composition, and does not carry that.  The ell-orderings test of
tools/orderideal.py (a RECONSTRUCTED convention) gives 2 of 120 on the 118 cells; register 66 states no such count
(register 68's 120 counts down-sets of the column poset).
Imports LW1-ground.py, tools/orderideal.py, tools/cypher.py and index_audit.py by path; reads the paper, the main bundle
and the rulings file (read-only).  Stdlib.  python3 no_madelung.py [--selftest | --mutants]
"""
import contextlib
import fractions
import importlib.util
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
PAPER = os.path.join(ROOT, "method", "members", "THE-LOWDIN-SOLUTION-2.md")
MAIN = os.path.join(ROOT, "method", "The_Method_1_6_BUILD90_main_and_register.md")
MUT = {}
L = "spdfg"
M219 = ("Let's consider position 2 universe where the madelung exceptions didn't exist. That is the principle difference "
        "between ours and theirs, all other differences are built from that condition. My Löwdin challenge work may be "
        "very helpful here")
PAPER_Q = ["except at exactly three elements, La (Z=57), Ac (Z=89), and Th (Z=90)",
           "the d-block anomalies are total-energy rearrangements *within* an already-opened block",
           "They disagree at eleven elements: Mn, Zn, Ag, Cd, Nd, Pm, Sm, Lu, Hg, Lr, and Rf.",
           "cfg(Z)     := cfg(Z−1) + one electron in entrant(Z)"]
REG_Q = ["180 VOID · 240 REACTIVE · 92 RESERVED · 118 OCCUPIED", "Kendall τ = 0.992; the 28 inversions",
         "19 SATURATED, 6 EMPTY, NONE PARTIAL", "DOWNWARD CLOSED WITHOUT EXCEPTION",
         "DIFFERS FROM MADELUNG AT TWO OF NINETEEN"]
EXC = {57: (5, 2), 89: (6, 2), 90: (6, 2)}           # M's paper's three: the entrant takes d
LANGS = ("order", "algebra", "geometry", "information")


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


SUBS = sorted([(n, l) for n in range(1, 9) for l in range(0, min(n, 5))], key=lambda t: (t[0] + t[1], t[0]))
CAP = lambda s: 2 * (2 * s[1] + 1)


def aufbau(Z):
    out, left = {}, Z
    for s in SUBS:
        if left <= 0:
            break
        out[s] = min(left, CAP(s))
        left -= out[s]
    return out


def chain(zmax, exc):
    """M's algorithm (paper II.2): cfg(Z) = cfg(Z-1) + one electron in entrant(Z).  The entrant is the first
    (n + l, n) channel with room, except where exc names it.  Returns (configurations, differentiating cells)."""
    cfg, cfgs, cells = {}, {}, {}
    for Z in range(1, zmax + 1):
        ent = exc.get(Z) or next(s for s in SUBS if cfg.get(s, 0) < CAP(s))
        cfg = dict(cfg)
        cfg[ent] = cfg.get(ent, 0) + 1
        cfgs[Z], cells[Z] = cfg, (ent[0], ent[1], cfg[ent])
    return cfgs, cells


def inversions(cells):
    zs = sorted(cells, key=lambda Z: (cells[Z][0] + cells[Z][1], cells[Z][0], cells[Z][2]))
    return sum(1 for i in range(len(zs)) for j in range(i + 1, len(zs)) if zs[i] > zs[j])


def compute():
    g = _load(os.path.join(ROOT, "method", "members", "LW1-ground.py"), "nm_lw1")
    oi = _load(os.path.join(ROOT, "tools", "orderideal.py"), "nm_oi")
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "nm_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "nm_ia")
    obs = {Z: {(n, l): o for n, l, o in g.expand(Z)} for Z in g.GROUND}
    d = {"counts": sum(g.occ_count(Z) == Z for Z in g.GROUND)}
    # N1 three readings
    d["config_exc"] = [g.GROUND[Z][0] for Z in sorted(obs) if obs[Z] != aufbau(Z)]
    opened, prev, tb, c1, first = set(), {}, [], [], []
    for Z in range(1, 109):
        cur = obs[Z]
        for s in [k for k in cur if cur[k] > prev.get(k, 0)]:
            if s not in opened:
                first.append(s)
            for t in SUBS:
                never = t not in opened if not MUT.get("tb_currently_empty") else prev.get(t, 0) == 0
                if t[0] + t[1] == s[0] + s[1] and t[0] < s[0] and never and t in aufbau(108):
                    tb.append(g.GROUND[Z][0])
                if t[0] + t[1] < s[0] + s[1] and t not in opened and t in aufbau(108):
                    c1.append((Z, s, t))
        opened |= set(cur)
        prev = cur
    madel = SUBS[:len(first)]
    d["tb"] = sorted(set(tb), key=lambda e: [g.GROUND[Z][0] for Z in g.GROUND].index(e))
    d["clause1"] = c1
    d["openings"] = ["%d%s" % (s[0], L[s[1]]) for s in first]
    d["open_diff"] = [i for i in range(len(first)) if first[i] != madel[i]]
    # N2 position 2's table
    exc = dict(EXC)
    p2cfg, p2cell = chain(118, {} if not MUT.get("p2_keeps_la") else {57: (5, 2)})
    ourcfg, ourcell = chain(118, exc)
    d["p2_is_aufbau"] = all(p2cfg[Z] == aufbau(Z) for Z in range(1, 109))
    sopen = lambda f: [Z for Z in range(1, 109) if any(l == 0 and (n, l) not in f(Z - 1) for (n, l) in f(Z))]
    d["s_open_p2"] = sopen(lambda Z: p2cfg.get(Z, {}))
    d["s_open_ours"] = [Z for Z in range(1, 109) if any(l == 0 and (n, l) not in set().union(*[set(obs[y]) for y in range(1, Z)] or [set()]) for (n, l) in obs[Z])]

    def pg(c):
        n, l, k = c
        if (n, l, k) == (1, 0, 2):
            return (1, 18)                            # He in group 18, the fixture's convention
        return {0: (n, k), 1: (n, 12 + k), 2: (n + 1, 2 + k)}.get(l)
    fx = cy._periodic()
    inv0 = [{v: k for k, v in fx.code[i].items()} for i in range(2)]
    fixture = sorted(tuple(inv0[i][c[i]] for i in range(2)) for c in fx.cells)
    reg = dict(p2cell)
    reg[57] = (5, 2, 1) if not MUT.get("reg_la_f") else (4, 3, 1)
    if not MUT.get("reg_la_f"):
        for i, Z in enumerate(range(58, 72)):
            reg[Z] = (4, 3, i + 1)
    reg[89] = (6, 2, 1)
    for i, Z in enumerate(range(90, 104)):
        reg[Z] = (5, 3, i + 1)
    labs = {"p2": p2cell, "register": reg, "chain": ourcell}
    d["pg_equal_fixture"] = {k: sorted({pg(c) for c in v.values() if pg(c)}) == fixture for k, v in labs.items()}
    # N3 the lattice
    lat = {k: set(v.values()) for k, v in labs.items()}
    d["lat_same"] = lat["p2"] == lat["register"] == lat["chain"] and len(lat["p2"]) == 118
    box = [(n, l, k) for n in range(1, 8) for l in range(5) for k in range(1, 19)]
    d["census"] = (sum(l >= n for n, l, k in box), sum(l < n and k > 2 * (2 * l + 1) for n, l, k in box),
                   sum(oi.admissible(n, l, k) for n, l, k in box) - len(lat["p2"]), len(lat["p2"]))
    d["lat_ideal"] = len(oi.ideal_violations(lat["p2"]))
    cols = {}
    for n, l, k in lat["p2"]:
        cols[(n, l)] = max(cols.get((n, l), 0), k)
    adm_cols = [(n, l) for n in range(1, 8) for l in range(5) if l < n]
    d["columns"] = (sum(cols.get(c, 0) == CAP(c) for c in adm_cols), sum(c not in cols for c in adm_cols),
                    sum(0 < cols.get(c, 0) < CAP(c) for c in adm_cols))
    d["lat_lord"] = len(oi.l_orderings(lat["p2"]))

    def E(coords, cells):
        ix = cy.Index("nm", coords, [list(c) for c in cells])
        out = {}
        for l in LANGS:
            a, _ = cy.ADMISSION[l][0](ix, {})
            out[l] = None if a is None else len(a) - len(cells)
        if len(coords) == 3:
            a, _ = cy.op_statistics(ix, {"statistics_order": 2})
            out["statistics2"] = len(a) - len(cells)
            inv = [{v: k for k, v in ix.code[i].items()} for i in range(3)]
            out["stat2_over"] = sorted({tuple(inv[i][c[i]] for i in range(3)) for c in a} - set(cells))
        return out
    d["lat_E"] = E(["n", "l", "k"], sorted(lat["p2"]))
    d["inv"] = {k: inversions(v) for k, v in labs.items()}
    d["tau"] = {k: fractions.Fraction(6903 - 2 * v, 6903) for k, v in d["inv"].items()}
    # N4 the labelling as an index
    rank = {c: Z for Z, c in p2cell.items()}
    d["lab_E"] = {k: E(["madelung_rank", "Z"], sorted((rank[c], Z) for Z, c in v.items())) for k, v in labs.items()}
    # N5 observed sets
    obs_cells = sorted({(n, l, o) for Z in obs for (n, l), o in obs[Z].items()})
    p2_cells = sorted({(n, l, o) for Z in range(1, 109) for (n, l), o in p2cfg[Z].items()})

    class _G:
        pass
    gp = _G()
    gp.GROUND = g.GROUND
    gp.expand = lambda Z: [(n, l, o) for (n, l), o in sorted(p2cfg[Z].items(), key=lambda t: (sum(t[0]), t[0][0]))]
    d["obs"] = {"cells": len(obs_cells), "viol": len(oi.ideal_violations(set(obs_cells))),
                "holes": len(oi.holes(set(obs_cells))), "drops": len(oi.z_linear_extension(g)),
                "E": E(["n", "l", "k"], obs_cells), "audit": ia.audit_index(["n", "l", "k"], obs_cells)}
    d["p2obs"] = {"cells": len(p2_cells), "viol": len(oi.ideal_violations(set(p2_cells))),
                  "holes": len(oi.holes(set(p2_cells))), "drops": len(oi.z_linear_extension(gp)),
                  "E": E(["n", "l", "k"], p2_cells), "audit": ia.audit_index(["n", "l", "k"], p2_cells)}
    # N6 built from the condition
    diff = [Z for Z in range(1, 119) if ourcfg[Z] != p2cfg[Z]]
    d["diff"] = diff
    d["meet"] = [Z for Z in (71, 104) if ourcfg[Z] == p2cfg[Z] and ourcfg[Z - 1] != p2cfg[Z - 1]]
    d["p2_cfgs"] = {Z: (g.GROUND[Z][0] if Z in g.GROUND else str(Z), ourcfg[Z], p2cfg[Z]) for Z in diff if Z <= 108}
    d["below_la"] = [e for e in d["config_exc"] if [Z for Z in g.GROUND if g.GROUND[Z][0] == e][0] < 57]
    return d


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rulings = open(os.path.join(os.path.dirname(HERE), "M-RULINGS-2026-10-03.md"), encoding="utf-8").read().replace("\n    ", " ")
    paper = open(PAPER, encoding="utf-8").read()
    main = open(MAIN, encoding="utf-8").read()
    add("N0 M's 219 verbatim in the rulings file; the paper's three exceptions, its d-block reading, its c -> infinity "
        "list and its chain step verbatim; registers 11, 49, 66, 67, 1307 verbatim; 108/108 electron counts (1306)",
        M219 in rulings and all(q in paper for q in PAPER_Q) and all(q in main for q in REG_Q) and d["counts"] == 108)
    add("N1 three readings: 20 configuration exceptions; first openings differ from Madelung at 2 of 19 (La 5d, Ac 6d: "
        "register 1307); the differentiating electron at exactly La, Ac, Th (M's paper's three); primary rule unbroken",
        len(d["config_exc"]) == 20 and len(d["openings"]) == 19 and len(d["open_diff"]) == 4
        and d["tb"] == ["La", "Ac", "Th"] and not d["clause1"])
    add("N2 position 2's table is the Madelung aufbau table (M's chain, no exception); first s openings 1 3 11 19 37 55 "
        "87 in both; period x group cells equal the cypher's fixture in both (one periodic-table cell)",
        d["p2_is_aufbau"] and d["s_open_p2"] == d["s_open_ours"] == [1, 3, 11, 19, 37, 55, 87]
        and all(d["pg_equal_fixture"].values()))
    e = d["lat_E"]
    add("N3 the Method's lattice: the same 118 cells in both (180 void, 240 reactive, 92 reserved; an order ideal; 19 "
        "columns saturated, 6 empty, none partial); cypher E order 38, algebra 38, geometry 0, information 38, "
        "statistics(2) 0; inversions 28 (register 49, tau = 6847/6903), 42 (M's chain), 0 (position 2)",
        d["lat_same"] and d["census"] == (180, 240, 92, 118) and d["lat_ideal"] == 0 and d["columns"] == (19, 6, 0)
        and (e["order"], e["algebra"], e["geometry"], e["information"], e["statistics2"]) == (38, 38, 0, 38, 0)
        and d["inv"] == {"p2": 0, "register": 28, "chain": 42}
        and d["tau"]["register"] == fractions.Fraction(6847, 6903) and round(float(d["tau"]["register"]), 3) == 0.992)
    lab = {k: tuple(v[l] for l in LANGS) for k, v in d["lab_E"].items()}
    add("N4 the labelling (Madelung rank, Z) through the cypher: position 2 E = 0 in all four lattice languages; "
        "register 49's 238/238/1054/28; M's chain 267/267/1102/42 (information = inversions)",
        lab == {"p2": (0, 0, 0, 0), "register": (238, 238, 1054, 28), "chain": (267, 267, 1102, 42)})
    o, p = d["obs"], d["p2obs"]
    add("N5 observed configurations: ours 98 cells, 197 violations, 5 gaps, 6 drops, cypher 58/58/14/56, statistics(2) "
        "over-reach 8; position 2 108 cells, an order ideal, no gap, no drop, 48/48/2/48, statistics(2) 0; no key or "
        "one-hot in either", (o["cells"], o["viol"], o["holes"], o["drops"]) == (98, 197, 5, 6)
        and tuple(o["E"][l] for l in LANGS) == (58, 58, 14, 56) and o["E"]["statistics2"] == 8
        and (p["cells"], p["viol"], p["holes"], p["drops"]) == (108, 0, 0, 0)
        and tuple(p["E"][l] for l in LANGS) == (48, 48, 2, 48) and p["E"]["statistics2"] == 0
        and not o["audit"]["keys"] and not o["audit"]["onehot"] and not p["audit"]["keys"] and not p["audit"]["onehot"])
    add("N6 built from the condition: the chains differ at exactly 29 elements, Z = 57-70 and 89-103, meeting again at Lu "
        "and Rf; nothing below 57 changes, so the eight anomalies below La are not built from it",
        d["diff"] == list(range(57, 71)) + list(range(89, 104)) and d["meet"] == [71, 104]
        and d["below_la"] == ["Cr", "Cu", "Nb", "Mo", "Ru", "Rh", "Pd", "Ag"])
    return res


MUTANTS = {"tb_currently_empty": "tie-break read as 'smaller-n channel empty now' (counts Lr: 6d emptied at No)",
           "p2_keeps_la": "position 2 built with La's exception kept",
           "reg_la_f": "register 49's labelling entered with La in 4f (no lanthanide irregularity)"}


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
        print("  mutant %-18s %-78s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def fmt(a, b):
    """the subshells whose occupancy differs between two configurations"""
    keys = sorted(set(a) | set(b), key=lambda t: (sum(t), t[0]))
    show = lambda c: " ".join("%d%s%d" % (n, L[l], c[(n, l)]) for (n, l) in keys if c.get((n, l), 0) != (a if c is b else b).get((n, l), 0) and c.get((n, l), 0))
    return show(a) or "-", show(b) or "-"


def report(d):
    print("no_madelung.py -- position 2 without the Madelung exceptions (item 219)\n")
    print("N1 configuration exceptions (%d): %s" % (len(d["config_exc"]), " ".join(d["config_exc"])))
    print("   first openings: %s  (differ from Madelung at positions %s)" % (" ".join(d["openings"]), d["open_diff"]))
    print("   differentiating-electron exceptions: %s   primary-rule violations: %d" % (d["tb"], len(d["clause1"])))
    print("N2 position 2 = aufbau: %s; first s openings %s; period x group = fixture %s" % (d["p2_is_aufbau"], d["s_open_p2"], d["pg_equal_fixture"]))
    print("N3 lattice: same 118 cells %s; census (void, reactive, reserved, occupied) %s; ideal violations %d; columns "
          "(saturated, empty, partial) %s; l-orderings %d of 120" % (d["lat_same"], d["census"], d["lat_ideal"], d["columns"], d["lat_lord"]))
    print("   cypher on the 118 cells: %s" % {k: v for k, v in d["lat_E"].items() if k != "stat2_over"})
    print("   inversions against (n+l, n, k): %s   tau: %s" % (d["inv"], {k: str(v) for k, v in d["tau"].items()}))
    print("N4 labelling index (Madelung rank, Z): %s" % d["lab_E"])
    for k in ("obs", "p2obs"):
        o = d[k]
        print("N5 %-5s cells %d, violations %d, gaps %d, drops %d, E %s, over-reach %s" % (
            "ours" if k == "obs" else "p2", o["cells"], o["viol"], o["holes"], o["drops"],
            {l: o["E"][l] for l in LANGS + ("statistics2",)}, ["%d%s%d" % (n, L[l], kk) for n, l, kk in o["E"]["stat2_over"]]))
    print("N6 M's chain, ours vs position 2: differ at %d elements (%d-%d, %d-%d), meet again at %s; anomalies below La: %s"
          % (len(d["diff"]), d["diff"][0], 70, 89, 103, d["meet"], " ".join(d["below_la"])))
    print("   where they differ, the subshells that differ (M's chain, ours -> position 2):")
    for Z, (el, a, b) in d["p2_cfgs"].items():
        print("     %3d %-2s  %-10s -> %s" % ((Z, el) + fmt(a, b)))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
