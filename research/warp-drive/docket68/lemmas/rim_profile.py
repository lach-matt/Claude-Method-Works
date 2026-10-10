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
     tangential null energy.  That is why every rim at 2.10-2.20m (S3's family) fails it
  P4 (computed) launched from the throat region with a steeper slope, the marginal corridor stays up past r_b and
     meets the plane beyond it, with the tangential null energy and the energy positive all the way and the radial
     null energy held at zero -- and with the radial held strictly positive (margin 0.002) as well.  A family, not a
     point: launch depths 0.25-0.75m, slopes 6-15 (in r; near the throat g_rr ~ 4e4, so 0.03-0.08 in proper distance),
     rims at r = 3.2-4.9m, meeting angles 5.6-19.7 degrees.  S3's verdict held for the slopes it scanned, not in general
  P5 (computed, forming_rim F3b) the meeting angle theta (proper: tan theta = |Y'| / sqrt(g_rr)) and the ring that
     balances the rim in the Z2 double cover: lambda = a sigma (1 - cos theta)(1 + 2 cos theta), 0.014-0.17 a sigma
     over the family (0.051 at the representative).  The ring, a 2-sphere of energy density equal to its tension, obeys the NEC
  P6 (cypher) forming_rim's index with the new computed cell (static, Z2 images and a ring, steep-launched marginal
     corridor: balance, radial, tangential, fits 198, through the hold).  The closing rim is now DATA: all five admit
     it.  Control: the cell removed -- statistics refuses again at order 3, blocked by forming_rim's triples
What this does not show, recorded: (i) the corridor's joint with the throat region at r = 2.005m (the bank's inner
edge; ITEM197's facing form there) is not computed -- the launch depth and slope are free here; (ii) the bulk is eq.
(17)'s static bulk in the flat limit, by Pade continuation (a heuristic; corridor_shape's bank, not regenerated);
(iii) the ring is matter at the rim, of positive tension, which nothing else in the theory supplies yet -- what it is
is OPEN; (iv) the corridor's own energy against 203's E (corridor_shape S2) is not re-read; (v) F0's caveat: the rim
is a force diagram realisable in the Z2 double cover.
Named readings (the board's): H-RING-AT-THE-RIM (a ring of positive tension sits where the corridor meets our plane;
rim_readme R4 already said an edge needs a force there).  fits_198 = 1: the corridor carries its own surface stress
only -- no README stress at the rim, no partner.
So: the rim's null-energy block is lifted for steep-launched corridors -- radial and tangential null energy kept,
energy positive, the rim beyond r_b, balanced by a ring of 0.014-0.17 a sigma.  The rim is no longer what blocks
M1 within one universe; the throat joint, the ring's nature and Wall C's bridge are.
Imports corridor_shape.py and forming_rim.py (and tools/cypher.py) by path.  Stdlib + sympy + mpmath (through
corridor_shape).  python3 rim_profile.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
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
        _C.update(cs=cs, ks=cs.curvature_exprs(), bulk=cs.Bulk(cs.load_bank()))
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
    s3 = cs.marginal(ks, bulk, 0.5, 0.0, 0.0, rmax=12.0)
    s3_neg = any(row[5] < 0 for row in s3["rows"])
    return {"int_kappa": tot, "kappa_max": kmax, "s3_rim": s3["rim"], "s3_neg": s3_neg}


# ---------------------------------------------------------------------------------------------------------- P4, P5
FAMILY = [(0.25, 6.0), (0.4, 10.0), (0.5, 12.0), (0.6, 15.0), (0.75, 15.0)]


def family(margins=(0.0, 0.002)):
    cs, ks, bulk = shape()
    out = {}
    for m in margins:
        mm = m if not MUT.get("radial_off") else -0.01
        for d, s in FAMILY:
            R = cs.marginal(ks, bulk, d, mm, s if not MUT.get("small_slope") else 0.3, rmax=12.0)
            rows = R["rows"]
            r, Y, Y1 = rows[-1][:3]
            B = bulk.at(r, max(Y, 1e-6))["B"][0]
            th = math.atan(abs(Y1) / (math.sqrt(B) if not MUT.get("theta_r") else 1.0))
            out[(m, d, s)] = {"rim": R["rim"], "min_rad": min(x[4] for x in rows), "min_tan": min(x[5] for x in rows),
                              "min_rho": min(x[3] for x in rows), "theta": th, "ring": (1 - math.cos(th)) * (1 + 2 * math.cos(th)),
                              "launch_proper": s / math.sqrt(bulk.at(2.005, d)["B"][0])}
    return out


# ---------------------------------------------------------------------------------------------------------- P6
def cypher():
    fr = _load(os.path.join(HERE, "forming_rim.py"), "rp_forming_rim")
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "rp_cypher")
    C7 = fr.C7
    new = (0, 2, 1, 1, 1, 1, 1, 1)                 # static, Z2 images + ring, steep-launched marginal corridor (P4, P5)
    cells = list(fr.CELLS) + ([] if MUT.get("drop_new_cell") else [new])
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
    main = {l: all(new in (adm(cells, l, None, tuple(p)) or []) for p in itertools.permutations(range(4))) for l in langs}
    main["statistics2"] = new in (adm(cells, "statistics", {"statistics_order": 2}) or [])
    main["statistics3"] = new in (adm(cells, "statistics", {"statistics_order": 3}) or [])
    ctrl3 = adm(list(fr.CELLS), "statistics", {"statistics_order": 3})
    return {"main": main, "ctrl3": ctrl3, "is_data": new in cells}


def compute():
    q2 = p2()
    return {"p1": p1(), "p2": q2, "p3": p3(q2["rb"] or 3.0), "fam": family(), "cy": cypher()}


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
        "S3's family (launch slope 0) meets the plane inside r_b with it negative", math.isfinite(p3["int_kappa"])
        and 0 < p3["kappa_max"] < 100 and p3["s3_rim"] is not None and p3["s3_rim"] < 3.0 and p3["s3_neg"])
    fam = d["fam"]
    ok0 = all((v["rim"] or 0) > (rb or 3.01) and v["min_tan"] > 0 and v["min_rho"] > 0
              and v["min_rad"] > -1e-10 for (m, dd, s), v in fam.items() if m == 0.0)
    add("P4 the steep-launched marginal family (depths 0.25-0.75m, slopes 6-15) meets the plane beyond r_b with the "
        "tangential null energy and the energy positive throughout, radial held at zero", ok0)
    ok2 = all((v["rim"] or 0) > (rb or 3.01) and v["min_tan"] > 0 and v["min_rho"] > 0
              and v["min_rad"] >= 0.002 - 1e-10 for (m, dd, s), v in fam.items() if m == 0.002)
    add("P4 the same with the radial null energy held strictly positive (margin 0.002)", ok2)
    rep = fam[(0.0, 0.5, 12.0)]
    add("P5 at the representative (0.5m, slope 12): rim 4.16m, meeting angle 10.6 degrees (tan = |Y'|/sqrt(g_rr)), ring "
        "lambda = 0.051 a sigma; every member's ring between 0.01 and 0.2 a sigma; launch slopes 0.03-0.08 in proper "
        "distance",
        abs((rep["rim"] or 0) - 4.16) < 0.02 and abs(math.degrees(rep["theta"]) - 10.6) < 0.3 and abs(rep["ring"] - 0.051) < 0.003
        and all(0.01 < v["ring"] < 0.2 for v in fam.values()) and all(0.02 < v["launch_proper"] < 0.09 for v in fam.values()))
    c = d["cy"]
    add("P6 cypher: with the new cell the closing rim is data -- order, algebra, geometry, information admit it under all "
        "24 codings of the support axis, statistics at orders 2 and 3", c["is_data"] and all(c["main"].values()))
    add("P6 control: the new cell removed -- statistics refuses the closing rim at order 3 (forming_rim's block)",
        c["ctrl3"] == [])
    return res


MUTANTS = {"small_slope": "the family launched at slope 0.3 (S3's range)",
           "b_sign": "the tangential slope term's sign flipped",
           "radial_off": "the radial null energy let go negative (margin -0.01)",
           "theta_r": "the meeting angle taken without sqrt(g_rr)",
           "drop_new_cell": "the computed closing cell left out of the cypher's index"}


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
    print("P6", d["cy"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
