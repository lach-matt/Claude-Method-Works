#!/usr/bin/env python3
"""m1p2x_fifth.py -- item 266: the fifth coordinate m1p2x_index.py predicts, sought among the four candidates in M's
order, each added to the index, the index repopulated and the cypher run every time.  M: "All four, in this order".
Worked in the conversation (computed with sympy and mpmath, exact where marked; deduced where marked; the cypher run
and audited; not verified by a separate session; not seated); 2026-10-11.

[M, item 270: "You are forgetting that the passage is one-way only".  This instrument populated the eternal hole's
half-horizons as if the corridor ran both ways -- position 2's future horizon and our past horizon (V = 0) are the
reverse passage, and its past horizons were stretched to an infinite past.  Superseded by m1p2x_oneway.py; kept as
the record of the two-way reading, its computations (the junction's law, the crossing share, the sweeps) standing.]

  Z0 (read) M's item-266 words, verbatim in the rulings file.
  F1 (computed, exact) The junction's starting null energy over the finite hold.  An observer of Killing energy E~
     falling across a junction at Kruskal U sees the surface energy mu E~/(kappa U) (the delta(V) integral of S_ab u^a
     u^b, with u . xi = -E~ and xi = kappa U d/dU on the horizon) -- over the 2-sphere 4 pi r_h^3 E~ (mu_0/U - [lambda])
     by m1p2x_index Y1.  The start decays as e^(-tau) in clocks; what is left is fixed by the tension's jump: on
     position 2's horizons with the hole's interiors at +sigma, -(10/pi)(r_h/ell) E~ E -- -2.6e-15 E~ E at the example
     README (sigma = 3 c^4/(4 pi G ell^2), p2_planck).  If the README's own E is laid on the junction (seen at E~ = 1
     where it is laid), it pays for the fall for ln((pi/10)(ell/r_h)) = 33.6 clocks after; the hold is the write, at
     least 66,980 clocks (write_small S3).  So
     the start, the README's or any, does not carry a falling junction through the hold: the coordinate repopulates
     no profile, and the all-four cell stays unreached and admitted.
  F2 (computed; deduced where marked) 183's pairing, net per ray.  A null ray of f = 1 - r_h^2/r^2 that scatters sweeps
     more than pi in its orbital plane at every impact parameter (computed: 1.351 pi at b = 2.2 r_h, 1.113 pi at 3,
     1.033 pi at 5, 1.0019 pi at 20, 1.0000008 pi at 1000), so it crosses the plane's great 2-sphere at least once
     (deduced: an arc longer than pi holds one of any antipodal pair), and every crossing lies in the exterior it
     scatters in (no causal curve joins the exteriors, C1).  Each crossing of a pure tension q adds q (b/r) sin psi
     (|n.k| from the conserved b; psi the orbital plane's tilt; far_cypher F8).  So every ray crossing position 2's
     plane at -sigma/4 has negative net null energy -- nothing positive lies on it.  For a negative piece inside the
     hole, a ray of small b sweeps less than pi and its phase is free, so one can be laid across that piece alone
     (deduced).  Net per ray is then non-negative on every ray if and only if no piece of the plane has negative
     tension: z_net is the index's pointwise Z, and 139 (1) excludes it.  Repopulated, the cypher no longer admits the
     all-four cell in geometry or statistics -- (keeps139, z_net) = (1, 1) lies outside the shadow's hull and is an
     unseen marginal -- so under 183 the cell is excluded, not merely missing, unless something positive lies on
     those rays: the negative pieces' own matter, its surface energy at least sigma/4 with rho + p >= 0 (m1x_cypher X2's
     e >= 0, e + P >= 0) -- 184 "There are no matter free planes", 139 (2) "positive, and you have to prove it".
     Named, not computed.
  F3 (computed) Formation.  A hole formed by collapse has only exterior I and the future interior on the plane (C1
     verifier, item 254): no position 2 side, no exterior II for a plane apart, so 139 (1) and reading the leg are 0 in
     every formed cell; on F2's coordinate a formed hole with a negative interior has net per ray 0.  Added, it
     repopulates (0, 0, 0, 0) and (0, 0, 1, 1); the all-four cell stays as F2 left it.
  F4 (computed at flat order; deduced at warp order) Position 2's own bulk, ell_2 = 2 ell (m1x_cypher X0).  Near the
     hole the bulk's curvature enters as r^2/ell^2 -- r_h^2/ell^2 = 6.4e-31 at the example -- so at flat order it
     changes no cell.  At warp order two bulks of different Lambda (-6/ell^2 and -6/ell_2^2) joined through one bridge
     meet across a bulk junction carrying stress, by the bulk's own Codazzi equation as X2 found for the plane --
     another stress, in the bulk, not on the plane; it moves none of the four properties.
  Z (deduced) None of the four fills the all-four cell.  F1 and F3 repopulate nothing; F4 adds a bulk stress; F2 turns
     the cell from missing to excluded in two languages.  What F2 names as the partner -- positive null energy on
     position 2's negative pieces, its own matter -- is the board's reading of where the index now points: a
     candidate sixth coordinate, for M.

What this does not show.
  - The partner's magnitude and whether position 2's plane's matter can meet it (F2); the bulk junction's stress (F4).
  - Infalling rays' net (F2): with the interiors at +sigma a ray crossing position 2's plane outside and the plane
    inside can be paired; not needed for the verdict, since the scattering rays already break it.

Imports m1p2x_index.py, write_small.py, p2_gravity.py, index_audit.py and tools/cypher.py by path.  Stdlib + sympy +
mpmath.  python3 m1p2x_fifth.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M266 = "All four, in this order"
N_EX = 2742570311524972
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
COORDS = ["keeps139", "reads_leg", "d_ours", "nec"]
LANGS = ("order", "algebra", "geometry", "information", "statistics")


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


def cypher(profiles, tag):
    held = sorted(set(profiles))
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "m5_cy_" + tag)
    ia = _load(os.path.join(HERE, "index_audit.py"), "m5_ia_" + tag)
    ix = cy.Index("m1p2x_" + tag, COORDS, [list(c) for c in held], value_order={c: [0, 1] for c in COORDS})
    run = cy.run(ix, "1173", dict(OPTS))
    adm = {}
    for lg in LANGS:
        a, _ = cy.ADMISSION[lg][0](ix, dict(OPTS))
        adm[lg] = None if a is None else (1, 1, 1, 1) in {tuple(ix.decode[i][x[i]] for i in range(4)) for x in a}
    return dict(held=held, reached=(1, 1, 1, 1) in held, admits=adm, E={v["language"]: v["E"] for v in run["verdicts"]},
                audit=ia.audit_index(COORDS, held))


def f1(MI, rows):
    U, F, kap, Et, mu, uV = sp.symbols("U F kappa E_t mu u_V", positive=True)
    k_u = -(F / 2) * uV
    sig = mu * k_u ** 2 * (2 / F) / uV
    sig = sp.simplify(sig.subs(uV, sp.solve(sp.Eq(kap * U * (-(F / 2)) * uV, -Et), uV)[0]))
    rh, c, G, ell = sp.symbols("r_h c G ell", positive=True)
    sigma = 3 * c ** 4 / (4 * sp.pi * G * ell ** 2)
    E = 3 * sp.pi * c ** 4 * rh ** 2 / (8 * G * ell)
    jump = sp.Rational(5, 4) * sigma
    if MUT.get("start_wins"):
        jump = 0 * sigma
    late = sp.simplify(-4 * sp.pi * rh ** 3 * Et * jump / (Et * E))
    PG = _load(os.path.join(HERE, "p2_gravity.py"), "m5_pg")
    l5 = (PG.HBAR * PG.G * PG.ELL_MAX / PG.C ** 3) ** (1 / 3)
    rh_ex = (2 * N_EX * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    late_ex = float(late.subs({rh: rh_ex, ell: PG.ELL_MAX}))
    covered = math.log(-1 / late_ex) if late_ex < 0 else float("inf")
    WS = _load(os.path.join(HERE, "write_small.py"), "m5_ws")
    hold = WS.head_clocks()
    prof = []
    for start in (0, 1):
        for cell, p in rows.items():
            falls = [j for j in p["junctions"].values() if not j["kept"]]
            kept = (not falls) or (start == 1 and covered >= hold)
            prof.append((p["keeps139"], p["reads_leg"], p["d_ours"], int(kept)))
    return dict(sig=sig, late=late, late_ex=late_ex, covered=covered, hold=hold, cy=cypher(prof, "f1"))


def sweep(b):
    mp.mp.dps = 30
    rh = mp.mpf(1)
    rmin = mp.sqrt((b ** 2 + mp.sqrt(b ** 4 - 4 * b ** 2 * rh ** 2)) / 2)       # r^4 - b^2 r^2 + b^2 r_h^2 = 0
    h = lambda u: rmin / mp.sqrt((1 - u ** 2) * (rmin ** 2 - rh ** 2 - rh ** 2 * u ** 2))   # r = rmin/u, factored
    return float(2 * mp.quad(h, [0, 1]) / mp.pi)                                # in units of pi


def f2(rows):
    bs = (2.2, 3, 5, 20, 1000)
    sw = {b: sweep(mp.mpf(b)) for b in bs}
    every_crosses = all(s > 1 for s in sw.values())
    prof = []
    for cell, p in rows.items():
        s2, sF, sP, apart = cell
        negative_piece = min(s2, sF, sP) < 0 or apart == 1
        if MUT.get("pair_by_fiat"):
            negative_piece = False
        z_net = int(not negative_piece) if every_crosses else 1
        prof.append((p["keeps139"], p["reads_leg"], p["d_ours"], z_net))
    return dict(sweeps=sw, every_crosses=every_crosses, cy=cypher(prof, "f2"), prof=prof)


def f3(rows, f2r):
    formed = []
    for sF in (sp.Rational(-1, 4), sp.Integer(1)):
        junction = sF != 1                     # only our future horizon borders F
        # on F2's coordinate (net per ray): a negative interior piece can be crossed alone, so z_net = 0 there
        formed.append((0, 0, int(not junction), int(bool(sF > 0))))
    return dict(formed=formed, cy=cypher(f2r["prof"] + formed, "f3"))


def f4(f3r):
    PG = _load(os.path.join(HERE, "p2_gravity.py"), "m5_pg4")
    l5 = (PG.HBAR * PG.G * PG.ELL_MAX / PG.C ** 3) ** (1 / 3)
    rh_ex = (2 * N_EX * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    lam_ratio = (rh_ex / PG.ELL_MAX) ** 2
    lam1, lam2 = -6, sp.Rational(-6, 4)        # -6/ell^2 and -6/(2 ell)^2, in units of 1/ell^2
    return dict(curv=lam_ratio, jump=lam1 - lam2, cy=f3r["cy"])


def compute():
    MI = _load(os.path.join(HERE, "m1p2x_index.py"), "m5_mi")
    law = MI.junction_law()
    rows = MI.populate(law)
    r1 = f1(MI, rows)
    r2 = f2(rows)
    r3 = f3(rows, r2)
    return dict(f1=r1, f2=r2, f3=r3, f4=f4(r3))


def report(o):
    print("m1p2x_fifth.py -- the fifth coordinate, sought among M's four candidates (item 266)\n")
    a = o["f1"]
    print("F1 seen surface energy %s; late, over E~ E: %s = %.3g at the example; the README covers %.1f clocks, the hold "
          "%.0f" % (a["sig"], a["late"], a["late_ex"], a["covered"], a["hold"]))
    for k in ("f1", "f2", "f3"):
        c = o[k]["cy"]
        print("   %s cypher: profiles %d, all-four reached %s, admitted %s, audit %s" % (k.upper(), len(c["held"]),
                                                                                    c["reached"], c["admits"], c["audit"]))
    print("F2 sweeps (x pi): %s" % {b: round(s, 7) for b, s in o["f2"]["sweeps"].items()})
    print("F3 formed cells %s" % o["f3"]["formed"])
    print("F4 bulk curvature at the hole r_h^2/ell^2 = %.2g; Lambda jump %s / ell^2" % (o["f4"]["curv"], o["f4"]["jump"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("Z0 M's item-266 words verbatim in the rulings file", M266 in rul)
    a = o["f1"]
    E_t, mu, U, kap = sp.symbols("E_t mu U kappa", positive=True)
    rh, ell = sp.symbols("r_h ell", positive=True)
    ok = sp.simplify(a["sig"] - E_t * mu / (U * kap)) == 0 and sp.simplify(a["late"] + 10 * rh / (sp.pi * ell)) == 0
    ok &= "%.2g" % a["late_ex"] == "-2.6e-15" and "%.1f" % a["covered"] == "33.6" and a["covered"] < a["hold"]
    ok &= not a["cy"]["reached"] and all(a["cy"]["admits"].values())
    add("F1 seen energy mu E~/(kappa U); late -(10/pi)(r_h/ell) E~ E = -2.6e-15; the README covers 33.6 clocks of a "
        "66,980-clock hold; the all-four cell unreached, admitted by every language", ok)
    b = o["f2"]
    ok = b["every_crosses"] and abs(b["sweeps"][2.2] - 1.3508546) < 1e-6 and abs(b["sweeps"][3] - 1.1130811) < 1e-6
    ok &= not b["cy"]["reached"] and b["cy"]["admits"]["geometry"] is False and b["cy"]["admits"]["statistics"] is False
    add("F2 every scattering ray sweeps more than pi (1.351 pi at 2.2 r_h ...); net per ray = pointwise; the all-four "
        "cell refused by geometry and statistics", ok)
    c = o["f3"]
    add("F3 formed cells keep neither 139 (1) nor the leg; the cell stays unreached",
        all(x[0] == 0 and x[1] == 0 for x in c["formed"]) and not c["cy"]["reached"])
    d = o["f4"]
    add("F4 the bulk's curvature at the hole is 6.4e-31 (flat order unchanged); the two bulks' Lambda differ by 9/2 "
        "per ell^2", "%.2g" % d["curv"] == "6.4e-31" and d["jump"] == sp.Rational(-9, 2))
    return res


MUTANTS = {"start_wins": "the tension jump left out of the junction's late energy (the start always wins)",
           "pair_by_fiat": "every ray taken as paired (net per ray never negative)"}


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
        print("  mutant %-12s %-72s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
