#!/usr/bin/env python3
"""encode_read.py -- item 437: the read, a geometric object into binary information (ENCODE), and the write by size.

M, 437: "Any information is reconstructed to obey the 26 of any position 2"; "I don't know. That's why I said we need to
address turning a geometric object into binary information, it bears on your question"; "yes, the math, always. The
write time is whatever is needed for the size of the geometric object".  M, 432 (1): "Information is energy in the
form of a binary interaction".  Labels: computed (exact unless marked), deduced, READ, standard (not READ here), M's.
Worked in the conversation; not verified; not seated.

  E0 (read) M's words, verbatim in the rulings file (432, 437).
  E1 (deduced, with a computed identity) The geometry is carried as labels of structure.  (i) No tolerance (146) with
     a finite README (131: its shortest exact binary form, N bits) admits only discrete data: a real coordinate needs
     unboundedly many bits to be exact, and a coordinate on a grid of cell d carries d/2.  (ii) A coordinate is a law
     value: in Planck units the Bohr radius is a0 = (m_P/m_e)/alpha l_P exactly (checked against CODATA 2018 to 1e-9),
     so one doubling of the electron's mass coordinate halves every atomic length in Planck units, and no coordinate is
     the same at every point of the 26-lattice (431 (2)).  At position 2 it is re-set by its 26 (437, M-RECON-ALWAYS)
     -- carrying it would exceed the shortest form (131).  (iii) A count, a site index, a species label (Z) and a bond
     (which site to which) are integers, the same at every point of the lattice.  So the read's output is a labelled
     graph -- which species sits at which site, which site bonds to which -- and the spacings are position 2's 26's
     (148, 437).  That is fork (a)'s first option, the board's reading 18 (SOURCE-REQUIRED), now deduced from M's
     131, 146, 148 and 437; it stays M's to confirm.  147's values survive as the values that are not law values.
  E2 (computed) Each bit's energy is Smarr's share of Landauer's.  At the face E(N)/N = ((D-2)/(D-3)) kT ln2, T the
     face's Hawking temperature: 2 kT ln2 on the 4D plane (kT = hbar c/(4 pi r0)), (3/2) kT ln2 on the 5D hole (kT =
     hbar c/(2 pi r_h)), exactly, from the record's E(N) at both ends (exactE; ledger.e_small).  So the README's energy
     is N binary units each a fixed multiple of the face's own Landauer cost: 432 (1)'s "information is energy" holds
     at the face with the standard relations (Smarr, Landauer; standard, not READ here).
  E3 (computed; a finding, recorded beside SOURCE-REQUIRED, not repaired) Ordinary READMEs are at the small end.  The
     large end begins at N_L = pi^2 ell^2/(2 l_P^2 ln2) = 5.31e60 bits (far_large L1), above every reading of any
     laboratory object; the record's copper table (SOURCE-REQUIRED, item 399) priced its readings with the large end's
     459,404,002.42 J per sqrt(bit).  At the small end, E5(N) = 3 pi hbar c r_h^2/(8 l5^3), r_h = l5 (2 N ln2/pi^2)^(1/3)
     (ledger.e_small), the four readings of 1 cm^3 of copper cost 6.5e6 J (envelope voxels), 1.0e15 J (atomic grid),
     1.2e14 J (isotope labels) and 2.9 J (perfect crystal), not 4.6e14, 6.5e20, 1.3e20 and 8.0e9 J.
  E4 (computed) The object's own energy against the README's.  E5 grows as N^(2/3), so an object of mass m carries
     E5(N) in its own rest energy exactly when N <= N*(m) = (m c^2/E5(1))^(3/2), which grows as m^(3/2).  For 1 cm^3 of
     copper (m c^2 = 8.05e14 J) N* = 1.37e24 bits: the isotope reading (7.57e22, 14.5 % of m c^2) and the crystal's
     labels lie under it, the 1 A atomic grid (2e24) over it.  A per-atom reading grows as m, so it lies under N* for
     every piece heavier than (N/N*)^2 m: 27.5 mg of copper for the isotope reading, 19.2 g for the atomic grid.
  E5 (computed on READ bounds) The least write time, by the size.  Margolus and Levitin (quant-ph/9710043, READ): an
     orthogonal state takes "tau >= h/(4E)" (eq. 4).  Each bit flipped on its own share (E2): tau = pi hbar/(2 E/N) =
     (pi^2/ln2) r0/c = 14.24 r0/c = 28.48 m/c clocks on the 4D plane, (2 pi^2/(3 ln2)) r_h/c = 9.49 r_h/c on the 5D
     hole -- the same number of face clocks for every N, so in seconds proportional to the face's size, which the read
     sets: 437 (2)'s "whatever is needed for the size", by the math.  At 4D it is Lloyd's black-hole bit-flip time
     (quant-ph/9908043, READ: "t_com = pi R_S/c ... t_com/t_flip = ln 2/pi").  A write pooling the whole E(N) is bounded
     instead by the light time around the face, Lloyd's t_com = pi r/c: 3.14 clocks.  Either way proportional to the
     size.  Against the record: the free-field floors (66,980 r_h/c, 199,702 m/c at the example README; 3.90 N m/c at
     the large end's own Z) rested on H-BITS-ARE-STATES, the board's (425), set aside by 432 (1).  Over 9.49 or 28.48
     clocks the face's Hawking emission takes about 5.5e-15 or 1.4e-15 of E -- the 2 % tension stated in
     LATTICE-BEARING 2, which rested on S7's share of the life, does not arise at the least write time.
  E6 (deduced; put to M) What the read decides in Q1.  T0: a face of the README's size encloses exactly E(N) whenever
     it stands; 162: it stands at that size from the opening; 432 (1): that energy is the README, which the read makes
     (399; the read before the write).  So what crosses into the face by the opening is the read's output.  (a) Its
     source: the object's own rest energy when N <= N*(m) (the destroying read, 136 (4)); the device's input making up
     at least E(N) - m c^2 when N > N* (130 (2)).  (b) Its timing: the object's energy cannot reach the face faster than
     light crosses the object -- 3.3e-11 s for 1 cm, 2.9e15 face clocks at the isotope reading -- so the read is long in
     face clocks and the opening is the end of its delivery.  On a slice (Misner-Sharp, T0) the face first appears at
     full size when the fill keeps 2m(r) < r inside until the last increment -- a uniform fill does, a centre-heavy fill
     closes a smaller face first, which 162 refuses.  Whether the delivery crosses as one whole at the opening (the
     shell) or gathers over the read, and whether the isotope is read (fork (b), 146) -- these are M's.

[Item 438, beside E1, E3, E4 and E6, not repairing them.  E1's labels are M's (fork (a): "confirm",
M-GEOMETRY-AS-LABELS).  The isotope is not in the README (fork (b): "no", M-ISOTOPE-OUT): "The README only contains the
last state of the object at position 1, not all of its states possible states, however, potential to be other states is
carried as part of the README" (M-LAST-STATE, M-POTENTIAL-IN).  So E3 and E4's isotope reading (7.57e22 bits, 1.2e14 J)
is not the copper's README; its README is the labels of its last state -- the crystal's element, lattice and shape,
about 300 bits for a perfect crystal (2.9 J at the small end), more with a real piece's defects, far under N*.  E6's
fork is answered by the math (b4d_large K12): what crosses is energy alone on the light cone (386), so the delivery is
null, and a null inflow keeps 162 only as a step -- the README crosses into the face all at once at the opening.]

python3 encode_read.py [--selftest | --mutants]
"""
import importlib.util, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((432, "Information is energy in the form of a binary interaction"),
         (437, "Any information is reconstructed to obey the 26 of any position 2"),
         (437, "we need to address turning a geometric object into binary information"),
         (437, "The write time is whatever is needed for the size of the geometric object"))
HBAR, G, C = 1.0545718176461565e-34, 6.6743e-11, 299792458.0      # as sync_face and p2_gravity
LN2 = math.log(2)
LP = math.sqrt(HBAR * G / C ** 3)
MP = math.sqrt(HBAR * C / G)
ELL = 13.964e-6                                                   # ell at its table-top ceiling (p2_gravity.ELL_MAX)
EXAMPLE_N = 2742570311524972
E_LARGE_PER_SQRT_BIT = 459404002.42356985                         # exactE.py (warptheorem T1)
# CODATA 2018 (standard, not READ here)
ME, ALPHA, A0 = 9.1093837015e-31, 1 / 137.035999084, 5.29177210903e-11
# 1 cm^3 of copper (standard values, not READ here): density, molar mass, Avogadro (exact), 63Cu/65Cu abundances
CU_M, CU_MOLAR, NA, CU_ABUND = 8.96e-3, 63.546e-3, 6.02214076e23, (0.6915, 0.3085)
LIFE_SMALL = 8.57e14                                              # close_small K5: the example's life, r_h/c clocks
LIFE_LARGE_PER_N = 2.417                                          # close_large L3: the life per N, m/c clocks, Z 108.75


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_LEDGER = None


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


def e_small(N):
    """the record's small-end E5(N) and r_h (ledger.e_small, G5 = G ell)"""
    global _LEDGER
    if _LEDGER is None:
        _LEDGER = _load(os.path.join(HERE, "ledger.py"), "er_ledger")
    E, rh, _ = _LEDGER.e_small(N, 1.0)
    return E, rh


def e_large(N):
    """the large end: E = m c^2 with 4 pi r0^2 = N 4 l_P^2 ln2, r0 = 2 G m/c^2; returns (E, r0, m)"""
    r0 = math.sqrt(N * 4 * LP ** 2 * LN2 / (4 * math.pi))
    m = r0 * C ** 2 / (2 * G)
    return m * C ** 2, r0, m


def kT_face(r, D):
    return HBAR * C / (4 * math.pi * r) if D == 4 else HBAR * C / (2 * math.pi * r)


def e1():
    """a0 in Planck units against (m_P/m_e)/alpha; the shift of atomic lengths along the electron's mass axis"""
    ident = (A0 / LP) / ((MP / ME) / ALPHA)
    shift = 1.0 if "coord_invariant" in MUT else 2.0 ** -1          # one doubling of m_e: a0 x 2^-1 in Planck units
    return {"ident": ident, "a0_planck": A0 / LP, "per_doubling": shift}


def smarr(D):
    return 1.0 if "no_smarr" in MUT else (D - 2) / (D - 3)


def e2():
    E4, r0, _ = e_large(EXAMPLE_N)
    E5, rh = e_small(EXAMPLE_N)
    return {"large": (E4 / EXAMPLE_N) / (smarr(4) * kT_face(r0, 4) * LN2),
            "small": (E5 / EXAMPLE_N) / (smarr(5) * kT_face(rh, 5) * LN2),
            "E_large_check": E4 / math.sqrt(EXAMPLE_N)}


def copper():
    atoms = CU_M / CU_MOLAR * NA
    h = -sum(p * math.log2(p) for p in CU_ABUND)
    return {"atoms": atoms, "h": h, "readings": [("envelope voxels at 1 um (Gemini's phase 1, raw)", 1e12),
                                                  ("atomic grid at 1 A, occupancy and element", 2e24),
                                                  ("element and isotope per atom", h * atoms),
                                                  ("a perfect crystal: element, lattice, shape (an estimate)", 300)]}


def n_large_start():
    return math.pi ** 2 * ELL ** 2 / (2 * LP ** 2 * LN2)


def price(N):
    """E at the end N belongs to; the mutant prices it at the large end, as the record's copper table did"""
    if "large_end" in MUT or N >= n_large_start():
        return E_LARGE_PER_SQRT_BIT * math.sqrt(N)
    return e_small(N)[0]


def n_star(m):
    """E4: N*(m) with E5(N*) = m c^2; E5 = E5(1) N^(2/3)"""
    return (m * C ** 2 / e_small(1)[0]) ** 1.5


def write_time():
    """E5: Margolus-Levitin's h/(4E) on each bit's share, in face clocks (r0/c and m/c at 4D, r_h/c at 5D)"""
    share = (lambda E, N: E) if "ml_global" in MUT else (lambda E, N: E / N)
    E4, r0, m = e_large(EXAMPLE_N)
    E5, rh = e_small(EXAMPLE_N)
    t4 = math.pi * HBAR / (2 * share(E4, EXAMPLE_N))
    t5 = math.pi * HBAR / (2 * share(E5, EXAMPLE_N))
    lloyd_flip = math.pi * r0 / C * math.pi / LN2                   # t_com = pi R_S/c, t_com/t_flip = ln2/pi (READ)
    return {"t4_r0": t4 / (r0 / C), "t4_m": t4 / (G * m / C ** 3), "t5_rh": t5 / (rh / C), "lloyd": t4 / lloyd_flip,
            "t5_s": t5, "rh": rh}


def hawking_share(t5_rh, t4_m):
    """fraction of E lost over the least write: dM/M ~ t/(2 tau) at 5D (M^2 ~ tau - t), t/(3 tau) at 4D"""
    return t5_rh / (2 * LIFE_SMALL), t4_m / (3 * LIFE_LARGE_PER_N * EXAMPLE_N)


def fill_face(profile, steps=400):
    """E6: on a slice, the radius where 2 m(r)/r first reaches 1 as the total grows to r_h/2 (units r_h = 1)"""
    for k in range(1, steps + 1):
        M = 0.5 * k / steps
        for j in range(1, steps + 1):
            r = j / steps
            frac = r ** 3 if profile == "uniform" else min(1.0, (r / 0.5) ** 3)      # centre-heavy: all inside r/2
            if 2 * M * frac / r >= 1 - 1e-12:
                return r, M
    return None, None


def report():
    print("E0 M's words inside 432 and 437:", words())
    a = e1()
    print("E1 a0/l_P = %.6e = (m_P/m_e)/alpha x %.10f; one doubling of m_e moves every atomic length by x %.1f in "
          "Planck units: a coordinate is a law value, a count is not" % (a["a0_planck"], a["ident"], a["per_doubling"]))
    b = e2()
    print("E2 E(N)/N over ((D-2)/(D-3)) kT ln2: %.12f (4D plane), %.12f (5D hole)" % (b["large"], b["small"]))
    cu = copper()
    print("E3 the large end begins at N_L = %.3e bits; 1 cm^3 of copper (%.4e atoms, %.4f isotope bits each):"
          % (n_large_start(), cu["atoms"], cu["h"]))
    for name, N in cu["readings"]:
        print("   %-58s N = %.3g  E5 = %.3g J (the table's large-end price %.3g J)" % (name, N, price(N),
                                                                                    E_LARGE_PER_SQRT_BIT * N ** 0.5))
    ns = n_star(CU_M)
    print("E4 N*(1 cm^3 Cu) = %.4g bits (m c^2 = %.4g J); isotope reading %.3g of m c^2; crossover mass %.3g mg "
          "(isotope), %.3g g (atomic grid)" % (ns, CU_M * C ** 2, price(cu["readings"][2][1]) / (CU_M * C ** 2),
                                               (cu["readings"][2][1] / ns) ** 2 * CU_M * 1e6,
                                               (2e24 / ns) ** 2 * CU_M * 1e3))
    w = write_time()
    print("E5 least write time on each bit's share: %.4f r0/c = %.4f m/c (4D; Lloyd's t_flip x %.12f), %.4f r_h/c "
          "(5D) = %.3g s at the example README; t_com = pi = %.4f clocks" % (w["t4_r0"], w["t4_m"], w["lloyd"],
                                                                            w["t5_rh"], w["t5_s"], math.pi))
    hs = hawking_share(w["t5_rh"], w["t4_m"])
    print("   Hawking share of E over it: %.2g (small end), %.2g (large end, Z = 108.75)" % hs)
    E, rh = e_small(cu["readings"][2][1])
    print("E6 1 cm^3 Cu, isotope reading: r_h = %.3g m; light across 1 cm = %.3g s = %.3g face clocks; a uniform fill "
          "closes the face at r = %s, a centre-heavy fill at r = %s (units r_h)"
          % (rh, 1e-2 / C, 1e-2 / rh, fill_face("uniform")[0], fill_face("centre")[0]))


def selftest(quiet=False):
    ok = []

    def say(s):
        if not quiet:
            print(s, flush=True)
    w0 = words(); ok.append(w0); say("E0 M's words verbatim inside 432 and 437: %s" % w0)
    a = e1()
    g1 = abs(a["ident"] - 1) < 1e-9 and a["per_doubling"] == 0.5
    ok.append(g1); say("E1 a0 = (m_P/m_e)/alpha l_P to 1e-9 (%.3e); a doubling of m_e halves it: %s" % (a["ident"] - 1,
                                                                                                     g1))
    b = e2()
    g2 = abs(b["large"] - 1) < 1e-12 and abs(b["small"] - 1) < 1e-9 and abs(b["E_large_check"]
                                                                          - E_LARGE_PER_SQRT_BIT) < 1e-3
    ok.append(g2); say("E2 E(N)/N = 2 kT ln2 (4D) and (3/2) kT ln2 (5D) exactly; E/sqrt(N) = exactE's: %s" % g2)
    cu = copper()
    pr = [price(N) for _, N in cu["readings"]]
    g3 = (abs(n_large_start() / 5.31e60 - 1) < 2e-3 and abs(cu["atoms"] - 8.491e22) < 1e19 and abs(cu["h"] - 0.8914)
          < 1e-4 and all(N < n_large_start() for _, N in cu["readings"])
          and [round(math.log10(p), 1) for p in pr] == [6.8, 15.0, 14.1, 0.5])
    ok.append(g3); say("E3 N_L = 5.31e60; copper's four readings at the small end: %s J: %s"
                       % (", ".join("%.2g" % p for p in pr), g3))
    ns = n_star(CU_M)
    iso = cu["readings"][2][1]
    g4 = (abs(ns / 1.366e24 - 1) < 2e-3 and abs(price(ns) / (CU_M * C ** 2) - 1) < 1e-9 and iso < ns < 2e24
          and abs((iso / ns) ** 2 * CU_M * 1e6 - 27.5) < 0.1 and abs((2e24 / ns) ** 2 * CU_M * 1e3 - 19.2) < 0.1)
    ok.append(g4); say("E4 N*(1 cm^3 Cu) = %.4g, isotope reading under it, atomic grid over; 27.5 mg and 19.2 g: %s"
                       % (ns, g4))
    w = write_time()
    hs = hawking_share(w["t5_rh"], w["t4_m"])
    g5 = (abs(w["t4_r0"] - math.pi ** 2 / LN2) < 1e-9 and abs(w["t5_rh"] - 2 * math.pi ** 2 / (3 * LN2)) < 1e-6
          and abs(w["lloyd"] - 1) < 1e-12 and abs(w["t4_m"] - 28.478) < 1e-3 and hs[0] < 1e-14 and hs[1] < 1e-14)
    ok.append(g5); say("E5 least write time %.4f r0/c (Lloyd's t_flip), %.4f r_h/c; Hawking share %.1e, %.1e: %s"
                       % (w["t4_r0"], w["t5_rh"], hs[0], hs[1], g5))
    u, c_ = fill_face("uniform")[0], fill_face("centre")[0]
    g6 = u == 1.0 and c_ is not None and c_ < 1.0
    ok.append(g6); say("E6 on a slice a uniform fill closes the face at full size, a centre-heavy one smaller (%s): %s"
                       % (c_, g6))
    return all(ok)


def mutants():
    names = ["coord_invariant", "no_smarr", "large_end", "ml_global"]
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-16s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
