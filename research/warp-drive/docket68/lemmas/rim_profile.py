#!/usr/bin/env python3
"""rim_profile.py -- the rim's null-energy triple, by profile: does any corridor reach our plane with its radial and
tangential null energy both kept?  Pass 2 of the cycle (items 204-206); put to the cypher (computed, deduced; flat
limit; eq. (17)'s static bulk by Pade continuation; not verified by a separate session; not seated; 2026-10-10).

forming_rim.py left the rim's force balance closable (Z2 images and a ring of positive tension, static, through the
hold) and named what blocks a closing rim: no computed arrangement had the radial and the tangential null energy
together and fit 198 (statistics, order 3).  corridor_shape.py's marginal family (radial held at zero by solving for
Y'') met the plane at r = 2.10-2.20m with its tangential null energy negative on the last stretch (S3) -- for launch
slopes 0 and +-0.3 only.

  P1 (computed, corridor_shape's curvature) k_t and k_theta do not depend on Y''; k_r does, linearly, with dk_r/dY'' > 0.
     So the tangential null energy rho + p_theta = k_t - k_theta is fixed by (r, Y, Y'), and the radial one
     rho + p_r = k_t - k_r is kept exactly when Y'' <= Y''_m(r, Y, Y') (the marginal curvature)
  P2 (computed) near the plane, to first order in depth and slope: tangential = a(r) Y + b(r) Y' with a > 0, and b > 0
     inside r_b ~ 3.01m, b < 0 beyond (the sign change located); Y''_m = -lambda(r) Y + mu(r) Y' with lambda > 0
  P3 (deduced from P2; Gronwall) inside r_b a descending corridor keeps the tangential null energy only if
     Y' >= -kappa Y, kappa = a/b, bounded on [2.02, 2.9]m; then Y >= Y0 exp(-int kappa) > 0: NO rim inside r_b keeps the
     tangential null energy.  Illustrated by the marginal corridor held strictly positive (margin 0.01): its rims fall
     inside r_b and its tangential fails there
  P4 (computed, on corridor_shape's corrected interpolation, S0) the marginal corridor (radial held at zero) meets
     the plane beyond r_b with the tangential null energy and the energy positive all the way: launch depths 0.25-1m,
     launch slopes 0 to 0.017 in proper distance (0-3 in r), rims at r = 3.40-5.29m, meeting angles 5.3-15.1 degrees.
     Held strictly positive (margin 0.002) the launches with a positive slope still close (rims 3.57-4.68m).
     [The first version of this lemma, on corridor_shape's uncorrected interpolation, needed slopes 6-15 in r; that was
     the interpolation's 8% error in g_rr near the throat, not the geometry.]
  P4b (computed; the throat joint) with six exactly computed columns between 2.00001m and 2.003m
     (corridor_shape_inner.json), the marginal corridor traced inward from its launch flattens into the throat: its
     proper slope falls toward zero (about as sqrt(r - 2m)) and its depth settles, the tangential null energy and the
     energy positive throughout -- the throat's constant-depth corridor (ITEM197's facing form) joined smoothly
  P5 (computed, forming_rim F3b) the meeting angle theta (proper: tan theta = |Y'| / sqrt(g_rr)) and the ring that
     balances the rim in the Z2 double cover: lambda = a sigma (1 - cos theta)(1 + 2 cos theta), 0.013-0.10 a sigma over
     the family (0.037 at the representative, 0.5m launched at slope 1).  The ring, a 2-sphere of energy density equal
     to its tension, obeys the NEC
     [CORRECTED, item 208 (ring_consistent.py; the item-208 critics confirmed the sign): this ring is positive only b
     ecause the corridor's sheet is given -sigma at the rim (TENS['corr'] = -1, rim_readme R5's coincidence law for f
     acing sheets) while the meeting angle comes from the tilted marginal corridor.  With the marginal corridor's own
      tension (rho_rim > 0, rho + p_r = 0) the balance asks lambda = -(cos 2t + tau cos t) a sigma < 0: a junction in
      compression.  The computation below is kept as it was; its premise is refuted.]
  P6 (cypher) forming_rim's corrected index (its static marginal cells carry this computation): the closing rim through
     the hold is DATA, all five admit it.  Control: the static closing cells removed -- statistics refuses at order 4
What this does not show, recorded: (i) the bulk is eq. (17)'s static bulk in the flat limit, by Pade continuation (a
heuristic); (ii) the ring is matter at the rim, of positive tension, which nothing else in the theory supplies yet --
what it is is OPEN; (iii) the corridor's own energy against 203's E (corridor_shape S2) is not re-read; (iv) F0's
caveat: the rim is a force diagram realisable in the Z2 double cover.
Named readings (the board's): H-RING-AT-THE-RIM (a ring of positive tension sits where the corridor meets our plane;
rim_readme R4 already said an edge needs a force there).  fits_198 = 1: the corridor carries its own surface stress
only -- no README stress at the rim, no partner.
So: the marginal corridor keeps its radial and tangential null energy from the throat, which it joins smoothly, to a
rim beyond r_b, energy positive, balanced by a ring of 0.013-0.10 a sigma.  The rim is no longer what blocks M1 within
one universe; the ring's nature and Wall C's bridge are.
Imports corridor_shape.py and forming_rim.py (and tools/cypher.py) by path.  Stdlib + sympy + mpmath (through
corridor_shape).  python3 rim_profile.py [--selftest | --mutants]
"""
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


def shape():
    if not _C:
        cs = _load(os.path.join(HERE, "corridor_shape.py"), "rp_cs")
        bank = cs.load_bank()
        inner = json.load(open(os.path.join(HERE, "corridor_shape_inner.json")))
        full = dict(bank)
        for rc, e in inner.items():
            full[rc] = {k: ([float(v) for v in nd[0]], [float(v) for v in nd[1]]) for k, nd in e.items()}
        _C.update(cs=cs, ks=cs.curvature_exprs(), bulk=cs.Bulk(bank), inner=cs.Bulk(full))
    return _C["cs"], _C["ks"], _C["bulk"]


def _args(bulk, r, Y, Y1, Y2):
    g = bulk.at(r, Y)
    return (g["A"][0], g["B"][0], g["C"][0], g["A"][1], g["B"][1], g["C"][1], g["A"][2], g["B"][2], g["C"][2], Y1, Y2)


def tangential(r, Y, Y1):
    cs, ks, bulk = shape()
    t = cs.stresses(ks, bulk.at(r, Y), Y1, 0.0)[2]
    return t if not MUT.get("b_sign") else cs.stresses(ks, bulk.at(r, Y), -Y1, 0.0)[2]


# ---------------------------------------------------------------------------------------------------------- P1, P2
def p1():
    cs, ks, bulk = shape()
    out = []
    for r, Y, Y1 in ((2.1, 0.3, -0.2), (3.5, 0.1, -0.4), (2.5, 0.6, 0.5)):
        a0, a1 = _args(bulk, r, Y, Y1, 0.0), _args(bulk, r, Y, Y1, 1.0)
        a2 = _args(bulk, r, Y, Y1, 2.0)
        free = abs(ks["kt"](*a1) - ks["kt"](*a0)) < 1e-12 and abs(ks["kth"](*a1) - ks["kth"](*a0)) < 1e-12
        lin = abs((ks["kr"](*a2) - ks["kr"](*a1)) - (ks["kr"](*a1) - ks["kr"](*a0))) < 1e-9
        out.append(free and lin and ks["kr"](*a1) > ks["kr"](*a0))
    return all(out)


def p2(rs=(2.02, 2.05, 2.1, 2.2, 2.4, 2.8, 3.5, 4.0)):
    cs, ks, bulk = shape()
    Y, dY = 0.01, 0.02
    rows = {}
    for r in rs:
        a = tangential(r, Y, 0.0) / Y
        b = (tangential(r, Y, dY) - tangential(r, Y, -dY)) / (2 * dY)
        def y2m(Y1):
            a0, a1 = _args(bulk, r, Y, Y1, 0.0), _args(bulk, r, Y, Y1, 1.0)
            return (ks["kt"](*a0) - ks["kr"](*a0)) / (ks["kr"](*a1) - ks["kr"](*a0))
        lam = -y2m(0.0) / Y
        mu = (y2m(dY) - y2m(-dY)) / (2 * dY)
        rows[r] = {"a": a, "b": b, "lam": lam, "mu": mu}
    # the sign change of b
    prev, rb = None, None
    for i in range(0, 120):
        r = 2.4 + 0.01 * i
        b = (tangential(r, Y, dY) - tangential(r, Y, -dY)) / (2 * dY)
        if prev is not None and prev > 0 >= b:
            rb = r
            break
        prev = b
    return {"rows": rows, "rb": rb}


def p3(rb):
    """int of kappa = a/b over [2.02, rb - 0.1]: finite, so Y >= Y0 exp(-int kappa) > 0 (no rim there)"""
    grid = [2.02 + 0.01 * i for i in range(int((rb - 0.1 - 2.02) / 0.01) + 1)]
    Y, dY, tot, kmax = 0.01, 0.02, 0.0, 0.0
    for r0, r1 in zip(grid, grid[1:]):
        a = tangential(r0, Y, 0.0) / Y
        b = (tangential(r0, Y, dY) - tangential(r0, Y, -dY)) / (2 * dY)
        k = a / b
        kmax = max(kmax, k)
        tot += k * (r1 - r0)
    cs, ks, bulk = shape()
    s3 = cs.marginal(ks, bulk, 0.5, 0.01, 0.0, rmax=12.0)             # held strictly positive: rim inside r_b
    s3_neg = any(row[5] < 0 for row in s3["rows"])
    return {"int_kappa": tot, "kappa_max": kmax, "s3_rim": s3["rim"], "s3_neg": s3_neg}


# ---------------------------------------------------------------------------------------------------------- P4, P5
FAMILY = [(0.25, 0.0), (0.5, 0.0), (0.5, 1.0), (0.75, 2.0), (1.0, 3.0)]
STRICT = [(0.5, 1.0), (0.75, 2.0), (1.0, 3.0)]                      # the members that still close at margin 0.002


def family(margins=(0.0, 0.002)):
    cs, ks, bulk = shape()
    out = {}
    for m in margins:
        mm = m if not MUT.get("radial_off") else -0.01
        for d, s in (FAMILY if m == 0.0 else STRICT):
            R = cs.marginal(ks, bulk, d, mm, s if not MUT.get("small_slope") else -1.0, rmax=12.0)
            rows = R["rows"]
            r, Y, Y1 = rows[-1][:3]
            B = bulk.at(r, max(Y, 1e-6))["B"][0]
            th = math.atan(abs(Y1) / (math.sqrt(B) if not MUT.get("theta_r") else 1.0))
            out[(m, d, s)] = {"rim": R["rim"], "min_rad": min(x[4] for x in rows), "min_tan": min(x[5] for x in rows),
                              "min_rho": min(x[3] for x in rows), "theta": th, "ring": (1 - math.cos(th)) * (1 + 2 * math.cos(th)),
                              "launch_proper": s / math.sqrt(bulk.at(2.005, d)["B"][0])}
    return out


def joint(cases=((0.5, 1.0), (0.25, 0.0), (1.0, 3.0))):
    """trace the marginal corridor inward from its launch at 2.005m to 2.00001m on the inner columns"""
    cs, ks, _ = shape()
    bulk = _C["inner"] if not MUT.get("no_inner") else _C["bulk"]

    def y2m(r, Y, Y1):
        a0, a1 = _args(bulk, r, Y, Y1, 0.0), _args(bulk, r, Y, Y1, 1.0)
        return (ks["kt"](*a0) - ks["kr"](*a0)) / (ks["kr"](*a1) - ks["kr"](*a0))
    out = {}
    for d, s0 in cases:
        r, Y, Y1, rows = 2.005, d, s0, []
        while r > 2.000012:
            h = -max(1e-8, min(2e-5, (r - 2.0) * 0.005))
            f = lambda rr, st: (st[1], y2m(rr, st[0], st[1]))
            k1 = f(r, (Y, Y1)); k2 = f(r + h/2, (Y + h/2*k1[0], Y1 + h/2*k1[1]))
            k3 = f(r + h/2, (Y + h/2*k2[0], Y1 + h/2*k2[1])); k4 = f(r + h, (Y + h*k3[0], Y1 + h*k3[1]))
            Y += h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]); Y1 += h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]); r += h
            if Y <= 0.005:
                break
            if not rows or r <= rows[-1][0] * 0 + (2 + (rows[-1][0] - 2) / 2):
                B = bulk.at(r, Y)["B"][0]
                rho, nr, nt = cs.stresses(ks, bulk.at(r, Y), Y1, y2m(r, Y, Y1))
                rows.append((r, Y, Y1 / math.sqrt(B), nt, rho))
        out[(d, s0)] = rows
    return out


# ---------------------------------------------------------------------------------------------------------- P6
def cypher():
    fr = _load(os.path.join(HERE, "forming_rim.py"), "rp_forming_rim")
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "rp_cypher")
    C7 = fr.C7
    closing = {(0, 1, 1, 1, 1, 1, 1, 1), (0, 2, 1, 1, 1, 1, 1, 1)}
    cells = list(fr.CELLS)
    if MUT.get("drop_new_cell"):
        cells = [c for c in cells if c not in closing]
    full = lambda h: all(h[i] == 1 for i in range(2, 8))

    def adm(cs_, lang, opts=None, sup=(0, 1, 2, 3)):
        vo = {"phase": [0, 1], "support": [x for x in sup if x in {c[1] for c in cs_}]}
        for j, name in enumerate(C7[2:], start=2):
            vo[name] = [x for x in (0, 1, fr.U) if x in {c[j] for c in cs_}]
        ix = cy.Index("rim_profile", C7, [list(c) for c in cs_], value_order=vo)
        inv = [{v: k for k, v in ix.code[i].items()} for i in range(len(C7))]
        out, _ = cy.ADMISSION[lang][0](ix, opts or {})
        if out is None:
            return None
        dec = {tuple(inv[i][c[i]] for i in range(len(C7))) for c in out if all(c[i] in inv[i] for i in range(len(C7)))}
        return sorted(h for h in dec if full(h))

    langs = ("order", "algebra", "geometry", "information")
    main = {l: all(closing <= set(adm(cells, l, None, tuple(p)) or []) for p in itertools.permutations(range(4))) for l in langs}
    main["statistics4"] = closing <= set(adm(cells, "statistics", {"statistics_order": 4}) or [])
    ctrl4 = adm([c for c in fr.CELLS if c not in closing], "statistics", {"statistics_order": 4})
    return {"main": main, "ctrl4": ctrl4, "is_data": closing <= set(cells)}


def compute():
    q2 = p2()
    return {"p1": p1(), "p2": q2, "p3": p3(q2["rb"] or 3.0), "fam": family(), "joint": joint(), "cy": cypher()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("P1 k_t and k_theta are free of Y''; k_r is linear in Y'' and increases with it", d["p1"])
    rows, rb = d["p2"]["rows"], d["p2"]["rb"]
    add("P2 near the plane: a > 0 everywhere sampled; b > 0 inside, b < 0 beyond, the sign change at r_b in (3.0, 3.02)m",
        all(v["a"] > 0 for v in rows.values()) and all(rows[r]["b"] > 0 for r in rows if r < 3.0)
        and all(rows[r]["b"] < 0 for r in rows if r > 3.05) and rb is not None and 3.0 <= rb <= 3.02)
    add("P2 the marginal curvature: lambda > 0 and mu < 0 at every radius sampled (Y''_m = -lambda Y + mu Y')",
        all(v["lam"] > 0 and v["mu"] < 0 for v in rows.values()))
    p3 = d["p3"]
    add("P3 kappa = a/b is bounded inside r_b (int kappa finite): no rim inside r_b keeps the tangential null energy; "
        "the marginal corridor held strictly positive (margin 0.01) meets the plane inside r_b with it negative",
        math.isfinite(p3["int_kappa"]) and 0 < p3["kappa_max"] < 100 and p3["s3_rim"] is not None and p3["s3_rim"] < 3.0
        and p3["s3_neg"])
    fam = d["fam"]
    ok0 = all((v["rim"] or 0) > (rb or 3.01) and v["min_tan"] > 0 and v["min_rho"] > 0
              and v["min_rad"] > -1e-10 for (m, dd, s), v in fam.items() if m == 0.0)
    add("P4 the marginal corridor (launch depths 0.25-1m, slopes 0-0.017 in proper distance) meets the plane beyond r_b, "
        "at 3.40-5.29m, with the tangential null energy and the energy positive throughout, radial held at zero", ok0
        and all(3.39 < v["rim"] < 5.3 for (m, dd, s), v in fam.items() if m == 0.0))
    ok2 = all((v["rim"] or 0) > (rb or 3.01) and v["min_tan"] > 0 and v["min_rho"] > 0
              and v["min_rad"] >= 0.002 - 1e-10 for (m, dd, s), v in fam.items() if m == 0.002)
    add("P4 held strictly positive (margin 0.002), the launches with a positive slope still close beyond r_b", ok2)
    jt = d["joint"]
    okj = all(len(rows) >= 6 and rows[-1][0] < 2.00002 and all(x[3] > 0 and x[4] > 0 for x in rows)
              and abs(rows[-1][2]) < 0.002 and abs(rows[-1][1] - rows[-2][1]) < 0.001 for rows in jt.values())
    add("P4b the throat joint: traced inward to 2.00002m on the exact inner columns, the corridor's proper slope falls "
        "under 0.002 and its depth settles (under 0.001 over the last halving of r - 2m), tangential null energy and "
        "energy positive throughout", okj)
    rep = fam[(0.0, 0.5, 1.0)]
    add("P5 at the representative (0.5m, slope 1): rim 4.16m, meeting angle 9.0 degrees (tan = |Y'|/sqrt(g_rr)), ring "
        "lambda = 0.037 a sigma; every member's ring between 0.01 and 0.11 a sigma at margin 0", abs((rep["rim"] or 0) - 4.16) < 0.02
        and abs(math.degrees(rep["theta"]) - 9.0) < 0.3 and abs(rep["ring"] - 0.037) < 0.003
        and all(0.01 < v["ring"] < 0.11 for (m, dd, s), v in fam.items() if m == 0.0))
    c = d["cy"]
    add("P6 cypher: on forming_rim's corrected index the closing rim through the hold is data -- order, algebra, "
        "geometry, information admit it under all 24 codings of the support axis, statistics at order 4",
        c["is_data"] and all(c["main"].values()))
    add("P6 control: the static closing cells removed -- statistics refuses the closing rim at order 4", c["ctrl4"] == [])
    return res


MUTANTS = {"small_slope": "the family launched descending (slope -1)",
           "b_sign": "the tangential slope term's sign flipped",
           "radial_off": "the radial null energy let go negative (margin -0.01)",
           "theta_r": "the meeting angle taken without sqrt(g_rr)",
           "drop_new_cell": "the computed closing cells left out of the cypher's index",
           "no_inner": "the throat joint traced without the inner columns (extrapolated)"}


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
        print("  mutant %-13s %-50s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("rim_profile.py -- the rim's null-energy triple, by profile\n")
    print("P2 r_b (b changes sign) = %s" % d["p2"]["rb"])
    for r, v in d["p2"]["rows"].items():
        print("   r=%.2f a=%+.4f b=%+.4f lambda=%+.3f mu=%+.3f" % (r, v["a"], v["b"], v["lam"], v["mu"]))
    print("P3", d["p3"])
    for (m, dd, s), v in d["fam"].items():
        print("P4 margin %.3f depth %.2f slope %4.1f: rim %s  min radial %+.2e  min tangential %+.2e  min rho %+.2e  "
              "theta %.1f deg  ring %.3f a sigma" % (m, dd, s, v["rim"], v["min_rad"], v["min_tan"], v["min_rho"],
                                                     math.degrees(v["theta"]), v["ring"]))
    for k, rows in d["joint"].items():
        print("P4b launch %s traced inward:" % (k,), ["r=%.6f Y=%.4f proper=%+.4f" % x[:3] for x in rows[-3:]])
    print("P6", d["cy"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
