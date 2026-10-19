#!/usr/bin/env python3
"""wh5_dictionary.py -- item 447 (1), stage 1 of BOUNCE-RESEARCH section 13: what the planes see of the corridor M
names at 446 (2), "the wormhole in 5D, but when viewed in 4D it appears as a black hole/white hole respectively", the
black hole at position 1 and the white hole at position 2 (447 (2)).  Exact where marked.  Labels: READ (SOURCES),
computed (sympy exact; mpmath quadrature where marked), estimate (marked), deduced.  Worked in the conversation; not
verified; not seated.  2026-10-16.

  W0 (read) M's words: 446 (2), confirmed at 447 (2).
  W1 (READ) The outside art (SOURCES): MM's figure 6 (the near-horizon region of a near-extremal black hole is "a
     Rindler-like portion of global AdS2"); Spradlin and Strominger ("An AdS_2 black hole spacetime is an AdS_2
     spacetime together with a preferred choice of time"); the Reissner-Nordstrom inner horizon is a Cauchy horizon,
     unstable to perturbations from outside (Gursel, Novikov, Sandberg, Starobinsky; Hod).
  W2 (computed, exact) A near-extremal charged hole's throat is AdS2 with its two horizons at x = +-1.  With
     r_+- = r_e +- delta and r = r_e + delta x, f = (r - r_+)(r - r_-)/r^2 -> delta^2 (x^2 - 1)/r_e^2 (four dimensions;
     AdS2 radius r_e) and f = (r^2 - r_+^2)(r^2 - r_-^2)/r^4 -> 4 delta^2 (x^2 - 1)/r_e^2 (five; radius r_e/2):
     x > 1 is outside r_+, |x| < 1 between the horizons, x < -1 inside r_-.
  W3 (computed, exact) The passage in the throat.  In global AdS2, ds^2 = (-dtau^2 + dsigma^2)/sin^2 sigma, the black
     -hole coordinate is x = cos tau/sin sigma.  A light ray leaving position 1's boundary (sigma = pi) at any tau0 in
     (-pi/2, pi/2) -- position 1's exterior W_R of the bifurcation point P0 = (0, pi/2) -- crosses r_+ (x = 1) at
     tau = (pi/2 + tau0)/2 into the diamond between P0 and P1 = (pi, pi/2), crosses r_- (x = -1) at
     tau = (3 pi/2 + tau0)/2 into the left wedge W_L' of P1, and reaches position 2's boundary (sigma = 0) at
     tau0 + pi.  The diamond is P0's future interior and P1's past interior at once: seen from position 1 (W_R) it is
     a black hole, entered through r_+; seen from position 2 (W_L') it is a white hole, left through r_-.  So
     position 2's white-hole horizon is position 1's inner horizon.  Every ray spends global time pi/2 in the diamond
     and pi in all; with MM's outside time t = l tau (5.19) the crossing is pi l (5.20).
  W4 (computed, exact) The two mouths' own clocks.  Each mouth's thermal time is the boost angle about its own
     bifurcation point (P0 for position 1, P1 for position 2, both future-directed): the ray leaves position 1 at
     artanh(sin tau0) and arrives at position 2 at artanh(sin tau0), the same reading.  In the mouths' own clocks the
     passage takes no time; in the throat's shared global time position 2's patch sits pi (outside, pi l) ahead.
     Which clock each plane keeps is the convention M-CLOCK-OFFSET's hour fixes.
  W5 (computed, exact; quadrature where marked) The charged hole away from extremality, at the small end: a five-
     dimensional Reissner-Nordstrom hole on the plane, f = 1 - mu/r^2 + q^2/r^4 (the AdS term r^2/ell^2 at
     (r_h/ell)^2 = 6.4e-31, and the plane equatorial to O(r_h/ell), as the record's small end).  Its horizons are
     r_+-^2 = (mu +- sqrt(mu^2 - 4 q^2))/2, its surface gravities k_+- = (r_+^2 - r_-^2)/r_+-^3.  Inside r_- f falls
     monotonically from +infinity to 0 (f' < 0 there, exact), so every massive radial route turns at one r_min < r_-
     and passes out through the white hole into the next exterior, in a finite proper time (quadrature); every route
     with angular momentum turns too; radial light alone reaches r = 0, where the curvature diverges (exact).  The
     next exterior carries the same f, so clocks at equal radius tick alike there.
  W6 (computed; estimate for the plane's corrections) The large end: the plane's view of the charged hole is four-
     dimensional Reissner-Nordstrom to first order in (ell/r0)^2 (the record's reading for the uncharged hole, here
     an estimate for the charged), with the same chain.
  W7 (deduced) What stage 1 settles.
     - M-CORRIDOR-5D is realized exactly: a charged hole's chain, a black hole at position 1 and a white hole at
       position 2.  Near extremality the passage lies in the AdS2 throat, where it is Maldacena and Milekhin's
       crossing read in each mouth's own time.  Section 13's two candidates are one object: (b) is (a)'s near-extremal
       throat, its cold state read in global time and its black-hole/white-hole state read in the mouths' times.
     - Classically, the chain is complete for every massive route and every route with angular momentum; radial
       light reaches the timelike centre, a set of measure zero.  In Maldacena and Milekhin's wormhole the region
       beyond r_- is position 2's exterior, so that centre is not there.
     - The obstruction is the inner horizon, which is position 2's white-hole horizon: a Cauchy horizon of the
       charged hole, unstable to perturbations from position 1 (READ).  Stage 2 computes it.

python3 wh5_dictionary.py [--selftest | --mutants]
"""
import math
import os
import re
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ("the wormhole in 5D, but when viewed in 4D it appears as a black hole/white hole respectively",)
SOURCES = {
    "MM-fig6": ("1807.04726", "The two triangles correspond to the two exteriors of the maximally extended black hole.",
                "These red regions correspond to a Rindler-like portion of global AdS2 space."),
    "SS": ("hep-th/9904143", "An AdS_2 black hole spacetime is an AdS_2 spacetime together with a preferred choice of "
                             "time."),
    "GNSS": ("PRD 19, 2821", "Thus the solution is unstable to physically reasonable perturbations which arise outside "
                             "the black hole"),
    "HOD": ("1801.07261", "the instability of the dynamically formed inner Cauchy horizons"),
}
C = 299792458.0
RH = 1.12008e-20                                                        # m, the small end's face (b4d_small RH)
ELL = 13.9642e-6                                                        # m, bounce_scope.ELL
R_EARTH_CAP = 8.870e-3                                                  # m


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def w1():
    return all(len(v) >= 2 and all(len(q) > 20 for q in v[1:]) for v in SOURCES.values())


def w2():
    r, re_, d, x = sp.symbols("r r_e delta x", positive=True)
    rp, rm = re_ + d, re_ - d
    f4 = (r - rp) * (r - rm) / r ** 2
    f5 = (r ** 2 - rp ** 2) * (r ** 2 - rm ** 2) / r ** 4
    lead4 = sp.limit(f4.subs(r, re_ + d * x) / d ** 2, d, 0)
    lead5 = sp.limit(f5.subs(r, re_ + d * x) / d ** 2, d, 0)
    return (sp.simplify(lead4 - (x ** 2 - 1) / re_ ** 2) == 0, sp.simplify(lead5 - 4 * (x ** 2 - 1) / re_ ** 2) == 0)


def _pt(tau, sig):
    """embedding: x = cos tau/sin sigma (the black-hole coordinate about P0), T = sin tau/sin sigma, S = -cot sigma"""
    return math.cos(tau) / math.sin(sig), math.sin(tau) / math.sin(sig), -math.cos(sig) / math.sin(sig)


def region(tau, sig):
    x, T, S = _pt(tau, sig)
    if x > 1 and S > 0:
        return "W_R"
    if abs(x) < 1 and T > 0:
        return "diamond"
    if x < -1 and S < 0:
        return "W_L'"
    return "other"


def ray(tau0, n=4000):
    """the light ray from sigma = pi at tau0 toward sigma = 0: sigma = pi - (tau - tau0); the regions in order"""
    shift = math.pi / 2 if "no_shift" in MUT else math.pi
    seq = []
    for i in range(1, n):
        tau = tau0 + shift * i / n
        sig = math.pi - (tau - tau0)
        if abs(abs(_pt(tau, sig)[0]) - 1) < 1e-9:                      # a sample on a horizon belongs to neither side
            continue
        g = region(tau, sig)
        if not seq or seq[-1] != g:
            seq.append(g)
    return seq


def w3():
    t0, tau = sp.symbols("tau0 tau", real=True)
    sig = sp.pi - (tau - t0)
    xr = sp.cos(tau) / sp.sin(sig)
    cross_p = (sp.pi / 2 + t0) / 2
    cross_m = (3 * sp.pi / 2 + t0) / 2
    ok_p = sp.simplify(xr.subs(tau, cross_p) - 1) == 0
    ok_m = sp.simplify(xr.subs(tau, cross_m) + 1) == 0
    inside = sp.simplify(cross_m - cross_p) == sp.pi / 2
    arrive = sp.simplify(sig.subs(tau, t0 + sp.pi)) == 0
    seqs = {round(v, 2): ray(v) for v in (-1.2, -0.6, 0.0, 0.6, 1.2)}
    order = all(s == ["W_R", "diamond", "W_L'"] for s in seqs.values())
    return ok_p and ok_m and inside and arrive, order, seqs


def w4(tau0):
    """thermal times: position 1 about P0 at its boundary; position 2 about P1 (tau -> tau - pi), S' = +cot sigma"""
    eps = 1e-9
    _, T, S = _pt(tau0, math.pi - eps)
    t1 = math.atanh(T / S)
    tau = tau0 + math.pi - eps
    sig = eps
    T2 = math.sin(tau - math.pi) / math.sin(sig)
    S2 = math.cos(sig) / math.sin(sig)
    if "orientation" in MUT:
        T2 = -T2
    t2 = math.atanh(T2 / S2)
    future = (math.cos(tau - math.pi) / math.sin(sig)) > 0                # dT2/dtau > 0: future-directed
    return t1, t2, future


def f5(r, mu, q2):
    return 1 - mu / r ** 2 + q2 / r ** 4


def hole5(x):
    """r_+ = 1, r_- = x: mu = 1 + x^2, q^2 = x^2"""
    mu, q2 = 1 + x ** 2, x ** 2
    if "sign_q" in MUT:
        q2 = -q2
    disc = mu ** 2 - 4 * q2
    rp = math.sqrt((mu + math.sqrt(disc)) / 2)
    rm2 = (mu - math.sqrt(disc)) / 2
    rm = math.sqrt(rm2) if rm2 > 0 else 0.0
    kp = (rp ** 2 - rm ** 2) / rp ** 3
    km = (rp ** 2 - rm ** 2) / rm ** 3 if rm > 0 else float("inf")
    return mu, q2, rp, rm, kp, km


def passage5(x, rs=2.0):
    """a massive radial route released from rest at rs: E^2 = f(rs); r_min where f = E^2 inside r_-; proper time
    from rs in, through the white hole, back out to rs (mpmath tanh-sinh quadrature)"""
    mu, q2, rp, rm, kp, km = hole5(x)
    if rm == 0:
        return None
    E2 = f5(rs, mu, q2)
    rmin = mp.findroot(lambda r: f5(r, mu, q2) - E2, (1e-6, rm * (1 - 1e-12)), solver="bisect")
    tau = 2 * mp.quad(lambda r: 1 / mp.sqrt(abs(E2 - f5(r, mu, q2))), [rmin, rm, rp, rs])
    return float(rmin), float(tau), rp, rm, kp, km


def w5():
    r, mu, q = sp.symbols("r mu q", positive=True)
    f = 1 - mu / r ** 2 + q ** 2 / r ** 4
    rp2, rm2 = sp.symbols("r_p2 r_m2", positive=True)
    fact = sp.simplify(f.subs({mu: rp2 + rm2, q: sp.sqrt(rp2 * rm2)}) - (r ** 2 - rp2) * (r ** 2 - rm2) / r ** 4) == 0
    fp = sp.diff(f.subs({mu: rp2 + rm2, q: sp.sqrt(rp2 * rm2)}), r)
    rstar2 = 2 * rp2 * rm2 / (rp2 + rm2)                                # f' = 0 at r^2 = 2 q^2/mu
    zero_at = sp.simplify(fp.subs(r, sp.sqrt(rstar2))) == 0
    between = sp.simplify(rstar2 - rm2 - rm2 * (rp2 - rm2) / (rp2 + rm2)) == 0   # r*^2 > r_-^2 since rp2 > rm2
    K = sp.diff(f, r, 2) ** 2 + 6 * sp.diff(f, r) ** 2 / r ** 2 + 12 * (1 - f) ** 2 / r ** 4
    diverges = sp.limit(K * r ** 12, r, 0) > 0
    Lsym = sp.Symbol("L", positive=True)
    barrier = sp.limit(f * Lsym ** 2 / r ** 2, r, 0) == sp.oo            # any angular momentum turns before r = 0
    diverges = diverges and barrier
    rows = {x: passage5(x) for x in (0.1, 0.5, 0.9, 0.99)}
    return fact, zero_at and between, diverges, rows


def w6(x, rs=2.0):
    """four-dimensional Reissner-Nordstrom with r_+ = 1, r_- = x: f = (r - 1)(r - x)/r^2"""
    f = lambda r: (r - 1) * (r - x) / r ** 2                            # noqa: E731
    E2 = f(rs)
    rmin = mp.findroot(lambda r: f(r) - E2, (1e-9, x * (1 - 1e-12)), solver="bisect")
    tau = 2 * mp.quad(lambda r: 1 / mp.sqrt(abs(E2 - f(r))), [rmin, x, 1, rs])
    return float(rmin), float(tau)


def report():
    print("W0 M's words:", words())
    print("W1 outside art quoted:", w1())
    print("W2 the throat is AdS2 with r_+- at x = +-1 (4D, 5D):", w2())
    exact, order, seqs = w3()
    print("W3 crossings exact (r_+, r_-, pi/2 inside, arrival at tau0 + pi): %s; regions in order %s" % (exact, order))
    for t0 in (-1.2, 0.0, 1.2):
        t1, t2, fut = w4(t0)
        print("W4 tau0 = %+.1f: position 1's thermal time %.6f, position 2's %.6f, future-directed %s" % (t0, t1, t2,
                                                                                                         fut))
    fact, mono, div, rows = w5()
    print("W5 f factorizes %s; f monotone inside r_- %s; curvature diverges at r = 0 and an angular-momentum "
          "barrier turns every non-radial route there %s" % (fact, mono, div))
    for x, row in rows.items():
        rmin, tau, rp, rm, kp, km = row
        print("   r_-/r_+ = %.2f: k_+ r_+ = %.4f, k_- r_+ = %.4f, r_min = %.4f r_+, passage %.3f r_+/c = %.3e s at r_h;"
              " energy %.4f x the uncharged" % (x, kp, km, rmin, tau, tau * RH / C, 1 + x ** 2))
    for x in (0.5, 0.9):
        rmin, tau = w6(x)
        print("W6 4D, r_-/r_+ = %.1f: r_min = %.4f r_+, passage %.3f r_+/c = %.3e s at the Earth cap" % (
            x, rmin, tau, tau * R_EARTH_CAP / C))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("W0 words: %s" % r)
    r = w1(); ok.append(r); say("W1 outside art quoted: %s" % r)
    a, b = w2(); r = a and b; ok.append(r); say("W2 the throat AdS2, horizons at x = +-1: %s" % r)
    exact, order, _ = w3(); r = exact and order; ok.append(r)
    say("W3 the ray: W_R, black hole (r_+), white hole (r_-), W_L'; pi/2 inside, pi in all: %s" % r)
    r = all(abs(w4(t)[0] - w4(t)[1]) < 1e-6 and w4(t)[2] for t in (-1.2, -0.6, 0.0, 0.6, 1.2)); ok.append(r)
    say("W4 equal thermal readings at departure and arrival, both future-directed: %s" % r)
    fact, mono, div, rows = w5()
    good = all(row is not None and 0 < row[0] < row[3] and row[1] > 0 for row in rows.values())
    r9 = rows[0.5]
    r = fact and mono and div and good and abs(r9[0] - 1 / math.sqrt(4.75)) < 1e-9 and abs(r9[4] - 0.75) < 1e-9
    ok.append(r); say("W5 the small end's charged hole: horizons, turning inside r_-, the centre singular: %s" % r)
    rmin, tau = w6(0.5); r = 0 < rmin < 0.5 and tau > 0; ok.append(r)
    say("W6 the large end's four-dimensional chain: %s" % r)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    names = ("no_shift", "orientation", "sign_q")
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-11s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
