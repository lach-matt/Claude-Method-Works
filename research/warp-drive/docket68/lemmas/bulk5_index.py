#!/usr/bin/env python3
"""bulk5_index.py -- item 233: the five-dimensional bulk index, built from positions 1, 2a, 2b, 2c and 2P.  M: "Use
universe positions 1, 2a, 2b, 2c, and 2P to build the 5D bulk index. The 5D bulk should contain every plausible and
possible statistical universe".  Worked in the conversation (computed, exact where marked; deduced where marked; not
verified by a separate session; not seated); 2026-10-11.

Readings (item 233, the board's, to be overruled by M): "possible" is every universe the positions' differences
generate, composed in any order and either direction; "plausible" is the theorem's own conditions on a universe;
"statistical" is computed both ways -- the ensemble weighted by our unknown tension's window, and the cypher's
statistics language over the positions; an axis the positions never move is reported as unseen.

  K0 (read) M's item-233 words, verbatim in the rulings file.
  K1 (computed, exact) Each position's five-dimensional side, as exact powers of 2 of ours.  A universe at G x 2^g with
     its plane's tension and offset x 2^s has kappa5^4 x 2^(g-s), ell^2 x 2^-(g+s), Lambda5 x 2^(g+s), G5 x 2^((g-s)/2),
     the 5D Planck length l5 x 2^((g-s)/6) and ell/l5 x 2^-((2g+s)/3) -- so (ell/l5)^3 x sigma/sigma_P = ours exactly:
     the bulk's curvature in its own 5D Planck units is the plane's Planck-unit tension (201's second reading).  All
     twelve members agree with p2_planck.sector() to 1e-12.  The positions sit in three distinct 5D bulks -- {1, 2a}
     (kappa5^4 x 1, ell x 1), {2b, 2c} (x 2, x 2^-1/2), {2P} (x 8, x 2^1/2) -- and in two 5D geometries: 2P's ell/l5 is
     ours, 2b's is x 2^-2/3.
  K2 (computed, exact) Every possible universe the positions generate.  2b moves (g, s) by (1, 0), 2P by (1, -2), 2a
     moves the matter law; combined in any order and either direction, i steps of 2b and j of 2P give g = i + j,
     s = -2j: the lattice of (i, j) in Z^2 for each law.  In 5D terms the bulk's curvature exponent is 2i and the 5D
     coupling's i + 3j.  The twelve members are i, j in {0, 1}.  The lattice is exactly half of the integer (g, s)
     plane (s even): a universe at G x 2, tension x 2 is possible but no composition of the positions reaches it.
  K3 (computed; the conditions sourced) Plausible: with our tension at S0 x 2^w, w in [0, W], W = log2 of our window =
     196.885 doublings, a universe is plausible for that w when (229) its tension and offset are positive and its
     matter ordinary -- every lattice universe, on the three computed laws; (ITEM197) its tension is under its own top,
     w + 2i <= W; (the table-top floor) w + i - j >= 0 read against its own G, or w - 2j >= 0 read as the same absolute
     force; (the README's capacity, EXAMPLE_N) 2i <= C = 354.66, which the top always binds first.  Plausible for some w:
     j <= W - |i| and i <= W/2 (relative floor), or 2j <= W - 2 max(i, 0) and i <= W/2 (absolute).  The strongest-gravity plausible
     universe on the 2b axis is i = 98.  The region is bounded above and open below: every universe with weaker gravity
     in either direction stays plausible.  The plausible bulk is infinite.
  K4 (computed) The statistical weight -- the fraction of our tension's window for which a universe is plausible.
     Position 1 and 2a weigh 1; 2b and 2c (W - 2)/W; 2P (W - 1)/W relative, (W - 2)/W absolute, as p2_planck Q3 found
     (our sigma >= 2 S0 or 4 S0).  Infinitely many universes weigh exactly 1 (every i <= 0, j <= i under the relative
     reading), so the ensemble 230 names cannot be normalised by the theorem's conditions: a measure on G and the
     tension -- the 5D coupling's distribution over the bulk -- is needed, and no ruling gives one.
  K5 (computed; the cypher, roster 1173, audited, each axis ordered away from ours) The positions as an index, held
     cells the seven position universes.
     - In 201's basis (matter, sigma_SI, sigma/sigma_P) the box is the twelve.  Order, algebra and information admit
       exactly the five compositions (E = 5 each); geometry and statistics admit none (E = 0), as p2_planck Q7 found.
     - In the 5D basis (matter, ell/l5, kappa5^4) 2b and 2P both move the coupling, so 2b + 2P compounds to x 16, a
       value no position carries, outside the box of 18: these are not the basis in which the positions compose as
       joins.  Exact E: order 8, algebra 8, geometry 3, information 5, statistics 0.  Order and algebra admit the two
       compositions in the box (2a + 2P) and six universes no composition reaches -- G x 2^(1/3) with tension x
       2^(-2/3), and G x 2^(5/3) with x 2^(-4/3), on every law: the bulk's own coordinates fill in between the
       positions, so the lattice of K2 is a sublattice of what is possible.
     - Statistics admits nothing beyond the seven in either basis: read as the cypher's statistics language, the
       positions determine no universe but themselves.  So "every plausible and possible statistical universe" comes
       from the generation rule and the conditions (K2-K4) and from the lattice languages, not from statistics; and the
       cypher's box holds only values the positions carry, so it never reaches beyond i, j in {0, 1}.
     - The audit finds no key and no one-hot code in either index.
  K6 (deduced from K1) No single homogeneous AdS5 with one coupling holds positions 1, 2b and 2P as planes: their 5D
     couplings differ (x 1, x 2, x 8).  Positions 1 and 2a share one 5D bulk, so a construction joining them needs no
     varying coupling.  Lambda5 can differ from one bulk region to the next across a brane (as in asymmetric
     braneworlds), but in standard 5D gravity kappa5 is a constant of the theory: joining 1 to 2b, 2c or 2P needs the
     coupling itself to vary across the bulk, which takes a field over the bulk (a dilaton's role).  2P is the cleanest
     case: its 5D geometry in its own Planck units is ours (K1), and only the coupling against matter differs.  The
     everything bulk that holds every plausible universe is then that field's configuration space, and K4's missing
     measure is its distribution.
  K7 (read, deduced) Unseen axes: the offset's ratio to the tension (every position keeps it: plausible for any value
     from 0 up to the capacity's bound, reported, not filled); the matter law between and beyond the three computed laws
     (item 221's delta is continuous; only delta = 0, min and mirror are computed); hbar and c as carriers, excluded by
     225 A's shared SI (p2_planck Q1), so not possible universes under a README every universe can read.

What this does not show.
  - W and the floors are the window's computed values (sigma_cypher W1, imported exact, 209); C uses the example README.
  - "Ordinary matter" is taken from item 221's computed laws (Cu2 has no bound minimum under mirror; it is still
    null-energy-keeping matter).
  - Bodies, stars and cosmology are not conditions of the theorem and are not used to cut the bulk.
  - K6's field is the board's deduction from standard 5D gravity, not a construction.

Imports p2_planck.py (and through it p2_gravity.py), tools/cypher.py and index_audit.py by path; reads the rulings file.
Stdlib.  python3 bulk5_index.py [--selftest | --mutants]
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
M233 = ("Use universe positions 1, 2a, 2b, 2c, and 2P to build the 5D bulk index. The 5D bulk should contain every "
        "plausible and possible statistical universe")
EXAMPLE_N = 2742570311524972                   # warptheorem.py's example README
LANGS = ("order", "algebra", "geometry", "information", "statistics")
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}


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


PP = _load(os.path.join(HERE, "p2_planck.py"), "b5_pp")
PG = PP.PG
POSITIONS = ("ours", "2a-min", "2a-mirror", "2b", "2c-min", "2c-mirror", "2P")      # the five positions' universes
LAW_ORDER = ("ours", "min", "mirror")                                               # item 221's delta: 0 < min < mirror


# ============================================================================================== K1 the 5D side
def exps(gf, sf):
    """exact exponents of 2 (as Fractions) of each quantity against ours, for G x gf and tension, offset x sf"""
    g, s = F(int(math.log2(gf))), F(round(math.log2(float(sf))))
    assert F(2) ** int(g) == gf and F(2) ** int(s) == sf
    e = dict(G=g, sigma=s, k4=g - s, ell2=-(g + s), L5=g + s, G5=(g - s) / 2, l5=(g - s) / 6, ell_l5=-(2 * g + s) / 3,
             sigma_planck=2 * g + s, N_max=-(2 * g + s), E1=-g / 2, m1=g / 2)
    if MUT.get("k4_wrong"):
        e["k4"] = g + s
    return e


def five_d():
    """each member's exact 5D exponents, checked against p2_planck.sector()'s floats"""
    base = PP.sector(1, F(1))
    out = {}
    for name, (law, gf, sf) in PP.MEMBERS.items():
        e = exps(gf, sf)
        sec = PP.sector(gf, sf)
        num = dict(k4=sec["k4"] / base["k4"], ell2=(sec["ell"] / base["ell"]) ** 2, L5=sec["L5"] / base["L5"],
                   sigma_planck=sec["sigma_planck"] / base["sigma_planck"], N_max=sec["N_max"] / base["N_max"],
                   E1=sec["E1"] / base["E1"], m1=sec["m1"] / base["m1"])
        agree = all(abs(num[k] / 2 ** float(e[k]) - 1) < 1e-12 for k in num)
        out[name] = dict(law=law, gf=gf, sf=sf, e=e, agree=agree)
    return out


def bulks(fd):
    """which members share one 5D bulk (the same kappa5^4 and ell), and which one 5D geometry (the same ell/l5)"""
    by_bulk, by_geom = {}, {}
    for n, v in fd.items():
        by_bulk.setdefault((v["e"]["k4"], v["e"]["ell2"]), []).append(n)
        by_geom.setdefault(v["e"]["ell_l5"], []).append(n)
    return by_bulk, by_geom


# ========================================================================================= K2 the generated lattice
MOVES = {"2b": (1, 0), "2P": (1, -2)}          # (g, s) per step; 2a moves the law


def lattice_point(i, j):
    g = i * MOVES["2b"][0] + j * MOVES["2P"][0]
    s = i * MOVES["2b"][1] + j * MOVES["2P"][1]
    return g, s


def member_steps():
    """the twelve members as (law, i, j)"""
    out = {}
    for name, (law, gf, sf) in PP.MEMBERS.items():
        g, s = int(math.log2(gf)), round(math.log2(float(sf)))
        j = -s // 2
        i = g - j
        out[name] = (law, i, j)
    return out


# ============================================================================================ K3, K4 plausibility
def constants():
    S0, S1 = PG.SIGMA_WINDOW
    W = math.log2(S1 / S0)
    C = math.log2(PP.sector(1, F(1))["N_max"] / EXAMPLE_N)
    return dict(S0=S0, S1=S1, W=W, C=C)


def w_interval(i, j, k, floor):
    """the range of w (our tension = S0 x 2^w, w in [0, W]) for which universe (i, j) is plausible"""
    W, C = k["W"], k["C"]
    if 2 * i > C:
        return None
    lo = max(0.0, float(j - i) if floor == "rel" else float(2 * j))
    if MUT.get("floor_sign"):
        lo = max(0.0, float(i - j))
    hi = min(W, W - 2 * i)
    return (lo, hi) if lo <= hi else None


def weight(i, j, k, floor):
    iv = w_interval(i, j, k, floor)
    return 0.0 if iv is None else (iv[1] - iv[0]) / k["W"]


def window_check(k):
    """K3's exponent inequalities against p2_planck.window()'s own floors and top, for the twelve members"""
    ok = True
    for name, (law, gf, sf) in PP.MEMBERS.items():
        g, s = int(math.log2(gf)), round(math.log2(float(sf)))
        j = -s // 2
        i = g - j
        wn = PP.window(gf, sf)
        for floor, need in (("rel", wn["need_rel"]), ("abs", wn["need_abs"])):
            lo = max(k["S0"], need)
            hi = min(k["S1"], wn["need_top"])
            iv = w_interval(i, j, k, floor)
            if iv is None:
                ok &= lo > hi
            else:
                ok &= abs(math.log2(lo / k["S0"]) - iv[0]) < 1e-9 and abs(math.log2(hi / k["S0"]) - iv[1]) < 1e-9
    return ok


def region(k, floor, span=400):
    """the plausible lattice: its extremes, and what happens going toward weaker gravity"""
    pts = [(i, j) for i in range(-span, span + 1) for j in range(-span, span + 1) if w_interval(i, j, k, floor)]
    imax = max(i for i, _ in pts)
    jmax = max(j for _, j in pts)
    edge = [(i, j) for i, j in pts if i == -span or j == -span]                       # the region reaches the box's edge
    ones = sum(1 for i, j in pts if weight(i, j, k, floor) == 1.0)
    return dict(imax=imax, jmax=jmax, reaches_edge=bool(edge), n_in_box=len(pts), weight_one_in_box=ones)


# ================================================================================================ K5 the cypher
def cypher_positions(cy, ia, fd):
    steps = member_steps()
    out = {}
    bases = {"201": lambda n: (LAW_ORDER.index(fd[n]["law"]), int(fd[n]["e"]["sigma"]), int(fd[n]["e"]["sigma_planck"])),
             "5D": lambda n: (LAW_ORDER.index(fd[n]["law"]), int(3 * fd[n]["e"]["ell_l5"]), int(fd[n]["e"]["k4"]))}
    names = {"201": ["matter", "sigma_SI", "sigma_planck"], "5D": ["matter", "ell_l5_x3", "kappa5_4"]}
    for b, f in bases.items():
        held = sorted({f(n) for n in POSITIONS})
        combos = {n: f(n) for n in PP.MEMBERS if n not in POSITIONS}
        coords = names[b]
        # each axis ordered away from ours: ours' value first, then by distance from it (a position's move points up;
        # sorted numerically, 2P's tension x 1/4 would point down and a join would drop it -- p2_combined's finding)
        vals = [sorted({c[x] for c in held}, key=lambda v: (abs(v), v)) for x in range(3)]
        if MUT.get("numeric_order"):
            vals = [sorted({c[x] for c in held}) for x in range(3)]
        box = [(a, c, d) for a in vals[0] for c in vals[1] for d in vals[2]]
        ix = cy.Index("bulk5_" + b, coords, [list(c) for c in held], value_order={coords[x]: vals[x] for x in range(3)})
        adm = {}
        for lg in LANGS:
            a, _ = cy.ADMISSION[lg][0](ix, dict(OPTS))
            adm[lg] = None if a is None else {tuple(ix.decode[x][c[x]] for x in range(3)) for c in a}
        def off_lattice(cell):
            """a 5D-basis cell as (g, s): on the positions' lattice only if g is an integer and s an even one"""
            x, kap = cell[1], cell[2]
            g = F(kap - x, 3)
            s_ = g - kap
            return (g, s_, g.denominator == 1 and s_.denominator == 1 and s_.numerator % 2 == 0)
        extra = {}
        if b == "5D":
            for lg in LANGS:
                if adm[lg] is not None:
                    extra[lg] = sorted((LAW_ORDER[c[0]],) + off_lattice(c)[:2] for c in adm[lg]
                                       if c not in held and c not in combos.values() and not off_lattice(c)[2])
        out[b] = dict(held=held, box=len(box), combos=combos, off_lattice=extra,
                      in_box=sorted(n for n, c in combos.items() if c in box),
                      E={lg: (None if adm[lg] is None else len(adm[lg]) - len(held)) for lg in LANGS},
                      predicted={lg: (None if adm[lg] is None else sorted(n for n, c in combos.items() if c in adm[lg]))
                                 for lg in LANGS},
                      run=cy.run(ix, "1173", dict(OPTS)), audit=ia.audit_index(coords, held))
    out["steps"] = steps
    return out


# ================================================================================================ compute, report
def unseen():
    """K7: the offset's ratio to the tension in each member (every position keeps ours), and the matter law's values"""
    base = PP.sector(1, F(1))
    r0 = base["offset"] / base["sigma"]
    ratios = {n: PP.sector(gf, sf)["offset"] / PP.sector(gf, sf)["sigma"] / r0 for n, (law, gf, sf) in PP.MEMBERS.items()}
    if MUT.get("offset_moves"):
        ratios["2P"] = 2.0
    return dict(ratios=ratios, laws=sorted({law for law, gf, sf in PP.MEMBERS.values()}, key=LAW_ORDER.index))


def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "b5_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "b5_ia")
    fd = five_d()
    k = constants()
    return dict(fd=fd, bulks=bulks(fd), k=k, steps=member_steps(), wcheck=window_check(k), unseen=unseen(),
                reg={f: region(k, f) for f in ("rel", "abs")},
                wts={n: (weight(i, j, k, "rel"), weight(i, j, k, "abs")) for n, (law, i, j) in member_steps().items()},
                cy=cypher_positions(cy, ia, fd))


def report(o):
    k = o["k"]
    print("bulk5_index.py -- the 5D bulk index from positions 1, 2a, 2b, 2c, 2P (item 233)\n")
    print("K1 the members' 5D side (exponents of 2 against ours):")
    for n, v in o["fd"].items():
        e = v["e"]
        print("  %-13s law %-6s G %s sigma %s | kappa5^4 %s ell^2 %s Lambda5 %s G5 %s l5 %s ell/l5 %s | sigma/sigma_P %s  %s"
              % (n, v["law"], e["G"], e["sigma"], e["k4"], e["ell2"], e["L5"], e["G5"], e["l5"], e["ell_l5"],
                 e["sigma_planck"], "agrees" if v["agree"] else "DISAGREES"))
    by_bulk, by_geom = o["bulks"]
    print("  5D bulks (kappa5^4, ell^2):", {str(kk): vv for kk, vv in by_bulk.items()})
    print("  5D geometries (ell/l5):", {str(kk): vv for kk, vv in by_geom.items()})
    print("\nK2 the members as (law, i 2b-steps, j 2P-steps):", o["steps"])
    print("\nK3 W = %.6f doublings (our window %.6e .. %.6e J/m^3); C = %.4f; window inequalities agree with p2_planck: %s"
          % (k["W"], k["S0"], k["S1"], k["C"], o["wcheck"]))
    for f, r in o["reg"].items():
        print("  %s floor: i <= %d, j <= %d; reaches the scanned box's lower edge: %s; %d plausible in |i|,|j| <= 400, %d of "
              "them weight 1" % (f, r["imax"], r["jmax"], r["reaches_edge"], r["n_in_box"], r["weight_one_in_box"]))
    print("\nK4 weights (relative, absolute):", {n: ("%.6f" % a, "%.6f" % b) for n, (a, b) in o["wts"].items()})
    print("\nK5 the cypher over the seven position universes:")
    for b in ("201", "5D"):
        c = o["cy"][b]
        print("  basis %s: box %d; compositions inside it %s; exact E %s" % (b, c["box"], c["in_box"], c["E"]))
        print("     predicted compositions per language: %s" % c["predicted"])
        if c["off_lattice"]:
            print("     admitted universes no composition reaches, as (law, g, s): %s" % {
                lg: [(a, str(g), str(s_)) for a, g, s_ in v] for lg, v in c["off_lattice"].items()})
        print("     roster 1173: %s; audit %s" % ("; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"])
                                                          for v in c["run"]["verdicts"]), c["audit"]))


# ================================================================================================= checks
def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("K0 M's item-233 words verbatim in the rulings file", M233 in rul)
    fd = o["fd"]
    e2b, e2P, e22 = fd["2b"]["e"], fd["2P"]["e"], fd["2b+2P"]["e"]
    ok = all(v["agree"] for v in fd.values()) and len(fd) == 12
    ok &= (e2b["k4"], e2b["ell2"], e2P["k4"], e2P["ell2"], e22["k4"], e22["ell2"]) == (1, -1, 3, 1, 4, 0)
    ok &= all(v["e"]["ell_l5"] * 3 == -v["e"]["sigma_planck"] for v in fd.values())
    by_bulk, by_geom = o["bulks"]
    pos_bulks = {kk: sorted(n for n in vv if n in POSITIONS) for kk, vv in by_bulk.items()}
    ok &= sorted(v for v in pos_bulks.values() if v) == sorted([["2a-min", "2a-mirror", "ours"],
                                                                 ["2b", "2c-min", "2c-mirror"], ["2P"]])
    ok &= sorted(by_geom[F(0)]) == sorted(["ours", "2a-min", "2a-mirror", "2P", "2a+2P-min", "2a+2P-mirror"])
    add("K1 the 5D side exact on all twelve (agrees with p2_planck.sector to 1e-12): 2b kappa5^4 x 2, ell^2 x 1/2; 2P x 8, "
        "x 2; 2b+2P x 16, x 1; (ell/l5)^3 x sigma/sigma_P = ours; the positions in three 5D bulks, 2P in ours' geometry", ok)
    st = o["steps"]
    ok = all(st[n][1:] in ((0, 0), (1, 0), (0, 1), (1, 1)) for n in st) and len(set(st.values())) == 12
    ok &= st["2b"] == ("ours", 1, 0) and st["2P"] == ("ours", 0, 1) and st["2c+2P-mirror"] == ("mirror", 1, 1)
    ok &= all(lattice_point(i, j) == (int(fd[n]["e"]["G"]), int(fd[n]["e"]["sigma"])) for n, (law, i, j) in st.items())
    ok &= lattice_point(1, 0)[1] % 2 == 0 and all(lattice_point(i, j)[1] % 2 == 0 for i in range(-3, 4) for j in range(-3, 4))
    add("K2 the twelve are the lattice's i, j in {0, 1}; every composition has s even -- G x 2 with tension x 2 is possible "
        "but generated by no composition", ok)
    k, r = o["k"], o["reg"]
    ok = o["wcheck"] and "%.3f" % k["W"] == "196.885" and "%.2f" % k["C"] == "354.66" and k["C"] > k["W"]
    ok &= r["rel"]["imax"] == 98 and r["rel"]["jmax"] == 196 and r["abs"]["imax"] == 98 and r["abs"]["jmax"] == 98
    ok &= r["rel"]["reaches_edge"] and r["abs"]["reaches_edge"]
    add("K3 W = 196.885, C = 354.66 (the top binds first); the inequalities agree with p2_planck.window on all twelve; "
        "plausible i <= 98, j <= 196 (relative) or 98 (absolute); open toward weaker gravity: the plausible bulk is "
        "infinite", ok)
    wt = o["wts"]
    W = k["W"]
    ok = wt["ours"] == (1.0, 1.0) and wt["2a-min"] == (1.0, 1.0)
    ok &= abs(wt["2b"][0] - (W - 2) / W) < 1e-12 and abs(wt["2b"][1] - (W - 2) / W) < 1e-12
    ok &= abs(wt["2P"][0] - (W - 1) / W) < 1e-12 and abs(wt["2P"][1] - (W - 2) / W) < 1e-12
    ok &= abs(wt["2b+2P"][1] - (W - 4) / W) < 1e-12
    ok &= r["rel"]["weight_one_in_box"] > 1000 and all(weight(-n, -n, k, "rel") == 1.0 for n in (10, 100, 1000, 10 ** 6))
    add("K4 weights: 1 and 2a weigh 1; 2b (W-2)/W; 2P (W-1)/W relative, (W-2)/W absolute (Q3's 2 S0, 4 S0); infinitely "
        "many universes weigh 1, so the ensemble cannot be normalised by the theorem's conditions", ok)
    c2, c5 = o["cy"]["201"], o["cy"]["5D"]
    five = sorted(n for n in PP.MEMBERS if n not in POSITIONS)
    ok = c2["box"] == 12 and c2["in_box"] == five and c5["box"] == 18
    ok &= c2["E"] == {"order": 5, "algebra": 5, "geometry": 0, "information": 5, "statistics": 0}
    ok &= all(c2["predicted"][lg] == five for lg in ("order", "algebra", "information"))
    ok &= c2["predicted"]["geometry"] == [] and c2["predicted"]["statistics"] == []
    ok &= c5["in_box"] == ["2a+2P-min", "2a+2P-mirror"] and "2b+2P" not in c5["in_box"]
    ok &= c5["E"] == {"order": 8, "algebra": 8, "geometry": 3, "information": 5, "statistics": 0}
    ok &= sorted({(str(g), str(s_)) for _, g, s_ in c5["off_lattice"]["order"]}) == [("1/3", "-2/3"), ("5/3", "-4/3")]
    ok &= len(c5["off_lattice"]["order"]) == 6 and c5["off_lattice"]["statistics"] == []
    ok &= all(c["run"]["verdicts"] for c in (c2, c5)) and all(not c["audit"]["keys"] and not c["audit"]["onehot"]
                                                             for c in (c2, c5))
    add("K5 cypher: 201's basis -- order, algebra, information admit exactly the five compositions (E 5/5/0/5/0), geometry "
        "and statistics none; 5D basis -- box 18, 2b+2P outside, E 8/8/3/5/0, six admitted universes off the positions' "
        "lattice (G x 2^1/3 and 2^5/3); statistics admits nothing beyond the seven in either; no key, no one-hot", ok)
    un = o["unseen"]
    add("K7 unseen axes: the offset's ratio to the tension is ours in all twelve (to 1e-12) -- no position moves it; the "
        "matter law takes only the three computed values (ours, min, mirror)",
        all(abs(v - 1) < 1e-12 for v in un["ratios"].values()) and un["laws"] == list(LAW_ORDER))
    return res


MUTANTS = {"k4_wrong": "kappa5^4 taken as G sigma instead of G / sigma",
           "floor_sign": "the table-top floor read with the wrong sign (j - i reversed)",
           "numeric_order": "the cypher's axes ordered numerically, not away from ours",
           "offset_moves": "a position read as moving the offset's ratio"}


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
        print("  mutant %-11s %-60s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
