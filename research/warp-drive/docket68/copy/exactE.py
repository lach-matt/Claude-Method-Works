#!/usr/bin/env python3
"""exactE.py -- DOCKET 68, M-RULINGS item 134: compute E, the one exact energy, and machine-check E and every value
derived from the coefficients.  Deduced, computed and machine-checked; not verified; not seated.  Write-up: EXACTE.md.

M's words (verbatim in the rulings file): item 134 "Seat them and then compute E. Machine check E and all the values
derived from the coefficients."; item 133 "There is only one exact energy needed for any given README" (identified by
the board with E(N) at the bound, H-EXACT-ENERGY-AT-BOUND); item 130: N is the user's input, read from the object;
item 125: no general coefficients.

THE ROUTE (PROOF-ASSISTANT.md): Z3, an SMT solver.  A claim is checked by asserting its negation together with its
hypotheses and asking for a model: unsat = no counterexample exists.  Two kinds of obligation here:
  IDENTITIES -- universal over the reals: every positive h, c, G, pi, ln2, N (and m, x where they appear), not one
     point.  Square roots enter as positive roots of their squares (E > 0, E^2 = ...), so the claims are polynomial and
     Z3's nonlinear real arithmetic decides them.
  VALUES -- rigorous enclosures: h = 6.62607015e-34 and c = 299792458 exactly (SI 2019), G = 6.6743e-11 (CODATA 2018,
     entered exactly, u_r 2.2e-5 named), pi and ln2 bounded by mpmath's interval arithmetic (rigorous outward rounding);
     Z3 proves lo <= value <= hi for EVERY pi and ln2 in those bounds.  A transcendental value (the passage's factor,
     with ln(2 + sqrt3)) is enclosed by interval arithmetic itself; its algebraic core, artanh(sqrt3/2) = ln(2 + sqrt3),
     i.e. tanh(ln(2 + sqrt3)) = sqrt3/2, is a Z3 identity.
GUARDS (PROOF-ASSISTANT.md's two): VACUITY -- every obligation's hypotheses are satisfiable on their own (else unsat is
empty); ENCODING DRIFT -- each Z3 encoding, evaluated at sampled points, matches the owner's own closed form (chain.py's
exact coefficients, plane.py's masses and g_xx), so the solver is not proving a mistyped formula.  CONTROLS -- deliberately
wrong claims (a coefficient off by one part in 1e9; r0 = 3m/2; the opposite chart's crossing) must come back sat.

WHAT IS CHECKED (each printed with its status)
  E   = sqrt(N h c^5 ln2/(8 pi^2 G))      J        -- coefficient per sqrt(bit), enclosed; the README example evaluated
  m   = G E / c^4 = r_min / 2              m        -- the pull (PLANE.md point 2)
  r0  = r_min = sqrt(N h G ln2/(2 pi^2 c^3)) = 2m   -- the throat on the horizon (current.py X6, item 133)
  A_bit = 2 h G ln2/(pi c^3), 4 pi r0^2 = N A_bit   -- the throat and the horizon each hold N bits
  E r_min = N h c ln2/(4 pi^2)                     -- Bekenstein's bound saturated
  M = E / c^2                                       -- the pull as a mass
  ADM = m/4 + r0/2 = 5m/4; ADM - pull = m/4        -- plane.py's masses at r0 = 2m
  g_tt g_xx = 2(m + 2x^2) at r0 = 2m               -- the ingoing chart regular (current.py X7)
  the cone at the throat: xdot <= 0                 -- one way (X7); the outgoing chart's opposite as control
  leg = -(4/3m)[1 - (sqrt3/6) ln(2 + sqrt3)] E      -- the passage per leg at r0 = 2m, enclosed

NAMED HYPOTHESES
  M's: H-ONE-EXACT-ENERGY (133), H-N-IS-INPUT (130), H-THROAT-CARRIES-README (131), H-HORIZON-AND-THROAT-HOLD,
    H-ONE-WAY-BY-NATURE (132), M-EXACT-VALUES (125).
  The board's: H-EXACT-ENERGY-AT-BOUND (133's energy is E(N) at the bound); H-STRONG-BOUND, H-HORIZON-HOLDS,
    H-THROAT-AT-BOUND (chain.py, PLANE.md, current.py); H-CORE-README (the example N, illustrative).

USAGE
    python3 exactE.py | --selftest | --json      (z3, sympy, mpmath; under a minute)
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
    """Imported, never copied: chain.py (the exact coefficients), plane.py (the corridor's masses and g_xx)."""
    if not _CACHE:
        _CACHE["chain"] = _load(os.path.join(HERE, "chain.py"), "copy_chain_exactE")
        _CACHE["plane"] = _load(os.path.join(HERE, "plane.py"), "copy_plane_exactE")
    return _CACHE


def bounds():
    """Rigorous rational bounds on pi and ln2 from mpmath's interval arithmetic (outward rounding)."""
    import mpmath as mp
    mp.iv.dps = 40
    pi, l2 = mp.iv.pi, mp.iv.log(2)
    return {"pi": (Fraction(*_ratio(pi.a)), Fraction(*_ratio(pi.b))),
            "ln2": (Fraction(*_ratio(l2.a)), Fraction(*_ratio(l2.b)))}


def _ratio(x):
    """An mpf endpoint as an exact (numerator, denominator)."""
    import mpmath as mp
    with mp.workdps(80):                       # keep the endpoint's every bit (the default 15 digits would round it)
        v = mp.mpf(x)
        sgn = -1 if v < 0 else 1
        man, exp = abs(v).man_exp
    man *= sgn
    return (man * 2 ** exp, 1) if exp >= 0 else (man, 2 ** (-exp))


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
    """Universal obligations over the reals.  Returns {name: (status, hypotheses satisfiable)}."""
    import z3
    h, c, G, P, L, N, E, r, m, A, x, s3 = z3.Reals("h c G P L N E r m A x s3")
    pos = [h > 0, c > 0, G > 0, P > 0, L > 0, N > 0]
    E_def = [E > 0, E * E * 8 * P * P * G == N * h * c ** 5 * L]
    r_def = [r > 0, r * r * 2 * P * P * c ** 3 == N * h * G * L]
    out = {}
    out["m = G E/c^4 = r_min/2"] = _solve(pos + E_def + r_def, r * c ** 4 == 2 * G * E)
    out["E r_min = N h c ln2/(4 pi^2)"] = _solve(pos + E_def + r_def, E * r * 4 * P * P == N * h * c * L)
    out["4 pi r_min^2 = N A_bit, A_bit = 2 h G ln2/(pi c^3)"] = _solve(
        pos + r_def + [A * P * c ** 3 == 2 * h * G * L], 4 * P * r * r == N * A)
    # the corridor's member: throat r0 = r_min, pull m = G E/c^4 -> r0 = 2m
    out["r0 = r_min and m = G E/c^4 give r0 = 2m"] = _solve(
        pos + E_def + r_def + [m * c ** 4 == G * E], r == 2 * m)
    M = z3.Real("M")
    out["M = E/c^2 = m c^2/G"] = _solve(pos + E_def + [m * c ** 4 == G * E, M * c * c == E], M * G == m * c * c)
    adm, pull = z3.Reals("adm pull")
    out["ADM = m/4 + r0/2 = 5m/4 at r0 = 2m; ADM - pull = m/4"] = _solve(
        [m > 0, adm == m / 4 + (2 * m) / 2, pull == m], z3.And(adm == 5 * m / 4, adm - pull == m / 4))
    gtt = x * x / (2 * m + x * x)
    gxx = 4 * m * m / (x * x) + 10 * m + 4 * x * x
    out["g_tt g_xx = 2(m + 2x^2) at r0 = 2m (x != 0)"] = _solve([m > 0, x != 0], gtt * gxx == 2 * (m + 2 * x * x))
    # the cone at the throat (g_vv = 0 there, g_vx = +h ingoing): future causal => xdot <= 0
    hh, vd, xd = z3.Reals("hh vd xd")
    cone = [hh > 0, hh * hh == 2 * m, m > 0, 2 * hh * vd * xd <= 0,
            z3.Or(vd > 0, z3.And(vd == 0, hh * xd < 0))]
    out["one way: the future cone at the throat has xdot <= 0"] = _solve(cone, xd <= 0)
    # control: the outgoing chart (g_vx = -h, reference +d_x) -- 'xdot <= 0' must be refuted
    cone_out = [hh > 0, hh * hh == 2 * m, m > 0, -2 * hh * vd * xd <= 0,
                z3.Or(vd > 0, z3.And(vd == 0, -hh * xd < 0))]
    out["CONTROL outgoing chart: 'xdot <= 0' must fail"] = _solve(cone_out, xd <= 0)
    # artanh(sqrt3/2) = ln(2 + sqrt3): tanh(ln u) = (u^2 - 1)/(u^2 + 1) with u = 2 + sqrt3
    u = 2 + s3
    out["tanh(ln(2 + sqrt3)) = sqrt3/2"] = _solve([s3 > 0, s3 * s3 == 3], (u * u - 1) * 2 == s3 * (u * u + 1))
    # control: r0 = 3m/2 (the Schwarzschild edge) is not the corridor's member
    out["CONTROL r0 = 3m/2 must fail"] = _solve(pos + E_def + r_def + [m * c ** 4 == G * E], 2 * r == 3 * m)
    return out


def values(B):
    """Rigorous enclosures, Z3-proved for every pi, ln2 in their interval bounds.  Returns rows."""
    import z3
    import mpmath as mp
    P, L, X = z3.Reals("P L X")
    pl, ph = B["pi"]
    ll, lh = B["ln2"]
    box = [P >= _q(pl), P <= _q(ph), L >= _q(ll), L <= _q(lh)]
    h, c, G = _q(H_SI), _q(C_SI), _q(G_SI)
    mp.iv.dps = 40
    ivpi, ivl2 = mp.iv.pi, mp.iv.log(2)
    hI, cI, GI = mp.iv.mpf(str(H_SI.numerator)) / H_SI.denominator, mp.iv.mpf(str(C_SI)), \
        mp.iv.mpf(str(G_SI.numerator)) / G_SI.denominator
    Ni = mp.iv.mpf(N_EXAMPLE)
    specs = [
        # name, unit, interval value, z3 relation defining X (X > 0 and polynomial), tag
        ("E per sqrt(bit)", "J", mp.iv.sqrt(hI * cI ** 5 * ivl2 / (8 * ivpi ** 2 * GI)),
         X * X * 8 * P * P * G == h * c ** 5 * L),
        ("m per sqrt(bit)", "m", mp.iv.sqrt(hI * GI * ivl2 / (2 * ivpi ** 2 * cI ** 3)) / 2,
         4 * X * X * 2 * P * P * c ** 3 == h * G * L),
        ("r0 = r_min = 2m per sqrt(bit)", "m", mp.iv.sqrt(hI * GI * ivl2 / (2 * ivpi ** 2 * cI ** 3)),
         X * X * 2 * P * P * c ** 3 == h * G * L),
        ("A_bit, area per bit", "m^2", 2 * hI * GI * ivl2 / (ivpi * cI ** 3),
         X * P * c ** 3 == 2 * h * G * L),
        ("M = E/c^2 per sqrt(bit)", "kg", mp.iv.sqrt(hI * cI ** 5 * ivl2 / (8 * ivpi ** 2 * GI)) / cI ** 2,
         X * X * c ** 4 * 8 * P * P * G == h * c ** 5 * L),
        ("E at the example N", "J", mp.iv.sqrt(Ni * hI * cI ** 5 * ivl2 / (8 * ivpi ** 2 * GI)),
         X * X * 8 * P * P * G == N_EXAMPLE * h * c ** 5 * L),
        ("m at the example N", "m", mp.iv.sqrt(Ni * hI * GI * ivl2 / (2 * ivpi ** 2 * cI ** 3)) / 2,
         4 * X * X * 2 * P * P * c ** 3 == N_EXAMPLE * h * G * L),
        ("r0 at the example N", "m", mp.iv.sqrt(Ni * hI * GI * ivl2 / (2 * ivpi ** 2 * cI ** 3)),
         X * X * 2 * P * P * c ** 3 == N_EXAMPLE * h * G * L),
        ("M at the example N", "kg", mp.iv.sqrt(Ni * hI * cI ** 5 * ivl2 / (8 * ivpi ** 2 * GI)) / cI ** 2,
         X * X * c ** 4 * 8 * P * P * G == N_EXAMPLE * h * c ** 5 * L),
        ("ADM total at the example N (5/4 of the pull)", "kg",
         mp.iv.mpf(5) / 4 * mp.iv.sqrt(Ni * hI * cI ** 5 * ivl2 / (8 * ivpi ** 2 * GI)) / cI ** 2,
         16 * X * X * c ** 4 * 8 * P * P * G == 25 * N_EXAMPLE * h * c ** 5 * L),
    ]
    rows = []
    for name, unit, iv, rel in specs:
        lo = Fraction(*_ratio(iv.a)) * (1 - Fraction(1, 10 ** 30))
        hi = Fraction(*_ratio(iv.b)) * (1 + Fraction(1, 10 ** 30))
        st, vac = _solve(box + [X > 0, rel], z3.And(X >= _q(lo), X <= _q(hi)))
        mid = (lo + hi) / 2
        # control: a claimed value one part in 1e9 too high must be refuted
        wrong = mid * (1 + Fraction(1, 10 ** 9))
        stc, _ = _solve(box + [X > 0, rel], z3.And(X >= _q(wrong * (1 - Fraction(1, 10 ** 12))),
                                                  X <= _q(wrong * (1 + Fraction(1, 10 ** 12)))))
        rows.append({"name": name, "unit": unit, "value": float(mid), "lo": float(lo), "hi": float(hi),
                     "digits": _digits(mid, 20), "lo_digits": _digits(lo, 25), "hi_digits": _digits(hi, 25),
                     "status": st,
                     "vacuity_ok": vac, "control": stc,
                     "rel_width": float((hi - lo) / mid)})
    # the passage factor at r0 = 2m: transcendental, enclosed by interval arithmetic
    s3 = mp.iv.sqrt(3)
    leg = -mp.iv.mpf(4) / 3 * (1 - s3 / 6 * mp.iv.log(2 + s3))
    rows.append({"name": "passage factor per leg, -(4/3)[1 - (sqrt3/6) ln(2 + sqrt3)] (x E/m)", "unit": "1",
                 "value": float(mp.mpf(leg.mid)), "lo": float(mp.mpf(leg.a)), "hi": float(mp.mpf(leg.b)),
                 "digits": _digits(Fraction(*_ratio(leg.mid)), 20), "status": "enclosed (interval arithmetic)",
                 "vacuity_ok": True, "lo_digits": _digits(Fraction(*_ratio(leg.a)), 25),
                 "hi_digits": _digits(Fraction(*_ratio(leg.b)), 25),
                 "control": None, "rel_width": float(mp.mpf(leg.delta) / abs(mp.mpf(leg.mid)))})
    return rows


def drift():
    """ENCODING DRIFT: the encodings above against the owners' own closed forms, at sampled points."""
    import sympy as sp
    o = owners()
    co = o["chain"].coefficients()
    hS, cS, GS = sp.Rational(str(H_SI.numerator), str(H_SI.denominator)), sp.Integer(299792458), \
        sp.Rational(str(G_SI.numerator), str(G_SI.denominator))
    mine = {"E_min_J_per_sqrt_bit": sp.sqrt(hS * cS ** 5 * sp.log(2) / (8 * sp.pi ** 2 * GS)),
            "r_min_m_per_sqrt_bit": sp.sqrt(hS * GS * sp.log(2) / (2 * sp.pi ** 2 * cS ** 3)),
            "neck_area_m2_per_bit": 2 * hS * GS * sp.log(2) / (sp.pi * cS ** 3)}
    res = {k: float(abs(sp.N(v / sp.sympify(co[k]["exact"]) - 1, 30))) for k, v in mine.items()}
    bm = o["plane"].bk_masses()
    r, r0, m, x = bm["syms"]
    adm_edge = sp.simplify(bm["M_adm"].subs(r0, 2 * m))
    gxx_edge = sp.expand(sp.simplify(bm["cxx"].subs(r0, 2 * m)))
    return {"chain_rel_diff": res, "adm_at_r0_2m": str(adm_edge), "gxx_at_r0_2m": str(gxx_edge),
            "adm_matches": sp.simplify(adm_edge - sp.Rational(5, 4) * m) == 0,
            "gxx_matches": sp.simplify(gxx_edge - (4 * m ** 2 / x ** 2 + 10 * m + 4 * x ** 2)) == 0}


def compute():
    B = bounds()
    return {"bounds": {k: [_digits(a, 30), _digits(b, 30)] for k, (a, b) in B.items()},
            "identities": {k: list(v) for k, v in identities().items()}, "values": values(B), "drift": drift(),
            "N_example": N_EXAMPLE, "u_r_G": U_R_G}


def report(d):
    print("exactE.py -- item 134: E, the one exact energy, computed and machine-checked")
    print("  pi in [%s, %s], ln2 in [%s, %s] (mpmath interval arithmetic, 40 digits)" % (
        d["bounds"]["pi"][0], d["bounds"]["pi"][1], d["bounds"]["ln2"][0], d["bounds"]["ln2"][1]))
    print("  IDENTITIES (Z3, for every positive h, c, G, pi, ln2, N):")
    for k, (st, vac) in d["identities"].items():
        print("    %-58s %s%s" % (k, st, "" if vac else "  (HYPOTHESES UNSATISFIABLE)"))
    print("  VALUES (Z3-proved enclosures; h, c exact; G entered exactly, u_r %.1e):" % d["u_r_G"])
    for v in d["values"]:
        print("    %-52s %s %s  [%s]" % (v["name"], v["digits"], v["unit"], v["status"]))
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

    ids = d["identities"]
    for k, (st, vac) in ids.items():
        if k.startswith("CONTROL"):
            chk("%s: Z3 says %s" % (k, st), st == "refuted" and vac, ctl=True)
        else:
            chk("MACHINE-CHECKED: %s (Z3: %s; hypotheses satisfiable: %s)" % (k, st, vac), st == "proved" and vac)
    for v in d["values"]:
        if v["control"] is None:
            chk("ENCLOSED: %s = %s (interval width %.1e relative)" % (v["name"], v["digits"], v["rel_width"]),
                v["lo"] <= v["value"] <= v["hi"] and v["rel_width"] < 1e-25)
        else:
            chk("MACHINE-CHECKED: %s = %s %s (Z3 enclosure %s, width %.1e relative; a value 1e-9 high %s)" % (
                v["name"], v["digits"], v["unit"], v["status"], v["rel_width"], v["control"]),
                v["status"] == "proved" and v["vacuity_ok"] and v["control"] == "refuted" and v["rel_width"] < 1e-20)
    dr = d["drift"]
    worst = max(dr["chain_rel_diff"].values())
    chk("ENCODING DRIFT: the encoded E, r_min and A_bit match chain.py's exact coefficients (worst relative %.1e); the "
        "encoded ADM and g_xx at r0 = 2m match plane.py's (%s; %s)" % (worst, dr["adm_at_r0_2m"], dr["gxx_at_r0_2m"]),
        worst < 1e-25 and dr["adm_matches"] and dr["gxx_matches"])
    structural.append("the values carry G's uncertainty, u_r %.1e (E, M per sqrt(bit): 1.1e-5; m, r0: 1.1e-5; A_bit: "
                      "2.2e-5) -- the enclosures are exact for G = 6.6743e-11 as entered" % d["u_r_G"])
    structural.append("N = %d is the board's illustrative example; E(N) = (E per sqrt(bit)) x sqrt(N) for the user's "
                      "input N (item 130)" % d["N_example"])
    structural.append("the passage factor is transcendental (ln(2 + sqrt3)): interval arithmetic encloses it; its "
                      "algebraic core, tanh(ln(2 + sqrt3)) = sqrt3/2, is the Z3 identity above")
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
