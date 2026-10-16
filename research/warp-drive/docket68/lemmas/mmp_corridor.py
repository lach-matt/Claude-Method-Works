#!/usr/bin/env python3
"""mmp_corridor.py -- item 445 (2): Maldacena, Milekhin and Popov's wormhole computed on the plane as the corridor, its
mouths magnetically charged as a device specification, the passage one-way by its use.  M: "2 - Should I compute this
wormhole on the plane as the corridor? - yes".  Labels: READ (the two papers, quoted in BOUNCE-RESEARCH section 9),
computed (sympy exact where marked; numbers at standard constants), imported (the record's instruments named),
estimate, deduced.  Worked in the conversation; not verified; not seated.  2026-10-16.

The prior art is two papers, both READ in full:
  MMP  Maldacena, Milekhin, Popov, "Traversable wormholes in four dimensions", 1807.04726: Einstein-Maxwell with
       charged massless fermions; two oppositely charged near-extremal magnetic black holes whose throats are joined;
       the fermions' lowest Landau level gives c_2 two-dimensional modes on the field-line circles, whose negative
       Casimir energy holds the throat open.  Its section 8 points to Randall-Sundrum II.
  MM   Maldacena, Milekhin, "Humanly traversable wormholes", 2008.06618: the same wormhole in Randall-Sundrum II with a
       bulk U(1); the 4D CFT in the throat's magnetic field flows to AdS3 x R^2, a 2D CFT whose central charge grows
       with the flux; "what looks like a quantum Casimir energy in four dimensions is actually a classical effect in
       five dimensions (the negative classical energy of AdS3)", and the field-line circle is filled in by the fifth
       dimension.  It holds for r_e >> R5; its existence is argued by patching, the full 5D solution not computed.

  V0 (read) M's words: 445 (2).
  V1 (computed, exact, on READ relations) MMP's balance.  E(l) = r_e^3/(G l^2) - c_2/(8 l) is least at
     l = 16 r_e^3/(G c_2), binding -c_2/(16 l) = -G c_2^2/(256 r_e^3); with r_e^2 = pi q^2 l_p^2/g^2 and c_2 = N_f q,
     l/r_e = 16 pi q/(g^2 N_f) (MMP 5.31, 7.58; MM 2.12-2.15).  The Standard Model's charges and degeneracies give
     N_f = 54 (MMP 8.59-8.60).
  V2 (computed, exact, on READ relations) MM's plane.  From MM (3.21) with 1/G4 = s R5/(2 G5) and 1/g4^2 = s (R5/g5^2)
     log(l_B/R5), log(l_B/R5) = log(r_e/R5)/2, the bulk on s = 1 or 2 sides: c_2 = 4 pi R5 r_e/(G4 sqrt(L)), L =
     log(r_e/R5), the same for s = 1 and s = 2 (our plane is two-sided, B6'), and independent of the gauge coupling.
     Hence l = (4/pi) r_e^2 sqrt(L)/R5 and E_bind = (pi^2/16) R5^2/(G4 r_e L), as MM print.  MM's own case (r_e = 0.05
     light-seconds, R5 = 50 um) reproduces their (3.27): c_2 7e72, l 3e3 light-years, gamma 2e12, E_bind 5e9 kg.
  V3 (computed) On our plane, R5 = ell = 13.964 um (bounce_scope), at the large end (r_e = r0):
     - the Earth cap (8.870 mm): c_2 = 2.35e63, l = 18.2 m, the passage seen outside pi l/c = 1.9e-7 s, the boost
       gamma = 2055, E_bind = 2.5e35 J (2.8e18 kg), the gap hbar c/l = 1.1e-8 eV, so the dark sector must be colder
       than 1.3e-4 K; each mouth an extremal hole of 1.19e25 kg (two Earths);
     - r_e = 10 ell: l = 2.70 mm, E_bind = 4.5e37 J;
     - r0 = 1.25 ell, the large end's foot, lies outside MM's regime (r_e/R5 = 1.25; l_B is not between R5 and r_e).
     The README's energy (room_work: 7.79e12 J for the real piece) is 3e-23 of the Earth cap's binding; its 1.3e21
     bits against c_2 = 2.3e63 quanta per l of capacity (MM: "~ c_2 qubits per l").
  V4 (computed; estimate where marked) Holding the mouths.  Orbiting (MM B.32), Omega = sqrt(r_e/d^3) << 1/l needs
     d >> (r_e l^2)^(1/3) = 1.43 m at the Earth cap, with d <~ l = 18.2 m; MM's lifetime (B.34) (3/4) d^3/r_e^2 is
     0.19 s at d = l, 1e6 passages.  Always pi l > d (MMP 5.46, figure 7): slower than light outside.
  V5 (computed) A corridor whose outside delay is one hour (pi l = c x 3600 s) has mouths of r_e = 942 m (0.64 solar
     masses each).  Put to M as a question, not a reading: whether 218's hour is the corridor's delay.
  V6 (computed on READ conditions; deduced) The Standard Model's own fields (MMP section 8) need the mouths' distance
     below the electroweak scale, hbar c/(1 TeV) = 1.97e-19 m, 1.4e-14 of ell: there the plane's hole is five-
     dimensional and MMP's four-dimensional gravity does not hold.  The small end (r_h = 1.12e-20 m, b4d_small) is
     below that scale but five-dimensional for the same reason.  Neither end takes the Standard Model version.
  V7 (deduced) What it gives the record.
     - A corridor on the plane at the large end, needing a U(1) gauge field in the bulk (the record's bulk has gravity
       alone) and two oppositely magnetically charged extremal mouths (445 (2)'s device).
     - No horizon, no trapped surface, no core: the passage through it needs no bounce.  If the corridor is this
       object, O1a-O1c are re-posed, not proved as written.
     - 179 in established physics, in part: the negative energy is the bulk's classical AdS3 energy and the field-line
       circle closes through the fifth dimension (MM, READ); the passage itself runs through the plane's throat.
     - The README passes as quanta above the gap with total energy under E_bind; one-way by its use.
     - It stands before the README: it is not formed by the README's energy (162, 270, 276 bear on this).
     - The small end lies outside it; no prior art was found there.
     - Its existence is argued, not computed: the full five-dimensional solution is the computation it leaves.

python3 mmp_corridor.py [--selftest | --mutants]
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
WORDS = ("2 - Should I compute this wormhole on the plane as the corridor? - yes",)
HBAR, G, C = 1.0545718176461565e-34, 6.6743e-11, 299792458.0          # standard (CODATA), as encode_read
LP = math.sqrt(HBAR * G / C ** 3)
EV, KB, LY = 1.602176634e-19, 1.380649e-23, 9.4607304725808e15         # standard (SI exact; IAU light-year)
TEV_LENGTH = HBAR * C / (1e12 * EV)                                    # hbar c / 1 TeV, m
R_EARTH_CAP = 8.870e-3                                                 # m, the large end's top (372), as bounce_scope
M_EARTH = 5.972e24                                                     # kg, standard


def _load(name):
    spec = importlib.util.spec_from_file_location("mmp_" + name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def v1():
    """MMP's balance minimized, the free-fermion length, and the Standard Model's N_f"""
    re_, Gs, c2, l, q, g, lp, Nf = sp.symbols("r_e G c_2 l q g l_p N_f", positive=True)
    E = re_ ** 3 / (Gs * l ** 2) - c2 / (8 * l)
    lstar = [s for s in sp.solve(sp.diff(E, l), l) if s.is_positive][0]
    ok_l = sp.simplify(lstar - 16 * re_ ** 3 / (Gs * c2)) == 0
    Eb = sp.simplify(E.subs(l, lstar))
    ok_E = sp.simplify(Eb + c2 / (16 * lstar)) == 0 and sp.simplify(Eb + Gs * c2 ** 2 / (256 * re_ ** 3)) == 0
    sub = {re_: sp.sqrt(sp.pi) * q * lp / g, Gs: lp ** 2, c2: Nf * q}
    ratio = sp.simplify((lstar / re_).subs(sub))
    ok_ratio = sp.simplify(ratio - 16 * sp.pi * q / (g ** 2 * Nf)) == 0
    charges, degen = (-6, 3, 4, -2, -1), (1, 2, 3, 3, 6)               # MMP (8.60) and its footnote 11
    nf_sm = sp.Rational(3, 2) * sum(abs(a) * b for a, b in zip(charges, degen))
    return ok_l, ok_E, ok_ratio, nf_sm


def c2_closed(re_, R5, G4, L):
    return 4 * sp.pi * R5 * re_ / (G4 * sp.sqrt(L))


def v2():
    """c_2 from MM (3.21) on one-sided and two-sided bulks; l and E_bind in MM's closed forms"""
    re_, R5, lp, g4, L = sp.symbols("r_e R_5 l_p g_4 L", positive=True)
    G4 = lp ** 2
    out = {}
    for s in (1, 2):
        G5 = s * R5 * G4 / 2                                            # 1/G4 = s R5/(2 G5)
        g5 = sp.sqrt(s * R5 * (L / 2)) * g4                             # 1/g4^2 = s (R5/g5^2) log(l_B/R5)
        if "one_side" in MUT and s == 2:
            g5 = sp.sqrt(R5 * (L / 2)) * g4
        q = g4 * re_ / (sp.sqrt(sp.pi) * lp)
        per_side = 2 * sp.pi ** sp.Rational(3, 2) * sp.sqrt(R5 ** 3 / G5) * (sp.sqrt(R5) / g5) * q
        c2 = sp.simplify(s * per_side)
        out[s] = sp.simplify(c2 - c2_closed(re_, R5, G4, L)) == 0
    c2 = c2_closed(re_, R5, G4, L)
    l = sp.simplify(16 * re_ ** 3 / (G4 * c2))
    ok_l = sp.simplify(l - 4 * re_ ** 2 * sp.sqrt(L) / (sp.pi * R5)) == 0
    Eb = sp.simplify(c2 / (16 * l))
    ok_E = sp.simplify(Eb - sp.pi ** 2 * R5 ** 2 / (16 * G4 * re_ * L)) == 0
    return out, ok_l, ok_E


def point(re_, R5):
    """MM's wormhole at mouth radius re_ (m) on a plane of AdS radius R5 (m); energies in 1/m converted by hbar c"""
    L = math.log(re_ / R5)
    sq = 1.0 if "no_log" in MUT else math.sqrt(L)
    G4 = LP ** 2
    c2 = 4 * math.pi * R5 * re_ / (G4 * sq)
    ell_w = 16 * re_ ** 3 / (G4 * c2)
    eb_inv_m = c2 / (16 * ell_w)
    lB = (3 * L) ** 0.25 * math.sqrt(re_ * R5) if L > 0 else float("nan")
    return dict(L=L, c2=c2, l=ell_w, delay=math.pi * ell_w / C, gamma=ell_w / re_,
                Eb_J=eb_inv_m * HBAR * C, Eb_kg=eb_inv_m * HBAR / C, gap_eV=HBAR * C / ell_w / EV,
                Tmax=HBAR * C / ell_w / KB, lB=lB, Me=re_ * C ** 2 / G,
                regime=(re_ / R5 >= 10) and (R5 < lB < re_),
                d_rot=(re_ * ell_w ** 2) ** (1 / 3), life_at_l=0.75 * ell_w ** 3 / re_ ** 2 / C)


def mm_case():
    """MM (3.27): r_e = 0.05 light-seconds, R5 = 50 um"""
    return point(0.05 * C, 50e-6)


def ell():
    return _load("bounce_scope").ELL


def v3():
    e = ell()
    rows = {name: point(r, e) for name, r in (("1.25 ell", 1.25 * e), ("10 ell", 10 * e), ("100 ell", 100 * e),
                                              ("Earth cap", R_EARTH_CAP))}
    n_perfect, e_perfect, n_real, e_real = _load("room_work").budget()
    return rows, (n_real, e_real)


def v5():
    """the mouth radius whose outside delay pi l/c is one hour (bisection on the monotone l(r_e))"""
    e, target = ell(), C * 3600.0
    lo, hi = 10 * e, 1e9
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if math.pi * point(mid, e)["l"] < target:
            lo = mid
        else:
            hi = mid
    r = math.sqrt(lo * hi)
    return r, point(r, e)["Me"] / 1.98892e30


def v6():
    rh = _load("b4d_small").RH
    return TEV_LENGTH, TEV_LENGTH / ell(), rh, rh < TEV_LENGTH, rh / ell()


def report():
    print("V0 M's words:", words())
    ok_l, ok_E, ok_r, nf = v1()
    print("V1 l = 16 r_e^3/(G c_2) %s, E_bind = -G c_2^2/(256 r_e^3) %s, l/r_e = 16 pi q/(g^2 N_f) %s; SM N_f = %s"
          % (ok_l, ok_E, ok_r, nf))
    sides, okl, okE = v2()
    print("V2 c_2 = 4 pi R5 r_e/(G4 sqrt L) on one side %s, two sides %s; l and E_bind as MM print: %s %s"
          % (sides[1], sides[2], okl, okE))
    m = mm_case()
    print("   MM's case: c_2 %.2e, l %.2e ly, gamma %.2e, E_bind %.2e kg, gap %.1e eV"
          % (m["c2"], m["l"] / LY, m["gamma"], m["Eb_kg"], m["gap_eV"]))
    rows, (n_real, e_real) = v3()
    for name, p in rows.items():
        print("V3 %-9s L %.3f regime %-5s c_2 %.3e l %.4g m delay %.3g s gamma %.4g E_bind %.3g J (%.3g kg) gap %.3g eV"
              " T < %.3g K l_B %.3g m mouth %.3g kg" % (name, p["L"], p["regime"], p["c2"], p["l"], p["delay"],
                                                        p["gamma"], p["Eb_J"], p["Eb_kg"], p["gap_eV"], p["Tmax"],
                                                        p["lB"], p["Me"]))
    cap = rows["Earth cap"]
    print("   the README: %.3g J = %.2g of the Earth cap's binding; %.3g bits against c_2 %.3g per l"
          % (e_real, e_real / cap["Eb_J"], n_real, cap["c2"]))
    print("V4 orbiting needs d >> %.3g m, with d <~ l = %.3g m; lifetime at d = l %.3g s (%.2g passages)"
          % (cap["d_rot"], cap["l"], cap["life_at_l"], cap["life_at_l"] / cap["delay"]))
    r1h, msun = v5()
    print("V5 a one-hour corridor: r_e = %.4g m, %.3g solar masses per mouth" % (r1h, msun))
    tev, tev_ell, rh, below, rh_ell = v6()
    print("V6 hbar c/TeV = %.3g m = %.2g ell; the small end r_h = %.4g m (below: %s) = %.3g ell" % (tev, tev_ell, rh,
                                                                                                  below, rh_ell))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r1 = words(); ok.append(r1); say("V0 words: %s" % r1)
    ok_l, ok_E, ok_r, nf = v1()
    r1 = ok_l and ok_E and ok_r and nf == 54; ok.append(r1)
    say("V1 MMP's balance, l/r_e, the Standard Model's N_f = 54: %s" % r1)
    sides, okl, okE = v2()
    r1 = sides[1] and sides[2] and okl and okE; ok.append(r1)
    say("V2 c_2 the same on one or two sides; l and E_bind as MM print: %s" % r1)
    m = mm_case()
    r1 = (abs(m["c2"] / 7e72 - 1) < 0.1 and abs(m["l"] / LY / 3e3 - 1) < 0.1 and abs(m["gamma"] / 2e12 - 1) < 0.1
          and abs(m["Eb_kg"] / 5e9 - 1) < 0.1)
    ok.append(r1); say("V2 MM's (3.27) reproduced: %s" % r1)
    rows, (n_real, e_real) = v3()
    cap, ten, foot = rows["Earth cap"], rows["10 ell"], rows["1.25 ell"]
    r1 = (abs(cap["c2"] / 2.345e63 - 1) < 2e-3 and abs(cap["l"] - 18.22) < 0.02 and abs(cap["gamma"] - 2055) < 2
          and abs(cap["Eb_J"] / 2.543e35 - 1) < 2e-3 and abs(ten["l"] / 2.698e-3 - 1) < 2e-3 and cap["regime"]
          and ten["regime"] and not foot["regime"] and abs(cap["Tmax"] / 1.256e-4 - 1) < 5e-3)
    ok.append(r1); say("V3 the Earth cap and 10 ell on our plane; the foot outside the regime: %s" % r1)
    r1 = abs(e_real / 7.79e12 - 1) < 1e-2 and e_real < 1e-20 * cap["Eb_J"] and n_real < cap["c2"]
    ok.append(r1); say("V3 the README under the binding and the capacity: %s" % r1)
    r1 = (abs(cap["d_rot"] - 1.433) < 0.01 and cap["d_rot"] < cap["l"] and cap["life_at_l"] > 1e5 * cap["delay"])
    ok.append(r1); say("V4 an orbiting window 1.43 m << d <~ 18.2 m; lifetime >> passage: %s" % r1)
    r1h, msun = v5()
    r1 = abs(r1h - 942) < 2 and abs(msun - 0.64) < 0.01; ok.append(r1)
    say("V5 the one-hour corridor's mouths, 942 m: %s" % r1)
    tev, tev_ell, rh, below, rh_ell = v6()
    r1 = abs(tev / 1.973e-19 - 1) < 1e-3 and tev_ell < 1e-13 and below and rh_ell < 1e-15; ok.append(r1)
    say("V6 the Standard Model version below ell at both ends: %s" % r1)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    names = ("no_log", "one_side")
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
