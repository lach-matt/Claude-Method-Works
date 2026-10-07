#!/usr/bin/env python3
"""exactE.py -- DOCKET 68, M-RULINGS item 134: compute E, the one exact energy, and machine-check E and every value
derived from the coefficients.  Deduced, computed and machine-checked; verified once; SEATED (ledger.py section 8p).  Write-up: EXACTE.md.
First headed "... not verified; not seated".

M's words (verbatim in the rulings file): item 134 "Seat them and then compute E. Machine check E and all the values
derived from the coefficients."; item 133 "There is only one exact energy needed for any given README" (identified by
the board with E(N) at the bound, H-EXACT-ENERGY-AT-BOUND); item 130: N is the user's input, read from the object;
item 125: no general coefficients.

THE ROUTE (PROOF-ASSISTANT.md): Z3, an SMT solver.  A claim is checked by asserting its negation with its hypotheses and
asking for a model: unsat = no counterexample exists.
  VALUES -- each value's enclosure [lo, hi] is taken from its OWNER's closed form (chain.py's exact coefficients;
     m = r_min/2, M = E/c^2, the total 5M/4 from them), padded 1e-30 relative.  Z3 then proves that the board's OWN
     encoded relation (the value as the positive root of a polynomial in pi, ln2 with h, c, G exact) has its root in
     [lo, hi] for EVERY pi and ln2 inside mpmath's rigorous interval bounds.  So the proof is the drift guard: a typo in
     either the owner's form or the encoding refutes it.  CONTROL for each value: the same relation with G raised by one
     part in 1e9 must be refuted on the same [lo, hi].  First written with the enclosure from a separate interval copy
     and a "1e-9 high" control that could not fail independently; the verifier showed a typo in both copies passed.
  IDENTITIES -- universal over the reals (every positive h, c, G, pi, ln2, N, m, x where they appear).  Kinds:
     DEFINING (a closed form solves its own defining equation -- an algebra check, not a physics result: chain.py
     defines E_min and r_min as the meeting of E r = N h c ln2/(4 pi^2) with E = r c^4/(2G)); CHECK (the regular chart,
     the one-way cone under the time orientation H-FUTURE-INGOING, the passage factor's tanh step); STRUCTURAL
     (true by the hypotheses' own arithmetic: r0 = 2m given r0 := r_min and m := G E/c^4; M = E/c^2; the total 5m/4
     -- run, printed, not counted); CONTROL (must be refuted).
  THE PASSAGE FACTOR -(4/3)(E/m)[1 - (sqrt3/6) ln(2 + sqrt3)] per leg at r0 = 2m is a COEFFICIENT: E is the null ray's
     affine normalization (not E(N)) and m the pull, geometric units -- OPEN under M-EXACT-VALUES.  Its number is
     enclosed by interval arithmetic and checked against coin.py's closed form (coin.py derives it and checks it
     against quadrature); Z3 checks only its tanh step, tanh(ln(2 + sqrt3)) = sqrt3/2.  First written as a checked
     value of unit 1.
GUARDS: VACUITY -- every obligation's hypotheses are satisfiable on their own.  DRIFT -- the values' Z3 proofs above;
the three chain coefficients satisfy the encoded relations EXACTLY (sympy simplify to 0); plane.py's own total and g_xx at
r0 = 2m equal the encoded ones (sympy); coin.py's closed form equals the passage factor.

NAMED HYPOTHESES
  M's: H-ONE-EXACT-ENERGY (133), H-N-IS-INPUT (130), H-THROAT-CARRIES-README (131), H-HORIZON-AND-THROAT-HOLD,
    H-ONE-WAY-BY-NATURE (132), M-EXACT-VALUES (125).
  The board's: H-EXACT-ENERGY-AT-BOUND (133's energy is E(N) at the bound); H-PULL-IS-COST (m = G E/c^4, wall 4);
    H-STRONG-BOUND, H-HORIZON-HOLDS, H-NECK-HOLDS, H-THROAT-AT-BOUND, H-DEVICE-SIZES (chain.py, PLANE.md, current.py X6);
    H-FUTURE-INGOING (v increases to the future, -d_x future at the throat -- current.py X7's orientation; reversed, the
    one-way claim is refuted); H-IV-BOUNDS (mpmath's interval pi and ln2; checked independently by the verifier by exact
    rational comparison); H-CORE-README (the example N, illustrative).  r0 = 2m is the value BK exclude: stability and
    fine-tuning OPEN (current.py X6).

USAGE
    python3 exactE.py | --selftest | --json      (z3, sympy, mpmath; about a minute and a half)
"""

import contextlib
import importlib.util
import io
import json
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
_CACHE = {}

H_SI = Fraction("6.62607015e-34")       # exact, SI 2019
C_SI = Fraction(299792458)              # exact, SI 2019
G_SI = Fraction("6.6743e-11")           # CODATA 2018, u_r 2.2e-5 (entered exactly; the uncertainty named)
U_R_G = 2.2e-5
N_EXAMPLE = 2742570311524972            # the board's core README (H-CORE-README, illustrative): an example input
PAD = Fraction(1, 10 ** 30)


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
    """Imported, never copied: chain.py (the exact coefficients), plane.py (the corridor's total and g_xx), coin.py (the
    passage's closed form)."""
    if not _CACHE:
        _CACHE["chain"] = _load(os.path.join(HERE, "chain.py"), "copy_chain_exactE")
        _CACHE["plane"] = _load(os.path.join(HERE, "plane.py"), "copy_plane_exactE")
        _CACHE["coin"] = _load(os.path.join(HERE, "coin.py"), "copy_coin_exactE")
    return _CACHE


def e_per_sqrt_bit():
    """E per sqrt(bit), J, from chain.py's exact coefficient at 30 digits (cheap: no Z3) -- what the ledger asks."""
    import sympy as sp
    co = owners()["chain"].coefficients()
    return float(sp.N(sp.sympify(co["E_min_J_per_sqrt_bit"]["exact"]), 30))


def _ratio(x):
    """An mpf endpoint as an exact (numerator, denominator), sign kept, every bit kept."""
    import mpmath as mp
    with mp.workdps(80):
        v = mp.mpf(x)
        sgn = -1 if v < 0 else 1
        man, exp = abs(v).man_exp
    man *= sgn
    return (man * 2 ** exp, 1) if exp >= 0 else (man, 2 ** (-exp))


def bounds():
    """Rigorous rational bounds on pi and ln2 from mpmath's interval arithmetic (outward rounding)."""
    import mpmath as mp
    mp.iv.dps = 40
    pi, l2 = mp.iv.pi, mp.iv.log(2)
    return {"pi": (Fraction(*_ratio(pi.a)), Fraction(*_ratio(pi.b))),
            "ln2": (Fraction(*_ratio(l2.a)), Fraction(*_ratio(l2.b)))}


def _digits(fr, n):
    """A Fraction to n significant digits, computed at 60 digits (not mpmath's default 15)."""
    import mpmath as mp
    with mp.workdps(60):
        return mp.nstr(mp.mpf(fr.numerator) / fr.denominator, n)


def _q(fr):
    import z3
    return z3.RealVal("%d/%d" % (fr.numerator, fr.denominator))


def _solve(hyps, goal, timeout_ms=60000):
    """'proved' if hyps and not goal is unsat, 'refuted' if sat, else 'unknown'; and whether hyps alone are sat."""
    import z3
    s = z3.Solver()
    s.set("timeout", timeout_ms)
    s.add(*hyps)
    vac = s.check()
    s.add(z3.Not(goal))
    r = s.check()
    status = "proved" if r == z3.unsat else ("refuted" if r == z3.sat else "unknown")
    return status, vac == z3.sat


def identities():
    """Universal obligations over the reals: {name: (kind, status, hypotheses satisfiable)}."""
    import z3
    h, c, G, P, L, N, E, r, m, A, x, s3 = z3.Reals("h c G P L N E r m A x s3")
    pos = [h > 0, c > 0, G > 0, P > 0, L > 0, N > 0]
    E_def = [E > 0, E * E * 8 * P * P * G == N * h * c ** 5 * L]
    r_def = [r > 0, r * r * 2 * P * P * c ** 3 == N * h * G * L]
    out = {}
    out["the closed forms meet: r_min c^4 = 2 G E (so m = G E/c^4 = r_min/2)"] = (
        "DEFINING",) + _solve(pos + E_def + r_def, r * c ** 4 == 2 * G * E)
    out["the closed forms meet: E r_min = N h c ln2/(4 pi^2) (the bound at equality)"] = (
        "DEFINING",) + _solve(pos + E_def + r_def, E * r * 4 * P * P == N * h * c * L)
    out["the closed forms meet: 4 pi r_min^2 = N A_bit, A_bit = 2 h G ln2/(pi c^3)"] = (
        "DEFINING",) + _solve(pos + r_def + [A * P * c ** 3 == 2 * h * G * L], 4 * P * r * r == N * A)
    out["r0 := r_min and m := G E/c^4 give r0 = 2m"] = (
        "STRUCTURAL",) + _solve(pos + E_def + r_def + [m * c ** 4 == G * E], r == 2 * m)
    M = z3.Real("M")
    out["M = E/c^2 = m c^2/G"] = ("STRUCTURAL",) + _solve(
        pos + E_def + [m * c ** 4 == G * E, M * c * c == E], M * G == m * c * c)
    adm, pull = z3.Reals("adm pull")
    out["total = m/4 + r0/2 = 5m/4 at r0 = 2m; total - pull = m/4"] = ("STRUCTURAL",) + _solve(
        [m > 0, adm == m / 4 + (2 * m) / 2, pull == m], z3.And(adm == 5 * m / 4, adm - pull == m / 4))
    gtt = x * x / (2 * m + x * x)
    gxx = 4 * m * m / (x * x) + 10 * m + 4 * x * x
    out["g_tt g_xx = 2(m + 2x^2) at r0 = 2m, every x != 0 (the ingoing chart regular)"] = (
        "CHECK",) + _solve([m > 0, x != 0], gtt * gxx == 2 * (m + 2 * x * x))
    # the cone at the throat: g_vv = -g_tt(0) = 0 (from g_tt's formula), g_vx = +h ingoing; H-FUTURE-INGOING
    hh, vd, xd, gvv = z3.Reals("hh vd xd gvv")
    cone = [hh > 0, hh * hh == 2 * m, m > 0, gvv == -(0 * 0) / (2 * m + 0 * 0),
            gvv * vd * vd + 2 * hh * vd * xd <= 0, z3.Or(vd > 0, z3.And(vd == 0, hh * xd < 0))]
    out["one way under H-FUTURE-INGOING: the future cone at the throat has xdot <= 0"] = (
        "CHECK",) + _solve(cone, xd <= 0)
    cone_out = [hh > 0, hh * hh == 2 * m, m > 0, gvv == 0, gvv * vd * vd - 2 * hh * vd * xd <= 0,
                z3.Or(vd > 0, z3.And(vd == 0, -hh * xd < 0))]
    out["CONTROL the outgoing chart's 'xdot <= 0' must fail"] = ("CONTROL",) + _solve(cone_out, xd <= 0)
    cone_rev = [hh > 0, hh * hh == 2 * m, m > 0, gvv == 0, gvv * vd * vd + 2 * hh * vd * xd <= 0,
                z3.Or(vd < 0, z3.And(vd == 0, hh * xd > 0))]
    out["CONTROL the reversed orientation's 'xdot <= 0' must fail"] = ("CONTROL",) + _solve(cone_rev, xd <= 0)
    u = 2 + s3
    out["tanh(ln(2 + sqrt3)) = sqrt3/2 (the passage factor's artanh step)"] = (
        "CHECK",) + _solve([s3 > 0, s3 * s3 == 3], (u * u - 1) * 2 == s3 * (u * u + 1))
    out["CONTROL r0 = 3m/2 must fail"] = ("CONTROL",) + _solve(
        pos + E_def + r_def + [m * c ** 4 == G * E], 2 * r == 3 * m)
    return out


def _owner_values():
    """Each value's closed form from its owner (chain.py's exact coefficients), as sympy expressions."""
    import sympy as sp
    co = owners()["chain"].coefficients()
    E1 = sp.sympify(co["E_min_J_per_sqrt_bit"]["exact"])
    r1 = sp.sympify(co["r_min_m_per_sqrt_bit"]["exact"])
    A1 = sp.sympify(co["neck_area_m2_per_bit"]["exact"])
    c = sp.Integer(299792458)
    sN = sp.sqrt(sp.Integer(N_EXAMPLE))
    return {"E1": E1, "m1": r1 / 2, "r1": r1, "A1": A1, "M1": E1 / c ** 2,
            "EN": E1 * sN, "mN": r1 / 2 * sN, "rN": r1 * sN, "MN": E1 / c ** 2 * sN,
            "TN": sp.Rational(5, 4) * E1 / c ** 2 * sN}


def values(B):
    """Z3-proved enclosures around the owners' closed forms, each with a perturbed-relation control."""
    import z3
    import sympy as sp
    P, L, X = z3.Reals("P L X")
    pl, ph = B["pi"]
    ll, lh = B["ln2"]
    box = [P >= _q(pl), P <= _q(ph), L >= _q(ll), L <= _q(lh)]
    h, c = _q(H_SI), _q(C_SI)
    ow = _owner_values()
    n = N_EXAMPLE

    def rel(key, G):
        return {"E1": X * X * 8 * P * P * G == h * c ** 5 * L,
                "m1": 4 * X * X * 2 * P * P * c ** 3 == h * G * L,
                "r1": X * X * 2 * P * P * c ** 3 == h * G * L,
                "A1": X * P * c ** 3 == 2 * h * G * L,
                "M1": X * X * c ** 4 * 8 * P * P * G == h * c ** 5 * L,
                "EN": X * X * 8 * P * P * G == n * h * c ** 5 * L,
                "mN": 4 * X * X * 2 * P * P * c ** 3 == n * h * G * L,
                "rN": X * X * 2 * P * P * c ** 3 == n * h * G * L,
                "MN": X * X * c ** 4 * 8 * P * P * G == n * h * c ** 5 * L,
                "TN": 16 * X * X * c ** 4 * 8 * P * P * G == 25 * n * h * c ** 5 * L}[key]
    names = [("E1", "E per sqrt(bit)", "J"), ("m1", "m per sqrt(bit) (the pull)", "m"),
             ("r1", "r0 = r_min = 2m per sqrt(bit)", "m"), ("A1", "A_bit, area per bit", "m^2"),
             ("M1", "M = E/c^2 per sqrt(bit)", "kg"), ("EN", "E at the example N", "J"),
             ("mN", "m at the example N", "m"), ("rN", "r0 at the example N", "m"),
             ("MN", "M at the example N", "kg"), ("TN", "total at the example N (5/4 of the pull)", "kg")]
    Gq, Gw = _q(G_SI), _q(G_SI * (1 + Fraction(1, 10 ** 9)))
    rows = []
    for key, name, unit in names:
        mid = Fraction(str(sp.N(ow[key], 60)))
        lo, hi = mid * (1 - PAD), mid * (1 + PAD)
        goal = z3.And(X >= _q(lo), X <= _q(hi))
        st, vac = _solve(box + [X > 0, rel(key, Gq)], goal)
        stc, _ = _solve(box + [X > 0, rel(key, Gw)], goal)
        rows.append({"key": key, "name": name, "unit": unit, "digits": _digits(mid, 20), "lo_digits": _digits(lo, 34),
                     "hi_digits": _digits(hi, 34), "value": float(mid), "status": st, "vacuity_ok": vac,
                     "control": stc})
    return rows


def passage():
    """The passage factor per leg at r0 = 2m: interval-enclosed, and coin.py's closed form at m = 1, r0 = 2."""
    import mpmath as mp
    mp.iv.dps = 40
    s3 = mp.iv.sqrt(3)
    leg = -mp.iv.mpf(4) / 3 * (1 - s3 / 6 * mp.iv.log(2 + s3))
    lo, hi = Fraction(*_ratio(leg.a)), Fraction(*_ratio(leg.b))
    coin_val = owners()["coin"].anec_closed(1.0, 2.0)
    return {"digits": _digits((lo + hi) / 2, 20), "lo_digits": _digits(lo, 40), "hi_digits": _digits(hi, 40),
            "rel_width": float((hi - lo) / abs((lo + hi) / 2)), "coin": coin_val,
            "coin_rel_diff": float(abs(coin_val / float((lo + hi) / 2) - 1))}


def drift():
    """The chain coefficients satisfy the encoded relations EXACTLY; plane.py's total and g_xx match the encoded ones."""
    import sympy as sp
    o = owners()
    co = o["chain"].coefficients()
    h, c, G = sp.Rational(str(H_SI.numerator), str(H_SI.denominator)), sp.Integer(299792458), \
        sp.Rational(str(G_SI.numerator), str(G_SI.denominator))
    E1 = sp.sympify(co["E_min_J_per_sqrt_bit"]["exact"])
    r1 = sp.sympify(co["r_min_m_per_sqrt_bit"]["exact"])
    A1 = sp.sympify(co["neck_area_m2_per_bit"]["exact"])
    exact = {"E_def": sp.simplify(E1 ** 2 * 8 * sp.pi ** 2 * G - h * c ** 5 * sp.log(2)) == 0,
             "r_def": sp.simplify(r1 ** 2 * 2 * sp.pi ** 2 * c ** 3 - h * G * sp.log(2)) == 0,
             "A_def": sp.simplify(A1 * sp.pi * c ** 3 - 2 * h * G * sp.log(2)) == 0}
    bm = o["plane"].bk_masses()
    r, r0, m, x = bm["syms"]
    adm_edge = sp.simplify(bm["M_adm"].subs(r0, 2 * m))
    gxx_edge = sp.expand(sp.simplify(bm["cxx"].subs(r0, 2 * m)))
    return {"chain_exact": exact, "adm_at_r0_2m": str(adm_edge), "gxx_at_r0_2m": str(gxx_edge),
            "adm_matches": sp.simplify(adm_edge - sp.Rational(5, 4) * m) == 0,
            "gxx_matches": sp.simplify(gxx_edge - (4 * m ** 2 / x ** 2 + 10 * m + 4 * x ** 2)) == 0}


def compute():
    B = bounds()
    return {"bounds": {k: [_digits(a, 45), _digits(b, 45)] for k, (a, b) in B.items()},
            "identities": {k: list(v) for k, v in identities().items()}, "values": values(B), "passage": passage(),
            "drift": drift(), "N_example": N_EXAMPLE, "u_r_G": U_R_G}


def report(d):
    print("exactE.py -- item 134: E, the one exact energy, computed and machine-checked")
    print("  pi  in [%s,\n         %s]" % tuple(d["bounds"]["pi"]))
    print("  ln2 in [%s,\n         %s]  (mpmath interval arithmetic)" % tuple(d["bounds"]["ln2"]))
    print("  IDENTITIES (Z3, universal over the positive reals):")
    for k, (kind, st, vac) in d["identities"].items():
        print("    %-10s %-78s %s%s" % (kind, k, st, "" if vac else "  (HYPOTHESES UNSATISFIABLE)"))
    print("  VALUES (Z3: the encoded root lies in the owner's enclosure, 2e-30 relative; G raised 1e-9 refuted):")
    for v in d["values"]:
        print("    %-44s %s %s  [%s; control %s]" % (v["name"], v["digits"], v["unit"], v["status"], v["control"]))
    p = d["passage"]
    print("  passage factor per leg at r0 = 2m: %s x (E/m), E the ray's normalization -- a coefficient, OPEN;"
          " coin.py's closed form %.15f" % (p["digits"], p["coin"]))
    print("  example N = %d bits (illustrative; N is the input)" % d["N_example"])


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

    for k, (kind, st, vac) in d["identities"].items():
        if kind == "CONTROL":
            chk("%s: Z3 says %s" % (k, st), st == "refuted" and vac, ctl=True)
        elif kind == "STRUCTURAL":
            structural.append("Z3 (by the hypotheses' own arithmetic): %s -- %s" % (k, st))
        else:
            chk("%s: %s (Z3: %s; hypotheses satisfiable: %s)" % (kind, k, st, vac), st == "proved" and vac)
    for v in d["values"]:
        chk("MACHINE-CHECKED: %s = %s %s -- the encoded root lies in the owner's enclosure (Z3 %s); with G raised by "
            "1e-9 the same enclosure is %s" % (v["name"], v["digits"], v["unit"], v["status"], v["control"]),
            v["status"] == "proved" and v["vacuity_ok"] and v["control"] == "refuted")
    p = d["passage"]
    chk("the passage factor per leg at r0 = 2m, -(4/3)[1 - (sqrt3/6) ln(2 + sqrt3)] = %s per unit E/m (geometric), "
        "enclosed to %.1e relative by interval arithmetic, equals coin.py's closed form (relative %.1e) -- a coefficient "
        "per unit ray normalization, OPEN under M-EXACT-VALUES" % (p["digits"], p["rel_width"], p["coin_rel_diff"]),
        p["rel_width"] < 1e-30 and p["coin_rel_diff"] < 1e-12)
    dr = d["drift"]
    chk("DRIFT: chain.py's exact E, r_min and A_bit satisfy the encoded relations exactly (sympy: %s); plane.py's total "
        "and g_xx at r0 = 2m equal the encoded ones (%s; %s)" % (dr["chain_exact"], dr["adm_at_r0_2m"],
                                                              dr["gxx_at_r0_2m"]),
        all(dr["chain_exact"].values()) and dr["adm_matches"] and dr["gxx_matches"])
    structural.append("G's uncertainty, u_r %.1e: E, M and the total carry 1.1e-5 (G^-1/2), m and r0 1.1e-5 (G^1/2), "
                      "A_bit 2.2e-5 (G) -- the enclosures are exact for G = 6.6743e-11 as entered" % d["u_r_G"])
    structural.append("N = %d is the board's illustrative example; E(N) = (E per sqrt(bit)) x sqrt(N) for the user's "
                      "input N (item 130)" % d["N_example"])
    structural.append("the one-way claim rests on the orientation H-FUTURE-INGOING; reversed, it is refuted (control)")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("exactE.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
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
