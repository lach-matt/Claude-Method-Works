#!/usr/bin/env python3
"""m1p2x_small.py -- chain input M1P2x ("position 2's side reads eq. (17)'s other leg", OPEN) at the family's small end
(items 251, 256, 263).  Between universes, M's 139 (1) puts position 2's plane at negative tension, a quarter of ours
(H-P2-NEGATIVE-PLANE), counted once (200 (1)); M's 203: the corridor is where the two planes' own bulks meet.  At the
small end the corridor is the localized hole, our plane its equator in exterior I and position 2's side the second
exterior (C1 H4).  Worked in the conversation (computed with sympy, exact where marked; deduced where marked; the
cypher run and audited; not verified by a separate session; not seated); 2026-10-11.

[M, item 270: "You are forgetting that the passage is one-way only".  This instrument populated the eternal hole's
half-horizons as if the corridor ran both ways -- position 2's future horizon and our past horizon (V = 0) are the
reverse passage, and its past horizons were stretched to an infinite past.  Superseded by m1p2x_oneway.py; kept as
the record of the two-way reading, its computations (the junction's law, the crossing share, the sweeps) standing.]

  X0 (read) M's words, verbatim in the rulings file: 139 "1 - yes" (to "whether position 2's plane is the negative-
     tension one, a quarter of ours, with ours positive", the board's question); 200 (1) "1 - Once: k_R = k_L/2".
  X1 (computed, exact) Position 2's side reads the other leg.  The Kruskal form -F(r) dU dV has r a function of UV
     alone, and (U, V) -> (-U, -V) keeps UV: an isometry exchanging exteriors I and II and leaving the equator in place.
     So a plane on exterior II's equator reads the same f = 1 - r_h^2/r^2 as ours -- at flat order, where each plane's
     tension bends it by r_h/ell (ours) and r_h/ell_2 = r_h/(2 ell) (position 2's, counted once: m1x_cypher X0).
  X2 (computed, exact; the general case deduced) A pure tension is constant on a connected plane.  With a vacuum bulk
     on both sides, Codazzi's equation gives D_a (K^a_b - delta^a_b K) = 0 on each side, and Israel's [K_ab - h_ab K] =
     -kappa^2 S_ab then gives D_a S^a_b = 0; for S_ab = -lambda h_ab that is d_b lambda = 0.  Computed in the mirrored
     case: D_a (K^a_b - delta^a_b K) = (kappa^2/2) d_b lambda.  A tension that changes along the plane needs a stress
     beyond tension where it changes.
  X3 (computed, exact: the plane's own Kruskal regions enumerated) The equator through the bridge is one connected
     plane: exteriors I (U < 0 < V) and II (V < 0 < U) and the hole's interiors F (U, V > 0) and P (U, V < 0), F and P
     each bordering both exteriors along the plane's horizons.  With ours at +sigma on I and position 2's at -sigma/4
     on II, every assignment of F's and P's tension leaves the change on exactly two of the four half-horizons, and
     every such surface passes through the bifurcation 2-sphere U = V = 0 -- the throat on the bridge's slice, where the
     README crosses (C1 H4, item 251).  So 139 (1)'s two tensions on one plane put a null stress on a horizon of the
     plane through the throat: the record's "ring at the fold" (m1_cypher, item 231) returns at the small end, in null
     form, between universes.  [Its magnitude is not computed: the jump is [lambda] = 5 sigma/4.]
  X4 (computed) (Z) on position 2's plane at -sigma/4: a ray crossing a pure tension q at angle a sees q sin a (far_cypher
     F8; write_cypher WZ) -- negative at every a for q < 0: pointwise broken; net per ray (183) not computed (U).
  X5 (computed; the cypher, roster 1173, audited) Which position 2's plane at the small end?  Three readings, three
     properties, each computed above: (A) one plane, one tension -- position 2's side is our plane continued at +sigma
     (conserved; reads the leg; 139 (1) set aside between universes); (B) one surface, two tensions -- +sigma | -sigma/4
     with X3's junction stress (139 (1) kept; reads the leg; not conserved without added stress); (C) position 2's
     plane apart from the bridge -- -sigma/4 elsewhere in exterior II (139 (1) kept; conserved; does not read the leg).
     No reading holds all three: a trilemma, computed.  The index is a one-cold code -- each cell lacks exactly one
     property -- so the cypher's verdicts are forced by its construction and void as evidence (item 211; index_audit
     flags it); the cypher is run and reported, not silent (196).  Which property gives way is not the math's: (A) sets
     aside M's 139 (1) between universes, (B) adds a stress at the throat beside 251's "README only", (C) changes what
     M1P2x asks.

What this does not show.
  - The junction stress's magnitude and its energy conditions (B); whether position 2's bulk, with its own ell_2 =
    2 ell, joins ours across the bridge without a bulk shell at warp order (between universes the two bulks' Lambda
    differ; at flat order it does not enter).
  - Net null energy per ray across position 2's negative plane (X4; F5 of write_cypher).
  - Within one universe nothing here applies: M1P2 reduces to M1 (m1p2_cypher L7), and C4's (f) -- the plane continued
    at the same positive tension -- is reading (A) there.

Imports localized_hole.py, index_audit.py and tools/cypher.py by path.  Stdlib + sympy.
python3 m1p2x_small.py [--selftest | --mutants]
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
M139 = '"1 - yes'
M200 = "1 - Once: k_R = k_L/2"
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
SIGMA = sp.Integer(1)
P2_TENSION = -SIGMA / 4                                   # 139 (1): a quarter of ours, negative


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod                                 # tools/cypher.py's dataclasses look themselves up here
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def isometry():
    """r depends on U V only (U V = -exp(2 kappa r*)); (U, V) -> (-U, -V) keeps U V"""
    U, V, r, rh = sp.symbols("U V r r_h", positive=True)
    rstar = r + rh / 2 * sp.log((r - rh) / (r + rh))
    UV = -sp.exp(2 * rstar / rh)                           # kappa = 1/r_h; exterior I
    LH = _load(os.path.join(HERE, "localized_hole.py"), "mx_lh")
    br = LH.bridge()
    Us, Vs = sp.symbols("U V")
    keeps = sp.simplify((Us * Vs).subs({Us: -Us, Vs: -Vs}, simultaneous=True) - Us * Vs) == 0
    return dict(keeps=keeps, F_closed=br["closed"], F_positive=br["finite_positive"], UV=UV)


def codazzi():
    xs = sp.symbols("t x y z")
    k = sp.Symbol("k", positive=True)
    lam = sp.Function("lam")(*xs)
    h = sp.diag(-1, 1, 1, 1)
    S = -lam * h
    if MUT.get("tension_free"):
        S = -sp.Integer(1) * h                              # the mutant forgets that lambda may vary
    Str = sum(S[i, i] / h[i, i] for i in range(4))
    K = -(k ** 2 / 2) * (S - Str * h / 3)                 # Israel, mirrored bulk
    Kmix = h.inv() * K
    div = [sp.simplify(sum(sp.diff(Kmix[a, b], xs[a]) for a in range(4)) - sp.diff(Kmix.trace(), xs[b]))
           for b in range(4)]
    return dict(div=div, expect=[sp.simplify(k ** 2 / 2 * sp.diff(lam, xs[b])) for b in range(4)])


def regions():
    """the plane's Kruskal regions and their shared half-horizons; every tension assignment for F and P"""
    border = {("F", "I"): "U = 0, V > 0", ("F", "II"): "V = 0, U > 0", ("P", "I"): "V = 0, U < 0",
              ("P", "II"): "U = 0, V < 0"}
    lam_I, lam_II = SIGMA, (SIGMA if MUT.get("positive_p2") else P2_TENSION)
    out = []
    for lF, lP in itertools.product((lam_I, lam_II), repeat=2):
        lam = dict(I=lam_I, II=lam_II, F=lF, P=lP)
        jumps = [b for (x, y), b in border.items() if lam[x] != lam[y]]
        out.append(dict(F=lF, P=lP, jumps=jumps,
                        # deduced: each border is a half-axis of the (U, V) plane, so its end is U = V = 0
                        through_bifurcation=bool(jumps) and all(j.startswith(("U = 0", "V = 0")) for j in jumps)))
    return dict(assignments=out, jump=lam_I - lam_II)


def crossing():
    a = sp.Symbol("a", positive=True)
    q = SIGMA if MUT.get("positive_p2") else P2_TENSION
    share = q * sp.sin(a)
    samples = [share.subs(a, x) for x in (sp.Rational(1, 1000), sp.pi / 6, sp.pi / 4, sp.pi / 3, sp.pi / 2)]
    return dict(share=share, all_negative=all(s < 0 for s in samples))


def trilemma(rg, cz, iso):
    # (B) is conserved without added stress only if a varying tension were divergence-free (X2) or no change were
    # forced (X3)
    conserved_B = int(all(sp.simplify(d) == 0 for d in cz["div"]) or not any(x["jumps"] for x in rg["assignments"]))
    props = {"(A) one plane, one tension": dict(keeps139=0, conserved=1, reads_leg=int(iso["keeps"])),
             "(B) one surface, two tensions": dict(keeps139=1, conserved=conserved_B,
                                                    reads_leg=int(iso["keeps"])),
             "(C) position 2's plane apart from the bridge": dict(keeps139=1, conserved=1, reads_leg=0)}
    coords = ["keeps139", "conserved", "reads_leg"]
    cells = {n: tuple(p[x] for x in coords) for n, p in props.items()}
    held = sorted(set(cells.values()))
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "mx_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "mx_ia")
    ix = cy.Index("m1p2x_small", coords, [list(cc) for cc in held], value_order={x: [0, 1] for x in coords})
    run = cy.run(ix, "1173", dict(OPTS))
    holders = sorted(n for n, cc in cells.items() if cc == (1, 1, 1))
    return dict(props=props, cells=cells, holders=holders, E={v["language"]: v["E"] for v in run["verdicts"]},
                audit=ia.audit_index(coords, held))


def compute():
    iso, cz, rg, cr = isometry(), codazzi(), regions(), crossing()
    return dict(iso=iso, cz=cz, rg=rg, cr=cr, tri=trilemma(rg, cz, iso))


def report(o):
    print("m1p2x_small.py -- M1P2x at the family's small end\n")
    print("X1 (U, V) -> (-U, -V) keeps U V: %s; the Kruskal F smooth and positive at r_h: %s" % (
        o["iso"]["keeps"], o["iso"]["F_positive"]))
    print("X2 Codazzi with Israel, mirrored: D_a (K^a_b - delta K) = %s" % o["cz"]["div"])
    print("X3 tension jump %s; assignments of (F, P):" % o["rg"]["jump"])
    for x in o["rg"]["assignments"]:
        print("     F %s, P %s -> changes on %s (all through U = V = 0: %s)" % (x["F"], x["P"], x["jumps"],
                                                                             x["through_bifurcation"]))
    print("X4 crossing share on position 2's plane %s; negative at every sampled angle: %s" % (
        o["cr"]["share"], o["cr"]["all_negative"]))
    t = o["tri"]
    print("X5 cells %s; holders of all three: %s; E %s; audit %s" % (t["cells"], t["holders"], t["E"], t["audit"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("X0 M's 139 and 200 (1) words verbatim in the rulings file", M139 in rul and M200 in rul)
    add("X1 the exteriors are isometric ((U, V) -> (-U, -V)); position 2's side reads the same f",
        o["iso"]["keeps"] and o["iso"]["F_positive"] and o["iso"]["F_closed"])
    cz = o["cz"]
    add("X2 D_a (K^a_b - delta K) = (kappa^2/2) d_b lambda: a pure tension is constant on a connected plane",
        all(sp.simplify(a - b) == 0 for a, b in zip(cz["div"], cz["expect"])))
    rg = o["rg"]
    ok = rg["jump"] == sp.Rational(5, 4) and all(len(x["jumps"]) == 2 and x["through_bifurcation"]
                                                 for x in rg["assignments"])
    add("X3 +sigma | -sigma/4 on one plane: every assignment changes tension on two half-horizons, all through the "
        "bifurcation 2-sphere (the throat); jump 5 sigma/4", ok)
    add("X4 position 2's negative tension gives every crossing ray negative null energy (pointwise)",
        o["cr"]["all_negative"])
    t = o["tri"]
    ok = t["holders"] == [] and len(t["cells"]) == 3 and t["audit"]["onehot"] != []
    add("X5 no reading holds all three (a trilemma); the index is a one-cold code, flagged by index_audit -- the "
        "cypher's verdicts void as evidence", ok)
    return res


MUTANTS = {"tension_free": "the plane's tension taken constant by fiat (lambda never varies)",
           "positive_p2": "position 2's plane at our positive tension"}


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
        print("  mutant %-12s %-60s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
