#!/usr/bin/env python3
"""m1p2x_oneway.py -- item 270: M1P2x's index repopulated on the one-way corridor.  M: "You are forgetting that the
passage is one-way only" -- the seated O1a and M's own 132: "the passage is one way by nature, a black hole in and a
white hole out, side views of the same corridor object *different views of the same object", position 2's face its
white-hole (past) horizon (122 (3)).  m1p2x_index, m1p2x_fifth and m1p2x_sixth populated the eternal hole's four
half-horizons as if the corridor ran both ways; this instrument populates the one-way object instead.  Worked in the
conversation (computed with sympy, exact where marked; deduced where marked; the cypher run and audited; not verified by
a separate session; not seated); 2026-10-11.

[M, item 277: "You are forgetting that the passage is one-way only".  O6 (a)'s "not position 2's ambient fields" let them reach the white-hole face -- a passage from
position 2 into the corridor.  Kept as written; i_oneway.py I3.]

[Item 272's owed items, worked 2026-10-12 after M's "Not yet, we have to close everything that is still owed": (b) the
interior's continuation -- b_interior.py (Penrose) and, under item 273's quantum bounce, b_bounce.py; (c) the junction's
ends and (a) the white-hole blueshift -- c_junction.py (position 2's face open at most 33.6 clocks; the bounce
asymmetric); (d) eternal versus evaporating -- d_evap.py (the hole bounces 4.4e7-1.2e10 times sooner than it
evaporates); (e) the proof 139 (2) orders -- e_positive.py (positive with expansion only where the warp decays on every
side; with like sides, rho_m > sigma/4).  O6 and the list below are kept as written.]

[Item 329: C8 brought level with items 275-328 and audited to completion in c8_level.py V0-V9 -- the index under
275 (apart = 0), the face's junction on every reading of position 2's side (310 (7)), 274's caveat closed on the
computed rows, every owed item one-way, and the question through the calculator clause by clause (291).  O5-O6 and
the list below are kept as written.]

  O0 (read) M's item-270 and item-132 words, verbatim in the rulings file.
  O1 (computed, exact) The one object is one null surface.  With U = -e^(-kappa (t - r*)), V = e^(kappa (t + r*)) the
     Killing field is xi = kappa (-U d_U + V d_V); on U = 0 it is kappa V d_V.  So U = 0 carries both of O1a's views:
     our black-hole face (U = 0, V > 0: our future horizon) and position 2's white-hole face (U = 0, V < 0: its past
     horizon) -- the record's S5, "P1's future horizon and P2's past horizon are one null surface", at the small end.
     The other surface, V = 0, is our past horizon (a white hole facing us) and position 2's future horizon (a black
     hole facing position 2): the reverse passage, no face of a one-way corridor.  On our face the affine V grows as
     e^(kappa tau) (unbounded); on position 2's face, in position 2's forward time, V = -|V_0| e^(-kappa tau_2) -> 0:
     the face's future affine extent from any point V_open is |V_open|, finite.
  O2 (deduced; H-ONE-INTERIOR, the board's reading of 132's "different views of the same object") The interior is one
     object, seen as a black hole from our side and as a white hole from position 2's: one tension, s_in.
  O2b (computed; item 272) What O2 rests on.  The index below holds on the glued object -- our exterior and its future
     interior continuing into position 2's past interior and exterior, no V = 0 border.  On the eternal Kruskal
     manifold the regions beside V = 0 still exist, and the key cell (s2 = -sigma/4, interior at our tension) carries a
     jump on position 2's future horizon whose null energy falls (m1p2x_index's cell (-1/4, 1, 1, 0), recomputed here).
     So the result rests on owed item (b), the interior's continuation.
  O3 (computed, exact; m1p2x_index Y1's law mu' = -[lambda]) The faces begin at the corridor's opening, not in an
     infinite past.  On our face [lambda] = s_in - sigma, so mu' = sigma - s_in >= 0 for every s_in <= sigma: a junction
     there only rises, kept from any non-negative start.  On position 2's face [lambda] = s2 - s_in, mu' = s_in - s2:
     with 139 (1)'s s2 = -sigma/4 it rises for every s_in -- kept from any non-negative start; it falls only if s2 =
     +sigma and s_in = -sigma/4, and then a finite start, (5/4) sigma |V_open|, covers the face's bounded extent.  So on
     the one-way object no junction loses its null energy: the "falling" junctions of m1p2x_index lay on position 2's
     future horizon (V = 0, the reverse passage) or on past horizons stretched to an infinite past.
  O4 (deduced) No inflow from position 2 (132, 270): position 2's matter cannot fall into the object -- m1p2x_sixth W2's
     "falls through" is excluded -- and static matter cannot stand at the face (W2: (u.l)^2 = 1/f); so at its face
     position 2's matter emerges, the white hole's outflow.  What emerges is the README (115 (c); 139 (3): "the
     README/information itself is the trigger").
  O5 (computed; the cypher, roster 1173, audited) The one-way index: s2, s_in in {-sigma/4, +sigma}, apart in {0, 1},
     m2 in {0, 1: position 2's own matter, total positive (268), emerging at the face} -- 16 cells; properties keeps139,
     reads_leg, d_ours (no junction on our face: s_in = sigma), nec (every junction keeps mu >= 0 over its face), z_net
     (every crossing ray's share >= 0: m2 = 1 or no negative piece).  All five are reached: position 2's plane at
     -sigma/4 through the bridge, the object's interior at our tension, the one junction on position 2's white-hole
     face rising from the opening, position 2's own matter emerging -- with or without a plane apart.  Over the four
     without z_net, m2 = 0 reaches them too.  m1p2x_index's exclusivity of (d) on our side and the junctions' null
     energy (Y3) was the two-way reading's: one-way, they hold together.
  O6 (named, not computed) What the one-way object still owes.  (a) The white-hole face's blueshift (item 271 (3)):
     at kappa = c^2/r_h any flux from position 2 meeting the white-hole face is blueshifted one e-fold per clock --
     e^66980 over the write's floor (Eardley's white-hole instability); one-way excludes inflow as the corridor's
     traffic, not position 2's ambient fields.  (b) How the black-hole interior continues into the white-hole interior
     (H-ONE-INTERIOR names it, nothing constructs it).  (c) The junction's start at the opening and its end at the
     closing (CLOSE).  (d) The one-way object is a black hole on our side with no past horizon facing us -- C5's
     "eternal versus evaporating" (item 267 (5)) is to be re-read on it.

What this does not show.
  - The proof 139 (2) orders (position 2's matter rho >= sigma/4, m1p2x_sixth W5) and O6's four.
  - Which statuses move: M1P2x stays OPEN until M has the one-way index.

Imports m1p2x_index.py, index_audit.py and tools/cypher.py by path.  Stdlib + sympy.
python3 m1p2x_oneway.py [--selftest | --mutants]
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
M270 = "You are forgetting that the passage is one-way only"
M132 = "the passage is one way by nature, a black hole in and a white hole out"
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
NEG, POS = sp.Rational(-1, 4), sp.Integer(1)
PROPS = ["keeps139", "reads_leg", "d_ours", "nec", "z_net"]


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


def flows():
    t, rs, kap = sp.symbols("t r_star kappa", positive=True)
    U = -sp.exp(-kap * (t - rs))
    V = sp.exp(kap * (t + rs))
    xi_U = sp.simplify(sp.diff(U, t) / U)                 # -kappa
    xi_V = sp.simplify(sp.diff(V, t) / V)                 # +kappa
    tau, tau2, V0 = sp.symbols("tau tau_2 V_0", positive=True)
    ours = V0 * sp.exp(kap * tau)                          # our face, V > 0, along xi
    theirs = -V0 * sp.exp(-kap * tau2)                     # position 2's face, V < 0, position 2's forward time
    return dict(xi_U=xi_U, xi_V=xi_V, ours_lim=sp.limit(ours, tau, sp.oo), theirs_lim=sp.limit(theirs, tau2, sp.oo))


def junctions(law, s2, s_in):
    """the one-way object's two faces; mu' from m1p2x_index Y1 with the face orientations of its BORDERS"""
    s = law["mu_prime"]
    out = {}
    faces = {"our black-hole face": (s_in, POS, "unbounded"), "position 2's white-hole face": (s2, s_in, "bounded")}
    if MUT.get("two_way"):
        faces["position 2's future horizon"] = (s_in, s2, "unbounded")     # the reverse passage, put back
    for name, (plus, minus, extent) in faces.items():
        if plus == minus:
            continue
        mp = s.subs({law["lp"]: plus, law["lm"]: minus})
        if MUT.get("eternal_past") and name == "position 2's white-hole face":
            kept = bool(mp <= 0)               # the infinite-past reading of m1p2x_index Y2
        else:
            kept = bool(mp >= 0) or extent == "bounded"     # rising: any start; falling: only a bounded face
        out[name] = dict(mu_prime=mp, kept=kept, rising=bool(mp >= 0))
    return out


def populate(law):
    rows = {}
    for s2, s_in, apart, m2 in itertools.product((NEG, POS), (NEG, POS), (0, 1), (0, 1)):
        js = junctions(law, s2, s_in)
        neg = [v for v in (s2, s_in) if v == NEG] + ([NEG] if apart else [])
        rows[(s2, s_in, apart, m2)] = dict(
            keeps139=int(s2 == NEG or apart == 1), reads_leg=int(s2 == NEG),
            d_ours=int("our black-hole face" not in js), nec=int(all(j["kept"] for j in js.values())),
            z_net=int(m2 == 1 or not neg), junctions=js)
    return rows


def cypher(rows, coords, tag):
    held = sorted({tuple(p[c] for c in coords) for p in rows.values()})
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "mow_cy_" + tag)
    ia = _load(os.path.join(HERE, "index_audit.py"), "mow_ia_" + tag)
    ix = cy.Index("m1p2x_oneway_" + tag, coords, [list(c) for c in held], value_order={c: [0, 1] for c in coords})
    run = cy.run(ix, "1173", dict(OPTS))
    target = tuple([1] * len(coords))
    return dict(held=held, reached=target in held, E={v["language"]: v["E"] for v in run["verdicts"]},
                audit=ia.audit_index(coords, held),
                holders=sorted(c for c, p in rows.items() if tuple(p[x] for x in coords) == target))


def compute():
    MI = _load(os.path.join(HERE, "m1p2x_index.py"), "mow_mi")
    law = MI.junction_law()
    rows = populate(law)
    two_way = MI.populate(law)
    excl_two_way = not any(p["d_ours"] and p["nec_kept"] for p in two_way.values() if p["keeps139"] and p["reads_leg"])
    eternal_key = two_way[(NEG, POS, POS, 0)]["junctions"]
    return dict(fl=flows(), rows=rows, c5=cypher(rows, PROPS, "five"), c4=cypher(rows, PROPS[:4], "four"),
                excl_two_way=excl_two_way, eternal_key=eternal_key)


def report(o):
    f = o["fl"]
    print("m1p2x_oneway.py -- M1P2x's index on the one-way corridor (item 270)\n")
    print("O1 xi = (%s) U d_U + (%s) V d_V; our face's affine V -> %s, position 2's -> %s" % (
        f["xi_U"], f["xi_V"], f["ours_lim"], f["theirs_lim"]))
    print("O5 %-34s %s  junctions" % ("cell (s2, s_in, apart, m2)", " ".join("%-9s" % p for p in PROPS)))
    for cell, p in o["rows"].items():
        js = "; ".join("%s mu' %s%s" % (n, j["mu_prime"], "" if j["rising"] else " (falls, bounded face)")
                       for n, j in p["junctions"].items()) or "none"
        print("   %-34s %s  %s" % (str(tuple(str(x) for x in cell)), " ".join("%-9d" % p[q] for q in PROPS), js))
    for k in ("c4", "c5"):
        c = o[k]
        print("   %s: profiles %d, all reached %s, E %s, audit %s" % (k, len(c["held"]), c["reached"], c["E"], c["audit"]))
        for h in c["holders"]:
            print("      holder %s" % (tuple(str(x) for x in h),))
    print("   the two-way index's exclusivity of d_ours and nec (m1p2x_index Y3) reproduced: %s" % o["excl_two_way"])


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("O0 M's item-270 and item-132 words verbatim in the rulings file", M270 in rul and M132 in rul)
    f = o["fl"]
    kap = sp.Symbol("kappa", positive=True)
    add("O1 xi = kappa(-U d_U + V d_V); our face's affine extent unbounded, position 2's bounded (V -> 0)",
        sp.simplify(f["xi_U"] + kap) == 0 and sp.simplify(f["xi_V"] - kap) == 0 and f["ours_lim"] == sp.oo
        and f["theirs_lim"] == 0)
    rows = o["rows"]
    key = rows[(NEG, POS, 0, 1)]
    ok = list(key["junctions"]) == ["position 2's white-hole face"] and key["junctions"]["position 2's white-hole face"][
        "rising"] and all(j["kept"] for p in rows.values() for j in p["junctions"].values())
    add("O3 one-way: with s2 = -sigma/4 and the interior at our tension the one junction lies on position 2's "
        "white-hole face, rising; no junction on the object loses its null energy", ok)
    c5, c4 = o["c5"], o["c4"]
    ok = c5["reached"] and (NEG, POS, 0, 1) in c5["holders"] and (NEG, POS, 1, 1) in c5["holders"]
    ok &= all(h[0] == NEG and h[1] == POS and h[3] == 1 for h in c5["holders"])
    ok &= c4["reached"] and (NEG, POS, 0, 0) in c4["holders"] and o["excl_two_way"]
    add("O5 all five properties reached: position 2 at -sigma/4, the interior at ours, its matter emerging; the four "
        "without z_net with or without matter; the two-way exclusivity was the two-way reading's", ok)
    ek = o["eternal_key"]
    name = "position 2's future horizon (V = 0, U > 0)"
    add("O2b on the eternal manifold the key cell carries a falling jump on position 2's future horizon: the result "
        "rests on the interior's continuation", name in ek and not ek[name]["kept"])
    return res


MUTANTS = {"two_way": "position 2's future horizon (the reverse passage) put back as a face",
           "eternal_past": "position 2's white-hole face stretched to an infinite past (m1p2x_index Y2's rule)"}


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
        print("  mutant %-12s %-74s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
