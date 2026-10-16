#!/usr/bin/env python3
"""navlattice.py -- item 432: the strong CP angle tested as a coordinate, and the navigational lattice index of the
constants, exact and calibrated to our universe.

M, 432: "3 - are we sure it is not represented some other way in baez's list? Can we truly claim it to be a
universal constant, and can we prove it? If so, we'll be to include the proof and it as a coordinate.  4 - exact.
Recalculate in accordance with the new coordinates (build an navigational lattice index from these constants, and
calibrate to our universe)".  Labels: computed (exact unless marked), deduced, READ (verbatim at source, 2026-10-16),
standard (textbook, not READ here), M's.  Worked in the conversation; not verified; not seated.

THE STRONG CP ANGLE (M's 3)
  P0 (READ) PDG 2024, "Axions and Other Similar Particles" (rev. August 2023): "The QCD Lagrangian includes a
     CP-violating term L_Theta = -Theta-bar (alpha_s/8 pi) G G-tilde, where -pi <= Theta-bar <= +pi is the effective
     Theta parameter after diagonalizing quark masses"; "dn = C_EDM e Theta-bar", "|dn| < 1.8 x 10^-26 e cm ... imply
     |Theta-bar| <~ 10^-10"; and the Peccei-Quinn axion, whose potential has its minimum "at a = Theta-bar f_a,
     thereby canceling the Theta-bar term".  PDG 2024, quark masses: "mu differs from zero by more than 30 times the
     quoted error, making a scenario in which mu = 0 very unlikely.  This is important because there would be no
     strong CP problem if mu were to vanish."  Baez: "It's sometimes called 'theta' ... I won't count this one."
  P1 (computed, exact) Not represented in Baez's 26.  The quark masses are the singular values of the mass matrices
     and the CKM matrix is V = U_uL^dagger U_dL, both read from M M^dagger (the left-handed rotations).  Rotating the
     up-type matrix by a phase, M_u -> e^(i phi) M_u, leaves M_u M_u^dagger exactly unchanged -- so every mass and
     every CKM number (the CKM phase among them) is unchanged -- while det(M_u M_d) gains e^(3 i phi), so Theta-bar =
     Theta - arg det(M_u M_d) moves by -3 phi.  At fixed values of all 26, Theta-bar takes every value in [-pi, pi]:
     it is not a function of the 26, and the CKM phase, which is one of them, is a different parameter (the sign
     of arg det in Theta-bar is a convention).  [Standard,
     not READ: the axial anomaly shifts Theta and arg det M together, which is why only Theta-bar is physical.]
  P2 (READ; deduced) It is physical.  Theta-bar could be rotated away only if a quark were massless; m_u differs from
     zero by more than 30 standard errors (P0), so Theta-bar is observable (through the neutron EDM).
  P3 (READ; deduced) It is a constant on the theory the 26 belong to.  In the Standard Model it is a fixed
     dimensionless coefficient of the Lagrangian, as each of the 26 is; Baez leaves it out for its value ("I'm not
     counting 'zero'"), not for its standing, and under M's 431 (2) every value, zero included, is a position.  The one
     condition: if a Peccei-Quinn axion exists, Theta-bar is replaced by a field relaxed to cancel it (P0) and is then
     not a constant.  No axion is established.
  P4 So the claim the record can make, proved: Theta-bar is legitimately defined, not represented in Baez's 26 (P1),
     physical (P2), and a constant of the Standard Model with the same standing as the 26 (P3), conditional on no
     axion; our value is BOUND, |Theta-bar| <~ 1e-10 (P0).  It enters as the 27th coordinate, with this proof and that
     condition (M-PROVE-THETA).

THE NAVIGATIONAL LATTICE (M's 4)
  L1 (the board's reading of "exact ... calibrate to our universe") Every coordinate is calibrated so that our universe
     is the origin, exactly, and each axis's unit is its binary step: a doubling for a scale (a mass over the Planck
     mass, a mixing sine, a coupling, the cosmological constant over the Planck density), a sign flip -- a half turn --
     for a phase (the two CP phases and Theta-bar).  D_i = log2(x_i / x_i,ours) on a scale axis; D_i = the shortest
     signed (delta - delta_ours)/pi in (-1, 1] on a phase axis.  The three neutrino masses, of which none is measured
     one by one, are charted by the two measured splittings Delta m^2_21 and |Delta m^2_3l| (over m_P^2) and the
     lightest mass: two axes calibrated, the lightest NOT MEASURED, its origin unknown.  (A chart of the same three
     constants, the board's; the ordering, normal or inverted, is one more bit not known.)  A negative cosmological
     constant lies on a second chart (the sign), a constant exactly zero at D = -infinity.
  L2 (computed, exact) The length on the lattice: L(1 -> 2) = sum_i log2(1 + |D_i|) bits, with no tolerance (146) --
     each D_i exact -- and our universe at L = 0.  It is a metric: zero iff every D_i = 0 (R4b), zero within one
     universe (R4c), and L(1 -> 3) <= L(1 -> 2) + L(2 -> 3) exactly for real offsets, since 1 + |a + b| <= (1 + |a|)
     (1 + |b|) (R4d).  One binary step on one axis costs one bit.
  L3 (computed) The lattice index: nodes at the integer binary steps (depth 0) and, at depth d, at multiples of
     2^-d; a position whose offsets have finite binary forms sits exactly on a node (131's shortest exact binary
     form).  Our universe is the origin cell at every depth.
  L4 (computed from READ) Calibration: navigation is relative and exact; our own position is known per axis to the
     depth our measurements reach, d_i = floor(log2(1/sigma_D,i)) -- the mass axes limited by G's own precision
     (CODATA 2018, 2.2e-5) through the Planck mass.  The lightest neutrino mass's origin is not known at all, and
     Theta-bar's to |Theta-bar|/pi < 3.2e-11.
  L5 (computed) The record's positions recalculated.  2b's G scaled by g, every other dimensionful quantity held in
     SI (the board's convention for the record's 2b): each mass over m_P moves (1/2) log2 g, each splitting over m_P^2
     log2 g, the cosmological constant over the Planck density 2 log2 g, the couplings, mixings and phases not at all.
     For G2/G = 2 and 4 (355 (Q10)'s readings) L = 10.6 and 17.5 bits.  One coupling doubled: 1 bit.  A CP phase
     flipped: 1 bit.

What this does not claim: that no axion exists; our three neutrino masses or their ordering; that the binary step
per axis is the measure's last word (the board's reading under 432's "binary interaction"); 219's position, which is
a location question still.

python3 navlattice.py [--selftest | --mutants]
"""
import math, os, re, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((432, "are we sure it is not represented some other way in baez's list"),
         (432, "Can we truly claim it to be a universal constant, and can we prove it"),
         (432, "build an navigational lattice index from these constants, and calibrate to our universe"),
         (432, "Information is energy in the form of a binary interaction"))
SIG_G = 0.00015 / 6.67430              # CODATA 2018 relative uncertainty of G (PDG 2024 table 1.1, READ)
# (axis, kind, our value, our 1-sigma (larger side), source); masses in GeV over m_P are taken as ratios below
OURS = [
    ("u", "mass", 2.16e-3, 7.0e-5, "PDG 2026 data file"), ("d", "mass", 4.70e-3, 7.0e-5, "PDG 2026"),
    ("s", "mass", 9.29e-2, 7.0e-4, "PDG 2026"), ("c", "mass", 1.273, 5.0e-3, "PDG 2026"),
    ("b", "mass", 4.186, 6.0e-3, "PDG 2026"), ("t", "mass", 172.60, 0.27, "PDG 2026"),
    ("e", "mass", 5.1099895069e-4, 1.6e-13, "PDG 2026"), ("mu", "mass", 0.1056583755, 2.3e-9, "PDG 2026"),
    ("tau", "mass", 1.77693, 9.0e-5, "PDG 2026"),
    ("dm2_21", "split", 7.49e-5, 0.19e-5, "NuFIT 6.0 T1 (eV^2)"), ("dm2_3l", "split", 2.513e-3, 0.021e-3, "NuFIT 6.0"),
    ("m_light", "mass?", None, None, "NOT MEASURED"),
    ("ckm_s12", "scale", 0.22501, 0.00068, "PDG 2024 (12.28)"), ("ckm_s13", "scale", 0.003732, 0.000090, "(12.28)"),
    ("ckm_s23", "scale", 0.04183, 0.00079, "(12.28)"), ("ckm_delta", "phase", 1.147, 0.026, "(12.28)"),
    ("pmns_s2_12", "scale", 0.308, 0.012, "NuFIT 6.0 T1"), ("pmns_s2_23", "scale", 0.470, 0.017, "NuFIT, octant open"),
    ("pmns_s2_13", "scale", 0.02215, 0.00058, "NuFIT 6.0 T1"),
    ("pmns_delta", "phase", math.radians(212), math.radians(41), "NuFIT 6.0 T1"),
    ("m_H", "mass", 125.13, 0.11, "PDG 2026"),
    ("v", "mass", 246.22, 246.22 * (6e-12 / 1.1663788e-5) / 2, "PDG 2024; sigma from G_F, v = (sqrt2 G_F)^(-1/2)"),
    ("alpha_1", "scale", None, None, "computed"), ("alpha_2", "scale", None, None, "computed"),
    ("alpha_s", "scale", 0.1187, 0.0017, "PDG 2024 EW fit"),
    ("Lambda", "scale", None, None, "Planck 2018"), ("theta_bar", "phase", 0.0, 1e-10, "BOUND, PDG axions"),
]


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


def p1_theta():
    """P1: M_u -> e^(i phi) M_u keeps M_u M_u^dagger (masses, CKM) and moves det by e^(3 i phi)"""
    phi = sp.Symbol("phi", real=True)
    a = sp.symbols("a0:9", real=True)
    b = sp.symbols("b0:9", real=True)
    M = sp.Matrix(3, 3, [a[k] + sp.I * b[k] for k in range(9)])
    rot = sp.exp(sp.I * phi) * M
    if "phase_leaks" in MUT:
        rot = sp.diag(sp.exp(sp.I * phi), 1, 1) * M                     # the mutant: M M^dagger not kept
    keep = sp.simplify(rot * rot.H - M * M.H) == sp.zeros(3)
    det = sp.simplify(rot.det() - sp.exp(3 * sp.I * phi) * M.det()) == 0
    return keep and det


def our_alphas():
    a_hat, s2 = 1 / 127.930, 0.23129
    da, ds = 0.008 / 127.930, 0.00004
    a1, a2 = a_hat / (1 - s2), a_hat / s2
    s1 = math.hypot(da, ds / (1 - s2))                                  # relative sigmas
    s2r = math.hypot(da, ds / s2)
    return (a1, a1 * s1), (a2, a2 * s2r)


def our_lambda():
    """rho_Lambda / rho_P and its relative sigma from Planck 2018's H0, Omega_m (flat), and G"""
    G, HB, C, MPC = 6.6743e-11, 1.0545718176461565e-34, 299792458.0, 3.0856775814913673e22
    H0 = 67.4e3 / MPC
    rho = (1 - 0.315) * 3 * H0 ** 2 * C ** 2 / (8 * math.pi * G)
    rhoP = C ** 7 / (HB * G ** 2)
    rel = math.sqrt((0.007 / 0.685) ** 2 + (2 * 0.5 / 67.4) ** 2 + SIG_G ** 2)
    return rho / rhoP, rel


def axes():
    out = []
    (a1, s1), (a2, s2) = our_alphas()
    lam, lrel = our_lambda()
    for name, kind, val, sig, src in OURS:
        if name == "alpha_1":
            val, sig = a1, s1
        elif name == "alpha_2":
            val, sig = a2, s2
        elif name == "Lambda":
            val, sig = lam, lam * lrel
        out.append((name, kind, val, sig, src))
    if "drop_theta" in MUT:
        out = out[:-1]
    return out


def depth(kind, val, sig):
    """L4: the binary depth to which our own position is known on one axis"""
    if val is None:
        return None
    if kind == "phase":
        sd = sig / math.pi
    else:
        rel = sig / val
        if kind == "mass":
            rel = math.hypot(rel, SIG_G / 2)                            # m / m_P, m_P = sqrt(hbar c / G)
        elif kind == "split":
            rel = math.hypot(rel, SIG_G)                                # Delta m^2 / m_P^2
        sd = rel / math.log(2)
    return math.floor(math.log2(1 / sd))


def length(D):
    """L2: sum log2(1 + |D_i|), exact; the mutant 'tolerance' rounds each offset to a cell"""
    if "tolerance" in MUT:
        D = [float(round(d)) for d in D]                               # cells of one binary step
    return sum(math.log2(1 + abs(d)) for d in D)


def g_shift(g):
    """L5: the offsets of 2b with G scaled by g, every other dimensionful quantity held in SI"""
    D = []
    for name, kind, *_ in axes():
        if kind in ("mass", "mass?"):
            D.append(0.5 * math.log2(g))
        elif kind == "split":
            D.append(math.log2(g))
        elif name == "Lambda":
            D.append(2 * math.log2(g))
        else:
            D.append(0.0)
    return D


def metric_checks():
    a, b = sp.symbols("a b", nonnegative=True)
    sym = sp.expand((1 + a) * (1 + b) - (1 + a + b)) == a * b
    grid = [x / 8 for x in range(-40, 41)]
    real = all(math.log2(1 + abs(x + y)) <= math.log2(1 + abs(x)) + math.log2(1 + abs(y)) + 1e-12
               for x in grid for y in grid)
    k = len(axes())
    return sym and real and length([0.0] * k) == 0 and length([0.0] * (k - 1) + [1.0]) == 1.0


def report():
    print("P1 Theta-bar not a function of the 26 (M M^dagger kept, det moved by e^(3 i phi)):", p1_theta())
    print("axes %d (Baez's 26 with the neutrino chart, and Theta-bar):" % len(axes()))
    tot = 0
    for name, kind, val, sig, src in axes():
        d = depth(kind, val, sig)
        tot += d or 0
        print("   %-11s %-6s %-14s depth %-5s %s" % (name, kind, "--" if val is None else "%.6g" % val,
                                                    "--" if d is None else d, src))
    print("our own address known to %d bits in all (navigation itself exact)" % tot)
    print("L2 a metric, zero at ours, one bit per binary step:", metric_checks())
    for g in (2, 4):
        print("L5 2b with G2/G = %d: L = %.2f bits" % (g, length(g_shift(g))))


def selftest(quiet=False):
    ok = []
    def say(s):
        if not quiet:
            print(s, flush=True)
    w = words(); ok.append(w); say("N0 M's words verbatim inside 432: %s" % w)
    p = p1_theta(); ok.append(p); say("P1 masses and CKM kept, det(M_u M_d) moved: Theta-bar not in the 26: %s" % p)
    ax = axes()
    n = len(ax) == 27 and ax[-1][0] == "theta_bar"
    ok.append(n); say("P4 the 27th coordinate Theta-bar entered, with the proof: %s" % n)
    unknown = [a[0] for a in ax if a[2] is None]
    c = unknown == ["m_light"]; ok.append(c)
    say("L1 the neutrino chart: two splittings calibrated, the lightest mass NOT MEASURED: %s" % c)
    m = metric_checks(); ok.append(m); say("L2 the length a metric, zero at ours, one bit per binary step: %s" % m)
    L2, L4 = length(g_shift(2)), length(g_shift(4))
    want2 = 12 * math.log2(1.5) + 2 * 1 + math.log2(3)
    want4 = 12 * 1 + 2 * math.log2(3) + math.log2(5)
    l5 = abs(L2 - want2) < 1e-12 and abs(L4 - want4) < 1e-12 and abs(L2 - 10.6) < 0.05 and abs(L4 - 17.5) < 0.05
    ok.append(l5); say("L5 2b at G2/G = 2 and 4: %.2f and %.2f bits, exact: %s" % (L2, L4, l5))
    d_e = depth("mass", 5.1099895069e-4, 1.6e-13)
    l4 = d_e == math.floor(math.log2(math.log(2) / (SIG_G / 2)))
    ok.append(l4); say("L4 the mass axes' calibration limited by G (electron at depth %d): %s" % (d_e, l4))
    return all(ok)


def mutants():
    names = ["phase_leaks", "drop_theta", "tolerance"]
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-12s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
