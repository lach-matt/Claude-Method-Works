#!/usr/bin/env python3
"""positivity.py -- is the energy positive on M's coinciding planes?  (M-RULINGS item 139, answer 2)

M (item 139): position 2's plane has negative tension, a quarter of ours, ours positive (answer 1); "positive, and you
have to prove it" (answer 2).  This instrument tries, and reports what holds and what does not.

Two kinds of positivity, kept apart:
  BACKGROUND -- the stress of the surfaces and the bulk as they sit: the null energy condition on them.
  DYNAMICAL  -- no mode with negative kinetic energy (a ghost).  Pilo-Rattazzi-Zaffaroni (hep-th/0004028v2, READ): in the
                Lykken-Randall bulk the mode that moves the second plane, the radion, has kinetic coefficient C_r
                (eq. 2.16), negative whenever that plane's tension is negative (p.11).

  Q1  the radion's coefficient C_r, apart (r = 1/2) and at the coinciding endpoint (r = 0): both negative
  Q2  which configurations keep a moving mode, by the mirror identification y -> -y:
        (a) position 2's plane as LR has it -- a sheet at +r with its image at -r: displacing both by f stays mirror-
            symmetric for every f, so the mode survives, also from r = 0 (PRZ p.4: "the translational degrees of
            freedom of this brane are not projected out"; the board's earlier step 1 missed this);
        (b) control: one sheet that is its own image at the mirror plane: only f = 0 is symmetric (PRZ p.3)
  Q3  BACKGROUND, the surfaces: tensions +4/3 and -1/3 of the one-plane value (the -1/3 is the pair, sheet plus image:
      PRZ's jump rule gives one sheet -1/6); summed, +1: null energy lambda k_y^2 >= 0 on the surface (censor.py C1)
  Q4  the plane's own reading: averaged null energy along the passage, -0.826436 E/m per leg (coin.py; censor.py C6)
  Q5  the cost and the alternative: if position 2's sheets are FUSED with ours into one self-image surface (Q2 b),
      there is no radion, the energy is dynamically positive -- and the bulk is one Randall-Sundrum plane (gamma = 1);
      nothing then fixes the quarter
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
        _C["coin"] = _load(os.path.join(D68, "copy", "coin.py"), "pos_coin")
    return _C


def q1():
    mp = owners()["mp"]
    Cr = mp.lr()["Cr"]
    vals = {}
    for rv in (sp.Rational(1, 2), sp.Integer(0)):
        vals[str(rv)] = sp.simplify(Cr.subs({mp.M: 1, mp.kL: 1, mp.kR: sp.Rational(3, 4), mp.r: rv}))
    return vals


def symmetric(config, f):
    """Is the displaced configuration (a list of sheet positions, as sympy expressions in f) mapped onto itself by
    y -> -y?  Returns the set of f (as a sympy condition) for which it is."""
    imaged = sorted([sp.expand(-y) for y in config], key=sp.default_sort_key)
    orig = sorted([sp.expand(y) for y in config], key=sp.default_sort_key)
    return all(sp.simplify(a - b) == 0 for a, b in zip(orig, imaged))


def q2():
    f, r = sp.symbols("f r", real=True)
    pair = [r + f, -(r + f)]                                       # LR: the sheet at +r and its image, both moved by f
    pair_at_0 = [f, -f]                                            # the same pair from the coinciding endpoint r = 0
    single = [f]                                                   # one sheet that is its own image, moved by f
    return {"pair_generic": symmetric(pair, f), "pair_from_r0": symmetric(pair_at_0, f),
            "single_generic": symmetric(single, f), "single_at_f0": symmetric([sp.Integer(0)], f)}


def q3():
    cs, mp = owners()["cs"], owners()["mp"]
    lam, ky = sp.Symbol("lambda", real=True), sp.Symbol("k_y", real=True)
    lrs = sp.Symbol("lambda_RS", positive=True)
    m4 = mp.m4()
    S = cs.c1()["S_kk"]
    total = m4["tau1_over_rs"] + m4["tau2_over_rs"]
    # PRZ's jump rule Delta phi' = -tau/(12 M^3): one sheet at z = r has 12 M^3 (k_R - k_L); the pair (sheet + image) 24
    one_sheet = sp.Rational(1, 2) * m4["tau2_over_rs"]
    return {"t1": m4["tau1_over_rs"], "t2_pair": m4["tau2_over_rs"], "t2_one_sheet": one_sheet, "total": total,
            "S_total": sp.simplify(S.subs(lam, total * lrs)), "S_pair_alone": sp.simplify(S.subs(lam, m4["tau2_over_rs"] * lrs)),
            "sum_with_one_sheet": m4["tau1_over_rs"] + one_sheet}


def q4():
    return {"leg": float(owners()["coin"].anec_closed(1, 2))}


def q5():
    mp = owners()["mp"]
    return {"gamma_fused": mp.gamma_from_c0(sp.Integer(-1)), "gamma_free_pair": mp.m4()["gamma"]}


def report():
    a, b, c, d, e = q1(), q2(), q3(), q4(), q5()
    print("positivity.py -- is the energy positive on M's coinciding planes? (item 139)\n")
    print("Q1 DYNAMICAL: the radion's coefficient C_r (k_R = 3k_L/4, units M = k_L = 1): apart %s; at r = 0 %s"
          % (a["1/2"], a["0"]))
    print("Q2 which configurations keep the moving mode (mirror-symmetric for every f?):")
    print("   position 2's plane as a mirror pair: %s; from the coinciding endpoint r = 0: %s -- the mode survives"
          % (b["pair_generic"], b["pair_from_r0"]))
    print("   control, one self-image sheet: symmetric for every f? %s; at f = 0: %s -- only that one is pinned"
          % (b["single_generic"], b["single_at_f0"]))
    print("Q3 BACKGROUND: tensions %s and %s (the pair; one sheet %s), summed %s; null energy on the summed surface %s;"
          % (c["t1"], c["t2_pair"], c["t2_one_sheet"], c["total"], c["S_total"]))
    print("   the pair alone %s" % c["S_pair_alone"])
    print("Q4 the plane's reading: averaged null energy along the passage %.6f E/m per leg" % d["leg"])
    print("Q5 fused into one self-image surface: no radion, gamma = %s (one Randall-Sundrum plane); the free pair gives "
          "gamma = %s with C_r < 0" % (e["gamma_fused"], e["gamma_free_pair"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    a, b, c, d, e = q1(), q2(), q3(), q4(), q5()
    lrs, ky = sp.Symbol("lambda_RS", positive=True), sp.Symbol("k_y", real=True)
    chk("Q1: the radion's coefficient is negative apart (r = 1/2) and at the coinciding endpoint (r = 0): a ghost both",
        a["1/2"] < 0 and a["0"] < 0)
    chk("Q2: position 2's plane as a mirror pair stays symmetric for every displacement, from r = 0 too: the mode lives",
        b["pair_generic"] and b["pair_from_r0"])
    chk("Q2 control: one sheet that is its own image is symmetric only undisplaced: that mode is pinned",
        (not b["single_generic"]) and b["single_at_f0"])
    chk("Q3: the -1/3 is the pair (sheet + image): with one sheet (-1/6) the sum rule fails; with the pair it closes",
        c["sum_with_one_sheet"] != 1 and c["total"] == 1)
    chk("Q3 BACKGROUND: on the summed surface the null energy is lambda_RS k_y^2 >= 0 for every null vector",
        sp.simplify(c["S_total"] - lrs * ky**2) == 0)
    chk("Q3 control: the pair taken alone reads -(1/3) lambda_RS k_y^2 < 0",
        sp.simplify(c["S_pair_alone"] + lrs * ky**2 / 3) == 0)
    chk("Q4: the plane's averaged null energy along the passage is negative (the 4D reading)", d["leg"] < 0)
    chk("Q5 (structural): fused, the field is Einstein's (gamma = 1); the free pair gives 5/4 with a ghost",
        e["gamma_fused"] == 1 and e["gamma_free_pair"] == sp.Rational(5, 4))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
