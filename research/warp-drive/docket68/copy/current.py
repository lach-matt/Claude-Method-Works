#!/usr/bin/env python3
"""current.py -- DOCKET 68, M-RULINGS items 125-127: the README corridor's coefficients evaluated with exact values,
from our current state outward.  Deduced and computed; verified once; not seated.  Write-up: CURRENT.md.

M's words (verbatim in the rulings file): item 125 "We cannot use general coefficients for this work. We must always
avoid that debt by evaluating the coefficient in full and calculate using it exact values." (M-EXACT-VALUES); item 127
"1 - yes" (H-PLANES-COINCIDE) and "The coefficient value is the difference of that value in a counterfactual universe
and its value in our current universe, added to the value of our current universe" (H-COEFF-FROM-CURRENT).

INPUTS.  h, c exact (SI 2019); G = 6.6743e-11 (CODATA 2018, u_r 2.2e-5).  N = 2742570311524972 bits is the board's
core README (chain.py's core_bits): a float, faithful.identity_core() = synapse density x bits per synapse x
H_GREY_VOLUME_MM3 = 5e5, a volume the code marks "H-GREY-VOLUME, NAMED-NOT-READ, illustrative" (H-CORE-README, the
board's).  Under item 108 ("Whatever is needed") N is itself a coefficient, and under item 125 an illustrative input is
what must go: N's value is OPEN, so the 16 digits below are arithmetic, not precision.  First written "EXACT INPUTS ...
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
  WHAT STAYS A COEFFICIENT.  N (item 108); m's current value; Delta and its side; E and its normalization; the tension's
  sign (H-OUR-TENSION; RS1 puts our atoms on the negative-tension sheet, BULK.md); k and kappa (through the tension and
  the 4D G); the coinciding junction.

NAMED HYPOTHESES
  M's: M-EXACT-VALUES (125); H-PLANES-COINCIDE, H-COEFF-FROM-CURRENT (127); H-COLOCATED-REALIZATION,
    H-SHORTEST-DISTANCE (126); H-HORIZON-NEEDS-OBJECT (109); H-README-AS-NEEDED (108); the horizon members' window.
  The board's: H-CORE-README, H-GREY-VOLUME (illustrative); H-CURRENT-IS-SCHWARZSCHILD (asked; in conflict with 109);
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
    return {"N": int(N), "m_exact": str(m), "m": float(sp.N(m, 15)), "m_over_floor_half": mv / (X["floor_r"] / 2),
            "E_min": float(sp.N(X["E_min"], 15)), "u_r_G_share": X["u_r"], "r0_current": 1.5 * mv,
            "window_end_Delta": mv / 2, "hole_kg": hole_kg, "gkk_Delta": str(gkk_D), "gkk_Delta_exact_m": gkk_D_exact,
            "gkk_current_zero": sp.simplify(gkk_D.subs(D, 0)) == 0, "gkk_flat": str(gkk_flat), "leg_flat": leg_flat,
            "leg_current": leg0, "rows": rows, "series_remainder_over_dlogd_at_1e-8": small,
            "series_wrong_constant": wrong, "E_per_bit": E_bit, "E_per_bit_geo_m": E_geo,
            "leg_current_dimensionless_at_E_bit": leg0 * E_geo, "K_kk_on_plane": str(kk[0]),
            "together_yy": [str(v) for v in together["constraints"]["yy"]],
            "bk_quote_in_plane": BK_SCHWARZSCHILD.replace(".", "") in owners()["plane_src"].replace(".", "")}


def report(d):
    print("current.py -- items 125-127: the README corridor's coefficients from a current state outward")
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
    chk("X4: the board's two sheets of opposite tension put at one place (K = 0) fail the bulk's yy constraint: %s -- "
        "the coinciding junction is not B3's" % d["together_yy"], d["together_yy"][0] != "0")
    structural.append("X1: m = %.14e m; chain.py's bisected floor (same equation, second implementation) agrees to "
                      "%.2e -- nopath's rounded hbar; N is the board's illustrative core (H-GREY-VOLUME), OPEN" % (
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
