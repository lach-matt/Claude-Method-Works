#!/usr/bin/env python3
"""e_positive.py -- item 272's owed item (e): the proof 139 (2) orders, position 2's plane's total surface energy --
tension -sigma/4 plus its own matter (184; item 268, H-P2-TOTAL-POSITIVE) -- positive.  M (139 (2)): "positive, and
you have to prove it".  Worked in the conversation (computed with sympy, exact where marked; READ where marked;
estimates marked; deduced where marked; the cypher run and audited; not verified by a separate session; not seated);
2026-10-12.

[M, item 284: 139 (2)'s positivity is owed where the README lands and the corridor's rays cross position 2's plane
("Where it lands").  E7 carries it: the README's own density is above sigma/4 within 2.0e-15 m of the face, where
those rays cross; owed item (e) is closed on E7.]

[Auditing agent, item 281 (the reverse passage, 270/276): written after 270 and missed by item 277: E6's counter-case
is a static slab between the planes (W5; f_slab, 275), and its does-not-show cites the summed-stress junction (W4,
b5_positive B5a).  Kept as written.]

  E0 (read) M's words, verbatim in the rulings file: 139 (2) and (3), 184, 268.
  E1 (computed, exact) Israel's condition, contracted with the plane's own time u: rho_b = -(1/kappa5^2) [sum over the
     sides of theta_s], theta_s the spatial trace of K for the normal pointing into that side.  So at every point the
     plane's total surface energy is positive exactly when its 3-volume falls off the plane on net -- the warp
     decaying away from it.  No symmetry is assumed.  Control: Randall-Sundrum's plane, -(1/kappa^2)(-3k - 3k) = 6k/kappa^2
     = 3 c^4/(4 pi G ell^2) = sigma with kappa5^2 = 8 pi G ell/c^4, k = 1/ell (G5 = G ell).
  E2 (computed, exact) The plane as a Friedmann sheet in Schwarzschild-AdS5 (f = k^2 r^2 - C/r^2, flat slicing, scale
     factor a = R(tau)): K^x_x = n^r/R = +-sqrt(H^2 + k^2 - C/a^4).  So rho_b = (3/kappa^2) (e1 sqrt(A1) + e2 sqrt(A2)),
     A_i = H^2 + k_i^2 - C_i/a^4, e_i = +1 where the warp decays into side i, -1 where it grows (the Binetruy-Deffayet-
     Langlois / Kraus junction, standard, derived here rather than READ).
  E3 (computed, exact) The sign theorem.  Like orientations: rho_b . d rho_b/dH^2 = +(9/kappa^4)(sqrt A1 + sqrt A2)^2
     /(2 sqrt(A1 A2)) > 0.  Opposite orientations: -(9/kappa^4)(sqrt A1 - sqrt A2)^2/(2 sqrt(A1 A2)) <= 0.  So the README's
     energy, added to the plane, raises its expansion rate (dH^2/d rho_b > 0) AND finds its total positive only where
     the warp decays away on both sides; on a plane with like sides (mirrored, or one-sided) the two are the same
     statement; with opposite sides they never hold together.
  E4 (computed, exact) Position 2's own four-dimensional gravity.  The zero mode's norm over an infinite side,
     int_0^oo e^(-2 e y/ell2) dy, is ell2/2 where the warp decays and diverges where it grows: a growing infinite side
     leaves position 2 no Newton constant of its own (items 221-236 build position 2's matter with one, p2_gravity).
  E5 (computed; the cypher, roster 1173, audited) The index: each side's orientation e_i in {+1, -1} (e2 = 0: a
     one-sided plane), which side has the larger A (equal, 1, 2), which side is a finite slab (none, 1, 2) -- 40 rows,
     each with total_pos (139 (2)), expands (139 (3), the board's reading below) and gravity (E4).  The all-three cell
     is REACHED, by the 11 rows decaying on every side and by no other; (1, 1, 0) is held by none -- 139 (2) with 139
     (3) gives position 2 its own gravity.  The five operator-bearing languages agree at E = 1, and the one cell the
     closure under coordinatewise max and min adds is (1, 1, 0): the closure the languages expect is the cell E3-E4
     forbid.  b4d_stage6 J3's matter-free mirrored sheet at -1/3 lambda_RS (growing on both sides) sits at (0, 0, 0):
     it fails all three, the board's matter-free limit (184).
  E6 (deduced; the board's reading) The proof.  139 (3), "Absorbing of the README into position 2 is an expansion of
     that universe", is read as: the README's energy added to position 2's plane raises its expansion rate, the bulk's
     k_i and C_i held through the absorption.  Position 2's plane is read as having like sides: at 127's coincidence
     the slab of multiplane M4's arrangement has no width (M4 evaluates 139 (1)'s quarter there, r = 0), and as a
     separate position (152) b4d_stage6 J3 had it mirrored in its own bulk.  By E3, the expansion then forces e = +1 on
     both sides, and rho_b = (3/kappa^2)(sqrt A1 + sqrt A2) > 0: position 2's matter is rho_m = sigma/4 + rho_b >
     sigma/4 at every point where the plane is locally Friedmann -- the "at least sigma/4" of items 268 and 272, strict.
     184 follows: a matter-free plane at -sigma/4 is excluded there.  The one counter-case is M4's arrangement at a
     separation r > 0 (Lykken-Randall's, in which Pilo-Rattazzi-Zaffaroni find the ghost radion, READ in multiplane.py):
     position 2's plane grows into the slab with k_L and decays beyond with k_R = 3 k_L/4, opposite sides, the row (+1,
     -1, 2, 2) at (0, 1, 1) -- it expands, it has gravity, and its total is negative, static 3 (k_R - k_L)/kappa^2 = -1/4
     of our plane's 3 k_L/kappa^2 on its one side (139 (1)'s quarter, in M4's count); positive only if the slab carries
     more bulk mass than the far side, C_L - C_R > (k_L^2 - k_R^2) a^4 = (7/16) k_L^2 a^4, and then it contracts.  There
     139 (2) and 139 (3) conflict (E3), and 127 is what excludes it.
  E7 (computed) At the example (ell = 13.964 um, E = 1.281e9 J): sigma/4 = 3.7e52 J/m^3; near the face the emerging
     README alone carries the plane past sigma/4 within R <= (3E/(pi sigma))^(1/3) = 2.0e-15 m = 1.8e5 r_h.  Beyond it
     the excess rho_b is the bulk's (E6), of the plane's own scale -- with like sides of position 2's own ell2, static
     and without bulk mass, rho_b = 6 k2/kappa^2, position 2's lambda_RS.

What this does not show.
  - That position 2's plane has like sides: it rests on 127 (no slab at the coincidence) and on J3's mirrored reading
    of 152 (E6); 138 alone does not give it -- M4 built its opposite-sided arrangement from 138.
  - That position 2's separate total is fixed by a junction at the coincidence: there Israel's condition sees only the
    summed stress (b5_positive B5a, b4d_stage6 J2); E2-E3 apply to position 2's plane as a sheet with its own sides.
  - The README's absorption as a local, inhomogeneous event: E2-E3 are the plane's Friedmann average; pointwise, E1
    makes positivity the warp decaying at each point, and ordinary inhomogeneity (densities far below sigma) is a small
    perturbation of rho_b, not a reversal of its sign (estimate).
  - b4d_stage5 F2: eq. (17) data on a decaying side ran singular within 8-16 clocks -- the large-scale model; our own
    plane decays on both sides alike (b4d_stage6 J2).  Recorded, not repaired.
  - Position 2's ell2, G2 and bulk mass C2 (202: its own values).

Imports index_audit.py, tools/cypher.py and p2_gravity.py by path.  Stdlib + sympy.
python3 e_positive.py [--selftest | --mutants]
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
M_WORDS = ["2 - positive, and you have to prove it.",
           "Absorbing of the README into position 2 is an expansion of that universe",
           "There are no matter free planes", "Yes, tension plus matter"]
PROPS = ["total_pos", "expands", "gravity"]
FIVE = ["order", "algebra", "geometry", "information", "statistics"]
N_EX = 2742570311524972


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


def israel():
    """E1: rho_b from the spatial traces; the Randall-Sundrum control and sigma"""
    k, kap2, G, ell, c = sp.symbols("k kappa5sq G ell c", positive=True)
    theta_plus, theta_minus = -3 * k, -3 * k                # each side's normal pointing into it, warp decaying
    rho_rs = -(theta_plus + theta_minus) / kap2
    sigma = 3 * c ** 4 / (4 * sp.pi * G * ell ** 2)
    as_sigma = sp.simplify(rho_rs.subs({kap2: 8 * sp.pi * G * ell / c ** 4, k: 1 / ell}) - sigma)
    return dict(rho_rs=rho_rs, rs_ok=sp.simplify(rho_rs - 6 * k / kap2) == 0, sigma_ok=as_sigma == 0)


def sheet():
    """E2: K^x_x of a Friedmann sheet r = R(tau) in f = k^2 r^2 - C/r^2, by the Christoffel symbols"""
    k, C, R, Rd = sp.symbols("k C R Rdot", positive=True)
    eps = sp.Symbol("epsilon")
    r = sp.Symbol("r", positive=True)
    f = k ** 2 * r ** 2 - C / r ** 2
    g = sp.diag(-f, 1 / f, r ** 2, r ** 2, r ** 2)
    ginv = g.inv()
    X = [sp.Symbol("t"), r, *sp.symbols("x1 x2 x3")]
    # Gamma^mu_{x1 x1}
    gam = [sp.simplify(sum(ginv[m, l] * (2 * sp.diff(g[l, 2], X[2]) - sp.diff(g[2, 2], X[l])) for l in range(5)) / 2)
           for m in range(5)]
    fR = f.subs(r, R)
    Td = sp.sqrt(fR + Rd ** 2) / fR                         # -f Tdot^2 + Rdot^2/f = -1
    n_low = [eps * (-Rd), eps * Td, 0, 0, 0]
    norm = sp.simplify(sum(ginv[m, m].subs(r, R) * n_low[m] ** 2 for m in range(5)).subs(eps, 1))
    Kxx = -sum(n_low[m] * gam[m].subs(r, R) for m in range(5))
    Kmix = sp.simplify(Kxx / R ** 2)
    H = Rd / R
    target = eps * sp.sqrt(H ** 2 + k ** 2 - C / R ** 4)
    return dict(norm_ok=sp.simplify(norm - 1) == 0, K=Kmix,
                K_ok=sp.simplify((Kmix ** 2 - target ** 2).subs(eps, 1)) == 0 and sp.simplify(
                    (Kmix / eps).subs(eps, 1)) .is_positive is not False)


def junction(e1, e2, A1, A2, kap2=1):
    """rho_b and its derivative in H^2 (A_i = H^2 + k_i^2 - C_i/a^4); e = +1 decaying, -1 growing, 0 absent"""
    h = sp.Symbol("h", nonnegative=True)
    s = 1
    if MUT.get("orientation_flip"):
        s = -1                                             # the mutant reads a decaying side as growing
    rho = 3 * s * (e1 * sp.sqrt(A1 + h) + e2 * sp.sqrt(A2 + h)) / kap2
    d = sp.diff(rho, h)
    return rho.subs(h, 0), d.subs(h, 0)


def sign_theorem():
    """E3: rho_b . d rho_b/dH^2, exact, for like and opposite orientations"""
    A1, A2, kap2 = sp.symbols("A1 A2 kappa5sq", positive=True)
    out = {}
    for e1, e2 in ((1, 1), (-1, -1), (1, -1), (-1, 1)):
        rho, d = junction(e1, e2, A1, A2, kap2)
        out[(e1, e2)] = sp.simplify(rho * d)
    like = sp.simplify(out[(1, 1)] - 9 * (sp.sqrt(A1) + sp.sqrt(A2)) ** 2 / (2 * kap2 ** 2 * sp.sqrt(A1 * A2))) == 0
    like &= sp.simplify(out[(-1, -1)] - out[(1, 1)]) == 0
    opp = sp.simplify(out[(1, -1)] + 9 * (sp.sqrt(A1) - sp.sqrt(A2)) ** 2 / (2 * kap2 ** 2 * sp.sqrt(A1 * A2))) == 0
    opp &= sp.simplify(out[(-1, 1)] - out[(1, -1)]) == 0
    return dict(products=out, like=like, opp=opp)


def zero_mode():
    """E4: the zero mode's norm over an infinite side"""
    y, l2 = sp.symbols("y ell2", positive=True)
    dec = sp.integrate(sp.exp(-2 * y / l2), (y, 0, sp.oo))
    grow = sp.integrate(sp.exp(2 * y / l2), (y, 0, sp.oo))
    if MUT.get("grow_normalizable"):
        grow = l2 / 2                                      # the mutant lets a growing infinite side hold the mode
    return dict(dec=dec, grow=grow, dec_ok=sp.simplify(dec - l2 / 2) == 0, grow_inf=grow == sp.oo)


def populate(zm):
    rows = {}
    A_of = {"eq": (1, 1), "1": (4, 1), "2": (1, 4)}
    for e1, e2, big, fin in itertools.product((1, -1), (1, -1, 0), ("eq", "1", "2"), ("none", "1", "2")):
        if e2 == 0 and (big != "eq" or fin == "2"):
            continue                                       # a one-sided plane: one A, no second side to be finite
        A1, A2 = A_of[big]
        rho, d = junction(e1, e2, sp.Integer(A1), sp.Integer(A2))
        expands = d > 0
        if MUT.get("expands_as_total"):
            expands = rho > 0                              # the mutant reads expansion off the total's sign
        norm_ok = True
        for side, e in ((1, e1), (2, e2)):
            if e == 0 or fin == str(side):
                continue                                   # absent, or a finite slab: the mode's norm is finite
            norm_ok &= (zm["dec"] if e == 1 else zm["grow"]) != sp.oo
        rows[(e1, e2, big, fin)] = dict(total_pos=int(bool(rho > 0)), expands=int(bool(expands)),
                                        gravity=int(bool(norm_ok)), rho=rho, d=d)
    return rows


def cypher(rows):
    held = sorted({tuple(p[c] for c in PROPS) for p in rows.values()})
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "ep_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "ep_ia")
    ix = cy.Index("e_positive", PROPS, [list(c) for c in held], value_order={c: [0, 1] for c in PROPS})
    run = cy.run(ix, "1173", dict(OPTS))
    clo = set(held)
    while True:
        new = {tuple(op(a, b) for a, b in zip(x, y)) for x in clo for y in clo for op in (max, min)} - clo
        if not new:
            break
        clo |= new
    return dict(held=held, reached=(1, 1, 1) in held, closure_adds=sorted(clo - set(held)), E={v["language"]: v["E"] for v in run["verdicts"]},
                audit=ia.audit_index(PROPS, held),
                holders=sorted((c for c, p in rows.items() if (p["total_pos"], p["expands"], p["gravity"]) == (1, 1, 1)),
                               key=str))


def lr_case():
    """E6's counter-case: M4's arrangement at r > 0 -- decaying beyond with k_R = 3 k_L/4, growing into the slab"""
    kL, a, H2 = sp.symbols("k_L a H2", positive=True)
    CL, CR = sp.symbols("C_L C_R", real=True)
    kR = sp.Rational(3, 4) * kL
    Ad, Ag = H2 + kR ** 2 - CR / a ** 4, H2 + kL ** 2 - CL / a ** 4
    # rho_b > 0 iff sqrt(Ad) > sqrt(Ag) iff Ad - Ag > 0
    thresh = sp.solve(sp.Eq(Ad - Ag, 0), CL)[0] - CR
    rho_static = 3 * (kR - kL)                              # C equal, H = 0, kappa = 1: Lykken-Randall's tension
    # over our plane counted on its one physical side, 3 k_L (Pilo-Rattazzi-Zaffaroni's count, multiplane M4)
    return dict(thresh=sp.simplify(thresh), thresh_ok=sp.simplify(thresh - sp.Rational(7, 16) * kL ** 2 * a ** 4) == 0,
                quarter=sp.simplify(rho_static / (3 * kL)))


def example():
    PG = _load(os.path.join(HERE, "p2_gravity.py"), "ep_pg")
    l5 = (PG.HBAR * PG.G * PG.ELL_MAX / PG.C ** 3) ** (1 / 3)
    rh = (2 * N_EX * math.log(2) / math.pi ** 2) ** (1 / 3) * l5
    E = 3 * math.pi * PG.C ** 4 * rh ** 2 / (8 * PG.G * PG.ELL_MAX)
    sigma = 3 * PG.C ** 4 / (4 * math.pi * PG.G * PG.ELL_MAX ** 2)
    R = (3 * E / (math.pi * sigma)) ** (1 / 3)
    dens = E / (4 / 3 * math.pi * R ** 3)
    return dict(rh=rh, E=E, quarter=sigma / 4, R=R, R_rh=R / rh, at_R=dens / (sigma / 4))


def compute():
    zm = zero_mode()
    rows = populate(zm)
    return dict(isr=israel(), sh=sheet(), st=sign_theorem(), zm=zm, rows=rows, cy=cypher(rows), lr=lr_case(),
                ex=example())


def report(o):
    print("e_positive.py -- the proof 139 (2) orders: position 2's plane, tension -sigma/4 plus matter, positive "
          "(item 272 (e))\n")
    print("E1 Randall-Sundrum control rho_b = %s; equals sigma = 3c^4/(4 pi G ell^2): %s" % (o["isr"]["rho_rs"],
                                                                                           o["isr"]["sigma_ok"]))
    print("E2 K^x_x of the Friedmann sheet = %s" % o["sh"]["K"])
    for k_, v in o["st"]["products"].items():
        print("E3 orientation %-8s rho_b . d rho_b/dH^2 = %s" % (k_, v))
    print("E4 zero mode over an infinite side: decaying %s, growing %s" % (o["zm"]["dec"], o["zm"]["grow"]))
    cy = o["cy"]
    print("E5 %d rows; held (total_pos, expands, gravity): %s" % (len(o["rows"]), cy["held"]))
    print("   all three reached: %s, by %d rows, orientations %s; E %s; closure adds %s; audit keys %s one-hot %s" % (
        cy["reached"], len(cy["holders"]), sorted({h[:2] for h in cy["holders"]}), cy["E"], cy["closure_adds"],
        cy["audit"]["keys"], cy["audit"]["onehot"]))
    print("E6 M4's arrangement at r > 0, row (+1, -1, 2, 2): %s; its static total over our one-sided 3 k_L: %s; positive only if "
          "C_L - C_R > %s" % (tuple(o["rows"][(1, -1, "2", "2")][c] for c in PROPS), o["lr"]["quarter"], o["lr"]["thresh"]))
    x = o["ex"]
    print("E7 sigma/4 = %.3g J/m^3; the README covers sigma/4 within R = %.3g m = %.3g r_h" % (x["quarter"], x["R"],
                                                                                              x["R_rh"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("E0 M's words (139 (2), 139 (3), 184, 268) verbatim in the rulings file", all(w in rul for w in M_WORDS))
    add("E1 rho_b = -(1/kappa^2) sum theta_s: Randall-Sundrum's 6k/kappa^2 = 3c^4/(4 pi G ell^2) = sigma",
        o["isr"]["rs_ok"] and o["isr"]["sigma_ok"])
    add("E2 the Friedmann sheet's normal is unit and K^x_x = +-sqrt(H^2 + k^2 - C/a^4)", o["sh"]["norm_ok"] and
        o["sh"]["K_ok"])
    add("E3 rho_b . d rho_b/dH^2 is +(sqrtA1 + sqrtA2)^2/(2 sqrt(A1A2)) for like sides, -(sqrtA1 - sqrtA2)^2/(...) for "
        "opposite", o["st"]["like"] and o["st"]["opp"])
    add("E4 the zero mode's norm is ell2/2 over a decaying infinite side and diverges over a growing one",
        o["zm"]["dec_ok"] and o["zm"]["grow_inf"])
    cy, rows = o["cy"], o["rows"]
    like = [p for c, p in rows.items() if c[1] in (c[0], 0)]
    opp = [p for c, p in rows.items() if c[1] == -c[0]]
    ok = cy["reached"] and len(rows) == 40 and {h[:2] for h in cy["holders"]} == {(1, 1), (1, 0)}
    ok &= all(c[0] == 1 and c[1] in (1, 0) for c in cy["holders"]) and len(cy["holders"]) == 11
    ok &= cy["closure_adds"] == [(1, 1, 0)] and all(cy["E"][L] == 1 for L in FIVE)
    ok &= (1, 1, 0) not in cy["held"] and not cy["audit"]["keys"] and not cy["audit"]["onehot"]
    ok &= all(p["total_pos"] == p["expands"] for p in like) and not any(p["total_pos"] and p["expands"] for p in opp)
    ok &= rows[(-1, -1, "eq", "none")]["total_pos"] + rows[(-1, -1, "eq", "none")]["expands"] + \
        rows[(-1, -1, "eq", "none")]["gravity"] == 0
    add("E5 the all-three cell is reached only by planes decaying on every side (11 of 40 rows); like sides: expands "
        "iff positive; opposite: never both; (1, 1, 0) unheld, the closure's one cell, E = 1 in all five languages; "
        "audit clean; J3's growing mirror at (0, 0, 0)", ok)
    lr, row = o["lr"], o["rows"][(1, -1, "2", "2")]
    ok = (row["total_pos"], row["expands"], row["gravity"]) == (0, 1, 1) and lr["thresh_ok"]
    ok &= lr["quarter"] == sp.Rational(-1, 4)
    add("E6 M4's arrangement at r > 0 expands with gravity and a negative total, (0, 1, 1), 139 (1)'s quarter; positive "
        "only past C_L - C_R = (7/16) k_L^2 a^4", ok)
    x = o["ex"]
    ok = "%.2g" % x["quarter"] == "3.7e+52" and "%.2g" % x["R"] == "2e-15" and "%.2g" % x["R_rh"] == "1.8e+05"
    ok &= abs(x["at_R"] - 1) < 1e-9
    add("E7 sigma/4 = 3.7e52 J/m^3; the README covers it within 2.0e-15 m = 1.8e5 r_h", ok)
    return res


MUTANTS = {"orientation_flip": "a decaying side read as growing in the junction",
           "expands_as_total": "expansion read off the total's sign, not dH^2/d rho",
           "grow_normalizable": "a growing infinite side taken to hold the zero mode"}


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
        print("  mutant %-18s %-52s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
