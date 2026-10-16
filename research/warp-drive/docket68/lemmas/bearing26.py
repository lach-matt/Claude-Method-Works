#!/usr/bin/env python3
"""bearing26.py -- items 433 and 436: where the 26 coordinates enter the work, and how the approach adjusts.

M, 433: "consider how the new navigation coordinates bear on the very work we are doing. Adjust you approach
accordingly and wisely sir."  M, 436: "Thank you. Please continue".  The lattice has 26 coordinates (434-435).
Labels: computed (exact unless marked), deduced, READ, standard (not READ here), M's.  Worked in the conversation;
not verified; not seated.

  G0 (read) M's words, verbatim in the rulings file (433, 436).
  G1 (computed) The 26 enter the face's physics through one door: the species count Z, the particles lighter than the
     face's temperature.  The carrier at the bound has kT = (8/3) kT_H (source_capacity S6), kT_H = hbar c/(4 pi r0)
     on the 4D plane and hbar c/(2 pi r_h) on the 5D hole (hbar c = 197.3269804 MeV fm, PDG 2024 table 1.1, READ).
     Small end (r_h = 1.12008e-20 m): kT = 7.5 TeV, every Standard Model species free, Z = 106.75 -- the record's
     figure (standard count: 28 bosonic, 90 fermionic at 7/8).  Large end: kT = 1.5e-4 eV at r0 = 20 ell and 4.7e-6 eV
     at the Earth cap -- below the electron by nine orders and below the two heavier neutrinos (m2 >= 8.65 meV, m3 >=
     50.1 meV from NuFIT 6.0's splittings): Z = 2 (the photon), or 3.75 if the lightest neutrino, whose mass no one
     has measured, lies below kT.  The graviton is not counted, as in 386's Z = 2.
  G2 (computed) Position 2's side.  Its face is the same in its own Planck units (address26 A5), so its temperature
     over its own Planck energy is the same; a species counts there iff its mass over position 2's Planck mass lies
     below that, which on the lattice is D_i < D_i* = log2((kT/E_P) / (m_i/m_P)_ours) for each mass axis.  At the large
     end D* for the electron is -31.7 doublings: a position 2 emits electrons from its face only if its electron is
     2^31.7 times lighter (relative to its Planck mass) than ours.  Z2 is a step function of position 2's mass
     coordinates, nothing else.
  G3 (computed; a finding, recorded beside source_capacity, not repaired) The record's large-end figures at Z = 108.75
     (source_capacity S3, S4 and S7's life; close_large L3) count Standard Model species the face is far too cold to
     carry.  At Z = 2 the write's least time (45/4) N ln2/Z is 3.90 N clocks, at Z = 3.75 2.08 N, against 0.0717 N at
     108.75; the life grows by the same factor, so S7's share, 5.9 %, is unchanged (Z cancels).
  G4 (deduced) The bearing, by kind.
     (a) None of the 26 but Lambda (and sigma beside them): the face (sync_face T0, Y1, Y2; O1b, O1c; M1P2x, H2tx,
         E1x, CLOSE) and the bulk (B3, B4a, B4d, B4ds) -- the bulk carries gravity alone (the brane models the record
         READ, 143's text: only gravity crosses), so it sees sigma, Lambda and E(N), and the other 25 live on the
         planes.  The synchronization model stands unchanged.
     (b) The 26 through Z: the write's least time, the face's life, the Hawking loss over the write (its 2 % share
         Z-free), and ARRIVAL's clocks -- at the large end set by whether the lightest neutrino is below 1.5e-4 eV.
     (c) Position 2's 26: what position 2 builds (240), whether the README's object can be reconstructed from its
         stock (24, 136 H), the copy's survival (240), and its own Z2 (G2).  Reachable is every position (427, 431
         (2)); reconstructible is a region of the lattice, not yet measured.
     (d) The offsets: the length L (navlattice L2) -- the difference position 2 needs to build the copy under its own
         laws (240, 114 (c)), carried in the length and not the width (117, 136 (3)); by 432 (1) it is energy, but L
         is tens of bits against N, so its energy is negligible beside E(N).
     (e) The README's encoding: one fixed exact encoding (136 (5)) with no tolerance in what every universe shares
         (146) must read the same at every point of the lattice -- in units the 26 do not change (Planck units, or
         labels and counts), not in our SI or our atoms' sizes.  This bears on SOURCE's read (399's forks).
  G5 (deduced) The approach, adjusted.  Stage 3 re-poses ARRIVAL, B3 and B4d at the large end on the object, with (a)
     keeping B3 and B4d free of the 25, (b) putting ARRIVAL's clocks on the large end's own Z, and (c)-(e) entered as
     their own items rather than folded into the face: RECON (position 2 can rebuild the object from its stock under
     its 26) and ENCODE (the README's encoding invariant across the lattice), each put to M.

python3 bearing26.py [--selftest | --mutants]
"""
import math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((433, "consider how the new navigation coordinates bear on the very work we are doing"),
         (436, "Thank you. Please continue"))
HBARC_EV_M = 197.3269804e-9              # eV m (PDG 2024 table 1.1: 197.3269804 MeV fm)
ELL = 13.964e-6                          # ell at its table-top ceiling (earth_cap K3)
HOLES = {"small end (5D, r_h = 1.12008e-20 m)": (1.12008e-20, 5), "large end, r0 = 20 ell": (20 * ELL, 4),
         "large end, the Earth cap (r0 = 8.870 mm)": (8.870e-3, 4)}
E_P_EV = 1.22089e28                      # the Planck energy (CODATA 2018, scipy), eV
# (species, mass in eV, bosonic dof, fermionic dof); masses READ (PDG 2026 data file; NuFIT 6.0 splittings); the
# neutrino rows give lower bounds; m1 is not measured
SPECIES = [("photon", 0.0, 2, 0), ("gluons", 0.0, 16, 0), ("W", 80.362e9, 6, 0), ("Z", 91.1879e9, 3, 0),
           ("H", 125.13e9, 1, 0), ("u", 2.16e6, 0, 12), ("d", 4.70e6, 0, 12), ("s", 92.9e6, 0, 12),
           ("c", 1.273e9, 0, 12), ("b", 4.186e9, 0, 12), ("t", 172.60e9, 0, 12), ("e", 0.51099895e6, 0, 4),
           ("mu", 105.658e6, 0, 4), ("tau", 1776.93e6, 0, 4), ("nu1", None, 0, 2),
           ("nu2", math.sqrt(7.49e-5), 0, 2), ("nu3", math.sqrt(2.513e-3), 0, 2)]
LAMBDA_QCD_EV = 0.2e9                    # below it quarks and gluons are not free (standard, not READ)


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


def kT(r, D):
    """G1: the carrier's kT at the bound, (8/3) of Hawking's, in eV"""
    th = HBARC_EV_M / (4 * math.pi * r) if D == 4 else HBARC_EV_M / (2 * math.pi * r)
    return th if "no_83" in MUT else (8 / 3) * th                    # the mutant drops S6's factor


def Z(T, nu1_light):
    """G1: bosonic dof plus 7/8 of fermionic dof for the species lighter than T (nu1 by assumption)"""
    z = 0.0
    for name, m, b, f in SPECIES:
        if name in ("gluons", "u", "d", "s", "c", "b", "t") and T < LAMBDA_QCD_EV:
            continue                                                 # confined
        light = nu1_light if m is None else (m < T)
        if "count_all" in MUT:
            light = True
        if light:
            z += b + 0.875 * f
    return z


def thresholds(T):
    """G2: D_i* = log2((kT/E_P) / (m_i/m_P)_ours) for the massive species with a measured mass"""
    out = {}
    for name, m, b, f in SPECIES:
        if m:
            out[name] = math.log2((T / E_P_EV) / (m / E_P_EV))
    return out


def stale(z):
    """G3: tau_min = (45/4) N ln2 / Z clocks, per N"""
    return 45 / 4 * math.log(2) / z


def report():
    print("G0 M's words inside 433 and 436:", words())
    for k, (r, D) in HOLES.items():
        T = kT(r, D)
        print("G1 %-42s kT = %.3g eV; Z = %.2f (lightest neutrino heavier) or %.2f (lighter)" % (k, T, Z(T, False),
                                                                                                 Z(T, True)))
    T = kT(20 * ELL, 4)
    th = thresholds(T)
    print("G2 large end, the lattice threshold D* (doublings) a position 2's species must fall below to count:")
    print("   " + ", ".join("%s %.1f" % (k, v) for k, v in th.items()))
    print("G3 tau_min per N: %.4f (Z = 108.75, the record's), %.2f (Z = 2), %.2f (Z = 3.75)" % (stale(108.75),
                                                                                          stale(2), stale(3.75)))


def selftest(quiet=False):
    ok = []
    def say(s):
        if not quiet:
            print(s, flush=True)
    w = words(); ok.append(w); say("G0 M's words verbatim inside 433 and 436: %s" % w)
    Ts = kT(1.12008e-20, 5)
    g1s = abs(Z(Ts, True) - 106.75) < 1e-9 and Ts > 1e12
    ok.append(g1s); say("G1 small end: kT = %.3g eV, every species free, Z = 106.75 (the record's): %s" % (Ts, g1s))
    Tl, Te = kT(20 * ELL, 4), kT(8.870e-3, 4)
    g1l = (Z(Tl, False) == 2 and Z(Tl, True) == 3.75 and Z(Te, False) == 2 and abs(Tl - 1.5e-4) < 0.05e-4
           and abs(Te - 4.7e-6) < 0.1e-6)
    ok.append(g1l)
    say("G1 large end: kT = %.2g and %.2g eV, Z = 2 or 3.75 by the lightest neutrino: %s" % (Tl, Te, g1l))
    th = thresholds(Tl)
    g2 = abs(th["e"] - (-31.7)) < 0.05 and all(v < 0 for v in th.values())
    ok.append(g2); say("G2 position 2's thresholds: the electron at %.1f doublings, all species below ours: %s"
                       % (th["e"], g2))
    g3 = abs(stale(108.75) - 0.0717) < 1e-4 and abs(stale(2) - 3.90) < 0.005 and abs(stale(3.75) - 2.08) < 0.005
    ok.append(g3); say("G3 the record's large-end Z = 108.75 overcounts: 0.0717 N against 3.90 N and 2.08 N: %s" % g3)
    return all(ok)


def mutants():
    names = ["count_all", "no_83"]
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-10s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
