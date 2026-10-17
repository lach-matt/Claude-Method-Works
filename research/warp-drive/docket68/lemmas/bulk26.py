#!/usr/bin/env python3
"""bulk26.py -- items 458-461: the bulk's universal constants weighed against the hierarchy of Baez's 26, and the
answers the other languages could not give computed in binary.  M (458): "I would consider weighing a hierarchy
principle to baez's 26, and see if any combination of them gives the universal constants of the bulk"; (459): "find the
binary solution/definition instead of dimensional languages"; (461): "weigh the bulk constants against that hierarchy
and compute the answers you are struggling to compute in binary of you cannot get a concrete answer in the other
languages".  Labels: READ (quoted), computed, deduced, placed (put by the hierarchy, not derived from an object of the
theorem).  Worked in the conversation; not verified; not seated.  2026-10-17.

  W0 (read) M's words: 458, 459, 461.
  W1 (computed) The 26 by dependence.  First order, set by nothing else among them: the three couplings, the Higgs
     field's value v, the Higgs mass and the cosmological constant (6).  Second order: the twelve masses, each v times
     that particle's coupling to the Higgs field (12).  Third order: the eight mixing numbers, CKM and PMNS, which exist
     only as the misalignment of the second-order mass matrices (8).  6 + 12 + 8 = 26.
  W2 (computed) The 26 by size.  With the Cabibbo number lam_C = sin theta_12 = 0.22501 (one of the 26) as the base,
     every scale sits at a rank n = log(x/M_Pl)/log(lam_C): the top quark at 26.1, v at 25.8, the electron at 34.5, the
     dark energy's scale rho_Lambda^(1/4) at 46.6.  Within a family the ratios sit near whole powers (u/t 7.6, c/t 3.3,
     d/b 4.6, s/b 2.6, e/tau 5.5, mu/tau 1.9; CKM theta_23 2.1, theta_13 3.8).  The neutrino mixings are large and do
     not follow; the neutrino masses are not measured.
  W3 (computed; deduced) The bulk's constants all follow from one number once the plane's relations hold.  Randall and
     Sundrum's G5 = G ell (the record's), the tuned tension sigma_RS = 3/(4 pi G ell^2) with its offset set by the
     cosmological constant (201), Lambda_5 = -6/ell^2, and the bulk's Planck energy E5 = M_Pl (l_P/ell)^(1/3).  So
     weighing the bulk is placing ell -- equivalently E5 -- in the 26's hierarchy.  The bulk U(1)'s coupling g5 and the
     plane's field term lam are the two further constants (W8).
  W4 (computed) Three routes place E5, and they meet.  The midpoint of the hierarchy's top rank, between M_Pl (rank 0)
     and v (rank 25.8): rank 12.9, E5 = sqrt(v M_Pl) = 5.48e10 GeV.  The integer rank 13: E5 = M_Pl lam_C^13 = 4.63e10
     GeV.  The Higgs quartic's zero (ell_higgs H3, the record's own three-loop run): 3.68e10 GeV, rank 13.15.  The
     spread is a quarter of one rank.
  W5 (computed) The binary definition.  Counted in halvings of the Planck energy, E5 = 2^-k M_Pl, the three routes give
     k = 27.7, 28.0 and 28.3: all within half a bit of k = 28.  So, in binary, E5 = 2^-28 M_Pl = 4.55e10 GeV and
     ell = 2^84 l_P = 0.313 nm, the bulk's length 84 bits above the Planck length.  This is the placement the hierarchy
     gives, not a derivation from an object of the theorem (384: the theorem holds no object forcing it).
  W6 (computed) Against the record's window.  ell = 0.313 nm lies inside 13.964 um (B6P) and inside the Higgs tie's
     band (0.024 to 9.6 nm over the top mass's one sigma).  ell_higgs H5's floor (E_I >= E5, the theorem's corridors not
     seeding the Higgs vacuum's decay) holds for a top mass at or below 172.51 GeV, 0.06 GeV under the run's central
     172.57.  At the edge, as the Higgs route itself is.
  W7 (computed) What the placement sets.  G5 = G ell; E5 = 4.55e10 GeV; sigma^(1/4) = (3/(4 pi))^(1/4)
     (M_Pl/ell)^(1/2); Lambda_5 = -6/ell^2; the bulk's length scale against the de Sitter length L = sqrt(3/Lambda):
     log2(L/ell) bits.  The table-top correction to Newton's law at 52 um, (2/3) ell^2/r^2, is 2.4e-11.
  W8 (computed; deduced) The U(1), under 459 (446's dark U(1) stale under the 26): the one U(1) among the 26 is
     hypercharge, coupling g' = e/cos theta_W from the 26's alpha and weak mixing.  The bulk field's four-dimensional
     coupling runs (u1_bulk U4): 1/g'^2 = (lam + s ell ln(L/ell))/g5^2.  So g5^2/ell = g'^2 (lam/ell + s ln(L/ell)) --
     one relation for two constants.  lam >= 0 (no ghost) needs g5^2/ell >= s g'^2 ln(L/ell); the corridor's throat
     needs lam >= lam_min (P1, corridor_p1).  The hierarchy does not split g5 from lam: which rank g5^2/ell occupies is
     the open question it leaves.  [W11 decides it from the measured Coulomb law: no binary needed.]
  W9 (READ; computed) The inner horizon, in bits.  Ansorg and Hennig (arXiv:0810.3998; PRL 102, 221102), READ: "the
     remarkable universal relation (8 pi J)^2 + (4 pi Q^2)^2 = A+ A-" for axisymmetric stationary black holes with
     surrounding matter in four-dimensional Einstein-Maxwell theory.  Static (J = 0), in bits N = A/(4 ln2 l_P^2):
     N+ N- = N_Q^2, N_Q = pi Q^2/(ln2 l_P^2).  So the inner horizon carries N- = N_Q^2/N+ bits, and r-/r+ = (Q/r+)^2.
     For P2's lam = 64 member (Q/r+ = mu-tilde = 0.42, R4 = 1.79 ell): r- = 0.316 ell, N-/N+ = 0.031.
  W10 (computed; estimate) Against P3's computed interior (BOUNCE-RESEARCH section 24): fitting the plane's Killing norm
     to Reissner-Nordstrom with r+ fixed, the inferred r- rises as the computation deepens -- 0.13, 0.18, 0.19, 0.22,
     0.21, 0.25, 0.27 ell from R = 1.57 to 0.775 ell -- toward W9's 0.316 ell.  W9 holds on the plane to the extent the
     plane is four-dimensional Einstein-Maxwell; the bulk's Weyl term is the difference (P2: 15% at R4 ~ 2 ell).
  W11 (READ; computed; estimate) The g5/lam split, by the measured Coulomb law.  A bulk share runs the U(1)'s coupling
     (u1_bulk U4): the flux through a sphere of radius r falls by s ell/(lam + s ell ln(r/ell)) per e-fold of r, where
     Gauss's law keeps it fixed.  Goldhaber and Nieto (0809.1003, READ): Williams, Faller and Hill's experiment "remains
     the landmark test of Coulomb's Law.  Their limit of [reduced Compton wavelength] >~ 2 x 10^7 m" stands, and for
     the Proca deviation "the first non-Coulombic term in E is of order (mu r)^2".  Matching the two at the apparatus
     scale r = 1 m (an estimate of order, not a fit): s ell/lam <= (r/2e7 m)^2 = 2.5e-15, so lam/ell >= 8.0e14, about
     2^49.5, and g5^2/ell = g'^2 (lam/ell + s ln(L/ell)) >= 1.0e14.  The bulk's kinetic term for the U(1) is at most
     ~1e-15 of the plane's: the field lives on the plane, Kaus and Reall's limit (corridor_p1 P7: lam -> infinity with
     lam c^2 held).  g5 is then not a constant of the bulk -- it drops out with g5^2/lam = g'^2 held -- and 446's bulk
     U(1) is the plane's own.
  W12 (computed) lam >= lam_min: yes, by 11.4 decades over the largest lam_min P1 computed (3.4e3 ell at L1 = 10 ell).
     The extremal throat exists on the plane for every hole P1 computed.
  W13 (READ; computed) Electric charge does not hold.  The 26 carry the electron, charged under the U(1).  At P2's
     member's horizon (mu-tilde 0.42, R4 = 1.79 ell, ell = 2^84 l_P) the field, |F| = e|E| = Q/(2 r+^2) (Maldacena
     2004.06084 (2), READ form), is 5.9e17 times Schwinger's m_e^2: pair creation unsuppressed (exponent
     pi m_e^2/|F| = 5e-18).  Gibbons (Commun. Math. Phys. 44, 245 (1975), abstract, READ): "For large black holes (more
     massive than 10^17 g) the process is shown to be governed by a Schwinger type formula."  So the hole of section
     14, electrically charged, discharges: in binary 0, magnitude log10 17.8.
  W14 (READ; computed) Magnetic charge holds.  Maldacena (2004.06084, READ): "Extremal magnetic black holes are more
     stable than their electric counterparts, since unit charge magnetic monopoles are much heavier than electrically
     charged particles, and are thus harder to pair create.  In addition, an electrically charged black hole can be
     neutralized in conductive medium, while a magnetically charged one cannot be neutralized with ordinary matter."
     The 26 hold no magnetic charge lighter than a unit magnetic hole, M l_p ~ sqrt(pi)/e (his (3) at Q = 1), so the
     pair-creation exponent pi Q (M l_p)^2 (his (13)) is pi^2 Q/e^2 = 2.7e26 at the member's Q = r_Q e/(sqrt(pi) l_p)
     = 2.5e24: in binary 1, magnitude log10 26.4.  Its horizon field is 2.4e7 m_W^2, so the electroweak symmetry is
     restored there and only hypercharge field survives (his (6)); the corona reaches r_w = sqrt(Q/2)/m_W = 2.7 um (his
     (10)-(11)), Q under his Q_ew = 3.4e32.  Deduced: on the plane the duality F -> *F leaves the stress tensor, so the
     geometry, unchanged; P1-P3's computed holes and W9's r- carry over with the charge magnetic (cos theta_W
     corrections near the horizon, his section 2.3, aside).
  W15 (deduced) P3's wall is the method's, not the geometry's.  It stands at R = 0.78-0.95 ell (section 24), above W9's
     r- = 0.316 ell, in the region between the horizons that Reissner-Nordstrom holds regular; there P3's metric
     function A diverged while the Killing norm and the areal radius, both invariants, stayed finite (g_tt = 0.70),
     and both candidates section 24 leaves -- the conditioning of a global solve of an initial-value region, and a
     growing mode of that solve -- are the method's.  So, in binary: is the wall a horizon or a singularity of the
     geometry?  0.  W9's value does not by itself move it: section 24's two-horizon reference at s- = -2.0 already put
     the second horizon near R ~ 0.4 ell (estimate) and stopped short of 0.95 ell.  What it calls for is a march in s
     as an evolution with constraint-preserving rows on the plane and axis, which section 24 records the elliptic rows
     are not.

python3 bulk26.py [--selftest | --mutants]
"""
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
WORDS = ("weighing a hierarchy principle to baez's 26", "find the binary solution/definition instead of dimensional "
         "languages", "weigh the bulk constants against that hierarchy")
MUT = set()

# the 26 as the record holds them (address26 A2): GeV, PDG 2026 capture and the reviews it names
MPL = 1.220890e19                       # Planck mass, GeV (CODATA 2018)
LP = 1.616255e-35                       # Planck length, m
HBARC = 1.973269804e-16                 # GeV m
MASS = dict(u=2.16e-3, d=4.7e-3, s=0.0929, c=1.273, b=4.186, t=172.6, e=0.510998951e-3, mu=0.105658376,
            tau=1.77693, H=125.13)
V = 246.22
ALPHA_HAT = 1 / 127.930
S2W = 0.23129
ALPHA_S = 0.1187
CKM = dict(s12=0.22501, s13=0.003732, s23=0.04183, delta=1.147)
PMNS = dict(s2_12=0.308, s2_23=0.470, s2_13=0.02215, delta_deg=212)
RHO_L_JM3 = 5.25e-10                    # rho_Lambda c^2, J/m^3
GEV_J = 1.602176634e-10
LAM_C = CKM["s12"]
E_I = {172.57: 3.68e10, 172.86: 1.45e10, 172.28: 1.06e11}   # ell_higgs H3: the quartic's zero by the top mass
B6P_ELL_MAX = 13.964e-6                 # m
MU_T, R4_P2 = 0.42, 1.79                # P2's lam = 64 member (section 22)
RFIT = [(1.57, 0.13), (1.38, 0.18), (1.20, 0.19), (1.02, 0.22), (0.94, 0.21), (0.86, 0.25), (0.775, 0.27)]
ALPHA0 = 1 / 137.035999                 # the fine-structure constant at zero momentum (CODATA)
M_E, M_W = 0.51099895e-3, 80.369        # GeV
LAMBDA_C_PROCA = 2e7                    # m: Williams, Faller and Hill's reduced Compton wavelength floor (READ)
R_APP = 1.0                             # m: the apparatus scale the floor is matched at (estimate)
LAM_MIN_P1 = 3.4e3                      # ell: P1's largest computed lam_min (L1 = 10 ell)
WALL = (0.78, 0.95)                     # ell: P3's wall (section 24)


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def rank(x):
    """the rank of a scale x (GeV) under the Cabibbo base, from the Planck mass"""
    base = LAM_C if "base_2" not in MUT else 0.5
    return math.log(x / MPL) / math.log(base)


def rank_ratio(r):
    return math.log(r) / math.log(LAM_C)


def rho_lambda_gev4():
    return RHO_L_JM3 / GEV_J * HBARC**3


def orders():
    first = ["g1", "g2", "g3", "v", "m_H", "Lambda"]
    second = ["u", "d", "s", "c", "b", "t", "e", "mu", "tau", "nu1", "nu2", "nu3"]
    third = ["CKM_12", "CKM_13", "CKM_23", "CKM_delta", "PMNS_12", "PMNS_13", "PMNS_23", "PMNS_delta"]
    if "drop_mixing" in MUT:
        third = third[:4]
    return first, second, third


def placements():
    n_v = rank(V)
    e_mid = math.sqrt(V * MPL)
    e_int = MPL * LAM_C**13
    e_hig = E_I[172.57]
    out = {}
    for name, e in (("midpoint", e_mid), ("integer 13", e_int), ("Higgs zero", e_hig)):
        out[name] = dict(E5=e, rank=rank(e), k=math.log2(MPL / e), ell=LP * (MPL / e)**3)
    return n_v, out


def binary():
    n_v, P = placements()
    ks = [p["k"] for p in P.values()]
    k = round(sum(ks) / len(ks))
    E5 = MPL * 2.0**-k
    ell = LP * 2.0**(3 * k)
    return dict(k=k, spread=max(abs(x - k) for x in ks), E5=E5, ell=ell, bits=3 * k)


def floor_top_mass(E5):
    """the top mass below which E_I >= E5 (log-linear in the run's three points)"""
    m0, m1 = 172.57, 172.28
    slope = (math.log(E_I[m1]) - math.log(E_I[m0])) / (m1 - m0)
    return m0 + (math.log(E5) - math.log(E_I[m0])) / slope


def setting(ell):
    rho = rho_lambda_gev4()
    lam4 = 8 * math.pi * rho / MPL**2                       # GeV^2
    L = math.sqrt(3 / lam4) * HBARC                          # m
    ell_gev = ell / HBARC
    sig14 = (3 / (4 * math.pi))**0.25 * math.sqrt(MPL / ell_gev)
    return dict(E5=MPL * (LP / ell)**(1 / 3), sigma14=sig14, Lambda5=-6 / ell**2, L=L, bitsL=math.log2(L / ell),
                lnL=math.log(L / ell), tabletop=(2 / 3) * (ell / 52e-6)**2)


def u1(ell, s=2):
    """the 26's U(1): g'^2 = 4 pi alpha_hat / cos^2 theta_W; g5^2/ell = g'^2 (lam/ell + s ln(L/ell))"""
    gp2 = 4 * math.pi * ALPHA_HAT / (1 - S2W)
    st = setting(ell)
    return dict(gp2=gp2, g5sq_over_ell_at_lam0=gp2 * s * st["lnL"], lnL=st["lnL"])


def inner_horizon(mu_t=MU_T, r4=R4_P2):
    """Ansorg-Hennig at J = 0: A+ A- = (4 pi Q^2)^2, so r-/r+ = (Q/r+)^2, in bits N- = N_Q^2/N+"""
    k = 1 if "area_sum" not in MUT else 0.5
    ratio = mu_t**(2 * k)
    return dict(r_minus=ratio * r4, ratio=ratio, Nratio=ratio**2)


def coulomb_floor(ell, s=2):
    """W11: the least lam/ell for which the bulk share's running stays under the Coulomb test's (r/lam_C)^2"""
    d = (R_APP / LAMBDA_C_PROCA)**(2 if "flux_linear" not in MUT else 1)
    lam = s / d - s * math.log(R_APP / ell)
    gp2 = u1(ell, s)["gp2"]
    return dict(dev=d, lam=lam, bits=math.log2(lam), g5sq_over_ell=gp2 * (lam + s * math.log(setting(ell)["L"] / ell)),
                margin=math.log10(lam / LAM_MIN_P1))


def charge_on_hole(k, mu_t=MU_T, r4=R4_P2):
    """W13-W14: the member's horizon field in Planck units, |F| = Q/(2 r+^2), Q = r_Q e/sqrt(pi) (Maldacena (2)-(3))"""
    e = math.sqrt(4 * math.pi * ALPHA0)
    rp = r4 * 2.0**(3 * k)                                   # l_p
    Q = mu_t * rp * e / math.sqrt(math.pi)
    F = Q / (2 * rp**2) * MPL**2                             # GeV^2
    schwinger = F / M_E**2
    S = math.pi**2 * Q / e**2 if "no_pair_exponent" not in MUT else 0.0
    return dict(Q=Q, sqrtF=math.sqrt(F), schwinger=schwinger, electric=schwinger < 1, S=S, magnetic=S > 1,
                ew=F / M_W**2, Qew=e**2 / (2 * math.pi) * (MPL / M_W)**2,
                r_w=math.sqrt(Q / 2) / M_W * HBARC)


def report():
    first, second, third = orders()
    print("W1 the 26 by dependence: %d first, %d second, %d third = %d" % (len(first), len(second), len(third),
                                                                      len(first) + len(second) + len(third)))
    print("W2 ranks from the Planck mass, base lam_C = %.5f:" % LAM_C)
    for nm, x in sorted(list(MASS.items()) + [("v", V), ("rho_L^1/4", rho_lambda_gev4()**0.25)], key=lambda t: -t[1]):
        print("     %-10s %10.4g GeV  rank %6.2f" % (nm, x, rank(x)))
    for nm, r in (("u/t", MASS["u"] / MASS["t"]), ("c/t", MASS["c"] / MASS["t"]), ("d/b", MASS["d"] / MASS["b"]),
                  ("s/b", MASS["s"] / MASS["b"]), ("e/tau", MASS["e"] / MASS["tau"]), ("mu/tau", MASS["mu"] / MASS["tau"]),
                  ("CKM 23", CKM["s23"]), ("CKM 13", CKM["s13"]), ("PMNS 12", math.sqrt(PMNS["s2_12"])),
                  ("PMNS 13", math.sqrt(PMNS["s2_13"]))):
        print("     %-8s %9.4g  rank %5.2f" % (nm, r, rank_ratio(r)))
    n_v, P = placements()
    print("W4 the bulk's E5 placed (v at rank %.2f):" % n_v)
    for nm, p in P.items():
        print("     %-11s E5 %.3g GeV  rank %.2f  k %.2f halvings  ell %.3g nm" % (nm, p["E5"], p["rank"], p["k"],
                                                                                  p["ell"] * 1e9))
    b = binary()
    print("W5 binary: k = %d (all within %.2f bit): E5 = 2^-%d M_Pl = %.4g GeV, ell = 2^%d l_P = %.4g nm" % (
        b["k"], b["spread"], b["k"], b["E5"], b["bits"], b["ell"] * 1e9))
    print("W6 window: ell < 13.964 um %s; Higgs-vacuum floor holds for m_t <= %.2f GeV" % (b["ell"] < B6P_ELL_MAX,
                                                                                      floor_top_mass(b["E5"])))
    st = setting(b["ell"])
    print("W7 sets: E5 %.4g GeV, sigma^1/4 %.4g GeV, Lambda_5 %.3g m^-2, log2(L/ell) %.1f bits, table-top %.2g" % (
        st["E5"], st["sigma14"], st["Lambda5"], st["bitsL"], st["tabletop"]))
    q = u1(b["ell"])
    print("W8 U(1): g'^2 = %.4f; lam >= 0 needs g5^2/ell >= %.3f (s = 2, ln(L/ell) = %.1f)" % (
        q["gp2"], q["g5sq_over_ell_at_lam0"], q["lnL"]))
    ih = inner_horizon()
    print("W9 inner horizon in bits: N-/N+ = %.4f, r-/r+ = %.4f, r- = %.3f ell" % (ih["Nratio"], ih["ratio"],
                                                                                ih["r_minus"]))
    print("W10 P3's inferred r- by depth:", ", ".join("%.2f at R %.3g" % (r, R) for R, r in RFIT))
    cf = coulomb_floor(b["ell"])
    print("W11 Coulomb: s ell/lam <= %.2g, so lam/ell >= %.3g (2^%.1f), g5^2/ell >= %.3g" % (
        cf["dev"], cf["lam"], cf["bits"], cf["g5sq_over_ell"]))
    print("W12 lam >= lam_min: %s, by %.1f decades over %.2g ell" % (cf["lam"] > LAM_MIN_P1, cf["margin"], LAM_MIN_P1))
    ch = charge_on_hole(b["k"])
    print("W13 electric: Q %.3g, sqrt|F| %.3g GeV, |F|/m_e^2 %.3g -- holds: %d (log10 %.1f)" % (
        ch["Q"], ch["sqrtF"], ch["schwinger"], ch["electric"], math.log10(ch["schwinger"])))
    print("W14 magnetic: pair exponent %.3g -- holds: %d (log10 %.1f); |F|/m_W^2 %.3g, Q_ew %.3g, r_w %.3g um" % (
        ch["S"], ch["magnetic"], math.log10(ch["S"]), ch["ew"], ch["Qew"], ch["r_w"] * 1e6))
    print("W15 the wall at R %.2f-%.2f ell lies above r- %.3f ell: %s" % (WALL[0], WALL[1], ih["r_minus"],
                                                                          WALL[0] > ih["r_minus"]))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("W0 words: %s" % r)
    f, s_, t = orders()
    r = (len(f), len(s_), len(t)) == (6, 12, 8); ok.append(r); say("W1 6 + 12 + 8: %s" % r)
    r = abs(rank(V) - 25.77) < 0.02 and abs(rank(MASS["t"]) - 26.0) < 0.15 and abs(rank_ratio(MASS["u"] / MASS["t"]) - 7.57) < 0.02
    ok.append(r); say("W2 ranks: v %.2f, t %.2f, u/t %.2f: %s" % (rank(V), rank(MASS["t"]), rank_ratio(MASS["u"] / MASS["t"]), r))
    st = setting(1e-9)
    r = abs(st["E5"] / (MPL * (LP / 1e-9)**(1 / 3)) - 1) < 1e-12 and st["Lambda5"] == -6e18
    ok.append(r); say("W3 E5 and Lambda_5 from ell: %s" % r)
    n_v, P = placements()
    spread = max(p["rank"] for p in P.values()) - min(p["rank"] for p in P.values())
    r = spread < 0.3 and abs(P["integer 13"]["rank"] - 13) < 1e-9; ok.append(r)
    say("W4 three routes within %.2f rank: %s" % (spread, r))
    b = binary()
    r = b["k"] == 28 and b["spread"] < 0.5 and abs(b["ell"] * 1e9 - 0.3126) < 0.001; ok.append(r)
    say("W5 binary k = %d, ell %.4f nm: %s" % (b["k"], b["ell"] * 1e9, r))
    mt = floor_top_mass(b["E5"])
    r = b["ell"] < B6P_ELL_MAX and 172.4 < mt < 172.57; ok.append(r)
    say("W6 window and the floor's top mass %.2f GeV: %s" % (mt, r))
    st = setting(b["ell"])
    r = abs(st["E5"] / b["E5"] - 1) < 1e-9 and 115 < st["bitsL"] < 122; ok.append(r)
    say("W7 consistent E5; log2(L/ell) %.1f: %s" % (st["bitsL"], r))
    q = u1(b["ell"])
    r = 0.12 < q["gp2"] < 0.14 and q["g5sq_over_ell_at_lam0"] > 0; ok.append(r)
    say("W8 g'^2 %.4f: %s" % (q["gp2"], r))
    ih = inner_horizon(0.6, 1.0)
    r = abs(ih["ratio"] - 0.36) < 1e-12 and abs(inner_horizon()["r_minus"] - 0.42**2 * 1.79) < 1e-12; ok.append(r)
    say("W9 Reissner-Nordstrom r-/r+ = (Q/r+)^2 reproduced: %s" % r)
    rising = all(RFIT[i + 1][1] >= RFIT[i][1] - 0.011 for i in range(len(RFIT) - 1))
    r = rising and RFIT[-1][1] < inner_horizon()["r_minus"]; ok.append(r)
    say("W10 P3's inferred r- rises toward W9's: %s" % r)
    cf = coulomb_floor(b["ell"])
    r = abs(cf["dev"] - 2.5e-15) < 1e-17 and 7.9e14 < cf["lam"] < 8.1e14 and 1.0e14 < cf["g5sq_over_ell"] < 1.05e14
    ok.append(r); say("W11 Coulomb floor lam/ell %.3g, g5^2/ell %.3g: %s" % (cf["lam"], cf["g5sq_over_ell"], r))
    r = cf["lam"] > LAM_MIN_P1 and 11.3 < cf["margin"] < 11.5; ok.append(r)
    say("W12 lam >= lam_min by %.2f decades: %s" % (cf["margin"], r))
    ch = charge_on_hole(b["k"])
    r = (not ch["electric"]) and 5.8e17 < ch["schwinger"] < 6.0e17 and 2.4e24 < ch["Q"] < 2.6e24; ok.append(r)
    say("W13 electric discharges, |F|/m_e^2 %.3g: %s" % (ch["schwinger"], r))
    r = ch["magnetic"] and 26.3 < math.log10(ch["S"]) < 26.5 and ch["ew"] > 1 and ch["Q"] < ch["Qew"]; ok.append(r)
    say("W14 magnetic holds, exponent %.3g, EW restored %.3g: %s" % (ch["S"], ch["ew"], r))
    r = WALL[0] > inner_horizon()["r_minus"] and WALL[1] < R4_P2; ok.append(r)
    say("W15 the wall between the horizons: %s" % r)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    names = ["base_2", "drop_mixing", "area_sum", "flux_linear", "no_pair_exponent"]
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        bad = not selftest(quiet=True)
        caught += bad
        print("mutant %-12s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
