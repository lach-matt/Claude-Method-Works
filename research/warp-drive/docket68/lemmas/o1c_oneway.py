#!/usr/bin/env python3
"""o1c_oneway.py -- item 282 (c): theorem row O1c (geodesic completeness) re-posed on the glued one-way object.
o1c_complete.py proved completeness for Bronnikov-Kim's eq. (17) at r0 = 2m through its maximal extension -- bound
geodesics turning "at V = 0 on each side", horizon generators over all Killing time -- which the auditing agent marked
as the reverse passage and an infinite past (281 (6)).  It is kept as written with its item-281 note; this is the row's
one-way form, after C1, C4, C5 and C7.  Worked in the conversation (computed with sympy, exact where marked; READ where
marked; deduced where marked; not verified by a separate session; not seated); 2026-10-12.

  Z0 (read) The words the row rests on, verbatim in the rulings file: M's 282 (1), "Re-pose them one-way
     (Recommended)", with the board's reading (c) that O1c and B5a are re-posed the same way; M's 273, "One-way,
     complete, README only" and "and classical GR there"; and 261 (3), the C3 verifier's report (not M's words): "the
     large end is four-dimensional Schwarzschild on the plane with corrections O(ell^2/r0^2)" and "surface gravity
     1/(4M), non-extremal".
  Z1 (computed, exact; READ where marked) Eq. (17) at r0 = 2m is not the corridor's geometry at either end.  Its g^rr
     has a double zero at r = 2m and its surface gravity, (1/2)|d_r g_tt| sqrt(g^rr/(-g_tt)) on the horizon, is 0
     (computed).  The small end is Tangherlini near the hole, kappa = 1/r_h (computed; rows_small O2s), and the large end
     is Schwarzschild on the plane, kappa = 1/(4M) (READ through 261 (3); computed here).  So o1c_complete's result is
     about a geometry the corridor does not have, and the row is re-posed on the object's own.
  Z2 (computed, exact; deduced where marked) The passage's classical part at the small end.  Our future interior, and
     position 2's past interior, outside the quantum region are Tangherlini's interior in its own time, -dT^2 + G dt^2 +
     R^2 dOmega_3^2 with G = r_h^2/R^2 - 1 -- on position 2's side with its own r_h (240; c7_oneway V9 (1)), every bound
     below holding with either side's.  Its Einstein tensor vanishes exactly where R'^2 = G: the TT component is the
     constraint, zero if and only if R'^2 = G, and with it every component vanishes (computed, both ways).  With p_t =
     -E~ and the angular momentum L conserved, every causal geodesic there has Tdot^2 = eps + E~^2/G + L^2/R^2, eps = 1
     timelike and 0 null (computed), so T is monotone along it.  Between the horizon and any R_c > 0 T spans less than
     r_h, the E~ = 0 fall (computed); timelike geodesics take less proper time than that, and null ones have Tdot^2 >=
     E~^2 R_c^2/(r_h^2 - R_c^2) + L^2/r_h^2 > 0 (computed), a finite affine length.  A radial body entering our face
     reaches the core in at most r_h/(1 + E~) of proper time (computed; c5_oneway U1).  So every causal geodesic in our
     interior reaches the quantum region in finite affine parameter, and every one in position 2's past interior leaves
     it, in finite affine parameter, by one of its boundaries (deduced).  Those entering by our face have E~ > 0: in our
     exterior d_t is future timelike, so every future causal momentum has p . d_t < 0 (deduced).  Those with E~ <= 0 do
     not come from our exterior but from what opened the hole -- among them the E~ = 0 T-lines, which on the eternal
     hole ran from bifurcation sphere to bifurcation sphere (c4_residue R6's item-310 note) -- and are covered the same.
     This carries c5_oneway U11 (4), verified at item 317, from the core to the whole interior.
  Z3 (READ; computed; deduced where marked) The quantum region.  Completeness there is M's ruling, not a result of this
     row: 273 chose the bounce "One-way, complete, README only" and gives up "classical GR there", so inside it no
     classical geodesic equation holds to be integrated.  The ruling is realized classically by c4_residue R6's core (R6
     run here): the same metric with R(T) smooth and even, R >= r_min > 0, G = r_h^2/R^2 - 1 > 0 throughout -- vacuum
     exactly outside the core, the null energy negative at the bounce, the curvature finite there (computed).  The first
     integrals of Z2 hold through it; there G <= r_h^2/r_min^2 - 1, so the null bound of Z2 holds with R_c = r_min, and
     T, monotone, crosses the core's finite range in finite affine parameter (deduced).  R6 realizes completeness for
     every causal geodesic crossing it; it does not model the README's route, which reverses its Killing energy against
     the continued d_t (c4_residue R13; Z4).  So the classical realization is complete, and the region's own
     completeness, with the README's passage through it, rests on 273.
  Z4 (computed, c4_residue R13 run here; deduced where marked) The boundary a geodesic leaves by.  A body crossing a
     t-independent core keeps its Killing energy and, under the gluing map (U, V) -> (-U, -V) (forced on 270 (a)'s
     single chart, a board reading: c5_oneway U11 (9), U12 (Q7)), leaves position 2's past interior by V' = 0,
     opposite U' = 0, the map's image of our face (computed) -- toward the map's image of what opened the hole, which
     on the one-way object is not an exterior (c5_oneway U9).  The README, the matter that bounces, leaves as its own
     image by U' = 0, position 2's face, into position 2's exterior, the map's image of ours -- the time symmetry of
     the construction M chose (c5_oneway U12 (Q3), deduced from 273).  The row does not turn on which boundary: either
     way the geodesic leaves the hole in finite affine parameter (Z2).  The passage, the README's, is by position 2's
     face, as 273 names it and the board's index at 283 orders it.
  Z5 (deduced) Dropped, as 270 and 282 require.  The bound geodesics that turned "at V = 0 on each side" crossed back
     from position 2's side -- the reverse passage: from position 2's exterior no future causal curve reaches its
     white-hole face (c7_oneway V9 (5)).  The generators "over all Killing time" ran into an infinite past the object
     does not have: its faces begin at the opening (270 (c)), before which the positions are joined through the bulk
     with no horizons (282 (2)).  The E~ = 0 lines' bifurcation sphere is dropped by 282; on the one-way object they
     come from what opened the hole (Z2).
  Z6 (deduced) The row, one way: no causal geodesic ends in the hole.  Every one that enters our face, or lies in our
     interior, crosses the classical interior in finite affine parameter (Z2); the quantum region is complete by M's
     ruling and on its classical realization (Z3); and every one leaves position 2's past interior in finite affine
     parameter (Z2), the README by position 2's face into position 2's exterior (Z4).  The null energy the region gives
     up is confined to it (pair_math P2, P4).  At the small end -- the corridor's, the README fixing r_h at 72,762 l5,
     r_h/ell = 8.0e-16 (c5_oneway U9, U12 (Q8)) -- at flat order, warp order entering at O(r_h/ell) = 8.0e-16.  It
     rests on M1 (C4, verified at the small end) and on 273.
  Z7 (computed) The row's question through the calculator, in the form C4's, C5's and C7's stand in (c4_residue R12):
     the clause "complete through the passage" read from b_interior's cells (B6's complete: singular 0, inner 0,
     quantum 1, shell 1) -- 1 at orders 2 and 3 under all 96 codings; 211's audit clean.  As for C4, C5 and C7 the
     agreement is the quantum bounce's own row read back, the clause replicated over every class of tension and matter.

What this row does not claim -- each left out with its reason, none open in it (314).
  - The quantum region's own form.  Completeness inside it is 273's, realized classically by R6's core (Z3); the
    region's quantum-gravitational form is beyond any computation here (c4_residue R12).
  - Anything outside the hole.  The exteriors are C1's and C4's outside-the-hole figures, which 282 keeps; before the
    opening is the join, about which B7 and B4a stand (282 (2)), and beyond V' = 0 the map's image of what opened the
    hole, which stands with that region; our face's closing is the CLOSE row's (c5_oneway U11 (11)).  O1c is the
    passage's row -- O1, one way and nonsingular -- and the trapped interior, where Penrose's theorem bites (b_interior
    B1, B2), is where it is decided.
  - Corrections beyond flat order (Z6), as for C5 (c5_oneway U11 (10)).
  - The large end.  The corridor is at the small end (Z6); the large end enters only to show that eq. (17) at r0 = 2m
    is the geometry of neither end (Z1), and its interior is not computed here.
  - That eq. (17) at r0 = 2m is the corridor's geometry (Z1): o1c_complete stands as a statement about eq. (17).

Imports c4_residue.py (ricci_diag, R6, R13), b_interior.py, c4_oneway.py, calculator.py, index_audit.py and
research/warp-drive/hlaw.py by path.  Stdlib + sympy.  python3 o1c_oneway.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import sys
from collections import Counter

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M282 = "Re-pose them one-way (Recommended)"
M282C = "theorem rows O1c and B5a, marked at 281, are re-posed the same way"
M273 = ("One-way, complete, README only", "and classical GR there")
V261 = ("the large end is four-dimensional Schwarzschild on the plane with corrections O(ell^2/r0^2)",
        "surface gravity 1/(4M), non-extremal")
CITED = (("c7_oneway.py", "never reaches its white-hole face U' = 0"),                      # Z5
         ("c4_residue.py", "the sphere 282 drops"),                                         # Z2, Z5
         ("c4_residue.py", "R6 does not model along the README"),                           # Z3
         ("c5_oneway.py", "that side is Q1's image of what opened the hole, not an exterior"),  # Z4
         ("c5_oneway.py", "r_h/(c (1 + E~))"),                                              # Z2
         ("c5_oneway.py", "r_h/l5 = 72,762"), ("c5_oneway.py", "O(r_h/ell) = 8.0e-16"),     # Z6
         ("pair_math.py", "Outside the quantum region every ray segment keeps 183"),        # Z6
         ("pair_math.py", "the negative is confined to the quantum region"))                # Z6
_MOD = {}


def _load(name, key):
    path = name if os.path.isabs(name) else os.path.join(HERE, name)
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


def z1():
    """surface gravities: eq. (17) at r0 = 2m against the corridor's holes"""
    r, m, rh, M = sp.symbols("r m r_h M", positive=True)
    f17 = 1 - 2 * m / r
    grr17 = (1 - 2 * m / r) * (1 - 2 * m / r) / (1 - sp.Rational(3, 2) * m / r)       # g^rr at r0 = 2m
    # static metric -A dt^2 + dr^2/B: kappa = (1/2)|A'| sqrt(B/A) on the horizon; here sqrt(B/A) = sqrt(f/H) -> 0
    kappa17 = sp.limit(sp.Abs(sp.diff(f17, r)) * sp.sqrt(grr17 / f17) / 2, r, 2 * m, "+")
    double = sp.simplify(sp.diff(grr17, r).subs(r, 2 * m)) == 0
    ftang = 1 - rh ** 2 / r ** 2
    k5 = sp.simplify(sp.diff(ftang, r).subs(r, rh) / 2)
    fs = 1 - 2 * M / r
    k4 = sp.simplify(sp.diff(fs, r).subs(r, 2 * M) / 2)
    if MUT.get("extremal_small"):
        k5 = sp.Integer(0)                                  # the mutant: the small end read as extremal
    return dict(kappa17=sp.simplify(kappa17), double=double, k5=k5, k4=k4)


def _cr():
    if "cr" not in _MOD:
        _MOD["cr"] = _load("c4_residue.py", "o1co_cr")
    return _MOD["cr"]


def _interior(dim):
    """-dT^2 + G dt^2 + R^2 dOmega^(dim-2): the Einstein tensor zero exactly where R'^2 = G, both ways"""
    T, t = sp.symbols("T t", real=True)
    angs = sp.symbols("a1:%d" % (dim - 1), real=True)
    Rf = sp.Function("R")(T)
    rh, m = sp.symbols("r_h m", positive=True)
    G = (rh ** 2 / Rf ** 2 - 1) if dim == 5 else (2 * m / Rf - 1)
    sph = [Rf ** 2]
    for i in range(1, dim - 2):
        sph.append(sph[-1] * sp.sin(angs[i - 1]) ** 2)
    g = sp.diag(-1, G, *sph)
    X = [T, t] + list(angs)
    Ric, _ = _cr().ricci_diag(g, X)
    gi = g.inv()
    Rs = sp.simplify(sum(gi[i, i] * Ric[i, i] for i in range(dim)))
    Ein = [sp.simplify(Ric[i, i] - Rs * g[i, i] / 2) for i in range(dim)]
    R0, R1, R2, x = sp.symbols("R0 R1 R2 x")
    sub = lambda e: e.subs(sp.Derivative(Rf, (T, 2)), R2).subs(sp.Derivative(Rf, T), R1).subs(Rf, R0)
    Gs = G.subs(Rf, R0)
    R2v = sp.diff(G.subs(Rf, x), x).subs(x, R0) / 2           # R'' from R'^2 = G
    if MUT.get("wrong_vacuum_%d" % dim):
        Gs = Gs + 1                                          # the mutant: the vacuum condition shifted
    vac = all(sp.simplify(sub(e).subs(R2, R2v).subs(R1, sp.sqrt(Gs))) == 0 for e in Ein)
    tt = sp.factor(sp.simplify(sub(Ein[0])))                 # the constraint: no R''
    sols = {sp.simplify(z ** 2) for z in sp.solve(sp.numer(tt), R1)}
    iff = not tt.has(R2) and sols == {sp.simplify(Gs)}
    return dict(vac=vac, iff=iff)


def zc():
    """Z2, Z3: Tangherlini's interior at the small end, and R6's core"""
    r, rh, Et, Rc, d = sp.symbols("r r_h E_t R_c d", positive=True)
    tau5 = sp.integrate(r / sp.sqrt((Et ** 2 - 1) * r ** 2 + rh ** 2), (r, 0, rh))
    tau5 = sp.cancel(sp.simplify(tau5.replace(sp.polar_lift, lambda z: z)))
    span5 = sp.simplify(sp.integrate(r / sp.sqrt(rh ** 2 - r ** 2), (r, Rc, rh)))   # T from R_c to the horizon
    G, R, E, L = sp.symbols("G R E L", positive=True)
    Td, td, pd = sp.symbols("Tdot tdot phidot", real=True)
    sign = -1 if MUT.get("null_stalls") else 1
    # the norm of u on -dT^2 + G dt^2 + R^2 dphi^2 with the Killing momenta G tdot = E~ and R^2 phidot = L
    norm = lambda eps_, s_: sp.Eq((-Td ** 2 + s_ * G * td ** 2 + R ** 2 * pd ** 2).subs({td: E / G, pd: L / R ** 2}),
                                  -eps_)
    td_time = sp.expand(sp.solve(norm(1, 1), Td)[-1] ** 2)
    td_null = sp.expand(sp.solve(norm(0, sign), Td)[-1] ** 2)
    first = sp.simplify(td_time - 1 - E ** 2 / G - L ** 2 / R ** 2) == 0 and sp.simplify(td_null - E ** 2 / G - L ** 2
                                                                                         / R ** 2) == 0
    Gmax = rh ** 2 / Rc ** 2 - 1                              # G is largest at the smallest R
    if MUT.get("no_core"):
        Gmax = sp.oo                                         # the mutant: the singular interior, R_c -> 0
    low = td_null.subs({G: Gmax, R: rh})                     # and 1/R^2 smallest at the horizon
    ispos = lambda e: sp.factor(sp.simplify(sp.expand(e))).is_positive is True
    null = ispos(low.subs(L, 0).subs(rh, Rc + d)) and ispos(low.subs(E, 0).subs(rh, Rc + d))
    form = sp.simplify(low - E ** 2 * Rc ** 2 / (rh ** 2 - Rc ** 2) - L ** 2 / rh ** 2) == 0
    R6 = _cr().r6()
    return dict(tau5=tau5, span5=span5, first=first, form=form, null=null, i5=_interior(5),
                r6=dict(vac=R6["vac"], neg=R6["neg"], finite=R6["finite"]))


def z4():
    """the boundary a geodesic crossing a t-independent core leaves position 2's past interior by (R13)"""
    q = dict(_cr().r13()["Q1"])
    if MUT.get("exit_mirror"):
        q["face"], q["opposite"] = q["mirror_face"], False  # the mutant: it leaves by position 2's face
    return q


_Z7 = {}


def z7():
    """the row's question through the calculator, in R12's form"""
    key = tuple(sorted(k for k in MUT if k.startswith("z7_")))
    if key in _Z7:
        return _Z7[key]
    C4 = _load("c4_oneway.py", "o1co_c4")
    CA = _load("calculator.py", "o1co_calc")
    HL = C4._load_path(os.path.join(os.path.dirname(D68), "hlaw.py"), "o1co_hl")
    IA = _load("index_audit.py", "o1co_ia")
    cells = _load("b_interior.py", "o1co_bi").cells()
    keys = {"singular": (0, "none", "ours"), "inner": (1, "none", "pos2"), "quantum": (0, "quantum", "pos2"),
            "shell": (0, "shell", "pos2")}
    names4 = ("singular", "inner", "quantum", "shell")
    row = {k: cells[keys[k]]["complete"] for k in names4}
    if MUT.get("z7_singular_complete"):
        row["singular"] = 1                                 # the mutant: the singular interior read as complete
    F18 = {(1, 1): {1}, (1, 0): {0, 1}, (0, 1): {1}, (0, 0): {0, 1}}
    out, audit = {}, None
    for k in (2, 3):
        res = Counter()
        for perm in itertools.permutations(range(4)):
            kmap = dict(zip(names4, perm))
            for tf, mf in itertools.product((0, 1), repeat=2):
                tq, mq = 1 ^ tf, 1 ^ mf
                kn = [(kmap[kk], t ^ tf, mm ^ mf, row[kk]) for kk in names4 for (t, mm) in F18
                      if (kk, t ^ tf, mm ^ mf) != ("quantum", tq, mq)]
                views = dict(order=(0,), algebra=(0,), geometry=(0,), information=(0,), statistics=(0, 1, 2))
                res[C4._staged(CA, HL, ["K", "t", "m", "O1c"], kn, (kmap["quantum"], tq, mq), views, k)["answer"]] += 1
                if audit is None:
                    a = IA.audit_index(["K", "t", "m", "O1c"], kn)
                    audit = bool(a["keys"] or a["onehot"])
        out[k] = res
    _Z7[key] = dict(row=row, out=out, audit=audit)
    return _Z7[key]


def compute():
    return dict(z1=z1(), zc=zc(), z4=z4(), z7=z7())


def report(o):
    print("o1c_oneway.py -- theorem row O1c re-posed one-way (item 282 (c))\n")
    a = o["z1"]
    print("Z1 eq. (17) at r0 = 2m: g^rr's double zero %s, surface gravity %s; small end kappa = %s; large end kappa = %s"
          % (a["double"], a["kappa17"], a["k5"], a["k4"]))
    b = o["zc"]
    print("Z2 Tangherlini's interior: vacuum where R'^2 = G %s, only there %s; first integrals %s; fall r_h/(1+E~): %s; "
          "T span from R_c: %s; null bound E~^2 R_c^2/(r_h^2 - R_c^2) + L^2/r_h^2: %s, positive %s"
          % (b["i5"]["vac"], b["i5"]["iff"], b["first"], b["tau5"], b["span5"], b["form"], b["null"]))
    print("Z3 R6's core (run here): %s" % b["r6"])
    c = o["z4"]
    print("Z4 R13 under (U, V) -> (-U, -V): a t-independent core's body leaves by %s, opposite the image %s of our "
          "face: %s" % (c["face"], c["mirror_face"], c["opposite"]))
    z = o["z7"]
    print("Z7 the row %s; order 2 %s, order 3 %s; audit flagged: %s" % (z["row"], dict(z["out"][2]), dict(z["out"][3]),
                                                                        z["audit"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("Z0 282 (1) and its reading (c), 273's two phrases and 261 (3)'s two verbatim in the rulings file",
        all(w in rul for w in (M282, M282C) + M273 + V261))
    a = o["z1"]
    r_h, M = sp.symbols("r_h M", positive=True)
    add("Z1 eq. (17) at r0 = 2m extremal (double zero, surface gravity 0); the small end 1/r_h, the large end 1/(4M)",
        a["double"] and a["kappa17"] == 0 and sp.simplify(a["k5"] - 1 / r_h) == 0
        and sp.simplify(a["k4"] - 1 / (4 * M)) == 0)
    b = o["zc"]
    rh, Et, Rc = sp.symbols("r_h E_t R_c", positive=True)
    add("Z2 Tangherlini's interior vacuum exactly where R'^2 = G (both ways); first integrals from the norm; the fall "
        "r_h/(1 + E~); T spans sqrt(r_h^2 - R_c^2) < r_h; the null bound positive", b["i5"]["vac"] and b["i5"]["iff"]
        and b["first"] and sp.simplify(b["tau5"] - rh / (1 + Et)) == 0
        and sp.simplify(b["span5"] - sp.sqrt(rh ** 2 - Rc ** 2)) == 0 and b["form"] and b["null"])
    add("Z3 R6's core, run here: vacuum outside it, the null energy negative at the bounce, the curvature finite",
        all(b["r6"].values()))
    c = o["z4"]
    add("Z4 under (U, V) -> (-U, -V) a body crossing a t-independent core leaves by V' = 0, opposite U' = 0, the image "
        "of our face", c["sign"] == 1 and c["face"] == "V'=0" and c["mirror_face"] == "U'=0" and c["opposite"])
    txt = lambda f: " ".join(open(os.path.join(HERE, f), encoding="utf-8").read().split())
    cited = CITED if not MUT.get("cite_moved") else ((CITED[0][0], CITED[0][1].replace("U'", "V'")),) + CITED[1:]
    add("Z5/Z6 the record Z2-Z6 cite, verbatim in the cited files", all(w in txt(f) for f, w in cited))
    z = o["z7"]
    add("Z7 the row's question through the calculator in R12's form: 1 at orders 2 and 3 under all 96 codings; audit "
        "clean", z["row"] == {"singular": 0, "inner": 0, "quantum": 1, "shell": 1}
        and all(z["out"][k] == Counter({1: 96}) for k in (2, 3)) and not z["audit"])
    return res


MUTANTS = {"extremal_small": "the small end read as extremal (Z1)",
           "wrong_vacuum_5": "Tangherlini's vacuum condition shifted (Z2)",
           "null_stalls": "a null route stalled in the interior (Z2)",
           "no_core": "the quantum region removed, R_c -> 0: the singular interior (Z2)",
           "exit_mirror": "a t-independent core's body read as leaving by position 2's face (Z4)",
           "cite_moved": "V9 (5) cited with the wrong face (Z5/Z6)",
           "z7_singular_complete": "the singular interior read as complete (Z7)"}


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
        print("  mutant %-22s %-52s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
