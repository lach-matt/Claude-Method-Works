#!/usr/bin/env python3
"""two_sided.py -- item 212: the corridor's sheet with bulk on both sides ("the bulk is everything everywhere all at once";
"what is it's just Z's reflection creating the appearance of negative null energy").  Computed (sympy, and corridor_shape's
own curvature), deduced where marked; each result checked a second way inside this file; seated under 206; 2026-10-10.

  T1 (computed, sympy; any static metric -A dt^2 + B dr^2 + C dOmega^2 + dy^2, any Y(r)) ONE BULK, smooth across the sheet:
     K computed with the normal into either side satisfies K(-n) = -K(n), so the two-sided Israel stress vanishes
     identically -- Y'' included, the only place a fold's line comes from.  No stress, no line
  T2 (computed, open_mouth.py) the two one-sided readings of one sheet are each other's reflection: every flat-limit stress
     flips (D+ against D-), the fold carries -(2/kappa5^2) t one way and +(2/kappa5^2) t the other, and the two-sided real
     stress is their mean, 0.  So in one bulk the negative line at the rim exists only in the one-sided (mirror)
     construction: M's guess H-Z-REFLECTION holds exactly at flat order -- the negative null energy is the appearance the
     reflection creates, and (Z) needs no partner there.  [T2 restates open_mouth's two readings numerically -- its D- is
     the D+ reading reflected by construction; T1 is the proof]
  T3 (computed, sympy) TWO BULKS meeting as mirror images (203's 'the two planes' own bulks', with 202's same values, matched
     at the same depth -- m1p2_junction J5): K(side 2, its normal) = K(side 1, its normal), so the stress is exactly the
     one-sided reading.  There the reflection is real, and both the corridor's flat-order energy and the joint's negative
     line come with it
  T4 (computed, corridor_shape's curvature with the warp) a sheet whose warp DEcreases away from it on both sides -- the
     local mirror that item 197's L1 forces at a sheet carrying only its tension, as at our plane -- carries
     rho = sigma cos t (1 + sin^2 t/3) > 0, rho + p_r = sigma cos t sin^2 t/3 >= 0, rho + p_theta = 0, and this part does
     not depend on Y'': no line at a fold.  The warp's reflection is real and creates no negative null energy
  T5 (cypher, 196; audited per 211) the four computed configurations over (flat_mirror, warp_mirror, energy, joint_negative,
     z_kept): M's cell from 212 with 203 -- no flat-order reflection, the corridor's energy positive, no negative at the
     joint, (Z) kept -- is exactly the configuration of T1 with T4.  Without it entered, statistics refuses that cell, and
     the refusal is forced (no computed cell pairs flat_mirror 0 with energy 1), and the index carries two redundant pairs
     (energy with joint_negative, flat_mirror with z_kept -- index_audit), so its verdicts are forced either way: the
     cypher adds nothing beyond T1-T4
So, on the board's reading H-CORRIDOR-IS-OUR-BRANE (the corridor's sheet is our plane's kind of sheet -- smooth at flat
order, mirrored only at warp order, as our plane is: open_mouth O1, K = 0 at flat order, sigma from the warp's kink), all
three of M's statements hold together: the bulk is one bulk at flat order (212, M-BULK-EVERYWHERE); the negative line at
the rim is the reflection's appearance and (Z) holds at the rim with no partner (212, H-Z-REFLECTION); and the corridor
carries positive energy, its warp-order tension, where the two bulks meet (203).  The other reading -- the two bulks as
flat-order mirror images (T3) -- keeps 203's energy at flat order but makes the joint's negative real.
What this does not show: no bulk has been computed in which the warp's kink follows our plane into the corridor (the bank
puts it at y = 0), so H-CORRIDOR-IS-OUR-BRANE is a reading on the sheet's own geometry, not a solved bulk; 203's equality
of the corridor's energy with the README's E is not computed; flat limit and thin sheets throughout.
Imports corridor_shape.py, open_mouth.py, index_audit.py and tools/cypher.py by path.  Stdlib + sympy.
python3 two_sided.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
MUT = {}
_C = {}
M212 = ("the bulk is everything everywhere all at once. Our universe is a cell in the bulk index.",
        "what is it's just Z's reflection creating the appearance of negative null energy.")


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


# ================================================================================================================ T1
def t1():
    """two-sided K for y = Y(r) in -A dt^2 + B dr^2 + C dOmega^2 + dy^2, A, B, C arbitrary functions of (r, y)"""
    import sympy as sp
    t, r, th, ph, y = sp.symbols("t r theta phi y", real=True)
    Y = sp.Function("Y")(r)
    Af, Bf, Cf = [sp.Function(n)(r, y) for n in "ABC"]
    X = [t, r, th, ph, y]
    g = sp.diag(-Af, Bf, Cf, Cf * sp.sin(th) ** 2, 1)
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(5)) / 2
             for c in range(5)] for b in range(5)] for a in range(5)]
    emb, U = [t, r, th, ph, Y], [t, r, th, ph]
    E = [[sp.diff(emb[m], U[a]) for m in range(5)] for a in range(4)]

    def kmix(sign):
        nl = sign * sp.Matrix([0, -sp.diff(Y, r), 0, 0, 1])
        nl = nl / sp.sqrt((nl.T * gi * nl)[0])
        sub = lambda e: e.subs(y, Y)
        K = sp.zeros(4)
        for a in range(4):
            for b in range(4):
                K[a, b] = -sub(sum(nl[m] * (sp.diff(emb[m], U[a], U[b]) + sum(Gam[m][n][q] * E[a][n] * E[b][q]
                                                                                for n in range(5) for q in range(5)))
                                   for m in range(5)))
        h = sp.Matrix(4, 4, lambda a, b: sub(sum(g[m, n] * E[a][m] * E[b][n] for m in range(5) for n in range(5))))
        return h.inv() * K
    Kp, Km = kmix(1), kmix(-1 if not MUT.get("same_normal") else 1)
    S = -(Kp - sp.eye(4) * Kp.trace()) - (Km - sp.eye(4) * Km.trace())
    Y2 = sp.Derivative(Y, (r, 2))
    return {"antisym": sp.simplify(Kp + Km) == sp.zeros(4), "S_zero": sp.simplify(S) == sp.zeros(4),
            "Y2_only_in_Krr": (not Kp[0, 0].has(Y2)) and (not Kp[2, 2].has(Y2)) and Kp[1, 1].has(Y2)}


# ================================================================================================================ T2
def t2():
    om = _load(os.path.join(HERE, "open_mouth.py"), "ts_open_mouth")
    out = []
    for d, s in om.FOLDS:
        v = om.member(d, s)
        p, m = om.fold(v["r"], -v["Y1"], +1), om.fold(v["r"], -v["Y1"], -1)
        out.append({"theta": p["theta"], "plus": p["rho"], "minus": m["rho"], "mean": (p["rho"] + m["rho"]) / 2})
    return out


# ================================================================================================================ T3
def t3():
    import sympy as sp
    y, yj = sp.symbols("y y_j", real=True)
    fs = [sp.Function(n) for n in "ABC"]
    K1 = [-sp.diff(sp.log(F(y)), y) / 2 for F in fs]                                 # side 1 (y < y_j), normal -d/dy
    K2m = [sp.diff(sp.log(F(2 * yj - y)), y) / 2 for F in fs]                        # side 2 the mirror of side 1, normal +d/dy
    K2s = [sp.diff(sp.log(F(y)), y) / 2 for F in fs]                                 # side 2 the same bulk continued
    at = lambda e: sp.simplify(e.subs(y, yj).doit())
    mirror_equal = all(sp.simplify(at(a) - at(b)) == 0 for a, b in zip(K1, K2m))
    smooth_opposite = all(sp.simplify(at(a) + at(b)) == 0 for a, b in zip(K1, K2s))
    return {"mirror_equal": mirror_equal, "smooth_opposite": smooth_opposite}


# ================================================================================================================ T4
def t4():
    cs = _load(os.path.join(HERE, "corridor_shape.py"), "ts_cs")
    ks = cs.curvature_exprs()
    side = -1 if not MUT.get("facing") else 1                                          # away = -corridor_shape's normal

    def st(w, t, Y2):
        r = 4.0
        a = (1.0, 1.0, r * r, w, w, w * r * r, 0.0, 0.0, 2 * r, math.tan(t), Y2)
        kt, kr, kth = side * ks["kt"](*a), side * ks["kr"](*a), side * ks["kth"](*a)
        return -(kr + 2 * kth), kt - kr, kt - kth
    worst, line_free, nec = 0.0, True, True
    for ell in (10.0, 100.0):
        sig = 3 / ell
        for t in (0.1, 0.3, 0.6, 1.0):
            parts = []
            for Y2 in (0.0, 5.0, -40.0):
                w1, w0 = st(-2 / ell, t, Y2), st(0.0, t, Y2)
                parts.append(tuple(a - b for a, b in zip(w1, w0)))
            rw, aw, bw = parts[0]
            ref = (sig * math.cos(t) * (1 + math.sin(t) ** 2 / 3), sig * math.cos(t) * math.sin(t) ** 2 / 3, 0.0)
            worst = max(worst, abs(rw - ref[0]) / ref[0], abs(aw - ref[1]) / sig, abs(bw - ref[2]) / sig)
            line_free = line_free and all(abs(parts[0][i] - parts[k][i]) < 1e-12 for k in (1, 2) for i in range(3))
            nec = nec and rw > 0 and aw >= -1e-15 and abs(bw) < 1e-12
    return {"worst": worst, "line_free": line_free, "nec": nec}


# ================================================================================================================ T5
def t5():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "ts_cypher")
    ia = _load(os.path.join(HERE, "index_audit.py"), "ts_index_audit")
    coords = ["flat_mirror", "warp_mirror", "energy", "joint_negative", "z_kept"]
    cells = {"one_bulk": (0, 0, 0, 0, 1),               # T1, no warp kink on the sheet: nothing there
             "two_mirror_Dplus": (1, 0, 1, 1, 0),       # T3 with the seated corridor's side (open_mouth O5)
             "two_mirror_Dminus": (1, 0, 0, 0, 0),      # T3 with the other side (open_mouth O4, O6; TS grazing)
             "brane": (0, 1, 1, 0, 1)}                  # T1 with T4: our plane's kind of sheet
    target = (0, 1, 1, 0, 1) if not MUT.get("target_mirror") else (1, 1, 1, 0, 1)

    def run(cl):
        cl = sorted(set(cl))
        ix = cy.Index("two_sided", coords, [list(c) for c in cl])
        inv = [{v: k for k, v in ix.code[i].items()} for i in range(len(coords))]
        res = {}
        for lang in ("order", "algebra", "geometry", "information"):
            out, _ = cy.ADMISSION[lang][0](ix, {})
            dec = set() if out is None else {tuple(inv[i][c[i]] for i in range(len(coords))) for c in out}
            res[lang] = target in dec
        out, _ = cy.op_statistics(ix, {"statistics_order": 2})
        dec = {tuple(inv[i][c[i]] for i in range(len(coords))) for c in out}
        res["statistics"] = target in dec
        return res, ia.audit_index(coords, cl)
    full, audit_full = run(list(cells.values()))
    without, audit_wo = run([c for k, c in cells.items() if k != "brane"])
    wo = [c for k, c in cells.items() if k != "brane"]
    unpaired = not any(c[0] == 0 and c[2] == 1 for c in wo)
    return {"target_is_brane": target == cells["brane"], "full": full, "without": without, "unpaired": unpaired,
            "audit_full": audit_full, "audit_wo": audit_wo}


def compute():
    return {"t1": t1(), "t2": t2(), "t3": t3(), "t4": t4(), "t5": t5()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rulings = open(os.path.join(os.path.dirname(HERE), "M-RULINGS-2026-10-03.md")).read().replace("\n    ", " ")
    add("T0 M's 212 verbatim in the rulings file", all(w in rulings for w in M212))
    a = d["t1"]
    add("T1 one bulk smooth across the sheet: K(-n) = -K(n) for any static metric and any Y(r); the two-sided stress is "
        "identically 0, Y'' (which enters K^r_r only) included -- no stress, no line", a["antisym"] and a["S_zero"]
        and a["Y2_only_in_Krr"])
    b = d["t2"]
    add("T2 the one-sided readings are reflections: the fold's line is -t one way and +t the other (1%), their mean 0 -- "
        "the negative at the rim is the reflection's appearance in one bulk",
        all(abs(x["plus"] + x["theta"]) < 0.01 * x["theta"] and abs(x["minus"] - x["theta"]) < 0.01 * x["theta"]
            and abs(x["mean"]) < 1e-12 for x in b))
    c = d["t3"]
    add("T3 two bulks meeting as mirror images: K(side 2) = K(side 1), so the stress is the one-sided reading (the "
        "reflection real); one bulk continued: K(side 2) = -K(side 1)", c["mirror_equal"] and c["smooth_opposite"])
    e = d["t4"]
    add("T4 warp mirror (warp decreasing away on both sides, L1's local mirror): rho = sigma cos t (1 + sin^2 t/3) > 0, "
        "rho + p_r = sigma cos t sin^2 t/3 >= 0, rho + p_theta = 0, independent of Y'' -- no negative null energy, no line",
        e["worst"] < 1e-9 and e["line_free"] and e["nec"])
    f = d["t5"]
    add("T5 cypher: M's 212-with-203 cell is the brane configuration (T1 with T4), admitted by all five by construction; "
        "without it statistics refuses, forced (no computed cell has flat_mirror 0 with energy 1)",
        f["target_is_brane"] and all(f["full"].values()) and not f["without"]["statistics"] and f["unpaired"])
    return res


MUTANTS = {"same_normal": "both sides' K computed with the same normal",
           "facing": "the warp part taken in the facing orientation (corridor_shape's normal)",
           "target_mirror": "M's cell entered with a flat-order reflection"}


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
        print("  mutant %-14s %-70s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("two_sided.py -- the corridor's sheet with bulk on both sides (item 212)\n")
    print("T1", d["t1"])
    for x in d["t2"]:
        print("T2 t %.5f  D+ %+.5f  D- %+.5f  mean %+.1e" % (x["theta"], x["plus"], x["minus"], x["mean"]))
    print("T3", d["t3"])
    print("T4", d["t4"])
    f = d["t5"]
    print("T5 with the brane cell:", f["full"], " without:", f["without"], " audit:", {k: f["audit_wo"][k] for k in ("keys", "onehot")})


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
