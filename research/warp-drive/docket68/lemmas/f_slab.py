#!/usr/bin/env python3
"""f_slab.py -- item 274: e_positive.py E6's counter-case, the caveat M named ("The one counter-case.  - this is a
caveat, C8 is not ready for verification").  Is the counter-case one arrangement or every arrangement in which position
2's plane faces ours across bulk, and what escapes it?  Worked in the conversation (computed with sympy, exact where
marked; deduced where marked; the cypher run and audited; not verified by a separate session; not seated); 2026-10-12.

  F0 (read) M's item-274 words, verbatim in the rulings file.
  F1 (computed, exact) Null energy across a static slab.  For ds^2 = e^(2A(y)) g4 + dy^2 with g4 maximally symmetric
     (flat, de Sitter H^2 > 0, anti-de Sitter -1/L^2) and a null k with k^y != 0, the 5D Ricci tensor gives
     R_kk = -3 (k^y)^2 (A'' + H^2 e^(-2A)) -- computed from the metric for the de Sitter and anti-de Sitter slicings.
  F2 (computed, exact) The warp is monotone across the slab.  In vacuum -- the theorem's clause (B), "A vacuum
     five-dimensional bulk carries the corridor" -- R_kk = 0 and A'' = -H^2 e^(-2A) exactly (the flat warp -y/ell and
     the de Sitter warp ln(H ell sinh((y0 - y)/ell)) both computed to satisfy it), with no appeal to null energy.  With
     matter in the slab, pointwise null energy (117/120) gives A'' <= -H^2 e^(-2A).  Along a ray crossing the slab k^y = p e^(-A) (the conformal frame), so 183's net per ray
     over the slab's segment is int (A'' + H^2 e^(-2A)) e^(-A) dy <= 0, and with d/dy (A' e^(-A)) = (A'' - A'^2) e^(-A) (exact) it reads
     [A' e^(-A)] from y1 to y2 <= -int (A'^2 + H^2 e^(-2A)) e^(-A) dy, at most 0 for flat or de Sitter slicing.  So if
     the warp falls from our plane into the slab (A'(y1+) < 0) it is still falling at position 2's plane (A'(y2-) < 0):
     position 2's plane grows into the slab.  Control (computed, exact): anti-de Sitter slicing escapes -- vacuum AdS5
     as e^(2A) = cosh^2(y/L) saturates the null energy and has a warp minimum, both planes decaying into the slab
     (Karch-Randall's two positive planes); the slicing is common to the slab, so both planes would be AdS4.
  F3 (computed; e_positive E3) Two planes facing across a static flat or de Sitter slab cannot both be positive and
     expanding.  Ours is (our matter's energy positive and our expansion raised by it, standard): by E3 our plane decays
     on both sides, into the slab too; by F2 position 2's plane then grows into the slab -- its sides opposite or both
     growing -- and by E3 its total positive and its expansion on absorbing the README never hold together.  So E6's
     counter-case is not one arrangement: it is every static slab between the planes, M4's at r > 0 among them.
  F4 (computed, exact) What escapes.  (i) A horizon between: in planar Schwarzschild-AdS5 (f = k^2 r^2 - C/r^2, C > 0,
     horizon r+ = (C/k^2)^(1/4)) a plane in each exterior keeping r < R faces the throat and decays toward it (E2's
     e = +1), so with its far side like it is positive and expands (E3); no causal curve runs between the exteriors
     (Kruskal: U < 0 < V in one, V < 0 < U in the other, U and V non-decreasing along every future causal curve).
     (ii) Position 2's plane in its own bulk, reached from ours only through the corridor: like sides, as e_positive E6.
     (iii) The coincidence of 127: the junction sees only the summed stress (b5_positive B5a), so position 2's own total
     is not fixed by any junction -- neither proved nor refuted there.
  F5 (computed; the cypher, roster 1173, audited) The index: how position 2's plane meets ours (a static slab, the
     coincidence, a horizon between, its own bulk) x its near side x its far side (decaying, growing) -- 14 rows (a plane
     facing a throat decays toward it), each with p2 (positive and expanding, E3), nec (null energy kept, F2) and fixed
     (its own total fixed by a junction).  The all-three cell is reached only beyond a horizon or in position 2's own
     bulk, decaying on both sides; a static slab reaches p2 only by breaking null energy, the coincidence never fixes it.
     The languages split: geometry, information and statistics admit exactly the five held cells (E = 0); order and
     algebra add one, the meet (0, 0, 0) of the null-breaking slab and the coincidence (E = 1) -- a coincidence breaking
     null energy, which b5_positive B5a excludes (deduced); K.langclose holds, 4 of 10 pairs agreeing.
  F6 (deduced) The caveat in one statement: under 139 (3) and the rulings' null energy (117/120, or 183), position 2's
     plane is positive exactly where it does not face ours across a static slab -- where ours and position 2's are
     joined only through something that is not a static slab, as the corridor is (179: "it only bridges them"; 136 (3);
     152; 270, 273: one-way, through the bounce).  A static slab is also a second, two-way connection between the
     universes: a ray with p > 0 crosses it in affine length int e^A dy / p, finite, and one with p < 0 returns (F2's
     frame).  Whether one separates the planes away from the corridor is not computed here and no ruling decides it.

What this does not show.
  - Which of F4's configurations holds away from the corridor: that is M's (149).
  - 183's pairing with a partner off the slab's segment (on a plane, or beyond it) for a slab carrying matter: F2 nets
    the ray over the segment; a vacuum slab needs no null-energy reading at all.
  - Time-dependent slabs other than F4's horizon (a slab whose warp is not static, without a horizon).
  - Our plane's slicing as data: flat or de Sitter is our expansion's, standard, not READ here.

Imports e_positive.py, index_audit.py and tools/cypher.py by path.  Stdlib + sympy.
python3 f_slab.py [--selftest | --mutants]
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
M274 = "this is a caveat, C8 is not ready for verification"
PROPS = ["p2", "nec", "fixed"]
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


def ricci(g, X):
    n = len(X)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    R = sp.zeros(n, n)
    for b in range(n):
        for c in range(b, n):
            v = sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c]) for a in range(n))
            v += sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for a in range(n) for d in range(n))
            R[b, c] = R[c, b] = sp.simplify(v)
    return R


def null_energy():
    """F1: R_kk for the de Sitter and anti-de Sitter slicings"""
    t, x1, x2, x3, y, H, L, ky = sp.symbols("t x1 x2 x3 y H L k_y", positive=True)
    A = sp.Function("A")(y)
    out = {}
    # de Sitter (flat at H = 0): -dt^2 + e^(2Ht) dx^2
    X = [t, x1, x2, x3, y]
    g = sp.diag(-sp.exp(2 * A), *[sp.exp(2 * A + 2 * H * t)] * 3, 1)
    R = ricci(g, X)
    kt = sp.exp(-A) * ky                                   # -e^(2A) kt^2 + ky^2 = 0
    Rkk = sp.simplify(R[0, 0] * kt ** 2 + 2 * R[0, 4] * kt * ky + R[4, 4] * ky ** 2)
    out["dS"] = sp.simplify(Rkk + 3 * ky ** 2 * (A.diff(y, 2) + H ** 2 * sp.exp(-2 * A))) == 0
    # anti-de Sitter: e^(2z/L) (-dt^2 + dx1^2 + dx2^2) + dz^2
    z = x3
    g = sp.diag(-sp.exp(2 * A + 2 * z / L), sp.exp(2 * A + 2 * z / L), sp.exp(2 * A + 2 * z / L), sp.exp(2 * A), 1)
    R = ricci(g, X)
    kt = sp.exp(-A - z / L) * ky
    Rkk = sp.simplify(R[0, 0] * kt ** 2 + 2 * R[0, 4] * kt * ky + R[4, 4] * ky ** 2)
    out["AdS"] = sp.simplify(Rkk + 3 * ky ** 2 * (A.diff(y, 2) - sp.exp(-2 * A) / L ** 2)) == 0
    return out


def monotone():
    """F2: the integration by parts, the sign of the bound, and the anti-de Sitter control"""
    y = sp.Symbol("y", real=True)
    A = sp.Function("A")(y)
    parts = sp.simplify(sp.diff(A.diff(y) * sp.exp(-A), y) - (A.diff(y, 2) - A.diff(y) ** 2) * sp.exp(-A)) == 0
    a1, Av, H = sp.symbols("a1 A_v H", real=True)
    s_ours = 1
    if MUT.get("ads_ours"):
        s_ours = -1                                        # the mutant slices our slab anti-de Sitter
    sign = {}
    for name, s in (("flat", 0), ("dS", s_ours), ("AdS", -1)):
        integrand = (a1 ** 2 + s * H ** 2 * sp.exp(-2 * Av)) * sp.exp(-Av)
        sign[name] = integrand.is_nonnegative
    yy, Lc = sp.symbols("y L", positive=True)
    ell, Hs, y0, d = sp.symbols("ell H y_0 d", positive=True)
    vac_flat = sp.diff(-yy / ell, yy, 2)
    AdS_ = sp.log(Hs * ell * sp.sinh((y0 - yy) / ell))
    vac_dS = sp.simplify((sp.diff(AdS_, yy, 2) + Hs ** 2 * sp.exp(-2 * AdS_)).rewrite(sp.exp))
    if MUT.get("vacuum_rising"):
        vac_dS = sp.Integer(1)                             # the mutant gives the vacuum slab a rising warp
    affine = sp.integrate(sp.exp(-yy / ell), (yy, 0, d))   # int e^A dy across a vacuum slab: finite, both ways
    Akr = sp.log(sp.cosh(yy / Lc))
    kr_nec = sp.simplify(sp.diff(Akr, yy, 2) - sp.exp(-2 * Akr) / Lc ** 2)
    kr_ends = (sp.diff(Akr, yy).subs(yy, -Lc), sp.diff(Akr, yy).subs(yy, Lc))   # A'(y1+), A'(y2-)
    return dict(parts=parts, sign=sign, kr_nec=kr_nec, kr_ends=[sp.nsimplify(e) for e in kr_ends], vac_flat=vac_flat,
                vac_dS=sp.simplify(vac_dS), affine=affine)


def facing():
    """F3: ours decays on both sides; position 2 grows into the slab; E3 on position 2's sides"""
    EP = _load(os.path.join(HERE, "e_positive.py"), "fs_ep")
    both = lambda e1, e2, A1, A2: tuple(bool(v > 0) for v in EP.junction(e1, e2, sp.Integer(A1), sp.Integer(A2)))
    ours = all(both(1, 1, A1, A2) == (True, True) for A1, A2 in ((1, 1), (4, 1), (1, 4)))
    near = -1                                              # F2: position 2's plane grows into the slab
    if MUT.get("p2_decays"):
        near = 1                                           # the mutant lets position 2 decay into the slab too
    p2 = [both(far, near, A1, A2) for far in (1, -1) for A1, A2 in ((1, 1), (4, 1), (1, 4))]
    return dict(ours=ours, p2_never=not any(t and e for t, e in p2))


def horizon():
    """F4: the planar horizon and the causal separation of the two exteriors"""
    r, k, C = sp.symbols("r k C", positive=True)
    rp = [s for s in sp.solve(sp.Eq(k ** 2 * r ** 2 - C / r ** 2, 0), r) if s.is_positive]
    u, v, kap, du, dv = sp.symbols("u v kappa du dv", real=True)
    U, V = -sp.exp(-kap * u), sp.exp(kap * v)
    dU_du, dV_dv = sp.diff(U, u), sp.diff(V, v)
    crossable = False
    if MUT.get("horizon_crossable"):
        crossable = True                                   # the mutant lets a causal curve run between the exteriors
    return dict(rp=rp, rp_ok=len(rp) == 1 and sp.simplify(rp[0] - (C / k ** 2) ** sp.Rational(1, 4)) == 0,
                monotone=sp.simplify(dU_du / (kap * sp.exp(-kap * u))) == 1 and sp.simplify(
                    dV_dv / (kap * sp.exp(kap * v))) == 1, crossable=crossable)


def populate(fc, hz):
    rows = {}
    EP = _load(os.path.join(HERE, "e_positive.py"), "fs_ep2")
    for conn, near, far in itertools.product(("slab", "coincide", "horizon", "own"), (1, -1), (1, -1)):
        if conn == "horizon" and near == -1:
            continue                                       # a plane facing a throat keeps r < R: it decays toward it
        rho, d = EP.junction(near, far, sp.Integer(1), sp.Integer(1))
        both = bool(rho > 0) and bool(d > 0)
        if conn == "slab":
            nec = int(near == -1)                          # F2: decaying into the slab breaks null energy
            if MUT.get("p2_decays"):
                nec = 1
        elif conn == "horizon":
            nec = int(not hz["crossable"])
        else:
            nec = 1
        fixed = int(conn != "coincide")
        rows[(conn, near, far)] = dict(p2=int(both and fixed == 1), nec=nec, fixed=fixed)
    return rows


def cypher(rows):
    held = sorted({tuple(p[c] for c in PROPS) for p in rows.values()})
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "fs_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "fs_ia")
    ix = cy.Index("f_slab", PROPS, [list(c) for c in held], value_order={c: [0, 1] for c in PROPS})
    run = cy.run(ix, "1173", dict(OPTS))
    clo = set(held)
    while True:
        new = {tuple(op(a, b) for a, b in zip(x, y)) for x in clo for y in clo for op in (max, min)} - clo
        if not new:
            break
        clo |= new
    return dict(held=held, reached=(1, 1, 1) in held, closure_adds=sorted(clo - set(held)),
                E={v["language"]: v["E"] for v in run["verdicts"]}, audit=ia.audit_index(PROPS, held),
                langclose=run["langclose_holds"], agreeing=run["pairs_agreeing"],
                holders=sorted((c for c, p in rows.items() if tuple(p[x] for x in PROPS) == (1, 1, 1)), key=str))


def compute():
    fc, hz = facing(), horizon()
    rows = populate(fc, hz)
    return dict(ne=null_energy(), mo=monotone(), fc=fc, hz=hz, rows=rows, cy=cypher(rows))


def report(o):
    print("f_slab.py -- e_positive E6's counter-case under item 274: every static slab, and what escapes it\n")
    print("F1 R_kk = -3 (k^y)^2 (A'' + H^2 e^(-2A)): de Sitter slicing %s, anti-de Sitter (H^2 = -1/L^2) %s" % (
        o["ne"]["dS"], o["ne"]["AdS"]))
    mo = o["mo"]
    print("F2 d/dy(A' e^-A) = (A'' - A'^2) e^-A: %s; the bound's integrand non-negative: %s" % (mo["parts"], mo["sign"]))
    print("   anti-de Sitter control e^2A = cosh^2(y/L): null energy %s, A' at the planes %s" % (mo["kr_nec"],
                                                                                              mo["kr_ends"]))
    print("F3 ours positive and expanding with like decaying sides: %s; position 2, growing into the slab, never both: "
          "%s" % (o["fc"]["ours"], o["fc"]["p2_never"]))
    print("F4 horizon r+ = %s; U, V non-decreasing along future causal curves: %s" % (o["hz"]["rp"], o["hz"]["monotone"]))
    cy = o["cy"]
    print("F5 %d rows; held (p2, nec, fixed): %s; all three reached: %s by %s" % (len(o["rows"]), cy["held"],
                                                                                 cy["reached"], cy["holders"]))
    print("   E %s; langclose %s, %d of 10 pairs agreeing; closure adds %s; audit keys %s one-hot %s" % (
        cy["E"], cy["langclose"], cy["agreeing"], cy["closure_adds"], cy["audit"]["keys"], cy["audit"]["onehot"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("F0 M's item-274 words verbatim in the rulings file", M274 in rul)
    add("F1 R_kk = -3 (k^y)^2 (A'' + H^2 e^(-2A)) from the metric, de Sitter and anti-de Sitter slicings",
        o["ne"]["dS"] and o["ne"]["AdS"])
    mo = o["mo"]
    ok = mo["parts"] and mo["sign"]["flat"] is True and mo["sign"]["dS"] is True and mo["sign"]["AdS"] is not True
    ok &= mo["kr_nec"] == 0 and mo["kr_ends"][0] < 0 < mo["kr_ends"][1]
    ok &= mo["vac_flat"] == 0 and mo["vac_dS"] == 0
    ok &= sp.simplify(mo["affine"] - sp.Symbol("ell", positive=True) * (1 - sp.exp(-sp.Symbol("d", positive=True) /
                                                                              sp.Symbol("ell", positive=True)))) == 0
    add("F2 the warp is monotone across a flat or de Sitter slab: in vacuum exactly (A'' = -H^2 e^(-2A)), with matter "
        "pointwise and net over the segment; the anti-de Sitter slab escapes (cosh warp); a vacuum slab is crossed in "
        "finite affine length", ok)
    add("F3 ours decays on both sides; position 2, growing into a static slab, is never both positive and expanding",
        o["fc"]["ours"] and o["fc"]["p2_never"])
    hz = o["hz"]
    add("F4 planar horizon r+ = (C/k^2)^(1/4); U, V non-decreasing on future causal curves, so no curve runs between "
        "the exteriors", hz["rp_ok"] and hz["monotone"] and not hz["crossable"])
    cy, rows = o["cy"], o["rows"]
    ok = cy["reached"] and len(rows) == 14 and all(h[0] in ("horizon", "own") and h[1:] == (1, 1) for h in cy["holders"])
    ok &= len(cy["holders"]) == 2 and not cy["audit"]["keys"] and not cy["audit"]["onehot"]
    ok &= not any(p["p2"] and p["nec"] for c, p in rows.items() if c[0] == "slab")
    ok &= not any(p["p2"] for c, p in rows.items() if c[0] == "coincide")
    ok &= cy["closure_adds"] == [(0, 0, 0)] and [cy["E"][L] for L in FIVE] == [1, 1, 0, 0, 0] and cy["langclose"]
    add("F5 the all-three cell is reached only beyond a horizon or in position 2's own bulk, decaying on both sides; a "
        "static slab never with null energy kept; the coincidence never fixed; E 1, 1, 0, 0, 0 (the meet (0, 0, 0)), "
        "langclose holds; audit clean", ok)
    return res


MUTANTS = {"ads_ours": "our slab sliced anti-de Sitter",
           "vacuum_rising": "the vacuum slab given a rising warp",
           "p2_decays": "position 2 let decay into the static slab",
           "horizon_crossable": "a causal curve let run between the exteriors"}


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
        print("  mutant %-18s %-46s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
