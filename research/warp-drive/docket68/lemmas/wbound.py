#!/usr/bin/env python3
"""wbound.py -- item 237: the missing bound on weak gravity, sought in the record; item 233's region redrawn with it and
items 234-235 re-run.  M chose: "A bound is missing" ("Something bounds weak gravity that the theorem's conditions don't
yet state.").  Worked in the conversation (computed, exact where marked; READ where marked; deduced where marked; not
verified by a separate session; not seated); 2026-10-11.

  Z0 (read) M's item-237 answer, verbatim in the rulings file.
  Z1 (computed, exact) The open direction of item 233 is the 2P step: along it every Planck-unit quantity is unchanged
     -- sigma/sigma_P, N_max, ell/l5 -- and only matter-against-gravity comparisons move: G itself against matter's
     fixed scale (alpha_G), the README's energy in SI (E1 ~ G^-1/2), and the ledger's no-sink README size N* ~ G.  A
     bound on weak gravity must be one of those comparisons.
  Z2 (computed; each candidate the record holds) Which bounds the open direction: the README's capacity, the corridor
     inside the bulk's curvature (the top), the table-top floor, the throat's density against the tension (item 236
     R4) and the existence of bodies do not -- each is flat along the 2P step or bounds the other side; the stock's
     stars are not a condition (136 H: the stock is multi-universal).  One does: the energy ledger read at position 2.
     The build uses "that and only that which is provided by the closing" (111 (a)); the build's need is matter-scale,
     at most T3's assembly ceiling A = 1.1947e10 J for the example's core; the closing energy read with position 2's G
     is E1(G2) sqrt(N), and E1 ~ G^-1/2.  So G2 >= N h c^5 ln 2 / (8 pi^2 A^2) (exact): for the example README (N =
     2742570311524972, E = 2.405878e16 J at ours) G2 >= 4.055362e12 G, 41.883 doublings above ours.  The record already
     reads the ledger this way per position (p2_gravity's N* = (A / E1(G_u))^2).
  Z3 (computed) With the bound the plausible region is finite: 21274 lattice universes per law under the relative floor,
     7239 under the absolute; position 2's G between 2^41.883 and the ceiling (2^196.885 / 2^98.443) times ours.
  Z4 (computed) Items 234 and 235 re-run on the bounded region.  234's rule: the unweighted count is now a probability,
     so (i) fails -- UNWEIGHTED: no weighting is needed.  The statistics language's maximum entropy with nothing but the
     support is uniform; position 2's address under it: log2 G = 111.71 +- 44.15 (relative) or 67.87 +- 16.31
     (absolute); with the window share 93.30 +- 36.62 / 60.48 +- 13.42.  The record's G-weights still normalise and
     still press position 2 to the ceiling, but nothing now requires them.
  Z5 (computed; the matter law, an illustration) The bound falls as A^-2, and A is the build's matter-scale need, so the
     matter law moves it: for an object of one metal, whose need scales with its cohesive energy, position 2's minimum G
     moves by x 0.878 / 1.424 (Cu, min / mirror), x 0.540 / 1.976 (Ag), x 0.604 / 0.752 (Au).  Through the ledger the
     matter law sets the floor under position 2's G -- the link to item 236: matter governs the bound on G, not G.
  Z6 (computed; the cypher, roster 1173, audited) The candidates as cells over (moves along the open direction, sourced
     in the record, bounds weak gravity, rests on a reading not yet ruled).  The target -- a sourced condition that
     bounds the open direction -- is held by the ledger alone.  The index has four cells and the audit finds one-hot
     codes in it, so the languages' verdicts here are void as evidence (211): the table is the finding, Z1-Z2 decide.
  Z7 (deduced; for M) The ledger bounds G2 only if the closing energy at the build is read with position 2's G -- as
     p2_gravity reads N* per position, and as 111 (b)'s "one energy read from two sides" allows.  Item 230 has the energy
     "read/defined at position 1": read with our G it is 2.406e16 J whatever G2 is, the ledger bounds nothing, and T3's
     sink stays.  The rulings pull both ways; the reading is M's.

A correction to item 235's reading, recorded and not repaired: item 229 defines "like 2a-2P" by its parenthesis --
tension and offset not negative, ordinary matter -- which every plausible universe meets; weight_address.py A4 took the
destination as 2a-2P's own addresses, a narrower reading than 229's text.  Under the text, every universe in the bounded
region is a destination like 2a-2P; 2a-2P's own addresses (G at most x 4) lie below the bound for the example README.

What this does not show.
  - A is T3's ceiling for the example's 70 kg core (11.11 eV per atom, generous); a real build's need is not computed,
    so 4.055e12 is the bound at that ceiling (a larger need lowers it as A^-2).
  - Z5 scales A by a pure metal's cohesive energy; the example's core is not a metal.
  - The bound is per README: G2_min grows with N.

Imports bulk5_index.py (and through it p2_planck.py, p2_gravity.py), p2_matter.py, tools/cypher.py and index_audit.py by
path.  Stdlib.  python3 wbound.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M237 = 'M chose: "A bound is missing"'
M111 = "that and only that which is provided by the closing of the horizon."
M230 = "the energy being read/defined at position 1 can be absorbed by position 2"
EXAMPLE_N = 2742570311524972
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


B5 = _load(os.path.join(HERE, "bulk5_index.py"), "wb_b5")
PG = B5.PG
K = B5.constants()
W = K["W"]


# ================================================================================ Z1 the open direction
def z1():
    e0, ej = B5.exps(1, F(1)), B5.exps(2, F(1, 4))          # one 2P step: (g, s) = (1, -2)
    move = {k: ej[k] - e0[k] for k in e0}
    return dict(move=move, flat=sorted(k for k, v in move.items() if v == 0),
                moving=sorted(k for k, v in move.items() if v != 0))


# ================================================================================ Z2 the ledger bound
def ledger(N=EXAMPLE_N, A=None):
    A = PG.ASSEMBLY_MAX_J if A is None else A
    E1 = PG.corridor(PG.G)["E1"]
    E0 = E1 * math.sqrt(N)
    ratio = (E0 / A) ** 2
    if MUT.get("ledger_power"):
        ratio = E0 / A
    exact = N * PG.H * PG.C ** 5 * math.log(2) / (8 * math.pi ** 2 * A ** 2) / PG.G
    return dict(E0=E0, A=A, ratio=ratio, gmin=math.log2(ratio), exact=exact, nstar0=(A / E1) ** 2)


CANDIDATES = {
    # name: (j-coefficient of the quantity it bounds, the side it bounds, sourced in the record, reading needed)
    "capacity": ("N_max", None, 1, 0),
    "top": ("sigma_planck", None, 1, 0),
    "table-top floor": ("sigma", "above", 1, 0),             # it moves along the 2P step but bounds the other side
    "throat density (236 R4)": ("N_max", None, 1, 0),        # rho_E / 2 sigma ~ 2^(-2i): the same flat j-coefficient
    "bodies exist": (None, "none", 1, 0),
    "stock's stars": (None, "not a condition", 0, 0),
    "ledger at position 2": ("G", "below", 1, 1),
}


def z2(mv):
    rows = {}
    for name, (q, side, src, reading) in CANDIDATES.items():
        moves = int(q is not None and mv["move"][q] != 0)
        bounds = int(moves == 1 and side == "below")
        if MUT.get("capacity_bounds") and name == "capacity":
            bounds, moves = 1, 1
        rows[name] = dict(moves=moves, sourced=src, bounds=bounds, reading=reading)
    return rows


# ================================================================================ Z3, Z4 the bounded region
def region(gmin, floor, span=400):
    return [(i, j) for i in range(-span, int(W // 2) + 2) for j in range(-span, int(W) + 2)
            if B5.w_interval(i, j, K, floor) and i + j >= gmin]


def ensemble(pts, floor, weighted):
    ws = [B5.weight(i, j, K, floor) if weighted else 1.0 for i, j in pts]
    Z = sum(ws)
    mean = lambda f: sum(f(i, j) * w for (i, j), w in zip(pts, ws)) / Z
    sd = lambda f: math.sqrt(sum((f(i, j) - mean(f)) ** 2 * w for (i, j), w in zip(pts, ws)) / Z)
    g = lambda i, j: i + j
    return dict(logG=(mean(g), sd(g)), n=len(pts))


def z34(gmin):
    out = {}
    for floor in ("rel", "abs"):
        pts = region(gmin, floor)
        edge = any(i == -400 or j == -400 for i, j in pts)
        out[floor] = dict(n=len(pts), finite=not edge, gmax=max(i + j for i, j in pts), gmin_cell=min(i + j for i, j in pts),
                          uniform=ensemble(pts, floor, False), share=ensemble(pts, floor, True))
    # item 234's rule re-run: (i) is there an unweighted probability? on a finite region, yes
    out["verdict_234"] = "UNWEIGHTED" if out["rel"]["finite"] and out["abs"]["finite"] else "WEIGHTED"
    return out


# ================================================================================ Z5 the matter law moves the bound
def z5():
    pm = _load(os.path.join(HERE, "p2_matter.py"), "wb_pm")
    o = pm.compute()
    out = {}
    for el in ("Cu", "Ag", "Au"):
        e = {l: o["sol"][(el, l)]["Ecoh"] for l in ("ours", "min", "mirror")}
        out[el] = {l: (e["ours"] / e[l]) ** 2 for l in ("min", "mirror")}
    return out


# ================================================================================ Z6 the cypher
def z6(cy, ia, rows):
    cells = {}
    for n, r in rows.items():
        cells.setdefault((r["moves"], r["sourced"], r["bounds"], r["reading"]), []).append(n)
    coords = ["moves_open_direction", "sourced", "bounds_weak_gravity", "reading_unruled"]
    held = sorted(cells)
    ix = cy.Index("wbound", coords, [list(c) for c in held])
    holders = sorted(n for c, ns in cells.items() if c[0] == 1 and c[1] == 1 and c[2] == 1 for n in ns)
    return dict(cells=cells, holders=holders, run=cy.run(ix, "1173", dict(OPTS)), audit=ia.audit_index(coords, held))


# ================================================================================ compute, report
def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "wb_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "wb_ia")
    mv = z1()
    led = ledger()
    rows = z2(mv)
    return dict(z1=mv, led=led, rows=rows, reg=z34(led["gmin"]), z5=z5(), z6=z6(cy, ia, rows))


def report(o):
    print("wbound.py -- the missing bound on weak gravity (item 237)\n")
    print("Z1 one 2P step moves: %s; leaves flat: %s" % ({k: str(v) for k, v in o["z1"]["move"].items() if v != 0},
                                                         o["z1"]["flat"]))
    l = o["led"]
    print("\nZ2 the ledger at position 2: E %.6e J at ours, A %.4e J -> G2 >= %.6e G (exact form %.6e), %.3f doublings; "
          "N* at ours %.2f bits" % (l["E0"], l["A"], l["ratio"], l["exact"], l["gmin"], l["nstar0"]))
    for n, r in o["rows"].items():
        print("  %-26s moves %d  sourced %d  bounds weak gravity %d  reading unruled %d" % (n, r["moves"], r["sourced"],
                                                                                       r["bounds"], r["reading"]))
    g = o["reg"]
    for f in ("rel", "abs"):
        r = g[f]
        print("\nZ3/Z4 %s: %d universes per law (finite %s); log2 G from %d to %d; uniform %.2f +- %.2f; with the share "
              "%.2f +- %.2f" % (f, r["n"], r["finite"], r["gmin_cell"], r["gmax"], *r["uniform"]["logG"], *r["share"]["logG"]))
    print("   item 234's rule re-run: %s" % g["verdict_234"])
    print("\nZ5 position 2's minimum G under the law, against ours (one-metal object): %s" % {
        el: {l: "%.3f" % v for l, v in d.items()} for el, d in o["z5"].items()})
    c = o["z6"]
    print("\nZ6 the cypher: target held by %s; cells %s" % (c["holders"], {str(k): v for k, v in c["cells"].items()}))
    print("   roster 1173: %s; audit %s" % ("; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"])
                                                    for v in c["run"]["verdicts"]), c["audit"]))


# ================================================================================ checks
def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("Z0 M's item-237 answer verbatim in the rulings file; 111 (a) and 230's words present", M237 in rul and M111 in rul
        and M230 in rul)
    mv = o["z1"]["move"]
    ok = mv["sigma_planck"] == 0 and mv["N_max"] == 0 and mv["ell_l5"] == 0 and mv["G"] == 1 and mv["E1"] == F(-1, 2)
    add("Z1 a 2P step leaves sigma/sigma_P, N_max, ell/l5 flat and moves G (x 2) and E1 (x 2^-1/2)", ok)
    l = o["led"]
    ok = "%.6e" % l["ratio"] == "4.055362e+12" and "%.3f" % l["gmin"] == "41.883" and abs(l["exact"] / l["ratio"] - 1) < 1e-9
    ok &= "%.2f" % l["nstar0"] == "676.28" and "%.6e" % l["E0"] == "2.405878e+16"
    holders = sorted(n for n, r in o["rows"].items() if r["moves"] and r["sourced"] and r["bounds"])
    ok &= holders == ["ledger at position 2"]
    add("Z2 of the record's candidates only the ledger at position 2 bounds the open direction: G2 >= 4.055362e12 G "
        "(41.883 doublings; N h c^5 ln 2 / (8 pi^2 A^2) to 1e-9); N* at ours 676.28 bits", ok)
    g = o["reg"]
    ok = g["rel"]["finite"] and g["abs"]["finite"] and (g["rel"]["n"], g["abs"]["n"]) == (21274, 7239)
    ok &= g["rel"]["gmin_cell"] == 42 and g["rel"]["gmax"] == 196 and g["abs"]["gmax"] == 98
    add("Z3 the bounded region is finite: 21274 universes per law (relative), 7239 (absolute); log2 G from 42 to 196 / 98",
        ok)
    ok = g["verdict_234"] == "UNWEIGHTED"
    ok &= ["%.2f" % v for v in g["rel"]["uniform"]["logG"] + g["abs"]["uniform"]["logG"]] == ["111.71", "44.15", "67.87",
                                                                                              "16.31"]
    add("Z4 item 234's rule on the bounded region: UNWEIGHTED; uniform position 2: log2 G 111.71 +- 44.15 (relative), "
        "67.87 +- 16.31 (absolute)", ok)
    z = o["z5"]
    ok = ["%.3f" % z[el][lw] for el in ("Cu", "Ag", "Au") for lw in ("min", "mirror")] == [
        "0.878", "1.424", "0.540", "1.976", "0.604", "0.752"]
    add("Z5 the matter law moves the floor under position 2's G (one-metal object): Cu x 0.878 / 1.424, Ag x 0.540 / "
        "1.976, Au x 0.604 / 0.752", ok)
    c = o["z6"]
    ok = c["holders"] == ["ledger at position 2"] and bool(c["run"]["verdicts"]) and len(c["cells"]) == 4
    ok &= bool(c["audit"]["onehot"]) and not c["audit"]["keys"]
    ok &= o["rows"]["table-top floor"]["moves"] == 1 and o["rows"]["table-top floor"]["bounds"] == 0
    add("Z6 the cypher (run and audited): the target held by the ledger alone; four cells, one-hot codes found -- the "
        "languages' verdicts void as evidence (211), the computation decides; the table-top floor moves but bounds the "
        "strong side", ok)
    return res


MUTANTS = {"ledger_power": "the bound taken as E/A instead of (E/A)^2",
           "capacity_bounds": "the README's capacity read as bounding the open direction"}


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
        print("  mutant %-16s %-56s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
