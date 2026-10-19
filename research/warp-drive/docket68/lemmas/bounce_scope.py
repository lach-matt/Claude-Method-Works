#!/usr/bin/env python3
"""bounce_scope.py -- item 443 (2): the passage through the core, scoped for deeper research.  M: "they are provable.
It's going to take more work and deeper research".  This instrument holds the estimates the research note
(BOUNCE-RESEARCH.md) rests on; it proves nothing about the bounce itself, and runs no evolution (414: the computation
is discussed first).  Labels: computed (exact where marked), READ (the literature, quoted in BOUNCE-RESEARCH.md),
estimate, deduced, standard.  Worked in the conversation; not verified; not seated.

  B0 (read) M's words: 443 (2).
  B1 (deduced; READ) What any proof must supply.  Penrose's theorem holds in every dimension (prior_art HR, READ
     there); with trapped surfaces and the null condition kept pointwise -- which every smooth plane of ordinary
     matter does (b5b_wall W2-W3) -- the passage ends.  So the bounce needs negative null energy, and established
     physics supplies it only through quantum fields: the renormalized stress tensor (prior_art FR_NULL: the local null
     energy unbounded below; QNEC: the averaged condition kept).
  B2 (computed on READ equations; standard constants) The plane multiplies the semiclassical effect.  Barcelo,
     Boyanov, Carballo-Rubio and Garay (2011.07331, eq. 66, READ): the inner horizon's semiclassical mass grows as
     (l_P^2 lambda/(192 pi)) e^{lambda (v - v_f)} and turns the collapse when it reaches lambda r_i^2.  On the plane
     the classical bulk is dual to a four-dimensional field theory of central charge c = pi ell^2/(8 l_P^2) (Emparan,
     Fabbri, Kaloper hep-th/0206155; Tanaka gr-qc/0203082, READ: a conjecture with evidence), so l_P^2 becomes
     pi ell^2/8: c = 2.93e59 at ell = 13.964 um, and the e-folds needed fall from 145-157 to 7.8-20.2 across the large
     end (r0 = 1.25 ell to the Earth cap).
  B3 (computed, exact) The README cannot arrive as a sharp step.  Each bit's energy is ((D-2)/(D-3)) k T_H ln 2
     (encode_read E2); a quantum of that energy has wavelength 4 pi^2 r0/ln 2 = 56.96 r0 at the large end
     (T_H = hbar c/(4 pi k r0)) and 8 pi^2 r_h/(3 ln 2) = 37.97 r_h at the small (T_H = hbar c/(2 pi k r_h)): longer
     than the face by a factor of 38 to 57.  A delivery of N such quanta is spread over tens of face clocks, so the
     inner trapping horizon lingers -- the condition the semiclassical mechanism needs (2011.07331: it is avoided only
     if "the classical trajectory of the inner horizon goes to zero quickly").
  [Item 484: B2's e-folds and B4 calculate with the semiclassical inner horizon; struck from the checks, M-NO-CAUCHY.]
  B4 (estimate) The room it gives.  If the inner horizon lingers one wavelength at a rate lambda ~ 1/r0, it has
     about 57 e-folds at the large end: more than the 7.8-20.2 the plane requires, fewer than the 145-157 a single
     field would.  The estimate is the research question, not its answer; C1-C3 of BOUNCE-RESEARCH.md compute it.

python3 bounce_scope.py [--selftest | --mutants]
"""
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ("they are provable. It's going to take more work and deeper research",)
LP = 1.616255e-35                                  # m, standard (CODATA)
ELL = 13.9642e-6                                   # m, b6p_scale's ceiling
R_EARTH_CAP = 8.870e-3                             # m, the large end's top (372)


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def central_charge(ell=ELL):
    return math.pi * ell ** 2 / (8 * LP ** 2) * (8.0 if "no_pi_8" in MUT else 1.0)


def efolds(r, c=1.0):
    """B2: lambda (v - v_f) at which alpha reaches lambda r^2, from eq. 66 with l_P^2 -> c l_P^2"""
    return math.log(192 * math.pi * r ** 2 / (c * LP ** 2))


def wavelengths():
    """B3: the bit's quantum's wavelength over the face's radius, exactly, at D = 4 and 5"""
    D, ln2 = sp.symbols("D"), sp.log(2)
    out = {}
    for d, T_coeff in ((4, sp.Rational(1, 4)), (5, sp.Rational(1, 2))):   # k T_H = hbar c T_coeff / (pi r)
        eps = sp.Rational(d - 2, d - 3) * ln2 * T_coeff / sp.pi           # bit energy, units hbar c / r
        if "planck_bit" in MUT:
            eps = sp.Integer(1)
        out[d] = sp.simplify(2 * sp.pi / eps)                             # lambda = 2 pi hbar c / eps, units r
    return out


def report():
    print("B0 M's words:", words())
    c = central_charge()
    print("B2 central charge c = %.3e" % c)
    for name, r in (("r0 = 1.25 ell", 1.25 * ELL), ("r0 = 10 ell", 10 * ELL), ("Earth cap", R_EARTH_CAP)):
        print("   %-14s e-folds needed: the plane %.1f, one field %.1f" % (name, efolds(r, c), efolds(r)))
    w = wavelengths()
    print("B3 the bit's wavelength: %s r0 = %.2f r0 (4D), %s r_h = %.2f r_h (5D)" % (w[4], float(w[4]), w[5],
                                                                                 float(w[5])))
    print("B4 about %.0f e-folds if the inner horizon lingers one wavelength at lambda ~ 1/r0" % float(w[4]))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("B0 words: %s" % r)
    c = central_charge()
    r = abs(c / 2.931e59 - 1) < 1e-3; ok.append(r); say("B2 c = 2.931e59: %s" % r)
    # [item 484, M-NO-CAUCHY: B2's e-folds and B4 grow the semiclassical inner horizon's mass; struck from the checks]
    w = wavelengths()
    r = sp.simplify(w[4] - 4 * sp.pi ** 2 / sp.log(2)) == 0 and sp.simplify(w[5] - 8 * sp.pi ** 2 / (3 * sp.log(2))) == 0
    ok.append(r); say("B3 wavelengths 4 pi^2/ln2 r0 and 8 pi^2/(3 ln2) r_h exactly: %s" % r)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    for m in ("no_pi_8", "planck_bit"):
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-11s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/2 caught" % caught)
    return caught == 2


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
