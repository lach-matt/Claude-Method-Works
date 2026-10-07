#!/usr/bin/env python3
"""kscale.py -- hypothesize the bulk scale k from what is established, and derive what would be seen
(M-RULINGS item 136: question 8, "leave it to measurement. But we can accurately hypothesize it first. Measurement
would confirm"; wall I, "derive something we can observe/witness"; item 137: D, then I, then C).

The plane sits in a five-dimensional bulk of curvature k; its scale is ell = 1/k.  On the plane, gravity between two
masses at separation r is Newton's with a correction (Maartens-Koyama, Living Rev. Rel. 13 (2010) 5,
arXiv:1004.3962v2 p.10-11 eq. (41), READ):  V(r) = G M / r (1 + 2 ell^2 / (3 r^2)).  The plane's tension is
lambda = 3 M_p^2 / (4 pi ell^2) (eq. (25), READ; M_p the unreduced Planck mass).  These are Randall-Sundrum II, one
plane in an unbounded bulk -- M's item 136 answer 9 (no ends).

Candidates for ell, each from an established scale, each with what it predicts:
  K1  the dark-energy length, ell = (hbar c / rho_d)^(1/4) ~ 85 um (Lee et al. 2020 p.1, READ)
  K2  the largest ell the short-range data leave (a rough bound from Lee et al.'s percent-level G at ~50 um, READ;
      the board's point-mass arithmetic, NOT a fit to their torques)
  K3  the Planck length (k at the Planck scale, as Randall-Sundrum I's hierarchy uses), ell = sqrt(hbar G / c^3)

And eq. (17) read in Eddington-Robertson form (P) -- a re-derivation of Casadio-Fabbri-Mazzacurati, gr-qc/0111072
eq. (8) ("gamma = beta"; their zero-temperature member is beta = 5/4): the corridor's far field in Eddington-Robertson form,
g_tt = 1 - 2M/r + 2(beta - gamma) M^2/r^2, g_rr = 1 + 2 gamma M/r (areal coordinates).  For eq. (17),
gamma(r0) = 1/4 + r0/(2m) and beta = gamma; at the corridor's member r0 = 2m, gamma = beta = 5/4, where a plain mass
(general relativity's Schwarzschild, the r0 = 3m/2 member) has 1.  Light bends by (1 + gamma)/2 = 9/8 of a plain
mass with the same pull; the Shapiro delay is 9/8 too; an orbit's perihelion turns by (2 + 2 gamma - beta)/3 = 13/12.
Stdlib + sympy (exact SI where the constants are exact).  python3 kscale.py [--selftest]
"""
import sys

import sympy as sp

H = sp.Rational(662607015, 10**42)
HBAR = H / (2 * sp.pi)
C = sp.Integer(299792458)
EV = sp.Rational(1602176634, 10**28)
G = sp.Rational(66743, 10**15)

RHO_D = sp.Rational(38, 10) * 1000 * EV / sp.Rational(1, 10**6)     # 3.8 keV/cm^3 (Lee et al. p.1), J/m^3
R_MIN = sp.Rational(52, 10**6)                                     # their smallest separation, m (p.1)
G_PRECISION = sp.Rational(1, 100)                                  # "percent-level measurements of G_N at
                                                                   # separations down to about 50 um" (p.2)


def deviation(ell, r):
    """Fractional change of Newton's potential on the plane, eq. (41): 2 ell^2 / (3 r^2).  Valid for r >> ell."""
    return 2 * ell**2 / (3 * r**2)


def force_deviation(ell, r):
    """Fractional change of the force, -d/dr of eq. (41)'s potential: 2 ell^2 / r^2 (three times the potential's).
    A torsion balance measures force.  Valid for r >> ell; for r << ell gravity turns 5D (eq. 40)."""
    return 2 * ell**2 / r**2


def tension(ell):
    """lambda = 3 M_p^2 / (4 pi ell^2) (eq. 25, natural units) as an energy per unit 3-volume: with M_p^2 = hbar c / G
    and dividing by (hbar c)^3, lambda_SI = 3 c^4 / (4 pi G ell^2), J/m^3."""
    return 3 * C**4 / (4 * sp.pi * G * ell**2)


def candidates():
    k1 = (HBAR * C / RHO_D) ** sp.Rational(1, 4)
    k2 = R_MIN * sp.sqrt(G_PRECISION / 2)                             # force_deviation(ell, 52 um) = 1%
    k3 = sp.sqrt(HBAR * G / C**3)
    return {"K1": k1, "K2": k2, "K3": k3}


def fingerprint():
    """Eddington-Robertson parameters of eq. (17) at large r, and the three classic tests' factors."""
    r, m, u, r0 = sp.symbols("r m u r0", positive=True)
    gtt = 1 - 2 * m / r
    grr = (1 - 3 * m / (2 * r)) / ((1 - 2 * m / r) * (1 - r0 / r))
    M = -sp.series(gtt.subs(r, 1 / u), u, 0, 2).removeO().coeff(u, 1) / 2       # g_tt = 1 - 2M/r
    gamma = sp.simplify(sp.series(grr.subs(r, 1 / u), u, 0, 2).removeO().coeff(u, 1) / (2 * M))
    c2 = sp.series(gtt.subs(r, 1 / u), u, 0, 3).removeO().coeff(u, 2)           # 2 (beta - gamma) M^2
    beta = sp.simplify(gamma + c2 / (2 * M**2))
    out = {"M": M, "gamma": gamma, "beta": beta}
    for name, val in (("floor", 2 * m), ("schw", sp.Rational(3, 2) * m)):
        g_, b_ = gamma.subs(r0, val), beta.subs(r0, val)
        out[name] = {"gamma": sp.simplify(g_), "beta": sp.simplify(b_), "deflection": sp.simplify((1 + g_) / 2),
                     "perihelion": sp.simplify((2 + 2 * g_ - b_) / 3)}
    return out


def compute():
    cs = candidates()
    out = {}
    for name, ell in cs.items():
        out[name] = {"ell_m": ell, "k_per_m": 1 / ell, "dev_at_52um": force_deviation(ell, R_MIN),
                     "dev_at_10um": force_deviation(ell, sp.Rational(10, 10**6)),
                     "r_for_1pct": ell * sp.sqrt(2 / G_PRECISION), "tension_J_m3": tension(ell),
                     "valid_at_52um": bool(R_MIN > 3 * ell)}
    out["P"] = fingerprint()
    return out


def report(d):
    print("kscale.py -- the bulk scale k, hypothesized from established scales, and what each predicts\n")
    print("Newton on the plane: V = G M / r (1 + 2 ell^2 / 3 r^2)  (Maartens-Koyama eq. 41, READ)")
    for name, label in (("K1", "the dark-energy length"), ("K2", "the largest ell the 52 um data leave (rough)"),
                        ("K3", "the Planck length")):
        v = d[name]
        print("\n%s %s" % (name, label))
        print("  ell = %s m   k = %s 1/m" % (sp.N(v["ell_m"], 6), sp.N(v["k_per_m"], 6)))
        print("  the force changed by %s at 52 um%s, %s at 10 um; a 1%% force change sets in at r = %s m"
              % (sp.N(v["dev_at_52um"], 4), "" if v["valid_at_52um"] else " (outside eq. 41's r >> ell)",
                 sp.N(v["dev_at_10um"], 4), sp.N(v["r_for_1pct"], 4)))
        print("  the plane's tension 3 c^4/(4 pi G ell^2) = %s J/m^3" % sp.N(v["tension_J_m3"], 4))
    p = d["P"]
    print("\nP eq. (17) in Eddington-Robertson form (CFM eq. 8): gamma(r0) = %s, beta = gamma" % p["gamma"])
    for name, label in (("floor", "the corridor, r0 = 2m"), ("schw", "control: Schwarzschild, r0 = 3m/2")):
        q = p[name]
        print("  %-36s gamma = %s, beta = %s; light bending and Shapiro delay x %s; perihelion turn x %s"
              % (label, q["gamma"], q["beta"], q["deflection"], q["perihelion"]))


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    chk("K1 reproduces Lee et al.'s dark-energy length, about 85 um", abs(float(d["K1"]["ell_m"]) - 85e-6) < 1e-6)
    chk("K1's 1% force change sets in at about 1.2 mm, inside Lee et al.'s 52 um - 3.0 mm range, where eq. 41 holds "
        "(r >> ell) and their fit is Newtonian", 1.0e-3 < float(d["K1"]["r_for_1pct"]) < 3.0e-3 and
        float(d["K1"]["r_for_1pct"]) > 10 * float(d["K1"]["ell_m"]))
    chk("K2 is the ell whose force change at 52 um is exactly 1% (by construction; a rough bound, not a fit)",
        sp.simplify(d["K2"]["dev_at_52um"] - G_PRECISION) == 0)
    chk("the force's change is three times the potential's (eq. 41 differentiated)", sp.simplify(
        force_deviation(sp.Symbol("l"), sp.Symbol("r")) / deviation(sp.Symbol("l"), sp.Symbol("r")) - 3) == 0)
    chk("K3 is the Planck length, 1.616e-35 m", abs(float(d["K3"]["ell_m"]) / 1.616255e-35 - 1) < 1e-5)
    chk("K3 predicts no change measurable at any tabletop separation (below 1e-50 at 10 um)",
        float(d["K3"]["dev_at_10um"]) < 1e-50)
    chk("the three candidates are ordered K3 < K2 < K1", float(d["K3"]["ell_m"]) < float(d["K2"]["ell_m"]) <
        float(d["K1"]["ell_m"]))
    p = d["P"]
    chk("P: at r0 = 2m, gamma = beta = 5/4; light bends 9/8 and the perihelion turns 13/12 of a plain mass's",
        p["floor"]["gamma"] == sp.Rational(5, 4) and p["floor"]["beta"] == sp.Rational(5, 4) and
        p["floor"]["deflection"] == sp.Rational(9, 8) and p["floor"]["perihelion"] == sp.Rational(13, 12))
    chk("P control: the Schwarzschild member (r0 = 3m/2) gives general relativity's gamma = beta = 1",
        p["schw"]["gamma"] == 1 and p["schw"]["beta"] == 1 and p["schw"]["deflection"] == 1 and
        p["schw"]["perihelion"] == 1)
    rr0, mm = sp.symbols("r0 m", positive=True)
    chk("P agrees with Casadio-Fabbri-Mazzacurati eq. (8): r0 = M(4 beta - 1)/2, i.e. beta = (M + 2 r0)/(4M)",
        sp.simplify(p["gamma"] - (mm + 2 * rr0) / (4 * mm)) == 0)
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
