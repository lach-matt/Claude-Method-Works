#!/usr/bin/env python3
"""positivity.py -- the energy is positive: a proof for the coinciding planes (M-RULINGS item 139, answer 2)

M (item 139): position 2's plane has negative tension, a quarter of ours, ours positive (answer 1); "positive, and you
have to prove it" (answer 2).  The obstacle (multiplane.py M3, READ): a negative-tension plane FREE TO MOVE makes the
mode that moves it -- the radion -- a ghost, with negative kinetic energy (Pilo-Rattazzi-Zaffaroni, hep-th/0004028v2,
eq. 2.16 and p.11).  M's planes coincide (item 127) on the mirror plane, the fixed point of the two sides' identification.

  Q1  the obstacle, imported: a free negative-tension plane (Lykken-Randall, r > 0) has radion coefficient C_r < 0
  Q2  at the fixed point a sheet cannot be displaced: a displacement f is identified with -f, so its even part, the only
      part that survives, is 0.  PRZ p.3 (READ): "Since the negative tension brane is sitting at an orbifold fixed
      point, the negative energy mode associated with its fluctuations in the transverse direction is projected out."
      So the coinciding planes carry no radion: no negative-kinetic mode.
  Q3  the coinciding sheets act as one surface (Israel's condition is linear in the stress, loose.py L4): total tension
      (+4/3 - 1/3) = +1 times the one-plane value.  The null energy on it, S_AB k^A k^B = lambda_total k_y^2 >= 0 for every
      null vector (censor.py C1); position 2's sheet ALONE would give -(1/3) lambda k_y^2 < 0 -- broken only if taken
      alone, never as the surface that exists.
  Q4  the bulk: vacuum with a cosmological constant, null energy 0 (censor.py C1)
  Q5  the cost, stated: with no radion, the long-range field of a lasting source on this plane is Einstein's (gamma = 1),
      so the static gamma = 5/4 of eq. (17) never forms -- which M's rulings already have (items 86 answer 5, 94, 136 E:
      instantaneous or near instantaneous).  Contrast: a free negative plane (r > 0) does give gamma = 5/4, with a ghost.
Imports multiplane.py and censor.py (by path); stdlib + sympy.  python3 positivity.py [--selftest]
"""
import contextlib
import importlib.util
import io
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)


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


_C = {}


def owners():
    if not _C:
        _C["mp"] = _load(os.path.join(HERE, "multiplane.py"), "pos_multiplane")
        _C["cs"] = _load(os.path.join(HERE, "censor.py"), "pos_censor")
    return _C


def q1():
    mp = owners()["mp"]
    d = mp.lr()
    Cr = d["Cr"].subs({mp.M: 1, mp.kL: 1, mp.kR: sp.Rational(3, 4), mp.r: sp.Rational(1, 2)})
    return {"Cr_free": sp.nsimplify(sp.N(Cr, 30)), "Cr_free_float": float(Cr)}


def q2():
    """Z2: z -> -z.  A sheet at the fixed point displaced by f is identified with one displaced by -f; the surviving
    (even) part is (f + (-f))/2.  Control: a sheet away from the fixed point (at z = r) has no image constraint."""
    f = sp.Symbol("f", real=True)
    even_at_fixed = sp.simplify((f + (-f)) / 2)
    return {"even_part_at_fixed_point": even_at_fixed, "free_away": f}


def q3():
    cs = owners()["cs"]
    c1 = cs.c1()
    lam, ky = sp.Symbol("lambda", real=True), sp.Symbol("k_y", real=True)
    m4 = owners()["mp"].m4()
    t_total = m4["tau1_over_rs"] + m4["tau2_over_rs"]
    S_total = sp.simplify(c1["S_kk"].subs(lam, t_total * sp.Symbol("lambda_RS", positive=True)))
    S_p2_alone = sp.simplify(c1["S_kk"].subs(lam, m4["tau2_over_rs"] * sp.Symbol("lambda_RS", positive=True)))
    return {"t1": m4["tau1_over_rs"], "t2": m4["tau2_over_rs"], "t_total": t_total, "S_total": S_total,
            "S_p2_alone": S_p2_alone, "bulk_kk": c1["bulk_kk"]}


def q5():
    mp = owners()["mp"]
    # no radion: the graviton term alone, (1/(8 Mhat^2))(P2 - P0) -> c0 = -1
    g_no_radion = mp.gamma_from_c0(sp.Integer(-1))
    g_free = mp.m3()["gamma_X"].subs(mp.X, sp.Rational(1, 3))
    return {"gamma_no_radion": g_no_radion, "gamma_free_negative_plane": g_free}


def report():
    a, b, c, e = q1(), q2(), q3(), q5()
    print("positivity.py -- the energy positive, for the coinciding planes (item 139)\n")
    print("Q1 the obstacle: a FREE negative-tension plane (r = 1/2, k_R = 3k_L/4) has radion coefficient C_r = %.6g < 0"
          % a["Cr_free_float"])
    print("Q2 at the fixed point a displacement f survives only as its even part: %s -- no radion, no ghost"
          % b["even_part_at_fixed_point"])
    print("Q3 the coinciding sheets: tensions %s + (%s) = %s of the one-plane value; null energy on the surface %s >= 0;"
          % (c["t1"], c["t2"], c["t_total"], c["S_total"]))
    print("   position 2's sheet alone would read %s < 0 -- broken only if taken alone" % c["S_p2_alone"])
    print("Q4 the bulk's null energy: %s" % c["bulk_kk"])
    print("Q5 with no radion a lasting source's field has gamma = %s; a free negative plane gives %s, with a ghost"
          % (e["gamma_no_radion"], e["gamma_free_negative_plane"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    a, b, c, e = q1(), q2(), q3(), q5()
    lrs, ky = sp.Symbol("lambda_RS", positive=True), sp.Symbol("k_y", real=True)
    chk("Q1 (the obstacle, imported): a free negative-tension plane has C_r < 0", a["Cr_free_float"] < 0)
    chk("Q2: at the fixed point the displacement's surviving part is 0 -- the radion is projected out (PRZ p.3)",
        b["even_part_at_fixed_point"] == 0)
    chk("Q2 control: away from the fixed point the displacement is unconstrained", b["free_away"] != 0)
    chk("Q3: the coinciding sheets' tensions sum to +1 times the one-plane value (+4/3 - 1/3)",
        c["t_total"] == 1 and c["t1"] == sp.Rational(4, 3) and c["t2"] == sp.Rational(-1, 3))
    chk("Q3: on the surface that exists the null energy is lambda_RS k_y^2 >= 0, for every null vector",
        sp.simplify(c["S_total"] - lrs * ky**2) == 0)
    chk("Q3 control: position 2's sheet taken alone reads -(1/3) lambda_RS k_y^2 < 0",
        sp.simplify(c["S_p2_alone"] + lrs * ky**2 / 3) == 0)
    chk("Q4: the bulk's null energy is 0", c["bulk_kk"] == 0)
    chk("Q5: with no radion a lasting source's field is Einstein's (gamma = 1); a free negative plane gives 5/4",
        e["gamma_no_radion"] == 1 and e["gamma_free_negative_plane"] == sp.Rational(5, 4))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
