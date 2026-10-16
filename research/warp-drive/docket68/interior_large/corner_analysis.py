"""corner_analysis.py -- item 406: the corner where the far end s = 1 meets the brane x = 1, analysed exactly.

M, 406, on the far end's line-by-line exponents changing with x: "do it" -- the corner analysis.  The record's static
solution (solver_fw.py, FW's RSII large hole) does not converge in its DeTurck vector (item 405); its far end is clean
away from the brane (every field goes as t = 1 - s, converged) and erratic near it.  Here the corner is blown up:
  t = 1 - s,  eta = (1 - x^2)/t,  w = 1 + eta = (2 - s - x^2)/(1 - s);
the record's five equations and four brane rows are linearised about the reference metric (T = S = A = B = 1, F = 0,
the far end's own data) -- exactly, from gen_eqs_fw.py's expressions, cached in CORNER-LIN.json (--derive rebuilds it,
about 20 minutes) -- and dX_f = t^lam Phi_f(w) is put in.  Found (selftest C1-C7):
  - at leading order in t the corner is an ordinary differential system in w alone, independent of lam (g^ss goes as
    t^4 against g^xx as t^2, so the s-derivatives enter one order later);
  - it is of Euler type: T, S, A: -w^2 Phi''/2 + 3 w Phi'/2 + (Phi_T + 2 Phi_S + Phi_A); B: the same with 4 Phi_B;
    F: -w^2 Phi''/4 + 3 w Phi'/4 + 5 Phi_F/4;
  - its exponents (Phi = w^m) are exact: 2 +- 2 sqrt 3 for B and for Sigma = T + 2S + A, {0, 4} for the differences
    T - S and T - A, {-1, 5} for F -- 2 +- 2 sqrt 3 irrational;
  - the reference's own residual forces it at t^3 (T, A: 3w^2 - 15w/2 + 4; S, B: 4 - 3w), with particular solutions
    Phi_B = -1 + 6w/11, Sigma = -4 + 42w/11 - w^2, T - S = 3w - 3w^2/2;
  - the brane rows at w = 1: Phi_T' = Phi_S' = Phi_A' = -Phi_B, F = 0; the xi^x row enters only at the next order;
    they tie the two admissible singular amplitudes, sigma_ = 2 b_/(sqrt 3 - 1);
  - the record's own solution follows the analytic particular solution at this order: on the brane (B - 1)/t^3 ->
    -5/11 + b_, and the static solutions give -0.453 against -5/11 = -0.4545 (|b_| <~ 0.01).
So the irrational modes are admitted at the corner but not excited at order t^3; the non-analytic term must come at
the next order, where the lam-dependent s-derivatives act on the t^3 solution, the xi^x row enters, and the exponent
4 of the differences can resonate (w^4 log w).

python3 corner_analysis.py                 -- the analysis, printed
python3 corner_analysis.py --selftest | --mutants | --derive
"""
import sys, json, os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
NAMES = ["T", "S", "A", "B", "F"]
TAGS = ["", "_s", "_x", "_ss", "_xx", "_sx"]
s, x = sp.symbols("s x", real=True)
t, eta, w = sp.symbols("t eta w", positive=True)
lam, m = sp.symbols("lam m")


def derive(path=os.path.join(HERE, "CORNER-LIN.json")):
    """the record's equations and brane rows linearised about the reference metric, exactly (slow)"""
    sys.path.insert(0, HERE)
    import core_fw as C
    bg = {sp.Symbol(n + tg): ((0 if n == "F" else 1) if tg == "" else 0) for n in C.names for tg in C.tags}
    bg[C.bt] = 1
    out = {"J": {}, "R0": {}, "JB": {}, "B0": {}}
    for lab, exprs, jkey, rkey in (("eq", C.RES, "J", "R0"), ("row", C.BCS, "JB", "B0")):
        for e, E in enumerate(exprs):
            out[rkey][str(e)] = str(sp.simplify(E.subs(bg)))
            for v in C.VARS:
                d = sp.diff(E, v)
                if d != 0:
                    dv = sp.simplify(d.subs(bg))
                    if dv != 0:
                        out[jkey]["%d|%s" % (e, v)] = str(dv)
    json.dump(out, open(path, "w"), indent=0, sort_keys=True)
    return out


def load():
    return json.load(open(os.path.join(HERE, "CORNER-LIN.json")))


def chain(p0, p1, p2):
    """d_tag [t^lam Phi(eta)] / t^lam, by hand: t = 1 - s, eta = (1 - x^2)/t, x = sqrt(1 - eta t)"""
    X_ = sp.sqrt(1 - eta * t)
    ds = (-lam * p0 + eta * p1) / t if "chain" not in MUT else -lam * p0 / t
    return {"": p0, "_s": ds, "_x": -2 * X_ * p1 / t,
            "_ss": (lam * (lam - 1) * p0 + 2 * (1 - lam) * eta * p1 + eta ** 2 * p2) / t ** 2,
            "_xx": (4 * X_ ** 2 * p2 - 2 * t * p1) / t ** 2, "_sx": -2 * X_ * ((1 - lam) * p1 + eta * p2) / t ** 2}


def q(f):
    return sp.symbols("q0_%s q1_%s q2_%s" % (f, f, f))


NS = {"s": s, "x": x, "bt": sp.Integer(1)}


def leading(L):
    """each equation's leading order in t at fixed eta, in the symbols q0_f, q1_f, q2_f (Phi, Phi', Phi''),
    rewritten in w = 1 + eta; and the reference's residual's leading term"""
    ops, forc = {}, {}
    for e in range(5):
        tot = 0
        for f in NAMES:
            D = chain(*q(f))
            for tg in TAGS:
                k = "%d|%s" % (e, f + tg)
                if k in L["J"]:
                    c = sp.sympify(L["J"][k], locals=NS).subs({s: 1 - t}).subs({x: sp.sqrt(1 - eta * t)})
                    if "nocoupling" in MUT and tg == "" and f != NAMES[e]:
                        continue
                    tot += c * D[tg]
        lead = sp.series(sp.simplify(tot), t, 0, 1).removeO()
        ops[e] = sp.expand(lead.subs(eta, w - 1))
        r0 = sp.sympify(L["R0"][str(e)], locals=NS).subs({s: 1 - t}).subs({x: sp.sqrt(1 - eta * t)})
        sgn = -1 if "forcesign" in MUT else 1
        forc[e] = sp.expand(sgn * sp.series(sp.simplify(r0), t, 0, 4).removeO().subs(eta, w - 1) / t ** 3)
    return ops, forc


def apply_op(op, Phi):
    """the leading operator of one equation acting on functions Phi_f(w) given as a dict"""
    rep = {}
    for f in NAMES:
        q0, q1, q2 = q(f)
        rep[q0] = Phi[f]; rep[q1] = sp.diff(Phi[f], w); rep[q2] = sp.diff(Phi[f], w, 2)
    return sp.simplify(op.subs(rep))


def exponents(ops):
    """Phi = w^m in the decoupled combinations: B, Sigma = T + 2S + A, T - S, T - A, F"""
    z = {f: 0 for f in NAMES}
    out = {}
    combos = {"B": {"B": 1}, "Sigma": {"T": 1, "S": 1, "A": 1}, "T-S": {"T": 1, "S": -1}, "T-A": {"T": 1, "A": -1},
              "F": {"F": 1}}
    weights = {"B": {3: 1}, "Sigma": {0: 1, 1: 2, 2: 1}, "T-S": {0: 1, 1: -1}, "T-A": {0: 1, 2: -1}, "F": {4: 1}}
    for name, cmb in combos.items():
        Phi = dict(z); Phi.update({f: c * w ** m for f, c in cmb.items()})
        expr = sum(cw * apply_op(ops[e], Phi) for e, cw in weights[name].items())
        poly = sp.simplify(expr / w ** m)
        out[name] = (sp.factor(poly), sorted(sp.solve(poly, m), key=lambda r: float(r)))
    return out


def particular():
    return {"B": -1 + sp.Rational(6, 11) * w, "Sigma": -4 + sp.Rational(42, 11) * w - w ** 2,
            "T-S": 3 * w - sp.Rational(3, 2) * w ** 2, "T-A": sp.Integer(0)}


def fields_from(P):
    """T, S, A from Sigma, T - S, T - A"""
    Sg, dTS, dTA = P["Sigma"], P["T-S"], P["T-A"]
    T = (Sg + 2 * dTS + dTA) / 4
    return {"T": T, "S": T - dTS, "A": T - dTA, "B": P["B"], "F": sp.Integer(0)}


def brane_rows(L):
    out = {}
    for e in range(4):
        tot = 0
        for f in NAMES:
            D = chain(*q(f))
            for tg in TAGS:
                k = "%d|%s" % (e, f + tg)
                if k in L["JB"]:
                    c = sp.sympify(L["JB"][k], locals=NS).subs({s: 1 - t}).subs({x: sp.sqrt(1 - eta * t)})
                    tot += c * D[tg]
        out[e] = sp.simplify(sp.series(sp.simplify(tot.subs(eta, 0)), t, 0, 1).removeO())
        b0 = sp.sympify(L["B0"][str(e)], locals=NS).subs({s: 1 - t}).subs({x: sp.sqrt(1 - eta * t)}).subs(eta, 0)
        out[(e, "ref")] = sp.simplify(b0)
    return out


def static_brane(npy=os.path.join(HERE, "fw_bt1_24_24.npy"), N=24):
    """(B - 1)/t^3 on the brane at the static solution's nodes nearest s = 1"""
    import numpy as np
    sys.path.insert(0, HERE)
    import core_fw as C
    U = np.load(npy); n = (N + 1) ** 2; sn = C.radau01(N)
    Bm = U[3 * n:4 * n].reshape(N + 1, N + 1); tt = 1 - sn[-5:-1]
    return tt, (Bm[-5:-1, -1] - 1) / tt ** 3


def selftest(quiet=False):
    ok = []
    # C1: the chain rule against direct differentiation, a concrete Phi
    zz = sp.Symbol("zz"); Ph = zz ** 3 + sp.sin(zz)
    X = (1 - s) ** lam * Ph.subs(zz, (1 - x ** 2) / (1 - s))
    pt = {s: sp.Rational(3, 10), x: sp.Rational(7, 10), lam: sp.Rational(5, 4)}
    tv = 1 - pt[s]; ev = (1 - pt[x] ** 2) / tv
    pv = [sp.diff(Ph, zz, k).subs(zz, ev) for k in range(3)]
    D = chain(*pv); D = {k: v.subs({t: tv, eta: ev, lam: pt[lam]}) for k, v in D.items()}
    direct = {"_s": sp.diff(X, s), "_x": sp.diff(X, x), "_ss": sp.diff(X, s, 2), "_xx": sp.diff(X, x, 2),
              "_sx": sp.diff(X, s, x)}
    e1 = max(abs(sp.N(direct[k].subs(pt) / tv ** pt[lam] - D[k], 30)) for k in direct)
    ok.append(("C1 the chain rule in (t, eta) is exact (%.1e)" % e1, e1 < 1e-25))
    L = load(); ops, forc = leading(L)
    # C2: the leading operators, Euler form
    q0 = {f: q(f) for f in NAMES}
    want = {}
    for e, f in enumerate(["T", "S", "A"]):
        a, b, c = q0[f]
        want[e] = -w ** 2 * c / 2 + 3 * w * b / 2 + q0["T"][0] + 2 * q0["S"][0] + q0["A"][0]
    a, b, c = q0["B"]; want[3] = -w ** 2 * c / 2 + 3 * w * b / 2 + 4 * a
    a, b, c = q0["F"]; want[4] = -w ** 2 * c / 4 + 3 * w * b / 4 + 5 * a / 4
    e2 = all(sp.simplify(ops[e] - want[e]) == 0 for e in range(5)) and all(lam not in ops[e].free_symbols
                                                                       for e in range(5))
    ok.append(("C2 at leading order the corner is the Euler system in w, independent of lam", e2))
    # C3: the exponents
    ex = exponents(ops)
    r3 = sp.sqrt(3)
    e3 = (ex["B"][1] == [2 - 2 * r3, 2 + 2 * r3] and ex["Sigma"][1] == [2 - 2 * r3, 2 + 2 * r3]
          and ex["T-S"][1] == [0, 4] and ex["T-A"][1] == [0, 4] and ex["F"][1] == [-1, 5])
    ok.append(("C3 exponents: 2 +- 2 sqrt 3 (B, Sigma), {0, 4} (differences), {-1, 5} (F)", e3))
    # C4: the particular solutions solve the forced system exactly
    Phi = fields_from(particular())
    res = [sp.simplify(apply_op(ops[e], Phi) + forc[e]) for e in range(5)]
    ok.append(("C4 the order-t^3 particular solutions solve the forced corner system exactly", all(r == 0 for r in res)))
    # C5: the brane rows at w = 1
    br = brane_rows(L)
    want_b = [-q0[f][1] / 2 - q0["B"][0] / 2 for f in ("T", "S", "A")]
    e5 = (all(sp.simplify(br[e] - want_b[e]) == 0 for e in range(3)) and sp.simplify(br[3]) == 0
          and all(br[(e, "ref")] == 0 for e in range(4)))
    ok.append(("C5 brane rows at the corner: Phi_T' = Phi_S' = Phi_A' = -Phi_B; xi^x next order; reference exact", e5))
    # C6: the rows tie the singular amplitudes: sigma_ = 2 b_/(sqrt 3 - 1)
    bm, sm = sp.symbols("b_m s_m")
    P = particular(); mm = 2 - 2 * r3
    Sg = P["Sigma"] + sm * w ** mm; Bf = P["B"] + bm * w ** mm
    cond = sp.simplify((sp.diff(Sg, w) + 4 * Bf).subs(w, 1))               # Sigma'(1) = 4 Phi_T'(1) = -4 Phi_B(1)
    sol = sp.solve(cond, sm)
    e6 = len(sol) == 1 and sp.simplify(sol[0] - 2 * bm / (r3 - 1)) == 0
    ok.append(("C6 the brane rows give sigma_ = 2 b_/(sqrt 3 - 1)", e6))
    # C7: the record's solution follows the particular solution on the brane: (B - 1)/t^3 -> -5/11 + b_
    try:
        tt, r = static_brane(); val = float(r[-2]); e7 = abs(val + 5 / 11) < 0.02
        lab = "%.4f" % val
    except FileNotFoundError:
        e7, lab = False, "no static solution (run solver_fw.py 1 24 24)"
    ok.append(("C7 static solution N = 24: (B - 1)/t^3 on the brane %s against -5/11 = -0.4545" % lab, e7))
    if not quiet:
        for name, good in ok:
            print("%s  %s" % ("PASS" if good else "FAIL", name))
    return all(g for _, g in ok), ok


def mutants():
    caught = []
    for mname, what in (("nocoupling", "the T-S-A coupling dropped"), ("forcesign", "the forcing's sign flipped"),
                        ("chain", "the chain rule's eta term dropped from d_s")):
        MUT.clear(); MUT.add(mname)
        good, ok = selftest(quiet=True)
        caught.append((what, not good, [n.split()[0] for n, g in ok if not g]))
    MUT.clear()
    for what, c, fails in caught:
        print("%s  %-45s failed: %s" % ("caught" if c else "MISSED", what, ", ".join(fails) or "none"))
    return all(c for _, c, _ in caught)


def main():
    L = load(); ops, forc = leading(L)
    print("leading operators in w = (2 - s - x^2)/(1 - s):")
    for e in range(5):
        print("  %s: %s" % (NAMES[e], ops[e]))
    print("forcing at t^3:", {NAMES[e]: forc[e] for e in range(5)})
    for k, (poly, roots) in exponents(ops).items():
        print("  exponents %-6s: %s = 0  ->  %s" % (k, poly, roots))
    print("particular solutions:", particular())
    br = brane_rows(L)
    print("brane rows at w = 1:", {k: v for k, v in br.items() if not isinstance(k, tuple)})
    tt, r = static_brane()
    print("static N = 24, (B - 1)/t^3 on the brane at t = %s: %s (against -5/11 = %.6f)" % (
        " ".join("%.2e" % v for v in tt), " ".join("%.4f" % v for v in r), -5 / 11))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        good, _ = selftest(); print("selftest: %s" % ("PASS" if good else "FAIL")); sys.exit(0 if good else 1)
    elif "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    elif "--derive" in sys.argv:
        derive()
    else:
        main()
