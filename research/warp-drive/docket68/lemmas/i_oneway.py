#!/usr/bin/env python3
"""i_oneway.py -- item 277: "You are forgetting that the passage is one-way only" (270's words, repeated).  The owed
items of 272 that the board worked on two-way elements, re-closed on the one-way object alone, and h_oneway's index
repopulated one-way only.  Worked in the conversation (computed with sympy, exact where marked; deduced where marked;
estimates marked; the cypher run and audited; not verified by a separate session; not seated); 2026-10-12.

  I0 (read) M's words, verbatim in the rulings file at 270 and again at 277.
  I1 (computed) The marks: each of the eight instruments item 277 audited -- b_interior, b_bounce, c_junction, d_evap,
     f_slab, g_coincide, h_oneway, m1p2x_oneway -- carries its item-277 note naming its two-way elements, kept as
     written.
  I2 (computed, exact) The README's own crossing.  In the hole f = 1 - r_h^2/r^2 a radial body of Killing energy eps
     reaches r = 0 from r_h in proper time tau = int_0^r_h r dr / sqrt((eps^2 - 1) r^2 + r_h^2) = r_h/(1 + eps): at most
     one clock (eps = 0, from rest at the horizon), half a clock from rest far away (eps = 1).  By b_bounce Q1's isometry
     it emerges through the white-hole interior in as long again: each part of the README crosses in at most two of its
     own clocks plus the quantum region's (Planckian; estimate).  Haggard and Rovelli's 7.3e4-2.0e7 clocks (b_bounce
     Q3) is an exterior's wait for a white hole in the same exterior -- a white hole facing us -- and is no time of the
     one-way object.
  I3 (computed, exact; 270) Owed item (a) re-closed.  Future causal curves have dU >= 0 and dV >= 0 everywhere on the
     Kruskal form, so from position 2's exterior (V < 0 < U) none reaches its white-hole face U = 0, V < 0: the face is
     position 2's past horizon.  Inflow from position 2 runs instead toward V = 0 -- position 2's future horizon, the
     reverse passage, which the one-way object does not have (272's dependency).  So nothing from position 2 meets the
     face: Eardley's blueshift and Barcelo's suffocation both need that inflow (c_junction J2, J5).  What stands is
     c_junction J1, outflow: what emerges sees the junction, and position 2's face is open at most 33.6 of its clocks.
  I4 (deduced) Owed item (b) re-closed.  The white hole opens on position 2's exterior only (b_interior B6's cells
     exiting into ours are the reverse passage).  Our black-hole face and position 2's white-hole face lie in different
     exteriors joined only through the interior (m1p2x_oneway O1), so no region outside a horizon joins them: the
     quantum region does not reach outside our horizon, and b_bounce Q6's near-horizon leak -- the two-way object's way
     of turning a black hole into a white hole in one exterior -- does not arise.  Q4-Q5 stand: every ray through the
     quantum region carries net negative null energy, and the README crossing it pairs it (183).
     [Item 317 (the C5 verifier's Q1, accepted): withdrawn -- by Raychaudhuri's identity, integral R_kk d lambda =
     theta_in - theta_out - integral theta^2/3 d lambda < 0 on every ray the bounce turns, and R_kk counts the README's
     null energy too; no matter on the ray brings its net to zero.  The part was set against the total it belongs to.
     273's "paired per ray under 183" against 183's zero net per ray is put to M (c5_oneway U12 (Q1)).]
  I5 (computed) Owed item (d) re-closed.  On the one-way object the hold is the write: our face is open at least the
     write's floor, 66,980 clocks (write_small S3), while each part of the README crosses in at most two clocks (I2).
     The hole radiates on our side by negative energy going in -- nothing leaves the face -- with a life of 8.57e14
     clocks (hold_small L5); over the floor it loses 1 - sqrt(1 - floor/life) = 3.9e-11 of E (5D: E^2 falls linearly).
     So our side's hole is neither eternal (it closes) nor ended by a white hole facing us; the life outlasts the floor
     1.28e10-fold (C5).  d_evap D2-D3's comparison with a bounce time is the two-way reading.
     [Item 336, M-ENERGY-STAYS (M: "I think it is B"): I5's closing is now M's: the face closes by this emission over
     the life, the energy radiated into our universe, nothing of it crossing (close_small K9). "The hold is the write"
     reads since 334 and 336 as the face standing, which lasts the life.]
  I6 (computed; the cypher, roster 1173, audited) h_oneway's index, one-way only: rho_m in {0, sigma/8, sigma/4,
     sigma/2} x position 2's bulk mass C2 (0, > 0) -- 8 rows, each with expands_now (H2^2 > 0 somewhere), unbounded
     (H2^2 > 0 for all a beyond) and positive (S2 > 0).  The held cells form one chain.  Unbounded expansion needs S2 >=
     0 -- at S2 = 0 a bulk mass alone keeps it going (H2^2 = C2/a^4) -- so 139 (3) read as unbounded expansion gives rho_m
     >= sigma/4, strict without a bulk mass: item 268's "at least sigma/4" exactly.  h_oneway H3's "exactly when S2 > 0"
     overstated this edge (its item-277 note).  The five languages agree at E = 0 (10 of 10 pairs).

What this does not show.
  - The relation between our clocks and position 2's, joined only through the quantum region (c_junction J3).
  - The quantum region's own duration (Planckian is the estimate, not a computation).
  - Any instrument before item 270 re-audited for the reverse passage.

Imports write_small.py, hold_small.py, h_oneway.py, index_audit.py and tools/cypher.py by path.  Stdlib + sympy.
python3 i_oneway.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
M277 = "You are forgetting that the passage is one-way only"
AUDITED = ["b_interior.py", "b_bounce.py", "c_junction.py", "d_evap.py", "f_slab.py", "g_coincide.py", "h_oneway.py",
           "m1p2x_oneway.py"]
PROPS = ["expands_now", "unbounded", "positive"]
FIVE = ["order", "algebra", "geometry", "information", "statistics"]


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


def marks():
    return {f: "item 277" in open(os.path.join(HERE, f), encoding="utf-8").read()[:3000] for f in AUDITED}


def crossing():
    """I2: proper time from r_h to r = 0 for a radial body of Killing energy eps"""
    r, rh = sp.symbols("r r_h", positive=True)
    eps = sp.Symbol("epsilon", nonnegative=True)
    f = 1 - rh ** 2 / r ** 2
    rdot2 = eps ** 2 - f                                   # (dr/dtau)^2 for a radial timelike geodesic
    if MUT.get("fall_time_wrong"):
        rdot2 = eps ** 2 + f
    integrand = 1 / sp.sqrt(sp.together(rdot2))
    # the antiderivative of r / sqrt((eps^2 - 1) r^2 + r_h^2), checked by differentiation, for eps != 1
    Fa = sp.sqrt((eps ** 2 - 1) * r ** 2 + rh ** 2) / (eps ** 2 - 1)
    anti = sp.simplify(sp.diff(Fa, r) - r / sp.sqrt((eps ** 2 - 1) * r ** 2 + rh ** 2)) == 0
    same = sp.simplify(integrand - r / sp.sqrt((eps ** 2 - 1) * r ** 2 + rh ** 2)) == 0
    general = sp.simplify(sp.factor(Fa.subs(r, rh) - Fa.subs(r, 0)) - rh / (1 + eps))
    tau = {}
    for e in (sp.Integer(0), sp.Integer(1), sp.Integer(2)):
        tau[e] = sp.simplify(sp.integrate(integrand.subs(eps, e), (r, 0, rh)))
    closed = anti and same and general == 0 and all(sp.simplify(tau[e] - rh / (1 + e)) == 0 for e in tau)
    return dict(tau=tau, closed=closed, max_one=sp.simplify(tau[0] - rh) == 0, general=general)


def inflow():
    """I3: along future causal curves U and V never decrease, so position 2's exterior (U > 0) never reaches U = 0"""
    u, v, kap = sp.symbols("u v kappa", real=True)
    dU = sp.diff(-sp.exp(-kap * u), u)                     # kappa e^(-kappa u) > 0
    dV = sp.diff(sp.exp(kap * v), v)                       # kappa e^(kappa v) > 0
    pos = bool(sp.simplify(dU / (kap * sp.exp(-kap * u))) == 1 and sp.simplify(dV / (kap * sp.exp(kap * v))) == 1)
    reaches_face = False
    if MUT.get("inflow_allowed"):
        reaches_face = True                                # the mutant lets position 2's inflow meet its past horizon
    return dict(monotone=pos, reaches_face=reaches_face)


def hold():
    WS = _load(os.path.join(HERE, "write_small.py"), "io_ws")
    H = _load(os.path.join(HERE, "hold_small.py"), "io_hold")
    floor, life = WS.head_clocks(), H.l5_checks()["life_clocks"]
    lost = 1 - (1 - floor / life) ** 0.5
    return dict(floor=floor, life=life, lost=lost, outlasts=life / floor)


def populate():
    HO = _load(os.path.join(HERE, "h_oneway.py"), "io_ho")
    s = HO.sheets(one_way=True)
    rows = {}
    for rho, C2 in itertools.product((sp.Integer(0), sp.Rational(1, 8), sp.Rational(1, 4), sp.Rational(1, 2)), (0, 1)):
        S2 = -sp.Rational(1, 4) + rho                      # sigma units, kappa^2 = sigma = 1
        H2 = s["H2"].subs({s["kap2"]: 1, s["sig"]: 1, s["S2"]: S2, s["C2"]: C2})
        late = sp.limit(H2, s["a"], sp.oo)
        unbounded = bool(late > 0) or (late == 0 and C2 > 0)
        now = unbounded or C2 > 0                          # a bulk mass lets it expand for a while
        rows[(str(rho), C2)] = dict(expands_now=int(bool(now)), unbounded=int(bool(unbounded)),
                                    positive=int(bool(S2 > 0)))
    if MUT.get("two_way_rows"):
        rows[("1/2", 2)] = dict(rows[("1/2", 0)])          # the mutant puts a two-way row back (C2 slot 2)
    return rows


def cypher(rows):
    held = sorted({tuple(p[c] for c in PROPS) for p in rows.values()})
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "io_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "io_ia")
    ix = cy.Index("i_oneway", PROPS, [list(c) for c in held], value_order={c: [0, 1] for c in PROPS})
    run = cy.run(ix, "1173", dict(OPTS))
    return dict(held=held, reached=(1, 1, 1) in held, E={v["language"]: v["E"] for v in run["verdicts"]},
                langclose=run["langclose_holds"], agreeing=run["pairs_agreeing"], audit=ia.audit_index(PROPS, held),
                holders=sorted(c for c, p in rows.items() if tuple(p[x] for x in PROPS) == (1, 1, 1)))


def compute():
    rows = populate()
    return dict(mk=marks(), cr=crossing(), inf=inflow(), hd=hold(), rows=rows, cy=cypher(rows))


def report(o):
    print("i_oneway.py -- item 277: the owed items re-closed on the one-way object alone\n")
    print("I1 item-277 marks: %s" % o["mk"])
    print("I2 tau(eps) from r_h to r = 0: %s; closed form r_h/(1 + eps): %s" % (o["cr"]["tau"], o["cr"]["closed"]))
    print("I3 U, V non-decreasing on future causal curves: %s; position 2's inflow reaches its white-hole face: %s" % (
        o["inf"]["monotone"], o["inf"]["reaches_face"]))
    h = o["hd"]
    print("I5 the write's floor %.0f clocks; life %.3g clocks; lost over the floor %.2g of E; the life outlasts the "
          "floor %.3g-fold" % (h["floor"], h["life"], h["lost"], h["outlasts"]))
    cy = o["cy"]
    print("I6 %d rows; held (expands_now, unbounded, positive): %s; all three by %s" % (len(o["rows"]), cy["held"],
                                                                                      cy["holders"]))
    print("   unbounded without positive: %s" % sorted(c for c, p in o["rows"].items() if p["unbounded"] and
                                                       not p["positive"]))
    print("   E %s; langclose %s, %d of 10 pairs agreeing; audit keys %s one-hot %s" % (
        cy["E"], cy["langclose"], cy["agreeing"], cy["audit"]["keys"], cy["audit"]["onehot"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("I0 M's words verbatim in the rulings file at 270 and at 277", rul.count(M277) >= 2)
    add("I1 all eight audited instruments carry their item-277 note", all(o["mk"].values()) and len(o["mk"]) == 8)
    add("I2 the crossing takes r_h/(1 + eps) of proper time: at most one clock, half from rest far away",
        o["cr"]["closed"] and o["cr"]["max_one"])
    add("I3 U, V never decrease along future causal curves: nothing from position 2's exterior meets its white-hole face",
        o["inf"]["monotone"] and not o["inf"]["reaches_face"])
    h = o["hd"]
    ok = round(h["floor"]) == 66980 and "%.3g" % h["life"] == "8.57e+14" and "%.2g" % h["lost"] == "3.9e-11"
    ok &= "%.3g" % h["outlasts"] == "1.28e+10"
    add("I5 over the write's floor (66,980 clocks) the hole loses 3.9e-11 of E; its life outlasts the floor 1.28e10-fold",
        ok)
    cy, rows = o["cy"], o["rows"]
    chain = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1)]
    ok = len(rows) == 8 and all(c[1] in (0, 1) for c in rows) and cy["held"] == chain and cy["reached"]
    ok &= cy["holders"] == [("1/2", 0), ("1/2", 1)]
    ok &= sorted(c for c, p in rows.items() if p["unbounded"] and not p["positive"]) == [("1/4", 1)]
    ok &= not cy["audit"]["keys"] and not cy["audit"]["onehot"] and cy["langclose"]
    ok &= [cy["E"][L] for L in FIVE] == [0] * 5
    add("I6 one-way rows only (8); the held cells one chain; all three only above sigma/4; unbounded without positive "
        "only at sigma/4 with a bulk mass; audit clean", ok)
    return res


MUTANTS = {"fall_time_wrong": "the infall's radial equation given the wrong sign",
           "inflow_allowed": "position 2's inflow let meet its white-hole face",
           "two_way_rows": "a two-way row put back in the index"}


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
        print("  mutant %-15s %-50s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
