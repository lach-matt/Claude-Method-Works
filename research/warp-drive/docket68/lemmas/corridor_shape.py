#!/usr/bin/env python3
"""corridor_shape.py -- the corridor as the surface where the two planes' bulks meet (item 203), its shape, and the
null energy (Z) asks of it; put to the cypher (computed, deduced; not verified by a separate session; not seated;
2026-10-10).

Item 203: the corridor is the surface where the two planes' own bulks meet; within one universe the two bulks are the
same (202), so the corridor is a symmetric junction in the full static bulk of eq. (17) (b4_static.py's exact series,
flat limit), with depth y = Y(r) below each plane.  Seated (Z) through TS (p2_full.py) asks its null energy to be
non-negative in every tangent direction.

  S1 (computed, sympy) the extrinsic curvature of a graph y = Y(r) in -A dt^2 + B dr^2 + C dOmega^2 + dy^2; at Y const it
     reduces to k = (1/2) d_y ln g.  Y'' enters k_r only, through Y'' B/(B + Y'^2)^2 (B small near the throat)
  S2 (computed) the corridor's own Killing energy is (I/4pi)(m/ell) E, at most 0.76 (m/ell) E (d = 1-1.5m): E is read
     on the planes (111, 203 as read: each plane reads eq. (17) with mass m), not carried by the surface's own stress
     [STALE, item 208 (recorded by the item-208 critics; no function here computes it): on the corrected bank the
     marginal members carry q = I/4pi = 0.67-5.66 (box members), 2.71-4.22 at slope 0 and depth 1-1.5m; the first
     interpolation gave 0.70-1.00.  The 0.76 is not reproduced under any reading tried]
  S0 (computed; CORRECTION, 2026-10-10, pass 3 of the cycle) the bank is interpolated between its columns in
     u = ln(r - 2) on the near-horizon-scaled functions A/x, B x^2, C (x = r - 2): within 1e-4 of three exactly
     computed columns mid-interval (corridor_shape_mid.json).  The first version interpolated A, B, C in r unscaled,
     which put g_rr 8% low between 2.005m and 2.04m.  Every result of S3-S6 as first written rested on that error; they
     are restated below, and the first wording is kept here for the record: S3 "meets our plane at r = 2.10-2.20m ...
     its tangential null energy turns negative from r = 2.05-2.09m"; S5 "the gap ... 0.027-0.126 (m/ell) E, at most
     1/68 of E"; S6 "the README is the only carrier that closes the gap"
  S3 (computed) shapes: constant depth -- radial null energy < 0 (small), tangential and energy > 0; deepening outward
     (a > 0) -- worse; rising (a < 0) -- slightly better, still < 0; a bump -- radial > 0 where Y'' < 0, worse on its
     flanks.  The marginal shape (rho + p_r held at 0 by solving for Y''): energy > 0 throughout, and it meets our plane
     at r = 3.1-3.8m for every start depth (0.25m, 1m) and slope (0, +-0.3), beyond r_b = 3.01m (rim_profile P2), with
     its tangential null energy never negative.  Held strictly positive instead (margin 0.01), the radial condition
     brings the rim inside r_b (2.26-2.87m) and the tangential fails there (rim_profile P3)
  S4 (computed; the cypher CLASSIFIES) roster 1173 on the computed shapes: the target (a whole surface with both null
     directions non-negative and energy positive) is DATA -- the marginal corridor -- admitted by all five; with that
     cell left out statistics refuses again
  S5 (computed) at margin 0 no tangential gap remains on the marginal family
  S6 (computed; the cypher CLASSIFIES) the rim's candidate carriers as cells -- the shape alone (now: no gap, positive,
     sufficient), our plane's matter, the README on the corridor.  The shape alone closes: no carrier is needed for the
     null energy.  The ring where the surfaces meet (its force balance) is forming_rim's and rim_profile's.  LIMIT
     (deduced): a thin surface's stress IS the jump in extrinsic curvature across it
So: in the throat both directions hold (ITEM197); the marginal corridor carries the radial condition at zero across the
whole surface to a rim beyond r_b where it meets our plane (r ~ 3.1-3.8m), with the tangential null energy and the
energy positive all the way.  Flat limit; Pade continuation (a heuristic); thin surface; static.
Imports p2_full.py (and through it b4_static.py) and tools/cypher.py by path.  Bank: corridor_shape_bank.json (Pade
coefficients per column; --regenerate rebuilds it, about 8 minutes).  python3 corridor_shape.py [--selftest | --mutants]
"""
import bisect
import contextlib
import importlib.util
import io
import json
import math
import os
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
BANK = os.path.join(HERE, "corridor_shape_bank.json")
MUT = {}


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


_P2 = []


def p2():
    if not _P2:
        _P2.append(_load(os.path.join(HERE, "p2_full.py"), "cs_p2_full"))
    return _P2[0]


# ------------------------------------------------------------------------------------------------- S1: curvature
def curvature_exprs():
    t, r, th, ph, y = sp.symbols("t r theta phi y", real=True)
    Af, Bf, Cf = [sp.Function(n)(r, y) for n in "ABC"]
    Y = sp.Function("Y")(r)
    X = [t, r, th, ph, y]
    g = sp.diag(-Af, Bf, Cf, Cf * sp.sin(th) ** 2, 1)
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(5)) / 2
             for c in range(5)] for b in range(5)] for a in range(5)]
    emb, U = [t, r, th, ph, Y], [t, r, th, ph]
    E = [[sp.diff(emb[m], U[a]) for m in range(5)] for a in range(4)]
    nl = sp.Matrix([0, -sp.diff(Y, r), 0, 0, 1])
    nl = nl / sp.sqrt((nl.T * gi * nl)[0])
    sub = lambda e: e.subs(y, Y)
    K = sp.zeros(4)
    for a in range(4):
        for b in range(4):
            K[a, b] = -sub(sum(nl[m] * (sp.diff(emb[m], U[a], U[b]) + sum(Gam[m][n][q] * E[a][n] * E[b][q]
                                                                            for n in range(5) for q in range(5)))
                               for m in range(5)))
    h = sp.Matrix(4, 4, lambda a, b: sub(sum(g[m, n] * E[a][m] * E[b][n] for m in range(5) for n in range(5))))
    Km = h.inv() * K
    S = sp.symbols("A B C Ay By Cy Ar Br Cr Y1 Y2", real=True)
    Av, Bv, Cv, Ay, By, Cy, Ar, Br, Cr, Y1, Y2 = S
    rep = {}
    for F, v, vy, vr in ((Af, Av, Ay, Ar), (Bf, Bv, By, Br), (Cf, Cv, Cy, Cr)):
        rep[sp.Derivative(F.subs(y, Y), Y)] = vy
        rep[sp.Subs(sp.Derivative(F, r), y, Y)] = vr
    out = {}
    for name, i in (("kt", 0), ("kr", 1), ("kth", 2)):
        e = sp.simplify(Km[i, i]).xreplace(rep)
        e = e.xreplace({sp.Derivative(Y, (r, 2)): Y2}).xreplace({sp.Derivative(Y, r): Y1})
        e = e.xreplace({Af.subs(y, Y): Av, Bf.subs(y, Y): Bv, Cf.subs(y, Y): Cv})
        sgn = -1 if not MUT.get("normal_out") else 1                 # normal into the slab (toward its plane)
        out[name] = sp.lambdify(S, sgn * e, "math")
        out[name + "_expr"] = e
    return out


# ------------------------------------------------------------------------------------------------- the bulk bank
def regenerate(cols=None):
    P = p2()
    b4 = P._b4()
    rs = cols or json.load(open(os.path.join(HERE, "b4_static.json")))["r"]
    mp.mp.dps = 40
    bank = {}
    for rc in rs:
        ser = b4.series(rc, 40)
        entry = {}
        for X in "ABC":
            for i in (0, 1):
                c = ser[X][i]
                even = [c[2 * j] for j in range(21)]
                for (a1, b1) in ((10, 10), (8, 8), (6, 6)):
                    try:
                        num, den = P._pade(even, a1, b1)
                        entry["%s%d" % (X, i)] = [[str(v) for v in num], [str(v) for v in den]]
                        break
                    except ZeroDivisionError:
                        continue
        bank[rc] = entry
    return bank


def load_bank():
    raw = json.load(open(BANK))
    return {rc: {k: ([float(v) for v in nd[0]], [float(v) for v in nd[1]]) for k, nd in e.items()} for rc, e in raw.items()}


def _ev(p, s):
    return sum(c * s ** k for k, c in enumerate(p))


def _dev(p, s):
    return sum(k * c * s ** (k - 1) for k, c in enumerate(p) if k)


class Bulk:
    def __init__(self, bank):
        self.b = bank
        self.rs = sorted(bank, key=lambda x: float(sp.Rational(x)))
        self.rv = [float(sp.Rational(x)) for x in self.rs]

    def col(self, i, Yv):
        e, s, out = self.b[self.rs[i]], Yv * Yv, {}
        for X in "ABC":
            n0, d0 = e[X + "0"]
            n1, d1 = e[X + "1"]
            v = _ev(n0, s) / _ev(d0, s)
            dv = (_dev(n0, s) * _ev(d0, s) - _ev(n0, s) * _dev(d0, s)) / _ev(d0, s) ** 2 * 2 * Yv
            out[X] = (v, dv, _ev(n1, s) / _ev(d1, s))
        return out

    POW = {"A": 1, "B": -2, "C": 0}                           # near the horizon A ~ x, B ~ x^-2, C ~ 1, x = r - 2

    def at(self, r, Yv):
        """Hermite interpolation between banked columns, in u = ln(r - 2) on the scaled functions F / x^p (S0: within 1e-4,
        5e-5 of exact columns mid-interval).  The first version interpolated F itself in r, which put g_rr 8% low
        between 2.005m and 2.04m (S0's mutant 'hermite_r')."""
        j = max(0, min(len(self.rv) - 2, bisect.bisect_right(self.rv, r) - 1))
        r0, r1 = self.rv[j], self.rv[j + 1]
        c0, c1 = self.col(j, Yv), self.col(j + 1, Yv)
        out = {}
        if MUT.get("hermite_r"):
            h, t = r1 - r0, (r - r0) / (r1 - r0)
            for X in "ABC":
                f0, fy0, fr0 = c0[X]
                f1, fy1, fr1 = c1[X]
                f = (2*t**3 - 3*t**2 + 1) * f0 + (t**3 - 2*t**2 + t) * h * fr0 + (-2*t**3 + 3*t**2) * f1 + (t**3 - t**2) * h * fr1
                fr = ((6*t**2 - 6*t) / h) * f0 + (3*t**2 - 4*t + 1) * fr0 + ((-6*t**2 + 6*t) / h) * f1 + (3*t**2 - 2*t) * fr1
                out[X] = (f, (1 - t) * fy0 + t * fy1, fr)
            return out
        u0, u1, u = math.log(r0 - 2), math.log(r1 - 2), math.log(r - 2)
        h, t, x = u1 - u0, (u - u0) / (u1 - u0), r - 2
        for X in "ABC":
            p = self.POW[X]

            def sc(c, rr):
                f, fy, fr = c[X]
                xx = rr - 2
                return f / xx**p, fy / xx**p, (fr / xx**p - p * f / xx**(p + 1)) * xx
            g0, gy0, gu0 = sc(c0, r0)
            g1, gy1, gu1 = sc(c1, r1)
            g = (2*t**3 - 3*t**2 + 1) * g0 + (t**3 - 2*t**2 + t) * h * gu0 + (-2*t**3 + 3*t**2) * g1 + (t**3 - t**2) * h * gu1
            gu = ((6*t**2 - 6*t) / h) * g0 + (3*t**2 - 4*t + 1) * gu0 + ((-6*t**2 + 6*t) / h) * g1 + (3*t**2 - 2*t) * gu1
            out[X] = (g * x**p, ((1 - t) * gy0 + t * gy1) * x**p, (gu / x) * x**p + p * g * x**(p - 1))
        return out


def stresses(ks, g, Y1, Y2):
    a = (g["A"][0], g["B"][0], g["C"][0], g["A"][1], g["B"][1], g["C"][1], g["A"][2], g["B"][2], g["C"][2], Y1, Y2)
    kt, kr, kth = ks["kt"](*a), ks["kr"](*a), ks["kth"](*a)
    return -(kr + 2 * kth), kt - kr, kt - kth                         # rho, rho + p_r, rho + p_theta (2/kappa^2 units)


def marginal(ks, bulk, d, margin=0.0, slope0=0.0, rmax=6.0):
    def Y2m(r, Yv, Y1):
        g = bulk.at(r, Yv)
        a0 = (g["A"][0], g["B"][0], g["C"][0], g["A"][1], g["B"][1], g["C"][1], g["A"][2], g["B"][2], g["C"][2], Y1, 0.0)
        a1 = a0[:-1] + (1.0,)
        kt0, kr0, kr1 = ks["kt"](*a0), ks["kr"](*a0), ks["kr"](*a1)
        if MUT.get("drop_curvature"):
            return 0.0
        return (kt0 - margin - kr0) / (kr1 - kr0)
    r, Yv, Y1, out = bulk.rv[0], d, slope0, []
    while r < rmax:
        h = 2e-4 if r < 2.1 else (1e-3 if r < 3 else 1e-2)
        f = lambda rr, st: (st[1], Y2m(rr, st[0], st[1]))
        k1 = f(r, (Yv, Y1)); k2 = f(r + h/2, (Yv + h/2*k1[0], Y1 + h/2*k1[1]))
        k3 = f(r + h/2, (Yv + h/2*k2[0], Y1 + h/2*k2[1])); k4 = f(r + h, (Yv + h*k3[0], Y1 + h*k3[1]))
        Yv += h/6*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]); Y1 += h/6*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1]); r += h
        if not (0.0 < Yv < 3.0):
            return {"rim": r if Yv <= 0.01 else None, "rows": out}
        g = bulk.at(r, Yv)
        out.append((r, Yv, Y1) + stresses(ks, g, Y1, Y2m(r, Yv, Y1)))
    return {"rim": None, "rows": out}


def cypher_run():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "cs_cypher")
    C = ["shape", "radial", "tangential", "energy", "whole"]
    # 4: the marginal corridor -- radial held at 0 (1), tangential > 0 at margin 0 since S0's correction (2)
    cells = [(0, 0, 2, 1, 1), (1, 0, 2, 1, 1), (2, 0, 2, 1, 1), (2, 0, 0, 0, 1), (3, 0, 2, 1, 1), (3, 0, 2, 0, 1),
             (4, 1, 2 if not MUT.get("old_tangential") else 0, 1, 1), (5, 1, 2, 1, 0)]
    ok = lambda h: h[1] >= 1 and h[2] >= 1 and h[3] == 1 and h[4] == 1

    def ask(cs):
        cl = sorted(set(cs))
        ix = cy.Index("shapes", C, [list(c) for c in cl])
        inv = [{v: k for k, v in ix.code[i].items()} for i in range(len(C))]
        res = {}
        for lang in ("order", "algebra", "geometry", "information", "statistics"):
            out, _ = cy.ADMISSION[lang][0](ix, {})
            res[lang] = None if out is None else any(ok(tuple(inv[i][c[i]] for i in range(len(C)))) for c in out)
        return res
    return {"all": ask(cells), "leave": ask([c for c in cells if c[0] != 5]), "leave4": ask([c for c in cells if c[0] != 4])}


def rim_gap(ks, bulk, d):
    run = marginal(ks, bulk, d, 0.0, 0.0)
    rows, gap, tot = run["rows"], 0.0, 0.0
    for (r0, Y0, Y10, rho0, nr0, nt0), (r1, *_rest) in zip(rows, rows[1:]):
        g = bulk.at(r0, Y0)
        w = math.sqrt(g["A"][0] * (g["B"][0] + Y10 ** 2)) * g["C"][0] * 4 * math.pi
        gap += max(0.0, -nt0) * w * (r1 - r0)
        tot += rho0 * w * (r1 - r0)
    return {"gap_over_E_times_ell_over_m": gap / (4 * math.pi), "gap_over_energy": gap / tot}


def rim_cypher():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "cs_cypher_rim")
    C = ["carrier", "sign", "sufficient", "compatible"]
    # shape alone (no gap at margin 0 since S0's correction: positive, sufficient); our plane's matter; the README
    cells = [(0, 1, 1, 1) if not MUT.get("old_tangential") else (0, 0, 0, 1), (1, 1, 0, 1), (2, 1, 1, 1)]
    if MUT.get("readme_insufficient"):
        cells[2] = (2, 1, 0, 1)
    ok = lambda h: h[1] == 1 and h[2] == 1 and h[3] == 1

    def ask(cs):
        cl = sorted(set(cs))
        ix = cy.Index("rim", C, [list(c) for c in cl])
        inv = [{v: k for k, v in ix.code[i].items()} for i in range(len(C))]
        res = {}
        for lang in ("order", "algebra", "geometry", "information", "statistics"):
            out, _ = cy.ADMISSION[lang][0](ix, {})
            res[lang] = None if out is None else any(
                all(c[i] in inv[i] for i in range(len(C))) and ok(tuple(inv[i][c[i]] for i in range(len(C)))) for c in out)
        return res
    return {"all": ask(cells), "leave": ask([c for c in cells if c[0] != 2]), "ctrl": ask(cells[:2] + [(3, 1, 1, 1)]),
            "shape_only": ask([cells[0], cells[1]])}


MID = os.path.join(HERE, "corridor_shape_mid.json")


def interp_check(bulk):
    """the interpolation against three exactly computed columns mid-interval (2.0075, 2.015, 2.03m)"""
    raw = json.load(open(MID))
    ex = Bulk({rc: {k: ([float(v) for v in nd[0]], [float(v) for v in nd[1]]) for k, nd in e.items()} for rc, e in raw.items()})
    worst = 0.0
    for i, r in enumerate(ex.rv):
        for Yv in (0.0, 0.4, 0.8):
            e, a = ex.col(i, Yv), bulk.at(r, Yv)
            worst = max(worst, max(abs(a[X][0] / e[X][0] - 1) for X in "ABC"))
    return worst


def compute(full=False):
    ks = curvature_exprs()
    bulk = Bulk(load_bank())
    runs = {(d, m, s): marginal(ks, bulk, d, m, s) for d in (0.25, 1.0) for m in ((0.0, 0.01) if full else (0.0,))
            for s in ((0.0, 0.3, -0.3) if full else (0.0,))}
    const = []
    for i, rc in enumerate(bulk.rs[:20]):
        g = bulk.col(i, 0.5)
        const.append(stresses(ks, g, 0.0, 0.0))
    gaps = {d0: rim_gap(ks, bulk, d0) for d0 in (0.25, 1.0)}
    return {"ks": ks, "runs": runs, "const": const, "cy": cypher_run(), "gaps": gaps, "rim_cy": rim_cypher(),
            "interp": interp_check(bulk)}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    ks = d["ks"]
    a = (1.0, 2.0, 3.0, 0.4, 0.6, 0.9, 0.1, 0.2, 0.3, 0.0, 0.0)
    add("S1 at Y const the curvature reduces to k = -(1/2) d_y ln g (normal into the slab): k_t = -A_y/(2A), k_r = -B_y/(2B)",
        abs(ks["kt"](*a) + 0.4 / 2) < 1e-12 and abs(ks["kr"](*a) + 0.6 / 4) < 1e-12)
    a2 = a[:-1] + (1.0,)
    add("S1 Y'' enters k_r and not k_t", abs(ks["kt"](*a2) - ks["kt"](*a)) < 1e-12 and abs(ks["kr"](*a2) - ks["kr"](*a)) > 1e-3)
    c = d["const"]
    add("S3 constant depth 0.5m: radial null energy < 0 at every sampled radius, tangential and energy > 0 (P2-FULL)",
        all(x[1] < 0 for x in c[1:]) and all(x[2] > 0 and x[0] > 0 for x in c))
    add("S0 the interpolation between banked columns is within 1e-4 of three exactly computed columns mid-interval "
        "(2.0075, 2.015, 2.03m); the first version's (in r, unscaled) put g_rr 8% low there", d["interp"] < 1e-4)
    runs = d["runs"]
    add("S3 the marginal corridor (radial held at 0) meets our plane at r = 3.1-3.8m, beyond r_b = 3.01m, with energy "
        "> 0 throughout", all(v["rim"] is not None and 3.1 <= v["rim"] <= 3.8 for v in runs.values())
        and all(min(x[3] for x in v["rows"]) > 0 for v in runs.values()))
    add("S3 its tangential null energy is never negative, all the way to the rim",
        all(not any(x[5] < 0 for x in v["rows"]) for v in runs.values()))
    cy = d["cy"]
    add("S4 cypher: the target (both directions kept, energy positive, a whole surface) is data -- the marginal corridor "
        "-- admitted by all five; left out, statistics refuses again", all(cy["all"].values())
        and cy["leave4"]["statistics"] is False)
    gp = d["gaps"]
    add("S5 at margin 0 no tangential gap remains (the 0.02-0.13 (m/ell) E of the first version was the interpolation's)",
        all(abs(v["gap_over_E_times_ell_over_m"]) < 1e-9 for v in gp.values()))
    rc_ = d["rim_cy"]
    add("S6 rim cypher: the shape alone now closes -- positive, sufficient, compatible -- so the README's cell is not "
        "needed (left out, every language still admits); control: a ring cell seated admitted by all five",
        all(rc_["all"].values()) and all(rc_["leave"].values()) and all(rc_["shape_only"].values()) and all(rc_["ctrl"].values()))
    return res


MUTANTS = {"hermite_r": "the first version's interpolation (in r, unscaled)", "normal_out": "the corridor's normal pointing away from its plane", "drop_curvature": "Y'' dropped (no design)",
           "old_tangential": "the marginal corridor's tangential entered as the first version had it (negative)"}


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
        print("  mutant %-15s %-52s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--regenerate" in sys.argv:
        json.dump(regenerate(), open(BANK, "w"))
        print("wrote", BANK)
    elif "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    else:
        d = compute(full=True)
        for key, v in d["runs"].items():
            neg = [x[0] for x in v["rows"] if x[5] < 0]
            print("start depth %.2f margin %.3f slope %+.1f: rim r = %s; min energy %+.3e; tangential < 0 from r = %s" %
                  (key[0], key[1], key[2], ("%.3f" % v["rim"]) if v["rim"] else "none", min(x[3] for x in v["rows"]),
                   ("%.3f" % neg[0]) if neg else "never"))
        print("cypher:", d["cy"])
