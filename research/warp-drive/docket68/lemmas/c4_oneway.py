#!/usr/bin/env python3
"""c4_oneway.py -- item 282: claim C4 (M1, the plane's reading of the corridor's mouth, at the small end) re-posed on
the glued one-way object.  C4 as verified (m1_small.py, items 262, 269) is kept as written with its item-281 note;
this is its one-way form, after C1's (c1_oneway.py).  Worked in the conversation (computed with sympy, exact where
marked; estimates marked; deduced where marked; not verified by a separate session; not seated); 2026-10-12.

  P0 (read) M's item-282 words, verbatim in the rulings file.
  P1 (computed, exact; imported from m1_small) 203, kept: the hole's Komar mass over the 3-sphere in our exterior is
     3 pi r_h^2/(8 G5), independent of r at flat order (N1), with the verifier's qualifications as seated (the AdS
     term at warp order, the hemisphere's first law, N4).  Position 2 reads the same mass from its own exterior because
     the bounce's map (U, V) -> (-U, -V) is an isometry of the form (b_bounce Q1) -- position 2's reading of its side,
     nothing passing back; the eternal solution's two isometric exteriors are no longer the reason.
  P2 (computed, exact) The plane on the object.  In the Kruskal form -F(UV) dU dV + r(UV)^2 (dchi^2 + sin^2 chi dOmega_2)
     the equator chi = pi/2 has extrinsic curvature 0 for any F and r -- computed for that general form -- so it is
     totally geodesic in every chart of the object: our exterior, our face, our future interior, position 2's past
     interior, position 2's face and exterior.  Clause (b) re-posed: the corridor is in the bulk, bridging P1 (the
     equator on our side, up to our black-hole face) and P2 (the same surface on position 2's side, from its white-hole
     face), joined through the interiors and the bounce (c1_oneway K2-K3) -- not through the eternal hole's second
     exterior; "exclusive to the bulk" holds for stress, the horizon cutting P1 (the C4 verifier's note, kept).
     (a), (c), (d) are C1's, kept (c1_oneway K1): the bulk Ricci-flat at flat order, P1 reading the equator for r_h <<
     r << ell, no matter stress on P1.
  P3 (computed; c1_oneway K4, b_bounce Q4-Q5) Clause (e) re-posed: regular on both exteriors and both faces, a smooth
     horizon at each face (curvature at most 72/r_h^4).  The interiors' r = 0 is where the bounce's quantum region
     stands (273): there the classical equations and pointwise null energy give way, every ray through it carrying net
     negative null energy, paired by the README crossing it (183).  Item 259's admission of the singularity was the
     classical interior's; on the bounce it is replaced.
  P4 (computed; e_positive E7, item 284) Clause (f) re-posed: P2 carries 139 (1)'s tension -sigma/4 and its own matter
     (268), positive where the README lands -- the README's density above sigma/4 within 2.0e-15 m = 1.8e5 r_h of the
     face (E7) -- which is where the corridor's rays cross P2 (284).  A ray crossing P2 there at angle a picks up e sin a
     + (e + P) cos^2 a / sin a >= 0 for e > 0 and e + P >= 0 (m1p2x_sixth W1, a direction-neutral share).  The
     earlier (f) -- the same positive tension, within one universe (L7) -- is set aside: between universes 139 (1)
     puts -sigma/4 on P2.
  P5 (estimate) The state.  The one-way object opens -- it is formed, not eternal -- so its quantum state is the
     collapse-formed one, outgoing Hawking flux without the Hartle-Hawking bath's ingoing half; m1_small N4's bath
     (rho/sigma = 0.305, bending P1 0.92 as much as the tension) is the eternal manifold's and is dropped.  The outgoing
     flux keeps the order: with the hole's luminosity P = E/(2 life) from hold_small L5 (greybody included), the flux's
     energy density on P1 at r = r_h, P/(4 pi r_h^2 c), is 0.29 sigma -- the same order as the bath.  C4's
     qualification (5), "C4 is classical", stands on the one-way object: near the hole the plane's quantum load is of
     the order of its tension.
  P6 (deduced) The ledger.  Kept: N1 (203, with its qualifications), (a), (c), (d), the kink at warp order (KTN,
     READ by the C1 verifier; through the faces deduced, KTN computing only outside the horizon).  Re-posed: (b) through
     the bounce, (e) with the quantum region, (f) between universes, the state.  Dropped (282): P2 on the eternal hole's
     second exterior, the bridge's slice in (e), the Hartle-Hawking bath.  So M1 holds at the small end on the one-way
     object on (a)-(f) at flat order in classical GR, with the quantum flux of P5 near the hole.
  P7 (the cypher NOT-RUN, stated) C4's clauses over the object's regions form a two-coordinate table, degenerate for
     the cypher's statistics (reg 1175); the object's own causal order is c1_oneway K6's run, which C4 shares.

What this does not show.
  - The kink through the faces and the interiors (deduced from KTN's exterior, not computed).
  - The flux's back-reaction on P1 (P5 is the load's size, not the bending computed).

Imports m1_small.py, c1_oneway.py, e_positive.py and hold_small.py by path.  Stdlib + sympy.
python3 c4_oneway.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M282 = "Re-pose them one-way (Recommended)"


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [HERE]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def komar():
    MS = _load("m1_small.py", "c4o_ms")
    o = MS.compute()
    res = {n.split()[0]: ok for n, ok in MS.checks(o)}
    return dict(N1=res.get("N1", False), N4=res.get("N4", False), r_free=o["k5"]["r_free"])


def equator():
    """P2: the equator's extrinsic curvature in the Kruskal form, F and r arbitrary functions of U V"""
    U, V, chi, th, ph = sp.symbols("U V chi theta phi", real=True)
    F = sp.Function("F")(U * V)
    R = sp.Function("R")(U * V)
    g = sp.zeros(5, 5)
    g[0, 1] = g[1, 0] = -F / 2
    ang = [1, sp.sin(chi) ** 2, sp.sin(chi) ** 2 * sp.sin(th) ** 2]
    if MUT.get("bent_equator"):
        ang = [1, sp.sin(chi) ** 2 * (1 + sp.cos(chi)), sp.sin(chi) ** 2 * sp.sin(th) ** 2]   # breaks chi -> pi - chi
    for i, a in enumerate(ang):
        g[2 + i, 2 + i] = R ** 2 * a
    # unit normal along chi: n^chi = 1/R; K_ab = (1/2) n^chi d_chi g_ab on the surface's tangent directions
    K = [sp.simplify((sp.diff(g[i, i], chi) / (2 * R)).subs(chi, sp.pi / 2)) for i in (3, 4)]
    K_tu = [sp.simplify((sp.diff(g[0, 1], chi) / (2 * R)).subs(chi, sp.pi / 2))]
    return dict(K=K + K_tu, zero=all(k == 0 for k in K + K_tu))


def c1_parts():
    C1 = _load("c1_oneway.py", "c4o_c1")
    res = {n.split()[0]: ok for n, ok in C1.checks(C1.compute())}
    return {k: res[k] for k in ("K1", "K2", "K3", "K4")}


def positive():
    EP = _load("e_positive.py", "c4o_ep")
    x = EP.example()
    e, sn = sp.symbols("e s", positive=True)                 # s = sin a in (0, 1], a ray's angle to the plane
    P, cs2 = sp.symbols("P c2", nonnegative=True)            # c2 = cos^2 a; P with e + P >= 0
    share = e * sn + (e + P) * cs2 / sn
    return dict(R=x["R"], R_rh=x["R_rh"], share_pos=bool(share.is_positive))


def state():
    """P5: the collapse-formed state's outgoing flux on P1 at r = r_h, against sigma"""
    H = _load("hold_small.py", "c4o_hold")
    life = H.l5_checks()["life"]
    PG = _load("p2_gravity.py", "c4o_pg")
    l5 = (PG.HBAR * PG.G * PG.ELL_MAX / PG.C ** 3) ** (1 / 3)
    N = 2742570311524972
    rh = (2 * N * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    E = 3 * math.pi * PG.C ** 4 * rh ** 2 / (8 * PG.G * PG.ELL_MAX)
    sigma = 3 * PG.C ** 4 / (4 * math.pi * PG.G * PG.ELL_MAX ** 2)
    P = E / (2 * life)
    if MUT.get("bath_kept"):
        P = 2 * P                                          # the mutant keeps the bath's ingoing half too
    rho = P / (4 * math.pi * rh ** 2 * PG.C)
    return dict(P=P, ratio=rho / sigma, life=life)


def compute():
    return dict(k=komar(), eq=equator(), c1=c1_parts(), pos=positive(), st=state())


def report(o):
    print("c4_oneway.py -- claim C4 re-posed on the one-way object (item 282)\n")
    print("P1 m1_small N1 %s, N4 %s; Komar mass free of r: %s" % (o["k"]["N1"], o["k"]["N4"], o["k"]["r_free"]))
    print("P2 the equator's extrinsic curvature in the Kruskal form, any F(UV), r(UV): %s -- zero: %s; c1_oneway %s" % (
        o["eq"]["K"], o["eq"]["zero"], o["c1"]))
    p = o["pos"]
    print("P4 the README carries P2 past sigma/4 within %.3g m = %.3g r_h; the crossing share positive: %s" % (
        p["R"], p["R_rh"], p["share_pos"]))
    s = o["st"]
    print("P5 luminosity %.3g W (life %.3g s); outgoing flux on P1 at r_h: %.2g sigma (m1_small N4's bath: 0.305)" % (
        s["P"], s["life"], s["ratio"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("P0 M's item-282 words verbatim in the rulings file", M282 in rul)
    add("P1 203 kept: the Komar mass 3 pi r_h^2/(8 G5), free of r at flat order (m1_small N1, N4)",
        o["k"]["N1"] and o["k"]["N4"] and o["k"]["r_free"])
    add("P2 the equator is totally geodesic in the Kruskal form for any F(UV), r(UV) -- every chart of the object; "
        "C1's (a), (c), (d) and the faces and route hold (c1_oneway K1-K3)", o["eq"]["zero"] and o["c1"]["K1"] and
        o["c1"]["K2"] and o["c1"]["K3"])
    add("P3 regular on both exteriors and faces (c1_oneway K4)", o["c1"]["K4"])
    p = o["pos"]
    add("P4 P2 positive where the README lands: above sigma/4 within 2.0e-15 m = 1.8e5 r_h; the crossing share positive",
        "%.2g" % p["R"] == "2e-15" and "%.2g" % p["R_rh"] == "1.8e+05" and p["share_pos"])
    s = o["st"]
    add("P5 the collapse-formed state's outgoing flux on P1 at r_h is 0.29 sigma, the order of N4's bath",
        "%.2f" % s["ratio"] == "0.29")
    return res


MUTANTS = {"bent_equator": "the reflection chi -> pi - chi broken in the angular metric",
           "bath_kept": "the Hartle-Hawking bath's ingoing half kept"}


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
        print("  mutant %-14s %-58s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
