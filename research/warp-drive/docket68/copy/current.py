#!/usr/bin/env python3
"""current.py -- DOCKET 68, M-RULINGS items 125-131 (X5-X6 verified 2026-10-07): the README corridor's coefficients evaluated with exact values,
from our current state outward.  Deduced and computed; verified once; not seated.  Write-up: CURRENT.md.

M's words (verbatim in the rulings file): item 125 "We cannot use general coefficients for this work. We must always
avoid that debt by evaluating the coefficient in full and calculate using it exact values." (M-EXACT-VALUES); item 127
"1 - yes" (H-PLANES-COINCIDE) and "The coefficient value is the difference of that value in a counterfactual universe
and its value in our current universe, added to the value of our current universe" (H-COEFF-FROM-CURRENT).

INPUTS.  h, c exact (SI 2019); G = 6.6743e-11 (CODATA 2018, u_r 2.2e-5).  N = 2742570311524972 bits is the board's
core README (chain.py's core_bits): a float, faithful.identity_core() = synapse density x bits per synapse x
H_GREY_VOLUME_MM3 = 5e5, a volume the code marks "H-GREY-VOLUME, NAMED-NOT-READ, illustrative" (H-CORE-README, the
board's).  Under item 130 N is the user's input to the device for each trip, read from the object being moved
(H-N-IS-INPUT): the board's core is an example of an input, and every result is a formula in the input N with its
coefficients evaluated exactly -- m = 3.79592555457311e-36 m x sqrt(N), E_min = 4.59404002423570e8 J x sqrt(N).
First written "N's value is OPEN" (item 108).  First written "EXACT INPUTS ...
N = 2742570311524972".  Through chain.py's exact coefficients: E_min = sqrt(N h c^5 ln2/(8 pi^2 G)), r_min = sqrt(N h G
ln2/(2 pi^2 c^3)), and the pull m = G E_min/c^4 = r_min/2 (PLANE.md point 2).

WHAT THE WORK FINDS
  X1 THE PULL AT THE BOARD'S N.  m = 1.98790932853678e-28 m; u_r 1.1e-5 is G's share only (m goes as sqrt(N)).  chain.py's
     bisected floor solves the same equation by a second implementation and agrees to 3.06e-10 -- the size of nopath's
     rounded hbar (1.054571817e-34) against h/2pi, not noise.  First written "two routes agree".
  X2 THE THROAT FROM A CURRENT STATE -- THE BOARD'S CANDIDATE, AND ITS CONFLICT.  The candidate (H-CURRENT-IS-
     SCHWARZSCHILD; asked): r0 = 3m/2 + Delta, the no-throat member of eq. (17) -- Bronnikov-Kim p.4: "The Schwarzschild
     metric is restored from (17) in the special case r0 = 3m/2".  But at fixed m that member is a singular black hole of
     m c^2/G = 0.2677 kg with a horizon at 2m, not empty space -- against M's item 109, "A horizon cannot exist without
     the object of which it needs to exist" -- and it keeps m at its counterfactual value; m's current value is OPEN.
     Alternatives, named: (a) the current state is flat (m = 0, no throat): then G_kk = -E^2 r0/r^3, also linear in the
     difference, but each leg is -4E/(3 r0), unbounded as r0 -> 0 -- the finite limit -4E/(3m) belongs to the
     candidate's path only; (b) m and r0 both move, a two-dimensional difference; (c) outward is two-sided: Delta < 0
     gives G_kk > 0; the horizon side comes from PLANE.md's window, not from item 127.  Delta = 0 is also a change of
     topology (a singular hole against a throat): the candidate starts at the family's boundary.  On the candidate,
     G_kk = -4 Delta E^2/(r (2r - 3m)^2) with the board's m inserted -- "exactly the difference" is M's identity
     (current + (cf - current) = cf with current 0), STRUCTURAL.
  X3 THE PASSAGE ON THE CANDIDATE'S PATH.  Per leg, coin.py's closed form at the board's m: the limit -4E/(3m) =
     -6.70721402728537e27 per metre times E in metres (geometric: E -> G E/c^4), and moving outward
         leg(Delta) = -(4E/3m) [1 + (Delta/3m) ln(Delta/6m) + O((Delta/m)^2 ln(Delta/m))]
     hand-derived and checked against the closed form at delta = 1e-8 (a wrong constant, ln(delta/3), fails); coin.py's
     quadrature checks the closed form at five Delta at SI scale -- floating-point robustness and the import, since the
     leg scales exactly as 1/lambda.  For the candidate E = E_min/N = 8.772 J, G E/c^4 = 7.248e-44 m and the
     current-state limit per leg is -4.86e-16 (dimensionless; E is also the affine normalization, so only signs and
     ratios are free of it).  First written "(sympy series, checked)", and "E per metre" without E's unit.
  X4 COINCIDING PLANES: NOT SHOWN.  On an empty umbilic plane the null stress at y = 0 totals zero (K_kk = 0 there,
     STRUCTURAL: it follows from build()'s input K = -a q and k null).  The junction of two sheets at one place is not
     closedbulk.py's B3 (there is no bulk gap between them) and is not computed.  The board's two-sheet model put at one
     place -- opposite tensions, so K = 0 -- fails the bulk's own yy constraint unless a = 0 (computed).  The plane's
     tension, and the 4D G that sets m, depend on k and kappa.  First written "the device needs no k and no kappa" --
     withdrawn.
  X5 THE TOTAL MINUS THE PULL (item 129: "the corridor is a bridge, so it adds nothing to either position").  In
     plane.py's own masses, ADM = m/4 + r0/2 and the pull (Komar) = m, so at r0 = 3m/2 + Delta the total exceeds the pull
     by Delta/2 (STRUCTURAL: PLANE.md point 4's Penrose gap) -- exactly the integral of eq. 18's tidal density outside
     the horizon; BK p.1 calls E_mn "the tidal SET ... Due to its geometric origin", p.2 "the most natural 'matter'
     supporting wormholes" (READ by the verifier).  Two readings of "adds nothing": (i) no matter -- every member of eq. (17)
     has tau = 0 on the plane (escape.py S3), so this holds already; (ii) no mass beyond what is already there -- if the
     pull is the carried energy, which belongs to the matter already present (H-CURRENT-HAS-MATTER), the corridor adds
     Delta/2 and "nothing" forces Delta = 0, where eq. (17) has no throat: in reading (ii) Bronnikov-Kim's family hosts
     the bridge only at its edge (item 82: the boundary).  Both of the board's current states are ruled out by item 129
     (a 0.2677 kg hole that is not there; empty space).
  ITEM 130.  M: reading (i), "no added matter" -- every member of eq. (17) already has tau = 0, so it does not fix
     Delta.  "a black hole is not matter, it is what the mouth at position 1 looks like. It's observed mass appears
     negative only from the outside of the horizon."  In eq. (17) every gravitational mass read from outside a horizon
     member is positive -- the pull m > r0/2 > 0, the total m + Delta/2, the light-bending mean of the two; a negative
     total needs m < -2 r0, which has no horizon (plane.py's zero-total member).  So "negative from outside" is not
     eq. (17)'s gravitational mass; the board's candidate is PLANE.md's apparent mass = carried - defined (item 107).
  ITEM 131.  "strike that statement. I meant the gravitational pull."  The board reads it as striking item 130's
     "observed mass appears negative" (the board's reading); read instead as keeping "appears negative" for the pull,
     eq. (17) contradicts it -- outside a horizon member the pull m, the total m/4 + r0/2 and the light-bending mean are
     positive; the pull is negative iff m < 0, the mean iff m < -2 r0/5, the total iff m < -2 r0, none with a horizon
     (asked).  And "the throat size only needs to carry the binary information defining the object in transit, so the
     size of the throat is dependent on the size of the README in its most simplistically exact  binary code form".
  X6 THE THROAT SIZED BY THE README.  Read as the least throat that carries N bits (the board's: H-THROAT-AT-BOUND, with
     H-NECK-HOLDS and H-STRONG-BOUND on a surface that is not a horizon -- Bousso's extrapolation, CHAIN.md): 4 pi r0^2 =
     N A_bit, A_bit = 2 h G ln2/(pi c^3) = 4 l_P^2 ln2, so r0 = r_min(N) = 7.59185110914622e-36 m x sqrt(N).  A horizon
     holds N whenever 2m >= r_min; equality is the floor m = E_min, from wall 4's hypotheses (one E_min(N) per trip:
     H-PULL-IS-COST, H-DEVICE-SIZES, H-HORIZON-HOLDS, H-STRONG-BOUND), not from holding alone.  So:
       AT THE FLOOR r0 = 2m (STRUCTURAL: one bound on two surfaces): the boundary member, a degenerate (extremal) horizon
       at the throat -- g_tt = x^2/(2m + x^2), zero surface gravity (Hawking T = 0; the horizon's own Komar charge -> 0,
       so the whole pull is the tidal stress outside), the throat infinitely far at fixed t (g_xx = 4m^2/x^2 + ...), the
       null leg finite, -(4E/3m)[1 - (sqrt3/6) ln(2 + sqrt3)].  g_xx > 0 for every x != 0: x is never a time direction,
       so PLANE.md point 1's one-way mechanism (the throat a moment between two horizons) is GONE there -- in conflict
       with H-CORRIDOR-HORIZON's computed mechanism; item 106's two holds become one surface, and item 109's ending
       horizon is that surface.  BK pp.3-4 (READ by the verifier): eq. 17 is a wormhole "for any r0 > 2m >= 0"; r0 = 2m
       is excluded and is not a BK throat (a double zero); BK's own example 3, "r0 = 2m leads to the extreme
       Reissner-Nordstrom black hole metric".  Simpson-Visser 1812.07114v3 (READ by the verifier): a = 2m is "a one-way
       wormhole with an extremal null throat" (p.3), "only one-way traversable" (p.4) -- an analogue; eq. 17's own causal
       structure is OPEN, as are stability and fine-tuning (a measure-zero member).  The total 5m/4 is PLANE point 2's
       upper endpoint; Delta/2 = m/4 is eq. 18's tidal energy outside the horizon.
       ABOVE THE FLOOR (floor < m < 4/3 floor) r0 = r_min lies inside the horizon: a horizon member of PLANE point 1's
       kind, the horizon holding more than N (PLANE point 3's interval, restored by item 131).
     First written "With the horizon also holding N ..., r0 = 2m EXACTLY" and "Delta: fixed at m/2" -- an over-claim.
  WHAT STAYS A COEFFICIENT.  N, now the input (item 130); m's current value; Delta and its side; E and its normalization; the tension's
  sign (H-OUR-TENSION; RS1 puts our atoms on the negative-tension sheet, BULK.md); k and kappa (through the tension and
  the 4D G); the coinciding junction.

NAMED HYPOTHESES
  M's: M-EXACT-VALUES (125); H-PLANES-COINCIDE, H-COEFF-FROM-CURRENT (127); H-COLOCATED-REALIZATION,
    H-SHORTEST-DISTANCE (126); H-HORIZON-NEEDS-OBJECT (109); H-README-AS-NEEDED (108); the horizon members' window.
  M's, items 129-131: H-CURRENT-HAS-MATTER, H-BRIDGE-ADDS-NOTHING, H-BRIDGE-ADDS-NO-MATTER, H-MOUTH-AS-BLACK-HOLE,
    H-N-IS-INPUT, H-THROAT-CARRIES-README, H-README-MINIMAL-EXACT; H-NEGATIVE-FROM-OUTSIDE (struck, item 131).
  The board's: H-THROAT-AT-BOUND, H-NECK-HOLDS, H-STRONG-BOUND (X6); wall 4's floor hypotheses; H-CORE-README,
    H-GREY-VOLUME (illustrative); H-CURRENT-IS-SCHWARZSCHILD (asked; in conflict with 109);
    H-E-PER-BIT (asked); PLANE.md's H-HORIZON-HOLDS, H-STRONG-BOUND.

USAGE
    python3 current.py | --selftest | --json      (sympy, mpmath; about a minute and a half)
"""

import contextlib
import importlib.util
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
_CACHE = {}

BK_SCHWARZSCHILD = "The Schwarzschild metric is restored from (17) in the special case r0 = 3m/2."
FRACTIONS = ("1/1000", "1/100", "1/10", "1/4", "1/2")


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def owners():
    """Imported, never copied: chain.py (exact coefficients, the core README's N, the floor), coin.py (G_kk and the
    passage in closed form), closedbulk.py (K_kk off the plane), plane.py (BK's text, READ there)."""
    if not _CACHE:
        _CACHE["chain"] = _load(os.path.join(HERE, "chain.py"), "copy_chain_current")
        _CACHE["coin"] = _load(os.path.join(HERE, "coin.py"), "copy_coin_current")
        _CACHE["closedbulk"] = _load(os.path.join(D68, "bulk", "closedbulk.py"), "d68_closedbulk_current")
        _CACHE["plane_src"] = open(os.path.join(HERE, "plane.py"), encoding="utf-8").read()
        _CACHE["plane"] = _load(os.path.join(HERE, "plane.py"), "copy_plane_current")
    return _CACHE


def exact_pull():
    """m = r_min / 2 as an exact sympy expression, its value, and the core README's N."""
    import sympy as sp
    o = owners()
    with contextlib.redirect_stdout(io.StringIO()):
        d = o["chain"].compute()
    N = sp.Integer(int(d["core_bits"]))
    co = o["chain"].coefficients()
    r_coeff = sp.sympify(co["r_min_m_per_sqrt_bit"]["exact"])
    e_coeff = sp.sympify(co["E_min_J_per_sqrt_bit"]["exact"])
    m = r_coeff * sp.sqrt(N) / 2
    return {"N": N, "m": m, "E_min": e_coeff * sp.sqrt(N), "floor_r": d["floor_core"]["r_m"],
            "u_r": co["r_min_m_per_sqrt_bit"]["u_r"]}


def leg(m, frac):
    """coin.py's closed form (imported, not copied) per unit E at r0 = 3m/2 + frac m; m in metres."""
    return owners()["coin"].anec_closed(m, m * (1.5 + frac))


def compute():
    import sympy as sp
    o = owners()
    X = exact_pull()
    m, N = X["m"], X["N"]
    mv = float(sp.N(m, 20))
    G_SI, C_SI = 6.6743e-11, 299792458.0
    # X2: coin's G_kk on the candidate path, and the flat alternative (a)
    r, M, D, E, R0 = sp.symbols("r m Delta E r0", positive=True)
    gkk = sp.sympify(o["coin"].g_kk()["gkk"], locals={"r": r, "m": M, "E": E, "r0": R0})
    gkk_D = sp.factor(gkk.subs(R0, sp.Rational(3, 2) * M + D))
    gkk_D_exact = str(sp.N(gkk_D.subs(M, m), 15))
    gkk_flat = sp.simplify(gkk.subs(M, 0))
    leg_flat = [o["coin"].anec_closed(0.0, rr) for rr in (1e-28, 1e-29, 1e-30)]
    hole_kg = mv * C_SI ** 2 / G_SI
    # X3: on the candidate's path
    leg0 = -4.0 / (3.0 * mv)
    rows = []
    for f in FRACTIONS:
        fr = float(sp.Rational(f))
        v = leg(mv, fr)
        quad = o["coin"].anec_leg(mv, mv * (1.5 + fr))
        rows.append({"frac": f, "Delta_m": fr * mv, "leg": v, "minus_current": v - leg0, "quad": quad,
                     "boundary": f == "1/2"})
    d_ = sp.Symbol("delta", positive=True)
    c = sp.sqrt(1 + sp.Rational(2, 3) * d_)
    br = 1 - ((c ** 2 - 1) / c) * sp.atanh(1 / c)
    small = float(sp.N(((br - (1 + (d_ / 3) * sp.log(d_ / 6))) / (d_ * sp.log(d_))).subs(d_, sp.Rational(1, 10 ** 8)), 15))
    wrong = float(sp.N(((br - (1 + (d_ / 3) * sp.log(d_ / 3))) / (d_ * sp.log(d_))).subs(d_, sp.Rational(1, 10 ** 8)), 15))
    E_bit = float(sp.N(X["E_min"] / N, 15))
    E_geo = G_SI * E_bit / C_SI ** 4
    # X4: the two-sheet model at one place (opposite tensions: K = 0)
    cb = o["closedbulk"]
    E5 = cb.field_equations()
    P, _ = cb.planes()
    kk = cb.kkk_series(cb.build(*P["bk"], order=2), 2)
    together = cb.build(*P["bk"], order=2, a1=0)
    # item 131: the throat carries the README -- r0 from the neck's area per bit, against 2m from the horizon's hold
    co = o["chain"].coefficients()
    a_bit = sp.sympify(co["neck_area_m2_per_bit"]["exact"])
    r0_throat = sp.sqrt(N * a_bit / (4 * sp.pi))
    throat_over_2m = sp.simplify(r0_throat / (2 * m))
    bm6 = o["plane"].bk_masses()
    q_r, q_r0, q_m, q_x = bm6["syms"]
    gtt_x = sp.simplify(((q_x ** 2 + q_r0 - 2 * q_m) / (q_r0 + q_x ** 2)).subs(q_r0, 2 * q_m))
    gxx_x = sp.expand(sp.simplify(bm6["cxx"].subs(q_r0, 2 * q_m)))
    komar_h_edge = sp.limit(bm6["komar_horizon"], q_r0, 2 * q_m, "-")
    cb2 = 2 / sp.sqrt(3)
    bracket_edge = 1 - sp.sqrt(3) / 6 * sp.log(2 + sp.sqrt(3))
    leg_edge_closed = float(sp.N(-sp.Rational(4, 3) * bracket_edge / m, 15))
    leg_edge_coin = o["coin"].anec_closed(mv, 2 * mv)
    # item 129: what the corridor adds beyond its pull, in plane.py's own masses
    bm = o["plane"].bk_masses()
    pr, pr0, pm, _ = bm["syms"]
    added = sp.simplify((bm["M_adm"] - bm["M_komar"]).subs(pr0, sp.Rational(3, 2) * pm + D))
    return {"N": int(N), "m_exact": str(m), "m": float(sp.N(m, 15)), "m_over_floor_half": mv / (X["floor_r"] / 2),
            "E_min": float(sp.N(X["E_min"], 15)), "u_r_G_share": X["u_r"], "r0_current": 1.5 * mv,
            "window_end_Delta": mv / 2, "hole_kg": hole_kg, "gkk_Delta": str(gkk_D), "gkk_Delta_exact_m": gkk_D_exact,
            "gkk_current_zero": sp.simplify(gkk_D.subs(D, 0)) == 0, "gkk_flat": str(gkk_flat), "leg_flat": leg_flat,
            "leg_current": leg0, "rows": rows, "series_remainder_over_dlogd_at_1e-8": small,
            "series_wrong_constant": wrong, "E_per_bit": E_bit, "E_per_bit_geo_m": E_geo,
            "leg_current_dimensionless_at_E_bit": leg0 * E_geo, "K_kk_on_plane": str(kk[0]),
            "together_yy": [str(v) for v in together["constraints"]["yy"]],
            "r0_throat": float(sp.N(r0_throat, 15)), "throat_over_2m": str(throat_over_2m), "gtt_edge": str(gtt_x),
            "gxx_edge": str(gxx_x), "komar_h_edge": str(komar_h_edge), "bracket_edge": float(sp.N(bracket_edge, 15)),
            "leg_edge_closed": leg_edge_closed, "leg_edge_coin": leg_edge_coin,
            "M_adm": str(bm["M_adm"]), "M_komar": str(bm["M_komar"]), "adm_minus_pull": str(added),
            "adm_minus_pull_kg_per_Delta_frac": [float(sp.Rational(f)) * mv / 2 * C_SI ** 2 / G_SI for f in FRACTIONS],
            "bk_quote_in_plane": BK_SCHWARZSCHILD.replace(".", "") in owners()["plane_src"].replace(".", "")}


def report(d):
    print("current.py -- items 125-131: the README corridor's coefficients from a current state outward")
    print("  board's N = %d bits (illustrative grey volume; OPEN under item 108);  m = %.14e m (G's share u_r %.1e)" % (
        d["N"], d["m"], d["u_r_G_share"]))
    print("  candidate current state r0 = 3m/2 = %.14e m: a %.4f kg singular black hole (item 109 conflict)" % (
        d["r0_current"], d["hole_kg"]))
    print("  G_kk on the candidate path = %s;  flat alternative (m = 0): G_kk = %s, leg = -4E/(3 r0) %s" % (
        d["gkk_Delta_exact_m"], d["gkk_flat"], ["%.3e" % v for v in d["leg_flat"]]))
    print("  per leg, per metre of E (geometric): limit %.14e" % d["leg_current"])
    for row in d["rows"]:
        print("    Delta/m = %-6s%s Delta = %.11e m: leg %.11e, minus limit %.11e (quadrature %.11e)" % (
            row["frac"], " (boundary)" if row["boundary"] else "", row["Delta_m"], row["leg"], row["minus_current"],
            row["quad"]))
    print("  at E = E_min/N = %.14e J (G E/c^4 = %.4e m): limit per leg %.4e" % (
        d["E_per_bit"], d["E_per_bit_geo_m"], d["leg_current_dimensionless_at_E_bit"]))
    print("  two sheets of opposite tension at one place: yy constraint %s" % d["together_yy"])
    print("  X5 total minus pull = %s;  X6 least throat r0 = %.14e m (= 2m at the floor: %s), leg there %.11e" % (
        d["adm_minus_pull"], d["r0_throat"], d["throat_over_2m"], d["leg_edge_closed"]))


def selftest(d):
    n_pass = n_fail = n_ctl = n_con = 0
    structural = []

    def chk(label, ok, ctl=False, contrast=False):
        nonlocal n_pass, n_fail, n_ctl, n_con
        tag = "CONTROL: " if ctl else ("CONTRAST: " if contrast else "")
        print("  %s %s%s" % ("ok  " if ok else "FAIL", tag, label))
        n_pass += bool(ok)
        n_fail += not ok
        n_ctl += bool(ctl)
        n_con += bool(contrast)

    chk("X2: the candidate's current state (r0 = 3m/2 at the board's m) is a singular black hole of %.4f kg with a "
        "horizon at 2m -- not empty space; against item 109" % d["hole_kg"], abs(d["hole_kg"] - 0.2677) < 1e-3)
    chk("X2 (a): if the current state is flat (m = 0), G_kk = %s and each leg -4E/(3 r0) grows without bound as r0 -> 0 "
        "(%s per metre of E)" % (d["gkk_flat"], ["%.3e" % v for v in d["leg_flat"]]),
        d["gkk_flat"] == "-E**2*r0/r**3" and d["leg_flat"][0] > d["leg_flat"][1] > d["leg_flat"][2])
    worst = max(abs(row["quad"] / row["leg"] - 1) for row in d["rows"])
    chk("coin.py's closed form and quadrature agree at the board's m in metres at five Delta (worst %.1e) -- floating-"
        "point robustness and the import at SI scale" % worst, worst < 1e-10, ctl=True)
    chk("X3: on the candidate's path the leg rises monotonically from the limit %.11e (five points: %s)" % (
        d["leg_current"], ["%.4e" % row["leg"] for row in d["rows"]]),
        all(d["rows"][i]["leg"] < d["rows"][i + 1]["leg"] for i in range(len(d["rows"]) - 1))
        and d["leg_current"] < d["rows"][0]["leg"] < 0)
    chk("X3: the hand-derived series -(4E/3m)[1 + (Delta/3m) ln(Delta/6m)] matches the closed form at delta = 1e-8 "
        "(remainder/(delta ln delta) %.2e); with ln(delta/3) it fails (%.2e)" % (
            d["series_remainder_over_dlogd_at_1e-8"], d["series_wrong_constant"]),
        abs(d["series_remainder_over_dlogd_at_1e-8"]) < 1e-6 < abs(d["series_wrong_constant"]))
    chk("X6 at the floor (r0 = 2m): g_tt = %s (a double zero at the throat), the horizon's Komar charge -> %s (zero "
        "surface gravity, T = 0), g_xx = %s > 0 for x != 0 (the throat infinitely far at fixed t; x never a time "
        "direction -- PLANE point 1's one-way mechanism gone)" % (d["gtt_edge"], d["komar_h_edge"], d["gxx_edge"]),
        d["gtt_edge"] == "x**2/(2*m + x**2)" and d["komar_h_edge"] == "0" and d["gxx_edge"].startswith("4*m**2/x**2"))
    chk("X6: each leg's null integral there is -(4E/3m)[1 - (sqrt3/6) ln(2 + sqrt3)] = %.11e per metre of E, coin.py's "
        "closed form %.11e" % (d["leg_edge_closed"], d["leg_edge_coin"]),
        abs(d["leg_edge_closed"] / d["leg_edge_coin"] - 1) < 1e-12)
    chk("X4: the board's two sheets of opposite tension put at one place (K = 0) fail the bulk's yy constraint: %s -- "
        "the coinciding junction is not B3's" % d["together_yy"], d["together_yy"][0] != "0")
    structural.append("X1: m = %.14e m; chain.py's bisected floor (same equation, second implementation) agrees to "
                      "%.2e -- nopath's rounded hbar; N here is the board's example input (H-N-IS-INPUT, item 130)" % (
                          d["m"], d["m_over_floor_half"] - 1))
    structural.append("X2: on the candidate path G_kk = %s (board's m: %s) -- M's identity with current value 0" % (
        d["gkk_Delta"], d["gkk_Delta_exact_m"]))
    structural.append("X2: r0's candidate current value %.14e m (BK p.4 '%s', in plane.py: %s); alternatives (b) m and "
                      "r0 both move, (c) Delta < 0 gives G_kk > 0" % (d["r0_current"], BK_SCHWARZSCHILD,
                                                                      d["bk_quote_in_plane"]))
    structural.append("X3: at E = E_min/N = %.14e J (geometric %.4e m) the candidate's limit per leg is %.4e; E is "
                      "also the affine normalization" % (d["E_per_bit"], d["E_per_bit_geo_m"],
                                                         d["leg_current_dimensionless_at_E_bit"]))
    structural.append("X4: K_kk on an empty umbilic plane = %s (from the input K = -a q and k null) -- the null stress "
                      "there totals zero; first counted with 'needs no k', withdrawn" % d["K_kk_on_plane"])
    structural.append("X5: the total minus the pull = (%s) - (%s) = %s at r0 = 3m/2 + Delta -- PLANE point 4's Penrose "
                      "gap, eq. 18's tidal energy outside the horizon (first counted)" % (
                          d["M_adm"], d["M_komar"], d["adm_minus_pull"]))
    structural.append("X6: the least throat carrying N bits, r0 = sqrt(N A_bit/4pi) = %.14e m; at the floor (2m = r_min) "
                      "r0/2m = %s by construction (one bound, two surfaces; first counted); above the floor, floor < m < "
                      "4/3 floor, r0 lies inside the horizon -- a horizon member" % (d["r0_throat"], d["throat_over_2m"]))
    structural.append("X5 at the board's m: Delta/2 in mass for Delta/m = %s is %s kg" % (
        list(FRACTIONS), ["%.4e" % v for v in d["adm_minus_pull_kg_per_Delta_frac"]]))
    structural.append("the last row (Delta = m/2, r0 = 2m) is the window's boundary, not a horizon member")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("current.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
    return n_fail == 0


def main(argv):
    d = compute()
    if "--json" in argv:
        print(json.dumps(d, indent=1, default=str))
        return 0
    if "--selftest" in argv:
        return 0 if selftest(d) else 1
    report(d)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
