#!/usr/bin/env python3
r"""
massform.py -- DOCKET 65.  MASS FORMATION AT THE SEAT.  M'S MECHANISM, DECIDED
ON ITS ARITHMETIC.

    python3 massform.py             the reading
    python3 massform.py --selftest  every figure, every control; STDLIB ONLY

Run under python3 (3.11) from research/warp-drive.  STDLIB ONLY.  It imports
higgs, excite, warpfolder, stock, stockgate, transit, ledger, nopath, permute,
gravity and pdgcapture from this directory and COPIES NONE OF THEM: every figure
an owner holds is ASKED of it at run time, and the selftest checks with
`inspect` that no callable used here is a local re-implementation carrying an
owner's name.  It edits no peer.

M's mechanism, verbatim (ledger.RULED_BY_M, row M-S1A-P1):

    "As soon as the information hits the seat, it triggers the higgs field,
     and atomic mass forms."

M's consideration, verbatim, same row:

    "If the elements required for seating are present, then the conditions
     for a higgs field or something like it are also present."

M ruled it be TESTED AS A DOCKET.  It was neither dismissed nor accepted in
advance.  Five computations decide it; the selftest checks both strings against
the ledger row, so a misquote of M breaks the build.

===============================================================================
0.  THE ANSWER
===============================================================================

THE CONSIDERATION IS TRUE.  THE MECHANISM, AS STATED, IS REFUSED ON FOUR
COUNTS.  EACH COUNT ALONE IS SUFFICIENT, AND NONE RESTS ON A CONTESTED FIGURE.

  M65-1 PRESENCE.  The consideration holds, and more strongly than M put it.
     An electron of the measured mass REQUIRES a nonzero Higgs field where it
     is, because fermion masses are proportional to phi (READ).  But the vev is
     uniform, so the condition holds everywhere, with or without the elements.
     A condition that holds everywhere cannot be what triggers anything.  The
     field is not switched on by arrival, because it is already on.  To change
     it at the seat needs a local source (D15, D16).  A source of positive rest
     energy whose mass comes from phi (D20's model) can only LOWER it.
  M65-2 SHARE.  The Higgs gives the payload 3.010e-4 of its mass through the
     electrons.  It gives the nucleons 9.28 % (FLAG 2+1) to 10.85 % (FLAG
     2+1+1) of theirs by the READ sigma terms, and 0.961 % / 1.230 % by the
     naive valence sum.  Only if the heavy-quark trace-anomaly coupling is
     counted, which is CONTESTED as a mass share, does it reach 0.2944 to
     0.3066.  On every reading the Higgs supplies less than half of the atomic
     mass.  The rest is QCD binding.
  M65-3 ENERGY.  Forming the payload's rest energy needs Mc^2 = 6.2913e18 J
     carried by the signal's CARRIER.  That is 1504 megatons.  A bit has no
     energy of its own.  Landauer prices only erasure: the count of erased
     bits whose minimum heat at the CMB temperature equals Mc^2 is 2.4120e41.
     Bekenstein bounds the bits by the energy, never the reverse: at most
     1.8038e45 bits fit in a body of that energy within 1 m.  Neither turns a
     bit into a baryon.
  M65-4 CONSERVATION.  The payload holds 4.2109e28 baryons and 2.3132e28
     electrons, so B - L = N_n = 1.8977e28.  With B and L conserved, making it
     from energy needs at least 1.9975 Mc^2, and at least 4.2109e28 units of
     antibaryon number must be put somewhere.  The only Standard Model process
     that violates B is the sphaleron, with Delta B = Delta L = 3.  At zero
     temperature one transition is suppressed by 10^-160.95, a figure that
     inherits NAMED-NOT-READ through v.  The payload needs
     1.4036e28 transitions.  Each one crosses a barrier 3226 times the rest
     energy of the 3 baryons it makes.  Above T_c the transitions are
     unsuppressed, but the vev is approximately zero there, so no masses form.
     At collider energies the rate is CONTESTED, and it is recorded, not
     resolved.
  M65-5 VERDICT.  What survives is reconstruction from destination stock
     (D25, transit.CARRIES_SUBSTANCE = False).  In that route no mass forms and
     the Higgs triggers nothing.  The sphaleron route also survives, as the one
     Standard Model process in which the Higgs field's structure turns energy
     into baryons.  It is PRICED, not dismissed.

===============================================================================
1.  M65-1  PRESENCE
===============================================================================

THE CONSIDERATION, COMPUTED.  At tree level in unitary gauge, "the masses of the
W+/- and Z0 weak vector bosons and the fermions are proportional to phi"
(Morrissey & Ramsey-Musolf 1206.2942 p.4, READ).  So m_f = y_f v/sqrt(2).  If
m_f > 0 at a place, then phi != 0 at that place.  The electron mass in the
capture is 0.510998951 MeV (READ).  Wherever the payload's elements exist with
their measured masses, therefore, the Higgs field has its vev.  THEOREM, on
H-TREE.

The Yukawas y_f = sqrt(2) m_f / v are computed from the READ masses for all
nine charged fermions.  The top's is 0.9914 and the electron's is 2.935e-6.
Every y_f inherits G_F's NAMED-NOT-READ through v = higgs.vev().

THE CONSEQUENCE, DERIVED AND NOT ASSUMED.  The vev is the constant solution
V'(v) = 0, the same at the seat as everywhere else.  Arrival therefore has
nothing to switch on.  There are exactly three ways to change a field that is
already on, and each is asked of its owner:

  (a) a RADIAL displacement.  It returns to v at rate exactly m_h outside its
      source (D15, excite.TAIL_RATE_IS_MASS), over hbar/(m_h c) =
      1.577e-18 m.  Inside the source it is -J/m_h^2, ultralocal (D16,
      excite.DISPLACEMENT_IS_ULTRALOCAL).  A signal that brings no source to
      the seat changes nothing there.  A source whose mass is proportional to
      phi holds phi = v(1 - eps) with rest energy 4 rho_EW eps(2-eps)(1-eps)^2
      (D20, excite.holding_terms).  That is positive only for eps > 0.  So a
      source of POSITIVE rest energy can only LOWER the vev, and with it every
      Yukawa mass, by the fraction eps.  Raising the vev at the seat would need
      a source of negative rest energy.  Holding any eps costs 2/eps joules of
      source per joule of field (excite.holding_ratio).
  (b) a displacement along a GAUGE direction.  It changes no mass and no
      derivative-free gauge-invariant local observable (D19,
      excite.FLAT_DIRECTIONS_ARE_INERT).
  (c) making Higgs QUANTA.  Each costs m_h c^2 and lives about 2e-22 s
      (excite.QUANTUM_LIFETIME_S, one significant figure by excite's refusal
      6).  A number state has <delta phi> = 0 (excite section 0).  Their decays
      conserve B and L, so they reduce to M65-4's pair floor.

And where a displacement does change m_e, the result is an exact dilation, not
new mass (D18, excite.ELECTRON_MASS_IS_A_RULER).

This is NOT higgs.py's withdrawn "cannot be switched on in one place" (DOCKET
63 F3; higgs.CANNOT_BE_SWITCHED_ON_IN_ONE_PLACE = False, asked).  A source does
displace the vev locally, at the price D20 states.  What fails is the SWITCH:
there is no off state at the seat for arrival to end.

    SO THE CONSIDERATION IS TRUE AND DISCRIMINATES NOTHING.  It is true at the
    seat because it is true everywhere.  This is nopath.py's Campbell-Magaard
    lesson in a second setting: a condition that always holds carries no
    information about any one place.

===============================================================================
2.  M65-2  SHARE -- WHAT PART OF THE PAYLOAD'S MASS THE HIGGS SUPPLIES
===============================================================================

The payload is stock.HUMAN (ICRP Reference Man, CITED by stock.py) at stock.py's
own default of 70 kg, asked through inspect.  No fraction is retyped.  The
atom count of element e is f_e M / (A_r(e) u).  The electrons number Z per
atom, with Z READ from the AME2020 capture through gravity.symbol_to_Z().  The
nucleons number A per atom, on H-A.

THREE MEASURES OF THE NUCLEONS' HIGGS PART, KEPT APART:

  NAIVE VALENCE.  (2m_u + m_d)/m_p = 0.961 % and (m_u + 2m_d)/m_n = 1.230 %,
     from the capture's current-quark masses (READ).  This counts the valence
     quarks' own masses and nothing else.
  SIGMA TERMS.  The FLAG 2024 averages, READ with their locators.  sigma_piN
     is 60.9(6.5) MeV at N_f = 2+1+1 and 42.2(2.4) MeV at N_f = 2+1.  sigma_s
     is 41.0(8.8) and 44.9(6.4) MeV.  Each gives f_l = (sigma_piN + sigma_s)/
     m_N = 10.85 % and 9.28 %, with m_N = (m_p + m_n)/2 READ.  "The sigma_piN,s,c
     give the shift in M_N due to nonzero light-, strange- and charm-quark
     masses" (FLAG).  THIS is the part of the nucleon mass that comes from
     quark masses, i.e. from the Higgs.  sigma_piN is CONTESTED: "there is now
     a 2.7 sigma difference between the N_f = 2 + 1 and N_f = 2 + 1 + 1 FLAG
     averages" (FLAG p.273).  So both are printed and neither is chosen.  The
     chiQCD lattice gives 9(2)(1)% and Ji gives "about 1/8"
     (both READ).
  HEAVY-QUARK COUPLING.  The SVZ relation gives f_TQ = (2/27)(1 - f_l) for
     each of c, b, t (Ellis-Olive-Savage eq. (10), READ; SVZ 1978 CITED).
     The coupling sum is 2/9 + (7/9) f_l, which is 0.3066 and 0.2944 here
     against Hoferichter et al.'s 0.305(9) (READ).  The algebra is checked
     exactly over Fraction.  AS THE SOURCE STATES IT this is the Higgs's
     COUPLING to the nucleon, and Ji: "the contributions cancel each other in
     the limit of m_f -> infinity".  Counting it as mass the Higgs MAKES is
     CONTESTED.  It is printed with that label and never added to the sigma
     terms.

THE REMAINDER IS QCD.  1 - f_l of each nucleon's mass is not quark-mass mass.
chiQCD's decomposition (quark energy, glue energy, and a quarter of the trace
anomaly at 23(1)(1)%) is READ.  The nuclear binding is computed as the closure
term: nucleon rest masses plus electron rest masses, minus the listed payload.
It comes to 0.5020 kg, the nuclear binding net of Coulomb.  It is the one
figure here that H-A moves materially: raising every mean nucleon number by
0.01 moves it by 0.1124 kg.  So it is printed to close the books, and nothing
turns on it.

    NO SINGLE "HIGGS SHARE" IS PRINTED.  The verdict uses only the LARGEST
    reading, as an upper bound, and it uses that bound computed twice: over
    the READ readings alone, and over all of them.

===============================================================================
3.  M65-3  ENERGY -- WHAT INFORMATION CAN CARRY
===============================================================================

A signal carries energy only through its carrier.  For mass to form FROM the
signal, the carrier must deliver at least Mc^2 = 6.2913e18 J
(warpfolder.rest_energy_j) if B is free.  If B and L are conserved it must
deliver 1.9975 Mc^2 (section 4).  That is energy conservation.  THEOREM.

  LANDAUER, at the CMB temperature.  At least k_B T ln 2 of heat per bit
     ERASED (Lloyd, Bennett; READ), computed by nopath.landauer_energy.  At
     permute.T_CMB = 2.7255 K that is 2.608e-23 J per bit.  So Mc^2 equals the
     minimum heat of erasing 2.4120e41 bits.
     WHAT IT SHOWS: if the seat erased that many bits, it would have to shed
     at least one payload's rest energy as HEAT.  Heat has B = 0.
     WHAT IT DOES NOT SHOW: that a bit contains energy, or that the signal
     needs any.  Reversible transfer has no minimum cost (nopath.
     LANDAUER_IS_THE_WEAKER_HALF), and an inequality on dissipation turns
     nothing into mass.
  BEKENSTEIN, for a body of energy Mc^2 within R = 1 m (H-R).  I <=
     2 pi E R/(hbar c ln 2) = 1.8038e45 bits (nopath.bekenstein_bits).  This
     is the most information such a body can hold.
     WHAT IT SHOWS: it bounds bits BY energy.  More bits need more energy,
     never the reverse, so the bound supplies no joule.  The ratio of the two
     counts is 2 pi R k_B T / (hbar c) = 7478, and it is INDEPENDENT OF THE
     MASS.  Erasing a body's maximal content at 2.7255 K would cost 7478
     times its rest energy.  Information and mass break even only for
     R < hbar c/(2 pi k_B T) = 0.134 mm.
     WHAT IT DOES NOT SHOW: how many bits a human actually is.  No reliable
     figure exists: the two published counts were NOT-FOUND (section 9), and
     this file quotes neither.

===============================================================================
4.  M65-4  CONSERVATION
===============================================================================

THE COUNT.  B = 4.2109e28 and L = N_e = 2.3132e28.  N_p = N_e because the atoms
are neutral.  So N_n = 1.8977e28 and B - L = N_n.  Cross-check: B against
warpfolder's M/m_p is 1.0062.  The excess is the nuclear binding, net of the
neutrons' extra mass and the electrons.

FROM ENERGY ALONE, WITH B AND L CONSERVED.  Every Yukawa term is a fermion
bilinear.  The selftest computes B = L = 0 for each one, so no Higgs coupling
makes a baryon.  The payload must come with antimatter carrying B' = -B.  Its
mirror costs exactly 2 Mc^2 (CPT).  The rigorous floor is Mc^2 + B mu_min c^2,
where mu_min = 930.1746 MeV is the least nuclear mass per nucleon in the AME2020
capture (56Fe, measured).  That gives 1.9975 Mc^2.  AND THE ANTIMATTER MUST GO
SOMEWHERE: at least 4.2109e28 units of antibaryon number, held apart from all
matter.

WITH B VIOLATED.  The Standard Model has exactly one route: "Delta N_e =
Delta N_mu = Delta N_tau = (1/3) Delta B ; (B - L) is conserved while (B + L) is
violated" (Rubakov & Shaposhnikov, READ).  That is Delta B = Delta L = N_f = 3
per transition, with N_f counted from the capture's charged leptons.

  alpha_W = g^2/4 pi, with g = 2 m_W/v, m_W READ and v from higgs.vev():
     1/29.49.  It INHERITS NAMED-NOT-READ through v.
  zero-temperature suppression, exactly as the source states it,
     exp(-4 pi/alpha_W) = exp(-16 pi^2/g^2): 10^-160.95 per transition.
     No prefactor was read, so NO RATE IS PRINTED.  To make the payload's
     1.4036e28 transitions, (attempts) x (prefactor) must reach 10^189.10.
  E_sph = (2 m_W/alpha_W) B(m_H/m_W) = 4.740 TeV x B, with B between 1.56
     and 2.72 (READ).  The READ values at the measured Higgs mass are 9.11 TeV
     (Tye-Wong, pure SU(2)), 9.08 TeV (Funakubo et al.) and 9.0 TeV (with
     U(1)).  At 9.08 TeV the barrier is 3226 times the rest energy of the 3
     baryons one transition makes.  E_sph is a barrier HEIGHT, not a
     rest-mass cost, and whether it is recovered is not computed.
  B - L is conserved, and the payload's B - L is N_n.  So the sphaleron
     route must emit 1.8977e28 more leptons than the payload keeps.  Like the
     antimatter, they must go somewhere.
  ABOVE T_c = 159.5 +/- 1.5 GeV (D'Onofrio-Rummukainen abstract, READ), which
     is 1.851e15 K, the rate is unsuppressed: Gamma/T^4 = (18 +/- 3)
     alpha_W^5 (READ), which is 8.07e-7 at this file's alpha_W.  But
     the Higgs field there is "approximately zero" (READ), and fermion masses
     are proportional to phi.  So THERE ARE NO YUKAWA MASSES WHILE THE
     TRANSITIONS RUN.  This is warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY,
     asked.  B freezes out at T* = 131.7 GeV (READ).  In the Standard Model
     alone the crossover yields no net asymmetry: "EWBG is unable to explain
     the observed baryon asymmetry within the SM alone" (READ).
  AT COLLIDER ENERGIES: CONTESTED.  Tye-Wong find no exponential
     suppression above E_sph.  Bezrukov et al. find suppression to at least
     250 TeV, on their own stated s-wave hypothesis.  Funakubo et al. find an
     overlap factor of about 10^-155 that survives any band structure.  CMS
     bounds only the Tye-Wong prefactor, at 0.021.  NOT RESOLVED HERE, AND NO
     REFUSAL RESTS ON IT.  Even at no suppression, the route costs at least
     1.4036e28 x E_sph = 3246 Mc^2 in barrier crossings.

===============================================================================
5.  M65-5  VERDICT, DERIVED FROM PINNED BOOLEANS WITH OWNERS
===============================================================================

The mechanism has three links: (L1) arrival TRIGGERS the field; (L2) ATOMIC
MASS FORMS from the triggered field; (L3) the INFORMATION supplies it.  They
are conjunctive, so any one link that fails refuses the mechanism.  Each count
is a boolean with an owner, and derive_verdict() reads the booleans.  Nothing
in it is typed.

  C1 FIELD_SWITCHED_ON_BY_ARRIVAL = False     (L1; M65-1, D15, D16)
  C2 HIGGS_SUPPLIES_MOST_ATOMIC_MASS = False  (L2; M65-2, READ bound alone)
  C3 HIGGS_COUPLING_CREATES_FERMIONS = False  (L2; M65-4, Yukawa charges)
  C4 INFORMATION_HAS_INTRINSIC_ENERGY = False (L3; M65-3, nopath's Landauer)

A count that rests on a CONTESTED figure ALONE cannot refuse.  The selftest
builds that case and checks that it returns OPEN rather than REFUSED.

THE MECHANISM AS STATED: REFUSED, on C1, C2, C3 and C4.  Each alone suffices.
THE CONSIDERATION: TRUE (THEOREM on H-TREE), and it does not discriminate.

WHAT SURVIVES:
  (a) RECONSTRUCTION FROM DESTINATION STOCK.  stockgate.GATE is the condition,
      and transit.CARRIES_SUBSTANCE = False.  No mass forms at the seat, and
      the stock's masses were already given by the uniform vev.  The Higgs's
      part is a precondition already met everywhere, which is M's
      consideration, and it is not a trigger.  S5 and D25 stand unchanged.
  (b) THE SPHALERON ROUTE, priced in section 4.  It is the one Standard Model
      process in which the Higgs field's structure turns energy into baryons.
      The barrier E_sph = (4 pi v/g) B is set by the vev.

===============================================================================
6.  NAMED HYPOTHESES -- EVERY LIMITATION, NONE BURIED
===============================================================================

  H-TREE  m_f = y_f v/sqrt(2), at tree level in unitary gauge, as the READ
          source states it.  The capture's mass column is used as it stands
          (PDG: MS-bar u, d, s at 2 GeV; m_c(m_c), m_b(m_b); t direct), so each
          Yukawa carries that scheme.
  H-A     A_e is the nearest integer to stock.ATOMIC_MASS[e], and the natural
          mixture's mean nucleon number lies within 1/2 of it.  The selftest
          recomputes every count at A_e +/- 1/2 and checks that no boolean
          moves.
  H-LIST  The payload is stock.HUMAN's 14 listed elements.  Their fractions
          sum to 0.99992; the unlisted remainder is carried as its own line
          and assigned no composition.
  H-R     R = 1 m for the Bekenstein comparison.  The ratio of section 3 is
          linear in R and independent of M.
  H-BL    B - L is exactly conserved ("(B - L) is conserved", READ).  A
          Majorana neutrino mass would break it by 2 units.  That was not read.
  H-FLAV  Each lepton flavour is conserved (massless neutrinos).  It is used
          ONLY for the flavour sub-count in the report, which carries no
          verdict.
  H-THERM Plasma fermions above T_c may carry thermal masses of order gT.
          That was NOT read in any source, it is not asserted, and nothing
          here uses it.

===============================================================================
7.  WHAT THIS FILE REFUSES
===============================================================================

   1. ONE NUMBER FOR "THE HIGGS SHARE".  The measures are printed apart.
   2. RESOLVING THE COLLIDER-ENERGY DISPUTE.  It is CONTESTED in the READ.
   3. A REFUSAL ON A CONTESTED FIGURE ALONE.  derive_verdict() makes this
      structurally impossible, and the selftest proves it.
   4. A SPHALERON RATE WITHOUT ITS PREFACTOR.  Only the exponent was read.
   5. AN EXACT ZERO FOR THE VEV ABOVE T_c.  The source says "approximately
      zero".
   6. ANY FIGURE FOR THE INFORMATION CONTENT OF A HUMAN.  Both were NOT-FOUND.
   7. TREATING k_B T ln 2 AS THE ENERGY OF A BIT.  It is a bound on erasure.
   8. COUNTING THE HEAVY-QUARK COUPLING AS HIGGS-MADE MASS.  It is printed as
      CONTESTED.
   9. DISMISSING THE SPHALERON ROUTE.  It is priced.
  10. A FIGURE HELD WITHOUT ITS SOURCE TEXT.  Every READ number used here
      appears in a quotation held in SOURCES, and the selftest checks it.
  11. THE STATUS WORD M RETIRED.  No status here is that word.

===============================================================================
8.  STATUSES AND A DIVERGENCE, RECORDED
===============================================================================

THEOREM: the consideration on H-TREE; D15, D16, D18, D19 as excite states them;
the sign of the holding source; the Yukawa charges; the pair floor; energy
conservation.  MEASURED: every count, share, energy and exponent, each carrying
its inputs' status.  Through v, every Yukawa, alpha_W, E_sph formula value and
exponent INHERITS NAMED-NOT-READ.  Through u = gravity.U_KG (CODATA 2018) and
stock.ATOMIC_MASS, every count and payload share INHERITS NAMED-NOT-READ.
READ: every figure in SOURCES marked READ.  CONTESTED: sigma_piN between
averages; the heavy-quark share as a mass share; the collider rate.

DIVERGENCE FROM THE DOCKET TEXT.  The docket calls the CMB temperature READ.
The tree holds it as permute.T_CMB = 2.7255 with a comment naming Fixsen 2009,
with no capture and no quoted locator.  Here it is CITED, and the Landauer count
inherits CITED.  Nothing turns on it: the ratio of section 3 moves linearly
with T.

NOTHING IS REPAIRED.

===============================================================================
9.  SOURCES
===============================================================================

SOURCES below holds, for every figure used, its locator, its status and the
verbatim text the READ stage returned.  The primaries from before arXiv ('t
Hooft 1976, Klinkhamer-Manton 1984, Ringwald 1990, Espinosa 1990, Sakharov
1967, SVZ 1978, Landauer 1961) are CITED through the papers that were read.
Braunstein's ~1e32 bits and the Leicester 2.6e42 bits are NOT-FOUND: the proxy
blocked both pages, and neither is used.
"""

import inspect
import math
import re
import sys
from fractions import Fraction

import gravity
import excite
import higgs
import ledger
import nopath
import pdgcapture
import permute
import stock
import stockgate
import transit
import warpfolder

# ---------------------------------------------------------------------------
# IMPORTED, NEVER COPIED.  Every owner name this file asks, by module
# attribute.  The selftest checks that each callable is defined in the module
# it is asked of.
# ---------------------------------------------------------------------------
IMPORTS = (
    ("higgs", ("vev", "_capture_row", "M_HIGGS", "GEV_IN_J", "c",
               "VEV_SATURATES_NEC", "CANNOT_BE_SWITCHED_ON_IN_ONE_PLACE")),
    ("excite", ("TAIL_RATE_IS_MASS", "DISPLACEMENT_IS_ULTRALOCAL",
                "ELECTRON_MASS_IS_A_RULER", "FLAT_DIRECTIONS_ARE_INERT",
                "holding_terms", "holding_ratio", "QUANTUM_LIFETIME_S",
                "LAMBDA_H_READ_M", "one_sig", "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18")),
    ("warpfolder", ("HEATING_TO_EW_SCALE_RESTORES_SYMMETRY", "rest_energy_j",
                    "megatons", "baryons_in", "BLUEPRINT_SOURCES_BARYON_NUMBER",
                    "FLASH_IS_A_RECONSTRUCTION_MECHANISM")),
    ("stock", ("HUMAN", "ATOMIC_MASS", "feedstock_kg", "SOURCES")),
    ("stockgate", ("GATE",)),
    ("transit", ("CARRIES_SUBSTANCE", "IT_IS_A_MOVE_NOT_A_COPY")),
    ("nopath", ("landauer_energy", "bekenstein_bits", "KB", "HBAR", "C",
                "LANDAUER_IS_THE_WEAKER_HALF", "BEKENSTEIN_IS_THE_ARGUMENT")),
    ("permute", ("T_CMB",)),
    ("gravity", ("U_KG", "symbol_to_Z", "nuclides")),
    ("pdgcapture", ("read",)),
    ("ledger", ("RULED_BY_M", "DEMAND", "SUPPLY")),
)
_MODS = {"higgs": higgs, "excite": excite, "warpfolder": warpfolder,
         "stock": stock, "stockgate": stockgate, "transit": transit,
         "nopath": nopath, "permute": permute, "gravity": gravity,
         "pdgcapture": pdgcapture, "ledger": ledger}

# ------------------------------------------------------------------ M's words
M_MECHANISM = ("As soon as the information hits the seat, it triggers the higgs "
               "field, and atomic mass forms")
M_CONSIDERATION = ("If the elements required for seating are present, then the "
                   "conditions for a higgs field or something like it are also "
                   "present")
M_ROW = "M-S1A-P1"

# ------------------------------------------------------------- the SI bridge
C = higgs.c                                     # SI-exact, via ladder
MEV_J = higgs.GEV_IN_J / 1000.0                 # SI-exact
MEV_KG = MEV_J / C ** 2
U_KG = gravity.U_KG                             # CODATA 2018  NAMED-NOT-READ
U_MEV = U_KG / MEV_KG

# --------------------------------------------------------------- READ masses
PDGID = {"e": 11, "mu": 13, "tau": 15, "d": 1, "u": 2, "s": 3, "c": 4,
         "b": 5, "t": 6, "p": 2212, "n": 2112, "W": 24}
CHARGED_FERMIONS = ("e", "mu", "tau", "u", "d", "s", "c", "b", "t")


def _read_masses():
    """{name: mass in MeV}, each through higgs._capture_row -- the reader that
    owns captures/PDG-2026.tsv's path in this tree.  READ."""
    return {k: float(higgs._capture_row(i)["mass_MeV"]) for k, i in PDGID.items()}


MASS_MEV = _read_masses()                                        # READ
M_N_MEV = (MASS_MEV["p"] + MASS_MEV["n"]) / 2.0                  # from READ
M_W_GEV = MASS_MEV["W"] / 1000.0                                 # READ


def lightest_baryon():
    """(name, mass MeV) of the lightest baryon in the capture.  READ: the floor
    of section 4 takes it from the table, not from memory."""
    rows = [(float(r["mass_MeV"]), r["name"]) for r in pdgcapture.read()
            if r["family"] == "baryon"]
    m, name = min(rows)
    return name, m


def n_generations():
    """N_f, counted from the capture: charged leptons (family lepton, Q3 = -3).
    The capture excludes the tau' by PDG's own status flag (pdgcapture.py)."""
    return sum(1 for r in pdgcapture.read()
               if r["family"] == "lepton" and r["Q3"] == "-3")


N_F = n_generations()

# ==================================================================== SOURCES
# key: (status, locator, verbatim text as the READ stage returned it).  The
# text is what the misquote check reads; nothing is paraphrased inside it.
SOURCES = {
    "RS96-sel": ("READ",
                 "Rubakov & Shaposhnikov, hep-ph/9603208 (Usp. Fiz. Nauk 166 "
                 "(1996) 493), Sec. 2, eqs. (2.4)-(2.5), PDF pp. 4-5",
                 "Delta N_e = Delta N_mu = Delta N_tau = (1/3) Delta B ; (B - L) "
                 "is conserved while (B + L) is violated.  ... where the factor "
                 "1/3 comes from the baryon number of a quark, while the factor "
                 "3 . 3 is due to colour and number of generations."),
    "tHooft": ("CITED", "cited as ref [20] in hep-ph/9603208 and ref [43] in "
               "CMS 1805.06013; not on arXiv; not read",
               "[20] G. 't Hooft. Phys. Rev. Lett., 37:8, 1976."),
    "RS96-inst": ("READ", "Rubakov & Shaposhnikov hep-ph/9603208, Sec. 4.1, p. 11",
                  "This process can be described by instantons and is strongly "
                  "suppressed by the semiclassical exponent exp(-4 pi / alpha_W)."),
    "TW-size": ("CONTESTED", "Tye & Wong 1505.03690, p.2 (Introduction) and p.7 "
                "(Sec. 2.1)",
                "exponentially suppressed, by a factor like exp(-4 pi/alpha_W) ~ "
                "10^-162 where alpha_W ~ 1/30.   /  since an instanton action S = "
                "2 pi/alpha_W where the weak coupling alpha_W ~ 1/29.7, the "
                "tunneling rate goes like exp(-2S) ~ 10^-162"),
    "RS96-esph": ("READ", "Rubakov & Shaposhnikov hep-ph/9603208, eq. (2.11), p. 7 "
                  "(reporting Klinkhamer & Manton PRD 30, 2212 (1984), CITED)",
                  "E_sph = (2 m_W / alpha_W) B(m_H/m_W), where m_H is the mass of "
                  "the Higgs boson. The function B(m_H/m_W) has been evaluated "
                  "numerically [32]; it varies from 1.56 to 2.72 as m_H/m_W varies "
                  "from zero to infinity. So, the height of the barrier in the "
                  "electroweak theory is of order 10 TeV."),
    "TW-FFS-esph": ("READ", "Tye & Wong 1505.03690 eq.(1.2) p.3; Funakubo, Fuyuto, "
                    "Senaha 1612.05431 eq.(10) p.2",
                    "Using the known Higgs vacuum expectation value v = 246 GeV, W "
                    "Boson mass m_W = 80 GeV and the Higgs Boson mass m_H = 125 "
                    "GeV, we obtain V(Q) ~ 4.75 TeV (1.31 sin^2(m_W Q) + 0.60 "
                    "sin^4(m_W Q)), E_sph = max[V(Q)] = V(pi/(2 m_W)) = 9.11 TeV   "
                    "/   E_sph = g_2 v V(pi/2) ~ 9.08 TeV."),
    "DR-Tc": ("READ", "D'Onofrio & Rummukainen, 1508.07161 (PRD 93 (2016) 025003): "
              "abstract p.1 (the value used); Sec. VII p.8 prints 159.6 +/- 0.1 "
              "+/- 1.5",
              "While the cross-over is smooth, it is very well defined with a "
              "width of only ~ 5 GeV. We measure the cross-over temperature from "
              "the maximum of the susceptibility of the Higgs condensate, with "
              "the result T_c = 159.5 +/- 1.5 GeV.  /  we obtain T_c = 159.6 +/- "
              "0.1 +/- 1.5 GeV, where the first error is due to the statistical "
              "accuracy of the lattice computation and the second one is the "
              "estimated uncertainty of the effective theory approach"),
    "DRT-vev": ("READ", "D'Onofrio, Rummukainen, Tranberg 1404.3565 p.1 and p.3; "
                "1508.07161 footnote 1 p.1",
                "the electroweak symmetry breaking transition in the early "
                "Universe was a smooth cross-over from the symmetric phase at T > "
                "T_c, where the (expectation value of the) Higgs field was "
                "approximately zero, to the broken phase at T < T_c GeV where it "
                "is finite  /  If the temperature is below T_c, v^2(T) is "
                "approximately linear in T, and at T > T_c, it is close to zero.  "
                "/  Although there is no real symmetry breaking phase transition, "
                "we use the conventional labels 'broken' and 'symmetric'"),
    "MRM-phi": ("READ", "Morrissey & Ramsey-Musolf 1206.2942, Sec. 2, below eq.(1), p.4",
                "Note that (in unitary gauge) the masses of the W+/- and Z0 weak "
                "vector bosons and the fermions are proportional to phi."),
    "DRT-rate": ("READ", "D'Onofrio, Rummukainen, Tranberg 1404.3565 (PRL 113 (2014) "
                 "141602): abstract p.1, eqs.(7)-(8) pp.3-4",
                 "The sphaleron rate in the symmetric phase (T > T_c) is "
                 "Gamma/T^4 = (18 +/- 3) alpha_W^5 ... The freeze-out temperature "
                 "in the early Universe, where the Hubble rate wins over the "
                 "baryon number violation rate, is T* = (131.7 +/- 2.3) GeV."),
    "RS96-coll": ("CITED", "Rubakov & Shaposhnikov hep-ph/9603208 p.3, refs [39] "
                  "Ringwald NPB 330 (1990) 1 and [40] Espinosa NPB 343 (1990) 310, "
                  "neither read",
                  "This problem has attracted considerable interest in recent "
                  "years, after the first -- and encouraging at the time -- "
                  "quantitative results were obtained [39,40]. In spite of "
                  "remarkable theoretical developments, this problem is still not "
                  "completely solved; existing results indicate that the "
                  "electroweak baryon number violating processes occur at "
                  "unobservable rates even at very high energies."),
    "BLRRT": ("READ", "Bezrukov, Levkov, Rebbi, Rubakov, Tinyakov hep-ph/0304180 "
              "(PRD 68 (2003) 036005): abstract p.1; Sec. II p.7; their scope: "
              "s-wave, N -> 0, m_H = m_W",
              "Our results show that baryon and lepton number violation remains "
              "exponentially suppressed up to very high energies of at least 30 "
              "sphaleron masses (250 TeV).  /  up to the energy 8 M_W/alpha_W ~ "
              "20TeV the suppression is still high: the suppression factor is "
              "smaller than e^-60 ~ 10^-26 for alpha_W ~ 1/30."),
    "TW-claim": ("CONTESTED", "Tye & Wong 1505.03690 (PRD 92 (2015) 045005): "
                 "abstract p.1; p.28",
                 "We show that the baryon-lepton number violating processes can "
                 "take place without the exponential tunneling suppression (at "
                 "zero temperature) at energies around and above the barrier "
                 "height (sphaleron energy) at 9.0 TeV.  /  A very crude order of "
                 "magnitude estimate gives 10^{4+/-2} such events in the coming "
                 "Large Hadron Collider (LHC) run at 14 TeV"),
    "FFS-rebut": ("READ", "Funakubo, Fuyuto, Senaha 1612.05431, p.4",
                  "the overlap between the coherent state and the in-state "
                  "composed of two particles whose total momentum is E_sph yields "
                  "a suppression factor ~ e^{-pi E_sph/m_W} ~ 10^-155, rendering "
                  "(B + L)-changing process unobservably small. ... Those types of "
                  "the suppressions still remain regardless of the band "
                  "structure, which is not properly discussed in Ref. [8]"),
    "CMS": ("READ", "CMS Collaboration 1805.06013 (JHEP 11 (2018) 042): abstract p.1, "
            "Sec. 8.2 p.17",
            "An upper limit of 0.021 is set at 95% confidence level on the "
            "fraction of all quark-quark interactions above the nominal threshold "
            "energy of 9 TeV resulting in the sphaleron transition."),
    "Sakharov": ("READ", "Rubakov & Shaposhnikov hep-ph/9603208, Sec. 1, p.2 "
                 "(Sakharov JETP Lett. 5 (1967) 24 CITED)",
                 "Today, this short extract is usually dubbed as three necessary "
                 "Sakharov's conditions for baryon asymmetry generation from the "
                 "initial charge symmetric state in the hot Universe, namely: (i) "
                 "Baryon number non-conservation. (ii) C and CP violation. (iii) "
                 "Deviations from thermal equilibrium."),
    "MRM-SM": ("READ", "Morrissey & Ramsey-Musolf 1206.2942 (New J. Phys. 14 (2012) "
               "125003), Sec. 1 pp.2-3",
               "All the ingredients required for EWBG are contained in the SM. "
               "Unfortunately, EWBG is unable to explain the observed baryon "
               "asymmetry within the SM alone. The first impediment is that the "
               "SM electroweak phase transition is first-order only if the mass "
               "of the Higgs boson lies below m_h <~ 70 GeV [18, 19]. ... Even if "
               "the phase transition were first order, the CP violation induced "
               "by the CKM phase does not appear to be sufficient to generate "
               "large enough chiral asymmetries [22, 23, 24]."),
    # ------------------------------------------------------------ the masses
    "FLAG-447": ("READ", "FLAG Review 2024, Aoki et al., arXiv:2411.04268v3, "
                 "Sec. 10.4.4 Eq. (447), p.272",
                 "N_f = 2 + 1 + 1 : sigma_piN = 60.9(6.5) MeV Refs. [26, 101]. (447)"),
    "FLAG-448": ("CONTESTED", "FLAG 2024, arXiv:2411.04268v3, Sec. 10.4.4 Eq. (448), "
                 "p.273; 2.7 sigma from Eq. (447) (FLAG p.273)",
                 "N_f = 2 + 1 : sigma_piN = 42.2(2.4) MeV Refs. [102-106]. (448)"),
    "FLAG-tension": ("READ", "FLAG 2024, arXiv:2411.04268v3, p.273 (quoted in the "
                     "READ stage's note to Eq. (448))",
                     "there is now a 2.7 sigma difference between the N_f = 2 + 1 "
                     "and N_f = 2 + 1 + 1 FLAG averages"),
    "FLAG-449": ("READ", "FLAG 2024, arXiv:2411.04268v3, Eq. (449), p.273",
                 "N_f = 2 + 1 + 1 : sigma_s = 41.0(8.8) MeV Ref. [107]. (449)"),
    "FLAG-450": ("READ", "FLAG 2024, arXiv:2411.04268v3, Eq. (450), p.273",
                 "N_f = 2 + 1 : sigma_s = 44.9(6.4) MeV Refs. [102-108], (450)"),
    "HRKM-21": ("CONTESTED", "Hoferichter, Ruiz de Elvira, Kubis, Meissner, "
                "arXiv:1506.04142v2 (PRL 115, 092301), Eq. (21), p.4",
                "we obtain sigma_piN = (59.1 +- 1.9 +- 3.0) MeV = (59.1 +- 3.5) MeV"),
    "FLAG-def": ("READ", "FLAG 2024 arXiv:2411.04268v3 Eqs. (431)-(433) p.260 and "
                 "Sec. 10.4.2 p.267",
                 "The sigma_piN,s,c give the shift in M_N due to nonzero light-, "
                 "strange- and charm-quark masses."),
    "EOS-SVZ": ("READ", "Ellis, Olive, Savage, arXiv:0801.3656v2 (PRD 77, 065026), "
                "Eqs. (10) and (12), p.5 (SVZ PLB 78, 443 (1978) CITED)",
                "f_N/m_N = sum_{q=u,d,s} f_Tq alpha_3q/m_q + (2/27) f_TG "
                "sum_{q=c,b,t} alpha_3q/m_q ... f_TG = 1 - sum_{q=u,d,s} f_Tq (12)"),
    "HRKM-24": ("READ", "Hoferichter et al., arXiv:1506.04142v2, Eq. (24), p.5",
                "sum_{q=u,...,t} f_q^N = 2/9 + 7/9 (f_u^N + f_d^N + f_s^N) = "
                "0.305 +- 0.009"),
    "Ji-cancel": ("READ", "X. Ji, arXiv:hep-ph/9410274 (PRL 74, 1071), after Eq. (25), p.5",
                  "Note that the heavy quarks do contribute to the mass term, the "
                  "kinetic and potential energy term, and the trace anomaly term. "
                  "However, the contributions cancel each other in the limit of "
                  "m_f -> infinity"),
    "Ji-eighth": ("READ", "X. Ji, arXiv:hep-ph/9410274, Table I p.9 and bullet p.7",
                  "The quark mass term accounts for about 1/8 of the nucleon mass. "
                  "About half of which or more is carried by the strange quark."),
    "chiQCD": ("READ", "Yang et al. (chiQCD), arXiv:1808.08677v2 (PRL 121, 212001), "
               "abstract p.1 and p.5 (the abstract and p.5 disagree on quark and "
               "glue energy, 33/37 % against 32/36 %: recorded, not repaired)",
               "A quarter of the trace anomaly gives a 23(1)(1)% contribution to "
               "the proton mass based on the sum rule, given 9(2)(1)% contribution "
               "from the u, d, and s quark scalar condensates."),
    # ----------------------------------------------------------- information
    "Landauer": ("READ", "Lloyd, arXiv:quant-ph/9908043v3, Box pp.8-9; Bennett, "
                 "arXiv:physics/0210005v2, pp.1 and 4 (Landauer, IBM J. Res. Dev. "
                 "5, 183 (1961) CITED)",
                 "irreversible, many-to-one operations such as AND or ERASE "
                 "require dissipation at least k_B ln 2 for each bit of "
                 "information lost (Lloyd p.9); 'This is an irreversible entropy "
                 "increase of k ln 2' (Bennett p.4)"),
    "Bekenstein": ("READ", "Bekenstein, arXiv:quant-ph/0404042v1, Eq. (1) p.1 "
                   "(PRD 23, 287 (1981) CITED); bit form Lloyd "
                   "arXiv:quant-ph/9908043v3 p.7",
                   "S <= 2 pi E R / hbar c. (1)  [k_B = 1];  'The amount of "
                   "information that can be registered by a physical system is "
                   "I = S(E)/k_B ln 2' (Lloyd p.7)"),
    "Braunstein": ("NOT-FOUND", "S. L. Braunstein, 'A fun talk on teleportation' "
                   "(egress-blocked; not opened)",
                   "NOT QUOTED -- page could not be fetched; figure known only "
                   "from a search-engine summary"),
    "Leicester": ("NOT-FOUND", "Nelms, Roberts, Thomas, Starkey, J. Phys. Special "
                  "Topics P4_4 (2013) (egress-blocked; not opened)",
                  "NOT QUOTED -- page could not be fetched; figure known only "
                  "from search summaries (ScienceDaily/phys.org 2013)"),
}

# (source key, the numeral as the source prints it, the value this file uses).
# The selftest checks that each numeral occurs in its source's held text and
# that it parses to exactly the value used.
PINS = (
    ("FLAG-447", "60.9", 60.9), ("FLAG-448", "42.2", 42.2),
    ("FLAG-449", "41.0", 41.0), ("FLAG-450", "44.9", 44.9),
    ("HRKM-21", "59.1", 59.1), ("HRKM-24", "0.305", 0.305),
    ("chiQCD", "9(2)(1)%", 9.0), ("chiQCD", "23(1)(1)%", 23.0),
    ("RS96-esph", "1.56", 1.56), ("RS96-esph", "2.72", 2.72),
    ("TW-FFS-esph", "9.11", 9.11), ("TW-FFS-esph", "9.08", 9.08),
    ("TW-FFS-esph", "4.75", 4.75), ("TW-FFS-esph", "1.31", 1.31),
    ("TW-FFS-esph", "0.60", 0.60), ("TW-claim", "9.0 TeV", 9.0),
    ("DR-Tc", "159.5", 159.5), ("DRT-rate", "131.7", 131.7),
    ("DRT-rate", "(18 +/- 3)", 18.0), ("CMS", "0.021", 0.021),
    ("TW-size", "1/29.7", 29.7), ("TW-size", "1/30", 30.0),
    ("FLAG-tension", "2.7 sigma", 2.7),
)

SIGMA_PIN_2P1P1 = 60.9          # MeV  READ          FLAG-447
SIGMA_PIN_2P1 = 42.2            # MeV  CONTESTED     FLAG-448
SIGMA_S_2P1P1 = 41.0            # MeV  READ          FLAG-449
SIGMA_S_2P1 = 44.9              # MeV  READ          FLAG-450
SIGMA_PIN_ROY_STEINER = 59.1    # MeV  CONTESTED     HRKM-21
COUPLING_SUM_HRKM = 0.305       # READ               HRKM-24
CHIQCD_QUARK_CONDENSATE = 9.0   # %    READ          chiQCD
CHIQCD_QUARTER_ANOMALY = 23.0   # %    READ          chiQCD
JI_QUARK_MASS_TERM = Fraction(1, 8)   # "about 1/8"  READ  Ji-eighth
B_KM_RANGE = (1.56, 2.72)       # READ               RS96-esph
TW_B_TERMS = (1.31, 0.60)       # READ               TW-FFS-esph
TW_PREFACTOR_TEV = 4.75         # READ, rounded (section 4 check)
E_SPH_TEV = {"Tye-Wong, pure SU(2)": 9.11, "Funakubo-Fuyuto-Senaha": 9.08,
             "Tye-Wong, with U(1)": 9.0}                 # READ
E_SPH_USED = "Funakubo-Fuyuto-Senaha"
T_C_GEV = 159.5                 # READ  DR-Tc, the abstract's figure
T_FREEZE_GEV = 131.7            # READ  DRT-rate
RATE_COEFF_SYMM = 18.0          # READ  DRT-rate, Gamma/T^4 = 18 alpha_W^5
CMS_PEF_BOUND = 0.021           # READ  CMS
TW_ALPHA_INV = (29.7, 30.0)     # READ  TW-size, the two pairings

# fragments quoted in this module's docstring, each against its source
QUOTED = (
    ("MRM-phi", "the masses of the W+/- and Z0 weak vector bosons and the "
                "fermions are proportional to phi"),
    ("FLAG-def", "The sigma_piN,s,c give the shift in M_N due to nonzero "
                 "light-, strange- and charm-quark masses"),
    ("Ji-cancel", "the contributions cancel each other in the limit of m_f -> "
                  "infinity"),
    ("Ji-eighth", "about 1/8"),
    ("RS96-sel", "Delta N_e = Delta N_mu = Delta N_tau = (1/3) Delta B ; (B - L) "
                 "is conserved while (B + L) is violated"),
    ("DRT-vev", "approximately zero"),
    ("MRM-SM", "EWBG is unable to explain the observed baryon asymmetry within "
               "the SM alone"),
    ("RS96-sel", "(B - L) is conserved"),
    ("FLAG-tension", "there is now a 2.7 sigma difference between the N_f = 2 + "
                     "1 and N_f = 2 + 1 + 1 FLAG averages"),
)

# ===================================================================== M65-1
def vev_gev():
    """v, asked of higgs.  From G_F: NAMED-NOT-READ."""
    return higgs.vev()


def yukawa(m_mev, v_gev=None):
    """y_f = sqrt(2) m_f / v.  H-TREE.  Inherits v's NAMED-NOT-READ."""
    v = vev_gev() if v_gev is None else v_gev
    return math.sqrt(2.0) * (m_mev / 1000.0) / v


def yukawas(masses=None):
    masses = MASS_MEV if masses is None else masses
    return {f: yukawa(masses[f]) for f in CHARGED_FERMIONS}


def consideration_holds(masses=None):
    """M's consideration, computed.  H-TREE: m_f = y_f v/sqrt(2), so any
    fermion of the payload with m_f > 0 forces phi != 0 where it is.  The
    payload's fermions are e, u, d.  Returns True iff one of them is massive
    in the capture."""
    masses = MASS_MEV if masses is None else masses
    return any(masses[f] > 0.0 for f in ("e", "u", "d"))


#: THE VEV IS THE CONSTANT SOLUTION.  higgs.py: "A VEV is a constant field, so
#: d_m phi = 0" -- the premise VEV_SATURATES_NEC is proved on.  Uniform where
#: nothing sources it (higgs caveat (b), as corrected by DOCKET 63 F3).
VEV_IS_UNIFORM = higgs.VEV_SATURATES_NEC
CONSIDERATION_HOLDS = consideration_holds()
#: True everywhere with or without the elements, so it singles out no place.
CONSIDERATION_DISCRIMINATES = not VEV_IS_UNIFORM


def source_sign_scan(eps_values=(Fraction(-1, 2), Fraction(-1, 10), Fraction(-1, 1000),
                                 Fraction(1, 1000), Fraction(1, 10), Fraction(1, 2))):
    """[(eps, source rest energy / rho_EW)] from excite.holding_terms, exact."""
    return [(e, excite.holding_terms(e)[0]) for e in eps_values]


#: A source of positive rest energy holds only eps > 0: phi = v(1 - eps) < v.
SOURCE_CAN_RAISE_VEV = any(s > 0 and e < 0 for e, s in source_sign_scan())


def field_switched_on_by_arrival(vev_uniform=None, present=None, d15=None,
                                 d16=None):
    """C1.  Arrival switches the field on only if it was off at the seat, or
    if a sourceless arrival could displace it.  The first is refuted by M65-1
    (present, uniform), the second by D15 and D16 together."""
    vev_uniform = VEV_IS_UNIFORM if vev_uniform is None else vev_uniform
    present = CONSIDERATION_HOLDS if present is None else present
    d15 = excite.TAIL_RATE_IS_MASS if d15 is None else d15
    d16 = excite.DISPLACEMENT_IS_ULTRALOCAL if d16 is None else d16
    already_on = vev_uniform and present
    sourceless_change = not (d15 and d16)
    return (not already_on) or sourceless_change


FIELD_SWITCHED_ON_BY_ARRIVAL = field_switched_on_by_arrival()

# ===================================================================== M65-2
PAYLOAD_KG = inspect.signature(stock.feedstock_kg).parameters["payload_kg"].default
COMPOSITION = stock.HUMAN
Z_OF = gravity.symbol_to_Z()                                     # READ, AME2020


def mass_number(el, shift=Fraction(0)):
    """A_e on H-A: the nearest integer to the standard atomic weight."""
    return Fraction(round(stock.ATOMIC_MASS[el])) + shift


def counts(payload_kg=None, comp=None, a_shift=Fraction(0)):
    """Exact rational counts over the listed elements.  Returns floats for
    B, N_e, N_p, N_n, and the listed mass fraction.  u and the atomic weights
    are NAMED-NOT-READ; Z is READ."""
    payload_kg = PAYLOAD_KG if payload_kg is None else payload_kg
    comp = COMPOSITION if comp is None else comp
    M = Fraction(repr(float(payload_kg)))
    u = Fraction(repr(U_KG))
    B = Ne = Fraction(0)
    for el, f in comp.items():
        atoms = Fraction(repr(f)) * M / (Fraction(repr(stock.ATOMIC_MASS[el])) * u)
        B += atoms * mass_number(el, a_shift)
        Ne += atoms * Z_OF[el]
    listed = sum(Fraction(repr(f)) for f in comp.values())
    return {"B": float(B), "N_e": float(Ne), "N_p": float(Ne),
            "N_n": float(B - Ne), "B_minus_L": float(B - Ne),
            "listed": float(listed), "unlisted": float(1 - listed)}


COUNTS = counts()


def valence_fractions(masses=None):
    """(proton, neutron): (2m_u + m_d)/m_p and (m_u + 2m_d)/m_n.  READ inputs."""
    m = MASS_MEV if masses is None else masses
    return ((2 * m["u"] + m["d"]) / m["p"], (m["u"] + 2 * m["d"]) / m["n"])


def sigma_fraction(sigma_pin, sigma_s):
    """f_l = (sigma_piN + sigma_s)/m_N -- the Feynman-Hellmann quark-mass part."""
    return (sigma_pin + sigma_s) / M_N_MEV


SIGMA_MEASURES = {
    "FLAG 2+1+1": (SIGMA_PIN_2P1P1, SIGMA_S_2P1P1, "READ"),
    "FLAG 2+1": (SIGMA_PIN_2P1, SIGMA_S_2P1, "CONTESTED"),
}
F_LIGHT = {k: sigma_fraction(a, b) for k, (a, b, _s) in SIGMA_MEASURES.items()}


def coupling_sum(f_l):
    """sum over six quarks = 2/9 + (7/9) f_l.  EXACT over Fraction."""
    return Fraction(2, 9) + Fraction(7, 9) * f_l


def svz_heavy_sum(f_l):
    """3 x (2/27)(1 - f_l), the three heavy quarks by SVZ.  EXACT."""
    return 3 * Fraction(2, 27) * (1 - f_l)


def payload_masses(c=None, masses=None):
    """{line: kg} of the payload's rest-mass bookkeeping, closing exactly.
    nucleon rest masses + electron rest masses - binding = listed payload."""
    c = COUNTS if c is None else c
    m = MASS_MEV if masses is None else masses
    nuc = (c["N_p"] * m["p"] + c["N_n"] * m["n"]) * MEV_KG
    ele = c["N_e"] * m["e"] * MEV_KG
    listed = PAYLOAD_KG * c["listed"]
    return {"nucleon rest": nuc, "electron rest": ele,
            "binding (closure)": nuc + ele - listed, "listed payload": listed,
            "unlisted (H-LIST)": PAYLOAD_KG * c["unlisted"]}


def binding_sensitivity_kg(step=Fraction(1, 100)):
    """How far the binding closure moves when every mean nucleon number rises
    by `step`: the one figure H-A moves materially."""
    return (payload_masses(counts(a_shift=step))["binding (closure)"]
            - payload_masses()["binding (closure)"])


def share_rows(c=None):
    """[(measure, status, fraction of the payload, what it is)].  Electrons
    first, then each nucleon measure on its own.  NEVER SUMMED ACROSS ROWS."""
    pm = payload_masses(c)
    nuc, M = pm["nucleon rest"], PAYLOAD_KG
    cc = COUNTS if c is None else c
    vp, vn = valence_fractions()
    val_kg = (cc["N_p"] * (2 * MASS_MEV["u"] + MASS_MEV["d"])
              + cc["N_n"] * (MASS_MEV["u"] + 2 * MASS_MEV["d"])) * MEV_KG
    rows = [("electrons (all Higgs-given, H-TREE)", "MEASURED from READ",
             pm["electron rest"] / M, "electron rest mass"),
            ("nucleons: naive valence sum", "MEASURED from READ",
             val_kg / M, "valence current-quark masses only")]
    for k, (_a, _b, st) in SIGMA_MEASURES.items():
        rows.append(("nucleons: sigma terms, %s" % k, st,
                     F_LIGHT[k] * nuc / M, "quark-mass part (Feynman-Hellmann)"))
    rows.append(("nucleons: chiQCD u,d,s condensate", "READ",
                 CHIQCD_QUARK_CONDENSATE / 100.0 * nuc / M, "lattice, proton"))
    rows.append(("nucleons: Ji quark mass term", "READ",
                 float(JI_QUARK_MASS_TERM) * nuc / M, "'about 1/8'"))
    for k in SIGMA_MEASURES:
        rows.append(("nucleons: six-quark coupling, %s" % k, "CONTESTED as mass",
                     float(coupling_sum(Fraction(F_LIGHT[k]))) * nuc / M,
                     "coupling incl. heavy-quark trace anomaly"))
    rows.append(("nucleons: six-quark coupling, Hoferichter", "CONTESTED as mass",
                 COUPLING_SUM_HRKM * nuc / M, "0.305(9), READ as a coupling"))
    return rows


def higgs_share_bound(rows=None, read_only=False):
    """The LARGEST reading, electrons plus one nucleon measure -- an upper
    bound, never a share.  read_only drops every CONTESTED row."""
    rows = share_rows() if rows is None else rows
    ele = rows[0][2]
    nucs = [r[2] for r in rows[1:]
            if not (read_only and r[1].startswith("CONTESTED"))]
    return ele + max(nucs)


HIGGS_SHARE_BOUND_ALL = higgs_share_bound()
HIGGS_SHARE_BOUND_READ = higgs_share_bound(read_only=True)
#: C2.  The charitable reading of "atomic mass forms": MOST of it.
HIGGS_SUPPLIES_MOST_ATOMIC_MASS = HIGGS_SHARE_BOUND_ALL >= 0.5
#: Would C2 still refuse on the READ rows alone?  (It must, or it is
#: contested-only and cannot carry a refusal.)
C2_CONTESTED_ONLY = not (HIGGS_SHARE_BOUND_READ < 0.5)

# ===================================================================== M65-3
def rest_energy_j(kg=None):
    return warpfolder.rest_energy_j(PAYLOAD_KG if kg is None else kg)


T_CMB = permute.T_CMB                  # CITED (Fixsen 2009 per permute.py)
R_BEKENSTEIN_M = 1.0                   # H-R


def landauer_bits(E=None, T=None):
    """Erased bits whose MINIMUM heat equals E, at T."""
    E = rest_energy_j() if E is None else E
    T = T_CMB if T is None else T
    return E / nopath.landauer_energy(1.0, T)


def bekenstein_bits(E=None, R=None):
    E = rest_energy_j() if E is None else E
    R = R_BEKENSTEIN_M if R is None else R
    return nopath.bekenstein_bits(R, E)


def bek_over_landauer_closed(R=None, T=None):
    """2 pi R k_B T/(hbar c): the ratio of the two counts, with no M in it."""
    R = R_BEKENSTEIN_M if R is None else R
    T = T_CMB if T is None else T
    return 2.0 * math.pi * R * nopath.KB * T / (nopath.HBAR * nopath.C)


def break_even_radius_m(T=None):
    T = T_CMB if T is None else T
    return nopath.HBAR * nopath.C / (2.0 * math.pi * nopath.KB * T)


#: C4.  A bit has no energy of its own: Landauer prices erasure only
#: (nopath.LANDAUER_IS_THE_WEAKER_HALF, READ Lloyd/Bennett).
INFORMATION_HAS_INTRINSIC_ENERGY = not nopath.LANDAUER_IS_THE_WEAKER_HALF

# ===================================================================== M65-4
# Every Standard Model Yukawa term, as its field content with (B, L) charges.
# A bar is the conjugate field and carries the opposite charges.  (H carries
# none.)  The selftest computes the total charge of each term.
_Q = {"Q": (Fraction(1, 3), 0), "u_R": (Fraction(1, 3), 0),
      "d_R": (Fraction(1, 3), 0), "L": (0, 1), "e_R": (0, 1), "H": (0, 0)}
YUKAWA_TERMS = {
    "y_e  Lbar H e_R": (("L", -1), ("H", +1), ("e_R", +1)),
    "y_d  Qbar H d_R": (("Q", -1), ("H", +1), ("d_R", +1)),
    "y_u  Qbar Hc u_R": (("Q", -1), ("H", -1), ("u_R", +1)),
}
#: The 't Hooft vertex per the READ rule: one (q q q l) per generation.
THOOFT_VERTEX = tuple([("Q", +1)] * 3 * N_F + [("L", +1)] * N_F)


def term_charge(term):
    """(B, L) of a product of fields; sign +1 field, -1 conjugate."""
    B = sum(s * _Q[f][0] for f, s in term)
    L = sum(s * _Q[f][1] for f, s in term)
    return B, L


#: C3.  Some Higgs coupling carries B or L?  Computed, term by term.
HIGGS_COUPLING_CREATES_FERMIONS = any(term_charge(t) != (0, 0)
                                      for t in YUKAWA_TERMS.values())
#: And the anomaly vertex does, by exactly N_F each: the READ rule reproduced.
THOOFT_DELTA_B_L = term_charge(THOOFT_VERTEX)


def mu_min_mev():
    """The least nuclear mass per nucleon in the AME2020 capture (measured
    rows), (A u + Delta - Z m_e)/A.  Electron binding is dropped, which only
    lowers the figure, so the floor built on it stays a floor.  Returns
    (MeV per nucleon, symbol, A)."""
    best = None
    for Z, _N, A, sym, d_kev, q in gravity.nuclides():
        if q != "M" or A < 1:
            continue
        mu = (A * U_MEV + d_kev / 1000.0 - Z * MASS_MEV["e"]) / A
        if best is None or mu < best[0]:
            best = (mu, sym, A)
    return best


MU_MIN = mu_min_mev()


def pair_floor_j(c=None):
    """Mc^2 + B mu_min c^2: the least energy that makes the payload from
    energy with B and L conserved.  THEOREM on B, L conservation."""
    c = COUNTS if c is None else c
    return rest_energy_j() + c["B"] * MU_MIN[0] * MEV_J


def alpha_w(m_w_gev=None, v_gev=None):
    """g = 2 m_W / v, alpha_W = g^2 / 4 pi.  m_W READ; v NAMED-NOT-READ."""
    m_w = M_W_GEV if m_w_gev is None else m_w_gev
    v = vev_gev() if v_gev is None else v_gev
    g = 2.0 * m_w / v
    return g * g / (4.0 * math.pi), g


def log10_suppression(aw=None):
    """log10 exp(-4 pi / alpha_W), exactly the source's form."""
    aw = alpha_w()[0] if aw is None else aw
    return -(4.0 * math.pi / aw) / math.log(10.0)


def log10_suppression_g(g=None):
    """log10 exp(-16 pi^2 / g^2): the second form, computed independently."""
    g = alpha_w()[1] if g is None else g
    return -(16.0 * math.pi ** 2 / g ** 2) / math.log(10.0)


def transitions_needed(c=None):
    c = COUNTS if c is None else c
    return math.ceil(c["B"] / N_F)


def log10_attempts_times_prefactor(c=None):
    return math.log10(transitions_needed(c)) - log10_suppression()


def esph_formula_tev(B_fn):
    """(2 m_W / alpha_W) x B, TeV."""
    aw, _g = alpha_w()
    return 2.0 * M_W_GEV / aw * B_fn / 1000.0


def esph_over_three_baryons(tev):
    return tev * 1e6 / (N_F * MASS_MEV["p"])


def barrier_total_over_mc2(c=None, tev=None):
    tev = E_SPH_TEV[E_SPH_USED] if tev is None else tev
    return transitions_needed(c) * tev * 1e6 * MEV_J / rest_energy_j()


def extra_leptons(c=None):
    """Leptons the sphaleron route makes beyond the payload's electrons:
    N_F x transitions - N_e.  B - L conservation makes it N_n (to rounding)."""
    c = COUNTS if c is None else c
    return N_F * transitions_needed(c) - c["N_e"]


def electron_family_shortfall(c=None):
    """H-FLAV ONLY.  Sphalerons give Delta N_e = Delta B/3 (READ); the payload
    holds N_e electrons.  Carries no verdict."""
    c = COUNTS if c is None else c
    return c["N_e"] - transitions_needed(c)


def t_kelvin(gev):
    return gev * higgs.GEV_IN_J / nopath.KB


def symmetric_rate_over_t4(aw=None):
    aw = alpha_w()[0] if aw is None else aw
    return RATE_COEFF_SYMM * aw ** 5


#: The collider exponent, as the READ has it.  Never resolved here.
COLLIDER_RATE_STATUS = "CONTESTED"
MASS_FORMS_FROM_ENERGY_WITH_BL_CONSERVED_WITHOUT_ANTIMATTER = False
HOT_ROUTE_HAS_YUKAWA_MASSES = not warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY

# ===================================================================== M65-5
#: (id, link, pinned boolean name, owner, status, contested_only).  The value
#: is the value of the pinned boolean: True means the link the mechanism needs
#: HOLDS on this count.
COUNTS_ON_THE_MECHANISM = (
    ("C1", "L1 triggers the higgs field", "FIELD_SWITCHED_ON_BY_ARRIVAL",
     ("excite", "TAIL_RATE_IS_MASS"), "THEOREM (D15, D16; H-TREE)", False),
    ("C2", "L2 atomic mass forms", "HIGGS_SUPPLIES_MOST_ATOMIC_MASS",
     ("massform", "HIGGS_SHARE_BOUND_READ"), "MEASURED from READ", C2_CONTESTED_ONLY),
    ("C3", "L2 atomic mass forms", "HIGGS_COUPLING_CREATES_FERMIONS",
     ("massform", "YUKAWA_TERMS"), "THEOREM (perturbative SM)", False),
    ("C4", "L3 from the information", "INFORMATION_HAS_INTRINSIC_ENERGY",
     ("nopath", "LANDAUER_IS_THE_WEAKER_HALF"), "READ (Lloyd, Bennett)", False),
)


def derive_verdict(values, contested=None):
    """values: {count id: bool, True = the link holds on that count}.
    contested: {count id: bool, True = the count rests on a CONTESTED figure
    alone}.  REFUSED iff some non-contested count fails its link; OPEN iff only
    contested counts fail; STANDS iff none fails."""
    contested = {} if contested is None else contested
    failing = [k for k in sorted(values) if not values[k]]
    carried = [k for k in failing if not contested.get(k, False)]
    if carried:
        return "REFUSED", carried
    if failing:
        return "OPEN", failing
    return "STANDS", []


def mechanism_values():
    g = globals()
    return {cid: bool(g[name]) for cid, _l, name, _o, _s, _c in COUNTS_ON_THE_MECHANISM}


def mechanism_contested():
    return {cid: c for cid, _l, _n, _o, _s, c in COUNTS_ON_THE_MECHANISM}


MECHANISM_VERDICT = derive_verdict(mechanism_values(), mechanism_contested())


def derive_consideration(holds=None, discriminates=None):
    holds = CONSIDERATION_HOLDS if holds is None else holds
    discriminates = CONSIDERATION_DISCRIMINATES if discriminates is None else discriminates
    if not holds:
        return "NOT ESTABLISHED"
    return "TRUE" if discriminates else "TRUE, AND DISCRIMINATES NOTHING"


CONSIDERATION_VERDICT = derive_consideration()

SURVIVES = (
    ("reconstruction from destination stock",
     "stockgate.GATE is the condition; transit.CARRIES_SUBSTANCE = %s.  No mass "
     "forms at the seat; the stock's masses were already given by the uniform "
     "vev.  The Higgs's part is a precondition met everywhere -- M's "
     "consideration -- not a trigger.  S5 and D25 unchanged."
     % transit.CARRIES_SUBSTANCE),
    ("the sphaleron route",
     "the one Standard Model process in which the Higgs field's structure "
     "(E_sph = (4 pi v/g) B) turns energy into baryons.  PRICED in M65-4; the "
     "collider exponent is %s and is not resolved." % COLLIDER_RATE_STATUS),
)
RECONSTRUCTION_SURVIVES = (not transit.CARRIES_SUBSTANCE) and bool(stockgate.GATE)
SPHALERON_ROUTE_PRICED = True

# ------------------------------------------------------------------ refusals
PRINTS_ONE_HIGGS_SHARE = False                              # 1
RESOLVES_COLLIDER_DISPUTE = False                           # 2
REFUSES_ON_A_CONTESTED_FIGURE_ALONE = False                 # 3
PRINTS_A_SPHALERON_RATE_WITHOUT_PREFACTOR = False           # 4
CLAIMS_EXACT_ZERO_VEV_ABOVE_TC = False                      # 5
QUOTES_A_HUMAN_INFORMATION_CONTENT = False                  # 6
TREATS_LANDAUER_AS_BIT_ENERGY = INFORMATION_HAS_INTRINSIC_ENERGY   # 7
COUNTS_HEAVY_QUARK_COUPLING_AS_HIGGS_MADE_MASS = False      # 8
DISMISSES_THE_SPHALERON_ROUTE = not SPHALERON_ROUTE_PRICED  # 9
HOLDS_A_FIGURE_WITHOUT_ITS_SOURCE_TEXT = False              # 10
USES_THE_RETIRED_STATUS_WORD = False                        # 11
REFUSAL_FLAGS = (
    (1, "PRINTS_ONE_HIGGS_SHARE"), (2, "RESOLVES_COLLIDER_DISPUTE"),
    (3, "REFUSES_ON_A_CONTESTED_FIGURE_ALONE"),
    (4, "PRINTS_A_SPHALERON_RATE_WITHOUT_PREFACTOR"),
    (5, "CLAIMS_EXACT_ZERO_VEV_ABOVE_TC"),
    (6, "QUOTES_A_HUMAN_INFORMATION_CONTENT"),
    (7, "TREATS_LANDAUER_AS_BIT_ENERGY"),
    (8, "COUNTS_HEAVY_QUARK_COUPLING_AS_HIGGS_MADE_MASS"),
    (9, "DISMISSES_THE_SPHALERON_ROUTE"),
    (10, "HOLDS_A_FIGURE_WITHOUT_ITS_SOURCE_TEXT"),
    (11, "USES_THE_RETIRED_STATUS_WORD"))
REFUSALS = len({n for n, _ in REFUSAL_FLAGS})
NOTHING_IS_REPAIRED = True
EDITS_A_PEER = False

# ------------------------------------------------------------- proposed rows
PROPOSED_ROWS = (
    ("D27", "DEMAND",
     "M's consideration, computed: fermion masses are proportional to phi "
     "(READ, 1206.2942), so wherever the payload's elements exist with their "
     "measured masses the vev is nonzero there.  The vev is uniform, so the "
     "condition holds everywhere and singles out no seat; arrival switches "
     "nothing on, and a change at the seat needs a local source (D15, D16) of "
     "positive rest energy, which can only LOWER phi (D20's source term is "
     "negative for eps < 0)",
     "THEOREM", ("massform", "CONSIDERATION_HOLDS"),
     "a fermion mass not proportional to phi at tree level (H-TREE fails), or a "
     "failure of D15/D16's hypotheses; FIELD_SWITCHED_ON_BY_ARRIVAL is the "
     "boolean that would flip"),
    ("D28", "DEMAND",
     "Forming the payload from energy with B and L conserved costs at least "
     "Mc^2 + B mu_min c^2 (mu_min the least nuclear mass per nucleon, AME2020) "
     "and leaves B units of antibaryon number to be held apart; B - L of the "
     "payload is N_n != 0, so every B-L-conserving route must also emit N_n "
     "leptons the payload does not keep",
     "THEOREM", ("massform", "pair_floor_j"),
     "B - L violation (a Majorana neutrino mass; H-BL), or a counted payload "
     "with N_n = 0; the numbers move with gravity.U_KG and stock.ATOMIC_MASS, "
     "both NAMED-NOT-READ"),
    ("S10", "SUPPLY",
     "M's mechanism, 'information hits the seat, triggers the higgs field, "
     "atomic mass forms', as a supply of payload mass.  REFUSED, gap None, on "
     "four counts each alone sufficient and none contested-only: C1 the field "
     "is already on (D27); C2 the Higgs supplies less than half of atomic mass "
     "on every reading (READ bound alone); C3 no Higgs coupling carries B or L; "
     "C4 a bit has no energy of its own (nopath's Landauer)",
     "REFUSED", ("massform", "MECHANISM_VERDICT"),
     "any one count reversed does NOT move it (each alone suffices); all four "
     "reversed would -- e.g. a READ sigma term above half m_N AND a B-carrying "
     "Higgs coupling AND an intrinsic bit energy AND a sourceless displacement"),
    ("S11", "SUPPLY",
     "The sphaleron route: the one SM process in which the Higgs field's "
     "structure turns energy into baryons.  Zero temperature: exp(-4 pi/"
     "alpha_W) per transition, alpha_W from READ m_W and v; B/3 transitions; "
     "E_sph ~ 9 TeV per transition (READ), ~3.2e3 x the 3 baryons' rest "
     "energy.  Above T_c: unsuppressed, vev approximately zero, no Yukawa "
     "masses.  Collider energies: CONTESTED",
     "OPEN", ("massform", "SPHALERON_ROUTE_PRICED"),
     "a READ prefactor (turns the exponent into a rate); a settlement of the "
     "collider-energy dispute (Tye-Wong against Bezrukov et al. and Funakubo "
     "et al.); a READ G_F (lifts alpha_W's NAMED-NOT-READ)"),
    ("S5 (note)", "SUPPLY",
     "APPEND to S5's note: DOCKET 65 -- reconstruction from destination stock "
     "survives M's mechanism: no mass forms at the seat and the Higgs plays no "
     "triggering role (massform.RECONSTRUCTION_SURVIVES)",
     "OPEN (unchanged)", ("massform", "RECONSTRUCTION_SURVIVES"),
     "nothing in DOCKET 65; S5's own owed items stand"),
)
#: Not opened, and why (one row per question): the Higgs share alone gates no
#: price on the board and is C2 inside S10; the Landauer/Bekenstein counts are
#: C4 inside S10; the flavour sub-count rests on H-FLAV and carries no verdict.
NOT_OPENED = ("the Higgs share (C2 of S10)",
              "the information counts (C4 of S10)",
              "the electron-family shortfall (H-FLAV only)")


# ================================================================ doc figures
def _e(x, p):
    """%.pe with the exponent written as the docstring writes it: 6.2913e18."""
    return re.sub(r"e([+-])0*(\d)",
                  lambda m: "e" + ("-" if m.group(1) == "-" else "") + m.group(2),
                  "%.*e" % (p, x))


def doc_figures():
    """[(label, the string the docstring prints, the value computed now)].
    The selftest checks every printed string is regenerated from the value."""
    c = COUNTS
    vp, vn = valence_fractions()
    aw, _g = alpha_w()
    return [
        ("electron share", _e(share_rows()[0][2], 3)),
        ("f_l FLAG 2+1+1", "%.2f %%" % (100 * F_LIGHT["FLAG 2+1+1"])),
        ("f_l FLAG 2+1", "%.2f %%" % (100 * F_LIGHT["FLAG 2+1"])),
        ("valence p", "%.3f %%" % (100 * vp)),
        ("valence n", "%.3f %%" % (100 * vn)),
        ("coupling 2+1+1", "%.4f" % float(coupling_sum(Fraction(F_LIGHT["FLAG 2+1+1"])))),
        ("coupling 2+1", "%.4f" % float(coupling_sum(Fraction(F_LIGHT["FLAG 2+1"])))),
        ("Mc^2", _e(rest_energy_j(), 4) + " J"),
        ("megatons", "%.0f megatons" % warpfolder.megatons(rest_energy_j())),
        ("Landauer bits", _e(landauer_bits(), 4)),
        ("per bit", _e(nopath.landauer_energy(1.0, T_CMB), 3) + " J per bit"),
        ("Bekenstein bits", _e(bekenstein_bits(), 4)),
        ("ratio", "%.0f" % bek_over_landauer_closed()),
        ("break-even", "%.3f mm" % (1000 * break_even_radius_m())),
        ("B", _e(c["B"], 4)), ("N_e", _e(c["N_e"], 4)),
        ("N_n", _e(c["N_n"], 4)),
        ("B/(M/m_p)", "%.4f" % (c["B"] / warpfolder.baryons_in(PAYLOAD_KG))),
        ("pair floor", "%.4f Mc^2" % (pair_floor_j() / rest_energy_j())),
        ("mu_min", "%.4f MeV" % MU_MIN[0]),
        ("1/alpha_W", "1/%.2f" % (1.0 / aw)),
        ("suppression", "10^%.2f" % log10_suppression()),
        ("transitions", _e(transitions_needed(), 4)),
        ("attempts x prefactor", "10^%.2f" % log10_attempts_times_prefactor()),
        ("2 m_W/alpha_W", "%.3f TeV" % esph_formula_tev(1.0)),
        ("barrier ratio", "%.0f times" % esph_over_three_baryons(E_SPH_TEV[E_SPH_USED])),
        ("T_c kelvin", _e(t_kelvin(T_C_GEV), 3) + " K"),
        ("18 alpha^5", _e(symmetric_rate_over_t4(), 2)),
        ("barrier total", "%.0f Mc^2" % barrier_total_over_mc2()),
        ("y_t", "%.4f" % yukawas()["t"]), ("y_e", _e(yukawas()["e"], 3)),
        ("lambda_h", _e(excite.LAMBDA_H_READ_M, 3) + " m"),
        ("binding", "%.4f kg" % payload_masses()["binding (closure)"]),
        ("binding sensitivity", "%.4f kg" % binding_sensitivity_kg()),
        ("listed", "%.5f" % COUNTS["listed"]),
    ]


def _norm(s):
    return re.sub(r"\s+", " ", s)


def _doc_section(n):
    m = re.search(r"\n%d\.  [^\n]*\n=+\n(.*?)\n=+\n" % n, __doc__ or "", re.S)
    return m.group(1) if m else ""


def doc_refusal_numbers():
    return [int(k) for k in re.findall(r"(?m)^ {2,3}(\d+)\. ", _doc_section(7))]


def check_quotes(sources=None, quoted=None, pins=None, doc=None):
    """The misquote check.  Returns a list of failures (empty = clean):
    every QUOTED fragment is in its source's held text AND in the docstring;
    every PIN's numeral is in its source's text and parses to the value used."""
    sources = SOURCES if sources is None else sources
    quoted = QUOTED if quoted is None else quoted
    pins = PINS if pins is None else pins
    doc = _norm(__doc__ if doc is None else doc)
    bad = []
    for key, frag in quoted:
        if _norm(frag) not in _norm(sources[key][2]):
            bad.append(("not in source", key, frag))
        if _norm(frag) not in doc:
            bad.append(("not in docstring", key, frag))
    for key, numeral, value in pins:
        if numeral not in sources[key][2]:
            bad.append(("numeral not in source", key, numeral))
        tail = numeral[2:] if numeral.startswith("1/") else numeral
        num = re.search(r"\d+(?:\.\d+)?", tail)
        if num is None or float(num.group(0)) != value:
            bad.append(("numeral does not parse to the value", key, numeral))
    return bad


# ===================================================================== report
def _p(label, value, status=""):
    print("      %-46s %20s  %s" % (label, value, status))


def report():
    print(__doc__.split("=====", 1)[0].strip())
    print()
    print("=" * 79)
    print("M65-1  PRESENCE")
    print("=" * 79)
    v = vev_gev()
    _p("v = higgs.vev()", "%.6f GeV" % v, "NAMED-NOT-READ (G_F)")
    print("      %-10s %16s %18s" % ("fermion", "m (MeV, READ)", "y = sqrt2 m/v"))
    for f, y in yukawas().items():
        print("      %-10s %16.9g %18.6e" % (f, MASS_MEV[f], y))
    _p("consideration: massive e, u, d force phi != 0", CONSIDERATION_HOLDS,
       "THEOREM on H-TREE")
    _p("the vev is uniform (higgs.VEV_SATURATES_NEC)", VEV_IS_UNIFORM, "THEOREM")
    _p("so the condition singles out the seat", CONSIDERATION_DISCRIMINATES)
    _p("D15 excite.TAIL_RATE_IS_MASS", excite.TAIL_RATE_IS_MASS, "THEOREM")
    _p("D16 excite.DISPLACEMENT_IS_ULTRALOCAL", excite.DISPLACEMENT_IS_ULTRALOCAL,
       "THEOREM")
    _p("  tail length hbar/(m_h c)", _e(excite.LAMBDA_H_READ_M, 3) + " m", "READ m_h")
    print("      D20 source rest energy / rho_EW against eps (excite.holding_terms):")
    for e, s in source_sign_scan():
        print("        eps = %-8s  source = %+.6f" % (e, float(s)))
    _p("a positive source can RAISE the vev", SOURCE_CAN_RAISE_VEV, "THEOREM")
    _p("source/field -> 2/eps; eps x ratio at 1e-9",
       "%.9f" % (excite.holding_ratio(Fraction(1, 10 ** 9)) * Fraction(1, 10 ** 9)))
    _p("D19 excite.FLAT_DIRECTIONS_ARE_INERT", excite.FLAT_DIRECTIONS_ARE_INERT)
    print("      D18 excite.ELECTRON_MASS_IS_A_RULER = %r" % excite.ELECTRON_MASS_IS_A_RULER)
    _p("higgs.CANNOT_BE_SWITCHED_ON_IN_ONE_PLACE", higgs.CANNOT_BE_SWITCHED_ON_IN_ONE_PLACE,
       "WITHDRAWN (DOCKET 63 F3)")
    _p("Higgs quantum lifetime (excite)", excite.one_sig(excite.QUANTUM_LIFETIME_S) + " s")
    _p("Higgs quanta with total rest energy Mc^2",
       "%.4e" % (rest_energy_j() / (higgs.M_HIGGS * higgs.GEV_IN_J)))
    _p("C1 FIELD_SWITCHED_ON_BY_ARRIVAL", FIELD_SWITCHED_ON_BY_ARRIVAL)
    print()
    print("=" * 79)
    print("M65-2  SHARE   (stock.HUMAN at %.0f kg, asked of stock.feedstock_kg)"
          % PAYLOAD_KG)
    print("=" * 79)
    c = COUNTS
    for k in ("B", "N_e", "N_p", "N_n"):
        _p(k, "%.6e" % c[k], "MEASURED; u, A_r NAMED-NOT-READ; Z READ")
    _p("listed mass fraction (H-LIST)", "%.6f" % c["listed"])
    _p("binding closure moves per +0.01 in every A (H-A)", "%.6f kg" % binding_sensitivity_kg())
    for k, kg in payload_masses().items():
        _p(k, "%.6f kg" % kg)
    vp, vn = valence_fractions()
    _p("naive valence, proton (2m_u+m_d)/m_p", "%.4f %%" % (100 * vp), "READ inputs")
    _p("naive valence, neutron (m_u+2m_d)/m_n", "%.4f %%" % (100 * vn), "READ inputs")
    _p("m_N = (m_p+m_n)/2", "%.7f MeV" % M_N_MEV, "READ")
    for k, (a, b, st) in SIGMA_MEASURES.items():
        f = F_LIGHT[k]
        _p("f_l %s (%.1f + %.1f)/m_N" % (k, a, b), "%.4f %%" % (100 * f), st)
        _p("  SVZ heavy-quark coupling (2/9)(1-f_l)",
           "%.4f" % float(svz_heavy_sum(Fraction(f))), "CONTESTED as mass")
        _p("  six-quark coupling 2/9 + 7/9 f_l",
           "%.4f" % float(coupling_sum(Fraction(f))), "CONTESTED as mass")
        _p("  remainder 1 - f_l (QCD)", "%.4f %%" % (100 * (1 - f)))
    _p("sigma_piN, Roy-Steiner (alone)", "%.4f %%"
       % (100 * SIGMA_PIN_ROY_STEINER / M_N_MEV), "CONTESTED")
    print()
    print("      the payload, measure by measure -- NEVER SUMMED ACROSS ROWS")
    for name, st, frac, what in share_rows():
        print("      %-44s %11.4e  %-20s %s" % (name, frac, st, what))
    _p("largest reading, READ rows only", "%.4f" % HIGGS_SHARE_BOUND_READ, "bound")
    _p("largest reading, all rows", "%.4f" % HIGGS_SHARE_BOUND_ALL, "bound")
    _p("C2 HIGGS_SUPPLIES_MOST_ATOMIC_MASS", HIGGS_SUPPLIES_MOST_ATOMIC_MASS)
    print()
    print("=" * 79)
    print("M65-3  ENERGY")
    print("=" * 79)
    E = rest_energy_j()
    _p("Mc^2 (warpfolder.rest_energy_j)", "%.6e J" % E, "MEASURED")
    _p("  in megatons (warpfolder.megatons)", "%.1f" % warpfolder.megatons(E))
    _p("  with B, L conserved (section 4 floor)", "%.6e J" % pair_floor_j(), "THEOREM")
    _p("T_CMB (permute.T_CMB)", "%.4f K" % T_CMB, "CITED")
    _p("k_B T ln 2 (nopath.landauer_energy)", "%.6e J" % nopath.landauer_energy(1.0, T_CMB))
    _p("erased bits whose minimum heat = Mc^2", "%.6e" % landauer_bits(), "inherits CITED")
    _p("Bekenstein, E = Mc^2, R = 1 m (H-R)", "%.6e bits" % bekenstein_bits())
    _p("ratio (computed from the two counts)", "%.4f" % (bekenstein_bits() / landauer_bits()))
    _p("ratio 2 pi R k_B T/(hbar c), no M", "%.4f" % bek_over_landauer_closed())
    _p("break-even R = hbar c/(2 pi k_B T)", "%.6e m" % break_even_radius_m())
    _p("nopath.LANDAUER_IS_THE_WEAKER_HALF", nopath.LANDAUER_IS_THE_WEAKER_HALF)
    _p("nopath.BEKENSTEIN_IS_THE_ARGUMENT", nopath.BEKENSTEIN_IS_THE_ARGUMENT)
    _p("C4 INFORMATION_HAS_INTRINSIC_ENERGY", INFORMATION_HAS_INTRINSIC_ENERGY)
    print("      human information content: NOT-FOUND (Braunstein, Leicester); "
          "not quoted")
    print()
    print("=" * 79)
    print("M65-4  CONSERVATION")
    print("=" * 79)
    for name, t in YUKAWA_TERMS.items():
        _p("(B, L) of %s" % name, str(tuple(str(x) for x in term_charge(t))))
    _p("(B, L) of the 't Hooft vertex, N_F = %d" % N_F,
       str(tuple(str(x) for x in THOOFT_DELTA_B_L)), "READ rule reproduced")
    _p("C3 HIGGS_COUPLING_CREATES_FERMIONS", HIGGS_COUPLING_CREATES_FERMIONS)
    _p("B - L of the payload = N_n", "%.6e" % c["B_minus_L"])
    lb = lightest_baryon()
    _p("lightest baryon in the capture", "%s %.6f MeV" % lb, "READ")
    _p("mu_min, AME2020 measured (nuclear/nucleon)", "%.4f MeV (%d%s)"
       % (MU_MIN[0], MU_MIN[2], MU_MIN[1]))
    _p("pair floor / Mc^2", "%.6f" % (pair_floor_j() / E), "THEOREM")
    _p("mirror antipayload / Mc^2 (CPT)", "2", "THEOREM")
    _p("antibaryon number to be held apart", "%.6e" % c["B"])
    aw, g = alpha_w()
    _p("g = 2 m_W / v", "%.6f" % g, "inherits NAMED-NOT-READ")
    _p("alpha_W = g^2/4pi", "%.6f = 1/%.4f" % (aw, 1 / aw))
    _p("log10 exp(-4 pi/alpha_W)", "%.4f" % log10_suppression())
    _p("log10 exp(-16 pi^2/g^2)", "%.4f" % log10_suppression_g())
    _p("transitions needed ceil(B/N_F)", "%.6e" % transitions_needed())
    _p("log10 (attempts x prefactor) needed", "%.4f" % log10_attempts_times_prefactor())
    print("      NO RATE PRINTED: the prefactor was not read (refusal 4).")
    _p("2 m_W/alpha_W", "%.4f TeV" % esph_formula_tev(1.0))
    for B_ in B_KM_RANGE + (sum(TW_B_TERMS),):
        _p("  x B = %.2f" % B_, "%.4f TeV" % esph_formula_tev(B_))
    for k, tev in E_SPH_TEV.items():
        _p("E_sph READ, %s" % k, "%.2f TeV" % tev, "READ")
        _p("  / rest energy of %d baryons" % N_F, "%.1f" % esph_over_three_baryons(tev))
    _p("transitions x E_sph / Mc^2 (%s)" % E_SPH_USED, "%.1f" % barrier_total_over_mc2())
    _p("leptons beyond the payload", "%.6e" % extra_leptons(), "B - L conservation")
    _p("  H-FLAV only: electron-family shortfall", "%.6e" % electron_family_shortfall(),
       "carries no verdict")
    _p("T_c (1508.07161 abstract)", "%.1f GeV = %.4e K" % (T_C_GEV, t_kelvin(T_C_GEV)), "READ")
    _p("Gamma/T^4 = (18 +/- 3) alpha_W^5 here", "%.4e" % symmetric_rate_over_t4(),
       "coefficient READ; alpha_W inherits")
    _p("warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY",
       warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY)
    _p("  so the hot route has Yukawa masses", HOT_ROUTE_HAS_YUKAWA_MASSES)
    _p("freeze-out T*", "%.1f GeV" % T_FREEZE_GEV, "READ")
    print("      collider energies: %s --" % COLLIDER_RATE_STATUS)
    for key in ("TW-claim", "BLRRT", "FFS-rebut", "CMS"):
        st, loc, _t = SOURCES[key]
        print("        %-10s %-9s %s" % (key, st, loc[:60]))
    print("      NOT RESOLVED; no refusal rests on it.")
    print()
    print("=" * 79)
    print("M65-5  VERDICT")
    print("=" * 79)
    for cid, link, name, owner, st, cont in COUNTS_ON_THE_MECHANISM:
        print("      %s %-34s %-36s = %-5s %s%s"
              % (cid, link, name, globals()[name], st,
                 "  [contested only]" if cont else ""))
    print()
    print("      THE MECHANISM AS STATED: %s on %s"
          % (MECHANISM_VERDICT[0], ", ".join(MECHANISM_VERDICT[1])))
    print("      THE CONSIDERATION:       %s" % CONSIDERATION_VERDICT)
    print()
    print("      WHAT SURVIVES")
    for name, text in SURVIVES:
        print("        %s: %s" % (name, text))
    print()
    print("      PROPOSED LEDGER ROWS (text only; ledger.py is not edited)")
    for rid, side, claim, st, owner, moves in PROPOSED_ROWS:
        print("        %-9s %-6s %-16s owner %s.%s" % (rid, side, st, owner[0], owner[1]))
        print("          %s" % claim)
        print("          what would move it: %s" % moves)
    print("        not opened: %s" % "; ".join(NOT_OPENED))
    print()
    print("  NOTHING IS REPAIRED.")


# =================================================================== selftest
def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-64s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    def chkrel(label, got, want, rtol):
        ok = abs(got - want) <= rtol * abs(want)
        print("  [%s] %-64s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("massform.py --selftest\n")

    # ---------------------------------------------- imported, never copied
    for modname, names in IMPORTS:
        mod = _MODS[modname]
        for n in names:
            obj = getattr(mod, n, None)
            chk("%s.%s exists" % (modname, n), obj is not None, True)
            if callable(obj) and inspect.isfunction(obj):
                chk("  and is defined in %s" % modname, obj.__module__, modname)
    chk("no owner function is redefined here under its own name",
        [n for n in ("vev", "_capture_row", "holding_terms", "landauer_energy",
                     "symbol_to_Z", "nuclides", "megatons", "baryons_in")
         if n in globals() and inspect.isfunction(globals()[n])], [])

    # ------------------------------------------------------- M's words
    row = [r for r in ledger.RULED_BY_M if r[0] == M_ROW][0]
    text = _norm(" ".join(str(x) for x in row))
    chk("M's mechanism is verbatim in ledger row M-S1A-P1", M_MECHANISM in text, True)
    chk("M's consideration is verbatim in the same row", M_CONSIDERATION in text, True)
    chk("the row names DOCKET 65", "DOCKET 65" in text, True)

    # ------------------------------------------------ the ledger rows asked
    dem = {r[0]: r for r in ledger.DEMAND}
    sup = {r[0]: r for r in ledger.SUPPLY}
    for rid, st, owner in (("D15", ledger.THEOREM, ("excite", "TAIL_RATE_IS_MASS")),
                           ("D16", ledger.THEOREM, ("excite", "DISPLACEMENT_IS_ULTRALOCAL")),
                           ("D18", ledger.THEOREM, ("excite", "ELECTRON_MASS_IS_A_RULER")),
                           ("D19", ledger.THEOREM, ("excite", "FLAT_DIRECTIONS_ARE_INERT")),
                           ("D20", ledger.MEASURED, ("excite", "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18")),
                           ("D25", ledger.OPEN, ("stockgate", "GATE"))):
        chk("ledger %s is %s, owned by %s.%s" % ((rid, st) + owner),
            (dem[rid][2], dem[rid][3]), (st, owner))
    for rid, st, owner in (("S5", ledger.OPEN, ("branelink", "S5_FIGURES_MEASURED")),
                           ("S6", ledger.REFUSED, ("excite", "ROLE1_DOMINATED_BY_OWN_SOURCE")),
                           ("S7", ledger.REFUSED, ("excite", "ROLE2_REBINDS")),
                           ("S8", ledger.REFUSED, ("higgs", "MINIMAL_SCALAR_SATISFIES_NEC")),
                           ("S9", ledger.REFUSED, ("warpfolder", "FLASH_IS_A_RECONSTRUCTION_MECHANISM"))):
        chk("ledger %s is %s, owned by %s.%s" % ((rid, st) + owner),
            (sup[rid][2], sup[rid][3]), (st, owner))
    chk("the proposed ids are free on the board",
        [r[0] for r in PROPOSED_ROWS if r[0] in dem or r[0] in sup], [])
    chk("S9's owner says the flash is not a reconstruction mechanism",
        warpfolder.FLASH_IS_A_RECONSTRUCTION_MECHANISM, False)

    # ------------------------------------------------ READ masses, fixtures
    # FIXTURES: captures/PDG-2026.tsv's own rows, reproduced through
    # higgs._capture_row, never typed into the computation.
    chk("m_e READ 0.510998951 MeV", MASS_MEV["e"], 0.510998951)
    chk("m_p READ 938.272089 MeV", MASS_MEV["p"], 938.272089)
    chk("m_n READ 939.565422 MeV", MASS_MEV["n"], 939.565422)
    chk("m_W READ 80.362 GeV", M_W_GEV, 80.362)
    chk("m_u, m_d READ 2.16, 4.7 MeV", (MASS_MEV["u"], MASS_MEV["d"]), (2.16, 4.7))
    chkrel("m_e/m_p = 5.446170e-4 (the READ finding's ratio)",
           MASS_MEV["e"] / MASS_MEV["p"], 5.446170e-4, 1e-6)
    chkrel("m_N = 938.9187555 MeV (the READ finding's figure)", M_N_MEV, 938.9187555, 1e-12)
    chk("the lightest baryon in the capture is the proton", lightest_baryon()[0], "p")
    chk("N_F counted from the capture's charged leptons", N_F, 3)
    chk("which is the 3 of the READ rule's '3 . 3'", "3 . 3" in SOURCES["RS96-sel"][2], True)

    # ------------------------------------------------------------ M65-1
    chkrel("v from higgs.vev() (higgs's own fixture 246.2196)", vev_gev(), 246.2196, 1e-5)
    y = yukawas()
    chkrel("y_t = sqrt2 x 172.6 GeV / v", y["t"], math.sqrt(2) * 172.6 / vev_gev(), 1e-12)
    chk("y_t is of order one, y_e of order 1e-6",
        (0.9 < y["t"] < 1.1, 1e-6 < y["e"] < 1e-5), (True, True))
    # CONTROL THAT MUST FIRE: a READ mass perturbed moves its Yukawa, exactly
    pert = dict(MASS_MEV, e=MASS_MEV["e"] * 1.01)
    chkrel("CONTROL m_e x 1.01 moves y_e by exactly 1.01",
           yukawas(pert)["e"] / y["e"], 1.01, 1e-12)
    chk("  and moves no other Yukawa",
        all(yukawas(pert)[f] == y[f] for f in CHARGED_FERMIONS if f != "e"), True)
    chk("consideration holds (massive e, u, d force phi != 0)", CONSIDERATION_HOLDS, True)
    chk("CONTROL with e, u, d massless it is NOT ESTABLISHED",
        derive_consideration(consideration_holds(dict(MASS_MEV, e=0.0, u=0.0, d=0.0))),
        "NOT ESTABLISHED")
    chk("the vev is uniform (asked of higgs)", VEV_IS_UNIFORM, True)
    chk("so the consideration discriminates nothing", CONSIDERATION_DISCRIMINATES, False)
    chk("CONSIDERATION VERDICT", CONSIDERATION_VERDICT, "TRUE, AND DISCRIMINATES NOTHING")
    chk("D15 asked of excite", excite.TAIL_RATE_IS_MASS, True)
    chk("D16 asked of excite", excite.DISPLACEMENT_IS_ULTRALOCAL, True)
    chk("D19 asked of excite", excite.FLAT_DIRECTIONS_ARE_INERT, True)
    chk("higgs.py's withdrawn 'cannot be switched on' is not restated (F3, asked)",
        higgs.CANNOT_BE_SWITCHED_ON_IN_ONE_PLACE, False)
    chk("D18 asked of excite, a THEOREM",
        excite.ELECTRON_MASS_IS_A_RULER.startswith("THEOREM"), True)
    chkrel("lambda_h at READ m_h (excite / higgs fixture 1.576976e-18 m)",
           excite.LAMBDA_H_READ_M, 1.576976e-18, 1e-6)
    scan = source_sign_scan()
    chk("D20 source term is negative at every eps < 0 scanned",
        all(s < 0 for e, s in scan if e < 0), True)
    chk("  and positive at every 0 < eps < 1 scanned",
        all(s > 0 for e, s in scan if e > 0), True)
    chk("  so a positive source can only LOWER the vev", SOURCE_CAN_RAISE_VEV, False)
    chk("  exact: 4 eps(2-eps)(1-eps)^2 at eps = -1/10",
        excite.holding_terms(Fraction(-1, 10))[0],
        4 * Fraction(-1, 10) * (2 + Fraction(1, 10)) * (1 + Fraction(1, 10)) ** 2)
    chkrel("D20 source/field x eps -> 2 at eps = 1e-9",
           float(excite.holding_ratio(Fraction(1, 10 ** 9)) * Fraction(1, 10 ** 9)), 2.0, 1e-8)
    chk("C1 FIELD_SWITCHED_ON_BY_ARRIVAL", FIELD_SWITCHED_ON_BY_ARRIVAL, False)
    chk("CONTROL C1 flips if the field were absent before arrival",
        field_switched_on_by_arrival(present=False), True)
    chk("CONTROL C1 flips if D16 failed (a sourceless change)",
        field_switched_on_by_arrival(d16=False), True)
    chk("Higgs quantum lifetime, one significant figure (excite refusal 6)",
        excite.one_sig(excite.QUANTUM_LIFETIME_S), "2e-22")

    # ------------------------------------------------------------ M65-2
    chk("payload is stock.py's own default, asked", PAYLOAD_KG, 70.0)
    chk("composition IS stock.HUMAN (same object)", COMPOSITION is stock.HUMAN, True)
    chk("Z READ from AME2020 via gravity: O 8, Zn 30", (Z_OF["O"], Z_OF["Zn"]), (8, 30))
    chkrel("listed fraction 0.9999231 (H-LIST)", COUNTS["listed"], 0.9999230998799999, 1e-12)
    chk("N_p = N_e: neutral atoms", COUNTS["N_p"], COUNTS["N_e"])
    chkrel("B - L = N_n", COUNTS["B_minus_L"], COUNTS["N_n"], 0)
    # INDEPENDENT CONTROL: warpfolder's M/m_p counts baryons with no composition
    ratio = COUNTS["B"] / warpfolder.baryons_in(PAYLOAD_KG)
    chk("B against warpfolder's M/m_p lies within 1 %", 1.0 < ratio < 1.01, True)
    pm = payload_masses()
    chkrel("the bookkeeping closes exactly on the listed payload",
           pm["nucleon rest"] + pm["electron rest"] - pm["binding (closure)"],
           pm["listed payload"], 1e-12)
    chk("binding is positive and under 1 % (nuclear, residual strong)",
        0 < pm["binding (closure)"] / PAYLOAD_KG < 0.01, True)
    vp, vn = valence_fractions()
    chkrel("naive valence proton (2x2.16 + 4.7)/938.272089", vp,
           (2 * 2.16 + 4.7) / 938.272089, 1e-12)
    chkrel("naive valence neutron (2.16 + 2x4.7)/939.565422", vn,
           (2.16 + 2 * 4.7) / 939.565422, 1e-12)
    # the READ finding's recomputations, reproduced
    chk("six-quark sum, FLAG 2+1+1 = 0.3066 (READ finding's recomputation)",
        round(float(coupling_sum(Fraction(F_LIGHT["FLAG 2+1+1"]))), 4), 0.3066)
    chk("six-quark sum, FLAG 2+1 = 0.2944", round(float(coupling_sum(Fraction(F_LIGHT["FLAG 2+1"]))), 4), 0.2944)
    chk("f_l FLAG 2+1+1 = 10.9 % (101.9/938.92, READ dispute text)",
        round(100 * F_LIGHT["FLAG 2+1+1"], 1), 10.9)
    # THE ALGEBRA, EXACT: 3 (2/27)(1 - f) + f = 2/9 + 7/9 f for every rational f
    chk("3 x (2/27)(1-f) + f == 2/9 + (7/9) f, exact, 200 rationals",
        all(svz_heavy_sum(Fraction(k, 199)) + Fraction(k, 199)
            == coupling_sum(Fraction(k, 199)) for k in range(200)), True)
    chk("  and 2/9 + 7/9 x 1 = 1: the sum is 1 when f_l = 1", coupling_sum(Fraction(1)), 1)
    chk("the 2+1+1 recomputation lies within 1 sigma of Hoferichter's 0.305(9)",
        abs(float(coupling_sum(Fraction(F_LIGHT["FLAG 2+1+1"]))) - 0.305) < 0.009, True)
    rows = share_rows()
    chk("the heavy-quark coupling rows are labelled CONTESTED as mass",
        all(r[1] == "CONTESTED as mass" for r in rows if "coupling" in r[0]), True)
    chk("no row is a sum across measures (one electron row, the rest nucleon)",
        [r[0].split(":")[0] for r in rows].count("electrons (all Higgs-given, H-TREE)"), 1)
    chk("electron share is 3.01e-4", round(rows[0][2], 6), 0.000301)
    chk("largest READ-only reading is under one half", HIGGS_SHARE_BOUND_READ < 0.5, True)
    chk("largest reading of all is under one half", HIGGS_SHARE_BOUND_ALL < 0.5, True)
    chk("C2 HIGGS_SUPPLIES_MOST_ATOMIC_MASS", HIGGS_SUPPLIES_MOST_ATOMIC_MASS, False)
    chk("C2 does NOT rest on a CONTESTED figure alone", C2_CONTESTED_ONLY, False)
    # CONTROL: a hypothetical sigma term above half of m_N flips the bound
    fake = [r if "FLAG 2+1+1" not in r[0] or "sigma" not in r[0]
            else (r[0], r[1], 0.6, r[3]) for r in rows]
    chk("CONTROL a sigma-term row at 0.6 would lift the bound above 1/2",
        higgs_share_bound(fake) >= 0.5, True)

    # ------------------------------------------------------------ M65-3
    E = rest_energy_j()
    chkrel("Mc^2 at 70 kg (warpfolder.rest_energy_j)", E, 70.0 * 299792458.0 ** 2, 1e-15)
    chk("T_CMB asked of permute", T_CMB, 2.7255)
    chkrel("Landauer at 310 K = 2.967e-21 J (READ finding's arithmetic)",
           nopath.landauer_energy(1.0, 310.0), 2.967e-21, 1e-3)
    chkrel("  = 0.01852 eV", nopath.landauer_energy(1.0, 310.0) / 1.602176634e-19, 0.01852, 1e-3)
    chkrel("Bekenstein 70 kg, R = 1 m = 1.80e45 bits (READ finding)",
           bekenstein_bits(), 1.80e45, 3e-3)
    chkrel("Bekenstein 70 kg, R = 0.875 m = 1.58e45 bits", bekenstein_bits(R=0.875),
           1.58e45, 3e-3)
    chkrel("the two counts' ratio equals the closed form with no M",
           bekenstein_bits() / landauer_bits(), bek_over_landauer_closed(), 1e-12)
    chkrel("  and is the same at 1 kg and at 1e6 kg",
           bekenstein_bits(rest_energy_j(1.0)) / landauer_bits(rest_energy_j(1.0)),
           bekenstein_bits(rest_energy_j(1e6)) / landauer_bits(rest_energy_j(1e6)), 1e-12)
    chkrel("break-even radius makes the ratio exactly 1",
           bek_over_landauer_closed(R=break_even_radius_m()), 1.0, 1e-12)
    chk("Landauer prices erasure only (asked of nopath)", nopath.LANDAUER_IS_THE_WEAKER_HALF, True)
    chk("C4 INFORMATION_HAS_INTRINSIC_ENERGY", INFORMATION_HAS_INTRINSIC_ENERGY, False)
    chk("the human-information figures are NOT-FOUND and unused",
        (SOURCES["Braunstein"][0], SOURCES["Leicester"][0], QUOTES_A_HUMAN_INFORMATION_CONTENT),
        ("NOT-FOUND", "NOT-FOUND", False))

    # ------------------------------------------------------------ M65-4
    chk("every Yukawa term carries (B, L) = (0, 0)",
        all(term_charge(t) == (0, 0) for t in YUKAWA_TERMS.values()), True)
    chk("C3 HIGGS_COUPLING_CREATES_FERMIONS", HIGGS_COUPLING_CREATES_FERMIONS, False)
    chk("the 't Hooft vertex carries Delta B = Delta L = N_F (READ rule)",
        THOOFT_DELTA_B_L, (Fraction(N_F), N_F))
    # CONTROL: a term that is not a bilinear does carry charge
    chk("CONTROL a lone quark field carries B = 1/3",
        term_charge((("Q", +1), ("H", +1))), (Fraction(1, 3), 0))
    chk("mu_min is 56Fe (AME2020, measured)", (MU_MIN[1], MU_MIN[2]), ("Fe", 56))
    chk("mu_min lies below m_p (bound nucleons are lighter)", MU_MIN[0] < MASS_MEV["p"], True)
    fl = pair_floor_j() / E
    chk("the pair floor lies between 1.99 and 2 Mc^2", 1.99 < fl < 2.0, True)
    chk("MASS FORMS WITH B, L CONSERVED WITHOUT ANTIMATTER",
        MASS_FORMS_FROM_ENERGY_WITH_BL_CONSERVED_WITHOUT_ANTIMATTER, False)
    aw, g = alpha_w()
    chkrel("alpha_W = g^2/4pi from READ m_W and higgs.vev()", aw,
           (2 * 80.362 / vev_gev()) ** 2 / (4 * math.pi), 1e-12)
    chkrel("the two exponent forms agree (alpha_W = g^2/4pi)",
           log10_suppression(), log10_suppression_g(), 1e-12)
    # CONTROL: m_W up 1 % moves alpha_W by exactly 1.01^2
    chkrel("CONTROL m_W x 1.01 moves alpha_W by 1.0201",
           alpha_w(M_W_GEV * 1.01)[0] / aw, 1.0201, 1e-12)
    # the READ findings' own arithmetic, reproduced
    chk("Tye-Wong: alpha_W = 1/29.7 gives 10^-162.09",
        round(log10_suppression(1 / 29.7), 2), -162.09)
    chk("  and 1/30 gives 10^-163.73 -- the p.2 pairing is 1.6 decades off",
        round(log10_suppression(1 / 30.0), 2), -163.73)
    chk("Tye-Wong eq. (1.2): 4.75 x 1.91 = 9.07, not 9.11",
        round(TW_PREFACTOR_TEV * sum(TW_B_TERMS), 2), 9.07)
    chk("  the prefactor is rounded: 9.11/1.91 = 4.770",
        round(E_SPH_TEV["Tye-Wong, pure SU(2)"] / sum(TW_B_TERMS), 3), 4.770)
    chk("implied B = 1.91 lies inside KM's range",
        B_KM_RANGE[0] < sum(TW_B_TERMS) < B_KM_RANGE[1], True)
    chk("FFS: pi x 9080/80.4 gives 10^-154.1 (printed 10^-155)",
        round(-math.pi * 9080 / 80.4 / math.log(10), 1), -154.1)
    chk("FFS: 80 log10(1/(4 pi)^2) = -175.9", round(80 * math.log10(1 / (4 * math.pi) ** 2), 1), -175.9)
    chkrel("18 alpha_W^5 is exactly 18 x alpha_W^5 at this file's alpha_W",
           symmetric_rate_over_t4(), RATE_COEFF_SYMM * aw ** 5, 1e-15)
    chk("our alpha_W lies inside [1/30, 1/29] -- the sources' range",
        1 / 30 < aw < 1 / 29, True)
    chkrel("E_sph formula x implied B lies within 1 % of the READ 9.08",
           esph_formula_tev(sum(TW_B_TERMS)), 9.08, 1e-2)
    chk("transitions = ceil(B/3)", transitions_needed(), math.ceil(COUNTS["B"] / 3))
    chkrel("extra leptons = N_n (B - L conservation)", extra_leptons(), COUNTS["N_n"], 1e-12)
    chk("H-FLAV sub-count is positive (2 N_p > N_n)", electron_family_shortfall() > 0, True)
    chk("above T_c: heating restores the symmetry (asked of warpfolder)",
        warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY, True)
    chk("  so the hot route has no Yukawa masses", HOT_ROUTE_HAS_YUKAWA_MASSES, False)
    chk("T_c is read as 'approximately zero' vev, not exact zero",
        ("approximately zero" in SOURCES["DRT-vev"][2], CLAIMS_EXACT_ZERO_VEV_ABOVE_TC),
        (True, False))
    chk("collider rate CONTESTED, never resolved",
        (COLLIDER_RATE_STATUS, RESOLVES_COLLIDER_DISPUTE), ("CONTESTED", False))
    chk("the Tye-Wong claim is held as CONTESTED", SOURCES["TW-claim"][0], "CONTESTED")

    # ------------------------------------------------------------ M65-5
    chk("MECHANISM VERDICT", MECHANISM_VERDICT, ("REFUSED", ["C1", "C2", "C3", "C4"]))
    vals = mechanism_values()
    # CONTROL: all links holding -> STANDS
    chk("CONTROL every count reversed -> STANDS",
        derive_verdict({k: True for k in vals}), ("STANDS", []))
    # each count alone suffices: only it failing -> REFUSED resting on it alone
    for k in sorted(vals):
        only = {j: (j != k) for j in vals}
        chk("CONTROL only %s failing -> REFUSED on %s alone" % (k, k),
            derive_verdict(only), ("REFUSED", [k]))
    # a CONTESTED figure alone never carries a refusal
    for k in sorted(vals):
        only = {j: (j != k) for j in vals}
        chk("CONTROL only %s failing, and contested-only -> OPEN, not REFUSED" % k,
            derive_verdict(only, {k: True}), ("OPEN", [k]))
    chk("no count on the mechanism is contested-only",
        [c for c, v in mechanism_contested().items() if v], [])
    # flipping a pinned boolean flips its entry, recomputed from the function
    chk("CONTROL flipping C1's inputs flips C1 in the recomputed verdict",
        derive_verdict(dict(vals, C1=field_switched_on_by_arrival(present=False)),
                       mechanism_contested())[1], ["C2", "C3", "C4"])
    # H-A: every count at A +/- 1/2, and no boolean moves
    for sh in (Fraction(-1, 2), Fraction(1, 2)):
        cc = counts(a_shift=sh)
        b = higgs_share_bound(share_rows(cc)) >= 0.5
        chk("H-A: at A %+s every boolean stands (C2 %s; floor > 1.9 Mc^2)" % (sh, b),
            (b, pair_floor_j(cc) / E > 1.9, extra_leptons(cc) > 0), (False, True, True))
    chk("what survives: reconstruction from stock", RECONSTRUCTION_SURVIVES, True)
    chk("  transit carries no substance (asked)", transit.CARRIES_SUBSTANCE, False)
    chk("what survives: the sphaleron route is priced, not dismissed",
        (SPHALERON_ROUTE_PRICED, DISMISSES_THE_SPHALERON_ROUTE), (True, False))

    # ------------------------------------------- the misquote check, and its control
    bad = check_quotes()
    chk("every quoted fragment and every pinned numeral is in its source", bad, [])
    mutated = dict(SOURCES)
    st, loc, t = mutated["DR-Tc"]
    mutated["DR-Tc"] = (st, loc, t.replace("159.5", "159.9"))
    chk("CONTROL a misquoted T_c is caught", len(check_quotes(sources=mutated)) > 0, True)
    chk("CONTROL a fragment altered in the docstring is caught",
        len(check_quotes(doc=_norm(__doc__).replace("approximately zero", "exactly zero"))) > 0, True)
    chk("pinned values are the ones used",
        (SIGMA_PIN_2P1P1, SIGMA_S_2P1P1, T_C_GEV, E_SPH_TEV[E_SPH_USED]),
        (60.9, 41.0, 159.5, 9.08))
    chk("every source status is in the vocabulary",
        sorted({s for s, _l, _t in SOURCES.values()}),
        ["CITED", "CONTESTED", "NOT-FOUND", "READ"])
    chk("no status anywhere is the retired word",
        any(s == "DECLARED" for s, _l, _t in SOURCES.values())
        or any(r[3] == "DECLARED" for r in PROPOSED_ROWS), USES_THE_RETIRED_STATUS_WORD)

    # ----------------------------------------------- docstring figures, live
    doc = _norm(__doc__)
    missing = [(lab, s) for lab, s in doc_figures() if s not in doc]
    chk("every docstring figure is regenerated from its computation", missing, [])
    chk("CONTROL a stale figure would be caught", "1.8038e46" in doc, False)
    chk("refusals enumerated in the docstring match the flags",
        doc_refusal_numbers(), sorted({n for n, _ in REFUSAL_FLAGS}))
    chk("every refusal flag is unset",
        [n for _k, n in REFUSAL_FLAGS if globals()[n]], [])
    chk("nothing is repaired, no peer is edited", (NOTHING_IS_REPAIRED, EDITS_A_PEER), (True, False))

    print()
    if fails:
        print("  SELFTEST FAILED: %d" % len(fails))
        for f in fails:
            print("    %s: got %r want %r" % f)
        return 1
    print("  SELFTEST OK")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    report()
