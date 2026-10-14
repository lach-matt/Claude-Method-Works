#!/usr/bin/env python3
"""far_bridge.py -- FAR's computed candidate, the two-sided bridge with a negative position-2 plane (model C), against
(Z) net per ray (183).  Item 211: the hold analyst's pass, its critic's verdict (FB1 and BRIDGE-NEG's (Z) earned on
their assumptions, re-derived by hand in closed form; 'every computed candidate refuted' and 'positive in total'
over-reached); re-built here in closed form, stdlib + sympy; seated under 206; 2026-10-10.

  F1 (computed, sympy) a null ray crossing a thin plane of surface stress S gains S(k_par, k_par)/|n.k| = |n.k| S(u, u),
     u the plane's tangential observer along k_par (TS's crossing share, P2-FULL).  A pure tension gives sigma |n.k|.
     So where nothing else lies on the ray, net >= 0 holds iff the surface WEC holds: rho >= 0 and rho + p >= 0
  F2 (computed, imported modelc.py) the plane's total stress (tension and any matter, 184) in model C's arrangement --
     a static symmetric plane at r = R, the Schwarzschild-AdS5 bridge (mu > 0) kept inside, position 2's own pure AdS
     outside -- is modelc's own junction: rho = (3/R)(sqrt f_s + eps sqrt f_o), rho + p = B(R)/R, eps = -1 on the
     GROWING outer side, +1 on the decaying one
  F3 (deduced, closed form; the critic's derivation) on the growing outer side the surface WEC fails for every matter
     content.  k = 1: rho >= 0 is s >= o and rho + p >= 0 is o (1 - 2 mu/R^2) >= s (s = sqrt f_s, o = sqrt f_o), which
     together force mu <= 0.  k = 0: rho + p = -2 mu/(R^3 s) < 0, on EITHER outer side.  Control: k = 1 on the decaying
     side meets both.  Second engine: a random scan finds no growing-side point meeting both
  F4 (computed, imported modelc.py; far_cypher F7's member) BRIDGE-NEG: k = 1, ell_s = 1, mu = 4/3, our tension lam = 2;
     position 2's plane at R2 = 2.874732, outside r_h = 0.870808 and outside the photon sphere sqrt(2 mu) = 1.632993,
     tension -lam/4 = -1/2; rho = -3/2 and rho + p = 0: the matter-free member, negative
  F5 (deduced; Kruskal monotonicity, standard-not-READ) no causal curve joins exterior III, where position 2's plane
     sits, to exterior I.  So every null geodesic that meets that plane meets no other member, and its net is
     sigma_2 sum |n.k_i| < 0: BRIDGE-NEG's (Z) is 0, not U
So model C's growing-side family -- the only arrangement giving position 2's plane negative net energy (modelc C4, C5)
-- cannot keep (Z) for any matter content, and its matter-free member breaks it on every ray meeting the plane.  FAR
stays OPEN: SLAB fails (G) only on the board's reading H-STAGE7-IS-THE-BOARD'S (far_cypher X9's reading leaves it U),
and FAR needs either every ray crossing position 2's plane paired on that ray -- 177's coupling of the ends is the
obvious candidate outside model C's vacuum family -- or that plane meeting the surface WEC in total, which for k = 0 no
outer side gives.
What this does not show: planes static (141) and sharing the bridge's symmetry (H-SYMMETRIC-PLANES); thin
(H-THIN-PLANE); outer bulks pure AdS (mu_2 = 0, as modelc models them); k in {0, 1}; the maximally extended Kruskal
structure (standard-not-READ, BULK-BALANCE section 7).
Imports kequality_scratch/two-sided/modelc.py by path.  Stdlib + sympy.  python3 far_bridge.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
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


def mc():
    if "mc" not in _C:
        _C["mc"] = _load(os.path.join(HERE, "kequality_scratch", "two-sided", "modelc.py"), "fb_modelc")
    return _C["mc"]


# ================================================================================================================ F1
def f1():
    import sympy as sp
    kap, v, sig, rho, p1, p2, p3 = sp.symbols("kappa v sigma rho p1 p2 p3", real=True)
    eta = sp.diag(-1, 1, 1, 1, 1)
    n = sp.Matrix([0, 0, 0, 0, 1])
    g = lambda a, b: (a.T * eta * b)[0]
    h = eta - eta * n * n.T * eta
    gam = 1 / sp.sqrt(1 - v ** 2)
    u = sp.Matrix([gam, gam * v, 0, 0, 0])
    kpar = sp.Abs(kap) * u
    k = kpar + kap * n
    tension = sp.simplify((kpar.T * (-sig * h) * kpar)[0] / sp.Abs(kap))
    S = sp.diag(rho, p1, p2, p3, 0)
    general = sp.simplify((kpar.T * S * kpar)[0] / sp.Abs(kap))
    return {"null": sp.simplify(g(k, k)) == 0, "tension": sp.simplify(tension - sig * sp.Abs(kap)) == 0,
            "general": sp.simplify(general - sp.Abs(kap) * gam ** 2 * (rho + v ** 2 * p1)) == 0}


# ============================================================================================================ F2, F3
def f23():
    import sympy as sp
    m = mc()
    R = sp.Symbol("R", positive=True)
    mu, ls, l2 = sp.symbols("mu ell_s ell_2", positive=True)
    out = {}
    for k in (1, 0):
        for eps in (-1, 1):
            fs = k + R ** 2 / ls ** 2 - mu / R ** 2
            fo = k + R ** 2 / l2 ** 2
            sides = [(1, fs, sp.diff(fs, R)), (eps, fo, sp.diff(fo, R))]
            J = m.junction_conditions(sides)
            rho = J["rho"].subs(J["R"], R)
            p = J["p"].subs(J["R"], R)
            B = m.balance_function(sides, R, k)
            out[(k, eps)] = {"rho_form": sp.simplify(rho - 3 * (sp.sqrt(fs) + eps * sp.sqrt(fo)) / R) == 0,
                             "nec_form": sp.simplify(rho + p - B / R) == 0, "B": sp.simplify(B), "fs": fs, "fo": fo}
    # F3 in closed form, k = 1, growing side: with s, o > 0, rho >= 0 <=> s >= o; B R^2 s o = (R^2 - 2 mu) o - R^2 s
    s, o = sp.symbols("s o", positive=True)
    B1 = (1 - 2 * mu / R ** 2) / s - 1 / o
    k1 = sp.simplify(sp.expand(B1 * R ** 2 * s * o - ((R ** 2 - 2 * mu) * o - R ** 2 * s))) == 0
    # with s >= o and (1 - 2mu/R^2) o >= s: (1 - 2mu/R^2) o >= o, so -2 mu o / R^2 >= 0, so mu <= 0
    k1_forces = sp.simplify(((1 - 2 * mu / R ** 2) * o - o) + 2 * mu * o / R ** 2) == 0
    # k = 0: B = -2 mu/(R^2 s) on either side
    k0 = all(sp.simplify(out[(0, e)]["B"] + 2 * mu / (R ** 2 * sp.sqrt(out[(0, e)]["fs"]))) == 0 for e in (-1, 1))
    return {"forms": out, "k1_identity": k1, "k1_forces": k1_forces, "k0": k0}


def scan(n=20000, seed=211):
    """second engine: random (k, mu, ell_s, ell_2, R) with f_s > 0; growing side never meets rho >= 0 and B >= 0"""
    rnd = random.Random(seed)
    bad = adm = 0
    ctrl = None
    eps = 1 if MUT.get("decaying_as_growing") else -1
    for _ in range(n):
        k = rnd.choice((0, 1))
        mu = 10 ** rnd.uniform(-3, 3)
        a = 10 ** rnd.uniform(-2, 2)
        b = 10 ** rnd.uniform(-2, 2)
        R = 10 ** rnd.uniform(-2, 3)
        fs, fo = k + R * R / (a * a) - mu / (R * R), k + R * R / (b * b)
        if fs <= 0:
            continue
        adm += 1
        rho = 3 * (math.sqrt(fs) + eps * math.sqrt(fo)) / R
        B = (k - 2 * mu / R ** 2) / math.sqrt(fs) + eps * k / math.sqrt(fo)
        if rho >= 0 and B >= 0:
            bad += 1
        if ctrl is None and k == 1:
            rc = 3 * (math.sqrt(fs) + math.sqrt(fo)) / R
            Bc = (1 - 2 * mu / R ** 2) / math.sqrt(fs) + 1 / math.sqrt(fo)
            if rc >= 0 and Bc >= 0:
                ctrl = (mu, a, b, R)
    return {"bad": bad, "adm": adm, "ctrl": ctrl}


# ============================================================================================================ F4, F5
def f45():
    import sympy as sp
    m = mc()
    o = m.rs_at_ell_s(sp.Integer(2))
    target = -o["lam"] / 4 if not MUT.get("bridge_plus") else o["lam"] / 4
    sol = m.p2_given(o["mu"], target)[0]
    mu = sp.nsimplify(o["mu"])
    r = sp.Symbol("r", positive=True)
    rh = sp.sqrt((-1 + sp.sqrt(1 + 4 * mu)) / 2)
    u2, L2 = sol["u2"], sol["L2"]
    fs = 1 + u2 - mu / u2
    fo = 1 + u2 / L2 ** 2
    R2 = sp.sqrt(u2)
    rho = 3 * (sp.sqrt(fs) - sp.sqrt(fo)) / R2
    nec = ((1 - 2 * mu / u2) / sp.sqrt(fs) - 1 / sp.sqrt(fo)) / R2
    return {"mu": mu, "lam": sp.nsimplify(o["lam"]), "target": target, "R2": float(sol["R2"]), "rh": float(rh),
            "photon": float(sp.sqrt(2 * mu)), "bal": abs(float(sol["bal"])), "ten": abs(float(sol["ten"])),
            "rho": float(rho), "nec": float(nec), "fprime_rh": float(sp.diff(1 + r ** 2 - mu / r ** 2, r).subs(r, rh))}


def kruskal():
    """a future causal vector of -F dU dV + r^2 dSigma^2 (F > 0) has U', V' >= 0: from III (U > 0 > V) no causal curve
    reaches I (U < 0 < V).  Exhaustive sign check over a grid of components."""
    grid = [x / 2 for x in range(-6, 7)]
    return all(not (a + b > 0 and a * b >= 0) or (a >= 0 and b >= 0) for a in grid for b in grid)


def compute():
    return {"f1": f1(), "f23": f23(), "scan": scan(), "f45": f45(), "kruskal": kruskal()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    a = d["f1"]
    add("F1 crossing a thin plane: S(k_par, k_par)/|n.k| = |n.k| S(u, u); a pure tension gives sigma |n.k|: net >= 0 on "
        "rays meeting nothing else iff rho >= 0 and rho + p >= 0", a["null"] and a["tension"] and a["general"])
    b = d["f23"]
    add("F2 modelc's junction for model C's plane: rho = (3/R)(sqrt f_s + eps sqrt f_o), rho + p = B/R, k = 0 and 1, both "
        "outer sides", all(v["rho_form"] and v["nec_form"] for v in b["forms"].values()))
    s = d["scan"]
    add("F3 growing outer side: k = 1, rho >= 0 and rho + p >= 0 force mu <= 0; k = 0, rho + p = -2 mu/(R^3 s) < 0 on "
        "either side; a random scan of %d admissible points finds none meeting both; control: the decaying side does" % s["adm"],
        b["k1_identity"] and b["k1_forces"] and b["k0"] and s["bad"] == 0 and s["adm"] > 5000 and s["ctrl"] is not None)
    f = d["f45"]
    ok4 = (abs(float(f["mu"]) - 4 / 3) < 1e-12 and f["lam"] == 2 and abs(float(f["target"]) + 0.5) < 1e-15 and f["bal"] < 1e-30
           and f["ten"] < 1e-30 and abs(f["R2"] - 2.874732) < 1e-6 and abs(f["rh"] - 0.870808) < 1e-6
           and abs(f["photon"] - 1.632993) < 1e-6 and f["fprime_rh"] > 0 and abs(f["rho"] + 1.5) < 1e-9 and abs(f["nec"]) < 1e-20)
    add("F4 BRIDGE-NEG: mu = 4/3, lam = 2, position 2's tension -1/2 met; R2 = 2.874732 > r_h = 0.870808 and > the photon "
        "sphere 1.632993; rho = -3/2, rho + p = 0 (matter-free, negative)", ok4)
    add("F5 no causal curve joins exterior III to I (Kruskal); every ray meeting position 2's plane meets no other "
        "member, net sigma_2 sum |n.k| < 0: BRIDGE-NEG's (Z) is 0", d["kruskal"] and f["target"] < 0 and f["rho"] < 0)
    return res


MUTANTS = {"decaying_as_growing": "the scan run on the decaying side as if it were the growing one",
           "bridge_plus": "position 2's plane entered with positive tension"}


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
        print("  mutant %-20s %-62s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("far_bridge.py -- model C's bridge with a negative position-2 plane, against (Z) (item 211)\n")
    print("F1", d["f1"])
    print("F2/F3 closed forms:", {k: (v["rho_form"], v["nec_form"]) for k, v in d["f23"]["forms"].items()},
          "k=1 identity", d["f23"]["k1_identity"], "k=0", d["f23"]["k0"])
    print("    scan:", d["scan"])
    print("F4", {k: v for k, v in d["f45"].items()})
    print("F5 Kruskal monotonicity:", d["kruskal"])


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
