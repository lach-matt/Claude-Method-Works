#!/usr/bin/env python3
"""g_coincide.py -- item 275: the planes coincide everywhere ("Coincident everywhere").  Item 274's caveat closed, and
the proof 139 (2) orders re-worked for position 2's sheet as one of two coincident sheets, from what the coincidence
fixes: the background warp 139 (1)'s quarter came from, the shared sheet's expansion, and the null rays that cross both
sheets at one point.  Worked in the conversation (computed with sympy, exact where marked; READ where marked; standard
values marked; deduced where marked; the cypher run and audited; not verified by a separate session; not seated);
2026-10-12.

[M, item 277: "You are forgetting that the passage is one-way only".  G2-G4 acted from position 2 onto ours (recorded at 276).  Kept as written; h_oneway.py and
i_oneway.py follow it.]

  G0 (read) M's item-275 words, verbatim in the rulings file.
  G1 (computed; f_slab F3) No slab of bulk lies between the planes anywhere, so f_slab's static slab -- and with it
     e_positive E6's counter-case, in which 139 (2) and 139 (3) conflict -- exists nowhere.  Item 274's caveat is
     closed by M's ruling, not by a board reading.
  G2 (computed, exact; READ via multiplane.py: Pilo-Rattazzi-Zaffaroni eqs. 2.16, 3.3-3.4) At the coincidence the
     junction fixes only the summed stress; the background warp splits it as tau1 = 24 M^3 k_L, tau2 = 24 M^3 (k_R -
     k_L).  At r = 0 the radion's kinetic coefficient is C_r = 24 M^3/(k_R - k_L) = (24 M^3)^2/tau2 -- the sign of
     position 2's static total -- and gamma = (3 + X)/(3 - X), X = (k_L - k_R)/k_R.  139 (1)'s quarter (k_R = 3 k_L/4)
     is gamma = 5/4 with tau2 = -tau1/4 and C_r < 0, the ghost M3 records; any positive static total gives k_R > k_L,
     gamma between 1/2 and 1, and no ghost.  Matter that is static (w = -1) enters the warp as tension does, so
     position 2's tension plus static matter is tau2: with 139 (1) kept it is -tau1/4, negative.
  G3 (computed; standard H0) Matter that is not static gravitates on the one sheet both universes share: the
     coincident sheet's Friedmann form (like decaying sides, e_positive E3) gives H^2 = (8 pi G/3)(rho/c^2)(1 +
     rho/(2 sigma)).  At rho = sigma/4 = 3.7e52 J/m^3, H = 1.6e13 s^-1 -- 7.4e30 times our H0 (67.4 km/s/Mpc, Planck
     2018, standard, not READ here), at ell = 13.964 um, the largest the table-top bound allows; a smaller ell raises
     sigma and H with it.  So position 2's matter at sigma/4 cannot be spread over its sheet; within the README's
     2.0e-15 m of the face (e_positive E7) it is the README itself.
  G4 (computed) The rays.  At the coincidence every null ray through position 2's sheet crosses ours at the same
     point, and its share is the composite's: tension tau1 + tau2 = +1 of the one-plane value (b5_positive B5a),
     share e sin a > 0 on every ray -- with no matter on position 2's sheet at all.  183's pair ("never violated as a
     pair", a negative member paired along the same light rays) is ours and position 2's, on every ray; m1p2x_sixth
     W1's condition (every crossing ray's share non-negative) holds through ours.
  G5 (computed; the cypher, roster 1173, audited) The index: position 2's own matter (none, static, spread and not
     static, local and not static) x the sense of 139 (2) (per ray, its sheet everywhere, its sheet at the face) -- 12
     rows, each with keeps_quarter (139 (1)'s gamma = 5/4), keeps_H0 (our expansion) and positive (in that sense).  The
     all-three cell is reached per ray and at the face, with no matter of position 2's own or local matter; position
     2's sheet positive everywhere keeps 139 (1) and our expansion in no row.  The held set is every cell with at least
     two of the three -- the polytope keeps_quarter + keeps_H0 + positive >= 2, which geometry, information and
     statistics admit exactly (E = 0); order and algebra add the four cells below it (E = 4); K.langclose holds.  Any
     two of the three demands can be met together; all three only per ray or at the face.
  G6 (deduced) Under 275, 139 (2) is proved per ray (G4) and at the face (e_positive E7), with 139 (1) and our
     expansion kept.  Position 2's sheet alone positive everywhere -- the board's reading of 268 in m1p2x_sixth -- costs
     139 (1)'s quarter if its matter is static (G2) and our expansion rate if it is not (G3).  Which sense 268's
     "tension plus matter" is, is M's.  Per ray, m1p2x_oneway O5's z_net (every crossing ray's share >= 0) holds with no
     matter of position 2's own (m2 = 0): at the coincidence the positive member of 183's pair is our plane.

What this does not show.
  - The pin (141) as a degree of freedom: b5_positive B5c read the held separation as no radion at all; G2's C_r is
    the coefficient a separation would carry, its sign the static total's either way.
  - Position 2's matter beyond these four kinds (a static part and a local part together are G5's rows combined).

Imports f_slab.py, e_positive.py, bulk/multiplane.py, p2_gravity.py, index_audit.py and tools/cypher.py by path.
Stdlib + sympy.  python3 g_coincide.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
M275 = "Coincident everywhere"
PROPS = ["keeps_quarter", "keeps_H0", "positive"]
FIVE = ["order", "algebra", "geometry", "information", "statistics"]
H0 = 67.4e3 / 3.0857e22                                   # Planck 2018, standard, not READ here


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


def no_slab():
    FS = _load(os.path.join(HERE, "f_slab.py"), "gc_fs")
    fc = FS.facing()
    return dict(f3=fc["ours"] and fc["p2_never"])


def warp():
    """G2: PRZ at r = 0 -- C_r against tau2, gamma against the split"""
    MP = _load(os.path.join(D68, "bulk", "multiplane.py"), "gc_mp")
    d = MP.lr()
    kL, kR, r, M = MP.kL, MP.kR, MP.r, MP.M
    Cr0 = sp.simplify(d["Cr"].subs(r, 0))
    tau2 = d["tau2"]
    if MUT.get("ghost_sign"):
        tau2 = -tau2                                       # the mutant flips position 2's tension
    rel = sp.simplify(Cr0 * tau2 - (24 * M ** 3) ** 2)
    X = (kL - kR) / kR
    g = (3 + X) / (3 - X)
    q = sp.Rational(3, 4) * kL
    quarter = dict(gamma=sp.simplify(g.subs(kR, q)), tau2_over_tau1=sp.simplify((tau2 / d["tau1"]).subs(kR, q)),
                   Cr=sp.simplify(Cr0.subs(kR, q)))
    s = sp.Symbol("s", positive=True)                      # k_R = k_L (1 + s): a positive static total
    gpos = sp.simplify(g.subs(kR, kL * (1 + s)))
    lim = (sp.limit(gpos, s, 0), sp.limit(gpos, s, sp.oo))
    below = sp.simplify(1 - gpos)
    return dict(rel=rel, quarter=quarter, gpos=gpos, lim=lim, below_pos=bool(sp.simplify(below.subs({kL: 1})).is_positive),
                Cr_pos=bool(sp.simplify(Cr0.subs(kR, kL * (1 + s))).is_positive))


def expansion():
    """G3: the shared sheet's expansion rate with position 2's matter at sigma/4, spread and not static"""
    PG = _load(os.path.join(HERE, "p2_gravity.py"), "gc_pg")
    sigma = 3 * PG.C ** 4 / (4 * math.pi * PG.G * PG.ELL_MAX ** 2)
    rho = sigma / 4
    H2 = 8 * math.pi * PG.G / 3 * (rho / PG.C ** 2) * (1 + rho / (2 * sigma))
    if MUT.get("no_shared_H"):
        H2 = 0.0                                           # the mutant lets position 2's matter leave our expansion
    H = math.sqrt(H2)
    return dict(quarter=rho, H=H, over_H0=H / H0)


def rays():
    """G4: the composite's share on every ray (one-plane units)"""
    t1, t2 = sp.Rational(4, 3), sp.Rational(-1, 3)
    if MUT.get("composite_negative"):
        t2 = sp.Rational(-5, 3)                            # the mutant over-weights position 2's tension
    a = sp.Symbol("a", positive=True)
    e = t1 + t2
    share = e * sp.sin(a) + (e + (-e)) * sp.cos(a) ** 2 / sp.sin(a)   # tension: P = -e
    return dict(e=e, share=sp.simplify(share), positive=bool(e > 0))


def populate(gw, ex):
    rows = {}
    for m, sense in itertools.product(("none", "static", "spread", "local"), ("ray", "everywhere", "face")):
        keeps_quarter = int(m != "static" or MUT.get("static_ignored", False))
        keeps_H0 = int(not (m == "spread" and ex["over_H0"] > 1))
        if sense == "ray":
            pos = 1                                        # G4: the composite on every ray
        elif sense == "face":
            pos = 1                                        # e_positive E7: the README at the face
        else:
            pos = int(m in ("static", "spread"))           # sigma/4 across the whole sheet needs matter across it
        rows[(m, sense)] = dict(keeps_quarter=keeps_quarter, keeps_H0=keeps_H0, positive=pos)
    return rows


def cypher(rows):
    held = sorted({tuple(p[c] for c in PROPS) for p in rows.values()})
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "gc_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "gc_ia")
    ix = cy.Index("g_coincide", PROPS, [list(c) for c in held], value_order={c: [0, 1] for c in PROPS})
    run = cy.run(ix, "1173", dict(OPTS))
    clo = set(held)
    while True:
        new = {tuple(op(a, b) for a, b in zip(x, y)) for x in clo for y in clo for op in (max, min)} - clo
        if not new:
            break
        clo |= new
    return dict(held=held, reached=(1, 1, 1) in held, closure_adds=sorted(clo - set(held)),
                E={v["language"]: v["E"] for v in run["verdicts"]}, langclose=run["langclose_holds"],
                agreeing=run["pairs_agreeing"], audit=ia.audit_index(PROPS, held),
                holders=sorted(c for c, p in rows.items() if tuple(p[x] for x in PROPS) == (1, 1, 1)))


def compute():
    gw, ex = warp(), expansion()
    rows = populate(gw, ex)
    return dict(ns=no_slab(), gw=gw, ex=ex, ry=rays(), rows=rows, cy=cypher(rows))


def report(o):
    print("g_coincide.py -- 139 (2) under item 275, the planes coincident everywhere\n")
    print("G1 f_slab F3 (no static slab can carry both): %s -- and under 275 there is none" % o["ns"]["f3"])
    gw = o["gw"]
    print("G2 C_r(r = 0) . tau2 - (24 M^3)^2 = %s; at 139 (1)'s quarter gamma = %s, tau2/tau1 = %s, C_r = %s" % (
        gw["rel"], gw["quarter"]["gamma"], gw["quarter"]["tau2_over_tau1"], gw["quarter"]["Cr"]))
    print("   a positive static total (k_R = k_L (1 + s)): gamma = %s, from %s to %s; C_r > 0: %s" % (
        gw["gpos"], gw["lim"][0], gw["lim"][1], gw["Cr_pos"]))
    ex = o["ex"]
    print("G3 position 2's matter at sigma/4 = %.3g J/m^3 spread, not static: H = %.3g s^-1 = %.3g H0" % (
        ex["quarter"], ex["H"], ex["over_H0"]))
    print("G4 the composite's tension %s of the one-plane value; share on every ray %s" % (o["ry"]["e"], o["ry"]["share"]))
    cy = o["cy"]
    print("G5 %d rows; held (keeps_quarter, keeps_H0, positive): %s; all three by %s" % (len(o["rows"]), cy["held"],
                                                                                      cy["holders"]))
    print("   E %s; langclose %s, %d of 10 pairs agreeing; closure adds %s; audit keys %s one-hot %s" % (
        cy["E"], cy["langclose"], cy["agreeing"], cy["closure_adds"], cy["audit"]["keys"], cy["audit"]["onehot"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("G0 M's item-275 words verbatim in the rulings file", M275 in rul)
    add("G1 f_slab F3 holds: no static slab carries two positive, expanding planes -- under 275 none exists",
        o["ns"]["f3"])
    gw = o["gw"]
    q = gw["quarter"]
    ok = gw["rel"] == 0 and q["gamma"] == sp.Rational(5, 4) and q["tau2_over_tau1"] == sp.Rational(-1, 4)
    ok &= bool(q["Cr"].is_negative) and gw["lim"] == (1, sp.Rational(1, 2)) and gw["below_pos"] and gw["Cr_pos"]
    add("G2 at r = 0, C_r = (24 M^3)^2/tau2; 139 (1)'s quarter is gamma = 5/4, tau2 = -tau1/4, C_r < 0; a positive "
        "static total gives gamma in (1/2, 1) and C_r > 0", ok)
    ex = o["ex"]
    ok = "%.2g" % ex["quarter"] == "3.7e+52" and "%.2g" % ex["H"] == "1.6e+13" and "%.2g" % ex["over_H0"] == "7.4e+30"
    add("G3 position 2's matter at sigma/4 spread over the shared sheet: H = 1.6e13 s^-1 = 7.4e30 H0", ok)
    ry = o["ry"]
    add("G4 the composite's tension is +1 of the one-plane value; every ray's share is (sin a) > 0",
        ry["e"] == 1 and sp.simplify(ry["share"] - sp.sin(sp.Symbol("a", positive=True))) == 0 and ry["positive"])
    cy, rows = o["cy"], o["rows"]
    ok = cy["reached"] and len(rows) == 12
    ok &= cy["holders"] == sorted([("none", "ray"), ("none", "face"), ("local", "ray"), ("local", "face")])
    ok &= not any(tuple(p[x] for x in PROPS) == (1, 1, 1) for c, p in rows.items() if c[1] == "everywhere")
    ok &= not cy["audit"]["keys"] and not cy["audit"]["onehot"] and cy["langclose"]
    ok &= cy["held"] == sorted(c for c in itertools.product((0, 1), repeat=3) if sum(c) >= 2)
    ok &= [cy["E"][L] for L in FIVE] == [4, 4, 0, 0, 0]
    add("G5 the all-three cell is reached per ray and at the face (no own matter, or local); position 2's sheet "
        "positive everywhere in no row; held = at least two of three (E 4, 4, 0, 0, 0); langclose holds; audit clean",
        ok)
    return res


MUTANTS = {"ghost_sign": "position 2's tension flipped in C_r",
           "no_shared_H": "position 2's spread matter left out of our expansion",
           "composite_negative": "the composite's tension over-weighted negative",
           "static_ignored": "static matter left out of the background warp"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-18s %-50s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
