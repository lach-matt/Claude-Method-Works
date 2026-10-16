#!/usr/bin/env python3
"""address26.py -- items 429 and 431: position 2's address on the 26 universal constants (the trajectories re-posed).

M, 429: "Instead I want to utilize the Anthropic Principles of the 26 universal constants, which are in turn the 26
multiverse variants for determine relative position in an index."  M, 431: "1 - baez's list, unless we have
legitimately defined additional universal constants, in which case they too are included... 2 - a  3 - any other
true universal constant we have identified."  So the index's coordinates are Baez's 26, every value is a position
(reading (a): habitability not a factor, 24; survivability the object's, 240), and beside them stands any other true
universal constant.  Labels: computed (exact unless marked), deduced, READ, M's.  Worked in the conversation; not
verified; not seated.

  A0 (read) M's words, verbatim in the rulings file (429, 431).
  A1 (READ, Baez, "How Many Fundamental Constants Are There?", math.ucr.edu/home/baez/constants.html, 2026-10-16)
     The 26, in the parametrization "that theorists like best": six quark masses, four numbers for the Kobayashi-
     Maskawa matrix, the electron, muon and tau masses and their three neutrinos' masses, four numbers for the
     Pontecorvo-Maki-Nakagawa-Sakata matrix, the Higgs mass, the Higgs field's expectation value, the U(1), SU(2) and
     strong couplings, and the cosmological constant: 6 + 4 + 6 + 4 + 2 + 3 + 1 = 26 (computed).  The masses are made
     dimensionless by the Planck mass ("The masses of these quarks, divided by the Planck mass, give 6 dimensionless
     constants").  The strong CP angle is not counted: "until we get a glimmering of evidence that this parameter
     might be nonzero, I won't count this one."
  A2 (READ; computed) Our position, coordinate by coordinate, each with its source and status; never filled:
     masses: the PDG 2026 capture (captures/PDG-2026.tsv, md5 recorded), u 2.16, d 4.7, s 92.9, c 1273, b 4186,
       t 172600, e 0.510998951, mu 105.658376, tau 1776.93, H 125130 MeV -- the three neutrino masses are '?' there:
       NOT MEASURED (NuFIT 6.0 Table 1 gives Delta m^2_21 = 7.49e-5 eV^2 and Delta m^2_3l = +2.513e-3 eV^2; Planck
       2018 gives sum m_nu < 0.12 eV), so three of our 26 coordinates are not known and are carried as such;
     CKM: PDG 2024 review (Ceccucci, Ligeti, Sakai), eq. (12.28): sin theta12 = 0.22501, sin theta13 = 0.003732,
       sin theta23 = 0.04183, delta = 1.147;
     PMNS: NuFIT 6.0 (arXiv:2410.05380v2) Table 1, IC24 with SK atmospheric data, normal ordering: sin^2 theta12 =
       0.308, sin^2 theta23 = 0.470, sin^2 theta13 = 0.02215, delta_CP = 212 degrees -- the theta23 octant and the mass
       ordering not settled (the same table's IC19 column has 0.561), delta_CP weakly measured;
     the Higgs expectation value: v = 246.22 GeV (PDG 2024 electroweak review, Erler and Freitas);
     the couplings at M_Z in MS-bar: alpha-hat^(5)(M_Z)^-1 = 127.930 and s-hat_Z^2 = 0.23129 (same review), so
       alpha_1 = alpha-hat/c^2 and alpha_2 = alpha-hat/s^2 (e = g sin theta_W, theta_W = arctan(g'/g), READ there;
       computed); alpha_s(M_Z) = 0.1187 (the review's global fit; the PDG world average not READ here);
     the cosmological constant: Planck 2018 (arXiv:1807.06209, abstract) H0 = 67.4 km/s/Mpc, Omega_m = 0.315, flat,
       so Omega_Lambda = 0.685 (deduced, radiation neglected) and rho_Lambda c^2 = 5.25e-10 J/m^3 (computed), equal to
       201's 5.25e-10 at three figures.
     Dimensionless: each mass over the Planck mass (CODATA 2018, scipy), rho_Lambda over the Planck energy density.
  A3 (deduced; M's 431 (3)) Beside the 26.  The record has identified one further constant of a universe: sigma, the
     plane's tension, which with its offset defines our universe (M's 201); its value lies in its window, unfixed.  The
     offset is the 26th constant itself.  G is not a further coordinate: it is the unit that makes the masses
     dimensionless, so a change of G (the record's 2b) is a common scaling of the fourteen mass coordinates (A6).
     The strong CP angle theta-bar is defined in the Standard Model Lagrangian -- "legitimately defined" -- but bounded
     by the neutron EDM, d_n = (0.0 +- 1.1 stat +- 0.2 sys) x 10^-26 e cm (Abel et al., arXiv:2001.11966, READ), and
     Baez does not count it: the board's reading, put to M, carries it as a 27th coordinate with status BOUND.
     Majorana phases are not included: whether neutrinos are Majorana is not established.
  A4 (computed, exact) R4 on the 26.  The length L(1 -> 2) = sum_i log2(1 + |n_i|) bits, n_i the number of cells of
     width delta_i between position 2's value and ours (155's measure: the bits to specify position 2's values given
     ours).  R4a: it takes no README and no place, so it is a length and not a width, and not a distance.  R4b: L = 0
     iff every n_i = 0.  R4c: within one universe every constant is the same, so L = 0 there; between universes L > 0.
     R4d: L(1 -> 3) <= L(1 -> 2) + L(2 -> 3), exactly, because 1 + |a + b| <= (1 + |a|)(1 + |b|) for all integers.
     The resolution delta_i is a parameter: the board's reading is our measurement's precision, which stands in
     tension with 146 ("no tolerance in what every universe shares") -- put to M.  Under 431 there are no history
     trajectories (118), so R4c's within-universe length is zero, not the history bits: the address (116 (a), the
     device's input) carries location.
  A5 (computed, exact) The face carries none of the 26 but the cosmological constant.  In Planck units the bit area is
     A/l_P^2 = 4 N ln2 and the face's energy E/E_P = (1/2) sqrt(N ln2/pi): functions of N alone.  At the large end the
     plane enters through ell, which B6' fixes from sigma alone (sigma G ell^2 = 3/(4 pi)), and the offset -- the 26th
     -- sets the plane's flatness (201).  So position 2's face in its own Planck units is fixed by N, its sigma and its
     cosmological constant; the other 25 constants enter only what position 2 builds (240) and the length (A4).
  A6 (computed; deduced) The record's positions on the 26.  2b (G scaled by g) moves every mass over the Planck mass
     by g^(1/2): the fourteen mass coordinates (twelve fermions, the Higgs mass, v) along one ray, the rest fixed.
     219's position without the Madelung exceptions is a location question: the order is a readout of alpha and the
     electron's mass (settle.H12), so it is a point of the index only if some values of the 26 produce it -- not
     computed here.
  A7 (deduced) The Address station on the 26: R4 stands (A4); M1P2x, H2tx and E1x stand at every point of the index,
     as at every sigma (427, 428), since the face depends on N, sigma and Lambda only (A5); B4a, B4ds and B4d concern
     the bulk's geometry and carry none of the 26.

What this does not claim: the values of position 2 (the destination is the user's input, 130 (2), 116 (a)); our three
neutrino masses; the PDG world average of alpha_s; that the board's resolution is the measure's last word (146).

python3 address26.py [--selftest | --mutants]
"""
import itertools, math, os, random, re, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
PDG = os.path.join(WD, "captures", "PDG-2026.tsv")
MUT = set()
WORDS = ((429, "Anthropic Principles of the 26 universal constants"), (429, "relative position in an index"),
         (431, "baez's list, unless we have legitimately defined additional universal constants"),
         (431, "2 - a"), (431, "any other true universal constant we have identified"))
BAEZ = (("quark masses", ("u", "d", "s", "c", "b", "t")), ("CKM", ("ckm_s12", "ckm_s13", "ckm_s23", "ckm_delta")),
        ("lepton masses", ("e", "mu", "tau", "nu1", "nu2", "nu3")),
        ("PMNS", ("pmns_s2_12", "pmns_s2_23", "pmns_s2_13", "pmns_delta")),
        ("Higgs", ("m_H", "v")), ("couplings", ("alpha_1", "alpha_2", "alpha_s")), ("cosmological", ("Lambda",)))
PDGID = {"u": 2, "d": 1, "s": 3, "c": 4, "b": 5, "t": 6, "e": 11, "mu": 13, "tau": 15, "nu1": 12, "nu2": 14,
         "nu3": 16, "m_H": 25}
MP_GEV = 1.22089e19                      # the Planck mass energy equivalent, CODATA 2018 (scipy.constants)
G, HBAR, C = 6.6743e-11, 1.0545718176461565e-34, 299792458.0
MPC = 3.0856775814913673e22


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


def coords():
    out = [c for _, cs in BAEZ for c in cs]
    if "count25" in MUT:
        out = out[:-1]
    return out


def pdg_masses():
    """A2: the masses as the capture prints them, in MeV; '?' kept as None (NOT MEASURED)"""
    rows = {}
    for line in open(PDG, encoding="utf-8"):
        if line.startswith("#") or line.startswith("pdgid"):
            continue
        f = line.rstrip("\n").split("\t")
        rows[int(f[0])] = f[11]
    out = {}
    for k, pid in PDGID.items():
        v = rows[pid]
        out[k] = None if v == "?" else float(v)
    if "fill_nu" in MUT:
        out["nu1"] = 1e-9                                         # the mutant: an unmeasured coordinate filled
    return out


def ours():
    """A2: our position, each coordinate (value, source, status)"""
    m = pdg_masses()
    P = {}
    for k in ("u", "d", "s", "c", "b", "t", "e", "mu", "tau", "nu1", "nu2", "nu3", "m_H"):
        if m[k] is None:
            P[k] = (None, "PDG 2026 capture prints '?'", "NOT MEASURED")
        else:
            P[k] = (m[k] / 1e3 / MP_GEV, "PDG 2026 capture, %g MeV over the Planck mass" % m[k], "READ")
    P.update({"ckm_s12": (0.22501, "PDG 2024 eq. (12.28)", "READ"), "ckm_s13": (0.003732, "PDG 2024 (12.28)", "READ"),
              "ckm_s23": (0.04183, "PDG 2024 (12.28)", "READ"), "ckm_delta": (1.147, "PDG 2024 (12.28)", "READ"),
              "pmns_s2_12": (0.308, "NuFIT 6.0 Table 1, IC24, NO", "READ"),
              "pmns_s2_23": (0.470, "NuFIT 6.0 Table 1, IC24, NO", "READ; octant not settled"),
              "pmns_s2_13": (0.02215, "NuFIT 6.0 Table 1, IC24, NO", "READ"),
              "pmns_delta": (math.radians(212), "NuFIT 6.0 Table 1, IC24, NO", "READ; weakly measured"),
              "v": (246.22 / MP_GEV, "PDG 2024 electroweak review, 246.22 GeV", "READ")})
    a_hat, s2 = 1 / 127.930, 0.23129
    P["alpha_1"] = (a_hat / (1 - s2), "alpha-hat(M_Z)/c^2, PDG 2024", "computed from READ")
    P["alpha_2"] = (a_hat / s2, "alpha-hat(M_Z)/s^2, PDG 2024", "computed from READ")
    P["alpha_s"] = (0.1187, "PDG 2024 electroweak global fit", "READ (not the world average)")
    P["Lambda"] = (lambda_planck(), "Planck 2018: H0 67.4, Omega_m 0.315, flat", "computed from READ")
    return P


def rho_lambda():
    """A2: rho_Lambda c^2 in J/m^3 from Planck 2018's H0 and Omega_m, flat"""
    H0 = 67.4e3 / MPC
    return (1 - 0.315) * 3 * H0 ** 2 * C ** 2 / (8 * math.pi * G)


def lambda_planck():
    rho_P = C ** 7 / (HBAR * G ** 2)                               # the Planck energy density, J/m^3
    return rho_lambda() / rho_P


def length(x1, x2, delta):
    """A4: L = sum log2(1 + |n_i|), n_i cells between position 2 and ours"""
    L = 0.0
    for a, b, d in zip(x1, x2, delta):
        n = round((b - a) / d)
        L += (abs(n) ** 2 if "square" in MUT else math.log2(1 + abs(n)))
    return L


def r4_checks():
    """A4: R4b and R4d on random positions; R4d's integer inequality exact on a box, and symbolically"""
    rnd = random.Random(429)
    k = len(coords())
    delta = [1.0] * k
    ok_b = length([0.0] * k, [0.0] * k, delta) == 0
    ok_pos = length([0.0] * k, [0.0] * (k - 1) + [3.0], delta) > 0
    ok_d = True
    for _ in range(2000):
        p = [[rnd.randint(-50, 50) for _ in range(k)] for _ in range(3)]
        ok_d &= length(p[0], p[2], delta) <= length(p[0], p[1], delta) + length(p[1], p[2], delta) + 1e-12
    box = all((1 + abs(a + b)) <= (1 + abs(a)) * (1 + abs(b)) for a in range(-60, 61) for b in range(-60, 61))
    a, b = sp.symbols("a b", nonnegative=True)
    sym = sp.expand((1 + a) * (1 + b) - (1 + a + b)) == a * b          # |a+b| <= |a|+|b| closes the general case
    return ok_b and ok_pos, ok_d and box and sym


def face_free():
    """A5: the face's area and energy in Planck units are functions of N alone"""
    N = sp.Symbol("N", positive=True)
    lP, mP = sp.symbols("l_P m_P", positive=True)
    consts = sp.symbols("y_u y_d y_s y_c y_b y_t y_e y_mu y_tau alpha_1 alpha_2 alpha_s v m_H", positive=True)
    area = 4 * lP ** 2 * N * sp.log(2)
    if "face_alpha" in MUT:
        area = area * (1 + consts[9])                              # the mutant: a coupling in the face's area
    r0 = sp.sqrt(area / (4 * sp.pi))
    M = r0 * mP / (2 * lP)                                         # r0 = 2 G M / c^2, l_P c^2 / G = m_P
    e_over = sp.simplify(M / mP)
    ok = (sp.simplify(area / lP ** 2).free_symbols == {N} and e_over.free_symbols == {N}
          and sp.simplify(e_over - sp.sqrt(N * sp.log(2) / sp.pi) / 2) == 0)
    return ok


def g_ray():
    """A6: 2b, G -> g G, moves every m / m_P by g^(1/2), m_P = sqrt(hbar c / G)"""
    g, m, hb, c, Gs = sp.symbols("g m hbar c G", positive=True)
    ratio = (m / sp.sqrt(hb * c / (g * Gs))) / (m / sp.sqrt(hb * c / Gs))
    return sp.simplify(ratio - sp.sqrt(g)) == 0


def report():
    P = ours()
    print("A0 M's words inside 429 and 431:", words())
    print("A1 Baez's 26 counted by kind: %s = %d" % ("+".join(str(len(cs)) for _, cs in BAEZ), len(coords())))
    print("A2 our position (dimensionless; NOT MEASURED never filled):")
    for k in coords():
        v, src, st = P[k]
        print("   %-11s %-12s %-30s %s" % (k, "--" if v is None else "%.6g" % v, st, src))
    print("   rho_Lambda c^2 = %.3g J/m^3 (201: 5.25e-10)" % rho_lambda())
    ok_b, ok_d = r4_checks()
    print("A4 R4b (zero iff equal) %s; R4d (triangle, exact) %s" % (ok_b, ok_d))
    print("A5 the face in Planck units a function of N alone:", face_free())
    print("A6 2b moves every mass over m_P by g^(1/2):", g_ray())


def selftest(quiet=False):
    ok = []
    def say(s):
        if not quiet:
            print(s, flush=True)
    a0 = words(); ok.append(a0); say("A0 M's words verbatim inside 429 and 431: %s" % a0)
    a1 = len(coords()) == 26 and sum(len(cs) for _, cs in BAEZ) == 26
    ok.append(a1); say("A1 Baez's 26: 6 + 4 + 6 + 4 + 2 + 3 + 1 = 26: %s" % a1)
    P = ours()
    unk = sorted(k for k in coords() if P[k][0] is None)
    a2 = (unk == ["nu1", "nu2", "nu3"] and all(P[k][2] == "NOT MEASURED" for k in unk)
          and abs(P["t"][0] - 172.6 / MP_GEV) < 1e-25 and abs(rho_lambda() / 5.25e-10 - 1) < 0.005)
    ok.append(a2); say("A2 our position: three neutrino masses NOT MEASURED, never filled; rho_Lambda c^2 = %.3g J/m^3, "
                       "201's 5.25e-10 at three figures: %s" % (rho_lambda(), a2))
    ok_b, ok_d = r4_checks()
    a4 = ok_b and ok_d; ok.append(a4)
    say("A4 R4 on the 26: zero iff every cell equal, and the triangle inequality exact: %s" % a4)
    a5 = face_free(); ok.append(a5); say("A5 the face's area and energy in Planck units functions of N alone: %s" % a5)
    a6 = g_ray(); ok.append(a6); say("A6 2b: G -> g G moves every mass over the Planck mass by g^(1/2): %s" % a6)
    return all(ok)


def mutants():
    names = ["count25", "fill_nu", "square", "face_alpha"]
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
