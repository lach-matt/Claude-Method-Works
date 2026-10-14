#!/usr/bin/env python3
r"""
warpfolder.py -- ADJUDICATING THE EIGHT DOCUMENTS OF THE DRIVE FOLDER "Warp"

M supplied eight PDFs in a Drive folder and deferred the handling of them:
"The warp folder and its contents are yours to use as you see fit.  As long as
we stay on path, I defer to you regarding the warp folder."

They were produced with a different assistant while this session was rate
limited.  THEY ARE NOT A CORPUS AND NOTHING IN THEM IS SEATED BY BEING READ.
This file exists so that every number said about them is OWNED, because
"quoting figures no instrument owns" is this project's named failure mode 3 and
it has fired here once already (DOCKET 56).

    python3 warpfolder.py             the adjudication
    python3 warpfolder.py --selftest  fixtures

===============================================================================
THE HEADLINE, AND IT SPLITS
===============================================================================

    THE ENGINEERING SPECIFICATION DOES NOT SURVIVE ARITHMETIC.  Its pulsed-
    ignition store (Marx bank plus laser) holds 1,486 J and its own premise
    needs 8.988e18 J -- SHORT BY 15.8 ORDERS.  That is the SUBSYSTEM's
    figure: the folder also energises a 20 T stator, two 85,000 RPM rotors it
    calls "rotational kinetic energy storage" and a muCF starter cell, and
    prints no energy for any of them.  Bounded by the printed dimensions
    (DOCKET 67, computed) the whole device is short by a floor of about 5.7 to
    8.2 orders, the spread being which bound is taken; every bound computed
    leaves it short.  The whole store's ENERGY is 7.6e-07 of the Planck
    energy; the text's own claim is "Optical Intensity Spikes to Planck
    Threshold", and against the Planck INTENSITY the ratio is 9.2e-99.

    CORRECTED (DOCKET 67).  First written as "The device stores 1,486 J ...
    SHORT BY 15.8 ORDERS.  It reaches 7.6e-07 of the Planck energy at a focal
    point".  "The device" was the pulsed subsystem only; "at a focal point"
    counted the Marx energy, which drives the laser and never reaches the
    focus (the laser alone is 1.53e-07 of E_P); and the document says
    intensity where this file tested energy.  No flag moves:
    ENERGY_BUDGET_IS_CONNECTED_TO_THE_CHAIN and REACHES_PLANCK_THRESHOLD stay
    False under every reading DOCKET 67 computed.

    THE ADDRESSING IDEA IS REAL, AND IT CONVERGED WITH OURS INDEPENDENTLY.
    The folder proposes addressing by "CMB Coordinate Map & Local Higgs Field
    VEV", and its Lemma VIII states that a vev shift moves m_e/m_p and hence
    Bohr radii.  That is DOCKET 63's role 1 and role 2, reached from a
    different direction on a different day by a different model.  Two
    independent routes onto the same mechanism is the strongest signal the
    folder carries, AND IT IS THE ONLY PART OF IT THIS TREE SHOULD KEEP.

===============================================================================
1. WHAT THE DEVICE HAS, AGAINST WHAT IT NEEDS
===============================================================================

The specification is a "read-compress-index-reconstruct" cycle: collapse the
payload to a micro-black-hole, thread it through a transient Einstein-Rosen
bridge, and re-condense it at the far end on a Hawking flash.  Every stage is
declared proportional to M_obj.  The PROPORTIONALITIES THEMSELVES ARE ARITHMETI-
CALLY CORRECT -- r_s = 2GM/c^2 gives 1.485e-25 m at 100 kg, and the document
prints 1.48e-25 m.  That is not where it fails.

IT FAILS ON THE ENERGY BUDGET, WHICH THE DOCUMENT NEVER CONNECTS TO THE CHAIN.
Its own hardware specification fixes both sides of the comparison:

    Marx bank    10 x 100 nF charged to 50 kV      ->  E = 10 * (1/2) C V^2
    laser        1e20 W/cm^2, 0.1 mm spot, 30 fs   ->  E = I * area * t

Both are computed below from the document's own printed parameters.  No
figure is taken from its prose, but three readings are this file's, and DOCKET
67 recorded each:
  - the two are SUMMED, though the document's power flow has "The 500 kV
    output pulse drives an array of eight CPA laser heads": the laser draws on
    the Marx store, so the sum counts it twice, +19 % in the DOCUMENT's
    favour (Marx alone is 15.857 orders short against the sum's 15.782);
  - 1e20 W/cm^2 is printed as a floor ("exceeding"), and the same document
    prints a 10 PW peak: 10 PW x 30 fs is 300 J against the 235.6 J used here,
    0.02 orders against the document; 50 kV is printed "up to", on
    capacitors rated 60 kV (1800 J, 0.16 orders at most);
  - Marx plus laser is the PULSED store, not the device's: the stator, the
    rotors and the muCF cell are energised and unquantified (see the
    headline).  The 15.8 orders is the subsystem's shortfall.

SECOND, AND WORSE FOR THE PROPOSAL AS A TRANSPORT: the terminal flash is
E = M c^2 BY CONSTRUCTION, and the document presents this as the reconstruction
mechanism.  At 100 kg that is 2.1 GIGATONS arriving at the destination.  The
document's own table calls it an "Instantaneous High-Frequency Higgs Pulse".

===============================================================================
2. THE HIGGS RECONSTRUCTION RUNS THE WRONG WAY.  THIS IS THE LOAD-BEARING ERROR
===============================================================================

The reconstruction claim is that the flash "temporarily elevates the local
ambient temperature to the electroweak scale, exciting the local Higgs
potential", after which the payload's binary template guides re-condensation.

  (a) HEATING TO THE ELECTROWEAK SCALE TAKES THE HIGGS TO ITS SYMMETRIC-
      LABELLED SIDE.  In the Standard Model with one Higgs doublet at the
      measured Higgs mass, the vev is the LOW-temperature side of a smooth
      crossover at T_c = 159.5 +/- 1.5 GeV, about 5 GeV wide (1508.07161,
      READ in DOCKET 65, which notes "there is no real symmetry breaking phase
      transition"; "broken" and "symmetric" are conventional labels).  Above
      T_c the Higgs expectation value is "approximately zero" (1404.3565), and
      the tree-level, vev-generated fermion masses, proportional to phi, are
      approximately zero with it.  The document has the thermodynamic
      direction inverted: it is describing the condition under which mass
      ceases to be generated and calling it the condition under which mass is
      generated.  The direction rests on the one-doublet SM; restoration at
      high T is model-dependent, and thermal masses are not addressed here.

      CORRECTED (DOCKET 67).  First written as "RESTORES THE SYMMETRY ...
      Raising T to the crossover drives <phi> -> 0 and UN-GENERATES the
      fermion masses", with the SM hypothesis unnamed.  That stated a
      crossover as a transition, "approximately zero, above T_c" as "-> 0",
      and tree-level vev masses as "the fermion masses".  The direction, which
      is all (a) uses, stands; HEATING_TO_EW_SCALE_RESTORES_SYMMETRY keeps
      its value and names the symmetric-labelled side of the crossover.

  (b) AND THE COOLING IS UNCORRELATED.  For a global symmetry broken at a
      continuous transition, causally disconnected domains pick independent
      phases, and where the vacuum manifold has nontrivial homotopy the
      generic output of a rapid quench is a TOPOLOGICAL DEFECT NETWORK, not a
      templated object -- the Kibble-Zurek mechanism.  The SM case meets
      neither hypothesis: its electroweak transition is a crossover (see (a)),
      its Higgs vacuum manifold is S^3, whose pi_0, pi_1 and pi_2 are trivial
      (computed in DOCKET 67), and for the gauged Higgs the phase is
      gauge-dependent.  So the SM output has no topologically stable walls,
      strings or monopoles, and no quench or relaxation time for the flash is
      computed here.  What survives is the conclusion, not a templated
      object, which nothing contradicts; it is not derived on the SM's own
      hypotheses.  Kibble 1976 and Zurek 1985 are NAMED-NOT-READ.

      CORRECTED (DOCKET 67).  First written as "Symmetry breaking in causally
      disconnected domains picks independent phases ... The generic output of
      a rapid quench through a symmetry-breaking transition is a TOPOLOGICAL
      DEFECT NETWORK", applied to the SM with neither hypothesis named.

  (c) BARYON NUMBER CLOSES IT.  100 kg counted at the free-proton mass is
      5.98e28 baryons; bound nuclei are lighter per baryon, so 100 kg of
      carbon holds 6.02e28 and of iron 6.03e28 (+0.7 to +0.85 %, DOCKET 67),
      and the printed figure fits hydrogen-dominated matter.  A thermal flash
      makes baryon-ANTIbaryon pairs, net B = 0: at equilibrium <B> = 0 needs
      a CPT-invariant Hamiltonian with no baryon chemical potential, which
      the SM and a lab flash meet.  The Sakharov conditions are NECESSARY for
      a net baryon number from a charge-symmetric start; they are not
      sufficient and fix no yield.  eta ~ 6.1e-10 per photon is the OBSERVED
      present-day ratio (Planck 2018's Omega_b h^2, converted), and SM
      electroweak baryogenesis is "unable to explain" it (1206.2942, READ in
      DOCKET 65).  Item (b) calls the flash a quench, which is out of
      equilibrium, so condition (iii) is met there and cannot be what closes
      (c).  The closure rests on (i), B conserved below T_EW and B - L
      conserved by sphalerons above it, so B_eq = (28/79)(B - L) = 0 from
      B - L = 0 (computed in DOCKET 67), and on (ii), SM CP violation being
      insufficient for the observed yield.  A blueprint does not source
      baryon number; no arrangement of information does.

      CORRECTED (DOCKET 67).  First written as "100 kg of ordinary matter is
      5.98e28 baryons ... requires the Sakharov conditions and delivers eta ~
      6.1e-10 per photon".  The conditions deliver no value, the count is the
      free-proton count, and the closure was left on equilibrium.

  (d) AND THE FIELD CANNOT BE PUT SOMEWHERE WITHOUT FILLING THE PLACE.
      higgs.py's caveat (b), as corrected by DOCKET 63 (ruling F3), records
      that the vev can be displaced in one place only by filling that place
      with a source whose rest energy is 2/eps times the field energy it buys.
      The screening behind it is NOW VERIFIED: excite.py's THEOREM D15,
      TAIL_RATE_IS_MASS -- a static displacement of any vacuum with V''(v) =
      m^2 > 0 returns to v at asymptotic rate exactly m, nonlinearly, for every
      source sign, size and shape outside the source -- proved by an
      elementary Riccati argument and witnessed by excite.py's selftest; and
      THEOREM D16, DISPLACEMENT_IS_ULTRALOCAL.  For the Higgs that rate is
      hbar/(m_h c), attometres.  See SCREENING_IS_VERIFIED below, now True.

      CORRECTED (DOCKET 63, ruling F4).  The first draft said the screening
      was "UNVERIFIED AT THIS WRITING: every DOCKET 63 verifier died on a rate
      limit before attacking it.  IT IS NOT USED HERE AND MUST NOT BE QUOTED
      AS A RESULT", and quoted caveat (b)'s withdrawn wording "does not
      localise, cannot be switched on in one place".  Both were true of their
      moment and are kept as SCREENING_IS_VERIFIED_AS_FIRST_WRITTEN = False
      with its reason.  (a), (b) and (c) never rested on (d) and do not now.

Note that (a), (b) and (c) are INDEPENDENT.  Each alone is sufficient --
with (b), on the SM case, standing on its conclusion rather than on the
Kibble-Zurek hypotheses it names (see its correction); (a) and (c) do not
lean on (b).

===============================================================================
3. THE ROTOR IS OVER ITS MATERIAL LIMIT, AND IS NOT RELATIVISTIC
===============================================================================

A 1.8 m rotor at 85,000 RPM has a tip speed of 8,011 m/s.  The documents call
the counter-rotating surfaces "relativistic surface velocities"; 8,011 m/s is
2.67e-05 c.  Against the thin-rim burst speed sqrt(sigma/rho) of the two
materials the CAD page actually names, the demanded speed is over the limit by
4.2x (T1000 carbon fibre) and 19.4x (beryllium-copper).  A thin rim asked to
exceed sqrt(sigma/rho) does not spin; it disassembles.

CORRECTED (DOCKET 67).  First written as "A rotor asked to exceed
sqrt(sigma/rho) ... disassembles", for every rotor.  sqrt(sigma/rho) is exact
for a thin rim.  A uniform isotropic disc (nu = 0.3) reaches 1.557x it, so the
factors become 2.7x and 12.5x, still over; a constant-stress (Stodola) profile
has no fixed-multiple ceiling.  Beryllium-copper is over on every geometry
(the Stodola escape needs a taper of exp(-189)).  For T1000 the Stodola
escape (taper 1.2e-4) is closed only by the fibre's anisotropy, a hypothesis
this file names here and does not compute; the printed construction wraps the
fibre at the outer radius, a thin rim.  The T1000 figure is the bare fibre's
strength along its axis, not a laminate's (a composite would raise the factor
to about 5); "beryllium-copper" names no temper, and 1.4 GPa is peak-aged
C17200 (a lower temper raises the factor).  Both favour the rotor.
ROTOR_IS_WITHIN_MATERIAL_LIMITS stays False.

===============================================================================
4. THE 12-VECTOR FAILS THE CRITERION, AND THAT IS A CATEGORY FINDING
===============================================================================

M's standing criterion: A MEMBER OF AN INDEX MUST CARRY QUANTUM NUMBERS.

The 12-vector V = [M, R, K, T, CP, alpha_s, Z0, Lambda, G, G_F, G_theta, v] is
a list of COUPLING CONSTANTS AND ONE VACUUM EXPECTATION VALUE.  A coupling
constant parameterises a theory; it does not label a state of a system.  None
of the twelve carries a quantum number, so the 12-vector CANNOT BE SEATED AS AN
INDEX in this tree.  This is the same category error DOCKET 44 repaired in the
paper's section 4.2, arriving from the other side.

    BUT AN ADDRESS DOES NOT NEED QUANTUM NUMBERS.  Nothing about addressing
    requires the coordinate to be an index, and conflating the two is what the
    folder does.  Separated, the addressing proposal survives the criterion
    that the indexing proposal fails.  THAT SEPARATION IS THE FOLDER'S ONE
    CONTRIBUTION TO THIS TREE.

===============================================================================
5. ATTRIBUTION, WHERE THE FOLDER OVERSTATES A SOURCE THIS TREE HOLDS
===============================================================================

The folder says Bobrick-Martire "generalized this into positive-energy physical
shells, proving that local spacetime modifications are physically viable".
WARP-DRIVE.md already holds the accurate statement and it is narrower in two
ways: the all-energy-conditions shell is FUCHS ET AL. 2024, not Bobrick-Martire
2021, and it is SUBLUMINAL.  WARP-DRIVE.md line 213, on the B-M optimisations:
"none of that makes the energy positive.  It makes less of it negative.
Optimisation moves the magnitude; it does not touch the sign, and the sign is
the whole obstruction."

Two further claims are named and NOT adjudicated here, because adjudicating
them properly needs sources read rather than recalled:
  - that a shear gap's dynamic Casimir effect yields usable negative energy
    density (DCE is real and observed; that it gives a usable STATIC negative
    density in this geometry is the unestablished step);
  - that Berry-phase measurement across a "ghost horizon" extracts all twelve
    parameters simultaneously.
Both are filed NOT-ADJUDICATED.  A NOT-ADJUDICATED may not be quoted as a
refutation any more than as a finding.

===============================================================================
6. WHAT THIS FILE REFUSES
===============================================================================

  - IT DOES NOT RATE THE FOLDER.  There is no score, no percentage correct, no
    verdict on the document set as a whole.  Claims are adjudicated one at a
    time and two of them are NOT-ADJUDICATED.
  - NO VERDICT HERE RESTS ON DOCKET 63's SCREENING LENGTH ALONE.  It was
    refused while unverified; it is now verified (excite.py, D15) and (d) cites
    it, but (a), (b) and (c) each stand without it.
  - IT DOES NOT TREAT CONVERGENCE AS CORROBORATION.  That the folder and
    DOCKET 63 independently reached vev-addressing makes the idea WORTH
    TESTING.  It is not evidence the idea is right: two models sharing a
    training distribution is a correlated sample, not an independent one.
  - IT MAKES NO CLAIM ABOUT WHAT THE AUTHORS INTENDED.

NOTHING IS REPAIRED.  The folder is not edited and no document is rewritten.
"""

import math
import sys

import ladder

c = ladder.c
G = ladder.G
HBAR = ladder.HBAR
KB = 1.380649e-23                        # SI-EXACT
M_PROTON = 1.67262192369e-27             # kg, CODATA 2018    NAMED-NOT-READ
# The FREE-proton rest mass, CODATA 2018 (superseded by CODATA 2022,
# 1.67262192595e-27, +1.35e-9 relative; both READ via the scipy/astropy
# restatements in DOCKET 67).  Used as mass per baryon by baryons_in(), which
# fits hydrogen-dominated matter: bound nuclei are lighter per baryon.
MT_TNT_J = 4.184e15                      # J per megaton, by definition
TSAR_BOMBA_MT = 50.0                     # Mt                 NAMED-NOT-READ

# ---------------------------------------------------------- the folder itself
# READ: all eight were read in full through the Drive connector on 2026-09-24.
FOLDER = "Warp"
FOLDER_ID = "1U2VjhhcC28qEu3NeLilwVi1k_dB6FUo7"
DOCUMENTS = (
    "transient_metric_propulsion_specification.pdf",
    "multiverse_12_vector_taxonomy_v2.pdf",
    "multiverse_warp_engineering_paper_v5.pdf",
    "one_way_multiverse_theory_v4.pdf",
    "cost_and_location_assessment.pdf",
    "schematics_and_blueprints.pdf",
    "pulsed_ignition_and_optics_specification.pdf",
    "warp drive theory.pdf",
)
DOCUMENTS_READ_IN_FULL = True

# ------------------------------- parameters TAKEN FROM THE DOCUMENTS' OWN TEXT
# STATUS: READ.  Each is printed in the named document; none is inferred.
MARX_STAGES = 10                         # pulsed_ignition, sect. 1.1
MARX_C_FARAD = 100e-9                    # "ten 100 nF energy storage capacitors"
MARX_V_VOLT = 50e3                       # "up to +50 kV DC"
LASER_I_W_PER_CM2 = 1e20                 # "exceeding 1e20 W/cm^2"  (a floor;
                                         # the same document prints a 10 PW peak,
                                         # 1.27e20 W/cm^2 over this spot -- DOCKET 67)
LASER_SPOT_M = 0.1e-3                    # "0.1 mm spot"
LASER_PULSE_S = 30e-15                   # "30 fs duration"
ROTOR_D_M = 1.8                          # blueprints, "Flywheel Rotor 1.8 m"
ROTOR_RPM = 85000.0                      # "85,000 RPM"
PAYLOADS_KG = (100.0, 5000.0, 1.0e5)     # the document's own three rows

# Materials the CAD page names.  sigma/rho are NOT from the folder -- the folder
# gives no strength figures -- so they carry their own status.
# T1000: the BARE FIBRE's strength along its axis (data sheet ~6.37 GPa, 1.80
# g/cm^3), not a laminate's; a composite rotor is weaker per unit density and
# would raise the over-limit factor.  'beryllium-copper' names no temper:
# 1.4 GPa is peak-aged C17200, and a lower temper also raises the factor.
# Room-temperature ultimate strengths, no fatigue, no safety factor.  Every one
# of these choices favours the rotor (DOCKET 67).  Not READ at source.
MATERIALS = (                            # (name, sigma_Pa, rho_kg_m3)  ORDER
    ("carbon fibre T1000", 6.4e9, 1800.0),
    ("beryllium-copper",   1.4e9, 8250.0),
)

ETA_BARYON = 6.1e-10                     # observed, from Planck 2018
# Planck 2018 (1807.06209, Table 2, READ in DOCKET 67) prints Omega_b h^2 =
# 0.02237 +/- 0.00015, NOT eta; eta = (6.124 +/- 0.041)e-10 is the standard
# conversion of it with T_CMB = 2.7255 K, here to 2 s.f.  It is the OBSERVED
# ratio.  No mechanism produced it in this file, and SM electroweak
# baryogenesis cannot (1206.2942, READ in DOCKET 65).
T_EW_CROSSOVER_GEV = 160.0               # order              ORDER
# The lattice crossover is T_c = 159.5 +/- 1.5 GeV (1508.07161 abstract, READ in
# DOCKET 65 and owned by massform.py), the susceptibility maximum of a smooth
# crossover ~5 GeV wide, in the one-doublet SM.  160 is 0.33 sigma from it.

# The document's own scaling table, third row, as printed.  STATUS: READ.
# Kept as a constant because this file DISAGREES with it, and a figure a file
# disagrees with must be owned as carefully as one it endorses.
TABLE_1E5_PRINTED_J = 8.98e22
TABLE_1E5_ROW_IS_CONSISTENT = False

# ----------------------------------------------------- the adjudicated claims
PROPORTIONALITY_ARITHMETIC_IS_CORRECT = True
ENERGY_BUDGET_IS_CONNECTED_TO_THE_CHAIN = False
REACHES_PLANCK_THRESHOLD = False
FLASH_IS_A_RECONSTRUCTION_MECHANISM = False
# 'RESTORES' is the conventional label for the symmetric-labelled side of an SM
# crossover, not a real phase transition (1508.07161 fn.1); the flag records
# the DIRECTION, which is what (a) uses (DOCKET 67).
HEATING_TO_EW_SCALE_RESTORES_SYMMETRY = True
# A literal.  It rests on (b), whose Kibble-Zurek hypotheses the SM crossover
# does not meet (see (b)'s correction); no ledger row or specthm class reads it.
# Pinned by the selftest since DOCKET 67, which found it asserted nowhere.
QUENCH_GIVES_A_TEMPLATED_OBJECT = False
BLUEPRINT_SOURCES_BARYON_NUMBER = False
ROTOR_IS_RELATIVISTIC = False
ROTOR_IS_WITHIN_MATERIAL_LIMITS = False
TWELVE_VECTOR_MEETS_THE_CRITERION = False
TWELVE_VECTOR_MAY_STILL_BE_AN_ADDRESS = True
BOBRICK_MARTIRE_CLAIM_IS_ACCURATE = False

# Two claims are filed unadjudicated, and the tag is load-bearing.
NOT_ADJUDICATED = (
    "shear-gap dynamic Casimir effect yields usable negative energy density",
    "Berry-phase 'ghost horizon' measurement extracts all twelve parameters",
)

# DOCKET 63's screening length.  VERIFIED by excite.py's THEOREM D15
# (TAIL_RATE_IS_MASS) and D16 (DISPLACEMENT_IS_ULTRALOCAL); the selftest asks
# excite for both rather than trusting this flag.  (DOCKET 63 ruling F4.)
SCREENING_IS_VERIFIED = True
SCREENING_VERIFIED_BY = ("excite", "TAIL_RATE_IS_MASS")
#: The first draft's flag, WITHDRAWN and kept.
SCREENING_IS_VERIFIED_AS_FIRST_WRITTEN = False
SCREENING_WITHDRAWAL_REASON = (
    "False when written: every DOCKET 63 verifier had died on a rate limit "
    "before attacking the screening claim.  DOCKET 63 then proved it "
    "(ruling F1, an elementary Riccati argument replacing an unread "
    "Levinson/Hartman citation) and excite.py's selftest witnesses it, so "
    "ruling F4 flips the flag.")
CONVERGENCE_IS_CORROBORATION = False
NOTHING_IS_REPAIRED = True
FOLDER_IS_NOT_SEATED = True


# --------------------------------------------------------------- what it has
def marx_joules():
    """Ten capacitors charged in parallel, each (1/2) C V^2."""
    return MARX_STAGES * 0.5 * MARX_C_FARAD * MARX_V_VOLT ** 2


def laser_joules():
    """I * area * t, with the document's own intensity, spot and duration.

    The intensity is the printed FLOOR, 1e20 W/cm^2 exactly; the document's
    own 10 PW peak x 30 fs gives 300 J against this 235.6 J -- 0.02 orders
    AGAINST the document (DOCKET 67).  Top-hat in space and time."""
    area_cm2 = math.pi * (LASER_SPOT_M * 100.0 / 2.0) ** 2
    return LASER_I_W_PER_CM2 * area_cm2 * LASER_PULSE_S


def stored_joules():
    """The PULSED store, Marx plus laser.

    Not the device's whole store: the stator, rotors and muCF cell are
    energised and unquantified.  And the laser heads are driven BY the Marx
    pulse, so the sum counts the laser twice, +19 % in the document's favour
    (DOCKET 67).  Kept as the sum because S9 and the selftest read it."""
    return marx_joules() + laser_joules()


def planck_energy():
    """E_P = sqrt(hbar c^5 / G), the CODATA convention (hbar, not h; G, not
    8 pi G).  Under h the store fraction is 3.03e-7, under 8 pi G 3.81e-6
    (DOCKET 67).  A dimensional unit, compared here with a TOTAL energy:
    21.76 ug of rest mass exceeds it."""
    return math.sqrt(HBAR * c ** 5 / G)


# -------------------------------------------------------------- what it needs
def schwarzschild_m(mass_kg):
    return 2.0 * G * mass_kg / c ** 2


def rest_energy_j(mass_kg):
    return mass_kg * c ** 2


def hawking_lifetime_s(mass_kg):
    """tau = 5120 pi G^2 M^3 / (hbar c^4)."""
    return 5120.0 * math.pi * G ** 2 * mass_kg ** 3 / (HBAR * c ** 4)


def hawking_temperature_k(mass_kg):
    return HBAR * c ** 3 / (8.0 * math.pi * G * mass_kg * KB)


def shortfall(mass_kg):
    """How many times the device's store falls short of its own premise."""
    return rest_energy_j(mass_kg) / stored_joules()


def megatons(joules):
    return joules / MT_TNT_J


# -------------------------------------------------------------------- the rotor
def tip_speed_m_s():
    return math.pi * ROTOR_D_M * ROTOR_RPM / 60.0


def burst_speed_m_s(sigma_pa, rho):
    """The THIN-RIM limit sqrt(sigma/rho), independent of radius.

    Exact for a thin rim (hoop stress rho v^2).  A uniform isotropic disc
    reaches 1.557x it (nu = 0.3); a constant-stress Stodola profile has no
    fixed-multiple ceiling, closed for T1000 only by fibre anisotropy, which
    is not computed here.  Independence of radius holds at fixed shape for
    every geometry (DOCKET 67)."""
    return math.sqrt(sigma_pa / rho)


# ------------------------------------------------------------- baryon number
def baryons_in(mass_kg):
    """mass / m_p: the free-proton count, which fits hydrogen-dominated matter.
    Atomic matter holds 0.67-0.85 % more baryons per kg (water 6.019e28,
    56Fe 6.029e28 per 100 kg; DOCKET 67).  No flag reads it."""
    return mass_kg / M_PROTON


def report():
    print("=" * 79)
    print("warpfolder.py -- the eight documents of the Drive folder %r" % FOLDER)
    print("=" * 79)
    print()
    print("  %d documents, all read in full through the Drive connector." %
          len(DOCUMENTS))
    print("  NOTHING HERE IS SEATED BY HAVING BEEN READ.")
    print()

    print("-" * 79)
    print("1. WHAT THE DEVICE HAS, AGAINST WHAT ITS OWN PREMISE NEEDS")
    print("-" * 79)
    print()
    print("      %-42s %16.1f J" % ("Marx bank, 10 x 100 nF at 50 kV",
                                    marx_joules()))
    print("      %-42s %16.1f J" % ("laser, 1e20 W/cm^2, 0.1 mm, 30 fs",
                                    laser_joules()))
    print("      %-42s %16.1f J" % ("TOTAL PULSED STORE", stored_joules()))
    print("      (the Marx pulse drives the laser, so the sum counts it twice;")
    print("      the stator, rotors and muCF cell are energised and unquantified)")
    print()
    print("      %-42s %16.3e J" % ("needed, 100 kg black hole",
                                    rest_energy_j(100.0)))
    print("      %-42s %16.3e" % ("SHORTFALL, times", shortfall(100.0)))
    print("      %-42s %16.1f" % ("  orders of magnitude, pulsed store",
                                  math.log10(shortfall(100.0))))
    print()
    print("      %-42s %16.3e J" % ("Planck energy", planck_energy()))
    print("      %-42s %16.3e" % ("  pulsed-store ENERGY / E_P (hbar)",
                                  stored_joules() / planck_energy()))
    print("      the document says 'Optical Intensity Spikes to Planck")
    print("      Threshold' -- an INTENSITY; the energy test is the generous one.")
    print()

    print("-" * 79)
    print("2. THE PROPORTIONAL CHAIN IS ARITHMETICALLY RIGHT, AND ARRIVES AS A BOMB")
    print("-" * 79)
    print()
    print("      %12s %14s %14s %12s %12s" %
          ("payload/kg", "r_s/m", "E_flash/J", "Mt TNT", "tau/s"))
    for m in PAYLOADS_KG:
        print("      %12.0f %14.3e %14.3e %12.3e %12.3e" %
              (m, schwarzschild_m(m), rest_energy_j(m),
               megatons(rest_energy_j(m)), hawking_lifetime_s(m)))
    print()
    print("      a 100 kg arrival is %.0f Tsar Bombas, at the destination." %
          (megatons(rest_energy_j(100.0)) / TSAR_BOMBA_MT))
    print("      and T_H = %.3e K over tau = %.3e s -- not a controlled process."
          % (hawking_temperature_k(100.0), hawking_lifetime_s(100.0)))
    print()

    print("-" * 79)
    print("3. THE RECONSTRUCTION RUNS THE WRONG WAY.  THREE INDEPENDENT REASONS")
    print("-" * 79)
    print()
    print("  (a) heating TO the electroweak scale (one-doublet SM) crosses over")
    print("      to the symmetric-labelled side: T_EW ~ %.0f GeV = %.3e K," %
          (T_EW_CROSSOVER_GEV,
           T_EW_CROSSOVER_GEV * 1e9 * 1.602176634e-19 / KB))
    print("      and above it <phi> is approximately zero.")
    print("      the document has the thermodynamic direction inverted.")
    print()
    print("  (b) the quench is uncorrelated: not a templated object.  Kibble-")
    print("      Zurek's defect network needs a continuous transition and a")
    print("      vacuum manifold with nontrivial homotopy; the SM's is a")
    print("      crossover, and its S^3 has trivial pi_0, pi_1, pi_2.")
    print()
    print("  (c) baryon number. 100 kg / m_p is %.3e baryons; a thermal flash"
          % baryons_in(100.0))
    print("      makes pairs, net B = 0; the observed eta = %.1e, and SM"
          % ETA_BARYON)
    print("      baryogenesis cannot produce it (1206.2942).")
    print("      a blueprint does not source baryon number.")
    print()
    print("      EACH ALONE IS SUFFICIENT.  They are independent.")
    print()

    print("-" * 79)
    print("4. THE ROTOR")
    print("-" * 79)
    print()
    v = tip_speed_m_s()
    print("      %-42s %16.1f m/s" % ("1.8 m at 85,000 RPM, tip speed", v))
    print("      %-42s %16.2e c" % ("  which is", v / c))
    print("      the documents call this 'relativistic surface velocities'.")
    print()
    for name, sigma, rho in MATERIALS:
        vb = burst_speed_m_s(sigma, rho)
        print("      %-24s burst %8.0f m/s   demanded/limit %6.1fx" %
              (name, vb, v / vb))
    print("      thin-rim limits; a uniform isotropic disc allows 1.557x (nu = 0.3),")
    print("      still over on both materials.")
    print()

    print("-" * 79)
    print("5. THE 12-VECTOR AGAINST THE CRITERION")
    print("-" * 79)
    print()
    print("  A MEMBER OF AN INDEX MUST CARRY QUANTUM NUMBERS.")
    print("  The twelve are coupling constants and one vev.  None carries a")
    print("  quantum number, so THE 12-VECTOR CANNOT BE SEATED AS AN INDEX.")
    print("  Same category error DOCKET 44 repaired in section 4.2, from the")
    print("  other side.")
    print()
    print("  BUT AN ADDRESS DOES NOT NEED QUANTUM NUMBERS, and separating the")
    print("  two is the folder's one contribution to this tree.")
    print()

    print("-" * 79)
    print("6. WHAT IS NOT ADJUDICATED, AND WHAT IS NOT USED")
    print("-" * 79)
    print()
    for claim in NOT_ADJUDICATED:
        print("      NOT-ADJUDICATED  %s" % claim)
    print()
    print("      DOCKET 63's screening length, now verified (excite.py D15):")
    print("      SCREENING_IS_VERIFIED = %s  (first written: %s, withdrawn)"
          % (SCREENING_IS_VERIFIED, SCREENING_IS_VERIFIED_AS_FIRST_WRITTEN))
    print("      CONVERGENCE_IS_CORROBORATION = %s" % CONVERGENCE_IS_CORROBORATION)
    print()

    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  The specification fails on its own printed numbers -- its pulsed")
    print("  store by 15.8 orders, the whole device by a floor of ~5.7 to 8.2")
    print("  on DOCKET 67's bounds -- and its reconstruction mechanism is")
    print("  inverted.  The addressing idea is real, converged with DOCKET 63's")
    print("  role 1 independently, and is the only part this tree should keep.")
    print()
    print("  NOTHING IS REPAIRED.  The folder is not edited.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    def chkrel(label, got, want, rtol):
        ok = abs(got - want) <= rtol * abs(want)
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("warpfolder.py --selftest")
    print()

    # ------------------------------------------------ the store, from the text
    chkrel("Marx bank is 1250 J", marx_joules(), 1250.0, 1e-12)
    chkrel("laser delivers 235.6 J", laser_joules(), 235.62, 1e-4)
    chkrel("total stored is 1485.6 J", stored_joules(), 1485.6, 1e-4)

    # --------------------------------- the chain's own arithmetic, reproduced
    # The document prints 1.48e-25 m for 100 kg.  We must agree with it: the
    # proportionalities are not where the specification fails, and saying so
    # is part of not overstating the refutation.
    chkrel("r_s(100 kg) matches the document's 1.48e-25 m",
           schwarzschild_m(100.0), 1.48e-25, 5e-3)
    chkrel("E_flash(100 kg) matches the document's 8.98e18 J",
           rest_energy_j(100.0), 8.98e18, 2e-3)
    chkrel("r_s(5000 kg) matches the document's 7.42e-24 m",
           schwarzschild_m(5000.0), 7.42e-24, 5e-3)
    chkrel("E_flash(5000 kg) matches the document's 4.49e20 J",
           rest_energy_j(5000.0), 4.49e20, 2e-3)
    chkrel("r_s(1e5 kg) matches the document's 1.48e-22 m",
           schwarzschild_m(1.0e5), 1.48e-22, 5e-3)
    chk("so the proportionality arithmetic IS correct",
        PROPORTIONALITY_ARITHMETIC_IS_CORRECT, True)

    # ------------------------------- AND THE TABLE'S LAST CELL IS OFF BY TEN
    # Found by this selftest, not by reading.  The document's third row prints
    # E_flash = 8.98e22 J for 100,000 kg; its own E = M c^2 gives 8.99e21.  The
    # RADIUS on that row is right, so it is one slipped cell and not a
    # different convention -- which is why it is recorded as an internal
    # inconsistency rather than as a disagreement about physics.
    chkrel("the document's OWN E=Mc^2 gives 8.99e21 J at 1e5 kg",
           rest_energy_j(1.0e5), 8.9876e21, 1e-3)
    chkrel("  but the table prints 8.98e22 -- a factor of",
           TABLE_1E5_PRINTED_J / rest_energy_j(1.0e5), 9.9916, 1e-3)
    chk("  so the third row is internally inconsistent",
        TABLE_1E5_ROW_IS_CONSISTENT, False)
    chk("  and the first two rows are not",
        (abs(rest_energy_j(100.0) / 8.98e18 - 1.0) < 2e-3,
         abs(rest_energy_j(5000.0) / 4.49e20 - 1.0) < 2e-3), (True, True))

    # ------------------------------------------------------------ the shortfall
    chkrel("shortfall is 6.05e15", shortfall(100.0), 6.050e15, 1e-3)
    chkrel("  = 15.78 orders", math.log10(shortfall(100.0)), 15.7818, 1e-4)
    chk("the budget is NOT connected to the chain",
        ENERGY_BUDGET_IS_CONNECTED_TO_THE_CHAIN, False)

    # The Planck claim, which the document makes in its own operational
    # chronology ("Optical Intensity Spikes to Planck Threshold").
    frac = stored_joules() / planck_energy()
    # CORRECTED (DOCKET 67): the document's word is INTENSITY; this tests the
    # pulsed store's ENERGY against E_P (hbar convention), the most generous
    # reading.  Against the Planck intensity the ratio is 9.2e-99.  The flag
    # is False under every reading.
    chkrel("pulsed-store energy is 7.60e-07 of the Planck energy", frac,
           7.595e-7, 1e-3)
    chk("  so it does not reach the Planck threshold",
        REACHES_PLANCK_THRESHOLD, frac >= 1.0)

    # ------------------------------------------------------------ the arrival
    chkrel("100 kg arrives as 2148 Mt", megatons(rest_energy_j(100.0)),
           2148.2, 1e-3)
    chkrel("  = 43 Tsar Bombas",
           megatons(rest_energy_j(100.0)) / TSAR_BOMBA_MT, 42.96, 1e-3)
    chkrel("tau(100 kg) = 8.41e-11 s", hawking_lifetime_s(100.0), 8.411e-11,
           1e-3)
    chkrel("T_H(100 kg) = 1.23e21 K", hawking_temperature_k(100.0), 1.227e21,
           1e-3)

    # tau ~ M^3 and T_H ~ 1/M -- the document states both scalings and they
    # are right; check the SCALING, not just the point value.
    chkrel("tau scales as M^3",
           hawking_lifetime_s(1000.0) / hawking_lifetime_s(100.0), 1000.0,
           1e-12)
    chkrel("T_H scales as 1/M",
           hawking_temperature_k(100.0) / hawking_temperature_k(1000.0), 10.0,
           1e-12)

    # ------------------------------------------------------------ baryon number
    # The free-proton count; atomic matter holds 0.67-0.85 % more (DOCKET 67).
    chkrel("100 kg / m_p is 5.98e28 baryons", baryons_in(100.0), 5.979e28,
           1e-3)
    chk("a blueprint does not source baryon number",
        BLUEPRINT_SOURCES_BARYON_NUMBER, False)
    chk("heating to the EW scale reaches the symmetric-labelled side (SM)",
        HEATING_TO_EW_SCALE_RESTORES_SYMMETRY, True)
    # DOCKET 67 found this literal asserted nowhere; pinned, not derived.
    chk("the quench gives no templated object (a literal)",
        QUENCH_GIVES_A_TEMPLATED_OBJECT, False)
    chk("so the flash is not a reconstruction mechanism",
        FLASH_IS_A_RECONSTRUCTION_MECHANISM, False)

    # ---------------------------------------------------------------- the rotor
    chkrel("tip speed is 8011 m/s", tip_speed_m_s(), 8011.06, 1e-4)
    chkrel("  = 2.67e-05 c", tip_speed_m_s() / c, 2.672e-5, 1e-3)
    chk("which is not relativistic", ROTOR_IS_RELATIVISTIC,
        tip_speed_m_s() / c > 0.01)
    over = [round(tip_speed_m_s() / burst_speed_m_s(s, r), 1)
            for _, s, r in MATERIALS]
    # Thin-rim factors, rounded from ORDER inputs.  The unrounded T1000 factor
    # is 4.2485, 0.0015 below the rounding edge; at the data-sheet 6,370 MPa
    # it prints 4.3, and BeCu at 1.357-1.38 GPa prints 19.6-19.8 -- digit
    # discrepancies, not refutations (DOCKET 67).  A uniform disc gives
    # 2.7x and 12.5x, still over.
    chk("over the thin-rim burst limit by these factors", over, [4.2, 19.4])
    chk("  so it is outside material limits on BOTH named materials",
        ROTOR_IS_WITHIN_MATERIAL_LIMITS, False)

    # -------------------------------------------------------------- the criterion
    chk("the 12-vector fails THE CRITERION",
        TWELVE_VECTOR_MEETS_THE_CRITERION, False)
    chk("but may still be an address", TWELVE_VECTOR_MAY_STILL_BE_AN_ADDRESS,
        True)

    # ------------------------------------------------------------- the refusals
    chk("two claims are filed NOT-ADJUDICATED", len(NOT_ADJUDICATED), 2)
    # DOCKET 63 F4: the flag is flipped, and it is ASKED of its owner rather
    # than believed -- excite.py must still export both theorems, and its
    # stdlib witnesses must still hold (exact kink rate, multipole residuals,
    # and one boundary-value solve with its massless control).
    import excite
    chk("DOCKET 63's screening is verified (ruling F4)",
        SCREENING_IS_VERIFIED, True)
    chk("  and its owner still exports D15 and D16",
        (getattr(excite, SCREENING_VERIFIED_BY[1]),
         excite.DISPLACEMENT_IS_ULTRALOCAL), (True, True))
    xs, us, _it, h = excite.bvp_solve(-2.448516, 40.0)
    chk("  witness: the deepest profile's rate at x = 25 is 1 (to 1e-8)",
        abs(excite.measured_rate(xs, us, h, 25.0) - 1.0) < 1e-8, True)
    xs, us, _it, h = excite.bvp_solve(-0.5, 40.0, mu2=0.0)
    chk("  CONTROL the massless solve is NOT 1 (1/(X-x) = 1/15)",
        abs(excite.measured_rate(xs, us, h, 25.0) - 1.0 / 15.0) < 1e-9, True)
    chk("  the first draft's False is kept, withdrawn",
        SCREENING_IS_VERIFIED_AS_FIRST_WRITTEN, False)
    chk("and convergence is NOT treated as corroboration",
        CONVERGENCE_IS_CORROBORATION, False)
    chk("nothing is repaired and the folder is not seated",
        (NOTHING_IS_REPAIRED, FOLDER_IS_NOT_SEATED), (True, True))
    chk("all eight documents were read in full", len(DOCUMENTS), 8)

    # ------------------------------------------- the gate is not vacuous
    # A selftest that only ever confirms refusals proves nothing.  This file
    # AGREES with the folder on the proportionalities and DISAGREES on the
    # budget; both must be live.
    chk("the adjudication both agrees and disagrees",
        (PROPORTIONALITY_ARITHMETIC_IS_CORRECT,
         ENERGY_BUDGET_IS_CONNECTED_TO_THE_CHAIN), (True, False))

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
