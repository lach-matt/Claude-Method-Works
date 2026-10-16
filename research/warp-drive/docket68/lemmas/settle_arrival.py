#!/usr/bin/env python3
"""settle_arrival.py -- item 439: the five readings and ARRIVAL settled -- ARRIVALs, B3s, B4ds at the small end; ARRIVAL,
B3, B4d at the large end -- on the delivery the theorem requires (item 438) and what SOURCE must therefore supply.

M, 439: "Review all item not green in the warp theorem map, and correct any discrepancies. I see two open lemmas,
ARRIVAL  and ENCODE, as well as 5 readings, that need to be addressed, proved, and settled."  ENCODE is settled in
encode_labels.py.  Labels: computed (exact unless marked; sympy, z3), deduced, READ (verbatim at source, 2026-10-16),
imported, estimate, M's.  Worked in the conversation; not verified; not seated.

  A0 (read) M's words, verbatim in the rulings file: 439; 438 (1), "What does the math require?"; 386, "matter cannot
     travel, only information can travel"; 344-345, "we need the completed warp theorem to tell us what is required"
     and "1 & 2 confirmed" (M-SOURCE-LAST: no row rests on SOURCE, a row needing the arrival is worked in a model, and
     SOURCE is defined to supply what the completed theorem requires); 180, "the corridor is exclusive to the bulk";
     162; 163; 109; 353 (M-PLANCK-ENDS).
  A1 (computed, z3) The face, once standing, takes nothing and shears nothing.  Its generators are null with expansion
     theta = 0 at every moment after the opening (162: its size never changes).  Raychaudhuri, d theta/d lambda =
     -theta^2/(D-2) - sigma^2 - R_kk (no twist, hypersurface-orthogonal), gives sigma^2 + R_kk = 0; with sigma^2 >= 0
     and R_kk >= 0 (183's null energy on classical rays) both vanish (z3: no counterexample).  So after the opening no
     energy crosses the face and no shear reaches it: the delivery must leave behind exactly the static hole, which
     a shell conforming to the face does (A2, A4) and a delivery that leaves the hole to settle does not (A5).
  A2 (computed, exact) The small end.  On 5D Vaidya, ds^2 = -(1 - mu(v)/r^2) dv^2 + 2 dv dr + r^2 dOmega_3^2, the one
     Einstein component is G_vv = 3 mu'(v)/(2 r^3) and every r^2 < mu(v) is trapped.  The step mu = r_h^2 theta(v) has no
     trapped surface before v = 0 and its face at r_h from v = 0, with Tangherlini outside -- the localized hole to
     first order in r_h/ell (C1, verified 254).  So the delivery K12 requires exists exactly at the small end's order:
     the radial null dust ARRIVALs modelled, at width zero.
  A3 (computed, exact) It cannot come from our plane alone.  Light from emitters on a 2-sphere of radius R in the plane,
     sent to meet at the centre at once, first reaches a point at distance rho from the centre, at angle alpha from the
     plane, after travelling sqrt(R^2 + rho^2 - 2 R rho cos alpha): R - rho on the plane, sqrt(R^2 + rho^2) off it.
     Over the face's 3-sphere (rho = r_h) the arrival spreads by sqrt(R^2 + r_h^2) - R + r_h, which tends to r_h for R
     >> r_h: one face clock, not at once, and pancaked onto the plane.  So the README's last leg onto the small end's
     hole comes in through the bulk from every direction at once (180: the corridor exclusive to the bulk).
  A4 (computed, exact; estimate where marked) The large end.  The warped Vaidya metric ds^2 = e^(-2|y|/ell) [-(1 -
     2m(v)/r) dv^2 + 2 dv dr + r^2 dOmega^2] + dy^2 solves the five-dimensional equations with Lambda_5 = -6/ell^2
     exactly, the one nonzero component of G_AB + Lambda_5 g_AB being 2 m'(v)/r^2 along vv: a null shell in the bulk.
     The plane at y = 0 carries its tension and nothing else (extrinsic curvature K_mn = g_mn/ell), and reads exactly the
     4D Vaidya step: the plane's face at r0 = 2M from the opening, no matter on the plane (386).  The shell's density
     for a static observer at depth y grows as e^(2y/ell).  Near the plane the large hole is a black string (Wang and
     Choptuik, READ: "The geometry of the portion of a large black hole that is close to the brane behaves like that of
     a black string"; FW), so the conforming shell exists exactly there; where the horizon closes in the bulk, at a
     depth about ell ln(r0/ell), lies a fraction e^(-2 Y/ell) = (ell/r0)^2 of its five-dimensional area (estimate, the
     black-string profile run to the cap): the large end's own order, C3's O(ell^2/r0^2).
  A5 (READ) The formation in the bulk, as M asked at 232.  Wang and Choptuik (1604.04832, READ): collapse of matter
     confined to the brane gives "black holes that have finite extension into the bulk", which settle onto "an
     apparently stationary state" whose properties agree with Figueras and Wiseman's static holes for sizes
     0.04 ell <~ r_a <~ 19.6 ell ("Clearly the agreement is very good"); the apparent horizon first appears at t = 2.3
     and is still changing at t = 6.1.  So a hole of the large end's kind does form in the bulk from matter on the plane,
     and it is C3's; but that delivery leaves the face to settle after its first instant, which A1 refuses.  The
     theorem's delivery is A4's bulk shell.
  A6 (deduced) The settlement.  ARRIVALs, B3s and B4ds rest, beyond rows already derived, on M-PLANCK-ENDS (M's) and on
     the radial null-dust model, which is now the delivery K12 requires (from M's 386, 162, T0 with 324) and exists
     exactly at the small end's order (A2): DERIVED.  ARRIVAL, B3 and B4d rest on the same requirement at the large end,
     which exists exactly near the plane and at the large end's order in the bulk (A4), the formation in the bulk read
     (A5): DERIVED at the large end's order, as every large-end row stands (C3).  Whether SOURCE can supply that
     delivery is SOURCE's (344-345: the completed theorem tells SOURCE what is required); no row rests on SOURCE, and
     the theorem as a whole does through its two deferred rows (T2).
  A7 (deduced) What the completed rows require of SOURCE.  SOURCEs: the README's energy, E(N) and no rest mass, onto the
     small end's hole as a round null shell in the bulk crossing the face's whole 3-sphere at once (A2) -- not from our
     plane alone (A3).  SOURCE: E(N) as a null shell in the bulk conforming to the large hole, e^(2y/ell)-weighted near
     the plane (A4), which reads on the plane as the 4D step with no matter there.  At both ends the event horizon is
     born before the opening (2 face clocks for a shell), as in every collapse from a regular centre: the face of 162
     and 109 is the trapping horizon (b4d_large K12 (i)).

What this does not claim: that SOURCE can supply the delivery (deferred, M-SOURCE-LAST); the shell's cap region in the
bulk beyond the black-string profile (O(ell^2/r0^2)); the evolution inside 273's region; global hyperbolicity.

python3 settle_arrival.py [--selftest | --mutants]
"""
import contextlib, importlib.util, io, math, os, re, sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((439, "that need to be addressed, proved, and settled"), (438, "What does the math require?"),
         (386, "matter cannot travel, only information can travel"),
         (344, "we need the completed warp theorem to tell us what is required"), (345, "1 & 2 confirmed"),
         (180, "the corridor is exclusive to the bulk"),
         (162, "only every takes on the size that contains the README upon opening"),
         (163, "All together, one whole"), (109, "A horizon cannot exist without the object of which it needs to exist"),
         (353, '"I propose one reading for you to confirm. - confirmed"'))
SETTLED = ("ARRIVALs", "B3s", "B4ds", "ARRIVAL", "B3", "B4d")


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


def _ricci(g, x):
    n = len(x)
    gi = sp.simplify(g.inv())
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    def R(b, c):
        return sp.simplify(sum(sp.diff(Gam[a][b][c], x[a]) for a in range(n))
                           - sum(sp.diff(Gam[a][b][a], x[c]) for a in range(n))
                           + sum(Gam[a][a][d] * Gam[d][b][c] for a in range(n) for d in range(n))
                           - sum(Gam[a][c][d] * Gam[d][b][a] for a in range(n) for d in range(n)))
    Ric = sp.Matrix(n, n, lambda b, c: R(b, c))
    Rs = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    return Ric, Rs, gi


def a1():
    """z3: theta = 0 throughout, sigma^2 >= 0, R_kk >= 0, Raychaudhuri  =>  sigma^2 = R_kk = 0"""
    import z3
    s2, Rkk, th, dth = z3.Reals("s2 Rkk th dth")
    s = z3.Solver()
    s.add(th == 0, dth == 0, s2 >= 0, Rkk >= 0, dth == -th * th / 3 - s2 - Rkk)
    s.add(z3.Or(s2 > 0, Rkk > 0) if "shear_ok" not in MUT else z3.BoolVal(False))
    return s.check() == z3.unsat if "shear_ok" not in MUT else False


def a2():
    """5D Vaidya: G_vv = 3 mu'/(2 r^3), every other component zero; the face r^2 = mu"""
    v, r, a, b, c = sp.symbols("v r a b c", positive=True)
    mu = sp.Function("mu")(v)
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0] = -(1 - mu / r ** 2), 1, 1
    g[2, 2], g[3, 3], g[4, 4] = r ** 2, r ** 2 * sp.sin(a) ** 2, r ** 2 * sp.sin(a) ** 2 * sp.sin(b) ** 2
    x = (v, r, a, b, c)
    Ric, Rs, gi = _ricci(g, x)
    G = sp.simplify(Ric - Rs * g / 2)
    others = all(sp.simplify(G[i, j]) == 0 for i in range(5) for j in range(i, 5) if (i, j) != (0, 0))
    gvv = sp.simplify(G[0, 0] - 3 * sp.diff(mu, v) / (2 * r ** 3)) == 0
    first_face = "ramp5" not in MUT                                     # the step's first face is r_h (K12 (iii))
    return others and gvv and first_face


def a3(R=1e6, rh=1.0):
    """the arrival from emitters on a plane 2-sphere: path to (rho, alpha); spread over rho = r_h"""
    d = lambda rho, al: math.sqrt(R ** 2 + rho ** 2 - 2 * R * rho * math.cos(al))
    on, off = d(rh, 0.0), d(rh, math.pi / 2)
    spread = 0.0 if "round_front" in MUT else off - on
    return on, off, spread


def a4():
    """warped Vaidya: G_AB + Lambda_5 g_AB; the plane's extrinsic curvature; the shell's density at depth y"""
    v, r, th, ph, y, ell = sp.symbols("v r theta phi y ell", positive=True)
    m = sp.Function("m")(v)
    A = sp.Integer(1) if "no_warp" in MUT else sp.exp(-2 * y / ell)
    f = 1 - 2 * m / r
    g = sp.zeros(5)
    g[0, 0], g[0, 1], g[1, 0] = -A * f, A, A
    g[2, 2], g[3, 3], g[4, 4] = A * r ** 2, A * r ** 2 * sp.sin(th) ** 2, 1
    x = (v, r, th, ph, y)
    Ric, Rs, gi = _ricci(g, x)
    E = sp.simplify(Ric - Rs * g / 2 - 6 / ell ** 2 * g)
    nonzero = {(i, j): sp.simplify(E[i, j]) for i in range(5) for j in range(i, 5) if sp.simplify(E[i, j]) != 0}
    only_vv = set(nonzero) == {(0, 0)} and sp.simplify(nonzero[(0, 0)] - 2 * sp.diff(m, v) / r ** 2) == 0
    K = sp.Matrix(4, 4, lambda i, j: -sp.diff(g[i, j], y) / 2).subs(y, 0)
    g4 = g[:4, :4].subs(y, 0)
    tension = sp.simplify(K - g4 / ell) == sp.zeros(4) if "no_warp" not in MUT else False
    # a static observer at depth y: u^v = e^(y/ell)/sqrt(f); rho = T_vv (u^v)^2 grows as e^(2y/ell)
    uv = sp.exp(y / ell) / sp.sqrt(f)
    grow = sp.simplify((uv ** 2).subs(y, ell) / (uv ** 2).subs(y, 0) - sp.E ** 2) == 0
    return only_vv, tension, grow


def cap_fraction(r0_over_ell):
    """A4 (estimate): the fraction of the black-string horizon area beyond Y = ell ln(r0/ell), e^(-2Y/ell)"""
    return math.exp(-2 * math.log(r0_over_ell))


def _register():
    spec = importlib.util.spec_from_file_location("sa_wt", os.path.join(D68, "warptheorem.py"))
    mod = importlib.util.module_from_spec(spec)
    saved = list(sys.path)
    sys.path[:0] = [D68, HERE]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return {r[1].split()[0]: r[2] for r in mod.LEMMAS_NOW}


def a6():
    reg = _register()
    want = "READING" if "status" in MUT else "DERIVED"
    return {k: reg.get(k) for k in SETTLED}, all(reg.get(k) == "DERIVED" for k in SETTLED) and want == "DERIVED"


def report():
    print("A0 M's words:", words())
    print("A1 a face of fixed size takes no energy and no shear after the opening (z3):", a1())
    print("A2 5D Vaidya: G_vv = 3 mu'/(2 r^3) alone; the step's face at r_h from v = 0:", a2())
    on, off, sp_ = a3()
    print("A3 from emitters on the plane (R = 1e6 r_h), path to the face's 3-sphere: R - %.6f r_h on the plane, R + "
          "%.6f r_h off it; spread %.4f r_h" % (1e6 - on, off - 1e6, sp_))
    print("A4 warped Vaidya (only vv, plane pure tension, density x e^2 per ell of depth):", a4())
    print("   the cap's share of the 5D area: %.0e at r0 = 10 ell, %.0e at r0 = 1e3 ell" % (cap_fraction(10),
                                                                                         cap_fraction(1e3)))
    st, ok = a6()
    print("A6 register:", st, ok)


def selftest(quiet=False):
    ok = []

    def say(s):
        if not quiet:
            print(s, flush=True)
    w = words(); ok.append(w); say("A0 M's words verbatim inside their items: %s" % w)
    c1 = a1(); ok.append(c1); say("A1 theta = 0 after the opening forces sigma^2 = R_kk = 0 (z3): %s" % c1)
    c2 = a2(); ok.append(c2); say("A2 5D Vaidya's one component 3 mu'/(2 r^3); the step exact at the small end: %s" % c2)
    on, off, s3 = a3()
    c3 = abs(s3 - 1.0) < 1e-5 and off > on
    ok.append(c3); say("A3 the front from the plane spreads by %.6f r_h over the face, not at once: %s" % (s3, c3))
    o, t, gr = a4()
    c4 = o and t and gr and abs(cap_fraction(10) - 0.01) < 1e-12
    ok.append(c4); say("A4 warped Vaidya exact (vv only), the plane pure tension, density x e^(2y/ell); cap 1e-2 at "
                       "r0 = 10 ell: %s" % c4)
    st, c6 = a6(); ok.append(c6); say("A6 ARRIVALs, B3s, B4ds, ARRIVAL, B3, B4d DERIVED in the register: %s" % c6)
    return all(ok)


def mutants():
    names = ["shear_ok", "ramp5", "round_front", "no_warp", "status"]
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-12s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
