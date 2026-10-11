#!/usr/bin/env python3
"""relgrav.py -- item 236: do the matter laws and the offset govern G because they provide the mass for relative gravity?
M: "No weighting touches the matter law or the offset. - do the matter laws and offsets govern G because they provide
the mass for relative gravity?"  Worked in the conversation (computed, exact where marked; READ where marked; deduced
where marked; not verified by a separate session; not seated); 2026-10-11.

"Govern G" is read two ways (item 236 (a)): G as a function of them, and gravity as what bodies feel -- G times the mass
and density matter supplies.  "Relative gravity" is gravity against matter's own scale.

  R0 (read) M's item-236 words, verbatim in the rulings file.
  R1 (computed, exact) G as a function.  Over (G, the tension, the offset, matter's density), a set of quantities fixes G
     when G's log-gradient lies in the span of theirs (exact Fractions, our offset ratio).  No minimal set of the bulk's
     and the plane's own parameters contains matter: neither its density nor its law ever helps fix G, and G is the same
     in position 1 and 2a, which differ only in the law.  The offset is a member of {curvature, tension, offset} and
     {coupling, curvature, offset}, never of {coupling, tension}: it moves G only when G is read through the bulk's
     curvature, by d ln G / d ln delta_sigma = 2r/(1 - 2r), at most 7.08e-63 in ours (r taken at our tension window's
     floor; exact in r), and not at all through the coupling (G = kappa5^4 sigma c^4 / 48 pi).  The mass that governs G is the plane's own -- its tension, an energy
     density -- carried by the bulk's coupling.
  R2 (computed; the record's bodies, p2_gravity's integrator on item 221's solids) Relative gravity: at our G a 1e22 kg
     body's surface gravity under min / mirror against ours is Cu x 1.042 / 1.084, Ag x 1.143 / 1.246, Au x 1.008 /
     1.022 -- the same as raising G for our matter by x 1.042 / 1.083, 1.141 / 1.242, 1.008 / 1.021.  The law does it
     through density (mean density up to x 1.390), not mass: an atom's mass moves by at most 3.7e-11 (Ag, mirror), so
     G m^2 / (hbar c) per atom by at most 7.5e-11.  It is a surface effect: outside the body, at a given distance, the
     pull is G M and the law moves it by less than 4e-11; at the surface it moves by up to 24.6 % because the denser
     body's surface lies closer to its centre.  So the matter law governs what a body's surface feels, as a G change of
     up to 24 % would, without touching G or the pull at a distance.
  R3 (computed) Matter is also how G is read: a body's surface gravity and matter's density fix G ({g, density} is a
     minimal set) -- the Cavendish route, G = g R^2 / M.  The surface gravity is G times matter, so this is G measured
     against the mass matter supplies, not G set by it.
  R4 (READ, computed) Above the plane's tension matter's density raises its own gravity: the braneworld's effective
     coupling at density rho is G (1 + rho / 2 sigma) (the quadratic term of Shiromizu-Maeda-Sasaki's equations, as
     in the brane Friedmann equation).  Over (G, the tension, the offset, matter's density) every minimal set of the
     bulk's, the plane's and matter's parameters fixing this effective coupling contains matter's density.  For ordinary
     matter it is negligible: gold's rho c^2 / 2 sigma <= 5.3e-33 at the bottom of our tension's window.  For the README
     at the corridor's throat it is not: E / (4/3 pi r0^3) = 9.1e97 J/m^3 at the example README, above 2 sigma over the
     lower 75.1 % of our tension's window (in doublings) -- there the README's own mass-energy governs its gravity.  The
     term is the plane's: it applies to the README as energy on our plane, arriving, at the throat's scale; the corridor
     itself lies in the bulk (179).
  R5 (READ, deduced) The offset is mass too -- rho_Lambda = 5.84e-27 kg/m^3, the record's value -- and it gravitates as
     a source (Lambda4 = 8 pi G rho_Lambda / c^2), not as the coupling; its measured value comes through the expansion
     rate read with our own G, so "the offset's mass" is itself known through G.
  R6 (computed; the cypher, roster 1173, audited) The minimal sets for G and for the effective coupling as cells over
     (which quantity, has a bulk parameter, has the tension, has the offset, has matter, has a quantity made from G).
     The target "matter fixes G with the bulk and the plane" is held by none; "matter fixes the effective coupling" by
     every set without a quantity made from G.

So: no for G -- G is the bulk's coupling carried by the plane's own tension, and neither matter nor (in ours) the offset
moves it.  Yes for relative gravity, in three ways -- matter governs what a body's surface feels through its density (as
a G change of up to 24 % would, the pull at a distance untouched), it is the mass against which G is measured, and above
the plane's tension its own density raises its gravity, which at the corridor's throat it does over three quarters of
our tension's window.

What this does not show.
  - R2's bodies are cold spheres of one metal (p2_gravity's integrator, BM3 fits); stars and planets are not computed.
  - R4's throat density is a scale comparison -- the README's E in a sphere of the throat's radius -- not the corridor's
    computed stress; the effective coupling is the high-energy term on the plane, READ, not derived here.
  - The offset's provenance through G is READ from the standard derivation of rho_Lambda, not from the record's source.

Imports p2_gravity.py, p2_matter.py, bulk5_index.py, weight_cypher.py, tools/cypher.py and index_audit.py by path.
Stdlib.  python3 relgrav.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M236 = ("No weighting touches the matter law or the offset. - do the matter laws and offsets govern G because they provide "
        "the mass for relative gravity?")
EXAMPLE_N = 2742570311524972
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
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


B5 = _load(os.path.join(HERE, "bulk5_index.py"), "rg_b5")
WC = _load(os.path.join(HERE, "weight_cypher.py"), "rg_wc")
PG = B5.PG
K = B5.constants()


# ================================================================================ R1, R3, R4 what fixes G, G_eff
CLASS = {"coupling": "bulk", "curvature": "bulk", "tension": "plane", "offset": "plane",
         "rho_m": "matter", "matter_law": "matter", "g_body": "laden", "E1": "laden", "Lambda4": "laden"}


def grads(r, x):
    """d log Q / d (log G, log sigma, log delta_sigma, log rho_m) at offset ratio r and x = rho_m / (2 sigma)"""
    q = F(1) / (1 - 2 * r)
    g = {"coupling": (1, -1, 0, 0), "curvature": (F(-1, 2), -q / 2, r * q, 0), "tension": (0, 1, 0, 0),
         "offset": (0, 0, 1, 0), "rho_m": (0, 0, 0, 1), "matter_law": (0, 0, 0, 0),
         "g_body": (1, 0, 0, F(2, 3)),            # a homogeneous body of fixed mass: g = G M^(1/3) (4 pi rho / 3)^(2/3)
         "E1": (F(-1, 2), 0, 0, 0), "Lambda4": (1, 0, 1, 0)}
    if MUT.get("matter_in_G"):
        g["rho_m"] = (1, 0, 0, 1)                 # matter's density read as carrying G (the hypothesis as a mutant)
    y = x / (1 + x)
    targets = {"G": (1, 0, 0, 0), "G_eff": (1, -y, 0, y)}
    return {k: tuple(F(v) for v in t) for k, t in g.items()}, {k: tuple(F(v) for v in t) for k, t in targets.items()}


def determines(names, gr, target):
    rows = [gr[n] for n in names]
    return bool(rows) and WC.rank(rows + [target]) == WC.rank(rows)


def minimal_sets(r, x):
    gr, tg = grads(r, x)
    out = {}
    for tname, t in tg.items():
        mins = []
        for size in (1, 2, 3, 4):
            for S in itertools.combinations(sorted(CLASS), size):
                if determines(S, gr, t) and not any(set(m) <= set(S) for m in mins):
                    mins.append(S)
        out[tname] = mins
    return out


def r1():
    r_ours = F(PG.DSIG) / F(K["S0"])
    ms = minimal_sets(r_ours, F(1))
    prim = lambda S: all(CLASS[n] in ("bulk", "plane", "matter") for n in S)
    sens = 2 * r_ours / (1 - 2 * r_ours)
    fd = B5.five_d()
    same_G = fd["ours"]["e"]["G"] == fd["2a-min"]["e"]["G"] == fd["2a-mirror"]["e"]["G"]
    return dict(r=r_ours, ms=ms, sens=sens, same_G=same_G,
                G_prim=[S for S in ms["G"] if prim(S)], Geff_prim=[S for S in ms["G_eff"] if prim(S)],
                G_laden=[S for S in ms["G"] if not prim(S)])


# ================================================================================ R2 bodies, relative gravity
def r2():
    pm = _load(os.path.join(HERE, "p2_matter.py"), "rg_pm")
    o = pm.compute()
    G = PG.G
    rows = {}
    for el in ("Cu", "Ag", "Au"):
        s0 = o["sol"][(el, "ours")]
        b0 = PG.body(1e22, s0["rho"], s0["B0"] * 1e9, s0["Bp"], G)
        for law in ("min", "mirror"):
            s = o["sol"][(el, law)]
            b = PG.body(1e22, s["rho"], s["B0"] * 1e9, s["Bp"], G)
            lo, hi = 0.9, 1.4
            for _ in range(18):
                mid = 0.5 * (lo + hi)
                bm = PG.body(1e22, s0["rho"], s0["B0"] * 1e9, s0["Bp"], G * mid)
                lo, hi = (mid, hi) if bm["g"] < b["g"] else (lo, mid)
            rows[(el, law)] = dict(g=b["g"] / b0["g"], rho=b["rho_mean"] / b0["rho_mean"], R=b["R"] / b0["R"],
                                   G_eq=0.5 * (lo + hi), dm=abs(o["mass"][el]["G0_" + law]))
    mass = {el: max(abs(v) for v in m.values()) for el, m in o["mass"].items()}
    return dict(rows=rows, mass=mass, rho_au=o["sol"][("Au", "ours")]["rho"])


# ================================================================================ R4 the high-energy term
def r4(rho_au):
    C = PG.C
    E1 = PG.corridor(PG.G)["E1"]
    E = E1 * math.sqrt(EXAMPLE_N)
    r0 = 2 * PG.G * E / C ** 4
    rho_E = E / (4 / 3 * math.pi * r0 ** 3)
    w_star = math.log2(rho_E / (2 * K["S0"]))
    frac = min(max(w_star, 0.0), K["W"]) / K["W"]
    au = rho_au * C ** 2 / (2 * K["S0"])
    if MUT.get("throat_volume"):
        rho_E = E / (4 * math.pi * r0 ** 2)
    return dict(E=E, r0=r0, rho_E=rho_E, w_star=w_star, frac=frac, au=au)


# ================================================================================ R6 the cypher
def r6(cy, ia, ms):
    cells = {}
    for qi, (tname, mins) in enumerate(sorted(ms.items())):
        for S in mins:
            cl = [CLASS[n] for n in S]
            cell = (qi, int("bulk" in cl), int("tension" in S), int("offset" in S), int("matter" in cl), int("laden" in cl))
            cells.setdefault(cell, []).append(S)
    coords = ["quantity", "has_bulk", "has_tension", "has_offset", "has_matter", "has_laden"]
    held = sorted(cells)
    ix = cy.Index("relgrav", coords, [list(c) for c in held])
    qG, qE = sorted(ms).index("G"), sorted(ms).index("G_eff")
    t_G = [c for c in held if c[0] == qG and c[1] == 1 and c[4] == 1 and c[5] == 0]
    t_E = [c for c in held if c[0] == qE and c[5] == 0]
    return dict(cells=cells, t_G=t_G, t_E_all_matter=all(c[4] == 1 for c in t_E) and bool(t_E),
                run=cy.run(ix, "1173", dict(OPTS)), audit=ia.audit_index(coords, held))


# ================================================================================ compute, report
def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "rg_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "rg_ia")
    a1 = r1()
    a2 = r2()
    return dict(r1=a1, r2=a2, r4=r4(a2["rho_au"]), r6=r6(cy, ia, a1["ms"]))


def report(o):
    a = o["r1"]
    print("relgrav.py -- do the matter laws and the offset govern G by providing the mass for relative gravity? (item 236)\n")
    print("R1 minimal sets fixing G: %s" % a["ms"]["G"])
    print("   of the bulk's, the plane's and matter's own parameters: %s" % a["G_prim"])
    print("   d ln G / d ln delta_sigma at fixed curvature and tension: %.3e (exact 2r/(1-2r)); G the same in 1 and 2a: %s"
          % (float(a["sens"]), a["same_G"]))
    print("   minimal sets fixing G (1 + rho/2 sigma), primitive: %s" % a["Geff_prim"])
    b = o["r2"]
    print("\nR2 a 1e22 kg body at our G, law against ours (surface g, mean density, radius; G-equivalent; atom's mass shift):")
    for (el, law), r in b["rows"].items():
        print("  %-2s %-6s g x %.5f  rho x %.5f  R x %.5f  -> G x %.5f   dm/m %.2e" % (el, law, r["g"], r["rho"], r["R"],
                                                                                   r["G_eq"], r["dm"]))
    c = o["r4"]
    print("\nR4 the README at the throat: E %.4e J, r0 %.4e m, rho_E %.3e J/m^3; above 2 sigma for w < %.3f of W = %.3f "
          "(%.1f %%); gold rho c^2 / 2 sigma <= %.2e" % (c["E"], c["r0"], c["rho_E"], c["w_star"], K["W"], 100 * c["frac"],
                                                         c["au"]))
    d = o["r6"]
    print("\nR6 the cypher: cells %s" % {str(k): v for k, v in d["cells"].items()})
    print("   'matter fixes G with the bulk and plane' held by %s; every primitive set for G_eff has matter: %s" % (
        d["t_G"], d["t_E_all_matter"]))
    print("   roster 1173: %s; audit %s" % ("; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"])
                                                    for v in d["run"]["verdicts"]), d["audit"]))


# ================================================================================ checks
def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("R0 M's item-236 words verbatim in the rulings file", M236 in rul)
    a = o["r1"]
    pats = sorted(tuple(sorted(S)) for S in a["G_prim"])
    ok = pats == [("coupling", "curvature", "offset"), ("coupling", "tension"), ("curvature", "offset", "tension")]
    ok &= not any(CLASS[n] == "matter" for S in a["G_prim"] for n in S) and a["same_G"]
    ok &= "%.2e" % float(a["sens"]) == "7.08e-63"
    ok &= all("offset" not in S for S in a["G_prim"] if "coupling" in S and "tension" in S)
    add("R1 no minimal set of bulk, plane and matter parameters fixing G contains matter; G the same in 1 and 2a; the "
        "offset only with the curvature, d ln G / d ln delta_sigma = 7.08e-63 in ours, 0 through the coupling", ok)
    b = o["r2"]["rows"]
    ok = ["%.3f" % b[(el, l)]["g"] for el in ("Cu", "Ag", "Au") for l in ("min", "mirror")] == [
        "1.042", "1.084", "1.143", "1.246", "1.008", "1.022"]
    ok &= ["%.3f" % b[(el, l)]["G_eq"] for el in ("Cu", "Ag", "Au") for l in ("min", "mirror")] == [
        "1.042", "1.083", "1.141", "1.242", "1.008", "1.021"]
    ok &= max(r["dm"] for r in b.values()) < 4e-11 and "%.3f" % b[("Ag", "mirror")]["rho"] == "1.390"
    add("R2 relative gravity: the law raises a 1e22 kg body's g by x 1.042-1.246 at our G (as G x 1.008-1.242 would), "
        "through density (up to x 1.390), while an atom's mass moves < 4e-11", ok)
    ms = a["ms"]["G"]
    ok = ("g_body", "rho_m") in [tuple(sorted(S)) for S in ms]
    add("R3 {surface gravity, matter's density} fixes G -- the Cavendish route; the surface gravity is made from G", ok)
    c = o["r4"]
    ep = sorted(tuple(sorted(S)) for S in a["Geff_prim"])
    ok = bool(ep) and all("rho_m" in S for S in ep) and ("coupling", "rho_m", "tension") in ep
    ok &= "%.1e" % c["rho_E"] == "9.1e+97" and "%.1f" % (100 * c["frac"]) == "75.1" and c["au"] < 6e-33
    add("R4 the effective coupling G (1 + rho/2 sigma): every primitive minimal set contains matter's density; gold's "
        "term <= 5.3e-33; the README at the throat 9.1e97 J/m^3, above 2 sigma over 75.1 % of our tension's window", ok)
    d = o["r6"]
    ok = d["t_G"] == [] and d["t_E_all_matter"] and bool(d["run"]["verdicts"]) and not d["audit"]["keys"]
    add("R6 the cypher (run and audited, no key): 'matter fixes G with the bulk and the plane' held by none; every set "
        "fixing the effective coupling without a quantity made from G contains matter", ok)
    return res


MUTANTS = {"matter_in_G": "matter's density read as carrying G (G proportional to it)",
           "throat_volume": "the README's energy spread over the throat's area, not its volume"}


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
        print("  mutant %-14s %-62s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
