#!/usr/bin/env python3
"""b4d_stage4.py -- Warp Theorem lemma B4d, stage 4: the null shell that opens the corridor, on the plane.  Computed,
READ and deduced; not verified; not seated.

M's words (verbatim in the rulings file): item 162 (the size set at once upon opening); item 157 (our universe before
the opening); items 117/120 (null energy: "the NEC only ever appears to break, but never does"); clause (B) (the
plane carries no matter).

READ
  Poisson, gr-qc/0207101: p.4, eqs. (2.12)-(2.15), a null shell's surface stress S = mu k k + j (k e + e k) + p sigma;
    p.9, eqs. (5.7), (5.12)-(5.14), for ds^2 = -e^psi dw (f e^psi dw + 2 zeta dr) + r^2 dOmega^2, f = 1 - 2m/r:
    mu = (-zeta) [m]/(4 pi r^2), p = (-zeta) [d psi/dr]/(8 pi), zeta = -1 contracting; p.8, eq. (5.6), the imploding
    shell from Minkowski into Schwarzschild has mu = M/(4 pi r^2) and p = 0.

  D1 THE SHELL FROM OUR UNIVERSE INTO EQ. (17), ON THE PLANE (computed).  Inside (before the opening) Minkowski: m = 0,
     psi = 0.  Outside, eq. (17) at r0 = 2m: -F dt^2 + dr^2/H + r^2 dOmega^2 with F = 1 - 2x, H = (1 - 2x)^2/(1 - 3x/2),
     x = m/r -- in Poisson's form f = H, e^psi = sqrt(F/H).  So
        mu = m_+(r)/(4 pi r^2),  m_+ = r (1 - H)/2 = m (5/2 - 4x)/(2 (1 - 3x/2)):  m at r = 2m, 5m/4 far out (E4's total);
        p  = (1/8 pi) d psi_+/dr = -m/(16 pi (r - 2m)(2r - 3m))   < 0  for every r > 2m, diverging at the throat
     (in Poisson's parameterization lambda = -r on both sides; e^psi = sqrt(F/H) diverges at eq. (17)'s extremal
     horizon, where F has a single zero and H a double one -- whether p's sign survives a reparameterization of the
     generators is for the verifier and stage 5).
     The shell carries positive energy (mu > 0) and a tension (p < 0).  Control: Schwarzschild outside gives Poisson's
     mu = M/(4 pi r^2), p = 0 exactly.
  D2 THE TENSION BREAKS THE 4D NULL CONDITION ON THE SHELL (deduced).  For a future null n = a k + b N + c^A e_A
     (|c|^2 = 2ab), S(n,n) = mu b^2 + 2 p a b: with p < 0 it is negative for a large enough.  So read as matter on the
     plane, this shell breaks the null energy condition -- as eq. (17) itself does on the plane (opening.py O3).
  D3 WHAT THAT MEANS UNDER YOUR RULINGS (deduced).  Clause (B): the plane carries no matter, so this 4D shell is not
     matter -- it is the bulk's Weyl field jumping across the null cone, read on the plane (Maartens-Koyama's -E_mu nu,
     as E4 reads eq. (17)'s deficit).  That is the kind of violation your 117/120 call an appearance.  The real test is
     five-dimensional: the null shell in the bulk, across the cone's boundary between eq. (17)'s static bulk and the
     prior bulk, must carry non-negative energy in the 5D sense -- stage 5.

Imports nothing; stdlib + sympy.  python3 b4d_stage4.py [--selftest]
"""
import sys

import sympy as sp

r, m, M = sp.symbols("r m M", positive=True)


def shell(F, H):
    """Poisson's mu and p for an ingoing (zeta = -1) shell from Minkowski (m = 0, psi = 0) into -F dt^2 + dr^2/H."""
    m_plus = sp.simplify(r * (1 - H) / 2)
    psi = sp.log(F / H) / 2
    mu = sp.simplify(m_plus / (4 * sp.pi * r**2))
    p = sp.simplify(sp.diff(psi, r) / (8 * sp.pi))
    return m_plus, mu, p


def eq17():
    x = m / r
    F = 1 - 2 * x
    H = (1 - 2 * x) ** 2 / (1 - sp.Rational(3, 2) * x)
    return F, H


def compute():
    F, H = eq17()
    mp_, mu, p = shell(F, H)
    sF = 1 - 2 * M / r
    cm, cmu, cp = shell(sF, sF)
    x = sp.Symbol("x", positive=True)
    p_closed = -m / (16 * sp.pi * (r - 2 * m) * (2 * r - 3 * m))
    return {"m_plus": mp_, "mu": mu, "p": p, "p_closed": p_closed, "ctl": (cm, cmu, cp),
            "m_throat": sp.simplify(mp_.subs(r, 2 * m)), "m_far": sp.limit(mp_, r, sp.oo),
            "p_samples": [float(p.subs({m: 1, r: rv})) for rv in (2.001, 2.5, 3, 5, 10, 100)],
            "mu_samples": [float(mu.subs({m: 1, r: rv})) for rv in (2.001, 2.5, 3, 5, 10, 100)]}


def report(d):
    print("b4d_stage4.py -- B4d stage 4: the opening's null shell on the plane\n")
    print("D1 m_+ = %s (m at the throat: %s; far out: %s)" % (d["m_plus"], d["m_throat"], d["m_far"]))
    print("   mu = %s; p = %s" % (d["mu"], d["p"]))
    print("   mu at r = 2.001..100: %s" % ", ".join("%.3g" % v for v in d["mu_samples"]))
    print("   p  at r = 2.001..100: %s" % ", ".join("%.3g" % v for v in d["p_samples"]))
    print("   control (Schwarzschild): m_+ = %s, mu = %s, p = %s" % d["ctl"])


def selftest():
    ok = n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    d = compute()
    cm, cmu, cp = d["ctl"]
    chk("D1 control: the shell from Minkowski into Schwarzschild has Poisson's mu = M/(4 pi r^2) and p = 0 (eq. (5.6))",
        sp.simplify(cmu - M / (4 * sp.pi * r**2)) == 0 and sp.simplify(cp) == 0)
    chk("D1: into eq. (17) the shell's mass function is m at the throat and 5m/4 far out (E4's total); mu > 0 for every "
        "r > 2m", sp.simplify(d["m_throat"] - m) == 0 and sp.simplify(d["m_far"] - sp.Rational(5, 4) * m) == 0
        and all(v > 0 for v in d["mu_samples"]))
    chk("D1: its pressure is a tension, p = -m/(16 pi (r - 2m)(2r - 3m)) < 0 for every r > 2m",
        sp.simplify(d["p"] - d["p_closed"]) == 0 and all(v < 0 for v in d["p_samples"]))
    chk("D2 (deduced, checked): with p < 0, S(n,n) = mu b^2 + 2 p a b < 0 for a null n with a large enough",
        all(mu_ * 1.0**2 + 2 * p_ * 1e6 * 1.0 < 0 for mu_, p_ in zip(d["mu_samples"], d["p_samples"])))
    print("selftest: %d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report(compute())
