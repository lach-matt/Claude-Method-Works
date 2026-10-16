#!/usr/bin/env python3
"""stage2_inner.py -- item 448, stage 2 of BOUNCE-RESEARCH section 13: the inner horizon, which stage 1 found is
position 2's white-hole horizon and the corridor's obstruction -- classically in five dimensions and on the plane, and
semiclassically as the plane sees it.  M: "yes, continue to stage 2".  Labels: READ (SOURCES), computed (sympy exact;
numbers at standard constants), estimate (marked: first-order extrapolations), deduced.  Worked in the conversation;
not verified; not seated.  2026-10-16.

  J0 (read) M's words: 448.
  J1 (READ) The outside art (SOURCES): Barcelo, Boyanov, Carballo-Rubio and Garay 2011.07331 (READ in full: eqs.
     (41)-(42) for a static inner horizon, (69) for its evaporation time, section 2.2's conditions for mass inflation
     and its de Sitter exception); Gursel, Novikov, Sandberg and Starobinsky (tails make the Cauchy horizon's energy
     density infinite); Cardoso, Yoshida, Dias and Lemos hep-th/0307122 (tails in odd dimensions).
  J2 (computed, exact) The classical blueshift belongs to the thermal clock.  In the throat (wh5_dictionary W3), infall
     from position 1's boundary leaving at global time tau_e runs on sigma = pi - (tau - tau_e); as tau_e -> pi/2 these
     lines tend to the branch of r_- from (pi/2, pi) to P1 -- position 1's Cauchy horizon CH^R -- while position 1's
     thermal time artanh(sin tau_e) -> infinity, with d(thermal)/d(global) = 1/cos tau_e -> infinity: position 1's
     whole thermal future lands on CH^R.  In global time the same infall arrives with finite blueshift.  The passage's
     light rays to position 2 run parallel to CH^R and never meet it; they cross the other branch (P1's lower-left
     edge, position 2's white-hole horizon), which collects instead the thermal future of the earlier left exterior.
  J3 (READ; computed) Classically the black-hole reading's inner horizon is unstable at both ends.  Tails fall as
     powers -- t^-(2l+3) in four dimensions, t^-(2l+D-2) in odd D, so t^-(2l+3) in five (READ) -- slower than any
     exponential, so the blueshift wins (GNSS, READ).  The de Sitter exception needs the cosmological horizon's
     surface gravity above the Cauchy horizon's (2011.07331 section 2.2, READ); on the plane H0/c = 7.3e-27 1/m
     against kappa_- r_+ of order one at r_+ = r0: a ratio of 1e-28 or less, no exception.
  J4 (computed on READ equations; the closing time an estimate, as 2011.07331's (69)) The semiclassical push, the
     plane's view of the charged mouth (four-dimensional Reissner-Nordstrom, the multiplier N l_P^2 = c l_P^2 =
     pi ell^2/8).  Eq. (41) with k1 = -kappa_-: for Reissner-Nordstrom 1 - 2 k1 r_- = r_+/r_- exactly, so the growth
     rate is Gamma = r_+/r_-^2, and with (42) Delta r_- = (N l_P^2 kappa_- r_-/(48 pi r_+))(e^{Gamma t} - 1).  It
     reaches the outer horizon at t_close = (r_-^2/r_+) ln(1 + 96 pi r_+ r_-/(N l_P^2)) (exact algebra on the first
     order): at the Earth cap with r_-/r_+ = 0.5, 1.4e-10 s with the plane's multiplier, 1.15e-9 s for one field.
  J5 (computed; the threshold an estimate) Which wins.  Gamma/kappa_- = 2 + 2 r_-/(r_+ - r_-) > 2 (exact): the
     semiclassical push outgrows the classical blueshift at late times always.  It closes the trapped region first if
     the late classical influx is a fraction below (N l_P^2/(96 pi r_+ r_-))^(kappa_-/Gamma) of the mass: 0.9% at the
     Earth cap with r_-/r_+ = 0.5 and the multiplier.
  J6 (computed) Before the Planck-curvature surface: the inner horizon stays at r_-, where the curvature in Planck
     units is K l_P^4 = 7.8e-129 at the Earth cap (r_-/r_+ = 0.5): the closing happens there, far outside any quantum
     region.
  J7 (deduced) What stage 2 settles.
     - In the cold reading (global time) the inner horizon is a regular null surface, and nothing piles up on it.
     - In the black-hole reading (thermal time) it is unstable classically at both ends.
     - On the plane, the in vacuum's negative energy pushes it outward at r_+/r_-^2, outgrowing the classical
       blueshift.  It closes the trapped region in about 20 (r_-^2/r_+)/c, before the Planck-curvature surface: the
       black-to-white transition, which 444's C2 asked for, now with the device's inner horizon.  It comes first if
       the late classical influx is below the J5 threshold.
     - The small end's semiclassical reading is outside the prior art: 2011.07331 is four-dimensional Polyakov, and
       there the plane's hole is five-dimensional.  Only J2-J3 hold there.

python3 stage2_inner.py [--selftest | --mutants]
"""
import importlib.util
import math
import os
import re
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ("yes, continue to stage 2",)
SOURCES = {
    "BBCG-41": ("2011.07331", "We see that, much like before, the redshift function tends to increase, and this leads "
                              "to a reduction of the size of the trapped region"),
    "BBCG-69": ("2011.07331", "Needless to say, this process is much quicker than the time it would take for a "
                              "Schwarzschild black hole to evaporate from the outside"),
    "BBCG-dS": ("2011.07331", "if the spacetime contains a cosmological constant, the singularity can be made to "
                              "completely disappear in special cases in which the value of the surface gravity of the "
                              "cosmological horizon is greater than that of the Cauchy horizon"),
    "GNSS": ("PRD 19, 2821", "This decay in time is sufficiently slow that the tails yield infinite energy densities on "
                             "the Cauchy horizon."),
    "CYDL": ("hep-th/0307122", "for odd D>3 we find that the field behaves as t^[-(2l+D-2)] at late times"),
}
C = 299792458.0
H0 = 67.4e3 / 3.0856775814913673e22                                    # 1/s, standard (Planck 2018)
R_EARTH_CAP = 8.870e-3


def _load(name):
    spec = importlib.util.spec_from_file_location("s2_" + name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


BS = _load("bounce_scope")
LP, ELL = BS.LP, BS.ELL


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def j1():
    return all(len(v) == 2 and len(v[1]) > 20 for v in SOURCES.values())


def j2():
    te, tau = sp.symbols("tau_e tau", real=True)
    infall = sp.pi - (tau - te)                                          # sigma along the infall line
    ch_r = sp.pi - (tau - sp.pi / 2)                                     # the branch from (pi/2, pi) to P1
    tends = sp.limit(infall - ch_r, te, sp.pi / 2) == 0
    through_p1 = sp.simplify(ch_r.subs(tau, sp.pi) - sp.pi / 2) == 0
    thermal = sp.atanh(sp.sin(te))
    rate = sp.simplify(sp.diff(thermal, te))
    rate_ok = sp.simplify(rate - 1 / sp.cos(te)) == 0
    diverges = sp.limit(rate, te, sp.pi / 2, "-") == sp.oo
    t0 = sp.Symbol("tau0", real=True)
    passage = sp.pi - (tau - t0)
    parallel = sp.simplify(sp.diff(passage - ch_r, tau)) == 0 and sp.simplify(passage - ch_r) != 0
    return tends and through_p1 and rate_ok and diverges, parallel


def rn(x, rp=1.0):
    rm = x * rp
    km = (rp - rm) / (2 * rm ** 2)
    if "schw_rate" in MUT:
        return rm, km, 1 / (2 * rm)
    gamma = (1 + 2 * km * rm) / rm                                     # 2011.07331 (41): (1 - 2 k1 r_i)/r_i, k1 = -km
    return rm, km, gamma


def j4_exact():
    rp, rm, Nl = sp.symbols("r_p r_m Nl", positive=True)
    km = (rp - rm) / (2 * rm ** 2)
    gamma = (1 + 2 * km * rm) / rm
    ok_gamma = sp.simplify(gamma - rp / rm ** 2) == 0
    t = sp.Symbol("t", positive=True)
    dr = Nl * km ** 2 / (24 * sp.pi * (1 + 2 * km * rm)) * (sp.exp(gamma * t) - 1) / (2 * km)
    tclose = rm ** 2 / rp * sp.log(1 + 96 * sp.pi * rp * rm / Nl)
    ok_close = sp.simplify(dr.subs(t, tclose) - (rp - rm)) == 0
    ratio = sp.simplify(gamma / km - (2 + 2 * rm / (rp - rm))) == 0
    return ok_gamma, ok_close, ratio


def t_close(x, rp, n_lp2):
    rm, km, gamma = rn(x, rp)
    dr_target = rp - rm
    coef = n_lp2 * km / (48 * math.pi * (1 + 2 * km * rm))
    return math.log(1 + dr_target / coef) / gamma


def threshold(x, rp, n_lp2):
    rm, km, gamma = rn(x, rp)
    return (n_lp2 / (96 * math.pi * rp * rm)) ** (km / gamma)


def kretschmann_rn(r, rp, rm):
    M, Q2 = (rp + rm) / 2, rp * rm
    return (48 * M ** 2 * r ** 2 - 96 * M * Q2 * r + 56 * Q2 ** 2) / r ** 8


def multiplier():
    if "no_multiplier" in MUT:
        return LP ** 2
    return BS.central_charge() * LP ** 2                                 # c l_P^2 = pi ell^2/8


def report():
    print("J0 M's words:", words())
    print("J1 outside art quoted:", j1())
    a, b = j2()
    print("J2 the infall lands on CH^R as the thermal clock diverges: %s; the passage parallel to CH^R: %s" % (a, b))
    kc = H0 / C
    print("J3 kappa_c = H0/c = %.2e 1/m; against kappa_- at the Earth cap (r_-/r_+ = 0.5) %.2e 1/m: ratio %.1e"
          % (kc, rn(0.5, R_EARTH_CAP)[1], kc / rn(0.5, R_EARTH_CAP)[1]))
    print("J4 Gamma = r_+/r_-^2, Delta r_- reaches r_+ at t_close, Gamma/kappa_- = 2 + 2 r_-/(r_+ - r_-):", j4_exact())
    nl = multiplier()
    for name, rp in (("10 ell", 10 * ELL), ("Earth cap", R_EARTH_CAP)):
        for x in (0.5, 0.9, 0.99):
            tm, t1 = t_close(x, rp, nl), t_close(x, rp, LP ** 2)
            print("   %-9s r_-/r_+ = %.2f: t_close %.3e s (the plane's multiplier), %.3e s (one field); threshold "
                  "%.2e" % (name, x, tm / C, t1 / C, threshold(x, rp, nl)))
    rp = R_EARTH_CAP
    rm = 0.5 * rp
    print("J6 K l_P^4 at r_- (Earth cap, 0.5): %.2e" % (kretschmann_rn(rm, rp, rm) * LP ** 4))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("J0 words: %s" % r)
    r = j1(); ok.append(r); say("J1 outside art quoted: %s" % r)
    a, b = j2(); r = a and b; ok.append(r)
    say("J2 the blueshift is the thermal clock's; the passage never meets CH^R: %s" % r)
    kc = H0 / C
    r = abs(kc / 7.28e-27 - 1) < 2e-2 and kc / rn(0.5, R_EARTH_CAP)[1] < 1e-27; ok.append(r)
    say("J3 no de Sitter exception on the plane: %s" % r)
    g, c, q = j4_exact(); r = g and c and q; ok.append(r)
    say("J4-J5 Gamma = r_+/r_-^2, the closing time, Gamma/kappa_- > 2, exact: %s" % r)
    nl = multiplier()
    tm, t1 = t_close(0.5, R_EARTH_CAP, nl) / C, t_close(0.5, R_EARTH_CAP, LP ** 2) / C
    th = threshold(0.5, R_EARTH_CAP, nl)
    closed = 0.25 * R_EARTH_CAP * math.log(1 + 768 * R_EARTH_CAP * 0.5 * R_EARTH_CAP / ELL ** 2) / C   # r_-^2/r_+
    r = abs(tm / 1.394e-10 - 1) < 5e-3 and abs(t1 / 1.153e-9 - 1) < 5e-3 and abs(th - 8.96e-3) < 5e-5
    r = r and abs(tm / closed - 1) < 1e-9
    ok.append(r)
    say("J4-J5 the Earth cap: 1.39e-10 s with the multiplier, 1.15e-9 s one field, threshold 0.9%%: %s" % r)
    rp = R_EARTH_CAP
    K = kretschmann_rn(0.5 * rp, rp, 0.5 * rp) * LP ** 4
    r = abs(K / 7.76e-129 - 1) < 1e-2; ok.append(r); say("J6 the closing far from Planck curvature: %s" % r)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    names = ("schw_rate", "no_multiplier")
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-9s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
