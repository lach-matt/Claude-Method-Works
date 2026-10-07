#!/usr/bin/env python3
"""multiplane.py -- can a bulk of more than one plane give the corridor's far field?  (M-RULINGS item 138)

M (item 138): "the problem is that you assume the bulk is contained to a single plain. It is not. I keep saying, it is
multi-universal."  The corridor's far field (eq. 17 at r0 = 2m) has gamma = beta = 5/4 (kscale.py P; Casadio-Fabbri-
Mazzacurati eq. 8).  One Randall-Sundrum II plane gives gamma = 1 (Maartens-Koyama eq. 155).

The post-Newtonian gamma from a propagator's tensor structure.  On a plane, one-graviton exchange between static
sources goes as (P2 + c0 P0)/q^2 (Pilo-Rattazzi-Zaffaroni's normalisation: Einstein is c0 = -1, eq. 3.1; a massive
graviton c0 = -2/3, eq. 3.2).  Then h_mu nu ~ T_mu nu + (c0/2) eta_mu nu T, so for a static source
gamma = h_ii / h_00 = -c0 / (2 + c0).

READ at source (alphaXiv):
  Pilo, Rattazzi, Zaffaroni, hep-th/0004028v2 -- the Lykken-Randall (LR) two-plane bulk, warp -k_L z for 0 <= z <= r,
    -k_R z + (k_R - k_L) r beyond (eq. 2.3); tensions tau1 = 24 M^3 k_L, tau2 = 24 M^3 (k_R - k_L) (p.3); radion kinetic
    coefficient C_r = (24 M^3/k_L)(e^{2 k_L r} k_R/(k_R - k_L) - 1) (eq. 2.16); Planck mass
    2 Mhat^2 = (2 M^3/k_L)(1 + e^{-2 k_L r}(k_L - k_R)/k_R) (eq. 2.17); the zero-mode propagator on our plane
    (1/(8 Mhat^2))(P2 - (2/3) P0)/q^2 - (1/(24 M_L^2)) P0/q^2 with M_L^2 = M^3/k_L (eq. 3.3); and the identity
    1/Mhat^2 - 24/C_r = 1/M_L^2 (eq. 3.4).  p.11: "the need for a non-decoupling massless and ghost-like radion is always
    associated with the presence of a brane of negative tension."  Abstract: "The model violates positivity of energy due
    to a negative tension brane, which induces a negative kinetic term for the radion."
  Garriga & Tanaka, hep-th/9911055v4 -- the orbifold two-plane bulk (the negative plane at a fixed point, its ghost mode
    projected out, PRZ p.3): Brans-Dicke on each plane, omega(+-) = (3/2)(e^{+-2d/ell} - 1) (eq. 27); shadow matter
    through the first term of eq. (25), structure P2 - (2/3) P0, "25 % weaker" light bending (p.1, p.8).

  M1  the GT orbifold bulk: gamma < 1 on either plane, at every separation (exact forms)
  M2  GT's shadow matter: c0 = -2/3, gamma = 1/2 (a re-derivation of GT's published 25%)
  M3  the LR bulk, ours the Planck plane: gamma = (3 + X)/(3 - X), X = e^{-2 k_L r}(k_L - k_R)/k_R; gamma = 5/4 at X = 1/3,
      which needs the second plane's tension negative and its radion a ghost
  M4  the planes coinciding (M's item 127, r = 0): gamma = 5/4 at k_R = 3 k_L / 4; tensions +4/3 and -1/3 of the one-plane
      value, summing to it (loose.py L4's sum rule)
Stdlib + sympy.  python3 multiplane.py [--selftest]
"""
import sys

import sympy as sp

x = sp.Symbol("x", positive=True)                                  # d/ell (GT)
kL, kR, r, M = sp.symbols("k_L k_R r M", positive=True)
X = sp.Symbol("X")


def gamma_from_c0(c0):
    """Post-Newtonian gamma for exchange structure (P2 + c0 P0)/q^2: gamma = -c0/(2 + c0)."""
    return sp.simplify(-c0 / (2 + c0))


def gamma_bd(omega):
    return (1 + omega) / (2 + omega)


def m1():
    wp = sp.Rational(3, 2) * (sp.exp(2 * x) - 1)
    wm = sp.Rational(3, 2) * (sp.exp(-2 * x) - 1)
    gp, gm = sp.simplify(gamma_bd(wp)), sp.simplify(gamma_bd(wm))
    return {"gamma_plus": gp, "gamma_minus": gm,
            "one_minus_gp": sp.simplify(1 - gp), "one_minus_gm": sp.simplify(1 - gm),
            "gp_limits": (sp.limit(gp, x, 0, "+"), sp.limit(gp, x, sp.oo)),
            "gm_limits": (sp.limit(gm, x, 0, "+"), sp.limit(gm, x, sp.oo))}


def m2():
    return {"gamma": gamma_from_c0(sp.Rational(-2, 3))}


def lr():
    Mhat2 = (M**3 / kL) * (1 + sp.exp(-2 * kL * r) * (kL - kR) / kR)           # eq. 2.17
    ML2 = M**3 / kL
    Cr = (24 * M**3 / kL) * (sp.exp(2 * kL * r) * kR / (kR - kL) - 1)          # eq. 2.16
    tau1, tau2 = 24 * M**3 * kL, 24 * M**3 * (kR - kL)
    # eq. 3.3: (1/(8 Mhat^2))(P2 - (2/3) P0) - (1/(24 ML^2)) P0 = (1/(8 Mhat^2)) (P2 + c0 P0)
    c0 = sp.simplify(sp.Rational(-2, 3) - 8 * Mhat2 / (24 * ML2))
    return {"Mhat2": Mhat2, "ML2": ML2, "Cr": Cr, "tau1": tau1, "tau2": tau2, "c0": c0,
            "gamma": sp.simplify(gamma_from_c0(c0)),
            "identity_34": sp.simplify(1 / Mhat2 - 24 / Cr - 1 / ML2)}               # eq. 3.4, must vanish


def m3():
    d = lr()
    gX = sp.simplify((3 + X) / (3 - X))
    Xdef = sp.exp(-2 * kL * r) * (kL - kR) / kR
    sol = sp.solve(sp.Eq(gX, sp.Rational(5, 4)), X)
    return {"gamma_X": gX, "agrees": sp.simplify(d["gamma"] - gX.subs(X, Xdef)) == 0, "X_for_5_4": sol[0],
            "identity_34": d["identity_34"]}


def m4():
    """r = 0: X = (k_L - k_R)/k_R = 1/3."""
    d = lr()
    kr = sp.solve(sp.Eq((kL - kR) / kR, sp.Rational(1, 3)), kR)[0]
    lam_rs = 24 * M**3 * kr                                         # the one-plane (Z2) value at the outer curvature
    t1 = sp.simplify(d["tau1"].subs(kR, kr) / lam_rs)
    t2 = sp.simplify(d["tau2"].subs(kR, kr) / lam_rs)
    cr0 = sp.simplify(d["Cr"].subs({r: 0, kR: kr}))
    g0 = sp.simplify(d["gamma"].subs({r: 0, kR: kr}))
    return {"kR": kr, "tau1_over_rs": t1, "tau2_over_rs": t2, "Cr_at_r0": cr0, "gamma": g0}


def report():
    a, b, c, e = m1(), m2(), m3(), m4()
    print("multiplane.py -- what a bulk of more than one plane gives on our plane (item 138)\n")
    print("M1 Garriga-Tanaka's orbifold bulk: 1 - gamma(+) = %s; 1 - gamma(-) = %s -- both > 0: gamma < 1 always"
          % (a["one_minus_gp"], a["one_minus_gm"]))
    print("M2 GT's shadow matter (structure P2 - (2/3) P0): gamma = %s, light bending x 3/4" % b["gamma"])
    print("M3 Lykken-Randall, ours the Planck plane: gamma = %s, X = e^(-2 k_L r)(k_L - k_R)/k_R; eq. 3.4 residual %s"
          % (c["gamma_X"], c["identity_34"]))
    print("   gamma = 5/4 at X = %s: needs k_R < k_L, i.e. the second plane's tension 24 M^3 (k_R - k_L) < 0, and then"
          % c["X_for_5_4"])
    print("   the radion's kinetic coefficient C_r < 0: a ghost (PRZ p.11)")
    print("M4 the planes coinciding (r = 0): gamma = %s at k_R = %s; tensions %s and %s of the one-plane value; C_r = %s"
          % (e["gamma"], e["kR"], e["tau1_over_rs"], e["tau2_over_rs"], e["Cr_at_r0"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    a, b, c, e = m1(), m2(), m3(), m4()
    chk("gamma_from_c0: Einstein's c0 = -1 gives 1 and the massive graviton's -2/3 gives 1/2 (the formula's controls)",
        gamma_from_c0(sp.Integer(-1)) == 1 and gamma_from_c0(sp.Rational(-2, 3)) == sp.Rational(1, 2))
    chk("M1: exactly, 1 - gamma(+) = 2/(3 e^{2x} + 1) and 1 - gamma(-) = 2 e^{2x}/(e^{2x} + 3): gamma < 1 on both planes",
        sp.simplify(a["one_minus_gp"] - 2 / (3 * sp.exp(2 * x) + 1)) == 0 and
        sp.simplify(a["one_minus_gm"] - 2 * sp.exp(2 * x) / (sp.exp(2 * x) + 3)) == 0)
    chk("M1: gamma(+) runs (1/2, 1), gamma(-) runs (1/2, -1)", a["gp_limits"] == (sp.Rational(1, 2), 1) and
        a["gm_limits"] == (sp.Rational(1, 2), -1))
    chk("M2: shadow matter's structure P2 - (2/3) P0 gives gamma = 1/2 -- GT's 25% (re-derived from eq. 25's structure)",
        b["gamma"] == sp.Rational(1, 2))
    chk("M3: PRZ eq. (3.4) holds identically from eqs. (2.16), (2.17) -- the transcription checks itself",
        c["identity_34"] == 0)
    chk("M3: eq. (3.3) gives gamma = (3 + X)/(3 - X) with X = e^{-2 k_L r}(k_L - k_R)/k_R", c["agrees"])
    chk("M3: gamma = 5/4 exactly at X = 1/3", c["X_for_5_4"] == sp.Rational(1, 3))
    chk("M3: X > 0 needs k_R < k_L: the second plane's tension negative and C_r < 0 (ghost), e.g. k_L = 1, k_R = 1/2",
        float(lr()["tau2"].subs({M: 1, kL: 1, kR: sp.Rational(1, 2)})) < 0 and
        float(lr()["Cr"].subs({M: 1, kL: 1, kR: sp.Rational(1, 2), r: 1})) < 0)
    chk("M3 control: a positive-tension second plane (k_R > k_L) gives X < 0 and gamma < 1",
        float(lr()["gamma"].subs({M: 1, kL: 1, kR: 2, r: 1})) < 1)
    chk("M3 control: far separation (r -> oo) recovers one plane's gamma = 1",
        sp.limit(lr()["gamma"].subs({kL: 1, kR: sp.Rational(1, 2)}), r, sp.oo) == 1)
    chk("M4: coinciding planes give gamma = 5/4 at k_R = 3 k_L / 4, tensions +4/3 and -1/3 of the one-plane value",
        e["gamma"] == sp.Rational(5, 4) and sp.simplify(e["kR"] - sp.Rational(3, 4) * kL) == 0 and
        e["tau1_over_rs"] == sp.Rational(4, 3) and e["tau2_over_rs"] == sp.Rational(-1, 3))
    chk("M4: the two tensions sum to the one-plane value, as loose.py L4's sum rule requires",
        e["tau1_over_rs"] + e["tau2_over_rs"] == 1)
    chk("M4: the radion is a ghost there too (C_r < 0)", sp.simplify(e["Cr_at_r0"]).is_negative)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
