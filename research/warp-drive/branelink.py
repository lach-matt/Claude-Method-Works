#!/usr/bin/env python3
r"""
branelink.py -- O6 AND O7, THE BRANE LEFTOVERS; AND S5's FOUR FIGURES, REFUSED.

DOCKET 62's O6/O7 pass proposed closing both rows and left every figure in
/tmp/o6o7.  The ruling kept the finds, corrected the decisive number by a factor
of four, refused both closures and refused the new row R-1.  This file seats
exactly that.

    python3 branelink.py             the reading
    python3 branelink.py --selftest  stdlib decimal + sympy; a few seconds

===============================================================================
1. O6 -- THE BRANE-BULK TRANSDUCER.  OPEN, NARROWED.  NOT CLOSED.
===============================================================================

THE FIND, AND IT STANDS.  O6's line "neither GKLP paper states a coupling
constant, a source model or an emission rate" is true of the two papers read and
false of the literature.  Kabat & Nomura, arXiv:2309.05759 -- the third paper of
the same group -- state the coupling (eq. 68, g_AB = eta_AB + (2/Mbar5^{3/2})
h_AB, about a flat bulk; eq. 70, the brane stress-tensor coupling, introduced
with "We assume"), the source term, the vertex (eq. 71) and the normalisation that
fixes it (eqs. 72-73, Mbar4 = (2 pi r)^{1/2} Mbar5^{3/2}, where KN's r is the
effective radius gamma R of an S^1 of radius R).  The zero-mode coupling 1/Mbar4
is not a free parameter: G fixes it and r drops out.  O6's stated cause of death
is REFUTED, and that is a NARROWING, not an answer.  Also kept, on the
bulk-graviton branch only (on the brane-confined branch below it bounds
nothing): GLP's potential for a moving brane puts the Eot-Wash 38.6 um null on
r = gamma L/(2 pi), so on gamma L (<= 242.5 um), not on L.  (The O6/O7 pass
recorded Kabat & Nomura and GLP as READ at source; the Eot-Wash figure it did
not read there -- see below.)
    CORRECTED (DOCKET 67).  (a) "The coupling is not a free parameter" is true of
    the zero mode only: 1/Mbar5^{3/2} = (2 pi r)^{1/2}/Mbar4 and every non-zero-
    mode or winding amplitude, eq. 76's 1/(pi r Mbar4)^2 among them, carry the
    unmeasured r.  (b) "The source model" was KN's quantum Dirac (or scalar)
    stress tensor inside one-loop self-energies, not an emitter: KN give no
    classical emission model and no rate (as conceded below), and the rod is
    this file's own 4D quadrupole computation.  (c) Eq. 72 is Greene-Levin-
    Parikh's, derived for a boost-like brane; KN "take this relation to hold in
    general", i.e. ASSUME it for a tilt-like one.  (d) This said "the PRODUCT
    gamma L" with no branch condition; the bounded quantity is r = gamma L/(2 pi)
    (the code uses r), and gamma L is the boost-like case of KN's r.  (e) The
    tree's "GLP eq. (39)" is an unverified equation number: in GKLP 2206.13590
    eq. (39) is the GW170817 bound, and the two labels may have been confused.
    (f) "All READ at source by the O6/O7 pass" was wrong for Lee et al.: that
    pass's own source list marks it "Obtained by web search; the PDF was not
    opened this pass", and another pass of the session read it at source.  The
    value, 38.6 um, is right.

THE DECISIVE NUMBER, CORRECTED.  A rod spinning at Omega radiates at omega_GW =
2 Omega -- proved below by the period of its own quadrupole.  The pass's script
used Omega.  At the pass's own design point (1000 t, 100 m, Omega = 100 rad/s,
LIGO-class 1e-23 receiver, Proxima span) the sky-rms strain is h = 4.3359e-48 and the
bulk channel carries 1.5347e-27 bits/s per watt of GW power -- COMPUTED here --
against the reported 8.6717e-48 and 6.1389e-27, exactly 2x and 4x.  Those two are
WITHDRAWN, kept as computed values so the correction names what it corrects.  The
direction survives: an EM link of the same hardware scale (100 m dishes both
ends, 1 GHz) beats it by ~26.6 orders.

WHY IT DOES NOT CLOSE.  (1) The closing premise -- the single-mode capacity
ceiling sqrt(pi P/(3 hbar))/ln 2 is "field-blind" -- is NOT-FOUND by the pass's
own tagging (Pendry 1983, Bekenstein & Schiffer not read), and assuming its
functional form for a carrier with gamma > 1 on a moving brane in a 5D bulk is
failure mode (4).  CORRECTED (DOCKET 67), what the form needs, re-derived with
the sources still unread: one unidirectional transverse mode, energy from the
band bottom, a monotone dispersion (the "field-blind" clause), and an ideal
noiseless receiver, which "capacity ceiling" assumes silently -- so beside a
LIGO-class receiver it bounds a rate and does not estimate one.  A boost
leaves S_dot^2/P unchanged for a massless unidirectional flux; the massive-
carrier boost was not computed; N modes at total P carry sqrt(N) times the
single-mode ceiling, so it does not carry to a bulk carrier unless the modes
are counted.  (2) The closure runs through O7's untested B = 0.  (3) THE
DICHOTOMY NOBODY STATED:
    graviton IS a bulk degree of freedom  -> the transducer exists (LIGO is an
        operating read end; the strain below is the 4D flux formula, which on
        this branch counts only the massless 4D zero mode -- a NAMED, untested
        hypothesis), GW170817 binds beta, the saving is <= 93.8 ns AT
        THE UNTESTED B = 0 (reason (2): that figure is O7's, evaluated where B
        has never been measured), the row is settled;
    graviton is NOT (brane-confined)      -> GW170817 bounds nothing about beta,
        the LIGO transducer does not exist, and the bulk scalar's coupling
        carries a free Yukawa lambda (Kabat & Nomura eq. 41): no rate.  The row
        reverts to where it was.
Both branches are unfavourable to the route; only one is a closure.  SETTLED
CONDITIONALLY, which is narrowed.  Still conceded: no moving-brane emission rate
is in print, and the non-zero-winding amplitude has never been computed.

===============================================================================
2. O7 -- OUR OWN BOOST.  OPEN, NARROWED.  NOT CLOSED.
===============================================================================

THE ARITHMETIC, AT 50 DIGITS, NEVER AS A SUBTRACTION AGAINST 1 + d.  With
d = gamma - 1 <= 7.0e-16 (GW170817, manyc.py's seated bound -- 1710.05834
bounds (v_GW - v_EM)/v_EM, read here with v_EM = c, and derives the +7e-16 edge
assuming the GW peak and the first photons were emitted simultaneously, from
one event on one line of sight at D = 26 Mpc; GKLM eq. (38) identifies
Delta c/c = gamma - 1 for a test brane, untilted, in flat M4 x S1, with light
confined to the brane at c, seen from B = 0):
    beta = sqrt(d(2+d))/(1+d) = 3.74165738677e-08,  1/beta = 26726124.1912,
    brane speed 11.2172066497 m/s,  Proxima light time 134009348.4 s = 4.2465 yr
    EXACTLY (a light year is c times a Julian year), Delta_tau = T d/(1+d) =
    93.80654 ns, fraction 7.0e-16.  "EXACTLY" is arithmetic on the seated span:
    as physics the span carries about four figures (Gaia DR3's formal parallax
    sigma is 6.5e-5 relative, at epoch J2016.0).  CORRECTED (DOCKET 67): the
    edge was quoted with no emission or line-of-sight condition.  Under the
    source's own exotic -100 s emission window it is +3.80e-14, giving
    beta <= 2.757e-7 and a B = 0 saving of 5.09 us (computed); a tilt-like
    brane can have a direction with no excess (Polychronakos 2210.11497
    eq. 5.3), where one event need not bound beta.  The ruling's ten-digit 134009341.889 s,
    4.246499794 yr and 93.8065393226 ns are the same arithmetic on the span
    rounded to 4.017499e16 m; they reproduce exactly from that input and differ
    from the seated span's figures by 5e-8, which is the rounding, not the sum.
The pass's double-precision fault is REAL and is reproduced here as a control:
1 - 1/(1+d)^2 in floats gives beta = 3.650024e-08 and 89.2682 ns -- d is three
ulps -- and neither may be quoted.  W7's 1/beta = 2.6726124e7 is vindicated to
every printed digit.  PROVENANCE, CORRECTED: the 94 ns is GW170817's 7e-16, NOT
the CMB dipole; the dipole's Gamma - 1 = 7.6161e-07 is a candidate for the
receiver's B and enters only through the anisotropy.  CORRECTED (DOCKET 67):
this called it "the RECEIVER's B".  The dipole velocity is the Solar System
barycentre's, a velocity only under the kinematic reading of the dipole, and
Earth's annual motion spreads the receiver's Gamma - 1 over 6.456e-07 ..
8.860e-07 (computed); the five figures come from the two-figure 3.7e5 m/s
(Planck's 369.82 km/s, as restated, gives 7.6087e-07).

WHY IT DOES NOT CLOSE.  GW170817 bounds BETA, the brane's speed through S^1.  O7
asks about B, Earth's velocity relative to the preferred brane frame, and
ledger.py's own answering condition is a measurement of B.  The pass argued that
beta and B are orthogonal degrees of freedom and then closed on beta.  B is not
measured.  The escape is priced (GKLP eq. (22) extremised -- GW170817's
propagation taken exactly antiparallel to Earth -> Proxima -- g -> 1, as the
pass read it): B >= 0.999387630 is the floor for one second over the Proxima
span, and B >= 0.99999993 for half the light time on the gamma -> 1
linearisation.  UNTESTED, not excluded.  And the bound is CONDITIONAL on the
graviton being a bulk degree of freedom -- GKLM hedge in the sentence the pass
quotes ("if we entertain the possibility that these are bulk degrees of
freedom"); if gravity is brane-confined, Delta c/c = 0 for it at tree level.
    CORRECTED (DOCKET 67).  (a) Both prices said "buys", a necessary floor
    stated as sufficient.  On the real sky AT2017gfo and Proxima are 41.5 deg
    apart; with the boost direction optimised -- its fast axis about 41.5 deg
    off the Proxima line -- one second costs B >= 0.9994645711 (computed).
    (b) The linearisation fails at T/2, where gamma - 1 = 1.87e-8 against
    1 - B = 7.5e-8: the exact saving at 0.99999993 is 0.400 T and the exact
    threshold 0.999999935193 (computed).  (c) This said "Delta c/c = 0
    identically"; GKLM say only that brane-localized matter "would presumably
    respect" the worldvolume Lorentz symmetry, and Kabat & Nomura show bulk loops
    with non-zero winding induce UV-finite Lorentz-violating brane terms -- a
    discrepancy of wording, far too small to move the dichotomy.

REFUSED: the new row R-1.  It holds exactly the unmeasured B that O7 was opened
to hold; opening it while retiring O7 renames the question so the closed count
rises -- the mirror of failure mode (5).

RESTATED O7: beta <= 3.74e-08 conditional on a bulk graviton, so one of the
row's two unknowns is fixed and the saving at B = 0 is 93.81 ns over 4.2465
years.  What remains is B, with the escape priced and the experiment named: a
DIRECTIONAL multi-messenger GW/EM arrival-time survey, which has N = 1 event.
AN HONEST NULL, ALSO RECORDED: the loop-induced SME route (Kabat & Nomura eqs.
76-77), evaluated at r = 38.6 um and beta = 1, gives |c| = 6.37e-64 against a
1e-21 laboratory level -- 42 orders short, a real measurement that does not bite
there.  CORRECTED (DOCKET 67): this said "at the maximal r ... |c| <= 6.37e-64".
(a) |c| goes as beta^2/r^2 and Eot-Wash bounds r from above, so 38.6 um gives
the SMALLEST |c| over the allowed r; at beta = 1 the 1e-21 is reached only for
r <= 3.08e-26 m, which Eot-Wash does not exclude.  (b) Eq. 77's I_grav =
-zeta(3)/4 is stated for b^2 ~ 0 and m ~ 0.  beta = 1 lies outside it and
outside the paper's b^2 in (0,1), where |I_grav| grows with b^2, so 6.37e-64 is
no bound as beta -> 1; and m = m_e gives pi m r = 3.14e8, which suppresses
|I_grav| by about 16 orders.  This file's own r <= 38.6 um/gamma also excludes
beta = 1 at r = 38.6 um.  On the bulk branch's beta <= 3.74e-8, where b^2 ~ 0
holds, the null is 57 orders.  (c) The 1e-21 is Dreissen et al.'s abstract
"level": their Table 1 gives 1-sigma values 3.9-9.3e-21 on four anisotropic
Sun-frame components of c' = c + k/2, against which this file sets the
isotropic scalar c_00; the projection needs the unmeasured B.

===============================================================================
3. S5 -- THE FOUR FIGURES ARE NOT SEATED
===============================================================================

The O6/O7 pass "re-derived" S5's four missing figures.  It did not: its script
hard-codes one seed value, inverts the channel law to get N, reports a round-trip
residual of 0 -- which is A(N(A)) = A, true for ANY A, proved below symbolically
-- divides once for E, and uses a separately hard-coded mass for Mc^2.
"Mutually consistent to the last printed digit" reads as corroboration and is
not.  NOT MEASURED.  NONE OF THE FOUR APPEARS IN THIS FILE, deliberately, so a
grep for them still finds only ledger.py's note about their absence.  S5 stays
OPEN and DOCKET 56 still owes the instrument that computes N from a
specification.
"""

import math
import sys
from decimal import Decimal, getcontext

import achievable
import foliation
import higgs
import manyc

# ---------------------------------------------------------------------------
# Constants ASKED of seated modules, never retyped.
# ---------------------------------------------------------------------------
C = foliation.C_LIGHT
G = foliation.G_NEWTON
HBAR = achievable.HBAR
L_PROXIMA = foliation.proxima_span_m()
YR = manyc.YR                                   # Julian year, s
D_GW = manyc.GW170817_BOUND_HI                  # (v_GW - v_EM)/v_EM <= 7e-16, READ there
#: v_EM = c is GKLM's "light travels on the brane with speed c".  The edge is
#: 1710.05834's under simultaneous emission of the GW peak and the first
#: photons, from one event on one line of sight (DOCKET 67).

# INPUTS -- the pass's design point and literature values, each with its
# status word.  Not results.
M_TX, L_TX, OMEGA_TX = 1.0e6, 100.0, 100.0      # kg, m, rad/s: 1000 t rod
H_NOISE = 1.0e-23                               # Hz^-1/2, LIGO-class receiver
#: No source recorded by the pass.  DOCKET 67 read the curves at 31.83 Hz (the
#: seated omega_GW = 200 rad/s): aLIGO design 8.24e-24, O4-high 9.21e-24.  The
#: ASD is frequency-dependent and <= 1e-23 only above ~28-30 Hz, so this is
#: not a value for any w, though bulk_bits_per_watt takes it as the default.
NU_EM, DISH_D = 1.0e9, 100.0                    # Hz, m: the EM control link
HPL = 2 * math.pi * HBAR                        # h, from hbar
#: hbar c in GeV m, ASKED of higgs.py (HBAR_C in J m over GEV_IN_J, the exact
#: elementary charge x 1e9).  Formerly a retyped E_CHARGE = 1.602176634e-19 here.
HBARC_GEV_M = higgs.HBAR_C / higgs.GEV_IN_J
R_EOTWASH = 38.6e-6                             # m, Lee et al. 2020, 95% CL (READ)
#: The |alpha| = 1 (gravitational-strength Yukawa) edge.  A circle's leading
#: correction is alpha = 2 (8/3 with the graviton's tensor structure, NAMED,
#: not read), whose edge is tighter -- Lee's own extra-dimension reading is a
#: toroidal radius below 30 um -- so this r is generous; at 30 um the SME null
#: is 41.98 orders, not 42.20 (DOCKET 67, computed).
#: Mbar4, the reduced Planck mass (G = 1/(8 pi Mbar4^2)), COMPUTED by higgs.py
#: from hbar, c and G.  The consolidation first TYPED 2.435e18 here, the
#: four-figure quotation of the same quantity (1.3e-4 relative low); it is not
#: a Kabat & Nomura printed input -- their eq. 72-73 fix Mbar4 as the 4D reduced
#: Planck mass, which is this -- so it is replaced, not kept as a READ input.
#: NAMED HYPOTHESIS (DOCKET 67), stated by neither KN nor this file: a
#: stabilised radion.  With eq. 69's n = 0 tensor structure an unstabilised
#: radion gives static sources G_N = (4/3)/(8 pi Mbar4^2) against light's
#: 1/(8 pi Mbar4^2), gamma_PPN = 1/2 (computed), which light deflection
#: excludes; the measured G is eq. 73's Mbar4 only with the radion stabilised.
MBAR4_GEV = higgs.reduced_planck_gev()
SME_LAB_BOUND = 1.0e-21                         # Dreissen et al. (READ)
#: The abstract's "10^-21 level" (arXiv:2206.00570), which KN p.25 also quote
#: citing Dreissen; whether the pass took it from Dreissen or from KN is
#: unrecorded.  Table 1: 1-sigma values 3.9-9.3e-21 on four anisotropic
#: Sun-frame components of c' = c + k/2, not on a scalar |c| (DOCKET 67).
V_CMB = 3.7e5                                   # m/s, CMB dipole (READ)
#: No document recorded.  Planck 2018 I (as restated to DOCKET 67) gives
#: 369.82 +/- 0.11 km/s for the Solar System barycentre, a velocity only under
#: the kinematic reading of the dipole; 3.7e5 is its two-figure rounding.

# ---------------------------------------------------------------------------
# The ruling, as data.
# ---------------------------------------------------------------------------
O6_STATUS = "OPEN (narrowed) -- NOT CLOSED"
O6_CLOSED = False
O6_CAUSE_OF_DEATH_REFUTED = True
#: CORRECTED (DOCKET 67): "source model" became the one-loop stress-tensor
#: source it is, and the normalisation's boost-like scope is named after the
#: status word (specthm reads the word within the sentence after the id).
COUPLING_SOURCE = ("Kabat & Nomura arXiv:2309.05759 eqs. 68, 70-73 -- coupling, "
                   "vertex, normalisation, one-loop stress-tensor source "
                   "(READ by the pass); the source is a quantum stress tensor in "
                   "one-loop self-energies, not an emitter, and the normalisation "
                   "is derived for a boost-like brane and assumed for a tilt-like one")
#: CORRECTED (DOCKET 67): was "gamma*L, not L (GLP eq. 39)" -- no branch
#: condition, the product named for r, and an unverified equation number.
EOTWASH_BOUNDS = ("r = gamma*L/(2 pi), so gamma*L, not L -- on the bulk-graviton "
                  "branch only (GLP's moving-brane potential; its equation "
                  "number, given as 39, is unverified)")
OMEGA_GW_OVER_OMEGA = 2
CLOSING_PREMISE = "field-blind single-mode capacity ceiling"
CLOSING_PREMISE_STATUS = "NOT-FOUND"
# O6_DICHOTOMY is built BELOW, after SAVING_AT_B0_NS is computed: its bulk
# branch quotes that figure, and a typed copy would not follow the span or D_GW.
O6_SETTLED = "CONDITIONALLY -- narrowed, not closed"

O7_STATUS = "OPEN (narrowed) -- NOT CLOSED"
O7_CLOSED = False
GW170817_BOUNDS = "beta (the brane's speed through S^1), not B"
B_MEASURED = False
#: CORRECTED (DOCKET 67): named only the bulk graviton.  GKLM eq. (38) is the
#: untilted, B = 0 case; for B != 0 the GW excess depends on B and direction
#: (at B = 0.999387630 the backward-held beta is 57.1x BETA_MAX, computed).
BETA_BOUND_CONDITIONAL_ON = ("the graviton being a bulk degree of freedom, on an "
                             "untilted brane seen from B = 0 (GKLM eq. 38)")
PROVENANCE_94NS = "GW170817 (7e-16), NOT the CMB dipole"
R1_ROW_OPENED = False
O7_ANSWERED_BY = ("a measurement of B, Earth's velocity relative to the "
                  "preferred brane frame -- a directional multi-messenger GW/EM "
                  "arrival-time survey (N = 1 event today)")

S5_STATUS = "OPEN -- unchanged, downgrade stands"
S5_FIGURES_MEASURED = False
S5_FIGURES_STATUS = ("RECOVERED BY INVERSION from a hard-coded seed; round-trip "
                     "residual is x = f(f^-1(x)) -- NOT MEASURED")
S5_OWED = "DOCKET 56: the instrument that computes N from the specification"

#: The span the O6/O7 pass and the ruling fed their scripts: the seated span
#: rounded to seven figures.  A FIXTURE INPUT ONLY -- it reproduces the ruling's
#: ten-digit figures below; every seated O7 figure uses foliation's span.
RULING_SPAN_M = 4.017499e16

#: Fixtures the ruling reproduced AT RULING_SPAN_M; --selftest recomputes each.
O7_FIXTURES = (("beta", "3.74165738677e-08"), ("1/beta", "26726124.1912"),
               ("brane speed m/s", "11.2172066497"),
               ("Proxima light time s", "134009341.889"),
               ("Proxima light time yr", "4.246499794"),
               ("Delta_tau ns", "93.8065393226"))


# ============================================================ O6
def rod_luminosity(Mkg=M_TX, l_m=L_TX, Om=OMEGA_TX, coeff=(2, 45)):
    """L_GW = (2/45) G M^2 l^4 Omega^6 / c^5; coefficient re-derived by sympy."""
    return coeff[0] / coeff[1] * G * Mkg ** 2 * l_m ** 4 * Om ** 6 / C ** 5


def strain(Lw, D, w):
    """h at distance D, angular frequency w, from Lw/(4 pi D^2) = c^3 w^2 h^2/(16 pi G).

    h is the SKY-RMS strain, h^2 = <h_+^2 + h_x^2> averaged over directions:
    the published flux is c^3/(16 pi G) <hdot_+^2 + hdot_x^2> (exact for
    this h; a linearly polarised wave of peak h carries half), and
    L/(4 pi D^2) is isotropic, while the rod radiates 5/2 of it face-on and
    5/16 edge-on, its axis against the Proxima line unspecified (DOCKET 67)."""
    return (2.0 / (D * w)) * math.sqrt(G * Lw / C ** 3)


def bulk_bits_per_watt(w, D=L_PROXIMA, hn=H_NOISE):
    """(h/h_n)^2 bits/s at unit SNR, per watt radiated: 4G/(D^2 c^3 w^2 h_n^2).

    h is strain()'s sky-rms strain; h_n defaults to H_NOISE at every w,
    although 1e-23 holds only above ~28-30 Hz (DOCKET 67)."""
    return 4.0 * G / (D ** 2 * C ** 3 * w ** 2 * hn ** 2)


def corrected():
    """(h, bits/s/W) at omega_GW = 2 Omega -- the seated figures."""
    w = OMEGA_GW_OVER_OMEGA * OMEGA_TX
    return strain(rod_luminosity(), L_PROXIMA, w), bulk_bits_per_watt(w)


def as_scripted():
    """(h, bits/s/W) at omega = Omega -- the pass's figures, WITHDRAWN."""
    return strain(rod_luminosity(), L_PROXIMA, OMEGA_TX), bulk_bits_per_watt(OMEGA_TX)


def em_bits_per_watt(D=L_PROXIMA, dish=DISH_D, nu=NU_EM):
    """The EM comparison link: identical dishes both ends, one bit per photon.
    Route 1, antenna gain: G_t A_r / (4 pi D^2), G_t = 4 pi A / lambda^2."""
    lam = C / nu
    area = math.pi * (dish / 2) ** 2
    gain = 4 * math.pi * area / lam ** 2
    return gain * area / (4 * math.pi * D ** 2) / (HPL * nu)


def em_bits_per_watt_friis(D=L_PROXIMA, dish=DISH_D, nu=NU_EM):
    """Route 2, the Friis aperture form A_t A_r / (lambda^2 D^2), written
    without a gain -- an independent evaluation for the selftest's control."""
    area = math.pi * dish ** 2 / 4
    return area * area * nu ** 2 / (C ** 2 * D ** 2) / (HPL * nu)


def brane_beats_bulk_orders():
    return math.log10(em_bits_per_watt() / corrected()[1])


# ============================================================ O7
def o7_exact(digits=50, span_m=L_PROXIMA):
    """Everything in d = gamma - 1, at `digits`, never 1 - 1/(1+d).

    With the seated span (4.2465 ly) the light time is 4.2465 Julian years
    EXACTLY, since a light year is c times one; the ruling's 4.246499794 yr is
    its span rounded to 4.017499e16 m, not a property of the arithmetic."""
    getcontext().prec = digits
    d = Decimal(repr(D_GW))
    beta = (d * (2 + d)).sqrt() / (1 + d)
    T = Decimal(repr(span_m)) / Decimal(repr(C))
    dtau = T * d / (1 + d)
    return {"beta": beta, "1/beta": 1 / beta, "brane speed m/s": beta * Decimal(repr(C)),
            "Proxima light time s": T, "Proxima light time yr": T / Decimal(repr(YR)),
            "Delta_tau ns": dtau * Decimal(10) ** 9, "fraction": dtau / T}


def o7_naive_double():
    """The pass's first script, reproduced as a CONTROL: in double precision d
    is three ulps and 1 - 1/(1+d)^2 loses every digit.  WITHDRAWN figures."""
    beta = math.sqrt(1.0 - 1.0 / (1.0 + D_GW) ** 2)
    save = L_PROXIMA * (1.0 - 1.0 / (1.0 + D_GW)) / C
    return beta, save * 1e9


def cmb_gamma_minus_1():
    """Gamma - 1 at the CMB dipole, precision-safe: expm1(-log1p(-x)/2).

    Five figures computed from the two-figure V_CMB, at the barycentre: the
    receiver's value runs 6.456e-07 .. 8.860e-07 over a year (DOCKET 67)."""
    return math.expm1(-0.5 * math.log1p(-(V_CMB / C) ** 2))


def b_for_saving(want_s):
    """The escape priced: the common boost B whose forward saving is want_s
    over the Proxima span with the backward excess held at d = D_GW (GW170817's
    edge, under simultaneous emission) (GKLP eq. (22) extremised, g -> 1, as
    the pass read it).

    "Extremised" means antipodal: GW170817's propagation exactly antiparallel
    to Earth -> Proxima, so the result is a FLOOR, not a sufficient price (on
    the real sky, one second costs 0.9994645711).  saving/T = d((1+B)/(1-B))^2
    is the gamma -> 1 linearisation; it fails near T/2 (DOCKET 67)."""
    T = L_PROXIMA / C
    r = (want_s / T) / D_GW
    return (math.sqrt(r) - 1.0) / (math.sqrt(r) + 1.0)


def zeta3(n=200000):
    return sum(1.0 / k ** 3 for k in range(1, n)) + 1.0 / (2 * n * n)


def sme_coefficient(beta=1.0, R=R_EOTWASH):
    """|c| from Kabat & Nomura eqs. 76-77 at mu r -> 0: I_grav = -zeta(3)/4.

    Eq. 77 holds for b^2 ~ 0 and m ~ 0 (mu is the graviton's IR regulator,
    eq. 69, so mu r -> 0 is legitimate).  The default beta = 1 lies outside
    b^2 ~ 0 and outside the paper's b^2 in (0,1), and the electron's
    pi m r = 3.14e8 at 38.6 um violates m ~ 0: this is the formula evaluated
    outside its hypotheses, an arithmetic value and not a bound.  It is the
    isotropic c_00 = (3/4) beta^2 part (DOCKET 67)."""
    rG = R / HBARC_GEV_M
    return (1 / (16 * math.pi ** 2)) / (math.pi * rG * MBAR4_GEV) ** 2 \
        * 0.75 * beta ** 2 * zeta3() / 4


# ---------------------------------------------------------------------------
# COMPUTED AT IMPORT, stdlib, so ledger.py can ask them.  Not typed: each is the
# output of a function above, and --selftest pins it against the ruling.
# ---------------------------------------------------------------------------
STRAIN_H, THROUGHPUT_BITS_PER_S_PER_W = corrected()
WITHDRAWN_STRAIN_H, WITHDRAWN_THROUGHPUT = as_scripted()
BRANE_BEATS_BULK_ORDERS = brane_beats_bulk_orders()
_O7 = o7_exact()
BETA_MAX = float(_O7["beta"])                       # conditional on a bulk graviton
SAVING_AT_B0_NS = float(_O7["Delta_tau ns"])
SAVING_FRACTION = float(_O7["fraction"])
CMB_GAMMA_MINUS_1 = cmb_gamma_minus_1()
B_FOR_ONE_SECOND = b_for_saving(1.0)                # a floor (antipodal), not a sufficient price
SME_ORDERS_SHORT = math.log10(SME_LAB_BOUND / sme_coefficient())

#: O6's dichotomy (the ruling's third reason O6 does not close).  The bulk
#: branch's figure is FORMATTED from SAVING_AT_B0_NS, and it is a figure at the
#: UNTESTED B = 0: the closure runs through O7's unmeasured B (reason 2).
O6_DICHOTOMY = (
    ("graviton is a bulk degree of freedom",
     "transducer exists (LIGO reads); GW170817 binds beta; saving <= %.1f ns "
     "at the UNTESTED B = 0 (O7's B is not measured); settled only on this "
     "branch" % SAVING_AT_B0_NS),
    ("graviton is brane-confined",
     "no transducer; GW170817 bounds nothing about beta; free Yukawa lambda "
     "(Kabat & Nomura eq. 41); no rate; the row reverts"),
)


# ============================================================ symbolic
def verify_symbolic(sp):
    t, Om, M, ell, Gs, cs = sp.symbols('t Omega M ell G c', positive=True)
    A = M * ell ** 2 / 12
    I = sp.Matrix([[A * sp.cos(Om * t) ** 2, A * sp.sin(Om * t) * sp.cos(Om * t), 0],
                   [A * sp.sin(Om * t) * sp.cos(Om * t), A * sp.sin(Om * t) ** 2, 0],
                   [0, 0, 0]])
    Q = I - sp.eye(3) * I.trace() / 3
    rows = []
    # omega_GW = 2 Omega: the quadrupole has period pi/Omega, not 2 pi/Omega
    shift = Q.subs(t, t + sp.pi / Om) - Q
    rows.append(("Q(t + pi/Omega) - Q(t) = 0", sp.simplify(shift) == sp.zeros(3), True))
    half = sp.simplify((Q.subs(t, t + sp.pi / (2 * Om)) - Q)[0, 0])
    rows.append(("Q(t + pi/2 Omega) != Q(t)  (so the period is exactly pi/Omega)",
                 half != 0, True))
    Q3 = Q.applyfunc(lambda e: sp.diff(e, t, 3))
    Lsym = Gs / (5 * cs ** 5) * sum(Q3[i, j] ** 2 for i in range(3) for j in range(3))
    Lavg = sp.simplify(sp.integrate(Lsym, (t, 0, 2 * sp.pi / Om)) * Om / (2 * sp.pi))
    coeff = sp.nsimplify(sp.simplify(Lavg / (Gs * M ** 2 * ell ** 4 * Om ** 6 / cs ** 5)))
    rows.append(("rod: L_GW / (G M^2 l^4 Omega^6/c^5)", coeff, sp.Rational(2, 45)))
    Lg, D, w, h = sp.symbols('L D omega h', positive=True)
    hsol = sp.solve(sp.Eq(Lg / (4 * sp.pi * D ** 2), cs ** 3 * w ** 2 * h ** 2 / (16 * sp.pi * Gs)), h)[0]
    rows.append(("strain: h - (2/(D w)) sqrt(G L/c^3)",
                 sp.simplify(hsol - 2 / (D * w) * sp.sqrt(Gs * Lg / cs ** 3)), 0))
    # S5: the round trip is a tautology for ANY A
    Asym, hb = sp.symbols('A hbar', positive=True)
    N_of_A = sp.sqrt(Asym * sp.pi / (3 * hb * sp.log(2) ** 2))
    A_of_N = lambda n: 3 * hb * n ** 2 * sp.log(2) ** 2 / sp.pi
    rows.append(("S5: A(N(A)) - A for SYMBOLIC A -- residual 0 proves nothing",
                 sp.simplify(A_of_N(N_of_A) - Asym), 0))
    return rows


# ============================================================ report / selftest
def report():
    print(__doc__.split("=====", 1)[0].strip())
    h, b = corrected()
    hx, bx = as_scripted()
    print("\nO6  corrected (omega_GW = 2 Omega): h = %.4e   bulk = %.4e bits/s/W" % (h, b))
    print("    WITHDRAWN (omega = Omega):       h = %.4e   bulk = %.4e bits/s/W" % (hx, bx))
    print("    EM control %.4e bits/s/W; brane beats bulk by %.2f orders"
          % (em_bits_per_watt(), brane_beats_bulk_orders()))
    ex = o7_exact()
    print("\nO7  (50 digits, conditional on a bulk graviton)")
    for k in ("beta", "1/beta", "brane speed m/s", "Proxima light time s",
              "Proxima light time yr", "Delta_tau ns", "fraction"):
        print("    %-24s %s" % (k, "%.12g" % ex[k]))
    nb, ns = o7_naive_double()
    print("    WITHDRAWN, double precision: beta = %.6e, %.4f ns" % (nb, ns))
    print("    CMB dipole Gamma - 1 = %.4e (barycentric) -- a candidate for the receiver's B, not the 94 ns" % cmb_gamma_minus_1())
    print("    escape floor: B >= %.9f for 1 s; B >= %.8f for half the light time (linearised)"
          % (b_for_saving(1.0), b_for_saving(0.5 * L_PROXIMA / C)))
    print("    SME null: |c| = %.3e at r = 38.6 um, beta = 1 vs %.0e -- %.0f orders short"
          % (sme_coefficient(), SME_LAB_BOUND, math.log10(SME_LAB_BOUND / sme_coefficient())))
    print("\nO6: %s   O7: %s   S5: %s" % (O6_STATUS, O7_STATUS, S5_STATUS))
    return 0


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-62s %s" % ("ok" if good else "XX", label,
                                   got if good else "%s != %s" % (got, want)))

    def near(label, got, want, tol):
        nonlocal ok
        d = abs(got - want) / max(1e-300, abs(want))
        good = d <= tol
        ok &= good
        print("  [%s] %-62s %.12g (rel %.1e)" % ("ok" if good else "XX", label, got, d))

    try:
        import sympy as sp
    except ImportError as exc:                       # pragma: no cover
        raise SystemExit("branelink.py --selftest needs sympy: %s" % exc)

    print("1. THE SYMBOLIC STEPS (sympy)")
    for lab, got, want in verify_symbolic(sp):
        if isinstance(got, bool):
            chk(lab, got, want)
        else:
            chk(lab, sp.simplify(got - want) == 0, True)

    print("\n2. O6 -- THE DECISIVE NUMBER, CORRECTED BY A FACTOR OF FOUR")
    h, b = corrected()
    hx, bx = as_scripted()
    near("corrected strain h at omega_GW = 2 Omega", h, 4.3359e-48, 1e-4)
    near("corrected bulk channel, bits/s/W", b, 1.5347e-27, 1e-4)
    near("WITHDRAWN strain (omega = Omega)", hx, 8.6717e-48, 1e-4)
    near("WITHDRAWN bulk channel", bx, 6.1389e-27, 1e-4)
    chk("the error is exactly 2x and 4x", (round(hx / h, 12), round(bx / b, 12)), (2.0, 4.0))
    # CONTROLS on the EM comparison link, each computed and each able to fail:
    # two independent forms of the link budget, and its two scalings.
    e0 = em_bits_per_watt()
    near("CONTROL: EM link, gain form = Friis aperture form", e0,
         em_bits_per_watt_friis(), 1e-12)
    near("CONTROL: EM link scales as D^-2 (D -> 2D gives 1/4)",
         em_bits_per_watt(D=2 * L_PROXIMA) / e0, 0.25, 1e-12)
    near("CONTROL: EM link scales as (dish area)^2 (d -> 2d gives 16)",
         em_bits_per_watt(dish=2 * DISH_D) / e0, 16.0, 1e-12)
    near("REGRESSION PIN (no corpus provenance): EM link bits/s/W",
         e0, 0.6417571715841273, 1e-9)
    near("brane beats bulk by ~26.6 orders", brane_beats_bulk_orders(), 26.6, 2e-3)
    chk("O6's cause of death is refuted, and that is a narrowing",
        (O6_CAUSE_OF_DEATH_REFUTED, O6_CLOSED), (True, False))
    chk("the closing premise is NOT-FOUND", CLOSING_PREMISE_STATUS, "NOT-FOUND")
    chk("the dichotomy has two branches, one a closure", len(O6_DICHOTOMY), 2)
    chk("the bulk branch's saving is formatted from SAVING_AT_B0_NS",
        ("<= %.1f ns" % float(o7_exact()["Delta_tau ns"])) in O6_DICHOTOMY[0][1], True)
    chk("... and says it is at the untested B = 0",
        "UNTESTED B = 0" in O6_DICHOTOMY[0][1], True)
    chk("the docstring's dichotomy quotes the same figure",
        ("<= %.1f ns" % SAVING_AT_B0_NS) in __doc__, True)
    near("hbar c in GeV m: higgs.py's agrees with this file's hbar and c",
         HBARC_GEV_M, HBAR * C / higgs.GEV_IN_J, 1e-15)

    print("\n3. O7 -- THE ARITHMETIC AT 50 DIGITS")
    exr = o7_exact(span_m=RULING_SPAN_M)
    for key, want in O7_FIXTURES:
        near("%s (the ruling's span, 4.017499e16 m)" % key, float(exr[key]),
             float(want), 1e-10)          # the ruling printed 10-12 digits
    ex = o7_exact()
    near("SEATED span: light time = 4.2465 Julian years exactly",
         float(ex["Proxima light time yr"]), foliation.PROXIMA_LY, 1e-15)
    near("SEATED span: Delta_tau = 93.80654 ns (agrees with the ruling to 5e-8)",
         float(ex["Delta_tau ns"]), float(exr["Delta_tau ns"]), 1e-7)
    near("fraction = d/(1+d) = 7.0e-16", float(ex["fraction"]), 7.0e-16, 1e-12)
    chk("W7's 1/beta = 2.6726124e7 vindicated to every printed digit",
        "%.7e" % float(ex["1/beta"]), "2.6726124e+07")
    nb, ns = o7_naive_double()
    chk("CONTROL: double precision DOES lose it -- beta 3.650024e-08",
        "%.6e" % nb, "3.650024e-08")
    chk("CONTROL: ... and 89.2682 ns (both WITHDRAWN)", "%.4f" % ns, "89.2682")
    near("provenance: T x 7e-16 = 9.3807e-08 s (GW170817)",
         float(ex["Proxima light time s"]) * D_GW, 9.3807e-08, 1e-4)
    near("the CMB dipole's Gamma - 1 (barycentric; a candidate for B)", cmb_gamma_minus_1(),
         7.6161e-07, 1e-4)
    near("escape: B for a one-second saving", b_for_saving(1.0), 0.999387630, 1e-9)
    near("escape: B for half the light time (linearised, g -> 1)", b_for_saving(0.5 * L_PROXIMA / C),
         0.99999993, 1e-8)
    near("SME null |c| at r = 38.6 um, beta = 1", sme_coefficient(), 6.37e-64, 1e-3)
    chk("... 42 orders short of the 1e-21 bound",
        round(math.log10(SME_LAB_BOUND / sme_coefficient())), 42)
    chk("GW170817 bounds beta, not B -- B is not measured", B_MEASURED, False)
    chk("R-1 is not opened", R1_ROW_OPENED, False)
    chk("O7 is not closed", O7_CLOSED, False)

    print("\n4. S5 -- NOT SEATED")
    chk("the four figures are not MEASURED", S5_FIGURES_MEASURED, False)
    src = open(__file__).read()
    # joined at run time: a literal "a" + "b" is constant-folded into the .pyc,
    # and the grep this row relies on would then find it there.
    seed = "".join(["8.04", "1537", "e23"])
    chk("and the hard-coded seed does not appear in this file", seed in src, False)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
