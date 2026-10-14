#!/usr/bin/env python3
"""close_small.py -- item 335: the CLOSE row at the family's small end, on the one-way object.  M: "I agree" (to the
board's recommendation that CLOSE be worked next, since M-HOLD-IS-THE-FACE, 334, makes the hold last exactly as long as
the write and nothing yet ends our face when the write is done).  The question, posed in the record's own terms: what
ends our face when the write is done, and what does ending it cost.  Worked in the conversation (computed with sympy,
exact where marked; READ where marked; deduced where marked; not verified by a separate session; not seated);
2026-10-12.

  K0 (read) The words the row rests on, verbatim in the rulings file: 109, "A horizon cannot exist without the object of
     which it needs to exist"; 115 (a), "It ends; energy moved"; 136 (2), "released at position two at the closing of
     the horizon"; 136 (3), "It can only facilitate transport, not indefinitely hold something"; 158 (2), "Exactly as
     long as the write needs"; 160, "the corridor and the opening are the same object"; 162, "The throat doesn't change
     size"; 183, "Yes: never violated as a pair", with (Z) seated as "a negative member paired along the same light
     rays is the appearance"; 276, "The passage is one-way in all aspects"; 318, "For the math"; 334, "For you — one
     reading to confirm or overrule - confirmed"; 335, "I agree".
  K1 (computed, exact) The flux that moves a face, in five dimensions.  On our side, the ingoing Vaidya form of the hole,
     -(1 - mu(v)/r^2) dv^2 + 2 dv dr + r^2 dOmega_3^2: the Einstein tensor's only component is G_vv = 3 mu'(v)/(2 r^3)
     (computed from the metric).  On position 2's side, the outgoing form, -(1 - mu(u)/r^2) du^2 - 2 du dr + r^2
     dOmega_3^2: G_uu = -3 mu'(u)/(2 r^3).  So the one loss of mass reads as a negative inflow at our face and a positive
     outflow at position 2's -- the record's CLOSE-FLUX K1 (four dimensions there) carried to the small end, and M's 132,
     "a black hole in and a white hole out".  The large end's four-dimensional forms, G_vv = 2 m'(v)/r^2 and G_uu =
     -2 m'(u)/r^2, are computed as the control.
  K2 (READ; computed) Which face can shrink.  READ: Hayward, gr-qc/9303006v3, Theorem 3 (the second law): "If the null
     energy condition holds, the area form of a future outer or past inner trapping horizon is non-decreasing, and the
     area form of a past outer or future inner trapping horizon is non-increasing"; the laws are quasi-local ("requires
     no global assumptions") -- so they hold whether or not our face is an event horizon (CLOSE-FLUX K3's split does not
     reach them); and the paper sets aside distributional stress, "since this can produce artificial discontinuous
     jumps in the trapping horizon".  On the five-dimensional Vaidya forms: the marginal surfaces sit at r^2 = mu and
     kappa = f'(r_h)/2 = 1/r_h > 0 (computed); with theta_+ proportional to f the outer condition L_- theta_+ < 0 is
     that sign (deduced) -- the corridor's horizon, not extremal (stability S6, item 331); the area ~ mu^(3/2) changes as
     mu', the sign of the null flux (computed).  Our face
     is future outer: under non-negative null energy it cannot shrink.  Position 2's is past outer: it shrinks as it
     releases positive energy.  The record's escape for our face (close_object O2: "degenerate, so Hayward's
     outer-horizon law does not bind") rested on kappa = 0 and is gone (its item-331 note).
  K3 (computed, exact) Where the flux must come from.  The five-dimensional Misner-Sharp mass, 1 - mu_MS/r^2 = g^ab
     d_a r d_b r, equals mu(v) on the ingoing form, and d_v mu_MS = (2 r^3/3) G_vv at every r: the mass inside any sphere
     of our exterior changes only by the null flux through that sphere (computed).  So for our face to end with nothing
     carried out of our universe -- one-way, nothing leaves our face (276), and the energy moved, not radiated (115 (a))
     -- a total -E must cross every sphere of our exterior inward.  The ingoing surface v = v_end reaches r -> infinity
     at t = v_end - r* -> -infinity (computed: r* diverges with r), so that flux is present in our exterior at every
     radius before the closing, back to our past null infinity -- and since r* is unbounded, at large enough R it
     passes before the opening itself: the closing's -E would be on its way in before the corridor opened (deduced
     from the same limit).  Emitted instead from a finite radius R_e, the mass
     outside R_e stays E unless +E leaves R_e outward, into our universe (the flux law at R_e) -- and then the energy is
     not moved.  Either way the closing's negative member lies in our exterior, in the closing's causal past: the
     corridor cannot send it, since nothing leaves our face (deduced).
  K4 (computed, exact) What 162, 158 (2) and 334 require of it.  The size fixed from the opening until the write ends,
     then no face: mu(v) = mu0 Theta(v_end - v), so G_vv = -(3 mu0/(2 r^3)) delta(v - v_end) -- a null shell, and its
     energy through any sphere, (1/kappa5^2) x 2 pi^2 r^3 x (-3 mu0/(2 r^3)) with kappa5^2 = 8 pi G5, is exactly
     -3 pi mu0/(8 G5) = -E at mu0 = r_h^2 (computed; c = 1): the closing is a shell of exactly -E at the write's end.
  K5 (computed) Hawking's emission ends the face without any of K3's cost, but on its own clock: our side's life is
     8.57e14 clocks, 1.28e10 times the write's floor (hold_small, C5 U4), and its energy goes to our infinity, ours.  So
     it fails 158 (2) with 334 by ten orders and is not 115 (a)'s move.
  K6 (computed) The pairing 183 asks for.  On the glued one-way object (270 (a), 273 (a): (U, V) -> (-U, -V)) an ingoing
     ray V = V0 > 0 runs from our exterior (U < 0) through our face into our interior (U > 0), and is glued to V = -V0 in
     position 2's past interior (U < 0), leaving through position 2's face into position 2's exterior (U > 0, V < 0)
     (computed: the region labels along the ray).  The rays position 2's white hole releases along are those same glued
     rays.  So the closing's -E at our face and the release's +E at position 2's face can lie on one ray each: net zero
     along every ray, 183 kept and the negative 117/120's appearance; the sign turns in the quantum region, which gives
     up classical GR (273).  But the -E is pointwise negative in our exterior along the whole shell, outside the quantum
     region -- 318's reading, which confines the passage's negative to that region, does not cover it (deduced).
  K7 (deduced) The fork.  Our face ends at the write's end with E moved to position 2 (109, 115 (a), 136 (2), 158 (2)
     with 334, one-way 276) only if our exterior carries the closing's -E from its own past (K3, K4): 183 is kept net per
     ray (K6), but the negative is not caused by the corridor and is not confined to the quantum region.  Without it,
     one of the rulings gives way: keep the energy in our universe and the face ends by Hawking emission after its life
     (K5) -- 158 (2)'s timing and 115 (a)'s move given up; or the face outlives the write.  The five-dimensional route
     (B4a's one end) does not escape: K1-K3 are computed in five dimensions, and with the two sheets coincident (275)
     whatever carries E at position 2 would gravitate at the same place in the bulk, which 276's one-way gravity forbids
     our sheet to read (deduced).
  K8 (the cypher NOT-RUN, stated) Which ruling gives way, or whether our exterior carries the -E, is a ruling the record
     does not give, not a configuration to classify; K1-K6 are identities, and an index of the four outcomes over (ends
     at the write, energy moved, one-way, 183 kept) would carry the answer as its own column, a key (211).  Put to M.
  K9 (item 336; read, computed) M's answer, verbatim: "I think it is B" -- seated as M-ENERGY-STAYS. Our face's energy E
     stays in our universe: the face closes by Hawking emission over the hole's life, 8.57e14 clocks, 1.28e10 times the
     write's floor (K5), its energy radiated into our universe -- no negative null energy in our exterior beyond the
     emission's own, and nothing of E crosses. 158 (2) no longer times the hold: the face standing (334) lasts the life.
     115 (a)'s "energy moved" is given up for position 1's horizon, which still ends (109). Position 2's face, past
     outer (K2), closes within 33.6 clocks (c_junction J1), its release position 2's own energy (110, 111 (a), 240): the
     energy plane 2 read while its face held, which the build uses exactly. What crosses is the README. So the CLOSE row
     at the small end is closed on M's ruling (computed: the life and the floor, K5; the open period, c_junction J1).
     [Items 387-389: J1's 33.6 clocks is the period where the junction rises: 139 (1)'s quarter, or any sigma2 below
     ours (junction_own G3). At a destination at its own sigma equal to ours there is no junction. Position 2's face
     then ends 2 clocks after the README's last part -- the reflection of our face's birth, 109 (junction_own G8). Either
     way it closes, and K9 stands.]
     [Item 390, M: "it closes when there is nothing contained within the corridor" -- M-CLOSES-WHEN-EMPTY, the closing
     at our sigma ruled. The face closes as the README's last part leaves the anti-trapped region (junction_own G10).]

What this does not claim.
  - That a -E shell can be prepared, or what would prepare it: K3 says only where it must be.
  - The quantum region's form, or how the sign turns along the glued ray (273: classical GR given up there).
  - The large end beyond K1's control: there the record's CLOSE row stands (close_cypher, close_object).
  - Gravitational radiation in the bulk: spherical symmetry is assumed in K1-K4, as the record's hole has it.

Imports hold_small.py, write_small.py and c_junction.py by path.  Stdlib + sympy.
python3 close_small.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ("A horizon cannot exist without the object of which it needs to exist", "It ends; energy moved",
         "released at position two at the closing of the horizon",
         "It can only facilitate transport, not indefinitely hold something", "Exactly as long as the write needs",
         "the corridor and the opening are the same object", "The throat doesn't change size",
         "Yes: never violated as a pair", "a negative member paired along the same light rays is the appearance",
         "The passage is one-way in all aspects", "For the math",
         "For you — one reading to confirm or overrule - confirmed", "I agree")
v, u, r, th, ph, ps, t = sp.symbols("v u r theta phi psi t")
mu = sp.Function("mu")


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), HERE, D68]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def einstein(g, X):
    """the Einstein tensor G_ab of the metric g in coordinates X (exact)"""
    n = len(X)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                             for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]

    def ric(b, c):
        return sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                               + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a] for d in range(n))
                               for a in range(n)))
    R = sp.Matrix(n, n, lambda b, c: ric(b, c))
    Rs = sp.simplify(sum(gi[a, b] * R[a, b] for a in range(n) for b in range(n)))
    return sp.simplify(R - Rs * g / 2)


def vaidya(dim, side):
    """the ingoing (our face) or outgoing (position 2's face) Vaidya form of the dim-dimensional hole"""
    w = v if side == "in" else u
    sgn = 1 if side == "in" else -1
    if MUT.get("flux_sign"):
        sgn = -sgn                                          # the mutant: ingoing and outgoing forms exchanged
    if dim == 5:
        f = 1 - mu(w) / r ** 2
        X = [w, r, th, ph, ps]
        g = sp.diag(-f, 0, r ** 2, r ** 2 * sp.sin(th) ** 2, r ** 2 * sp.sin(th) ** 2 * sp.sin(ph) ** 2)
    else:
        f = 1 - 2 * mu(w) / r
        X = [w, r, th, ph]
        g = sp.diag(-f, 0, r ** 2, r ** 2 * sp.sin(th) ** 2)
    g[0, 1] = g[1, 0] = sgn
    G = einstein(g, X)
    others = [sp.simplify(G[i, j]) for i in range(len(X)) for j in range(i, len(X)) if (i, j) != (0, 0)]
    return dict(G00=sp.factor(G[0, 0]), others_zero=all(o == 0 for o in others), f=f, w=w, g=g)


def k2():
    """K2: the marginal surfaces, the outer condition and the area's rate on the 5D ingoing form"""
    mu0, rh = sp.symbols("mu0 r_h", positive=True)
    f = 1 - mu0 / r ** 2
    marginal = sp.solve(sp.Eq(f, 0), r)
    fprime = sp.diff(f, r).subs(r, sp.sqrt(mu0))                   # outer: L_- theta_+ < 0 <-> f'(r_h) > 0
    kappa = sp.simplify(fprime / 2)
    if MUT.get("our_face_past"):
        kappa = -kappa                                           # the mutant: our face read as past (inner) type
    area = 2 * sp.pi ** 2 * mu(v) ** sp.Rational(3, 2)
    rate = sp.simplify(sp.diff(area, v) / sp.diff(mu(v), v))      # dA/dv per mu'
    return dict(marginal=marginal, kappa=kappa, rate=rate, outer=bool(sp.simplify(kappa - 1 / sp.sqrt(mu0)) == 0))


def k3():
    """K3: the 5D Misner-Sharp mass on the ingoing form and its flux law; the shell's far past"""
    f = 1 - mu(v) / r ** 2
    # g^ab d_a r d_b r on -f dv^2 + 2 dv dr: g^{rr} = f
    grr = f
    mu_ms = sp.simplify(r ** 2 * (1 - grr))
    G_vv = 3 * sp.diff(mu(v), v) / (2 * r ** 3)
    law = sp.simplify(sp.diff(mu_ms, v) - (2 * r ** 3 / 3) * G_vv) == 0
    if MUT.get("local_source"):
        law = False                                              # the mutant: a source with no partner admitted
    rs = sp.Symbol("r_s", positive=True)                         # tortoise r* for f = 1 - r_h^2/r^2, r_h = 1
    rstar = sp.integrate(1 / (1 - 1 / rs ** 2), rs)
    far = sp.limit(rstar, rs, sp.oo)
    return dict(mu_ms=mu_ms, law=law, far=far)


def k4():
    """K4: the step 162 and 158 (2) with 334 require, and its energy"""
    mu0, vend, G5 = sp.symbols("mu0 v_end G5", positive=True)
    step = mu0 * sp.Heaviside(vend - v)
    d = sp.diff(step, v)                                          # -mu0 delta(v - v_end)
    Gvv = sp.simplify(3 * d / (2 * r ** 3))
    kap5 = 8 * sp.pi * G5
    energy = sp.integrate(sp.simplify(Gvv * 2 * sp.pi ** 2 * r ** 3 / kap5), (v, -sp.oo, sp.oo))
    E = 3 * sp.pi * mu0 / (8 * G5)                                # the Komar mass at mu0 = r_h^2 (c = 1)
    if MUT.get("shell_half"):
        energy = energy / 2                                      # the mutant: half the mass moved
    return dict(Gvv=Gvv, energy=sp.simplify(energy), E=E, exact=sp.simplify(energy + E) == 0)


def k5():
    """K5: the life against the write's floor (hold_small, write_small)"""
    H = _load(os.path.join(HERE, "hold_small.py"), "cs_hold")
    life = H.l5_checks()["life_clocks"]
    W = _load(os.path.join(HERE, "write_small.py"), "cs_ws")
    floor = W.head_clocks()
    if MUT.get("life_write_scale"):
        life = floor                                             # the mutant: the hole read as living one write
    return dict(life=life, floor=floor, ratio=life / floor)


def k6():
    """K6: the glued ray's regions; (U, V) -> (-U, -V) through the quantum region"""
    def region(U, V):
        return {(-1, 1): "our exterior", (1, 1): "our interior", (-1, -1): "position 2's past interior",
                (1, -1): "position 2's exterior"}[(1 if U > 0 else -1, 1 if V > 0 else -1)]
    V0 = 1
    path = [region(U, V0) for U in (-2, -1, 1, 2)]               # ingoing at V = V0, U increasing
    glue = (lambda U, V: (U, V)) if MUT.get("no_glue") else (lambda U, V: (-U, -V))
    U1, V1 = glue(2, V0)
    path += [region(U, V1) for U in (U1, U1 / 2, -U1 / 2, -U1)]  # continue with U increasing after the glue
    release = region(1, V1)                                      # position 2's release leaves along V = -V0
    E = sp.Symbol("E", positive=True)
    net = -E + E                                                 # the closing's -E and the release's +E on one ray
    return dict(path=path, release=release, net=net)


def k9(k5r):
    """K9 (item 336): the closing at the small end on M-ENERGY-STAYS -- our face by Hawking emission over its life,
    position 2's face within its open period (c_junction J1)"""
    CJ = _load(os.path.join(HERE, "c_junction.py"), "cs_cj")
    open2 = CJ.example(CJ.seen())["t_full"]
    close_clocks = k5r["floor"] if MUT.get("close_at_write") else k5r["life"]   # the mutant: closing at the write
    return dict(close_clocks=close_clocks, open2=open2)


def compute():
    k5r = k5()
    return dict(in5=vaidya(5, "in"), out5=vaidya(5, "out"), in4=vaidya(4, "in"), out4=vaidya(4, "out"),
                k2=k2(), k3=k3(), k4=k4(), k5=k5r, k6=k6(), k9=k9(k5r))


def report(o):
    print("close_small.py -- the CLOSE row at the small end, on the one-way object (item 335)\n")
    print("K1 5D ingoing G_vv = %s (others zero: %s); outgoing G_uu = %s; control 4D: %s, %s"
          % (o["in5"]["G00"], o["in5"]["others_zero"], o["out5"]["G00"], o["in4"]["G00"], o["out4"]["G00"]))
    a = o["k2"]
    print("K2 marginal surfaces r = %s; kappa = %s (outer, our face future outer); dA/dv = (%s) mu'" % (
        a["marginal"], a["kappa"], a["rate"]))
    b = o["k3"]
    print("K3 Misner-Sharp mu_MS = %s; d_v mu_MS = (2 r^3/3) G_vv: %s; r* -> %s as r -> infinity" % (
        b["mu_ms"], b["law"], b["far"]))
    c = o["k4"]
    print("K4 the step's G_vv = %s; its energy %s = -E: %s" % (c["Gvv"], c["energy"], c["exact"]))
    d = o["k5"]
    print("K5 life %.3g clocks against the write's floor %.0f: %.3g x" % (d["life"], d["floor"], d["ratio"]))
    e = o["k6"]
    print("K6 the glued ray: %s; the release leaves into %s; net along the ray %s" % (" -> ".join(e["path"]),
                                                                                         e["release"], e["net"]))
    g = o["k9"]
    print("K9 (item 336) M-ENERGY-STAYS: our face closes after %.3g clocks (Hawking emission, the energy ours); "
          "position 2's face within %.2f clocks" % (g["close_clocks"], g["open2"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("K0 M's words verbatim in the rulings file: 109, 115 (a), 136 (2)-(3), 158 (2), 160, 162, 183 with (Z), 276, "
        "318, 334, 335", all(w in rul for w in WORDS))
    mp = sp.Derivative(mu(v), v)
    add("K1 5D: the ingoing form's only Einstein component G_vv = 3 mu'/(2 r^3); the outgoing G_uu = -3 mu'/(2 r^3) "
        "-- mass falling is a negative inflow at our face, a positive outflow at position 2's; control 4D 2 m'/r^2",
        sp.simplify(o["in5"]["G00"] - 3 * mp / (2 * r ** 3)) == 0 and o["in5"]["others_zero"]
        and sp.simplify(o["out5"]["G00"] + 3 * sp.Derivative(mu(u), u) / (2 * r ** 3)) == 0
        and sp.simplify(o["in4"]["G00"] - 2 * mp / r ** 2) == 0
        and sp.simplify(o["out4"]["G00"] + 2 * sp.Derivative(mu(u), u) / r ** 2) == 0)
    a = o["k2"]
    mu0 = sp.Symbol("mu0", positive=True)
    add("K2 (READ Hayward Thm 3; computed) the marginal surface at r^2 = mu, outer exactly when kappa = 1/r_h > 0, the "
        "area's rate 3 pi^2 mu^(1/2) mu' -- our face future outer, unable to shrink under non-negative null energy",
        sp.sqrt(mu0) in a["marginal"] and a["outer"]
        and sp.simplify(a["rate"] - 3 * sp.pi ** 2 * sp.sqrt(mu(v))) == 0)
    b = o["k3"]
    add("K3 the 5D Misner-Sharp mass is mu(v) and changes only by the null flux through each sphere; the ingoing shell "
        "reaches r -> infinity in the far past (r* diverges)", sp.simplify(b["mu_ms"] - mu(v)) == 0 and b["law"]
        and b["far"] == sp.oo)
    c = o["k4"]
    add("K4 162 and 158 (2) with 334: the step mu0 Theta(v_end - v) is a null shell of exactly -E, E = 3 pi mu0/(8 G5)",
        c["exact"])
    d = o["k5"]
    add("K5 Hawking's emission ends the face only after its life, 8.57e14 clocks, 1.28e10 times the write's floor",
        "%.3g" % d["life"] == "8.57e+14" and "%.3g" % d["ratio"] == "1.28e+10")
    e = o["k6"]
    add("K6 the glued ray runs our exterior -> our interior -> position 2's past interior -> position 2's exterior, "
        "where the release leaves; the closing's -E and the release's +E net zero along it",
        e["path"][0] == "our exterior" and e["path"][2] == "our interior" and "position 2's past interior" in e["path"]
        and e["path"][-1] == "position 2's exterior" and e["release"] == "position 2's exterior" and e["net"] == 0)
    rul336 = rul.split("336. **")[-1]
    add("K9 (item 336) M's answer \"I think it is B\", seated M-ENERGY-STAYS: our face closes by Hawking emission after "
        "its life, 1.28e10 writes, the energy ours; position 2's face within 33.6 clocks",
        "I think it is B" in rul336 and "Seated as M's: M-ENERGY-STAYS" in rul336 and d["ratio"] > 1e10
        and o["k9"]["close_clocks"] == d["life"] and "%.1f" % o["k9"]["open2"] == "33.6")
    return res


MUTANTS = {"close_at_write": "our face read as closing at the write's end, against M-ENERGY-STAYS (K9; item 336)",
           "flux_sign": "the ingoing and outgoing forms exchanged: a falling mass read as positive inflow (K1)",
           "our_face_past": "our face read as a past (white-hole) face, free to shrink under positive energy (K2)",
           "local_source": "a negative source at our face with no partner admitted (K3)",
           "shell_half": "half the mass moved at the closing (K4)",
           "life_write_scale": "the hole read as living one write (K5)",
           "no_glue": "the one-way object read without the (U, V) -> (-U, -V) gluing (K6)"}


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    kk = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (kk, len(r_)))
    return kk == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = sorted({n.split()[0] for n, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-17s %-80s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
