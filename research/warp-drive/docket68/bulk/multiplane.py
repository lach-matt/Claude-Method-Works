#!/usr/bin/env python3
"""multiplane.py -- can a bulk of more than one plane give the corridor's far field?  (M-RULINGS item 138)

M (item 138): "the problem is that you assume the bulk is contained to a single plain. It is not. I keep saying, it is
multi-universal."  The corridor's far field (eq. 17 at r0 = 2m) has gamma = beta = 5/4 (kscale.py P; Casadio-Fabbri-
Mazzacurati eq. 8).  A single Randall-Sundrum II plane gives gamma = 1 (Maartens-Koyama eq. 155).  This asks what a
bulk with more planes gives.

READ at source (alphaXiv): Garriga & Tanaka, "Gravity in the Randall-Sundrum Brane World", hep-th/9911055v4.
  p.7 eq. (27): on a plane of the two-plane bulk, gravity is linearized Brans-Dicke with
      omega(+-) = (3/2)(e^(+-2d/ell) - 1)        (+ the positive-tension plane, - the negative one; d the separation)
  p.7: "In the Einstein frame, the kinetic term for the BD field has the usual sign for omega_BD > -3/2."
  p.7-8, eq. (25): matter on the other plane ("shadow matter") gravitates on ours through the first term alone, giving
      h00 = 2 h_zz, and "for the same Newtonian mass the deflection of light rays caused by shadow matter is 25%
      smaller than in Einstein gravity".
Brans-Dicke's post-Newtonian gamma is (1 + omega)/(2 + omega) (Will, as cited there [10]; standard, the board's
formula); light bends by (1 + gamma)/2.

  M1  gamma on each plane, over every separation d: the positive-tension plane (1/2, 1); the negative (-1, 1/2)
  M2  shadow matter: gamma = 1/2 (h00 = 2 h_zz), light bending 3/4 -- the 25% READ
  M3  gamma = 5/4 needs omega = -6, below -3/2: a scalar with the wrong-sign kinetic term (GT p.7)
Stdlib + sympy.  python3 multiplane.py [--selftest]
"""
import sys

import sympy as sp

d, ell, w = sp.symbols("d ell omega", positive=True)
x = sp.Symbol("x", positive=True)                                  # x = d/ell


def gamma_bd(omega):
    return (1 + omega) / (2 + omega)


def m1():
    wp = sp.Rational(3, 2) * (sp.exp(2 * x) - 1)
    wm = sp.Rational(3, 2) * (sp.exp(-2 * x) - 1)
    gp, gm = sp.simplify(gamma_bd(wp)), sp.simplify(gamma_bd(wm))
    return {"omega_plus": wp, "omega_minus": wm, "gamma_plus": gp, "gamma_minus": gm,
            "gp_limits": (sp.limit(gp, x, 0, "+"), sp.limit(gp, x, sp.oo)),
            "gm_limits": (sp.limit(gm, x, 0, "+"), sp.limit(gm, x, sp.oo)),
            "dgp": sp.simplify(sp.diff(gp, x)), "dgm": sp.simplify(sp.diff(gm, x))}


def m2():
    """Shadow matter: h00 = 2 h_zz (GT p.8), so gamma = h_zz/h00 = 1/2 in the far field."""
    g = sp.Rational(1, 2)
    return {"gamma": g, "deflection": (1 + g) / 2}


def m3():
    sol = sp.solve(sp.Eq(gamma_bd(sp.Symbol("o")), sp.Rational(5, 4)), sp.Symbol("o"))
    return {"omega_for_5_4": sol[0], "healthy": sol[0] > sp.Rational(-3, 2)}


def report():
    a, b, c = m1(), m2(), m3()
    print("multiplane.py -- what a bulk of more than one plane gives on our plane (item 138)\n")
    print("M1 two planes, every separation (Garriga-Tanaka eq. 27):")
    print("   positive-tension plane: omega = %s, gamma = %s, from %s (d -> 0) to %s (d -> oo)"
          % (a["omega_plus"], a["gamma_plus"], a["gp_limits"][0], a["gp_limits"][1]))
    print("   negative-tension plane: omega = %s, gamma = %s, from %s (d -> 0) to %s (d -> oo)"
          % (a["omega_minus"], a["gamma_minus"], a["gm_limits"][0], a["gm_limits"][1]))
    print("M2 shadow matter on the other plane: gamma = %s, light bends x %s (GT: 25%% weaker)"
          % (b["gamma"], b["deflection"]))
    print("M3 the corridor's gamma = 5/4 needs omega = %s; a healthy scalar needs omega > -3/2: %s"
          % (c["omega_for_5_4"], c["healthy"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    a, b, c = m1(), m2(), m3()
    chk("M1: on the positive-tension plane gamma runs from 1/2 to 1 and rises monotonically with d",
        a["gp_limits"] == (sp.Rational(1, 2), 1) and all(float(a["dgp"].subs(x, v)) > 0 for v in (0.1, 1, 3)))
    chk("M1: on the negative-tension plane gamma runs from 1/2 down to -1",
        a["gm_limits"] == (sp.Rational(1, 2), -1) and all(float(a["dgm"].subs(x, v)) < 0 for v in (0.1, 1, 3)))
    chk("M1: so on either plane, at every separation, gamma < 1",
        all(float(a["gamma_plus"].subs(x, v)) < 1 and float(a["gamma_minus"].subs(x, v)) < 1
            for v in (0.01, 0.5, 2, 10)))
    chk("M1 control: far separation on the positive plane recovers Einstein's gamma = 1 (one plane, GT p.6)",
        a["gp_limits"][1] == 1)
    chk("M2: shadow matter has gamma = 1/2 and bends light 3/4 as much -- Garriga-Tanaka's 25% (READ)",
        b["gamma"] == sp.Rational(1, 2) and b["deflection"] == sp.Rational(3, 4))
    chk("M3: gamma = 5/4 needs omega = -6, which is below -3/2: the wrong-sign scalar (GT p.7)",
        c["omega_for_5_4"] == -6 and not c["healthy"])
    chk("M3 control: gamma = 1 is omega -> infinity, gamma = 1/2 is omega = 0",
        sp.limit(gamma_bd(w), w, sp.oo) == 1 and gamma_bd(sp.Integer(0)) == sp.Rational(1, 2))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
