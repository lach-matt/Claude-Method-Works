#!/usr/bin/env python3
"""copy_p2.py -- item 240: the copy built at position 2 under position 2's laws; the corridor's side there; the
variances each destination presents, which the object's survival asks it to mitigate.  M: "the object is built from the
bulk at position 2 as an exact copy under the laws and conditions of position 2. The mass on position 2's side is not
equal to ours. Position 2 accounts for the difference as it assembles the mass to match a README from position 1 under
position 2's laws. Survivability of the object when contained in position 2 depends on how well it is equipped to
mitigate that variances of position 2".  Worked in the conversation (computed, exact where marked; deduced where
marked; not verified by a separate session; not seated); 2026-10-11.

  C0 (read) M's item-240 words, verbatim in the rulings file.
  C1 (computed, exact) The corridor on position 2's side, matched to the README (240 (b)): its throat holds exactly the
     README's N bits at position 2's own bit area (clause (H) there), so its size m2 / m = r0,2 / r0 = (G2 / G)^1/2 and
     its mass-energy E2 / E = (G / G2)^1/2.  2b, 2c, 2P: size x 2^1/2, mass-energy x 2^-1/2; 2b + 2P and 2c + 2P: x 2,
     x 1/2; 2a: both ours.  The record's trip (p2_gravity.trip, theorem_p2 TC) held one E between the universes (203):
     m2 / m = G2 / G and a capacity (G2 / G) N -- the reading 240 (a) withdraws; matched to the README the capacity at
     position 2 is N exactly.
  C2 (computed) The copy's own mass under position 2's laws.  Rest masses are the shared SI's; the matter law moves an
     atom's mass only through binding, by at most 3.7e-11 (Ag, mirror; p2_matter); G moves none.  So what position 2
     "accounts for as it assembles" is chiefly the closing energy's difference -- E2 - E = -29.3 % at 2b, 2c and 2P, -50
     % at 2b + 2P, 0 at 2a -- and the binding's 1e-11.
  C3 (computed) The variances each destination presents (against ours), what the object must be equipped to mitigate:
     gravity G2 / G (x 1, 2, 4); the dark energy Lambda4 (x 2^(g+s): 2b x 2, 2P x 1/2, 2b + 2P x 1); a reference
     body's surface gravity (a 1e22 kg sphere of Cu, Ag or Au, p2_gravity's integrator: x 2.03 at 2b and 2P, up to
     x 5.07 at 2c + 2P under mirror); the closing energy delivered (x 0.7071, x 0.5); and, under the matter laws, the
     chemistry -- bond energies of seven molecules change by -3 % to +35 % (min) and -121 % to +0.4 % (mirror), Cu2
     unbound under mirror and Ag2 and CuF unresolved; solid densities -4 % to +23 % (min), -6 % to +41 % (mirror);
     cohesive energies +1 % to +36 % (min), -29 % to +15 % (mirror).
  C4 (deduced) Survivability (240) is a condition on the object: it survives at a destination when every variance there
     lies within its means of mitigation.  Those means are the object's, not computed; the destinations an object can
     survive are then a box in the variance axes it sets.  If its means hold a limit on gravity, that limit bounds
     weak (and strong) gravity for that object -- the board's candidate for item 237's missing bound: object-relative,
     not a property of the bulk.
  C5 (computed; the cypher, roster 1173, audited) The twelve destinations as cells over the three variance axes they
     move (the matter law, log2 G, log2 Lambda4).  No coordinate adds nothing and none is a key: the variances are three
     independent axes, each to be met by its own means.  The languages' admissions beyond the twelve are reported.
  C6 (record) What item 240 overrules or withdraws: ledger_cypher L7-L8's consequences (destinations at our G only;
     m2 = m) and the selection of ONE, which rested on reading the one value as equal energies in SI (item 238 (b)).
     With 239's need and 240's reading the build reads under position 2's laws (P2): no sink (239), the README the one
     value, position 2's own G (226) and mass (240) -- every ruling kept but 237, whose bound the ledger no longer
     supplies.

What this does not show.
  - C1 holds the README fixed as M's words put it; whether the corridor's own energy equals the README's E at
    position 2 (203, item 232 (7)) is still to be computed.
  - C3's reference bodies are cold spheres of one metal; the object's own structure is not computed.
  - The mirror law's bond energies carry item 221's caveats (biased low; Ag2 unresolved; branches followed).

Imports bulk5_index.py (and through it p2_planck.py, p2_gravity.py), p2_matter.py, tools/cypher.py and index_audit.py by
path.  Stdlib.  python3 copy_p2.py [--selftest | --mutants]
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
M240 = ("the object is built from the bulk at position 2 as an exact copy under the laws and conditions of position 2. The "
        "mass on position 2's side is not equal to ours.")
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


B5 = _load(os.path.join(HERE, "bulk5_index.py"), "cp_b5")
PP = B5.PP
PG = B5.PG


# ================================================================================ C1 the corridor on position 2's side
def c1():
    fd = B5.five_d()
    out = {}
    for n, v in fd.items():
        g = v["e"]["G"]
        m_exp = g / 2 if not MUT.get("one_E") else g             # README-matched: size ~ G^1/2; one E: ~ G
        e_exp = -g / 2 if not MUT.get("one_E") else F(0)
        tr = PG.trip(PG.G, PG.G * v["gf"])
        out[n] = dict(g=g, m_exp=m_exp, e_exp=e_exp, cap_readme=1, cap_oneE=tr["capacity_ratio"], m_oneE=tr["m_ratio"])
    return out


def c1_check_numeric():
    """the README-matched size from clause (H) at position 2's G, against the exponent"""
    N = 2742570311524972
    r = lambda Gx: math.sqrt(N * 2 * PG.H * Gx * math.log(2) / (math.pi * PG.C ** 3) / (4 * math.pi))
    E = lambda Gx: r(Gx) / 2 * PG.C ** 4 / Gx
    return dict(r_ratio=r(2 * PG.G) / r(PG.G), E_ratio=E(2 * PG.G) / E(PG.G))


# ================================================================================ C2, C3 the copy and the variances
def c23():
    pm = _load(os.path.join(HERE, "p2_matter.py"), "cp_pm")
    o = pm.compute()
    mass = max(abs(v) for m in o["mass"].values() for v in m.values())
    chem = {}
    for law in ("min", "mirror"):
        ch = []
        unbound, unresolved = [], []
        for (mol, lw), v in o["mol"].items():
            if lw != law:
                continue
            ours = o["mol"][(mol, "ours")]["De"]
            ch.append(v["De"] / ours - 1)
            if v["De"] <= 0:
                unbound.append(mol)
            if v.get("unresolved") or abs(v["De"]) < 0.01:
                unresolved.append(mol)
        sol = [o["sol"][(el, law)]["rho"] / o["sol"][(el, "ours")]["rho"] - 1 for el in ("Cu", "Ag", "Au", "Cr")]
        coh = [o["sol"][(el, law)]["Ecoh"] / o["sol"][(el, "ours")]["Ecoh"] - 1 for el in ("Cu", "Ag", "Au", "Cr")]
        chem[law] = dict(bond=(min(ch), max(ch)), unbound=sorted(unbound), unresolved=sorted(set(unresolved) - set(unbound)),
                         rho=(min(sol), max(sol)), coh=(min(coh), max(coh)))
    # reference bodies: 1e22 kg spheres, every (law, G factor) a destination carries
    bodies = {}
    for el in ("Cu", "Ag", "Au"):
        s0 = o["sol"][(el, "ours")]
        g0 = PG.body(1e22, s0["rho"], s0["B0"] * 1e9, s0["Bp"], PG.G)["g"]
        for law in ("ours", "min", "mirror"):
            s = o["sol"][(el, law)]
            for gf in (1, 2, 4):
                bodies[(el, law, gf)] = PG.body(1e22, s["rho"], s["B0"] * 1e9, s["Bp"], PG.G * gf)["g"] / g0
    return dict(mass=mass, chem=chem, bodies=bodies)


def variances(c, fd):
    out = {}
    for n, v in fd.items():
        law, gf = v["law"], v["gf"]
        out[n] = dict(G=gf, Lambda=2.0 ** float(v["e"]["G"] + v["e"]["sigma"]), E=2.0 ** float(-v["e"]["G"] / 2),
                      body=max(c["bodies"][(el, law, gf)] for el in ("Cu", "Ag", "Au")), law=law)
    return out


# ================================================================================ C5 the cypher
def c5(cy, ia, fd):
    laws = B5.LAW_ORDER
    cells = sorted({(laws.index(v["law"]), int(v["e"]["G"]), int(v["e"]["G"] + v["e"]["sigma"])) for v in fd.values()})
    if MUT.get("drop_lambda"):
        cells = sorted({c[:2] + (0,) for c in cells})
    coords = ["matter_law", "log2_G", "log2_Lambda4"]
    ix = cy.Index("copy_variances", coords, [list(c) for c in cells],
                  value_order={"matter_law": [0, 1, 2], "log2_G": [0, 1, 2], "log2_Lambda4": sorted({c[2] for c in cells},
                                                                                                     key=lambda x: (abs(x), x))})
    rows, keys = cy.coordinate_report(ix)
    run = cy.run(ix, "1173", dict(OPTS))
    return dict(cells=cells, adds_nothing=[r["coordinate"] for r in rows if r["adds_nothing"]], keys=keys, run=run,
                audit=ia.audit_index(coords, cells))


# ================================================================================ compute, report
def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "cp_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "cp_ia")
    fd = B5.five_d()
    c = c23()
    return dict(c1=c1(), c1n=c1_check_numeric(), c23=c, var=variances(c, fd), c5=c5(cy, ia, fd))


def report(o):
    print("copy_p2.py -- the copy at position 2 under its own laws; the variances it must mitigate (item 240)\n")
    print("C1 the corridor on position 2's side (exponents of 2): README-matched size, mass-energy; the record's one-E trip")
    for n, r in o["c1"].items():
        print("  %-13s size 2^%-5s mass-energy 2^%-5s capacity N | one E: size x %g, capacity x %g" % (
            n, r["m_exp"], r["e_exp"], r["m_oneE"], r["cap_oneE"]))
    print("   numeric at G x 2 from clause (H): size x %.6f, mass-energy x %.6f" % (o["c1n"]["r_ratio"], o["c1n"]["E_ratio"]))
    c = o["c23"]
    print("\nC2 the copy's own mass under position 2's laws: at most %.2e from the matter law; none from G" % c["mass"])
    print("\nC3 chemistry under the laws: %s" % {l: dict(bond="%+.0f%%..%+.1f%%" % (100 * v["bond"][0], 100 * v["bond"][1]),
                                                       unbound=v["unbound"], unresolved=v["unresolved"],
                                                       rho="%+.0f%%..%+.0f%%" % (100 * v["rho"][0], 100 * v["rho"][1]),
                                                       coh="%+.0f%%..%+.0f%%" % (100 * v["coh"][0], 100 * v["coh"][1]))
                                              for l, v in c["chem"].items()})
    print("   the variances per destination:")
    for n, v in o["var"].items():
        print("  %-13s G x %g  Lambda4 x %g  closing energy x %.4f  a reference body's surface gravity up to x %.3f  "
              "matter law %s" % (n, v["G"], v["Lambda"], v["E"], v["body"], v["law"]))
    d = o["c5"]
    print("\nC5 the cypher: cells %s; adds nothing %s; keys %s; audit %s" % (d["cells"], d["adds_nothing"], d["keys"], d["audit"]))
    print("   roster 1173: %s" % "; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"]) for v in d["run"]["verdicts"]))


# ================================================================================ checks
def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("C0 M's item-240 words verbatim in the rulings file", M240 in rul)
    c = o["c1"]
    ok = (c["2b"]["m_exp"], c["2b"]["e_exp"], c["2P"]["m_exp"], c["2b+2P"]["m_exp"], c["2b+2P"]["e_exp"]) == (
        F(1, 2), F(-1, 2), F(1, 2), F(1), F(-1))
    ok &= c["2a-min"]["m_exp"] == 0 and c["2b"]["m_oneE"] == 2 and c["2b"]["cap_oneE"] == 2
    ok &= abs(o["c1n"]["r_ratio"] - math.sqrt(2)) < 1e-12 and abs(o["c1n"]["E_ratio"] - 1 / math.sqrt(2)) < 1e-12
    add("C1 README-matched: size x 2^1/2, mass-energy x 2^-1/2 at 2b, 2c, 2P (x 2, x 1/2 at 2b+2P; 2a ours); clause (H) "
        "at G x 2 agrees to 1e-12; the record's one-E trip gave size x 2, capacity 2N", ok)
    c2 = o["c23"]
    var = o["var"]
    ok = c2["mass"] < 4e-11 and abs(var["2b"]["E"] - 2 ** -0.5) < 1e-12 and abs(var["2b+2P"]["E"] - 0.5) < 1e-12
    ok &= var["2a-mirror"]["E"] == 1.0
    add("C2 the copy's own mass moves < 4e-11 (matter law), not with G; the closing energy at position 2: x 0.7071 at "
        "2b/2c/2P, x 0.5 at 2b+2P, x 1 at 2a", ok)
    ch = c2["chem"]
    ok = ch["mirror"]["unbound"] == ["CuCu"] and ch["mirror"]["unresolved"] == ["AgAg", "CuF"]
    ok &= "%+.0f" % (100 * ch["min"]["bond"][0]) == "-3" and "%+.0f" % (100 * ch["min"]["bond"][1]) == "+35"
    ok &= "%+.0f" % (100 * ch["mirror"]["bond"][0]) == "-121"
    ok &= (var["2b"]["G"], var["2b"]["Lambda"], var["2P"]["Lambda"], var["2b+2P"]["Lambda"]) == (2, 2.0, 0.5, 1.0)
    ok &= "%.2f" % var["2c+2P-mirror"]["body"] == "5.07" and "%.2f" % var["2b"]["body"] == "2.03"
    add("C3 the variances: G x 1/2/4, Lambda4 x 2 (2b), x 1/2 (2P), x 1 (2b+2P); bonds -3..+35 % (min), down to -121 % "
        "(mirror; Cu2 unbound, Ag2 and CuF unresolved); a reference body's gravity x 2.03 (2b) up to x 5.07 (2c+2P, mirror)", ok)
    d = o["c5"]
    ok = d["adds_nothing"] == [] and d["keys"] == [] and len(d["cells"]) == 12 and bool(d["run"]["verdicts"])
    ok &= not d["audit"]["onehot"]
    add("C5 the cypher (run and audited): the twelve destinations over (law, log2 G, log2 Lambda4) -- no coordinate adds "
        "nothing, no key, no one-hot: three independent variance axes", ok)
    return res


MUTANTS = {"one_E": "the corridor's side read with one E held (the withdrawn reading)",
           "drop_lambda": "the dark-energy variance dropped from the destinations"}


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
        print("  mutant %-12s %-60s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
