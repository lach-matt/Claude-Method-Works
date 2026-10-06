#!/usr/bin/env python3
"""current.py -- DOCKET 68, M-RULINGS items 125-127: the README corridor's coefficients evaluated with exact values,
from our current state outward.  Deduced and computed; not verified; not seated.  Write-up: CURRENT.md.

M's words (verbatim in the rulings file): item 125 "We cannot use general coefficients for this work. We must always
avoid that debt by evaluating the coefficient in full and calculate using it exact values." (M-EXACT-VALUES); item 127
"1 - yes" (H-PLANES-COINCIDE: the two planes occupy the same place, the extra dimension included) and "The coefficient
value is the difference of that value in a counterfactual universe and its value in our current universe, added to the
value of our current universe" (H-COEFF-FROM-CURRENT).

EXACT INPUTS.  h, c exact (SI 2019); G = 6.6743e-11 (CODATA 2018, u_r 2.2e-5, carried); the core README's N =
2742570311524972 bits (chain.py's core_bits, from the identity core).  Through chain.py's exact coefficients:
E_min = sqrt(N h c^5 ln2/(8 pi^2 G)), r_min = sqrt(N h G ln2/(2 pi^2 c^3)), and the corridor's pull (PLANE.md point 2)
m = G E_min/c^4 = r_min/2.

WHAT THE WORK FINDS
  X1 THE PULL, EXACT.  m = 1.98790932853678e-28 m (u_r 1.1e-5 from G); two routes agree: chain.py's exact coefficient
     times sqrt(N), and chain.py's bisected floor radius halved.
  X2 THE THROAT FROM OUR CURRENT STATE.  The board's candidate for r0's current value (asked of M): our current state
     has no corridor, and the member of eq. (17) with none is Schwarzschild -- Bronnikov-Kim p.4: "The Schwarzschild
     metric is restored from (17) in the special case r0 = 3m/2".  So r0 = 3m/2 + Delta, current value
     2.98186399280517e-28 m, Delta the counterfactual difference, 0 < Delta < m/2 = 9.93954664268e-29 m (the horizon
     members).  The plane's reading is then EXACTLY the difference: G_kk = -4 Delta E^2/(r (2r - 3m)^2) -- zero in our
     current state, linear in Delta (sympy, from coin.py's G_kk).
  X3 THE PASSAGE, FROM THE CURRENT STATE OUTWARD.  Per leg (coin.py's closed form, exact m): the current-state limit is
     -4E/(3m) = -6.70721402728537e27 E per metre, and moving outward
         leg(Delta) = -(4E/3m) [1 + (Delta/3m) ln(Delta/6m) + O((Delta/m)^2 ln(Delta/m))]   (sympy series, checked)
     with the range printed from Delta/m = 1e-3 to the window's end (r0 = 2m: -4.15731236130e27 E per metre).
     At the current state itself G_kk = 0 and there is no throat, so no passage; the limit from the counterfactual side
     is -4E/(3m), not 0 -- the passage's whole reading gathers at the throat as Delta -> 0.
  X4 WITH THE PLANES COINCIDING, k DROPS OUT.  The second plane's null matter at coincidence is (2/kappa^2) K_kk(0) = 0
     exactly (closedbulk.py's K_kk vanishes on our plane), and every reading of the corridor on our plane -- G_kk, the
     bulk's E_kk = -G_kk (umbilic.py), the passage -- is free of the bulk scale a = k (computed).  So in the coinciding
     configuration the device needs no k and no kappa.
  WHAT STAYS A COEFFICIENT.  E, the ray's energy: every passage reading is linear in it.  Its current-state value is
  asked of M; the board's candidate is the floor's energy per bit, E_min/N = 8.77234875675332 J (not M's).

NAMED HYPOTHESES
  M's: M-EXACT-VALUES (125); H-PLANES-COINCIDE, H-COEFF-FROM-CURRENT (127); H-COLOCATED-REALIZATION,
    H-SHORTEST-DISTANCE (126); H-BK-CORRIDOR's horizon members (the window, PLANE.md).
  The board's: H-CURRENT-IS-SCHWARZSCHILD (r0's current value is the no-corridor member r0 = 3m/2; asked); H-E-PER-BIT
    (the candidate current value of E; asked); PLANE.md's H-HORIZON-HOLDS, H-STRONG-BOUND (m = r_min/2).

USAGE
    python3 current.py | --selftest | --json      (sympy, mpmath; about half a minute)
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


def leg_exact(m, frac):
    """coin.py's closed form per unit E at r0 = 3m/2 + frac m (c^2 = 1 + 2 frac/3), exact m, 20 digits."""
    import sympy as sp
    c2 = 1 + sp.Rational(2, 3) * frac
    c = sp.sqrt(c2)
    return -(sp.Rational(4, 3) / m) * (1 - ((c2 - 1) / c) * sp.atanh(1 / c))


def compute():
    import sympy as sp
    o = owners()
    X = exact_pull()
    m, N = X["m"], X["N"]
    mv = float(sp.N(m, 20))
    # X2: coin's G_kk with r0 = 3m/2 + Delta
    r, M, D, E = sp.symbols("r m Delta E", positive=True)
    gkk = sp.sympify(o["coin"].g_kk()["gkk"], locals={"r": r, "m": M, "E": E, "r0": sp.Symbol("r0", positive=True)})
    gkk_D = sp.factor(gkk.subs(sp.Symbol("r0", positive=True), sp.Rational(3, 2) * M + D))
    # X3: from the current state outward
    leg0 = -sp.Rational(4, 3) / m
    rows = []
    for f in FRACTIONS:
        fr = sp.Rational(f)
        v = leg_exact(m, fr)
        quad = o["coin"].anec_leg(mv, mv * (1.5 + float(fr)))           # coin's quadrature, SI metres
        rows.append({"frac": f, "Delta_m": float(sp.N(fr * m, 15)), "leg": float(sp.N(v, 15)),
                     "minus_current": float(sp.N(v - leg0, 15)), "quad": quad})
    d_ = sp.Symbol("delta", positive=True)
    c = sp.sqrt(1 + sp.Rational(2, 3) * d_)
    br = 1 - ((c ** 2 - 1) / c) * sp.atanh(1 / c)
    lead = 1 + (d_ / 3) * sp.log(d_ / 6)
    small = float(sp.N(((br - lead) / (d_ * sp.log(d_))).subs(d_, sp.Rational(1, 10 ** 8)), 15))
    # X4: coincidence and the bulk scale
    cb = o["closedbulk"]
    E5 = cb.field_equations()
    P, (mm, rr0, L) = cb.planes()
    kk = cb.kkk_series(cb.build(*P["bk"], order=2), 2)
    return {"N": int(N), "m_exact": str(m), "m": float(sp.N(m, 15)), "m_over_floor_half": mv / (X["floor_r"] / 2),
            "E_min": float(sp.N(X["E_min"], 15)), "u_r_m": X["u_r"], "r0_current": float(sp.N(sp.Rational(3, 2) * m, 15)),
            "window_end_Delta": float(sp.N(m / 2, 15)), "gkk_Delta": str(gkk_D),
            "gkk_current_zero": sp.simplify(gkk_D.subs(D, 0)) == 0, "leg_current": float(sp.N(leg0, 15)), "rows": rows,
            "series_remainder_over_dlogd_at_1e-8": small,
            "K_kk_on_plane": str(kk[0]), "reading_free_of_a": E5["a"] not in sp.sympify(kk[1]).free_symbols,
            "E_per_bit": float(sp.N(X["E_min"] / N, 15)),
            "bk_quote_in_plane": BK_SCHWARZSCHILD.replace(".", "") in owners()["plane_src"].replace(".", "")}


def report(d):
    print("current.py -- items 125-127: the README corridor's coefficients from our current state outward")
    print("  N = %d bits;  E_min = %.14e J;  m = G E_min/c^4 = r_min/2 = %.14e m (u_r %.1e)" % (
        d["N"], d["E_min"], d["m"], d["u_r_m"]))
    print("  r0 = 3m/2 + Delta: current value %.14e m; window 0 < Delta < %.11e m" % (d["r0_current"],
                                                                                    d["window_end_Delta"]))
    print("  G_kk = %s" % d["gkk_Delta"])
    print("  per leg (E per metre): current-state limit %.14e" % d["leg_current"])
    for row in d["rows"]:
        print("    Delta/m = %-6s Delta = %.11e m: leg %.11e, minus current %.11e (quadrature %.11e)" % (
            row["frac"], row["Delta_m"], row["leg"], row["minus_current"], row["quad"]))
    print("  coinciding planes: K_kk on our plane = %s; the corridor's reading free of the bulk scale: %s" % (
        d["K_kk_on_plane"], d["reading_free_of_a"]))
    print("  still a coefficient: E (candidate current value E_min/N = %.14e J per bit)" % d["E_per_bit"])


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

    chk("X1: m = %.14e m by chain.py's exact coefficient times sqrt(N), and the bisected floor radius halved agrees "
        "(ratio %.12f)" % (d["m"], d["m_over_floor_half"]), abs(d["m_over_floor_half"] - 1) < 1e-9)
    chk("X2: with r0 = 3m/2 + Delta the plane's reading is %s -- zero in our current state, linear in the difference" %
        d["gkk_Delta"], d["gkk_current_zero"] and d["gkk_Delta"].startswith("-4*Delta*E**2"))
    worst = max(abs(row["quad"] / row["leg"] - 1) for row in d["rows"])
    chk("the closed form at exact m in metres agrees with coin.py's quadrature at all five Delta (worst relative %.1e)" %
        worst, worst < 1e-10, ctl=True)
    chk("X3: moving outward the leg rises monotonically from the current-state limit %.11e toward the window's end "
        "(%s)" % (d["leg_current"], [("%.4e" % row["leg"]) for row in d["rows"]]),
        all(d["rows"][i]["leg"] < d["rows"][i + 1]["leg"] for i in range(len(d["rows"]) - 1))
        and d["leg_current"] < d["rows"][0]["leg"] < 0)
    chk("X3: leg = -(4E/3m)[1 + (Delta/3m) ln(Delta/6m) + O(delta^2 ln delta)]: the remainder over delta ln delta at "
        "delta = 1e-8 is %.3e" % d["series_remainder_over_dlogd_at_1e-8"],
        abs(d["series_remainder_over_dlogd_at_1e-8"]) < 1e-6)
    chk("X4: K_kk on our plane = %s, so a second plane coinciding with ours carries no matter along light rays; the "
        "corridor's reading is free of the bulk scale a (%s)" % (d["K_kk_on_plane"], d["reading_free_of_a"]),
        d["K_kk_on_plane"] == "0" and d["reading_free_of_a"])
    structural.append("X2: r0's current value 3m/2 = %.14e m is the board's candidate (H-CURRENT-IS-SCHWARZSCHILD; BK "
                      "p.4 '%s', in plane.py: %s) -- asked of M" % (d["r0_current"], BK_SCHWARZSCHILD,
                                                                   d["bk_quote_in_plane"]))
    structural.append("X3: at Delta = 0 there is no throat and G_kk = 0; the limit -4E/(3m) from the counterfactual side "
                      "is coin.py's C2 (the reading gathers at the throat)")
    structural.append("E stays a coefficient: every passage reading is linear in it; candidate current value E_min/N = "
                      "%.14e J per bit (H-E-PER-BIT, asked)" % d["E_per_bit"])
    structural.append("m carries G's uncertainty: u_r = %.1e (half of G's 2.2e-5)" % d["u_r_m"])
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
