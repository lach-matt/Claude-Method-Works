#!/usr/bin/env python3
"""forming_rim.py -- the rim while the corridor forms (198 (a)): can the README's inflow, at a rim that moves, supply
both the force balance and the null energy?  Put to the cypher (computed, deduced; flat limit; thin sheets; not
verified by a separate session; not seated; 2026-10-10).

rim_readme.py left the static finite-ell rim with no closing arrangement on M's guess 198, and named what was left: the
forming phase, where the rim is not static and the README is mid-inflow (198 (a): "the README comes in while the
corridor forms, with no partner, the size growing as it comes in (94) and fixed once the whole README is in").

The geometry at the rim is not pinned by anything the board has computed (Wall C, the corridor's global bulk, is open).
R7 fixed only the tension count -- outside sigma, inside ours sigma and position 2's sigma, corridor -sigma (R5) -- so
every arrangement consistent with that count is run, in a cross-section with the rim at the origin:
  A  R7's own check: our inside sheet and position 2's both along the plane, the corridor tilted by theta
  B  our plane flat through the rim (corridor_shape.py's frame, the corridor a graph y = Y(r) over it), the corridor at
     theta, position 2's sheet its mirror across the corridor at 2 theta ("depth Y below each plane")
  C  mirror-symmetric about the corridor (202's symmetry applied at the rim): the outside sheet and the corridor on the
     mirror line, our sheet and position 2's at +-theta.  Our plane then kinks by theta at the rim
  F1 (computed, sympy) a pure-tension sheet's stress -sigma eta is invariant under boosts along the sheet, so a rim
     sliding along our plane at any speed meets the same planes in its own rest frame: rim motion alone changes no
     balance, and each case is read in the rim's rest frame (the README's flux Doppler-shifted, still >= 0)
  F2 (computed) a flow arriving along sheet i and leaving along sheet j with momentum flux Pi pushes the rim by
     -Pi (e_i + e_j): to the rim it is a pressure Pi added to both sheets.  The NEC on the flow gives Pi >= 0 (a null or
     timelike README carries Pi = (rho + p) gamma^2 v^2, or Pi = Phi)
  F3 (computed, sympy) the steep forming rim (theta in (0, pi)), README arriving from outside (it falls in from large r):
     A  into the corridor: balance needs Pi = -sigma at every theta -- a negative flux, or a README that is itself a
        membrane of net tension sigma; onto either plane sheet: no bend, no force, theta = 0 only
     B  no route balances at any theta in (0, pi), whatever Pi's sign (the cross product is -k sigma (cos th - 1) sin th)
     C  onto both plane sheets, split evenly: balance at EVERY theta with Pi = 2 sigma exactly -- the README's pressure
        cancels the inside sheets' tension and turns the outside sheet's to -sigma, head-on against the corridor's;
        into the corridor (on the mirror line): no bend, theta = 0 only; onto one plane sheet alone: none
  F4 (computed, sympy) null energy the README supplies: null dust Phi l l gives T(l,l) = 0 along its own rays, 4 Phi along
     the opposite radial rays, Phi along tangential ones; timelike dust gives rho (u.k)^2 > 0 along every null k.  So a
     null README never covers a deficit along its own infall rays; a timelike one can, by magnitude
  F5 (deduced, computed) the hold: on 198 (a) the README is all in once the corridor has formed, Pi = 0 at the rim, and
     every geometry balances only at theta = 0 -- R7 again, with R8's radial deficit.  Nothing in the forming phase
     carries through the hold
  F6 (ESTIMATE, the board's; uniform spread over r < 2.15m) C's flux is within the README's budget: its mean density
     near the rim is 0.10 (ell/m)^2 sigma (7.3 sigma at ell/m = 8.54), and E feeds Pi = 2 sigma through the rim for at
     most 0.036 (ell/m)^2 m/c (2.6 m/c at ell/m = 8.54; far longer for a real README, ell/m ~ 7e22)
  F7 (cypher) the static (rim_readme R9) and forming arrangements as cells; NEC coordinates take 2 = not computed
     (the corridor's null energy with the README's flux at the rim needs the self-consistent bulk re-solve).  Target A,
     a rim that closes through the hold: refused by statistics under every coding tried.  Target B, closing while the
     README flows: refused by statistics with the uncomputed cells left unknown; with them set favourable (control),
     statistics admits the timelike-README cells and still refuses target A
Named readings (the board's): H-DEPTH-LAW-FOLLOWS-R4 -- the corridor's radial null energy near the rim follows the
plane's 4D radial null Ricci along the same direction (R8's sign match, not derived); on it a null README leaves the
corridor's deficit along the README's own infall rays.  Geometries A, B, C are the board's; none is M's.
So: in the forming phase the README's inflow balances the steep rim only in the mirror-symmetric arrangement C, with
its flux onto the two planes tuned to exactly 2 sigma; it cannot supply null energy along its own rays if it is null;
and on 198 (a) nothing of it remains at the rim through the hold.
Imports tools/cypher.py by path.  Stdlib + sympy.  python3 forming_rim.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
MUT = {}
S, TH, PI = sp.symbols("sigma theta Pi", real=True)


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def _v(a):
    return sp.Matrix([sp.cos(a), sp.sin(a)])


# ---------------------------------------------------------------------------------------------------------- F1
def boost():
    v = sp.Symbol("v", real=True)
    g = 1 / sp.sqrt(1 - v**2)
    L = sp.Matrix([[g, g * v], [g * v, g]])
    eta = sp.diag(-1, 1)
    T = -S * eta if not MUT.get("dust_sheet") else S * sp.diag(1, 0)
    return sp.simplify(L * T * L.T - T) == sp.zeros(2, 2)


# ---------------------------------------------------------------------------------------------------------- F2, F3
def geometries():
    p2C = _v(sp.pi + TH) if not MUT.get("no_mirror") else _v(sp.pi)
    return {"A": {"ours": _v(sp.pi), "p2": _v(sp.pi), "corr": _v(sp.pi - TH)},
            "B": {"ours": _v(sp.pi), "p2": _v(sp.pi - 2 * TH), "corr": _v(sp.pi - TH)},
            "C": {"ours": _v(sp.pi - TH), "p2": p2C, "corr": _v(sp.pi)}}


TENS = {"ours": 1, "p2": 1, "corr": -1}                        # in units of sigma; corr -sigma by R5
ROUTES = {"corr": {"corr": 1}, "ours": {"ours": 1}, "p2": {"p2": 1},
          "both": {"ours": sp.Rational(1, 2), "p2": sp.Rational(1, 2)}}


def flux_force(e_in, outs, Pi):
    """momentum in minus momentum out at the rim: arriving along sheet e_in (moving -e_in), leaving along e_j"""
    sgn = 1 if not MUT.get("pi_plus") else -1
    p_in = -e_in * Pi
    p_out = sum((w * Pi * e for e, w in outs), sp.zeros(2, 1))
    return sgn * (p_in - p_out)


def balance(g, route, Pi=PI):
    sh = geometries()[g]
    o = _v(0)
    R = S * o + sum((TENS[k] * S * sh[k] for k in sh), sp.zeros(2, 1))
    F = R + flux_force(o, [(sh[k], w) for k, w in ROUTES[route].items()], Pi)
    return R, F


def solve_route(g, route):
    """theta in (0, pi): 'nobend' (flux exerts no force; theta = 0 only), 'family' (balance at every theta with Pi = ...),
    or the finite roots"""
    R, F = balance(g, route)
    D = sp.simplify(balance(g, route, 1)[1] - R)                  # the flux's force per unit Pi
    if sp.simplify(D.T * D)[0] == 0:
        return {"kind": "nobend"}
    cross = sp.factor(sp.simplify(sp.expand_trig(R[0] * D[1] - R[1] * D[0])))
    if sp.simplify(cross) == 0:
        Pi = sp.simplify(-(R.T * D)[0] / (D.T * D)[0])
        return {"kind": "family", "Pi": Pi}
    roots = sp.solveset(sp.simplify(cross.subs(S, 1)), TH, sp.Interval.open(0, sp.pi))
    return {"kind": "roots", "roots": roots, "cross": cross}


def hold(g):
    """F5: Pi = 0 at the rim (198 (a), the README all in): theta in (0, pi) with the pure tensions balancing"""
    Pi = 0 if not MUT.get("hold_flux") else 2 * S
    R, F = balance(g, "both", Pi)
    F = sp.simplify(F.subs(S, 1))
    sol = sp.solveset(F[0], TH, sp.Interval.open(0, sp.pi)).intersect(
        sp.solveset(F[1], TH, sp.Interval.open(0, sp.pi))) if F[1] != 0 else sp.solveset(F[0], TH, sp.Interval.open(0, sp.pi))
    return sol


# ---------------------------------------------------------------------------------------------------------- F4
def null_energy():
    eta = sp.diag(-1, 1, 1)
    Phi, rho, v, a = sp.symbols("Phi rho v alpha", positive=True)
    l = sp.Matrix([1, -1, 0])                                    # the README's infall direction
    n = sp.Matrix([1, 1, 0])
    kt = sp.Matrix([1, 0, 1])
    lo = eta * l
    Tn = Phi * lo * lo.T
    own = l if not MUT.get("null_own") else n
    q = lambda T, k: sp.simplify((k.T * T * k)[0])
    g = 1 / sp.sqrt(1 - v**2)
    u = g * sp.Matrix([1, -v, 0])
    k = sp.Matrix([1, sp.cos(a), sp.sin(a)])
    uk = sp.simplify((u.T * eta * k)[0])                         # u.k = -gamma (1 + v cos alpha)
    num = sp.simplify(-uk * sp.sqrt(1 - v**2))                    # 1 + v cos alpha; its least value over alpha
    uk_min = sp.simplify(num.subs(sp.cos(a), -1))
    return {"own": q(Tn, own), "opp": q(Tn, n), "tan": q(Tn, kt), "uk": uk, "v": v, "a": a, "uk_min": uk_min,
            "uk_min_expect": 1 - v}


# ---------------------------------------------------------------------------------------------------------- F6
def estimate(lm=8.54, rr=2.15):
    ratio = lm**2 / rr**3                                         # [E / ((4pi/3)(rr m)^3)] / [3 c^4/(4 pi G ell^2)], E = c^4 m/G
    tau = lm**2 / (2 * 3 * rr**2)                                 # E / (2 sigma 4 pi r^2 c) in units of m/c
    return {"ratio": ratio, "coef_ratio": ratio / lm**2, "tau": tau, "coef_tau": tau / lm**2}


# ---------------------------------------------------------------------------------------------------------- F7
C7 = ["arrangement", "balance", "nec_in", "nec_out", "nec_t", "no_partner", "through_hold"]
U = 2                                                            # not computed
CELLS = [(0, 1, 0, 0, 1, 1, 1),    # static, tangent, pure tensions (rim_readme R9)
         (1, 0, 1, 1, 0, 1, 1),    # static, steep, marginal corridor (R9)
         (2, 1, 1, 1, 1, 0, 1),    # static, tangent, README cancelling (set aside on 198)
         (3, 0, U, U, U, 1, 0),    # forming, steep, geometry A or B, README flux Pi >= 0 any route (F3)
         (4, 1, 0, U, 1, 1, 0),    # forming, tangent, null README (F4 + H-DEPTH-LAW-FOLLOWS-R4)
         (5, 1, U, U, 1, 1, 0),    # forming, tangent, timelike README
         (6, 1, 0, U, U, 1, 0),    # forming, steep, geometry C, null README onto both planes, Pi = 2 sigma
         (7, 1, U, U, U, 1, 0),    # forming, steep, geometry C, timelike README, Pi = 2 sigma
         (8, 1, U, U, U, 1, 0)]    # forming, steep, geometry A, README into the corridor with net tension sigma


def _codings(n):
    base = list(range(n))
    out = []
    for k in range(n):
        rot = base[k:] + base[:k]
        out += [rot, rot[::-1]]
    return out


def cypher():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "fr_cypher")
    langs = ("order", "algebra", "geometry", "information", "statistics")
    full = lambda h: all(h[i] == 1 for i in range(1, 7))
    forming = lambda h: all(h[i] == 1 for i in range(1, 6))
    cells = list(CELLS)
    if MUT.get("seat_hold"):
        cells.append((9, 1, 1, 1, 1, 1, 1))

    def ask(cs, test, arr_order, unk_low=False):
        n_arr = sorted({c[0] for c in cs})
        vo = {"arrangement": [n_arr[i] for i in arr_order if i < len(n_arr)] + [a for a in n_arr if a >= len(arr_order)]}
        for name in C7[1:]:
            vo[name] = [x for x in ([U, 0, 1] if unk_low else [0, 1, U]) if x in {c[C7.index(name)] for c in cs}]
        ix = cy.Index("forming_rim", C7, [list(c) for c in cs], value_order=vo)
        inv = [{v: k for k, v in ix.code[i].items()} for i in range(len(C7))]
        res = {}
        for lang in langs:
            out, _ = cy.ADMISSION[lang][0](ix, {})
            if out is None:
                res[lang] = None
                continue
            dec = {tuple(inv[i][c[i]] for i in range(len(C7))) for c in out if all(c[i] in inv[i] for i in range(len(C7)))}
            res[lang] = sorted(h[0] for h in dec if test(h))
        return res

    n = len({c[0] for c in cells})
    runs = {}
    for unk_low in (False, True):
        for order in _codings(n):
            runs[(unk_low, tuple(order))] = {"full": ask(cells, full, order, unk_low),
                                             "forming": ask(cells, forming, order, unk_low)}
    fav = [(c[0],) + tuple(1 if x == U else x for x in c[1:]) for c in cells]     # the arrangement axis is not converted
    control = {"full": ask(fav, full, list(range(n))), "forming": ask(fav, forming, list(range(n)))}
    return {"runs": runs, "control": control}


# ---------------------------------------------------------------------------------------------------------- run
def compute():
    sols = {(g, r): solve_route(g, r) for g in "ABC" for r in ROUTES}
    return {"boost": boost(), "sols": sols, "hold": {g: hold(g) for g in "ABC"}, "nec": null_energy(),
            "est": estimate(), "cy": cypher()}


def checks(d):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    add("F1 a pure-tension sheet's stress is invariant under boosts along it: rim motion alone changes no balance", d["boost"])
    s = d["sols"]
    add("F3 A: into the corridor needs Pi = -sigma at every theta (negative flux or a README of net tension sigma); onto "
        "either plane sheet: no bend, theta = 0 only", s[("A", "corr")]["kind"] == "family"
        and sp.simplify(s[("A", "corr")]["Pi"] + S) == 0 and all(s[("A", r)]["kind"] == "nobend" for r in ("ours", "p2", "both")))
    add("F3 B: no route balances at any theta in (0, pi), whatever Pi's sign", s[("B", "ours")]["kind"] == "nobend"
        and all(s[("B", r)]["kind"] == "roots" and s[("B", r)]["roots"] == sp.EmptySet for r in ("corr", "p2", "both")))
    add("F3 C: onto both plane sheets, balance at every theta with Pi = 2 sigma exactly; into the corridor no bend; onto "
        "one plane sheet alone none", s[("C", "both")]["kind"] == "family" and sp.simplify(s[("C", "both")]["Pi"] - 2 * S) == 0
        and s[("C", "corr")]["kind"] == "nobend" and all(s[("C", r)]["kind"] == "roots" and s[("C", r)]["roots"] == sp.EmptySet
                                                       for r in ("ours", "p2")))
    nec = d["nec"]
    Phi = sp.Symbol("Phi", positive=True)
    add("F4 null dust: T(l,l) = 0 along its own rays, 4 Phi along the opposite radial rays, Phi along tangential ones; "
        "timelike dust: u.k = -gamma (1 + v cos alpha), and 1 + v cos alpha >= 1 - v > 0, so rho (u.k)^2 > 0 along every "
        "null k",
        nec["own"] == 0 and sp.simplify(nec["opp"] - 4 * Phi) == 0 and sp.simplify(nec["tan"] - Phi) == 0
        and nec["uk_min"] == nec["uk_min_expect"] and all(float(nec["uk"].subs({nec["v"]: vv, nec["a"]: aa})) < 0
                                                           for vv in (0.1, 0.9, 0.999) for aa in (0, 1.5, 3.14159)))
    add("F5 the hold (Pi = 0, 198 (a)): no geometry balances at any theta in (0, pi) -- R7 again",
        all(d["hold"][g] == sp.EmptySet for g in "ABC"))
    e = d["est"]
    add("F6 ESTIMATE: mean README density near the rim 0.10 (ell/m)^2 sigma (7.3 sigma at ell/m = 8.54); E feeds "
        "Pi = 2 sigma for at most 0.036 (ell/m)^2 m/c (2.6 m/c at 8.54)", abs(e["coef_ratio"] - 0.1006) < 1e-3
        and 7.2 < e["ratio"] < 7.5 and abs(e["coef_tau"] - 0.03606) < 1e-4 and 2.5 < e["tau"] < 2.7)
    runs = d["cy"]["runs"]
    add("F7 cypher: target A (closing through the hold) refused by statistics under every coding tried (18 orderings of "
        "the arrangement axis, unknown above 1 and below 0)", all(r["full"]["statistics"] == [] for r in runs.values()))
    add("F7 cypher: target B (closing while the README flows) refused by statistics with the uncomputed cells unknown, "
        "under every coding tried", all(r["forming"]["statistics"] == [] for r in runs.values()))
    c = d["cy"]["control"]
    add("F7 control: uncomputed cells set favourable -- statistics admits the timelike-README cells (5, 7, 8) for target "
        "B and still refuses target A", c["forming"]["statistics"] == [5, 7, 8] and c["full"]["statistics"] == [])
    return res


MUTANTS = {"dust_sheet": "the sheet given dust's stress (not boost-invariant)",
           "pi_plus": "the flux's push sign flipped (acting as tension)",
           "no_mirror": "C's position-2 sheet not mirrored",
           "null_own": "null dust tested along the opposite rays as its own",
           "hold_flux": "the README left flowing at the rim through the hold",
           "seat_hold": "a rim closing through the hold seated as data"}


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
        print("  mutant %-11s %-52s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(d):
    print("forming_rim.py -- the rim while the corridor forms (198 (a))\n")
    for (g, r), v in d["sols"].items():
        print("F3 %s %-5s %s" % (g, r, v))
    print("F4", d["nec"])
    print("F5 hold:", d["hold"])
    print("F6", d["est"])
    runs = d["cy"]["runs"]
    for key in list(runs)[:2] + list(runs)[-2:]:
        print("F7 coding", key, runs[key])
    print("F7 control", d["cy"]["control"])
    over = {l: sorted({tuple(r["full"][l] or []) for r in runs.values()}) for l in ("order", "algebra", "geometry", "information")}
    print("F7 over-reach on target A by coding (closing arrangements invented):", over)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
